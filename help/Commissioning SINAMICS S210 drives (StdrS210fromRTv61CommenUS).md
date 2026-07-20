---
title: "Commissioning SINAMICS S210 drives"
package: StdrS210fromRTv61CommenUS
topics: 130
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Commissioning SINAMICS S210 drives

This section contains information on the following topics:

- [Guided quick startup](#guided-quick-startup)
- [Parameterization](#parameterization)
- [Rotate &amp; optimize](#rotate-optimize-1)

## Guided quick startup

This section contains information on the following topics:

- [Overview](#overview)
- [Edit mode (online)](#edit-mode-online)
- [Connection to PLC](#connection-to-plc)
- [Application](#application)
- [Limits](#limits)
- [Application settings](#application-settings)
- [I/O configuration](#io-configuration)
- [Telegrams (only offline)](#telegrams-only-offline)
- [Rotate &amp; optimize](#rotate-optimize)
- [Overview](#overview-1)

### Overview

#### Overview

Using "Guided quick startup", you perform the basic settings for the drive in Startdrive that are used to avoid the following detailed settings as far as possible. All drive settings are pre-assigned according to the specific application using these basic settings.

> **Note**
>
> **The significance of Note symbols**
>
> Settings of individual steps may affect the previous settings of other steps. In this case, an appropriate note with the following icon ![Overview](images/149683184779_DV_resource.Stream@PNG-de-DE.png) appears at the active quick startup step. Check and, if necessary, correct the corresponding settings.
>
> Further identifications:
>
> The ![Overview](images/149683193355_DV_resource.Stream@PNG-de-DE.png) icon designates information or a context-sensitive note for users.
>
> The ![Overview](images/149847587083_DV_resource.Stream@PNG-de-DE.png) icon identifies an area of the step where an entry is urgently required.

#### Requirements

- The drive has been completely created and specified in the device configuration.

  Without a complete specification, the guided quick startup cannot be used and a message appears.
- If a control is also used, it must be connected to the drive in the topology view and in the network view. The connection between the devices must also be configured.
- The operating unit is connected to the drive via LAN (physically online).

  There is no active online connection between the drive and the operating unit.
- If project protection is activated:   
  The [function rights](User%20administration%20and%20security.md#access-control) required for the configuration in the quick startup are activated for your user role. User authentication via a login is required.   
  Observe the detailed information under point "[User administration and security](User%20administration%20and%20security.md#overview)".

#### Description of function

You can define the following basic settings in the steps with the same name:

- [Connection to PLC](#connection-to-plc)

  This step indicates that the drive in the project can only be operated together with a controller. Here you specify whether you also want to use Safety Integrated Functions.
- [Application](#application)

  You define the converter control mode in this step. With the "Positioning" control mode activated, make detailed settings, for example the motion type, the measuring unit, encoder settings for the position control or the values for a modulo correction.
- [Limits](#limits)

  The settings in step "Limits" are also dependent on the selected control mode.

  - "Speed control":

    Here, you define the minimum and maximum values of the motor used: Torque, speed, operating times.
  - "Positioning":

    In this case, make the settings for the traversing profile, for alternative ramp-down times, for jerk limitation and/or for traversing range limitation.
- [Application settings](#application-settings)

  Step "Application settings" is only active when the "Positioning" control mode is activated. Here, you make the detailed settings for active or passive homing.
- [I/O configuration](#io-configuration)

  Here, you configure the digital (in some instances failsafe) inputs and outputs.
- [Telegrams](#telegrams-only-offline)

  Based on the selected control mode, the preferred telegrams are suggested here. You can define different telegrams and/or make detailed settings. Telegram settings can only be made offline.
- [Rotate &amp; optimize](#rotate-optimize)

  With this step you optimize the motor in online operation. "One Button Tuning" is available for this purpose.
- [Overview](#overview-1)

  Here you will find a compilation of all settings made after completing the configuration in the guided quick startup.

  - Offline mode: When required, you can load these settings directly to the drive.
  - Online mode: When required, you can load these settings directly into the Startdrive project.

#### Status display after changes

Changes to individual settings affect other settings in the "guided quick startup". Status symbols indicate the change status of the particular step:

| Icon | Meaning |
| --- | --- |
| ![Status display after changes](images/155564453003_DV_resource.Stream@PNG-de-DE.png) | The system defaults in this step are valid. |
| ![Status display after changes](images/151783943947_DV_resource.Stream@PNG-de-DE.png) | The settings made in this step are valid.   The settings were made directly in this step, or are the consequences of settings in another step. |
| ![Status display after changes](images/152995660555_DV_resource.Stream@PNG-de-DE.png) | The program changed the settings in this step. Possible causes are:   - Subsequent changes were made in other steps, which are not automatically valid. - Subsequent changes have been made in the device configuration that affect the original settings.   Check the settings of this step. |

#### Manual navigation

You can navigate between the individual steps using the two navigation buttons:

| Button | Explanation |
| --- | --- |
| ![Manual navigation](images/165979777547_DV_resource.Stream@PNG-en-US.png) | Displays the next quick startup step. However, it must already have been displayed once before. |
| ![Manual navigation](images/165979781899_DV_resource.Stream@PNG-en-US.png) | Shows the last step that was displayed before the current step. |

### Edit mode (online)

#### Operating the guided quick startup in online mode

If you want to work with the guided quick startup in online mode, you need restore points in case commissioning is aborted. Restore points are stored retentively on the memory card of the converter.

Restore points are created automatically when you activate or exit the editing mode and also when you switch from one quick startup step to another step.

> **Note**
>
> **Behavior when the online connection is terminated**
>
> If the connection to the drive is re-established after the online connection has been terminated, the program reverts to the stored data of the last restore point.

#### Requirements

- The drive has been completely created and specified in the device configuration.

  Without a complete specification, the guided quick startup cannot be used and a message appears.
- If a control is also used, it must be connected to the drive in the topology view and in the network view. The connection between the devices must also be configured.
- There is an active [online connection](Configuring%20SINAMICS%20S210%20drives%20%28StdrS210fromRTv61ConfenUS%29.md#establishing-an-online-connection-to-the-target-device) between the drive and the operating unit.
- No other access from another operating unit to the selected drive is active.

#### Activating/exiting the editing mode

Settings in the guided quick startup can be made online only in an "editing mode".

| Display | Status | Description |
| --- | --- | --- |
| ![Activating/exiting the editing mode](images/148900746379_DV_resource.Stream@PNG-de-DE.png) | The editing mode is not yet activated. | Proceed as follows to activate editing mode:   - In the toolbar of the step, click on the button ![Activating/exiting the editing mode](images/154401807627_DV_resource.Stream@PNG-en-US.PNG).    - Or - - In the step below, click the button ![Activating/exiting the editing mode](images/154401807627_DV_resource.Stream@PNG-en-US.PNG).   You can configure the settings. |
| ![Activating/exiting the editing mode](images/148900767755_DV_resource.Stream@PNG-de-DE.png) | The editing mode is active. | To exit the editing mode, proceed as follows:  - In the toolbar of the step, click on the button ![Activating/exiting the editing mode](images/154401817611_DV_resource.Stream@PNG-en-US.PNG).   - Or - - In the step below, click the button ![Activating/exiting the editing mode](images/154401817611_DV_resource.Stream@PNG-en-US.PNG).   Editing has been finished. A new restore point is assigned automatically. The current configuration is saved retentively. |

> **Note**
>
> **Message in case of multiple access**
>
> The editing mode can only be activated if the drive is not simultaneously accessed by another PC via Startdrive or the web server.
>
> If another access is active, activation of the editing mode will be denied. An appropriate message is displayed.

> **Note**
>
> **Message when editing factory settings in the online mode**
>
> A message is displayed if a drive still has the factory settings, and the edit mode of the prompted guided quick startup is started. This states that the motor data is based on the rated power of a standard motor.
>
> Therefore, check the motor data online in dialog "Show motor data". When required, correct the motor data and close the dialog.

#### Completing online commissioning

1. To complete online commissioning in the guided quick startup, click the button ![Completing online commissioning](images/154401817611_DV_resource.Stream@PNG-en-US.PNG).

   All settings made in the quick startup are then saved retentively. You are provided with an overview of all of the settings made in the last "Overview" step.

#### Canceling online commissioning

1. If you want to cancel online commissioning via the guided quick startup, click on the "Cancel" button.

   A confirmation prompt appears.
2. If you really want to cancel, click on "OK".

   All settings made in the quick startup are then discarded. Then the previous settings are restored via the last restore point.

### Connection to PLC

#### Overview

The quick startup step "Connection to PLC" indicates that this drive can only be commissioned together with a controller. In this step you specify whether you also want to use Safety Integrated Functions during operation.

#### Requirements

- The drive has been completely created and specified in the device configuration.
- Optionally, a controller (PLC) also can be created in the device configuration and networked with the drive.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

#### Procedure

"Yes" is automatically set as the default setting for "Define the connection to the PLC". SINAMICS S210 drives can only be operated together with a PLC. This setting can therefore not be changed.

1. Specify whether motion control is to be executed by the drive or by a connected controller.

   The controller is set by default. The activated area of the switch is marked blue (![Procedure](images/149502818699_DV_resource.Stream@PNG-de-DE.png)). Click on the white part of the switch if you wish to change the active setting.
2. If you also want to use Safety Integrated Functions with PROFIsafe, additionally activate the option "Define Safety Integrated Functions via PROFIsafe".

   This option automatically activates the PROFIsafe telegram 901 in the telegram configuration.
3. Save the settings in the project.
4. Click on "Next" to display the next quick startup step.

#### Result

Startdrive defines the default settings of the setup based on what you have specified.

- EPOS settings deactivated:

  If you defined that the ramp-function generator function (motion control) is to be performed by a connected controller, then quick startup steps "Application" and "Application settings" are deactivated. EPOS settings are then not possible.
- Motion control is performed by the drive (step 1):

  In this case, basic positioning is automatically activated as the control mode.

#### Additional parameters

---

### Application

#### Overview

In the quick startup step "Application", you define in detail in which application area the S210 drive is to be used. You define:

- The control mode of the application
- The motion type of the drive
- Detailed settings for the encoder type of the position control used
- The modulo correction

#### Requirements

- The drive has been completely created and specified in the device configuration.
- In the quick startup step "Connection to PLC", it is defined that the SINAMICS drive performs motion control.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

#### Procedure

As soon as the S210 drive acts as motion control (default setting), speed control is no longer possible, only the "Positioning" control mode.

1. Select the motion type that you wish to use for the drive when positioning.

   - Rotary motion

     ![Procedure](images/167359924235_DV_resource.Stream@PNG-en-US.png)

     ![Procedure](images/167359924235_DV_resource.Stream@PNG-en-US.png)
   - Linear motion

     ![Procedure](images/167354006539_DV_resource.Stream@PNG-en-US.png)

     ![Procedure](images/167354006539_DV_resource.Stream@PNG-en-US.png)
2. Then select the measurement units for position and velocity.

   The length unit "LU" is used in the factory setting. The units that can be set depend on the motion type.

   All values are reset to the default values when changing the measurement unit and the axis type.
3. Use the settings for the motor encoder used for the position control:

   - Acquire the number of motor revolutions ([p2504](SINAMICS%20Parameter%20S210.md#p25040-lr-motorload-motor-revolutions)) and load revolutions ([p2505](SINAMICS%20Parameter%20S210.md#p25050-lr-motorload-load-revolutions)).
4. If you wish to apply modulo correction:

   - To do this, activate option "Modulo correction activation" (c2577).
   - Define the modulo range ([p2576](SINAMICS%20Parameter%20S210.md#p2576-epos-modulo-correction-modulo-range-1)).
5. Click on "Next" to display the next quick startup step.

#### Result

Startdrive defines the default settings of the setup based on what you have specified. The telegrams that match the selected application area are also preset.

When control mode "Positioning" is activated, then the additional quick startup step "Application settings" is activated. In this step, you define the settings for active homing or for an absolute encoder adjustment.   
You can also configure additional EPOS functions via the function view "[Parameterization &gt; Technology functions &gt; Basic positioner](#basic-positioner-epos)".

> **Note**
>
> Alternatively, the "Positioning" control mode can also be activated in the "[Function selection](#function-selection)" function view.

#### Additional parameters

---

### Limits

This section contains information on the following topics:

- [Limits when speed control is active](#limits-when-speed-control-is-active)
- [Limits when positioning is active](#limits-when-positioning-is-active)

#### Limits when speed control is active

##### Overview

When speed control is active, you define the basic properties of the closed-loop drive control in the "Limits" quick startup step. When positioning is active, all other settings are visible (see [Limits when positioning is active](#limits-when-positioning-is-active)).

| Designation | Number | Description |
| --- | --- | --- |
| Upper speed limit | [p1083](SINAMICS%20Parameter%20S210.md#p10830-positive-speed-limit) | Maximum speed for the positive direction.   The set value must be less than or equal to the maximum speed ([p1082](SINAMICS%20Parameter%20S210.md#p10820-maximum-speed)). |
| Lower speed limit | [p1086](SINAMICS%20Parameter%20S210.md#p10860-negative-speed-limit) | Maximum speed for the negative direction. The set value must be less than or equal to the maximum speed (p1082). |
| Upper torque limit | [p1520](SINAMICS%20Parameter%20S210.md#p15200-torque-limit-upper) | Defines the upper torque limit or torque limit when motoring. |
| Lower torque limit | [p1521](SINAMICS%20Parameter%20S210.md#p15210-torque-limit-lower) | Defines the lower torque limit or the torque limit when generating |
| Quick stop  Ramp-down time (OFF3) | [p1135](SINAMICS%20Parameter%20S210.md#p11350-off3-ramp-down-time) | The OFF3 ramp-down time is effective from the maximum speed down to the motor standstill. |

> **Note**
>
> **Displaying the actual motor data**
>
> The actual motor data of the drive are shown in dialog "Show motor data". The dialog can be opened using button "Show motor data". The following values can be configured:
>
> - Supply voltage ([p0210](SINAMICS%20Parameter%20S210.md#p0210-device-supply-voltage)).
> - Motor ambient temperature ([p0613](SINAMICS%20Parameter%20S210.md#p06130-motor-temperature-model-ambient-temperature))
> - Direction of rotation ([p1821](SINAMICS%20Parameter%20S210.md#p18210-direction-of-rotation))

##### Requirements

- The motor used in the device configuration has been completely specified and configured.

  This basic parameterization cannot be performed without complete configuration.
- Control mode "Speed control" is activated in the quick startup step "Application".

  When "Positioning" is active other settings are displayed.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

##### Procedure

1. If necessary, correct the specified default values (see table above).
2. Click on "Next" to display the next quick startup step.

##### Result

Startdrive defines the default settings of the setup based on what you have specified.

##### Additional parameters

---

#### Limits when positioning is active

##### Overview

The following settings are displayed in quick startup step "Limits" if a basic positioner is used in the drive for positioning. You define the following limits for EPOS in the lower part of the step:

- Traversing profile

  Defines the maximum traversing profile limitation referred to the velocity.
- Ramp-down times

  Defines the maximum ramp-down time referred to the maximum speed.
- Jerk

  Jerk limitation delays the acceleration.
- Position limits

  The traversing range is dynamically limited by the software limit switch, or alternatively, via the hardware limit switch.

> **Note**
>
> **Displaying the actual motor data**
>
> The actual motor data of the drive are shown in dialog "Show motor data". The dialog can be opened using button "Show motor data". The following values can be configured:
>
> - Supply voltage ([p0210](SINAMICS%20Parameter%20S210.md#p0210-device-supply-voltage)).
> - Motor ambient temperature ([p0613](SINAMICS%20Parameter%20S210.md#p06130-motor-temperature-model-ambient-temperature))
> - Direction of rotation ([p1821](SINAMICS%20Parameter%20S210.md#p18210-direction-of-rotation))

##### Requirements

- The motor used in the device configuration has been completely specified and configured.

  This basic parameterization cannot be performed without complete configuration.
- Control mode "Positioning" is activated in the quick startup step "Application".

  When "Speed control" is active other settings are displayed.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

##### Specifying the maximum traversing profile limitation

1. Correct the specified value in LU for the maximum velocity in the "Max. velocity" field ([p2571](SINAMICS%20Parameter%20S210.md#p2571-epos-maximum-velocity-1)).

   The maximum velocity defines the maximum travel velocity [1000 LU/min]. A change immediately limits the velocity of an active traversing block.

   The "Corresponds to speed" field displays the converted speed, the "Max. speed" field displays the maximum speed.

   The limitation acts when positioning (jogging, processing the traversing blocks, direct setpoint input, home position approach).
2. Correct the specified value in LU for the acceleration at "Max. acceleration" ([p2572](SINAMICS%20Parameter%20S210.md#p2572-epos-maximum-acceleration-1)).

   The "Corresponds to ... ramp-up time" field displays the converted ramp-up time.
3. Correct the specified value in LU for the deceleration at "Max. deceleration" ([p2573](SINAMICS%20Parameter%20S210.md#p2573-epos-maximum-deceleration-1)).

   The "Corresponds to ... ramp-down time" field displays the converted ramp-down time.

   The maximum acceleration and maximum deceleration specify the maximum acceleration for increasing the velocity and the maximum deceleration for reducing the velocity. Both values act when positioning (jogging, processing the traversing blocks, direct setpoint input, home position approach).
4. Save the settings.

##### Specifying the ramp-down time in relation to the maximum speed

The velocity, acceleration and deceleration limitation values do not apply for faults or for a safe stop. Instead, the ramp-down times for OFF1 and OFF3 are used. The proposed ramp-down time is displayed in the "Ramp-down time in relation to max. speed" field.

1. If you want to apply this ramp-down time in OFF1, click the "Accept values" button.

   The ramp-down time is now applied to the "OFF1 ramp-down time" ([p1121](SINAMICS%20Parameter%20S210.md#p11210-off1-ramp-down-time)) field.
2. Enter the required value in field "Ramp-down time (OFF3)" ([p1135](SINAMICS%20Parameter%20S210.md#p11350-off3-ramp-down-time)).
3. Save the settings.

##### Specifying the maximum jerk limitation

A jerk limitation delays the acceleration. Proceed as follows:

1. Activate option "Jerk limitation". (p2575)
2. Enter a value for the maximum jerk limitation under "Max. jerk" ([p2574](SINAMICS%20Parameter%20S210.md#p2574-epos-jerk-limiting-1)).

   The converted values for the rounding times are displayed in the fields below the diagram.
3. Save the settings.

##### Defining position limits

The settings of the position control words and position status words of telegrams 111 or 112 define whether a SW limit switch or a HW limit switch is active.

1. Acquire the values for the negative end position ([p2580](SINAMICS%20Parameter%20S210.md#p2580-epos-negative-software-limit-switch-1)) and the positive end position ([p2581](SINAMICS%20Parameter%20S210.md#p2581-epos-positive-software-limit-switch-1)) of the SW limit switch.

   Both values are preassigned with the factory settings.
2. Save the settings.

##### Result

Startdrive defines the default settings of the setup based on what you have specified. These default settings have an impact on the following EPOS settings in the guided quick startup and/or under [Parameterization &gt; Technology functions &gt; Basic positioner](#basic-positioner-epos).

##### Additional parameters

---

### Application settings

This section contains information on the following topics:

- [Fundamentals](#fundamentals)
- [Configuring active homing](#configuring-active-homing)
- [Configuring absolute encoder adjustment](#configuring-absolute-encoder-adjustment)

#### Fundamentals

##### Overview

Make the positioning settings for EPOS in quick startup step "Application settings". The positioning settings listed depend on the defined application area. You can make the following EPOS settings:

- [Active homing](#configuring-active-homing)
- [Absolute encoder adjustment](#configuring-absolute-encoder-adjustment)

You can make additional EPOS settings via function view "Parameterization". Example:

- [Passive homing](#configuring-passive-homing)
- [Configuring limitations](#configuring-limitations)
- [Configuring monitoring functions](#configuring-position-monitoring)
- [Configuring the direct setpoint specification (MDI)](#checking-the-direct-setpoint-input-mdi)
- [Configuring and using traversing blocks](#using-traversing-blocks)
- [Jogging](#configuring-jog)

In addition, in the same function view you can also see the status of all EPOS functions.

##### Requirements

- The drive has been completely created and specified in the device configuration.
- In the quick startup step "Connection to PLC", it is defined that the SINAMICS drive performs motion control.
- "Positioning" as control type is defined in the quick startup step "Application".
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

##### Additional parameters

---

#### Configuring active homing

##### Overview

With an incremental measuring system, the drive can be homed without requiring a higher-level control. Active homing can be used to traverse to a home position.

The drive itself controls and monitors the homing cycle. There are 3 homing modes for active homing.

##### Requirements

- The drive has been completely created and specified in the device configuration.
- In the quick startup step "Connection to PLC", it is defined that the SINAMICS drive performs motion control.
- "Positioning" as control type is defined in the quick startup step "Application".
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

##### Procedure

In the quick startup step "Application settings", the detailed settings for the homing mode "Active homing" are opened.

| Symbol | Meaning |
| --- | --- |
| 1. Optional: If the detailed settings are hidden, expand them with a mouse click. 2. Activate the required homing mode in field "Homing mode selection".       | Symbol | Meaning |    | --- | --- |    | ① | Use the encoder zero mark and reference cam |    | ② | Use the encoder zero mark |    | ③ | Use the external zero mark via digital input | 3. Optional (for ① and ③):  For home position approach, enter the approach velocity to the reference cam in field "to the reference cam" ([p2605](SINAMICS%20Parameter%20S210.md#p2605-epos-active-homing-approach-velocity-reference-cam-1)). 4. Enter an approach velocity in field "To the zero mark" ([p2608](SINAMICS%20Parameter%20S210.md#p2608-epos-active-homing-approach-velocity-zero-mark-1)).     For home position approach, this approach velocity is applicable after detecting the reference cam to search for the zero mark. 5. Optional (for ③):  From drop-down list "Digital input of the external zero mark" ([p0494](SINAMICS%20Parameter%20S210.md#p04940n-equivalent-zero-mark-input-terminal)) select the input terminal to connect a zero mark replacement.    This parameter supplies incorrect measured values during an active measurement. In this particular case, it is not permissible to write to the parameter. 6. Enter the required home position offset for the home position approach in field "Home position offset" ([p2600](SINAMICS%20Parameter%20S210.md#p2600-epos-active-homing-home-position-offset-1)). 7. If you want to perform the adjustment immediately after the home position approach, activate the option of the same name ([p2584](SINAMICS%20Parameter%20S210.md#p258403-epos-functions-configuration).3). 8. Click on "Next" if you do not wish to make any additional EPOS settings.     The quick startup step "I/O configuration" is displayed. |  |

##### Result

Drive configuration continues based on the selected positioning settings. The approach direction and the home position are specified by the selected telegram.

##### Additional parameters

---

#### Configuring absolute encoder adjustment

##### Overview

Absolute encoders must be adjusted during commissioning. When the machine is switched off, the position information of the encoder is retained. The absolute encoder is therefore first adjusted to the home position, e.g. by jogging.

##### Requirements

- The drive has been completely created and specified in the device configuration.
- In the quick startup step "Connection to PLC", it is defined that the SINAMICS drive performs motion control.
- Control mode "Positioning" is activated in the quick startup step "Application".
- An online connection to the drive has been established.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

##### Setting the home position coordinate

1. In quick startup step "Application settings", open the detailed settings for homing mode "Absolute encoder adjustment".

   The absolute encoder adjustment settings are displayed.
2. Optional: Establish an online connection to the drive if an online connection does not already exist.
3. Correct the home position value in the field "Home position coordinate" (p2511).
4. Click on "Set" ([p2507](SINAMICS%20Parameter%20S210.md#p25070n-lr-absolute-encoder-adjustment-status) = 2).

   Status display "Home position set" ([r2684](SINAMICS%20Parameter%20S210.md#r2684015-epos-status-word-2).11) is then updated. When the adjustment is correct, entry "Absolute encoder adjusted" is displayed in field "Absolute encoder adjustment state".

##### Resetting the home position coordinate

1. In quick startup step "Application settings", open the detailed settings for homing mode "Absolute encoder adjustment".

   The absolute encoder adjustment settings are displayed.
2. Click on "Reset" (p2507 = 1).

   Status display "Home position set" (r2684.11) is then updated. After the reset, entry "Absolute encoder not adjusted" is displayed in field "Absolute encoder adjustment state".
3. Optional: Then set a new home position coordinate.

##### Result

Drive configuration continues based on the selected positioning settings. Click on "Next" if you do not wish to make any additional EPOS settings.

The quick startup step "I/O configuration" is displayed.

##### Additional parameters

---

### I/O configuration

#### Overview

In quick startup step "I/O configuration", make the basic settings for the (fail-safe) digital inputs of the drive:

- Fail-safe digital input (F-DI, DI 2 and DI 3)
- 2 fast digital inputs (DI 0 and DI 1) as measuring inputs for evaluation in the control
- Digital input DI 4 for monitoring the temperature of an optional external braking resistor

#### Requirements

- The motor used in the device configuration of the drive has been completely specified and configured.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

#### Procedure

1. In field "Activate measuring probe 1", select whether you wish to use the measuring probe for DI 0.
2. In field "Activate measuring probe 2", select whether you wish to use the measuring probe for DI 1.
3. In the drop-down list "Activate equivalent zero mark", select whether you wish to use an external zero mark or whether this external zero mark should apply for DI 0 or DI 1.
4. In the drop-down list on the right for DI4, select whether the temperature monitoring of the external braking resistor should be activated or not. Temperature monitoring is deactivated by default.
5. Click on the button to the right of "F-DI" if you wish to configure fail-safe digital inputs.

   The safety function view "Control" then opens. Here, parameterize the fail-safe digital inputs for control via PROFIsafe (see [Control](#control)).
6. Click "Next" to display the next quick startup step.

#### Additional parameters

---

### Telegrams (only offline)

#### Overview

The telegrams of the drive were preconfigured by the specifications previously defined in the guided quick startup.

In quick startup step "Telegrams", you can optimize these default settings if this is necessary for your drive. The following telegrams are preassigned depending on the selected control mode:

| Control mode | Preset telegram | Telegrams that can be set |
| --- | --- | --- |
| "Speed control" | 105 | 3, 4, 5, 6, 102, 103, 106 |
| "Positioning" | 112 | 7, 9, 111 |

#### Requirements

- The motor used in the device configuration of the drive has been completely specified and configured.
- Optionally, a controller (PLC) also can be created in the device configuration and networked with the drive.
- There is **no** active online connection between the drive and operating unit.

  Telegrams can only be configured offline.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

#### Procedure

The default telegrams are displayed in the "Telegrams" quick startup step.

1. Select the desired standard telegram from the "Telegram" drop-down list.
2. If you have not yet activated a PROFIsafe telegram in the quick startup step "Connection to PLC", then you can activate a PROFIsafe telegram here. For this purpose, activate the option "Use Safety Integrated Functions via PROFIsafe".

   This option automatically activates the PROFIsafe telegram 901 in the telegram configuration.
3. If, instead of the suggested PROFIsafe telegram 901, you wish to use PROFIsafe telegram 30, then select the telegram in the "PROFIsafe Telegram" drop-down list.

   ([details](Communication%20and%20telegrams.md#telegram-overview-for-sinamics-s210) on telegrams)
4. Correct the preset reference speed ([p2000](SINAMICS%20Parameter%20S210.md#p2000-reference-speed)) in the field with the same name.
5. If you want to optimize the settings of the telegrams used in the telegram configuration, click on the ![Procedure](images/92607914379_DV_resource.Stream@PNG-de-DE.PNG) "Extended settings" icon.

   The properties of the PROFINET interface are displayed in the inspector window. Make the required settings under "[Telegram settings](Communication%20and%20telegrams.md#settings-for-sinamics-s210)".
6. Switch back to the quick startup step "Telegrams".
7. Click "Next" to display the next quick startup step.

#### Result

The telegrams for communication are configured.

#### Additional parameters

---

### Rotate & optimize

#### Overview

Optimize the converter online in quick startup step "Rotate &amp; Optimize". To do this, use the "One Button Tuning". This step cannot be configured offline.

With "One Button Tuning" (OBT), the mechanical drive train is measured using short test signals. This procedure adapts the controller parameters to the existing mechanical system. With this optimization procedure you determine the optimum controller settings with few entries.

> **Note**
>
> **Alternatively: Moving the drive via the control panel**
>
> If you want to use the control panel in the "Rotate &amp; Optimize" step, click the "Use control panel" button. Instead of the OBT, the control panel is now displayed in the quick startup step. Proceed as described under [Traverse the drive from the control panel by specifying the speed](#traverse-the-drive-from-the-control-panel-by-specifying-the-speed).

#### Requirements

- The motor used in the device configuration of the drive has been completely specified and configured.
- There is an active online connection between the drive and the operating unit.
- The [editing mode](#edit-mode-online) is activated.
- With project protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

#### Step 1: Assuming master control

When an online connection has been established, the control bar is highlighted in color. The control elements are grayed-out apart from the "Activate" button. The remaining control elements become active only after you have activated the master control and set the enables.

> **Note**
>
> **Project lock not available when master control is active**
>
> As long as the master control of a drive is active, you cannot apply the project lock if project protection is activated.
>
> The automatic project lock is also suspended on inactivity.

| Symbol | Meaning |
| --- | --- |
| 1. Establish an online connection to the drive if up until now you had worked in the offline mode. 2. If the master control is still not active, click on "Activate" under "Master control".    The "Activate master control" message window is opened. 3. Read the warning carefully. Check the monitoring time and if required, correct it.     The monitoring time specifies the time during which the connection from the operating unit to the drive is cyclically monitored. The minimum value is 1000 ms. 4. The "Stop with spacebar" option is active by default. When the option is activated the drive is always braked using the shutdown function OFF3 if you press the spacebar or if the focus switches. The focus switches when a dialog is opened (e.g. download dialog) or when switching from TIA Portal to another application.       | Symbol | Meaning |    | --- | --- |    |  | **Warning** |    | **Braking not guaranteed if the "Stop with spacebar" option is deactivated** Stopping by using the buttons on the control panel cannot be guaranteed in extreme operating modes. If the additional braking function "Stop with spacebar" is deactivated, it may no longer be possible to brake the motor via the TIA Portal. This can lead to accidents resulting in death or serious injury.  - Only deactivate the "Stop with spacebar" option in absolute exceptional cases and if it has been ensured that you are able to stop the drive safely using suitable hardware solutions. |  |     - Optional: If you do not want to use the "Stop with spacebar" option, deactivate this option in the message window.       This setting requires a safety confirmation. The message window cannot be closed without confirmation.    - Also activate the "Continue without quick stop function via spacebar and focus switch" option. 5. To close the message window and confirm your inputs, click on "OK".     The message window closes. The master control is then active. |  |

#### Step 2: Making the optimization settings

You can make the optimization settings exclusively online. Proceed as follows:

1. Select the desired dynamic response setting for the One Button Tuning corresponding to the mechanical system of your machine.

   One Button Tuning optimizes the drive based on the selected dynamic response setting.

   - Conservative

     Slow control – low mechanical load.
   - Standard

     Best compromise between fast speed control and low mechanical load.
   - Dynamic

     Fast closed-loop speed control – high mechanical load.
2. Enter the angle in the "Rotation limit" field through which the motor and the connected machine are permitted to turn for the required measurements (e.g. 360°) without the mechanical system being damaged.

   The angle should be at least 60° in order to be able to determine useful controller parameters. Generally, longer traversing distances result in better optimization results.
3. Should you wish to perform extended settings, click on the "Extended settings" button.

   The "Machine property" dialog opens. You will receive information under which conditions you can increase the speed control dynamic response. If you want to increase the dynamic response, activate the "Set current setpoint filter with distance compensation" option.
4. If you want to perform OBT at a later time, click "Next" to display the next quick startup step.

   - Or -

   If you want to perform OBT now, proceed as described below in Step 2 ff.

#### Step 3: Start One Button Tuning

When all necessary default settings have been performed, you can start One Button Tuning:

1. To measure the drive to optimize it, click on the "Start" button in the "Measurement" area.

   The optimization function determines all actual values of the drive necessary for optimization.

   Optional: If you want to cancel optimization, click the "0" button in the "Switch off" area.
2. If optimization was successful, save the project.

#### Step 4: Deactivate master control

Following conclusion of One Button Tuning, the master control can be returned as follows:

1. Click the "Deactivate" button under "Master control".

   The "Deactivate master control" message window opens.
2. If you really want to deactivate the master control, click "Yes".

   The grayed-out user interface of the "Deactivate" button indicates that the master control is deactivated.

#### Optional: displaying the next step

1. Click on "Next" to display the next quick startup step.

   The follow-up step "Overview" is displayed.

#### Result

The result of the optimization is displayed in the "Status" area. If the optimization was successful, the corresponding LED lights up in green. The "Optimization result" list compares the settings changed by the tuning with the earlier settings prior to tuning.

If optimization was not successful, repeat tuning with modified specifications, if applicable.

#### Additional parameters

---

### Overview

This section contains information on the following topics:

- [Overview (offline)](#overview-offline)
- [(Online) overview](#online-overview)

#### Overview (offline)

##### Overview

Here you will find a compilation of all settings made (offline) after completing the commissioning steps in the guided quick startup.

If necessary, you can load the settings made offline from the overview into the device.

##### Requirements

- The drive has been completely created and specified in the device configuration.

  This basic parameterization cannot be performed without complete configuration.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

##### Optional: Downloading project data to the device

1. In the "Overview" step, click the button ![Optional: Downloading project data to the device](images/154854713483_DV_resource.Stream@PNG-en-US.PNG).

   To transfer the protected project data, you must log into the device with your user data.
2. Proceed as described under "[Download to device](Configuring%20SINAMICS%20S210%20drives%20%28StdrS210fromRTv61ConfenUS%29.md#loading-the-configuration-from-the-project-to-the-device)".

#### (Online) overview

##### Overview

Here you will find a compilation of all settings made (online) after completing the commissioning steps in the guided quick startup. You can sort and export the corresponding information or also compare it with the factory settings.

##### Requirements

- The drive has been completely created and specified in the device configuration.

  This basic parameterization cannot be performed without complete configuration.
- There is an active online connection between the drive and the operating unit.
- The online configuration has been [completed](#edit-mode-online).
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

##### Optional: Uploading project data from the device

1. If you want to transfer the current project data into the TIA project of your operating unit after online commissioning has been completed, click on "Finish".

   The ![Optional: Uploading project data from the device](images/145960130315_DV_resource.Stream@PNG-de-DE.png) icon (Upload from device) is then displayed in the "Overview" step.
2. Click the ![Optional: Uploading project data from the device](images/145960130315_DV_resource.Stream@PNG-de-DE.png) icon (Upload from device).
3. Proceed as described under "[Upload from device](Configuring%20SINAMICS%20S210%20drives%20%28StdrS210fromRTv61ConfenUS%29.md#loading-the-configuration-from-the-device-to-the-project)".

## Parameterization

This section contains information on the following topics:

- [Overview](#overview-2)
- [Basic parameterization](#basic-parameterization)
- [Inputs/outputs](#inputsoutputs)
- [Safety Integrated](#safety-integrated)
- [Technology functions](#technology-functions)

### Overview

#### Differences between offline and online parameterization

Settings performed offline in the "Parameterization" area generally must be downloaded to the drive before they become active (see [Downloading project data to the device](Configuring%20SINAMICS%20S210%20drives%20%28StdrS210fromRTv61ConfenUS%29.md#loading-the-configuration-from-the-project-to-the-device)).

Settings performed online in the "Parameterization" area generally require an activated editing mode. Automatic restore points that are required as a return points following a cancellation of the current online parameterization are defined by the editing mode during configuration. Without these restore points, the entire parameterization of the drive would have to be repeated.

> **Note**
>
> **Behavior when the online connection is terminated**
>
> If the connection to the drive is re-established after the online connection has been terminated, the program reverts to the stored data of the last restore point.

**Special case Safety Integrated**: The editing mode must be activated for the Safety Integrated Functions both online and offline in order to enable configuration of the safety functions.

#### Requirements

- The drive has been completely created and fully specified in the device configuration.
- The basic settings in the guided quick startup have been made.
- For the online parameterization:   
  There is an active [online connection](Configuring%20SINAMICS%20S210%20drives%20%28StdrS210fromRTv61ConfenUS%29.md#establishing-an-online-connection-to-the-target-device) between the drive and the operating unit.
- No other access from another operating unit to the selected drive is active.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

#### Activating/exiting the editing mode

| Display | Status | Description |
| --- | --- | --- |
| ![Activating/exiting the editing mode](images/148900746379_DV_resource.Stream@PNG-de-DE.png) | The editing mode is not yet activated. | Proceed as follows to activate editing mode:   - Click the button ![Activating/exiting the editing mode](images/154401807627_DV_resource.Stream@PNG-en-US.PNG) in the toolbar of the function view.    - Or - - Click the ![Activating/exiting the editing mode](images/154401807627_DV_resource.Stream@PNG-en-US.PNG) button in the function view below.   You can configure the settings. |
| ![Activating/exiting the editing mode](images/148900767755_DV_resource.Stream@PNG-de-DE.png) | The editing mode is active. | To exit the editing mode, proceed as follows:  - Click the button ![Activating/exiting the editing mode](images/154401817611_DV_resource.Stream@PNG-en-US.PNG) in the toolbar of the function view.   - Or - - Click the ![Activating/exiting the editing mode](images/154401817611_DV_resource.Stream@PNG-en-US.PNG) button in the function view below.   Editing has been finished. A new restore point is assigned automatically. The current configuration is saved retentively. |

> **Note**
>
> **Message in case of multiple access**
>
> The editing mode can only be activated if the drive is not simultaneously accessed by another PC via Startdrive or the web server.
>
> If another access is active, activation of the editing mode will be denied. An appropriate message is displayed.

#### Switching the display: Standard/Extended

The parameterization functions in the parameter view can be switched between standard scope or extended scope. On the 1st call, only the functions of the standard parameter assignment are displayed in the secondary navigation.

- Click ![Switching the display: Standard/Extended](images/153507418891_DV_resource.Stream@PNG-en-US.PNG) to display the functions for extended parameterization.
- Click ![Switching the display: Standard/Extended](images/153509539339_DV_resource.Stream@PNG-en-US.PNG) to reduce the display to the functions of standard parameterization again.

#### Manually navigating between function views

You can navigate between function views using the two navigation buttons:

| Button | Explanation |
| --- | --- |
| ![Manually navigating between function views](images/165979777547_DV_resource.Stream@PNG-en-US.png) | Shows the next function view. However, the function view must already have been displayed once before. |
| ![Manually navigating between function views](images/165979781899_DV_resource.Stream@PNG-en-US.png) | Shows the last function view that was displayed before the current function view. |

### Basic parameterization

This section contains information on the following topics:

- [Basic parameterization](#basic-parameterization-1)
- [Basic parameterization/limitations](#basic-parameterizationlimitations)

#### Basic parameterization

##### Overview

You can parameterize the most important operating parameters in the basic settings. These include:

- Drive supply voltage
- Direction of rotation
- Forced opening of the brake

> **Note**
>
> **Basic parameterization also possible online**
>
> Basic parameterization of the S210 Control Unit is possible offline as well as online.

##### Requirements

- The drive has been completely created and fully specified in the device configuration.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

##### Performing basic parameterization

1. The device supply voltage is preset and depends on the selected drive version.   
   If you want to specify another line voltage, correct the specified line voltage in the input field of the same name ([p0210](SINAMICS%20Parameter%20S210.md#p0210-device-supply-voltage)).
2. The motor ambient temperature is preassigned with 40 °C. Correct the value in the text box "Motor ambient temperature" ([p0613](SINAMICS%20Parameter%20S210.md#p06130-motor-temperature-model-ambient-temperature)) if the ambient temperature is different.

   The underlying temperature model uses the motor ambient temperature to calculate the thermal motor utilization.
3. The direction of rotation last set for the motor is displayed in the "Direction of rotation" drop-down list ([p1821](SINAMICS%20Parameter%20S210.md#p18210-direction-of-rotation)[0]). If you want to adjust the counter-rotational direction, select the desired direction of rotation from the drop-down list:

   - [0] Right
   - [1] Left
4. If you use the "Speed control" control type, make adjustments to the preset limits if necessary (see [Basic parameterization/limitations](#basic-parameterizationlimitations)).
5. Then save the project to accept the settings.

##### Activating/deactivating forced opening of the brake

You can activate forced opening of the brake if the motor being used is equipped with a standard motor holding brake.

As standard, a motor holding brake in an S210 drive is controlled depending on the operating state of the drive. Pulse cancellation automatically closes the brake.

You can change this default setting, and instead, activate forced opening of the brake. The motor holding brake is then always open.

1. Click on "Forced opening of brake" ([p1215](SINAMICS%20Parameter%20S210.md#p12150-motor-holding-brake-configuration) = 2).

   The motor holding brake is now permanently opened.
2. If you now wish to close the motor holding brake, then click on "End forced opening of brake".

##### Additional parameters

---

#### Basic parameterization/limitations

##### Overview

You can parameterize the most important operating parameters in the basic settings in the "Limitations" area. These include:

- Speed limit
- Torque limit
- Ramp-down times (following an OFF1 command and for a fast stop OFF3)

##### Requirements

- The drive has been completely created and fully specified in the device configuration.
- The "Speed control" control method is active.

  When "Positioning" is active as method of control, then the speed control limits are not displayed in the basic parameterization.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

##### Procedure

1. The positive and negative speed limits are preassigned.   
   If you want to change this pre-assignment, correct the values in the "Positive speed limit " ([p1083](SINAMICS%20Parameter%20S210.md#p10830-positive-speed-limit)[0]) or "Negative speed limit" fields ([p1086](SINAMICS%20Parameter%20S210.md#p10860-negative-speed-limit)[0]).
2. If you want to define the fixed upper or motor torque limit, enter an appropriate value in the "Torque limit upper" field ([p1520](SINAMICS%20Parameter%20S210.md#p15200-torque-limit-upper)[0]).
3. If you want to define the fixed lower torque limit or torque limit when generating, enter an appropriate value in the "Torque limit lower" field ([p1521](SINAMICS%20Parameter%20S210.md#p15210-torque-limit-lower)[0]).
4. A ramp-down time in which the speed setpoint is ramped down from maximum speed to standstill following an OFF3 can be specified for the down ramp.   
   In this case, enter a ramp-down time in the "Quick stop (OFF3 ramp-down time)" field ([p1135](SINAMICS%20Parameter%20S210.md#p11350-off3-ramp-down-time)).
5. Then save the project to accept the settings.

##### Result

Startdrive defines the default settings of the setup based on what you have specified.

##### Additional parameters

---

### Inputs/outputs

This section contains information on the following topics:

- [Digital inputs](#digital-inputs)

#### Digital inputs

##### Overview

> **Note**
>
> **Interconnecting signals using drop-down lists**
>
> With SINAMICS S210 there are no direct signal interconnections for the digital inputs. However, drop-down lists at the inputs allow functions or signals to be assigned in a similar way.

SINAMICS S210 drives have the following digital inputs, which you can parameterize:

- Fail-safe digital input (F-DI, DI 2 and DI 3)
- 2 fast digital inputs (DI 0 and DI 1) as measuring inputs for evaluation in the control
- Digital input DI 4 for monitoring the temperature of an optional external braking resistor

##### Requirements

- The drive has been completely created and specified in the device configuration.
- To parameterize the F-DI, the following settings must have been applied in the Safety Integrated basic setting:

  - At least one Safety Integrated Function is activated.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

##### Procedure

Options "Activate measuring probe 1" for DI 0 and "Activate measuring probe 2" for DI 1 are preset when creating the S210 drive.

However, if you are not using a measuring probe, then you can deactivate this measuring probe manually from the appropriate drop-down list. However, as a rule the measuring probes are available.

1. In the drop-down list "Activate equivalent zero mark", select whether you wish to use an external zero mark or whether this external zero mark should apply for DI 0 or DI 1.
2. In drop-down list "Activate overtemperature monitoring for external braking resistor", select whether external braking resistor temperature monitoring should be activated or not.
3. Click on the button to the right of "F-DI" if you wish to configure fail-safe digital inputs.

   The safety function view "Control" then opens. Here, parameterize the fail-safe digital inputs for control via PROFIsafe (see [Control](#control)).
4. Then save the project to accept the settings.

### Safety Integrated

This section contains information on the following topics:

- [Introduction](#introduction)
- [Safety Integrated safety notes](#safety-integrated-safety-notes)
- [Basic settings](#basic-settings)
- [Stop functions](#stop-functions)
- [Brake functions](#brake-functions)
- [Motion monitoring](#motion-monitoring)
- [Actual value acquisition/mechanical system](#actual-value-acquisitionmechanical-system)
- [Control](#control)
- [Function status](#function-status)
- [Responses to safety faults and alarms](#responses-to-safety-faults-and-alarms)

#### Introduction

##### Overview

When compared to standard drive functions, Safety Integrated Functions have an especially low error rate. Performance level (PL) and safety integrity level (SIL) of the corresponding standards are a measure of the error rate.

As a consequence, Safety Integrated Functions are suitable for use in safety-related applications to minimize risk. An application is safety-related if the risk analysis of the machine or the system indicates a special hazard potential in the application.

Safety Integrated ("drive-integrated") means that the safety functions are integrated in the drive and can be executed without additional external components.

##### Conformity

Safety Integrated Functions comply with:

- Safety Integrity Level (SIL) 3 according to IEC 61800‑5‑2
- Category 3 or 4 according to EN ISO 138491
- Performance Level (PL) e according to EN ISO 13849-1

Safety Integrated Functions correspond to the functions according to IEC 61800‑5‑2 and IEC 61800‑5‑3.

##### Safety functions used

The SINAMICS S210 drives feature the following drive-integrated safety functions:

| Functions | Abbr. | Area | Meaning |
| --- | --- | --- | --- |
| [Safe Torque Off](#sto) | STO | **Stop functions** | Safe Torque Off according to stop Category 0  Must always be parameterized, because this function is selected internally in the system as a stop response after limit value violations or after an internal event. |
| [Safe Stop 1](#ss1) | SS1 | Safe stop in accordance with stop category 1  Must always be parameterized, because this function is selected internally in the system as a stop response after limit value violations or after an internal event. |  |
| [Safe Stop 1E](#ss1e) | SS1E | Safe stop according to stop category 1 with external stop |  |
| [Safe Stop 2](#ss2) | SS2 | Safe stop according to stop category 2 |  |
| [Safe Stop 2E](#ss2e) | SS2E | Safe stop according to stop category 2 with external stop |  |
| [Safe Acceleration Monitor](#configuring-sam) | SAM | Safe monitoring of drive acceleration  Is required as a subfunction for other safety functions. |  |
| [Safe Brake Ramp](#configuring-sbr) | SBR | Safe Brake Ramp  Is required as a subfunction for other safety functions. |  |
| [Safe Operating Stop](#sos) | SOS | Safe monitoring of the standstill position. |  |
| [Safe Brake Control](#sbc) | SBC | **Brake functions** | Safety-related control of a holding brake integrated in the motor. |
| [Safe Brake Test](#sbt) | SBT | Safe test of the required holding torque of a brake.   **Diagnostic function** |  |
| [Safely-Limited Speed](#sls) | SLS | **Motion monitoring** | Safely-Limited Speed |
| [Safe Speed Monitor](#ssm) | SSM | Safe monitoring of the speed |  |
| [Safe Direction](#sdi) | SDI | Safe monitoring of the direction of motion |  |
| [Safely-Limited Acceleration](#sla) | SLA | Safely-Limited Acceleration |  |

**Special features of PROFIsafe**

For PROFIsafe, you need a telegram extension, which you set under "[Telegram configuration](Communication%20and%20telegrams.md#telegram-configuration-via-profidrive)" or in the "Connection to PLC" step in the guided quick startup.

##### Acceptance test

The EC Machinery Directive and EN ISO 13849-1 require that safety-relevant functions and machine components are tested after commissioning.

The acceptance test supports the validation of the machine. This configuration test listed in drive standard IEC 61800-5-2 is intended to detect potential configuration errors or to document the correct function ("parameter setting matches the machine").

Detailed information about the acceptance test in Startdrive can be found on the following page: [SINAMICS Safety Integrated acceptance test](Safety%20Integrated%20acceptance%20test.md#sinamics-safety-integrated-acceptance-test).

#### Safety Integrated safety notes

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Unexpected machine movement caused by inactive Safety Integrated Functions**  Inactive Safety Integrated Functions or Safety Integrated Functions that have not been adapted can trigger unexpected machine movements that may result in serious injury or death.  If you insert a memory card without Safety Integrated Functions instead of a memory card with active Safety Integrated Functions, the next time the supply voltage is switched on, the Safety Integrated Functions are deactivated.  - Only insert a memory card with the required settings into the drive. - Prevent unauthorized persons accessing the drive. - Protect configurations with active Safety Integrated Functions against changes by assigning roles using user management (UMAC). |  |

> **Note**
>
> **Safety Integrated Functions fault in the case of non-EMC-compliant installation**
>
> A non-EMC-compliant installation of your system/machine can result in sporadic Safety Integrated Functions faults.
>
> - Install the drive so that it is EMC-compliant.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Unexpected movement as a result of an incorrect component replacement**  After a component has been replaced, connections or functions can be defective. This can lead to unexpected motor movements, which can result in death or serious injury.  - After replacing a component, always perform a simplified function test. |  |

#### Basic settings

This section contains information on the following topics:

- [License for Extended Functions required](#license-for-extended-functions-required)
- [Starting and Ending Safety Integrated commissioning](#starting-and-ending-safety-integrated-commissioning)
- [Selecting the safety functionality](#selecting-the-safety-functionality)
- [Security settings for Safety Integrated](#security-settings-for-safety-integrated)

##### License for Extended Functions required

###### Overview

For function packages subject to license, such as Safety Integrated Extended Functions, a memory card is required with a license key. An insufficient license is indicated via the following fault and LED:

- F13000 → license not sufficient
- LED RDY → flashes red at 2 Hz

  ![Overview](images/148901058059_DV_resource.Stream@PNG-de-DE.png)

**Overview of licenses**

Startdrive provides a "License overview" page. This page shows the most important information about the licenses and the license status of your drive system; see [License overview](Configuring%20SINAMICS%20S210%20drives%20%28StdrS210fromRTv61ConfenUS%29.md#overview-of-licenses).

**Trial License Mode**

The drive system can only be operated with an insufficient license for an option during commissioning and servicing. For this purpose, the Trial License Mode must be activated explicitly, see [Trial License Mode](Configuring%20SINAMICS%20S210%20drives%20%28StdrS210fromRTv61ConfenUS%29.md#activate-trial-license-mode).

**Displaying/acquiring the license key**

You can display the currently entered license key or activate a new license key via the "License overview" page; see [License key](Configuring%20SINAMICS%20S210%20drives%20%28StdrS210fromRTv61ConfenUS%29.md#creating-a-license-key).

**Marking of the Extended Functions**

Extended Functions are indicated in the function selection by the icon ![Overview](images/145073587083_DV_resource.Stream@PNG-de-DE.png).

###### Functions that require a license

A Safety Extended license is required for the following Safety Integrated Functions:

- Safe Stop 1

  - Safe Stop 1 with acceleration monitoring (SS1-a)
  - Safe Stop 1 with braking ramp monitoring (SS1-r)
- Safe Stop 1 External stop

  - Safe Stop 1 External stop with time control (SS1E-t)
  - Safe Stop 1 External stop with acceleration monitoring (SS1E-a)
  - Safe Stop 1 External stop with brake ramp monitoring (SS1E-r)
- Safe Stop 2

  - Safe Stop 2 with time control (SS2-t)
  - Safe Stop 2 with acceleration monitoring (SS2-a)
  - Safe Stop 2 with brake ramp monitoring (SS2-r)
- Safe Stop 2 External stop

  - Safe Stop 2 External stop with time control (SS2E-t)
  - Safe Stop 2 External stop with acceleration monitoring (SS2E-a)
  - Safe Stop 2 External stop with brake ramp monitoring (SS2E-r)
- Safe Operating Stop (SOS)
- Safe Brake Test (SBT)
- Safely-Limited Speed (SLS)
- Safe Speed Monitor (SSM)
- Safe Direction (SDI)
- Safely-Limited Acceleration (SLA)

##### Starting and Ending Safety Integrated commissioning

###### Requirement

For safety reasons, you can only set the Safety Integrated-relevant parameters of the 1st channel offline with the Startdrive commissioning tool. If the drive is online, the data of the 1st channel is automatically duplicated in the 2nd channel.

###### Activating/exiting the editing mode

Safety Integrated is configured online and offline exclusively in the "Editing mode" (corresponds to the commissioning mode).

When editing mode is started, it is checked whether the specified security rights are available.

When you exit editing mode, the checksums for the parameterization that have been performed are calculated and stored in the project during offline editing and in the drive during online editing.

In addition, when working in online mode, STO is activated for safety reasons when editing mode is started, so that the drive remains in a safe state during Safety Integrated parameterization.

| Display | Status | Description |
| --- | --- | --- |
| ![Activating/exiting the editing mode](images/148900746379_DV_resource.Stream@PNG-de-DE.png) | The editing mode is not yet activated. | Proceed as follows to activate editing mode:   - Click the button ![Activating/exiting the editing mode](images/154401807627_DV_resource.Stream@PNG-en-US.PNG) in the toolbar of the Safety function view.    - Or - - Click the ![Activating/exiting the editing mode](images/154401807627_DV_resource.Stream@PNG-en-US.PNG) button in the function view below.   You can configure the Safety Integrated Functions. |
| ![Activating/exiting the editing mode](images/148900767755_DV_resource.Stream@PNG-de-DE.png) | The editing mode is active. | To exit the editing mode, proceed as follows:  - Click the button ![Activating/exiting the editing mode](images/154401817611_DV_resource.Stream@PNG-en-US.PNG) in the toolbar of the Safety function view.   - Or - - Click the ![Activating/exiting the editing mode](images/154401817611_DV_resource.Stream@PNG-en-US.PNG) button in the function view below.   Editing has been finished. If you access the drive online, the configuration is saved retentively when you exit editing mode. |

> **Note**
>
> **Starting editing in online mode**
>
> If the Safety Integrated settings differ from the factory settings, a prompt appears when you click on ![Activating/exiting the editing mode](images/154401807627_DV_resource.Stream@PNG-en-US.PNG). You can then choose between the two options for the follow-up settings:
>
> - You want to make your modifications based on the current settings.
> - You want to make your modifications based on the factory settings.   
>   In this case, the safety settings are reset to the factory settings.

> **Note**
>
> **Navigation in the Safety Integrated Function views**
>
> You mainly use the secondary navigation of the parameterization for the navigation between the different Safety Integrated Function views.
>
> However, as alternative the "Next" and "Back" buttons are available in the footer of the function view. You can scroll from function view to function view using these buttons.

> **Note**
>
> **Read-only mode**
>
> You can open the Safety Integrated Functions in read mode at any time.
>
> If editing rights are not available, only read mode is available.

> **Note**
>
> **Special case: Canceling in the online mode**
>
> You can discard the safety settings you have made at any time by clicking on "Cancel". Then the safety settings of the restore point last saved will be applied.

> **Note**
>
> **Message in case of multiple accesses to the drive**
>
> The online editing mode can only be activated if the drive is not simultaneously accessed by another operating unit via Startdrive or the web server. If another access is active, activation of the editing mode will be denied. An appropriate message is displayed.
>
> Offline, the editing mode can be activated at Safety Integrated without any restriction.

##### Selecting the safety functionality

###### Usable Safety Integrated Functions

In the function selection, the control type releases a number of Safety Integrated Functions that can then be activated.

Safety functions that can be activated for each control type

| Control type | PROFIsafe | PROFIsafe and emergency stop via terminals | Terminals <sup>1)</sup> |
| --- | --- | --- | --- |
| STO | x | x | x |
| SS1 | x | x | x |
| SS1E | x | x | x |
| SS2 | x | x | ‑ |
| SS2E | x | x | ‑ |
| SOS | x | x | ‑ |
| SBC | x | x | X |
| SBT | x | x | ‑ |
| SLS | x | x | ‑ |
| SSM | x | x | ‑ |
| SDI | x | x | ‑ |
| SLA | x | x | ‑ |
| <sup>1)</sup> Several Extended Functions are not usable here. This function is automatically deactivated when switching over the control type. |  |  |  |

> **Note**
>
> **Marking of the Extended Functions**
>
> Extended Functions are indicated in the function selection by the icon ![Usable Safety Integrated Functions](images/145073587083_DV_resource.Stream@PNG-de-DE.png). The corresponding safety functions are part of a function package that requires a license.

###### Requirements

- Using Safety Extended Functions:

  A [Safety Extended license](#license-for-extended-functions-required) is available for the following Safety Integrated Functions.
- The drive has been completely created and specified in the device configuration.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

###### Procedure

1. Call the "Safety Integrated &gt; Function selection" menu in the secondary navigation.
2. Click on ![Procedure](images/154401807627_DV_resource.Stream@PNG-en-US.PNG) to activate the editing mode.
3. Select one of the following from the "Control type" drop-down list:

   - No Safety Integrated Function
   - via PROFIsafe
   - via PROFIsafe and emergency stop via terminals
   - via terminals
4. Then activate the Safety Integrated Functions that you require in the lower part of the dialog.

   Startdrive only displays the functions that belong to the control type you selected. The entries for the selected and preselected functions are displayed in the secondary navigation.
5. Select the drive axis type in the "Axis type" drop-down list ([p9502](SINAMICS%20Parameter%20S210.md#r9502-si-axis-type)):

   - "Linear axis"
   - "Rotary axis"

   This setting influences the setting options in the "Actual value acquisition" function view and provides for a unit switchover.
6. If you made the previous settings in online mode, subsequently perform a warm start of the drive.
7. Then click the buttons (or the entry in the secondary navigation) to display and to parameterize the required safety function.
8. After completing parameterization, to exit the editing mode, click ![Procedure](images/154401817611_DV_resource.Stream@PNG-en-US.PNG).

   - If you are working offline, the project can now be loaded into the drive.
   - If you are working online, the parameterization performed takes effect and can be executed at the machine.

**Higher-level settings**

With the selected control type, you can set the actual value acquisition and the actual value acquisition cycle. Actual value sensing "with encoder" (p9506) is preassigned and cannot be changed.

The Safety Integrated monitoring clock cycle is preset to 4 ms and the actual value acquisition clock cycle is preset to 1 ms. This does not have to be changed for Safety Integrated applications.

###### Result

The basic settings for Safety Integrated have been made. The desired Safety Integrated Functions are enabled. The Safety Integrated Functions are executed with pre-defined standard settings. You can change the settings in the detail settings to address your specific requirements.

###### Additional parameters

---

---

**See also**

[Control](#control)

##### Security settings for Safety Integrated

###### Overview

Access rights for Safety Integrated Functions of SINAMICS drives (from SINAMICS firmware V6.1) can be set via the user administration of the TIA Portal. In this user administration, (with administrator rights), you can create very detailed specific users and roles. As a result of the assigned function rights, these users can change settings in the Safety Integrated Functions.

This protection replaces the use of a classic safety password, as was still used with older SINAMICS drives.

###### More information

Detailed information on project protection can be found in the online help under the heading of "[User management (UMAC)](User%20administration%20and%20security.md#user-management-and-access-control-umac)".

For information about the elementary function rights in Startdrive, see "[Access control](User%20administration%20and%20security.md#access-control)".

#### Stop functions

This section contains information on the following topics:

- [STO](#sto)
- [SS1](#ss1)
- [SS1E](#ss1e)
- [SS2](#ss2)
- [SS2E](#ss2e)
- [SAM/SBR](#samsbr)
- [SOS](#sos)

##### STO

This section contains information on the following topics:

- [Safe Torque Off (STO) mode of operation](#safe-torque-off-sto-mode-of-operation)
- [Configuring STO/SBC](#configuring-stosbc)

###### Safe Torque Off (STO) mode of operation

###### Overview

![Overview](images/146580629515_DV_resource.Stream@PNG-de-DE.png)

The Safe Torque Off (STO) function prevents energy from being fed to the motor and prevents unexpected restarting of the motor.

If the motor is still rotating when STO is selected, then it coasts down to standstill.

STO corresponds to Stop Category 0 in accordance with EN 60204-1.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Unexpected movement of the motor due to active Safe Torque Off**  Unexpected movements of the motor can occur when the Safe Torque Off (STO) function is active. For example, the motor may coast or a suspended load may accelerate the motor. Unexpected movements could cause property damage, endanger persons, and result in serious bodily injury and death.  - Consider the functionality of the Safe Torque Off (STO) function in the risk assessment of the machine or plant. - Prevent motor movements, e.g. by using a holding brake. |  |

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Short-term limited movement of the motor due to the simultaneous breakdown of the depletion layer of power transistors**  Simultaneous breakdown of 2 power transistors (of which one in the upper and one offset in the lower inverter bridge) in the power unit can cause a brief, limited movement. Unexpected movements could cause property damage, endanger persons, and result in serious bodily injury and death.  The maximum movement must not exceed:  - Synchronous rotary motors = 180 °/number of pole pairs - Synchronous linear motors = pole width    **Remedy:**    - Prevent motor movements, e.g. by using a holding brake. |  |

###### Applications

- Applications include all machines and systems with moving axes (e.g. conveyor technology, handling).
- STO is suitable for applications where the motor is already at a standstill or will come to a standstill in a short, safe period of time as a result of friction.
- STO allows you to work safely on the machine with the protective door open. A classic Emergency Stop with electromechanical isolation is not required. The drive remains connected to the line and can be fully diagnosed.

> **Note**
>
> **The distinction between Emergency Off and Emergency Stop**
>
> "Emergency Off" and "Emergency Stop" are commands that minimize different risks in the machine or plant.
>
> The STO function is suitable for implementing an Emergency Stop - but not an Emergency Off.

###### Sequence

![Sequence: STO](images/173808080779_DV_resource.Stream@PNG-en-US.png)

Sequence: STO

|  |  |  |
| --- | --- | --- |
| **Action** |  | **Response / converter** |
| ① | Selection of STO | - The converter identifies when STO is selected and signals the status "STO active" ([r9722](SINAMICS%20Parameter%20S210.md#r9722028-si-status-signals).00) - The converter interrupts the torque-generating energy supply to the motor. There is no electrical isolation. - If you are using a line contactor, then the converter opens the line contactor. - The switch-on inhibit prevents the motor from automatically restarting. |
| ② |  | - The motor coasts down to a standstill. |
| ③ | Deselection of STO | - The converter detects the deselection of STO. |
| ④ | Signal change at ON/OFF1 from 1 to 0 | - The converter is again ready for switching on. |
| ⑤ | Signal change at ON/OFF1 from 0 to 1 | - The motor starts again. |

###### Additional parameters

---

###### Configuring STO/SBC

###### Overview

The "Safe Torque Off" (STO) function is used to safely disconnect the torque-generating energy supply to the motor for a machine function or in the event of a fault. A restart is prevented by the two-channel pulse cancellation. The switch-on inhibit prevents an automatic restart after deselection of STO.

The "Safe Brake Control" (SBC) function supplies a safe output signal for controlling a holding brake.

###### Requirements

- The editing mode for Safety Integrated is [activated](#starting-and-ending-safety-integrated-commissioning).
- The STO stop function is released in the Safety Integrated [function selection](#selecting-the-safety-functionality).
- Optional: Brake monitoring SBC is released in the Safety Integrated [function selection](#selecting-the-safety-functionality).

###### Procedure

1. Click the ![Procedure](images/149396101643_DV_resource.Stream@PNG-de-DE.png) button (Select STO) in the "STO" function view to configure control of the "STO" function.

   The "Control" function view appears. The display of the function view depends on the basic setting of the Safety Integrated Functions in the function selection.

   In this function view, configure the controls via the fail-safe inputs and outputs and/or PROFIsafe (see "[Control](#control)").
2. Optional: Call the "STO/SBC" Safety Integrated Function again.

###### Additional parameters

- [r9720](SINAMICS%20Parameter%20S210.md#r9720028-si-control-word)
- [r9722](SINAMICS%20Parameter%20S210.md#r9722028-si-status-signals)

---

##### SS1

This section contains information on the following topics:

- [SS1 with time control mode of operation (SS1-t)](#ss1-with-time-control-mode-of-operation-ss1-t)
- [SS1 with acceleration monitoring (SS1-a) mode of operation](#ss1-with-acceleration-monitoring-ss1-a-mode-of-operation)
- [SS1 with braking ramp monitoring (SS1-r) mode of operation](#ss1-with-braking-ramp-monitoring-ss1-r-mode-of-operation)
- [Configuring SS1/SBC](#configuring-ss1sbc)

###### SS1 with time control mode of operation (SS1-t)

###### Overview

![Overview](images/151248331275_DV_resource.Stream@PNG-de-DE.png)

With the "Safe Stop 1" (SS1) function, the drive stops the dangerous movement of an electrically driven machine component. After stopping, the Safe Torque Off (STO) function prevents the machine component from restarting. SS1 corresponds to stop category 1 according to EN 60204-1.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Unexpected movement of the motor due to active Safe Torque Off**  Unexpected movements of the motor can occur when the Safe Torque Off (STO) function is active. For example, the motor may coast or a suspended load may accelerate the motor. Unexpected movements could cause property damage, endanger persons, and result in serious bodily injury and death.  - Consider the functionality of the SS1 function in the risk assessment of the machine or plant. - Prevent motor movements, e.g. by using a holding brake. |  |

**Variants of the function**

| Abbreviation | Brief description |
| --- | --- |
| SS1-t | Safe Stop 1 with time control |
| SS1-a | Safe Stop 1 with acceleration monitoring (SAM) |
| SS1-r | Safe Stop 1 with braking ramp monitoring (SBR) |

**Interrupting SS1**

- If SS1 is deselected again within the delay time, after the delay time elapses or after the shutdown velocity is fallen below, the drive selects and deselects STO. This exits the SS1 function normally, and it cannot be interrupted.
- During the delay time, SS1 cannot be deselected by withdrawing the control command, therefore fulfilling the requirements of EN 60204‑1 relating to an EMERGENCY STOP function.

**SS1 delay time**

Select the SS1 delay time so that before the torque is shut down, the motor can completely ramp down along the OFF3 ramp, and if available, the motor holding brake can be closed. The OFF3 ramp-down time must be oriented to the actual braking capability of the system or machine.

Set the SS1 delay time as follows:

- SS1 delay time **with** parameterized motor holding brake:

  SS1 delay time ([p9556](SINAMICS%20Parameter%20S210.md#p9556-si-transition-time-ss1-to-sto)) ≥ OFF3 ramp-down time ([p1135](SINAMICS%20Parameter%20S210.md#p11350-off3-ramp-down-time)) + pulse cancellation delay time ([p1228](SINAMICS%20Parameter%20S210.md#p12280-pulse-cancellation-delay-time)) + motor holding brake closing time ([r1217](SINAMICS%20Parameter%20S210.md#r12170-motor-holding-brake-closing-time))
- SS1 delay time **without** parameterized motor holding brake:

  SS1 delay time (p9556) ≥ OFF3 ramp-down time (p1135) + pulse cancellation delay time (p1228)

###### Applications

SS1 can be applied in the following cases:

- The load torque cannot reduce the motor to a standstill through friction within a sufficiently short time.
- Coasting down of the drive (STO) will pose risks to safety.

###### Safe Stop 1 with time control (SS1-t)

**Sequence:**

When SS1-t is selected, the motor speed is reduced along the OFF3 ramp for the duration of the selected delay time. After the delay time expires, the drive activates the STO function (independent of the actual speed).

> **Note**
>
> Braking at the OFF3 ramp is not monitored!

![Sequence: SS1 with OFF3 (SS1-t)](images/171316884363_DV_resource.Stream@PNG-en-US.png)

Sequence: SS1 with OFF3 (SS1-t)

|  |  |  |
| --- | --- | --- |
| **Action** |  | **Motor / converter response** |
| ① | Selection of SS1 | - The converter detects when SS1 is selected and signals status "SS1 active" ([r9722](SINAMICS%20Parameter%20S210.md#r9722028-si-status-signals).1). - The converter starts the transition time SS1 to STO (p9556). - The converter initiates braking along the OFF3 ramp. |
| ② |  | - The converter brakes the motor along the OFF3 ramp. Braking along the OFF3 ramp is not monitored. |
| ③ |  | - The transition time from SS1 to STO (p9556) elapses. - The converter activates STO and signals status "STO active" (r9722.0) and status "SS1 active". - STO interrupts the torque-generating supply of energy to the motor and prevents the motor from restarting. - The motor coasts down to a standstill. |
| ④ | Deselection of SS1 | - The converter detects the deselection of SS1. - The converter deactivates STO. |
| ⑤ | Signal change at ON/OFF1 from 1 to 0 | - The converter is again ready for switching on. |
| ⑥ | Signal change at ON/OFF1 from 0 to 1 | - The motor starts again. |

###### Additional parameters

---

###### SS1 with acceleration monitoring (SS1-a) mode of operation

###### Overview

With SS1‑a, the converter stops the motor within the set delay time via the OFF3 ramp. With Safe Acceleration Monitor (SAM), the converter monitors whether the motor does not accelerate inadmissibly during the braking process. After the delay time has elapsed or the velocity falls below the set switch-off velocity, the converter activates the Safe Torque Off (STO) function.

###### Sequence:

![Sequence: SS1 with SAM](images/165203494795_DV_resource.Stream@PNG-en-US.png)

Sequence: SS1 with SAM

|  |  |  |
| --- | --- | --- |
| **Action** |  | **Motor / converter response** |
| ① | Selection of SS1 | - The converter detects when SS1 is selected and signals status "SS1 active" ([r9722](SINAMICS%20Parameter%20S210.md#r9722028-si-status-signals).1). - The converter starts the transition time SS1 to STO ([p9556](SINAMICS%20Parameter%20S210.md#p9556-si-transition-time-ss1-to-sto)) and the SAM delay time ([p9582](SINAMICS%20Parameter%20S210.md#p9582-si-samsbr-delay-time-for-ss1-and-ss2)). - The converter brakes the motor along the OFF3 ramp. |
| ② |  | - The SAM delay time elapses. With SAM, the drive monitors whether the motor impermissibly accelerates. - The SAM limit value follows the decreasing motor velocity:   As long as the amount of velocity decreases, the converter continuously adds the configurable tolerance [p9548](SINAMICS%20Parameter%20S210.md#p9548-si-sam-velocity-tolerance-1) to the actual velocity so that the monitoring tracks the velocity as it changes. If the velocity temporarily increases, the monitoring threshold remains at the last value. - If the motor velocity exceeds the SAM monitoring velocity by more than the velocity tolerance (p9548), then the converter signals a fault and activates STO. - If the motor velocity reaches the SAM limit value ([p9568](SINAMICS%20Parameter%20S210.md#p9568-si-sam-velocity-limit-1)), then the converter limits the value for the SAM monitoring to p9568. |
| ③ |  | - SAM ends when the motor velocity falls below the STO shutdown velocity ([p9560](SINAMICS%20Parameter%20S210.md#p9560-si-sto-shutdown-velocity-1)) or the SS1 to STO (p9556) transition time expires. STO is then activated. - The converter identifies when STO is selected and signals the status "STO active" (r9722.0). SS1 still remains active. - STO interrupts the torque-generating supply of energy to the motor and prevents the motor from unexpectedly restarting. - The motor coasts down to a standstill. |
| ④ | Deselection of SS1 | - The converter detects the deselection of SS1. STO is simultaneously deactivated. |
| ⑤ | Signal change at ON/OFF1 from 1 to 0 | - The converter is again ready for switching on. |
| ⑥ | Signal change at ON/OFF1 from 0 to 1 | - The motor starts again. |

###### Additional parameters

---

###### SS1 with braking ramp monitoring (SS1-r) mode of operation

###### Overview

With SS1‑r, the converter stops the motor within the set delay time via the OFF3 ramp. With Safe Brake Ramp (SBR) monitoring, the converter monitors whether the velocity of the motor remains below a specified brake ramp. After the velocity falls below the set switch-off velocity, the converter activates the Safe Torque Off (STO) function.

###### Sequence:

![Sequence: SS1 with SBR](images/173619812363_DV_resource.Stream@PNG-en-US.png)

Sequence: SS1 with SBR

|  |  |  |
| --- | --- | --- |
| **Action** |  | **Motor / converter response** |
| ① | Selection of SS1 | - The converter detects when SS1 is selected and signals status "SS1 active" ([r9722](SINAMICS%20Parameter%20S210.md#r9722028-si-status-signals).1). - The converter brakes the motor along the OFF3 ramp. - The converter starts the SBR delay time ([p9582](SINAMICS%20Parameter%20S210.md#p9582-si-samsbr-delay-time-for-ss1-and-ss2)). |
| ② |  | - The SBR delay time elapses. - The converter starts the Safe Brake Ramp SBR. |
| ③ |  | - The converter monitors whether the motor exceeds the set safe brake ramp when braking. - If the motor velocity does not follow the brake ramp, then the converter signals a fault and activates STO. - Upon reaching the SBR velocity limit ([p9584](SINAMICS%20Parameter%20S210.md#p9584-si-sbr-velocity-limit-1)), monitoring of the SBR brake ramp is deactivated. Braking continues. |
| ④ |  | - SBR ends as soon as the actual speed value is below the STO shutdown speed ([p9560](SINAMICS%20Parameter%20S210.md#p9560-si-sto-shutdown-velocity-1)). - The converter identifies when STO is selected and signals the status "STO active" (r9722.0). SS1 still remains active. - STO interrupts the torque-generating supply of energy to the motor and prevents the motor from unexpectedly restarting. - The motor coasts down to a standstill. |
| ⑤ | Deselection of SS1 | - The converter detects the deselection of SS1. STO is simultaneously deactivated. |
| ⑥ | Signal change at ON/OFF1 from 1 to 0 | - The converter is again ready for switching on. |
| ⑦ | Signal change at ON/OFF1 from 0 to 1 | - The motor starts again. |

###### Additional parameters

---

###### Configuring SS1/SBC

###### Overview

In the "Safe Stop 1" (SS1) function view you make settings for the motor deceleration. Function "SS1" brakes the motor. It monitors the motor deceleration within specified limits.

###### Requirements

- The editing mode for Safety Integrated is [activated](#starting-and-ending-safety-integrated-commissioning).
- The SS1 stop function is released in the Safety Integrated [function selection](#selecting-the-safety-functionality).
- Optional: Brake monitoring SBC is enabled in the Safety Integrated function selection.

###### Configuring SS1 without SAM/SBR

1. Click the ![Configuring SS1 without SAM/SBR](images/149396101643_DV_resource.Stream@PNG-de-DE.png) button (Select SS1) in the "SS1" function view to configure control of the "SS1" function.

   The "Control" function view appears. The display of the function view depends on the basic setting of the Safety Integrated Functions.

   In this function view, configure the controls via the fail-safe inputs and outputs and/or PROFIsafe (see "[Control](#control)").
2. Select the monitoring type "none" in the "Monitoring" drop-down list ([p9606](SINAMICS%20Parameter%20S210.md#p9606-si-ss1-function-specification)).
3. Enter the required delay time in the "Delay time SS1 -&gt; STO active" ([p9556](SINAMICS%20Parameter%20S210.md#p9556-si-transition-time-ss1-to-sto)) entry field.
4. Click "Save project" in the toolbar to save the changes in the project.

###### Variant 1: Configuring SS1 with SAM

1. Click the ![Variant 1: Configuring SS1 with SAM](images/149396101643_DV_resource.Stream@PNG-de-DE.png) button (Select SS1) in the "SS1" function view to configure control of the "SS1" function.

   The "Control" function view appears. The display of the function view depends on the basic setting of the Safety Integrated Functions.

   In this function view, configure the controls via the fail-safe inputs and outputs and/or PROFIsafe (see "[Control](#control)").
2. Select the monitoring type "SAM" in the "Monitoring" drop-down list (p9606).
3. Click the "Monitoring" button and parameterize the alternative brake monitoring functions "[SAM](#configuring-sam)" in the dialog.
4. Enter the required delay time in the "Delay time SS1 -&gt; STO active" (p9556) entry field.
5. Enter the shutdown speed for activating STO in the "STO shutdown speed" ([p9560](SINAMICS%20Parameter%20S210.md#p9560-si-sto-shutdown-velocity-1)) entry field.
6. Click "Save project" in the toolbar to save the changes in the project.

###### Variant 2: Configuring SS1 with SBR

1. Click the ![Variant 2: Configuring SS1 with SBR](images/149396101643_DV_resource.Stream@PNG-de-DE.png) button (Select SS1) in the "SS1" function view to configure control of the "SS1" function.

   The "Control" function view appears. The display of the function view depends on the basic setting of the Safety Integrated Functions.

   In this function view, configure the controls via the fail-safe inputs and outputs and/or PROFIsafe (see "[Control](#control)").
2. Select the monitoring type "SBR" in the "Monitoring" drop-down list (p9606).
3. Click on the "Monitoring" button and parameterize the alternative brake monitoring functions "[SBR](#configuring-sbr)" in the dialog.
4. Enter the shutdown speed for activating STO in the "STO shutdown speed" (p9560) entry field.
5. Click "Save project" in the toolbar to save the changes in the project.

###### Result

You have configured the safety function SS1.

###### Additional parameters

- [r9722](SINAMICS%20Parameter%20S210.md#r9722028-si-status-signals)

---

---

**See also**

[Overview](#overview-2)

##### SS1E

This section contains information on the following topics:

- [Safe Stop 1 external stop (SS1E) mode of operation](#safe-stop-1-external-stop-ss1e-mode-of-operation)
- [SS1E with acceleration monitoring (SS1E-a) mode of operation](#ss1e-with-acceleration-monitoring-ss1e-a-mode-of-operation)
- [SS1E with brake ramp monitoring (SS1E-r) mode of operation](#ss1e-with-brake-ramp-monitoring-ss1e-r-mode-of-operation)
- [Configuring SS1E/SBC](#configuring-ss1esbc)

###### Safe Stop 1 external stop (SS1E) mode of operation

###### Overview

![Overview](images/151248331275_DV_resource.Stream@PNG-de-DE.png)

Safe Stop 1 with external stop (SS1E) stops a dangerous movement of a machine component.

The "Safe Stop 1 with external stop" (SS1E-t) function initiates the "Safe Torque Off" (STO) function after a preset time interval has elapsed. The brake response is specified by the higher-level controller. This function corresponds to stop category 1 to EN 60204‑1.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Unexpected movement of the motor due to active Safe Torque Off**  Unexpected movements of the motor can occur when the Safe Torque Off (STO) function is active. For example, the motor may coast or a suspended load may accelerate the motor. Unexpected movements could cause property damage, endanger persons, and result in serious bodily injury and death.  - Consider the functionality of the SS1E function in the risk assessment of the machine or plant. - Prevent motor movements, e.g. by using a holding brake. |  |

> **Note**
>
> **SS1E cannot be interrupted**
>
> - If SS1E is deselected again within the delay time, the drive selects and then deselects the STO function after the delay time elapses or after the shutdown velocity is undershot. This exits the SS1E function normally, and it cannot be interrupted.
> - During the delay time, SS1E cannot be deselected by withdrawing the control command, therefore fulfilling the requirements of EN 60204‑1 relating to an emergency stop function.

###### Applications

Safe Stop 1 with external stop (SS1E) is suitable for use with drive line-ups where drive-autonomous braking at the respective OFF3 ramp is detrimental to the application.

Drive line-ups are, for example, drives that are mechanically connected to each other via the material.

###### SS1E with time control mode of operation

**Sequence**

When the safety function SS1E-t is used, the drive is shut down using the user program of a higher-level control system. Although the safe delay time is activated when SS1E-t is selected, OFF3 is not activated. Using an appropriate program, the control must then ramp down the drives involved within the delay time to the safe state. After the delay time has elapsed, the drive activates the STO function and safely interrupts the energy feed to the motor (independent of the actual speed).

![Sequence: SS1 with external stop (SS1E-t)](images/171310465547_DV_resource.Stream@PNG-en-US.png)

Sequence: SS1 with external stop (SS1E-t)

Description

|  |  |  |
| --- | --- | --- |
| **Action** |  | **Response motor / controller** |
| ① | Selection of SS1E | - SS1E is selected via the control bit of the selected PROFIsafe telegram or via the F‑DI. |
| ② |  | - The controller triggers the stopping process via the external setpoint specification. - At the same time, the drive starts the SS1E delay time ([p9594](SINAMICS%20Parameter%20S210.md#p9594-si-transition-time-ss1e-to-sto)). |
| ③ |  | - Once the SS1E delay time has expired, the drive automatically triggers STO independent of the actual speed. - The "SS1_active" status is signaled in the status bit of the PROFIsafe telegram. - The motor coasts down to a standstill. - The pulse inhibit safely prevents the motor restarting. |
| ④ | Deselection of SS1E | - SS1E and STO are deactivated by the drive through (manual or automatic program-controlled) deselection. - The drive is "ready for switching on" again. |
| ⑤ | Signal change at ON/OFF1 from 1 to 0 | - The drive can be restarted with the ON/OFF1 signal. |

###### Additional parameters

---

###### SS1E with acceleration monitoring (SS1E-a) mode of operation

###### Overview

SS1E-a with Safe Acceleration Monitor (SAM) monitors whether the motor inadmissibly accelerates when braking. After a defined time interval has elapsed or the velocity falls below a defined shutdown velocity, Safe Torque Off (STO) becomes active.

###### Sequence:

![Sequence: SS1E with SAM](images/171322809099_DV_resource.Stream@PNG-en-US.png)

Sequence: SS1E with SAM

|  |  |  |
| --- | --- | --- |
| **Action** |  | **Motor / converter response** |
| ① | Selection of SS1E | - The converter detects when SS1E is selected and signals status "SS1E active" ([r9722](SINAMICS%20Parameter%20S210.md#r9722028-si-status-signals).18). - The controller triggers the stopping process via the external setpoint specification. - The converter starts the transition time SS1E to STO ([p9594](SINAMICS%20Parameter%20S210.md#p9594-si-transition-time-ss1e-to-sto)) and the SAM delay time ([p9592](SINAMICS%20Parameter%20S210.md#p9592-si-samsbr-delay-time-for-ss1e-and-ss2e)). |
| ② |  | - The SAM delay time elapses. With SAM, the converter monitors whether the motor impermissibly accelerates. - The SAM limit value follows the decreasing motor velocity:   The converter reduces the SAM monitoring velocity step-by-step if the absolute motor velocity is less than the previous SAM monitoring velocity.   It is not possible to increase the SAM monitoring velocity while braking. - If the motor velocity exceeds the SAM monitoring velocity by more than the velocity tolerance ([p9548](SINAMICS%20Parameter%20S210.md#p9548-si-sam-velocity-tolerance-1)), then the converter signals a fault and activates STO. - If the motor velocity reaches the SAM limit value ([p9568](SINAMICS%20Parameter%20S210.md#p9568-si-sam-velocity-limit-1)), then the converter limits the value for the SAM monitoring to p9568. - As long as the velocity decreases, the converter continuously adds the configurable tolerance p9548 to the actual velocity so that the monitoring tracks the velocity as it changes. If the velocity temporarily increases, the monitoring threshold remains at the last value. |
| ③ |  | - SAM ends when the motor velocity falls below the STO shutdown velocity ([p9560](SINAMICS%20Parameter%20S210.md#p9560-si-sto-shutdown-velocity-1)) or the SS1E to STO (p9594) transition time expires. STO is then activated. - The converter identifies when STO is selected and signals the status "STO active" (r9722.0). SS1E still remains active. - STO interrupts the torque-generating supply of energy to the motor and prevents the motor from unexpectedly restarting. - The motor coasts down to a standstill. |
| ④ | Deselection of SS1E | - The converter detects the deselection of SS1E. STO is simultaneously deactivated. |
| ⑤ | Signal change at ON/OFF1 from 1 to 0 | - The converter is again ready for switching on. |
| ⑥ | Signal change at ON/OFF1 from 0 to 1 | - The motor starts again. |

###### Additional parameters

---

###### SS1E with brake ramp monitoring (SS1E-r) mode of operation

###### Overview

With SS1E-r, while braking, the converter monitors whether the velocity of the motor remains below a defined ramp using safe brake ramp monitoring (SBR).

###### Sequence:

![Sequence: SS1E with SBR](images/171319356939_DV_resource.Stream@PNG-en-US.png)

Sequence: SS1E with SBR

|  |  |  |
| --- | --- | --- |
| **Action** |  | **Motor / converter response** |
| ① | Selection of SS1E | - The converter detects when SS1E is selected and signals status "SS1E active" ([r9722](SINAMICS%20Parameter%20S210.md#r9722028-si-status-signals).18). - The controller triggers the stopping process via the external setpoint specification. - The converter starts the SBR delay time ([p9592](SINAMICS%20Parameter%20S210.md#p9592-si-samsbr-delay-time-for-ss1e-and-ss2e)). |
| ② |  | - The SBR delay time elapses. - The converter starts the Safe Brake Ramp SBR. |
| ③ |  | - The converter monitors whether the motor exceeds the set safe brake ramp when braking. - If the motor velocity does not follow the brake ramp, then the converter signals a fault and activates STO. - Upon reaching the SBR velocity limit ([p9584](SINAMICS%20Parameter%20S210.md#p9584-si-sbr-velocity-limit-1)), monitoring of the SBR brake ramp is deactivated. Braking continues. |
| ④ |  | - SBR ends as soon as the actual speed value is below the STO shutdown speed ([p9560](SINAMICS%20Parameter%20S210.md#p9560-si-sto-shutdown-velocity-1)). - The converter identifies when STO is selected and signals the status "STO active" (r9722.0). SS1E still remains active. - STO interrupts the torque-generating supply of energy to the motor and prevents the motor from unexpectedly restarting. - The motor coasts down to a standstill. |
| ⑤ | Deselection of SS1E | - The converter detects the deselection of SS1E. STO is simultaneously deactivated. |
| ⑥ | Signal change at ON/OFF1 from 1 to 0 | - The converter is again ready for switching on. |
| ⑦ | Signal change at ON/OFF1 from 0 to 1 | - The motor starts again. |

###### Additional parameters

---

###### Configuring SS1E/SBC

###### Overview

In the "Safe Stop 1 external stop" (SS1E) function view you make settings for the motor deceleration. The "SS1E" function brakes the motor, monitors the magnitude of the motor deceleration within specified limits, and triggers the STO function after a delay time or violation of a speed threshold.

With SS1E, the drive is not decelerated at the OFF3 ramp. You are responsible for applying suitable measures to brake the drive.

###### Requirements

- The editing mode for Safety Integrated is [activated](#overview-2).
- The SS1E monitoring function is enabled in the Safety Integrated [function selection](#selecting-the-safety-functionality).
- Optional: Brake monitoring SBC is enabled in the Safety Integrated function selection.

###### Configuring SS1E without SAM/SBR

1. Click the ![Configuring SS1E without SAM/SBR](images/149396101643_DV_resource.Stream@PNG-de-DE.png) button (Select SS1E) in the "SS1E" function view to configure control of the "SS1E" function.

   The "Control" function view appears. The display of the function view depends on the basic setting of the Safety Integrated Functions.

   In this function view, configure the controls via the fail-safe inputs and outputs and/or PROFIsafe (see "[Control](#control)").
2. Select the monitoring type "none" in the "Monitoring" drop-down list ([p9606](SINAMICS%20Parameter%20S210.md#p9606-si-ss1-function-specification)).
3. Enter the required delay time in the "Delay time SS1E -&gt; STO active" ([p9594](SINAMICS%20Parameter%20S210.md#p9594-si-transition-time-ss1e-to-sto)) entry field.
4. Click "Save project" in the toolbar to save the changes in the project.

###### Variant 1: Configuring SS1E with SAM

1. Click the ![Variant 1: Configuring SS1E with SAM](images/149396101643_DV_resource.Stream@PNG-de-DE.png) button (Select SS1E) in the "SS1E" function view to configure control of the "SS1E" function.

   The "Control" function view appears. The display of the function view depends on the basic setting of the Safety Integrated Functions.

   In this function view, configure the controls via the fail-safe inputs and outputs and/or PROFIsafe (see "[Control](#control)").
2. Select the monitoring type "SAM" in the "Monitoring" drop-down list (p9606).
3. Click the "Monitoring" button and parameterize the alternative brake monitoring functions "[SAM](#configuring-sam)" in the dialog.
4. Enter the required delay time in the "Delay time SS1E -&gt; STO active" (p9594) entry field.
5. Enter the shutdown speed for activating STO in the "STO shutdown speed" ([p9560](SINAMICS%20Parameter%20S210.md#p9560-si-sto-shutdown-velocity-1)) entry field.
6. Click "Save project" in the toolbar to save the changes in the project.

###### Variant 2: Configuring SS1E with SBR

1. Click the ![Variant 2: Configuring SS1E with SBR](images/149396101643_DV_resource.Stream@PNG-de-DE.png) button (Select SS1E) in the "SS1E" function view to configure control of the "SS1E" function.

   The "Control" function view appears. The display of the function view depends on the basic setting of the Safety Integrated Functions.

   In this function view, configure the controls via the fail-safe inputs and outputs and/or PROFIsafe (see "[Control](#control)").
2. Select the monitoring type "SBR" in the "Monitoring" drop-down list (p9606).
3. Click on the "Monitoring" button and parameterize the alternative brake monitoring functions "[SBR](#configuring-sbr)" in the dialog.
4. Enter the shutdown speed for activating STO in the "STO shutdown speed" (p9560) entry field.
5. Click "Save project" in the toolbar to save the changes in the project.

###### Result

You have configured the safety function SS1E.

###### Additional parameters

- [p1135](SINAMICS%20Parameter%20S210.md#p11350-off3-ramp-down-time)
- p9560
- [r9722](SINAMICS%20Parameter%20S210.md#r9722028-si-status-signals)

---

##### SS2

This section contains information on the following topics:

- [Safe Stop 2 (SS2) mode of operation](#safe-stop-2-ss2-mode-of-operation)
- [SS2 with acceleration monitoring (SS2-a) mode of operation](#ss2-with-acceleration-monitoring-ss2-a-mode-of-operation)
- [SS2 with braking ramp monitoring (SS2-r) mode of operation](#ss2-with-braking-ramp-monitoring-ss2-r-mode-of-operation)
- [Configuring SS2/SBC](#configuring-ss2sbc)

###### Safe Stop 2 (SS2) mode of operation

###### Overview

![Overview](images/146582185739_DV_resource.Stream@PNG-de-DE.png)

The function "Safe Stop 2" SS2 causes the motor to stop with subsequent safe monitoring of the standstill position. This function corresponds to stop category 2 according to EN 60204‑1.

**Variants of the function**

| Abbreviation | Brief description |
| --- | --- |
| SS2-t | Safe Stop 2 with time control (until activation of SOS) |
| SS2-a | Safe Stop 2 with acceleration monitoring (SAM) |
| SS2-r | Safe Stop 2 with brake ramp monitoring (SBR) |

Selection and monitoring of the acceleration (SAM) and the braking ramp (SBR) are realized with two channels. Braking with the OFF3 ramp is realized with one channel.

###### Applications

Use the SS2 for applications where an axis must be safely stopped and where the standstill position must then be safely monitored. Following deselection of SS2, you can continue traversing the axis without reference point approach.

###### Interruption of the ramp function with OFF2

Activating SS2 can cause the higher-level controller (PLC, motion controller) that specifies the speed setpoint to interrupt the ramp function (e.g. with OFF2). The device behaves in this way as a result of a fault response triggered by OFF3 activation. This fault reaction must be prevented by way of appropriate parameterization/configuration.

> **Note**
>
> If a higher-level motion controller is used, you should use the Safety Integrated Function SS2E or SOS.
>
> Reason: For the Safety Integrated Function SS2-r/SS2-a, SINAMICS S210 autonomously brakes at the OFF3 ramp. The motion controller detects a deviation between target value and actual value and shifts the drive to pulse cancellation.

###### Procedure with time control

![Procedure SS2-t with time control](images/173616125323_DV_resource.Stream@PNG-en-US.png)

Procedure SS2-t with time control

|  |  |  |
| --- | --- | --- |
| **Action** |  | **Motor / converter response** |
| ① | Selection of SS2 | - The converter detects when SS2 is selected and signals status "SS2 active" (r9722.1). - The converter starts the SOS delay time (p9553). - The converter initiates braking along the OFF3 ramp. |
| ② | Braking along OFF3 ramp without monitoring | - The converter brakes the motor along the OFF3 ramp. Braking along the OFF3 ramp is not monitored. |
| ③ | Start SOS | - SOS is triggered after the SS2 delay time p9552 elapses. - The SS2 delay time set must allow the drive to brake to a standstill from every speed of the operating process within this time. - The standstill state of the motor is safely monitored with the Safety Integrated Function SOS. The motor remains in control and monitors the standstill tolerance (p9530). - If the standstill tolerance is violated, the drive executes SS1 as an error response with subsequent transition to STO. |
| ④ | Deselection of SS2 | - If SOS is active, the status "SOS active" is also reported in the corresponding status bit of the PROFIsafe telegram. - The "SS2 active" status remains active. - SS2 and SOS are deactivated through (manual or automatic program-controlled) deselection. |
|  |  | - You can immediately continue traversing the axis from the standstill position. |

###### SS2 with acceleration monitoring (SS2-a) mode of operation

###### Overview

With SS2‑a, the converter stops the motor within the set delay time via the OFF3 ramp. With Safe Acceleration Monitor (SAM), the converter monitors whether the motor does not accelerate inadmissibly during the braking process. After the delay time has elapsed, the converter activates the Safe Operating Stop (SOS) function.

###### Sequence:

![Sequence: SS2 with SAM](images/173679166219_DV_resource.Stream@PNG-en-US.png)

Sequence: SS2 with SAM

Description

|  |  |  |
| --- | --- | --- |
| **Action** |  | **Motor / converter response** |
| ① | Selection of SS2 | - The converter detects when SS2 is selected and signals status "SS2 active" ([r9722](SINAMICS%20Parameter%20S210.md#r9722028-si-status-signals)**.**02). - The converter starts the SAM delay time ([p9582](SINAMICS%20Parameter%20S210.md#p9582-si-samsbr-delay-time-for-ss1-and-ss2)). - The converter starts the SS2 delay time ([p9552](SINAMICS%20Parameter%20S210.md#p9552-si-transition-time-ss2-to-sos)). |
| ② |  | - The converter brakes the motor along the OFF3 ramp. - At the same time, the converter activates the Safe Acceleration Monitor (SAM) with a velocity tolerance ([p9548](SINAMICS%20Parameter%20S210.md#p9548-si-sam-velocity-tolerance-1)).   The converter monitors the speed of the motor and prevents the motor from re-accelerating by continuously adjusting the monitoring threshold to the decreasing speed.   Monitoring is deactivated when the SAM velocity limit ([p9568](SINAMICS%20Parameter%20S210.md#p9568-si-sam-velocity-limit-1)) is undershot. |
| ③ | Start SOS | - SOS is triggered once the SS2 delay time has elapsed. The SS2 delay time set must allow the converter to brake to a standstill from any speed of the operating process within this time. - The converter safely monitors the standstill of the motor with the SOS function. The motor remains in control and monitors the standstill tolerance ([p9530](SINAMICS%20Parameter%20S210.md#p9530-si-sos-standstill-tolerance-1)). |
| ④ |  | - If the standstill tolerance is violated, the converter executes SS1 as an error response with subsequent transition to STO. |
| ⑤ |  | - The "SS2 active" status is signaled in the status bit of the PROFIsafe telegram. - You can utilize this status in the higher-level controller. - If SOS is active, the converter also signals "SOS active" in the corresponding status bit of the PROFIsafe telegram. |
| ⑥ | Deselection of SS2 | - SS2 and SOS are deactivated by the converter through (manual or automatic program-controlled) deselection. - You can immediately continue traversing the axis from the standstill position. |

###### Additional parameters

---

###### SS2 with braking ramp monitoring (SS2-r) mode of operation

###### Overview

With SS2‑r, the converter stops the motor within the set delay time via the OFF3 ramp. With Safe Brake Ramp (SBR) monitoring, the converter monitors whether the velocity of the motor remains below a specified brake ramp. After the delay time has elapsed, the converter activates the Safe Operating Stop (SOS) function.

###### Sequence:

![Sequence: SS2 with SBR](images/173609149451_DV_resource.Stream@PNG-en-US.png)

Sequence: SS2 with SBR

Description

|  |  |  |
| --- | --- | --- |
| **Action** |  | **Motor / converter response** |
| ① | Selection of SS2 | - The converter detects the selection of SS2 and signals the status "SS2 active" ([r9722](SINAMICS%20Parameter%20S210.md#r9722028-si-status-signals).02) in the status bit of the PROFIsafe telegram. - The converter starts the SS2 delay time ([p9552](SINAMICS%20Parameter%20S210.md#p9552-si-transition-time-ss2-to-sos)). - The converter starts the SBR delay time ([p9582](SINAMICS%20Parameter%20S210.md#p9582-si-samsbr-delay-time-for-ss1-and-ss2)). No monitoring takes place during this time. |
| ② | Braking along OFF3 ramp with SBR monitoring | - The converter immediately triggers the braking process via the OFF3 ramp after the response time. |
| ③ | Braking along OFF3 ramp with SBR monitoring | - The brake ramp is composed of the reference velocity ([p9591](SINAMICS%20Parameter%20S210.md#p9591-si-sbr-reference-velocity-for-ss1e-and-ss2e-1)) and the SBR monitoring time ([p9583](SINAMICS%20Parameter%20S210.md#p9583-si-sbr-reference-time-for-ss1-and-ss2)). - The converter uses SBR to monitor that the motor does not exceed the set brake ramp during the braking process. - Upon reaching the SBR velocity limit ([p9584](SINAMICS%20Parameter%20S210.md#p9584-si-sbr-velocity-limit-1)), monitoring of the SBR brake ramp is deactivated. Braking continues. |
| ④ | Start SOS | - SOS is triggered after the SS2 delay time (p9552) elapses. - The SS2 delay time set must allow the converter to brake to a standstill from any speed of the operating process within this time. - The standstill state of the motor is safely monitored with the Safety Integrated Function SOS. The motor remains in control and monitors the standstill tolerance ([p9530](SINAMICS%20Parameter%20S210.md#p9530-si-sos-standstill-tolerance-1)). - If the standstill tolerance is violated, the converter executes SS1 as an error response with subsequent transition to STO. |
| ⑤ | Deselection of SS2 | - If SOS is active, the status "SOS active" is also reported in the corresponding status bit of the PROFIsafe telegram. - The "SS2 active" status remains active. - SS2 and SOS are deactivated through (manual or automatic program-controlled) deselection. |
|  |  | - You can immediately continue traversing the axis from the standstill position. |

###### Additional parameters

---

###### Configuring SS2/SBC

###### Overview

The "Safe Stop 2" ("SS2") safety function is used to brake the motor safely along the OFF3 deceleration ramp ([p1135](SINAMICS%20Parameter%20S210.md#p11350-off3-ramp-down-time)) with subsequent transition to the "SOS" state (see "[Safe Operating Stop (SOS)](#sos)") after the delay time expires ([p9552](SINAMICS%20Parameter%20S210.md#p9552-si-transition-time-ss2-to-sos)). The delay time set must allow the drive to brake to a standstill from every speed of the operating process within this time. The standstill tolerance ([p9530](SINAMICS%20Parameter%20S210.md#p9530-si-sos-standstill-tolerance-1)) must not be violated after this time.

After braking, the drives remain in speed control mode with the speed setpoint n = 0. The full torque is available. The default setpoint (e.g. from the setpoint channel, or from a higher-level controller) remains inhibited as long as "SS2" is selected.

> **Note**
>
> **Interruption of the ramp function with OFF3**
>
> Activating SS2 can mean that the higher-level controller (PLC, motion controller) which specifies the speed setpoint, interrupts the ramp function (e.g. with OFF2). The device behaves in this way as a result of a fault response triggered by OFF3 activation. This fault response must be avoided by appropriate parameterization or configuration.

###### Requirements

- The editing mode for Safety Integrated is [activated](#overview-2).
- The SS2 monitoring function is enabled in the Safety Integrated [function selection](#selecting-the-safety-functionality).
- Optional: Brake monitoring SBC is enabled in the Safety Integrated function selection.

###### Procedure

1. Click the ![Procedure](images/148125432331_DV_resource.Stream@PNG-en-US.png) button (Select SS2) in the "SS2" function view to configure control of the "SS2" function.

   The "Control" function view appears. The display of the function view depends on the basic setting of the Safety Integrated Extended Functions.

   In this function view, configure the controls via the fail-safe inputs and outputs and/or PROFIsafe (see "[Control](#control)").
2. Select the monitoring type in the "Monitoring" drop-down list ([p9608](SINAMICS%20Parameter%20S210.md#p9608-si-ss2-function-specification)):

   - None
   - with SAM
   - with SBR
3. Optionally with activated SAM or SBR:   
   Click on the "Monitoring" button and parameterize the alternative brake monitoring functions "[SAM](#configuring-sam)" or "[SBR](#configuring-sbr)" in the dialog.
4. Correct the prescribed delay time in the "Delay time SS2 -&gt; SOS active" field (p9552).
5. Correct the value prescribed for the standstill tolerance in the "Standstill monitoring" field (p9530).
6. Click "Save project" in the toolbar to save the changes in the project.

###### Result

You have configured the safety function SS2.

###### Additional parameters

- p1135
- p9530
- [p9548](SINAMICS%20Parameter%20S210.md#p9548-si-sam-velocity-tolerance-1)
- [r9722](SINAMICS%20Parameter%20S210.md#r9722028-si-status-signals)

---

##### SS2E

This section contains information on the following topics:

- [Safe Stop 2 external stop (SS2E) mode of operation](#safe-stop-2-external-stop-ss2e-mode-of-operation)
- [SS2E with acceleration monitoring (SS2E-a) mode of operation](#ss2e-with-acceleration-monitoring-ss2e-a-mode-of-operation)
- [SS2E with brake ramp monitoring (SS2E-r) mode of operation](#ss2e-with-brake-ramp-monitoring-ss2e-r-mode-of-operation)
- [Configuring SS2E/SBC](#configuring-ss2esbc)

###### Safe Stop 2 external stop (SS2E) mode of operation

###### Overview

![Overview](images/146582185739_DV_resource.Stream@PNG-de-DE.png)

The Safety Integrated Function "Safe Stop 2" SS2E causes the motor to stop with subsequent safe monitoring of the standstill position. The command for stopping comes from a higher-level controller in SS2E. The OFF3 ramp is not used with SS2E.

**Variants of the function**

| Abbreviation | Brief description |
| --- | --- |
| SS2E-t | Safe Stop 2 with external stop and time control (until activation of SOS) |
| SS2E-a | Safe Stop 2 with external stop and acceleration monitoring (SAM) |
| SS2E-r | Safe Stop 2 with external stop and brake ramp monitoring (SBR) |

###### Applications

Safe Stop 2 with external stop (SS2E) is suitable for use with drive line-ups where drive-autonomous braking at the respective OFF3 ramp is detrimental to the application.

Drive line-ups are, for example, drives that are mechanically connected to each other via the material.

###### Procedure with time control

When SS2E‑t is selected, the motor speed is reduced for the duration of the set delay time. After the delay time expires, the drive activates the SOS function (independent of the actual speed).

![Procedure SS2E with time control](images/173612089099_DV_resource.Stream@PNG-en-US.png)

Procedure SS2E with time control

|  |  |  |
| --- | --- | --- |
| **Action** |  | **Motor / converter response** |
| ① | Selection of SS2 | - During operation, SS2E is selected via the control word S_ZSW2.28 of the selected PROFIsafe telegram. - The converter detects the status of SS2E and reports the status "SS2E active" (r9722.22) in the status bit of the PROFIsafe telegram. - The converter starts the SOS delay time (p9553). |
| ② | Braking process starts | - The converter immediately triggers the braking process after the response time. |
| ③ | Start SOS | - SOS is triggered after the SS2 delay time p9552 elapses. - The SS2 delay time set must allow the drive to brake to a standstill from every speed of the operating process within this time. - The standstill state of the motor is safely monitored with the Safety Integrated Function SOS. The motor remains in control and monitors the standstill tolerance (p9530). - If the standstill tolerance is violated, the drive executes SS1 as an error response with subsequent transition to STO. |
| ④ | Deselection of SS2 | - If SOS is active, the status "SOS active" is also reported in the corresponding status bit of the PROFIsafe telegram. - The "SS2 active" status remains active. - SS2 and SOS are deactivated through (manual or automatic program-controlled) deselection. |
|  |  | - You can immediately continue traversing the axis from the standstill position. |

###### SS2E with acceleration monitoring (SS2E-a) mode of operation

###### Overview

With SS2E‑a, the motor is stopped via the user program of a higher-level controller. The controller detects the selection of SS2E from the Safety Info Channel (SIC) in telegram 700 or 701 and stops the motor within the delay time. With Safe Acceleration Monitor (SAM), the converter monitors whether the motor does not accelerate inadmissibly during the braking process. After the delay time has elapsed, the converter activates the Safe Operating Stop (SOS) function.

###### Sequence:

![Sequence: SS2E SAM](images/173678877963_DV_resource.Stream@PNG-en-US.png)

Sequence: SS2E SAM

Description

|  |  |  |
| --- | --- | --- |
| **Action** |  | **Motor / converter response** |
| ① | Selection of SS2E | - During operation, SS2E is selected via the control word S_ZSW2.28 of the selected PROFIsafe telegram. - The converter detects the status of SS2E and reports the status "SS2E active" ([r9722](SINAMICS%20Parameter%20S210.md#r9722028-si-status-signals).22) in the status bit of the PROFIsafe telegram. - The converter starts the SAM delay time ([p9592](SINAMICS%20Parameter%20S210.md#p9592-si-samsbr-delay-time-for-ss1e-and-ss2e)). - The converter starts the SOS delay time ([p9553](SINAMICS%20Parameter%20S210.md#p9553-si-transition-time-ss2e-to-sos)). |
| ② |  | - The converter immediately triggers the braking process after the response time. - At the same time, the converter activates the Safe Acceleration Monitor (SAM) with a velocity tolerance ([p9548](SINAMICS%20Parameter%20S210.md#p9548-si-sam-velocity-tolerance-1)).   The converter monitors the speed of the motor and prevents the motor from re-accelerating by continuously adjusting the monitoring threshold to the decreasing speed.   Monitoring is deactivated when the SAM velocity limit ([p9568](SINAMICS%20Parameter%20S210.md#p9568-si-sam-velocity-limit-1)) is undershot. |
| ③ | Start SOS | - SOS is triggered after the SS2E delay time elapses. The SS2E delay time set must allow the converter to brake to a standstill from any speed of the operating process within this time. - The converter safely monitors the standstill of the motor with the Safety Integrated Function SOS. The motor remains in control and monitors the standstill tolerance ([p9530](SINAMICS%20Parameter%20S210.md#p9530-si-sos-standstill-tolerance-1)). |
| ④ |  | - If the standstill tolerance is violated, the converter executes SS1 as an error response with subsequent transition to STO. |
| ⑤ |  | - The "SS2E active" status is signaled in the status bit of the PROFIsafe telegram. - You can utilize this status in the higher-level controller. - If SOS is active, the converter also signals "SOS active" in the corresponding status bit of the PROFIsafe telegram. |
| ⑥ | Deselection of SS2E | - SS2E and SOS are deactivated by the converter through (manual or automatic program-controlled) deselection. - You can immediately continue traversing the axis from the standstill position. |

###### Additional parameters

---

###### SS2E with brake ramp monitoring (SS2E-r) mode of operation

###### Overview

With SS2E‑r, the motor is stopped via the user program of a higher-level controller. The controller detects the selection of SS2E from the Safety Info Channel (SIC) in telegram 700 or 701 and stops the motor within the delay time. With Safe Brake Ramp (SBR) monitoring, the converter monitors whether the velocity of the motor remains below a specified brake ramp. After the delay time has elapsed, the converter activates the Safe Operating Stop (SOS) function.

###### Sequence:

![Sequence: SS2E SBR](images/173609646731_DV_resource.Stream@PNG-en-US.png)

Sequence: SS2E SBR

Description

|  |  |  |
| --- | --- | --- |
| **Action** |  | **Motor / converter response** |
| ① | Selection of SS2E | - The converter detects the selection of SS2E and signals the status "SS2E active" ([r9722](SINAMICS%20Parameter%20S210.md#r9722028-si-status-signals).22) in the status bit of the PROFIsafe telegram. - The converter starts the SS2E delay time ([p9553](SINAMICS%20Parameter%20S210.md#p9553-si-transition-time-ss2e-to-sos)) via the external setpoint value specification. - The converter starts the SBR delay time ([p9592](SINAMICS%20Parameter%20S210.md#p9592-si-samsbr-delay-time-for-ss1e-and-ss2e)). No monitoring takes place during this time. |
| ② |  | - The SBR delay time elapses. - The converter starts the Safe Brake Ramp SBR. |
| ③ |  | - The brake ramp is composed of the reference velocity ([p9591](SINAMICS%20Parameter%20S210.md#p9591-si-sbr-reference-velocity-for-ss1e-and-ss2e-1)) and the SBR monitoring time ([p9593](SINAMICS%20Parameter%20S210.md#p9593-si-sbr-reference-time-for-ss1e-and-ss2e)). - The converter monitors that the motor does not exceed the set brake ramp when braking. - Upon reaching the SBR velocity limit ([p9584](SINAMICS%20Parameter%20S210.md#p9584-si-sbr-velocity-limit-1)), monitoring of the brake ramp is deactivated. Braking continues. |
| ④ | Start SOS | - SOS is triggered after the SS2E delay time elapses. - The SS2E delay time set must allow the converter to brake to a standstill from any speed of the operating process within this time. - The standstill state of the motor is safely monitored with the Safety Integrated Function SOS. The motor remains in control and monitors the standstill tolerance ([p9530](SINAMICS%20Parameter%20S210.md#p9530-si-sos-standstill-tolerance-1)). - If the standstill tolerance is violated, the converter executes SS1 as an error response with subsequent transition to STO. |
| ⑤ | Deselection of SS2E | - If SOS is active, the status "SOS active" is also reported in the corresponding status bit of the PROFIsafe telegram. - The "SS2E active" status remains active. - SS2E and SOS are deactivated through the (manual or automatic program-controlled) deselection. |
|  |  | - You can immediately continue traversing the axis from the standstill position. |

###### Additional parameters

---

###### Configuring SS2E/SBC

###### Overview

The "Safe Stop 2 with external stop" ("SS2E") safety function is used to brake the motor safely with the help of an external stop.

When SS2E is selected, however, the drive does not brake the motor independently, but follows the specified speed setpoint of an external control. The PROFIsafe control word S_STW2.28 in telegram 901 selects the SS2E function. The PROFIsafe status word S_ZSW2.28 indicates whether the SS2E function is active.

###### Requirements

- The editing mode for Safety Integrated is [activated](#overview-2).
- The SS2E monitoring function is enabled in the Safety Integrated [function selection](#selecting-the-safety-functionality).
- Optional: Brake monitoring SBC is enabled in the Safety Integrated function selection.

###### Procedure

1. Click the ![Procedure](images/148125432331_DV_resource.Stream@PNG-en-US.png) button (Select SS2E) in the "SS2E" function view to configure control of the "SS2E" function.

   The "Control" function view appears. The display of the function view depends on the basic setting of the Safety Integrated Extended Functions.

   In this function view, configure the controls via the fail-safe inputs and outputs and/or PROFIsafe (see "[Control](#control)").
2. Select the monitoring type in the "Monitoring" drop-down list ([p9609](SINAMICS%20Parameter%20S210.md#p9609-si-ss2e-function-specification)):

   - None
   - with SAM
   - with SBR
3. Optionally with activated SAM or SBR:   
   Click on the "Monitoring" button and parameterize the alternative brake monitoring functions "[SAM](#configuring-sam)" or "[SBR](#configuring-sbr)" in the dialog.
4. Correct the prescribed delay time in the "Delay time SS2E -&gt; SOS active" field ([p9553](SINAMICS%20Parameter%20S210.md#p9553-si-transition-time-ss2e-to-sos)).

   SBR/SAM is not monitored during this delay time. SOS becomes active after this delay time has elapsed.
5. Correct the value prescribed for the standstill tolerance in the "Standstill monitoring" field ([p9530](SINAMICS%20Parameter%20S210.md#p9530-si-sos-standstill-tolerance-1)).
6. Click "Save project" in the toolbar to save the changes in the project.

###### Result

You have configured the safety function SS2E.

###### Additional parameters

- [p1135](SINAMICS%20Parameter%20S210.md#p11350-off3-ramp-down-time)
- p9530
- [p9548](SINAMICS%20Parameter%20S210.md#p9548-si-sam-velocity-tolerance-1)

---

##### SAM/SBR

This section contains information on the following topics:

- [Configuring SAM](#configuring-sam)
- [Configuring SBR](#configuring-sbr)

###### Configuring SAM

###### Overview

The "Safe Acceleration Monitor" (SAM) function is used to safely monitor braking along the OFF3 ramp.

As long as the speed reduces, the converter continuously adds the adjustable velocity tolerance [p9548](SINAMICS%20Parameter%20S210.md#p9548-si-sam-velocity-tolerance-1) to the current speed so that the monitoring tracks the speed. If the speed is temporarily higher, the monitoring remains at the last value. The converter reduces the monitoring until the SAM velocity limit in [p9568](SINAMICS%20Parameter%20S210.md#p9568-si-sam-velocity-limit-1) is reached. The SAM limit value is frozen when the velocity falls below the SAM velocity limit in p9568.

If the motor accelerates by the velocity tolerance during the OFF3 deceleration ramp, SAM detects the incident and triggers an STO.

- SAM monitoring will continue to be performed until the SS1 delay time [p9556](SINAMICS%20Parameter%20S210.md#p9556-si-transition-time-ss1-to-sto) expires.

Calculating the SAM tolerance of the actual velocity:

- The following applies when parameterizing the SAM tolerance:

  - The maximum velocity increase after SS1 is triggered is derived from the effective acceleration (a) and the duration of the acceleration phase.
  - The duration of the acceleration phase is equivalent to one monitoring cycle (MC; [p9500](SINAMICS%20Parameter%20S210.md#p9500-si-monitoring-clock-cycle)) (delay from detecting an SS1 until n<sub>set</sub> = 0)
- Calculating the SAM tolerance:

  Actual velocity for SAM = acceleration x acceleration duration   
  This results in the following setting rule:

  - For a linear axis: SAM tolerance [mm/min] = a [m/s<sup>2</sup>] MC [s] 1000 [mm/m] 60 [s/min]
  - For a rotary axis: SAM tolerance [rpm] = a [rev/s<sup>2</sup>] MC [s] 60 [s/min]
- Recommendation   
  The SAM tolerance value entered should be approx. 20% higher than the calculated value.
- You set the tolerance so that the "undershoot" which inevitably occurs when standstill is reached after braking along the OFF3 ramp is tolerated. However, the size of this cannot be calculated.

###### Additional parameters

- [p9516](SINAMICS%20Parameter%20S210.md#p95161-si-encoder-configuration-safety-functions)
- [p9581](SINAMICS%20Parameter%20S210.md#p9581-si-sbr-reference-velocity-for-ss1-and-ss2-1)
- [p9583](SINAMICS%20Parameter%20S210.md#p9583-si-sbr-reference-time-for-ss1-and-ss2)

---

###### Configuring SBR

###### Overview

The "Safe Brake Ramp" (SBR) function provides a safe method for monitoring the brake ramp. The "Safe Brake Ramp" function is used with the Safe Stop functions for monitoring the braking process.

The motor is immediately decelerated along the OFF3 ramp as soon as "SS1" (SS2, etc.) is initiated. Monitoring of the brake ramp is activated once the delay time [p9582](SINAMICS%20Parameter%20S210.md#p9582-si-samsbr-delay-time-for-ss1-and-ss2) has expired. Monitoring ensures that the motor does not exceed the set brake ramp (SBR) when braking.

The gradient of the brake ramp is defined using the reference velocity [p9581](SINAMICS%20Parameter%20S210.md#p9581-si-sbr-reference-velocity-for-ss1-and-ss2-1) and the brake ramp monitoring time [p9583](SINAMICS%20Parameter%20S210.md#p9583-si-sbr-reference-time-for-ss1-and-ss2).

The braking process can be monitored in parallel with the braking ramp of the converter. Follow these rules for settings:

Linear axis:

- Reference velocity p9581 = Maximum speed [p1082](SINAMICS%20Parameter%20S210.md#p10820-maximum-speed)[0] * Transmission ratio [p9521](SINAMICS%20Parameter%20S210.md#p952107-si-gearbox-encoder-motorload-denominator)[0]/[p9522](SINAMICS%20Parameter%20S210.md#p952207-si-gearbox-encoder-motorload-numerator)[0]* Leadscrew pitch [p9520](SINAMICS%20Parameter%20S210.md#p9520-si-leadscrew-pitch)
- Reference time p9583 = Ramp-down time (OFF3) [p1135](SINAMICS%20Parameter%20S210.md#p11350-off3-ramp-down-time)[0]

Rotary axis:

- Reference velocity p9581 = Maximum speed p1082[0] * Transmission ratio p9521[0]/p9522[0]
- Reference time p9583 = Ramp-down time (OFF3) p1135[0]

###### Pre-assigning the reference velocity/reference time

If required, you can automatically pre-assign the values for reference velocity or reference time. In the lower part of the dialog, the calculation formulas for the corresponding value are displayed for this purpose.

1. If you want to pre-assign the value for the reference velocity, click "Accept" in the corresponding line.
2. If you want to pre-assign the value for the reference time, click "Accept" in the corresponding line.

###### Additional parameters

- [p9516](SINAMICS%20Parameter%20S210.md#p95161-si-encoder-configuration-safety-functions)
- [p9548](SINAMICS%20Parameter%20S210.md#p9548-si-sam-velocity-tolerance-1)

---

##### SOS

This section contains information on the following topics:

- [Safe Operating Stop (SOS) mode of operation](#safe-operating-stop-sos-mode-of-operation)
- [Configuring SOS](#configuring-sos)

###### Safe Operating Stop (SOS) mode of operation

###### Overview

![Overview](images/146579717003_DV_resource.Stream@PNG-de-DE.png)

When the "Safe Operating Stop" (SOS) safety function is selected, the converter safely monitors the position of the converter for standstill. The converter is in control mode and can thus withstand external forces.

After SOS has been selected it becomes active after the parameterizable delay time has expired. The converter must be braked to standstill within this delay time, e.g. by the controller.

**Additional functional features**

- Contrary to SS1 and SS2, SOS does not automatically brake the converter.
- The controller still has setpoint control.
- In the user program of the controller, respond to the "Select SOS" so that the controller brings the converter to a standstill within the delay time.

  | Symbol | Meaning |
  | --- | --- |
  |  | **Warning** |
  | **Unplanned movement of the converter due to mechanical forces**  Mechanical forces greater than the maximum torque of the converter may force a converter in position control out of Safe Operating Stop (SOS). Consequently, this process triggers a category 1 stop function according to EN 60204-1 (fault response function SS1). As a result, unexpected axis movements, which can lead to bodily injury or death, are possible. - Note the alarms for SS1 and STO.   Take suitable measures to prevent unwanted movement, e.g. by using a brake with safe monitoring. |  |

  > **Note**
  >
  > **Size of the tolerance window**
  >
  > The size of the tolerance window must be right for the application, otherwise the default monitoring settings will no longer be effective.

###### Applications

SOS is suitable for the following applications:

- Machine parts must be safely monitored that they actually are at a standstill.
- A holding torque is required.

###### Sequence:

![Sequence: SOS](images/146579780875_DV_resource.Stream@PNG-en-US.png)

Sequence: SOS

Description

|  |  |  |
| --- | --- | --- |
| **Action** |  | **Motor / converter response** |
| ① | Selection of SOS | - SOS is selected during operation via the control bit of the selected PROFIsafe telegram. |
| ② | Start delay time | - The controller triggers the stopping process via an external setpoint specification. - At the same time, the converter starts the SOS delay time. |
| ③ | Start SOS | - SOS is triggered after the SOS delay time elapses. - The SOS delay time ([p9551](SINAMICS%20Parameter%20S210.md#p9551-si-sls-delay-time-for-limit-value-change)) set must allow the converter to brake to a standstill from any speed of the operating process within this time. - The "SOS active" status is signaled in the status bit of the PROFIsafe telegram. - You can utilize this status in the higher-level controller. - The motor is then reliably monitored in the standstill position via an adjustable standstill tolerance ([p9530](SINAMICS%20Parameter%20S210.md#p9530-si-sos-standstill-tolerance-1)). |
| ④ |  | - If the standstill tolerance is violated, SS1 is executed as a stop response followed by a transition to STO. |
| ⑤ | Deselection of SOS | - With the (manual or automatic program-controlled) deselection, the converter deactivates SOS and thus monitoring of the position window. - You can immediately continue traversing the axis from the standstill position. |

###### Additional parameters

---

###### Configuring SOS

###### Overview

The "Safe Operating Stop" (SOS) function is used for safe monitoring of the standstill position of a drive. Positions of a user-defined standstill tolerance are interpreted by the drive as "standstill".

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Unplanned movement of the drive through mechanical forces**  Mechanical forces that are greater than the maximum torque of the drive can force a drive under closed-loop position control out of the Safe Operating Stop (SOS). Consequently, this process triggers a category 1 stop function according to EN 60204-1. As a result, unexpected axis movements, which can lead to bodily injury or death, are possible.  - Note the alarms for SS1 and STO. - Take suitable measures to prevent unwanted movement, e.g. by using a brake with safe monitoring. |  |

**Effectiveness of the SOS function:**

In the "[Function status](#function-status)" function view, you can recognize whether SOS is active by the green "SOS active" LED.

The "SOS" function takes effect in the following cases:

- After SOS is selected and the delay time (in [p9551](SINAMICS%20Parameter%20S210.md#p9551-si-sls-delay-time-for-limit-value-change)) has expired

  The drive must be braked to standstill within this delay time, e.g. by the controller.
- As a consequence of SS2

**Response of the SOS standstill monitoring**

If the standstill tolerance is exceeded (in [p9530](SINAMICS%20Parameter%20S210.md#p9530-si-sos-standstill-tolerance-1)), the drive responds as follows with Safety message C01707.

###### Requirements

- The editing mode for Safety Integrated is [activated](#overview-2).
- In the Safety Integrated [function selection](#selecting-the-safety-functionality), the control mode "via terminals" is not activated.
- The SOS stop function is enabled in the Safety Integrated function selection.

###### Procedure

1. Click the ![Procedure](images/148125432331_DV_resource.Stream@PNG-en-US.png) button (Select SOS) to configure control of the "SOS" function.

   The "Control" function view appears. The display of the function view depends on the basic setting of the Safety Integrated Extended Functions.

   In this function view, configure the controls via PROFIsafe (see "[Control](#control)").

   You can select the PROFIsafe telegrams in the telegram configuration. This means you also specify the required control word.
2. Call the "SOS" function view again.
3. Correct the specified delay time in the field "Delay time SOS -&gt; SOS active" ([p9596](SINAMICS%20Parameter%20S210.md#p9596-si-sos-delay-time)).
4. Enter the required value in the "Standstill tolerance" (p9530) field.

   Alternatively, you can also click on the "Standstill tolerance SOS" button. A dialog with a graphic display of the standstill monitoring opens. Then enter the standstill tolerance in the dialog.
5. Click "Save project" in the toolbar to save the changes in the project.

###### Result

You have configured the safety function SOS.

###### Additional parameters

- [r9722](SINAMICS%20Parameter%20S210.md#r9722028-si-status-signals)

---

#### Brake functions

This section contains information on the following topics:

- [SBC](#sbc)
- [SBT](#sbt)

##### SBC

This section contains information on the following topics:

- [Principle of operation of Safe Brake Control (SBC)](#principle-of-operation-of-safe-brake-control-sbc)
- [Configuring SBC](#configuring-sbc)

###### Principle of operation of Safe Brake Control (SBC)

###### Overview

![Overview](images/159561594123_DV_resource.Stream@PNG-de-DE.png)

The "Safe Brake Control" function (SBC) is used to safely control the motor-integrated holding brake, which operates according to the closed-circuit principle.

> **Note**
>
> **Making detailed settings**
>
> There is no dedicated function view for SBC. Additional detailed settings for SBC are not possible. The activated SBC function acts on the general response of other safety functions, for example STO (see "Sequence").

###### Functional characteristics

You must enable the function when commissioning in order that SBC can become active.

For the "Safe Brake Control" function, the converter assumes a controlling function and ensures the following behavior:

- If the converter detects a fault or failure of the brake, it switches off the brake current.
- The brake closes and a safe state is reached.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Unexpected movement as a result of defective, worn or dirty holding brake**  SBC does not detect mechanical defects of the holding brake, wear or dirt that has accumulated. SBC only detects an interrupted cable or short-circuit in the brake winding when opening the holding brake. Undetected defects, wear or dirt can result in unexpected movement. Unexpected movement of the motor can result in severe injury or death.  - Regularly test the holding brake function. - Replace a defective, worn or dirty holding brake. |  |

###### Applications

Use SBC in applications where the converter must maintain a safe position even when the motor is de-energized. SBC thus prevents suspended or passing loads from dropping (e.g. for lifting gear, passenger elevators, winders). External logic or switching elements are not required as the function is fully integrated in the converter.

###### Sequence

![Sequence: SBC](images/159561598347_DV_resource.Stream@PNG-en-US.png)

Sequence: SBC

|  |  |  |
| --- | --- | --- |
| **Action** |  | **Motor / converter response** |
| ① | Selection of STO | - The converter identifies when STO is selected and signals the status "STO active" ([r9722](SINAMICS%20Parameter%20S210.md#r9722028-si-status-signals).0).   The converter interrupts the torque-generating energy supply to the motor.   The switch-on inhibit prevents the motor from automatically restarting. - The converter requests SBC at the same time as STO. The holding brake is safely controlled by SBC.   The converter immediately closes the holding brake. |
| ② |  | - The motor brakes down to standstill. - Using SBC, the converter ensures that the brake current is interrupted and the holding brake remains closed. |
| ③ | Deselection of STO | - The converter detects the deselection of STO. SBC is also deactivated when STO is deselected. - The holding brake remains (unsafely) closed, until the standard program issues a command to open the brake. |
| ④ | Command to open the brake | - The converter opens the brake taking into account the brake opening time. |

###### Additional parameters

---

###### Configuring SBC

Safety function SBC is never configured alone. As soon as SBC has been activated, you can make the corresponding SBC settings in the STO, SS1, SS1E, SS2 or SS2E function views if the corresponding functions are enabled.

---

**See also**

[Configuring STO/SBC](#configuring-stosbc)
  
[Configuring SS1/SBC](#configuring-ss1sbc)
  
[Configuring SS1E/SBC](#configuring-ss1esbc)
  
[Configuring SS2/SBC](#configuring-ss2sbc)
  
[Configuring SS2E/SBC](#configuring-ss2esbc)

##### SBT

This section contains information on the following topics:

- [Safe Brake Test (SBT) mode of operation](#safe-brake-test-sbt-mode-of-operation)
- [Configuring SBT](#configuring-sbt)

###### Safe Brake Test (SBT) mode of operation

###### Overview

![Overview](images/146579847691_DV_resource.Stream@PNG-de-DE.png)

The diagnostic function "Safe Brake Test" (SBT) checks the required holding torque of a motor holding brake.

This diagnostic function exceeds the scope of EN 61800-5-2.

The converter purposely generates a force/torque against the applied brake. If the brake is operating correctly, the axis movement remains within a parameterized tolerance. However, if a larger axis movement is detected via the actual encoder values, the brake is not able to apply the required holding torque. The brake must now be serviced or replaced.

The "Safe Brake Test" (SBT) diagnostic function meets the requirements for category 2 according to EN ISO 13849‑1.

###### Applications

SBT is suitable for implementing a "safe brake" in conjunction with SBC. This allows errors or wear to be detected in the brake mechanics. Automatic testing of the braking effect reduces maintenance costs and increases safety and availability of the machine or plant.

###### Sequence:

![Sequence: SBT](images/146580615563_DV_resource.Stream@PNG-en-US.png)

Sequence: SBT

Description

|  |  |  |
| --- | --- | --- |
| **Action** |  | **Motor / converter response** |
| ① | Selection of SBT  Start SBT | - The SBT function can be directly operated from a higher-level controller. They are controlled via the control bits of the Safety Control Channel (SCC) - in PROFIdrive telegram 701. - The converter starts the brake test. |
| ② | Parameterization of the brake test | - The converter performs the brake test with the following parameterized variables:    - Ramp time ([p10208](SINAMICS%20Parameter%20S210.md#p1020801-si-sbt-test-torque-ramp-time)[0])   - Holding torque ([p10209](SINAMICS%20Parameter%20S210.md#p1020901-si-sbt-brake-holding-torque)[0])   - Test torque = Factor ([p10210](SINAMICS%20Parameter%20S210.md#p1021001-si-sbt-test-torque-factor-sequence-1)[0])   - Test duration ([p10211](SINAMICS%20Parameter%20S210.md#p1021101-si-sbt-test-duration-sequence-1)[0]) |
| ③ |  | - With SBT, the converter takes into account the parameterized position tolerance ([p10212](SINAMICS%20Parameter%20S210.md#p1021201-si-sbt-position-tolerance-sequence-1-1)[0]) and thus the maximum permissible axis movement. |
| ④ |  | - The converter reports the "SBT active" status in the status bit of the SIC/SCC. - You can utilize this status in the higher-level controller. |
| ⑤ |  | - The converter generates the test torque against the closed brake.   If the brake operates correctly, the axis movement remains within a specified tolerance. - However, if a larger axis movement is detected from the actual encoder values, the brake is not able to apply the required holding torque. The converter terminates the brake test with an error. - In this case, service or replace the brake. |
| ⑥ | Deselection of SBT | - SBT is deactivated by the converter through (manual or automatic program-controlled) deselection. - Depending on the result of the brake test, the automation program can initiate the next step. |

###### Additional parameters

---

###### Configuring SBT

###### Overview

The diagnostic function "Safe Brake Test" (SBT) checks the required holding torque of the motor holding brake for the motor used. The drive purposely generates a configurable torque against the applied brake. If the brake is operating correctly, the axis movement remains within a parameterized tolerance. However, if a larger axis movement is identified from the encoder actual values, the brake is not in a position to provide the specified holding torque. The brake must now be serviced or replaced.

**Functional characteristics**

The "SBT" diagnostic function has the following properties:

- Using this function, brakes can be tested that are directly connected the converter (integrated brake control), but also externally controlled brakes (e.g. via a PLC).
- Test configurations: A maximum of one brake can be tested:

  - One motor holding brake, controlled by the integrated brake control of the SINAMICS.
- The "SBT" function is controlled via Safety Control Channel (SCC) via PROFINET.

  Using "SCC", the "SBT" function can be directly controlled from a higher-level controller.
- The "Safe Brake Test" (SBT) diagnostic function meets the requirements for category 2 according to EN ISO 13849‑1.

###### Requirements

- The editing mode for Safety Integrated is [activated](#starting-and-ending-safety-integrated-commissioning).
- The diagnostic function SBT is enabled in the Safety Integrated [function selection](#selecting-the-safety-functionality).
- Safe Brake Control must be enabled when testing a brake controlled by SINAMICS (motor holding brake).

###### Procedure

The interconnection of the parameters for the telegram extension relevant for SCC/SIC can be performed automatically by setting [p60122](SINAMICS%20Parameter%20S210.md#r60122-profidrive-sicscc-telegram) = 701. However, the telegram extension must have been previously created.

1. Record or correct the following information in the entry fields:

   - Holding torque ([p10209](SINAMICS%20Parameter%20S210.md#p1020901-si-sbt-brake-holding-torque)[0])
   - Factor ([p10210](SINAMICS%20Parameter%20S210.md#p1021001-si-sbt-test-torque-factor-sequence-1)[0])
   - Position tolerance ([p10212](SINAMICS%20Parameter%20S210.md#p1021201-si-sbt-position-tolerance-sequence-1-1)[0])
   - Ramp time ([p10208](SINAMICS%20Parameter%20S210.md#p1020801-si-sbt-test-torque-ramp-time)[0])
   - Test duration ([p10211](SINAMICS%20Parameter%20S210.md#p1021101-si-sbt-test-duration-sequence-1)[0])
2. Click "Save project" in the toolbar to save the changes in the project.

###### Result

You have configured the SBT diagnostic function.

###### Additional parameters

- [p1215](SINAMICS%20Parameter%20S210.md#p12150-motor-holding-brake-configuration)
- [r1216](SINAMICS%20Parameter%20S210.md#r12160-motor-holding-brake-opening-time)
- [r1217](SINAMICS%20Parameter%20S210.md#r12170-motor-holding-brake-closing-time)
- [p10202](SINAMICS%20Parameter%20S210.md#p1020201-si-sbt-brake-selection)
- p10203
- [r10234](SINAMICS%20Parameter%20S210.md#r10234015-si-safety-information-channel-status-word-s_zsw3b)

---

#### Motion monitoring

This section contains information on the following topics:

- [SLS](#sls)
- [SSM](#ssm)
- [SDI](#sdi)
- [SLA](#sla)

##### SLS

This section contains information on the following topics:

- [Safely-Limited Speed (SLS) mode of operation](#safely-limited-speed-sls-mode-of-operation)
- [Principle of operation of SLS with one speed level](#principle-of-operation-of-sls-with-one-speed-level)
- [Principle of operation of SLS with switchover of speed levels](#principle-of-operation-of-sls-with-switchover-of-speed-levels)
- [Principle of operation of SLS with a variable speed limit value](#principle-of-operation-of-sls-with-a-variable-speed-limit-value)
- [Measures when EPOS is activated](#measures-when-epos-is-activated)
- [Additional functional features](#additional-functional-features)
- [Configuring SLS](#configuring-sls)

###### Safely-Limited Speed (SLS) mode of operation

###### Overview

![Overview](images/146581236875_DV_resource.Stream@PNG-de-DE.png)

The converter monitors the motor speed using Safely-Limited Speed (SLS). The converter executes the set stop response if the motor exceeds the permitted speed.

SLS can be used in various ways:

- SLS with 4 independent speed levels that can be switched between during the runtime
- SLS with a variable speed limit value

SLS is controlled via PROFIsafe. Selecting SLS or the switchover to a lower SLS level starts the SLS delay time (p9551). The active SLS level remains active during the delay time. The newly selected SLS level only becomes active afterwards.  
Changing the variable speed limit value via PROFIsafe should also be considered as SLS level switchover.

###### Applications

SLS is suitable for machines susceptible to hazardous situations if a speed is exceeded and wherever work must be performed directly on a machine, for example:

- during operation
- in setup mode
- during maintenance work

---

**See also**

[Principle of operation of SLS with one speed level](#principle-of-operation-of-sls-with-one-speed-level)
  
[Principle of operation of SLS with switchover of speed levels](#principle-of-operation-of-sls-with-switchover-of-speed-levels)
  
[Principle of operation of SLS with a variable speed limit value](#principle-of-operation-of-sls-with-a-variable-speed-limit-value)

###### Principle of operation of SLS with one speed level

###### Overview

SLS can be used with one speed level. If the motor velocity violates the SLS limit value, then the converter initiates the set stop response.

###### Sequence:

![Sequence: SLS 1 level](images/165210163979_DV_resource.Stream@PNG-en-US.png)

Sequence: SLS 1 level

| Action |  | Motor / converter response |
| --- | --- | --- |
| ① | Selection of SLS | - The converter detects the selection of SLS. - The converter starts the SLS delay time ([p9551](SINAMICS%20Parameter%20S210.md#p9551-si-sls-delay-time-for-limit-value-change)). |
| ② |  | - The motor is braked as a result of the external setpoints. - The actual speed must remain below the SLS limit value until the SLS delay time has elapsed. |
| ③ |  | - Once the SLS delay time (p9551) has elapsed, the monitoring of SLS limit value (level 1: [p9531](SINAMICS%20Parameter%20S210.md#p953103-si-sls-limit-values-1)[0]) becomes active. - The converter signals the status "SLS active" ([r9722](SINAMICS%20Parameter%20S210.md#r9722028-si-status-signals).4). |
| ④ |  | - If the SLS limit value is violated, the converter initiates the set stop response (level 1: [p9563](SINAMICS%20Parameter%20S210.md#p956303-si-sls-stop-response)[0]). |
| ⑤ | Deselection of SLS | - The converter detects the deselection of SLS. - The motor can again be operated with higher speed setpoints (e.g. switched over to the "Automatic" mode). |

###### Additional parameters

---

###### Principle of operation of SLS with switchover of speed levels

###### Overview

Safely-Limited Speed (SLS) has 4 independent speed levels that can be switched between during operation. For each level, the converter sets a new SLS limit value. If the motor velocity violates an SLS limit value, then the converter initiates the set stop response.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Unexpectedly high speed due to incorrect parameterization**   The motor can accelerate beyond the selected SLS level if you do not parameterize the SLS limit values in an ascending order. Unexpectedly high speeds can lead to severe injury and death.  - Always parameterize SLS limit values in an ascending order:   - SLS limit value level 1 = lowest speed   - SLS limit value level 4 = highest speed |  |

###### Sequence:

The flow diagram shows SLS with switchover to a higher SLS level and to a lower SLS level. The SLS delay time is not activated when switching over from a lower SLS level to a higher SLS level. The new level is active immediately.

![Sequence: SLS 2 levels](images/165210168971_DV_resource.Stream@PNG-en-US.png)

Sequence: SLS 2 levels

| Action |  | Motor / converter response |
| --- | --- | --- |
| ① | Selection of SLS | - The converter detects the selection of SLS level 2. - The converter starts the SLS delay time ([p9551](SINAMICS%20Parameter%20S210.md#p9551-si-sls-delay-time-for-limit-value-change)). |
| ② |  | - The motor is braked as a result of the external setpoints. - The actual speed must remain below the SLS limit value until the SLS delay time has elapsed. |
| ③ |  | - Once the SLS delay time (p9551) elapses, monitoring of the SLS limit value (level 2: [p9531](SINAMICS%20Parameter%20S210.md#p953103-si-sls-limit-values-1)[1]) becomes active. - The converter signals the status "SLS active" ([r9722](SINAMICS%20Parameter%20S210.md#r9722028-si-status-signals).4) and active SLS level 2 (r9722.9 = 1, r9722.10 = 0). |
| ④ |  | - If the motor velocity violates the SLS limit value, then the converter initiates the set stop response (level 2: [p9563](SINAMICS%20Parameter%20S210.md#p956303-si-sls-stop-response)[1]) off. |
| ⑤ | Switching over to SLS level 1 | - The converter detects the selection of SLS level 1. - The converter starts the SLS delay time (p9551). The SLS limit value of level 2 remains active during the SLS delay time. |
| ⑥ |  | - The motor is braked as a result of the external setpoints. - The actual speed must remain below the SLS limit value until the SLS delay time has elapsed. |
| ⑦ |  | - Once the SLS delay time (p9551) elapses, monitoring of the SLS limit value (level 1: p9531[0]) becomes active. - The converter signals active SLS level 1 (r9722.9 = 0, r9722.10 = 0). |
| ⑧ |  | - If the motor velocity violates the SLS limit value, then the converter initiates the set stop response (level 1: p9563[0]). |
| ⑨ | Deselection of SLS | - The converter detects the deselection of SLS. - The motor can again be operated with higher speed setpoints (e.g. switched over to the "Automatic" mode). |

###### Additional parameters

---

###### Principle of operation of SLS with a variable speed limit value

###### Overview

SLS limit value, level 1 can be influenced using a PROFIsafe override. The scaled limit value is active after the override.

###### Description

SINAMICS offers the option of influencing the first SLS limit value via PROFIsafe:

- If the following conditions are satisfied, then the transfer of the 1st SLS limit value via PROFIsafe is active:

  - Speed level 1 is selected in the PROFIsafe telegram.
  - [p9604](SINAMICS%20Parameter%20S210.md#p9604030-si-enable).9 is set: Transfer of SLS limit values via PROFIsafe is enabled.
- S_SLS_LIMIT_A has the value range 1 ... 32767. The following applies:

  - 32767 ≙ 100% of the 1st SLS level
  - The actually monitored limit value is calculated as follows:  
    SLS limit value = (S_SLS_LIMIT_A/32767) · [p9531](SINAMICS%20Parameter%20S210.md#p953103-si-sls-limit-values-1)[0].
- In this case, speed levels 2, 3 and 4 can be parameterized and selected.
- The selected delay time cannot be changed during operation. If various delay times are required in the application, then this requirement must be realized using a time-delayed transfer of the SLS limit value using your control system (F‑CPU).
- If an incorrect SLS limit value is transferred, the drive responds with the stop response parameterized in [p9563](SINAMICS%20Parameter%20S210.md#p956303-si-sls-stop-response) for speed level 1 and safety alarm C01711.

###### Additional parameters

---

###### Measures when EPOS is activated

###### Overview

If the EPOS and SLS or SDI functions are activated at the same time, EPOS must be informed about the activated monitoring limits.

These monitoring limits may otherwise be violated by the setpoint value specification of EPOS. By monitoring the limit value, a violation leads to the drive being stopped and thus to the intended motion sequence being abandoned.

**Result:**

- First, the relevant safety faults are output.
- Then, the subsequent errors generated by EPOS are output.

**Remedy:**

The safety functions provide EPOS with the parameter r9733 setpoint limit values, the consideration of which prevents a safety limit violation.

###### Requirement

- In addition to EPOS, the Safety Integrated Functions SLS or SDI are also activated.

###### Procedure

1. Transfer the setpoint limitation value (r9733) to the maximum setpoint velocity of EPOS (p2594) as follows:

   - r9733[0] = p2594[1]
   - r9733[1] = p2594[2]
2. Set the delay time for SLS (p9551) so that the respective safe monitoring only becomes active after the maximum time required for reducing the speed below the limit value.

   The required deceleration time is determined by the current velocity, the jerk limitation in p2574 and the maximum deceleration in p2573.

###### Result

Correct entry prevents a safety limit violation by the EPOS setpoint value specification.

###### Additional functional features

###### Setpoint speed limit and SLS

It also makes sense to configure the speed setpoint limit at the same time that SLS is parameterized. This configuration functions in a higher-level control system that evaluates the Safety Info Channel (SIC) in telegram 700, for example.

[p9533](SINAMICS%20Parameter%20S210.md#p9533-si-sls-setpoint-speed-limiting) defines the evaluation factor to determine the setpoint limit from the selected actual speed limit as a percentage. The active limit value is evaluated using this factor, and is made available in [r9733](SINAMICS%20Parameter%20S210.md#r973302-si-effective-setpoint-velocity-limiting). r9733 is used to transfer the values to a higher-level control, for example. For example, the control system can adapt traversing speeds to SLS levels. r9733 is part of the SIC.

- r9733[0] = [p9531](SINAMICS%20Parameter%20S210.md#p953103-si-sls-limit-values-1)[x] · p9533 (converted from the load to the motor side)
- r9733[1] = -p9531[x] · p9533 (converted from the load to the motor side)

  [x] = selected SLS level

Conversion factor from the motor to the load side:

- Motor type = rotary and axis type = linear: [p9522](SINAMICS%20Parameter%20S210.md#p952207-si-gearbox-encoder-motorload-numerator)/([p9521](SINAMICS%20Parameter%20S210.md#p952107-si-gearbox-encoder-motorload-denominator) · [p9520](SINAMICS%20Parameter%20S210.md#p9520-si-leadscrew-pitch))
- Otherwise: p9522/p9521

###### Switching over between SLS limit values

The limit values are switched over binary coded using 2 PROFIsafe control bits. The statuses of the speed selection can be checked using [r9720](SINAMICS%20Parameter%20S210.md#r9720028-si-control-word).9 and r9720.10.

The actual SLS limit value can be displayed using [r9722](SINAMICS%20Parameter%20S210.md#r9722028-si-status-signals).9 and r9722.10. The precondition to display the limit value is: SLS is active (r9722.4 = 1).

Switchover to another level is possible with a time delay. The procedure corresponds to the sequences from "SLS with one speed level" with different SLS levels.

When changing over from a lower to a higher limit value, the delay time is not active. The higher limit value immediately becomes active.

###### Additional parameters

---

###### Configuring SLS

###### Overview

The "Safely-Limited Speed" ("SLS") Safety Integrated Function is used to protect a drive against unintentionally high speeds in both directions of rotation. This is achieved by monitoring the current drive speed up to a velocity limit.

"SLS" prevents a parameterized speed limit value from being exceeded. Limits must be specified based on results of the risk analysis. Up to four different SLS speed limits can be parameterized; it is possible to switch between them even if the SLS is activated.

A PROFIsafe override can also be added to SLS limit value 1. In operation, this PROFIsafe override can be varied using a PROFIsafe telegram.

###### Requirements

- The editing mode for Safety Integrated is [activated](#starting-and-ending-safety-integrated-commissioning).
- The SLS monitoring function is released in the Safety Integrated [function selection](#selecting-the-safety-functionality).

###### Setting SLS via PROFIsafe

1. Click the ![Setting SLS via PROFIsafe](images/149396101643_DV_resource.Stream@PNG-de-DE.png) button (Select SLS) in the "SLS" function view to configure control of the "SLS" Safety Integrated Function.

   The "Control" function view appears. The display of the function view depends on the basic setting of the Safety Integrated Function "SLS".

   In this function view, configure the controls via the fail-safe inputs and outputs and/or PROFIsafe (see "[Control](#control)").
2. Call the "SLS" Safety Integrated Function again.
3. Make the following settings:

   - Delay time for SLS ([p9551](SINAMICS%20Parameter%20S210.md#p9551-si-sls-delay-time-for-limit-value-change))
   - Speed limits for max. 4 levels ([p9531](SINAMICS%20Parameter%20S210.md#p953103-si-sls-limit-values-1)[0])
   - Stop responses (STO or SS1) for each level ([p9563](SINAMICS%20Parameter%20S210.md#p956303-si-sls-stop-response)[0])
   - Activate/inhibit PROFIsafe override for SLS of level 1 ([p9604](SINAMICS%20Parameter%20S210.md#p9604030-si-enable).9)

     This means that you transfer variable SLS limits via PROFIsafe to the converter.

**Result**

The velocity limit value of the drive is configured. The current SLS limit value is displayed in the field of the same name ([r9714](SINAMICS%20Parameter%20S210.md#r971407-si-diagnostics-velocity-1)[2]). The effective setpoint limit is displayed in the field of the same name ([r9733](SINAMICS%20Parameter%20S210.md#r973302-si-effective-setpoint-velocity-limiting)). It is used, for example, to transmit values to a higher-level control system, which can then, for example, adapt traversing speeds to the SLS levels.

###### Additional parameters

- [p9581](SINAMICS%20Parameter%20S210.md#p9581-si-sbr-reference-velocity-for-ss1-and-ss2-1)
- [p9582](SINAMICS%20Parameter%20S210.md#p9582-si-samsbr-delay-time-for-ss1-and-ss2)
- [p9583](SINAMICS%20Parameter%20S210.md#p9583-si-sbr-reference-time-for-ss1-and-ss2)
- [r9720](SINAMICS%20Parameter%20S210.md#r9720028-si-control-word)
- [r9722](SINAMICS%20Parameter%20S210.md#r9722028-si-status-signals)

---

##### SSM

This section contains information on the following topics:

- [Safe Speed Monitor (SSM) mode of operation](#safe-speed-monitor-ssm-mode-of-operation)
- [Configuring SSM](#configuring-ssm)

###### Safe Speed Monitor (SSM) mode of operation

###### Overview

![Overview](images/146581347083_DV_resource.Stream@PNG-de-DE.png)

Safe Speed Monitor (SSM) safely detects when the speed falls below a speed limit in both directions of motion. SSM is a pure signaling function. The converter provides a safe output signal for further processing.

If the speed of the motor exceeds the SSM limit value, no stop response is initiated, contrary to other Safety Integrated Functions.

###### Applications

SSM is suitable for the realization of enabling access to the machine by way of safe SSM feedback. For example, to ensure that protective doors can only be unlocked when the critical speeds fall below those specified.

###### Sequence:

![Sequence: SSM](images/173829547147_DV_resource.Stream@PNG-en-US.png)

Sequence: SSM

Description

| Action |  | Motor / converter response |
| --- | --- | --- |
| ① | Selection of SSM | - The converter detects the selection of SSM. - If the motor velocity is between the velocity limit and the negative velocity limit, the converter sets the signal "Speed below limit value" ([p9722](SINAMICS%20Parameter%20S210.md#r9722028-si-status-signals).15 = 1). |
| ② | Exceeding the velocity limit | - When the motor velocity exceeds the velocity limit, the converter resets the "Speed below limit value" signal (p9722.15 = 0). |
| ③ |  | - If the motor velocity falls below the velocity limit minus the hysteresis, the converter sets the signal "Speed below limit value" (p9722.15 = 1). |
| ④ | Exceeding the negative velocity limit | - If the motor velocity falls below the negative velocity limit, the converter resets the "Speed below limit value" signal (p9722.15 = 0). |
| ⑤ |  | - If the motor velocity exceeds the negative velocity limit plus the hysteresis, the converter sets the signal "Speed below limit value" (p9722.15 = 1). |

![Sequence: SSM filter](images/173830294923_DV_resource.Stream@PNG-en-US.png)

Sequence: SSM filter

The signal filter smoothes the measured value of the velocity.

The filter reduces signal changes of the SSM feedback when monitoring velocities that are just below the speed limit.

An active filter leads to a time delay of the SSM feedback.

The behavior of the signal filter can be set using filter time ([p9545](SINAMICS%20Parameter%20S210.md#p9545-si-ssm-filter-time)).

###### Example

SSM is suitable for enabling machine access through safe SSM feedback. Thus, for example, it is possible to unlock safety doors only when the velocity falls below critical levels.

> **Note**
>
> **SSM initial value during ramp-up**
>
> The initial value of the SSM signal during ramp-up can be adapted via [p9507](SINAMICS%20Parameter%20S210.md#p950789-si-function-configuration).9.
>
> - p9507.9 = 0 means "SSM status signal initialized to "1" during ramp-up".
> - p9507.9 = 1 means "SSM status signal initialized to "0" during ramp-up".

###### Additional parameters

---

###### Configuring SSM

###### Overview

The "Safe Speed Monitor" (SSM) function provides a reliable method for detecting when the velocity falls below the velocity limit ([p9546](SINAMICS%20Parameter%20S210.md#p9546-si-ssm-velocity-limit-1)) in both directions of rotation, e.g. for standstill detection. A failsafe output signal is available for further processing.

A velocity hysteresis can be configured for the "SSM" function. This is predominantly automatically active. In this way, a more stable signal characteristic of SSM can be achieved at speeds close to the velocity limit.

For the hysteresis, the velocity (or speed) determined by the two channels must not differ by more than the difference between the velocity limit and the velocity hysteresis. Otherwise it would be theoretically possible that one channel returns a HIGH signal and the other a LOW signal for "SSM".

The following figure shows the characteristic of the "SSM" safe output signal when hysteresis is active:

![Overview](images/159834983435_DV_resource.Stream@PNG-en-US.png)

The output signal for SSM is smoothed by setting a filter time with a PT1 filter ([p9545](SINAMICS%20Parameter%20S210.md#p9545-si-ssm-filter-time)).

###### Requirements

- The editing mode for Safety Integrated is [activated](#starting-and-ending-safety-integrated-commissioning).
- The SSM monitoring function is released in the Safety Integrated [function selection](#selecting-the-safety-functionality).

###### Procedure

1. Click the ![Procedure](images/148125432331_DV_resource.Stream@PNG-en-US.png) button (Select SSM) to configure control of the "SSM" function.

   The "Control" function view appears. The display of the function view depends on the basic setting of the Safety Integrated Extended Functions.

   In this function view, configure the controls via PROFIsafe (see "[Control](#control)").

   You can select the PROFIsafe telegrams in the telegram configuration. This means you also specify the required control word.
2. Call the "SSM" function view again.
3. Enter the required value in mm/min in the "Velocity hysteresis" ([p9547](SINAMICS%20Parameter%20S210.md#p9547-si-ssm-velocity-hysteresis-1)) field.
4. Enter the required limit value in mm/min in the "Velocity limit" (p9546) field.
5. Specify a time value for the PT1 filter in the "Filter time" (p9545) field.

###### Result

You have configured the safety function SSM. Save the settings in the project.

###### Additional parameters

- [r9722](SINAMICS%20Parameter%20S210.md#r9722028-si-status-signals)

---

##### SDI

This section contains information on the following topics:

- [Safe Direction (SDI) mode of operation](#safe-direction-sdi-mode-of-operation)
- [Configuring SDI](#configuring-sdi)

###### Safe Direction (SDI) mode of operation

###### Overview

![Overview](images/146581508107_DV_resource.Stream@PNG-de-DE.png)

With Safe Direction (SDI), the converter monitors the motor's direction of motion. If the motor moves in the impermissible direction, the converter stops the motor with an SDI-specific stop response.

The following SDI variants are available, depending on the direction of motion:

- SDI positive (SDI+)
- SDI negative (SDI‑)

###### Applications

SDI is suitable for the following cases:

- Machines on which cyclic material must be loaded and removed
- For protection against impermissible direction of rotation

###### Sequence:

![Sequence: SDI](images/165209841803_DV_resource.Stream@PNG-en-US.png)

Sequence: SDI

| Action |  | Response / converter |
| --- | --- | --- |
| ① | Selection of SDI+ | - The converter detects the selection of SDI+. - The converter starts the SDI delay time ([p9565](SINAMICS%20Parameter%20S210.md#p9565-si-sdi-delay-time)). |
| ② |  | - The converter monitors the motor's direction of motion once the SDI delay time expires. - The converter signals the status "SDI positive active" ([r9722](SINAMICS%20Parameter%20S210.md#r9722028-si-status-signals).12). - The converter continuously calculates the motor position. - As soon as the motor moves in the impermissible direction, the converter saves the current position and monitors the deviation between the current position and saved position. |
| ③ |  | - If the deviation between the actual position and the saved position is higher than the SDI tolerance [p9564](SINAMICS%20Parameter%20S210.md#p9564-si-sdi-tolerance-1), then the converter brakes the motor with the set stop response ([p9566](SINAMICS%20Parameter%20S210.md#p9566-si-sdi-stop-response)) and outputs a safety message <sup>1)</sup>. |
| ④ | Deselection of SDI+ | - The converter detects the deselection of SDI+. - The converter stops monitoring the motion direction. - The motor can now be moved in both directions. |
| <sup>1)</sup> The following steps are required to acknowledge the safety message: - Deselect SDI and select again - Safe acknowledgment |  |  |

> **Note**
>
> **Direction change is not detected using [p1821](SINAMICS%20Parameter%20S210.md#p18210-direction-of-rotation)**
>
> Safe monitoring is still possible if the direction of motion is reversed using p1821. However, in this case, setpoint limiting [r9733](SINAMICS%20Parameter%20S210.md#r973302-si-effective-setpoint-velocity-limiting) is calculated with the wrong direction of rotation. Parameter [p9539](SINAMICS%20Parameter%20S210.md#p953907-si-gearbox-rotation-reversal) can be used to set the direction of motion for safety monitoring.

###### Additional functional features

It also makes sense to configure the setpoint velocity limit at the same time that SDI is parameterized. This configuration functions in a higher-level control system that evaluates the Safety Info Channel (SIC), for example.

The velocity setpoint limiting is indicated in parameter r9733.

- For SDI negative (SDI-): r9733[0] = 0
- For SDI positive (SDI+): r9733[1] = 0

Velocity setpoint limiting r9733, for example, is used to transfer values to a higher-level control system. r9733 is part of the Safety Info Channel (SIC).

###### Additional parameters

---

###### Configuring SDI

###### Overview

The "Safe Direction" (SDI) function allows reliable monitoring of the direction of motion of the drive. If this function is activated, the drive can only move in the enabled direction. You can check whether SDI is active in the "[Function status](#function-status)" function view. When active, at least one of the LEDs is green:

- SDI positive active ([r9722](SINAMICS%20Parameter%20S210.md#r9722028-si-status-signals).12)
- SDI negative active (r9722.13)

> **Note**
>
> **No change of direction detected**
>
> If the direction of rotation ([p1821](SINAMICS%20Parameter%20S210.md#p18210-direction-of-rotation)) is reversed in the [basic parameterization](#basic-parameterization-1), then safe monitoring is still possible: However, in this case, the setpoint limitation [r9733](SINAMICS%20Parameter%20S210.md#r973302-si-effective-setpoint-velocity-limiting) is calculated with the wrong direction of rotation. A reversal of the direction of rotation therefore does not make sense in this case.

After selecting SDI via PROFIsafe, delay time [p9565](SINAMICS%20Parameter%20S210.md#p9565-si-sdi-delay-time) is started. During this time, you have the option of ensuring that the drive is moving in the enabled direction. After this, the "Safe Direction" function is active and the direction of motion is monitored.

If the drive now moves more than the configured tolerance ([p9564](SINAMICS%20Parameter%20S210.md#p9564-si-sdi-tolerance-1)) in the blocked direction, message C01716 is output and the stop response defined in [p9566](SINAMICS%20Parameter%20S210.md#p9566-si-sdi-stop-response) is initiated. To acknowledge the messages, you must first deselect SDI, remove the fault cause and then safely acknowledge the messages. Only then can you reselect SDI.

**Meaning of the display (SDI active)**

The "SDI active" icon indicates the following states:

| Symbol | Meaning |
| --- | --- |
| ![Overview](images/149395584907_DV_resource.Stream@PNG-de-DE.png) | SDI not selected |
| ![Overview](images/149395977739_DV_resource.Stream@PNG-de-DE.png) | SDI positive active |
| ![Overview](images/149395986315_DV_resource.Stream@PNG-de-DE.png) | SDI negative active |
| ![Overview](images/149396007691_DV_resource.Stream@PNG-de-DE.png) | SDI positive and SDI negative active |

###### Requirements

- The editing mode for Safety Integrated is [activated](#starting-and-ending-safety-integrated-commissioning).
- The SDI monitoring function is released in the Safety Integrated [function selection](#selecting-the-safety-functionality).

###### Procedure

1. Click the ![Procedure](images/148125432331_DV_resource.Stream@PNG-en-US.png) button (Select SDI) to configure control of the "SDI" function.

   The "Control" function view appears. The display of the function view depends on the basic setting of the Safety Integrated Extended Functions.

   In this function view, configure the controls via PROFIsafe (see "[Control](#control)").

   You can select the PROFIsafe telegrams in the telegram configuration. This means you also specify the required control word.
2. Call the "SDI" function view again.
3. Enter a delay time in ms in the "Delay time for selection of SDI -&gt; SDI active" (p9565) field.
4. Enter a monitoring tolerance in mm in the "Monitoring tolerance" (p9564) field.
5. Select the required stop response in the "Selection" drop-down list (p9566).
6. Click on the icon ![Procedure](images/148900571915_DV_resource.Stream@PNG-de-DE.PNG) to display a function view of the set [stop response](#stop-responses).

   Make the necessary configuration here.

###### Result

You have configured the safety function SDI. Save the settings in the project.

###### Additional parameters

- [r9720](SINAMICS%20Parameter%20S210.md#r9720028-si-control-word)
- r9733

---

##### SLA

This section contains information on the following topics:

- [Safely-Limited Acceleration (SLA) mode of operation](#safely-limited-acceleration-sla-mode-of-operation)
- [Configuring SLA](#configuring-sla)

###### Safely-Limited Acceleration (SLA) mode of operation

###### Overview

![Overview](images/146579806347_DV_resource.Stream@PNG-de-DE.png)

The Safety Integrated Function "Safely-Limited Acceleration" (SLA) ensures that the converter does not exceed a preset acceleration limit (e.g. in setup mode).

###### Applications

SLA is suitable for machines for which the permissible acceleration may not be exceeded, for example in setup mode.

###### Sequence:

![Sequence: SLA](images/173808432267_DV_resource.Stream@PNG-en-US.png)

Sequence: SLA

Description

|  |  |  |
| --- | --- | --- |
| **Action** |  | **Motor / converter response** |
| ① | Selection of SLA | - You select SLA during ongoing operation via a control bit of the PROFIsafe telegram. - The converter starts acceleration monitoring after the delay time [p9595](SINAMICS%20Parameter%20S210.md#p9595-si-sla-delay-time) has elapsed. - The converter reports the status "SLA active" in the status bit of the PROFIsafe telegram. |
| ② | Activating the SLA limit value | - After the SLA delay time (p9595) has elapsed, monitoring of the SLA limit value ([p9578](SINAMICS%20Parameter%20S210.md#p9578-si-sla-acceleration-limit-1)) is effective. - The converter signals status "SLA active" ([r9722](SINAMICS%20Parameter%20S210.md#r9722028-si-status-signals).8). - The signal filter ([p9576](SINAMICS%20Parameter%20S210.md#p9576-si-sla-filter-time)) smoothes the measured value of the acceleration. Active filtering leads to delayed triggering of the SLA stop response. |
| ③ |  | - The converter also monitors during acceleration to ensure that the specified acceleration limit is not exceeded. |
| ④ | Violation of the acceleration limit | - The converter monitors during braking that no unacceptable re-acceleration occurs. The gradient of the braking process is not monitored. |
| ⑤ | Deselection of SLA | - With the (manual or automatic program-controlled) deselection, SLA is deactivated and "Selection SLA" is reset. - The converter detects the deselection of SLA. - The converter stops acceleration monitoring. - You can traverse the axis immediately in both directions of rotation. |

###### Additional parameters

---

###### Configuring SLA

###### Overview

The safety function "Safely-Limited Acceleration" (SLA) ensures that the drive does not exceed a preset acceleration limit (e.g. in setup mode). SLA detects early on whether the drive is accelerating too quickly and initiates the fault response.

SLA has no effect with braking.

###### Requirements

- The editing mode for Safety Integrated is [activated](#starting-and-ending-safety-integrated-commissioning).
- In the Safety Integrated [function selection](#selecting-the-safety-functionality), the control mode "via terminals" is not activated.
- The SLA monitoring function is enabled in the Safety Integrated function selection.

###### Procedure

1. Click the ![Procedure](images/148125432331_DV_resource.Stream@PNG-en-US.png) button (Select SLA) to configure control of the "SLA" function.

   The "Control" function view appears. The display of the function view depends on the basic setting of the Safety Integrated Extended Functions.

   In this function view, configure the controls via PROFIsafe (see "[Control](#control)").

   You can select the PROFIsafe telegrams in the telegram configuration. This means you also specify the required control word.
2. Call the "SLA" function view again.
3. Enter a delay time in ms in the "Delay time for selection of SLA -&gt; SLA active" ([p9595](SINAMICS%20Parameter%20S210.md#p9595-si-sla-delay-time)) field.
4. Enter a value for the acceleration limit of the Safely-Limited Acceleration in the "Acceleration limit" field ([p9578](SINAMICS%20Parameter%20S210.md#p9578-si-sla-acceleration-limit-1)).

   This limit value applies to a positive and negative direction of rotation. The drive in [r9790](SINAMICS%20Parameter%20S210.md#r979001-si-sla-acceleration-resolution-1) indicates the possible acceleration resolution.
5. In the "Filter time" ([p9576](SINAMICS%20Parameter%20S210.md#p9576-si-sla-filter-time)) field, enter a value for the acceleration monitoring filter time.
6. In the "Fault response" ([p9579](SINAMICS%20Parameter%20S210.md#p9579-si-sla-stop-response)) drop-down list, choose the fault response for Safely-Limited Acceleration.

   If SLA later detects that the acceleration limit has been exceeded, the drive initiates the configured fault response.
7. Click the ![Procedure](images/147856715147_DV_resource.Stream@PNG-en-US.PNG) icon to open the function view of the set stop response (e.g. "SS1").

   If necessary, correct the settings of the underlying Safety Integrated function.
8. Click "Save project" in the toolbar to save the changes in the project.

###### Result

You have configured the safety function SLA.

**For transmission via PROFIsafe**

After SLA has been parameterized and selected, the results of monitoring are transferred in the status words S_ZSW1.8 (SLA deselection) or S_ZSW2.8 (SLA active) (see flow diagram [SLA mode of operation](#safely-limited-acceleration-sla-mode-of-operation)).

**For transmission via SIC**

After "SLA" has been parameterized and selected, the results of the monitoring are also transferred in the SIC in status word S_ZSW1B.8. You will find this status word in telegrams 700 and 701.

###### Additional parameters

---

#### Actual value acquisition/mechanical system

##### Overview

The properties of the selected encoder are displayed in this view. The load-side accuracies are calculated and displayed with the mechanical settings.

**Load-side limits and accuracies for the safe motion monitoring functions**

The safe maximum velocity [r9730](SINAMICS%20Parameter%20S210.md#r9730-si-safe-maximum-velocity-1) is determined based on the actual value acquisition system. It specifies the maximum load velocity that can still be correctly detected with the current encoder parameterization.

With the current encoder parameterization, a maximum position accuracy [r9731](SINAMICS%20Parameter%20S210.md#r9731-si-safe-position-accuracy-1) can be achieved.

##### Requirements

- The editing mode for Safety Integrated is [activated](#starting-and-ending-safety-integrated-commissioning).
- The required axis type was selected in the "[Function selection](#selecting-the-safety-functionality)".
- At least one Safety Integrated Extension Function (e.g. SS1-r/-a, SLS ...) is enabled.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

##### Procedure

> **Note**
>
> The number of encoder pulses ([p0408](SINAMICS%20Parameter%20S210.md#p04080n-rotary-encoder-pulse-number)) can be changed in the inspector window.

1. Should you wish to use a gear ratio for the gear, record the values for "Load revolutions" ([p9521](SINAMICS%20Parameter%20S210.md#p952107-si-gearbox-encoder-motorload-denominator)) and "Encoder revolutions" ([p9522](SINAMICS%20Parameter%20S210.md#p952207-si-gearbox-encoder-motorload-numerator)) necessary in this regard.  
   A gear ratio is the ratio of encoder revolutions to revolutions of the drive shaft (load revolutions).
2. If a rotational direction reversal is linked with the gear being used, activate the 'Load rotational direction reversal" ([p9539](SINAMICS%20Parameter%20S210.md#p953907-si-gearbox-rotation-reversal)) option.
3. If using the "Linear axis" axis type, set the transmission ratio between encoder and load in mm/revolution (linear axis with rotary encoder) in the "Leadscrew pitch" field ([p9520](SINAMICS%20Parameter%20S210.md#p9520-si-leadscrew-pitch)).

##### Result

You have configured the safety settings for the actual value acquisition. Save the settings in the project.

##### Additional parameters

---

#### Control

This section contains information on the following topics:

- [Overview](#overview-3)
- [Control via PROFIsafe](#control-via-profisafe)
- [Control via PROFIsafe and emergency stop via terminals](#control-via-profisafe-and-emergency-stop-via-terminals)
- [Control via terminals](#control-via-terminals)
- [Self-test of the fail-safe digital input (F-DI)](#self-test-of-the-fail-safe-digital-input-f-di)

##### Overview

###### Overview

In the "Control" function view, you configure the settings for control via PROFIsafe or via the safe inputs. These settings always relate to the Safety Integrated Functions activated in the function selection (see [Selecting the safety functionality](#selecting-the-safety-functionality)).

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Uncontrollable responses of the drive when PROFIsafe addresses are not unique**  PROFIsafe addresses can be assigned via an automated mechanism. If these automatically generated PROFIsafe addresses are not unique CPU-wide and network-wide, this can lead to uncontrollable responses of the drive. If persons are in the danger zone, accidents causing death or severe injury can occur.  - Take suitable measures to ensure that the fail-safe I/O of PROFIsafe address type 1 is addressed clearly by its fail-safe destination address. - Make sure that the F-destination address of the F-I/O (here drives) is unique CPU-wide and network-wide (system-wide) for the whole F-I/O. The F-I/O of PROFIsafe address type 2, e.g. modules of the ET 200SP type, must also be taken into account. - Note also the corresponding documentation in the TIA Portal online help in Section "[SIMATIC Safety - Configuring and programming](SIMATIC%20Safety%20-%20Configuring%20and%20Programming.md#simatic-safety---configuring-and-programming)". |  |

###### Requirements

- One of the following control types is activated in the function selection.

  - via [PROFIsafe](#control-via-profisafe)
  - via [PROFIsafe and emergency stop via terminals](#control-via-profisafe-and-emergency-stop-via-terminals)
  - via [terminals](#control-via-terminals)

  Each of the possible control types requires further specific detailed settings that are explained in greater detail below.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

###### Important functions of the control configuration

| Element | Brief description |
| --- | --- |
| Fail-safe  digital input F-DI | A fail-safe digital input (F-DI) allows Safety Integrated Functions to be selected and deselected along with a fail-safe acknowledgment. A fail-safe digital input comprises 2 channels, each with one digital input. The F-DI must be enabled in order to safely monitor the drive. |
| Discrepancy time | During the discrepancy time, the drive tolerates briefly inconsistent signals at both input terminals of the fail-safe digital input (F-DI). Permanent discrepancy indicates an error in the F-DI circuit. In this case, the drive responds with a safety message. |
| Debounce time | The debounce time specifies the maximum time an interference pulse can be present at an F-DI; during this time, the drive does not interpret the pulse as a switching operation. The drive status does not change. The drive suppresses tolerated signal changes in this way. |
| Self-test | Using test signals, the self-test checks whether the fail-safe digital input (F-DI) can be switched into the "low" safe state during the "high" signal state. The drive initiates a fault response if it does not detect a test signal. Instead of internal test signals, external dark pulses can also be used for the self-test. |

##### Control via PROFIsafe

###### Requirements

- The editing mode for Safety Integrated is [activated](#starting-and-ending-safety-integrated-commissioning).
- In the Safety Integrated [function selection](#selecting-the-safety-functionality), control "via PROFIsafe" is activated.
- The desired Safety Integrated Functions are also enabled in the function selection.

###### Configuring control via PROFIsafe

The following configuration is required for controlling the Safety Integrated Functions via PROFIsafe.

1. Click the ![Configuring control via PROFIsafe](images/148900571915_DV_resource.Stream@PNG-de-DE.PNG) icon "Telegram configuration"

   The properties of the PROFINET interface are displayed in the inspector window. The "Cyclic data exchange" setting area is active. The telegrams for the drive objects can be specified here.

   The following steps 2 and 3 apply if no PROFIsafe telegram has yet been created (e.g. via the guided quick startup).
2. Optional: Click in the telegram configuration of the "Drive control telegrams" on the entry &lt;Add telegram&gt;.
3. Optional: Select the "Add Safety telegram" option in the drop-down list of the entry:

   Then the lines "Send Safety Integrated Telegram (actual value)" and "Receive Safety Integrated Telegram (setpoint)" are inserted. PROFIsafe telegram 901 is preset. As an alternative, you can select PROFIsafe telegram 30.
4. Open the detail view "Receive Safety Integrated Telegram (setpoint)" in the inspector window.
5. Correct the PROFIsafe address of the drive in the "F-address" field.
6. Switch back to the "Control" function view.

   The communication parameters transferred to the drive (PROFIsafe telegram, F-addresses, F-monitoring time) are displayed in this function view. The value of the F-address is displayed in the "PROFIsafe address" ([p9610](SINAMICS%20Parameter%20S210.md#p9610-si-profisafe-destination-address)) field. A preassigned PROFIsafe telegram is displayed in the "PROFIsafe telegram no." drop-down list.
7. Select the response for communication failure ([p9612](SINAMICS%20Parameter%20S210.md#p9612-si-stop-response-for-failure-or-control-fault)).

**Note**

**"SS1" set as failure response**

When PROFIsafe communication fails, the drive brakes the motor using function SS1.  
The drive continues braking even if PROFIsafe communication is restored before the end of braking.  
While braking, the drive ignores all commands that it receives via PROFIsafe.  
As long as the drive brakes the motor using function SS1, then controlling STO, for example, has no effect.

###### Configuring routing

The routing must also be configured to transfer the F-DI states via PROFIsafe. Routing requires a routing-capable telegram. As a consequence, telegram 901 is required for SINAMICS S210.

1. Click the ![Configuring routing](images/148900571915_DV_resource.Stream@PNG-de-DE.PNG) icon "Telegram configuration"

   The properties of the PROFINET interface are displayed in the inspector window. The "Telegram configuration" setting area is active. The telegrams for the drive objects can be specified here.
2. Click the &lt;Add telegram&gt; entry in the telegram configuration of "Drive axis_x".
3. Select the "Add Safety Integrated telegram" option in the drop-down list of the entry.

   The "Send Safety Integrated telegram (Actual value)" and "Receive Safety Integrated telegram (Setpoint)" lines are then inserted.
4. In column "Telegram", select telegram 901 in the drop-down list of the entry.
5. Switch back to the "Control" function view of the drive.

   The "Configuration routing" area is now displayed.
6. In the "Configuration routing" area, select the input mode of the fail-safe digital input (F-DI 3).  
   To do so, in the drop-down list for the fail-safe digital input ([p10040](SINAMICS%20Parameter%20S210.md#p100400-si-f-di-input-mode).0), select whether this is to be a normally closed contact or a normally open contact.
7. Click on the connection icon ![Configuring routing](images/141470326667_DV_resource.Stream@PNG-de-DE.PNG) (p10050.0) beside the drop-down list of the fail-safe digital input to activate the transfer of the F-DI state to the F-controller.  
   The transfer is activated when the icon shows a closed connection between two points ![Configuring routing](images/141474457099_DV_resource.Stream@PNG-de-DE.PNG).

###### Configuring control via the F-DI

The signal states of an F-DI are monitored to determine whether they have assumed the same logical signal state within the discrepancy time.

The drive-internal Safety Integrated Function issues safety faults for internal faults or limit value violations.

1. Enter a discrepancy time [ms] in the "Discrepancy time" (10002) field.

   Based on the discrepancy time, the converter tolerates short-time differences in input signals. During this time the failsafe digital input (F-DI) remains guaranteed.
2. Click "Save project" in the toolbar to save the changes in the project.

**Performing the online test**

Detailed information on possible self-tests is provided on Page [Self-test of the fail-safe digital input (F-DI)](#self-test-of-the-fail-safe-digital-input-f-di).

###### Result

You have configured the control via PROFIsafe.

###### Additional parameters

- p9610

---

##### Control via PROFIsafe and emergency stop via terminals

###### Requirements

- The editing mode for Safety Integrated is [activated](#starting-and-ending-safety-integrated-commissioning).
- In the Safety Integrated [function selection](#selecting-the-safety-functionality), control "via PROFIsafe and emergency stop via terminals" is released.
- The required Safety Functions of this control type are also activated in the function selection.

###### Configuring control via PROFIsafe

The PROFIsafe address is required for control of the Safety Integrated Functions via PROFIsafe.

1. Click the ![Configuring control via PROFIsafe](images/148900571915_DV_resource.Stream@PNG-de-DE.PNG) icon "Telegram configuration"

   The properties of the PROFINET interface are displayed in the inspector window. The "Cyclic data exchange" setting area is active. The telegrams for the drive objects can be specified here.

   The following steps 2 and 3 apply if no PROFIsafe telegram has yet been created (e.g. via the guided quick startup).
2. Optional: Click in the telegram configuration of the "Drive control telegrams" on the entry &lt;Add telegram&gt;.
3. Optional: Select the "Add Safety telegram" option in the drop-down list of the entry:

   Then the lines "Send Safety Integrated Telegram (actual value)" and "Receive Safety Integrated Telegram (setpoint)" are inserted. The relevant PROFIsafe telegrams are preassigned.
4. Open the detail view "Receive Safety Integrated Telegram (setpoint)" in the inspector window.
5. Set the PROFIsafe address of the drive in the "F-address" field.
6. Switch back to the "Control" function view.

   The value of the F-address is displayed in the "PROFIsafe address" ([p9610](SINAMICS%20Parameter%20S210.md#p9610-si-profisafe-destination-address)) field. A preassigned PROFIsafe telegram is displayed in the "PROFIsafe telegram no." drop-down list.
7. Select the response for communication failure ([p9612](SINAMICS%20Parameter%20S210.md#p9612-si-stop-response-for-failure-or-control-fault)).

**Note**

**"SS1" set as failure response**

When PROFIsafe communication fails, the drive brakes the motor using function SS1.  
The drive continues braking even if PROFIsafe communication is restored before the end of braking.  
While braking, the drive ignores all commands that it receives via PROFIsafe.  
As long as the drive brakes the motor using function SS1, then controlling STO, for example, has no effect.

###### Configuring routing

The routing must also be configured to transfer the F-DI states via PROFIsafe. The following Safety Integrated telegrams are routing-capable: 901. A corresponding telegram therefore needs to be set for routing. To ensure this, proceed as follows:

1. Click the ![Configuring routing](images/148900571915_DV_resource.Stream@PNG-de-DE.PNG) icon "Telegram configuration"

   The properties of the PROFINET interface are displayed in the inspector window. The "Telegram configuration" setting area is active. The telegrams for the drive objects can be specified here.
2. Click the &lt;Add telegram&gt; entry in the telegram configuration of "Drive axis_x".
3. Select the "Add Safety Integrated telegram" option in the drop-down list of the entry.

   The "Send Safety Integrated telegram (Actual value)" and "Receive Safety Integrated telegram (Setpoint)" lines are then inserted.
4. In the "Telegram" column, select a routing-capable telegram in the drop-down list of the entry (see above).
5. Switch back to the "Control" function view of the drive.

   The "Configuration routing" area is now displayed.
6. In the "Configuration routing" area, select the input mode of the fail-safe digital input (F-DI 3).  
   To do so, in the drop-down list for the fail-safe digital input ([p10040](SINAMICS%20Parameter%20S210.md#p100400-si-f-di-input-mode).0), select whether this is to be a normally closed contact or a normally open contact.
7. Click on the connection icon ![Configuring routing](images/141470326667_DV_resource.Stream@PNG-de-DE.PNG) (p10050.0) beside the drop-down list of the fail-safe digital input to activate the transfer of the F-DI state to the F-controller.  
   The transfer is activated when the icon shows a closed connection between two points ![Configuring routing](images/141474457099_DV_resource.Stream@PNG-de-DE.PNG).

###### Configuring control via F-DI

The signal states of an F-DI are monitored to determine whether they have assumed the same logical signal state within the discrepancy time.

The drive-internal Safety Integrated Function issues safety faults for internal faults or limit value violations.

1. Select whether an emergency stop is to be activated and which failure response (STO, SS1, etc.) is to apply in the event of an emergency stop using the drop-down list "Emergency stop via terminals". The Emergency Stop functions, which were previously enabled in the function selection, can be selected.
2. Enter a discrepancy time [ms] in the "Discrepancy time" ([p10002](SINAMICS%20Parameter%20S210.md#p10002-si-f-di-changeover-discrepancy-time)) field.

   Based on the discrepancy time, the converter tolerates short-time differences in input signals. During this time the failsafe digital input (F-DI) remains guaranteed.
3. Click "Save project" in the toolbar to save the changes in the project.

**Performing the online test**

Detailed information on possible self-tests is provided on Page [Self-test of the fail-safe digital input (F-DI)](#self-test-of-the-fail-safe-digital-input-f-di).

###### Result

You have configured the control via PROFIsafe with emergency stop via terminals.

###### Additional parameters

---

##### Control via terminals

###### Requirements

- The editing mode for Safety Integrated is [activated](#starting-and-ending-safety-integrated-commissioning).
- In the Safety Integrated [function selection](#selecting-the-safety-functionality), control "via terminals" is enabled.
- The required Safety Functions of this control type are also activated in the function selection.

###### Configuring control via F-DI

The signal states of an F-DI are monitored to determine whether they have assumed the same logical signal state within the discrepancy time.

The drive-internal Safety Integrated Function issues safety faults for internal faults or limit value violations.

1. Select whether an emergency stop is to be activated and which failure response (STO or SS1) is to apply in the event of an emergency stop using the drop-down list "Emergency stop via terminals". The Emergency Stop functions, which were previously enabled in the function selection, can be selected.
2. Enter a discrepancy time [ms] in the "Discrepancy time" ([p10002](SINAMICS%20Parameter%20S210.md#p10002-si-f-di-changeover-discrepancy-time)) field.

   Based on the discrepancy time, the converter tolerates short-time differences in input signals. During this time the failsafe digital input (F-DI) remains guaranteed.
3. Select the input mode of the fail-safe digital input (F-DI 3).  
   To do so, in the drop-down list for the fail-safe digital input ([p10040](SINAMICS%20Parameter%20S210.md#p100400-si-f-di-input-mode).0), select whether this is to be a normally closed contact or a normally open contact.
4. Click "Save project" in the toolbar to save the changes in the project.

**Performing the online test**

Detailed information on possible self-tests is provided on Page [Self-test of the fail-safe digital input (F-DI)](#self-test-of-the-fail-safe-digital-input-f-di).

###### Result

You have configured the control via the F-DI.

###### Additional parameters

---

##### Self-test of the fail-safe digital input (F-DI)

###### Overview

To detect faults at an early stage, the drive continuously tests its shutdown paths, functions and interfaces.

Various modes are available for testing a fail-safe digital input (F-DI):

- Self-test with internal test signals
- Self-test by specified dark pulses (VS+)
- Self-test using externally entered dark pulses

The self-test checks with test signals at the input terminals of the F-DI whether the F-DI can be switched to the fail-safe state (to "low"). The drive initiates a fault response if it does not detect any feedback signal.

The debounce time ([p10017](SINAMICS%20Parameter%20S210.md#p1001702-si-digital-inputs-input-filter)) must be adapted to the particular test mode. If the debounce time is shorter than the test signal or dark pulse length, then the test pulse performs a switching operation.

###### Self-test with internal test signals

The drive internally generates test signals for the input circuit of the F-DI ([p10041](SINAMICS%20Parameter%20S210.md#p1004102-si-f-di-self-test-mode-selection) = 0).

The test signal length and the test cycle cannot be changed.

The following applies to the debounce time:

- p10017 &gt; 2 ms

The self-test with internal test signals complies with the following requirements:

- Safety Integrity Level (SIL) 3 according to IEC 61800‑5‑2
- Performance Level (PL) e according to EN ISO 13849-1
- Category 3 according to EN ISO 138491.

###### Self-test using entered dark pulses

The drive provides switchable voltage source VS+ at terminal block X130. VS+ generates dark pulses, e.g. to diagnose the control circuit.

The self-test using specified dark pulses with VS+ (p10041 = 1) offers additional short-circuit detection between ground and 24 V.

The dark pulse length of the switchable power supply ([p10018](SINAMICS%20Parameter%20S210.md#p10018-si-f-di-self-test-length-dark-pulses-vs)) can be parameterized. The test cycle has a fixed value of 5 seconds.

![Dark pulses through switchable power supply](images/165216227339_DV_resource.Stream@PNG-en-US.png)

Dark pulses through switchable power supply

The following applies to the debounce time:

- p10017 &gt; dark pulse length (p10018) + 2 ms

The self-test using entered dark pulses complies with the following requirements:

- Safety Integrity Level (SIL) 3 to IEC 61800-5-2
- Performance Level (PL) e according to EN ISO 13849-1
- Category 4 according to EN ISO 138491

###### Self-test using externally entered dark pulses

An electronic control, e.g. F-PLC, generates dark pulses at the input terminals of the F-DI (p10041 = 3).

The dark pulse length is determined by the control. The maximum wait time for dark pulses ([p10019](SINAMICS%20Parameter%20S210.md#p10019-si-f-di-self-test-external-dark-pulses-wait-time)) can be parameterized.

![Dark pulses through control](images/165215224843_DV_resource.Stream@PNG-en-US.png)

Dark pulses through control

The following applies to the debounce time:

- p10017 &gt; dark pulse length + 2 ms

  The test pulse length of the external control must be checked and the debounce time must be adapted.

The self-test using externally entered dark pulses complies with die following requirements:

- Safety Integrity Level (SIL) 3 to IEC 61800-5-2
- Performance Level (PL) e according to EN ISO 13849-1
- Category 4 according to EN ISO 138491

###### Making settings

1. If you want to test the configuration of F-DI 0 online, click on "Configuration online test".

   The "Online test configuration" function view is displayed.
2. Here, select the test mode (p10041) for each F-DI 0 via a drop-down list, and correct the preset input filter (p10017), if necessary.

   The debounce time specifies the maximum time an interference pulse can be present at an F-DI before it is not interpreted as a switching operation.
3. If you have selected a test mode with dark pulse, also specify the duration of the dark pulse (p10018) and the maximum dark pulse wait time (p10019) for the F-DI.

   If the terminal input is high, during operation the drive repeatedly checks each F-DI with test pulses. The test pulse has no influence on the F-DI state. The drive initiates a fault response if it does not detect a test pulse.
4. Click "Save project" in the toolbar to save the changes in the project.

###### Result

You have configured the self-test for the F-DI.

###### Additional parameters

---

#### Function status

##### Overview

The function status shows the status of the enabled Safety Integrated Functions. If a function is active, then the status indicates "active" ([r9722](SINAMICS%20Parameter%20S210.md#r9722028-si-status-signals)). When STO and SS1 are active, then an Emergency Stop is initiated. The brake is safely controlled if SBC is active. When SLS, SDI and SSM are active, then the monitoring of the particular function is also active.

- Supplementary information (depending on the function)

  - Example of SLS: Displays the active level, the active SLS limit value and the speed actual value ([r9714](SINAMICS%20Parameter%20S210.md#r971407-si-diagnostics-velocity-1)).
- Status

  - Internal event

    Provides information as to whether internal events (e.g. software faults in the drive or a discrepancy in the monitoring channels) have been signaled and whether the communications function.
- Overview of the checksums:

  - Functional checksum ([p9780](SINAMICS%20Parameter%20S210.md#r978001-si-checksum-to-check-changes)) and time stamp ([r9781](SINAMICS%20Parameter%20S210.md#r978101-si-change-control-time-stamp-days))

    The checksum displays the functional checksum of the drive and is used to track changes (safety logbook). The functional checksum corresponds to a fingerprint of the parameterized Safety Integrated functionality on the drive. The checksum is updated after Safety Integrated has been commissioned. The time stamp displays the update time.
  - Functions (offline: [p9799](SINAMICS%20Parameter%20S210.md#p9799-si-reference-checksum-over-the-configuration-of-the-drive) and online: [r9798](SINAMICS%20Parameter%20S210.md#r9798-si-actual-checksum-over-the-drive-configuration)) and PROFIsafe (offline: [p9797](SINAMICS%20Parameter%20S210.md#p9797-si-reference-checksum-profisafe-addresses) and online: [r9796](SINAMICS%20Parameter%20S210.md#r9796-si-actual-checksum-profisafe-addresses))

    The checksum is displayed using the checksum-checked parameters for the drive configuration. Based on this data, it can be identified whether the parameterization of the Safety Integrated Function was changed. The checksum of the PROFIsafe parameterization is displayed next to it.

    The checksums are calculated and displayed once offline and online commissioning have been completed.
  > **Note**
  >
  > **Changed checksums indicate a changed safety configuration**
  >
  > An acceptance test is required after changing the checksums. The system outputs the appropriate messages to indicate that an acceptance test is required. The checksums are used for documentation purposes within the scope of an acceptance test.
- Version:

  The version shows the software versions of the corresponding components relevant for Safety Integrated. This data is predominantly provided as information for service and update.

  - SINAMICS Safety firmware version
  - I/O processor firmware version
  - Encoder firmware version

##### Requirements

- Safety Integrated Functions are activated in the [function selection](#selecting-the-safety-functionality).
- There is an active online connection between the drive and the operating unit.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

##### Status messages in detail

| Display | Function status |
| --- | --- |
| ![Status messages in detail](images/146631416203_DV_resource.Stream@PNG-de-DE.png) | Function is active |
| ![Status messages in detail](images/146630242827_DV_resource.Stream@PNG-de-DE.png) | Function is not active |

##### Additional parameters

---

#### Responses to safety faults and alarms

This section contains information on the following topics:

- [Faults and alarms](#faults-and-alarms)
- [Safety message buffer and safety message history](#safety-message-buffer-and-safety-message-history)
- [Fail-safe acknowledgment of safety messages](#fail-safe-acknowledgment-of-safety-messages)
- [Stop responses](#stop-responses)

##### Faults and alarms

###### Definitions

A message comprises a letter followed by the relevant number.

The letters have the following meaning:

- A means "Alarm"
- F means "Fault"
- N means "No message" or "Internal message"
- C means "Safety message"

  In the factory state ([p3117](SINAMICS%20Parameter%20S210.md#p3117-change-safety-message-type) = 0), safety messages correspond to message type "C" and the safety message buffer is active. With p3117 = 1, safety messages correspond to message types "A" or "F". Therefore, search for Safety Integrated messages in this list only by their number without the message type (e.g. 01711).

**Detailed examples:**

| Symbol | Meaning |
| --- | --- |
| **Axxxxx** | Alarm xxxxx |
| **Fxxxxx** | Fault xxxxx |
| **Nxxxxx** | No message |
| **Cxxxxx** | Safety message (dedicated message buffer) |

###### Additional parameters

---

##### Safety message buffer and safety message history

###### Overview

The converter stores the most recent safety messages in a safety message buffer.

In the factory state ([p3117](SINAMICS%20Parameter%20S210.md#p3117-change-safety-message-type) = 0), safety messages correspond to message type "C" and the safety message buffer is active. With p3117 = 1, safety messages correspond to the message types Alarm (A) or Fault (F) and are stored in the fault buffer or the alarm buffer.

A safety message includes message code, message value, and 2 message times.

- The message code and the message value describe the message cause.
- The message value provides additional and more detailed information about the safety message.
- The message times indicate when the message occurred and when the message was resolved.

> **Note**
>
> **Extended parameterization**
>
> Safety parameters that refer to messages are part of the extended parameterization. To display these parameters in the parameter list, you first need to activate [extended parameterization](#overview-2).

###### Safety message buffer

Entry in the message buffer is made with a delay. Read the message buffer only after the converter detects a change in the buffer ([r60044](SINAMICS%20Parameter%20S210.md#r60044-si-message-buffer-counter-changes)).

The converter stores up to 8 message cases in the safety message buffer. The safety message buffer comprises the current message case and the message history.

The safety message buffer is saved to the non-volatile memory when the converter is switched off. The message history is still available when the converter is switched on again. The safety messages active before switch-off are automatically moved to the message history when the converter starts up.

![Structure of the safety message buffer S210](images/163614474379_DV_resource.Stream@PNG-en-US.png)

Structure of the safety message buffer S210

###### Current message case

The current message case contains up to 8 active messages.

The safety messages are sorted by "Message time received". If the current message case is full and an additional safety message arrives, the converter overwrites the values with Index [7]. Resolved messages are moved to the safety message history.

![Current message case](images/163614393483_DV_resource.Stream@PNG-en-US.png)

Current message case

###### Acknowledging safety messages

Once the cause of the safety message has been eliminated, the converter writes the time to "Message time resolved". The "Message time resolved" of the unresolved safety messages retains the value 0.

Safety messages are acknowledged automatically via a fail-safe digital input (F-DI) or via PROFIsafe.

Resolved and acknowledged safety messages are deleted from the active message case. Unresolved safety messages remain stored. If more than 8 messages are active, then the active message case is filled with these messages.

###### Safety message history

Up to 7 message cases with 8 already acknowledged safety messages each are stored in the safety message history.

![Moving the acknowledged safety messages to the safety message history](images/163607912587_DV_resource.Stream@PNG-en-US.png)

Moving the acknowledged safety messages to the safety message history

The converter moves the acknowledged safety messages from the current message case to the safety message history as follows:

- The converter moves the values previously saved in the safety message history by 8 indices in each case.   
  The converter deletes the safety messages that were saved in the indices [56 … 63] before the acknowledgment.
- The converter copies the current message case with the acknowledged messages to the safety message history.  
  The safety message history can contain acknowledged but unresolved messages (fault time acknowledged = 0); these messages remain as active messages until they are resolved.

###### Deleting a safety message buffer

The message buffer can be deleted as follows: [p60052](SINAMICS%20Parameter%20S210.md#p60052-si-message-cases-counter) = 0.

Parameter p60052 is also reset to 0 with POWER ON. This also clears the fault buffer.

###### Additional parameters

---

##### Fail-safe acknowledgment of safety messages

###### Overview

In the event of safety messages, e.g. due to limit violations of the motor with active Safety Integrated Functions, the converter detects an internal event.

A safety message requires a fail-safe acknowledgement.

###### Requirement

You checked and eliminated the cause of the internal event.

###### Procedure

You must acknowledge safety messages with a fail-safe signal. You have the following options for fail-safe acknowledgement:

| Acknowledgement type | Procedure |
| --- | --- |
| Via PROFIsafe | Acknowledge the fault with bit 7 of safety control words 1 or 2:   - Bit 7 = 0 → 1 → 0 |
| Via selection and deselection of STO/SS1 | Select the Safety Integrated Function STO or SS1 and then deselect again:  - Via F-DI = 1 → 0 → 1   or - With bit 0 or 1 of the PROFIsafe safety control word 1 or 2: Bit 0 or 1 = 1 → 0 → 1 |
| By switching the supply voltage on and off | Temporarily switch the power supply of the converter off and on again. |

> **Note**
>
> **Additional acknowledgement via the "standard" acknowledgement signal**
>
> Safety Integrated uses its own message type (C) by default. This message type is neither Alarm (A) nor Fault (F). You have the option of reparameterizing safety messages as faults and alarms via p3117.
>
> In this case, you must additionally acknowledge the internal event with the "Standard" acknowledgement signal.

##### Stop responses

###### Description

The drive initiates stop responses of safety functions as a result of faults. The stop responses initiate that the drive stops the motor. The response to alarms or faults, e.g. due to limit value violations, is specified or can be configured. The drive internally initiates stop responses, which do not require that an external source is selected.

In this way, you can stop the machine optimally adapted to the specific situation.

###### Overview of stop responses

You can directly select and thus activate stop functions/responses such as STO or SS1 (or SS1E, SS2, SS2E) via the function selection.

Motion monitoring functions such as SLS, SSM or SDI, on the other hand, can be configured to primarily execute one of the following stop responses in the event of limit violations; e.g. SS1. Depending on the selected stop response, further stop responses are then initiated in the further course.

If the stop/subsequent responses are not already activated in the function selection, they are enabled by the system so that they can be parameterized.

![Overview of stop variants as of SINAMICS FW V6.3](images/171308825611_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| SS1 | Safe Stop1 |
| SS1E | Safe Stop 1 external stop |
| SS2 | Safe Stop 2 |
| SS2E | Safe Stop 2 external stop |
| SCF | Safety channel failed |

Overview of stop variants as of SINAMICS FW V6.3

If a discrepancy is detected in the monitoring channels of Safety Integrated (e.g. error in result and data comparison), an SCF (Safety channel failed) is triggered. The transition to the stop response SSx can be handled with specific delay times.

###### Additional parameters

- [p9552](SINAMICS%20Parameter%20S210.md#p9552-si-transition-time-ss2-to-sos)
- [p9553](SINAMICS%20Parameter%20S210.md#p9553-si-transition-time-ss2e-to-sos)
- [p9556](SINAMICS%20Parameter%20S210.md#p9556-si-transition-time-ss1-to-sto)
- [p9594](SINAMICS%20Parameter%20S210.md#p9594-si-transition-time-ss1e-to-sto)

---

### Technology functions

This section contains information on the following topics:

- [Basic positioner (EPOS)](#basic-positioner-epos)

#### Basic positioner (EPOS)

This section contains information on the following topics:

- [Fundamentals](#fundamentals-1)
- [Function selection](#function-selection)
- [Basic parameters / Mechanical system](#basic-parameters-mechanical-system)
- [Setting the backlash](#setting-the-backlash)
- [Configuring limitations](#configuring-limitations)
- [Homing](#homing)
- [Configuring position monitoring](#configuring-position-monitoring)
- [Using traversing blocks](#using-traversing-blocks)
- [Checking the direct setpoint input (MDI)](#checking-the-direct-setpoint-input-mdi)
- [Configuring jog](#configuring-jog)
- [Function status](#function-status-1)
- [Application examples](#application-examples)

##### Fundamentals

###### Overview

The basic positioner (EPOS) calculates the traversing profile for the time-optimized traversing of the axis to the target position.

![Example: EPOS for SINAMICS S2x0](images/173378263307_DV_resource.Stream@PNG-en-US.png)

Example: EPOS for SINAMICS S2x0

Extensive positioning tasks can be performed without a higher-level controller with the basic positioner (EPOS):

- The basic positioner calculates the traversing profile for the time-optimized behavior.

  A basic positioner requires the functions of a position controller.
- The term "subordinate position control" means controlling the position of an axis.

  An "axis" is a machine or system component that comprises a converter with active position control and the driven mechanical system.

###### Requirements

- The device configuration is completely executed (an encoder has been assigned).
- The configuration in the guided quick startup was completely executed.
- The "Positioning" control mode is activated.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

###### Operating modes of the basic positioner

The basic positioner can be operated with the following operating modes:

- [Homing](#homing)

  Homing establishes the reference of the position measurement in the converter to the machine. Possible homing types:

  - Active or passive homing
  - Absolute encoder adjustment
- [Jogging](#configuring-jog)

  The "Jog" function incrementally traverses the axis (e.g. for setting up).
- [Direct setpoint input (MDI)](#checking-the-direct-setpoint-input-mdi)

  The external control specifies the set position together with the traversing profile for the axis. The converter does not save any values. This is the reason that the converter requires new target values from the control for every movement.
- [Traversing blocks](#using-traversing-blocks)

  Position setpoints are saved in different traversing blocks in the drive. The external controller only selects a saved traversing block. The drive then independently handles everything else.

###### Positioning options of the basic positioner

EPOS offers the following positioning options:

- **Linear axis**

  For a linear axis the traversing range is limited in both motor directions of rotation by the mechanical system of the machine.

  ![Positioning options of the basic positioner](images/167354006539_DV_resource.Stream@PNG-en-US.png)

  For linear axes, the position of the axis is specified as a linear measure, e.g. millimeters (mm). Application examples:

  - Stacker crane
  - Lifting platform
  - Tilting station
  - Gate/door drive

- **Rotary axis**

  The rotary axis is always configured with a standard motor.

  ![Positioning options of the basic positioner](images/167359924235_DV_resource.Stream@PNG-en-US.png)

  For rotary axes, the position of the axis is specified as an angular measure, e.g. degrees (°). Application examples:

  - Rotary table
  - Conveyor belt
  - Roller conveyor
- Absolute positioning

  The converter interprets the set position as an absolute set position relative to the machine zero/home position.
- Relative positioning

  The converter interprets the set position as set position relative to the current starting position.

###### Measurement unit MU

In the factory setting, the units of the basic positioner use measurement unit "MU".

The table below shows the supported measurement units for position and velocity:

| Position | Velocity |
| --- | --- |
| LU  The value range of LU use is limited to +/-16 000 000. | LU/s |
| nm, μm, mm, m, km | mm/s, mm/min, mm/h, m/s, m/min, m/h, km/min, km/h |
| in, ft, mi | in/s, in/min, ft/s, ft/min, mi/h |
| Degrees (°) | Degrees (°)/s, degrees (°)/min |

Correspondingly, acceleration is set as measurement unit position/s<sup>2</sup>.

Correspondingly, jerk is set as measurement unit position/s<sup>3</sup>.

All information and displays correspond to the selected measurement unit.

All values are reset to the default values when changing the measurement unit and the axis type.

The required unit can be defined in the "[Basic parameters / Mechanical system](#basic-parameters-mechanical-system)" function view.

##### Function selection

###### Overview

If you are using a basic positioner, you can also activate the EPOS functions via the "Function selection" function view in the parameterization as an alternative to quick startup.

> **Note**
>
> **Interactions with Safety Integrated Functions**
>
> If your drive uses extended Safety Integrated Functions, EPOS must be informed about the monitoring limits activated in SLS or SDI.

###### Requirements

- The device configuration is completely executed (an encoder has been assigned).
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

###### Procedure

1. Select the "Basic positioner via telegram" option in the "Function selection" drop-down list.

   An overview of the existing EPOS functions is then displayed. Individual elements of this overview are directly linked to the individual functions.
2. Click the button of an EPOS individual function.

   The function view now displays the detailed settings of the selected EPOS function.

**Note**

The option "No basic positioner function" deactivates the EPOS functions again and the control mode "Speed controller" is active.

###### Result

The EPOS functionality is now activated and can be configured.

At the same time, however, the "Speed control" control type is also deactivated. All settings made for this control type are ignored. Limit values that refer to speed control are completely hidden ("Limitations" area in "Basic parameterization").

---

**See also**

[Measures when EPOS is activated](#measures-when-epos-is-activated)

##### Basic parameters / Mechanical system

###### Overview

In the "Basic parameters / Mechanical system" function view, you define detailed settings for the "Positioning" control method. You define:

- The motion type of the drive
- Detailed settings for the encoder type of the position control used
- Detailed settings of the modulo offset

###### Requirements

- The device configuration is completely executed (an encoder has been assigned).
- The "Positioning" control mode is activated.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

###### Procedure

1. Select the motion type that you wish to use for the drive when positioning.

   - Rotary motion

     ![Procedure](images/167359924235_DV_resource.Stream@PNG-en-US.png)

     ![Procedure](images/167359924235_DV_resource.Stream@PNG-en-US.png)
   - Linear motion

     ![Procedure](images/167354006539_DV_resource.Stream@PNG-en-US.png)

     ![Procedure](images/167354006539_DV_resource.Stream@PNG-en-US.png)
2. Then select the measurement units for position and velocity.

   The length unit "LU" is used in the factory setting. The units that can be set depend on the motion type.

   All values are reset to the default values when changing the measurement unit and the axis type.
3. Use the settings for the motor encoder used for the position control:

   Acquire the number of motor revolutions (p2504) and load revolutions (p2505).
4. If you wish to apply modulo correction:

   - To do this, activate option "Modulo correction activation" (c2577).
   - Define the modulo range (p2576).
5. Optional: If you work with backlash, measure the backlash and set the backlash compensation (see [Setting the backlash](#setting-the-backlash)).
6. Click on "Next" to display the next quick startup step.

###### Result

Startdrive defines the default settings of the setup based on what you have specified.

##### Setting the backlash

###### Overview

"Backlash" (also called play, gap) is the distance or the angle that a motor must travel through when the direction of rotation reverses until the axis actually moves in the other direction.

![Example: Backlash](images/171125903627_DV_resource.Stream@PNG-de-DE.png)

Example: Backlash

**Backlash compensation**

When a mechanical force is transmitted between a machine part and its drive, backlash generally occurs. If the mechanical system were adjusted so that absolutely no backlash occurs, this would result in high wear.

If the axis with indirect position detection is operated in a process in which a reversal of direction occurs during the traverse movement, mechanical backlashes can result in an incorrect traverse distance. The axis either traverses too far or not far enough.

To compensate for the backlash, the determined backlash must be specified with the correct sign in p2583. With each direction reversal, the actual value of the axis is then calculated in a corrective manner depending on the current traversing direction and displayed in r2667. This value is calculated into the actual position value via p2516 (position offset).

Parameter c2604 (home position approach start direction) becomes relevant for the connection of the compensation value in the following cases:

- A stationary axis is referenced by setting the home position.
- An adjusted axis is switched on with the absolute encoder.

###### Requirements

- The device configuration is completely executed (an encoder has been assigned).
- The "Positioning" control mode is activated.
- The axis was adjusted for absolute measuring systems.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

###### Measuring backlash

Proceed as follows to measure the backlash:

1. Traverse the axis to position A in the machine. Mark this position in the machine. Make a note of the actual position value in the converter.
2. Move the axis a little bit more in the same direction.
3. Traverse the axis in the opposite direction until the actual position value in the converter shows the same value as at position A.

   Due to the backlash, the axis is now at position B.
4. Measure the position difference Δ = A ‑ B in the machine.

   ![Example: Measuring backlash](images/171126752907_DV_resource.Stream@PNG-de-DE.png)

   ![Example: Measuring backlash](images/171126752907_DV_resource.Stream@PNG-de-DE.png)

   Example: Measuring backlash

###### Defining backlash compensation

1. Enter the backlash compensation value in the "Backlash" field (p2583) with the correct sign.

##### Configuring limitations

This section contains information on the following topics:

- [Configuring position limits](#configuring-position-limits)
- [Configuring dynamic response limits](#configuring-dynamic-response-limits)

###### Configuring position limits

###### Overview

The settings of the position control words and position status words of telegrams 111 or 112 define whether a SW limit switch or a HW limit switch is active.

In the "Position limits" function view, you define the negative and positive end positions of the SW limit switch for the "basic positioner".

![Position limiting](images/171136439819_DV_resource.Stream@PNG-en-US.png)

Position limiting

###### Requirements

- The device configuration is completely executed (an encoder has been assigned).
- The configuration in the guided quick startup was completely executed.
- The "Positioning" control mode is activated.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

###### Procedure

1. Acquire the values for the negative end position ([p2580](SINAMICS%20Parameter%20S210.md#p2580-epos-negative-software-limit-switch-1)) and the positive end position ([p2581](SINAMICS%20Parameter%20S210.md#p2581-epos-positive-software-limit-switch-1)) of the SW limit switch.

   Both values are preassigned with the factory settings.
2. Save the settings.

###### Result

Drive configuration continues based on the selected positioning settings.

###### Additional parameters

- c2569
- c2570

---

###### Configuring dynamic response limits

###### Overview

You can define the limitations of the traversing profile for the basic positioner in function view "Dynamic response limits". The drive calculates the traversing profile when positioning from specified values for velocity, acceleration and jerk (= acceleration change with respect to time).

![Example: Traversing profile with or without jerk limitation](images/162353283339_DV_resource.Stream@PNG-en-US.png)

Example: Traversing profile with or without jerk limitation

A lower limitation is necessary if the axis must traverse more slowly or must accelerate at a lower rate or "more softly". The lower a limitation is, the longer the drive requires to position the axis.

###### Requirements

- The device configuration is completely executed (an encoder has been assigned).
- The configuration in the guided quick startup was completely executed.
- The "Positioning" control mode is activated.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

###### Specifying the maximum traversing profile limitation

1. Correct the specified value for the maximum velocity in the "Max. velocity" field ([p2571](SINAMICS%20Parameter%20S210.md#p2571-epos-maximum-velocity-1)).

   The maximum velocity defines the maximum travel velocity. A change immediately limits the velocity of an active traversing block.

   The "Corresponds to speed" field displays the converted speed, the "Max. speed" field displays the maximum speed.

   The limitation acts when positioning (jogging, processing the traversing blocks, direct setpoint input, home position approach).
2. Correct the specified value for the acceleration at "Max. acceleration" ([p2572](SINAMICS%20Parameter%20S210.md#p2572-epos-maximum-acceleration-1)).

   The "Corresponds to ... ramp-up time" field displays the converted ramp-up time.
3. Correct the specified value for the deceleration at "Max. deceleration" ([p2573](SINAMICS%20Parameter%20S210.md#p2573-epos-maximum-deceleration-1)).

   The "Corresponds to ... ramp-down time" field displays the converted ramp-down time.

   The maximum acceleration and maximum deceleration specify the maximum acceleration for increasing the velocity and the maximum deceleration for reducing the velocity. Both values act when positioning (jogging, processing the traversing blocks, direct setpoint input, home position approach).
4. Save the settings.

###### Specifying the traversing profile limitation in relation to the maximum speed

The velocity, acceleration and deceleration limitation values do not apply for faults or for a safe stop. Instead, the ramp-down times for OFF1 and OFF3 are used. The proposed ramp-down time is displayed in the "Ramp-down time in relation to max. speed" field.

1. If you want to apply this ramp-down time in OFF1, click the "Accept values" button.

   The ramp-down time is now applied to the "OFF1 ramp-down time" ([p1121](SINAMICS%20Parameter%20S210.md#p11210-off1-ramp-down-time)) field.
2. Manually enter the required value in field "Ramp-down time (OFF3)" ([p1135](SINAMICS%20Parameter%20S210.md#p11350-off3-ramp-down-time)).
3. Save the settings.

###### Specifying the maximum jerk limitation

A jerk limitation delays the acceleration. Proceed as follows:

1. Activate option "Jerk limitation".
2. Enter a value for the maximum jerk limitation under "Max. jerk" ([p2574](SINAMICS%20Parameter%20S210.md#p2574-epos-jerk-limiting-1)).

   The converted values for the rounding times are displayed in the fields below the diagram.
3. Save the settings.

###### Result

Drive configuration continues based on the selected positioning settings.

###### Additional parameters

---

##### Homing

This section contains information on the following topics:

- [Configuring active homing](#configuring-active-homing-1)
- [Configuring passive homing](#configuring-passive-homing)
- [Configuring absolute encoder adjustment](#configuring-absolute-encoder-adjustment-1)

###### Configuring active homing

###### Overview

With an incremental measuring system, the drive can be homed without requiring a higher-level control. Active homing can be used to traverse to a home position.

The drive itself controls and monitors the homing cycle. There are 3 homing modes for active homing.

###### Requirements

- The device configuration is completely executed (an encoder has been assigned).
- The configuration in the guided quick startup was completely executed.
- The "Positioning" control mode is activated.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

###### Procedure

| Symbol | Meaning |
| --- | --- |
| 1. In function view "Active homing" select the required homing mode in field "Homing mode selection".       | Symbol | Meaning |    | --- | --- |    | ① | Encoder zero mark and homing cam |    | ② | Encoder zero mark |    | ③ | External zero mark via digital input | 2. Optional (for ① and ③):  For home position approach, enter the approach velocity to the reference cam in field "to the reference cam" ([p2605](SINAMICS%20Parameter%20S210.md#p2605-epos-active-homing-approach-velocity-reference-cam-1)). 3. In the "to the zero mark" ([p2608](SINAMICS%20Parameter%20S210.md#p2608-epos-active-homing-approach-velocity-zero-mark-1)) field, enter the approach velocity after detecting the reference cam when searching for the zero mark during home position approach. 4. Optional (for ③):  From drop-down list "Digital input of the external zero mark" ([p0494](SINAMICS%20Parameter%20S210.md#p04940n-equivalent-zero-mark-input-terminal)) select the input terminal to connect a zero mark replacement.    This parameter supplies incorrect measured values during an active measurement. In this particular case, it is not permissible to write to the parameter. 5. If absolute encoder adjustment should be automatically performed after home position approach, then activate option "carry out adjustment after home position approach" ([p2584](SINAMICS%20Parameter%20S210.md#p258403-epos-functions-configuration).3). 6. Enter the required home position offset for the home position approach in field "Home position offset" ([p2600](SINAMICS%20Parameter%20S210.md#p2600-epos-active-homing-home-position-offset-1)). 7. Save the settings. |  |

###### Result

Drive configuration continues based on the selected positioning settings. The approach direction and the home position are specified by the selected telegram.

###### Additional parameters

---

###### Configuring passive homing

###### Overview

For passive (flying) homing, homing is superimposed on the traversing block. In this case, the traversing block of the associated operating mode is executed and the evaluation of the measuring probe is also activated.

When the measuring probe is detected, the difference between the home position and the determined measured value is corrected on-the-fly (i.e. during motion). When doing this, window limits are evaluated. The traversing block is then executed to the end.

###### Requirements

- The device configuration is completely executed (an encoder has been assigned).
- The configuration in the guided quick startup was completely executed.
- The "Positioning" control mode is activated.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

###### Procedure

1. In function view "Passive homing" select the input terminal for direct measuring probe 1 in drop-down list "Digital input of measuring probe 1 for the zero mark " (p2517).

   The direct measuring probe can be parameterized as non-cyclic (value = 1 ... 8) or cyclic (value = 11 ... 18) probe.
2. Optional: Switch over the signal edge.

   Field "Homing position" (c2598) shows the fixed position value of the home position coordinate.
3. Save the settings.

###### Result

Drive configuration continues based on the selected positioning settings.

###### Additional parameters

---

###### Configuring absolute encoder adjustment

###### Overview

Absolute encoders must be adjusted during commissioning. When the machine is switched off, the position information of the encoder is retained. The absolute encoder is therefore first adjusted to the home position, e.g. by jogging.

###### Requirements

- The device configuration is completely executed (an encoder has been assigned).
- The "Positioning" control mode is activated.
- An online connection to the drive has been established.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

###### Setting the home position coordinate

1. Select function view "Absolute encoder adjustment".

   The absolute encoder adjustment settings are displayed.
2. Optional: Establish an online connection to the drive if an online connection does not already exist.
3. Click on "Set" ([p2507](SINAMICS%20Parameter%20S210.md#p25070n-lr-absolute-encoder-adjustment-status) = 2).

   Status display "Home position set" ([r2684](SINAMICS%20Parameter%20S210.md#r2684015-epos-status-word-2).11) is then updated. When the adjustment is correct, entry "Absolute encoder adjusted" is displayed in field "Absolute encoder adjustment state".

###### Resetting the home position coordinate

1. Click on "Reset" (p2507 = 1) in function view "Absolute encoder adjustment".

   The status display for the absolute value adjustment is then updated (p2507[0]). The adjustment is deactivated.

   Status display "Home position set" (r2684.11) is then updated. After the reset, entry "Absolute encoder not adjusted" is displayed in field "Absolute encoder adjustment state".
2. Optional: Then set a new home position coordinate.

###### Result

Drive configuration continues based on the selected positioning settings. The home position coordinate (c2598) is set via a telegram.

###### Additional parameters

- c2511

---

##### Configuring position monitoring

This section contains information on the following topics:

- [Positioning and standstill monitoring](#positioning-and-standstill-monitoring)
- [Following error monitoring](#following-error-monitoring)

###### Positioning and standstill monitoring

###### Overview

Monitoring comprises the following parts:

- Positioning monitoring

  On the basis of a positioning window, the entry of the axis into the specified position at the end of a positioning motion is monitored. A positioning window and a time interval are specified.

  ![Positioning monitoring](images/166142703627_DV_resource.Stream@PNG-en-US.png)

  Positioning monitoring
- Standstill monitoring

  The standstill monitoring monitors the actual position of the axis after traversing motion has been completed. 2 windows are specified for the standstill monitoring.

  ![Standstill monitoring](images/166143936651_DV_resource.Stream@PNG-en-US.png)

  Standstill monitoring

###### Requirements

- The device configuration is completely executed (an encoder has been assigned).
- The "Positioning" control mode is activated.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

###### Procedure

1. Enter a value   
   (value = 0, positioning monitoring is deactivated; value &gt;= 1, positioning monitoring is activated) in the "Positioning window" ([p2544](SINAMICS%20Parameter%20S210.md#p2544-lr-positioning-window-1)) field.

   The positioning window defines the range around the target position in which the actual position value must lie after the positioning monitoring time has expired.
2. Enter a value in the "Positioning monitoring time" ([p2545](SINAMICS%20Parameter%20S210.md#p2545-lr-positioning-monitoring-time)) field.

   The positioning monitoring time defines the interval in which the following error must lie once within the positioning window, after the time expires.
3. Enter a value   
   (value = 0, standstill monitoring is deactivated; value ≥ 1, standstill monitoring is activated) in the "Standstill window" ([p2542](SINAMICS%20Parameter%20S210.md#p2542-lr-standstill-window-1)) field.

   The standstill window defines the range around the target position in which the actual position value must lie after the standstill monitoring time has expired.
4. Enter a value in the "Standstill monitoring time" ([p2543](SINAMICS%20Parameter%20S210.md#p2543-lr-standstill-monitoring-time)) field.

   The standstill monitoring time defines the interval which after it expires the following error must lie within the standstill window. The standstill window is cyclically monitored.
5. Save the settings in the project.

###### Result

The settings for the positioning and standstill monitoring have been made.

The drive sets the "Setpoint stationary" signal to 1 as soon as the setpoint for the position within a positioning operation no longer changes. With this signal, the drive starts to monitor the actual position value:

- As soon as the axis has reached the positioning window, the drive signals that the target has been reached, and maintains the axis in closed-loop control.
- The drive signals fault F07450 if the axis does not come to a standstill within the standstill monitoring time.
- The drive signals fault F07451 if the axis does not enter the positioning window within the positioning monitoring time.

###### Additional parameters

---

###### Following error monitoring

###### Overview

A following error is the difference between a ramp-shaped, variable position setpoint and the associated actual position value. The more dynamic a control loop, the smaller the resulting following error. A maximum following error for the actual position value is often specified for monitoring position control loops. If this following error is violated, the position control cancels the current positioning operation and generates a fault message.

![Following error](images/162356999563_DV_resource.Stream@PNG-en-US.png)

Following error

Subsequently you can define the highest possible following error.

###### Requirements

- The device configuration is completely executed (an encoder has been assigned).
- The "Positioning" control mode is activated.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

###### Procedure

1. Enter the maximum deviation between the calculated and the measured actual position value before an error occurs in the "Maximum following error" ([p2546](SINAMICS%20Parameter%20S210.md#p25460-lr-dynamic-following-error-monitoring-tolerance-1)) field.
2. Save the settings in the project.

###### Result

The following error monitoring settings have been made. Following error monitoring is activated as soon as the entered value p2546 ≥ 1.

###### Additional parameters

---

##### Using traversing blocks

This section contains information on the following topics:

- [Configuring traversing blocks](#configuring-traversing-blocks)
- [Traversing blocks in detail](#traversing-blocks-in-detail)

###### Configuring traversing blocks

###### Overview

Depending on the drive, you can define 32 to 64 traversing blocks in a configuration table in the "Traversing blocks" function view. For each traversing block, define a fixed position actual value and an additional parameter. An external control can subsequently select a traversing block that has been selected.

Function "Travel to fixed stop" is one of the configuration parameters. Using this function you can traverse a spindle sleeve against a workpiece with a specified clamping torque, for example. You define the clamping torque in the traversing block. Set the fixed stop monitoring window in dialog "Travel to fixed stop". This allows the drive to traverse beyond the window if the fixed stop breaks away.

###### Requirements

- The device configuration is completely executed (an encoder has been assigned).
- The "Positioning" control mode is activated.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

###### Procedure

1. Enter the maximum number of traversing blocks.

   The number of rows in the table then changes accordingly.

   If you reduce the number of traversing blocks, then the excess traversing blocks are lost.
2. Define the required settings for each traversing block (see "[Traversing blocks in detail](#traversing-blocks-in-detail)").
3. Click on "Fixed stop configuration".

   A dialog with the same name opens.

   - Enter the value for "Following error for the fixed stop detection" ([p2634](SINAMICS%20Parameter%20S210.md#p26340-epos-fixed-stop-maximum-following-error-1)) in the input field with the same name.

     When this following error value is exceeded, this indicates that the "Fixed stop reached" state has been reached.
   - Enter the value for "Position tolerance after fixed stop detection" ([p2635](SINAMICS%20Parameter%20S210.md#p2635-epos-fixed-stop-monitoring-window-1)) in the input field with the same name.

     This value defines the monitoring window of the actual position after the fixed stop is reached.
   - Click on "Close" once all the necessary settings have been made.

     The dialog closes.
4. Optional: If you additionally want to configure the settings for the external block changes, proceed as follows:

   - Click the "external block change" button.
   - In the dialog select in the "External block change" drop-down list whether you want to carry out the block change with the measuring input (factory setting) or via parameter c2633.
   - In the "Activate measuring probe 1" drop-down list, select whether you want to use the preset measuring probe 1 or no measuring probe.
   - Click on "Close" once all the necessary settings have been made.
5. Save the settings.

###### Result

The traversing blocks are configured.

###### Additional parameters

---

###### Traversing blocks in detail

###### Overview

Depending on the drive, you can define 32 to 64 traversing blocks in the "Traversing blocks" function view. You parameterize each individual traversing block in the table. You can enter the various parameters in the columns. Expert knowledge is required to define the traversing blocks.

###### Settings

| Column | Setting | Description |
| --- | --- | --- |
| **Index** | - | The column shows the index of the corresponding parameters. |
| **Number**    **[-1,0, ... 31]** | - | The number represents the block number (p2616). It is used to uniquely identify the task for the selection using the block selection bit 0 ... 5 signals. Several tasks are processed in an ascending order. Traversing tasks with number -1 are ignored.   This allows the task to be removed from the sequence without deleting it. The task number can be assigned as required [0 ... 31]. For example, a task 5 can be defined after task 2. Numbers 3 and 4 are then reserved for subsequent processing. |
| **Task** | - | Required traversing task |
| [1] POSITIONING | Initiates traversing motion until the target position is reached. |  |
| [2] FIXED STOP | Allows a clamping torque and a clamping force to be entered for the fixed stop.  Activates the "Fixed stop configuration" button with which a dialog to configure the fixed stop parameters can be called. |  |
| [3] ENDLESS_POS | Accelerates to the defined velocity:  - Until the software limit switch is reached - Until the traversing range limit is reached - Until motion is interrupted by OC/intermediate stop. - Until motion is canceled by OC/Reject traversing block. |  |
| [4] ENDLESS_NEG | See "ENDLESS_POS". |  |
| [5] WAIT | Defines a wait time for the following task. |  |
| [6] GOTO | Allows jumps within a series of traversing tasks. The block number to which the jump is to be made must be specified as task parameter (see below). |  |
| [7] SET_O | Allows up to 2 digital outputs to be simultaneously set. |  |
| [8] RESET_O | Allows up to 2 digital outputs to be simultaneously reset. |  |
| [9] JERK | Allows a jerk limitation. |  |
| **Parameter** | - | Additional information for the tasks. |
| WAIT | Wait time in [ms] |  |
| GOTO | Block number (see task) |  |
| SET_O | Sets a digital output 1, 2 or both (3). |  |
| RESET_O | Resets a digital output 1, 2 or both (3). |  |
| Jerk | "1" to activate or "0" to deactivate |  |
| FIXED STOP | Enters the clamping torque (rotary 0...65536 [0.01 Nm]) and the clamping force (linear 0...65536 [N]) |  |
| **Mode** | - | Required positioning mode |
| ABSOLUTE | Travel to the specified position. |  |
| RELATIVE | The axis is traversed by the specified value. |  |
| ABS_POS | The specified position is approached in the direction of increasing position actual values (only when modulo correction is activated). |  |
| ABS_NEG | The specified position is approached in the direction of decreasing position actual values (only when modulo correction is activated). |  |
| **Position** | - | Target position to be approached in the traversing block. |
| **Velocity** | - | Execution speed for the traversing command. The value is influenced by the velocity override. |
| **Acceleration** | - | Value for the acceleration override, which influences the maximum acceleration. |
| **Deceleration** | - | Value for the deceleration override, which influences the maximum deceleration. |
| **Transition** | - | The transition specifies the continuation condition when the next traversing task is to be activated. |
| END | Ends the traversing task. The continuation condition can be used for pure single operation (each task is started individually) or for the last traversing task of a sequence. |  |
| CONTINUE_WITH_STOP | The position specified in the traversing block is precisely approached and the axis is braked to standstill. The following task is performed without a restart using the "activate traversing task" (c2631) signal as soon as the actual position lies within the positioning window. |  |
| CONTINUE_FLYING | The following traversing block is processed immediately when the time to apply the brake is reached. If the direction must be reversed, then the response corresponds to that for CONTINUE_WITH_STOP. The axis is braked down to standstill. |  |
| CONTINUE_EXTERNAL | The response is the same as CONTINUE_FLYING However, until the brake closes, an immediate block change can be initiated. If an external block change is not triggered, a flying changeover is made to the next block at the brake closing time. |  |
| CONTINUE_EXTERNAL_WAIT | A flying changeover to the next task can be triggered during the entire motion phase using control signal "External block change". If an "external block change" is not initiated, the axis remains in the parameterized target position until the signal is issued. |  |
| CONTINUE_EXTERNAL_ALARM | The response is the same as for CONTINUE_EXTERNAL_WAIT. However, alarm A07463 "External traversing block change in traversing block x not requested" is output if an "external block change" has not been initiated before standstill is reached. The alarm can be converted to an alarm with a stop response so that block processing can be canceled if the control signal is not issued. |  |
| **Hide** | - | Hidden traversing tasks are not processed. The traversing task then responds in exactly the same way as if it had task number -1. |

##### Checking the direct setpoint input (MDI)

###### Overview

The external control specifies the position value and also the traversing profile for the axis. As the drive does not save, new target values must also be specified by the control for new movements.

The following setpoints are entered via the PLC communications:

- "Position setpoint" (c2642)
- "Velocity setpoint" (c2643)
- "Acceleration override" (c2644)
- "Deceleration override" (c2645)

You can check these setpoints in this diagnostics view for diagnostic purposes.

###### Requirements

- The device configuration is completely executed (an encoder has been assigned).
- The "Positioning" control mode is activated.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

###### Procedure

1. Check the setpoints.

###### Result

None

###### Additional parameters

---

##### Configuring jog

###### Overview

Jog is the simplest position-controlled traversing option. Using "EPOS jog"incremental, the drive can be traversed either endlessly (jog) or can be traversed by a distance that can be parameterized. When jogging, acceleration or deceleration is with the parameterized maximum acceleration or maximum deceleration.

The following parameters can be set for EPOS jog:

- Velocity setpoint (either for jog 1 or 2)
- Traversing distances (either for jog 1 or 2)

###### Requirements

- The device configuration is completely executed (an encoder has been assigned).
- The "Positioning" control mode is activated.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

###### Procedure

| Symbol | Meaning |
| --- | --- |
| 1. In function view "Jog", make the following settings for incremental jogging:        | Symbol | Meaning |    | --- | --- |    | Jog 1 | "Velocity setpoint 1" ([p2585](SINAMICS%20Parameter%20S210.md#p2585-epos-jog-1-setpoint-velocity-1)) |    | "Traversing path 1" ([p2587](SINAMICS%20Parameter%20S210.md#p2587-epos-jog-1-traversing-distance-1)) |  |    | Jog 2 | "Velocity setpoint 2" ([p2586](SINAMICS%20Parameter%20S210.md#p2586-epos-jog-2-setpoint-velocity-1)) |    | "Traversing path 2" ([p2588](SINAMICS%20Parameter%20S210.md#p2588-epos-jog-2-traversing-distance-1)) |  | 2. Save the settings. |  |

###### Result

Drive configuration continues based on the selected positioning settings.

###### Additional parameters

- [p2572](SINAMICS%20Parameter%20S210.md#p2572-epos-maximum-acceleration-1)
- [p2573](SINAMICS%20Parameter%20S210.md#p2573-epos-maximum-deceleration-1)
- c2589
- c2590
- c2591

---

##### Function status

###### Overview

The function status shows the status of the enabled EPOS functions. If a function is active, then the status indicates "active".

- Operating mode

  Shows which EPOS operating mode is active ([r2669](SINAMICS%20Parameter%20S210.md#r266905-epos-actual-operating-mode)).
- Enables

  Shows the existing enables of the basic positioner.

  Missing enables are also shown.
- Status

  Shows the detailed status of individual EPOS functions.

  Actual values and setpoints are displayed for velocity and position.

  The same is true for distance to go and actual following error.

###### Requirements

- There is an active online connection between the drive and the operating unit.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

###### Additional parameters

---

##### Application examples

Application examples for configuring EPOS for SINAMICS drives are provided in the Internet at the following address:

- [Interaction between SIMATIC controls and SINAMICS drives](https://support.industry.siemens.com/cs/ww/en/view/60733299)

## Rotate & optimize

This section contains information on the following topics:

- [Overview](#overview-4)
- [Traverse the drive from the control panel by specifying the speed](#traverse-the-drive-from-the-control-panel-by-specifying-the-speed)
- [Testing EPOS settings with the control panel](#testing-epos-settings-with-the-control-panel)
- [Performing One Button Tuning](#performing-one-button-tuning)

### Overview

After the device configuration and the basic setting of the drive in the guided quick startup, drive optimizations can be performed.

> **Note**
>
> **No editing mode required**
>
> No special editing mode is required for the optimizations.

The following requirements must be met for drive optimization:

#### Requirements

- The drive has been completely created and specified in the device configuration.
- The basic parameterization has been completed in the [guided quick startup](#guided-quick-startup).
- There is an active [online connection](Configuring%20SINAMICS%20S210%20drives%20%28StdrS210fromRTv61ConfenUS%29.md#establishing-an-online-connection-to-the-target-device) between the drive and the operating unit.
- If the project protection is activated:

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

### Traverse the drive from the control panel by specifying the speed

#### Overview

You can use the control panel to traverse the drive and therefore test the settings that have been made.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Incorrect operation if the safety instructions for the control panel are not observed**  The safety shutdowns from the higher-level controller have no effect with this function. The **Stop with spacebar** function is not guaranteed in all operating modes. Incorrect operation by untrained personnel and non-observance of the appropriate safety instructions can result in death or serious injury.   - Make sure that this function is only used for commissioning, diagnostic and service purposes. - Make sure that this function is only used by trained and authorized skilled personnel. - Make sure that the EMERGENCY OFF circuit is always implemented as hardware. |  |

> **Note**
>
> **Drive reacts immediately**
>
> Although all enables are removed before returning the master control, the setpoints and commands still come from the original parameterized sources after the control priority is returned.

#### Requirements

- An online connection to the drive has been established.
- If the project protection is activated:

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

#### Step 1: Activate master control

When an online connection has been established, the bar in the header area is shown in color. The control elements are grayed-out apart from the "Activate" button. The remaining control elements become active only after you have activated the master control and set the enables.

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
| 1. Click the "Activate" button under "Master control".    The "Activate master control" message window opens. 2. Read the warning carefully. Check the monitoring time and if required, correct it.    The monitoring time specifies the time during which the connection from the operating unit to the drive is cyclically monitored. The minimum value is 1000 ms. 3. The "Stop with spacebar" option is active by default. When the option is activated the drive is always braked using the shutdown function OFF3 if you press the spacebar or if the focus switches. The focus switches when a dialog is opened (e.g. download dialog) or when switching from TIA Portal to another application.       | Symbol | Meaning |    | --- | --- |    |  | **Warning** |    | **Braking not guaranteed if the "Stop with spacebar" option is deactivated** Stopping by using the buttons on the control panel cannot be guaranteed in extreme operating modes. If the additional braking function "Stop with spacebar" is deactivated, it may no longer be possible to brake the motor via the TIA Portal. This can lead to accidents resulting in death or serious injury.  - Only deactivate the "Stop with spacebar" option in absolute exceptional cases and if it has been ensured that you are able to stop the drive safely using suitable hardware solutions. |  |     - Optional: If you do not want to use the "Stop with spacebar" option, deactivate this option in the message window.       This setting requires a safety confirmation. The message window cannot be closed without confirmation.    - Also activate the "Continue without quick stop function via spacebar and focus switch" option. 4. To close the message window and confirm your inputs, click the "OK" button.     The message window closes. The master control is then active. |  |

#### Step 2: Set the drive enable

To set the required enable for the control panel, proceed as follows:

1. Click the "Set" button under "Drive enables".

   Further areas of the control panel are activated.
2. Click the "Acknowledge faults" button to acknowledge the currently active faults.
3. If you no longer require the enables, click the "Reset" button under "Drive enables".

#### Step 3: Traverse drive

To traverse the drive, proceed as follows:

1. If the motor is not yet switched on, switch it on.
2. In the "Control" area, enter a speed setpoint in the "Speed" field with which the motor is to turn.
3. Click the "Reverse", "Backward", "Jog forward", or "Jog backward" button to traverse the drive.

   The motor does not accelerate until you click the "Backward" or "Forward" button:

   - To rotate the motor backwards, click the "Backward" button.
   - To rotate the motor forward, click the "Forward" button.
   - Click the "Jog forward" button to inch the motor forward.
   - Click the "Jog backward" button to inch the motor backward.
4. Click "Stop" to stop the drive.
5. Click the "Off" button to switch off the drive.

**Note**

**Rotation by clicking**

The motor continues to rotate while you keep the mouse clicked on the button. Motion stops once the mouse key is released.

#### Step 4: Deactivate master control

Proceed as follows to return the master control:

1. Click the "Off" button to stop the drive.

   This is a basic requirement for deactivating the master control.
2. Click the "Deactivate" button under "Master control".

   The grayed-out user interface of the control panel indicates that the master control is deactivated.

#### Result

The current values of various parameters are displayed at "Actual values". Enables and faults are displayed at "Drive status". The currently active fault is displayed next to "Active fault".

#### Additional parameters

---

### Testing EPOS settings with the control panel

#### Overview

You can test the saved EPOS settings in the SINAMICS drive via the control panel. Various positioning modes are available for the test in "Positioning" mode.

| Mode | Description | Further settings |
| --- | --- | --- |
| Manual positioning | This traverses the drive endlessly or with jog position-controlled with a defined velocity and acceleration. | - Velocity - Acceleration |
| Relative positioning | This traverses an axis by a defined distance. | - Distance - Velocity - Acceleration |
| Absolute positioning | This traverses the axis to an absolute position. The function is oriented towards "Direct setpoint specification/MDI". | - Target position - Velocity - Acceleration |
| Active homing | This traverses the drive to a home position by means of a home position approach without a higher-level controller. The drive itself controls and monitors the homing cycle. | - Start home position - Start adjustment |

> **Note**
>
> The settings for the desired positioning mode are preset (see [Basic positioner (EPOS)](#basic-positioner-epos)). If the default settings are correct, you do not have to fundamentally reconfigure the settings when testing via the control panel.

#### Requirements

- The device configuration is completely executed (an encoder has been assigned).
- An online connection to the drive has been established.
- The "Positioning" control mode is activated.

  Ideally, the positioning settings for the drive have already been implemented completely.
- If project protection is activated:

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

#### Procedure

1. Call the control panel and activate master control.

   If the "Positioning" control type is activated and "Master control" is activated, the "Operating mode" drop-down list is displayed.
2. Select the entry "Positioning" in the "Operating mode" drop-down list.

   After selecting the "Positioning" operating mode, the "Mode" drop-down list is displayed, from which you can select the EPOS mode.
3. In the "Mode" drop-down list, select the desired mode (e.g. "Manual positioning").
4. Click on the "1" icon in the "Switch on" field to switch on the motor.
5. Make further settings for the activated positioning mode (see "Further settings" table column).
6. In the "Control" area, click the corresponding buttons to traverse the drive forwards, backwards or jog forwards or backwards.
7. When the test is complete, click on the "0" icon in the "Switch on" field to switch off the motor. Then deactivate master control.

#### Result

Under "Drive status" the status of the various parameters is displayed as LEDs.

The values currently active in the drive are displayed in the "Actual values" area (actual values and current values in the drive).

### Performing One Button Tuning

#### Overview

With "One Button Tuning" (OBT), the mechanical drive train is measured using short test signals. This procedure adapts the controller parameters to the existing mechanical system. With this optimization procedure you determine the optimum controller settings with few entries.

> **Note**
>
> **Optimization also possible via a guided quick startup**
>
> Alternatively, you also can perform these optimizations in online mode via the guided quick startup ([Rotate/Optimize](#rotate-optimize)).

#### Requirements

- There is an online connection between the drive and the operating unit.
- With project protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

#### Step 1: Assuming master control

If an online connection exists, the header of the function view is highlighted in orange. The control elements are grayed-out apart from the "Activate" button. The remaining control elements become active only after you have activated the master control and set the enables.

> **Note**
>
> **Project lock not available when master control is active**
>
> As long as the master control of a drive is active, you cannot apply the project lock if project protection is activated.
>
> The automatic project lock is also suspended on inactivity.

Proceed as follows to activate the master control:

| Symbol | Meaning |
| --- | --- |
| 1. If the master control is still not active, click on "Activate" under "Master control".    The "Activate master control" message window is opened. 2. Read the warning carefully. Check the monitoring time and if required, correct it.     The monitoring time specifies the time during which the connection from the operating unit to the drive is cyclically monitored. The minimum value is 1000 ms. 3. The "Stop with spacebar" option is active by default. When the option is activated the drive is always braked using the shutdown function OFF3 if you press the spacebar or if the focus switches. The focus switches when a dialog is opened (e.g. download dialog) or when switching from TIA Portal to another application.       | Symbol | Meaning |    | --- | --- |    |  | **Warning** |    | **Braking not guaranteed if the "Stop with spacebar" option is deactivated** Stopping by using the buttons on the control panel cannot be guaranteed in extreme operating modes. If the additional braking function "Stop with spacebar" is deactivated, it may no longer be possible to brake the motor via the TIA Portal. This can lead to accidents resulting in death or serious injury.  - Only deactivate the "Stop with spacebar" option in absolute exceptional cases and if it has been ensured that you are able to stop the drive safely using suitable hardware solutions. |  |     - Optional: If you do not want to use the "Stop with spacebar" option, deactivate this option in the message window.       This setting requires a safety confirmation. The message window cannot be closed without confirmation.    - Also activate the "Continue without quick stop function via spacebar and focus switch" option. 4. To close the message window and confirm your inputs, click on "OK".     The message window closes. The master control is then active. |  |

#### Step 2: Make optimization settings

1. Select the desired dynamic response setting for the One Button Tuning corresponding to the mechanical system of your machine.

   One Button Tuning optimizes the drive based on the selected dynamic response setting.

   - Conservative

     Slow control – low mechanical load.
   - Standard

     Best compromise between fast speed control and low mechanical load.
   - Dynamic

     Fast closed-loop speed control – high mechanical load.
2. Enter the angle in the "Rotation limit" field through which the motor and the connected machine are permitted to turn for the required measurements (e.g. 360°) without the mechanical system being damaged.

   The angle should be at least 60° in order to be able to determine useful controller parameters. Generally, longer traversing distances result in better optimization results.
3. Should you wish to perform extended settings, click on the "Extended settings" button.

   The "Machine property" dialog opens. You will receive information under which conditions you can increase the speed control dynamic response.
4. If you want to increase the dynamic response, activate the "Set current setpoint filter with distance compensation" option.   
   Close the dialog window with "Close".

#### Step 3: Start One Button Tuning

When all necessary default settings have been performed, you can start One Button Tuning:

1. To measure the drive to optimize it, click on the "Start" button in the "Measurement" area.

   The optimization function determines all actual values of the drive necessary for optimization.

   Optional: If you want to cancel optimization, click the "0" button in the "Switch off" area.
2. If optimization was successful, save the project.

#### Step 4: Deactivate master control

Following conclusion of One Button Tuning, the master control can be returned as follows:

1. Click the "Deactivate" button under "Master control".

   The "Deactivate master control" message window opens.
2. If you really want to deactivate the master control, click "Yes".

   The grayed-out user interface of the "Deactivate" button indicates that the master control is deactivated.

#### Result

The result of the optimization is displayed in the "Status" area. If the optimization was successful, the corresponding LED lights up in green. The "Optimization result" list compares the settings changed by the tuning with the earlier settings prior to tuning.

If optimization was not successful, repeat tuning with modified specifications, if applicable.

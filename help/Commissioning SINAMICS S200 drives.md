---
title: "Commissioning SINAMICS S200 drives"
package: StdrS200CommenUS
topics: 64
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Commissioning SINAMICS S200 drives

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
- The operating unit is connected to the drive via LAN (physically ONLINE).

  There is no active online connection between the drive and the operating unit.
- If project protection is activated:   
  The function rights required for the configuration in the quick startup are activated for your user role. Observe the detailed information under point "[User administration and security](User%20administration%20and%20security.md#access-control)".

#### Description of function

You can define the following basic settings in the quick startup steps with the same name:

- [Connection to PLC](#connection-to-plc)

  This step indicates that the drive in the project can only be operated together with a controller. Here you define which of the two devices performs motion control.
- [Application](#application)

  You define the converter control mode in this step. With the "Positioning" control mode activated, make detailed settings, for example the motion type, the measuring unit, encoder settings for the position control or the values for a modulo correction.
- [Limits](#limits-when-speed-control-is-active)

  The settings in step "Limits" are also dependent on the selected control mode.

  - "Speed control":

    Here, you define the minimum and maximum values of the motor used: Torque, speed, operating times.
  - "Positioning":

    In this case, make the settings for the traversing profile, for alternative ramp-down times, for jerk limitation and/or for traversing range limitation.
- [Application settings](#application-settings)

  Step "Application settings" is only active when the "Positioning" control mode is activated. Here, you make the detailed settings for active or passive homing.
- [I/O configuration](#io-configuration)

  Here, you configure the digital inputs used.
- [Telegrams](#telegrams-only-offline)

  Based on the selected control mode, the preferred telegrams are suggested here (1, 105 or 112). You can define different telegrams and/or make detailed settings. Telegram settings can only be made offline.
- [Rotate &amp; optimize](#rotate-optimize)

  In online mode, you optimize the drive via the control panel or using one-button tuning. Settings and optimizations can only be performed online.
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
- There is an active [online connection](Configuring%20SINAMICS%20S200%20drives.md#establishing-an-online-connection-to-the-target-device) between the drive and the operating unit.
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

The quick startup step "Connection to PLC" indicates that this drive can only be commissioned together with a controller.

In this step you define whether motion control is performed by the drive or by the controller.

#### Requirements

- The drive has been completely created and specified in the device configuration.
- Optional: A control (PLC) is created in the device configuration and networked with the drive.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

#### Procedure

"Yes" is automatically set as the default setting for "Define the connection to the PLC". SINAMICS S200 drives can only be operated together with a PLC. This setting can therefore not be changed.

1. Specify whether motion control is to be executed by the drive or by a connected controller.

   The controller is set by default. The activated area of the switch is marked blue (![Procedure](images/149502818699_DV_resource.Stream@PNG-de-DE.png)). Click on the white part of the switch if you wish to change the active setting.
2. Save the settings in the project.
3. Click on "Next" to display the next quick startup step.

#### Result

Startdrive defines the default settings of the setup based on what you have specified.

> **Note**
>
> **EPOS settings deactivated**
>
> If you defined that the ramp-function generator function (motion control) is to be performed by a connected controller, then quick startup steps "Application" and "Application settings" are deactivated. EPOS settings are then not possible.

#### Additional parameters

---

### Application

#### Overview

In quick startup step "Application" you define in detail in which application area the S200 is to be used. You define:

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

1. Select how you wish to control your drive in your application. Define the required control mode. Click on the appropriate button:

   - Speed control

     Using a speed control, the speed is controlled as precisely as possible to track a specified setpoint.
   - Positioning

     A "Basic positioner (EPOS)" calculates the traversing profile to traverse an axis as quickly as possible to a target position.

   It is not possible to select several control modes simultaneously. For control mode "Speed control" no other settings are possible.

   For control mode "Positioning", the following detailed settings are required:
2. Select the motion type that you wish to use for the drive when positioning.

   - Rotary motion

     ![Procedure](images/167359924235_DV_resource.Stream@PNG-en-US.png)

     ![Procedure](images/167359924235_DV_resource.Stream@PNG-en-US.png)
   - Linear motion

     ![Procedure](images/167354006539_DV_resource.Stream@PNG-en-US.png)

     ![Procedure](images/167354006539_DV_resource.Stream@PNG-en-US.png)
3. Then select the measurement units for position and velocity.

   The length unit "LU" is used in the factory setting. The units that can be set depend on the motion type.

   All values are reset to the default values when changing the measurement unit and the axis type.
4. Use the settings for the motor encoder used for the position control:

   - Acquire the number of motor revolutions ([p2504](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p25040-lr-motorload-motor-revolutions)) and load revolutions ([p2505](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p25050-lr-motorload-load-revolutions)).
5. If you wish to apply modulo correction:

   - To do this, activate option "Modulo correction activation" (c2577).
   - Define the modulo range ([p2576](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p2576-epos-modulo-correction-modulo-range-1)).
6. Click on "Next" to display the next quick startup step.

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
| Upper speed limit | [p1083](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p10830-speed-limit-in-positive-direction-of-rotation) | Maximum speed for the positive direction.   The set value must be less than or equal to the maximum speed ([p1082](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p10820-maximum-speed)). |
| Lower speed limit | [p1086](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p10860-speed-limit-in-negative-direction-of-rotation) | Maximum speed for the negative direction. The set value must be less than or equal to the maximum speed (p1082). |
| Upper torque limit | [p1520](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p15200-torque-limit-upper) | Defines the upper torque limit or torque limit when motoring. |
| Lower torque limit | [p1521](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p15210-torque-limit-lower) | Defines the lower torque limit or the torque limit when generating |
| Quick stop  Ramp-down time (OFF3) | [p1135](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p11350-off3-ramp-down-time) | The OFF3 ramp-down time is effective from the maximum speed down to the motor standstill. |

> **Note**
>
> **Displaying the actual motor data**
>
> The actual motor data of the drive are shown in dialog "Show motor data". The dialog can be opened using button "Show motor data". The following values can be configured:
>
> - Supply voltage ([p0210](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p0210-device-supply-voltage)).
> - Motor ambient temperature ([p0613](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p06130-mot_temp_mod-13-ambient-temperature))
> - Direction of rotation ([p1821](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p18210-direction-of-rotation))

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
> - Supply voltage ([p0210](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p0210-device-supply-voltage)).
> - Motor ambient temperature ([p0613](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p06130-mot_temp_mod-13-ambient-temperature))
> - Direction of rotation ([p1821](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p18210-direction-of-rotation))

##### Requirements

- The motor used in the device configuration has been completely specified and configured.

  This basic parameterization cannot be performed without complete configuration.
- Control mode "Positioning" is activated in the quick startup step "Application".

  When "Speed control" is active other settings are displayed.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

##### Specifying the maximum traversing profile limitation

1. Correct the specified value in LU for the maximum velocity in the "Max. velocity" field ([p2571](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p2571-epos-maximum-velocity-1)).

   The maximum velocity defines the maximum travel velocity [1000 LU/min]. A change immediately limits the velocity of an active traversing block.

   The "Corresponds to speed" field displays the converted speed, the "Max. speed" field displays the maximum speed.

   The limitation acts when positioning (jogging, processing the traversing blocks, direct setpoint input, home position approach).
2. Correct the specified value in LU for the acceleration at "Max. acceleration" ([p2572](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p2572-epos-maximum-acceleration-1)).

   The "Corresponds to ... ramp-up time" field displays the converted ramp-up time.
3. Correct the specified value in LU for the deceleration at "Max. deceleration" ([p2573](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p2573-epos-maximum-deceleration-1)).

   The "Corresponds to ... ramp-down time" field displays the converted ramp-down time.

   The maximum acceleration and maximum deceleration specify the maximum acceleration for increasing the velocity and the maximum deceleration for reducing the velocity. Both values act when positioning (jogging, processing the traversing blocks, direct setpoint input, home position approach).
4. Save the settings.

##### Specifying the ramp-down time in relation to the maximum speed

The velocity, acceleration and deceleration limitation values do not apply for faults or for a safe stop. Instead, the ramp-down times for OFF1 and OFF3 are used. The proposed ramp-down time is displayed in the "Ramp-down time in relation to max. speed" field.

1. If you want to apply this ramp-down time in OFF1, click the "Accept values" button.

   The ramp-down time is now applied to the "OFF1 ramp-down time" ([p1121](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p11210-off1-ramp-down-time)) field.
2. Enter the required value in field "Ramp-down time (OFF3)" ([p1135](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p11350-off3-ramp-down-time)).
3. Save the settings.

##### Specifying the maximum jerk limitation

A jerk limitation delays the acceleration. Proceed as follows:

1. Activate option "Jerk limitation". (p2575)
2. Enter a value for the maximum jerk limitation under "Max. jerk" ([p2574](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p2574-epos-jerk-limiting-1)).

   The converted values for the rounding times are displayed in the fields below the diagram.
3. Save the settings.

##### Defining position limits

The settings of the position control words and position status words of telegrams 111 or 112 define whether a SW limit switch or a HW limit switch is active.

1. Acquire the values for the negative end position ([p2580](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p2580-epos-negative-software-limit-switch-1)) and the positive end position ([p2581](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p2581-epos-positive-software-limit-switch-1)) of the SW limit switch.

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
| 1. Optional: If the detailed settings are hidden, expand them with a mouse click. 2. Activate the required homing mode in field "Homing mode selection".       | Symbol | Meaning |    | --- | --- |    | ① | Use the encoder zero mark and reference cam |    | ② | Use the encoder zero mark |    | ③ | Use the external zero mark via digital input | 3. Optional (for ① and ③):  For home position approach, enter the approach velocity to the reference cam in field "to the reference cam" ([p2605](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p2605-epos-active-homing-approach-velocity-reference-cam-1)). 4. Enter an approach velocity in field "To the zero mark" ([p2608](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p2608-epos-active-homing-approach-velocity-zero-mark-1)).     For home position approach, this approach velocity is applicable after detecting the reference cam to search for the zero mark. 5. Optional (for ③):  From drop-down list "Digital input of the external zero mark" ([p0494](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p04940-equivalent-zero-mark-input-terminal)) select the input terminal to connect a zero mark replacement.    This parameter supplies incorrect measured values during an active measurement. In this particular case, it is not permissible to write to the parameter. 6. Enter the required home position offset for the home position approach in field "Home position offset" ([p2600](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p2600-epos-active-homing-home-position-offset-1)). 7. If you want to perform the adjustment immediately after the home position approach, activate the option of the same name ([p2584](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p258403-epos-functions-configuration).3). 8. Optional (for ①):    If you want to acquire the reference cams via a digital input, activate the option of the same name ([p11550](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p11550-epos-active-homing-reference-cam-selection)). 9. Click on "Next" if you do not wish to make any additional EPOS settings.     The quick startup step "I/O configuration" is displayed. |  |

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
4. Click on "Set" ([p2507](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p25070-lr-absolute-encoder-adjustment-status) = 2).

   Status display "Home position set" ([r2684](SINAMICS%20Parameter%20S200%20Basic%20PN.md#r2684015-epos-status-word-2).11) is then updated. When the adjustment is correct, entry "Absolute encoder adjusted" is displayed in field "Absolute encoder adjustment state".

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

> **Note**
>
> **Interconnecting signals using drop-down lists**
>
> For SINAMICS S200 there are no direct signal interconnections for the digital inputs and outputs. However, drop-down lists at the inputs and outputs allow functions or signals to be assigned in a similar way.

In quick startup step "I/O configuration", make the basic settings for the digital inputs and digital outputs of the drive:

- Digital input (DI 0 to DI 3)

  You can assign control signals (high/low) or functions to all digital inputs using drop-down lists. The program prevents the same signals or functions being assigned to different digital inputs.

  You can alternatively use digital inputs DI 0 and DI 1 as measuring probe and therefore evaluate in the control.
- Digital output (DO 0 to DO 1)

  You can assign status signals (high/low) or functions to the two digital outputs using drop-down lists. Different signals or functions should be assigned to the two digital outputs. The program prevents a multiple assignment.

  > **Note**
  >
  > **S200 Basic**
  >
  > SINAMICS S200 Basic drives only have one DO.

#### Requirements

- The motor used in the device configuration of the drive has been completely specified and configured.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

#### Procedure

1. If you wish to use the digital inputs as measuring probe, for DI 0 or DI 1 activate option "Use as measuring probe".

   Both digital inputs can be activated as measuring probe. The corresponding drop-down list is then deactivated.

   When activating a DI as measuring probe, option "Activate equivalent zero mark" is displayed.
2. Optional: Click on the through icon to invert the signal ![Procedure](images/166364501899_DV_resource.Stream@PNG-de-DE.png).

   When the signal is inverted, the icon changes to look like this: ![Procedure](images/166364493323_DV_resource.Stream@PNG-de-DE.png).
3. In the drop-down list "Activate equivalent zero mark", select whether you wish to use an equivalent zero mark or whether this equivalent zero mark should apply for DI 2 or DI 3.
4. If you want to additionally execute status signals of functions via digital inputs, in the digital input, select the appropriate signal or the required function.

   You can use all 4 digital inputs for this purpose. However, it is not permissible that the required digital input is activated as measuring probe (drop-down list deactivated).

   The program prevents the same signal being selected a multiple number of times or the same function for several digital inputs.
5. In the drop-down list under "Digital outputs", select the required status signals or functions for digital outputs DO 0 to DO 1.
6. Click on "Next" to display the next quick startup step.

#### Result

Startdrive defines the default settings of the setup based on what you have specified.

#### Additional parameters

- [p0488](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p048802-measuring-probe-1-input-terminal)
- [p0489](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p048902-measuring-probe-2-input-terminal)
- [p0490](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p049001-invert-measuring-probe-or-equivalent-zero-mark)
- [p0494](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p04940-equivalent-zero-mark-input-terminal)
- c0730
- c0731

---

### Telegrams (only offline)

#### Overview

The telegrams of the drive were preconfigured by the specifications previously defined in the guided quick startup.

In quick startup step "Telegrams", optimize these default settings if this is necessary for your drive. The following telegrams are preassigned depending on the selected control mode:

| Control mode | Preset telegram | Telegrams that can be set |
| --- | --- | --- |
| "Speed control" | 1 | 2, 3, 5, 102, 105 |
| "Positioning" | 112 | 7, 9, 111, 999 |
| Connected PLC controls | 105 | 1, 2, 3, 5, 102 |

#### Requirements

- The motor used in the device configuration of the drive has been completely specified and configured.
- There is **no** active online connection between the drive and operating unit.

  Telegrams can only be configured offline.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

#### Procedure

The default telegrams are displayed in the "Telegrams" quick startup step.

1. Select the required standard telegram from the "Telegram" drop-down list.
2. Optional when speed control is activated:

   Correct the preset reference speed ([p2000](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p2000-reference-speed)) in the field with the same name.
3. If you want to optimize the settings of the telegrams used in the telegram configuration, click on the ![Procedure](images/92607914379_DV_resource.Stream@PNG-de-DE.PNG) "Extended settings" icon.

   Make the required settings under "[Telegram settings for S200](Communication%20and%20telegrams.md#settings-for-sinamics-s200)".
4. Switch back to the quick startup step "Telegrams".
5. Click on "Next" to display the next quick startup step.

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
2. Proceed as described under "[Download to device](Configuring%20SINAMICS%20S200%20drives.md#loading-the-configuration-from-the-project-to-the-device)".

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
3. Proceed as described under "[Upload from device](Configuring%20SINAMICS%20S200%20drives.md#loading-the-configuration-from-the-device-to-the-project)".

## Parameterization

This section contains information on the following topics:

- [Overview](#overview-2)
- [Basic parameterization](#basic-parameterization)
- [Inputs/outputs](#inputsoutputs)
- [Safety Integrated (not for S200 Basic)](#safety-integrated-not-for-s200-basic)
- [Technology functions](#technology-functions)

### Overview

#### Differences between offline and online parameterization

Settings performed offline in the "Parameterization" area generally must be downloaded to the drive before they become active (see [Downloading project data to the device](Configuring%20SINAMICS%20S200%20drives.md#loading-the-configuration-from-the-project-to-the-device)).

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
  There is an active [online connection](Configuring%20SINAMICS%20S200%20drives.md#establishing-an-online-connection-to-the-target-device) between the drive and the operating unit.
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

- Supply voltage
- Direction of rotation

> **Note**
>
> **Basic parameterization also possible online**
>
> Basic parameterization of the S200 Control Unit is possible offline as well as online.

##### Requirements

- The drive has been completely created and fully specified in the device configuration.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

##### Procedure

1. The supply voltage is preset and depends on the selected drive version.   
   If you want to specify another line voltage, correct the specified line voltage in the input field of the same name ([p0210](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p0210-device-supply-voltage)).
2. The motor ambient temperature is preassigned with 40 °C. Correct the value in the text box "Motor ambient temperature" ([p0613](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p06130-mot_temp_mod-13-ambient-temperature)) if the ambient temperature is different.

   The underlying temperature model uses the motor ambient temperature to calculate the thermal motor utilization.
3. The direction of rotation last set for the motor is displayed in the "Direction of rotation" drop-down list ([p1821](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p18210-direction-of-rotation)[0]). If you want to adjust the counter-rotational direction, select the desired direction of rotation from the drop-down list:

   - [0] Right
   - [1] Left
4. If you use the "Speed control" control type, make adjustments to the preset limits if necessary (see [Basic parameterization/limitations](#basic-parameterizationlimitations)).
5. Then save the project to accept the settings.

##### Result

Startdrive defines the default settings of the setup based on what you have specified.

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
   If you want to change this pre-assignment, correct the values in the "Positive speed limit " ([p1083](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p10830-speed-limit-in-positive-direction-of-rotation)[0]) or "Negative speed limit" fields ([p1086](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p10860-speed-limit-in-negative-direction-of-rotation)[0]).
2. If you want to define the fixed upper or motor torque limit, enter an appropriate value in the "Torque limit upper" field ([p1520](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p15200-torque-limit-upper)[0]).
3. If you want to define the fixed lower torque limit or torque limit when generating, enter an appropriate value in the "Torque limit lower" field ([p1521](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p15210-torque-limit-lower)[0]).
4. A ramp-down time in which the speed setpoint is ramped down from maximum speed to standstill following an OFF3 can be specified for the down ramp.   
   In this case, enter a ramp-down time in the "Quick stop (OFF3 ramp-down time)" field ([p1135](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p11350-off3-ramp-down-time)).
5. Then save the project to accept the settings.

##### Result

Startdrive defines the default settings of the setup based on what you have specified.

##### Additional parameters

---

### Inputs/outputs

This section contains information on the following topics:

- [Digital inputs and outputs](#digital-inputs-and-outputs)

#### Digital inputs and outputs

##### Overview

> **Note**
>
> **Interconnecting signals using drop-down lists**
>
> For SINAMICS S200 there are no direct signal interconnections for the digital inputs and outputs. However, drop-down lists at the inputs and outputs allow functions or signals to be assigned in a similar way.

In a SINAMICS S200 drive make the basic settings for the digital inputs and digital outputs of the drive:

- Digital input (DI 0 to DI 3)

  You can assign control signals or functions to all digital inputs using drop-down lists and in so doing interconnect them. The program prevents the same signals or functions being assigned to different digital inputs.

  You can alternatively use digital inputs DI 0 and DI 1 as measuring probe and therefore evaluate in the control.
- Digital output (DO 0 to DO 1)

  You can assign status signals or functions to the two digital outputs using drop-down lists and in so doing interconnect them. In an ideal case, assign the two digital outputs different signals and/or functions.

  > **Note**
  >
  > **S200 Basic**
  >
  > SINAMICS S200 Basic drives only have one digital output DO.

##### Requirements

- The motor used has been completely specified and configured.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

##### Procedure

1. If you wish to use the digital inputs as measuring probe, for DI 0 or DI 1 activate option "Use as measuring probe".

   Both digital inputs can be activated as measuring probe. The corresponding drop-down list is then deactivated.

   When activating a DI as measuring probe, option "Activate equivalent zero mark" is displayed.
2. Optional: Click on the through icon to invert the signal ![Procedure](images/166364501899_DV_resource.Stream@PNG-de-DE.png).

   When the signal is inverted, the icon changes to look like this: ![Procedure](images/166364493323_DV_resource.Stream@PNG-de-DE.png).
3. In the drop-down list "Activate equivalent zero mark", select whether you wish to use an equivalent zero mark or whether this equivalent zero mark applies for DI 2 or DI 3.
4. If you want to additionally execute status signals of functions via digital inputs, in the digital input, select the appropriate signal or the required function.

   You can use all 4 digital inputs for this purpose. However, it is not permissible that the required digital input is activated as measuring probe (drop-down list deactivated).

   The program prevents the same signal being selected a multiple number of times or the same function for several digital inputs.
5. In the drop-down list under "Digital outputs", select the required status signals or functions for digital outputs DO 0 to DO 1.

##### Result

Startdrive defines the default settings of the setup based on what you have specified.

##### Additional parameters

- [p0488](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p048802-measuring-probe-1-input-terminal)
- [p0489](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p048902-measuring-probe-2-input-terminal)
- [p0490](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p049001-invert-measuring-probe-or-equivalent-zero-mark)
- [p0494](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p04940-equivalent-zero-mark-input-terminal)
- c0730
- c0731

---

### Safety Integrated (not for S200 Basic)

This section contains information on the following topics:

- [Introduction](#introduction)
- [Emergency Off and Emergency Stop](#emergency-off-and-emergency-stop)
- [Stop function - STO](#stop-function---sto)
- [Function status](#function-status)
- [Stop responses](#stop-responses)
- [Fail-safe acknowledgment of safety messages](#fail-safe-acknowledgment-of-safety-messages)

#### Introduction

##### Overview

When compared to standard drive functions, Safety Integrated Functions have an especially low error rate. Performance level (PL) and safety integrity level (SIL) of the corresponding standards are a measure of the error rate.

As a consequence, Safety Integrated Functions are suitable for use in safety-related applications to minimize risk. An application is safety-related if the risk analysis of the machine or the system indicates a special hazard potential in the application.

Safety Integrated ("integrated in the drive") means:

- The safety functions are integrated in the drive.
- Safety functions can run without requiring additional external components.

##### Conformity

Safety Integrated Functions comply with:

- Safety Integrity Level (SIL) 3 according to IEC 61800‑5‑2
- Category 3 or 4 according to EN ISO 138491
- Performance Level (PL) e according to EN ISO 13849-1

Safety Integrated Functions correspond to the functions according to IEC 61800‑5‑2 and IEC 61800‑5‑3.

##### Safety Integrated Functions used

SINAMICS S200 standard drives as of firmware V6.2 are equipped with the following drive-integrated Safety Integrated Functions:

| Functions | Abbr. | Area | Meaning |
| --- | --- | --- | --- |
| [Safe Torque Off](#stop-function---sto) | STO | **Stop functions** | Safe Torque Off according to stop Category 0  The Safety Integrated Function STO is activated by default and cannot be configured.   To deactivate the Safety Integrated Functions, use the connector included in the connector kit at the X131 interface to deactivate STO. |

> **Note**
>
> **Not available for basic versions**
>
> The Safety Integrated Functions described are not available for SINAMICS S200 basic versions.

#### Emergency Off and Emergency Stop

"Emergency Off" and "Emergency Stop" are commands that minimize different risks in the machine or plant.

| Symbol | Meaning |
| --- | --- |
| **Emergency Off**   Risk of electric shock.    ![Figure](images/167196795915_DV_resource.Stream@PNG-de-DE.png) | **Emergency Stop**   Risk of unexpected motion.    ![Figure](images/167196838795_DV_resource.Stream@PNG-de-DE.png) |

Measures and solutions

| Command | Emergency Off | Emergency Stop |
| --- | --- | --- |
| Measure to minimize risk | **Safe switch off**   Switching off the electric power supply for the installation, either completely or partially. | **Safely stop and safely prevent restarting**   Stopping or preventing the dangerous movement |
| Classic solution | Switch off the power supply.    ![Figure](images/167196936843_DV_resource.Stream@PNG-de-DE.png) | Switch off the drive power supply.    ![Figure](images/167196881419_DV_resource.Stream@PNG-de-DE.png) |
| Solution with the STO safety function integrated in the drive | STO is not suitable for safely switching off a voltage. | Select STO.    ![Figure](images/167196979467_DV_resource.Stream@PNG-de-DE.png)   It is permissible that you switch off the converter power supply as well. However, switching off the voltage is not required as a risk-reduction measure. |

#### Stop function - STO

This section contains information on the following topics:

- [Safe Torque Off (STO) mode of operation](#safe-torque-off-sto-mode-of-operation)

##### Safe Torque Off (STO) mode of operation

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
| ① | Selection of STO | - The converter identifies when STO is selected and signals the status "STO active" ([r9722](SINAMICS%20Parameter%20S200%20PN.md#r972207-si-status-signals).00) - The converter interrupts the torque-generating energy supply to the motor. There is no electrical isolation. - If you are using a line contactor, then the converter opens the line contactor. - The switch-on inhibit prevents the motor from automatically restarting. |
| ② |  | - The motor coasts down to a standstill. |
| ③ | Deselection of STO | - The converter detects the deselection of STO. |
| ④ | Signal change at ON/OFF1 from 1 to 0 | - The converter is again ready for switching on. |
| ⑤ | Signal change at ON/OFF1 from 0 to 1 | - The motor starts again. |

###### Additional parameters

---

#### Function status

##### Overview

The function status shows the status of the enabled Safety Integrated Functions. If a function is active, then the status indicates "active" ([r9722](SINAMICS%20Parameter%20S200%20PN.md#r972207-si-status-signals)). An EMERGENCY STOP is initiated if STO is active.

- Status

  - Internal event

    Provides information as to whether internal events (e.g. software faults in the converter or a discrepancy in the monitoring channels) have been signaled and whether the communication functions.
- Version:

  The version shows the software versions of the corresponding components relevant for Safety Integrated. This data is predominantly provided as information for service and update.

  - SINAMICS Safety firmware version
  - I/O processor firmware version

##### Requirement

- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

##### Status messages in detail

| Display | Function status |
| --- | --- |
| ![Status messages in detail](images/146631416203_DV_resource.Stream@PNG-de-DE.png) | Function is active |
| ![Status messages in detail](images/146630242827_DV_resource.Stream@PNG-de-DE.png) | Function is not active |

##### Additional parameters

---

#### Stop responses

##### Description of function

The drive triggers a stop response depending on certain events:

- Stop response SCF

  The converter detects a discrepancy in the Safety Integrated monitoring channels, for example an error in the result and data comparison.

External selection of a stop response is not possible. All stop responses bring the motor to a standstill.

![Stop responses S200](images/171967067403_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| STO | Safe Torque Off |
| SCF | Safety Channel Failure |

Stop responses S200

#### Fail-safe acknowledgment of safety messages

##### Overview

In the event of a safety message, the converter detects an internal event.

A safety message requires a fail-safe acknowledgment.

##### Requirement

- You checked and eliminated the cause of the internal event.

##### Procedure

You acknowledge safety messages with a fail-safe signal. You have the following options for fail-safe acknowledgment:

- **Through selection and deselection of STO**

  By selecting and then deselecting STO, the safety messages are automatically cleared.

- **By switching the supply voltage off and then on again**

  Temporarily switch the converter power supply off and on again.

### Technology functions

This section contains information on the following topics:

- [Basic positioner (EPOS)](#basic-positioner-epos)
- [Pulse Train Output (PTO) (not for S200 Basic)](#pulse-train-output-pto-not-for-s200-basic)

#### Basic positioner (EPOS)

This section contains information on the following topics:

- [Fundamentals](#fundamentals-1)
- [Function selection](#function-selection)
- [Basic parameters / Mechanical system](#basic-parameters-mechanical-system)
- [Setting the backlash](#setting-the-backlash)
- [Configuring limitations](#configuring-limitations)
- [Homing](#homing)
- [Configuring position monitoring](#configuring-position-monitoring)
- [Checking the direct setpoint input (MDI)](#checking-the-direct-setpoint-input-mdi)
- [Using traversing blocks](#using-traversing-blocks)
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

1. Acquire the values for the negative end position ([p2580](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p2580-epos-negative-software-limit-switch-1)) and the positive end position ([p2581](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p2581-epos-positive-software-limit-switch-1)) of the SW limit switch.

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

1. Correct the specified value for the maximum velocity in the "Max. velocity" field ([p2571](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p2571-epos-maximum-velocity-1)).

   The maximum velocity defines the maximum travel velocity. A change immediately limits the velocity of an active traversing block.

   The "Corresponds to speed" field displays the converted speed, the "Max. speed" field displays the maximum speed.

   The limitation acts when positioning (jogging, processing the traversing blocks, direct setpoint input, home position approach).
2. Correct the specified value for the acceleration at "Max. acceleration" ([p2572](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p2572-epos-maximum-acceleration-1)).

   The "Corresponds to ... ramp-up time" field displays the converted ramp-up time.
3. Correct the specified value for the deceleration at "Max. deceleration" ([p2573](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p2573-epos-maximum-deceleration-1)).

   The "Corresponds to ... ramp-down time" field displays the converted ramp-down time.

   The maximum acceleration and maximum deceleration specify the maximum acceleration for increasing the velocity and the maximum deceleration for reducing the velocity. Both values act when positioning (jogging, processing the traversing blocks, direct setpoint input, home position approach).
4. Save the settings.

###### Specifying the traversing profile limitation in relation to the maximum speed

The velocity, acceleration and deceleration limitation values do not apply for faults or for a safe stop. Instead, the ramp-down times for OFF1 and OFF3 are used. The proposed ramp-down time is displayed in the "Ramp-down time in relation to max. speed" field.

1. If you want to apply this ramp-down time in OFF1, click the "Accept values" button.

   The ramp-down time is now applied to the "OFF1 ramp-down time" ([p1121](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p11210-off1-ramp-down-time)) field.
2. Manually enter the required value in field "Ramp-down time (OFF3)" ([p1135](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p11350-off3-ramp-down-time)).
3. Save the settings.

###### Specifying the maximum jerk limitation

A jerk limitation delays the acceleration. Proceed as follows:

1. Activate option "Jerk limitation".
2. Enter a value for the maximum jerk limitation under "Max. jerk" ([p2574](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p2574-epos-jerk-limiting-1)).

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
| 1. In function view "Active homing" select the required homing mode in field "Homing mode selection".       | Symbol | Meaning |    | --- | --- |    | ① | Encoder zero mark and homing cam |    | ② | Encoder zero mark |    | ③ | External zero mark via digital input | 2. Optional (for ① and ③):  For home position approach, enter the approach velocity to the reference cam in field "to the reference cam" ([p2605](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p2605-epos-active-homing-approach-velocity-reference-cam-1)). 3. In the "to the zero mark" ([p2608](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p2608-epos-active-homing-approach-velocity-zero-mark-1)) field, enter the approach velocity after detecting the reference cam when searching for the zero mark during home position approach. 4. Optional (for ③):  From drop-down list "Digital input of the external zero mark" ([p0494](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p04940-equivalent-zero-mark-input-terminal)) select the input terminal to connect a zero mark replacement.    This parameter supplies incorrect measured values during an active measurement. In this particular case, it is not permissible to write to the parameter. 5. If absolute encoder adjustment should be automatically performed after home position approach, then activate option "carry out adjustment after home position approach" ([p2584](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p258403-epos-functions-configuration).3). 6. Optional (for ①):    If you want to acquire the reference cams via a digital input, activate the option of the same name ([p11550](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p11550-epos-active-homing-reference-cam-selection)). 7. Enter the required home position offset for the home position approach in field "Home position offset" ([p2600](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p2600-epos-active-homing-home-position-offset-1)). 8. Save the settings. |  |

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
3. Click on "Set" ([p2507](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p25070-lr-absolute-encoder-adjustment-status) = 2).

   Status display "Home position set" ([r2684](SINAMICS%20Parameter%20S200%20Basic%20PN.md#r2684015-epos-status-word-2).11) is then updated. When the adjustment is correct, entry "Absolute encoder adjusted" is displayed in field "Absolute encoder adjustment state".

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
   (value = 0, positioning monitoring is deactivated; value &gt;= 1, positioning monitoring is activated) in the "Positioning window" ([p2544](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p2544-lr-positioning-window-1)) field.

   The positioning window defines the range around the target position in which the actual position value must lie after the positioning monitoring time has expired.
2. Enter a value in the "Positioning monitoring time" ([p2545](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p2545-lr-positioning-monitoring-time)) field.

   The positioning monitoring time defines the interval in which the following error must lie once within the positioning window, after the time expires.
3. Enter a value   
   (value = 0, standstill monitoring is deactivated; value ≥ 1, standstill monitoring is activated) in the "Standstill window" ([p2542](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p2542-lr-standstill-window-1)) field.

   The standstill window defines the range around the target position in which the actual position value must lie after the standstill monitoring time has expired.
4. Enter a value in the "Standstill monitoring time" ([p2543](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p2543-lr-standstill-monitoring-time)) field.

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

1. Enter the maximum deviation between the calculated and the measured actual position value before an error occurs in the "Maximum following error" ([p2546](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p25460-lr-dynamic-following-error-monitoring-tolerance-1)) field.
2. Save the settings in the project.

###### Result

The following error monitoring settings have been made. Following error monitoring is activated as soon as the entered value p2546 ≥ 1.

###### Additional parameters

---

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

   - Enter the value for "Following error for the fixed stop detection" ([p2634](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p26340-epos-fixed-stop-maximum-following-error-1)) in the input field with the same name.

     When this following error value is exceeded, this indicates that the "Fixed stop reached" state has been reached.
   - Enter the value for "Position tolerance after fixed stop detection" ([p2635](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p2635-epos-fixed-stop-monitoring-window-1)) in the input field with the same name.

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
| 1. In function view "Jog", make the following settings for incremental jogging:        | Symbol | Meaning |    | --- | --- |    | Jog 1 | "Velocity setpoint 1" ([p2585](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p2585-epos-jog-1-setpoint-velocity-1)) |    | "Traversing path 1" ([p2587](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p2587-epos-jog-1-traversing-distance-1)) |  |    | Jog 2 | "Velocity setpoint 2" ([p2586](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p2586-epos-jog-2-setpoint-velocity-1)) |    | "Traversing path 2" ([p2588](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p2588-epos-jog-2-traversing-distance-1)) |  | 2. Save the settings. |  |

###### Result

Drive configuration continues based on the selected positioning settings.

###### Additional parameters

- [p2572](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p2572-epos-maximum-acceleration-1)
- [p2573](SINAMICS%20Parameter%20S200%20Basic%20PN.md#p2573-epos-maximum-deceleration-1)
- c2589
- c2590
- c2591

---

##### Function status

###### Overview

The function status shows the status of the enabled EPOS functions. If a function is active, then the status indicates "active".

- Operating mode

  Shows which EPOS operating mode is active ([r2669](SINAMICS%20Parameter%20S200%20Basic%20PN.md#r266905-epos-actual-operating-mode)).
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

#### Pulse Train Output (PTO) (not for S200 Basic)

This section contains information on the following topics:

- [Configuring PTO](#configuring-pto)

##### Configuring PTO

###### Overview

Pulse Train Output is a simple and universal interface between a SIMATIC control and a SINAMICS drive. PTO is supported worldwide by many stepper drives and servo drives and is used in many positioning applications, e.g. for adjusting or feed axes.

PTO is also referred to as pulse/direction interface. The pulse/direction interface comprises 2 signals. The frequency of the pulse output represents the speed and the number of output pulses for the section to be traversed. The direction output defines the traversing direction. As a consequence, the position is specified in precise increments.

> **Note**
>
> The pulse width is permanently set. It is dependent on the maximum pulse frequency set for the particular channel.

**Possible applications:**

The pulse/direction interface signals supplied are especially suitable to address the following applications:

- To implement an autonomous closed-loop control system in the control.
- As pulse sequence setpoint for a synchronous axis of another drive.

**Electronic gear ratio**

![Gear ratio PTO](images/171967742347_DV_resource.Stream@PNG-en-US.png)

Gear ratio PTO

The electronic gear ratio is a multiplication factor for pulse sequence output to a controller.

You can select one of the following two values for setting the electronic gear ratio:

- Number of PTO pulses per motor revolution ([p4408](SINAMICS%20Parameter%20S200%20PN.md#p4408-pto-pulse-number)).
- Gear ratio using a numerator ([p4410](SINAMICS%20Parameter%20S200%20PN.md#p4410-gearbox-encoder-motorpto-numerator-control-unit)) and a denominator ([p4409](SINAMICS%20Parameter%20S200%20PN.md#p4409-gearbox-encoder-motorpto-denominator-control-unit)).

  > **Note**
  >
  > If the electronic gear ratio is determined using the counter and the denominator, the number of PTO pulses per motor revolution (p4408) must be set to 0. Otherwise, no electronic gear ratio will be active.

> **Note**
>
> The range of the electronic gear ratio is 0.02 to 8000.
>
> The electronic gear ratio can only be set in the "Servo off" state.

> **Note**
>
> When using the electronic PTO gear ratio: If multiplying the PTO setpoint pulses per motor revolution by the electronic gear ratio does not produce an integer, no zero mark is generated.

###### Requirements

- The drive has been completely created and specified in the device configuration.
- A control (PLC) is created in the device configuration and networked with the drive.   
  The required technology objects for the control have been completely created in the device configuration (e.g. "TO_PositioningAxis").
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

###### Procedure

1. Define whether the PTO position actual value should be inverted. Click on the appropriate button:

   - Positive logic (= not inverted, default setting)
   - Negative logic (= inverted)
2. Correct the value for the maximum output frequency ([p4405](SINAMICS%20Parameter%20S200%20PN.md#p4405-pto-maximum-output-frequency)).

   This value represents the velocity and the number of output pulses for the section to be traversed.
3. In the "PTP zero mark offset" field ([p4426](SINAMICS%20Parameter%20S200%20PN.md#p4426-pto-zero-mark-offset)), specify the offset value for moving the zero mark within one mechanical revolution.
4. Then, using a switch, define which values you wish to use to define the gearbox ratio.

   - Number of PTO pulses per motor revolution (p4408)
   - Gearbox ratio is entered using numerator/denominator = p4410/p4409

   The activated area of the switch is marked blue (![Procedure](images/149502818699_DV_resource.Stream@PNG-de-DE.png)). Click on the white part of the switch if you wish to change the active setting.
5. Enter the number of pulses per motor revolution (pulse number p4408).

   - Or -

   Enter the gearbox ratio directly in the two input fields above and below the fraction bar.

   The resulting pulses per revolution are calculated from this entry.
6. Save the settings in the project.

###### Result

The pulse/direction interface PTO has been configured.

###### Additional parameters

- [p4422](SINAMICS%20Parameter%20S200%20PN.md#p44220-pto-configuration)

---

## Rotate & optimize

This section contains information on the following topics:

- [Overview](#overview-3)
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
- There is an active [online connection](Configuring%20SINAMICS%20S200%20drives.md#establishing-an-online-connection-to-the-target-device) between the drive and the operating unit.
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

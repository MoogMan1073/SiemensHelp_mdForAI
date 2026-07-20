---
title: "Commissioning SINAMICS G220 drives"
package: StdrG220CommenUS
topics: 216
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Commissioning SINAMICS G220 drives

This section contains information on the following topics:

- [Guided quick startup](#guided-quick-startup)
- [Parameterization](#parameterization)
- [Rotate & optimize](#rotate-optimize-1)

## Guided quick startup

This section contains information on the following topics:

- [Overview](#overview)
- [Connection to PLC](#connection-to-plc)
- [Operating mode](#operating-mode)
- [Limits](#limits)
- [I/O configuration](#io-configuration)
- [Telegrams (only offline)](#telegrams-only-offline)
- [Rotate & optimize](#rotate-optimize)
- [Overview](#overview-1)

### Overview

This section contains information on the following topics:

- [Fundamentals](#fundamentals)
- [Edit mode (online)](#edit-mode-online)

#### Fundamentals

##### Overview

Using "Guided quick startup", you perform the basic settings for the drive in Startdrive that are used to avoid the following detailed settings as far as possible. All drive settings are pre-assigned according to the specific application using these basic settings.

> **Note**
>
> **Online/offline differences**
>
> You can make most of the settings in the guided quick startup offline as well as offline. However, there are a few exceptions:
>
> - Telegram settings can only be made offline, as telegrams can only be configured offline.
> - For Rotate & optimize, it is possible to carry out optimization online once optimization has been set.
>
> All of the other differences are specifically marked in the subsequent description.

> **Note**
>
> **The significance of Note symbols**
>
> Settings of individual steps may affect the previous settings of other steps. In this case, an appropriate note with the following symbol ![Overview](images/149683184779_DV_resource.Stream@PNG-de-DE.png) appears at the active quick startup step. Check and, if necessary, correct the corresponding settings.
>
> Further identifications:
>
> The ![Overview](images/149683193355_DV_resource.Stream@PNG-de-DE.png) symbol designates information or a context-sensitive note for users.
>
> The ![Overview](images/149847587083_DV_resource.Stream@PNG-de-DE.png) symbol identifies an area of the step where an entry is urgently required.

##### Requirements

- The drive has been completely created and specified in the device configuration.

  Without a complete specification, the guided quick startup cannot be used and a message appears.
- If a control is also used, it must be connected to the drive in the topology view and in the network view. The connection between the devices must also be configured.
- If the project protection is activated:   
  The [function rights](User%20administration%20and%20security.md#access-control) required for the configuration in the quick startup are activated for your user role. User authentication via a login is required.   
  Observe the detailed information under point "[User administration and security](User%20administration%20and%20security.md#overview)".

##### Description of function

You can define the following basic settings in the steps with the same name:

- [Connection to PLC](#connection-to-plc)

  Here you define whether you want to configure the drive in the project together with a control and which of the two components then has master control.
- [Operating mode](#operating-mode)

  Here, you specify the required operating mode or a specific drive control type.
- [Limits](#limits)

  Here, you define the minimum and maximum values of the motor used: Current, speed, running times.
- [I/O configuration](#io-configuration)

  Here, you can configure the analog or digital inputs and outputs used.
- [Telegrams](#telegrams-only-offline)

  Telegrams are proposed here based on previous presettings. You can define different telegrams and/or make detailed settings. Telegram settings can only be made offline.
- [Rotate & optimize](#making-the-optimization-settings)

  Here, you specify the basic settings for the motor data identification which then become effective the first time the motor is switched on.

  In addition, in online mode, you have the option of immediately performing the motor data identification when the motor is switched on and then also immediately optimizing the drive using the control panel.
- [Overview](#overview-1)

  Here you will find a compilation of all settings made after completing the configuration in the guided quick startup.

  - Offline mode: When required, you can load these settings directly to the drive.
  - Online mode: When required, you can load these settings directly into the Startdrive project.

> **Note**
>
> **Requirement for the following detailed configuration**
>
> The complete basic setting of the G220 in the quick startup is a requirement for optional subsequent detailed configuration in the "Parameterization" area.

##### Status display after changes

Changes to individual settings affect other settings in the "guided quick startup". Status symbols indicate the change status of the particular step:

| Symbol | Meaning |
| --- | --- |
| ![Status display after changes](images/155564453003_DV_resource.Stream@PNG-de-DE.png) | The system defaults in this step are valid. |
| ![Status display after changes](images/151783943947_DV_resource.Stream@PNG-de-DE.png) | The settings made in this step are valid.   The settings were made directly in this step, or are the consequences of settings in another step. |
| ![Status display after changes](images/152995660555_DV_resource.Stream@PNG-de-DE.png) | The program changed the settings in this step. Possible causes are:   - Subsequent changes were made in other steps, which are not automatically valid. - Subsequent changes have been made in the device configuration that affect the original settings.   Check the settings of this step. |

##### Manual navigation

You can navigate between the individual steps using the two navigation buttons:

| Button | Explanation |
| --- | --- |
| ![Manual navigation](images/165979777547_DV_resource.Stream@PNG-en-US.png) | Displays the next quick startup step. However, it must already have been displayed once before. |
| ![Manual navigation](images/165979781899_DV_resource.Stream@PNG-en-US.png) | Shows the last step that was displayed before the current step. |

#### Edit mode (online)

##### Operating the guided quick startup in online mode

If you want to work with the guided quick startup in online mode, you need restore points in case commissioning is aborted. Restore points are stored retentively on the memory card of the converter.

Restore points are created automatically when you activate or exit the editing mode and also when you switch from one quick startup step to another step.

> **Note**
>
> **Behavior when the online connection is terminated**
>
> If the connection to the drive is re-established after the online connection has been terminated, the program reverts to the stored data of the last restore point.

##### Requirements

- The drive has been completely created and specified in the device configuration.

  Without a complete specification, the guided quick startup cannot be used and a message appears.
- If a control is also used, it must be connected to the drive in the topology view and in the network view. The connection between the devices must also be configured.
- There is an active [online connection](Configuring%20SINAMICS%20G220%20drives.md#establishing-an-online-connection-to-the-target-device) between the drive and the operating unit.
- No other access from another operating unit to the selected drive is active.

##### Activating/exiting the editing mode

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

##### Completing online commissioning

1. To complete online commissioning in the guided quick startup, click the button ![Completing online commissioning](images/154401817611_DV_resource.Stream@PNG-en-US.PNG).

   All settings made in the quick startup are then saved retentively. You are provided with an overview of all of the settings made in the last "Overview" step.

##### Canceling online commissioning

1. If you want to cancel online commissioning via the guided quick startup, click on the "Cancel" button.

   A confirmation prompt appears.
2. If you really want to cancel, click on "OK".

   All settings made in the quick startup are then discarded. Then the previous settings are restored via the last restore point.

### Connection to PLC

#### Overview

In the quick startup step "Connection to the PLC", you define whether you wish to commission and/or operate the drive together with a control system, and whether you also wish to use Safety Integrated Functions.

Startdrive then makes default settings to speed up commissioning.

#### Requirements

- The drive has been completely created and specified in the device configuration.

  This basic parameterization cannot be performed without complete configuration.
- Optionally, a controller (PLC) also can be created in the device configuration and networked with the drive.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

#### Procedure

1. Specify whether the drive is connected to a controller (PLC). Click on the white part of the switch (![Procedure](images/149502425867_DV_resource.Stream@PNG-de-DE.png)) for this purpose.

   The activated area of the switch is marked blue (![Procedure](images/149502818699_DV_resource.Stream@PNG-de-DE.png)).
2. If you selected the option "Yes", the step is extended to include a further setting.

   - Specify whether the ramp-function generator is to be executed by the drive or by the control.
   - Click the corresponding configuration button to do so.

     The activated configuration-button is marked blue.
3. If you also want to use Safety Integrated Functions with PROFIsafe, additionally activate option "Use Safety Integrated Functions via PROFIsafe".

   This option automatically activates the PROFIsafe telegram 901 in the telegram configuration.
4. Click "Next" to display the next quick startup step.

**Note**

This setting is automatically set to "Yes" and locked against change if a PROFIsafe telegram has been activated at another point in the program for the active drive:

- Quick startup step "Telegrams"
- "Telegram configuration" inspector window menu

The lock at this point can only be removed if the telegram setting at the setting location is undone.

**Note**

The specification where the ramp-function generator is to be executed determines the type of ramp-function generator used and makes a corresponding presetting in the function view "Ramp-function generator".

- Drive: Basic ramp-function generator
- Control: Extended ramp-function generator

#### Result

Startdrive defines the default settings of the setup based on your specifications.

#### Additional parameters

---

### Operating mode

#### Overview

In the "Operating mode" quick startup step, you define the required operating mode and therefore also define the underlying control type. The following settings are possible:

- Standard Drive Control (SDC)

  For standard motor and drive applications.   
  Basic setting for induction motors.
- Dynamic Drive Control (DDC)

  For demanding applications with high utilization of the motor and drive.   
  Basic setting for synchronous motors and reluctance motors. This setting cannot be changed.   
  Operates automatically with closed-loop speed control.
- Select other control types

  Enables manual selection of the control type.

> **Note**
>
> **Details**
>
> You can find details under [Areas of application and parameters of the operating modes](#operating-mode-1).

With the "Select other control types" option, the following control types are available to you:

- [0] U/f control with linear characteristic
- [1] U/f control with linear characteristic and FCC
- [2] U/f control with parabolic characteristic
- [3] U/f control with parameterizable characteristic
- [4] U/f control with linear characteristic and ECO
- [5] U/f control for drives requiring a precise frequency (textile sector)
- [6] U/f control for drives requiring a precise frequency and FCC
- [7] U/f control with parabolic characteristic and ECO
- [19] U/f control with independent voltage setpoint
- [20] Closed-loop speed control (encoderless)
- [21] Closed-loop speed control (with encoder)
- [22] Torque control (encoderless)
- [23] Torque control (with encoder)

> **Note**
>
> **Displaying the actual motor data**
>
> Using the "Show motor data" button, you can open a dialog box with the same name which lists the current motor data of your drive.
>
> Special feature of the online mode: The motor data displayed in online mode can be directly changed for motors with manual motor data input.

#### Requirements

- The drive has been completely created and fully specified in the device configuration.

  This basic parameterization cannot be performed without complete configuration.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

#### Procedure

1. Activate the required operating mode ([p0504](SINAMICS%20Parameter%20G220.md#p05040n-operating-mode)) or activate option "Select other control types".

   For reluctance motors, the "DDC" operating mode is preset and cannot be changed.

   If "DDC" is selected, then closed-loop speed control is automatically set as control type. Whether closed-loop speed control is pre-selected with or without encoder depends on the setting in the device configuration. If an encoder is available in the device configuration, then "Closed-loop speed control (with encoder)" is pre-selected.
2. Select the required control mode ([p1300](SINAMICS%20Parameter%20G220.md#p13000n-open-loopclosed-loop-control-type)) if you selected option "Select other control types" or operating mode "DDC".

   If you have selected the "Torque control (encoderless)" control type, the additional option "Encoderless control up to f=0 (pulse control)" will automatically be activated if you have the appropriate license. You can deselect this option manually.
3. Click "Next" to display the next quick startup step.

#### Result

If you selected either SDC or DDC, the step then lists the typical applications and parameters of this operating mode. Startdrive defines further default settings of the setup based on your specifications. With SDC, configurability for open-loop and closed-loop control functions is severely limited.

#### Additional parameters

---

### Limits

#### Overview

You define the basic properties of the closed-loop drive control using the "Limits" quick startup step.

| Designation | Number | Description |
| --- | --- | --- |
| Device supply voltage | [p0210](SINAMICS%20Parameter%20G220.md#p0210-device-supply-voltage) | Determines the converter supply voltage.   The value affects the following:  - Switch-on threshold for the braking resistor - Activation thresholds of the Vdc_max and Vdc_min control - Selection of the rated values of the power unit   The setting of the parameter determines whether the power unit is operated in the lower or upper voltage range. - Power failure monitoring |
| Current limit motor current | [p0640](SINAMICS%20Parameter%20G220.md#p06400n-motor-current-limit) | Determines the limit value of the motor overload current. |
| Minimum speed | [p1080](SINAMICS%20Parameter%20G220.md#p10800n-minimum-speed) | Setting of the lowest possible speed/velocity. This value is not fallen below in operation. |
| Maximum speed | [p1082](SINAMICS%20Parameter%20G220.md#p10820n-maximum-speed) | Setting of the highest possible speed/velocity. This value is calculated during the commissioning phase depending on the motor and drive unit and can only be equal to or less than the value in [p0322](SINAMICS%20Parameter%20G220.md#p03220n-maximum-motor-speed) (maximum motor speed). |
| Ramp-up time | [p1120](SINAMICS%20Parameter%20G220.md#p11200n-ramp-function-generator-ramp-up-time) | The ramp-up/ramp-down time always refers to the time interval from motor standstill to the set maximum speed (without using roundings). |
| Ramp-down time | [p1121](SINAMICS%20Parameter%20G220.md#p11210n-ramp-function-generator-ramp-down-time) |  |
| Ramp-down time (OFF3) | [p1135](SINAMICS%20Parameter%20G220.md#p11350n-off3-ramp-down-time) | The OFF3 ramp-down time is effective from the maximum speed down to the motor standstill. |

> **Note**
>
> **Displaying the actual motor data**
>
> Using the "Show motor data" button, you can open a dialog box with the same name which displays the current motor data of your drive.
>
> Special feature of the online mode: The motor data displayed in online mode can be directly changed for motors with manual motor data input.

#### Requirement

- The drive has been completely created and specified in the device configuration.

  This basic parameterization cannot be performed without complete configuration.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

#### Procedure

1. Adapt the specified default values (see the table above).
2. Click "Next" to display the next quick startup step.

#### Additional parameters

---

### I/O configuration

#### Overview

In the "I/O configuration" quick startup step, you make basic settings for the analog and digital inputs and outputs of the drive.

Alternatively, you can use predefined templates for the basic input and output settings. The following default settings are possible:

- Conveyor with 4 fixed setpoints
- Fieldbus with data set switchover
- Standard I/O with analog setpoint
- None

  Manual settings are used.

#### Requirements

- The drive has been completely created and fully specified in the device configuration.

  This basic parameterization cannot be performed without complete configuration.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

#### Basic setting (template)

Use the "Template" drop-down list to select saved templates for the I/O configuration.

1. Select the desired I/O template from the "Template" drop-down list.

   The previous I/O settings are automatically overwritten. These settings cannot be restored.

#### Basic settings for analog inputs

1. Make sure that "User-defined" is selected in the "Template" drop-down list. If not, correct this setting.
2. Select the basic configuration of the input signal for the analog input 0 ([p0756](SINAMICS%20Parameter%20G220.md#p075601-analog-inputs-type)):
3. Click the "Scaling" button to configure the scaling.

   The "Scaling analog input AI 0" dialog opens.
4. Enter the x and y values for 2 points of the scaling line and then click "Close".
5. Interconnect the signal sink for the input value of the analog input.

   Several interconnections are possible.
6. If you want to make detailed settings at the analog input, click the icon ![Basic settings for analog inputs](images/92607914379_DV_resource.Stream@PNG-de-DE.PNG) "Extended settings"

   The "[Analog inputs](#analog-inputs)" function view is displayed. Make the necessary settings here.
7. Switch back to the "I/O configuration" quick startup step.
8. Click "Next" to display the next quick startup step.

#### Basic settings for analog output

1. Make sure that "User-defined" is selected in the "Template" drop-down list. If not, correct this setting.
2. Select the type of analog output 0 ([p0776](SINAMICS%20Parameter%20G220.md#p07760-analog-output-type)):

   - Current output (0 mA...+20 mA)

     The analog output is configured as current output.
   - Voltage output (0 V...+10 V)

     The analog output is configured as voltage output.
   - Current output (+4 mA...+20 mA)

     The analog output is configured as current output.
3. Interconnect the signal source of analog output 1 (r0771).
4. Click the "Scaling" button to configure the scaling.

   The "Scaling analog output AO 0" dialog opens.
5. Enter the x and y values for 2 points of the scaling line and then click "Close".
6. If you want to make detailed settings at the analog output, click the icon ![Basic settings for analog output](images/92607914379_DV_resource.Stream@PNG-de-DE.PNG) "Extended settings"

   The "[Analog outputs](#analog-outputs)" function view is displayed. Make the necessary settings here.
7. Switch back to the "I/O configuration" quick startup step.
8. Click "Next" to display the next quick startup step.

#### Basic settings for digital inputs

1. Make sure that "User-defined" is selected in the "Template" drop-down list. If not, correct this setting.
2. Interconnect the signal sources of the digital inputs 0 to 5, 11, 12, 21 and 22 ([r0722](SINAMICS%20Parameter%20G220.md#r0722022-digital-inputs-status)).

   Several interconnections are possible.
3. If you also want to interconnect the signal sources of the inverted digital inputs, click the icon ![Basic settings for digital inputs](images/92607914379_DV_resource.Stream@PNG-de-DE.PNG) "Extended settings"

   The "[Isolated digital inputs](#digital-inputs)" function view is displayed. Make the necessary settings here.
4. Switch back to the "I/O configuration" quick startup step.
5. Click "Next" to display the next quick startup step.

#### Basic settings for digital outputs

1. Make sure that "User-defined" is selected in the "Template" drop-down list. If not, correct this setting.
2. Interconnect the signal sinks of digital outputs 0, 1 and 2 (r0730, r0731, r0732).
3. If you want to make detailed settings at the digital outputs, click the icon ![Basic settings for digital outputs](images/92607914379_DV_resource.Stream@PNG-de-DE.PNG) "Extended settings"

   The "[Digital outputs isolated](#digital-outputs)" function view is displayed. Make the necessary settings here.
4. Switch back to the "I/O configuration" quick startup step.
5. Click "Next" to display the next quick startup step.

#### Additional parameters

---

---

**See also**

[Edit mode (online)](#edit-mode-online)
  
[Establishing an online connection to the target device](Configuring%20SINAMICS%20G220%20drives.md#establishing-an-online-connection-to-the-target-device)

### Telegrams (only offline)

#### Overview

The telegrams of the drive were preconfigured by the specifications previously defined in the guided quick startup.

You can optimize these default settings in the "Telegrams" quick startup step if that is necessary for your drive.

#### Requirements

- The motor used in the device configuration of the drive has been completely specified and configured.
- Optionally, a controller (PLC) also can be created in the device configuration and networked with the drive.
- There is **no** active online connection between the drive and the operating unit.

  Just the same as when configuring telegrams, telegram settings can only be made offline. If the online mode was previously active, you must exit the online mode before setting telegrams.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

#### Procedure

The default telegrams are displayed in the "Telegrams" quick startup step.

1. Select the desired standard telegram from the "Telegram" drop-down list.
2. If you have not yet activated a PROFIsafe telegram in the quick startup step "Connection to PLC", you can do so at this point. For this purpose, activate the option "Use Safety Integrated Functions via PROFIsafe".

   This option automatically activates the PROFIsafe telegram 902 in the telegram configuration.
3. If you want to use PROFIsafe telegram 30 instead of the recommended PROFIsafe telegram 902, then select the telegram from the "PROFIsafe telegram" drop-down list.

   ([details](Communication%20and%20telegrams.md#telegram-overview-for-sinamics-g220) on telegrams)
4. Correct the preset reference speed ([p2000](SINAMICS%20Parameter%20G220.md#p2000-reference-speed-reference-frequency)) in the field with the same name.
5. If you want to optimize the settings of the telegrams used in the telegram configuration, click the ![Procedure](images/92607914379_DV_resource.Stream@PNG-de-DE.PNG) "Extended settings" icon

   The properties of the PROFINET interface are displayed in the Inspector window. Make the desired settings under "[Telegram settings for SINAMICS G220](Communication%20and%20telegrams.md#settings-for-sinamics-g220)".
6. Switch back to the quick startup step "Telegrams".
7. Click "Next" to display the next quick startup step.

#### Result

The telegrams for communication are configured.

#### Additional parameters

---

---

**See also**

[Telegram configuration via PROFIdrive](Communication%20and%20telegrams.md#telegram-configuration-via-profidrive)

### Rotate & optimize

This section contains information on the following topics:

- [Making the optimization settings](#making-the-optimization-settings)
- [Optimization criteria in detail](#optimization-criteria-in-detail)

#### Making the optimization settings

##### Overview

In the quick startup step "Rotating & optimizing", you define default settings for optimizing the motor data, which are activated the first time the motor is switched on.

A motor identification (MotID) provides a means of determining motor data, for example, of third-party motors. The MotID is required to improve the control properties of the motor. Especially for encoderless speed control, as a minimum the stator resistance (including the supply cable resistance) and the power unit parameters must be determined for each drive.

You specify the main optimization settings for the motor data identification either offline or online. In online mode you assume master control and start the optimization.

> **Note**
>
> **Displaying the actual motor data**
>
> Using the "Show motor data" button, you can open a dialog box with the same name which lists the current motor data of your drive.
>
> The motor data displayed in online mode can be changed for motors with manual motor data input.

##### Requirements

- The drive has been completely created and specified in the device configuration.

  This basic parameterization cannot be performed without complete configuration.
- Direct optimization required:

  - There is an active [online connection](Configuring%20SINAMICS%20G220%20drives.md#establishing-an-online-connection-to-the-target-device) between the drive and the operating unit.
  - The [editing mode](#edit-mode-online) is activated.
- With project protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

##### Step 1: Configuring the optimization

You can carry out the optimization settings both offline as well as online. Proceed as follows:

1. In the drop-down list "Motor data identification and rotating measurement" ([p1900](SINAMICS%20Parameter%20G220.md#p1900-motor-data-identification-and-rotating-measurement)), select the method for performing the motor data identification with a stationary or a rotating motor:

   - [0] Locked
   - [1] Motor data ident. (stationary) and speed controller opt.

     Recommended if you have set "Speed control" as the control type. The drive then optimizes the speed controller.
   - [2] Motor data identification (stationary)

     Recommended if you have set "Closed-loop speed control" as the control type, but the motor cannot rotate freely, e.g. if the traversing paths are mechanically restricted.
   - [3] Optimize speed controller (rotating)

     Motor data identification for rotating motor.
   - [11] Motor data ident. (stationary) and speed contr. opt., operation

     After the MotID, the motor immediately goes into operation.
   - [12] Identify motor data (stationary), operation

     After the MotID, the motor immediately goes into operation.
2. Then select the desired technological application as the optimization criterion:

   - [SDC](#operating-mode) operating mode: Select "Optimization criteria" ([p0501](SINAMICS%20Parameter%20G220.md#p05010n-technological-application-standard-drive-control)) in the drop-down list.
   - [DDC](#operating-mode) operating mode: Select "Optimization criteria" ([p0502](SINAMICS%20Parameter%20G220.md#p05020n-technological-application-dynamic-drive-control)) in the drop-down list.
   - [Select other control type](#operating-mode) operating mode: Select "Optimization criteria" ([p0500](SINAMICS%20Parameter%20G220.md#p05000n-technology-application)) in the drop-down list.
3. If you want to make further settings in the next quick startup step, click "Next".

   - Or -

   If you want to optimize the drive online now, proceed as described below in Step 2 ff.

**Note**

The selection shown above is restricted depending on the motor type.

**Note**

For more details on the optimization criteria, see "[Optimization criteria in detail](#optimization-criteria-in-detail)".

##### Step 2: Activate master control

When an online connection has been established, the control bar is highlighted in color. The control elements are grayed-out apart from the "Activate" button. The remaining control elements become active only after you have activated the master control and set the enables.

> **Note**
>
> **Project lock not available when master control is active**
>
> As long as the master control for a drive is active, you cannot activate the project lock if project protection is active and the automatic project lock on inactivity is also suspended.

The master control can only be activated for one drive.

| Symbol | Meaning |
| --- | --- |
| 1. Establish an online connection to the drive if up until now you had worked in the offline mode. 2. Click the "Activate" button under "Master control".    The "Activate master control" message window opens. 3. Read the warning carefully. Check the monitoring time and if required, correct it.    The monitoring time specifies the time during which the connection from the operating unit to the drive is cyclically monitored. The minimum value is 1000 ms. 4. The "Stop with spacebar" option is active by default. When the option is activated the drive is always braked using the shutdown function OFF3 if you press the spacebar or if the focus switches. The focus switches when a dialog is opened (e.g. download dialog) or when switching from TIA Portal to another application.       | Symbol | Meaning |    | --- | --- |    |  | **Warning** |    | **Braking not guaranteed if the "Stop with spacebar" option is deactivated** Stopping by using the buttons on the control panel cannot be guaranteed in extreme operating modes. If the additional braking function "Stop with spacebar" is deactivated, it may no longer be possible to brake the motor via the TIA Portal. This can lead to accidents resulting in death or serious injury.  - Only deactivate the "Stop with spacebar" option in absolute exceptional cases and if it has been ensured that you are able to stop the drive safely using suitable hardware solutions. |  |     - Optional: If you do not want to use the "Stop with spacebar" option, deactivate this option in the message window.       This setting requires a safety confirmation. The message window cannot be closed without confirmation.    - Also activate the "Continue without quick stop function via spacebar and focus switch" option. 5. To close the message window, click the "OK" button.     The message window closes. The master control is then active. |  |

##### Step 3: Performing motor data identification

> **Note**
>
> **Manually selecting the measurement type**
>
> We only recommend to experienced users that they manually select the measurement type from the list. Numerous detail values must be defined in the configuration dialog box for the measurement types "Stationary measurement" and "Rotating measurement" (see [Parameter values](#parameter-values-for-experts)).

1. To set the drive enables, click "Set" in the "Drive enables" area.
2. Click the "1" icon in the "Switch on" area to switch on the motor.
3. Click the "Activate" button in the "Measurement" area to start the measurement.

   A status display at the center of the step shows how the measurement is progressing ([r0047](SINAMICS%20Parameter%20G220.md#r0047-motor-data-identification-and-speed-controller-optimization)).

   The measurement ends independently and a message appears stating that the drive is in the "Switching on inhibited" state.

   After the measurement, the new parameter values are displayed in the results table. You can view and check the new values.
4. Check the values that have been determined to ensure that they are plausible. If the values do not seem appropriate, perform another measurement.
5. If you do not want to perform any more measurements, click the "0" icon in the motor and infeed area.

##### Step 4: Deactivate master control

Following conclusion of the optimization, the master control can be returned as follows:

1. Click the "Deactivate" button under "Master control".

   The "Deactivate master control" message window opens.
2. If you really want to deactivate the master control, click "Yes".

   The grayed-out user interface of the "Deactivate" button indicates that the master control is deactivated.

##### Result

**If optimization takes place online:**

The default settings for the motor data identification become effective the first time the motor is switched on. A corresponding MotID is performed, after which the motor immediately goes into operation depending on the settings.

If required, you can further configure the drive via the connectable control panel.

> **Note**
>
> In the "Standard Drive Control" (SDC) operating mode, the behavior of the motor may change considerably (e.g. higher speed) due to the change in the technological application (p0501). Therefore, be suitably cautious when starting the motor.

**If optimization is only preset:**

The optimization settings are preset. The last step "Overview" is displayed.

##### Additional parameters

---

#### Optimization criteria in detail

##### Overview

Depending on the set operating mode, various technological applications are offered as optimization criteria. The details of the individual technological applications are explained below.

##### Optimization for "Other control types" (p0500)

|  | Technological application | Explanation |
| --- | --- | --- |
| 0 | Standard drive | - Factory setting for control with or without speed encoder - In all applications that do not fit the other setting options. |
| 1 | Pumps and fans | - Optimized utilization of the converter output voltage by reducing the voltage reserve at higher speeds   If high load surges in the range of low and medium speeds cannot be ruled out, we recommend setting p0501 = 0. - Applications involving pumps and fans |
| 2 | Encoderless control down to f = 0 (passive loads) | - Setting for encoderless control of induction motors - Speed-controlled operation of induction motors at low speeds - Speed-controlled operation of reluctance motors with pulse technique (license required) - A passive load cannot accelerate the current-free motor.   Examples are pumps, fans, extruders, but not hoisting gear |
| 3 | Pumps and fans, efficiency optimization | - Setting for control of induction motors - Suitable for applications without dynamic requirements for speed and load changes - A passive load cannot accelerate the current-free motor.   Examples are pumps, fans - Efficiency optimization   Less energy consumption and reduced noise - The setting only makes sense for steady-state operation with slow speed changes. We recommend the setting 0 if load surges in operation cannot be ruled out. |
| 5 | Starting with high break loose torque | - Setting for encoderless control (all motor types) - For speed-controlled operation at low speeds, the current is raised via p1610. - A break loose torque is a high load in the lower speed range - Increased default setting of the static torque setpoint (p1610) |
| 6 | High load inertia | - Setting for drives with high power and a total moment of inertia at least 5 times greater than the motor moment of inertia - Increased presetting of speed actual value smoothing - Optimized presetting of the speed controller |

##### Optimization with Standard Drive Control SDC (p0501)

|  | Technological application | Explanation |
| --- | --- | --- |
| 0 | Constant load (linear characteristic) | - Setting for all drives without speed-dependent load characteristic - High load torque even at low speeds |
| 1 | Speed-dependent load (parabolic characteristic) | - Setting, e.g. for parabolic load characteristics for pumps, fans - Only small load torques at low speeds - Full load is reached at the rated operating point - If high load surges in the range of low and medium speeds cannot be ruled out, we recommend setting p0501 = 0. |

##### Optimization with Dynamic Drive Control DDC (p0502)

|  | Technological application | Explanation |
| --- | --- | --- |
| 0 | Standard drive, e.g. pumps and fans | - Factory setting for control with or without speed encoder - Recommended setting for standard applications |
| 1 | Dynamic starting or reversing | - Setting for encoderless control of induction motors - Recommended setting for applications with short ramp-up and ramp-down times of less than 10 s - Starting from standstill with closed-loop speed control   Requirement: The speed setpoint at the ramp-function generator input is greater than the switchover speed p1755 |
| 2 | Encoderless control down to f = 0 (passive loads) | - Setting for encoderless control of induction motors - Speed-controlled operation of induction motors at low speeds - Speed-controlled operation of reluctance motors with pulse technique (license required) - A passive load cannot accelerate the current-free motor.   Examples are pumps and fans, but not hoisting gear |
| 5 | Starting with high break loose torque | - Setting for encoderless control (all motor types) - For speed-controlled operation at low speeds, the current is raised via p1610. - A break loose torque is a high load in the lower speed range - Increased default setting of the static torque setpoint (p1610) |
| 6 | High load inertia | - Setting for drives with high power and a total moment of inertia at least 5 times greater than the motor moment of inertia - Increased presetting of speed actual value smoothing - Optimized presetting of the speed controller |

> **Note**
>
> The selection shown above (0, 1, 5, 6) is limited for the synchronous motor types RESM and PMSM.

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
2. Proceed as described under "[Download to device](Configuring%20SINAMICS%20G220%20drives.md#loading-the-configuration-from-the-project-to-the-device)".

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
3. Proceed as described under "[Upload from device](Configuring%20SINAMICS%20G220%20drives.md#loading-the-configuration-from-the-device-to-the-project)".

## Parameterization

This section contains information on the following topics:

- [Overview](#overview-2)
- [Basic parameterization](#basic-parameterization)
- [Inputs/outputs](#inputsoutputs)
- [Setpoint channel](#setpoint-channel)
- [Drive control](#drive-control)
- [Drive functions](#drive-functions)
- [Safety Integrated](#safety-integrated)
- [Technology functions](#technology-functions)

### Overview

#### Differences between offline and online parameterization

Settings performed offline in the "Parameterization" area generally must be downloaded to the drive before they become active (see [Downloading project data to the device](Configuring%20SINAMICS%20G220%20drives.md#loading-the-configuration-from-the-project-to-the-device)).

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
  There is an active [online connection](Configuring%20SINAMICS%20G220%20drives.md#establishing-an-online-connection-to-the-target-device) between the drive and the operating unit.
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

The parameterization functions (function view/parameter view) can be set in the standard scope or extended scope. On the 1st call, only the functions of the standard parameter assignment are displayed in the secondary navigation.

- Click ![Switching the display: Standard/Extended](images/153507418891_DV_resource.Stream@PNG-en-US.PNG) to display the functions for extended parameterization.
- Click ![Switching the display: Standard/Extended](images/153509539339_DV_resource.Stream@PNG-en-US.PNG) to reduce the display to the functions of standard parameterization again.

The following extended parameterization functions can be displayed in the function view:

| Menu | Extended parameterization functions |
| --- | --- |
| Basic parameterization | Encoder evaluation |
| Data sets |  |
| Sampling times |  |
| Reference parameters |  |
| Line contactor control |  |
| Inputs/outputs | Analog inputs |
| Analog outputs |  |
| Isolated digital inputs |  |
| Digital outputs isolated |  |
| Drive control | Setpoint addition |
| Speed setpoint filter |  |
| Torque setpoints |  |
| Torque limitation |  |
| Current setpoint filter |  |
| Flux setpoint |  |
| Current controller |  |
| Motor data |  |
| Drive functions | Vdc min/max controller |
| Blocking message |  |
| Load torque monitoring |  |
| Variable signaling function |  |
| Stall message |  |
| Friction characteristic |  |
| Encoder functions |  |
| Bypass operation |  |

The switchover of the display to some extent also has an effect within the function views. However, a list at this point would be too extensive.

> **Note**
>
> The display of the functions listed in the table is to some extent dependent on other default settings, for example the operating mode or the motor type. Details on this topic are provided in the detailed description of the specific function.

> **Note**
>
> **Access from the inspection window**
>
> By clicking on the link in the Inspector window, the program jumps to the detailed settings of the linked target. If the detailed settings belong to the extended parameterization, then this function view is automatically displayed, even if only the standard parameterization was previously displayed. The secondary navigation is automatically adapted to the functions of the extended parameterization.

#### Manually navigating between function views

You can navigate between function views using the two navigation buttons:

| Button | Explanation |
| --- | --- |
| ![Manually navigating between function views](images/165979777547_DV_resource.Stream@PNG-en-US.png) | Shows the next function view. However, the function view must already have been displayed once before. |
| ![Manually navigating between function views](images/165979781899_DV_resource.Stream@PNG-en-US.png) | Shows the last function view that was displayed before the current function view. |

### Basic parameterization

This section contains information on the following topics:

- [Configuration summary](#configuration-summary)
- [Operating mode](#operating-mode-1)
- [Limits](#limits-1)
- [Optimizations](#optimizations)
- [Encoder evaluation](#encoder-evaluation)
- [Data sets](#data-sets)
- [Sampling times](#sampling-times)
- [Reference parameters](#reference-parameters)
- [Line contactor control](#line-contactor-control)

#### Configuration summary

##### Overview

The "Configuration summary" function view lists the most important basic settings of the drive from the device configuration and the guided quick startup. It consists of two parts:

- General functions

  - Device name
  - Supply voltage
  - Rated power
  - Telegram
  - Safety Integrated

  All of the data refer to the currently active drive data set.
- Motor

  Shows all motor data of the motor from the active drive data set.

Based on this summary, you can then decide which settings should still be made in the "Parameterization" area.

##### Requirement

- The drive has been completely created and fully specified in the device configuration.

##### Additional parameters

---

#### Operating mode

##### Overview

Using the "Operating mode" function view, you can define the required operating mode and therefore also define the underlying control type. The following settings are possible:

- Standard Drive Control (SDC)

  For standard motor and drive applications.   
  Basic setting for induction motors.
- Dynamic Drive Control (DDC)

  For demanding applications with high utilization of the motor and drive.   
  Basic setting for synchronous motors and reluctance motors. This setting cannot be changed.
- Selecting other closed-loop control types

  Enables manual selection of the control type.

The following control types ([p1300](SINAMICS%20Parameter%20G220.md#p13000n-open-loopclosed-loop-control-type)) are available for detailed selection:

| Operating mode | Control type |
| --- | --- |
| Standard Drive Control (SDC) | no selection possible |
| Dynamic Drive Control (DDC) | - [20] Closed-loop speed control (encoderless) - [21] Closed-loop speed control (with encoder) |
| Selecting other closed-loop control types | - [0] U/f control with linear characteristic - [1] U/f control with linear characteristic and FCC - [2] U/f control with parabolic characteristic - [3] U/f control with parameterizable characteristic - [4] U/f control with linear characteristic and ECO - [5] U/f control for drives requiring a precise frequency (textile sector) - [6] U/f control for drives requiring a precise frequency and FCC - [7] U/f control with parabolic characteristic and ECO - [19] U/f control with independent voltage setpoint - [20] Closed-loop speed control (encoderless) - [21] Closed-loop speed control (with encoder) - [22] Torque control (encoderless) - [23] Torque control (with encoder) |

> **Note**
>
> You also can make these settings via the [guided quick startup](#operating-mode).

##### Requirement

- The drive has been completely created and fully specified in the device configuration.

##### Procedure

1. Activate the required operating mode ([p0504](SINAMICS%20Parameter%20G220.md#p05040n-operating-mode)) or activate option "Select other control types".

   For reluctance motors, the "DDC" operating mode is preset and cannot be changed.

   If "DDC" is selected, then closed-loop speed control is automatically set as control type. Whether closed-loop speed control is pre-selected with or without encoder depends on the setting in the device configuration. If an encoder is available in the device configuration, then "Closed-loop speed control (with encoder)" is pre-selected.
2. Select the required control type (p1300) if you selected option "Select other control types" or operating mode "DDC".

##### Result

If you selected either SDC or DDC, the function view then lists the typical applications and parameters of this operating mode. Additional default settings are made for the drive according to the operating mode/control type. With SDC, configurability for open-loop and closed-loop control functions is severely limited.

##### Properties of the operating modes

Areas of application and parameters of the operating modes

|  | Standard Drive Control | Dynamic Drive Control | Other control types |
| --- | --- | --- | --- |
| Typical areas of application | - Pumps, fans and compressors with flow characteristic - Blasting technology (wet and dry blasting) - Mills, mixers, kneaders, crushers, agitators - Horizontal conveyor technology (conveyor belts, roller conveyors, chain conveyors) - Basic spindles | - Demanding applications with high utilization of the motor and converter - Pumps and compressors with displacement machines - Rotary kilns - Extruders - Centrifuges - Vertical conveyor technology (conveyor belts, roller conveyors, chain conveyors) with encoder - Escalators, lifting/lowering gear, elevators, overhead cranes with encoder - Cable railways with encoder - Storage and retrieval machines with encoder - Encoderless synchronous motors - Reluctance motors | - All control types with corresponding function views are available. |
| Typical characteristic values | - Robust vector control for simple handling - Drive commissioning only via rated motor current/speed - Motor power up to 45 kW - Ramp times greater than 5 - 10 s - Continuous motion with constant load - Static torque limitation (500 ms) - Stationary speed accuracy (transient recovery time 100 - 200 ms) | - Precise vector control: Efficient utilization of power unit, motor and mechanical system - Particularly recommended for motor powers greater than 45 kW - Required for ramp times less than 2 s - Continuous motion with dynamic load - High speed control accuracy during setpoint response and transient response - Dynamically controlled transient response (fast, high load surges) - Dynamic torque limitation (20 ms) - Heavy starting (with up to 90% breakdown torque) | - All control types with corresponding function views are available. |

##### Additional parameters

---

#### Limits

##### Overview

Define basic properties of the drive control via the "Limits".

| Designation | Parameter | Description |
| --- | --- | --- |
| Supply voltage | [p0210](SINAMICS%20Parameter%20G220.md#p0210-device-supply-voltage) | Determines the converter supply voltage.   The value affects the following:  - Switch-on threshold for the braking resistor - Activation thresholds of the Vdc_max and Vdc_min control - Selection of the rated values of the power unit   The setting of the parameter determines whether the power unit is operated in the lower or upper voltage range. - Power failure monitoring |
| Current limit motor current | [p0640](SINAMICS%20Parameter%20G220.md#p06400n-motor-current-limit) | Determines the limit value of the motor overload current. |
| Minimum speed | [p1080](SINAMICS%20Parameter%20G220.md#p10800n-minimum-speed) | Setting of the lowest possible speed/velocity. This value is not fallen below in operation. |
| Maximum speed | [p1082](SINAMICS%20Parameter%20G220.md#p10820n-maximum-speed) | Setting of the highest possible speed/velocity. This value is calculated during the commissioning phase depending on the motor and drive unit and can only be equal to or less than the value in [p0322](SINAMICS%20Parameter%20G220.md#p03220n-maximum-motor-speed) (maximum motor speed). |
| Positive speed limit | [p1083](SINAMICS%20Parameter%20G220.md#p10830n-speed-limit-in-positive-direction-of-rotation) | Sets the speed limit for the positive direction. Only visible and parameterizable in the "Extended" display mode. |
| Negative speed limit | [p1086](SINAMICS%20Parameter%20G220.md#p10860n-speed-limit-in-negative-direction-of-rotation) | Sets the speed limit for the negative direction. Only visible and parameterizable in the "Extended" display mode. |
| Ramp-up time | [p1120](SINAMICS%20Parameter%20G220.md#p11200n-ramp-function-generator-ramp-up-time) | The ramp-up/ramp-down time always refers to the time interval from motor standstill to the set maximum speed (without using roundings). |
| Ramp-down time | [p1121](SINAMICS%20Parameter%20G220.md#p11210n-ramp-function-generator-ramp-down-time) |  |
| Ramp-down time (OFF3) | [p1135](SINAMICS%20Parameter%20G220.md#p11350n-off3-ramp-down-time) | The OFF3 ramp-down time is effective from the maximum speed down to the motor standstill. |

The limits can be defined ONLINE as well as OFFLINE.

> **Note**
>
> You also can make these settings via the [guided quick startup](#limits).

##### Requirement

- The motor used in the device configuration of the drive has been completely specified and configured.

  This basic parameterization cannot be performed without complete configuration.

##### Procedure

If necessary, correct the specified default values.

##### Additional parameters

---

#### Optimizations

##### Overview

In this function view, you make the default settings for optimizing the motor data which will be activated the first time the motor is switched on.

The motor identification (MotID) required for optimization serves as resource to determine the motor data, e.g. of third-party motors. The control properties of the motor are to be improved using MotID. Especially for encoderless speed control, as a minimum the stator resistance (including the supply cable resistance) and the power unit parameters must be determined for each drive.

> **Note**
>
> You also can make these settings via the [guided quick startup](#rotate-optimize).

##### Requirements

- The motor used in the device configuration of the drive has been completely specified and configured.
- The motor is switched off.

##### Procedure

1. In the drop-down list "Motor data identification and rotating measurement" ([p1900](SINAMICS%20Parameter%20G220.md#p1900-motor-data-identification-and-rotating-measurement)), select whether and how the motor data identification will be performed with a stationary or a rotating motor.

   - [0] No optimization
   - [1] Identify motor data, optimize speed controller

     Recommended if you have set "Speed control" as the control type. The drive then optimizes the speed controller.
   - [2] Identify motor data (at standstill)

     Recommended if you have set "Closed-loop speed control" as the control type, but the motor cannot rotate freely, e.g. if the traversing paths are mechanically restricted.
   - [3] Optimize speed controller (rotating)

     Motor data identification for rotating motor. Recommended if identification has already been performed with the motor stopped.
   - [11] Identify motor data, optimize (rotating), operation

     After the MotID, the motor immediately goes into operation.
   - [12] Identify motor data, operation

     After the MotID, the motor immediately goes into operation.
2. Then select the desired technological application as the optimization criterion:

   - [SDR](#operating-mode-1) operating mode: Select "Optimization criteria" ([p0501](SINAMICS%20Parameter%20G220.md#p05010n-technological-application-standard-drive-control)) in the drop-down list.
   - [DDR](#operating-mode-1) operating mode: Select "Optimization criteria" ([p0502](SINAMICS%20Parameter%20G220.md#p05020n-technological-application-dynamic-drive-control)) in the drop-down list.
   - "Select other control type" operating mode: Select "Optimization criteria" ([p0500](SINAMICS%20Parameter%20G220.md#p05000n-technology-application)) in the drop-down list.

**Note**

For more details on the optimization criteria, see "[Optimization criteria in detail](#optimization-criteria-in-detail)".

##### Result

The preliminary settings carried out online for the motor data identification become effective the first time the motor is switched on. For an offline configuration, the data must first be downloaded to the drive. A MotID is executed, after which the motor immediately goes into operation depending on the settings.

> **Note**
>
> In the "Standard Drive Control" (SDR) operating mode, the behavior of the motor may change considerably (e.g. higher speed) due to the change in the technological application (p0501). Therefore, be suitably cautious when starting the motor.

##### Additional parameters

---

#### Encoder evaluation

This section contains information on the following topics:

- [Overview](#overview-3)
- [Configuring the encoder evaluation](#configuring-the-encoder-evaluation)

##### Overview

###### Fundamentals of actual position values

The actual position values are provided according to the PROFIdrive standard in Gn_XIST1 ([r0482](SINAMICS%20Parameter%20G220.md#r048202-encoder-position-actual-value-gn_xist1)) and Gn_XIST2 ([r0483](SINAMICS%20Parameter%20G220.md#r048302-encoder-position-actual-value-gn_xist2)) (n = 1 or 2, number of the encoder).

- **Gn_XIST1**:   
  Here, the incremental position change of the encoder is transferred to the controller.
- **Gn_XIST2**:

  Here, different position information can be transmitted in accordance with the PROFIdrive standard. The required values must be requested via the encoder control word (r0480). For example, this can be the absolute position for absolute encoders or the zero mark position for incremental encoders with a zero mark.

###### Requirements

- The motor used in the device configuration of the drive axis has been completely specified and configured.

  This basic parameterization cannot be performed without complete configuration.
- The encoder used in the device configuration of the drive, including the encoder evaluation selection, has been completely specified and configured.

  Without complete configuration, this function view would not be displayed in the basic parameterization and a parameterization would not be possible.

###### Fine resolution position value for XIST_2 ([p0419](SINAMICS%20Parameter%20G220.md#p04190n-fine-resolution-absolute-value-gx_xist2-in-bits))

The position value of the Gn_XIST2 includes a fine resolution (p0419). The position values of the absolute position are multiplied within one sinusoidal period.

###### Relationship between multiturn resolution and fine resolution (p0419 - X_IST2)

The actual encoder values transferred from the drive to the controller are limited to 32 bits. If, for example, a standard multiturn encoder with a multiturn resolution of 12 bits (4096) and a number of encoder pulses per revolution of 2048 (=2<sup>11</sup>) is used, only 32-12-11=9 bits (512) remain in the actual encoder value for the fine resolution (p0419). The following graphic shows the relationship between multiturn information and fine resolution. Increasing the fine resolution moves the value of the multiturn information to the left, which decreases the multiturn range of the encoder that can be used.

![Relationship between multiturn resolution and fine resolution (p0419 - X_IST2)](images/149062007947_DV_resource.Stream@PNG-en-US.png)

###### Measuring gearbox position tracking

The position tracking serves to reproduce and extend the traversing range of the load position when measuring gearboxes are used. Measuring gearboxes are deployed when the encoder is not mounted on the motor shaft, but rather, for example, driven with a belt or gear wheels with different diameters. The transformation ratio must not be 2<sup>n</sup>. The position tracking can also be used to extend the measuring range of the encoder for a linear axis.

**Virtual multiturn resolution ([p0412](SINAMICS%20Parameter%20G220.md#p04120n-measuring-gearbox-absolute-encoder-rotary-revolutions-virtual))**

For a rotary absolute encoder ([p0404](SINAMICS%20Parameter%20G220.md#p04040n023-encoder-configuration-effective).1 = 1) with activated position tracking ([p0411](SINAMICS%20Parameter%20G220.md#p04110n03-measuring-gearbox-configuration).0 = 1), p0412 specifies a virtual multiturn resolution. This makes it possible to generate a virtual multiturn encoder (r0483) from a singleturn encoder. It must be possible to represent the virtual encoder range in r0483.

When no measuring gearboxes (n = 1) are present, the actual number of stored revolutions of a rotary absolute encoder replaces the value in [p0421](SINAMICS%20Parameter%20G220.md#p04210n-absolute-encoder-rotary-multiturn-resolution). Increasing this value extends the position range (see linear axis). When measuring gearboxes are present, this value sets the resolvable motor revolutions represented in r0483.

**Tolerance window ([p0413](SINAMICS%20Parameter%20G220.md#p04130n-measuring-gearbox-position-tracking-tolerance-window))**

After switch on, the difference between the stored position and the current position is determined and initiated depending on the following:

- Difference within the tolerance window: The position is reproduced based on the current actual encoder value.
- Difference outside the tolerance window: Message F07449 is output.
- The tolerance window is preassigned to the encoder range quadrant, although it can be changed.

###### Additional parameters

---

##### Configuring the encoder evaluation

###### Overview

The encoder can be evaluated ONLINE as well as OFFLINE. Depending on the encoders used in the drive, different detail settings are possible in this function view.

###### Requirements

- The motor used in the device configuration of the drive axis has been completely specified and configured.
- The encoder used in the device configuration of the drive, including the encoder evaluation selection, has been completely specified and configured.

  Without complete configuration, this function view would not be displayed in the basic parameterization and a parameterization would not be possible.
- The [extended parameterization](#overview-2) is active.

###### Selecting encoders for configuring the evaluation

If the drive is equipped with several encoders, then these can be used as motor encoder and as external encoder (see [Managing the drive data set](#managing-a-drive-data-set-dds)). The settings for the encoder evaluation differ depending on the specific use.

1. If the drive is equipped with several encoders, in the drop-down list, select the application use (e.g. motor encoder).
2. Activate all of the options required (see possible detail settings) for the encoder evaluation and make the required detail settings.

###### Possible detail settings

| Settings | Description |
| --- | --- |
| **Inversion** |  |
| Invert the speed actual value ([p0410](SINAMICS%20Parameter%20G220.md#p04100n01-encoder-inversion-actual-value)[0].0) | The parameter is already preassigned for standard motors.   The counting direction of the encoder (p0410 Bit0 = 1 and Bit1 = 1) can be set for third-party or modular motors. The counting direction (speed and position) of the encoder is inverted. |
| Invert position actual value (p0410[0].1) |  |
| **Advanced settings** |  |
| Activate additional messages ([p0437](SINAMICS%20Parameter%20G220.md#p04370n126-sensor-module-configuration-extended)[0].12) | Activates additional error messages for extended fault diagnostics. |
| Switch-off encoder voltage supply during parking ([p0430](SINAMICS%20Parameter%20G220.md#p04300n1927-sensor-module-configuration)[0].25) | Activates the option. |
| Extended cyclic DQ telegram ([p0454](SINAMICS%20Parameter%20G220.md#p04540n4-sensor-module-configuration-extended-part-2)[0].0) | Activates an extended cyclic DQ telegram. This requires a subsequent restart. |
| Encoder ramp-up time ([p0439](SINAMICS%20Parameter%20G220.md#p04390n-encoder-ramp-up-time)[0]) | Automatic pre-assignment of the ramp-up time when using encoders from the encoder list or an encoder identification. |
| **Measuring gearbox position tracking** |  |
| Activate axis type ([p0411](SINAMICS%20Parameter%20G220.md#p04110n03-measuring-gearbox-configuration)) | In the case of a linear axis, position tracking is mainly used to extend the position range. |
| Virtual multiturn resolution ([p0412](SINAMICS%20Parameter%20G220.md#p04120n-measuring-gearbox-absolute-encoder-rotary-revolutions-virtual)) | Default value for a rotary absolute encoder.  This field is deactivated for a linear axis. |
| Tolerance window ([p0413](SINAMICS%20Parameter%20G220.md#p04130n-measuring-gearbox-position-tracking-tolerance-window)) | Default value for the tolerance window for position tracking. |
| **Incremental tracks** |  |
| Filter bandwidth ([p4660](SINAMICS%20Parameter%20G220.md#p46600n-sensor-module-filter-bandwidth)) | Sets the filter bandwidth for Sensor Module SMx10 (resolver) and SMx20 (sin/cos). |
| Speed calculation mode (only SMC30) (p0430[0].20) | If activated, the speed is calculated via the incremental difference without extrapolation.  If deactivated, the speed is calculated via edge time measurement with extrapolation. [p0453](SINAMICS%20Parameter%20G220.md#p04530n-pulse-encoder-evaluation-zero-speed-measuring-time) is effective in this mode. |
| Edge evaluation | Possible settings:   - 4-fold - 4-fold with averaging - 1-fold |
| Freezing the actual speed for dn/dt errors (p0437[0].6) | If activated, the speed actual value is internally frozen for two current controller sampling times when dn/dt monitoring responds. The rotor position continues to integrate. The actual value is then re-enabled after this time has expired. |
| De-select track monitoring (p0437[0].26) | If activated, track monitoring is deactivated for the square-wave encoders, even if it is selected in [p0405](SINAMICS%20Parameter%20G220.md#p04050n06-square-wave-encoder-track-ab).2. |
| Filter time ([p0438](SINAMICS%20Parameter%20G220.md#p04380n-square-wave-encoder-filter-time)) | Filter time at the square-wave encoder. The most suitable filter time depends on the number of pulses and maximum speed of the square-wave encoder. |
| Zero speed measuring time (p0453) | Measuring time for the evaluation of zero speed. Necessary for slow-running motors. |
| Speed actual value mean value generation ([p4685](SINAMICS%20Parameter%20G220.md#p46850n-speed-actual-value-average-value-generation)) | Number of current controller sampling times for mean value generation of the speed actual value for a square-wave encoder. |
| **Absolute value Gx_XIST2** |  |
| De-select monitoring multiturn representation in Gx_XIST2 (p0437[0].25) | Activates the option. |
| Fine resolution Gx_XIST2 ([p0419](SINAMICS%20Parameter%20G220.md#p04190n-fine-resolution-absolute-value-gx_xist2-in-bits)) | Enter the fine resolution of the encoder being used in bits.   The fine resolution is already preset to 9 bits for sinusoidal SIEMENS encoders. |
| **Encoder serial number** |  |
| Apply values | Applies the values from the last commissioning. |
| Extrapolate position value (p0430[0].27) | This setting is only displayed for pure SSI encoders, i.e. for encoders without additional incremental tracks. Compared with the current controller clock of the SINAMICS, the serial transfer is relatively slow, and therefore the data can already be obsolete on arrival at the Sensor Module.  - Advantage: The dead time decreases and the controller becomes more dynamic. - Disadvantage: The extrapolated value can be inaccurate with dynamic position changes. |
| Resolution absolute position as factor (p0437[0].22) | If activated, the resolution of the absolute position in the serial protocol is set using a distribution factor in p4630. The resolution for the absolute position is then calculated using p0407/p4630. |
| Absolute encoder linear measuring increments (p4630) | Resolution of the absolute position for a linear absolute encoder as factor from p0407. |

###### Additional parameters

---

#### Data sets

This section contains information on the following topics:

- [Overview](#overview-4)
- [Structure of the data set function view](#structure-of-the-data-set-function-view)
- [Managing a drive data set (DDS)](#managing-a-drive-data-set-dds)
- [Managing a command data set (CDS)](#managing-a-command-data-set-cds)
- [Activating or editing data sets](#activating-or-editing-data-sets)
- [Switching data sets](#switching-data-sets)

##### Overview

###### Fundamentals

For many applications it is beneficial if multiple parameters can be changed simultaneously by means of an external signal during operation or when the system is ready for operation. This can be carried out with the aid of indexed parameters. For the purpose of this function, the parameters have been combined in such a way that they form groups or data sets and are indexed. By using the indexing, several different settings can be stored for each parameter and activated by changing the data set (i.e. switching back and forth between the data sets).

Those parameters (signal sinks) that are used to control the converter and to enter a setpoint are assigned to the command data set (CDS).

The drive data set (DDS) contains various adjustable parameters that are relevant for the open-loop and closed-loop motor control.

You can configure the data sets for each drive within a project:

- You create the corresponding components in the device configuration.
- You configure the available data sets in Startdrive while creating new data sets or deleting existing data sets.

###### Requirement

- The [extended parameterization](#overview-2) is active.

###### Function diagrams (FD)

Command data sets (CDS) - 8560 -

Drive data sets (DDS) - 8565 -

Encoder data sets (EDS) - 8570 -

Motor data sets (MDS) - 8575 -

###### Additional parameters

- [p0120](SINAMICS%20Parameter%20G220.md#p0120-number-of-power-unit-data-sets-pds)
- [p0130](SINAMICS%20Parameter%20G220.md#p0130-number-of-motor-data-sets-mds)
- [p0140](SINAMICS%20Parameter%20G220.md#p0140-number-of-encoder-data-sets-eds)
- [p0170](SINAMICS%20Parameter%20G220.md#p0170-number-of-command-data-sets-cds)
- [p0180](SINAMICS%20Parameter%20G220.md#p0180-number-of-drive-data-sets-dds)

---

---

**See also**

[Rules for the use of data sets](Configuring%20SINAMICS%20G220%20drives.md#rules-for-the-use-of-data-sets)

##### Structure of the data set function view

###### Structure of the data sets

![Example: Function view for command data sets](images/153909176075_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | - Icon: Saves data protected against power failure (in online mode) - Icon: Restores the factory settings (in online mode) - Button ![Structure of the data sets](images/153509539339_DV_resource.Stream@PNG-en-US.PNG): Switches between standard functions and extended functions. Data sets belong to the extended functions. - Drop-down lists for switching over DDS and CDS data sets - Icons for editing/activating DDS drive data sets in online mode. Not relevant for CDS. |
| ② | Two buttons in the active function view enable the insertion and deletion of individual data sets of the list. |
| ③ | List of the created drive or command data sets. The created data sets are numbered chronologically.   In the list of drive data sets, different (MDS or EDS) data sets are assigned to the drive data sets.   Each CDS or DDS data set can be assigned a separate name. The assigned name is displayed in the drop-down lists. |
| ④ | Work area for activating a selected data set via signal interconnections. |
| ⑤ | Only for DDS, when several MDS are available: Editing the motor number. If the MDS have the same motor numbers, additional settings relating to the motor are retained when the data set is switched. Example: Settings for the brake or for the thermal model. |

Example: Function view for command data sets

> **Note**
>
> **Data sets in online mode**
>
> The [editing mode](#activating-or-editing-data-sets) must be activated first in order to edit data sets in online mode. The editing mode is not required in the offline mode.

##### Managing a drive data set (DDS)

###### Overview

You can edit the drive data sets of the drive via the "Drive data sets (DDS)" function view.

###### Requirements

- At least 1 DDS exists.
- The basic parameterization of a drive axis has been opened in the secondary navigation.

###### Creating a new DDS as a copy of an existing DDS

New drive data sets always can be created via the "Drive data sets (DDS)" function view only as a copy of an existing data set.

1. Click "Add".

   The "Add new drive data set" dialog box opens.

   ![Adding a DDS](images/150374473355_DV_resource.Stream@PNG-en-US.PNG)

   ![Adding a DDS](images/150374473355_DV_resource.Stream@PNG-en-US.PNG)

   Adding a DDS

   The list shows the existing drive data sets which can be used as master copies.
2. Activate the "Copy" option for the existing data set which you want to use as a master copy.
3. Click "OK" in the dialog box to confirm your selection.

**Result**

The new drive data set is created from the selected template and also inserted in the last position of the list of drive data sets.

###### Naming the drive data set (DDS)

1. Select the DDS you want to name (or change the name of) from the list of drive data sets.
2. Select the existing name (default = DDS-xx) in the "Name" column. Enter a new name for the DDS.

   ![Rename DDS](images/150346582155_DV_resource.Stream@PNG-en-US.PNG)

   ![Rename DDS](images/150346582155_DV_resource.Stream@PNG-en-US.PNG)

   Rename DDS

   The name of the DDS is then updated wherever it is displayed, for example in a drop-down list.

###### Deleting a drive data set (DDS)

Drive data sets can be deleted only if there are at least two DDSs in the list.

1. Select the DDSs to be deleted in the list of drive data sets.

   The DDS is displayed again in detail in a worklist located below the collective list.
2. Click "Delete".

   A confirmation prompt is displayed.

   ![Example: Deleting a DDS](images/150374605323_DV_resource.Stream@PNG-en-US.PNG)

   ![Example: Deleting a DDS](images/150374605323_DV_resource.Stream@PNG-en-US.PNG)

   Example: Deleting a DDS
3. Click "OK" to delete the DDS.

**Result**

The DDS is deleted from the list of drive data sets. The following DDSs in the list are renumbered. The numbering of the DDSs is always chronological. The last available DDS remains and cannot be deleted.

###### Online mode: Assign encoder data sets (EDS)

The editing mode must be active in order to edit data sets in online mode.

1. Click the ![Online mode: Assign encoder data sets (EDS)](images/145986507659_DV_resource.Stream@PNG-de-DE.png) icon to start the editing mode.
2. Select a DDS in the list of drive data sets.
3. Click in the EDS cell of the data set row and select the required EDS from the "Motor encoder" drop-down list.

   If you want to assign 2 additional EDSs, repeat this step using the "External encoder 1" and "External encoder 2" drop-down lists.
4. Click the ![Online mode: Assign encoder data sets (EDS)](images/145986499211_DV_resource.Stream@PNG-de-DE.png) icon to exit the editing mode once the settings have been completed.

**Result**

The assigned data sets are displayed for the selected DDS in the list of drive data sets.

###### Offline mode: Assign encoder data sets (EDS)

In the offline mode, the data sets can be configured without an editing mode.

1. Select a DDS in the list of drive data sets.
2. Click in the EDS cell of the data set row and select the required EDS from the "Motor encoder" drop-down list.

   If you want to assign 2 additional EDSs, repeat this step using the "External encoder 1" and "External encoder 2" drop-down lists.

**Result**

The assigned data sets are displayed for the selected DDS in the list of drive data sets. The drive data then has to be downloaded to the drive for use in the drive.

###### Changing the assignment of physical motor

When creating MDS, a motor number of the physical motor is automatically created. The first MDS is assigned the number 0. The number is simply incremented for the following MDSs.

If several MDSs are used in the drive device configuration, which are based on the same physical motor, then you can assign the corresponding MDS the same motor number.

**Advantage of identical motor numbers**: Certain detailed settings, such as settings for the brake or for the thermal model, only have to be created for the motor of the first MDS. These settings remain the same when the data set is switched over.

Proceed as follows to assign an existing MDS the same motor number:

1. Display setting area "Assignment of physical motor".
2. Localize the motor number of the first MDS.
3. Select the row of another MDS, which uses the same physical motor.
4. Enter the number of the first motor in field "Number of the physical motor".
5. Repeat this procedure for all the MDSs that also use the same physical motor.
6. Save the project.

**Result**

Both MDSs now have the same number.

##### Managing a command data set (CDS)

###### Overview

You can edit up to four command data sets of the drive via the "Command data sets (CDS)" function view.

###### Requirements

- At least 1 CDS exists.
- Creating and deleting CDSs: There is no online connection to the drive.

  CDSs can only be created or deleted offline. However, CDSs can be activated online.

###### Creating a new CDS with contents from other CDSs

1. Click "Add".

   The "Add new command data set" dialog box opens.

   ![Adding a CDS](images/145986418187_DV_resource.Stream@PNG-en-US.png)

   ![Adding a CDS](images/145986418187_DV_resource.Stream@PNG-en-US.png)

   Adding a CDS
2. Activate the "Create as copy" option.
3. Click "OK" in the dialog box to confirm your selection.

**Note**

**Special case**

If there are 2 or more CDSs available, you can select here which CDS should be copied.

**Result**

The new command data set is created from the selected template and also inserted in the last position of the list of command data sets.

###### Creating a new command data set (CDS)

1. Click "Add".

   The "Add new command data set" dialog box opens.

   ![Adding a CDS](images/145986418187_DV_resource.Stream@PNG-en-US.png)

   ![Adding a CDS](images/145986418187_DV_resource.Stream@PNG-en-US.png)

   Adding a CDS
2. Make sure that the "Create as copy" option is deactivated.
3. Click "OK" in the dialog box.

**Result**

A new command data set is created in the list.

###### Naming a command data set (CDS)

1. Select the CDS you want to name (or change the name of) from the list of command data sets.
2. Select the existing name in the "Name" column (default = CDS-xx) and enter a new name for the CDS.

   ![Rename CDS](images/150346573579_DV_resource.Stream@PNG-en-US.PNG)

   ![Rename CDS](images/150346573579_DV_resource.Stream@PNG-en-US.PNG)

   Rename CDS

   The name of the CDS is updated wherever it is displayed, e.g. in a drop-down list.

###### Deleting a command data set (CDS)

Command data sets can be deleted only if there are at least 3 CDSs in the list.

1. Select the CDSs to be deleted in the list of command data sets.

   The CDS is displayed again in detail in a worklist located below the collective list.
2. Click "Delete".

   A confirmation prompt is displayed.

   ![Example: Deleting a CDS](images/150372508299_DV_resource.Stream@PNG-en-US.PNG)

   ![Example: Deleting a CDS](images/150372508299_DV_resource.Stream@PNG-en-US.PNG)

   Example: Deleting a CDS
3. Click "OK" to delete the data set.

**Result**

The CDS is deleted from the list of command data sets. The subsequent CDSs in the list will be renumbered if necessary. The numbering of the CDSs is always chronological. The last available CDS remains and cannot be deleted.

##### Activating or editing data sets

###### Overview

Several data sets of a data set type must be created for a data set switchover.

###### Editing offline

To assign the settings of a drive to a data set, proceed as follows:

1. Open the function view for the desired data set type (e.g. the function view for the drive data set).
2. Select the required data set from the list of data sets.
3. Change the signal sources of the signal interconnections at the bottom of the working area.
4. Save your settings [permanently](Configuring%20SINAMICS%20G220%20drives.md#permanently-save-the-settings).

**Result:**

Specific parameterizations are available for each of the various data sets.

###### Editing online

The editing mode must be active in order to edit data sets in online mode.   
To assign the settings of a drive to a data set, proceed as follows:

1. Click the ![Editing online](images/145986507659_DV_resource.Stream@PNG-de-DE.png) icon to start the editing mode.
2. Open the function view for the desired data set type (e.g. the function view for the drive data set).
3. Select the required data set from the list of data sets.
4. Change the signal sources of the signal interconnections at the bottom of the working area.
5. Save your settings [permanently](Configuring%20SINAMICS%20G220%20drives.md#permanently-save-the-settings).
6. Click the ![Editing online](images/145986499211_DV_resource.Stream@PNG-de-DE.png) icon to exit the editing mode once the settings have been completed.

**Result:**

Specific parameterizations are available for each of the various data sets.

###### DDS offline only: Assignment of the physical motor

By default, when motors are created in the device configuration of the drive, a different motor number is automatically defined for each MDS. To ensure that defined motor settings are retained when the data set is switched, the motor numbers can be aligned using the table in the "Assignment of physical motor" work area.

**Advantage with identical motor number:**

- If a motor brake is used, the brake remains open when the data set is switched.
- The same thermal model is applied.
- The correction values of the Rs, Lh or kT adaptation are passed along when the data set is switched.

**Requirement for assignment of an identical motor number:**

- The motor actually used is identical. The placeholder for the same motor is in the device configuration several times.

**Editing a motor number:**

1. Assign the same motor number for each MDS in the "Number of the physical motor" column.
2. Save your settings permanently.

##### Switching data sets

###### Overview

You can switch between different data sets in the function view. The switchover is performed via drop-down lists in the toolbar.

![Data set switchover](images/153902306187_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Shows the active drive data set (DDS). Enables switchover to a different data set. |
| ② | Shows the active command data set (CDS). Enables switchover to a different data set. |

Data set switchover

###### Requirement

- Multiple drive data sets or command data sets have been created.

  If only one data set of one data set type has been created, the drop-down list for switchover is deactivated.

###### Procedure

1. Open the required function view.

   The drop-down lists for the data set switchover show the active data set in each case. The settings and parameter values of this data set are displayed in the function view below them.
2. Select another data set from the drop-down lists for the data set switchover.
3. Change the signal sources of the signal interconnections at the bottom of the working area.

###### Result

In the function view, all data-set-dependent settings are changed to the values of the selected data set (if these values are configured differently). The differences in the drive data sets also may result solely from the MDSs or EDSs used in the selected DDS.

#### Sampling times

##### Overview

The sampling times of the functions are automatically preassigned when the drive is configured. Each controller circuit has a default setting.

You can completely change this default setting for all controller circuits using another data set. This allows you to utilize higher output frequencies. Alternatively, you can manually assign the sampling time for every controller circuit (Expert mode).

> **Note**
>
> **Recommendation**
>
> Each time you change a sampling time, recalculate the controller settings after commissioning has been completed.

> **Note**
>
> **Influence of subsequent parameterizations**
>
> Subsequent parameterizations in other functions can also influence the sampling times shown in this function view. In case of doubt, the sampling times are then overwritten.

##### Rules when manually setting the sampling time

- Higher-level controls must be calculated in integral ratios to lower-level controls.   
  Example: [p0115](SINAMICS%20Parameter%20G220.md#p011506-sampling-times-for-internal-control-loops)[1] = N * p0115[0]; with N = integer number.

  The sampling time of the speed controller (p0115[1]) can have as a maximum a value of 800% of the current controller sampling time (p0115[0]).
- The sampling times for setpoint channel (p0115[3]), position controller (p0115[4]), positioning (p0115[5]) and technology controller (p0115[6]) must have at least 2x the value of the current controller sampling time (p0115[0]).

##### Requirements

- The drive has been completely created and fully specified in the device configuration.
- The [extended parameterization](#overview-2) is active.

##### Changing sampling times using defined data sets

The sampling times are preset using parameter [p0112](SINAMICS%20Parameter%20G220.md#p0112-sampling-times-pre-setting-p0115).

1. Select one of the following defaults via the drop-down list "Configure sampling times" (p0112):

   - [3] Fixed values 4 kHz (default)
   - [5] Fixed values 4 kHz (speed controller)
   - [6] Fixed values 4 / 8 kHz (dynamic response)

   The designation of the defaults refer to the desired output frequency and control dynamic response.

   The display of the parameter values set for p0115 changes depending on the default setting made.

##### Manually entering sampling times

1. From the drop-down list "Configure sampling times" (p0112), select default:

   - [0] Sampling times can be changed

   With this setting, the expert mode is active.
2. Correct the default settings for the sampling times of the individual controller circuits:

   - p0115[0]: Current controller
   - p0115[1]: Speed controller
   - p0115[2]: Flux controller
   - p0115[3]: Setpoint channel
   - p0115[4]: Position controller
   - p0115[5]: Positioning
   - p0115[6]: Technology controller

**Note**

Slower time slices are only taken if the calculated sampling time is also permitted. Upper limit is 8 ms.

##### Result

The sampling times are changed.

##### Additional parameters

- [p1800](SINAMICS%20Parameter%20G220.md#p18000n-pulse-frequency-setpoint)

---

#### Reference parameters

##### Overview

The "Reference parameters" function view shows the elementary reference parameters and their values in a table:

- [p2000](SINAMICS%20Parameter%20G220.md#p2000-reference-speed-reference-frequency): Reference speed, reference frequency
- [p2001](SINAMICS%20Parameter%20G220.md#p2001-reference-voltage): Reference voltage
- [p2002](SINAMICS%20Parameter%20G220.md#p2002-reference-current): Reference currents
- [p2003](SINAMICS%20Parameter%20G220.md#p2003-reference-torque): Reference torque
- [r2004](SINAMICS%20Parameter%20G220.md#r2004-reference-power): Reference power
- [p2005](SINAMICS%20Parameter%20G220.md#p2005-reference-angle): Reference angle
- [p2006](SINAMICS%20Parameter%20G220.md#p2006-reference-temperature): Reference temperature
- [p2007](SINAMICS%20Parameter%20G220.md#p2007-reference-acceleration): Reference acceleration

##### Requirements

- The drive has been completely created and fully specified in the device configuration.
- The [extended parameterization](#overview-2) is active.

##### Correcting defaults

You can correct the defaults for all p parameters in the table:

1. In function view "Reference parameters", click in the "Values" field for the corresponding reference parameter.
2. Enter the desired new value.
3. Repeat steps 1 and 2 for the other reference parameters whose default settings you want to change.

##### Result

You have corrected the reference parameters. Save the settings in the project.

##### Additional parameters

---

#### Line contactor control

This section contains information on the following topics:

- [Line contactor control](#line-contactor-control-1)

##### Line contactor control

###### Overview

This function allows an external line contactor to be controlled. The closing and opening of the line contactor can be monitored by evaluating the feedback contact of the line contactor.

This function view shows the enabling interconnection of the line contactor.

###### Requirements

- The drive has been completely created and fully specified in the device configuration.
- The [extended parameterization](#overview-2) is active.

###### Procedure

1. Enter in the "Line contactor/monitoring time" ([p0861](SINAMICS%20Parameter%20G220.md#p0861-line-contactor-monitoring-time)) field, the monitoring time of the line contactor.  
   The monitoring time starts for each switching operation of the line contactor ([r0863](SINAMICS%20Parameter%20G220.md#r086301-drive-coupling-status-wordcontrol-word).1). If no feedback from the line contactor is detected within this time, a message is issued.
2. Interconnect the signal source for "Line contactor feedback signal" (c0860).

   Note for activated monitoring (c0860 not equal to r0863.1): Use the signal r0863.1 for the line contactor control for the local drive.
3. Interconnect the signal sink for "Control contactor (r0863.1)".

###### Result

You have configured the line contactor control. Save the settings in the project.

###### Additional parameters

---

### Inputs/outputs

This section contains information on the following topics:

- [Digital inputs](#digital-inputs)
- [Digital outputs](#digital-outputs)
- [Analog inputs](#analog-inputs)
- [Analog outputs](#analog-outputs)

#### Digital inputs

##### Overview

Here you can change the interconnection of the digital inputs on the control unit.

Digital inputs are used for the acquisition of digital signals. For example, drive enables can be controlled externally. The digital inputs are interconnected via signal interconnections.

For every digital input signal there is the corresponding inverted signal which can also be used for interconnection.

You can interconnect the following digital inputs:

- 0...5
- 11...12
- 21...22

##### Requirements

- The drive has been completely created and fully specified in the device configuration.
- The [extended parameterization](#overview-2) is active.

##### Procedure

1. Interconnect the signal sources of digital inputs 0 to 5, 11, 12, 21 and 22 and of the inverted digital inputs ([r0722](SINAMICS%20Parameter%20G220.md#r0722022-digital-inputs-status) and [r0723](SINAMICS%20Parameter%20G220.md#r0723022-digital-inputs-status-inverted)).

   Several interconnections are possible.

##### Function diagrams (FD)

Isolated digital inputs (DI 0 … DI 5, DI 21 ... DI 22) - 2221 -

##### Additional parameters

---

#### Digital outputs

##### Overview

Here you can change the interconnection for the digital outputs of the G220.

A digital output is used for the feedback of signals, such as enable signals. The digital outputs are interconnected via a signal interconnection.

##### Requirements

- The drive has been completely created and fully specified in the device configuration.
- The [extended parameterization](#overview-2) is active.

##### Procedure

1. Interconnect the signal sinks of digital outputs 0, 1 and 2.
2. If necessary, invert the desired digital outputs via the icon.

   The ![Procedure](images/148900737803_DV_resource.Stream@PNG-de-DE.png) symbol then indicates the inversion.

##### Function diagrams (FD)

Digital outputs 0 ... 2 (DO 0 ... DO 2) - 2242 -

##### Additional parameters

- c0730
- c0731
- c0732
- [p0748](SINAMICS%20Parameter%20G220.md#p074802-invert-digital-outputs)

---

#### Analog inputs

##### Overview

Here you can change the interconnection for the two analog inputs.

An analog input is used for the acquisition of external analog signals. These signals can be voltages or currents, for example. Analog inputs are used, for example, to specify an analog definition of a speed or torque.

##### Requirements

- The drive has been completely created and fully specified in the device configuration.
- The [extended parameterization](#overview-2) is active.

##### Making basic settings

1. Select the basic configuration of the input signal for the analog input 0 ([p0756](SINAMICS%20Parameter%20G220.md#p075601-analog-inputs-type)):

   - [0] Unipolar voltage input (0 V...+10 V)

     The analog input is configured as voltage input.
   - [1] Monitored unipolar voltage input (+2 V...+10 V)

     The analog input is configured as voltage input. This input is also monitored.
   - [2] Unipolar current input (0 mA...+20 mA)

     The analog input is configured as current input.
   - [3] Monitored unipolar current input (4 mA...+20 mA)

     The analog input is configured as current input. In addition, wire-break monitoring is active (see below).
   - [4] Bipolar voltage input (-10 V...+10 V)

     The analog input is configured as voltage input. The input range is +/-10 V.
   - [8] No sensor connected

     The analog input is configured as current input. The input range is +/-20 mA.
2. For the settings [0] to [4], the DIP switch must also be set in each case.

   - For a voltage input, set the DIP switch to "U".
   - For a current input, set the DIP switch to "I"
3. Enter the offset value for the analog input in the "Offset" field ([p0763](SINAMICS%20Parameter%20G220.md#p076301-analog-inputs-offset)).

   The offset value is added to the input signal before the standardization characteristic.
4. When using the 2nd analog input 1, repeat steps 1 to 3 for this input.

##### Configure scaling of the analog input

The scaling serves to adapt to the machine or to the existing components. For example, even when the complete input range of the voltage or the current is not utilized, the input value can still be scaled to 100%.

1. Click the "Scaling" button to configure the scaling.

   The "Scaling analog input AI 0" dialog opens.
2. Enter the x and y values for two points of the scaling line:

   - y2:   
     Top scaling value as percentage, e.g. y2 = 100% with x 2 = 10 V means that 10 V at the input correspond to 100% at the output.
   - y1:   
     Low scaling value as percentage, e.g. y1 = -100% with x1 = -10 V means that -10 V at the input correspond to -100% at the output.
   - x1:   
     Low input value to be scaled.
   - x2:   
     High input value to be scaled.
3. Click "Close" to confirm the settings.

##### Specify filter for the analog input (optional)

Analog values are always subject to noise. You can suppress this noise by using a filter.

The input signal can also be smoothed to suppress strong fluctuations or short-term peaks.

1. Enter the value for smoothing of the input signalin the "Smoothing" field ([p0753](SINAMICS%20Parameter%20G220.md#p075301-analog-inputs-smoothing-time-constant)).

   This value smooths the input signal using a PT1 filter. However, a smoothing value which is too high makes the input slow.
2. Enter the value for noise suppression in the "Noise suppression" field([p0768](SINAMICS%20Parameter%20G220.md#p076801-analog-inputs-noise-suppression-window)).

   This suppresses the noise of the input signal according to the following function:

   - **|y-x| > noise suppression results in y = x**

     The output value is set to the current input value.
   - **|y-x| ≤ noise suppression results in y = yold**

     The output value retains its value.

##### Configuring wire-break monitoring (optional)

Wire-break monitoring is used when the basic configuration "[3] Unipolar current input monitored (4 mA...+20 mA)" is set. In this case, the function view is extended by two additional input fields.

1. Enter the wire-break monitoring response threshold in the "Threshold" field ([p0761](SINAMICS%20Parameter%20G220.md#p076101-analog-inputs-wire-break-monitoring-response-threshold)).

   If the threshold value is undershot for longer than the delay time, a wire break is detected.
2. Enter the delay time ([p0762](SINAMICS%20Parameter%20G220.md#p076201-analog-inputs-wire-break-monitoring-delay-time)) for wire-break monitoring in the field to the right of the "Threshold" field.

   If the wire-break monitoring response threshold is undershot for longer than the delay time, a wire break is detected.

##### Additional functions (optional)

| Function | Description |
| --- | --- |
| Absolute-value generation | Switch on the absolute-value generation in the function view if the absolute value of the scaled input value is to be generated.   The activated absolute-value generation is indicated by the ![Additional functions (optional)](images/148900643851_DV_resource.Stream@PNG-de-DE.png) symbol. |
| Inversion | The signal source for inverting the analog input signals can be interconnected via a signal interconnection. Inversion is deactivated by default.   If you want to make an inversion, interconnect the signal source in the "Inversion" field (c0767). |
| Activate | The signal source for enabling the analog input can be interconnected via a signal interconnection. Enable is activated by default.   If required, correct the signal source (c0769). |
| Analog input 0 | Here you interconnect the signal sink for the input value of the analog input.   Several interconnections are possible. |
| Simulation mode | A simulation mode can be activated in online mode. |

##### Result

The analog inputs are configured.

##### Function diagrams (FD)

Analog inputs 0 ... 1 (AI 0 ... AI 1) - 2251 -

##### Additional parameters

---

#### Analog outputs

##### Overview

The Control Unit has one analog output (AO). You can use the analog output to display a wide range of signals, e.g. the current speed, the current output voltage or the current output current.

The function view shows the current I/O configuration. The analog outputs are preassigned accordingly.

##### Requirements

- The drive has been completely created and fully specified in the device configuration.
- The [extended parameterization](#overview-2) is active.

##### Making basic settings

1. Select the type of analog output 0 ([p0776](SINAMICS%20Parameter%20G220.md#p07760-analog-output-type)):

   - Current output (0 mA...+20 mA)

     The analog output is configured as current output.
   - Voltage output (0 V...+10 V)

     The analog output is configured as voltage output.
   - Current output (+4 mA...+20 mA)

     The analog output is configured as current output.
2. If necessary, interconnect the signal source of analog output 0 (c0771).
3. If you want to smooth the input signal, enter a smoothing value in the "Smoothing" ([p0753](SINAMICS%20Parameter%20G220.md#p075301-analog-inputs-smoothing-time-constant)) field.

   This value causes a smoothing of the input signal using a PT1 filter. However, a smoothing value which is too high makes the input slow.

##### Configuring the scaling of the analog output

At the analog output, a signal in the value range of -100%...100% is converted to an output signal with the corresponding current/voltage range. You specify the current/voltage range via the scaling.

1. Click the "Scaling" button to configure the scaling.

   The "Scaling analog output AO 0" dialog opens.
2. Enter the x and y values for two points of the scaling line:

   - y2:   
     Upper scaling value in percent
   - y1:   
     Lower scaling value in percent
   - x1:   
     Lower output value to be scaled.
   - x2:   
     Upper output value to be scaled.
3. Click "Close" to confirm the settings.

##### Additional functions (optional)

| Function | Description |
| --- | --- |
| Absolute-value generation | Activate the absolute-value generation in the function view if the value of the analog output is to be generated.   The activated absolute-value generation is indicated by the ![Additional functions (optional)](images/148900643851_DV_resource.Stream@PNG-de-DE.png) symbol. |
| Inversion | The signal source for inverting the analog output signals can be interconnected via a signal interconnection. Inversion is deactivated by default.   If you want to make an inversion, interconnect the signal source in the "Inversion" field (c0782). |
| Offset | Enter the offset value for the analog output in the "Offset" ([p0783](SINAMICS%20Parameter%20G220.md#p07830-analog-output-offset)) field.  The offset value is added to the output signal before the normalizing characteristic curve. |

##### Function diagrams (FD)

Analog output 0 (AO 0) - 2261 -

##### Additional parameters

---

### Setpoint channel

This section contains information on the following topics:

- [Setpoint sources and setpoint preparation](#setpoint-sources-and-setpoint-preparation)
- [Motorized potentiometer](#motorized-potentiometer)
- [Fixed setpoints](#fixed-setpoints)
- [Speed setpoint](#speed-setpoint)
- [Speed limiting](#speed-limiting)
- [Ramp-function generator](#ramp-function-generator)

#### Setpoint sources and setpoint preparation

##### Overview of the setpoint sources

The setpoint channel forms the connecting element between the external interfaces and the actual motor control. Whereby the input signals are influenced from the point of view of the driven machine, e.g. disabling a direction, hiding certain frequencies, forming acceleration and deceleration ramps through to switchover between different setpoint and command sources.

Generally, different command sources result from the requirements to operate a drive from different locations (local/remote access), in different situations (normal/emergency operation) and/or in different operating modes.

The setpoint source is therefore the interface via which the converter receives its setpoint. The following options are available:

- Motorized potentiometer emulated in the converter
- Analog input of the converter
- Fixed setpoints stored in the converter
- Fieldbus interface of the converter

Depending on the parameter assignment, the setpoint in the converter has one of the following meanings:

- Speed setpoint for the motor
- Torque setpoint for the motor
- Setpoint for a process variable

  The converter receives a setpoint for a process variable, e.g. the level of a liquid container. The converter calculates the speed setpoint internally in the technology controller from this process variable.

##### Overview of the setpoint processing

The setpoint processing modifies the speed setpoint. For example, it limits the setpoint to a maximum and a minimum value and prevents speed jumps of the motor via the ramp-function generator.

- Minimum speed and maximum speed
- Ramp-function generator

##### Function diagrams (FD)

Overview - 3001 -

#### Motorized potentiometer

This section contains information on the following topics:

- [Method of operation](#method-of-operation)
- [Configuring the motorized potentiometer](#configuring-the-motorized-potentiometer)
- [Configuring the ramp-function generator (motorized potentiometer)](#configuring-the-ramp-function-generator-motorized-potentiometer)

##### Method of operation

###### Overview

The drive emulates an electromechanical motorized potentiometer. It is possible to switch over between manual and automatic operation for the setpoint specification. The specified setpoint is supplied to an internal ramp-function generator. Setting values and start values, as well as braking with OFF1 do not require the ramp-function generator of the motorized potentiometer.

They change the motorized potentiometer (MOP) smoothly via the "Higher" and "Lower" control signals. The control signal can be switched via the digital inputs of the drive or via status words of telegrams. The longer the commands are present, the quicker the setpoint changes.

###### Application cases

- Entering the speed setpoint during the commissioning phase.
- Manual operation of the motor if the higher-level controller fails.
- Entering the speed setpoint after switching over from automatic operation to manual operation.
- Applications with mainly constant setpoint without a higher-level controller.
- Interconnection as main or additional setpoint via r1050, see also [Configuring the motorized potentiometer](#configuring-the-motorized-potentiometer).

##### Configuring the motorized potentiometer

###### Overview

The "Motorized potentiometer" function emulates an electromechanical potentiometer for the input of setpoints. The value of the motorized potentiometer is set via the "Setpoint higher" and "Setpoint lower" commands. This value is saved and can be interconnected as main setpoint or as additional setpoint. The "Motorized potentiometer" function can be selected when digital inputs of the operator panel or fieldbuses are used. The behavior of the motorized potentiometer depends on the duration of the "Setpoint higher" and "Setpoint lower" commands: The longer the commands are present, the quicker the setpoint changes.

The function is intended for manual control of the drive or for automatic speed specification. The ramp-function generator of the motorized potentiometer can be switched off in automatic operation.

- With manual control, you manually specify the setpoint via a digital input, for example.
- In automatic operation, a higher-level controller specifies the setpoint, for example. You then interconnect the signal source.

###### Requirements

- The drive has been completely created and fully specified in the device configuration.
- The [extended parameterization](#overview-2) is active.

###### Setting automatic operation or manual operation

1. Interconnect the "Manual/automatic" signal source (c1041) for switching from manual to automatic mode at the motorized potentiometer.

   In manual operation, the setpoint is set higher and lower via two signals.

   In automatic mode, the setpoint must be interconnected via a signal sink.

###### Parameterizing the motorized potentiometer for manual operation

1. To specify limit values for the speed setpoint in manual operation, enter a maximum value ([p1037](SINAMICS%20Parameter%20G220.md#p10370n-motorized-potentiometer-maximum-speed)) or minimum value ([p1038](SINAMICS%20Parameter%20G220.md#p10380n-motorized-potentiometer-minimum-speed)).

   The "Maximum speed" or "Minimum speed" is not overshot or undershot when using the motorized potentiometer.
2. Interconnect the "Setpoint raise" signal source (c1035) for a continuous increase of the setpoint at the motorized potentiometer.
3. Interconnect the "Lower setpoint" signal source (c1036) for a continuous decrease of the setpoint at the motorized potentiometer.
4. Interconnect the "Inversion" signal source (c1039) to invert the minimum speed/velocity or the maximum speed/velocity at the motorized potentiometer.
5. To parameterize the ramp-function generator, click the "Ramp-function generator" button.

   Specify the values for the ramp-function generator in the dialog of the same name (see [Configuring the ramp-function generator (motorized potentiometer)](#configuring-the-ramp-function-generator-motorized-potentiometer)).

###### Parameterizing the motorized potentiometer for the automatic mode

1. Interconnect the "Automatic setpoint" signal source (c1042) for the setpoint of the motorized potentiometer during automatic operation.
2. In the "Automatic operation active" drop-down list ([p1030](SINAMICS%20Parameter%20G220.md#p10300n04-motorized-potentiometer-configuration).1), select whether the ramp-function generator is to be active during Automatic operation.

   - [0] No = In this case, the "Ramp-function generator" button is deactivated.
   - [1] Yes = In this case, the ramp-function generator can be subsequently parameterized.
3. To parameterize the activated ramp-function generator, click the "Ramp-function generator" button.

   Specify the values for the ramp-function generator in the dialog of the same name. (See [Configuring the ramp-function generator (motorized potentiometer)](#configuring-the-ramp-function-generator-motorized-potentiometer)).

###### Saving the setpoint

The output of the motorized potentiometer [r1050](SINAMICS%20Parameter%20G220.md#r1050-motorized-potentiometer-setpoint-after-ramp-function-generator) is saved after OFF and the motorized potentiometer is set to the saved value after ON if p1030.0 = 1. The ramp-function generator of the motorized potentiometer moves from this start value in the direction of the new setpoint. With p1030.0 a decision is made as to whether the ramp-function generator of the motorized potentiometer is based on the motorized potentiometer output that was valid before the OFF command or on a start value specified by [p1040](SINAMICS%20Parameter%20G220.md#p10400n-motorized-potentiometer-starting-value). Parameter p1030.3 decides whether or not the setpoint is stored in a non-volatile memory.

For saving important data, the converter has an NVRAM (Non-Volatile Random Access Memory). The setpoint of the motorized potentiometer is stored protected against power failure there. The value is re-loaded after POWER ON and specified as the start value after OFF1 enable.

1. Select the "[1] Yes" option in the "Save active" (p1030.0) drop-down list to save the setpoint in the volatile memory (not protected against power failure).
2. Select the "[1] Yes" option in the "Non-volatile saving active" (p1030.3) drop-down list to save the setpoint in the non-volatile memory.

> **Note**
>
> Non-volatile saving is only possible when p1030.0 = 1 and p1030.3 = 1, that is, when the "[1] Yes" option is selected in both drop-down lists.

###### Result

You have configured the settings for the motorized potentiometer. Save the settings in the project.

###### Function diagrams (FD)

Motorized potentiometer - 3020 -

Control word, sequence control - 2501 -

###### Additional parameters

- [p0115](SINAMICS%20Parameter%20G220.md#p011506-sampling-times-for-internal-control-loops)
- [r1045](SINAMICS%20Parameter%20G220.md#r1045-mot-potentiometer-speed-setpoint-in-front-of-ramp-function-gen)

---

##### Configuring the ramp-function generator (motorized potentiometer)

###### Overview

The ramp-function generator (RFG) limits the acceleration at sudden setpoint changes and helps to avoid load surges in the entire drive train. An acceleration ramp and a deceleration ramp can be set independently with the ramp-up time and ramp-down time. This enables a controlled transition at setpoint changes.

In addition to the acceleration limitation, the "Ramp-function generator" function view also displays the maximum motor speed, and in which speed range the motor operates.

> **Note**
>
> If the ramp-function generator of the motorized potentiometer is used, the actual [ramp-function generator of the setpoint channel](#ramp-function-generator) is generally not used in addition.

###### Requirements

- The drive has been completely created and fully specified in the device configuration.
- The [extended parameterization](#overview-2) is active.

###### Activate initial rounding

An initial rounding results in an S-shaped ramp which provides smooth transitions for acceleration and deceleration.

1. To connect a fixed specified rounding, select the "[1] Yes" entry in the "Initial rounding active" ([p1030](SINAMICS%20Parameter%20G220.md#p10300n04-motorized-potentiometer-configuration).2) drop-down list.

   The set ramp-up or ramp-down time can be exceeded with the initial rounding.

###### Setting the ramp-up time and ramp-down time

The ramp-function generator is parameterized via the ramp-up and ramp-down time parameters, whereby these refer to the speed limit n_max.

1. Enter a value for the "Ramp-up time" ([p1047](SINAMICS%20Parameter%20G220.md#p10470n-motorized-potentiometer-ramp-up-time)).

   The lower the value, the faster the drive accelerates. The ramp-up time is extended accordingly with activated initial rounding (p1030.2).
2. Enter a value for the "Ramp-down time" ([p1048](SINAMICS%20Parameter%20G220.md#p10480n-motorized-potentiometer-ramp-down-time)).

   The lower the value, the faster the drive decelerates. The ramp-down time is extended accordingly with activated initial rounding (p1030.2).

> **Note**
>
> **Direction reversal**
>
> With direction reversal, the two times are added: With direction reversal, the ramp-down time is effective first and then the ramp-up time in the opposite direction.

###### Parameterizing the start value and the setting value

Setting values are the values to which the ramp-function generator jumps automatically. You set the ramp-function generator output to the motorized potentiometer setting value.

1. Interconnect the "Accept setting value" signal source (c1043) to accept the setting value at the motorized potentiometer.
2. Interconnect the "Setting value" (c1044) signal source for the setting value at the motorized potentiometer.

   The setting value influences [r1050](SINAMICS%20Parameter%20G220.md#r1050-motorized-potentiometer-setpoint-after-ramp-function-generator) (motorized potentiometer setpoint after ramp-function generator).
3. Enter a start value for the motorized potentiometer in the "Start value" ([p1040](SINAMICS%20Parameter%20G220.md#p10400n-motorized-potentiometer-starting-value)) field.

   The ramp-function generator of the motorized potentiometer moves from this start value in the direction of the new setpoint.

###### Result

You have configured the settings for ramp-function generator of the motorized potentiometer. Save the settings in the project.

###### Function diagrams (FD)

Control word, sequence control - 2501 -

Basic ramp-function generator - 3060 -

Extended ramp-function generator - 3070 -

Ramp-function generator selection, -status word, -tracking - 3080 -

###### Additional parameters

- [r1045](SINAMICS%20Parameter%20G220.md#r1045-mot-potentiometer-speed-setpoint-in-front-of-ramp-function-gen)
- [p1082](SINAMICS%20Parameter%20G220.md#p10820n-maximum-speed)

---

#### Fixed setpoints

This section contains information on the following topics:

- [Configure fixed setpoints](#configure-fixed-setpoints)

##### Configure fixed setpoints

###### Overview

This function allows you to specify preset speed/frequency setpoints. The fixed setpoints are defined via parameters and selected via binary signal sinks. For example, the digital inputs or the appropriate bits in the PROFINET telegrams can be used for the external control. The individual fixed setpoints and the effective fixed setpoint are each available via a numerical signal sink for further interconnection. Simple applications in which switchover is only to be between a few dedicated speeds, can be implemented with this function.

###### Requirement

- The drive has been completely created and fully specified in the device configuration.

###### Selecting fixed setpoints via direct selection

1. In the drop-down list "Fixed speed setpoint selection methods" ([p1016](SINAMICS%20Parameter%20G220.md#p1016-fixed-speed-setpoint-select-mode)), select selection method "[1] Direct".
2. Interconnect the four signal sources for setting the selection bit of the speed setpoint.

   - "Bit 0" (c1020)
   - "Bit 1" (c1021)
   - "Bit 2" (c1022)
   - "Bit 3" (c1023)
3. Interconnect the "Fixed speed setpoint selected" ([r1025](SINAMICS%20Parameter%20G220.md#r10250-fixed-speed-setpoint-status)) signal sink to display the status of the fixed speed setpoints.
4. Enter fixed speed setpoints in fields "Fixed value 1...4" ([p1001](SINAMICS%20Parameter%20G220.md#p10010n-fixed-speed-setpoint-1)...[p1004](SINAMICS%20Parameter%20G220.md#p10040n-fixed-speed-setpoint-4)).

   The effective speed setpoint then results from the addition of the individual speed setpoints according to the selection bits.
5. Click the "Interconnections" button.

   The "Fixed setpoint interconnection" dialog opens.
6. Interconnect the "Fixed value 1...4" fixed values (p1001...p1004) via the connected signal sources.
7. Once all necessary settings have been made in the dialog, click "Close".

   The dialog closes.
8. Interconnect the "Fixed value active" ([r1024](SINAMICS%20Parameter%20G220.md#r1024-fixed-speed-setpoint-effective)) signal source to display the active fixed speed setpoint.

###### Selecting fixed setpoints via binary selection

1. In the drop-down list "Fixed speed setpoint selection methods" (p1016), select selection method "[2] Binary".
2. Interconnect the four signal sources for setting the selection bit of the speed setpoint.

   - "Bit 0" (c1020)
   - "Bit 1" (c1021)
   - "Bit 2" (c1022)
   - "Bit 3" (c1023)
3. Enter fixed speed setpoints in the "Fixed value 1...15" (p1001...[p1015](SINAMICS%20Parameter%20G220.md#p10150n-fixed-speed-setpoint-15)) fields.

   The effective speed setpoint then results from the addition of the individual speed setpoints according to the selection bits.
4. Click the "Interconnections" button.

   The "Fixed setpoint interconnection" dialog opens.
5. Interconnect the "Fixed value 1...15" fixed values (p1001...p1015) via the connected signal sources.
6. Once all necessary settings have been made in the dialog, click "Close".

   The dialog closes.
7. Interconnect the "Fixed value active" (r1024) signal source to display the active fixed speed setpoint.

###### Result

You have configured the fixed setpoints. Save the settings in the project.

###### Additional parameters

- [p0115](SINAMICS%20Parameter%20G220.md#p011506-sampling-times-for-internal-control-loops)

---

#### Speed setpoint

This section contains information on the following topics:

- [Method of operation](#method-of-operation-1)
- [Configuring the speed setpoint](#configuring-the-speed-setpoint)

##### Method of operation

###### Overview

The speed setpoint is the reference variable of the drive to be controlled. You also specify the speed of the drive via the size of the speed setpoint. There are numerous ways to influence the speed setpoint:

- Main setpoint (+ scaling)
- Additional setpoint (+ scaling)
- Jog
- Direction of rotation limitation and direction reversal
- Speed limit in the setpoint channel

###### Description of function

**Additional setpoint**

The additional setpoint can be used to incorporate correction values from lower-level controllers. This can be easily carried out using the addition point of the main/additional setpoint in the setpoint channel. Both variables are imported via two separate sources and added in the setpoint channel. In contrast to the setpoint addition, the main and additional setpoints are added before the ramp-function generator. The added speed setpoint is then routed over the acceleration ramp of the ramp-function generator.

**Jog**

The jog mode is typically based on the classic " tapping" method, with which you traverse a motor by briefly tapping.

When a jog signal is connected, the motor accelerates with the acceleration ramp of the ramp-function generator (in relation to the maximum speed [p1082](SINAMICS%20Parameter%20G220.md#p10820n-maximum-speed); see figure) up to the jog setpoint. When the jog signal is deselected, shutdown is performed on the set ramp of the ramp-function generator.

![Jog 1 and Jog 2 flow diagram](images/164678126091_DV_resource.Stream@PNG-en-US.png)

Jog 1 and Jog 2 flow diagram

**Jog properties**

- If both Jog signals are set simultaneously, the momentary speed is maintained (constant speed phase).
- Jog setpoints are approached and left via the ramp-function generator.
- Jog is possible from the "Ready for switching on" state.
- If ON/OFF1 = "1" and Jog have been selected simultaneously, ON/OFF1 takes priority.  
  For this reason, ON/OFF1 = "1" must not be active for Jog to be activated.
- OFF2 and OFF3 take priority over Jog.
- The ON command is issued via c1055 and c1056.
- The Jog speed is defined via [p1058](SINAMICS%20Parameter%20G220.md#p10580n-jog-1-speed-setpoint) and [p1059](SINAMICS%20Parameter%20G220.md#p10590n-jog-2-speed-setpoint).
- The following applies during "Jog mode":

  - The main speed setpoints ([r1078](SINAMICS%20Parameter%20G220.md#r1078-total-setpoint-effective)) are disabled.
  - Additional setpoint 1 (p1155) is disabled.
  - Additional setpoint 2 (p1160) is passed on and added to the current speed.
- The skip frequency bands ([p1091](SINAMICS%20Parameter%20G220.md#p10910n-skip-speed-1) ... [p1094](SINAMICS%20Parameter%20G220.md#p10940n-skip-speed-4)) and the minimum limit ([p1080](SINAMICS%20Parameter%20G220.md#p10800n-minimum-speed)) in the setpoint channel are also effective in Jog mode.
- The freezing of the ramp-function generator via p1141 is deactivated ([r0046](SINAMICS%20Parameter%20G220.md#r0046031-missing-enable-signal).31 = 1) during Jog mode.

###### Additional parameters

---

##### Configuring the speed setpoint

###### Overview

The speed setpoint is the reference variable of the drive to be controlled. You also specify the speed of the drive via the size of the speed setpoint.

###### Requirement

- The drive has been completely created and fully specified in the device configuration.

###### Setting the main/supplementary setpoint and setpoint modification

1. Interconnect the "Main setpoint" signal source (c1070) of the main setpoint.
2. Interconnect the "Scaling" signal source (c1071) for scaling the main setpoint.

   Example: Interconnect "Fixed value 1" at "Fixed setpoint interconnection" as signal source.
3. Interconnect the "Supplementary setp" signal source (c1075) of the additional setpoint.
4. Interconnect the "Scaling" signal source (c1076) for scaling the additional setpoint.

   Example: Interconnect "Fixed value 2" at "Fixed setpoint interconnection" as signal source.

###### Setting jog

To traverse a motor via "Jog", e.g. a motor after a program interruption, enter speed setpoints in the following fields:

1. Enter a value for "Jog 1" ([p1058](SINAMICS%20Parameter%20G220.md#p10580n-jog-1-speed-setpoint)).

   - and/or -
2. Enter a value for "Jog 2" ([p1059](SINAMICS%20Parameter%20G220.md#p10590n-jog-2-speed-setpoint)).
3. Interconnect the signal sources for Jog 1 or Jog 2, and therefore enable the drive for "Jog":

   - "Jog bit 0" (c1055); signal source for Jog 1
   - "Jog bit 1" (c1056); signal source for Jog 2

   If you have connected both signal sources, the setpoint is maintained.

###### Setting the direction of rotation limitation and direction reversal

A direction reversal can be achieved in the setpoint channel by selecting the setpoint inversion (p1113). However, if the specification of a negative or positive setpoint via the setpoint channel is to be prevented, this can be disabled.

1. Interconnect the "Setpoint inversion" signal source (c1113) to set the reversal of the direction of rotation.
2. Interconnect the "Inhibit negative direction" signal source (c1110) to disable the negative direction of rotation.
3. Interconnect the "Inhibit positive direction" signal source (c1111) to disable the positive direction of rotation.

###### Setting the speed limit in the setpoint channel

To limit the speed in the setpoint channel, enter a value for the "Setpoint channel speed limit" ([p1063](SINAMICS%20Parameter%20G220.md#p10630n-setpoint-channel-speed-limit)).

###### Result

You have configured the settings for the speed setpoint. Save the settings in the project.

###### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/148900336907_DV_resource.Stream@PNG-de-DE.png) | [Speed limiting](#speed-limiting) |

###### Function diagrams (FD)

Main/additional setpoint, setpoint scaling, jog - 3030 -

Direction limitation and direction reversal - 3040 -

###### Additional parameters

- [p0115](SINAMICS%20Parameter%20G220.md#p011506-sampling-times-for-internal-control-loops)
- [r0899](SINAMICS%20Parameter%20G220.md#r0899013-status-word-sequence-control)
- [r1114](SINAMICS%20Parameter%20G220.md#r1114-setpoint-after-the-direction-limiting)
- [r1073](SINAMICS%20Parameter%20G220.md#r1073-main-setpoint-effective)
- [r1077](SINAMICS%20Parameter%20G220.md#r1077-supplementary-setpoint-effective)
- [r1078](SINAMICS%20Parameter%20G220.md#r1078-total-setpoint-effective)

---

#### Speed limiting

This section contains information on the following topics:

- [Configuring the speed limitation](#configuring-the-speed-limitation)

##### Configuring the speed limitation

###### Overview

The speed limitation is used to avoid damage to the connected machine. For example, reversing is not always possible and must be avoided. The speed setpoint limitation can disable the specification of a negative or positive setpoint via the setpoint channel. The maximum speed can also be limited for the connected machine.

In torque control, the sum of the two torque setpoints is limited in the same way as the torque setpoint of the speed control. Above the maximum speed, a speed limitation reduces the torque limits in order to prevent a further acceleration of the drive.

###### Signal source

| Symbol | Meaning |
| --- | --- |
| ![Signal source](images/148900443659_DV_resource.Stream@PNG-de-DE.PNG) | [Speed setpoint](#speed-setpoint) |

###### Requirement

- The drive has been completely created and fully specified in the device configuration.

###### Defining skip frequency bands

If a drive train has interfering points of resonance in the range from 0 rpm to the setpoint speed, you can define skip frequency bands for these points. Skip frequency bands are used, e.g. to prevent mechanical resonance effects. Resonances can cause unwanted mechanical vibrations. The skip frequency bands prevent continuous operation of the drive at these points of resonance. During ramp-up, the speed remains at the lower limit of a skip frequency band, and during ramp-down, the speed remains at the upper limit.

1. To define skip frequency bands, click the "Skip frequency bands" button.

   The "Skip frequency bands" dialog opens.
2. Enter values in the "Skip value 1 to 4" fields ([p1091](SINAMICS%20Parameter%20G220.md#p10910n-skip-speed-1) to [p1094](SINAMICS%20Parameter%20G220.md#p10940n-skip-speed-4)) in order to define up to four skip frequency bands.
3. Enter a value for the skip frequency band ([p1101](SINAMICS%20Parameter%20G220.md#p11010n-skip-speed-bandwidth)) in the "Bandwidth" field. You can only define one identical bandwidth for all four skip frequency bands.

   If you enter "0" as value, no skip frequency bands are taken into account - irrespective of which values you have defined for the "Skip values 1 to 4" (p1091 to p1094).
4. Once all necessary settings have been made, click "Close".

   The dialog closes.

   You have defined valid skip frequency bands when the "Skip frequency bands" button appears as follows:

   ![Defining skip frequency bands](images/148900328331_DV_resource.Stream@PNG-de-DE.png)

   ![Defining skip frequency bands](images/148900328331_DV_resource.Stream@PNG-de-DE.png)

###### Defining the minimum limitation

A minimum limitation is approached after the pulse enable.

1. To enter a minimum value for the speed setpoint, click the "Minimum limitation" button.

   The "Minimum limitation" dialog opens.
2. Enter a value for the lower limit of the speed setpoint at "Minimum speed" ([p1080](SINAMICS%20Parameter%20G220.md#p10800n-minimum-speed)).

   - Or -

   Interconnect the signal source "Minimum speed" (c1106) for the lowest possible speed of the motor.
3. Once all necessary settings have been made, click "Close".

   The dialog closes.

   You have defined a valid minimum limitation when the "Minimum limitation" button appears as follows:

   ![Defining the minimum limitation](images/148900469387_DV_resource.Stream@PNG-de-DE.png)

   ![Defining the minimum limitation](images/148900469387_DV_resource.Stream@PNG-de-DE.png)

###### Defining the maximum limitation

1. To enter a maximum value for the speed setpoint, click the "Maximum limitation" button.

   The "Maximum limitation" dialog opens.
2. Interconnect the speed limitations for the following directions of rotation:

   - "Speed limit positive direction of rotation" (c1051)

     This speed limitation goes directly into the ramp-function generator.
   - "Speed limit negative direction of rotation" (c1052)

     This speed limitation goes directly into the ramp-function generator.
3. Make the following settings for the "Speed limit positive effective" ([r1084](SINAMICS%20Parameter%20G220.md#r1084-positive-speed-limit-effective)) here:

   - "Pos. variable speed limit" (c1085)

     Interconnect the signal source of a variable speed limitation in the positive direction of rotation.
   - "Positive speed limit" ([p1083](SINAMICS%20Parameter%20G220.md#p10830n-speed-limit-in-positive-direction-of-rotation))

     Enter the maximum speed for the positive direction.
   - "Maximum speed" ([p1082](SINAMICS%20Parameter%20G220.md#p10820n-maximum-speed))

     Enter a value for the highest possible positive speed. The inverted value is used as the lowest possible value.

   The lowest of the three values in p1082, p1083 and p1085 is used as the "Speed limit positive effective" (r1084).
4. Make the following settings for the "Speed limit negative effective" ([p1086](SINAMICS%20Parameter%20G220.md#p10860n-speed-limit-in-negative-direction-of-rotation)) here:

   - "negative speed limit" (p1086)

     Enter the maximum speed for the positive direction.
   - "Neg. variable speed limit" (c1088)

     Interconnect the signal source of a variable speed limitation in the negative direction of rotation.

   The lowest of the three values in p1082, p1086 and p1088 is used as the "Speed limit positive effective" ([r1087](SINAMICS%20Parameter%20G220.md#r1087-negative-speed-limit-effective)).

   The setpoint of the ramp-function generator for diagnostic and control purposes is displayed in "CO: ramp-function generator setpoint at the input" ([r1119](SINAMICS%20Parameter%20G220.md#r1119-ramp-function-generator-setpoint-at-the-input)).
5. Once all necessary settings have been made, click "Close".

   The dialog closes.

###### Result

You have made the detailed settings for speed limiting. Then save the project.

###### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/148900460811_DV_resource.Stream@PNG-de-DE.png) | [Ramp-function generator](#ramp-function-generator) |

###### Function diagrams (FD)

Skip frequency bands - 3050 -

Speed limitations - 3051 -

###### Additional parameters

- [p0115](SINAMICS%20Parameter%20G220.md#p011506-sampling-times-for-internal-control-loops)
- [r1112](SINAMICS%20Parameter%20G220.md#r1112-speed-setpoint-after-minimum-limiting)
- [r1114](SINAMICS%20Parameter%20G220.md#r1114-setpoint-after-the-direction-limiting)

---

#### Ramp-function generator

This section contains information on the following topics:

- [Configuring the ramp-function generator](#configuring-the-ramp-function-generator)
- [Configuring the basic ramp-function generator](#configuring-the-basic-ramp-function-generator)
- [Configuring the extended ramp-function generator](#configuring-the-extended-ramp-function-generator)

##### Configuring the ramp-function generator

###### Overview

The ramp-function generator is used to limit the acceleration if the setpoint changes suddenly. The setting of the ramp-function generator parameters depends on your application and the construction of your machine.

- [Basic ramp-function generator](#configuring-the-basic-ramp-function-generator)

  The basic ramp-function generator passes on the input values to the output via linear ramps. The speed setpoint is accelerated or decelerated linearly.
- [Extended ramp-function generator](#configuring-the-extended-ramp-function-generator)

  With the extended ramp-function generator, acceleration and deceleration are not linear. Rounding can be parameterized at the start and end of the range via a selected rounding type.

> **Note**
>
> **Presetting via the guided quick startup**
>
> The ramp-function generator type that is used can be pre-selected via the quick startup step "[Connection to PLC](#connection-to-plc)".

An acceleration ramp and a deceleration ramp can be set independently with the ramp-up time and ramp-down time. This enables a controlled transition at setpoint changes.

If the drive is in the range of the torque limits or the drive is temporarily not controlled via the ramp-function generator, then the actual speed value moves away from the speed setpoint.

With ramp-function generator tracking, the speed setpoint follows the actual speed value and therefore flattens the ramp. The ramp-function generator tracking can be activated for the basic and the extended ramp-function generator.

> **Note**
>
> If a [Motorized potentiometer with ramp-function generator](#configuring-the-ramp-function-generator-motorized-potentiometer) is used in the setpoint channel, the ramp-function generator described below is usually superfluous.

###### Signal source

| Symbol | Meaning |
| --- | --- |
| ![Signal source](images/148900336907_DV_resource.Stream@PNG-de-DE.png) | [Speed limitation](#speed-limiting) |

###### Requirement

- The drive has been completely created and fully specified in the device configuration.

###### Making the basic settings for the ramp-function generator

1. Select in the "Ramp-function generator selection" drop-down list whether a basic ramp-function generator or an extended ramp-function generator is to be used.

   The ramp-function generator type is shown as subentry in the secondary navigation:
2. In the "Enable setpoint" field (c1142), interconnect the signal source to enable the frequency setpoint.
3. Interconnect the signal source to start the ramp-function generator in the "Continue ramp-function generator" (c1141) field.
4. Click the "Ramp-function generator" button or select the appropriate function view via the secondary navigation.
5. Make the additional settings for the selected ramp-function generator type.

   - [Basic ramp-function generator](#configuring-the-basic-ramp-function-generator)
   - [Extended ramp-function generator](#configuring-the-extended-ramp-function-generator)
6. Interconnect the signal source in the "Enable ramp-function generator" (c1140) field to enable the ramp-function generator.
7. Save the settings.

###### Required enables

Various enables are required to operate the ramp-function generator.

- "OFF1 enable" and "OFF3 enable" are set via the control word "Sequential control system".

  The control inputs of the ramp-function generator take effect as follows:

  - 1st priority: OFF3
  - 2nd priority: Ramp-function generator enable
  - 3rd priority: Ramp-function generator start
  - 4th priority: Setpoint enable

The following internal enables are required ([r0046](SINAMICS%20Parameter%20G220.md#r0046031-missing-enable-signal)):

- "OFF1 enable internal missing" (r0046[16])

  Shows whether a fault response is present at OFF1. The enable is made only when the fault has been corrected and acknowledged, and the switching on disabled removed with OFF1 = 0.
- "OFF3 enable internal missing" (r0046[18])

  Shows whether an OFF3 has not yet been completed or an OFF3 fault response is present.
- "STOP2 enable internal missing" (r0046[18])

  Shows whether a STOP2 fault response is present.
- "Operation enable missing" (r0046[3])

  Shows that the signal source in p0852 is a 0 signal.

###### Result

The ramp-function generator only becomes active when the settings described above have been made and the enables according to the logical operations are present.

###### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/148900537739_DV_resource.Stream@PNG-de-DE.png) | [Setpoint addition](#setpoint-addition) |

###### Function diagrams (FD)

Basic ramp-function generator - 3060 -

Extended ramp-function generator - 3070 -

Ramp-function generator selection, -status word, -tracking - 3080 -

###### Additional parameters

- [p0115](SINAMICS%20Parameter%20G220.md#p011506-sampling-times-for-internal-control-loops)
- [r1119](SINAMICS%20Parameter%20G220.md#r1119-ramp-function-generator-setpoint-at-the-input)
- [r1150](SINAMICS%20Parameter%20G220.md#r1150-ramp-function-generator-speed-setpoint-at-the-output)
- [r1198](SINAMICS%20Parameter%20G220.md#r1198015-control-word-setpoint-channel)

---

##### Configuring the basic ramp-function generator

###### Overview

With the basic ramp-function generator, the input values are passed on to the output via linear ramps, i.e. there is no rounding at the start and end of the range; the drive is accelerated or decelerated linearly.

![Basic ramp-function generator](images/148900904459_DV_resource.Stream@PNG-en-US.png)

Basic ramp-function generator

###### Signal source

| Symbol | Meaning |
| --- | --- |
| ![Signal source](images/148900460811_DV_resource.Stream@PNG-de-DE.png) | [Ramp-function generator](#configuring-the-ramp-function-generator) |

###### Requirements

- The drive has been completely created and fully specified in the device configuration.
- The [extended parameterization](#overview-2) is active.

  The standard parameterization only allows some of the settings described below.

###### Setting the ramp-up time and ramp-down time

You parameterize the ramp-function generator via the ramp-up and ramp-down times, whereby these refer to the speed limit n<sub>max</sub>.

1. Correct the specified ramp-up time ([p1047](SINAMICS%20Parameter%20G220.md#p10470n-motorized-potentiometer-ramp-up-time)) from standstill to maximum speed.
2. Interconnect the signal source for scaling the ramp-up time of the ramp-function generator in the "Scaling" (c1138) field.
3. Correct the specified ramp-down time ([p1048](SINAMICS%20Parameter%20G220.md#p10480n-motorized-potentiometer-ramp-down-time)) from maximum speed to standstill.
4. Interconnect the signal source for scaling the ramp-down time of the ramp-function generator in the "Scaling" (c1139) field.
5. Correct the value specified for the ramp-down time (OFF) ([p1135](SINAMICS%20Parameter%20G220.md#p11350n-off3-ramp-down-time)).

   The ramp-down time (OFF) is the ramp-down time that may elapse from maximum speed down to standstill for the OFF3 command.

###### Setting the setting value

Setting values are the values to which the ramp-function generator jumps automatically.

| Symbol | Meaning |
| --- | --- |
| 1. Interconnect the signal source to accept the setting value in the "Accept setting value" (c1143) field.     The ramp-function generator behaves as follows depending on the values of parameter c1143:       | Symbol | Meaning |    | --- | --- |    | 0/1 signal | The output of the ramp-function generator is set to the setting value of the ramp-function generator without delay. |    | 1 signal | The setting value of the ramp-function generator takes effect. |    | 1/0 signal | The input value of the ramp-function generator takes effect. The output of the ramp-function generator is adapted to the input value via the ramp-up time or the ramp-down time. |    | 0 signal | The input value of the ramp-function generator takes effect. | 2. Interconnect the signal source for the setting value on the ramp-function generator in the "Setting value" (c1144) field. |  |

###### Result

The detailed settings for the basic ramp-function generator have been made. Then save the project with the current settings.

###### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/148900460811_DV_resource.Stream@PNG-de-DE.png) | [Ramp-function generator](#configuring-the-ramp-function-generator) |

###### Function diagrams (FD)

Basic ramp-function generator - 3060 -

###### Additional parameters

- [p1082](SINAMICS%20Parameter%20G220.md#p10820n-maximum-speed)

---

##### Configuring the extended ramp-function generator

###### Overview

With the extended ramp-function generator, acceleration and deceleration are not linear. The acceleration can be described by a ramp for a set rounding. Without rounding, the acceleration jumps to the value specified by the ramp-up or ramp-down time.

![Extended ramp-function generator](images/148900917259_DV_resource.Stream@PNG-en-US.png)

Extended ramp-function generator

The "Effective ramp-up/ramp-down time" is calculated according to the following formula:

- Effective ramp-up time = ramp-up time + initial rounding/2 + final rounding/2
- Effective ramp-down time = ramp-down time + initial rounding/2 + final rounding/2

###### Signal source

| Symbol | Meaning |
| --- | --- |
| ![Signal source](images/148900460811_DV_resource.Stream@PNG-de-DE.png) | [Ramp-function generator](#configuring-the-ramp-function-generator) |

###### Requirements

- The drive has been completely created and fully specified in the device configuration.
- The [extended parameterization](#overview-2) is active.

  The standard parameterization only allows some of the settings described below.

###### Entering rounding parameters

1. Enter a value for the "Initial rounding 1" or 2 ([p1130](SINAMICS%20Parameter%20G220.md#p11300n-ramp-function-generator-initial-rounding-off-time)).

   The value applies for ramp-up and ramp-down.
2. Enter a value for the "Final rounding 1" or 2 ([p1131](SINAMICS%20Parameter%20G220.md#p11310n-ramp-function-generator-final-rounding-off-time)).

   The value applies for ramp-up and ramp-down.

###### Setting the ramp-up time and ramp-down time

The ramp-function generator is parameterized via the ramp-up and ramp-down times, whereby these refer to the speed limit n<sub>max</sub>.

1. Correct the specified ramp-up time ([p1047](SINAMICS%20Parameter%20G220.md#p10470n-motorized-potentiometer-ramp-up-time)) from standstill to maximum speed.
2. Interconnect the signal source for scaling the ramp-up time of the ramp-function generator in the "Scaling" (c1138) field.
3. Correct the specified ramp-down time ([p1048](SINAMICS%20Parameter%20G220.md#p10480n-motorized-potentiometer-ramp-down-time)) from maximum speed to standstill.
4. Interconnect the signal source for scaling the ramp-down time of the ramp-function generator in the "Scaling" (c1139) field.
5. Select the "[1] Yes" setting in the "Enable rounding at the zero crossover" drop-down list to enable the rounding at the zero crossover.

###### Setting the setting value

Setting values are the values to which the ramp-function generator jumps automatically. You set the ramp-function generator output to the ramp-function generator setting value.

| Symbol | Meaning |
| --- | --- |
| 1. Interconnect the signal source to accept the setting value in the "Accept setting value" (c1143) field.     The ramp-function generator behaves as follows depending on the values of parameter c1143:       | Symbol | Meaning |    | --- | --- |    | 0/1 signal | The output of the ramp-function generator is set to the setting value of the ramp-function generator without delay. |    | 1 signal | The setting value of the ramp-function generator takes effect. |    | 1/0 signal | The input value of the ramp-function generator takes effect. The output of the ramp-function generator is adapted to the input value via the ramp-up time or the ramp-down time. |    | 0 signal | The input value of the ramp-function generator takes effect. | 2. Interconnect the signal source for the setting value on the ramp-function generator in the "Setting value" (c1144) field. |  |

###### Setting OFF3-relevant parameters

When an OFF3 occurs, the drive is braked along the OFF3 deceleration ramp.

1. To specify a rounding type, select one of the following options from the drop-down list:

   - "Continuous smoothing" (p1134 = 0)

     With this setting the rounding is always active. When setpoint changes occur, they only take effect after the final rounding has been completed. This can result in overshoot.
   - "Discontinuous smoothing" (p1134 = 1)

     A change in the setpoint causes a final rounding to be canceled. This prevents an overshoot. However, this can result in abrupt changes of the velocity/acceleration (jerk).
2. Correct the value specified for the "ramp-down time (OFF)" ([p1135](SINAMICS%20Parameter%20G220.md#p11350n-off3-ramp-down-time)).

   The value describes the ramp-down time from maximum speed to standstill with OFF3.
3. Enter a value for the "OFF3 initial rounding time" ([p1136](SINAMICS%20Parameter%20G220.md#p11360n-off3-initial-rounding-off-time)).
4. Enter a value for the "OFF3 final rounding time" ([p1137](SINAMICS%20Parameter%20G220.md#p11370n-off3-final-rounding-off-time)).

###### Result

The detailed settings for the extended ramp-function generator have been made. Then save the project with the current settings.

###### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/148900460811_DV_resource.Stream@PNG-de-DE.png) | [Ramp-function generator](#configuring-the-ramp-function-generator) |

###### Function diagrams (FD)

Extended ramp-function generator - 3070 -

###### Additional parameters

- [p1082](SINAMICS%20Parameter%20G220.md#p10820n-maximum-speed)

---

### Drive control

This section contains information on the following topics:

- [Setpoint addition](#setpoint-addition)
- [Speed setpoint filter](#speed-setpoint-filter)
- [Speed controller](#speed-controller)
- [Standard Drive Control](#standard-drive-control)
- [U/f control](#uf-control)
- [Torque setpoints](#torque-setpoints)
- [Torque limitation](#torque-limitation)
- [Current setpoint filter](#current-setpoint-filter)
- [Flux setpoint](#flux-setpoint)
- [Current controller](#current-controller)
- [Power unit](#power-unit)
- [Motor](#motor)
- [Motor encoder](#motor-encoder)

#### Setpoint addition

This section contains information on the following topics:

- [Configuring setpoint addition](#configuring-setpoint-addition)
- [Configuring droop feedback](#configuring-droop-feedback)

##### Configuring setpoint addition

###### Overview

The setpoint addition optionally adds two additional speed setpoints to the main setpoint, which is specified by the ramp-function generator.

An interpolator causes a finer grading of the speed setpoints from the ramp-function generator by calculating intermediate steps (interpolation). An interpolator can be used for the respective speed setpoints 1 and 2, and for the speed setpoint at the output of the ramp-function generator.

###### Signal source

| Symbol | Meaning |
| --- | --- |
| ![Signal source](images/148900460811_DV_resource.Stream@PNG-de-DE.png) | [Ramp-function generator](#ramp-function-generator) |
| ![Signal source](images/148900477963_DV_resource.Stream@PNG-de-DE.png) | [Torque limitation](#torque-limitation)   For source for droop feedback: "[1] Droop from the torque setpoint" |
| ![Signal source](images/148898416523_DV_resource.Stream@PNG-de-DE.PNG) | [Torque setpoints](#torque-setpoints)   For source for droop feedback: "[2] Droop from the speed controller output" |
| ![Signal source](images/148900435083_DV_resource.Stream@PNG-de-DE.png) | [Speed controller](#speed-controller)   For source for droop feedback: "[3] Droop from the integral output speed controller" |

###### Requirements

- The drive has been completely created and fully specified in the device configuration.
- The "Speed control" or "Torque control" control type is activated with the option "Select other control type" (see [Operating mode](#operating-mode-1)).

  The "Dynamic Drive Control (DDC)" or "Standard Drive Control" (SDC) operating modes cannot be activated.

  Otherwise the settings for the droop feedback are missing from the function view.
- The [extended parameterization](#overview-2) is active.

###### Procedure

1. In the "Droop source" ([p1488](SINAMICS%20Parameter%20G220.md#p14880n-droop-input-selection)) drop-down list, select from where the value is to be taken for the droop feedback:

   - "[0] Droop feedback not connected"
   - "[1] Droop from the torque setpoint"
   - "[2] Droop from the torque control output"
   - "[3] Droop from the integral output, speed controller"
2. Interconnect the "Speed setpoint 1" (c1155) signal source for speed setpoint 1 of the speed controller.
3. Interconnect the "Speed setpoint 2" (c1160) signal source for speed setpoint 2 of the speed controller.

   "Speed setpoint 1" and "Speed setpoint 2" are added to the speed setpoint after the ramp-function generator.
4. Select the interpolators if required:

   - In the drop-down list below the top button "Interpolation", select the option "[1] Yes" ([p1189](SINAMICS%20Parameter%20G220.md#p11890n01-speed-setpoint-configuration).1) to activate the interpolator for speed setpoints 1 and 2.
   - In the drop-down list below the lower button "Interpolation", select the option "[1] Yes" (p1189.0) to activate the interpolator for the speed setpoint from the ramp-function generator.
5. If you have activated a droop feedback (droop source [1] ... [3]), you now parameterize the droop feedback (see [Droop feedback](#configuring-droop-feedback)).

###### Result

You have configured the setpoint addition. Save the settings in the project.

###### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/148900452235_DV_resource.Stream@PNG-de-DE.png) | [Speed setpoint filter](#speed-setpoint-filter) |

###### Function diagrams (FD)

Speed setpoint, droop - 6030 -

###### Additional parameters

- [p0115](SINAMICS%20Parameter%20G220.md#p011506-sampling-times-for-internal-control-loops)
- [r0898](SINAMICS%20Parameter%20G220.md#r0898014-control-word-sequence-control)
- [r1150](SINAMICS%20Parameter%20G220.md#r1150-ramp-function-generator-speed-setpoint-at-the-output)
- [r1169](SINAMICS%20Parameter%20G220.md#r1169-speed-controller-speed-setpoints-1-and-2)
- [r1170](SINAMICS%20Parameter%20G220.md#r1170-speed-controller-setpoint-sum)

---

##### Configuring droop feedback

###### Overview

A droop (enabled via c1492) causes the speed setpoint to be reduced proportionally as the load torque increases.

![Speed controller with droop](images/164668724875_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Active only when the precontrol has been activated ([p1496](SINAMICS%20Parameter%20G220.md#p14960n-acceleration-precontrol-scaling) > 0) |
| ② | Active only for SLVC |

Speed controller with droop

The droop has a torque limiting effect on a drive that is mechanically coupled to a different speed (e.g. roller for a web guidance). In connection with the torque setpoint of a leading speed-controlled drive, a very effective load distribution can also be implemented. With the appropriate setting (in contrast to torque control or load distribution with overload and limitation), this load distribution controls even a smooth mechanical coupling or the case of slipping.

> **Note**
>
> Do not use this method for drives that are accelerated or braked with significant changes in speed.

To satisfy the above requirement, droop feedback is often deployed. For example, in applications in which two or more motors are coupled mechanically or operate with a common shaft. It limits the torque differences that can occur as a result of the mechanical coupling by appropriately modifying the speeds of the individual motors. The drive is relieved when the torque is too large.

###### Requirements

- The drive has been completely created and fully specified in the device configuration.
- The "Speed control" or "Torque control" control type is activated with the option "Select other control type" (see [Operating mode](#operating-mode-1)).

  The "Dynamic Drive Control (DDC)" or "Standard Drive Control" (SDC) operating modes cannot be activated.

  Otherwise the settings for the droop feedback are missing from the function view.
- A common ramp-function generator for the mechanically coupled drives.
- The [extended parameterization](#overview-2) is active.

###### Procedure

1. Click the "Droop feedback" button in the "Setpoint addition" function view.

   A dialog with the same name opens.
2. Interconnect the signal source for the compensation torque within the droop calculation in the "Droop torque 2" (c1486) field.
3. Correct the specified value for scaling the compensation torque within the droop calculation in the "Droop scaling torque 2" ([p1487](SINAMICS%20Parameter%20G220.md#p14870n-droop-compensation-torque-scaling)) field.
4. Interconnect the signal source to enable the droop to be applied to the speed/velocity setpoint in the "Droop feedback enable" (c1492) field.
5. Correct the specified value for scaling the droop feedback in the "Droop scaling" ([p1489](SINAMICS%20Parameter%20G220.md#p14890n-droop-feedback-scaling)) field.
6. Once all necessary settings have been made, click "Close".

###### Result

The dialog closes. Save the settings in the project.

###### Function diagrams (FD)

Speed setpoint, droop - 6030 -

###### Additional parameters

- [r0079](SINAMICS%20Parameter%20G220.md#r0079-torque-setpoint)
- [r1482](SINAMICS%20Parameter%20G220.md#r1482-speed-controller-i-torque-output)
- [p1488](SINAMICS%20Parameter%20G220.md#p14880n-droop-input-selection)
- [r1490](SINAMICS%20Parameter%20G220.md#r1490-droop-feedback-speed-reduction)
- [r1508](SINAMICS%20Parameter%20G220.md#r1508-torque-setpoint-before-supplementary-torque)

---

#### Speed setpoint filter

This section contains information on the following topics:

- [Configuring the speed setpoint filter](#configuring-the-speed-setpoint-filter)
- [Configuring the maximum limit](#configuring-the-maximum-limit)
- [Configuring the acceleration precontrol](#configuring-the-acceleration-precontrol)
- [Configuring pre-control balancing](#configuring-pre-control-balancing)

##### Configuring the speed setpoint filter

###### Overview

The speed setpoint filter contains the acceleration precontrol, the speed setpoint limiting, and the precontrol balancing.

The speed precontrol and the acceleration precontrol are processed using an acceleration model. The acceleration is calculated from the speed difference over the time "dn/dt". You can parameterize settings for the acceleration precontrol torque in the "[Precontrol](#configuring-the-acceleration-precontrol)" dialog. A limiter ensures that the acceleration torque cannot become excessively high. Over the further course, an integration element ensures that the acceleration is converted back to a speed and is applied to the speed setpoint as a value for the speed precontrol.

The signal paths depend on the following settings:

- Acceleration precontrol signal source ([p1400](SINAMICS%20Parameter%20G220.md#p14000n031-speed-control-configuration).2):

  - [0] Internal (n_set)

    The main signal comes from the setpoint addition and is modified via the acceleration model (precontrol).
  - [1] External (r1495)

    An external signal is interconnected for the acceleration precontrol. The value comes from a higher-level control, for example.
- Reference model (p1400.3):

  - [0] Off

    The signal runs directly from the setpoint addition into the speed controller. The acceleration model plays no role in this scenario.
  - [1] On

    The signal runs through the acceleration model.

###### Requirements

- The drive has been completely created and fully specified in the device configuration.
- The "Dynamic Drive Control (DDC)" operating mode is activated.

  - Or -

  The "Speed control" or "Torque control" control type is activated (see [Operating mode](#operating-mode-1)).
- The [extended parameterization](#overview-2) is active.

###### Signal source

| Symbol | Meaning |
| --- | --- |
| ![Signal source](images/148900537739_DV_resource.Stream@PNG-de-DE.png) | [Setpoint addition](#setpoint-addition) |

###### Set speed setpoint with acceleration precontrol from external signal source

1. Select the "[1] External (p1495)" signal source in the "Acceleration precontrol signal source" (p1400.2) drop-down list.

   The circuit diagram is updated according to this setting.
2. If you want to use an acceleration model, activate the "Acceleration model (with speed encoder)" (p1400) option.
3. Interconnect the signal source for the acceleration precontrol in the "Acceleration precontrol" (c1495) field.
4. Click the "Precontrol acceleration" button and record the values for the precontrol in the "[Precontrol](#configuring-the-acceleration-precontrol)" dialog.
5. Correct the value specified for scaling the acceleration precontrol ([p1496](SINAMICS%20Parameter%20G220.md#p14960n-acceleration-precontrol-scaling)) in the field below the "Precontrol acceleration" button.

   Via this evaluation factor, you can adapt the acceleration precontrol depending on the application.
6. Then make the settings for the precontrol balancing using the [Precontrol balancing](#configuring-pre-control-balancing) dialog.

###### Set speed setpoint from "Setpoint addition" without acceleration model

1. Select the "[0] Internal (n_set)" or "[1] External (p1495)" signal source in the "Acceleration precontrol signal source" (p1400.2) drop-down list.

   The circuit diagram is updated according to this setting. With the "External" setting, you can also parameterize the precontrol balancing.
2. If you do not want to use an acceleration model, deactivate the "Acceleration model (with speed encoder)" (p1400) option.

   In this way, you define that the input value of the "Precontrol balancing" comes from the "setpoint addition".
3. Click the "Speed setpoint limited" button and record the values for the maximum limit of the speed setpoint in the "[Maximum limitation](#configuring-the-maximum-limit)" dialog.
4. Enter a value for the time constant in the "Smoothing" field ([p1416](SINAMICS%20Parameter%20G220.md#p14160n-speed-setpoint-filter-1-time-constant)).

   The speed setpoint is given to the "Precontrol balancing" delayed by the time constant (PT1 behavior).
5. If you set an external signal source (see 1.), you can make the settings for [precontrol balancing](#configuring-pre-control-balancing).

###### Set speed setpoint from "Setpoint addition" with acceleration model

1. Select the "[0] Internal (n_set)" signal source in the "Acceleration precontrol signal source" (p1400.2) drop-down list.

   The circuit diagram is updated according to this setting.
2. If you want to use an acceleration model, activate the "Acceleration model (with speed encoder)" (p1400) option.
3. Click the "Speed setpoint limited" button and record the values for the maximum limit of the speed setpoint in the "[Maximum limitation](#configuring-the-maximum-limit)" dialog.
4. Enter a value for the time constant in the "Smoothing" field (p1416).

   The speed setpoint is given at the output, delayed by the time constant (PT1 behavior).
5. Click the "Precontrol acceleration" button and record the values for the Dn/Dt precontrol in the "[Precontrol](#configuring-the-acceleration-precontrol)" dialog.
6. Enter a value for the scaling of the acceleration precontrol (p1496) in the field below the "Precontrol acceleration" button.

   Via this evaluation factor, you can adapt the acceleration precontrol depending on the application.

###### Result

You have configured the speed setpoint filter. Save the settings in the project.

###### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/148898416523_DV_resource.Stream@PNG-de-DE.PNG) | [Torque setpoints](#torque-setpoints) |
| ![Signal processing](images/148900435083_DV_resource.Stream@PNG-de-DE.png) | [Speed controller](#speed-controller) |

###### Function diagrams (FD)

Speed setpoint, droop - 6030 -

Precontrol symmetrization, acceleration model - 6031 -

###### Additional parameters

- [r0062](SINAMICS%20Parameter%20G220.md#r0062-speed-setpoint-after-the-filter)
- [r0115](SINAMICS%20Parameter%20G220.md#p011506-sampling-times-for-internal-control-loops)
- [r1438](SINAMICS%20Parameter%20G220.md#r1438-speed-controller-speed-setpoint)

---

##### Configuring the maximum limit

###### Overview

You limit the speed setpoint via a maximum speed. This is the maximum speed value the motor should have. A change of this value has an effect on the controller and ramp-function generator settings. There are other limitation variants, i.e. an individual fixed limit can be specified for the negative and the positive direction of rotation.

The value "n max" (maximum speed) always has priority.

> **Note**
>
> **Changing the maximum speed**
>
> Changing the maximum speed [p1082](SINAMICS%20Parameter%20G220.md#p10820n-maximum-speed) has an effect on the following functions:
>
> - Ramp-down (OFF3)
> - Ramp-function generator
> - Motorized potentiometer

###### Requirements

- The drive has been completely created and fully specified in the device configuration.
- The "Dynamic Drive Control (DDC)" operating mode is activated.

  - Or -

  The "Speed control" or "Torque control" mode is activated (see [Operating mode](#operating-mode-1)).
- The [extended parameterization](#overview-2) is active.

###### Procedure

1. Click the "Speed setpoint limited" button.

   The "Maximum limitation" dialog opens.
2. Interconnect the signal source for speed limitation in the positive direction of rotation in the "Pos. variable speed limit" (c1085) field.
3. Correct the value specified for limitation of the positive speed setpoint in the "Positive speed limit" ([p1083](SINAMICS%20Parameter%20G220.md#p10830n-speed-limit-in-positive-direction-of-rotation)) field.
4. Correct the value specified for the maximum speed in the "Maximum speed" (p1082) field.
5. Correct the value specified for limitation of the negative speed setpoint in the "Negative speed limit" ([p1086](SINAMICS%20Parameter%20G220.md#p10860n-speed-limit-in-negative-direction-of-rotation)) field.
6. Interconnect the signal source for speed limitation in the negative direction of rotation in the "Neg. variable speed limit" (c1088) field.
7. Once all necessary settings have been made, click "Close".

###### Result

The dialog closes. Save the settings in the project.

###### Function diagrams (FD)

Speed setpoint, droop - 6030 -

###### Additional parameters

- [r1084](SINAMICS%20Parameter%20G220.md#r1084-positive-speed-limit-effective)
- [r1087](SINAMICS%20Parameter%20G220.md#r1087-negative-speed-limit-effective)

---

##### Configuring the acceleration precontrol

###### Overview

The command behavior of the speed control loop is improved when the acceleration torque is calculated from the speed setpoint and the speed controller is series-connected.

The motor moment of inertia [p0341](SINAMICS%20Parameter%20G220.md#p03410n-motor-moment-of-inertia) is calculated directly during commissioning or when the entire set of parameters is calculated (p0340 = 1). You determine the factor [p0342](SINAMICS%20Parameter%20G220.md#p03420n-ratio-between-the-total-and-motor-moment-of-inertia) between the total moment of inertia J and the motor moment of inertia manually or via the speed controller optimization. The acceleration is calculated from the speed difference over time dn/dt.

###### Requirements

- The drive has been completely created and fully specified in the device configuration.
- The "Dynamic Drive Control (DDC)" operating mode is activated.

  - Or -

  The "Speed control" or "Torque control" mode is activated (see [Operating mode](#operating-mode-1)).
- The [extended parameterization](#overview-2) is active.

###### Procedure

1. Click the "Acceleration precontrol" button.

   The "Precontrol" dialog opens.
2. Interconnect the signal source for scaling the moment of inertia in the "Scaling of moment of inertia" field (c1497).
3. Correct the value specified for scaling the acceleration precontrol in [%] in the "Precontrol acceleration" field ([p1496](SINAMICS%20Parameter%20G220.md#p14960n-acceleration-precontrol-scaling)).
4. Correct the value specified for the motor moment of inertia in the "Motor moment of inertia" (p0341) field.
5. Correct the value specified for the ratio between the total moment of inertia/mass (load + motor) and the solitary motor moment of inertia/mass (without load) in the "Ratio moment of inertia/motor" (p0342) field.

   The rated startup time of the motor is calculated from p0342 and p0341.
6. If you want to consider the values from the moment of inertia estimator for the precontrol, activate the "Moment of inertia estimator" option ([p1400](SINAMICS%20Parameter%20G220.md#p14000n031-speed-control-configuration)[0].18).

   The following parameters from the moment of inertia estimator are then displayed and can be corrected for the precontrol:

   - Threshold, accelerating torque ([p1560](SINAMICS%20Parameter%20G220.md#p15600n-moment-of-inertia-estimator-accelerating-torque-threshold-value))
   - Smoothing, motor moment of inertia ([p1561](SINAMICS%20Parameter%20G220.md#p15610n-moment-of-inertia-estimator-change-time-moment-of-inertia))
   - Smoothing, load moment of inertia ([p1562](SINAMICS%20Parameter%20G220.md#p15620n-moment-of-inertia-estimator-change-time-load))

   If required, correct the specified parameter values.
7. If the determined moment of inertia estimator is to be obtained for a pulse inhibit, activate the option of the same name.
8. Once all necessary settings have been made, click "Close".

###### Result

The dialog closes. The acceleration precontrol is displayed as a percentage in the "Speed setpoint filter" function view (p1496).

###### Function diagrams (FD)

Precontrol symmetrization, acceleration model - 6031 -

Speed controller - 6040 -

###### Additional parameters

- [r0056](SINAMICS%20Parameter%20G220.md#r0056015-status-word-closed-loop-control)
- [r1493](SINAMICS%20Parameter%20G220.md#r1493-moment-of-inertia-total-scaled)

---

##### Configuring pre-control balancing

###### Overview

In order that the speed controller does not counteract the applied torque setpoint, you must parameterize the precontrol balancing. The precontrol balancing serves to prevent unwanted controller motions until the precontrol is activated. The precontrol balancing is implemented as a PT1 element.

###### Requirements

- The drive has been completely created and fully specified in the device configuration.
- The [extended parameterization](#overview-2) is active.
- The precontrol balancing becomes active only when P gain [p1460](SINAMICS%20Parameter%20G220.md#p14600n-speed-controller-p-gain) > 0% is set and the reference model is deactivated.

###### Procedure

1. Click the "Precontrol balancing" button in the "Speed setpoint filter" function view.

   An input dialog with the same name opens.
2. In the "Dead time factor" field ([p1428](SINAMICS%20Parameter%20G220.md#p14280n-speed-precontrol-symmetrizing-dead-time)), enter the dead time for the balancing of the speed setpoint with active torque precontrol.

   With active torque precontrol, the speed precontrol must be delayed until the torque precontrol has acted, and the new actual speed value is available. The "new" setpoint should not arrive until the current actual value of the speed controller is known. If torque precontrol is not possible (e.g. the moment of inertia J of the drive is not known), the speed precontrol value does not need to be delayed.
3. In the "Smoothing" field ([p1429](SINAMICS%20Parameter%20G220.md#p14290n-speed-precontrol-symmetrizing-time-constant)), enter the time constant (PT1) for the balancing of the speed setpoint with active torque precontrol.

   The time constant specifies the course of the signal rise. You specify the rate of increase of the speed setpoint with this time constant.
4. Close the dialog box.

###### Result

p1428 and p1429 together emulate the runtime behavior of the torque development (dynamics of the closed current control loop).

###### Function diagrams (FD)

Precontrol symmetrization, acceleration model - 6031 -

###### Additional parameters

---

#### Speed controller

This section contains information on the following topics:

- [Configuring the speed controller](#configuring-the-speed-controller)
- [Configuring the Kp/Tn adaptation](#configuring-the-kptn-adaptation)
- [Configuring the integrator control](#configuring-the-integrator-control)

##### Configuring the speed controller

###### Overview

In the "Speed controller" function view, specify the parameters of the speed controller.

- The P gain K<sub>p</sub> and the integral time T<sub>n</sub> of the lower adaptation speed of the speed controller will be displayed.
- The smoothing for the actual speed value can be entered.

Using the adaptation, enables a switchable parameterization of the K<sub>p</sub> (P gain) value for two different speeds (upper and lower adaptation speed). It is hence easier to overcome friction forces, for example, if during startup a higher K<sub>p</sub> is selected and then switched over.

Use the PI controller to amplify the controller difference between the setpoint (from the speed setpoint filter) and the actual speed value.

###### Requirements

- The drive has been completely created and fully specified in the device configuration.
- The "Dynamic Drive Control (DDC)" operating mode is activated.

  - Or -

  The "Speed control" or "Torque control" mode is activated (see [Operating mode](#operating-mode-1)).
- The [extended parameterization](#overview-2) is active.

###### Signal source

| Symbol | Meaning |
| --- | --- |
| ![Signal source](images/148900452235_DV_resource.Stream@PNG-de-DE.png) | [Speed setpoint filter](#speed-setpoint-filter) |

###### Procedure

If necessary, you can change the set control mode on this function view again.

1. Select the control type in the "Control type" ([p1300](SINAMICS%20Parameter%20G220.md#p13000n-open-loopclosed-loop-control-type)) drop-down list:

   - [20] Speed control (encoderless)  
     With this control mode, an automatic Kp/Tn adaptation can also be optionally activated.
   - [21] Speed control (with encoder)
   - [22] Speed control (encoderless)  
     For this control mode, an automatic Kp/Tn adaptation can also be optionally activated.
   - [23] Torque control (with encoder)
2. Correct the P gain before the adaptation speed range specified in the "P gain" ([p1470](SINAMICS%20Parameter%20G220.md#p14700n-speed-controller-encoderless-operation-p-gain)) field.
3. Correct the integral time before the adaptation speed range specified in the "Integral time" ([p1472](SINAMICS%20Parameter%20G220.md#p14720n-speed-controller-encoderless-operation-integral-time)) field.
4. Click the "Smoothing" button and interconnect the signal source for the actual speed value of the speed controller (c1440) in the "Actual speed value filter" dialog.
5. In the "Smoothing" field ([p1452](SINAMICS%20Parameter%20G220.md#p14520n-speed-controller-speed-actual-value-smoothing-time-sensorless)), enter the smoothing time for the actual speed value of the speed controller for speed control with encoder.
6. Specify the values for the Kp/Tn adaptation (see [Configuring the Kp/Tn adaptation](#configuring-the-kptn-adaptation)).
7. Specify the controller parameters for the I component of the PI controller via the "Integrator control" (see [Configuring the integrator control](#configuring-the-integrator-control)).

###### Result

You have configured the speed controller. Save the settings in the project.

###### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/148898416523_DV_resource.Stream@PNG-de-DE.PNG) | [Torque setpoints](#torque-setpoints) |
| ![Signal processing](images/148900537739_DV_resource.Stream@PNG-de-DE.png) | [Setpoint addition](#setpoint-addition) |

###### Function diagrams (FD)

Closed-loop speed control and generation of the torque limits, overview - 6020 -

Kp_n/Tn_n adaptation - 6050 -

###### Additional parameters

- [r0062](SINAMICS%20Parameter%20G220.md#r0062-speed-setpoint-after-the-filter)
- [r0063](SINAMICS%20Parameter%20G220.md#r006302-speed-actual-value)
- [r0064](SINAMICS%20Parameter%20G220.md#r0064-speed-controller-system-deviation)
- [p0115](SINAMICS%20Parameter%20G220.md#p011506-sampling-times-for-internal-control-loops)
- [r1436](SINAMICS%20Parameter%20G220.md#r1436-speed-controller-reference-model-speed-setpoint-output)
- [r1438](SINAMICS%20Parameter%20G220.md#r1438-speed-controller-speed-setpoint)
- [r1443](SINAMICS%20Parameter%20G220.md#r1443-speed-controller-speed-actual-value-at-actual-value-input)
- [r1445](SINAMICS%20Parameter%20G220.md#r1445-speed-controller-actual-speed-smoothed)
- [r1454](SINAMICS%20Parameter%20G220.md#r1454-speed-controller-system-deviation-i-component)
- [r1468](SINAMICS%20Parameter%20G220.md#r1468-speed-controller-p-gain-effective)
- [r1469](SINAMICS%20Parameter%20G220.md#r1469-speed-controller-integral-time-effective)
- [r1480](SINAMICS%20Parameter%20G220.md#r1480-speed-controller-pi-torque-output)
- [r1481](SINAMICS%20Parameter%20G220.md#r1481-speed-controller-p-torque-output)
- [r1482](SINAMICS%20Parameter%20G220.md#r1482-speed-controller-i-torque-output)

---

##### Configuring the Kp/Tn adaptation

###### Overview

The K<sub>p</sub>/T<sub>n</sub> adaptation enables a completely variable proportional gain K<sub>p</sub>. A linear adaptation characteristic can be defined by specifying two characteristic interpolation points.

###### Requirements

- The drive has been completely created and fully specified in the device configuration.
- A speed control or torque control is activated as control mode (see [Operating mode](#operating-mode-1)).
- The [extended parameterization](#overview-2) is active.

###### Procedure

1. Select the "[1] Yes" option ([p1400](SINAMICS%20Parameter%20G220.md#p14000n031-speed-control-configuration).5) in the drop-down list below the "Adaptation" button.

   The K<sub>p</sub>/T<sub>n</sub> adaptation is activated and can be parameterized. No adaptation parameters can be specified without this activation.
2. Click the "Adaptation" button next to the input field of the p gain.

   The "K<sub>p</sub>/T<sub>n</sub> adaptation" function view is displayed.
3. Interconnect the signal source for scaling the P gain of the velocity controller in the "Scaling" (c1466) field.
4. Interconnect the signal source for the adaptation signal for the additional adaptation of the P gain of the speed controller in the "Adaptation signal" (c1455) field.
5. Click the "Adaptation" button.

   A dialog with the same name is displayed.
6. Enter the percentage values for the following adaptation parameters:

   - "Adaptation factor upper" ([p1459](SINAMICS%20Parameter%20G220.md#p14590n-adaptation-factor-upper))

     Adaptation range (> [p1457](SINAMICS%20Parameter%20G220.md#p14570n-speed-controller-p-gain-adaptation-upper-starting-point)) to additionally adapt the P gain of the speed/velocity controller.
   - "Adaptation factor lower" ([p1458](SINAMICS%20Parameter%20G220.md#p14580n-adaptation-factor-lower))

     Adaptation range (0% ... [p1456](SINAMICS%20Parameter%20G220.md#p14560n-speed-controller-p-gain-adaptation-lower-starting-point)) to additionally adapt the P gain of the speed/velocity controller.
   - "Lower application point" (p1456)

     Lower application point of the adaptation range for the additional adaptation of the P gain of the speed controller.
   - "Upper application point" (p1457)

     Upper application point of the adaptation range for the additional adaptation of the P gain of the speed controller.
7. Once all necessary settings have been made, click "Close".

   The dialog closes.
8. Enter the percentage values for the following parameters:

   - "Scaling Kp" ([p1461](SINAMICS%20Parameter%20G220.md#p14610n-speed-controller-kp-adaptation-speed-upper-scaling))

     P gain of the speed controller for the upper adaptation speed range (> [p1465](SINAMICS%20Parameter%20G220.md#p14650n-speed-controller-adaptation-speed-upper)).
   - "Scaling Tn" ([p1463](SINAMICS%20Parameter%20G220.md#p14630n-speed-controller-tn-adaptation-speed-upper-scaling))

     Integral time of the speed controller after the adaptation speed range (> p1465).
9. Enter the desired speed in the "Upper adaptation speed" (p1465) field.
10. Enter the desired speed in the "Lower adaptation speed" ([p1464](SINAMICS%20Parameter%20G220.md#p14640n-speed-controller-adaptation-speed-lower)) field.
11. If you want to optimize the T<sub>n</sub> component of the speed-dependent adaptation, select the "[1] Yes" option in the "Free T<sub>n</sub> adaptation active" drop-down list (p1400.6).

    The T<sub>n</sub> value of the speed-dependent adaptation is divided by the factor of the free adaptation.

###### Result

You have configured the K<sub>p</sub>/T<sub>n</sub> adaptation for the variable proportional gain K<sub>p</sub>.

###### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/148900435083_DV_resource.Stream@PNG-de-DE.png) | [Speed controller](#configuring-the-speed-controller) |

###### Function diagrams (FD)

Speed controller - 6040 -

Kp_n/Tn_n adaptation - 6050 -

###### Additional parameters

- [r0063](SINAMICS%20Parameter%20G220.md#r006302-speed-actual-value)
- [r1468](SINAMICS%20Parameter%20G220.md#r1468-speed-controller-p-gain-effective)
- [r1469](SINAMICS%20Parameter%20G220.md#r1469-speed-controller-integral-time-effective)
- [p1470](SINAMICS%20Parameter%20G220.md#p14700n-speed-controller-encoderless-operation-p-gain)
- [p1472](SINAMICS%20Parameter%20G220.md#p14720n-speed-controller-encoderless-operation-integral-time)

---

##### Configuring the integrator control

###### Overview

You specify the parameters used to control the I-component of the PI controller in the "Integrator control" dialog.

If you set a value in "Integrator feedback", the integrator of the speed/velocity controller is reparameterized to become a PT1 filter through a feedback element (1st order low-pass filter characteristic). For an application example, see p1494.

For cases where the control goes into saturation because, for example, a limit is exceeded (e.g. suspended load), the I-component increases rapidly. If the fault disappears, the excessively high I-component must first be slowly reduced (windup).

With "Hold integrator", you shut down the integrator when the limit is exceeded (saturation) and specify a setting value when switching on the final controlling element for the I component, e.g. via "Set integrator value".

###### Requirements

- The drive has been completely created and fully specified in the device configuration.
- A speed control or torque control is activated as control type (see [Operating mode](#operating-mode-1)).
- The [extended parameterization](#overview-2) is active.

###### Procedure

1. Click the "Integrator control" button in the "Speed controller" function view.

   The dialog with the same name opens.
2. If required, interconnect the following signal sources:

   - "Speed controller enabled" (c0856) for the "Enable speed controller" command ([r0898](SINAMICS%20Parameter%20G220.md#r0898014-control-word-sequence-control).12).
   - "Hold integrator" (c1476) for holding the integrator (speed control with encoder, torque control with encoder).
   - "Setting value for motor holding brake" (c1475) for the torque setting value when starting with motor holding brake.
   - "Set integrator value" (c1477) for setting the integrator setting value.
   - "Integrator setting value" (c1478) from which the integrator setting value is to be read.
   - "Setting value scaling" (c1479) for scaling the integrator setting value (p1478) of the speed controller.
3. Once all necessary settings have been made, click "Close".

###### Result

The dialog closes. The settings are applied to the "Speed controller" function view.

###### Terminology for the use of linear motors

When linear motors are used, a linear motion is executed instead of a rotary motion. The terms change accordingly:

- Speed corresponds to velocity
- Torque corresponds to force

###### Function diagrams (FD)

Speed controller - 6040 -

###### Additional parameters

- [r1468](SINAMICS%20Parameter%20G220.md#r1468-speed-controller-p-gain-effective)
- [r1469](SINAMICS%20Parameter%20G220.md#r1469-speed-controller-integral-time-effective)
- [r1480](SINAMICS%20Parameter%20G220.md#r1480-speed-controller-pi-torque-output)
- [r1481](SINAMICS%20Parameter%20G220.md#r1481-speed-controller-p-torque-output)
- [r1482](SINAMICS%20Parameter%20G220.md#r1482-speed-controller-i-torque-output)

---

#### Standard Drive Control

This section contains information on the following topics:

- [Configuring Standard Drive Control](#configuring-standard-drive-control)
- [Configuring the current and power limitation](#configuring-the-current-and-power-limitation)
- [Configuring the SDR characteristic](#configuring-the-sdr-characteristic)
- [Configuring magnetization control](#configuring-magnetization-control)

##### Configuring Standard Drive Control

###### Overview

Standard Drive Control is the simplest operating mode. With this operating mode, the stator voltage for the induction motor is controlled proportionately to the stator frequency. This method has proved successful in a wide range of applications with low dynamic requirements (see [Areas of application and parameters of the operating modes](#operating-mode-1))

###### Signal sources

| Symbol | Meaning |
| --- | --- |
| ![Signal sources](images/148900537739_DV_resource.Stream@PNG-de-DE.png) | [Setpoint addition](#setpoint-addition) |

###### Requirements

- The drive has been completely created and fully specified in the device configuration.
- An induction motor is used.
- The "Standard Drive Control (SDC)" operating mode is set in the basic parameterization (see [Operating mode](#operating-mode-1)).
- The [extended parameterization](#overview-2) is active.

  In the standard parameterization, some of the settings described below are not visible.

###### Procedure

1. Correct the value specified for the current limit in the "Current limit motor current" ([p0640](SINAMICS%20Parameter%20G220.md#p06400n-motor-current-limit)) field.
2. In the "Slip compensation" ([p1793](SINAMICS%20Parameter%20G220.md#p17930n-slip-compensation-scaling-sdc)) field, correct the slip compensation amount for induction motors.

   This slip compensation keeps the motor speed constant irrespective of the load. With synchronous motors, this setting has no effect.
3. Correct the resonance damping setting in the "Resonance damping" field ([p1740](SINAMICS%20Parameter%20G220.md#p17400n-gain-resonance-damping-for-encoderless-closed-loop-control)).
4. Check the settings for the current and power limit and correct the preset values if necessary (see [Configuring the current and power limit](#configuring-the-current-and-power-limitation)).
5. Check the settings for the SDC characteristic and, if necessary, correct the preset values (see "[Configuring the SDR characteristic](#configuring-the-sdr-characteristic)").
6. Configure the magnetization curve (see [Magnetization control](#configuring-magnetization-control)).
7. If you use a motor holding brake, connect the signal source "Setting value motor holding brake" (r1475) for the torque setting value when starting with motor holding brake.

   This setting is only available if the motor holding brake is activated.

###### Result

You have configured the settings for the SDC operating mode. Save the settings in the project.

###### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/148879237771_DV_resource.Stream@PNG-de-DE.png) | [Power unit](#power-unit) |
| ![Signal processing](images/148879237771_DV_resource.Stream@PNG-de-DE.png) | [Power unit](#power-unit) |

###### Function diagrams (FD)

Overview - 6850 -

Characteristic and voltage boost - 6851 -

Current/power/torque limits - 6852 -

###### Additional parameters

---

##### Configuring the current and power limitation

###### Overview

A machine sets a counter-torque or load torque against the torque of the drive.

In order to avoid overloads of the machine particularly during acceleration and deceleration phases, the torque of the drive must be limited according to the connected machine.

You can set the following limits for current and power limitation:

- Torque limit upper

  Permits the upper torque value to be specified and, if necessary, be scaled.
- Current limit motor current

  Permits the actual current limit to be viewed. Because the current limiting also limits the maximum torque that the motor can provide, if the torque limit is increased, more torque will only be available if a higher current can also flow. It may be necessary to also adapt the current limit.
- Power limit motoring

  Permits the current motorized and regenerative power limit to be viewed. The value specifies the maximum permissible power, whereby different limits can be viewed for motorized and regenerative mode.
- Torque limit lower

  Permits the lower torque value to be specified and, if necessary, be scaled.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Danger to life due to uncontrolled movement of the drive as a result of incorrect parameter assignment**   Incorrect parameter assignment of the torque limits can result in uncontrolled movement of the drives if there is no counter-torque, and cause death or serious injury.  - Make sure that the parameter assignment is correct. |  |

###### Requirements

- The drive has been completely created and fully specified in the device configuration.
- An induction motor is used.
- The "Standard Drive Control (SDC)" operating mode is set in the basic parameterization (see [Operating mode](#operating-mode-1)).
- The [extended parameterization](#overview-2) is active.

  In the standard parameterization, some of the settings described below are not visible.

###### Configuring the current limitation

The current limit can be configured alternatively or in addition to the torque limiting. If only the current limit is configured (without the torque limit), the drive ramps up quickly. However, as only the ramp-function generator is stopped when the current limit is reached, the current can continue to rise. This must be taken into account during the parameterization (if required, through a safety clearance) so that the drive is not switched off with an overcurrent error.

1. In the "Standard Drive Control" function view, click the "Current limit" button.

   The "Current limitation" view is displayed.
2. Enter the fixed upper torque limit in the "Torque limit upper" ([p1520](SINAMICS%20Parameter%20G220.md#p15200n-torque-limit-upper)[0]) field.
3. If necessary, correct the values for the "Motor current limit" ([p0640](SINAMICS%20Parameter%20G220.md#p06400n-motor-current-limit)[0]) here.
4. Correct the scaling of the current limit if necessary.

   - Click the "Current limit" button.
   - In the "Current limit" dialog, interconnect the "Scaling" signal source (c0641[0]) for scaling the current limit.
   - Once all necessary settings have been made, click "Close".
5. If necessary, correct the values for "Power limit motoring" ([p1530](SINAMICS%20Parameter%20G220.md#p15300n-power-limit-motoring)[0]) here.
6. Enter the fixed lower torque limit in the "Torque limit lower" ([p1521](SINAMICS%20Parameter%20G220.md#p15210n-torque-limit-lower)[0]) field.

###### Configuring the power limit

The power limit can be configured alternatively or additionally to the current limit.

1. Click the "Power limit" button in the "Current limitation" function view.

   A dialog with the same name opens.
2. In the "Power limit motorized" field (p1530[0]), enter the motorized power limit.
3. In the "Power limit scaling" field ([p1556](SINAMICS%20Parameter%20G220.md#p15560n-power-limit-scaling)[0]), enter the scaling of the signal source for the motorized and negative regenerative power limit.
4. In the "Power limit" field (c1555[0]), interconnect the signal source for the motorized and negative regenerative power limit.
5. In the "Power limit regenerative" field ([p1531](SINAMICS%20Parameter%20G220.md#p15310n-power-limit-regenerative)[0]), enter the regenerative power limit.
6. Once all necessary settings have been made, click "Close".

   The dialog closes.

###### Result

You have configured the current and power limits. Save the settings in the project.

###### Additional parameters

---

##### Configuring the SDR characteristic

###### Overview

The SDC characteristic compensates for voltage losses in the stator resistance for static/dynamic loads.

This is particularly useful for small motors, since they have a relatively high stator resistance.

![Overview](images/148901134859_DV_resource.Stream@PNG-en-US.png)

###### Requirements

- The drive has been completely created and fully specified in the device configuration.
- An induction motor is used.
- The "Standard Drive Control (SDC)" operating mode is set in the basic parameterization (see [Operating mode](#operating-mode-1)).
- The [extended parameterization](#overview-2) is active.

  In the standard parameterization, some of the settings described below are not visible.

###### Procedure

1. In the "Standard Drive Control" function view, click the "SDR characteristic" button.

   The function view of the same name is displayed.
2. If required, correct the preset values in the "SDC characteristic" function view.

   - Static torque setpoint ([p1610](SINAMICS%20Parameter%20G220.md#p16100n-starting-torque-static-without-encoder))
   - Additional acceleration torque ([p1611](SINAMICS%20Parameter%20G220.md#p16110n-acceleration-starting-torque-encoderless))

   Both values refer to the rated motor torque ([r0333](SINAMICS%20Parameter%20G220.md#r03330n-rated-motor-torque)).
3. Click the "Voltage boost" button to additionally configure a voltage boost.

   A dialog with the same name opens.
4. Correct the specified percentage of a permanent voltage boost in the "Permanent starting current" ([p1310](SINAMICS%20Parameter%20G220.md#p13100n-starting-current-voltage-boost-permanent)) field.
5. Enter a value for an optional voltage boost for ramp-up in the "Starting current when accelerating" ([p1311](SINAMICS%20Parameter%20G220.md#p13110n-starting-current-voltage-boost-when-accelerating)) field.

   The voltage boost follows a positive setpoint increase and is removed when the setpoint is reached.
6. Once all necessary settings have been made, click "Close".

   The dialog closes.

###### Result

You have configured the SDR characteristic. Save the settings in the project.

###### Function diagrams (FD)

Characteristic and voltage boost - 6851 -

###### Additional parameters

---

##### Configuring magnetization control

###### Overview

For crane applications, frequently a frequency converter is switched alternately to different motors. After being switched to a different motor, a new dataset must be loaded in the frequency converter and the motor magnetized. This can result in excessive waiting times that could be reduced by magnetization, if required.

The magnetization can be parameterized via a separate dialog in the "Standard Drive Control" function view. The most important setting is the selection of the correct magnetization curve.

| Magnetization | Parameterization | Curve |
| --- | --- | --- |
| Standard | [p1401](SINAMICS%20Parameter%20G220.md#p14010n030-flux-control-configuration).0 = 0, p1401.6 = 0 | ![Overview](images/148900635531_DV_resource.Stream@PNG-de-DE.png) |
| Quick magnetization | p1401.6 = 1 | ![Overview](images/148900614411_DV_resource.Stream@PNG-de-DE.png) |
| Soft starting | p1401.0 = 1 | ![Overview](images/148900580491_DV_resource.Stream@PNG-de-DE.png) |

**Features**

- Quick flux build-up through injection of a field-generating current at the current limit,  
  resulting in a significant reduction in magnetization time.
- When quick magnetization is selected (p1401.6 = 1), soft starting is deactivated internally and alarm A07416 displayed.
- The "flying restart" function continues working with parameter [p0346](SINAMICS%20Parameter%20G220.md#p03460n-motor-excitation-build-up-time) (magnetization time).
- If the "flying restart" function is active (see [p1200](SINAMICS%20Parameter%20G220.md#p12000n-flying-restart-operating-mode)), no quick magnetization is performed.
- If stator resistance identification is activated, quick magnetization is deactivated internally and alarm A07416 displayed.

###### Requirements

- The drive has been completely created and fully specified in the device configuration.
- An induction motor is used.
- The "Standard Drive Control (SDC)" operating mode is set in the basic parameterization (see [Operating mode](#operating-mode-1)).
- The [extended parameterization](#overview-2) is active.

###### Procedure

1. Click the "Magnetization control" button in the "Standard Drive Control" function view.  
   A dialog with the same name opens.
2. In order to parameterize a magnetization of the induction motor with an initial low rise, activate the "Flux setpoint soft starting active" (p1401.0 = 1) option.
3. To activate the quick magnetization, activate the "Quick magnetizing" (p1401.6 = 1) option.
4. Correct the value for the flux threshold of the magnetization in the "Flux threshold value magnetizing" ([p1573](SINAMICS%20Parameter%20G220.md#p15730n-flux-threshold-value-magnetizing)) field.
5. Enter a value for the motor excitation build-up time in the "Motor excitation build-up time" (p0346) field.
6. Once all necessary settings have been made, click "Close".

###### Result

The dialog closes. Save the settings in the project.

###### Additional parameters

---

#### U/f control

This section contains information on the following topics:

- [Configuring U/f control](#configuring-uf-control)
- [Configuring the U/f characteristic](#configuring-the-uf-characteristic)
- [Configuring the voltage boost of the U/f characteristic](#configuring-the-voltage-boost-of-the-uf-characteristic)
- [Configuring the I_max controller](#configuring-the-i_max-controller)
- [Configuring slip compensation](#configuring-slip-compensation)
- [Configuring resonance damping](#configuring-resonance-damping)

##### Configuring U/f control

###### Overview

The simplest solution for a control procedure is the U/f characteristic. Whereby the stator voltage for the induction motor or synchronous motor is controlled proportionately to the stator frequency. This method has proved successful in a wide range of applications with low dynamic requirements, such as:

- Pumps and fans,
- Belt drives

###### Signal sources

| Symbol | Meaning |
| --- | --- |
| ![Signal sources](images/148900537739_DV_resource.Stream@PNG-de-DE.png) | [Setpoint addition](#setpoint-addition) |

###### Requirements

- The drive has been completely created and fully specified in the device configuration.
- A "U/f control ..." is set as the control mode In the basic parameterization (see [Operating mode](#operating-mode-1)).
- The [extended parameterization](#overview-2) is active.

  In the standard parameterization, some of the settings described below are not visible and configurable.

###### Procedure

1. If required, select another U/f control mode in the "Control mode" drop-down list.

   The appearance of the function view changes accordingly.
2. If the motor voltage should be increased continually during the magnetization phase, select the "[1] On" option in the "Soft starting" ([p1350](SINAMICS%20Parameter%20G220.md#p13500n-uf-control-soft-start)) drop-down list.

   Otherwise, the voltage jumps immediately to voltage boost.
3. Check the settings for the U/f characteristic and, if necessary, correct the preset values (see "[Configuring the U/f characteristic](#configuring-the-uf-characteristic)").
4. If you require a voltage limiting controller, make the necessary settings via the I_max controller (see "[Configuring the I_max controller](#configuring-the-i_max-controller)").
5. Correct the value specified for the current limit in the "Current limit" ([p0640](SINAMICS%20Parameter%20G220.md#p06400n-motor-current-limit)) field.

   This value originates from the settings of the I_max controller.
6. Correct the specified value to limit the voltage setpoint in the "Voltage limit" ([p1331](SINAMICS%20Parameter%20G220.md#p13310n-voltage-limiting)) field.
7. If you require slip compensation, make the necessary settings for it (see "[Configuring slip compensation](#configuring-slip-compensation)").
8. If you experience excessive resonance effects, make the necessary settings for resonance damping (see "[Configuring resonance damping](#configuring-resonance-damping)").

###### Result

You have configured U/f control. Save the settings in the project.

###### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/148879237771_DV_resource.Stream@PNG-de-DE.png) | [Power unit](#power-unit) |
| ![Signal processing](images/148879237771_DV_resource.Stream@PNG-de-DE.png) | [Power unit](#power-unit) |

###### Function diagrams (FD)

U/f control, overview - 6300 -

###### Additional parameters

---

##### Configuring the U/f characteristic

###### Overview

At low output frequencies, the U/f characteristics supply only a low output voltage. Along with the influence of the ohmic resistance at low frequencies, this can result in a too low output voltage. To counteract this, a voltage boost can be set. This can achieve the following:

- Implement the magnetization of the induction motor
- Maintain the load
- Compensate for the losses (ohmic losses in the winding resistors) in the system
- Generate a breakaway/acceleration/braking torque

###### Principle of operation of the U/f characteristics

| U/f control type | Application/property |  |
| --- | --- | --- |
| [0] U/f control with linear characteristic | Standard case (without voltage boost) | ![Principle of operation of the U/f characteristics](images/148901083659_DV_resource.Stream@PNG-en-US.png) |
| [1] U/f control with linear characteristic and FCC | Characteristic compensates for voltage losses in the stator resistance for static/dynamic loads (Flux Current Control FCC).  This is particularly useful for small motors, since they have a relatively high stator resistance. | ![Principle of operation of the U/f characteristics](images/148901134859_DV_resource.Stream@PNG-en-US.png) |
| [2] U/f control with parabolic characteristic | Characteristic takes into account the motor torque curve (e.g. fan/pump):  - Quadratic characteristic (f<sup>2</sup> characteristic) - Energy saving because the low voltage also results in low currents and losses | ![Principle of operation of the U/f characteristics](images/148901147659_DV_resource.Stream@PNG-en-US.png) |
| [3] U/f control with parameterizable characteristic | Characteristic takes into account the motor/machine torque curve. | ![Principle of operation of the U/f characteristics](images/148901160459_DV_resource.Stream@PNG-en-US.png) |
| [4] U/f control with linear characteristic and ECO | Characteristic, see parameter 0 and ECO mode at a constant operating point.   - In the ECO mode, the efficiency at a constant operating point is optimized. This optimization is effective only in stationary operation and when the ramp-function generator is not bypassed. - The scaling of the slip compensation ([p1335](SINAMICS%20Parameter%20G220.md#p13350n-slip-compensation-scaling)) must be parameterized so that the slip is completely compensated (generally, 100%). |  |
| [5] U/f control for a drive that requires a precise frequency (textile sector) | Characteristic takes into account the special technological features of the application:  - The current limitation (I_max controller) affects only the output voltage, not the output frequency. - Disable slip compensation |  |
| [6] U/f control for drive requiring a precise frequency and FCC | Characteristic takes into account the special technological features of the application:  - The current limitation (I_max controller) affects only the output voltage, not the output frequency. - Disable slip compensation   Voltage losses in the stator resistance for static/dynamic loads are also compensated (Flux Current Control FCC). This function is required for small motors, because unlike large motors, they have a relatively high stator resistance. |  |
| [7] U/f control for parabolic characteristic and ECO | Characteristic, see parameter 1 and ECO mode at a constant operating point.  - In the ECO mode, the efficiency at a constant operating point is optimized. This optimization is effective only in stationary operation and when the ramp-function generator is not bypassed. - The scaling of the slip compensation (p1335) must be parameterized so that the slip is completely compensated (generally, 100%). |  |
| [19] U/f control with independent voltage setpoint | The user can set the parameter p1330 via the interfaces to specify the output voltage of the Motor Module independent of the frequency. |  |

###### Requirements

- The drive has been completely created and fully specified in the device configuration.
- A "U/f control ..." is set as the control mode In the basic parameterization (see [Operating mode](#operating-mode-1)).
- The [extended parameterization](#overview-2) is active.

  A voltage boost cannot be set in the standard parameterization.

###### Procedure

1. In the "U/f control" function view, click the "U/f characteristic" button.
2. If necessary, correct the preset values in the "U/f characteristic" function view.
3. Correct also the defaults for any voltage boost (see "[Configuring the voltage boost of the U/f characteristic](#configuring-the-voltage-boost-of-the-uf-characteristic)").

###### Result

The U/f characteristic of the set control type is configured. Save the settings in the project.

###### Function diagrams (FD)

U/f control, voltage boost - 6301 -

U/f control, voltage characteristics - 6302 -

###### Additional parameters

---

##### Configuring the voltage boost of the U/f characteristic

###### Overview

At low output frequencies, the U/f characteristics supply only a low output voltage. The ohmic resistance of the stator winding is significant at low frequencies. They are, however, ignored when determining the motor magnetic flux for the U/f control. Consequently, the output voltage can be too low for various motor states. The following reasons can make a voltage boost necessary:

- Magnetization build-up of an induction motor at n = 0 rpm
- Torque build-up at n = 0 rpm, e.g. in order to hold a load
- Generation of a breakaway, acceleration or braking torque
- Compensation of ohmic losses in the windings and feeder cables

For this reason, you can specify the various voltage boosts for the U/f characteristic:

| Boost type | Representation |
| --- | --- |
| Permanent starting current ([p1310](SINAMICS%20Parameter%20G220.md#p13100n-starting-current-voltage-boost-permanent)) | ![Permanent voltage boost (example: p1300 = 0 and p1310 > 0)](images/148900968459_DV_resource.Stream@PNG-en-US.png)   Permanent voltage boost (example: [p1300](SINAMICS%20Parameter%20G220.md#p13000n-open-loopclosed-loop-control-type) = 0 and p1310 > 0) |
| Starting current when accelerating ([p1311](SINAMICS%20Parameter%20G220.md#p13110n-starting-current-voltage-boost-when-accelerating)) | ![Voltage boost during acceleration (example: p1300 = 0 and p1311 > 0)](images/148900955659_DV_resource.Stream@PNG-en-US.png)   Voltage boost during acceleration (example: p1300 = 0 and p1311 > 0) |
| Starting current at startup ([p1312](SINAMICS%20Parameter%20G220.md#p13120n-starting-current-voltage-boost-when-starting)) | - |

> **Note**
>
> The voltage boost affects all U/f characteristics (p1300).

> **Note**
>
> **Excessive motor temperature rise as a result of excessive voltage boost**
>
> If the voltage boost value is too high, this can result in an excessively high motor winding temperature increase - and therefore result in a shutdown (trip).

The desired voltage boost can be configured via a subsequent dialog in the "U/f characteristic" function view.

###### Requirements

- The drive has been completely created and fully specified in the device configuration.
- A "U/f control ..." is set as the control mode In the basic parameterization (see [Operating mode](#operating-mode-1)).
- The [extended parameterization](#overview-2) is active.

###### Procedure

1. Click the "Voltage boost" button in the "U/f characteristic" function view.

   A dialog with the same name opens.
2. Correct the specified rated current of the motor in the "Rated current" ([p0305](SINAMICS%20Parameter%20G220.md#p03050n-rated-motor-current)) field.
3. Correct the specified percentage of a permanent voltage boost in the "Permanent starting current" (p1310) field.
4. Enter a value for an optional voltage boost for ramp-up in the "Starting current when accelerating" (p1311) field.

   The voltage boost follows a positive setpoint increase and is removed when the setpoint is reached.
5. Enter a value for an optional voltage boost for the 1st acceleration operation in the "Starting current during startup" (p1312) field.
6. Once all necessary settings have been made, click "Close".

###### Result

The dialog closes. The "U/f characteristic" function view shows the currently set values for the permanent voltage boost and the voltage boost for acceleration. Save the settings in the project.

###### Function diagrams (FD)

U/f control, voltage boost - 6301 -

###### Additional parameters

---

##### Configuring the I_max controller

###### Overview

To avoid overloads during motorized operation, the converter has a current limitation controller (I_max controller) in the "U/f characteristic" operating mode.

An I_max controller protects the converter and motor against continuous overload. The converter output frequency and the converter output voltage are reduced by f<sub>Imax</sub> ([r1343](SINAMICS%20Parameter%20G220.md#r1343-i_max-controller-frequency-output)) and V<sub>Imax</sub> ([r1344](SINAMICS%20Parameter%20G220.md#r1344-i_max-controller-voltage-output)), respectively. This reduction reduces loading on the converter. You can configure the I_max controller via a separate dialog.

###### Requirement

- The [extended parameterization](#overview-2) is active.

###### Procedure

1. Click the "I_max controller" button in the "U/f control" function view.

   A dialog with the same name opens.
2. Correct the specified integral time of the I_max voltage controller in the "Integral time" ([p1346](SINAMICS%20Parameter%20G220.md#p13460n-i_max-voltage-controller-integral-time)) field.
3. Enter the proportional gain of the I_max voltage controller in the "P gain" ([p1345](SINAMICS%20Parameter%20G220.md#p13450n-i_max-voltage-controller-proportional-gain)) field.
4. Correct the value specified for the current limit in the "Current limit" ([p0640](SINAMICS%20Parameter%20G220.md#p06400n-motor-current-limit)) field.
5. Interconnect the signal source for scaling the current limit in the "Scaling" (c0641) field.
6. Correct the specified integral time of the I_max frequency controller in the "Integral time" ([p1341](SINAMICS%20Parameter%20G220.md#p13410n-i_max-frequency-controller-integral-time)) field.
7. Enter the proportional gain of the I_max frequency controller in the "P gain" ([p1340](SINAMICS%20Parameter%20G220.md#p13400n-i_max-frequency-controller-proportional-gain)) field.
8. Once all necessary settings have been made, click "Close".

###### Result

The dialog closes. Save the settings in the project.

###### Function diagrams (FD)

U/f control, overview - 6300 -

###### Additional parameters

---

##### Configuring slip compensation

###### Overview

The slip compensation ensures that the motor speed is kept constant irrespective of the load. Reduction of the motor speed with increasing load is a typical feature of induction motors. You can configure the desired slip compensation via a dialog of the "U/f control" function view.

###### Requirements

- The drive has been completely created and fully specified in the device configuration.
- An induction motor is used.
- The following control modes are **not** used:

  - U/f control for drives requiring a precise frequency
  - U/f control for drives requiring a precise frequency and FCC
- The [extended parameterization](#overview-2) is active.

###### Procedure

1. Click the "Slip compensation" button in the "U/f control" function view.

   A dialog with the same name opens.
2. Enter the percentage setpoint of the slip compensation in relation to the rated motor slip in the "Scaling" ([p1335](SINAMICS%20Parameter%20G220.md#p13350n-slip-compensation-scaling)) field.

   For the slip compensation to become active, a scaling > 0% must be entered.
3. Correct the specified percentage limitation of the slip compensation in relation to the rated motor slip in the "Limit value" ([p1336](SINAMICS%20Parameter%20G220.md#p13360n-slip-compensation-limit-value)) field.
4. Once all necessary settings have been made, click "Close".

###### Result

The dialog closes. The set scaling is displayed on the "U/f control" function view. Save the settings in the project.

###### Function diagrams

U/f control, slip compensation - 6311 -

###### Additional parameters

---

##### Configuring resonance damping

###### Overview

Resonance effects increase the noise level and can also damage or destroy the mechanical system. The resonance damping function dampens active current oscillations that can occur under no-load conditions. The resonance damping is active in a range between 5% and 90% of the rated motor frequency ([p0310](SINAMICS%20Parameter%20G220.md#p03100n-rated-motor-frequency)); however, up to a maximum of 45 Hz. You can configure the desired resonance damping via a dialog.

###### Requirements

- The drive has been completely created and fully specified in the device configuration.
- A "U/f control ..." is set as the control mode In the basic parameterization (see [Operating mode](#operating-mode-1)).
- The [extended parameterization](#overview-2) is active.

###### Procedure

1. Click the "Resonance damping" button in the "U/f control" function view.

   A dialog with the same name opens.
2. Enter a gain value for resonance damping for U/f control in the "Gain" ([p1338](SINAMICS%20Parameter%20G220.md#p13380n-uf-mode-resonance-damping-gain)) field.
3. Correct the specified maximum output frequency for resonance damping for U/f operation in the "Maximum frequency" ([p1349](SINAMICS%20Parameter%20G220.md#p13490n-uf-mode-resonance-damping-maximum-frequency)) field.
4. Correct the filter time constant specified for the resonance damping for U/f control in the "Smoothing" ([p1339](SINAMICS%20Parameter%20G220.md#p13390n-uf-mode-resonance-damping-filter-time-constant)) field.
5. Once all necessary settings have been made, click "Close".

###### Result

The dialog closes. The set gain is displayed on the "U/f control" function view. Save the settings in the project.

###### Function diagrams

U/f control, resonance damping - 6310 -

###### Additional parameters

---

#### Torque setpoints

This section contains information on the following topics:

- [Configuring the torque setpoint](#configuring-the-torque-setpoint)

##### Configuring the torque setpoint

###### Overview

You edit the torque setpoint by scaling or by applying an additional setpoint. The supplementary torque acts for the torque control as well as for the speed control.

This feature with the additional torque setpoint enables a precontrol torque to be implemented for speed control.

###### Requirements

- The drive has been completely created and fully specified in the device configuration.
- The "Dynamic Drive Control (DDC)" operating mode is activated.

  - Or -

  The "Speed control" or "Torque control" mode is activated (see [Operating mode](#operating-mode-1)).
- The [extended parameterization](#overview-2) is active.

###### Signal source

| Symbol | Meaning |
| --- | --- |
| ![Signal source](images/148900452235_DV_resource.Stream@PNG-de-DE.png) | [Speed setpoint filter](#speed-setpoint-filter) |
| ![Signal source](images/148900435083_DV_resource.Stream@PNG-de-DE.png) | [Speed controller](#speed-controller) |

###### Change over between closed-loop speed/torque control (only with activated torque control)

1. In the "Speed/torque control" field (c1501), interconnect the signal source for the switchover between speed control and torque control.

   - 0 signal: Speed control
   - 1 signal: Torque control
2. Depending on the set signal source, now make the settings for speed control or torque control.

###### Setting torque setpoints for speed control (only with activated torque control)

1. Interconnect the signal source "Torque setpoint" (c1503)" for the torque setpoint of the torque control.
2. Specify the torque limiting (see "Specifying the torque limiting").
3. Set up to two additional torques (see "Setting additional torques").

###### Setting torque setpoints for torque control

1. Enter a smoothing constant of the acceleration torque in the "Smoothing" field ([p1517](SINAMICS%20Parameter%20G220.md#p15170n-accelerating-torque-smoothing-time-constant)).
2. Specify the torque limiting (see "Specifying the torque limiting").

###### Setting supplementary torques

For an activated speed control, you can set up to two additional torques.

1. Interconnect the signal source of supplementary torque 1 in the "Supplementary torque 1" (c1511) field.
2. Interconnect the signal source of the scaling factor of supplementary torque 1 in the "Scaling" (c1512) field.
3. Interconnect the signal source of supplementary torque 2 in the "Supplementary torque 2" (c1513) field.
4. Enter the scaling of supplementary torque 2 in the "Supplementary torque 2 scaling" field ([p1514](SINAMICS%20Parameter%20G220.md#p15140n-supplementary-torque-2-scaling)).

###### Defining torque limitation

1. Click the "Torque limiting" button.

   The "Speed controller torque limiting" function view is displayed.
2. Interconnect the scaling signal source for scaling the upper torque limit to limit the speed controller output without considering current and power limits in the "Scaling" (c1552[0]) field.
3. Interconnect the scaling signal source of the lower torque limit to limit the speed controller output without considering current and power limits in the "Scaling" (c1554[0]) field.
4. Interconnect the signal source to switch the torque limits between variable (c1551[0] = 1) and fixed torque limit (c1551[0] = 0) in the "Torque limit variable" (c1551[0]) field.

###### Result

You have configured the settings for the torque setpoint. Save the settings in the project.

###### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/148900477963_DV_resource.Stream@PNG-de-DE.png) | [Torque limitation](#torque-limitation) |

###### Function diagrams (FD)

Torque setpoint - 6060 -

###### Additional parameters

- [p0115](SINAMICS%20Parameter%20G220.md#p011506-sampling-times-for-internal-control-loops)
- [r1480](SINAMICS%20Parameter%20G220.md#r1480-speed-controller-pi-torque-output)
- [r1508](SINAMICS%20Parameter%20G220.md#r1508-torque-setpoint-before-supplementary-torque)
- [r1515](SINAMICS%20Parameter%20G220.md#r1515-supplementary-torque-total)
- [r1518](SINAMICS%20Parameter%20G220.md#r151801-accelerating-torque)

---

#### Torque limitation

This section contains information on the following topics:

- [Configuring torque limitation](#configuring-torque-limitation)

##### Configuring torque limitation

###### Overview

A machine sets a counter-torque or load torque against the torque of the drive.

In order to avoid overloads of the machine particularly during acceleration and deceleration phases, the torque of the drive must be limited according to the connected machine.

The following limits can be set for the torque limiting:

- Upper torque limit

  Permits the upper torque value to be specified and, if necessary, be scaled.
- Current limit

  Permits the actual current limit to be viewed. Because the current limiting also limits the maximum torque that the motor can provide, if the torque limit is increased, more torque will only be available if a higher current can also flow. It may be necessary to also adapt the current limit.
- Power limit

  Permits the current motorized and regenerative power limit to be viewed. The value specifies the maximum permissible power, whereby different limits can be viewed for motorized and regenerative mode.
- Lower torque limit

  Permits the lower torque value to be specified and, if necessary, be scaled.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Danger to life due to uncontrolled movement of the drive as a result of incorrect parameter assignment**   Incorrect parameter assignment of the torque limits can result in uncontrolled movement of the drives if there is no counter-torque, and cause death or serious injury.  - Make sure that the parameter assignment is correct. |  |

###### Requirements

- The drive has been completely created and fully specified in the device configuration.
- The "Dynamic Drive Control (DDC)" operating mode is activated.

  - Or -

  The "Speed control" or "Torque control" mode is activated (see [Operating mode](#operating-mode-1)).
- The [extended parameterization](#overview-2) is active.

###### Signal source

| Symbol | Meaning |
| --- | --- |
| ![Signal source](images/148898416523_DV_resource.Stream@PNG-de-DE.PNG) | [Torque setpoints](#torque-setpoints) |

###### Configuring torque limitation

1. Click the "Upper torque limit" button.

   A dialog with the same name opens.
2. Enter the fixed upper torque limit in the "Torque limit upper" ([p1520](SINAMICS%20Parameter%20G220.md#p15200n-torque-limit-upper)[0]) field.
3. Interconnect the signal source for the upper torque limit in the "Torque limit upper" (c1522[0]) field.
4. Correct the scaling for the upper torque limit in the "Scaling" ([p1524](SINAMICS%20Parameter%20G220.md#p15240n-torque-limit-upper-scaling)[0]) field.
5. Interconnect the scaling signal source of the upper torque limit with p1524[0] in the c1528 field.
6. Interconnect the signal source to switch the torque limits between variable (c1551[0] = 1) and fixed torque limit (c1551[0] = 0) in the "Torque limit variable" (c1551[0]) field.

   If you select the setting "Fixed torque limit", the value "Upper torque limit" (p1520[0]) is used. For a "variable torque limit", the minimum of "Torque limit upper" (p1520[0]) and the scaled "Torque limit upper" (c1528[0]) is used.
7. Enter a value for the fixed lower torque limit in the "Torque limit lower" ([p1521](SINAMICS%20Parameter%20G220.md#p15210n-torque-limit-lower)[0]) field.
8. Once all necessary settings have been made, click "Close".

   The dialog closes.
9. Click the "Lower torque limit" button.

   A dialog with the same name opens.
10. Enter the fixed lower torque limit in the "Torque limit lower" (p1521[0]) field.
11. Interconnect the signal source for the lower torque limit in the "Torque limit lower" (c1523[0]) field.
12. Correct the specified scaling for the lower torque limit in the "Scaling" ([p1525](SINAMICS%20Parameter%20G220.md#p15250n-torque-limit-lower-scaling)[0]) field.
13. Interconnect the scaling signal source of the lower or regenerative torque limit in p1523 in the field "c1529[0]".
14. Interconnect the signal source to switch the torque limits between variable (c1551[0] = 1) and fixed torque limit (c1551[0] = 0) in the "Torque limit variable" (c1551[0]) field.

    If you select the setting "Fixed torque limit", the value "Lower torque limit" (p1521[0]) is used. For a "variable torque limit", the maximum of "Torque limit lower" (p1521[0]) and the scaled "Torque limit lower" (c1529[0]) is used.
15. Once all necessary settings have been made, click "Close".

    The dialog closes.

###### Configuring the current limit

The current limit can be configured alternatively or in addition to the torque limiting. If only the current limit is configured (without the torque limit), the drive ramps up quickly. However, as only the ramp-function generator is stopped when the current limit is reached, the current can continue to rise. This must be taken into account during the parameterization (if required, through a safety clearance) so that the drive is not switched off with an overcurrent error.

1. Click the "Current limit" button.

   A dialog with the same name opens.
2. Enter the "Current limit" ([p0640](SINAMICS%20Parameter%20G220.md#p06400n-motor-current-limit)[0]) here.
3. Interconnect the "Scaling" (c0641[0]) signal source for the scaling of the current limit.
4. Once all necessary settings have been made, click "Close".

   The dialog closes.

###### Configuring the power limit

The power limit can be configured alternatively or in addition to the torque limiting.

1. Click the "Power limit" button.

   A dialog with the same name opens.
2. In the "Power limit motorized" field ([p1530](SINAMICS%20Parameter%20G220.md#p15300n-power-limit-motoring)[0]), enter the motorized power limit.
3. In the "Power limit scaling" field ([p1556](SINAMICS%20Parameter%20G220.md#p15560n-power-limit-scaling)[0]), enter the scaling of the signal source for the motorized and negative regenerative power limit.
4. In the "Power limit" field (c1555[0]), interconnect the signal source for the motorized and negative regenerative power limit.
5. In the "Power limit regenerative" field ([p1531](SINAMICS%20Parameter%20G220.md#p15310n-power-limit-regenerative)[0]), enter the regenerative power limit.
6. Once all necessary settings have been made, click "Close".

   The dialog closes.

###### Display of the set torque limiting

The set torque limiting is displayed via the following parameters:

- Torque limit reached ([r1407](SINAMICS%20Parameter%20G220.md#r1407031-status-word-speed-controller).7)
- Upper torque limit reached (r1407.8)
- Lower torque limit reached (1407.9)
- Speed limitation controller active (r1407.17)

###### Result

You have configured the settings for torque limiting. Save the settings in the project.

###### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/148898527499_DV_resource.Stream@PNG-de-DE.png) | [Current setpoint filter](#current-setpoint-filter) |

###### Function diagrams (FD)

Torque setpoint - 6060 -

Upper/lower torque limit - 6630 -

Current/power/torque limits - 6640 -

###### Additional parameters

- [r0079](SINAMICS%20Parameter%20G220.md#r0079-torque-setpoint)
- [p0115](SINAMICS%20Parameter%20G220.md#p011506-sampling-times-for-internal-control-loops)
- [r1526](SINAMICS%20Parameter%20G220.md#r1526-total-upper-torque-limit)
- [r1527](SINAMICS%20Parameter%20G220.md#r1527-total-lower-torque-limit)
- [r1536](SINAMICS%20Parameter%20G220.md#r153601-torque-generating-current-maximum-limit)
- [r1537](SINAMICS%20Parameter%20G220.md#r153701-torque-generating-current-minimum-limit)
- [r1538](SINAMICS%20Parameter%20G220.md#r1538-upper-effective-torque-limit)
- [r1539](SINAMICS%20Parameter%20G220.md#r1539-lower-effective-torque-limit)
- [r1548](SINAMICS%20Parameter%20G220.md#r154801-stall-current-limit-torque-generating-maximum)

---

#### Current setpoint filter

This section contains information on the following topics:

- [Configuring the current setpoint filter](#configuring-the-current-setpoint-filter)

##### Configuring the current setpoint filter

###### Overview

The current setpoint filters are used to skip or weaken certain frequency ranges in order to suppress resonance effects. Bandstop filters and low-pass filters are available to suppress specific interference frequency ranges.

Up to 2 current setpoint filters and a supplementary torque can be set by default.

You can parameterize the two current setpoint filters 1 and 2 connected in series as follows:

- PT2 low pass (PT2: -40 dB/decade)
- General 2nd order filter

###### Requirements

- The drive has been completely created and fully specified in the device configuration.
- The "Dynamic Drive Control (DDC)" operating mode is activated.

  - Or -

  The "Speed control" or "Torque control" control type is activated (see [Operating mode](#operating-mode-1)).
- The [extended parameterization](#overview-2) is active.

  In the standard parameterization, the modulator mode and modulation depth settings are not shown.

###### Signal source

| Symbol | Meaning |
| --- | --- |
| ![Signal source](images/148900477963_DV_resource.Stream@PNG-de-DE.png) | [Torque limitation](#torque-limitation) |
| ![Signal source](images/148914160779_DV_resource.Stream@PNG-de-DE.png) | [Vdc-min/max controller](#vdc-minmax-controller) |

###### Procedure

1. To activate current setpoint filter 1, activate the "Filter 1" ([p1656](SINAMICS%20Parameter%20G220.md#p16560n04-current-setpointspeed-actual-value-filter-activation)[0].0) option.

   To activate further available current setpoint filters, activate further filter options in the same way.

   The function view now displays a curve for all filters not activated previously rather than a straight line.
2. Click the button of filter 1.

   The "Current setpoint filter" dialog opens.
3. Select the required filter type for current setpoint filter 1 in the "Filter type" ([p1657](SINAMICS%20Parameter%20G220.md#p16570n-current-setpoint-filter-1-type)) drop-down list:

   - [1] PT2 low pass
   - [2] General 2nd order filter
4. Correct the following default values for current setpoint filter 1:

   - Numerator frequency
   - Numerator damping
   - Denominator frequency
   - Denominator damping
5. Click "Accept" to confirm the new values.
6. If you have activated additional current setpoint filters, repeat steps 3 and 5 for these filters.
7. Once all necessary settings have been made, click "Close".

   The dialog closes.
8. Interconnect the signal source in the "Natural frequency tuning filter 1" (c1655[0]) field for the tuning of the natural frequency of current setpoint filter 1.

   If a 2nd current setpoint has been configured, interconnect the signal source in the "Natural frequency tuning filter 2" (c1655[1]) field for the tuning of the natural frequency of current setpoint filter 2.

###### Setting additional torque 3 for applying a friction characteristic

1. Interconnect the signal source in the "Supplementary torque 3" field (c1569[0]) for supplementary torque 3.

   The signal input is preferably used for injecting the friction characteristic. The friction compensation is also effective if the velocity controller output reaches its force limits, but the current limits have not yet been reached.
2. If the friction characteristic should also be configured, click the ![Setting additional torque 3 for applying a friction characteristic](images/92607914379_DV_resource.Stream@PNG-de-DE.PNG) icon.

   The "Friction characteristic" function view is then displayed (see "[Friction characteristic](#friction-characteristic)").

###### Result

You have configured the settings for the current setpoint filter. Save the settings in the project.

###### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/148914105227_DV_resource.Stream@PNG-de-DE.png) | [Current controller](#current-controller) |

###### Function diagrams (FD)

Current setpoint filter - 6710 -

###### Additional parameters

- [r0079](SINAMICS%20Parameter%20G220.md#r0079-torque-setpoint)
- [p0115](SINAMICS%20Parameter%20G220.md#p011506-sampling-times-for-internal-control-loops)
- [r1536](SINAMICS%20Parameter%20G220.md#r153601-torque-generating-current-maximum-limit)
- [r1537](SINAMICS%20Parameter%20G220.md#r153701-torque-generating-current-minimum-limit)
- [r1650](SINAMICS%20Parameter%20G220.md#r1650-current-setpoint-torque-generating-before-filter)
- [p1400](SINAMICS%20Parameter%20G220.md#p14000n031-speed-control-configuration)
- [p1658](SINAMICS%20Parameter%20G220.md#p16580n-current-setpoint-filter-1-denominator-natural-frequency)
- [p1659](SINAMICS%20Parameter%20G220.md#p16590n-current-setpoint-filter-1-denominator-damping)
- [p1660](SINAMICS%20Parameter%20G220.md#p16600n-current-setpoint-filter-1-numerator-natural-frequency)
- [p1661](SINAMICS%20Parameter%20G220.md#p16610n-current-setpoint-filter-1-numerator-damping)
- [p1662](SINAMICS%20Parameter%20G220.md#p16620n-current-setpoint-filter-2-type)
- [p1663](SINAMICS%20Parameter%20G220.md#p16630n-current-setpoint-filter-2-denominator-natural-frequency)
- [p1664](SINAMICS%20Parameter%20G220.md#p16640n-current-setpoint-filter-2-denominator-damping)
- [p1665](SINAMICS%20Parameter%20G220.md#p16650n-current-setpoint-filter-2-numerator-natural-frequency)

---

#### Flux setpoint

This section contains information on the following topics:

- [Description of function](#description-of-function)
- [Efficiency optimization for reluctance motors](#efficiency-optimization-for-reluctance-motors)
- [Efficiency optimization for asynchronous motor](#efficiency-optimization-for-asynchronous-motor)

##### Description of function

###### Overview

You can configure the flux setpoint processing that generates the current setpoint for the current controller via various settings in the "Flux setpoint" function view. The specific configuration options depend on the type of motor being used.

###### Requirements

- The drive has been completely created and fully specified in the device configuration.
- An induction motor or a reluctance motor is used.
- The "Dynamic Drive Control (DDC)" operating mode is activated.

  - Or -

  The "Speed control" or "Torque control" control type is activated (see [Operating mode](#operating-mode-1)).
- The [extended parameterization](#overview-2) is active.

###### Principle of operation for induction motors

Speed and torque are specified by the driven machine. Therefore, the remaining variable value for the efficiency optimization is the flux. The efficiency of induction motors can be optimized via 2 different methods. Both optimizing methods via the flux. It only makes sense to activate the efficiency optimization if the dynamic response demands are low (e.g. pumps and fans).

**Efficiency optimization 1 (standard)**

With p1580 = 100%, the flux in the machine in no-load operation is reduced to half the flux setpoint ([p1570](SINAMICS%20Parameter%20G220.md#p15700n-flux-setpoint)). As soon as the drive is loaded, the flux setpoint rises linearly with the load and reaches the setpoint set in p1570 at approx. [r0077](SINAMICS%20Parameter%20G220.md#r0077-current-setpoint-torque-generating) = [r0331](SINAMICS%20Parameter%20G220.md#r03310n-actual-motor-magnetizing-currentshort-circuit-current) x p1570.

![Efficiency optimization 1](images/159813335819_DV_resource.Stream@PNG-en-US.png)

Efficiency optimization 1

In the field-weakening range, the full-scale value is reduced by the actual degree of field weakening. The smoothing time ([p1582](SINAMICS%20Parameter%20G220.md#p15820n-flux-setpoint-smoothing-time)) should be set to approx. 100 to 200 ms. Flux differentiation (see also [p1401](SINAMICS%20Parameter%20G220.md#p14010n030-flux-control-configuration).1) is automatically deactivated internally following magnetizing.

![Simple efficiency optimization](images/159828678923_DV_resource.Stream@PNG-en-US.png)

Simple efficiency optimization

**Efficiency optimization 2 (extended)**

Generally, the efficiency optimization 2 (p1401.14) achieves a better efficiency than the simple efficiency optimization (p1580). With the efficiency optimization 2, the current operating point of the motor is determined depending on the efficiency and flux, and the flux set to the optimal efficiency. Depending on the operation point of the motor, the converter reduces or increases the flux of the motor in partial load operation.

| Symbol | Meaning |
| --- | --- |
| ![Efficiency optimization 2 with flux reduction](images/159828649099_DV_resource.Stream@PNG-en-US.png)   Efficiency optimization 2 with flux reduction | ![Efficiency optimization 2 with flux increase](images/159827876875_DV_resource.Stream@PNG-en-US.png)   Efficiency optimization 2 with flux increase |

Efficiency optimization 2 can be activated with p1401.14 = 1. It deactivated by default.

**Magnetization control**

For crane applications, frequently a frequency converter is switched alternately to different motors. After being switched to a different motor, a new dataset must be loaded in the frequency converter and the motor magnetized. This can result in excessive waiting times that could be reduced by magnetization, if required.

Magnetizing curves:

| Magnetization | Parameterization | Curve |
| --- | --- | --- |
| Standard | p1401.0 = 0, p1401.6 = 0 | ![Principle of operation for induction motors](images/110892116875_DV_resource.Stream@PNG-de-DE.png) |
| Quick magnetization | p1401.6 = 1 | ![Principle of operation for induction motors](images/110892206475_DV_resource.Stream@PNG-de-DE.png) |
| Soft starting | p1401.0 = 1 | ![Principle of operation for induction motors](images/110892244875_DV_resource.Stream@PNG-de-DE.png) |

###### Principle of operation for reluctance motors

The high efficiency typical of 1FP1 reluctance motors can also be achieved in the partial load range. For this purpose, the motor is operated with a loss-optimized current specification depending on the required torque (MTPC: Max-Torque-Per-Current). This operation corresponds to a load-dependent specification of the flux setpoint and can be preconfigured accordingly during commissioning using p1401.3 = 1. In addition, the flux setpoint can be configured via p1401.9 = 1 so that it increases dynamically with rapid torque build-up.

###### Function diagrams (FD)

Field weakening characteristic, Id setpoint (induction motor, p0300 = 1xxx) - 6722 -

Field weakening controller, flux controller, Id setpoint (induction motor, p0300 = 1xxx) - 6723 -

Flux setpoint (synchronous reluctance motor, p0300 = 6xxx) - 6790 -

###### Additional parameters

---

##### Efficiency optimization for reluctance motors

###### Overview

For reluctance motors, the efficiency can be optimized via a flux setpoint and flux reduction.

###### Requirements

- The drive has been completely created and fully specified in the device configuration.
- A reluctance motor is used.
- The "Speed control" or "Torque control" control type is activated (see [Operating mode](#operating-mode-1)).
- The [extended parameterization](#overview-2) is active.

###### Configuring the flux setpoint

1. Correct the specified value in the "Voltage reserve dynamic" ([p1574](SINAMICS%20Parameter%20G220.md#p15740n-voltage-reserve-dynamic)) field.
2. Correct the specified integral time of the field weakening controller in the "Field weakening controller" ([p1596](SINAMICS%20Parameter%20G220.md#p15960n-field-weakening-controller-integral-action-time)) field.
3. Configure the flux reduction (see below).
4. Correct the specified scaling of the flux setpoint in the "Flux setpoint" ([p1570](SINAMICS%20Parameter%20G220.md#p15700n-flux-setpoint)) field.
5. Correct the smoothing time specified for the flux setpoint for flux build-up because of a flux reduction in the upper "Smoothing" ([p1579](SINAMICS%20Parameter%20G220.md#p15790n-flux-reduction-flux-build-up-smoothing-time)) field.
6. Correct the smoothing time specified for the flux setpoint for flux removal because of a flux reduction in the lower "Smoothing" ([p1578](SINAMICS%20Parameter%20G220.md#p15780n-flux-reduction-flux-decrease-smoothing-time)) field.
7. For open-loop speed controlled drives, the torque default settings are active in the lower left part of the function view. In this case, correct the following defaults:

   - "Static torque setpoint" ([p1610](SINAMICS%20Parameter%20G220.md#p16100n-starting-torque-static-without-encoder))
   - "Supplementary torque when accelerating" ([p1611](SINAMICS%20Parameter%20G220.md#p16110n-acceleration-starting-torque-encoderless))
   - "Current injection ramp time" ([p1601](SINAMICS%20Parameter%20G220.md#p16010n-current-injection-ramp-time))
   - "Id_set/flux calculation" ([p0346](SINAMICS%20Parameter%20G220.md#p03460n-motor-excitation-build-up-time))
   - "Smoothing" ([p1616](SINAMICS%20Parameter%20G220.md#p16160n-current-setpoint-smoothing-time))

###### Configuring flux reduction

1. Click "Flux reduction"  
   Dialog "Flux reduction" opens.
2. Correct the value specified for the flux reduction in the "Flux reduction factor" ([p1581](SINAMICS%20Parameter%20G220.md#p15810n-flux-reduction-factor)) field.
3. To activate the dynamic increase in the flux setpoint when torque is built-up quickly, activate the "Dynamic load-dependent flux boost" ([p1401](SINAMICS%20Parameter%20G220.md#p14010n030-flux-control-configuration).9) option.
4. To deactivate the load-dependent calculation of the flux characteristic, deactivate the "Flux characteristic load-dependent" (p1401.3) option.
5. Once all necessary settings have been made, click "Close".

   The dialog closes.

###### Result

You have configured the flux setpoint and the flux reduction for efficiency optimization of a reluctance motor.

###### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/110697927947_DV_resource.Stream@PNG-de-DE.png) | [Current controller](#current-controller) |

###### Additional parameters

---

##### Efficiency optimization for asynchronous motor

###### Overview

Speed and torque are specified by the driven machine. Therefore, the remaining variable value for the efficiency optimization is the flux. The efficiency of induction motors can be optimized via 2 different methods. In addition, magnetizing can be controlled via different magnetizing curves.

###### Requirements

- The drive has been completely created and fully specified in the device configuration.
- An induction motor is used.
- The "Speed control" or "Torque control" mode is activated (see [Operating mode](#operating-mode-1)).
- The [extended parameterization](#overview-2) is active.

###### Configuring the flux setpoint

1. Correct the specified value in the "Voltage reserve dynamic" ([p1574](SINAMICS%20Parameter%20G220.md#p15740n-voltage-reserve-dynamic)) field.
2. Correct the specified integral time of the field weakening controller in the "Field weakening controller" ([p1596](SINAMICS%20Parameter%20G220.md#p15960n-field-weakening-controller-integral-action-time)) field.
3. Correct the smoothing time specified for the flux setpoint in the "Smoothing" ([p1582](SINAMICS%20Parameter%20G220.md#p15820n-flux-setpoint-smoothing-time)) field.
4. Configure the field-weakening characteristic for the desired efficiency optimization (see "Configuring the field-weakening characteristic ...").
5. Configure the magnetizing curve (see "Configuring magnetizing control").
6. By default, flux differentiation is active for induction motors. However, this reduces the acceleration, because the field weakening is still active during the magnetization.

   If you want to deactivate the magnetization, select the "[0] No" ([p1401](SINAMICS%20Parameter%20G220.md#p14010n030-flux-control-configuration).1) option in the "Differentiation" drop-down list.
7. For open-loop speed controlled drives, the torque default settings are active in the lower left part of the function view. In this case, correct the following defaults:

   - "Static torque setpoint" ([p1610](SINAMICS%20Parameter%20G220.md#p16100n-starting-torque-static-without-encoder))
   - "Supplementary torque when accelerating" ([p1611](SINAMICS%20Parameter%20G220.md#p16110n-acceleration-starting-torque-encoderless))
   - "Smoothing" ([p1616](SINAMICS%20Parameter%20G220.md#p16160n-current-setpoint-smoothing-time))

###### Configuring magnetizing control

1. Click the "Magnetization control" button in the "Flux setpoint" function view.  
   A dialog with the same name opens.
2. In order to parameterize a magnetization of the induction motor with an initial low rise, activate the "Flux setpoint soft starting active" (p1401.0 = 1) option.
3. To activate the quick magnetization, activate the "Quick magnetizing" (p1401.6 = 1) option.
4. Correct the scaling of the flux setpoint in the "Flux setpoint" ([p1570](SINAMICS%20Parameter%20G220.md#p15700n-flux-setpoint)) field.
5. Correct the value for the flux threshold of the magnetization in the "Flux threshold value magnetizing" ([p1573](SINAMICS%20Parameter%20G220.md#p15730n-flux-threshold-value-magnetizing)) field.
6. Enter a value for the motor excitation build-up time in the "Motor excitation build-up time" ([p0346](SINAMICS%20Parameter%20G220.md#p03460n-motor-excitation-build-up-time)) field.
7. Once all necessary settings have been made, click "Close".

   The dialog closes.

###### Configuring the field-weakening characteristic with efficiency optimization 1

1. Ensure that the "Efficiency optimization" option is deactivated in the "Flux setpoint" function view.
2. Click the "Field weakening characteristic" button.  
   A dialog with the same name opens.
3. Correct the specified scaling value of the precontrol characteristic for the application point of field weakening in the "Field weakening characteristic scaling" ([p1586](SINAMICS%20Parameter%20G220.md#p15860n-field-weakening-characteristic-scaling)) field.
4. Correct the flux setpoint specified in the "Flux setpoint" (p1570[0]) field; this value refers to the motor rated current.
5. Correct the specified efficiency in the "Efficiency optimization" (p1580) field.
6. Once all necessary settings have been made, click "Close".

   The dialog closes.

###### Alternatively: Configuring the field-weakening characteristic with efficiency optimization 2

1. Activate the "Efficiency optimization" option in the "Flux setpoint" function view.
2. Click the "Field weakening characteristic" button.  
   A dialog with the same name opens.
3. Correct the specified scaling value of the precontrol characteristic for the application point of field weakening in the "Field weakening characteristic scaling" (p1586) field.
4. Correct the flux setpoint specified in the "Flux setpoint" (p1570[0]) field; this value refers to the motor rated current.
5. Correct the specified maximum limit value for the calculated optimal flux in the "Maximum flux limit value" ([p3316](SINAMICS%20Parameter%20G220.md#p33160n-efficiency-optimization-maximum-flux-limit-value)) field.
6. Correct the specified minimum limit value for the calculated optimal flux in the "Flux minimum limit value" ([p3315](SINAMICS%20Parameter%20G220.md#p33150n-efficiency-optimization-minimum-flux-limit-value)) field.
7. Once all necessary settings have been made, click "Close".

   The dialog closes.

###### Result

You have configured the flux setpoint, the magnetization control and the field weakening characteristic for efficiency optimization of an induction motor.

###### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/110697927947_DV_resource.Stream@PNG-de-DE.png) | [Current controller](#current-controller) |

###### Additional parameters

---

#### Current controller

This section contains information on the following topics:

- [Configuring the current controller](#configuring-the-current-controller)

##### Configuring the current controller

###### Overview

The current controller is generally only required for the first commissioning. No further settings are required in normal operation. The settings of the controller can be further optimized for special application cases.

The following settings can be made for the current controller:

- P gain
- Adaptation of the current controller
- Integral time

###### Requirement

- The drive has been completely created and fully specified in the device configuration.
- The "Dynamic Drive Control (DDC)" operating mode is activated.

  - Or -

  The "Speed control" or "Torque control" control type is activated (see [Operating mode](#operating-mode-1)).
- The [extended parameterization](#overview-2) is active.

  In the standard parameterization, the modulator mode and modulation depth settings are not shown.

###### Signal source

| Symbol | Meaning |
| --- | --- |
| ![Signal source](images/148898527499_DV_resource.Stream@PNG-de-DE.png) | [Current setpoint filter](#current-setpoint-filter) |
| ![Signal source](images/148898407947_DV_resource.Stream@PNG-de-DE.PNG) | [Power unit (torque-generating actual current value)](#power-unit) |
| ![Signal source](images/148898407947_DV_resource.Stream@PNG-de-DE.PNG) | [Power unit (field-generating actual current value)](#power-unit) |
| ![Signal source](images/148898527499_DV_resource.Stream@PNG-de-DE.png) | [Flux setpoint](#flux-setpoint) |

###### Setting P gain and integral time

1. Enter the desired value for the proportional gain of the lower adaptation current range in the "P gain" ([p1715](SINAMICS%20Parameter%20G220.md#p17150n-current-controller-p-gain)) field.
2. Correct the specified value for the integral time of the current controller in the "Integral time" ([p1717](SINAMICS%20Parameter%20G220.md#p17170n-current-controller-integral-action-time)) field.

###### Setting the adaptation of the current controller

The P gain of the current controller can be reduced via an adaptation depending on the current. The adaptation function must be activated first for the configuration of the adaptation.

1. Select the "[1] Yes" option ([p1402](SINAMICS%20Parameter%20G220.md#p14020n030-closed-loop-current-control-and-motor-model-configuration).2) in the drop-down list below the "Adaptation" button in the "Current controller" function view.

   The "Adaptation" button now shows a curve and can be used.
2. Click the "Adaptation" button.

   A dialog with the same name opens.
3. Correct the factor for the P gain of the current controller in the adaptation range (current > [p0392](SINAMICS%20Parameter%20G220.md#p03920n-current-controller-adaptation-starting-point-kp-adapted)) in the "Scaling" ([p0393](SINAMICS%20Parameter%20G220.md#p03930n-current-controller-adaptation-p-gain-scaling)) field.
4. Enter the application point of the current-dependent current controller adaptation at which the adapted current controller gain takes effect p1715 x p0393 in the "Application point Kp adapted" (p0392) field.
5. Enter the application point of the current-dependent current controller adaptation at which the current controller gain takes effect p1715 in the "Application point Kp" ([p0391](SINAMICS%20Parameter%20G220.md#p03910n-current-controller-adaptation-starting-point-kp)) field.
6. Once all necessary settings have been made, click "Close".

   The dialog closes.

###### Result

You have configured the current controller settings. Save the settings in the project.

###### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/148879237771_DV_resource.Stream@PNG-de-DE.png) | [Power unit](#power-unit) |
| ![Signal processing](images/148879237771_DV_resource.Stream@PNG-de-DE.png) | [Power unit](#power-unit) |

###### Function diagrams (FD)

Iq and Id controllers (Part 1) - 6714 -

###### Additional parameters

- [r0029](SINAMICS%20Parameter%20G220.md#r0029-current-actual-value-field-generating-smoothed)
- [r0030](SINAMICS%20Parameter%20G220.md#r0030-current-actual-value-torque-generating-smoothed)
- [r0072](SINAMICS%20Parameter%20G220.md#r0072-output-voltage)
- [r0075](SINAMICS%20Parameter%20G220.md#r0075-current-setpoint-field-generating)
- [r0077](SINAMICS%20Parameter%20G220.md#r0077-current-setpoint-torque-generating)
- [p0115](SINAMICS%20Parameter%20G220.md#p011506-sampling-times-for-internal-control-loops)

---

#### Power unit

This section contains information on the following topics:

- [Configuring the power unit](#configuring-the-power-unit)

##### Configuring the power unit

###### Overview

The operating values of the power unit are displayed in the "Power unit" function view.

You can only change the setpoint of the pulse frequency (converter switching frequency) here.

This pulse frequency ([p1800](SINAMICS%20Parameter%20G220.md#p18000n-pulse-frequency-setpoint)) must be set to the rated value of the converter at the first commissioning. The maximum possible pulse frequency is therefore determined by the power unit used. If the pulse frequency is set higher, this can result in a reduction of the maximum output current depending on the power unit.

###### Signal source

| Symbol | Meaning |
| --- | --- |
| ![Signal source](images/148914105227_DV_resource.Stream@PNG-de-DE.png) | [Current controller](#current-controller)   Not for activated U/f control |
| ![Signal source](images/148914105227_DV_resource.Stream@PNG-de-DE.png) | [Current controller](#current-controller)   Not for activated U/f control |
| ![Signal source](images/148914152203_DV_resource.Stream@PNG-de-DE.PNG) | [U/f control](#uf-control)   Only for activated U/f control |
| ![Signal source](images/148914152203_DV_resource.Stream@PNG-de-DE.PNG) | [U/f control](#uf-control)   Only for activated U/f control |

###### Requirements

- The drive has been completely created and fully specified in the device configuration.
- The [extended parameterization](#overview-2) is active.

  In the standard parameterization, the modulator mode and modulation depth settings are not shown.

###### Set modulator mode and maximum modulation depth

1. Click the "Modulator mode" ([p1802](SINAMICS%20Parameter%20G220.md#p18020n-modulator-mode)) drop-down list and select the mode for the modulator.
2. Enter the maximum modulation depth in the "Maximum modulation depth" field ([p1803](SINAMICS%20Parameter%20G220.md#p18030n-maximum-modulation-depth)).

###### Setting the pulse frequency setpoint

1. Enter the desired converter switching frequency in the "Pulse frequency setpoint" (p1800) field.
2. Make sure that the frequency does not exceed the rated value of the converter, as this would result in a reduction of the output current.
3. If the motor does not rotate in the right direction, you can reverse the phase sequence of the output phases. Select the option "Yes" in the "Reverse the output phase sequence" ([p1820](SINAMICS%20Parameter%20G220.md#p18200n-reverse-the-output-phase-sequence)) drop-down list.

###### Result

You have configured the power unit settings. Save the settings in the project.

###### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/148914036875_DV_resource.Stream@PNG-de-DE.png) | [Motor](#motor) |
| ![Signal processing](images/148914105227_DV_resource.Stream@PNG-de-DE.png) | [Current controller](#current-controller)   Not for activated U/f control |
| ![Signal processing](images/148914105227_DV_resource.Stream@PNG-de-DE.png) | [Current controller](#current-controller)   Not for activated U/f control |

###### Additional parameters

- [r0024](SINAMICS%20Parameter%20G220.md#r0024-output-frequency-smoothed)
- [r0027](SINAMICS%20Parameter%20G220.md#r0027-absolute-actual-current-smoothed)
- [r0029](SINAMICS%20Parameter%20G220.md#r0029-current-actual-value-field-generating-smoothed)
- [r0030](SINAMICS%20Parameter%20G220.md#r0030-current-actual-value-torque-generating-smoothed)
- [r0036](SINAMICS%20Parameter%20G220.md#r003602-power-unit-overload)
- [r0037](SINAMICS%20Parameter%20G220.md#r0037010-power-unit-temperatures)
- [r0069](SINAMICS%20Parameter%20G220.md#r006908-phase-current-actual-value)
- [r0070](SINAMICS%20Parameter%20G220.md#r0070-actual-dc-link-voltage)
- [r0072](SINAMICS%20Parameter%20G220.md#r0072-output-voltage)
- [r0073](SINAMICS%20Parameter%20G220.md#r0073-maximum-modulation-depth)
- [r0074](SINAMICS%20Parameter%20G220.md#r0074-modulation-depth)
- [r1801](SINAMICS%20Parameter%20G220.md#r180102-pulse-frequency)

---

#### Motor

This section contains information on the following topics:

- [Checking the motor data](#checking-the-motor-data)

##### Checking the motor data

###### Overview

The most important motor data can be viewed and set for the converter in the "Motor" function view. The buttons listed below call the associated detail view with which the motor data can be checked or the settings changed.

| Symbol | Meaning |
| --- | --- |
| ![Overview](images/148913550347_DV_resource.Stream@PNG-de-DE.png) | Configuring a [motor brake](#brake-control) (brake control) |
| ![Overview](images/148914045451_DV_resource.Stream@PNG-de-DE.png) | Configure [motor temperature monitoring](#motor-temperature) |
| ![Overview](images/148914015499_DV_resource.Stream@PNG-de-DE.png) | Checking the motor data  Requirement: configured motor; no DQ motor. |

###### Requirements

- The drive has been completely created and fully specified in the device configuration.
- The [extended parameterization](#overview-2) is active.

  In the standard parameterization, the detailed motor data is not shown.

###### Signal source

| Symbol | Meaning |
| --- | --- |
| ![Signal source](images/148879237771_DV_resource.Stream@PNG-de-DE.png) | [Power unit](#power-unit) |

###### Motor data

The tabular overview in the lower area of the "Motor" function view clearly shows the motor parameters of the motor:

| Parameter | Name |
| --- | --- |
| [r0020](SINAMICS%20Parameter%20G220.md#r0020-speed-setpoint-smoothed) | Speed setpoint smoothed |
| [r0021](SINAMICS%20Parameter%20G220.md#r0021-speed-actual-value-smoothed) | Actual speed value smoothed |
| [r0024](SINAMICS%20Parameter%20G220.md#r0024-output-frequency-smoothed) | Output frequency |
| [r0025](SINAMICS%20Parameter%20G220.md#r0025-output-voltage-smoothed) | Output voltage smoothed |
| [r0027](SINAMICS%20Parameter%20G220.md#r0027-absolute-actual-current-smoothed) | Absolute current value smoothed |
| [r0031](SINAMICS%20Parameter%20G220.md#r0031-actual-torque-smoothed) | Actual torque smoothed |
| [r0032](SINAMICS%20Parameter%20G220.md#r0032-active-power-actual-value-smoothed) | Active power actual value smoothed |
| [r0035](SINAMICS%20Parameter%20G220.md#r0035-motor-temperature) | Motor temperature |

The current data is displayed in online mode.

**Displaying further motor data**

To display further current parameters of your motor, proceed as follows:

1. Click the ![Motor data](images/148913558923_DV_resource.Stream@PNG-de-DE.png) "Check motor data" button.  
   The "Motor data" function view opens.

###### Changing the direction of rotation of the motor

The default setting is "[0] Clockwise". If required, the direction of rotation of the motor, and thus also of the actual encoder value, can be changed.

1. Select direction of rotation "[1] Left" ([p1821](SINAMICS%20Parameter%20G220.md#p18210n-direction-of-rotation)) in the drop-down list.

   When switching the drive data set with differently set rotational direction and pulse enable, fault F07434 is issued.

###### Result

You were able to view the motor data and configure the direction of rotation. Save the settings in the project.

###### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/154889541131_DV_resource.Stream@PNG-de-DE.PNG) | [Motor encoder](#motor-encoder) |

###### Additional parameters

---

#### Motor encoder

This section contains information on the following topics:

- [Configuring the motor encoder](#configuring-the-motor-encoder)

##### Configuring the motor encoder

###### Overview

For operation with motor encoder, you can define the actual speed value acquisition and the smoothing of the actual speed value.

###### Requirement

- The drive has been completely created and fully specified in the device configuration.
- "Speed or torque control" control type is activated.
- A motor encoder is used.

  No setting is required for encoderless operation. In this case, the speed of the motor model is automatically adopted.
- The [extended parameterization](#overview-2) is active.

  In the standard parameterization, only some of the settings described below are possible.

###### Signal source

| Symbol | Meaning |
| --- | --- |
| ![Signal source](images/154753304331_DV_resource.Stream@PNG-de-DE.png) | [Motor](#checking-the-motor-data) |

###### Parameterizing the actual speed value acquisition of the motor encoder

1. If you want to smooth fluctuation peaks in the actual speed value, enter a smoothing time constant in the "Smoothing" ([p1441](SINAMICS%20Parameter%20G220.md#p14410n-actual-speed-smoothing-time)) field.

   If required, you can use a trace to check whether the controller with the smoothing is still sufficiently dynamic.
2. To activate the actual speed value filter, activate the "Filter 5" ([p1656](SINAMICS%20Parameter%20G220.md#p16560n04-current-setpointspeed-actual-value-filter-activation)[0].4) option.

   This filter can now be parameterized. A description of the filters can be found in section "[Using a signal filter](Configuring%20SINAMICS%20G220%20drives.md#using-a-signal-filter)".
3. Click the button below the "Filter 5" option.

   The "Actual speed value filter" dialog opens.
4. In the "Actual speed value filter 5 type" ([p1677](SINAMICS%20Parameter%20G220.md#p16770n-speed-actual-value-filter-5-type)) drop-down list, select one of the following filter types for the actual speed value filter.

   - Low-pass PT2
   - Bandstop
   - Low-pass with reduction
   - General 2nd order filter
5. Correct the following default settings:

   - Numerator frequency ([p1680](SINAMICS%20Parameter%20G220.md#p16800n-speed-actual-value-filter-5-numerator-natural-frequency))
   - Numerator damping ([p1681](SINAMICS%20Parameter%20G220.md#p16810n-speed-actual-value-filter-5-numerator-damping))
   - Denominator frequency ([p1678](SINAMICS%20Parameter%20G220.md#p16780n-speed-actual-value-filter-5-denominator-natural-frequency))
   - Denominator damping ([p1679](SINAMICS%20Parameter%20G220.md#p16790n-speed-actual-value-filter-5-denominator-damping))
6. Click "Apply" to apply the filter settings.
7. Once all necessary settings have been made, click "Close".

   The dialog closes.
8. In the "Natural frequency tuning" (c1655[4]) field, interconnect the signal source for the tuning of the natural frequency of actual speed value filter 5.

###### Result

You have configured the settings for the motor encoder. Save the settings in the project.

###### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/148900435083_DV_resource.Stream@PNG-de-DE.png) | [Speed controller](#configuring-the-speed-controller) |

###### Function diagrams (FD)

Speed actual value and pole position sensing motor encoder (encoder 1) - 4715 -

###### Additional parameters

- [r0061](SINAMICS%20Parameter%20G220.md#r006102-speed-actual-value-from-the-encoder)
- [r0063](SINAMICS%20Parameter%20G220.md#r006302-speed-actual-value)

---

### Drive functions

This section contains information on the following topics:

- [Brake control](#brake-control)
- [DC brake](#dc-brake)
- [Vdc-min/max controller](#vdc-minmax-controller)
- [Automatic restart](#automatic-restart)
- [Flying restart](#flying-restart)
- [Messages/monitoring](#messagesmonitoring)
- [Friction characteristic](#friction-characteristic)
- [Bypass operation](#bypass-operation)
- [Encoder functions](#encoder-functions)

#### Brake control

This section contains information on the following topics:

- [Description of function](#description-of-function-1)
- [Configuring brake control](#configuring-brake-control)

##### Description of function

###### Overview

A distinction is made between the mechanical and electrical brakes of a motor:

- Mechanical brakes are generally motor holding brakes that are closed when the motor is at a standstill.
- Mechanical operating brakes that are closed while the motor is rotating are subject to a high wear and are therefore often only used as an emergency brake.
- The motor is electrically braked by the converter. An electrical braking is completely wear-free.

SINAMICS G220 drives are equipped with a brake control for motor holding brakes.

Generally, a motor is switched off at standstill in order to save energy and so that the motor temperature is not unnecessarily increased. Drives that have been switched off, can be secured against unwanted motion by the holding brake.

The converter-internal control of the motor holding brake is suitable typically for horizontal, inclined and vertical conveyors. A motor holding brake can also be useful in several applications for pumps or fans to ensure that the switched-off motor does not rotate in the wrong direction due to a liquid or air flow.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Destruction of the motor holding brake due to incorrect parameter assignment**  If the drive moves against the closed motor holding brake, this can destroy the holding brake and cause death or serious injury.   - If there is a motor holding brake, do not set the parameter assignment [p1215](SINAMICS%20Parameter%20G220.md#p12150n-motor-holding-brake-configuration) = 0 (no motor holding brake available). - Set all the relevant parameters correctly. |  |

###### Method of operation

The brake control is only used for the control of motor holding brakes. The motor holding brake prevents drives from making unwanted motions when they are switched off.

The control command for releasing and applying the holding brake is transmitted directly to the converter via DRIVE-CLiQ from the Control Unit, which logically combines the signals with the system-internal processes and monitors these signals.

The converter then performs the action and activates the output for the motor holding brake accordingly. The exact sequential control is shown in function diagrams 2701 and 2704. The operating principle of the holding brake can be configured via parameter p1215.

![Sequence diagram, simple brake control](images/159838232203_DV_resource.Stream@PNG-en-US.png)

Sequence diagram, simple brake control

The start of the closing time for the brake depends on the expiration of the shorter of the two times [p1227](SINAMICS%20Parameter%20G220.md#p12270n-zero-speed-detection-monitoring-time) (standstill detection monitoring time) and [p1228](SINAMICS%20Parameter%20G220.md#p12280n-pulse-cancellation-delay-time) (Pulse cancellation delay time).

###### Function diagrams (FD)

Simple brake control - 2701 -

###### Additional parameters

- [r0056](SINAMICS%20Parameter%20G220.md#r0056015-status-word-closed-loop-control)
- [r0060](SINAMICS%20Parameter%20G220.md#r0060-speed-setpoint-before-the-setpoint-filter)
- [r0063](SINAMICS%20Parameter%20G220.md#r006302-speed-actual-value)
- [r0899](SINAMICS%20Parameter%20G220.md#r0899013-status-word-sequence-control)
- [p1216](SINAMICS%20Parameter%20G220.md#p12160n-motor-holding-brake-opening-time)
- [p1217](SINAMICS%20Parameter%20G220.md#p12170n-motor-holding-brake-closing-time)
- [p1226](SINAMICS%20Parameter%20G220.md#p12260n-threshold-for-zero-speed-detection)

---

##### Configuring brake control

###### Overview

The following types of brake control are available in the "Brake control" function view:

- [0] No motor holding brake available

  In this case, no configuration of the brake control is possible.

  | Symbol | Meaning |
  | --- | --- |
  |  | **Warning** |
  | **Destruction of the holding brake due to incorrect parameter assignment**  If the drive moves against the closed holding brake, this can destroy the holding brake and cause death or serious injury.  - Do **not** use parameterization [p1215](SINAMICS%20Parameter%20G220.md#p12150n-motor-holding-brake-configuration) = 0 **if there is a holding brake**. - Set all the relevant parameters correctly. |  |
- [3] Motor holding brake like sequential control system, connection via interconnection.

  If a motor holding brake is used via the drive-integrated brake connection of the converter, this option must not be set. If an external motor holding brake is used, p1215 = 3 should be set and [r0899](SINAMICS%20Parameter%20G220.md#r0899013-status-word-sequence-control).12 connected as control signal.

###### Requirements

- The drive has been completely created and fully specified in the device configuration.
- The [extended parameterization](#overview-2) is active.

  In the standard parameterization, only some of the settings described below can be made.

###### Procedure

To configure the brake control, proceed as follows:

1. Select the desired type of brake control from the "Configuration" drop-down list (see above).

   If the motor holding brake is to function like the sequential control system, further settings are possible:
2. Set the opening time of the brake ([p1216](SINAMICS%20Parameter%20G220.md#p12160n-motor-holding-brake-opening-time)).

   After activating the holding brake (opening), the speed/velocity setpoint zero is active during this time. The speed/velocity setpoint is then enabled after this time.

   The time should be set greater than the actual opening time of the brake. The drive does not then accelerate when the brake is closed.
3. Set the closing time of the brake ([p1217](SINAMICS%20Parameter%20G220.md#p12170n-motor-holding-brake-closing-time)).

   The drive still remains in closed-loop control at standstill with speed/velocity setpoint zero after OFF1 or OFF3 and activation of the holding brake (closing). The pulses are suppressed when this time expires.

   The time should be set greater than the actual closing time of the brake. In this way, the pulses are only suppressed when the brake is closed.
4. Click the "Open brake" button to open the "Open brake" dialog.
5. Interconnect the "Unconditionally release holding brake" (c0855) signal source for the command to release the brake unconditionally.

   The brake releases when this signal or the internal signal "Open brake" has the value "1".
6. Close the dialog and interconnect the signal sink "Open brake command" ([p0899](SINAMICS%20Parameter%20G220.md#r0899013-status-word-sequence-control).12) with the desired parameters. Several connections are possible.
7. To open the "Close brake" dialog, click the "Close brake" button.
8. Enter the speed threshold at which "Standstill" is identified when the threshold is undershot in the "Threshold" ([p1226](SINAMICS%20Parameter%20G220.md#p12260n-threshold-for-zero-speed-detection)) field.

   When this threshold is undershot, the brake control is started and the closing time in p1217 awaited. The pulses are then suppressed.
9. Enter the delay time for pulse cancellation in the "Delay time" ([p1228](SINAMICS%20Parameter%20G220.md#p12280n-pulse-cancellation-delay-time)) field.

   The pulses are suppressed after OFF1 or OFF3 when at least one of the following conditions has been satisfied:

   - The actual speed value falls below the threshold in p1226 and the time started in p1228 has expired.
   - The speed setpoint falls below the threshold in p1226 and the time started in [p1227](SINAMICS%20Parameter%20G220.md#p12270n-zero-speed-detection-monitoring-time) has expired.
10. Enter the monitoring time for standstill detection in the "Monitoring time" (p1227) field.

    When braking with OFF1 or OFF3, standstill is detected after this time has expired, after the set speed has fallen below p1226. The brake control is then started, the closing time in p1217 awaited and the pulses suppressed.
11. Interconnect the "Unconditionally close holding brake" (c0858) signal source for the command to unconditionally close the brake.
12. Close the dialog and interconnect the signal sink "Command close brake" (p0899.13) with the required parameters. Several connections are possible.

**Note**

The "Unconditionally close holding brake" signal has a higher priority than the "Unconditionally open holding brake" signal.

###### Result

Brake control is configured.

###### Function diagrams (FD)

Simple brake control - 2701 -

###### Additional parameters

---

#### DC brake

This section contains information on the following topics:

- [Description of function](#description-of-function-2)
- [Configuring armature short-circuit braking](#configuring-armature-short-circuit-braking)
- [Configuring DC braking for OFF1/OFF3](#configuring-dc-braking-for-off1off3)
- [Configuring DC braking below starting speed](#configuring-dc-braking-below-starting-speed)
- [Configuring fault responses](#configuring-fault-responses)
- [Configuring the current controller](#configuring-the-current-controller-1)

##### Description of function

###### Overview

You can parameterize either "DC braking" or "Armature short-circuit braking" via the "DC brake" function view irrespective of the motor type.

###### Requirements

- The drive has been completely created and fully specified in the device configuration.
- Do not use the braking function for pulling loads, as a mechanical brake is either not used or only used as a support, depending on the type of brake.

###### Armature short-circuit braking

Using this function, you can brake permanent-magnet synchronous motors. The stator windings of synchronous motors are then short-circuited. For a rotating synchronous motor, a current flows that brakes the motor.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Motor accelerates uncontrollably for pulling loads**  With pulling loads, for an armature short-circuit, the motor can uncontrollably accelerate if a mechanical brake is not additionally used. If the motor accelerates uncontrollably this can result in severe injury or death.  - With pulling loads, only use armature short-circuit braking to support a mechanical brake (a mechanical brake is mandatory). |  |

Armature short-circuit is preferably used in the following cases:

- If braking is to be performed without feedback
- If braking is to be performed when the power fails
- If an infeed is used that is not capable of feedback
- If with orientation loss (e.g. with encoder errors), the motor should still be braked

You can switch the armature short-circuit internally via the converter or externally using a contactor circuit with braking resistors.

The advantage of armature short-circuit braking over a mechanical brake is the response time of the internal armature short-circuit braking with just a few milliseconds. The response time of a mechanical brake is about 40 ms. For external armature short-circuit braking, the inertia of the switching contactor results in a response time of over 60 ms.

###### DC braking

Using this function, you can brake induction motors down to standstill. With DC braking, a DC current is injected in the stator windings of the induction motor.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Motor accelerates uncontrollably for pulling loads**  With pulling loads, when DC braking is used, during the demagnetization time the motor can accelerate uncontrollably. This can result in severe injury or death. An additional supporting mechanical brake is only closed after the demagnetization time - when the motor is already rotating - and therefore does not prevent the motor from accelerating uncontrollably.  - Do not use DC braking for pulling loads. |  |

DC braking is preferred in case of danger:

- If it is not possible to ramp-down the drive in a controlled fashion
- If an infeed not capable of feedback is used
- If no braking resistor is used

###### Function diagrams (FD)

External armature short-circuit (EASC, p0300 = 2xxx) - 7014 -

Internal armature short-circuit (IASC, p0300 = 2xxx) - 7016 -

DC braking (p0300 = 1xxx) - 7017 -

###### Additional parameters

---

##### Configuring armature short-circuit braking

###### Overview

For internal armature short-circuit braking, the stator windings of the synchronous motors are short-circuited. For a rotating synchronous motor, a current flows that brakes the motor.

###### Requirements

- The drive has been completely created and fully specified in the device configuration.
- Short-circuit-proof motors ([p0320](SINAMICS%20Parameter%20G220.md#p03200n-motor-rated-magnetizing-currentshort-circuit-current) < [p0323](SINAMICS%20Parameter%20G220.md#p03230n-maximum-motor-current)) are used.
- One of the following motor types is used:

  - Rotary permanent-magnet synchronous motor ([p0300](SINAMICS%20Parameter%20G220.md#p03000n-motor-type-selection) = 2xx)
  - Linear permanent-magnet synchronous motor (p0300 = 4xx)
- The maximum current of the converter ([r0209](SINAMICS%20Parameter%20G220.md#r020902-power-unit-maximum-current).0) must be at least 1.8-times the motor short-circuit current ([r0331](SINAMICS%20Parameter%20G220.md#r03310n-actual-motor-magnetizing-currentshort-circuit-current)).

  > **Note**
  >
  > **Internal short-circuit braking despite power failure**
  >
  > If armature short-circuit braking should still be maintained despite a voltage failure, you must buffer the 24 V power supply for the converter. For this purpose, you can use, for example, a dedicated SITOP unit for the converter or a Control Supply Module (CSM).
- The [extended parameterization](#overview-2) is active.

  In the standard parameterization, only some of the settings described below can be made.

###### Procedure

1. In drop-down list "Braking configuration", select option "[4] DC braking/Armature short-circuit internal" ([p1231](SINAMICS%20Parameter%20G220.md#p12310n-dc-brakingarmature-short-circuit-configuration)).
2. Enter the desired braking current value in the "Braking current" ([p1232](SINAMICS%20Parameter%20G220.md#p12320n-dc-braking-braking-current)) field.
3. Enter an appropriate time in the "Motor de-excitation time" ([p0347](SINAMICS%20Parameter%20G220.md#p03470n-motor-de-excitation-time)) field.
4. If necessary, configure the desired fault response of the encoder (see "[Configuring fault responses](#configuring-fault-responses)").
5. If required, configure the values of the current controller (see "[Configuring the current controller](#configuring-the-current-controller-1)").
6. Interconnect the signal source "Braking activation" (c1230) for the activation of the armature short-circuit or DC braking.

###### Result

As soon as the signal source of c1230 is set to "1" signal, the function is activated and triggered. The braking can be stopped again via the "0" signal.

###### Additional parameters

---

##### Configuring DC braking for OFF1/OFF3

###### Overview

With the function "DC braking", after a demagnetization time, a DC current is injected in the stator windings of the induction motor. The DC current brakes the motor.

With this DC braking, the braking is set as a response to OFF1 or OFF3.

###### Requirements

- The drive has been completely created and fully specified in the device configuration.
- An induction motor is used.
- The [extended parameterization](#overview-2) is active.

  In the standard parameterization, only some of the settings described below can be made.

###### Procedure

1. Select the "[5] DC braking for OFF1/OFF3" option ([p1231](SINAMICS%20Parameter%20G220.md#p12310n-dc-brakingarmature-short-circuit-configuration)) in the "Braking configuration" drop-down list.
2. Correct the specified default value in the "Start speed" ([p1234](SINAMICS%20Parameter%20G220.md#p12340n-speed-at-the-start-of-dc-braking)) field.
3. Enter the desired braking current value in the "Braking current" ([p1232](SINAMICS%20Parameter%20G220.md#p12320n-dc-braking-braking-current)) field.
4. Enter an appropriate time in the "Motor de-excitation time" ([p0347](SINAMICS%20Parameter%20G220.md#p03470n-motor-de-excitation-time)) field.
5. Enter an appropriate time in the "Duration" ([p1233](SINAMICS%20Parameter%20G220.md#p12330n-dc-braking-time)) field.
6. If necessary, configure the desired fault response of the encoder (see "[Configuring fault responses](#configuring-fault-responses)").
7. If required, configure the values of the current controller (see "[Configuring the current controller](#configuring-the-current-controller-1)").

###### Result

If the motor speed is above the starting speed, the motor speed is reduced until it is below the starting speed. When the speed is below the starting speed, the pulses are disabled and the motor is demagnetized. DC braking is then activated for the specified duration and is then switched off.

###### Additional parameters

---

##### Configuring DC braking below starting speed

###### Overview

With the function "DC braking", after a demagnetization time, a DC current is injected in the stator windings of the induction motor. The DC current brakes the motor.

With this DC braking, this function is triggered as soon as the actual speed falls below the starting speed of the DC braking ([p1234](SINAMICS%20Parameter%20G220.md#p12340n-speed-at-the-start-of-dc-braking)).

###### Requirements

- The drive has been completely created and fully specified in the device configuration.
- An induction motor is used.
- The [extended parameterization](#overview-2) is active.

  In the standard parameterization, only some of the settings described below can be made.

###### Procedure

1. Select the "[14] DC braking below starting speed" option ([p1231](SINAMICS%20Parameter%20G220.md#p12310n-dc-brakingarmature-short-circuit-configuration)) in the "Braking configuration" drop-down list.
2. Correct the specified default value in the "Start speed" (p1234) field.
3. Enter the desired braking current value in the "Braking current" ([p1232](SINAMICS%20Parameter%20G220.md#p12320n-dc-braking-braking-current)) field.
4. Enter an appropriate time in the "Motor de-excitation time" ([p0347](SINAMICS%20Parameter%20G220.md#p03470n-motor-de-excitation-time)) field.
5. Enter an appropriate time in the "Duration" ([p1233](SINAMICS%20Parameter%20G220.md#p12330n-dc-braking-time)) field.
6. If necessary, configure the desired fault response of the encoder (see "[Configuring fault responses](#configuring-fault-responses)").
7. If required, configure the values of the current controller (see "[Configuring the current controller](#configuring-the-current-controller-1)").
8. Interconnect the signal source "Braking activation" (c1230) for the activation of the armature short-circuit or DC braking.

###### Result

If the actual speed falls below the starting speed, all pulses are disabled. This demagnetizes the motor. DC braking is then initiated for the set duration.

###### Additional parameters

---

##### Configuring fault responses

###### Overview

You can configure the fault responses for the armature short-circuit braking and the DC braking.

###### Requirement

- The drive has been completely created and fully specified in the device configuration.

###### Procedure

1. Click the "Fault response" button.

   The configuration dialog with the same name opens. A fault response can be configured for each line in the configuration table.
2. Click in the line of the fault that you want to configure.
3. Enter a number for selected fault in the "Fault number" ([p2100](SINAMICS%20Parameter%20G220.md#p2100019-change-fault-response-fault-number)) field of this line.
4. Select the desired fault response to the fault in this line in the "Fault response" ([p2101](SINAMICS%20Parameter%20G220.md#p2101019-change-fault-response-response)) column.
5. Repeat steps 2 to 4 for further fault that you want to configure.
6. Once all necessary settings have been made, click "Close".

###### Introduction

The fault responses are parameterized. The dialog closes.

###### Additional parameters

---

##### Configuring the current controller

###### Overview

Configure the respective important parameters of the current controller for armature short-circuit braking and DC braking.

###### Requirements

- The drive has been completely created and fully specified in the device configuration.
- The [extended parameterization](#overview-2) is active.

  In the standard parameterization, the "Current controller" dialog cannot be parameterized.

###### Procedure

1. Click the "Current controller" button in the "DC braking" function view.

   The dialog box with the same name opens:
2. If required, correct the specified values in the following fields:

   - P gain ([p1345](SINAMICS%20Parameter%20G220.md#p13450n-i_max-voltage-controller-proportional-gain))
   - Integral time ([p1346](SINAMICS%20Parameter%20G220.md#p13460n-i_max-voltage-controller-integral-time))
   - Braking current ([p1232](SINAMICS%20Parameter%20G220.md#p12320n-dc-braking-braking-current))
3. Once all necessary settings have been made, click "Close".

###### Result

The current controller is configured. The dialog closes.

###### Additional parameters

---

#### Vdc-min/max controller

This section contains information on the following topics:

- [Description of function](#description-of-function-3)
- [Configuring Vdc-min/max control](#configuring-vdc-minmax-control)

##### Description of function

###### Overview

The "Vdc control" function can be activated using the appropriate measures if an overvoltage or undervoltage is present in the DC link.

Measures against overvoltage and undervoltage:

| Deviation | Typical cause | Remedy |
| --- | --- | --- |
| Overvoltage | The drive is operating in regenerative mode and is supplying too much energy to the DC link. | Reduce the regenerative torque to maintain the DC-link voltage within permissible limits. With the Vdc controller activated, the converter sometimes automatically extends the ramp-down time of a drive if the shutdown supplies too much energy to the DC link. |
| Undervoltage | Failure of the line voltage or supply for the DC link. | Specify a regenerative torque for the rotating drive to compensate the existing losses, thereby stabilizing the voltage in the DC link. This process is called "kinetic buffering". |

Properties:

| Control mode | Properties |
| --- | --- |
| Vdc | - This comprises Vdc_max control and Vdc_min control (kinetic buffering), which are independent of each other. - Joint PI controller. The dynamic factor is used to set Vdc_min and Vdc_max control independently of each other. |
| Vdc_max | - This function can be used to control momentary regenerative load without shutdown using "overvoltage in the DC link". - Vdc_max control is only recommended for a supply without active closed-loop control for the DC link and without feedback. |
| Vdc_min  (kinetic buffering) | - With this function, the kinetic energy of the motor is used for buffering the DC-link voltage in the event of a momentary power failure, thereby delaying the drive. |

###### Vdc_min control

![Switching Vdc_min control on/off (kinetic buffering)](images/148901006859_DV_resource.Stream@PNG-en-US.png)

Switching V<sub>dc_min</sub> control on/off (kinetic buffering)

In the event of a power failure, Vdc_min control is activated when the Vdc_min switch-on level is undershot. This controls the DC-link voltage and maintains it at a constant level. The motor speed is reduced.

When the power supply is restored, the DC-link voltage increases again and Vdc_min control is deactivated again at 5% above the Vdc_min switch-on level. The motor continues operating normally.

If the power supply is not re-established, the motor speed continues to drop. When the threshold in [p1257](SINAMICS%20Parameter%20G220.md#p12570n-vdc_min-controller-speed-threshold) is reached, this results in a response in accordance with [p1256](SINAMICS%20Parameter%20G220.md#p12560n-vdc_min-controller-response-kinetic-buffering).

Once the time threshold ([p1255](SINAMICS%20Parameter%20G220.md#p12550n-vdc_min-controller-time-threshold)) has elapsed without the line voltage being re-established, a fault is triggered (F07406), which can be parameterized as required (factory setting: OFF3).

The Vdc_min controller can be activated for a drive. Other drives can participate in supporting the DC link, by transferring to them a scaling of their speed setpoint from the controlling drive via signal interconnection.

> **Note**
>
> If it is expected that the line supply will return, you must make sure that the drive lineup is not disconnected from the power supply. It could become disconnected, for example, if the line contactor drops out. The line contactor must be supplied, e.g. from an uninterruptible power supply (UPS).

###### Vdc_max control

![Switching Vdc_max control on/off](images/148900981259_DV_resource.Stream@PNG-en-US.png)

Switching Vdc_max control on/off

The switch-on level for Vdc_max control ([r1242](SINAMICS%20Parameter%20G220.md#r1242-vdc_max-controller-switch-in-level)) is calculated as follows:

- When the function for automatically detecting the switch-on level is switched off ([p1254](SINAMICS%20Parameter%20G220.md#p1254-vdc_max-controller-automatic-on-level-detection) = 0)  
  r1242 = 1.15 • [p0210](SINAMICS%20Parameter%20G220.md#p0210-device-supply-voltage) (device connection voltage, DC link)
- When the function for automatically detecting the switch-on level is switched on (p1254 = 1)  
  r1242 = Vdc_max - 50 V (Vdc_max: overvoltage threshold of the converter)

###### Function diagrams (FD)

Vdc_max controller and Vdc_min controller - 6220 -

###### Additional parameters

---

##### Configuring Vdc-min/max control

###### Requirements

- The drive has been completely created and fully specified in the device configuration.
- The [extended parameterization](#overview-2) is active.

###### Making basic settings

1. Select the required control type in the "Vdc controller or Vdc monitoring configuration ..." ([p1240](SINAMICS%20Parameter%20G220.md#p12400n-vdc-controller-or-vdc-monitoring-configuration)/[p1280](SINAMICS%20Parameter%20G220.md#p12800n-vdc-controller-or-vdc-monitoring-configuration-uf)) drop-down list.

   Depending on the control type that is selected, the schematic display and the necessary detailed settings change.
2. Make the detailed settings of the selected control type (see below)
3. Save the project settings.

###### Detailed settings "Disable Vdc controller"

No settings are possible for the disabled Vdc controller.

###### Detailed settings "Enable Vdc_max controller"

1. Click the "Switch-on level Vdc_max" button.

   The "Switch-on level Vdc_max" dialog opens.
2. Select whether the automatic acquisition is enabled or disabled in the "Automatic acquisition ON signal level" ([p1254](SINAMICS%20Parameter%20G220.md#p1254-vdc_max-controller-automatic-on-level-detection)) drop-down list.
3. If required, correct the default value in the "Device supply voltage" ([p0210](SINAMICS%20Parameter%20G220.md#p0210-device-supply-voltage)) field.

   The device supply voltage can only be parameterized with disabled automatic acquisition.
4. Once all necessary settings have been made, click "Close".

   The dialog closes.
5. Click the "Vdc-max controller" button.

   The "Vdc-min/max controller" dialog opens.
6. If required, correct the default values in the following fields:

   - Proportional gain ([p1250](SINAMICS%20Parameter%20G220.md#p12500n-vdc_max-controller-proportional-gain)[0])
   - Integral time ([p1251](SINAMICS%20Parameter%20G220.md#p12510n-vdc_max-controller-integral-time)[0])
   - Derivative-action time ([p1252](SINAMICS%20Parameter%20G220.md#p12520n-vdc_max-ctrl-rate-time)[0])
7. Once all necessary settings have been made, click "Close".

   The dialog closes.
8. Enter the dynamic response factor as percentage in the input field ([p1243](SINAMICS%20Parameter%20G220.md#p12430n-vdc_max-controller-dynamic-factor)) below the "Vdc-max controller" button.

###### Detailed settings "Enable Vdc_min controller (kinetic buffering)"

1. Click the "Switch-on level Vdc_min" button.

   The "Switch-on level Vdc_min" dialog opens.
2. Select how the Vdc_min controller should respond in the "Vdc_min controller response (kinetic buffering)" ([p1256](SINAMICS%20Parameter%20G220.md#p12560n-vdc_min-controller-response-kinetic-buffering)) drop-down list.
3. If required, correct the default values in the following fields:

   - Switch-on level ([p1245](SINAMICS%20Parameter%20G220.md#p12450n-vdc_min-controller-switch-in-level-kinetic-buffering))
   - Speed threshold ([p1257](SINAMICS%20Parameter%20G220.md#p12570n-vdc_min-controller-speed-threshold))
   - Time threshold ([p1255](SINAMICS%20Parameter%20G220.md#p12550n-vdc_min-controller-time-threshold))

     Can only be parameterized for Vdc_min controller response [1].
4. Once all necessary settings have been made, click "Close".

   The dialog closes.
5. Click the "Vdc_min controller" button.

   The "Vdc-min/max controller" dialog opens.
6. If required, correct the default values in the following fields:

   - Proportional gain (p1250)
   - Integral time (p1251)
   - Derivative-action time (p1252)
7. Once all necessary settings have been made, click "Close".

   The dialog closes.
8. Enter the dynamic response factor as percentage in the input field ([p1247](SINAMICS%20Parameter%20G220.md#p12470n-vdc_min-controller-dynamic-factor-kinetic-buffering)) below the "Vdc_min controller" button.

###### Detailed settings "Enable the Vdc_min controller and Vdc_max controller"

1. Click the "Switch-on level Vdc_max" button.

   The "Switch-on level Vdc_max" dialog opens.
2. Select whether the automatic acquisition is enabled or disabled in the "Automatic acquisition ON signal level" (p1254) drop-down list.
3. If required, correct the default value in the "Device supply voltage" (p0210) field.

   The device supply voltage can only be parameterized with disabled automatic acquisition.
4. Once all necessary settings have been made, click "Close".

   The dialog closes.
5. Click the "Vdc-max controller" button.

   The "Vdc-min/max controller" dialog opens.
6. If required, correct the default values in the following fields:

   - Proportional gain (p1250)
   - Integral time (p1251)
   - Derivative-action time (p1252)
7. Once all necessary settings have been made, click "Close".

   The dialog closes.
8. Enter the dynamic response factor as percentage in the input field (p1243) below the "Vdc-max controller" button.
9. Click the lower "Switch-on level Vdc_min" button.

   The "Switch-on level Vdc_min" dialog opens.
10. Select how the Vdc_min controller should respond in the "Vdc_min controller response (kinetic buffering)" (p1256) drop-down list.
11. If required, correct the default values in the following fields:

    - Switch-on level (p1245)
    - Speed threshold (p1257)
    - Time threshold (p1255)

      Can only be parameterized for Vdc_min controller response [1].
12. Once all necessary settings have been made, click "Close".

    The "Switch-on level" dialog closes.
13. Click the "Vdc_min controller" button.

    The "Vdc-min/max controller" dialog opens.
14. If required, correct the default values in the following fields:

    - Proportional gain (p1250)
    - Integral time (p1251)
    - Derivative-action time (p1252)
15. Once all necessary settings have been made, click "Close".

    The dialog closes.

###### Detailed settings "Activate Vdc_max monitoring"

1. Click the "Switch-on level Vdc_max" button.

   The "Switch-on level Vdc_max" dialog opens.
2. Select whether the automatic acquisition is enabled or disabled in the "Automatic acquisition ON signal level" (p1254) drop-down list.
3. Correct the default value in the "Device supply voltage:" (p0210) field.

   The device supply voltage can only be parameterized with disabled automatic acquisition.
4. Once all necessary settings have been made, click "Close".

   The dialog closes.

###### Detailed settings "Activate Vdc_min monitoring"

1. Click the "Switch-on level Vdc_min" button.

   The "Switch-on level Vdc_min" dialog opens.
2. Select how the Vdc_min controller should respond in the "Vdc_min controller response (kinetic buffering)" (p1256) drop-down list.
3. Correct the default values in the following fields:

   - Switch-on level (p1245)
   - Speed threshold (p1257)
   - Time threshold (p1255)

     Can only be parameterized for Vdc_min controller response [1].
4. Once all necessary settings have been made, click "Close".

   The dialog closes.

###### Detailed settings "Activate Vdc_min monitoring and Vdc_max monitoring"

1. Click the "Switch-on level Vdc_max" button.

   The "Switch-on level Vdc_max" dialog opens.
2. Select whether the automatic acquisition is enabled or disabled in the "Automatic acquisition ON signal level" (p1254) drop-down list.
3. Correct the default value in the "Device supply voltage:" (p0210) field.

   The device supply voltage can only be parameterized with disabled automatic acquisition.
4. Once all necessary settings have been made, click "Close".

   The dialog closes.
5. Click the "Switch-on level Vdc_min" button.

   The "Switch-on level Vdc_min" dialog opens.
6. Select how the Vdc_min controller should respond in the "Vdc_min controller response (kinetic buffering)" (p1256) drop-down list.
7. Correct the default values in the following fields:

   - Switch-on level (p1245)
   - Speed threshold (p1257)
   - Time threshold (p1255)

     Can only be parameterized for Vdc_min controller response [1].
8. Once all necessary settings have been made, click "Close".

   The dialog closes.

###### Result

The desired Vdc-min/max control is enabled and configured.

###### Function diagrams (FD)

Vdc_max controller and Vdc_min controller - 6220 -

###### Additional parameters

- [r1242](SINAMICS%20Parameter%20G220.md#r1242-vdc_max-controller-switch-in-level)
- [r1246](SINAMICS%20Parameter%20G220.md#r1246-vdc_min-controller-switch-in-level-kinetic-buffering)
- [r1254](SINAMICS%20Parameter%20G220.md#p1254-vdc_max-controller-automatic-on-level-detection)
- [r1258](SINAMICS%20Parameter%20G220.md#r1258-vdc-controller-output)

---

#### Automatic restart

This section contains information on the following topics:

- [Configuring the automatic restart](#configuring-the-automatic-restart)

##### Configuring the automatic restart

###### Overview

The automatic restart function automatically restarts the drive after an undervoltage or a power failure. The pending alarms are acknowledged and the drive is restarted automatically.

The drive can be restarted in two ways:

- Normal start of the drive starting from standstill.
- Starting the drive with the "Flying restart" function.

  For drives with low inertia loads and load torques where the drive can be brought to a standstill within seconds (such as pump drives with water gauges), the start from standstill is recommended.

If the automatic restart function is activated ([p1210](SINAMICS%20Parameter%20G220.md#p1210-automatic-restart-mode) > 1), the motor can be started automatically when the line supply is restored. This is especially critical, if, after longer line supply failures, motors come to a standstill and it is incorrectly assumed that they have been powered down.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Unplanned movements when the automatic restart function is active**  When the automatic restart is activated, unexpected movements can occur that may result in death or serious injury when the line supply returns.   - Take the appropriate measures on the plant side so that there is no safety risk as a result of an unexpected restart. |  |

###### Automatic restart mode

| Mode (p1210) | Meaning |
| --- | --- |
| [0] Inhibit automatic restart | Automatic restart inactive |
| [1] Acknowledge all faults without restarting | Any faults are automatically acknowledged. If further faults occur after faults have been acknowledged, they will also be acknowledged automatically. [p1211](SINAMICS%20Parameter%20G220.md#p1211-automatic-restart-start-attempts) has no influence on the number of acknowledgement attempts. |
| [4] Restart after line supply failure without additional start attempts | An automatic restart is only performed if fault F30003 occurred on the power unit. If additional faults are pending, then these faults will also be acknowledged; if this is successful, the startup attempt will be resumed. If, for external 24 V power supplies of the Control Unit, further faults subsequently occur, these are no longer interpreted as line faults and are therefore also not acknowledged. |
| [6] Restart after fault with additional start attempts | An automatic restart is performed after any fault. If the faults occur one after the other, then the number of startup attempts is defined in p1211. Monitoring over time can be set using [p1213](SINAMICS%20Parameter%20G220.md#p121301-automatic-restart-monitoring-time). |
| [14] Restart after line supply failure following manual acknowledgment | As for 4: However, pending faults must be acknowledged manually. This is then followed by an automatic restart. |
| [16] Restart after fault following manual acknowledgment | As for 6: However, pending faults must be acknowledged manually. This is then followed by an automatic restart. |
| [26] Acknowledging all faults and reclosing for an ON command | As for 6: For this mode, the switch-on command can be entered with a delay. The restart is aborted with OFF2 or OFF3. Warning A07321 is only displayed when the cause of the fault has been eliminated and the unit is switched on again by setting the switch-on command. |

###### Requirement

- The drive has been completely created and fully specified in the device configuration.

###### Procedure

1. Select the restart mode that you want to use in the "Automatic restart mode" (p1210) drop-down list (see table above).

   The following input fields depend on the set mode of the restart and are displayed dynamically. If available, you can also make the following additional settings:
2. Enter the desired delay time until the restart in the "Delay time start attempts" ([p1212](SINAMICS%20Parameter%20G220.md#p1212-automatic-restart-wait-time-acknowledgment-and-start-attempt)) field.
3. Mode (1/4/6/14/16/26):   
   Enter a monitoring time for the restart in the "Restart" (p1213[0]) field.
4. Mode (1/4/6/14/16/26):   
   Enter the wait time after which the start counter is to be reset in the "Reset start counter" (p1213[1]) field.
5. Mode (6/16):   
   Enter the number of desired start attempts in the "Start attempts" (p1211) field.

###### Example

![Typical automatic restart procedure](images/159833412363_DV_resource.Stream@PNG-en-US.png)

Typical automatic restart procedure

###### Result

Depending on the set mode, either only the fault is acknowledged or the drive is also switched on again.

To prevent the motor from switching to phase opposition when the drive is being restarted, there is a delay while the motor demagnetizes (t = 2.3 x motor magnetization time constant). Once this time has elapsed, the inverter is enabled and the motor is supplied with power.

###### Additional parameters

- [r0863](SINAMICS%20Parameter%20G220.md#r086301-drive-coupling-status-wordcontrol-word)
- [p1206](SINAMICS%20Parameter%20G220.md#p120609-automatic-restart-faults-not-active)
- [r1214](SINAMICS%20Parameter%20G220.md#r1214015-automatic-restart-status)

---

#### Flying restart

This section contains information on the following topics:

- [Configuring flying restart](#configuring-flying-restart)

##### Configuring flying restart

###### Overview

The "Flying restart" function allows a converter to be switched on for a running motor. The output frequency of the converter is changed until the actual motor speed/velocity is found. The motor then ramps up with the setting for the ramp-function generator to the setpoint. The "Flying restart" function can be activated during operation with or without an encoder.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Unplanned movement of the motor when flying restart is activated**  When the "flying restart" ([p1200](SINAMICS%20Parameter%20G220.md#p12000n-flying-restart-operating-mode)) function is activated, the drive can still be accelerated by the search current despite the fact that it is at standstill and the setpoint is "0"; this can result in death, severe injury or material damage.   - Ensure that nobody is present in the hazardous zone and that the mechanical system can move freely. |  |

###### Requirement

- The drive has been completely created and fully specified in the device configuration.

###### Procedure

1. Select the desired mode of the flying restart in the "Flying restart operating mode" (p1200) drop-down list in the "Flying restart" function view:

   - [0] Flying restart inactive (no further settings are possible with this setting)
   - [1] Flying restart always active (start in setpoint direction)
   - [4] Flying restart always active (start only in setpoint direction)
2. If required, enter the maximum frequency for the flying restart in the "Flying restart maximum frequency inhibited direction" ([p1271](SINAMICS%20Parameter%20G220.md#p12710n-flying-restart-maximum-frequency-for-the-inhibited-direction)) field.
3. Interconnect the signal for enabling or starting flying restart in the "Flying restart enable" (c1201) field.

   The removal of the enable signal also deactivates the flying restart.
4. Save the project settings.

**Note**

The "Flying restart enable" (c1201) signal source is interconnected with 1 by default. You can interconnect a different signal source here. You can briefly deactivate the "Flying restart" function via an interconnection with 0 (acts as p1200 = 0), but retain the other settings on this function view.

###### Result

- With an induction motor, the system waits for a demagnetization time to elapse before the search is carried out. The demagnetization time can reduce the voltage at the motor terminals. At the pulse enable, this avoids high equalizing currents due to a phase short-circuit.

  The internal demagnetization time is calculated. In addition, you can define a de-excitation time via parameter [p0347](SINAMICS%20Parameter%20G220.md#p03470n-motor-de-excitation-time). The system waits for the longer of the two times to elapse. When operated with an encoder (actual speed value is sensed), the search phase is eliminated.
- For an induction or reluctance motor, immediately after the speed has been determined, magnetization starts ([p0346](SINAMICS%20Parameter%20G220.md#p03460n-motor-excitation-build-up-time)).

  The current speed setpoint in the ramp-function generator is then set to the current actual speed value.

  The ramp-up to the final speed setpoint starts with this value.

###### Additional parameters

- [p0247](SINAMICS%20Parameter%20G220.md#p024709-voltage-measurement-configuring)
- [p0352](SINAMICS%20Parameter%20G220.md#p03520n-cable-resistance)
- [p1082](SINAMICS%20Parameter%20G220.md#p10820n-maximum-speed)

---

#### Messages/monitoring

This section contains information on the following topics:

- [Actual speed value alarms](#actual-speed-value-alarms)
- [Speed messages](#speed-messages)
- [Setpoint / actual value messages](#setpoint-actual-value-messages)
- [Blocking message](#blocking-message)
- [Variable signaling function](#variable-signaling-function)
- [Stall message](#stall-message)
- [Load torque monitoring](#load-torque-monitoring)
- [Motor temperature](#motor-temperature)

##### Actual speed value alarms

###### Overview

Comparators are provided for monitoring the actual speed and setpoint thresholds that based on these threshold values activate monitoring functions (e.g. air flow monitor for fans, pressure switch for pumps) or initiate product steps for other plant sections (e.g. open feeder valves for pumps and fans). The monitoring of actual speed value thresholds and setpoint thresholds can be configured using the "Actual speed value alarms" function view.

###### Requirements

- The drive has been completely created and fully specified in the device configuration.
- The [extended parameterization](#overview-2) is active.

  In the standard parameterization, only minimal settings are possible.

###### Procedure

1. Enter the time constant of the PT1 element for smoothing the actual speed/velocity value in the "Smoothing" ([p2153](SINAMICS%20Parameter%20G220.md#p21530n-speed-actual-value-filter-time-constant)) field.

   The smoothed actual speed/velocity is compared with the thresholds and is only used for messages.
2. In field "Hysteresis speed 1" ([p2142](SINAMICS%20Parameter%20G220.md#p21420n-hysteresis-speed-1)), enter the hysteresis speed (bandwidth) for message "f or n comparison value reached or exceeded" (binary signal source: [r2199](SINAMICS%20Parameter%20G220.md#r2199011-status-word-monitoring-3).1).
3. Interconnect the "f or n comparison value reached or exceeded" (r2199) signal sink with the required parameters. Several interconnections are possible.

   Interconnect binary signal sink:

   The "f or n comparison value reached/exceeded" signal is generated under consideration of hysteresis speed 1, speed threshold 1 and the ON delay.
4. Enter the speed threshold 1 in the "Speed threshold 1" ([p2141](SINAMICS%20Parameter%20G220.md#p21410n-speed-threshold-1)) field.
5. Enter the ON delay time for signal |n_act| > speed threshold in the "ON delay" ([p2156](SINAMICS%20Parameter%20G220.md#p21560n-on-delay-comparison-value-reached)) field.
6. Enter the bandwidths for the following messages in the "Hysteresis speed 2" ([p2140](SINAMICS%20Parameter%20G220.md#p21400n-hysteresis-speed-2)) field:

   - |n_act| < speed threshold 2
   - |n_set| > speed threshold 2
7. Interconnect the following signal sinks with the required parameters:

   - |n_act| ≤ speed threshold 2
   - |n_act| > speed threshold 2
8. Enter speed threshold 2 in the "Speed threshold 2" ([p2155](SINAMICS%20Parameter%20G220.md#p21550n-speed-threshold-2)) field.
9. Enter the bandwidths for the n_act > n_max message in the "Hysteresis speed n_act > n_max" ([p2162](SINAMICS%20Parameter%20G220.md#p21620n-hysteresis-speed-n_act-n_max)) field.
10. Interconnect the "|n_act| > n_max" ([r2197](SINAMICS%20Parameter%20G220.md#r2197013-status-word-monitoring-1)) signal sink with the required parameters. Several interconnections are possible.

    Interconnect binary signal sink:

    Signal n_act > n_max is generated under consideration of hysteresis speed n_act > n_max.

    For a negative speed limit, the hysteresis is effective below the limit value and for a positive speed limit, above the limit value.

    Note:  
    The limits are set in the setpoint channel; see also [Speed limiting](#speed-limiting).

###### Result

You have configured the actual speed value alarms. Save the settings in the project.

###### Function diagrams (FD)

Speed signals (Part 1) - 8010 -

Speed signals (Part 2) - 8011 -

###### Additional parameters

---

##### Speed messages

###### Overview

Comparators are provided for monitoring the speed thresholds used to activate monitoring functions (e.g. air flow monitor for fans, pressure switch for pumps) or initiate product steps for other plant sections (e.g. open gates for pumps and fans).

###### Requirements

- The drive has been completely created and fully specified in the device configuration.
- The [extended parameterization](#overview-2) is active.

###### Procedure

You can set the speed signals as follows:

1. Correct the specified bandwidths for the following messages in the "Hysteresis speed 3" ([p2150](SINAMICS%20Parameter%20G220.md#p21500n-hysteresis-speed-3)[0]) field:

   - n_act ≥ 0
   - |n_act| < speed threshold value 3
   - n_set < [p2161](SINAMICS%20Parameter%20G220.md#p21610n-speed-threshold-3)
   - n_set ≥ 0

   The calculation mode is defined using p0340.
2. Interconnect the following signal sinks. Several interconnections are possible in each case.

   - n_act ≥ 0

     Signal "n_act ≥ 0" is generated considering hysteresis speed 3.
   - |n_act| < speed threshold value 3

     Signal |n_act| < speed threshold 3 is generated considering hysteresis speed 3 and speed threshold 3.
   - n_set < p2161
   - n_set ≥ 0
3. Correct the speed threshold 3 for |n_act| < speed setpoint 3 in the "Speed threshold 3" (p2161) field.
4. Interconnect the "Speed setpoint for messages" (c2151) signal source for speed setpoint messages.
5. Interconnect the "Speed setpoint 2" (c2154) signal source.

###### Result

You have configured the speed messages. Save the settings in the project.

###### Function diagrams (FD)

Speed signals (Part 1) - 8010 -

Speed signals (Part 2) - 8011 -

###### Additional parameters

---

##### Setpoint / actual value messages

###### Overview

Comparators are provided for monitoring the actual speed and setpoint thresholds that activate monitoring functions (e.g. air flow monitor for fans, pressure switch for pumps) or initiate product steps for other plant sections (e.g. open gates for pumps and fans).

###### Requirements

- The drive has been completely created and fully specified in the device configuration.
- The [extended parameterization](#overview-2) is active.

###### Procedure

1. Correct the specified bandwidth for the "Speed setp - act val deviation in tolerance t_off" message in the "Hysteresis speed 4" ([p2164](SINAMICS%20Parameter%20G220.md#p21640n-hysteresis-speed-4)) field.
2. Correct the specified speed threshold in the "Speed threshold 4" ([p2163](SINAMICS%20Parameter%20G220.md#p21630n-speed-threshold-4)) field.
3. Correct the OFF delay time for the "Speed setpoint - actual value deviation in tolerance t_off" message in the "OFF delay" ([p2166](SINAMICS%20Parameter%20G220.md#p21660n-off-delay-n_act-n_set)) field.
4. Interconnect the "Setpoint - actual value deviation in tolerance t_off" ([r2197](SINAMICS%20Parameter%20G220.md#r2197013-status-word-monitoring-1).7) signal sink for displaying the 1st monitoring status word.
5. Correct the ON delay time for the "Speed setpoint - actual value deviation in tolerance t_off" signal in the "ON delay" ([p2167](SINAMICS%20Parameter%20G220.md#p21670n-switch-on-delay-n_act-n_set)) field.
6. Interconnect the "Ramp-function generator active" (c2148) signal source for the "Ramp-function generator active" signal for the following messages:

   - Speed setp - act val deviation in tolerance t_on
   - Ramp-up/ramp-down completed
7. Interconnect the "Setpoint - actual value deviation in tolerance t_on" ([r2199](SINAMICS%20Parameter%20G220.md#r2199011-status-word-monitoring-3).4) signal sink for displaying the monitoring 3 status word.
8. Interconnect the "Ramp-up/ramp-down completed" (r2199.5) signal sink for displaying the monitoring 3 status word.

###### Result

You have configured the setpoint/actual value alarms. Save the settings in the project.

###### Function diagrams (FD)

Speed signals (Part 1) - 8010 -

Speed signals (Part 2) - 8011 -

###### Additional parameters

---

##### Blocking message

###### Overview

If a motor blocks, when a freely set speed threshold ([p2175](SINAMICS%20Parameter%20G220.md#p21750n-motor-blocked-speed-threshold)) is undershot, the message "F07900 (N, A) drive: motor blocks" is issued after expiration of a delay time ([p2177](SINAMICS%20Parameter%20G220.md#p21770n-motor-blocked-delay-time)). The speed threshold and the delay time for the message can be configured in the "Blocking message" function view.

###### Requirements

- The drive has been completely created and fully specified in the device configuration.
- The [extended parameterization](#overview-2) is active.
- With U/f control activated (see [Operating mode](#operating-mode-1)), the current limit must be reached.

###### Procedure

1. Interconnect the "Stall monitoring enable (negated)" (c2144) signal source for the negated enable of the stall monitoring (0 = enable).
2. Correct the specified "Speed threshold" (p2175) value.

   If this speed threshold is overshot, the message "F07900 (N, A) drive: motor blocks" is issued.
3. Correct the specified delay time in the "Delay time" (p2177) field.

   The message "F07900 (N, A) drive: motor blocks" message is issued after expiration of this delay time.
4. Interconnect the "Motor blocked" ([r2198](SINAMICS%20Parameter%20G220.md#r2198013-status-word-monitoring-2).6) signal sink for the 2nd status word monitoring.

###### Result

You have configured the blocking message. Save the settings in the project.

###### Function diagrams (FD)

Blocking and stall monitoring - 8015 -

###### Additional parameters

---

##### Variable signaling function

###### Overview

Up to 3 different signaling functions can be configured and activated using the "Variable signaling function" function view. Using signaling functions, signal interconnections and parameters can be monitored; these can also be recorded using the "Device trace" commissioning function.

An input signal (c3291) is necessary for the required data source. You define a threshold value of the data source ([p3295](SINAMICS%20Parameter%20G220.md#p329502-variable-signaling-function-threshold-value)) and the hysteresis of the threshold value ([p3296](SINAMICS%20Parameter%20G220.md#p329602-variable-signaling-function-hysteresis)). If the threshold value is violated, then an output signal is generated from [r3294](SINAMICS%20Parameter%20G220.md#r329402-variable-signaling-function-output-signal). A pickup delay ([p3297](SINAMICS%20Parameter%20G220.md#p329702-variable-signaling-function-pickup-delay)) and an OFF delay ([p3298](SINAMICS%20Parameter%20G220.md#p329802-variable-signaling-function-dropout-delay)) can be set for the output signal.

A tolerance band around the threshold value is obtained by setting a specific hysteresis. If the upper band limit is exceeded, output signal r3294 is set to "1", if it drops below the lower band limit, the output signal is set to "0".

You can activate the variable signaling function once the sampling time has been defined ([p3299](SINAMICS%20Parameter%20G220.md#p329902-variable-signaling-function-sampling-time)).

###### Example: Monitoring pressure

Pressure as process variable is to be monitored, whereby a temporary overpressure is tolerated. To do this, the output signal of an external sensor is interconnected with the variable signaling function. The pressure thresholds and an ON delay are set as tolerance time. When the output signal of the variable signaling function is set, for cyclic communication, bit 5 in message word MELDW is set. Message word MELDW is a component of telegrams 102, 103.

![Example: Variable signaling function](images/159832096907_DV_resource.Stream@PNG-en-US.png)

Example: Variable signaling function

###### Requirements

- The drive has been completely created and fully specified in the device configuration.
- The [extended parameterization](#overview-2) is active.

###### Procedure

1. Interconnect the signal source for the input signal of the signaling function (c3291).
2. Define whether the sign should be taken into account when making the comparison ([p3290](SINAMICS%20Parameter%20G220.md#p329005-variable-signaling-function-start).1).

   - Sign is taken into account: The signaling function only takes into account one high limit violation at precisely one location.
   - Sign is not taken into account: The signaling function takes into account a low limit violation as well as a high limit violation.
3. Assign fixed, defined values for the following parameters:

   - Threshold value (p3295)
   - Hysteresis (p3296)
   - ON delay (p3297)
   - OFF delay (p3298)
   - Sampling time (p3299)
4. Interconnect the signal sink for the output signal of the signaling function (r3294).
5. Activate the required signaling function (p3290.0).
6. Repeat steps 1 to 5 for each additional variable signaling function that you wish to create.

###### Result

You have configured the required signaling functions. Then save the project.

###### Function diagrams (FD)

Variable signaling function 1, 2, 3 - 8024 -

###### Additional parameters

---

##### Stall message

###### Overview

The stall monitoring of the motor responds when one of the following thresholds is exceeded:

- If the adaptation controller output exceeds the speed threshold set in [p1744](SINAMICS%20Parameter%20G220.md#p17440n-motor-model-speed-threshold-stall-detection) for stall detection, [r1408](SINAMICS%20Parameter%20G220.md#r1408031-status-word-current-controller).11 (speed adaptation, speed deviation) is set.
- If the speed exceeds a set error threshold ([p1745](SINAMICS%20Parameter%20G220.md#p17450n-motor-model-error-threshold-stall-detection)), r1408.12 (motor stalled) is set.

  This monitoring acts, however, only for low speeds (below [p1755](SINAMICS%20Parameter%20G220.md#p17550n-motor-model-changeover-speed-encoderless-operation) * (100% - [p1756](SINAMICS%20Parameter%20G220.md#p17560n-motor-model-changeover-speed-hysteresis-encoderless-operation))).

If one of the r1408.11 or r1408.12 signals is set, then after the delay time in [p2178](SINAMICS%20Parameter%20G220.md#p21780n-motor-stalled-delay-time), fault "F07902 (N, A) drive: motor stalled" is issued.

If the hysteresis speed ([p3237](SINAMICS%20Parameter%20G220.md#p32370n-hysteresis-speed-7)) and speed ([p3236](SINAMICS%20Parameter%20G220.md#p32360n-speed-threshold-value-7)) exceed a freely defined threshold, after expiration of a specified delay time ([p3238](SINAMICS%20Parameter%20G220.md#p32380n-off-delay-n_act_motor-model-n_act-external)), message "F07937 (N) drive: speed deviation between the motor model and the external speed" is issued.

The thresholds and the delay times required for stall monitoring of the motor and the monitoring of the speed deviation can be configured (defined) in the "Stall message" function view.

###### Requirements

- The drive has been completely created and fully specified in the device configuration.
- The [extended parameterization](#overview-2) is active.
- When using synchronous motors, no "U/f control..." control mode is set.

###### Configuring the (motor stalled) message

1. Enter the maximum permitted speed difference within the current controller sampling time in the "Maximum speed difference per sampling cycle" ([p0492](SINAMICS%20Parameter%20G220.md#p0492-maximum-speed-difference-per-sampling-cycle)) field.

   - and/or -

   Correct the threshold specified for stall detection in the "Motor model speed threshold stall detection" (p1744) field.
2. Correct the threshold specified for motor stall detection in the "Motor model error threshold stall detection" (p1745) field.
3. Correct the specified delay time for the "F07902 (motor stalled)" message in the "Motor stalled delay time" (p2178) field.
4. Interconnect the "Motor stalled" ([r2189](SINAMICS%20Parameter%20G220.md#p21890n-load-monitoring-torque-threshold-3-upper).7) signal sink for the 2nd monitoring status word.

###### Configuring the (speed deviation) message

1. Correct the value specified for the "Speed deviation model/external in tolerance" ([r2199](SINAMICS%20Parameter%20G220.md#r2199011-status-word-monitoring-3).7) message in the "Hysteresis speed 7" (p3237) field.
2. Correct the value specified for the "Speed deviation model/external in tolerance" (r2199.7) message in the "Speed threshold value 7" (p3236) field.
3. Correct the specified OFF delay time for the "Speed deviation model/external in tolerance" (r2199.7) message in the "OFF-delay ..." (p3238) field.
4. Interconnect the "Speed deviation model/external in tolerance" (r2199.7) signal sink for the 3rd monitoring status word.

###### Result

You have configured the stall message settings. Save the settings in the project.

###### Function diagrams (FD)

Blocking and stall monitoring - 8015 -

###### Additional parameters

---

##### Load torque monitoring

###### Overview

With the load torque monitoring, you can check the power that is transmitted between a motor and a driven machine. Typical applications are, for example, V belts, flat belts or chains that grip belt pulleys or sprocket wheels of drive and output shafts, and thereby transmit peripheral speeds and forces. Load monitoring can be used here to identify blocking of the driven machine and interruptions to the power transmission.

During load torque monitoring, the current speed/torque curve is compared with the programmed speed/torque curve ([p2182](SINAMICS%20Parameter%20G220.md#p21820n-load-monitoring-speed-threshold-value-1) to [p2190](SINAMICS%20Parameter%20G220.md#p21900n-load-monitoring-torque-threshold-3-lower)).

**Possible responses of the load torque monitoring**

- [1] A07920 for torque/speed too low

  There is a negative difference of the torque to the torque/speed envelope curve (too low).

  - No response
- [2] A07921 for torque/speed too high

  There is a positive difference of the torque to the torque/speed envelope curve (too high).

  - No response
- [3] A07922 for torque/speed out of tolerance

  The torque deviates from the torque/speed envelope curve.

  - No response
- [4] F07923 for torque/speed too low

  There is a negative difference of the torque to the torque/speed envelope curve (too low).

  - OFF1 (OFF2, OFF3, NONE) as response
- [5] F07924 for torque/speed too high

  There is a positive difference of the torque to the torque/speed envelope curve (too high).

  - OFF1 (OFF2, OFF3, NONE) as response
- [6] F07925 for torque/speed out of tolerance

  The torque deviates from the torque/speed envelope curve.

  - OFF1 (OFF2, OFF3, NONE) as response
- [7] Pump/fan load monitoring as warning
- [8] Pump/fan load monitoring as fault

###### Requirements

- The drive has been completely created and fully specified in the device configuration.
- The [extended parameterization](#overview-2) is active.

###### Procedure

1. In the "Load monitoring configuration" drop-down list ([p2193](SINAMICS%20Parameter%20G220.md#p21930n-load-monitoring-configuration)), select the desired basic configuration of the load torque monitoring.

   The following setting of the desired response to the load monitoring is only possible after this basic setting.
2. In the "Load monitoring response" drop-down list ([p2181](SINAMICS%20Parameter%20G220.md#p21810n-load-monitoring-response)), select the desired response to the results of the load monitoring (see description above).

   The view of the function view is adapted to the setting that was made.
3. If the load monitoring is only to be performed in the 1st quadrant, select the option "Yes" in the drop-down list of the same name ([p2149](SINAMICS%20Parameter%20G220.md#p21490n05-monitoring-configuration)).
4. If required, correct the desired delay time in the "Delay time" field ([p2192](SINAMICS%20Parameter%20G220.md#p21920n-load-monitoring-delay-time)).
5. Enter the desired actual values in the fields at the axes of the graphic (e.g. speed threshold 1).
6. For load failure monitoring, interconnect the signal for failure detection (c3232).
7. If required, correct the desired delay time for failure detection in the "Delay time" field (p2192).
8. Save the project settings.

###### Result

If the current comparison value with active load torque monitoring is outside the programmed tolerance band, a fault or alarm is triggered depending on parameter p2181. The faults or warnings are delayed if a delay time is defined in p2192. This prevents false messages caused by brief transitional states.

###### Function diagrams (FD)

Load monitoring (Part 1) - 8013 -

###### Additional parameters

- [p2183](SINAMICS%20Parameter%20G220.md#p21830n-load-monitoring-speed-threshold-value-2)
- [p2184](SINAMICS%20Parameter%20G220.md#p21840n-load-monitoring-speed-threshold-value-3)
- [p2189](SINAMICS%20Parameter%20G220.md#p21890n-load-monitoring-torque-threshold-3-upper)
- [p2187](SINAMICS%20Parameter%20G220.md#p21870n-load-monitoring-torque-threshold-2-upper)
- [p2188](SINAMICS%20Parameter%20G220.md#p21880n-load-monitoring-torque-threshold-2-lower)
- [p2185](SINAMICS%20Parameter%20G220.md#p21850n-load-monitoring-torque-threshold-1-upper)
- [p2186](SINAMICS%20Parameter%20G220.md#p21860n-load-monitoring-torque-threshold-1-lower)

---

##### Motor temperature

This section contains information on the following topics:

- [Description of function](#description-of-function-4)
- [Configuring temperature models and temperature monitoring](#configuring-temperature-models-and-temperature-monitoring)
- [Motor temperature - Configuration example](#motor-temperature---configuration-example)

###### Description of function

###### Overview

The thermal motor protection monitors the motor temperature and responds to overtemperature conditions with alarms or faults. The motor temperature is either measured with sensors in the motor, or is calculated without sensors, with the aid of a temperature model, from the operating data of the motor.

- For thermal motor protection with temperature sensors, the motor temperature is directly measured in the motor windings. The temperature sensors are connected either to the converter or to add-on modules. The determined temperature values are sent to the converter, which then responds according to the parameter settings.
- The thermal motor protection without temperature sensors uses different temperature models for the calculation. Depending on the temperature model, the temperatures are calculated from the motor operating data. Whereby, the masses of the motor components and the type of ventilation, and for the I<sup>2</sup>t model (for synchronous motors), the motor current in relation to the operating time is taken into consideration in the calculation. Depending on the temperature model, the temperature rise is either assigned to various motor components (stator, rotor) or is calculated from the motor current and the thermal time constant.

You can also use a combination of temperature models with additional temperature sensors. As soon as critical motor temperatures are determined, measures to protect the motor are automatically initiated.

###### Temperature sensors

**Monitoring sensors**

The motor temperature is measured using temperature sensors integrated in the motor windings. The following settings are possible as monitoring sensor:

- [0] No sensor

  The motor temperature is determined automatically through the motor model of the respective motor type.
- [1] Temperature sensor via encoder 1

  Bimetallic switches and Pt100 temperature sensors are not supported.
- [2] Temperature sensor via encoder 2

  Bimetallic switches and Pt100 temperature sensors are not supported.
- [3] Temperature sensor via encoder 3

  Bimetallic switches and Pt100 temperature sensors are not supported.
- [10] Temperature sensor via signal interconnection

  The signal interconnection must be executed via the signal sink p0603.
- [11] Temperature sensor via Motor Module/CU terminals
- [20] Temperature sensor via signal interconnection p0608

  The signal interconnection must be executed via the signal sink p0608. This is only possible in the parameter view.
- [21] Temperature sensor via signal interconnection p0609

  The signal interconnection must be executed via the signal sink p0609. This is only possible in the parameter view.

**Sensor types**

The sensors used are selected as standard from the following four different sensor types or via temperature channels:

- **PTC**

  The temperature sensor is connected to the Sensor Module at the appropriate terminals (-Temp) and (+Temp). A corresponding alarm is output after exceeding the tripping resistance (1650 Ω) and a corresponding fault after the delay time set in [p0606](SINAMICS%20Parameter%20G220.md#p06060n-mot_temp_mod-2-sensor-timer) has expired.
- **KTY84**

  The temperature sensor is connected to the Sensor Module at the appropriate terminals (-Temp) and (+Temp). A KTY84 temperature sensor has an almost linear characteristic and is therefore also suitable for continuously measuring and displaying the motor temperature.
- **Pt100/Pt1000**

  A Pt100 or Pt1000 is in principle a PTC with a very linear characteristic, and is suitable for continuous and exact temperature measurements. Not every sensor input is Pt100/Pt1000-capable.
- **Bimetallic sensor with NC contact** (abbreviated, "bimetal NC contact")

  A bimetallic NC contact actuates a switch at a certain nominal response temperature. The tripping resistance is <100 Ω. Not every sensor input is bimetal NC contact-capable.
- **Evaluation via temperature channels**

  If you use several temperature channels, the sensors are interconnected via signals.

###### Temperature models

If temperature sensors are not used to protect the motor from overheating, then temperature models (also called "thermal motor models") can be used instead. Temperature models respond dynamically faster than temperature sensors and therefore provide better protection against short-term overloads.

> **Note**
>
> During commissioning, the respective temperature model is automatically set after selecting an appropriate motor type. The parameters are automatically set suitable for the motor type.

- **Temperature model 1**

  This temperature model is only used for selected synchronous motors and protects against short-term overloads. It is based on continuous current measurement. The dynamic load of the motor is determined from the motor current and the motor model time constant. The actual value of the motor winding temperature can be measured via a temperature sensor and taken into account.
- **Temperature model 2**

  This temperature model is used for induction motors.
- **Temperature model 3**

  This temperature model is only intended for certain Siemens motors, which do not have their own integrated temperature sensors. Temperature module 3 is a thermal 3-mass model.

###### Additional parameters

---

###### Configuring temperature models and temperature monitoring

###### Overview

The three commonly used motor temperature models require different detailed settings. The respective motor temperature models are automatically assigned to the motors used (or motor types). For example, motor temperature model 2 is automatically assigned to induction motors.

Extensions that add further parameters to the models are automatically activated for motor temperature models 1 and 2.

###### Requirements

- The drive has been completely created and fully specified in the device configuration.
- The [extended parameterization](#overview-2) is active.

  In the standard parameterization, only some of the settings described below are available.

###### Configuring the temperature monitoring

The temperature monitoring settings are also automatically preassigned when the corresponding motor type is selected. You can change the following default settings:

1. In the "Sensor for monitoring" ([p0600](SINAMICS%20Parameter%20G220.md#p06000n-motor-temperature-sensor-for-monitoring)) drop-down list, select another sensor for monitoring the motor temperature.

   The function view is adapted.
2. In the "Sensor type" ([p0601](SINAMICS%20Parameter%20G220.md#p06010n-motor-temperature-sensor-type)) drop-down list, select another sensor type for motor temperature monitoring (if available).

   The function view is adapted.
3. Depending on the preset monitoring sensor, a response to overtemperature ([p0610](SINAMICS%20Parameter%20G220.md#p06100n-motor-overtemperature-response)) can also be configured as an option.

   To do this, select the desired message type.
4. The "Fault message for sensor failure" option is generally always activated when this function view is called and should only be deactivated in exceptional circumstances. For safety reasons, only deactivate this option in exceptional cases.
5. Depending on the sensor and sensor type that have been set, additional parameters for the active motor temperature model are displayed on the function view. Correct the default settings there as required.

###### Temperature monitoring without motor temperature model

For temperature monitoring, it is recommended to use a sensor and a temperature model in parallel. In exceptional cases, however, you can also monitor the temperature exclusively via a sensor.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Overheating with deactivated motor temperature model 3**  The temperature model 3 is only automatically activated for SIEMENS motors that do not have integrated temperature sensors. Deactivating this motor temperature model means that the motor temperature is not monitored at all in this case. This can lead to overheating and destruction of the motor.   - Never deactivate an automatically set motor temperature model 3. |  |

1. Check whether a sensor (p0600) and a sensor type (p0601) are set.
2. Deactivate the preset motor temperature model ([p0612](SINAMICS%20Parameter%20G220.md#p06120n02-mot_temp_mod-activation)).

**Note**

If you subsequently want to deactivate the temperature model, the motor would be completely without monitoring if no sensor were used and set.

###### Configure overtemperature messages

A number of message types are available in order to indicate overtemperature. In the default setting, the message is deactivated.

1. In the function view, show the "Configuration messages" viewlet.
2. In the "Motor overtemperature response" (p0610) drop-down list, select the response when the alarm threshold of the motor temperature is reached.

###### Configuring motor temperature model 1

If the motor temperature model is activated, you can make the following settings:

1. Click the "Temperature model" button in the "Motor temperature" function view.

   The "Motor temperature model 1" dialog opens. All fields are automatically assigned values. You can change these values.
2. Correct the values in the following entry fields:

   - "Motor stall current" ([p0318](SINAMICS%20Parameter%20G220.md#p03180n-motor-stall-current)) for synchronous motors
   - "Thermal time constant" ([p0611](SINAMICS%20Parameter%20G220.md#p06110n-i2t-motor-model-thermal-time-constant)) for the cold stator winding when loaded with the motor stall current
   - "Boost factor at standstill" ([p5350](SINAMICS%20Parameter%20G220.md#p53500n-mot_temp_mod-13-boost-factor-at-standstill)) for the copper losses at standstill.
   - "Overtemperature, stator winding" ([p0627](SINAMICS%20Parameter%20G220.md#p06270n-motor-overtemperature-stator-winding)) in relation to the ambient temperature
   - "Alarm threshold" ([p5390](SINAMICS%20Parameter%20G220.md#p53900n-mot_temp_mod-13-alarm-threshold)) for monitoring the motor temperature
   - "Ambient temperature" ([p0613](SINAMICS%20Parameter%20G220.md#p06130n-mot_temp_mod-13-ambient-temperature))
3. Once all necessary settings have been made, click "Close".

###### Configuring motor temperature model 2

If the motor temperature model is activated, you can make the following settings:

1. Click the "Temperature model" button in the "Motor temperature" function view.

   The "Motor temperature model 2" dialog opens.
2. If required, correct the values in the following fields:

   - "Overtemperature, stator core" ([p0626](SINAMICS%20Parameter%20G220.md#p06260n-motor-overtemperature-stator-core)) in relation to the ambient temperature
   - "Overtemperature, stator winding" (p0627) in relation to the ambient temperature
   - "Overtemperature, rotor" ([p0628](SINAMICS%20Parameter%20G220.md#p06280n-motor-overtemperature-rotor)) in relation to the ambient temperature
   - "Motor weight" ([p0344](SINAMICS%20Parameter%20G220.md#p03440n-motor-weight-for-the-thermal-motor-model)) that influences the 3-mass model of the induction motor
3. Once all necessary settings have been made, click "Close".

###### Configuring motor temperature model 3

If the motor temperature model is activated, you can make the following settings:

1. Click the "Temperature model" button in the "Motor temperature" function view.

   The "Motor temperature model 3" dialog opens.
2. Correct the values in the following entry fields:

   - "Thermal time constant" (p0611) for the cold stator winding when loaded with the motor stall current
   - "Boost factor at standstill" (p5350) for the copper losses at standstill.
   - "Alarm threshold" (p5390) for monitoring the motor temperature
   - "Fault threshold" ([p5391](SINAMICS%20Parameter%20G220.md#p53910n-mot_temp_mod-13-fault-threshold)) for monitoring the motor temperature
   - "Ambient temperature" (p0613)
3. Once all necessary settings have been made, click "Close".

###### Result

You have configured the temperature monitoring settings. Save the settings in the project.

###### Additional parameters

- [p0604](SINAMICS%20Parameter%20G220.md#p06040n-mot_temp_mod-2sensor-alarm-threshold)
- [p0605](SINAMICS%20Parameter%20G220.md#p06050n-mot_temp_mod-12-sensor-threshold-and-temperature-value)
- [p0606](SINAMICS%20Parameter%20G220.md#p06060n-mot_temp_mod-2-sensor-timer)
- [p0616](SINAMICS%20Parameter%20G220.md#p06160n-motor-temperature-alarm-threshold-1)

---

###### Motor temperature - Configuration example

###### Overview

The monitoring of the motor temperature can be performed via a temperature model or a temperature sensor or a combination of both. There are numerous setting variants for the configuration of the motor temperature monitoring that depend on the monitoring sensor used, on the sensor type and on the temperature model used. A detailed description of all these variants would exceed the framework here.

A description of the procedure is shown below for an example with the following configuration:

- Sensor for monitoring: Temperature sensor via encoder 1
- Sensor type: Pt1000
- Motor type: Induction motor
- Alarm message for sensor failure is to be output.

###### Requirements

- The drive has been completely created and fully specified in the device configuration.
- The [extended parameterization](#overview-2) is active.

###### Example of a configuration procedure

1. Select the "Temperature sensor via encoder 1" sensor for monitoring the motor temperature in the "Sensor for monitoring" ([p0600](SINAMICS%20Parameter%20G220.md#p06000n-motor-temperature-sensor-for-monitoring)) drop-down list.

   The display is adapted.

   Since an induction motor is being used, temperature model 2 is activated automatically.

   The "Fault message for sensor failure" option is generally always activated when this function view is called and should only be deactivated in exceptional circumstances.
2. In the "Sensor type" ([p0601](SINAMICS%20Parameter%20G220.md#p06010n-motor-temperature-sensor-type)) drop-down list select the sensor type "Pt1000" for motor temperature monitoring.
3. Optional: Select the message type for overtemperature.
4. In the "Alarm threshold" ([p0604](SINAMICS%20Parameter%20G220.md#p06040n-mot_temp_mod-2sensor-alarm-threshold)) field, correct the proposed alarm threshold for monitoring the motor temperature.
5. In the "Fault threshold" ([p0605](SINAMICS%20Parameter%20G220.md#p06050n-mot_temp_mod-12-sensor-threshold-and-temperature-value)) field, correct the threshold or the temperature value for monitoring the motor temperature.
6. In the "Delay" ([p0606](SINAMICS%20Parameter%20G220.md#p06060n-mot_temp_mod-2-sensor-timer)) field, enter the timer for monitoring the motor temperature.
7. In the "Timer" ([p0607](SINAMICS%20Parameter%20G220.md#p06070n-temperature-sensor-fault-timer)) field, correct the time between the output of an alarm and of a fault.

   This timer is started when a sensor fault is present.
8. Optional: Optimize the detailed settings of the temperature model.

   To do this, click the "Temperature model" button. The configuration dialog of the temperature model opens.

   Correct the following detailed settings:

   - Overtemperature of the stator iron ([p0626](SINAMICS%20Parameter%20G220.md#p06260n-motor-overtemperature-stator-core))
   - Overtemperature of the stator winding ([p0627](SINAMICS%20Parameter%20G220.md#p06270n-motor-overtemperature-stator-winding))
   - Overtemperature of the rotor ([p0628](SINAMICS%20Parameter%20G220.md#p06280n-motor-overtemperature-rotor))
   - Motor weight ([p0344](SINAMICS%20Parameter%20G220.md#p03440n-motor-weight-for-the-thermal-motor-model))

   Once all necessary settings have been made, click "Close".

> **Note**
>
> Depending on the combination of the monitoring sensor, sensor type and temperature model, the values "Alarm threshold", "Fault threshold" and "Delay" in the function view may have to be measured separately or corrected for monitoring via a temperature sensor, and for monitoring via a temperature model.

> **Note**
>
> You can view and partially correct further details of the motor and motor data. Click the ![Example of a configuration procedure](images/92607914379_DV_resource.Stream@PNG-de-DE.PNG) icon to open the "Motor" function view.

###### Result

You have configured the temperature monitoring settings. Save the settings in the project.

###### Function diagrams (FD)

Thermal monitoring, motor - 8016 -

Motor temperature model 1 (I2t) - 8017 -

Motor temperature model 2 - 8018 -

Motor temperature model 3 - 8019 -

###### Additional parameters

- [p0613](SINAMICS%20Parameter%20G220.md#p06130n-mot_temp_mod-13-ambient-temperature)
- [p0625](SINAMICS%20Parameter%20G220.md#p06250n-motor-ambient-temperature-during-commissioning)
- [r0631](SINAMICS%20Parameter%20G220.md#r06310n-mot_temp_mod-stator-iron-temperature)
- [r0632](SINAMICS%20Parameter%20G220.md#r06320n-mot_temp_mod-stator-winding-temperature)
- [r0633](SINAMICS%20Parameter%20G220.md#r06330n-mot_temp_mod-rotor-temperature)
- [p5390](SINAMICS%20Parameter%20G220.md#p53900n-mot_temp_mod-13-alarm-threshold)
- [p5391](SINAMICS%20Parameter%20G220.md#p53910n-mot_temp_mod-13-fault-threshold)

---

#### Friction characteristic

This section contains information on the following topics:

- [Configuring the friction characteristic](#configuring-the-friction-characteristic)
- [Configuring the recording of friction characteristics](#configuring-the-recording-of-friction-characteristics)

##### Configuring the friction characteristic

###### Overview

The friction characteristic is used to compensate the friction torque for the motor and the driven machine. A friction characteristic allows the speed controller to be precontrolled and improves the control response. Use 10 interpolation points for the friction characteristic. You define the coordinates of every interpolation point by a speed parameter ([p3820](SINAMICS%20Parameter%20G220.md#p38200n-friction-characteristic-value-n0) ... [p3829](SINAMICS%20Parameter%20G220.md#p38290n-friction-characteristic-value-n9)) and a torque parameter ([p3830](SINAMICS%20Parameter%20G220.md#p38300n-friction-characteristic-value-m0) ... [p3839](SINAMICS%20Parameter%20G220.md#p38390n-friction-characteristic-value-m9)). The default coordinates can be changed as required in the "Friction characteristic" function view.

**Features**

- 10 interpolation points are available for mapping the friction characteristic.
- An automatic function allows you to record the friction characteristic (record friction characteristic).
- The speed actual value input (c3848) can be wired as friction torque.
- The friction characteristic can be activated and deactivated ([p3842](SINAMICS%20Parameter%20G220.md#p3842-friction-characteristic-activation)).
- Online mode is required for using the friction characteristic.

###### Requirements

- The drive has been completely created and fully specified in the device configuration.
- The "Speed/torque control" mode is activated (see [Operating mode](#operating-mode-1)).

  - Or -

  The "Dynamic Drive Control" operating mode is activated.
- U/f control is **not** activated.
- The [extended parameterization](#overview-2) is active.

###### Procedure

1. Select the "[1] Friction characteristic activated" (p3842) option in the "Friction characteristic activation" drop-down list.

   The LED next to the drop-down list lights up green. The switchover switch is set to 1.
2. Correct the signal interconnection of the speed actual value of the friction characteristic via the "Speed actual value input" signal source (c3848) if required.
3. Interconnect the signal for the torque of the friction characteristic via the "Friction characteristic output" signal sink ([r3841](SINAMICS%20Parameter%20G220.md#r3841-friction-characteristic-output)) depending on the speed or velocity.
4. Save the settings in the project.

###### Result

The friction characteristic is activated. It uses the specified coordinates of the 10 interpolation points. These coordinates can be configured together with the settings for recording the friction characteristic (see "[Configuring the recording of friction characteristics](#configuring-the-recording-of-friction-characteristics)").

###### Function diagrams (FD)

Friction characteristic - 7010 -

###### Additional parameters

- [p3821](SINAMICS%20Parameter%20G220.md#p38210n-friction-characteristic-value-n1)
- [p3822](SINAMICS%20Parameter%20G220.md#p38220n-friction-characteristic-value-n2)
- [p3823](SINAMICS%20Parameter%20G220.md#p38230n-friction-characteristic-value-n3)
- [p3824](SINAMICS%20Parameter%20G220.md#p38240n-friction-characteristic-value-n4)
- [p3825](SINAMICS%20Parameter%20G220.md#p38250n-friction-characteristic-value-n5)
- [p3826](SINAMICS%20Parameter%20G220.md#p38260n-friction-characteristic-value-n6)
- [p3827](SINAMICS%20Parameter%20G220.md#p38270n-friction-characteristic-value-n7)
- [p3828](SINAMICS%20Parameter%20G220.md#p38280n-friction-characteristic-value-n8)
- [r3840](SINAMICS%20Parameter%20G220.md#r384009-friction-characteristic-status-word)
- [p3843](SINAMICS%20Parameter%20G220.md#p38430n-friction-characteristic-frictional-torque-diff-smoothing-time)
- [p3844](SINAMICS%20Parameter%20G220.md#p38440n-friction-characteristic-number-changeover-point-upper)
- [p3845](SINAMICS%20Parameter%20G220.md#p3845-record-friction-characteristic-activation)
- [p3846](SINAMICS%20Parameter%20G220.md#p38460n-record-friction-characteristic-ramp-upramp-down-time)
- [p3847](SINAMICS%20Parameter%20G220.md#p38470n-record-friction-characteristic-time-to-warm-up)

---

##### Configuring the recording of friction characteristics

###### Overview

You can make the following settings in the "Recording of the friction characteristic" function view:

- Configuring the recording of the friction characteristic
- Configuring the coordinates of the interpolation points

When the friction characteristic is recorded, the drive can cause the motor to move. As a result, the motor may reach maximum speed.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Unplanned motor motion while recording the friction characteristic**  Drive motion caused when recording the friction characteristic can result in death, severe injury or material damage.  - Ensure that nobody is present in the hazardous zone and that the mechanical system can move freely. |  |

###### Requirements

- The drive has been completely created and fully specified in the device configuration.
- The [extended parameterization](#overview-2) is active.

###### Procedure

For configuring, proceed as follows:

1. Enter the warm-up time until the maximum speed is to be reached in the "Recording warm-up time" field ([p3847](SINAMICS%20Parameter%20G220.md#p38470n-record-friction-characteristic-time-to-warm-up)).

   After the end of the warm-up period, measurement is started.
2. Enter the ramp-up/ramp-down time of the ramp-up/ramp-down generator for automatic recording of the friction characteristic in the "Recording ramp-up/ramp-down time" field ([p3846](SINAMICS%20Parameter%20G220.md#p38460n-record-friction-characteristic-ramp-upramp-down-time)).
3. If required, correct the n and M coordinates of the 10 specified interpolation points:

   - In the "Speed" fields, configure the specified speed ([p3820](SINAMICS%20Parameter%20G220.md#p38200n-friction-characteristic-value-n0)[0] ... [p3829](SINAMICS%20Parameter%20G220.md#p38290n-friction-characteristic-value-n9)[0]) for each interpolation point.
   - In the "Torque" fields, configure the specified torque ([p3830](SINAMICS%20Parameter%20G220.md#p38300n-friction-characteristic-value-m0)[0] ... [p3839](SINAMICS%20Parameter%20G220.md#p38390n-friction-characteristic-value-m9)[0]) for each interpolation point.
4. Establish an online connection to the drive.
5. In the "Recording of the friction characteristic" function view, select the desired automatic friction characteristic recording in the "Record friction characteristic activation" drop-down list ([p3845](SINAMICS%20Parameter%20G220.md#p3845-record-friction-characteristic-activation)). The following options are available:

   - [0] Record friction characteristic deactivated
   - [1] Record friction characteristic activated all directions

     The friction characteristic is recorded in both directions of rotation. The results of the positive and negative measurement are averaged and entered in p3830 ... p3839.
   - [2] Record friction characteristic activated positive direction
   - [3] Record friction characteristic activated negative direction
6. Save the configuration in the project.

###### Result

After the next switch-on command, the friction characteristic will be automatically recorded.

###### Function diagrams (FD)

Friction characteristic - 7010 -

###### Additional parameters

---

#### Bypass operation

This section contains information on the following topics:

- [Description of function](#description-of-function-5)
- [Configuring a bypass](#configuring-a-bypass)

##### Description of function

###### Overview

The bypass mode allows you to operate a motor using the converter or directly on the line supply. The switches are controlled using the converter; feedback signals of the switch positions must be returned to the converter. The bypass mode is used for G220 drives without synchronization.

###### Requirement

- An asynchronous motor is used.

###### Description of function

If the bypass mode is active, the drive switch is opened when the motor is transferred to the line supply (after pulse inhibit of the converter), the system waits until the motor has been deenergized and then the line side switch is closed, so that the motor can be operated directly on the line supply. The non-synchronized switch-off of the motors means a startup current flows when the motor is switched on; this must be taken into account for the design of the protective equipment.

The activation of the "Bypass without synchronization" mode can be initiated using the following signals:

- Binary signal:   
  The activation of the bypass is triggered by a binary signal, e.g. from a higher-level automation system. If the binary signal is withdrawn again, the switch to converter operation is initiated after the expiration of the bypass time.
- Motor speed:   
  Once a certain speed is reached, the system changes over to bypass operation, i.e. the converter is used as a start-up converter. In order that the bypass is switched in, the speed setpoint must also be higher than the comparison speed.

###### Function diagrams (FD)

Bypass - 7035 -

###### Additional parameters

- [p1260](SINAMICS%20Parameter%20G220.md#p1260-bypass-configuration)
- [r1261](SINAMICS%20Parameter%20G220.md#r1261014-bypass-controlstatus-word)
- [p1262](SINAMICS%20Parameter%20G220.md#p12620n-bypass-dead-time)
- [p1263](SINAMICS%20Parameter%20G220.md#p1263-debypass-delay-time)
- [p1264](SINAMICS%20Parameter%20G220.md#p1264-bypass-delay-time)
- [p1265](SINAMICS%20Parameter%20G220.md#p1265-bypass-speed-threshold)
- c1266
- [p1267](SINAMICS%20Parameter%20G220.md#p126701-bypass-changeover-source-configuration)
- c1269
- [p1274](SINAMICS%20Parameter%20G220.md#p127401-bypass-switch-monitoring-time)

---

##### Configuring a bypass

###### Overview

When the motor is transferred to the line supply, contactor K1 is opened (after pulse disable of the converter). The system then waits for the motor de-excitation time to elapse, after which contactor K2 is closed, connecting the motor directly to the line supply.

Due to the non-synchronized connection of the motor to the line supply, an equalizing current will flow when the motor is connected, which must be taken into account when designing the protective device (see figure). This is why this type of bypass is only suitable for drives with a low power rating.

![Example: bypass without synchronization](images/159832350219_DV_resource.Stream@PNG-en-US.png)

Example: bypass without synchronization

When the motor is transferred from the line supply by the converter, contactor K2 opens first, then contactor K1 closes after the de-excitation time. The converter then captures the rotating motor and the motor is operated on the converter.

###### Requirements

- The drive has been completely created and fully specified in the device configuration.
- Contactor K2 must be designed for switching under inductive load.
- Contactors K1 and K2 must be mutually interlocked so that they cannot close at the same time.
- The [extended parameterization](#overview-2) is active.

###### Procedure

1. Select the "Bypass without synchronization" configuration in the "Bypass configuration" ([p1260](SINAMICS%20Parameter%20G220.md#p1260-bypass-configuration)) drop-down list.
2. Specify when the bypass is to be triggered. To do this, activate the following options:

   - Bypass via signal ([p1267](SINAMICS%20Parameter%20G220.md#p126701-bypass-changeover-source-configuration).0)

     Also displays the "Bypass control command" input field.

     - And/or -
   - Bypass when reaching the speed threshold (p1267.1)

     Also displays the "Bypass speed threshold" input field.
3. If the "Bypass via signal" option is active, interconnect the signal source for the control command to activate the bypass under "Bypass control command" (p1266).
4. Interconnect the signals sources via which the feedback signals can be output:

   - "Switch motor/drive" (c1269.0)
   - "Switch motor/line supply" (c1269.1)
5. Interconnect the following signal sinks for the control and feedback signals of the bypass switches:

   - "Command switch motor - power unit" ([r1261](SINAMICS%20Parameter%20G220.md#r1261014-bypass-controlstatus-word).0)
   - "Command switch motor - line supply" (r1261.1)
6. Correct the specified values in the following input fields:

   - "Bypass dead time" ([p1262](SINAMICS%20Parameter%20G220.md#p12620n-bypass-dead-time))
   - "Debypass delay time" ([p1263](SINAMICS%20Parameter%20G220.md#p1263-debypass-delay-time))
   - "Bypass" delay time ([p1264](SINAMICS%20Parameter%20G220.md#p1264-bypass-delay-time))
   - "Bypass speed threshold" ([p1265](SINAMICS%20Parameter%20G220.md#p1265-bypass-speed-threshold))
7. Enter the monitoring time for the following bypass switches:

   - "Switch motor/drive" ([p1274](SINAMICS%20Parameter%20G220.md#p127401-bypass-switch-monitoring-time).0)
   - "Switch motor/line supply" (p1274.1)

###### Result

Bypass mode is activated and configured.

###### Additional parameters

---

#### Encoder functions

This section contains information on the following topics:

- [Configuring the zero mark tolerance](#configuring-the-zero-mark-tolerance)
- [Configuring the absolute position of the incremental encoders](#configuring-the-absolute-position-of-the-incremental-encoders)

##### Configuring the zero mark tolerance

###### Overview

"Zero mark tolerance" allows individual faults to be tolerated regarding the number of encoder pulses between two zero marks. This improves the evaluation of the encoder signals.

> **Note**
>
> - You can only parameterize the zero mark tolerance when commissioning the encoder. It is not possible to change parameters in operation!
> - The functions described in the following apply to SMC30 modules and to Control Units with internal encoder evaluation.

![Sketch: Zero mark tolerance](images/159834050315_DV_resource.Stream@PNG-en-US.png)

Sketch: Zero mark tolerance

###### Requirements

- The motor used in the device configuration has been completely specified and configured.
- The encoders used in the device configuration of the drive, including the encoder evaluation selection, have been completely specified and configured.
- The [extended parameterization](#overview-2) is active.

###### Procedure

1. If the drive uses several encoders, then select the required encoder in the function view.
2. Enter a value for "Zero mark minimum length" ([p4686](SINAMICS%20Parameter%20G220.md#p46860n-zero-mark-minimum-length)).

   The minimum length is subdivided into 1/4 encoder pulses.
3. Enter the default value for the permissible tolerance ([p4680](SINAMICS%20Parameter%20G220.md#p46800n-zero-mark-monitoring-tolerance-permissible)).

   The tolerance is entered in encoder pulses.
4. Enter the following range-defining values for the required tolerance window:

   - Tolerance window limit positive ([p4681](SINAMICS%20Parameter%20G220.md#p46810n-zero-mark-monitoring-tolerance-window-limit-1-positive))
   - Alarm threshold positive ([p4683](SINAMICS%20Parameter%20G220.md#p46830n-zero-mark-monitoring-tolerance-window-alarm-threshold-positive))
   - Tolerance window limit negative ([p4682](SINAMICS%20Parameter%20G220.md#p46820n-zero-mark-monitoring-tolerance-window-limit-1-negative))
   - Alarm threshold negative ([p4684](SINAMICS%20Parameter%20G220.md#p46840n-zero-mark-monitoring-tolerance-window-alarm-threshold-negative))

###### Result

If the function is activated, then the following responses are executed:

1. The "Zero mark tolerance" function starts to become effective after the 2nd zero mark has been detected.
2. After this, if the number of track pulses between 2 zero marks does not match the configured number of pulses once, then alarm A3x400<sup>1)</sup> (alarm threshold, zero mark distance error) or A3x401<sup>1)</sup> (alarm threshold, zero mark failed) is output.
3. The alarms are cleared if the next zero mark is received at the correct position.
4. However, if a new zero mark position error is identified, fault F3x100<sup>1)</sup> (zero mark distance error) or Fx3101<sup>1)</sup> (zero mark failed) is output.

| Symbol | Meaning |
| --- | --- |
| <sup>1)</sup> x = encoder number (x = 1, 2 or 3) |  |

###### Example

![Tolerance window and correction](images/153598822667_DV_resource.Stream@PNG-en-US.png)

Tolerance window and correction

###### Additional parameters

- [p0430](SINAMICS%20Parameter%20G220.md#p04300n1927-sensor-module-configuration)

---

##### Configuring the absolute position of the incremental encoders

###### Overview

The actual value "XIST_ERW" can be reset for each encoder used in the drive. The following modes ([p4652](SINAMICS%20Parameter%20G220.md#p465202-xist1_erw-reset-mode)) are available for resetting:

- [0] Inactive

  Resetting is deactivated.
- [1] Reset with zero mark

  The value in XIST1_ERW is reset when passing every zero mark.
- [2] Reset with signal interconnection

  The value in XIST1_ERW is reset with a 0/1 edge via the binary signal sink c4655.
- [3] Reset with selected zero mark

  The value in XIST1_ERW is reset after a 0/1 edge via binary signal sink r4655 when passing the next zero mark.

The absolute value is only valid after passing the zero mark.

###### Requirements

- The motor used in the device configuration has been completely specified and configured.

  This basic parameterization cannot be performed without complete configuration.
- The encoders used in the device configuration of the drive, including the encoder evaluation selection, have been completely specified and configured.
- The [extended parameterization](#overview-2) is active.

###### Procedure

In the "Absolute position incremental encoder" function view, setting areas for resetting the respective encoder are displayed for each encoder used in the drive.

1. Select the reset mode for the desired encoder (e.g. motor encoder) in the drop-down list.
2. Then make a sensible signal interconnection for [r4654](SINAMICS%20Parameter%20G220.md#r465408-xist1_erw-status), [r4653](SINAMICS%20Parameter%20G220.md#r465302-xist1_erw-actual-value) and, depending on the mode, c4655 for each of the individual values.
3. Repeat steps 1 and 2 for all encoders for which you want to configure the reset.

###### Result

The actual values for the encoders are reset.

###### Additional parameters

---

### Safety Integrated

This section contains information on the following topics:

- [Introduction](#introduction)
- [Safety Integrated safety notes](#safety-integrated-safety-notes)
- [Basic settings](#basic-settings)
- [Stop functions](#stop-functions)
- [Motion monitoring functions](#motion-monitoring-functions)
- [Temperature monitoring](#temperature-monitoring)
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

Safety Integrated Functions correspond to functions according to IEC 61800‑5‑2 and IEC 61800‑5‑3.

##### Safety Integrated Functions used

The SINAMICS G220 drives of firmware V6.1 feature the following drive-integrated Safety Integrated Functions:

| Functions | Abbr. | Area | Meaning |
| --- | --- | --- | --- |
| [Safe Torque Off](#sto) | STO | **Stop functions** | Safe Torque Off according to stop Category 0  Must always be parameterized, because this function is selected internally in the system as a stop response after limit value violations or after an internal event. |
| [Safe Stop 1](#ss1) | SS1 | Safe stop in accordance with stop category 1  Must always be parameterized, because this function is selected internally in the system as a stop response after limit value violations or after an internal event. |  |
| [Safe Acceleration Monitor](#configuring-sam) | SAM | Safe monitoring of drive acceleration  Is required as a subfunction for other Safety Integrated Functions. |  |
| [Safe Brake Ramp](#configuring-sbr) | SBR | Safe Brake Ramp  Is required as a subfunction for other Safety Integrated Functions. |  |
| [Safely-Limited Speed](#sls) | SLS | **Motion monitoring** | Safely-Limited Speed |
| [Safe Speed Monitor](#ssm) | SSM | Safe monitoring of the speed |  |
| [Safe Direction](#sdi) | SDI | Safe monitoring of the direction of motion |  |
| [Safe Motor Temperature](#using-smt) | SMT | **Temperature monitoring** | Safe monitoring of the motor temperature |

**Special features of PROFIsafe**

For PROFIsafe, you need a telegram extension, which you set under "[Telegram configuration](Communication%20and%20telegrams.md#telegram-configuration-via-profidrive)" or in the "Conn. to PLC" function view in the guided quick startup.

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

- F13000 → License not sufficient
- LED RDY → flashes red at 2 Hz

  ![Overview](images/148901058059_DV_resource.Stream@PNG-de-DE.png)

**Overview of licenses**

Startdrive provides a "License overview" page. This shows the most important information about the licenses and the license status of your drive system; see [License overview](Configuring%20SINAMICS%20G220%20drives.md#overview-of-licenses).

**Trial License Mode**

The drive system can only be operated with an insufficient license for an option during commissioning and servicing. For this purpose, the Trial License Mode must be activated explicitly, see [Trial License Mode](Configuring%20SINAMICS%20G220%20drives.md#activate-trial-license-mode).

**Displaying/acquiring the license key**

You can display the currently entered license key or activate a new license key via the "License overview" page; see [License key](Configuring%20SINAMICS%20G220%20drives.md#creating-a-license-key).

**Marking of the Extended Functions**

Extended Functions are indicated in the function selection by the icon ![Overview](images/145073587083_DV_resource.Stream@PNG-de-DE.png).

###### Functions that require a license

A Safety Extended license is required for the following Safety Integrated Functions:

- Safe Stop 1 with acceleration monitoring (SS1-a)
- Safe Stop 1 with braking ramp monitoring (SS1-r)
- Safely-Limited Speed (SLS)
- Safe Speed Monitor (SSM)
- Safe Direction (SDI)

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

| Control type | STO<sup>1)</sup> | SS1 | SLS | SSM | SDI | SMT<sup>2)</sup> |
| --- | --- | --- | --- | --- | --- | --- |
| PROFIsafe | x | x | x | x | x | x |
| PROFIsafe and emergency stop via terminals | x | x | x | x | x | x |
| Terminals | x<sup>1)</sup> | x | x | x | x | x |
| <sup>1)</sup> Factory setting: STO is enabled in the factory setting and can be controlled via F-DI 0. If STO is not used, the terminals of the F-DI 0 must be short-circuited with a wire jumper.   <sup>2)</sup> Temperature monitoring independent of the control mode. This requires that an SMT option module (OM-SMT) is plugged in for use in ATEX applications. |  |  |  |  |  |  |

> **Note**
>
> **Marking of the Extended Functions**
>
> Extended Functions are indicated in the function selection by the icon ![Usable Safety Integrated Functions](images/145073587083_DV_resource.Stream@PNG-de-DE.png). The corresponding safety functions are part of a function package that requires a license.

> **Note**
>
> **Extended parameterization functions**
>
> The actual value acquisition cycle and monitoring cycle belong to the extended parameterization functions. Both are not shown in the standard functions display in the function view (see [Switching the display](#overview-2)).

###### Requirements

- Using Safety Extended Functions:

  The Safety Extended license is available for the following Safety Integrated Functions:

  - Safe Stop 1 with acceleration monitoring (SS1-a)
  - Safe Stop 1 with braking ramp monitoring (SS1-r)
  - Safely-Limited Speed (SLS)
  - Safe Speed Monitor (SSM)
  - Safe Direction (SDI)
- The drive has been completely created and specified in the device configuration.
- The created drive uses an encoder.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

###### Procedure

1. Call the "Safety Integrated > Function selection" menu in the secondary navigation.
2. Click on ![Procedure](images/154401807627_DV_resource.Stream@PNG-en-US.PNG) to activate the editing mode.
3. Select one of the following from the "Control type" drop-down list:

   - No Safety Integrated Function
   - via PROFIsafe
   - via PROFIsafe and emergency stop via terminals
   - via terminals
4. Then enable the Safety Integrated Functions that you require in the lower part of the dialog.

   Startdrive only displays the functions that belong to the control type you selected. The entries for the selected and preselected functions are displayed in the secondary navigation.
5. Select the drive axis type in the "Axis type" drop-down list ([p9502](SINAMICS%20Parameter%20G220.md#r9502-si-axis-type)):

   - "Linear axis"
   - "Rotary axis"

   This setting influences the setting options in the "Actual value acquisition" function view and provides for a unit switchover.
6. Optional: In the "Actual value acquisition cycle" field ([p9511](SINAMICS%20Parameter%20G220.md#p9511-si-actual-value-sensing-cycle)), enter the cycle time with which the actual values for Safety Integrated are to be acquired.
7. Optional: Enter the desired sampling time for the Safety Integrated Functions in the "Monitoring cycle" field ([p9500](SINAMICS%20Parameter%20G220.md#p9500-si-monitoring-clock-cycle)).
8. If you made the previous settings in online mode, subsequently perform a warm start of the drive.
9. Then click the buttons (or the entry in the secondary navigation) to parameterize the desired Safety function.
10. After completing parameterization, to exit the editing mode, click ![Procedure](images/154401817611_DV_resource.Stream@PNG-en-US.PNG).

    - If you are working offline, the project can now be loaded into the drive. The drive must then be restarted.
    - If you are working online, the parameterization performed takes effect and can be executed at the machine.

**Note**

STO is released by default when the function selection is called for the first time. Using an Emergency Stop command device connected to the F-DI 0, the STO can be used immediately after startup. If the STO is used exclusively via F-DI 0, no Safety commissioning is required.

You can disable this function if necessary.

**Higher-level settings**

With the selected control type, you can set the actual value acquisition and the actual value acquisition cycle. Actual value sensing "with encoder" (p9506) is preassigned and cannot be changed.

The Safety Integrated monitoring clock cycle is preset to 4 ms and the actual value acquisition clock cycle is preset to 1 ms. This does not have to be changed for Safety Integrated applications.

###### Result

The basic settings for Safety Integrated have been made. The desired Safety Integrated Functions are enabled. The Safety Integrated Functions are executed with pre-defined standard settings. You can change the settings in the function views (exception: [SMT](#using-smt)) as required.

###### Additional parameters

---

---

**See also**

[License for Extended Functions required](#license-for-extended-functions-required)
  
[Starting and Ending Safety Integrated commissioning](#starting-and-ending-safety-integrated-commissioning)

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
- [SAM/SBR](#samsbr)

##### STO

This section contains information on the following topics:

- [Safe Torque Off (STO) mode of operation](#safe-torque-off-sto-mode-of-operation)
- [Configuring STO](#configuring-sto)

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
| ① | Selection of STO | - The converter identifies when STO is selected and signals the status "STO active" ([r9722](SINAMICS%20Parameter%20G220.md#r9722015-si-status-signals).00) - The converter interrupts the torque-generating energy supply to the motor. There is no electrical isolation. - If you are using a line contactor, then the converter opens the line contactor. - The switch-on inhibit prevents the motor from automatically restarting. |
| ② |  | - The motor coasts down to a standstill. |
| ③ | Deselection of STO | - The converter detects the deselection of STO. |
| ④ | Signal change at ON/OFF1 from 1 to 0 | - The converter is again ready for switching on. |
| ⑤ | Signal change at ON/OFF1 from 0 to 1 | - The motor starts again. |

###### Additional parameters

---

###### Configuring STO

###### Overview

The "Safe Torque Off" (STO) function is used to safely disconnect the torque-generating energy supply to the motor for a machine function or in the event of a fault. A restart is prevented by the two-channel pulse suppression. The switch-on inhibit prevents an automatic restart after deselection of STO.

###### Requirements

- The editing mode for Safety Integrated is [activated](#starting-and-ending-safety-integrated-commissioning).
- The STO stop function is released in the Safety Integrated [function selection](#selecting-the-safety-functionality).

###### Procedure

1. Click the ![Procedure](images/149396101643_DV_resource.Stream@PNG-de-DE.png) button (Select STO) in the "STO" function view to configure control of the "STO" function.

   The "Control" function view appears. The display of the function view depends on the basic setting of the Safety Integrated Functions in the function selection.

   In this function view, configure the controls via the fail-safe inputs and outputs and/or PROFIsafe (see "[Control](#control-via-profisafe)").
2. Optional: Call the "STO" Safety Integrated Function again.
3. Click "Save project" in the toolbar to save the changes in the project.

###### Additional parameters

- [r9720](SINAMICS%20Parameter%20G220.md#r9720015-si-control-word)
- [r9722](SINAMICS%20Parameter%20G220.md#r9722015-si-status-signals)

---

##### SS1

This section contains information on the following topics:

- [SS1 with time control mode of operation (SS1-t)](#ss1-with-time-control-mode-of-operation-ss1-t)
- [SS1 with acceleration monitoring (SS1-a) mode of operation](#ss1-with-acceleration-monitoring-ss1-a-mode-of-operation)
- [SS1 with braking ramp monitoring (SS1-r) mode of operation](#ss1-with-braking-ramp-monitoring-ss1-r-mode-of-operation)
- [Configuring SS1](#configuring-ss1)

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

  SS1 delay time ([p9556](SINAMICS%20Parameter%20G220.md#p9556-si-transition-time-ss1-to-sto)) ≥ OFF3 ramp-down time ([p1135](SINAMICS%20Parameter%20G220.md#p11350n-off3-ramp-down-time)) + pulse cancellation delay time ([p1228](SINAMICS%20Parameter%20G220.md#p12280n-pulse-cancellation-delay-time)) + motor holding brake closing time ([r1217](SINAMICS%20Parameter%20G220.md#p12170n-motor-holding-brake-closing-time))
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
| ① | Selection of SS1 | - The converter detects when SS1 is selected and signals status "SS1 active" ([r9722](SINAMICS%20Parameter%20G220.md#r9722015-si-status-signals).1). - The converter starts the transition time SS1 to STO (p9556). - The converter initiates braking along the OFF3 ramp. |
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
| ① | Selection of SS1 | - The converter detects when SS1 is selected and signals status "SS1 active" ([r9722](SINAMICS%20Parameter%20G220.md#r9722015-si-status-signals).1). - The converter starts the transition time SS1 to STO ([p9556](SINAMICS%20Parameter%20G220.md#p9556-si-transition-time-ss1-to-sto)) and the SAM delay time ([p9582](SINAMICS%20Parameter%20G220.md#p9582-si-samsbr-delay-time)). - The converter brakes the motor along the OFF3 ramp. |
| ② |  | - The SAM delay time elapses. With SAM, the drive monitors whether the motor impermissibly accelerates. - The SAM limit value follows the decreasing motor velocity:   As long as the amount of velocity decreases, the converter continuously adds the configurable tolerance [p9548](SINAMICS%20Parameter%20G220.md#p9548-si-sam-velocity-tolerance-1) to the actual velocity so that the monitoring tracks the velocity as it changes. If the velocity temporarily increases, the monitoring threshold remains at the last value. - If the motor velocity exceeds the SAM monitoring velocity by more than the velocity tolerance (p9548), then the converter signals a fault and activates STO. - If the motor velocity reaches the SAM limit value ([p9568](SINAMICS%20Parameter%20G220.md#p9568-si-sam-velocity-limit-1)), then the converter limits the value for the SAM monitoring to p9568. |
| ③ |  | - SAM ends when the motor velocity falls below the STO shutdown velocity ([p9560](SINAMICS%20Parameter%20G220.md#p9560-si-sto-shutdown-velocity-1)) or the SS1 to STO (p9556) transition time expires. STO is then activated. - The converter identifies when STO is selected and signals the status "STO active" (r9722.0). SS1 still remains active. - STO interrupts the torque-generating supply of energy to the motor and prevents the motor from unexpectedly restarting. - The motor coasts down to a standstill. |
| ④ | Deselection of SS1 | - The converter detects the deselection of SS1. STO is simultaneously deactivated. |
| ⑤ | Signal change at ON/OFF1 from 1 to 0 | - The converter is again ready for switching on. |
| ⑥ | Signal change at ON/OFF1 from 0 to 1 | - The motor starts again. |

###### Additional parameters

---

###### SS1 with braking ramp monitoring (SS1-r) mode of operation

###### Overview

With SS1-r, while braking, the converter monitors whether the velocity of the motor remains below a defined ramp using the safe brake ramp monitoring (SBR).

###### Sequence:

![Sequence: SS1 with SBR](images/173618995083_DV_resource.Stream@PNG-en-US.png)

Sequence: SS1 with SBR

|  |  |  |
| --- | --- | --- |
| **Action** |  | **Motor / converter response** |
| ① | Selection of SS1 | - The converter detects when SS1 is selected and signals status "SS1 active" ([r9722](SINAMICS%20Parameter%20G220.md#r9722015-si-status-signals).1). - The converter brakes the motor along the OFF3 ramp. - The converter starts the SBR delay time ([p9582](SINAMICS%20Parameter%20G220.md#p9582-si-samsbr-delay-time)). |
| ② |  | - The SBR delay time elapses. - The converter starts the safe brake ramp SBR. |
| ③ |  | - The converter monitors whether the motor exceeds the set safe brake ramp when braking. - If the motor velocity does not follow the brake ramp, then the converter signals a fault and activates STO. |
| ④ |  | - SBR ends as soon as the actual speed value is below the STO shutdown speed ([p9560](SINAMICS%20Parameter%20G220.md#p9560-si-sto-shutdown-velocity-1)). - The converter identifies when STO is selected and signals the status "STO active" (r9722.0). SS1 still remains active. - STO interrupts the torque-generating supply of energy to the motor and prevents the motor from unexpectedly restarting. - The motor coasts down to a standstill. |
| ⑤ | Deselection of SS1 | - The converter detects the deselection of SS1. STO is simultaneously deactivated. |
| ⑥ | Signal change at ON/OFF1 from 1 to 0 | - The converter is again ready for switching on. |
| ⑦ | Signal change at ON/OFF1 from 0 to 1 | - The motor starts again. |

###### Additional parameters

---

###### Configuring SS1

###### Overview

In the "Safe Stop 1" (SS1) function view you make settings for the motor deceleration. The "SS1" function brakes the motor, monitors the motor deceleration within specified limits, and after a delay time or violation of a speed threshold, triggers the "STO" function.

###### Comparison of settings for motor deceleration

| Settings | Method of operation |
| --- | --- |
| SS1 with SAM | - Braking is monitored with the "Safe Acceleration Monitor" function. - The delay time starts after the function has been selected ([p9556](SINAMICS%20Parameter%20G220.md#p9556-si-transition-time-ss1-to-sto)). If SS1 is deselected again within this time, the STO function is selected and deselected again immediately after the delay time has expired or if the shutdown velocity is undershot, i.e. the SS1 function is terminated normally. It cannot be interrupted. |
| SS1 with SBR | - Braking is monitored with the "Safe Brake Ramp" function. - The drive brakes along the OFF3 ramp ([p1135](SINAMICS%20Parameter%20G220.md#p11350n-off3-ramp-down-time)) once "Safe Stop 1" is selected and switches to "Safe Torque Off" (STO) when the shutdown velocity is undershot ([p9560](SINAMICS%20Parameter%20G220.md#p9560-si-sto-shutdown-velocity-1)). |

###### Requirements

- The editing mode for Safety Integrated is [activated](#starting-and-ending-safety-integrated-commissioning).
- The SS1 stop function is released in the Safety Integrated [function selection](#selecting-the-safety-functionality).

###### Variant 1: Configuring SS1 with SAM

1. Click the ![Variant 1: Configuring SS1 with SAM](images/149396101643_DV_resource.Stream@PNG-de-DE.png) button (Select SS1) in the "SS1" function view to configure control of the "SS1" function.

   The "Control" function view appears. The display of the function view depends on the basic setting of the Safety Integrated Functions.

   In this function view, configure the controls via the fail-safe inputs and outputs and/or PROFIsafe (see "[Control](#control-via-profisafe)").
2. Select the monitoring type "SAM" in the "Monitoring" drop-down list ([p9606](SINAMICS%20Parameter%20G220.md#p9606-si-ss1-function-specification)).
3. Click the "Monitoring" button and parameterize the alternative brake monitoring functions "[SAM](#configuring-sam)" in the dialog.
4. Enter the required delay time in the "Delay time SS1 -> STO active" (p9556) entry field.
5. Enter the shutdown speed for activating STO in the "STO shutdown speed" (p9560) entry field.
6. Click "Save project" in the toolbar to save the changes in the project.

###### Variant 2: Configuring SS1 with SBR

1. Click the ![Variant 2: Configuring SS1 with SBR](images/149396101643_DV_resource.Stream@PNG-de-DE.png) button (Select SS1) in the "SS1" function view to configure control of the "SS1" function.

   The "Control" function view appears. The display of the function view depends on the basic setting of the Safety Integrated Functions.

   In this function view, configure the controls via the fail-safe inputs and outputs and/or PROFIsafe (see "[Control](#control-via-profisafe)").
2. Select the monitoring type "SBR" in the "Monitoring" drop-down list (p9606).
3. Click the "Monitoring" button and parameterize the alternative brake monitoring functions "[SBR](#configuring-sbr)" in the dialog.
4. Enter the shutdown speed for activating STO in the "STO shutdown speed" (p9560) entry field.
5. Click "Save project" in the toolbar to save the changes in the project.

###### Additional parameters

- [r9722](SINAMICS%20Parameter%20G220.md#r9722015-si-status-signals)

---

##### SAM/SBR

This section contains information on the following topics:

- [Configuring SAM](#configuring-sam)
- [Configuring SBR](#configuring-sbr)

###### Configuring SAM

###### Overview

The "Safe Acceleration Monitor" (SAM) function is used to safely monitor braking along the OFF3 ramp.

As long as the speed reduces, the converter continuously adds the adjustable velocity tolerance [p9548](SINAMICS%20Parameter%20G220.md#p9548-si-sam-velocity-tolerance-1) to the current speed so that the monitoring tracks the speed. If the speed is temporarily higher, the monitoring remains at the last value. The converter reduces the monitoring until the SAM velocity limit in [p9568](SINAMICS%20Parameter%20G220.md#p9568-si-sam-velocity-limit-1) is reached. The SAM limit value is frozen when the velocity falls below the SAM velocity limit in p9568.

If the motor accelerates by the velocity tolerance during the OFF3 deceleration ramp, SAM detects the incident and triggers an STO.

- SAM monitoring will continue to be performed until the SS1 delay time [p9556](SINAMICS%20Parameter%20G220.md#p9556-si-transition-time-ss1-to-sto) expires.

Calculating the SAM tolerance of the actual velocity:

- The following applies when parameterizing the SAM tolerance:

  - The maximum velocity increase after SS1 is triggered is derived from the effective acceleration (a) and the duration of the acceleration phase.
  - The duration of the acceleration phase is equivalent to one monitoring cycle (MC; [p9500](SINAMICS%20Parameter%20G220.md#p9500-si-monitoring-clock-cycle)) (delay from detecting an SS1 until n<sub>set</sub> = 0)
- Calculating the SAM tolerance:

  Actual velocity for SAM = acceleration x acceleration duration   
  This results in the following setting rule:

  - For a linear axis: SAM tolerance [mm/min] = a [m/s<sup>2</sup>] MC [s] 1000 [mm/m] 60 [s/min]
  - For a rotary axis: SAM tolerance [rpm] = a [rev/s<sup>2</sup>] MC [s] 60 [s/min]
- Recommendation   
  The SAM tolerance value entered should be approx. 20% higher than the calculated value.
- You set the tolerance so that the "undershoot" which inevitably occurs when standstill is reached after braking along the OFF3 ramp is tolerated. However, the size of this cannot be calculated.

###### Additional parameters

- [p9516](SINAMICS%20Parameter%20G220.md#p95161-si-encoder-configuration-safety-functions)
- [p9581](SINAMICS%20Parameter%20G220.md#p9581-si-sbr-reference-velocity-1)
- [p9583](SINAMICS%20Parameter%20G220.md#p9583-si-sbr-reference-time)

---

###### Configuring SBR

###### Overview

The "Safe Brake Ramp" (SBR) function provides a safe method for monitoring the brake ramp. The "Safe Brake Ramp" function is used with the Safe Stop functions for monitoring the braking process.

The motor is immediately decelerated along the OFF3 ramp as soon as "SS1" (SS2, etc.) is initiated. Monitoring of the brake ramp is activated once the delay time [p9582](SINAMICS%20Parameter%20G220.md#p9582-si-samsbr-delay-time) has expired. Monitoring ensures that the motor does not exceed the set brake ramp (SBR) when braking.

The gradient of the brake ramp is defined using the reference velocity [p9581](SINAMICS%20Parameter%20G220.md#p9581-si-sbr-reference-velocity-1) and the brake ramp monitoring time [p9583](SINAMICS%20Parameter%20G220.md#p9583-si-sbr-reference-time).

The braking process can be monitored in parallel with the braking ramp of the converter. Follow these rules for settings:

Linear axis:

- Reference velocity p9581 = Maximum speed [p1082](SINAMICS%20Parameter%20G220.md#p10820n-maximum-speed)[0] * Transmission ratio [p9521](SINAMICS%20Parameter%20G220.md#p952107-si-gearbox-encoder-motorload-denominator)[0]/[p9522](SINAMICS%20Parameter%20G220.md#p952207-si-gearbox-encoder-motorload-numerator)[0]* Leadscrew pitch [p9520](SINAMICS%20Parameter%20G220.md#p9520-si-leadscrew-pitch)
- Reference time p9583 = Ramp-down time (OFF3) [p1135](SINAMICS%20Parameter%20G220.md#p11350n-off3-ramp-down-time)[0]

Rotary axis:

- Reference velocity p9581 = Maximum speed p1082[0] * Transmission ratio p9521[0]/p9522[0]
- Reference time p9583 = Ramp-down time (OFF3) p1135[0]

###### Pre-assigning the reference velocity/reference time

If required, you can automatically pre-assign the values for reference velocity or reference time. In the lower part of the dialog, the calculation formulas for the corresponding value are displayed for this purpose.

1. If you want to pre-assign the value for the reference velocity, click "Accept" in the corresponding line.
2. If you want to pre-assign the value for the reference time, click "Accept" in the corresponding line.

###### Additional parameters

- [p9516](SINAMICS%20Parameter%20G220.md#p95161-si-encoder-configuration-safety-functions)
- [p9548](SINAMICS%20Parameter%20G220.md#p9548-si-sam-velocity-tolerance-1)

---

#### Motion monitoring functions

This section contains information on the following topics:

- [SLS](#sls)
- [SSM](#ssm)
- [SDI](#sdi)

##### SLS

This section contains information on the following topics:

- [Safely-Limited Speed (SLS) mode of operation](#safely-limited-speed-sls-mode-of-operation)
- [Principle of operation of SLS with one speed level](#principle-of-operation-of-sls-with-one-speed-level)
- [Principle of operation of SLS with switchover of speed levels](#principle-of-operation-of-sls-with-switchover-of-speed-levels)
- [Principle of operation of SLS with a variable speed limit value](#principle-of-operation-of-sls-with-a-variable-speed-limit-value)
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
  
[Additional functional features](#additional-functional-features)

###### Principle of operation of SLS with one speed level

###### Overview

SLS can be used with one speed level. If the motor velocity violates the SLS limit value, then the converter initiates the set stop response.

###### Sequence:

![Sequence: SLS 1 level](images/165210163979_DV_resource.Stream@PNG-en-US.png)

Sequence: SLS 1 level

| Action |  | Motor / converter response |
| --- | --- | --- |
| ① | Selection of SLS | - The converter detects the selection of SLS. - The converter starts the SLS delay time ([p9551](SINAMICS%20Parameter%20G220.md#p9551-si-sls-delay-time-for-limit-value-change)). |
| ② |  | - The motor is braked as a result of the external setpoints. - The actual speed must remain below the SLS limit value until the SLS delay time has elapsed. |
| ③ |  | - Once the SLS delay time (p9551) has elapsed, the monitoring of SLS limit value (level 1: [p9531](SINAMICS%20Parameter%20G220.md#p953103-si-sls-limit-values-1)[0]) becomes active. - The converter signals the status "SLS active" ([r9722](SINAMICS%20Parameter%20G220.md#r9722015-si-status-signals).4). |
| ④ |  | - If the SLS limit value is violated, the converter initiates the set stop response (level 1: [p9563](SINAMICS%20Parameter%20G220.md#p956303-si-sls-stop-response)[0]). |
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
| ① | Selection of SLS | - The converter detects the selection of SLS level 2. - The converter starts the SLS delay time ([p9551](SINAMICS%20Parameter%20G220.md#p9551-si-sls-delay-time-for-limit-value-change)). |
| ② |  | - The motor is braked as a result of the external setpoints. - The actual speed must remain below the SLS limit value until the SLS delay time has elapsed. |
| ③ |  | - Once the SLS delay time (p9551) elapses, monitoring of the SLS limit value (level 2: [p9531](SINAMICS%20Parameter%20G220.md#p953103-si-sls-limit-values-1)[1]) becomes active. - The converter signals the status "SLS active" ([r9722](SINAMICS%20Parameter%20G220.md#r9722015-si-status-signals).4) and active SLS level 2 (r9722.9 = 1, r9722.10 = 0). |
| ④ |  | - If the motor velocity violates the SLS limit value, then the converter initiates the set stop response (level 2: [p9563](SINAMICS%20Parameter%20G220.md#p956303-si-sls-stop-response)[1]) off. |
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
  - [p9604](SINAMICS%20Parameter%20G220.md#p9604030-si-enable).9 is set: Transfer of SLS limit values via PROFIsafe is enabled.
- S_SLS_LIMIT_A has the value range 1 ... 32767. The following applies:

  - 32767 ≙ 100% of the 1st SLS level
  - The actually monitored limit value is calculated as follows:  
    SLS limit value = (S_SLS_LIMIT_A/32767) · [p9531](SINAMICS%20Parameter%20G220.md#p953103-si-sls-limit-values-1)[0].
- In this case, speed levels 2, 3 and 4 can be parameterized and selected.
- The selected delay time cannot be changed during operation. If various delay times are required in the application, then this requirement must be realized using a time-delayed transfer of the SLS limit value using your control system (F‑CPU).
- If an incorrect SLS limit value is transferred, the drive responds with the stop response parameterized in [p9563](SINAMICS%20Parameter%20G220.md#p956303-si-sls-stop-response) for speed level 1 and safety alarm C01711.

###### Additional parameters

---

###### Additional functional features

###### Setpoint speed limit and SLS

It also makes sense to configure the speed setpoint limit at the same time that SLS is parameterized. This configuration functions in a higher-level control system that evaluates the Safety Info Channel (SIC) in telegram 700, for example.

[p9533](SINAMICS%20Parameter%20G220.md#p9533-si-sls-setpoint-speed-limiting) defines the evaluation factor to determine the setpoint limit from the selected actual speed limit as a percentage. The active limit value is evaluated using this factor, and is made available in [r9733](SINAMICS%20Parameter%20G220.md#r973302-si-effective-setpoint-velocity-limiting). r9733 is used to transfer the values to a higher-level control, for example. For example, the control system can adapt traversing speeds to SLS levels. r9733 is part of the SIC.

- r9733[0] = [p9531](SINAMICS%20Parameter%20G220.md#p953103-si-sls-limit-values-1)[x] · p9533 (converted from the load to the motor side)
- r9733[1] = -p9531[x] · p9533 (converted from the load to the motor side)

  [x] = selected SLS level

Conversion factor from the motor to the load side:

- Motor type = rotary and axis type = linear: [p9522](SINAMICS%20Parameter%20G220.md#p952207-si-gearbox-encoder-motorload-numerator)/([p9521](SINAMICS%20Parameter%20G220.md#p952107-si-gearbox-encoder-motorload-denominator) · [p9520](SINAMICS%20Parameter%20G220.md#p9520-si-leadscrew-pitch))
- Otherwise: p9522/p9521

###### Switching over between SLS limit values

The limit values are switched over binary coded using 2 PROFIsafe control bits. The statuses of the speed selection can be checked using [r9720](SINAMICS%20Parameter%20G220.md#r9720015-si-control-word).9 and r9720.10.

The actual SLS limit value can be displayed using [r9722](SINAMICS%20Parameter%20G220.md#r9722015-si-status-signals).9 and r9722.10. The precondition to display the limit value is: SLS is active (r9722.4 = 1).

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

   - Delay time for SLS ([p9551](SINAMICS%20Parameter%20G220.md#p9551-si-sls-delay-time-for-limit-value-change))
   - Speed limits for max. 4 levels ([p9531](SINAMICS%20Parameter%20G220.md#p953103-si-sls-limit-values-1)[0])
   - Stop responses (STO or SS1) for each level ([p9563](SINAMICS%20Parameter%20G220.md#p956303-si-sls-stop-response)[0])
   - Activate/inhibit PROFIsafe override for SLS of level 1 ([p9604](SINAMICS%20Parameter%20G220.md#p9604030-si-enable).9)

     This means that you transfer variable SLS limits via PROFIsafe to the converter.

**Result**

The velocity limit value of the drive is configured. The current SLS limit value is displayed in the field of the same name ([r9714](SINAMICS%20Parameter%20G220.md#r971404-si-diagnostics-velocity-1)[2]). The effective setpoint limit is displayed in the field of the same name ([r9733](SINAMICS%20Parameter%20G220.md#r973302-si-effective-setpoint-velocity-limiting)). It is used, for example, to transmit values to a higher-level control system, which can then, for example, adapt traversing speeds to the SLS levels.

###### Additional parameters

- [p9581](SINAMICS%20Parameter%20G220.md#p9581-si-sbr-reference-velocity-1)
- [p9582](SINAMICS%20Parameter%20G220.md#p9582-si-samsbr-delay-time)
- [p9583](SINAMICS%20Parameter%20G220.md#p9583-si-sbr-reference-time)
- [r9720](SINAMICS%20Parameter%20G220.md#r9720015-si-control-word)
- [r9722](SINAMICS%20Parameter%20G220.md#r9722015-si-status-signals)

---

---

**See also**

[Configuring SS1](#configuring-ss1)
  
[Stop responses](#stop-responses)

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
| ① | Selection of SSM | - The converter detects the selection of SSM. - If the motor velocity is between the velocity limit and the negative velocity limit, the converter sets the signal "Speed below limit value" ([p9722](SINAMICS%20Parameter%20G220.md#r9722015-si-status-signals).15 = 1). |
| ② | Exceeding the velocity limit | - When the motor velocity exceeds the velocity limit, the converter resets the "Speed below limit value" signal (p9722.15 = 0). |
| ③ |  | - If the motor velocity falls below the velocity limit minus the hysteresis, the converter sets the signal "Speed below limit value" (p9722.15 = 1). |
| ④ | Exceeding the negative velocity limit | - If the motor velocity falls below the negative velocity limit, the converter resets the "Speed below limit value" signal (p9722.15 = 0). |
| ⑤ |  | - If the motor velocity exceeds the negative velocity limit plus the hysteresis, the converter sets the signal "Speed below limit value" (p9722.15 = 1). |

![Sequence: SSM filter](images/173830294923_DV_resource.Stream@PNG-en-US.png)

Sequence: SSM filter

The signal filter smoothes the measured value of the velocity.

The filter reduces signal changes of the SSM feedback when monitoring velocities that are just below the speed limit.

An active filter leads to a time delay of the SSM feedback.

The behavior of the signal filter can be set using filter time ([p9545](SINAMICS%20Parameter%20G220.md#p9545-si-ssm-filter-time)).

###### Example

SSM is suitable for enabling machine access through safe SSM feedback. Thus, for example, it is possible to unlock safety doors only when the velocity falls below critical levels.

> **Note**
>
> **SSM initial value during ramp-up**
>
> The initial value of the SSM signal during ramp-up can be adapted via p9507.9.
>
> - p9507.9 = 0 means "SSM status signal initialized to "1" during ramp-up".
> - p9507.9 = 1 means "SSM status signal initialized to "0" during ramp-up".

###### Additional parameters

---

###### Configuring SSM

###### Overview

The "Safe Speed Monitor" (SSM) function provides a reliable method for detecting when the velocity falls below the velocity limit ([p9546](SINAMICS%20Parameter%20G220.md#p9546-si-ssm-velocity-limit-1)) in both directions of rotation, e.g. for standstill detection. A failsafe output signal is available for further processing.

A velocity hysteresis can be configured for the "SSM" function. This is predominantly automatically active. In this way, a more stable signal characteristic of SSM can be achieved at speeds close to the velocity limit.

For the hysteresis, the velocity (or speed) determined by the two channels must not differ by more than the difference between the velocity limit and the velocity hysteresis. Otherwise it would be theoretically possible that one channel returns a HIGH signal and the other a LOW signal for "SSM".

The following figure shows the characteristic of the "SSM" safe output signal when hysteresis is active:

![Overview](images/159834983435_DV_resource.Stream@PNG-en-US.png)

The output signal for SSM is smoothed by setting a filter time with a PT1 filter ([p9545](SINAMICS%20Parameter%20G220.md#p9545-si-ssm-filter-time)).

###### Requirements

- The editing mode for Safety Integrated is [activated](#starting-and-ending-safety-integrated-commissioning).
- The SSM monitoring function is released in the Safety Integrated [function selection](#selecting-the-safety-functionality).

###### Procedure

1. Click the ![Procedure](images/148125432331_DV_resource.Stream@PNG-en-US.png) button (Select SSM) to configure control of the "SSM" function.

   The "Control" function view appears. The display of the function view depends on the basic setting of the Safety Integrated Extended Functions.

   In this function view, configure the controls via PROFIsafe (see "[Control](#control)").

   You can select the PROFIsafe telegrams in the telegram configuration. This means you also specify the required control word.
2. Call the "SSM" function view again.
3. Enter the required value in mm/min in the "Velocity hysteresis" ([p9547](SINAMICS%20Parameter%20G220.md#p9547-si-ssm-velocity-hysteresis-1)) field.
4. Enter the required limit value in mm/min in the "Velocity limit" (p9546) field.
5. Specify a time value for the PT1 filter in the "Filter time" (p9545) field.

###### Result

You have configured the safety function SSM. Save the settings in the project.

###### Additional parameters

- [r9722](SINAMICS%20Parameter%20G220.md#r9722015-si-status-signals)

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
| ① | Selection of SDI+ | - The converter detects the selection of SDI+. - The converter starts the SDI delay time ([p9565](SINAMICS%20Parameter%20G220.md#p9565-si-sdi-delay-time)). |
| ② |  | - The converter monitors the motor's direction of motion once the SDI delay time expires. - The converter signals the status "SDI positive active" ([r9722](SINAMICS%20Parameter%20G220.md#r9722015-si-status-signals).12). - The converter continuously calculates the motor position. - As soon as the motor moves in the impermissible direction, the converter saves the current position and monitors the deviation between the current position and saved position. |
| ③ |  | - If the deviation between the actual position and the saved position is higher than the SDI tolerance [p9564](SINAMICS%20Parameter%20G220.md#p9564-si-sdi-tolerance-1), then the converter brakes the motor with the set stop response ([p9566](SINAMICS%20Parameter%20G220.md#p9566-si-sdi-stop-response)) and outputs a safety message <sup>1)</sup>. |
| ④ | Deselection of SDI+ | - The converter detects the deselection of SDI+. - The converter stops monitoring the motion direction. - The motor can now be moved in both directions. |
| <sup>1)</sup> The following steps are required to acknowledge the safety message: - Deselect SDI and select again - Safe acknowledgment |  |  |

> **Note**
>
> **Direction change is not detected using [p1821](SINAMICS%20Parameter%20G220.md#p18210n-direction-of-rotation)**
>
> Safe monitoring is still possible if the direction of motion is reversed using p1821. However, in this case, setpoint limiting [r9733](SINAMICS%20Parameter%20G220.md#r973302-si-effective-setpoint-velocity-limiting) is calculated with the wrong direction of rotation. Parameter [p9539](SINAMICS%20Parameter%20G220.md#p953907-si-gearbox-rotation-reversal) can be used to set the direction of motion for safety monitoring.

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

- SDI positive active ([r9722](SINAMICS%20Parameter%20G220.md#r9722015-si-status-signals).12)
- SDI negative active (r9722.13)

> **Note**
>
> **No change of direction detected**
>
> If the direction of rotation ([p1821](SINAMICS%20Parameter%20G220.md#p18210n-direction-of-rotation)) is reversed in the [basic parameterization](#selecting-the-safety-functionality), then safe monitoring is still possible: However, in this case, the setpoint limitation [r9733](SINAMICS%20Parameter%20G220.md#r973302-si-effective-setpoint-velocity-limiting) is calculated with the wrong direction of rotation. A reversal of the direction of rotation therefore does not make sense in this case.

After selecting SDI via PROFIsafe, delay time [p9565](SINAMICS%20Parameter%20G220.md#p9565-si-sdi-delay-time) is started. During this time, you have the option of ensuring that the drive is moving in the enabled direction. After this, the "Safe Direction" function is active and the direction of motion is monitored.

If the drive now moves more than the configured tolerance ([p9564](SINAMICS%20Parameter%20G220.md#p9564-si-sdi-tolerance-1)) in the blocked direction, message C01716 is output and the stop response defined in [p9566](SINAMICS%20Parameter%20G220.md#p9566-si-sdi-stop-response) is initiated. To acknowledge the messages, you must first deselect SDI, remove the fault cause and then safely acknowledge the messages. Only then can you reselect SDI.

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
3. Enter a delay time in ms in the "Delay time for selection of SDI -> SDI active" (p9565) field.
4. Enter a monitoring tolerance in mm in the "Monitoring tolerance" (p9564) field.
5. Select the required stop response in the "Selection" drop-down list (p9566).
6. Click on the icon ![Procedure](images/148900571915_DV_resource.Stream@PNG-de-DE.PNG) to display a function view of the set [stop response](#stop-responses).

   Make the necessary configuration here.

###### Result

You have configured the safety function SDI. Save the settings in the project.

###### Additional parameters

- [r9720](SINAMICS%20Parameter%20G220.md#r9720015-si-control-word)
- r9733

---

#### Temperature monitoring

This section contains information on the following topics:

- [Principle of operation of safe motor temperature (SMT)](#principle-of-operation-of-safe-motor-temperature-smt)
- [Using SMT](#using-smt)

##### Principle of operation of safe motor temperature (SMT)

###### Overview

![Overview SMT](images/150436640011_DV_resource.Stream@PNG-de-DE.png)

Overview SMT

Safe Motor Temperature (SMT) prevents the motor temperature from exceeding a defined limit value. SMT is used to protect a motor used in a potentially explosive atmosphere against overtemperature.

SMT is a safety function according to IEC61800-5-2.

The OM-SMT Option Module has 2 inputs for PTC sensors (PTC thermistor) to monitor the temperature of the motors that are deployed in hazardous areas:

- For shutdown

  - ATEX certified according to:

    SIL 2: IEC 61508, IEC 61800-5-2, IEC 62061, EN 61511-1

    PL d, Cat. 3: ISO 13849-1, ISO 13849-2
- For the alarm

Type A PTC thermistors according to IEC 60947-8 and DIN VDE 0898-1-401 are used.

ATEX applications in zones 2/22 and 1/21 are supported.

###### Applications

SMT is used to protect against overtemperature of a motor in hazardous environments, e.g. in the chemical industry, in paper mills, or in paint shops.

###### Sequence

![SMT sequence](images/159829473035_DV_resource.Stream@PNG-en-US.png)

SMT sequence

| Action |  | Response |
| --- | --- | --- |
| ① |  | - The OM-SMT monitors the motor temperature using the PTC thermistor mounted on the motor. |
| ② |  | - The OM-SMT identifies when a temperature is exceeded.   Above the shutdown limit, the electrical resistance of the PTC thermistor suddenly increases as a step function. This response activates STO. - The OM-SMT responds with fault C35550 "Motor overtemperature". - The converter activates Safe Torque Off (STO) as a stop response and signals "STO active". - STO prevents energy from being fed to the motor. The motor coasts down. |
| ③ | Deselection of STO  Acknowledge the fault | - The converter deactivates STO.   The PTC thermistor resistance drops below the shutdown limit. |
| ④ | Signal change at ON/OFF1 from 1 to 0 | - The converter is again ready for switching on. |
| ⑤ | Signal change at ON/OFF1 from 0 to 1 | - The motor starts again. |

###### Additional parameters

---

---

**See also**

[Adding an SMT option module](Configuring%20SINAMICS%20G220%20drives.md#adding-an-smt-option-module)
  
[Starting and Ending Safety Integrated commissioning](#starting-and-ending-safety-integrated-commissioning)
  
[Selecting the safety functionality](#selecting-the-safety-functionality)
  
[Description of function](#description-of-function-4)

##### Using SMT

###### Overview

The motor temperature can be safely monitored with a plugged Option Module OM-SMT (ATEX module).

The temperature thresholds for shutdown and optionally for setting an alarm are detected by the PTC temperature sensors installed in the motor. The PTC temperature sensors are connected to the OM-SMT.

When the shutdown threshold is reached, SMT is activated and triggers STO as a fault response.

###### Applications

With safe motor temperature monitoring, the SINAMICS G220 converter can operate an explosion-proof motor in the hazardous area. ATEX applications in zones 2/22 and 1/21 are supported.

###### Requirements

- In the device configuration, the Control Unit is connected to an [OM-SMT](Configuring%20SINAMICS%20G220%20drives.md#adding-an-smt-option-module).
- A PTC temperature sensor is used in the motor.

  You can generally set the sensor type via the settings of the [motor temperature monitoring](#description-of-function-4) or, in the case of third-party motors, also during the acquisition of the motor data.
- The editing mode for Safety Integrated is [activated](#starting-and-ending-safety-integrated-commissioning).
- The SMT monitoring function is released in the Safety Integrated [function selection](#selecting-the-safety-functionality).

###### Procedure

1. Startdrive checks if the function SMT is enabled in the function selection and if an Option Module OM-SMT is connected (inserted) with the G220 drive in the device configuration.
2. If SMT is triggered, STO is automatically activated as a stop response.

   The respective status can be checked via the "[Function status](#function-status)" function view.

#### Actual value acquisition/mechanical system

##### Overview

The properties of the selected encoder are displayed in this view. The load-side accuracies are calculated and displayed with the mechanical settings.

**Load-side limits and accuracies for the safe motion monitoring functions**

The safe maximum velocity [r9730](SINAMICS%20Parameter%20G220.md#r9730-si-safe-maximum-velocity-1) is determined based on the actual value acquisition system. It specifies the maximum load velocity that can still be correctly detected with the current encoder parameterization.

With the current encoder parameterization, a maximum position accuracy [r9731](SINAMICS%20Parameter%20G220.md#r9731-si-safe-position-accuracy-1) can be achieved.

##### Requirements

- The editing mode for Safety Integrated is [activated](#starting-and-ending-safety-integrated-commissioning).
- The required axis type was selected in the "[Function selection](#selecting-the-safety-functionality)".
- At least one Safety Integrated Extension Function (e.g. SS1-r/-a, SLS ...) is enabled.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

##### Procedure

> **Note**
>
> The number of encoder pulses ([p0408](SINAMICS%20Parameter%20G220.md#p04080n-rotary-encoder-pulse-number)) can be changed in the inspector window.

1. Should you wish to use a gear ratio for the gear, record the values for "Load revolutions" ([p9521](SINAMICS%20Parameter%20G220.md#p952107-si-gearbox-encoder-motorload-denominator)) and "Encoder revolutions" ([p9522](SINAMICS%20Parameter%20G220.md#p952207-si-gearbox-encoder-motorload-numerator)) necessary in this regard.  
   A gear ratio is the ratio of encoder revolutions to revolutions of the drive shaft (load revolutions).
2. If a rotational direction reversal is linked with the gear being used, activate the 'Load rotational direction reversal" ([p9539](SINAMICS%20Parameter%20G220.md#p953907-si-gearbox-rotation-reversal)) option.
3. If using the "Linear axis" axis type, set the transmission ratio between encoder and load in mm/revolution (linear axis with rotary encoder) in the "Leadscrew pitch" field ([p9520](SINAMICS%20Parameter%20G220.md#p9520-si-leadscrew-pitch)).

##### Result

You have configured the safety settings for the actual value acquisition. Save the settings in the project.

##### Additional parameters

---

#### Control

This section contains information on the following topics:

- [Overview of controls](#overview-of-controls)
- [Control via PROFIsafe](#control-via-profisafe)
- [Control via PROFIsafe and emergency stop via terminals](#control-via-profisafe-and-emergency-stop-via-terminals)
- [Control via terminals](#control-via-terminals)
- [Self-test of the fail-safe digital input (F-DI)](#self-test-of-the-fail-safe-digital-input-f-di)

##### Overview of controls

###### Overview

In the "Control" function view, you configure the settings for control via PROFIsafe or via the safe inputs and outputs. These settings always relate to the Safety Integrated Functions activated in the function selection (see [Safety functions that can be activated for each control type](#selecting-the-safety-functionality)).

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
| Safe state | Using function "Safe State", the drive (e.g. G220) combines the "Active" status of the Safety Integrated functions to form a common status signal. Using Safe State, a safety function can be externally evaluated via a fail-safe digital output or PROFIsafe, for example. |
| Fail-safe  digital input F-DI | A fail-safe digital input (F-DI) allows Safety Integrated Functions to be selected and deselected along with a fail-safe acknowledgment. A fail-safe digital input comprises 2 channels, each with one digital input. The F-DI must be enabled in order to safely monitor the drive. |
| Fail-safe  digital output F-DO | A fail-safe digital output (F-DO) supplies feedback signals from the selected Safety Integrated functions. An F-DO is active after setting up the control type and connecting the F-DO signal source. When commissioning Safety Integrated, the F-DO goes into a safe state (0 V, OFF). When the safety function signals a fault condition, the F-DO remains in the safe state until fail-safe acknowledgment. |
| Discrepancy time | During the discrepancy time, the drive tolerates briefly inconsistent signals at both input terminals of the fail-safe digital input (F-DI). Permanent discrepancy indicates an error in the F-DI circuit. In this case, the drive responds with a safety message. |
| Debounce time | The debounce time specifies the maximum time an interference pulse can be present at an F-DI; during this time, the drive does not interpret the pulse as a switching operation. The drive status does not change. The drive suppresses tolerated signal changes in this way. |
| Self-test | Using test signals, the self-test checks whether the fail-safe digital input (F-DI) can be switched into the "low" safe state during the "high" signal state. The drive initiates a fault response if it does not detect a test signal. Instead of internal test signals, external dark pulses can also be used for the self-test. |

###### Function diagrams (FD)

Fail-safe digital inputs (F-DI 0 ... F-DI 2) - 2850 -

Fail-safe digital output (F-DO 0) - 2853 -

Control signals safe motion monitoring function (Part 1) - 2854 -

Control signals safe motion monitoring function (Part 2) - 2855 -

Safe State selection - 2856 -

##### Control via PROFIsafe

###### Requirements

- The editing mode for Safety Integrated is [activated](#starting-and-ending-safety-integrated-commissioning).
- In the Safety Integrated [function selection](#selecting-the-safety-functionality), control "via PROFIsafe" is activated.
- The desired Safety Integrated Functions are also enabled in the function selection.

###### Configuring control via PROFIsafe

The following configuration is required for controlling the Safety Integrated Functions via PROFIsafe.

1. Click the ![Configuring control via PROFIsafe](images/148900571915_DV_resource.Stream@PNG-de-DE.PNG) icon "Telegram configuration"

   The properties of the PROFINET interface are displayed in the Inspector window. The "Cyclic data exchange" setting area is active. The telegrams for the drive objects can be specified here.

   The following steps 2 and 3 apply if no PROFIsafe telegram has yet been created (e.g. via the guided quick startup).
2. Optional: Click in the telegram configuration of the "Drive control telegrams" on the entry <Add telegram>.
3. Optional: Select the "Add Safety telegram" option in the drop-down list of the entry:

   Then the lines "Send Safety Integrated Telegram (actual value)" and "Receive Safety Integrated Telegram (setpoint)" are inserted. PROFIsafe telegram 902 is preset. Alternatively, you can select PROFIsafe telegram 30.
4. Open the lower-level function view "Receive Safety Integrated Telegram (setpoint)" in the Inspector window.
5. Correct the PROFIsafe address of the drive in the "F-address" field.
6. Switch back to the "Control" function view.

   The communication parameters transferred to the drive (PROFIsafe telegram, F-addresses, F-monitoring time) are displayed here. The value of the F-address is displayed in the "PROFIsafe address" ([p9610](SINAMICS%20Parameter%20G220.md#p9610-si-profisafe-destination-address)) field. A preassigned PROFIsafe telegram is displayed in the "PROFIsafe telegram no." drop-down list.
7. Select the response for communication failure ([p9612](SINAMICS%20Parameter%20G220.md#p9612-si-stop-response-for-failure-or-control-fault)).

**Note**

**"SS1" set as failure response**

When PROFIsafe communication fails, the drive brakes the motor using function SS1.  
The drive continues braking even if PROFIsafe communication is restored before the end of braking.  
While braking, the drive ignores all commands that it receives via PROFIsafe.  
As long as the drive brakes the motor using function SS1, then controlling STO, for example, has no effect.

###### Configuring routing

The F-DI can also be used for controlling via PROFIsafe. In this case, the connected sensors report their status to the higher-level F-controller for further processing. The routing must be configured to transfer the F-DI states via PROFIsafe. The following Safety Integrated telegrams are routing-capable: 902. In addition, the F-DI can be set here in such a way that both antivalent sensors (NC/NO contact) and equivalent sensors (NC/NC contact) can be connected.

1. Open the "Control" function view of the drive.

   The "Configuration routing" area is now displayed.
2. Select the input mode of the fail-safe digital inputs (F-DI) in the "Configuration routing" area.  
   To do so, select whether they should be NC or NO in the drop-down lists for the fail-safe digital inputs ([p10040](SINAMICS%20Parameter%20G220.md#p1004002-si-f-di-input-mode).0 to p10040.2).
3. Click on the connection icon ![Configuring routing](images/141470326667_DV_resource.Stream@PNG-de-DE.PNG) (p10050.0 to p10050.2) beside the drop-down list of the respective fail-safe digital input to activate the transfer of the F-DI state to the F-controller.  
   The transfer is activated when the symbol shows a closed connection between two points ![Configuring routing](images/141474457099_DV_resource.Stream@PNG-de-DE.PNG).

###### Configuring control via the F-DI

The signal states of an F-DI are monitored to determine whether they have assumed the same logical signal state within the discrepancy time.

The drive-internal Safety Integrated Function issues safety faults for internal faults or limit value violations.

1. Enter a discrepancy time [ms] in the "Discrepancy time" ([p10002](SINAMICS%20Parameter%20G220.md#p10002-si-f-di-changeover-discrepancy-time)) field.

   Based on the discrepancy time, the converter tolerates short-time differences in input signals. During this time the fail-safe digital input (F-DI) remains guaranteed.

**Performing the online test**

Detailed information on possible self-tests is provided on Page [Self-test of the fail-safe digital input (F-DI)](#self-test-of-the-fail-safe-digital-input-f-di).

###### Configuring the control via the F-DOs

Fail-safe digital outputs (F-DOs) supply feedback signals from selected safety functions. Signal interconnections are required for the evaluation of safety functions. Configure the F-DOs as follows:

1. Click the "Safe State" button.  
   A dialog with the same name opens. The "Safe State" function generates an overall status through an evaluation of the status signals of all available and enabled safety functions.
2. Select the individual signals of the individual Safety Integrated Functions to be linked for the Safe State evaluation.  
    For this purpose, click the connection icon ![Configuring the control via the F-DOs](images/141470326667_DV_resource.Stream@PNG-de-DE.PNG) in the row of the respective Safety Integrated Function. If the symbol shows a closed connection between two points (![Configuring the control via the F-DOs](images/141474457099_DV_resource.Stream@PNG-de-DE.PNG)), the Safety Integrated Function is linked with "Safe State" ([p10039](SINAMICS%20Parameter%20G220.md#p10039010-si-safe-state-signal-selection).0 to p10039.7).
3. Click "Close" to accept the settings and close the dialog.
4. Select the signal sources for F-DO 0 (X131.5) in the "F-DO configuration" area. You can create an AND logic operation for up to six signal sources and output the result at F-DO 0.  
   Make a corresponding signal interconnection for the individual signal sources (p10042[0] to 10042[5]).

**Performing the online test**

Via online tests it can be checked whether the two input signals of the F-DO always have the same signal state (high or low).

Two test procedures are suitable for the online tests of the F-DOs:

- Diagnostics using internal feedback signals
- Online test using entered dark pulses

  The converter here tests with test pulses during operation if the terminal has assumed a high signal state.

Proceed as follows:

1. Select the desired test procedure from the "Online test through" ([p10047](SINAMICS%20Parameter%20G220.md#p10047-si-f-do-diagnostics-mode-selection)) drop-down list.
2. If you have selected the test procedure with the dark pulses, then enter the desired dark pulse duration ([p10020](SINAMICS%20Parameter%20G220.md#p10020-si-f-do-self-test-dark-pulses-duration)).

   The test cycle has a fixed value of five seconds. The dark pulse duration must therefore be shorter.

###### Result

You have made the detailed settings for control via PROFIsafe. Save the settings in the project.

###### Additional parameters

- p9610

---

##### Control via PROFIsafe and emergency stop via terminals

###### Requirements

- The editing mode for Safety Integrated is [activated](#starting-and-ending-safety-integrated-commissioning).
- In the Safety Integrated [function selection](#selecting-the-safety-functionality), control "via PROFIsafe and EMERGENCY STOP via terminals" is enabled.
- The required Safety Functions of this control type are also activated in the function selection.

###### Configuring control via PROFIsafe

The PROFIsafe address is required for control of the Safety Integrated Functions via PROFIsafe.

1. Click the ![Configuring control via PROFIsafe](images/148900571915_DV_resource.Stream@PNG-de-DE.PNG) icon "Telegram configuration"

   The properties of the PROFINET interface are displayed in the Inspector window. The "Cyclic data exchange" setting area is active. The telegrams for the drive objects can be specified here.

   The following steps 2 and 3 apply if no PROFIsafe telegram has yet been created (e.g. via the guided quick startup).
2. Optional: Click in the telegram configuration of the "Drive control telegrams" on the entry <Add telegram>.
3. Optional: Select the "Add Safety telegram" option in the drop-down list of the entry:

   Then the lines "Send Safety Integrated Telegram (actual value)" and "Receive Safety Integrated Telegram (setpoint)" are inserted. The relevant PROFIsafe telegrams are preassigned.
4. Open the new function view "Receive Safety Integrated Telegram (setpoint)" in the Inspector window.
5. Set the PROFIsafe address of the drive in the "F-address" field.
6. Switch back to the "Control" function view. The value of the F-address is displayed in the "PROFIsafe address" ([p9610](SINAMICS%20Parameter%20G220.md#p9610-si-profisafe-destination-address)) field. A preassigned PROFIsafe telegram is displayed in the "PROFIsafe telegram no." drop-down list. The PROFIsafe failure response is permanently set to STO and cannot be changed.
7. Select the response for communication failure ([p9612](SINAMICS%20Parameter%20G220.md#p9612-si-stop-response-for-failure-or-control-fault)).

**Note**

**"SS1" set as failure response**

When PROFIsafe communication fails, the drive brakes the motor using function SS1.  
The drive continues braking even if PROFIsafe communication is restored before the end of braking.  
While braking, the drive ignores all commands that it receives via PROFIsafe.  
As long as the drive brakes the motor using function SS1, then controlling STO, for example, has no effect.

###### Configuring routing

The routing must also be configured to transfer the F-DI states via PROFIsafe. The following Safety Integrated telegrams are routing-capable: 902. A corresponding telegram therefore needs to be set for the routing. To ensure this, proceed as follows:

1. Click the ![Configuring routing](images/148900571915_DV_resource.Stream@PNG-de-DE.PNG) icon "Telegram configuration"

   The properties of the PROFINET interface are displayed in the Inspector window. The "Telegram configuration" setting area is active. The telegrams for the drive objects can be specified here.
2. Click the <Add telegram> entry in the telegram configuration of "Drive axis_x".
3. Select the "Add Safety Integrated telegram" option in the drop-down list of the entry.

   The "Send Safety Integrated telegram (Actual value)" and "Receive Safety Integrated telegram (Setpoint)" lines are then inserted.
4. In the "Telegram" column, select a routing-capable telegram in the drop-down list of the entry (see above).
5. Switch back to the "Control" function view of the drive.

   The "Configuration routing" area is now displayed.
6. Select the input mode of the failsafe digital inputs (F-DI) in the "Configuration routing" area.  
   To do so, select whether they should be NC or NO in the drop-down lists for the failsafe digital inputs ([p10040](SINAMICS%20Parameter%20G220.md#p1004002-si-f-di-input-mode).0 to p10040.2).
7. Click on the connection icon ![Configuring routing](images/141470326667_DV_resource.Stream@PNG-de-DE.PNG) (p10050.0 to p10050.2) beside the drop-down list of the respective failsafe digital input to activate the transfer of the F-DI state to the F-controller.  
   The transfer is activated when the symbol shows a closed connection between two points ![Configuring routing](images/141474457099_DV_resource.Stream@PNG-de-DE.PNG).

###### Configuring control via the F-DI

The signal states of an F-DI are monitored to determine whether they have assumed the same logical signal state within the discrepancy time.

The drive-internal Safety Integrated Function issues safety faults for internal faults or limit value violations.

1. Select whether an emergency stop is to be activated and which failure response (STO or SS1) is to apply in the event of an emergency stop using the drop-down list "Emergency stop via terminals". The EMERGENCY STOP functions, which were previously enabled in the function selection, can be selected.
2. Enter a discrepancy time [ms] in the "Discrepancy time" ([p10002](SINAMICS%20Parameter%20G220.md#p10002-si-f-di-changeover-discrepancy-time)) field.

   Based on the discrepancy time, the converter tolerates short-time differences in input signals. During this time the failsafe digital input (F-DI) remains guaranteed.

**Performing the online test**

Detailed information on possible self-tests is provided on Page [Self-test of the fail-safe digital input (F-DI)](#self-test-of-the-fail-safe-digital-input-f-di).

###### Configuring the control via the F-DOs

Failsafe digital outputs (F-DOs) supply feedback signals from selected safety functions. Signal interconnections are required for the evaluation of safety functions. Configure the F-DOs as follows:

1. Click the "Safe State" button.  
   A dialog with the same name opens. The "Safe State" function generates an overall status through an evaluation of the status signals of all available and enabled safety functions.
2. Select the individual signals of the individual Safety Integrated Functions to be linked for the Safe State evaluation.  
    For this purpose, click the connection icon ![Configuring the control via the F-DOs](images/141470326667_DV_resource.Stream@PNG-de-DE.PNG) in the row of the respective Safety Integrated Function. If the symbol shows a closed connection between two points (![Configuring the control via the F-DOs](images/141474457099_DV_resource.Stream@PNG-de-DE.PNG)), the Safety Integrated Function is linked with "Safe State" ([p10039](SINAMICS%20Parameter%20G220.md#p10039010-si-safe-state-signal-selection).0 to p10039.7).
3. Click "Close" to accept the settings and close the dialog.
4. Select the signal sources for F-DO 0 (X131.5) in the "F-DO configuration" area. You can create an AND logic operation for up to six signal sources and output the result at F-DO 0.  
   Make a corresponding signal interconnection for the individual signal sources (p10042[0] to 10042[5]).

**Performing the online test**

Via online tests it can be checked whether the two input signals of the F-DO always have the same signal state (high or low).

Two test procedures are suitable for the online tests of the F-DOs:

- Diagnostics using internal feedback signals
- Online test using entered dark pulses

  The converter here tests with test pulses during operation if the terminal has assumed a high signal state.

Proceed as follows:

1. Select the desired test procedure from the "Online test through" ([p10047](SINAMICS%20Parameter%20G220.md#p10047-si-f-do-diagnostics-mode-selection)) drop-down list.
2. If you have selected the test procedure with the dark pulses, then enter the desired dark pulse duration ([p10020](SINAMICS%20Parameter%20G220.md#p10020-si-f-do-self-test-dark-pulses-duration)).

   The test cycle has a fixed value of five seconds. The dark pulse duration must therefore be shorter.

###### Result

You have made the detailed settings for control via PROFIsafe and for emergency stop via terminals. Save the settings in the project.

###### Additional parameters

---

##### Control via terminals

###### Requirements

- The editing mode for Safety Integrated is [activated](#starting-and-ending-safety-integrated-commissioning).
- In the Safety Integrated [function selection](#selecting-the-safety-functionality), control "via terminals" is activated.
- The desired safety functions of this control type are also released in the function selection.

###### Configuring control via the F-DI

In the "F-DI configuration" field in the "Selection F-DI" area, configure the inputs of the selected Safety Integrated Extended Functions of the drive. The input terminals are low-active, i.e.:  
- 1 signal: Deselecting the function  
- 0 signal: Selecting the function

1. Configure the signal interconnection for the desired input terminal (c10022 to c10035) of a Safety Integrated Function.

   The input terminals can be connected for all Safety Integrated Functions enabled in the function selection. The SLS, SDI and SSM functions can be set statically active with the fixed value 0, this means the functions are therefore always active without selection.
2. If you want to activate acknowledgment of the Safety alarms, change the signal interconnection (c10006) to the fixed value 1 or a selected signal. The SLS, SDI and SSM functions can be set statically active with the fixed value 0, this means the functions are therefore always active without selection.
3. Configure the F-DI to connect antivalent sensors (NC/NO contact) or equivalent sensors (NC/NC contact).  
   To do this, select whether the F-DI should be NC contact or NO contact in the drop-down lists for the failsafe digital inputs ([p10040](SINAMICS%20Parameter%20G220.md#p1004002-si-f-di-input-mode).0 to p10040.2).
4. Enter a discrepancy time [ms] in the "Discrepancy time F-DI" field ([p10002](SINAMICS%20Parameter%20G220.md#p10002-si-f-di-changeover-discrepancy-time)).

   Based on the discrepancy time, the converter tolerates short-time differences in input signals. During this time the failsafe digital input (F-DI) remains guaranteed.

**Performing the online test**

Detailed information on possible self-tests is provided on Page [Self-test of the fail-safe digital input (F-DI)](#self-test-of-the-fail-safe-digital-input-f-di).

###### Configuring the control via the F-DOs

Failsafe digital outputs (F-DOs) supply feedback signals from selected safety functions. Signal interconnections are required for the evaluation of safety functions. Configure the F-DOs as follows:

1. Click the "Safe State" button.  
   A dialog with the same name opens. The "Safe State" function generates an overall status through an evaluation of the status signals of all available and enabled safety functions.
2. Select the individual signals of the individual Safety Integrated Functions to be linked for the "Safe State" evaluation.  
   For this purpose, click the connection icon ![Configuring the control via the F-DOs](images/141470326667_DV_resource.Stream@PNG-de-DE.PNG) in the row of the respective Safety Integrated Function. If the symbol shows a closed connection between two points (![Configuring the control via the F-DOs](images/141474457099_DV_resource.Stream@PNG-de-DE.PNG)), the Safety Integrated Function is linked with "Safe State" ([p10039](SINAMICS%20Parameter%20G220.md#p10039010-si-safe-state-signal-selection).0 to p10039.7). The signal sources selected here form the safe state via an OR logic operation.
3. Click "Close" to accept the settings and close the dialog.
4. Select the signal sources for F-DO 0 (X131.5) in the "F-DO configuration" area. You can create an AND logic operation for up to six signal sources and output the result at F-DO 0.  
   Make a corresponding signal interconnection for the individual signal sources (p10042[0] to 10042[5]).

**Performing the online test**

Via online tests it can be checked whether the two input signals of the F-DO always have the same signal state (high or low).

Two test procedures are suitable for the online tests of the F-DOs:

- Diagnostics using internal feedback signals
- Online test using entered dark pulses

  The converter here tests with test pulses during operation if the terminal has assumed a high signal state.

Proceed as follows:

1. Select the desired test procedure from the "Online test through" ([p10047](SINAMICS%20Parameter%20G220.md#p10047-si-f-do-diagnostics-mode-selection)) drop-down list.
2. If you have selected the test procedure with the dark pulses, then enter the desired dark pulse duration ([p10020](SINAMICS%20Parameter%20G220.md#p10020-si-f-do-self-test-dark-pulses-duration)).

   The test cycle has a fixed value of five seconds. The dark pulse duration must therefore be shorter.

###### Result

You have made the detailed settings for control via terminals. Save the settings in the project.

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

The debounce time ([p10017](SINAMICS%20Parameter%20G220.md#p1001702-si-digital-inputs-input-filter)) must be adapted to the particular test mode. If the debounce time is shorter than the test signal or dark pulse length, then the test pulse performs a switching operation.

###### Self-test with internal test signals

The drive internally generates test signals for the input circuit of the F-DI ([p10041](SINAMICS%20Parameter%20G220.md#p1004102-si-f-di-self-test-mode-selection) = 0).

The test signal length and the test cycle cannot be changed.

The following applies to the debounce time:

- p10017 > 2 ms

The self-test with internal test signals complies with the following requirements:

- Safety Integrity Level (SIL) 3 according to IEC 61800‑5‑2
- Performance Level (PL) e according to EN ISO 13849-1
- Category 3 according to EN ISO 138491.

###### Self-test using entered dark pulses

The drive provides switchable voltage source VS+ at terminal block X130. VS+ generates dark pulses, e.g. to diagnose the control circuit.

The self-test using specified dark pulses with VS+ (p10041 = 1) offers additional short-circuit detection between ground and 24 V.

The dark pulse length of the switchable power supply ([p10018](SINAMICS%20Parameter%20G220.md#p10018-si-f-di-self-test-length-dark-pulses-vs1vs2)) can be parameterized. The test cycle has a fixed value of 5 seconds.

![Dark pulses through switchable power supply](images/165216227339_DV_resource.Stream@PNG-en-US.png)

Dark pulses through switchable power supply

The following applies to the debounce time:

- p10017 > dark pulse length (p10018) + 2 ms

The self-test using entered dark pulses complies with the following requirements:

- Safety Integrity Level (SIL) 3 to IEC 61800-5-2
- Performance Level (PL) e according to EN ISO 13849-1
- Category 4 according to EN ISO 138491

###### Self-test using externally entered dark pulses

An electronic control, e.g. F-PLC, generates dark pulses at the input terminals of the F-DI (p10041 = 3).

The dark pulse length is determined by the control. The maximum wait time for dark pulses ([p10019](SINAMICS%20Parameter%20G220.md#p10019-si-f-di-self-test-external-dark-pulses-wait-time)) can be parameterized.

![Dark pulses through control](images/165215224843_DV_resource.Stream@PNG-en-US.png)

Dark pulses through control

The following applies to the debounce time:

- p10017 > dark pulse length + 2 ms

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

The function status shows the status of the enabled Safety Integrated Functions. If a function is active, then the status indicates "active" ([r9722](SINAMICS%20Parameter%20G220.md#r9722015-si-status-signals)). When STO and SS1 are active, then an Emergency Stop is initiated. When SLS, SDI and SSM are active, then the monitoring of the particular function is also active.

- Supplementary information (depending on the function)

  - Example of SLS: Displays the active level, the active SLS limit value and the speed actual value ([r9714](SINAMICS%20Parameter%20G220.md#r971404-si-diagnostics-velocity-1)).
- Status

  - Internal event

    Provides information as to whether internal events (e.g. software faults in the drive or a discrepancy in the monitoring channels) have been signaled and whether the communications function.
- Overview of the checksums:

  - Functional checksum ([p9780](SINAMICS%20Parameter%20G220.md#r978001-si-checksum-to-check-changes)) and time stamp ([r9781](SINAMICS%20Parameter%20G220.md#r978101-si-change-control-time-stamp-days))

    The checksum displays the functional checksum of the drive and is used to track changes (safety logbook). The functional checksum corresponds to a fingerprint of the parameterized Safety Integrated functionality on the drive. The checksum is updated after Safety Integrated has been commissioned. The time stamp displays the update time.
  - Functions (offline: [p9799](SINAMICS%20Parameter%20G220.md#p9799-si-reference-checksum-over-the-configuration-of-the-drive) and online: [r9798](SINAMICS%20Parameter%20G220.md#r9798-si-actual-checksum-over-the-drive-configuration)) and PROFIsafe (offline: [p9797](SINAMICS%20Parameter%20G220.md#p9797-si-reference-checksum-profisafe-addresses) and online: [r9796](SINAMICS%20Parameter%20G220.md#r9796-si-actual-checksum-profisafe-addresses))

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
  - OM-SMT firmware version

    Only displayed if an SMT option module is inserted.
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
| ![Status messages in detail](images/146631416203_DV_resource.Stream@PNG-de-DE.png) | Only for SMT:  Function is active, temperature thresholds have not been exceeded |

##### Additional parameters

---

#### Responses to safety faults and alarms

This section contains information on the following topics:

- [Faults and alarms](#faults-and-alarms)
- [Safety message buffer and safety message history](#safety-message-buffer-and-safety-message-history)
- [Fail-safe acknowledgment of safety messages](#fail-safe-acknowledgment-of-safety-messages)
- [Stop responses](#stop-responses)
- [Stop response priorities](#stop-response-priorities)

##### Faults and alarms

###### Definitions

A message comprises a letter followed by the relevant number.

The letters have the following meaning:

- A means "Alarm"
- F means "Fault"
- N means "No message" or "Internal message"
- C means "Safety message"

  In the factory state ([p3117](SINAMICS%20Parameter%20G220.md#p3117-change-safety-message-type) = 0), safety messages correspond to message type "C" and the safety message buffer is active. With p3117 = 1, safety messages correspond to message types "A" or "F". Therefore, search for Safety Integrated messages in this list only by their number without the message type (e.g. 01711).

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

In the factory state ([p3117](SINAMICS%20Parameter%20G220.md#p3117-change-safety-message-type) = 0), safety messages correspond to message type "C" and the safety message buffer is active. With p3117 = 1, safety messages correspond to the message types Alarm (A) or Fault (F) and are stored in the fault buffer or the alarm buffer.

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

Entry in the message buffer is made with a delay. Read the message buffer only after the converter detects a change in the buffer ([r60044](SINAMICS%20Parameter%20G220.md#r60044-si-message-buffer-counter-changes)).

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

The message buffer can be deleted as follows: [p60052](SINAMICS%20Parameter%20G220.md#p60052-si-message-cases-counter) = 0.

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

You can directly select and thus activate stop functions/responses such as STO or SS1 via the function selection.

If the stop/subsequent responses are not already activated in the function selection, they are enabled by the system so that they can be parameterized.

![Overview of stop variants from SINAMICS FW V6.1](images/159829657099_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| SS1 | Safe Stop1 |
| SCF | Safety channel failed |

Overview of stop variants from SINAMICS FW V6.1

If a discrepancy is detected in the monitoring channels of Safety Integrated (e.g. error in result and data comparison), an SCF (Safety channel failed) is triggered. The transition to the stop response SS1 can be handled with the delay time (p9555).

---

**See also**

[Motion monitoring functions](#motion-monitoring-functions)

##### Stop response priorities

###### Overview

If several Safety Integrated Functions or stop responses are simultaneously active, the motor response is defined by the priority of the particular function.

###### Description

The priority defines whether a stop response or a stop function influences another active Safety Integrated Function.

Stop responses and stop functions have a higher priority than all other Safety Integrated Functions.

Stop responses and stop functions have different priorities.

Stop response priorities

| Priority classes | Stop responses |
| --- | --- |
| Raise | Select the Safe Torque Off (STO) |
| Lower | Select Safe Stop 1 (SS1) |

A stop response or stop function with a higher priority influences an active stop response or stop function with a lower priority.

A stop response or stop function with a lower priority does not influence an active stop response or stop function with a higher priority.

###### Example

Examples for the response of the motor for a stop response or when selecting a stop function:

- Safely-Limited Speed (SLS) is active and Safe Stop1 (SS1) is selected.

  Result: The drive brakes the motor as stop function Safe Stop1 (SS1) has a higher priority than Safely-Limited Speed (SLS).
- Safely-Limited Speed (SLS) is active, and the converter detects a limit value violation.

  Safe Torque Off (STO) is set as stop response to a limit value violation.

  Stop function Safe Stop1 (SS1) is selected during the stop response.

  Result: Selecting Safe Stop1 (SS1) does not influence the motor response. The motor coasts down as Safe Torque Off (STO) has a higher priority than Safe Stop1 (SS1).

### Technology functions

This section contains information on the following topics:

- [Technology controller](#technology-controller)

#### Technology controller

This section contains information on the following topics:

- [Description of function](#description-of-function-6)
- [Technology motorized potentiometer](#technology-motorized-potentiometer)
- [Technology fixed setpoints](#technology-fixed-setpoints)
- [Technology setpoints / actual values](#technology-setpoints-actual-values)
- [Technology PID controller](#technology-pid-controller)

##### Description of function

###### Overview

Simple closed-loop control functions can be implemented with the technology controller, e.g.:

- Level control
- Temperature control
- Dancer roll position control
- Pressure control
- Flow control
- Simple closed-loop controls without higher-level controller
- Tension control

###### Description of function

The technology controller is designed as a PID controller. Whereby the derivative-action element can be switched to the control deviation channel or the actual value channel (factory setting). The P, I, and D components can be set separately. A value of 0 deactivates the corresponding component. Setpoints can be specified via two signal sinks. Setpoints can be scaled via parameters. A ramp-function generator in the setpoint channel can be used to set the setpoint ramp-up/ramp-down time via parameters. The setpoint and actual value channels each have a smoothing element. The smoothing time can be set via parameters.

**Features of the technology controller:**

- Two scalable setpoints
- Scalable output signal
- Integrated fixed values
- Integrated motorized potentiometer
- The output limits are activated and deactivated via the ramp-function generator.
- The D component can be switched to the control deviation or actual value channel.
- The motorized potentiometer of the technology controller is active only when the drive pulses are enabled.

##### Technology motorized potentiometer

This section contains information on the following topics:

- [Configuring the technology motorized potentiometer](#configuring-the-technology-motorized-potentiometer)
- [Configuring the ramp-function generator (motorized potentiometer)](#configuring-the-ramp-function-generator-motorized-potentiometer-1)

###### Configuring the technology motorized potentiometer

###### Overview

The motorized potentiometer enables a setpoint to be specified for the technology controller. The setpoint is specified via a ramp-function generator.

###### Requirements

- The drive has been completely created and fully specified in the device configuration.
- The [extended parameterization](#overview-2) is active.

  In the standard parameterization, only some of the settings described below can be made.

###### Procedure

1. Interconnect the "Raise setpoint" signal source (c2235) to increase the setpoint.
2. Interconnect the "Lower setpoint" signal source (c2236) to decrease the setpoint.
3. Correct the specified value for the upper limit of the speed setpoint in % in the "Maximum value" field ([p2237](SINAMICS%20Parameter%20G220.md#p22370n-technology-controller-motorized-potentiometer-maximum-value)).
4. Correct the specified value for the lower limit of the speed setpoint in % in the "Minimum value" field ([p2238](SINAMICS%20Parameter%20G220.md#p22380n-technology-controller-motorized-potentiometer-minimum-value)).
5. Configure the ramp-function generator of the motorized potentiometer (see "[Motorized potentiometer ramp-function generator](#configuring-the-ramp-function-generator-motorized-potentiometer-1)").
6. To save the setpoint after switching the motor off, select "Yes" in the "Saving active" drop-down list.
7. To save the setpoint protected against power failure, select "Yes" in the "Non-volatile saving active" drop-down list.
8. Interconnect the "Setpoint after RFG" ([r2250](SINAMICS%20Parameter%20G220.md#r2250-technology-controller-motorized-potentiometer-setpoint-after-rfg)) signal sink to display the effective setpoint after the internal ramp-function generator for the motorized potentiometer of the technology controller.

###### Result

The detailed settings of the motorized potentiometer have been made.

###### Function diagrams (FD)

Motorized potentiometer - 7954 -

###### Additional parameters

---

###### Configuring the ramp-function generator (motorized potentiometer)

###### Overview

The ramp-function generator ramps the setpoint up and down without acceleration jumps. The ramp-function generator is parameterized via the ramp-up time and ramp-down time parameters. The times refer to the time needed to reach the reference setpoint (0% or 100%) in the specified time.

###### Requirements

- The drive has been completely created and fully specified in the device configuration.
- The [extended parameterization](#overview-2) is active.

  In the standard parameterization, the "Motorized potentiometer technology ramp-function generator" dialog cannot be parameterized.

###### Procedure

1. Click the "Ramp-function generator" button in the "Technology motorized potentiometer" function view.

   The "Motorized potentiometer technology ramp-function generator" dialog opens. The initial rounding is active by default.
2. If you do not require an initial rounding, select "No" in the "Initial rounding active" drop-down list.

   The set ramp-up or ramp-down time can be exceeded with the initial rounding.
3. Correct the specified default value in the "Ramp-up time" ([p2247](SINAMICS%20Parameter%20G220.md#p22470n-technology-controller-motorized-potentiometer-ramp-up-time)) field.
4. Correct the specified default value in the "Ramp-down time" ([p2248](SINAMICS%20Parameter%20G220.md#p22480n-technology-controller-motorized-potentiometer-ramp-down-time)) field.
5. Enter the desired start value for the motorized potentiometer in the "Start value" ([p2240](SINAMICS%20Parameter%20G220.md#p22400n-technology-controller-motorized-potentiometer-starting-value)) field.

   This value takes effect when the drive is switched on.
6. Correct the specified maximum value for the motorized potentiometer of the technology controller in the field of the same name ([p2237](SINAMICS%20Parameter%20G220.md#p22370n-technology-controller-motorized-potentiometer-maximum-value)).
7. Correct the specified minimum value for the motorized potentiometer of the technology controller in the field of the same name ([p2238](SINAMICS%20Parameter%20G220.md#p22380n-technology-controller-motorized-potentiometer-minimum-value)).
8. Once all necessary settings have been made, click "Close".

###### Result

The dialog closes. The detailed settings for this ramp-function generator are completed.

###### Function diagrams (FD)

Motorized potentiometer - 7954 -

###### Additional parameters

---

##### Technology fixed setpoints

This section contains information on the following topics:

- [Configuring fixed setpoints technology controller](#configuring-fixed-setpoints-technology-controller)

###### Configuring fixed setpoints technology controller

###### Overview

You can select the fixed setpoints of the technology controller via a direct selection or a binary selection. Fixed setpoints are speed setpoints freely stored by the user.

###### Requirements

- The drive has been completely created and fully specified in the device configuration.
- The [extended parameterization](#overview-2) is active.

  In the standard parameterization, only some of the settings described below can be made.

###### Selecting fixed setpoints via direct selection

1. Select the "[1] Direct selection" method from the "Fixed value selection method" ([p2216](SINAMICS%20Parameter%20G220.md#p22160n-technology-controller-fixed-value-selection-method)) drop-down list.
2. Interconnect the four signal sources for setting the selection bit of the speed setpoint.

   - Bit 0: c2220
   - Bit 2: c2221
   - Bit 2: c2222
   - Bit 3: c2223
3. Interconnect the "Fixed value selected" ([r2225](SINAMICS%20Parameter%20G220.md#r22250-technology-controller-fixed-value-selection-status-word)) signal sink to display the status of the fixed setpoints (0/1 = off/on).
4. Enter fixed speed setpoints in the "Fixed value 1...4" ([p2201](SINAMICS%20Parameter%20G220.md#p22010n-technology-controller-fixed-value-1)...[p2204](SINAMICS%20Parameter%20G220.md#p22040n-technology-controller-fixed-value-4)) fields.

   The effective speed setpoint then results from the addition of the individual speed setpoints according to the selection bits.
5. Click the "Interconnections" button.

   The "Technology fixed setpoint interconnection" dialog opens.
6. Interconnect the "Fixed value 1...15" fixed values (p2201...[p2215](SINAMICS%20Parameter%20G220.md#p22150n-technology-controller-fixed-value-15)) via the connected signal sources.
7. Once all necessary settings have been made in the dialog, click "Close".

   The dialog closes.
8. Interconnect the "Fixed value active" ([r2224](SINAMICS%20Parameter%20G220.md#r2224-technology-controller-fixed-value-effective)) signal source to display the active fixed speed setpoint.

###### Selecting fixed setpoints via binary selection

1. Select the "[2] Binary selection" method from the "Fixed value selection method" (p2216) drop-down list.
2. Interconnect the four signal sources for setting the selection bit of the speed setpoint.

   - Bit 0: c2220
   - Bit 2: c2221
   - Bit 2: c2222
   - Bit 3: c2223
3. Interconnect the "Fixed value selected" (r2225) signal sink to display the status of the fixed setpoints (0/1 = off/on).
4. Enter fixed speed setpoints in the "Fixed value 1...15" (p2201...p2215) fields.

   The effective speed setpoint then results from the addition of the individual speed setpoints according to the selection bits.
5. Click the "Interconnections" button.

   The "Technology fixed setpoint interconnection" dialog opens.
6. Interconnect the "Fixed value 1...15" fixed values (p2201...p2215) via the connected signal sources.
7. Once all necessary settings have been made in the dialog, click "Close".

   The dialog closes.
8. Interconnect the "Fixed value active" (r2224) signal source to display the active fixed speed setpoint.

###### Result

The fixed setpoints have been parameterized.

###### Function diagrams (FD)

Fixed values, binary selection (p2216 = 2) - 7950 -

Fixed values, direct selection (p2216 = 1) - 7951 -

###### Additional parameters

---

##### Technology setpoints / actual values

This section contains information on the following topics:

- [Configuring setpoints/actual values technology](#configuring-setpointsactual-values-technology)
- [Configuring technology setpoint ramp-function generator](#configuring-technology-setpoint-ramp-function-generator)

###### Configuring setpoints/actual values technology

###### Overview

The converter contains an integrated technology controller (PID controller) for simple closed-loop control functions such as level control or temperature control. The P, I and D component can each be set and switched off separately. Switching off is performed by entering a "0" in the appropriate parameter (p2200).

###### Requirements

- The drive has been completely created and fully specified in the device configuration.
- The [extended parameterization](#overview-2) is active.

  In the standard parameterization, only some of the settings described below can be made.

###### Parameterizing setpoints 1 and 2

1. Interconnect the signal source for setpoint 1 of the technology controller at "Setpoint 1" (c2253).

   The PID motorized potentiometer, fixed setpoints, analog inputs or the fieldbus interface can be used as the setpoint source.
2. To scale setpoint 1, enter a value between 0 ... 100% at "Setpoint 1 scaling" ([p2255](SINAMICS%20Parameter%20G220.md#p2255-technology-controller-setpoint-1-scaling)).
3. Interconnect the signal source for setpoint 2 of the technology controller at "Setpoint 2" (c2254).

   The additional setpoint is added to the main setpoint.
4. To scale setpoint 2, enter a value between 0 ... 100% at "Setpoint 2 scaling" ([p2256](SINAMICS%20Parameter%20G220.md#p2256-technology-controller-setpoint-2-scaling)).
5. If required, parameterize the ramp-function generator of the setpoint technology controller (see "[Configuring technology setpoint ramp-function generator](#configuring-technology-setpoint-ramp-function-generator)").
6. Enter a value for the smoothing time in the "Setpoint filter" field ([p2261](SINAMICS%20Parameter%20G220.md#p2261-technology-controller-setpoint-filter-time-constant)).

   The setpoint filter is implemented as a PT1 element.

###### Parameterizing the actual value source and the actual value function

1. Interconnect the signal source for the actual value of the technology controller at "Actual value" (c2264).
2. In order to apply a smoothing filter to the actual value, enter a value between 0 ... 60 s in the "Actual value filter" field ([p2265](SINAMICS%20Parameter%20G220.md#p2265-technology-controller-actual-value-filter-time-constant)).
3. To activate the actual value limit (p2253.3), select the "Yes" option in the "Actual value limit" ([p2252](SINAMICS%20Parameter%20G220.md#p225208-technology-controller-configuration).3) drop-down list.
4. To limit the actual value, enter a value for the upper limit in the "Upper limit actual value" ([p2267](SINAMICS%20Parameter%20G220.md#p2267-technology-controller-upper-limit-actual-value)) field and a value for the lower limit in the "Lower limit actual value" ([p2268](SINAMICS%20Parameter%20G220.md#p2268-technology-controller-lower-limit-actual-value)) field.
5. Select which function is to be used on the actual value in the "Actual value function" ([p2270](SINAMICS%20Parameter%20G220.md#p2270-technology-controller-actual-value-function)) drop-down list:

   - Output (y) = input (x)
   - Square root function (square root from x)
   - Square function (x * x)
   - Cubic function (x * x * x)
6. If you want to invert the actual value, select the "Inversion actual value signal" option in the "Actual value inversion (sensor type)" ([p2271](SINAMICS%20Parameter%20G220.md#p2271-technology-controller-actual-value-inversion-sensor-type)) drop-down list.
7. Enter a value in [%] for the gain in the "Gain actual value" ([r2269](SINAMICS%20Parameter%20G220.md#p2269-technology-controller-gain-actual-value)) field.

###### Result

The actual values and setpoints are configured.

###### Function diagrams (FD)

Closed-loop control, vector (Part 2) - 7958 -

###### Additional parameters

---

###### Configuring technology setpoint ramp-function generator

###### Overview

Ramp-up and ramp-down times prevent sudden setpoint jumps and therefore abrupt acceleration. A change at the PID controller input is passed on to the output via a defined ramp.

###### Requirements

- The drive has been completely created and fully specified in the device configuration.
- The [extended parameterization](#overview-2) is active.

  In the standard parameterization, the "Technology setpoint ramp-function generator" dialog cannot be parameterized.

###### Procedure

1. Click the "Ramp-function generator" button in the "Technology setpoints / actual values" function view.

   The "Technology setpoint ramp-function generator" dialog opens.
2. The "Acceleration/deceleration ramp independent of setpoint sign" option is active by default.

   Deactivate this option if required.
3. Correct the default value in the "Ramp-up time" ([p2257](SINAMICS%20Parameter%20G220.md#p2257-technology-controller-ramp-up-time)) field.
4. Correct the default value in the "Ramp-down time" ([p2258](SINAMICS%20Parameter%20G220.md#p2258-technology-controller-ramp-down-time)) field.
5. Once all necessary settings have been made, click "Close".

###### Result

The dialog closes. The settings for the ramp-function generator are completed.

###### Function diagrams (FD)

Closed-loop control, vector (Part 2) - 7958 -

###### Additional parameters

---

##### Technology PID controller

This section contains information on the following topics:

- [Configuring PID controller technology](#configuring-pid-controller-technology)
- [Configuring Kp/Tn adaptation of the PID controller](#configuring-kptn-adaptation-of-the-pid-controller)
- [Configuring the limitation of the PID controller](#configuring-the-limitation-of-the-pid-controller)

###### Configuring PID controller technology

###### Overview

The technology controller is configured optionally as P, I, PI, or PID controller.

The value 0 deactivates the corresponding controller component.

###### Requirements

- The drive has been completely created and fully specified in the device configuration.
- The [extended parameterization](#overview-2) is active.

  In the standard parameterization, only some of the settings described below can be made. In this case in particular, the signal interconnections are not present.

###### Procedure

Proceed as follows to parameterize the PI component of the controller as well as the proportional gain and the integral time:

1. Enter a value in the "Proportional gain" ([p2280](SINAMICS%20Parameter%20G220.md#p2280-technology-controller-proportional-gain)) field.
2. Enter a value in the "Integral time" ([p2285](SINAMICS%20Parameter%20G220.md#p2285-technology-controller-integral-time)) field.
3. If you do not require a Kp/Tn adaptation, configure this adaptation vi a downstream dialog (see "[Configuring Kp/Tn adaptation of the PID controller](#configuring-kptn-adaptation-of-the-pid-controller)").
4. Click the large button connected to the button for the Kn/Tn adaptation.

   Dialog "PID controller" opens.
5. Interconnect the signal source to hold the integrator for the technology controller at "Hold integrator" (c2286).
6. Deactivate the "Integrator independent of Kp" ([p2252](SINAMICS%20Parameter%20G220.md#p225208-technology-controller-configuration).1) option to evaluate the integration time of the PID controller with the gain factor Kp (p2280).
7. Enter a value for the "Differentiation" ([p2274](SINAMICS%20Parameter%20G220.md#p2274-technology-controller-differentiation-time-constant)).
8. Select one of the following options in the "Technology controller type" ([p2263](SINAMICS%20Parameter%20G220.md#p2263-technology-controller-type)) drop-down list:

   - [0] D component in the actual value signal

     With this setting, the differential component of the controller is applied to the actual value signal. You use this setting, for example if the actual value signal has significant fluctuations, which should be quickly filtered out in the setpoint using the D component in the controller.
   - [1] D component in the control deviation

     The differential component of the controller is used on the setpoint / actual value difference with this setting.
9. Once all necessary settings have been made, click "Close".

   The dialog closes. The settings are accepted on the "Technology PID controller" function view.
10. Interconnect the signal source for the precontrol at "Precontrol signal" (c2289).
11. Interconnect the signal source for the enabling signal at "Enable" (c2200).
12. If required, also configure the limits of the PID controller (see "[Configuring the limitation of the PID controller](#configuring-the-limitation-of-the-pid-controller)").
13. If required, correct the interconnection of the "Technology controller output scaling" (c2296) signal source for scaling the technology controller output.

    Parameter [p2295](SINAMICS%20Parameter%20G220.md#p2295-technology-controller-output-scaling) is interconnected as default setting. If you want to use a different value for the scaling, change the interconnection.
14. To directly scale the technology controller, enter a value between -100...100% in the "Output scaling" (p2295) field.

    You can make the following additional settings with the default setting of the technology controller mode (...as main speed setpoint):
15. Enter the start value for the output of the technology controller as percentage in field "Output signal signal value" ([p2302](SINAMICS%20Parameter%20G220.md#p2302-technology-controller-output-signal-starting-value)).

    If the technology controller is already enabled (see r2200, [r0056](SINAMICS%20Parameter%20G220.md#r0056015-status-word-closed-loop-control).3), then its output signal [r2294](SINAMICS%20Parameter%20G220.md#r2294-technology-controller-output-signal) first goes to the start value p2302, before the controller starts to operate.
16. Alternatively, you can also define the technology controller response when fault F07426 occurs. To do this, click on "Fault response".

    Dialog "Fault response" opens.
17. In the drop-down list "Technology controller fault response" ([p2345](SINAMICS%20Parameter%20G220.md#p2345-technology-controller-fault-response)), select the required fault response.

    This function is locked as default setting.
18. If you have selected fault response "For fault: Switch over to [p2215](SINAMICS%20Parameter%20G220.md#p22150n-technology-controller-fixed-value-15)", then enter "Technology controller fixed value 15 (p2215).
19. Then close the dialog box.

###### Deviations when the technology controller mode is changed

| Technology controller mode | Response |
| --- | --- |
| [0] Technology controller as main speed setpoint | See above, starting at Step 15.  Selected as default setting. |
| [1] Technology controller as supplementary speed setpoint | See the sequence above up to Step 14. Any additional setting is not required. |
| [2] Technology controller can be freely interconnected | See the sequence above up to Step 14.  You can then interconnect "Output signal" (r2294) signal sink to display the output signal of the technology controller. |

> **Note**
>
> The two technology controller modes [1] and [2] are only active if enable signal r2200 is interconnected (Step 11).

###### Result

The PID controller is configured.

###### Function diagrams (FD)

Closed-loop control, vector (Part 2) - 7958 -

###### Additional parameters

---

###### Configuring Kp/Tn adaptation of the PID controller

###### Overview

You can optionally activate and configure the Kp/Tn adaptation of the PID controller. Whereby, you can specify whether you require only a Kp or only a Tn adaptation or whether you require both adaptations together and have to configure them for your purposes.

###### Requirements

- The drive has been completely created and fully specified in the device configuration.
- The [extended parameterization](#overview-2) is active.

  In the standard parameterization, the "Kp/Tn adaptation" dialog cannot be parameterized.

###### Procedure

The Kp/Tn adaptation is deactivated when calling the "Technology PID controller" function view the first time. If you want to use an adaptation, proceed as follows:

1. Select the "[1] Yes" option in both drop-down lists below the "Kp/Tn adaptation" button. If you only want to use one of the two adaptations, only select the Yes option in the appropriate drop-down list.

   The "Kp/Tn adaptation" button is switched active.
2. Click the "Kp/Tn adaptation" button.

   The configuration dialog with the same name opens. The configuration options in the dialog depend on whether you have activated only one or both adaptation options. The activation of both adaptations is assumed in the following.
3. Interconnect the "Kp scaling" (c2315) signal source for scaling the result of the adaptation of the proportional gain Kp for the technology controller.

   This field is only displayed if Kp adaptation is activated.
4. Interconnect the "Kp input value" (c2310) signal source for the input value of the adaptation of the proportional gain Kp for the technology controller.
5. Correct the specified values in the fields:

   - "Upper Kp starting point" ([p2314](SINAMICS%20Parameter%20G220.md#p2314-technology-controller-kp-adaptation-upper-starting-point))
   - "Upper Kp value" ([p2312](SINAMICS%20Parameter%20G220.md#p2312-technology-controller-kp-adaptation-upper-value))
   - "Lower Kp value" ([p2311](SINAMICS%20Parameter%20G220.md#p2311-technology-controller-kp-adaptation-lower-value))
   - "Lower Kp starting point" ([p2313](SINAMICS%20Parameter%20G220.md#p2313-technology-controller-kp-adaptation-lower-starting-point))
6. Interconnect the "Tn input value" (c2317) signal source for the input value of the adaptation of the integral time Tn for the technology controller.

   This field is only displayed if Tn adaptation is activated.
7. Correct the specified values in the fields:

   - "Upper Tn starting point" ([p2321](SINAMICS%20Parameter%20G220.md#p2321-technology-controller-tn-adaptation-upper-starting-point))
   - "Lower Tn value" ([p2319](SINAMICS%20Parameter%20G220.md#p2319-technology-controller-tn-adaptation-lower-value))
   - "Upper Tn value" ([p2318](SINAMICS%20Parameter%20G220.md#p2318-technology-controller-tn-adaptation-upper-value))
   - "Lower Tn starting point" ([p2320](SINAMICS%20Parameter%20G220.md#p2320-technology-controller-tn-adaptation-lower-starting-point))
8. Once all necessary settings have been made, click "Close".

###### Result

The dialog closes. The settings are applied to the "Technology PID controller" function view.

###### Function diagrams (FD)

Kp-/Tn adaptation and Kp-/Tn selection - 7959 -

###### Additional parameters

---

###### Configuring the limitation of the PID controller

###### Overview

For some applications, the PID output variable must be limited to defined values. This can be achieved using fixed limits. To prevent large jumps of the PID controller output when the device is switched on, these PID output limits will be ramped-up via the ramp time from 0 to the appropriate values (upper limit for the PID output or lower limit for the PID output). As soon as the limits are reached, the dynamic response of the PID controller is no longer limited by this ramp-up/ramp-down time.

The limits are entered in [%].

###### Requirements

- The drive has been completely created and fully specified in the device configuration.
- The [extended parameterization](#overview-2) is active.

  In the standard parameterization, the "Technology PID controller limits" dialog cannot be parameterized.

###### Procedure

1. Click the "Controller limited" button.  
   The "Technology PID controller limits" dialog opens.
2. Deactivate the "Output signal without ramp" ([p2252](SINAMICS%20Parameter%20G220.md#p225208-technology-controller-configuration).2) option to reduce the output signal [r2294](SINAMICS%20Parameter%20G220.md#r2294-technology-controller-output-signal) via the deceleration ramp [p2293](SINAMICS%20Parameter%20G220.md#p2293-technology-controller-ramp-upramp-down-time) to zero.
3. Interconnect the "Limit offset" (c2299) signal source for the offset of the output limiting of the technology controller.
4. Enter a value in the "Maximum limiting" ([p2291](SINAMICS%20Parameter%20G220.md#p2291-technology-controller-maximum-limiting)) field.
5. Interconnect the "Maximum limiting" (c2297) signal source for the maximum limiting of the technology controller.
6. Enter a value in the "Minimum limiting" ([p2292](SINAMICS%20Parameter%20G220.md#p2292-technology-controller-minimum-limiting)) field.
7. Interconnect the "Minimum limiting" signal source (c2298) for the minimum limiting of the technology controller.
8. Enter a value (in seconds) for the ramp-up and ramp-down time for the output signal of the technology controller in the "Ramp-up/ramp-down time" (p2293) field.
9. Interconnect the "Limiting enable" (c2290) signal source to enable the technology controller output.
10. Once all necessary settings have been made, click "Close".

###### Result

The dialog closes. The settings are accepted on the "Technology PID controller" function view.

###### Function diagrams (FD)

Closed-loop control, vector (Part 2) - 7958 -

###### Additional parameters

---

## Rotate & optimize

This section contains information on the following topics:

- [Overview](#overview-5)
- [Control panel](#control-panel)
- [Stationary/rotating measurement](#stationaryrotating-measurement)
- [Switching data sets during optimization](#switching-data-sets-during-optimization)

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
- There is an active [online connection](Configuring%20SINAMICS%20G220%20drives.md#establishing-an-online-connection-to-the-target-device) between the drive and the operating unit.
- If the project protection is activated:

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

---

**See also**

[Rotate & optimize](#rotate-optimize)

### Control panel

This section contains information on the following topics:

- [Traverse the drive from the control panel by specifying the speed](#traverse-the-drive-from-the-control-panel-by-specifying-the-speed)

#### Traverse the drive from the control panel by specifying the speed

##### Overview

You can use the control panel to traverse the drive and therefore test the settings that have been made.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Danger to life if the safety instructions for the control panel are not observed**  The safety shutdowns from the higher-level controller have no effect with this function. The **Stop with spacebar** function is not guaranteed in all operating modes. Incorrect operation by untrained personnel and non-observance of the appropriate safety instructions can result in death or serious injury.   - Make sure that this function is only used for commissioning, diagnostic and service purposes. - Make sure that this function is only used by trained and authorized skilled personnel. - Make sure that the EMERGENCY OFF circuit is always implemented as hardware. |  |

> **Note**
>
> **Drive responds immediately**
>
> Although all enables are removed before returning the master control, the setpoints and commands still come from the original parameterized sources after the control priority is returned.

##### Requirements

- An online connection to the drive has been established.
- If the project protection is activated:

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

##### Step 1: Activate master control

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
| 1. Click the "Activate" button under "Master control".    The "Activate master control" message window opens. 2. Read the warning carefully. Check the monitoring time and if required, correct it.    The monitoring time specifies the time during which the connection from the operating unit to the drive is cyclically monitored. The minimum value is 1000 ms. 3. The "Stop with spacebar" option is active by default. When the option is activated the drive is always braked using the shutdown function OFF3 if you press the spacebar or if the focus switches. The focus switches when a dialog is opened (e.g. download dialog) or when switching from TIA Portal to another application.       | Symbol | Meaning |    | --- | --- |    |  | **Warning** |    | **Braking not guaranteed if the "Stop with spacebar" option is deactivated** Stopping by using the buttons on the control panel cannot be guaranteed in extreme operating modes. If the additional braking function "Stop with spacebar" is deactivated, it may no longer be possible to brake the motor via the TIA Portal. This can lead to accidents resulting in death or serious injury.  - Only deactivate the "Stop with spacebar" option in absolute exceptional cases and if it has been ensured that you are able to stop the drive safely using suitable hardware solutions. |  |     - Optional: If you do not want to use the "Stop with spacebar" option, deactivate this option in the message window.       This setting requires a safety confirmation. The message window cannot be closed without confirmation.    - Also activate the "Continue without quick stop function via spacebar and focus switch" option. 4. To close the message window, click the "OK" button.     The message window closes. The master control is then active. |  |

##### Step 2: Set the drive enable

To set the required enable for the control panel, proceed as follows:

1. Click the "Set" button under "Drive enables".

   Further areas of the control panel are activated.
2. Click the "Acknowledge faults" button to acknowledge the currently active faults.
3. If you no longer require the enables, click the "Reset" button under "Drive enables".

##### Step 3: Traverse drive

To traverse the drive, proceed as follows:

1. Switch the motor on.
2. Enter a speed setpoint at which the motor is to turn in the "Speed" field of the "Control panel" function view.
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

The motor continues to rotate while you keep the mouse clicked on the button. Traversing stops when you release the mouse button.

##### Step 4: Deactivate master control

Proceed as follows to return the master control:

1. Click the "Off" button to stop the drive.

   This is a basic requirement for deactivating the master control.
2. Click the "Deactivate" button under "Master control".

   The grayed-out user interface of the control panel indicates that the master control is deactivated.

##### Result

The current values of various parameters are displayed at "Actual values". Enables and faults are displayed at "Drive status". The currently active fault is displayed next to "Active fault".

##### Additional parameters

---

### Stationary/rotating measurement

This section contains information on the following topics:

- [Motor data identification procedure](#motor-data-identification-procedure)
- [Performing a stationary/rotating measurement](#performing-a-stationaryrotating-measurement)
- [Parameter values (for experts)](#parameter-values-for-experts)

#### Motor data identification procedure

##### Overview

The motor identification (MotID) helps with determining the motor data, for example, for third-party motors. The MotID should be executed to improve the control properties of the motor. Especially for encoderless speed control, as a minimum the stator resistance (including the supply cable resistance) and the power unit parameters must be determined for each drive. This is required so that the observer model can operate correctly even for very low speeds.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Damage to the device as a result of incorrectly selected rated current and/or maximum current values**  Incorrect rated current or maximum current data can destroy the motor!  - Check that the entered current values are correct. |  |

> **Note**
>
> **Loss of the determined motor data during restart**
>
> If a POWER ON or a warm restart is performed when motor data identification is selected, the motor data identification request is lost. A desired motor data identification must be reselected manually after ramp-up.

> **Note**
>
> For the duration of the period in which a rotating measurement is selected and running, the following actions or functions cannot be carried out:
>
> - Upload (upload from device)
> - Download (download to device)
> - Save retentively (copy RAM to ROM)
> - Restoring factory settings​​​

##### Motor data identification procedure

1. Configure the motor data
2. Perform the motor identification for a cold motor
3. Perform a stationary measurement, see [Stationary measurement](#performing-a-stationaryrotating-measurement).
4. Perform a rotating measurement for a motor running without load, see [Rotating measurement](#performing-a-stationaryrotating-measurement).

   For the rotational measurement, the motor should be disconnected from the machine to prevent damage to the mechanical system
5. Calculating the motor and closed-loop control parameters.

##### Additional parameters

---

#### Performing a stationary/rotating measurement

##### Overview

The "Measurement type" setting area shows the available measurement types. When the function view is opened, a check is made to determine whether a measurement is already active and, if so, it will be displayed. If no measurement is selected, a check is made as to which measurement has already been performed and then used as a recommendation.

Following the basic parameterization in the guided quick startup and subsequent download, the "Stationary measurement" measurement type is active since the "Calculation of motor/control parameters" has already been performed.

##### Requirements

- An online connection to the drive has been established.
- If project protection is activated:

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

##### Step 1: Activate master control

When an online connection has been established, the bar in the header area is shown in color. The control elements are grayed-out apart from the "Activate" button. The remaining control elements become active only after you have activated the master control and set the enables.

> **Note**
>
> **Project lock not available when master control is active**
>
> As long as the master control for a drive is active, you cannot activate the project lock if project protection is active and the automatic project lock on inactivity is also suspended.

The master control can only be activated for one drive.

| Symbol | Meaning |
| --- | --- |
| 1. Click the "Activate" button under "Master control".    The "Activate master control" message window opens. 2. Read the warning carefully. Check the monitoring time and if required, correct it.    The monitoring time specifies the time during which the connection from the operating unit to the drive is cyclically monitored. The minimum value is 1000 ms. 3. The "Stop with spacebar" option is active by default. When the option is activated the drive is always braked using the shutdown function OFF3 if you press the spacebar or if the focus switches. The focus switches when a dialog is opened (e.g. download dialog) or when switching from TIA Portal to another application.       | Symbol | Meaning |    | --- | --- |    |  | **Warning** |    | **Braking not guaranteed if the "Stop with spacebar" option is deactivated** Stopping by using the buttons on the control panel cannot be guaranteed in extreme operating modes. If the additional braking function "Stop with spacebar" is deactivated, it may no longer be possible to brake the motor via the TIA Portal. This can lead to accidents resulting in death or serious injury.  - Only deactivate the "Stop with spacebar" option in absolute exceptional cases and if it has been ensured that you are able to stop the drive safely using suitable hardware solutions. |  |     - Optional: If you do not want to use the "Stop with spacebar" option, deactivate this option in the message window.       This setting requires a safety confirmation. The message window cannot be closed without confirmation.    - Also activate the "Continue without quick stop function via spacebar and focus switch" option. 4. To close the message window, click the "OK" button.     The message window closes. The master control is then active. |  |

##### Step 2: Performing motor data identification

When you open the function view in online mode, the drive control panel that you require for the measurement is displayed automatically.

> **Note**
>
> **Manually selecting the measurement type**
>
> We only recommend to experienced users that they manually select the measurement type from the list. Numerous detail values must be defined in the configuration dialog box for the measurement types "Stationary measurement" and "Rotating measurement" (see [Parameter values](#parameter-values-for-experts)).

1. To set the drive enables, click "Set" in the "Drive enables" area.
2. Click the "1 On" icon in the "Switch on" area to switch on the motor.
3. Click the "Activate" button in the "Measurement" area to start the measurement.

   The center of the function view contains the status display that shows the progress of the measurement (parameter [r0047](SINAMICS%20Parameter%20G220.md#r0047-motor-data-identification-and-speed-controller-optimization)).

   The measurement ends independently and the message appears that the drive is in the "Switching on disabled" state.

   After the measurement, the new parameter values are displayed in the results table. You can view and check the new values.
4. Check the values that have been determined to ensure that they are plausible. If the values do not seem appropriate, perform another measurement.
5. If you do not want to perform any more measurements, click the "0 Off" icon in the motor and infeed area. Then click "Deactivate" under "Master control".

##### Step 3: Deactivate master control

Proceed as follows to return the master control:

1. Click the "Off" button to stop the drive.

   This is a basic requirement for deactivating the master control.
2. Click the "Deactivate" button under "Master control".

   The grayed-out user interface in the setting area indicates that the master control is deactivated.

##### Additional parameters

---

#### Parameter values (for experts)

##### Overview

The mandatory entries for the measurements are listed below. The results of the respective measurements are displayed in the "Stationary/rotating measurement" function view after completion of the respective measurement.

##### Parameter values for stationary measurement

Overview of the required parameter values for the stationary measurement:

- [p0352](SINAMICS%20Parameter%20G220.md#p03520n-cable-resistance) Cable resistance

  Important for long motor cables
- [p0353](SINAMICS%20Parameter%20G220.md#p03530n-motor-series-inductance) Series inductance

  Important for long motor cables
- [p0625](SINAMICS%20Parameter%20G220.md#p06250n-motor-ambient-temperature-during-commissioning) Motor ambient temperature during commissioning
- [p1909](SINAMICS%20Parameter%20G220.md#p19090n028-motor-data-identification-control-word) Motor identification control word

##### Parameter values for rotating measurement

Overview of the required parameter values for the rotating measurement:

- [p1959](SINAMICS%20Parameter%20G220.md#p19590n014-rotating-measurement-configuration) Rotating measurement configuration
- [p1961](SINAMICS%20Parameter%20G220.md#p1961-saturation-characteristic-speed-to-determine) Saturation characteristic speed for calculation
- [p1965](SINAMICS%20Parameter%20G220.md#p1965-speed_ctrl_opt-speed) Speed_ctrl_opt speed
- [p1967](SINAMICS%20Parameter%20G220.md#p19670n-speed_ctrl_opt-dynamic-factor) Speed_ctrl_opt dynamic response factor

##### Additional parameters

---

### Switching data sets during optimization

#### Overview

Various drive data sets (DDS) or control data sets (CDS) can be used for traversing the drive and for optimization. As soon as 2 or more data sets of one type have been created for a drive, a drop-down list for selecting the DDS or CDS is activated in the optimization views of the toolbar. You can use the corresponding drop-down list to select the required data set. Selection of the required data set is, however, possible only if the master control is deactivated.

#### Requirements

- At least 2 drive data sets (DDSs) or control data sets (CDSs) have been created in the drive.
- An online connection to the drive has been established.

#### Procedure

1. Open the required optimization view (e.g. control panel).

   The drop-down list for data set switchover shows the active DDS or the active CDS.

   ![Example: DDS](images/150376085131_DV_resource.Stream@PNG-de-DE.PNG)

   ![Example: DDS](images/150376085131_DV_resource.Stream@PNG-de-DE.PNG)

   Example: DDS
2. Select the required data set from the drop-down lists.
3. Click the "Activate" button under "Master control".

   The "Activate master control" message window opens.
4. Read the warning carefully and check the value for the monitoring time.

   The monitoring time specifies the time during which the connection from the PG/PC to the drive is cyclically monitored. The minimum value is 1000 ms.
5. Click the "Continue" button to confirm the monitoring time.

   The message window closes. The control panel is then active.

#### Result

The master control is active. The drop-down lists display the currently set data sets. You can perform additional settings in the optimization view.

The selection of the data sets can no longer be changed if the master control is active. Selection is blocked via the drop-down lists.

---

**See also**

[Rules for the use of data sets](Configuring%20SINAMICS%20G220%20drives.md#rules-for-the-use-of-data-sets)

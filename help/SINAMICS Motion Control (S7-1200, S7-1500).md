---
title: "SINAMICS Motion Control (S7-1200, S7-1500)"
package: TFSINAMainenUS
topics: 37
source: Siemens TIA Portal Information System (offline help, en-US)
---


# SINAMICS Motion Control (S7-1200, S7-1500)

This section contains information on the following topics:

- [Using SINAMICS Motion Control](#using-sinamics-motion-control)

## Using SINAMICS Motion Control

This section contains information on the following topics:

- [BasicPosControl (former TO_BasicPos) V2 and V2.1](#basicposcontrol-former-to_basicpos-v2-and-v21)
- [TO_BasicPos V1](#to_basicpos-v1)

### BasicPosControl (former TO_BasicPos) V2 and V2.1

This section contains information on the following topics:

- [Technology object "BasicPosControl"](#technology-object-basicposcontrol)
- [Configuring the TO Basic Positioner](#configuring-the-to-basic-positioner)
- [Diagnostics](#diagnostics)

#### Technology object "BasicPosControl"

##### Description

The corresponding instance DB is automatically created when the BasicPosControl is integrated.

Can be used in SIMATIC S7- 1500 and S7- 1200 CPUs.

##### Calling OBs

The block can be alternatively called in the following OBs:

- Cyclic task: OB1
- Cyclic interrupt OB: e.g. OB32

> **Note**
>
> - The name of TO is updated as BasicPosControl in V2.
> - You can use one BasicPosControl TO in one OB/function block.
> - You can use one version of TO in a PLC.

#### Configuring the TO Basic Positioner

This section contains information on the following topics:

- [Adding a technology object](#adding-a-technology-object)
- [Configuring drive in the configuration window](#configuring-drive-in-the-configuration-window)
- [Configuring security functions](#configuring-security-functions)
- [Calling instruction in the user program](#calling-instruction-in-the-user-program)

##### Adding a technology object

When you add a technology object, a data block is added. The configuration of the technology object is stored in this data block.

###### Requirements

A project with a CPU S7 - 1500 or CPU S7 - 1200.

###### Procedure

To add a technology object, proceed as follows:

1. Open the CPU folder in the project tree.
2. Open the "Technology objects" folder.
3. Double-click on "Add new object".  
   "Add new object" dialog box opens.
4. Click the "SINAMICS Technology" button.
5. In the "Version" column, by default the newest version gets selected.
6. Select the object "BasicPosControl".
7. Click "OK".

> **Note**
>
> You can select the "Add new and open" check box at the bottom of the dialog box. This opens the configuration of the technology object after creating the object in project tree.

###### Result

The new technology object is created and stored in the project tree in the "Technology objects" folder.

##### Configuring drive in the configuration window

This section contains information on the following topics:

- [Working with configuration window](#working-with-configuration-window)
- [Basic parameters](#basic-parameters)
- [Hardware interface](#hardware-interface)
- [Extended parameters](#extended-parameters)

###### Working with configuration window

You configure the properties of the technology object in the configuration window. To open the configuration window of the technology object, follow these steps:

1. In the project tree, open the "Technology objects" folder.
2. Open the technology object in the project tree.
3. Double-click on the "Configuration" object.

The configuration is divided into the following categories:

- Basic parameter
- Hardware interface
- Extended parameters

###### Symbols of the configuration window

Symbols in the area navigation of the configuration and inspector window shows additional information about the status of the configuration:

| Symbol | Meaning |
| --- | --- |
| ![Symbols of the configuration window](images/95593220363_DV_resource.Stream@PNG-de-DE.png) | The configuration contains default values and is complete  The configuration only contains default values. With these preset values you can use the technology object without additional changes. |
| ![Symbols of the configuration window](images/95593236235_DV_resource.Stream@PNG-de-DE.png) | The configuration contains values defined by the user or automatically adapted values and is complete  All input fields of the configuration contain valid values and at least one default value was modified. |
| ![Symbols of the configuration window](images/95593252107_DV_resource.Stream@PNG-de-DE.png) | The configuration is valid but contains unexpected values  At least one input field or a drop-down list contains an unexpected value. The corresponding field, or the drop-down list is displayed on a yellow background. When you click on it, the roll-out warning message shows you the cause of the warning. |
| ![Symbols of the configuration window](images/95582951691_DV_resource.Stream@PNG-de-DE.png) | The configuration is incomplete or incorrect  At least one input field or a drop-down list contains no or an invalid value. The corresponding field, or the drop-down list, is displayed on a red background. Click the roll-out error message to identify the cause of the error. |

###### Basic parameters

You can parameterize the basic parameters of "BasicPosControl" technology object in the basic settings.

**Name**

Define the name of the axis or the name of the positioning axis technology object in this field. The technology object lists with this name in project tree.

**Axis type**

In "Axis type" select whether to control a linear axis or a rotary axis. Default selection is "Linear axis".

You can aslo select the motor type, i.e.; standard motor or linear motor.

> **Note**
>
> When rotary axis is selected, you cannot change the motor type and by default standard motor is selected.

**Units of measure**

In the drop-down list, select the desired units of measure for position and velocity.

The "BasicPosControl" technology object supports the following units of measure for position and velocity of linear axis:

| Position | Velocity |
| --- | --- |
| nm, μm, mm, m, km | mm/s, mm/min, mm/h, m/s, m/min, m/h, km/min, km/h |
| in, ft, mi | in/s, in/min, ft/s, ft/min, mi/h |
| LU | 1000 LU/min |

The "BasicPosControl" technology object supports the following units of measure for position and velocity of rotary axis:

| Position | Velocity |
| --- | --- |
| ° | °/s, °/min |
| rad | rad/s, rad/min |
| LU | 1000 LU/min |

Default selection of units for different axis types are:

| Axis type | Position unit | Velocity unit |
| --- | --- | --- |
| Linear axis | mm | mm/s |
| Rotary axis | ° | °/s |

###### Hardware interface

This section contains information on the following topics:

- [Configuration - Drive](#configuration---drive)

###### Configuration - Drive

In the "Drive" configuration window, you can configure the drive you want to use.

By using "BasicPosControl" the encoder is connected directly to the drive interface as shown below:

![Figure](images/120748437387_DV_resource.Stream@PNG-en-US.png)

###### Drive

In the "Drive" field, select an already configured PROFINET or PROFIBUS drive.

> **Note**
>
> You can only browse the drive configured with telegram 111.

###### Extended parameters

This section contains information on the following topics:

- [Mechanics](#mechanics)

###### Mechanics

This section contains information on the following topics:

- [Mechanics](#mechanics-1)
- [Linear](#linear)
- [Rotary](#rotary)

###### Mechanics

You can configure the parameters for the position of the externally controlled drive in the "Mechanics" configuration window.

The configuration varies according to the type of mechanical system motion:

- [Linear](#linear)
- [Rotary](#rotary)

###### Linear

The configuration varies based on the type of the drive:

- Drive configured using Startdrive  
  The "Automatic data exchange for drive values (offline)" checkbox is always selected. The offline values of the drive for "Reference speed", "Number of motor revolutions", "Number of load revolutions", and "Length units per load revolution" are transferred to the technology object. The value transferred is readonly.

  > **Note**
  >
  > You can synchronize the values by either compiling the PLC program or by closing and reopening the TO editor.
- Drive configured using GSD files (generic station description)  
  The "Automatic data exchange for drive values (offline)" checkbox is always unchecked. The default values of the drive are set for "Reference speed", "Number of motor revolutions", "Number of load revolutions", and "Length units per load revolution".

  > **Note**
  >
  > The values will not synchronize, you need to manually edit the values.

The parameter numbers vary for each drive as shown in the following table:

| Parameter Name | Parameter number for the supported drives |  |
| --- | --- | --- |
| G120/S120 | V90 |  |
| Reference speed | p2000 | p2000 |
| Number of motor revolutions | p2504[0] | p29249 |
| Number of load revolutions | p2505[0] | p29248 |
| Length units per load revolutions | p2506[0] | P29247 |

###### Linear axis + standard motor

> **Note**
>
> Motor type selection is valid for BasicPosControl V2.1.

###### Drive parameters

**Drive dataset**

You can view the "Drive dataset" value of the drive. The drive parameter values used in TO are from the corresponding drive.

**Reference speed**

Displays the reference speed of the drive.

###### Load gear

Load gear is the ratio between motor revolutions and load revolutions of the measuring gearbox specified in Startdrive.

**Number of motor revolutions**
  
Displays the integer number of motor revolutions.

**Number of load revolutions**

Displays the integer number of load revolutions.

###### Position parameters

The configuration varies based on the type of units of measure selected in "[Basic Parameters](#basic-parameters)":

- Physical unit
- Length unit (LU)

**Length units per load revolutions**
  
Displays the value of neutral length unit LU per load revolution.

**Leadscrew pitch**

Enter the value to configure the distance by which the load is moved when the leadscrew makes one revolution.  
If the units of measure selected is physical unit for position and velocity, the "Leadscrew pitch" value is used to get the resolution and velocity factor to convert physical unit to LU.   
The following table describes the dependencies in units of measure for position and leadscrew pitch:

| Position | Leadscrew pitch |
| --- | --- |
| km | m/rot |
| m | mm/rot |
| mm | mm/rot |
| μm | μm/rot |
| nm | nm/rot |
| in | in/rot |
| ft | in/rot |
| mi | in/rot |
| LU | No unit Default value is set as "- - -" |

###### Scaling parameters

If the units of measure for position and velocity is LU and 1000 LU/min respectively, then the resolution and velocity factor will be set to "1 [LU]" and "1 [1000 LU/min]" respectively.  
If the units of measure for position and velocity is physical units, then the resolution and velocity factor will be calculated as shown below.

**Resolution**

Resolution [LU] = Length units per load revolution [LU/rot] / Leadscrew pitch [mm/rot]

You can view the position setpoint in length units.

Example:

If you consider; Length units per load revolution = 10000 [LU/rot]; Leadscrew pitch = 10 [mm/rot] and Units of measure for position = "m", then the calculation is as shown below

Resolution = 10000 [LU/rot]] / 10 [mm/rot]

= 1000 [LU/mm]

= 1000 * 1000 [LU/m]

Resolution = 1000000 [LU/m]

> **Note**
>
> The resolution unit is always same as the units of measure configured for position in Basic parameter.

**Velocity**

The drive can understand velocity in [1000 LU/min]. If the units of measure for velocity is different, then unit gets converted to [1000 LU/min].

Example:

If you consider; units of measure for velocity is set as "m/s" and 1m = 1000000 [LU], then the calculation is as shown below.

Velocity = 1 [m/s]

= 1000000 [LU/s]

= 60 * 1000000 [LU/min]

= 60000000 [LU/min]

= 60000 [1000 LU/min]

###### Linear axis + linear motor

> **Note**
>
> Motor type selection is valid for BasicPosControl V2.1.

###### Drive parameters

**Drive data set**

You can view the "Drive data set" value of the drive. The drive parameter values used in TO are from the corresponding drive.

**Reference velocity**

Displays the reference velocity of the drive.

###### Position parameters

The configuration varies based on the type of units of measure selected in "Basic Parameters":

- Physical unit
- Length unit (LU)

**Length units per 10mm**
  
Displays the value of neutral length unit LU per 10mm.

###### Scaling parameters

If the units of measure for position and velocity is LU and 1000 LU/min respectively, then the resolution and velocity factor will be set to "1 [LU]" and "1 [1000 LU/min]" respectively.  
If the units of measure for position and velocity is physical units, then the resolution and velocity factor will be calculated as shown below.

**Resolution**

Resolution [LU] = Length units per load revolution [LU/rot] / Leadscrew pitch [mm/rot]

You can view the position setpoint in length units.

Example:

If you consider; Length units per 10mm = 10000 [LU/10mm] and Units of measure for position = "mm", then the calculation is as shown below

Resolution = 10000 / 10

Resolution = 1000 [LU/mm]

> **Note**
>
> The resolution unit is always same as the units of measure configured for position in Basic parameter.

**Velocity**

The drive can understand velocity in [1000 LU/min]. If the units of measure for velocity is different, then unit gets converted to [1000 LU/min].

Example:

If you consider; units of measure for velocity is set as "m/s" and 1m = 1000000 [LU], then the calculation is as shown below.

Velocity = 1 [m/s]

= 1000000 [LU/s]

= 60 * 1000000 [LU/min]

= 60000000 [LU/min]

= 60000 [1000 LU/min]

###### Rotary

The configuration varies based on the type of the drive:

- Drive configured using Startdrive  
  The "Automatic data exchange for drive values (offline)" checkbox is always selected. The offline values of the drive for "Reference speed", "Number of motor revolutions", "Number of load revolutions", and "Length units per load revolution" are transferred to the technology object. The value transferred is readonly.

  > **Note**
  >
  > You can synchronize the values by either compiling the PLC program or by closing and reopening the TO editor.
- Drive configured using GSD files (generic station description)  
  The "Automatic data exchange for drive values (offline)" checkbox is always unchecked. The default values of the drive are set for "Reference speed", "Number of motor revolutions", "Number of load revolutions", and "Length units per load revolutions".

  > **Note**
  >
  > The values will not synchronize, you need to manually edit the values.

The configuration varies based on the type of the drive:

- Drive configured using Startdrive  
  The "Automatic data exchange for drive values (offline)" checkbox is always selected. The offline values of the drive for "Reference speed", "Number of motor revolutions", "Number of load revolutions", and "Length units per load revolution" are transferred to the technology object. The value transferred is readonly.

  > **Note**
  >
  > You can synchronize the values by either compiling the PLC program or by closing and reopening the TO editor.
- Drive configured using GSD files (generic station description)  
  The "Automatic data exchange for drive values (offline)" checkbox is always unchecked. The default values of the drive are set for "Reference speed", "Number of motor revolutions", "Number of load revolutions", and "Length units per load revolution".

  > **Note**
  >
  > The values will not synchronize, you need to manually edit the values.

The parameter numbers vary for each drive as shown in the following table:

| Parameter Name | Parameter number for the supported drives |  |
| --- | --- | --- |
| G120/S120 | V90 |  |
| Reference speed | p2000 | p2000 |
| Number of motor revolutions | p2504[0] | p29249 |
| Number of load revolutions | p2505[0] | p29248 |
| Length units per load revolutions | p2506[0] | P29247 |

###### Drive parameters

**Drive dataset**

You can view the "Drive dataset" value of the drive. The drive parameter values used in TO are from the corresponding drive.

**Reference speed**

Displays the reference speed of the drive.

###### Load gear

Load gear is the ratio between motor revolutions and load revolutions of the measuring gearbox specified in Startdrive.

**Number of motor revolutions** 
  
Displays the integer number of motor revolutions.

**Number of load revolutions**

Displays the integer number of load revolutions.

###### Position parameters

**Length units per load revolutions** 
  
Displays the value of neutral length unit LU per load revolution.

**Relation to**

Displays default value of 360°/rot.

###### Scaling parameters

The units of measure for resolution and velocity depends on the units set in Basic parameter.

**Resolution**

Resolution [LU]= Length units per load revolution [LU/rot] / Relation to [°/rot]

You can view the position setpoint in length units.

Example:

If you consider; "Length units per load revolution" = 36000 [LU/rot] and "Relation to" = 360 [°/rot], then the calculation is as shown below

Resolution = 36000 [LU/rot]] / 360 [°/rot]

Resolution = 100 [LU/°]

> **Note**
>
> The resolution unit is always same as the units of measure configured for position in Basic parameter.

**Velocity**

The drive can understand velocity in [1000 LU/min]. If the units of measure for velocity is different, then unit gets converted to [1000 LU/min].

Example:

If you consider; units of measure for velocity is set as "°/s" and 1° = 100 [LU], then the calculation is as shown below.

Velocity = 1 [°/s]

= 100 [LU/s]

= 60 * 100 [LU/min]

= 6000 [LU/min]

Velocity = 6 [1000 LU/min]

##### Configuring security functions

###### Access to security functions

You can access security functions after activating **Project protection** and a user has successfully logged on. The logged on user must have the required engineering and runtime rights.

You will find basic information of STEP 7 user management in the "Using user management" section of the information system.

###### Engineering rights for BasicPosControl

You have option to set the following engineering rights for a user-defined role:

| Engineering rights | Description |
| --- | --- |
| **Monitor PLC program** | In online and offline mode you can monitor the PLC program. All the parameters in the TO are read only.  If you enable the **Monitor PLC program** engineering rights, then by default **Open the project read-only** function right also gets enabled. The **Open the project read-only** engineering right is required to open the project. |
| **Edit online PLC program** | In online mode you can edit the PLC program. You should also select **Monitor PLC program** function right to monitor the program online.  If you enable the **Monitor PLC program** function rights, then by default **Open the project read-only** and **Open and edit the project** function rights also gets enabled. The **Open the project read-only** and **Open and edit the project** function rights are required to open the project. |
| **Edit PLC program** | In offline mode you can edit the PLC program. You should also select **Monitor PLC program** function right to monitor the program online.  If you enable the **Edit PLC program** function rights, then by default **Open the project read-only** and **Open and edit the project** function rights also gets enabled. The **Open the project read-only** and **Open and edit the project** function rights are required to open the project. |

> **Note**
>
> You need to have **Download to PLC** function rights to download the modified program to PLC.

###### Banner on the software interface

In technology object **Configuration** editor and Organization block (OB) editor, you get additional information in a banner at the top of the editor. In the banner you get information on the function rights necessary for the user logged in to perform read/write. To hide the banner, click on the vertical blue bar at the left edge of the banner or on the X in the upper right corner. To expand a collapsed banner, click on the information symbol at the top left of the editor.

For example, If user with **Monitor PLC program** function rights login to the project, below banner appears:

![Banner on the software interface](images/140442749835_DV_resource.Stream@PNG-en-US.png)

By clicking on the link in banner text, you are navigated to **Users and roles** editor.

##### Calling instruction in the user program

###### Procedure

To call the technology object instruction in the user program, proceed as follows:

1. Open the CPU folder in the project tree.
2. Open the "Program blocks" folder.
3. Double-click on the OB for cyclic program execution.  
   The block opens in the working area.
4. In the "Instruction" window open the group "Technology" and the folder "SINAMICS Motion Control".  
   The folder contains the technology object.
5. Select the technology object basic positioner and drag it to your OB.  
   The "Call option" dialog opens.
6. From the "Name" list select the previously created instance DB.
7. Click "OK" to add the instruction along with instance DB.  
   Or  
   Click "Cancel" to add only the instruction and configure the previously created data base to the instruction.

> **Note**
>
> The technology object can also be added in "Function block" and "Function" code blocks.

#### Diagnostics

This section contains information on the following topics:

- [Diagnostic](#diagnostic)
- [Basic positioning](#basic-positioning)
- [Binary signals](#binary-signals)
- [SinaPos status](#sinapos-status)

##### Diagnostic

After configuration of the technology object is complete, you can monitor the devices configured in the technology object using the diagnostics function.

###### Requirements

- There is an online connection between STEP 7 (TIA Portal) and the S7 controller.
- The SINAMICS technology object is called in the user program.
- A technology object was created and loaded on the S7 controller.
- The S7 controller is in "RUN" mode.

###### Procedure

To open the display editor for the diagnostics function, follow these steps:

1. In the project tree, open the "Technological objects" folder.
2. Open the relevant technology object in the project tree.
3. Double-click on the "Diagnostics".

##### Basic positioning

You can use the "Basic positioning" diagnostic function to monitor the most important status and error messages for the axis in TIA Portal.

The following values are read by the technology object and displayed.

| Displayed values | Description |
| --- | --- |
| ModePos | Shows the operating mode set.  Operating mode:               1 = relative positioning              2 = absolute positioning              3 = positioning as setup              4 = homing procedure              5 = set home position              6 = traversing block 0 – 15/63 (G120/S120)              7 = jog              8 = jog incremental |
| ActFault | Shows current fault number. |
| Status | Shows the status of the block and possible error description. |
| ExecuteMode | The technology object block is enabled and activates traversing job/setpoint acceptance/activate reference function. |
| Name of Drive | Shows the name of the drive configured. |
| ActVelocity | Shows the measured velocity in LU/min or the physical unit as configured in **Units of measure** field in **Basic parameter** window. |
| ActPosition | Shows the measured position in LU or the physical unit as configured in **Units of measure** field in **Basic parameter** window. |

##### Binary signals

The following table shows the status of the drive inputs and outputs.

| Parameter | Declaration | Description |
| --- | --- | --- |
| EnableAxis | INPUT | The axis is enabled and ready to be controlled via Motion Control commands. |
| CancelTraversing | INPUT | The traversing job is rejected. Default value is 1 = do not reject. |
| IntermediateStop | INPUT | The traversing command is interrupted. Default value is 1 = no intermediate stop. |
| Positive | INPUT | Axis moves in positive direction |
| Negative | INPUT | Axis moves in negative direction |
| ExecuteMode | INPUT | The technology object is enabled. |
| Jog2 | INPUT | The axis is being moved with a command for jog2 mode of Motion Control instruction |
| FlyRef | INPUT | The flying homing function is selected during operation. |
| AckError | INPUT | Acknowledge faults |
| Error | OUTPUT | An error occurred at the technology object. |
| AxisEnabled | OUTPUT | Drive is ready and switched on. |
| AxisError | OUTPUT | Fault in drive. |
| AxisWarn | OUTPUT | Alarm of the drive effective. |
| AxisPosOk | OUTPUT | Target position of the axis reached. |
| Lockout | OUTPUT | Switching on the drive is inhibited. |

##### SinaPos status

The following table shows the status of the configuration input "ConfigEPos"

![Figure](images/136065413771_DV_resource.Stream@PNG-en-US.png)

The following table shows the bit funtions:

| Parameter | Declaration | Description |
| --- | --- | --- |
| ConfigEPos | INPUT | With this interface, the following bit functions of telegram 111 can be transmitted:  Bit0 = STW1.1 (OFF2: 1 = no pulse inhibit)  Bit1 = STW1.2 (OFF3: 1 = no pulse inhibit)  Bit2 = EPosSTW2.14 (Software limit switch: 1 = active)  Bit3 = EPosSTW2.15 (Stop output cam: 1 = active)  Bit4 = EPosSTW2.11 (reserved)  Bit5 = EPosSTW2.10 (reserved)  Bit6 = EPosSTW2.2 (signal source reference mark)  Bit7 = STW1.13 (External block change)  Bit8 = EPosSTW1.12 (continuous setpoint transfer MDI: 1 = active)  Bit9 = STW2.0 (reserved)  Bit10 = STW2.1 (reserved)  Bit11 = STW2.2 (reserved)  Bit12 = STW2.3 (reserved)  Bit13 = STW2.4 (reserved)  Bit14 = STW2.7 (reserved)  Bit15 = STW1.12 (reserved)  Bit16 = STW1.14 (reserved)  Bit17 = STW1.15 (reserved)  Bit18 = EPosSTW1.6 (reserved)  Bit19 = EPosSTW1.7 (reserved)  Bit20 = EPosSTW1.11 (reserved)  Bit21 = EPosSTW1.13 (reserved)  Bit22 = EPosSTW2.3 (reserved)  Bit23 = EPosSTW2.4 (reserved)  Bit24 = EPosSTW2.6 (reserved)  Bit25 = EPosSTW2.7 (reserved)  Bit26 = EPosSTW2.12 (reserved)  Bit27 = EPosSTW2.13 (reserved)  Bit28 = STW2.5 (reserved)  Bit29 = STW2.6 (reserved)  Bit30 = STW2.8 (travel to fixed endstop: 1 = active)  Bit31 = STW2.9 (reserved) |

### TO_BasicPos  V1

This section contains information on the following topics:

- [Technology object "TO_BasicPos"](#technology-object-to_basicpos)
- [Configuring the TO Basic Positioner](#configuring-the-to-basic-positioner-1)
- [Diagnostics](#diagnostics-1)

#### Technology object "TO_BasicPos"

##### Description

The corresponding instance DB is automatically created when the TO_BasicPos is integrated.

Can be used in SIMATIC S7- 1500 and S7- 1200 CPUs.

##### Calling OBs

The block can be alternatively called in the following OBs:

- Cyclic task: OB1
- Cyclic interrupt OB: e.g. OB32

#### Configuring the TO Basic Positioner

This section contains information on the following topics:

- [Adding a technology object](#adding-a-technology-object-1)
- [Configuring drive in the configuration window](#configuring-drive-in-the-configuration-window-1)
- [Calling instruction in the user program](#calling-instruction-in-the-user-program-1)

##### Adding a technology object

When you add a technology object, a data block is added. The configuration of the technology object is stored in this data block.

###### Requirements

A project with a CPU S7 - 1500 or CPU S7 - 1200.

###### Procedure

To add a technology object, proceed as follows:

1. Open the CPU folder in the project tree.
2. Open the "Technology objects" folder.
3. Double-click on "Add new object".  
   "Add new object" dialog box opens.
4. Click the "SINAMICS Technology" button.
5. In the "Version" column, by default the newest version gets selected.
6. Select the object "TO_BasicPos".
7. Click "OK".

> **Note**
>
> You can select the "Add new and open" check box at the bottom of the dialog box. This opens the configuration of the technology object after creating the object in project tree.

###### Result

The new technology object is created and stored in the project tree in the "Technology objects" folder.

##### Configuring drive in the configuration window

This section contains information on the following topics:

- [Working with configuration window](#working-with-configuration-window-1)
- [Hardware interface](#hardware-interface-1)

###### Working with configuration window

You configure the properties of the technology object in the configuration window. To open the configuration window of the technology object, follow these steps:

1. In the project tree, open the "Technology objects" folder.
2. Open the technology object in the project tree.
3. Double-click on the "Configuration" object.

You can configure "Hardware interface" in configuration window.

###### Symbols of the configuration window

Symbols in the area navigation of the configuration and inspector window shows additional information about the status of the configuration:

| Symbol | Meaning |
| --- | --- |
| ![Symbols of the configuration window](images/95593220363_DV_resource.Stream@PNG-de-DE.png) | The configuration contains default values and is complete  The configuration only contains default values. With these preset values you can use the technology object without additional changes. |
| ![Symbols of the configuration window](images/95593236235_DV_resource.Stream@PNG-de-DE.png) | The configuration contains values defined by the user or automatically adapted values and is complete  All input fields of the configuration contain valid values and at least one default value was modified. |
| ![Symbols of the configuration window](images/95593252107_DV_resource.Stream@PNG-de-DE.png) | The configuration is valid but contains unexpected values  At least one input field or a drop-down list contains an unexpected value. The corresponding field, or the drop-down list is displayed on a yellow background. When you click on it, the roll-out warning message shows you the cause of the warning. |
| ![Symbols of the configuration window](images/95582951691_DV_resource.Stream@PNG-de-DE.png) | The configuration is incomplete or incorrect  At least one input field or a drop-down list contains no or an invalid value. The corresponding field, or the drop-down list, is displayed on a red background. Click the roll-out error message to identify the cause of the error. |

###### Hardware interface

This section contains information on the following topics:

- [Configuration - Drive](#configuration---drive-1)

###### Configuration - Drive

In the "Drive" configuration window, you can configure the drive you want to use.

By using the TO_BasicPos the encoder is connected directly to the drive interface as shown below:

![Figure](images/120748437387_DV_resource.Stream@PNG-en-US.png)

###### Drive

In the "Drive" field, select an already configured PROFINET.

> **Note**
>
> You can only browse the drive configured with telegram 111.

##### Calling instruction in the user program

###### Procedure

To call the technology object instruction in the user program, proceed as follows:

1. Open the CPU folder in the project tree.
2. Open the "Program blocks" folder.
3. Double-click on the OB for cyclic program execution.  
   The block opens in the working area.
4. In the "Instruction" window, open the group "Technology" and the folder "SINAMICS Motion Control".  
   The folder contains the technology object.
5. Select the technology object basic positioner and drag it to your OB.  
   The "Call option" dialog opens.
6. From the "Name" list select the previously created instance DB.
7. Click "OK" to add the instruction along with instance DB.  
   Or  
   Click "Cancel" to add only the instruction and configure the previously created data base to the instruction.

> **Note**
>
> The technology object can also be added in "Function block" and "Function" code blocks.

#### Diagnostics

This section contains information on the following topics:

- [Diagnostic](#diagnostic-1)
- [Basic positioning](#basic-positioning-1)
- [Binary signals](#binary-signals-1)
- [SinaPos status](#sinapos-status-1)

##### Diagnostic

After configuration of the technology object is complete, you can monitor the devices configured in the technology object using the diagnostics function.

###### Requirements

- There is an online connection between STEP 7 (TIA Portal) and the S7 controller.
- The SINAMICS technology object is called in the user program.
- A technology object was created and loaded on the S7 controller.
- The S7 controller is in "RUN" mode.

###### Procedure

To open the display editor for the diagnostics function, follow these steps:

1. In the project tree, open the "Technological objects" folder.
2. Open the relevant technology object in the project tree.
3. Double-click on the "Diagnostics".

##### Basic positioning

You can use the "Basic positioning" diagnostic function to monitor the most important status and error messages for the axis in TIA Portal.

The following values are read by the technology object and displayed.

| Displayed values | Description |
| --- | --- |
| ModePos | Shows the operating mode set.  Operating mode:               1 = relative positioning              2 = absolute positioning              3 = positioning as setup              4 = homing procedure              5 = set home position              6 = traversing block 0 – 15/63 (G120/S120)              7 = jog              8 = jog incremental |
| ActFault | Shows current fault number. |
| Status | Shows the status of the block and possible error description. |
| ExecuteMode | The technology object block is enabled and activates traversing job/setpoint acceptance/activate reference function. |
| Name of Drive | Shows the name of the drive configured. |
| ActVelocity | Shows the measured velocity in LU/min or the physical unit as configured in **Units of measure** field in **Basic parameter** window. |
| ActPosition | Shows the measured position in LU or the physical unit as configured in **Units of measure** field in **Basic parameter** window. |

##### Binary signals

The following table shows the status of the drive inputs and outputs.

| Parameter | Declaration | Description |
| --- | --- | --- |
| EnableAxis | INPUT | The axis is enabled and ready to be controlled via Motion Control commands. |
| CancelTraversing | INPUT | The traversing job is rejected. Default value is 1 = do not reject. |
| IntermediateStop | INPUT | The traversing command is interrupted. Default value is 1 = no intermediate stop. |
| Positive | INPUT | Axis moves in positive direction |
| Negative | INPUT | Axis moves in negative direction |
| ExecuteMode | INPUT | The technology object is enabled. |
| Jog2 | INPUT | The axis is being moved with a command for jog2 mode of Motion Control instruction |
| FlyRef | INPUT | The flying homing function is selected during operation. |
| AckError | INPUT | Acknowledge faults |
| Error | OUTPUT | An error occurred at the technology object. |
| AxisEnabled | OUTPUT | Drive is ready and switched on. |
| AxisError | OUTPUT | Fault in drive. |
| AxisWarn | OUTPUT | Alarm of the drive effective. |
| AxisPosOk | OUTPUT | Target position of the axis reached. |
| Lockout | OUTPUT | Switching on the drive is inhibited. |

##### SinaPos status

The following table shows the status of the configuration input "ConfigEPos"

![Figure](images/136065413771_DV_resource.Stream@PNG-en-US.png)

The following table shows the bit funtions:

| Parameter | Declaration | Description |
| --- | --- | --- |
| ConfigEPos | INPUT | With this interface, the following bit functions of telegram 111 can be transmitted:  Bit0 = STW1.1 (OFF2: 1 = no pulse inhibit)  Bit1 = STW1.2 (OFF3: 1 = no pulse inhibit)  Bit2 = EPosSTW2.14 (Software limit switch: 1 = active)  Bit3 = EPosSTW2.15 (Stop output cam: 1 = active)  Bit4 = EPosSTW2.11 (reserved)  Bit5 = EPosSTW2.10 (reserved)  Bit6 = EPosSTW2.2 (signal source reference mark)  Bit7 = STW1.13 (External block change)  Bit8 = EPosSTW1.12 (continuous setpoint transfer MDI: 1 = active)  Bit9 = STW2.0 (reserved)  Bit10 = STW2.1 (reserved)  Bit11 = STW2.2 (reserved)  Bit12 = STW2.3 (reserved)  Bit13 = STW2.4 (reserved)  Bit14 = STW2.7 (reserved)  Bit15 = STW1.12 (reserved)  Bit16 = STW1.14 (reserved)  Bit17 = STW1.15 (reserved)  Bit18 = EPosSTW1.6 (reserved)  Bit19 = EPosSTW1.7 (reserved)  Bit20 = EPosSTW1.11 (reserved)  Bit21 = EPosSTW1.13 (reserved)  Bit22 = EPosSTW2.3 (reserved)  Bit23 = EPosSTW2.4 (reserved)  Bit24 = EPosSTW2.6 (reserved)  Bit25 = EPosSTW2.7 (reserved)  Bit26 = EPosSTW2.12 (reserved)  Bit27 = EPosSTW2.13 (reserved)  Bit28 = STW2.5 (reserved)  Bit29 = STW2.6 (reserved)  Bit30 = STW2.8 (travel to fixed endstop: 1 = active)  Bit31 = STW2.9 (reserved) |

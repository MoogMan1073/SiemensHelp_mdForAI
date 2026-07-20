---
title: "Using Easy Motion Control (S7-300, S7-400)"
package: TFTOEMCenUS
topics: 115
devices: [S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Using Easy Motion Control (S7-300, S7-400)

This section contains information on the following topics:

- [Positioning with Easy Motion Control (S7-300, S7-400)](#positioning-with-easy-motion-control-s7-300-s7-400)
- [Functions with Easy Motion Control (S7-300, S7-400)](#functions-with-easy-motion-control-s7-300-s7-400)
- [Configuring Easy Motion Control (S7-300, S7-400)](#configuring-easy-motion-control-s7-300-s7-400)
- [Download to CPU (S7-300, S7-400)](#download-to-cpu-s7-300-s7-400)
- [Programming Easy Motion Control (S7-300, S7-400)](#programming-easy-motion-control-s7-300-s7-400)
- [Commissioning Easy Motion Control (S7-300, S7-400)](#commissioning-easy-motion-control-s7-300-s7-400)
- [Diagnostics (S7-300, S7-400)](#diagnostics-s7-300-s7-400)

## Positioning with Easy Motion Control (S7-300, S7-400)

This section contains information on the following topics:

- [Product overview (S7-300, S7-400)](#product-overview-s7-300-s7-400)
- [Components for Positioning (S7-300, S7-400)](#components-for-positioning-s7-300-s7-400)
- [Supported hardware configurations (S7-300, S7-400)](#supported-hardware-configurations-s7-300-s7-400)
- [Principles of Positioning with Easy Motion Control (S7-300, S7-400)](#principles-of-positioning-with-easy-motion-control-s7-300-s7-400)
- [Concept Definitions (S7-300, S7-400)](#concept-definitions-s7-300-s7-400)
- [Linear axis (S7-300, S7-400)](#linear-axis-s7-300-s7-400)
- [Rotary axis (S7-300, S7-400)](#rotary-axis-s7-300-s7-400)

### Product overview (S7-300, S7-400)

#### Overview

Easy Motion Control allows you to control the positioning of drives. The movement is controlled solely by software (instructions) in the CPU. **No special hardware** is required for connection to the drives, although corresponding I/O must of course be available in order to record actual positions and output speed setpoint values.

The instructions of Easy Motion Control were created based on the "Technical Specification Function blocks for motion control V1.0" of **PLCopen**.

You assign parameters using configuration software that also supports commissioning using test functions. All parameters of an axis are stored in a single data block, namely the axis DB.

You can connect the drives to central I/O, or to distributed I/O via a DP master / IO controller that is integrated in the CPU.

You execute the movement by interconnecting the corresponding instructions and running them in the user program.

### Components for Positioning (S7-300, S7-400)

The following figure shows a configuration model with Easy Motion Control.

![Figure](images/29414502795_DV_resource.Stream@PNG-en-US.png)

#### Safety device

When the safety device is actuated, the emergency STOP button disconnects the power supply.

#### Power unit

The power unit controls the motor. The safety limit switches disconnect the power unit.

#### Motor

The motor is controlled by the power unit and drives the axis.

#### Encoder

The encoder provides information on distance and direction.

#### Easy Motion Control

Easy Motion Control provides the following functions:

- Jogging
- Reference point approach
- Absolute/relative positioning
- Electronic gear
- Set reference point
- All common monitoring functions for positioning
- Velocity override
- Closed-loop position control
- Simulation
- Preconfigured input drivers for recording encoder values, or output drivers for analog output modules

#### Modules for position detection and setpoint output

These modules form the interface between the CPU and the machine. They read axis positions and output setpoint values to the power unit.

#### CPU

The CPU executes the user program that contains the embedded instructions of Easy Motion Control.

#### PC/PG

A PC/PG is used for the following functions:

- Parameter assignment: You assign parameters to Easy Motion Control using the configuration software, or directly in the axis DB (see [Configuring the axis TO](#configuring-the-axis-to-s7-300-s7-400)).
- Programming: You integrate the Easy Motion Control instructions directly in your program.

### Supported hardware configurations (S7-300, S7-400)

The following hardware configurations are conveniently supported by driver instructions. These are supplied with Easy Motion Control.

You can adapt configurations that are not directly supported using the open driver blocks that are also provided in your package.

The following figure shows **distributed** configurations for Easy Motion Control.

![Figure](images/32832443147_DV_resource.Stream@PNG-en-US.png)

The following figure shows **centralized** configurations for Easy Motion Control.

![Figure](images/29414547339_DV_resource.Stream@PNG-en-US.png)

### Principles of Positioning with Easy Motion Control (S7-300, S7-400)

#### Setting up closed loop position control

With controlled positioning, the current position of the axis is compared with the setpoint position. Any deviations are compensated using the position controller both during a travel movement as well as at a standstill.

The following figure shows the schematic representation of controlled positioning with Easy Motion Control. A [travel instruction](#user-program-setup-s7-300-s7-400) specifies the position setpoints. The [input driver](Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#input-driver-s7-300-s7-400) records the actual value of the axis position. The [position controller](#controller-s7-300-s7-400) compares the actual position value with the position setpoint and generates a velocity setpoint value from the difference. The [output driver](Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#output-driver-s7-300-s7-400) outputs the scaled velocity setpoint.

![Setting up closed loop position control](images/29522344715_DV_resource.Stream@PNG-en-US.png)

The following figure shows the relationship between the axis velocity and the distance covered during a traversing movement.

![Setting up closed loop position control](images/29522386187_DV_resource.Stream@PNG-en-US.png)

### Concept Definitions (S7-300, S7-400)

#### Target

The target is the absolute or relative position of the axis that is approached during positioning.

#### Traversing movement

Traversing movements are triggered by calling instructions, which are also referred to as travel instructions in the following.

#### Residual distance

Residual distance is the difference between target position and current position setpoint.

#### Following distance / following error

During a travel movement, a difference builds up between the current position setpoint and the actual position value due to axial inertia. This is called the following error. If the following distance exceeds an assignable value, a following error occurs.

#### Monitoring ranges

- Work range:

  Defines the permitted traversing range of your axis, which you determine for your task using the [software limit switches](#linear-axis-s7-300-s7-400), or the end of the [rotary axis](#rotary-axis-s7-300-s7-400).
- Standstill range:

  Defines a configurable range that the axis must not leave when at a standstill. The standstill range lies to the left and right of the target.
- Target range:

  If the setpoint has reached the target at the end of a motion, the approach of the axis into the target range is monitored. The target range is used to monitor the positioning accuracy of your application and lies to the left and right of the target.

  Standstill range monitoring begins as soon as the axis reaches the target range. For this reason, the standstill range should be greater than the target range.

The following figure shows the position of the ranges in the target area.

![Monitoring ranges](images/29522162443_DV_resource.Stream@PNG-en-US.png)

### Linear axis (S7-300, S7-400)

#### Description

The **working range** extends from the start of the software limit switch to the end of the software limit switch and is limited to 1 × 2<sup>24</sup> length units (Cartesian coordinates between -2<sup>24</sup>+6 and +2<sup>24</sup>-6).

The **physical axis length** is limited by the mechanical stops of your axis.

The **numerical range** of Easy Motion Control is only relevant if work range monitoring is switched off. It is limited to 2 × 2<sup>24</sup>-12 length units (from -2<sup>24</sup>+6 to +2<sup>24</sup>-6).

The **encoder range** is:

- The range covered by an absolute encoder
- The distance from -2<sup>31</sup> to +2<sup>31</sup> steps covered by an incremental encoder

With linear axes, the **work range** (= travel range) is limited as follows:

Working range &lt; physical axis length &lt; numerical range of Easy Motion Control &lt; encoder range

The following figure shows the various ranges of a linear axis.

![Description](images/68931087243_DV_resource.Stream@PNG-en-US.png)

### Rotary axis (S7-300, S7-400)

#### Description

The **working range** extends from the start of the rotary axis to the end of the rotary axis and is limited to 1 × 2<sup>24</sup> length units (Cartesian coordinates between -2<sup>24</sup>+6 and +2<sup>24</sup>-6).

The **encoder range** is:

- Arbitrary for an incremental encoder
- Determined for an absolute encoder based on the rule:

  Encoder range = working range × n

  where:

  - n = 1 with single-turn encoders
  - n &gt; 1 and integer with multi-turn encoders

The actual value of a rotary axis is reset to the start of the rotary axis after every revolution. Rotary axes therefore have an infinite traversing range that extends beyond the start or end of the rotary axis. The axis position is always displayed as a value between the start and end of the rotary axis.

![Description](images/29532511243_DV_resource.Stream@PNG-en-US.png)

## Functions with Easy Motion Control (S7-300, S7-400)

This section contains information on the following topics:

- [Overview (S7-300, S7-400)](#overview-s7-300-s7-400)
- [Jogging (S7-300, S7-400)](#jogging-s7-300-s7-400)
- [Synchronization (S7-300, S7-400)](#synchronization-s7-300-s7-400)
- [Absolute or Relative Positioning (S7-300, S7-400)](#absolute-or-relative-positioning-s7-300-s7-400)
- [Gear (S7-300, S7-400)](#gear-s7-300-s7-400)
- [Stopping Travel (S7-300, S7-400)](#stopping-travel-s7-300-s7-400)
- [Overriding Travel (S7-300, S7-400)](#overriding-travel-s7-300-s7-400)
- [Tracking (S7-300, S7-400)](#tracking-s7-300-s7-400)
- [Velocity override (S7-300, S7-400)](#velocity-override-s7-300-s7-400)
- [Simulation (S7-300, S7-400)](#simulation-s7-300-s7-400)
- [Error Responses and Diagnosis (S7-300, S7-400)](#error-responses-and-diagnosis-s7-300-s7-400)

### Overview (S7-300, S7-400)

Easy Motion Control is used to position an axis on a target with programmable acceleration, velocity, and deceleration or move it at constant velocity. The necessary traversing movements are triggered by calling travel instructions.

At the start of a traversing job, the target or distance of the traversing movement and possibly the required acceleration, velocity, or deceleration, are configured at the travel instruction. The system of units (length unit) can be selected freely for these values (for example, mm).

### Jogging (S7-300, S7-400)

The jogging function allows you to move the drive in the positive or negative direction. No target is specified.

The jogging function is realized using the [MC_MoveJog](Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#mc_movejog-s7-300-s7-400) instruction.

### Synchronization (S7-300, S7-400)

In order to assign a reproducible encoder value to the real position, a reference (synchronization) must be established between the axis position and the encoder value.

The synchronization function is realized using the [MC_Home](Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#mc_home-s7-300-s7-400) instruction.

#### Synchronization with an Incremental Encoder

An incremental encoder does not give any information about the immediate position of the axis when the system is switched on. Instead, it starts counting at the current position of the axis.

Synchronization is always necessary when the system is switched on again after occurrence of errors or after replacing the encoder.

An incremental encoder can be synchronized by:

- Reference point approach
- Set reference point

#### Synchronization with absolute encoder

When commissioning absolute encoders, you must synchronize the value indicated by the encoder with the actual axis position.

Resynchronization is not necessary when the system is switched back on or after errors have occurred. After the encoder has been replaced, however, resynchronization is necessary.

An absolute encoder can only be synchronized by means of reference point setting (also called absolute encoder adjustment).

#### Reference point approach

The axis is moved in the direction of the reference point. The axis is synchronized after it has passed the reference point, i.e. a position value is assigned to the numerical value of the incremental encoder. A new coordinate value can be assigned to the reference point with every reference point approach.

A reference point approach is only possible with incremental encoders.

#### Set reference point

With reference setting, a new coordinate value is assigned to the current position.

Reference point setting is supported for incremental and absolute encoders.

### Absolute or Relative Positioning (S7-300, S7-400)

Easy Motion Control can move the axis

- To **absolute** targets
- By a given distance in a specific direction with **relative** positioning

The absolute and relative positioning functions are realized using [MC_MoveAbsolute](Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#mc_moveabsolute-s7-300-s7-400) and [MC_MoveRelative](Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#mc_moverelative-s7-300-s7-400) instructions.

### Gear (S7-300, S7-400)

Easy Motion Control realizes an electronic gear between two axes using the [MC_GearIn](Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#mc_gearin-s7-300-s7-400) instruction.

### Stopping Travel (S7-300, S7-400)

You can stop current travel at any time.

The Stop function is realized using the [MC_StopMotion](Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#mc_stopmotion-s7-300-s7-400) instruction.

### Overriding Travel (S7-300, S7-400)

A currently active travel instruction can always

- Be overridden by starting a different travel instruction
- Be canceled by calling instruction MC_StopMotion (see [Sequence of traversing movements](#sequence-of-travel-movements-s7-300-s7-400)).

### Tracking (S7-300, S7-400)

With tracking, the position setpoint is continuously adjusted (tracked) in the position controller to the actual position value. During tracking, the axis is not monitored for leaving the standstill range.

This function is activated by clearing the "EnableDrive" signal at instruction [MC_Control](Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#mc_control-s7-300-s7-400), or after an error has occurred.

### Velocity override (S7-300, S7-400)

Velocity override enables dynamic changes to the velocity that is configured in a travel instruction. Acceleration and deceleration values are not affected.

For more information on velocity override, refer to [Specifying velocity override](#specifying-velocity-override-s7-300-s7-400).

### Simulation (S7-300, S7-400)

In simulation mode, you can test your travel program without moving your axis.

Simulation is realized using the [MC_Simulation](Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#mc_simulation-s7-300-s7-400) instruction.

### Error Responses and Diagnosis (S7-300, S7-400)

All errors detected by the instructions are displayed in the axis DB by

- Setting a group error and
- Error-specific display

With errors requiring acknowledgment, an error acknowledgment must be set after rectifying the error.

If a travel instruction (for example, MC_MoveJog, or MC_MoveAbsolute) has caused or detected the error, the "Error" output is set at the corresponding block.

However, if the error was detected by a driver block, the exact cause of the error is indicated in the static data of the block (see [Input drivers](Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#input-driver-s7-300-s7-400)).

For detailed information on error response, error display, and error acknowledgment, see [Error Displays and Error Acknowledgment in the axis DB](#error-displays-and-error-acknowledgement-in-the-axis-db-s7-300-s7-400).

## Configuring Easy Motion Control (S7-300, S7-400)

This section contains information on the following topics:

- [Guideline for using Easy Motion Control (S7-300, S7-400)](#guideline-for-using-easy-motion-control-s7-300-s7-400)
- [Adding an axis technology object (S7-300, S7-400)](#adding-an-axis-technology-object-s7-300-s7-400)
- [Configuring the axis TO (S7-300, S7-400)](#configuring-the-axis-to-s7-300-s7-400)

### Guideline for using Easy Motion Control (S7-300, S7-400)

This guideline shows you the basic procedures for using Easy Motion Control in combination with an S7-300/400 CPU.

#### Requirement

To use the "Axis" technology object (TO), you need to create a project with a CPU.

#### Procedure

Proceed based on the sequence recommended below to use Easy Motion Control with the S7‑300/400 CPU. Use the following links for this purpose:

1. [Adding an axis technology object](#adding-an-axis-technology-object-s7-300-s7-400)
2. [Working with the configuration dialog](#working-with-the-configuration-dialog-s7-300-s7-400)
3. [Download to CPU](#download-to-cpu-s7-300-s7-400)
4. Function test of the axis in the commissioning window
5. [Programming Easy Motion Control](#programming-easy-motion-control-s7-300-s7-400)
6. Diagnostics of the axis control

### Adding an axis technology object (S7-300, S7-400)

#### Inserting an axis TO in the project navigator

When you add a technology object, an instance DB of this TO will be generated. The axis configuration is stored in this instance DB.

#### Requirement

A project with a CPU has been created.

#### Procedure

Proceed as follows to insert an axis TO in the project navigator:

1. Open the CPU folder in the project tree.
2. Open the "Technology objects" folder.
3. Double-click "Add new object".

   The "Add new object" dialog opens.
4. Select the "Motion" technology.
5. Open the "Motion Control" folder.
6. Open the "Easy Motion Control" folder.
7. Select the instruction for the technology object: in this case, AXIS_REF.
8. Type in an individual name for the axis in the "Name" text box.
9. Select the "Manual" option if you want to change the proposed data block number of the instance DB.
10. Click "More information" if you want to supplement user information on the TO.
11. Click "OK" to add the TO.

    Click "Cancel" if you want to discard your entries.

#### Result

The new technology object has been created and stored in the project tree in the "Technology objects" folder. The technology object is used if the instructions for this TO are called in a cyclic interrupt or synchronous cycle interrupt OB.

For more information, refer to "[User Program Setup](#user-program-setup-s7-300-s7-400)".

> **Note**
>
> You can select the "Add new and open" check box at the bottom of the dialog box. This opens the configuration of the technology object after adding has been completed.

### Configuring the axis TO (S7-300, S7-400)

This section contains information on the following topics:

- [Working with the configuration dialog (S7-300, S7-400)](#working-with-the-configuration-dialog-s7-300-s7-400)
- [Basic parameters (S7-300, S7-400)](#basic-parameters-s7-300-s7-400)
- [Advanced parameters (S7-300, S7-400)](#advanced-parameters-s7-300-s7-400)

#### Working with the configuration dialog (S7-300, S7-400)

You configure the properties of the technology object in the configuration window. To open the configuration window of the technology object, follow these steps:

1. Open the group of the selected technology object in the project tree.
2. Double-click the "Configuration" object.

The configuration is divided into the following categories:

- **Basic parameters**

  The basic parameters contain all the parameters which must be configured for a functioning axis.
- **Advanced parameters**

  The advanced parameters include parameters for adapting to your drive or plant.

##### Icons of the configuration window

Icons in the area navigation of the configuration show additional details about the status of the configuration:

| Symbol | Meaning |
| --- | --- |
| ![Icons of the configuration window](images/29885995659_DV_resource.Stream@PNG-de-DE.png) | **The configuration contains default values and is complete**.  The configuration contains only default values. With these default values you can use the technology object without additional changes. |
| ![Icons of the configuration window](images/29886007307_DV_resource.Stream@PNG-de-DE.png) | **The configuration contains values set by the user and is complete.**   All input fields of the configuration contain valid values and at least one preset value has changed. |
| ![Icons of the configuration window](images/29885766411_DV_resource.Stream@PNG-de-DE.png) | **The configuration is incomplete or incorrect**   At least one input field or drop-down list contains an invalid value. The corresponding field or the drop-down list is displayed on a red background. Click the roll-out error message to indicate the cause of error. |
| ![Icons of the configuration window](images/29886018955_DV_resource.Stream@PNG-de-DE.png) | **The configuration is valid but contains warnings**   Only one hardware limit switch is configured. Depending on the plant, the lacking configuration of a hardware limit switch may result in a hazard. The corresponding field or the drop-down list is displayed on a yellow background. |

#### Basic parameters (S7-300, S7-400)

This section contains information on the following topics:

- [Naming the axis (S7-300, S7-400)](#naming-the-axis-s7-300-s7-400)
- [Selecting axis type (S7-300, S7-400)](#selecting-axis-type-s7-300-s7-400)
- [Selecting length units (S7-300, S7-400)](#selecting-length-units-s7-300-s7-400)
- [Activating simulation mode (S7-300, S7-400)](#activating-simulation-mode-s7-300-s7-400)

##### Naming the axis (S7-300, S7-400)

###### Axis name

Define the name of the axis, or the name of the "Axis" technology object, in this field. The technology object is listed under this name in the project navigator.

##### Selecting axis type (S7-300, S7-400)

###### Axis types

Easy Motion Control is able to control the following axis types:

- Linear axis

  A linear axis is an axis which has a limited physical traversing range.

  ![Axis types](images/29860848139_DV_resource.Stream@PNG-en-US.png)
- Rotary axis

  The rotary axis is an axis whose traversing range is not restricted by mechanical stops.

  ![Axis types](images/29860859787_DV_resource.Stream@PNG-en-US.png)

###### Data used in the axis DB

| Address | Name | Type | Initial value | Comment |  |
| --- | --- | --- | --- | --- | --- |
| 4.0 | AxisType | BOOL | FALSE | **Axis type**   Valid values:   - FALSE = Linear axis - TRUE = Rotary axis | ![Data used in the axis DB](images/29245571339_DV_resource.Stream@PNG-de-DE.png) |

##### Selecting length units (S7-300, S7-400)

###### Length unit

Select the length unit for the axis unit system from the drop-down list. The selected unit will be used for further configuration of the "Axis" TO and for visualization of the current axis data.

You can select a length unit for data input and output from the following:

- Millimeter (default setting)
- Degree
- Inch

The values at the input parameters (Position, Distance, Velocity, ...) of the Motion Control instructions also refer to this unit.

> **Note**
>
> A change of the length unit will not affect the values of the parameters. There, is no conversion.

###### Data used in the axis DB

| Address | Name | Type | Initial value | Comment |
| --- | --- | --- | --- | --- |
| 196.0 | LengthUnit | STRING [4] | mm | **Length unit** for configuration software  Valid values:  - mm (default) - Degree - Inch |

##### Activating simulation mode (S7-300, S7-400)

###### Simulation mode

Select the check box if you want to test your traversing program without traversing the axis.

###### Data used in the axis DB

| Address | Name | Type | Initial value | Comment |
| --- | --- | --- | --- | --- |
| 4.2 | Sim | BOOL | FALSE | **Simulation mode**   Valid values:  - FALSE = Deactivated - TRUE = Activated |

#### Advanced parameters (S7-300, S7-400)

This section contains information on the following topics:

- [Driver interfaces (S7-300, S7-400)](#driver-interfaces-s7-300-s7-400)
- [Mechanics (S7-300, S7-400)](#mechanics-s7-300-s7-400)
- [Limit switches (S7-300, S7-400)](#limit-switches-s7-300-s7-400)
- [Dynamic response (S7-300, S7-400)](#dynamic-response-s7-300-s7-400)
- [Monitoring (S7-300, S7-400)](#monitoring-s7-300-s7-400)

##### Driver interfaces (S7-300, S7-400)

This section contains information on the following topics:

- [Input driver (S7-300, S7-400)](#input-driver-s7-300-s7-400)
- [Output drivers (S7-300, S7-400)](#output-drivers-s7-300-s7-400)

###### Input driver (S7-300, S7-400)

This section contains information on the following topics:

- [Selecting an input module (S7-300, S7-400)](#selecting-an-input-module-s7-300-s7-400)
- [Selecting the encoder type (S7-300, S7-400)](#selecting-the-encoder-type-s7-300-s7-400)
- [Input module: Module address inputs (S7-300, S7-400)](#input-module-module-address-inputs-s7-300-s7-400)
- [Input module: Module address outputs (S7-300, S7-400)](#input-module-module-address-outputs-s7-300-s7-400)
- [Input module: Channel number (S7-300, S7-400)](#input-module-channel-number-s7-300-s7-400)

###### Selecting an input module (S7-300, S7-400)

###### Input module

Select the input module to which your encoder is connected from the drop-down list.

Based on your selection, the "Instruction" field displays the name of the instruction that you have to call for actual value acquisition.

###### Data used in the axis DB

| Address | Name | Type | Initial value | Comment |
| --- | --- | --- | --- | --- |
| 202.0 | InputModuleType | STRING [24] | IM 174 | Input driver **for the module**.  It is not allowed to overwrite this parameter in manual mode. |

###### Selecting the encoder type (S7-300, S7-400)

###### Encoder type

Select the check box for the encoder used.

###### Data used in the axis DB

| Address | Name | Type | Initial value | Comment |  |
| --- | --- | --- | --- | --- | --- |
| 4.1 | EncoderType | BOOL | FALSE | **Encoder type**   Valid values:  - FALSE = Incremental encoder - TRUE = Absolute encoder | ![Data used in the axis DB](images/29245571339_DV_resource.Stream@PNG-de-DE.png) |

###### Input module: Module address inputs (S7-300, S7-400)

###### Module address inputs

Enter the value specified for the input module in your hardware configuration in the text box.

###### Data used in the axis DB

| Address | Name | Type | Initial value | Comment |  |
| --- | --- | --- | --- | --- | --- |
| 58.0 | InputModuleInAddr | INT | 0 | **Start address of the inputs of the position decoder module**   Range:  - Determined by the hardware configuration | ![Data used in the axis DB](images/29245571339_DV_resource.Stream@PNG-de-DE.png) |

###### Input module: Module address outputs (S7-300, S7-400)

###### Module address outputs

The parameter is used only for modules for which it is possible to set the "Module address outputs" separately from the "Module address inputs" in the hardware configuration.

Enter the value specified for the input module in your hardware configuration in the text box.

###### Data used in the axis DB

| Address | Name | Type | Initial value | Comment |  |
| --- | --- | --- | --- | --- | --- |
| 60.0 | InputModuleOutAddr | INT | 0 | **Start address of the outputs of the position decoder module**   Range:  - Determined by the hardware configuration | ![Data used in the axis DB](images/29245571339_DV_resource.Stream@PNG-de-DE.png) |

###### Input module: Channel number (S7-300, S7-400)

###### Channel number

- Single-channel modules: The default value "0" that is set in the text box cannot be edited.
- Multi-channel modules: Enter the number of the channel used in this text box. Enter "0" for the first channel, etc.

###### Data used in the axis DB

| Address | Name | Type | Initial value | Comment |  |
| --- | --- | --- | --- | --- | --- |
| 62.0 | InputChannelNo | INT | 0 | **Channel number of the position input module**   Range:  - Depends on the module | ![Data used in the axis DB](images/29245571339_DV_resource.Stream@PNG-de-DE.png) |

###### Output drivers (S7-300, S7-400)

This section contains information on the following topics:

- [Selecting output modules (S7-300, S7-400)](#selecting-output-modules-s7-300-s7-400)
- [Output module: Module address inputs (S7-300, S7-400)](#output-module-module-address-inputs-s7-300-s7-400)
- [Output module: Module address outputs (S7-300, S7-400)](#output-module-module-address-outputs-s7-300-s7-400)
- [Output module: Channel number (S7-300, S7-400)](#output-module-channel-number-s7-300-s7-400)

###### Selecting output modules (S7-300, S7-400)

###### Output module

Select the output module to which your drive is connected from the drop-down list.

Based on your selection, the "Instruction" field displays the name of the instruction that you have to call for speed setpoint output.

###### Data used in the axis DB

| Address | Name | Type | Initial value | Comment |
| --- | --- | --- | --- | --- |
| 228.0 | OutputModuleType | STRING [24] | IM 174 | Output driver **for the module**.  It is not allowed to overwrite this parameter in manual mode. |

###### Output module: Module address inputs (S7-300, S7-400)

###### Module address inputs

The parameter is used only for modules for which it is possible to set the "Module address inputs" separately from the "Module address outputs" in the hardware configuration.

Enter the value specified for the output module in your hardware configuration in the text box.

###### Data used in the axis DB

| Address | Name | Type | Initial value | Comment |  |
| --- | --- | --- | --- | --- | --- |
| 82.0 | OutputModuleInAddr | INT | 0 | **Start address of the inputs of the output module**   Range:  - Determined by the hardware configuration | ![Data used in the axis DB](images/29245571339_DV_resource.Stream@PNG-de-DE.png) |

###### Output module: Module address outputs (S7-300, S7-400)

###### Module address outputs

Enter the value specified for the output module in your hardware configuration in the text box.

###### Data used in the axis DB

| Address | Name | Type | Initial value | Comment |  |
| --- | --- | --- | --- | --- | --- |
| 80.0 | OutputModuleOutAddr | INT | 0 | **Start address of the outputs of the module outputs**   Range:  - Determined by the hardware configuration | ![Data used in the axis DB](images/29245571339_DV_resource.Stream@PNG-de-DE.png) |

###### Output module: Channel number (S7-300, S7-400)

###### Channel number

- Single-channel modules: The default value "0" that is set in the text box cannot be edited.
- Multi-channel modules: Enter the number of the channel used in this text box. Enter "0" for the first channel, etc.

###### Data used in the axis DB

| Address | Name | Type | Initial value | Comment |  |
| --- | --- | --- | --- | --- | --- |
| 84.0 | OutputChannelNo | INT | 0 | **Channel number of the output module**   Range:  - Depends on the module | ![Data used in the axis DB](images/29245571339_DV_resource.Stream@PNG-de-DE.png) |

##### Mechanics (S7-300, S7-400)

This section contains information on the following topics:

- [Encoders (S7-300, S7-400)](#encoders-s7-300-s7-400)
- [Controller (S7-300, S7-400)](#controller-s7-300-s7-400)
- [Motor (S7-300, S7-400)](#motor-s7-300-s7-400)

###### Encoders (S7-300, S7-400)

This section contains information on the following topics:

- [Specifying the steps per encoder revolution (S7-300, S7-400)](#specifying-the-steps-per-encoder-revolution-s7-300-s7-400)
- [Specifying the number of encoder revolutions (S7-300, S7-400)](#specifying-the-number-of-encoder-revolutions-s7-300-s7-400)
- [Specifying the axis distance per encoder revolution (S7-300, S7-400)](#specifying-the-axis-distance-per-encoder-revolution-s7-300-s7-400)
- [Selecting the encoder polarity (S7-300, S7-400)](#selecting-the-encoder-polarity-s7-300-s7-400)

###### Specifying the steps per encoder revolution (S7-300, S7-400)

###### Steps per encoder revolution

In the text box, enter the number of steps that your position decoder module outputs per encoder revolution.

The number of steps is converted to the length unit based on this value and the "Axis distance per encoder revolution" parameter ([axis DB address 68.0](#specifying-the-axis-distance-per-encoder-revolution-s7-300-s7-400)).

###### Data used in the axis DB

| Address | Name | Type | Initial value | Comment |  |
| --- | --- | --- | --- | --- | --- |
| 64.0 | StepsPerRev | DINT | L#1 | **Steps per encoder revolution**   Valid range of values:   - ≥ 1 [steps/encoder revolution] | ![Data used in the axis DB](images/29245571339_DV_resource.Stream@PNG-de-DE.png) |

###### Incremental encoder

If the incremental encoder is read using a module that evaluates the pulses in a two-step or four-step operation, this has to be taken into account when entering the parameters.

Example:

- Encoder pulses per revolution: 500
- 4-step evaluation

In the "Steps per encoder revolution" text box, enter: 2000

###### Absolute encoder

The number of steps per encoder revolution is usually a power of two for absolute encoders.

Common values are:

- With single-turn encoders: 4096 and 8192
- With multi-turn encoders (12 × 12 bits in the 25-bit frame): 4096

If there, is any doubt, the correct value can be determined by moving the encoder one revolution and observing the change of the encoder value in the configuration software.

With a linear scale, enter the total number of steps for "Steps per encoder revolution" corresponding to the length of your linear scale.

###### Specifying the number of encoder revolutions (S7-300, S7-400)

###### Number of encoder revolutions

In the text box, enter the number of encoder revolutions for an absolute encoder.

Enter "1" for a single-turn encoder.

With a **linear scale**, enter "1" for "number of encoder revolutions".

This parameter is irrelevant for incremental encoders.

###### Data used in the axis DB

| Address | Name | Type | Initial value | Comment |  |
| --- | --- | --- | --- | --- | --- |
| 72.0 | NumberRevs | INT | 1 | **Number of revolutions** of an absolute encoder  Valid range of values:   - &gt; 0 | ![Data used in the axis DB](images/29245571339_DV_resource.Stream@PNG-de-DE.png) |

###### Specifying the axis distance per encoder revolution (S7-300, S7-400)

###### Axis distance per encoder revolution

In the text box, enter the distance traversed by the axis that is equivalent to one encoder revolution. This value depends on the structure of the axis and on the encoder mounting position. You must make allowances for all transmission elements, such as couplings or gears.

![Axis distance per encoder revolution](images/30225332619_DV_resource.Stream@PNG-en-US.png)

![Axis distance per encoder revolution](images/30225553291_DV_resource.Stream@PNG-en-US.png)

For a **linear scale**, enter the length of your linear scale for "Axis travel per encoder revolution".

###### Data used in the axis DB

| Address | Name | Type | Initial value | Comment |  |
| --- | --- | --- | --- | --- | --- |
| 68.0 | DisplacementPerRev | REAL | 1.0 | **Axis distance per encoder revolution**   Valid range of values:  - &gt; 0.0 [length unit/encoder revolution] | ![Data used in the axis DB](images/29245571339_DV_resource.Stream@PNG-de-DE.png) |

###### Special features with rotary axes

The encoder must perform an integer number of steps per rotary axis revolution:

![Special features with rotary axes](images/30225569163_DV_resource.Stream@PNG-en-US.png)

###### Special features for rotary axes with absolute encoders

To ensure the reproducibility of all positions, the axis traversing distance covered by the encoder must be an integer multiple of the distance that the rotary axis covers in one rotation:

![Special features for rotary axes with absolute encoders](images/30225600907_DV_resource.Stream@PNG-en-US.png)

**Example:**

24-bit absolute encoder

=&gt; Number of encoder revolutions = 4096

Rotary axis start = 0.0°

Rotary axis end = 360.0°

=&gt; Rotary axis end - rotary axis start = 360.0°

Axis distance per encoder revolution = 45°

![Special features for rotary axes with absolute encoders](images/30225585035_DV_resource.Stream@PNG-en-US.png)

###### Selecting the encoder polarity (S7-300, S7-400)

###### Set encoder polarity

Here, you adjust the position feedback direction to the movement direction of the axis:

- Positive = Incremental count pulses (incremental encoder), or encoder values (absolute encoder) represent increasing actual position values
- Negative = Incremental count pulses (incremental encoder), or encoder values (absolute encoder) represent descending actual position values.

Select the corresponding option from the drop-down list.

###### Data used in the axis DB

| Address | Name | Type | Initial value | Comment |  |
| --- | --- | --- | --- | --- | --- |
| 74.0 | PolarityEncoder | INT | 1 | **Set encoder polarity**   Valid values:  - +1 or -1 | ![Data used in the axis DB](images/29245571339_DV_resource.Stream@PNG-de-DE.png) |

###### Controller (S7-300, S7-400)

This section contains information on the following topics:

- [Specifying controller gain (S7-300, S7-400)](#specifying-controller-gain-s7-300-s7-400)
- [Specifying the velocity setpoint in manual mode (S7-300, S7-400)](#specifying-the-velocity-setpoint-in-manual-mode-s7-300-s7-400)

###### Specifying controller gain (S7-300, S7-400)

###### Controller gain

The optimum controller gain can be determined empirically on the axis.

Increase controller gain in increments of 1.0 until the axis begins to oscillate while traversing, or while it is at a standstill. If this is the case, reduce controller gain until this tendency to oscillate is no longer perceptible.

Enter the corresponding value in the text box.

###### Data used in the axis DB

| Address | Name | Type | Initial value | Comment |
| --- | --- | --- | --- | --- |
| 44.0 | FactorP | REAL | 1.0 | **Controller gain**   Valid range of values:   - &gt; 0.0 [1/s] |

###### Specifying the velocity setpoint in manual mode (S7-300, S7-400)

###### Velocity setpoint in manual mode

Enter a velocity setpoint for manual mode in this text box.

When manual mode is activate, the controller outputs the value in "Manual setpoint velocity" as a manipulated variable and limits it to "MaxVelocity". The position setpoint is tracked to the actual position value.

###### Data used in the axis DB

| Address | Name | Type | Initial value | Comment |
| --- | --- | --- | --- | --- |
| 48.0 | ManVelocity | REAL | 0.0 | **Velocity setpoint in manual mode**   Valid range of values:  - ≤ ± [MaxVelocity](#specifying-the-maximum-axis-velocity-s7-300-s7-400) [length unit/s] |
| 52.0 | ManEnable | BOOL | FALSE | **Activating manual mode**   Valid values:  - FALSE = Deactivated - TRUE = Activated |

###### Motor (S7-300, S7-400)

This section contains information on the following topics:

- [Reference value for 100 % speed (S7-300, S7-400)](#reference-value-for-100-speed-s7-300-s7-400)
- [Specifying the reference value for maximum axis velocity (S7-300, S7-400)](#specifying-the-reference-value-for-maximum-axis-velocity-s7-300-s7-400)
- [Specifying zero offset compensation (S7-300, S7-400)](#specifying-zero-offset-compensation-s7-300-s7-400)
- [Selecting the drive polarity (S7-300, S7-400)](#selecting-the-drive-polarity-s7-300-s7-400)

###### Reference value for 100 % speed (S7-300, S7-400)

###### Reference value for 100 % speed

This parameter is irrelevant when you are operating power units with a control voltage of ±10 V.

When you use the OutputMM4_DP output driver (bus-controlled MICROMASTER DP module), set the frequency that is needed to accelerate the drive to 100% of its speed at this parameter.

###### Data used in the axis DB

| Address | Name | Type | Initial value | Comment |  |
| --- | --- | --- | --- | --- | --- |
| 96.0 | DriveInputAt100 | REAL | 10.0 | **Reference value for 100 % speed**   Valid range of values:   - -10.0 to +10.0 [V] | ![Data used in the axis DB](images/29245571339_DV_resource.Stream@PNG-de-DE.png) |

###### Example

- Rated speed (100 %) of the motor: = 1380 rpm
- Motor is synchronized to: = 1380 rpm at 50 Hz

=&gt; Enter "Reference value for 100% speed = 50 Hz

###### Specifying the reference value for maximum axis velocity (S7-300, S7-400)

###### Reference value for maximum axis velocity

If using power unit with a control voltage of **±10 V**, enter the voltage value at which the drive reaches "Maximum velocity" in the text box (see [Axis DB address 14.0](#specifying-the-maximum-axis-velocity-s7-300-s7-400)).

Example:

- Rated speed of the motor: = 3000 rpm
- Motor is synchronized to: = 9 V at 3000 rpm
- Maximum speed to reach: = 1500 rpm

=&gt; Enter the following value for "Reference value for maximum axis speed": = 4.5 V

If using the **OutputMM4_DP** output driver, enter the voltage value at which the drive reaches "Maximum speed" in the text box (see [Axis DB address 14.0](#specifying-the-maximum-axis-velocity-s7-300-s7-400)).

Example:

- Rated speed of the motor: = 1380 rpm
- Motor is synchronized to: = 1380 rpm at 50 Hz
- Maximum speed to reach: = 690 rpm

=&gt; Enter the following value for "Reference value for maximum axis speed": = 25 Hz

###### Data used in the axis DB

| Address | Name | Type | Initial value | Comment |  |
| --- | --- | --- | --- | --- | --- |
| 88.0 | DriveInputAtMaxVel | REAL | 9.0 | **Reference value for max. axis velocity [V]**   Valid range of values:  - Depends on the power unit | ![Data used in the axis DB](images/29245571339_DV_resource.Stream@PNG-de-DE.png) |

###### Specifying zero offset compensation (S7-300, S7-400)

###### Zero offset compensation

Use this parameter to implement zero offset compensation if your drive does not provide this option. The value configured here is added to the output value.

The OutputMM4_DP output driver ignores this parameter.

###### Data used in the axis DB

| Address | Name | Type | Initial value | Comment |
| --- | --- | --- | --- | --- |
| 92.0 | OffsetCompensation | REAL | 0.0 | **Zero offset compensation**   Valid range of values:   - -10.0 to +10.0 [V] |

###### Selecting the drive polarity (S7-300, S7-400)

###### Set drive polarity

Here, you select the direction of drive movement:

- Positive = Positive velocity setpoints initiate movements towards the positive direction.
- Negative = positive velocity setpoints initiate movements towards the negative direction.

Select the corresponding option from the drop-down list.

If you change "Set drive polarity", you must also change "Set encoder polarity" ([Axis DB address 74.0](#selecting-the-encoder-polarity-s7-300-s7-400)).

###### Data used in the axis DB

| Address | Name | Type | Initial value | Comment |  |
| --- | --- | --- | --- | --- | --- |
| 86.0 | PolarityDrive | INT | 1 | **Steps per encoder revolution**   Valid values:  - +1 or -1 | ![Data used in the axis DB](images/29245571339_DV_resource.Stream@PNG-de-DE.png) |

##### Limit switches (S7-300, S7-400)

This section contains information on the following topics:

- [Activating software limit switches (S7-300, S7-400)](#activating-software-limit-switches-s7-300-s7-400)
- [Specifying software limit switches (S7-300, S7-400)](#specifying-software-limit-switches-s7-300-s7-400)

###### Activating software limit switches (S7-300, S7-400)

###### Software limit switches

Software limit switches are only available for linear axes.

Monitoring begins as soon as the axis has been synchronized and software limit switch monitoring has been activated.

When software limit switch monitoring is deactivated, the "Software limit switch start" and "Software limit switch end" parameters ([Axis DB addresses 6.0 and 10.0](#specifying-software-limit-switches-s7-300-s7-400)) are of no significance.

###### Data used in the axis DB

| Address | Name | Type | Initial value | Comment |
| --- | --- | --- | --- | --- |
| 42.1 | SWLimitEnable | BOOL | TRUE | **Monitoring software limit switches**   Valid values:  - TRUE = Monitoring activated - FALSE = Monitoring deactivated |

###### Specifying software limit switches (S7-300, S7-400)

###### Software limit switches

Software limit switches are only available for linear axes.

**Linear axis: Software limit switch start/end**

Monitoring begins as soon as the axis has been synchronized and software limit switch monitoring has been activated (see "[Activating software limit switches](#activating-software-limit-switches-s7-300-s7-400)"). The working range is limited by means of software limit switches.

The value in "Software limit switch start" must always be less than the "Software limit switch end" value.

**Incremental encoder**

Initially, the axis is not synchronized after CPU startup. The axis is not synchronized and the software limit switches are not monitored unless a reference point approach or reference point setting has been completed.

**Absolute encoder**

Once reference point setting has been completed, the setting will not be lost at the next CPU restart. The software limit switches can be monitored.  
The encoder range of the absolute encoder must cover at least the working range.

**Rotary axis: Rotary axis start / Rotary axis end**

"Rotary axis start" and "Rotary axis end" are used to define the range of axis position values to be displayed during one rotation of the axis.

The "Rotary axis end" value is theoretically the maximum an actual value can reach:

![Software limit switches](images/30253823755_DV_resource.Stream@PNG-en-US.png)

However, the theoretical maximum value is never displayed, as it is physically identical to the rotary axis start position (= zero).

**Example:**

- AxisLimitMin = 0.0°
- AxisLimitMax = 360.0°

With positive direction, the actual value counts ...359.8, 359.9, 0.0, 0.1, etc.

Pay attention to the "[Axis distance per encoder revolution](#specifying-the-axis-distance-per-encoder-revolution-s7-300-s7-400)" parameter when using absolute encoders.

###### Data used in the axis DB

| Address | Name | Type | Initial value | Comment |  |
| --- | --- | --- | --- | --- | --- |
| 6.0 | AxisLimitMax | REAL | 1.0e<sup>+6</sup> | Linear axis: **Software limit switch end**  Rotary axis: **Rotary axis end**  Valid range of values:   - -2<sup>24</sup>+6 ≤ AxisLimitMin &lt; AxisLimitMax ≤ +2<sup>24</sup>-6 [length unit] | ![Data used in the axis DB](images/29245571339_DV_resource.Stream@PNG-de-DE.png) |
| 10.0 | AxisLimitMin | REAL | -1.0e<sup>+6</sup> | Linear axis: **Software limit switch start**  Rotary axis: **Rotary axis start**  Valid range of values:   - -2<sup>24</sup>+6 ≤ AxisLimitMin &lt; AxisLimitMax ≤ +2<sup>24</sup>-6 [length unit] | ![Data used in the axis DB](images/29245571339_DV_resource.Stream@PNG-de-DE.png) |

##### Dynamic response (S7-300, S7-400)

This section contains information on the following topics:

- [General (S7-300, S7-400)](#general-s7-300-s7-400)
- [Emergency stop (S7-300, S7-400)](#emergency-stop-s7-300-s7-400)

###### General (S7-300, S7-400)

This section contains information on the following topics:

- [Specifying the maximum axis velocity (S7-300, S7-400)](#specifying-the-maximum-axis-velocity-s7-300-s7-400)
- [Specifying velocity override (S7-300, S7-400)](#specifying-velocity-override-s7-300-s7-400)
- [Specifying the maximum axis velocity (S7-300, S7-400)](#specifying-the-maximum-axis-velocity-s7-300-s7-400-1)
- [Specifying maximum axis deceleration (S7-300, S7-400)](#specifying-maximum-axis-deceleration-s7-300-s7-400)
- [Specifying the scan time (S7-300, S7-400)](#specifying-the-scan-time-s7-300-s7-400)
- [Displaying the ramp-up time (S7-300, S7-400)](#displaying-the-ramp-up-time-s7-300-s7-400)
- [Displaying the ramp-down time (S7-300, S7-400)](#displaying-the-ramp-down-time-s7-300-s7-400)

###### Specifying the maximum axis velocity (S7-300, S7-400)

###### Maximum axis velocity

Here, you configure the maximum axis velocity if the motor is controlled with the value entered in the "Reference value for maximum axis velocity" parameter ([Axis DB address 88.0](#specifying-the-reference-value-for-maximum-axis-velocity-s7-300-s7-400)).

The "Maximum axis velocity" parameter is also used as a factor for calculating the value of the signal output to the drive, as well as for limiting the axis velocity.

###### Special features for rotary axes with absolute encoders

To enable the recording of all the rotary axis rotations, the maximum axis velocity must be limited so that the distance traversed in each scan cycle is less than half of the encoder range of the absolute encoder.

**Example for single-turn encoders:**

Condition =&gt; one axis rotation is equivalent to one encoder rotation.

Traversing distance / encoder range = 360.0°

Traversing distance / half of encoder range = 180.0°

Scan time = 0.01 s

![Special features for rotary axes with absolute encoders](images/30264144779_DV_resource.Stream@PNG-en-US.png)

=&gt; "Maximum velocity" &lt; 180.0° / 0.01s = 18000°/s is equivalent to 50 axis rev/s

###### Data used in the axis DB

| Address | Name | Type | Initial value | Comment |  |
| --- | --- | --- | --- | --- | --- |
| 14.0 | MaxVelocity | REAL | 0.1 | **Maximum axis velocity**   Valid range of values:   - &gt; 0.0 [unit of length/s] | ![Data used in the axis DB](images/29245571339_DV_resource.Stream@PNG-de-DE.png) |

###### Specifying velocity override (S7-300, S7-400)

###### Velocity override

"Velocity override" has a sustained effect on the configured velocity of a travel instruction.   
Acceleration and deceleration values are not affected.

Example: Travel trends with 50 % and 100 % override

![Velocity override](images/30265557771_DV_resource.Stream@PNG-en-US.png)

The velocity is doubled if you switch from 50 % to 100 %. As acceleration and deceleration are not affected by the "Velocity override" parameter, however, the positioning time is **not** halved.

###### Data used in the axis DB

| Address | Name | Type | Initial value | Comment |
| --- | --- | --- | --- | --- |
| 100.0 | Override | REAL | 100.0 | **Velocity override**   Valid range of values:  - 0.0 to +100.0 [%] |

###### Specifying the maximum axis velocity (S7-300, S7-400)

###### Maximum axis acceleration

The gradient of the acceleration ramp of the axis is limited to this value in controlled mode.

The maximum possible acceleration can be determined empirically.

It should only be high enough so that, when accelerating to maximum velocity (under load), it is just below the current limit of the drive.

###### Data used in the axis DB

| Address | Name | Type | Initial value | Comment |  |
| --- | --- | --- | --- | --- | --- |
| 18.0 | MaxAcceleration | REAL | 0.1 | **Maximum axis acceleration**   Valid range of values:   - &gt; 0.0 [length unit/s<sup>2</sup>] | ![Data used in the axis DB](images/29245571339_DV_resource.Stream@PNG-de-DE.png) |

###### Specifying maximum axis deceleration (S7-300, S7-400)

###### Maximum axis deceleration

The slope of the deceleration ramp of the axis is restricted to this value in controlled mode.

The maximum possible deceleration can be determined empirically.

It should only be high enough so that, when slowing down from maximum velocity (under load), it is just below the current limit of the drive.

###### Data used in the axis DB

| Address | Name | Type | Initial value | Comment |  |
| --- | --- | --- | --- | --- | --- |
| 22.0 | MaxDeceleration | REAL | 0.1 | **Maximum axis deceleration**   Valid range of values:   - &gt; 0.0 [length unit/s<sup>2</sup>] | ![Data used in the axis DB](images/29245571339_DV_resource.Stream@PNG-de-DE.png) |

###### Specifying the scan time (S7-300, S7-400)

###### Scan time

To ensure correct functioning of position control, it is important that all functions of one axis are processed in a fixed time frame. This time pattern is determined by calling all instructions of an axis in the same cyclic interrupt or synchronous cycle interrupt OB. Select the time pattern of this OB in the hardware configuration of the CPU.

For the "Scan time", enter the time pattern of the OB in which you call all instructions of an axis.

**Example:**

Call the program using the Easy Motion Control instructions in OB 35. You have set the cyclic interrupt time pattern of OB 35 to 10 ms in the hardware configuration.

Enter 0.010 as the "scan time".

###### Data used in the axis DB

| Address | Name | Type | Initial value | Comment |  |
| --- | --- | --- | --- | --- | --- |
| 0.0 | Sample_T | REAL | 0.01 | **Scan time** of the axis instructions  Recommended:  - S7 300 to CPU 316 ≥ 0.020 [s] - S7 400 and as of CPU 317 ≥ 0.004 [s] | ![Data used in the axis DB](images/29245571339_DV_resource.Stream@PNG-de-DE.png) |

###### Displaying the ramp-up time (S7-300, S7-400)

###### Ramp­up time

The ramp-up time denotes the time an axis needs to accelerate from a standstill to maximum velocity.

The ramp-up time is calculated based on the following parameters:

|  |  |  |
| --- | --- | --- |
| Ramp­up time | = | Maximum axis velocity × velocity override /  maximum acceleration |

The output field displays the calculated ramp-up time.

###### Displaying the ramp-down time (S7-300, S7-400)

###### Ramp-down time

The ramp-down time denotes the time required to decelerate an axis without jerk limitation from maximum velocity to a standstill.

The ramp-down time is calculated based on the following parameters:

|  |  |  |
| --- | --- | --- |
| Ramp-down time | = | Maximum axis velocity × velocity override /  maximum deceleration |

The output field displays the calculated ramp-down time.

###### Emergency stop (S7-300, S7-400)

This section contains information on the following topics:

- [Specifying emergency stop deceleration (S7-300, S7-400)](#specifying-emergency-stop-deceleration-s7-300-s7-400)
- [Displaying the ramp-down time (S7-300, S7-400)](#displaying-the-ramp-down-time-s7-300-s7-400-1)

###### Specifying emergency stop deceleration (S7-300, S7-400)

###### Deceleration for emergency stop (hard stop)

At this parameter you define the slope of the time-controlled deceleration ramp used to decelerate the drive when an error with hard stop occurs.

###### Data used in the axis DB

| Address | Name | Type | Initial value | Comment |  |
| --- | --- | --- | --- | --- | --- |
| 54.0 | EmergencyDec | REAL | 1.0 | **Emergency stop deceleration**   Valid range of values:   - &gt; 0.0 [length unit/s<sup>2</sup>] | ![Data used in the axis DB](images/29245571339_DV_resource.Stream@PNG-de-DE.png) |

###### Displaying the ramp-down time (S7-300, S7-400)

###### Ramp-down time

The ramp-down time denotes the time required to decelerate an axis in emergency stop mode from maximum velocity to a standstill.

The ramp-down time is calculated based on the following parameters:

|  |  |  |
| --- | --- | --- |
| Ramp-down time | = | Maximum axis velocity / emergency stop deceleration |

The output field displays the calculated ramp-down time.

##### Monitoring (S7-300, S7-400)

This section contains information on the following topics:

- [Specifying the target range (S7-300, S7-400)](#specifying-the-target-range-s7-300-s7-400)
- [Specifying the standstill range (S7-300, S7-400)](#specifying-the-standstill-range-s7-300-s7-400)
- [Target approach monitoring (S7-300, S7-400)](#target-approach-monitoring-s7-300-s7-400)
- [Specifying the monitoring time for target approach (S7-300, S7-400)](#specifying-the-monitoring-time-for-target-approach-s7-300-s7-400)
- [Specifying the valid maximum following error (S7-300, S7-400)](#specifying-the-valid-maximum-following-error-s7-300-s7-400)

###### Specifying the target range (S7-300, S7-400)

###### Target range

The "target range" lies to the left and right of the target (see [Concept Definitions](#concept-definitions-s7-300-s7-400)).

###### Data used in the axis DB

| Address | Name | Type | Initial value | Comment |  |
| --- | --- | --- | --- | --- | --- |
| 30.0 | TargetRange | REAL | 1.0 | **Target range**   Valid range of values:   - &gt; 0.0 [length unit] | ![Data used in the axis DB](images/29245571339_DV_resource.Stream@PNG-de-DE.png) |

###### Specifying the standstill range (S7-300, S7-400)

###### Standstill range

When at a standstill, the axis is monitored to determine whether it is remaining at a given position or drifting away from it. The "Outside standstill range" error bit ([Axis DB address 130.3](#error-with-hard-stop-s7-300-s7-400)) is set as soon as the axis leaves the "standstill range" without an active traversing job. The "standstill range" lies to the left and right of the target (see [Concept Definitions](#concept-definitions-s7-300-s7-400)).

Recommended: The "standstill range" should be greater than the "target range" ([Axis DB address 30.0](#specifying-the-target-range-s7-300-s7-400)).

###### Data used in the axis DB

| Address | Name | Type | Initial value | Comment |  |
| --- | --- | --- | --- | --- | --- |
| 34.0 | StandstillRange | REAL | 1.5 | **Standstill range**   Valid range of values:   - &gt; 0.0 [length unit] | ![Data used in the axis DB](images/29245571339_DV_resource.Stream@PNG-de-DE.png) |

###### Target approach monitoring (S7-300, S7-400)

###### Monitoring the target approach

When target range monitoring is activated, a movement is terminated as soon as the actual position value has reached the "target range" (axis DB address 30.0) within the "Monitoring time for target approach" (axis DB address 26.0).

If target range monitoring is deactivated, axis movement is terminated as soon as the position setpoint has reached the target (see [Terminology](#concept-definitions-s7-300-s7-400)).

###### Data used in the axis DB

| Address | Name | Type | Initial value | Comment |
| --- | --- | --- | --- | --- |
| 42.0 | MonitorTargetAppr | BOOL | TRUE | **Target approach monitoring**   Valid values:  - TRUE = Monitoring activated - FALSE = Monitoring deactivated |

###### Specifying the monitoring time for target approach (S7-300, S7-400)

###### Monitoring time for target approach

The "Monitoring time for target approach" starts as soon as the traversing axis has reached the **position setpoint** in the target area, provided the "Monitor target approach" bit has been set ([Axis DB address 42.0](#target-approach-monitoring-s7-300-s7-400)). If the **actual position value** has not reached the range defined in the "target area" parameter ([Axis DB address 30.0](#specifying-the-target-range-s7-300-s7-400)) on expiration of this time, the "Target approach error" bit is set in the axis DB ([Axis DB address 130.4](#error-with-hard-stop-s7-300-s7-400)).

###### Data used in the axis DB

| Address | Name | Type | Initial value | Comment |  |
| --- | --- | --- | --- | --- | --- |
| 26.0 | MonTimeTargetAppr | REAL | 1.0 | **Monitoring time for target approach**   Valid range of values:   - &gt; 2 × Sample_T [s] ([scan time](#specifying-the-scan-time-s7-300-s7-400)) | ![Data used in the axis DB](images/29245571339_DV_resource.Stream@PNG-de-DE.png) |

###### Specifying the valid maximum following error (S7-300, S7-400)

###### Maximum permitted following distance

The following error monitoring function is used to check whether the actual position during a motion remains inadmissibly far behind the position setpoint. If the maximum following error has been exceeded, the "Following error exceeded" error bit is set in the axis DB" ([Axis DB address 130.2](#error-with-hard-stop-s7-300-s7-400)).

Recommended setting: ("maximum velocity" / "controller gain") × 1.1 (see axis DB addresses [14.0](#specifying-the-maximum-axis-velocity-s7-300-s7-400) and [44.0](#specifying-controller-gain-s7-300-s7-400))

###### Data used in the axis DB

| Address | Name | Type | Initial value | Comment |  |
| --- | --- | --- | --- | --- | --- |
| 38.0 | MaxFollowingDist | REAL | 5.0 | **Maximum permitted following distance**   Valid range of values:   - &gt; 0.0 [length unit] | ![Data used in the axis DB](images/29245571339_DV_resource.Stream@PNG-de-DE.png) |

## Download to CPU (S7-300, S7-400)

New or modified project data must be downloaded to the CPU.

### Downloading the program blocks and the TO configuration to the CPU

Proceed as follows for downloading:

1. Select the "Program blocks" object, or the "Technology objects" object in the project navigator.
2. Select the "Online &gt; Download to device" command.

> **Note**
>
> Whenever you download blocks to the CPU, the TIA Portal always verifies consistency between the offline project blocks and the online blocks in the CPU.
>
> Regardless of the marking in the project tree, all new and modified offline blocks and technology objects are downloaded to the CPU.
>
> On each loading operation, all process values of the data blocks are reset to their initial values.

### Downloading the hardware configuration to the CPU

Proceed as follows when downloading the hardware configuration:

1. Select the CPU object in the project navigator.
2. Select the "Download &gt; Hardware configuration" command from the shortcut menu.

### Downloading the program blocks and the TO configuration to the CPU

Proceed as follows for downloading:

1. Select the CPU object in the project navigator.
2. Select the "Online &gt; Download to device" command.

## Programming Easy Motion Control (S7-300, S7-400)

This section contains information on the following topics:

- [User Program Setup (S7-300, S7-400)](#user-program-setup-s7-300-s7-400)
- [Influences on Position Control in the CPU (S7-300, S7-400)](#influences-on-position-control-in-the-cpu-s7-300-s7-400)
- [Importance of Shared Parameters (S7-300, S7-400)](#importance-of-shared-parameters-s7-300-s7-400)
- [Initialization and Parameter Changes (S7-300, S7-400)](#initialization-and-parameter-changes-s7-300-s7-400)
- [Sequence of Travel Movements (S7-300, S7-400)](#sequence-of-travel-movements-s7-300-s7-400)
- [Axis data block (S7-300, S7-400)](#axis-data-block-s7-300-s7-400)
- [User Program as a Multi-instance FB (S7-300, S7-400)](#user-program-as-a-multi-instance-fb-s7-300-s7-400)

### User Program Setup (S7-300, S7-400)

#### Interaction of the instructions

The following figure demonstrates how instructions interact in Easy Motion Control.

![Interaction of the instructions](images/29551922059_DV_resource.Stream@PNG-en-US.png)

instruction MC_Init serves to **initialize** the instructions.

The **input driver** (Encoder… instruction) reads the actual position value of an axis from the I/O module and scales this value in accordance with the length unit that you have selected.

One of the **travel instructions** generates the position setpoint.

The **position controller** (MC_Control instruction) compares the actual position value with the position setpoint and generates a velocity setpoint value from the difference.

The **output driver** (Output… instruction) scales the velocity setpoint to the suitable format and writes it to the connected I/O module.

The program for a **closed-loop control circuit** consists of the input driver (Encoder…), at least one travel instruction, the controller (MC_Control), and the output driver (Output…).

All instructions of an axis work with the same **Axis DB**. This axis DB contains all axis data needed to operate the axis and is available for each axis. Read the information on [Loading the axis DB](#saving-and-loading-the-axis-data-block-s7-300-s7-400).

#### Call environment

To ensure correct functioning of position control, it is important that all functions of one axis are processed in a fixed **time frame**. This time pattern is determined by calling the instructions of Easy Motion Control in the **same** execution level. The following two methods can be applied, depending on the CPU and type of I/O connection used:

**Cyclic interrupt OB (OB 30 to OB 38)**

 Used for central integration of the I/O, or for distributed integration via DP bus system without constant bus cycle time. The cyclic interrupt time corresponds to the position-control cycle.

**Synchronous cycle interrupt OBs (OB 61 to OB 64)**

 The position control cycle on a continuously isochronous DP bus for I/O integration corresponds to the value you have selected in the bus configuration for "Constant bus cycle time".

This value must be entered at the axis DB in both cases.

For general information on the isochronous mode, refer to the TIA Portal online help and to the [Isochronous Mode Function Manual](http://support.automation.siemens.com/WW/view/en/15218045).

Please note the following special features for Easy Motion Control:

- When configuring the I/O bus and the DP slaves / IO devices (including their modules, if applicable), you must select and configure the "constant bus cycle time".
- The I/O addresses of an axis used for position detection or setpoint output must be placed in the same process image partition (PIP). When using gear axes, both gear axes must be placed into the same PIP.
- When configuring the CPU, this PIP is assigned to the synchronous cycle interrupt used.
- You need to update this PIP in the interrupt OB before and after each call of the EMC blocks using the system instructions "SYNC_PI" / "SYNC_PO".
- Evaluate the feedback from these system instructions in your program and respond accordingly. (If an error has occurred, the PIP update has possibly failed and the actual value read was therefore incorrect.)

#### Recommended Call Sequence

The following figure shows the call sequence recommended for the instructions of Easy Motion Control.

![Recommended Call Sequence](images/29551906187_DV_resource.Stream@PNG-en-US.png)

(*) A call of the gear instruction MC_GearIn is only appropriate for following axes.

#### Multiple Axes

We recommend the following user program structure for controlling multiple axes in one CPU:

![Multiple Axes](images/29551890315_DV_resource.Stream@PNG-en-US.png)

| **Recommended for** the cyclic interrupt OB**.** | **Recommended for** the synchronous cycle OB. |
| --- | --- |
| **Advantage:** Calling the input drivers at the start of the OB produces a minimum time offset and minimum jitter when reading the I/O. | **Advantage:** It is possible to group all instructions of an axis in a single multi-instance instruction.   Due to the PIP, which is required for the synchronous cycle interrupt OB, the read I/O data are consistent irrespective of the driver call. |
| **Disadvantage:** It is not possible to group all instructions of an axis in a single multi-instance instruction. |  |

All interacting axes must be called in the same OB.

**All** axes of an isochronous application must be placed into the same process image partition.

#### Handling Instance Data

You can store the **instance data** for each instruction in its own DB, or in a single multi-instance DB for all instructions.

On completion of the download of the instance data of a instruction to the module, it is necessary to initialize the instruction. Set the "Init" input of the instruction accordingly. See also [Initialization and Parameter Changes](#initialization-and-parameter-changes-s7-300-s7-400) and [Saving and Loading the Axis Data Block](#saving-and-loading-the-axis-data-block-s7-300-s7-400).

#### Interconnecting the instructions

The **connections** between the instructions and the axis DB displayed in the above figure under Interaction of the instructions are handled using the following parameters:

- Axis
- Init

(See [Significance of the common parameters](#importance-of-shared-parameters-s7-300-s7-400))

The following interconnections are also necessary:

- The "EnableDrive" input of instruction MC_Control must be interconnected with an enable switch. instruction MC_Control will only output a speed setpoint if input "EnableDrive" = TRUE.
- Input "EnableDrive" of instruction Output… must be interconnected with output "DriveEnabled" of instruction MC_Control. "EnableDrive" = TRUE must be set in order to output a value not equal to zero at instruction Output….
- You should interconnect the "DriveEnabled" output of instruction MC_Control with the enable input of your drive.

  ![Interconnecting the instructions](images/29551759243_DV_resource.Stream@PNG-en-US.png)

### Influences on Position Control in the CPU (S7-300, S7-400)

Recommended for optimal position control:

- Scan time must be adhered to as closely as possible.

  - In the hardware configuration parameters for the CPU, assign the highest possible priority to the cyclic interrupt OB that calls the instructions.
  - Minimize the communication load on the cycle as far as possible with appropriate parameter settings in the hardware configuration of the CPU.
  - Use an isochronous environment to avoid having to take additional measures.
- When integrating encoder value acquisition via distributed I/O (PROFIBUS DP / PROFINET IO), set the maximum possible transmission rate for the I/O bus (for example, 12 Mbps).

### Importance of Shared Parameters (S7-300, S7-400)

The following table lists the parameters that are used in all instructions.

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| EN | INPUT | BOOL | Enable input of LAD/instructionD box |
| ENO | OUTPUT | BOOL | Enable output of LAD/instructionD box |
| Axis | IN-OUT | STRUCT | Interconnect this parameter with the axis DB.  For a DB of the type AXIS_REF, the interconnection is:  - Axis := DBname.Ax   For a DB that contains a variable of the type AXIS_REF, the interconnection is:  - Axis := DBname.Variable name.Ax |
| Init | IN-OUT | BOOL | Interconnect these parameter with an initialization bit in the axis DB that is not used by any other instruction ("Init.I0" … "Init.I31"; refer to [Bit array for the initialization function](#bit-field-for-the-initialization-function-s7-300-s7-400)).  With Init = TRUE, the instruction completes its initialization and then resets the bit.  For a DB of the type AXIS_REF, the interconnection is:  - Init := DBname.Ax.Init.Ix   For a DB that contains a variable of the type AXIS_REF, the interconnection is:  - Init := DBname.Variablename.Ax.Init.Ix  when Ix = I0 … I31 |

### Initialization and Parameter Changes (S7-300, S7-400)

The functionality of Easy Motion Control instructions is based on the data stored in the axis DB. This is where parameters describing the basic axis itself can also be found. If these parameters are changed, **all** Easy Motion Control instructions called in your user program must run their initialization **once** following the change. These parameters are identified in [configuration sections](#configuring-the-axis-to-s7-300-s7-400) by the following symbol:

![Figure](images/29245571339_DV_resource.Stream@PNG-de-DE.png)

Bit array "Init.Ix" is defined for initialization in the axis DB and all instructions are assigned the "Init" parameter. The instructions run their initialization routine if their "Init" input is set and then reset the interconnected initialization bit.

The bits in the "Init.Ix" bit array are set in the axis DB:

- At every call of instruction MC_Init.
- By the configuration software in the event of any change in corresponding parameters of the axis DB

Interconnect the "Init" parameter with an initialization bit in the axis DB that is not in use by any other instruction for all Easy Motion Control instructions called in your user program. This interconnection ensures that the instructions run their initialization routine whenever this becomes necessary as a result of parameter changes or CPU restart ("Init.I0" … "Init.I31"; refer to [Bit array for the initialization function](#bit-field-for-the-initialization-function-s7-300-s7-400)).

Call instruction MC_Init once in the following situations:

- After every startup of the CPU
- If you have changed one of the parameters identified by the following symbol in the [configuration sections](#configuring-the-axis-to-s7-300-s7-400) without using the configuration software:

  ![Figure](images/29245571339_DV_resource.Stream@PNG-de-DE.png)

For additional information on the initialization instruction, refer to [MC_Init](Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#mc_init-s7-300-s7-400).

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| Parameters identified by the following symbol in the [configuration section](#configuring-the-axis-to-s7-300-s7-400) may only be changed **when the axis is at a standstill**: ![Figure](images/29245571339_DV_resource.Stream@PNG-de-DE.png)  If you do not observe this rule, controlled axis movement cannot be guaranteed. |  |

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| During initialization, specific auxiliary values are calculated and saved to the static parameters of the instructions and to the axis DB. For this reason, you are only permitted to overwrite the instance data blocks and the axis DB when the axis is at a standstill.   If you do not observe this rule, controlled axis movement cannot be guaranteed. |  |

### Sequence of Travel Movements (S7-300, S7-400)

**Start of a travel order**

The input parameters of travel instructions are interpreted once at the start of a travel order. Changing these values while an order is in progress does not affect current travel.

**Maximum Travel Distance**

The travel distance per movement is limited to the distance that is equivalent to 2<sup>24</sup> steps of the encoder. It is calculated as follows:

![Figure](images/29553194507_DV_resource.Stream@PNG-en-US.png)

**Example:**

| Symbol | Meaning |
| --- | --- |
| Axis distance per encoder revolution | = 2.5 mm |
| Steps per encoder revolution | = 4096 |
| Maximum distance = 2<sup>24</sup> x 2.5 mm / 4096 | = 10240 mm |

**Exception:**

The MC_MoveJog and MC_GearIn instructions do not limit the traversing distance of a rotary axis.

#### Overriding travel

A currently active travel instruction can always be

- Overridden by starting a different travel instruction
- Cancelled by the start of instruction MC_StopMotion
- Aborted by setting manual mode

When overridden by another travel instruction, the axis is decelerated or accelerated to the velocity specified in the overriding instruction and then approaches the new target without intermediate stop. The overridden travel instruction sets the "CommandAborted" output.

If the new motion requires a change in direction of the axis, the axis is first stopped and then moved in the opposite direction (reversal).

For safety reasons, the deceleration of the two travel instructions involved in the override must coincide. This ensures that on reversing direction, the **original** target of the movement is not overtraveled.

#### Multiple use of a travel instruction

A travel instruction can be called several times for an axis in your program if necessary.

#### Error Response

All errors that occur are indicated in the axis DB, where they must be acknowledged by the user (see [Error Displays and Error Acknowledgment in the axis DB](#error-displays-and-error-acknowledgement-in-the-axis-db-s7-300-s7-400)). Each error will abort any travel order that is currently active. A new travel order can only start if there is no longer any error pending.

#### Signal Flow Diagrams

The following diagram shows the signal flow of a movement without error.

![Signal Flow Diagrams](images/29330561419_DV_resource.Stream@PNG-en-US.png)

The following diagram shows the signal flow of a movement with error.

![Signal Flow Diagrams](images/32834237451_DV_resource.Stream@PNG-en-US.png)

### Axis data block (S7-300, S7-400)

This section contains information on the following topics:

- [Function (S7-300, S7-400)](#function-s7-300-s7-400)
- [Saving and Loading the Axis Data Block (S7-300, S7-400)](#saving-and-loading-the-axis-data-block-s7-300-s7-400)
- [Axis parameters (S7-300, S7-400)](#axis-parameters-s7-300-s7-400)
- [Actual values (S7-300, S7-400)](#actual-values-s7-300-s7-400)
- [Bit Field for the Initialization Function (S7-300, S7-400)](#bit-field-for-the-initialization-function-s7-300-s7-400)

#### Function (S7-300, S7-400)

The axis DB is the central database of Easy Motion Control. It contains:

- Parameters that describe the basic axis (for example, I/O addresses)
- Position control parameters that are calculated based on these basic parameters during initialization of the instructions of Easy Motion Control.
- Actual values of the position control (for example, position, error states, etc.).
- Initialization bits for coordinating the start of the instructions

Interaction of these parameter types is ensured if you take one of the following measures:

- Edit and transfer the axis DB using the configuration software.
- After having changed specific parameters, ensure that instruction [MC_Init](Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#mc_init-s7-300-s7-400) is called.

In both cases, the plausibility of the entered parameters is checked wherever possible, and the values internally required by Easy Motion Control are computed.

The configuration software also analyzes the type of changes and uses this information to control the loading processes.

#### Saving and Loading the Axis Data Block (S7-300, S7-400)

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| The entire axis DB can only be overwritten when the axis is at a standstill.  You may **NOT** download the axis DB in RUN mode.  Correct movement of the axis cannot be ensured if you download the axis DB to the module while ignoring the notes in the following sections. |  |

##### Offline

After specific parameters have been changed, all instructions of Easy Motion Control must complete an initialization routine.

These parameters are identified in the description of the axis DB by the following symbol:

![Offline](images/29245571339_DV_resource.Stream@PNG-de-DE.png)

Changing and loading these parameters:

- Is only possible when the axis is at a standstill
- Must include setting the initialization bits (see [Initialization and Parameter Changes](#initialization-and-parameter-changes-s7-300-s7-400)).

##### Online

Transferring parameters that were changed online (for example, the coordinate of the reference point for absolute encoders) to the offline management is not supported.

#### Axis parameters (S7-300, S7-400)

All information on length, velocity, and deceleration provided in the "[Configuring Easy Motion Control](#configuring-easy-motion-control-s7-300-s7-400)" section refers to an arbitrary, yet uniform length unit. All times are specified in seconds.

In the tables of that section, the parameter name from the axis DB is specified in the "Name" column, while the parameter name used in the configuration software is specified in the "Comments" column.

> **Note**
>
> Parameters not listed are reserved for internal use by the Easy Motion Control instructions and must not be altered.

#### Actual values (S7-300, S7-400)

##### Overview

The following parameters in the axis DB show information on the current status of the moving axis. You must not change the contents of these parameters.

##### Actual position value

Displays the actual position value.

| Address | Name | Type | Initial value | Comment |
| --- | --- | --- | --- | --- |
| 104.0 | ActPosition | REAL | 0.0 | **Actual position value**   Range of values: Floating point number [length unit] |

##### Following error

Following error = current position setpoint - actual position value

| Address | Name | Type | Initial value | Comment |
| --- | --- | --- | --- | --- |
| 108.0 | FollowingDistance | INT | 0 | **Following error**   Range of values: Floating point number [length unit] |

##### Residual distance

Indicates the distance remaining to the target position during movements with defined target (MC_MoveAbsolute, MC_MoveRelative).

Travel without target (MC_MoveJog, MC_Home) and errors with hard stop reset the remaining distance to 0.

| Address | Name | Type | Initial value | Comment |
| --- | --- | --- | --- | --- |
| 112.0 | RemainingDistance | REAL | 0.0 | **Distance remaining** to target  Range of values: Floating point number [length unit] |

##### Setpoint velocity

Displays the velocity setpoint of the axis calculated by the travel instruction during a movement.

| Address | Name | Type | Initial value | Comment |
| --- | --- | --- | --- | --- |
| 116.0 | NomVelocity | REAL | 0.0 | **Setpoint velocity**   Range of values: Floating point number [length unit/s] |

##### Actual velocity

The actual velocity of the axis is displayed here.

| Address | Name | Type | Initial value | Comment |
| --- | --- | --- | --- | --- |
| 120.0 | ActVelocity | REAL | 0.0 | **Actual velocity**   Range of values: Floating point number [length unit/s] |

##### Axis synchronized

When using an incremental encoder:

- FALSE: After CPU startup or detection of an encoder error
- TRUE: After a reference point approach or reference setting

When using an absolute encoder:

- FALSE: Before initial reference setting
- TRUE: After reference setting

| Address | Name | Type | Initial value | Comment |
| --- | --- | --- | --- | --- |
| 124.0 | Sync | BOOL | FALSE | **Axis synchronized**   FALSE = Not synchronized  TRUE = Synchronized |

##### Current encoder value

The current encoder value is displayed here.

| Address | Name | Type | Initial value | Comment |
| --- | --- | --- | --- | --- |
| 136.0 | EncoderValue | DINT | L#0 | **Current encoder value**   Range of values: Decimal [steps] |

#### Bit Field for the Initialization Function (S7-300, S7-400)

##### Bit array function

All Easy Motion Control instructions must be initialized after every CPU startup and after specific parameters have been changed.

For this purpose, the "Init.Ix" bit array is defined for initialization in the axis DB and all instructions are assigned the "Init" parameter. The instructions run their initialization routine if their "Init" input is set. On completion, the instructions reset the interconnected initialization bit.

You must interconnect the "Init" parameter with a bit of the bit array at each call of a instruction. This bit may not be used by another instruction (refer to [Initialization and parameter changes](#initialization-and-parameter-changes-s7-300-s7-400)).

Whenever the MC_Init instruction is called, or if you change a parameter in the configuration software, which is not activated unless the instructions have completed their initialization, all bits of this array is set simultaneously to TRUE. This allows all instructions to carry out an initialization with their next call.

| Address | Name | Type | Initial value | Comment |
| --- | --- | --- | --- | --- |
| 278.0 | Init | STRUCT | TRUE | Bit array for initialization of the instructions |

### User Program as a Multi-instance FB (S7-300, S7-400)

If you want to save all parameters of your travel instructions to a single DB, or use the same program for several axes, create the user program in a multi-instance FB.

Place the axis data in this multi-instance DB, as well. To do this, declare a static variable of the type AXIS_REF from the "Easy Motion Control" library in your multi-instance FB.

Interconnect the Axis and Init parameters of the instructions of Easy Motion Control with this variable.

Call instruction MC_Init conditionally as the first instruction in your multi-instance block. This condition must be set in the startup OB (for example, OB100) and reset after instruction MC_Init has been called.

New multi-instance DBs can only be created using the TIA Portal, or the LAD/STL/instructionD Editor.

## Commissioning Easy Motion Control (S7-300, S7-400)

This section contains information on the following topics:

- [Safety Information (S7-300, S7-400)](#safety-information-s7-300-s7-400)
- [Commissioning the axis technology object (S7-300, S7-400)](#commissioning-the-axis-technology-object-s7-300-s7-400)
- [Testing the wiring (S7-300, S7-400)](#testing-the-wiring-s7-300-s7-400)
- [Measuring the axis velocity (S7-300, S7-400)](#measuring-the-axis-velocity-s7-300-s7-400)
- [Set reference point (S7-300, S7-400)](#set-reference-point-s7-300-s7-400)
- [Measuring the axis distance (S7-300, S7-400)](#measuring-the-axis-distance-s7-300-s7-400)
- [Error profiles and remedies during commissioning of the user program (S7-300, S7-400)](#error-profiles-and-remedies-during-commissioning-of-the-user-program-s7-300-s7-400)

### Safety Information (S7-300, S7-400)

#### Introduction

Read the following notes before you start commissioning.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **The commissioning functions result in a movement of the axis.**  Uncontrolled travel motions of the axis during commissioning and operation can cause serious injury and material damage.  To avoid injury to persons and damage to objects, take the following precautions:  - Install an EMERGENCY STOP switch in the vicinity of the computer. This is the only way to ensure that the system is reliably switched off in the event of a hardware or software failure. - Install safety limit switches for direct control of the power units of all drives. - Ensure that nobody has access to the area of the system where there are moving parts. |  |

### Commissioning the axis technology object (S7-300, S7-400)

The commissioning editor helps you with commissioning and the function test for the axis technology object. You can run the following tests and measurements:

- [Wiring test](#testing-the-wiring-s7-300-s7-400)
- [Velocity measurement](#measuring-the-axis-velocity-s7-300-s7-400)
- [Homing the axis](#set-reference-point-s7-300-s7-400)
- [Distance measurement](#measuring-the-axis-distance-s7-300-s7-400)

#### Procedure

To open the commissioning editor of the axis technology object, follow these steps:

1. Open the "Technology objects" folder in the project tree.
2. Open the corresponding instance of the AXIS_REF technology object (e.g. EMC_AXIS_1) in the project tree.
3. Double-click on the "Commissioning" object.

#### Remedy in the case of errors

If errors occur during commissioning, you will find information about possible remedies in section [Error profiles and remedies during commissioning of the user program](#error-profiles-and-remedies-during-commissioning-of-the-user-program-s7-300-s7-400).

#### Additional information

The corresponding tooltips include detailed information on the parameters and buttons of the commissioning user interfaces.

### Testing the wiring (S7-300, S7-400)

The Wiring test is used to determine the direction of rotation of the axis.

#### Procedure

To perform the Wiring test, follow these steps:

1. Click on "Wiring test" in the configuration view.
2. Click the "Activate" button.  
   A query regarding activation of manual control is displayed.
3. Click "OK".  
   An online connection is created between STEP 7 (TIA Portal) and the CPU.
4. Enter a velocity as a percentage of the maximum velocity in the "Specified velocity" entry field.
5. Enter a value in the "Ramp-up time" entry field.
6. Make sure that the start position permits a movement of the axis in both directions.
7. Click the "Jog backwards" or "Jog forwards" button to move the axis.
8. In "Result", specify whether the axis has moved in the requested direction.
9. If you have selected "Yes" as the result, click "OK" in the window that appears.
10. If you have selected "No" as the result, click "Yes" in the window that appears.  
    The parameters "Encoder polarity" and "Drive polarity" are changed.

### Measuring the axis velocity (S7-300, S7-400)

The velocity measurement determines the maximum axis velocity.

#### Procedure

To perform velocity measurement, follow these steps:

1. Click on "Velocity measurement" in the configuration view.
2. Click the "Activate" button.  
   A query regarding activation of manual control is displayed.
3. Click "OK".  
   An online connection is created between STEP 7 (TIA Portal) and the CPU.
4. Enter a velocity as a percentage of the maximum velocity in the "Specified velocity" entry field.
5. Enter a value in the "Ramp-up time" entry field.
6. Make sure that the start position permits a sufficiently long travel distance in at least one direction.
7. Click the "Jog backwards" or "Jog forwards" button and hold it until the value in the "Actual output" output field has reached the "Setpoint output".

   Easy Motion Control calculates the maximum axis velocity and displays it in the "Determined value" output field.
8. If you want to save the calculated axis velocity in the project, click the "Apply" button.

   The calculated value overwrites the "Maximum velocity" in the online/offline data management of the technology object.

### Set reference point (S7-300, S7-400)

A reference point is set for absolute encoders, and this is referred to as absolute encoder adjustment in this case.

#### Procedure

To set a reference point for an absolute encoder, proceed as follows:

1. Click on "Homing the axis" in the configuration view.
2. Click the "Activate" button.  
   A query regarding activation of manual control is displayed.
3. Click "OK".  
   An online connection is created between STEP 7 (TIA Portal) and the CPU.
4. Enter a velocity as a percentage of the maximum velocity in the "Specified velocity" entry field.
5. Enter a value in the "Ramp-up time" entry field.
6. Click the "Jog backwards" or "Jog forwards" button until the axis has traveled to the reference point.  
   Alternatively:  
   Move the axis to the reference point manually.
7. In the "Input of reference position" input field, enter a position value as reference value.  
   The offset between the reference position and the physical axis position is determined and saved in the axis DB.
8. In the window that appears, confirm whether you wish to save the offset for the absolute encoder adjustment in the offline data management of the technology object.

> **Note**
>
> If you replace the absolute encoder, you will have to set the reference point again.

### Measuring the axis distance (S7-300, S7-400)

The distance measurement determines the axis distance per encoder revolution.

#### Procedure

Proceed as follows to perform the distance measurement:

1. Click on "Distance measurement" in the configuration view.
2. Click the "Activate" button.  
   A query regarding activation of manual control is displayed.
3. Click "OK".  
   An online connection is created between STEP 7 (TIA Portal) and the CPU.
4. Enter a velocity as a percentage of the maximum velocity in the "Specified velocity" entry field.
5. Enter a value in the "Ramp-up time" entry field.
6. Click the "Jog backwards" or "Jog forwards" button until the axis has traveled to the start position.  
   Alternatively:  
   Move the axis to the start position manually.
7. Enter a position value as the start position in the "Input of start position" entry field.
8. Click the "Jog backwards" or "Jog forwards" button until the axis has traveled to the end position.  
   Alternatively:  
   Move the axis to the end position manually.
9. Enter a position value as the end position in the "Input of end position" entry field.

   Easy Motion Control calculates the axis distance per encoder revolution and displays it in the output field "Determined value".
10. If you want to save the calculated axis distance per encoder revolution in the project, click "Apply".

    The calculated value is entered in the online/offline data management of the technology object.

### Error profiles and remedies during commissioning of the user program (S7-300, S7-400)

This section contains information on the following topics:

- [Axis does not Move Despite Travel Order (S7-300, S7-400)](#axis-does-not-move-despite-travel-order-s7-300-s7-400)
- [Axis Moves without Travel Order (S7-300, S7-400)](#axis-moves-without-travel-order-s7-300-s7-400)
- [Axis Velocity Other than Expected or Axis Oscillates (S7-300, S7-400)](#axis-velocity-other-than-expected-or-axis-oscillates-s7-300-s7-400)
- [Positioning Not Accurate Enough (S7-300, S7-400)](#positioning-not-accurate-enough-s7-300-s7-400)
- [Maximum Following Distance Exceeded (S7-300, S7-400)](#maximum-following-distance-exceeded-s7-300-s7-400)
- [The MC_GearIn instruction displays neither "InGear" nor "Coupled" (S7-300, S7-400)](#the-mc_gearin-instruction-displays-neither-ingear-nor-coupled-s7-300-s7-400)
- [MC_GearIn instruction displays "InGear", but not "Coupled" (S7-300, S7-400)](#mc_gearin-instruction-displays-ingear-but-not-coupled-s7-300-s7-400)

#### Axis does not Move Despite Travel Order (S7-300, S7-400)

If the axis is not moving irrespective of a pending travel command, check the following conditions:

| Error | Remedies |
| --- | --- |
| Wiring of the drive is faulty | - Check whether the "DriveEnabled" output of the MC_Control instruction is continuously interconnected with the enable input of the power unit. - Check whether the "DriveEnabled" output of the MC_Control instruction is interconnected with the "EnableDrive" input of the output driver. |
| I/O addresses or channel numbers are incorrect | Set the correct I/O addresses and channel numbers:  In the axis DB, the **start** addresses of the modules are expected. From the start address and channel number (counting method: from channel 0), the driver blocks calculate the module-specific I/O addresses for setpoint and actual values. |
| Simulation mode switched on | Switch off simulation mode ("Sim" = FALSE).  If the simulation mode is switched on ("Sim" = TRUE), **no** I/O values are read or written. |
| Manual mode switched on with missing setpoint velocity | If manual mode is switched on ("ManEnable" = TRUE), specify a "manual setpoint velocity" ("ManVelocity" &lt;&gt; 0.0 [length unit/s]). |
| Drive enable not set | Set the "EnableDrive" input of the MC_Control instruction to TRUE. |
| Axis error pending | If the "group error" bit ("Error") is set in the axis DB, the type of axis error is visible in the bit arrays for the error display:  - After the MC_Init instruction is called, the "Stop status requiring acknowledgment" error is always set ("Err.StoppedMotion"). Acknowledge the error by setting the "Group acknowledgment" "ErrorAck" = TRUE. - After you have rectified incorrect values in the case of a parameter assignment error, you need to restart MC_Init. - In the case of an encoder error, check whether the position input module is fully configured (with the help of the module configuration software, if necessary). - Other errors: Remedy and acknowledge the error by setting the "Group acknowledgment" "ErrorAck" = TRUE. |
| "Group acknowledgment" is not reset | If a "Group acknowledgment" ("ErrorAck") you have set is not detected and reset by Easy Motion Control , then:  - Prevent the Easy Motion Control instructions from remaining in their initialization branch due to the constant call of the MC_Init instruction. - Check whether the position decoder module responds to the error acknowledgment. |
| "Velocity override" not 0% | Configure the "Velocity override" = 0% ("Override"). |
| Travel command not processed by program | Set the parameter "Busy" = TRUE in the travel instruction. |
| "Parameter of travel instruction inadmissible" ("Err.DataErr") or "Target outside travel range" ("Err.TargetErr") | If you download the axis DB to the CPU without using the Easy Motion Control configuration software, you must subsequently call the MC_Init instruction. MC_Init stores the auxiliary values in the axis DB. |

#### Axis Moves without Travel Order (S7-300, S7-400)

Possible causes of axis movement without a travel command are:

| Error | Causes | Remedies |
| --- | --- | --- |
| The axis starts moving very quickly. | The direction of control action has been set incorrectly. | Adjust the "Encoder polarity" ("PolarityEncoder") and "Drive polarity" ("PolarityDrive") parameters with the help of the "Wiring test" wizard. In this way, you adapt the instructions to your hardware installation. |
| The axis is drifting slowly. | The power unit of the drive is enabled and the axis is **not** in control (MC_Control instruction outputs "DriveEnabled" = FALSE). | — |
| The analog output is not correctly wired with the power unit of the drive. | Correct the wiring between the analog output and the power unit of the drive. |  |
| Either the input driver or the output driver is not accessing the modules belonging to the drive because the module address or the channel number in the axis DB is set incorrectly. | Adjust the parameters with the help of the "wiring test" wizard. |  |

#### Axis Velocity Other than Expected or Axis Oscillates (S7-300, S7-400)

##### Are the parameters describing the axis correct?

There are certain relations between these parameters as shown in the following example.

- "Controller gain" ("FactorP"):

  The axis may oscillate if the selected "Controller gain" ("FactorP") factor is too high.
- "Maximum axis velocity" ("MaxVelocity")
- "Reference value for maximum axis velocity" ("DriveInputAtMaxVel"):

  **Example** of a ±10 V control:

  ![Are the parameters describing the axis correct?](images/52873533579_DV_resource.Stream@PNG-en-US.png)

  The following relationship holds:

  With an output voltage of 9 V at the output module, the drive rotates at a speed of 3000 rpm. This speed is proportional to a spindle speed of 300 rpm or 5 rps and the slide moves by a distance of 10 mm per spindle revolution. The maximum velocity of the slide is thus 10 mm/s • 300 U/min = 50 mm/s.

  In other words, set:

  - "Maximum axis velocity" = 50 mm/s and "Reference value for maximum axis velocity" = 9 V.
- "Steps per encoder revolution" ("StepsPerRev"):

  You can check whether the number of steps produced by the encoder coincides with the configured value by observing the parameter "Encoder value" with the configuration software, while you turn the **encoder once** by hand.

  **Example**: The "encoder value" changes by 4096 steps per spindle revolution.
- "Axis distance per encoder revolution" ("DisplacementPerRev"):

  This parameter assigns a specific distance to one revolution of the encoder. You can check whether this is correct by observing the parameter "Actual position" with the configuration software, while you turn the **encoder once** by hand.

  **Example**: The "actual position" changes by 10 mm per spindle revolution.
- "Scan time" ("Sample_T"):

  Scan time is used together with the distance covered since the last scan in order to calculate axis velocity The time must correspond to the call time of the OB in which the instructions of Easy Motion Control are called.

  "Sample_T" must be entered with the second unit in the axis DB.

#### Positioning Not Accurate Enough (S7-300, S7-400)

If positioning lacks precision:

- Check the settings in the "Steps per encoder revolution" parameter ("StepsPerRev").
- Calculate the "Axis distance per encoder revolution" parameter ("DisplacementPerRev") with maximum possible precision ("Distance measurement" wizard).

---

**See also**

[Measuring the axis distance (S7-300, S7-400)](#measuring-the-axis-distance-s7-300-s7-400)

#### Maximum Following Distance Exceeded (S7-300, S7-400)

Overshoot of the maximum following error has different causes:

- In order for the "maximum axis velocity" ("MaxVelocity") to be reached at all, the following rules must apply:

  ![Figure](images/29704034955_DV_resource.Stream@PNG-de-DE.png)
- The configured acceleration cannot be reached by the real axis.
- Incorrect settings for the "Maximum axis velocity" ("MaxVelocity") and "Reference value for maximum axis velocity" ("DriveInputAtMaxVel") parameters, or of the "Reference value for 100 % speed" ("DriveInputAt100") (refer to [Axis velocity not as expected, or axis oscillates](#axis-velocity-other-than-expected-or-axis-oscillates-s7-300-s7-400)).

#### The MC_GearIn instruction displays neither "InGear" nor "Coupled" (S7-300, S7-400)

The following causes prevent the MC_GearIn instruction from displaying "InGear" or "Coupled":

- The slave axis is about to couple to a moving master axis without having (yet) reached the gear speed.
- The slave axis has released the coupling due to an error.

#### MC_GearIn instruction displays "InGear", but not "Coupled" (S7-300, S7-400)

instruction MC_GearIn displays "InGear", but not "Coupled" due to the following causes:

- The slave axis may have reached the gear speed for (possibly only for one cycle), but has lost this speed:

  - The acceleration or deceleration of the master axis exceeds the capability of the slave axis based on its configuration and the gear ratio.
  - The slave axis cannot reach the velocity that is determined by the velocity setpoint of the master axis and by the gear ratio.

## Diagnostics (S7-300, S7-400)

This section contains information on the following topics:

- [Error Displays and Error Acknowledgement in the Axis DB (S7-300, S7-400)](#error-displays-and-error-acknowledgement-in-the-axis-db-s7-300-s7-400)
- [Axis error (S7-300, S7-400)](#axis-error-s7-300-s7-400)
- [Parameter errors (S7-300, S7-400)](#parameter-errors-s7-300-s7-400)
- [JOB_ERR interrupts (S7-300, S7-400)](#job_err-interrupts-s7-300-s7-400)

### Error Displays and Error Acknowledgement in the Axis DB (S7-300, S7-400)

#### Error displays and error acknowledgment

All errors detected by the instructions are displayed in the axis DB as follows:

- By setting the group error "Error"
- By means of error-specific display "Err.xxxx"

With errors requiring acknowledgment, an error acknowledgment must be set after the error has been eliminated (parameter "ErrorAck" in the axis DB; see below).

There are three types of errors with different error responses:

- Errors where perfect functioning of position control is **no longer** guaranteed lead to a **hard stop**:

  instruction MC_Control brings the axis to a standstill along the deceleration ramp stored in "EmergencyDec". instruction MC_Control will then reset its "DriveEnabled" to "0".

  Once the error has been eliminated, set the error acknowledgment in the axis DB. "DriveEnabled" is then set again.
- Errors where position control still functions lead to a **soft stop**:

  The axis is slowed down at the deceleration that is configured in the active travel instruction. The axis retains controlled operation and "DriveEnabled" is **not** reset.

  In this situation, the movement can only be overridden by means of MC_StopMotion.

  Once the error has been eliminated, set the error acknowledgment in the axis DB.
- Error in the axis parameters (**parameter error**):

  instruction MC_Init checks the parameter entered in the Axis Db as far as possible. In the event of an error, it sets "Err.ConfigErr" bit and enters the precise cause of error in "Config.Err_xxx".

  Parameter errors **cannot** be rectified by acknowledgment. Approach of the axis is prevented. After having corrected the invalid parameter entry, you must once again call instruction MC_Init. Parameter error displays are then reset once there is no longer any error.

> **Note**
>
> **The following applies to errors with hard and soft stop:**
>
> No travel order is possible as long as one or several unacknowledged errors are pending.
>
> Exception:
>
> If the axis only overshoots a software limit switch, a travel order for reversing the movement is possible. This error is automatically acknowledged once the axis has cleared the software limit switch.

> **Note**
>
> If a travel block (for example, MC_MoveJog, or MC_MoveAbsolute) has detected the error, the "Error" output is set at the corresponding instruction.
>
> If a driver instruction has detected the error, the precise cause of error is indicated at this instruction (see [Input drivers](Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#input-driver-s7-300-s7-400)).

#### Error display in the axis DB

The group error is TRUE as long as there is at least one error.

| Address | Name | Type | Initial value | Comment |
| --- | --- | --- | --- | --- |
| 124.1 | Error | BOOL | TRUE | **Group error**   FALSE = No error  TRUE = Group error |

#### Error acknowledgment in the axis DB

When group acknowledgment is set, all acknowledgeable error displays are deleted.

Group acknowledgment is only effective when the axis is at a standstill and after initialization.

On completion of the evaluation of error acknowledgment, "ErrorAck" is reset automatically.

| Address | Name | Type | Initial value | Comment |
| --- | --- | --- | --- | --- |
| 124.2 | ErrorAck | BOOL | FALSE | **Group acknowledgment** for all errors  FALSE = No acknowledgment  TRUE = Acknowledge error |

### Axis error (S7-300, S7-400)

This section contains information on the following topics:

- [Error with soft stop (S7-300, S7-400)](#error-with-soft-stop-s7-300-s7-400)
- [Error with hard stop (S7-300, S7-400)](#error-with-hard-stop-s7-300-s7-400)

#### Error with soft stop (S7-300, S7-400)

##### Description

The following rules apply to the errors described below: TRUE = Error is pending.

Errors requiring acknowledgment are identified by the following symbol:

![Description](images/29705308043_DV_resource.Stream@PNG-de-DE.png)

The following table lists all errors with soft stop.

| Address | Name:  Err.xxx | Description |  | ![Description](images/29705308043_DV_resource.Stream@PNG-de-DE.png) |
| --- | --- | --- | --- | --- |
| 128.0 | SWLimitMinExceeded | **Software limit switch start exceeded** |  | — |
| Cause: | - The actual position value is outside the working range. - Replacement of the absolute encoder. |  |  |  |
| Remedy: | - Move the axis out of the range of the limit switch. - Deactivate the software limit switch  ("SWLimitEnable" = FALSE), synchronize the axis and then reactivate the software limit switch. |  |  |  |
| 128.1 | SWLimitMaxExceeded | **Software limit switch end exceeded** |  | — |
| Cause: | - The actual position value is outside the working range. - Replacement of the absolute encoder. |  |  |  |
| Remedy: | - Move the axis out of the range of the limit switch. - Deactivate the software limit switch  ("SWLimitEnable" = FALSE), synchronize the axis and the reactivate the software limit switch. |  |  |  |
| 128.2 | TargetErr | **Target outside of travel range** |  | ![Description](images/29705308043_DV_resource.Stream@PNG-de-DE.png) |
| Cause: | - **MC_MoveAbsolute**:   - The target is in the range of a software limit switch.   - The target is &lt; "Rotary axis start", or ≥ "Rotary axis end".   - The calculated traversing distance is greater than the distance that is equivalent to 2<sup>24</sup> steps of your encoder.   - Auxiliary variables were not calculated in the axis DB, because instruction MC_Init was not called. - **MC_MoveRelative**:   - The travel distance entered leads to a target on a software limit switch.   - The specified travel distance is greater than the distance that is equivalent to 2<sup>24</sup> steps of your encoder.   - Auxiliary variables were not calculated in the axis DB, because instruction MC_Init was not called. - **MC_Home**:   - The reference point coordinate is in the range of a software limit switch.   - The reference point coordinate is &lt; "Rotary axis start", or ≥ "Rotary axis end".   - Auxiliary variables were not calculated in the axis DB, because instruction MC_Init was not called. |  |  |  |
| Remedy: | - Correct the parameters. - Call the MC_Init instruction. |  |  |  |
| 128.3 | NoSync | **Axis not synchronized** |  | ![Description](images/29705308043_DV_resource.Stream@PNG-de-DE.png) |
| Cause: | instruction MC_MoveAbsolute was started with unsynchronized axis. |  |  |  |
| Remedy: | Synchronize the axis (reference point approach, reference setting). |  |  |  |
| 128.4 | DirectionErr | **Invalid travel direction entered** |  | ![Description](images/29705308043_DV_resource.Stream@PNG-de-DE.png) |
| Cause: | Further movement into the range of a software limit switch is not allowed. |  |  |  |
| Remedy: | Start a travel order that moves the axis out of the range of the software limit switch. |  |  |  |
| 128.5 | DataErr | **Invalid parameter in travel instruction** |  | ![Description](images/29705308043_DV_resource.Stream@PNG-de-DE.png) |
| Cause: | **MC_MoveHome**:  - "Velocity" &lt; 0 - "Velocity" &gt; 0 and "Acceleration" ≤ 0 - "Velocity" &gt; 0 and "Deceleration" ≤ 0 - "Velocity" &gt; 0 with absolute encoder - "Position" lies outside the numerical range on a linear axis. - Auxiliary variables were not calculated in the axis DB, because instruction MC_Init was not called.      **MC_MoveAbsolute**, **MC_MoveRelative** and **MC_MoveJog**:  - "Velocity" ≤ 0 - "Acceleration" ≤ 0 - "Deceleration" ≤ 0 - The entered or calculated target coordinate is outside the numerical range (for MC_MoveAbsolute and MC_MoveRelative). - Gear ratio denominator (RatioDenominator") ≤ 0 (MC_GearIn) - Gear ratio numerator ("RatioNumerator") = 0 (MC_GearIn) - A travel instruction was canceled and "Deceleration" of the overriding instruction is inconsistent with the deceleration configured at the canceled instruction (see [Overriding a movement](#overriding-travel-s7-300-s7-400)). - Auxiliary variables were not calculated in the axis DB, because instruction MC_Init was not called. |  |  |  |
| Remedy: | - Specify admissible values. - Initialize the instructions. - Call the MC_Init instruction. |  |  |  |
| 128.6 | StartErr | **Start from current axis status not possible** |  | ![Description](images/29705308043_DV_resource.Stream@PNG-de-DE.png) |
| Cause: | - In a travel order, or at MC_StopMotion, the Execute input was set while the axis was in error state or manual mode ("ManEnable" = TRUE), or while a MC_StopMotion instruction was active. - instruction MC_Home was not started while the axis was at a standstill. - Both directions are set in instruction MC_MoveJog. - Invalid status at the leading axis for instruction MC_GearIn:   - Error with hard stop   - MC_Home is active   - Manual mode ("ManEnable" = TRUE) |  |  |  |
| Remedy: | - Eliminate any errors. - Make sure that the master axis is in a permitted state. |  |  |  |
| 128.7 | DistanceErr | **Overtravel** |  | ![Description](images/29705308043_DV_resource.Stream@PNG-de-DE.png) |
| Cause: | A movement without target (MC_Home, MC_MoveJog, MC_GearIn) has covered a distance that is equivalent to more than 2<sup>24</sup> encoder steps. The axis is braked at about this point.   A MC_MoveJog or MC_GearIn instruction has decelerated a synchronized linear axis onto a software limit switch. Moreover, "SWLimitMinExceeded" or "SWLimitMaxExceeded" is set as well in most cases. |  |  |  |
| Remedy: | Make sure the travel distance does not exceed the limit specified above (see [Maximum Travel Distance](#sequence-of-travel-movements-s7-300-s7-400)). |  |  |  |
| 129.0 | MasterErr | **Master axis in invalid state** |  | ![Description](images/29705308043_DV_resource.Stream@PNG-de-DE.png) |
| Cause: | The master axis was set to an invalid state during gear coupling:  - Error with hard stop - MC_Home is active - Manual mode ("ManEnable" = TRUE) |  |  |  |
| Remedy: | Correct the invalid state of the master axis. |  |  |  |

#### Error with hard stop (S7-300, S7-400)

##### Description

The following rules apply to the errors described below: TRUE = Error is pending.

Errors requiring acknowledgment are identified by the following symbol:

![Description](images/29705308043_DV_resource.Stream@PNG-de-DE.png)

The following table lists all errors with hard stop.

| Address | Name: Err.xxx | Description |  | ![Description](images/29705308043_DV_resource.Stream@PNG-de-DE.png) |
| --- | --- | --- | --- | --- |
| 130.0 | StoppedMotion | **Axis is in stop state requiring acknowledgment** |  | ![Description](images/29705308043_DV_resource.Stream@PNG-de-DE.png) |
| Cause: | The axis is in a stop state requiring acknowledgment:  - After initialization by calling instruction MC_Init - As the result of an error listed in this table |  |  |  |
| Remedy: | Rectify any errors that might possibly be present. |  |  |  |
| 130.1 | EnableDriveErr | **Drive enable missing** |  | ![Description](images/29705308043_DV_resource.Stream@PNG-de-DE.png) |
| Cause: | "EnableDrive" is not set at instruction MC_Control. |  |  |  |
| Remedy: | Set "EnableDrive". |  |  |  |
| 130.2 | FollowingDistErr | **Following error exceeded** |  | ![Description](images/29705308043_DV_resource.Stream@PNG-de-DE.png) |
| Cause: | The axis is not following the setpoints or is too slow in following. |  |  |  |
| Remedy: | - Switch on the drive. - Optimize "Controller gain" ([Axis DB address 44.0](#specifying-controller-gain-s7-300-s7-400)). - Adjust "Set encoder polarity" ([Axis DB address 74.0](#selecting-the-encoder-polarity-s7-300-s7-400)) to "Set drive polarity" ([Axis DB address 86.0](#selecting-the-drive-polarity-s7-300-s7-400)). - Increase the valid maximum following error ([Axis DB address 38.0](#specifying-the-valid-maximum-following-error-s7-300-s7-400)). |  |  |  |
| 130.3 | StandstillErr | **Outside standstill range** |  | ![Description](images/29705308043_DV_resource.Stream@PNG-de-DE.png) |
| Cause: | - The axis has moved out of "Standstill range" without a travel order. - "Standstill range" is less than "Target range". - "Set encoder polarity" or "Set drive polarity" is incorrectly configured. |  |  |  |
| Remedy: | - Check the connection to the setpoint input of the power unit. - Adjust the parameters "Standstill range"/"Target range" parameters ([Axis DB address 34.0](#specifying-the-standstill-range-s7-300-s7-400) / [30.0](#specifying-the-target-range-s7-300-s7-400)) - During first commissioning: Test the wiring ([Axis DB address 74.0](#selecting-the-encoder-polarity-s7-300-s7-400) / [86.0](#selecting-the-drive-polarity-s7-300-s7-400)). |  |  |  |
| 130.4 | TargetApproachErr | **Error on target approach** |  | ![Description](images/29705308043_DV_resource.Stream@PNG-de-DE.png) |
| Cause: | The actual value has not reached the "Target range" within the "Monitoring time for target approach". |  |  |  |
| Remedy: | - Optimize the "target range" and "Monitoring time for target approach" ([Axis DB address 30.0](#specifying-the-target-range-s7-300-s7-400) / [26.0](#specifying-the-monitoring-time-for-target-approach-s7-300-s7-400)). - Check the drive and axis. |  |  |  |
| 130.5 | EncoderErr | **Encoder error** |  | ![Description](images/29705308043_DV_resource.Stream@PNG-de-DE.png) |
| Cause: | - The input driver has detected an encoder error. The instance DB of the driver DB indicates the precise cause of error. See [Input drivers](Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#input-driver-s7-300-s7-400). - Input "EncErr" was set at the input driver (see [Input drivers](Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#input-driver-s7-300-s7-400), error handling section). |  |  |  |
| Remedy: | Eliminate the cause of the error. |  |  |  |
| 130.6 | OutputErr | **Error at output driver** |  | ![Description](images/29705308043_DV_resource.Stream@PNG-de-DE.png) |
| Cause: | Input "OutErr" was set at the output driver (see [Output drivers](Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#output-driver-s7-300-s7-400), error handling section). |  |  |  |
| Remedy: | Eliminate the cause of the error. |  |  |  |
| 130.7 | ConfigErr | **Group error: Axis data incorrectly configured** |  | **Acknowledgment not possible** |
| Cause: | The parameters in the axis DB are defective. For exact cause of error, see [Parameter errors](#parameter-errors-s7-300-s7-400). |  |  |  |
| Remedy: | Adjust the faulty parameter and make sure that instruction MC_Init is called. |  |  |  |
| 131.0 | DriveErr | **Drive error** |  | **Acknowledgment not possible** |
| Cause: | The output driver has detected an error at the power unit / drive. The instance DB of the driver DB indicates the precise cause of error. See [Output drivers](Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#output-driver-s7-300-s7-400). |  |  |  |
| Remedy: | Eliminate the cause of the error. |  |  |  |

### Parameter errors (S7-300, S7-400)

#### Parameter error

The following table shows the parameter errors that are likely to occur in Easy Motion Control.

The "Address" column contains the address of the error display in the axis DB. The "Parameter address" column points to the address of the faulty parameter in the axis DB (see [Structure of the axis data block](Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#axis-data-block-axis-db-s7-300-s7-400)).

| Address | Name Config.xxx | Parameter error | Parameter address |
| --- | --- | --- | --- |
| 132.0 | Err_AxisLimit | "Software limit switch start" &lt; -2<sup>24 </sup>+6 [length unit]  "Software limit switch end" &gt; +2<sup>24</sup>-6 [length unit]  "Software limit switch end" ≤ "Software limit switch start" | [6.0](#specifying-software-limit-switches-s7-300-s7-400) , [10.0](#specifying-software-limit-switches-s7-300-s7-400) |
| 132.1 | Err_MaxVelocity | "Maximum axis velocity" ≤ 0.0 [length unit/s] | [14.0](#specifying-the-maximum-axis-velocity-s7-300-s7-400) |
| 132.2 | Err_MaxAcceleration | "Maximum acceleration" ≤ 0.0 [length unit/s<sup>2</sup>] | [18.0](#specifying-the-maximum-axis-velocity-s7-300-s7-400-1) |
| 132.3 | Err_MaxDeceleration | "Maximum deceleration" ≤ 0.0 [length unit/s<sup>2</sup>] | [22.0](#specifying-maximum-axis-deceleration-s7-300-s7-400) |
| 132.4 | Err_MonTimeTargetAppr | "Monitoring time for target approach" ≤ 0.0 [s] | [26.0](#specifying-the-monitoring-time-for-target-approach-s7-300-s7-400) |
| 132.5 | Err_TargetRange | "Target range" ≤ 0.0 [length unit] | [30.0](#specifying-the-target-range-s7-300-s7-400) |
| 132.6 | Err_StandstillRange | "Standstill range" ≤ 0.0 [length unit] | [34.0](#specifying-the-standstill-range-s7-300-s7-400) |
| 132.7 | Err_MaxFollowingDist | "Maximum permitted following distance" ≤ 0.0 [length unit] | [38.0](#specifying-the-valid-maximum-following-error-s7-300-s7-400) |
| 133.0 | Err_EmergencyDec | "Deceleration for hard stop" ≤ 0.0 [length unit/s<sup>2</sup>] | [54.0](#specifying-emergency-stop-deceleration-s7-300-s7-400) |
| 133.1 | Err_StepsPerRev | "Steps per encoder revolution" &lt; 1 | [64.0](#specifying-the-steps-per-encoder-revolution-s7-300-s7-400) |
| 133.2 | Err_DisplacementPerRev | "Axis distance per encoder revolution" ≤ 0.0 [length unit] | [68.0](#specifying-the-axis-distance-per-encoder-revolution-s7-300-s7-400) |
| 133.3 | Err_NumberRevs | "Number of encoder revolutions" &lt; 1 for absolute encoder | [72.0](#specifying-the-number-of-encoder-revolutions-s7-300-s7-400) |
| 133.4 | Err_PolarityEncoder | "Encoder polarity" not equal to ±1 | [74.0](#selecting-the-encoder-polarity-s7-300-s7-400) |
| 133.5 | Err_PolarityDrive | "Drive polarity" not equal to ±1 | [86.0](#selecting-the-drive-polarity-s7-300-s7-400) |
| 133.6 | Err_DriveInputAtMaxVel | "Reference value for maximum axis velocity" ≤ 0.0, or &gt; "DriveInputAt100" | [88.0](#specifying-the-reference-value-for-maximum-axis-velocity-s7-300-s7-400) , [96.0](#reference-value-for-100-speed-s7-300-s7-400) |
| 133.7 | Err_AxisLength | Axis length &gt; 2<sup>24</sup> [length unit], or  axis length &gt; (2<sup>31 </sup>-1) [steps] | [6.0](#specifying-software-limit-switches-s7-300-s7-400) , [10.0](#specifying-software-limit-switches-s7-300-s7-400) |
| 134.0 | Err_EncoderRange | Encoder range does not match axis length  (see "Axis Distance per Encoder Revolution", [Axis DB address 68.0](#specifying-the-axis-distance-per-encoder-revolution-s7-300-s7-400)) | [6.0](#specifying-software-limit-switches-s7-300-s7-400) , [10.0](#specifying-software-limit-switches-s7-300-s7-400) ,  [68.0](#specifying-the-axis-distance-per-encoder-revolution-s7-300-s7-400) , [72.0](#specifying-the-number-of-encoder-revolutions-s7-300-s7-400) |
| 134.1 | Err_MaxVelRotaryAxis | Maximum velocity and scan time do not match rotary axis length  (see "Maximum axis velocity" [Axis DB address 14.0](#specifying-the-maximum-axis-velocity-s7-300-s7-400)) | [14.0](#specifying-the-maximum-axis-velocity-s7-300-s7-400) , [0.0](#specifying-the-scan-time-s7-300-s7-400) ,  [68.0](#specifying-the-axis-distance-per-encoder-revolution-s7-300-s7-400) , [72.0](#specifying-the-number-of-encoder-revolutions-s7-300-s7-400) |
| 134.2 | Err_DriveInputAt100 | "Reference value for 100 % speed" ≤ 0 | [96.0](#reference-value-for-100-speed-s7-300-s7-400) |

### JOB_ERR interrupts (S7-300, S7-400)

#### JOB_ERR interrupts

| JOB_ERR  (Hex) | JOB_ERR  (Dec) | JOB_ERR  (Int) | Meaning |
| --- | --- | --- | --- |
| 80A0 | 32928 | -32608 | Negative acknowledgment on reading from module. Module removed during reading process or module defective |
| 80A1 | 32929 | -32607 | Negative acknowledgment on writing to module. Module removed during write process or module defective |
| 80A2 <sup>1)</sup> | 32930 | -32606 | Protocol error at layer 2 |
| 80A3 <sup>1)</sup> | 32931 | -32605 | Protocol error at user interface / user |
| 80A4 <sup>1)</sup> | 32932 | -32604 | Communication faulty at K-bus |
| 80B0 | 32944 | -32592 | Data record / order unknown |
| 80B1 | 32945 | -32591 | Length data incorrect. FM_TYPE parameter in the channel DB is not correctly set for the module being used. |
| 80B2 | 32946 | -32590 | Configured slot is not assigned. |
| 80B3 | 32947 | -32589 | Actual module type not same as setpoint module type. |
| 80C0 <sup>1)</sup> | 32960 | -32576 | Module has not yet prepared the data to be read. |
| 80C1 <sup>1)</sup> | 32961 | -32575 | Data of a similar write order has not yet been processed on the module. |
| 80C2 <sup>1)</sup> | 32962 | -32574 | Module is currently processing the maximum possible number of orders. |
| 80C3 <sup>1)</sup> | 32963 | -32573 | Required resources (memory, etc.) are currently occupied. |
| 80C4 <sup>1)</sup> | 32964 | -32572 | Communication error |
| 80C5 <sup>1)</sup> | 32965 | -32571 | Distributed I/O not available. |
| 80C6 <sup>1)</sup> | 32966 | -32570 | Priority class aborted (restart or background) |
| 8522 | 34082 | -31454 | Channel DB or parameter DB too short. Data cannot be read from the DB (write order). |
| 8532 | 34098 | -31438 | DB number of parameter DB too high (write order) |
| 853A | 34106 | -31430 | Parameter DB not available (write order). |
| 8544 | 34116 | -31420 | Error at nth (n &gt; 1) read access to a DB after an error has occurred (write order). |
| 8723 | 34595 | -30941 | Channel DB or parameter DB too short. Data cannot be written to the DB (read order). |
| 8730 | 34608 | -30928 | Parameter DB in CPU is write-protected. Data cannot be written to the DB (read order). |
| 8732 | 34610 | -30926 | DB number of parameter DB too high (read order). |
| 873A | 34618 | -30918 | Parameter DB not available (read order). |
| 8745 | 34629 | -30907 | Error at nth (n &gt; 1) write access to a DB after an error has occurred (read order). |
| 1) Errors 80A2 to 80A4 and 80Cx are temporary, i.e., they can be rectified automatically after a waiting time. |  |  |  |

---
title: "Motion Control OBs (S7-1500, S7-1500T)"
package: Prog15MCOBenUS
topics: 9
devices: [S7-1500, S7-1500T]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Motion Control OBs (S7-1500, S7-1500T)

This section contains information on the following topics:

- [MC_Servo OB (S7-1500, S7-1500T)](#mc_servo-ob-s7-1500-s7-1500t)
- [Configuring MC_Servo OB (S7-1500, S7-1500T)](#configuring-mc_servo-ob-s7-1500-s7-1500t)
- [MC_PreServo OB (S7-1500, S7-1500T)](#mc_preservo-ob-s7-1500-s7-1500t)
- [MC_PostServo OB (S7-1500, S7-1500T)](#mc_postservo-ob-s7-1500-s7-1500t)
- [MC_Interpolator OB (S7-1500, S7-1500T)](#mc_interpolator-ob-s7-1500-s7-1500t)
- [MC_PreInterpolator OB (S7-1500, S7-1500T)](#mc_preinterpolator-ob-s7-1500-s7-1500t)
- [MC_Transformation OB (S7-1500T)](#mc_transformation-ob-s7-1500t)
- [MC_LookAhead OB (S7-1500T)](#mc_lookahead-ob-s7-1500t)

## MC_Servo OB (S7-1500, S7-1500T)

### Description

When you create a technology object for S7-1500 Motion Control, the organization block MC_Servo [OB91] for processing the technology objects is created automatically. The motion control functionality of the technology objects creates its own execution level and is called in the SIMATIC S7‑1500 execution system according to the application cycle.

The MC_Servo is write-protected. The contents cannot be changed.

The closed-loop position control algorithms of all technology objects configured for Motion Control on the CPU are calculated within the MC_Servo.

You can set the application cycle and the priority of the organization block in accordance with your requirements for control quality and system load.

### Application cycle

You can set the application cycle in which the MC_Servo is called in the properties of the organization block:

- **Synchronous to the bus**

  The MC_Servo is called synchronously with a bus system. You set the send clock in the properties of the selected bus system. You can select the following bus systems:

  - PROFIBUS DP
  - PROFINET IO
  - Local bus system (as of technology version V4.0 or firmware version ≥ 2.6)
  - X142 interface (only SIMATIC Drive Controller)
- You cannot call the MC_Servo synchronously with a bus system that is connected to the CPU via a communications processor/communication module (CP/CM).
- **Cyclic**

  The MC_Servo is called cyclically with the specified application cycle.

The selected application cycle must be long enough to allow all the technology objects for motion control to be processed in one cycle. If the application cycle is not observed, overflows occur. The CPU switches to STOP mode in the case of an overflow of the MC_Servo.

### Clock reduction (CPU V1.5 and higher)

You can reduce the application cycle of the MC_Servo relative to the send clock of an isochronous PROFINET IO system. You can set an integer multiple of the send clock as the factor. Values up to 14 times the send clock (maximum 32 ms) are possible for the application cycle.

If you call an isochronous mode interrupt OB and the MC_Servo synchronously with the same PROFINET IO system, you must set the same application cycle for both organization blocks.

---

**See also**

[Configuring MC_Servo OB (S7-1500, S7-1500T)](#configuring-mc_servo-ob-s7-1500-s7-1500t)
  
[MC_PreServo OB (S7-1500, S7-1500T)](#mc_preservo-ob-s7-1500-s7-1500t)
  
[MC_PostServo OB (S7-1500, S7-1500T)](#mc_postservo-ob-s7-1500-s7-1500t)
  
[MC_Interpolator OB (S7-1500, S7-1500T)](#mc_interpolator-ob-s7-1500-s7-1500t)
  
[MC_Transformation OB (S7-1500T)](#mc_transformation-ob-s7-1500t)

## Configuring MC_Servo OB (S7-1500, S7-1500T)

### Procedure for setting the parameters

To assign the parameters of an [MC_Servo [OB91]](#mc_servo-ob-s7-1500-s7-1500t), follow these steps:

1. Open the "Properties" dialog associated with the MC_Servo in question.
2. Click on the "Cycle time " group in the area navigation.

### Overview of the parameters that can be set

In the "Cycle time" group, select how the MC_Servo will be called in the execution system of the SIMATIC S7-1500:

- Cyclic
- Synchronous to the bus

According to the selected option, you can set the following parameters:

- Application cycle
- Source of the send clock
- Send clock
- Factor

### "Cyclical" option

The MC_Servo is called cyclically with the specified application cycle.

You set the cycle in which the MC_Servo is called in the "Application cycle" field.

### "Synchronous to the bus" option

The MC_Servo is called synchronously with a bus system. You set the send clock in the properties of the selected bus system.

The following parameters are available for the "Synchronous to the bus" option:

- **Source of the send clock**

  In the drop-down list, select the bus system to which the MC_Servo will be called isochronously. You can select the following bus systems:

  - PROFIBUS DP
  - PROFINET IO
  - Local bus system (V4.0 and higher or FW version 2.6 and higher)
  - X142 interface (only SIMATIC Drive Controller)

  You cannot call the MC_Servo synchronously with a bus system that is connected to the CPU via a communications processor/communication module (CP/CM).
- **Send clock (ms)**

  The send clock or DP cycle that is set in the selected PROFINET IO system or DP master system is displayed in this field.
- **Factor**

  You can reduce the application cycle of the MC_Servo relative to the send clock of an isochronous PROFINET IO system. You set an integer multiple of the send clock in the "Factor" field. Values up to 14 times the send clock (maximum 32 ms) are possible for the application cycle.
- **Application cycle (ms)**

  The application cycle that results from the send clock and the specified factor is displayed in this field.

## MC_PreServo OB (S7-1500, S7-1500T)

### Description

The organization block MC_PreServo [OB67] can be programmed and is called in the application cycle configured at the [MC_Servo](#mc_servo-ob-s7-1500-s7-1500t). The MC_PreServo is called directly before the MC_Servo.

Via the organization block, you can read out the configured application cycle (information in ns).

### Structure of the start information

Optimized start information:

| Name | Data type | Meaning |  |
| --- | --- | --- | --- |
| Initial_Call | BOOL | TRUE | In the first call of this OB during transition from STOP to RUN |
| PIP_Input | BOOL | TRUE | The associated process image input is up-to-date. |
| PIP_Output | BOOL | TRUE | The associated process image output was transferred to the outputs in time after the last cycle. |
| IO_System | USINT | Number of the distributed I/O system triggering the interrupt |  |
| Event_Count | INT | n | Number of lost cycles |
| -1 | An unknown number of cycles has been lost, e.g. because the cycle has changed. |  |  |
| Synchronous | BOOL | TRUE | The MC_Servo is called synchronously with a bus system. |
| CycleTime | UDINT | Display of the application cycle configured for the MC_Servo in ns |  |

## MC_PostServo OB (S7-1500, S7-1500T)

### Description

The organization block MC_PostServo [OB95] can be programmed and is called in the application cycle configured at the [MC_Servo](#mc_servo-ob-s7-1500-s7-1500t). The MC_PostServo is called directly after the MC_Servo.

Via the organization block, you can read out the configured application cycle (information in ns).

### Structure of the start information

Optimized start information:

| Name | Data type | Meaning |  |
| --- | --- | --- | --- |
| Initial_Call | BOOL | TRUE | In the first call of this OB during transition from STOP to RUN |
| PIP_Input | BOOL | TRUE | The associated process image input is up-to-date. |
| PIP_Output | BOOL | TRUE | The associated process image output was transferred to the outputs in time after the last cycle. |
| IO_System | USINT | Number of the distributed I/O system triggering the interrupt |  |
| Event_Count | INT | n | Number of lost cycles |
| -1 | An unknown number of cycles has been lost, e.g. because the cycle has changed. |  |  |
| Synchronous | BOOL | TRUE | The MC_Servo is called synchronously with a bus system. |
| CycleTime | UDINT | Display of the application cycle configured for the MC_Servo in ns |  |

## MC_Interpolator OB (S7-1500, S7-1500T)

### Description

When you create a technology object for S7‑1500 Motion Control, the organization block MC_Interpolator [OB92] for processing the technology objects is created automatically. The Motion Control functionality of the technology objects creates its own execution level and is called in the SIMATIC S7‑1500 execution system according to the [MC_Servo](#mc_servo-ob-s7-1500-s7-1500t) application cycle.

The MC_Interpolator is write-protected. The contents cannot be changed.

The evaluation of the Motion Control instructions as well as the monitoring and the setpoint generation for all technology objects configured on the CPU (Motion Control) is performed within the MC_Interpolator.

The MC_Interpolator is called at the end of processing of the MC_Servo OBs. The clock ratio between MC_Interpolator and MC_Servo is always 1:1.

### Improving system performance (S7-1500T FW V3.0 and higher)

To improve the system performance for interpolating the cam technology object, select the "Improve system performance" check box in the properties of MC_Interpolator under "General &gt; Multi-core processor".

The check box "Improve system performance" is selected by default. If the "Improve system performance" check box is grayed out, the setting is not supported by the CPU used.

### Process response

You must select the application cycle of the MC_Servo long enough to allow all the technology objects for Motion Control to be processed in one application cycle. If the application cycle is not observed, overflows occur. Note the following response to overflows:

- The CPU tolerates a maximum of three consecutive MC_Interpolator overflows.
- The execution of an MC_Interpolator may only be interrupted by an MC_Servo call.

If more overflows or interruptions occur, the CPU switches to STOP mode.

You can find more information in section "[Operational sequence and timeouts](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#operational-sequence-and-timeouts-s7-1500-s7-1500t)" of function manual "S7-1500/S7-1500T Motion Control Overview".

## MC_PreInterpolator OB (S7-1500, S7-1500T)

### Description

The organization block MC_PreInterpolator [OB68] can be programmed and is called in the application cycle configured at the [MC_Servo](#mc_interpolator-ob-s7-1500-s7-1500t). The MC_PreInterpolator is called directly before the MC_Interpolator .

Via the organization block, you can read out the configured application cycle.

### Structure of the start information

Optimized start information:

| Name | Data type | Meaning |  |
| --- | --- | --- | --- |
| Initial_Call | BOOL | TRUE | In the first call of this OB after the CPU is switched on |
| PIP_Input | BOOL | TRUE | The associated process image input is up-to-date. |
| PIP_Output | BOOL | TRUE | The associated process image output was transferred to the outputs in time after the last cycle. |
| IO_System | USINT | Number of the distributed I/O system triggering the interrupt |  |
| Event_Count | INT | n | Number of lost cycles |
| -1 | An unknown number of cycles has been lost, e.g. because the cycle has changed. |  |  |
| Reduction | UINT | Reduction ratio of MC_Interpolator to MC_Servo |  |
| CycleTime | UDINT | Display of the application cycle configured for the MC_Interpolator in ns |  |

## MC_Transformation OB (S7-1500T)

### Description

You program the user [transformation](Using%20S7-1500T%20Kinematics%20functions%20%28S7-1500T%29.md#transformation-for-user-defined-kinematics-systems-s7-1500t) of the Cartesian coordinates and the axis-specific setpoints for the user-defined kinematics in the organization block MC_Transformation [OB98]. This programming includes the transformation of the positions and the dynamic values (velocity, acceleration, jerk).

When you add the MC_Transformation in the TIA Portal, the data block "TransformationParameter" is automatically created under "Program blocks &gt; System blocks &gt; Program resources". In the properties of the organization block, the MC_Transformation indicates the number of the data block "TransformationParameter" under "General &gt; Transformation".

In the user program, supply the input parameters of the MC_Transformation with the required start information. You write the axis-specific parameters or the Cartesian parameters in the "TransformationParameter" data block. The MC_Transformation is called with this start information in the execution system of the CPU.

> **Note**
>
> **Only one MC_Transformation per CPU**
>
> You program all required user transformations in an organization block MC_Transformation. If you require multiple transformations or multiple instances of a transformation, you need to identify the transformations or the instances in your user program.

### Block call and priority

The MC_Transformation is called according to the configured priority in the execution system of the CPU.

You configure the priority of the MC_Transformation in the properties of the organization block under "General &gt; Attributes &gt; Priority". For the priority you can set values from 17 to 25 (default setting 25):

- The priority of MC_Transformation must be at least one level lower than the priority of [MC_Servo](#mc_servo-ob-s7-1500-s7-1500t).
- The priority of MC_Transformation must be at least one level higher than the priority of [MC_Interpolator](#mc_interpolator-ob-s7-1500-s7-1500t).

### Parameter

The following table shows the parameters of the MC_Transformation:

| Parameter | Declaration | Data type | Default value | Description |  |
| --- | --- | --- | --- | --- | --- |
| KinematicsObject | INPUT | DB_ANY | - | Kinematics technology object for which the MC_Transformation calculates the transformation when called. |  |
| ExecutionContext | INPUT | DINT | - | Processing context of the MC_Transformation |  |
| 0 | MOTION_EXECUTION  Calculation of the axis setpoints in the motion execution in the interpolator. The calculated values are necessary for the current motion control. Torque precontrol values can be calculated and preset. |  |  |  |  |
| 1 | NON_MOTION_EXECUTION  Calculation of axis setpoints from IPO task and other OBs are possible. The transformation is necessary for the motion planning. |  |  |  |  |
| TransformationType | INPUT | DINT | - | Calculation called for |  |
| 0 | Forward transformation  Calculation of the Cartesian parameters from the axis positions |  |  |  |  |
| 1 | Inverse transformation  Calculation of the axis-specific parameters from the Cartesian parameters |  |  |  |  |
| TransformationParameters | InOut | VARIANT | - | Pointer to the data block "TransformationParameter" |  |
| FunctionResult | OUTPUT | DINT | - | Return value of the MC_Transformation to the kinematics technology object |  |
| 0 | Calculation performed and parameters output |  |  |  |  |
| &lt; 0 | Error during calculation  If an error occurs during the calculation, the kinematics technology object stops the motion. The kinematics technology object outputs a technology alarm with the error ID as an accompany value and deletes the job sequence. |  |  |  |  |
| If an error occurs during the calculation, the kinematics technology object stops the motion. The kinematics technology object outputs a technology alarm with the error ID as an accompany value and deletes the job sequence. |  |  |  |  |  |

---

**See also**

[Transformation for user-defined kinematics systems (S7-1500T)](Using%20S7-1500T%20Kinematics%20functions%20%28S7-1500T%29.md#transformation-for-user-defined-kinematics-systems-s7-1500t)

## MC_LookAhead OB (S7-1500T)

### Description

When you create a kinematics technology object as of V5.0 or an Interpreter technology object as of V8.0 for S7-1500T Motion Control, the organization block MC_LookAhead [OB97] is created automatically. The motion preparation of the kinematics technology object and of the Interpreter technology object is calculated in the MC_LookAhead organization block.

The MC_LookAhead is write-protected. The contents cannot be changed.

> **Note**
>
> **Only one MC_LookAhead per CPU**
>
> The motions of all kinematics and Interpreters of a CPU are prepared in an MC_LookAhead organization block. The MC_LookAhead can only be created once.

Jobs of the job sequence are prepared in advance within the MC_LookAhead. In this way, less time is required for motion preparation in the MC_Interpolator organization block and you can set a shorter application cycle of the MC_Servo organization block.

A download in RUN mode increases the CPU time required to prepare the motion jobs in the job sequence.

### Block call and priority

The MC_LookAhead is triggered by the MC_Interpolator. The MC_LookAhead is not called cyclically according to the configured priority and cycle load in the execution system of the CPU.

You configure the priority of the MC_LookAhead in the properties of the organization block under "General &gt; Attributes &gt; Priority". You can set values from 15 to 16 (default setting 15) for the priority. The priority of MC_LookAhead must be lower than the priority of MC_Interpolator.

### Improving system performance (S7-1500T FW V3.0 and higher)

To improve the system performance for motion preparation of the kinematics technology object, select the "Improve system performance" check box in the properties of MC_LookAhead under "General &gt; Multi-core processor".

The check box "Improve system performance" is selected by default. If the "Improve system performance" check box is grayed out, the setting is not supported by the CPU used.

> **Note**
>
> **User-defined kinematics**
>
> If you are using user-defined kinematics, clear the "Improve system performance" check box.

### Cycle load

You can configure the maximum cycle load of the MC_LookAhead in the properties of the organization block under "General &gt; Multi-core processor". You can set values from 1% to 40% (default setting 20%) for the maximum cycle load.

Select the cycle load of the MC_LookAhead in such a way that the CPU can process all technology objects for Motion Control in one application cycle.

### Process response

If the application cycle is not observed, overflows occur. Note the following response to overflows:

- The CPU tolerates a maximum of three consecutive MC_Interpolator overflows.
- The execution of an MC_Interpolator may only be interrupted by an MC_Servo call.

If more overflows or interruptions occur, the CPU switches to STOP mode.

You can find more information in section "[Operational sequence and timeouts](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#operational-sequence-and-timeouts-s7-1500-s7-1500t)" of function manual "S7-1500/S7-1500T Motion Control Overview".

---
title: "PID_Compact (S7-1200, S7-1500)"
package: ProgFBPIDCompenUS
topics: 30
devices: [S7-1200, S7-1500, S7-1500T]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# PID_Compact (S7-1200, S7-1500)

This section contains information on the following topics:

- [New features of PID_Compact (S7-1200, S7-1500)](#new-features-of-pid_compact-s7-1200-s7-1500)
- [Compatibility with CPU and FW (S7-1200, S7-1500)](#compatibility-with-cpu-and-fw-s7-1200-s7-1500)
- [CPU processing time and memory requirement PID_Compact as of V2 (S7-1200, S7-1500)](#cpu-processing-time-and-memory-requirement-pid_compact-as-of-v2-s7-1200-s7-1500)
- [PID_Compact as of V2 (S7-1200, S7-1500)](#pid_compact-as-of-v2-s7-1200-s7-1500)
- [PID_Compact V1 (S7-1200)](#pid_compact-v1-s7-1200)

## New features of PID_Compact (S7-1200, S7-1500)

### PID_Compact V3.0

- **Dead zone**

  If the process value is noisy, unnecessary fluctuations in the output value can be reduced by manually setting a dead zone width.
- **Active limitation of the integral part and change of the output value limits in automatic mode**

  In addition to the direction-dependent stopping of the integral component, this is now actively limited.

  This allows the change of the output value limits in automatic mode
- **New tags** 
  **Config.OutputSelect**
   **and** 
  **Retain.CtrlParams.SetByUser**

  The tags Config.OutputSelect and Retain.CtrlParams.SetByUser replace the previous tags _Config.OutputSelect and _Retain.CtrlParams.SetByUser, which are only available via the Openness API.

  The tags Config.OutputSelect and Retain.CtrlParams.SetByUser are available both in the instance data block and via the Openness API.

  The existing values for the new tags Config.OutputSelect and Retain.CtrlParams.SetByUser are transferred to individual instances after switching to V3. For multi-instances, the new tags will have the default value after switching to V3. You restore the associated settings manually.

  If you have been using _Config.OutputSelect or _Retain.CtrlParams.SetByUser in your Openness application so far, replace them with the tags Config.OutputSelect and Retain.CtrlParams.SetByUser when you switch to PID_Compact V3.

### PID_Compact V2.4

- **Initialization of the integral action**

  PID_Compact now initializes the integral action if you use OverwriteInitialOutputValue together with inverted control logic.

  If you have been using OverwriteInitialOutputValue together with inverted control logic up to now, please note that the sign of the output value changes with PID_Compact V2.4.

### PID_Compact V2.3

- **Response of the output value when switching from "Inactive" operating mode to "Automatic mode"**

  The new option IntegralResetMode = 4 was added and defined as default. With IntegralResetMode = 4, the integral action is automatically preassigned when switching from "Inactive" operating mode to "Automatic mode" so that a control deviation results in a jump of the output value with identical sign.
- **Initialization of the integral action in automatic mode**

  The integral action can be initialized in automatic mode with the tags OverwriteInitialOutputValue and PIDCtrl.PIDInit. This simplifies the use of PID_Compact for override controls.

### PID_Compact V2.2

- **Use with S7-1200**

  As of PID_Compact V2.2, the instruction with V2 functionality can also be used on S7-1200 with firmware version as of 4.0.

### PID_Compact V2.0

- **Responses in the event of an error**

  The response in the event of an error has been completely overhauled. PID_Compact now responds in a more fault-tolerant manner in the default setting. This reaction is set when copying PID_Compact V1.X from an S7-1200 CPU to an S7-1500 CPU.

  | Symbol | Meaning |
  | --- | --- |
  |  | **Notice** |
  | **Your system may be damaged.**  If you use the default setting, PID_Compact remains in automatic mode when the process value limits are exceeded. This may damage your system.   It is essential to configure how your controlled system responds in the event of an error to protect your system from damage. |  |

  The Error parameter indicates if an error is pending. When the error is no longer pending, Error = FALSE. The ErrorBits parameter shows which errors have occurred. Use ErrorAck to acknowledge the errors and warnings without restarting the controller or clearing the integral action. Switching operating modes no longer clears errors that are no longer pending.

  You can configure the responses in the event of an error with SetSubstituteOutput and ActivateRecoverMode.
- **Substitute output value**

  You can configure a substitute output value that is to be output if an error occurs.
- **Switching the operating mode**

  You specify the operating mode at the Mode in/out parameter and use a positive edge at ModeActivate to start the operating mode. The sRet.i_Mode tag has been omitted.
- **Multi-instance capability**

  You can call up PID_Compact as multi-instance DB.
- **Startup characteristics**

  The operating mode specified at the Mode parameter is also started on a falling edge at Reset and during a CPU cold restart, if RunModeByStartup = TRUE.
- **ENO characteristics**

  ENO is set depending on the operating mode.

  If State = 0, then ENO = FALSE.

  If State ≠ 0, then ENO = TRUE.
- **Setpoint value specification during tuning**

  You configure the permitted fluctuation of the setpoint during tuning at the CancelTuningLevel tag.
- **Value range for output value limits**

  The value 0.0 no longer has to fall within the output value limits.
- **Preassigning the integral action**

  Using the tags IntegralResetMode and OverwriteInitialOutputValue, you can determine the preassignment of the integral action when switching from "Inactive" operating mode to "Automatic mode".
- **Switching a disturbance variable on**

  You can switch a disturbance variable on at the Disturbance parameter.
- **Default value of PID parameters**

  The following default settings have been changed:

  - Proportional action weighting (PWeighting) from 0.0 to 1.0
  - Derivative action weighting (DWeighting) from 0.0 to 1.0
  - Coefficient for derivative delay (TdFiltRatio) from 0.0 to 0.2
- **Renaming tags**

  The static tags have been given new names that are compatible with PID_3Step.

### PID_Compact V1.2

- **Manual mode on CPU startup**

  If ManualEnable = TRUE when the CPU starts, PID_Compact starts in manual mode. A rising edge at ManualEnable is not necessary.
- **Pretuning**

  If the CPU is switched off during pretuning, pretuning starts again when the CPU is switched back on.

### PID_Compact V1.1

- **Manual mode on CPU startup**

  When the CPU starts up, PID_Compact only switches to manual mode with a rising edge at ManualEnable. Without rising edge, PID_Compact starts in the last operating mode in which ManualEnable was FALSE.
- **Reaction to reset**

  A rising edge at Reset resets the errors and warnings and clears the integral action. A falling edge at Reset triggers a switchover to the most recently active operating mode.
- **Default of process value high limit**

  The default value of r_Pv_Hlm has been changed to 120.0.
- **Monitoring the sampling time**

  - An error is no longer output when the current sampling time is ≥ 1.5 x current mean value or when the current sampling time is ≤ 0.5 x current mean value. The sampling time may deviate much more in automatic mode.
  - PID_Compact is compatible with FW as of V2.0.
- **Access to tags**

  The following tags can now be used in the user program.

  - i_Event_SUT
  - i_Event_TIR
  - r_Ctrl_Ioutv
- **Troubleshooting**

  PID_Compact now outputs the correct pulses when the shortest ON time is not equal to the shortest OFF time.

## Compatibility with CPU and FW (S7-1200, S7-1500)

The following table shows which version of PID_Compact can be used on which CPU.

| CPU | FW | PID_Compact |
| --- | --- | --- |
| S7-1200 | as of V4.2 | V2.3  V2.2  V1.2 |
| V4.0 to V4.1 | V2.2  V1.2 |  |
| V3.x | V1.2  V1.1 |  |
| V2.x | V1.2  V1.1 |  |
| V1.x | V1.0 |  |
| S7-1500 | as of V3.1 | V3.0  V2.4 |
| V3.0 | V2.4 |  |
| V2.5 to V2.9 | V2.4  V2.3  V2.2  V2.1  V2.0 |  |
| V2.0 and V2.1 | V2.3  V2.2  V2.1  V2.0 |  |
| V1.5 to V1.8 | V2.2  V2.1  V2.0 |  |
| V1.1 | V2.1  V2.0 |  |
| V1.0 | V2.0 |  |

## CPU processing time and memory requirement PID_Compact as of V2 (S7-1200, S7-1500)

### CPU processing time

Typical CPU processing times of the PID_Compact technology object as of Version V2.0, depending on CPU type and operating mode for standard, F, T and TF CPUs.

|  |  |  |  |
| --- | --- | --- | --- |
| **CPU** | **FW** | **Typ. CPU processing time Automatic mode** | **Typ. CPU processing time pre-tuning and fine tuning** |
| CPU 1211 | ≥ V4.0 | 190 µs | 270 µs |
| CPU 1212 |  |  |  |
| CPU 1214 |  |  |  |
| CPU 1215 |  |  |  |
| CPU 1217 |  |  |  |
| CPU 1510SP | ≤ V2.9 | 65 µs | 80 µs |
| CPU 1511 |  |  |  |
| CPU 1511C |  |  |  |
| CPU 1512C |  |  |  |
| CPU 1512SP |  |  |  |
| CPU 1513 |  |  |  |
| CPU 1515 | 50 µs | 65 µs |  |
| CPU 1516 |  |  |  |
| CPU 1517 | Every | 8 µs | 12 µs |
| CPU 1518 | 4 µs | 6 µs |  |
| CPU 1510SP | ≥ V3.0 | 55 µs | 70 µs |
| CPU 1511 |  |  |  |
| CPU 1511C |  |  |  |
| CPU 1512C |  |  |  |
| CPU 1512SP |  |  |  |
| CPU 1513 |  |  |  |
| CPU 1514SP |  |  |  |
| CPU 1515 | 40 µs | 55 µs |  |
| CPU 1516 |  |  |  |

Typical CPU processing times of the PID_Compact technology object as of Version V2.0, depending on the CPU type and operating mode for R-CPUs in the RUN-Redundant system state.

|  |  |  |  |
| --- | --- | --- | --- |
| **CPU** | **FW** | **Typ. CPU processing time Automatic mode** | **Typ. CPU processing time pre-tuning and fine tuning** |
| CPU 1513R | ≥ V3.0 | 90 µs | 140 µs |
| CPU 1515R | 70 µs | 90 µs |  |

### Memory requirement

Memory requirement of an instance DB of the PID_Compact technology object as of Version V2.0.

|  |  |  |
| --- | --- | --- |
| **Memory requirement** | **Memory requirement of the instance DB of**  **PID_Compact**  **V2.x** | **Memory requirement of the instance DB of**  **PID_Compact**  **V3.x** |
| Load memory requirement | Approx. 3700 bytes | Approx. 3750 bytes |
| Total work memory requirement | 788 bytes | 802 bytes |
| Retentive work memory requirement | 44 bytes | 52 bytes |

## PID_Compact as of V2 (S7-1200, S7-1500)

This section contains information on the following topics:

- [Description of PID_Compact V3 (S7-1200, S7-1500)](#description-of-pid_compact-v3-s7-1200-s7-1500)
- [Description of PID_Compact V2 (S7-1200, S7-1500)](#description-of-pid_compact-v2-s7-1200-s7-1500)
- [PID_Compact as of V2 operating principle (S7-1200, S7-1500)](#pid_compact-as-of-v2-operating-principle-s7-1200-s7-1500)
- [Input parameters of PID_Compact as of V2 (S7-1200, S7-1500)](#input-parameters-of-pid_compact-as-of-v2-s7-1200-s7-1500)
- [Output parameters of PID_Compact as of V2 (S7-1200, S7-1500)](#output-parameters-of-pid_compact-as-of-v2-s7-1200-s7-1500)
- [In/out parameter of PID_Compact as of V2 (S7-1200, S7-1500)](#inout-parameter-of-pid_compact-as-of-v2-s7-1200-s7-1500)
- [Static tags of PID_Compact as of V2 (S7-1200, S7-1500)](#static-tags-of-pid_compact-as-of-v2-s7-1200-s7-1500)
- [Changing the interface of PID_Compact as of V2 (S7-1200, S7-1500)](#changing-the-interface-of-pid_compact-as-of-v2-s7-1200-s7-1500)
- [State and Mode as of V2 parameters (S7-1200, S7-1500)](#state-and-mode-as-of-v2-parameters-s7-1200-s7-1500)
- [ErrorBits as of V2 parameter (S7-1200, S7-1500)](#errorbits-as-of-v2-parameter-s7-1200-s7-1500)
- [ActivateRecoverMode tag as of V2 (S7-1200, S7-1500)](#activaterecovermode-tag-as-of-v2-s7-1200-s7-1500)
- [Warning tag as of V2 (S7-1200, S7-1500)](#warning-tag-as-of-v2-s7-1200-s7-1500)
- [Tag IntegralResetMode as of V2 (S7-1200, S7-1500)](#tag-integralresetmode-as-of-v2-s7-1200-s7-1500)
- [Example program for PID_Compact V2 (S7-1200, S7-1500)](#example-program-for-pid_compact-v2-s7-1200-s7-1500)

### Description of PID_Compact V3 (S7-1200, S7-1500)

#### Description

The PID_Compact instruction provides a PID controller with integrated tuning for actuators with proportional action.

The following operating modes are possible:

- Inactive
- Pretuning
- Fine tuning
- Automatic mode
- Manual mode
- Substitute output value with error monitoring

For a more detailed description of the operating modes, see the State parameter.

#### PID algorithm

PID_Compact is a PIDT1 controller with anti-windup and weighting of the proportional and derivative actions. The PID algorithm operates according to the following equation (dead zone disabled):

![PID algorithm](images/166084815371_DV_resource.Stream@PNG-de-DE.png)

|  |  |  |
| --- | --- | --- |
| **Symbol** | **Description** | **Associated parameters of the PID_Compact instruction** |
| y | Output value of the PID algorithm | - |
| K<sub>p</sub> | Proportional gain | Retain.CtrlParams.Gain |
| s | Laplace operator | - |
| b | Proportional action weighting | Retain.CtrlParams.PWeighting |
| w | Setpoint | CurrentSetpoint |
| x | Process value | ScaledInput |
| T<sub>I</sub> | Integration time | Retain.CtrlParams.Ti |
| T<sub>D</sub> | Derivative action time | Retain.CtrlParams.Td |
| a | Derivative delay coefficient (derivative delay T1 = a × T<sub>D</sub>) | Retain.CtrlParams.TdFiltRatio |
| c | Derivative action weighting | Retain.CtrlParams.DWeighting |
| DeadZone | Dead zone width | Retain.CtrlParams.DeadZone |

#### Block diagram of PID_Compact

![Block diagram of PID_Compact](images/166086830475_DV_resource.Stream@PNG-de-DE.png)

#### Block diagram of PIDT1 with anti-windup

![Block diagram of PIDT1 with anti-windup](images/171621836555_DV_resource.Stream@PNG-de-DE.png)

#### Call

PID_Compact is called in the constant time scale of a cyclic interrupt OB.

#### Download to device

The actual values of retentive variables are only updated when you download PID_Compact completely.

[Download technology object to device](Configuring%20a%20software%20controller.md#downloading-technology-objects-to-device)

#### Startup

When the CPU starts up, PID_Compact starts in the operating mode that is saved in the Mode in/out parameter. To switch to "Inactive" operating mode during startup, set RunModeByStartup = FALSE.

#### Responses in the event of an error

The response in the event of an error is determined by the tags SetSubstituteOutput and ActivateRecoverMode. If ActivateRecoverMode = TRUE, the reaction additionally depends on the error that occurred.

| SetSubstituteOutput | ActivateRecoverMode | Configuration editor  > output value  > Set Output to | Reaction |
| --- | --- | --- | --- |
| Not relevant | FALSE | Zero (inactive) | Switch to "Inactive" mode (State = 0)  The value 0.0 is transferred to the actuator. |
| FALSE | TRUE | Current output value while error is pending | Switch to "Substitute output value with error monitoring" mode (State = 5)  The current output value is transferred to the actuator while the error is pending. |
| TRUE | TRUE | Substitute output value while error is pending | Switch to "Substitute output value with error monitoring" mode (State = 5)  The value at SubstituteOutput is transferred to the actuator while the error is pending. |

In manual mode, PID_Compact uses ManualValue as output value, unless ManualValue is invalid. If ManualValue is invalid, SubstituteOutput is used. If ManualValue and SubstituteOutput are invalid, Config.OutputLowerLimit is used.

The Error parameter indicates if an error is pending. When the error is no longer pending, Error = FALSE. The ErrorBits parameter shows which errors have occurred. ErrorBits is reset by a rising edge at Reset or ErrorAck.

### Description of PID_Compact V2 (S7-1200, S7-1500)

#### Description

The PID_Compact instruction provides a PID controller with integrated tuning for actuators with proportional action.

The following operating modes are possible:

- Inactive
- Pretuning
- Fine tuning
- Automatic mode
- Manual mode
- Substitute output value with error monitoring

For a more detailed description of the operating modes, see the State parameter.

#### PID algorithm

PID_Compact is a PIDT1 controller with anti-windup and weighting of the proportional and derivative actions. The PID algorithm operates according to the following equation:

![PID algorithm](images/166084815371_DV_resource.Stream@PNG-de-DE.png)

|  |  |  |
| --- | --- | --- |
| **Symbol** | **Description** | **Associated parameters of the**  **PID_Compact** instruction |
| y | Output value of the PID algorithm | - |
| K<sub>p</sub> | Proportional gain | Retain.CtrlParams.Gain |
| s | Laplace operator | - |
| b | Proportional action weighting | Retain.CtrlParams.PWeighting |
| w | Setpoint | CurrentSetpoint |
| x | Process value | ScaledInput |
| T<sub>I</sub> | Integration time | Retain.CtrlParams.Ti |
| T<sub>D</sub> | Derivative action time | Retain.CtrlParams.Td |
| a | Derivative delay coefficient (derivative delay T1 = a × T<sub>D</sub>) | Retain.CtrlParams.TdFiltRatio |
| c | Derivative action weighting | Retain.CtrlParams.DWeighting |

#### Block diagram of PID_Compact

![Block diagram of PID_Compact](images/166086830475_DV_resource.Stream@PNG-de-DE.png)

#### Block diagram of PIDT1 with anti-windup

![Block diagram of PIDT1 with anti-windup](images/166084809867_DV_resource.Stream@PNG-en-US.png)

#### Call

PID_Compact is called in the constant time scale of a cyclic interrupt OB.

#### Download to device

The actual values of retentive variables are only updated when you download PID_Compact completely.

[Downloading technology objects to device](Configuring%20a%20software%20controller.md#downloading-technology-objects-to-device)

#### Startup

When the CPU starts up, PID_Compact starts in the operating mode that is saved in the Mode in/out parameter. To switch to "Inactive" operating mode during startup, set RunModeByStartup = FALSE.

#### Responses in the event of an error

The response in the event of an error is determined by the tags SetSubstituteOutput and ActivateRecoverMode. If ActivateRecoverMode = TRUE, the reaction additionally depends on the error that occurred.

| SetSubstituteOutput | ActivateRecoverMode | Configuration editor  > output value  > Set Output to | Reaction |
| --- | --- | --- | --- |
| Not relevant | FALSE | Zero (inactive) | Switch to "Inactive" mode (State = 0)  The value 0.0 is transferred to the actuator. |
| FALSE | TRUE | Current output value while error is pending | Switch to "Substitute output value with error monitoring" mode (State = 5)  The current output value is transferred to the actuator while the error is pending. |
| TRUE | TRUE | Substitute output value while error is pending | Switch to "Substitute output value with error monitoring" mode (State = 5)  The value at SubstituteOutput is transferred to the actuator while the error is pending. |

In manual mode, PID_Compact uses ManualValue as output value, unless ManualValue is invalid. If ManualValue is invalid, SubstituteOutput is used. If ManualValue and SubstituteOutput are invalid, Config.OutputLowerLimit is used.

The Error parameter indicates if an error is pending. When the error is no longer pending, Error = FALSE. The ErrorBits parameter shows which errors have occurred. ErrorBits is reset by a rising edge at Reset or ErrorAck.

### PID_Compact as of V2 operating principle (S7-1200, S7-1500)

#### Monitoring process value limits

You specify the high limit and low limit of the process value in the Config.InputUpperLimit and Config.InputLowerLimit tags. If the process value is outside these limits, an error occurs (ErrorBits = 0001h).

You specify a high and low warning limit of the process value in the Config.InputUpperWarning and Config.InputLowerWarning tags. If the process value is outside these warning limits, a warning occurs (Warning = 0040h), and the InputWarning_H or InputWarning_L output parameter changes to TRUE.

#### Limiting the setpoint

You specify a high limit and low limit of the setpoint in the Config.SetpointUpperLimit and Config.SetpointLowerLimit tags. PID_Compact automatically limits the setpoint to the process value limits. You can limit the setpoint to a smaller range. PID_Compact checks whether this range falls within the process value limits. If the setpoint is outside these limits, the high or low limit is used as the setpoint, and output parameter SetpointLimit_H or SetpointLimit_L is set to TRUE.

The setpoint is limited in all operating modes.

#### Limiting the output value

You specify a high limit and low limit of the output value in the Config.OutputUpperLimit and Config.OutputLowerLimit tags. Output, ManualValue and SubstituteOutput are limited to these values. The output value limits must match the control logic.

The valid output value limit values depend on the Output used.

| Symbol | Meaning |
| --- | --- |
| Output | -100.0 to 100.0% |
| Output_PER | -100.0 to 100.0% |
| Output_PWM | 0.0 to 100.0% |

Rule:

OutputUpperLimit > OutputLowerLimit

> **Note**
>
> **Use with two or more actuators**
>
> PID_Compact is not suitable for use with two or more actuators (for example, in heating/cooling applications), because different actuators need different PID parameters to achieve a good control response. Use PID_Temp for applications with two actuators acting in opposite directions.

#### Substitute output value

In the event of an error, PID_Compact can output a substitute output value that you define at the SubstituteOutput tag. The substitute output value must be within the output value limits.

#### Monitoring signal validity

The values of the following parameters are monitored for validity when used:

- Setpoint
- Input
- Input_PER
- Disturbance
- ManualValue
- SubstituteOutput
- Output
- Output_PER
- Output_PWM

#### Monitoring of the sampling time PID_Compact

Ideally, the sampling time is equivalent to the cycle time of the calling OB. The PID_Compact instruction measures the time interval between two calls. This is the current sampling time. On every switchover of operating mode and during the initial startup, the mean value is formed from the first 10 sampling times. Too great a difference between the current sampling time and this mean value triggers an error (Error = 0800h).

The error occurs during tuning if:

- New mean value >= 1.1 x old mean value
- New mean value <= 0.9 x old mean value

The error occurs in automatic mode if:

- New mean value >= 1.5 x old mean value
- New mean value <= 0.5 x old mean value

If you deactivate the sampling time monitoring (CycleTime.EnMonitoring = FALSE), you can also call PID_Compact in OB1. You must then accept a lower control quality due to the deviating sampling time.

#### Sampling time of the PID algorithm

The controlled system needs a certain amount of time to respond to changes in the output value. It is therefore not advisable to calculate the output value in every cycle. The sampling time of the PID algorithm represents the time between two calculations of the output value. It is calculated during tuning and rounded to a multiple of the cycle time. All other functions of PID_Compact are executed at every call.

If you use Output_PWM, the sampling time of the PID algorithm is used as the period duration of the pulse width modulation. The accuracy of the output signal is determined by the ratio of the PID algorithm sampling time to the cycle time of the OB. It is therefore recommended that the cycle time is a maximum of one tenth of the PID algorithm sampling time.

#### Control logic

An increase of the output value is generally intended to cause an increase in the process value. This is referred to as a normal control logic. For cooling and discharge control systems, it may be necessary to invert the control logic. PID_Compact does not work with negative proportional gain. If InvertControl = TRUE, an increasing control deviation causes a reduction in the output value. The control logic is also taken into account during pretuning and fine tuning.

### Input parameters of PID_Compact as of V2 (S7-1200, S7-1500)

The names of the following parameters apply both to the data block and to access via the Openness API.

| Parameter | Data type | Default | Description |
| --- | --- | --- | --- |
| Setpoint | REAL | 0.0 | Setpoint of the PID controller in automatic mode |
| Input | REAL | 0.0 | A tag of the user program is used as source for the process value.   If you are using parameter Input, then Config.InputPerOn = FALSE must be set. |
| Input_PER | INT | 0 | An analog input is used as the source of the process value.  If you are using parameter Input_PER, then Config.InputPerOn = TRUE must be set. |
| Disturbance | REAL | 0.0 | Disturbance variable or precontrol value |
| ManualEnable | BOOL | FALSE | - A FALSE -> TRUE edge activates "manual mode", while State = 4, Mode remains unchanged.   As long as ManualEnable = TRUE, you cannot change the operating mode via a rising edge at ModeActivate or use the commissioning dialog. - A TRUE -> FALSE edge activates the operating mode that is specified by Mode.  We recommend that you change the operating mode using ModeActivate only. |
| ManualValue | REAL | 0.0 | Manual value  This value is used as the output value in manual mode.  Values from Config.OutputLowerLimit to Config.OutputUpperLimit are permitted. |
| ErrorAck | BOOL | FALSE | - FALSE -> TRUE edge   ErrorBits and Warning are reset. |
| Reset | BOOL | FALSE | Restarts the controller.  - FALSE -> TRUE edge   - Switch to "Inactive" mode   - ErrorBits and Warnings are reset. - As long as Reset = TRUE,    - PID_Compact remains in "Inactive" mode (State = 0).   - You cannot change the operating mode with Mode and ModeActivate or ManualEnable.   - You cannot use the commissioning dialog. - TRUE -> FALSE edge   - If ManualEnable = FALSE, PID_Compact switches to the operating mode that is saved in Mode.   - If Mode = 3, the integral action is treated as configured with the tag IntegralResetMode. |
| ModeActivate | BOOL | FALSE | - FALSE -> TRUE edge   PID_Compact switches to the operating mode that is saved in the Mode parameter. |

### Output parameters of PID_Compact as of V2 (S7-1200, S7-1500)

The names of the following parameters apply both to the data block and to access via the Openness API.

| Parameter | Data type | Default | Description |
| --- | --- | --- | --- |
| ScaledInput | REAL | 0.0 | Scaled process value |
| The "Output", "Output_PER", and "Output_PWM" outputs can be used concurrently. |  |  |  |
| Output | REAL | 0.0 | Output value in REAL format |
| Output_PER | INT | 0 | Analog output value |
| Output_PWM | BOOL | FALSE | Pulse-width-modulated output value  The output value is formed by variable On and Off times. |
| SetpointLimit_H | BOOL | FALSE | If SetpointLimit_H = TRUE, the absolute setpoint high limit is reached (Setpoint ≥ Config.SetpointUpperLimit).  The setpoint is limited to Config.SetpointUpperLimit . |
| SetpointLimit_L | BOOL | FALSE | If SetpointLimit_L = TRUE, the absolute setpoint low limit has been reached (Setpoint ≤ Config.SetpointLowerLimit).  The setpoint is limited to Config.SetpointLowerLimit . |
| InputWarning_H | BOOL | FALSE | If InputWarning_H = TRUE, the process value has reached or exceeded the warning high limit. |
| InputWarning_L | BOOL | FALSE | If InputWarning_L = TRUE, the process value has reached or fallen below the warning low limit. |
| State | INT | 0 | The [State parameter](#state-and-mode-as-of-v2-parameters-s7-1200-s7-1500) shows the current operating mode of the PID controller. You can change the operating mode using the input parameter Mode and a rising edge at ModeActivate.   - State = 0: Inactive - State = 1: Pre-tuning - State = 2: Fine tuning - State = 3: Automatic mode - State = 4: Manual mode - State = 5: Substitute output value with error monitoring |
| Error | BOOL | FALSE | If Error = TRUE, at least one error message is pending in this cycle. |
| ErrorBits | DWORD | DW#16#0 | The [ErrorBits parameter](#errorbits-as-of-v2-parameter-s7-1200-s7-1500) shows which error messages are pending. ErrorBits is retentive and is reset upon a rising edge at Reset or ErrorAck. |

### In/out parameter of PID_Compact as of V2 (S7-1200, S7-1500)

The names of the following parameters apply both to the data block and to access via the Openness API.

| Parameter | Data type | Default | Description |
| --- | --- | --- | --- |
| Mode | INT | 4 | At Mode, specify the operating mode to which PID_Compact is to switch. Options are:  - Mode = 0: Inactive - Mode = 1: Pretuning - Mode = 2: Fine tuning - Mode = 3: Automatic mode - Mode = 4: Manual mode   The operating mode is activated by:  - Rising edge at ModeActivate - Falling edge at Reset - Falling edge at ManualEnable - Cold restart of CPU if RunModeByStartup = TRUE   Mode is retentive.  A detailed description of the operating modes can be found in [State and Mode as of V2 parameters](#state-and-mode-as-of-v2-parameters-s7-1200-s7-1500). |

---

**See also**

[State and Mode as of V2 parameters (S7-1200, S7-1500)](#state-and-mode-as-of-v2-parameters-s7-1200-s7-1500)

### Static tags of PID_Compact as of V2 (S7-1200, S7-1500)

> **Note**
>
> Change the tags identified with <sup>(1)</sup> only in "Inactive" mode to prevent malfunction of the PID controller.

Unless otherwise specified, the names of the following variables apply both to the data block and to access via the Openness API.

| Tag | Data type | Default | Description |
| --- | --- | --- | --- |
| IntegralResetMode | INT | Up to V2.2: 1,   as of V2.3: 4 | The [Tag IntegralResetMode as of V2](#tag-integralresetmode-as-of-v2-s7-1200-s7-1500) determines how the integral action PIDCtrl.IntegralSum is preassigned when switching from "Inactive" operating mode to "Automatic mode". This setting only works for one cycle.  Options are:  - IntegralResetMode = 0: Smooth - IntegralResetMode = 1: Delete - IntegralResetMode = 2: Hold - IntegralResetMode = 3: Pre-assign - IntegralResetMode = 4: Like setpoint change (only for PID_Compact with version ≥ 2.3) |
| OverwriteInitialOutputValue | REAL | 0.0 | If one of the following conditions is met, the integral action PIDCtrl.IntegralSum is preassigned automatically as if Output = OverwriteInitialOutputValue in the previous cycle:  - IntegralResetMode = 3 when switching from "Inactive" operating mode to "Automatic mode" - IntegralResetMode = 3, TRUE -> FALSE edge at parameter Reset and parameter Mode = 3 - PIDCtrl.PIDInit = TRUE in "Automatic mode" (available as of PID_Compact version 2.3) |
| RunModeByStartup | BOOL | TRUE | Activate operating mode at Mode parameter after CPU restart  If RunModeByStartup = TRUE, PID_Compact starts in the operating mode saved in the Mode parameter after CPU startup.  If RunModeByStartup = FALSE, PID_Compact remains in "Inactive" mode after CPU startup. |
| LoadBackUp | BOOL | FALSE | If LoadBackUp = TRUE, the last set of PID parameters is reloaded from the CtrlParamsBackUp structure. The set was saved prior to the last tuning. LoadBackUp is automatically set back to FALSE. |
| PhysicalUnit | INT | 0 | Unit of measurement of the process value and setpoint, e.g., ºC, or ºF.  PhysicalUnit serves the display in the editors and has no influence on the behavior of the control algorithm in the CPU.  When importing PID_Compact up to Version 2.4 via the Openness API, PhysicalUnit is reset to the default value.  As of Version 3.0, the value of PhysicalUnit is retained when importing. |
| PhysicalQuantity | INT | 0 | Physical quantity of the process value and setpoint, e.g., temperature.  PhysicalQuantity serves the display in the editors and has no influence on the behavior of the control algorithm in the CPU.  When importing PID_Compact up to Version 2.4 via the Openness API, PhysicalQuantity is reset to the default value.   As of Version 3.0, the value of PhysicalQuantity is retained when importing. |
| ActivateRecoverMode | BOOL | TRUE | The [ActivateRecoverMode tag as of V2](#activaterecovermode-tag-as-of-v2-s7-1200-s7-1500) determines the response in the event of an error. |
| Warning | DWORD | 0 | [Warning tag as of V2](#warning-tag-as-of-v2-s7-1200-s7-1500) shows the warnings since Reset = TRUE or ErrorAck =TRUE. Warning is retentive. |
| Progress | REAL | 0.0 | Progress of current tuning phase as a percentage (0.0 - 100.0) |
| CurrentSetpoint | REAL | 0.0 | CurrentSetpoint always displays the currently effective setpoint. This value is frozen during tuning. |
| CancelTuningLevel | REAL | 10.0 | Permissible fluctuation of setpoint during tuning. Tuning is not canceled until:  - Setpoint > CurrentSetpoint + CancelTuningLevel or - Setpoint < CurrentSetpoint - CancelTuningLevel |
| SubstituteOutput | REAL | 0.0 | Substitute output value  When the following conditions are met, the substitute output value is used as the output value:  - One or more errors are pending in automatic mode for which ActivateRecoverMode is in effect. - SetSubstituteOutput = TRUE - ActivateRecoverMode = TRUE   Config.OutputUpperLimit ≥ SubstituteOutput ≥ Config.OutputLowerLimit |
| SetSubstituteOutput | BOOL | TRUE | Selection of the output value while an error is pending (State = 5):   - If SetSubstituteOutput = TRUE and ActivateRecoverMode = TRUE, the SubstituteOutput substitute output value configured is output as long as an error is pending. - If SetSubstituteOutput = FALSE and ActivateRecoverMode = TRUE, the actuator remains at the current output value as long as an error is pending. - If ActivateRecoverMode = FALSE, SetSubstituteOutput is not effective. - If SubstituteOutput is invalid (ErrorBits = 16#0002_0000), the substitute output value cannot be output. In this case, the low limit of the output value (Config.OutputLowerLimit) is used as output value. |
| Config.InputPerOn<sup>(1)</sup> | BOOL | TRUE | If InputPerOn = TRUE, the Input_PER parameter is used for detecting the process value. If InputPerOn = FALSE, the Input parameter is used. |
| Config.InvertControl<sup>(1)</sup> | BOOL | FALSE | Invert control logic  If InvertControl = TRUE, an increasing control deviation causes a reduction in the output value. |
| Config.OutputSelect | INT | 0 | Selection of the output value (as of Version 3.0):  - OutputSelect = 0: Output_PER (analog) - OutputSelect = 1: Output - OutputSelect = 2: Output_PWM   Config.OutputSelect is used for configuring the controller in the TIA Portal and has no influence on the calculation of the output values in the CPU. |
| _Config.OutputSelect | INT | 0 | Selection of the output value (up to Version 2.4):  - OutputSelect = 0: Output_PER (analog) - OutputSelect = 1: Output - OutputSelect = 2: Output_PWM   _Config.OutputSelect is used for configuring the controller in the TIA Portal and has no influence on the calculation of the output values in the CPU.   _Config.OutputSelect is not available in the data block and can only be configured in the configuration editor or via the Openness API.  When importing PID_Compact via the Openness API, _Config.OutputSelect is reset to the default value. |
| Config.InputUpperLimit<sup>(1)</sup> | REAL | 120.0 | High limit of the process value  Input and Input_PER are monitored to ensure adherence to this limit. If the limit is exceeded, an error is output and the reaction is determined by ActivateRecoverMode.  At the I/O input, the process value can be a maximum of 18% higher than the standard range (overrange). This means the limit cannot be exceeded when you use an I/O input with the pre-setting for high limit and process value scaling.  When pretuning is started, the difference between high and low limit of the process value is checked to determine whether the distance between setpoint and process value meets the necessary requirements.  InputUpperLimit > InputLowerLimit |
| Config.InputLowerLimit<sup>(1)</sup> | REAL | 0.0 | Low limit of the process value  Input and Input_PER are monitored to ensure adherence to this limit. If the limit is undershot, an error is output and the reaction is determined by ActivateRecoverMode.  InputLowerLimit < InputUpperLimit |
| Config.InputUpperWarning<sup>(1)</sup> | REAL | 3.402822e+38 | Warning high limit of the process value  Input and Input_PER are monitored to ensure adherence to this limit. If the limit is exceeded, a warning is output at the parameter.  If you set InputUpperWarning outside the process value limits, the configured absolute process value high limit is used as the warning high limit.   If you configure InputUpperWarning within the process value limits, this value is used as the warning high limit.  InputUpperWarning > InputLowerWarning |
| Config.InputLowerWarning<sup>(1)</sup> | REAL | -3.402822e+38 | Warning low limit of the process value  Input and Input_PER are monitored to ensure adherence to this limit. If the limit is undershot, a warning is output at the Warning parameter.  If you set InputLowerWarning outside the process value limits, the configured absolute process value low limit is used as the warning low limit.   If you configure InputLowerWarning within the process value limits, this value is used as the warning low limit.  InputLowerWarning < InputUpperWarning |
| Config.OutputUpperLimit | REAL | 100.0 | High limit of output value  For details, see OutputLowerLimit  100.0 ≥ OutputUpperLimit > OutputLowerLimit |
| Config.OutputLowerLimit | REAL | 0.0 | Low limit of output value   For Output and Output_PER, the range of values from -100.0 to +100.0, including zero, is valid. At -100.0, Output_PER = -27648; at +100.0, Output_PER = 27648.  For Output_PWM, the value range 0.0 to +100.0 applies.  The output value limits must match the control logic.  As of Version 3.0, PID_Compact supports the change of the output value limits in automatic mode. Up to version 2.4, these may only be changed in the inactive or manual modes.  OutputLowerLimit < OutputUpperLimit |
| Config.SetpointUpperLimit<sup>(1)</sup> | REAL | 3.402822e+38 | High limit of setpoint  Setpoint is monitored to ensure adherence to this limit. If the limit is exceeded, a warning is output at the Warning parameter.  If you configure SetpointUpperLimit outside the process value limits, the configured process value absolute high limit is used as the setpoint high limit.   If you configure SetpointUpperLimit within the process value limits, this value is used as the setpoint high limit.  SetpointUpperLimit > SetpointLowerLimit |
| Config.SetpointLowerLimit<sup>(1)</sup> | REAL | -3.402822e+38 | Low limit of the setpoint  Setpoint is monitored to ensure adherence to this limit. If the limit is undershot, a warning is output at the Warning parameter.  If you set SetpointLowerLimit outside the process value limits, the configured process value absolute low limit is used as the setpoint low limit.  If you set SetpointLowerLimit within the process value limits, this value is used as the setpoint low limit.  SetpointLowerLimit < SetpointUpperLimit |
| Config.MinimumOnTime<sup>(1)</sup> | REAL | 0.0 | The minimum ON time of the pulse width modulation in seconds is rounded to  MinimumOnTime = n×CycleTime.Value  100000.0 ≥ MinimumOnTime ≥ 0.0 |
| Config.MinimumOffTime<sup>(1)</sup> | REAL | 0.0 | The minimum OFF time of the pulse width modulation in seconds is rounded to  MinimumOffTime = n×CycleTime.Value  100000.0 ≥ MinimumOffTime ≥ 0.0 |
| Config.InputScaling.UpperPointIn<sup>(1)</sup> | REAL | 27648.0 | Scaling Input_PER high  Input_PER is scaled based on the two value pairs UpperPointOut, UpperPointIn and LowerPointOut, LowerPointIn.  Only effective if Input_PER is used for process value detection (Config.InputPerOn = TRUE).  UpperPointIn > LowerPointIn |
| Config.InputScaling.LowerPointIn<sup>(1)</sup> | REAL | 0.0 | Scaling Input_PER low  Input_PER is scaled based on the two value pairs UpperPointOut, UpperPointIn and LowerPointOut, LowerPointIn.  Only effective if Input_PER is used for process value detection Config.InputPerOn = TRUE.  LowerPointIn < UpperPointIn |
| Config.InputScaling.UpperPointOut<sup>(1)</sup> | REAL | 100.0 | Scaled high process value   Input_PER is scaled based on the two value pairs UpperPointOut, UpperPointIn and LowerPointOut, LowerPointIn.  Only effective if Input_PER is used for process value detection Config.InputPerOn = TRUE.  UpperPointOut > LowerPointOut |
| Config.InputScaling.LowerPointOut<sup>(1)</sup> | REAL | 0.0 | Scaled low process value   Input_PER is scaled based on the two value pairs UpperPointOut, UpperPointIn and LowerPointOut, LowerPointIn.  Only effective if Input_PER is used for process value detection Config.InputPerOn = TRUE.  LowerPointOut < UpperPointOut |
| CycleTime.StartEstimation | BOOL | TRUE | If CycleTime.EnEstimation = TRUE, CycleTime.StartEstimation = TRUE starts the automatic determination of the PID_Compact sampling time (cycle time of the calling OB). Once measurement is complete CycleTime.StartEstimation = FALSE. |
| CycleTime.EnEstimation | BOOL | TRUE | If CycleTime.EnEstimation = TRUE, the PID_Compact sampling time is determined automatically.   If CycleTime.EnEstimation = FALSE, the PID_Compact sampling time is not determined automatically and must be configured correctly manually with CycleTime.Value. |
| CycleTime.EnMonitoring | BOOL | TRUE | If CycleTime.EnMonitoring = FALSE, the PID_Compact sampling time is not monitored. If PID_Compact cannot be executed within the sampling time, no error (ErrorBits=16#0000_0800) is output and PID_Compact does not respond as configured with ActivateRecoverMode. |
| CycleTime.Value<sup>(1)</sup> | REAL | 0.1 | PID_Compact sampling time (cycle time of the calling OB) in seconds  CycleTime.Value is determined automatically and is usually equivalent to the cycle time of the calling OB. |
| You can load values from the CtrlParamsBackUp structure with LoadBackUp = TRUE. |  |  |  |
| CtrlParamsBackUp.SetByUser | BOOL | FALSE | Saved value of Retain.CtrlParams.SetByUser (as of Version 3.0) |
| CtrlParamsBackUp.Gain | REAL | 1.0 | Saved proportional gain |
| CtrlParamsBackUp.Ti | REAL | 20.0 | Saved integration time in seconds |
| CtrlParamsBackUp.Td | REAL | 0.0 | Saved derivative action time in seconds |
| CtrlParamsBackUp.TdFiltRatio | REAL | 0.2 | Saved derivative delay coefficient |
| CtrlParamsBackUp.PWeighting | REAL | 1.0 | Saved proportional action weighting factor |
| CtrlParamsBackUp.DWeighting | REAL | 1.0 | Saved derivative action weighting factor |
| CtrlParamsBackUp.Cycle | REAL | 1.0 | Saved sampling time of PID algorithm in seconds |
| CtrlParamsBackUp.DeadZone | REAL | 0.0 | Saved dead zone width (as of Version 3.0) |
| PIDSelfTune.SUT.CalculateParams | BOOL | FALSE | The properties of the controlled system are saved during tuning. If SUT.CalculateParams = TRUE, the parameters for pretuning are recalculated according to these properties. This enables you to change the parameter calculation method without having to repeat controller tuning.  SUT.CalculateParams is set to FALSE after the calculation. |
| PIDSelfTune.SUT.TuneRule | INT | 0 | Methods used to calculate parameters during pretuning:  - SUT.TuneRule = 0: PID according to Chien, Hrones and Reswick - SUT.TuneRule = 1: PI according to Chien, Hrones and Reswick |
| PIDSelfTune.SUT.State | INT | 0 | The SUT.State tag indicates the current phase of pretuning:  - State = 0: Initialize pretuning - State = 100: Calculate the standard deviation - State = 200: Find the point of inflection - State = 9900: Pretuning successful - State = 1: Pretuning not successful |
| PIDSelfTune.TIR.RunIn | BOOL | FALSE | With the RunIn tag, you can specify that fine tuning can also be performed without pretuning.  - RunIn = FALSE   Pretuning is started when fine tuning is started from inactive or manual mode. If the requirements for pretuning are not met, PID_Compact reacts as if RunIn = TRUE.   If fine tuning is started from automatic mode, the system uses the existing PID parameters to control to the setpoint.   Only then will fine tuning start. If pretuning is not possible, PID_Compact switches to the mode from which tuning was started. - RunIn = TRUE   The pre-tuning is skipped. PID_Compact attempts to reach the setpoint with the minimum or maximum output value. This can produce increased overshoot. Fine tuning then starts automatically.   RunIn is set to FALSE after fine tuning. |
| PIDSelfTune.TIR.CalculateParams | BOOL | FALSE | The properties of the controlled system are saved during tuning. If TIR.CalculateParams = TRUE, the parameters for fine tuning are recalculated according to these properties. This enables you to change the parameter calculation method without having to repeat controller tuning.  TIR.CalculateParams is set to FALSE after the calculation. |
| PIDSelfTune.TIR.TuneRule | INT | 0 | Methods used to calculate parameters during fine tuning:  - TIR.TuneRule = 0: PID automatic - TIR.TuneRule = 1: PID fast (faster control response with higher amplitudes of the output value than with TIR.TuneRule = 2) - TIR.TuneRule = 2: PID slow (slower control response with lower amplitudes of the output value than with TIR.TuneRule = 1) - TIR.TuneRule = 3: Ziegler-Nichols PID - TIR.TuneRule = 4: Ziegler-Nichols PI - TIR.TuneRule = 5: Ziegler-Nichols P   To be able to repeat the calculation of the PID parameters with TIR.CalculateParams and TIR.TuneRule = 0, 1 or 2, the previous fine tuning also has to have been executed with TIR.TuneRule = 0, 1 or 2.  If this is not the case, TIR.TuneRule = 3 is used.  The recalculation of the PID parameters with TIR.CalculateParams and TIR.TuneRule = 3, 4 or 5 is always possible. |
| PIDSelfTune.TIR.State | INT | 0 | The TIR.State tag indicates the current phase of fine tuning:  - State = -100 Fine tuning is not possible. Pretuning will be performed first. - State = 0: Initialize fine tuning - State = 200: Calculate the standard deviation - State = 300: Attempt to reach setpoint - State = 400: Attempt to reach setpoint with existing PID parameters (if pretuning was successful) - State = 500: Determine oscillation and calculate parameters - State = 9900: Fine tuning successful - State = 1: Fine tuning not successful |
| PIDCtrl.IntegralSum<sup>(1)</sup> | REAL | 0.0 | Current integral action |
| PIDCtrl.PIDInit | BOOL | FALSE | PIDCtrl.PIDInit is available as of PID_Compact version 2.3.   If PIDCtrl.PIDInit = TRUE in "Automatic mode", the integral action PIDCtrl.IntegralSum is preassigned automatically as if Output = OverwriteInitialOutputValue in the previous cycle. This can be used for a [Override control with PID_Compact as of V2](Using%20PID_Compact%20%28S7-1200%2C%20S7-1500%29.md#override-control-with-pid_compact-as-of-v2-s7-1200-s7-1500). |
| Retain.CtrlParams.SetByUser<sup>(1)</sup> | BOOL | FALSE | Enable manual input of PID parameters (as of Version 3.0)  If Retain.CtrlParams.SetByUser = TRUE, the PID parameters are editable.  Retain.CtrlParams.SetByUser is used for configuring the controller in the TIA Portal and has no influence on the behavior of the control algorithm in the CPU.  SetByUser is retentive. |
| _Retain.CtrlParams.SetByUser<sup>(1)</sup> | BOOL | FALSE | Enable manual input of PID parameters (up to Version 2.4)  If _Retain.CtrlParams.SetByUser = TRUE, the PID parameters are editable.  _Retain.CtrlParams.SetByUser is used for configuring the controller in the TIA Portal and has no influence on the behavior of the control algorithm in the CPU.  _Retain.CtrlParams.SetByUser is not available in the data block and can only be configured in the configuration editor or via the Openness API.  When importing PID_Compact via the Openness API, _Retain.CtrlParams.SetByUser is reset to the default value. |
| Retain.CtrlParams.Gain<sup>(1)</sup> | REAL | 1.0 | Active proportional gain  PID_Compact does not work with a negative proportional gain. To invert the control logic, use the Config.InvertControl tag.  Gain is retentive.  Gain ≥ 0.0 |
| Retain.CtrlParams.Ti<sup>(1)</sup> | REAL | 20.0 | - CtrlParams.Ti > 0.0: Active integration time in seconds - CtrlParams.Ti = 0.0: Integral action is deactivated  Ti is retentive.  100000.0 ≥ Ti ≥ 0.0 |
| Retain.CtrlParams.Td<sup>(1)</sup> | REAL | 0.0 | - CtrlParams.Td > 0.0: Active derivative action time in seconds - CtrlParams.Td = 0.0: Derivative action is deactivated  Td is retentive.  100000.0 ≥ Td ≥ 0.0 |
| Retain.CtrlParams.TdFiltRatio<sup>(1)</sup> | REAL | 0.2 | Active derivative delay coefficient  The derivative delay coefficient delays the effect of the derivative action.   Derivative delay = derivative action time × derivative delay coefficient  - 0.0: Derivative action is effective for one cycle only and therefore almost not effective. - 0.5: This value has proved useful in practice for controlled systems with **one** dominant time constant. - > 1.0: The greater the coefficient, the longer the effect of the derivative action is delayed.   TdFiltRatio is retentive.  TdFiltRatio ≥ 0.0 |
| Retain.CtrlParams.PWeighting<sup>(1)</sup> | REAL | 1.0 | Active proportional action weighting  The proportional action may weaken with changes to the setpoint.  Values from 0.0 to 1.0 are applicable.  - 1.0: Proportional action for setpoint change is fully effective - 0.0: Proportional action for setpoint change is not effective   The proportional action is always fully effective when the process value is changed.  PWeighting is retentive.  1.0 ≥ PWeighting ≥ 0.0 |
| Retain.CtrlParams.DWeighting<sup>(1)</sup> | REAL | 1.0 | Active derivative action weighting  The derivative action may weaken with changes to the setpoint.  Values from 0.0 to 1.0 are applicable.  - 1.0: Derivative action is fully effective upon setpoint change - 0.0: Derivative action is not effective upon setpoint change   The derivative action is always fully effective when the process value is changed.  DWeighting is retentive.  1.0 ≥ DWeighting ≥ 0.0 |
| Retain.CtrlParams.Cycle<sup>(1)</sup> | REAL | 1.0 | Active sampling time of the PID algorithm in seconds  CtrlParams.Cycle is calculated during tuning and rounded to an integer multiple of CycleTime.Value.  CtrlParams.Cycle is used as time period of the pulse width modulation.  Cycle is retentive.  100000.0 ≥ Cycle > 0.0 |
| Retain.CtrlParams.DeadZone<sup>(1)</sup> | REAL | 0.0 | Active dead zone width  CtrlParams.DeadZone is available as of PID_Compact Version 3.0.  With CtrlParams.DeadZone = 0.0, the dead zone is switched off.  CtrlParams.DeadZone is not set automatically or adjusted during tuning. You must correctly configure CtrlParams.DeadZone manually.  When the dead zone is switched on, the result can be a permanent control deviation (deviation between setpoint and process value). This can have a negative effect on fine tuning.  DeadZone is retentive.  DeadZone≥ 0.0 |

---

**See also**

[ActivateRecoverMode tag as of V2 (S7-1200, S7-1500)](#activaterecovermode-tag-as-of-v2-s7-1200-s7-1500)
  
[Warning tag as of V2 (S7-1200, S7-1500)](#warning-tag-as-of-v2-s7-1200-s7-1500)
  
[Downloading technology objects to device](Configuring%20a%20software%20controller.md#downloading-technology-objects-to-device)

### Changing the interface of PID_Compact as of V2 (S7-1200, S7-1500)

The following table shows what has changed in the PID_Compact instruction interface.

| PID_Compact V1 | PID_Compact as of V2 | Change |
| --- | --- | --- |
| Input_PER | Input_PER | Data type from Word to Int |
|  | Disturbance | New |
|  | ErrorAck | New |
|  | ModeActivate | New |
| Output_PER | Output_PER | Data type from Word to Int |
| Error | ErrorBits | Renamed |
|  | Error | New |
|  | Mode | New |
| sb_RunModeByStartup | RunModeByStartup | Function |
|  | IntegralResetMode |  |
|  | OverwriteInitialOutputValue | New |
|  | SetSubstituteOutput | New |
|  | CancelTuningLevel | New |
|  | SubstituteOutput | New |

The following table shows which variables have been renamed.

| PID_Compact V1.x | PID_Compact as of V2 |
| --- | --- |
| sb_GetCycleTime | CycleTime.StartEstimation |
| sb_EnCyclEstimation | CycleTime.EnEstimation |
| sb_EnCyclMonitoring | CycleTime.EnMonitoring |
| sb_RunModeByStartup | RunModeByStartup |
| si_Unit | PhysicalUnit |
| si_Type | PhysicalQuantity |
| sd_Warning | Warning |
| sBackUp.r_Gain | CtrlParamsBackUp.Gain |
| sBackUp.r_Ti | CtrlParamsBackUp.Ti |
| sBackUp.r_Td | CtrlParamsBackUp.Td |
| sBackUp.r_A | CtrlParamsBackUp.TdFiltRatio |
| sBackUp.r_B | CtrlParamsBackUp.PWeighting |
| sBackUp.r_C | CtrlParamsBackUp.DWeighting |
| sBackUp.r_Cycle | CtrlParamsBackUp.Cycle |
| sPid_Calc.r_Cycle | CycleTime.Value |
| sPid_Calc.b_RunIn | PIDSelfTune.TIR.RunIn |
| sPid_Calc.b_CalcParamSUT | PIDSelfTune.SUT.CalculateParams |
| sPid_Calc.b_CalcParamTIR | PIDSelfTune.TIR.CalculateParams |
| sPid_Calc.i_CtrlTypeSUT | PIDSelfTune.SUT.TuneRule |
| sPid_Calc.i_CtrlTypeTIR | PIDSelfTune.TIR.TuneRule |
| sPid_Calc.r_Progress | Progress |
| sPid_Cmpt.r_Sp_Hlm | Config.SetpointUpperLimit |
| sPid_Cmpt.r_Sp_Llm | Config.SetpointLowerLimit |
| sPid_Cmpt.r_Pv_Norm_IN_1 | Config.InputScaling.LowerPointIn |
| sPid_Cmpt.r_Pv_Norm_IN_2 | Config.InputScaling.UpperPointIn |
| sPid_Cmpt.r_Pv_Norm_OUT_1 | Config.InputScaling.LowerPointOut |
| sPid_Cmpt.r_Pv_Norm_OUT_2 | Config.InputScaling.UpperPointOut |
| sPid_Cmpt.r_Lmn_Hlm | Config.OutputUpperLimit |
| sPid_Cmpt.r_Lmn_Llm | Config.OutputLowerLimit |
| sPid_Cmpt.b_Input_PER_On | Config.InputPerOn |
| sPid_Cmpt.b_LoadBackUp | LoadBackUp |
| sPid_Cmpt.b_InvCtrl | Config.InvertControl |
| sPid_Cmpt.r_Lmn_Pwm_PPTm | Config.MinimumOnTime |
| sPid_Cmpt.r_Lmn_Pwm_PBTm | Config.MinimumOffTime |
| sPid_Cmpt.r_Pv_Hlm | Config.InputUpperLimit |
| sPid_Cmpt.r_Pv_Llm | Config.InputLowerLimit |
| sPid_Cmpt.r_Pv_HWrn | Config.InputUpperWarning |
| sPid_Cmpt.r_Pv_LWrn | Config.InputLowerWarning |
| sParamCalc.i_Event_SUT | PIDSelfTune.SUT.State |
| sParamCalc.i_Event_TIR | PIDSelfTune.TIR.State |
| sRet.i_Mode | sRet.i_Mode has been omitted. The operating mode is changed using Mode and ModeActivate. |
| sRet.r_Ctrl_Gain | Retain.CtrlParams.Gain |
| sRet.r_Ctrl_Ti | Retain.CtrlParams.Ti |
| sRet.r_Ctrl_Td | Retain.CtrlParams.Td |
| sRet.r_Ctrl_A | Retain.CtrlParams.TdFiltRatio |
| sRet.r_Ctrl_B | Retain.CtrlParams.PWeighting |
| sRet.r_Ctrl_C | Retain.CtrlParams.DWeighting |
| sRet.r_Ctrl_Cycle | Retain.CtrlParams.Cycle |

### State and Mode as of V2 parameters (S7-1200, S7-1500)

#### Correlation of the parameters

The State parameter shows the current operating mode of the PID controller. You cannot change the State parameter.

With a rising edge at ModeActivate, PID_Compact switches to the operating mode saved in the Mode in-out parameter.

When the CPU is switched on or switches from Stop to RUN mode, PID_Compact starts in the operating mode that is saved in the Mode parameter. To retain PID_Compact in "Inactive" mode, set RunModeByStartup = FALSE.

#### Meaning of values

| State / Mode | Description of operating mode |
| --- | --- |
| 0 | Inactive  In "Inactive" operating mode, the output value 0.0 is always output, regardless of Config.OutputUpperLimit and Config.OutputLowerLimit. Pulse width modulation is off. |
| 1 | Pretuning  The pretuning determines the process response to a jump change of the output value and searches for the point of inflection. The PID parameters are calculated from the maximum rate of rise and dead time of the controlled system. You obtain the best PID parameters when you perform pretuning and fine tuning.  Pretuning requirements:  - Inactive (State = 0), manual mode (State = 4), or automatic mode (State = 3) - ManualEnable = FALSE - Reset = FALSE - The process value must not be too close to the setpoint.   |Setpoint - Input| > 0.3 * | Config.InputUpperLimit - Config.InputLowerLimit| and   |Setpoint - Input| > 0.5 * |Setpoint| - The setpoint and the process value lie within the configured limits.   The more stable the process value is, the easier it is to calculate the PID parameters and the more precise the result will be. Noise on the process value can be tolerated as long as the rate of rise of the process value is significantly higher compared to the noise.   The setpoint is frozen in the CurrentSetpoint tag. Tuning is canceled when:  - Setpoint > CurrentSetpoint + CancelTuningLevel or - Setpoint < CurrentSetpoint - CancelTuningLevel   Before the PID parameters are recalculated, they are backed up and can be reactivated with LoadBackUp.  The controller switches to automatic mode following successful pretuning. If pretuning is unsuccessful, the switchover of the operating mode is dependent on ActivateRecoverMode.  The phase of pretuning is indicated with PIDSelfTune.SUT.State.  For starting pretuning in Automatic mode, it is recommended to perform the required setpoint change simultaneously with the rising edge at ModeActivate. If the setpoint is changed first and the pretuning is started later, the output value in automatic mode is adjusted accordingly and causes a change to the process value. This can have a negative effect on the subsequent pretuning or prevent it from starting. |
| 2 | Fine tuning  Fine tuning generates a constant, limited oscillation of the process value. The PID parameters are recalculated based on the amplitude and frequency of this oscillation. PID parameters from fine tuning usually have better master control and disturbance characteristics than PID parameters from pretuning. You obtain the best PID parameters when you perform pretuning and fine tuning.  PID_Compact automatically attempts to generate an oscillation greater than the noise of the process value. Fine tuning is only minimally influenced by the stability of the process value.   The setpoint is frozen in the CurrentSetpoint tag. Tuning is canceled when:  - Setpoint > CurrentSetpoint + CancelTuningLevel or - Setpoint < CurrentSetpoint - CancelTuningLevel   Before the PID parameters are recalculated, they are backed up and can be reactivated with LoadBackUp.  Requirements for fine tuning:  - No disturbances are expected. - The setpoint and the process value lie within the configured limits. - ManualEnable = FALSE - Reset = FALSE - Automatic (State = 3), inactive (State = 0) or manual (State = 4) mode   Fine tuning proceeds as follows when started from:  - Automatic mode (State = 3)   Start fine tuning from automatic mode if you wish to improve the existing PID parameters through tuning.   PID_Compact controls the system using the existing PID parameters until the control loop has stabilized and the requirements for fine tuning have been met. Only then will fine tuning start. - Inactive (State = 0) or manual mode (State = 4)   If the requirements for pretuning are met, pretuning is started. The determined PID parameters will be used for control until the control loop has stabilized and the requirements for fine tuning have been met.    If the process value for pretuning is already too near the setpoint or PIDSelfTune.TIR.RunIn = TRUE, an attempt is made to reach the setpoint with the minimum or maximum output value. This can produce increased overshoot.    Only then will fine tuning start.   The controller switches to automatic mode following successful fine tuning. If fine tuning is unsuccessful, the switchover of the operating mode is dependent on ActivateRecoverMode.  The "Fine tuning" phase is indicated with PIDSelfTune.TIR.State. |
| 3 | Automatic mode  In automatic mode, PID_Compact corrects the controlled system in accordance with the parameters specified.  The controller switches to automatic mode if one the following requirements is fulfilled:  - Pretuning successfully completed - Fine tuning successfully completed - Changing of the Mode in-out parameter to the value 3 and a rising edge at ModeActivate.   The switchover from automatic mode to manual mode is only bumpless if carried out in the commissioning editor.  The ActivateRecoverMode tag is taken into consideration in automatic mode. |
| 4 | Manual mode  In manual mode, you specify a manual output value in the ManualValue parameter.  You can also activate this operating mode using ManualEnable = TRUE. We recommend that you change the operating mode using Mode and ModeActivate only.  The switchover from manual mode to automatic mode is bumpless. Manual mode is also possible when an error is pending. |
| 5 | Substitute output value with error monitoring  The control algorithm is deactivated. The SetSubstituteOutput tag determines which output value is output in this operating mode.  - SetSubstituteOutput = FALSE: Last valid output value - SetSubstituteOutput = TRUE: Substitute output value   You cannot activate this operating mode using Mode = 5.   In the event of an error, it is activated instead of "Inactive" operating mode if all the following conditions are met:  - Automatic mode (Mode = 3) - ActivateRecoverMode = TRUE - One or more errors have occurred in which ActivateRecoverMode is effective.   As soon as the errors are no longer pending, PID_Compact switches back to automatic mode. |

#### ENO characteristics

If State = 0, then ENO = FALSE.

If State ≠ 0, then ENO = TRUE.

#### Automatic switchover of operating mode during commissioning

Automatic mode is activated following successful pretuning or fine tuning. The following table shows how Mode and State change during successful pretuning.

| Cycle no. | Mode | State | Action |
| --- | --- | --- | --- |
| 0 | 4 | 4 | Set Mode = 1 |
| 1 | 1 | 4 | Set ModeActivate = TRUE |
| 1 | 4 | 1 | Value of State is saved in Mode parameter  Pretuning is started |
| n | 4 | 1 | Pretuning successfully completed |
| n | 3 | 3 | Automatic mode is started |

PID_Compact automatically switches the operating mode in the event of an error. The following table shows how Mode and State change during pretuning with errors.

| Cycle no. | Mode | State | Action |
| --- | --- | --- | --- |
| 0 | 4 | 4 | Set Mode = 1 |
| 1 | 1 | 4 | Set ModeActivate = TRUE |
| 1 | 4 | 1 | Value of State is saved in Mode parameter  Pretuning is started |
| n | 4 | 1 | Pretuning canceled |
| n | 4 | 4 | Manual mode is started |

If ActivateRecoverMode = TRUE, the operating mode that is saved in the Mode parameter is activated. At the start of pretuning or fine tuning, PID_Compact has saved the value of State in the Mode in/out parameter. PID_Compact therefore switches to the operating mode from which tuning was started.

If ActivateRecoverMode = FALSE, the system switches to "Inactive" operating mode.

---

**See also**

[Output parameters of PID_Compact as of V2 (S7-1200, S7-1500)](#output-parameters-of-pid_compact-as-of-v2-s7-1200-s7-1500)

### ErrorBits as of V2 parameter (S7-1200, S7-1500)

If several errors are pending simultaneously, the values of the ErrorBits are displayed with binary addition. The display of ErrorBits = 16#0000_0003, for example, indicates that the errors 16#0000_0001 and 16#0000_0002 are pending simultaneously.

In manual mode, PID_Compact uses ManualValue as output value. The exception is Errorbits = 16#0001_0000.

| ErrorBits  (DW#16#...) | Description |
| --- | --- |
| 0000_0000 | There is no error. |
| 0000_0001 | The "Input" parameter is outside the process value limits.  - Input > Config.InputUpperLimit or - Input < Config.InputLowerLimit   If automatic mode was active before the error occurred and ActivateRecoverMode = TRUE, PID_Compact remains in automatic mode.  If pretuning or fine tuning mode was active before the error occurred and ActivateRecoverMode = TRUE, PID_Compact switches to the operating mode that is saved in the Mode parameter. |
| 0000_0002 | Invalid value at "Input_PER" parameter. Check whether an error is pending at the analog input.  If automatic mode was active before the error occurred and ActivateRecoverMode = TRUE, PID_Compact outputs the configured substitute output value. As soon as the error is no longer pending, PID_Compact switches back to automatic mode.  If pretuning or fine tuning mode was active before the error occurred and ActivateRecoverMode = TRUE, PID_Compact switches to the operating mode that is saved in the Mode parameter. |
| 0000_0004 | Error during fine tuning. The oscillation of the process value could not be maintained.  If ActivateRecoverMode = TRUE before the error occurred, PID_Compact cancels the tuning and switches to the operating mode that is saved in the Mode parameter. |
| 0000_0008 | Error at start of pretuning. The process value is too close to the setpoint. Start fine tuning.  If ActivateRecoverMode = TRUE before the error occurred, PID_Compact cancels the tuning and switches to the operating mode that is saved in the Mode parameter. |
| 0000_0010 | The setpoint was changed during tuning.  You can set the permitted fluctuation of the setpoint at the CancelTuningLevel tag.  If ActivateRecoverMode = TRUE before the error occurred, PID_Compact cancels the tuning and switches to the operating mode that is saved in the Mode parameter. |
| 0000_0020 | Pretuning is not permitted during fine tuning.  If ActivateRecoverMode = TRUE before the error occurred, PID_Compact remains in fine tuning mode. |
| 0000_0080 | Error during pretuning. The output value limits are not configured correctly or the process value is not reacting as expected.  Make sure that:  - The limits of the output value are configured correctly and match the control logic. - It is possible to change the output value so that the process value approaches the setpoint. The output value is not already limited by the corresponding output value limit before the pretuning.   Example: With normal control logic and a process value that is below the setpoint, the output value must not have reached the high limit before the start of the pretuning. - The process value does not show a strong oscillation before the start of the pretuning.   For starting a pretuning in automatic mode, it is recommended to perform the required setpoint change simultaneously with the rising edge at ModeActivate. This prevents the output value from running into the limitation between the setpoint change and the start of the pretuning. Alternatively, this can also be achieved by starting from manual mode or "Inactive" mode.  If ActivateRecoverMode = TRUE before the error occurred, PID_Compact cancels the tuning and switches to the operating mode that is saved in the Mode parameter. |
| 0000_0100 | Error during fine tuning resulted in invalid parameters.  If ActivateRecoverMode = TRUE before the error occurred, PID_Compact cancels the tuning and switches to the operating mode that is saved in the Mode parameter. |
| 0000_0200 | Invalid value at "Input" parameter: Value has an invalid number format.  If automatic mode was active before the error occurred and ActivateRecoverMode = TRUE, PID_Compact outputs the configured substitute output value. As soon as the error is no longer pending, PID_Compact switches back to automatic mode.  If pretuning or fine tuning mode was active before the error occurred and ActivateRecoverMode = TRUE, PID_Compact switches to the operating mode that is saved in the Mode parameter. |
| 0000_0400 | Calculation of output value failed. Check the PID parameters.  If automatic mode was active before the error occurred and ActivateRecoverMode = TRUE, PID_Compact outputs the configured substitute output value. As soon as the error is no longer pending, PID_Compact switches back to automatic mode.  If pretuning or fine tuning mode was active before the error occurred and ActivateRecoverMode = TRUE, PID_Compact switches to the operating mode that is saved in the Mode parameter. |
| 0000_0800 | Sampling time error: PID_Compact is not called within the sampling time of the cyclic interrupt OB.  It is recommended to call PID_Compact in a cyclic interrupt OB without conditions and to activate or deactivate it via the operating mode at the Mode parameter. Conditional calls or the call in OB1 can have a negative effect on the control quality.  Monitoring of the sampling time can be disabled with CycleTime.EnMonitoring = FALSE.  If automatic mode was active before the error occurred and ActivateRecoverMode = TRUE, PID_Compact remains in automatic mode.  If pretuning or fine tuning mode was active before the error occurred and ActivateRecoverMode = TRUE, PID_Compact switches to the operating mode that is saved in the Mode parameter.  If this error occurred during simulation with PLCSIM, see the notes under [Simulating PID_Compact as of V2 with PLCSIM](Using%20PID_Compact%20%28S7-1200%2C%20S7-1500%29.md#simulating-pid_compact-as-of-v2-with-plcsim-s7-1200-s7-1500). |
| 0000_1000 | Invalid value at "Setpoint" parameter: Value has an invalid number format.  If automatic mode was active before the error occurred and ActivateRecoverMode = TRUE, PID_Compact outputs the configured substitute output value. As soon as the error is no longer pending, PID_Compact switches back to automatic mode.  If pretuning or fine tuning mode was active before the error occurred and ActivateRecoverMode = TRUE, PID_Compact switches to the operating mode that is saved in the Mode parameter. |
| 0001_0000 | Invalid value at ManualValue parameter. Value has an invalid number format.  If ActivateRecoverMode = TRUE before an error occurred, PID_Compact uses SubstituteOutput as the output value. As soon as you specify a valid value in ManualValue, PID_Compact uses it as the output value. |
| 0002_0000 | Invalid value at SubstituteOutput tag. Value has an invalid number format.  PID_Compact uses the output value low limit as the output value.   If automatic mode was active before the error occurred, ActivateRecoverMode = TRUE, and the error is no longer pending, PID_Compact switches back to automatic mode. |
| 0004_0000 | Invalid value at Disturbance parameter. Value has an invalid number format.  If automatic mode was active and ActivateRecoverMode = TRUE before the error occurred, Disturbance is set to zero. PID_Compact remains in automatic mode.  If pretuning or fine tuning mode was active and ActivateRecoverMode = TRUE before the error occurred, PID_Compact switches to the operating mode saved in the Mode parameter. If Disturbance in the current phase has no effect on the output value, tuning is not be canceled. |

### ActivateRecoverMode tag as of V2 (S7-1200, S7-1500)

The ActivateRecoverMode tag determines the response in the event of an error. The Error parameter indicates if an error is pending. When the error is no longer pending, Error = FALSE. The ErrorBits parameter shows which errors have occurred.

#### Automatic mode

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Your system may be damaged.**  If ActivateRecoverMode = TRUE, PID_Compact remains in automatic mode even if there is an error and the process limit values are exceeded. This may damage your system.   It is essential to configure how your controlled system responds in the event of an error to protect your system from damage. |  |

| ActivateRecoverMode | Description |
| --- | --- |
| FALSE | PID_Compact automatically switches to "Inactive" mode in the event of an error. The controller is only activated by a falling edge at Reset or a rising edge at ModeActivate. |
| TRUE | If errors occur frequently in automatic mode, this setting has a negative effect on the control response, because PID_Compact switches between the calculated output value and the substitute output value at each error. In this case, check the ErrorBits parameter and eliminate the cause of the error.  If one or more of the following errors occur, PID_Compact stays in automatic mode:  - 0001h: The "Input" parameter is outside the process value limits. - 0800h: Sampling time error - 40000h: Invalid value at Disturbance parameter.   If one or more of the following errors occur, PID_Compact switches to "Substitute output value with error monitoring" mode:  - 0002h: Invalid value at Input_PER parameter. - 0200h: Invalid value at Input parameter. - 0400h: Calculation of output value failed. - 1000h: Invalid value at Setpoint parameter.   If the following error occurs, PID_Compact switches to "Substitute output value with error monitoring" mode and moves the actuator to Config.OutputLowerLimit:  - 20000h: Invalid value at SubstituteOutput tag. Value has an invalid number format.   This characteristics are independent of SetSubstituteOutput.   As soon as the errors are no longer pending, PID_Compact switches back to automatic mode. |

#### Pretuning and fine tuning

| ActivateRecoverMode | Description |
| --- | --- |
| FALSE | PID_Compact automatically switches to "Inactive" mode in the event of an error. The controller is only activated by a falling edge at Reset or a rising edge at ModeActivate. |
| TRUE | If the following error occurs, PID_Compact remains in the active mode:  - 0020h: Pretuning is not permitted during fine tuning.   The following errors are ignored:  - 10000h: Invalid value at ManualValue parameter. - 20000h: Invalid value at SubstituteOutput tag.   When any other error occurs, PID_Compact cancels the tuning and switches to the mode from which tuning was started. |

#### Manual mode

ActivateRecoverMode is not effective in manual mode.

### Warning tag as of V2 (S7-1200, S7-1500)

If several warnings are pending simultaneously, the values of the Warning tag are displayed with binary addition. The display of the warning 16#0000_0003, for example, indicates that the warnings 0000_0001 and 0000_0002 are pending simultaneously.

| Warning  (DW#16#....) | Description |
| --- | --- |
| 0000_0000 | No warning pending. |
| 0000_0001 | The point of inflection was not found during pretuning. |
| 0000_0004 | The setpoint was limited to the configured limits. |
| 0000_0008 | Not all the necessary controlled system properties were defined for the selected method of calculation. Instead, the PID parameters were calculated using the TIR.TuneRule = 3 method. |
| 0000_0010 | The operating mode could not be changed because Reset = TRUE or ManualEnable = TRUE. |
| 0000_0020 | The cycle time of the calling OB limits the sampling time of the PID algorithm.   Improve results by using shorter OB cycle times. |
| 0000_0040 | The process value exceeded one of its warning limits. |
| 0000_0080 | Invalid value at Mode. The operating mode is not switched. |
| 0000_0100 | The manual value was limited to the limits of the controller output. |
| 0000_0200 | The specified rule for tuning is not supported. No PID parameters are calculated. |
| 0000_1000 | The substitute output value cannot be reached because it is outside the output value limits. |

The following warnings are deleted as soon as the cause is eliminated:

- 16#0000_0001
- 16#0000_0004
- 16#0000_0008
- 16#0000_0040
- 16#0000_0100

All other warnings are cleared with a rising edge at Reset or ErrorAck.

### Tag IntegralResetMode as of V2 (S7-1200, S7-1500)

The IntegralResetMode tag determines how the integral action PIDCtrl.IntegralSum is pre-assigned:

- When switching from "Inactive" operating mode to "Automatic mode"
- With edge TRUE -> FALSE at parameter Reset and parameter Mode = 3

This setting only works for one cycle and is only effective if the integral action is activated (Retain.CtrlParams.Ti > 0.0 tag).

| IntegralResetMode | Description |
| --- | --- |
| 0 | Smooth  The value of PIDCtrl.IntegralSum is pre-assigned so that the switchover is bumpless, which means "Automatic mode" starts with the output value = 0.0 (parameter Output) and there is no jump of the output value regardless of the control deviation (setpoint – actual value). |
| 1 | Delete  We recommend setting the weighting of the proportional action (Retain.CtrlParams.PWeighting) to 1.0 if this option is used.   The value of PIDCtrl.IntegralSum is deleted. Any control deviation will cause a jump change of the output value. The direction of the output value jump depends on the configured weighting of the proportional action (Retain.CtrlParams.PWeighting tag) and the control deviation:   - Proportional action weighting = 1.0:    Output value jump and control deviation have identical signs.  Example: If the actual value is smaller than the setpoint (positive control deviation), the output value jumps to a positive value. - Proportional action weighting < 1.0:    For large control deviations, the output value jump and control deviation have identical signs.  Example: If the actual value is much smaller than the setpoint (positive control deviation), the output value jumps to a positive value.    For small control deviations, the output value jump and control deviation have different signs.  Example: If the actual value is just below the setpoint (positive control deviation), the output value jumps to a negative value. This is usually not desirable, because it results in a temporary increase in the control deviation.    The smaller the configured weighting of the proportional action, the greater the control deviation must be to receive an output value jump with identical sign.   We recommend setting the weighting of the proportional action (Retain.CtrlParams.PWeighting) to 1.0 when this option is used. Otherwise, you may experience the undesirable behavior described for small control deviations. Alternatively, you can also use IntegralResetMode = 4. This option guarantees identical signs of the output value jump and control deviation independent of the configured weighting of the proportional action and the control deviation. |
| 2 | Hold  The value of PIDCtrl.IntegralSum is not changed. You can define a new value using the user program. |
| 3 | Pre-assign   The value of PIDCtrl.IntegralSum is automatically pre-assigned as if Output = OverwriteInitialOutputValue in the last cycle. |
| 4 | Like setpoint change (only for PID_Compact with version ≥ 2.3)   The value of PIDCtrl.IntegralSum is automatically pre-assigned so that a similar output value jump results as for a PI controller in automatic mode in case of a setpoint change from the current actual value to the current setpoint.  Any control deviation will cause a jump of the output value. Output value jump and control deviation have identical signs.  Example: If the actual value is smaller than the setpoint (positive control deviation), the output value jumps to a positive value. This is independent of the configured weighting of the proportional action and the control deviation. |

If IntegralResetMode is assigned a value outside the valid value range, PID_Compact behaves as with the pre-assignment of IntegralResetMode:

- PID_Compact up to V2.2: IntegralResetMode = 1
- PID_Compact as of V2.3: IntegralResetMode = 4

All statements made above regarding the sign of the output value jump are based on a normal control logic (Config.InvertControl = FALSE tag). With an inverted control logic (Config.InvertControl = TRUE), the output value jump will have a reverse sign.

### Example program for PID_Compact V2 (S7-1200, S7-1500)

In the following example, you are controlling temperature values with the technology object of the instruction "PID_Compact". The temperature values are simulated based on a block which simulates a delay element of the third order (PT3 element). The PID parameters of the technology object can be set automatically via the pretuning.

![Figure](images/166086893323_DV_resource.Stream@PNG-en-US.png)

#### Data storage

Create seven tags in a global data block for storage of the interconnection data.

![Data storage](images/166086835979_DV_resource.Stream@PNG-de-DE.png)

#### Interconnection of the parameters

You call the following interconnections in a cyclic interrupt OB.

**Network 1**: You interconnect the parameters of the instruction "PID_Compact" as follows.

![Interconnection of the parameters](images/166086839947_DV_resource.Stream@PNG-de-DE.png)

**Network 2**: You interconnect the parameters of the block simulating the temperature values "SLI_PROC_C" as follows.

![Interconnection of the parameters](images/166086856715_DV_resource.Stream@PNG-de-DE.png)

#### Technology object

You configure the technology object with the properties of the instruction "PID_Compact" or by using the path Technology object > Configuration. The controller type and the input/output parameters are important for the example. With the controller type, you make a preselection for the unit of the value to the controlled. In this example, "Temperature" with the unit "°C" is used as controller type. The parameters of the "PID_Compact" are already interconnected with global tags. Therefore, the information on use of the parameters Input and Output is sufficient.

![Technology object](images/166086885387_DV_resource.Stream@PNG-de-DE.png)

#### Procedure for starting the control

After the download to the CPU the PID_Compact is in manual mode with manual value 0.0. To start the control, follow these steps:

1. Open the Commissioning of the technology object "SLI_Tech_PID_Compact".
2. Click the "Start" button in the "Measurement" area.

   ![Procedure for starting the control](images/166086860683_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure for starting the control](images/166086860683_DV_resource.Stream@PNG-de-DE.png)

   Measurement starts and PID_Compact can be activated.
3. Pretuning is selected.

   Click the "Start" button in the "Tuning mode" area.

   A pretuning is performed. The PID parameters are automatically adjusted to the process. After the completion of the pretuning PID_Compact switches to automatic mode.

**Note**

**Alternative to start PID_Compact**

Alternatively, you can switch PID_Compact to automatic mode in the "Online status of controller" area with the "Stop PID_Compact" / "Start PID_Compact" without pretuning. In this case the controller uses default values for the PID parameters and shows a worse controller behavior for the application case.

#### Procedure for stopping control

To stop and exit PID_Compact and the program, follow these steps:

1. Click the "Stop PID_Compact" button in the technology object "SLI_Tech_PID_Compact" in the "Online status of controller" area.

   ![Procedure for stopping control](images/166086864651_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure for stopping control](images/166086864651_DV_resource.Stream@PNG-de-DE.png)

   The instruction "PID_Compact" exits the control and outputs the value "0.0" as manipulated variable.
2. Click the "Stop" button in the "Measurement" area.
3. To set the process value immediately to the value "0.0", follow these steps:

   In the block "SLI_OB_PID_Compact", set the "resetAll" tag to the value "TRUE", and then to the value "FALSE".

#### "PID_Compact" instruction

The setpoint for the temperature that is to be controlled is specified at the parameter Setpoint ("setpoint"). The control is started when the instruction "PID_Compact" was started with the technology object. The instruction "PID_Compact" outputs a manipulated variable at the output parameter Output ("outputValue"). The process value of the temperature is transferred to the instruction "PID_Compact" with the input parameter Input ("inputValue").

The instruction "PID_Compact" adjusts the manipulated variable ("outputValue") depending on the history of the difference between setpoint ("setpoint") and process value ("inputValue") . The process is repeated so that the process value ("inputValue") approaches the setpoint ("setpoint") through the manipulated variable ("outputValue").

The current operating mode of the instruction "PID_Compact" is displayed at the output parameter State ("state"). After pretuning (the value of "state" is "1"), the PID_Compact switches to automatic mode (the value is "3").

The output parameter Error ("error") currently shows that no error is pending. The output parameter ErrorBits ("errorBits") provides information on the error type in case of error. If an error occurs, this can be acknowledged in the technology object, in the optimization status area with the "ErrorAck" button.

!["PID_Compact" instruction](images/166086881419_DV_resource.Stream@PNG-de-DE.png)

#### "SLI_PROC_C" block

The "SLI_PROC_C" block simulates the process value ("inputValue") of the rising temperature of a plant. The block "SLI_PROC_C" contains the manipulated variable of the controller ("outputValue) and simulates the temperature behavior of the process. This temperature is fed as process value ("inputValue") into the controller.

A change in the values of the "resetAll" tag (of the comRst parameter) has the following effects:

| Parameter comRst ("resetAll") | The instruction "PID_Compact" is running | The instruction "PID_Compact" was stopped |
| --- | --- | --- |
| comRst ("resetAll") remains set to the value "FALSE" | The "SLI_PROC_C" block outputs a new process value ("inputValue") based on a manipulated variable ("outputValue"). | The "SLI_PROC_C" block does not receive a manipulated variable > "0.0", but it still outputs a new process value > "0.0". |
| comRst ("resetAll"): Change from "FALSE" to the value "TRUE" | Both manipulated variable ("outputValue") and output process value ("inputValue") are reset to "0.0". | The output process value ("inputValue") / the temperature of the "SLI_PROC_C" block is reset to "0.0". |
| comRst ("resetAll"): Change from "TRUE" to the value "FALSE" | Temperature control starts again. | The output process value / the temperature ("inputValue") remains "0.0". |

!["SLI_PROC_C" block](images/166086889355_DV_resource.Stream@PNG-de-DE.png)

#### Program code

You can find additional information about the program code for the above-named example under the keyword "Sample Library for Instructions".

## PID_Compact V1 (S7-1200)

This section contains information on the following topics:

- [Description of PID_Compact V1 (S7-1200)](#description-of-pid_compact-v1-s7-1200)
- [Input parameters of PID_Compact V1 (S7-1200)](#input-parameters-of-pid_compact-v1-s7-1200)
- [Output parameters of PID_Compact V1 (S7-1200)](#output-parameters-of-pid_compact-v1-s7-1200)
- [Static tags of PID_Compact V1 (S7-1200)](#static-tags-of-pid_compact-v1-s7-1200)
- [Parameters State and sRet.i_Mode V1 (S7-1200)](#parameters-state-and-sreti_mode-v1-s7-1200)
- [Parameter Error V1 (S7-1200)](#parameter-error-v1-s7-1200)
- [Reset V1 parameter (S7-1200)](#reset-v1-parameter-s7-1200)
- [Tag sd_warning V1 (S7-1200)](#tag-sd_warning-v1-s7-1200)
- [Tag i_Event_SUT V1 (S7-1200)](#tag-i_event_sut-v1-s7-1200)
- [Tag i_Event_TIR V1 (S7-1200)](#tag-i_event_tir-v1-s7-1200)

### Description of PID_Compact V1 (S7-1200)

#### Description

The PID_Compact instruction provides a PID controller with integrated tuning for automatic and manual mode.

#### Call

PID_Compact is called in the constant interval of the cycle time of the calling OB (preferably in a cyclic interrupt OB).

#### Download to device

The actual values of retentive tags are only updated when you download PID_Compact completely.

[Downloading technology objects to device](Configuring%20a%20software%20controller.md#downloading-technology-objects-to-device)

#### Startup

At the startup of the CPU, PID_Compact starts in the operating mode that was last active. To retain PID_ Compact in "Inactive" mode, set sb_RunModeByStartup = FALSE.

#### Monitoring of the sampling time PID_Compact

Ideally, the sampling time is equivalent to the cycle time of the calling OB. The PID_Compact instruction measures the time interval between two calls. This is the current sampling time. On every switchover of operating mode and during the initial startup, the mean value is formed from the first 10 sampling times. If the current sampling time deviates too much from this mean value, Error = 0800 hex occurs and PID_Compact switches to "Inactive" mode.

PID_Compact as of Version 1.1 is set to "Inactive" mode during controller tuning under the following conditions:

- New mean value >= 1.1 x old mean value
- New mean value <= 0.9 x old mean value

In automatic mode, PID_Compact, as of Version 1.1, is set to "Inactive" mode under the following conditions:

- New mean value >= 1.5 x old mean value
- New mean value <= 0.5 x old mean value

During controller tuning and in automatic mode, PID_Compact 1.0 is set to "Inactive" operating mode under the following conditions:

- New mean value >= 1.1 x old mean value
- New mean value <= 0.9 x old mean value
- Current sampling time >= 1.5 x current mean value
- Current sampling time <= 0.5 x current mean value

#### Sampling time of the PID algorithm

The controlled system needs a certain amount of time to respond to changes in the output value. It is therefore not advisable to calculate the output value in every cycle. The sampling time of the PID algorithm represents the time between two calculations of the output value. It is calculated during tuning and rounded to a multiple of the cycle time. All other functions of PID_Compact are executed at every call.

#### PID algorithm

PID_Compact is a PIDT1 controller with anti-windup and weighting of the proportional and derivative actions. The following equation is used to calculate the output value.

![PID algorithm](images/172252714123_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| **Symbol** | **Description** |
| y | Output value |
| K<sub>p</sub> | Proportional gain |
| s | Laplace operator |
| b | Proportional action weighting |
| w | Setpoint |
| x | Process value |
| T<sub>I</sub> | Integration time |
| a | Derivative delay coefficient (T1 = a × T<sub>D</sub>) |
|  | Derivative action time |
| c | Derivative action weighting |

#### Block diagram of PID_Compact

![Block diagram of PID_Compact](images/166086899339_DV_resource.Stream@PNG-de-DE.png)

#### Block diagram of PIDT1 with anti-windup

![Block diagram of PIDT1 with anti-windup](images/166014208907_DV_resource.Stream@PNG-en-US.png)

#### Responses in the event of an error

If errors occur, they are output in parameter Error, and PID_Compact changes to "Inactive" mode. Reset the errors using the Reset parameter.

#### Control logic

An increase of the output value is generally intended to cause an increase in the process value. This is referred to as a normal control logic. For cooling and discharge control systems, it may be necessary to invert the control logic. PID_Compact does not work with negative proportional gain. If InvertControl = TRUE, an increasing control deviation causes a reduction in the output value. The control logic is also taken into account during pretuning and fine tuning.

---

**See also**

[Control mode V1 (S7-1200, S7-1500)](Using%20PID_Compact%20%28S7-1200%2C%20S7-1500%29.md#control-mode-v1-s7-1200-s7-1500)

### Input parameters of PID_Compact V1 (S7-1200)

| Parameter | Data type | Default | Description |
| --- | --- | --- | --- |
| Setpoint | REAL | 0.0 | Setpoint of the PID controller in automatic mode |
| Input | REAL | 0.0 | A variable of the user program is used as source for the process value.   If you are using parameter Input, then sPid_Cmpt.b_Input_PER_On = FALSE must be set. |
| Input_PER | WORD | W#16#0 | Analog input as the source of the process value   If you are using parameter Input_PER, then sPid_Cmpt.b_Input_PER_On = TRUE must be set. |
| ManualEnable | BOOL | FALSE | - A FALSE -> TRUE edge selects "Manual mode", while State = 4, sRet.i_Mode remains unchanged. - A TRUE -> FALSE edge selects the most recently active operating mode, State =sRet.i_Mode.  A change of sRet.i_Mode will not take effect during ManualEnable = TRUE. The change of sRet.i_Mode will only be considered upon a TRUE -> FALSE edge at ManualEnable .   **PID_Compact V1.2**  **and**  **PID_Compact V1.0**   If at start of the CPU ManualEnable = TRUE, PID_Compact starts in manual mode. A rising edge (FALSE > TRUE) at ManualEnable is not necessary.   **PID_Compact V1.1**   At the start of the CPU, PID_Compact only switches to manual mode with a rising edge (FALSE->TRUE) at ManualEnable . Without rising edge, PID_Compact starts in the last operating mode in which ManualEnable was FALSE. |
| ManualValue | REAL | 0.0 | Manual value  This value is used as the output value in manual mode. |
| Reset | BOOL | FALSE | The [Reset parameter](#reset-v1-parameter-s7-1200) restarts the controller. |

### Output parameters of PID_Compact V1 (S7-1200)

| Parameter | Data type | Default | Description |
| --- | --- | --- | --- |
| ScaledInput | REAL | 0.0 | Output of the scaled process value |
| Outputs "Output", "Output_PER", and "Output_PWM" can be used concurrently. |  |  |  |
| Output | REAL | 0.0 | Output value in REAL format |
| Output_PER | WORD | W#16#0 | Analog output value |
| Output_PWM | BOOL | FALSE | Pulse-width-modulated output value  The output value is formed by minimum On and Off times. |
| SetpointLimit_H | BOOL | FALSE | If SetpointLimit_H = TRUE, the setpoint absolute high limit is reached. The setpoint in the CPU is limited to the configured setpoint absolute high limit. The configured process value absolute high limit is the default for the setpoint high limit.  If you set sPid_Cmpt.r_Sp_Hlm to a value within the process value limits, this value is used as the setpoint high limit. |
| SetpointLimit_L | BOOL | FALSE | If SetpointLimit_L = TRUE, the setpoint absolute low limit has been reached. In the CPU, the setpoint is limited to the configured setpoint absolute low limit. The configured process value absolute low limit is the default setting for the setpoint low limit.  If you set sPid_Cmpt.r_Sp_Llm to a value within the process value limits, this value is used as the setpoint low limit. |
| InputWarning_H | BOOL | FALSE | If InputWarning_H = TRUE, the process value has reached or exceeded the warning high limit. |
| InputWarning_L | BOOL | FALSE | If InputWarning_L = TRUE, the process value has reached or fallen below the warning low limit. |
| State | INT | 0 | The [State parameter](#parameters-state-and-sreti_mode-v1-s7-1200) shows the current operating mode of the PID controller. To change the operating mode, use variable sRet.i_Mode.   - State = 0: Inactive - State = 1: pretuning - State = 2: fine tuning - State = 3: Automatic mode - State = 4: Manual mode |
| Error | DWORD | W#16#0 | The [Error parameter](#parameter-error-v1-s7-1200) indicates the error messages.   Error = 0000: No error pending. |

### Static tags of PID_Compact V1 (S7-1200)

> **Note**
>
> You must not change tags that are not listed. These are used for internal purposes only.
>
> Change the tags identified with <sup>(1)</sup> only in "Inactive" mode to prevent malfunction of the PID controller. "Inactive" mode is forced by setting the "sRet.i_Mode" tag to "0".

| Tag | Data type | Default | Description |
| --- | --- | --- | --- |
| sb_GetCycleTime | BOOL | TRUE | If sb_GetCycleTime = TRUE, the automatic determination of the cycle time is started. CycleTime.StartEstimation = FALSE once measurement is complete. |
| sb_EnCyclEstimation | BOOL | TRUE | If sb_EnCyclEstimation = TRUE, the PID_Compact sampling time is calculated. |
| sb_EnCyclMonitoring | BOOL | TRUE | If sb_EnCyclMonitoring = FALSE, the PID_Compact sampling time is not monitored. If it is not possible to execute PID_Compact within the sampling time, an 0800 error is not output and PID_Compact does not change to "Inactive" mode. |
| sb_RunModeByStartup | BOOL | TRUE | Activate Mode after CPU restart  If sb_RunModeByStartup = FALSE, the controller remains inactive after a CPU startup.   If sb_RunModeByStartup = TRUE, the controller returns to the last active operating mode after a CPU restart. |
| si_Unit | INT | 0 | Unit of measurement of the process value and setpoint, e.g., ºC, or ºF. |
| si_Type | INT | 0 | Physical quantity of the process value and setpoint, e.g., temperature. |
| sd_Warning | DWORD | DW#16#0 | [Variable sd_warning](#tag-sd_warning-v1-s7-1200) displays the warnings generated since the reset, or since the last change of the operating mode. |
| sBackUp.r_Gain | REAL | 1.0 | Saved proportional gain  You can reload values from the sBackUp structure with sPid_Cmpt.b_LoadBackUp = TRUE. |
| sBackUp.r_Ti | REAL | 20.0 | Saved integral action time [s] |
| sBackUp.r_Td | REAL | 0.0 | Saved derivative action time [s] |
| sBackUp.r_A | REAL | 0.0 | Saved derivative delay coefficient |
| sBackUp.r_B | REAL | 0.0 | Saved proportional action weighting factor |
| sBackUp.r_C | REAL | 0.0 | Saved derivative action weighting factor |
| sBackUp.r_Cycle | REAL | 1.0 | Saved sampling time of PID algorithm |
| sPid_Calc.r_Cycle<sup>(1)</sup> | REAL | 0.1 | Sampling time of the PID_Compact instruction  r_Cycle is determined automatically and is usually equivalent to the cycle time of the calling OB. |
| sPid_Calc.b_RunIn | BOOL | FALSE | - b_RunIn = FALSE   Pretuning is started when fine tuning is started from inactive or manual mode. If the requirements for pretuning are not met, PID_Compact reacts as if b_RunIn = TRUE.   If fine tuning is started from automatic mode, the system uses the existing PID parameters to control to the setpoint.   Only then will fine tuning start. If pretuning is not possible, PID_Compact switches to "Inactive" mode. - b_RunIn = TRUE   The pretuning is skipped. PID_3Compact tries to reach the setpoint with minimum or maximum output value. This can produce increased overshoot. Fine tuning then starts automatically.   b_RunIn is set to FALSE after fine tuning. |
| sPid_Calc.b_CalcParamSUT | BOOL | FALSE | The parameters for pretuning will be recalculated if b_CalcParamSUT = TRUE. This enables you to change the parameter calculation method without having to repeat controller tuning.  b_CalcParamSUT is set to FALSE after the calculation. |
| sPid_Calc.b_CalcParamTIR | BOOL | FALSE | The parameters for fine tuning will be recalculated if b_CalcParamTIR = TRUE. This enables you to change the parameter calculation method without having to repeat controller tuning.  b_CalcParamTIR will be set to FALSE after calculation. |
| sPid_Calc.i_CtrlTypeSUT | INT | 0 | Methods used to calculate parameters during pretuning:  - i_CtrlTypeSUT = 0: PID according to Chien, Hrones and Reswick - i_CtrlTypeSUT = 1: PI according to Chien, Hrones and Reswick |
| sPid_Calc.i_CtrlTypeTIR | INT | 0 | Methods used to calculate parameters during fine tuning:  - i_CtrlTypeTIR = 0: PID automatic - i_CtrlTypeTIR = 1: PID fast (faster control response with higher amplitudes of the output value than with i_CtrlTypeTIR = 2) - i_CtrlTypeTIR = 2: PID slow (slower control response with lower amplitudes of the output value than with i_CtrlTypiTIR = 1) - i_CtrlTypeTIR = 3: Ziegler-Nichols PID - i_CtrlTypeTIR = 4: Ziegler-Nichols PI - i_CtrlTypeTIR = 5: Ziegler-Nichols P   To be able to repeat the calculation of the PID parameters with b_CalcParamTIR and i_CtrlTypeTIR = 0, 1 or 2, the previous fine tuning also has to have been executed with i_CtrlTypeTIR = 0, 1 or 2.  If this is not the case, i_CtrlTypeTIR = 3 is used.  The recalculation of the PID parameters with b_CalcParamTIR and i_CtrlTypeTIR = 3, 4 or 5 is always possible. |
| sPid_Calc.r_Progress | REAL | 0.0 | Progress of tuning as a percentage (0.0 - 100.0) |
| sPid_Cmpt.r_Sp_Hlm<sup>(1)</sup> | REAL | +3.402822e+38 | High limit of setpoint  If you configure sPid_Cmpt.r_Sp_Hlm outside the process value limits, the configured process value absolute high limit is used as the setpoint high limit.   If you configure sPid_Cmpt.r_Sp_Hlm within the process value limits, this value is used as the setpoint high limit. |
| sPid_Cmpt.r_Sp_Llm<sup>(1)</sup> | REAL | -3.402822e+38 | Low limit of the setpoint  If you set sPid_Cmpt.r_Sp_Llm outside the process value limits, the configured process value absolute low limit is used as the setpoint low limit.  If you set sPid_Cmpt.r_Sp_Llm within the process value limits, this value is used as the setpoint low limit. |
| sPid_Cmpt.r_Pv_Norm_IN_1<sup>(1)</sup> | REAL | 0.0 | Scaling Input_PER low  Input_PER is converted to a percentage based on the two value pairs r_Pv_Norm_OUT_1, r_Pv_Norm_IN_1 and r_Pv_Norm_OUT_2, r_Pv_Norm_IN_2 of the sPid_Cmpt structure. |
| sPid_Cmpt.r_Pv_Norm_IN_2<sup>(1)</sup> | REAL | 27648.0 | Scaling Input_PER high  Input_PER is converted to a percentage based on the two value pairs r_Pv_Norm_OUT_1, r_Pv_Norm_IN_1 and r_Pv_Norm_OUT_2, r_Pv_Norm_IN_2 of the sPid_Cmpt structure. |
| sPid_Cmpt.r_Pv_Norm_OUT_1<sup>(1)</sup> | REAL | 0.0 | Scaled low process value   Input_PER is converted to a percentage based on the two value pairs r_Pv_Norm_OUT_1, r_Pv_Norm_IN_1 and r_Pv_Norm_OUT_2, r_Pv_Norm_IN_2 of the sPid_Cmpt structure. |
| sPid_Cmpt.r_Pv_Norm_OUT_2<sup>(1)</sup> | REAL | 100.0 | Scaled high process value   Input_PER is converted to a percentage based on the two value pairs r_Pv_Norm_OUT_1, r_Pv_Norm_IN_1 and r_Pv_Norm_OUT_2, r_Pv_Norm_IN_2 of the sPid_Cmpt structure. |
| sPid_Cmpt.r_Lmn_Hlm<sup>(1)</sup> | REAL | 100.0 | Output value high limit for output parameter "Output" |
| sPid_Cmpt.r_Lmn_Llm<sup>(1)</sup> | REAL | 0.0 | Low output value limit for output parameter "Output" |
| sPid_Cmpt.b_Input_PER_On<sup>(1)</sup> | BOOL | TRUE | If b_Input_PER_On = TRUE, the Input_PER parameter is used. If b_Input_PER_On = FALSE, the Input parameter is used. |
| sPid_Cmpt.b_LoadBackUp | BOOL | FALSE | Activate the back-up parameter set. If an optimization has failed, you can reactivate the previous PID parameters by setting this bit. |
| sPid_Cmpt.b_InvCtrl<sup>(1)</sup> | BOOL | FALSE | Invert control logic  If b_InvCtrl = TRUE, an increasing control deviation causes a reduction in the output value. |
| sPid_Cmpt.r_Lmn_Pwm_PPTm<sup>(1)</sup> | REAL | 0.0 | The minimum ON time of the pulse width modulation in seconds is rounded to  r_Lmn_Pwm_PPTm = r_Cycle or r_Lmn_Pwm_PPTm = n*r_Cycle |
| sPid_Cmpt.r_Lmn_Pwm_PBTm<sup>(1)</sup> | REAL | 0.0 | The minimum OFF time of the pulse width modulation in seconds is rounded to  r_Lmn_Pwm_PBTm = r_Cycle or r_Lmn_Pwm_PBTm = n*r_Cycle |
| sPid_Cmpt.r_Pv_Hlm<sup>(1)</sup> | REAL | 120.0 | High limit of the process value  At the I/O input, the process value can be a maximum of 18% higher than the standard range (overrange). An error is no longer reported for a violation of the "Process value high limit". Only a wire-break and a short-circuit are recognized and the PID_Compact switches to "Inactive" mode.  r_Pv_Hlm > r_Pv_Llm |
| sPid_Cmpt.r_Pv_Llm<sup>(1)</sup> | REAL | 0.0 | Low limit of the process value  r_Pv_Llm < r_Pv_Hlm |
| sPid_Cmpt.r_Pv_HWrn<sup>(1)</sup> | REAL | +3.402822e+38 | Warning high limit of the process value  If you set r_Pv_HWrn outside the process value limits, the configured process value absolute high limit is used as the warning high limit.   If you configure r_Pv_HWrn within the process value limits, this value is used as the warning high limit.  r_Pv_HWrn > r_Pv_LWrn  r_Pv_HWrn ≤ r_Pv_Hlm |
| sPid_Cmpt.r_Pv_LWrn<sup>(1)</sup> | REAL | -3.402822e+38 | Warning low limit of the process value  If you set r_Pv_LWrn outside the process value limits, the configured process value absolute low limit is used as the warning low limit.   If you configure r_Pv_LWrn within the process value limits, this value is used as the warning low limit.  r_Pv_LWrn < r_Pv_HWrn  r_Pv_LWrn ≥ r_Pv_LWrn |
| sPidCalc.i_Ctrl_IOutv<sup>(1)</sup> | REAL | 0.0 | Current integral action |
| sParamCalc.i_Event_SUT | INT | 0 | [Variable i_Event_SUT](#tag-i_event_sut-v1-s7-1200) indicates the current phase of "pretuning": |
| sParamCalc.i_Event_TIR | INT | 0 | [Variable i_Event_TIR](#tag-i_event_tir-v1-s7-1200) indicates the current phase of "fine tuning": |
| sRet.i_Mode | INT | 0 | The operating mode is changed edge-triggered.  The following operating mode is enabled on a change to  - i_Mode = 0: "Inactive" mode (controller stop) - i_Mode = 1: "Pretuning" mode - i_Mode = 2: "Fine tuning" mode - i_Mode = 3: "Automatic" mode - i_Mode = 4: "Manual" mode   i_Mode is retentive. |
| sRet.r_Ctrl_Gain<sup>(1)</sup> | REAL | 1.0 | Active proportional gain  Gain is retentive. |
| sRet.r_Ctrl_Ti<sup>(1)</sup> | REAL | 20.0 | - r_Ctrl_Ti > 0.0: Active integral action time - r_Ctrl_Ti = 0.0: Integral action is deactivated  r_Ctrl_Ti is retentive. |
| sRet.r_Ctrl_Td<sup>(1)</sup> | REAL | 0.0 | - r_Ctrl_Td > 0.0: Active derivative action time - r_Ctrl_Td = 0.0: Derivative action is deactivated  r_Ctrl_Td is retentive. |
| sRet.r_Ctrl_A<sup>(1)</sup> | REAL | 0.0 | Active derivative delay coefficient  r_Ctrl_A is retentive. |
| sRet.r_Ctrl_B<sup>(1)</sup> | REAL | 0.0 | Active proportional action weighting  r_Ctrl_B is retentive. |
| sRet.r_Ctrl_C<sup>(1)</sup> | REAL | 0.0 | Active derivative action weighting  r_Ctrl_C is retentive. |
| sRet.r_Ctrl_Cycle<sup>(1)</sup> | REAL | 1.0 | Active sampling time of the PID algorithm  r_Ctrl_Cycle is calculated during tuning and rounded to an integer multiple of r_Cycle.  r_Ctrl_Cycle is used as time period of the pulse width modulation.  r_Ctrl_Cycle is retentive. |

---

**See also**

[Downloading technology objects to device](Configuring%20a%20software%20controller.md#downloading-technology-objects-to-device)

### Parameters State and sRet.i_Mode V1 (S7-1200)

#### Correlation of the parameters

The State parameter indicates the current operating mode of the PID controller. You cannot modify the State parameter.

You need to modify the sRet.i_Mode tag to change the operating mode. This also applies when the value for the new operating mode is already in sRet.i_Mode. First set sRet.i_Mode = 0 and then sRet.i_Mode = 3. Provided the current operating mode of the controller supports this change, State is set to the value of sRet.i_Mode.

When PID_Compact automatically switches the operating mode, the following applies: State != sRet.i_Mode.

Examples:

- Successful pretuning  
  State = 3 and sRet.i_Mode = 1
- Error  
  State = 0 and sRet.i_Mode remains at the same value, e.g sRet.i_Mode = 3
- ManualEnalbe = TRUE  
  State = 4 and sRet.i_Mode remain at the previous value, for example, sRet.i_Mode = 3

  > **Note**
  >
  > You wish to repeat successful fine tuning without exiting automatic mode with i_Mode = 0.
  >
  > Setting sRet.i_Mode to an invalid value such as 9999 for one cycle has no effect on State. Set Mode = 2 in the next cycle. You can generate a change to sRet.i_Mode without first switching to "inactive" mode.

#### Meaning of values

| State / sRet.i_Mode | Description of the operating mode |
| --- | --- |
| 0 | Inactive  The controller is switched off.   The controller was in "inactive" mode before pretuning was performed.  The PID controller will change to "inactive" mode when running if an error occurs or if the "Deactivate controller" icon is clicked in the commissioning window. |
| 1 | Pretuning  The pretuning determines the process response to a jump of the output value and searches for the point of inflection. The optimized PID parameters are calculated as a function of the maximum rate of rise and dead time of the controlled system.   Pretuning requirements:  - The controller is in inactive mode or manual mode - ManualEnable = FALSE - The process value must not be too close to the setpoint.   |Setpoint - Input| > 0.3 * |sPid_Cmpt.r_Pv_Hlm - sPid_Cmpt.r_Pv_Llm| and   |Setpoint - Input| > 0.5 * |Setpoint| - The setpoint may not be changed during pretuning.   The higher the stability of the process value, the easier it is to calculate the PID parameters and increase precision of the result. Noise on the process value can be tolerated as long as the rate of rise of the process value is significantly higher compared to the noise.   PID parameters are backed up before they are recalculated and can be reactivated with sPid_Cmpt.b_LoadBackUp.  There is a change to automatic mode following successful pretuning and to "inactive" mode following unsuccessful pretuning.  The phase of pretuning is indicated with [Tag i_Event_SUT V1](#tag-i_event_sut-v1-s7-1200). |
| 2 | Fine tuning  Fine tuning generates a constant, limited oscillation of the process value. The PID parameters are optimized based on the amplitude and frequency of this oscillation. The differences between the process response during pretuning and fine tuning are analyzed. All PID parameters are recalculated on the basis of the findings. PID parameters from fine tuning usually have better master control and disturbance behavior than PID parameters from pretuning.  PID_Compact automatically attempts to generate an oscillation greater than the noise of the process value. Fine tuning is only minimally influenced by the stability of the process value.   PID parameters are backed up before they are recalculated and can be reactivated with sPid_Cmpt.b_LoadBackUp.  Requirements for fine tuning:  - No disturbances are expected. - The setpoint and the process value lie within the configured limits. - The setpoint may not be changed during fine tuning. - ManualEnable = FALSE - Automatic (State = 3), inactive (State = 0) or manual (State = 4) mode   Fine tuning proceeds as follows when started in:  - Automatic mode (State = 3)   Start fine tuning in automatic mode if you wish to improve the existing PID parameters using controller tuning.   PID_Comact will regulate using the existing PID parameters until the control loop has stabilized and the requirements for fine tuning have been met. Only then will fine tuning start. - Inactive (State = 0) or manual (State = 4) mode   If the requirements for pretuning are met, pretuning is started. The PID parameters established will be used for adjustment until the control loop has stabilized and the requirements for fine tuning have been met. Only then will fine tuning start. If pretuning is not possible, PID_Compact will change to "Inactive" mode.   An attempt is made to reach the setpoint with a minimum or maximum output value if the process value for pretuning is already too near the setpoint or sPid_Calc.b_RunIn = TRUE. This can produce increased overshoot.   The controller will change to "automatic mode" after successfully completed "fine tuning" and to "inactive" mode if "fine tuning" has not been successfully completed.  The "Fine tuning" phase is indicated with [Tag i_Event_TIR V1](#tag-i_event_tir-v1-s7-1200). |
| 3 | Automatic mode  In automatic mode, PID_Compact corrects the controlled system in accordance with the parameters specified.  The controller changes to automatic mode if one the following conditions is fulfilled:  - Pretuning successfully completed - Fine tuning successfully completed - Change of variable sRet.i_Mode to the value 3.   After CPU startup or change from Stop to RUN mode, PID_Compact will start in the most recently active operating mode. To retain PID_Compact in "Inactive" mode, set sb_RunModeByStartup = FALSE. |
| 4 | Manual mode  In manual mode, you specify a manual output value in the ManualValue parameter.  This operating mode is enabled if sRet.i_Mode = 4, or at the rising edge on ManualEnable. If ManualEnable changes to TRUE, only State will change. sRet.i_Mode will retain its current value. PID_Compact will return to the previous operating mode upon a falling edge at ManualEnable.  The change to automatic mode is bumpless. |

---

**See also**

[Output parameters of PID_Compact V1 (S7-1200)](#output-parameters-of-pid_compact-v1-s7-1200)
  
[Pretuning V1 (S7-1200, S7-1500)](Using%20PID_Compact%20%28S7-1200%2C%20S7-1500%29.md#pretuning-v1-s7-1200-s7-1500)
  
[Fine tuning V1 (S7-1200, S7-1500)](Using%20PID_Compact%20%28S7-1200%2C%20S7-1500%29.md#fine-tuning-v1-s7-1200-s7-1500)
  
["Manual" mode V1 (S7-1200, S7-1500)](Using%20PID_Compact%20%28S7-1200%2C%20S7-1500%29.md#manual-mode-v1-s7-1200-s7-1500)
  
[Tag i_Event_SUT V1 (S7-1200)](#tag-i_event_sut-v1-s7-1200)
  
[Tag i_Event_TIR V1 (S7-1200)](#tag-i_event_tir-v1-s7-1200)

### Parameter Error V1 (S7-1200)

If several errors are pending simultaneously, the values of the error codes are displayed with binary addition. The display of error code 0003, for example, indicates that the errors 0001 and 0002 are pending simultaneously.

| Error  (DW#16#...) | Description |
| --- | --- |
| 0000 | There is no error. |
| 0001 | The "Input" parameter is outside the process value limits.  - Input > sPid_Cmpt.r_Pv_Hlm or - Input < sPid_Cmpt.r_Pv_Llm   You cannot move the actuator again until you eliminate the error. |
| 0002 | Invalid value at "Input_PER" parameter. Check whether an error is pending at the analog input. |
| 0004 | Error during fine tuning. Oscillation of the process value could not be maintained. |
| 0008 | Error at start of pretuning. The process value is too close to the setpoint. Start fine tuning. |
| 0010 | The setpoint was changed during tuning. |
| 0020 | Pretuning is not permitted in automatic mode or during fine tuning. |
| 0080 | Error during pretuning. The output value limits are not configured correctly or the actual value does not react as expected.  Check whether the limits of the output value are configured correctly and match the control logic.  Also make sure that the actual value does not oscillate strongly before starting pretuning. |
| 0100 | Error during tuning resulted in invalid parameters. |
| 0200 | Invalid value at "Input" parameter: Value has an invalid number format. |
| 0400 | Calculation of output value failed. Check the PID parameters. |
| 0800 | Sampling time error: PID_Compact is not called within the sampling time of the cyclic interrupt OB.  If this error occurred during simulation with PLCSIM, see the notes under [Simulating PID_Compact V1 with PLCSIM](Using%20PID_Compact%20%28S7-1200%2C%20S7-1500%29.md#simulating-pid_compact-v1-with-plcsim-s7-1200-s7-1500). |
| 1000 | Invalid value at "Setpoint" parameter: Value has an invalid number format. |

---

**See also**

[Output parameters of PID_Compact V1 (S7-1200)](#output-parameters-of-pid_compact-v1-s7-1200)

### Reset V1 parameter (S7-1200)

The response to Reset = TRUE depends on the version of the PID_Compact instruction.

#### Reset response PID_Compact as of Version 1.1

A rising edge at Reset triggers a change to "Inactive" mode; errors and warnings are reset and the integral action is deleted. A falling edge at Reset triggers a change to the most recently active operating mode. If automatic mode was active before, the integral action is pre-assigned in such a way that the switchover is bumpless.

![Reset response PID_Compact as of Version 1.1](images/166086904843_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Activation |
| ② | Error |
| ③ | Reset |

#### Reset response PID_Compact V.1.0

A rising edge at Reset triggers a change to "Inactive" mode; errors and warnings are reset and the integral action is deleted. The controller is not reactivated until the next edge at i_Mode.

![Reset response PID_Compact V.1.0](images/166086935947_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Activation |
| ② | Error |
| ③ | Reset |

### Tag sd_warning V1 (S7-1200)

If several warnings are pending, the values of variable sd_warning are displayed by means of binary addition. The display of warning 0003, for example, indicates that the warnings 0001 and 0002 are also pending.

| sd_warning  (DW#16#....) | Description |
| --- | --- |
| 0000 | No warning pending. |
| 0001 | The point of inflection was not found during pretuning. |
| 0002 | Oscillation increased during fine tuning. |
| 0004 | The setpoint was outside the set limits. |
| 0008 | Not all the necessary controlled system properties were defined for the selected method of calculation. The PID parameters were instead calculated using the "i_CtrlTypeTIR = 3" method. |
| 0010 | The operating mode could not be changed because ManualEnable = TRUE. |
| 0020 | The cycle time of the calling OB limits the sampling time of the PID algorithm.   Improve results by using shorter OB cycle times. |
| 0040 | The process value exceeded one of its warning limits. |

The following warnings are deleted as soon as the cause is dealt with:

- 0004
- 0020
- 0040

All other warnings are cleared with a rising edge at Reset.

---

**See also**

[Static tags of PID_Compact V1 (S7-1200)](#static-tags-of-pid_compact-v1-s7-1200)

### Tag i_Event_SUT V1 (S7-1200)

| i_Event_SUT | Name | Description |
| --- | --- | --- |
| 0 | SUT_INIT | Initialize pretuning |
| 100 | SUT_STDABW | Calculate the standard deviation |
| 200 | SUT_GET_POI | Find the point of inflection |
| 9900 | SUT_IO | Pretuning successful |
| 1 | SUT_NIO | Pretuning not successful |

---

**See also**

[Static tags of PID_Compact V1 (S7-1200)](#static-tags-of-pid_compact-v1-s7-1200)
  
[Parameters State and sRet.i_Mode V1 (S7-1200)](#parameters-state-and-sreti_mode-v1-s7-1200)

### Tag i_Event_TIR V1 (S7-1200)

| i_Event_TIR | Name | Description |
| --- | --- | --- |
| -100 | TIR_FIRST_SUT | Fine tuning is not possible. Pretuning will be executed first. |
| 0 | TIR_INIT | Initialize fine tuning |
| 200 | TIR_STDABW | Calculate the standard deviation |
| 300 | TIR_RUN_IN | Attempt to reach the setpoint |
| 400 | TIR_CTRLN | Attempt to reach the setpoint with the existing PID parameters   (if pretuning has been successful) |
| 500 | TIR_OSZIL | Determine oscillation and calculate parameters |
| 9900 | TIR_IO | Fine tuning successful |
| 1 | TIR_NIO | Fine tuning not successful |

---

**See also**

[Static tags of PID_Compact V1 (S7-1200)](#static-tags-of-pid_compact-v1-s7-1200)
  
[Parameters State and sRet.i_Mode V1 (S7-1200)](#parameters-state-and-sreti_mode-v1-s7-1200)

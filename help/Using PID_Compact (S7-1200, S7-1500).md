---
title: "Using PID_Compact (S7-1200, S7-1500)"
package: TFTOPIDCompenUS
topics: 45
devices: [S7-1200, S7-1500, S7-1500T]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Using PID_Compact (S7-1200, S7-1500)

This section contains information on the following topics:

- [Technology object PID_Compact (S7-1200, S7-1500)](#technology-object-pid_compact-s7-1200-s7-1500)
- [PID_Compact as of V2 (S7-1200, S7-1500)](#pid_compact-as-of-v2-s7-1200-s7-1500)
- [PID_Compact V1 (S7-1200, S7-1500)](#pid_compact-v1-s7-1200-s7-1500)

## Technology object PID_Compact (S7-1200, S7-1500)

The technology object PID_Compact provides a continuous PID controller with integrated optimization. You can alternatively configure a pulse controller. Both manual and automatic mode are possible.

PID-Compact continuously acquires the measured process value within a control loop and compares it with the required setpoint. From the resulting control deviation, the instruction PID_Compact calculates an output value by which the process value is adapted as quickly and stable as possible to the setpoint. The output value for the PID controller consists of three actions:

- **Proportional** action

  The proportional action of the output value increases in proportion to the control deviation.
- **I** action

  The integral action of the output value increases until the control deviation has been balanced.
- **D** action

  The derivative action increases with the rate of change of control deviation. The process value is corrected to the setpoint as quickly as possible. The derivative action will be reduced again if the rate of change of control deviation drops.

The instruction PID_Compact calculates the proportional, integral and derivative parameters for your controlled system during pretuning. Fine tuning can be used to tune the parameters further. You do not need to manually determine the parameters.

### Additional information

- [Overview of software controller](Configuring%20a%20software%20controller.md#overview-of-software-controller)
- [Add technology objects](Configuring%20a%20software%20controller.md#add-technology-objects)
- [Configure technology objects](Configuring%20a%20software%20controller.md#configure-technology-objects)
- [Configuring PID_Compact as of V2](#configuring-pid_compact-as-of-v2-s7-1200-s7-1500)
- [Configuring PID_Compact V1](#configuring-pid_compact-v1-s7-1200-s7-1500)

### FAQ

For more information, see the following FAQs in the Siemens Industry Online Support:

- Entry ID [79047707](https://support.industry.siemens.com/cs/ww/en/view/79047707)

## PID_Compact as of V2 (S7-1200, S7-1500)

This section contains information on the following topics:

- [Configuring PID_Compact as of V2 (S7-1200, S7-1500)](#configuring-pid_compact-as-of-v2-s7-1200-s7-1500)
- [Commissioning PID_Compact as of V2 (S7-1200, S7-1500)](#commissioning-pid_compact-as-of-v2-s7-1200-s7-1500)
- [Override control with PID_Compact as of V2 (S7-1200, S7-1500)](#override-control-with-pid_compact-as-of-v2-s7-1200-s7-1500)
- [Simulating PID_Compact as of V2 with PLCSIM (S7-1200, S7-1500)](#simulating-pid_compact-as-of-v2-with-plcsim-s7-1200-s7-1500)

### Configuring PID_Compact as of V2 (S7-1200, S7-1500)

This section contains information on the following topics:

- [Basic settings as of V2 (S7-1200, S7-1500)](#basic-settings-as-of-v2-s7-1200-s7-1500)
- [Process value settings as of V2 (S7-1200, S7-1500)](#process-value-settings-as-of-v2-s7-1200-s7-1500)
- [Advanced settings as of V2 (S7-1200, S7-1500)](#advanced-settings-as-of-v2-s7-1200-s7-1500)

#### Basic settings as of V2 (S7-1200, S7-1500)

This section contains information on the following topics:

- [Introduction as of V2 (S7-1200, S7-1500)](#introduction-as-of-v2-s7-1200-s7-1500)
- [Control mode as of V2 (S7-1200, S7-1500)](#control-mode-as-of-v2-s7-1200-s7-1500)
- [Setpoint as of V2 (S7-1200, S7-1500)](#setpoint-as-of-v2-s7-1200-s7-1500)
- [Process value as of V2 (S7-1200, S7-1500)](#process-value-as-of-v2-s7-1200-s7-1500)
- [Output value as of V2 (S7-1200, S7-1500)](#output-value-as-of-v2-s7-1200-s7-1500)

##### Introduction as of V2 (S7-1200, S7-1500)

Configure the following properties of the "PID_Compact" technology object under "Basic settings" in the Inspector window or in the configuration window:

- Physical quantity
- Control logic
- Start-up behavior after reset
- Setpoint (only in the Inspector window)
- Process value (only in the Inspector window)
- Output value (only in the Inspector window)

###### Setpoint, process value and output value

You can only configure the setpoint, process value and output value in the Inspector window of the programming editor. Select the source for each value:

- Instance DB

  The value saved in the instance DB is used.

  Value must be updated in the instance DB by the user program.

  There should be no value at the instruction.

  Change via HMI possible.
- Instruction

  The value connected to the instruction is used.   
  The value is written to the instance DB each time the instruction is called.

  No change via HMI possible.

##### Control mode as of V2 (S7-1200, S7-1500)

###### Physical quantity

Select the unit of measurement and physical quantity for the setpoint and the process value in the "Controller type" group. The setpoint and the process value are displayed in this unit.

###### Control logic

An increase of the output value is generally intended to cause an increase in the process value. This is referred to as a normal control logic.

PID_Compact does not work with negative proportional gain. Select the check box "Invert control logic" to reduce the process value with a higher output value.

Examples

- Opening the drain valve will reduce the level of a container's contents.
- Increasing cooling will reduce the temperature.

###### Startup characteristics

1. To switch to "Inactive" mode after CPU restart, clear the "Activate Mode after CPU restart" check box.

   To switch to the operating mode saved in the Mode parameter after CPU restart, select the "Activate Mode after CPU restart" check box.
2. In the "Set Mode to" drop-down list, select the mode that is to be enabled after a complete download to the device.

   After a complete download to the device, PID_Compact starts in the selected operating mode. With each additional restart, PID_Compact starts in the mode that was last saved in Mode.

Example

You have selected the "Activate Mode after CPU restart" check box and the entry "Pretuning" in the "Set Mode to" list. After a complete download to the device, PID_Compact starts in the "Pretuning" mode. If pretuning is still active, PID_Compact starts in "Pretuning" mode again after restart of the CPU. If pretuning was successfully completed and automatic mode is active, PID_Compact starts in "Automatic mode" after restart of the CPU.

##### Setpoint as of V2 (S7-1200, S7-1500)

###### Procedure

Proceed as follows to define a fixed setpoint:

1. Select "Instance DB".
2. Enter a setpoint, e.g. 80° C.
3. Delete any entry in the instruction.

Proceed as follows to define a variable setpoint:

1. Select "Instruction".
2. Enter the name of the REAL variable in which the setpoint is saved.

   Program-controlled assignment of various values to the REAL variable is possible, for example for the time controlled change of the setpoint.

##### Process value as of V2 (S7-1200, S7-1500)

PID_Compact will scale the value of the analog input to the physical quantity if you use the analog input value directly.

You will need to write a program for processing if you wish first to process the analog input value. The process value is, for example, not directly proportional to the value at the analog input. The processed process value must be in floating point format.

###### Procedure

Proceed as follows to use the analog input value without processing:

1. Select the entry "Input_PER" in the drop-down list "Input".
2. Select "Instruction" as source.
3. Enter the address of the analog input.

Proceed as follows to use the processed process value in floating point format:

1. Select the entry "Input" in the drop-down list "Input".
2. Select "Instruction" as source.
3. Enter the name of the variable in which the processed process value is saved.

##### Output value as of V2 (S7-1200, S7-1500)

PID_Compact offers three output values. Your actuator will determine which output value you use.

- Output_PER

  The actuator is triggered via an analog output and controlled with a continuous signal, e.g. 0...10V, 4...20mA.
- Output

  The output value needs to be processed by the user program, for example because of non-linear actuator response.
- Output_PWM

  The actuator is controlled via a digital output. Pulse width modulation creates minimum ON and minimum OFF times.

###### Procedure

Proceed as follows to use the analog output value:

1. Select the entry "Output_PER (analog)" in the drop-down list "Output".
2. Select "Instruction".
3. Enter the address of the analog output.

Proceed as follows to process the output value using the user program:

1. Select the entry "Output" in the drop-down list "Output".
2. Select "Instance DB".

   The calculated output value is saved in the instance data block.
3. For the preparation of the output value, use the output parameter Output.
4. Transfer the processed output value to the actuator via a digital or analog CPU output.

Proceed as follows to use the digital output value:

1. Select the entry "Output_PWM" in the drop-down list "Output".
2. Select "Instruction".
3. Enter the address of the digital output.

#### Process value settings as of V2 (S7-1200, S7-1500)

This section contains information on the following topics:

- [Scaling process value as of V2 (S7-1200, S7-1500)](#scaling-process-value-as-of-v2-s7-1200-s7-1500)
- [Process value limits as of V2 (S7-1200, S7-1500)](#process-value-limits-as-of-v2-s7-1200-s7-1500)

##### Scaling process value as of V2 (S7-1200, S7-1500)

If you have configured the use of Input_PER in the basic setting, you must convert the value of the analog input to the physical quantity of the process value. The current configuration is displayed in the Input_PER display.

Input_PER will be scaled using a low and high value pair if the process value is directly proportional to the value of the analog input.

###### Procedure

To scale the process value, follow these steps:

1. Enter the low pair of values in the "Scaled low process value" and "Low" input fields.
2. Enter the high pair of values in the "Scaled high process value" and "High" input boxes.

Default settings for the value pairs are stored in the hardware configuration. To use the value pairs from the hardware configuration, follow these steps:

1. Select the PID_Compact instruction in the programming editor.
2. Interconnect Input_PER with an analog input in the basic settings.
3. Click the "Automatic setting" button in the process value settings.

The existing values will be overwritten with the values from the hardware configuration.

##### Process value limits as of V2 (S7-1200, S7-1500)

You must specify an appropriate absolute high limit and low limit for the process value as limit values for your controlled system. As soon as the process value violates these limits, an error occurs (ErrorBits = 0001h). Tuning is canceled when the process value limits are violated. You can configure how PID_Compact reacts to an error in automatic mode in the output value settings.

#### Advanced settings as of V2 (S7-1200, S7-1500)

This section contains information on the following topics:

- [Process value monitoring as of V2 (S7-1200, S7-1500)](#process-value-monitoring-as-of-v2-s7-1200-s7-1500)
- [PWM limits as of V2 (S7-1200, S7-1500)](#pwm-limits-as-of-v2-s7-1200-s7-1500)
- [Output value as of V2 (S7-1200, S7-1500)](#output-value-as-of-v2-s7-1200-s7-1500-1)
- [PID parameters V2 (S7-1200, S7-1500)](#pid-parameters-v2-s7-1200-s7-1500)
- [PID parameters V3 (S7-1200, S7-1500)](#pid-parameters-v3-s7-1200-s7-1500)

##### Process value monitoring as of V2 (S7-1200, S7-1500)

Configure a warning high and low limit for the process value in the "Process value monitoring" configuration window. If one of the warning limits is exceeded or undershot during operation, a warning will be displayed at the PID_Compact instruction:

- At the InputWarning_H output parameter if the warning high limit has been exceeded
- At the InputWarning_L output parameter if the warning low limit has been undershot

The warning limits must be within the process value high and low limits.

The process value high and low limits will be used if you do not enter values.

###### Example

Process value high limit = 98 °C; warning high limit = 90 °C

Warning low limit = 10 °C; process value low limit = 0 °C

PID_Compact will respond as follows:

| Process value | InputWarning_H | InputWarning_L | ErrorBits | Operating mode |
| --- | --- | --- | --- | --- |
| &gt; 98 °C | TRUE | FALSE | 0001h | Inactive or   Substitute output value with error monitoring |
| ≤ 98 °C and &gt; 90 °C | TRUE | FALSE | 0000h | Automatic mode |
| ≤ 90 °C and ≥ 10 °C | FALSE | FALSE | 0000h | Automatic mode |
| &lt; 10 °C and ≥ 0 °C | FALSE | TRUE | 0000h | Automatic mode |
| &lt; 0 °C | FALSE | TRUE | 0001h | Inactive or   Substitute output value with error monitoring |

In the output value settings, you can specify the reaction of PID_Compact when the process value high limit or low limit is violated.

---

**See also**

[State and Mode as of V2 parameters (S7-1200, S7-1500)](PID_Compact%20%28S7-1200%2C%20S7-1500%29.md#state-and-mode-as-of-v2-parameters-s7-1200-s7-1500)

##### PWM limits as of V2 (S7-1200, S7-1500)

Via pulse width modulation, the value at the output parameter Output is transformed into a pulse sequence that is output at output parameter Output_PWM.

Output is calculated in the PID algorithm sampling time. The sampling time is used as time period of the pulse width modulation.

The PID algorithm sampling time is determined during pretuning or fine tuning. If manually setting the PID parameters, you will also need to configure the PID algorithm sampling time.

Output_PWM is output in the PID_Compact sampling time. The PID_Compact sampling time is equivalent to the cycle time of the calling OB.

The pulse duration is proportional to the value at Output and is always an integer multiple of the PID_Compact sampling time.

![Figure](images/166014203659_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | PID_Compact sampling time |
| ② | PID algorithm sampling time |
| ③ | Pulse duration |
| ④ | Break time |

The "Minimum ON time" and the "Minimum OFF time" are rounded to an integer multiple of the PID_Compact sampling time.

A pulse or a break is never shorter than the minimum ON or OFF time. The inaccuracies this causes are added up and compensated in the next cycle.

**Example**

PID_Compact sampling time (equivalent to the cycle time of the calling OB) = 100 ms

PID algorithm sampling time (equivalent to the time period)= 1000 ms

Minimum ON time = 200 ms

Output is a constant 15%. The smallest pulse that PID_Compact can output is 20%. In the first cycle, no pulse is output. In the second cycle, the pulse not output in the first cycle is added to the pulse of the second cycle.

![Figure](images/166014198155_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | PID_Compact sampling time |
| ② | PID algorithm sampling time |
| ⑤ | Minimum ON time |

In order to minimize operation frequency and conserve the actuator, extend the minimum ON and OFF times.

If you are using "Output" or "Output_PER", you must configure the value 0.0 for the minimum ON and OFF times.

> **Note**
>
> The minimum ON and OFF times only affect the output parameter Output_PWM and are not used for any pulse generators integrated in the CPU.

##### Output value as of V2 (S7-1200, S7-1500)

###### Output value limits

In the "Output value limits" configuration window, configure the absolute limits of your output value in percent. Absolute output value limits are not violated in neither manual mode nor automatic mode. If an output value outside the limits is specified in manual mode, the effective value is limited in the CPU to the configured limits.

The output value limits must match the control logic.

The valid output value limit values depend on the Output used.

| Symbol | Meaning |
| --- | --- |
| Output | -100.0 to 100.0% |
| Output_PER | -100.0 to 100.0% |
| Output_PWM | 0.0 to 100.0% |

###### Reaction to error

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Your system may be damaged.**  If you output "Current value while error pending " or "Substitute output value while error pending" in the event of an error, PID_Compact remains in automatic mode. This may cause a violation of the process value limits and damage your system.   It is essential to configure how your controlled system reacts in the event of an error to protect your system from damage. |  |

PID_Compact is preset so that the controller stays active in most cases in the event of an error. If errors occur frequently in controller mode, this default reaction has a negative effect on the control response. In this case, check the Errorbits parameter and eliminate the cause of the error.

PID_Compact generates a programmable output value in response to an error:

- Zero (inactive)

  PID_Compact outputs 0.0 as output value for all errors and switches to "Inactive" mode. The controller is only reactivated by a falling edge at Reset or a rising edge at ModeActivate.
- Current value while error is pending

  If the following errors occur in **automatic mode**, PID_Compact returns to automatic mode as soon as the errors are no longer pending.

  If one or more of the following errors occur, PID_Compact stays in   
  automatic mode:

  - 0001h: The "Input" parameter is outside the process value limits.
  - 0800h: Sampling time error
  - 40000h: Invalid value at Disturbance parameter.

  If one or more of the following errors occur in **automatic mode**, PID_Compact switches to "Substitute output value with error monitoring" mode and outputs the last valid output value:

  - 0002h: Invalid value at Input_PER parameter.
  - 0200h: Invalid value at Input parameter.
  - 0400h: Calculation of output value failed.
  - 1000h: Invalid value at Setpoint parameter.

  If an error occurs in **manual mode**, PID_Compact continues using the manual value as the output value. If the manual value is invalid, the substitute output value is used. If the manual value and substitute output value are invalid, the output value low limit is used.

  If the following error occurs during a **pretuning or fine tuning**, PID_Compact remains in active mode:

  - 0020h: Pretuning is not permitted during fine tuning.

  When any other error occurs, PID_Compact cancels the tuning and switches to the mode from which tuning was started.

  As soon as no errors are pending, PID_Compact returns to automatic mode.
- Substitute output value while error is pending

  PID_Compact outputs the substitute output value.

  If the following error occurs, PID_Compact stays in "Substitute output value with error monitoring" mode and outputs the output value low limit:

  - 20000h: Invalid value at SubstituteOutput tag.

  For all other errors, PID_Compact reacts as described for "Current value while error is pending".

---

**See also**

[State and Mode as of V2 parameters (S7-1200, S7-1500)](PID_Compact%20%28S7-1200%2C%20S7-1500%29.md#state-and-mode-as-of-v2-parameters-s7-1200-s7-1500)

##### PID parameters V2 (S7-1200, S7-1500)

The PID parameters are displayed in the "PID Parameters" configuration window. The PID parameters will be adapted to your controlled system during controller tuning. You do not need to enter the PID parameters manually.

> **Note**
>
> The currently active PID parameters are located for PID_Compact V1 in the sRet structure and as of PID_Compact V2 in the Retain.CtrlParams structure.
>
> Change the currently active PID parameters only in "Inactive" mode online to prevent malfunction of the PID controller.
>
> If you want to change the PID parameters in "Automatic mode" or "Manual mode" online, change the PID parameters as follows:
>
> - PID_Compact V1: Change the PID parameters in the sBackUp structure and apply these changes with sPid_Cmpt.b_LoadBackUp = TRUE to the sRet structure.
> - PID_Compact as of V2: Change the PID parameters in the CtrlParamsBackUp structure and apply these changes with LoadBackUp = TRUE to the Retain.CtrlParams structure.
>
> Online changes to the PID parameters in "Automatic mode" can result in jumps at the output value.

The PID algorithm operates according to the following equation:

![Figure](images/172252714123_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| **Symbol** | **Description** |
| y | Output value of the PID algorithm |
| K<sub>p</sub> | Proportional gain |
| s | Laplace operator |
| b | Proportional action weighting |
| w | Setpoint |
| x | Process value |
| T<sub>I</sub> | Integration time |
| a | Derivative delay coefficient (derivative delay T1 = a × T<sub>D</sub>) |
| T<sub>D</sub> | Derivative action time |
| c | Derivative action weighting |

The diagram below illustrates the integration of the parameters into the PID algorithm:

![Figure](images/166014208907_DV_resource.Stream@PNG-en-US.png)

All PID parameters are retentive. If you enter the PID parameters manually, you must completely download PID_Compact.

[Downloading technology objects to device](Configuring%20a%20software%20controller.md#downloading-technology-objects-to-device)

###### Proportional gain

The value specifies the proportional gain of the controller. PID_Compact does not work with a negative proportional gain. Control logic is inverted under Basic settings &gt; Controller type.

###### Integration time

The integration time determines the time behavior of the integral action. The integral action is deactivated with integration time = 0.0. When the integration time is changed from a different value to 0.0 online in "Automatic mode", the previous integral action is deleted and the output value jumps.

###### Derivative action time

The derivative action time determines the time behavior of the derivative action. Derivative action is deactivated with derivative action time = 0.0.

###### Derivative delay coefficient

The derivative delay coefficient delays the effect of the derivative action.

Derivative delay = derivative action time × derivative delay coefficient

- 0.0: Derivative action is effective for one cycle only and therefore almost not effective.
- 0.5: This value has proved useful in practice for controlled systems with **one** dominant time constant.
- &gt; 1.0: The greater the coefficient, the longer the effect of the derivative action is delayed.

###### Proportional action weighting

The proportional action may weaken with changes to the setpoint.

Values from 0.0 to 1.0 are applicable.

- 1.0: Proportional action for setpoint change is fully effective
- 0.0: Proportional action for setpoint change is not effective

The proportional action is always fully effective when the process value is changed.

###### Derivative action weighting

The derivative action may weaken with changes to the setpoint.

Values from 0.0 to 1.0 are applicable.

- 1.0: Derivative action is fully effective upon setpoint change
- 0.0: Derivative action is not effective upon setpoint change

The derivative action is always fully effective when the process value is changed.

###### PID algorithm sampling time

The controlled system needs a certain amount of time to respond to changes in the output value. It is therefore not advisable to calculate the output value in every cycle. The sampling time of the PID algorithm represents the time between two calculations of the output value. It is calculated during tuning and rounded to a multiple of the cycle time. All other functions of PID_Compact are executed at every call.

If you use Output_PWM, the sampling time of the PID algorithm is used as the period duration of the pulse width modulation. The accuracy of the output signal is determined by the ratio of the PID algorithm sampling time to the cycle time of the OB. It is therefore recommended that the cycle time is a maximum of one tenth of the PID algorithm sampling time.

###### Rule for tuning

Select whether PI or PID parameters are to be calculated in the "Controller structure" drop-down list.

- **PID**

  Calculates PID parameters during pretuning and fine tuning.
- **PI**

  Calculates PI parameters during pretuning and fine tuning.
- **User-defined**

  The drop-down list displays "User-defined" if you have configured different controller structures for pretuning and fine tuning via a user program.

---

**See also**

[Selection of the controller structure for specified controlled systems](PID%20control.md#selection-of-the-controller-structure-for-specified-controlled-systems)

##### PID parameters V3 (S7-1200, S7-1500)

The PID parameters are displayed in the "PID Parameters" configuration window. During tuning, the PID parameters are adapted to the controlled system with the exception of the dead zone width that has to be configured manually.

> **Note**
>
> The currently active PID parameters are located in the Retain.CtrlParams structure.
>
> Change the currently active PID parameters only in "Inactive" mode online to prevent malfunction of the PID controller.
>
> If you want to change the PID parameters in "Automatic mode" or "Manual mode" online, change the PID parameters in the CtrlParamsBackUp structure and apply these changes with LoadBackUp = TRUE to the Retain.CtrlParams structure.
>
> Online changes to the PID parameters in "Automatic mode" can result in jumps at the output value.

PID_Compact is a PIDT1 controller with Anti-Windup and weighting of the proportional and derivative actions.

The PID algorithm operates according to the following equation (dead zone disabled):

![Figure](images/172252714123_DV_resource.Stream@PNG-de-DE.png)

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
| a | Derivative delay coefficient (derivative delay T1 = a × T<sub>D</sub>) | Retain.CtrlParams.TdFiltRatio |
| T<sub>D</sub> | Derivative action time | Retain.CtrlParams.Td |
| c | Derivative action weighting | Retain.CtrlParams.DWeighting |
| DeadZone | Dead zone width | Retain.CtrlParams.DeadZone |

The diagram below illustrates the integration of the parameters into the PID algorithm:

![Figure](images/171621836555_DV_resource.Stream@PNG-de-DE.png)

All PID parameters are retentive. If you enter the PID parameters manually, you must completely download PID_Compact.

[Download technology objects to device](Configuring%20a%20software%20controller.md#downloading-technology-objects-to-device)

###### Proportional gain

The value specifies the proportional gain of the controller. PID_Compact does not work with a negative proportional gain. Control logic is inverted under Basic settings &gt; Controller type.

###### Integration time

The integration time determines the time behavior of the integral action. The integral action is deactivated with integration time = 0.0. When the integration time is changed from a different value to 0.0 online in "Automatic mode", the previous integral action is deleted and the output value jumps.

If the output value reaches an output value limit in automatic mode, the integral action is stopped depending on the direction (Anti-Windup). As of PID_Compact Version 3.0, the integral component is also actively limited in order to prevent delayed control behavior, e.g. when the output value limits change. Changes to the following tags can lead to an adjustment of the integral component in automatic mode:

- Output value limits (Config.OutputLowerLimit and Config.OutputUpperLimit tags)
- Setpoint (Setpoint tag)
- Proportional gain (Retain.CtrlParams.Gain tag)
- Proportional action weighting (Retain.CtrlParams.PWeighting tag)
- Disturbance variable (Disturbance variable)

###### Derivative action time

The derivative action time determines the time behavior of the derivative action. Derivative action is deactivated with derivative action time = 0.0.

###### Derivative delay coefficient

The derivative delay coefficient delays the effect of the derivative action.

Derivative delay = derivative action time × derivative delay coefficient

- 0.0: Derivative action is effective for one cycle only and therefore almost not effective.
- 0.5: This value has proved useful in practice for controlled systems with **one** dominant time constant.
- &gt; 1.0: The greater the coefficient, the longer the effect of the derivative action is delayed.

###### Proportional action weighting

The proportional action may weaken with changes to the setpoint.

Values from 0.0 to 1.0 are applicable.

- 1.0: Proportional action for setpoint change is fully effective
- 0.0: Proportional action for setpoint change is not effective

The proportional action is always fully effective when the process value is changed.

###### Derivative action weighting

The derivative action may weaken with changes to the setpoint.

Values from 0.0 to 1.0 are applicable.

- 1.0: Derivative action is fully effective upon setpoint change
- 0.0: Derivative action is not effective upon setpoint change

The derivative action is always fully effective when the process value is changed.

###### PID algorithm sampling time

The controlled system needs a certain amount of time to respond to changes in the output value. It is therefore not advisable to calculate the output value in every cycle. The sampling time of the PID algorithm represents the time between two calculations of the output value. It is calculated during tuning and rounded to a multiple of the cycle time. All other functions of PID_Compact are executed at every call.

If you use Output_PWM, the sampling time of the PID algorithm is used as the period duration of the pulse width modulation. The accuracy of the output signal is determined by the ratio of the PID algorithm sampling time to the cycle time of the OB. It is therefore recommended that the cycle time is a maximum of one tenth of the PID algorithm sampling time.

###### Dead zone width

If the process value is affected by noise, the noise can also have an effect on the output value. The output value may fluctuate considerably when the controller gain is high and the derivative action is activated. If the process value lies within the dead zone around the setpoint, the control deviation is suppressed so that the PID algorithm does not react and unnecessary fluctuations of the output value are reduced.

The dead zone width is not set automatically during tuning. You have to correctly configure the dead zone width manually. The dead zone is deactivated by setting the dead zone width = 0.0.

When the dead zone is switched on, the result can be a permanent control deviation (deviation between setpoint and process value). This can have a negative effect on fine tuning.

If values other than 1.0 are configured for the proportional action weighting or the derivative action weighting, setpoint changes even within the dead zone affect the output value.

Process value changes within the dead zone do not affect the output value, regardless of the weighting.

The diagram below illustrates the effect of the dead zone: The X / horizontal axis shows the control deviation = Setpoint - Process value. The Y / vertical axis shows the output signal of the dead zone that is passed to the PID algorithm.

![Dead zone width](images/171622762379_DV_resource.Stream@PNG-de-DE.png)

###### Rule for tuning

Select whether PI or PID parameters are to be calculated in the "Controller structure" drop-down list.

- **PID**

  Calculates PID parameters during pretuning and fine tuning.
- **PI**

  Calculates PI parameters during pretuning and fine tuning.
- **User-defined**

  The drop-down list displays "User-defined" if you have configured different controller structures for pretuning and fine tuning via a user program.

### Commissioning PID_Compact as of V2 (S7-1200, S7-1500)

This section contains information on the following topics:

- [Pretuning as of V2 (S7-1200, S7-1500)](#pretuning-as-of-v2-s7-1200-s7-1500)
- [Fine tuning as of V2 (S7-1200, S7-1500)](#fine-tuning-as-of-v2-s7-1200-s7-1500)
- ["Manual" mode as of V2 (S7-1200, S7-1500)](#manual-mode-as-of-v2-s7-1200-s7-1500)

#### Pretuning as of V2 (S7-1200, S7-1500)

The pretuning determines the process response to a jump change of the output value and searches for the point of inflection. The PID parameters are calculated from the maximum rate of rise and dead time of the controlled system. You obtain the best PID parameters when you perform pretuning and fine tuning.

The more stable the process value is, the easier it is to calculate the PID parameters and the more precise the result will be. Noise on the process value can be tolerated as long as the rate of rise of the process value is significantly higher compared to the noise. This is most likely the case in operating modes "Inactive" and "manual mode". The PID parameters are backed up before being recalculated.

##### Requirement

- The "PID_Compact" instruction is called in a cyclic interrupt OB.
- ManualEnable = FALSE
- Reset = FALSE
- PID_Compact is in one of the following modes: "Inactive", "Manual mode", or "Automatic mode".
- The setpoint and the process value lie within the configured limits (see "Process value monitoring" configuration).
- The difference between setpoint and process value is greater than 30% of the difference between process value high limit and process value low limit.
- The distance between the setpoint and the process value is &gt; 50% of the setpoint.

##### Procedure

To perform pretuning, follow these steps:

1. Double-click the "PID_Compact &gt; Commissioning" entry in the project tree.
2. Select the entry "Pretuning" in the "Tuning mode" drop-down list.
3. Click the "Start" icon.

   - An online connection will be established.
   - Value recording is started.
   - Pretuning is started.
   - The "Status" field displays the current steps and any errors that may have occurred. The progress bar indicates the progress of the current step.

**Note**

Click the "Stop" icon when the progress bar has reached 100% and it can be assumed the controller tuning function is blocked. Check the configuration of the technology object and, if necessary, restart controller tuning.

##### Result

If pretuning was performed without an error message, the PID parameters have been tuned. PID_Compact switches to automatic mode and uses the tuned parameters. The tuned PID parameters will be retained during power OFF and a restart of the CPU.

If pretuning is not possible, PID_Compact responds with the configured reaction to errors.

---

**See also**

[State and Mode as of V2 parameters (S7-1200, S7-1500)](PID_Compact%20%28S7-1200%2C%20S7-1500%29.md#state-and-mode-as-of-v2-parameters-s7-1200-s7-1500)

#### Fine tuning as of V2 (S7-1200, S7-1500)

Fine tuning generates a constant, limited oscillation of the process value. The PID parameters are tuned for the operating point from the amplitude and frequency of this oscillation. All PID parameters are recalculated from the results. PID parameters from fine tuning usually have better master control and disturbance characteristics than PID parameters from pretuning. You obtain the best PID parameters when you perform pretuning and fine tuning.

PID_Compact automatically attempts to generate an oscillation greater than the noise of the process value. Fine tuning is only minimally influenced by the stability of the process value. The PID parameters are backed up before being recalculated.

##### Requirement

- The PID_Compact instruction is called in a cyclic interrupt OB.
- ManualEnable = FALSE
- Reset = FALSE
- The setpoint and the process value lie within the configured limits.
- The control loop has stabilized at the operating point. The operating point is reached when the process value corresponds to the setpoint.
- No disturbances are expected.
- PID_Compact is in inactive mode, automatic mode or manual mode.

##### Process depends on initial situation

Fine tuning can be started from the following operating modes: "Inactive", "automatic mode", or "manual mode". Fine tuning proceeds as follows when started from:

- Automatic mode

  Start fine tuning from automatic mode if you wish to improve the existing PID parameters through tuning.

  PID_Compact controls the system using the existing PID parameters until the control loop has stabilized and the requirements for fine tuning have been met. Only then will fine tuning start.
- Inactive or manual mode

  If the requirements for pretuning are met, pretuning is started. The determined PID parameters will be used for control until the control loop has stabilized and the requirements for fine tuning have been met. Only then will fine tuning start. If pretuning is not possible, PID_Compact responds with the configured responses in the event of an error.

  An attempt is made to reach the setpoint with the minimum or maximum output value if the process value for pretuning is already too near the setpoint. This can produce increased overshoot.

##### Procedure

To perform fine tuning, follow these steps:

1. Select the entry "Fine tuning" in the "Tuning mode" drop-down list.
2. Click the "Start" icon.

   - An online connection will be established.
   - Value recording is started.
   - The process of fine tuning is started.
   - The "Status" field displays the current steps and any errors that may have occurred. The progress bar indicates the progress of the current step.

**Note**

Click the "Stop" icon in the "Tuning mode" group when the progress bar has reached 100% and it is to be assumed that tuning is blocked. Check the configuration of the technology object and, if necessary, restart controller tuning.

##### Result

If fine tuning was performed without errors, the PID parameters have been tuned. PID_Compact switches to automatic mode and uses the tuned parameters. The tuned PID parameters will be retained during power OFF and a restart of the CPU.

If errors occurred during "fine tuning", PID_Compact responds with the configured response to errors.

---

**See also**

[State and Mode as of V2 parameters (S7-1200, S7-1500)](PID_Compact%20%28S7-1200%2C%20S7-1500%29.md#state-and-mode-as-of-v2-parameters-s7-1200-s7-1500)

#### "Manual" mode as of V2 (S7-1200, S7-1500)

The following section describes how you can use the "manual mode" operating mode in the commissioning window of the "PID_Compact" technology object. Manual mode is also possible when an error is pending.

##### Requirement

- The "PID_Compact" instruction is called in a cyclic interrupt OB.
- An online connection to the CPU has been established and the CPU is in "RUN" mode.

##### Procedure

Use "Manual mode" in the commissioning window if you want to test the controlled system by specifying a manual value. To define a manual value, proceed as follows:

1. Click the "Start" icon.
2. Select the "Manual mode" check box in the "Online status of controller" area.

   PID_Compact operates in manual mode. The most recent current output value remains in effect.
3. Enter the manual value in the "Output" field as a % value.
4. Click the ![Procedure](images/166014232715_DV_resource.Stream@PNG-de-DE.png) icon.

##### Result

The manual value is written to the CPU and immediately goes into effect.

Clear the "Manual mode" check box if the output value is to be specified again by the PID controller. The switchover to automatic mode is bumpless.

---

**See also**

[State and Mode as of V2 parameters (S7-1200, S7-1500)](PID_Compact%20%28S7-1200%2C%20S7-1500%29.md#state-and-mode-as-of-v2-parameters-s7-1200-s7-1500)

### Override control with PID_Compact as of V2 (S7-1200, S7-1500)

#### Override control

In case of override control, two or more controllers share one actuator. Only one controller has access to the actuator at any time and influences the process.

A logic operation decides which controller has access to the actuator. This decision is often made based on a comparison of the output values of all controllers, for example, in case of a maximum selection, the controller with the largest output value gets access to the actuator.

The selection based on the output value requires that all controllers operate in automatic mode. The controllers that do not have an effect on the actuator are updated. This is necessary to prevent windup effects and their negative impacts on the control response and the switchover between the controllers.

PID_Compact supports override controls as of version 2.3 by offering a simple process for updating the controllers that are not active:

- By using the OverwriteInitialOutputValue and PIDCtrl.PIDInit tags, you can preassign the integral action of the controller in automatic mode as though the PID algorithm had calculated Output = OverwriteInititalOutputValue for the output value in the last cycle.
- To do this, OverwriteInitialOutputValue is interconnected with the output value of the controller that currently has access to the actuator.
- By setting the bit PIDCtrl.PIDInit, you trigger the pre-assignment of the integral action as well as the restart of the controller cycle and the PWM period.
- The subsequent calculation of the output value in the current cycle takes place based on the pre-assigned (and synchronized for all controllers) integral action as well as the proportional action and integral action from the current control deviation.
- The derivative action is not active during the call with PIDCtrl.PIDInit = TRUE and therefore does not contribute to the output value.

This procedure ensures that the calculation of the current output value and thus the decision on which controller is to have access to the actuator is only based on the current process state and the PI parameters. Windup effects for controllers that are not active and thus incorrect decisions of the switchover logic are prevented.

#### Requirements

- PIDCtrl.PIDInit is only effective if the integral action is activated (Retain.CtrlParams.Ti tag &gt; 0.0).
- You must assign PIDCtrl.PIDInit and OverwriteInitialOutputValue in your user program yourself (see example below). PID_Compact does not automatically change these tags.
- PIDCtrl.PIDInit is only effective when PID_Compact is in automatic mode (parameter State = 3)
- If possible, select the sampling time of the PID algorithm (Retain.CtrlParams.Cycle tag) in such a way that it is identical for all controllers, and call all controllers in the same cyclic interrupt OB. In this way, you ensure that the switchover does not take place within a controller cycle or a PWM period.

> **Note**
>
> **Constant adaptation of the output value limits**
>
> Instead of the active updating of the controllers without access to the actuator described here, this is implemented alternatively by constant adaptation of the output value limits in other controller systems.
>
> This is not possible with PID_Compact, because a change of the output value limits is not supported in automatic mode.

#### Example: Control of a gas pipeline

PID_Compact is used for control of a gas pipeline.

The main goal is to control the flow rate Input1. The controller PID_Compact_1 is used for this purpose. In addition, the pressure Input2 (measured in flow direction in front of the valve) is to be kept below the high limit with the limiting controller PID_Compact_2.

Flow rate and pressure are controlled by a single solenoid valve. The output value of the controller corresponds to the valve opening: The valve is opened when the output value increases. This means the flow rate increases (normal control logic) while the pressure drops (inverted control logic).

![Example: Control of a gas pipeline](images/166014236811_DV_resource.Stream@PNG-de-DE.png)

The valve is controlled with the output value of PID_Compact in I/O format (parameter Output_PER) by writing the program tag ActuatorInput.

The setpoint for the flow rate is specified at the parameter PID_Compact_1.Setpoint.

The pressure high limit is specified as setpoint at the parameter PID_Compact_2.Setpoint.

![Example: Control of a gas pipeline](images/166014267531_DV_resource.Stream@PNG-de-DE.png)

Both controllers must share one valve as shared actuator. The logic that decides which controller gets access to the actuator is implemented by a maximum selection of the output value (in Real format, parameter Output) in this case. Because the output value corresponds to the opening of the valve, the controller that requires the larger valve opening gets the control.

> **Note**
>
> **Activate inversion of the control logic**
>
> Because a decrease of the actual value (pressure) is to be achieved with the pressure regulator PID_Compact_2 when the output value increases (valve opening), the inversion of the control logic must be activated: PID_Compact_2.Config.InvertControl = TRUE.

In normal operation of the plant, the actual value of the flow rate corresponds to the setpoint. The flow controller PID_Compact_1 has settled on a stationary output value PID_Compact_1.Output. The actual value of the pressure in normal operation is significantly below the high limit that is specified as setpoint for PID_Compact_2. The pressure regulator therefore wants to close the valve even further to increase the pressure, which means it will calculate an output value PID_Compact_2.Output that is smaller than the output value of the flow controller PID_Compact_1.Output. The maximum selection of the switchover logic therefore gives the flow controller PID_Compact_1 continued access to the actuator. In addition, it is ensured that PID_Compact_2 is updated by means of the assignments PID_Compact_2.OverwriteInitialOutputValue = PID_Compact_1.Output and PID_Compact_2.PIDCtrl.PIDInit = TRUE.

If the pressure now approaches the high limit or exceeds it, for example due to a fault, the pressure regulator PID_Compact_2 calculates a higher output value to open the valve even further and thus reduce the pressure. If PID_Compact_2.Output is greater than PID_Compact_1.Output, the pressure regulator PID_Compact_2 receives access to the actuator through the maximum selection and opens it. It is ensured that PID_Compact_1 is updated by means of the assignments PID_Compact_1.OverwriteInitialOutputValue = PID_Compact_2.Output and PID_Compact_1.PIDCtrl.PIDInit = TRUE.

The pressure is reduced while the flow rate increases and can no longer be kept at the setpoint.

Once the fault has been remedied, the pressure will continue to drop and the opening of the valve is reduced by the pressure regulator. If the flow controller calculates a larger opening as output value, the plant returns to normal operation so that the flow controller PID_Compact_1 once again has access to the actuator.

This example can be implemented with the following SCL program code:

| Symbol | Meaning |
| --- | --- |
| `"PID_Compact_1"(Input := "Input1");` |  |
| `"PID_Compact_2"(Input := "Input2");` |  |
| `IF "PID_Compact_1".Output >= "PID_Compact_2".Output THEN` |  |
|  | `"ActuatorInput" := "PID_Compact_1".Output_PER;` |
|  | `"PID_Compact_1".PIDCtrl.PIDInit := FALSE;` |
|  | `"PID_Compact_2".PIDCtrl.PIDInit := TRUE;` |
|  | `"PID_Compact_2".OverwriteInitialOutputValue := "PID_Compact_1".Output;` |
| `ELSE` |  |
|  | `"ActuatorInput" := "PID_Compact_2".Output_PER;` |
|  | `"PID_Compact_1".PIDCtrl.PIDInit := TRUE;` |
|  | `"PID_Compact_2".PIDCtrl.PIDInit := FALSE;` |
|  | `"PID_Compact_1".OverwriteInitialOutputValue := "PID_Compact_2".Output;` |
| `END_IF;` |  |

### Simulating PID_Compact as of V2 with PLCSIM (S7-1200, S7-1500)

> **Note**
>
> **Simulation with PLCSIM**
>
> The simulation of PID_Compact V2.x with PLCSIM for CPU S7-1200 is not supported.
>
> PID_Compact V2.x can only be simulated for CPU S7-1500 with PLCSIM.
>
> For the simulation with PLCSIM, the time behavior of the simulated PLC is not exactly identical to that of a "real" PLC. The actual cycle clock of a cyclic interrupt OB can have larger fluctuations with a simulated PLC than with "real" PLCs.
>
> In the standard configuration, PID_Compact determines the time between calls automatically and monitors them for fluctuations.
>
> For the simulation of PID_Compact with PLCSIM, for example, a sampling time error (ErrorBits = DW#16#00000800) can therefore be detected.
>
> This results in ongoing tuning being aborted.
>
> The response in automatic mode depends on the value of the ActivateRecoverMode tag.
>
> To prevent this from happening, you should configure PID_Compact for simulation with PLCSIM as follows:
>
> - CycleTime.EnEstimation = FALSE
> - CycleTime.EnMonitoring = FALSE
> - CycleTime.Value: Assign the cycle clock of the calling cyclic interrupt OB in seconds to this tag.

## PID_Compact V1 (S7-1200, S7-1500)

This section contains information on the following topics:

- [Configuring PID_Compact V1 (S7-1200, S7-1500)](#configuring-pid_compact-v1-s7-1200-s7-1500)
- [Commissioning PID_Compact V1 (S7-1200, S7-1500)](#commissioning-pid_compact-v1-s7-1200-s7-1500)
- [Simulating PID_Compact V1 with PLCSIM (S7-1200, S7-1500)](#simulating-pid_compact-v1-with-plcsim-s7-1200-s7-1500)

### Configuring PID_Compact V1 (S7-1200, S7-1500)

This section contains information on the following topics:

- [Basic settings V1 (S7-1200, S7-1500)](#basic-settings-v1-s7-1200-s7-1500)
- [Process value settings V1 (S7-1200, S7-1500)](#process-value-settings-v1-s7-1200-s7-1500)
- [Advanced settings V1 (S7-1200, S7-1500)](#advanced-settings-v1-s7-1200-s7-1500)

#### Basic settings V1 (S7-1200, S7-1500)

This section contains information on the following topics:

- [Introduction V1 (S7-1200, S7-1500)](#introduction-v1-s7-1200-s7-1500)
- [Control mode V1 (S7-1200, S7-1500)](#control-mode-v1-s7-1200-s7-1500)
- [Setpoint V1 (S7-1200, S7-1500)](#setpoint-v1-s7-1200-s7-1500)
- [Process value V1 (S7-1200, S7-1500)](#process-value-v1-s7-1200-s7-1500)
- [Output value V1 (S7-1200, S7-1500)](#output-value-v1-s7-1200-s7-1500)

##### Introduction V1 (S7-1200, S7-1500)

Configure the following properties of the "PID_Compact" technology object under "Basic settings" in the Inspector window or in the configuration window:

- Physical quantity
- Control logic
- Start-up behavior after reset
- Setpoint (only in the Inspector window)
- Process value (only in the Inspector window)
- Output value (only in the Inspector window)

###### Setpoint, process value and output value

You can only configure the setpoint, process value and output value in the Inspector window of the programming editor. Select the source for each value:

- Instance DB

  The value saved in the instance DB is used.

  Value must be updated in the instance DB by the user program.

  There should be no value at the instruction.

  Change via HMI possible.
- Instruction

  The value connected to the instruction is used.   
  The value is written to the instance DB each time the instruction is called.

  No change via HMI possible.

##### Control mode V1 (S7-1200, S7-1500)

###### Physical quantity

Select the unit of measurement and physical quantity for the setpoint and process value in the "Controller type" group. The setpoint and process value will be displayed in this unit.

###### Control logic

An increase of the output value is generally intended to cause an increase in the process value. This is referred to as a normal control logic.

PID_Compact does not work with negative proportional gain. Select the check box "Invert control logic" to reduce the process value with a higher output value.

Examples

- Opening the drain valve will reduce the level of a container's contents.
- Increasing cooling will reduce the temperature.

###### Start-up behavior after reset

To change straight to the last active operating mode after restarting the CPU, select the "Enable last mode after CPU restart" check box.

PID_Compact will remain in "Inactive" mode if the check box is cleared.

##### Setpoint V1 (S7-1200, S7-1500)

###### Procedure

Proceed as follows to define a fixed setpoint:

1. Select "Instance DB".
2. Enter a setpoint, e.g. 80° C.
3. Delete any entry in the instruction.

Proceed as follows to define a variable setpoint:

1. Select "Instruction".
2. Enter the name of the REAL variable in which the setpoint is saved.

   Program-controlled assignment of various values to the REAL variable is possible, for example for the time controlled change of the setpoint.

##### Process value V1 (S7-1200, S7-1500)

PID_Compact will scale the value of the analog input to the physical quantity if you use the analog input value directly.

You will need to write a program for processing if you wish first to process the analog input value. The process value is, for example, not directly proportional to the value at the analog input. The processed process value must be in floating point format.

###### Procedure

Proceed as follows to use the analog input value without processing:

1. Select the entry "Input_PER" in the drop-down list "Input".
2. Select "Instruction" as source.
3. Enter the address of the analog input.

Proceed as follows to use the processed process value in floating point format:

1. Select the entry "Input" in the drop-down list "Input".
2. Select "Instruction" as source.
3. Enter the name of the variable in which the processed process value is saved.

##### Output value V1 (S7-1200, S7-1500)

PID_Compact offers three output values. Your actuator will determine which output value you use.

- Output_PER

  The actuator is triggered via an analog output and controlled with a continuous signal, e.g. 0...10V, 4...20mA.
- Output

  The output value needs to be processed by the user program, for example because of non-linear actuator response.
- Output_PWM

  The actuator is controlled via a digital output. Pulse width modulation creates minimum ON and minimum OFF times.

###### Procedure

Proceed as follows to use the analog output value:

1. Select the entry "Output_PER (analog)" in the drop-down list "Output".
2. Select "Instruction".
3. Enter the address of the analog output.

Proceed as follows to process the output value using the user program:

1. Select the entry "Output" in the drop-down list "Output".
2. Select "Instance DB".

   The calculated output value is saved in the instance data block.
3. For the preparation of the output value, use the output parameter Output.
4. Transfer the processed output value to the actuator via a digital or analog CPU output.

Proceed as follows to use the digital output value:

1. Select the entry "Output_PWM" in the drop-down list "Output".
2. Select "Instruction".
3. Enter the address of the digital output.

#### Process value settings V1 (S7-1200, S7-1500)

Configure the scaling of your process value and specify the process value absolute limits In the "Process value settings" configuration window.

##### Scaling the process value

If you have configured the use of Input_PER in the basic settings, you will need to convert the value of the analog input into the physical quantity of the process value. The current configuration will be displayed in the Input_PER display.

Input_PER will be scaled using a low and high value pair if the process value is directly proportional to the value of the analog input.

1. Enter the low pair of values in the "Scaled low process value" and "Low" input fields.
2. Enter the high pair of values in the "Scaled high process value" and "High" input boxes.

Default settings for the value pairs are saved in the hardware configuration. Proceed as follows to use the value pairs from the hardware configuration:

1. Select the instruction PID_Compact in the programming editor.
2. Connect Input_PER with an analog input in the basic settings.
3. Click on the "Automatic setting" button in the process value settings.

The existing values will be overwritten with the values from the hardware configuration.

##### Monitoring process value

Specify the absolute high and low limit of the process value. As soon as these limits are violated during operation, the controller switches off and the output value is set to 0%. You must enter reasonable limits for your controlled system. Reasonable limits are important during optimization to obtain optimal PID parameters.

The default for the "High limit process value" is 120 %. At the I/O input, the process value can be a maximum of 18% higher than the standard range (overrange). An error is no longer reported for a violation of the "High limit process value". Only a wire-break and a short-circuit are recognized and the PID_Compact switches to "Inactive" mode.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| If you set very high process value limits (for example -3.4*10<sup>38</sup>...+3.4*10<sup>38</sup>), process value monitoring will be disabled. Your system may then be damaged if an error occurs. |  |

---

**See also**

[Process value monitoring V1 (S7-1200, S7-1500)](#process-value-monitoring-v1-s7-1200-s7-1500)
  
[PWM limits V1 (S7-1200, S7-1500)](#pwm-limits-v1-s7-1200-s7-1500)
  
[Output value limits V1 (S7-1200, S7-1500)](#output-value-limits-v1-s7-1200-s7-1500)
  
[PID parameters V1 (S7-1200, S7-1500)](#pid-parameters-v1-s7-1200-s7-1500)

#### Advanced settings V1 (S7-1200, S7-1500)

This section contains information on the following topics:

- [Process value monitoring V1 (S7-1200, S7-1500)](#process-value-monitoring-v1-s7-1200-s7-1500)
- [PWM limits V1 (S7-1200, S7-1500)](#pwm-limits-v1-s7-1200-s7-1500)
- [Output value limits V1 (S7-1200, S7-1500)](#output-value-limits-v1-s7-1200-s7-1500)
- [PID parameters V1 (S7-1200, S7-1500)](#pid-parameters-v1-s7-1200-s7-1500)

##### Process value monitoring V1 (S7-1200, S7-1500)

Configure a warning high and low limit for the process value in the "Process value monitoring" configuration window. If one of the warning limits is exceeded or undershot during operation, a warning will be displayed at the PID_Compact instruction:

- At the InputWarning_H output parameter if the warning high limit has been exceeded
- At the InputWarning_L output parameter if the warning low limit has been undershot

The warning limits must be within the process value high and low limits.

The process value high and low limits will be used if you do not enter values.

###### Example

Process value high limit = 98° C; warning high limit = 90° C

Warning low limit = 10° C; process value low limit = 0° C

PID_Compact will respond as follows:

| Process value | InputWarning_H | InputWarning_L | Operating mode |
| --- | --- | --- | --- |
| &gt; 98° C | TRUE | FALSE | Inactive |
| ≤ 98° C and &gt; 90° C | TRUE | FALSE | Automatic mode |
| ≤ 90° C and ≥ 10° C | FALSE | FALSE | Automatic mode |
| &lt; 10° C and ≥ 0° C | FALSE | TRUE | Automatic mode |
| &lt; 0° C | FALSE | TRUE | Inactive |

---

**See also**

[Process value settings V1 (S7-1200, S7-1500)](#process-value-settings-v1-s7-1200-s7-1500)
  
[PWM limits V1 (S7-1200, S7-1500)](#pwm-limits-v1-s7-1200-s7-1500)
  
[Output value limits V1 (S7-1200, S7-1500)](#output-value-limits-v1-s7-1200-s7-1500)
  
[PID parameters V1 (S7-1200, S7-1500)](#pid-parameters-v1-s7-1200-s7-1500)

##### PWM limits V1 (S7-1200, S7-1500)

Via pulse width modulation, the value at the output parameter Output is transformed into a pulse sequence that is output at output parameter Output_PWM.

Output is calculated in the PID algorithm sampling time. The sampling time is used as time period of the pulse width modulation.

The PID algorithm sampling time is determined during pretuning or fine tuning. If manually setting the PID parameters, you will also need to configure the PID algorithm sampling time.

Output_PWM is output in the PID_Compact sampling time. The PID_Compact sampling time is equivalent to the cycle time of the calling OB.

The pulse duration is proportional to the value at Output and is always an integer multiple of the PID_Compact sampling time.

![Figure](images/166014203659_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | PID_Compact sampling time |
| ② | PID algorithm sampling time |
| ③ | Pulse duration |
| ④ | Break time |

The "Minimum ON time" and the "Minimum OFF time" are rounded to an integer multiple of the PID_Compact sampling time.

A pulse or a break is never shorter than the minimum ON or OFF time. The inaccuracies this causes are added up and compensated in the next cycle.

**Example**

PID_Compact sampling time (equivalent to the cycle time of the calling OB) = 100 ms

PID algorithm sampling time (equivalent to the time period)= 1000 ms

Minimum ON time = 200 ms

Output is a constant 15%. The smallest pulse that PID_Compact can output is 20%. In the first cycle, no pulse is output. In the second cycle, the pulse not output in the first cycle is added to the pulse of the second cycle.

![Figure](images/166014198155_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | PID_Compact sampling time |
| ② | PID algorithm sampling time |
| ⑤ | Minimum ON time |

In order to minimize operation frequency and conserve the actuator, extend the minimum ON and OFF times.

If you are using "Output" or "Output_PER", you must configure the value 0.0 for the minimum ON and OFF times.

> **Note**
>
> The minimum ON and OFF times only affect the output parameter Output_PWM and are not used for any pulse generators integrated in the CPU.

---

**See also**

[Process value settings V1 (S7-1200, S7-1500)](#process-value-settings-v1-s7-1200-s7-1500)
  
[Process value monitoring V1 (S7-1200, S7-1500)](#process-value-monitoring-v1-s7-1200-s7-1500)
  
[Output value limits V1 (S7-1200, S7-1500)](#output-value-limits-v1-s7-1200-s7-1500)
  
[PID parameters V1 (S7-1200, S7-1500)](#pid-parameters-v1-s7-1200-s7-1500)

##### Output value limits V1 (S7-1200, S7-1500)

In the "Output value limits" configuration window, configure the absolute limits of your output value in percent. Absolute output value limits are not violated in neither manual mode nor in automatic mode. If a output value outside the limits is specified in manual mode, the effective value is limited in the CPU to the configured limits.

The valid output value limit values depend on the Output used.

| Symbol | Meaning |
| --- | --- |
| Output | -100.0 to 100.0 |
| Output_PER | -100.0 to 100.0 |
| Output_PWM | 0.0 to 100.0 |

PID_Compact sets the output value to 0.0 if an error occurs. 0.0 must therefore always be within the output value limits. You will need to add an offset to Output and Output_PER in the user program if you want an output value low limit of greater than 0.0.

---

**See also**

[Process value settings V1 (S7-1200, S7-1500)](#process-value-settings-v1-s7-1200-s7-1500)
  
[Process value monitoring V1 (S7-1200, S7-1500)](#process-value-monitoring-v1-s7-1200-s7-1500)
  
[PWM limits V1 (S7-1200, S7-1500)](#pwm-limits-v1-s7-1200-s7-1500)
  
[PID parameters V1 (S7-1200, S7-1500)](#pid-parameters-v1-s7-1200-s7-1500)

##### PID parameters V1 (S7-1200, S7-1500)

The PID parameters are displayed in the "PID Parameters" configuration window. The PID parameters will be adapted to your controlled system during controller tuning. You do not need to enter the PID parameters manually.

> **Note**
>
> The currently active PID parameters are located for PID_Compact V1 in the sRet structure and as of PID_Compact V2 in the Retain.CtrlParams structure.
>
> Change the currently active PID parameters only in "Inactive" mode online to prevent malfunction of the PID controller.
>
> If you want to change the PID parameters in "Automatic mode" or "Manual mode" online, change the PID parameters as follows:
>
> - PID_Compact V1: Change the PID parameters in the sBackUp structure and apply these changes with sPid_Cmpt.b_LoadBackUp = TRUE to the sRet structure.
> - PID_Compact as of V2: Change the PID parameters in the CtrlParamsBackUp structure and apply these changes with LoadBackUp = TRUE to the Retain.CtrlParams structure.
>
> Online changes to the PID parameters in "Automatic mode" can result in jumps at the output value.

The PID algorithm operates according to the following equation:

![Figure](images/172252714123_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| **Symbol** | **Description** |
| y | Output value of the PID algorithm |
| K<sub>p</sub> | Proportional gain |
| s | Laplace operator |
| b | Proportional action weighting |
| w | Setpoint |
| x | Process value |
| T<sub>I</sub> | Integration time |
| a | Derivative delay coefficient (derivative delay T1 = a × T<sub>D</sub>) |
| T<sub>D</sub> | Derivative action time |
| c | Derivative action weighting |

The diagram below illustrates the integration of the parameters into the PID algorithm:

![Figure](images/166014208907_DV_resource.Stream@PNG-en-US.png)

All PID parameters are retentive. If you enter the PID parameters manually, you must completely download PID_Compact.

[Downloading technology objects to device](Configuring%20a%20software%20controller.md#downloading-technology-objects-to-device)

###### Proportional gain

The value specifies the proportional gain of the controller. PID_Compact does not work with a negative proportional gain. Control logic is inverted under Basic settings &gt; Controller type.

###### Integration time

The integration time determines the time behavior of the integral action. The integral action is deactivated with integration time = 0.0. When the integration time is changed from a different value to 0.0 online in "Automatic mode", the previous integral action is deleted and the output value jumps.

###### Derivative action time

The derivative action time determines the time behavior of the derivative action. Derivative action is deactivated with derivative action time = 0.0.

###### Derivative delay coefficient

The derivative delay coefficient delays the effect of the derivative action.

Derivative delay = derivative action time × derivative delay coefficient

- 0.0: Derivative action is effective for one cycle only and therefore almost not effective.
- 0.5: This value has proved useful in practice for controlled systems with **one** dominant time constant.
- &gt; 1.0: The greater the coefficient, the longer the effect of the derivative action is delayed.

###### Proportional action weighting

The proportional action may weaken with changes to the setpoint.

Values from 0.0 to 1.0 are applicable.

- 1.0: Proportional action for setpoint change is fully effective
- 0.0: Proportional action for setpoint change is not effective

The proportional action is always fully effective when the process value is changed.

###### Derivative action weighting

The derivative action may weaken with changes to the setpoint.

Values from 0.0 to 1.0 are applicable.

- 1.0: Derivative action is fully effective upon setpoint change
- 0.0: Derivative action is not effective upon setpoint change

The derivative action is always fully effective when the process value is changed.

###### PID algorithm sampling time

The controlled system needs a certain amount of time to respond to changes in the output value. It is therefore not advisable to calculate the output value in every cycle. The sampling time of the PID algorithm represents the time between two calculations of the output value. It is calculated during tuning and rounded to a multiple of the cycle time. All other functions of PID_Compact are executed at every call.

If you use Output_PWM, the sampling time of the PID algorithm is used as the period duration of the pulse width modulation. The accuracy of the output signal is determined by the ratio of the PID algorithm sampling time to the cycle time of the OB. It is therefore recommended that the cycle time is a maximum of one tenth of the PID algorithm sampling time.

###### Rule for tuning

Select whether PI or PID parameters are to be calculated in the "Controller structure" drop-down list.

- **PID**

  Calculates PID parameters during pretuning and fine tuning.
- **PI**

  Calculates PI parameters during pretuning and fine tuning.
- **User-defined**

  The drop-down list displays "User-defined" if you have configured different controller structures for pretuning and fine tuning via a user program.

---

**See also**

[Selection of the controller structure for specified controlled systems](PID%20control.md#selection-of-the-controller-structure-for-specified-controlled-systems)

### Commissioning PID_Compact V1 (S7-1200, S7-1500)

This section contains information on the following topics:

- [Commissioning V1 (S7-1200, S7-1500)](#commissioning-v1-s7-1200-s7-1500)
- [Pretuning V1 (S7-1200, S7-1500)](#pretuning-v1-s7-1200-s7-1500)
- [Fine tuning V1 (S7-1200, S7-1500)](#fine-tuning-v1-s7-1200-s7-1500)
- ["Manual" mode V1 (S7-1200, S7-1500)](#manual-mode-v1-s7-1200-s7-1500)

#### Commissioning V1 (S7-1200, S7-1500)

The commissioning window helps you commission the PID controller. You can monitor the values for the setpoint, process value and output value along the time axis in the trend view. The following functions are supported in the commissioning window:

- Controller pretuning
- Controller fine tuning

  Use fine tuning for fine adjustments to the PID parameters.
- Monitoring the current closed-loop control in the trend view
- Testing the controlled system by specifying a manual output value

All functions require an online connection to the CPU to have been established.

##### Basic handling

- Select the desired sampling time in the "Sampling time" drop-down list.

  All values in the commissioning window are updated in the selected update time.
- Click the "Start" icon in the measuring group if you want to use the commissioning functions.

  Value recording is started. The current values for the setpoint, process value and output value are entered in the trend view. Operation of the commissioning window is enabled.
- Click the "Stop" icon if you want to end the commissioning functions.

  The values recorded in the trend view can continue to be analyzed.

Closing the commissioning window will terminate recording in the trend view and delete the recorded values.

---

**See also**

[Pretuning V1 (S7-1200, S7-1500)](#pretuning-v1-s7-1200-s7-1500)
  
[Fine tuning V1 (S7-1200, S7-1500)](#fine-tuning-v1-s7-1200-s7-1500)
  
["Manual" mode V1 (S7-1200, S7-1500)](#manual-mode-v1-s7-1200-s7-1500)

#### Pretuning V1 (S7-1200, S7-1500)

The pretuning determines the process response to a jump change of the output value and searches for the point of inflection. The tuned PID parameters are calculated as a function of the maximum slope and dead time of the controlled system.

The more stable the process value is, the easier it is to calculate the PID parameters and the more precise the result will be. Noise on the process value can be tolerated as long as the rate of rise of the process value is significantly higher compared to the noise. The PID parameters are backed up before being recalculated.

##### Requirement

- The "PID_Compact" instruction is called in a cyclic interrupt OB.
- ManualEnable = FALSE
- PID_Compact is in "inactive" or "manual" mode.
- The setpoint may not be changed during controller tuning. PID_Compact will otherwise be deactivated.
- The setpoint and the process value lie within the configured limits (see "Process value monitoring" configuration).
- The difference between setpoint and process value is greater than 30% of the difference between process value high limit and process value low limit.
- The distance between the setpoint and the process value is &gt; 50% of the setpoint.

##### Procedure

To perform pretuning, follow these steps:

1. Double-click the "PID_Compact &gt; Commissioning" entry in the project tree.
2. Select the entry "Pretuning" in the "Tuning mode" drop-down list.
3. Click the "Start" icon.

   - An online connection will be established.
   - Value recording is started.
   - Pretuning is started.
   - The "Status" field displays the current steps and any errors that may have occurred. The progress bar indicates the progress of the current step.

**Note**

Click the "Stop" icon when the progress bar has reached 100% and it is to be assumed the controller tuning function is blocked. Check the configuration of the technology object and, if necessary, restart controller tuning.

##### Result

If pretuning was performed without an error message, the PID parameters have been tuned. PID_Compact switches to automatic mode and uses the tuned parameters. The tuned PID parameters will be retained during power OFF and a restart of the CPU.

If pretuning is not possible, PID_Compact will change to "Inactive" mode.

---

**See also**

[Parameters State and sRet.i_Mode V1 (S7-1200)](PID_Compact%20%28S7-1200%2C%20S7-1500%29.md#parameters-state-and-sreti_mode-v1-s7-1200)
  
[Commissioning V1 (S7-1200, S7-1500)](#commissioning-v1-s7-1200-s7-1500)
  
[Fine tuning V1 (S7-1200, S7-1500)](#fine-tuning-v1-s7-1200-s7-1500)
  
["Manual" mode V1 (S7-1200, S7-1500)](#manual-mode-v1-s7-1200-s7-1500)

#### Fine tuning V1 (S7-1200, S7-1500)

Fine tuning generates a constant, limited oscillation of the process value. The PID parameters are optimized for the operating point from the amplitude and frequency of this oscillation. All PID parameters are recalculated on the basis of the findings. PID parameters from fine tuning usually have better master control and disturbance behavior than PID parameters from pretuning.

PID_Compact automatically attempts to generate an oscillation greater than the noise of the process value. Fine tuning is only minimally influenced by the stability of the process value. The PID parameters are backed up before being recalculated.

##### Requirement

- The PID_Compact instruction is called in a cyclic interrupt OB.
- ManualEnable = FALSE
- The setpoint and the process value lie within the configured limits (see "Process value monitoring" configuration).
- The control loop has stabilized at the operating point. The operating point is reached when the process value corresponds to the setpoint.
- No disturbances are expected.
- The setpoint may not be changed during controller tuning.
- PID_Compact is in inactive mode, automatic mode or manual mode.

##### Process depends on initial situation

Fine tuning can be started in "inactive", "automatic" or "manual" mode. Fine tuning proceeds as follows when started in:

- Automatic mode

  Start fine tuning in automatic mode if you wish to improve the existing PID parameters using controller tuning.

  PID_Comact will regulate using the existing PID parameters until the control loop has stabilized and the requirements for fine tuning have been met. Only then will fine tuning start.
- Inactive or manual mode

  If the requirements for pretuning are met, pretuning is started. The PID parameters established will be used for adjustment until the control loop has stabilized and the requirements for fine tuning have been met. Only then will fine tuning start. If pretuning is not possible, PID_Compact will change to "Inactive" mode.

  An attempt is made to reach the setpoint with a minimum or maximum output value if the process value for pretuning is already too near the setpoint. This can produce increased overshoot.

##### Procedure

Proceed as follows to carry out "fine tuning":

1. Select the entry "Fine tuning" in the "Tuning mode" drop-down list.
2. Click the "Start" icon.

   - An online connection will be established.
   - Value recording is started.
   - The process of fine tuning is started.
   - The "Status" field displays the current steps and any errors that may have occurred. The progress bar indicates the progress of the current step.

**Note**

Click the "Stop" icon in the "Tuning mode" group when the progress bar has reached 100% and it is to be assumed the controller tuning function is blocked. Check the configuration of the technology object and, if necessary, restart controller tuning.

##### Result

The PID parameters will have been optimized if fine tuning has been executed without errors. PID_Compact changes to automatic mode and uses the optimized parameters. The optimized PID parameters will be retained during power OFF and a restart of the CPU.

If errors occurred during "fine tuning", PID_Compact will change to "inactive" mode.

---

**See also**

[Parameters State and sRet.i_Mode V1 (S7-1200)](PID_Compact%20%28S7-1200%2C%20S7-1500%29.md#parameters-state-and-sreti_mode-v1-s7-1200)
  
[Commissioning V1 (S7-1200, S7-1500)](#commissioning-v1-s7-1200-s7-1500)
  
[Pretuning V1 (S7-1200, S7-1500)](#pretuning-v1-s7-1200-s7-1500)
  
["Manual" mode V1 (S7-1200, S7-1500)](#manual-mode-v1-s7-1200-s7-1500)

#### "Manual" mode V1 (S7-1200, S7-1500)

The following section describes how you can use the "Manual" operating mode in the commissioning window of the "PID Compact" technology object.

##### Requirement

- The "PID_Compact" instruction is called in a cyclic interrupt OB.
- An online connection to the CPU has been established and the CPU is in the "RUN" mode.
- The functions of the commissioning window have been enabled via the "Start" icon.

##### Procedure

Use "Manual mode" in the commissioning window if you want to test the controlled system by specifying a manual value. To define a manual value, proceed as follows:

1. Select the "Manual mode" check box in the "Online status of controller" area.

   PID_Compact operates in manual mode. The most recent current output value remains in effect.
2. Enter the manual value in the "Output" field as a % value.
3. Click the control icon ![Procedure](images/166014232715_DV_resource.Stream@PNG-de-DE.png).

##### Result

The manual value is written to the CPU and immediately goes into effect.

> **Note**
>
> PID_Compact continues to monitor the process value. If the process value limits are exceeded, PID_Compact is deactivated.

Clear the "Manual mode" check box if the output value is to be specified again by the PID controller. The switchover to automatic mode is bumpless.

---

**See also**

[Parameters State and sRet.i_Mode V1 (S7-1200)](PID_Compact%20%28S7-1200%2C%20S7-1500%29.md#parameters-state-and-sreti_mode-v1-s7-1200)
  
[Commissioning V1 (S7-1200, S7-1500)](#commissioning-v1-s7-1200-s7-1500)
  
[Pretuning V1 (S7-1200, S7-1500)](#pretuning-v1-s7-1200-s7-1500)
  
[Fine tuning V1 (S7-1200, S7-1500)](#fine-tuning-v1-s7-1200-s7-1500)

### Simulating PID_Compact V1 with PLCSIM (S7-1200, S7-1500)

> **Note**
>
> **Simulation with PLCSIM**
>
> For the simulation with PLCSIM, the time behavior of the simulated PLC is not exactly identical to that of a "real" PLC. The actual cycle clock of a cyclic interrupt OB can have larger fluctuations with a simulated PLC than with "real" PLCs.
>
> In the standard configuration, PID_Compact determines the time between calls automatically and monitors them for fluctuations.
>
> For a simulation of PID_Compact with PLCSIM, for example, a sampling time error (ErrorBits = DW#16#00000800) can therefore be detected.
>
> PID_Compact switches to "Inactive" mode (State = 0) in this case.
>
> To prevent this from happening, you should configure PID_Compact for simulation with PLCSIM as follows:
>
> - sb_EnCyclEstimation = FALSE
> - sb_EnCyclMonitoring = FALSE
> - sPid_Calc.r_Cycle: Assign the cycle clock of the calling cyclic interrupt OB in seconds to this tag.

---
title: "Using PID_3Step (S7-1200, S7-1500)"
package: TFTOPID3StepenUS
topics: 48
devices: [S7-1200, S7-1500, S7-1500T]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Using PID_3Step (S7-1200, S7-1500)

This section contains information on the following topics:

- [Technology object PID_3Step (S7-1200, S7-1500)](#technology-object-pid_3step-s7-1200-s7-1500)
- [PID_3Step V2 (S7-1200, S7-1500)](#pid_3step-v2-s7-1200-s7-1500)
- [PID_3Step V1 (S7-1200, S7-1500)](#pid_3step-v1-s7-1200-s7-1500)

## Technology object PID_3Step (S7-1200, S7-1500)

The technology object PID_3Step provides a PID controller with tuning for valves or actuators with integral response.

You can configure the following controllers:

- Three-point step controller with position feedback
- Three-point step controller without position feedback
- Valve controller with analog output value

PID_3Step continuously acquires the measured process value within a control loop and compares it with the setpoint. From the resulting control deviation, PID_3Step calculates an output value through which the process value reaches the setpoint as quickly and steadily as possible. The output value for the PID controller consists of three actions:

- **Proportional** action

  The proportional action of the output value increases in proportion to the control deviation.
- **I** action

  The integral action of the output value increases until the control deviation has been balanced.
- **D** action

  The derivative action increases with the rate of change of control deviation. The process value is corrected to the setpoint as quickly as possible. The derivative action will be reduced again if the rate of change of control deviation drops.

The instruction PID_3Step calculates the proportional, integral and derivative parameters for your controlled system during pretuning. Fine tuning can be used to tune the parameters further. You do not need to manually determine the parameters.

### Additional information

- [Overview of software controller](Configuring%20a%20software%20controller.md#overview-of-software-controller)
- [Add technology objects](Configuring%20a%20software%20controller.md#add-technology-objects)
- [Configure technology objects](Configuring%20a%20software%20controller.md#configure-technology-objects)
- [Configuring PID_3Step V2](#configuring-pid_3step-v2-s7-1200-s7-1500)
- [Configuring PID_3Step V1](#configuring-pid_3step-v1-s7-1200-s7-1500)

### Principle

For more information, see the following FAQs in the Siemens Industry Online Support:

- Entry ID [68011827](https://support.industry.siemens.com/cs/ww/en/view/68011827)

## PID_3Step V2 (S7-1200, S7-1500)

This section contains information on the following topics:

- [Configuring PID_3Step V2 (S7-1200, S7-1500)](#configuring-pid_3step-v2-s7-1200-s7-1500)
- [Commissioning PID_3Step V2 (S7-1200, S7-1500)](#commissioning-pid_3step-v2-s7-1200-s7-1500)
- [Simulating PID_3Step V2 with PLCSIM (S7-1200, S7-1500)](#simulating-pid_3step-v2-with-plcsim-s7-1200-s7-1500)

### Configuring PID_3Step V2 (S7-1200, S7-1500)

This section contains information on the following topics:

- [Basic settings V2 (S7-1200, S7-1500)](#basic-settings-v2-s7-1200-s7-1500)
- [Process value settings V2 (S7-1200, S7-1500)](#process-value-settings-v2-s7-1200-s7-1500)
- [Actuator settings V2 (S7-1200, S7-1500)](#actuator-settings-v2-s7-1200-s7-1500)
- [Advanced settings V2 (S7-1200, S7-1500)](#advanced-settings-v2-s7-1200-s7-1500)

#### Basic settings V2 (S7-1200, S7-1500)

This section contains information on the following topics:

- [Introduction V2 (S7-1200, S7-1500)](#introduction-v2-s7-1200-s7-1500)
- [Control mode V2 (S7-1200, S7-1500)](#control-mode-v2-s7-1200-s7-1500)
- [Setpoint V2 (S7-1200, S7-1500)](#setpoint-v2-s7-1200-s7-1500)
- [Process value V2 (S7-1200, S7-1500)](#process-value-v2-s7-1200-s7-1500)
- [Position feedback V2 (S7-1200, S7-1500)](#position-feedback-v2-s7-1200-s7-1500)
- [Output value V2 (S7-1200, S7-1500)](#output-value-v2-s7-1200-s7-1500)

##### Introduction V2 (S7-1200, S7-1500)

Configure the following properties of the "PID_3Step" technology object under "Basic settings" in the Inspector window or in the configuration window:

- Physical quantity
- Control logic
- Start-up behavior after reset
- Setpoint (only in the Inspector window)
- Process value (only in the Inspector window)
- Output value (only in the Inspector window)
- Position feedback (only in the Inspector window)

###### Setpoint, process value, output value and position feedback

You can only configure the setpoint, process value, output value and position feedback in the Inspector window of the programming editor. Select the source for each value:

- Instance DB

  The value saved in the instance DB is used.

  Value must be updated in the instance DB by the user program.

  There should be no value at the instruction.

  Change via HMI possible.
- Instruction

  The value connected to the instruction is used.   
  The value is written to the instance DB each time the instruction is called.

  No change via HMI possible.

##### Control mode V2 (S7-1200, S7-1500)

###### Physical quantity

Select the unit of measurement and physical quantity for the setpoint and the process value in the "Controller type" group. The setpoint and the process value are displayed in this unit.

###### Control logic

An increase of the output value is generally intended to cause an increase in the process value. This is referred to as a normal control logic.

PID_3Step does not work with negative proportional gain. Select the check box "Invert control logic" to reduce the process value with a higher output value.

Examples

- Opening the drain valve will reduce the level of a container's contents.
- Increasing cooling will reduce the temperature.

###### Startup characteristics

1. To switch to "Inactive" mode after CPU restart, clear the "Activate Mode after CPU restart" check box.

   To switch to the operating mode saved in the Mode parameter after CPU restart, select the "Activate Mode after CPU restart" check box.
2. In the "Set Mode to" drop-down list, select the mode that is to be enabled after a complete download to the device.

   After a complete download to the device, PID_3Step starts in the selected operating mode. With each additional restart, PID_3Step starts in the mode that was last saved in Mode.

Example

You have selected the "Activate Mode after CPU restart" check box and the entry "Pretuning" in the "Set Mode to" list. After a complete download to the device, PID_3Step starts in the "Pretuning" mode. If pretuning is still active, PID_3Step starts in "Pretuning" mode again after restart of the CPU. If pretuning was successfully completed and automatic mode is active, PID_3Step starts in "Automatic mode" after restart of the CPU.

##### Setpoint V2 (S7-1200, S7-1500)

###### Procedure

Proceed as follows to define a fixed setpoint:

1. Select "Instance DB".
2. Enter a setpoint, e.g. 80° C.
3. Delete any entry in the instruction.

Proceed as follows to define a variable setpoint:

1. Select "Instruction".
2. Enter the name of the REAL variable in which the setpoint is saved.

   Program-controlled assignment of various values to the REAL variable is possible, for example for the time controlled change of the setpoint.

##### Process value V2 (S7-1200, S7-1500)

PID_3Step will scale the value of the analog input to the physical quantity if you use the analog input value directly.

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

##### Position feedback V2 (S7-1200, S7-1500)

Position feedback configuration depends upon the actuator used.

- Actuator without position feedback
- Actuator with digital endstop signals
- Actuator with analog position feedback
- Actuator with analog position feedback and endstop signals

###### Actuator without position feedback

Proceed as follows to configure PID_3Step for an actuator without position feedback:

1. Select the entry "No Feedback" in the drop-down list "Feedback".

###### Actuator with digital endstop signals

Proceed as follows to configure PID_3Step for an actuator with endstop signals:

1. Select the entry "No Feedback" in the drop-down list "Feedback".
2. Activate the "Actuator endstop signals" check box.
3. Select "Instruction" as source for Actuator_H and Actuator_L.
4. Enter the addresses of the digital inputs for Actuator_H and Actuator_L.

###### Actuator with analog position feedback

Proceed as follows to configure PID_3Step for an actuator with analog position feedback:

1. Select the entry "Feedback" or "Feedback_PER" in the drop-down list "Feedback".

   - Use the analog input value for Feedback_PER. Configure Feedback_PER scaling in the actuator settings.
   - Process the analog input value for Feedback using your user program.
2. Select "Instruction" as source.
3. Enter the address of the analog input or the variable of your user program.

###### Actuator with analog position feedback and endstop signals

Proceed as follows to configure PID_3Step for an actuator with analog position feedback and endstop signals:

1. Select the entry "Feedback" or "Feedback_PER" in the drop-down list "Feedback".
2. Select "Instruction" as source.
3. Enter the address of the analog input or the variable of your user program.
4. Activate the "Actuator endstop signals" check box.
5. Select "Instruction" as source for Actuator_H and Actuator_L.
6. Enter the addresses of the digital inputs for Actuator_H and Actuator_L.

##### Output value V2 (S7-1200, S7-1500)

PID_3Step offers an analog output value (Output_PER) and digital output values (Output_UP, Output_DN). Your actuator will determine which output value you use.

- Output_PER

  The actuator has a relevant motor transition time and is triggered via an analog output and controlled with a continuous signal, e.g. 0...10 V or 4...20 mA. The value at Output_PER corresponds to the target position of the valve, e.g. Output_PER = 13824, when the valve is to be opened by 50%.

  For auto-tuning and anti windup behavior, for example, PID_3Step takes into consideration that the analog output value has a delayed effect on the process due to the motor transition time. If no relevant motor transition time is in effect in your process (e.g. with solenoid valves), so that the output value has a direct and full effect on the process, use PID_Compact instead.
- Output_UP, Output_DN

  The actuator has a relevant motor transition time and is controlled by two digital outputs.   
  Output_UP moves the valve in the open state direction.   
  Output_DN moves the valve in the closed state direction.

The motor transition time is taken into consideration in the calculation of the analog output value as well as in the calculation of the digital output values. It is mainly required for correct operation during auto-tuning and the anti-windup behavior. You should therefore configure the motor transition time under "Actuator settings" with the value that the motor requires to move the actuator from the closed to the opened state.

###### Procedure

Proceed as follows to use the analog output value:

1. Select the entry "Output (analog)" in the drop-down list "Output".
2. Select "Instruction".
3. Enter the address of the analog output.

Proceed as follows to use the digital output value:

1. Select the entry "Output (digital)" in the drop-down list "Output".
2. Select "Instruction" for Output_UP and Output_DN.
3. Enter the addresses of the digital outputs.

Proceed as follows to process the output value using the user program:

1. Select the entry corresponding to the actuator in the drop-down list "Output".
2. Select "Instruction".
3. Enter the name of the tag you are using to process the output value.
4. Transfer the processed output value to the actuator by means of an analog or digital CPU output.

#### Process value settings V2 (S7-1200, S7-1500)

This section contains information on the following topics:

- [Process value scaling V2 (S7-1200, S7-1500)](#process-value-scaling-v2-s7-1200-s7-1500)
- [Process value limits V2 (S7-1200, S7-1500)](#process-value-limits-v2-s7-1200-s7-1500)

##### Process value scaling V2 (S7-1200, S7-1500)

If you have configured the use of Input_PER in the basic setting, you must convert the value of the analog input to the physical quantity of the process value. The current configuration is displayed in the Input_PER display.

Input_PER will be scaled using a low and high value pair if the process value is directly proportional to the value of the analog input.

###### Procedure

To scale the process value, follow these steps:

1. Enter the low pair of values in the "Scaled low process value" and "Low" text boxs.
2. Enter the high pair of values in the "Scaled high process value" and "High" input boxes.

Default settings for the value pairs are stored in the hardware configuration. To use the value pairs from the hardware configuration, follow these steps:

1. Select the PID_3Step instruction in the programming editor.
2. Interconnect Input_PER with an analog input in the basic settings.
3. Click the "Automatic setting" button in the process value settings.

The existing values will be overwritten with the values from the hardware configuration.

##### Process value limits V2 (S7-1200, S7-1500)

You must specify an appropriate absolute high limit and low limit for the process value as limit values for your controlled system. As soon as the process value violates these limits, an error occurs (ErrorBits = 0001h). Tuning is canceled when the process value limits are violated. You can specify how PID_3Step responds to errors in automatic mode in the actuator settings.

#### Actuator settings V2 (S7-1200, S7-1500)

This section contains information on the following topics:

- [Actuator V2 (S7-1200, S7-1500)](#actuator-v2-s7-1200-s7-1500)
- [Feedback scaling V2 (S7-1200, S7-1500)](#feedback-scaling-v2-s7-1200-s7-1500)
- [Output value limits V2 (S7-1200, S7-1500)](#output-value-limits-v2-s7-1200-s7-1500)

##### Actuator V2 (S7-1200, S7-1500)

###### Actuator-specific times

Configure the motor transition time and the minimum ON and OFF times to prevent damage to the actuator. You can find the specifications in the actuator data sheet.

The motor transition time is the time in seconds the motor requires to move the actuator from the closed to the opened state. You can measure the motor transition time during commissioning.

The motor transition time is taken into consideration in the calculation of the analog output value as well as in the calculation of the digital output values. It is mainly required for correct operation during auto-tuning and the anti-windup behavior.

If no relevant motor transition time is in effect in your process (e.g. with solenoid valves), so that the output value has a direct and full effect on the process, use PID_Compact instead.

The motor transition time is retentive. If you enter the motor transition time manually, you must completely download PID_3Step.

[Downloading technology objects to device](Configuring%20a%20software%20controller.md#downloading-technology-objects-to-device)

If you are using "Output_UP" or "Output_DN", you can reduce the switching frequency with the minimum on and minimum OFF time.

The on or off times calculated are totaled in automatic mode and only become effective when the sum is greater than or equal to the minimum on or OFF time.

Manual_UP = TRUE or Manual_DN = TRUE in manual mode operates the actuator for at least the minimum ON or OFF time.

If you have selected the analog output value Output_PER, the minimum ON time and the minimum OFF time are not evaluated and cannot be changed.

###### Reaction to error

PID_3Step is preset so that the controller stays active in most cases in the event of an error. If errors occur frequently in controller mode, this default reaction has a negative effect on the control response. In this case, check the Errorbits parameter and eliminate the cause of the error.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Your system may be damaged.**  If you output "Current value while error pending" or "Substitute output value while error pending" in the event of an error, PID_3Step remains in automatic mode even if the process value limits are violated. This may damage your system.   It is essential to configure how your controlled system reacts in the event of an error to protect your system from damage. |  |

PID_3Step generates a programmable output value in the case of an error:

- Current value

  PID_3Step is switched off and no longer modifies the actuator position.
- Current value for error while error is pending

  The controller functions of PID_3Step are switched off and the position of the actuator is no longer changed.

  If the following errors occur in automatic mode, PID_3Step returns to automatic mode as soon as the errors are no longer pending.

  - 0002h: Invalid value at Input_PER parameter.
  - 0200h: Invalid value at Input parameter.
  - 0400h: Calculation of output value failed.
  - 1000h: Invalid value at Setpoint parameter.
  - 2000h: Invalid value at Feedback_PER parameter.
  - 4000h: Invalid value at Feedback parameter.
  - 8000h: Error during digital position feedback.
  - 20000h: Invalid value at SavePosition tag.

  If one or more of the following errors occur, PID_3Step stays in   
  automatic mode:

  - 0001h: The Input parameter is outside the process value limits.
  - 0800h: Sampling time error
  - 40000h: Invalid value at Disturbance parameter.

  PID_3Step remains in manual mode if an error occurs in manual mode.

  If an error occurs during tuning or transition time measurement, PID_3Step switches to the mode in which tuning or transition time measurement was started. Only in the event of the following error is tuning not aborted:

  - 0020h: Pretuning is not permitted during fine tuning.
- Substitute output value

  PID_3Step moves the actuator to the substitute output value and then switches off.
- Substitute output value while error is pending

  PID_3Step moves the actuator to the substitute output value. When the substitute output value is reached, PID_3Step reacts as it does with "Current value for while error is pending".

Enter the substitute output value in "%".

Only substitute output values 0% and 100% can be configured when using Output_UP and Output_DN without analog position feedback (Config.OutputPerOn = FALSE and Config.FeedbackOn = FALSE). To reach the high or low endstop, the actuator is moved in the corresponding direction. If endstops are available (Config.ActuatorEndStopOn = TRUE), Output_UP and Output_DN are reset with Actuator_H = TRUE or Actuator_L = TRUE. If no endstop signals are available (Config.ActuatorEndStopOn = FALSE), Output_UP and Output_DN are reset after a travel time of Config.VirtualActuatorLimit * Retain.TransitTime/100.

Any substitute output values within the output value limits can be configured when using Output_PER or analog position feedback (Config.OutputPerOn = TRUE or Config.FeedbackOn = TRUE).

##### Feedback scaling V2 (S7-1200, S7-1500)

###### Scaling position feedback

If you have configured the use of Feedback_PER in the basic settings, you will need to convert the value of the analog input into %. The current configuration will be displayed in the "Feedback" display.

Feedback_PER is scaled using a low and high value pair.

1. Enter the low pair of values in the "Low endstop" and "Low" input boxes.
2. Enter the high pair of values in the "High endstop" and "High" input boxes.

"Low endstop" must be less than "High endstop"; "Low" must be less than "High".

The valid values for "High endstop" and "Low endstop" depend upon:

- No Feedback, Feedback, Feedback_PER
- Output (analog), Output (digital)

| Output | Feedback | Low endstop | High endstop |
| --- | --- | --- | --- |
| Output (digital) | No Feedback | Cannot be set (0.0%) | Cannot be set (100.0%) |
| Output (digital) | Feedback | -100.0% or 0.0% | 0.0% or +100.0% |
| Output (digital) | Feedback_PER | -100.0% or 0.0% | 0.0% or +100.0% |
| Output (analog) | No Feedback | Cannot be set (0.0%) | Cannot be set (100.0%) |
| Output (analog) | Feedback | -100.0% or 0.0% | 0.0% or +100.0% |
| Output (analog) | Feedback_PER | -100.0% or 0.0% | 0.0% or +100.0% |

##### Output value limits V2 (S7-1200, S7-1500)

###### Limiting the output value

You can exceed or undershoot the output value limits during the transition time measurement and with mode = 10. The output value is limited to these values in all other modes.

Enter the absolute output value limits in the "Output value high limit" and "Output value low limit" input boxes. The output value limits must be within "Low endstop" and "High endstop".

If no Feedback is available and Output (digital) is set, you cannot limit the output value. Output_UP and Output_DN are then reset upon Actuator_H = TRUE or Actuator_L = TRUE. If no endstop signals are available, Output_UP and Output_DN are reset after a travel time of 150% of the motor actuating time.

The default value of 150% can be adjusted using the tagConfig.VirtualActuatorLimit. As of PID_3Step Version 2.3 the monitoring and limiting of the travel time can be deactivated with Config.VirtualActuatorLimit = 0.0.

#### Advanced settings V2 (S7-1200, S7-1500)

This section contains information on the following topics:

- [Process value monitoring V2 (S7-1200, S7-1500)](#process-value-monitoring-v2-s7-1200-s7-1500)
- [PID parameters V2 (S7-1200, S7-1500)](#pid-parameters-v2-s7-1200-s7-1500)

##### Process value monitoring V2 (S7-1200, S7-1500)

Configure a warning high and low limit for the process value in the "Process value monitoring" configuration window. If one of the warning limits is exceeded or undershot during operation, a warning will be displayed at the PID_3Step instruction:

- At the InputWarning_H output parameter if the warning high limit has been exceeded
- At the InputWarning_L output parameter if the warning low limit has been undershot

The warning limits must be within the process value high and low limits.

The process value high and low limits will be used if you do not enter values.

###### Example

Process value high limit = 98° C; warning high limit = 90° C

Warning low limit = 10° C; process value low limit = 0° C

PID_3Step will respond as follows:

| Process value | InputWarning_H | InputWarning_L | ErrorBits | Operating mode |
| --- | --- | --- | --- | --- |
| > 98° C | TRUE | FALSE | 0001h | As configured |
| ≤ 98° C and > 90° C | TRUE | FALSE | 0000h | Automatic mode |
| ≤ 90° C and ≥ 10° C | FALSE | FALSE | 0000h | Automatic mode |
| < 10° C and ≥ 0° C | FALSE | TRUE | 0000h | Automatic mode |
| < 0° C | FALSE | TRUE | 0001h | As configured |

In the actuator settings, you can configure the response of PID_3Step when the process value high limit or low limit is violated.

##### PID parameters V2 (S7-1200, S7-1500)

The PID parameters are displayed in the "PID Parameters" configuration window. The PID parameters will be adapted to your controlled system during controller tuning. You do not need to enter the PID parameters manually.

> **Note**
>
> The currently active PID parameters are located in the Retain.CtrlParams structure.
>
> Change the currently active PID parameters only in "Inactive" mode online to prevent malfunction of the PID controller.
>
> If you want to change the PID parameters in "Automatic mode" or "Manual mode" online, change the PID parameters in the CtrlParamsBackUp structure and apply these changes to the Retain.CtrlParams structure as follows:
>
> - PID_3Step V1: Apply the changes with Config.LoadBackUp = TRUE
> - PID_3Step V2: Apply the changes with LoadBackUp = TRUE
>
> Online changes to the PID parameters in "Automatic mode" can result in jumps at the output value.

The PID algorithm operates according to the following equation:

![Figure](images/166014278155_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| Δy | Output value of the PID algorithm |
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

![Figure](images/166014272651_DV_resource.Stream@PNG-de-DE.png)

All PID parameters are retentive. If you enter the PID parameters manually, you must completely download PID_3Step.

[Downloading technology objects to device](Configuring%20a%20software%20controller.md#downloading-technology-objects-to-device)

###### Proportional gain

The value specifies the proportional gain of the controller. PID_3Step does not work with a negative proportional gain. Control logic is inverted under Basic settings > Controller type.

###### Integration time

The integration time determines the time behavior of the integral action. The integral action is deactivated with integration time = 0.0. When the integration time is changed from a different value to 0.0 online in "Automatic mode", the previous integral action is deleted and the output value jumps.

###### Derivative action time

The derivative action time determines the time behavior of the derivative action. Derivative action is deactivated with derivative action time = 0.0.

###### Derivative delay coefficient

The derivative delay coefficient delays the effect of the derivative action.

Derivative delay = derivative action time × derivative delay coefficient

- 0.0: Derivative action is effective for one cycle only and therefore almost not effective.
- 0.5: This value has proved useful in practice for controlled systems with **one** dominant time constant.
- > 1.0: The greater the coefficient, the longer the effect of the derivative action is delayed.

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

The controlled system needs a certain amount of time to respond to changes in the output value. It is therefore not advisable to calculate the output value in every cycle. The sampling time of the PID algorithm represents the time between two calculations of the output value. It is calculated during tuning and rounded to a multiple of the PID_3Step sampling time. All other functions of PID_3Step are executed at every call.

###### Dead zone width

The dead zone suppresses the noise component in the steady controller state. The dead zone width specifies the size of the dead zone. The dead zone is off if the dead zone width is 0.0.

If values not equal to 1.0 are configured for the proportional action weighting or the derivative action weighting, setpoint changes even within the dead zone affect the output value.  
Process value changes within the dead zone do not affect the output value, regardless of the weighting.

---

**See also**

[Selection of the controller structure for specified controlled systems](PID%20control.md#selection-of-the-controller-structure-for-specified-controlled-systems)

### Commissioning PID_3Step V2 (S7-1200, S7-1500)

This section contains information on the following topics:

- [Pretuning V2 (S7-1200, S7-1500)](#pretuning-v2-s7-1200-s7-1500)
- [Fine tuning V2 (S7-1200, S7-1500)](#fine-tuning-v2-s7-1200-s7-1500)
- [Commissioning with manual PID parameters V2 (S7-1200, S7-1500)](#commissioning-with-manual-pid-parameters-v2-s7-1200-s7-1500)
- [Measuring the motor transition time V2 (S7-1200, S7-1500)](#measuring-the-motor-transition-time-v2-s7-1200-s7-1500)

#### Pretuning V2 (S7-1200, S7-1500)

The pretuning determines the process response to a pulse of the output value and searches for the point of inflection. The tuned PID parameters are calculated as a function of the maximum slope and dead time of the controlled system. You obtain the best PID parameters when you perform pretuning and fine tuning.

The more stable the process value is, the easier it is to calculate the PID parameters and the more precise the result will be. Noise on the process value can be tolerated as long as the rate of rise of the process value is significantly higher compared to the noise. This is most likely the case in operating modes "Inactive" and "manual mode". The PID parameters are backed up before being recalculated.

The setpoint is frozen during pretuning.

##### Requirement

- The PID_3Step instruction is called in a cyclic interrupt OB.
- ManualEnable = FALSE
- Reset = FALSE
- The motor transition time has been configured or measured.
- PID_3Step is in one of the following modes: "Inactive", "Manual mode", or "Automatic mode".
- The setpoint and the process value lie within the configured limits (see "Process value settings" configuration).

##### Procedure

To perform pretuning, follow these steps:

1. Double-click the "PID_3Step > Commissioning" entry in the project tree.
2. Select the entry "Pretuning" in the "Tuning mode" drop-down list in the working area "Tuning".
3. Click the "Start" icon.

   - An online connection will be established.
   - Value recording is started.
   - Pretuning is started.
   - The "Status" field displays the current steps and any errors that may have occurred. The progress bar indicates the progress of the current step.

**Note**

Click the "Stop" icon when the progress bar has reached 100% and it is to be assumed the controller tuning function is blocked. Check the configuration of the technology object and, if necessary, restart controller tuning.

##### Result

If pretuning was performed without an error message, the PID parameters have been tuned. PID_3Step switches to automatic mode and uses the tuned parameters. The tuned PID parameters will be retained during power OFF and a restart of the CPU.

If pretuning is not possible, PID_3Step responds with the configured reaction to errors.

#### Fine tuning V2 (S7-1200, S7-1500)

Fine tuning generates a constant, limited oscillation of the process value. The PID parameters are tuned for the operating point from the amplitude and frequency of this oscillation. All PID parameters are recalculated from the results. PID parameters from fine tuning usually have better master control and disturbance characteristics than PID parameters from pretuning. You obtain the best PID parameters when you perform pretuning and fine tuning.

PID_3Step automatically attempts to generate an oscillation greater than the noise of the process value. Fine tuning is only minimally influenced by the stability of the process value. The PID parameters are backed up before being recalculated.

The setpoint is frozen during fine tuning.

##### Requirement

- The PID_3Step instruction is called in a cyclic interrupt OB.
- ManualEnable = FALSE
- Reset = FALSE
- The motor transition time has been configured or measured.
- The setpoint and the process value lie within the configured limits (see "Process value settings" configuration).
- The control loop has stabilized at the operating point. The operating point is reached when the process value corresponds to the setpoint.
- No disturbances are expected.
- PID_3Step is in inactive mode, automatic mode or manual mode.

##### Process depends on initial situation

Fine tuning proceeds as follows when started from:

- Automatic mode

  Start fine tuning from automatic mode if you wish to improve the existing PID parameters through tuning.

  PID_3Step controls the system using the existing PID parameters until the control loop has stabilized and the requirements for fine tuning have been met. Only then will fine tuning start.
- Inactive or manual mode

  Pretuning is always started first. The determined PID parameters will be used for control until the control loop has stabilized and the requirements for fine tuning have been met. Only then will fine tuning start.

##### Procedure

To perform fine tuning, follow these steps:

1. Select the entry "Fine tuning" in the "Tuning mode" drop-down list.
2. Click the "Start" icon.

   - An online connection will be established.
   - Value recording is started.
   - The process of fine tuning is started.
   - The "Status" field displays the current steps and any errors that may have occurred. The progress bar indicates the progress of the current step.

**Note**

Click the "Stop" icon in the "Tuning mode" group when the progress bar has reached 100% and it is to be assumed the controller tuning function is blocked. Check the configuration of the technology object and, if necessary, restart controller tuning.

##### Result

If no errors occurred during fine tuning, the PID parameters have been tuned. PID_3Step switches to automatic mode and uses the tuned parameters. The tuned PID parameters will be retained during power OFF and a restart of the CPU.

If errors occurred during fine tuning, PID_3Step responds with the configured response to errors.

#### Commissioning with manual PID parameters V2 (S7-1200, S7-1500)

##### Requirement

- The PID_3Step instruction is called in a cyclic interrupt OB.
- ManualEnable = FALSE
- Reset = FALSE
- The motor transition time has been configured or measured.
- PID_3Step is in "inactive" mode.
- The setpoint and the process value lie within the configured limits (see "Process value settings" configuration).

##### Procedure

Proceed as follows to commission PID_3Step with manual PID parameters:

1. Double-click on "PID_3Step > Configuration" in the project tree.
2. Click on "Advanced settings > PID Parameters" in the configuration window.
3. Select the check box "Enable direct input".
4. Enter the PID parameters.
5. Double-click the "PID_3Step > Commissioning" entry in the project tree.
6. Establish an online connection to the CPU.
7. Load the PID parameters to the CPU.
8. Click the "Start PID_3Step" icon.

##### Result

PID_3Step changes to automatic mode and controls using the current PID parameters.

---

**See also**

[PID parameters V2 (S7-1200, S7-1500)](#pid-parameters-v2-s7-1200-s7-1500)

#### Measuring the motor transition time V2 (S7-1200, S7-1500)

##### Introduction

PID_3Step requires the motor transition time to be as accurate as possible for good controller results. The data in the actuator documentation contains average values for this type of actuator. The value for the specific actuator used may differ.

You can measure the motor transition time during commissioning if you are using actuators with position feedback or endstop signals. The output value limits are not taken into consideration during the motor transition time measurement. The actuator can travel to the high or the low endstop.

The motor transition time cannot be measured if neither position feedback nor endstop signals are available.

##### Actuators with analog position feedback

Proceed as follows to measure motor transition time with position feedback:

**Requirement**

- Feedback or Feedback_PER has been selected in the basic settings and the signal has been connected.
- An online connection to the CPU has been established.

1. Select the "Use position feedback" check box.
2. Enter the position to which the actuator is to be moved in the "Target position" input field.

   The current position feedback (starting position) will be displayed. The difference between "Target position" and "Position feedback" must be at least 50% of the valid output value range.
3. Click the "Start" icon.

##### Result

The actuator is moved from the starting position to the target position. Time measurement starts immediately and ends when the actuator reaches the target position. The motor transition time is calculated according to the following equation:

Motor transition time = (output value high limit – output value low limit) × Measuring time / AMOUNT (target position – starting position).

The progress and status of transition time measurement are displayed. The transition time measured is saved in the instance data block on the CPU and displayed in the "Measured transition time" field. When the transition time measurement is ended and ActivateRecoverMode = TRUE, PID_3Step switches to the operating mode from which the transition time measurement was started. If the transition time measurement is ended and ActivateRecoverMode = FALSE, PID_3Step changes to "Inactive" mode.

> **Note**
>
> Click on the icon ![Result](images/166014016267_DV_resource.Stream@PNG-de-DE.png) "Upload measured transition time" to load the motor transition time measured to the project.

##### Actuators with endstop signals

Proceed as follows to measure the transition time of actuators with endstop signals:

**Requirement**

- The "Endstop signals" check box in the basic settings has been selected and Actuator_H and Actuator_L are connected.
- An online connection to the CPU has been established.

Proceed as follows to measure motor transition time with endstop signals:

1. Select the "Use actuator endstop signals" check box.
2. Select the direction in which the actuator is to be moved.

   - Open - Close - Open

     The actuator is moved first to the high endstop, then to the low endstop and then back to the high endstop.
   - Close - Open - Close

     The actuator is moved first to the low endstop, then to the high endstop and then back to the low endstop.
3. Click the "Start" icon.

##### Result

The actuator is moved in the selected direction. Time measurement will start once the actuator has reached the first endstop and will end when the actuator reaches this endstop for the second time. The motor transition time is equal to the time measured divided by two.

The progress and status of transition time measurement are displayed. The transition time measured is saved in the instance data block on the CPU and displayed in the "Measured transition time" field. When the transition time measurement is ended and ActivateRecoverMode = TRUE, PID_3Step switches to the operating mode from which the transition time measurement was started. If the transition time measurement is ended and ActivateRecoverMode = FALSE, PID_3Step changes to "Inactive" mode.

##### Cancelling transition time measurement

PID_3Step switches to "Inactive" mode if you cancel transition time measurement by pressing the Stop button.

### Simulating PID_3Step V2 with PLCSIM (S7-1200, S7-1500)

> **Note**
>
> **Simulation with PLCSIM**
>
> The simulation of PID_3Step V2.x with PLCSIM for CPU S7-1200 is not supported.
>
> PID_3Step V2.x can only be simulated for CPU S7-1500 with PLCSIM.
>
> For the simulation with PLCSIM, the time behavior of the simulated PLC is not exactly identical to that of a "real" PLC. The actual cycle clock of a cyclic interrupt OB can have larger fluctuations with a simulated PLC than with "real" PLCs.
>
> In the standard configuration, PID_3Step determines the time between calls automatically and monitors them for fluctuations.
>
> For a simulation of PID_3Step with PLCSIM, for example, a sampling time error ((ErrorBits = DW#16#00000800) can therefore be detected.
>
> This results in ongoing tuning being aborted.
>
> The response in automatic mode depends on the value of the ActivateRecoverMode tag.
>
> To prevent this from happening, you should configure PID_3Step for simulation with PLCSIM as follows:
>
> - CycleTime.EnEstimation = FALSE
> - CycleTime.EnMonitoring = FALSE
> - CycleTime.Value: Assign the cycle clock of the calling cyclic interrupt OB in seconds to this tag.

## PID_3Step V1 (S7-1200, S7-1500)

This section contains information on the following topics:

- [Configuring PID_3Step V1 (S7-1200, S7-1500)](#configuring-pid_3step-v1-s7-1200-s7-1500)
- [Commissioning PID_3Step V1 (S7-1200, S7-1500)](#commissioning-pid_3step-v1-s7-1200-s7-1500)
- [Simulating PID_3Step V1 with PLCSIM (S7-1200, S7-1500)](#simulating-pid_3step-v1-with-plcsim-s7-1200-s7-1500)

### Configuring PID_3Step V1 (S7-1200, S7-1500)

This section contains information on the following topics:

- [Basic settings V1 (S7-1200, S7-1500)](#basic-settings-v1-s7-1200-s7-1500)
- [Process value settings V1 (S7-1200, S7-1500)](#process-value-settings-v1-s7-1200-s7-1500)
- [Actuator settings V1 (S7-1200, S7-1500)](#actuator-settings-v1-s7-1200-s7-1500)
- [Advanced settings V1 (S7-1200, S7-1500)](#advanced-settings-v1-s7-1200-s7-1500)

#### Basic settings V1 (S7-1200, S7-1500)

This section contains information on the following topics:

- [Introduction V1 (S7-1200, S7-1500)](#introduction-v1-s7-1200-s7-1500)
- [Control mode V1 (S7-1200, S7-1500)](#control-mode-v1-s7-1200-s7-1500)
- [Setpoint V1 (S7-1200, S7-1500)](#setpoint-v1-s7-1200-s7-1500)
- [Process value V1 (S7-1200, S7-1500)](#process-value-v1-s7-1200-s7-1500)
- [Position feedback V1 (S7-1200, S7-1500)](#position-feedback-v1-s7-1200-s7-1500)
- [Output value V1 (S7-1200, S7-1500)](#output-value-v1-s7-1200-s7-1500)

##### Introduction V1 (S7-1200, S7-1500)

Configure the following properties of the "PID_3Step" technology object under "Basic settings" in the Inspector window or in the configuration window:

- Physical quantity
- Control logic
- Start-up behavior after reset
- Setpoint (only in the Inspector window)
- Process value (only in the Inspector window)
- Output value (only in the Inspector window)
- Position feedback (only in the Inspector window)

###### Setpoint, process value, output value and position feedback

You can only configure the setpoint, process value, output value and position feedback in the Inspector window of the programming editor. Select the source for each value:

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

PID_3Step does not work with negative proportional gain. Select the check box "Invert control logic" to reduce the process value with a higher output value.

Examples

- Opening the drain valve will reduce the level of a container's contents.
- Increasing cooling will reduce the temperature.

###### Start-up behavior after reset

To change straight to the last active mode after restarting the CPU, select the "Enable last mode after CPU restart" check box.

PID_3Step will remain in "Inactive" mode if the check box is cleared.

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

PID_3Step will scale the value of the analog input to the physical quantity if you use the analog input value directly.

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

##### Position feedback V1 (S7-1200, S7-1500)

Position feedback configuration depends upon the actuator used.

- Actuator without position feedback
- Actuator with digital endstop signals
- Actuator with analog position feedback
- Actuator with analog position feedback and endstop signals

###### Actuator without position feedback

Proceed as follows to configure PID_3Step for an actuator without position feedback:

1. Select the entry "No Feedback" in the drop-down list "Feedback".

###### Actuator with digital endstop signals

Proceed as follows to configure PID_3Step for an actuator with endstop signals:

1. Select the entry "No Feedback" in the drop-down list "Feedback".
2. Activate the "Actuator endstop signals" check box.
3. Select "Instruction" as source for Actuator_H and Actuator_L.
4. Enter the addresses of the digital inputs for Actuator_H and Actuator_L.

###### Actuator with analog position feedback

Proceed as follows to configure PID_3Step for an actuator with analog position feedback:

1. Select the entry "Feedback" or "Feedback_PER" in the drop-down list "Feedback".

   - Use the analog input value for Feedback_PER. Configure Feedback_PER scaling in the actuator settings.
   - Process the analog input value for Feedback using your user program.
2. Select "Instruction" as source.
3. Enter the address of the analog input or the variable of your user program.

###### Actuator with analog position feedback and endstop signals

Proceed as follows to configure PID_3Step for an actuator with analog position feedback and endstop signals:

1. Select the entry "Feedback" or "Feedback_PER" in the drop-down list "Feedback".
2. Select "Instruction" as source.
3. Enter the address of the analog input or the variable of your user program.
4. Activate the "Actuator endstop signals" check box.
5. Select "Instruction" as source for Actuator_H and Actuator_L.
6. Enter the addresses of the digital inputs for Actuator_H and Actuator_L.

##### Output value V1 (S7-1200, S7-1500)

PID_3Step offers an analog output value (Output_PER) and digital output values (Output_UP, Output_DN). Your actuator will determine which output value you use.

- Output_PER

  The actuator has a relevant motor transition time and is triggered via an analog output and controlled with a continuous signal, e.g. 0...10 V or 4...20 mA. The value at Output_PER corresponds to the target position of the valve, e.g. Output_PER = 13824, when the valve is to be opened by 50%.

  For auto-tuning and anti windup behavior, for example, PID_3Step takes into consideration that the analog output value has a delayed effect on the process due to the motor transition time. If no relevant motor transition time is in effect in your process (e.g. with solenoid valves), so that the output value has a direct and full effect on the process, use PID_Compact instead.
- Output_UP, Output_DN

  The actuator has a relevant motor transition time and is controlled by two digital outputs.   
  Output_UP moves the valve in the open state direction.   
  Output_DN moves the valve in the closed state direction.

The motor transition time is taken into consideration in the calculation of the analog output value as well as in the calculation of the digital output values. It is mainly required for correct operation during auto-tuning and the anti-windup behavior. You should therefore configure the motor transition time under "Actuator settings" with the value that the motor requires to move the actuator from the closed to the opened state.

###### Procedure

Proceed as follows to use the analog output value:

1. Select the entry "Output (analog)" in the drop-down list "Output".
2. Select "Instruction".
3. Enter the address of the analog output.

Proceed as follows to use the digital output value:

1. Select the entry "Output (digital)" in the drop-down list "Output".
2. Select "Instruction" for Output_UP and Output_DN.
3. Enter the addresses of the digital outputs.

Proceed as follows to process the output value using the user program:

1. Select the entry corresponding to the actuator in the drop-down list "Output".
2. Select "Instruction".
3. Enter the name of the tag you are using to process the output value.
4. Transfer the processed output value to the actuator by means of an analog or digital CPU output.

#### Process value settings V1 (S7-1200, S7-1500)

Configure the scaling of your process value and specify the process value absolute limits In the "Process value settings" configuration window.

##### Scaling the process value

If you have configured the use of Input_PER in the basic settings, you will need to convert the value of the analog input into the physical quantity of the process value. The current configuration will be displayed in the Input_PER display.

Input_PER will be scaled using a low and high value pair if the process value is directly proportional to the value of the analog input.

1. Enter the low pair of values in the "Scaled low process value" and "Low" input fields.
2. Enter the high pair of values in the "Scaled high process value" and "High" input boxes.

Default settings for the value pairs are saved in the hardware configuration. Proceed as follows to use the value pairs from the hardware configuration:

1. Select the instruction PID_3Step in the programming editor.
2. Connect Input_PER to an analog input in the basic settings.
3. Click on the "Automatic setting" button in the process value settings.

   The existing values will be overwritten with the values from the hardware configuration.

##### Monitoring process value

Specify the absolute high and low limit of the process value. You must enter reasonable limits for your controlled system. Reasonable limits are important during optimization to obtain optimal PID parameters. The default for the "High limit process value" is 120 %. At the I/O input, the process value can be a maximum of 18% higher than the standard range (overrange). This setting ensures that an error is no longer signaled due to a violation of the "Process value high limit". Only a wire-break and a short-circuit are recognized and PID_3Step reacts according to the configured reaction to error.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Your system may be damaged.**  If you set very high process value limits (for example -3.4*10<sup>38</sup>...+3.4*10<sup>38</sup>), process value monitoring will be disabled. Your system may then be damaged if an error occurs. You need to configure useful process value limits for your controlled system. |  |

#### Actuator settings V1 (S7-1200, S7-1500)

##### Actuator-specific times

Configure the motor transition time and the minimum ON and OFF times to prevent damage to the actuator. You can find the specifications in the actuator data sheet.

The motor transition time is the time in seconds the motor requires to move the actuator from the closed to the opened state. The maximum time that the actuator is moved in one direction is 110% of the motor transition time. You can measure the motor transition time during commissioning.

The motor transition time is taken into consideration in the calculation of the analog output value as well as in the calculation of the digital output values. It is mainly required for correct operation during auto-tuning and the anti-windup behavior.

If no relevant motor transition time is in effect in your process (e.g. with solenoid valves), so that the output value has a direct and full effect on the process, use PID_Compact instead.

If you are using "Output_UP" or "Output_DN", you can reduce the switching frequency with the minimum on and minimum OFF time.

The on or off times calculated are totaled in automatic mode and only become effective when the sum is greater than or equal to the minimum on or OFF time.

A rising edge at Manual_UP or Manual_DN in manual mode will operate the actuator for at least the minimum on or OFF time.

If you have selected the analog output value Output_PER, the minimum ON time and the minimum OFF time are not evaluated and cannot be changed.

##### Reaction to error

PID_3Step is preset so that the controller stays active in most cases in the event of an error. If errors occur frequently in controller mode, this default reaction has a negative effect on the control response. In this case, check the Errorbits parameter and eliminate the cause of the error.

PID_3Step generates a programmable output value in response to an error:

- Current value

  PID_3Step is switched off and no longer modifies the actuator position.
- Current value for error while error is pending

  The controller functions of PID_3Step are switched off and the position of the actuator is no longer changed.

  If the following errors occur in automatic mode, PID_3Step returns to automatic mode as soon as the errors are no longer pending.

  - 0002h: Invalid value at Input_PER parameter.
  - 0200h: Invalid value at Input parameter.
  - 0800h: Sampling time error
  - 1000h: Invalid value at Setpoint parameter.
  - 2000h: Invalid value at Feedback_PER parameter.
  - 4000h: Invalid value at Feedback parameter.
  - 8000h: Error during digital position feedback.

  If one of these error occurs in manual mode, PID_3Step remains in manual mode.

  If an error occurs during the tuning or transition time measurement, PID_3Step is switched off.
- Substitute output value

  PID_3Step moves the actuator to the substitute output value and then switches off.
- Substitute output value while error is pending

  PID_3Step moves the actuator to the substitute output value. When the substitute output value is reached, PID_3Step reacts as it does with "Current value for while error is pending".

Enter the substitute output value in "%".

Only substitute output values 0% and 100% can be configured when using Output_UP and Output_DN without analog position feedback (Config.OutputPerOn = FALSE and Config.FeedbackOn = FALSE). The actuator is moved in one direction at 110% of the motor transition time to ensure the high or low endstop is reached. There endstop signals take priority.

Any substitute output values within the output value limits can be configured when using Output_PER or analog position feedback (Config.OutputPerOn = TRUE or Config.FeedbackOn = TRUE).

##### Feedback scaling

If you have configured the use of Feedback_PER in the basic settings, you will need to convert the value of the analog input into %. The current configuration will be displayed in the "Feedback" display.

Feedback_PER is scaled using a low and high value pair.

1. Enter the low pair of values in the "Low endstop" and "Low" input boxes.
2. Enter the high pair of values in the "High endstop" and "High" input boxes.

"Low endstop" must be less than "High endstop"; "Low" must be less than "High".

The valid values for "High endstop" and "Low endstop" depend upon:

- No Feedback, Feedback, Feedback_PER
- Output (analog), Output (digital)

| Output | Feedback | Low endstop | High endstop |
| --- | --- | --- | --- |
| Output (digital) | No Feedback | Cannot be set (0.0%) | Cannot be set (100.0%) |
| Output (digital) | Feedback | -100.0% or 0.0% | 0.0% or +100.0% |
| Output (digital) | Feedback_PER | -100.0% or 0.0% | 0.0% or +100.0% |
| Output (analog) | No Feedback | Cannot be set (0.0%) | Cannot be set (100.0%) |
| Output (analog) | Feedback | -100.0% or 0.0% | 0.0% or +100.0% |
| Output (analog) | Feedback_PER | -100.0% or 0.0% | 0.0% or +100.0% |

##### Limiting the output value

You can only exceed or undershoot the output value limits during the transition time measurement. The output value is limited to these values in all other modes.

Enter the absolute output value limits in the "Output value high limit" and "Output value low limit" input boxes. The output value limits must be within "Low endstop" and "High endstop".

If no Feedback is available and Output (digital) is set, you cannot limit the output value. The digital outputs are reset with Actuator_H = TRUE or Actuator_L = TRUE, or after a travel time amounting to 110% of the motor transition time.

#### Advanced settings V1 (S7-1200, S7-1500)

This section contains information on the following topics:

- [Process value monitoring V1 (S7-1200, S7-1500)](#process-value-monitoring-v1-s7-1200-s7-1500)
- [PID parameters V1 (S7-1200, S7-1500)](#pid-parameters-v1-s7-1200-s7-1500)

##### Process value monitoring V1 (S7-1200, S7-1500)

Configure a warning high and low limit for the process value in the "Process value monitoring" configuration window. If one of the warning limits is exceeded or undershot during operation, a warning will be displayed at the PID_3Step instruction:

- At the InputWarning_H output parameter if the warning high limit has been exceeded
- At the InputWarning_L output parameter if the warning low limit has been undershot

The warning limits must be within the process value high and low limits.

The process value high and low limits will be used if you do not enter values.

###### Example

Process value high limit = 98° C; warning high limit = 90° C

Warning low limit = 10° C; process value low limit = 0° C

PID_3Step will respond as follows:

| Process value | InputWarning_H | InputWarning_L | Operating mode |
| --- | --- | --- | --- |
| > 98° C | TRUE | FALSE | Inactive |
| ≤ 98° C and > 90° C | TRUE | FALSE | Automatic mode |
| ≤ 90° C and ≥ 10° C | FALSE | FALSE | Automatic mode |
| < 10° C and ≥ 0° C | FALSE | TRUE | Automatic mode |
| < 0° C | FALSE | TRUE | Inactive |

##### PID parameters V1 (S7-1200, S7-1500)

The PID parameters are displayed in the "PID Parameters" configuration window. The PID parameters will be adapted to your controlled system during controller tuning. You do not need to enter the PID parameters manually.

> **Note**
>
> The currently active PID parameters are located in the Retain.CtrlParams structure.
>
> Change the currently active PID parameters only in "Inactive" mode online to prevent malfunction of the PID controller.
>
> If you want to change the PID parameters in "Automatic mode" or "Manual mode" online, change the PID parameters in the CtrlParamsBackUp structure and apply these changes to the Retain.CtrlParams structure as follows:
>
> - PID_3Step V1: Apply the changes with Config.LoadBackUp = TRUE
> - PID_3Step V2: Apply the changes with LoadBackUp = TRUE
>
> Online changes to the PID parameters in "Automatic mode" can result in jumps at the output value.

The PID algorithm operates according to the following equation:

![Figure](images/166014278155_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| Δy | Output value of the PID algorithm |
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

![Figure](images/166014272651_DV_resource.Stream@PNG-de-DE.png)

All PID parameters are retentive. If you enter the PID parameters manually, you must completely download PID_3Step.

[Downloading technology objects to device](Configuring%20a%20software%20controller.md#downloading-technology-objects-to-device)

###### Proportional gain

The value specifies the proportional gain of the controller. PID_3Step does not work with a negative proportional gain. Control logic is inverted under Basic settings > Controller type.

###### Integration time

The integration time determines the time behavior of the integral action. The integral action is deactivated with integration time = 0.0. When the integration time is changed from a different value to 0.0 online in "Automatic mode", the previous integral action is deleted and the output value jumps.

###### Derivative action time

The derivative action time determines the time behavior of the derivative action. Derivative action is deactivated with derivative action time = 0.0.

###### Derivative delay coefficient

The derivative delay coefficient delays the effect of the derivative action.

Derivative delay = derivative action time × derivative delay coefficient

- 0.0: Derivative action is effective for one cycle only and therefore almost not effective.
- 0.5: This value has proved useful in practice for controlled systems with **one** dominant time constant.
- > 1.0: The greater the coefficient, the longer the effect of the derivative action is delayed.

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

The controlled system needs a certain amount of time to respond to changes in the output value. It is therefore not advisable to calculate the output value in every cycle. The sampling time of the PID algorithm represents the time between two calculations of the output value. It is calculated during tuning and rounded to a multiple of the PID_3Step sampling time. All other functions of PID_3Step are executed at every call.

###### Dead zone width

The dead zone suppresses the noise component in the steady controller state. The dead zone width specifies the size of the dead zone. The dead zone is off if the dead zone width is 0.0.

If values not equal to 1.0 are configured for the proportional action weighting or the derivative action weighting, setpoint changes even within the dead zone affect the output value.  
Process value changes within the dead zone do not affect the output value, regardless of the weighting.

---

**See also**

[Selection of the controller structure for specified controlled systems](PID%20control.md#selection-of-the-controller-structure-for-specified-controlled-systems)

### Commissioning PID_3Step V1 (S7-1200, S7-1500)

This section contains information on the following topics:

- [Commissioning V1 (S7-1200, S7-1500)](#commissioning-v1-s7-1200-s7-1500)
- [Pretuning V1 (S7-1200, S7-1500)](#pretuning-v1-s7-1200-s7-1500)
- [Fine tuning V1 (S7-1200, S7-1500)](#fine-tuning-v1-s7-1200-s7-1500)
- [Commissioning with manual PID parameters V1 (S7-1200, S7-1500)](#commissioning-with-manual-pid-parameters-v1-s7-1200-s7-1500)
- [Measuring the motor transition time V1 (S7-1200, S7-1500)](#measuring-the-motor-transition-time-v1-s7-1200-s7-1500)

#### Commissioning V1 (S7-1200, S7-1500)

You can monitor the setpoint, process value and output value over time in the "Tuning" working area. The following commissioning functions are supported in the curve plotter:

- Controller pretuning
- Controller fine tuning
- Monitoring the current closed-loop control in the trend view

All functions require an online connection to the CPU to have been established.

##### Basic handling

- Select the desired sampling time in the "Sampling time" drop-down list.

  All values in the tuning working area are updated in the selected update time.
- Click the "Start" icon in the measuring group if you want to use the commissioning functions.

  Value recording is started. The current values for the setpoint, process value and output value are entered in the trend view. Operation of the commissioning window is enabled.
- Click the "Stop" icon if you want to end the commissioning functions.

  The values recorded in the trend view can continue to be analyzed.
- Closing the commissioning window will terminate recording in the trend view and delete the recorded values.

#### Pretuning V1 (S7-1200, S7-1500)

The pretuning determines the process response to a pulse of the output value and searches for the point of inflection. The tuned PID parameters are calculated as a function of the maximum slope and dead time of the controlled system.

The more stable the process value is, the easier it is to calculate the PID parameters and the more precise the result will be. Noise on the process value can be tolerated as long as the rate of rise of the process value is significantly higher compared to the noise. The PID parameters are backed up before being recalculated.

The setpoint is frozen during pretuning.

##### Requirement

- The PID_3Step instruction is called in a cyclic interrupt OB.
- ManualEnable = FALSE
- PID_3Step is in "inactive" or "manual" mode.
- The setpoint and the process value lie within the configured limits (see "Process value settings" configuration).

##### Procedure

To perform pretuning, follow these steps:

1. Double-click the "PID_3Step > Commissioning" entry in the project tree.
2. Select the entry "Pretuning" in the "Tuning mode" drop-down list in the working area "Tuning".
3. Click the "Start" icon.

   - An online connection will be established.
   - Value recording is started.
   - Pretuning is started.
   - The "Status" field displays the current steps and any errors that may have occurred. The progress bar indicates the progress of the current step.

**Note**

Click the "Stop" icon when the progress bar has reached 100% and it is to be assumed the controller tuning function is blocked. Check the configuration of the technology object and, if necessary, restart controller tuning.

##### Result

If pretuning was performed without an error message, the PID parameters have been tuned. PID_3Step switches to automatic mode and uses the tuned parameters. The tuned PID parameters will be retained during power OFF and a restart of the CPU.

If pretuning is not possible, PID_3Step changes to "Inactive" mode.

#### Fine tuning V1 (S7-1200, S7-1500)

Fine tuning generates a constant, limited oscillation of the process value. The PID parameters are optimized for the operating point from the amplitude and frequency of this oscillation. All PID parameters are recalculated on the basis of the findings. PID parameters from fine tuning usually have better master control and disturbance behavior than PID parameters from pretuning.

PID_3Step automatically attempts to generate an oscillation greater than the noise of the process value. Fine tuning is only minimally influenced by the stability of the process value. The PID parameters are backed up before being recalculated.

The setpoint is frozen during fine tuning.

##### Requirement

- The PID_3Step instruction is called in a cyclic interrupt OB.
- ManualEnable = FALSE
- The motor transition time has been configured or measured.
- The setpoint and the process value lie within the configured limits (see "Process value settings" configuration).
- The control loop has stabilized at the operating point. The operating point is reached when the process value corresponds to the setpoint.
- No disturbances are expected.
- PID_3Step is in inactive mode, automatic mode or manual mode.

##### Process depends on initial situation

Fine tuning proceeds as follows when started in:

- Automatic mode

  Start fine tuning in automatic mode if you wish to improve the existing PID parameters using controller tuning.

  PID_3Step will regulate using the existing PID parameters until the control loop has stabilized and the requirements for fine tuning have been met. Only then will fine tuning start.
- Inactive or manual mode

  Pretuning is always started first. The PID parameters established will be used for adjustment until the control loop has stabilized and the requirements for fine tuning have been met. Only then will fine tuning start.

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

The PID parameters will have been optimized if fine tuning has been executed without errors. PID_3Step changes to automatic mode and uses the optimized parameters. The optimized PID parameters will be retained during power OFF and a restart of the CPU.

If errors occurred during fine tuning, PID_3Step will change to "inactive" mode.

#### Commissioning with manual PID parameters V1 (S7-1200, S7-1500)

##### Procedure

Proceed as follows to commission PID_3Step with manual PID parameters:

1. Double-click on "PID_3Step > Configuration" in the project tree.
2. Click on "Advanced settings > PID Parameters" in the configuration window.
3. Select the check box "Enable direct input".
4. Enter the PID parameters.
5. Double-click on "PID_3Step > Commissioning" in the project tree.
6. Establish an online connection to the CPU.
7. Load the PID parameters to the CPU.
8. Click on the "Activate controller" icon.

##### Result

PID_3Step changes to automatic mode and controls using the current PID parameters.

#### Measuring the motor transition time V1 (S7-1200, S7-1500)

##### Introduction

PID_3Step requires the motor transition time to be as accurate as possible for good controller results. The data in the actuator documentation contains average values for this type of actuator. The value for the specific actuator used may differ.

You can measure the motor transition time during commissioning if you are using actuators with position feedback or endstop signals. The output value limits are not taken into consideration during the motor transition time measurement. The actuator can travel to the high or the low endstop.

The motor transition time cannot be measured if neither position feedback nor endstop signals are available.

##### Actuators with analog position feedback

Proceed as follows to measure motor transition time with position feedback:

**Requirement**

- Feedback or Feedback_PER has been selected in the basic settings and the signal has been connected.
- An online connection to the CPU has been established.

1. Select the "Use position feedback" check box.
2. Enter the position to which the actuator is to be moved in the "Target position" input field.

   The current position feedback (starting position) will be displayed. The difference between "Target position" and "Position feedback" must be at least 50% of the valid output value range.
3. Click the ![Actuators with analog position feedback](images/166014283659_DV_resource.Stream@PNG-de-DE.png) "Start transition time measurement" icon.

##### Result

The actuator is moved from the starting position to the target position. Time measurement starts immediately and ends when the actuator reaches the target position. The motor transition time is calculated according to the following equation:

Motor transition time = (output value high limit – output value low limit) × Measuring time / AMOUNT (target position – starting position).

The progress and status of transition time measurement are displayed. The transition time measured is saved in the instance data block on the CPU and displayed in the "Measured transition time" field. PID_3Step will change to "Inactive" mode once transition time measurement is complete.

> **Note**
>
> Click on the icon ![Result](images/166014016267_DV_resource.Stream@PNG-de-DE.png) "Upload measured transition time" to load the motor transition time measured to the project.

##### Actuators with endstop signals

Proceed as follows to measure the transition time of actuators with endstop signals:

**Requirement**

- The "Endstop signals" check box in the basic settings has been selected and Actuator_H and Actuator_L are connected.
- An online connection to the CPU has been established.

Proceed as follows to measure motor transition time with endstop signals:

1. Select the "Use actuator endstop signals" check box.
2. Select the direction in which the actuator is to be moved.

   - Open - Close - Open

     The actuator is moved first to the high endstop, then to the low endstop and then back to the high endstop.
   - Close - Open - Close

     The actuator is moved first to the low endstop, then to the high endstop and then back to the low endstop.
3. Click the ![Actuators with endstop signals](images/166014283659_DV_resource.Stream@PNG-de-DE.png) "Start transition time measurement" icon.

##### Result

The actuator is moved in the selected direction. Time measurement will start once the actuator has reached the first endstop and will end when the actuator reaches this endstop for the second time. The motor transition time is equal to the time measured divided by two.

The progress and status of transition time measurement are displayed. The transition time measured is saved in the instance data block on the CPU and displayed in the "Measured transition time" field. PID_3Step will change to "Inactive" mode once transition time measurement is complete.

##### Cancelling transition time measurement

PID_3Step will change to "Inactive" mode immediately if you cancel transition time measurement. The actuator will stop being moved. You can reactive PID-3Step in the curve plotter.

### Simulating PID_3Step V1 with PLCSIM (S7-1200, S7-1500)

> **Note**
>
> **Simulation with PLCSIM**
>
> For the simulation with PLCSIM, the time behavior of the simulated PLC is not exactly identical to that of a "real" PLC. The actual cycle clock of a cyclic interrupt OB can have larger fluctuations with a simulated PLC than with "real" PLCs.
>
> In the standard configuration, PID_3Step determines the time between calls automatically and monitors them for fluctuations.
>
> For a simulation of PID_3Step with PLCSIM, for example, a sampling time error (ErrorBits = DW#16#00000800) can therefore be detected.
>
> This results in ongoing tuning being aborted.
>
> The response in automatic mode depends on the value of the ActivateRecoverMode tag.
>
> To prevent this from happening, you should configure PID_3Step for simulation with PLCSIM as follows:
>
> - CycleTime.EnEstimation = FALSE
> - CycleTime.EnMonitoring = FALSE
> - CycleTime.Value: Assign the cycle clock of the calling cyclic interrupt OB in seconds to this tag.

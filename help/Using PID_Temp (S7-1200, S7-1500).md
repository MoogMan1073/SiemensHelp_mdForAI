---
title: "Using PID_Temp (S7-1200, S7-1500)"
package: TFTOPIDTempenUS
topics: 37
devices: [S7-1200, S7-1500, S7-1500T]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Using PID_Temp (S7-1200, S7-1500)

This section contains information on the following topics:

- [Technology object PID_Temp (S7-1200, S7-1500)](#technology-object-pid_temp-s7-1200-s7-1500)
- [Configuring PID_Temp (S7-1200, S7-1500)](#configuring-pid_temp-s7-1200-s7-1500)
- [Commissioning PID_Temp (S7-1200, S7-1500)](#commissioning-pid_temp-s7-1200-s7-1500)
- [Cascade control with PID_Temp (S7-1200, S7-1500)](#cascade-control-with-pid_temp-s7-1200-s7-1500)
- [Multi-zone controlling with PID_Temp (S7-1200, S7-1500)](#multi-zone-controlling-with-pid_temp-s7-1200-s7-1500)
- [Override control with PID_Temp (S7-1200, S7-1500)](#override-control-with-pid_temp-s7-1200-s7-1500)
- [Simulating PID_Temp with PLCSIM (S7-1200, S7-1500)](#simulating-pid_temp-with-plcsim-s7-1200-s7-1500)

## Technology object PID_Temp (S7-1200, S7-1500)

The PID_Temp technology object provides a continuous PID controller with integrated tuning. PID_Temp is especially designed for temperature control and is suited for heating or heating/cooling applications. Two outputs are available for this purpose, one each for heating and cooling. PID_Temp can also be used for other control tasks. PID_Temp is cascadable and can be used in manual or automatic mode.

PID_Temp continuously acquires the measured process value within a control loop and compares it with the set setpoint. From the resulting control deviations, the instruction PID_Temp calculates the output value for heating and/or cooling which is used to adjust the process value to the setpoint. The output values for the PID controller consist of three actions:

- Proportional action

  The proportional action of the output value increases in proportion to the control deviation.
- Integral action

  The integral action of the output value increases until the control deviation has been balanced.
- Derivative action

  The derivative action increases with the rate of change of control deviation. The process value is corrected to the setpoint as quickly as possible. The derivative action will be reduced again if the rate of change of control deviation drops.

The instruction PID_Temp calculates the proportional, integral and derivative parameters for your controlled system during "pretuning". "Fine tuning" can be used to tune the parameters further. You do not need to manually determine the parameters.

Either a fixed cooling factor or two PID parameter sets can be used for heating-and-cooling applications.

### Additional information

- [Overview of software controller](Configuring%20a%20software%20controller.md#overview-of-software-controller)
- [Add technology objects](Configuring%20a%20software%20controller.md#add-technology-objects)
- [Configure technology objects](Configuring%20a%20software%20controller.md#configure-technology-objects)
- [Configuring PID_Temp](#configuring-pid_temp-s7-1200-s7-1500)

## Configuring PID_Temp (S7-1200, S7-1500)

This section contains information on the following topics:

- [Basic settings (S7-1200, S7-1500)](#basic-settings-s7-1200-s7-1500)
- [Process value settings (S7-1200, S7-1500)](#process-value-settings-s7-1200-s7-1500)
- [Output settings (S7-1200, S7-1500)](#output-settings-s7-1200-s7-1500)
- [Advanced settings (S7-1200, S7-1500)](#advanced-settings-s7-1200-s7-1500)

### Basic settings (S7-1200, S7-1500)

This section contains information on the following topics:

- [Introduction (S7-1200, S7-1500)](#introduction-s7-1200-s7-1500)
- [Controller type (S7-1200, S7-1500)](#controller-type-s7-1200-s7-1500)
- [Setpoint (S7-1200, S7-1500)](#setpoint-s7-1200-s7-1500)
- [Process value (S7-1200, S7-1500)](#process-value-s7-1200-s7-1500)
- [Heating and cooling output value (S7-1200, S7-1500)](#heating-and-cooling-output-value-s7-1200-s7-1500)
- [Cascade (S7-1200, S7-1500)](#cascade-s7-1200-s7-1500)

#### Introduction (S7-1200, S7-1500)

Configure the following properties of the "PID_Temp" technology object under "Basic settings" in the Inspector window or in the configuration window:

- Physical quantity
- Start-up behavior after reset
- Source and input of the setpoint (only in the Inspector window)
- Selection of the process value
- Source and input of the process value (only in the Inspector window)
- Selection of the heating output value
- Source and input of the heating output value (only in the Inspector window)
- Activation and selection of the cooling output value
- Source and input of the cooling output value (only in the Inspector window)
- Activation of PID_Temp as master or slave of a cascade
- Number of slaves
- Selection of the master (only in the Inspector window)

##### Setpoint, process value, heating output value and cooling output value

You can select the source and enter values or tags for the setpoint, process value, heating output value and cooling output value in the Inspector window of the programming editor.

Select the source for each value:

- Instance DB:

  The value saved in the instance DB is used. The value must be updated by the user program in the instance DB. There should be no value at the instruction. Can be changed using HMI.
- Instruction:

  The value connected to the instruction is used. The value is written to the instance DB each time the instruction is called. Cannot be changed using HMI.

#### Controller type (S7-1200, S7-1500)

##### Physical quantity

Select the unit of measurement and physical quantity for the setpoint and the process value in the "Controller type" group. The setpoint and the process value are displayed in this unit.

##### Startup characteristics

1. To switch to "Inactive"mode after CPU restart, clear the "Activate Mode after CPU restart"check box.

   To switch to the operating mode saved in the Mode parameter after CPU restart, select the "Activate Mode after CPU restart" check box.
2. In the "Set Mode to" drop-down list, select the mode that is to be enabled after a complete download to the device.

   After a complete "Download to device", PID_Temp starts in the selected operating mode. With each additional restart, PID_Temp starts in the mode that was last saved in Mode.

   When selecting pretuning or fine tuning, you also have to set or reset the Heat.EnableTuning and Cool.EnableTuning tags in order to choose between tuning for heating and tuning for cooling.

Example:

You have selected the "Activate Mode after CPU restart" check box and the "Pretuning" entry in the "Set Mode to" list. After a complete "Download to device", PID_Temp starts in the "Pretuning" mode. If pretuning is still active, PID_Temp starts in "Pretuning" mode again after restart of the CPU (heating/cooling depends on the tags Heat.EnableTuning and Cool.EnableCooling). If pretuning was successfully completed and automatic mode is active, PID_Temp starts in "Automatic mode" after restart of the CPU.

#### Setpoint (S7-1200, S7-1500)

##### Procedure

Proceed as follows to define a fixed setpoint:

1. Select "Instance DB".
2. Enter a setpoint, e.g. 80° C.
3. Delete any entry in the instruction.

Proceed as follows to define a variable setpoint:

1. Select "Instruction".
2. Enter the name of the REAL tag in which the setpoint is saved.

   Program-controlled assignment of various values to the REAL tag is possible, for example for the time-controlled change of the setpoint.

#### Process value (S7-1200, S7-1500)

PID_Temp will scale the value of the analog input to the physical quantity if you use the analog input value directly.

You will need to write a program for processing if you wish first to process the analog input value. The process value is, for example, not directly proportional to the value at the analog input. The processed process value must be in floating point format.

##### Procedure

Proceed as follows to use the analog input value without processing:

1. Select the entry "Input_PER" in the drop-down list "Input".
2. Select "Instruction" as source.
3. Enter the address of the analog input.

Proceed as follows to use the processed process value in floating point format:

1. Select the entry "Input" in the drop-down list "Input".
2. Select "Instruction" as source.
3. Enter the name of the variable in which the processed process value is saved.

#### Heating and cooling output value (S7-1200, S7-1500)

The PID_Temp instruction provides a PID controller with integrated tuning for temperature processes. PID_Temp is suitable for heating or heating-and-cooling applications.

PID_Temp provides the following output values. Your actuator will determine which output value you use.

- OutputHeat

  Heating output value (floating-point format): The output value for heating needs to be processed by the user program, for example, because of non-linear actuator response.
- OutputHeat_PER

  Analog heating output value: The actuator for heating is triggered via an analog output and controlled with a continuous signal, e.g. 0...10 V, 4...20 mA.
- OutputHeat_PWM

  Pulse-width modulated heating output value: The actuator for heating is controlled via a digital output. Pulse width modulation creates variable ON and OFF times.
- OutputCool

  Cooling output value (floating-point format): The output value for cooling needs to be processed by the user program, for example because of non-linear actuator response.
- OutputCool_PER

  Analog cooling output value: The actuator for cooling is triggered via an analog output and controlled with a continuous signal, e.g. 0...10 V, 4...20 mA.
- OutputCool_PWM

  Pulse-width modulated cooling output value: The actuator for cooling is controlled via a digital output. Pulse width modulation creates variable ON and OFF times.

The cooling output is only available if it was activated via the "Activate cooling" check box.

- If the check box is cleared, the output value of the PID algorithm (PidOutputSum) is scaled and output at the outputs for heating.
- If the check box is selected, positive output values of the PID algorithm (PidOutputSum) are scaled and output at the outputs for heating. Negative output values of the PID algorithm are scaled and output at the outputs for cooling. You can choose between two methods for output value calculation at the output settings.

> **Note**
>
> **Note:**
>
> - The OutputHeat_PWM, OutputHeat_PER, OutputCool_PWM, OutputCool_PER outputs are only calculated if you select these correspondingly from the drop-down list.
> - The OutputHeat output is always calculated.
> - The OutputCool output is calculated if the check box for cooling is selected.
> - The "Activate cooling" check box is only available if the controller is not configured as a master in a cascade.

##### Procedure

Proceed as follows to use the analog output value:

1. Select the entry "OutputHeat_PER" or "OutputCool_PER" in the drop-down list "OutputHeat" or "OutputCool".
2. Select "Instruction".
3. Enter the address of the analog output.

Proceed as follows to use the pulse-width modulated output value:

1. Select the entry "OutputHeat_PWM" or "OutputCool_PWM" in the drop-down list "OutputHeat" or "OutputCool".
2. Select "Instruction".
3. Enter the address of the digital output.

Proceed as follows to process the output value using the user program:

1. Select the entry "OutputHeat" or "OutputCool" in the drop-down list "OutputHeat" or "OutpuCool".
2. Select "Instruction".
3. Enter the name of the variable you are using to process the output value.
4. Transfer the processed output value to the actuator by means of an analog or digital CPU output.

#### Cascade (S7-1200, S7-1500)

If a PID_Temp instance receives its setpoint from a higher-level master controller and outputs its output value in turn to a subordinate slave controller, this PID_Temp instance is both a master controller and a slave controller simultaneously. Both configurations listed below then have to be carried out for such a PID_Temp instance. This is the case, for example, for the middle PID_Temp instance in a cascade control system with three concatenated measured variables and three PID_Temp instances.

##### Configuring a controller as master in a cascade

A master controller defines the setpoint of a slave controller with its output.

In order to use PID_Temp as master in a cascade, you have to deactivate the cooling in the basic settings. In order to configure this PID_Temp instance as a master controller in a cascade, activate the "Controller is master" check box. The selection of the output value for heating is set automatically to OutputHeat.

OutputHeat_PWM and OutputHeat_PER cannot be used at a master in a cascade.

Subsequently specify the number of directly subordinate slave controllers that receive their setpoint from this master controller.

If no own scaling function is used when assigning the OutputHeat parameter of the master to the Setpoint parameter of the slave, it may be necessary to adapt the output value limits and the output scaling of the master to the setpoint/process value range of the slave. This can be done in the output settings of the master in the "OutputHeat / OutputCool" section.

##### Configuring a controller as a slave in a cascade

A slave controller receives its setpoint (Setpoint parameter) from the output of its master controller (OutputHeat parameter).

In order to configure this PID_Temp instance as a slave controller in a cascade, activate the "Controller is slave" check box in the basic settings.

Subsequently select the PID_Temp instance that is to be used as the master controller for this slave controller in the Inspector window of the programming editor. The Master and Setpoint parameters of the slave controller are interconnected with the selected master controller through this selection (the existing interconnections at these parameters are overwritten). This interconnection allows the exchange of information and the setpoint specification between master and slave. If required, the interconnection can be changed subsequently at the Setpoint parameter of the slave controller in order, for example, to insert an additional filter. The interconnection at the parameter Master may not be changed subsequently.

The "Controller is master" check box has to be selected and the number of slaves has to be configured correctly at the selected master controller. The master controller has to be called before the slave controller in the same cyclic interrupt OB.

##### Additional information

Additional information about program creation, configuration and commissioning when PID_Temp is used in cascade control systems is available under [Cascade control with PID_Temp](#cascade-control-with-pid_temp-s7-1200-s7-1500).

### Process value settings (S7-1200, S7-1500)

This section contains information on the following topics:

- [Process value limits (S7-1200, S7-1500)](#process-value-limits-s7-1200-s7-1500)
- [Process value scaling (S7-1200, S7-1500)](#process-value-scaling-s7-1200-s7-1500)

#### Process value limits (S7-1200, S7-1500)

You must specify an appropriate absolute high limit and low limit for the process value as limit values for your controlled system. As soon as the process value violates these limits, an error occurs (ErrorBits = 0001h). Tuning is canceled when the process value limits are violated. You can specify how PID_Temp responds to errors in automatic mode in the output settings.

#### Process value scaling (S7-1200, S7-1500)

If you have configured the use of Input_PER in the basic settings, you will need to convert the value of the analog input into the physical quantity of the process value. The current configuration is displayed in the Input_PER display.

Input_PER is scaled using a low and high value pair if the process value is directly proportional to the value of the analog input.

##### Procedure

To scale the process value, follow these steps:

1. Enter the low pair of values in the "Scaled low process value" and "Low" input fields.
2. Enter the high pair of values in the "Scaled high process value" and "High" input fields.

Default settings for the value pairs are saved in the hardware configuration. Proceed as follows to use the value pairs from the hardware configuration:

1. Select the instruction PID_Temp in the programming editor.
2. Interconnect Input_PER with an analog input in the basic settings.
3. Click on the "Automatic setting" button in the process value settings.

The existing values are overwritten with the values from the hardware configuration.

### Output settings (S7-1200, S7-1500)

This section contains information on the following topics:

- [Basic settings of output (S7-1200, S7-1500)](#basic-settings-of-output-s7-1200-s7-1500)
- [Output value limits and scaling (S7-1200, S7-1500)](#output-value-limits-and-scaling-s7-1200-s7-1500)

#### Basic settings of output (S7-1200, S7-1500)

##### Method for heating and cooling

If cooling is activated in the basic settings, two methods are available for calculating the PID output value:

- PID parameter switching (Config.AdvancedCooling = TRUE):

  The output value calculation for cooling takes place by means of a separate PID parameter set. Based on the calculated output value and the control deviation, the PID algorithm decides whether the PID parameter for heating or cooling is used. This method is suitable if the heating and cooling actuators have different time responses and different gains.

  Pretuning and fine tuning for cooling are only available if this method is selected.
- Cooling factor (Config.AdvancedCooling = FALSE):

  Output value calculation for cooling is effected with the PID parameters for heating under consideration of the configurable cooling factor Config.CoolFactor. This method is suitable if the heating and cooling actuators have a similar time response but different gains. If this method is selected, pretuning and fine tuning for cooling as well as the PID parameter set for cooling are not available. You can only execute the tuning for heating.

##### Cooling factor

If the cooling factor is selected as the method for heating/cooling, this factor is used in the calculation of the output value for cooling. This allows different gains of heating and cooling actuators to be taken into account.

The cooling factor is not set automatically or adjusted during tuning. You have to configure the correct cooling factor manually by using the ratio "Heating actuator gain/Cooling actuator gain".

Example: Cooling factor = 2.0 means that the heating actuator gain is twice as high as the cooling actuator gain.

The cooling factor is only effective and can only be changed if "Cooling factor" is selected as the method for heating/cooling.

##### Reaction to error

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Your system may be damaged.**  If you output "Current value while error is pending " or "Substitute output value while error is pending" in the event of an error, PID_Temp remains in automatic mode or in manual mode. This may cause a violation of the process value limits and damage your system.   It is essential to configure how your controlled system reacts in the event of an error to protect your system from damage. |  |

PID_Temp is preset so that the controller stays active in most cases in the event of an error.

If errors occur frequently in controller mode, this default reaction has a negative effect on the control response. In this case, check the ErrorBits parameter and eliminate the cause of the error.

PID_Temp generates a programmable output value in response to an error:

- Zero (inactive)

  At all errors, PID_Temp switches to the "Inactive" operating mode and outputs the following:

  - 0.0 as PID output value (PidOutputSum)
  - 0.0 as output value for heating (OutputHeat) and output value for cooling (OutputCool)
  - 0 as analog output value for heating (OutputHeat_PER) and analog output value for cooling (OutputCool_PER)
  - FALSE as PWM output value for heating (OutputHeat_PWM) and PWM output value for cooling (OutputCool_PWM)

  This is independent of the configured output value limits and the scaling. The controller is only reactivated by a falling edge at Reset or a rising edge at ModeActivate.
- Current value while error is pending

  The error response depends on the error occurring and the operating mode.

  If one or more of the following errors occur in automatic mode, PID_Temp stays in automatic mode:

  - 0000001h: The Input parameter is outside the process value limits.
  - 0000800h: Sampling time error
  - 0040000h: Invalid value at Disturbance parameter.
  - 8000000h: Error during the calculation of the PID parameters.

  If one or more of the following errors occur in automatic mode, PID_Temp switches to "Substitute output value with error monitoring" mode and outputs the last valid PID output value (PidOutputSum):

  - 0000002h: Invalid value at Input_PER parameter.
  - 0000200h: Invalid value at Input parameter.
  - 0000400h: Calculation of output value failed.
  - 0001000h: Invalid value at Setpoint or SubstituteSetpoint parameter.

  The values at the outputs for heating and cooling resulting from the PID output value are produced by the configured output scaling.

  As soon as the errors are no longer pending, PID_Temp switches back to automatic mode.

  If an error occurs during manual mode, PID_Temp remains in manual mode and continues to use the manual value as the PID output value.

  If the manual value is invalid, the configured substitute output value is used.

  If the manual value and substitute output value are invalid, the low limit of the PID output value for heating (Config.Output.Heat.PidLowerLimit) is used.

  If the following error occurs during pretuning or fine tuning, PID_Temp remains in active mode:

  - 0000020h: Pretuning is not permitted during fine tuning.

  When any other error occurs, PID_Temp cancels the tuning and switches to the mode from which tuning was started.
- Substitute output value while error is pending

  PID_Temp behaves as described at "Current value while error is pending", but outputs the configured substitute output value (SubstituteOutput) as a PID output value (PidOutputSum) in "Substitute output value with error monitoring" operating mode.

  The values at the outputs for heating and cooling resulting from the PID output value are produced by the configured output scaling.

  In the case of controllers with activated cooling output (Config.ActivateCooling = TRUE), enter:

  - A positive substitute output value to output the value at the outputs for heating.
  - A negative substitute output value to output the value at the outputs for cooling.

  If the following error occurs, PID_Temp stays in "Substitute output value with error monitoring" mode and outputs the low limit of the PID output value for heating (Config.Output.Heat.PidLowerLimit):

  - 0020000h: Invalid value at SubstituteOutput tag.

#### Output value limits and scaling (S7-1200, S7-1500)

Depending on the operating mode, the PID output value (PidOutputSum) is calculated automatically by the PID algorithm or by the manual value (ManualValue) or the configured substitute output value (SubstituteOutput).

The PID output value is limited depending on the configuration:

- If the cooling is deactivated in the basic settings (Config.ActivateCooling = FALSE), the value is limited to the high limit of the PID output value (heating) (Config.Output.Heat.PidUpperLimit) and the low limit of the PID output value (heating) (Config.Output.Heat.PidLowerLimit).

  You can configure both limits at the horizontal axis of the scaling characteristic line in the "OutputHeat / OutputCool" section. These are displayed in the "OutputHeat_PWM / OutputCool_PWM" and "OutputHeat_PER / OutputCool_PER" sections, but cannot be changed.
- If the cooling is activated in the basic settings (Config.ActivateCooling = TRUE), the value is limited to the high limit of the PID output value (Config.Output.Heat.PidUpperLimit) and the low limit of the PID output value (cooling) (Config.Output.Cool.PidLowerLimit).

  You can configure both limits at the horizontal axis of the scaling characteristic line in the "OutputHeat / OutputCool" section. These are displayed in the "OutputHeat_PWM / OutputCool_PWM" and "OutputHeat_PER / OutputCool_PER" sections, but cannot be changed.

  The low limit of the PID output value (heating) (Config.Output.Heat.PidLowerLimit) and the high limit of the PID output value (cooling) (Config.Output.Cool.PidUpperLimit) cannot be changed and have to be assigned the value 0.0.

The PID output value is scaled and output at the outputs for heating and cooling. Scaling can be specified separately for each output and is specified across 2 value pairs each, consisting of a limit value of the PID output value and a scaling value:

| Output | Value pair | Parameter |
| --- | --- | --- |
| OutputHeat | Value pair 1 | PID output value high limit (heating)  Config.Output.Heat.PidUpperLimit,   Scaled high output value (heating) Config.Output.Heat.UpperScaling |
| Value pair 2 | PID output value low limit (heating)   Config.Output.Heat.PidLowerLimit,   Scaled low output value (heating) Config.Output.Heat.LowerScaling |  |
| OutputHeat_PWM | Value pair 1 | PID output value high limit (heating)  Config.Output.Heat.PidUpperLimit,   Scaled high PWM output value (heating)  Config.Output.Heat.PwmUpperScaling |
| Value pair 2 | PID output value low limit (heating)  Config.Output.Heat.PidLowerLimit,   Scaled low PWM output value (heating)  Config.Output.Heat.PwmLowerScaling |  |
| OutputHeat_PER | Value pair 1 | PID output value high limit (heating)  Config.Output.Heat.PidUpperLimit,   Scaled high analog output value (heating)  Config.Output.Heat.PerUpperScaling |
| Value pair 2 | PID output value low limit (heating)  Config.Output.Heat.PidLowerLimit,   Scaled low analog output value (heating)  Config.Output.Heat.PerLowerScaling |  |
| OutputCool | Value pair 1 | PID output value low limit (cooling)  Config.Output.Cool.PidLowerLimit,  Scaled high output value (cooling)  Config.Output.Cool.UpperScaling |
| Value pair 2 | PID output value high limit (cooling)  Config.Output.Cool.PidUpperLimit,  Scaled low output value (cooling)  Config.Output.Cool.LowerScaling |  |
| OutputCool_PWM | Value pair 1 | PID output value low limit (cooling)  Config.Output.Cool.PidLowerLimit,   Scaled high PWM output value (cooling)  Config.Output.Cool.PwmUpperScaling |
| Value pair 2 | PID output value high limit (cooling)  Config.Output.Cool.PidUpperLimit,   Scaled low PWM output value (cooling)  Config.Output.Cool.PwmLowerScaling |  |
| OutputCool_PER | Value pair 1 | PID output value low limit (cooling)  Config.Output.Cool.PidLowerLimit,  Scaled high analog output value (cooling)  Config.Output.Cool.PerUpperScaling |
| Value pair 2 | PID output value high limit (cooling)  Config.Output.Cool.PidUpperLimit,   Scaled low analog output value (cooling)  Config.Output.Cool.PerLowerScaling |  |
| The low limit of PID output value (heating) (Config.Output.Heat.PidLowerLimit) has to have the value 0.0, if the cooling is activated (Config.ActivateCooling = TRUE).  The high limit of PID output value (cooling) (Config.Output.Cool.PidUpperLimit) must always have the value 0.0. |  |  |

**Example:**

Output scaling when the OutputHeat output is used (cooling deactivated. The low limit of PID output value (heating) (Config.Output.Heat.PidLowerLimit) may be unequal to 0.0):

![Figure](images/166014287243_DV_resource.Stream@PNG-de-DE.png)

**Example**:

Output scaling when the OutputHeat_PWM and OutputCool_PER outputs are used (cooling activated. The low limit of PID output value (heating) (Config.Output.Heat.PidLowerLimit) must be 0.0):

![Figure](images/166014305291_DV_resource.Stream@PNG-de-DE.png)

With the exception of the "Inactive" operating mode, the value at an output always lies between its scaled high output value and the scaled low output value, for example for OutputHeat always between the scaled high output value (heating) (Config.Output.Heat.UpperScaling) and the scaled low output value (heating) (Config.Output.Heat.LowerScaling).

If you want to limit the value at the associated output, you therefore have to adapt these scaling values as well.

You can configure the scaling values of an output at the vertical axes of the scaling characteristic line. Each output has two separate scaling values. These can only be changed for OutputHeat_PWM, OutputCool_PWM, OutputHeat_PER and OutputCool_PER if the corresponding output is selected in the basic settings. The cooling has to be activated additionally in the basic settings at all the outputs for cooling.

The trend view in the commissioning dialog box only records the values of OutputHeat and OutputCool, irrespective of the selected output in the basic settings. Therefore, if necessary, adapt the scaling values for OutputHeat or OutputCool if you use OutputHeat_PWM or OutputHeat_PER or OutputCool_PWM or OutputCool_PER and want to use the trend view in the commissioning dialog.

### Advanced settings (S7-1200, S7-1500)

This section contains information on the following topics:

- [Process value monitoring (S7-1200, S7-1500)](#process-value-monitoring-s7-1200-s7-1500)
- [PWM limits (S7-1200, S7-1500)](#pwm-limits-s7-1200-s7-1500)
- [PID parameters (S7-1200, S7-1500)](#pid-parameters-s7-1200-s7-1500)

#### Process value monitoring (S7-1200, S7-1500)

Configure a warning high and low limit for the process value in the "Process value monitoring" configuration window. If one of the warning limits is exceeded or undershot during operation, a warning is displayed at the PID_Temp instruction:

- At the InputWarning_H output parameter if the warning high limit has been exceeded
- At the InputWarning_L output parameter if the warning low limit has been undershot

The warning limits must be within the process value high and low limits.

The process value high and low limits are used if you do not enter values.

##### Example

Process value high limit = 98° C; warning high limit = 90° C

Warning low limit = 10° C; process value low limit = 0° C

PID_Temp will respond as follows:

| Process value | InputWarning_H | InputWarning_L | ErrorBits |
| --- | --- | --- | --- |
| > 98 °C | TRUE | FALSE | 0001h |
| ≤ 98° C and > 90° C | TRUE | FALSE | 0000h |
| ≤ 90° C and ≥ 10° C | FALSE | FALSE | 0000h |
| < 10° C and ≥ 0° C | FALSE | TRUE | 0000h |
| < 0° C | FALSE | TRUE | 0001h |

You can configure the response of PID_Temp when the process value high limit or low limit is violated in the output settings.

#### PWM limits (S7-1200, S7-1500)

The PID output value PidOutputSum is scaled and transformed via a pulse width modulation into a pulse train that is output at the output parameter OutputHeat_PWM or OutputCool_PWM.

The "Sampling time of PID algorithm" represents the time between two calculations of the PID output value. The sampling time is used as time period of the pulse width modulation.

During heating, the PID output value is always calculated in the "Sampling time of PID algorithm for heating".

Calculation of the PID output value during cooling depends on the type of cooling selected in "Basic settings Output":

- If the cooling factor is used, the "Sampling time of PID algorithm for heating" applies.
- If the PID parameter switching is used, the "Sampling time of PID algorithm for cooling" applies.

The PID algorithm sampling time for heating or cooling is determined during pretuning or fine tuning. If you set the PID parameters manually, you will also need to configure the PID algorithm sampling time for heating or cooling.

OutputHeat_PWM and OutputCool_PWM are output in the PID_Temp sampling time. The PID_Temp sampling time is equivalent to the cycle time of the calling OB.

The pulse duration is proportional to the PID output value and is always an integer multiple of the PID_Temp sampling time.

**Example for** 
**OutputHeat_PWM**

![Figure](images/166014315915_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | PID_Temp sampling time |
| ② | PID algorithm sampling time for heating |
| ③ | Pulse duration |
| ④ | Break time |

The "Minimum ON time" and the "Minimum OFF time" can be set separately for heating and cooling, rounded to an integer multiple of the PID_Temp sampling time.

A pulse or a break is never shorter than the minimum ON or OFF time. The inaccuracies this causes are added up and compensated in the next cycle.

**Example for** 
**OutputHeat_PWM**

PID_Temp sampling time (equivalent to the cycle time of the calling OB) = 100 ms

PID algorithm sampling time (equivalent to the time period) = 1000 ms

Minimum ON time = 200 ms

The PID output value PidOutputSum amounts to a constant 15%. The smallest pulse that PID_Temp can output corresponds to 20%. In the first cycle, no pulse is output. In the second cycle, the pulse not output in the first cycle is added to the pulse of the second cycle.

![Figure](images/166014310539_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | PID_Temp sampling time |
| ② | PID algorithm sampling time for heating |
| ⑤ | Minimum ON time |

In order to minimize operation frequency and conserve the actuator, extend the minimum ON and OFF times.

If you have selected OutputHeat/OutputCool or OutputHeat_PER/OutputCool_PER as the output in the basic settings, the minimum ON time and the minimum OFF time are not evaluated and cannot be changed.

If the "Sampling time of PID algorithm" (Retain.CtrlParams.Heat.Cycle or Retain.CtrlParams.Cool.Cycle) and thus the time period of the pulse width modulation is very high when OutputHeat_PWM or OutputCool_PWM is used, you can specify a deviating shorter time period at the parameters Config.Output.Heat.PwmPeriode or Config.Output.Cool.PwmPeriode in order to improve smoothness of the process value (see also [PwmPeriode tag](PID_Temp%20%28S7-1200%2C%20S7-1500%29.md#pwmperiode-tag-s7-1200-s7-1500)).

> **Note**
>
> The minimum ON and OFF times only affect the output parameters OutputHeat_PWM or OutputCool_PWM and are not used for any pulse generators integrated in the CPU.

#### PID parameters (S7-1200, S7-1500)

The PID parameters are displayed in the "PID Parameters" configuration window.

If cooling is activated in the basic settings and PID parameter switching is selected as the method for heating/cooling in the output settings, two parameter sets are available: One for heating and one for cooling.

In this case, the PID algorithm decides on the basis of the calculated output value and the control deviation whether the PID parameters for heating or cooling are used.

If cooling is deactivated or the cooling factor is selected as the method for heating/cooling, the parameter set for heating is always used.

During tuning, the PID parameters are adapted to the controlled system with the exception of the dead zone width that has to be configured manually.

> **Note**
>
> The currently active PID parameters are located in the Retain.CtrlParams structure.
>
> Change the currently active PID parameters only in "Inactive" mode online to prevent malfunction of the PID controller.
>
> If you want to change the PID parameters in "Automatic mode" or "Manual mode" online, change the PID parameters in the CtrlParamsBackUp structure and apply these changes with LoadBackUp = TRUE to the Retain.CtrlParams structure.
>
> Online changes to the PID parameters in "Automatic mode" can result in jumps at the output value.

PID_Temp is a PIDT1 controller with anti-windup and weighting of the proportional and derivative actions.

The PID algorithm operates according to the following equation (control zone and dead zone deactivated):

![Figure](images/166014326539_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Description | Associated parameters of the PID_Temp instruction |
| --- | --- | --- |
| y | Output value of the PID algorithm | - |
| K<sub>p</sub> | Proportional gain | Retain.CtrlParams.Heat.Gain  Retain.CtrlParams.Cool.Gain  CoolFactor |
| s | Laplace operator | - |
| b | Proportional action weighting | Retain.CtrlParams.Heat.PWeighting  Retain.CtrlParams.Cool.PWeighting |
| w | Setpoint | CurrentSetpoint |
| x | Process value | ScaledInput |
| T<sub>I</sub> | Integration time | Retain.CtrlParams.Heat.Ti  Retain.CtrlParams.Cool.Ti |
| T<sub>D</sub> | Derivative action time | Retain.CtrlParams.Heat.Td  Retain.CtrlParams.Cool.Td |
| a | Coefficient for derivative-action delay   (Derivative delay T1 = a × T<sub>D</sub>) | Retain.CtrlParams.Heat.TdFiltRatio  Retain.CtrlParams.Cool.TdFiltRatio |
| c | Derivative action weighting | Retain.CtrlParams.Heat.DWeighting  Retain.CtrlParams.Cool.DWeighting |
| DeadZone | Dead zone width | Retain.CtrlParams.Heat.DeadZone  Retain.CtrlParams.Cool.DeadZone |
| ControlZone | Control zone width | Retain.CtrlParams.Heat.ControlZone  Retain.CtrlParams.Cool.ControlZone |

The diagram below illustrates the integration of the parameters into the PID algorithm:

![Figure](images/166014331915_DV_resource.Stream@PNG-de-DE.png)

All PID parameters are retentive. If you enter the PID parameters manually, you must completely download PID_Temp ([Downloading technology objects to device](Configuring%20a%20software%20controller.md#downloading-technology-objects-to-device)).

##### PID_Temp block diagram

The following block diagram shows how the PID algorithm is integrated in the PID_Temp.

![PID_Temp block diagram](images/166014321163_DV_resource.Stream@PNG-de-DE.png)

##### Proportional gain

The value specifies the proportional gain of the controller. PID_Temp does not operate with a negative proportional gain and only supports the normal control direction, meaning that an increase in the process value is achieved by an increase in the PID output value (PidOutputSum).

##### Integration time

The integration time determines the time behavior of the integral action. The integral action is deactivated with integration time = 0.0. When the integration time is changed from a different value to 0.0 online in "Automatic mode", the previous integral action is deleted and the output value jumps.

##### Derivative action time

The derivative action time determines the time behavior of the derivative action. Derivative action is deactivated with derivative action time = 0.0.

##### Derivative delay coefficient

The derivative delay coefficient delays the effect of the derivative action.

Derivative delay = derivative action time × derivative delay coefficient

- 0.0: Derivative action is effective for one cycle only and therefore almost not effective.
- 0.5: This value has proved useful in practice for controlled systems with one dominant time constant.
- > 1.0: The greater the coefficient, the longer the effect of the derivative action is delayed.

##### Proportional action weighting

The proportional action may weaken with changes to the setpoint.

Values from 0.0 to 1.0 are applicable.

- 1.0: Proportional action for setpoint change is fully effective
- 0.0: Proportional action for setpoint change is not effective

The proportional action is always fully effective when the process value is changed.

##### Derivative action weighting

The derivative action may weaken with changes to the setpoint.

Values from 0.0 to 1.0 are applicable.

- 1.0: Derivative action is fully effective upon setpoint change
- 0.0: Derivative action is not effective upon setpoint change

The derivative action is always fully effective when the process value is changed.

##### PID algorithm sampling time

The controlled system needs a certain amount of time to respond to changes in the output value. It is therefore not advisable to calculate the output value in every cycle. The sampling time of "PID algorithm" represents the time between two calculations of the PID output value. It is calculated during tuning and rounded to a multiple of the PID_Temp sampling time (cycle time of the cyclic interrupt OB). All other functions of PID_Temp are executed at every call.

If you use OutputHeat_PWM or OutputCool_PWM, the sampling time of the PID algorithm is used as the period duration of the pulse width modulation. The accuracy of the output signal is determined by the ratio of the PID algorithm sampling time to the cycle time of the OB. The cycle time should be no more than a tenth of the PID algorithm sampling time.

The sampling time of the PID algorithm that is used as the period duration of the pulse width modulation at OutputCool_PWM depends on the method for heating/cooling selected in "Basic settings Output":

- If the cooling factor is used, the "sampling time of the PID algorithm for heating" also applies to OutputCool_PWM.
- If PID parameter switching is used, the "sampling time PID algorithm for cooling" applies as the period duration for OutputCool_PWM.

If the sampling time of the PID algorithm and thus the period duration of the pulse width modulation is very high when OutputHeat_PWM or OutputCool_PWM is used, you can specify a deviating shorter period duration at the parameters Config.Output.Heat.PwmPeriode or Config.Output.Cool.PwmPeriode in order to improve smoothness of the process value.

##### Dead zone width

If the process value is affected by noise, the noise can also have an effect on the output value. The output value may fluctuate considerably when controller gain is high and the derivative action is activated. If the process value lies within the dead zone around the setpoint, the control deviation is suppressed so that the PID algorithm does not react and unnecessary fluctuations of the output value are reduced.

The dead zone width for heating or cooling is not set automatically during tuning. You have to correctly configure the dead zone width manually. The dead zone is deactivated by setting the dead zone width = 0.0.

When the dead zone is switched on, the result can be a permanent control deviation (deviation between setpoint and process value). This can have a negative effect on fine tuning.

If cooling is activated in the basic settings and PID parameter switching is selected as the method for heating/cooling in the output settings, the dead zone lies between "Setpoint - dead zone width (heating)" and "Setpoint + dead zone width (cooling)".

If cooling is deactivated in the basic settings or the cooling factor is used, the dead zone lies symmetrically between "Setpoint - dead zone width (heating)" and "Setpoint + dead zone width (heating)".

If values not equal to 1.0 are configured for the proportional action weighting or the derivative action weighting, setpoint changes even within the dead zone affect the output value.  
Process value changes within the dead zone do not affect the output value, regardless of the weighting.

| Symbol | Meaning |
| --- | --- |
| ![Dead zone width](images/166014337163_DV_resource.Stream@PNG-de-DE.png) | ![Dead zone width](images/166014360203_DV_resource.Stream@PNG-de-DE.png) |

Dead zone with deactivated cooling or cooling factor (left) or activated cooling and PID parameter switching (right). The x / horizontal axis displays the control deviation = setpoint - process value. The y / vertical axis shows the output signal of the dead zone that is passed to the PID algorithm.

##### Control zone width

If the process value exits the control zone around the setpoint, the minimum or maximum output value is output. This means that the process value reaches the setpoint faster.

If the process value lies within the control zone around the setpoint, the output value is calculated by the PID algorithm.

The control zone width for heating or cooling is only set automatically during the pretuning, if "PID (temperature)" is selected as the controller structure for cooling or heating.

The control zone is deactivated by setting the control zone width = 3.402822e+38.

If cooling is deactivated in the basic settings or the cooling factor is used, the control zone lies symmetrically between "Setpoint - control zone width (heating)" and "Setpoint + control zone width (heating)".

If cooling is activated in the basic settings and PID parameter switching is selected as the method for heating/cooling in the output settings, the control zone lies between "Setpoint - control zone width (heating)" and "Setpoint + control zone width (cooling)".

![Control zone width](images/166014342283_DV_resource.Stream@PNG-de-DE.png)

Control zone with deactivated cooling or cooling factor​.

![Control zone width](images/166014365323_DV_resource.Stream@PNG-de-DE.png)

Control zone with activated cooling and PID parameter switching.

##### Rule for tuning

Select whether PI or PID parameters are to be calculated in the "Controller structure" drop-down list. You can specify the rules for tuning for heating and for tuning for cooling separately.

- PID (temperature)

  Calculates PID parameters during pretuning and fine tuning.

  Pretuning is designed for temperature processes and results in a slower and rather asymptotic control response with lower overshoot than with the "PID" option. Fine tuning is identical to the "PID" option.

  The control zone width is determined automatically during pretuning only if this option is selected.
- PID

  Calculates PID parameters during pretuning and fine tuning.
- PI

  Calculates PI parameters during pretuning and fine tuning.
- User-defined

  The drop-down list displays "User-defined" if you have configured different controller structures for pretuning and fine tuning via a user program or the parameter view.

## Commissioning PID_Temp (S7-1200, S7-1500)

This section contains information on the following topics:

- [Commissioning (S7-1200, S7-1500)](#commissioning-s7-1200-s7-1500)
- [Pretuning (S7-1200, S7-1500)](#pretuning-s7-1200-s7-1500)
- [Fine tuning (S7-1200, S7-1500)](#fine-tuning-s7-1200-s7-1500)
- ["Manual" mode (S7-1200, S7-1500)](#manual-mode-s7-1200-s7-1500)
- [Substitute setpoint (S7-1200, S7-1500)](#substitute-setpoint-s7-1200-s7-1500)
- [Cascade commissioning (S7-1200, S7-1500)](#cascade-commissioning-s7-1200-s7-1500)

### Commissioning (S7-1200, S7-1500)

The commissioning window helps you commission the PID controller. You can monitor the values for the setpoint, process value and the output values for heating and cooling along the time axis in the trend view. The following functions are supported in the commissioning window:

- Controller pretuning
- Controller fine tuning

  Use fine tuning for fine adjustments to the PID parameters.
- Monitoring the current closed-loop control in the trend view
- Testing the controlled system by specifying a manual PID output value and a substitute setpoint
- Saving the actual values of the PID parameters to an offline project.

All functions require an online connection to the CPU.

The online connection to the CPU is established, if it does not exist already, and operation of the commissioning window is enabled by means of the "Monitor all" ![Figure](images/166014421643_DV_resource.Stream@PNG-de-DE.png) or "Start" buttons of the trend view.

#### Operation of the trend view

- Select the desired sampling time in the "Sampling time" drop-down list.

  All the values of the trend view are updated in the selected sampling time.
- Click the "Start" icon in the Measurement group if you want to use the trend view.

  Value recording is started. The current values for the setpoint, process value and output values for heating and cooling are entered in the trend view.
- Click the "Stop" icon if you want to end the trend view.

  The values recorded in the trend view can continue to be analyzed.

Closing the commissioning window will terminate recording in the trend view and delete the recorded values.

### Pretuning (S7-1200, S7-1500)

The pretuning determines the process response to a jump change of the output value and searches for the point of inflection. The tuned PID parameters are calculated as a function of the maximum slope and dead time of the controlled system. You obtain the best PID parameters when you perform pretuning and fine tuning.

The more stable the process value is, the easier it is to calculate the PID parameters and the more precise the result will be. Noise on the process value can be tolerated as long as the rate of rise of the process value is significantly higher compared to the noise. This is most likely the case in operating modes "Inactive" or "Manual mode". The PID parameters are backed up before being recalculated.

PID_Temp offers different pretuning types depending on the configuration:

- Pretuning heating

  A jump is output at the output value heating, the PID parameters for heating are calculated and then the setpoint is used as the control variable in automatic mode.
- Pretuning heating and cooling

  A jump is output at the output value heating.

  As soon as the process value is close to the setpoint, a jump change is output at the output value cooling.

  The PID parameters for heating (Retain.CtrlParams.Heat structure) and cooling (Retain.CtrlParams.Cool structure) are calculated and then the setpoint is used as the control variable in automatic mode.
- Pretuning cooling

  A jump is output at the output value cooling.

  The PID parameters for cooling are calculated and then the setpoint is used as the control variable in automatic mode.

If you want to tune the PID parameters for heating and cooling, you can expect a better control response with "Pretuning heating" followed by "Pretuning cooling" rather than with "Pretuning heating and cooling". However, carrying out pretuning in two steps takes more time.

#### General requirements

- The PID_Temp instruction is called in a cyclic interrupt OB.
- ManualEnable = FALSE
- Reset = FALSE
- PID_Temp is in one of the following modes: "Inactive", "Manual mode", or "Automatic mode".
- The setpoint and the process value lie within the configured limits (see [Process value monitoring](#process-value-monitoring-s7-1200-s7-1500) configuration).

#### Requirements for pretuning heating

- The difference between setpoint and process value is greater than 30% of the difference between process value high limit and process value low limit.
- The distance between the setpoint and the process value is greater than 50% of the setpoint.
- The setpoint is greater than the process value.

#### Requirements for pretuning heating and cooling

- The cooling output in the "Basic settings" is activated (Config.ActivateCooling = TRUE).
- The PID parameter switching in the "Basic settings of output value" is activated (Config.AdvancedCooling = TRUE).
- The difference between setpoint and process value is greater than 30% of the difference between process value high limit and process value low limit.
- The distance between the setpoint and the process value is greater than 50% of the setpoint.
- The setpoint is greater than the process value.

#### Requirements for pretuning cooling

- The cooling output in the "Basic settings" is activated (Config.ActivateCooling = TRUE).
- The PID parameter switching in the "Basic settings of output value" is activated (Config.AdvancedCooling = TRUE).
- "Pretuning heating" or "Pretuning heating and cooling" has been carried out successfully (PIDSelfTune.SUT.ProcParHeatOk = TRUE). The same setpoint should be used for all tunings.
- The difference between setpoint and process value is smaller than 5% of the difference between process value high limit and process value low limit.

#### Procedure

To perform pretuning, follow these steps:

1. Double-click the "PID_Temp > Commissioning" entry in the project tree.
2. Activate the "Monitor all" ![Procedure](images/166014421643_DV_resource.Stream@PNG-de-DE.png) button or start the trend view.

   An online connection will be established.
3. Select the desired pretuning entry from the "Tuning mode" drop-down list.
4. Click the "Start" icon.

   - Pretuning is started.
   - The "Status" field displays the current steps and any errors that may have occurred. The progress bar indicates the progress of the current step.

**Note**

Click the "Stop" icon when the progress bar ("Progress" tag) has not changed for a long period and it is to be assumed that the tuning function is blocked. Check the configuration of the technology object and, if necessary, restart controller tuning.

#### Result

If pretuning was performed without an error message, the PID parameters have been tuned. PID_Temp switches to automatic mode and uses the tuned parameters. The tuned PID parameters will be retained during power OFF and a restart of the CPU.

If pretuning is not possible, PID_Temp responds with the configured responses in the event of an error.

### Fine tuning (S7-1200, S7-1500)

Fine tuning generates a constant, limited oscillation of the process value. The PID parameters are tuned for the operating point from the amplitude and frequency of this oscillation. The PID parameters are recalculated from the results. PID parameters from fine tuning usually have better master control and disturbance characteristics than PID parameters from pretuning. You obtain the best PID parameters when you perform pretuning and fine tuning.

PID_Temp automatically attempts to generate an oscillation greater than the noise of the process value. Fine tuning is only minimally influenced by the stability of the process value. The PID parameters are backed up before being recalculated.

PID_Temp offers different fine tuning types depending on the configuration:

- Fine tuning heating:

  PID_Temp generates an oscillation of the process value with periodic changes at the output value heating and calculates the PID parameters for heating.
- Fine tuning cooling:

  PID_Temp generates an oscillation of the process value with periodic changes at the output value cooling and calculates the PID parameters for cooling.

#### Temporary tuning offset for heating/cooling controllers

If PID_Temp is used as a heating/cooling controller (Config.ActivateCooling = TRUE), the PID output value (PidOutputSum) at the setpoint has to fulfill the following requirements so that process value oscillation can be generated and fine tuning can be carried out successfully:

- Positive PID output value for fine tuning heating
- Negative PID output value for fine tuning cooling

If this condition is not fulfilled, you can specify a temporary offset for fine tuning that is output at the opposing output.

- Offset for cooling output (PIDSelfTune.TIR.OutputOffsetCool) at fine tuning heating.

  Before starting tuning, enter a negative tuning offset cooling that is smaller than the PID output value (PidOutputSum) at the setpoint in the stationary state.
- Offset for heating output (PIDSelfTune.TIR.OutputOffsetHeat) at fine tuning cooling

  Before starting tuning, enter a positive tuning offset heating that is greater than the PID output value (PidOutputSum) at the setpoint in the stationary state.

The defined offset is balanced by the PID algorithm so that the process value remains at the setpoint. The height of the offset allows the PID output value to be adapted correspondingly so that it fulfills the requirement mentioned above.

To avoid larger overshoots of the process value when defining the offset, it can also be increased in several steps.

If PID_Temp exits the fine tuning mode, the tuning offset is reset.

#### Example: Specification of an offset for fine tuning cooling

- Without offset

  - Setpoint = Process value (ScaledInput) = 80 °C
  - PID output value (PidOutputSum) = 30.0
  - Output value heating (OutputHeat) = 30.0
  - Output value cooling (OutputCool) = 0.0

    Oscillation of the process value around the setpoint cannot be generated with the cooling output alone. Fine tuning would fail here.
- With offset for heating output (PIDSelfTune.TIR.OutputOffsetHeat) = 80.0

  - Setpoint = Process value (ScaledInput) = 80 °C
  - PID output value (PidOutputSum) = -50.0
  - Output value heating (OutputHeat) = 80.0
  - Output value cooling (OutputCool) = -50.0

    Thanks to the specification of an offset for the heating output, the cooling output can now generate oscillation of the process value around the setpoint. Fine tuning can now be carried out successfully.

#### General requirements

- The PID_Temp instruction is called in a cyclic interrupt OB.
- ManualEnable = FALSE
- Reset = FALSE
- The setpoint and the process value lie within the configured limits (see "Process value settings" configuration).
- The control loop has stabilized at the operating point. The operating point is reached when the process value corresponds to the setpoint.

  When the dead zone is switched on, the result can be a permanent control deviation (deviation between setpoint and actual value). This can have a negative effect on fine tuning.
- No disturbances are expected.
- PID_Temp is in inactive mode, automatic mode or manual mode.

#### Requirements for fine tuning heating

- Heat.EnableTuning = TRUE
- Cool.EnableTuning = FALSE
- If PID_Temp is configured as a heating-and-cooling controller (Config.ActivateCooling = TRUE), the heating output has to be active at the operating point where tuning is to be carried out.

  PidOutputSum > 0.0 (see tuning offset)

#### Requirements for fine tuning cooling

- Heat.EnableTuning = FALSE
- Cool.EnableTuning = TRUE
- The cooling output is activated (Config.ActivateCooling = TRUE).
- The PID parameter switching is activated (Config.AdvancedCooling = TRUE).
- The cooling output has to be active at the operating point where tuning is to be carried out.

  PidOutputSum < 0.0 (see tuning offset)

#### Process depends on initial situation

Fine tuning can be started from the following operating modes: "Inactive", "automatic mode", or "manual mode".

Fine tuning proceeds as follows when started from:

- Automatic mode with PIDSelfTune.TIR.RunIn = FALSE (default)

  Start fine tuning from automatic mode if you wish to improve the existing PID parameters through tuning.

  PID_Temp controls the system using the existing PID parameters until the control loop has stabilized and the requirements for fine tuning have been met. Only then will fine tuning start.
- Inactive, manual mode or automatic mode with PIDSelfTune.TIR.RunIn = TRUE

  An attempt is made to reach the setpoint with the minimum or maximum output value (two-point control):

  - With minimum or maximum output value heating at fine tuning heating.
  - With minimum or maximum output value cooling for fine tuning cooling.

  This can produce increased overshoot. Fine tuning starts when the setpoint is reached.

  If the setpoint cannot be reached, PID_Temp does not automatically abort tuning.

#### Procedure

To perform fine tuning, follow these steps:

1. Double-click the "PID_Temp > Commissioning" entry in the project tree.
2. Activate the "Monitor all" ![Procedure](images/166014421643_DV_resource.Stream@PNG-de-DE.png) button or start the trend view.

   An online connection will be established.
3. Select the desired fine tuning entry from the "Tuning mode" drop-down list.
4. If required (see tuning offset), specify a tuning offset and wait until the stationary state is reached again.
5. Click the "Start" icon.

   - The process of fine tuning is started.
   - The "Status" field displays the current steps and any errors that may have occurred.

     The progress bar indicates the progress of the current step.

**Note**

Click the "Stop" icon in the "Tuning mode" group if the progress bar ("Progress" tag) has not changed for a long period and it is to be assumed that the tuning function is blocked. Check the configuration of the technology object and, if necessary, restart controller tuning.

In the following phases in particular, tuning is not aborted automatically if the setpoint cannot be reached.

- "Attempting to reach setpoint for heating with two-point control."
- "Attempting to reach setpoint for cooling with two-point control."

#### Result

If fine tuning was performed without errors, the PID parameters have been tuned. PID_Temp switches to automatic mode and uses the tuned parameters. The tuned PID parameters will be retained during power OFF and a restart of the CPU.

If errors occurred during fine tuning, PID_Temp responds with the configured response to errors.

### "Manual" mode (S7-1200, S7-1500)

The following section describes how you can use "Manual mode" in the commissioning window of the "PID_Temp" technology object.

Manual mode is also possible when an error is pending.

#### Requirement

- The "PID_Temp" instruction is called in a cyclic interrupt OB.
- An online connection to the CPU has been established.
- The CPU is in "RUN" mode.

#### Procedure

If you want to test the controlled system by specifying a manual value, use "Manual mode" in the commissioning window.

To define a manual value, follow these steps:

1. Double-click the "PID_Temp > Commissioning" entry in the project tree.
2. Activate the "Monitor all" ![Procedure](images/166014421643_DV_resource.Stream@PNG-de-DE.png) button or start the trend view.

   An online connection will be established.
3. Select the "Manual mode" check box in the "Online status of controller" area.

   PID_Temp operates in manual mode. The most recent current output value remains in effect.
4. Enter the manual value in the editable field as a % value.

   If cooling is activated in the basic settings, enter the manual value as follows:

   - Enter a positive manual value to output the value at the outputs for heating.
   - Enter a negative manual value to output the value at the outputs for cooling.
5. Click the ![Procedure](images/166014425611_DV_resource.Stream@PNG-de-DE.png) icon.

#### Result

The manual value is written to the CPU and immediately goes into effect.

Clear the "Manual mode" check box if the output value is to be specified again by the PID controller.

The switchover to automatic mode is bumpless.

### Substitute setpoint (S7-1200, S7-1500)

The following section describes how you can use the substitute setpoint in the commissioning window of the "PID_Temp" technology object.

#### Requirement

- The "PID_Temp" instruction is called in a cyclic interrupt OB.
- An online connection to the CPU has been established.
- The CPU is in "RUN" mode.

#### Procedure

If you want to use a different value as the setpoint than that specified at the "Setpoint" parameter (for example to tune a slave in a cascade), use the substitute setpoint in the commissioning window.

Proceed as follows to specify a substitute setpoint:

1. Double-click the "PID_Temp > Commissioning" entry in the project tree.
2. Activate the "Monitor all" ![Procedure](images/166014421643_DV_resource.Stream@PNG-de-DE.png) button or start the trend view.

   An online connection will be established.
3. Select the "Subst.Setpoint" check box in the "Online status of controller" section.

   The substitute setpoint (SubstituteSetpoint tag) is initialized with the most recently updated setpoint and now used.
4. Enter the substitute setpoint in the editable field.
5. Click the ![Procedure](images/166014425611_DV_resource.Stream@PNG-de-DE.png) icon.

#### Result

The substitute setpoint is written to the CPU and immediately goes into effect.

Clear the "Subst.Setpoint" check box if the value at the "Setpoint" parameter is to be used again as setpoint.

The switchover is not bumpless.

### Cascade commissioning (S7-1200, S7-1500)

Information about cascade commissioning with PID_Temp is available under [Commissioning](#commissioning-s7-1200-s7-1500-1).

## Cascade control with PID_Temp (S7-1200, S7-1500)

This section contains information on the following topics:

- [Introduction (S7-1200, S7-1500)](#introduction-s7-1200-s7-1500-1)
- [Program creation (S7-1200, S7-1500)](#program-creation-s7-1200-s7-1500)
- [Configuration (S7-1200, S7-1500)](#configuration-s7-1200-s7-1500)
- [Commissioning (S7-1200, S7-1500)](#commissioning-s7-1200-s7-1500-1)
- [Substitute setpoint (S7-1200, S7-1500)](#substitute-setpoint-s7-1200-s7-1500-1)
- [Operating modes and fault response (S7-1200, S7-1500)](#operating-modes-and-fault-response-s7-1200-s7-1500)

### Introduction (S7-1200, S7-1500)

In cascade control, several control loops are nested within each other. In the process, slaves receive their setpoint (Setpoint) from the output value (OutputHeat) of the respective higher-level master.

A prerequisite for establishing a cascade control system is that the controlled system can be divided into subsystems, each with its own measured variable.

Setpoint specification for the controlled variable is carried out at the outmost master.

The output value of the innermost slave is applied to the actuator and thus acts on the controlled system.

The following major advantages result from the use of a cascade control system in comparison with a single-loop control system:

- Thanks to the additional subordinate control loops, disturbances which occur there are corrected quickly. Their influence on the controlled variable is reduced considerably. The disturbance behavior is thus improved.
- The subordinate control loops act in linearizing form. The negative effects of such non-linearities on the controlled variable are thus moderated.

PID_Temp offers the following functionality especially for use in cascade control systems:

- Specification of a substitute setpoint
- Exchange of status information between master and slave (for example, current operating mode)
- Different Anti-Wind-Up modes (response of the master to limitation of its slave)

#### Example

The following block diagram shows a cascade control system with PID_Temp using the simplified example of a chocolate melting unit:

![Example](images/166014429579_DV_resource.Stream@PNG-de-DE.png)

The PID_Temp_1 master compares the process value of the chocolate temperature (TempChocolate) with the setpoint specification by the user at the Setpoint parameter. Its output value OutputHeat forms the setpoint of the slave PID_Temp_2.

PID_Temp_2 attempts to regulate the process value of the water-bath temperature (TempWater) to this setpoint. The output value of PID_Temp_2 acts directly on the actuator of the controlled system (heating of the water bath) and thus influences the water-bath temperature. The water-bath temperature in turn has an effect on the chocolate temperature.

#### FAQ

For more information, see the following FAQs in the Siemens Industry Online Support:

- Entry ID [103526819](https://support.industry.siemens.com/cs/ww/en/view/103526819)

---

**See also**

[Program creation (S7-1200, S7-1500)](#program-creation-s7-1200-s7-1500)

### Program creation (S7-1200, S7-1500)

Observe the following points during program creation:

- Number of PID_Temp instances

  The number of different PID_Temp instances called up in a cyclic interrupt OB has to agree with the number of concatenated measured variables in the process.

  There are two concatenated measured variables in the example: TempChocolate and TempWater. Therefore two PID_Temp instances are required.
- Call sequence

  A master has to be called before its slaves in the same cyclic interrupt OB.

  The outermost master at which the user setpoint is specified is called first.

  The slave whose setpoint is specified by the outermost master is called next, etc.

  The innermost slave that acts on the actuator of the process with its output value is called last.

  In the example, PID_Temp_1 is called before PID_Temp_2.
- Interconnection of the measured variables

  The outermost master is interconnected with the outermost measured variable that is to be regulated to the user setpoint.

  The innermost slave is interconnected with the innermost measured variable that is influenced directly by the actuator.

  Interconnection of the measured variables with PID_Temp is carried out with the parameters Input or Input_PER.

  In the example, the outermost measured variable TempChocolate is interconnected with PID_Temp_1 and the innermost measured variable TempWater with PID_Temp_2.
- Interconnection of the output value of the master to the setpoint of the slave

  The output value (OutputHeat) of a master has to be assigned to the setpoint (Setpoint) of its slave.

  This interconnection can be carried out in the programming editor or automatically in the Inspector window of the slave in the basic settings via the selection of the master.

  If required, you can insert your own filter or scaling functions, for example in order to adapt the output value range of the master to the setpoint/process value range of the slave.

  In the example, OutputHeat of PID_Temp_1 is assigned to Setpoint of PID_Temp_2.
- Interconnection of the interface for information exchange between master and slave

  The "Slave" parameter of a master has to be assigned to the "Master" parameter of all its directly subordinate slaves (which receive their setpoint from this master). The assignment should be carried out via the interface of the slave in order to allow the interconnection of a master with multiple slaves and the display of the interconnection in the Inspector window of the slave in the basic settings.

  This interconnection can be carried out in the programming editor or automatically in the Inspector window of the slave in the basic settings via the selection of the master.

  The Anti-Wind-Up functionality and the evaluation of the slave operating modes at the master can only function correctly if this interconnection is carried out.

  In the example, the "Slave" parameter of PID_Temp_1 is assigned to the "Master" parameter of PID_Temp_2.

Program code of the example using SCL (without assignment of the output value of the slave to the actuator):

`"PID_Temp_1"(Input:="TempChocolate");`

`"PID_Temp_2"(Input:="TempWater", Master := "PID_Temp_1".Slave, Setpoint := "PID_Temp_1".OutputHeat);`

---

**See also**

[PID_Temp ActivateRecoverMode tag (S7-1200, S7-1500)](PID_Temp%20%28S7-1200%2C%20S7-1500%29.md#pid_temp-activaterecovermode-tag-s7-1200-s7-1500)

### Configuration (S7-1200, S7-1500)

You can carry out the configuration via your user program, the configuration editor or the Inspector window of the PID_Temp call.

When using PID_Temp in a cascade control system, ensure the correct configuration of the settings specified below.

If a PID_Temp instance receives its setpoint from a superior master controller and outputs its output value in turn to a subordinate slave controller, this PID_Temp instance is both a master controller and a slave controller simultaneously. Both configurations listed below have to be carried out for such a PID_Temp instance. This is the case, for example, for the middle PID_Temp instance in a cascade control system with three concatenated measured variables and three PID_Temp instances.

#### Configuration of a master

| Setting in the configuration editor or Inspector window | DB parameter | Explanation |
| --- | --- | --- |
| Basic settings → Cascade:  Activate "Controller is master" check box | Config.Cascade.IsMaster = TRUE | Activates this controller as a master in a cascade |
| Basic settings → Cascade:  Number of slaves | Config.Cascade.CountSlaves | Number of directly subordinate slaves that receive their setpoint directly from this master |
| Basic settings → Input/output parameters:  Selection of the output value (heating) = OutputHeat | Config.Output.Heat.Select = 0 | The master only uses the output parameter OutputHeat.   OutputHeat_PWM and OutputHeat_PER are deactivated. |
| Basic settings → Input/output parameters:  Clear "Activate cooling" check box | Config.ActivateCooling = FALSE | The cooling has to be deactivated at a master. |
| Output settings → Output limits and scaling → OutputHeat / OutputCool:  PID output value low limit (heating), PID output value high limit (heating), Scaled low output value (heating), Scaled high output value (heating) | Config.Output.Heat.PidLowerLimit,  Config.Output.Heat.PidUpperLimit,  Config.Output.Heat.LowerScaling,  Config.Output.Heat.UpperScaling | If no own scaling function is used when assigning OutputHeat of the master to Setpoint of the slave, it may be necessary to adapt the output value limits and the output scaling of the master to the setpoint/process value range of the slave. |
| This tag is not available in the Inspector window or in the functional view of the configuration editor.  You can change it via the parameter view of the configuration editor. | Config.Cascade.AntiWindUpMode | The Anti-Wind-Up mode determines how the integral action of this master is treated if directly subordinate slaves reach their output value limits.   Options are:  - AntiWindUpMode = 0:    The AntiWindUp functionality is deactivated. The master does not react to the limitation of its slaves. - AntiWindUpMode = 1 (default):   The integral action of the master is reduced in the relationship "Slaves in limitation/Number of slaves". This reduces the effects of the limitation on the control behavior. - AntiWindUpMode = 2:   The integral action of the master is held as soon as a slave is in limitation. |

#### Configuration of a slave

| Setting in the configuration editor or Inspector window | DB parameter | Explanation |
| --- | --- | --- |
| Basic settings → Cascade:  Select the "Controller is slave" check box | Config.Cascade.IsSlave = TRUE | Activates this controller as a slave in a cascade |

### Commissioning (S7-1200, S7-1500)

After compiling and loading of the program, you can start commissioning of the cascade control system.

Begin with the innermost slave at commissioning (implementation of tuning or change to automatic mode with existing PID parameters) and continue outwards until the outermost master has been reached.

In the above example, commissioning starts with PID_Temp_2 and is continued with PID_Temp_1.

#### Tuning the slave

Tuning of PID_Temp requires a constant setpoint. Therefore, activate the substitute setpoint of a slave (SubstituteSetpoint and SubstituteSetpointOn tags) to tune the slave or set the associated master to manual mode with a corresponding manual value. This ensures that the setpoint of the slave remains constant during tuning.

#### Tuning the master

In order for a master to influence the process or to carry out tuning, all the downstream slaves have to be in automatic mode and their substitute setpoint has to be deactivated. A master evaluates these conditions through the interface for information exchange between master and slave (Master parameter and Slave parameter) and displays the current state at the AllSlaveAutomaticState and NoSlaveSubstituteSetpoint tags. Corresponding status messages are output in the commissioning editor.

| Status message in the commissioning editor of the master | DB parameter of the master | Correction |
| --- | --- | --- |
| One or more slaves are not in automatic mode. | AllSlaveAutomaticState = FALSE,  NoSlaveSubstituteSetpoint = TRUE | First, carry out commissioning of all downstream slaves.  Ensure that the following conditions are fulfilled before carrying out tuning or activating manual mode or automatic mode of the master:  - All downstream slaves are in automatic mode (state = 3). - All downstream slaves have deactivated the substitute setpoint (SubstituteSetpointOn = FALSE). |
| One or more slaves have activated the substitute setpoint. | AllSlaveAutomaticState = TRUE,  NoSlaveSubstituteSetpoint = FALSE |  |
| One or more slaves are not in automatic mode and have activated the substitute setpoint. | AllSlaveAutomaticState = FALSE,  NoSlaveSubstituteSetpoint = FALSE |  |

If pretuning or fine tuning is started for a master, PID_Temp aborts tuning in the following cases and displays an error with ErrorBits = DW#16#0200000:

- One or more slaves are not in automatic mode (AllSlaveAutomaticState = FALSE)
- One or more slaves have activated the substitute setpoint (NoSlaveSubstituteSetpoint = FALSE).

The subsequent operating mode changeover depends on ActivateRecoverMode.

### Substitute setpoint (S7-1200, S7-1500)

In order to specify a setpoint, PID_Temp offers a substitute setpoint at the SubstituteSetpoint tag in addition to the Setpoint parameter. This can be activated by setting SubstituteSetpointOn = TRUE or by selecting the corresponding check box in the commissioning editor.

The substitute setpoint allows you to specify the setpoint temporarily directly at the slave, for example during commissioning or tuning.

In this case, the interconnection of the output value of the master with the setpoint of the slave that is required for normal operation of the cascade control system does not have to be changed in the program

In order for a master to influence the process or to carry out tuning, the substitute setpoint has to be deactivated at all downstream slaves.

You can monitor the currently effective setpoint as it is used by the PID algorithm for calculation at the CurrentSetpoint tag.

### Operating modes and fault response (S7-1200, S7-1500)

The master or slave of a PID_Temp instance does not change the operating mode of this PID_Temp instance.

If a fault occurs at one of its slaves, the master remains in its current operating mode.

If a fault occurs at its master, the slave remains in its current operating mode. However, further operation of the slave then depends on the fault and the configured fault response of the master since the output value of the master is used as the setpoint of the slave:

- If ActivateRecoverMode = TRUE is configured at the master. and the fault does not prevent the calculation of OutputHeat, the fault does not have any effect on the slave.
- If ActivateRecoverMode = TRUE is configured at the master and the fault prevents the calculation of OutputHeat, the master outputs the last output value or the configured substitute output value SubstituteOutput, depending on SetSubstituteOutput. This is then used by the slave as the setpoint.

  PID_Temp is preconfigured so that the substitute output value 0.0 is output in this case (ActivateRecoverMode = TRUE, SetSubstituteOutput = TRUE, SubstituteOutput = 0.0). Configure a suitable substitute output value for your application or activate the use of the last valid PID output value (SetSubstituteOutput = FALSE).
- If ActivateRecoverMode = FALSE is configured at the master, the master changes to the "Inactive" mode when a fault occurs and outputs OutputHeat = 0.0. The slave then uses 0.0 as the setpoint.

The fault response is located in the output settings in the configuration editor.

## Multi-zone controlling with PID_Temp (S7-1200, S7-1500)

### Introduction

In a multi-zone control system, several sections, so-called zones, of a plant are controlled simultaneously to different temperatures. A multi-zone control system is characterized by the mutual influence of the temperature zones through thermal coupling, i.e. the process value of one zone can influence the process value of a different zone through thermal coupling. The strength that this influence has depends on the structure of the plant and the selected operating points of the zones.

Example: Extrusion plant as it is used, for example, in plastics processing.

The substance mixture that passes through the extruder has to be controlled to different temperatures for optimal processing. For example, different temperatures can be required at the filling point of the extruder than at the outlet nozzle. The individual temperature zones mutually influence each other through thermal coupling.

When PID_Temp is used in multi-zone control systems, each temperature zone is controlled by a separate PID_Temp instance.

Observe the following explanations if you want to use the PID_Temp in a multi-zone control system.

### Separate pretuning for heating and cooling

Initial commissioning of a plant as a rule begins with the carrying out of pretuning in order to carry out initial setting of the PID parameters and control to the operating point. The pretuning for multi-zone control systems is often carried out simultaneously for all zones.

PID_Temp offers the possibility of carrying out pretuning for heating and cooling in one step (Mode = 1, Heat.EnableTuning = TRUE, Cool.EnableTuning = TRUE) for controllers with activated cooling and PID parameter switching as the method for heating/cooling (Config.ActivateCooling = TRUE, Config.AdvancedCooling = TRUE).

However, it is advisable not to use this tuning for simultaneous pretuning of several PID_Temp instances in a multi-zone control system. Instead, first carry out the pretuning for heating (Mode = 1, Heat.EnableTuning = TRUE, Cool.EnableTuning = FALSE) and the pretuning for cooling (Mode = 1, Heat.EnableTuning = FALSE, Cool.EnableTuning = TRUE) separately.

Pretuning for cooling should not be started until all zones have completed pretuning for heating and have reached their operating points.

This reduces mutual influencing through thermal coupling between the zones during tuning.

### Adapting the delay time

If PID_Temp is used in a multi-zone control system with strong thermal couplings between the zones, you should ensure that the adaption of the delay time is deactivated for pretuning with PIDSelfTune.SUT.AdaptDelayTime = 0. Otherwise, the determination of the delay time can be incorrect if the cooling of a zone is prevented by the thermal influence of other zones during the adapting of the delay time (heating is deactivated in this phase).

### Temporary deactivation of cooling

PID_Temp offers the possibility of deactivating cooling temporarily in automatic mode for controllers with active cooling (Config.ActivateCooling = TRUE) by setting DisableCooling = TRUE.

This ensures that this controller does not cool in automatic mode during commissioning while the controllers of other zones have not yet completed tuning of heating. The tuning could otherwise be influenced negatively by the thermal coupling between the zones.

### Procedure

You can proceed as follows during the commissioning of multi-zone control systems with relevant thermal couplings:

1. Set DisableCooling = TRUE for all controllers with activated cooling.
2. Set PIDSelfTune.SUT.AdaptDelayTime = 0 for all controllers.
3. Specify the desired setpoints (Setpoint parameter) and start pretuning for heating (Mode = 1, Heat.EnableTuning = TRUE, Cool.EnableTuning = FALSE) simultaneously for all controllers.
4. Wait until all the controllers have completed pretuning for heating.
5. Set DisableCooling = FALSE for all controllers with activated cooling.
6. Wait until the process values of all the zones are steady and close to the respective setpoint.

   If the setpoint cannot be reached permanently for a zone, the heating or cooling actuator is too weak.
7. Start pretuning for cooling (Mode = 1, Heat.EnableTuning = FALSE, Cool.EnableTuning = TRUE) for all controllers with activated cooling.

> **Note**
>
> **Limit violation of the process value**
>
> If the cooling is deactivated in automatic mode with DisableCooling = TRUE, this can cause the process value to exceed the setpoint and the process value limits while DisableCooling = TRUE. Observe the process values and intervene, if appropriate, if you use DisableCooling.

> **Note**
>
> **Multi-zone control systems**
>
> For multi-zone control systems, the thermal couplings between the zones can result in increased overshoots, permanent or temporary violation of limits and permanent or temporary control deviations during commissioning or operation. Observe the process values and be ready to intervene. Depending on the system, it can be necessary to deviate from the procedure described above.

### Synchronization of several fine tuning processes

If fine tuning is started from automatic mode with PIDSelfTune.TIR.RunIn = FALSE, PID_Temp tries to reach the setpoint with PID controlling and the current PID parameters. The actual tuning does not start until the setpoint is reached. The time required to reach the setpoint can be different for the individual zones of a multi-zone control system.

If you want to carry out fine tuning for several zones simultaneously, PID_Temp offers the possibility to synchronize these by waiting with the further tuning steps after the setpoint has been reached.

### Procedure

This ensures that all the controllers have reached their setpoint when the actual tuning steps start. This reduces mutual influencing through thermal coupling between the zones during tuning.

Proceed as follows for controllers for whose zones you want to carry out fine tuning simultaneously:

1. Set PIDSelfTune.TIR.WaitForControlIn = TRUE for all controllers.

   These controllers have to be in automatic mode with PIDSelfTune.TIR.RunIn = FALSE.
2. Specify the desired setpoints (Setpoint parameters) and start fine tuning for all controllers.
3. Wait until PIDSelfTune.TIR.ControlInReady = TRUE at all controllers.
4. Set PIDSelfTune.TIR.FinishControlIn = TRUE for all controllers.

All controllers then start the actual tuning simultaneously.

## Override control with PID_Temp (S7-1200, S7-1500)

### Override control

In case of override control, two or more controllers share one actuator. Only one controller has access to the actuator at any time and influences the process.

A logic operation decides which controller has access to the actuator. This decision is often made based on a comparison of the output values of all controllers, for example, in case of a maximum selection, the controller with the largest output value gets access to the actuator.

The selection based on the output value requires that all controllers operate in automatic mode. The controllers that do not have an effect on the actuator are updated. This is necessary to prevent windup effects and their negative impacts on the control response and the switchover between the controllers.

PID_Temp supports override controls as of version 1.1 by offering a simple process for updating the controllers that are not active: By using the tags OverwriteInitialOutputValue and PIDCtrl.PIDInit, you can pre-assign the integral action of the controller in automatic mode as though the PID algorithm had calculated PidOutputSum = OverwriteInititalOutputValue for the PID output value in the last cycle. To do this, OverwriteInitialOutputValue is interconnected with the PID output value of the controller that currently has access to the actuator. By setting the bit PIDCtrl.PIDInit, you trigger the preassignment of the integral action as well as the restart of the controller cycle and the PWM period. The subsequent calculation of the PID output value in the current cycle takes place based on the preassigned (and synchronized for all controllers) integral action as well as the proportional action and integral action from the current control deviation. The derivative action is not active during the call with PIDCtrl.PIDInit = TRUE and therefore does not contribute to the output value.

This procedure ensures that the calculation of the current PID output value and thus the decision on which controller is to have access to the actuator is only based on the current process state and the PI parameters. Windup effects for controllers that are not active and thus incorrect decisions of the switchover logic are prevented.

### Requirement

- PIDCtrl.PIDInit is only effective if the integral action is activated (tags Retain.CtrlParams.Heat.Ti and Retain.CtrlParams.Cool.Ti > 0.0).
- You must assign PIDCtrl.PIDInit and OverwriteInitialOutputValue in your user program yourself (see example below). PID_Temp does not automatically change these tags.
- PIDCtrl.PIDInit is only effective when PID_Temp is in automatic mode (parameter State = 3).
- If possible, select the sampling time of the PID algorithm ( Retain.CtrlParams.Heat.Cycle and Retain.CtrlParams.Cool.Cycle tags) so that it is identical for all controllers, and call all controllers in the same cyclic interrupt OB. In this way, you ensure that the switchover does not take place within a controller cycle or a PWM period.

> **Note**
>
> **Constant adaptation of the output value limits**
>
> Instead of the active updating of the controllers without access to the actuator described here, this is implemented alternatively by constant adaptation of the output value limits in other controller systems.
>
> This is not possible with PID_Temp, because a change of the output value limits is not supported in automatic mode.

### Example: Control of a large boiler

PID_Temp is used for control of a large boiler.

The main goal is to control the temperature Input1. The controller PID_Temp_1 is used for this purpose. In addition, the temperature Input2 is to be kept below a high limit at an additional measuring point with the limiting controller PID_Temp_2.

Both temperatures are influenced by only one heater. The output value of the controller corresponds to the heating power.

![Example: Control of a large boiler](images/166014473227_DV_resource.Stream@PNG-de-DE.png)

The heater is controlled with the pulse-width modulated output value of PID_Temp (parameter OutputHeat_PWM) by writing the program tag ActuatorInput. The setpoint for the temperature Input1 is specified at the parameter PID_Temp_1.Setpoint. The temperature high limit for the additional measuring point is specified as setpoint at the parameter PID_Temp_2.Setpoint.

![Example: Control of a large boiler](images/166014478347_DV_resource.Stream@PNG-de-DE.png)

Both controllers must share one heater as shared actuator. The logic that decides which controller gets access to the actuator is implemented by a minimum selection of the PID output value (in Real format, parameter PidOutputSum) in this case. Because the PID output value corresponds to the heating power, the controller that requires lower heating power gets the control.

In normal operation of the plant, the process value of the main controlled variable corresponds to the setpoint. The main controller PID_Temp_1 has settled on a stationary PID output value PID_Temp_1.PidOutputSum. The process value of the limiting controller Input2 in normal operation is significantly below the high limit that is specified as setpoint for PID_Temp_2. The limiting controller therefore wants to increase the heating power to increase its process value, which means it will calculate a PID output value PID_Temp_2.PidOutputSum that is greater than the output value of the main controller PID_Temp_1.PidOutputSum. The minimum selection of the switchover logic therefore gives the main controller PID_Temp_1 continued access to the actuator. In addition, it is ensured that PID_Temp_2 is updated by means of the assignments PID_Temp_2.OverwriteInitialOutputValue = PID_Temp_1.PidOutputSum and PID_Temp_2.PIDCtrl.PIDInit = TRUE.

If Input2 now approaches the high limit or exceeds it, for example due to a fault, the limiting controller PID_Temp_2 calculates a smaller PID output value to restrict the heating power and thus reduce Input2. If PID_Temp_2.PidOutputSum is smaller than PID_Temp_1.PidOutputSum, the limiting controller PID_Temp_2 receives access to the actuator through the minimum selection and reduces the heating power. It is ensured that PID_Temp_1 is updated by means of the assignments PID_Temp_1.OverwriteInitialOutputValue = PID_Temp_2.PidOutputSum and PID_Temp_1.PIDCtrl.PIDInit = TRUE.

The temperature at the additional measuring point Input2 drops. The temperature of the main controlled variable Input1 drops as well and cannot be held at the setpoint any longer.

Once the fault has been remedied, the Input2 will continue to drop and the heating power is further increased by the limiting controller. As soon as the main controller has calculated a lower heating power as output value, the plant returns to normal operation so that the main controller PID_Temp_1 once again has access to the actuator. This example can be implemented with the following SCL program code:

| Symbol | Meaning |
| --- | --- |
| `"PID_Temp_1"(Input := "Input1");` |  |
| `"PID_Temp_2"(Input := "Input2");` |  |
| `IF "PID_Temp_1".PidOutputSum <= "PID_Temp_2".PidOutputSum THEN` |  |
|  | `"ActuatorInput" := "PID_Temp_1".OutputHeat_PWM;` |
|  | `"PID_Temp_1".PIDCtrl.PIDInit := FALSE;` |
|  | `"PID_Temp_2".PIDCtrl.PIDInit := TRUE;` |
|  | `"PID_Temp_2".OverwriteInitialOutputValue := "PID_Temp_1".PidOutputSum;` |
| `ELSE` |  |
|  | `"ActuatorInput" := "PID_Temp_2".OutputHeat_PWM;` |
|  | `"PID_Temp_1".PIDCtrl.PIDInit := TRUE;` |
|  | `"PID_Temp_2".PIDCtrl.PIDInit := FALSE;` |
|  | `"PID_Temp_1".OverwriteInitialOutputValue := "PID_Temp_2".PidOutputSum;` |
| `END_IF;` |  |

## Simulating PID_Temp with PLCSIM (S7-1200, S7-1500)

> **Note**
>
> **Simulation with PLCSIM**
>
> The simulation of PID_Temp with PLCSIM for CPU S7-1200 is not supported.
>
> PID_TEMP can be simulated only for CPU S7-1500 with PLCSIM.
>
> For the simulation with PLCSIM, the time behavior of the simulated PLC is not exactly identical to that of a "real" PLC. The actual cycle clock of a cyclic interrupt OB can have larger fluctuations with a simulated PLC than with "real" PLCs.
>
> In the standard configuration, PID_Temp determines the time between calls automatically and monitors them for fluctuations.
>
> For the simulation of PID_Temp with PLCSIM, for example, a sampling time error (ErrorBits = DW#16#00000800) can therefore be detected.
>
> This results in ongoing tuning being aborted.
>
> The response in automatic mode depends on the value of the ActivateRecoverMode tag.
>
> To prevent this from happening, you should configure PID_Temp for simulation with PLCSIM as follows:
>
> - CycleTime.EnEstimation = FALSE
> - CycleTime.EnMonitoring = FALSE
> - CycleTime.Value: Assign the cycle clock of the calling cyclic interrupt OB in seconds to this tag.

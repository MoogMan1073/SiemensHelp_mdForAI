---
title: "Using the module (S7-1500)"
package: TFPulseTM15enUS
topics: 48
devices: [S7-1500, S7-1500T]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Using the module (S7-1500)

This section contains information on the following topics:

- [Using TM Pulse 2x24V (S7-1500)](#using-tm-pulse-2x24v-s7-1500)
- [Using TM PTO 4 (S7-1500)](#using-tm-pto-4-s7-1500)
- [Using TM PTO 2x24V (S7-1500)](#using-tm-pto-2x24v-s7-1500)
- [Using Compact CPU (S7-1500)](#using-compact-cpu-s7-1500)

## Using TM Pulse 2x24V (S7-1500)

This section contains information on the following topics:

- [Configuration and parameter assignment of technology module (S7-1500)](#configuration-and-parameter-assignment-of-technology-module-s7-1500)
- [Online & Diagnostics module (S7-1500)](#online-diagnostics-module-s7-1500)

### Configuration and parameter assignment of technology module (S7-1500)

This section contains information on the following topics:

- [Adding a technology module to hardware configuration (S7-1500)](#adding-a-technology-module-to-hardware-configuration-s7-1500)
- [Parameter setting (hardware configuration) Opening (S7-1500)](#parameter-setting-hardware-configuration-opening-s7-1500)
- [Channel configuration (S7-1500)](#channel-configuration-s7-1500)
- [Operating mode (S7-1500)](#operating-mode-s7-1500)
- [Reaction to CPU STOP (S7-1500)](#reaction-to-cpu-stop-s7-1500)
- [Diagnostics (S7-1500)](#diagnostics-s7-1500)
- [Parameter (S7-1500)](#parameter-s7-1500)

#### Adding a technology module to hardware configuration (S7-1500)

##### Requirements

- The project has been created.
- The CPU has been created.
- The ET 200 distributed I/O has been created.

##### Procedure

To add a technology module to the hardware configuration, proceed as follows:

1. Open the device configuration of the CPU or IM.
2. Select a module rack.
3. Select the technology module from the module catalog:  
   "Technology modules > Pulse output > TM Pulse 2x24V > Article number"
4. Drag the technology module to the required slot in the module rack.

#### Parameter setting (hardware configuration) Opening (S7-1500)

##### Opening from the device view

Proceed as follows:

1. Open the device configuration of the CPU or IM.
2. Select the device view.
3. Click on the module.

#### Channel configuration (S7-1500)

##### Channel configuration

This parameter is used to specify whether both channels are to be connected in parallel.

| Channel configuration | Meaning |
| --- | --- |
| 2 channels (2 A) (default) | The two channels operate separately and each has a maximum output current of 2 A. |
| 1 channel (4 A) | The two channels are connected in parallel and operate as a logical channel with a maximum output current of 4 A.  All parameter settings and operations that use the control interface must use addresses with Channel 0. Feedback signals are only provided for Channel 0.  The control and feedback interface is limited to one channel only. Channel 1 cannot be configured or operated.   Current measurement adds the measured values ​​of both channels. |

> **Note**
>
> **High-speed output**
>
> The "High-Speed Output (0.1 A)" can only be selected for the channel configuration "2 Channels (2 A)".

#### Operating mode (S7-1500)

##### Operating mode

You use this parameter to specify the function for which the channel of the technology module is used. This defines the setting options under "Parameters".

| Operating mode | Meaning | Mode-dependent [parameters](#parameter-s7-1500) |
| --- | --- | --- |
| Pulse output | The channel outputs a single pulse. You specify the pulse duration in the control interface. | - High-speed output (0.1 A) - Function DI - Input delay - On delay |
| Pulse width modulation PWM (default) | The channel outputs a pulse width modulated signal. You specify the duty cycle and/or the current setpoint in the control interface. | - High-speed output (0.1 A) - Function DI<sup>1</sup> - Input delay - Output format - Minimum pulse duration - Period duration - Actual period duration - On delay <sup>1</sup> - Dithering - Incline of dithering ramp up - Incline of dithering ramp down - Dithering amplitude - Dithering period duration - Current control - Enable proportional action - Enable integral action - Enable derivative action - Reference value current - Dead band width - Manipulated value high limit - Manipulated value low limit - Proportional gain - Integration time - Derivative action time - Delay time of derivative action |
| Pulse train | The channel outputs a number of pulses. You specify the number of pulses in the control interface. | - High-speed output (0.1 A) - Function DI - Input delay - Output format - Period duration - Actual period duration - On delay - Duty cycle |
| On/Off delay | The channel outputs pulses with specified switching delay with respect to DI0. You specify the On delay in the control interface. | - High-speed output (0.1 A) - Input delay - Off delay |
| Frequency output | The channel outputs a signal with a fixed duty cycle of 50%. You specify the frequency in the control interface. | - High-speed output (0.1 A) - Function DI - Input delay - Output format - On delay |
| PWM with DC motor | The channel outputs a pulse width modulated signal for controlling a DC motor in both directions of rotation. You specify the duty cycle in the control interface. | - Function DI<sup>1</sup> - Input delay - Output format - Period duration - Actual period duration - On delay <sup>1</sup> |
| <sup>1</sup> Parameters cannot be assigned in isochronous mode |  |  |

#### Reaction to CPU STOP (S7-1500)

**Reaction to CPU STOP**

You use this parameter to determine the response of the channel to the failure of a higher-level controller.

| Reaction to CPU STOP | Meaning |
| --- | --- |
| Output substitute value (default) | The channel outputs the configured substitute values at the digital outputs until the next STOP-RUN transition of the CPU. You can configure the substitute value 1 for only one of the two digital outputs.  An active output sequence is stopped and the STS_ENABLE feedback bit is reset.  The module is returned to its startup state after a STOP-RUN transition. Before you can start a new pulse output, you must reset the SW_ENABLE control bit. |
| Continue operation | The channel continues to operate.  The digital outputs continue to switch according to the parameter assignment. An active output sequence will thus be continued. If you have configured the hardware enable, you can also start additional output sequences using DIn.0.  The configuration of the technology module is not reset after a STOP-RUN transition. |

**Substitute value for DQA**

This parameter lets you specify which value the technology module is to output to the digital output DQA in the event of a CPU STOP under "Output substitute value".

The default setting is "0".

**Substitute value for DQB**

This parameter lets you specify which value the technology module is to output to the digital output DQB in the event of a CPU STOP under "Output substitute value".

The default setting is "0".

> **Note**
>
> You can select the default value 1 for only one of the two digital outputs.

#### Diagnostics (S7-1500)

The technology module can trigger additional diagnostic interrupts when you enable the diagnostic interrupts in the basic parameters. These diagnostic interrupts are processed in an interrupt OB.

##### Group diagnostics

You use this parameter to specify whether a diagnostic interrupt is to be triggered for following errors:

- Supply voltage fault (feedback bit ERR_PWR)
- Short-circuit or overload at sensor supply (feedback bit ERR_24V)
- Load voltage missing
- Overtemperature

The parameter is disabled in the default setting.

##### Diagnostics DQA

You use this parameter to specify whether a diagnostic interrupt "Error at digital outputs" is to be triggered in the event of an error at the digital output DQA. Regardless of this, the feedback bit ERR_DQA is set when an error occurs.

The parameter is disabled in the default setting.

##### Diagnostics DQB

You use this parameter to specify whether a diagnostic interrupt "Error at digital outputs" is to be triggered in the event of an error at the digital output DQB. Regardless of this, the feedback bit ERR_DQB is set when an error occurs.

The parameter is disabled in the default setting.

#### Parameter (S7-1500)

##### High-speed output (0.1 A)

Use this parameter to specify whether or not the respective digital output works as a fast push-pull switch.

| Option | Meaning |
| --- | --- |
| Activated | The digital outputs work as fast push-pull switches and each can carry a rated load current of 0.1 A. A push-pull switch is alternately switched to DC 24 V and ground. This makes for very fast edges. |
| Disabled (default) | The digital outputs work as fast push-pull switches and each can carry a rated load current of 2 A. |

> **Note**
>
> **Channel configuration**
>
> You can only select this parameter with the channel configuration "2 channels (2 A)".

> **Note**
>
> You cannot enable this parameter in the operating modes "PWM with DC motor" and "Pulse width modulation PWM" with current control.

##### Function DI

By configuring a digital input, you specify which functions the digital input triggers at switching.

You can select from the following options:

| Function | Meaning |
| --- | --- |
| Input (pre-selected) | No function is assigned to the respective digital input. The signal status of the digital input can be read by the CPU by means of the feedback interface. |
| HW enable | The respective digital input is used as enable input for the output sequence. |
| Limit switch | The respective digital input is used as external limit switch for a DC motor in the "PWM with DC motor" mode. |

##### Input delay

This parameter can be used to suppress signal noise at the digital inputs of a channel. Changes to the signal are only detected if they remain stable for longer than the configured input delay time.

You can select from the following input delays:

- None  
  (input delay of 4 μs, minimum pulse width of 3 μs)
- 0.05 ms
- 0.1 ms (default)
- 0.4 ms
- 0.8 ms
- 1.6 ms
- 3.2 ms
- 12.8 ms
- 20 ms

> **Note**
>
> If you select the "None" or "0.05 ms" option, you have to use shielded cables for connection of the digital inputs.

##### Output format

Use this parameter to specify the format or the value range with which the duty cycle or the current setpoint is evaluated:

| Output format | Value range |
| --- | --- |
| S7 analog output | "PWM with DC motor" mode:  ‒27648 ... 27648  Other operating mode:  0 ... 27648  ("27648" corresponds to 100% of Reference value current) |
| 1/100 (default) | 0 ... 100 |
| 1/1000 | 0 ... 1000 |
| 1/10000 | 0 ... 10000 |

> **Note**
>
> In "Frequency output" mode, "1 Hz" is selected as output format and cannot be changed.
>
> In "PWM with DC motor" mode, "S7 analog output" is selected as output format and cannot be changed.

##### Minimum pulse duration

This parameter is used to specify the minimum permitted pulse duration for the PWM signal.

Pulses and pauses which fall below the value are suppressed.

The default setting is "0 μs".

> **Note**
>
> The Minimum pulse duration is not effective if you have activated "Current control".

##### Period duration

This parameter is used to specify the period duration of the output signal.

In "PWM with DC motor" mode, the default setting is "1000 μs" (= 1 ms). In other operating modes the default setting is "2000000 μs" (= 2 s).

##### Actual period duration

The actual period duration is only displayed in isochronous mode.

The displayed value is the utilized period duration, which is calculated from the input period duration and the set application cycle.

##### On delay

This parameter is used to specify the delay with which the start of the output sequence effects the output of the pulse.

The default setting is "0 μs".

> **Note**
>
> **Isochronous mode**
>
> In isochronous mode you cannot set the On delay in the "Pulse width modulation PWM" and "PWM with DC motor" modes.

##### Off delay

This parameter is used to specify the delay with which a falling edge of the digital input DIO effects the digital output DQA.

The default setting is "0 μs".

##### Duty cycle

This parameter is used to specify the pulse-pause ratio (also referred to as pulse duty factor or duty factor) of the output signal in the selected output format.

The default setting is "50%".

##### Dithering

You can use this parameter to specify whether the PWM signal will be overlaid by a dither signal:

No dithering is enabled in the default setting.

##### Incline of dithering ramp up

You can use this parameter to specify the incline of the ramp up of the dithering amplitude for a theoretical increase of 0% to 100%.

The incline influences the effective ramp time.

Example of calculation of the effective ramp time in the case of a dithering amplitude of 10% and an incline of 2500 ms/100%:

10 % x 2500 ms/100 % = 250 ms

The default setting is "0".

##### Incline of dithering ramp down

You can use this parameter to specify the incline of the ramp down of the dithering amplitude for a theoretical drop from 100% to 0%.

The incline influences the effective ramp time:

Example of calculation of the effective ramp time in the case of a dithering amplitude of 10% and an incline of 2500 ms/100%:

10% x 2500 ms/100% = 250 ms

The default setting is "0".

##### Dithering amplitude

You can use this parameter to specify the amplitude of the dither signal in relation to the period duration of the output signal.

The default setting is "5.0%".

##### Dithering period duration

This parameter is used to specify the period duration of the dither signal. The parameter can be set in a fixed grid depending on the period duration of the PWM signal.

The default setting is "50000 μs" (= 50 ms).

##### Dithering frequency

This value is calculated from the configured period duration of the dither signal.

The value cannot be changed (read only).

##### Current control

You can use this parameter to activate the PID algorithm for the control of the output current.

The parameter is disabled in the default setting.

> **Note**
>
> **High-speed output**
>
> You can use current control with the associated parameters only in "Pulse width modulation PWM" mode with deactivated "High-speed output (0.1 A)".

##### Enable proportional action

You can use this parameter to activate the proportional action of the PID algorithm.

The parameter is enabled in the default setting.

##### Enable integral action

You can use this parameter to activate the integral action of the PID algorithm.

The parameter is enabled in the default setting.

##### Enable derivative action

You can use this parameter to activate the derivative action of the PID algorithm.

The parameter is disabled in the default setting.

##### Reference value current

You use this parameter to specify the maximum current as reference value for the current setpoint. A value of 100% for OUTPUT_VALUE in the control interface corresponds to a current setpoint in the magnitude of the reference value of the current.

The recommended setting is the value of the load current that is measured when current control is deactivated and the duty cycle is 100%.

The default setting is "0 mA".

##### Dead band width

You can use this parameter to specify the deviation of the output current from the current setpoint, within which there is no readjustment. The deviation refers to a range above and below the current setpoint.

The default setting is "0 μA".

##### Manipulated value high limit

You specify the high control limit with this parameter. "27648" corresponds to 100% of the duty cycle. The value must be greater than the "Manipulated variable low limit".

The default setting is "27648".

##### Manipulated value low limit

You specify the low control limit with this parameter. "0" corresponds to 0% of the duty cycle. The value must be less than the "Manipulated variable high limit".

The default setting is "0".

##### Proportional gain

This parameter is used to define the gain factor for the proportional action of the PID algorithm.

The default setting is "2.0000".

##### Integration time

This parameter defines the time used by the integral action of the PID algorithm.

The default setting is "20.0000" s.

##### Derivative action time

This parameter defines the time used by the derivative action of the PID algorithm.

The default setting is "10.0000 s".

##### Delay time of derivative action

This parameter is used to specify the delay time of derivative action of the PID algorithm.

The default setting is "2.0000 s".

### Online & Diagnostics module (S7-1500)

This section contains information on the following topics:

- [Displaying and evaluating diagnostics (S7-1500)](#displaying-and-evaluating-diagnostics-s7-1500)

#### Displaying and evaluating diagnostics (S7-1500)

The online and diagnostics view enables hardware diagnostics. You can also

- Obtain information on the module (e.g., Firmware version and serial number)
- Execute a firmware update if required

##### Procedure

To open the display editor for the diagnostic functions, follow these steps:

1. Open the device configuration of the CPU or IM.
2. Select the device view.
3. Right-click on the module and select "Online & Diagnostics".
4. Select the required display in the diagnostics navigation.

##### Additional information

Additional information on the diagnostic alarms and possible remedies can be found in the module's device manual.

## Using TM PTO 4 (S7-1500)

This section contains information on the following topics:

- [Configuration and parameter assignment of technology module (S7-1500)](#configuration-and-parameter-assignment-of-technology-module-s7-1500-1)
- [Online & Diagnostics module (S7-1500)](#online-diagnostics-module-s7-1500-1)

### Configuration and parameter assignment of technology module (S7-1500)

This section contains information on the following topics:

- [Adding a technology module to hardware configuration (S7-1500)](#adding-a-technology-module-to-hardware-configuration-s7-1500-1)
- [Parameter setting (hardware configuration) Opening (S7-1500)](#parameter-setting-hardware-configuration-opening-s7-1500-1)
- [Channel configuration (S7-1500)](#channel-configuration-s7-1500-1)
- [Operating mode (S7-1500)](#operating-mode-s7-1500-1)
- [Diagnostic interrupts (S7-1500)](#diagnostic-interrupts-s7-1500)
- [Axis parameters (S7-1500)](#axis-parameters-s7-1500)
- [Hardware inputs/outputs (S7-1500)](#hardware-inputsoutputs-s7-1500)
- [Sign-of-life error (S7-1500)](#sign-of-life-error-s7-1500)

#### Adding a technology module to hardware configuration (S7-1500)

##### Requirements

- The project has been created.
- The CPU S7-1500 has been created.

##### Procedure

To add a technology module to the hardware configuration, proceed as follows:

1. Open the device configuration of the CPU or IM.
2. Select a module rack.
3. Select the technology module from the module catalog:  
   "Technology modules > Pulse output > TM PTO 4 > Article number"
4. Drag the technology module to the required slot in the module rack.

#### Parameter setting (hardware configuration) Opening (S7-1500)

##### Opening from the device view

Proceed as follows:

1. Open the device configuration of the CPU or IM.
2. Select the device view.
3. Click on the module.

#### Channel configuration (S7-1500)

##### Channel configuration

This parameter defines the number of channels used. The channels are assigned in ascending order.

You can select from the following options:

- 4 channels (default)
- 3 channels
- 2 channels
- 1 channel

#### Operating mode (S7-1500)

##### Signal type

Use this parameter to specify the type of the [PTO pulse output](Basic%20principles%20of%20pulse%20output%20%28S7-1500%29.md#pulse-train-output-pto-s7-1500).

| Option | Meaning |
| --- | --- |
| PTO (Pulse (P) and direction (D)) (default) | The channel outputs a pulse signal and a direction signal. |
| PTO (count up (A), count down (B)) | The channel outputs a forward signal and a backward signal. |
| PTO (A, B phase-shifted) | The channel outputs two phase-shifted signals with single evaluation (as with an incremental encoder). |
| PTO (A, B phase-shifted, quadruple) | The channel outputs two phase-shifted signals with quadruple evaluation (as with an incremental encoder). |

##### Signal interface

You can use this parameter to define which interface is used for the pulse output.

| Option | Meaning |
| --- | --- |
| 24 V, asymmetrical | The channel outputs 24 V signals at terminals DQm.0 and DQm.1. |
| RS422, symmetrical / TTL (5 V), asymmetrical (default) | The channel outputs either RS422 signals at the terminals P/A and D/B and the respectively inverted terminals or 5 V-TTL signals at the terminals P/A and D/B. |

##### Pulse pause on reversal of direction

This parameter is used to define the minimum time between a change in direction and the output of the first pulse in the new direction.

You can select from the following options:

- 0 ms (default)
- 1 ms
- 4 ms
- 10 ms

#### Diagnostic interrupts (S7-1500)

##### Enable diagnostic interrupts

You can use this parameter to specify whether a diagnostic interrupt is to be triggered when no supply voltage is available or in the event of an error at the digital outputs. The detected error is displayed for the affected channel using feedback bit Fault_Present and Sensor_Error.

> **Note**
>
> The hardware outputs of the channels 0 and 1 and channels 2 and 3 each have common diagnostics. Due to this, in the event of an error at an output, pulse output of each of the two pairs of channels is stopped. A short-circuit at an output can also trigger the diagnostic interrupt "Supply voltage missing".

These diagnostic interrupts are processed in an interrupt OB.

The parameter is disabled in the default setting.

#### Axis parameters (S7-1500)

> **Note**
>
> **Technology object for Motion Control**
>
> Make sure that the respective parameter value matches the value of the technology object used in the configuration.

##### Increments per revolution

You can use this parameter to specify the number of steps (also micro steps) which corresponds to one revolution of the drive.

The range of values is 1 to 1000000. The value influences the value range of the maximum speed and reference speed. The default setting is "200".

##### Reference speed

This parameter is used to define the speed at which the drive rotates with a speed setpoint of 100%. The range of values is 1.0 to 20000.0 rpm. The permitted value range for the speed setpoint is -200% to 200% of the reference speed.

The reference speed influences the value range of the maximum speed and increments per revolution. The default setting is "3000.0".

##### Maximum speed

You can use this parameter to define the maximum permitted speed for the application.

The following table shows the calculation of the value range of the maximum speed:

| Signal  interface | Value range of the maximum speed |  |  |  |
| --- | --- | --- | --- | --- |
| Low limit |  | High limit (the smaller of the two values applies) |  |  |
| Signal evaluation "Single" | Signal evaluation "Quadruple" | Signal evaluation "Single" | Signal evaluation "Quadruple" |  |
| 24 V, asymmetrical | 0.1 Hz * 60 / (increments per revolution) | 0.1 Hz * 60 *4 / (increments per revolution) | - 2 * reference speed - 200000 Hz * 60 / (increments per revolution) | - 2 * reference speed - 200000 Hz * 60 *4 / (increments per revolution) |
| TTL (5 V), asymmetrical |  |  |  |  |
| RS422, symmetrical | - 2 * reference speed - 1000000 Hz * 60 / (increments per revolution) | - 2 * reference speed - 1000000 Hz * 60 *4 / (increments per revolution) |  |  |

The default setting is "3000.0".

##### Bits in incr. process value (G1_XIST1)

This parameter specifies the number of bits for the coding of the fine resolution within the incremental position process value of G1_XIST1.

The value is always "0" for this module.

##### Quick stop time (OFF3)

You can use this parameter to define the time interval to perform a fast stop from maximum speed to standstill.

The range of values is 1 to 65535 ms. The default setting is "1000 ms".

##### Ramp stop time (OFF1)

You can use this parameter to define the time interval to perform a stop from maximum speed to standstill.

The range of values is 1 to 65535 ms. The default setting is "5000 ms".

#### Hardware inputs/outputs (S7-1500)

##### Use drive enable

You use this parameter to define whether a hardware digital output will be used for the enabling signal for the drive.

The parameter is disabled in the default setting.

##### Drive enable output

You use this parameter to specify which hardware digital output will be used to enable the drive.

You can select from the following options:

- DQ0 (default)
- DIQ2

##### Use DI0 as reference switch

You use this parameter to define whether the hardware digital output DI0 will be used for the reference switch signal for the drive. You can synchronize the actual position of the drive axis with the reference mark via the reference switch signal.

The parameter is disabled in the default setting.

##### Edge selection reference switch

This parameter is used to define the edge at DI0 that triggers detection of the reference mark.

You can select from the following options:

- At rising edge (default)
- At falling edge

> **Note**
>
> The parameter is only active if you use the reference switch input.

This parameter is only available for selection and effective if "Use drive enable" is enabled.

##### Use DI1 as measuring input

You use this parameter to define whether the hardware digital output DI1 will be used for the measuring input signal for the drive. You can save the current position of the drive axis using the measuring input signal.

The parameter is disabled in the default setting.

##### Use "Drive ready"

You use this parameter to specify whether the ready signal of the drive is used at a hardware digital input.

The parameter is disabled in the default setting.

##### "Drive ready" input

You use this parameter to specify at which hardware digital input the ready signal of the drive is connected and read in.

You can select from the following options:

- DI0 (default)
- DI1
- DIQ2

> **Note**
>
> This parameter is only available for selection and effective if "Use "Drive ready"" is enabled.

##### Input delay

You use this parameter to suppress signal interference at the digital inputs. Changes to the signal are only detected if they remain stable for longer than the configured input delay time.

You can select from the following options:

- None  
  (input delay of 4 μs, minimum pulse width of 3 μs)
- 0.05 ms
- 0.1 ms (default)
- 0.4 ms
- 0.8 ms
- 1.6 ms
- 3.2 ms
- 12.8 ms
- 20 ms

> **Note**
>
> If you select the "None" or "0.05 ms" option, you have to use shielded cables for connection of the digital inputs.

#### Sign-of-life error  (S7-1500)

##### Tolerated number of sign-of-life errors

This parameter is used to define how many Master Sign-Of-Life errors are tolerated by the module. If the number is exceeded, an error message is triggered via the return bit Sensor_Error.

The range of values is 1 to 65535. The value 65535 indicates that no monitoring for sign-of-life errors is performed. The default setting is "1".

### Online & Diagnostics module (S7-1500)

This section contains information on the following topics:

- [Displaying and evaluating diagnostics (S7-1500)](#displaying-and-evaluating-diagnostics-s7-1500-1)

#### Displaying and evaluating diagnostics (S7-1500)

The online and diagnostics view enables hardware diagnostics. You can also

- Obtain information on the module (e.g., Firmware version and serial number)
- Execute a firmware update if required

##### Procedure

To open the display editor for the diagnostic functions, follow these steps:

1. Open the device configuration of the CPU or IM.
2. Select the device view.
3. Right-click on the module and select "Online & Diagnostics".
4. Select the required display in the diagnostics navigation.

##### Additional information

Additional information on the diagnostic alarms and possible remedies can be found in the module's device manual.

## Using TM PTO 2x24V (S7-1500)

This section contains information on the following topics:

- [Configuration and parameter assignment of technology module (S7-1500)](#configuration-and-parameter-assignment-of-technology-module-s7-1500-2)
- [Online & diagnostics module (S7-1500)](#online-diagnostics-module-s7-1500-2)

### Configuration and parameter assignment of technology module (S7-1500)

This section contains information on the following topics:

- [Adding a technology module to hardware configuration (S7-1500)](#adding-a-technology-module-to-hardware-configuration-s7-1500-2)
- [Parameter setting (hardware configuration) Opening (S7-1500)](#parameter-setting-hardware-configuration-opening-s7-1500-2)
- [Operating mode (S7-1500)](#operating-mode-s7-1500-2)
- [Diagnostic interrupts (S7-1500)](#diagnostic-interrupts-s7-1500-1)
- [Axis parameters (S7-1500)](#axis-parameters-s7-1500-1)
- [Hardware inputs/outputs (S7-1500)](#hardware-inputsoutputs-s7-1500-1)
- [Sign-of-life error (S7-1500)](#sign-of-life-error-s7-1500-1)

#### Adding a technology module to hardware configuration (S7-1500)

##### Requirements

- The project has been created.
- The CPU S7-1500 has been created.

##### Procedure

To add a technology module to the hardware configuration, proceed as follows:

1. Open the device configuration of the CPU or IM.
2. Select a module rack.
3. Select the technology module from the module catalog:  
   "Technological modules > Pulse output > TM PTO 2x24V > Article number"
4. Drag-and-drop the technology module to the required slot in the module rack.

#### Parameter setting (hardware configuration) Opening (S7-1500)

##### Opening from the device view

Proceed as follows:

1. Open the device configuration of the CPU or IM.
2. Select the device view.
3. Click on the module.

#### Operating mode (S7-1500)

##### Signal type

Use this parameter to specify the type of the [PTO pulse output](Basic%20principles%20of%20pulse%20output%20%28S7-1500%29.md#pulse-train-output-pto-s7-1500).

| Option | Meaning |
| --- | --- |
| PTO (Pulse (P) and direction (D)) (default) | The channel outputs a pulse signal and a direction signal. |
| PTO (count up (A), count down (B)) | The channel outputs a forward signal and a backward signal. |
| PTO (A, B phase-shifted) | The channel outputs two phase-shifted signals with single evaluation (as with an incremental encoder). |
| PTO (A, B phase-shifted, quadruple) | The channel outputs two phase-shifted signals with quadruple evaluation (as with an incremental encoder). |

##### Pulse pause on reversal of direction

This parameter is used to define the minimum time between a change in direction and the output of the first pulse in the new direction.

You can select from the following options:

- 0 ms (default)
- 1 ms
- 4 ms
- 10 ms

#### Diagnostic interrupts (S7-1500)

##### Enable diagnostic interrupts

You can use this parameter to specify whether a diagnostic interrupt is to be triggered when no supply voltage is available or in the event of an error at the digital outputs.

Missing supply voltage is also displayed for the respective channel with the feedback bit Parking_Sensor_Active. An error at the digital outputs is also displayed for the respective channel with the feedback bits Fault_Present and Sensor_Error.

> **Note**
>
> The hardware outputs of both channels have common diagnostics. As a result, when there is an error at one digital output, errors are automatically signaled for both channels. The pulse output of both channels is stopped in this case, regardless of whether "Enable diagnostic interrupts" is activated.

These diagnostic interrupts are processed in an interrupt OB.

The parameter is disabled in the default setting.

#### Axis parameters (S7-1500)

> **Note**
>
> **Technology object for Motion Control**
>
> Make sure that the respective parameter value matches the value of the technology object used in the configuration.

##### Increments per revolution

You can use this parameter to specify the number of steps (also micro steps) which corresponds to one revolution of the drive.

The range of values is 1 to 1000000. The value influences the value range of the maximum speed and reference speed. The default setting is "200".

##### Reference speed

This parameter is used to define the speed at which the drive rotates with a speed setpoint of 100%. The range of values is 1.0 to 20000.0 rpm. The permitted value range for the speed setpoint is -200% to 200% of the reference speed.

The reference speed influences the value range of the maximum speed and increments per revolution. The default setting is "3000.0".

##### Maximum speed

You can use this parameter to define the maximum permitted speed for the application.

The following table shows the calculation of the value range of the maximum speed:

| Value range of the maximum speed |  |  |  |
| --- | --- | --- | --- |
| Low limit |  | High limit (the smaller of the two values applies) |  |
| Signal evaluation "Single" | Signal evaluation "Quadruple" | Signal evaluation "Single" | Signal evaluation "Quadruple" |
| 0.1 Hz * 60 / (increments per revolution) | 0.1 Hz * 60 *4 / (increments per revolution) | - 2 * reference speed - 200000 Hz * 60 / (increments per revolution) | - 2 * reference speed - 200000 Hz * 60 *4 / (increments per revolution) |

The default setting is "3000.0".

##### Bits in incr. process value (G1_XIST1)

This parameter specifies the number of bits for the coding of the fine resolution within the incremental position process value of G1_XIST1.

The value is always "0" for this module.

##### Quick stop time (OFF3)

You can use this parameter to define the time interval to perform a fast stop from maximum speed to standstill.

The range of values is 1 to 65535 ms. The default setting is "1000 ms".

##### Ramp stop time (OFF1)

You can use this parameter to define the time interval to perform a stop from maximum speed to standstill.

The range of values is 1 to 65535 ms. The default setting is "5000 ms".

#### Hardware inputs/outputs (S7-1500)

##### Use ED as Enable Drive

You use this parameter to define whether the enabling signal for the drive is used at the digital output CHn.ED.

The parameter is disabled in the default setting.

##### Use RS as reference switch

You use this parameter to define whether the reference switch signal for the drive is used at the digital input CHn.RS. You can synchronize the actual position of the drive axis with the reference mark via the reference switch signal.

The parameter is disabled in the default setting.

##### Edge selection reference switch

This parameter is used to define the edge at CHn.RS that triggers detection of the reference mark.

You can select from the following options:

- At rising edge (default)
- At falling edge

> **Note**
>
> The parameter is only active if you use the reference switch input.

This parameter is only available for selection and effective if "Use ED as Enable Drive" is enabled.

##### Use MI as measuring input

You use this parameter to define whether the measuring input signal for the drive is used at the digital input CHn.MI. You can save the current position of the drive axis using the measuring input signal.

The parameter is disabled in the default setting.

##### Use DR as Drive Ready

You use this parameter to define whether the ready signal of the drive is used at the digital input CHn.DR.

The parameter is disabled in the default setting.

##### Input delay

You use this parameter to suppress signal interference at the digital inputs. Changes to the signal are only detected if they remain stable for longer than the configured input delay time.

You can select from the following options:

- None  
  (input delay of 4 μs, minimum pulse width of 3 μs)
- 0.05 ms
- 0.1 ms (default)
- 0.4 ms
- 0.8 ms
- 1.6 ms
- 3.2 ms
- 12.8 ms
- 20 ms

> **Note**
>
> If you select the "None" or "0.05 ms" option, you have to use shielded cables for connection of the digital inputs.

#### Sign-of-life error  (S7-1500)

##### Tolerated number of sign-of-life errors

This parameter is used to define how many Master Sign-Of-Life errors are tolerated by the module. If the number is exceeded, an error message is triggered via the return bit Sensor_Error.

The range of values is 1 to 65535. The value 65535 indicates that no monitoring for sign-of-life errors is performed. The default setting is "1".

### Online & diagnostics module (S7-1500)

This section contains information on the following topics:

- [Displaying and evaluating diagnostics (S7-1500)](#displaying-and-evaluating-diagnostics-s7-1500-2)

#### Displaying and evaluating diagnostics (S7-1500)

The online and diagnostics view enables hardware diagnostics. You can also

- Obtain information on the module (e.g., Firmware version and serial number)
- Execute a firmware update if required

##### Procedure

To open the display editor for the diagnostic functions, follow these steps:

1. Open the device configuration of the CPU or IM.
2. Select the device view.
3. Right-click on the module and select "Online & Diagnostics".
4. Select the required display in the diagnostics navigation.

##### Additional information

Additional information on the diagnostic alarms and possible remedies can be found in the module's device manual.

## Using Compact CPU (S7-1500)

This section contains information on the following topics:

- [Configuring and assigning parameters for Compact CPU (S7-1500)](#configuring-and-assigning-parameters-for-compact-cpu-s7-1500)
- [Online & Diagnostics module (S7-1500)](#online-diagnostics-module-s7-1500-3)

### Configuring and assigning parameters for Compact CPU (S7-1500)

This section contains information on the following topics:

- [Adding Compact CPU to the hardware configuration (S7-1500)](#adding-compact-cpu-to-the-hardware-configuration-s7-1500)
- [Compatibility 1511C (pulse generators of the Compact CPU 1512C-1 PN) (S7-1500)](#compatibility-1511c-pulse-generators-of-the-compact-cpu-1512c-1-pn-s7-1500)
- [Operating mode (S7-1500)](#operating-mode-s7-1500-3)
- [Reaction to CPU STOP (S7-1500)](#reaction-to-cpu-stop-s7-1500-1)
- [Diagnostic interrupts (S7-1500)](#diagnostic-interrupts-s7-1500-2)
- [Hardware inputs/outputs (PWN, frequency output) (S7-1500)](#hardware-inputsoutputs-pwn-frequency-output-s7-1500)
- [Hardware inputs/outputs (PTO) (S7-1500)](#hardware-inputsoutputs-pto-s7-1500)
- [Parameter (PWN, frequency output) (S7-1500)](#parameter-pwn-frequency-output-s7-1500)
- [Axis parameters (PTO) (S7-1500)](#axis-parameters-pto-s7-1500)

#### Adding Compact CPU to the hardware configuration (S7-1500)

##### Requirements

The project has been created.

##### Procedure

To add a compact CPU to the hardware configuration, proceed as follows:

1. Double-click "Add new device".   
   The "Add new device" dialog opens.
2. Select Controller".
3. Select the Compact CPU:  
   "SIMATIC S7‑1500 > CPU > Name of Compact CPU > Article number"
4. Confirm with "OK".

##### Result

The new Compact CPU is displayed with the following objects in the project tree. Double-click to open the required editor.

![Result](images/88462310027_DV_resource.Stream@PNG-en-US.png)

|  | Object | Description |
| --- | --- | --- |
| ① | Device configuration | In the Inspector window (per PTO/PWM channel):  - [Setting the operating mode](#operating-mode-s7-1500-3) - [Setting the reaction to CPU STOP](#reaction-to-cpu-stop-s7-1500-1) - [Enable diagnostic interrupts](#diagnostic-interrupts-s7-1500-2) - [Setting parameters for PWM or frequency output](#parameter-pwn-frequency-output-s7-1500) - [Setting axis parameters for PTO modes](#axis-parameters-pto-s7-1500) - [Assign signals to inputs and outputs](#hardware-inputsoutputs-pwn-frequency-output-s7-1500) - Setting the module addresses |
| ② | [Online & Diagnostics](#displaying-and-evaluating-diagnostics-s7-1500-3) | - Hardware diagnostics - Obtain information about the Compact CPU - Run firmware update |

#### Compatibility 1511C (pulse generators of the Compact CPU 1512C-1 PN) (S7-1500)

**Front connector assignment same as CPU 1511C**

You can use this parameter to define if the pin assignment for the front connector of the CPU 1511C‑1 PN is to be used for the pulse generators of the CPU 1512C-1 PN:

| Option | Meaning |
| --- | --- |
| Disabled (default) | CPU 1512C‑1 PN uses the pin assignment of the onboard front connector. 1512C-1 PN supports the use of the connections of both front connectors of the digital onboard I/Os for the pulse generators. The assignment of hardware inputs and outputs for the PTO/PWM channels is described in the product manual of the CPU 1512C-1 PN. |
| Enabled | CPU 1512C‑1 PN uses the pin assignment of the front connector of the CPU 1511C‑1 PN. 1511C-1 PN supports the use of the connections of the first front connector of the digital onboard I/Os for the pulse generators. The assignment of hardware inputs and outputs for the PTO/PWM channels is described in the product manual of the CPU 1511C-1 PN. |

#### Operating mode (S7-1500)

##### Operating mode

You use this parameter to specify the function for which the pulse generator of the compact CPU is used. You can find possible settings that are dependent on the operation mode under:

[Reaction to CPU STOP](#reaction-to-cpu-stop-s7-1500-1)

[Diagnostic interrupts](#diagnostic-interrupts-s7-1500-2)

[Hardware inputs/outputs (PWN, frequency output)](#hardware-inputsoutputs-pwn-frequency-output-s7-1500) or [Hardware inputs/outputs (PTO)](#hardware-inputsoutputs-pto-s7-1500)

[Parameter (PWN, frequency output)](#parameter-pwn-frequency-output-s7-1500) or [Axis parameters (PTO)](#axis-parameters-pto-s7-1500)

| Operating mode | Meaning | Mode-dependent parameters |
| --- | --- | --- |
| Disabled (default) | The pulse generator is not activated. The channel does not output pulses. | — |
| Pulse width modulation PWM | The channel outputs a [pulse width modulated signal](Basic%20principles%20of%20pulse%20output%20%28S7-1500%29.md#operating-mode-pulse-width-modulation-pwm-s7-1500) with the configured minimum pulse duration and the configured period duration. The duty cycle and the period duration are defined in the control interface. | - Reaction to CPU STOP - Substitute value for pulse output (DQA) - No supply voltage L+ - Pulse output (DQA) - High-speed output (0.1 A) - Output format - Minimum pulse duration - Period duration |
| Frequency output | The channel outputs a [signal with a fixed duty cycle](Basic%20principles%20of%20pulse%20output%20%28S7-1500%29.md#operating-mode-frequency-output-s7-1500) of 50%. You specify the frequency in the control interface. | - Reaction to CPU STOP - Substitute value for pulse output (DQA) - No supply voltage L+ - Pulse output (DQA) - High-speed output (0.1 A) - Output format |
| PTO (Pulse (P) and direction (D)) | The channel outputs a [pulse signal and a direction signal](Basic%20principles%20of%20pulse%20output%20%28S7-1500%29.md#operating-mode-pto-s7-1500) for a Motion Control application. | - No supply voltage L+ - Increments per revolution - Reference speed - Maximum speed - Bits in incr. process value (G1_XIST1) - Quick stop time - Reference switch input - Edge selection reference switch - Measurement input - Input "Drive ready" - Pulse output (A) / Clock generator forward (A) / Clock generator output (A) - Direction output (B) / Clock generator backward (B) / Clock generator output (B) - Drive enable output |
| PTO (count up (A), count down (B)) | The channel outputs a [forward signal and a backward signal](Basic%20principles%20of%20pulse%20output%20%28S7-1500%29.md#operating-mode-pto-s7-1500) for a Motion Control application. |  |
| PTO (A, B phase-shifted) | The channel outputs [two phase-shifted signals with single evaluation](Basic%20principles%20of%20pulse%20output%20%28S7-1500%29.md#operating-mode-pto-s7-1500) for a Motion Control application. |  |
| PTO (A, B phase-shifted, quadruple) | The channel outputs [two phase-shifted signals with quadruple evaluation](Basic%20principles%20of%20pulse%20output%20%28S7-1500%29.md#operating-mode-pto-s7-1500) for a Motion Control application. |  |

#### Reaction to CPU STOP (S7-1500)

##### Reaction to CPU STOP

You use this parameter to specify the reaction of the channel to the failure of the controller.

| Reaction to CPU STOP | Meaning |
| --- | --- |
| Output substitute value (default) | The channel outputs the configured substitute value at its digital output (DQA) until the next CPU STOP-RUN transition.   The feedback bit STS_ENABLE is set to 0.  The channel is returned to its startup state after a STOP-RUN transition. Before you can start a new pulse output, you must first set the SW_ENABLE control bit to 0. |
| Continue operation | The channel continues to operate.  The digital output (DQA) continue to switch according to the parameter assignment and the last setpoint. |

##### Substitute value for pulse output (DQA)

This parameter lets you specify which value the channel is to output to the digital output DQA in the event of a CPU STOP under "Output substitute value".

The default setting is "0".

#### Diagnostic interrupts (S7-1500)

##### Missing supply voltage L+

You can use this parameter to specify whether a diagnostic interrupt is to be triggered when no supply voltage is available. These diagnostic interrupts are processed in an interrupt OB.

The parameter is disabled in the default setting.

#### Hardware inputs/outputs (PWN, frequency output) (S7-1500)

##### Pulse output (DQA)

You can use this parameter to define which hardware digital output is used for the pulse output.

##### High-speed output (0.1 A)

Use this parameter to specify whether or not the respective hardware digital output works as fast push-pull or as sourcing output.

| Option | Meaning |
| --- | --- |
| Enabled | The digital output operates as very fast push-pull switch with up to 100 kHz and is capable of bearing loads up to 0.1 A. A push-pull switch is alternately switched to DC 24 V and ground. This makes for very fast edges. |
| Disabled (default) | The digital output works as 24 vacuum circuit-breaker/current-sourcing output with reference to M (up to 10 kHz) and can carry a rated load current of 0.5 A. |

> **Note**
>
> The parameter is only effective if the hardware output selected as pulse output supports 100 kHz operation. The parameter is not available for hardware outputs that only support frequencies up to 100 Hz.

#### Hardware inputs/outputs (PTO) (S7-1500)

##### Input reference switch

You can use this parameter to define which hardware digital input is used as reference switch input.

The default setting is "None".

##### Edge selection reference switch

This parameter is used to define the edge at the reference switch input that triggers detection of the reference mark.

The default setting is "Positive edge".

> **Note**
>
> The parameter is only active if you use a basic-position-switch input.

##### Measurement input

You can use this parameter to define which hardware digital input is used as measurement input.

The default setting is "None".

##### "Drive ready" input

You use this parameter to specify at which hardware digital input the ready signal of the drive is connected and read in.

The default setting is "None".

##### Pulse output (A) / Clock generator forward (A) / Clock generator output (A)

This parameter defines which hardware output is used for the PTO signal A. The value cannot be modified.

##### Direction output (B) / Clock generator backward (B) / Clock generator output (B)

This parameter defines which hardware output is used for the PTO signal B. You can change the value only in operating mode "PTO (pulse (A) and direction (B))".

##### Drive enable output

You use these parameters to specify which hardware output will be used to enable the drive.

The default setting is "None".

#### Parameter (PWN, frequency output) (S7-1500)

##### Output format

**"Pulse width modulation PWM" operating mode:**

Use this parameter to specify the format or the value range with which the duty cycle is evaluated:

| Output format | Value range |
| --- | --- |
| S7 analog output | 0 ... 27648  ("27648" corresponds to 100% of the reference value) |
| 1/100 (default) | 0 ... 100 |
| 1/1000 | 0 ... 1000 |
| 1/10000 | 0 ... 10000 |

**"Frequency output" operating mode:**

"1 Hz" is selected as output format and cannot be changed.

##### Minimum pulse duration

This parameter is used to specify the minimum permitted pulse duration for the PWM signal.

Pulses and pauses which fall below the value are suppressed.

The default setting is "0 μs".

##### Period duration

This parameter is used to specify the period duration of the output signal.

The default setting is "2000000 μs". This corresponds to 2 s.

#### Axis parameters (PTO) (S7-1500)

##### Increments per revolution

You can use this parameter to specify the number of steps (also micro steps) which corresponds to one revolution of the drive.

The default setting is "200".

> **Note**
>
> **Technology object for Motion Control**
>
> Make sure that the parameter value matches the value of the technology object used in the configuration.

##### Reference speed

You can use this parameter to define the speed to which the speed setpoint is to refer.

The permitted value range for the speed setpoint is -200% to 200% of the reference speed.

The default setting is "3000.0".

> **Note**
>
> **Technology object for Motion Control**
>
> Make sure that the parameter value matches the value of the technology object used in the configuration.

##### Maximum speed

You can use this parameter to define the maximum permitted speed for the application.

The default setting is "3000.0".

> **Note**
>
> **Technology object for Motion Control**
>
> Make sure that the parameter value matches the value of the technology object used in the configuration.

##### Bits in incr. process value (G1_XIST1)

This parameter specifies the number of bits for the coding of the fine resolution within the incremental process value of G1_XIST1.

> **Note**
>
> **Technology object for Motion Control**
>
> Make sure that the parameter value matches the value of the technology object used in the configuration.

##### Time OFF3

You can use this parameter to define the time interval to perform a fast stop from maximum speed to standstill.

The default setting is "1000 ms".

### Online & Diagnostics module (S7-1500)

This section contains information on the following topics:

- [Displaying and evaluating diagnostics (S7-1500)](#displaying-and-evaluating-diagnostics-s7-1500-3)

#### Displaying and evaluating diagnostics (S7-1500)

The online and diagnostics view enables hardware diagnostics. You can also

- Obtain information on the compact CPU (e.g. Firmware version and serial number)
- Execute a firmware update if required

##### Procedure

To open the display editor for the diagnostic functions, follow these steps:

1. Open the Compact CPU folder in the project tree.
2. Double-click on the "Online & diagnostics" object.
3. Select the required display in the diagnostics navigation.

##### Additional information

Additional information on the diagnostic alarms and possible remedies can be found in the compact CPU device manual.

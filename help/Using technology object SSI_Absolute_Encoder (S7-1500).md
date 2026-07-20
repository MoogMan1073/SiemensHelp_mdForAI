---
title: "Using technology object SSI_Absolute_Encoder (S7-1500)"
package: TFTOSSIenUS
topics: 19
devices: [S7-1500, S7-1500T]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Using technology object SSI_Absolute_Encoder (S7-1500)

This section contains information on the following topics:

- [Technology object SSI_Absolute_Encoder (S7-1500)](#technology-object-ssi_absolute_encoder-s7-1500)
- [Overview of the configuration steps (S7-1500)](#overview-of-the-configuration-steps-s7-1500)
- [Add technology object (S7-1500)](#add-technology-object-s7-1500)
- [Configuring SSI_Absolute_Encoder (S7-1500)](#configuring-ssi_absolute_encoder-s7-1500)
- [SSI_Absolute_Encoder programming (S7-1500)](#ssi_absolute_encoder-programming-s7-1500)
- [Commissioning SSI_Absolute_Encoder (S7-1500)](#commissioning-ssi_absolute_encoder-s7-1500)
- [SSI_Absolute_Encoder diagnostics (S7-1500)](#ssi_absolute_encoder-diagnostics-s7-1500)

## Technology object SSI_Absolute_Encoder (S7-1500)

STEP 7 (TIA Portal) supports you in the configuration, commissioning and diagnostics of counting and measuring functions for the TM PosInput technology module with the "Technology objects" function in combination with the SSI absolute encoders:

- In STEP 7 (TIA Portal) you configure the SSI_Absolute_Encoder technology object by entering the encoder parameters.
- The corresponding SSI_Absolute_Encoder instruction is programmed in the user program. This instruction supplies the control and feedback interface of the technology module.

The SSI_Absolute_Encoder technology object corresponds to the instance DB of the SSI_Absolute_Encoder instruction. The configuration of the position input and measuring functions is saved in the technology object. The technology object is located in the folder "PLC > Technology objects".

The SSI_Absolute_Encoder technology object can be used equally for the TM PosInput of the S7-1500, ET 200SP and ET 200eco PN M12-L systems.

### Operating mode

In order to assign the technology module parameters using a TM PosInput, you specify the [operating mode](Using%20the%20module%20%28S7-1500%29.md#operating-mode-s7-1500) "Operation with technology objects for "counting and measurement"" in the hardware configuration of the TM PosInput. This selection is already preset.

## Overview of the configuration steps (S7-1500)

### Introduction

The overview below shows the basic procedure for configuring the position input and measuring functions of the technology module with the SSI_Absolute_Encoder technology object.

### Requirement

Before you can use the technology object, a project with an S7-1500 CPU or an ET 200SP CPU must be created in STEP 7 (TIA Portal).

### Procedure

Proceed in the recommended sequence outlined below:

| Step | Description |
| --- | --- |
| 1 | [Configure a technology module](Using%20the%20module%20%28S7-1500%29.md#adding-a-technology-module-for-hardware-configuration-tm-count-and-tm-posinput-s7-1500) |
| 2 | [Add technology object](#add-technology-object-s7-1500) |
| 3 | [Configure a technology object according to your application](#working-with-the-configuration-dialog-s7-1500) |
| 4 | [Call instruction in the user program](#call-instruction-in-the-user-program-s7-1500) |
| 5 | Load to CPU |
| 6 | [Commissioning the technology object](#commissioning-the-technology-object-s7-1500) |
| 7 | [Diagnostics of the technology object](#monitoring-counter-values-measured-values-dis-and-dqs-s7-1500) |

## Add technology object (S7-1500)

### Adding a technology object in the project navigation

When a technology object is added, an instance DB is created for the instruction of this technology object. The configuration of the technology object is stored in this instance DB.

### Requirement

A project with a CPU S7‑1500 has been created.

### Procedure

To add a technology object, proceed as follows:

1. Open the CPU folder in the project tree.
2. Open the "Technology objects" folder.
3. Double-click on "Add new object".  
   The "Add new object" dialog opens.
4. Select the technology "Counting, measurement, cams".
5. Select the "SSI_Absolute_Encoder" object.
6. Enter an individual name for the technology object in the "Name" text box.
7. Click "Additional information" if you want to add your own information to the technology object.
8. Confirm with "OK".

### Result

The new technology object has now been created and stored in the project tree in the "Technology objects" folder.

![Result](images/85223774731_DV_resource.Stream@PNG-en-US.PNG)

|  | Object | Description |
| --- | --- | --- |
| ① | [Configuration](#working-with-the-configuration-dialog-s7-1500) | In the configuration dialog:  - Assignment of technology module and channel - Technology object parameter settings for position input and measurement functions   When you change the configuration of the technology object, you must download the technology object **and** the hardware configuration to the CPU. |
| ② | [Commissioning](#commissioning-the-technology-object-s7-1500) | Commissioning and function test of the technology object:  Simulating parameters of the SSI_Absolute_Encoder instruction and monitoring the effects |
| ③ | [Diagnostics](#monitoring-counter-values-measured-values-dis-and-dqs-s7-1500) | Monitoring of the position input and measurement functions |

## Configuring SSI_Absolute_Encoder (S7-1500)

This section contains information on the following topics:

- [Working with the configuration dialog (S7-1500)](#working-with-the-configuration-dialog-s7-1500)
- [Basic parameters (S7-1500)](#basic-parameters-s7-1500)
- [SSI absolute encoder (S7-1500)](#ssi-absolute-encoder-s7-1500)
- [Behavior of a DI (SSI_Absolute_Encoder) (S7-1500)](#behavior-of-a-di-ssi_absolute_encoder-s7-1500)
- [Behavior of a DQ (SSI_Absolute_Encoder) (S7-1500)](#behavior-of-a-dq-ssi_absolute_encoder-s7-1500)
- [Specify measured value (SSI_Absolute_Encoder) (S7-1500)](#specify-measured-value-ssi_absolute_encoder-s7-1500)
- [Examples of the frame format (S7-1500)](#examples-of-the-frame-format-s7-1500)

### Working with the configuration dialog (S7-1500)

You configure the properties of the technology object in the configuration window. Proceed as follows to open the configuration window of the technology object:

1. Open the "Technology objects" folder in the project tree.
2. Open the technology object in the project tree.
3. Double-click on the "Configuration" object.

The configuration is divided into the following categories:

- **Basic parameters**

  The basic parameters include the selection of the technology module and the number of the channel for which the technology object is configured.
- **Extended parameters**

  The extended parameters include the parameters for adapting the position input and measuring functions and for setting the characteristics of the digital inputs and digital outputs.

#### Configuration window icons

Icons in the area navigation of the configuration show additional details about the status of the configuration:

| Symbol | Meaning |
| --- | --- |
| ![Configuration window icons](images/41244027019_DV_resource.Stream@PNG-de-DE.png) | **The configuration contains default values and is complete**.  The configuration contains only default values. With these default values, you can use the technology object without additional changes. |
| ![Configuration window icons](images/41244015115_DV_resource.Stream@PNG-de-DE.png) | **The configuration contains values set by the user or automatically adapted values and is complete**   All text boxes of the configuration contain valid values and at least one default value was changed. |
| ![Configuration window icons](images/41243964811_DV_resource.Stream@PNG-de-DE.png) | **The configuration is incomplete or incorrect**   At least one text box or drop-down list contains an invalid value. The corresponding field or the drop-down list is displayed on a red background. Click the roll-out error message to indicate the cause of error. |

### Basic parameters (S7-1500)

Under "Basic parameters", you can establish the connection between the technology object and the TM PosInput technology module.

#### Module

You select the technology module in a subsequent dialog box. All TM PosInput technology modules (central or distributed) that are configured for use with a "Counting and measurement" technology object under the S7-1500 CPU or ET 200SP CPU are available for selection.

After selecting the technology module, you can open the device configuration associated with the technology module by clicking the"Device configuration" button.

The technology module parameter settings required for the use of the technology object are made in the "Extended parameters" of the technology object.

#### Channel

For a technology module with several channels, you select the number of the channel for which the technology object is valid.

> **Note**
>
> A channel can be assigned to only one technology object. A channel that is already assigned to a technology object can no longer be selected.

#### Synchronization of the parameter values

If, after assignment of the channel to the technology object, there is an inconsistency between the parameter values in the property dialog of the TM PosInput module and in the technology object, a button with a corresponding inquiry appears. When you click the button, the parameter values in the property dialog of the assigned module are overwritten by the parameter values of the technology object within STEP 7 (TIA Portal). The current parameter values of the technology object are displayed in the property dialog of the module (read-only).

> **Note**
>
> If you change parameter values of the technology object, the corresponding parameter values are also overwritten without prompt in the properties dialog of the hardware configuration. As after every change in hardware configuration, the next time the project is loaded in the CPU, a prompt appears asking whether the CPU should go to STOP mode.

### SSI absolute encoder (S7-1500)

#### Frame length

With the parameter assignment of the frame length, you specify the number of bits of an SSI frame of the [SSI absolute encoder](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#position-input-with-ssi-absolute-encoder-s7-1500) used. You can find the frame length of your SSI absolute encoder in the data sheet of the encoder. Special bits are also included in the frame length. A parity bit does not count in the frame length.

A frame length of between 10 bits and 40 bits is permitted. The default setting is "13 Bit".

You can find two examples of the SSI frame format at [Examples of the frame format](#examples-of-the-frame-format-s7-1500).

#### Code type

You use the parameter assignment of the code type to specify whether the encoder supplies Dual code or Gray code.

You can select from the following options:

| Code type | Meaning |
| --- | --- |
| Gray (default) | The gray-coded position value returned by the SSI absolute encoder is converted to dual code. |
| Dual | The value returned by the SSI absolute encoder is not converted. |

#### Transmission rate

With the parameter assignment of the transmission rate, you specify the data transmission rate between the technology module and the SSI absolute encoder.

You can select from the following options:

- 125 kHz (preset)
- 250 kHz
- 500 kHz
- 1 MHz
- 1.5 MHz
- 2 MHz

The maximum transmission rate depends on the cable length and the technical specifications of the SSI absolute encoder. For additional information, refer to the product manual of the TM PosInput and the encoder description.

#### Monoflop time

With the parameter assignment of the monoflop time, you specify the idle time between two SSI frames.

The configured monoflop time must be at least equal to the monoflop time of the SSI absolute encoder used. You can find this value in the technical specifications of the SSI absolute encoder.

You can select from the following options:

- Automatically (default)
- 16 µs
- 32 µs
- 48 µs
- 64 µs

> **Note**
>
> If you select the "Automatic" option, the monoflop time automatically adapts to the encoder used.
>
> In isochronous mode, the "Automatic" option corresponds to a monoflop time of 64 µs. If the monoflop time of the employed SSI absolute value encoder is less than 64 µs, you can select the value of the encoder to achieve faster isochronous times.

#### Parity

With the parameter assignment of the parity, you specify whether the SSI absolute encoder transfers a parity bit.

If, for example, a 25-bit encoder with parity is assigned, the technology module reads 26 bits. A parity error is indicated by the technology object at the ErrorID output parameter with the [value 80A2](SSI_Absolute_Encoder%20%28S7-1500%29.md#error-codes-of-parameter-errorid-s7-1500).

#### Bit number LSB of the position value

This parameter is used to specify the bit number of the LSB (least significant bit) of the position value in the frame of the SSI absolute encoder. In this way you limit the range in the frame that supplies the position value.

The value must be less than the bit number of the MSB of the position value. The difference between the bit numbers of the MSB and the LSB of the position value must be less than 32.

The default setting is "0".

> **Note**
>
> If you have selected the Code type "Gray", only the range from the LSB to the MSB of the position value is converted to binary code.

#### Bit number MSB of the position value

This parameter is used to specify the bit number of the MSB (most significant bit) of the position value in the frame of the SSI absolute encoder. In this way you limit the range in the frame that supplies the position value.

The value must be less than the frame length and higher than the bit number of the LSB of the position value. The difference between the bit numbers of the MSB and the LSB of the position value must be less than 32.

The default setting is "12".

> **Note**
>
> If you have selected the Code type "Gray", only the range from the LSB to the MSB of the position value is converted to binary code.

#### Invert direction

You can use this parameter to invert the values supplied by the SSIabsolute encoder. This allows you to adapt the detected direction of the encoder to the motor's direction of rotation.

> **Note**
>
> This parameter acts only on the range from the LSB to the MSB of the position value in the frame.

#### SSI frame

You can also set the following parameters in the graphic with drag-and-drop:

- Frame length
- Bit number LSB of the position value
- Bit number MSB of the position value

**Complete SSI frame**

If "Complete SSI frame" has been selected as the measured variable, the module returns the least significant 32 bits of the unprocessed current SSI frame as the measured value. The graphic shows the corresponding meaning of a supplied bit. The following abbreviations are used:

| Symbol | Meaning |
| --- | --- |
| V | Value: Position value as gray or dual code |
| S | Special: Special bit |
| P | Parity: Parity bit  When you have configured a parity bit, the module returns the least significant 31 bits of the SSI frame and the parity bit. |

### Behavior of a DI (SSI_Absolute_Encoder) (S7-1500)

#### Setting function of the DI

By configuring a digital input, you specify which functions the digital input triggers at switching.

You can select from the following options:

| Function of a digital input | Meaning | Additional option-specific parameters |
| --- | --- | --- |
| [Capture](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#capture-with-ssi-absolute-encoder-s7-1500) | The configured edge at the respective digital input saves the current position value as a Capture value. The technology object displays the Capture value at the output parameter CapturedValue.  The function can only be used for one of the two digital inputs. | - Input delay - Edge selection - Frequency of the Capture function |
| Digital input without function | No technological function is assigned to the respective digital input.   You can read the signal state of the digital input via the respective static variable of the technology object:  - UserStatusFlags.StatusDI0 - UserStatusFlags.StatusDI1 | - Input delay |

> **Note**
>
> You can choose the "Capture" function only in operating mode "Use position value (SSI absolute value) as reference".

#### Input delay

By configuring the input delay, you suppress interferences at the digital inputs. Signals with a pulse duration below the configured input delay are suppressed.

You can select from the following input delays:

- None
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

> **Note**
>
> You configure the input delay under "Behavior of DI0" for all digital inputs together. The input delay is also displayed under "Behavior of DI1".

#### Edge selection

You can use this parameter to specify the edge of the digital input at which the configured function is triggered for the "Capture" function.

You can select from the following options:

- At rising edge (default)
- At falling edge
- At rising and falling edge

#### Frequency of the Capture function

This parameter is used to define the frequency of [Capture events](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#capture-with-ssi-absolute-encoder-s7-1500):

You can select from the following options:

| Option | Meaning |
| --- | --- |
| Once | The first configured edge at the respective digital input saves the current counter value as Capture value. |
| Periodic (default) | Each configured edge at the respective digital input saves the current counter value as a Capture value. |

> **Note**
>
> This parameter is available for SSI_Absolute_Encoder as of V3.0.

### Behavior of a DQ (SSI_Absolute_Encoder) (S7-1500)

#### Operating mode

With the operating mode, you specify the reference value with which the comparison functions work.

| Operating mode | Meaning |
| --- | --- |
| Use position value (SSI absolute value) as reference (default) | The comparison functions and hardware interrupts for compare events work with the position value. |
| Use measured value as reference | The comparison functions and hardware interrupts for compare events work with the measured value. |

> **Note**
>
> You configure the operating mode under "Behavior of DQ0" for both digital outputs together. The operating mode is also displayed under "Behavior of DQ1".

#### Set output

With the parameter assignment of a digital output, you specify the condition upon which the digital output switches.

You can select from the following options depending on the operating mode:

| [Function of a digital output](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#switching-at-comparison-values-with-position-value-ssi-absolute-value-as-reference-s7-1500) in operating mode "Use position value (SSI absolute value) as reference" | Meaning | Additional option-specific parameters |
| --- | --- | --- |
| Between comparison value and high limit (default) | The respective digital output is active if: Comparison value <= position value <= maximum position value | - Comparison value 0 - Comparison value 1 - Hysteresis (in increments) |
| Between comparison value and low limit | The respective digital output is active if: Minimum position value <= Position value <= Comparison value | - Comparison value 0 - Comparison value 1 - Hysteresis (in increments) |
| Between comparison value 0 and 1 | The digital output DQ1 is active if: Comparison value 0 <= position value <= comparison value 1 | - Comparison value 0 - Comparison value 1 - Hysteresis (in increments) |
| At comparison value for a pulse duration | The respective digital output is active once for the assigned time and direction of the position value change when the position value is equal to the comparison value or has fallen below or exceeded it. | - Comparison value 0 - Comparison value 1 - Count direction - Pulse duration - Hysteresis (in increments) |
| After set command from CPU until comparison value | When a set command is sent from the CPU, the respective digital output is active for the assigned direction of the position value change until the position value is equal to the comparison value or has fallen below or exceeded it. | - Comparison value 0 - Comparison value 1 - Count direction - Hysteresis (in increments) |
| Use by user program | The respective digital output can be switched by the CPU [via the control interface](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#comparison-values-and-outputs-s7-1500). | — |

> **Note**
>
> You can only select the "Between comparison value 0 and 1" function for digital output DQ1 and only if you have selected the "Use by user program" function for digital output DQ0.

| [Function of a digital output](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#switching-at-comparison-values-with-measured-value-as-reference-s7-1500) in operating mode "Use measured value as reference" | Meaning | Additional option-specific parameters |
| --- | --- | --- |
| Measured value >= comparison value (default) | The respective digital output is active if the measured value is greater than or equal to the comparison value. | - Comparison value 0 - Comparison value 1 |
| Measured value <= comparison value | The respective digital output is active if the measured value is less than or equal to the comparison value. | - Comparison value 0 - Comparison value 1 |
| Between comparison value 0 and 1 | The digital output DQ1 is active if: Comparison value 0 <= measured value <= comparison value 1 | - Comparison value 0 - Comparison value 1 |
| Not between comparison value 0 and 1 | The digital output DQ1 is active if: Comparison value 1 <= measured value <= comparison value 0 | - Comparison value 0 - Comparison value 1 |
| Use by user program | The respective digital output can be switched by the CPU [via the control interface](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#comparison-values-and-outputs-s7-1500). | — |

> **Note**
>
> You can select the "Between comparison value 0 and 1" and "Not between comparison value 0 and 1" functions only for digital output DQ1 and only if you have selected the "Use by user program" function for digital output DQ0.

#### Comparison value 0

**Operating mode "**
**Use position value (SSI absolute value) as reference**
**"**

With the parameter assignment of the [comparison value](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#switching-at-comparison-values-with-position-value-ssi-absolute-value-as-reference-s7-1500), you specify the position value at which the digital output DQ0 switches as a result of the selected comparison event.

If you use an SSI absolute encoder with a position value length of up to 31 bits, you must enter a positive integer (DINT) with a value between 0 and 2<sup>(MSB-LSB+1)</sup>-1. If you use an SSI absolute encoder with a position value length of 32 bits, you must enter a signed integer (DINT) with a value between –2147483648 and 2147483647.

If you use the DQ function "Between comparison value 0 and 1", the comparison value 0 has to be smaller than comparison value 1. The default setting is "0".

**Operating mode "**
**Use measured value as reference**
**"**

With the parameter assignment of the [comparison value](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#switching-at-comparison-values-with-measured-value-as-reference-s7-1500), you specify the measured value at which the digital output DQ0 switches as a result of the selected comparison event.

You must enter a floating point number (REAL). If you use the DQ function "Between comparison value 0 and 1", the comparison value 0 has to be smaller than comparison value 1. The minimum value is -7.922816 x 10<sup>28</sup>. The default setting is "0.0". The unit of the comparison value depends on the measured variable.

#### Comparison value 1

**Operating mode "**
**Use position value (SSI absolute value) as reference**
**"**

With the parameter assignment of the [comparison value](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#switching-at-comparison-values-with-position-value-ssi-absolute-value-as-reference-s7-1500), you specify the position value at which the digital output DQ1 switches as a result of the selected comparison event.

If you use an SSI absolute encoder with a position value length of up to 31 bits, you must enter a positive integer (DINT) with a value between 0 and 2<sup>(MSB-LSB+1)</sup>-1. If you use an SSI absolute encoder with a position value length of 32 bits, you must enter a signed integer (DINT) with a value between –2147483648 and 2147483647.

If you use the DQ function "Between comparison value 0 and 1", the comparison value 0 has to be smaller than comparison value 1. The default setting is "10".

**Operating mode "**
**Use measured value as reference**
**"**

With the parameter assignment of the [comparison value](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#switching-at-comparison-values-with-measured-value-as-reference-s7-1500), you specify the measured value at which the digital output DQ1 switches as a result of the selected comparison event.

You must enter a floating point number (REAL). If you use the DQ function "Between comparison value 0 and 1", the comparison value 0 has to be smaller than comparison value 1. The maximum value is 7.922816 x 10<sup>28</sup>. The default setting is "10.0". The unit of the comparison value depends on the measured variable.

#### Count direction

You use this parameter to specify the direction of position value change for which the selected function is valid.

You can select from the following options:

| Direction of position value change | Meaning |
| --- | --- |
| In both directions  (default) | The comparison and switching of the respective digital output is carried out regardless of whether the position value increases of decreases. |
| Up | The comparison and switching of the respective digital output only takes place when the position value increases. |
| Down | The comparison and switching of the respective digital output only takes place when the position value decreases. |

The parameter can be configured for the following functions:

- At comparison value for a pulse duration
- After set command from CPU until comparison value

#### Pulse duration

By configuring the pulse duration for the function "At comparison value for a pulse duration", you specify the number of milliseconds for which the respective digital output is active.

A value from 0.1 to 6553.5 ms is permissible.

The default setting is "500.0", which is equivalent to a pulse duration of 0.5 s.

#### Hysteresis (in increments)

By configuring the [hysteresis](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#hysteresis-with-ssi-absolute-encoder-s7-1500), you can define a range around the comparison values. For the functions "Between comparison value and upper counter limit" and "Between comparison value and lower counter limit" the hysteresis also applies at the counter limits. Within the hysteresis range, the digital outputs cannot switch again until the position value has left this range once.

Choose a small enough hysteresis. When the hysteresis range, starting from the configured comparison value, spans the entire position value range, proper functioning of the comparison values cannot be guaranteed.

If a comparison value lies so close to the counter limit that the hysteresis range would extend beyond this counter limit, the hysteresis range ends there.

If you enter "0", the hysteresis is turned off. You can enter a value between 0and 255. The default setting is "0".

> **Note**
>
> You configure the hysteresis under "Behavior of DQ0" for both digital outputs together. The hysteresis is also displayed under "Behavior of DQ1".

> **Note**
>
> The hysteresis is only available in operating mode "Use position value (SSI absolute value) as reference".

### Specify measured value (SSI_Absolute_Encoder) (S7-1500)

#### Measured variable

With this parameter you specify whether the technology module is to provide a certain [measured variable](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#measuring-types-s7-1500-1) or the complete SSI frame.

You can select from the following options:

| Option | Meaning | Additional option-specific  parameters |
| --- | --- | --- |
| Frequency (default) | The measured variable shows the number of increments per second, where each increment corresponds to one position value change. The value is a floating point number (REAL). The unit is Hz.   The technology object displays the measured value at the output parameter MeasuredValue. | - Update time |
| Period | The measured variable is the average period between two increments of the position value. The value is an integer (DINT). The unit is s.  The technology object displays the measured value at the output parameter MeasuredValue. | - Update time |
| Velocity | The measured variable is a velocity.  Examples of a velocity measurement can be found in the explanation of the "Increments per unit" parameter.  The technology object displays the measured value at the output parameter MeasuredValue. | - Update time - Time base for velocity measurement - Increments per unit |
| Complete SSI frame | Instead of a measured variable, the first 32 bits of the SSI frame are returned (bit 0 to bit 31). In so doing, special bits that do not belong to the position information are also supplied. A configured inversion of the direction is ignored.  The technology object displays the value at the output parameter CompleteSSIFrame.  You can find examples under [Examples of the frame format](#examples-of-the-frame-format-s7-1500). This option is only available in operating mode "Use position value (SSI absolute value) as reference". | — |

> **Note**
>
> If the increment per revolution is required for calculation of the measured values, it is automatically calculated from the parameterized telegram length as the power of 2, e.g. 8192 increments per revolution with a telegram length of 13 bit. If you are using an SSI absolute encoder whose increment per revolution does not correspond to the power of 2, the calculated measured value may be incorrect for a short time.

#### Update time

By configuring the [update time](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#measuring-intervals-s7-1500-1) in milliseconds, you can specify the time interval between two measured value updates. Unsteady measured variables can be smoothed through longer update times

If you enter "0", the measured value is updated once per module-internal cycle. Up to three decimal places can be entered. A value from 0.0 to 25000.0 is permissible. The default setting is "10.0".

#### Time base for velocity measurement

This parameter defines the time base on which the velocity is to be returned.

You can select from the following options:

- 1 ms
- 10 ms
- 100 ms
- 1 s
- 60 s

The default setting is "60 s".

#### Increments per unit

With this parameter you define the number of increments per relevant unit that the SSI absolute encoder supplies for the velocity measurement.

You can enter a value between 1 and 65535.

**Example 1:**

Your absolute encoder operates with a resolution of 12 bits per revolution and performs 4096 increments per revolution. The velocity should be measured in revolutions per minute.

In this case, you need to assign the following parameters:

- Increments per unit: 4096
- Time base for velocity measurement: 60 s

**Example 2:**

You encoder delivers 10000 increments for travel over one meter. The velocity is to be measured in meters per second.

In this case, you need to assign the following parameters:

- Increments per unit: 10000
- Time base for velocity measurement: 1 s

### Examples of the frame format (S7-1500)

#### **Example 1**

In this example the SSI absolute encoder has the following specification:

- The encoder has a resolution of 13 bits per revolution and a value range of 12 bits of revolutions. The SSI frame has a length of 25 bits.
- The MSB of the position value is bit 24.
- The LSB of the position value is bit 0.
- The position value is Gray coded.
- A parity bit is not available.

The frame has the following format:

![Example 1](images/111042823819_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| MG | Multiturn bit as Gray code |
| SG | Singleturn bit as Gray code |

**Complete SSI frame**

If you configure "Complete SSI frame", the technology module returns the unprocessed SSI frame in the return interface right-justified:

![Example 1](images/58935096587_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| MG | Multiturn bit as Gray code |
| SG | Singleturn bit as Gray code |

**Position value feedback value**

The position value supplied in Gray code is converted into binary code by the technology module and returned right-justified in the feedback interface:

![Example 1](images/58936138123_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| MD | Multiturn bit as binary code |
| SD | Singleturn bit as binary code |

#### **Example** 2

In this example the SSI absolute encoder has the following specification:

- The encoder has a resolution of 17 bits per revolution and a value range of 11 bits of revolutions. The SSI frame has a length of 34 bits.
- The MSB of the position value is bit 33.
- The LSB of the position value is bit 6.
- The position value is Gray coded.
- The SSI frame has six special bits.
- A parity bit is available. A parity bit does not count in the frame length.

The frame has the following format:

![Example2](images/86069268619_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| MG | Multiturn bit as Gray code |
| SG | Singleturn bit as Gray code |
| Sn | Special bit n |
| P | Parity bit |

**Complete SSI frame**

If you configure "Complete SSI frame", the technology module returns the least significant 32 bits of the SSI frame as an unprocessed bit string. The technology module returns the bit following the LSB as parity bit. In this example, the technology module therefore returns only the least significant 31 bits of the SSI frame. With the complete SSI frame, you can evaluate the additional special bits in your application.

The returned bit string is structured as follows:

![Example2](images/86069273611_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| MG | Multiturn bit as Gray code |
| SG | Singleturn bit as Gray code |
| Sn | Special bit n |
| P | Parity bit |

**Position value**

The position value supplied in Gray code is converted into binary code by the technology module and returned right-justified in the feedback interface: The special bits are ignored in this case. The parity bit is evaluated but is not returned with the position value:

![Example2](images/86069304203_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| MD | Multiturn bit as binary code |
| SD | Singleturn bit as binary code |

## SSI_Absolute_Encoder programming (S7-1500)

This section contains information on the following topics:

- [Instruction SSI_Absolute_Encoder (S7-1500)](#instruction-ssi_absolute_encoder-s7-1500)
- [Call instruction in the user program (S7-1500)](#call-instruction-in-the-user-program-s7-1500)

### Instruction SSI_Absolute_Encoder (S7-1500)

#### SSI_Absolute_Encoder

The SSI_Absolute_Encoder instruction is part of the SSI_Absolute_Encoder technology object. It supplies the control and feedback interface of the TM PosInput technology module.

The SSI_Absolute_Encoder instruction thereby forms the software interface between the user program and the technology module. It must be called cyclically from the user program in order to synchronize the input and output data.

The SSI_Absolute_Encoder instruction can be used equally for the TM PosInput of the S7-1500, ET 200SP and ET 200eco PN M12-L systems. The TM PosInput modules can be used centrally and decentrally. The instruction applies in each case to the channel of the technology module that was assigned to the associated technology object.

#### Additional information

[Description SSI_Absolute_Encoder](SSI_Absolute_Encoder%20%28S7-1500%29.md#description-ssi_absolute_encoder-s7-1500)

[Input parameter SSI_Absolute_Encoder](SSI_Absolute_Encoder%20%28S7-1500%29.md#input-parameter-ssi_absolute_encoder-s7-1500)

[Output parameter SSI_Absolute_Encoder](SSI_Absolute_Encoder%20%28S7-1500%29.md#output-parameter-ssi_absolute_encoder-s7-1500)

[Error codes of parameter ErrorID](SSI_Absolute_Encoder%20%28S7-1500%29.md#error-codes-of-parameter-errorid-s7-1500)

[Static tags SSI_Absolute_Encoder](SSI_Absolute_Encoder%20%28S7-1500%29.md#static-tags-ssi_absolute_encoder-s7-1500)

### Call instruction in the user program (S7-1500)

The SSI_Absolute_Encoder instruction can be called once per channel, either cyclically or in a time-controlled program. The call is not permitted in an event-controlled interrupt program.

#### Procedure

Proceed as follows to call the instruction in the user program:

1. Open the CPU folder in the project tree.
2. Open the "Program blocks" folder.
3. Double-click the OB for cyclic program execution.  
   The block is opened in the work area.
4. In the "Instructions" window, open the "Technology" group and the "Counting, measurement, cams" folder.  
   The folder contains the instruction.
5. Select the instruction and drag it to your OB.  
   The "Call options" dialog opens.
6. Select a technology object from the "Name" list or enter the name for a new technology object.
7. Confirm with "OK".

#### Result

If the technology object does not exist yet, it is added. The instruction is added in the OB. The technology object is assigned to this call of the instruction.

> **Note**
>
> If you click one of the buttons "Configuration", "Commissioning" or "Diagnostics" in the user interface of the instruction, the respective editor opens.

## Commissioning SSI_Absolute_Encoder (S7-1500)

This section contains information on the following topics:

- [Commissioning the technology object (S7-1500)](#commissioning-the-technology-object-s7-1500)

### Commissioning the technology object (S7-1500)

A graphic display of the block in the commissioning editor helps you with commissioning and the function test for the technology object. You can change specific parameters of the SSI_Absolute_Encoder instruction in CPU/IM online mode and monitor their effects.

#### Requirements

- There is an online connection between STEP 7 (TIA Portal) and the CPU.
- The CPU is in RUN.
- The corresponding SSI_Absolute_Encoder instruction is called cyclically from the user program.
- The parameters of the technology object are not overwritten by the user program.

#### Procedure

To open the commissioning editor of a technology object and to simulate a parameter value change, follow these steps:

1. Open the "Technology objects" folder in the project tree.
2. Open the SSI_Absolute_Encoder technology object in the project tree.
3. Double-click on the "Commissioning" object.  
   The functions for commissioning the SSI_Absolute_Encoder technology object are displayed.
4. In the commissioning dialog, click on the "Monitor all" button.  
   The parameters (online values) of the SSI_Absolute_Encoder technology object are loaded and displayed.
5. If the parameter you want to change has a text box, enter the new value there.
6. Select the check box of the parameter.  
   The new parameter value becomes effective and the effects of the change are simulated.

#### Online mode

In online mode, you can modify the following parameters to test the technology object function:

- New comparison value 0 (NewReferenceValue0 or NewReferenceValue0_M)
- New comparison value 1 (NewReferenceValue1 or NewReferenceValue1_M)
- Enable Capture (CaptureEnable)
- Acknowledgment of signaled error states (ErrorAck)
- Resetting the status flag (EventAck)

## SSI_Absolute_Encoder diagnostics (S7-1500)

This section contains information on the following topics:

- [Monitoring counter values, measured values, DIs and DQs (S7-1500)](#monitoring-counter-values-measured-values-dis-and-dqs-s7-1500)

### Monitoring counter values, measured values, DIs and DQs (S7-1500)

The diagnostic functions are used to monitor the position input and measuring functions.

#### Requirements

- There is an online connection between STEP 7 (TIA Portal) and the CPU.
- The CPU is in RUN.

#### Procedure

To open the display editor for the diagnostic functions, follow these steps:

1. Open the "Technology objects" folder in the project tree.
2. Open the SSI_Absolute_Encoder technology object in the project tree.
3. Double-click on the "Diagnostics" object.
4. Click the "Monitor all" button.

#### Display

The following values are read by the technology object from the feedback interface and displayed:

- Event display/diagnostics information
- Signal states of the digital inputs and digital outputs
- Position value
- Capture value
- Measured value

Additional information on status displays is available in the context-sensitive help for each event in STEP 7 (TIA Portal). When the CPU is in STOP, the status display is not updated.

![Display](images/105103950731_DV_resource.Stream@PNG-en-US.PNG)

---
title: "Use technology object High_Speed_Counter (S7-1500)"
package: TFTOHSCenUS
topics: 22
devices: [S7-1500, S7-1500T]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Use technology object High_Speed_Counter (S7-1500)

This section contains information on the following topics:

- [Convention (S7-1500)](#convention-s7-1500)
- [High_Speed_Counter technology object (S7-1500)](#high_speed_counter-technology-object-s7-1500)
- [Overview of the configuration steps (S7-1500)](#overview-of-the-configuration-steps-s7-1500)
- [Add technology object (S7-1500)](#add-technology-object-s7-1500)
- [Configuring the High_Speed_Counter (S7-1500)](#configuring-the-high_speed_counter-s7-1500)
- [Programming the High_Speed_Counter (S7-1500)](#programming-the-high_speed_counter-s7-1500)
- [Commissioning the High_Speed_Counter (S7-1500)](#commissioning-the-high_speed_counter-s7-1500)
- [High_Speed_Counter diagnostics (S7-1500)](#high_speed_counter-diagnostics-s7-1500)

## Convention (S7-1500)

**Technology module**: We use the term "technology module" in this documentation both for the technology modules TM Count and TM PosInput and the technology component of the compact CPUs.

## High_Speed_Counter technology object (S7-1500)

STEP 7 (TIA Portal) supports you in the configuration, commissioning and diagnostics of counting and measuring functions for the following technology modules with the "Technology objects" function:

- You configure the High_Speed_Counter technology object in STEP 7 (TIA Portal) with the settings for the counting and measuring functions.
- The corresponding High_Speed_Counter instruction is programmed in the user program. This instruction supplies the control and feedback interface of the technology module.

The High_Speed_Counter technology object corresponds to the instance DB of the High_Speed_Counter instruction. The configuration of the counting and measuring functions is saved in the technology object. The technology object is located in the folder "PLC &gt; Technology objects".

The High_Speed_Counter technology object can be used equally for technology modules of the S7-1500, ET 200SP and ET 200eco PN M12-L systems.

### Operating mode

In order to assign the technology module parameters using the technology object, you specify the [operating mode](Using%20the%20module%20%28S7-1500%29.md#operating-mode-s7-1500) "Operating with "Counting and measurement" technology object" in the hardware configuration of the technology module. This selection is already preset.

## Overview of the configuration steps (S7-1500)

### Introduction

The overview below shows the basic procedure for configuring the counting and measuring functions of the technology module with the High_Speed_Counter technology object.

### Requirement (TM Count and TM PosInput)

Before you can use the High_Speed_Counter technology object, a project with an S7-1500 CPU or an ET 200SP CPU must be created in STEP 7 (TIA Portal) .

### Requirement (Compact CPU)

Before you can use the High_Speed_Counter technology object, a project with a Compact CPU S7‑1500 must be created in STEP 7 (TIA Portal).

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

### Requirement (TM Count and TM PosInput)

A project with a CPU S7‑1500 has been created.

### Requirement (Compact CPU)

A project with a Compact CPU S7‑1500 has been created.

### Procedure

To add a technology object, proceed as follows:

1. Open the CPU folder in the project tree.
2. Open the "Technology objects" folder.
3. Double-click on "Add new object".  
   The "Add new object" dialog opens.
4. Select the technology "Counting, measurement, cams".
5. Select the "High_Speed_Counter" object.
6. Enter an individual name for the technology object in the "Name" text box.
7. Click "Additional information" if you want to add your own information to the technology object.
8. Confirm with "OK".

### Result

The new technology object has now been created and stored in the project tree in the "Technology objects" folder.

![Result](images/44575028491_DV_resource.Stream@PNG-en-US.PNG)

|  | Object | Description |
| --- | --- | --- |
| ① | [Configuration](#working-with-the-configuration-dialog-s7-1500) | In the configuration dialog:  - Assignment of technology module and channel - Technology object parameter settings for counting and measurement functions   When you change the configuration of the technology object, you must download the technology object **and** the hardware configuration to the CPU. |
| ② | [Commissioning](#commissioning-the-technology-object-s7-1500) | Commissioning and function test of the technology object:  Simulating parameters of the High_Speed_Counter instruction and monitoring the effects |
| ③ | [Diagnostics](#monitoring-counter-values-measured-values-dis-and-dqs-s7-1500) | Monitoring the counting and measuring functions |

## Configuring the High_Speed_Counter (S7-1500)

This section contains information on the following topics:

- [Working with the configuration dialog (S7-1500)](#working-with-the-configuration-dialog-s7-1500)
- [Basic parameters (S7-1500)](#basic-parameters-s7-1500)
- [Counter inputs (High_Speed_Counter) (S7-1500)](#counter-inputs-high_speed_counter-s7-1500)
- [Counter behavior (S7-1500)](#counter-behavior-s7-1500)
- [Behavior of a DI (High_Speed_Counter) (S7-1500)](#behavior-of-a-di-high_speed_counter-s7-1500)
- [Behavior of a DQ (High_Speed_Counter) (S7-1500)](#behavior-of-a-dq-high_speed_counter-s7-1500)
- [Specify measured value (High_Speed_Counter) (S7-1500)](#specify-measured-value-high_speed_counter-s7-1500)

### Working with the configuration dialog (S7-1500)

You configure the properties of the technology object in the configuration window. Proceed as follows to open the configuration window of the technology object:

1. Open the "Technology objects" folder in the project tree.
2. Open the technology object in the project tree.
3. Double-click on the "Configuration" object.

The configuration is divided into the following categories:

- **Basic parameters**

  The basic parameters include the selection of the technology module and the number of the counting channel for which the technology object is configured.
- **Extended parameters**

  The extended parameters include the parameters for adapting the counting and measuring functions and for setting the characteristics of the digital inputs and digital outputs.

![Figure](images/44750680331_DV_resource.Stream@PNG-en-US.PNG)

#### Configuration window icons

Icons in the area navigation of the configuration show additional details about the status of the configuration:

| Symbol | Meaning |
| --- | --- |
| ![Configuration window icons](images/41244027019_DV_resource.Stream@PNG-de-DE.png) | **The configuration contains default values and is complete**.  The configuration contains only default values. With these default values, you can use the technology object without additional changes. |
| ![Configuration window icons](images/41244015115_DV_resource.Stream@PNG-de-DE.png) | **The configuration contains values set by the user or automatically adapted values and is complete**   All text boxes of the configuration contain valid values and at least one default value was changed. |
| ![Configuration window icons](images/41243964811_DV_resource.Stream@PNG-de-DE.png) | **The configuration is incomplete or incorrect**   At least one text box or drop-down list contains an invalid value. The corresponding field or the drop-down list is displayed on a red background. Click the roll-out error message to indicate the cause of error. |

### Basic parameters (S7-1500)

You can establish the connection between the High_Speed_Counter technology object and the technology module under "Basic parameters".

#### Module (TM Count and TM PosInput)

You select the technology module in a subsequent dialog box. All technology modules (central or distributed) that are configured for use with a "Counting and measurement" technology object under the S7-1500 CPU or ET 200SP CPU are available for selection.

After selecting the technology module, you can open the device configuration associated with the technology module by clicking the"Device configuration" button.

The technology module parameter settings required for the use of the technology object are made in the "Extended parameters" of the technology object.

#### Module (Compact CPU)

You can select a high-speed counter for the Compact CPU in a subsequent dialog. You can choose any of the high-speed counters which are enabled and configured for use with a technology object from "Counting and measuring".

After selecting the high-speed counter, you can open the device configuration associated with the Compact CPU by clicking the"Device configuration" button.

The parameter settings of the high-speed counter required for the use of the technology object are made in the "Extended parameters" of the technology object.

#### Channel

For a technology module with several counting channels, you can also select the number of the counting channel for which the High_Speed_Counter technology object is to be valid.

> **Note**
>
> A channel can be assigned to only one technology object. A channel that is already assigned to a technology object can no longer be selected.

#### Synchronization of the parameter values

If, after assignment of the channel to the technology object, there is an inconsistency between the parameter values in the property dialog of the module and in the technology object, a button with a corresponding inquiry appears. When you click the button, the parameter values in the property dialog are overwritten by the parameter values in the property dialog within STEP 7 (TIA Portal). The current parameter values of the technology object are displayed in the property dialog (read-only).

> **Note**
>
> If you change parameter values of the technology object, the corresponding parameter values are also overwritten without prompt in the properties dialog of the hardware configuration. As after every change in hardware configuration, the next time the project is loaded in the CPU, a prompt appears asking whether the CPU should go to STOP mode.

### Counter inputs (High_Speed_Counter) (S7-1500)

#### Signal type

You can choose from the following [signal types](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#encoder-signals-s7-1500):

| Symbol | Signal type | Meaning | Additional option-specific parameters |
| --- | --- | --- | --- |
| ![Signal type](images/42918897547_DV_resource.Stream@PNG-de-DE.png) | Incremental encoder (A, B phase-shifted) | An incremental encoder with phase-shifted A and B signals is connected. | - Signal evaluation - Invert direction - Filter frequency - Sensor type or Interface standard |
| ![Signal type](images/42919384843_DV_resource.Stream@PNG-de-DE.png) | Incremental encoder (A, B, N) | An incremental encoder with phase-shifted signals A and B and a zero signal N is connected. | - Signal evaluation - Invert direction - Filter frequency - Sensor type or Interface standard - Reaction to signal N - Frequency of synchronization - Frequency of the Capture function |
| ![Signal type](images/42919444875_DV_resource.Stream@PNG-de-DE.png) | Pulse (A) and direction (B) | A pulse encoder (signal A) with direction signal (signal B) is connected. | - Filter frequency - Sensor type or Interface standard |
| ![Signal type](images/42919620107_DV_resource.Stream@PNG-de-DE.png) | Pulse (A) | A pulse encoder (signal A) without direction signal is connected. You can specify the counting direction by means of the [control interface](Using%20the%20module%20%28S7-1500%29.md#assignment-of-the-control-interface-s7-1500). | - Filter frequency - Sensor type or Interface standard |
| ![Signal type](images/42919680907_DV_resource.Stream@PNG-de-DE.png) | Count up (A), count down (B) | Signals for counting up (signal A) and down (signal B) are connected. | - Filter frequency - Sensor type or Interface standard |

#### Invert direction

You can invert the counting direction to adapt it to the process.

The inverting of the direction can be configured and active for the following signal types:

- Incremental encoder (A, B phase-shifted)
- Incremental encoder (A, B, N)

#### Signal evaluation

By configuring [signal evaluation](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#overview-s7-1500), you can specify which edges of the signals are counted.

You can select from the following options:

| Symbol | Signal evaluation | Meaning |
| --- | --- | --- |
| ![Signal evaluation](images/42918897547_DV_resource.Stream@PNG-de-DE.png) | [Single](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#single-evaluation-s7-1500)  (default) | The edges of signal A are evaluated during a low level of signal B. |
| ![Signal evaluation](images/42918558091_DV_resource.Stream@PNG-de-DE.png) | [Double](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#double-evaluation-s7-1500) | Each edge of signal A is evaluated. |
| ![Signal evaluation](images/42918888715_DV_resource.Stream@PNG-de-DE.png) | [Quadruple](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#quadruple-evaluation-s7-1500) | Each edge of signals A and B is evaluated. |

The parameter can be assigned with the following signal types:

- Incremental encoder (A, B phase-shifted)
- Incremental encoder (A, B, N)

#### Filter frequency

By configuring the filter frequency, you suppress interferences at the counter inputs A, B and N.

The selected filter frequency is based on a pulse/break ratio of between around 40:60 and around 60:40. This results in a specific minimum pulse/break time. Signal changes with a duration shorter than the minimum pulse/break time are suppressed.

You can select from the following filter frequencies:

| Filter frequency | Minimum pulse/break time |
| --- | --- |
| 100 Hz | 4.0 ms |
| 200 Hz | 2.0 ms |
| 500 Hz | 800 µs |
| 1 kHz | 400 µs |
| 2 kHz | 200 µs |
| 5 kHz | 80 µs |
| 10 kHz | 40 µs |
| 20 kHz | 20 µs |
| 50 kHz | 8.0 µs |
| 100 kHz (default for Compact CPU) | 4.0 µs |
| 200 kHz<sup>2</sup> (default for TM Count and ET 200eco PN TM PosInput 2) | 2.0 µs |
| 500 kHz<sup>1</sup> | 0.8 µs |
| 1 MHz<sup>1</sup> (default for TM PosInput) | 0.4 µs |
| <sup>1</sup> Only available with TM PosInput   2 Not available with Compact CPU |  |

#### Sensor type (TM Count)

By configuring the sensor type, you specify how the counter inputs are switched for the TM Count.

You can select from the following options:

| Sensor type | Meaning |
| --- | --- |
| Sourcing output  (default) | The encoder/sensor switches the inputs A, B and N to 24VDC. |
| Sinking output | The encoder/sensor switches the inputs A, B and N to M. |
| Push-pull (sinking and sourcing output) | The encoder/sensor alternately switches the inputs A, B and N to M and 24VDC. |

"Push-pull" is usually selected when incremental encoders are used. If using 2-wire sensors, such as light barriers or proximity switches, you need to select the corresponding wiring "Sourcing output" or "Sinking output".

The data sheet of the encoder includes information on whether your incremental encoder is a push-pull encoder.

> **Note**
>
> If you use a push-pull encoder and the sensor type "Push-pull (sinking and sourcing output)" is configured, you can monitor the encoder signals for wire break.

#### Sensor type (Compact CPU)

The "Sourcing output" sensor type is set for the Compact CPU and cannot be changed. The encoder or sensor switches the inputs A, B and N to 24V DC.

You can operate both sourcing output encoders and push-pull encoders on the Compact CPU. You can find additional information on the sensor type in the data sheet for the encoder.

#### Sensor type (ET 200eco PN TM PosInput 2)

By configuring the sensor type, you specify how the counter inputs are switched for the ET 200eco PN TM PosInput 2.

You can select from the following options:

| Sensor type | Meaning |
| --- | --- |
| Sourcing output  (default) | The encoder or sensor switches the inputs A, B and N to 1U <sub>Sx</sub>. |
| Sinking output | The encoder or sensor switches the inputs A, B and N to 1M. |
| Push-pull (sinking and sourcing output) | The encoder or sensor switches the inputs A, B and N alternately to 1M and 1U<sub>Sx</sub>. |

"Push-pull" is usually selected when incremental encoders are used. If using 2-wire sensors, such as light barriers or proximity switches, you need to select the corresponding wiring "Sourcing output" or "Sinking output".

The data sheet of the encoder includes information on whether your incremental encoder is a push-pull encoder.

This parameter can only be configured if you have selected "24 V, asymmetrical" as the interface standard.

> **Note**
>
> If you use a push-pull encoder and the sensor type "Push-pull (sinking and sourcing output)" is configured, you can monitor the encoder signals for wire break.

#### Interface standard (TM PosInput)

You use this parameter to specify whether the encoder outputs symmetric (RS422) or asymmetric (TTL) signals for the TM PosInput.

You can select from the following options:

| Interface standard | Meaning |
| --- | --- |
| RS422, symmetrical (default) | The encoder outputs symmetric signals according to the [RS422 standard](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#rs422-count-signals-s7-1500). |
| TTL (5 V), asymmetrical | The encoder outputs asymmetric 5 V signals according to the [TTL standard](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#24-v-or-ttl-count-signals-s7-1500). |

> **Note**
>
> The RS422 standard provides greater interference immunity than the TTL standard. If your incremental or pulse encoder supports the RS422 standard **and** the TTL standard, we recommend using the RS422 standard.

#### Interface standard (ET 200eco PN M12-L TM PosInput 2)

You use this parameter to specify whether the encoder outputs symmetrical (RS422) or asymmetrical (24 V) signals for the ET 200eco PN M12-L TM PosInput 2.

You can select from the following options:

| Interface standard | Meaning |
| --- | --- |
| RS422, symmetrical (default) | The encoder outputs symmetric signals according to the [RS422 standard](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#rs422-count-signals-s7-1500). |
| 24 V, asymmetrical | The encoder outputs asymmetric 24 V signals according to the [TTL standard](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#24-v-or-ttl-count-signals-s7-1500). |

#### Reaction to signal N

You use this parameter to specify which reaction is triggered to signal N.

You can select from the following options:

| Option | Meaning |
| --- | --- |
| No reaction to signal N (default) | The counter is not affected by signal N. |
| [Synchronization at signal N](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#synchronization-at-signal-n-s7-1500) | The counter is set to the start value at signal N.   If you select the function "Enable synchronization at signal N" for a digital input, the synchronization depends on the level at the digital input. |
| [Capture at signal N](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#capture-with-incremental-or-pulse-encoder-s7-1500) | The counter value is stored in the Capture value at signal N. The use of a digital input and the use of the N signal are not mutually exclusive for the Capture function.  The technology object displays the Capture value at the output parameter CapturedValue. |

> **Note**
>
> You can only select the reaction to signal N if you have selected the "Incremental encoder (A, B, N)" signal type.

> **Note**
>
> If "Synchronization at signal N" is selected, you can select the function "Enable synchronization at signal N" for a [digital input](#behavior-of-a-di-high_speed_counter-s7-1500).

> **Note**
>
> **For High_Speed_Counter as of V3.0, the following applies:**
>
> You can choose "Capture at signal N" only in operating mode "Use count value as reference":

#### Frequency of synchronization

This parameter is used to define the frequency of the following events:

- Synchronization at signal N
- Synchronization as a function of a digital input

You can select from the following options:

| Option | Meaning |
| --- | --- |
| Once (default) | The counter is only set at the first signal N or the first configured edge of the digital input. |
| Periodic | The counter is set at each signal N or each configured edge of the digital input. |

#### Frequency of the Capture function

This parameter is used to define the frequency of Capture events for the following functions:

- Capture at Signal N
- Capture as function of a digital input

You can select from the following options:

| Option | Meaning |
| --- | --- |
| Once | The first configured edge at the respective digital input or first rising edge of the N signal saves the current counter value as a Capture value. |
| Periodic (default) | Each configured edge at the respective digital input or each rising edge of the N signal saves the current counter value as a Capture value. |

> **Note**
>
> This parameter is available for High_Speed_Counter as of V3.2.

### Counter behavior (S7-1500)

This section contains information on the following topics:

- [Counting limits and start value (S7-1500)](#counting-limits-and-start-value-s7-1500)
- [Counter behavior at limits and gate start (S7-1500)](#counter-behavior-at-limits-and-gate-start-s7-1500)

#### Counting limits and start value (S7-1500)

##### High counting limit

You limit the counting range by setting the high counting limit. You can enter a value up to 2147483647 (2<sup>31</sup>-1). You must enter a value that lies above the low counting limit.

The default setting is "2147483647".

##### Low counting limit

You limit the counting range by setting the low counting limit. You can enter a value up to -2147483648 (-2<sup>31</sup>). You must enter a value below the high counting limit.

The default setting is "-2147483648".

##### Start value

By configuring the start value, you specify the value at which counting is to start and where it is to continue in the case of defined events. You must enter a value between the counting limits or equal to the counting limits.

The default setting is "0".

##### Additional information

For more information, see [Behavior at the counting limits](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#behavior-at-the-counting-limits-s7-1500) and [Counter behavior at gate start](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#counter-behavior-at-gate-start-s7-1500).

#### Counter behavior at limits and gate start (S7-1500)

##### Reaction to violation of a counting limit

You can configure the following characteristics for [violation of a counting limit](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#behavior-at-the-counting-limits-s7-1500):

| Reaction | Meaning |
| --- | --- |
| Stop counting | If a counting limit is violated, counting is stopped and the internal gate is closed. To restart counting, you must also close and reopen the software/hardware gate. |
| Continue counting (default) | Counting continues either with the start value or at the opposite counting limit, depending on the additional parameter assignment. |

##### Reset when counting limit is violated

You can reset the counter to the following values when a counting limit is violated:

| Reset the value | Meaning |
| --- | --- |
| To start value | The counter value is set to the start value. |
| To opposite counting limit (default) | The counter value is set to the opposite counting limit. |

##### Reaction to gate start

You can set the following [Reaction to gate start](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#counter-behavior-at-gate-start-s7-1500):

| Reaction | Meaning |
| --- | --- |
| Set to start value | When the gate is opened, the counter value is set to the start value. |
| Continue with current value (default) | When the gate is opened, counting is continued with the last counter value. |

### Behavior of a DI (High_Speed_Counter) (S7-1500)

#### Setting function of the DI

By configuring a digital input, you specify which functions the digital input triggers at switching.

You can select from the following options:

| Function of a digital input | Meaning | Additional option-specific parameters |
| --- | --- | --- |
| Gate start/stop (level-triggered) | The level at the respective digital input opens and closes the [hardware gate](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#hardware-gate-s7-1500). | - Input delay - Select level |
| Gate start (edge-triggered) | The configured edge at the respective digital input opens the [hardware gate](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#hardware-gate-s7-1500). | - Input delay - Edge selection |
| Gate stop (edge-triggered) | The configured edge at the respective digital input closes the [hardware gate](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#hardware-gate-s7-1500). | - Input delay - Edge selection |
| [Synchronization](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#synchronization-s7-1500-1) | The configured edge at the respective digital input sets the counter to the start value.  The technology object indicates whether a synchronization has occurred at the [output parameter](High_Speed_Counter%20%28S7-1500%29.md#high_speed_counter-output-parameters-s7-1500) SyncStatus. | - Input delay - Edge selection - Frequency of synchronization |
| Enable synchronization at signal N | The active level at the respective digital input enables [synchronization of the counter at signal N](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#synchronization-at-signal-n-s7-1500). | - Input delay - Select level |
| Capture | The configured edge at the respective digital input [saves the current counter value](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#capture-with-incremental-or-pulse-encoder-s7-1500) as a Capture value. The use of a digital input and the use of the N signal are not mutually exclusive for the Capture function.  The technology object displays the Capture value at the [output parameter](High_Speed_Counter%20%28S7-1500%29.md#high_speed_counter-output-parameters-s7-1500) CapturedValue. | - Input delay - Edge selection - Frequency of the Capture function - Behavior of counter value after Capture |
| Digital input without function | No technological function is assigned to the respective digital input.  You can read the signal state of the digital input via the respective [static variable](High_Speed_Counter%20%28S7-1500%29.md#high_speed_counter-static-variables-s7-1500) of the technology object (number of digital inputs depends on the module):  - UserStatusFlags.StatusDI0 - UserStatusFlags.StatusDI1 - UserStatusFlags.StatusDI2 | - Input delay |

> **Note**
>
> With the exception of "Digital input without function", each function can only be used once for each counter, and if used for one digital input is not available to the others.

> **Note**
>
> **For High_Speed_Counter as of V3.0, the following applies:**
>
> You can choose the "Capture" function only in operating mode "Use count value as reference".

#### Input delay (TM Count and TM PosInput)

You use this parameter to suppress signal interference at the digital inputs. Changes to the signal are only detected if they remain stable for longer than the configured input delay time.

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
> You configure the input delay under "Behavior of DI0" for all digital inputs together. The input delay is also displayed under "Behavior of DI1" and for TM Count also under "Behavior of DI2".

#### Input delay (Compact CPU)

You use this parameter to suppress interference at the digital inputs of the DIn signals. Changes to the signal are only detected if they remain stable for longer than the configured input delay time.

You can configure the input delay for a digital input of a Compact CPU in the Inspector window of the device configuration under "Properties &gt; DI 16/DQ 16 &gt; Inputs &gt; Channel n".

You can select from the following input delays:

- None
- 0.05 ms
- 0.1 ms
- 0.4 ms
- 1.6 ms
- 3.2 ms (default)
- 12.8 ms
- 20 ms

> **Note**
>
> If you select the "None" or "0.05 ms" option, you have to use shielded cables for connection of the digital inputs.

#### Select level

You use this parameter to specify the level at which the digital input is active.

You can select from the following options:

| Level | Meaning |
| --- | --- |
| Active with high level  (default) | The respective digital input is active when it is set. |
| Active with low level | The respective digital input is active when it is not set. |

The parameter can be set for the following functions of a digital input:

- Gate start/stop (level-triggered)
- Enable synchronization at signal N

#### Edge selection

You can use this parameter to specify the edge of the digital input at which the configured function is triggered.

The following options may be available depending on the function selected:

- At rising edge (default)
- At falling edge
- At rising and falling edge

The parameter can be set for the following functions of a digital input:

- Gate start (edge-triggered)
- Gate stop (edge-triggered)
- Synchronization
- Capture

> **Note**
>
> "At rising and falling edge" can only be configured for the "Capture" function.

#### Frequency of synchronization

This parameter is used to define the frequency of the following events:

- Synchronization at signal N
- Synchronization as a function of a digital input

You can select from the following options:

| Option | Meaning |
| --- | --- |
| Once (default) | The counter is only set at the first signal N or the first configured edge of the digital input. |
| Periodic | The counter is set at each signal N or each configured edge of the digital input. |

#### Frequency of the Capture function

This parameter is used to define the frequency of Capture events for the following functions:

- Capture at Signal N
- Capture as function of a digital input

You can select from the following options:

| Option | Meaning |
| --- | --- |
| Once | The first configured edge at the respective digital input or first rising edge of the N signal saves the current counter value as a Capture value. |
| Periodic (default) | Each configured edge at the respective digital input or each rising edge of the N signal saves the current counter value as a Capture value. |

> **Note**
>
> This parameter is available for High_Speed_Counter as of V3.2.

#### Behavior of counter value after Capture

You can configure the following characteristics for the counter after a [capture event](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#capture-with-incremental-or-pulse-encoder-s7-1500):

| Reaction | Meaning |
| --- | --- |
| Continue counting (default) | After saving the current counter value as Capture value, counting is continued unchanged. |
| Set to start value and continue counting | After saving the current counter value as Capture value, counting is continued with the start value. |

### Behavior of a DQ (High_Speed_Counter) (S7-1500)

#### Operating mode (High_Speed_Counter V3.0 or higher)

The operating mode determines which value comparison functions work.

| Operating mode | Meaning |
| --- | --- |
| Use count value as reference (default) | The comparison functions and hardware interrupts for compare events work with the counter value.  This functionality corresponds to the functionality of the High_Speed_Counter in versions before V3.0. |
| Use measured value as reference | The comparison functions and hardware interrupts for compare events work with the measured value. |

> **Note**
>
> You configure the operating mode under "Behavior of DQ0" for both digital outputs together. The operating mode is also displayed under "Behavior of DQ1".

#### Set output

With the parameter assignment of a digital output, you specify the condition upon which the digital output switches.

You can select from the following options:

| [Function of a digital output](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#switching-at-comparison-values-with-counter-value-as-reference-s7-1500) in operating mode "Use count value as reference" | Meaning | Additional option-specific parameters |
| --- | --- | --- |
| Between comparison value and high limit (default) | The respective digital output is active if: Comparison value &lt;= counter value &lt;= high counting limit | - Comparison value 0 - Comparison value 1 - Hysteresis (in increments) |
| Between comparison value and low limit | The respective digital output is active if: Low counting limit &lt;= counter value &lt;= comparison value | - Comparison value 0 - Comparison value 1 - Hysteresis (in increments) |
| Between comparison value 0 and 1 | The digital output DQ1 is active if: Comparison value 0 &lt;= counter value &lt;= comparison value 1 | - Comparison value 0 - Comparison value 1 - Hysteresis (in increments) |
| At comparison value for a pulse duration | The respective digital output is active once for the configured time and count direction when the counter value reaches the comparison value. | - Comparison value 0 - Comparison value 1 - Count direction - Pulse duration - Hysteresis (in increments) |
| After set command from CPU until comparison value | When a set command is sent from the CPU, the respective digital output is active until the counter value is equal to the comparison value. | - Comparison value 0 - Comparison value 1 - Count direction - Hysteresis (in increments) |
| Use by user program | The respective digital output can be switched by the CPU [via the control interface](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#comparison-values-and-outputs-s7-1500). | — |

> **Note**
>
> **DQ0 of a counter of a Compact CPU**
>
> With a Compact CPU, the respective digital output DQ0 is available via the feedback interface, but not as a physical output.

> **Note**
>
> You can only select the "Between comparison value 0 and 1" function for digital output DQ1 and only if you have selected the "Use by user program" function for digital output DQ0.

> **Note**
>
> The "At comparison value for a pulse duration" and "After set command from CPU until comparison value" functions only switch the digital output in question if a count pulse reaches the comparison value. When the counter value is set, e.g. by synchronization, the digital output does not switch.

| [Function of a digital output](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#switching-at-comparison-values-with-measured-value-as-reference-s7-1500) in operating mode "Use measured value as reference" | Meaning | Additional option-specific parameters |
| --- | --- | --- |
| Measured value &gt;= comparison value (default) | The respective digital output is active if the measured value is greater than or equal to the comparison value. | - Comparison value 0 - Comparison value 1 |
| Measured value &lt;= comparison value | The respective digital output is active if the measured value is less than or equal to the comparison value. | - Comparison value 0 - Comparison value 1 |
| Between comparison value 0 and 1 | The digital output DQ1 is active if: Comparison value 0 &lt;= measured value &lt;= comparison value 1 | - Comparison value 0 - Comparison value 1 |
| Not between comparison value 0 and 1 | The digital output DQ1 is active if: Comparison value 1 &lt;= measured value &lt;= comparison value 0 | - Comparison value 0 - Comparison value 1 |
| Use by user program | The respective digital output can be switched by the CPU [via the control interface](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#comparison-values-and-outputs-s7-1500). | — |

> **Note**
>
> You can select the "Between comparison value 0 and 1" and "Not between comparison value 0 and 1" functions only for digital output DQ1 and only if you have selected the "Use by user program" function for digital output DQ0.

#### Comparison value 0(TM Count and TM PosInput)

**Operating mode "**
**Use count value as reference**
**"**

With the parameter assignment of the [comparison value](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#switching-at-comparison-values-with-counter-value-as-reference-s7-1500), you specify the counter value at which the digital output DQ0 switches as a result of the selected comparison event.

You must enter an integer (DINT) that is greater than or equal to the low counting limit. If you use the DQ function "Between comparison value 0 and 1", the comparison value 0 has to be smaller than comparison value 1. The default setting is "0".

**Operating mode "**
**Use measured value as reference**
**"**

With the parameter assignment of the [comparison value](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#switching-at-comparison-values-with-measured-value-as-reference-s7-1500), you specify the measured value at which the digital output DQ0 switches as a result of the selected comparison event.

You must enter a floating point number (REAL). If you use the DQ function "Between comparison value 0 and 1", the comparison value 0 has to be smaller than comparison value 1. The minimum value is -7.922816 x 10<sup>28</sup>. The default setting is "0.0". The unit of the comparison value depends on the measured variable.

#### Comparison value 0(Compact CPU)

**Operating mode "**
**Use count value as reference**
**"**

With the parameter assignment of the [Comparison value](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#switching-at-comparison-values-with-counter-value-as-reference-s7-1500), you specify the counter value at which the STS_DQ0 bit is set in the feedback interface of the selected comparison event. The digital output DQ0 is not available as a physical output in a Compact CPU.

You must enter an integer (DINT) that is greater than or equal to the low counting limit. If you use the DQ function "Between comparison value 0 and 1", the comparison value 0 has to be smaller than comparison value 1. The default setting is "0".

**Operating mode "**
**Use measured value as reference**
**"**

With the parameter assignment of the [Comparison value](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#switching-at-comparison-values-with-measured-value-as-reference-s7-1500), you specify the measured value at which the STS_DQ0 bit is set in the feedback interface of the selected comparison event. The digital output DQ0 is not available as a physical output in a Compact CPU.

You must enter a floating point number (REAL). If you use the DQ function "Between comparison value 0 and 1", the comparison value 0 has to be smaller than comparison value 1. The minimum value is -7.922816 x 10<sup>28</sup>. The default setting is "0.0". The unit of the comparison value depends on the measured variable.

#### Comparison value 1

**Operating mode "**
**Use count value as reference**
**"**

With the parameter assignment of the [comparison value](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#switching-at-comparison-values-with-counter-value-as-reference-s7-1500), you specify the counter value at which the digital output DQ1 switches as a result of the selected comparison event.

You must enter an integer (DINT) that is smaller than or equal to the high counting limit. If you use the DQ function "Between comparison value 0 and 1", the comparison value 0 has to be smaller than comparison value 1. The default setting is "10".

**Operating mode "**
**Use measured value as reference**
**"**

With the parameter assignment of the [comparison value](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#switching-at-comparison-values-with-measured-value-as-reference-s7-1500), you specify the measured value at which the digital output DQ1 switches as a result of the selected comparison event.

You must enter a floating point number (REAL). If you use the DQ function "Between comparison value 0 and 1", the comparison value 0 has to be smaller than comparison value 1. The maximum value is 7.922816 x 10<sup>28</sup>. The default setting is "10.0". The unit of the comparison value depends on the measured variable.

#### Count direction

You use this parameter to specify the count direction for which the selected function is valid.

You can select from the following options:

| Count direction | Meaning |
| --- | --- |
| In both directions  (default) | The comparison and switching of the respective digital output take place regardless of the count direction. |
| Up | The comparison and switching of the respective digital output only takes place when the counter counts up. |
| Down | The comparison and switching of the respective digital output only takes place when the counter counts down. |

The parameter can be configured for the following functions:

- At comparison value for a pulse duration
- After set command from CPU until comparison value

#### Pulse duration

By configuring the pulse duration for the function "At comparison value for a pulse duration", you specify the number of milliseconds for which the respective digital output is active.

If you enter "0" and the counter value corresponds to the comparison value, the digital output remains active until the next count pulse.

You can enter a value between 0.0 and 6553.5.

The default setting is "500.0", which is equivalent to a pulse duration of 0.5 s.

#### Hysteresis (in increments)

By configuring the [hysteresis](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#hysteresis-with-incremental-or-pulse-encoder-s7-1500), you can define a range around the comparison values. For the functions "Between comparison value and upper counter limit" and "Between comparison value and lower counter limit" the hysteresis also applies at the counter limits. Within the hysteresis range, the digital outputs cannot switch again until the counter value is outside the range.

Choose a small enough hysteresis. When the hysteresis range, starting from the configured comparison value, spans the entire counter value range, proper functioning of the comparison values cannot be guaranteed.

If a comparison value lies so close to the counter limit that the hysteresis range would extend beyond this counter limit, the hysteresis range ends at it.

If you enter "0", the hysteresis is turned off. You can enter a value between 0and 255. The default setting is "0".

> **Note**
>
> **The following applies for** 
> **High_Speed_Counter**
>  **as of V3.0:**
>
> You configure the hysteresis under "Behavior of DQ0" for both digital outputs together. The hysteresis is also displayed under "Behavior of DQ1".
>
> The hysteresis is only available in operating mode "Use count value as reference".

### Specify measured value (High_Speed_Counter) (S7-1500)

#### Measured variable

This parameter is used to specify the [measured variable](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#measuring-types-s7-1500) to be provided by the technology module. The technology object displays the measured value at the output parameter MeasuredValue.

You can select from the following options:

| Measured variable | Meaning | Additional option-specific parameters |
| --- | --- | --- |
| Frequency (default) | The measured variable shows the number of increments per second. The value is a floating point number (REAL). The unit is Hz.  The technology object displays the measured value at the output parameter MeasuredValue. | - Update time |
| Period | The measured variable is the average period between two increments. The value is an integer (DINT). The unit is s.  The technology object displays the measured value at the output parameter MeasuredValue. | - Update time |
| Velocity | The measured variable is a velocity.  Examples of a velocity measurement can be found in the explanation of the "Increments per unit" parameter.  The technology object displays the measured value at the output parameter MeasuredValue. | - Update time - Time base for velocity measurement - Increments per unit |

#### Update time

By configuring the [update time](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#measuring-intervals-s7-1500) in milliseconds, you can specify the time interval between two measured value updates.

The update time and the signal type effect the accuracy of the measurement. In the case of update times of at least 100 ms, the effect of the signal type is negligible.

In the case of update times of less than 100 ms, you achieve maximum measurement accuracy using the following signal types:

- Incremental encoder (A, B phase-shifted) with Signal evaluation "Single"
- Incremental encoder (A, B, N) with Signal evaluation "Single"
- Pulse (A) and direction (B)
- Pulse (A)

In the case of other signal types, measurement accuracy depends on the encoder and cable used.

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

You can use this parameter to define the number of count pulses per relevant unit that the incremental or absolute encoder supplies for the velocity measurement.

The number of count pulses depends on the configured signal evaluation. You can enter a value between 1 and 65535.

**Example 1:**

You encoder delivers 4000 count pulses for travel over one meter. The velocity is to be measured in meters per second. "Double" is configured as signal evaluation.

In this case, you need to assign the following parameters:

- Increments per unit: 8000
- Time base for velocity measurement: 1 s

**Example 2:**

Your encoder delivers 4096 count pulses per revolution. The velocity is to be measured in revolutions per minute. "Single" is configured as the signal evaluation.

In this case, you need to assign the following parameters:

- Increments per unit: 4096
- Time base for velocity measurement: 60 s

## Programming the High_Speed_Counter (S7-1500)

This section contains information on the following topics:

- [High_Speed_Counter instruction (S7-1500)](#high_speed_counter-instruction-s7-1500)
- [Call instruction in the user program (S7-1500)](#call-instruction-in-the-user-program-s7-1500)

### High_Speed_Counter instruction (S7-1500)

#### High_Speed_Counter

The High_Speed_Counter instruction is part of the High_Speed_Counter technology object. It supplies the control and feedback interface of the technology module.

The High_Speed_Counter instruction thereby forms the software interface between the user program and the technology module. It must be called cyclically from the user program in order to synchronize the input and output data.

The High_Speed_Counter instruction can be used equally for the technology modules of the S7-1500, ET 200SP and ET 200eco PN M12-L systems. The modules can be used centrally and decentrally. The instruction applies in each case to the channel of the technology module that was assigned to the associated technology object.

#### Additional information

[Description High_Speed_Counter](High_Speed_Counter%20%28S7-1500%29.md#description-high_speed_counter-s7-1500)

[High_Speed_Counter input parameters](High_Speed_Counter%20%28S7-1500%29.md#high_speed_counter-input-parameters-s7-1500)

[High_Speed_Counter output parameters](High_Speed_Counter%20%28S7-1500%29.md#high_speed_counter-output-parameters-s7-1500)

[Error codes of parameter ErrorID](High_Speed_Counter%20%28S7-1500%29.md#error-codes-of-parameter-errorid-s7-1500)

[High_Speed_Counter static variables](High_Speed_Counter%20%28S7-1500%29.md#high_speed_counter-static-variables-s7-1500)

### Call instruction in the user program (S7-1500)

The High_Speed_Counter instruction can be called once for each counter in the cycle or, alternatively, in a time-controlled program. The call is not permitted in an event-controlled interrupt program.

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

## Commissioning the High_Speed_Counter (S7-1500)

This section contains information on the following topics:

- [Commissioning the technology object (S7-1500)](#commissioning-the-technology-object-s7-1500)

### Commissioning the technology object (S7-1500)

A graphic display of the block in the commissioning editor helps you with commissioning and the function test for the technology object. You can change specific parameters of the High_Speed_Counter instruction in CPU/IM online mode and monitor their effects.

#### Requirements

- There is an online connection between STEP 7 (TIA Portal) and the CPU.
- The CPU is in RUN.
- The corresponding High_Speed_Counter instruction is called cyclically from the user program.
- The parameters of the technology object are not overwritten by the user program.

#### Procedure

To open the commissioning editor of a technology object and to simulate a parameter value change, follow these steps:

1. Open the "Technology objects" folder in the project tree.
2. Open the High_Speed_Counter technology object in the project tree.
3. Double-click on the "Commissioning" object.  
   The functions for commissioning the High_Speed_Counter technology object are displayed.
4. In the commissioning dialog, click on the "Monitor all" button.  
   The parameters (online values) of the High_Speed_Counter technology object are loaded and displayed.
5. If the parameter you want to change has a text box, enter the new value there.
6. Select the check box of the parameter.  
   The new parameter value becomes effective and the effects of the change are simulated.

#### Online mode

In online mode, you can modify the following parameters to test the technology object function:

- New counter value (NewCountValue)
- New high counting limit (NewUpperLimit)
- New low counting limit (NewLowerLimit)
- New comparison value 0 (NewReferenceValue0 or NewReferenceValue0_M)
- New comparison value 1 (NewReferenceValue1 or NewReferenceValue1_M)
- New start value (NewStartValue)
- Start and stop counter (SwGate)
- Enable Capture (CaptureEnable)
- Enable synchronization (SyncEnable)
- Acknowledgment of signaled error states (ErrorAck)
- Resetting the status flag (EventAck)

## High_Speed_Counter diagnostics (S7-1500)

This section contains information on the following topics:

- [Monitoring counter values, measured values, DIs and DQs (S7-1500)](#monitoring-counter-values-measured-values-dis-and-dqs-s7-1500)

### Monitoring counter values, measured values, DIs and DQs (S7-1500)

You use the diagnostic functions to monitor the counting and measuring functions.

#### Requirements

- There is an online connection between STEP 7 (TIA Portal) and the CPU.
- The CPU is in RUN.

#### Procedure

To open the display editor for the diagnostic functions, follow these steps:

1. Open the "Technology objects" folder in the project tree.
2. Open the High_Speed_Counter technology object in the project tree.
3. Double-click on the "Diagnostics" object.
4. Click the "Monitor all" button.

#### Display

The following values are read by the technology object from the feedback interface and displayed:

- Event display/diagnostics information
- Signal states of the digital inputs and digital outputs
- Counter value
- Capture value
- Measured value

Additional information on status displays is available in the context-sensitive help for each event in STEP 7 (TIA Portal). When the CPU is in STOP, the status display is not updated.

![Display](images/104871180683_DV_resource.Stream@PNG-en-US.PNG)

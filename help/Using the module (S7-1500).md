---
title: "Using the module (S7-1500)"
package: TFHWCTMenUS
topics: 66
devices: [S7-1500, S7-1500T]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Using the module (S7-1500)

This section contains information on the following topics:

- [Using the technology module (S7-1500)](#using-the-technology-module-s7-1500)
- [Using the digital module (S7-1500)](#using-the-digital-module-s7-1500)
- [Using SIMATIC Drive Controller (S7-1500)](#using-simatic-drive-controller-s7-1500)

## Using the technology module (S7-1500)

This section contains information on the following topics:

- [Convention (S7-1500)](#convention-s7-1500)
- [Configuring a module (S7-1500)](#configuring-a-module-s7-1500)
- [Online & diagnostics module (S7-1500)](#online-diagnostics-module-s7-1500)
- [Control and feedback interface (TM Count, TM PosInput) (S7-1500)](#control-and-feedback-interface-tm-count-tm-posinput-s7-1500)

### Convention (S7-1500)

**Technology module**: We use the term "technology module" in this documentation both for the technology modules TM Count and TM PosInput and the technology component of the compact CPUs.

### Configuring a module (S7-1500)

This section contains information on the following topics:

- [Adding a technology module for hardware configuration (TM Count and TM PosInput) (S7-1500)](#adding-a-technology-module-for-hardware-configuration-tm-count-and-tm-posinput-s7-1500)
- [Adding a technology module to hardware configuration (Compact CPU) (S7-1500)](#adding-a-technology-module-to-hardware-configuration-compact-cpu-s7-1500)
- [Adding a technology module to the hardware configuration (ET 200eco PN TM PosInput 2) (S7-1500)](#adding-a-technology-module-to-the-hardware-configuration-et-200eco-pn-tm-posinput-2-s7-1500)
- [Open hardware configuration (S7-1500)](#open-hardware-configuration-s7-1500)
- [Parameter assignment options (S7-1500)](#parameter-assignment-options-s7-1500)
- [Basic parameters (S7-1500)](#basic-parameters-s7-1500)
- [Additional parameters for Compact CPU (S7-1500)](#additional-parameters-for-compact-cpu-s7-1500)
- [Manual operation (incremental or pulse encoder) (S7-1500)](#manual-operation-incremental-or-pulse-encoder-s7-1500)
- [Manual operation (SSI absolute encoder) (S7-1500)](#manual-operation-ssi-absolute-encoder-s7-1500)
- [Fast Mode (incremental or pulse encoder) (S7-1500)](#fast-mode-incremental-or-pulse-encoder-s7-1500)
- [Fast Mode (SSI absolute encoder) (S7-1500)](#fast-mode-ssi-absolute-encoder-s7-1500)

#### Adding a technology module for hardware configuration (TM Count and TM PosInput) (S7-1500)

##### Requirement

- The project has been created.
- The CPU S7-1500 has been created.
- At decentralized operation a distributed I/O ET 200 is created.

##### Procedure

To add a technology module to the hardware configuration, proceed as follows:

1. Open the device configuration of the CPU or IM.
2. Select a module rack.
3. Select the technology module from the module catalog:  
   "Technology module > Counting or Position input > Technology module > Article number"
4. Drag the technology module to the required slot in the module rack.

#### Adding a technology module to hardware configuration (Compact CPU) (S7-1500)

##### Requirement

The project has been created.

##### Procedure

To add a Compact CPU to the project tree, follow these steps:

1. Double-click "Add new device".   
   The "Add new object" dialog opens.
2. Select Controller".
3. Select the Compact CPU:  
   "SIMATIC S7‑1500 > CPU > Compact CPU > Article number"
4. Confirm with "OK".

##### Result

The new Compact CPU is displayed with the following objects in the project tree. Double-click to open the required editor.

![Result](images/104898154123_DV_resource.Stream@PNG-en-US.png)

|  | Object | Description |
| --- | --- | --- |
| ① | [Device configuration](#basic-parameters-s7-1500) | In the Inspector window (per channel):  - [Activation of the counter](#general-s7-1500) - [Assign signals to inputs and outputs](#hardware-inputsoutputs-s7-1500) - [Setting the reaction to CPU STOP](#reaction-to-cpu-stop-s7-1500) - [Enable diagnostic interrupts](#diagnostics-interrupts-compact-cpu-s7-1500) - [Setting the operating mode](#operating-mode-s7-1500) - [Enable hardware interrupts](#hardware-interrupts-s7-1500) - Setting the module addresses |
| ② | [Online & Diagnostics](#displaying-and-evaluating-diagnostics-s7-1500) | - Hardware diagnostics - Obtain information about the Compact CPU - Run firmware update |

#### Adding a technology module to the hardware configuration (ET 200eco PN TM PosInput 2) (S7-1500)

##### Requirement

- The project has been created.
- The CPU S7-1500 has been created.

##### Procedure

To add a technology module to the hardware configuration, proceed as follows:

1. Open the device configuration of the CPU.
2. Select the network view.
3. Select the technology module from the hardware catalog:  
   "Distributed I/O systems > ET 200eco PN > Interface modules > Technology modules > Position detection > Module > Article number"
4. Drag-and-drop the technology module to the required location in the network view.

#### Open hardware configuration (S7-1500)

##### Procedure

1. Open the device configuration of the CPU or IM.
2. Select the device view.
3. Click on the module.

#### Parameter assignment options (S7-1500)

##### Counting, measuring and position input with SSI absolute encoder

For the counting and measuring function as well as the position input with an SSI absolute encoder, you have the following alternatives for parameter assignment and control of the technology module:

- Configuration of a technology object and control using the related instruction:

  When using an incremental or pulse encoder, we recommend the simple configuration with graphic support using thee High_Speed_Counter technology object. A detailed description of this configuration can be found in section Technology Object High_Speed_Counter.

  When using an SSI absolute value encoder, we recommend the simple configuration with graphic support using the SSI_Absolute_Encoder technology object. A detailed description of this configuration can be found in section Technology Object High_Speed_Counter.

  For configuration of a technology object, select the [operating mode](#operating-mode-s7-1500) "Operating with "Counting and measurement" technology object".
- Parameter setting via hardware configuration and control via the control and feedback interface of the technology module:

  Select the [operating mode](#operating-mode-s7-1500) "Manual operation (without technology object)" for this.

  A description of the control and feedback interface for TM Count and TM PosInput is available in the following sections:

  [Assignment of the control interface](#assignment-of-the-control-interface-s7-1500)

  [Assignment of the feedback interface](#assignment-of-the-feedback-interface-s7-1500)
- Parameter settings via GSD file and control via the control and feedback interface of the technology module.

  A description of the control and feedback interface for TM Count and TM PosInput is available in the following sections:

  [Assignment of the control interface](#assignment-of-the-control-interface-s7-1500)

  [Assignment of the feedback interface](#assignment-of-the-feedback-interface-s7-1500)

##### Position input for Motion Control

Alternatively, you have the option of using the technology module for position input for Motion Control.

Select the [operating mode](#operating-mode-s7-1500) "Position input for "Motion Control" technology object" and assign the parameters of the encoder using the [module parameters](#module-parameters-position-input-for-motion-control-s7-1500) in the device configuration of the technology module. You perform the rest of the configuration of this application using an axis technology object of S7-1500 Motion Control .

#### Basic parameters (S7-1500)

This section contains information on the following topics:

- [Activate channel (ET 200eco PN TM PosInput 2) (S7-1500)](#activate-channel-et-200eco-pn-tm-posinput-2-s7-1500)
- [Reaction to CPU STOP (S7-1500)](#reaction-to-cpu-stop-s7-1500)
- [Diagnostic interrupts (TM Count and TM PosInput) (S7-1500)](#diagnostic-interrupts-tm-count-and-tm-posinput-s7-1500)
- [Diagnostics interrupts (Compact CPU) (S7-1500)](#diagnostics-interrupts-compact-cpu-s7-1500)
- [Operating mode (S7-1500)](#operating-mode-s7-1500)
- [Module parameters (position input for Motion Control) (S7-1500)](#module-parameters-position-input-for-motion-control-s7-1500)
- [Hardware interrupts (S7-1500)](#hardware-interrupts-s7-1500)

##### Activate channel (ET 200eco PN TM PosInput 2) (S7-1500)

**Channel 0/Channel 1**

With this parameter, you specify whether the respective channel is used:

| Option | Meaning |
| --- | --- |
| Deactivated | The channel is not used. The channel cannot trigger any alarms. No addresses are allocated for the channel. |
| Enabled  (default) | The channel is used. Addresses for the control and feedback interface of the channel are allocated. |

> **Note**
>
> You must use at least one channel.

##### Reaction to CPU STOP (S7-1500)

**Reaction to CPU STOP**

You set the response of the technology module for each channel to CPU STOP in the basic parameters of the device configuration.

| Option | Meaning |
| --- | --- |
| Continue operation | The technology module remains fully functional. Incoming count pulses are processed or the actual position is read. The digital outputs continue to switch according to the parameter assignment. |
| Output substitute value | The technology module outputs the configured substitute values at the digital outputs until the next CPU STOP-RUN transition.   The technology module is returned to its startup state after a STOP-RUN transition: The counter value is set to the Start value (with incremental encoders or pulse encoders) and the digital outputs switch according to the parameter assignment. |
| Keep last value | The technology module outputs the values at the digital outputs that were valid when the transition to STOP took place until the next CPU STOP-RUN transition.   If a digital output with the function "In case of comparison value for a pulse duration" is set at CPU stop, the digital output is reset after expiry of pulse duration.  The technology module is returned to its startup state after a STOP-RUN transition: The counter value is set to the Start value (with incremental encoders or pulse encoders) and the digital outputs switch according to the parameter assignment. |

**Substitute value for DQ0**
 **(TM Count und TM PosInput)**

This parameter lets you specify which value the technology module is to output to the digital output DQ0 in the event of a CPU STOP under "Output substitute value".

> **Note**
>
> In operating mode "Operating with "Counting and measurement" technology object", you assign this parameter using the technology object.

**Substitute value for DQ0**
 **(Compact CPU)**

You can use this parameter to specify the value to be output for a STOP of the Compact CPU in the feedback interface for DQ0 in the context of the "Substitute value for DQ0" behavior.

> **Note**
>
> In operating mode "Operating with "Counting and measurement" technology object", you assign this parameter using the technology object.

**Substitute value for DQ1**

This parameter lets you specify which value the technology module is to output to the digital output DQ1 in the event of a CPU STOP under "Output substitute value".

> **Note**
>
> In operating mode "Operating with "Counting and measurement" technology object", you assign this parameter using the technology object.

##### Diagnostic interrupts (TM Count and TM PosInput) (S7-1500)

The technology module can trigger additional diagnostic interrupts when you enable the diagnostic interrupts in the basic parameters. These diagnostic interrupts are processed in an interrupt OB.

Detailed information on the error event is available in the error organization block with the instruction "RALRM" (read alarm supplementary information) and in the [Diagnostics function manual](https://support.industry.siemens.com/cs/ww/en/view/59192926), section "System diagnostics by means of the user program".

**Enable diagnostic interrupt on wire break**

You use this parameter to specify whether a diagnostic interrupt is to be triggered in the event of wire breaks of the utilized signals for the following encoders:

- Push-pull [24 V encoder](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#24-v-or-ttl-count-signals-s7-1500)
- [RS422 encoder](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#rs422-count-signals-s7-1500) (additionally monitored for short-circuits and incorrect supply voltage)
- [SSI absolute encoder](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#ssi-signals-s7-1500) (additionally monitored for short-circuits and incorrect supply voltage)

> **Note**
>
> If you use an encoder with a different sensor type or interface standard, wire break cannot be detected.

**Enable additional diagnostic interrupts**

You use this parameter to specify whether diagnostic interrupts are to be triggered for additional errors.

See the device manual for the technology module to find out which errors during operation can trigger a diagnostic interrupt.

##### Diagnostics interrupts (Compact CPU) (S7-1500)

**Enable diagnostic interrupts**

A Compact CPU can trigger diagnostic interrupts for certain faults if you have enabled diagnostic interrupts. These diagnostic interrupts are processed in an interrupt OB.

You use this parameter to determine if the Compact CPU should trigger diagnostic interrupts when a given error occurs.

See the device manual for the Compact CPU to find out which errors can trigger a diagnostic interrupt during operation. The diagnostic interrupts are not enabled in the default setting.

##### Operating mode (S7-1500)

**Selection of the operating mode**
**for the channel**

This setting defines how the channel counting and measuring functions are to be configured and controlled.

| Operating mode | Description |
| --- | --- |
| Operating with "Counting and measurement" technology object | A technology object is used for the parameter assignment of the channel.   The related instruction for the technology object in the user program provides the access to the control and feedback interfaces of the technology module.  You specify the assignment between the technology module/channel and technology object in the basic parameters of the technology object. |
| Position input for "Motion Control" technology object | The technology module is used for position input for a higher-level Motion Control controller. This operating mode affects all channels of the technology module for TM Count and TM PosInput. Setting the operating mode only affects the given channel of the Compact CPU.   Parameter assignment is implemented via the Device configuration of the technology module. Parameter assignment of the encoder signals is implemented by means of the [Module parameters](#module-parameters-position-input-for-motion-control-s7-1500). |
| Manual operation (without technology object) | Parameter assignment of the channel is effected via the hardware configuration of the technology module:   - [Manual operation (incremental or pulse encoder)](#manual-operation-incremental-or-pulse-encoder-s7-1500) - [Manual operation (SSI absolute encoder)](#manual-operation-ssi-absolute-encoder-s7-1500)   You have direct access to the control and feedback interface of the channel through the user program. |
| Fast Mode | The technology module is used for very fast acquisition of the counter value or position value. No control interface is available. The parameter setting (hardware configuration) of the module is used for the parameter assignment of the channel. You have direct access to the feedback interface of the channel through the user program. |

> **Note**
>
> **GSD file**
>
> When using a GSD file you determine the operating mode via the selection of the module name in the hardware catalog. You can select manual operation or Fast Mode in the process.

**Selection of the operating type for the channel**

You use this parameter in "Manual operation" to specify the main task for which the channel of the technology module is used. This defines the setting options under "Parameters" (hardware configuration).

| Operating mode | Description |
| --- | --- |
| [Counting](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#counting-with-incremental-or-pulse-encoder-s7-1500) / [Position input](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#position-input-with-ssi-absolute-encoder-s7-1500) | The main function of the channel is counting or position input. The comparison functions and hardware interrupts work with the counter value or position value. The measured values are available concurrently. |
| [Measuring](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#measured-value-determination-s7-1500) | The main function of the channel is counting. The [comparison functions](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#switching-at-comparison-values-with-measured-value-as-reference-s7-1500) and hardware interrupts for compare events work with the measured value. The counter value is available concurrently. |

> **Note**
>
> **GSD file**
>
> When using a GSD file, you determine the operating mode via the selection of the module name in the hardware catalog.

##### Module parameters (position input for Motion Control) (S7-1500)

In operating mode "Position input for technology object "Motion Control"", the parameters for the encoder signals of the channel are assigned under "Module parameters". The parameters depend on the encoder used.

> **Note**
>
> You cannot use this operating mode with a GSD file.

**Module parameters**
 **for incremental encoders and pulse encoders**

If you use an incremental or pulse encoder, you need to configure the following parameters for the encoder signals of the channel.

- Signal type
- Invert direction
- Signal evaluation
- Filter frequency
- Sensor type (for TM Count)
- Interface standard (for TM PosInput)
- Signal selection for reference mark 0
- Measuring input
- Encoder type
- Increments per revolution
- Steps per revolution
- Reference speed
- Distance between increments
- Fine-resolution increment distance
- Reference velocity

You can find a description of the first six parameters in section [Counter inputs](#counter-inputs-s7-1500).

**Module parameters**
 **for SSI absolute encoders**

If you use an TM PosInput with an SSI absolute encoder, you need to configure the following parameters for the encoder signals of the channel.

- Signal type
- Invert direction
- Frame length
- Code type
- Transmission rate
- Monoflop time
- Parity
- Bit number LSB of the position value
- Bit number MSB of the position value
- Measuring input
- Encoder type
- Steps per revolution
- Number of revolutions
- Reference speed
- Distance between increments
- Reference velocity

You can find additional information on the first new parameters in section [Counter inputs](#counter-inputs-s7-1500-1).

**Signal selection for reference mark 0**
 **(**
**TM Count**
 **and** 
**TM PosInput**
**)**

You can use this parameter to specify the external reference signal upon which a new reference mark is saved for the encoder position.

You can select from the following options:

| Option | Meaning |
| --- | --- |
| DI0 | The current counter value is saved as the new encoder position reference mark upon a positive edge at digital input DI0. |
| Signal N of incremental encoder (default) | The current counter value is saved as the new encoder position reference mark upon a positive edge of the signal N of incremental encoder. |

**Signal selection for reference mark 0**
 **(Compact CPU)**

You can use this parameter to specify the external reference signal upon which a new reference mark is saved for the encoder position.

You can select from the following options:

| Option | Meaning |
| --- | --- |
| None | No external reference signal is used. |
| DI0 | The current counter value is saved as the new encoder position reference mark upon a positive edge at digital input DI0. |
| Signal N of incremental encoder (default<sup>1</sup>) | The current counter value is saved as the new encoder position reference mark upon a positive edge of the signal N of incremental encoder. |
| <sup>1</sup>Exceptions: "DI0" is the default for HSC 3 and HSC 6 on the 1511C as well as on the 1512C in compatibility mode |  |

**Measuring input (**
**TM Count**
 **and** 
**TM PosInput**
**)**

The parameter specifies that the hardware digital input DI1 serves as a measuring input. For rising, falling or both edges of the DI1, the current counter value or position value is saved as the current encoder position. The value of the parameter cannot be changed.

**Measuring input (compact CPU)**

This parameter is used to define the hardware input which is used as the external measuring input for saving the encoder position.

You can select from the following options:

| Option | Meaning |
| --- | --- |
| None (default) | No external measuring input is used. |
| DI1 | The hardware digital input DI1 serves as the measuring input. For rising, falling or both edges of the DI1, the current counter value is saved as current encoder position. |

**Increments per revolution**

With this parameter you specify the line count of the incremental and pulse encoder. The line count can be found in the data sheet for the encoder.

**Steps per revolution** 
**(incremental and pulse encoder)**

The parameter specifies the number of count pulses per encode rotation.

The number of count pulses depends on the increment per rotation and the parameterized signal evaluation.

**Example:**

Your incremental or pulse encoder delivers 2048 increments per revolution. Depending on the signal evaluation the following value is displayed:

| Signal evaluation | Steps per revolution |
| --- | --- |
| Single | 2048 |
| Double | 4096 |
| Quadruple | 8192 |

**Steps per revolution** 
**(SSI absolute encoder)**

With this parameter you define the number of increments the SSI absolute encoder supplies per revolution.

**Number of revolutions**

The parameter specifies how many rotations the value range of the SSI absolute encoder encompasses.

The value is calculated from the parameterized values for the bit numbers LSB and MSB of the position value as well as the steps per revolution.

**Reference speed**

The encoder transmits the process value of the speed as a percentage of the reference speed. This parameter defines the speed in rpm which is to be correspond to the value 100 % . The reference speed must be identical to the setting in the controller.

You can enter a value between 6.00 and 210000.00. The default setting is "3000.00 rpm".

**Encoder type**

You can use this parameter to specify whether the encoder records linear or rotatory movements. The encoder type must be identical to the setting in the controller.

The default setting is "Rotary".

**Distance between increments**

You can use this parameter to specify the distance between two increments of the encoder in nm.

The value must be identical to the setting in the controller.

**Fine-resolution increment distance**

The parameter specifies the distance between two count pulses in nm.

The value depends on the distance between two increments and the configured signal evaluation.

**Example:**

Your incremental or pulse encoder has an incremental distance of 16000 nm. Depending on the signal evaluation the following value is displayed:

| Signal evaluation | Fine-resolution increment distance |
| --- | --- |
| Single | 16000.00 nm |
| Double | 8000.00 nm |
| Quadruple | 4000.00 nm |

**Reference velocity**

The encoder transmits the process value of the velocity as a percentage of the reference velocity. This parameter defines the velocity in m/min which corresponds to a value of 100%.

You can enter a value between 0.60 and 600.00. The default setting is "16.00 m/min".

**Further configuring**

You can perform the further configuration by using an axis or measuring input technology object of S7-1500 Motion Control . See the [S7-1500 Motion Control](https://support.industry.siemens.com/cs/ww/en/view/59381279) and [S7-1500T Motion Control](https://support.industry.siemens.com/cs/ww/en/view/109481326) function manuals for further details on configuring and commissioning position input and the measuring input technology object.

**See also**

[Position detection for Motion Control](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#position-detection-for-motion-control-s7-1500)

##### Hardware interrupts (S7-1500)

You can set for each channel the events which are to trigger a hardware interrupt during operation when assigning the basic parameters of the technology module.

In an S7‑1500 system, you enter a matching event name for each enabled hardware interrupt and assign a corresponding hardware interrupt OB to each hardware interrupt. If a hardware interrupt is triggered, the corresponding OB is started to evaluate the hardware interrupt data.

> **Note**
>
> In the following cases you can only release only one hardware interrupt per module.
>
> - Distributed operation with an S7-300/400 CPU
> - Use of a GSD file
>
> You cannot release a hardware interrupt in the following cases:
>
> - Distributed operation with ET 200eco PN M12-L

A hardware interrupt is triggered if the condition for changing the respective status bit or event bit in the feedback interface is fulfilled.

**Lost hardware interrupt**

If the hardware interrupts are triggered more quickly by the system than they can be acknowledged, hardware interrupts are lost and the "Hardware interrupt" diagnostic interrupt is signaled.

**Hardware interrupts that can be activated**

| Hardware interrupt | Available in counting mode using |  | Available in measuring mode using |  | Available in operating mode Position input for "Motion Control" technology object | Description | Event Type number |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Incremental or pulse encoder | SSI absolute encoder | Incremental or pulse encoder | SSI absolute encoder |  |  |  |  |
| New Capture value available | Yes | Yes | No | No | No | Hardware interrupt when current counter value or position value is saved as Capture value | 1000<sub>B</sub> |
| Synchronization of the counter by an external signal | Yes | No | Yes | No | No | Hardware interrupt upon synchronization of the counter by signal N or DI edge | 1001<sub>B</sub> |
| Gate start | Yes | No | Yes | No | No | Hardware interrupt when internal gate opens | 0001<sub>B</sub> |
| Gate stop | Yes | No | Yes | No | No | Hardware interrupt when internal gate closes | 0010<sub>B</sub> |
| Overflow (high counting limit violated) | Based on counter value | No | Based on counter value | No | No | Hardware interrupt when counter value exceeds high counting limit | 0011<sub>B</sub> |
| Underflow (low counting limit violated) | Based on counter value | No | Based on counter value | No | No | Hardware interrupt when counter value falls below low counting limit | 0100<sub>B</sub> |
| Change of direction<sup>1</sup> | Based on counter value | Based on position value | Based on counter value | Based on position value | No | Hardware interrupt when counter value or position value changes direction | 1010<sub>B</sub> |
| Zero crossing | Based on counter value | Based on position value | Based on counter value | Based on position value | No | Hardware interrupt with zero crossing of counter value or position value | 0111<sub>B</sub> |
| Comparison event for DQ0 occurred | Based on counter value | Based on position value | Based on measured value | Based on measured value | No | Hardware interrupt when a comparison event for DQ0 occurs as a result of the selected comparison condition.  No hardware interrupt when the change of the counter value for an incremental or pulse encoder was not caused by a count pulse | 0101<sub>B</sub> |
| Comparison event for DQ1 occurred | Based on counter value | Based on position value | Based on measured value | Based on measured value | No | Hardware interrupt when a comparison event for DQ1 occurs as a result of the selected comparison condition.  No hardware interrupt when the change of the counter value for an incremental or pulse encoder was not caused by a count pulse | 0110<sub>B</sub> |
| <sup>1</sup> The STS_DIR feedback bit has a default of "0". A hardware interrupt is not triggered when the first change to the counter value or position value immediately after the technology module is switched on is in the down direction. |  |  |  |  |  |  |  |

**Default setting**

No hardware interrupts are enabled in the default setting.

#### Additional parameters for Compact CPU (S7-1500)

This section contains information on the following topics:

- [Introduction (S7-1500)](#introduction-s7-1500)
- [Compatibility 1511C (high-speed counters of Compact CPU 1512C-1 PN) (S7-1500)](#compatibility-1511c-high-speed-counters-of-compact-cpu-1512c-1-pn-s7-1500)
- [General (S7-1500)](#general-s7-1500)
- [Hardware inputs/outputs (S7-1500)](#hardware-inputsoutputs-s7-1500)

##### Introduction (S7-1500)

When using a Compact CPU, the following parameters are additionally available for the signals of the high-speed counter.

##### Compatibility 1511C (high-speed counters of Compact CPU 1512C-1 PN) (S7-1500)

**Front connector assignment same as CPU 1511C**

You can use this parameter to specify if the pin assignment for the front connector of the CPU 1511C‑1 PN is to be used for the high-speed counter of the CPU 1512C-1 PN:

| Option | Meaning |
| --- | --- |
| Disabled (default) | CPU 1512C‑1 PN uses the pin assignment of the onboard front connector. 1512C-1 PN supports the use of the connections of both front connectors of the digital onboard I/Os for the high-speed counter. The assignment of hardware inputs and outputs for the HSC channels is described in the CPU 1512C‑1 PN manual. |
| Enabled | CPU 1512C‑1 PN uses the pin assignment of the front connector of the CPU 1511C‑1 PN. 1511C-1 PN supports the use of the connections of the first front connector of the digital onboard I/Os for the high-speed counter. The assignment of hardware inputs and outputs for the HSC channels is described in the CPU 1511C‑1 PN manual. |

##### General (S7-1500)

**Activate this high-speed counter**

You can use this parameter to specify whether the respective high speed counter is to be used:

| Option | Meaning |
| --- | --- |
| Disabled (default) | The high-speed counter is not used. The counter uses no connections of the onboard front connector and can not trigger interrupts. Writing to its control interface is ignored and its feedback interface returns zero values. |
| Enabled | The high-speed counter is used. The assignment of HSC addresses to the connections of the onboard front connector is described in the device manual of the Compact CPU. |

##### Hardware inputs/outputs (S7-1500)

**Clock generator input (A) / Pulse input (A) / Clock generator forward (A)**

This parameter specifies which input is used for the encoder signal A for the respective counter. The value cannot be changed.

**Clock generator input (B) / Pulse input (B) / Clock generator forward (B)**

If you use an encoder with multiple signals for the respective counter, this parameter specifies which input is used for the encoder signal B. The value cannot be changed.

**Reset input (N)**

If you use an incremental encoder for the respective counter, this parameter specifies which input is used for the reset input (encoder signal N). The value cannot be changed.

**HSC DI0 / HSC DI1**

This parameter determines which digital input of the Compact CPU is to be used as the DIm of the counter.

> **Note**
>
> You can configure the input delay for a digital input in the Inspector window of the device configuration under "Properties > DI 16/DQ 16 > Inputs > Channel n".

**HSC DQ0**

You can read the status of the DQ0 via the feedback interface. You cannot assign DQ0 to a physical digital output of the Compact CPU.

**HSC DQ1**

This parameter determines which digital output of the Compact CPU is to be used as DQ1. You can select an output with an output delay of 5 µs or 500 µs.

You can find an overview of the output delay for all digital outputs in the device manual of the Compact CPU.

#### Manual operation (incremental or pulse encoder) (S7-1500)

This section contains information on the following topics:

- [Counter inputs (S7-1500)](#counter-inputs-s7-1500)
- [Counting limits and start value (S7-1500)](#counting-limits-and-start-value-s7-1500)
- [Counter behavior at limits and gate start (S7-1500)](#counter-behavior-at-limits-and-gate-start-s7-1500)
- [Behavior of a DI (S7-1500)](#behavior-of-a-di-s7-1500)
- [Behavior of a DQ (S7-1500)](#behavior-of-a-dq-s7-1500)
- [Specifying the measured value (S7-1500)](#specifying-the-measured-value-s7-1500)

##### Counter inputs (S7-1500)

**Signal type**

You can choose from the following [signal types](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#encoder-signals-s7-1500):

| Signal type | Meaning | Additional option-specific parameters |
| --- | --- | --- |
| Incremental encoder (A, B phase-shifted) | An incremental encoder with phase-shifted A and B signals is connected. | - Invert direction - Signal evaluation - Filter frequency - Sensor type or Interface standard |
| Incremental encoder (A, B, N) | An incremental encoder with phase-shifted signals A and B and a zero signal N is connected. | - Invert direction - Signal evaluation - Filter frequency - Sensor type or Interface standard - Reaction to signal N - Frequency of synchronization - Frequency of the Capture function |
| Pulse (A) and direction (B) | A pulse encoder (signal A) with direction signal (signal B) is connected. | - Filter frequency - Sensor type or Interface standard |
| Pulse (A) | A pulse encoder (signal A) without direction signal is connected. You can specify the counting direction by means of the [control interface](#assignment-of-the-control-interface-s7-1500). | - Filter frequency - Sensor type or Interface standard |
| Count up (A), count down (B) | Signals for counting up (signal A) and down (signal B) are connected. | - Filter frequency - Sensor type or Interface standard |

**Invert direction**

You can invert the counting direction to adapt it to the process.

The inverting of the direction can be configured and active for the following signal types:

- Incremental encoder (A, B phase-shifted)
- Incremental encoder (A, B, N)

**Signal evaluation**

By configuring [signal evaluation](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#overview-s7-1500), you can specify which edges of the signals are counted.

You can select from the following options:

| Signal evaluation | Meaning |
| --- | --- |
| Single  (default) | The edges of signal A are evaluated during a low level of signal B. |
| Double | Each edge of signal A is evaluated. |
| Quadruple | Each edge of signals A and B is evaluated. |

The parameter can be assigned with the following signal types:

- Incremental encoder (A, B phase-shifted)
- Incremental encoder (A, B, N)

**Filter frequency**

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

**Sensor type**
 **(TM Count)**

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

**Sensor type**
 **(Compact CPU)**

The "Sourcing output" sensor type is set for the Compact CPU and cannot be changed. The encoder or sensor switches the inputs A, B and N to 24V DC.

You can operate both sourcing output encoders and push-pull encoders on the Compact CPU. You can find additional information on the sensor type in the data sheet for the encoder.

**Sensor type**
 **(**
**ET 200eco PN TM PosInput 2**
**)**

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

**Interface standard**
 **(TM PosInput)**

You use this parameter to specify whether the encoder outputs symmetric (RS422) or asymmetric (TTL) signals for the TM PosInput.

You can select from the following options:

| Interface standard | Meaning |
| --- | --- |
| RS422, symmetrical (default) | The encoder outputs symmetric signals according to the [RS422 standard](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#rs422-count-signals-s7-1500). |
| TTL (5 V), asymmetrical | The encoder outputs asymmetric 5 V signals according to the [TTL standard](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#24-v-or-ttl-count-signals-s7-1500). |

> **Note**
>
> The RS422 standard provides greater interference immunity than the TTL standard. Therefore, if your incremental or pulse encoder supports the RS422 **and** the TTL standard, it is recommended to use the RS422 signal standard.

**Interface standard (**
**ET 200eco PN M12-L TM PosInput 2**)

You use this parameter to specify whether the encoder outputs symmetrical (RS422) or asymmetrical (24 V) signals for the ET 200eco PN M12-L TM PosInput 2. You can select from the following options:

| Interface standard | Meaning |
| --- | --- |
| RS422, symmetrical (default) | The encoder outputs symmetric signals according to the [RS422 standard](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#rs422-count-signals-s7-1500). |
| 24 V, asymmetrical | The encoder outputs asymmetric 24 V signals according to the [TTL standard](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#24-v-or-ttl-count-signals-s7-1500). |

**Reaction to signal N**

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
> If "Synchronization at signal N" is selected, you can select the function "Enable synchronization at signal N" for a [digital input](#behavior-of-a-di-s7-1500).

> **Note**
>
> **For High_Speed_Counter as of V3.0, the following applies:**
>
> You can choose "Capture at signal N" only in operating mode "Use count value as reference":

**Frequency of synchronization**

This parameter is used to define the frequency of the following events:

- Synchronization at signal N
- Synchronization as a function of a digital input

You can select from the following options:

| Option | Meaning |
| --- | --- |
| Once (default) | The counter is only set at the first signal N or the first configured edge of the digital input. |
| Periodic | The counter is set at each signal N or each configured edge of the digital input. |

**Frequency of the** 
**Capture**
 **function**

This parameter is used to define the frequency of Capture events for the following functions:

- Capture at Signal N
- Capture as function of a digital input

You can select from the following options:

| Option | Meaning |
| --- | --- |
| Once | The first configured edge at the respective digital input or first rising edge of the N signal saves the current counter value as a Capture value. |
| Periodic (default) | Each configured edge at the respective digital input or each rising edge of the N signal saves the current counter value as a Capture value. |

##### Counting limits and start value (S7-1500)

**High counting limit**

You limit the counting range by setting the high counting limit. You can enter a value up to 2147483647 (2<sup>31</sup>-1). You must enter a value that lies above the low counting limit.

The default setting is "2147483647".

**Low counting limit**

You limit the counting range by setting the low counting limit. You can enter a value up to -2147483648 (-2<sup>31</sup>). You must enter a value below the high counting limit.

The default setting is "-2147483648".

**Start value**

By configuring the start value, you specify the value at which counting is to start and where it is to continue in the case of defined events. You must enter a value between the counting limits or equal to the counting limits.

The default setting is "0".

**Additional information**

For more information, see [Behavior at the counting limits](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#behavior-at-the-counting-limits-s7-1500) and [Counter behavior at gate start](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#counter-behavior-at-gate-start-s7-1500).

##### Counter behavior at limits and gate start (S7-1500)

**Reaction to violation of a counting limit**

You can configure the following characteristics for [violation of a counting limit](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#behavior-at-the-counting-limits-s7-1500):

| Reaction | Meaning |
| --- | --- |
| Stop counting | If a counting limit is violated, counting is stopped and the internal gate is closed. To restart counting, you must also close and reopen the software/hardware gate. |
| Continue counting (default) | Counting continues either with the start value or at the opposite counting limit, depending on the additional parameter assignment. |

**Reset when counting limit is violated**

You can reset the counter to the following values when a counting limit is violated:

| Reset the value | Meaning |
| --- | --- |
| To start value | The counter value is set to the start value. |
| To opposite counting limit (default) | The counter value is set to the opposite counting limit. |

**Reaction to gate start**

You can set the following [Reaction to gate start](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#counter-behavior-at-gate-start-s7-1500):

| Reaction | Meaning |
| --- | --- |
| Set to start value | When the gate is opened, the counter value is set to the start value. |
| Continue with current value (default) | When the gate is opened, counting is continued with the last counter value. |

##### Behavior of a DI (S7-1500)

**Set function of DI**

By configuring a digital input, you specify which functions the digital input triggers at switching.

You can select from the following options:

| Function of a digital input | Meaning | Additional option-specific parameters |
| --- | --- | --- |
| Gate start/stop (level-triggered) | The level at the respective digital input opens and closes the [hardware gate](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#hardware-gate-s7-1500). | - Input delay - Select level |
| Gate start (edge-triggered) | The configured edge at the respective digital input opens the [hardware gate](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#hardware-gate-s7-1500). | - Input delay - Edge selection |
| Gate stop (edge-triggered) | The configured edge at the respective digital input closes the [hardware gate](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#hardware-gate-s7-1500). | - Input delay - Edge selection |
| [Synchronization](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#synchronization-s7-1500) | The configured edge at the respective digital input sets the counter to the start value.  The EVENT_SYNC feedback bit indicates whether a synchronization has occurred. | - Input delay - Edge selection - Frequency of synchronization |
| Enable synchronization at signal N | The active level at the respective digital input enables [synchronization of the counter at signal N](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#synchronization-at-signal-n-s7-1500). | - Input delay - Select level |
| Capture | The configured edge at the respective digital input [saves the current counter value](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#capture-with-incremental-or-pulse-encoder-s7-1500) as a Capture value. The use of a digital input and the use of the N signal are not mutually exclusive for the Capture function.  The CAPTURED_VALUE value in the feedback interface indicates the Capture value. | - Input delay - Edge selection - Frequency of the Capture function - Behavior of counter value after Capture |
| Digital input without function | No technological function is assigned to the respective digital input.  You can read the signal state of the digital input via the respective feedback bit (number of digital inputs depends on the module):  - STS_DI0 - STS_DI1 - STS_DI2 | - Input delay |

> **Note**
>
> With the exception of "Digital input without function", each function can only be used once for each counter, and if used for one digital input is not available to the others.

**Input delay**
 **(TM Count and TM PosInput)**

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
> You configure the input delay under "Behavior of DI0" for all digital inputs together. The input delay is also displayed under "Behavior of DI1" and for TM Count also under "Behavior of DI2".

**Input delay**
 **(Compact CPU)**

You use this parameter to suppress interference at the digital inputs of the DIn signals. Changes to the signal are only detected if they remain stable for longer than the configured input delay time.

You can configure the input delay for a digital input of a Compact CPU in the Inspector window of the device configuration under "Properties > DI 16/DQ 16 > Inputs > Channel n".

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

**Select level**

You use this parameter to specify the level at which the digital input is active.

You can select from the following options:

| Level | Meaning |
| --- | --- |
| Active with high level  (default) | The respective digital input is active when it is set. |
| Active with low level | The respective digital input is active when it is not set. |

The parameter can be set for the following functions of a digital input:

- Gate start/stop (level-triggered)
- Enable synchronization at signal N

**Edge selection**

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

**Frequency of synchronization**

This parameter is used to define the frequency of the following events:

- Synchronization at signal N
- Synchronization as a function of a digital input

You can select from the following options:

| Option | Meaning |
| --- | --- |
| Once (default) | The counter is only set at the first signal N or the first configured edge of the digital input. |
| Periodic | The counter is set at each signal N or each configured edge of the digital input. |

**Frequency of the** 
**Capture**
 **function**

This parameter is used to define the frequency of Capture events for the following functions:

- Capture at Signal N
- Capture as function of a digital input

You can select from the following options:

| Option | Meaning |
| --- | --- |
| Once | The first configured edge at the respective digital input or first rising edge of the N signal saves the current counter value as a Capture value. |
| Periodic (default) | Each configured edge at the respective digital input or each rising edge of the N signal saves the current counter value as a Capture value. |

**Behavior of counter value after** 
**Capture**

You can configure the following characteristics for the counter after a [capture event](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#capture-with-incremental-or-pulse-encoder-s7-1500):

| Reaction | Meaning |
| --- | --- |
| Continue counting (default) | After saving the current counter value as Capture value, counting is continued unchanged. |
| Set to start value and continue counting | After saving the current counter value as Capture value, counting is continued with the start value. |

##### Behavior of a DQ (S7-1500)

###### Set output

With the parameter assignment of a digital output, you specify the condition upon which the digital output switches.

You can select from the following options:

| [Function of a digital output](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#switching-at-comparison-values-with-counter-value-as-reference-s7-1500) in the operating mode "Counting" | Meaning | Additional option-specific parameters |
| --- | --- | --- |
| Between comparison value and high limit (default) | The respective digital output is active if: Comparison value <= counter value <= high counting limit | - Comparison value 0 - Comparison value 1 - Hysteresis (in increments) |
| Between comparison value and low limit | The respective digital output is active if: Low counting limit <= counter value <= comparison value | - Comparison value 0 - Comparison value 1 - Hysteresis (in increments) |
| Between comparison value 0 and 1 | The digital output DQ1 is active if: Comparison value 0 <= counter value <= comparison value 1 | - Comparison value 0 - Comparison value 1 - Count direction - Hysteresis (in increments) |
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

| [Function of a digital output](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#switching-at-comparison-values-with-measured-value-as-reference-s7-1500) in the operating mode "Measuring" | Meaning | Additional option-specific parameters |
| --- | --- | --- |
| Measured value >= comparison value (default) | The respective digital output is active if the measured value is greater than or equal to the comparison value. | - Comparison value 0 - Comparison value 1 |
| Measured value <= comparison value | The respective digital output is active if the measured value is less than or equal to the comparison value. | - Comparison value 0 - Comparison value 1 |
| Between comparison value 0 and 1 | The digital output DQ1 is active if: Comparison value 0 <= measured value <= comparison value 1 | - Comparison value 0 - Comparison value 1 |
| Not between comparison value 0 and 1 | The digital output DQ1 is active if: Comparison value 1 <= measured value <= comparison value 0 | - Comparison value 0 - Comparison value 1 |
| Use by user program | The respective digital output can be switched by the CPU [via the control interface](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#comparison-values-and-outputs-s7-1500). | — |

> **Note**
>
> You can select the "Between comparison value 0 and 1" and "Not between comparison value 0 and 1" functions only for digital output DQ1 and only if you have selected the "Use by user program" function for digital output DQ0.

**Comparison value 0** 
**(TM Count and TM PosInput)**

**Operating mode "**
**Counting**
**":**

With the parameter assignment of the [comparison value](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#switching-at-comparison-values-with-counter-value-as-reference-s7-1500), you specify the counter value at which the digital output DQ0 switches as a result of the selected comparison event.

You must enter an integer (DINT) that is greater than or equal to the low counting limit. If you use the DQ function "Between comparison value 0 and 1", the comparison value 0 has to be smaller than comparison value 1. The default setting is "0".

**Operating mode "**
**Measurement**
**":**

With the parameter assignment of the [comparison value](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#switching-at-comparison-values-with-measured-value-as-reference-s7-1500), you specify the measured value at which the digital output DQ0 switches as a result of the selected comparison event.

You must enter a floating point number (REAL). If you use the DQ function "Between comparison value 0 and 1", the comparison value 0 has to be smaller than comparison value 1. The minimum value is -7.922816 x 10<sup>28</sup>. The default setting is "0.0". The unit of the comparison value depends on the measured variable.

**Comparison value 0** 
**(compact CPU)**

**Operating mode "**
**Counting**
**":**

With the parameter assignment of the [Comparison value](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#switching-at-comparison-values-with-counter-value-as-reference-s7-1500), you specify the counter value at which the STS_DQ0 bit is set in the feedback interface of the selected comparison event. The digital output DQ0 is not available as a physical output in a Compact CPU.

You must enter an integer (DINT) that is greater than or equal to the low counting limit. If you use the DQ function "Between comparison value 0 and 1", the comparison value 0 has to be smaller than comparison value 1. The default setting is "0".

**Operating mode "**
**Measurement**
**":**

With the parameter assignment of the [Comparison value](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#switching-at-comparison-values-with-measured-value-as-reference-s7-1500), you specify the measured value at which the STS_DQ0 bit is set in the feedback interface of the selected comparison event. The digital output DQ0 is not available as a physical output in a Compact CPU.

You must enter a floating point number (REAL). If you use the DQ function "Between comparison value 0 and 1", the comparison value 0 has to be smaller than comparison value 1. The minimum value is -7.922816 x 10<sup>28</sup>. The default setting is "0.0". The unit of the comparison value depends on the measured variable.

**Comparison value 1**

**Operating mode "**
**Counting**
**":**

With the parameter assignment of the [comparison value](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#switching-at-comparison-values-with-counter-value-as-reference-s7-1500), you specify the counter value at which the digital output DQ1 switches as a result of the selected comparison event.

You must enter an integer (DINT) that is less than or equal to the high counting limit. If you use the DQ function "Between comparison value 0 and 1", the comparison value 0 has to be smaller than comparison value 1. The default setting is "10".

**Operating mode "**
**Measurement**
**":**

With the parameter assignment of the [comparison value](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#switching-at-comparison-values-with-measured-value-as-reference-s7-1500), you specify the measured value at which the digital output DQ1 switches as a result of the selected comparison event.

You must enter a floating point number (REAL). If you use the DQ function "Between comparison value 0 and 1", the comparison value 0 has to be smaller than comparison value 1. The maximum value is 7.922816 x 10<sup>28</sup>. The default setting is "10.0". The unit of the comparison value depends on the measured variable.

**Count direction**

You use this parameter to specify the count direction for which the selected function is valid.

You can select from the following options:

| Count direction | Meaning |
| --- | --- |
| In both directions  (default) | The comparison and switching of the respective digital output take place regardless of the count direction. |
| Up | The comparison and switching of the respective digital output only takes place when the counter counts up. |
| Down | The comparison and switching of the respective digital output only takes place when the counter counts down. |

The parameter can be configured for the following functions:

- Between Comparison value 0 and 1 (Operating mode "Counting")
- At comparison value for a pulse duration
- After set command from CPU until comparison value

**Pulse duration**

By configuring the pulse duration for the function "At comparison value for a pulse duration", you specify the number of milliseconds for which the respective digital output is active.

If you enter "0" and the counter value corresponds to the comparison value, the digital output remains active until the next count pulse.

A value from 0.0 to 6553.5 ms is permissible.

The default setting is "500.0", which is equivalent to a pulse duration of 0.5 s.

**Hysteresis (in increments)**

By configuring the [hysteresis](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#hysteresis-with-incremental-or-pulse-encoder-s7-1500), you can define a range around the comparison values. For the functions "Between comparison value and high limit" and "Between comparison value and low limit", the hysteresis also applies at the counter limits. Within the hysteresis range, the digital outputs cannot switch again until the counter value is outside the range.

Choose a small enough hysteresis. When the hysteresis range, starting from the configured comparison value, spans the entire counting range, proper functioning of the comparison values cannot be guaranteed.

Regardless of the hysteresis value, the hysteresis range ends at the low or high counting limit.

If you enter "0", the hysteresis is turned off. You can enter a value between 0 and 255. The default setting is "0".

> **Note**
>
> The hysteresis is only available in operating mode "Counting".

##### Specifying the measured value (S7-1500)

**Measured variable**

This parameter is used to specify the [measured variable](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#measuring-types-s7-1500) to be provided by the technology module. The MEASURED_VALUE value in the feedback interface indicates the measured value.

You can select from the following options:

| Measured variable | Meaning | Additional option-specific parameters |
| --- | --- | --- |
| Frequency (default) | The measured variable shows the number of increments per second. The value is a floating point number (REAL). The unit is Hz. | - Update time |
| Period | The measured variable is the average period between two increments. The value is an integer (DINT). The unit is s. | - Update time |
| Velocity | The measured variable is a velocity.  Examples of a velocity measurement can be found in the explanation of the "Increments per unit" parameter. | - Update time - Time base for velocity measurement - Increments per unit |

**Update time**

By configuring the [update time](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#measuring-intervals-s7-1500) in milliseconds, you can specify the time interval between two measured value updates.

The update time and the [signal type](#counter-inputs-s7-1500) effect the accuracy of the measurement. In the case of update times of at least 100 ms, the effect of the signal type is negligible.

In the case of update times of less than 100 ms, you achieve maximum measurement accuracy using the following signal types:

- Incremental encoder (A, B phase-shifted) with Signal evaluation "Single"
- Incremental encoder (A, B, N) with Signal evaluation "Single"
- Pulse (A) and direction (B)
- Pulse (A)

In the case of other signal types, measurement accuracy depends on the encoder and cable used.

If you enter "0", the measured value is updated once per module-internal cycle. Up to three decimal places can be entered. A value from 0.0 to 25000.0 is permissible. The default setting is "10.0".

**Time base for velocity measurement**

This parameter defines the time base on which the velocity is to be returned.

You can select from the following options:

- 1 ms
- 10 ms
- 100 ms
- 1 s
- 60 s

The default setting is "60 s".

**Increments per unit**

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

#### Manual operation (SSI absolute encoder) (S7-1500)

This section contains information on the following topics:

- [Counter inputs (S7-1500)](#counter-inputs-s7-1500-1)
- [Behavior of a DI (S7-1500)](#behavior-of-a-di-s7-1500-1)
- [Behavior of a DQ (S7-1500)](#behavior-of-a-dq-s7-1500-1)
- [Specifying the measured value (S7-1500)](#specifying-the-measured-value-s7-1500-1)

##### Counter inputs (S7-1500)

**Signal type**

If an SSI absolute encoder with the data signal (Signal ID) and cycle signal (Signal C) is connected, select the [signal type](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#ssi-signals-s7-1500) "Absolute encoder (SSI)".

**Invert direction**

You can use this parameter to invert the values supplied by the SSI absolute encoder. This allows you to adapt the detected direction of the encoder to the motor's direction of rotation.

> **Note**
>
> This parameter acts only on the range from the LSB to the MSB of the position value in the frame.

**Frame length**

With the parameter assignment of the frame length, you specify the number of bits of an SSI frame of the [SSI absolute encoder](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#position-input-with-ssi-absolute-encoder-s7-1500) used. You can find the frame length of your SSI absolute encoder in the data sheet of the encoder. Special bits are also included in the frame length. A parity bit does not count in the frame length.

A frame length of between 10 bits and 40 bits is permitted. The default setting is "13 Bit".

You can find two examples of the SSI frame format at [Examples of the frame format](Using%20technology%20object%20SSI_Absolute_Encoder%20%28S7-1500%29.md#examples-of-the-frame-format-s7-1500).

**Code type**

You use the parameter assignment of the code type to specify whether the encoder supplies Dual code or Gray code.

You can select from the following options:

| Code type | Meaning |
| --- | --- |
| Gray (default) | The gray-coded position value returned by the SSI absolute encoder is converted to dual code. |
| Dual | The value returned by the SSI absolute encoder is not converted. |

**Transmission rate**

With the parameter assignment of the transmission rate, you specify the data transmission rate between the technology module and the SSI absolute encoder.

You can select from the following options:

- 125 kHz (preset)
- 250 kHz
- 500 kHz
- 1 MHz
- 1.5 MHz
- 2 MHz

The maximum transmission rate depends on the cable length and the technical specifications of the SSI absolute encoder. For additional information, refer to the product manual of the TM PosInput and the encoder description.

**Monoflop time**

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

**Parity**

With the parameter assignment of the parity, you specify whether the SSI absolute encoder transfers a parity bit.

If, for example, a 25-bit encoder with parity is assigned, the technology module reads 26 bits. A parity error is reported in the feedback interface by means of the ENC_ERROR bit.

**Bit number LSB of the position value**

This parameter is used to specify the bit number of the LSB (least significant bit) of the position value in the frame of the SSI absolute encoder. In this way you limit the range in the frame that supplies the position value.

The value must be less than the bit number of the MSB of the position value. The difference between the bit numbers of the MSB and the LSB of the position value must be less than 32.

The default setting is "0".

> **Note**
>
> If you have selected the Code type "Gray", only the range from the LSB to the MSB of the position value is converted to binary code.

**Bit number MSB of the position value**

This parameter is used to specify the bit number of the MSB (most significant bit) of the position value in the frame of the SSI absolute encoder. In this way you limit the range in the frame that supplies the position value.

The value must be less than the frame length and higher than the bit number of the LSB of the position value. The difference between the bit numbers of the MSB and the LSB of the position value must be less than 32.

The default setting is "12".

> **Note**
>
> If you have selected the Code type "Gray", only the range from the LSB to the MSB of the position value is converted to binary code.

##### Behavior of a DI (S7-1500)

**Setting function of the DI**

By configuring a digital input, you specify which functions the digital input triggers at switching.

You can select from the following options:

| Function of a digital input | Meaning | Additional option-specific parameters |
| --- | --- | --- |
| [Capture](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#capture-with-ssi-absolute-encoder-s7-1500) | The configured edge at the respective digital input saves the current position value as a Capture value.  The CAPTURED_VALUE feedback bit indicates the capture value.  The function can only be used for one of the two digital inputs. | - Input delay - Edge selection - Frequency of the Capture function |
| Digital input without function | No technological function is assigned to the respective digital input.   You can read the signal state of the digital input via the respective feedback bit:  - STS_DI0 - STS_DI1 | - Input delay |

> **Note**
>
> You can choose the "Capture" function only in operating mode "Use position value (SSI absolute value) as reference".

Input delay

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

**Edge selection**

You can use this parameter to specify the edge of the digital input at which the configured function is triggered for the "Capture" function.

You can select from the following options:

- At rising edge (default)
- At falling edge
- At rising and falling edge

**Frequency of the** 
**Capture**
 **function**

This parameter is used to define the frequency of [Capture events](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#capture-with-ssi-absolute-encoder-s7-1500):

You can select from the following options:

| Option | Meaning |
| --- | --- |
| Once | The first configured edge at the respective digital input saves the current counter value as Capture value. |
| Periodic (default) | Each configured edge at the respective digital input saves the current counter value as a Capture value. |

##### Behavior of a DQ (S7-1500)

**Set output**

With the parameter assignment of a digital output, you specify the condition upon which the digital output switches.

You can select from the following options depending on the operating mode:

| [Function of a digital output](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#switching-at-comparison-values-with-position-value-ssi-absolute-value-as-reference-s7-1500) in the operating mode "Position input" | Meaning | Additional option-specific parameters |
| --- | --- | --- |
| Between comparison value and high limit (default) | The respective digital output is active if: Comparison value <= position value <= maximum position value | - Comparison value 0 - Comparison value 1 - Hysteresis (in increments) |
| Between comparison value and low limit | The respective digital output is active if: Minimum position value <= Position value <= Comparison value | - Comparison value 0 - Comparison value 1 - Hysteresis (in increments) |
| Between comparison value 0 and 1 | The digital output DQ1 is active if: Comparison value 0 <= position value <= comparison value 1 | - Comparison value 0 - Comparison value 1 - Count direction - Hysteresis (in increments) |
| At comparison value for a pulse duration | The respective digital output is active once for the assigned time and direction of the position value change when the position value is equal to the comparison value or has fallen below or exceeded it. | - Comparison value 0 - Comparison value 1 - Count direction - Pulse duration - Hysteresis (in increments) |
| After set command from CPU until comparison value | When a set command is sent from the CPU, the respective digital output is active for the assigned direction of the position value change until the position value is equal to the comparison value or has fallen below or exceeded it. | - Comparison value 0 - Comparison value 1 - Count direction - Hysteresis (in increments) |
| Use by user program | The respective digital output can be switched by the CPU [via the control interface](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#comparison-values-and-outputs-s7-1500). | — |

> **Note**
>
> You can only select the "Between comparison value 0 and 1" function for digital output DQ1 and only if you have selected the "Use by user program" function for digital output DQ0.

| [Function of a digital output](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#switching-at-comparison-values-with-measured-value-as-reference-s7-1500) in the operating mode "Measuring" | Meaning | Additional option-specific parameters |
| --- | --- | --- |
| Measured value >= comparison value (default) | The respective digital output is active if the measured value is greater than or equal to the comparison value. | - Comparison value 0 - Comparison value 1 |
| Measured value <= comparison value | The respective digital output is active if the measured value is less than or equal to the comparison value. | - Comparison value 0 - Comparison value 1 |
| Between comparison value 0 and 1 | The digital output DQ1 is active if: Comparison value 0 <= measured value <= comparison value 1 | - Comparison value 0 - Comparison value 1 |
| Not between comparison value 0 and 1 | The digital output DQ1 is active if: Comparison value 1 <= measured value <= comparison value 0 | - Comparison value 0 - Comparison value 1 |
| Use by user program | The respective digital output can be switched by the CPU [via the control interface](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#comparison-values-and-outputs-s7-1500). | — |

> **Note**
>
> You can select the "Between comparison value 0 and 1" and "Not between comparison value 0 and 1" functions only for digital output DQ1 and only if you have selected the "Use by user program" function for digital output DQ0.

**Comparison value 0**

**Operating mode "Position input":**

With the parameter assignment of the [comparison value](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#switching-at-comparison-values-with-position-value-ssi-absolute-value-as-reference-s7-1500), you specify the position value at which the digital output DQ0 switches as a result of the selected comparison event.

If you use an SSI absolute encoder with a position value length of up to 31 bits, you must enter a positive integer (DINT) with a value between 0 and 2<sup>(MSB-LSB+1)</sup>-1. If you use an SSI absolute encoder with a position value length of 32 bits, you must enter a signed integer (DINT) with a value between -2147483648 and 2147483647.

If you use the DQ function "Between comparison value 0 and 1", the comparison value 0 has to be smaller than comparison value 1. The default setting is "0".

**Operating mode "Measurement":**

With the parameter assignment of the [comparison value](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#switching-at-comparison-values-with-measured-value-as-reference-s7-1500), you specify the measured value at which the digital output DQ0 switches as a result of the selected comparison event.

You must enter a floating point number (REAL). If you use the DQ function "Between comparison value 0 and 1", the comparison value 0 has to be smaller than comparison value 1. The minimum value is -7.922816 x 10<sup>28</sup>. The default setting is "0.0". The unit of the comparison value depends on the measured variable.

**Comparison value 1**

**Operating mode "**
**Position input**
**"**

With the parameter assignment of the [comparison value](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#switching-at-comparison-values-with-position-value-ssi-absolute-value-as-reference-s7-1500), you specify the position value at which the digital output DQ1 switches as a result of the selected comparison event.

If you use an SSI absolute encoder with a position value length of up to 31 bits, you must enter a positive integer (DINT) with a value between 0 and 2<sup>(MSB-LSB+1)</sup>-1. If you use an SSI absolute encoder with a position value length of 32 bits, you must enter a signed integer (DINT) with a value between -2147483648 and 2147483647.

If you use the DQ function "Between comparison value 0 and 1", the comparison value 0 has to be smaller than comparison value 1. The default setting is "10".

**Operating mode "Measurement"**

With the parameter assignment of the [comparison value](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#switching-at-comparison-values-with-measured-value-as-reference-s7-1500), you specify the measured value at which the digital output DQ1 switches as a result of the selected comparison event.

You must enter a floating point number (REAL). If you use the DQ function "Between comparison value 0 and 1", the comparison value 0 has to be smaller than comparison value 1. The maximum value is 7.922816 x 10<sup>28</sup>. The default setting is "10.0". The unit of the comparison value depends on the measured variable.

**Count direction**

You use this parameter to specify the direction of position value change for which the selected function is valid.

You can select from the following options:

| Direction of position value change | Meaning |
| --- | --- |
| In both directions  (default) | The comparison and switching of the respective digital output is carried out regardless of whether the position value increases of decreases. |
| Up | The comparison and switching of the respective digital output only takes place when the position value increases. |
| Down | The comparison and switching of the respective digital output only takes place when the position value decreases. |

The parameter can be configured for the following functions:

- Between comparison value 0 and 1 (operating mode "Position input")
- At comparison value for a pulse duration
- After set command from CPU until comparison value

**Pulse duration**

By configuring the pulse duration for the function "At comparison value for a pulse duration", you specify the number of milliseconds for which the respective digital output is active.

A value from 0.1 to 6553.5 ms is permissible.

The default setting is "500.0", which is equivalent to a pulse duration of 0.5 s.

**Hysteresis (in increments)**

By configuring the [hysteresis](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#hysteresis-with-ssi-absolute-encoder-s7-1500), you can define a range around the comparison values. For the functions "Between comparison value and high limit" and "Between comparison value and low limit", the hysteresis also applies at the counter limits. Within the hysteresis range, the digital outputs cannot switch again until the position value has left this range once.

Choose a small enough hysteresis. When the hysteresis range, starting from the configured comparison value, spans the entire position value range, proper functioning of the comparison values cannot be guaranteed.

Regardless of the hysteresis value, the hysteresis range ends at the low or high counting limit.

If you enter "0", the hysteresis is turned off. You can enter a value between 0 and 255. The default setting is "0".

> **Note**
>
> The hysteresis is only available in "Position input" operating mode.

##### Specifying the measured value (S7-1500)

**Measured variable**

With this parameter you specify whether the technology module is to provide a certain [measured variable](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#measuring-types-s7-1500) or the complete SSI frame.

You can select from the following options:

| Option | Meaning | Additional option-specific parameters |
| --- | --- | --- |
| Frequency (default) | The measured variable shows the number of increments per second, where each increment corresponds to one position value change. The value is a floating point number (REAL). The unit is Hz.   The MEASURED_VALUE value in the feedback interface indicates the measured value. | - Update time |
| Period | The measured variable is the average period between two increments of the position value. The value is an integer (DINT). The unit is s.  The MEASURED_VALUE value in the feedback interface indicates the measured value. | - Update time |
| Velocity | The measured variable is a velocity.  Examples of a velocity measurement can be found in the explanation of the "Increments per unit" parameter.  The MEASURED_VALUE value in the feedback interface indicates the measured value. | - Update time - Time base for velocity measurement - Increments per unit |
| Complete SSI frame | Instead of a measured variable, the first 32 bits of the SSI frame are returned (bit 0 to bit 31). In so doing, special bits that do not belong to the position information are also supplied. A configured inversion of the direction is ignored.  The MEASURED_VALUE value in the feedback interface indicates the 32 bits.  You can find examples under [Examples of the frame format](Using%20technology%20object%20SSI_Absolute_Encoder%20%28S7-1500%29.md#examples-of-the-frame-format-s7-1500). This option is only available in operating mode "Use position value (SSI absolute value) as reference". | — |

> **Note**
>
> If the increment per revolution is required for calculation of the measured values, it is automatically calculated from the parameterized telegram length as the power of 2, e.g. 8192 increments per revolution with a telegram length of 13 bit. If you are using an SSI absolute encoder whose increment per revolution does not correspond to the power of 2, the calculated measured value may be incorrect for a short time.

**Update time**

By configuring the [update time](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#measuring-intervals-s7-1500) in milliseconds, you can specify the time interval between two measured value updates. Unsteady measured variables can be smoothed through longer update times

If you enter "0", the measured value is updated once per module-internal cycle. Up to three decimal places can be entered. A value from 0.0 to 25000.0 is permissible. The default setting is "10.0".

**Time base for velocity measurement**

This parameter defines the time base on which the velocity is to be returned.

You can select from the following options:

- 1 ms
- 10 ms
- 100 ms
- 1 s
- 60 s

The default setting is "60 s".

**Increments per unit**

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

#### Fast Mode (incremental or pulse encoder)  (S7-1500)

This section contains information on the following topics:

- [Counter inputs (S7-1500)](#counter-inputs-s7-1500-2)
- [Counting limits and start value (S7-1500)](#counting-limits-and-start-value-s7-1500-1)
- [Counter behavior at limits and gate start (S7-1500)](#counter-behavior-at-limits-and-gate-start-s7-1500-1)
- [Behavior of a DI (S7-1500)](#behavior-of-a-di-s7-1500-2)
- [Behavior of a DQ (S7-1500)](#behavior-of-a-dq-s7-1500-2)

##### Counter inputs (S7-1500)

**Signal type**

You can choose from the following [signal types](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#encoder-signals-s7-1500):

| Signal type | Meaning | Additional option-specific parameters |
| --- | --- | --- |
| Incremental encoder (A, B phase-shifted) | An incremental encoder with phase-shifted A and B signals is connected. | - Invert direction - Signal evaluation - Filter frequency - Sensor type or Interface standard |
| Incremental encoder (A, B, N) | An incremental encoder with phase-shifted signals A and B and a zero signal N is connected. | - Invert direction - Signal evaluation - Filter frequency - Sensor type or Interface standard - Reaction to signal N - Frequency of synchronization - Count direction for synchronization |
| Pulse (A) and direction (B) | A pulse encoder (signal A) with direction signal (signal B) is connected. | - Filter frequency - Sensor type or Interface standard |
| Pulse (A) | A pulse encoder (signal A) without direction signal is connected. | - Filter frequency - Sensor type or Interface standard |
| Count up (A), count down (B) | Signals for counting up (signal A) and down (signal B) are connected. | - Filter frequency - Sensor type or Interface standard |

**Invert direction**

You can invert the count direction to adapt it to the process.

The inverting of the direction is configurable and active for the following signal types:

- Incremental encoder (A, B phase-shifted)
- Incremental encoder (A, B, N)

**Signal evaluation**

By configuring [signal evaluation](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#overview-s7-1500), you can specify which edges of the signals are counted.

You can select from the following options:

| Signal evaluation | Meaning |
| --- | --- |
| Single  (default) | The edges of signal A are evaluated during a low level of signal B. |
| Double | Each edge of signal A is evaluated. |
| Quadruple | Each edge of signals A and B is evaluated. |

The parameter can be assigned with the following signal types:

- Incremental encoder (A, B phase-shifted)
- Incremental encoder (A, B, N)

**Filter frequency**

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
| 100 kHz | 4.0 µs |
| 200 kHz (default for TM Count) | 2.0 µs |
| 500 kHz* | 0.8 µs |
| 1 MHz* (default for TM PosInput) | 0.4 µs |
| * Only available with TM PosInput |  |

**Sensor type**
 **(TM Count)**

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

**Interface standard**
 **(TM PosInput)**

You use this parameter to specify whether the encoder outputs symmetric (RS422) or asymmetric (TTL) signals for the TM PosInput.

You can select from the following options:

| Interface standard | Meaning |
| --- | --- |
| RS422, symmetrical (default) | The encoder outputs symmetric signals according to the [RS422 standard](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#rs422-count-signals-s7-1500). |
| TTL (5 V), asymmetrical | The encoder outputs asymmetric 5 V signals according to the [TTL standard](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#24-v-or-ttl-count-signals-s7-1500). |

> **Note**
>
> The RS422 standard provides greater interference immunity than the TTL standard. Therefore, if your incremental or pulse encoder supports the RS422 **and** the TTL standard, it is recommended to use the RS422 signal standard.

**Reaction to signal N**

You use this parameter to specify which reaction is triggered to signal N.

You can select from the following options:

| Option | Meaning |
| --- | --- |
| No reaction to signal N (default) | The counter is not affected by signal N. |
| [Synchronization at signal N](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#synchronization-at-signal-n-s7-1500) | The counter is set to the start value at signal N.   If you select the function "Enable synchronization at signal N" for a digital input, the synchronization depends on the level at the digital input. |

> **Note**
>
> You can only select the reaction to signal N if you have selected the "Incremental encoder (A, B, N)" signal type.

> **Note**
>
> If "Synchronization at signal N" is selected, you can select the function "Enable synchronization at signal N" for a [digital input](#behavior-of-a-di-s7-1500-2).

**Frequency of synchronization**

This parameter is used to define the frequency of the following events:

- Synchronization at signal N
- Synchronization as a function of a digital input

You can select from the following options:

| Option | Meaning |
| --- | --- |
| Once (default) | The counter is only set at the first signal N or the first configured edge of the digital input. |
| Periodic | The counter is set at each signal N or each configured edge of the digital input. |

**Count direction for synchronization**

You use this parameter to define the count direction for which the following functions are enabled:

- Synchronization at signal N
- Synchronization as a function of a digital input

You can select from the following options:

| Option | Meaning |
| --- | --- |
| Up (default) | The synchronization only takes place when the counter counts up. |
| Down | The synchronization only takes place when the counter counts down. |
| In both directions | The synchronization takes place regardless of the count direction. |

##### Counting limits and start value (S7-1500)

**High counting limit**

You limit the counting range by setting the high counting limit. You can enter a value up to 33554431 (2<sup>25</sup>-1). You must enter a value that lies above the low counting limit.

The default setting is "33554431".

**Low counting limit**

You limit the counting range by setting the low counting limit. You can enter a value starting with 0. You must enter a value below the high counting limit.

The default setting is "0".

**Start value**

By configuring the start value, you specify the value at which counting is to start and where it is to continue in the case of defined events. You must enter a value between the counting limits or equal to the counting limits.

The default setting is "0".

**More information**

For more information, see [Behavior at the counting limits](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#behavior-at-the-counting-limits-s7-1500) and [Counter behavior at gate start](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#counter-behavior-at-gate-start-s7-1500).

##### Counter behavior at limits and gate start (S7-1500)

**Reaction to violation of a counting limit**

You can configure the following [Reaction to violation of a counting limit](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#behavior-at-the-counting-limits-s7-1500):

| Reaction | Meaning |
| --- | --- |
| Stop counting | If a counting limit is violated, counting is stopped and the internal gate is closed. To restart counting, you must also close and reopen the software/hardware gate. |
| Continue counting (default) | Counting continues either with the start value or at the opposite counting limit, depending on the additional parameter assignment. |

**Reset when counting limit is violated**

You can reset the counter to the following values when a counting limit is violated:

| Reset the value | Meaning |
| --- | --- |
| To start value | The counter value is set to the start value. |
| To opposite counting limit (default) | The counter value is set to the opposite counting limit. |

**Reaction to gate start**

You can set the following [Reaction to gate start](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#counter-behavior-at-gate-start-s7-1500):

| Reaction | Meaning |
| --- | --- |
| Set to start value | When the gate is opened, the counter value is set to the start value. |
| Continue with current value (default) | When the gate is opened, counting is continued with the last counter value. |

> **Note**
>
> The parameter is only active if you have configured a hardware gate.

##### Behavior of a DI (S7-1500)

**Set function of DI**

By configuring a digital input, you specify which functions the digital input triggers at switching.

You can select from the following options:

| Function of a digital input | Meaning | Additional option-specific parameters |
| --- | --- | --- |
| Gate start/stop (level-triggered) | The level at the respective digital input opens and closes the [hardware gate](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#hardware-gate-s7-1500). | - Input delay - Select level |
| Gate start (edge-triggered) | The configured edge at the respective digital input opens the [hardware gate](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#hardware-gate-s7-1500). | - Input delay - Edge selection |
| Gate stop (edge-triggered) | The configured edge at the respective digital input closes the [hardware gate](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#hardware-gate-s7-1500). | - Input delay - Edge selection |
| [Synchronization](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#synchronization-s7-1500) | The configured edge at the respective digital input sets the counter to the start value. | - Input delay - Edge selection - Frequency of synchronization - Count direction for synchronization |
| Enable synchronization at signal N | The active level at the respective digital input enables [synchronization of the counter at signal N](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#synchronization-at-signal-n-s7-1500). | - Input delay - Select level |
| Digital input without function | No technological function is assigned to the respective digital input.  You can read the signal state of the digital input via the respective feedback bit (number of digital inputs depends on the module):  - STS_DI0 - STS_DI1 - STS_DI2 | - Input delay |

> **Note**
>
> With the exception of "Digital input without function", each function can only be used once for each counter, and if used for one digital input is not available to the others.

**Input delay**

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
> You configure the input delay under "Behavior of DI0" for all digital inputs together. The input delay is also displayed under "Behavior of DI1" and for TM Count also under "Behavior of DI2".

**Select level**

You use this parameter to specify the level at which the digital input is active.

You can select from the following options:

| Level | Meaning |
| --- | --- |
| Active with high level  (default) | The respective digital input is active when it is set. |
| Active with low level | The respective digital input is active when it is not set. |

The parameter can be set for the following functions of a digital input:

- Gate start/stop (level-triggered)
- Enable synchronization at signal N

**Edge selection**

You can use this parameter to specify the edge of the digital input at which the configured function is triggered.

The following options may be available depending on the function selected:

- At rising edge (default)
- At falling edge

The parameter can be set for the following functions of a digital input:

- Gate start (edge-triggered)
- Gate stop (edge-triggered)
- Synchronization

**Frequency of synchronization**

This parameter is used to define the frequency of the following events:

- Synchronization at signal N
- Synchronization as a function of a digital input

You can select from the following options:

| Option | Meaning |
| --- | --- |
| Once (default) | The counter is only set at the first signal N or the first configured edge of the digital input. |
| Periodic | The counter is set at each signal N or each configured edge of the digital input. |

**Count direction for synchronization**

You use this parameter to define the count direction for which the following functions are enabled:

- Synchronization at signal N
- Synchronization as a function of a digital input

You can select from the following options:

| Option | Meaning |
| --- | --- |
| Up (default) | The synchronization only takes place when the counter counts up. |
| Down | The synchronization only takes place when the counter counts down. |
| In both directions | The synchronization takes place regardless of the count direction. |

##### Behavior of a DQ (S7-1500)

###### Set output

With the parameter assignment of a digital output, you specify the condition upon which the digital output switches.

You can select from the following options:

| [Function of a digital output](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#switching-at-comparison-values-with-counter-value-as-reference-s7-1500) | Meaning | Additional option-specific parameters |
| --- | --- | --- |
| Between comparison value and high limit (default) | The respective digital output is active if: Comparison value <= counter value <= high counting limit | - Comparison value 0 - Comparison value 1 - Hysteresis (in increments) |
| Between comparison value and low limit | The respective digital output is active if: Low counting limit <= counter value <= comparison value | - Comparison value 0 - Comparison value 1 - Hysteresis (in increments) |
| Between comparison value 0 and 1 | The digital output DQ1 is active if: Comparison value 0 <= counter value <= comparison value 1 | - Comparison value 0 - Comparison value 1 - Count direction - Hysteresis (in increments) |
| At comparison value for a pulse duration | The respective digital output is active once for the configured time and count direction when the counter value reaches the comparison value. | - Comparison value 0 - Comparison value 1 - Count direction - Pulse duration - Hysteresis (in increments) |
| Digital output without function | The respective digital output is set to 0 regardless  of the reaction to CPU STOP. | — |

> **Note**
>
> You can only set the "Between comparison value 0 and 1" function for digital output DQ1 and only if you have selected the function "Digital output without function" for digital output DQ0.

**Comparison value 0**

With the parameter assignment of the [comparison value](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#switching-at-comparison-values-with-counter-value-as-reference-s7-1500), you specify the counter value at which the digital output DQ0 switches as a result of the selected comparison event.

You must enter an integer (DINT) with a value between 0 and 33554431. If you use the DQ function "Between comparison value 0 and 1", the comparison value 0 has to be smaller than comparison value 1. The default setting is "0".

**Comparison value 1**

With the parameter assignment of the [comparison value](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#switching-at-comparison-values-with-counter-value-as-reference-s7-1500), you specify the counter value at which the digital output DQ1 switches as a result of the selected comparison event.

You must enter an integer (DINT) with a value between 0 and 33554431. If you use the DQ function "Between comparison value 0 and 1", the comparison value 0 has to be smaller than comparison value 1. The default setting is "10".

**Count direction**

You use this parameter to specify the count direction for which the selected function is valid.

You can select from the following options:

| Count direction | Meaning |
| --- | --- |
| In both directions  (default) | The comparison and switching of the respective digital output take place regardless of the count direction. |
| Up | The comparison and switching of the respective digital output only takes place when the counter counts up. |
| Down | The comparison and switching of the respective digital output only takes place when the counter counts down. |

The parameter can be configured for the following functions:

- Between comparison value 0 and 1
- At comparison value for a pulse duration

**Pulse duration**

By configuring the pulse duration for the function "At comparison value for a pulse duration", you specify the number of milliseconds for which the respective digital output is active.

A value from 0.0 to 6553.5 ms is permissible.

The default setting is "500.0", which is equivalent to a pulse duration of 0.5 s.

**Hysteresis (in increments)**

By configuring the [hysteresis](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#hysteresis-with-incremental-or-pulse-encoder-s7-1500), you can define a range around the comparison values. For the functions "Between comparison value and high limit" and "Between comparison value and low limit", the hysteresis also applies at the counter limits. Within the hysteresis range, the digital outputs cannot switch again until the counter value is outside the range.

Choose a small enough hysteresis. When the hysteresis range, starting from the configured comparison value, spans the entire counting range, proper functioning of the comparison values cannot be guaranteed.

Regardless of the hysteresis value, the hysteresis range ends at the low or high counting limit.

If you enter "0", the hysteresis is turned off. You can enter a value between 0 and 255. The default setting is "0".

#### Fast Mode (SSI absolute encoder)  (S7-1500)

This section contains information on the following topics:

- [Counter inputs (S7-1500)](#counter-inputs-s7-1500-3)
- [Behavior of a DI (S7-1500)](#behavior-of-a-di-s7-1500-3)
- [Behavior of a DQ (S7-1500)](#behavior-of-a-dq-s7-1500-3)

##### Counter inputs (S7-1500)

**Signal type**

If an SSI absolute encoder with the data signal (Signal ID) and cycle signal (Signal C) is connected, select the [signal type](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#position-input-with-ssi-absolute-encoder-s7-1500) "Absolute encoder (SSI)".

**Invert direction**

You can use this parameter to invert the values supplied by the SSI absolute encoder. This allows you to adapt the detected direction of the encoder to the motor's direction of rotation.

> **Note**
>
> This parameter acts only on the range from the LSB to the MSB of the position value in the frame.

**Frame length**

With the parameter assignment of the frame length, you specify the number of bits of an SSI frame of the [SSI absolute encoder](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#ssi-signals-s7-1500) used. You can find the frame length of your SSI absolute encoder in the data sheet of the encoder. Special bits are also included in the frame length. A parity bit does not count in the frame length.

A frame length of between 10 bits and 40 bits is permitted. The default setting is "13 Bit".

You can find two examples of the SSI frame format at [Examples of the frame format](Using%20technology%20object%20SSI_Absolute_Encoder%20%28S7-1500%29.md#examples-of-the-frame-format-s7-1500).

**Code type**

You use the parameter assignment of the code type to specify whether the encoder supplies Dual code or Gray code.

You can select from the following options:

| Code type | Meaning |
| --- | --- |
| Gray (default) | The gray-coded position value returned by the SSI absolute encoder is converted to dual code. |
| Dual | The value returned by the SSI absolute encoder is not converted. |

**Transmission rate**

With the parameter assignment of the transmission rate, you specify the data transmission rate between the technology module and the SSI absolute encoder.

You can select from the following options:

- 125 kHz (preset)
- 250 kHz
- 500 kHz
- 1 MHz
- 1.5 MHz
- 2 MHz

The maximum transmission rate depends on the cable length and the technical specifications of the SSI absolute encoder. For additional information, refer to the product manual of the TM PosInput and the encoder description.

**Monoflop time**

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

**Parity**

With the parameter assignment of the parity, you specify whether the SSI absolute encoder transfers a parity bit.

If, for example, a 25-bit encoder with parity is assigned, the technology module reads 26 bits. A parity error is reported in the feedback interface by means of the ENC_ERROR bit.

**Bit number LSB of the position value**

This parameter is used to specify the bit number of the LSB (least significant bit) of the position value in the frame of the SSI absolute encoder. In this way you limit the range in the frame that supplies the position value.

The value must be less than the bit number of the MSB of the position value. The difference between the bit numbers of the MSB and the LSB of the position value must be less than 32.

The default setting is "0".

> **Note**
>
> If you have selected the Code type "Gray", only the range from the LSB to the MSB of the position value is converted to binary code.

**Bit number MSB of the position value**

This parameter is used to specify the bit number of the MSB (most significant bit) of the position value in the frame of the SSI absolute encoder. In this way you limit the range in the frame that supplies the position value.

The value must be less than the frame length and higher than the bit number of the LSB of the position value. The difference between the bit numbers of the MSB and the LSB of the position value must be less than 32.

The default setting is "12".

> **Note**
>
> If you have selected the Code type "Gray", only the range from the LSB to the MSB of the position value is converted to binary code.

##### Behavior of a DI (S7-1500)

**Set function of DI**

By configuring a digital input, you specify which functions the digital input triggers at switching.

You can select from the following options:

| Function of a digital input | Meaning | Additional option-specific parameters |
| --- | --- | --- |
| Digital input without function | No technological function is assigned to the respective digital input.   You can read the signal state of the digital input via the respective feedback bit:  - STS_DI0 - STS_DI1 | - Input delay |

**Input delay**

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

##### Behavior of a DQ (S7-1500)

**Set output**

With the parameter assignment of a digital output, you specify the condition upon which the digital output switches.

You can select from the following options depending on the operating mode:

| [Function of a digital output](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#switching-at-comparison-values-with-position-value-ssi-absolute-value-as-reference-s7-1500) | Meaning | Additional option-specific parameters |
| --- | --- | --- |
| Between comparison value and high limit (default) | The respective digital output is active if: Comparison value <= position value <= maximum position value | - Comparison value 0 - Comparison value 1 - Hysteresis (in increments) |
| Between comparison value and low limit | The respective digital output is active if: Minimum position value <= Position value <= Comparison value | - Comparison value 0 - Comparison value 1 - Hysteresis (in increments) |
| Between comparison value 0 and 1 | The digital output DQ1 is active if: Comparison value 0 <= position value <= comparison value 1 | - Comparison value 0 - Comparison value 1 - Count direction - Hysteresis (in increments) |
| At comparison value for a pulse duration | The respective digital output is active once for the assigned time and direction of the position value change when the position value is equal to the comparison value or has fallen below or exceeded it. | - Comparison value 0 - Comparison value 1 - Count direction - Pulse duration - Hysteresis (in increments) |
| Digital output without function | The respective digital output is set to 0 regardless of the reaction to CPU STOP. | — |

> **Note**
>
> You can only select the "Between comparison value 0 and 1" function for digital output DQ1 and only if you have selected the "Use by user program" function for digital output DQ0.

**Comparison value 0**

With the parameter assignment of the [comparison value](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#switching-at-comparison-values-with-position-value-ssi-absolute-value-as-reference-s7-1500), you specify the position value at which the digital output DQ0 switches as a result of the selected comparison event.

You must enter an integer (DINT) that is greater than or equal to the low counting limit. If you use the DQ function "Between comparison value 0 and 1", the comparison value 0 has to be smaller than comparison value 1. The default setting is "0".

If you use the DQ function "Between comparison value 0 and 1", the comparison value 0 has to be smaller than comparison value 1. The default setting is "0".

**Comparison value 1**

With the parameter assignment of the [comparison value](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#switching-at-comparison-values-with-position-value-ssi-absolute-value-as-reference-s7-1500), you specify the position value at which the digital output DQ1 switches as a result of the selected comparison event.

You must enter an integer (DINT) that is less than or equal to the high counting limit. If you use the DQ function "Between comparison value 0 and 1", the comparison value 0 has to be smaller than comparison value 1. The default setting is "10".

If you use the DQ function "Between comparison value 0 and 1", the comparison value 0 has to be smaller than comparison value 1. The default setting is "10".

**Count direction**

You use this parameter to specify the direction of position value change for which the selected function is valid.

You can select from the following options:

| Direction of position value change | Meaning |
| --- | --- |
| In both directions  (default) | The comparison and switching of the respective digital output is carried out regardless of whether the position value increases of decreases. |
| Up | The comparison and switching of the respective digital output only takes place when the position value increases. |
| Down | The comparison and switching of the respective digital output only takes place when the position value decreases. |

The parameter can be configured for the following functions:

- Between comparison value 0 and 1
- At comparison value for a pulse duration

**Pulse duration**

By configuring the pulse duration for the function "At comparison value for a pulse duration", you specify the number of milliseconds for which the respective digital output is active.

A value from 0.1 to 6553.5 ms is permissible.

The default setting is "500.0", which is equivalent to a pulse duration of 0.5 s.

**Hysteresis (in increments)**

By configuring the [hysteresis](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#hysteresis-with-ssi-absolute-encoder-s7-1500), you can define a range around the comparison values. For the functions "Between comparison value and high limit" and "Between comparison value and low limit", the hysteresis also applies at the counter limits. Within the hysteresis range, the digital outputs cannot switch again until the position value has left this range once.

Choose a small enough hysteresis. When the hysteresis range, starting from the configured comparison value, spans the entire position value range, proper functioning of the comparison values cannot be guaranteed.

Regardless of the hysteresis value, the hysteresis range ends at the low or high counting limit.

If you enter "0", the hysteresis is turned off. You can enter a value between 0 and 255. The default setting is "0".

### Online & diagnostics module (S7-1500)

This section contains information on the following topics:

- [Displaying and evaluating diagnostics (S7-1500)](#displaying-and-evaluating-diagnostics-s7-1500)

#### Displaying and evaluating diagnostics (S7-1500)

The online and diagnostics view enables hardware diagnostics. You can also

- Obtain information on the technology module (e.g., Firmware version and serial number)
- Execute a firmware update if required

##### Procedure (TM Count and TM PosInput)

To open the display editor for the diagnostic functions, follow these steps:

1. Open the device configuration of the CPU or IM.
2. Select the device view.
3. Right-click the module and select "Online & Diagnostics".

1. Select the required display in the diagnostics navigation.

##### Procedure (ET 200eco PN TM PosInput 2)

To open the display editor for the diagnostic functions, follow these steps:

1. Open the device configuration of the CPU.
2. Select the network view.
3. Right-click the module and select "Online & Diagnostics".

1. Select the required display in the diagnostics navigation.

##### Procedure (Compact CPU)

To open the display editor for the diagnostic functions, follow these steps:

1. Open the Compact CPU folder in the project tree.
2. Double-click on the "Online & diagnostics" object.
3. Select the required display in the diagnostics navigation.

##### Additional information

Additional information on the diagnostic alarms and possible remedies can be found in the technology module device manual.

> **Note**
>
> **Position input for Motion Control**
>
> In operating mode "Position input for "Motion Control" technology object", channel diagnostics is not available for the technology module.

### Control and feedback interface (TM Count, TM PosInput) (S7-1500)

This section contains information on the following topics:

- [Use of control and feedback interface (S7-1500)](#use-of-control-and-feedback-interface-s7-1500)
- [Assignment of the control interface (S7-1500)](#assignment-of-the-control-interface-s7-1500)
- [Notes on the control interface (S7-1500)](#notes-on-the-control-interface-s7-1500)
- [Assignment of the feedback interface (S7-1500)](#assignment-of-the-feedback-interface-s7-1500)
- [Notes on the feedback interface (S7-1500)](#notes-on-the-feedback-interface-s7-1500)

#### Use of control and feedback interface (S7-1500)

Information on using the control and feedback interface can be found under [Overview of application options](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#overview-of-applications-s7-1500).

> **Note**
>
> The following description does not apply for the operating modes "Fast Mode" and "Position input for technology object "Motion Control"". You can find a description of the feedback interface in the respective device manual for those technology modules that support the "Fast Mode" operating mode.

#### Assignment of the control interface (S7-1500)

The user program uses the control interface to influence the behavior of the technology module.

##### Control interface per channel

The following table shows control interface assignment:

| Byte offset to start address Channel 0/1 **↓ ↓** |  | Bit 7 | Bit 6 | Bit 5 | Bit 4 | Bit 3 | Bit 2 | Bit 1 | Bit 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 … 3 | 12 … 15 | SLOT_0:  DINT or REAL: Load value (significance of the value is specified in LD_SLOT_0)  Value range: –2147483648 to 2147483647<sub>D</sub> or 80000000 to 7FFFFFFF<sub>H</sub> |  |  |  |  |  |  |  |
| 4 … 7 | 16 … 19 | SLOT_1:  DINT or REAL: Load value (significance of the value is specified in LD_SLOT_1)  Value range: –2147483648 to 2147483647<sub>D</sub> or 80000000 to 7FFFFFFF<sub>H</sub> |  |  |  |  |  |  |  |
| 8 | 20 | LD_SLOT_1 |  |  |  | LD_SLOT_0 |  |  |  |
| 9 | 21 | EN_ CAPTURE | EN_ SYNC_DN | EN_ SYNC_UP | SET_DQ1 | SET_DQ0 | TM_ CTRL_DQ1 | TM_ CTRL_DQ0 | SW_GATE |
| 10 | 22 | SET_DIR | Reserved |  |  |  |  | RES_ EVENT | RES_ ERROR |
| 11 | 23 | Reserved |  |  |  |  |  |  |  |

#### Notes on the control interface (S7-1500)

##### Notes

| Control bit/value | Notes |
| --- | --- |
| SLOT_m | You specify the load value with this value. You specify the meaning of the value in LD_SLOT_m.  If you want to load a comparison value in the "Measuring" operating mode, specify the load value as floating-point number (REAL). In all other cases, you specify the load value as an integer (DINT).  Value range: –2147483648 to 2147483647<sub>D</sub> or 80000000 to 7FFFFFFF<sub>H</sub> |
| LD_SLOT_m | With this load request you specify the meaning of the value in SLOT_m:  - 0000 means: No action, idle - 0001 means: Load count value (with incremental or pulse encoder) - 0010 not permitted - 0011 means: Load start value (with incremental or pulse encoder) - 0100 means: Load Comparison value 0 - 0101 means: Load comparison value 1 - 0110 means: Load low counting limit (with incremental or pulse encoder) - 0111 means: Load high counting limit (with incremental or pulse encoder)​ - 1000 to 1111 not permitted   The technology module executes the respective action as soon as LD_SLOT_m changes.  If values are loaded simultaneously via LD_SLOT_0 and LD_SLOT_1, the first value is applied internally from SLOT_0 and then the value from SLOT_1 is applied. This might lead to unexpected intermediate states.  A change of the COUNT_VALUE value via LD_SLOT_m has no influence on the MEASURED_VALUE value. |
| EN_CAPTURE | Use this bit to enable the Capture function. Resetting this bit resets a set EVENT_CAP in the feedback interface. |
| EN_SYNC_DN | Use this bit to enable the synchronization of the counter when counting down with an incremental encoder or pulse encoder. Resetting this bit resets a set EVENT_SYNC in the feedback interface. |
| EN_SYNC_UP | Use this bit to enable the synchronization of the counter when counting up with an incremental encoder or pulse encoder. Resetting this bit resets a set EVENT_SYNC in the feedback interface. |
| SET_DQ0 | Use this bit to set digital output DQ0 when TM_CTRL_DQ0 is set to 0.  In the case of the function "After set command from CPU until comparison value", SET_DQ0 is effective regardless of TM_CTRL_DQ0 as long as the counter value is not equal to the comparison value. |
| SET_DQ1 | Use this bit to set digital output DQ1 when TM_CTRL_DQ1 is set to 0.  In the case of the function "After set command from CPU until comparison value", SET_DQ1 is effective regardless of TM_CTRL_DQ1 as long as the counter value is not equal to the comparison value. |
| TM_CTRL_DQ0 | Use this bit to enable the technological function of digital output DQ0.   - 0 means: SET_DQ0 defines the state of DQ0 - 1 means: assigned function defines the state of DQ0 |
| TM_CTRL_DQ1 | Use this bit to enable the technological function of digital output DQ1.   - 0 means: SET_DQ1 defines the state of DQ1 - 1 means: assigned function defines the state of DQ1 |
| SW_GATE | Use this bit to open and close the software gate when using an incremental encoder or pulse encoder. Together, the software gate and the hardware gate form the internal gate. The technology module only counts when the internal gate is open.  - 0 means: Software gate closed - 1 means: Software gate open   The control of the hardware gate takes place externally via the digital inputs of the technology module. The hardware gate can be activated through parameter assignment. The software gate cannot be deactivated. |
| SET_DIR | Use this bit to specify the counting direction for signal type "Pulse (A)".   - 0 means: Up - 1 means: Down |
| RES_EVENT | Use this bit to trigger the reset of the saved events in the EVENT_ZERO, EVENT_OFLW, EVENT_UFLW, EVENT_CMP0, EVENT_CMP1 feedback bits. |
| RES_ERROR | Use this bit to trigger the reset of the saved error states LD_ERROR and ENC_ERROR . |
| Reserved | Reserved bits must be set to 0. |

#### Assignment of the feedback interface (S7-1500)

The user program receives current values and status information from the technology module via the feedback interface.

##### Feedback interface per channel

The following table shows the assignment of the feedback interface:

| Byte offset to start address Channel 0/1 **↓ ↓** |  | Bit 7 | Bit 6 | Bit 5 | Bit 4 | Bit 3 | Bit 2 | Bit 1 | Bit 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 … 3 | 16 … 19 | COUNT_VALUE:  DINT: Current counter value or position value |  |  |  |  |  |  |  |
| 4 … 7 | 20 … 23 | CAPTURED_VALUE:  DINT: The last acquired Capture value |  |  |  |  |  |  |  |
| 8 ... 11 | 24 ... 27 | MEASURED_VALUE:  REAL: Current measured value or DWORD: Full SSI frame |  |  |  |  |  |  |  |
| 12 | 28 | Reserved |  |  |  |  | LD_ERROR | ENC_ ERROR | POWER_ ERROR |
| 13 | 29 | Reserved |  | STS_SW_ GATE | STS_ READY | LD_STS_ SLOT_1 | LD_STS_ SLOT_0 | RES_EVENT_ACK | Reserved |
| 14 | 30 | STS_DI2<sup>1</sup> | STS_DI1 | STS_DI0 | STS_DQ1 | STS_DQ0 | STS_GATE | STS_CNT | STS_DIR |
| 15 | 31 | STS_M_ INTERVAL | EVENT_ CAP | EVENT_ SYNC | EVENT_ CMP1 | EVENT_ CMP0 | EVENT_ OFLW | EVENT_ UFLW | EVENT_ ZERO |
| <sup>1</sup> For TM PosInput applies: Reserved |  |  |  |  |  |  |  |  |  |

> **Note**
>
> **Validity of the position value**
>
> The position value of an SSI absolute encoder is valid if STS_READY is set to 1 and ENC_ERROR is set to 0. In the module startup STS_READY is set to 0.

#### Notes on the feedback interface (S7-1500)

##### Notes

| Feedback bit/value | Notes |
| --- | --- |
| COUNT_VALUE | This DINT value shows the current counter value or position value.  If you use an SSI absolute encoder with a position value length of up to 31 bits, the position value is treated unsigned as a positive value and can assume values between 0 and 2<sup>(MSB-LSB+1)</sup>-1. If you use an SSI absolute encoder with a position value length of 32 bits, the MSB of the position value corresponds to the sign and the position value can assume values between -2147483648 and 2147483647. If you use a 32 bit position value for the comparison function, the position value is interpreted as DINT.  A change of the COUNT_VALUE value via LD_SLOT_m has no influence on the MEASURED_VALUE value. |
| CAPTURED_VALUE | This DINT value indicates the last detected Capture value.  The following external signals can trigger the Capture function:  - Rising or falling edge of a digital input - Both edges of a digital input   The parameter "Frequency of the Capture function" determines if the function is executed for each configured edge or only once after each enable. |
| MEASURED_ VALUE | This value shows the current measurement value with the REAL data type or the complete SSI frame with the DWORD data type:  - Frequency: The mean frequency is calculated at set measuring intervals on the basis of the time profile of the count pulses or position value changes and returned in Hertz as floating point number. - Period duration: The mean period duration is calculated at set measuring intervals on the basis of the time profile of the count pulses or position value changes and returned in seconds as floating point number. - Velocity: The mean velocity is calculated at set measuring intervals on the basis of the time profile of the count pulses or position value changes and other parameters, and returned in the configured unit of measurement. - Complete SSI frame: Instead of a measured variable, the least significant 32 bits of the unprocessed current SSI frame are returned. This provides you with encoder-specific additional bits, such as error bits, in addition to the position value. If the SSI frame is shorter than 32 bits, the complete SSI frame is returned right-aligned and the top unused bits are returned with "0" in the feedback interface.   The measured values are returned as signed values. The sign indicates whether the counter value or position value increased or decreased during the relevant time period.   The update time is asynchronous to the opening of the internal gate, which means that the update time is not started when the gate is opened. After the internal gate is closed, the last measured value captured is still returned. |
| LD_ERROR | This bit indicates that an error occurred (latching) during loading via the control interface. The loaded values were not applied. When using an incremental or pulse encoder, one of the following conditions is not fulfilled:  - Low counting limit <= counter value <= high counting limit - Low counting limit <= start value <= high counting limit - Low counting limit <= comparison value 0/1 <= high counting limit   When using an SSI absolute encoder, one of the following conditions is not fulfilled:   - 0 <= position value <= maximum position value - 0 <= comparison value 0/1 <= maximum position value   The bit is reset once you have acknowledged the error with RES_ERROR . |
| ENC_ERROR | This bit indicates that one of the following errors has occurred at the encoder signals (retentive) for the respective technology module:  TM Count:  - Wire break of digital input A, B, or N (with push-pull encoder) - Invalid transition of A/B signals (with incremental encoder)   TM PosInput:  - Invalid transition of A/B signals (with incremental encoder) - RS422/TTL error - SSI encoder error or SSI frame error (with SSI absolute encoder)   If you have enabled the diagnostic interrupts, the respective diagnostic interrupt is triggered in the event of encoder signal errors. For information on the meaning of the diagnostic interrupts, refer to the manual for the respective technology module.  The bit is reset once you have acknowledged the error with RES_ERROR . |
| POWER_ERROR | For an S7‑1500 technology module, this bit indicates that the supply voltage L+ is not available or too low or that the front plug is not plugged in. For an ET 200SP technology module, this bit indicates that the supply voltage L+ is too low.   If you have enabled the diagnostic interrupts, the respective diagnostic interrupt is triggered in the event of errors in the supply voltage. For details on the diagnostic interrupts and the corrective measures they require, refer to the device manual for the respective technology module.  If the supply voltage L+ is available at a sufficient level once again, POWER_ERROR is automatically set to 0. |
| STS_SW_GATE | This bit indicates the status of the software gate.   0 means: Gate closed  1 means: Gate open |
| STS_READY | This bit indicates that the technology module supplies valid user data. The technology module has been started up and configured. |
| LD_STS_SLOT_0 | This bit indicates by a status change (toggling) that the load request for Slot 0 (LD_SLOT_0) has been detected and executed. |
| LD_STS_SLOT_1 | This bit indicates by a status change (toggling) that the load request for Slot 1 (LD_SLOT_1) has been detected and executed. |
| RES_EVENT_ACK | This bit indicates that the reset of event bit EVENT_SYNC, EVENT_CMP0, EVENT_CMP1, EVENT_OFLW, EVENT_UFLW, EVENT_ZERO is active. |
| STS_DI0 | This bit indicates the status of digital input DI0. |
| STS_DI1 | This bit indicates the status of digital input DI1. |
| STS_DI2 | This bit indicates the status of digital input DI2 of the TM Count . |
| STS_DQ0 | This bit indicates the status of digital output DQ0. |
| STS_DQ1 | This bit indicates the status of digital output DQ1. |
| STS_GATE | This bit indicates the status of the internal gate when using an incremental or pulse encoder.   0 means: Gate closed  1 means: Gate open  Information for TM PosInput:  In order for the counting logic including the gate control to function correctly, the startup of the technology module must complete correctly at least once with a connected incremental or pulse encoder (STS_READY at 1). If a connected encoder is not ready yet during startup, the function of the STS_GATE feedback bit is delayed until the encoder for the technology module is available. If the technology module starts up without a connected encoder, the startup does not complete correctly and STS_READY as well as STS_GATE remain at 0. As soon as an encoder is then connected, the startup completes and the STS_GATE functions correctly. An encoder error after a completed startup has no influence on STS_GATE. |
| STS_CNT | This bit indicates that at least one count pulse or a position value change has been detected in the last approx. 0.5 s. |
| STS_DIR | This bit indicates the counting direction of the last count pulse or the direction of the last position value change.  0 means: Down  1 means: Up |
| STS_M_INTERVAL | This bit indicates that at least one count pulse or a position value change was detected in the previous measurement interval. |
| EVENT_CAP | This bit indicates that a Capture event has occurred and a counter value has been saved in CAPTURED_VALUE . You reset the state by resetting EN_CAPTURE . |
| EVENT_SYNC | This bit indicates the saved state that the counter was loaded with the start value by an external reference signal (synchronization) when using an incremental or pulse encoder. You reset the state by resetting EN_SYNC_UP or EN_SYNC_DN . |
| EVENT_CMP0 | This bit indicates the saved state that a comparison event (state change) has occurred for the digital output DQ0 based on the selected comparison condition. You reset the state by acknowledgment with RES_EVENT.  If the counter value is set to the start value in counting operating mode, EVENT_CMP0 is not set. |
| EVENT_CMP1 | This bit indicates the saved state that a comparison event (state change) has occurred for the digital output DQ1 based on the selected comparison condition. You reset the state by acknowledgment with RES_EVENT.  If the counter value is set to the start value in counting operating mode, EVENT_CMP1 is not set. |
| EVENT_OFLW | This bit indicates the saved state that there was a counter value overflow. You reset the state by acknowledgment with RES_EVENT. |
| EVENT_UFLW | This bit indicates the saved state, that there was a counter value underflow. You reset the state by acknowledgment with RES_EVENT. |
| EVENT_ZERO | This bit indicates the saved state that the counter value or position value experienced a zero crossing. You reset the state by acknowledgment with RES_EVENT. |
| Reserved | Reserved bits are set to 0. |

##### Complete acknowledgment principle

Saving bits are acknowledged according to the complete acknowledgment principle.

The figure below shows an example of the sequence of the complete acknowledgment principle in the event of an overflow:

![Complete acknowledgment principle](images/127576760843_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | The EVENT_OFLW feedback bit is set as a saving event upon overflow. |
| ② | You set the RES_EVENT control bit to trigger EVENT_OFLW reset. |
| ③ | The RES_EVENT_ACK feedback bit is set when reset of EVENT_OFLW is detected. |
| ④ | You then rest the control bit RES_EVENT . |
| ⑤ | The RES_EVENT_ACK feedback bit is reset. |

##### Applying values via load prompt

The figure below shows an example of the procedure of application of values with the load prompt and on error detection:

![Applying values via load prompt](images/127355930891_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| 1a | You write the valid value 1 (load count value) to LD_SLOT_0 and the desired load value to SLOT_0. |
| 1b | The LD_STS_SLOT_0 feedback bit is toggled because the LD_SLOT_0 load request was recognized by the module and implemented. |
| 2a | You write the invalid value 2 to LD_SLOT_0. |
| 2b | The LD_ERROR feedback bit is set because the value in LD_STS_SLOT_0 is invalid. The value in SLOT_0 is not applied. |
| 2c | You set the RES_ERROR control bit in order to acknowledge the error. |
| 2d | The LD_ERROR feedback bit is reset. |
| 2e | You reset the RES_ERROR control bit. |
| 3a | You write the valid value 3 (load start value) to LD_SLOT_0 and the desired load value to SLOT_0. |
| 3b | The LD_STS_SLOT_0 feedback bit is toggled because the LD_SLOT_0 load request was recognized by the module and implemented. |

## Using the digital module (S7-1500)

This section contains information on the following topics:

- [Configuring and assigning parameters to the module (S7-1500)](#configuring-and-assigning-parameters-to-the-module-s7-1500)
- [Online & diagnostics module (S7-1500)](#online-diagnostics-module-s7-1500-1)

### Configuring and assigning parameters to the module (S7-1500)

This section contains information on the following topics:

- [Adding a module to the hardware configuration (S7-1500)](#adding-a-module-to-the-hardware-configuration-s7-1500)
- [Open hardware configuration (S7-1500)](#open-hardware-configuration-s7-1500-1)
- [Counting operating mode (S7-1500)](#counting-operating-mode-s7-1500)

#### Adding a module to the hardware configuration (S7-1500)

##### Requirements

- The project has been created.
- The CPU S7-1500 has been created.
- At decentralized operation an ET 200 distributed I/O system is created.

##### Procedure

1. Open the device configuration of the CPU or IM.
2. Select a module rack.
3. Select the digital input module from the module catalog:  
   "DI > Digital input module > Article number" or   
   "DIQ > Digital input module /Digital output module > Article number"
4. Drag the module to the required slot in the module rack.

#### Open hardware configuration (S7-1500)

##### Procedure

1. Open the device configuration of the CPU or IM.
2. Select the device view.
3. Click on the module.

#### Counting operating mode (S7-1500)

In counting operating mode or in the counter configuration you can set the following parameters for each channel.

> **Note**
>
> Some of the parameters and options are not available for all digital modules. See the module's device manual for the associated parameters and options.

##### Channel enabled

You use this parameter to specify whether the respective channel is enabled or disabled.

Each channel is enabled by default.

##### Input delay

By configuring the input delay, you suppress signal errors at the digital inputs. Changes to the signal are only detected if they are constantly pending longer than the set input delay time.

Isochronous configuration is only possible if there is an input delay of 0.05 ms configured for at least one channel. In isochronous mode, the feedback interface is updated at the time T<sub>i</sub> (time for reading the input data).

You can select from the following options:

- 0.05 ms
- 0.1 ms
- 0.4 ms
- 0.8 ms
- 1.6 ms
- 3.2 ms (default)
- 12.8 ms
- 20 ms

> **Note**
>
> If you select the "0.05 ms" option for the input delay, you have to use shielded cables for connection of the digital inputs.

##### Reaction to violation of a counting limit

The following behavior can be configured for [Violation of the counter high limit in the upward direction or the counter low limit in the downward direction](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#behavior-at-the-counting-limits-s7-1500-1):

| Reaction | Meaning |
| --- | --- |
| Stop counting (default at ET200SP and ET200AL) | After a counting limit is violated, the internal gate is closed (automatic gate stop). As a result, the counting process is stopped and the module ignores any further counting signals. The counter value is set to the opposite counting limit. To restart counting, you must close and reopen the software/hardware gate. |
| Continue counting (default at S7-1500) | After a counting limit is violated, the counter value is set to the opposite counting limit and counting continues. |

##### Edge selection

This parameter is used to specify which edge the respective counter counts:

| Edge selection | Meaning |
| --- | --- |
| At rising edge (default) | The respective counter counts all rising edges at the digital input. |
| At falling edge | The respective counter counts all falling edges at the digital input. |
| At rising and falling edge | The respective counter counts all edges at the digital input. |

##### Count direction

Use this parameter to specify the counting direction of the respective counter.

You can select from the following options:

- Up
- Down

##### Set output

Use this parameter to specify the [Function](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#comparison-values-s7-1500-1) that controls the STS_DQ feedback bit. You can use the STS_DQ reset bit in order to control a digital output module's digital output.

You can select from the following options:

| Option | Meaning |
| --- | --- |
| Off (DQ = 0) | Regardless of the counter value, STS_DQ is permanently not set. |
| Off (DQ = 1) | Regardless of the counter value, STS_DQ is permanently set. |
| Between comparison value 0 and 1 | STS_DQ is set if the counter value between comparison values 0 and 1. |
| Not between comparison value 0 and 1 | STS_DQ is set if the counter value is outside the range between comparison values 0 and 1. |
| Between comparison value and counter high limit | STS_DQ is set if the counter value is between the comparison value and the counter high limit. |
| Between comparison value and counter low limit | STS_DQ is set if the counter value is between the comparison value and the counter low limit. |

##### Setting function of the DI

Use this parameter to specify which function the respective digital input DI<sub>n+4</sub> triggers.

You can select from the following options:

| Option | Meaning |
| --- | --- |
| Digital input without function | No function is assigned to the respective digital input DI<sub>n+4</sub>. The signal status of DI<sub>n+4</sub> can be read by the CPU using the feedback interface. |
| Gate start/stop | Setting the respective digital input DI<sub>n+4</sub> opens the [hardware gate](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#hardware-gate-s7-1500-1) for DI<sub>n</sub>. Resetting the respective digital input DI<sub>n+4</sub> closes the hardware gate for DI<sub>n</sub>. |
| Count direction | The respective DI<sub>n+4</sub> digital input determines the counting direction at DI<sub>n</sub>, in order to adjust it to the process. If DI<sub>n+4</sub> is not set, DI<sub>n</sub> counts up. If DI<sub>n+4</sub> is set, DI<sub>n</sub> counts down. |

> **Note**
>
> If "Count direction" is selected and the counting direction in the process changes, the counting edge is automatically adjusted (opposite edges).

##### High counting limit

You limit the counting range by setting the counter high limit. The maximum value for the counter high limit depends on the module:

| High counting limit | DI 8x24VDC HS,  DIQ 16x24VDC/0.5A 8xM12 | DI 32x24VDC HF,  DI 16x24VDC HF,  DI 16xNAMUR HF,  DI 16x24VDC HS |
| --- | --- | --- |
| Maximalwert | 2147483647 (2<sup>31</sup>–1) | 4294967295 (2<sup>32</sup>–1) |
| Voreinstellung | 2147483647 | 4294967295 |

You must enter a value that lies above the counter low limit.

##### Counter low limit

You limit the counting range by setting the counter low limit. The minimum value for the counter low limit depends on the module:

| Counter low limit | DI 8x24VDC HS,  DIQ 16x24VDC/0.5A 8xM12 | DI 32x24VDC HF,  DI 16x24VDC HF,  DI 16xNAMUR HF,  DI 16x24VDC HS |
| --- | --- | --- |
| Minimum value | –2147483648 (–2<sup>31</sup>) | 0 (not configurable) |
| Default | 0 | 0 |

You must enter a value below the counter high limit.

##### Start value

By configuring the start value, you specify the value at which counting is to start. You must enter a value between the counting limits or equal to the counting limits.

The default setting is "0".

##### Comparison value

By configuring a [comparison value](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#comparison-values-s7-1500-1), you specify the counter value that controls the STS_DQ reset bit based on the comparison function that was selected under "Set output".

You have to enter a value that is greater than or equal to the low counting limit as well as smaller than or equal to the high counting limit.

The default setting depends on the module:

| Comparison value | DI 8x24VDC HS,  DIQ 16x24VDC/0.5A 8xM12 | DI 32x24VDC HF,  DI 16x24VDC HF,  DI 16xNAMUR HF,  DI 16x24VDC HS |
| --- | --- | --- |
| Default | 10 | 1 |

##### Comparison value 0

By configuring a [comparison value](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#comparison-values-s7-1500-1), you specify the counter value that controls the STS_DQ reset bit based on the comparison function that was selected under "Set output".

You must enter a value which is greater than or equal to the counter low limit and less than comparison value 1.

The default setting is "0".

##### Comparison value 1

By configuring the second [comparison value](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#comparison-values-s7-1500-1), you specify the additional counter value that controls the STS_DQ reset bit based on the comparison function that was selected under "Set output".

You must enter a value which is greater than comparison value 0 and less than or equal to the counter high limit.

The default setting is "10".

##### Hardware gate

Use this parameter to specify the one-time counting process.

With the hardware gate, as with the software gate, you can start and stop the counting process with an external signal. If you use the hardware gate, the software gate must be enabled ("1").

Counting is stopped when the upper counting limit is violated. The count value jumps to the lower count limit (= 0).

##### Hardware interrupt: Comparison event for DQ occurred

With this parameter, you specify for S7-1500 and ET200AL whether a process alarm is given off when a comparison event occurs based on the comparison function that was selected under "Set output".

The hardware interrupt is not enabled in the default setting.

### Online & diagnostics module (S7-1500)

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

## Using SIMATIC Drive Controller (S7-1500)

This section contains information on the following topics:

- [Configuration and parameter assignment of SIMATIC Drive Controller (S7-1500)](#configuration-and-parameter-assignment-of-simatic-drive-controller-s7-1500)
- [Online & diagnostics module (S7-1500)](#online-diagnostics-module-s7-1500-2)

### Configuration and parameter assignment of SIMATIC Drive Controller (S7-1500)

This section contains information on the following topics:

- [Adding the SIMATIC Drive Controller to the hardware configuration (S7-1500)](#adding-the-simatic-drive-controller-to-the-hardware-configuration-s7-1500)
- [Open hardware configuration (S7-1500)](#open-hardware-configuration-s7-1500-2)
- [Event/period duration measurement operating mode (S7-1500)](#eventperiod-duration-measurement-operating-mode-s7-1500)

#### Adding the SIMATIC Drive Controller to the hardware configuration (S7-1500)

##### Requirements

The project has been created.

##### Procedure

1. Double-click "Add new device".   
   The "Add new object" dialog opens.
2. Select "Controller".
3. Select the SIMATIC Drive Controller:  
   "SIMATIC Drive Controller > CPU variant > Article number"
4. With the "Open device view" check box, you define whether the hardware configuration view should be opened after creation of a new device is completed. Leave the check box selected if you want to configure the CPU next.
5. Confirm with "OK".

#### Open hardware configuration (S7-1500)

##### Procedure

1. Select the device configuration item below the CPU in the project tree.   
   The device view opens.
2. Click on the interface DI/DQ 8x24VDC [X142] in the device view.   
   You can adapt the configurable properties in the Inspector window under Properties. Under Channel parameters, you will find an overview of all channels and their selected settings. To assign parameters to the desired channels, click on the arrow symbol after the channel number in the overview. Alternatively, you can also select the channel directly in the navigation.
3. Select the "Event/period duration measurement" operating mode for the desired channel.

#### Event/period duration measurement operating mode (S7-1500)

In [Event/period duration measurement operating mode](The%20basics%20of%20counting%2C%20measurement%20and%20position%20detection%20%28S7-1500%29.md#basics-of-counting-simatic-drive-controller-s7-1500), you can count positive edges and determine the period duration between two positive edges.

You can set the following parameters in event/period duration measurement operating mode:

##### Invert

You can invert the 24 V signal in order to adapt the signal to your process.

The signal is not inverted in the default setting.

##### Input delay

By configuring the input delay, you suppress signal errors at the digital inputs. Changes to the signal are only detected if they are constantly pending longer than the set input delay time.

To be able to record the very briefly pending signals at high counting frequencies, you need to set an input delay of 1 μs.

You can select from the following options:

- 125 μs (default)
- 1 μs

##### Isochronous mode

The event/period duration measurement requires isochronous operation.

You can find more information in the [SIMATIC Drive Controller system manual](https://support.industry.siemens.com/cs/ww/en/view/109766665).

### Online & diagnostics module (S7-1500)

This section contains information on the following topics:

- [Displaying and evaluating diagnostics (S7-1500)](#displaying-and-evaluating-diagnostics-s7-1500-2)

#### Displaying and evaluating diagnostics (S7-1500)

The online and diagnostics view enables hardware diagnostics. You can also

- Obtain information on the CPU or SINAMICS Integrated (e.g. Firmware version and serial number)
- Execute a firmware update if required

##### Procedure

To open the display editor for the diagnostic functions of the CPU, follow these steps:

1. Open the CPU folder in the project tree.
2. Double-click on the "Online & diagnostics" object.
3. Select the required display in the diagnostics navigation.

##### Additional information

You can find more information in the [SIMATIC Drive Controller system manual](https://support.industry.siemens.com/cs/ww/en/view/109766665).

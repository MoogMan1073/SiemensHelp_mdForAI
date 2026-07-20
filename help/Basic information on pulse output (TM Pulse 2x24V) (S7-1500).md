---
title: "Basic information on pulse output (TM Pulse 2x24V) (S7-1500)"
package: TFPulseTMPulseenUS
topics: 107
devices: [S7-1500, S7-1500T]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Basic information on pulse output (TM Pulse 2x24V) (S7-1500)

This section contains information on the following topics:

- [Pulse output (single pulse) mode (S7-1500)](#pulse-output-single-pulse-mode-s7-1500)
- [Pulse width modulation PWM mode (S7-1500)](#pulse-width-modulation-pwm-mode-s7-1500)
- [Pulse train mode (S7-1500)](#pulse-train-mode-s7-1500)
- [On/Off delay mode (S7-1500)](#onoff-delay-mode-s7-1500)
- [Frequency output mode (S7-1500)](#frequency-output-mode-s7-1500)
- [PWM with DC motor motor (S7-1500)](#pwm-with-dc-motor-motor-s7-1500)
- [Parallel connection of channels (S7-1500)](#parallel-connection-of-channels-s7-1500)
- [Direct control of digital outputs (S7-1500)](#direct-control-of-digital-outputs-s7-1500)
- [Handling of the SLOT parameters (S7-1500)](#handling-of-the-slot-parameters-s7-1500)

## Pulse output (single pulse) mode (S7-1500)

This section contains information on the following topics:

- [Function (S7-1500)](#function-s7-1500)
- [Configuring (S7-1500)](#configuring-s7-1500)
- [Reaction to CPU STOP (S7-1500)](#reaction-to-cpu-stop-s7-1500)
- [Parameter setting (S7-1500)](#parameter-setting-s7-1500)
- [Address space (S7-1500)](#address-space-s7-1500)
- [Control and feedback interface (S7-1500)](#control-and-feedback-interface-s7-1500)
- [Isochronous mode (S7-1500)](#isochronous-mode-s7-1500)

### Function (S7-1500)

This section contains information on the following topics:

- [Introduction (S7-1500)](#introduction-s7-1500)
- [Output sequence (S7-1500)](#output-sequence-s7-1500)
- [Pulse duration (S7-1500)](#pulse-duration-s7-1500)
- [On delay (S7-1500)](#on-delay-s7-1500)
- [Sequence counter (S7-1500)](#sequence-counter-s7-1500)
- [High-speed output (S7-1500)](#high-speed-output-s7-1500)

#### Introduction  (S7-1500)

In this operating mode, the respective channel of the technology module outputs a single pulse with the configured On delay and the pulse duration specified via the control interface.

#### Output sequence  (S7-1500)

##### Starting the output sequence

In order to output the output sequence at digital output DQn.A, the TM_CTRL_DQ control bit must be set. To start the output sequence using the software enable, you set the SW_ENABLE [control bit](#assignment-of-the-control-interface-s7-1500). The STS_SW_ENABLE [feedback bit](#assignment-of-the-feedback-interface-s7-1500) indicates that the software enable in the technology module is active.

You can additionally use the hardware enable via the respective digital input DIn.0. You can configure an input delay for DIn.0.

**Pulse diagram**

The following figure shows an example of an output sequence when DIn.0 is being used as a hardware enable.

![Example of an output sequence](images/115793594891_DV_resource.Stream@PNG-en-US.png)

Example of an output sequence

If you are using the hardware enable, it is combined with the software enable. When the software enable is active, the output sequence starts at the first positive edge of the hardware enable. Additional positive edges of the hardware enable during the output sequence are ignored. If the hardware enable is set and remains set for the duration of the input delay, the On delay is started and the STS_ENABLE feedback bit is set. As soon as the On delay has elapsed, the pulse is output with the assigned pulse duration at the respective digital output DQn.A. The output sequence is stopped at the end of the pulse duration, and STS_ENABLE is reset.

If you are not using a hardware enable, the On delay starts at the positive edge of SW_ENABLE.

##### Aborting the output sequence

If you reset the SW_ENABLE control bit, the software enable is deactivated and the current output sequence is aborted and not completed. The STS_ENABLE feedback bit and the digital output DQn.A are reset.

A renewed pulse output is only possible after a restart of the output sequence.

#### Pulse duration  (S7-1500)

The pulse duration is the time period that the digital output DQn.A remains set after the On delay has elapsed.

You set the pulse duration in µs in the control interface using OUTPUT_VALUE as integer (UDINT). The value range is dependent on whether or not the high-speed output function is being used:

| High-speed output | Value range of  OUTPUT_VALUE | Value range of the pulse duration |
| --- | --- | --- |
| Activated | 2 ... 85000000 | 2 ... 85000000 μs = 2 μs ... 85 s |
| Deactivated | 10 ... 85000000 | 10 ... 85000000 μs = 10 μs ... 85 s |

##### Pulse duration change while output sequence is active

If you change the pulse duration to a value that is greater than the pulse duration already elapsed, the change takes effect immediately. Thus, you can still adapt the pulse duration during the output sequence.

If you change the pulse duration to a value that is less than the portion of the pulse duration that already elapsed, the output sequence is aborted. In this case, the STS_ENABLE feedback bit and the digital output DQn.A are reset, and the ERR_PULSE feedback bit is set. To continue the pulse output, you must restart the output sequence. At the next start of the output sequence, the technology module resets the ERR_PULSE feedback bit again.

#### On delay (S7-1500)

You set the On delay from 0 to 85 s with a precision of 1 µs in the hardware configuration.

In addition, you can change the On delay via the control interface by entering a new value in SLOT as an integer (UDINT). In so doing, you use the MODE_SLOT control bit to choose whether you want to apply a change once or cyclically:

| Symbol | Meaning |
| --- | --- |
| MODE_SLOT = 0 | One-time change: As soon as you write the value 2<sub>D</sub> in the corresponding output byte, the value from SLOT is applied once as the On delay and kept until the next change.  A change via SLOT takes effect at the next output sequence. An active output sequence is not affected by the change. |
| MODE_SLOT = 1 | Cyclic change: When you write the value 18<sub>D</sub> in the corresponding output byte, the current value from SLOT in each case is applied cyclically as the On delay.  A change via SLOT takes effect at the next output sequence. An active output sequence is not affected by the change. |

For more detailed information, refer to the section  Handling the SLOT parameters.

#### Sequence counter (S7-1500)

The technology module has one sequence counter per channel, which counts the completed output sequences. Output sequences that were successfully completed as well those that were not successfully completed are counted. When the HW enable is being used, there is a possibility of very short output sequences that are not reliably detected by the CPU. With the help of the sequence counter, a check can be made in the user program to determine whether output sequences were initiated.

The number of output sequences is supplied in the [feedback interface](#assignment-of-the-feedback-interface-s7-1500) using the value SEQ_CNT. You can monitor the completion of an output sequence with this value.

When the HW enable is being used, the sequence counter counts from 0 to 15. When the HW enable is not being used, the output sequence is started exclusively by the SW_ENABLE control bit, and the sequence counter therefore counts only to 1.

The counter returns to 0 as soon as SW_ENABLE is reset as well as after an overflow.

#### High-speed output (S7-1500)

The high-speed output function enables an output frequency of a maximum of 100 kHz with an output current of a maximum of 100 mA. A high-speed output generates very steep edges. The high-speed output generates signals at a higher frequency, but provides a lower maximum load current. The high-speed output is only available in two-channel operation.

The following table presents the value range of the pulse duration and frequency depending on whether or not the high-speed output function is activated:

|  | Minimum value |  | Maximum value |  |
| --- | --- | --- | --- | --- |
| High-speed output deactivated | High-speed output activated | High-speed output deactivated | High-speed output activated |  |
| Pulse duration | 10 μs | 1,5 μs | 85000000 μs (= 85 s) |  |
| Frequency | 0,02 Hz |  | 10 kHz | 100 kHz |

### Configuring (S7-1500)

#### Introduction

You configure the technology module and assign its parameters with the configuration software.

The user program controls and monitors the functions of the technology module via the control interface and feedback interface.

#### System environment

The technology module can be used in the following system environments:

| Possible use | Components needed | Configuration software | In the user program |
| --- | --- | --- | --- |
| Centralized operation with a CPU 151xSP | - ET 200SP automation system - TM Pulse 2x24V | STEP 7 (TIA Portal):  Device configuration and parameter setting with hardware configuration | Direct access to control interface and feedback interface in the I/O data |
| Distributed operation with an S7-1500 CPU | - S7-1500 automation system - ET 200SP distributed I/O system - TM Pulse 2x24V | STEP 7 (TIA Portal):  Device configuration and parameter setting with hardware configuration |  |
| Distributed operation with an S7-300/400 CPU | - S7-300/400 automation system - ET 200SP distributed I/O system - TM Pulse 2x24V | STEP 7 (TIA Portal):  Device configuration and parameter setting with hardware configuration  STEP 7:  Device configuration and parameter setting with HSP |  |
| Distributed operation on the PROFINET IO in a third-party system | - Third-party automation system - ET 200SP distributed I/O system - TM Pulse 2x24V | Third-party configuration software:   Device configuration and parameter setting with GSD file |  |
| Distributed operation on the PROFIBUS DP in a third-party system | - Third-party automation system - ET 200SP distributed I/O system - TM Pulse 2x24V | Third-party configuration software:  GSD file; device configuration and parameter setting using data record 128 |  |

#### Hardware Support Packages (HSP)

**STEP 7**

The Hardware Support Packages (HSP) are available for download on the [Internet](https://support.industry.siemens.com/cs/ww/en/view/23183356).

#### GSD file

The respective GSD file for the ET 200SP distributed I/O system is available for download on the Internet:

- [GSD file PROFINET IO](http://support.automation.siemens.com/WW/view/en/57138621)
- [GSD file PROFIBUS DP](http://support.automation.siemens.com/WW/view/en/73016883)

### Reaction to CPU STOP (S7-1500)

You set the response of the channel to a CPU STOP in the parameters of the device configuration.

Response of channel to CPU STOP

| Option | Meaning |
| --- | --- |
| Output substitute value | The channel outputs the configured substitute values at the digital outputs until the next STOP-RUN transition of the CPU. You can configure the substitute value 1 for only one of the two digital outputs.  An active output sequence is stopped and the STS_ENABLE feedback bit is reset.  The technology module is set to its startup state after a STOP-RUN transition. Before you can start a new pulse output, you must reset the SW_ENABLE control bit. |
| Continue operation | The channel continues to operate.  The digital outputs continue to switch according to the parameter assignment. An active output sequence will thus be continued. If you have configured the hardware enable, you can also start additional output sequences using DIn.0.  The configuration of the technology module is not reset after a STOP-RUN transition. |

### Parameter setting (S7-1500)

You use various parameters to specify the properties of the technology module. Depending on the settings, not all parameters are available. When parameters are assigned in the user program, the parameters are transferred to the module with the "WRREC" instruction and data record 128.

You set the parameters of the module as follows in this operating mode:

| Parameter setting via... | Basic procedure |
| --- | --- |
| Hardware configuration in STEP 7 (TIA Portal) | 1. Insert the module from the hardware catalog under "Technology modules". 2. Set the "Pulse output" mode and the further parameters of the module in the hardware configuration. 3. Download the project to the CPU. |
| Hardware configuration in STEP 7 with HSP | 1. Install the corresponding HSP file. You will then find the module in the hardware catalog under "ET 200SP". 2. Set the "Pulse output" mode and the further parameters of the module in the hardware configuration. 3. Download the project to the CPU. |
| Hardware configuration with GSD file for distributed operation on PROFINET IO | 1. Install the latest PROFINET GSD file. You will then find the module in the hardware catalog under "Other field devices &gt; PROFINET IO &gt; I/O". 2. Set the "Pulse output" mode and the further parameters of the module in the hardware configuration. 3. Download the project to the CPU. |
| Hardware configuration with GSD file for distributed operation on PROFIBUS DP | 1. Install the latest PROFIBUS GSD file. You will then find the module in the hardware catalog under "Other field devices &gt; PROFIBUS DP &gt; I/O". 2. Download the project to the CPU. The parameters of the module are also downloaded with their default settings (see table below). 3. Set the "Pulse output" mode and the further parameters in the user program using data record 128. |

#### Parameters of the TM Pulse 2x24V in "Pulse output" mode

The default settings of the parameters are shown in bold in the "Value range" column.

Adjustable parameters

| Parameter | Value range | Scope |
| --- | --- | --- |
| Channel configuration<sup>1</sup> | - **2 channels (2 A)** - 1 channel (4 A) | Module |
| Reaction to CPU STOP | - **Output substitute value** - Continue operation | Channel |
| Substitute value for DQA | - **0** - 1 | Channel |
| Substitute value for DQB | - **0** - 1 | Channel |
| Group diagnostics | - **Deactivated** - Activated | Channel |
| Diagnostics DQA | - **Deactivated** - Activated | Channel |
| Diagnostics DQB | - **Deactivated** - Activated | Channel |
| High-speed output (0.1 A) | - **Deactivated** - Activated | Channel |
| Function DI | - **Input** - HW enable | Channel |
| Input delay for digital inputs | - None - 0.05 ms - **0.1 ms** - 0.4 ms - 0.8 ms - 1.6 ms - 3.2 ms - 12.8 ms - 20 ms | Channel |
| Output format | - S7 analog output - **1/100** - 1/1000 - 1/10000 | Channel |
| On delay for pulse output | **0**...85000000 μs | Channel |
| <sup>1</sup> When configuring with HSP for STEP 7 or with a GSD file, you define the channel configuration by the selection of the module name. |  |  |

> **Note**
>
> **PROFIBUS GSD configuration**
>
> When configuring with a PROFIBUS GSD file, the possible parameter assignments are not available. The parameters are preassigned in the module with the default setting. Set the "Pulse output" mode and the further parameters in the user program using data record 128.

### Address space (S7-1500)

#### Address space of the technology module

Size of input and output addresses

|  | Inputs | Outputs |
| --- | --- | --- |
| Size per technology channel | 8 bytes | 12 bytes |
| Size in one-channel operation | 8 bytes | 12 bytes |
| Size in two-channel operation | 16 bytes | 24 bytes |

### Control and feedback interface (S7-1500)

This section contains information on the following topics:

- [Library with PLC data types (S7-1500)](#library-with-plc-data-types-s7-1500)
- [Assignment of the control interface (S7-1500)](#assignment-of-the-control-interface-s7-1500)
- [Assignment of the feedback interface (S7-1500)](#assignment-of-the-feedback-interface-s7-1500)

#### Library with PLC data types (S7-1500)

> **Note**
>
> A library of PLC data types (LPD) for STEP 7 (TIA Portal) and SIMATIC S7-1200 / S7-1500 is available for download on the [Internet](https://support.industry.siemens.com/cs/ww/en/view/109482396).

#### Assignment of the control interface (S7-1500)

The user program uses the control interface to influence the behavior of the technology module.

##### Control interface per channel

The following table shows the control interface assignment:

| Byte offset relative to start address Channel 0/1 **↓ ↓** |  | Bit 7 | Bit 6 | Bit 5 | Bit 4 | Bit 3 | Bit 2 | Bit 1 | Bit 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 … 3 | 12 … 15 | OUTPUT_VALUE  UDINT: Pulse duration |  |  |  |  |  |  |  |
| 4 … 7 | 16 … 19 | SLOT  UDINT: Load value |  |  |  |  |  |  |  |
| 8 | 20 | Reserved |  |  | MODE_ SLOT | LD_SLOT |  |  |  |
| 9 | 21 | Reserved |  |  | SET_DQB | SET_DQA | Reserved | TM_ CTRL_DQ | SW_ ENABLE |
| 10 | 22 | Reserved |  |  |  |  |  |  | RES_ ERROR |
| 11 | 23 | Reserved |  |  |  |  |  |  |  |

> **Note**
>
> Channel 1 is only available in two-channel operation of the module.

| Control bit/value | Explanations |
| --- | --- |
| OUTPUT_VALUE | You specify the pulse duration with this value.  Value range:  - Pulse duration in μs when high-speed output is deactivated: 10 to 85000000<sub>D</sub> - Pulse duration in μs when high-speed output is activated: 2 to 85000000<sub>D</sub>   If the pulse duration setting is outside the value range, the ERR_OUT_VAL feedback bit is set and the last valid pulse duration is used. |
| SLOT | You specify the load value with this value.  Value range:   - On delay in μs: 0 to 85000000<sub>D</sub>   You specify whether to apply a change once or cyclically with MODE_SLOT.  Invalid values trigger setting of feedback bit ERR_LD (when MODE_SLOT = 0) or ERR_SLOT_VAL (when MODE_SLOT = 1). |
| MODE_SLOT | You specify whether you want to apply a change in SLOT once or cyclically with this bit.  0 means: As soon as you write the value 2<sub>D</sub> in the corresponding output byte, the value from SLOT is applied once as the On delay and kept until the next change. A change via SLOT takes effect at the next output sequence. After a restart of the module, the value is overwritten with the value set in the hardware configuration.   1 means: When you write the value 18<sub>D</sub> in the corresponding output byte, the current value from SLOT in each case is applied cyclically. A change via SLOT takes effect at the next output sequence. |
| LD_SLOT | You specify the meaning of the value in SLOT with this load request:  - 0000<sub>B</sub> means: No action, idle - 0010<sub>B</sub> means: On delay in μs   Values not listed are invalid and trigger setting of feedback bit ERR_LD (when MODE_SLOT = 0) or ERR_SLOT_VAL (when MODE_SLOT = 1). |
| SET_DQA | You use this bit to set digital output DQn.A when TM_CTRL_DQ and SET_DQB are set to 0. |
| SET_DQB | You use this bit to set digital output DQn.B when TM_CTRL_DQ and SET_DQA are set to 0. |
| TM_CTRL_DQ | You enable the technological function of the digital output with this bit.   - 0 means: SET_DQA and SET_DQB define states of DQn.A and DQn.B - 1 means: Output sequence defines the state of DQn.A; DQn.B is always 0. |
| SW_ENABLE | You activate the software enable with this bit. If you are using the hardware enable, it is combined with the software enable.  - 0 means: Stop output - 1 means: Start output   Use of the HW enable is activated through parameter assignment. The HW enable is controlled externally using the digital input DIn.0. |
| RES_ERROR | You use this bit to reset the following feedback bits when errors are pending:  - ERR_24V - ERR_DQA - ERR_DQB - ERR_LD |
| Reserved | Reserved bits must be set to 0. |

#### Assignment of the feedback interface (S7-1500)

The user program receives current values and status information from the technology module via the feedback interface.

##### Feedback interface per channel

The following table shows the assignment of the feedback interface:

| Byte offset relative to start address Channel 0/1 **↓ ↓** |  | Bit 7 | Bit 6 | Bit 5 | Bit 4 | Bit 3 | Bit 2 | Bit 1 | Bit 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 8 | ERR_ SLOT_VAL | ERR_ OUT_VAL | ERR_DQB | ERR_DQA | ERR_ PULSE | ERR_LD | ERR_24V | ERR_PWR |
| 1 | 9 | Reserved |  | STS_SW_ ENABLE | STS_ READY | Reserved | STS_LD_ SLOT | Reserved |  |
| 2 | 10 | Reserved |  |  |  | STS_DI | STS_DQB | STS_DQA | STS_ ENABLE |
| 3 | 11 | Reserved |  |  |  | SEQ_CNT |  |  |  |
| 4 ... 7 | 12 ... 15 | Reserved |  |  |  |  |  |  |  |

> **Note**
>
> Channel 1 is only available in two-channel operation of the module.

| Feedback bit/value | Explanations |
| --- | --- |
| ERR_SLOT_VAL | This bit indicates that the value in SLOT or LD_SLOT is invalid (when MODE_SLOT = 1) and was not accepted.   As soon as the module has received a valid value from the control interface, ERR_SLOT_VAL is automatically reset. |
| ERR_OUT_VAL | This bit indicates that the value in OUTPUT_VALUE is invalid.  As soon as the module has received a valid value from the control interface, ERR_OUT_VAL is automatically reset. |
| ERR_DQA | This bit indicates a short-circuit or an overload at the output DQn.A. If you have enabled the diagnostics interrupt "Diagnostics DQA", the diagnostics interrupt "Error at digital outputs" is triggered when this error occurs.   The bit is reset once you have acknowledged the error with RES_ERROR. |
| ERR_DQB | This bit indicates a short-circuit or an overload at the output DQn.B or the attempted simultaneous setting of the SET_DQA and SET_DQB control bits. If you have enabled the diagnostics interrupt "Diagnostics DQB", the diagnostics interrupt "Error at digital outputs" is triggered when this error occurs.   The bit is reset once you have acknowledged the error with RES_ERROR. |
| ERR_PULSE | This bit indicates an error in the pulse output, e.g. new pulse duration value is too low. |
| ERR_LD | This bit indicates that the value in SLOT or LD_SLOT (when MODE_SLOT = 0) is invalid and was not accepted.   The bit is reset once you have acknowledged the error with RES_ERROR. |
| ERR_24V | This bit indicates a short-circuit or an overload at output 24VDC If you have enabled diagnostic interrupts, the diagnostic interrupt "Short circuit / overload of the sensor supply voltage" is triggered when this error occurs.   The bit is reset once you have acknowledged the error with RES_ERROR. |
| ERR_PWR | This bit indicates that supply voltage L+ is too low. If you have enabled the diagnostic interrupts, the diagnostic interrupt "Supply voltage fault" is triggered when an error occurs.   As soon as supply voltage L+ is sufficiently high again, ERR_PWR is automatically reset.  The bit is not set if no supply voltage is present. |
| STS_SW_ENABLE | This bit indicates the status of the SW enable.   - 0 means: SW enable not active - 1 means: SW enable active |
| STS_READY | This bit indicates that the module is supplying valid user data. The module is started and configured. |
| STS_LD_SLOT | A status change (toggling) of this bit indicates that the LD_SLOT load request was detected and executed (when MODE_SLOT = 0). |
| STS_DI | This bit indicates the status of the digital input DIn.0. |
| STS_DQA | This bit indicates the status of the digital output DQn.A. |
| STS_DQB | This bit indicates the status of the digital output DQn.B. |
| STS_ENABLE | This bit indicates that an output sequence is active. |
| SEQ_CNT | This value indicates the number of completed output sequences as sequence counter. |
| Reserved | Reserved bits are set to 0. |

### Isochronous mode (S7-1500)

The technology module supports the "Isochronous mode" system function. If you are not using a hardware enable, the output sequence starts in isochronous mode at time T<sub>o</sub> after the SW_ENABLE control bit has been set.

#### Further information

You will find a detailed description of isochronous mode in:

- In the isochronous mode function manual as a download from the [Internet](https://support.industry.siemens.com/cs/ww/en/view/109755401).
- PROFINET with STEP 7 function manual available for download on the [Internet](https://support.industry.siemens.com/cs/ww/en/view/49948856).

## Pulse width modulation PWM mode (S7-1500)

This section contains information on the following topics:

- [Function (S7-1500)](#function-s7-1500-1)
- [Configuring (S7-1500)](#configuring-s7-1500-1)
- [Reaction to CPU STOP (S7-1500)](#reaction-to-cpu-stop-s7-1500-1)
- [Parameter setting (S7-1500)](#parameter-setting-s7-1500-1)
- [Address space (S7-1500)](#address-space-s7-1500-1)
- [Control interface and feedback interface (S7-1500)](#control-interface-and-feedback-interface-s7-1500)
- [Isochronous mode (S7-1500)](#isochronous-mode-s7-1500-1)

### Function (S7-1500)

This section contains information on the following topics:

- [Introduction (S7-1500)](#introduction-s7-1500-1)
- [Output sequence (S7-1500)](#output-sequence-s7-1500-1)
- [Duty cycle (S7-1500)](#duty-cycle-s7-1500)
- [Period duration (S7-1500)](#period-duration-s7-1500)
- [On delay (S7-1500)](#on-delay-s7-1500-1)
- [Dithering (S7-1500)](#dithering-s7-1500)
- [Current measurement/control (S7-1500)](#current-measurementcontrol-s7-1500)
- [Minimum pulse duration and minimum interpulse period (S7-1500)](#minimum-pulse-duration-and-minimum-interpulse-period-s7-1500)
- [High-speed output (S7-1500)](#high-speed-output-s7-1500-1)

#### Introduction  (S7-1500)

In this operating mode, the respective channel of the technology module outputs a pulse width modulated signal with the configured minimum pulse duration and the configured period duration. You can superimpose a dither signal on the PWM signal. The module also has an integrated PID controller that can be used to control the output current.

You specify the duty cycle or current setpoint via the control interface.

#### Output sequence (S7-1500)

##### Starting the output sequence

In order to output the output sequence at digital output DQn.A, the TM_CTRL_DQ control bit must be set. To start the output sequence using the software enable, you set the SW_ENABLE [control bit](#assignment-of-the-control-interface-s7-1500-1). The STS_SW_ENABLE [feedback bit](#assignment-of-the-feedback-interface-s7-1500-1) indicates that the software enable in the technology module is active.

You can additionally use the hardware enable via the respective digital input DIn.0. You can configure an input delay for DIn.0.

**Pulse diagram**

The following figure shows an example of an output sequence when DIn.0 is being used as a hardware enable.

![Example of an output sequence](images/117449422475_DV_resource.Stream@PNG-en-US.png)

Example of an output sequence

If you are using the hardware enable, it is combined with the software enable. When the software enable is active, the output sequence starts at the first rising edge of the hardware enable. Additional rising edges of the hardware enable during the output sequence are ignored. If the hardware enable is set and remains set for the duration of the input delay, the On delay is started and the STS_ENABLE feedback bit is set. As soon as the On delay has elapsed, the pulse width modulated signal is output with the assigned duty cycle at the respective digital output DQn.A. The duty cycle is the ratio of pulse duration to period duration. The output sequence runs continuously, as long as SW_ENABLE is set.

If you are not using a hardware enable, the On delay starts at the rising edge of SW_ENABLE. The hardware enable is not supported in isochronous mode.

##### Aborting the output sequence

If you reset the SW_ENABLE control bit, the software enable is deactivated and the current output sequence is aborted. The last period is not completed. The STS_ENABLE feedback bit and the digital output DQn.A are reset.

A renewed pulse output is only possible after a restart of the output sequence.

#### Duty cycle (S7-1500)

The duty cycle corresponds to the ratio of pulse duration to period duration (also referred to as mark-to-space ratio).

You set the duty cycle in the [control interface](#assignment-of-the-control-interface-s7-1500-1) using OUTPUT_VALUE as integer (UDINT). The value range is dependent on the configured output format. If you set the value 0, the DQn.A is not set during the entire period duration. If you set the maximum value, the DQn.A is set during the entire period duration. If you set a value above the value range, the maximum value is used.

| Output format | Value range of  OUTPUT_VALUE | Pulse duration |
| --- | --- | --- |
| 1/100 (%) | 0 ... 100 | (OUTPUT_VALUE/100) × Period duration |
| 1/1000 (‰) | 0 ... 1000 | (OUTPUT_VALUE/1000) × Period duration |
| 1/10000 | 0 ... 10000 | (OUTPUT_VALUE/10000) × Period duration |
| S7 analog output | 0 ... 27648 | (OUTPUT_VALUE/27648) × Period duration |

A changed duty cycle takes effect with the next rising edge at DQn.A.

> **Note**
>
> **Current control**
>
> If you are using [current control](#current-measurementcontrol-s7-1500), the module controls the duty cycle, and the current setpoint is assigned using OUTPUT_VALUE.

#### Period duration (S7-1500)

You set the period duration in µs in the hardware configuration. The value range is dependent on whether or not the high-speed output function is being used:

| High-speed output | Value range of the period duration |
| --- | --- |
| Activated | 10 ... 85000000 μs  = 10 μs ... 85 s |
| Deactivated | 100 ... 85000000 μs  = 100 μs ... 85 s |

In addition, you can change the period duration via the control interface by entering a new value in SLOT as an integer (UDINT). In so doing, you use the MODE_SLOT control bit to choose whether you want to apply a change once or cyclically:

| Symbol | Meaning |
| --- | --- |
| MODE_SLOT = 0 | One-time change: As soon as you write the value 1<sub>D</sub> in the corresponding output byte, the value from SLOT is applied once as the period duration and kept until the next change.  A period duration that has been changed using SLOT takes effect at the next positive edge at DQn.A. |
| MODE_SLOT = 1 | Cyclic change: When you write the value 17<sub>D</sub> in the corresponding output byte, the current value from SLOT in each case is applied cyclically as the period duration.  A period duration that has been changed using SLOT takes effect at the next positive edge at DQn.A. |

For more detailed information, refer to the section  Handling the SLOT parameters.

#### On delay (S7-1500)

You set the On delay from 0 s to 85 s with a precision of 1 µs in the hardware configuration.

In addition, you can change the On delay via the control interface by entering a new value in SLOT as an integer (UDINT). In so doing, you use the MODE_SLOT control bit to choose whether you want to apply a change once or cyclically:

| Symbol | Meaning |
| --- | --- |
| MODE_SLOT = 0 | One-time change: As soon as you write the value 2<sub>D</sub> in the corresponding output byte, the value from SLOT is applied once as the On delay and kept until the next change.  A change via SLOT takes effect at the next output sequence. An active output sequence is not affected by the change. |
| MODE_SLOT = 1 | Cyclic change: When you write the value 18<sub>D</sub> in the corresponding output byte, the current value from SLOT in each case is applied cyclically as the On delay.  A change via SLOT takes effect at the next output sequence. An active output sequence is not affected by the change. |

For more detailed information, refer to the section  Handling the SLOT parameters.

> **Note**
>
> In isochronous mode, a configured On delay has no effect.

#### Dithering (S7-1500)

The dither function is specially designed for control of proportional valves. The dither function superimposes an adjustable symmetrical variation on the setpoint for control of the valve solenoid. This results in a minimal motion around the set position and prevents the valve from sticking due to stiction or hysteresis effect. This improves the reaction to setpoint changes.

You set the parameters for the dithering in the hardware configuration. You activate the dithering using the DITHER bit in the [control interface](#assignment-of-the-control-interface-s7-1500-1).

##### Dithering amplitude

The dithering amplitude is the amplitude of the dither signal in relation to the period duration of the output sequence. The value range is 0 to 50%. If you set a value above the value range, a dithering amplitude of 50% is used.

The module dynamically adjusts the dithering amplitude when the determined effective duty cycle is greater than 100% or less than 0% so that the dither signal remains symmetrical.

Examples:

With a dithering amplitude of 10% and a duty cycle of 50%, the effective duty cycle of the output sequence varies periodically between 40% and 60%.

With a dithering amplitude of 10% and a duty cycle of 95%, the effective duty cycle of the output sequence varies periodically between 90% and 100%.

In addition, you can change the dithering amplitude via the control interface by entering a new value in SLOT as integer (UDINT). In so doing, you can use the MODE_SLOT control bit to choose whether you want to apply a change once or cyclically:

| Symbol | Meaning |
| --- | --- |
| MODE_SLOT = 0 | One-time change: As soon as you write the value 6<sub>D</sub> in the corresponding output byte, the value from SLOT is applied once as the dithering amplitude.  A change using SLOT takes effect after a stop and restart of the dithering. |
| MODE_SLOT = 1 | Cyclic change: When you write the value 22<sub>D</sub> in the corresponding output byte, the current value from SLOT in each case is applied cyclically as the dithering amplitude.  A change using SLOT takes effect after a stop and restart of the dithering. |

##### Dithering period duration

The dithering period duration is the period duration of the dither signal. The value must be at least 4 times the period duration of the PWM signal and greater than 2 ms. The maximum value is 100 ms. If you set a value above the value range, a dithering period duration of 100 ms is used.

The module uses only a multiple of the period duration of the PWM signal as the dithering period duration. The module adjusts the assigned value of the period duration in such a way that the next higher or lower multiple is used.

In addition, you can change the dithering period duration via the control interface by entering a new value in SLOT as integer (UDINT). In so doing, you can use the MODE_SLOT control bit to choose whether you want to apply a change once or cyclically:

| Symbol | Meaning |
| --- | --- |
| MODE_SLOT = 0 | One-time change: As soon as you write the value 7<sub>D</sub> in the corresponding output byte, the value from SLOT is applied once as the dithering period duration.  A change using SLOT takes effect after a stop and restart of the dithering. |
| MODE_SLOT = 1 | Cyclic change: When you write the value 23<sub>D</sub> in the corresponding output byte, the current value from SLOT in each case is applied cyclically as the dithering period duration.  A change using SLOT takes effect after a stop and restart of the dithering. |

> **Note**
>
> If you increase the period duration of the PWM signal during an active output sequence in such a way that the dithering period duration is less than 4 times as large, the dither signal will be deactivated.

> **Note**
>
> **Isochronous mode**
>
> In isochronous mode, for the best possible results you should set an integral multiple of the application cycle for the dithering period duration.

##### Incline of dithering ramp up and down

Incline of dithering ramp up: This parameter is the slope of the ramp up of the dithering amplitude for a theoretical increase of amplitude from 0% to 100%.

Incline of dithering ramp down: This parameter is the slope of the ramp down of the dithering amplitude for a theoretical decrease of amplitude from 100% to 0%.

The value range is 0 to 30000 ms in each case. If you set a value above the value range, a value of 30000 ms is used for the incline.

The respective incline influences the effective ramp time. Example: A dithering amplitude of 10% and an incline of 2500 ms/100% yields the following effective ramp time:

10 % × 2500 ms/100 % = 250 ms

In addition, you can change the incline of the ramp up and the ramp down jointly via the control interface by entering a new value in SLOT as integer (INT twice). In so doing, you can use the MODE_SLOT control bit to choose whether you want to apply a change once or cyclically:

| Symbol | Meaning |
| --- | --- |
| MODE_SLOT = 0 | One-time change: As soon as you write the value 5<sub>D</sub> in the corresponding output byte, the value from SLOT (LOWWORD) is applied once as the incline of the ramp up and the value from SLOT (HIGHWORD) is applied once as the incline of the ramp down.  A change using SLOT takes effect after a stop and restart of the dithering. |
| MODE_SLOT = 1 | Cyclic change: When you write the value 21<sub>D</sub> in the corresponding output byte, the current value from SLOT (LOWWORD) is applied cyclically in each case as incline of the ramp up and the value from SLOT (HIGHWORD) is applied in each case as incline of the ramp down.  A change using SLOT takes effect after a stop and restart of the dithering. |

##### Starting and stopping dithering

The dithering starts with the configured ramp up as soon as the DITHER bit is set in the [control interface](#assignment-of-the-control-interface-s7-1500-1) during an active output sequence and a new dithering period duration starts. After the start of the dithering, the STS_DITHER bit is set in the [feedback interface](#assignment-of-the-feedback-interface-s7-1500-1).

As soon as you reset the DITHER bit, the configured ramp down begins with the subsequent dithering period duration. After the ramp down finishes, the STS_DITHER bit is reset.

If the output sequence is aborted, the dithering is also aborted and the STS_DITHER bit is reset.

The following figure shows an example of an output sequence with a duty cycle of 50% without dithering.

![Starting and stopping dithering](images/118685489547_DV_resource.Stream@PNG-en-US.png)

The following figure shows an example of an output sequence with the following properties:

- Duty cycle = 50%
- Dithering period duration = 6 × Period duration of the PWM signal
- No ramp up/down

![Starting and stopping dithering](images/118685498763_DV_resource.Stream@PNG-en-US.png)

The following figure shows an example of an output sequence with the following properties:

- Duty cycle = 50%
- Dithering period duration = 6 × Period duration of the PWM signal
- With ramp up

![Starting and stopping dithering](images/118685494155_DV_resource.Stream@PNG-en-US.png)

The following figure shows an example of an output sequence with the following properties:

- Duty cycle = 50%
- Dithering period duration = 6 × Period duration of the PWM signal
- With ramp down

![Starting and stopping dithering](images/118685484939_DV_resource.Stream@PNG-en-US.png)

#### Current measurement/control (S7-1500)

##### Current measurement

The technology module measures the load current at the digital output. The measured value of the current is returned as an S7 analog value in the MEASURED_CURRENT value in the [feedback interface](#assignment-of-the-feedback-interface-s7-1500-1).

A valid measured value is available when the STS_ENABLE feedback bit is set after the first period duration of the output sequence. The returned measured value is an average of the measured values that were acquired over a time period of at least one period duration. If a valid measured value is not available, the value 32767<sub>D</sub> is returned.

When dithering is active, the average is for the time period of an entire dithering period duration.

> **Note**
>
> In order to use the current measurement, the high-speed output must be deactivated.

**Measuring range and accuracy**

The measuring range and accuracy are dependent on the channel configuration:

|  | Measured value 27648<sub>D</sub> | Maximum measured value 32511<sub>D</sub> | Accuracy<sup>3</sup> |  |
| --- | --- | --- | --- | --- |
| Period duration &gt; 333 μs | Period duration &lt; 333 μs |  |  |  |
| Two-channel operation | 2 A<sup>1</sup> | 2.37 A<sup>2</sup> | ±40 mA | -40 mA ... +100 mA |
| One-channel operation  (parallel connection) | 4 A<sup>1</sup> | 4.74 A<sup>2</sup> | ±80 mA | -80 mA ... +200 mA |
| <sup>1 </sup>May only be exceeded for a short time.   <sup>2 </sup>When this current value is exceeded, the ERR_DQA feedback bit will be set.   <sup>3 </sup>With constant period duration in the respective measuring period. |  |  |  |  |

##### Current control

You can use the current control function to proportionally control the power transferred to an inductive or resistive load. Thermal effects are automatically regulated out.

The setpoint of the current is specified by the user program. The module controls the duty cycle of the PWM signal according to the setpoint and the reaction depends on the PID parameters.

The PID controller compares the setpoint and the measured value of the load current to one another. If the resulting difference is outside a symmetrical dead band, a reaction of the controller is calculated by taking into account the enabled components of the PID controller (proportional, integral and/or differential).

The calculated manipulated variable value is subject to defined high and low limits. If the manipulated variable value reaches a limit, the user program reads this in the [feedback interface](#assignment-of-the-feedback-interface-s7-1500-1) via the QLMN_HLM and QLMN_LLM bits.

You set the parameters for the current control in the hardware configuration. The value of OUTPUT_VALUE in the [control interface](#assignment-of-the-control-interface-s7-1500-1) is interpreted as the current setpoint relative to the reference value of the current.

The figure below shows the principle of operation of the PID current control.

![Current control](images/118805438731_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| P_Sel | Enable proportional action of the PID algorithm |
| I_Sel | Enable integral action of the PID algorithm |
| D_Sel | Enable derivative action of the PID algorithm |
| Reference value current (mA) | Maximum value as reference value for the current setpoint. The recommended setting is the value of the load current that is measured when current control is deactivated and the duty cycle is 100%. |
| Dead band width (μA) | Deviation of the output current from the current setpoint within which no correction takes place. The deviation refers to a range above and below the current setpoint. |
| Manipulated value high limit (S7 analog value) | High control limit |
| Manipulated value low limit (S7 analog value) | Low control limit |
| Gain | Gain factor for P-component of the PID algorithm |
| TI (s) | Integration time; length of time used by the I-component of the PID algorithm.  If TI is less than the controller cycle time, TI is set internally to the value of the cycle time. |
| TD (s) | Derivative action time; length of time used by the D-component of the PID algorithm.  If TD is less than the controller cycle time, TI is set internally to the value of the cycle time. |
| TM_LAG (s) | Time lag of the D-component of the PID algorithm.  If TI is less than half the controller cycle time, TI is set internally to half the value of the cycle time. |

The default setting of the controller parameters is chosen conservatively to enable stable operation. For dynamic valve positioning, you optimize the individual parameters to fit your plant conditions. In particular, a higher gain factor and a lower integration time lead to faster reactions to a setpoint change.

**Controller cycle time**

When dithering is deactivated, the internal cycle time of the controller corresponds to the PWM period duration. When dithering is active, the internal cycle time of the controller corresponds to the dithering period duration.

**Resetting the PID controller**

The internal data of the controller is reset in the following cases:

- SW_ENABLE control bit is reset
- New parameter data record is sent to module

**Further information**

You can find further information on PID controllers in the [PID Control](https://support.industry.siemens.com/cs/ww/en/view/108210036) function manual, e.g. in the CONT_C section.

#### Minimum pulse duration and minimum interpulse period (S7-1500)

The minimum pulse duration and the minimum interpulse period are the minimum pulse duration and interpulse period that are to be output.

The module suppresses pulses and interpulse periods whose duration is less the minimum pulse duration. A pulse duration that is less than the period duration by an amount less than the minimum interpulse period is set by the module to the value of the period duration. In this way you can suppress undesired effects when the connected actuator is not able to react appropriately to such short signal changes.

![Pulse duration modulation](images/116763905035_DV_resource.Stream@PNG-en-US.png)

Pulse duration modulation

You set the minimum pulse duration from 0 to 85 s with a precision of 1 µs in the hardware configuration. The set value applies simultaneously to the minimum interpulse period.

> **Note**
>
> **Current control**
>
> If you are using current control, a configured minimum pulse duration has no effect.

> **Note**
>
> **Dithering**
>
> If you are using dithering without current control, the configured minimum pulse duration is effective. In this case, the superimposition of the PWM signal is reduced so that the effective pulse duration is within the permissible range.

#### High-speed output (S7-1500)

The high-speed output function enables an output frequency of a maximum of 100 kHz with an output current of a maximum of 100 mA. A high-speed output generates very steep edges. The high-speed output generates signals at a higher frequency, but provides a lower maximum load current.

The high-speed output is only available in two-channel operation and only without current control.

The following table presents the minimum and maximum pulse duration, period duration and frequency depending on whether or not the high-speed output is activated:

|  | Minimum value |  | Maximum value |  |
| --- | --- | --- | --- | --- |
| High-speed output deactivated | High-speed output activated | High-speed output deactivated | High-speed output activated |  |
| Pulse duration | 10 μs | 1,5 μs | 85000000 μs (= 85 s) |  |
| Period duration | 100 μs | 10 μs |  |  |
| Frequency | 0,02 Hz |  | 10 kHz | 100 kHz |

### Configuring (S7-1500)

#### Introduction

You configure the technology module and assign its parameters with the configuration software.

The user program controls and monitors the functions of the technology module via the control interface and feedback interface.

#### System environment

The technology module can be used in the following system environments:

| Possible use | Components needed | Configuration software | In the user program |
| --- | --- | --- | --- |
| Centralized operation with a CPU 151xSP | - ET 200SP automation system - TM Pulse 2x24V | STEP 7 (TIA Portal):  Device configuration and parameter setting with hardware configuration | Direct access to control interface and feedback interface in the I/O data |
| Distributed operation with an S7-1500 CPU | - S7-1500 automation system - ET 200SP distributed I/O system - TM Pulse 2x24V | STEP 7 (TIA Portal):  Device configuration and parameter setting with hardware configuration |  |
| Distributed operation with an S7-300/400 CPU | - S7-300/400 automation system - ET 200SP distributed I/O system - TM Pulse 2x24V | STEP 7 (TIA Portal):  Device configuration and parameter setting with hardware configuration  STEP 7:  Device configuration and parameter setting with HSP |  |
| Distributed operation on the PROFINET IO in a third-party system | - Third-party automation system - ET 200SP distributed I/O system - TM Pulse 2x24V | Third-party configuration software:   Device configuration and parameter setting with GSD file |  |
| Distributed operation on the PROFIBUS DP in a third-party system | - Third-party automation system - ET 200SP distributed I/O system - TM Pulse 2x24V | Third-party configuration software:  GSD file; device configuration and parameter setting using data record 128 |  |

#### Hardware Support Packages (HSP)

**STEP 7**

The Hardware Support Packages (HSP) are available for download on the [Internet](https://support.industry.siemens.com/cs/ww/en/view/23183356).

#### GSD file

The respective GSD file for the ET 200SP distributed I/O system is available for download on the Internet:

- [GSD file PROFINET IO](http://support.automation.siemens.com/WW/view/en/57138621)
- [GSD file PROFIBUS DP](http://support.automation.siemens.com/WW/view/en/73016883)

### Reaction to CPU STOP (S7-1500)

You set the response of the channel to a CPU STOP in the parameters of the device configuration.

Response of channel to CPU STOP

| Option | Meaning |
| --- | --- |
| Output substitute value | The channel outputs the configured substitute values at the digital outputs until the next STOP-RUN transition of the CPU. You can configure the substitute value 1 for only one of the two digital outputs.  An active output sequence is stopped and the STS_ENABLE feedback bit is reset.  The technology module is set to its startup state after a STOP-RUN transition. Before you can start a new pulse output, you must reset the SW_ENABLE control bit. |
| Continue operation | The channel continues to operate.  The digital outputs continue to switch according to the parameter assignment. An active output sequence will thus be continued. If you have configured the hardware enable, you can also start additional output sequences using DIn.0.  The configuration of the technology module is not reset after a STOP-RUN transition. |

### Parameter setting (S7-1500)

You use various parameters to specify the properties of the technology module. Depending on the settings, not all parameters are available. When parameters are assigned in the user program, the parameters are transferred to the module with the "WRREC" instruction and data record 128.

You set the parameters of the module as follows in this operating mode:

| Parameter setting via... | Basic procedure |
| --- | --- |
| Hardware configuration in STEP 7 (TIA Portal) | 1. Insert the module from the hardware catalog under "Technology modules". 2. Set the "Pulse width modulation PWM" mode and the further parameters of the module in the hardware configuration. 3. Download the project to the CPU. |
| Hardware configuration in STEP 7 with HSP | 1. Install the corresponding HSP file. You will then find the module in the hardware catalog under "ET 200SP". 2. Set the "Pulse width modulation PWM" mode and the further parameters of the module in the hardware configuration. 3. Download the project to the CPU. |
| Hardware configuration with GSD file for distributed operation on PROFINET IO | 1. Install the latest PROFINET GSD file. You will then find the module in the hardware catalog under "Other field devices &gt; PROFINET IO &gt; I/O". 2. Set the "Pulse width modulation PWM" mode and the further parameters of the module in the hardware configuration. 3. Download the project to the CPU. |
| Hardware configuration with GSD file for distributed operation on PROFIBUS DP | 1. Install the latest PROFIBUS GSD file. You will then find the module in the hardware catalog under "Other field devices &gt; PROFIBUS DP &gt; I/O". 2. Download the project to the CPU. The parameters of the module are also downloaded with their default settings (see table below). 3. Set the parameters in the user program using data record 128. |

#### Parameters of the TM Pulse 2x24V in "Pulse width modulation PWM" mode

The following table shows the parameters for the module.

The default settings of the parameters are shown in bold in the "Value range" column.

Adjustable parameters

| Parameter | Value range | Scope |
| --- | --- | --- |
| Channel configuration<sup>1</sup> | - **2 channels (2 A)** - 1 channel (4 A) | Module |
| Reaction to CPU STOP | - **Output substitute value** - Continue operation | Channel |
| Substitute value for DQA | - **0** - 1 | Channel |
| Substitute value for DQB | - **0** - 1 | Channel |
| Group diagnostics | - **Deactivated** - Activated | Channel |
| Diagnostics DQA | - **Deactivated** - Activated | Channel |
| Diagnostics DQB | - **Deactivated** - Activated | Channel |
| High-speed output (0.1 A) | - **Deactivated** - Activated | Channel |
| Function DI | - **Input** - HW enable | Channel |
| Input delay for digital inputs | - None - 0.05 ms - **0.1 ms** - 0.4 ms - 0.8 ms - 1.6 ms - 3.2 ms - 12.8 ms - 20 ms | Channel |
| Output format | - S7 analog output - **1/100** - 1/1000 - 1/10000 | Channel |
| Minimum pulse duration | **0**...85000000 μs | Channel |
| Period duration | 10...**2000000**...85000000 μs | Channel |
| Actual period duration | Automatically calculated (read-only) | Channel |
| On delay for pulse output | **0**...85000000 μs | Channel |
| Dithering | - **Deactivated** - Activated | Channel |
| Incline of dithering ramp up | **0**...30000 ms | Channel |
| Incline of dithering ramp down | **0**...30000 ms | Channel |
| Dithering amplitude | 0.0...**5.0**...50% | Channel |
| Dithering period duration | 2000...**50000**...100000 μs | Channel |
| Dithering frequency | Automatically calculated (read-only) | Channel |
| Current control | - **Deactivated** - Activated | Channel |
| Enable proportional action | - Deactivated - **Activated** | Channel |
| Enable integral action | - Deactivated - **Activated** | Channel |
| Enable derivative action | - **Deactivated** - Activated | Channel |
| Reference value current | **0**...2000 mA (two-channel operation);   **0**...4000 mA (one-channel operation) | Channel |
| Dead band width | **0**...65535 μA | Channel |
| Manipulated value high limit | 1...**27648** | Channel |
| Manipulated value low limit | **0**...27647 | Channel |
| Proportional gain | 0.0000...**2.0000**...7.9228×10<sup>28</sup> | Channel |
| Integration time | 0.0000...**20.0000**...7.9228×10<sup>28</sup> s | Channel |
| Derivative action time | 0.0000...**10.0000**...7.9228×10<sup>28</sup> s | Channel |
| Delay time of derivative action | 0.0000...**2.0000**...7.9228×10<sup>28</sup> s | Channel |
| <sup>1</sup> When configuring with HSP for STEP 7 or with a GSD file, you define the channel configuration by the selection of the module name. |  |  |

> **Note**
>
> **PROFIBUS GSD configuration**
>
> When configuring with a PROFIBUS GSD file, the possible parameter assignments are not available. The parameters are preassigned in the module with the default setting. Set the parameters in the user program using data record 128.

### Address space (S7-1500)

#### Address space of the technology module

Size of input and output addresses

|  | Inputs | Outputs |
| --- | --- | --- |
| Size per technology channel | 8 bytes | 12 bytes |
| Size in one-channel operation | 8 bytes | 12 bytes |
| Size in two-channel operation | 16 bytes | 24 bytes |

### Control interface and feedback interface (S7-1500)

This section contains information on the following topics:

- [Library with PLC data types (S7-1500)](#library-with-plc-data-types-s7-1500-1)
- [Assignment of the control interface (S7-1500)](#assignment-of-the-control-interface-s7-1500-1)
- [Assignment of the feedback interface (S7-1500)](#assignment-of-the-feedback-interface-s7-1500-1)

#### Library with PLC data types (S7-1500)

> **Note**
>
> A library of PLC data types (LPD) for STEP 7 (TIA Portal) and SIMATIC S7-1200 / S7-1500 is available for download on the [Internet](https://support.industry.siemens.com/cs/ww/en/view/109482396).

#### Assignment of the control interface (S7-1500)

The user program uses the control interface to influence the behavior of the technology module.

##### Control interface per channel

The following table shows the control interface assignment:

| Byte offset relative to start address Channel 0/1 **↓ ↓** |  | Bit 7 | Bit 6 | Bit 5 | Bit 4 | Bit 3 | Bit 2 | Bit 1 | Bit 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 … 3 | 12 … 15 | OUTPUT_VALUE  UDINT: Duty cycle or current setpoint |  |  |  |  |  |  |  |
| 4 … 7 | 16 … 19 | SLOT  UDINT: Load value |  |  |  |  |  |  |  |
| 8 | 20 | Reserved |  |  | MODE_ SLOT | LD_SLOT |  |  |  |
| 9 | 21 | Reserved |  | DITHER | SET_DQB | SET_DQA | Reserved | TM_ CTRL_DQ | SW_ ENABLE |
| 10 | 22 | Reserved |  |  |  |  |  |  | RES_ ERROR |
| 11 | 23 | Reserved |  |  |  |  |  |  |  |

> **Note**
>
> Channel 1 is only available in two-channel operation of the module.

| Control bit/value | Explanations |
| --- | --- |
| OUTPUT_VALUE | If you are not using current control, you specify the duty cycle (mark-to-space ratio, duty factor) with this value. A changed duty cycle takes effect at the next rising edge at DQn.A.   If you are using current control, the module controls the duty cycle, and you specify the current setpoint relative to the reference value current with OUTPUT_VALUE.   Value range of the duty cycle or current setpoint:  - Output format "1/100": 0 to 100<sub>D</sub> - Output format "1/1000": 0 to 1000<sub>D</sub> - Output format "1/10000": 0 to 10000<sub>D</sub> - Output format "S7 analog output": 0 ... 27648<sub>D</sub>   If the setting is outside the value range, the ERR_OUT_VAL feedback bit is set and the maximum permissible value of the output format is used in each case. |
| SLOT | You specify the load value with this value.  Value range:  - Period duration in μs: 10 to 85000000<sub>D</sub> - On delay in μs: 0 to 85000000<sub>D</sub> - Dithering ramp up/ramp down in ms: 0 to 30000<sub>D</sub> - Dithering amplitude in %: 0 to 500<sub>D</sub> - Dithering period duration in μs: 2000 to 100000<sub>D</sub>   You specify whether to apply a change once or cyclically with MODE_SLOT.  Invalid values trigger setting of feedback bit ERR_LD (when MODE_SLOT = 0) or ERR_SLOT_VAL (when MODE_SLOT = 1). |
| MODE_SLOT | You specify whether you want to apply a change in SLOT once or cyclically with this bit.  0 means: As soon as you write the respective value in the corresponding output byte, the value from SLOT is applied once and kept until the next change. A change via SLOT takes effect at the next output sequence. After a restart of the module, the value is overwritten with the value set in the hardware configuration.   1 means: When you write the respective value in the corresponding output byte, the current value from SLOT in each case is applied cyclically. A change via SLOT takes effect at the next output sequence. |
| LD_SLOT | You specify the meaning of the value in SLOT with this load request:  - 0000<sub>B</sub> means: No action, idle - 0001<sub>B</sub> means: Period duration in μs - 0010<sub>B</sub> means: On delay in μs - 0101<sub>B</sub> means: Dithering ramp up (LOWWORD), ramp down (HIGHWORD) in ms - 0110<sub>B</sub> means: Dithering amplitude in % - 0111<sub>B</sub> means: Dithering period duration in μs   Values not listed are invalid and trigger setting of feedback bit ERR_LD (when MODE_SLOT = 0) or ERR_SLOT_VAL (when MODE_SLOT = 1). |
| DITHER | You activate the superimposition of the dither signal on the PWM signal with this bit.  - 0 → 1 means: Dithering starts with the configured ramp up - 1 → 0 means: Dithering ends with the configured ramp down |
| SET_DQA | You use this bit to set digital output DQn.A when TM_CTRL_DQ and SET_DQB are set to 0. |
| SET_DQB | You use this bit to set digital output DQn.B when TM_CTRL_DQ and SET_DQA are set to 0. |
| TM_CTRL_DQ | You enable the technological function of the digital output with this bit.   - 0 means: SET_DQA and SET_DQB define states of DQn.A and DQn.B - 1 means: Output sequence defines the state of DQn.A; DQn.B is always 0. |
| SW_ENABLE | You activate the software enable with this bit. If you are using the hardware enable, it is combined with the software enable.  - 0 means: Stop output - 1 means: Start output   Use of the HW enable is activated through parameter assignment. The HW enable is controlled externally using the digital input DIn.0. |
| RES_ERROR | You use this bit to reset the following feedback bits when errors are pending:  - ERR_24V - ERR_DQA - ERR_DQB - ERR_LD |
| Reserved | Reserved bits must be set to 0. |

#### Assignment of the feedback interface (S7-1500)

The user program receives current values and status information from the technology module via the feedback interface.

##### Feedback interface per channel

The following table shows the assignment of the feedback interface:

| Byte offset relative to start address Channel 0/1 **↓ ↓** |  | Bit 7 | Bit 6 | Bit 5 | Bit 4 | Bit 3 | Bit 2 | Bit 1 | Bit 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 8 | ERR_ SLOT_VAL | ERR_ OUT_VAL | ERR_DQB | ERR_DQA | Reserved | ERR_LD | ERR_24V | ERR_PWR |
| 1 | 9 | Reserved |  | STS_SW_ ENABLE | STS_ READY | Reserved | STS_LD_ SLOT | Reserved |  |
| 2 | 10 | Reserved |  |  | STS_ DITHER | STS_DI | STS_DQB | STS_DQA | STS_ ENABLE |
| 3 | 11 | Reserved |  |  |  |  |  |  |  |
| 4 ... 5 | 12 ... 13 | MEASURED_CURRENT |  |  |  |  |  |  |  |
| 6 | 14 | Reserved |  |  |  |  |  | QLMN_HLM | QLMN_LLM |
| 7 | 15 | Reserved |  |  |  |  |  |  |  |

> **Note**
>
> Channel 1 is only available in two-channel operation of the module.

| Feedback bit/value | Explanations |
| --- | --- |
| ERR_SLOT_VAL | This bit indicates that the value in SLOT or LD_SLOT is invalid (when MODE_SLOT = 1) and was not accepted.   As soon as the module has received a valid value from the control interface, ERR_SLOT_VAL is automatically reset. |
| ERR_OUT_VAL | This bit indicates that the value in OUTPUT_VALUE is invalid.  As soon as the module has received a valid value from the control interface, ERR_OUT_VAL is automatically reset. |
| ERR_DQA | This bit indicates a short-circuit or an overload at the output DQn.A. If you have enabled the diagnostics interrupt "Diagnostics DQA", the diagnostics interrupt "Error at digital outputs" is triggered when this error occurs.   The bit is reset once you have acknowledged the error with RES_ERROR. |
| ERR_DQB | This bit indicates a short-circuit or an overload at the output DQn.B or the attempted simultaneous setting of the SET_DQA and SET_DQB control bits. If you have enabled the diagnostics interrupt "Diagnostics DQB", the diagnostics interrupt "Error at digital outputs" is triggered when this error occurs.   The bit is reset once you have acknowledged the error with RES_ERROR. |
| ERR_LD | This bit indicates that the value in SLOT or LD_SLOT (when MODE_SLOT = 0) is invalid and was not accepted.   The bit is reset once you have acknowledged the error with RES_ERROR. |
| ERR_24V | This bit indicates a short-circuit or an overload at output 24VDC If you have enabled diagnostic interrupts, the diagnostic interrupt "Short circuit / overload of the sensor supply voltage" is triggered when this error occurs.   The bit is reset once you have acknowledged the error with RES_ERROR. |
| ERR_PWR | This bit indicates that supply voltage L+ is too low. If you have enabled the diagnostic interrupts, the diagnostic interrupt "Supply voltage fault" is triggered when an error occurs.   As soon as supply voltage L+ is sufficiently high again, ERR_PWR is automatically reset.  The bit is not set if no supply voltage is present. |
| STS_SW_ENABLE | This bit indicates the status of the SW enable.  - 0 means: SW enable not active - 1 means: SW enable active |
| STS_READY | This bit indicates that the module is supplying valid user data. The module is started and configured. |
| STS_LD_SLOT | A status change (toggling) of this bit indicates that the LD_SLOT load request was detected and executed (when MODE_SLOT = 0). |
| STS_DITHER | This bit indicates that the dither signal is active with ramp up started and ramp down not yet complete. |
| STS_DI | This bit indicates the status of the digital input DIn.0. |
| STS_DQA | This bit indicates the status of the digital output DQn.A. |
| STS_DQB | This bit indicates the status of the digital output DQn.B. |
| STS_ENABLE | This bit indicates that an output sequence is active. |
| MEASURED_ CURRENT | This value indicates the measured value of the current as an S7 analog value:  - Two-channel operation: 27648<sub>D</sub> ≙ 2 A - One-channel operation: 27648<sub>D</sub> ≙ 4 A - 32767<sub>D</sub> means: Valid measured value of current not available, e.g. during the first PWM period duration |
| QLMN_HLM | This bit indicates that the manipulated value high limit of the current control has been reached. |
| QLMN_LLM | This bit indicates that the manipulated value low limit of the current control has been reached. |
| Reserved | Reserved bits are set to 0. |

### Isochronous mode (S7-1500)

The technology module supports the "Isochronous mode" system function. In isochronous mode, the output sequence starts at time T<sub>o</sub> after the SW_ENABLE control bit has been set. The period duration is also adapted to the application cycle (T<sub>APP</sub>) and synchronized with it. The synchronization is especially advantageous for setting up control loops.

The module adjusts the assigned value of the period duration in such a way that an integer ratio results. In the most unfavorable case, the difference amounts to half the application cycle.

Examples:

| Application cycle T<sub>APP</sub> | Assigned period duration T<sub>Setpoint</sub> | Actual period durationT<sub>Actual</sub> | T<sub>APP</sub>:T<sub>Actual</sub> |
| --- | --- | --- | --- |
| 10 ms  (10000 μs) | 1800 μs | 1666 μs | 6:1 |
| 2000 μs | 2000 μs | 5:1 |  |
| 3000 μs | 3333 μs | 3:1 |  |
| 5000 μs | 5000 μs | 2:1 |  |
| 6000 μs | 5000 μs | 2:1 |  |
| 12000 μs | 10000 μs | 1:1 |  |
| 16000 μs | 20000 μs | 1:2 |  |

The figure below shows an example of a 1:1 ratio of application cycle to period duration with a duty cycle of 50%.

![Figure](images/116953289227_DV_resource.Stream@PNG-en-US.png)

The figure below shows an example of a 3:1 ratio of application cycle to period duration with a duty cycle of 50%.

![Figure](images/116953292811_DV_resource.Stream@PNG-en-US.png)

The figure below shows an example of a 1:3 ratio of application cycle to period duration with a duty cycle of 50%.

![Figure](images/116976349195_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> **No HW enable or On delay**
>
> No hardware enable or On delay can be used in isochronous mode.

#### Further information

You will find a detailed description of isochronous mode in:

- In the isochronous mode function manual as a download from the [Internet](https://support.industry.siemens.com/cs/ww/en/view/109755401).
- PROFINET with STEP 7 function manual available for download on the [Internet](https://support.industry.siemens.com/cs/ww/en/view/49948856).

---

**See also**

Function: Isochronous mode

## Pulse train mode (S7-1500)

This section contains information on the following topics:

- [Function (S7-1500)](#function-s7-1500-2)
- [Configuring (S7-1500)](#configuring-s7-1500-2)
- [Reaction to CPU STOP (S7-1500)](#reaction-to-cpu-stop-s7-1500-2)
- [Parameter setting (S7-1500)](#parameter-setting-s7-1500-2)
- [Address space (S7-1500)](#address-space-s7-1500-2)
- [Control interface and feedback interface (S7-1500)](#control-interface-and-feedback-interface-s7-1500-1)
- [Isochronous mode (S7-1500)](#isochronous-mode-s7-1500-2)

### Function (S7-1500)

This section contains information on the following topics:

- [Introduction (S7-1500)](#introduction-s7-1500-2)
- [Output sequence (S7-1500)](#output-sequence-s7-1500-2)
- [Number of pulses (S7-1500)](#number-of-pulses-s7-1500)
- [Duty cycle (S7-1500)](#duty-cycle-s7-1500-1)
- [Period duration (S7-1500)](#period-duration-s7-1500-1)
- [On delay (S7-1500)](#on-delay-s7-1500-2)
- [Current measurement (S7-1500)](#current-measurement-s7-1500)
- [High-speed output (S7-1500)](#high-speed-output-s7-1500-2)

#### Introduction  (S7-1500)

In this operating mode, the respective channel of the technology module outputs a number of pulses with the configured period duration, duty cycle and On delay. You specify the number of pulses via the control interface.

#### Output sequence (S7-1500)

##### Starting the output sequence

In order to output the output sequence at the digital output DQn.A, the TM_CTRL_DQ control bit must be set. To start the output sequence using the software enable, you set the SW_ENABLE [control bit](#assignment-of-the-control-interface-s7-1500-2). The STS_SW_ENABLE feedback bit indicates that the software enable in the technology module is active.

You can additionally use the hardware enable via the respective digital input DIn.0. You can configure an input delay for DIn.0.

**Pulse diagram**

The following figure shows an example of an output sequence when DIn.0 is being used as a hardware enable.

![Example of an output sequence](images/117401508491_DV_resource.Stream@PNG-en-US.png)

Example of an output sequence

If you are using the hardware enable, it is combined with the software enable. When the software enable is active, the output sequence starts at the first positive edge of the hardware enable. Additional positive edges of the hardware enable during the output sequence are ignored. If the hardware enable is set and remains set for the duration of the input delay, the On delay is started and the STS_ENABLE feedback bit is set. As soon as the On delay has elapsed, the pulse train with the assigned number of pulses is output at the respective digital output DQn.A. The output sequence is stopped at the end of the last pulse, and STS_ENABLE is reset.

If you are not using a hardware enable, the On delay starts at the positive edge of SW_ENABLE.

##### Aborting the output sequence

If you reset the SW_ENABLE control bit, the software enable is deactivated and the current output sequence is aborted. The last period is not completed. The STS_ENABLE feedback bit and the digital output DQn.A are reset.

A renewed pulse output is only possible after a restart of the output sequence.

#### Number of pulses (S7-1500)

You set the number of pulses in the [control interface](#assignment-of-the-control-interface-s7-1500-2) using OUTPUT_VALUE as integer (UDINT). The value range is 1 to 4294967295 (2<sup>32</sup>-1). A change takes effect immediately.

If you reduce the number of pulses to 0 or to an already output number of pulses, the output sequence is aborted. In this case, the STS_ENABLE feedback bit and the digital output DQn.A are reset, and the ERR_PULSE feedback bit is set. To continue the pulse output, you must restart the output sequence. At the next start of the output sequence, the technology module resets the ERR_PULSE feedback bit again.

#### Duty cycle (S7-1500)

The duty cycle corresponds to the ratio of pulse duration to period duration (also referred to as duty factor or mark-to-space ratio).

You set the period duration in the hardware configuration. The value range is dependent on the configured output format. If you set the value 0, the DQn.A is not set during the entire period duration. If you set the maximum value, the DQn.A is set during the entire period duration. If you set a value above the value range, the maximum value is used.

| Output format | Value range of OUTPUT_VALUE | Pulse duration |
| --- | --- | --- |
| 1/100 (%) | 0 ... 100 | (OUTPUT_VALUE/100) × Period duration |
| 1/1000 (‰) | 0 ... 1000 | (OUTPUT_VALUE/1000) × Period duration |
| 1/10000 | 0 ... 10000 | (OUTPUT_VALUE/10000) × Period duration |
| S7 analog output | 0 ... 27648 | (OUTPUT_VALUE/27648) × Period duration |

In addition, you can change the duty cycle via the [control interface](#assignment-of-the-control-interface-s7-1500-2) by entering a new value in SLOT as integer (UDINT). In so doing, you use the MODE_SLOT control bit to choose whether you want to apply a change once or cyclically:

| Symbol | Meaning |
| --- | --- |
| MODE_SLOT = 0 | One-time change: As soon as you write the value 4<sub>D</sub> in the corresponding output byte, the value from SLOT is applied once as the duty cycle and kept until the next change.  A change via SLOT takes effect at the next output sequence. An active output sequence is not affected by the change. |
| MODE_SLOT = 1 | Cyclic change: When you write the value 20<sub>D</sub> in the corresponding output byte, the current value from SLOT in each case is applied cyclically as the duty cycle.  A change via SLOT takes effect at the next output sequence. An active output sequence is not affected by the change. |

For more detailed information, refer to the section  Handling the SLOT parameters.

#### Period duration (S7-1500)

You set the period duration in µs in the hardware configuration. The value range is dependent on whether or not the [high-speed output function](#high-speed-output-s7-1500-2) is being used:

| High-speed output | Value range of the period duration |
| --- | --- |
| Activated | 10 ... 85000000 μs  = 10 μs ... 85 s |
| Deactivated | 100 ... 85000000 μs  = 100 μs ... 85 s |

In addition, you can change the period duration via the control interface by entering a new value in SLOT as an integer (UDINT). In so doing, you use the MODE_SLOT control bit to choose whether you want to apply a change once or cyclically:

| Symbol | Meaning |
| --- | --- |
| MODE_SLOT = 0 | One-time change: As soon as you write the value 1<sub>D</sub> in the corresponding output byte, the value from SLOT is applied once as the period duration and kept until the next change.  A change via SLOT takes effect at the next output sequence. An active output sequence is not affected by the change. |
| MODE_SLOT = 1 | Cyclic change: When you write the value 17<sub>D</sub> in the corresponding output byte, the current value from SLOT in each case is applied cyclically as the period duration.  A change via SLOT takes effect at the next output sequence. An active output sequence is not affected by the change. |

For more detailed information, refer to the section  Handling the SLOT parameters.

#### On delay (S7-1500)

You set the On delay from 0 to 85 s with a precision of 1 µs in the hardware configuration.

In addition, you can change the On delay via the control interface by entering a new value in SLOT as an integer (UDINT). In so doing, you use the MODE_SLOT control bit to choose whether you want to apply a change once or cyclically:

| Symbol | Meaning |
| --- | --- |
| MODE_SLOT = 0 | One-time change: As soon as you write the value 2<sub>D</sub> in the corresponding output byte, the value from SLOT is applied once as the On delay and kept until the next change.  A change via SLOT takes effect at the next output sequence. An active output sequence is not affected by the change. |
| MODE_SLOT = 1 | Cyclic change: When you write the value 18<sub>D</sub> in the corresponding output byte, the current value from SLOT in each case is applied cyclically as the On delay.  A change via SLOT takes effect at the next output sequence. An active output sequence is not affected by the change. |

For more detailed information, refer to the section  Handling the SLOT parameters.

#### Current measurement (S7-1500)

The technology module measures the load current at the digital output. The measured value of the current is returned as an S7 analog value in the MEASURED_CURRENT value in the [feedback interface](#assignment-of-the-feedback-interface-s7-1500-2).

A valid measured value is available when the STS_ENABLE feedback bit is set after the first period duration of the output sequence. The returned measured value is an average of the measured values that were acquired over a time period of at least one period duration. If a valid measured value is not available, the value 32767<sub>D</sub> is returned.

> **Note**
>
> In order to use the current measurement, the high-speed output must be deactivated.

##### Measuring range and accuracy

The measuring range and accuracy are dependent on the channel configuration:

|  | Measured value 27648<sub>D</sub> | Maximum measured value 32511<sub>D</sub> ≙ ... | Accuracy<sup>3</sup> |  |
| --- | --- | --- | --- | --- |
| Period duration &gt; 333 μs | Period duration &lt; 333 μs |  |  |  |
| Two-channel operation | 2 A<sup>1</sup> | 2.37 A<sup>2</sup> | ±40 mA | -40 mA ... +100 mA |
| One-channel operation  (parallel connection) | 4 A<sup>1</sup> | 4.74 A<sup>2</sup> | ±80 mA | -80 mA ... +200 mA |
| <sup>1 </sup>May only be exceeded for a short time.   <sup>2 </sup>When this current value is exceeded, the ERR_DQA feedback bit will be set.   <sup>3 </sup>With constant period duration in the respective measuring period. |  |  |  |  |

#### High-speed output (S7-1500)

The high-speed output function enables an output frequency of a maximum of 100 kHz with an output current of a maximum of 100 mA. A high-speed output generates very steep edges. The high-speed output generates signals at a higher frequency, but provides a lower maximum load current. The high-speed output is only available in two-channel operation.

The following table presents the minimum and maximum pulse duration, period duration and frequency depending on whether or not the high-speed output is activated:

|  | Minimum value |  | Maximum value |  |
| --- | --- | --- | --- | --- |
| High-speed output deactivated | High-speed output activated | High-speed output deactivated | High-speed output activated |  |
| Pulse duration | 10 μs | 1,5 μs | 85000000 μs (= 85 s) |  |
| Period duration | 100 μs | 10 μs |  |  |
| Frequency | 0,02 Hz |  | 10 kHz | 100 kHz |

### Configuring (S7-1500)

#### Introduction

You configure the technology module and assign its parameters with the configuration software.

The user program controls and monitors the functions of the technology module via the control interface and feedback interface.

#### System environment

The technology module can be used in the following system environments:

| Possible use | Components needed | Configuration software | In the user program |
| --- | --- | --- | --- |
| Centralized operation with a CPU 151xSP | - ET 200SP automation system - TM Pulse 2x24V | STEP 7 (TIA Portal):  Device configuration and parameter setting with hardware configuration | Direct access to control interface and feedback interface in the I/O data |
| Distributed operation with an S7-1500 CPU | - S7-1500 automation system - ET 200SP distributed I/O system - TM Pulse 2x24V | STEP 7 (TIA Portal):  Device configuration and parameter setting with hardware configuration |  |
| Distributed operation with an S7-300/400 CPU | - S7-300/400 automation system - ET 200SP distributed I/O system - TM Pulse 2x24V | STEP 7 (TIA Portal):  Device configuration and parameter setting with hardware configuration  STEP 7:  Device configuration and parameter setting with HSP |  |
| Distributed operation on the PROFINET IO in a third-party system | - Third-party automation system - ET 200SP distributed I/O system - TM Pulse 2x24V | Third-party configuration software:   Device configuration and parameter setting with GSD file |  |
| Distributed operation on the PROFIBUS DP in a third-party system | - Third-party automation system - ET 200SP distributed I/O system - TM Pulse 2x24V | Third-party configuration software:  GSD file; device configuration and parameter setting using data record 128 |  |

#### Hardware Support Packages (HSP)

**STEP 7**

The Hardware Support Packages (HSP) are available for download on the [Internet](https://support.industry.siemens.com/cs/ww/en/view/23183356).

#### GSD file

The respective GSD file for the ET 200SP distributed I/O system is available for download on the Internet:

- [GSD file PROFINET IO](http://support.automation.siemens.com/WW/view/en/57138621)
- [GSD file PROFIBUS DP](http://support.automation.siemens.com/WW/view/en/73016883)

### Reaction to CPU STOP (S7-1500)

You set the response of the channel to a CPU STOP in the parameters of the device configuration.

Response of channel to CPU STOP

| Option | Meaning |
| --- | --- |
| Output substitute value | The channel outputs the configured substitute values at the digital outputs until the next STOP-RUN transition of the CPU. You can configure the substitute value 1 for only one of the two digital outputs.  An active output sequence is stopped and the STS_ENABLE feedback bit is reset.  The technology module is set to its startup state after a STOP-RUN transition. Before you can start a new pulse output, you must reset the SW_ENABLE control bit. |
| Continue operation | The channel continues to operate.  The digital outputs continue to switch according to the parameter assignment. An active output sequence will thus be continued. If you have configured the hardware enable, you can also start additional output sequences using DIn.0.  The configuration of the technology module is not reset after a STOP-RUN transition. |

### Parameter setting (S7-1500)

You use various parameters to specify the properties of the technology module. Depending on the settings, not all parameters are available. When parameters are assigned in the user program, the parameters are transferred to the module with the "WRREC" instruction and data record 128.

You set the parameters of the module as follows in this operating mode:

| Parameter setting via... | Basic procedure |
| --- | --- |
| Hardware configuration in STEP 7 (TIA Portal) | 1. Insert the module from the hardware catalog under "Technology modules". 2. Set the "Pulse train" mode and the further parameters of the module in the hardware configuration. 3. Download the project to the CPU. |
| Hardware configuration in STEP 7 with HSP | 1. Install the corresponding HSP file. You will then find the module in the hardware catalog under "ET 200SP". 2. Set the "Pulse train" mode and the further parameters of the module in the hardware configuration. 3. Download the project to the CPU. |
| Hardware configuration with GSD file for distributed operation on PROFINET IO | 1. Install the latest PROFINET GSD file. You will then find the module in the hardware catalog under "Other field devices &gt; PROFINET IO &gt; I/O". 2. Set the "Pulse train" mode and the further parameters of the module in the hardware configuration. 3. Download the project to the CPU. |
| Hardware configuration with GSD file for distributed operation on PROFIBUS DP | 1. Install the latest PROFIBUS GSD file. You will then find the module in the hardware catalog under "Other field devices &gt; PROFIBUS DP &gt; I/O". 2. Download the project to the CPU. The parameters of the module are also downloaded with their default settings (see table below). 3. Set the "Pulse train" mode and the further parameters in the user program using data record 128. |

#### Parameters of the TM Pulse 2x24V in "Pulse train" mode

The default settings of the parameters are shown in bold in the "Value range" column.

Adjustable parameters

| Parameter | Value range | Scope |
| --- | --- | --- |
| Channel configuration<sup>1</sup> | - **2 channels (2 A)** - 1 channel (4 A) | Module |
| Reaction to CPU STOP | - **Output substitute value** - Continue operation | Channel |
| Substitute value for DQA | - **0** - 1 | Channel |
| Substitute value for DQB | - **0** - 1 | Channel |
| Group diagnostics | - **Deactivated** - Activated | Channel |
| Diagnostics DQA | - **Deactivated** - Activated | Channel |
| Diagnostics DQB | - **Deactivated** - Activated | Channel |
| High-speed output (0.1 A) | - **Deactivated** - Activated | Channel |
| Function DI | - **Input** - HW enable | Channel |
| Input delay for digital inputs | - None - 0.05 ms - **0.1 ms** - 0.4 ms - 0.8 ms - 1.6 ms - 3.2 ms - 12.8 ms - 20 ms | Channel |
| Output format | - S7 analog output - **1/100** - 1/1000 - 1/10000 | Channel |
| Period duration | 10...**2000000**...85000000 μs | Channel |
| Actual period duration | Automatically calculated (read-only) | Channel |
| On delay for pulse output | **0**...85000000 μs | Channel |
| Duty cycle | Dependent on the output format | Channel |
| <sup>1</sup> When configuring with HSP for STEP 7 or with a GSD file, you define the channel configuration by the selection of the module name. |  |  |

> **Note**
>
> **PROFIBUS GSD configuration**
>
> When configuring with a PROFIBUS GSD file, the possible parameter assignments are not available. The parameters are preassigned in the module with the default setting. Set the "Pulse train" mode and the further parameters in the user program using data record 128.

### Address space (S7-1500)

#### Address space of the technology module

Size of input and output addresses

|  | Inputs | Outputs |
| --- | --- | --- |
| Size per technology channel | 8 bytes | 12 bytes |
| Size in one-channel operation | 8 bytes | 12 bytes |
| Size in two-channel operation | 16 bytes | 24 bytes |

### Control interface and feedback interface (S7-1500)

This section contains information on the following topics:

- [Library with PLC data types (S7-1500)](#library-with-plc-data-types-s7-1500-2)
- [Assignment of the control interface (S7-1500)](#assignment-of-the-control-interface-s7-1500-2)
- [Assignment of the feedback interface (S7-1500)](#assignment-of-the-feedback-interface-s7-1500-2)

#### Library with PLC data types (S7-1500)

> **Note**
>
> A library of PLC data types (LPD) for STEP 7 (TIA Portal) and SIMATIC S7-1200 / S7-1500 is available for download on the [Internet](https://support.industry.siemens.com/cs/ww/en/view/109482396).

#### Assignment of the control interface (S7-1500)

The user program uses the control interface to influence the behavior of the technology module.

##### Control interface per channel

The following table shows the control interface assignment:

| Byte offset relative to start address Channel 0/1 **↓ ↓** |  | Bit 7 | Bit 6 | Bit 5 | Bit 4 | Bit 3 | Bit 2 | Bit 1 | Bit 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 … 3 | 12 … 15 | OUTPUT_VALUE  UDINT: Number of pulses |  |  |  |  |  |  |  |
| 4 … 7 | 16 … 19 | SLOT  UDINT: Load value |  |  |  |  |  |  |  |
| 8 | 20 | Reserved |  |  | MODE_ SLOT | LD_SLOT |  |  |  |
| 9 | 21 | Reserved |  |  | SET_DQB | SET_DQA | Reserved | TM_ CTRL_DQ | SW_ ENABLE |
| 10 | 22 | Reserved |  |  |  |  |  |  | RES_ ERROR |
| 11 | 23 | Reserved |  |  |  |  |  |  |  |

> **Note**
>
> Channel 1 is only available in two-channel operation of the module.

| Control bit/value | Explanations |
| --- | --- |
| OUTPUT_VALUE | You specify the number of pulses with this value.  Value range: 1 to 4294967295<sub>D</sub> (2<sup>32</sup>-1)  If the setting is outside the value range, the ERR_OUT_VAL feedback bit is set and the last valid number of pulses is used. |
| SLOT | You specify the load value with this value.  Value range:   - Period duration in μs: 10 to 85000000<sub>D</sub> - On delay in μs: 0 to 85000000<sub>D</sub> - Duty cycle:   - Output format "1/100": 0 to 100<sub>D</sub>   - Output format "1/1000": 0 to 1000<sub>D</sub>   - Output format "1/10000": 0 to 10000<sub>D</sub>   - Output format "S7 analog output": 0 ... 27648<sub>D</sub>   You specify whether to apply a change once or cyclically with MODE_SLOT.  Invalid values trigger setting of feedback bit ERR_LD (when MODE_SLOT = 0) or ERR_SLOT_VAL (when MODE_SLOT = 1). |
| MODE_SLOT | You specify whether you want to apply a change in SLOT once or cyclically with this bit.  0 means: As soon as you write the respective value in the corresponding output byte, the value from SLOT is applied once and kept until the next change. A change via SLOT takes effect at the next output sequence. After a restart of the module, the value is overwritten with the value set in the hardware configuration.   1 means: When you write the respective value in the corresponding output byte, the current value from SLOT in each case is applied cyclically. A change via SLOT takes effect at the next output sequence. |
| LD_SLOT | You specify the meaning of the value in SLOT with this load request:  - 0000<sub>B</sub> means: No action, idle - 0001<sub>B</sub> means: Period duration in μs - 0010<sub>B</sub> means: On delay in μs - 0100<sub>B</sub> means: Duty cycle   Values not listed are invalid and trigger setting of feedback bit ERR_LD (when MODE_SLOT = 0) or ERR_SLOT_VAL (when MODE_SLOT = 1). |
| SET_DQA | You use this bit to set digital output DQn.A when TM_CTRL_DQ and SET_DQB are set to 0. |
| SET_DQB | You use this bit to set digital output DQn.B when TM_CTRL_DQ and SET_DQA are set to 0. |
| TM_CTRL_DQ | You enable the technological function of the digital output with this bit.   - 0 means: SET_DQA and SET_DQB define states of DQn.A and DQn.B - 1 means: Output sequence defines the state of DQn.A; DQn.B is always 0. |
| SW_ENABLE | You activate the software enable with this bit. If you are using the hardware enable, it is combined with the software enable.  - 0 means: Stop output - 1 means: Start output   Use of the HW enable is activated through parameter assignment. The HW enable is controlled externally using the digital input DIn.0. |
| RES_ERROR | You use this bit to reset the following feedback bits when errors are pending:  - ERR_24V - ERR_DQA - ERR_DQB - ERR_LD |
| Reserved | Reserved bits must be set to 0. |

#### Assignment of the feedback interface (S7-1500)

The user program receives current values and status information from the technology module via the feedback interface.

##### Feedback interface per channel

The following table shows the assignment of the feedback interface:

| Byte offset relative to start address Channel 0/1 **↓ ↓** |  | Bit 7 | Bit 6 | Bit 5 | Bit 4 | Bit 3 | Bit 2 | Bit 1 | Bit 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 8 | ERR_ SLOT_VAL | ERR_ OUT_VAL | ERR_DQB | ERR_DQA | ERR_ PULSE | ERR_LD | ERR_24V | ERR_PWR |
| 1 | 9 | Reserved |  | STS_SW_ ENABLE | STS_ READY | Reserved | STS_LD_ SLOT | Reserved |  |
| 2 | 10 | Reserved |  |  |  | STS_DI | STS_DQB | STS_DQA | STS_ ENABLE |
| 3 | 11 | Reserved |  |  |  | SEQ_CNT |  |  |  |
| 4 ... 5 | 12 ... 13 | MEASURED_CURRENT |  |  |  |  |  |  |  |
| 6 ... 7 | 14 ... 15 | Reserved |  |  |  |  |  |  |  |

> **Note**
>
> Channel 1 is only available in two-channel operation of the module.

| Feedback bit/value | Explanations |
| --- | --- |
| ERR_SLOT_VAL | This bit indicates that the value in SLOT or LD_SLOT is invalid (when MODE_SLOT = 1) and was not accepted.   As soon as the module has received a valid value from the control interface, ERR_SLOT_VAL is automatically reset. |
| ERR_OUT_VAL | This bit indicates that the value in OUTPUT_VALUE is invalid.  As soon as the module has received a valid value from the control interface, ERR_OUT_VAL is automatically reset. |
| ERR_DQA | This bit indicates a short-circuit or an overload at the output DQn.A. If you have enabled the diagnostics interrupt "Diagnostics DQA", the diagnostics interrupt "Error at digital outputs" is triggered when this error occurs.   The bit is reset once you have acknowledged the error with RES_ERROR. |
| ERR_DQB | This bit indicates a short-circuit or an overload at the output DQn.B or the attempted simultaneous setting of the SET_DQA and SET_DQB control bits. If you have enabled the diagnostics interrupt "Diagnostics DQB", the diagnostics interrupt "Error at digital outputs" is triggered when this error occurs.   The bit is reset once you have acknowledged the error with RES_ERROR. |
| ERR_PULSE | This bit indicates an error in the pulse output. |
| ERR_LD | This bit indicates that the value in SLOT or LD_SLOT (when MODE_SLOT = 0) is invalid and was not accepted.   The bit is reset once you have acknowledged the error with RES_ERROR. |
| ERR_24V | This bit indicates a short-circuit or an overload at output 24VDC If you have enabled diagnostic interrupts, the diagnostic interrupt "Short circuit / overload of the sensor supply voltage" is triggered when this error occurs.   The bit is reset once you have acknowledged the error with RES_ERROR. |
| ERR_PWR | This bit indicates that supply voltage L+ is too low. If you have enabled the diagnostic interrupts, the diagnostic interrupt "Supply voltage fault" is triggered when an error occurs.   As soon as supply voltage L+ is sufficiently high again, ERR_PWR is automatically reset.  The bit is not set if no supply voltage is present. |
| STS_SW_ENABLE | This bit indicates the status of the SW enable.   - 0 means: SW enable not active - 1 means: SW enable active |
| STS_READY | This bit indicates that the module is supplying valid user data. The module is started and configured. |
| STS_LD_SLOT | A status change (toggling) of this bit indicates that the LD_SLOT load request was detected and executed (when MODE_SLOT = 0). |
| STS_DI | This bit indicates the status of the digital input DIn.0. |
| STS_DQA | This bit indicates the status of the digital output DQn.A. |
| STS_DQB | This bit indicates the status of the digital output DQn.B. |
| STS_ENABLE | This bit indicates that an output sequence is active. |
| SEQ_CNT | This value indicates the number of completed output sequences as sequence counter. |
| MEASURED_ CURRENT | This value indicates the measured value of the current as an S7 analog value:  - Two-channel operation: 27648<sub>D</sub> ≙ 2 A - One-channel operation: 27648<sub>D</sub> ≙ 4 A - 32767<sub>D</sub> means: Valid measured value of current not available, e.g. during the first period duration |
| Reserved | Reserved bits are set to 0. |

### Isochronous mode (S7-1500)

The technology module supports the "Isochronous mode" system function. If you are not using a hardware enable, the output sequence starts in isochronous mode at time T<sub>o</sub> after the SW_ENABLE control bit has been set.

#### Further information

You will find a detailed description of isochronous mode in:

- In the isochronous mode function manual as a download from the [Internet](https://support.industry.siemens.com/cs/ww/en/view/109755401).
- PROFINET with STEP 7 function manual available for download on the [Internet](https://support.industry.siemens.com/cs/ww/en/view/49948856).

## On/Off delay mode (S7-1500)

This section contains information on the following topics:

- [Function (S7-1500)](#function-s7-1500-3)
- [Configuring (S7-1500)](#configuring-s7-1500-3)
- [Reaction to CPU STOP (S7-1500)](#reaction-to-cpu-stop-s7-1500-3)
- [Parameter setting (S7-1500)](#parameter-setting-s7-1500-3)
- [Address space (S7-1500)](#address-space-s7-1500-3)
- [Control interface and feedback interface (S7-1500)](#control-interface-and-feedback-interface-s7-1500-2)
- [Isochronous mode (S7-1500)](#isochronous-mode-s7-1500-3)

### Function (S7-1500)

This section contains information on the following topics:

- [Introduction (S7-1500)](#introduction-s7-1500-3)
- [Output sequence (S7-1500)](#output-sequence-s7-1500-3)
- [On delay (S7-1500)](#on-delay-s7-1500-3)
- [Off delay (S7-1500)](#off-delay-s7-1500)
- [High-speed output (S7-1500)](#high-speed-output-s7-1500-3)

#### Introduction  (S7-1500)

In this operating mode, the respective channel of the technology module outputs pulses with a specified switching delay relative to digital input DIn.0. You specify the On delay via the control interface.

#### Output sequence (S7-1500)

##### Starting the output sequence

In order to output the output sequence at the digital output DQn.A, the TM_CTRL_DQ control bit must be set. To start the output sequence using the software enable, you set the SW_ENABLE [control bit](#assignment-of-the-control-interface-s7-1500-3). The STS_SW_ENABLE feedback bit indicates that the software enable in the technology module is active.

**Pulse diagram**

The following figure shows an example of an output sequence for the case that you set SW_ENABLE while digital input DIn.0 is not set.

![Example 1 of an output sequence](images/117414473739_DV_resource.Stream@PNG-en-US.png)

Example 1 of an output sequence

The output sequence starts on a positive edge of SW_ENABLE, and the STS_SW_ENABLE and STS_ENABLE feedback bits are set. If digital input DIn.0 is set and remains set for the duration of the input delay, the On delay is started. As soon as the On delay has elapsed, the respective digital output DQn.A is set. If digital input DIn.0 is reset and remains set for the duration of the input delay, the Off delay is started. As soon as the Off delay has elapsed, the respective digital output DQn.A is reset.

The following figure shows an example of an output sequence for the case that you set SW_ENABLE while digital input DIn.0 is set.

![Example 2 of an output sequence](images/122015383307_DV_resource.Stream@PNG-en-US.png)

Example 2 of an output sequence

If you set SW_ENABLE while digital input DIn.0 is set, the first (falling) edge of DIn.0 is ignored.

##### Aborting the output sequence

If you reset the SW_ENABLE control bit, the software enable is deactivated and the current output sequence is aborted. The STS_ENABLE feedback bit and the digital output DQn.A are reset.

A renewed pulse output is only possible after a restart of the output sequence.

##### Minimum pulse duration and minimum interpulse period

The minimum pulse duration and the minimum interpulse period are the minimum pulse duration and interpulse period that are to be output. Each amounts to 1.5 µs when the [high-speed output](#high-speed-output-s7-1500-3) is activated and 10 µs when the high-speed output is deactivated.

Pulses and interpulse periods of digital input DIn.0 whose duration is less than the minimum pulse duration are ignored by the module and are not output at the digital output DQn.A.

The pulse or the interpulse period of DIn.0 is also ignored in the following cases:

- Pulse duration &lt; Input delay
- Pulse duration + Off delay ≤ On delay (ERR_PULSE is set)
- Pulse duration + Off delay + Minimum pulse duration &lt; On delay (ERR_PULSE is set)
- Interpulse period &lt; Input delay
- Interpulse period + On delay ≤ Off delay (ERR_PULSE is set)
- Interpulse period + On delay &lt; Off delay + Minimum interpulse period (ERR_PULSE is set)

A set ERR_PULSE feedback bit is cleared on the next rising edge at DIn.0.

##### Retriggering the On delay

In the following case, the module cancels the current On delay and restarts it with the next rising edge at digital input DIn.0:

On delay &gt; Pulse duration + Interpulse period

The following figure shows an example of the retriggering of the On delay:

![Retriggering the On delay](images/122225549835_DV_resource.Stream@PNG-en-US.png)

Retriggering the On delay

##### Retriggering the Off delay

In the following case, the module cancels the current Off delay and restarts it with the next rising edge at digital input DIn.0:

Off delay &gt; Pulse duration + Interpulse period

The following figure shows an example of the retriggering of the Off delay:

![Retriggering the Off delay](images/122225553675_DV_resource.Stream@PNG-en-US.png)

Retriggering the Off delay

#### On delay (S7-1500)

You set the duty cycle in the [control interface](#assignment-of-the-control-interface-s7-1500-3) using OUTPUT_VALUE as integer (UDINT). The value range is 0 to 85 s with a precision of 1 µs.

A change takes effect on the next rising edge at digital input DIn.0.

#### Off delay (S7-1500)

You set the Off delay from 0 to 85 s with a precision of 1 µs in the hardware configuration.

In addition, you can change the OFF delay via the control interface by entering a new value in SLOT as integer (UDINT). In so doing, you use the MODE_SLOT control bit to choose whether you want to apply a change once or cyclically:

| Symbol | Meaning |
| --- | --- |
| MODE_SLOT = 0 | One-time change: As soon as you write the value 3<sub>D</sub> in the corresponding output byte, the value from SLOT is applied once as the OFF delay and kept until the next change.  A change using SLOT takes effect on the next falling edge at digital input DIn.0. |
| MODE_SLOT = 1 | Cyclic change: When you write the value 19<sub>D</sub> in the corresponding output byte, the current value from SLOT in each case is applied cyclically as the Off delay.  A change using SLOT takes effect on the next falling edge at digital input DIn.0. |

For more detailed information, refer to the section  Handling the SLOT parameters.

#### High-speed output (S7-1500)

The high-speed output function enables an output frequency of a maximum of 100 kHz with an output current of a maximum of 100 mA. A high-speed output generates very steep edges. The high-speed output generates signals at a higher frequency, but provides a lower maximum load current. The high-speed output is only available in two-channel operation.

The following table presents the minimum and maximum pulse duration, period duration and frequency depending on whether or not the high-speed output is activated:

|  | Minimum value |  | Maximum value |  |
| --- | --- | --- | --- | --- |
| High-speed output deactivated | High-speed output activated | High-speed output deactivated | High-speed output activated |  |
| Pulse duration | 10 μs | 1,5 μs | 85000000 μs (= 85 s) |  |
| Period duration | 100 μs | 10 μs |  |  |
| Frequency | 0,02 Hz |  | 10 kHz | 100 kHz |

### Configuring (S7-1500)

#### Introduction

You configure the technology module and assign its parameters with the configuration software.

The user program controls and monitors the functions of the technology module via the control interface and feedback interface.

#### System environment

The technology module can be used in the following system environments:

| Possible use | Components needed | Configuration software | In the user program |
| --- | --- | --- | --- |
| Centralized operation with a CPU 151xSP | - ET 200SP automation system - TM Pulse 2x24V | STEP 7 (TIA Portal):  Device configuration and parameter setting with hardware configuration | Direct access to control interface and feedback interface in the I/O data |
| Distributed operation with an S7-1500 CPU | - S7-1500 automation system - ET 200SP distributed I/O system - TM Pulse 2x24V | STEP 7 (TIA Portal):  Device configuration and parameter setting with hardware configuration |  |
| Distributed operation with an S7-300/400 CPU | - S7-300/400 automation system - ET 200SP distributed I/O system - TM Pulse 2x24V | STEP 7 (TIA Portal):  Device configuration and parameter setting with hardware configuration  STEP 7:  Device configuration and parameter setting with HSP |  |
| Distributed operation on the PROFINET IO in a third-party system | - Third-party automation system - ET 200SP distributed I/O system - TM Pulse 2x24V | Third-party configuration software:   Device configuration and parameter setting with GSD file |  |
| Distributed operation on the PROFIBUS DP in a third-party system | - Third-party automation system - ET 200SP distributed I/O system - TM Pulse 2x24V | Third-party configuration software:  GSD file; device configuration and parameter setting using data record 128 |  |

#### Hardware Support Packages (HSP)

**STEP 7**

The Hardware Support Packages (HSP) are available for download on the [Internet](https://support.industry.siemens.com/cs/ww/en/view/23183356).

#### GSD file

The respective GSD file for the ET 200SP distributed I/O system is available for download on the Internet:

- [GSD file PROFINET IO](http://support.automation.siemens.com/WW/view/en/57138621)
- [GSD file PROFIBUS DP](http://support.automation.siemens.com/WW/view/en/73016883)

### Reaction to CPU STOP (S7-1500)

You set the response of the channel to a CPU STOP in the parameters of the device configuration.

Response of channel to CPU STOP

| Option | Meaning |
| --- | --- |
| Output substitute value | The channel outputs the configured substitute values at the digital outputs until the next STOP-RUN transition of the CPU. You can configure the substitute value 1 for only one of the two digital outputs.  An active output sequence is stopped and the STS_ENABLE feedback bit is reset.  The technology module is set to its startup state after a STOP-RUN transition. Before you can start a new pulse output, you must reset the SW_ENABLE control bit. |
| Continue operation | The channel continues to operate.  The digital outputs continue to switch according to the parameter assignment. An active output sequence will thus be continued.  The configuration of the technology module is not reset after a STOP-RUN transition. |

### Parameter setting (S7-1500)

You use various parameters to specify the properties of the technology module. Depending on the settings, not all parameters are available. When parameters are assigned in the user program, the parameters are transferred to the module with the "WRREC" instruction and data record 128.

You set the parameters of the module as follows in this operating mode:

| Parameter setting via... | Basic procedure |
| --- | --- |
| Hardware configuration in STEP 7 (TIA Portal) | 1. Insert the module from the hardware catalog under "Technology modules". 2. Set the "On/Off delay" mode and the further parameters of the module in the hardware configuration. 3. Download the project to the CPU. |
| Hardware configuration in STEP 7 with HSP | 1. Install the corresponding HSP file. You will then find the module in the hardware catalog under "ET 200SP". 2. Set the "On/Off delay" mode and the further parameters of the module in the hardware configuration. 3. Download the project to the CPU. |
| Hardware configuration with GSD file for distributed operation on PROFINET IO | 1. Install the latest PROFINET GSD file. You will then find the module in the hardware catalog under "Other field devices &gt; PROFINET IO &gt; I/O". 2. Set the "On/Off delay" mode and the further parameters of the module in the hardware configuration. 3. Download the project to the CPU. |
| Hardware configuration with GSD file for distributed operation on PROFIBUS DP | 1. Install the latest PROFIBUS GSD file. You will then find the module in the hardware catalog under "Other field devices &gt; PROFIBUS DP &gt; I/O". 2. Download the project to the CPU. The parameters of the module are also downloaded with their default settings (see table below). 3. Set the "On/Off delay" mode and the further parameters in the user program using data record 128. |

#### Parameters of the TM Pulse 2x24V in "On/Off delay" mode

The default settings of the parameters are shown in bold in the "Value range" column.

Adjustable parameters

| Parameter | Value range | Scope |
| --- | --- | --- |
| Channel configuration<sup>1</sup> | - **2 channels (2 A)** - 1 channel (4 A) | Module |
| Reaction to CPU STOP | - **Output substitute value** - Continue operation | Channel |
| Substitute value for DQA | - **0** - 1 | Channel |
| Substitute value for DQB | - **0** - 1 | Channel |
| Group diagnostics | - **Deactivated** - Activated | Channel |
| Diagnostics DQA | - **Deactivated** - Activated | Channel |
| Diagnostics DQB | - **Deactivated** - Activated | Channel |
| High-speed output (0.1 A) | - **Deactivated** - Activated | Channel |
| Input delay for digital inputs | - None - 0.05 ms - **0.1 ms** - 0.4 ms - 0.8 ms - 1.6 ms - 3.2 ms - 12.8 ms - 20 ms | Channel |
| Off delay for pulse output | **0**...85000000 μs | Channel |
| <sup>1</sup> When configuring with HSP for STEP 7 or with a GSD file, you define the channel configuration by the selection of the module name. |  |  |

> **Note**
>
> **PROFIBUS GSD configuration**
>
> When configuring with a PROFIBUS GSD file, the possible parameter assignments are not available. The parameters are preassigned in the module with the default setting. Set the "On/Off delay" mode and the further parameters in the user program using data record 128.

### Address space (S7-1500)

#### Address space of the technology module

Size of input and output addresses

|  | Inputs | Outputs |
| --- | --- | --- |
| Size per technology channel | 8 bytes | 12 bytes |
| Size in one-channel operation | 8 bytes | 12 bytes |
| Size in two-channel operation | 16 bytes | 24 bytes |

### Control interface and feedback interface (S7-1500)

This section contains information on the following topics:

- [Library with PLC data types (S7-1500)](#library-with-plc-data-types-s7-1500-3)
- [Assignment of the control interface (S7-1500)](#assignment-of-the-control-interface-s7-1500-3)
- [Assignment of the feedback interface (S7-1500)](#assignment-of-the-feedback-interface-s7-1500-3)

#### Library with PLC data types (S7-1500)

> **Note**
>
> A library of PLC data types (LPD) for STEP 7 (TIA Portal) and SIMATIC S7-1200 / S7-1500 is available for download on the [Internet](https://support.industry.siemens.com/cs/ww/en/view/109482396).

#### Assignment of the control interface (S7-1500)

The user program uses the control interface to influence the behavior of the technology module.

##### Control interface per channel

The following table shows the control interface assignment:

| Byte offset relative to start address Channel 0/1 **↓ ↓** |  | Bit 7 | Bit 6 | Bit 5 | Bit 4 | Bit 3 | Bit 2 | Bit 1 | Bit 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 … 3 | 12 … 15 | OUTPUT_VALUE  UDINT: On delay |  |  |  |  |  |  |  |
| 4 … 7 | 16 … 19 | SLOT  UDINT: Load value |  |  |  |  |  |  |  |
| 8 | 20 | Reserved |  |  | MODE_ SLOT | LD_SLOT |  |  |  |
| 9 | 21 | Reserved |  |  | SET_DQB | SET_DQA | Reserved | TM_ CTRL_DQ | SW_ ENABLE |
| 10 | 22 | Reserved |  |  |  |  |  |  | RES_ ERROR |
| 11 | 23 | Reserved |  |  |  |  |  |  |  |

> **Note**
>
> Channel 1 is only available in two-channel operation of the module.

| Control bit/value | Explanations |
| --- | --- |
| OUTPUT_VALUE | You specify the On delay with this value.  Value range:  - On delay in μs: 0 to 85000000<sub>D</sub>   If the setting is outside the value range, the ERR_OUT_VAL feedback bit is set and the last valid On delay is used. |
| SLOT | You specify the load value with this value.  Value range:   - Off delay in μs: 0 to 85000000<sub>D</sub>   You specify whether to apply a change once or cyclically with MODE_SLOT.  Invalid values trigger setting of feedback bit ERR_LD (when MODE_SLOT = 0) or ERR_SLOT_VAL (when MODE_SLOT = 1). |
| MODE_SLOT | You specify whether you want to apply a change in SLOT once or cyclically with this bit.  0 means: As soon as you write the value 3<sub>D</sub> in the corresponding output byte, the value from SLOT is applied once and kept until the next change. A change using SLOT takes effect on the next falling edge at DIn.0. After a restart of the module, the value is overwritten with the value set in the hardware configuration.   1 means: When you write the value 19<sub>D</sub> in the corresponding output byte, the current value from SLOT in each case is applied cyclically. A change using SLOT takes effect on the next falling edge at DIn.0. |
| LD_SLOT | You specify the meaning of the value in SLOT with this load request:  - 0000<sub>B</sub> means: No action, idle - 0011<sub>B</sub> means: Off delay in μs:   Values not listed are invalid and trigger setting of feedback bit ERR_LD (when MODE_SLOT = 0) or ERR_SLOT_VAL (when MODE_SLOT = 1). |
| SET_DQA | You use this bit to set digital output DQn.A when TM_CTRL_DQ and SET_DQB are set to 0. |
| SET_DQB | You use this bit to set digital output DQn.B when TM_CTRL_DQ and SET_DQA are set to 0. |
| TM_CTRL_DQ | You enable the technological function of the digital output with this bit.   - 0 means: SET_DQA and SET_DQB define states of DQn.A and DQn.B - 1 means: Output sequence defines the state of DQn.A; DQn.B is always 0. |
| SW_ENABLE | You activate the software enable with this bit. If you are using the hardware enable, it is combined with the software enable.  - 0 means: Stop output - 1 means: Start output   Use of the HW enable is activated through parameter assignment. The HW enable is controlled externally using the digital input DIn.0. |
| RES_ERROR | You use this bit to reset the following feedback bits when errors are pending:  - ERR_24V - ERR_DQA - ERR_DQB - ERR_LD |
| Reserved | Reserved bits must be set to 0. |

#### Assignment of the feedback interface (S7-1500)

The user program receives current values and status information from the technology module via the feedback interface.

##### Feedback interface per channel

The following table shows the assignment of the feedback interface:

| Byte offset relative to start address Channel 0/1 **↓ ↓** |  | Bit 7 | Bit 6 | Bit 5 | Bit 4 | Bit 3 | Bit 2 | Bit 1 | Bit 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 8 | ERR_ SLOT_VAL | ERR_ OUT_VAL | ERR_DQB | ERR_DQA | ERR_ PULSE | ERR_LD | ERR_24V | ERR_PWR |
| 1 | 9 | Reserved |  | STS_SW_ ENABLE | STS_ READY | Reserved | STS_LD_ SLOT | Reserved |  |
| 2 | 10 | Reserved |  |  |  | STS_DI | STS_DQB | STS_DQA | STS_ ENABLE |
| 3 | 11 | Reserved |  |  |  | SEQ_CNT |  |  |  |
| 4 ... 7 | 12 ... 15 | Reserved |  |  |  |  |  |  |  |

> **Note**
>
> Channel 1 is only available in two-channel operation of the module.

| Feedback bit/value | Explanations |
| --- | --- |
| ERR_SLOT_VAL | This bit indicates that the value in SLOT or LD_SLOT is invalid (when MODE_SLOT = 1) and was not accepted.   As soon as the module has received a valid value from the control interface, ERR_SLOT_VAL is automatically reset. |
| ERR_OUT_VAL | This bit indicates that the value in OUTPUT_VALUE is invalid.  As soon as the module has received a valid value from the control interface, ERR_OUT_VAL is automatically reset. |
| ERR_DQA | This bit indicates a short-circuit or an overload at the output DQn.A. If you have enabled the diagnostics interrupt "Diagnostics DQA", the diagnostics interrupt "Error at digital outputs" is triggered when this error occurs.   The bit is reset once you have acknowledged the error with RES_ERROR. |
| ERR_DQB | This bit indicates a short-circuit or an overload at the output DQn.B or the attempted simultaneous setting of the SET_DQA and SET_DQB control bits. If you have enabled the diagnostics interrupt "Diagnostics DQB", the diagnostics interrupt "Error at digital outputs" is triggered when this error occurs.   The bit is reset once you have acknowledged the error with RES_ERROR. |
| ERR_PULSE | This bit indicates an error in the pulse output. |
| ERR_LD | This bit indicates that the value in SLOT or LD_SLOT (when MODE_SLOT = 0) is invalid and was not accepted.   The bit is reset once you have acknowledged the error with RES_ERROR. |
| ERR_24V | This bit indicates a short-circuit or an overload at output 24VDC If you have enabled diagnostic interrupts, the diagnostic interrupt "Short circuit / overload of the sensor supply voltage" is triggered when this error occurs.   The bit is reset once you have acknowledged the error with RES_ERROR. |
| ERR_PWR | This bit indicates that supply voltage L+ is too low. If you have enabled the diagnostic interrupts, the diagnostic interrupt "Supply voltage fault" is triggered when an error occurs.   As soon as supply voltage L+ is sufficiently high again, ERR_PWR is automatically reset.  The bit is not set if no supply voltage is present. |
| STS_SW_ENABLE | This bit indicates the status of the SW enable.   - 0 means: SW enable not active - 1 means: SW enable active |
| STS_READY | This bit indicates that the module is supplying valid user data. The module is started and configured. |
| STS_LD_SLOT | A status change (toggling) of this bit indicates that the LD_SLOT load request was detected and executed (when MODE_SLOT = 0). |
| STS_DI | This bit indicates the status of the digital input DIn.0. |
| STS_DQA | This bit indicates the status of the digital output DQn.A. |
| STS_DQB | This bit indicates the status of the digital output DQn.B. |
| STS_ENABLE | This bit indicates that an output sequence is active. |
| SEQ_CNT | This value indicates the number of completed output sequences as sequence counter. |
| Reserved | Reserved bits are set to 0. |

### Isochronous mode (S7-1500)

The technology module supports the "Isochronous mode" system function. Isochronous mode has no effect in the "On/Off delay" mode.

#### Further information

You will find a detailed description of isochronous mode in:

- In the isochronous mode function manual as a download from the [Internet](https://support.industry.siemens.com/cs/ww/en/view/109755401).
- PROFINET with STEP 7 function manual available for download on the [Internet](https://support.industry.siemens.com/cs/ww/en/view/49948856).

## Frequency output mode (S7-1500)

This section contains information on the following topics:

- [Function (S7-1500)](#function-s7-1500-4)
- [Configuring (S7-1500)](#configuring-s7-1500-4)
- [Reaction to CPU STOP (S7-1500)](#reaction-to-cpu-stop-s7-1500-4)
- [Parameter setting (S7-1500)](#parameter-setting-s7-1500-4)
- [Address space (S7-1500)](#address-space-s7-1500-4)
- [Control interface and feedback interface (S7-1500)](#control-interface-and-feedback-interface-s7-1500-3)
- [Isochronous mode (S7-1500)](#isochronous-mode-s7-1500-4)

### Function (S7-1500)

This section contains information on the following topics:

- [Introduction (S7-1500)](#introduction-s7-1500-4)
- [Output sequence (S7-1500)](#output-sequence-s7-1500-4)
- [Frequency (S7-1500)](#frequency-s7-1500)
- [On delay (S7-1500)](#on-delay-s7-1500-4)
- [High-speed output (S7-1500)](#high-speed-output-s7-1500-4)

#### Introduction  (S7-1500)

In this operating mode, the respective channel of the technology module outputs a signal with a fixed duty cycle of 50% and the configured On delay. You specify the frequency via the control interface.

#### Output sequence (S7-1500)

##### Starting the output sequence

In order to output the output sequence at the digital output DQn.A, the TM_CTRL_DQ control bit must be set. To start the output sequence using the software enable, you set the SW_ENABLE [control bit](#assignment-of-the-control-interface-s7-1500-4). The STS_SW_ENABLE feedback bit indicates that the software enable in the technology module is active.

You can additionally use the hardware enable via the respective digital input DIn.0. You can configure an input delay for DIn.0.

**Pulse diagram**

The following figure shows an example of an output sequence when DIn.0 is being used as a hardware enable.

![Example of an output sequence](images/122024015499_DV_resource.Stream@PNG-en-US.png)

Example of an output sequence

If you are using the hardware enable, it is combined with the software enable. When the software enable is active, the output sequence starts at the first rising edge of the hardware enable. Additional rising edges of the hardware enable during the output sequence are ignored. If the hardware enable is set and remains set for the duration of the input delay, the On delay is started and the STS_ENABLE feedback bit is set. As soon as the on delay has elapsed, the pulses with the assigned frequency are output at the respective digital output DQn.A. The output sequence runs continuously, as long as SW_ENABLE is set.

If you are not using a hardware enable, the On delay starts at the rising edge of SW_ENABLE.

##### Aborting the output sequence

If you reset the SW_ENABLE control bit, the software enable is deactivated and the current output sequence is aborted. The last period is not completed. The STS_ENABLE feedback bit and the digital output DQn.A are reset.

A renewed pulse output is only possible after a restart of the output sequence.

#### Frequency (S7-1500)

You set the output frequency in the control interface using OUTPUT_VALUE as floating point number (REAL). The value range is dependent on whether or not the [high-speed output function](#high-speed-output-s7-1500-4) is being used:

| High-speed output | Value range of  OUTPUT_VALUE | Value range of the frequency |
| --- | --- | --- |
| Activated | 0.02 to 100000 | 0.02 Hz to 100000 Hz = 0.02 Hz to 100 kHz |
| Deactivated | 0.02 to 10000 | 0.02 Hz to 10000 Hz = 0.02 Hz to 10 kHz |

A changed frequency takes effect with the next rising edge at DQn.A.

##### Accuracy

The output sequence is output with an accuracy of ±100 ppm at DQn.A.

#### On delay (S7-1500)

You set the On delay from 0 s to 85 s with a precision of 1 µs in the hardware configuration.

In addition, you can change the On delay via the control interface by entering a new value in SLOT as an integer (UDINT). In so doing, you use the MODE_SLOT control bit to choose whether you want to apply a change once or cyclically:

| Symbol | Meaning |
| --- | --- |
| MODE_SLOT = 0 | One-time change: As soon as you write the value 2<sub>D</sub> in the corresponding output byte, the value from SLOT is applied once as the On delay and kept until the next change.  A change via SLOT takes effect at the next output sequence. An active output sequence is not affected by the change. |
| MODE_SLOT = 1 | Cyclic change: When you write the value 18<sub>D</sub> in the corresponding output byte, the current value from SLOT in each case is applied cyclically as the On delay.  A change via SLOT takes effect at the next output sequence. An active output sequence is not affected by the change. |

For more detailed information, refer to the section  Handling the SLOT parameters.

#### High-speed output (S7-1500)

The high-speed output function enables an output frequency of a maximum of 100 kHz with an output current of a maximum of 100 mA. A high-speed output generates very steep edges. The high-speed output generates signals at a higher frequency, but provides a lower maximum load current. The high-speed output is only available in two-channel operation.

The following table presents the value range of the pulse duration and frequency depending on whether or not the high-speed output function is activated:

|  | Minimum value |  | Maximum value |  |
| --- | --- | --- | --- | --- |
| High-speed output deactivated | High-speed output activated | High-speed output deactivated | High-speed output activated |  |
| Pulse duration | 10 μs | 1,5 μs | 85000000 μs (= 85 s) |  |
| Frequency | 0,02 Hz |  | 10 kHz | 100 kHz |

### Configuring (S7-1500)

#### Introduction

You configure the technology module and assign its parameters with the configuration software.

The user program controls and monitors the functions of the technology module via the control interface and feedback interface.

#### System environment

The technology module can be used in the following system environments:

| Possible use | Components needed | Configuration software | In the user program |
| --- | --- | --- | --- |
| Centralized operation with a CPU 151xSP | - ET 200SP automation system - TM Pulse 2x24V | STEP 7 (TIA Portal):  Device configuration and parameter setting with hardware configuration | Direct access to control interface and feedback interface in the I/O data |
| Distributed operation with an S7-1500 CPU | - S7-1500 automation system - ET 200SP distributed I/O system - TM Pulse 2x24V | STEP 7 (TIA Portal):  Device configuration and parameter setting with hardware configuration |  |
| Distributed operation with an S7-300/400 CPU | - S7-300/400 automation system - ET 200SP distributed I/O system - TM Pulse 2x24V | STEP 7 (TIA Portal):  Device configuration and parameter setting with hardware configuration  STEP 7:  Device configuration and parameter setting with HSP |  |
| Distributed operation on the PROFINET IO in a third-party system | - Third-party automation system - ET 200SP distributed I/O system - TM Pulse 2x24V | Third-party configuration software:   Device configuration and parameter setting with GSD file |  |
| Distributed operation on the PROFIBUS DP in a third-party system | - Third-party automation system - ET 200SP distributed I/O system - TM Pulse 2x24V | Third-party configuration software:  GSD file; device configuration and parameter setting using data record 128 |  |

#### Hardware Support Packages (HSP)

**STEP 7**

The Hardware Support Packages (HSP) are available for download on the [Internet](https://support.industry.siemens.com/cs/ww/en/view/23183356).

#### GSD file

The respective GSD file for the ET 200SP distributed I/O system is available for download on the Internet:

- [GSD file PROFINET IO](http://support.automation.siemens.com/WW/view/en/57138621)
- [GSD file PROFIBUS DP](http://support.automation.siemens.com/WW/view/en/73016883)

### Reaction to CPU STOP (S7-1500)

You set the response of the channel to a CPU STOP in the parameters of the device configuration.

Response of channel to CPU STOP

| Option | Meaning |
| --- | --- |
| Output substitute value | The channel outputs the configured substitute values at the digital outputs until the next STOP-RUN transition of the CPU. You can configure the substitute value 1 for only one of the two digital outputs.  An active output sequence is stopped and the STS_ENABLE feedback bit is reset.  The technology module is set to its startup state after a STOP-RUN transition. Before you can start a new pulse output, you must reset the SW_ENABLE control bit. |
| Continue operation | The channel continues to operate.  The digital outputs continue to switch according to the parameter assignment. An active output sequence will thus be continued. If you have configured the hardware enable, you can also start additional output sequences using DIn.0.  The configuration of the technology module is not reset after a STOP-RUN transition. |

### Parameter setting (S7-1500)

You use various parameters to specify the properties of the technology module. Depending on the settings, not all parameters are available. When parameters are assigned in the user program, the parameters are transferred to the module with the "WRREC" instruction and data record 128.

You set the parameters of the module as follows in this operating mode:

| Parameter setting via... | Basic procedure |
| --- | --- |
| Hardware configuration in STEP 7 (TIA Portal) | 1. Insert the module from the hardware catalog under "Technology modules". 2. Set the "Frequency output" mode and the further parameters of the module in the hardware configuration. 3. Download the project to the CPU. |
| Hardware configuration in STEP 7 with HSP | 1. Install the corresponding HSP file. You will then find the module in the hardware catalog under "ET 200SP". 2. Set the "Frequency output" mode and the further parameters of the module in the hardware configuration. 3. Download the project to the CPU. |
| Hardware configuration with GSD file for distributed operation on PROFINET IO | 1. Install the latest PROFINET GSD file. You will then find the module in the hardware catalog under "Other field devices &gt; PROFINET IO &gt; I/O". 2. Set the "Frequency output" mode and the further parameters of the module in the hardware configuration. 3. Download the project to the CPU. |
| Hardware configuration with GSD file for distributed operation on PROFIBUS DP | 1. Install the latest PROFIBUS GSD file. You will then find the module in the hardware catalog under "Other field devices &gt; PROFIBUS DP &gt; I/O". 2. Download the project to the CPU. The parameters of the module are also downloaded with their default settings (see table below). 3. Set the "Frequency output" mode and the further parameters in the user program using data record 128. |

#### Parameters of the TM Pulse 2x24V in "Frequency output" mode

The default settings of the parameters are shown in bold in the "Value range" column.

Adjustable parameters

| Parameter | Value range | Scope |
| --- | --- | --- |
| Channel configuration<sup>1</sup> | - **2 channels (2 A)** - 1 channel (4 A) | Module |
| Reaction to CPU STOP | - **Output substitute value** - Continue operation | Channel |
| Substitute value for DQA | - **0** - 1 | Channel |
| Substitute value for DQB | - **0** - 1 | Channel |
| Group diagnostics | - **Deactivated** - Activated | Channel |
| Diagnostics DQA | - **Deactivated** - Activated | Channel |
| Diagnostics DQB | - **Deactivated** - Activated | Channel |
| High-speed output (0.1 A) | - **Deactivated** - Activated | Channel |
| Function DI | - **Input** - HW enable | Channel |
| Input delay for digital inputs | - None - 0.05 ms - **0.1 ms** - 0.4 ms - 0.8 ms - 1.6 ms - 3.2 ms - 12.8 ms - 20 ms | Channel |
| On delay for pulse output | **0**...85000000 μs | Channel |
| <sup>1</sup> When configuring with HSP for STEP 7 or with a GSD file, you define the channel configuration by the selection of the module name. |  |  |

> **Note**
>
> **PROFIBUS GSD configuration**
>
> When configuring with a PROFIBUS GSD file, the possible parameter assignments are not available. The parameters are preassigned in the module with the default setting. Set the "Frequency output" mode and the further parameters in the user program using data record 128.

### Address space (S7-1500)

#### Address space of the technology module

Size of input and output addresses

|  | Inputs | Outputs |
| --- | --- | --- |
| Size per technology channel | 8 bytes | 12 bytes |
| Size in one-channel operation | 8 bytes | 12 bytes |
| Size in two-channel operation | 16 bytes | 24 bytes |

### Control interface and feedback interface (S7-1500)

This section contains information on the following topics:

- [Library with PLC data types (S7-1500)](#library-with-plc-data-types-s7-1500-4)
- [Assignment of the control interface (S7-1500)](#assignment-of-the-control-interface-s7-1500-4)
- [Assignment of the feedback interface (S7-1500)](#assignment-of-the-feedback-interface-s7-1500-4)

#### Library with PLC data types (S7-1500)

> **Note**
>
> A library of PLC data types (LPD) for STEP 7 (TIA Portal) and SIMATIC S7-1200 / S7-1500 is available for download on the [Internet](https://support.industry.siemens.com/cs/ww/en/view/109482396).

#### Assignment of the control interface (S7-1500)

The user program uses the control interface to influence the behavior of the technology module.

##### Control interface per channel

The following table shows the control interface assignment:

| Byte offset relative to start address Channel 0/1 **↓ ↓** |  | Bit 7 | Bit 6 | Bit 5 | Bit 4 | Bit 3 | Bit 2 | Bit 1 | Bit 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 … 3 | 12 … 15 | OUTPUT_VALUE  REAL: Frequency |  |  |  |  |  |  |  |
| 4 … 7 | 16 … 19 | SLOT  UDINT: Load value |  |  |  |  |  |  |  |
| 8 | 20 | Reserved |  |  | MODE_ SLOT | LD_SLOT |  |  |  |
| 9 | 21 | Reserved |  |  | SET_DQB | SET_DQA | Reserved | TM_ CTRL_DQ | SW_ ENABLE |
| 10 | 22 | Reserved |  |  |  |  |  |  | RES_ ERROR |
| 11 | 23 | Reserved |  |  |  |  |  |  |  |

> **Note**
>
> Channel 1 is only available in two-channel operation of the module.

| Control bit/value | Explanations |
| --- | --- |
| OUTPUT_VALUE | You specify the frequency with this value.  Value range:  - Frequency in Hz, when High-speed output is deactivated: 0.02 to 10000<sub>D</sub> - Frequency in Hz, when high-speed output is activated: 0.02 to 100000<sub>D</sub>   If the low limit or the high limit is violated, the feedback bit ERR_OUT_VAL is set and the last valid frequency is used. |
| SLOT | You specify the load value with this value.  Value range:   - On delay in μs: 0 to 85000000<sub>D</sub>   You specify whether to apply a change once or cyclically with MODE_SLOT.  Invalid values trigger setting of feedback bit ERR_LD (when MODE_SLOT = 0) or ERR_SLOT_VAL (when MODE_SLOT = 1). |
| MODE_SLOT | You specify whether you want to apply a change in SLOT once or cyclically with this bit.  0 means: As soon as you write the value 2<sub>D</sub> in the corresponding output byte, the value from SLOT is applied once and kept until the next change. A change via SLOT takes effect at the next output sequence. After a restart of the module, the value is overwritten with the value set in the hardware configuration.   1 means: When you write the value 18<sub>D</sub> in the corresponding output byte, the current value from SLOT in each case is applied cyclically. A change via SLOT takes effect at the next output sequence. |
| LD_SLOT | You specify the meaning of the value in SLOT with this load request:  - 0000<sub>B</sub> means: No action, idle - 0010<sub>B</sub> means: On delay in μs   Values not listed are invalid and trigger setting of feedback bit ERR_LD (when MODE_SLOT = 0) or ERR_SLOT_VAL (when MODE_SLOT = 1). |
| SET_DQA | You use this bit to set digital output DQn.A when TM_CTRL_DQ and SET_DQB are set to 0. |
| SET_DQB | You use this bit to set digital output DQn.B when TM_CTRL_DQ and SET_DQA are set to 0. |
| TM_CTRL_DQ | You enable the technological function of the digital output with this bit.   - 0 means: SET_DQA and SET_DQB define states of DQn.A and DQn.B - 1 means: Output sequence defines the state of DQn.A; DQn.B is always 0. |
| SW_ENABLE | You activate the software enable with this bit. If you are using the hardware enable, it is combined with the software enable.  - 0 means: Stop output - 1 means: Start output   Use of the HW enable is activated through parameter assignment. The HW enable is controlled externally using the digital input DIn.0. |
| RES_ERROR | You use this bit to reset the following feedback bits when errors are pending:  - ERR_24V - ERR_DQA - ERR_DQB - ERR_LD |
| Reserved | Reserved bits must be set to 0. |

#### Assignment of the feedback interface (S7-1500)

The user program receives current values and status information from the technology module via the feedback interface.

##### Feedback interface per channel

The following table shows the assignment of the feedback interface:

| Byte offset relative to start address Channel 0/1 **↓ ↓** |  | Bit 7 | Bit 6 | Bit 5 | Bit 4 | Bit 3 | Bit 2 | Bit 1 | Bit 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 8 | ERR_ SLOT_VAL | ERR_ OUT_VAL | ERR_DQB | ERR_DQA | Reserved | ERR_LD | ERR_24V | ERR_PWR |
| 1 | 9 | Reserved |  | STS_SW_ ENABLE | STS_ READY | Reserved | STS_LD_ SLOT | Reserved |  |
| 2 | 10 | Reserved |  |  |  | STS_DI | STS_DQB | STS_DQA | STS_ ENABLE |
| 3 ... 7 | 11 ... 15 | Reserved |  |  |  |  |  |  |  |

> **Note**
>
> Channel 1 is only available in two-channel operation of the module.

| Feedback bit/value | Explanations |
| --- | --- |
| ERR_SLOT_VAL | This bit indicates that the value in SLOT or LD_SLOT is invalid (when MODE_SLOT = 1) and was not accepted.   As soon as the module has received a valid value from the control interface, ERR_SLOT_VAL is automatically reset. |
| ERR_OUT_VAL | This bit indicates that the value in OUTPUT_VALUE is invalid.  As soon as the module has received a valid value from the control interface, ERR_OUT_VAL is automatically reset. |
| ERR_DQA | This bit indicates a short-circuit or an overload at the output DQn.A. If you have enabled the diagnostics interrupt "Diagnostics DQA", the diagnostics interrupt "Error at digital outputs" is triggered when this error occurs.   The bit is reset once you have acknowledged the error with RES_ERROR. |
| ERR_DQB | This bit indicates a short-circuit or an overload at the output DQn.B or the attempted simultaneous setting of the SET_DQA and SET_DQB control bits. If you have enabled the diagnostics interrupt "Diagnostics DQB", the diagnostics interrupt "Error at digital outputs" is triggered when this error occurs.   The bit is reset once you have acknowledged the error with RES_ERROR. |
| ERR_LD | This bit indicates that the value in SLOT or LD_SLOT (when MODE_SLOT = 0) is invalid and was not accepted.   The bit is reset once you have acknowledged the error with RES_ERROR. |
| ERR_24V | This bit indicates a short-circuit or an overload at output 24VDC If you have enabled diagnostic interrupts, the diagnostic interrupt "Short circuit / overload of the sensor supply voltage" is triggered when this error occurs.   The bit is reset once you have acknowledged the error with RES_ERROR. |
| ERR_PWR | This bit indicates that supply voltage L+ is too low. If you have enabled the diagnostic interrupts, the diagnostic interrupt "Supply voltage fault" is triggered when an error occurs.   As soon as supply voltage L+ is sufficiently high again, ERR_PWR is automatically reset.  The bit is not set if no supply voltage is present. |
| STS_SW_ENABLE | This bit indicates the status of the SW enable.   - 0 means: SW enable not active - 1 means: SW enable active |
| STS_READY | This bit indicates that the module is supplying valid user data. The module is started and configured. |
| STS_LD_SLOT | A status change (toggling) of this bit indicates that the LD_SLOT load request was detected and executed (when MODE_SLOT = 0). |
| STS_DI | This bit indicates the status of the digital input DIn.0. |
| STS_DQA | This bit indicates the status of the digital output DQn.A. |
| STS_DQB | This bit indicates the status of the digital output DQn.B. |
| STS_ENABLE | This bit indicates that an output sequence is active. |
| Reserved | Reserved bits are set to 0. |

### Isochronous mode (S7-1500)

The technology module supports the "Isochronous mode" system function. If you are not using a hardware enable, the output sequence starts in isochronous mode at time T<sub>o</sub> after the SW_ENABLE control bit has been set.

#### Further information

You will find a detailed description of isochronous mode in:

- In the isochronous mode function manual as a download from the [Internet](https://support.industry.siemens.com/cs/ww/en/view/109755401).
- PROFINET with STEP 7 function manual available for download on the [Internet](https://support.industry.siemens.com/cs/ww/en/view/49948856).

## PWM with DC motor motor (S7-1500)

This section contains information on the following topics:

- [Function (S7-1500)](#function-s7-1500-5)
- [Configuring (S7-1500)](#configuring-s7-1500-5)
- [Parameter setting (S7-1500)](#parameter-setting-s7-1500-5)
- [Address space (S7-1500)](#address-space-s7-1500-5)
- [Control interface and feedback interface (S7-1500)](#control-interface-and-feedback-interface-s7-1500-4)
- [Isochronous mode (S7-1500)](#isochronous-mode-s7-1500-5)

### Function (S7-1500)

This section contains information on the following topics:

- [Introduction (S7-1500)](#introduction-s7-1500-5)
- [Output sequence (S7-1500)](#output-sequence-s7-1500-5)
- [Duty cycle (S7-1500)](#duty-cycle-s7-1500-2)
- [Period duration (S7-1500)](#period-duration-s7-1500-2)
- [On delay (S7-1500)](#on-delay-s7-1500-5)

#### Introduction  (S7-1500)

In this operating mode, the respective channel of the technology module at the bipolar digital output sends a pulse width modulated signal to control a brushed DC motor in both directions of rotation. You specify the duty cycle via the control interface.

Each channel has a bipolar digital output DQn.A/DQn.B for the connection of a DC motor. The module works as four-quadrant actuator. DQn.A and DQn.B are connected inside the module as an H-bridge. For information on connecting the motor, refer to the section Connecting.

The duty cycle acts like a voltage and thus determines the speed of the motor. The sign of the duty cycle specifies the direction of rotation. When you drive the motor in forward direction, DQn.A is set and DQn.B is reset. When you drive the motor in the reverse direction, DQn.A is reset and DQn.B is set.

You can stop the motor using one of the following signals:

- Reset the control bit SW_ENABLE in the control interface
- Falling edge of the HW enable (DIn.0)
- Rising edge of the limit switch (DIn.0)

#### Output sequence (S7-1500)

##### Starting the output sequence

To start the output sequence using the software enable, you set the SW_ENABLE [control bit](#assignment-of-the-control-interface-s7-1500-5). The STS_SW_ENABLE feedback bit indicates that the software enable in the technology module is active.

You can additionally use the hardware enable via the respective digital input DIn.0. You can configure an input delay for DIn.0.

**Pulse diagram**

The following figure shows an example of an output sequence for the forward direction when DIn.0 is being used as a hardware enable.

![Example of an output sequence (HW enable)](images/122267062283_DV_resource.Stream@PNG-en-US.png)

Example of an output sequence (HW enable)

If you are using the hardware enable, it is combined with the software enable. When the software enable is active, the output sequence starts at the first rising edge of the hardware enable. If the hardware enable is set and remains set for the duration of the input delay, the On delay is started and the STS_ENABLE feedback bit is set. As soon as the On delay has elapsed, the pulse width modulated signal is output with the assigned duty cycle at the digital output DQn.A/DQn.B. The duty cycle is the ratio of pulse duration to period duration.

If you are not using a hardware enable, the On delay starts at the rising edge of SW_ENABLE. The hardware enable is not supported in isochronous mode. If you configure the hardware enable in isochronous mode, this is interpreted by the module as a limit switch.

The following figure shows an example of an output sequence for the forward direction when DIn.0 is being used as a limit switch.

![Example of an output sequence (limit switch)](images/122318824971_DV_resource.Stream@PNG-en-US.png)

Example of an output sequence (limit switch)

##### Aborting the output sequence

If you reset the SW_ENABLE control bit, the software enable is deactivated and the current output sequence is aborted. If canceled, the last period will not be completed. The feedback bit STS_ENABLE and DQn.A and DQn.B are reset (engine stop).

If you use the HW enable, you can alternatively cancel the output sequence with a falling edge at DIn.0. If you use the limit switch instead of the HW enable, you can alternatively cancel the output sequence with a rising edge at DIn.0.

A renewed pulse output is only possible after a restart of the output sequence.

#### Duty cycle (S7-1500)

The duty cycle corresponds to the ratio of pulse duration to period duration (also referred to as mark-to-space ratio).

You set the duty cycle in the [control interface](#assignment-of-the-control-interface-s7-1500-5) using OUTPUT_VALUE in S7 analog format (DINT). The sign specifies the direction of rotation of the motor. A positive value means forward direction. If you set the value 0, the motor is stopped. If you set the minimum value, the DQn.B is set during the entire period duration. If you set the maximum value, the DQn.A is set during the entire period duration. If you set a value above or below the value range, the minimum or maximum value is used.

A changed duty cycle takes effect with the next rising edge at DQn.A or DQn.B.

| Output format | Value range of  OUTPUT_VALUE | Pulse duration |
| --- | --- | --- |
| S7 analog output | ‒27648 ... 27648 | (OUTPUT_VALUE/27648) × Period duration |

Before changing the direction of rotation, it is recommended to set the value 0 for sufficiently long for OUTPUT_VALUE in order to first stop the motor. If the motor requires a ramp up or a ramp down, you must implement the ramp via a corresponding control of the duty cycle.

#### Period duration (S7-1500)

You set the period duration from 100 μs to 85 s with a precision of 1 µs in the hardware configuration.

In addition, you can change the period duration via the control interface by entering a new value in SLOT as an integer (UDINT). In so doing, you use the MODE_SLOT control bit to choose whether you want to apply a change once or cyclically:

| Symbol | Meaning |
| --- | --- |
| MODE_SLOT = 0 | One-time change: As soon as you write the value 1<sub>D</sub> in the corresponding output byte, the value from SLOT is applied once as the period duration and kept until the next change.  A change via SLOT takes effect at DQn.A/DQn.B with the next rising edge. |
| MODE_SLOT = 1 | Cyclic change: When you write the value 17<sub>D</sub> in the corresponding output byte, the current value from SLOT in each case is applied cyclically as the period duration.  A change via SLOT takes effect at DQn.A/DQn.B with the next rising edge. |

For more detailed information, refer to the section  Handling the SLOT parameters.

#### On delay (S7-1500)

You set the On delay from 0 s to 85 s with a precision of 1 µs in the hardware configuration.

In addition, you can change the On delay via the control interface by entering a new value in SLOT as an integer (UDINT). In so doing, you use the MODE_SLOT control bit to choose whether you want to apply a change once or cyclically:

| Symbol | Meaning |
| --- | --- |
| MODE_SLOT = 0 | One-time change: As soon as you write the value 2<sub>D</sub> in the corresponding output byte, the value from SLOT is applied once as the On delay and kept until the next change.  A change via SLOT takes effect at the next output sequence. An active output sequence is not affected by the change. |
| MODE_SLOT = 1 | Cyclic change: When you write the value 18<sub>D</sub> in the corresponding output byte, the current value from SLOT in each case is applied cyclically as the On delay.  A change via SLOT takes effect at the next output sequence. An active output sequence is not affected by the change. |

> **Note**
>
> In isochronous mode, a configured On delay has no effect.

For more detailed information, refer to the section  Handling the SLOT parameters.

### Configuring (S7-1500)

#### Introduction

You configure the technology module and assign its parameters with the configuration software.

The user program controls and monitors the functions of the technology module via the control interface and feedback interface.

#### System environment

The technology module can be used in the following system environments:

| Possible use | Components needed | Configuration software | In the user program |
| --- | --- | --- | --- |
| Centralized operation with a CPU 151xSP | - ET 200SP automation system - TM Pulse 2x24V | STEP 7 (TIA Portal):  Device configuration and parameter setting with hardware configuration | Direct access to control interface and feedback interface in the I/O data |
| Distributed operation with an S7-1500 CPU | - S7-1500 automation system - ET 200SP distributed I/O system - TM Pulse 2x24V | STEP 7 (TIA Portal):  Device configuration and parameter setting with hardware configuration |  |
| Distributed operation with an S7-300/400 CPU | - S7-300/400 automation system - ET 200SP distributed I/O system - TM Pulse 2x24V | STEP 7 (TIA Portal):  Device configuration and parameter setting with hardware configuration  STEP 7:  Device configuration and parameter setting with HSP |  |
| Distributed operation on the PROFINET IO in a third-party system | - Third-party automation system - ET 200SP distributed I/O system - TM Pulse 2x24V | Third-party configuration software:   Device configuration and parameter setting with GSD file |  |
| Distributed operation on the PROFIBUS DP in a third-party system | - Third-party automation system - ET 200SP distributed I/O system - TM Pulse 2x24V | Third-party configuration software:  GSD file; device configuration and parameter setting using data record 128 |  |

#### Hardware Support Packages (HSP)

**STEP 7**

The Hardware Support Packages (HSP) are available for download on the [Internet](https://support.industry.siemens.com/cs/ww/en/view/23183356).

#### GSD file

The respective GSD file for the ET 200SP distributed I/O system is available for download on the Internet:

- [GSD file PROFINET IO](http://support.automation.siemens.com/WW/view/en/57138621)
- [GSD file PROFIBUS DP](http://support.automation.siemens.com/WW/view/en/73016883)

### Parameter setting (S7-1500)

You use various parameters to specify the properties of the technology module. Depending on the settings, not all parameters are available. When parameters are assigned in the user program, the parameters are transferred to the module with the "WRREC" instruction and data record 128.

You set the parameters of the module as follows in this operating mode:

| Parameter setting via... | Basic procedure |
| --- | --- |
| Hardware configuration in STEP 7 (TIA Portal) | 1. Insert the module from the hardware catalog under "Technology modules". 2. Set the "PWM with DC motor" mode and the further parameters of the module in the hardware configuration. 3. Download the project to the CPU. |
| Hardware configuration in STEP 7 with HSP | 1. Install the corresponding HSP file. You will then find the module in the hardware catalog under "ET 200SP". 2. Set the "PWM with DC motor" mode and the further parameters of the module in the hardware configuration. 3. Download the project to the CPU. |
| Hardware configuration with GSD file for distributed operation on PROFINET IO | 1. Install the latest PROFINET GSD file. You will then find the module in the hardware catalog under "Other field devices &gt; PROFINET IO &gt; I/O". 2. Set the "PWM with DC motor" mode and the further parameters of the module in the hardware configuration. 3. Download the project to the CPU. |
| Hardware configuration with GSD file for distributed operation on PROFIBUS DP | 1. Install the latest PROFIBUS GSD file. You will then find the module in the hardware catalog under "Other field devices &gt; PROFIBUS DP &gt; I/O". 2. Download the project to the CPU. The parameters of the module are also downloaded with their default settings (see table below). 3. Set the "PWM with DC motor" mode and the further parameters in the user program using data record 128. |

#### Parameters of the TM Pulse 2x24V in "PWM with DC motor" mode

The default settings of the parameters are shown in bold in the "Value range" column.

Adjustable parameters

| Parameter | Value range | Scope |
| --- | --- | --- |
| Channel configuration<sup>1</sup> | - **2 channels (2 A)** - 1 channel (4 A) | Module |
| Group diagnostics | - **Deactivated** - Activated | Channel |
| Diagnostics DQA | - **Deactivated** - Activated | Channel |
| Diagnostics DQB | - **Deactivated** - Activated | Channel |
| Function DI | - **Input** - HW enable - Limit switch | Channel |
| Input delay for digital inputs | - None - 0.05 ms - **0.1 ms** - 0.4 ms - 0.8 ms - 1.6 ms - 3.2 ms - 12.8 ms - 20 ms | Channel |
| Period duration | 100...**1000**...85000000 μs | Channel |
| Actual period duration | Automatically calculated (read-only) | Channel |
| On delay for pulse output | **0**...85000000 μs | Channel |
| <sup>1</sup> When configuring with HSP for STEP 7 or with a GSD file, you define the channel configuration by the selection of the module name. |  |  |

> **Note**
>
> **PROFIBUS GSD configuration**
>
> When configuring with a PROFIBUS GSD file, the possible parameter assignments are not available. The parameters are preassigned in the module with the default setting. Set the "PWM with DC motor" mode and the further parameters in the user program using data record 128.

### Address space (S7-1500)

#### Address space of the technology module

Size of input and output addresses

|  | Inputs | Outputs |
| --- | --- | --- |
| Size per technology channel | 8 bytes | 12 bytes |
| Size in one-channel operation | 8 bytes | 12 bytes |
| Size in two-channel operation | 16 bytes | 24 bytes |

### Control interface and feedback interface (S7-1500)

This section contains information on the following topics:

- [Library with PLC data types (S7-1500)](#library-with-plc-data-types-s7-1500-5)
- [Assignment of the control interface (S7-1500)](#assignment-of-the-control-interface-s7-1500-5)
- [Assignment of the feedback interface (S7-1500)](#assignment-of-the-feedback-interface-s7-1500-5)

#### Library with PLC data types (S7-1500)

> **Note**
>
> A library of PLC data types (LPD) for STEP 7 (TIA Portal) and SIMATIC S7-1200 / S7-1500 is available for download on the [Internet](https://support.industry.siemens.com/cs/ww/en/view/109482396).

#### Assignment of the control interface (S7-1500)

The user program uses the control interface to influence the behavior of the technology module.

##### Control interface per channel

The following table shows the control interface assignment:

| Byte offset relative to start address Channel 0/1 **↓ ↓** |  | Bit 7 | Bit 6 | Bit 5 | Bit 4 | Bit 3 | Bit 2 | Bit 1 | Bit 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 … 3 | 12 … 15 | OUTPUT_VALUE  DINT: Duty cycle in the S7 analog format |  |  |  |  |  |  |  |
| 4 … 7 | 16 … 19 | SLOT  UDINT: Load value |  |  |  |  |  |  |  |
| 8 | 20 | Reserved |  |  | MODE_ SLOT | LD_SLOT |  |  |  |
| 9 | 21 | Reserved |  |  |  |  |  |  | SW_ ENABLE |
| 10 | 22 | Reserved |  |  |  |  |  |  | RES_ ERROR |
| 11 | 23 | Reserved |  |  |  |  |  |  |  |

> **Note**
>
> Channel 1 is only available in two-channel operation of the module.

| Control bit/value | Explanations |
| --- | --- |
| OUTPUT_VALUE | You specify the duty cycle with this value.  Value range:  - Duty cycle: -27648 to 27648<sub>D</sub>:   If the low limit or the high limit is violated, the feedback bit ERR_OUT_VAL is set and the minimum or maximum value is used. |
| SLOT | You specify the load value with this value.  Value range:   - Period duration in μs: 100 to 85000000<sub>D</sub> - On delay in μs: 0 to 85000000<sub>D</sub>   You specify whether to apply a change once or cyclically with MODE_SLOT.  Invalid values trigger setting of feedback bit ERR_LD (when MODE_SLOT = 0) or ERR_SLOT_VAL (when MODE_SLOT = 1). |
| MODE_SLOT | You specify whether you want to apply a change in SLOT once or cyclically with this bit.  0 means: As soon as you write the respective value in the corresponding output byte, the value from SLOT is applied once and kept until the next change. A change of the On delay via SLOT takes effect at the next output sequence. A change of the period duration via SLOT takes effect at DQn.A/DQn.B with the next rising edge. After a restart of the module, the value is overwritten with the value set in the hardware configuration.   1 means: When you write the respective value in the corresponding output byte, the current value from SLOT in each case is applied cyclically. A change of the On delay via SLOT takes effect at the next output sequence. A change of the period duration via SLOT takes effect at DQn.A/DQn.B with the next rising edge. |
| LD_SLOT | You specify the meaning of the value in SLOT with this load request:  - 0000<sub>B</sub> means: No action, idle - 0001<sub>B</sub> means: Period duration in μs - 0010<sub>B</sub> means: On delay in μs   Values not listed are invalid and trigger setting of feedback bit ERR_LD (when MODE_SLOT = 0) or ERR_SLOT_VAL (when MODE_SLOT = 1). |
| SW_ENABLE | You activate the software enable with this bit. If you are using the hardware enable, it is combined with the software enable.  - 0 means: Stop output - 1 means: Start output   Use of the HW enable is activated through parameter assignment. The HW enable is controlled externally using the digital input DIn.0. |
| RES_ERROR | You use this bit to reset the following feedback bits when errors are pending:  - ERR_24V - ERR_DQA - ERR_DQB - ERR_LD |
| Reserved | Reserved bits must be set to 0. |

#### Assignment of the feedback interface (S7-1500)

The user program receives current values and status information from the technology module via the feedback interface.

##### Feedback interface per channel

The following table shows the assignment of the feedback interface:

| Byte offset relative to start address Channel 0/1 **↓ ↓** |  | Bit 7 | Bit 6 | Bit 5 | Bit 4 | Bit 3 | Bit 2 | Bit 1 | Bit 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 8 | ERR_ SLOT_VAL | ERR_ OUT_VAL | ERR_DQB | ERR_DQA | Reserved | ERR_LD | ERR_24V | ERR_PWR |
| 1 | 9 | Reserved |  | STS_SW_ ENABLE | STS_ READY | Reserved | STS_LD_ SLOT | Reserved |  |
| 2 | 10 | Reserved |  |  |  | STS_DI | STS_DQB | STS_DQA | STS_ ENABLE |
| 3 ... 7 | 11 ... 15 | Reserved |  |  |  |  |  |  |  |

> **Note**
>
> Channel 1 is only available in two-channel operation of the module.

| Feedback bit/value | Explanations |
| --- | --- |
| ERR_SLOT_VAL | This bit indicates that the value in SLOT or LD_SLOT is invalid (when MODE_SLOT = 1) and was not accepted.   As soon as the module has received a valid value from the control interface, ERR_SLOT_VAL is automatically reset. |
| ERR_OUT_VAL | This bit indicates that the value in OUTPUT_VALUE is invalid.  As soon as the module has received a valid value from the control interface, ERR_OUT_VAL is automatically reset. |
| ERR_DQA | This bit indicates a short-circuit or an overload at the output DQn.A. If you have enabled the diagnostics interrupt "Diagnostics DQA", the diagnostics interrupt "Error at digital outputs" is triggered when this error occurs.   The bit is reset once you have acknowledged the error with RES_ERROR. |
| ERR_DQB | This bit indicates a short-circuit or an overload at the output DQn.B or the attempted simultaneous setting of the SET_DQA and SET_DQB control bits. If you have enabled the diagnostics interrupt "Diagnostics DQB", the diagnostics interrupt "Error at digital outputs" is triggered when this error occurs.   The bit is reset once you have acknowledged the error with RES_ERROR. |
| ERR_LD | This bit indicates that the value in SLOT or LD_SLOT (when MODE_SLOT = 0) is invalid and was not accepted.   The bit is reset once you have acknowledged the error with RES_ERROR. |
| ERR_24V | This bit indicates a short-circuit or an overload at output 24VDC If you have enabled diagnostic interrupts, the diagnostic interrupt "Short circuit / overload of the sensor supply voltage" is triggered when this error occurs.   The bit is reset once you have acknowledged the error with RES_ERROR. |
| ERR_PWR | This bit indicates that supply voltage L+ is too low. If you have enabled the diagnostic interrupts, the diagnostic interrupt "Supply voltage fault" is triggered when an error occurs.   As soon as supply voltage L+ is sufficiently high again, ERR_PWR is automatically reset.  The bit is not set if no supply voltage is present. |
| STS_SW_ENABLE | This bit indicates the status of the SW enable.   - 0 means: SW enable not active - 1 means: SW enable active |
| STS_READY | This bit indicates that the module is supplying valid user data. The module is started and configured. |
| STS_LD_SLOT | A status change (toggling) of this bit indicates that the LD_SLOT load request was detected and executed (when MODE_SLOT = 0). |
| STS_DI | This bit indicates the status of the digital input DIn.0. |
| STS_DQA | This bit indicates the status of the digital output DQn.A. |
| STS_DQB | This bit indicates the status of the digital output DQn.B. |
| STS_ENABLE | This bit indicates that an output sequence is active. |
| Reserved | Reserved bits are set to 0. |

### Isochronous mode (S7-1500)

The technology module supports the "Isochronous mode" system function. In isochronous mode, the output sequence starts at time T<sub>o</sub> after the SW_ENABLE control bit has been set. The period duration is also adapted to the application cycle (T<sub>APP</sub>) and synchronized with it. The synchronization is especially advantageous for setting up control loops.

The module adjusts the assigned value of the period duration in such a way that an integer ratio results. In the most unfavorable case, the difference amounts to half the application cycle.

Examples:

| Application cycle T<sub>APP</sub> | Assigned period duration T<sub>Setpoint</sub> | Actual period durationT<sub>Actual</sub> | T<sub>APP</sub>:T<sub>Actual</sub> |
| --- | --- | --- | --- |
| 10 ms  (10000 μs) | 1800 μs | 1666 μs | 6:1 |
| 2000 μs | 2000 μs | 5:1 |  |
| 3000 μs | 3333 μs | 3:1 |  |
| 5000 μs | 5000 μs | 2:1 |  |
| 6000 μs | 5000 μs | 2:1 |  |
| 12000 μs | 10000 μs | 1:1 |  |
| 16000 μs | 20000 μs | 1:2 |  |

The figure below shows an example of a 1:1 ratio of application cycle to period duration with a duty cycle of 50%.

![Figure](images/116953289227_DV_resource.Stream@PNG-en-US.png)

The figure below shows an example of a 3:1 ratio of application cycle to period duration with a duty cycle of 50%.

![Figure](images/116953292811_DV_resource.Stream@PNG-en-US.png)

The figure below shows an example of a 1:3 ratio of application cycle to period duration with a duty cycle of 50%.

![Figure](images/116976349195_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> **No HW enable or On delay**
>
> No hardware enable or On delay can be used in isochronous mode.
>
> If you configure the hardware enable in isochronous mode, this is interpreted by the module as a limit switch.

#### Further information

You will find a detailed description of isochronous mode in:

- In the isochronous mode function manual as a download from the [Internet](https://support.industry.siemens.com/cs/ww/en/view/109755401).
- PROFINET with STEP 7 function manual available for download on the [Internet](https://support.industry.siemens.com/cs/ww/en/view/49948856).

## Parallel connection of channels (S7-1500)

When the two channels are connected in parallel, you get a logical channel with an output current of up to 4 A.

The figure below shows two-channel operation in which the channels operate independent of each other and are separately configured.

![Two-channel operation](images/117801337739_DV_resource.Stream@PNG-en-US.png)

Two-channel operation

The figure below shows one-channel operation in which you only configure Channel 0.

![One-channel operation (parallel connection)](images/117801342347_DV_resource.Stream@PNG-en-US.png)

One-channel operation (parallel connection)

The following table presents the possible load current depending on whether or not the high-speed output is activated:

|  | Maximum output current |  |
| --- | --- | --- |
| High-speed output deactivated | High-speed output activated |  |
| Two-channel operation | 2 A | 100 mA |
| One-channel mode | 4 A | Not permitted |

You configure the function in the hardware configuration using the "Channel configuration" parameter.

## Direct control of digital outputs (S7-1500)

### Controlling of the output sequence by the user program or module

You define how DQn.A and DQn.B are controlled using the TM_CTRL_DQ control bit:

| TM_CTRL_DQ = 0 | TM_CTRL_DQ = 1 |
| --- | --- |
| You define the states of outputs DQn.A and DQn.B with the user program using the SET_DQA and SET_DQB control bits. | The output sequence of the configured operating mode defines the state of outputs DQn.A and DQn.B. |

> **Note**
>
> **No direct control available when using PWM with DC motor**
>
> In "PWM with DC motor" mode, the TM_CTRL_DQ, SET_DQA and SET_DQB control bits have no effect.

### Pulse diagram

An active output sequence is not aborted by the setting of TM_CTRL_DQ. The module initiates the output sequences internally regardless of the state of TM_CTRL_DQ.

The following figure shows an example of an output sequence for direct control of DQn.A:

![Example of an output sequence for direct control of DQn.A (Pulse output mode)](images/119765622283_DV_resource.Stream@PNG-en-US.png)

Example of an output sequence for direct control of DQn.A (Pulse output mode)

> **Note**
>
> If you set the SET_DQA and SET_DQB control bits simultaneously, the ERR_DQB bit is set in the feedback interface and only the digital output DQn.A is set.
>
> The ERR_DQB bit is reset once you have acknowledged the error by setting RES_ERROR.

## Handling of the SLOT parameters (S7-1500)

In addition to the main setpoint OUTPUT_VALUE, you can change a setpoint for another parameter.

You specify the load value with the SLOT value in the control interface. You use the LD_SLOT load request to specify the meaning of the value in SLOT depending on the operating mode:

| LD_SLOT | Meaning of the value in SLOT | Operating modes for use of the value | Data type of SLOT |
| --- | --- | --- | --- |
| 0<sub>D</sub> | No action, idle | All operating modes | — |
| 1<sub>D</sub> | Period duration | - Pulse width modulation PWM - Pulse train - PWM with DC motor | UDINT |
| 2<sub>D</sub> | On delay | - Pulse output - Pulse width modulation PWM - Pulse train - Frequency output - PWM with DC motor |  |
| 3<sub>D</sub> | Off delay | - On/Off delay |  |
| 4<sub>D</sub> | Duty cycle | - Pulse train |  |
| 5<sub>D</sub> | Dithering ramp up,  ramp down | - Pulse width modulation PWM | 2 × INT |
| 6<sub>D</sub> | Dithering amplitude | - Pulse width modulation PWM | UDINT |
| 7<sub>D</sub> | Dithering period duration | - Pulse width modulation PWM |  |

In so doing, you use the MODE_SLOT control bit to choose whether you want to apply a change of the respective value once or cyclically.

### MODE_SLOT

**One-time change (MODE_SLOT = 0)**

A one-time change is recommended when another parameter besides OUTPUT_VALUE must be changed occasionally. The module is not reset in this case. By contrast, if the change is made by transferring a new parameter data record, the module is reset.

The following parameters are used in the case of the one-time change:

| Symbol | Meaning |
| --- | --- |
| Control Parameters | - SLOT - LD_SLOT - MODE_SLOT - RES_ERROR |
| Feedback Parameters | - STS_LD_SLOT - ERR_LD |

To make a one-time change, follow these steps:

1. Check if the previous job was successfully performed, which means whether STS_LD_SLOT has changed and ERR_LD is not set.
2. If ERR_LD is set:

   - Write LD_SLOT = 0 and acknowledge the error by setting RES_ERROR. Continue with step 1.  
     or
   - Write a valid value in SLOT and LD_SLOT and acknowledge the error by setting RES_ERROR. Continue with step 1.
3. Enter a new value in SLOT.
4. Enter a changed value in LD_SLOT.

   > **Note**
   >
   > In the case of a one-time change, it is assumed that, in contrast to the cyclic change, the same parameter is not changed twice in succession. If you want to change the same parameter twice in succession, you must insert an "Idle job" (LD_SLOT = 0) between both jobs.
5. Continue with step 1.

   > **Note**
   >
   > The procedure is also shown in detail in a diagram in the appendix.

> **Note**
>
> After a restart of the module, the value of the parameter concerned is overwritten in the module-internal data record with the value set in the hardware configuration.

**Cyclic change (MODE_SLOT = 1)**

A cyclic change is recommended when another parameter besides OUTPUT_VALUE is to be cyclically changed.

> **Note**
>
> You can stop the cyclic change during the output sequence by setting LD_SLOT and MODE_SLOT to 0. The values changed up to that point are retained.

**Flowchart**

The following figure shows an example of the basic sequence:

![MODE_SLOT](images/123230250123_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| 1a | You write a valid value in SLOT and LD_SLOT. |
| 1b | The STS_LD_SLOT feedback bit is toggled because the LD_SLOT load request was recognized by the module and implemented. The value from SLOT is applied once and kept until the next change of LD_SLOT. The relevant parameter is updated in the module-internal data record and takes effect at the next output sequence. |
| 2a | You write a changed and valid value in LD_SLOT and an invalid value in SLOT. |
| 2b | The ERR_SLOT_LD feedback bit is set because the value in SLOT is invalid. The value is not applied. |
| 2c | You set the RES_ERROR control bit in order to acknowledge the error. |
| 2d | The feedback bit ERR_LD is reset. |
| 2e | You reset the RES_ERROR control bit. |
| 3a | You write a changed and valid value in SLOT and LD_SLOT. |
| 3b | The STS_LD_SLOT feedback bit is toggled because the LD_SLOT load request was recognized by the module and implemented. The value from SLOT is applied once and kept until the next change of LD_SLOT. The relevant parameter is updated in the module-internal data record and takes effect at the next output sequence. |
| 4a | You set MODE_SLOT and cyclically write valid values ​​in SLOT and LD_SLOT. The value from SLOT is cyclically applied and takes effect at the next output sequence. However, the respective change is not saved. |
| 4b | You cyclically write invalid values ​​in SLOT. |
| 4c | The ERR_SLOT_VAL feedback bit is set because the value in SLOT is invalid. The respective value from SLOT is not applied. |
| 4d | You cyclically write valid values ​​in SLOT. |
| 4e | The ERR_SLOT_VAL feedback bit is automatically reset because the module has again received valid values. |

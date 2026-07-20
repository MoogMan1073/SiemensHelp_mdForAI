---
title: "Using ET 200S 2PULSE (S7-300, S7-400)"
package: TFHWC2PULSEenUS
topics: 59
devices: [S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Using ET 200S 2PULSE (S7-300, S7-400)

This section contains information on the following topics:

- [2PULSE terminal assignment (S7-300, S7-400)](#2pulse-terminal-assignment-s7-300-s7-400)
- [Operating modes and functions (S7-300, S7-400)](#operating-modes-and-functions-s7-300-s7-400)
- [Configuring and assigning parameters to 2PULSE (S7-300, S7-400)](#configuring-and-assigning-parameters-to-2pulse-s7-300-s7-400)
- [2PULSE diagnostics (S7-300, S7-400)](#2pulse-diagnostics-s7-300-s7-400)

## 2PULSE terminal assignment (S7-300, S7-400)

### Wiring Rules

The cables (terminals 1 and 2 and terminals 5 and 6) must be shielded. The shield must be supported at both ends. To do this, use the shield contact (see the appendix of the [ET 200S Distributed I/O System](http://support.automation.siemens.com/WW/view/en/1144348) operating instructions).

### Terminal assignment of the 2PULSE

The following table shows the terminal assignment for 2PULSE.

| View | Terminal Assignment | Meaning |
| --- | --- | --- |
| ![Terminal assignment of the 2PULSE](images/22645720971_DV_resource.Stream@PNG-en-US.png) |  | Channel 0: Terminal 1 to 4  Channel 1: Terminal 5 to 8  24V DC: Encoder supply  M: Chassis ground  DI: Input Signal  DO: Output signal (max. 2 A per channel) |

## Operating modes and functions (S7-300, S7-400)

This section contains information on the following topics:

- [Overview (S7-300, S7-400)](#overview-s7-300-s7-400)
- ["Pulse output" operating mode (S7-300, S7-400)](#pulse-output-operating-mode-s7-300-s7-400)
- ["Pulse width modulation" operating mode (S7-300, S7-400)](#pulse-width-modulation-operating-mode-s7-300-s7-400)
- ["Pulse train" operating mode (S7-300, S7-400)](#pulse-train-operating-mode-s7-300-s7-400)
- ["On/Off-delay" operating mode (S7-300, S7-400)](#onoff-delay-operating-mode-s7-300-s7-400)
- ["Frequency output" mode (as of 6ES7138-4DD01-0AB0) (S7-300, S7-400)](#frequency-output-mode-as-of-6es7138-4dd01-0ab0-s7-300-s7-400)
- [Sequence counter (as of 6ES7138-4DD01-0AB0) (S7-300, S7-400)](#sequence-counter-as-of-6es7138-4dd01-0ab0-s7-300-s7-400)
- [Function: Current measurement (as of 6ES7138-4DD01-0AB0) (S7-300, S7-400)](#function-current-measurement-as-of-6es7138-4dd01-0ab0-s7-300-s7-400)
- [Function: Direct control of the digital output DO (S7-300, S7-400)](#function-direct-control-of-the-digital-output-do-s7-300-s7-400)
- [Function: Error detection / diagnostics (S7-300, S7-400)](#function-error-detection-diagnostics-s7-300-s7-400)
- [Parallel connection of both channels (as of 6ES7138-4DD01-0AB0) (S7-300, S7-400)](#parallel-connection-of-both-channels-as-of-6es7138-4dd01-0ab0-s7-300-s7-400)
- [Reaction to CPU/Master STOP (S7-300, S7-400)](#reaction-to-cpumaster-stop-s7-300-s7-400)

### Overview (S7-300, S7-400)

#### Principle

The 2PULSE has two channels. You can select a separate mode for each channel. The operating mode is specified during the configuration. The mode that has been assigned parameters can then no longer be changed with your control program.

You can select various modes for each channel:

- [Pulse output](#pulse-output-operating-mode-s7-300-s7-400)
- [Pulse width modulation](#pulse-width-modulation-operating-mode-s7-300-s7-400)
- [Pulse train](#pulse-train-operating-mode-s7-300-s7-400)
- [On/Off delay](#onoff-delay-operating-mode-s7-300-s7-400)
- [Frequency output](#frequency-output-mode-as-of-6es7138-4dd01-0ab0-s7-300-s7-400) (as of 6ES7138‑4DD01‑0AB0)

In addition to the set mode, the 2PULSE also has the following functions:

- [Current measurement](#function-current-measurement-as-of-6es7138-4dd01-0ab0-s7-300-s7-400) in the "Pulse width modulation" and "Pulse train" modes (as of 6ES7138‑4DD01‑0AB0)
- [Direct control of the DO digital output](#function-direct-control-of-the-digital-output-do-s7-300-s7-400) by means of your control program; can be controlled separately for each channel.
- [Error detection/diagnostics](#function-error-detection-diagnostics-s7-300-s7-400); the 2PULSE recognizes the errors for each channel separately.
- [Parallel connection of both channels](#parallel-connection-of-both-channels-as-of-6es7138-4dd01-0ab0-s7-300-s7-400) to achieve a higher output current (as of 6ES7138‑4DD01‑0AB0).
- [Reaction to CPU/Master STOP](#reaction-to-cpumaster-stop-s7-300-s7-400); the 2PULSE recognizes the CPU/Master STOP for both channels and responds in accordance with your parameter assignment.

The following figure shows the operating principle of the 2PULSE.

![Principle](images/23576074635_DV_resource.Stream@PNG-en-US.png)

#### Interfaces to the Control Program and Process

To run the modes and execute functions, the 2PULSE has as an interface to the process of a digital input and a digital output for each channel (DI 0, DO 0 for Channel 0 and DI 1, DO1 for Channel 1).

You can modify and monitor the modes and functions with your control program using [control signals](#2pulse-control-assignment-s7-300-s7-400) and [feedback signals](#2pulse-feedback-interface-s7-300-s7-400).

Parameters are assigned to the various modes.

You will find the following in the descriptions on operating modes and functions:

- The relevant parameters
- The control and feedback signals

The description of the modes and functions applies to both channels and the channels are therefore not referred to separately in the description.

### "Pulse output" operating mode (S7-300, S7-400)

This section contains information on the following topics:

- ["Pulse output" operating mode (S7-300, S7-400)](#pulse-output-operating-mode-s7-300-s7-400-1)
- [Parameters of the "Pulse output" operating mode (S7-300, S7-400)](#parameters-of-the-pulse-output-operating-mode-s7-300-s7-400)
- [Control and feedback signals of the "Pulse output" operating mode (S7-300, S7-400)](#control-and-feedback-signals-of-the-pulse-output-operating-mode-s7-300-s7-400)
- [Input and output signals of "Pulse output" operating mode (S7-300, S7-400)](#input-and-output-signals-of-pulse-output-operating-mode-s7-300-s7-400)

#### "Pulse output" operating mode (S7-300, S7-400)

##### Pulse output

For the pulse duration you set, the 2PULSE outputs a pulse at the DO digital output (output sequence) on expiration of the set [on-delay](#specifying-on-delay-s7-300-s7-400).

The following figure shows the block diagram for the operating mode "Pulse output".

![Pulse output](images/28155405835_DV_resource.Stream@PNG-en-US.png)

##### Starting the output sequence

You must always issue the enable for the output sequence by means of the [software enable](#2pulse-control-assignment-s7-300-s7-400) (SW_ENABLE 0 → 1; MANUAL_DO = 0) in your control program.

The [feedback bit](#2pulse-feedback-interface-s7-300-s7-400)ACK_SW_ENABLE indicates the software enable pending at the 2PULSE.

You can also set the DI digital input of the 2PULSE as a hardware enable (HW enable) with the "[DI function](#selecting-di-function-s7-300-s7-400)" parameter.

If you want to work with the software enable and hardware enable at the same time, when the software enable has been issued, the output sequence starts at the first positive edge of the hardware enable. Further positive edges of the hardware enable during the current output sequence are ignored by the 2PULSE. When the software enable has been issued, a positive edge of the hardware enable is enough to start the next output sequence.

When the enable is issued (positive edge), the on-delay is started and the STS_ENABLE set. On expiration of the on-delay, the pulse is output with the set pulse duration. The [output sequence](#sequence-counter-as-of-6es7138-4dd01-0ab0-s7-300-s7-400) finishes with the end of the pulse; STS_ENABLE is cleared.

If you make a prohibited change to the pulse duration during runtime, the [signal](#2pulse-feedback-interface-s7-300-s7-400)ERR_PULS indicates a pulse output error. You will then have to restart the output sequence.

The next time the output sequence starts, the 2PULSE deletes the ERR_PULS feedback bit.

##### Pulse Diagram

The following figure shows an output sequence for the operating mode "Pulse output".

![Pulse Diagram](images/28155755659_DV_resource.Stream@PNG-en-US.png)

##### Canceling the output sequence

Deleting the software enable (SW_ENABLE = 0) during the on-delay or the pulse output cancels the output sequence, and STS_ENABLE and the DO digital output are canceled.

You will then have to restart the output sequence.

##### Truth table

The table below shows how the 2PULSE responds to certain signals.

| Software enable SW_ENABLE | Hardware enable (digital input DI) | DO Digital Output | STS_ENABLE | Output Sequence |
| --- | --- | --- | --- | --- |
| 1 | 0 → 1 | 0, if on-delay &gt; 0 1, if on-delay = 0 | 0 → 1 | Start |
| 0 → 1 | Not used | 0, if on-delay &gt; 0 1, if on-delay = 0 | 0 → 1 | Starting |
| 0 | Any status | 0 | 0 | Terminate |
| 1 | Any status | Previous status remains |  | - |
| 0 → 1 | 0 | 0 | 0 | - |

##### Setting Times Using a Time Base

By means of the [time base](#selecting-a-time-base-s7-300-s7-400) that can be assigned parameters, you can select the resolution and range of the pulse duration and the on-delay.

| Symbol | Meaning |
| --- | --- |
| Time base = 0.1 ms: | You can set times from 0.2 ms to 6.5535 s with a resolution of 0.1 ms. |
| Time base = 1 ms: | You can set times from 1 ms to 65.535 s with a resolution of 1 ms. |

##### Setting and Changing the Pulse Duration

Set the [pulse duration](#specifying-pulse-duration-s7-300-s7-400) directly in your control program as a numerical value between 0 and 65535.

Pulse duration = Time basis x Specified numerical value

If you change the pulse duration when an output sequence is running, the time already output will be subtracted from the new pulse duration and the pulse will continue to be output.

##### Reducing the Pulse Duration

If you have reduced the pulse duration to a time that is shorter than the time already output, the output sequence is terminated, STS_ENABLE and the DO digital output are deleted, and the ERR_PULS status bit is set. At the next output sequence, the ERR_PULS status bit is cleared.

##### Set the on-delay and change when using the short control interface

You specify the [on-delay](#specifying-on-delay-s7-300-s7-400) as a value between 0 and 65535 in the parameters.

Configured on-delay = Time base x specified numerical value

Using the factor for the on-delay, you can adjust the time that has been assigned parameters in your control program. Set the factor between 0 and 255, with a weighting of 0.1:

On-delay = Factor x 0.1 x configured on-delay

If you change the on-delay factor during the output sequence, the new on-delay is activated at the next output sequence.

##### Isochronous mode (as of 6ES7138‑4DD01‑0AB0)

In the "Pulse output" operating mode, isochronous mode does not have any influence on the functionality.

#### Parameters of the "Pulse output" operating mode (S7-300, S7-400)

##### Parameters of the "Pulse output" operating mode

The table below shows the parameters of the operating mode "Pulse output".

| Parameter | Meaning | Value range | Default |
| --- | --- | --- | --- |
| [Operating mode](#selecting-an-operating-mode-s7-300-s7-400-1) | Set the "Pulse output" operating mode. | - Pulse output - Pulse width modulation - Pulse train - On/Off-delay - Frequency output | Pulse width modulation |
| [Time base](#selecting-a-time-base-s7-300-s7-400) | Using the time base, select the resolution and range of the pulse duration and the on-delay. | - 0.1 ms - 1 ms | 0.1 ms |
| [Function DI](#selecting-di-function-s7-300-s7-400) | You can use the DI digital input as an input or as a hardware enable. | - Input - HW enable | Input |
| [On-delay](#specifying-on-delay-s7-300-s7-400) <sup>1)</sup> | The time from the start of the output sequence to the output of the pulse. You can change the on-delay in your control program using the "On-delay factor". | 0 to 65535 | 0 |
| <sup>1)</sup> Only if the short [control interface](#2pulse-control-assignment-s7-300-s7-400) is used If the long control interface is used, enter this value directly in the control interface. |  |  |  |

#### Control and feedback signals of the "Pulse output" operating mode (S7-300, S7-400)

##### Control and feedback signals of the "Pulse output" operating mode

The table below shows the control and feedback signals of the operating mode "Pulse output".

| Control and feedback signals | Meaning | Value range | Channel 0 address | Channel 1 address |
| --- | --- | --- | --- | --- |
| **Control signals when the short control interface is used (8 bytes)** |  |  |  |  |
| Software enable SW_ENABLE | Starting and canceling of the output sequence. | 0 = SW_ENABLE canceled 1 = SW_ENABLE set 0→1 = start of output sequence; may be dependent on the hardware enable | Byte 2:  Bit 0 | Byte 6:  Bit 0 |
| Pulse duration | The time that is set for the DO digital output on expiration of the on-delay. | With time base 0.1 ms: 2 to 65535  With time base 1 ms: 1 to 65535  If you violate the low limit of the range, the 2PULSE will not output a pulse. | Word 0 | Word 4 |
| On-delay factor | The on-delay that has been assigned parameters can be changed before the start of the output sequence:  On-delay = Factor x 0.1 x configured on-delay | 0 to 255  If the on-delay &lt;0.2 ms or if factor = 0, the effective on-delay is = 0. If there is an on-delay &gt; 65.535 s, the on-delay is limited to 65.535 s. | Byte 3 | Byte 7 |
| **Control signals when the long control interface is used (12 bytes) (as of**  **6ES7138‑4DD01‑0AB0** **)** |  |  |  |  |
| Software enable (SW_ENABLE) | Starting and canceling of the output sequence. | 0 = SW_ENABLE canceled 1 = SW_ENABLE set 0→1 = start of output sequence; may be dependent on the hardware enable | Byte 4:  Bit 0 | Byte 10:  Bit 0 |
| Pulse duration | The time that is set for the DO digital output on expiration of the on-delay. | With time base 0.1 ms: 2 to 65535  With time base 1 ms: 1 to 65535  If you violate the low limit of the range, the 2PULSE will not output a pulse. | Word 0 | Word 6 |
| On-delay | The on-delay can be changed before the start of the output sequence. | 0 to 65535  On-delay = Time basis x Specified numerical value | Word 2 | Word 8 |
| **Feedback signals** |  |  |  |  |
| STS_ENABLE | Indicates an output sequence is running. | 0 = Pulse output blocked  1 = Pulse output running | Byte 0:  Bit 0 | Byte 4:  Bit 0 |
| STS_DO | Indicates the signal level at the digital output DO. Note the update rate. | 0 = Signal 0 on digital output DO  1 = Signal 1 on digital output DO | Byte 0:  Bit 1 | Byte 4:  Bit 1 |
| STS_DI | Indicates the signal level at digital input DI. | 0 = Signal 0 on digital input DI  1 = Signal 1 on digital input DI | Byte 0:  Bit 2 | Byte 4:  Bit 2 |
| ACK_SW_ENABLE | Indicates the status of SW_ENABLE. | 0 = SW_ENABLE cleared.  1 = SW_ENABLE set | Byte 0:  Bit 3 | Byte 4:  Bit 3 |
| ERR_PULS | Indicates a pulse output error. | 0 = no pulse output error  1 = pulse output error | Byte 0:  Bit 4 | Byte 4:  Bit 4 |
| SEQ_CNT (as of 6ES7138‑4DD01‑0AB0) | Is incremented after completion of an output sequence. | Without HW enable: 0 … 1  With HW enable: 0 … 15 | Byte 1:  Bit 0 to 3 | Byte 5:  Bit 0 … 3 |
| Reserved | – | 0 | Word 2 | Word 6 |

#### Input and output signals of "Pulse output" operating mode (S7-300, S7-400)

##### Input and output signals of "Pulse output" operating mode

The table below shows the input and output signals of the operating mode "Pulse output".

| Input and output signal | Meaning | Value range | Channel 0 terminal | Channel 1 terminal |
| --- | --- | --- | --- | --- |
| **Input signal** |  |  |  |  |
| HW enable | You can select the HW enable with the "Function DI" parameter. The signal of the digital input DI is then interpreted by the 2PULSE at the start of the output sequence. | 0 = HW enable cleared 1 = HW enable issued 0 → 1 = Start of the output sequence; dependent on the software enable (SW_ENABLE) | 1 | 5 |
| **Output signal** |  |  |  |  |
| Pulse at the DO digital output | A pulse is output at the DO digital output for the set pulse duration. | 0 = no pulse  1 = pulse | 4 | 8 |

### "Pulse width modulation" operating mode (S7-300, S7-400)

This section contains information on the following topics:

- ["Pulse width modulation" operating mode (S7-300, S7-400)](#pulse-width-modulation-operating-mode-s7-300-s7-400-1)
- [Isochronous mode in the operating mode "Pulse width modulation" (S7-300, S7-400)](#isochronous-mode-in-the-operating-mode-pulse-width-modulation-s7-300-s7-400)
- [Parameters of the "Pulse width modulation" operating mode (S7-300, S7-400)](#parameters-of-the-pulse-width-modulation-operating-mode-s7-300-s7-400)
- [Control and feedback signals of the "Pulse width modulation" operating mode (S7-300, S7-400)](#control-and-feedback-signals-of-the-pulse-width-modulation-operating-mode-s7-300-s7-400)
- [Input and output signals of the "Pulse width modulation" operating mode (S7-300, S7-400)](#input-and-output-signals-of-the-pulse-width-modulation-operating-mode-s7-300-s7-400)

#### "Pulse width modulation" operating mode (S7-300, S7-400)

##### Pulse width modulation

You specify an output value for the 2PULSE. The 2PULSE generates continuous pulses on this basis. The output value determines the pulse/interpulse ratio within a period (pulse-width modulation). The period can be adjusted.

The pulse train is output on expiration of the assigned [on-delay](#specifying-on-delay-s7-300-s7-400) on the DO digital output of the 2PULSE (output sequence).

The following figure shows the block diagram for the operating mode "Pulse-width modulation".

![Pulse width modulation](images/28155465483_DV_resource.Stream@PNG-en-US.png)

##### Starting the output sequence

You must always issue the enable for the output sequence by means of the [software enable](#2pulse-control-assignment-s7-300-s7-400) (SW_ENABLE 0 → 1; MANUAL_DO = 0) in your control program.

The [feedback bit](#2pulse-feedback-interface-s7-300-s7-400)ACK_SW_ENABLE indicates the software enable pending at the 2PULSE.

You can also set the digital input DI of the 2PULSE as a HW enable with the "[Function DI](#selecting-di-function-s7-300-s7-400)" parameter. In isochronous mode (as of 6ES7138‑4DD01‑0AB0), configuration of a hardware enable has no effect.

If you want to work with the software enable and hardware enable at the same time, when the software enable has been issued, the output sequence starts with the first positive edge of the hardware enable. Further positive edges of the hardware enable during the current output sequence are ignored by the 2PULSE.

When the enable is issued (positive edge), the on-delay is started and the STS_ENABLE set. The pulse train is output on expiration of the on-delay. The output sequence runs continuously as long as SW_ENABLE is set.

##### Pulse Diagram

The following figure shows an output sequence for the operating mode "Pulse-width modulation".

![Pulse Diagram](images/28155528203_DV_resource.Stream@PNG-en-US.png)

##### Canceling the output sequence

Deleting the software enable (SW_ENABLE = 0) during the on-delay or the pulse output cancels the output sequence, and STS_ENABLE and the DO digital output are canceled.

You will then have to restart the output sequence.

##### Truth table

The table below shows how the 2PULSE responds to certain signals.

| Software enable SW_ENABLE | Hardware enable (digital input DI) | Digital output DO | STS_ENABLE | Output sequence |
| --- | --- | --- | --- | --- |
| 1 | 0 → 1 | 0, if on-delay &gt; 0 1, if on-delay = 0 | 0 → 1 | Starting |
| 0 → 1 | Not used | 0, if on-delay &gt; 0 1, if on-delay = 0 | 0 → 1 | Starting |
| 0 | Any status | 0 | 0 | Canceling |
| 1 | Any status | Previous status remains |  | - |
| 0 → 1 | 0 | 0 | 0 | - |

##### Minimum Pulse Duration and Minimum Interpulse Period

The minimum pulse duration and minimum interpulse period are superimposed on the proportional output characteristic.

You assign the minimum pulse duration and minimum interpulse period using the "[Minimum pulse duration](#specifying-minimum-pulse-duration-s7-300-s7-400)" parameter; they always have the same value.

A pulse duration calculated by the 2PULSE that is shorter than the minimum pulse duration is suppressed.

A pulse duration calculated by the 2PULSE that is longer than the period minus the minimum interpulse period is set at 1000‰.

The following figure shows the modulation of the pulse duration.

![Minimum Pulse Duration and Minimum Interpulse Period](images/23584341899_DV_resource.Stream@PNG-en-US.png)

##### Setting Times Using a Time Base

You use the assignable [time base](#selecting-a-time-base-s7-300-s7-400) to select the resolution and range of the period, the minimum pulse duration and the on-delay.

| Symbol | Meaning |
| --- | --- |
| Time base = 0.1 ms: | You can set times from 0.2 ms to 6.5535 s with a resolution of 0.1 ms. |
| Time base = 1 ms: | You can set times from 1 ms to 65.535 s with a resolution of 1 ms. |

##### Setting and Changing the Output Value

You select the range of the output value with the "[Output format](#selecting-the-output-format-s7-300-s7-400)" parameter.

- Output format "Per mill": Value range between 0 and 1000

  The 2PULSE uses this specified output value to calculate the pulse duration:

  Pulse duration = (output value/1000) x time period.
- "S7 analog output" output format: Value range between 0 and 27648

  The 2PULSE uses this specified output value to calculate the pulse duration:

  Pulse duration = (output value/27648) x time period.

You set the output value directly using your control program. The new output value is applied at the next rising edge of the output.

##### Setting the time period

Depending on the configuration, the time period is specified as a parameter value or in the control interface. The table below shows when a specific value is used.

For isochronous mode (as of 6ES7138‑4DD01‑0AB0), you have to specify the time period when parameters are assigned. In contrast to non-isochronous mode, you cannot change the time period later during runtime.

|  | Configuration with ... |  |
| --- | --- | --- |
| Short control interface | Long control interface |  |
| Isochronous mode | Time period = "Time period" parameter value  The value from the control interface is ignored. |  |
| Non-isochronous mode | Time period = "Time period" parameter value × "Time period factor" from control interface | Time period = "Time period" setpoint from control interface  The "Time period" parameter value is ignored. |

##### Time period at configuration with short control interface

You specify the [time period](#specifying-period-s7-300-s7-400) in the parameters as a numerical value depending on the time base:

- With time base 1 ms: from 1 to 65535
- With time base 0.1 ms: from 2 to 65535

Configured time period = Time base x specified numerical value

Using the factor for the period duration, you can adjust the time that has been assigned parameters in your control program. Set the factor between 0 and 255, with a weighting of 0.1:

Time period = Factor x 0.1 x configured time period

The new setpoints for the time period are applied with the next rising edge of the output.

> **Note**
>
> If the time period changes in runtime, a brief minor increase in the time period can result (approx. 10 µs).

> **Note**
>
> A change in the time period using the control interface has no effect in isochronous mode (as of 6ES7138‑4DD01‑0AB0).

##### Setting the Minimum Pulse Duration and Minimum Interpulse Period

You specify the minimum pulse duration and the minimum interpulse period as a numerical value between 0 and 65535 using the "[Minimum pulse duration](#specifying-minimum-pulse-duration-s7-300-s7-400)" parameter:

Configured minimum pulse duration/minimum pause between pulses = Time base x specified numerical value

##### Setting the On-Delay

You specify the [on-delay](#specifying-on-delay-s7-300-s7-400) as a value between 0 and 65535 in the parameters.

Configured on-delay = Time base x specified numerical value

When the long control interface is used, the factor for the on-delay can be used to adjust the configured time in your control program. Set the factor between 0 and 255, with a weighting of 0.1:

On-delay = Factor x 0.1 x configured on-delay

##### Current measurement (as of 6ES7138‑4DD01‑0AB0)

An important application for current measurement in the "Pulse width modulation" operating mode is the current regulation of a proportional valve. This allows you to compensate for thermal effects at the valve, for example.

Additional information is available under "[Function: Current measurement (as of 6ES7138-4DD01-0AB0)](#function-current-measurement-as-of-6es7138-4dd01-0ab0-s7-300-s7-400)".

#### Isochronous mode in the operating mode "Pulse width modulation" (S7-300, S7-400)

##### Isochronous mode

> **Note**
>
> Isochronous mode is available with 2PULSE as of article number 6ES7138‑4DD01‑0AB0.

The following particular aspects apply to isochronous mode in the "Pulse width modulation" operating mode:

- The output always begins without an on-delay, a configured on-delay is ignored.
- The output always begins after the software enable has been issued, a configured hardware enable is ignored.
- A change of the time period during runtime is not possible. Corresponding specifications via the control interface are ignored.

In isochronous mode, the output sequence is synchronized with the moment T<sub>o</sub>. The time period is coordinated to the DP cycle. It is possible that your defined time period cannot be implemented exactly.

The configured value of the time period is adjusted by the 2PULSE to the DP cycle based on a calculation algorithm. The calculation is performed to minimize the difference between the specified and calculated time period. In the most unfavorable case, the deviation amounts to half the DP cycle. The table below shows examples.

| DP cycle time T<sub>DP</sub><sup>1)</sup> | Specified time period T<sub>Setpoint</sub> | Calculated time period T<sub>Actual</sub><sup>1)</sup> |
| --- | --- | --- |
| 10 ms | 5 ms | 5 ms |
| 10 ms | 2 ms | 2 ms |
| 10 ms | 6 ms | 5 ms |
| 10 ms | 16 ms | 20 ms |
| <sup>1)</sup> The calculated time period and the DP cycle time always have an integer ratio. |  |  |

The correlation between the and the DP cycle is represented graphically below. The pulse-pause ratio is shown in the examples with 50% each. For additional information, refer to the [Isochronous Mode](http://support.automation.siemens.com/WW/view/en/15218045) function manual.

- The time period is equal to the DP cycle

  ![Isochronous mode](images/24634095115_DV_resource.Stream@PNG-en-US.png)
- The time period is less than the DP cycle

  ![Isochronous mode](images/24634111499_DV_resource.Stream@PNG-en-US.png)
- The time period is greater than the DP cycle

  ![Isochronous mode](images/24634127883_DV_resource.Stream@PNG-en-US.png)

#### Parameters of the "Pulse width modulation" operating mode (S7-300, S7-400)

##### Parameters of the "Pulse width modulation" operating mode

The table below shows the parameters of the operating mode "Pulse width modulation".

| Parameter | Meaning | Value Range | Default |
| --- | --- | --- | --- |
| [Operating mode](#selecting-an-operating-mode-s7-300-s7-400-1) | Set the "Pulse width modulation" operating mode. | - Pulse output - Pulse-width modulation - Pulse train - On/Off-delay - Frequency output | Pulse width modulation |
| [Time base](#selecting-a-time-base-s7-300-s7-400) | Use the time base to select the resolution and the value range of the time period, the minimum pulse duration, and the on-delay. | - 0.1 ms - 1 ms | 0.1 ms |
| [Output format](#selecting-the-output-format-s7-300-s7-400) | Choose between the Per mil, and the S7 analog output formats, depending on which output value resolution you need. | - Per mill - S7 analog output | Per mill |
| [Function DI](#selecting-di-function-s7-300-s7-400) | You can use the digital input DI as an input or as a HW enable. | - Input - HW enable | Input |
| [On-delay](#specifying-on-delay-s7-300-s7-400) | The time from the start of the output sequence to the output of the pulse train. | 0 to 65535 | 0 |
| [Minimum pulse duration](#specifying-minimum-pulse-duration-s7-300-s7-400) | Minimum pulse duration and minimum interpulse period:  Enter the response time of the actuator connected on your DO digital output. | 0 to 65535 | 0 |
| [Time period](#specifying-period-s7-300-s7-400) <sup>1)</sup> | Setpoint of the time period  When specifying the time period take into account the set minimum pulse duration and the response time of your actuator that is connected to the digital output DO.  When the short control interface is used, you can use the "Time period factor" to change the time period in your control program in non-isochronous mode. | With time base 0.1 ms: 2 to 65535  With time base 1 ms: 1 to 65535 | 20000 → 2 s |
| <sup>1)</sup> Read the information provided above on "[Setting the time period](#pulse-width-modulation-operating-mode-s7-300-s7-400-1)" and on "[Isochronous mode](#isochronous-mode-in-the-operating-mode-pulse-width-modulation-s7-300-s7-400)". |  |  |  |

#### Control and feedback signals of the "Pulse width modulation" operating mode (S7-300, S7-400)

##### Control and feedback signals of the "Pulse width modulation" operating mode

The table below shows the control and feedback signals of the operating mode "Pulse width modulation".

| Control and feedback signals | Meaning | Value range | Channel 0 address | Channel 1 address |
| --- | --- | --- | --- | --- |
| **Control signals when the short control interface is used (8 bytes)** |  |  |  |  |
| Software enable (SW_ENABLE) | Starting and canceling of the output sequence. | 0 = SW_ENABLE canceled 1 = SW_ENABLE set 0→1 = start of output sequence; may be dependent on the hardware enable | Byte 2:  Bit 0 | Byte 6:  Bit 0 |
| Output value | The value that is output in pulse-width modulated format on the digital output DO. | Depending on the output format:  - Per mill: 0 ... 1000 - S7 analog output: 0 to 27648   If you enter an output value &gt; 1000 or 27648, the 2PULSE limits this to 1000 or 27648. | Word 0 | Word 4 |
| Period duration factor | You can change the assigned period:  Time period = Factor x 0.1 x configured time period | Factor: 0 to 255   Period duration:  2 × Minimum pulse duration up to 65.635 s.  If a period duration of &lt; 2 x minimum pulse duration occurs or &lt; 2 µs or if Factor = 0, the effective period = 2 x minimum pulse duration, but at least 200 µs.   If there is a period &gt; 65.535 s, it is limited to 65.535 s. | Byte 3 | Byte 7 |
| **Control signals when the long control interface is used (12 bytes) (as of**  **6ES7138‑4DD01‑0AB0** **)** |  |  |  |  |
| Software enable (SW_ENABLE) | Starting and canceling of the output sequence. | 0 = SW_ENABLE canceled 1 = SW_ENABLE set 0→1 = start of output sequence; may be dependent on the hardware enable | Byte 4:  Bit 0 | Byte 10:  Bit 0 |
| Output value | The value that is output in pulse-width modulated format on the digital output DO. | Depending on the output format:  - Per mill: 0 ... 1000 - S7 analog output: 0 to 27648   If you enter an output value &gt; 1000 or 27648, the 2PULSE limits this to 1000 or 27648. | Word 0 | Word 6 |
| Time period <sup>1)</sup> | Setpoint of the time period in non-isochronous mode | With time base 0.1 ms: 2 to 65535  With time base 1 ms: 1 to 65535 | Word 2 | Word 8 |
| On-delay factor | The on-delay that has been assigned parameters can be changed before the start of the output sequence:  On-delay = Factor x 0.1 x configured on-delay | 0 to 255  If the on-delay &lt;0.2 ms or if factor = 0, the effective on-delay is = 0. If there is an on-delay &gt; 65.535 s, the on-delay is limited to 65.535 s. | Byte 5 | Byte 11 |
| **Feedback signals** |  |  |  |  |
| STS_ENABLE | Indicates an output sequence is running. | 0 = pulse output blocked  1 = pulse output running | Byte 0:  Bit 0 | Byte 4:  Bit 0 |
| STS_DO | Indicates the signal level at the digital output DO.  Note the update rate. | 0 = Signal 0 on digital output DO  1 = Signal 1 on digital output DO | Byte 0:  Bit 1 | Byte 4:  Bit 1 |
| STS_DI | Indicates the signal level at digital input DI. | 0 = Signal 0 on digital input DI  1 = Signal 1 on digital input DI | Byte 0:  Bit 2 | Byte 4:  Bit 2 |
| ACK_SW_ENABLE | Indicates the status of SW_ENABLE. | 0 = SW_ENABLE cleared.  1 = SW_ENABLE set | Byte 0:  Bit 3 | Byte 4:  Bit 3 |
| SEQ_CNT (as of 6ES7138‑4DD01‑0AB0) | No function in this operating mode. | – | Byte 1:  Bit 0 to 3 | Byte 5:  Bit 0 … 3 |
| Current measurement (as of 6ES7138‑4DD01‑0AB0) | Current at the DO as a SIMATIC S7 analog value. | 0 to 27648 (overrange up to 32767) | Word 2 | Word 6 |
| <sup>1)</sup> Read the information provided on "[Setting the time period](#pulse-width-modulation-operating-mode-s7-300-s7-400-1)". |  |  |  |  |

#### Input and output signals of the "Pulse width modulation" operating mode (S7-300, S7-400)

##### Input and output signals of the "Pulse width modulation" operating mode

The table below shows the input and output signals of the operating mode "Pulse width modulation".

| Input and Output Signals | Meaning | Value range | Channel 0 terminal | Channel 1 terminal |
| --- | --- | --- | --- | --- |
| **Input signal** |  |  |  |  |
| HW enable | You can select the HW enable with the "Function DI" parameter. The signal of the digital input DI is then interpreted by the 2PULSE at the start of the output sequence. | 0 = HW enable cleared 1 = HW enable issued 0 → 1 = Start of the output sequence; dependent on the software enable | 1 | 5 |
| **Output signal** |  |  |  |  |
| Pulse train on the digital output DO | The pulse train is output on the digital output DO. | 0 = no pulse  1 = pulse | 4 | 8 |

### "Pulse train" operating mode (S7-300, S7-400)

This section contains information on the following topics:

- ["Pulse train" operating mode (S7-300, S7-400)](#pulse-train-operating-mode-s7-300-s7-400-1)
- [Parameters of the "Pulse train" operating mode (S7-300, S7-400)](#parameters-of-the-pulse-train-operating-mode-s7-300-s7-400)
- [Control and feedback signals of the "Pulse train" operating mode (S7-300, S7-400)](#control-and-feedback-signals-of-the-pulse-train-operating-mode-s7-300-s7-400)
- [Input and output signals of "Pulse train" operating mode (S7-300, S7-400)](#input-and-output-signals-of-pulse-train-operating-mode-s7-300-s7-400)

#### "Pulse train" operating mode (S7-300, S7-400)

##### Definition

The 2PULSE outputs the number of pulses you specified as a pulse train at the DO digital output on expiration of the set [on-delay](#specifying-on-delay-s7-300-s7-400) (output sequence). The period duration and pulse duration of the pulses can be adjusted.

The following figure shows the block diagram for the operating mode "Pulse train".

![Definition](images/28155559179_DV_resource.Stream@PNG-en-US.png)

##### Starting the Output Sequence

You must always issue the enable for the output sequence by means of the [software enable](#2pulse-control-assignment-s7-300-s7-400) (SW_ENABLE 0 → 1; MANUAL_DO = 0) in your control program. The [feedback bit](#2pulse-feedback-interface-s7-300-s7-400)ACK_SW_ENABLE indicates the software enable pending at the 2PULSE.

You can also set the digital input DI of the 2PULSE as a HW enable with the "[Function DI](#selecting-di-function-s7-300-s7-400)" parameter.

If you want to work with the software enable and hardware enable at the same time, when the software enable has been issued, the output sequence starts with the first positive edge of the hardware enable. Further positive edges of the hardware enable during the current output sequence are ignored by the 2PULSE. When the software enable has been issued, a positive edge of the hardware enable is enough to start the next output sequence.

When the enable is issued (positive edge), the on-delay is started and the STS_ENABLE set. On expiration of the on-delay, the pulse train is output with the set number of pulses. The [output sequence](#sequence-counter-as-of-6es7138-4dd01-0ab0-s7-300-s7-400) finishes as soon as the last pulse has been output; STS_ENABLE is cleared.

If you make a prohibited change to the number of pulses during runtime, the [signal](#2pulse-feedback-interface-s7-300-s7-400)ERR_PULS indicates a pulse output error.

At the next output sequence, the 2PULSE deletes the ERR_PULS feedback bit.

##### Pulse diagram

The following figure shows an output sequence for the operating mode "Pulse train".

![Pulse diagram](images/28155628683_DV_resource.Stream@PNG-en-US.png)

##### Canceling the output sequence

Deleting the software enable during the on-delay or the pulse train terminates the output sequence, and STS_ENABLE and the DO digital output are deleted.

You will then have to restart the output sequence.

##### Truth table

The table below shows how the 2PULSE responds to certain signals.

| Software enable SW_ENABLE | Hardware enable (digital input DI) | Digital output DO | STS_ENABLE | Output sequence |
| --- | --- | --- | --- | --- |
| 1 | 0 → 1 | 0, if on-delay &gt; 0 1, if on-delay = 0 | 0 → 1 | Starting |
| 0 → 1 | Not used | 0, if on-delay &gt; 0 1, if on-delay = 0 | 0 → 1 | Starting |
| 0 | Any status | 0 | 0 | Canceling |
| 1 | Any status | Previous status remains |  | - |
| 0 → 1 | 0 | 0 | 0 | - |

##### Setting Times Using a Time Base

By means of the [time base](#selecting-a-time-base-s7-300-s7-400) that can be assigned parameters, you can select the resolution and range of the period, pulse duration and on-delay.

| Symbol | Meaning |
| --- | --- |
| Time base = 0.1 ms: | You can set times from 0.2 ms to 6.5535 s with a resolution of 0.1 ms. |
| Time base = 1 ms: | You can set times from 1 ms to 65.535 s with a resolution of 1 ms. |

##### Setting and Changing the Number of Pulses

Set the [number of pulses](#2pulse-control-assignment-s7-300-s7-400) directly as a numerical value between 0 and 65535 with your control program.

If you change the number of pulses on expiration of the on-delay, the new value takes effect immediately:

- If you have increased the number of pulses, the new, higher number of pulses is output.
- If you have reduced the number of pulses, and if the lower number of pulses has already been output, the output sequence is terminated, STS_ENABLE and the DO digital output are deleted, and ERR_PULS is set. At the next output sequence, ERR_PULS is cleared.

##### Set the time period and change when using the short control interface

Set the [period duration](#specifying-period-s7-300-s7-400) as a value between 2 and 65535 in the parameters:

Configured time period = Time base x specified numerical value

Using the factor for the period, you can adjust the assigned time in your control program. Set the factor between 0 and 255, with a weighting of 0.1:

Time period = Factor x 0.1 x configured time period

If you change the factor during the output sequence, the new period duration will take effect at the start of the next output sequence.

##### Setting the Pulse Duration

Set the [pulse duration](#specifying-pulse-duration-s7-300-s7-400) as a numerical value between 1 and 65535 with the "Pulse duration" parameter:

Configured pulse duration = Time base x Specified numerical value

When the long control interface is used, you can set the ratio of the pulse duration to the interpulse period:

Pulse-pause ratio = (Setpoint / 255) × time period

##### Setting the On-Delay

You specify the [on-delay](#specifying-on-delay-s7-300-s7-400) as a value between 0 and 65535 in the parameters.

Configured on-delay = Time base x specified numerical value

##### Isochronous mode (as of 6ES7138‑4DD01‑0AB0)

In the "Pulse train" operating mode, isochronous mode does not have any influence on the functionality.

##### Current measurement (as of 6ES7138‑4DD01‑0AB0)

Additional information is available under "[Function: Current measurement (as of 6ES7138-4DD01-0AB0)](#function-current-measurement-as-of-6es7138-4dd01-0ab0-s7-300-s7-400)".

#### Parameters of the "Pulse train" operating mode (S7-300, S7-400)

##### Parameters of the "Pulse train" operating mode

The table below shows the parameters of the operating mode "Pulse train".

| Parameter | Meaning | Value range | Default |
| --- | --- | --- | --- |
| [Operating mode](#selecting-an-operating-mode-s7-300-s7-400-1) | Set the "Pulse train" operating mode. | - Pulse output - Pulse width modulation - Pulse train - On/Off-delay - Frequency output | Pulse width modulation |
| [Time base](#selecting-a-time-base-s7-300-s7-400) | Using the time base, select the resolution and range of the period duration, pulse duration, and on-delay. | - 0.1 ms - 1 ms | 0.1 ms |
| [Function DI](#selecting-di-function-s7-300-s7-400) | You can use the digital input DI as an input or as a HW enable. | - Input - HW enable | Input |
| [On-delay](#specifying-on-delay-s7-300-s7-400) | The time from the start of the output sequence to the output of the pulse train. | 0 to 65535 | 0 |
| [Pulse duration](#specifying-pulse-duration-s7-300-s7-400) <sup>1)</sup> | Pulse duration:  Enter the response time of the actuator connected on your DO digital output. | With time base 0.1 ms: 2 to 65535  With time base 1 ms: 1 to 65535  If you violate the low limit of the range, the 2PULSE sets the pulse duration to 0.2 ms or 1 ms. | 10000 → 1 s |
| [Time period](#specifying-period-s7-300-s7-400) <sup>1)</sup> | The period duration should always be a multiple of the response time of the actuator connected to the DO digital output.  Define the period duration according to the required repetition rate of the pulses.  You can change the time period in your control program using the "Time period factor". | With time base 0.1 ms: 2 to 65535  With time base 1 ms: 1 to 65535 | 20000 → 2 s |
| <sup>1)</sup> Only if the short [control interface](#2pulse-control-assignment-s7-300-s7-400) is used If the long control interface is used, enter this value directly in the control interface. |  |  |  |

#### Control and feedback signals of the "Pulse train" operating mode (S7-300, S7-400)

##### Control and feedback signals of the "Pulse train" operating mode

The table below shows the control and feedback signals of the operating mode "Pulse train".

| Control and feedback signals | Meaning | Value range | Channel 0 address | Channel 1 address |
| --- | --- | --- | --- | --- |
| **Control signals when the short control interface is used (8 bytes)** |  |  |  |  |
| Software enable (SW_ENABLE) | Starting and canceling of the output sequence. | 0 = SW_ENABLE cleared.  1 = SW_ENABLE set  0 → 1 = Start of the output sequence; may be dependent on the HW enable | Byte 2:  Bit 0 | Byte 6:  Bit 0 |
| Number of pulses | Number of pulses that are output at the DO digital output on expiration of the on-delay. | 0 to 65535  If the number of pulses is 0, the 2PULSE does not output any pulses. The output sequence is terminated with ERR_PULS = 1. | Word 0 | Word 4 |
| Period duration factor | The on-delay that can be assigned parameters can be changed before the start of the output sequence:  Time period = Factor x 0.1 x configured time period | Factor: 0 to 255   Period duration:  &gt; Pulse duration up to 65.535 s  If there is a period duration &gt; 65.535 s, it is set to 65.535 s. If a period duration ≤ pulse duration, it is set to a pulse duration of + 0.2 ms (or pulse duration + 1 ms). | Byte 3 | Byte 7 |
| **Control signals when the long control interface is used (12 bytes) (as of**  **6ES7138‑4DD01‑0AB0** **)** |  |  |  |  |
| Software enable (SW_ENABLE) | Starting and canceling of the output sequence. | 0 = SW_ENABLE cleared.  1 = SW_ENABLE set  0 → 1 = Start of the output sequence; may be dependent on the HW enable | Byte 4:  Bit 0 | Byte 10:  Bit 0 |
| Number of pulses | Number of pulses that are output at the DO digital output on expiration of the on-delay. | 0 to 65535  If the number of pulses is 0, the 2PULSE does not output any pulses. The output sequence is terminated with ERR_PULS = 1. | Word 0 | Word 6 |
| Period duration | Setpoint of the time period | With time base 0.1 ms: 2 to 65535  With time base 1 ms: 1 to 65535 | Word 2 | Word 8 |
| Pulse-pause ratio | You can set the ratio of the pulse duration to the interpulse period | 0 to 255   E.g the value of 128 corresponds to a ratio of 50:50. | Byte 5 | Byte 11 |
| **Feedback Signals** |  |  |  |  |
| STS_ENABLE | Indicates an output sequence is running. | 0 = pulse output blocked  1 = pulse output running | Byte 0:  Bit 0 | Byte 4:  Bit 0 |
| STS_DO | Indicates the signal level at the digital output DO.  Note the update rate. | 0 = Signal 0 on digital output DO  1 = Signal 1 on digital output DO | Byte 0:  Bit 1 | Byte 4:  Bit 1 |
| STS_DI | Indicates the signal level at digital input DI. | 0 = Signal 0 on digital input DI  1 = Signal 1 on digital input DI | Byte 0:  Bit 2 | Byte 4:  Bit 2 |
| ACK_SW_ENABLE | Indicates the status of SW_ENABLE. | 0 = SW_ENABLE cleared.  1 = SW_ENABLE set | Byte 0:  Bit 3 | Byte 4:  Bit 3 |
| ERR_PULS | Indicates a pulse output error. | 0 = no pulse output error  1 = pulse output error | Byte 0:  Bit 4 | Byte 4:  Bit 4 |
| SEQ_CNT (as of 6ES7138‑4DD01‑0AB0) | Is incremented after completion of an output sequence. | Without HW enable: 0 … 1  With HW enable: 0 … 15 | Byte 1:  Bit 0 … 3 | Byte 5:  Bit 0 … 3 |
| Current measurement (as of 6ES7138‑4DD01‑0AB0) | Current at the DO as a SIMATIC S7 analog value. | 0 … 27648 (overrange up to 32767) | Word 2 | Word 6 |

#### Input and output signals of "Pulse train" operating mode (S7-300, S7-400)

##### Input and output signals of "Pulse train" operating mode

The table below shows the input and output signals of the operating mode "Pulse train".

| Input and Output Signals | Meaning | Value range | Channel 0 terminal | Channel 1 terminal |
| --- | --- | --- | --- | --- |
| **Input signal** |  |  |  |  |
| HW enable | You can select the HW enable with the "Function DI" parameter. The signal of the digital input DI is then interpreted by the 2PULSE at the start. | 0 = HW enable cleared  1 = HW enable issued  0 → 1 = Start of the output sequence; dependent on the software enable (SW_ENABLE) | 1 | 5 |
| **Output Signal** |  |  |  |  |
| Pulse train at the DO digital output | The preset number of pulses is output at the DO digital output. | 0 = no pulse  1 = pulse | 4 | 8 |

### "On/Off-delay" operating mode (S7-300, S7-400)

This section contains information on the following topics:

- ["On/Off-delay" operating mode (S7-300, S7-400)](#onoff-delay-operating-mode-s7-300-s7-400-1)
- [Parameters for the "On/Off-delay" operating mode (S7-300, S7-400)](#parameters-for-the-onoff-delay-operating-mode-s7-300-s7-400)
- [Control and feedback signals of the "On/Off-delay" operating mode (S7-300, S7-400)](#control-and-feedback-signals-of-the-onoff-delay-operating-mode-s7-300-s7-400)
- [Input and output signals of the "On/Off-delay" operating mode (S7-300, S7-400)](#input-and-output-signals-of-the-onoff-delay-operating-mode-s7-300-s7-400)

#### "On/Off-delay" operating mode (S7-300, S7-400)

##### Definition

The signal pending at the digital input DI is output with an on/off-delay at the digital output DO by the 2PULSE.

The following figure shows the block diagram for the operating mode "On/Off-delay".

![Definition](images/23590347659_DV_resource.Stream@PNG-en-US.png)

##### Output Sequence Enable

You must always issue the enable for the output sequence by means of the [software enable](#2pulse-control-assignment-s7-300-s7-400) (SW_ENABLE 0 → 1; MANUAL_DO = 0) in your control program, STS_ENABLE is then set. The [feedback bit](#2pulse-feedback-interface-s7-300-s7-400)ACK_SW_ENABLE indicates the software enable pending at the 2PULSE.

The positive edge on the DI digital input (0 → 1) starts the on-delay, and the [DO digital output](#sequence-counter-as-of-6es7138-4dd01-0ab0-s7-300-s7-400) is set on expiration of the on-delay.

The negative edge on the DI digital input (1 → 0) starts the off-delay, and the [DO digital output](#sequence-counter-as-of-6es7138-4dd01-0ab0-s7-300-s7-400) is deleted on expiration of the off-delay.

If the 2PULSE recognizes a pulse duration or interpulse period that is too short, this is displayed by the [pulse output error](#2pulse-feedback-interface-s7-300-s7-400)ERR_PULS.

At the next edge at the DI digital input, the 2PULSE deletes the ERR_PULS feedback bit.

##### Pulse diagram

**SW_ENABLE is set, while DI = 0:**

The following figure shows an output sequence in the operating mode "On/Off-delay" if DI = 0 at the start.

![Pulse diagram](images/24634050699_DV_resource.Stream@PNG-en-US.png)

**SW_ENABLE is set, while DI = 1:**

If SW_ENABLE is set while DI = 1, the first edge at DI (falling edge) is ignored. The following figure shows the corresponding output sequence.

![Pulse diagram](images/24634067211_DV_resource.Stream@PNG-en-US.png)

##### Canceling the output sequence

Clearing the software enable (SW_ENABLE = 0) during the output sequence causes the output sequence to be aborted, along with STS_ENABLE and the digital output.

##### Truth table

The table below shows how the 2PULSE responds to certain signals.

| Software enable SW_ENABLE | Digital input DI | Digital output DO | STS_ENABLE | Output sequence |
| --- | --- | --- | --- | --- |
| 1 | 0 → 1 | 0, if on-delay &gt; 0 1, if on-delay = 0 | 1 | Starting |
| 1 | 1 → 0 | 1, if off-delay &gt; 0 0, if off-delay = 0 | 1 | Starting |
| 0 | Any status | 0 | 0 | Canceling |
| 1 | Any status | Previous status remains | 1 | - |
| 0 → 1 | 0 | 0 | 1 | - |

##### Minimum Pulse Duration/Minimum Interpulse Period of the Digital Output DO

The minimum pulse duration/minimum interpulse period of the digital output DO amounts to 100 µs.

Make sure you take this into consideration when you set the on/off-delay and the pulse duration/interpulse period of the digital input DI; otherwise, the response at the digital output DO is not defined.

##### The Pulse Duration of the Digital Input DI Is Too Short

The 2PULSE detects a pulse that is too short on the negative edge on the digital input DI if:

Pulse duration + Off-delay ≤ On-delay.

Response of the 2PULSE to a pulse duration that is too short:

- ERR_PULS is set
- The current on-delay is deleted.
- The Off-delay is not started.
- The signal level at the digital output DO remains at 0.

ERR_PULS is deleted at the next positive edge on the digital input DI.

The following figure shows the behavior if the pulse duration is too short.

![The Pulse Duration of the Digital Input DI Is Too Short](images/23590526475_DV_resource.Stream@PNG-en-US.png)

##### The Interpulse Period of the Digital Input DI Is Too Short

The 2PULSE detects an interpulse period that is too short on the positive edge on the digital input DI if:

Interpulse period + on-delay ≤ Off-delay.

Response of the 2PULSE to a interpulse period that is too short:

- ERR_PULS is set
- The current Off-delay is deleted.
- The on-delay is not started.
- The signal level at the digital output DO remains at 1.

ERR_PULS is deleted with the next negative edge on the digital input DI.

The following figure shows the behavior if the interpulse period is too short.

![The Interpulse Period of the Digital Input DI Is Too Short](images/23590556299_DV_resource.Stream@PNG-en-US.png)

##### Retriggering the current on-delay

The 2PULSE starts a new on-delay on the positive edge on the digital input DI if:

On-delay &gt; pulse duration + interpulse period

This deletes the current Off-delay.

The digital output DO is only set if signal level 1 is present on the digital input DI longer than the on-delay. This enables you to filter rapid pulse trains.

The following figure shows the retriggering of the current on-delay.

![Retriggering the current on-delay](images/23590586123_DV_resource.Stream@PNG-en-US.png)

##### Retriggering the current Off-delay

The 2PULSE starts a new off-delay on the negative edge on the digital input DI if:

Off-delay &gt; pulse duration + interpulse period.

This deletes the current on-delay.

The digital output DO is only deleted if signal level 0 is present on the digital input DI longer than the off-delay.

The following figure shows the retriggering of the current off-delay.

![Retriggering the current Off-delay](images/23590615947_DV_resource.Stream@PNG-en-US.png)

##### Setting Times Using a Time Base

Use the assigned [time base](#selecting-a-time-base-s7-300-s7-400) to select the resolution and the value range of the on-delay and the off-delay.

| Symbol | Meaning |
| --- | --- |
| Time base = 0.1 ms: | You can set times from 0.2 ms to 6.5535 s with a resolution of 0.1 ms. |
| Time base = 1 ms: | You can set times from 1 ms to 65.535 s with a resolution of 1 ms. |

##### Set the on-delay and change when using the short control interface

You specify the [on-delay](#specifying-on-delay-s7-300-s7-400) as a value between 0 and 65535 in the parameters.

Configured on-delay = Time base x specified numerical value

Using the factor for the on-delay, you can adjust the assigned time in your control program. Set the factor between 0 and 255, with a weighting of 0.1:

On-delay = Factor x 0.1 x configured on-delay

If you change the on-delay factor, the new on-delay is activated with the next positive edge on the digital input DI.

##### Setting and changing the off-delay

Set the off-delay directly as a numerical value between 0 and 65535 in your [control program](#2pulse-control-assignment-s7-300-s7-400).

Off-delay = Time base x Specified numerical value

If you change the off-delay factor, the new Off-delay is activated with the next negative edge on the digital input DI.

##### Isochronous mode (as of 6ES7138‑4DD01‑0AB0)

In the "On/Off-delay" operating mode, isochronous mode does not have any influence on the functionality.

#### Parameters for the "On/Off-delay" operating mode (S7-300, S7-400)

##### Parameters for the "On/Off-delay" operating mode

The table below shows the parameters of the operating mode "On/Off-delay".

| Parameter | Meaning | Value range | Default |
| --- | --- | --- | --- |
| [Operating mode](#selecting-an-operating-mode-s7-300-s7-400-1) | Set the "On/Off-delay" operating mode. | - Pulse output - Pulse width modulation - Pulse train - On/Off-delay - Frequency output | Pulse width modulation |
| [Time base](#selecting-a-time-base-s7-300-s7-400) | Use the time base to select the resolution and the value range of the on-delay and Off-delay. | - 0.1 ms - 1 ms | 0.1 ms |
| [On-delay](#specifying-on-delay-s7-300-s7-400) <sup>1)</sup> | The time between a positive edge of digital input DI and its output on the digital output DO. You can change the on-delay with your control program with "On-delay factor". | 0 to 65535 | 0 |
| <sup>1)</sup> Only if the short [control interface](#2pulse-control-assignment-s7-300-s7-400) is used If the long control interface is used, enter this value directly in the control interface. |  |  |  |

#### Control and feedback signals of the "On/Off-delay" operating mode (S7-300, S7-400)

##### Control and feedback signals of the "On/Off-delay" operating mode

The table below shows the control and feedback signals of the operating mode "On/Off-delay".

| Control and feedback signals | Meaning | Value range | Channel 0 address | Channel 1 address |
| --- | --- | --- | --- | --- |
| **Control signals when the short control interface is used (8 bytes)** |  |  |  |  |
| Software enable (SW_ENABLE) | You must always issue the software enable in your control program. If you cancel the software enable, the current output sequence will be canceled. | 0 = SW_ENABLE cleared.  1 = SW_ENABLE set | Byte 2:  Bit 0 | Byte 6:  Bit 0 |
| Off-delay | The time between a negative edge of the digital input DI and its output on the digital output DO. | With time base 0.1 ms: 2 to 65535  With time base 1 ms: 1 to 65535  If you violate the low limit of the range, the off-delay will not function. | Word 0 | Word 4 |
| On-delay factor | You can change the assigned on-delay:  On-delay = Factor x 0.1 x configured on-delay | Factor: 0 to 255  On-delay:  0.2 ms to 65.535 s  If the on-delay is &lt; 0.2 ms or if the factor = 0, the effective on-delay = 0.  If the on-delay is &gt; 65.535 s, the on-delay is limited to 65.535 s. | Byte 3 | Byte 7 |
| **Control signals when the long control interface is used (12 bytes) (as of**  **6ES7138‑4DD01‑0AB0** **)** |  |  |  |  |
| Software enable (SW_ENABLE) | You must always issue the software enable in your control program. If you cancel the software enable, the current output sequence will be canceled. | 0 = SW_ENABLE cleared.  1 = SW_ENABLE set | Byte 4:  Bit 0 | Byte 10:  Bit 0 |
| Off-delay | The time between a negative edge of the digital input DI and its output on the digital output DO. | With time base 0.1 ms: 2 to 65535  With time base 1 ms: 1 to 65535  If you violate the low limit of the range, the off-delay will not function. | Word 0 | Word 6 |
| On-delay | The time between a positive edge of the digital input DI and its output on the digital output DO. | With time base 0.1 ms: 2 to 65535  With time base 1 ms: 1 to 65535  If you violate the low limit of the range, the on-delay will not function. | Word 2 | Word 8 |
| **Feedback Signals** |  |  |  |  |
| STS_ENABLE | Indicates the status of the software enable (SW_ENABLE). | 0 = software enable blocked  1 = software enable issued | Byte 0:  Bit 0 | Byte 4:  Bit 0 |
| STS_DO | Indicates the signal level at the digital output DO.  Note the update rate. | 0 = Signal 0 on digital output DO  1 = Signal 1 on digital output DO | Byte 0:  Bit 1 | Byte 4:  Bit 1 |
| STS_DI | Indicates the signal level at digital input DI. | 0 = Signal 0 on digital input DI  1 = Signal 1 on digital input DI | Byte 0:  Bit 2 | Byte 4:  Bit 2 |
| ACK_SW_ENABLE | Indicates the status of SW_ENABLE. | 0 = SW_ENABLE cleared.  1 = SW_ENABLE set | Byte 0:  Bit 3 | Byte 4:  Bit 3 |
| ERR_PULS | Indicates a pulse output error if the pulse duration or interpulse period is too short. | 0 = no pulse output error  1 = pulse output error | Byte 0:  Bit 4 | Byte 4:  Bit 4 |
| SEQ_CNT (as of 6ES7138‑4DD01‑0AB0) | Is incremented at DO with each edge (positive and negative). | 0 … 15 | Byte 1:  Bit 0 … 3 | Byte 5:  Bit 0 … 3 |
| Reserved | – | 0 | Word 2 | Word 6 |

#### Input and output signals of the "On/Off-delay" operating mode (S7-300, S7-400)

##### Input and output signals of the "On/Off-delay" operating mode

The table below shows the input and output signals of the operating mode "On/Off-delay".

| Input and Output Signals | Meaning | Value range | Channel 0 terminal | Channel 1 terminal |
| --- | --- | --- | --- | --- |
| **Input signal** |  |  |  |  |
| Digital input DI | The signal of the digital input DI is output with an on/off-delay on digital output DO by the 2PULSE. | 0 = no pulse  1 = pulse | 1 | 5 |
| **Output Signal** |  |  |  |  |
| Pulse on the digital output DO | The signal of the digital input DI is output with an on/off-delay on digital output DO by the 2PULSE. | 0 = no signal  1 = signal | 4 | 8 |

### "Frequency output" mode (as of 6ES7138-4DD01-0AB0) (S7-300, S7-400)

This section contains information on the following topics:

- ["Frequency output" operating mode (S7-300, S7-400)](#frequency-output-operating-mode-s7-300-s7-400)
- [Parameters of the "Frequency output" operating mode (S7-300, S7-400)](#parameters-of-the-frequency-output-operating-mode-s7-300-s7-400)
- [Control and feedback signals of the "Frequency output" operating mode (S7-300, S7-400)](#control-and-feedback-signals-of-the-frequency-output-operating-mode-s7-300-s7-400)
- [Input and output signals of the "Frequency output" operating mode (S7-300, S7-400)](#input-and-output-signals-of-the-frequency-output-operating-mode-s7-300-s7-400)

#### "Frequency output" operating mode (S7-300, S7-400)

##### Definition

A square wave signal with a specified frequency is output at the digital output of the 2PULSE.

The output sequence is started on expiration of the configured [on-delay](#specifying-on-delay-s7-300-s7-400) on the DO digital output of the 2PULSE.

The following figure shows the block diagram for the operating mode "Frequency output".

![Definition](images/28155659787_DV_resource.Stream@PNG-en-US.png)

##### Starting the Output Sequence

You must always issue the enable for the output sequence by means of the [software enable](#2pulse-control-assignment-s7-300-s7-400) (SW_ENABLE 0 → 1; MANUAL_DO = 0) in your control program.

The [feedback bit](#2pulse-feedback-interface-s7-300-s7-400)ACK_SW_ENABLE indicates the software enable pending at the 2PULSE.

You can also set the digital input DI of the 2PULSE as a HW enable with the "[Function DI](#selecting-di-function-s7-300-s7-400)" parameter.

If you want to work with the software enable and hardware enable at the same time, when the software enable has been issued, the output sequence starts with the first positive edge of the hardware enable. Further positive edges of the hardware enable during the current output sequence are ignored by the 2PULSE.

When the enable is issued (positive edge), the on-delay is started and the STS_ENABLE set. The frequency output is started on expiration of the on-delay time. The output sequence runs continuously as long as SW_ENABLE is set.

##### Pulse diagram

The following figure shows an output sequence for the operating mode "Frequency output".

![Pulse diagram](images/28155718923_DV_resource.Stream@PNG-en-US.png)

##### Canceling the output sequence

Deleting the software enable (SW_ENABLE = 0) during the on-delay or the frequency output cancels the output sequence, and STS_ENABLE and the DO digital output are canceled.

You will then have to restart the output sequence.

##### Truth Table

The table below shows how the 2PULSE responds to certain signals.

| Software enable SW_ENABLE | Hardware enable (digital input DI) | Digital output DO | STS_ENABLE | Output sequence |
| --- | --- | --- | --- | --- |
| 1 | 0 → 1 | 0, if on-delay &gt; 0 1, if on-delay = 0 | 0 → 1 | Starting |
| 0 → 1 | Not used | 0, if on-delay &gt; 0 1, if on-delay = 0 | 0 → 1 | Starting |
| 0 | Any status | 0 | 0 | Canceling |
| 1 | Any status | Previous status remains |  | - |
| 0 → 1 | 0 | 0 | 0 | - |

##### Setting Times Using a Time Base

Use the configured [time base](#selecting-a-time-base-s7-300-s7-400) to select the resolution and the value range of the on-delay.

| Symbol | Meaning |
| --- | --- |
| Time base = 0.1 ms: | You can set times from 0.2 ms to 6.5535 s with a resolution of 0.1 ms. |
| Time base = 1 ms: | You can set times from 1 ms to 65.535 s with a resolution of 1 ms. |

##### Setting and Changing the Output Value

You select the range of the output value with the "[Output format](#selecting-the-output-format-s7-300-s7-400)" parameter.

- If your output value is between 1 Hz and 5000 Hz, select the output format "1 Hz".
- If your output value is a SIMATIC S7 analog value (between 0 and 27648), select the "S7 analog output" output format. With "S7 analog output" you attain a higher accuracy at the setpoint specification.

  The 2PULSE calculates the frequency according to the following equation:

  Frequency = (Setpoint / 27648) × 5 kHz

You set the output value directly using your control program. The new frequency value is applied at the next rising edge of the output.

##### Output frequency accuracy

The configured output frequency is output with the following accuracy at the digital output DO:

- 0.01 Hz at output frequencies of 0.1 Hz to 800 Hz
- 0.1 Hz at output frequencies &gt; 800 Hz to 2000 Hz
- 0.5 Hz at output frequencies &gt; 2000 Hz to 5000 Hz

##### Set the on-delay when using the short control interface

You specify the [on-delay](#specifying-on-delay-s7-300-s7-400) as a value between 0 and 65535 in the parameters.

Configured on-delay = Time base x specified numerical value

When the short control interface is used, the factor for the on-delay can be used to adjust the configured time in your control program. Set the factor between 0 and 255, with a weighting of 0.1:

On-delay = Factor x 0.1 x configured on-delay

##### Isochronous mode

In the "Frequency output" operating mode, isochronous mode does not have any influence on the functionality.

#### Parameters of the "Frequency output" operating mode (S7-300, S7-400)

##### Parameters of the "Frequency output" operating mode

The table below shows the parameters of the operating mode "Frequency output".

| Parameter | Meaning | Value range | Default |
| --- | --- | --- | --- |
| [Operating mode](#selecting-an-operating-mode-s7-300-s7-400-1) | Set the "Frequency output" operating mode. | - Pulse output - Pulse width modulation - Pulse train - On/Off-delay - Frequency output | Pulse width modulation |
| [Time base](#selecting-a-time-base-s7-300-s7-400) | Use the time base to select the resolution and the value range of the on-delay. | - 0.1 ms - 1 ms | 0.1 ms |
| [Output format](#selecting-the-output-format-s7-300-s7-400) | Choose between 1 Hz and the S7 analog output format, depending on which output frequency resolution you need. | - 1 Hz - S7 analog output | 1 Hz |
| [Function DI](#selecting-di-function-s7-300-s7-400) | You can use the digital input DI as an input or as a HW enable. | - Input - HW enable | Input |
| [On-delay](#specifying-on-delay-s7-300-s7-400) <sup>1)</sup> | The time from the start of the output sequence to the output of the pulse train. You can change the on-delay in your control program using the "On-delay factor". | 0 to 65535 | 0 |
| <sup>1)</sup> Only if the short [control interface](#2pulse-control-assignment-s7-300-s7-400) is used If the long control interface is used, enter this value directly in the control interface. |  |  |  |

#### Control and feedback signals of the "Frequency output" operating mode (S7-300, S7-400)

##### Control and feedback signals of the "Frequency output" operating mode

The table below shows the control and feedback signals of the operating mode "Frequency output".

| Control and feedback signals | Meaning | Value range | Channel 0 address | Channel 1 address |
| --- | --- | --- | --- | --- |
| **Control signals when the short control interface is used (8 bytes)** |  |  |  |  |
| Software enable (SW_ENABLE) | Starting and canceling of the output sequence. | 0 = SW_ENABLE canceled 1 = SW_ENABLE set 0→1 = start of output sequence; may be dependent on the hardware enable | Byte 2:  Bit 0 | Byte 6:  Bit 0 |
| Output value | The value that is output in frequency format on the digital output DO. | Depending on the output format:  - 1 Hz: 0 ... 5000 - S7 analog output: 0 to 27648   If you enter an output value &gt; 5000 or 27648, the 2PULSE limits this to 5000 or 27648. | Word 0 | Word 4 |
| On-delay factor | The on-delay that has been assigned parameters can be changed before the start of the output sequence:  On-delay = Factor x 0.1 x configured on-delay | 0 to 255  If the on-delay &lt;0.2 ms or if factor = 0, the effective on-delay is = 0. If there is an on-delay &gt; 65.535 s, the on-delay is limited to 65.535 s. | Byte 3 | Byte 7 |
| **Control signals when the long control interface is used (12 bytes)** |  |  |  |  |
| Software enable (SW_ENABLE) | Starting and canceling of the output sequence. | 0 = SW_ENABLE canceled 1 = SW_ENABLE set 0→1 = start of output sequence; may be dependent on the hardware enable | Byte 4:  Bit 0 | Byte 10:  Bit 0 |
| Output value | The value that is output in frequency format on the digital output DO. | Depending on the output format:  - 1 Hz: 0 ... 5000 - S7 analog output: 0 to 27648   If you enter an output value &gt; 5000 or 27648, the 2PULSE limits this to 5000 or 27648. | Word 0 | Word 6 |
| On-delay | The on-delay can be changed before the start of the output sequence. | 0 to 65535  On-delay = Time basis x Specified numerical value | Word 2 | Word 8 |
| **Feedback Signals** |  |  |  |  |
| STS_ENABLE | Indicates an output sequence is running. | 0 = pulse output blocked  1 = pulse output running | Byte 0:  Bit 0 | Byte 4:  Bit 0 |
| STS_DO | Indicates the signal level at the digital output DO.  Note the update rate. | 0 = Signal 0 on digital output DO  1 = Signal 1 on digital output DO | Byte 0:  Bit 1 | Byte 4:  Bit 1 |
| STS_DI | Indicates the signal level at digital input DI. | 0 = Signal 0 on digital input DI  1 = Signal 1 on digital input DI | Byte 0:  Bit 2 | Byte 4:  Bit 2 |
| ACK_SW_ENABLE | Indicates the status of SW_ENABLE. | 0 = SW_ENABLE cleared.  1 = SW_ENABLE set | Byte 0:  Bit 3 | Byte 4:  Bit 3 |
| SEQ_CNT | No function in this operating mode. | – | Byte 1:  Bit 0 … 3 | Byte 5:  Bit 0 … 3 |
| Reserved | – | 0 | Word 2 | Word 6 |

#### Input and output signals of the "Frequency output" operating mode (S7-300, S7-400)

##### Input and output signals of the "Frequency output" operating mode

The table below shows the input and output signals of the operating mode "Frequency output".

| Input and Output Signals | Meaning | Value range | Channel 0 terminal | Channel 1 terminal |
| --- | --- | --- | --- | --- |
| **Input signal** |  |  |  |  |
| HW enable | You can select the HW enable with the "Function DI" parameter. The signal of the digital input DI is then interpreted by the 2PULSE at the start of the output sequence. | 0 = HW enable cleared 1 = HW enable issued 0 → 1 = Start of the output sequence; dependent on the software enable | 1 | 5 |
| **Output Signal** |  |  |  |  |
| Frequency on the digital output DO | The frequency is output on the digital output DO. | 0 = no pulse  1 = pulse | 4 | 8 |

### Sequence counter (as of 6ES7138-4DD01-0AB0) (S7-300, S7-400)

The 2PULSE has a sequence counter for each channel with which the completed output sequences are counted.  
You can monitor the completion of an output sequence with the sequence counter SEC_CNT in the feedback interface.

The counter has a width of 4 bits. After an high limit violated it jumps back to 0.

#### Function of the sequence counter

The sequence counter has the following function in the individual operating modes:

- [Pulse output](#pulse-train-operating-mode-s7-300-s7-400-1) and [pulse train](#pulse-output-operating-mode-s7-300-s7-400-1)

  - Without hardware enable the counter is set to 1 after completion of the output sequence.
  - With hardware enable, the counter is incremented after every completed output sequence.
- [On/Off-delay](#onoff-delay-operating-mode-s7-300-s7-400-1)

  The counter is incremented at DO with each edge (positive and negative).
- Pulse width modulation and frequency output

  The counter does not have any function.

When the software enable (SW_ENABLE = 0) is created, the counter is reset to 0.

#### Application options

The sequence counter can be used in particular for:

- Detecting (counting) very short pulses
- Counting output sequences in connection with the hardware enable

### Function: Current measurement (as of 6ES7138-4DD01-0AB0) (S7-300, S7-400)

The measurement of current can be set in a variety of applications for control and diagnostics purposes. You can read the measured value of the current from the feedback interface.

#### Principle of operation

A measurement of current only takes place during the pulse output in the "[Pulse width modulation](#pulse-width-modulation-operating-mode-s7-300-s7-400-1)" and "[Pulse train](#pulse-train-operating-mode-s7-300-s7-400-1)" operating modes. Without a pulse output (at STS_ENABLE = 0), 0 is supplied as the measured value. The measured value is valid at STS_ENABLE = 1.

In the "Pulse output", On/Off-delay" and "Frequency output" operating modes, 0 is always measured as the measured value of the current.

The returned measured value of the current is a mean value of measured values that is recorded during the duration of a period. At period durations &lt; 5 ms, the interval between two individual measuring points amounts to a maximum of 40 µs. When longer periods are involved, 128 measuring points per period are always recorded. This results in correspondingly longer intervals between the measuring points.

In isochronous mode, a new measured value of the current is always made available in the feedback interface at the moment T<sub>i</sub>. In non-isochronous mode, a new measured value of the current is made available about every 500 µs.

> **Note**
>
> In order for the current measurement to work correctly, no freewheeling diode may be applied to the load.

#### Measuring range and measured value

The measuring range is set fixed to a rated current of 2 A.

The measured value of the current is supplied as a SIMATIC S7 analog value in the [feedback interface](#2pulse-feedback-interface-s7-300-s7-400).

- A current of 2 A corresponds to the SIMATIC S7 analog value of 27648.
- With a parallel connection, a current of 4 A corresponds to the SIMATIC S7 analog value of 27648.

Measurements of current are possible up to a SIMATIC S7 analog value of 32767. This corresponds to a current of 2.4 A. Currents above 2 A may occur only briefly.

#### Accuracy

The accuracy of the measurement of current amounts to 3% of the measuring range.

> **Note**
>
> This accuracy during current measurement can only be achieved if the time period is not changed during the measurement.

### Function: Direct control of the digital output DO (S7-300, S7-400)

#### Definition

You can directly control the digital output DO of the 2PULSE to test the actuator you have connected. To do this, you have to select the function from your [control program](#2pulse-control-assignment-s7-300-s7-400) with the MANUAL_DO control bit set and SW_ENABLE control bit cleared. The function

- Supports you in commissioning a plant
- Allows you to utilize an unused channel of the 2PULSE as DO

After you have selected the function, the [feedback bits](#2pulse-feedback-interface-s7-300-s7-400)STS_ENABLE and ERR_PULS are cleared by the 2PULSE, and an active output sequence is aborted. The function takes precedence over the currently selected operating mode.

You specify the status of the digital output DO with the [control bit](#2pulse-control-assignment-s7-300-s7-400)SET_DO.

When you clear the MANUAL_DO control bit, you deselect the "Direct control of the digital output DO" function. This deletes the digital output DO. You can then restart an output sequence with the rising edge of SW_ENABLE.

#### Control and Feedback Signals/Output Signal

| Signals | Meaning | Value range | When the short control interface is used (8 bytes) |  |  | When the long control interface is used (12 bytes) |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Channel 0 address | Channel 1 address |  | Channel 0 address | Channel 1 address |  |  |  |
| **Control signals** |  |  |  |  |  |  |  |
| SW_ENABLE | To select the function, the control bit must be deleted. | 0 = SW_ENABLE cleared.  1 = SW_ENABLE set | Byte 2:  Bit 0 |  | Byte 6:  Bit 0 | Byte 4:  Bit 0 | Byte 10:  Bit 0 |
| MANUAL_DO | You can select and deselect the function with the control bit. | 0 = direct control of the DO not selected.  1 = direct control of the DO selected. | Byte 2:  Bit 1 |  | Byte 6:  Bit 1 | Byte 4:  Bit 1 | Byte 10:  Bit 1 |
| SET_DO | You use the control bit to set the status of the digital output DO. | 0 = signal 0 on digital output DO  1 = signal 1 on digital output DO | Byte 2:  Bit 2 |  | Byte 6:  Bit 2 | Byte 4:  Bit 2 | Byte 10:  Bit 2 |
| **Feedback signals** |  |  |  |  |  |  |  |
| STS_ENABLE | Deleted after the function has been selected. | 0 = pulse output blocked  1 = pulse output running | Byte 0:  Bit 0 |  | Byte 4:  Bit 0 | Byte 0:  Bit 0 | Byte 4:  Bit 0 |
| STS_DO | Indicates the signal level at the digital output DO.  Note the update rate. | 0 = Signal 0 on digital output DO  1 = Signal 1 on digital output DO | Byte 0:  Bit 1 |  | Byte 4:  Bit 1 | Byte 0:  Bit 1 | Byte 4:  Bit 1 |
| STS_ DI | Indicates the signal level at digital input DI. | 0 = Signal 0 on digital input DI  1 = Signal 1 on digital input DI | Byte 0:  Bit 2 |  | Byte 4:  Bit 2 | Byte 0:  Bit 2 | Byte 4:  Bit 2 |
| **Output Signal** |  |  |  |  |  |  |  |
| Digital output DO | The status preset with the SET_DO control bit is output on the digital output DO. | 0 = No signal  1 = Signal | 4 |  | 8 | 4 | 8 |

### Function: Error detection / diagnostics (S7-300, S7-400)

#### Parameter Assignment ErrorERR_PARA

If the 2PULSE cannot identify the parameters as its own, it generates a [parameter assignment error](#2pulse-feedback-interface-s7-300-s7-400). The two channels are then not assigned parameters.

The 2PULSE slot you configure must match the setup.

#### Pulse output error ERR_PULS

The 2PULSE detects a channel-specific pulse output error in the operating modes "[Pulse output](#pulse-output-operating-mode-s7-300-s7-400-1)", "[On/off-delay](#onoff-delay-operating-mode-s7-300-s7-400-1)", and "[Pulse train](#pulse-train-operating-mode-s7-300-s7-400-1)".

You can find information about causes and responses in the respective operating mode descriptions and under "[Feedback interface of 2PULSE](#2pulse-feedback-interface-s7-300-s7-400)".

The pulse output error detected is displayed for the relevant channel with the [feedback bit](#2pulse-feedback-interface-s7-300-s7-400)ERR_PULS.

#### Short circuit of the encoder supply ERR_24V

The 2PULSE detects a short circuit in the encoder supply that it makes available at terminals 2 and 6.

The short circuit error detected is displayed for the two channels with the [feedback bit](#2pulse-feedback-interface-s7-300-s7-400)ERR_24V.

A drop in the 24 V supply voltage can also result in a short circuit message.

#### Short circuit digital output ERR_DO

The 2PULSE detects a short circuit on the digital output of the channel.

The detected short circuit is displayed for the relevant channel with the [feedback bit](#2pulse-feedback-interface-s7-300-s7-400)ERR_DO.

> **Note**
>
> If a short circuit occurs, the digital output is able to briefly supply a current substantially higher than the rated value.

#### Diagnostic Message

If a short circuit occurs in the encoder supply or in the digital output, the 2PULSE generates a diagnostic message for the connected CPU/master. You must enable the "[Group diagnostics](#enabling-group-diagnostics-s7-300-s7-400)" parameter in this case.

> **Note**
>
> Diagnostic messages provide you the information that an error has occurred in one or both channels of the 2PULSE. You can evaluate the diagnostics with STEP 7.
>
> The diagnostic record DS1 only contains the information for Channel 0. However, a diagnostic interrupt is also triggered at errors in Channel 1. The feedback signals provide detailed information about the occurring errors from both channels. Evaluate the [feedback interface](#2pulse-feedback-interface-s7-300-s7-400) in new user programs (see below).

#### Parameters

| Parameter | Meaning | Value Range | Default |
| --- | --- | --- | --- |
| [Group diagnostics](#enabling-group-diagnostics-s7-300-s7-400) | When group diagnostics is enabled, the 2PULSE generates a diagnostic message for the CPU/master. | Disable/enable | Disable |
| [Diagnostics DO](#activating-do-diagnostics-s7-300-s7-400) | The 2PULSE detects a short circuit of the digital outputs when "Diagnostics DO" = On. | Off/on | On |

#### Feedback Signals

| Feedback Signals | Meaning | Value Range | Channel 0 address | Channel 1 address |
| --- | --- | --- | --- | --- |
| ERR_PARA | Indicates a parameter assignment error. | 0 = no parameter assignment error  1 = parameter assignment error | Byte 0:  Bit 5 | Byte 4:  Bit 5 |
| ERR_PULS | Indicates a pulse output error. | 0 = no pulse output error  1 = pulse output error | Byte 0:  Bit 4 | Byte 4:  Bit 4 |
| ERR_24V | Indicates a short circuit of the encoder supply. | 0 = no encoder supply short circuit  1 = encoder supply short circuit | Byte 0:  Bit 7 | Byte 4:  Bit 7 |
| ERR_DO | Indicates a short circuit of the digital output DO. | 0 = no digital output short circuit  1 = digital output short circuit | Byte 0:  Bit 6 | Byte 4:  Bit 6 |

### Parallel connection of both channels (as of 6ES7138-4DD01-0AB0) (S7-300, S7-400)

#### Definition

In order to achieve higher output current, you can connect both channels of the 2PULSE in parallel. You then obtain a rated current of 4 A. This allows you to also operate actuators with a higher power requirement directly at the 2PULSE.

#### Parameter assignment and operation

You can enable parallel connection of the two channels during the configuration by selecting the check box "[Parallel connection Channel 0 and 1](#activating-parallel-connection-channel-0-and-1-s7-300-s7-400)".

Once enabled, the 2PULSE operates like a single-channel module. All the parameter assignments and operations via the [control interface](#2pulse-control-assignment-s7-300-s7-400) have to be executed with Channel 0. Channel 1 cannot be configured and operated.

[Feedback signals](#2pulse-feedback-interface-s7-300-s7-400) are also only provided for Channel 0.

#### Measurement of current

During the measurement of current, the measured values from both channels are averaged once more. This results in a measuring range up to 4 A.

The measured value of the current is supplied as a SIMATIC S7 analog value in the feedback interface. A current of 4 A corresponds here to the SIMATIC S7 analog value of 27648.

The accuracy of the current measurement also amounts to 3% of the measuring range in case of parallel connection.

#### Pin assignment for the parallel connection

The following terminals have to be connected at the terminal module for the parallel connection of both channels of the 2PULSE:

- Terminal 3 and Terminal 7
- Terminal 4 and Terminal 8

You then connect the load (e.g. a actuator) directly to Terminals 3 and 4 or to Terminals 7 and 8. The following figure shows a connection layout.

![Pin assignment for the parallel connection](images/23596188939_DV_resource.Stream@PNG-en-US.png)

### Reaction to CPU/Master STOP (S7-300, S7-400)

#### Definition

You can [configure the reaction](#selecting-reaction-to-cpumaster-stop-s7-300-s7-400) of the 2PULSE to failure of the higher-level controller for the two channels together.

| Reaction to CPU/Master STOP | Channel-specific response and status of the 2PULSE |
| --- | --- |
| Turn off DO | Delete the DO digital output  Delete STS_ENABLE and  Terminate the current output sequence |
| Continue working mode | The DO digital output remains unchanged  STS_ENABLE remains unchanged and  The current output sequence is continued |
| DO substitute a value | Output of the channel-specific, substitute value that has been assigned parameters of the DO digital output  Delete STS_ENABLE and  Terminate the current output sequence |
| DO keeps last value | The DO digital output remains unchanged  Delete STS_ENABLE and  Terminate the current output sequence |

#### Startup

To start a new output sequence after CPU/Master STOP and a set ACK_SW_ENABLE, first delete SW_ENABLE. Keep deleting until ACK_SW_ENABLE is also deleted.

If the mode is to continue during a change from CPU/Master STOP to RUN (startup), the CPU/Master cannot clear the outputs. **Possible solution:** In the part of the user program that is executed during startup, set the "Software enable" (SW_ENABLE = 1) control bit.

#### Modified Parameter Assignment

The status assumed by the 2PULSE at CPU/Master STOP remains even in the case of parameter assignment or configuration of the ET 200S station. This occurs, for example, at POWER ON of the CPU/master or the IM 151 or at the resumption of DP transfer.

In "Continue working mode", however, and after loading changed parameters or configuration of the ET 200S station to the CPU/master, the 2PULSE terminates the process. As a result, the 2PULSE does the following:

- Deletes the DO digital output.
- Deletes STS_ENABLE and
- Terminates the current output sequence.

## Configuring and assigning parameters to 2PULSE (S7-300, S7-400)

This section contains information on the following topics:

- [Parameters (S7-300, S7-400)](#parameters-s7-300-s7-400)
- [Channel n (S7-300, S7-400)](#channel-n-s7-300-s7-400)
- [2PULSE control and feedback interface (S7-300, S7-400)](#2pulse-control-and-feedback-interface-s7-300-s7-400)

### Parameters (S7-300, S7-400)

This section contains information on the following topics:

- [Selecting an operating mode (S7-300, S7-400)](#selecting-an-operating-mode-s7-300-s7-400)
- [Enabling group diagnostics (S7-300, S7-400)](#enabling-group-diagnostics-s7-300-s7-400)
- [Selecting reaction to CPU/Master STOP (S7-300, S7-400)](#selecting-reaction-to-cpumaster-stop-s7-300-s7-400)
- [Activating parallel connection Channel 0 and 1 (S7-300, S7-400)](#activating-parallel-connection-channel-0-and-1-s7-300-s7-400)

#### Selecting an operating mode (S7-300, S7-400)

##### Operating mode

Select the operating mode of the 2PULSE in accordance with your requirements:

- 2 Pulse: 8 bytes output data – compatible to predecessor module

  The control interface uses fewer addresses in the process image.
- 2 Pulse ext. control interface: 12 bytes output data – improved controlling possibilities

  You can enter the setpoints more conveniently.

#### Enabling group diagnostics (S7-300, S7-400)

##### Group diagnostics

Group diagnostics are enabled in the respective check box.

When group diagnostics is enabled, the 2PULSE will generate a diagnostic message for the CPU/master.

#### Selecting reaction to CPU/Master STOP (S7-300, S7-400)

##### Reaction to CPU/Master STOP

Select the desired response to CPU/Master STOP from the dropdown list:

- Turn off DO
- Continue working mode
- DO substitute a value
- DO keep last value

You will find further information on the response and mode of the 2PULSE under "[Reaction to CPU/Master STOP](#reaction-to-cpumaster-stop-s7-300-s7-400)".

#### Activating parallel connection Channel 0 and 1 (S7-300, S7-400)

##### Parallel connection channel 0 and 1 (as of 6ES7138‑4DD01‑0AB0)

If you require a rated current of more than 2 A, you can connect the two channels of the 2PULSE in parallel. This is done by selecting the check box "Parallel connection Channel 0 and 1".

Additional information is available under "[Parallel connection of both channels (as of 6ES7138-4DD01-0AB0)](#parallel-connection-of-both-channels-as-of-6es7138-4dd01-0ab0-s7-300-s7-400)".

### Channel n (S7-300, S7-400)

This section contains information on the following topics:

- [Activating DO diagnostics (S7-300, S7-400)](#activating-do-diagnostics-s7-300-s7-400)
- [Selecting DO substitute value (S7-300, S7-400)](#selecting-do-substitute-value-s7-300-s7-400)
- [Selecting an operating mode (S7-300, S7-400)](#selecting-an-operating-mode-s7-300-s7-400-1)
- [Selecting the output format (S7-300, S7-400)](#selecting-the-output-format-s7-300-s7-400)
- [Selecting a time base (S7-300, S7-400)](#selecting-a-time-base-s7-300-s7-400)
- [Selecting DI function (S7-300, S7-400)](#selecting-di-function-s7-300-s7-400)
- [Specifying on delay (S7-300, S7-400)](#specifying-on-delay-s7-300-s7-400)
- [Specifying minimum pulse duration (S7-300, S7-400)](#specifying-minimum-pulse-duration-s7-300-s7-400)
- [Specifying pulse duration (S7-300, S7-400)](#specifying-pulse-duration-s7-300-s7-400)
- [Specifying period (S7-300, S7-400)](#specifying-period-s7-300-s7-400)

#### Activating DO diagnostics (S7-300, S7-400)

##### Diagnostics DO

2PULSE will detect a short at the digital outputs if you have selected the "DO diagnostics" checkbox.

#### Selecting DO substitute value (S7-300, S7-400)

##### Substitute value DO

Select the required substitute value for the digital output:

- 0
- 1

The parameter "Substitute value DO" may only have a value not equal to zero if the parameter "[Reaction to CPU/Master STOP](#selecting-reaction-to-cpumaster-stop-s7-300-s7-400)" has been set to "DO substitute a value".

#### Selecting an operating mode (S7-300, S7-400)

##### Operating mode

Select the required operating mode from the drop-down list:

- [Pulse output](#pulse-output-operating-mode-s7-300-s7-400)
- ["Pulse width modulation"](#pulse-width-modulation-operating-mode-s7-300-s7-400)
- [Pulse train](#pulse-train-operating-mode-s7-300-s7-400)
- [On/Off delay](#onoff-delay-operating-mode-s7-300-s7-400)
- [Frequency output](#frequency-output-mode-as-of-6es7138-4dd01-0ab0-s7-300-s7-400) (as of 6ES7138‑4DD01‑0AB0)

#### Selecting the output format (S7-300, S7-400)

##### Output format

The output format is relevant for operating modes "Pulse width modulation(PWM)" and "Frequency output" (as of 6ES7138‑4DD01‑0AB0).

- You can select the following output formats from the drop-down list in "[Pulse width modulation (PWM)](#pulse-width-modulation-operating-mode-s7-300-s7-400-1)" mode:

  - Per mill
  - S7 analog output
- You can select the following output formats from the drop-down list in "[Frequency output](#frequency-output-operating-mode-s7-300-s7-400)" mode:

  - 1 Hz
  - S7 analog output

#### Selecting a time base (S7-300, S7-400)

##### Time base

Use the time base to select the resolution and value range for all predefined times:

- 0.1 ms

  You can set times from 0.2 ms to 6.5535 s with a resolution of 0.1 ms.
- 1 ms

  You can set times from 1 ms to 65.535 s with a resolution of 1 ms.

#### Selecting DI function (S7-300, S7-400)

##### Function DI

You can use the DI digital input as an input or as a hardware enable.

Select the required function for the digital input from the drop-down list:

- Input
- Hardware enable

#### Specifying on delay (S7-300, S7-400)

##### On-delay

The on delay is the time from the start of the output sequence to pulse output.

Enter the required on delay in the input field.

Valid value range: 0 … 65535

#### Specifying minimum pulse duration (S7-300, S7-400)

##### Minimum pulse duration

Minimum pulse duration is relevant for operating modes "[Pulse width modulation (PWM)](#pulse-width-modulation-operating-mode-s7-300-s7-400-1)" and "[Frequency output](#frequency-output-operating-mode-s7-300-s7-400)" (as of 6ES7138‑4DD01‑0AB0).

You assign the minimum pulse duration and minimum break time using the "Minimum pulse duration" parameter; they always have the same value.

You can, for example, enter the response time of the actuator connected to your DO digital output here.

Valid value range: 0 … 65535

#### Specifying pulse duration (S7-300, S7-400)

##### Pulse duration

Pulse duration is relevant for "[Pulse train](#pulse-train-operating-mode-s7-300-s7-400-1)" mode.

You can, for example, enter the response time of the actuator connected to your DO digital output here.

Valid value range:

- With time base 1 ms: from 1 ... 65535
- With time base 0.1 ms: from 2 ... 65535

#### Specifying period (S7-300, S7-400)

##### Time period

The period is relevant for "[Pulse width modulation (PWM)](#pulse-width-modulation-operating-mode-s7-300-s7-400-1)" and "[Pulse train](#pulse-train-operating-mode-s7-300-s7-400-1)" operating modes.

When specifying the time period, take into account the set minimum pulse duration / pulse duration and the response time of the actuator connected to the digital output DO. The period should always be a multiple of the response time of the actuator connected to the DO digital output.

You specify the period as a numerical value in accordance with the time base:

- With time base 1 ms: from 1 ... 65535
- With time base 0.1 ms: from 2 ... 65535

Configured period = Time base x specified numerical value

### 2PULSE control and feedback interface (S7-300, S7-400)

This section contains information on the following topics:

- [2PULSE control assignment (S7-300, S7-400)](#2pulse-control-assignment-s7-300-s7-400)
- [2PULSE feedback interface (S7-300, S7-400)](#2pulse-feedback-interface-s7-300-s7-400)

#### 2PULSE control assignment (S7-300, S7-400)

> **Note**
>
> The following control interface data is consistent for 2PULSE:
>
> - Bytes 0 ... 3
> - Bytes 4 ... 7

##### Assignment of the short control interface (8 bytes)

The following table shows the assignment of the short control interface (outputs) of 2PULSE.

| Address |  | Assignment |
| --- | --- | --- |
| Channel 0 | Channel 1 |  |
| Word 0 | Word 4 | Depending on the mode  - Pulse output: Pulse duration - Pulse-width modulation: Output value - Pulse train: Number of pulses - On/Off-delay: Off-delay - Frequency output: Output frequency (as of 6ES7138‑4DD01‑0AB0) |
| Byte 2 | Byte 6 | Bit 7: Reserve = 0  Bit 6: Reserve = 0  Bit 5: Reserve = 0  Bit 4: Reserve = 0  Bit 3: Reserve = 0  Bit 2: SET_DO  Bit 1: MANUAL_DO  Bit 0: SW_ENABLE |
| Byte 3 | Byte 7 | Depending on mode  - Pulse output: On-delay factor - Pulse width modulation: Period duration factor - Pulse train: Period duration factor - On/Off-delay: On-delay factor - Frequency output: On-delay factor (as of 6ES7138‑4DD01‑0AB0) |

##### Assignment of the long control interface (12 bytes) (as of 6ES7138‑4DD01‑0AB0)

The following table shows the assignment of the long control interface (outputs) of 2PULSE.

| Address |  | Assignment |
| --- | --- | --- |
| Channel 0 | Channel 1 |  |
| Word 0 | Word 6 | Depending on mode  - Pulse output: Pulse duration - Pulse width modulation: Output value - Pulse train: Number of pulses - On/Off-delay: Off-delay - Frequency output: Output frequency |
| Word 2 | Word 8 | Depending on mode  - Pulse output: On-delay - Pulse width modulation: Period - Pulse train: Period - On/Off-delay: On-delay - Frequency output: On-delay |
| Byte 4 | Byte 10 | Bit 7: Reserve = 0  Bit 6: Reserve = 0  Bit 5: Reserve = 0  Bit 4: Reserve = 0  Bit 3: Reserve = 0  Bit 2: SET_DO  Bit 1: MANUAL_DO  Bit 0: SW_ENABLE |
| Byte 5 | Byte 11 | Depending on mode  - Pulse output: Not used - Pulse width modulation: On-delay factor - Pulse train: Pulse-pause ratio - On/Off-delay: Not used - Frequency output: Not used |

##### Notes on the Control Signals

| Control Signal | Explanation |
| --- | --- |
| **"Pulse output" operating mode:** |  |
| - Pulse duration <sup>1) 2)</sup> | The time that is set for the DO digital output on expiration of the on-delay. |
| - On-delay factor <sup>1)</sup> | You can change the configured on-delay before the start of the output sequence: On-delay = Factor × 0.1 × configured on-delay |
| - On-delay <sup>2)</sup> | The time from the start of the output sequence to the output of the pulse train. |
| **"Pulse width modulation" operating mode:** |  |
| - Output value <sup>1)  2)</sup> | Value that is output with pulse-width modulation at the DO digital output on expiration of the on-delay. |
| - Time period factor <sup>1)</sup> | You can change the configured period duration: Period duration = Factor × 0.1 × configured period duration |
| - Time period <sup>2)</sup> | When specifying the time period take into account the set minimum pulse duration and the response time of your actuator that is connected to the digital output DO. |
| - On-delay factor <sup>2)</sup> | You can change the configured on-delay before the start of the output sequence: On-delay = Factor × 0.1 × configured on-delay |
| **"Pulse train" operating mode:** |  |
| - Number of pulses <sup>1)  2)</sup> | Number of pulses that are output at the DO digital output on expiration of the on-delay. |
| - Period factor <sup>1)</sup> | You can change the configured time period before the start of the output sequence: Time period = Factor x 0.1 x configured time period |
| - Period <sup>2)</sup> | When specifying the period, take into account the set minimum pulse duration and the response time of the actuator connected to the digital output DO. |
| - Pulse-pause ratio <sup>  2)</sup> | You can set the ratio of pulse duration to break time: Pulse/Break ratio = (Setpoint / 255) × Period |
| **"On/Off-delay" operating mode:** |  |
| - Off-delay <sup>1)  2)</sup> | The time between a negative edge of the digital input DI and its output on the digital output DO. |
| - On-delay factor <sup>1)</sup> | You can change the configured on-delay before the start of the output sequence: On-delay = Factor × 0.1 × configured on-delay |
| - On-delay <sup>2)</sup> | The time between a positive edge of the digital input DI and its output on the digital output DO. |
| **"Frequency output" mode**(as of 6ES7138‑4DD01‑0AB0)**:** |  |
| - Output frequency <sup>1)  2)</sup> | Frequency that is output at the DO digital output after expiration of the on-delay. |
| - On-delay factor <sup>1)</sup> | You can change the configured on-delay before the start of the output sequence: On-delay = Factor × 0.1 × configured on-delay |
| - On-delay <sup>2)</sup> | The time from the start of the output sequence to the output of the frequency. |
| **Direct control of the digital output** |  |
| - MANUAL_DO | You use the control bit to select and deselect the "Direct control of the digital output DO" function. |
| - SET_DO | You use the control bit to set the status of the digital output DO. |
| **Software enable** |  |
| - SW_ENABLE | You must always issue the software enable in your control program. If you do not use a hardware enable, the output sequence will be started by the positive edge of the software enable. If you delete the software enable, the current output sequence will be terminated. |
| <sup>1)</sup> When using the short control interface   <sup>2)</sup> When using the long control interface |  |

#### 2PULSE feedback interface (S7-300, S7-400)

> **Note**
>
> The following data of the feedback interface are consistent for the 2PULSE:
>
> - Bytes 0 ... 3
> - Bytes 4 ... 7

##### Assignment of the Feedback Interface

The following table shows the assignment of the feedback interface (inputs) of 2PULSE.

| Address |  | Assignment |
| --- | --- | --- |
| Channel 0 | Channel 1 |  |
| Byte 0 | Byte 4 | Bit 7: ERR_24V  Bit 6: ERR_DO  Bit 5: ERR_PARA  Bit 4: ERR_PULS  Bit 3: ACK_SW_ENABLE  Bit 2: STS_DI  Bit 1: STS_DO  Bit 0: STS_ENABLE |
| Byte 1 | Byte 5 | Bit 0 to Bit 3: Sequence counter SEQ_CNT (as of 6ES7138‑4DD01‑0AB0)  Bit 4 to Bit 7: Reserve = 0 |
| Word 2 | Word 6 | Current measurement (as of 6ES7138‑4DD01‑0AB0) |

> **Note**
>
> In line with the IM 151 interface module used and with the configuration, a feedback value (substitute value) of either 16#7FFF7FFF or 16#00000000 will be output if the module fails.

##### Notes on the feedback signals

| Checkback signal | Explanation |
| --- | --- |
| ACK_SW_ENABLE | Indicates the status of the software enable pending at the 2PULSE. |
| ERR_24V | Indicates a short circuit or drop of the encoder supply. |
| ERR_DO | Indicates a short circuit at the digital output. |
| ERR_PARA | Indicates a parameter assignment error. |
| ERR_PULS | "Pulse output" operating mode: Indicates a pulse output error. If the pulse duration is reduced after expiration of the on-delay so the time is less than the time already output, this is detected by the 2PULSE. The 2PULSE deletes the feedback bit ERR_PULS next time the output sequence starts.  "Pulse train" operating mode: Indicates a pulse output error. If the number of pulses is reduced after expiration of the on-delay and the smaller number of pulses is already output, this is detected by the 2PULSE. The 2PULSE deletes the feedback bit ERR_PULS next time the output sequence starts.  "On/Off-delay" mode: Indicates a pulse output error if the pulse duration or interpulse period is too short.  The 2PULSE deletes the ERR_PULS feedback bit at the next positive edge of the software enable or at the next edge at the DI digital input. |
| STS_ DI | Indicates the signal level at the digital input DI. |
| STS_DO | Indicates the signal level at the digital output DO. |
| STS_ENABLE | "Pulse output" operating mode: Is set at the start of the output sequence until the pulse duration expires. If you delete the software enable (SW_ENABLE) or the 2PULSE detects a pulse output error (ERR_PULS), STS_ENABLE is deleted.  "Pulse-width modulation" operating mode: Set at start of output sequence. If you delete the software enable (STS_ENABLE), SW_ENABLE is deleted.  "Pulse train" operating mode: Is set at the start of the output sequence until the output of the last pulse. If you delete the software enable (SW_ENABLE) or the 2PULSE detects a pulse output error (ERR_PULS), STS_ENABLE will be deleted.  "On/Off-delay" mode: Indicates the status of the software enable (SW_ENABLE) detected by the 2PULSE.  "Frequency output" mode (as of 6ES7138‑4DD01‑0AB0): Set at start of output sequence. If you delete the software enable (STS_ENABLE), SW_ENABLE will be deleted. |
| SEQ_CNT (as of 6ES7138‑4DD01‑0AB0) | Counts the completed output sequences in the "Pulse output", "Pulse train" and "On/Off-delay" operating modes.  No function in the "Pulse width modulation" and "Frequency output" operating modes. |
| Current measurement (as of 6ES7138‑4DD01‑0AB0) | Current at the DO as a SIMATIC S7 analog value |

## 2PULSE diagnostics (S7-300, S7-400)

This section contains information on the following topics:

- [Diagnostics using the LED display (S7-300, S7-400)](#diagnostics-using-the-led-display-s7-300-s7-400)
- [Error types (S7-300, S7-400)](#error-types-s7-300-s7-400)

### Diagnostics using the LED display (S7-300, S7-400)

#### LED display at the 2PULSE

![LED display at the 2PULSE](images/22648719115_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Group error (red) |
| ② | Status display for digital input (green) |
| ③ | Status display for the digital output (green) |

#### Status and error displays by means of LEDs on the 2PULSE

The table below shows the status and fault displays on the 2PULSE.

| Event (LED) |  |  |  |  | Cause | Remedy |
| --- | --- | --- | --- | --- | --- | --- |
| SF | 1 | 5 | 4 | 8 |  |  |
| On |  |  |  |  | No parameter assignment. There is a diagnostic message. | Check the error bits types in the feedback interface. Evaluate the diagnostics data. |
|  | On |  |  |  | Input DI0 on Channel 0 activated. |  |
|  |  | On |  |  | Input DI1 on Channel 1 activated. |  |
|  |  |  | On |  | Output DO0 on Channel 0 activated. |  |
|  |  |  |  | On | Output DO1 on Channel 1 activated. |  |

### Error types (S7-300, S7-400)

For information on the structure of the channel-related diagnostics, refer to the manual on the interface module used in your ET 200S station.

#### 2PULSE error types

The following table shows the 2PULSE error types.

| Error class |  | Meaning | Remedy |
| --- | --- | --- | --- |
| 1<sub>D</sub> | 00001:  Short circuit | Short circuit of the sensor supply or the actuator.  A drop in the 24 V supply voltage can also result in this error message. | Check the wiring to the switches and actuators. Correct the process wiring. |
| 9<sub>D</sub> | 01001:  Error | Internal module error occurred. | Replace the module. |
| 16<sub>D</sub> | 10000:  Parameter assignment error | Parameters have not been assigned to the module. | Correct the parameter assignment. |

A simple error evaluation is also possible through the corresponding bits in the [feedback interface](#2pulse-feedback-interface-s7-300-s7-400).

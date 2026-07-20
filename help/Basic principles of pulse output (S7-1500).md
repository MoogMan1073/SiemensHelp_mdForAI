---
title: "Basic principles of pulse output (S7-1500)"
package: TFPulseMain15enUS
topics: 13
devices: [S7-1500, S7-1500T]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Basic principles of pulse output (S7-1500)

This section contains information on the following topics:

- [Overview of modules and properties (S7-1500)](#overview-of-modules-and-properties-s7-1500)
- [Basic information on pulse output (TM Pulse 2x24V) (S7-1500)](Basic%20information%20on%20pulse%20output%20%28TM%20Pulse%202x24V%29%20%28S7-1500%29.md#basic-information-on-pulse-output-tm-pulse-2x24v-s7-1500)
- [Basic principles of pulse output (Compact CPU) (S7-1500)](#basic-principles-of-pulse-output-compact-cpu-s7-1500)
- [Basic principles of pulse output (TM PTO) (S7-1500)](#basic-principles-of-pulse-output-tm-pto-s7-1500)

## Overview of modules and properties (S7-1500)

### Modules

The following table provides an overview of the performance features of the pulse output modules for the S7-1500 system.

| Property | S7-1500 |  |  |
| --- | --- | --- | --- |
| Technology module | Compact CPU | Technology module |  |
| TM Timer DIDQ 16x24V | CPU 1511C-1 PN,  CPU 1512C-1 PN | TM PTO 4 |  |
| Number of pulse generators | 16 | 4 | 4 |
| Operating mode Oversampling | X | — | — |
| Operating mode Pulse width modulation PWM | X | [X](#overview-s7-1500) | — |
| Operating mode Pulse output | —<sup>1</sup> | — | — |
| Operating mode Pulse train | —<sup>1</sup> | — | — |
| Operating mode On/Off delay | — | — | — |
| Operating mode Frequency output | — | [X](#overview-s7-1500) | — |
| Operating mode PWM with DC motor | — | — | — |
| Operating mode Pulse Train Output (PTO) | — | [X](#overview-s7-1500) | X |
| Sequence counter | — | — | — |
| High-speed output supported | X | [X](#function-high-speed-output-s7-1500) | — |
| Ditheringsupported | — | — | — |
| Current measurement / control | — | — | — |
| Support for Motion Control | — | X | X |
| HW enable | — | — | X |
| Parallel operation of 2 channels | — | — | — |
| Control of digital outputs with the user program | X | [X](#function-direct-control-of-the-pulse-output-dqa-s7-1500) | — |
| Support for isochronous mode on PROFINET | X | — | X |
| Diagnostic interrupt support | X | X | X |
| <sup>1</sup> You can implement a comparable function with the timer function. |  |  |  |

The following table provides an overview of the performance features of the modules for pulse output for the ET 200SP system.

| Property | ET 200SP |  |  |
| --- | --- | --- | --- |
| Technology module |  | Digital output module |  |
| TM Timer DIDQ 10x24V | TM Pulse 2x24V | DQ 4x24VDC/ 2A HS |  |
| Number of pulse generators | 6 | 2 | 4 |
| Operating mode Oversampling | X | — | X |
| Operating mode Pulse width modulation PWM | X | X | X |
| Operating mode Pulse output | —<sup>1</sup> | X | — |
| Operating mode Pulse train | —<sup>1</sup> | X | — |
| Operating mode On/Off delay | — | X | — |
| Operating mode Frequency output | — | X | — |
| Operating mode PWM with DC motor | — | X | — |
| Operating mode Pulse Train Output (PTO) | — | — | — |
| Sequence counter | — | X | — |
| High-speed output supported | X | X | — |
| Ditheringsupported | — | X | — |
| Current measurement / control | — | X | — |
| Support for Motion Control | — | — | — |
| HW enable | — | X | — |
| Parallel operation of 2 channels | — | X | — |
| Control of digital outputs with the user program | X | X | X |
| Support for isochronous mode on PROFINET | X | X | X |
| Diagnostic interrupt support | X | X | X |
| <sup>1</sup> You can implement a comparable function with the timer function. |  |  |  |

## Basic principles of pulse output (Compact CPU) (S7-1500)

This section contains information on the following topics:

- [Operating modes (S7-1500)](#operating-modes-s7-1500)
- [Functions (S7-1500)](#functions-s7-1500)

### Operating modes (S7-1500)

This section contains information on the following topics:

- [Overview (S7-1500)](#overview-s7-1500)
- [Operating mode: Pulse-width modulation (PWM) (S7-1500)](#operating-mode-pulse-width-modulation-pwm-s7-1500)
- [Operating mode: Frequency output (S7-1500)](#operating-mode-frequency-output-s7-1500)
- [Operating mode: PTO (S7-1500)](#operating-mode-pto-s7-1500)

#### Overview (S7-1500)

This section lists the new features of the CPU with firmware version V2.0.

| Operating mode | Applications | Customer benefits |
| --- | --- | --- |
| [Pulse width modulation](#operating-mode-pulse-width-modulation-pwm-s7-1500) (PWM) | The PWM operating mode is used when an output module is to control greatest possible outputs with low power loss (temperature rise, frame size).   You use pulse width modulation, for example, to control:   - the temperature in a heating resistor - the force of a coil in a proportional valve and thus the position of a valve from closed to completely open - the speed of a motor from standstill to full speed | With pulse width modulation, a signal with a defined period duration and variable duty cycle is output at the digital output. The duty cycle is the ratio of pulse duration to period duration. In PWM mode, you can control both the duty cycle and the period duration.  With pulse width modulation, you vary the mean value of the output voltage. Depending on the connected load, you can control the load current or the power with this. |
| [Frequency output](#operating-mode-frequency-output-s7-1500) | You can implement frequencies up to 100 kHz and thus work in ranges that cannot be reached by a CPU with a simple digital output. | You can generate frequencies very precisely.   The receiver can reconstruct the information exactly when transmission conditions are less than ideal.   In frequency output mode, you assign a frequency value with high frequencies more precisely than by using period duration (PWM). |
| [Pulse Train Output (PTO)](#operating-mode-pto-s7-1500) | Pulse Train Output is a simple and universal interface between a SIMATIC controller and a drive.  PTO is supported worldwide by many stepper and servo drives and is used in many positioning applications, such as for adjustment axes and feed axes. | PTO is also referred to as the pulse/direction interface. The pulse/direction interface comprises two signals. The frequency of the pulse output represents the velocity and the number of pulses that are output for the distance to be traversed. The direction output defines the traversing direction. This means that the position is specified with a precision within one increment.   The pulse/direction interface is especially well-suited for operation with the technology objects TO_SpeedAxis, TO_PositioningAxis and TO_SynchronousAxis. TO_MeasuringInput can be used to detect measuring inputs on the drive axis. |

#### Operating mode: Pulse-width modulation (PWM) (S7-1500)

##### Properties

The pulse-width modulation (PWM) mode of the compact CPU has the following technical properties:

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | **Minimum** |  |  | **Maximum** |  |  |
| **Standard output** | **High-speed output deactivated** | **High-speed output activated** | **Standard output** | **High-speed output deactivated** | **High-speed output activated** |  |
| Pulse duration | 100 µs with load &gt; 0.1 A<sup> 1)</sup>  200 µs with load ≥ 2 mA<sup> 1)</sup> | 20 µs with load &gt; 0.1 A<sup> 1)</sup>  40 µs with load ≥ 2 mA<sup> 1)</sup> | 2 µs<sup> 1) </sup> | 10,000,000 µs (10 s) |  |  |
| Cycle duration | 10 ms <sup>2)</sup> | 100 μs <sup>2)</sup> | 10 μs |  |  |  |
| <sup>1)</sup> A lower value is theoretically possible but, depending on the connected load, the output voltage can no longer be output as complete rectangular pulse   <sup>2)</sup> Load dependent |  |  |  |  |  |  |

##### Principle of operation

With pulse width modulation, a signal with a defined cycle duration and variable duty cycle is output at the digital output. The duty cycle is the ratio of pulse duration to cycle duration. In PWM mode, you can control both the duty cycle and the cycle duration.

With pulse width modulation you vary the mean value of the output voltage. Depending on the connected load, you can control the load current or the power with this.

You can specify the pulse duration as one-hundredth of the cycle duration (0 to 100), as one-thousandth (0 to 1, 000), as one ten-thousandth (0 to 10,000) or in S7 analog format.

![Principle of operation](images/88456540427_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Cycle duration |
| ② | Pulse duration |

The pulse duration can be between 0 (no pulse, always off) and full-scale deflection (no pulse, cycle duration always on).

The PWM output can, for example, be used to control the speed of a motor from standstill to full speed or you can use it to control the position of a valve from closed to completely open.

Four pulse generators for PWM and Pulse Train Output (PTO) respectively are available to control high-speed pulse outputs (high-speed output). PTO is used by the technology objects positioning axis, speed axis or synchronized axis. You can assign each pulse generator to either PWM or PTO, but not to both at the same time.

You configure the pulse width modulation (PWM) mode in STEP 7 (TIA Portal).

The pulse width modulation mode has the following functions:

- If the "High-speed output (0.1 A)" option is activated, you can generate a minimum pulse duration of 2 μs at a current of 100 mA. If the "High-speed output (0.1 A)" option is not activated, you can generate a minimum pulse duration of 20 µs at a load &gt; 0.1 A and a minimum pulse duration of 40 µs at a load of ≥ 2mA and a current of maximum 0.5 A. If you use a standard output you can generate a minimum pulse duration of 100 µs at a load &gt; 0.1 A and a minimum pulse duration of 200 µs at a load of ≥ 2mA.
- You can control the pulse output (DQA) of the channel manually via the control and feedback interface.
- You can configure the reaction to CPU STOP. Upon change to CPU STOP, the pulse output (DQA) is set to the configured state.

##### Controller

For the pulse width modulation (PWM) mode, the user program directly accesses the control and feedback interface of the channel.

A reconfiguration via the instructions WRREC/RDREC and parameter assignment data record 128 is supported. You can find additional information on this in the Parameter data records (PWM) section of the respective product manner.

You control the on-load factor of the pulse width via the OUTPUT_VALUE field of the control interface. Pulse width modulation generates continuous pulses based on this value. The cycle duration is adjustable.

![Controller](images/88456476171_DV_resource.Stream@PNG-en-US.png)

##### Starting the output sequence

The control program must output the enable for the output sequence with the help of the software enable (SW_ENABLE 0 → 1). The feedback bit STS_SW_ENABLE indicates that the software enable is pending at the PWM.

If the software enable is activated (positive edge), STS_ENABLE is set. The output sequence runs continuously, as long as SW_ENABLE is set.

> **Note**
>
> **Output control signal TM_CTRL_DQ**
>
> - If TM_CTRL_DQ = 1, the technology function takes over the control and generates pulse sequences at the output PWM DQA.
> - If TM_CTRL_DQ = 0, the application program takes over the control and the user can set the output PWM DQA directly with the control bit SET_DQA.

##### Canceling the output sequence

A deactivation of the software enable (SW_ENABLE = 1 → 0) cancels the current output sequence. The last cycle duration is not completed. STS_ENABLE and the digital output PWM DQA are immediately set to 0.

A renewed pulse output is only possible after a restart of the output sequence.

##### Minimum pulse duration and minimum interpulse period

You assign the minimum pulse duration and the minimum interpulse period with the help of the parameter "Minimum pulse duration".

- A pulse duration, determined by the technology function or the PWM channel, which is shorter than the minimum pulse duration will be suppressed.
- A pulse duration, determined by the technology function or the PWM channel and which is longer than the cycle duration minus the minimum interpulse period will be set to the value of the cycle duration (output continuously enabled).

  ![Minimum pulse duration and minimum interpulse period](images/90593691019_DV_resource.Stream@PNG-de-DE.png)

  | Symbol | Meaning |
  | --- | --- |
  | ① | Cycle duration |
  | ② | Cycle duration minus minimum interpulse period |
  | ③ | Minimum pulse duration |
  | ③ | OUTPUT_VALUE (one tenth of one percent duty cycle) |
  | ③ | Pulse duration |

##### Setting and changing the pulse on-load factor

OUTPUT_VALUE assigns the on-load factor for the current cycle duration. You select the range of the field OUTPUT_VALUE of the control interface with the "Output format" parameter.

- Output format per 100: Value range between 0 and 100   
  Pulse duration = (OUTPUT_VALUE/100) x cycle duration.
- Output format 1/1000: Value range between 0 and 1,000   
  Pulse duration = (OUTPUT_VALUE/1,000) x cycle duration.
- Output format 1/10000: Value range between 0 and 10,000   
  Pulse duration = (OUTPUT_VALUE/10,000) x cycle duration.
- Output format "S7 analog output": Value range between 0 and 27,648   
  Pulse duration = (OUTPUT_VALUE/27 648) x cycle duration.

You assign OUTPUT_VALUE directly via the control program. A new OUTPUT_VALUE is applied at the output when the next positive edge occurs.

##### Setting and changing the cycle duration

- Permanent updating  
  The cycle duration is permanently controlled via the control interface. The MODE_SLOT bit must be set ("1" means permanent updating); LD_SLOT must be set to value 1 ("1" means cycle duration). Set the period value in the field SLOT. The unit is always a microsecond.

  - High-speed output activated: Between 10 μs and 10,000,000 μs (10 s) in the field SLOT
  - High-speed output deactivated: Between 100 μs and 10,000,000 μs (10 s) in the field SLOT
  - Standard output (100 Hz output): Between 10,000 µs (10 ms) and 10,000,000 µs (10 s) in the field SLOT
- Individual updating  
  Set the cycle duration in the configuration parameters. Alternatively, execute an individual updating via the control interface. MODE_SLOT must be deleted ("0" means individual updating); LD_SLOT must be set to value 1 ("1" means cycle duration). Set the cycle duration value in the field SLOT. The unit is always a microsecond.

  - High-speed output activated: Between 10 μs and 10,000,000 μs (10 s) in the parameters
  - High-speed output deactivated: Between 100 μs and 10,000,000 μs (10 s) in the parameters
  - Standard output (100 Hz output): Between 10,000 µs (10 ms) and 10,000,000 µs (10 s) in the parameters

The new cycle duration is applied at the next positive edge of the output.

##### Setting the minimum pulse duration and the minimum interpulse period

You assign the minimum pulse duration and the minimum interpulse period as DWord numerical value between 0 and 10,000,000 μs (10 s) using the channel parameter configuration "Minimum pulse duration".

##### Output signals for pulse width modulation (PWM) mode

| Output signal | Meaning | Value range |
| --- | --- | --- |
| Continuous pulse current at digital output PWM DQA | A pulse is output at the digital output PWM DQA for the set duty cycle and cycle duration. | Continuous pulse current |

#### Operating mode: Frequency output (S7-1500)

In this operating mode you can assign a frequency value with high frequencies more precisely than by using period duration in PWM mode.

A rectangular signal with an assigned frequency and a constant on-load factor of 50 % is generated at the digital output.

The frequency output mode has the following functions:

- If the "High-speed output (0.1 A)" option is activated, you can generate a minimum pulse duration of 2 μs at a current of 100 mA. If the "High-speed output (0.1 A)" option is not activated, you can generate a minimum pulse duration of 20 µs at a load of &gt; 0.1 A and a minimum pulse duration of 40 µs at a load of ≥ 2mA and a current of maximum 0.5 A.   
  If you use a standard output you can generate a minimum pulse duration of 100 µs at a load &gt; 0.1 A and a minimum pulse duration of 200 µs at a load of ≥ 2mA and current of maximum 0.5 A.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | **Minimum** |  |  | **Maximum** |  |  |
| **Standard output** | **High-speed output deactivated** | **High-speed output activated** | **Standard output** | **High-speed output deactivated** | **High-speed output activated** |  |
| **Frequency** | 0.1 Hz |  |  | 100 Hz<sup> 1)</sup> | 10 kHz<sup> 1)</sup> | 100 kHz |
| <sup>1)</sup> Load dependent |  |  |  |  |  |  |

- You can control the pulse output (DQA) of the channel manually via the control and feedback interface.
- You can configure the reaction to CPU STOP. Upon change to CPU STOP, the pulse output (DQA) is set to the configured state.

##### Controller

For the frequency output mode, the user program directly accesses the control and feedback interface of the channel.

A reconfiguration via the instructions WRREC/RDREC and parameter assignment data record 128 is supported. You can find additional information on this in the section "Parameter data records (PWM)" for the respective compact CPU.

![Controller](images/90640869771_DV_resource.Stream@PNG-en-US.png)

##### Starting the output sequence

The control program must initiate the enable for the output sequence with the help of the software enable (SW_ENABLE 0 → 1). The feedback bit STS_SW_ENABLE indicates that the software enable is pending at the pulse generator.

If the software enable is activated (positive edge), STS_ENABLE is set. The output sequence runs continuously, as long as SW_ENABLE is set.

> **Note**
>
> **Output control signal TM_CTRL_DQ**
>
> - If TM_CTRL_DQ = 1, the technology function takes over the control and generates pulse sequences at the output PWM DQA.
> - If TM_CTRL_DQ = 0, the application program takes over the control and the user can set the output PWM DQA directly with the control bit SET_DQA.
>
> **Canceling the output sequence**
>
> A deactivation of the software enable (SW_ENABLE = 1 → 0) during the frequency output cancels the current output sequence. The last period duration is not completed. STS_ENABLE and the digital output PWM DQA are immediately set to 0.
>
> A renewed pulse output is only possible after a restart of the output sequence.

##### Setting and changing the output value (frequency)

You set the frequency with the OUTPUT_VALUE directly with the control program in the control interface. The value is specified in the real format and the unit is always "Hz". The possible range depends on the parameter "High-speed output (0.1 A)" as follows:

- High-speed pulse output deactivated

  - Frequency (OUTPUT_VALUE) 0.1 Hz to 10,000 Hz
- High-speed pulse output activated

  - Frequency (OUTPUT_VALUE) 0.1 Hz to 100,000 Hz
- Standard output (100 Hz output)

  - Frequency (OUTPUT_VALUE): 0.1 Hz to 100,000 Hz

The new frequency is applied at the start of the next period. The new frequency has no effect on the negative edge or the pulse-pause ratio (duty cycle). However, the application can take up to 10 s depending on the previously set frequency.

##### Accuracy of the output frequency

The configured output frequency is out with a frequency dependent accuracy at the digital output PWM DQA. An overview of the accuracy as a function of the used frequency can be found in section "Interconnection overview of outputs" in the product manual of the respective compact CPU.

##### Output signals for frequency output mode

| Output signal | Meaning | Value range |
| --- | --- | --- |
| Continuous pulse current at digital output PWM DQA | A pulse is output at the digital output PWM DQA for the assigned frequency. | Continuous pulse current |

#### Operating mode: PTO (S7-1500)

##### Control

For the four operating modes of the pulse generators (PTO), the pulse output channels are controlled by means of Motion Control using the technology objects TO_SpeedAxis, TO_PositioningAxis and TO_SynchronousAxis. With these operating modes the control and feedback interface of the channels is a partial implementation of the PROFIdrive interface with the standard telegram 3.

A detailed description of the use of Motion Control and its configuration can be found in the online help for Motion Control and in the [S7-1500 Motion Control function manual](http://support.automation.siemens.com/WW/view/en/59381279).

##### Signal types

PTO mode is divided into the following four signal types:

- PTO (Pulse (P) and direction (D)):  
  One output (P) controls the pulses and one output (D) controls the direction. D is 'high' (active) when pulses are generated in the negative direction. D is 'low' (inactive) when pulses are generated in the positive direction.

  ![Signal types](images/92993095691_DV_resource.Stream@PNG-de-DE.png)

  | Symbol | Meaning |
  | --- | --- |
  | ① | Positive direction of rotation |
  | ② | Negative direction of rotation |
- PTO (Count up (A) and count down (B)):   
  One output (A) outputs pulses for positive directions and another output (B) outputs pulses for negative directions.

  ![Signal types](images/91684883339_DV_resource.Stream@PNG-en-US.png)

  | Symbol | Meaning |
  | --- | --- |
  | ① | Positive direction of rotation |
  | ② | Negative direction of rotation |
- PTO (A, B phase-shifted):   
  Output pulses are output by both outputs at the specified velocity, but phase-shifted by 90 degrees. This involves a single pulse output in which the duration of the pulse is the time between two transitions of signal A while signal B is in low state.   
  A positive direction of rotation is generated at a rising edge of signal A while signal B is in low state. A negative direction of rotation is generated at a falling edge of signal A while signal B is in low state.

  | Symbol | Meaning |
  | --- | --- |
  | A precedes B (positive direction of rotation) | A follows B (negative direction of rotation) |
  | ![Signal types](images/91685113867_DV_resource.Stream@PNG-de-DE.png) | ![Signal types](images/91685152139_DV_resource.Stream@PNG-de-DE.png) |
  | Number of pulses | Number of pulses |
- PTO (A, B phase-shifted, quadruple):   
  Output pulses are output by both outputs at the specified velocity, but phase-shifted by 90 degrees. This signal type involves a quadruple pulse output in which each edge transition corresponds to one increment. Therefore, a complete period of signal A contains four increments. In this way, it is possible, for example, to use two outputs, each with 100 kHz signal frequency, to output a control signal that supplies 400 000 increments per second.   
  Whether count pulses are generated in the positive or negative direction of rotation depends on the edge direction of one signal and the logic state of the other signal in each case.

  | Symbol | Meaning |
  | --- | --- |
  | A precedes B (positive direction of rotation) | A follows B (negative direction of rotation) |
  | ![Signal types](images/92714731531_DV_resource.Stream@PNG-de-DE.png) | ![Signal types](images/91685177483_DV_resource.Stream@PNG-de-DE.png) |
  | Number of pulses | Number of pulses |

##### Reaction of PTO channel to a CPU STOP

The PTO channel reacts to a change to CPU STOP by canceling the drive enable (if a drive enable output is configured) and with output of the velocity setpoint 0 at the hardware outputs configured for the signal tracks A and B. The reaction of the PTO channels to a CPU STOP is not configurable.

> **Note**
>
> **Reaction to CPU STOP**
>
> Following a CPU STOP, the hardware outputs assigned for the PTO outputs A and B can switch to signal state 'High' (1) and/or remain there. A switching/remaining of the two hardware outputs to/in signal level 'Low' (0) is not guaranteed.

### Functions (S7-1500)

This section contains information on the following topics:

- [Function: High-speed output (S7-1500)](#function-high-speed-output-s7-1500)
- [Function: Direct control of the pulse output (DQA) (S7-1500)](#function-direct-control-of-the-pulse-output-dqa-s7-1500)

#### Function: High-speed output (S7-1500)

The function "High-speed output (0.1 A)" enhances the signal clock of the digital outputs (DQ0 to DQ7). Less delay, fluctuation, jitter, and shorter rise and fall times, occur at the switching edges.

The function "High-speed output (0.1 A)" is suited for generating pulse signals in a more precise clock, but provides a lower maximum load current.

For the operating modes PWM and frequency output, select the high-speed output of the channel in STEP 7 (TIA Portal). You can also change the parameter assignment during runtime with the help of the program via the data record.

High-speed pulse output (high-speed output) is available for the following operating modes:

- PWM
- Frequency output
- PTO (the pulse output for the PTO mode are always "High-speed output (0.1 A)")

##### High-speed output

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Minimum** |  | **Maximum** |  |
| **High-speed output deactivated** | **High-speed output activated** | **High-speed output deactivated** | **High-speed output activated** |  |
| Pulse duration | 20 µs with load &gt; 0.1 A<sup> 1)</sup>  40 µs with load ≥ 2 mA<sup> 1)</sup> | 2 µs<sup> 1) </sup> | 10,000,000 μs (10 s) |  |
| Period duration | 100 μs <sup>2)</sup> | 10 μs |  |  |
| Frequency | 0.1 Hz |  | 10 kHz <sup>2)</sup> | 100 kHz |
| <sup>1)</sup> A lower value is theoretically possible but, depending on the connected load, the output voltage can no longer be output as complete rectangular pulse   <sup>2)</sup> Load dependent |  |  |  |  |

#### Function: Direct control of the pulse output (DQA) (S7-1500)

##### Direct control of the pulse output (DQA)

In the modes "Pulse width modulation PWM" and "Frequency output", you an set the pulse output (DQA) of a pulse generator directly via the control program. Select the function for the DQ direct control by resetting the output control bit of the PWM channel in the control interface (TM_CTRL_DQ = 0).

The direct control of the pulse output (DQA) can be helpful when commissioning a control system for automation.

When you select the direct control of the pulse output (DQA) during a pulse output sequence, the sequence continues to run in the background so that the output sequence is continued as soon as the channel takes control again (by setting TM_CTRL_DQ = 1).

You assign the status of the pulse output (DQA) with the control bit SET_DQA.

When you set TM_CTRL_DQ = 1, you deselect the direct control of the pulse output (DQA) and the channel takes over the processing. If the output sequence is still running (STS_ENABLE still active), the PWM channel takes over the control of the output again. If TM_CTRL_DQ = 1and STS_ENABLE is not active, the channel of the module also takes over the processing, but then outputs "0" at the output.

> **Note**
>
> **Output signal TM_CTRL_DQ of the PWM channel**
>
> - If TM_CTRL_DQ = 1, the technology function takes over the control and generates pulse sequences at the output PWM DQA.
> - If TM_CTRL_DQ = 0, the user program takes over the control and the user can set the PWM DQA directly with the control bit SET_DQA.

## Basic principles of pulse output (TM PTO) (S7-1500)

This section contains information on the following topics:

- [Pulse Train Output (PTO) (S7-1500)](#pulse-train-output-pto-s7-1500)

### Pulse Train Output (PTO) (S7-1500)

#### Applications

Pulse Train Output is a simple and universal interface between a SIMATIC controller and a drive. PTO is supported worldwide by many stepper and servo drives and is used in many positioning applications, such as for adjustment axes and feed axes.

PTO is also referred to as the pulse/direction interface. The pulse/direction interface comprises two signals. The frequency of the pulse output represents the velocity and the number of pulses that are output for the distance to be traversed. The direction output defines the traversing direction. This means that the position is specified with a precision within one increment. The pulse/direction interface is especially well-suited for operation with the technology objects TO_SpeedAxis, TO_PositioningAxis and TO_SynchronousAxis. TO_MeasuringInput can be used to detect measuring inputs on the drive axis.

#### Control

The control of the pulse output channels is provided above all with S7‑1500 Motion Control by means of the technology objects TO_SpeedAxis, TO_PositioningAxis and TO_SynchronousAxis .

For a detailed description of configuring the technology module with the axis technology objects, see Function Manual S7‑1500T Motion Control, section "Configuring", which is available for download on the [Internet](https://support.industry.siemens.com/cs/ww/en/view/109481326).

#### Signal types

The technology module supports the following four signal types:

> **Note**
>
> The pulse width is permanently set depending on the maximum pulse frequency set for the respective channel.

- PTO (Pulse (P) and direction (D)):  
  One output (P) controls the pulses and one output (D) controls the direction. D is 'high' (active) when pulses are generated in the negative direction. D is 'low' (inactive) when pulses are generated in the positive direction.

  ![Signal types](images/92993095691_DV_resource.Stream@PNG-de-DE.png)

  | Symbol | Meaning |
  | --- | --- |
  | ① | Positive direction of rotation |
  | ② | Negative direction of rotation |
- PTO (count up (A), count down (B)):  
  One output (A) outputs pulses for positive directions and another output (B) outputs pulses for negative directions.

  ![Signal types](images/91684883339_DV_resource.Stream@PNG-en-US.png)

  | Symbol | Meaning |
  | --- | --- |
  | ① | Positive direction of rotation |
  | ② | Negative direction of rotation |
- PTO (A, B phase-shifted):  
  Output pulses are output by both outputs at the specified velocity, but phase-shifted by 90 degrees. This involves a single pulse output in which the duration of the pulse is the time between two transitions of signal A while signal B is in low state.   
  A positive direction of rotation is generated at a rising edge of signal A while signal B is in low state. A negative direction of rotation is generated at a falling edge of signal A while signal B is in low state.

  | Symbol | Meaning |
  | --- | --- |
  | A precedes B (positive direction of rotation) | A follows B (negative direction of rotation) |
  | ![Signal types](images/91685113867_DV_resource.Stream@PNG-de-DE.png) | ![Signal types](images/91685152139_DV_resource.Stream@PNG-de-DE.png) |
  | Position | Position |
- PTO (A, B phase-shifted, quadruple):  
  Output pulses are output by both outputs at the specified velocity, but phase-shifted by 90 degrees. This signal type involves a quadruple pulse output in which each edge transition corresponds to one increment. Therefore, a complete period of signal A contains four increments. In this way, it is possible, for example, to use two outputs, each with 100 kHz signal frequency, to output a control signal that supplies 400 000 increments per second.   
  Whether count pulses are generated in the positive or negative direction of rotation depends on the edge direction of one signal and the logic state of the other signal in each case.

  | Symbol | Meaning |
  | --- | --- |
  | A precedes B (positive direction of rotation) | A follows B (negative direction of rotation) |
  | ![Signal types](images/92714731531_DV_resource.Stream@PNG-de-DE.png) | ![Signal types](images/91685177483_DV_resource.Stream@PNG-de-DE.png) |
  | Position | Position |

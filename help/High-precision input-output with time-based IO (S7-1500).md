---
title: "High-precision input/output with time-based IO (S7-1500)"
package: TFTimebasedMain1500enUS
topics: 28
devices: [S7-1500, S7-1500T]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# High-precision input/output with time-based IO (S7-1500)

This section contains information on the following topics:

- [Time-based IO basics (S7-1500)](#time-based-io-basics-s7-1500)
- [Configuring and parameter assignment (S7-1500)](#configuring-and-parameter-assignment-s7-1500)
- [Programming (S7-1500)](#programming-s7-1500)
- [Using the technology module (S7-1500)](#using-the-technology-module-s7-1500)

## Time-based IO basics (S7-1500)

This section contains information on the following topics:

- [Using Time-based IO (S7-1500)](#using-time-based-io-s7-1500)
- [Time behavior of Time-based IO (S7-1500)](#time-behavior-of-time-based-io-s7-1500)
- [System environment (S7-1500)](#system-environment-s7-1500)
- [Hardware requirements (S7-1500)](#hardware-requirements-s7-1500)
- [Configuration software requirements (S7-1500)](#configuration-software-requirements-s7-1500)
- [Technical implementation (S7-1500)](#technical-implementation-s7-1500)

### Using Time-based IO (S7-1500)

Many processes in a plant require a relatively precise reproducibility as far as time is concerned. The reproducibility can be optimized to a limited extent by shorter CPU cycle times. The use of high-precision input/output with Time-based IO provides a more accurate reproducibility than the one that can be achieved by optimizing the CPU cycle time. An additional advantage of Time-based IO is the independence from the time scale of the application cycle.

Below is a selection of typical areas of application that can benefit from this technology.

#### Defined response times

An output signal that responds with a precise delay time that is independent of the application cycle can be output by adding a specified time to the time stamp of an edge at the digital input.

#### Length measurement

The length of a product passing by can be determined by the difference between two input time stamps and an associated travel speed.

#### Cam controller

The ongoing movement can be extrapolated from a synchronous position information (for example, from a counter module or an axis). Based on this result, the time of a switching position (cam position) is calculated and transferred to the TIO module (output). This way the switch event takes place at the required position.

#### Dosing

By specifying a switch-on and a switch-off edge to a time-controlled digital output, a valve can be opened for a specific time and the amount of liquid can be dosed accordingly.

### Time behavior of Time-based IO (S7-1500)

This section contains information on the following topics:

- [Time behavior of standard technology (S7-1500)](#time-behavior-of-standard-technology-s7-1500)
- [Time-based IO properties (S7-1500)](#time-based-io-properties-s7-1500)

#### Time behavior of standard technology (S7-1500)

The time behavior of the inputs/outputs depends on the following factors for standard technology:

- CPU program (program structure)
- Bus cycle times (fieldbus, backplane bus)
- Cycle time of the I/O modules
- Internal cycle time of sensors/actuators

A deterministic statement as to

- when an input event (e.g., sensor signal) has taken place
- when the output event has an effect on the input event (e.g., output switches)

will become inaccurate due to the time factors listed above.

![Figure](images/63775024779_DV_resource.Stream@PNG-en-US.png)

#### Time-based IO properties (S7-1500)

##### Time-controlled I/O functionality

Time-based IO stands for time-based processing of I/O signals. All input signals are referred to one time (TIO_Time). The input signals receive the time stamp t1. After signal processing, the output event can also be linked with the TIO_Time and output at the required time. Output takes place at time t2.

Here an example for Time-based IO:

![Time-controlled I/O functionality](images/63531740555_DV_resource.Stream@PNG-en-US.png)

##### Independence and focus of Time-based IO

The shared time basis (TIO_Time) of all components involved is the basis for Time-based IO. By using TIO_Time, the accuracy of the output with Time-based IO does not depend on:

- CPU program (program structure)
- Bus cycle times (fieldbus, backplane bus)
- Cycle time of the I/O modules

The focus of Time-based IO is not on the I/O response time but on the predictability (determinism) of I/O signals. With Time-based IO, it is possible to respond to an input signal with an output signal within a defined time. Keep in mind the system-dependent minimum response time when using Time-based IO.

Time-based IO stands for:

- I/O functionalities executed with high precision
- I/O processes with time stamp

##### Accuracy

Accuracy is crucial for the performance capability of Time-based IO.

The accuracy is a property of the TIO modules and indicates the deviation with which the required response is achieved. For Time-based IO, the accuracy and reproducibility of the response is in the millisecond range.

##### Response time

In addition to a very high accuracy, a minimum response time to an input event can result depending on the configuration.

The response time is the time between the input event and the required output event.

For the minimum response time:

3 × application cycle T<sub>APP</sub>

### System environment (S7-1500)

#### Introduction

Possible system configurations with PROFINET for the use of Time-based IO are shown below.

#### Use with STEP 7 (TIA Portal)

![Use with STEP 7 (TIA Portal)](images/126172771723_DV_resource.Stream@PNG-en-US.png)

### Hardware requirements (S7-1500)

#### Introduction

The properties of the hardware components required for Time-based IO are listed below. You will also find specific modules as an example.

#### Requirements

| Component | Properties | Examples |
| --- | --- | --- |
| CPU | Isochronous mode/ PROFINET IO IRT: provides defines response time and high-precision plant behavior. | - CPU 1511-1 PN |
| ET 200 interface module | Supports isochronous mode | - ET 200SP with  IM 155-6 PN HF (as of firmware V2.1) - ET 200MP with  IM 155-5 PN HF |
| I/O module | TIO module | - ET 200SP:  TM Timer DIDQ 10x24V - ET 200MP: TM Timer DIDQ 16x24V (as of firmware V1.0.1) |

---

**See also**

[Requirements (S7-1500)](#requirements-s7-1500)

### Configuration software requirements (S7-1500)

#### Introduction

Below is a list of the software versions which support the "Time-based IO" function.

#### Requirements

| Configuration software | Requirements | Supported hardware components | Additional information |
| --- | --- | --- | --- |
| STEP 7 (TIA Portal) V16 and above | PROFINET IO IRT or isochronous mode on the backplane bus | - S7‑1500 automation system - ET 200SP and ET 200MP distributed I/O systems - TM Timer DIDQ 16x24V - TM Timer DIDQ 10x24V | STEP 7 (TIA Portal) online help |

Additional information on isochronous mode is available in the [Isochronous mode](http://support.automation.siemens.com/WW/view/en/49948856) and [PROFINET with STEP 7](https://support.industry.siemens.com/cs/ww/en/view/109755401) manuals.

#### TIO instructions

The TIO instructions are specific function blocks for use of Time-based IO. The following TIO instructions are available:

- TIO_SYNC
- TIO_DI
- TIO_DI_ONCE
- TIO_DQ

### Technical implementation (S7-1500)

#### Introduction

The information below will help you better understand the core aspects of Time-based IO and find out which SIMATIC functions are used to implement the described aspects.

#### Synchronization of involved modules (shared time basis)

The Time-based IO technology uses isochronous mode for all involved stations.

Isochronous mode enables multiple TIO modules to be synchronized to a shared time basis. The basis of the shared time basis for the TIO modules is the relative time TIO_Time.

Additional information on isochronous mode is available in the [Isochronous mode](http://support.automation.siemens.com/WW/view/en/49948856) and [PROFINET with STEP 7](https://support.industry.siemens.com/cs/ww/en/view/109755401) manuals.

#### TIO_Time

The TIO_Time is the central time basis to which all time stamps refer.

TIO_Time has the following properties:

- Shared time basis for all TIO modules which are synchronized with the TIO instruction TIO_SYNC.
- The time starts counting again with each CPU startup.
- The TIO_Time has data type LTime (e.g. LT#14s830ms652us315ns).
- All valid time stamps refer to TIO_Time:

  - Input time stamps of the TIO modules are converted to the TIO_Time in the TIO instructions TIO_DI and TIO_DI_ONCE.
  - In the TIO instruction TIO_DQ, output time stamps are converted to the output time stamp of the TIO modules.
- The value of TIO_TIME corresponds to the current time with respect to TIO instructions and is updated with the call of TIO_SYNC. If you want an output to relate not to a previous input time stamp but to the current time, you can use the value of TIO_TIME as basis for the output time stamp. Example: Output of an edge in 20 ms: TIO_DQ.TimeStampRE=TIO_SYNC_DATA.TIO_TIME+LT#20ms)

#### TIO instructions in the isochronous OB

The TIO instructions must be called in a "Synchronous Cycle" or "MC-PostServo" OB.

You can find additional information in the chapter Programming.

> **Note**
>
> The TIO instructions also support geared down isochronous mode. With a clock reduction ratio, the application cycle is longer than the send clock.

> **Note**
>
> The TIO instructions must be called in an "MC-PreServo" OB.
>
> If you use an OB of the "MC-PostServo" type, you can decide separately for each TIO model whether it is used with Motion Control technology objects or with TIO instructions.
>
> If you call the TIO instructions in an "MC-PostServo" type OB, you need to use the IPO model and also cannot use any reduction ratio.
>
> Calling TIO instructions in an OB of the type "MC-PostServo" with reduction ratio "MC-Servo" can result in incorrect calculation of time stamps.

#### Modes for updating the process image

In isochronous mode, you can influence the order of the update of the process image partition of the input and output data. In doing so, you can select the following program execution models:

- IPO model (application cycle factor = 1)
- OIP model (application cycle factor >= 1)

The abbreviations I, P, O stand for the following processes: I = Input, P= Processing, O = Output.

Additional information on the application cycle factor is available in the [PROFINET with STEP 7](http://support.automation.siemens.com/WW/view/en/49948856) Manual.

#### IPO model (application cycle factor = 1)

The user program is started after the delay time. Start by updating the corresponding process image partition of the inputs in the user program by calling the SYNC_PI system instruction. Processing is started next (for example, calculation of the time stamps). The corresponding process image partition of the outputs is updated at the end of the user program in the CPU by SYNC_PO.

![IPO model (application cycle factor = 1)](images/126175917963_DV_resource.Stream@PNG-en-US.png)

**Properties of the IPO model:**

- Supports shorter response times
- The application cycle must not be greater than the send clock.

  This gives the application less time than with the OIP model.

#### OIP model (application cycle factor >= 1)

The user program is started after the delay time. In PIP_Mode 0, the TIO_SYNC instruction updates the process image. In the other modes, you start by updating the corresponding process image partition of the outputs in the user program by calling the SYNC_PO system instruction. As a result, the output data that was calculated in the previous network cycle will become active during the next network cycle (T<sub>O</sub>). Next the corresponding process image partition of the inputs is updated in the CPU by SYNC_PI. Processing starts after the data is transmitted (for example, calculation of the time stamps).

![OIP model (application cycle factor >= 1)](images/126176447755_DV_resource.Stream@PNG-en-US.png)

**Properties of the OIP model:**

- The response time is longer than with the IPO model.
- It is one application cycle longer than permitted by the send clock.

  This gives the application more time than with the IPO model.

#### Influence of accuracy

To estimate the accuracy you need the accuracy of

- TIO module
- Sensor/ actuator

Consult the data sheets of the respective module regarding the accuracy value.

You have to add the individual jitters of the TIO modules and the sensors/actuators. You can neglect any other influencing factors.

---

**See also**

Programming of Time-based IO

## Configuring and parameter assignment (S7-1500)

This section contains information on the following topics:

- [Requirements (S7-1500)](#requirements-s7-1500)
- [Settings for Time-based IO (S7-1500)](#settings-for-time-based-io-s7-1500)

### Requirements (S7-1500)

#### Introduction

You need additional software components to use Time-based IO. You must also have created the standard configuration for your project.

Below you will learn more about the standard configuration for Time-based IO.

#### Requirements

In STEP 7 (TIA Portal):

- The project has been created.
- The CPU has been created and the parameters are assigned.
- Automation system and modules have been created and the parameters have been assigned.
- When using an ET 200 station: The connection has been created and the parameters are assigned via PROFINET.
- A "Synchronous Cycle" or "MC-PostServo" type OB has been created.

---

**See also**

[System environment (S7-1500)](#system-environment-s7-1500)
  
[Configuration software requirements (S7-1500)](#configuration-software-requirements-s7-1500)

### Settings for Time-based IO (S7-1500)

Below you will find an overview of which settings have to be made for which components of Time-based IO.

Overview of settings for Time-based IO

| Component | Where adjustable<sup>1</sup> | Properties to be set | Additional information |
| --- | --- | --- | --- |
| When using an ET 200 station: PROFINET subnet | Properties of the PROFINET subnet > sync domain | Create sync domain or edit properties of sync domain | - [PROFINET function manual](http://support.automation.siemens.com/WW/view/en/49948856) - Online help in the STEP 7 (TIA Portal) information system |
| Specify devices of the sync domain:  - Specify CPU as sync master. - Specify ET 200 interface module as sync slave with RT class "IRT". |  |  |  |
| S7-1500 station | Properties of the PROFINET interface > isochronous communication | Enable isochronous mode | - [Function Manual Isochronous Mode](https://support.industry.siemens.com/cs/ww/en/view/109755401) - [PROFINET function manual](http://support.automation.siemens.com/WW/view/en/49948856) - Manual Technology Module  [TM Timer DIDQ 16x24V](http://support.automation.siemens.com/WW/view/en/95153313) - Manual Technology Module  [TM Timer DIDQ 10x24V](http://support.automation.siemens.com/WW/view/en/95153951) - Online help in the STEP 7 (TIA Portal) information system |
| ET 200 station |  |  |  |
| TIO module | Properties of the TIO module > I/O addresses | Enable isochronous mode |  |
| Properties of the TIO module > I/O addresses | Assign or create a "Synchronous Cycle" or "MC-PostServo" type OB |  |  |
| Properties of the TIO module > I/O addresses | Assignment of I/O addresses to the process image partition (e.g., PIP1) |  |  |
| Properties of the TIO module > Basic parameters | Configure "Module use from the user program" |  |  |
| Properties of the TIO module > Basic parameters/Channel parameters | For TM Timer DIDQ 10x24V: If required, assign parameters for Configuration "Use input/output individually" |  |  |
| Parameter assignment for use of Timer DI and Timer DQ |  |  |  |
| Isochronous OB (Synchronous Cycle or MC-PostServo) | Properties of the Isochronous OB > Isochronous mode | Adjust application cycle, if necessary |  |

<sup>1</sup> Describes the topic area in the configuration software.

#### Setting for Time-based IO

If you have no special response time requirements, the following setting is suitable as a starting point:

- Send clock: 2 ms
- Application cycle: 4 ms
- Assignment to the process image partition: PIP1
- PIP_Mode: 0 (OIP model)

#### FAQ

For more information, see the following FAQs in the Siemens Industry Online Support:

- [Entry ID 109738186](https://support.industry.siemens.com/cs/ww/en/view/109738186)
- [Entry ID 109736374](https://support.industry.siemens.com/cs/ww/en/view/109736374)

---

**See also**

Programming of Time-based IO

## Programming (S7-1500)

This section contains information on the following topics:

- [Overview of instructions (S7-1500)](#overview-of-instructions-s7-1500)
- [Programming of Time-based IO (S7-1500)](#programming-of-time-based-io-s7-1500)

### Overview of instructions (S7-1500)

#### Introduction

Time-based IO is used with special instructions (TIO instructions). The TIO_SYNC TIO instruction is responsible for synchronizing all involved TIO modules and creates a unique time basis (TIO_Time) to which all actions are referenced.

Additional instructions undertake the reading in of process input signals with associated time stamps and/or the time-controlled output of process output signals.

> **Note**
>
> The TIO instructions are helpful for general time-based IO applications. For special applications, such as cam controllers, there are also separate technology objects, for example, TO_CamOutput.

> **Note**
>
> The TIO instructions use the time stamp functions of the TIO modules. The other functions of the TIO modules can be used independently of the TIO instructions in applications.

#### TIO instructions

| Instruction | Short description |
| --- | --- |
| [TIO_SYNC](Time-based%20IO%20%28S7-1500%29.md#tio_sync-synchronizing-tio-modules-s7-1500) | Synchronizes the TIO modules and provides the time basis for Time-based IO |
| [TIO_DI](Time-based%20IO%20%28S7-1500%29.md#tio_di-reading-in-edges-at-digital-input-and-associated-time-stamps-s7-1500) | Detects the edges at the digital input (Timer DI) and supplies the associated time stamp |
| [TIO_DI_ONCE](Time-based%20IO%20%28S7-1500%29.md#tio_di_once-reading-in-edges-once-at-the-digital-input-and-associated-time-stamps-s7-1500) | - Detects the edges at the digital input (timer DI) once and provides the associated time stamp - Controls a timer DI channel which is configured as an edge-triggered enable for another channel. |
| [TIO_DQ](Time-based%20IO%20%28S7-1500%29.md#tio_dq-output-edges-time-controlled-at-the-digital-output-s7-1500) | Outputs time-controlled edges at the digital output (Timer DQ) |

### Programming of Time-based IO (S7-1500)

#### Introduction

To use Time-based IO, the TIO instructions must be called in an isochronous OB. The application can also run in another OB. This allows you to shorten the runtime of the isochronous OB.

You need the following TIO instructions according to the required task:

| TIO module | TIO instructions |
| --- | --- |
| - TM Timer DIDQ 16x24V - TM Timer DIDQ 10x24V | - Per digital input, one TIO_DI or TIO_DI_ONCE for read-in - Per digital output, one TIO_DQ for output - One TIO_SYNC (for up to eight TIO modules) |

This section below describes the programming of the CPU for Time-based IO.

#### Requirements

Hardware configuration in STEP 7 (TIA Portal):

- The TIO modules are assigned to an isochronous network.
- The TIO modules are assigned to a shared process image partition.
- The process image partition is assigned to an isochronous OB.
- The TIO modules are configured for use with instructions from the "Time-based IO" library.

Additional information on configuration of Time-based IO is available in the section [Settings for Time-based IO](#settings-for-time-based-io-s7-1500).

#### Procedure

1. Create a TIO instruction, TIO_SYNC, in the isochronous OB.
2. Connect all TIO modules to be synchronized at the TIO_SYNC TIO instruction using parameters HWID_1 to HWID_8.

   The HWID can be found in the hardware configuration under "Properties > System constants".
3. Set the data update mode at the TIO_SYNC instruction at the PIP_Mode input parameter.

   The description of the modes is available in the chapter [Technical implementation](#technical-implementation-s7-1500).

   The parameter assignment of the TIO_SYNC TIO instruction is complete.
4. For the following instructions, note the call sequence depending on the selected value for PIP_Mode:

   ![Procedure](images/63088949899_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/63088949899_DV_resource.Stream@PNG-en-US.png)
5. Add the TIO instructions for read-in/output required for your application in the isochronous OB.
6. At the TIO instructions for read-in/output, interconnect in each case the input/output TIO_SYNC_Data with the same name output at the TIO_SYNC.
7. At the TIO instructions for read-in/output, assign parameters for the input parameters HWID (see "Properties > System constants" in hardware configuration) and Channel.  
   The Time-based IO functionality is successfully programmed.
8. Interconnect the Time-based IO functionality with your application, such as evaluating the read-in time stamp in a step sequencer in another OB.
9. If TIO_SYNC does not automatically read out the send clock: Define the send clock manually, e.g. in OB100.
10. Compile and download the entire project to the CPU.

**Note**

Use of symbolic constants is generally preferred instead of absolute numerical values when interconnecting.

#### Result

You have completed programming the use of Time-based IO.

#### FAQ

For more information, see the following FAQs in the Siemens Industry Online Support:

- [Entry ID 109738186](https://support.industry.siemens.com/cs/ww/en/view/109738186)
- [Entry ID 109736374](https://support.industry.siemens.com/cs/ww/en/view/109736374)

## Using the technology module (S7-1500)

This section contains information on the following topics:

- [Configuration and parameter assignment of TIO-Modul (S7-1500)](#configuration-and-parameter-assignment-of-tio-modul-s7-1500)
- [TIO-Modul Online & Diagnostics (S7-1500)](#tio-modul-online-diagnostics-s7-1500)

### Configuration and parameter assignment of TIO-Modul (S7-1500)

This section contains information on the following topics:

- [Adding a technology module to hardware configuration (S7-1500)](#adding-a-technology-module-to-hardware-configuration-s7-1500)
- [Open Hardware configuration (HWCN) (S7-1500)](#open-hardware-configuration-hwcn-s7-1500)
- [Basic parameters (S7-1500)](#basic-parameters-s7-1500)
- [Channel parameters (S7-1500)](#channel-parameters-s7-1500)

#### Adding a technology module to hardware configuration (S7-1500)

##### Requirements

- The project has been created.
- The CPU has been created.
- The ET 200 distributed I/O has been created.

##### Procedure

1. Open the device configuration of the CPU or IM.
2. Select a module rack.
3. Select the technology module from the module catalog:  
   "Technology modules > Time‑based IO > Technology module > Article number".
4. Drag the technology module to the required slot in the module rack.

##### Result

The new technology module is displayed under "Local modules" or "Distributed I/O" in the project tree.

#### Open Hardware configuration (HWCN) (S7-1500)

##### Opening via the project tree

Proceed as follows:

1. Open the "Local modules" or "Distributed I/O" folder in the project tree.
2. Double-click the technology module in the project tree.

##### Opening from the device view

Proceed as follows:

1. Open the device configuration of the CPU or IM.
2. Select the device view.
3. Click on the technology module.

#### Basic parameters (S7-1500)

##### Channel configuration (TM Timer DIDQ 16x24V)

You use the channel configuration to specify for TM Timer DIDQ 16x24V which combination of digital inputs and outputs you would like to use.

You can select from the following configurations:

- 0 inputs, 16 outputs (default)
- 3 inputs, 13 outputs
- 4 inputs, 12 outputs
- 8 inputs, 8 outputs

> **Note**
>
> Unused outputs are available as encoder supply.
>
> Unused inputs are available as digital input without technology function. You specify the input delay of an input together with the parameters of the corresponding output channel.

##### PWM period

Use this parameter to specify the period duration for the signals at the digital outputs with "PWM" mode.

You can select from the following period durations:

- 10 ms (default)
- 5 ms
- 2 ms
- 1 ms
- 0.5 ms
- 0.2 ms

> **Note**
>
> You specify the pulse-pause ratio in the control interface. The pulse-pause ratio is a percentage and is evaluated with an accuracy of about 3 %.

##### Reaction to CPU STOP

Use this parameter to specify the reaction of the technology module to a CPU STOP.

You can select from the following options:

| Reaction to CPU STOP | Meaning |
| --- | --- |
| Output substitute value (default) | The technology module outputs the configured substitute values at the digital outputs until the next CPU STOP-RUN transition.   The technology module is returned to its startup state after a STOP-RUN transition: If you are using counters, the counting values are set to 0 and the digital outputs switch according to the parameter assignment and the setpoints. |
| Keep last value | The technology module outputs the values at the digital outputs that were valid when the transition to STOP took place until the next CPU STOP-RUN transition. The last valid period duration with the last valid pulse-pause ratio is output for a configured pulse width modulation until the next STOP-RUN transition.  The technology module is returned to its startup state after a STOP-RUN transition: If you are using counters, the counting values are set to 0 and the digital outputs switch according to the parameter assignment and the setpoints. |

##### Enable diagnostic interrupts

The technology module triggers diagnostic interrupts in the event of certain errors. The technology module can trigger additional diagnostic interrupts when you enable the diagnostic interrupts. These diagnostic interrupts are processed in an interrupt OB.

You use this parameter to specify whether or not the technology module triggers the additional diagnostic interrupts when the respective errors occur.

See the device manual for the technology module to find out which errors during operation can trigger a diagnostic interrupt. The diagnostic interrupts are not enabled in the default setting.

##### Module use from the user program

With this parameter, you define whether you use the module with technology objects of Motion Control or with instructions from the library "Time-based IO“ (Instructions > Technology).

#### Channel parameters (S7-1500)

This section contains information on the following topics:

- [Overview (S7-1500)](#overview-s7-1500)
- [DQ group (S7-1500)](#dq-group-s7-1500)
- [DQ/DI group (S7-1500)](#dqdi-group-s7-1500)
- [DI group (S7-1500)](#di-group-s7-1500)

##### Overview (S7-1500)

The digital inputs and outputs are divided into groups with group-specific parameters in the channel parameters.

Each group is one of the following group types:

- [DQ group](#dq-group-s7-1500)
- [DQ/DI group](#dqdi-group-s7-1500)
- [DI group](#di-group-s7-1500)

The available group types for a TM Timer DIDQ 16x24V depend on the channel configuration in the basic parameters.

##### DQ group (S7-1500)

You can configure the following parameters for the digital outputs of a DQ group:

###### Operating mode

Use this parameter to specify the technological function of the respective digital output .

You can select from the following options:

| Operating mode | Meaning |
| --- | --- |
| Timer DQ (default) | The technology module outputs edges at the respective digital output at defined times.  This setting uses Time‑based IO and does not require isochronous mode.  If you are using the SIMOTION control system, use this setting for a cam application. |
| Oversampling | The respective digital output outputs 32 states at regular intervals for each application cycle (for example, OB61). The 32 states are specified by means of the control interface.  This setting requires isochronous mode. |
| PWM | The technology module switches the respective digital output with the period duration specified in the basic parameters and the pulse-pause ratio from the control interface.  The pulse-pause ratio is a percentage and is evaluated with an accuracy of about 3 %. |

###### Substitute value

With this parameter you specify for the "Output substitute value" behavior which value the technology module is to output at the respective digital output in the event of a CPU STOP.

The default setting is "0".

###### High-speed output (0.1 A)

Use this parameter to specify whether or not the respective digital output works as fast push-pull or as sourcing output.

You can select from the following options:

| Option | Meaning |
| --- | --- |
| Activated (default) | The digital output works as fast push-pull switch and can carry a rated load current of 0.1 A. A push-pull switch is alternately switched to DC 24 V and ground. This makes for very fast edges. |
| Deactivated | The digital output works as 24 V sourcing output in reference to M and can carry a rated load current of 0.5 A. |

###### Invert DI/DQ(TM Timer DIDQ 16x24V)

You can invert the 24 V signals at the digital output and at the corresponding digital input together in order to adapt them to the process.

The two signals are not inverted in the default setting.

###### Invert DQ

You can invert the 24 V signal at the digital output to adapt it to the process.

The signal is not inverted in the default setting.

###### Input delay

By configuring the input delay, you suppress interference at the digital input, which is available as input without technology function. Signals with a pulse duration below the configured input delay are suppressed.

You can choose from the following input delays:

- No  
  (input delay of 4 μs, minimum pulse width of 3 μs)
- 0.05 ms
- 0.1 ms (default)
- 0.4 ms
- 0.8 ms

> **Note**
>
> If you select the "None" or "0.05 ms" option, you have to use shielded cables for connection of the digital inputs. To increase the accuracy of the time stamp function, we recommend the use of shielded cables even for longer input delays.

> **Note**
>
> The input delay is subject to a tolerance that you can find in the technical specifications of the technology module manual.

##### DQ/DI group (S7-1500)

A DQ/DI group consists of a digital output and one or two digital inputs. You can configure the following parameters for the group:

###### Configuration DQ/DI group

You use this parameter to specify if the DI is used as enable input for the DQ.

You can select from the following options:

| Option | Meaning | Additional option-specific parameters |
| --- | --- | --- |
| Timer DQ with enable input (default) | The technology module outputs edges time-controlled at the DQ. The DQ is enabled by the DI. The operating mode of the DQ is "Timer DQ" and cannot be changed.  This setting uses Time‑based IO and does not require isochronous mode.  If you are using the SIMOTION control system, use this setting for a cam application. | Substitute value  High-speed output (0.1 A)  Invert DI/DQ(TM Timer DIDQ 16x24V)  Invert DQ(TM Timer DIDQ 10x24V)  Input delay  HW enable |
| Use input/output individually | The DQ and the DI are configured and used independent of one another. | Operating mode (DQ)  Substitute value  High-speed output (0.1 A)  Invert DI/DQ(TM Timer DIDQ 16x24V)  Invert DQ(TM Timer DIDQ 10x24V)  Operating mode (DI)  Input delay  Invert DI |

###### Configuration DQ/DI group (DQ2/DI2/DI3 of the TM Timer DIDQ 10x24V)

This parameter is used to specify how DQ2, DI2 and DI3 of the TM Timer DIDQ 10x24V are used.

You can select from the following options:

| Option | Meaning | Additional option-specific parameters |
| --- | --- | --- |
| Incremental encoder (A, B phase-shifted) (default) | DQ2 is used individually.  An incremental encoder with phase-shifted 24V A and B signals is connected to DI2 and DI3. The counter (DI2) always evaluates both signals four times. | Operating mode (DQ)  Substitute value  High-speed output (0.1 A)  Invert DQ  Invert counting direction |
| Timer-DI2 with enable input DI3 | Time stamps are detected at defined edges at DI2. DI2 is enabled by DI3. The operating mode of DI2 is "Timer DI" and cannot be changed.  This setting uses Time‑based IO and does not require isochronous mode.  If you are using the SIMOTION control system, use this setting for a probe application. | Operating mode (DQ)  Substitute value  High-speed output (0.1 A)  Invert DQ  Input delay  Invert DI  HW enable |
| Timer DQ2 with enable input DI2 | The technology module outputs edges time-controlled at DQ2. DQ2 is enabled by DI2. The operating mode of the DQ2 is "Timer DQ" and cannot be changed.  This setting uses Time‑based IO and does not require isochronous mode.  If you are using the SIMOTION control system, use this setting for a cam application. | Substitute value  High-speed output (0.1 A)  Invert DQ  Input delay  HW enable  Operating mode (DI)  Invert DI |
| Use input/output individually | The DQ and the DI are configured and used independent of one another. | Operating mode (DQ)  Substitute value  High-speed output (0.1 A)  Invert DQ  Operating mode (DI)  Input delay  Invert DI |

###### Operating mode (DQ)

Use this parameter to specify the technological function of the digital output.

You can select from the following options:

| Operating mode | Meaning |
| --- | --- |
| Timer DQ (default) | The technology module outputs edges at defined times at DQ.   This setting uses Time‑based IO and does not require isochronous mode.  If you are using the SIMOTION control system, use this setting for a cam application. |
| Oversampling | The technology module outputs 32 states consecutively at regular intervals at DQ for each application cycle (for example OB61) . The 32 states are specified by means of the control interface.  This setting requires isochronous mode. |
| PWM | The technology module switches the DQ with the period duration specified in the basic parameters and the pulse-pause ratio from the control interface.  The pulse-pause ratio is a percentage and is evaluated with an accuracy of about 3 %. |

###### Substitute value

This parameter lets you specify which value the technology module is to output at the DQ in the event of a CPU STOP under "Output substitute value".

The default setting is "0".

###### High-speed output (0.1 A)

Use this parameter to specify whether or not the DQ works as fast push-pull or as sourcing output.

You can select from the following options:

| Option | Meaning |
| --- | --- |
| Activated (default) | The DQ works as fast push-pull switch and can carry a rated load current of 0.1 A. A push-pull switch is alternately switched to DC 24 V and ground. This makes for very fast edges. |
| Deactivated | The DQ works as 24 V sourcing output in reference to M and can carry a rated load current of 0.5 A. |

###### Invert DI/DQ(TM Timer DIDQ 16x24V)

You can invert the 24 V signals of the DQ and the corresponding DI together in order to adapt them to the process.

The two signals are not inverted in the default setting.

###### Invert DQ(TM Timer DIDQ 10x24V)

You can invert the 24 V signal of the DQ to adapt it to the process.

The signal is not inverted in the default setting.

###### Input delay

You use this parameter to suppress signal interference at the digital inputs. Changes to the signal are only detected if they remain stable for longer than the configured input delay time.

You can choose from the following input delays:

- No  
  (input delay of 4 μs, minimum pulse width of 3 μs)
- 0.05 ms
- 0.1 ms (default)
- 0.4 ms
- 0.8 ms

The input delay has no effect on the function for signal evaluation set at the digital input:

| Function | Influence of the input delay |
| --- | --- |
| Timer DI | The detected time stamp is moved by the input delay. |
| Incremental encoder (A, B phase-shifted) | The counter value that was valid at time T<sub>i</sub> minus the input delay is returned. |
| Counters |  |
| Oversampling | The detected states are moved together by the input delay. |

> **Note**
>
> If you select the "None" or "0.05 ms" option, you have to use shielded cables for connection of the digital inputs. To increase the accuracy of the time stamp function, we recommend the use of shielded cables even for longer input delays.

> **Note**
>
> The input delay is subject to a tolerance that you can find in the technical specifications of the technology module manual.

###### HW enable

You use this parameter to specify if the Timer DQ is enabled by the level or the edges at DI.

You can select from the following options:

| Enable | Meaning | Additional option-specific parameters |
| --- | --- | --- |
| Level-triggered (default) | The DQ is enabled by the DI level. | Level selection for HW enable |
| Edge-triggered | This setting is available when you use the SIMOTION control system. | — |

The figure below shows an example of the output of positive and negative edges at DQ0 with enable of DI0 by the high level of DI1:

![HW enable](images/66492392075_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| R | Specified time of a positive DQ0-edge |
| F | Specified time of a negative DQ0-edge |

###### Level selection for HW enable

You use this parameter to specify the level at which the DQ is enabled for a level-triggered HW enable.

You can select from the following options:

| Level | Meaning |
| --- | --- |
| Active with high level  (default) | The DQ is enabled if the DI is set. |
| Active with low level | The DQ is enabled if the DI is not set. |

###### Operating mode (DI)

Use this parameter to specify the technological function of the DIm+1.

You can select from the following options:

| Operating mode | Meaning |
| --- | --- |
| Counters | An incremental encoder or sensor is connected to the DI. The counter counts the positive or negative edges at the DI.  See the device manual for the technology module to find out which digital inputs can be used as counter. |
| Timer DI (default) | Time stamps are read in for associated time stamps at the DI at defined edges.   This setting uses Time‑based IO and does not require isochronous mode.  If you are using the SIMOTION control system, use this setting for a probe application. |
| Oversampling | The technology reads the status of the DI for each application cycle (for example, OB61) at 32 points in time at regular intervals. The 32 states are returned at the same time.  This setting requires isochronous mode. |

###### Invert DI

You can invert the 24 V signal of the DI to adapt it to the process.

The signal is not inverted in the default setting.

##### DI group (S7-1500)

A DI group consists of two neighboring digital inputs DIm and DIm+1. You can configure the following parameters for the group:

###### Configuration DI group

Use this parameter to specify how the group is used.

You can select from the following options:

| Option | Meaning | Additional option-specific parameters |
| --- | --- | --- |
| Incremental encoder (A, B phase-shifted) (default) | An incremental encoder with phase-shifted 24V A and B signals is connected to both digital inputs. The counter of the DI group always evaluates both signals four times. | Inverting the count direction |
| Timer-DI with enable input | Time stamps are detected at defined edges at DIm. DIm is enabled by DIm+1. The operating mode of DIm is "Timer DI" and cannot be changed.  This setting uses Time‑based IO and does not require isochronous mode.  If you are using the SIMOTION control system, use this setting for a probe application. | Input delay  Invert  HW enable |
| Use inputs individually | The two digital inputs are configured and used independent of one another. | Operating mode  Input delay |

###### Inverting the count direction

You can invert the count direction to adapt it to the process. The technology module inverts the B signal of the incremental encoder at DIm+1. The respective counter then interprets the edges of both signals as backward pulses.

The figure below shows an example of counter pulses in forward and backward direction:

![Inverting the count direction](images/65726213003_DV_resource.Stream@PNG-en-US.png)

The count direction is not inverted in the default setting.

###### Input delay

You use this parameter to suppress signal interference at the digital inputs. Changes to the signal are only detected if they remain stable for longer than the configured input delay time.

You can choose from the following input delays:

- No  
  (input delay of 4 μs, minimum pulse width of 3 μs)
- 0.05 ms
- 0.1 ms (default)
- 0.4 ms
- 0.8 ms

The input delay has no effect on the function for signal evaluation set at the digital input:

| Function | Influence of the input delay |
| --- | --- |
| Timer DI | The detected time stamp is moved by the input delay. |
| Incremental encoder (A, B phase-shifted) | The counter value that was valid at time T<sub>i</sub> minus the input delay is returned. |
| Counters |  |
| Oversampling | The detected states are moved together by the input delay. |

> **Note**
>
> If you select the "None" or "0.05 ms" option, you have to use shielded cables for connection of the digital inputs. To increase the accuracy of the time stamp function, we recommend the use of shielded cables even for longer input delays.

> **Note**
>
> The input delay is subject to a tolerance that you can find in the technical specifications of the technology module manual.

###### Invert

You can invert the 24 V signal of the DIm to adapt it to the process.

The signal is not inverted in the default setting.

###### HW enable

You use this parameter to specify whether the Timer DI is enabled by the level or the edges at   
DIm+1.

You can select from the following options:

| Enable | Meaning | Additional option-specific parameters |
| --- | --- | --- |
| Level-triggered (default) | The DIm is enabled by the DIm+1 level. | Level selection for HW enable |
| Edge-triggered | This setting is available when you use the SIMOTION control system. | — |

The figure below shows an example for the detection of time stamps at positive and negative edges with enable of the DI0 through the high level of the DI1:

![HW enable](images/66492396043_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| R | Associated time stamp detected at positive DI0-edge |
| F | Associated time stamp detected at negative DI0 edge |

###### Level selection for HW enable

You use this parameter to specify the level at which DIm is enabled for a level-triggered HW enable.

You can select from the following options:

| Level | Meaning |
| --- | --- |
| Active with high level  (default) | DIm is enabled if the DIm+1 is set. |
| Active with low level | DIm is enabled if the DIm+1 is not set. |

###### Operating mode

Use this parameter to specify the technological function of the respective digital input.

You can select from the following options:

| Operating mode | Meaning | Additional option-specific parameters |
| --- | --- | --- |
| Counters | An incremental encoder or sensor is connected to DIm. The counter counts the positive or negative edges at DIm.  See the device manual for the technology module to find out which digital inputs can be used as counter. | Signal evaluation for counters |
| Timer DI (default) | The associated time stamps are read in at the respective digital input at defined edges.   This setting uses Time‑based IO and does not require isochronous mode.  If you are using the SIMOTION control system, use this setting for a probe application. | Invert |
| Oversampling | The technology module detects the status of the respective digital input for each application cycle (for example, OB61) at 32 points in time at regular intervals. The 32 states are returned at the same time.  This setting requires isochronous mode. | Invert |

###### Signal evaluation for counters

You use this parameter to specify if the counter counts the positive or the negative edges at DIm.

The positive edges are counted in the default setting.

### TIO-Modul Online & Diagnostics (S7-1500)

This section contains information on the following topics:

- [Displaying and evaluating diagnostics (S7-1500)](#displaying-and-evaluating-diagnostics-s7-1500)

#### Displaying and evaluating diagnostics (S7-1500)

The online and diagnostics view enables hardware diagnostics. You can also

- Obtain information on the technology module (e.g., Firmware version and serial number)
- Execute a firmware update if required

##### Procedure

To open the display editor for the diagnostic functions, follow these steps:

1. Open the device configuration of the CPU or IM.
2. Select the device view.
3. Right-click on the technology module and select "Online & Diagnostics".
4. Select the required display in the diagnostics navigation.

##### Additional information

Additional information on the diagnostic alarms and possible remedies can be found in the technology module device manual.

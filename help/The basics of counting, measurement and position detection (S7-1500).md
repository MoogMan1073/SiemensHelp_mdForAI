---
title: "The basics of counting, measurement and position detection (S7-1500)"
package: TFCountMainTM15enUS
topics: 78
devices: [S7-1500, S7-1500T]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# The basics of counting, measurement and position detection (S7-1500)

This section contains information on the following topics:

- [Overview of modules and properties (S7-1500)](#overview-of-modules-and-properties-s7-1500)
- [Basics of counting, measuring and position input (TM Count, TM PosInput, Compact CPU) (S7-1500)](#basics-of-counting-measuring-and-position-input-tm-count-tm-posinput-compact-cpu-s7-1500)
- [Basics of counting (TM Timer DIDQ) (S7-1500)](#basics-of-counting-tm-timer-didq-s7-1500)
- [Basics of counting (digital modules) (S7-1500)](#basics-of-counting-digital-modules-s7-1500)
- [Basics of counting (SIMATIC Drive Controller) (S7-1500)](#basics-of-counting-simatic-drive-controller-s7-1500)

## Overview of modules and properties (S7-1500)

### Modules for the S7‑1500 and ET 200MP systems

The table below summarizes the performance features of the modules for counting, measuring and position input for the S7-1500 and ET 200MP systems.

| Property | S7-1500 / ET 200MP |  |  |  |
| --- | --- | --- | --- | --- |
| Technology module |  |  | Digital input module |  |
| TM Count 2x24V | TM PosInput 2 | TM Timer DIDQ 16x24V | DI 32x24VDC HF  DI 16x24VDC HF |  |
| Number of counters | 2 | 2 | 4<sup>1</sup> | 2 |
| Use of counters can be activated/deactivated | — | — | X | X |
| Maximum signal frequency | 200 kHz | 1 MHz | 50 kHz | 3 kHz |
| Maximum count frequency for incremental encoders with [quadruple evaluation](#signal-evaluation-of-incremental-signals-s7-1500) | 800 kHz | 4 MHz | 200 kHz | — |
| Maximum counting range | [32 bits](#counting-with-incremental-or-pulse-encoder-s7-1500) | [32 bits](#counting-with-incremental-or-pulse-encoder-s7-1500) | [32 bits](#counting-with-incremental-encoder-s7-1500) | [32 bits](#counting-with-pulse-encoders-s7-1500) |
| Maximum [position value range](#position-input-with-ssi-absolute-encoder-s7-1500) | — | 32 bits | — | — |
| 24 V incremental encoder connection | [X](#24-v-or-ttl-count-signals-s7-1500) | — | [X](#24-v-count-signals-s7-1500) | — |
| 24 V pulse encoder connection | [X](#24-v-or-ttl-count-signals-s7-1500) | — | [X](#24-v-count-signals-s7-1500) | [X](#24-v-count-signals-s7-1500-1) |
| [RS422 or TTL incremental and pulse encoder](#rs422-count-signals-s7-1500) connection | — | X | — | — |
| [SSI absolute encoder](#ssi-signals-s7-1500) connection | — | X | — | — |
| [Position detection for Motion Control](#position-detection-for-motion-control-s7-1500) | X | X | — | — |
| 5 V encoder supply | — | X | — | — |
| 24 V encoder supply | X | X | X | — |
| Number of additional digital inputs per counter | 3 | 2 | 0 | 0 |
| Number of physical digital outputs per counter | 2 | 2 | 0 | 0 |
| Number of logical digital outputs per counter | 2 | 2 | 0 | 1 |
| Software gate | [X](#software-gate-s7-1500) | [X](#software-gate-s7-1500) | — | [X](#software-gate-s7-1500-1) |
| Hardware gate | [X](#hardware-gate-s7-1500) | [X](#hardware-gate-s7-1500) | — | — |
| [Capture function (Latch)](#capture-latch-s7-1500) | X | X | — | — |
| [Synchronization](#synchronization-s7-1500) | X | X | — | — |
| Comparison functions | [X](#comparison-values-s7-1500) | [X](#comparison-values-s7-1500) | — | [X](#comparison-values-s7-1500-1) |
| [Hysteresis](#hysteresis-s7-1500) | X | X | — | — |
| [Frequency, velocity and period duration measurement](#measured-value-determination-s7-1500) | X | X | — | — |
| Isochronous mode support | [X](#clock-synchronization-tm-count-and-tm-posinput-s7-1500) | [X](#clock-synchronization-tm-count-and-tm-posinput-s7-1500) | [X](#isochronous-mode-s7-1500) | [X](#isochronous-mode-s7-1500-1) |
| Support of diagnostic interrupts for sensor signals | [X](#interrupts-s7-1500) | [X](#interrupts-s7-1500) | — | — |
| Hardware interrupt support | [X](#interrupts-s7-1500) | [X](#interrupts-s7-1500) | — | [X](#interrupts-s7-1500-1) |
| Configurable filter for count signals and digital inputs | X | X | — | X |
| <sup>1</sup> The number of available counters is dependent on the channel configuration. In order to use four counters, you must choose the use of eight inputs in the channel configuration. If you choose the use of three inputs, you can use one counter. Other channel configurations do not allow any counter use. |  |  |  |  |

| Property | S7-1500 |  |  |  |
| --- | --- | --- | --- | --- |
| Digital input module |  | Compact CPU | SIMATIC Drive Controller |  |
| DI 16x24VDC HS | DI 16xNAMUR HF | CPU 1511C-1 PN  CPU 1512C-1 PN | CPU 1504D TF  CPU 1507D TF |  |
| Number of counters | 4 | 4 | 6 | 8 |
| Use of counters can be activated/deactivated | X | X | X | X |
| Maximum signal frequency | 20 kHz | 20 kHz | 100 kHz | 32 kHz |
| Maximum count frequency for incremental encoders with [quadruple evaluation](#signal-evaluation-of-incremental-signals-s7-1500) | — | — | 400 kHz | — |
| Maximum counting range | [32 bits](#counting-with-pulse-encoders-s7-1500) | [32 bits](#counting-with-pulse-encoders-s7-1500) | [32 bits](#counting-with-incremental-or-pulse-encoder-s7-1500) | Event counter: 16 bits  Period duration measurement: 32 bits |
| 24 V incremental encoder connection | — | — | [X](#24-v-or-ttl-count-signals-s7-1500) | — |
| 24 V pulse encoder connection | [X](#24-v-count-signals-s7-1500-1) | X | [X](#24-v-or-ttl-count-signals-s7-1500) | [X](#basics-of-counting-simatic-drive-controller-s7-1500) |
| [Position detection for Motion Control](#position-detection-for-motion-control-s7-1500) | — | — | X | — |
| 24 V encoder supply | X | — | X | Via 24 V supply |
| NAMUR encoder supply | — | X | — | — |
| Number of additional digital inputs per counter | 2 | 2 | 2 | 0 |
| Number of physical digital outputs per counter | 0 | 0 | 1 | 0 |
| Number of logical digital outputs per counter | 1 | 1 | 2 | 0 |
| Software gate | X | X | [X](#software-gate-s7-1500) | — |
| Hardware gate | [X](#counting-once-with-hardware-gate-s7-1500) | [X](#counting-once-with-hardware-gate-s7-1500) | [X](#hardware-gate-s7-1500) | — |
| [Capture function (Latch)](#capture-latch-s7-1500) | — | — | X | — |
| [Synchronization](#synchronization-s7-1500) | — | — | X | — |
| Comparison functions | [X](#comparison-values-s7-1500-1) | [X](#comparison-values-s7-1500-1) | [X](#comparison-values-s7-1500) | — |
| [Hysteresis](#hysteresis-s7-1500) | — | — | X | — |
| Frequency measurement | — | — | X | — |
| Period duration measurement | — | — | X | X |
| Velocity measurement | — | — | X | — |
| Isochronous mode support | [X](#isochronous-mode-s7-1500-1) | [X](#isochronous-mode-s7-1500-1) | — | X |
| Support of diagnostic interrupts for sensor signals | — | — | [X](#interrupts-s7-1500) | — |
| Hardware interrupt support | [X](#interrupts-s7-1500-1) | [X](#interrupts-s7-1500-1) | [X](#interrupts-s7-1500) | — |
| Configurable filter for digital inputs | X | X | X | X |

### Modules for the ET 200SP system

The following table provides an overview of the performance features of the modules for counting, measuring and position input for the ET 200SP system.

| Property | ET 200SP |  |  |  |
| --- | --- | --- | --- | --- |
| Technology module |  |  | Digital input module |  |
| TM Count 1x24V | TM PosInput 1 | TM Timer DIDQ 10x24V | DI 8x24VDC HS |  |
| Number of counters | 1 | 1 | 3<sup>1</sup> | 4 |
| Use of counters can be activated/deactivated | — | — | X | X |
| Maximum signal frequency | 200 kHz | 1 MHz | 50 kHz | 10 kHz |
| Maximum count frequency for incremental encoders with [quadruple evaluation](#signal-evaluation-of-incremental-signals-s7-1500) | 800 kHz | 4 MHz | 200 kHz | — |
| Maximum counting range | [32 bits](#counting-with-incremental-or-pulse-encoder-s7-1500) | [32 bits](#counting-with-incremental-or-pulse-encoder-s7-1500) | [32 bits](#counting-with-incremental-encoder-s7-1500) | [32 bits](#counting-with-pulse-encoders-s7-1500) |
| Maximum [position value range](#position-input-with-ssi-absolute-encoder-s7-1500) | — | 32 bits | — | — |
| 24 V incremental encoder connection | [X](#24-v-or-ttl-count-signals-s7-1500) | — | [X](#24-v-count-signals-s7-1500) | — |
| 24 V pulse encoder connection | [X](#24-v-or-ttl-count-signals-s7-1500) | — | [X](#24-v-count-signals-s7-1500) | [X](#24-v-count-signals-s7-1500-1) |
| [RS422 or TTL incremental and pulse encoder](#rs422-count-signals-s7-1500) connection | — | X | — | — |
| [SSI absolute encoder](#ssi-signals-s7-1500) connection | — | X | — | — |
| [Position detection for Motion Control](#position-detection-for-motion-control-s7-1500) | X | X | — | — |
| 24 V encoder supply | X | X | X | X |
| Number of additional digital inputs per counter | 3 | 2 | 0 | 1 |
| Number of physical digital outputs per counter | 2 | 2 | 0 | 0 |
| Number of logical digital outputs per counter | 2 | 2 | 0 | 1 |
| Software gate | [X](#software-gate-s7-1500) | [X](#software-gate-s7-1500) | — | [X](#software-gate-s7-1500-1) |
| Hardware gate | [X](#hardware-gate-s7-1500) | [X](#hardware-gate-s7-1500) | — | [X](#hardware-gate-s7-1500-1) |
| [Capture function (Latch)](#capture-latch-s7-1500) | X | X | — | — |
| [Synchronization](#synchronization-s7-1500) | X | X | — | — |
| Comparison functions | [X](#comparison-values-s7-1500) | [X](#comparison-values-s7-1500) | — | [X](#comparison-values-s7-1500-1) |
| [Hysteresis](#hysteresis-s7-1500) | X | X | — | — |
| [Frequency, velocity and period duration measurement](#measured-value-determination-s7-1500) | X | X | — | — |
| Isochronous mode support | [X](#clock-synchronization-tm-count-and-tm-posinput-s7-1500) | [X](#clock-synchronization-tm-count-and-tm-posinput-s7-1500) | [X](#isochronous-mode-s7-1500) | [X](#isochronous-mode-s7-1500-1) |
| Support of diagnostic interrupts for sensor signals | [X](#interrupts-s7-1500) | [X](#interrupts-s7-1500) | — | — |
| Hardware interrupt support | [X](#interrupts-s7-1500) | [X](#interrupts-s7-1500) | — | — |
| Configurable filter for count signals and digital inputs | X | X | — | X |
| <sup>1</sup> One counter for incremental encoder (A, B phase-shifted) and two counters for pulse encoder |  |  |  |  |

### Modules for the ET 200AL system

The following table provides an overview of the performance features of the modules for counting, measuring and position input for the ET 200AL system.

| Property | ET 200AL |
| --- | --- |
| Digital input/digital output module |  |
| DIQ 16x24VDC/0.5A 8xM12 |  |
| Number of counters | 4 |
| Use of counters can be activated/deactivated | X |
| Maximum signal frequency | 2 kHz |
| Maximum counting range | 32 bits |
| 24 V incremental encoder connection | — |
| 24 V pulse encoder connection | X |
| 24 V encoder supply | X |
| Number of additional digital inputs per counter | 2 |
| Number of physical digital outputs per counter | 1 |
| Number of logical digital outputs per counter | 1 |
| Software gate | X |
| Hardware gate | X |
| Capture function (Latch) | — |
| Synchronization | — |
| Comparison functions | X |
| Frequency, velocity and period duration measurement | — |
| Isochronous mode support | — |
| Support of diagnostic interrupts for sensor signals | X |
| Hardware interrupt support | X |
| Configurable filter digital inputs | X |

### Modules for the ET 200eco PN M12-L system

The following table provides an overview of the performance features of the modules for counting, measuring and position detection for the ET 200eco PN M12-L system.

| Property | ET 200eco PN M12-L |
| --- | --- |
| Technology module |  |
| TM PosInput 2 |  |
| Number of counters | 2 |
| Use of counters can be activated/deactivated | — |
| Maximum signal frequency | 200 kHz<sup>1</sup> or 1 MHz<sup>2</sup> |
| Maximum count frequency for incremental encoders with [quadruple evaluation](#signal-evaluation-of-incremental-signals-s7-1500) | 800 kHz<sup>1</sup> or 4 MHz<sup>2</sup> |
| Maximum counting range | [32 bits](#counting-with-incremental-or-pulse-encoder-s7-1500) |
| Maximum [position value range](#position-input-with-ssi-absolute-encoder-s7-1500) | 32 bits |
| 24 V incremental encoder connection | [X](#24-v-or-ttl-count-signals-s7-1500) |
| 24 V pulse encoder connection | [X](#24-v-or-ttl-count-signals-s7-1500) |
| [RS422 incremental and pulse encoder](#rs422-count-signals-s7-1500) connection | X |
| [SSI absolute encoder](#ssi-signals-s7-1500) connection | X |
| [Position detection for Motion Control](#position-detection-for-motion-control-s7-1500) | X |
| 5 V encoder supply | — |
| 24 V encoder supply | X |
| Number of additional digital inputs per counter | 2 |
| Number of physical digital outputs per counter | 2 |
| Number of logical digital outputs per counter | 2 |
| Software gate | [X](#software-gate-s7-1500) |
| Hardware gate | [X](#hardware-gate-s7-1500) |
| [Capture function (Latch)](#capture-latch-s7-1500) | X |
| [Synchronization](#synchronization-s7-1500) | X |
| Comparison functions | [X](#comparison-values-s7-1500) |
| [Hysteresis](#hysteresis-s7-1500) | X |
| [Frequency, velocity and period duration measurement](#measured-value-determination-s7-1500) | X |
| Isochronous mode support | [X](#clock-synchronization-tm-count-and-tm-posinput-s7-1500) |
| Support of diagnostic interrupts for sensor signals | [X](#interrupts-s7-1500) |
| Hardware interrupt support | — |
| Configurable filter for count signals and digital inputs | X |
| <sup>1</sup> Value with 24 V incremental and pulse encoders   <sup>2</sup> Value with RS422 incremental and pulse encoders |  |

## Basics of counting, measuring and position input (TM Count, TM PosInput, Compact CPU) (S7-1500)

This section contains information on the following topics:

- [Convention (S7-1500)](#convention-s7-1500)
- [Overview of applications (S7-1500)](#overview-of-applications-s7-1500)
- [Recording of count signals (S7-1500)](#recording-of-count-signals-s7-1500)
- [Behavior at the counting limits (S7-1500)](#behavior-at-the-counting-limits-s7-1500)
- [Gate control with incremental or pulse encoder (S7-1500)](#gate-control-with-incremental-or-pulse-encoder-s7-1500)
- [Capture (Latch) (S7-1500)](#capture-latch-s7-1500)
- [Synchronization (S7-1500)](#synchronization-s7-1500)
- [Comparison values (S7-1500)](#comparison-values-s7-1500)
- [Measured value determination (S7-1500)](#measured-value-determination-s7-1500)
- [Hysteresis (S7-1500)](#hysteresis-s7-1500)
- [Interrupts (S7-1500)](#interrupts-s7-1500)
- [Position detection for Motion Control (S7-1500)](#position-detection-for-motion-control-s7-1500)
- [Encoder signals (S7-1500)](#encoder-signals-s7-1500)
- [Signal evaluation of incremental signals (S7-1500)](#signal-evaluation-of-incremental-signals-s7-1500)
- [Clock synchronization (TM Count and TM PosInput) (S7-1500)](#clock-synchronization-tm-count-and-tm-posinput-s7-1500)

### Convention (S7-1500)

**Technology module**: We use the term "technology module" in this documentation both for the technology modules TM Count and TM PosInput and the technology component of the compact CPUs.

### Overview of applications (S7-1500)

#### Introduction

The technology module is configured and assigned parameters using the configuration software.

The operation and control of the technology module functions is effected either via the technology object or through the application program via the control and feedback interface.

#### System environment for TM Count and TM PosInput

The technology modules can be used in the following system environments:

| Application scenarios | Components required | Configuration software | In the user program |
| --- | --- | --- | --- |
| Central operation with an S7-1500 CPU or 151xSP CPU | - S7-1500 automation system or ET 200SP CPU - Technology module | STEP 7 (TIA Portal):  Operating with "Counting and measurement" technology object  - [Device configuration with hardware configuration](Using%20the%20module%20%28S7-1500%29.md#configuring-a-module-s7-1500) - Parameter setting with High_Speed_Counter or SSI_Absolute_Encoder technology object | For incremental / pulse encoders:  High_Speed_Counter instruction for the technology object  For SSI absolute encoder:  SSI_Absolute_Encoder instruction for the technology object |
| STEP 7 (TIA Portal):  Position input for "Motion Control" technology object  - [Device configuration with hardware configuration](Using%20the%20module%20%28S7-1500%29.md#configuring-a-module-s7-1500) - [Parameter setting with axis and measuring input technology object](Using%20the%20module%20%28S7-1500%29.md#module-parameters-position-input-for-motion-control-s7-1500) | Instructions for "Motion Control" technology object |  |  |
| STEP 7 (TIA Portal):  Manual operation (without technology object)  - [Device configuration and parameter setting](Using%20the%20module%20%28S7-1500%29.md#configuring-a-module-s7-1500) with hardware configuration | Direct access to control and feedback interface of the technology module in the I/O data |  |  |
| Distributed operation with a S7-1500 CPU | - S7-1500 automation system - ET 200 distributed I/O system - Technology module  or  - S7-1500 automation system - Technology module of the ET 200eco PN M12-L distributed I/O system | STEP 7 (TIA Portal):  Operating with "Counting and measurement" technology object  - [Device configuration with hardware configuration](Using%20the%20module%20%28S7-1500%29.md#configuring-a-module-s7-1500) - Parameter setting with High_Speed_Counter or SSI_Absolute_Encoder technology object | For incremental / pulse encoders:  High_Speed_Counter instruction for the technology object  For SSI absolute encoder:  SSI_Absolute_Encoder instruction for the technology object |
| STEP 7 (TIA Portal):  Position input for "Motion Control" technology object  - [Device configuration with hardware configuration](Using%20the%20module%20%28S7-1500%29.md#configuring-a-module-s7-1500) - [Parameter setting with axis and measuring input technology object](Using%20the%20module%20%28S7-1500%29.md#module-parameters-position-input-for-motion-control-s7-1500) | Instructions for "Motion Control" technology object |  |  |
| STEP 7 (TIA Portal):  Manual operation (without technology object)  - [Device configuration and parameter setting](Using%20the%20module%20%28S7-1500%29.md#configuring-a-module-s7-1500) with hardware configuration | Direct access to [control and feedback interface](Using%20the%20module%20%28S7-1500%29.md#control-and-feedback-interface-tm-count-tm-posinput-s7-1500) of the technology module in the I/O data |  |  |
| Distributed operation with an S7-1200 CPU | - S7‑1200 automation system - ET 200 distributed I/O system - Technology module  or  - S7‑1200 automation system - Technology module of the ET 200eco PN M12-L distributed I/O system | STEP 7 (TIA Portal):   [Device configuration and parameter setting](Using%20the%20module%20%28S7-1500%29.md#configuring-a-module-s7-1500) with hardware configuration | Direct access to [control and feedback interface](Using%20the%20module%20%28S7-1500%29.md#control-and-feedback-interface-tm-count-tm-posinput-s7-1500) of the technology module in the I/O data |
| Distributed operation with a S7-300/400 CPU | - S7-300/400 automation system - ET 200 distributed I/O system - Technology module  or  - S7-300/400 automation system - Technology module of the ET 200eco PN M12-L distributed I/O system | STEP 7 (TIA Portal):   [Device configuration and parameter setting](Using%20the%20module%20%28S7-1500%29.md#configuring-a-module-s7-1500) with hardware configuration  STEP 7:  Device configuration and parameter settings with HSP or GSD file | Direct access to [control and feedback interface](Using%20the%20module%20%28S7-1500%29.md#control-and-feedback-interface-tm-count-tm-posinput-s7-1500) of the technology module in the I/O data |
| Distributed operation in a third-party system | - Third-party automation system - ET 200 distributed I/O system - Technology module  or  - Third-party automation system - Technology module of the ET 200eco PN M12-L distributed I/O system | Third-party configuration software:  Device configuration and parameter settings with GSD file | Direct access to [control and feedback interface](Using%20the%20module%20%28S7-1500%29.md#control-and-feedback-interface-tm-count-tm-posinput-s7-1500) of the technology module in the I/O data |

#### System environment for a Compact CPU

The Compact CPUs can be used in the following system environments:

| Application scenarios | Components required | Configuration software | In the user program |
| --- | --- | --- | --- |
| Central operation with a S7-1500 Compact CPU | - S7-1500 automation system - Compact CPU | STEP 7 (TIA Portal):  Operating with "Counting and measurement" technology object  - [Device configuration with hardware configuration](Using%20the%20module%20%28S7-1500%29.md#configuring-a-module-s7-1500) - Parameter setting with High_Speed_Counter technology object | High_Speed_Counter instruction for the technology object |
| STEP 7 (TIA Portal):  Position input for "Motion Control" technology object  - [Device configuration with hardware configuration](Using%20the%20module%20%28S7-1500%29.md#configuring-a-module-s7-1500) - [Parameter setting with axis and measuring input technology object](Using%20the%20module%20%28S7-1500%29.md#module-parameters-position-input-for-motion-control-s7-1500) | Instructions for "Motion Control" technology object |  |  |
| STEP 7 (TIA Portal):  Manual operation (without technology object)  - [Device configuration and parameter setting](Using%20the%20module%20%28S7-1500%29.md#configuring-a-module-s7-1500) with hardware configuration | Direct access to control and feedback interface of the technology module in the I/O data |  |  |

#### Parameter assignment options

In an S7-1500 system, you have two options for parameter assignment and control of technology module functions:

- Configuration using the technology object and control using the associated instruction  
  Access to the control and feedback interface of the technology module takes place through the technology object.
- Parameter setting via hardware configuration  
  The control and feedback interface of the technology module is accessed using direct access to the I/O data.

#### Configuration via technology object

For central and distributed use, we recommend the convenient, graphics-assisted configuration using a technology object. A detailed description of this configuration can be found in section High_Speed_Counter technology object or SSI_Absolute_Encodertechnology object.

You specify the "Operation with technology object "Counting and measuring"" in the device configuration of the technology module: see section [Operating mode](Using%20the%20module%20%28S7-1500%29.md#operating-mode-s7-1500).

You can assign the technology module and counting channel in the basic parameters of the technology object: see section [Basic parameters](Use%20technology%20object%20High_Speed_Counter%20%28S7-1500%29.md#basic-parameters-s7-1500).

#### Parameter setting via hardware configuration

You specify the "Manual operation (without technology object)" in the device configuration of the technology module: see section [Operating mode](Using%20the%20module%20%28S7-1500%29.md#operating-mode-s7-1500).

Additional support for parameter setting via hardware configuration is available in the context-sensitive help for the parameters in STEP 7 (TIA Portal). A description of the control and feedback interface is available in the following sections:

- [Assignment of the control interface](Using%20the%20module%20%28S7-1500%29.md#assignment-of-the-control-interface-s7-1500)
- [Assignment of the feedback interface](Using%20the%20module%20%28S7-1500%29.md#assignment-of-the-feedback-interface-s7-1500)

### Recording of count signals (S7-1500)

This section contains information on the following topics:

- [Counting with incremental or pulse encoder (S7-1500)](#counting-with-incremental-or-pulse-encoder-s7-1500)
- [Position input with SSI absolute encoder (S7-1500)](#position-input-with-ssi-absolute-encoder-s7-1500)

#### Counting with incremental or pulse encoder (S7-1500)

Counting refers to the recording and adding up of events. The counters of the technology modules capture and evaluate pulse and incremental signals. The count direction can be specified using encoder or pulse signals or through the user program.

You can control counting processes using the digital inputs of the technology module. You can switch the digital outputs exactly at defined counter values, regardless of the user program.

You can configure the response of the counters using the functionalities described below.

##### Counter limits

The counter limits define the counter value range used. The counter limits are configurable and can be modified during runtime using the user program.

The highest counter limit that can be set is 2147483647 (2<sup>31</sup>–1). The lowest counter limit that can be set is –2147483648 (–2<sup>31</sup>).

You can configure the response of the counter at the counter limits:

- Continue or stop counting upon violation of a counter limit (automatic gate stop)
- Set counter value to start value or to opposite counter limit upon violation of a counter limit

##### Start value

You can configure a start value within the counter limits. The start value can be modified during runtime by the user program.

The technology module can, as configured, set the current counter value to the start value upon synchronization, upon Capture function activation, upon violation of a counter limit or when the gate is opened.

##### Gate control

Opening and closing the hardware gate and software gate defines the period of time during which the counting signals are captured.

The hardware gate is controlled externally via a digital input of the technology module. The software gate is controlled via the user program. The hardware gate can be enabled through parameter assignment. The software gate (bit in the control interface of the cyclic I/O data) cannot be disabled.

##### Capture (Latch)

You can configure an external reference signal edge that triggers the saving of the current counter value or position value as a Capture value. The following external signals can trigger the Capture function:

- Rising or falling edge of a digital input
- Both edges of a digital input
- Rising edge of the N signal at the encoder input

When using a digital input, you can specify whether counting is to continue from the current counter value or from the start value after the Capture function. When using the rising edge of the N signal at the encoder input, counting is to continue from the current counter value after the Capture function. The use of a digital input and the use of the N signal are not mutually exclusive for the Capture function.

The parameter "Frequency of the Capture function" determines if the function is executed for each configured edge or only once after each enable.

##### Measuring input

If you use the [position input for Motion Control](#position-detection-for-motion-control-s7-1500), you can use the "Measuring input" technology object to execute a measuring input function with a hardware digital input.

##### Synchronization

You can configure an external reference signal edge to load the counter with the specified start value. The following external signals can load the counter with the start value:

- Rising or falling edge of a digital input
- Rising edge of signal N at the encoder input
- Rising edge of signal N at the encoder input depending on the level of the assigned digital input

The parameter "Frequency of synchronization" determines whether the function is executed for each configured edge or only once after each enable.

##### Hysteresis

You can specify hysteresis for the comparison values, within which a digital output is prevented from switching again. An encoder can come to a standstill at a specific position, and slight movements may make the counter value fluctuate around this position. If a comparison value or a counting limit lies within this fluctuation range, the corresponding digital output will be switched on and off with corresponding frequency if hysteresis is not used. The hysteresis prevents these unwanted switching operations.

#### Position input with SSI absolute encoder (S7-1500)

##### Description

You can use the TM PosInput technology modules with an SSI absolute encoder for position detection. The technology module reads the position value via a synchronous serial interface from the SSI absolute encoder and makes it available to the controller.

You can switch the digital outputs of the technology module exactly at defined position values, regardless of the user program. Position input with an SSI absolute encoder does not involve gate control. Due to system constraints, synchronization is not possible with an SSI absolute encoder.

##### Gray- and dual-code

Gray-code and dual-code SSI absolute encoders are supported.

##### Capture (Latch)

You can configure one or both edges of a digital input that triggers a saving of the current position value as Capture value.

The parameter "Frequency of the Capture function" determines if the function is executed for each configured edge or only once after each enable.

##### Measuring input

If you use the [position input for Motion Control](#position-detection-for-motion-control-s7-1500), you can use the "Measuring input" technology object to execute a measuring input function with a hardware digital input.

##### Hysteresis

You can specify hysteresis for the comparison values, within which a digital output is prevented from switching again. An encoder can come to a standstill at a specific position, and slight movements may make the position value fluctuate around this position. If a comparison value or a limit lies within this fluctuation range, the corresponding digital output is switched on and off with corresponding frequency if hysteresis is not used. The hysteresis prevents these unwanted switching operations.

##### Range for position value

You can specify a frame length of 10 bits to 40 bits for the SSI absolute encoder. The configurable bit numbers of the LSB and the MSB of the position value in the frame define the value range. The technology module can read a position value with a maximum length of 32 bits and communicate it to the controller.

If you use an encoder with a position value length of up to 31 bits, the position value is handled unsigned as a positive value and can assume values between 0 and 2<sup>(MSB-LSB+1)</sup>-1. If you use an encoder with a position value length of 32 bits, the MSB of the position value corresponds to the sign and the position value can assume values between –2147483648 and 2147483647. If you use a 32 bit position value for the comparison function, the position value is interpreted as DINT.

##### Complete SSI frame

Instead of having a measured variable returned, you can choose to have the least significant 32 bits of the current unprocessed SSI frame returned. This provides you with encoder-specific additional bits, such as error bits, in addition to the position value. If the SSI frame is shorter than 32 bits, the complete SSI frame is returned right-aligned and the top unused bits are returned with "0" in the feedback interface.

### Behavior at the counting limits (S7-1500)

#### Violation of a counting limit

The high counting limit is violated when the current counter value is equal to the high counting limit and another upward count pulse is received. The counter low limit is violated when the current counter value is equal to the counter low limit and another downward count pulse is received.

The appropriate status bit is set in the feedback interface in the event of limit violation:

| Counting limit violated | Status bit |
| --- | --- |
| High counting limit | EVENT_OFLW is set |
| Low counting limit | EVENT_UFLW is set |

You can reset the status bits with RES_EVENT .

You can configure whether or not and from which counter value counting is to continue following counting limit violation.

> **Note**
>
> The high counting limit and the start value define the value range of the counter:
>
> Value range of the counter = (high limit – start value) + 1

#### Examples

The figure below shows an example for terminating the counting process (automatic gate stop) after an overflow and setting the counter to the start value:

![Examples](images/42673550731_DV_resource.Stream@PNG-en-US.png)

The figure below shows an example for continuing the counting process after an overflow and setting the counter to the start value:

![Examples](images/42818603659_DV_resource.Stream@PNG-en-US.png)

The figure below shows an example for terminating counting after an overflow and setting the counter to the opposite counting limit:

![Examples](images/42820721419_DV_resource.Stream@PNG-en-US.png)

The figure below shows an example for continuing the counting process after an overflow and setting the counter to the opposite counting limit:

![Examples](images/42821068555_DV_resource.Stream@PNG-en-US.png)

### Gate control with incremental or pulse encoder (S7-1500)

This section contains information on the following topics:

- [Gate functions (S7-1500)](#gate-functions-s7-1500)
- [Software gate (S7-1500)](#software-gate-s7-1500)
- [Hardware gate (S7-1500)](#hardware-gate-s7-1500)
- [Internal gate (S7-1500)](#internal-gate-s7-1500)
- [Counter behavior at gate start (S7-1500)](#counter-behavior-at-gate-start-s7-1500)

#### Gate functions (S7-1500)

Many applications require counting processes to be started or stopped in accordance with other events. In such cases, counting is started and stopped using the gate function.

The technology modules have two gates for each channel. These define the resulting internal gate:

- Software gate
- Hardware gate

#### Software gate (S7-1500)

The software gate of the channel is opened and closed with the [control bit](Using%20the%20module%20%28S7-1500%29.md#assignment-of-the-control-interface-s7-1500) SW_GATE. The status of the software gate is indicated by the [feedback bit](Using%20the%20module%20%28S7-1500%29.md#assignment-of-the-feedback-interface-s7-1500) STS_SW_GATE .

#### Hardware gate (S7-1500)

The hardware gate is optional. You open and close the hardware gate by means of signals at the configured digital inputs of the channel.

> **Note**
>
> The configured input filters delay the control signal of the digital input.

The status of a DIm digital input is indicated by the respective [feedback bit](Using%20the%20module%20%28S7-1500%29.md#assignment-of-the-feedback-interface-s7-1500) STS_DIm .

##### Level-triggered opening and closing of the hardware gate with a digital input

The figure below shows an example of level-triggered opening and closing with a digital input. The digital input is configured to be active with high level:

![Level-triggered opening and closing of the hardware gate with a digital input](images/42859050123_DV_resource.Stream@PNG-en-US.png)

As long as the digital input is active, the hardware gate is open and the count pulses are counted. The hardware gate is closed when the digital input becomes inactive. The counter value stays constant and ignores any further count pulses.

##### Edge-triggered opening and closing of the hardware gate with two digital inputs

The figure below shows an example of opening and closing with two digital inputs. The two digital inputs are configured so that the rising edge is evaluated:

![Edge-triggered opening and closing of the hardware gate with two digital inputs](images/42860962571_DV_resource.Stream@PNG-en-US.png)

The hardware gate is opened with the configured edge at the digital input that is configured for opening. The hardware gate is closed with the configured edge at the digital input that is configured for closing.

#### Internal gate (S7-1500)

##### Internal gate

The internal gate is open if the software gate is open and the hardware gate is open or has not been configured. The status of the internal gate is indicated by the [feedback bit](Using%20the%20module%20%28S7-1500%29.md#assignment-of-the-feedback-interface-s7-1500) STS_GATE.

If the internal gate is open, counting is started. If the internal gate is closed, all other count pulses are ignored and counting is stopped.

If you want to control a counting process with the hardware gate only, the software gate must be open. If you do not configure a hardware gate, the hardware gate is considered to be always open. In this case, you open and close the internal gate with the software gate only.

| Hardware gate | Software gate | Internal gate |
| --- | --- | --- |
| Open/not configured | open | open |
| Open/not configured | closed | closed |
| closed | open | closed |
| closed | closed | closed |

When you configure the counter behavior, you can specify whether the counting process is to start from the start value or from the current counter value when the internal gate is opened.

The internal gate can also be automatically closed upon violation of a counting limit. The software or hardware gate must then be closed and reopened to continue counting.

#### Counter behavior at gate start (S7-1500)

You have the following configuration options for counter behavior upon gate start:

- Setting counter to start value
- Continuing with the current counter value

##### Setting counter to start value

Counter behavior is as follows for this configuration:

Each counting process starts with the start value when the internal gate is opened.

The figure below shows an example for continuing the counting process after counter is set to the start value:

![Setting counter to start value](images/42673178123_DV_resource.Stream@PNG-en-US.png)

##### Continuing with the current counter value

Counter behavior is as follows for this configuration:

Each counting process starts from the current counter value after the internal gate is reopened.

The figure below shows an example for continuing the counting process with the current counter value:

![Continuing with the current counter value](images/42673481483_DV_resource.Stream@PNG-en-US.png)

### Capture (Latch) (S7-1500)

This section contains information on the following topics:

- [Capture with incremental or pulse encoder (S7-1500)](#capture-with-incremental-or-pulse-encoder-s7-1500)
- [Capture with SSI absolute encoder (S7-1500)](#capture-with-ssi-absolute-encoder-s7-1500)

#### Capture with incremental or pulse encoder (S7-1500)

##### Description

The "Capture" function is used to save the current counter value with an external reference signal. You can configure the Capture function for the following reference signals:

- Rising or falling edge at a digital input
- Rising and falling edge at a digital input
- Rising edge of signal N at the encoder input

##### Function principle

The Capture value is always the exact counter value at the time of the respective edge (delayed by the configured input filter time). The Capture function is effective regardless of the status of the internal gate. The unchanged counter value is saved when the gate is closed.

The figure below shows an example of the Capture function with the following configuration:

- Start value = 0
- Capture event upon rising edge at configured digital input
- Set counter to start value at gate start
- Continue counting after Capture event

![Function principle](images/113251597963_DV_resource.Stream@PNG-en-US.png)

The figure below shows another example of the Capture function with the following configuration:

- Start value = 0
- Capture event upon rising edge at configured digital input
- Set counter to start value at gate start
- Reset counter value to start value after Capture event and continue counting.

![Function principle](images/113251593867_DV_resource.Stream@PNG-en-US.png)

The [control bit](Using%20the%20module%20%28S7-1500%29.md#assignment-of-the-control-interface-s7-1500) EN_CAPTURE is used to enable the Capture function. The [feedback bit](Using%20the%20module%20%28S7-1500%29.md#assignment-of-the-feedback-interface-s7-1500) EVENT_CAP indicates that a counter value has been saved as a Capture in the feedback interface. If you reset EN_CAPTURE, EVENT_CAP is also reset. The status of a digital input is indicated by the respective [feedback bit](Using%20the%20module%20%28S7-1500%29.md#assignment-of-the-feedback-interface-s7-1500) STS_DIm .

The figure below shows an example of the EN_CAPTURE and EVENT_CAP bits with use of the one-time Capture function by the rising edge at a digital input:

![Function principle](images/108085034763_DV_resource.Stream@PNG-en-US.png)

The figure below shows an example of the EN_CAPTURE and EVENT_CAP bits with use of the periodic Capture function by the rising edge at a digital input:

![Function principle](images/42861608587_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> The configured input filters delay the control signal of the corresponding digital input.
>
> The Capture function has no effect on the feedback bit STS_CNT and the LEDs UP and DN.

##### Hardware interrupt

You can configure a hardware interrupt for the Capture function, if the module supports hardware interrupts. If the hardware interrupts are triggered more quickly by the system than they can be acknowledged, hardware interrupts are lost and the "Hardware interrupt" diagnostic interrupt is signaled.

#### Capture with SSI absolute encoder (S7-1500)

##### Description

The "Capture" function is used to save the current position value using an external reference signal. You can configure the Capture function for the following reference signals:

- Rising **or** falling edge at a digital input
- Rising **and** falling edge at a digital input

##### Function principle

At the time of each edge, the position value of the last valid SSI frame is stored in the Capture value.

The figure below shows an example of the Capture event by a rising edge at the configured digital input:

![Function principle](images/114792328459_DV_resource.Stream@PNG-en-US.png)

The [control bit](Using%20the%20module%20%28S7-1500%29.md#assignment-of-the-control-interface-s7-1500) EN_CAPTURE is used to enable the Capture function. The [feedback bit](Using%20the%20module%20%28S7-1500%29.md#assignment-of-the-feedback-interface-s7-1500) EVENT_CAP indicates that a position value has been saved as Capture value in the feedback interface. If you reset EN_CAPTURE, EVENT_CAP is also reset. The status of a digital input is indicated by the respective [feedback bit](Using%20the%20module%20%28S7-1500%29.md#assignment-of-the-feedback-interface-s7-1500) STS_DIm .

The figure below shows an example of the EN_CAPTURE and EVENT_CAP bits with use of the one-time Capture function by the rising edge at a digital input:

![Function principle](images/108085034763_DV_resource.Stream@PNG-en-US.png)

The figure below shows an example of the EN_CAPTURE and EVENT_CAP bits with use of the periodic Capture function by the rising edge at a digital input:

![Function principle](images/42861608587_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> The configured input filters delay the control signal of the corresponding digital input.

##### Hardware interrupt

You can configure a hardware interrupt for the Capture function, if the module supports hardware interrupts. If the hardware interrupts are triggered more quickly by the system than they can be acknowledged, hardware interrupts are lost and the "Hardware interrupt" diagnostic interrupt is signaled.

### Synchronization (S7-1500)

This section contains information on the following topics:

- [Synchronization (S7-1500)](#synchronization-s7-1500-1)
- [Synchronization by digital input (S7-1500)](#synchronization-by-digital-input-s7-1500)
- [Synchronization at signal N (S7-1500)](#synchronization-at-signal-n-s7-1500)

#### Synchronization (S7-1500)

##### Description

You use the "Synchronization" function to set the counter to the pre-defined start value with an external reference signal. You can configure synchronization for the following reference signals:

- Rising or falling edges at a digital input
- Rising edge of signal N at the encoder input
- Rising edge of signal N at the encoder input defined by the level of a digital input

##### Function principle

Synchronization always takes place exactly at the time of the reference signal. Synchronization is effective regardless of the status of the internal gate.

You use the [control bit](Using%20the%20module%20%28S7-1500%29.md#assignment-of-the-control-interface-s7-1500) EN_SYNC_UP to enable synchronization for counting in an up direction. Use the [control bit](Using%20the%20module%20%28S7-1500%29.md#assignment-of-the-control-interface-s7-1500) EN_SYNC_DN to enable synchronization for counting down. The [feedback bit](Using%20the%20module%20%28S7-1500%29.md#assignment-of-the-feedback-interface-s7-1500) EVENT_SYNC indicates that synchronization has been performed. Resetting EN_SYNC_UP or EN_SYNC_DN also resets EVENT_SYNC.

> **Note**
>
> The configured input filters delay the control signal of the corresponding digital input.
>
> Synchronization has no effect on the [feedback bit](Using%20the%20module%20%28S7-1500%29.md#assignment-of-the-feedback-interface-s7-1500) STS_CNT.

##### Single synchronization

The figure below shows an example of the EN_SYNC_UP, EN_SYNC_DN and EVENT_SYNC bits with single synchronization by an edge at a digital input for count pulses in an up direction:

![Single synchronization](images/42863559947_DV_resource.Stream@PNG-en-US.png)

After synchronization is enabled for counting in an up direction, the counter is synchronized at the first rising edge at the configured digital input. The counter can only be synchronized again once the [control bit](Using%20the%20module%20%28S7-1500%29.md#assignment-of-the-control-interface-s7-1500) EN_SYNC_UP has been reset and set again.

##### Periodic synchronization

The figure below shows an example of the EN_SYNC_UP, EN_SYNC_DN and EVENT_SYNC bits with periodic synchronization by an edge at a digital input for count pulses in an up direction:

![Periodic synchronization](images/42863680395_DV_resource.Stream@PNG-en-US.png)

As long as synchronization for counting in an up direction is enabled, the counter is synchronized at each rising edge at the configured digital input.

##### Hardware interrupt

You can configure a hardware interrupt for the synchronization, if the module supports hardware interrupts. If the hardware interrupts are triggered more quickly by the system than they can be acknowledged, hardware interrupts are lost and the "Hardware interrupt" diagnostic interrupt is signaled.

#### Synchronization by digital input  (S7-1500)

You can trigger synchronization by edges at a digital input.

##### Single synchronization

The figure below shows an example for single synchronization by an edge at a digital input:

![Single synchronization](images/42836705163_DV_resource.Stream@PNG-en-US.png)

After synchronization is enabled for counting in an upwards direction, the counter is synchronized at the first rising edge at the configured digital input. Until the [control bit](Using%20the%20module%20%28S7-1500%29.md#assignment-of-the-control-interface-s7-1500) EN_SYNC_UP has been reset and set again, any additional rising edge at the digital output is ignored. The counter can then be synchronized again.

##### Periodic synchronization

The figure below shows an example for periodic synchronization by an edge at a digital input:

![Periodic synchronization](images/43580279819_DV_resource.Stream@PNG-en-US.png)

As long as synchronization for counting in an upwards direction is enabled, the counter is synchronized at each rising edge at the configured digital input.

#### Synchronization at signal N (S7-1500)

You can trigger synchronization at signal N at the encoder input either directly or depending on the status of a digital input.

##### Single synchronization

The figure below shows an example of single synchronization at signal N (not dependent on a digital input):

![Single synchronization](images/43580302091_DV_resource.Stream@PNG-en-US.png)

After synchronization is enabled for counting in an upwards direction, the counter is synchronized at the first signal N. After resetting and setting the [control bit](Using%20the%20module%20%28S7-1500%29.md#assignment-of-the-control-interface-s7-1500) EN_SYNC_UP once again, the counter can be synchronized again.

##### Periodic synchronization

The figure below shows an example for periodic synchronization at signal N:

![Periodic synchronization](images/43580313611_DV_resource.Stream@PNG-en-US.png)

As long as synchronization for counting in an upwards direction is enabled, the counter is synchronized at each signal N.

##### Enable by a digital input

The figure below shows an example for periodic synchronization at signal N depending on the status of a digital input:

![Enable by a digital input](images/44321800459_DV_resource.Stream@PNG-en-US.png)

As long as synchronization for counting up is enabled and the corresponding digital input is active, the counter is synchronized at each signal N. If one of the conditions is not met, the counter is not synchronized at the signal N.

### Comparison values (S7-1500)

This section contains information on the following topics:

- [Comparison values and outputs (S7-1500)](#comparison-values-and-outputs-s7-1500)
- [Switching at comparison values with counter value as reference (S7-1500)](#switching-at-comparison-values-with-counter-value-as-reference-s7-1500)
- [Switching at comparison values with position value (SSI absolute value) as reference (S7-1500)](#switching-at-comparison-values-with-position-value-ssi-absolute-value-as-reference-s7-1500)
- [Switching at comparison values with measured value as reference (S7-1500)](#switching-at-comparison-values-with-measured-value-as-reference-s7-1500)

#### Comparison values and outputs (S7-1500)

##### Description

You can specify two comparison values to control both digital outputs of the channel independently of the user program:

- Comparison value 0 for digital output DQ0
- Comparison value 1 for digital output DQ1

Depending on the operating mode and the encoder used, define two position, counter or measured values as comparison value. The comparison values are configurable and can be modified during runtime using the user program.

> **Note**
>
> **DQ0 of a counter of a Compact CPU**
>
> With a Compact CPU, the respective digital output DQ0 is available via the feedback interface, but not as a physical output.

##### Switching digital outputs from the user program

The [control bits](Using%20the%20module%20%28S7-1500%29.md#assignment-of-the-control-interface-s7-1500) TM_CTRL_DQ0 and TM_CTRL_DQ1 are used to control use of the digital outputs.

If TM_CTRL_DQm is set to 0, you can control the relevant digital output from the user program with the control bit SET_DQm regardless of the configured technological function. If TM_CTRL_DQm is set to 1, the technological function of the controller of the respective digital output is enabled.

The status of a digital output is indicated by the respective STS_DQm feedback bit.

#### Switching at comparison values with counter value as reference (S7-1500)

The comparison values are compared with the current counter value. If the counter value meets the assigned comparison condition and the technological function of the associated digital output is enabled, the digital output is set. If you assign "Between comparison value 0 and 1" for digital output DQ1, both comparison values affect DQ1.

You can make switching for a digital output dependent on one of the following comparison events:

##### Setting between comparison value and high counting limit

The digital output is set to 1 if:

Comparison value &lt;= counter value &lt;= high counting limit

![Setting between comparison value and high counting limit](images/43580449163_DV_resource.Stream@PNG-en-US.png)

The comparison event is independent of the count direction.

##### Setting between comparison value and low limit

The digital output is set to 1 if:

Low counting limit &lt;= counter value &lt;= comparison value

![Setting between comparison value and low limit](images/43580524427_DV_resource.Stream@PNG-en-US.png)

The comparison event is independent of the count direction.

##### Setting between comparison value 0 and comparison value 1

The comparison event can be configured for the digital output DQ1 if "Use by user program" has been configured for the digital output DQ0. Comparison value 1 must be greater than Comparison value 0.

DQ1 is set to 1 if:

Comparison value 0 &lt;= counter value &lt;= comparison value 1

The figure below shows an example of the comparison event when counting in an upwards direction:

![Setting between comparison value 0 and comparison value 1](images/43580535435_DV_resource.Stream@PNG-en-US.png)

##### Setting at comparison value for one pulse duration

The respective digital output is set to 1 for a specified period of time when the following conditions are fulfilled:

- Counter value = comparison value
- Current count direction = configured count direction for the comparison event

The figure below shows an example of the comparison event when counting in an upwards direction:

![Setting at comparison value for one pulse duration](images/43580632203_DV_resource.Stream@PNG-en-US.png)

The figure below shows an example of the comparison event when counting in a downward direction:

![Setting at comparison value for one pulse duration](images/43580642955_DV_resource.Stream@PNG-en-US.png)

To repeat the comparison event, the counter value must change and then correspond to the respective comparison value again.

If the pulse duration has been defined as "0" and the counter value is equal to the comparison value, the digital output is set to 1 until the next count pulse:

![Setting at comparison value for one pulse duration](images/40314505483_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> This comparison event switches the relevant digital output if a count pulse reaches the comparison value. The digital output does not switch when the counter value is set, by synchronization for example.

##### Setting by the user program up to comparison value

You can set the respective digital output to 1 (edge) by setting the [control bit](Using%20the%20module%20%28S7-1500%29.md#assignment-of-the-control-interface-s7-1500) SET_DQm. The respective digital output is set to 0 by any of the following events:

- Match of the counter value and the comparison value in the configured direction of the comparison event
- Reset of the corresponding SET_DQm control bit.

The figure below shows an example of the comparison event when counting in an upwards direction:

![Setting by the user program up to comparison value](images/43580653707_DV_resource.Stream@PNG-en-US.png)

You can disable the digital output before the counter value reaches the comparison value by setting the control bit SET_DQm to 0.

> **Note**
>
> If the comparison value is reached in the configured count direction, the feedback bit EVENT_CMPm is set independently of the state of the control bit SET_DQm.
>
> The comparison event switches a digital output when a count pulse reaches the respective comparison value. The digital output does not switch when the counter value is set, by synchronization for example.

#### Switching at comparison values with position value (SSI absolute value) as reference (S7-1500)

The comparison values are compared with the current position value. If the position value meets the assigned comparison condition and the technological function of the associated digital output is enabled, the digital output is set. If you assign "Between comparison value 0 and 1" for digital output DQ1, both comparison values affect DQ1.

If you use a 32 bit position value for the comparison function, the position value is interpreted as DINT.

You can make switching for a digital output dependent on one of the following comparison events:

##### Setting between comparison value and high limit

The high limit corresponds to the maximum position value.

The digital output is set to 1 if:

Comparison value &lt;= position value &lt;= maximum position value

![Setting between comparison value and high limit](images/54106804491_DV_resource.Stream@PNG-en-US.png)

The comparison event is independent of the direction of the position value change. The maximum position value depends on the resolution of the SSI absolute encoder.

##### Setting between comparison value and low limit

The low limit corresponds to the position value "0".

The digital output is set to 1 if:

0 &lt;= position value &lt;= comparison value

![Setting between comparison value and low limit](images/54106808203_DV_resource.Stream@PNG-en-US.png)

The comparison event is independent of the direction of the position value change.

##### Setting between comparison value 0 and comparison value 1

The comparison event can be configured for the digital output DQ1 if "Use by user program" has been configured for the digital output DQ0. Comparison value 1 must be greater than Comparison value 0.

DQ1 is set to 1 if:

Comparison value 0 &lt;= position value &lt;= comparison value 1

The figure below shows an example of the comparison event when counting up:

![Setting between comparison value 0 and comparison value 1](images/54167888267_DV_resource.Stream@PNG-en-US.png)

##### Setting at comparison value for one pulse duration

The respective digital output is set to 1 for a specified period of time when the following conditions are fulfilled:

- Matching of the position value and comparison value or crossing of the comparison value
- Current direction of the position value change = assigned direction for the comparison event

The figure below shows an example of the comparison event when counting up:

![Setting at comparison value for one pulse duration](images/52884565643_DV_resource.Stream@PNG-en-US.png)

The figure below shows an example of the comparison event when counting down:

![Setting at comparison value for one pulse duration](images/52884569355_DV_resource.Stream@PNG-en-US.png)

To repeat the comparison event, the position value must change and then correspond to or cross the respective comparison value again.

##### Setting by the user program up to comparison value

You can set each digital output to 1 (edge) by setting the [control bit](Using%20the%20module%20%28S7-1500%29.md#assignment-of-the-control-interface-s7-1500) SET_DQm. The respective digital output is set to 0 by any of the following events:

- Matching of the position value and the comparison value or crossing of the comparison value in the configured direction of the comparison event
- Resetting of the SET_DQm control bit.

The figure below shows an example of the comparison event when counting up:

![Setting by the user program up to comparison value](images/52884573067_DV_resource.Stream@PNG-en-US.png)

You can disable the digital output before the position value corresponds to or exceeds the comparison value by setting the control bit SET_DQm to 0.

> **Note**
>
> If the comparison value is reached or exceeded in the assigned direction, feedback bit EVENT_CMPm is set independently of the status of control bit SET_DQm.

#### Switching at comparison values with measured value as reference (S7-1500)

The comparison values are compared with the current measured value. If the measured value meets the configured comparison condition and the technological function of the corresponding digital output is enabled, the digital output is set. If you configure "Between comparison value 0 and 1" or "Not between comparison value 0 and 1" for digital output DQ1, both comparison values affect DQ1.

You can make switching for a digital output dependent on one of the following comparison events:

##### Setting above the comparison value

The digital output is set to 1 if:

Measured value &gt;= comparison value

![Setting above the comparison value](images/44516724491_DV_resource.Stream@PNG-en-US.png)

##### Setting below the comparison value

The digital output is set to 1 if:

Measured value &lt;= comparison value

![Setting below the comparison value](images/44520694027_DV_resource.Stream@PNG-en-US.png)

##### Setting between comparison value 0 and comparison value 1

The comparison event can be configured for the digital output DQ1 if "Use by user program" has been configured for the digital output DQ0. Comparison value 1 must be greater than Comparison value 0.

DQ1 is set to 1 if:

Comparison value 0 &lt;= measured value &lt;= comparison value 1

![Setting between comparison value 0 and comparison value 1](images/44520424971_DV_resource.Stream@PNG-en-US.png)

##### Not setting between comparison value 0 and comparison value 1

The comparison event can be configured for the digital output DQ1 if "Use by user program" has been configured for the digital output DQ0. Comparison value 1 must be greater than Comparison value 0.

DQ1 is set to 1 if:

Comparison value 1 &lt;= measured value &lt;= comparison value 0

![Not setting between comparison value 0 and comparison value 1](images/44521321483_DV_resource.Stream@PNG-en-US.png)

### Measured value determination (S7-1500)

This section contains information on the following topics:

- [Overview of measuring functions (S7-1500)](#overview-of-measuring-functions-s7-1500)
- [Measured value determination with incremental or pulse encoder (S7-1500)](#measured-value-determination-with-incremental-or-pulse-encoder-s7-1500)
- [Measured value determination with SSI absolute encoder (S7-1500)](#measured-value-determination-with-ssi-absolute-encoder-s7-1500)

#### Overview of measuring functions (S7-1500)

The following highly accurate measuring functions are available (accuracy up to 100 ppm):

| [Measurement type](#measuring-types-s7-1500) | Description |
| --- | --- |
| Frequency measurement | The mean frequency is calculated at set measuring intervals on the basis of the time profile of the count pulses or position value changes and returned in Hertz as floating point number. |
| Period measurement | The mean period duration is calculated at set measuring intervals on the basis of the time profile of the count pulses or position value changes and returned in seconds as floating point number. |
| Velocity measurement | The mean velocity is calculated at set measuring intervals on the basis of the time profile of the count pulses or position value changes and other parameters, and returned in the configured unit of measurement. |

Measured values and counter values are available concurrently in the feedback interface.

##### Update time

You can configure the interval at which the technology module updates the measured values cyclically as the update time. Setting longer update time intervals allows uneven measured variables to be smoothed and increases measuring accuracy.

##### Gate control for incremental and pulse encoders

Opening and closing the internal gate defines the period of time during which the count pulses are captured. The update time is asynchronous to the opening of the gate, which means that the update time is not started when the gate is opened. After the internal gate is closed, the last measured value captured is still returned.

#### Measured value determination with incremental or pulse encoder (S7-1500)

This section contains information on the following topics:

- [Measuring ranges (S7-1500)](#measuring-ranges-s7-1500)
- [Measuring intervals (S7-1500)](#measuring-intervals-s7-1500)
- [Measuring types (S7-1500)](#measuring-types-s7-1500)

##### Measuring ranges (S7-1500)

###### Measuring range (TM Count and TM PosInput)

The measuring functions have the following measuring limits:

| Measurement type | Low measuring range limit | High measuring range limit |
| --- | --- | --- |
| Frequency measurement | 0.04 Hz | 800 kHz* / 4 MHz** |
| Period measurement | 1.25 µs* / 0.25 µs** | 25 s |
| Velocity measurement | Depending on the configured number of "increments per unit" and the "time base for velocity measurement" |  |
| * Applies to 24 V incremental encoders and "quadruple" signal evaluation.   ** Applies to RS422 incremental encoders and "quadruple" signal evaluation. |  |  |

All measured values are returned as signed values. The sign indicates whether the counter value increased or decreased during the relevant time period.

###### Measuring range (Compact CPU)

The measuring functions have the following measuring range limits:

| Measurement type | Low measuring range limit | High measuring range limit |
| --- | --- | --- |
| Frequency measurement | 0.04 Hz | 400 kHz* |
| Period measurement | 2.5 µs* | 25 s |
| Velocity measurement | Depends on the configured number of "Increments per unit" and the "Time base for velocity measurement" |  |
| * Applies to 24 V incremental encoders and "quadruple“ signal evaluation. |  |  |

All measured values are returned as signed values. The sign indicates whether the counter value increased or decreased during the relevant time period.

##### Measuring intervals (S7-1500)

###### Measuring principle

The technology module assigns a time value to each count pulse. The measuring interval is defined as the time between each last count pulse before and during the previous update time. The measuring interval and the number of pulses in the measuring interval are evaluated to calculate measured variables.

If there is no count pulse within an update time, the measuring interval is dynamically adjusted. In this case, a pulse is assumed at the end of the update time and the measuring interval is calculated as the time between that point and the last pulse which occurred. The number of pulses is then 1.

The feedback bit STS_M_INTERVAL indicates whether a count pulse occurred in the previous measuring interval. This allows for a differentiation between an assumed and an actual count pulse.

The following figures show the principle of measurement and the dynamic adjustment of the measuring interval:

![Measuring principle](images/51869025291_DV_resource.Stream@PNG-en-US.png)

##### Measuring types (S7-1500)

###### Frequency measurement

A value "0" is returned until the first measured value is available.

The measurement process begins with the first pulse detected once the internal gate has been opened. The first measured value can be calculated after the second pulse at the earliest.

The measured value is updated in the [feedback interface](Using%20the%20module%20%28S7-1500%29.md#assignment-of-the-feedback-interface-s7-1500) upon completion of each update time. If the internal gate is closed, measuring stops and the measured value is no longer updated.

The figures below shows an example of frequency measurement with an update time of 1 s:

![Frequency measurement](images/47291406475_DV_resource.Stream@PNG-en-US.png)

###### Period measurement

The reciprocal of the frequency is output as the measured value for period measurement.

A value "25 s" is returned until the first measured value is available.

###### Velocity measurement

The normalized frequency is output as the measured value in velocity measurement. You can configure the scaling using the time basis and the number of increments that your encoder delivers per unit.

**Example:**

Your encoder delivers 4000 increments per meter. The velocity is to be measured in meters per minute.

In this case, you need to configure 4000 Increments per unit and a time basis of one minute.

#### Measured value determination with SSI absolute encoder (S7-1500)

This section contains information on the following topics:

- [Measuring ranges (S7-1500)](#measuring-ranges-s7-1500-1)
- [Measuring intervals (S7-1500)](#measuring-intervals-s7-1500-1)
- [Measuring types (S7-1500)](#measuring-types-s7-1500-1)

##### Measuring ranges (S7-1500)

###### Measuring range SSI absolute encoder

The measuring functions have the following measuring limits:

| Measurement type | Low measuring range limit | High measuring range limit |
| --- | --- | --- |
| Frequency measurement | 0,04 Hz | 4 MHz |
| Period measurement | 0,25 μs | 25 s |
| Velocity measurement | Depending on the configured number of "increments per unit" and the "time base for velocity measurement" |  |

All measured values are returned as signed values. The sign indicates whether the position value increased or decreased during the relevant time period.

##### Measuring intervals (S7-1500)

###### Measuring principle

The technology module assigns a time value to each SSI frame. The measuring interval is defined as the time between the last SSI frame with a change of position value before and during the previous update time. The measuring interval and the total change in position value in the measuring interval are evaluated to calculate a measured variable. The total change in position value in a measuring interval corresponds to the number of encoder increments in the same measuring interval.

If there is no change in position value within an update time, the measuring interval is dynamically adjusted. In this case, a change in position value is assumed at the end of the update time and the measuring interval is calculated as the time between that point and the last SSI frame with a change in position value. The change in position value is then 1.

The feedback bit STS_M_INTERVAL indicates whether a change in position value occurred in the previous measuring interval. This allows for a differentiation between an assumed and an actual change in position value. If the technology module cannot calculate measured values because the measuring range limit has been violated, the feedback bit STS_M_INTERVAL is not set.

##### Measuring types (S7-1500)

###### Frequency measurement

The value "0.0" is reported in the time up to the first available measured value.

The measuring process begins with the first detected change in position value. The first measured value can be calculated after the second detected change in position value at the earliest.

The measured value is updated in the [feedback interface](Using%20the%20module%20%28S7-1500%29.md#assignment-of-the-feedback-interface-s7-1500) upon completion of each update time.

The figures below shows an example of frequency measurement with an update time of 1 s:

![Frequency measurement](images/54111011083_DV_resource.Stream@PNG-en-US.png)

###### Period measurement

The reciprocal of the frequency is output as the measured value for period measurement.

A value "25 s" is returned until the first measured value is available.

###### Velocity measurement

The normalized frequency is output as the measured value in velocity measurement. You can configure the scaling using the time basis and the number of increments that your encoder delivers per unit.

**Example:**

Your SSI absolute encoder operates with a resolution of 12 bits per revolution and performs 4096 increments per revolution. The velocity should be measured in revolutions per minute.

In this case, you need to configure 4096 Increments per unit and a time basis of one minute.

> **Note**
>
> **Excessive encoder speed can provide wrong direction of rotation.**
>
> If an SSI absolute encoder rotates so quickly that more than half of the value range is covered within one module cycle<sup>1</sup>, the velocity and direction of rotation can not be determined correctly anymore. This can result in an incorrect function at:
>
> - DQ functions
> - Feedback bits EVENT_OFLW, EVENT_UFLW, EVENT_ZERO, EVENT_CMP0, EVENT_CMP1 and STS_DIR
>
> <sup>1</sup> Non isochronous mode: 500 μs; isochronous mode: PROFINET cycle time

> **Note**
>
> If you are using an SSI absolute encoder whose value range does not correspond to the power of 2, the calculated speed measured value may be incorrect at the moment of the overflow.

### Hysteresis (S7-1500)

This section contains information on the following topics:

- [Hysteresis with incremental or pulse encoder (S7-1500)](#hysteresis-with-incremental-or-pulse-encoder-s7-1500)
- [Hysteresis with SSI absolute encoder (S7-1500)](#hysteresis-with-ssi-absolute-encoder-s7-1500)

#### Hysteresis with incremental or pulse encoder (S7-1500)

##### Description

Hysteresis allows you to specify a range around the comparison values within which the digital outputs are not to be switched again until the counter value has gone outside this range.

Slight movements by the encoder can result in the counter value fluctuating around a certain value. If a comparison value or a counting limit lies within this fluctuation range, the corresponding digital output is switched on and off with corresponding frequency if hysteresis is not used. Hysteresis prevents this unwanted switching, and configured hardware interrupts when a comparison event occurs.

The hysteresis becomes active when the respective comparison value is reached by a count pulse. If the counter value is set to the start value during an active hysteresis, the hysteresis becomes inactive.

Regardless of the hysteresis value, the hysteresis range ends at the low/high counting limits.

##### Function principle

The figure below shows an example for the hysteresis with the following configuration:

- Setting of a digital output between comparison value and high counting limit
- Comparison value = 5
- Hysteresis = 0 or 2 (gray background)

![Function principle](images/90909954443_DV_resource.Stream@PNG-en-US.png)

Hysteresis is enabled when the counter value 5 is reached. When the hysteresis is active, the comparison result remains unchanged. Hysteresis is disabled when the counter value 2 or 8 is reached.

The figure below shows an example for the hysteresis with the following configuration:

- Setting at comparison value for one pulse duration
- Comparison value = 5
- Comparison in both count directions
- Hysteresis = 0 or 2 (gray background)

![Function principle](images/90913286539_DV_resource.Stream@PNG-en-US.png)

#### Hysteresis with SSI absolute encoder (S7-1500)

##### Description

Hysteresis allows you to specify a range around the comparison values within which the digital outputs are not to be switched again until the position value has gone outside this range.

Slight movements by the encoder can result in the position value fluctuating around a certain value. If a comparison value, the minimum or maximum position value, lies within the fluctuation range, the associated digital output is switched on and off if a hysteresis is not used. Hysteresis prevents this unwanted switching, and configured hardware interrupts when a compare event occurs.

Regardless of the hysteresis value, the hysteresis range ends at the respective minimum or maximum position value.

##### Function principle

The figure below shows an example for the hysteresis with the following parameter assignment:

- Setting of a digital output between comparison value and high limit
- Comparison value = 10
- Hysteresis = 0 or 2 (gray background)

![Function principle](images/90913290507_DV_resource.Stream@PNG-en-US.png)

Hysteresis is enabled when the position value 10 is reached. When the hysteresis is active, the comparison result remains unchanged. Hysteresis is disabled when the position values 7 or 13 are reached.

The figure below shows an example for the hysteresis with the following parameter assignment:

- Setting at comparison value for one pulse duration
- Comparison value = 10
- Comparison in both directions of position value changes
- Hysteresis = 0 or 2 (gray background)

![Function principle](images/90908357643_DV_resource.Stream@PNG-en-US.png)

### Interrupts  (S7-1500)

#### Hardware interrupt

If the technology module supports hardware interrupts, it can trigger a hardware interrupt in the CPU, for example, if a compare event occurs, in the event of overflow or underflow, in the event of a zero crossing of the counter and/or of a change of count direction (direction reversal). You can specify which events are to trigger a hardware interrupt during operation.

#### Diagnostic interrupt

The technology module can trigger diagnostic interrupts in the event of errors. You enable the diagnostic interrupts for certain errors in the device configuration. Refer to the device manual for the technology module to learn about the events that can trigger a diagnostic interrupt during operation.

### Position detection for Motion Control (S7-1500)

#### Description

You can use the technology module for example with an incremental encoder for the following axis technology objects of S7-1500 Motion Control for position detection :

- TO_PositioningAxis
- TO_SynchronousAxis
- TO_ExternalEncoder

When using an incremental or pulse encoder, the position detection is based on the counting function of the technology module. With an SSI absolute encoder, the absolute value is read in via a synchronous, serial interface and prepared according to the parameter assignment and made available for S7-1500 Motion Control.

The range of functions of the technology module has the following limitations in this case:

- Counter behavior not configurable
- No functions for digital inputs available apart from measuring input function
- No comparison functions for digital outputs available
- No hardware interrupts available

In the device configuration of the technology module in STEP 7 (TIA Portal), select the "Position input for technology object "Motion Control"" operating mode and use the corresponding technology object in the program. This reduces the configuration options to the parameters that are essential. For TM Count or TM PosInput, the mode automatically applies to all channels of the technology module. For a Compact CPU, the mode automatically applies to the respective channel.

In this operating mode you can use the (TO_MeasuringInput) measuring input technology object to execute a measuring input function with a hardware digital input. To do this select the measuring input type "Measuring via PROFIdrive telegram" in the measuring input technology object and the value "1" as the number of the measuring input.

You can find information about further configuring in the help for the axis technology objects and the measuring input technology object of S7-1500 Motion Control.

### Encoder signals (S7-1500)

This section contains information on the following topics:

- [24 V or TTL count signals (S7-1500)](#24-v-or-ttl-count-signals-s7-1500)
- [RS422 count signals (S7-1500)](#rs422-count-signals-s7-1500)
- [SSI signals (S7-1500)](#ssi-signals-s7-1500)

#### 24 V or TTL count signals (S7-1500)

##### Count signals of 24 V or TTL incremental encoders

The 24 V incremental encoder returns the 24 V signals A, B, and N to the technology module. The A and B signals are phase-shifted by 90°. You can also connect incremental encoders without an N signal.

A 24 V incremental encoder uses the A and B signals for counting. If configured accordingly, the N signal is used for setting the counter to the start value or for saving the current counter value to the Capture value.

The figure below shows an example of the time profile of the signals of an 24 V incremental encoder:

![Count signals of 24 V or TTL incremental encoders](images/42826060043_DV_resource.Stream@PNG-en-US.png)

The technology module detects the count direction by evaluating the sequence of edges of the A and B signals. You can specify an inversion of the count direction.

##### Count signals of 24 V or TTL pulse encoders without/with direction signal

The encoder, for example an initiator (BERO) or a light barrier, returns only a count signal that is connected to terminal A of the counter.

In addition, you can connect a signal for direction detection to terminal B of the counter. In case of a high level the direction signal is counted backwards. If your encoder does not return a corresponding signal, you can specify the count direction with the user program using the control interface.

The figure below shows an example of the time profile of the signals of a 24 V pulse encoder with direction signal and the resulting count pulses:

![Count signals of 24 V or TTL pulse encoders without/with direction signal](images/44011074187_DV_resource.Stream@PNG-en-US.png)

##### Count signals of 24 V or TTL pulse encoders with Up/Down count signal

The Up count signal is connected to terminal A. The Down count signal is connected to terminal B.

The figure below shows an example of the time profile of the signals of a pulse encoder with Up/Down count signal and the resulting count pulses:

![Count signals of 24 V or TTL pulse encoders with Up/Down count signal](images/57885700363_DV_resource.Stream@PNG-en-US.png)

##### Sourcing output/sinking output for 24 V count signals (TM Count and ET 200eco PN M12-L TM PosInput 2)

You can connect the following encoders/sensors to the counter inputs:

- Sourcing output:  
  The A, B, and N inputs are wired to 24VDC .
- Sinking output:  
  The A, B, and N inputs are wired to ground M .
- Push-pull (sourcing and sinking output):  
  The A, B, and N inputs are wired alternately to 24VDC and ground M .

##### Sourcing output for 24 V counter signals (Compact CPU)

You can connect the sourcing output and push-pull encoders or sensors to the counter inputs.

##### Monitoring of the encoder signals (TM Count and TM PosInput)

The signals of push-pull 24 V encoders are monitored for wire breaks by the technology module. TTL signals are monitored by the technology module for faulty supply voltages.

If you enable the diagnostic interrupt in the device configuration, the technology module triggers a diagnostic interrupt in the event of encoder signal errors.

#### RS422 count signals (S7-1500)

##### RS422 incremental encoder count signals

The RS422 incremental encoder sends the following differential signals to the technology module:

- +A and -A
- +B and -B
- +N and -N

The signal information for RS422 signals is encoded in the differential voltage between A and -A, B and -B, and +N and -N. The A and B signals are phase-shifted by 90°. You can also connect incremental encoders without an N signal.

RS422 incremental encoders use the A and B signals for counting. If configured accordingly, the N signal is used for setting the counter to the start value or for saving the current counter value as the Capture value.

The figure below shows an example of the time profile of the signals of an RS422 incremental encoder:

![RS422 incremental encoder count signals](images/111732018571_DV_resource.Stream@PNG-en-US.png)

The technology module detects the count direction by evaluating the sequence of edges of the A and B signals. You can specify an inversion of the count direction.

##### Count signals of RS422 pulse encoders without/with direction signal

The encoder, for example a light barrier, only returns a count signal that is connected to terminal A.

You can also connect a signal for direction detection to terminal B. In case of a high level the direction signal is counted backwards. If your encoder does not return a corresponding signal, you can specify the count direction with the user program using the control interface.

The figure below shows an example of the time profile of the signals of a RS422 pulse encoder with direction signal and the resulting count pulses:

![Count signals of RS422 pulse encoders without/with direction signal](images/111732022539_DV_resource.Stream@PNG-en-US.png)

##### Count signals of RS422 pulse encoders with Up/Down count signal

The Up count signal is connected to the A terminals. The Down count signal is connected to the B terminals.

The figure below shows an example of the time profile of the signals of an RS422 pulse encoder with Up/Down count signal and the resulting count pulses:

![Count signals of RS422 pulse encoders with Up/Down count signal](images/111732026507_DV_resource.Stream@PNG-en-US.png)

##### Monitoring of encoder signals

RS422 signals are monitored by the technology module for wire breaks, short-circuits, and incorrect supply voltage.

If you enable the diagnostic interrupt in the device configuration, the technology module triggers a diagnostic interrupt in the event of encoder signal errors.

#### SSI signals (S7-1500)

##### Signals from SSI absolute encoders

The SSI absolute encoder and the technology module communicate by means of the SSI data signals +D and -D and the SSI clock signals +C and -C. SSI uses the RS422 signal standard. The signal information is coded in the respective differential voltage between +C and -C as well as +D and -D.

##### Monitoring of the encoder signals and the SSI frames

The signals of an SSI absolute encoder are monitored for wire breaks, short-circuits and incorrect supply voltage. The technology module also monitors the SSI frames for errors.

If you enable the diagnostic interrupts in the device configuration, the technology module triggers a diagnostic interrupt in the event of encoder signal or SSI frame errors.

### Signal evaluation of incremental signals (S7-1500)

This section contains information on the following topics:

- [Overview (S7-1500)](#overview-s7-1500)
- [Single evaluation (S7-1500)](#single-evaluation-s7-1500)
- [Double evaluation (S7-1500)](#double-evaluation-s7-1500)
- [Quadruple evaluation (S7-1500)](#quadruple-evaluation-s7-1500)

#### Overview (S7-1500)

The technology module counter counts the edges of encoder signals A and B. For incremental encoders with phase-shifted signals A and B, you can select either single or multiple evaluation to improve the resolution.

You can configure the following signal evaluations:

- [Single evaluation](#single-evaluation-s7-1500)
- [Double evaluation](#double-evaluation-s7-1500)
- [Quadruple evaluation](#quadruple-evaluation-s7-1500)

> **Note**
>
> The phase offset between the edges of signals A and B is evaluated. If no phase shift is identifiable, an encoder error (invalid transition of A/B signals) is reported via the ENC_ERROR feedback bit.

#### Single evaluation (S7-1500)

Single evaluation evaluates the rising and falling edge at signal A when signal B has a low level.

Count pulses in an upwards direction are generated with a rising edge at signal A during a low level at signal B. Count pulses in a downwards direction are generated with a falling edge at signal A during a low level of signal B.

The following figure shows an example for single evaluation of 24 V and TTL count signals:

![Figure](images/42825921035_DV_resource.Stream@PNG-en-US.png)

The following figure shows an example for single evaluation of RS422 count signals:

![Figure](images/111818279179_DV_resource.Stream@PNG-en-US.png)

#### Double evaluation (S7-1500)

With double evaluation, the rising and falling edges of signal A are evaluated.

The edge direction of signal A and the level at signal B determines whether count pulses are generated in an upward or downward direction.

The following figure shows an example for double evaluation of 24 V and TTL count signals:

![Figure](images/42825838987_DV_resource.Stream@PNG-en-US.png)

The following figure shows an example for double evaluation of RS422 count signals:

![Figure](images/111818284171_DV_resource.Stream@PNG-en-US.png)

#### Quadruple evaluation (S7-1500)

With quadruple evaluation, the rising and falling edges of signals A and B are evaluated.

The edge direction of one signal and the level of the other signal determines whether count pulses are generated in an upward or downward direction.

The figure below shows an example for quadruple evaluation of 24 V and TTL count signals:

![Figure](images/42824976139_DV_resource.Stream@PNG-en-US.png)

The figure below shows an example for quadruple evaluation of RS422 count signals:

![Figure](images/111820682763_DV_resource.Stream@PNG-en-US.png)

### Clock synchronization (TM Count and TM PosInput) (S7-1500)

The technology module supports the system function "Isochronous mode". This system function enables position, count and measured values to be recorded in a defined system cycle.

In isochronous mode, the cycle of the user program, the transmission of the input and output data and the processing in the module are synchronized with each other. The output signals switch immediately if the relevant comparison condition is met. A change in the state of a digital input immediately affects the planned reaction of the technology module and changes the status bit of the digital input in the feedback interface.

In the case of operation with a "Counting and measurement" technology object use an OB of the type "Synchronous Cycle" (for example OB61). In the assigned OB the instruction High_Speed_Counter or SSI_Absolute_Encoder is called.

For position detection of a "Motion Control" technology object use the OB of the type "MC-Servo". When using the technology objects cam and cam track, isochronous mode is required. When using the measuring input technology object in connection with the hardware digital input DI1, no isochronous mode is required.

In case of manual operation use an OB of the "Synchronous Cycle" type (for example OB61). In the assigned OB the input and output data is processed.

#### Data processing

The data that was transmitted to the technology module in the current bus cycle via the control interface takes effect when it is processed in the internal technology module cycle. At the moment when the input data (T<sub>i</sub>) are read, the position and counter value and, if appropriate, the measured value as well as status bits are detected and made available in the feedback interface for retrieval in the current bus cycle.

The update time for the measured value is synchronized in a suitable relationship to the system cycle and, if required, adapted in length. If you configure "0", the measured value is updated once per system cycle.

#### Isochronous mode parameter

In isochronous mode, the following parameters can have an effect on the isochronous parameters of the Sync domain.

- Filter frequency
- Frame length<sup>1</sup>
- Transmission rate<sup>1</sup>
- Monoflop time<sup>1</sup>
- Parity<sup>1</sup>

<sup>1</sup> Only when using an SSI absolute encoder

Because the isochronous parameters are not checked in RUN, overflows can occur when you change one or more of the named parameters in RUN: You prevent overflows by already selecting the option with the greatest time demand during the offline parameter assignment.

#### Additional information

For a detailed description of the isochronous mode refer to:

- The isochronous mode function manual available as a download from the [Internet](https://support.industry.siemens.com/cs/ww/en/view/109755401).
- The PROFINET with STEP 7 function manual as a download from the [Internet](https://support.industry.siemens.com/cs/ww/en/view/49948856).

## Basics of counting (TM Timer DIDQ) (S7-1500)

This section contains information on the following topics:

- [Overview of applications (S7-1500)](#overview-of-applications-s7-1500-1)
- [Counting with incremental encoder (S7-1500)](#counting-with-incremental-encoder-s7-1500)
- [Counting with pulse encoder (S7-1500)](#counting-with-pulse-encoder-s7-1500)
- [24 V count signals (S7-1500)](#24-v-count-signals-s7-1500)
- [Isochronous mode (S7-1500)](#isochronous-mode-s7-1500)

### Overview of applications (S7-1500)

#### Introduction

You configure the TM Timer DIDQ and assign its parameters with the configuration software.

The module's functions are controlled and monitored via the user program with the control and feedback interface.

#### System environment

The respective module can be used in the following system environments with its counter functions:

| Applications | Components required | Configuration software | In the user program |
| --- | --- | --- | --- |
| Central operation with an S7-1500 CPU or 151xSP CPU | - S7-1500 automation system or ET 200SP CPU - TM Timer DIDQ | STEP 7 (TIA Portal):  Device configuration and parameter setting with hardware configuration | Direct access to feedback interface of the technology module in the I/O data |
| Distributed operation with a S7-1500 CPU | - S7-1500 Automation System - ET 200 Distributed I/O System - TM Timer DIDQ |  |  |
| Distributed operation with a S7-300/400 CPU | - S7-300/400 automation system - ET 200 distributed I/O system - TM Timer DIDQ | STEP 7 (TIA Portal):  Device configuration and parameter setting with hardware configuration  STEP 7:  Device configuration and parameter setting with hardware configuration (only ET 200SP) |  |

> **Note**
>
> A description of the control and feedback interface is available in the device manual for the TM Timer DIDQ.

### Counting with incremental encoder (S7-1500)

You can use a few channels of a TM Timer DIDQ for simple counting tasks with an incremental encoder. Counting refers to the recording and adding up of events. The channels configured as counters each acquire the two incremental signals and evaluate these accordingly.

#### Count direction

The technology module can count up and down with an incremental encoder. You can invert the counting direction to adapt it to the process.

#### Counting limits

The counting limits define the counter value range used.

The minimum counter value is -2147483648 (-2<sup>31</sup>). The maximum counter value is 2147483647 (2<sup>31</sup>-1). The respective counter counts continuously. At an overflow, the counter jumps to the other counting limit in each case and continues counting.

The counter value cannot be influenced by the user program.

#### Parameter assignment

For use of a counter for an incremental encoder, two digital inputs each of a channel group are combined. For this purpose, you choose the configuration "Incremental encoder (A, B phase-shifted)" in the channel parameters for the respective group.

> **Note**
>
> **Counters of the TM Timer DIDQ 16x24V**
>
> The number of available counters of the TM Timer DIDQ 16x24V is dependent on the channel configuration. In order to use 4 counters, you must choose the use of 8 inputs in the channel configuration. If you choose the use of 3 inputs, you can use 1 counter. Other channel configurations do not allow any counter use.

#### Counter value feedback

The current counter value is indicated in the feedback interface in the TEC_IN value (DIm). DIm corresponds to the first of the two grouped digital inputs in each case. For the second digital input, "0" is returned in the value TEC_IN (DIm+1).

### Counting with pulse encoder (S7-1500)

You can use a few channels of a TM Timer DIDQ for simple counting tasks with a pulse encoder. Counting refers to the recording and adding up of events. The channels configured as counters each acquire one pulse signal and evaluate this accordingly.

#### Count direction

The technology module can count up and down with a pulse encoder.

#### Counting limits

The counting limits define the counter value range used.

The minimum counter value is -2147483648 (-2<sup>31</sup>). The maximum counter value is 2147483647 (2<sup>31</sup>-1). The respective counter counts continuously. At an overflow, the counter jumps to the other counting limit in each case and continues counting.

The counter value cannot be influenced by the user program.

#### Parameter assignment

For use of a counter for a pulse encoder, you choose the configuration "Use inputs individually" or "Use input/output individually" in the channel parameters for the respective group. You can configure the first digital input of a group as a counter.

> **Note**
>
> **Counters of the TM Timer DIDQ 16x24V**
>
> The number of available counters of the TM Timer DIDQ 16x24V is dependent on the channel configuration. In order to use 4 counters, you must choose the use of 8 inputs in the channel configuration. If you choose the use of 3 inputs, you can use 1 counter. Other channel configurations do not allow any counter use.

#### Counter value feedback

The current counter value is indicated in the feedback interface in the TEC_IN value (DIm). DIm corresponds to the respective digital input.

### 24 V count signals (S7-1500)

#### Count signals of 24 V incremental encoders

The 24 V incremental encoder returns the 24 V signals A and B to the technology module. The A and B signals are phase-shifted by 90°.

The figure below shows an example of the time profile of the signals of an 24 V incremental encoder:

![Count signals of 24 V incremental encoders](images/89801226379_DV_resource.Stream@PNG-en-US.png)

The technology module detects the count direction by evaluating the sequence of edges of the A and B signals. You can specify an inversion of the count direction.

**Signal evaluation**

The two phase-shifted signals of an incremental encoder are evaluated four times. With quadruple evaluation, the positive and negative edges of signal A and signal B are evaluated.

Whether count pulses are generated in an upward or downward direction depends on the edge direction of the one signal and the level of the other signal in the meantime.

The figure below shows an example of the quadruple evaluation of 24 V count signals:

![Count signals of 24 V incremental encoders](images/89815930891_DV_resource.Stream@PNG-en-US.png)

#### Count signals of 24 V pulse encoders

An encoder, for example, a proximity switch (BERO) or a light barrier, returns only one count signal that is connected to the digital input of a counter.

You can count the positive or the negative edges of the signal.

### Isochronous mode (S7-1500)

The TM Timer DIDQ supports the system function "Isochronous mode". This system function enables counter values to be acquired in a defined system cycle.

In isochronous mode, the cycle of the user program, the transmission of the input and output data and the processing in the module are synchronized with each other.

#### Data processing

The data that was transmitted to the module in the current bus cycle via the control interface takes effect when it is processed in the module's internal cycle. The counter value and status bits are detected at time T<sub>i</sub> and made available in the feedback interface for retrieval in the current bus cycle.

#### Additional information

You will find detailed description of the isochronous mode:

- In the Isochronous mode function manual as a download from the [Internet](https://support.industry.siemens.com/cs/ww/en/view/109755401) .
- In the PROFINET with STEP 7 function manual as a download from the [Internet](https://support.industry.siemens.com/cs/ww/en/view/49948856).

## Basics of counting (digital modules) (S7-1500)

This section contains information on the following topics:

- [Overview of applications (S7-1500)](#overview-of-applications-s7-1500-2)
- [Counting with pulse encoders (S7-1500)](#counting-with-pulse-encoders-s7-1500)
- [Behavior at the counting limits (S7-1500)](#behavior-at-the-counting-limits-s7-1500-1)
- [Gate control (S7-1500)](#gate-control-s7-1500)
- [Comparison values (S7-1500)](#comparison-values-s7-1500-1)
- [Interrupts (S7-1500)](#interrupts-s7-1500-1)
- [24 V count signals (S7-1500)](#24-v-count-signals-s7-1500-1)
- [Isochronous mode (S7-1500)](#isochronous-mode-s7-1500-1)
- [Counting once with direction setting via digital input (S7-1500)](#counting-once-with-direction-setting-via-digital-input-s7-1500)

### Overview of applications (S7-1500)

#### Introduction

You configure the digital module and assign its parameters using the configuration software.

The module's functions are controlled and monitored via the user program with the control and feedback interface.

#### System environment

The respective module can be used in the following system environments:

| Applications | Components required | Configuration software | In the user program |
| --- | --- | --- | --- |
| Central operation with a S7-1500 CPU or ET 200SP CPU | - S7-1500 automation system or ET 200SP CPU - Digital module | STEP 7 (TIA Portal):  Device configuration and parameter setting with hardware configuration | Direct access to the control and feedback interface of the digital module in the I/O data |
| Distributed operation with a S7-1500 CPU | - S7-1500 Automation System - ET 200 Distributed I/O System - Digital module |  |  |
| Distributed operation with a S7-300/400 CPU | - S7-300/400 automation system - ET 200 distributed I/O system - Digital module | STEP 7 (TIA Portal):  Device configuration and parameter setting with hardware configuration  STEP 7:  Device configuration and parameter setting with hardware configuration (ET 200SP) or GSD file (ET 200MP) |  |
| Distributed operation in a third-party system | - Third-party automation system - ET 200 distributed I/O system - Digital module | Third-party configuration software:  Device configuration and parameter settings with GSD file |  |

> **Note**
>
> A description of the control and feedback interface is available in the device manual for the digital module.

### Counting with pulse encoders (S7-1500)

Counting refers to the detection and summation of events. The modules' counters record and evaluate pulse signals. The counting direction can be specified using encoder or pulse signals or through the configuration.

You can use feedback bits to switch the digital outputs of digital output modules at defined counter values.

You can configure the characteristics of the counters using the functionalities described below.

#### Counter limits

The counter limits define the counter value range used. The counter limits are configurable and can be modified during runtime using the user program. See the module's device manual for the maximum and minimum configurable counter limits.

You can configure whether the counting processes are terminated or continue when a counter limit is violated (automatic gate stop).

#### Start value

You can configure a start value within the counter limits. The start value can be modified during runtime with the user program.

#### Gate control

Opening and closing the hardware gate and software gate defines the period of time during which the counting signals are recordd.

The hardware gate is controlled externally via a digital input of the digital module. The hardware gate can be enabled through parameter assignment. The software gate is controlled via the user program. A description of the control and feedback interface is available in the device manual for the digital module.

### Behavior at the counting limits (S7-1500)

#### Violation of a counting limit

The high counting limit is violated when the current counter value is equal to the high counting limit and another upward count pulse is received. The counter low limit is violated when the current counter value is equal to the counter low limit and another downward count pulse is received.

For digital modules of ET 200SP and ET 200AL, the corresponding event bit is set in the feedback interface when the limit is exceeded. You can reset an event bit with the respective control bit:

| Counting limit violated | Event bit | Reset bit |
| --- | --- | --- |
| High counting limit | EVENT_OFLW | RES_EVENT_OFLW |
| Low counting limit | EVENT_UFLW | RES_EVENT_UFLW |

> **Note**
>
> A description of the control and feedback interface is available in the device manual for the digital module.

You can configure whether or not you want to continue counting to another counter limit after a counting limit violation.

> **Note**
>
> The high counting limit and the start value define the value range of the counter:
>
> Value range of the counter = (high limit – start value) + 1

#### Examples

The figure below shows an example for terminating counting after overflow and setting the counter to the opposite counting limit:

![Examples](images/73783667083_DV_resource.Stream@PNG-en-US.png)

The figure below shows an example for continuing the counting process after an overflow and setting the counter to the opposite counting limit:

![Examples](images/73783683851_DV_resource.Stream@PNG-en-US.png)

### Gate control (S7-1500)

This section contains information on the following topics:

- [Gate functions (S7-1500)](#gate-functions-s7-1500-1)
- [Software gate (S7-1500)](#software-gate-s7-1500-1)
- [Hardware gate (S7-1500)](#hardware-gate-s7-1500-1)
- [Internal gate (S7-1500)](#internal-gate-s7-1500-1)
- [Counting once with hardware gate (S7-1500)](#counting-once-with-hardware-gate-s7-1500)

#### Gate functions (S7-1500)

Many applications require counting processes to be started or stopped in accordance with other events. In such cases, counting is started and stopped using the gate function.

The digital modules have two gates for each counting channel. These define the resulting internal gate:

- Software gate
- Hardware gate

> **Note**
>
> The hardware gate is not available for all digital modules.

#### Software gate (S7-1500)

The software gate of the channel is opened and closed with the SW_GATEcontrol bit.

> **Note**
>
> A description of the control and feedback interface is available in the device manual for the digital module.

#### Hardware gate (S7-1500)

The hardware gate is optional. You open and close the hardware gate using signals at the corresponding digital input.

> **Note**
>
> A configurable input delay delays the control signal of the digital input.

The status of a DIm digital input is indicated by the respective STS_DIm feedback bit. A description of the control and feedback interface is available in the device manual for the digital module.

##### Opening and closing the hardware gate

The figure below shows an example of opening and closing with a digital input:

![Opening and closing the hardware gate](images/73783945867_DV_resource.Stream@PNG-en-US.png)

As long as the digital input is set, the hardware gate is open and the count pulses are counted. The hardware gate is closed when the digital input is reset. The counter value stays constant and ignores any further count pulses.

#### Internal gate (S7-1500)

##### Internal gate

The internal gate is open if the software gate is open and the hardware gate is open or has not been configured. The status of the internal gate is indicated by the STS_GATE feedback bit. A description of the control and feedback interface is available in the device manual for the digital module.

If the internal gate is open, counting is started. If the internal gate is closed, all other count pulses are ignored and counting is stopped.

If you want to control a counting process with the hardware gate only, the software gate must be open. If you do not configure a hardware gate, the hardware gate is considered to be always open. In this case, you open and close the internal gate with the software gate only.

| Hardware gate | Software gate | Internal gate |
| --- | --- | --- |
| Open/not configured | open | open |
| Open/not configured | closed | closed |
| closed | open | closed |
| closed | closed | closed |

The internal gate can also be automatically closed upon violation of a counting limit. The software or hardware gate must then be closed and reopened to continue counting.

#### Counting once with hardware gate (S7-1500)

##### One-time counting with hardware gate

The following section describes the one-time counting with hardware gate (HW_Gate).

The counting process stops when the high counting limit is violated. The count value jumps to the lower count limit (= 0).

When counting with hardware gate, the software gate (SW_Gate) and the hardware gate must be set (AND operation). When counting once, the software gate must be set and is controlled with the hardware gate, i.e. when the limit is reached, the counter stops and only when the hardware gate is reset and set again does the counter restart.

If the "SW_Gate" control bit or the hardware gate is reset before the high counting limit is reached, the counter stops.

The following picture shows an example of the principle for counting with hardware gate.

![Principle: Counting with hardware gate](images/154134953867_DV_resource.Stream@PNG-en-US.png)

Principle: Counting with hardware gate

### Comparison values (S7-1500)

Depending on the module, you can define up to two comparison values that control a feedback bit for the channel, independent of the user program.

When there are two comparison values, comparison value 1 must be greater than comparison value 0. The comparison values are configurable and can be modified during runtime using the user program.

The comparison values are compared with the current counter value. If the counter value meets the configured comparison condition, the respective STS_DQ feedback bit is set.

You can use the respective feedback bit in order to switch a digital output module's digital output. You can make setting the respective STS_DQ feedback bit dependent on one of the following comparison events. See the device manual for the digital module to find out which comparison events can be configured.

#### Setting between comparison value and high counter limit

The respective STS_DQ feedback bit is set to 1 when:

Comparison value &lt;= counter value &lt;= high counter limit

![Setting between comparison value and high counter limit](images/74664531083_DV_resource.Stream@PNG-en-US.png)

#### Setting between comparison value and low counter limit

The respective STS_DQ feedback bit is set to 1 when:

Low counter limit &lt;= counter value &lt;= comparison value

![Setting between comparison value and low counter limit](images/74664546955_DV_resource.Stream@PNG-en-US.png)

#### Setting between comparison value 0 and comparison value 1

The respective STS_DQ feedback bit is set to 1 when:

Comparison value 0 &lt;= counter value &lt;= comparison value 1

![Setting between comparison value 0 and comparison value 1](images/74663811211_DV_resource.Stream@PNG-en-US.png)

#### Not setting between comparison value 0 and comparison value 1

The respective STS_DQ feedback bit is set to 1 when:

Comparison value 0 &lt;= counter value &lt;= comparison value 1

![Not setting between comparison value 0 and comparison value 1](images/74664562827_DV_resource.Stream@PNG-en-US.png)

### Interrupts  (S7-1500)

#### Hardware interrupt

The modules can trigger a hardware interrupt in the CPU for certain events during operation. Process interrupts are enabled via the parameter assignment. Refer to the device manual for the module for information about the events that can trigger a hardware interrupt during operation.

> **Note**
>
> Hardware interrupts for counting are not available at all the modules.

### 24 V count signals (S7-1500)

#### 24 V pulse encoder count signals

An encoder, for example an initiator (BERO) or a light barrier, returns a count signal that is connected to the terminal of a counter. For some modules you change the count direction via the parameter assignment of the DI function.

The figure below shows an example of the time profile of the signals of a 24 V pulse encoder with direction signal and the resulting count pulses:

![24 V pulse encoder count signals](images/113345091851_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> A signal for direction detection is not connectable for all digital modules.

### Isochronous mode (S7-1500)

The digital module supports the system function "Isochronous mode". This system function enables counter values to be acquired in a defined system cycle.

In isochronous mode, the cycle of the user program, the transmission of the input and output data and the processing in the module are synchronized with each other.

#### Data processing

The data that was transmitted to the module in the current bus cycle via the control interface takes effect when it is processed in the module's internal cycle. The counter value and status bits are detected at time T<sub>i</sub> and made available in the feedback interface for retrieval in the current bus cycle.

#### Additional information

You will find detailed description of the isochronous mode:

- In the Isochronous mode function manual as a download from the [Internet](https://support.industry.siemens.com/cs/ww/en/view/109755401) .
- In the PROFINET with STEP 7 function manual as a download from the [Internet](https://support.industry.siemens.com/cs/ww/en/view/49948856).

### Counting once with direction setting via digital input (S7-1500)

#### Counting once with direction setting via digital input

The following section describes the direction setting via a digital input.

The "Digital input" count direction is set via the parameters. This means that the count direction is specified via the "Partner digital input".

Count direction:

- "0" up
- "1" down

The start command determines the behavior when starting the counter:

- The counting process starts with the current count value.
- The counting process starts with the start value that was specified via parameter/command interface.

The following figure shows an example of the principle for counting with direction setting via a digital input.

![Principle: Counting with direction specification](images/154125528971_DV_resource.Stream@PNG-en-US.png)

Principle: Counting with direction specification

## Basics of counting (SIMATIC Drive Controller) (S7-1500)

This section contains information on the following topics:

- [Overview of applications (S7-1500)](#overview-of-applications-s7-1500-3)
- [Event counter (S7-1500)](#event-counter-s7-1500)
- [Period duration measurement (S7-1500)](#period-duration-measurement-s7-1500)
- [Isochronous mode (S7-1500)](#isochronous-mode-s7-1500-2)

### Overview of applications (S7-1500)

#### Introduction

You configure the X142 technology I/Os of the SIMATIC Drive Controller and assign its parameters with the STEP 7 configuration software. The event counter and the period duration measurement are evaluated via the feedback interface of the X142 technology I/Os in the IO data.

> **Note**
>
> A description of the control and feedback interface is available in the [SIMATIC Drive Controller system manual](https://support.industry.siemens.com/cs/ww/en/view/109766665).

#### System environment

The SIMATIC Drive Controllers can be used in the following system environment:

| Application scenarios | Components required | Configuration software | In the user program |
| --- | --- | --- | --- |
| Drive-based automation solution with SIMATIC Drive Controller | - SIMATIC Drive Controller<sup>1</sup> - SINAMICS S120 drive components (power units, ...) | STEP 7<sup>1</sup> and SINAMICS S120 Startdrive (TIA Portal):   [Device configuration and parameter setting](Using%20the%20module%20%28S7-1500%29.md#configuration-and-parameter-assignment-of-simatic-drive-controller-s7-1500) | Direct access to control and feedback interface of the X142 technology I/Os |
| <sup>1</sup> Required for X142 technology I/Os |  |  |  |

### Event counter (S7-1500)

You can use up to 8 channels of the X142 technology I/Os for counting tasks.

With the event counter (16-bit value), you measure the number of positive edges per application cycle via the feedback interface.

The event counter is a circumferential counter.

- An overflow of the event counter is not displayed.
- The exact value must be calculated from the difference.

#### Count direction

Counting always takes place in the forward direction.

### Period duration measurement (S7-1500)

You can use up to 8 channels of the X142 technology I/Os for period duration measurement.

With period duration measurement (32-bit value), you measure the number of increments of 41.67 ns between the last two incoming positive edges in the application cycle via the feedback interface.

Period duration = 41.67 ns x number of increments

### Isochronous mode (S7-1500)

The event/period duration measurement requires isochronous operation.

You can find more information in the [SIMATIC Drive Controller system manual](https://support.industry.siemens.com/cs/ww/en/view/109766665).

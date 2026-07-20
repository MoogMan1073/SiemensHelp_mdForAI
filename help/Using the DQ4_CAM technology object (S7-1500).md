---
title: "Using the DQ4_CAM technology object (S7-1500)"
package: TFTODQ4CAMenUS
topics: 17
devices: [S7-1500, S7-1500T]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Using the DQ4_CAM technology object (S7-1500)

This section contains information on the following topics:

- [Technology object DQ4_CAM (S7-1500)](#technology-object-dq4_cam-s7-1500)
- [Overview of the configuration steps (S7-1500)](#overview-of-the-configuration-steps-s7-1500)
- [Add technology object (S7-1500)](#add-technology-object-s7-1500)
- [Configuring DQ4_CAM (S7-1500)](#configuring-dq4_cam-s7-1500)
- [Programming DQ4_CAM (S7-1500)](#programming-dq4_cam-s7-1500)
- [Commissioning DQ4_CAM (S7-1500)](#commissioning-dq4_cam-s7-1500)
- [DQ4_CAM Diagnostics (S7-1500)](#dq4_cam-diagnostics-s7-1500)

## Technology object DQ4_CAM (S7-1500)

During the configuration, commissioning and diagnosis of the cam control functions for the DQ 4x24VDC/2A HS output module in combination with an encoder module, STEP 7 (TIA Portal) supports you with the "Technology objects" function:

- In STEP 7 (TIA Portal) you configure the DQ4_CAM technology object by entering the encoder parameters.
- The corresponding DQ4_CAM instruction is programmed in the user program. This instruction takes over the supply of the control and feedback interface of the output module. The encoder data are hereby transferred to the output module and processed there.

The DQ4_CAM technology object corresponds to the instance DB of the instruction DQ4_CAM. The configuration of the cam control functions is saved in the technology object. The technology object is located in the folder "PLC &gt; Technology objects".

### Operating mode

To parameterize a DQ 4x24VDC/2A HS via the technology object, specify the operating mode "Cam control" and the control mode "Use technology object "DQ4_CAM"" in the hardware configuration of the DQ 4x24VDC/2A HS.

## Overview of the configuration steps (S7-1500)

### Introduction

The following overview shows the basic procedure for configuring the cam control functions of the DQ 4x24VDC/2A HS output module via the technology object DQ4_CAM.

### Requirement

To use the technology object DQ4_CAM, a project must be created in STEP 7 (TIA Portal) with an S7-1500 CPU. The output module DQ 4x24VDC/2A HS and the encoder module must be added, but not necessarily in the same station.

> **Note**
>
> The interface module used must support the value status function.

### Procedure

Proceed in the recommended sequence outlined below:

| Step | Description |
| --- | --- |
| 1 | Configure output module and encoder module |
| 2 | [Add technology object](#add-technology-object-s7-1500) |
| 3 | [Configure a technology object according to your application](#configuring-dq4_cam-s7-1500) |
| 4 | [Call instruction in the user program](#call-instruction-in-the-user-program-s7-1500) |
| 5 | Load to CPU |
| 6 | [Commissioning the technology object](#commissioning-the-technology-object-s7-1500) |
| 7 | [Diagnostics of the technology object](#dq4_cam-diagnostics-s7-1500) |

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
5. Select the "DQ4_CAM" object.
6. Enter an individual name for the technology object in the "Name" text box.
7. Click "Additional information" if you want to add your own information to the technology object.
8. Confirm with "OK".

### Result

The new technology object has now been created and stored in the project tree in the "Technology objects" folder.

![Result](images/135289111947_DV_resource.Stream@PNG-en-US.PNG)

|  | Object | Description |
| --- | --- | --- |
| ① | [Configuration](#configuring-dq4_cam-s7-1500) | In the configuration dialog:  - Mapping of the encoder module, the encoder module channel and the output module - Setting the parameters of the technology object for the cam control functions   When you change the configuration of the technology object, you must download the technology object **and** the hardware configuration to the CPU. |
| ② | [Commissioning](#commissioning-the-technology-object-s7-1500) | Commissioning and function test of the technology object:  Controlling parameters of the DQ4_CAM instruction and monitoring the effects |
| ③ | [Diagnostics](#dq4_cam-diagnostics-s7-1500) | Monitoring of the cam control functions |

## Configuring DQ4_CAM (S7-1500)

This section contains information on the following topics:

- [Working with the configuration dialog (S7-1500)](#working-with-the-configuration-dialog-s7-1500)
- [Hardware interface (S7-1500)](#hardware-interface-s7-1500)
- [General parameters (S7-1500)](#general-parameters-s7-1500)
- [Cam parameters (S7-1500)](#cam-parameters-s7-1500)
- [Output parameters (S7-1500)](#output-parameters-s7-1500)

### Working with the configuration dialog (S7-1500)

You configure the properties of the technology object in the configuration window. Proceed as follows to open the configuration window of the technology object:

1. Open the "Technology objects" folder in the project tree.
2. Open the technology object in the project tree.
3. Double-click on the "Configuration" object.

The configuration is divided into the following categories:

- **Hardware interface**

  Connection between technology object and encoder module/output module
- **General parameters**

  Parameters for setting the encoder value range.
- **Cam parameters**

  Parameters for setting the behavior of the output module cams.
- **Output parameters**

  Parameters for setting the behavior of the digital outputs of the output module.

![Figure](images/138656288267_DV_resource.Stream@PNG-en-US.PNG)

#### Configuration window icons

Icons in the area navigation of the configuration show additional details about the status of the configuration:

| Symbol | Meaning |
| --- | --- |
| ![Configuration window icons](images/41244027019_DV_resource.Stream@PNG-de-DE.png) | **The configuration contains default values and is complete**.  The configuration contains only default values. With these default values, you can use the technology object without additional changes. |
| ![Configuration window icons](images/41244015115_DV_resource.Stream@PNG-de-DE.png) | **The configuration contains values set by the user or automatically adapted values and is complete**   All text boxes of the configuration contain valid values and at least one default value was changed. |
| ![Configuration window icons](images/41243964811_DV_resource.Stream@PNG-de-DE.png) | **The configuration is incomplete or incorrect**   At least one text box or drop-down list contains an invalid value. The corresponding field or the drop-down list is displayed on a red background. Click the roll-out error message to indicate the cause of error. |

#### Synchronization of the parameter values

When you change the configuration of the technology object, you must download the technology object and the hardware configuration to the CPU.

Within STEP 7 (TIA Portal), the parameter values in the property dialog of the assigned module are overwritten by the parameter values of the technology object. The current parameter values of the technology object are displayed in the property dialog of the module (read-only).

### Hardware interface (S7-1500)

Under "Hardware interface" you establish the connection between the technology object DQ4_CAM, the encoder module and the output module DQ 4x24VDC/2A HS.

#### Encoder module

In a follow-up dialog box, select the module to which the encoder you want to use is connected. If you do not use an MtM, the encoder module does not necessarily have to be in the same station as the output module. Depending on the encoder module, the value status of the encoder module and the direction of the encoder are supplied in the encoder data in addition to the encoder value, and processed in the cam control.

The following table lists the "encoder modules" that you can use under the S7-1500 CPU or ET 200SP CPU.

| Encoder module | Operating mode | Value status | Direction |
| --- | --- | --- | --- |
| DI 8x24VDC HS | Counting | ‒ | ‒ |
| AI 2xU/I 2-/4-wire HS | ‒ | x<sup>1</sup> | ‒ |
| AI 2xSG 4-/6-wire HS | ‒ | x | ‒ |
| TM Count 1x24VDC | - Operating with technology object "Counting and measurement" - Manual operation (without technology object) - Fast Mode | x | x |
| TM PosInput 1 | x | x |  |
| <sup>1</sup> In the configuration variant with QI |  |  |  |

The value status of the encoder module affects the value status of the output module. If the value status of the encoder module is invalid, the value status of the output module (static tag QI_CHn) is set to 0.

For encoder modules that do not provide a direction in the encoder data, it must be ensured that two valid, different encoder values are available before the direction is recognized.

After selecting the encoder module, you can click the "Device configuration" button to open the device configuration belonging to the module.

> **Note**
>
> You can assign an encoder module to several technology objects if necessary.

#### Channel

In the case of an encoder module with several channels, select the number of the channel that is to be used as encoder value.

#### Output module

In a follow-up dialog box, select the output module DQ 4x24VDC/2A HS.

After selecting the output module, you can click the "Device configuration" button to open the device configuration associated with the output module. The parameter settings of the output module required for using the technology object are made via the parameters of the technology object.

> **Note**
>
> An output module can be assigned to only one technology object. An output module that is already assigned to a technology object can no longer be selected.

#### Data transmission

Use this parameter to define how the encoder data is transferred to the output module.

You can select from the following options:

| Data transmission | Meaning |
| --- | --- |
| Via CPU (default) | The encoder data is transferred to the output module with the user program. |
| Via Module to Module Communication | The encoder data is transferred to the output module via Module to Module Communication (MtM).  The reaction time of the cam controller is thereby reduced to the duration of a backplane bus cycle. A backplane bus cycle typically corresponds to one PROFINET cycle. |

#### Synchronization of the parameter values

If, after assigning the output module to the technology object, there is an inconsistency between the parameter values in the properties dialog of the output module and in the technology object, a button appears with a message indicating this. When you click the button, the parameter values in the property dialog of the assigned module are overwritten by the parameter values of the technology object within STEP 7 (TIA Portal). The current parameter values of the technology object are displayed in the property dialog of the module (read-only).

> **Note**
>
> If you change parameter values of the technology object, the corresponding parameter values are also overwritten without prompt in the properties dialog of the hardware configuration. As after every change in hardware configuration, the next time the project is loaded in the CPU, a prompt appears asking whether the CPU should go to STOP mode.

### General parameters (S7-1500)

#### Enable modulo

With this parameter you map the encoder value to a repeating modulo range. The modulo range is determined by "Minimum encoder value" and "Maximum encoder value".

![Enable modulo](images/133704952459_DV_resource.Stream@PNG-en-US.png)

This parameter is deactivated in the default setting.

#### Hysteresis (in increments)

With the parameterization of the [hysteresis](Cam%20control%20basics%20%28S7-1500%29.md#hysteresis-s7-1500) you specify a range around the encoder value that is activated after a change of direction. In the hysteresis range, the cams cannot switch again before the encoder value has left this range.

The hysteresis setting must satisfy the following conditions:

- Hysteresis &lt; (Maximum encoder value – Minimum encoder value) / 4
- Hysteresis &lt; End position – Start position

If you enter "0", the hysteresis is switched off. You can enter a value between 0 and 65535. The default setting is "0".

#### Axis reference position

With the parameter assignment of the axis reference position you adapt the encoder value, for example, to take into account the zero position of the sensor. The axis reference position is subtracted from the encoder value before further processing of the encoder value.

You can enter a value between –2147483648 and 2147483647. The default setting is "0".

#### Maximum encoder value

With this parameter you specify the upper value of the valid encoder range.

"Maximum encoder value" must be at least 2 greater than "Minimum encoder value".

If you have activated the "Modulo" parameter, the following applies:

- Maximum encoder value – Minimum encoder value &lt;= 2147483646
- Maximum encoder value forms the upper limit of the modulo range.

You can enter a value between –2147483646 and 2147483647. The default setting is "2147483646".

#### Minimum encoder value

With this parameter you specify the lower value of the valid encoder range.

"Minimum encoder value" must be at least 2 less than "Maximum encoder value".

If you have activated the "Modulo" parameter, the following applies:

- Maximum encoder value – Minimum encoder value &lt;= 2147483646
- Minimum encoder value forms the lower limit of the modulo range.

You can enter a value between –2147483648 and 2147483645. The default setting is "0".

### Cam parameters (S7-1500)

#### Channel assignment

With the parameter assignment of the channel, you specify the digital output on which the cam is output.

If several cams are assigned to the same digital output, their switch-on ranges must not overlap.

The default setting is "Channel 0".

#### "Start position / end position"

With the parameter assignment of the two position values, you define the lower and upper value of the [switch-on range of the cam](Cam%20control%20basics%20%28S7-1500%29.md#start-and-end-position-s7-1500).

If the modulo is disabled:

- Minimum encoder value &lt;= Cam start position &lt; Cam end position &lt;= Maximum encoder value

When modulo is enabled, the following applies:

- Minimum encoder value &lt;= Cam start position &lt;= Maximum encoder value
- Minimum encoder value &lt;= Cam end position &lt;= Maximum encoder value

The default setting is "0" in each case.

> **Note**
>
> If several cams are assigned to the same digital output, their switch-on ranges must not overlap.

#### Effective direction

With this parameter you specify the [direction of movement](Cam%20control%20basics%20%28S7-1500%29.md#start-and-end-position-s7-1500) in which the respective cam acts.

You can select from the following options:

| Effective direction | Meaning |
| --- | --- |
| None (default) | The cam is switched off. |
| Positive | The cam only switches between the two position values when motion is forwards. |
| Negative | The cam only switches between the two position values when motion is backwards. |
| Both | The cam switches between the two position values regardless of the direction of movement. |

### Output parameters (S7-1500)

#### Channel activated

With this parameter you specify whether the respective channel of the digital output module is used.

This parameter is activated in the default setting.

#### Pulsed cam output period

With this parameter to specify the period duration for the [pulsed output of the cam signal](Cam%20control%20basics%20%28S7-1500%29.md#pulsed-cam-output-s7-1500).

The "None" option leads to a continuous cam signal.

The default setting is "0.93 ms" in each case.

#### Pulsed cam output duty cycle

This parameter is used to specify the pulse-period ratio (also called switch-on duration or duty cycle) of the [pulsed output signal](Cam%20control%20basics%20%28S7-1500%29.md#pulsed-cam-output-s7-1500) on the respective channel as a percentage.

The default setting is "50.0" in each case.

#### Reaction to CPU STOP

This parameter is used to specify the reaction of the digital output of the respective channel in case of a CPU STOP and in case of invalid encoder values.

You can select from the following options:

| Reaction to CPU STOP | Meaning |
| --- | --- |
| Shutdown (default) | The channel outputs value "0" at the digital output until the next STOP-RUN transition of the CPU or the next valid encoder values. |
| Keep last value | Until the next STOP-RUN transition of the CPU or the next valid encoder values, the channel outputs at the digital output the value that was valid at the time of the transition to STOP. A pulsed cam output continues to be effective. |
| Output substitute value 1 | The channel outputs value "1" at the digital output until the next STOP-RUN transition of the CPU or the next valid encoder values. A pulsed cam output continues to be effective. |

## Programming DQ4_CAM (S7-1500)

This section contains information on the following topics:

- [Instruction DQ4_CAM (S7-1500)](#instruction-dq4_cam-s7-1500)
- [Call instruction in the user program (S7-1500)](#call-instruction-in-the-user-program-s7-1500)

### Instruction DQ4_CAM (S7-1500)

#### DQ4_CAM

The instruction DQ4_CAM belongs to the technology object DQ4_CAM and supplies the control and feedback interface of the output module DQ 4x24VDC/2A HS.

The DQ4_CAM instruction thus forms the software interface between the user program and the output module. It must be called cyclically from the user program in order to synchronize the input and output data.

The output module can be used centrally or in distributed operation. The instruction applies in each case to the channel of the encoder module and the output module, both of which are assigned to the associated technology object.

#### Additional information

[Description DQ4_CAM](DQ4_CAM%20%28S7-1500%29.md#description-dq4_cam-s7-1500)

[Input parameters DQ4_CAM](DQ4_CAM%20%28S7-1500%29.md#input-parameters-dq4_cam-s7-1500)

[Output parameters DQ4_CAM](DQ4_CAM%20%28S7-1500%29.md#output-parameters-dq4_cam-s7-1500)

[Static tags DQ4_CAM](DQ4_CAM%20%28S7-1500%29.md#static-tags-dq4_cam-s7-1500)

[UDT DQ4_CAM_Parameters](DQ4_CAM%20%28S7-1500%29.md#udt-dq4_cam_parameters-s7-1500)

[Error codes of parameter Status](DQ4_CAM%20%28S7-1500%29.md#error-codes-of-parameter-status-s7-1500)

[Reaction to encoder errors](DQ4_CAM%20%28S7-1500%29.md#reaction-to-encoder-errors-s7-1500)

### Call instruction in the user program (S7-1500)

The DQ4_CAM instruction can be called once for each output module in the cycle or, alternatively, in a time-controlled program. The call is not permitted in an event-controlled interrupt program.

#### Requirements

- Encoder and output module are assigned to a common process image partition.
- The instruction is called in the OB to which the process image partition is assigned.

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

## Commissioning DQ4_CAM (S7-1500)

This section contains information on the following topics:

- [Commissioning the technology object (S7-1500)](#commissioning-the-technology-object-s7-1500)

### Commissioning the technology object (S7-1500)

A graphic display of an operating diagram for the digital output signals in the commissioning editor helps you with commissioning and the function test for the technology object. You can change specific parameters of the DQ4_CAM instruction in CPU online mode and monitor their effects.

#### Requirements

- There is an online connection between STEP 7 (TIA Portal) and the CPU.
- The CPU is in RUN.
- The corresponding DQ4_CAM instruction is called cyclically from the user program.
- The input parameters of the technology object are not overwritten by the user program.

> **Note**
>
> Input parameters in the DQ4_CAM instruction that are connected in the user program can no longer be operated in the commissioning editor.

#### Procedure

To open the commissioning editor of a technology object and to control a parameter value change, follow these steps:

1. Open the "Technology objects" folder in the project tree.
2. Open the DQ4_CAM technology object in the project tree.
3. Double-click on the "Commissioning" object.  
   The functions for commissioning the DQ4_CAM technology object are displayed.
4. In the commissioning dialog box, click the button "Monitor all".  
   The parameters (online values) of the technology object DQ4_CAM are loaded and displayed.
5. If you want to change a parameter, select the check box of the parameter.  
   The parameter value is changed.

#### Online mode

In online mode, you can modify the following parameters to test the technology object function:

- [CtrlDQn](DQ4_CAM%20%28S7-1500%29.md#input-parameters-dq4_cam-s7-1500)
- [SetDQn](DQ4_CAM%20%28S7-1500%29.md#input-parameters-dq4_cam-s7-1500)

![Online mode](images/139513530251_DV_resource.Stream@PNG-en-US.png)

## DQ4_CAM Diagnostics (S7-1500)

This section contains information on the following topics:

- [Monitor encoder values and DQs (S7-1500)](#monitor-encoder-values-and-dqs-s7-1500)

### Monitor encoder values and DQs (S7-1500)

The diagnostics functions is used to monitor the encoder values and the cam functions.

#### Requirements

- There is an online connection between STEP 7 (TIA Portal) and the CPU.
- The CPU is in RUN.
- The associated instruction DQ4_CAM is called cyclically from the user program.

#### Procedure

To open the display editor for the diagnostic functions, follow these steps:

1. Open the "Technology objects" folder in the project tree.
2. Open the DQ4_CAM technology object in the project tree.
3. Double-click on the "Diagnostics" object.
4. Click the "Monitor all" button.

#### Display

The following values are read by the technology object from the feedback interface of the output module and displayed:

- Event display/diagnostics information
- Signal states of the digital outputs
- Encoder value
- Read register value:

Additional information on status displays is available in the context-sensitive help for each event in STEP 7 (TIA Portal). When the CPU is in STOP, the status display is not updated.

![Display](images/138829622667_DV_resource.Stream@PNG-en-US.png)

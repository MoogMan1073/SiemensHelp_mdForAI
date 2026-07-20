---
title: "Cam control basics (S7-1500)"
package: TFCamBasics15enUS
topics: 9
devices: [S7-1500, S7-1500T]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Cam control basics (S7-1500)

This section contains information on the following topics:

- [Overview of applications (S7-1500)](#overview-of-applications-s7-1500)
- [Cam control (S7-1500)](#cam-control-s7-1500)
- [Start and end position (S7-1500)](#start-and-end-position-s7-1500)
- [Hysteresis (S7-1500)](#hysteresis-s7-1500)
- [Pulsed cam output (S7-1500)](#pulsed-cam-output-s7-1500)

## Overview of applications (S7-1500)

This section contains information on the following topics:

- [Parameterization and control options (S7-1500)](#parameterization-and-control-options-s7-1500)
- [Configuration via technology object (S7-1500)](#configuration-via-technology-object-s7-1500)
- [Parameter setting via hardware configuration with MtM communication (S7-1500)](#parameter-setting-via-hardware-configuration-with-mtm-communication-s7-1500)

### Parameterization and control options  (S7-1500)

You configure and parameterize the output module DQ 4x24VDC/2A HS using STEP 7 (TIA Portal).

You have two alternative options for parameterizing and controlling the functions of the output module:

- Configuration using the technology object and control with the corresponding instruction   
  The technology module control and feedback interface is accessed with the technology object.  
  The encoder data is transferred either with the technology object (user program) or via Module to Module Communication (MtM) to the output module and processed there.
- Parameter settings via hardware configuration  
  Access to the control and feedback interface of the output module takes place through direct access of the user program to the I/O data.  
  The encoder data are transferred via Module to Module Communication (MtM) and processed by the output module.

### Configuration via technology object (S7-1500)

For central and distributed use, we recommend the convenient, graphics-assisted configuration using a technology object. A detailed description of this configuration can be found starting from section [Technology object DQ4_CAM](Using%20the%20DQ4_CAM%20technology%20object%20%28S7-1500%29.md#technology-object-dq4_cam-s7-1500).

For the device configuration of the output module, specify "Cam control" mode and "Use "DQ4_CAM" technology object" control mode.

When assigning the parameters of the [Hardware interface](Using%20the%20DQ4_CAM%20technology%20object%20%28S7-1500%29.md#hardware-interface-s7-1500) in the technology object, you decide the assignment to the encoder module and to the output module and specify the type of data transmission.

#### Data transmission via the CPU

Here you parameterize as Data transmission "by controller".

> **Note**
>
> Encoder module and output modules may be located in different stations or in the same station. This applies to centralized as well as distributed operation.

The following figure shows the data exchange process when using the technology object without MtM communication.

![Data transmission via the CPU](images/138717747979_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Read encoder signals into encoder module |
| ② | Transfer encoder signals to interface module |
| ③ | Transfer encoder signals to technology object |
| ④ | Transfer encoder signals to interface module |
| ⑤ | Transfer encoder signals to output module |
| ⑥ | Process encoder signals in the output module and output signals |

The scope of the input and output addresses of the output module for data transmission via the CPU is:

|  | Inputs | Outputs |
| --- | --- | --- |
| Range | 14 bytes | 13 bytes or 23 bytes, depending on the encoder module used |

#### Data transmission via MtM communication

Here you parameterize as Data transmission "via Module to Module Communication".

> **Note**
>
> Data transmission via MtM communication can only be used in conjunction with an interface module that supports Module to Module Communication (MtM). In addition, the encoder module and output module must be in the same station.

The figure below shows the data exchange process when using the technology object with MtM communication.

![Data transmission via MtM communication](images/138717751819_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Read encoder signals into encoder module |
| ② | Transfer encoder signals to interface module |
| ③ | Transfer encoder signals to output module |
| ④ | Process encoder signals in the output module and output signals |

The scope of the input and output addresses of the output module for data transmission via MtM communication is:

|  | Inputs | Outputs |
| --- | --- | --- |
| Range | 14 bytes | 7 bytes |

When using Module to Module Communication (MtM), the reaction time of the cam controller is reduced to the duration of a backplane bus cycle. A backplane bus cycle typically corresponds to one PROFINET cycle.

You can find more information on Module-to-Module Communication (MtM) in the FAQ with entry ID [109767618](https://support.industry.siemens.com/cs/ww/en/view/109767618) in Siemens Industry Online Support.

### Parameter setting via hardware configuration with MtM communication (S7-1500)

For the device configuration of the output module, specify "Cam control" mode and "Use MtM without technology object" control mode. Additional support for setting parameters via the hardware configuration and a description of the control and feedback interface can be found in the equipment manual of the output module.

> **Note**
>
> Data transmission via MtM communication can only be used in conjunction with an interface module that supports Module to Module Communication (MtM). In addition, the encoder module and output module must be in the same station.

The figure below shows the data exchange process when using MtM communication (without technology object).

![Figure](images/138717751819_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Read encoder signals into encoder module |
| ② | Transfer encoder signals to interface module |
| ③ | Transfer encoder signals to output module |
| ④ | Process encoder signals in the output module and output signals |

The scope of the input and output addresses of the output module for data transmission via MtM communication is:

|  | Inputs | Outputs |
| --- | --- | --- |
| Range | 14 bytes | 7 bytes |

When using Module to Module Communication (MtM), the reaction time of the cam controller is reduced to the duration of a backplane bus cycle. A backplane bus cycle typically corresponds to one PROFINET cycle.

You can find more information on Module-to-Module Communication (MtM) in the FAQ with entry ID [109767618](https://support.industry.siemens.com/cs/ww/en/view/109767618) in Siemens Industry Online Support.

## Cam control (S7-1500)

With cam control, switching signals are generated depending on an encoder value. Encoder values can, for example, originate from a linear axis, from a rotary axis with modulo function, or from analog values.

The current actual position value of the axis is determined by an encoder to which an encoder module is connected. The encoder signals are hereby evaluated, e.g. the pulses counted that are proportional to the distance moved. The parameterized switch-on ranges of the cams are compared with the actual position value (encoder value). The digital outputs of the output module switch on or off depending on the switching status of the cams.

You can realize up to four cam tracks with one output module. A cam control with more than four cam tracks can be implemented with several output modules. All output modules of this cam controller can be supplied with the same encoder module. Each output module has its own control/feedback interface and can work independently of the other output modules in the cam controller.

> **Note**
>
> **Incremental jumps**
>
> Incremental jumps may occur if, due to the system, an encoder value is not transmitted to the output module for every increment of the sensor. This impairs the switching accuracy of the output.
>
> If incremental jumps occur in your system and the cams switch depending on the direction, ensure that the maximum incremental jump is significantly less than 1/2 x (maximum encoder value – minimum encoder value).

> **Note**
>
> **Direction detection**
>
> Some of the usable encoder modules do not provide explicit direction information. If no direction information is not supplied with the encoder data, two valid, different encoder values are required for direction detection. The two values allow a subtraction to be performed and the direction to be derived from the result.
>
> Make sure that the maximum incremental jump is significantly smaller than 1/2 x (maximum encoder value – minimum encoder value).

## Start and end position (S7-1500)

### Start and end position of a cam

The switch-on range of cams is basically defined by a start position and end position.

![Start and end position of a cam](images/133705028875_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> If several cams are assigned to the same digital output, their switch-on ranges must not overlap.

### Effective direction

A cam can be switched as a function of the motion direction.

The following effective directions are possible for the cams:

**None:**

The cam is switched off.

**Positive:**

The following figure shows an example of the switching behavior with "Positive" effective direction:

![Effective direction](images/133705450123_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | The cam switches on when the start position in positive direction of movement is reached. |
| ② | The cam switches off when the end position is exceeded in positive direction of motion. |
| ③ | If the direction is reversed in the switch-on range from positive to negative effective direction, the cam is switched off. |
| ④ | If the direction is reversed in the switch-on range from a negative to a positive effective direction, the cam is switched on. |

**Negative:**

The following figure shows an example of the switching behavior with "Negative" effective direction:

![Effective direction](images/133705500939_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | The cam switches on when the end position in the negative direction of movement is reached. |
| ② | The cam switches off when the value falls below the start position in the negative direction of motion. |
| ③ | If the direction is reversed in the switch-on range from negative to positive effective direction, the cam switches off. |
| ④ | If the direction is reversed in the switch-on range from positive to negative effective direction, the cam switches on. |

**Both:**

The following figure shows an example of the switching behavior with "Both" effective direction:

![Effective direction](images/133705590155_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | The cam switches on when the encoder value is in the switch-on range. |

### Channel assignment

You assign each cam to the digital output on which the cam is to be output.

If several cams are assigned to the same digital output, their switch-on ranges must not overlap.

## Hysteresis (S7-1500)

### Hysteresis

Slight movements of the encoder can result in the position value fluctuating around a certain position. If a start or end position is within the fluctuation range, the corresponding cam and the digital output are switched on and off correspondingly often without using a hysteresis, depending on the effective direction of the cam. The hysteresis prevents these unwanted switching operations.

The hysteresis is a position tolerance within which the position values may vary without changing the switching state of the cam.

**Behavior when hysteresis is activated:**

- The configured hysteresis width is in effect for all cams.
- The hysteresis range extends in the positive and negative directions around the detected direction reversal point. The hysteresis range thus extends over double the configured hysteresis. The hysteresis limit points represent the hysteresis range spanned by the firmware.
- Changes in direction recognized within the hysteresis are ignored and the switching status of cams is not changed.
- After the hysteresis range is exited, the output is set according to the cam settings.

![Hysteresis](images/133705373707_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Actual position |
| ② | Effective position |
| ③ | Effective hysteresis |

The following example shows the effects of the hysteresis on the switching behavior of the cam with positive effective direction. The hysteresis keeps the output stable when the encoder value signals a small direction reversal.

![Hysteresis](images/133705284491_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Hysteresis range |
| ② | Encoder value |

## Pulsed cam output (S7-1500)

It is possible to pulse the cams in order to save energy for the respective actuator. This function works while a cam has status 1. You configure the pulsed cam output with the "Pulsed cam output duty cycle" and "Pulsed cam output period" parameters.

The duty cycle is used to specify the pulse-period ratio of the pulsed output signal within the configured cycle duration.

> **Note**
>
> The edges of the pulsed output cam are not synchronized with the cam start or end.

The following figure shows an example of the pulsed cam output:

![Figure](images/133705679371_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | T<sub>ON</sub> |
| ② | Period duration |
|  | Duty cycle = T<sub>ON</sub> / Period * 100% |

---
title: "Using the IM 174 (S7-300, S7-400)"
package: TFHWCIM174enUS
topics: 12
devices: [S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Using the IM 174 (S7-300, S7-400)

This section contains information on the following topics:

- [Overview (S7-300, S7-400)](#overview-s7-300-s7-400)
- [Configuring and programming IM174 (S7-300, S7-400)](#configuring-and-programming-im174-s7-300-s7-400)

## Overview (S7-300, S7-400)

### Interface module for analog drives and stepper motors

An IM 174 module (interface module) is an interface module suitable for running up to 4 drives with an analog setpoint interface and with one TTL or SSI encoder per axis on the isochronous PROFIBUS.

Communication between the controller and the IM 174 is performed exclusively using PROFIBUS, via an IM 174-specific message frame type which, in addition to digital input/output data, also contains a message frame type (standard message frame 3 and 81) for each drive specified according to a PROFIDrive profile. As part of cyclic DP communication, the actual drive values (encoder values) are transferred from the IM 174 module to the controller via the isochronous PROFIBUS, and the speed setpoints calculated by the controller are transferred to the IM 174 module.

The transferred speed setpoints are then output from the IM 174 module to the drives as analog values or pulses.

### Field of application

IM 174 can be used for the following control jobs:

- controlling analog drives
- controlling stepper motors
- reading in encoder data

## Configuring and programming IM174 (S7-300, S7-400)

This section contains information on the following topics:

- [Configuring IM174 (S7-300, S7-400)](#configuring-im174-s7-300-s7-400)
- [Encoders and Drives (S7-300, S7-400)](#encoders-and-drives-s7-300-s7-400)
- [Drive parameters (S7-300, S7-400)](#drive-parameters-s7-300-s7-400)
- [Encoder parameters (S7-300, S7-400)](#encoder-parameters-s7-300-s7-400)
- [Parameters (S7-300, S7-400)](#parameters-s7-300-s7-400)
- [Selecting the message frame type (S7-300, S7-400)](#selecting-the-message-frame-type-s7-300-s7-400)
- [Message frame structure (S7-300, S7-400)](#message-frame-structure-s7-300-s7-400)
- [Zero mark monitoring (S7-300, S7-400)](#zero-mark-monitoring-s7-300-s7-400)
- [Programming the IM 174 (S7-300, S7-400)](#programming-the-im-174-s7-300-s7-400)

### Configuring IM174 (S7-300, S7-400)

#### Steps required - Overview

You configure the IM 174 in the Inspector window under "Properties". You must carry out the following steps:

1. Add a PROFIBUS module to the hardware configuration
2. Assign parameters for isochronous PROFIBUS
3. Specify drive and encoder parameters for the axes

#### Assign parameters for isochronous PROFIBUS

1. Select the PROFIBUS subnetwork in the "PROFIBUS address" section and assign a PROFIBUS address.
2. Select the check box "Synchronize DP slave to equidistant DP cycle" in the "Isochronous mode" section and set time Ti/To.
3. Select the [frame type](#selecting-the-message-frame-type-s7-300-s7-400) in the "Encoder and drives" section.
4. Specify the address ranges for the input and output parameters of the axes and assign a process display in the "Addresses" section.

**Note**

**PROFIBUS address at the DIP switch**

The PROFIBUS address is set via DISourcing outputs on the PROFIBUS module IM 174. A power on/off / is necessary on the IM 174 to activate a PROFIBUS address set on the DIP switch. The assigned PROFIBUS address must be identical to the PROFIBUS address set at the DIP switch.

#### Specify drive and encoder parameters for the axes

1. Select the [drive type](#encoders-and-drives-s7-300-s7-400) for each axis and set the [drive parameters](#drive-parameters-s7-300-s7-400) in the "Encoder and drives" section.
2. Select the [encoder type](#encoders-and-drives-s7-300-s7-400) for each axis and if necessary set the required [encoder parameters](#encoder-parameters-s7-300-s7-400) in the "Encoder and drives" section.
3. You can set the [parameters](#parameters-s7-300-s7-400) for switch-off behavior in the "Parameters" section.

### Encoders and Drives (S7-300, S7-400)

You can use the "Encoders and Drives" property in the area navigation to configure the drives and encoders that are connected to the IM 174.

#### Drive types

You can select the following drive types:

- Servo (analog drive)
- Stepper (stepper drive)

#### Encoder types for analog drives

The following encoder types can be selected for analog drives

- Encoder type not available
- Encoder type TTL
- Encoder type SSI

#### Encoder types for stepper drives

The following encoder types can be selected for stepper drives

- Encoder type not available
- Encoder type TTL
- Encoder type SSI
- Encoder type stepper

### Drive parameters (S7-300, S7-400)

#### Drive types

You can select the following drive types:

- Servo (analog drive)
- Stepper (stepper drive)

#### Servo drive type

If you have selected the servo drive type, you can switch the voltage range of the analog output voltage via the "Unipolar" check box.

#### Unipolar not selected

If the "Unipolar" option is **not** selected, an analog voltage in the range of **-10 V** to **+10 V** will be output as the setpoint. The drive can then be traversed in two directions.

#### Unipolar selected

If the "Unipolar" option **selected**, an analog voltage in the range of **0V** to **+10 V** will be output as the setpoint. The direction of rotation is then output from the IM 174, depending on the current speed setpoint via a digital output of the IM 174:

- Direction of rotation signal for Axis 1 -> Digital output X11, Pin 13
- Direction of rotation signal for Axis 2 -> Digital output X11, Pin 15
- Direction of rotation signal for Axis 3 -> Digital output X11, Pin 17
- Direction of rotation signal for Axis 4 -> Digital output X11, Pin 19

#### Alt.DrvRdy

Depending on the drive you use, the Drive Ready signal returns different status messages:

- The drive signals "Ready for switching on" with Signal Drive Ready. An enable from the controller is still required to switch the drive on.
- The drive signals "Ready" with the Signal Drive Ready signal. The drive is ready for control in this state and directly follows a setpoint.

You should **not**activate the "Alt.DrvRdy" function, if your drive reports a "ready to switch on" state upon a Drive-Ready signal (mostly in analogue drives).

Activate the "Alt.DrvRdy" function when the drive signals "Ready" with a Drive Ready signal (mostly with servo drives).

Information on which status message the drive you use returns can be found in the product information for your drive.

#### Stepper drive type

You must enter drive-specific or process-specific frequency values [Hz] in the fields "Max. frequency [Hz]" and "Stand. frequency [Hz]" for the "Stepper" drive type. The necessary power electronics (e.g. FM Stepdrive) and the stepper motor are required for the operation of a stepper motor on the IM 174.

The basic structure of an IM 174 with stepper drives and without encoders is shown in the following figure:

![Basic structure of an IM 174 with FM STEPDRIVE and SIMOSTEP motor](images/23986569995_DV_resource.Stream@PNG-en-US.png)

Basic structure of an IM 174 with FM STEPDRIVE and SIMOSTEP motor

#### Alt.DrvRdy

Depending on the drive you use, the Drive Ready signal returns different status messages:

- The drive signals "Ready" with the Drive Ready signal. An enable from the controller is still required to switch the drive on.
- The drive signals "Ready" with the Signal Drive Ready signal. The drive is ready for control in this state and directly follows a setpoint.

You should **not**activate the "Alt.DrvRdy" function, if your drive reports a "ready to switch on" state upon a Drive Ready signal (mostly in analogue drives).

Activate the "Alt.DrvRdy" function when the drive signals "Ready" with a Drive Ready signal (mostly with servo drives).

Information on which status message the drive you use returns can be found in the product information for your drive.

#### Max. frequency [Hz] and stand. frequency [Hz]

You must enter drive-specific or process-specific frequency values [Hz] in the fields "Max. frequency [Hz]" (maximum frequency) and "Stand. frequency [Hz]" (rated frequency) for the "Stepper" drive type.

#### Calculation of the stand. frequency

The stand. frequency is calculated according to the following formula:

**Stand. frequency [Hz] = n [rpm] / 60 * resolution on the stepper motor**

| Symbol | Meaning |
| --- | --- |
| n [rpm]: | Speed of the stepper motor  (characteristic values lie between 500 and 1000 rpm) |
| Resolution on the stepper motor: | Number of increments on the stepper motor (characteristic values: 500, 1000, 5000) |

#### Calculation of the max. frequency

The max. frequency is calculated according to the following formula:

**Maximum frequency [Hz] = n** 
<sub>max</sub>
 **[rpm] / 60 * resolution on stepping motor**

| Symbol | Meaning |
| --- | --- |
| n<sub>max</sub> [rpm]: | Maximum speed of the stepper motor  (characteristic values lie between 500 and 1000 rpm) |
| Resolution on the stepper motor: | Number of increments on the stepper motor (characteristic values: 500, 1000, 5000) |

The maximum speed n<sub>max </sub>is determined by the operating characteristics of

stepper motors. Hence, a maximum motor speed nmax,

corresponding to a maximum axis speed,

is determined from the technology required torque M_t.

![Characteristic operational features of a stepper motor](images/23974304267_DV_resource.Stream@PNG-de-DE.png)

Characteristic operational features of a stepper motor

> **Note**
>
> **Overload range**
>
> To avoid operating in the overload range, use the drive only at normal frequency!

#### Description of the behavior of a stepper motor

The positioning accuracy, the speed n as well as the torque M produced by the motor are very important for the process-specific requirements. For the optimum determination of these values, the behavior of the stepper motor must be considered. From a given speed of rotation of the stepper motor (around 500 rpm), the torque produced by the motor drops logarithmically, and approaches 0 at a maximum speed (around 3,000 rpm). The specific data can be found in the data sheet for the motor used.

#### Consequences of operation in the overload range

If the stepper motor is ever unable to produce the requested torque, it loses synchronization with the predefined frequency and its speed drops suddenly. This can lead to standstill. Motion can only be resumed in this state once a setpoint of 0 has been entered. For a position axis without additional encoders, the traversing position and thus synchronization of the axis are lost.

> **Note**
>
> **Stepper drive with "Stepper" encoder type (PULSE REFEED operation)**
>
> During operation with a "Stepper" encoder type (PULSE REFEED operation), the stepper motor may vibrate at standstill.
>
> This occurs with the default parameterization of a project when the stepper is traversed in a preceding traversing motion to a position value which is exactly between two natural step divisions of the stepper.

#### Stepper drive with TTL/SSI encoders

When using TTL/SSI encoders, the ratio of the encoder resolution (incl. fine resolution) to the step resolution of the stepper must be taken into account.

To prevent vibration between two position values at standstill, the stepper increment distance must be less than the distance representation in the encoder feedback (i.e. the increment of the stepper must be greater than the encoder resolution). If necessary, encoders with a lower resolution must be used or a higher step resolution set on the stepper.

### Encoder parameters (S7-300, S7-400)

#### Encoder types for analog drives

The following encoder types can be selected for analog drives:

- Encoder type not available
- Encoder type TTL
- Encoder type SSI

#### Encoder types for stepper drives

The following encoder types can be selected for stepper drives:

- Encoder type not available
- Encoder type TTL
- Encoder type SSI
- Encoder type stepper

#### Encoder type "not available"

The following applies to **"Servo" drive types**: Axis x is not available or should not be operated. Useful data transmitted for this axis in the PROFIBUS message frame are empty.

The following applies to**"Stepper" drive types**: The stepper is operated without an encoder.

If the stepper is configured for operation with encoder, it may only be used as a speed-controlled axis.

If no encoder (SSI/TTL) is used, the encoder type "Stepper" can be selected to enable positioning even if no encoder is connected.

#### Encoder type TTL

In the case of encoder type "TTL" you can set the following encoder parameters:

- **Resolution**: Encoder resolution in encoder pulses per encoder revolution
- **Speed calculation enabled**: The IM 174 calculates the speed if the check box is enabled.
- **Normalization speed**: This input box is only visible if the "Speed calculation enabled" option is enabled. Enter the rated speed of the motor in revolutions per minute. The speed with the least noise is obtained when the speed is calculated by the IM174.
- **Reserved bits for fine resolution**: Setting 0 - 15

  The "Reserved bits for fine resolution" parameter specifies the desired pulse multiplication of the encoder increments transmitted in actual encoder values G1_XIST1 and G1_XIST2.

  The setting corresponds to a pulse multiplication between 2<sup>0</sup> = 1to 2<sup>15</sup> = 32,768.

  > **Note**
  >
  > **Minimum fine resolution for TTL encoders**
  >
  > TTL encoders always require considering and setting a minimum fine resolution of 2<sup>2 </sup>(= 4).

![Encoder type TTL](images/23986595083_DV_resource.Stream@PNG-en-US.png)

#### Encoder type SSI

You can set the following parameters for encoder type "SSI":

- **Parity**: Select this option if the encoder data are to be transmitted from the encoder to the IM 174 with a parity bit.
- **MsgLength**: Setting 0 - 25

  Number of useful data bits transmitted by the encoder
- **Encoding**: The following encoder codes are supported:

  - Binary
  - Gray
- **Transmission rate**: The transmission rate setting must be identical for all SSI encoders. If transmission rate settings are different, the transmission rate of the SSI encoder with the highest encoder number is assigned.

  The following transmission rates are supported:

  - 187.5 Kbps
  - 375 Kbps
  - 750 Kbps
  - 1.5 Mbps
  - 3.0 Mbps

    > **Note**
    >
    > Configure a maximum of 187.5 Kbps. It is not practical to set a quicker transmission rate for this module.
- **Reserved bits for fine resolution**: Setting 0 - 15

  The "Reserved bits for fine resolution" parameter specifies the desired pulse multiplication of the encoder increments transmitted in actual encoder values G1_XIST1 and G1_XIST2.   
  The setting corresponds to a pulse multiplication between 2<sup>0</sup> = 1 to 2<sup>15</sup> = 32,768.

#### Encoder type stepper

**Stepper drive in PULSE REFEED mode**

An Axis x with the "Stepper" drive type can be operated with a "Stepper" encoder type. In this mode, the setpoints are signaled back as process values from the IM 174 to the controller.

You can set the following encoder parameters for encoder type "Stepper":

- **Motor monitoring**: If the "Motor monitoring" check box is activated, the number of steps of a stepper motor must be constantly monitored for a preset reference point distance (see "BERO distance"). In the case of encoderless operation, the stepper drive used simultaneously signals the process values (pulse refeed).
- **Bero distance**: In the case of "BERO distance" the number of steps (for the stepper drive used) between two BERO signals is entered. The distance between the two BERO signals is the reference point distance.
- **Bero tolerance**: Setting 0 - 65535

  In the case of "BERO tolerance" the permissible deviation of the steps is entered. The resulting step range lies within the following tolerance:   
  **resulting step range = Bero distance ± 1 / 2 * Bero tolerance**
- **Reserved bits for fine resolution**: Setting 0 - 15

  The "Reserved bits for fine resolution" parameter specifies the desired pulse multiplication of the encoder increments transmitted in actual encoder values G1_XIST1 and G1_XIST2.

  The setting corresponds to a pulse multiplication between 2<sup>0</sup> = 1to 2<sup>15</sup> = 32,768.

### Parameters (S7-300, S7-400)

Important parameters for the IM 174 are specified under the "Parameters" property in the area navigation.

#### shutdown ramp [ms]

The value range is 0 - 65535 ms.

The "Shutdown ramp" parameter specifies a function that is linear with respect to time. If an error is detected, all drives that are connected to the IM 174 are decelerated down to setpoint 0 in accordance with this function.

The shutdown ramp takes effect for the following errors:

- Temperature alarm of the module (approx. 90 °C ON, approx. 85 °C OFF)
- Lifebeat error
- Synchronization error between master and slave

  > **Note**
  >
  > **Parameter value 0**
  >
  > A parameter value of 0 causes the drive to coast to a standstill when an error occurs.

![Parameters: Shutdown ramp](images/23889098763_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| 1) | Maximum setpoint |
| 2) | Current setpoint |
| 3) | Parameter value: Shutdown ramp |

Parameters: Shutdown ramp

#### Shutdown delay

The value range is 0 - 65535 s.

The "Shutdown delay" parameter can be used to specify a time after which, after a **temperature alarm** has occurred, the shutdown ramp is activated.

The shutdown delay is started when a temperature of 90 °C is exceeded in the module. If the temperature drops to approx. 85 °C while the delay is active, the shutdown ramp is not activated and the shutdown delay time is reset.

#### Tolerable lifebeat errors

The value range is 0 - 15.

The "Tolerable lifebeat error" parameter specifies the number of lifebeat errors tolerated for the DP master. The shutdown ramp is activated when the parameterized number is exceeded. The value range is

#### 611U-compliant mode

In 611U-compliant mode, the signal source for homing of axes is no longer specified using the PROFIDrive standard message frame (STD3, encoder control word G1_STW), but rather using the additional digital output word in the PROFIBUS message frame of the IM 174 (see table "Message frame structure" in the "Message frame type" section).

611U-compliant mode:

- Not selected

  The signal source for homing is specified via the encoder control word Gx_STW in the PROFIDrive standard message frame.
- Selected

  The signal source for homing is specified via the additional digital output word in the PROFIBUS message frame.

### Selecting the message frame type (S7-300, S7-400)

#### Message frame type

The IM 174 DP slave is operated with two specific message frame types: Four axes, each with one encoder (standard message frame 3 and 81) and I/O data

> **Note**
>
> **Standard message frame 81**
>
> Standard message frame 81 can only be used for encoders.

---

**See also**

[Message frame structure (S7-300, S7-400)](#message-frame-structure-s7-300-s7-400)

### Message frame structure (S7-300, S7-400)

#### Message frame structure

The overview below explains the frame structure.

| Message frame type | Description |
| --- | --- |
| 4 axes, each with one encoder, standard message frame 3 + IO, PZD-5/9 O/I 1/1 or message frame 81 + IO, PZD-2/6 + I/O 1/1 | 4 x Standard message frame 3 or 81 and 1 PZD word each for digital I/O data |
| PZD x/y Number of process data words, x: Setpoint, y: Actual value,  for example, PZD-5 / 9:  5 process data words to desired values  9 process data words for actual values |  |
| ![Message frame structure](images/23895829771_DV_resource.Stream@PNG-en-US.png) |  |
| ![Message frame structure](images/23895872523_DV_resource.Stream@PNG-en-US.png) |  |
| ![Message frame structure](images/23895932427_DV_resource.Stream@PNG-en-US.png) |  |
| ![Message frame structure](images/23895974923_DV_resource.Stream@PNG-en-US.png) |  |
| ![Message frame structure](images/23895902475_DV_resource.Stream@PNG-en-US.png) |  |

> **Note**
>
> The message frame type setting for the IM 174 DP slave must agree with the message frame type setting in the controller. There is no automatic adjustment.

#### Encoder control word Gx_STW

The overview below explains the encoder control word (extract). The overview is based on the following requirements:

- Find reference mark
- On-the-fly measurement
- Encoder error

  ![Encoder control word Gx_STW](images/23896004619_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> **Measurement on rising or falling edge**
>
> IM 174 only supports measurement on a rising or falling edge.

#### Additional encoder actual value Gx_XIST2

The overview below sets out the error codes in Gx_XIST2 where G1_ZSW, Bit 15 == 1:

Error codes in Gx_XIST2

| G1_XIST2 | Meaning | Possible causes / description |
| --- | --- | --- |
| 1<sub>Hex</sub> | Encoder sum error | The encoder signal levels are too low, faulty (inadequate shielding) or open-circuit monitoring has been tripped. |
| 2<sub>Hex</sub> | Zero mark monitoring | A fluctuation in the measured rotor position has arisen between 2 encoder zero marks (encoder pulses may be lost). |

#### Status word ZSW_1 - Bit 11 to Bit 14

The following overview describes the status word ZSW_1 with regard to the module-specific messages Bit 11 to Bit 14:

Status word ZSW_1

| Bit | Name | Description |
| --- | --- | --- |
| 11 | Temperature error | A specific temperature in the housing of module IM 174 has been exceeded. |
| 12 | PLL synchronization error | The IM 174 cannot be synchronized with the global check-back signal. |
| 13 | Master life sign error | The IM 174 cannot be synchronized with the master life sign signal. |
| 14 | Drive error | A drive error exists, for example the Drive Ready signal is missing. |

### Zero mark monitoring (S7-300, S7-400)

#### Method of functioning of the zero reference mark monitoring

Zero mark monitoring compares the recognized encoder increments between two zero marks with the configured encoder resolution. If a difference is found, an encoder error is reported.

Track A and Track B as well as Track Z of the encoder have to be on the high level simultaneously so that zero mark monitoring is carried out correctly.

**Restrictions**:

- The failure of a zero mark in itself does not inevitably result in an error, since checking is not started until a zero mark is reached.
- The result of the counted encoder increments MOD 16 has to be nonzero so that an error is reported.
- The result of the counted encoder increments MOD 10 has to be nonzero so that an error is reported.

**Example**:

Encoder configuration: TTL 2048 pulses

Counted encoder increments 2049 -> encoder error

Counted encoder increments 1024 -> no encoder error

### Programming the IM 174 (S7-300, S7-400)

We recommend the "Easy Motion Control" add-on package for programming the IM 174.

#### Instructions for IM 174

The following instructions are available for IM 174 in the Easy Motion Control instruction list:

- EncoderIM174 - Use of IM 174 as position feedback module for incremental and absolute encoders
- OutputIM174 - Use of a channel of module IM 174 as output module

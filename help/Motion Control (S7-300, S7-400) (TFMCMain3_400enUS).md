---
title: "Motion Control (S7-300, S7-400)"
package: TFMCMain3_400enUS
topics: 14
devices: [S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Motion Control (S7-300, S7-400)

This section contains information on the following topics:

- [Position feedback basics (S7-300, S7-400)](#position-feedback-basics-s7-300-s7-400)
- [Using SM 338 (S7-300, S7-400)](Using%20SM%20338%20%28S7-300%2C%20S7-400%29.md#using-sm-338-s7-300-s7-400)
- [Using ET 200S 1SSI (S7-300, S7-400)](Using%20ET%20200S%201SSI%20%28S7-300%2C%20S7-400%29.md#using-et-200s-1ssi-s7-300-s7-400)
- [Basics of positioning with function modules (S7-300, S7-400)](#basics-of-positioning-with-function-modules-s7-300-s7-400)
- [Using FM 351 (S7-300, S7-400)](Using%20FM%20351%20%28S7-300%2C%20S7-400%29.md#using-fm-351-s7-300-s7-400)
- [Using FM 451 (S7-300, S7-400)](Using%20FM%20451%20%28S7-300%2C%20S7-400%29.md#using-fm-451-s7-300-s7-400)
- [Using ET 200S 1PosU (S7-300, S7-400)](Using%20ET%20200S%201PosU%20%28S7-300%2C%20S7-400%29.md#using-et-200s-1posu-s7-300-s7-400)
- [Using ET 200S 1STEP 5V (S7-300, S7-400)](Using%20ET%20200S%201STEP%205V%20%28S7-300%2C%20S7-400%29.md#using-et-200s-1step-5v-s7-300-s7-400)
- [Using the IM 174 (S7-300, S7-400)](Using%20the%20IM%20174%20%28S7-300%2C%20S7-400%29.md#using-the-im-174-s7-300-s7-400)
- [Using Easy Motion Control (S7-300, S7-400)](Using%20Easy%20Motion%20Control%20%28S7-300%2C%20S7-400%29.md#using-easy-motion-control-s7-300-s7-400)

## Position feedback basics (S7-300, S7-400)

This section contains information on the following topics:

- [What is position feedback? (S7-300, S7-400)](#what-is-position-feedback-s7-300-s7-400)
- [Encoder value acquisition (S7-300, S7-400)](#encoder-value-acquisition-s7-300-s7-400)
- [Gray/dual converter (S7-300, S7-400)](#graydual-converter-s7-300-s7-400)
- [Encoder value and scaling (S7-300, S7-400)](#encoder-value-and-scaling-s7-300-s7-400)

### What is position feedback? (S7-300, S7-400)

#### Position feedback

Position feedback is the detection of actual values scaled to units of length.

It differs depending on the encoder used:

- Incremental encoder

  The module counts the incremental encoder signals. A reference point approach is required before position feedback to create a reference point for the encoder position. The counter can, for example, be set to "0" at a reference mark.

  Following the reference point approach (with synchronized axis), the counter value is a measurement of the current position.
- Absolute encoder

  No reference point approach is required. The signal output represents a fixed position.

The values determined can be processed directly in the user program. A direct response to encoder values from motion systems is therefore possible.

### Encoder value acquisition (S7-300, S7-400)

#### Description

The absolute encoder transfers its encoder values to the module in frames. The transmission of frames is initiated by the module.

- In non-isochrone mode, the encoder values are acquired freewheeling.
- In isochrone mode, the encoder values are acquired in synchronism with the bus cycle at each T<sub>i</sub>.

#### Freewheeling encoder value acquisition

The module initiates the transmission of a frame each time the parameterized monoflop time elapses.

The module processes the acquired encoder value asynchronously to these freewheeling frames in the cycle of the update rate.

Freewheeling acquisition therefore returns encoder values of different ages. The difference between the maximum and minimum age is the jitter.

#### Isochrone encoder value acquisition

Isochrone encoder value acquisition is automatically set if the bus system and I/O modules are synchronized.

The module initiates a frame transfer in each bus cycle at T<sub>i</sub>.

The module processes the transmitted encoder value isochronously to the bus cycle.

### Gray/dual converter (S7-300, S7-400)

#### Gray code/dual code converter

The "Gray code/dual code converter allows you to define how the codes returned by the encoder are processed:

- When "Gray code" is set, the encoder value returned by the absolute encoder in gray code will be converted to dual code.
- When "Dual code" is set, the values returned by the encoder will remain unchanged.

> **Note**
>
> If you have selected the "Gray code" setting, the module will always convert the total encoder value (13 to 25 bits). Any leading special bits will therefore influence the encoder value and the appended bits may be corrupted.

### Encoder value and scaling (S7-300, S7-400)

#### Encoder value and scaling

The encoder value transferred contains the encoder position of the absolute encoder. In addition to the encoder position, the encoder transfers additional bits located before and after the encoder position, depending on the encoder used.

The module requires the following information if it is to determine the encoder position:

- Encoder type
- Number of adjusted bits
- Increments per encoder revolution

Scaling specifies the position of the encoder value at the feedback interface.

- You specify that trailing, irrelevant bits in the encoder value are to be discounted by entering either "Number of adjusted bits = 1, 2 ... 12" (for SM 338) or "Scaling on" (for ET 200S 1SSI). The encoder value is then positioned in the address area, right-aligned (see example below).
- Entering "Number of adjusted bits = 0" (for SM 338) or "Scaling of" (for ET 200S 1SSI) will mean adjusted bits are retained and available for evaluation.

  This can be useful is you are using an absolute encoder which transfers information in the adjusted bits (see manufacturer's specifications) and you wish to evaluate this information. Please also read the [Gray code/dual code converter](#graydual-converter-s7-300-s7-400) information.

#### Example of encoder value scaling

Requirements:

You are using a single-turn encoder with 2<sup>9</sup> steps (corresponds to 9 bits) = 512 increments/encoder revolution (resolution/360°) with the following parameter assignment:

- Encoder type: SSI-13 bit
- Number of adjusted bits: 4 places
- Increments per encoder revolution: 512

The following image shows the location of the relevant bits before and after scaling.

![Example of encoder value scaling](images/22186518539_DV_resource.Stream@PNG-en-US.png)

## Basics of positioning with function modules (S7-300, S7-400)

This section contains information on the following topics:

- [What is positioning? (S7-300, S7-400)](#what-is-positioning-s7-300-s7-400)
- [Controlled positioning with rapid traverse/creep speed (S7-300, S7-400)](#controlled-positioning-with-rapid-traversecreep-speed-s7-300-s7-400)
- [Ranges and switching points of the positioning module (S7-300, S7-400)](#ranges-and-switching-points-of-the-positioning-module-s7-300-s7-400)
- [Encoder signals (S7-300, S7-400)](#encoder-signals-s7-300-s7-400)

### What is positioning? (S7-300, S7-400)

#### Positioning

Positioning is taking up a specific spatial position, in particular a position defined by coordinates.

In SIMATIC technology, positioning means adjusting and positioning mechanical axes. A range of difference procedures are used:

- Controlled positioning with rapid traverse/creep speed
- Controlled positioning
- Positioning with stepper motor

Positioning can control linear axes with a limited traversing range and continuous rotary axes.

### Controlled positioning with rapid traverse/creep speed (S7-300, S7-400)

#### Controlled positioning

Each positioning process is characterized by:

- A starting position
- The target of the positioning
- Parameters that determine the sequence of the positioning

The target is initially approached at a higher velocity (rapid traverse). At a specified distance from the target, the velocity switches to creep speed. The drive is switched off shortly before the axis reaches the target - also at a specified distance from the target. In doing so, the module monitors the target approach.

The drive is controlled via digital outputs with rapid traverse or creep speed and in the appropriate direction.

### Ranges and switching points of the positioning module (S7-300, S7-400)

#### Target

The target is the absolute or relative position on the axis that is approached during a positioning process.

#### Definition of the switching points and switching ranges

The following ranges and positions can be parameterized for controlled positioning:

| Range / Position | Description |
| --- | --- |
| Operating range | defines the range you set for your job by means of the software limit switches or the end of the rotary axis. |
| Switch-over difference | defines the distance from the target at which the drive changes from rapid traverse to creep traverse. |
| Switch-over point | Defines the position at which the drive changes from rapid traverse to creep speed. |
| Switch-off difference | defines the distance from the target at which the drive is switched off. |
| Switch-off point | Defines the position at which the drive is switched off. The positioning module then adopts the monitoring functions from this point on. |
| Target range | defines the positioning precision for your application and surrounds the target symmetrically. |
| Standstill range | Defines a symmetrical range around the target to be monitored by the positioning module. |

#### Switching points and switching differences

The following figure shows how the switching points and switching differences can be arranged for positioning. In the interests of simplicity, it is assumed that the actual speed changes linearly over the distance traversed. The emerging ramps can be explained by mechanical inertia or by the parameterization possibilities of the power section.

![Switching points and switching differences](images/19686364939_DV_resource.Stream@PNG-en-US.png)

#### Switching ranges

The figure below shows how the switching ranges can be arranged around the target.

![Switching ranges](images/19687345803_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Operating range |
| ② | Changeover difference in direction plus |
| ③ | Changeover difference in direction minus |
| ④ | Switch-off difference in plus traverse direction |
| ⑤ | Switch-off difference in minus traverse direction |
| ⑥ | Standstill range |
| ⑦ | Target range |

### Encoder signals (S7-300, S7-400)

This section contains information on the following topics:

- [Supported encoders (S7-300, S7-400)](#supported-encoders-s7-300-s7-400)
- [Incremental encoder (S7-300, S7-400)](#incremental-encoder-s7-300-s7-400)
- [Absolute encoder (S7-300, S7-400)](#absolute-encoder-s7-300-s7-400)

#### Supported encoders (S7-300, S7-400)

##### Incremental encoders supported

[Incremental encoders](#incremental-encoder-s7-300-s7-400) with two pulses 90° out of phase with or without zero marks are supported:

- Encoders with asymmetrical output signals with 24 V level

  - Limit frequency = 50 kHz
  - Cable up to 100 m long, shielded
- Encoders with symmetrical output signals with 5 V differential interface in accordance with RS 422

  - Limit frequency = 400 kHz
  - With 5 V voltage supply: Cable up to 32 m long, shielded
  - With 24 V voltage supply: Cable up to 100 m long, shielded

> **Note**
>
> If the 5 V encoder does not output a zero mark signal and wire-break monitoring is enabled, you must interconnect the zero mark signal inputs N and /N externally so that the inputs have different signal levels (for example, N to 5 V, /N to ground).

##### Absolute encoders supported

[Absolute encoders](#absolute-encoder-s7-300-s7-400) with serial interface are supported. Position data are transferred synchronously using the SSI protocol (**S**ynchronous**S**erial**I**nterface). FM x51 only supports GRAY code. The data formats 25-bit (fir tree) and 13-bit (half fir tree) result from the arrangement of the data bits in the frames.

Absolute encoders are divided into the categories:

- Single-turn encoder

  The total range of single-turn encoders is scaled to one revolution.
- Multiturn encoder

  The total range of multiturn encoders is scaled to several revolutions.

| Encoder type | Frame length |
| --- | --- |
| Single-turn encoder | 13 bits |
| Single-turn encoder | 25 bits |
| Multiturn encoder | 13 bits … 25 bits |

The transmission rate for data transmission depends on the cable length:

- Max. 188 kHz for 200 m of cable, shielded
- Max. 375 kHz for 100 m of cable, shielded
- Max. 750 kHz for 40 m of cable, shielded
- Max. 1.5 MHz for 12 m of cable, shielded

#### Incremental encoder (S7-300, S7-400)

##### Signal forms

The table below illustrates the signal forms of encoders with asymmetrical and symmetrical output signals.

| asymmetrical | symmetrical |
| --- | --- |
| ![Signal forms](images/20187364107_DV_resource.Stream@PNG-de-DE.png) | ![Signal forms](images/20187414155_DV_resource.Stream@PNG-de-DE.png) |

##### Signal evaluation

**Increments**

An increment identifies a signal period of the two encoder signals A and B. This value is specified on the rating plate of the encoder and/or in the encoder specifications.

The figure below shows the ratio of increments to pulses.

![Signal evaluation](images/20187425803_DV_resource.Stream@PNG-en-US.png)

**Pulses**

The positioning module evaluates all 4 edges of signals A and B in each increment (quadruple evaluation).

Pulses

1 increment (encoder specification) = 4 pulses (evaluation in the module)

##### Response times

The positioning module has the following response times for connected incremental encoders:

Response times

Response time = switching cycle of the connected switching elements

> **Note**
>
> You can compensate for the minimum response time by assigning the changeover difference and switch-off difference accordingly.

##### Indecision

The indecision influences the precision of the positioning. In the case of incremental encoders the indecision is negligible.

#### Absolute encoder (S7-300, S7-400)

##### Pulse evaluation of absolute encoders

Pulse evaluation of absolute encoders

1 increment (encoder specification) = 1 pulse (FM evaluation)

##### Response times

The FM x51 has the following response times for absolute encoders:

Response times

Minimum response time = message frame time + switching cycle of the connected switching elements

Maximum reaction time = 2 x frame runtime + monoflop time + switching time of the connected switching elements

With programmable absolute encoders:

Maximum reaction time = message frame time + monoflop time + switching cycle of the connected switching elements +1/max. step sequence frequency

##### Monoflop time

The monoflop time is 64 µs.

Encoders with values greater than the limits specified here are not permitted.

##### Message frame times

The message frame times depend on the transmission rate:

| Transmission rate | Message frame time with 13 bit | Message frame time with 25 bit |
| --- | --- | --- |
| 0.188 MHz | 75 µs | 139 µs |
| 0.375 MHz | 38 µs | 70 µs |
| 0.750 MHz | 19 µs | 35 µs |
| 1.500 MHz | 10 µs | 18 µs |

##### Example of response times

This example shows you how to calculate the minimum and maximum reaction time. The example does not use a programmable encoder.

- Hardware switching cycle: approx. 150 µs
- Message frame time: 18 µs at 1.5 MHz transmission rate (25 Bit message frames)
- Monoflop time: 64 µs

Minimum response time = 18 µs + 150 µs = 168 µs

Maximum reaction time = 2 x 18 µs + 64 µs + 150 µs = 250 µs

> **Note**
>
> You can compensate for the minimum response time by assigning the changeover and switch-off differences accordingly.

##### Indecision

The indecision is the difference between the maximum and the minimum response time. With an absolute encoder this amounts to

Indecision

Indecision = message frame time + monoflop time

With programmable absolute encoders:

Indecision = message frame time + monoflop time + 1/max. step sequence frequency

---
title: "Cam control (S7-300, S7-400)"
package: TFCamMainenUS
topics: 19
devices: [S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Cam control (S7-300, S7-400)

This section contains information on the following topics:

- [Cam control basics (S7-300, S7-400)](#cam-control-basics-s7-300-s7-400)
- [Functions of the FM x52 (S7-300, S7-400)](#functions-of-the-fm-x52-s7-300-s7-400)
- [Using FM 352 (S7-300, S7-400)](Using%20FM%20352%20%28S7-300%2C%20S7-400%29.md#using-fm-352-s7-300-s7-400)
- [Using FM 452 (S7-300, S7-400)](Using%20FM%20452%20%28S7-300%2C%20S7-400%29.md#using-fm-452-s7-300-s7-400)

## Cam control basics (S7-300, S7-400)

This section contains information on the following topics:

- [What is cam control? (S7-300, S7-400)](#what-is-cam-control-s7-300-s7-400)
- [Properties of the cam types (S7-300, S7-400)](#properties-of-the-cam-types-s7-300-s7-400)
- [Normal tracks and track results (S7-300, S7-400)](#normal-tracks-and-track-results-s7-300-s7-400)
- [Special tracks (S7-300, S7-400)](#special-tracks-s7-300-s7-400)
- [Hysteresis (S7-300, S7-400)](#hysteresis-s7-300-s7-400)
- [Dynamic adjustment (S7-300, S7-400)](#dynamic-adjustment-s7-300-s7-400)
- [Interfaces of the cam controller (S7-300, S7-400)](#interfaces-of-the-cam-controller-s7-300-s7-400)
- [Encoder signals (S7-300, S7-400)](#encoder-signals-s7-300-s7-400)

### What is cam control? (S7-300, S7-400)

#### Cam control

Cam controllers are implemented to activate position-dependent or time-dependent functions. They are far superior to mechanical cam controllers, in particular due to their high flexibility; changes can for example be implemented during operation using software.

A cam generates position-dependent switching signals depending on the position values of the axis or an external encoder. You distinguish between position-based and time-based cams.

A cam is defined by the following:

- Initial position and final position ([position-based cams](#properties-of-the-cam-types-s7-300-s7-400))
- Initial position and ON period ([time-based cams](#properties-of-the-cam-types-s7-300-s7-400))

### Properties of the cam types (S7-300, S7-400)

#### Cam types

You can assign each cam for operation as a position-based cam or time-based cam.

The following table sets outs the properties of the two cam types:

|  | Position-based cams | Time-based cams |
| --- | --- | --- |
| **Representation** | ![Cam types](images/24633443467_DV_resource.Stream@PNG-en-US.png) | ![Cam types](images/24633462155_DV_resource.Stream@PNG-en-US.png) |
| **Parameter assignment** | The following parameters are assigned:  - Cam start - Cam end - Effective direction - Lead time | The following parameters are assigned:  - Cam start - Activation time - Effective direction - Lead time |
| **Effective direction** | Two effective directions are supported:  - positive: The cam is activated at the cam start, if the axis is moving in direction of increasing actual values. - negative: The cam is activated at the cam end, if the axis is moving in direction of decreasing actual values.   You can set both effective directions in parallel. | Two effective directions are supported:  - positive: The cam is activated at the cam start, if the axis is moving in direction of increasing actual values. - negative: The cam is activated at the cam start if the axis is moving in direction of decreasing actual values.   You can set both effective directions in parallel. |
| **Enabling** | The cam is activated:  - at the cam start, if the axis is moving in positive direction, and a positive effective direction is set. - at the cam end if the axis is moving in a negative direction and a negative effective direction is set. - when the actual value lies within the cam range. | The cam is activated:  - at the cam start if the axis is moving in positive direction and a positive effective direction is set or the axis is moving in a negative direction and a negative effective direction is set.   After it has been activated, the full cam activation time elapses. even if the direction of motion of the axis changes after the cam is activated. The cam is **not** retriggered if its start position is passed once again within the cam activation time. |
| **Deactivating** | The cam is deactivated if:   - the assigned distance has been traveled - its effective direction is opposite to the direction of the axis motion, and you have not assigned a hysteresis - the actual value is out of the cam range. | The cam is deactivated on expiration of the assigned time. |
| **Path length** | The path length of the cam is defined by the cam start and cam end.  The cam start and cam end belong to the active section of the cam. | The path length of the cam is determined by the axis velocity within the cam activation time. |
| **ON period** | The on period of the cam is determined by the speed at which the axis travels across the path length of the cam. | The on period of the cam is assigned with the activation time. |

#### Direction recognition

The direction of the axis motion is determined as follows:

- At each pulse of the incremental encoder.
- With each error-free frame of an SSI encoder.

#### Inverse cam

An inverse cam can briefly be generated with "Change cam edge" if the new cam start is greater than the old cam end. The table below shows the effect of an inverse cam on a linear and on a rotary axis.

| Inverse cam with a linear axis | Inverse cam with a rotary axis |
| --- | --- |
| ![Inverse cam](images/20316588811_DV_resource.Stream@PNG-en-US.png) | ![Inverse cam](images/20316675979_DV_resource.Stream@PNG-en-US.png) |
| The cam start is greater than the cam end | The cam start is more positive than the cam end |
| With both types of axis there must always be a minimum clearance of 4 pulses between the cam start and the cam end. |  |

### Normal tracks and track results (S7-300, S7-400)

#### Cam tracks

The 32 tracks can be used to control up to 32 different switching actions. You can evaluate the tracks based on the checkback signals.

The first 13 tracks (track 0 to 12) are each assigned a digital output (Q0 to Q12) of FM 352. This output can be used for the direct control of a connected contactor, for example.   
The first 16 tracks (track 0 to 15) in the FM 452 are each assigned a digital output (Q0 to Q15).

#### Track result

The system provides up to 128 cams which can be assigned to user-specific tracks.

Each track can be assigned several cams. The track result is a logic OR operation derived from all cam values of this track.

#### Example of a track result

During parameter assignment, you define the following cams for track 3:

| Cam | Cam start | Cam end |
| --- | --- | --- |
| 1 | 101 µm | 106 µm |
| 2 | 100 µm | 104 µm |

The figure below shows the track result.

![Example of a track result](images/20317472907_DV_resource.Stream@PNG-en-US.png)

#### Track enable

You must activate the tracks used in order to transfer the track results of tracks 0 to 12 as track signals to the digital outputs Q0 to Q12 of FM 352. The FM 452 has tracks 0 to 15.

#### External enable of a track

You can assign an external enable signal for track 3 in the machine data. Track signal 3 is then logically linked to digital input I3 by an AND operation before it can switch digital output Q3 of the FM 352.

Digital output Q3 is thus only set if the following conditions are satisfied:

- The corresponding track is enabled.
- At least one cam on this track is active (track result = 1).
- The corresponding digital input I3 was set by an external event.

Tracks 3 to 10 are available for external enabling in the FM 452.

#### Setting the track signals

The track signals 0 to 12 (according to digital outputs Q0 to Q12) can be set by the cam control system, or by the CPU. Track signals 0 to 15 can be set in the FM 452.

### Special tracks  (S7-300, S7-400)

#### Definition

You can program tracks 0 to 2 for operation as special tracks:

- Track 0 or 1: Counter cam track
- Track 2: Brake cam track

  Input I0 must be evaluated in order to enable the track.

#### Requirements

Requirements of working with special tracks:

- You programmed the cams for the track
- Cam processing is enabled
- The corresponding track is enabled
- The track is programmed as special track

#### Counter cam track

A counter cam track counts the status transitions of the track results on this track.

Define a counter high counter value for the counter cam track and then start the counter function.

The counter value of the relevant track decrements by the count of 1 at each positive edge of the track result signal.

The track flag bit = 0 as long as the value of the counter cam track is not equal to zero.

The controller sets the track flag bit and, if assigned parameters accordingly, the [track signal](#interfaces-of-the-cam-controller-s7-300-s7-400) when the counter value = 0.

It resets the track flag bit and sets the default value of the counter at the next negative edge of the track result signal (all cams on this track are disabled).

The figure below shows how a counter cam track is switched.

![Counter cam track](images/20317521931_DV_resource.Stream@PNG-en-US.png)

#### Brake cam track

In order to use track 2 as a brake cam track, interconnect digital input I0.

A positive edge of the I0 signal sets the track flag bit.

The track flag bit is reset again when:

- there is no longer a "1" signal at I0 **and** afterwards
- the controller has detected a negative edge at the track 2 result signal.

The figure below shows how a brake cam track is switched.

![Brake cam track](images/20317621899_DV_resource.Stream@PNG-en-US.png)

In the example, the track flag bit is reset by a negative edge at cam 3 or 4.

### Hysteresis (S7-300, S7-400)

#### Definition

Mechanical imbalance at the axis may cause fluctuation of the actual position value. If the actual position value is offset by one edge of a cam, or within an active cam with only one effective direction, this cam's activation would be cycled on and off continuously. A hysteresis prevents this flutter.

A hysteresis setting is dependent on the actual value, and applies globally to all cams. It is enabled when a direction reversal is detected. A hysteresis will always take effect, regardless of whether or not a cam is set at the current axis position.

#### Rules for the hysteresis range

Rules applicable to the hysteresis range:

- The hysteresis will always be set when a directional reversal is detected.
- The indication of the actual value remains constant within the hysteresis.
- The direction is not redefined within the hysteresis.
- A position-based cam is neither activated nor deactivated within the hysteresis.
- A time-based cam is not activated within the hysteresis. An active time-based cam is deactivated on expiration of the assigned activation (not only on reaching the hysteresis limit).
- When the value is out of the hysteresis range, the FM x52 sets:

  - the actual position value
  - the current direction of motion of the axis
  - the current states of all cams
- The hysteresis range applies to all cams.

#### Direction reversal of a cam with hysteresis

The table below gives an example of the response to cam direction reversal. A distinction must be made between the reaction of position- and time-based cams. The effective direction of the cam is **positive**.

| Position-based cam | Time-based cam |
| --- | --- |
| ![Direction reversal of a cam with hysteresis](images/20319252747_DV_resource.Stream@PNG-en-US.png) | ![Direction reversal of a cam with hysteresis](images/20319634315_DV_resource.Stream@PNG-en-US.png) |
| The hysteresis will be set when a directional reversal is detected. The cam is deactivated immediately when the the hysteresis range is violated. | The cam always remains active for the duration of the assigned activation time. |
| ![Direction reversal of a cam with hysteresis](images/20319657483_DV_resource.Stream@PNG-de-DE.png) Cam    ![Direction reversal of a cam with hysteresis](images/20319681931_DV_resource.Stream@PNG-de-DE.png) Hysteresis |  |

### Dynamic adjustment (S7-300, S7-400)

#### Introduction

The dynamic adjustment is used to compensate delay times of the connected control elements.

#### Lead time

You can program a delay time and assign it as derivative-action time to each cam. You can assign one derivative-action time to each cam. The derivative-action time applies to the cam start and end position.

#### Correction distance

The actuation distance of a cam is calculated continuously based on the current velocity and derivative-action time. The entire cam is shifted in direction of the actual value by this value. The programmed range is the "static range," and the range calculated based on the derivative-action time represents the "dynamic range."

Actuation distance = lead time x actual velocity of the axis

FM x52 calculates the actuation distance of all cams within 1/4 of the longest parameterized lead time.

An extremely high derivative-action time of a cam reduces the dynamic performance of cam processing.

### Interfaces of the cam controller (S7-300, S7-400)

#### Overview

Taking FM 352 as an example, the schematic diagram below sets out the major interfaces of the cam controller to illustrate the connection between data, inputs and outputs. Differences to the FM 452 are set out in the table below.

![Overview](images/22558231563_DV_resource.Stream@PNG-en-US.png)

| No. | Description |
| --- | --- |
| ① | The cam processing functions of FM x52 calculate the cam identifier bits on the basis of the switching conditions and actual value. The module also determines the track results according to the assignment of the cams to the tracks. |
| ② | If you assigned track 0 or 1 as a counter cam track, the track result of the cam controller (point 1) is logically linked to the counter result in order to produce the track identifier bit. The track identifier bit is otherwise equivalent to the track result. |
| ③ | If you assigned track 2 as a brake cam track, the track result of the cam controller (point 1) is logically linked to input I0 to produce the track identifier bit. The track identifier bit is otherwise equivalent to the track result. |
| ④ | Using machine data, you can control whether the previously determined track identifier bits of tracks 0 to 12 (in FM 352) or 0 to 15 (in FM 452) of the cam controller are transferred to the channel DB, or whether they are set directly by the track enable signal (TRACK_EN). |
| ⑤ | You enable the track signals of tracks 0 to 12 (or 0 to 15) by setting TRACK_EN and the count function by setting CNTC0_EN / CNTC1_EN. |
| ⑥ | FM 352: The track signal of track 3 and digital input I3 can be logically linked by an AND operation provided you have set this option in the machine data (EN_IN_I3). |
| FM 452: The track signals of tracks 3 to 10 can be logically linked to digital inputs I3 to I10 with an AND operation if you have set this option in the machine data (EN_IN_I3 to EN_IN_I10). |  |
| ⑦ | All track and cam identifier bits can be read at this location (i.e. before being logically linked with machine and channel data) using the ACTPOS_EN or CAMOUT_EN job.  At tracks 3 to 31, the track identifier bit is equivalent to the track result (point 1). |
| ⑧ | FM 352: The track signals of tracks 0 to 12 are available in the checkback signals after having been logically linked with the machine data (e.g. axis type, software limit switch, distance per encoder revolution...) and channel data. The track signals of tracks 13 to 31 and the track identifier bits of point 7 are identical. The track signals of tracks 0 to 12 are also available at the digital outputs Q0 to Q12. |
| FM 452: The track signals of tracks 0 to 15 are available in the checkback signals after having been logically linked with the machine and channel data. The track signals of tracks 16 to 31 and the track identifier bits of point 7 are identical. The track signals of tracks 0 to 15 are also available at the digital outputs Q0 to Q15. |  |

### Encoder signals (S7-300, S7-400)

This section contains information on the following topics:

- [Supported encoders (S7-300, S7-400)](#supported-encoders-s7-300-s7-400)
- [Incremental encoder (S7-300, S7-400)](#incremental-encoder-s7-300-s7-400)
- [Proximity switches (S7-300, S7-400)](#proximity-switches-s7-300-s7-400)
- [Absolute encoder (SSI) (S7-300, S7-400)](#absolute-encoder-ssi-s7-300-s7-400)

#### Supported encoders (S7-300, S7-400)

##### Connectable incremental encoders

[Incremental encoders](#incremental-encoder-s7-300-s7-400) with two pulses 90° out of phase with or without zero marks are supported:

- Encoders with asymmetrical 24 V output signals

  - Limit frequency = 50 kHz
  - Cable up to 100 m long, shielded
- Encoders with symmetrical output signals with 5 V differential interface in accordance with RS 422

  - Limit frequency = 1 MHz
  - With 5 V voltage supply: Cable up to 32 m long, shielded
  - With 24 V voltage supply: Cable up to 100 m long, shielded

> **Note**
>
> If the 5 V encoder does not output a zero mark signal and wire-break monitoring is enabled, you must interconnect the zero mark signal inputs N and /N externally so that the inputs have different signal levels (for example, N to 5 V, /N to ground).

##### Supported initiators

The FM x52 supports the following [initiators](#proximity-switches-s7-300-s7-400):

- Initiators with 24 V signal level (proximity switches)
- Limit frequency = 50 kHz
- Cable up to 100 m long

##### Absolute encoders supported

[Absolute encoders](#absolute-encoder-ssi-s7-300-s7-400) with serial interface are supported. Position data are transferred synchronously using the SSI protocol (**S**ynchronous**S**erial**I**nterface). The FM x52 only supports the GRAY code. Due to the arrangement of the data bits in the transferred frames, the data formats "fir tree", "half fir tree" and "right-justified" are used.

Absolute encoders are divided into the categories:

- Single-turn encoder

  The total range of single-turn encoders is scaled to one revolution.
- Multiturn encoder

  The total range of multiturn encoders is scaled to several revolutions.

| Encoder type | Frame length / type |
| --- | --- |
| Single-turn encoder  Single-turn encoder  Single-turn encoder  Multiturn encoder  Multiturn encoder  Listen in  Listen in | 13-bit half fir tree  13-bit right-justified  25-bit right-justified  25-bit fir tree  25-bit right-justified  Fir tree  Right-justified |
| Special setting:  Multiturn encoder in single-turn mode | 25-bit half fir tree |

The transmission rate for data transmission depends on the cable length:

- Max. 125 kHz for 320 m of cable, shielded
- Max. 250 kHz for 160 m of cable, shielded
- Max. 500 kHz for 60 m of cable, shielded
- Max. 1 MHz for 20 m of cable, shielded

#### Incremental encoder (S7-300, S7-400)

##### Signal shapes

The following figure illustrates the signal forms of encoders with asymmetrical and symmetrical output signals.

![Signal shapes](images/20441103755_DV_resource.Stream@PNG-en-US.png)

##### Signal evaluation

**Increments**

An increment identifies a signal period of the encoders signals A and B. This value is specified in the technical data and/or on the rating plate of the encoder.

The figure below shows the ratio of increments to pulses.

![Signal evaluation](images/20440811787_DV_resource.Stream@PNG-en-US.png)

**Pulses**

FM x52 evaluates all 4 edges of signals A and B in each increment (quadruple evaluation).

1 increment (encoder default) = 4 pulses (FM evaluation)

##### Reaction times

FM x52 has the following response times for connected incremental encoders:

- Minimum reaction time = cam cycle time + switching time of the connected switching elements
- Maximum reaction time = 2 x cam cycle time + switching time of the connected switching elements

##### Example of reaction times

Example of the min./max. reaction time with 16 cams:

- Cam cycle time: approx. 20 µs
- Switching time of the hardware: approx. 150 µs

Minimum reaction time = 20 µs + 150 µs = 170 µs

Maximum reaction time = 2 x 20 µs + 150 µs = 190 µs

> **Note**
>
> You can compensate the reaction time by assigning the cam parameters accordingly or using dynamic adjustment.

##### Flat gain

The flat gain is equivalent to the difference between the min./max. reaction time. For incremental encoders this is:

Flat gain = cam cycle time

> **Note**
>
> If the switching time of the FM x52 hardware and of the connected switching elements can be disregarded, reliable cam activation is always ensured if the cam is longer than the distance covered within the cam cycle time.

#### Proximity switches (S7-300, S7-400)

##### Definition

Initiators are simple switches which output pulse-shaped signals, and do not return a directional signal. You define the direction with the machine data "Initiator direction".

| Symbol | Meaning |
| --- | --- |
|  | **Caution** |
| Risk of material damage!  Incorrect direction settings can cause serious errors in the system (for example, faulty control of a unit of equipment).  Check the direction settings in the commissioning phase, and whenever you replace an initiator. |  |

##### Signal evaluation

With an initiator, the rising edge of signal A* is counted.

#### Absolute encoder (SSI) (S7-300, S7-400)

##### Absolute encoder pulse evaluation

1 increment (encoder default) = 1 pulse (FM evaluation)

##### Listen in

"Listen in" means: An absolute encoder is operated in parallel in two modules (for example FM x51 and FM x52). The FM x51 positioning module is the master and clocks the absolute encoder; the FM x52 electronic cam controller acts as the slave listening in to the signals of the SSI frame.

Set "Increments/Encoder revolution" and "Number of revolutions" to the master setting. The "Transmission rate" is not relevant. Depending on the encoder type select "Listen in" or "Listen in Right-Justified" for "Frame Length".

##### Reaction times

The FM x52 has the following reaction times for absolute encoders:

- Minimum reaction time = frame run time + cam cycle time + switching time of the connected switching elements
- Maximum reaction time = 2 x frame runtime + monoflop time + 2 x cam cycle time + switching time of the connected switching elements
- For programmable absolute encoders:

  Maximum reaction time = frame runtime + monoflop time + 2 x cam cycle time + switching time of the connected switching elements +1/max. step sequence rate

##### Monoflop time

The following limit values apply to the monoflop time:

- Minimum monoflop time: > 15 µs
- Maximum monoflop time: < 64 µs

Encoders with values outside the limits shown here are not permitted.

##### Frame run time

The frame run times depend on the transmission rate:

| Transmission rate | Frame run time for 13 bits | Frame run time for 25 bits |
| --- | --- | --- |
| 0.125 MHz | 112 µs | 208 µs |
| 0.250 MHz | 56 µs | 104 µs |
| 0.500 MHz | 28 µs | 52 µs |
| 1000 MHz | 14 µs | 26 µs |

##### Example of Reaction Times

The following example shows how to calculate the minimum and maximum reaction times. In the example a programmable encoder is not used.

- Cam cycle time: approx. 20 µs for max. 16 cams
- Switching time of the hardware: approx. 150 µs
- Frame run time: 26 µs at a transmission rate of 1 MHz (25-bit frame)
- Monoflop time: 20 µs (depends on the encoder: typical 20 µs to 40 µs

Maximum reaction time = 26 µs + 20 µs + 150 µs = 196 µs

Maximum reaction time = 2 x 26 µs + 20 µs + 2 x 20 µs + 150 µs = 262 µs

> **Note**
>
> You can compensate the reaction time by assigning the cam parameters accordingly or by using dynamic adjustment.

##### Flat gain

The flat gain is equivalent to the difference between the minimum and maximum reaction times.

For an absolute encoder, it is as follows:

- Flat gain = cam cycle time + frame run time + monoflop time

With programmable absolute encoders, it is as follows:

- Flat gain = cam cycle time + frame run time + monoflop time  
  + 1/max. step sequence frequency

> **Note**
>
> If the switching time of the FM x52 hardware and of the connected switching elements can be disregarded, reliable cam activation is always ensured if the cam is longer than the distance covered within the cam cycle time.

## Functions of the FM x52 (S7-300, S7-400)

This section contains information on the following topics:

- [Writing and enabling machine data (S7-300, S7-400)](#writing-and-enabling-machine-data-s7-300-s7-400)
- [Reading machine data (S7-300, S7-400)](#reading-machine-data-s7-300-s7-400)
- [Writing cam data (S7-300, S7-400)](#writing-cam-data-s7-300-s7-400)
- [Reading cam data (S7-300, S7-400)](#reading-cam-data-s7-300-s7-400)

### Writing and enabling machine data (S7-300, S7-400)

#### Writing and activating machine data

You can use the machine data to adapt the FM x52 to the axis and the encoder.

You can change parameters during operation using the user program.

All parameters are stored in the parameter DB:

- Machine data are stored in the parameter DB at addresses 3.1 to 104.0.

Enter the parameter DB number in the corresponding channel DB.

You can enter the parameters with the DB Editor, or indeed simply and easily enter them in the "System of units", "Axis", "Encoder" and "Tracks" dialogs and write them to the parameter DB with the "Export" function.

You can use the "Import" function to import parameters from an existing parameter DB to the dialogs.

#### Initial parameter assignment

If the module does not yet contain any machine data (feedback signal PARA = 0), proceed as follows for initial parameter assignment without the parameter assignment dialogs:

1. Enter the new values in the parameter DB.
2. Download the parameter DB to the CPU.
3. Set the following trigger bit in the channel DB:

   - Write machine data (MDWR_EN = 1)
4. Call the [CAM_CTRL](FM%20x52%20Cam%20Controlling%20%28S7-300%2C%20S7-400%29.md#cam_ctrl-s7-300-s7-400) or [CAM_CTRL_452](FM%20x52%20Cam%20Controlling%20%28S7-300%2C%20S7-400%29.md#cam_ctrl_452-s7-300-s7-400) instruction in the cyclic user program.

#### Modifying machine data

To modify existing machine data (feedback signal PARA = 1) using the user program, proceed as follows:

1. Enter the new values in the parameter DB.
2. Set the trigger bits at the channel DB:

   - Write machine data (MDWR_EN = 1)
   - Activate machine data (MD_EN = 1)
3. Call the [CAM_CTRL](FM%20x52%20Cam%20Controlling%20%28S7-300%2C%20S7-400%29.md#cam_ctrl-s7-300-s7-400) or [CAM_CTRL_452](FM%20x52%20Cam%20Controlling%20%28S7-300%2C%20S7-400%29.md#cam_ctrl_452-s7-300-s7-400) instruction in the cyclic user program.
4. Check whether the previous cam data and the modified machine data are compatible.
5. Always rewrite the cam data of the parameterized cams, irrespective of whether or not they have been changed (CAM1WR_EN … CAM8WR_EN).

If you set the trigger bits simultaneously, the CAM_CTRL or CAM_CTRL_452 instruction ensures the jobs are processed in the correct order.

Otherwise, you must always change the machine data in the following order:

1. Write machine data
2. Activate machine data

#### Data used in the channel DB

| Address | Name | Type | Start value | Comment |
| --- | --- | --- | --- | --- |
| 35.0 | MDWR_EN | BOOL | FALSE | 1 = write machine data |
| 35.1 | MD_EN | BOOL | FALSE | 1 = enable machine data |

> **Note**
>
> If any parameters relevant for synchronization were modified, the synchronization will be canceled when the machine data are activated. The functions will also be reset and all machine and cam data deleted from the module.
>
> Parameters relevant to synchronization:
>
> - Axis type
> - End of rotary axis
> - Signal type
> - Distance per encoder revolution
> - Increments per encoder revolution
> - Number of revolutions
> - Reference point coordinate
> - Absolute encoder adjustment
> - Type of reference point retriggering
> - Direction adaptation
> - Number of cams
> - Software limit switch start and end

### Reading machine data (S7-300, S7-400)

#### Reading machine data

To read actual machine data from the module:

1. Set the following trigger bit in the channel DB:

   - Reading machine data (MDRD_EN = 1)
2. Call the [CAM_CTRL](FM%20x52%20Cam%20Controlling%20%28S7-300%2C%20S7-400%29.md#cam_ctrl-s7-300-s7-400) or [CAM_CTRL_452](FM%20x52%20Cam%20Controlling%20%28S7-300%2C%20S7-400%29.md#cam_ctrl_452-s7-300-s7-400) instruction in the cyclic user program.

This saves the current machine data to the parameter DB on the CPU.

#### Data used in the channel DB

| Address | Name | Type | Initial value | Comment |
| --- | --- | --- | --- | --- |
| 37.1 | MDRD_EN | BOOL | FALSE | 1 = read machine data |

### Writing cam data (S7-300, S7-400)

#### Writing cam data

Cam data define the type and function principle of the cams and their assignment to the tracks.

Cam data are stored in the parameter DB, starting at address 108.0. These data are grouped in packets, each consisting of 16 cams.

Cam data are active immediately after having been written.

To write cam data without the parameter assignment dialogs, proceed as follows:

1. Enter the new values in the parameter DB.
2. Download the parameter DB to the CPU.
3. Set the trigger bits in the channel DB (CAM1WR_EN … CAM8WR_EN)
4. Call the [CAM_CTRL](FM%20x52%20Cam%20Controlling%20%28S7-300%2C%20S7-400%29.md#cam_ctrl-s7-300-s7-400) or [CAM_CTRL_452](FM%20x52%20Cam%20Controlling%20%28S7-300%2C%20S7-400%29.md#cam_ctrl_452-s7-300-s7-400) instruction in the cyclic user program.

#### Data used in the channel DB

| Address | Name | Type | Initial value | Comment |
| --- | --- | --- | --- | --- |
| 35.3 | CAM1WR_EN | BOOL | FALSE | 1 = write cam data 1 (cams 0 to 15) |
| 35.4 | CAM2WR_EN | BOOL | FALSE | 1 = write cam data 2 (cams 16 to 31) |
| 35.5 | CAM3WR_EN | BOOL | FALSE | 1 = write cam data 3 (cams 32 to 47) |
| 35.6 | CAM4WR_EN | BOOL | FALSE | 1 = write cam data 4 (cams 48 to 63) |
| 35.7 | CAM5WR_EN | BOOL | FALSE | 1 = write cam data 5 (cams 64 to 79) |
| 36.0 | CAM6WR_EN | BOOL | FALSE | 1 = write cam data 6 (cams 80 to 95) |
| 36.1 | CAM7WR_EN | BOOL | FALSE | 1 = write cam data 7 (cams 96 to 111) |
| 36.2 | CAM8WR_EN | BOOL | FALSE | 1 = write cam data 8 (cams 112 to 127) |

### Reading cam data (S7-300, S7-400)

#### Reading cam data

To read actual cam data from the module:

1. Set the following trigger bit in the channel DB:

   - Read cam data (CAM1RD_EN … CAM8RD_EN)
2. Call the [CAM_CTRL](FM%20x52%20Cam%20Controlling%20%28S7-300%2C%20S7-400%29.md#cam_ctrl-s7-300-s7-400) or [CAM_CTRL_452](FM%20x52%20Cam%20Controlling%20%28S7-300%2C%20S7-400%29.md#cam_ctrl_452-s7-300-s7-400) instruction in the cyclic user program.

This saves the actual cam data to the parameter DB on the CPU.

#### Data used in the channel DB

| Address | Name | Type | Initial value | Comment |
| --- | --- | --- | --- | --- |
| 37.2 | CAM1RD_EN | BOOL | FALSE | 1 = read cam data 1 (cams 0 to 15) |
| 37.3 | CAM2RD_EN | BOOL | FALSE | 1 = read cam data 2 (cams 16 to 31) |
| 37.4 | CAM3RD_EN | BOOL | FALSE | 1 = read cam data 3 (cams 32 to 47) |
| 37.5 | CAM4RD_EN | BOOL | FALSE | 1 = read cam data 4 (cams 48 to 63) |
| 37.6 | CAM5RD_EN | BOOL | FALSE | 1 = read cam data 5 (cams 64 to 79) |
| 37.7 | CAM6RD_EN | BOOL | FALSE | 1 = read cam data 6 (cams 80 to 95) |
| 38.0 | CAM7RD_EN | BOOL | FALSE | 1 = read cam data 7 (cams 96 to 111) |
| 38.1 | CAM8RD_EN | BOOL | FALSE | 1 = read cam data 8 (cams 112 to 127) |

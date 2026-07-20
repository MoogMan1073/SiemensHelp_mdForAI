---
title: "Using ET 200S 1SSI (S7-300, S7-400)"
package: TFHWC1SSIenUS
topics: 42
devices: [S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Using ET 200S 1SSI (S7-300, S7-400)

This section contains information on the following topics:

- [Terminal Assignment of the 1SSI (S7-300, S7-400)](#terminal-assignment-of-the-1ssi-s7-300-s7-400)
- [Configuring and assigning parameters to 1SSI (S7-300, S7-400)](#configuring-and-assigning-parameters-to-1ssi-s7-300-s7-400)
- [Diagnostics of the 1SSI (S7-300, S7-400)](#diagnostics-of-the-1ssi-s7-300-s7-400)

## Terminal Assignment of the 1SSI (S7-300, S7-400)

### Wiring Rules

The cables (terminals 1 and 5 and terminals 4 and 8) must be shielded, twisted-pair cables. The shield must be supported at both ends. To do this, use the shield contact (see the appendix of the [ET 200S Distributed I/O System](http://support.automation.siemens.com/WW/view/en/1144348) operating instructions).

### Terminal assignment of the 1SSI

The following table shows the terminal assignment of 1SSI.

| View | Terminal assignment | Remarks |  |
| --- | --- | --- | --- |
| ![Terminal assignment of the 1SSI](images/23262516875_DV_resource.Stream@PNG-en-US.png) |  | Terminals 1 to 8: |  |
| 1/5: | Data from the SSI encoder <sup>1)</sup> |  |  |
| 2/6: | Power supply for absolute value encoder and switch <sup>2)</sup> |  |  |
| 3: | Chassis ground |  |  |
| 7: | Digital input latch function |  |  |
| 4/8: | SSI clock (clock wire) <sup>1)</sup> |  |  |
| ![Terminal assignment of the 1SSI](images/23262981899_DV_resource.Stream@PNG-en-US.png) |  |  |  |
| <sup>1)</sup> It is essential that you maintain the correct polarity when wiring the encoder. If you do not, an absolute encoder error is reported. Signals to RS 422   <sup>2)</sup> Short circuit-proof, maximum 0.5 A. |  |  |  |

## Configuring and assigning parameters to 1SSI (S7-300, S7-400)

This section contains information on the following topics:

- [Operation (S7-300, S7-400)](#operation-s7-300-s7-400)
- [Standard mode parameters (S7-300, S7-400)](#standard-mode-parameters-s7-300-s7-400)
- [Control and feedback interface for standard mode (S7-300, S7-400)](#control-and-feedback-interface-for-standard-mode-s7-300-s7-400)
- [Fast mode parameters (S7-300, S7-400)](#fast-mode-parameters-s7-300-s7-400)
- [Fast mode feedback interface (S7-300, S7-400)](#fast-mode-feedback-interface-s7-300-s7-400)

### Operation (S7-300, S7-400)

This section contains information on the following topics:

- [Selecting an operating mode (S7-300, S7-400)](#selecting-an-operating-mode-s7-300-s7-400)

#### Selecting an operating mode (S7-300, S7-400)

##### Operating mode

You define 1SSI functionality by specifying an operating mode.

| Operating mode | Description |
| --- | --- |
| [Standard Mode](#standard-mode-parameters-s7-300-s7-400) | 1SSI standard operating mode with complete functional scope:  - Scaling the encoder value - Direction reversal to adapt the direction of motion of the absolute encoder to the axis. - Encoder value acquisition modes:   - freewheeling   - synchronous to the update rate - Maximum encoder sampling rate (e.g. for ultrasonic encoders) is taken into account in isochrone mode - Lifebeat in isochrone mode - Parity check of encoder value can be performed - Gray code/dual code converter - Latch function for freezing the current encoder value - Compare function for comparing the current encoder value and loadable comparison values   This operating mode is suitable for monitoring or detecting position points and for length measurement, edge detection and synchronization with workpieces. |
| [Fast mode](#fast-mode-parameters-s7-300-s7-400) | The 1SSI has compressed functionality in this operating mode. The latch and compare functions are not available.  This operating mode is suitable for rapid encoder value acquisition and controller applications such as position controllers with the position as the actual value. |

### Standard mode parameters (S7-300, S7-400)

This section contains information on the following topics:

- [Enabling group diagnostics (S7-300, S7-400)](#enabling-group-diagnostics-s7-300-s7-400)
- [Selecting encoder value acquisition (S7-300, S7-400)](#selecting-encoder-value-acquisition-s7-300-s7-400)
- [Selecting encoder type (S7-300, S7-400)](#selecting-encoder-type-s7-300-s7-400)
- [Selecting Gray code/dual code converter (S7-300, S7-400)](#selecting-gray-codedual-code-converter-s7-300-s7-400)
- [Selecting the transmission rate (S7-300, S7-400)](#selecting-the-transmission-rate-s7-300-s7-400)
- [Selecting parity (S7-300, S7-400)](#selecting-parity-s7-300-s7-400)
- [Selecting monoflop time (S7-300, S7-400)](#selecting-monoflop-time-s7-300-s7-400)
- [Activating scaling (S7-300, S7-400)](#activating-scaling-s7-300-s7-400)
- [Entering number of adjusted bits (S7-300, S7-400)](#entering-number-of-adjusted-bits-s7-300-s7-400)
- [Enabling direction reversal (S7-300, S7-400)](#enabling-direction-reversal-s7-300-s7-400)
- [Entering increments per encoder revolution (S7-300, S7-400)](#entering-increments-per-encoder-revolution-s7-300-s7-400)
- [Selecting encoder value latching (S7-300, S7-400)](#selecting-encoder-value-latching-s7-300-s7-400)
- [Selecting comparator behavior (S7-300, S7-400)](#selecting-comparator-behavior-s7-300-s7-400)
- [Enabling lifebeat (default mode) (S7-300, S7-400)](#enabling-lifebeat-default-mode-s7-300-s7-400)
- [Setting the encoder sampling rate (S7-300, S7-400)](#setting-the-encoder-sampling-rate-s7-300-s7-400)

#### Enabling group diagnostics (S7-300, S7-400)

##### Group diagnostics

Channel-specific diagnostics will be carried out if you enable group diagnostics in your parameter assignment.

#### Selecting encoder value acquisition (S7-300, S7-400)

##### Description

The following alternatives are available for encoder value acquisition:

- freewheeling encoder value acquisition
- synchronous encoder value acquisition
- Isochrone encoder value acquisition

You can set cyclic or synchronous encoder value acquisition with the "Detection" parameter in parameter assignment. This parameter only works in non-isochrone mode.

Encoder value acquisition will be isochrone when the 1SSI is operating in isochrones mode. In this case, the "Detection" parameter is not evaluated.

The following table sets out these encoder value acquisition conditions.

| Operation | "Detection" parameter | Encoder value acquisition |
| --- | --- | --- |
| Non-isochrone mode | freewheeling | freewheeling encoder value acquisition |
| Synchronous | synchronous encoder value acquisition |  |
| Isochrone mode | - (irrelevant) | [Isochrone encoder value acquisition](Motion%20Control%20%28S7-300%2C%20S7-400%29%20%28TFMCMain3_400enUS%29.md#encoder-value-acquisition-s7-300-s7-400) |

##### Cyclic encoder value acquisition

You obtain maximum accuracy when [latching the encoder value](#selecting-encoder-value-latching-s7-300-s7-400) during freewheeling encoder value acquisition.

The 1SSI initiates the transmission of a frame each time the parameterized [monoflop time](#selecting-monoflop-time-s7-300-s7-400) elapses.

The 1SSI processes the acquired encoder value asynchronously to these freewheeling frames in the update rate cycle.

Freewheeling acquisition therefore returns encoder values of different ages. The difference between the maximum and minimum age is the jitter.

##### Synchronous encoder value acquisition

Synchronous encoder value acquisition gives you maximum accuracy.

The 1SSI initiates the transmission of a frame in the cycle of its update rate.

The 1SSI processes the transferred encoder value synchronously with its update rate.

#### Selecting encoder type (S7-300, S7-400)

##### Encoder type

The 1SSI supports the following encoder types:

- Absolute encoder (SSI) with 13 bits

  to
- Absolute encoder (SSI) with 25 bits

You will find the encoder type in the technical specifications for your absolute encoder.

Selecting "No encoder" deactivates the encoder input.

#### Selecting Gray code/dual code converter (S7-300, S7-400)

##### Gray code/dual code converter

The "[Gray code/dual code converter](Motion%20Control%20%28S7-300%2C%20S7-400%29%20%28TFMCMain3_400enUS%29.md#graydual-converter-s7-300-s7-400)" parameter defines how the codes returned by the encoder are processed:

- When "Gray code" is set, the encoder value returned by the absolute encoder in gray code will be converted to dual code.
- When "Dual code" is set, the values returned by the encoder will remain unchanged.

#### Selecting the transmission rate (S7-300, S7-400)

##### Transmission rate

You define the data transmission rate between the SSI encoder and the 1SSI with the "transmission rate".

Select the desired transmission rate in the drop-down box.

Note that the transmission rate affects how accurate and up-to-date the encoder values are.

The maximum transmission rate depends on the cable length:

- 320 m → 125 kHz
- 160 m → 250 kHz
- 60 m → 500 kHz
- 20 m → 1 MHz
- 10 m → 1.5 MHz
- 8 m → 2 MHz

---

**See also**

[Selecting monoflop time (S7-300, S7-400)](#selecting-monoflop-time-s7-300-s7-400)

#### Selecting parity (S7-300, S7-400)

##### Parity

With "Parity", you specify whether no parity, even parity or odd parity should be assigned for an absolute encoder.

A configured parity bit is not included in the "[Encoder Type](#selecting-encoder-type-s7-300-s7-400)" parameter. If a 25-bit encoder with parity is parameterized, the encoder will read 26 bits.

The bit following the LSB (least significant bit) of the encoder is evaluated as a parity bit. A parity error is reported in the [feedback interface](#standard-mode-feedback-interface-s7-300-s7-400-1) via the bit ERR_SSI.

#### Selecting monoflop time (S7-300, S7-400)

##### Monoflop time

The monoflop time represents the interval between two SSI frames.

The parameterized monoflop time must be greater than the monoflop time of the absolute encoder used (refer to the technical specifications of the manufacturer).

The following restriction applies to the monoflop time of the absolute encoder:

(1/transmission rate) &lt; monoflop time of absolute encoder &lt; 64 µs

Select the desired monoflop time in the drop-down box.

The specification of the monoflop time is relevant for [freewheeling encoder value acquisition](#selecting-encoder-value-acquisition-s7-300-s7-400).

---

**See also**

[Selecting the transmission rate (S7-300, S7-400)](#selecting-the-transmission-rate-s7-300-s7-400)

#### Activating scaling (S7-300, S7-400)

##### Encoder value and scaling

The encoder value transferred contains the encoder position of the absolute encoder. In addition to the encoder position, the encoder transfers additional bits located before and after the encoder position, depending on the encoder used.

The 1SSI requires the following information to allow it to detect the encoder position:

- [Encoder type](#selecting-encoder-type-s7-300-s7-400)
- [Number of adjusted bits](#entering-number-of-adjusted-bits-s7-300-s7-400)
- [Increments per encoder revolution](#entering-increments-per-encoder-revolution-s7-300-s7-400)

[Scaling](Motion%20Control%20%28S7-300%2C%20S7-400%29%20%28TFMCMain3_400enUS%29.md#encoder-value-and-scaling-s7-300-s7-400) specifies presentation of the encoder value at the [feedback interface](#standard-mode-feedback-interface-s7-300-s7-400-1).

- "Scaling **on**" specifies that trailing, irrelevant bits in the encoder value are to be discounted.
- "Scaling **off**" specifies that adjusted bits are retained and are available for evaluation.

#### Entering number of adjusted bits (S7-300, S7-400)

##### Number of adjusted bits

The 1SSI requires the number of adjusted bits in order to detect the encoder position and correctly detect the encoder's direction of motion.

You will find this value in the technical specifications for your absolute encoder.

#### Enabling direction reversal (S7-300, S7-400)

##### Direction detection and direction reversal

The 1SSI needs the following information to detect the direction of movement of the encoder correctly:

- [Encoder type](#selecting-encoder-type-s7-300-s7-400)
- [Number of adjusted bits](#entering-number-of-adjusted-bits-s7-300-s7-400)
- [Increments per encoder revolution](#entering-increments-per-encoder-revolution-s7-300-s7-400)

The direction of motion determined is displayed in the [feedback interface](#standard-mode-feedback-interface-s7-300-s7-400-1) and by the LEDs.

- LED UP: Encoder position change from lower to higher value
- LED DN: Encoder position change from higher to lower value

**Direction reversal** adapts the encoder direction of motion to the axis.

Two settings are possible:

- **Off:** The direction of the transferred encoder position is maintained.
- **On:** The direction of the transferred encoder position is reversed. This means that although the encoder sends ascending values, descending values are displayed.

  The reversal relates to the increments/encoder revolution set in the parameters.

##### Example of Direction Reversal

Presettings:

You are using a single-turn encoder with 2<sup>10</sup> (corresponds to 10 bits) = 1024 increments/encoder revolution (resolution/360°) with the following parameter assignment:

- Encoder type: SSI-13 bit
- Number of adjusted bits: 3 places
- Direction reversal: On
- Increments per encoder revolution: 1024

Encoder value before direction reversal: cyclically recorded encoder position 1023

Encoder value after direction reversal: displayed encoder position 0

#### Entering increments per encoder revolution (S7-300, S7-400)

##### Increments per encoder revolution

The "Increments per encoder revolution" parameter defines the number of increments an encoder returns per revolution.

You will find this value in the technical specifications for your absolute encoder.

##### Valid value ranges

The limits depend on the individual encoder models. Only values to the power of 2 are permitted.

- 13-bit encoder type: 16 to 8192
- 14-bit encoder type: 16 to 16384
- 15-bit encoder type: 16 to 32768
- 16-bit encoder type: 16 to 65536
- 17-bit encoder type: 16 to 131072
- 18-bit encoder type: 16 to 262144
- 19-bit encoder type: 16 to 524288
- 20-bit encoder type: 16 to 1048576
- 21-bit encoder type: 16 to 2097152
- 22-bit encoder type: 16 to 4194304
- 23-bit encoder type: 16 to 8388608
- 24-bit encoder type: 16 to 16777216
- 25-bit encoder type: 16 to 33554432

#### Selecting encoder value latching (S7-300, S7-400)

##### Latching the encoder value

You use the latch function to "freeze" the current encoder value of the 1SSI with an edge at the digital input (DI).

The encoder value can thus be evaluated on an event-dependent basis.

A frozen encoder value is identified by the set bit 31 and is retained until the latch function is exited.

The frozen encoder value is entered at the [feedback interface](#standard-mode-feedback-interface-s7-300-s7-400-1) at the position of the otherwise cyclically recorded value and assigned the identifier "Bit 31 set".

> **Note**
>
> Direction determination, comparison, and error monitoring also take place when the encoder value is frozen.

##### Prerequisites for Using the Latch Function

You specify which edge at the digital input is to freeze the encoder value using parameter assignment.

- Falling edge at DI
- Rising edge at DI
- Both edges at DI

Selecting an edge activates the latch function coupled to the digital input.

The encoder value cannot be frozen if "Inactive" is selected.

##### Terminating the Latch Function

The latch function must be acknowledged. When the controller program acknowledges the acceptance of the encoder value, bit 31 is deleted and the encoder value is updated again. Freezing is then possible again.

The figure below shows the latch function process.

![Terminating the Latch Function](images/22021739403_DV_resource.Stream@PNG-en-US.png)

#### Selecting comparator behavior (S7-300, S7-400)

##### Setting comparators

The encoder position detected can be compared with up to two loadable values. Both comparison results are stored in the [feedback interface](#standard-mode-feedback-interface-s7-300-s7-400-1). The appropriate comparator becomes active only after the comparison value is loaded.

You set the two comparators in the "Comparator 1" and "Comparator 2" parameters:

| Setting | Effect on the result of comparison (CMPx) |
| --- | --- |
| inactive | The encoder value is not compared. The feedback bit CMPx = 0 |
| UP | The encoder value is compared in the up direction (UP).  - If the encoder value ≥ comparison value, feedback bit CMPx = 1. - If the encoder value &lt; comparison value, feedback bit CMPx = 0. - If the direction is down, the feedback bit CMPx remains unchanged. - If no change is detected in the encoder value, the feedback bit CMPx will remain unchanged. |
| Down | The encoder value is compared in the down direction (DN).  - If the encoder value ≤ comparison value, feedback bit CMPx = 1. - If the encoder value &gt; comparison value, feedback bit CMPx = 0. - If the direction is up, the feedback bit CMPx will remain unchanged. - If no change is detected in the encoder value, the feedback bit CMPx will remain unchanged. |
| In both directions | The encoder value is compared in both directions.  If the direction is up, the following conditions apply:  - If the encoder value ≥ comparison value, feedback bit CMPx = 1. - If the encoder value &lt; comparison value, feedback bit CMPx = 0. - If no change is detected in the encoder value, the feedback bit CMPx will remain unchanged.   If the direction is down, the following conditions apply:  - If the encoder value ≤ comparison value, feedback bit CMPx = 1. - If encoder value &gt; comparison value, feedback bit CMPx = 0. - If no change is detected in the encoder value, the feedback bit CMPx will remain unchanged. |

The comparison result is deleted and entered in accordance with the directional setting as soon as you load a comparison value.

> **Note**
>
> Only one control bit can be set at a particular time:
>
> CMP_VAL1 or CMP_VAL2).
>
> Otherwise, the ERR_LOAD error will be reported until both control bits are deleted.

##### Loading the Comparison Value

The figure below illustrates the value transfer process:

![Loading the Comparison Value](images/22021846923_DV_resource.Stream@PNG-en-US.png)

##### Comparator in Isochronous Mode

In isochronous mode, the comparison values are loaded at time T<sub>o</sub> and are effective as of time T<sub>i</sub> in the same bus cycle.

#### Enabling lifebeat (default mode) (S7-300, S7-400)

##### Lifebeat

This parameter is only active in isochrone mode.

When lifebeat is activated, the lifebeat bit is toggled each time an encoder value is read in in isochronous mode, i.e. the last value sent is inverted. If a reduction is assigned in the "[Encoder Sampling Rate](#setting-the-encoder-sampling-rate-s7-300-s7-400)" parameter, the value is only toggled if an encoder value has actually been read in.

The lifebeat bit can be found in the [feedback interface](#standard-mode-feedback-interface-s7-300-s7-400-1) in byte 4 / bit 7.

#### Setting the encoder sampling rate (S7-300, S7-400)

##### Encoder sampling rate

This parameter is only active in isochrone mode.

Any encoder sampling rate to be taken into account is set here. This allows slower encoders (such as ultrasound encoders) to be used, even with a fast processing cycle.

An integer reduction n is calculated using the set frequency. The encoder is then only read in again every nth clock cycle.

##### Example

- Processing cycle 500 μs
- Encoder sampling rate: 1.2 kHz (approximately every 833 µs)

This produces a reduction n = 2.

The encoder is only read in again every second processing cycle, in other words each millisecond.

### Control and feedback interface for standard mode (S7-300, S7-400)

This section contains information on the following topics:

- [Standard mode feedback interface (S7-300, S7-400)](#standard-mode-feedback-interface-s7-300-s7-400)
- [Standard mode feedback interface (S7-300, S7-400)](#standard-mode-feedback-interface-s7-300-s7-400-1)

#### Standard mode feedback interface (S7-300, S7-400)

> **Note**
>
> The following control interface data is consistent for 1SSI:
>
> - Bytes 0 to 3
> - Bytes 4 to 7

##### Control interface assignment

The table below shows the assignment of the 1SSI control interface (outputs) in standard mode.

| Address | Assignment |  | Name |
| --- | --- | --- | --- |
| Bytes 0 to 3 | Comparison value 1 or 2 (double word) |  |  |
| Byte 4 | Bit 7 | Error Acknowledgment | EXTF_ACK |
| Bit 6 | Acknowledgement latch function | LATCH_ACK |  |
| Bit 5 | Reserved = 0 |  |  |
| Bit 4 | Reserved = 0 |  |  |
| Bit 3 | Reserved = 0 |  |  |
| Bit 2 | Reserved = 0 |  |  |
| Bit 1 | Load comparison value 2 | CMP_VAL2 |  |
| Bit 0 | Load comparison value 1 | CMP_VAL1 |  |
| Byte 5 | Reserved = 0 |  |  |
| Bytes 6 to 7 | Reserved = 0 |  |  |

##### Notes on the control bits

| Bit | Explanation |
| --- | --- |
| CMP_VAL1 | Load comparison value 1 |
| CMP_VAL2 | Load comparison value 2 |
| EXTF_ACK | Error acknowledgement for the "Absolute encoder error" ERR_SSI and "Encoder supply short circuit" ERR_24V. |
| LATCH_ACK | Acknowledgement for latch function |

#### Standard mode feedback interface (S7-300, S7-400)

> **Note**
>
> The following feedback interface data is consistent for 1SSI:
>
> - Bytes 0 to 3
> - Bytes 4 to 7

##### Feedback interface assignment

The table below shows the assignment of the 1SSI feedback interface (inputs) in standard mode.

| Address | Assignment |  | Name |
| --- | --- | --- | --- |
| Bytes 0 to 3 | Encoder value (double word)  (bit 31 set, encoder value frozen) |  |  |
| Byte 4 | Bit 7 | Reserved = 0 or lifebeat | Lifebeat |
| Bit 6 | Ready | RDY |  |
| Bit 5 | Parameter assignment error | ERR_PARA |  |
| Bit 4 | Absolute encoder error | ERR_SSI |  |
| Bit 3 | Encoder supply short circuit | ERR_24V |  |
| Bit 2 | DI status | STS_DI |  |
| Bit 1 | Status DN | STS_DN |  |
| Bit 0 | Status UP | STS_UP |  |
| Byte 5 | Bit 7 | Reserved = 0 |  |
| Bit 6 | Reserved = 0 |  |  |
| Bit 5 | Reserved = 0 |  |  |
| Bit 4 | Reserved = 0 |  |  |
| Bit 3 | Comparison value 2 reached | CMP2 |  |
| Bit 2 | Comparison value 1 reached | CMP |  |
| Bit 1 | Load function error | ERR_LOAD |  |
| Bit 0 | Load function is running | STS_LOAD |  |
| Bytes 6 to 7 | Reserved = 0 |  |  |

##### Notes on the feedback bits

| Bit | Explanation |
| --- | --- |
| CMP | Comparison result of comparator 1 |
| CMP2 | Comparison result of comparator 2 |
| ERR_24V | There is a short circuit in the encoder supply. ERR_24V is reset when the short circuit is eliminated and acknowledged with the EXTF_ACK control bit. |
| ERR_LOAD | Error while loading the comparison values because both control bits CMP_VAL1 and CMP_VAL2 are set. |
| ERR_PARA | Incorrect parameter assignment for the ET 200S station.  Cause: Increments per encoder revolution not in the valid value range for the encoder type.  The parameter bit is cleared when correct parameter assignment is transmitted. |
| ERR_SSI | The 1SSI detects an "Absolute encoder error" if the frames at the SSI interface are interrupted.   Causes: No encoder connected; wire break in the encoder cable; encoder supply under-voltage; encoder type, transmission rate, monoflop time do not correspond to the connected encoder; programmable encoders do not correspond to the settings on the 1SSI; encoder is defective or faults or parity errors exist.  ERR_SSI is reset when the cause of the error is eliminated and acknowledged with the EXTF_ACK control bit. |
| Lifebeat | This parameter is only active in isochrone mode.  When lifebeat is on, the lifebeat bit is toggled each time an encoder value is read in in isochronous mode, i.e. the last value sent is inverted. If a reduction is assigned in the "Encoder Sampling Rate" parameter, the value is only toggled if an encoder value has actually been read in. |
| STS_DI | The bit displays the status of the digital input DI. |
| STS_DN | Status direction down; for encoder value change from larger to smaller encoder positions (including zero pass) |
| STS_LOAD | Feedback bit for CMP_VAL1 and CMP_VAL2. The 1SSI uses this bit to indicate that a comparison value is loaded. |
| STS_UP | Status direction down; for encoder value change from smaller to larger encoder positions (including zero pass) |
| RDY | 1SSI parameter assignment is correct, and the module is executing its functions. The feedback displayed is valid. For absolute value encoder errors, ERR_SSI is also set. |

### Fast mode parameters (S7-300, S7-400)

This section contains information on the following topics:

- [Enabling group diagnostics (S7-300, S7-400)](#enabling-group-diagnostics-s7-300-s7-400-1)
- [Selecting encoder value acquisition (S7-300, S7-400)](#selecting-encoder-value-acquisition-s7-300-s7-400-1)
- [Selecting encoder type (S7-300, S7-400)](#selecting-encoder-type-s7-300-s7-400-1)
- [Selecting Gray code/dual code converter (S7-300, S7-400)](#selecting-gray-codedual-code-converter-s7-300-s7-400-1)
- [Selecting the transmission rate (S7-300, S7-400)](#selecting-the-transmission-rate-s7-300-s7-400-1)
- [Selecting parity (S7-300, S7-400)](#selecting-parity-s7-300-s7-400-1)
- [Selecting monoflop time (S7-300, S7-400)](#selecting-monoflop-time-s7-300-s7-400-1)
- [Activating scaling (S7-300, S7-400)](#activating-scaling-s7-300-s7-400-1)
- [Entering number of adjusted bits (S7-300, S7-400)](#entering-number-of-adjusted-bits-s7-300-s7-400-1)
- [Enabling direction reversal (S7-300, S7-400)](#enabling-direction-reversal-s7-300-s7-400-1)
- [Entering increments per encoder revolution (S7-300, S7-400)](#entering-increments-per-encoder-revolution-s7-300-s7-400-1)
- [Enabling lifebeat (Fast mode) (S7-300, S7-400)](#enabling-lifebeat-fast-mode-s7-300-s7-400)
- [Setting the encoder sampling rate (S7-300, S7-400)](#setting-the-encoder-sampling-rate-s7-300-s7-400-1)

#### Enabling group diagnostics (S7-300, S7-400)

##### Group diagnostics

Channel-specific diagnostics will be carried out if you enable group diagnostics in your parameter assignment.

#### Selecting encoder value acquisition (S7-300, S7-400)

##### Description

The absolute encoder transfers its encoder values in frames to the 1SSI. The transmission of frames is initiated by the 1SSI. The following alternatives are available for encoder value acquisition:

- freewheeling encoder value acquisition
- synchronous encoder value acquisition
- Isochrone encoder value acquisition

You can set freewheeling or synchronous encoder value acquisition with the "Detection" parameter in parameter assignment. This parameter only works in non-isochrone mode.

Encoder value acquisition will be isochrone when the 1SSI is operating in isochrones mode. In this case, the "Detection" parameter is not evaluated.

The following table sets out these encoder value acquisition conditions.

| Operation | "Detection" parameter | Encoder value acquisition |
| --- | --- | --- |
| Non-isochrone mode | freewheeling | freewheeling encoder value acquisition |
| Synchronous | synchronous encoder value acquisition |  |
| Isochrone mode | - (irrelevant) | Isochrone encoder value acquisition |

##### Cyclic encoder value acquisition

The 1SSI initiates the transmission of a frame each time the parameterized [monoflop time](#selecting-monoflop-time-s7-300-s7-400-1) elapses.

The 1SSI processes the acquired encoder value asynchronously to these freewheeling frames in the update rate cycle.

Freewheeling acquisition therefore returns encoder values of different ages. The difference between the maximum and minimum age is the jitter.

##### Synchronous encoder value acquisition

Synchronous encoder value acquisition gives you maximum accuracy.

The 1SSI initiates the transmission of a frame in the cycle of its update rate.

The 1SSI processes the transferred encoder value synchronously with its update rate.

##### Isochrone encoder value acquisition

Isochrone encoder value acquisition is automatically set if the bus system and I/O modules are synchronized.

The 1SSI initiates the transmission of a frame in each bus cycle at time T<sub>i</sub> as long as the configured maximum encoder sampling rate does not result in a reduction.

The 1SSI processes the transmitted encoder value isochronously to the bus cycle.

#### Selecting encoder type (S7-300, S7-400)

##### Encoder type

The 1SSI supports the following encoder types:

- Absolute encoder (SSI) with 13 bits

  to
- Absolute encoder (SSI) with 25 bits

You will find the encoder type in the technical specifications for your absolute encoder.

Selecting "No encoder" deactivates the encoder input.

#### Selecting Gray code/dual code converter (S7-300, S7-400)

##### Gray code/dual code converter

The "[Gray code/dual code converter](Motion%20Control%20%28S7-300%2C%20S7-400%29%20%28TFMCMain3_400enUS%29.md#graydual-converter-s7-300-s7-400)" parameter defines how the codes returned by the encoder are processed:

- When "Gray code" is set, the encoder value returned by the absolute encoder in gray code will be converted to dual code.
- When "Dual code" is set, the values returned by the encoder will remain unchanged.

#### Selecting the transmission rate (S7-300, S7-400)

##### Transmission rate

You define the data transmission rate between the SSI encoder and the 1SSI with the "transmission rate".

Select the desired transmission rate in the drop-down box.

Note that the transmission rate affects how accurate and up-to-date the encoder values are.

The maximum transmission rate depends on the cable length:

- 320 m → 125 kHz
- 160 m → 250 kHz
- 60 m → 500 kHz
- 20 m → 1 MHz
- 10 m → 1.5 MHz
- 8 m → 2 MHz

---

**See also**

[Selecting monoflop time (S7-300, S7-400)](#selecting-monoflop-time-s7-300-s7-400-1)

#### Selecting parity (S7-300, S7-400)

##### Parity

"Parity" allows you to specify whether no parity, even parity or odd parity is to be assigned for an absolute encoder.

A configured parity bit is not included in the "[Encoder Type](#selecting-encoder-type-s7-300-s7-400-1)" parameter. If a 25-bit encoder with parity is parameterized, the encoder will read 26 bits.

The bit following the LSB (least significant bit) of the encoder is evaluated as a parity bit. A parity error is reported in the [feedback interface](#fast-mode-feedback-interface-s7-300-s7-400) via the bit EXTF.

#### Selecting monoflop time (S7-300, S7-400)

##### Monoflop time

The monoflop time represents the interval between two SSI frames.

The parameterized monoflop time must be greater than the monoflop time of the absolute encoder used (refer to the technical specifications of the manufacturer).

The following restriction applies to the monoflop time of the absolute encoder:

(1/transmission rate) &lt; monoflop time of absolute encoder &lt; 64 µs

Select the desired monoflop time in the drop-down box.

The specification of the monoflop time is relevant for [freewheeling encoder value acquisition](#selecting-encoder-value-acquisition-s7-300-s7-400-1).

---

**See also**

[Selecting the transmission rate (S7-300, S7-400)](#selecting-the-transmission-rate-s7-300-s7-400-1)

#### Activating scaling (S7-300, S7-400)

##### Encoder value and scaling

The encoder value transferred contains the encoder position of the absolute encoder. In addition to the encoder position, the encoder transfers additional bits located before and after the encoder position, depending on the encoder used.

The 1SSI requires the following information to allow it to detect the encoder position:

- [Encoder type](#selecting-encoder-type-s7-300-s7-400-1)
- [Number of adjusted bits](#entering-number-of-adjusted-bits-s7-300-s7-400-1)
- [Increments per encoder revolution](#entering-increments-per-encoder-revolution-s7-300-s7-400-1)

[Scaling](Motion%20Control%20%28S7-300%2C%20S7-400%29%20%28TFMCMain3_400enUS%29.md#encoder-value-and-scaling-s7-300-s7-400) specifies presentation of the encoder value at the [feedback interface](#fast-mode-feedback-interface-s7-300-s7-400).

- "Scaling **on**" specifies that trailing, irrelevant bits in the encoder value are to be discounted.
- "Scaling **off**" specifies that adjusted bits are retained and are available for evaluation.

#### Entering number of adjusted bits (S7-300, S7-400)

##### Number of adjusted bits

The 1SSI requires the number of adjusted bits in order to detect the encoder position and correctly detect the encoder's direction of motion.

You will find this value in the technical specifications for your absolute encoder.

#### Enabling direction reversal (S7-300, S7-400)

##### Direction detection and direction reversal

The 1SSI needs the following information to detect the direction of movement of the encoder correctly:

- [Encoder type](#selecting-encoder-type-s7-300-s7-400-1)
- [Number of adjusted bits](#entering-number-of-adjusted-bits-s7-300-s7-400-1)
- [Increments per encoder revolution](#entering-increments-per-encoder-revolution-s7-300-s7-400-1)

The direction of motion determined is displayed in the [feedback interface](#fast-mode-feedback-interface-s7-300-s7-400) and by the LEDs.

- LED UP: Encoder position change from lower to higher value
- LED DN: Encoder position change from higher to lower value

**Direction reversal** adapts the encoder direction of motion to the axis.

Two settings are possible:

- **Off:** The direction of the transferred encoder position is maintained.
- **On:** The direction of the transferred encoder position is reversed. This means that although the encoder sends ascending values, descending values are displayed.

  The reversal relates to the increments/encoder revolution set in the parameters.

##### Example of Direction Reversal

Presettings:

You are using a single-turn encoder with 2<sup>10</sup> (corresponds to 10 bits) = 1024 increments/encoder revolution (resolution/360°) with the following parameter assignment:

- Encoder type: SSI-13 bit
- Number of adjusted bits: 3 places
- Direction reversal: On
- Increments per encoder revolution: 1024

Encoder value before direction reversal: cyclically recorded encoder position 1023

Encoder value after direction reversal: displayed encoder position 0

#### Entering increments per encoder revolution (S7-300, S7-400)

##### Increments per encoder revolution

The "Increments per encoder revolution" parameter defines the number of increments an encoder returns per revolution.

You will find this value in the technical specifications for your absolute encoder.

##### Valid value ranges

The limits depend on the individual encoder models. Only values to the power of 2 are permitted.

- 13-bit encoder type: 16 to 8192
- 14-bit encoder type: 16 to 16384
- 15-bit encoder type: 16 to 32768
- 16-bit encoder type: 16 to 65536
- 17-bit encoder type: 16 to 131072
- 18-bit encoder type: 16 to 262144
- 19-bit encoder type: 16 to 524288
- 20-bit encoder type: 16 to 1048576
- 21-bit encoder type: 16 to 2097152
- 22-bit encoder type: 16 to 4194304
- 23-bit encoder type: 16 to 8388608
- 24-bit encoder type: 16 to 16777216
- 25-bit encoder type: 16 to 33554432

#### Enabling lifebeat (Fast mode) (S7-300, S7-400)

##### Lifebeat

This parameter is only active in isochrone mode.

When lifebeat is activated, the lifebeat bit is toggled each time an encoder value is read in in isochronous mode, i.e. the last value sent is inverted. If a reduction is assigned in the "[Encoder sampling rate](#setting-the-encoder-sampling-rate-s7-300-s7-400-1)" parameter, the value is only toggled if an encoder value has actually been read in.

The lifebeat bit can be found in the [feedback interface](#fast-mode-feedback-interface-s7-300-s7-400) in bytes 0 to 3 / bit 31.

#### Setting the encoder sampling rate (S7-300, S7-400)

##### Encoder sampling rate

This parameter is only active in isochrone mode.

Any encoder sampling rate to be taken into account is set here. This allows slower encoders (such as ultrasound encoders) to be used, even with a fast processing cycle.

An integer reduction n is calculated using the set frequency. The encoder is then only read in again every nth clock cycle.

##### Example

- Processing cycle 500 μs
- Encoder sampling rate: 1.2 kHz (approximately every 833 µs)

This produces a reduction n = 2.

The encoder is only read in again every second processing cycle, in other words each millisecond.

### Fast mode feedback interface (S7-300, S7-400)

#### Feedback interface assignment

The table below shows the assignment of the 1SSI feedback interface (inputs) in fast mode.

| Address | Assignment |  | Name |
| --- | --- | --- | --- |
| Bytes 0 to 3 | Bit 31 | Reserved = 0 or lifebeat | Lifebeat |
| Bit 30 | Ready for operation (feedback is valid) | RDY |  |
| Bit 29 | Parameter assignment error | ERR_PARA |  |
| Bit 28 | Group error , absolute encoder or encoder supply short circuit | EXTF |  |
| Bit 27 | DI status | STS_DI |  |
| Bit 26 | Status DN | STS_DN |  |
| Bit 25 | Status UP | STS_UP |  |
| Bits 0 to 24 | Encoder value |  |  |

#### Notes on the feedback bits

| Bit | Explanation |
| --- | --- |
| ERR_PARA | Incorrect parameter assignment for the ET 200S station.  Cause: Increments per encoder revolution not in the valid value range for the encoder type.  The parameter bit is cleared when correct parameter assignment is transmitted. |
| EXTF | Group error absolute encoder or encoder supply short circuit  Causes:  - The encoder supply has short-circuited - No encoder connected; wire break in the encoder cable; encoder type, transmission rate, monoflop time do not correspond to the connected encoder; programmable encoders do not correspond to the settings on the 1SSI; encoder is defective or faults or parity errors exist.   EXTF is reset when the causes of the errors have been eliminated. |
| Lifebeat | This parameter is only active in isochrone mode.  When lifebeat is on, the lifebeat bit is toggled each time an encoder value is read in in isochronous mode, i.e. the last value sent is inverted. If a reduction is assigned in the "Encoder Sampling Rate" parameter, the value is only toggled if an encoder value has actually been read in. |
| STS_DI | The bit displays the status of the digital input DI. |
| STS_DN | Status direction down; for encoder value change from larger to smaller encoder positions (including zero pass) |
| STS_UP | Status direction down; for encoder value change from smaller to larger encoder positions (including zero pass) |
| RDY | 1SSI parameter assignment is correct, and the module is executing its functions. The feedback displayed is valid. For absolute value encoder errors, EXTF is also set. |

## Diagnostics of the 1SSI (S7-300, S7-400)

This section contains information on the following topics:

- [Diagnostics using the LED display (S7-300, S7-400)](#diagnostics-using-the-led-display-s7-300-s7-400)
- [Error types (S7-300, S7-400)](#error-types-s7-300-s7-400)

### Diagnostics using the LED display (S7-300, S7-400)

#### LED display on the 1SSI

![LED display on the 1SSI](images/23263845387_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Group error (red) |
| ② | Status display for change in sensor value (green) |
| ③ | Status display for result of comparison |
| ④ | Status display for digital input (green) |

#### Status and error displays by means of LEDs on the 1SSI

The table below shows the status and error displays on the 1SSI.

| Event (LED) |  |  |  |  | Cause | Remedy |
| --- | --- | --- | --- | --- | --- | --- |
| SF | UP | DN | CMP | 7 |  |  |
| On |  |  |  |  | No parameter assignment. There is a diagnostic message. | Check the parameter assignment. Evaluate the diagnostics data. |
|  | On |  |  |  | At value change from smaller to larger sensor values (including zero-crossing) |  |
|  |  | On |  |  | At value change from larger to smaller sensor values (including zero-crossing) |  |
|  |  |  | On |  | Set for comparison result CMP 1 |  |
|  |  |  |  | On | DI (latch) is activated. |  |

### Error types (S7-300, S7-400)

For information on the structure of the channel-related diagnostics, refer to the manual on the interface module used in your ET 200S station.

#### 1SSI error types

The following table shows the error types on the 1SSI.

| Error class |  | Meaning | Remedy |
| --- | --- | --- | --- |
| 1<sub>D</sub> | 00001:  Short circuit | Short circuit of the supply to the absolute encoder. | Correct the process wiring. |
| 9<sub>D</sub> | 01001:  Error | Internal module error occurred. | Replace the module. |
| Load voltage from the power module is too low. | Correct the process wiring. Check the load voltage. |  |  |
| 16<sub>D</sub> | 10000:  Parameter assignment error | Parameters have not been assigned to the module. | Correct the parameter assignment. |
| 26<sub>D</sub> | 11010:  External error | Start/Stop bit error (error absolute value encoder)  Wire break in the encoder cable or encoder cable is not connected.  Encoder type, transmission rate, monoflop time do not correspond to the connected encoder  Programmable encoders do not correspond to the settings on the 1SSI  Sensor is defective or there are faults. | Replace the encoder  Correct the process wiring  Correct the parameter assignment. |

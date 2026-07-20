---
title: "Counting and measuring (S7-300, S7-400)"
package: TFCountMainenUS
topics: 32
devices: [S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Counting and measuring (S7-300, S7-400)

This section contains information on the following topics:

- [Counting and measuring basics (S7-300, S7-400)](#counting-and-measuring-basics-s7-300-s7-400)
- [Using FM 350-1 (S7-300, S7-400)](Using%20FM%20350-1%20%28S7-300%2C%20S7-400%29.md#using-fm-350-1-s7-300-s7-400)
- [Using FM 350-2 (S7-300, S7-400)](Using%20FM%20350-2%20%28S7-300%2C%20S7-400%29.md#using-fm-350-2-s7-300-s7-400)
- [Using FM 450-1 (S7-300, S7-400)](Using%20FM%20450-1%20%28S7-300%2C%20S7-400%29.md#using-fm-450-1-s7-300-s7-400)
- [Using ET 200S 1Count24V (S7-300, S7-400)](Using%20ET%20200S%201Count24V%20%28S7-300%2C%20S7-400%29.md#using-et-200s-1count24v-s7-300-s7-400)
- [Using ET 200S 1Count5V (S7-300, S7-400)](Using%20ET%20200S%201Count5V%20%28S7-300%2C%20S7-400%29.md#using-et-200s-1count5v-s7-300-s7-400)
- [Using ET 200S 2PULSE (S7-300, S7-400)](Using%20ET%20200S%202PULSE%20%28S7-300%2C%20S7-400%29.md#using-et-200s-2pulse-s7-300-s7-400)

## Counting and measuring basics (S7-300, S7-400)

This section contains information on the following topics:

- [What is counting and measuring? (S7-300, S7-400)](#what-is-counting-and-measuring-s7-300-s7-400)
- [Counting basics (S7-300, S7-400)](#counting-basics-s7-300-s7-400)
- [Count modes (S7-300, S7-400)](#count-modes-s7-300-s7-400)
- [Main count direction (S7-300, S7-400)](#main-count-direction-s7-300-s7-400)
- [Measuring basics (S7-300, S7-400)](#measuring-basics-s7-300-s7-400)
- [Measuring modes (S7-300, S7-400)](#measuring-modes-s7-300-s7-400)
- [Dosing (only for FM 350-2) (S7-300, S7-400)](#dosing-only-for-fm-350-2-s7-300-s7-400)
- [Gate control (S7-300, S7-400)](#gate-control-s7-300-s7-400)
- [Encoder signals (S7-300, S7-400)](#encoder-signals-s7-300-s7-400)
- [Signal evaluation (S7-300, S7-400)](#signal-evaluation-s7-300-s7-400)

### What is counting and measuring? (S7-300, S7-400)

#### Counting and measuring

Counting is the capturing and totalizing of events. The counter modules detect and analyze encoder signals (pulses).

The pulses are detected in real time in measuring modes and used to calculate the relevant measured values (e.g. frequency).

### Counting basics (S7-300, S7-400)

#### Counting ranges and count limits

The module counts within various counting limits in the two counting ranges "0 to +32 bits" and "-31 to +31 bits". An high limit violated or an low limit violated is detected at the respective count limits.

In the "-31 to +31 bits" counting range, the counter value is represented in 2's complement.

| Counting range |  | High limit violated | Low limit violated |
| --- | --- | --- | --- |
| 0 to +32 bits <sup>1)</sup> | 0 to 4,294,967,295  0 to FFFF FFFFH | When the counter value changes from 4 294 967 295 to 0 | When the counter value changes from 0 to 4 294 967 295 |
| -31 to +31 bits | -2,147,483,648 to 2,147,483,647  8000 0000H to 7FFF FFFFH | When the counter value changes from +2 147 483 647 to  –2 147 483 648 | When the counter value changes from -2,147,483,648 to 2,147,483,647 |
| <sup>1)</sup> This counting range is only available with FM x50‑1. You can only specify and evaluate hexadecimal values. |  |  |  |

#### Load value

The load value is the counter value from which the module starts the counting process.

You can assign a load value LOAD_VAL to the module during operation. This will overwrite the initial value.

You can assign this load value **directly**. It will then be accepted directly by the module as a new counter value and loaded in preparation.

You can only load the load value **in preparation**. A load value loaded in preparation is accepted by the module as the new counter value in response to the following events:

- In all Count modes

  - The counting process is started by the interrupting software or hardware gate (the counter continues counting from the current counter value when the software or hardware gate is started if the interrupting gate function is activated; the load value is not applied).
  - Synchronization (via corresponding DI)
  - Latch/Retrigger (via corresponding DI)
- In the "Count once" and " Count periodically" modes also:

  - When the set high count limit is reached for main counting direction up.
  - Reaching 0 when counting down.

#### Gate control

You can use the hardware gate and software gate to control i.e. start and stop the module's counting processes.

#### Main counting direction

When you set a main counting direction (up or down), you can limit the maximum count range to a smaller range by setting the high count limit. The set count range is then between 0 and the set high count limit. This can be used to create incrementing or decrementing counting applications, for example. The set main counting direction has no effect on the direction evaluation when the count pulses are detected.

#### Starting Counts According to Parameterization

| Value | Main counting direction | Start value |
| --- | --- | --- |
| Load value | None  Up  Down | 0  0  Parameterized high count limit |
| Count value | None  Up  Down | 0  0  Parameterized high count limit |
| Comparison value 1 and 2 | None  Up  Down | 0  0  Parameterized high count limit |
| Latch value | None  Up  Down | 0  0  Parameterized high count limit |

#### Commands for the Counting Modes

You can apply commands to the module counting process during operation:

| Command | Description |
| --- | --- |
| Open and close gate | The counting process starts when a gate opens and ends when it closes. |
| Set counter <sup>1</sup>) | The counter will be set to the load value via various signals (DI, zero mark). |
| Latch/Retrigger <sup>2)</sup> | Saves the counter level and loads the counter with the load value in response to a positive edge at DI Start. |
| Latching <sup>2)</sup> | Saves the counter level in response to a positive edge at DI.Start. |
| Measuring times between two edges<sup>3)</sup> | Measures the times between two immediately successive edges at the DI Start digital input. |
| <sup>1)</sup> only with FM 350‑1 and FM 450‑1   <sup>2)</sup> only with FM 350‑1, ET 200S 1Count24V and ET 200S 1Count5V   <sup>3)</sup> only with FM 350‑1 |  |

#### Isochronous mode

In isochrone mode, the module accepts control bits and control values from the control interface in each PROFIBUS / PROFINET cycle and returns its response to them within the same cycle.

In each PROFIBUS / PROFINET cycle, the module transfers the counter and latch value that were valid at time T<sub>i</sub> and the status bits valid at time T<sub>i</sub>.

A counter value influenced by hardware input signals will only be transferred in the same cycle if the input signal occurs before time T<sub>i</sub>.

### Count modes (S7-300, S7-400)

This section contains information on the following topics:

- [Overview of the count modes (S7-300, S7-400)](#overview-of-the-count-modes-s7-300-s7-400)
- [Count continuously (S7-300, S7-400)](#count-continuously-s7-300-s7-400)
- [Count once (S7-300, S7-400)](#count-once-s7-300-s7-400)
- [Count periodically (S7-300, S7-400)](#count-periodically-s7-300-s7-400)

#### Overview of the count modes (S7-300, S7-400)

You select module functionality by setting a default operating mode. The table below gives an overview of the counting modes.

| Operating mode | Description |
| --- | --- |
| [Count continuously](#count-continuously-s7-300-s7-400)  (with or without software or hardware gate) | The module counts continuously from the current counter value. |
| [Count once](#count-once-s7-300-s7-400)  (with software gate or hardware gate) | When the gate opens, the module counts from the load value to the count limit. |
| [Count periodically](#count-periodically-s7-300-s7-400)  (with software gate or hardware gate) | When the gate opens, the module counts between the load value and the count limit. |

#### Count continuously (S7-300, S7-400)

##### Description

In this operating mode, the module counts continuously from the counter value:

- If the counter reaches the high limit when counting up and a further count pulse is received, it jumps to the low count limit and continues to count from there without any pulse losses.
- If the counter reaches the low limit when counting down and a further count pulse is received, it jumps to the high limit and continues to count from there without any pulse losses.

The following applies to the ±31 bit counting range:

- The high count limit is set to +2,147,483,647 (2<sup>31</sup> - 1).
- The low count limit is set to -2,147,483,648 (-2<sup>31</sup>).

The following applies to the 32 bit counting range:

- The high count limit is set at +4,294,967,295 (2<sup>32</sup> - 1).
- The low count limit is set to 0 (zero).

##### Behavior at the Count Limits

If the counter reaches the high or low count limit and a further count pulse is received, then the counter is set to the other count limit. An appropriate status bit is set in the feedback interface and if applicable in the DB:

| Count limit reached | Status bit |
| --- | --- |
| High count limit | STS_OFLW is set |
| Low count limit | STS_UFLW is set |

##### Selecting gate control

This mode allows you to select gate control. The following options are available to you:

- Without gate (default)
- [Software gate](#software-gate-s7-300-s7-400)
- [Hardware gate](#hardware-gate-s7-300-s7-400), level-controlled or edge-controlled

The figure below shows an example of continuous counting with gate control.

![Selecting gate control](images/17705365899_DV_resource.Stream@PNG-en-US.png)

#### Count once (S7-300, S7-400)

##### Description

In this operating mode, the module counts once in the parameterized main counting direction and then stops the counting process automatically.

##### Behavior at the Count Limits

If the counter has reached the high or low count limit and a further count pulse is received, the counter is set

- to the other count limit when [counting without a main count direction](#main-count-direction-s7-300-s7-400)
- to the load value when [counting with a main count direction](#main-count-direction-s7-300-s7-400).

The gate is then closed and the counting process terminated, even if the parameter / the control bitSW_GATE is still set or the hardware gate is still open. The appropriate status bit is set in the feedback interface / in the DB:

| Count limit reached | Status bit |
| --- | --- |
| High count limit | STS_OFLW is set |
| Low count limit | STS_UFLW is set |

If you want to restart the counter, you must reset the parameter / the control bit SW_GATE and/or reopen the hardware gate. The counting process is then continued from the load value.

##### Selecting gate control

This mode allows you to select gate control. The following options are available to you:

- [Software gate](#software-gate-s7-300-s7-400)
- [Hardware gate](#hardware-gate-s7-300-s7-400), level-controlled or edge-controlled

The figure below shows an example of continuous counting with load value and gate control.

![Selecting gate control](images/24575485067_DV_resource.Stream@PNG-en-US.png)

#### Count periodically (S7-300, S7-400)

##### Description

In this operating mode, the module counts periodically when the gate is open and does not stop counting at the count limits.

##### Behavior at the Count Limits

If the counter

- has reached one of the count limits when [counting without a main count direction](#main-count-direction-s7-300-s7-400)
- has reached the high count limit when [counting with the main count direction up](#main-count-direction-s7-300-s7-400)
- has reached the low count limit when [counting with main count direction down](#main-count-direction-s7-300-s7-400)

The gate is then closed and the count is terminated even if the SW_GATE parameter is still set or the hardware gate is still open. The appropriate status bit is set in the feedback interface / in the DB.

| Count limit reached | Status bit |
| --- | --- |
| High count limit | STS_OFLW is set |
| Low count limit | STS_UFLW is set |

##### Selecting gate control

This mode allows you to select gate control. The following options are available to you:

- [Software gate](#software-gate-s7-300-s7-400)
- [Hardware gate](#hardware-gate-s7-300-s7-400), level-controlled or edge-controlled

The figure below shows an example of count periodically with load value and gate control.

![Selecting gate control](images/17756529803_DV_resource.Stream@PNG-en-US.png)

### Main count direction (S7-300, S7-400)

A main count direction can only be selected in the "Count once", " Count periodically" and "Dosing" modes.

You can parameterize the following behavior:

- None (no main count direction)
- Up
- Down

#### Count once without main count direction

When the gate is opened in "Count once" mode without a main count direction, the module will count up or down from the load value until one of the count limits is exceeded.

If one of the count limits is exceeded,

- the gate is closed,
- the STS_OFLW or STS_UFLW bit is set in the feedback interface,
- the counter is set to the other count limit.

The count limits are fixed at the maximum count range.

The STS_ZERO and/or STS_ND bit is set if the counter value is zero (not in FM 350‑2).

You must open the gate again to restart the count.

#### Count Periodically without Main Counting Direction

When the gate is opened in " Count periodically" mode without a main count direction, the module counts up or down from the load value until one of the count limits is exceeded.

If one of the count limits is exceeded

- the STS_OFLW or STS_UFLW bit is set in the feedback interface,
- the counter is set to the load value from which it resumes counting.

The count limits are fixed at the maximum count range.

The STS_ZERO and/or STS_ND bit is set if the counter value is zero (not in FM 350‑2).

The counting is resumed when the gate is closed.

#### Count once with main count direction up

When the gate is opened in "Count once" or "Dosing" mode with the main count direction up, the module counts up or down from the load value until the high count limit is exceeded.

If the high count limit is exceeded,

- the gate is closed,
- the STS_OFLW bit in the feedback interface is set,
- the counter is set to the load value.

The high count limit can be set. The load value has a starting count and can be changed.

You must open the gate again to restart the count.

#### Count Periodically with Main Counting Direction Up

When the gate is opened in " Count periodically" mode with main count direction up, the module counts up or down from the load value until the high count limit is exceeded.

If the high count limit is exceeded,

- the STS_OFLW bit in the feedback interface is set,
- the counter is set to the load value from which it resumes counting.

The high count limit can be set. The load value has a starting count and can be changed.

The counting is resumed when the gate is closed.

#### Count once with main count direction down

When the gate is opened in "Count once" or "Dosing" mode with main count direction down, the module counts up or down from the load value until the low count limit is violated.

If the low count limit is under-run,

- the gate is closed,
- the STS_UFLW bit in the feedback interface is set,
- the counter is set to the load value.

The low count limit is fixed at 0; the load value has an initial value and can be changed.

You must open the gate again to restart the count.

#### Count Periodically with Main Counting Direction Down

When the gate is opened in " Count periodically" mode with main count direction down, the module counts up or down from the load value until the low count limit is violated.

If the low count limit is under-run,

- the STS_UFLW bit in the feedback interface is set,
- the counter is set to the load value from which it resumes counting.

The low count limit is fixed at 0; the load value has an initial value and can be changed.

The counting is resumed when the gate is closed.

### Measuring basics (S7-300, S7-400)

#### Measuring ranges

The modules have the following measuring ranges in measuring modes:

| Operating mode | Measuring range |
| --- | --- |
| Frequency measurement | 0.1 Hz <sup>1)</sup> to 650 000 Hz (depending on the module) |
| Rotational speed measurement | Up to 25,000 /min |
| Period measurement | Up to 120 s |
| <sup>1)</sup> The low limit of 0.1 Hz is defined by the maximum update time of 10 s. The resolution of the value is 0.001 Hz. |  |

#### Update time / Integration time

The module updates the measured values cyclically. Set the "Measuring time" parameter as factor n to calculate the update time / integration time.

Calculation of the update time / integration time:

| Boundary conditions |  | Update time / Integration time | Value range of n |  |
| --- | --- | --- | --- | --- |
| n<sub>min</sub> | n<sub>max</sub> |  |  |  |
| Non-isochronous mode | Any T<sub>DP</sub> | n × 10 ms | 1 | 1000 <sup>3)</sup> |
| Isochronous mode <sup>2)</sup> | T<sub>DP</sub> < 10 ms | n × T<sub>DP</sub> | ( 10 ms/T<sub>DP</sub> [ms] ) + 1 <sup>1)</sup> | 1000 <sup>3)</sup> |
| T<sub>DP</sub> ≥ 10 ms | n x T<sub>DP</sub> | 1 | 10000 <sup>3)</sup> ms/T<sub>DP</sub> [ms] <sup>1)</sup> |  |
| <sup>1</sup> Any decimal places that result from dividing by T<sub>DP</sub> are omitted.  It is prohibited to exceed these limits. If these limits are violated, the module will generate a parameter assignment error and will not go into isochrone mode.   <sup>2)</sup> not with FM 350‑2   <sup>3)</sup> for period measurement: 120000 |  |  |  |  |

The measured value is updated in the feedback interface and the STS_CMP1 or STS_COMP1 bit is set at the end of update time / integration time.

#### Measuring principle

The module counts each positive edge of a pulse and allocates it a time value in μs.

The dynamic measuring time is defined as the difference between two time values.

At a pulse sequence with one or several pulses per update interval:

| Symbol | Meaning |
| --- | --- |
| Dynamic measuring time = | Time value of last pulse in the current update time interval   minus  time value of the last pulse in the previous update interval |

If no pulses are received within the next update intervals after the dynamic measuring time is calculated, the measuring time is extended by these update intervals. In this case, a pulse is assumed at the end of the update time and the measuring interval is calculated as the time between that point and the last pulse which occurred. The number of pulses is then 1. If the value "1 pulse per dynamic measuring time" is less than the last measured value, it will be output as the new value. The figure below shows the measuring principle.

![Measuring principle](images/18975367051_DV_resource.Stream@PNG-en-US.png)

#### Measurement sequence

The module measures continuously. You define a specific update time in the parameter settings.

The module returns the value "-1" until the first update time has expired. The first update time starts when the gate has opened.

When the gate has opened, continuous measurement starts at the first pulse of the pulse sequence to measure. The first measured value can be calculated after the second pulse at the earliest.

On each expiration of the update time, a measured value is output at the checkback interface (frequency, period or rpm.) The end of measurement is reported at the STS_CMP1 or STS_COMP1 (for FM 350‑2) status bits. This bit is reset by the RES_ZERO and STS_RES_ZERO or RES_STS and RES_STS_A bits by applying the complete acknowledgement principle.

If the direction of rotation is reversed during an update time, the measured value for this measurement period will be undefined. You can respond to any irregularities in the process by evaluating the feedback bits for direction.

The following figure illustrates the principle of continuous measurement taking frequency measurement as an example.

![Measurement sequence](images/18975426187_DV_resource.Stream@PNG-en-US.png)

#### Limit Monitoring

The limit values must meet each of the following conditions:

- Low limit value ≥ low measuring range limit
- High limit value ≥ high measuring range limit
- High limit value ≥ (low limit value + 1)

Upon expiry of the update time, the module compares the measured value (frequency, speed or period) with the low and high limit values parameterized. The result of the comparison is as follows.

| If the measured value... | ...the following bit will be set in the status: |
| --- | --- |
| is greater than the high limit value | STS_OFLW |
| is smaller than the low limit value | STS_UFLW |

A hardware interrupt may also be generated.

The image below shows the value of the status bits for limit monitoring in measuring modes.

![Limit Monitoring](images/18975446923_DV_resource.Stream@PNG-en-US.png)

Reset the STS_OFLW and STS_UFLW bits by setting the RES_ZERO and STS_RES_ZERO or RES_STS bits by applying the complete acknowledgement principle. The module sets the status bits again if it detects high limit violated of the measured value after the acknowledgement bits were set.

If parameters are assigned accordingly, you also can use limit monitoring to set output DOn.

#### Gate control

You can use the hardware gate and software gate to control i.e. start and stop the module's measuring processes.

#### Commands in the measuring modes

You can apply commands to the module measuring process during operation:

| Designation | Description |
| --- | --- |
| Open and close gate | You start the measurement by opening a gate, and stop it by closing this gate. |

#### Isochronous mode

When operating in isochrone mode, the module accepts the control signals output by the control interface at time T<sub>o</sub> in each PROFIBUS / PROFINET cycle. As a result, all control operations are executed in isochronous mode and take effect at the time T<sub>o</sub>. The response to the control signals is reported within the same PROFIBUS / PROFINET cycle.

The module returns a measured value and the status bits at time T<sub>i</sub> in each PROFIBUS / PROFINET cycle<sub>.</sub>

Each measurement starts and ends at the time T<sub>i</sub>.

> **Note**
>
> As you define the update time as an integer multiple of 10 ms for operation in non-isochrone mode and in integer multiples of the bus cycle time for operation in isochrone mode, you should also always adapt the update time parameter when you toggle these modes if you wish to retain the actual update time.

### Measuring modes (S7-300, S7-400)

This section contains information on the following topics:

- [Overview of measuring modes (S7-300, S7-400)](#overview-of-measuring-modes-s7-300-s7-400)
- [Frequency measurement (S7-300, S7-400)](#frequency-measurement-s7-300-s7-400)
- [Rotational speed measurement (S7-300, S7-400)](#rotational-speed-measurement-s7-300-s7-400)
- [Period measurement (S7-300, S7-400)](#period-measurement-s7-300-s7-400)

#### Overview of measuring modes (S7-300, S7-400)

You select module functionality by setting a default operating mode. The table below gives an overview of measuring modes.

| Operating mode | Description |
| --- | --- |
| [Frequency measurement](#frequency-measurement-s7-300-s7-400) | The module counts the pulses it receives within a dynamic measuring time <sup>1)</sup> and uses them to calculate the frequency. |
| [Rotational speed measurement](#rotational-speed-measurement-s7-300-s7-400) | The module counts pulses received from a tachometer generator within a dynamic measuring time <sup>1)</sup> and calculates the velocity based on this value and the number of pulses per encoder revolution. |
| [Period measurement](#period-measurement-s7-300-s7-400) | The module displays the dynamic measuring time <sup>1)</sup> as a period. If the period is less than the update time, a mean value is calculated for the period. |
| <sup>1)</sup> Dynamic measuring time means: if no 2 edges are detected by the measuring signal before the end of the parameterized measuring time, an estimated measured value will be calculated with the dynamic measuring time. It is assumed that a pulse was sent at the end of the update time. This gives you a constant measured value. |  |

> **Note**
>
> FM 450‑1 does not support any measuring modes.

#### Frequency measurement (S7-300, S7-400)

##### Description

In this operating mode, the module counts the pulses it receives within a dynamic measuring time or a specified integration time. The frequency is then calculated with the edge time stamps.

##### Selecting gate control

This mode allows you to select gate control. The following options are available to you:

- [Software gate](#software-gate-s7-300-s7-400)
- [Hardware gate](#hardware-gate-s7-300-s7-400), level-controlled or edge-controlled

The figure below shows an example of frequency measurement with gate control.

![Selecting gate control](images/17756956043_DV_resource.Stream@PNG-en-US.png)

##### Possible Measuring Ranges with Error Indication

The table below sets out the measuring ranges and absolute errors for continuous frequency measurements.

| Frequency f | Absolute error |  |
| --- | --- | --- |
| FM 350‑1 ET 200S 1Count5V | ET 200S 1Count24V |  |
| 0.1 Hz | ± 0.001 Hz |  |
| 1 Hz | ± 0.001 Hz |  |
| 10 Hz | ± 0.003 Hz |  |
| 100 Hz | ± 0.02 Hz |  |
| 1,000 Hz | ± 0.18 Hz |  |
| 10,000 Hz | ± 1.8 Hz |  |
| 100,000 Hz | ± 18 Hz |  |
| 500,000 Hz | ± 90 Hz | – |

The table below sets out the measuring ranges and absolute errors for continuous frequency measurements with integration time.

| Integration time | f<sub>min</sub> ± absolute error | f<sub>max</sub> ± absolute error |  |
| --- | --- | --- | --- |
| ET 200S 1Count24V | ET 200S 1Count5V |  |  |
| 10 s | 0.1 Hz ± 0.001 Hz | 100,000 Hz ± 18 Hz | 500,000 Hz ± 90 Hz |
| 1 s | 1 Hz ± 0.001 Hz | 100,000 Hz ± 11 Hz | 500,000 Hz ± 55 Hz |
| 0.1 s | 10 Hz ± 0.002 Hz | 100,000 Hz ± 10 Hz | 500,000 Hz ± 52 Hz |
| 0.01 s | 100 Hz ± 0.013 Hz | 100,000 Hz ± 13 Hz | 500,000 Hz ± 63 Hz |

##### Values that can be changed during operation

The following values can be changed during operation:

- Low limit
- High limit
- Update time (measuring time) <sup>1)</sup>
- Function of the digital output  <sup>1)</sup>

<sup>1)</sup> not with FM 350‑2

##### Result

The end of a frequency measurement is reported at the STS_CMP1 or STS_COMP1 (for FM 350‑2) status bit. The value of the calculated frequency is displayed in units of 10<sup>-3</sup> Hz. You can read the frequency value measured from the feedback interface.

#### Rotational speed measurement (S7-300, S7-400)

##### Description

In this operating mode, the module counts the pulses it receives from a tachometer generator within a dynamic measuring time or a specified integration time and measures the time interval between the edges. On this basis it then calculates the velocity with the pulses per encoder revolution.

For "Rotational speed measurement" mode, you must also assign the pulses per encoder revolution.

##### Selecting gate control

This mode allows you to select gate control. The following options are available to you:

- [Software gate](#software-gate-s7-300-s7-400)
- [Hardware gate](#hardware-gate-s7-300-s7-400), level-controlled or edge-controlled

The figure below shows an example of rotational speed measurement with gate control.

![Selecting gate control](images/17803178507_DV_resource.Stream@PNG-en-US.png)

##### Possible measuring ranges with error indication

The table below sets out the measuring ranges and absolute errors for continuous rotational speed measurement when the number of pulses per encoder rotation = 60.

| Speed n | Absolute error |
| --- | --- |
| 1 /min | ± 0.04 /min |
| 10 /min | ± 0.04 /min |
| 100 /min | ± 0.05 /min |
| 1,000 /min | ± 0.21 /min |
| 10,000 /min | ± 1.82 /min |
| 25,000 /min | ± 4.50 /min |

The table below sets out the measuring ranges and absolute errors for rotational speed measurement with integration time when the number of pulses per encoder rotation = 60.

| Integration time | n<sub>min</sub> ± absolute error | n<sub>max</sub> ± absolute error |
| --- | --- | --- |
| 10 s | 1 /min ± 0.03 /min | 25000 /min ± 4.5 /min |
| 1 s | 1 /min ± 0.03 /min | 25000 /min ± 2.8 /min |
| 0.1 s | 10 /min ± 0.03 /min | 25000 /min ± 2.6 /min |
| 0.01 s | 100 /min ± 0.04 /min | 25000 /min ± 3.2 /min |

##### Values that can be changed during operation

The following values can be changed during operation:

- Low limit
- High limit
- Update time (measuring time) <sup>1)</sup>
- Function of the digital output  <sup>1)</sup>

<sup>1)</sup> not with FM 350‑2

##### Result

The end of a rotational speed measurement is reported at the STS_CMP1 or STS_COMP1 (for FM 350‑2) status bit. The value of the velocity calculated is displayed in 10<sup>-3</sup> /min. You can read the velocity measured from the feedback interface.

#### Period measurement (S7-300, S7-400)

##### Description

In this operating mode, the module indicates the dynamic measuring time as a period. If the period is less than the update time, a mean value is calculated for the period.

In "Period measurement with integration time" mode, 1Count24V measures the time between two positive edges of the count signal by counting the pulses of an internal quartz-accurate reference frequency (16 MHz) within a specified integration time.

##### Selecting gate control

This mode allows you to select gate control. The following options are available to you:

- [Software gate](#software-gate-s7-300-s7-400)
- [Hardware gate](#hardware-gate-s7-300-s7-400), level-controlled or edge-controlled

The figure below shows an example of period measurement with gate control.

![Selecting gate control](images/17809479179_DV_resource.Stream@PNG-en-US.png)

##### Possible measuring ranges with error indication

Continuous period measurement:

- The absolute error for continuous period measurement with a **resolution of 1 µs** is equal to 0.1‰ of the measured value.
- The table below sets out the measuring ranges and absolute error for continuous period measurements with a **resolution of 1/16 µs**.

  Period T<sub>min</sub> ± Absolute error

  1/16 μs x (160 ± 1)

  1/16 μs x (1,600 ± 1)

  1/16 μs x (16,000 ± 3)

  1/16 μs x (160,000 ± 20)

  1/16 µs × (1,600,000 ± 160)

  1/16 µs × (16,000,000 ± 1,600)

  1/16 µs × (160,000,000 ± 16,000)

  1/16 µs × (1,600,000,000 ± 160,000)

Period measurements with integration time:

- The table below sets out the measuring ranges and absolute error for period measurements with integration time with a **resolution of 1 µs**.

  | Integration time | T<sub>min</sub> ± absolute error | T ± absolute error |
  | --- | --- | --- |
  | 100 s | 1 µs × (10 ± 0) | 1 µs × (100,000,000 ± 10,000) |
  | 10 s | 1 µs × (10 ± 0) | 1 µs × (10,000,000 ± 1,000) |
  | 1 s | 1 µs × (10 ± 0) | 1 µs × (1,000,000 ± 100) |
  | 0.1 s | 1 µs × (10 ± 0) | 1 µs × (100,000 ± 10) |
  | 0.01 s | 1 µs × (10 ± 0) | 1 µs × (10,000 ± 1) |
- The table below sets out the measuring ranges and absolute error for period measurements with integration time with a **resolution of 1/16 µs**.

  | Integration time | T<sub>min</sub> ± absolute error | T ± absolute error |
  | --- | --- | --- |
  | 100 s | 1/16 µs × (160 ± 0) | 1/16 µs × (1,600,000,000 ± 160,000) |
  | 10 s | 1/16 µs × (160 ± 0) | 1/16 µs × (160,000,000 ± 16,000) |
  | 1 s | 1/16 µs × (160 ± 0) | 1/16 µs × (16,000,000 ± 1,600) |
  | 0.1 s | 1/16 µs × (160 ± 0) | 1/16 µs × (1,600,000 ± 160) |
  | 0.01 s | 1/16 µs × (160 ± 0) | 1/16 µs × (160,000 ± 16) |

##### Values that can be changed during operation

The following values can be changed during operation:

- Low limit
- High limit
- Update time (measuring time) <sup>1)</sup>
- Function of the digital output  <sup>1)</sup>

<sup>1)</sup> not with FM 350‑2

##### Result

The end of a period measurement is reported at the STS_CMP1 or STS_COMP1 (for FM 350‑2) status bit. The value of the calculated period is displayed in 1 μs or 1/16 μs. You can read the period measured from the feedback interface.

### Dosing (only for FM 350-2) (S7-300, S7-400)

#### Description

In this mode, four counter channels are grouped together on the FM 350‑2 to form one dosing channel. When the gate is open, FM 350‑2 counts once in the main count direction:

- In the main count direction "up" between 0 and the parameterized high count limit.

  If you set the main count direction as "up,” the start value is 0 and you specify the end value.
- In the main count direction "down" between the parameterized high count limit and 0.

  If you set the main count direction as "down,” you specify the start value and the end value is 0.

#### Selecting gate control

This mode allows you to select gate control. The following options are available to you:

- [Software gate](#software-gate-s7-300-s7-400)
- [Software gate](#software-gate-s7-300-s7-400) and [HW gate](#hardware-gate-s7-300-s7-400)

  You can add a hardware gate to the software gate. The two gates act together like a logical AND operation, meaning the FM 350‑2 only counts when both gates are open.

#### Behavior at the Count Limits, Software Gate

**Main count direction up:** If the counter receives a further count pulse after reaching the "High count limit - 1", the module sets the counter to 0, closes the internal gate and terminates the count even if the SW_GATE0, 4 bit is still set. The relevant status bit STS_OFLW0, 4 is set. The high count limit itself is therefore never reached.

**Main count direction down:** If the counter receives a further count pulse after reaching the value "1", the module sets the counter to the high count limit, closes the internal gate and terminates the count even if the SW_GATE0, 4 bit is still set. The relevant status bit STS_UFLW0, 4 is set. The value "0" is therefore never reached.

If you want to start the counter again, you must reset the SW_GATE0, 4 bit and then set it again.

#### Behavior at the Count Limits, Hardware Gate

**Main count direction up:** If the counter receives a further count pulse after reaching the "High count limit - 1", the module sets the counter to 0, closes the internal gate and terminates the count even if the SW_GATE0, 4 bit and the I0, I4 input are still set. The high count limit itself is therefore never reached. The relevant status bit STS_OFLW0, 4 is set.

**Main count direction down:** If the counter receives a further count pulse after reaching the value "1", the module sets the counter to the high count limit, closes the internal gate and terminates the count even if the SW_GATE0, 4 bit and the I0, I4 input are still set. The value "0" is therefore never reached. The relevant status bit STS_UFLW0, 4 is set.

If you want to start the counter again, you must reset the I0, I4 input and then set it again. You can only start a new count with the hardware gate.

#### Comparison values

You can configure four comparison values within the parameterized counting range for each dosing channel of the FM 350‑2. You can also configure whether and under what conditions a digital output should be set and/or a hardware interrupt triggered in conjunction with a comparison value. You can set the following conditions for this:

- A hardware interrupt is triggered if the current counter value matches a comparison value.
- A digital output is set if the current counter value is greater than or equal to a comparison value.
- A digital output is set if the current counter value is less than or equal to a comparison value.

A digital output is only set if you have enabled the corresponding output with the CTRL_DQ0…7 bit.

> **Note**
>
> Outputs can only be set while the CPU is in RUN mode if the gate is open.

The figure below shows an example of dosing in the main count direction "down" with comparison values.

![Comparison values](images/24575520651_DV_resource.Stream@PNG-en-US.png)

#### Load Value in Preparation

You can define a load value within the parameterized counting range while the CPU is in RUN mode. This value is used by the counter as the new start value every time after the following events:

- When the high count limit is reached for main count direction up.
- Reaching 0 when counting down
- Canceling of the count process by a software gate or a hardware gate (when the count process is interrupted the load value is not used)

The load value is then the new initial value from which the next and all subsequent dosing processes begin. The set output and interrupt behavior remains the same.

#### Load Value Directly

You can change the current counter value while the CPU is in RUN mode. The new count value is used by the counter directly as the dosing value.

#### Value Range for Load Values

The value range for load values depends on the set main count direction. The range is:

- 0 to high count limit - 2 in main count direction "up"
- High count limit to 2 in main count direction down

### Gate control (S7-300, S7-400)

This section contains information on the following topics:

- [Gate functions (S7-300, S7-400)](#gate-functions-s7-300-s7-400)
- [Software gate (S7-300, S7-400)](#software-gate-s7-300-s7-400)
- [Hardware gate (S7-300, S7-400)](#hardware-gate-s7-300-s7-400)
- [Cancel and interrupt function of the gate (S7-300, S7-400)](#cancel-and-interrupt-function-of-the-gate-s7-300-s7-400)
- [Gate control in isochronous mode (S7-300, S7-400)](#gate-control-in-isochronous-mode-s7-300-s7-400)

#### Gate functions (S7-300, S7-400)

##### Counting with Gate Functions

Many applications require that the count be started or stopped at a defined time depending on other events. The counting process in counter modules is started and stopped like this using a gate function. When the gate opens, the counter receives count pulses and the count starts. When the gate is closed, the counter can no longer receive count pulses and the count stops.

##### Software Gate and Hardware Gate

The counter modules have two gates:

- A [software gate](#software-gate-s7-300-s7-400) which is controlled by the input parameter / control bit SW_GATE.
- A [hardware gate](#hardware-gate-s7-300-s7-400) which is controlled by signals at the module's digital inputs.

Please also see the information on gate function in [isochrone mode](#gate-control-in-isochronous-mode-s7-300-s7-400).

##### Internal Gate

The internal gate is the logic AND operation combining a hardware gate and a software gate. The status at the internal gate is indicated by the STS_GATE bit.

If no hardware gate was assigned, only the setting of the software gate is relevant. The count process is activated, interrupted, resumed, and canceled via the internal gate. The internal gate can also be closed by events dependent on the counter value in the operating modes "Count once" and "Dosing".

| Hardware gate | Software gate | Internal gate | Count process |
| --- | --- | --- | --- |
| open | open | open | active |
| open | closed | closed | inactive |
| closed | open | closed | inactive |
| closed | closed | closed | inactive |

When configuring the hardware and software gates, you can specify whether the internal gate is to cancel or interrupt counting.

- When [cancelled](#cancel-and-interrupt-function-of-the-gate-s7-300-s7-400), the count restarts at its initial value after gate stop and gate start.
- When [interrupted](#cancel-and-interrupt-function-of-the-gate-s7-300-s7-400), the count is resumed from the last current count value following gate stop and gate start.

##### Example

The gate is opened and the count pulses are counted by setting the gate signal. If the gate signal is taken away, the gate will be closed and the count pulses no longer detected by the counter. The count value remains constant.

The diagram below shows the opening and closing of a gate and pulse counting.

![Example](images/17823191435_DV_resource.Stream@PNG-en-US.png)

##### Stopping the count using the gate stop function

You can also stop the count in the FM x50‑1 modules by setting the gate stop function, regardless of the signals set at or status of the software gate. You do this by setting the GATE_STP input parameter.

When you reset this parameter, you can only reopen the gate by setting a positive edge at the digital input "DI start" (hardware gate) or by setting the input parameter SW_GATE (software gate) again.

#### Software gate (S7-300, S7-400)

You open and close the software gate with the input parameter / control bit SW_GATE.

##### Opening and closing the software gate

The image below shows how the software gate is opened and closed. No hardware gates should be configured.

![Opening and closing the software gate](images/17832139659_DV_resource.Stream@PNG-en-US.png)

The software gate is:

- opened by setting the input parameter / control bit SW_GATE.
- closed by resetting the input parameter / control bit SW_GATE.

You can re-open the closed gate by resetting input parameter SW_GATE.

#### Hardware gate (S7-300, S7-400)

You open and close the hardware gate by applying the relevant signals to or removing the signals from the digital inputs.

The software gate must be open.

##### Level-triggered opening and closing of the HW gate

![Level-triggered opening and closing of the HW gate](images/17832341259_DV_resource.Stream@PNG-en-US.png)

Count pulses will be received and counted by the counter as long as the digital input is set. Resetting the digital input closes the gate. The counter stops and ignores any further count pulses.

If the gate is closed as a result of high limit violated or low limit violated, you open it again by a reset > set cycle at the digital input.

The level-controlled hardware gate is activated by the first positive edge at the digital input after you assign parameters.

**ET 200S 1Count24V**
**and**
**1Count5V**
**:**

1Count24V / 1Count5V has a hardware gate, which is controlled by the digital input on the module. You configure the hardware gate as a function of the digital input (Function DI "Hardware Gate"). The gate is opened in response to a positive edge on the digital input and closed in response to a negative edge.

##### Edge-triggered opening and closing of the hardware gate

Edge-controlled opening and closing of the hardware gate is only possible for FM x50‑1.

![Edge-triggered opening and closing of the hardware gate](images/17832643595_DV_resource.Stream@PNG-en-US.png)

An edge-controlled hardware gate is opened by a positive edge at digital input "DI start". The gate is closed by a positive edge at digital input "DI stop".

If a positive edges is set in parallel at both inputs, an open gate will be closed, whereas a closed gate remains closed. A positive edge at digital input "DI start" cannot open the gate if digital input "DI stop" is set.

#### Cancel and interrupt function of the gate (S7-300, S7-400)

In your gate function parameters, you can define whether the gate should cancel or interrupt the count.

##### Cancel gate function

When the "cancel" gate function is active, the count stops when the gate closes and is restarted at the load value when the gate is restarted (time ① in the figure below).

The figure below shows an example of continuous counting down with the "cancel" gate function.

![Cancel gate function](images/24575543179_DV_resource.Stream@PNG-en-US.png)

##### "Interrupt" gate function

When the "interrupt" gate function is active, the count stops when the gate closes, and resumes at the last current counter value when the gate is restarted (time ① in the figure below).

The figure below shows an example of continuous counting up with the "interrupt" gate function.

!["Interrupt" gate function](images/17833160843_DV_resource.Stream@PNG-en-US.png)

#### Gate control in isochronous mode (S7-300, S7-400)

Gate control operates as follows in isochrone mode:

##### Software gate control

The software gate is controlled by setting and resetting the SW_GATE control bit. After the control bit has changed, the count starts and ends at time T<sub>o</sub> in the next PROFIBUS DP cycle:

![Software gate control](images/17833182219_DV_resource.Stream@PNG-en-US.png)

##### Hardware gate control

In hardware gate control mode, the count starts or stops instantaneously when the hardware gate opens or closes:

![Hardware gate control](images/17833382155_DV_resource.Stream@PNG-en-US.png)

### Encoder signals (S7-300, S7-400)

This section contains information on the following topics:

- [Encoders which can be connected (S7-300, S7-400)](#encoders-which-can-be-connected-s7-300-s7-400)
- [5 V differential signal (S7-300, S7-400)](#5-v-differential-signal-s7-300-s7-400)
- [24 V signals (S7-300, S7-400)](#24-v-signals-s7-300-s7-400)

#### Encoders which can be connected (S7-300, S7-400)

The counter module can process square wave signals generated by incremental encoders or pulse generators.

- **Incremental encoders** scan a grating to generate square wave electrical pulses. They differ in terms of pulse amplitude and number of signals. Incremental encoders output two tracks out of phase by 90°.
- **Pulse generators** such as light barriers and initiators (BEROs) only supply a square wave signal with a specific voltage level.

#### 5 V differential signal (S7-300, S7-400)

##### 5 V incremental encoder count signals

The 5 V incremental encoder sends the following RS 422 differential signal to the module:

- A and /A
- B and /B
- N and /N

The signals /A, /B and /N are the inverted signals of A, B and N. Signals A and B are phase-shifted by 90°.

5 V incremental encoders use tracks A and B for counting. Track N is used to initialize the counter with the load value, if programmed accordingly.

Encoders which return inverted signals for each signal sent are symmetrical encoders.

The diagram below shows the time profile of the encoder signals of a 5 V incremental encoder.

![5 V incremental encoder count signals](images/24575587083_DV_resource.Stream@PNG-en-US.png)

The module detects the count direction by evaluating the ratio of signals A and B.

##### Changing the count direction

You can change the count direction using the "Count direction normal" and "Count direction inverted" parameters without having to modify the wiring.

##### Monitoring encoder signals

The module monitors the cable connection, and detects wire-break or short-circuit.

You can define which of the three signal pairs to include in monitoring in your program. There is no need to wire any unused signal pairs, if you have disabled the corresponding diagnostics functions in the program (monitoring.)

An error at all three signals indicates a defective encoder, a short circuit in the encoder supply or that no encoder is connected.

When programming is completed, and the module detects an error, the error information will be written to the diagnostics data records DS0 and DS1. This situation my lead to a diagnostics interrupt if programmed accordingly.

#### 24 V signals (S7-300, S7-400)

##### 24 V incremental encoder count signals

The 24 V incremental encoder returns the 24 V signals A*, B* and N* to the module. The A* and B* signals are phase-shifted by 90°.

24-V signals are marked with an asterisk "*" character.

24 V incremental encoders use tracks A* and B* for counting. Track N* is used to initialize the counter with the load value, if programmed accordingly.

Encoders which do not return inverted signals asymmetrical encoders.

The diagram below shows the time profile of the encoder signals of a 24 V incremental encoder.

![24 V incremental encoder count signals](images/24575616267_DV_resource.Stream@PNG-en-US.png)

The module detects the count direction by evaluating the ratio of signals A* and B*.

You can configure the inputs of 24 V encoder signals for the connection of Sourcing output/push pull or Sinking output to the counter. For further information, refer to the encoder manual.

**Changing the count direction**

You can change the count direction using the "Count direction normal" and "Count direction inverted" parameters without having to modify the wiring.

##### Count signals from 24 V pulse generators without/with direction level

Encoders such as proximity switches (BERO) or light barriers return only a count signal which you wire to terminal A* of the front connector.

in additional, you can wire a signal for direction detection to terminal B* of the relevant counter. If your encoder does not return a corresponding signal, you can wire a corresponding ID signal you generate within the user program, or use a corresponding process signal.

The diagram below shows the time profile of the encoder signals of a 24 V pulse generator with direction level and the resultant count pulses.

![Count signals from 24 V pulse generators without/with direction level](images/17840460555_DV_resource.Stream@PNG-en-US.png)

##### Monitoring encoder signals

The 24 V count signals are not monitored to detect wire breaks or short circuits.

### Signal evaluation (S7-300, S7-400)

This section contains information on the following topics:

- [Overview (S7-300, S7-400)](#overview-s7-300-s7-400)
- [Single evaluation (S7-300, S7-400)](#single-evaluation-s7-300-s7-400)
- [Double evaluation (S7-300, S7-400)](#double-evaluation-s7-300-s7-400)
- [Quadruple evaluation (S7-300, S7-400)](#quadruple-evaluation-s7-300-s7-400)

#### Overview (S7-300, S7-400)

The counter module counter counts the signal edges. It usually evaluates the edge at A (A*) (single evaluation). Options in the program of increasing the resolution:

- [Single evaluation](#single-evaluation-s7-300-s7-400)
- [Double evaluation](#double-evaluation-s7-300-s7-400)
- [Quadruple evaluation](#quadruple-evaluation-s7-300-s7-400)

Multiple evaluation is supported only:

- for incremental 5 V encoders with signals A and B out of phase by 90°.
- for incremental 24 V encoders with signals A* and B* out of phase by 90°.

##### Default setting

The default setting is "Single evaluation".

#### Single evaluation (S7-300, S7-400)

In this mode, the module evaluates only one edge of signal A.

- "Up" count pulses are recorded at the negative edge at A and a low level at B.
- Down count pulses are recorded if the edge at A falls or the level at B is low.

The diagram below illustrates the single evaluation of the signals.

![Figure](images/17841409291_DV_resource.Stream@PNG-en-US.png)

#### Double evaluation (S7-300, S7-400)

Double evaluation refers to the evaluation of the positive and negative edges of signal A. The level of signal B determines whether up or down count pulses are generated.

The diagram below shows double evaluation of signals.

![Figure](images/24575633547_DV_resource.Stream@PNG-en-US.png)

#### Quadruple evaluation (S7-300, S7-400)

Quadruple evaluation refers to the evaluation of the positive and negative edges of signals A and B. The level of signals A and B determines whether up or down count pulses are generated.

The diagram below illustrates the quadruple evaluation of signals.

![Figure](images/17842351627_DV_resource.Stream@PNG-en-US.png)

---
title: "Using ET 200S 1Count24V (S7-300, S7-400)"
package: TFHWC1Count24VenUS
topics: 107
devices: [S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Using ET 200S 1Count24V (S7-300, S7-400)

This section contains information on the following topics:

- [1Count24V terminal assignment (S7-300, S7-400)](#1count24v-terminal-assignment-s7-300-s7-400)
- [Configuring and assigning parameters to 1Count24V (S7-300, S7-400)](#configuring-and-assigning-parameters-to-1count24v-s7-300-s7-400)
- [1Count24V diagnostics (S7-300, S7-400)](#1count24v-diagnostics-s7-300-s7-400)

## 1Count24V terminal assignment (S7-300, S7-400)

### Wiring Rules

The cables (terminals 1 and 5 and terminals 2 and 8) must be shielded. The shield must be supported at both ends. To do this, use the shield support (see the appendix to the [ET 200S Distributed I/O System](http://support.automation.siemens.com/WW/view/en/1144348) operating instructions).

### Terminal assignment of the 1Count24V

The following table shows the terminal assignment for 1Count24V.

| View | Terminal Assignment | Remarks |
| --- | --- | --- |
| ![Terminal assignment of the 1Count24V](images/22611680267_DV_resource.Stream@PNG-en-US.png) |  | B: Direction input or track B  A: Pulse input or track A  24V DC: Sensor supply  M: Chassis ground  DI: Digital input  DO1: Digital output |

### Pulse generator connection

The following table shows the pulse generator connections to the terminal module and the possible count directions.

| Encoder Type | Connection | Count Direction |
| --- | --- | --- |
| Pulse generator without direction indicator | 24 V count pulses at terminal 5 (A) | Up |
| Pulse generator with direction indicator | 24 V count pulses at terminal 5 (A) and 24 V direction at terminal 1 (B) | Up, down |
| Pulse generator with 2 tracks that are 90<sup>o</sup> out of phase | Track A terminal 5 (A) and track B terminal 1 (B) | Up, down |

## Configuring and assigning parameters to 1Count24V (S7-300, S7-400)

This section contains information on the following topics:

- [Operation (S7-300, S7-400)](#operation-s7-300-s7-400)
- [Counting parameters (S7-300, S7-400)](#counting-parameters-s7-300-s7-400)
- [Control and feedback interface for counting modes (S7-300, S7-400)](#control-and-feedback-interface-for-counting-modes-s7-300-s7-400)
- [Measurement parameters (S7-300, S7-400)](#measurement-parameters-s7-300-s7-400)
- [Control and feedback interface for measuring modes (S7-300, S7-400)](#control-and-feedback-interface-for-measuring-modes-s7-300-s7-400)
- [Position feedback parameters (S7-300, S7-400)](#position-feedback-parameters-s7-300-s7-400)
- [Control and feedback interface for position feedback (S7-300, S7-400)](#control-and-feedback-interface-for-position-feedback-s7-300-s7-400)
- [Fast mode parameters (S7-300, S7-400)](#fast-mode-parameters-s7-300-s7-400)
- [Fast mode feedback interface (S7-300, S7-400)](#fast-mode-feedback-interface-s7-300-s7-400)

### Operation (S7-300, S7-400)

This section contains information on the following topics:

- [Selecting an operating mode (S7-300, S7-400)](#selecting-an-operating-mode-s7-300-s7-400)

#### Selecting an operating mode (S7-300, S7-400)

##### Operating mode

You define 1Count24V functionality by setting an operating mode.

| Operating mode | Description |
| --- | --- |
| [Counting](#counting-parameters-s7-300-s7-400) | Preselection for counting modes |
| [Measuring](#measurement-parameters-s7-300-s7-400) | Preselection for measuring modes |
| [Position feedback](#position-feedback-parameters-s7-300-s7-400) | In this mode, 1Count24V counts continuously from the load value:  - If another count pulse is received after 1Count24V reaches the high count limit when counting up, it will jump to the low count limit and continue counting from there without losing a pulse. - If another count pulse is received after 1Count24V reaches the low count limit when counting down, it will jump to the high count limit and continue counting from there without losing a pulse. |
| [Fast mode](#fast-mode-parameters-s7-300-s7-400)   (supported as of firmware version V2.0) | In this mode, 1Count24V counts continuously from the initial value:  - If another count pulse is received after 1Count24V reaches the maximum value that can be represented by 25 bits when counting up (all counter bits are set), the count value will jump to "0" and resume counting from there without losing a pulse. - If 1Count24V reaches the value "0" when counting down and another count pulse is then received, the count value will jump to the maximum value that can be represented by 25 bits (all counter bits set) and resume counting from there without losing a pulse.   This operating mode can be used for position feedback in particularly short isochrone cycles. |

### Counting parameters (S7-300, S7-400)

This section contains information on the following topics:

- [Enabling group diagnostics (S7-300, S7-400)](#enabling-group-diagnostics-s7-300-s7-400)
- [Selecting reaction to CPU/Master STOP (S7-300, S7-400)](#selecting-reaction-to-cpumaster-stop-s7-300-s7-400)
- [Signal evaluation (S7-300, S7-400)](#signal-evaluation-s7-300-s7-400)
- [Selecting filters for input signals (S7-300, S7-400)](#selecting-filters-for-input-signals-s7-300-s7-400)
- [Selecting encoder inputs (S7-300, S7-400)](#selecting-encoder-inputs-s7-300-s7-400)
- [Selecting the count direction (S7-300, S7-400)](#selecting-the-count-direction-s7-300-s7-400)
- [Behavior of the outputs in counting modes (S7-300, S7-400)](#behavior-of-the-outputs-in-counting-modes-s7-300-s7-400)
- [Selecting substitute value DO1 (S7-300, S7-400)](#selecting-substitute-value-do1-s7-300-s7-400)
- [Activating DO1 diagnostics (S7-300, S7-400)](#activating-do1-diagnostics-s7-300-s7-400)
- [Setting hysteresis (S7-300, S7-400)](#setting-hysteresis-s7-300-s7-400)
- [Specifying pulse duration (S7-300, S7-400)](#specifying-pulse-duration-s7-300-s7-400)
- [Selecting counting mode (S7-300, S7-400)](#selecting-counting-mode-s7-300-s7-400)
- [Selecting main count direction (S7-300, S7-400)](#selecting-main-count-direction-s7-300-s7-400)
- [Selecting the gate function (S7-300, S7-400)](#selecting-the-gate-function-s7-300-s7-400)
- [DI function (S7-300, S7-400)](#di-function-s7-300-s7-400)
- [Selecting hardware gate input signal (S7-300, S7-400)](#selecting-hardware-gate-input-signal-s7-300-s7-400)
- [Selecting synchronization (S7-300, S7-400)](#selecting-synchronization-s7-300-s7-400)
- [Specifying the high count limit (S7-300, S7-400)](#specifying-the-high-count-limit-s7-300-s7-400)

#### Enabling group diagnostics (S7-300, S7-400)

##### Group diagnostics

Channel-specific diagnostics will be carried out if you enable group diagnostics in your parameter assignment.

#### Selecting reaction to CPU/Master STOP (S7-300, S7-400)

##### Setting response to CPU/Master STOP

You can configure the response of the 1Count24V to failure of the higher-level controller.

| Parameter | Status of the 1Count24V at CPU/Master STOP | What happens when new parameters are assigned? |
| --- | --- | --- |
| Turn off DO1 | The current mode is cancelled. The gate is closed and the digital output disabled.  Comparison values 1 and 2 the load value are reset. The high and low limit, function and behavior of the digital outputs and the integration time are transferred from the parameters. | The changed parameters are accepted and become effective. |
| Continue working mode <sup>1)</sup> | The current mode will continue working. The gate and digital output status will not change. | The gate is closed. The current mode is cancelled. The digital output is disabled. The changed parameters are accepted and become effective. |
| DO 1 substitute a value | The current mode is cancelled. The gate is closed and the substitute value set for the digital output is activated. Comparison values 1 and 2 and the load value are reset. The high and low limit, function and behavior of the digital outputs and the integration time are transferred from the parameters.  If "Pulse when comparison value is reached" has been set for the output, the only available pulse duration substitute value will be 1. | The changed parameters are accepted and become effective. |
| DO 1 keep last value | The current mode is cancelled. The gate is closed and the status of the digital output is maintained. Comparison values 1 and 2 and the load value are reset. The high and low limit, function and behavior of the digital outputs and the integration time are transferred from the parameters. | The changed parameters are accepted and become effective. |
| <sup>1)</sup>The CPU/Master must not clear the outputs if the mode is to continue working upon transition from CPU/Master STOP to RUN (startup).  Possible solution: In the part of the user program that is executed during startup, set the SW_GATE control bit and transfer the values to 1Count24V. |  |  |

##### Leaving the Assigned State

Under what conditions does the 1Count24V leave the assigned state?

The CPU or master must be in RUN mode and you must make a change at the [control interface](#control-interface-for-counting-modes-s7-300-s7-400).

##### Automatic New Parameter Assignment

New parameters are assigned to the ET 200S station by your CPU/ DP master:

- Upon power on of the CPU/DP master
- Upon IM 151‑1 / IM 151‑1 FO power on
- After failure of the DP transmission
- Once altered parameters or configuration of the ET 200S station have been loaded to the CPU/DP master
- When the 1Count24V is plugged
- Upon power on or inserting of the appropriate power module

#### Signal evaluation (S7-300, S7-400)

This section contains information on the following topics:

- [Selecting count and direction evaluation (S7-300, S7-400)](#selecting-count-and-direction-evaluation-s7-300-s7-400)
- ["Pulse and direction" evaluation (S7-300, S7-400)](#pulse-and-direction-evaluation-s7-300-s7-400)

##### Selecting count and direction evaluation (S7-300, S7-400)

###### Signal evaluation A*, B*

Signal evaluation by means of A*, B* allows you to count directionally. Different evaluation modes are possible depending on the parameter assignment:

- [Pulse and Direction](#pulse-and-direction-evaluation-s7-300-s7-400)

  In the case of 24 V pulse generators with a direction level, there must be an interval of at least 5 µs/50 µs (depending on the input filter set) between the direction signal (B*) and the count signal (A*).

  The following figure shows the interval between direction signal and count signal.

  ![Signal evaluation A*, B*](images/21753136779_DV_resource.Stream@PNG-en-US.png)
- [Rotary Encoder](Counting%20and%20measuring%20%28S7-300%2C%20S7-400%29.md#overview-s7-300-s7-400)

  If you connect a 24 V rotary encoder with two tracks that are 90 degrees out of phase at the count and direction inputs, you can set [single evaluation](Counting%20and%20measuring%20%28S7-300%2C%20S7-400%29.md#single-evaluation-s7-300-s7-400) in all counting modes. You can alternatively set [dual](Counting%20and%20measuring%20%28S7-300%2C%20S7-400%29.md#double-evaluation-s7-300-s7-400) or [quadruple evaluation](Counting%20and%20measuring%20%28S7-300%2C%20S7-400%29.md#quadruple-evaluation-s7-300-s7-400).

  You can invert the [count direction](#selecting-the-count-direction-s7-300-s7-400) at direction input B* in all evaluation modes.

  A range of different sensors can be connected to the encoder inputs (Sourcing output/push pull or Sinking output).

  > **Note**
  >
  > If you have selected the "Sinking output" setting with 1Count24V for the "Encoder inputs" parameter, you must use the M-switching sensors.

  > **Note**
  >
  > The count frequency of 100 kHz is the maximum frequency of the A* and B* signals. The maximum frequency for count pulses is therefore 200 kHz in double evaluation and 400 kHz in quadruple evaluation.

##### "Pulse and direction" evaluation (S7-300, S7-400)

###### Pulse and direction

The level at direction input B* is used as the direction setting in this type of evaluation.

An unwired input corresponds to the "Up" count direction if you have selected "Pulse and direction" for the "Signal evaluation" parameter.

The diagram below shows the signals of a 24 V pulse generator with direction level.

![Pulse and direction](images/21757198603_DV_resource.Stream@PNG-en-US.png)

#### Selecting filters for input signals (S7-300, S7-400)

##### Input filter

You can activate a filter to filter signals at count input A*, direction input B* and digital input DI in line with the minimum pulse duration or the maximum signal frequency.

You can select a minimum pulse width of 2.5 µs or 25 µs for each input.

#### Selecting encoder inputs (S7-300, S7-400)

##### Encoder inputs

A range of different sensors can be connected to the encoder inputs (Sourcing output/push pull or Sinking output).

> **Note**
>
> If you have selected the "Sinking output" setting with for the "Encoder inputs" parameter, you must use the M-switching sensors.

#### Selecting the count direction (S7-300, S7-400)

##### Count direction

To adapt the count direction to the process, you can select:

- Normal count direction:
- Inverted count direction

#### Behavior of the outputs in counting modes (S7-300, S7-400)

This section contains information on the following topics:

- [Comparison values and outputs (S7-300, S7-400)](#comparison-values-and-outputs-s7-300-s7-400)
- [Selecting output behavior (S7-300, S7-400)](#selecting-output-behavior-s7-300-s7-400)
- [Output (S7-300, S7-400)](#output-s7-300-s7-400)
- [On when counter value ≤ comparison value or when counter value ≥ comparison value (S7-300, S7-400)](#on-when-counter-value-comparison-value-or-when-counter-value-comparison-value-s7-300-s7-400)
- [Pulse on reaching the comparison value (S7-300, S7-400)](#pulse-on-reaching-the-comparison-value-s7-300-s7-400)
- [Switch at comparison values (S7-300, S7-400)](#switch-at-comparison-values-s7-300-s7-400)

##### Comparison values and outputs (S7-300, S7-400)

###### Introduction

The 1Count24V allows you to store two comparison values, which are assigned to the digital outputs. The outputs can be activated, depending on the counter status and the comparison values.

###### Digital outputs

The 1Count24V has a real digital output and a virtual digital output that exists only as a status bit in the feedback interface.

Parameters can be assigned for both outputs ("Function DO1" and "Function DO2" parameters).

You can change the function and the behavior of the digital outputs during operation. The new function takes effect immediately.

###### Controlling the outputs and comparators simultaneously

You can continue to control the outputs using SET_DO1 or SET_DO2 if you have selected a compare function for the outputs. This allows you to simulate the effect of the compare functions in your control program:

- The output is set with the positive edge of SET_DO1 or SET_DO2.

  However, if the "Pulse on reaching the comparison value" function is selected, only one pulse with the specified duration will be output. SET_DO1 and SET_DO2 have no effect when pulse duration = 0.

  The SET_DO1 control bit cannot be used with output behavior "Switch at comparison values".
- A SET_DO1 or SET_DO2 negative edge resets the output.

Please note that the comparators are still active and can set or reset the output if the comparison result changes.

> **Note**
>
> An output set by SET_DO1 or SET_DO2 cannot be reset by the comparator.

###### Loading comparison values

You transfer the comparison values to the 1Count24V. This does not affect the count.

###### Valid range for the two comparison values

| Main count direction:  None | Main count direction:  Up | Main count direction:  Down |
| --- | --- | --- |
| Low count limit to high count limit | –2147483648 to high count limit -1 | 1 to 2147483647 |

###### Changing the function and behavior of digital outputs

You can change the functions and behavior of the outputs during operation using the [control interface](#control-interface-for-counting-modes-s7-300-s7-400). The 1Count24V clears the outputs and accepts the values as follows:

- **Function of digital outputs DO1 and DO2:** If you change this function so that the comparison condition is satisfied, the output will not be set until after the next count pulse. However, 1Count24V will not make any changes at the output if [hysteresis](#setting-hysteresis-s7-300-s7-400) is enabled.
- **Hysteresis:** Active [hysteresis](#setting-hysteresis-s7-300-s7-400) remains active after a change. The new hysteresis range will be applied the next time the comparison value is reached.
- **Pulse duration:** The new [pulse duration](#specifying-pulse-duration-s7-300-s7-400) will take effect with the next pulse.

##### Selecting output behavior (S7-300, S7-400)

###### Behavior of outputs DO1 and DO2

Select the behavior of the output in question in the drop down list:

- [Output](#output-s7-300-s7-400)
- [On when counter value ≥ comparison value](#on-when-counter-value-comparison-value-or-when-counter-value-comparison-value-s7-300-s7-400)
- [On when counter value ≤ comparison value](#on-when-counter-value-comparison-value-or-when-counter-value-comparison-value-s7-300-s7-400)
- [Pulse on reaching the comparison value](#pulse-on-reaching-the-comparison-value-s7-300-s7-400)
- [Switch at comparison values](#switch-at-comparison-values-s7-300-s7-400) (DO1 only)

###### Setting or Modifying the Function and Behavior of the Digital Output DO1

When setting or modifying the behavior of DO1, you must take all assignable interdependencies into account. Failure to do so will generate a parameter assignment error or a loading error.

###### Boundary conditions:

If you assign "Switch at comparison values" for DO1, you must:

- Set hysteresis = 0, and
- also configure "DO2 function" as "Output".

##### Output (S7-300, S7-400)

###### Output

You can switch the outputs on and off with the [control bits](#control-interface-for-counting-modes-s7-300-s7-400)SET_DO1 and SET_DO2.

The [control bits](#control-interface-for-counting-modes-s7-300-s7-400)CTRL_DO1 or CTRL_DO2 must be set.

You can query the status of the outputs with the status bits STS_DO1 and STS_DO2 in the [feedback interface](#feedback-interface-for-counting-modes-s7-300-s7-400).

The [status bits](#feedback-interface-for-counting-modes-s7-300-s7-400)STS_CMP1 and STS_CMP2 indicate that the relevant output is or was switched on. These status bits retain their status until they are acknowledged. If the output is still switched, the corresponding bit is set again immediately. These status bits are also set when the control bit SET_DO1 or SET_DO2 is operated without DO1 or DO2 being enabled.

###### Isochrone mode

Output DO1 is switched at time T<sub>o</sub> in isochrone mode. The status of the virtual output DO2 is signaled at time T<sub>i</sub>.

##### On when counter value = comparison value or when counter value = comparison value (S7-300, S7-400)

###### Counter status ≤ Comparison Value and Counter Status ≥ Comparison Value

If the comparison conditions are fulfilled, the respective comparator switches on the output. The [status of the output](#feedback-interface-for-counting-modes-s7-300-s7-400) is indicated by STS_DO1 and STS_DO2.

The [control bits](#control-interface-for-counting-modes-s7-300-s7-400)CTRL_DO1 or CTRL_DO2 must be set.

The result of the comparison is indicated by the [status bits](#feedback-interface-for-counting-modes-s7-300-s7-400)STS_CMP1 or STS_CMP2. You cannot acknowledge and thus reset these bits until the comparison conditions are no longer fulfilled.

###### Isochronous mode

In isochrone mode, too, output DO1 is switched as soon as the comparison condition is fulfilled and is therefore independent of the bus cycle. The status of the virtual output DO2 is reported at time T<sub>i</sub>.

##### Pulse on reaching the comparison value (S7-300, S7-400)

###### Pulse on reaching the comparison value

If the counter status reaches the comparison value, the comparator switches on the respective digital output for the assigned pulse duration.

The [control bit](#control-interface-for-counting-modes-s7-300-s7-400)CTRL_DO1 or CTRL_DO2 must be set.

The status of the [status bits](#feedback-interface-for-counting-modes-s7-300-s7-400)STS_DO1 and STS_DO2 is always the same as that of the corresponding digital output.

The comparison result is indicated by the [status bit](#feedback-interface-for-counting-modes-s7-300-s7-400)STS_CMP1 or STS_CMP2 and cannot be reset by acknowledgment until the pulse duration has elapsed.

If a main count direction is assigned, the comparator switches only when the comparison value in the main count direction is reached.

If a main count direction is not assigned, the comparator switches when the comparison value is reached from either direction.

If the digital output is set by [control bit](#control-interface-for-counting-modes-s7-300-s7-400) SET_DO1 or SET_DO2, it will be reset when the pulse duration has elapsed.

###### Isochronous mode

In isochrone mode, too, output DO1 is switched as soon as the comparison condition is fulfilled and is therefore independent of the bus cycle. The status of virtual output DO2 is reported at time T<sub>i</sub>.

##### Switch at comparison values (S7-300, S7-400)

###### Switch at comparison values

The comparator switches the output when the following conditions are met:

- The two comparison values must be loaded with the [load functions](#control-interface-for-counting-modes-s7-300-s7-400)CMP_VAL1 and CMP_VAL2 and
- The [output DO1](#control-interface-for-counting-modes-s7-300-s7-400) must be enabled with CRTL_DO1 after the comparison values are loaded.

The following table shows you when the DO1 is switched on or off:

|  | DO1 is switched on when | DO1 Is switched off when |
| --- | --- | --- |
| V2 &lt; V1  (see Figure below) | V2 ≤ counter status ≤ V1 | V2 &gt; counter status  or  counter status &gt; V1 |
| V2 = V1 | V2 = counter status = V1 | V2 ≠ counter status ≠ V1 |
| V2 &gt; V1  (see Figure below) | V1 &gt; counter status  or  counter status &gt; V2 | V1 ≤ counter status ≤ V2 |

The figures below show the status of output DO1 as determined by the counter value and comparison values:

- V2 &lt; V1 at the start of counting

  ![Switch at comparison values](images/21844367371_DV_resource.Stream@PNG-en-US.png)
- V2 &gt; V1 at the start of counting

  ![Switch at comparison values](images/21844477323_DV_resource.Stream@PNG-en-US.png)

The result of the comparison is shown by the [status bit](#feedback-interface-for-counting-modes-s7-300-s7-400)STS_CMP1. You can only acknowledge and thus reset this bit when the comparison condition is no longer fulfilled.

There is no hysteresis in the case of this output behavior.

It is not possible to control the DO1 output with [control bit](#control-interface-for-counting-modes-s7-300-s7-400)SET_DO1 if this is the output behavior.

###### Isochronous mode

In isochrone mode, too, output DO1 is switched as soon as the comparison condition is fulfilled and is therefore independent of the bus cycle.

#### Selecting substitute value DO1 (S7-300, S7-400)

##### Substitute value DO1

This is where you select the substitute value which is to be output at digital output DO1 if you have selected the parameter "DO1substitute a value" under "[Reaction to CPU/Master STOP](#selecting-reaction-to-cpumaster-stop-s7-300-s7-400)".

#### Activating DO1 diagnostics (S7-300, S7-400)

##### DO1 diagnostics

"DO1 diagnostics" (wire break, short circuit) are possible only with pulse lengths of &gt; 90 ms at digital output DO1.

Select the check box for diagnostics at output DO1.

#### Setting hysteresis (S7-300, S7-400)

##### Hysteresis

An encoder can remain at a particular position and then fluctuate around this position. This state causes the counter status to fluctuate around a particular value. If there is a comparison value in this fluctuation range, for example, the associated output is switched on and off in accordance with the rhythm of the fluctuations. The 1Count24V is equipped with programmable hysteresis to prevent this switching in response to small fluctuations. You can assign a range between 0 and 255 (0 means: hysteresis switched off).

Hysteresis also works with high limit violated and low limit violated.

##### Method of Operation with Counter Status ≤ Comparison Value and Counter Status ≥ Comparison Value

The example in the figure below demonstrates the effect of hysteresis. The figure shows the differences in the behavior of an output when hysteresis of 0 (= switched off) is parameterized as opposed to hysteresis of 3. In the example, the comparison value is 5.

The following settings are assigned for the counter: "Main count direction" = "Up" and "Turn on at counter status≥ comparison value".

When the comparison condition is met, hysteresis becomes active. While the hysteresis is active, the comparison result remains unchanged.

Hysteresis will no longer be active if the counter value is outside the hysteresis range. The comparator switches again according to its comparison conditions.

![Method of Operation with Counter Status ≤ Comparison Value and Counter Status ≥ Comparison Value](images/21848390411_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> If the count direction changes on the comparison value when hysteresis is active, the output is reset.

##### Method of Operation when the Comparison Value Is Reached and the Pulse Duration = 0

The example in the figure below demonstrates the effect of hysteresis. The figure shows the various responses of an output with a hysteresis of 0 (= switched off) as opposed to hysteresis of 3. In the example, the comparison value is 5.

The following settings are assigned for the counter: "Pulse on reaching the comparison value", "No main count direction" and "Pulse duration = 0".

When the comparison conditions are met, hysteresis becomes active. While the hysteresis is active, the comparison result remains unchanged.

If the counter value goes outside the hysteresis range, hysteresis is no longer active. The comparator deletes the result of the comparison.

![Method of Operation when the Comparison Value Is Reached and the Pulse Duration = 0](images/21848957707_DV_resource.Stream@PNG-en-US.png)

##### Method of Operation when the Comparison Value Is Reached, Output Pulse Duration

The example in the figure below demonstrates the effect of hysteresis. The figure shows the various responses of an output with a hysteresis of 0 (= switched off) as opposed to hysteresis of 3. In the example, the comparison value is 5.

The following settings are assigned for the counter: "Pulse on reaching the comparison value", "No main count direction" and "pulse duration &gt; 0".

When the comparison conditions have been met, hysteresis becomes active and a pulse of the assigned duration is output.

If the counter value goes outside the hysteresis range, hysteresis is no longer active.

When hysteresis is enabled, the 1Count24V stores the count direction.

If the hysteresis range is exited in a different direction to the one stored, a pulse is output.

![Method of Operation when the Comparison Value Is Reached, Output Pulse Duration](images/24575776139_DV_resource.Stream@PNG-en-US.png)

#### Specifying pulse duration (S7-300, S7-400)

##### Pulse duration

The pulse duration begins when the respective digital output is set. The pulse duration is accurate to at least 2 ms.

The pulse duration can be set to suit the actuators used. The pulse duration specifies how long the output is to be set for. The pulse duration can be preselected between 0 ms and 510 ms in increments of 2 ms.

If the pulse duration = 0, the output is set until the comparison condition is no longer fulfilled. Note that the count pulse times must be greater than the minimum switching times of the digital output.

##### Isochronous mode

In isochrone mode, too, output DO1 is switched as soon as the comparison condition is fulfilled and is therefore independent of the bus cycle. The status of virtual output DO2 is reported at time T<sub>i</sub>.

#### Selecting counting mode (S7-300, S7-400)

##### Description

You define 1Count24V functionality by setting a counting mode.

| Operating mode | Description |
| --- | --- |
| [Count continuously](Counting%20and%20measuring%20%28S7-300%2C%20S7-400%29.md#count-continuously-s7-300-s7-400)  (with or without gate) | 1Count24V counts continuously from the current counter value. |
| [Count once](Counting%20and%20measuring%20%28S7-300%2C%20S7-400%29.md#count-once-s7-300-s7-400)   (with hardware or software gate) | When the gate opens, 1Count24V counts from the load value to the count limit. |
| [Count periodically](Counting%20and%20measuring%20%28S7-300%2C%20S7-400%29.md#count-periodically-s7-300-s7-400)   (with hardware or software gate) | When the gate opens, 1Count24V counts from the load value between the count limits. |

The default setting is the "Count continuously" operating mode.

#### Selecting main count direction (S7-300, S7-400)

##### Description

By configuring a [main count direction](Counting%20and%20measuring%20%28S7-300%2C%20S7-400%29.md#main-count-direction-s7-300-s7-400) (up or down), you can reduce the maximum counting range by setting an [high count limit](#specifying-the-high-count-limit-s7-300-s7-400). The parameterized counting range is then between 0 and the high count limit parameterized.

A main count direction can only be selected in the "Count once" and " Count periodically" modes.

You can select the following behavior:

- None (no main count direction)
- Up
- Down

#### Selecting the gate function (S7-300, S7-400)

##### Description

When configuring the hardware and software gates, you can specify whether the internal gate is to cancel or interrupt counting.

- [Cancel counting](Counting%20and%20measuring%20%28S7-300%2C%20S7-400%29.md#cancel-and-interrupt-function-of-the-gate-s7-300-s7-400): The counting process restarts from the beginning after gate stop and restart.
- [Interrupt counting](Counting%20and%20measuring%20%28S7-300%2C%20S7-400%29.md#cancel-and-interrupt-function-of-the-gate-s7-300-s7-400): The counting process starts from the last current counter value after gate stop and restart.

#### DI function (S7-300, S7-400)

This section contains information on the following topics:

- [Selecting DI function (S7-300, S7-400)](#selecting-di-function-s7-300-s7-400)
- [Latch/Retrigger with positive edge (S7-300, S7-400)](#latchretrigger-with-positive-edge-s7-300-s7-400)
- [Synchronization with positive edge (S7-300, S7-400)](#synchronization-with-positive-edge-s7-300-s7-400)
- [Latching with positive edge (S7-300, S7-400)](#latching-with-positive-edge-s7-300-s7-400)

##### Selecting DI function (S7-300, S7-400)

###### Description

You select the digital input function with "DI function":

- Input

  The digital input operates as a "normal" input.
- [Hardware gate](Counting%20and%20measuring%20%28S7-300%2C%20S7-400%29.md#hardware-gate-s7-300-s7-400), level-controlled

  The hardware gate is opened and closed by signals at the digital input.
- [Latch/Retrigger with positive edge](#latchretrigger-with-positive-edge-s7-300-s7-400)

  Counter values are saved (latched) with positive edges at the digital input. The counter is set to the load value each time the values are saved.
- [Synchronization with positive edge](#synchronization-with-positive-edge-s7-300-s7-400)

  The counter is set to the load value with positive edges at the digital input.
- [Latching with positive edge](#latching-with-positive-edge-s7-300-s7-400)

  Counter values are saved (latched) with positive edges at the digital input.

The default setting is "Input".

##### Latch/Retrigger with positive edge (S7-300, S7-400)

###### Latch/Retrigger

This function stores the current internal counter status of the 1Count24V and retriggers counting when there is a positive edge on the digital input. This means that the current internal counter status at the time of the positive edge is stored (latch value), and the 1Count24V is then loaded again with the load value, from which counting resumes.

The following figure shows latch/retrigger when load value = 0.

![Latch/Retrigger](images/21863979019_DV_resource.Stream@PNG-en-US.png)

The counting mode must be enabled with the SW gate before the function can be executed. It is started with the first positive edge on the digital input.

The saved rather than the current counter value is displayed in the [feedback interface](#feedback-interface-for-counting-modes-s7-300-s7-400). The STS_DI bit indicates the status of the latch and retrigger signal.

The latch value is pre-assigned its RESET status:

- "0" for main count direction "None" and "Up"
- "High count limit parameters assigned" for main count direction "Down"

It is not changed when the SW gate is opened.

Direct loading of the counter does not cause the indicated stored counter status to be changed.

If you close the SW gate, counting is only interrupted; this means that when you open the SW gate again, counting is continued. The digital input DI remains active even when the SW gate is closed.

Counting is also latched and triggered in isochronous mode with each edge on the digital input. The counter status that was valid at the time of the last edge before T<sub>i</sub> is displayed in the feedback interface.

###### Extended feedback interface

If the 1Count24V is inserted behind an IM 151 that supports the reading and writing of broader user data interfaces, the current counter value can be read from bytes 8 to 11 of the [feedback interface](#feedback-interface-for-counting-modes-s7-300-s7-400).

##### Synchronization with positive edge (S7-300, S7-400)

###### Synchronization

If you have configured "Synchronization with positive edge", the rising edge of a reference signal at the input will set 1Count24V to the load value.

You can select between once-only and periodic synchronization ("Synchronization" parameter).

The figure below shows the counter values in once-only and periodic synchronization.

![Synchronization](images/21864281867_DV_resource.Stream@PNG-en-US.png)

The following conditions apply:

- The counting mode must have been started with the SW gate.
- The "Enable synchronization" (CTRL_SYN) [control bit](#control-interface-for-counting-modes-s7-300-s7-400) must be set.
- Synchronize once only: If the enable bit is set, the first edge loads the 1Count24V with the load value.
- Synchronization periodically: If the enable bit is set, the first and each subsequent edge loads the 1Count24V with the load value.
- The [feedback bit](#feedback-interface-for-counting-modes-s7-300-s7-400)STS_SYN is set after successful synchronization. It must be reset by the [control bit](#control-interface-for-counting-modes-s7-300-s7-400)RES_STS.
- The signal of a bounce-free switch or the zero mark of a rotary encoder can serve as the reference signal.
- The [feedback bit](#feedback-interface-for-counting-modes-s7-300-s7-400)STS_DI indicates the level of the reference signal.

In isochrone mode, the set [feedback bit](#feedback-interface-for-counting-modes-s7-300-s7-400)STS_SYN indicates that the rising edge at the digital input was between time T<sub>i</sub> in the current cycle and time T<sub>i</sub> in the previous cycle.

##### Latching with positive edge (S7-300, S7-400)

###### Latching

Counter value and latch value are pre-assigned their RESET statuses:

- "0" for main count direction "None" and "Up"
- "High count limit parameters assigned" for main count direction "Down"

The counting function is started when the SW gate is opened. 1Count24V begins at the load value:

- "0" for main count direction "None" and "Up"
- "High count limit parameters assigned" for main count direction "Down"

The following figure shows latching when load value = 0.

![Latching](images/21864252043_DV_resource.Stream@PNG-en-US.png)

The latch value is always the exact counter status at the time of the positive edge on the digital input DI.

The saved rather than the current counter value is displayed in the [feedback interface](#feedback-interface-for-counting-modes-s7-300-s7-400). The STS_DI bit indicates the level of the latch signal.

Direct loading of the counter does not cause the indicated stored counter status to be changed.

In isochronous mode, the counter status that was latched at the time of the last positive edge before T<sub>i</sub> is displayed in the feedback interface.

When you close the SW gate, the effect is either canceling or interrupting, depending on the parameter assignment. The digital input DI remains active even when the software gate is closed.

###### Extended feedback interface

If the 1Count24V is inserted behind an IM 151 that supports the reading and writing of broader user data interfaces, the current counter value can be read from bytes 8 to 11 of the [feedback interface](#feedback-interface-for-counting-modes-s7-300-s7-400).

#### Selecting hardware gate input signal (S7-300, S7-400)

##### Hardware gate input signal

The level of the digital input for the "Function DI = HW gate" configuration with the parameter "Input signal HW gate" can be inverted.

The [feedback bit](#feedback-interface-for-counting-modes-s7-300-s7-400)STS_DI indicates the level of the digital input.

#### Selecting synchronization (S7-300, S7-400)

##### Synchronization

If you have selected "Synchronization with positive edge" at the "[DI function](#selecting-di-function-s7-300-s7-400)" parameter, this is where you can select either once-only or periodic synchronization:

- Once-only: If the enable bit is set, the first edge loads the 1Count24V with the load value.
- Periodic: If the enable bit is set, the first and each subsequent edge loads 1Count24V with the load value.

#### Specifying the high count limit (S7-300, S7-400)

##### Description

By configuring an high count limit together with a [main count direction](Counting%20and%20measuring%20%28S7-300%2C%20S7-400%29.md#main-count-direction-s7-300-s7-400)  (up or down), you can reduce the maximum counting range. The parameterized counting range is then between 0 and the high count limit parameterized.

The high count limit can be any value between &gt; 1 and the high count range limit.

### Control and feedback interface for counting modes (S7-300, S7-400)

This section contains information on the following topics:

- [Control interface for counting modes (S7-300, S7-400)](#control-interface-for-counting-modes-s7-300-s7-400)
- [Feedback interface for counting modes (S7-300, S7-400)](#feedback-interface-for-counting-modes-s7-300-s7-400)

#### Control interface for counting modes (S7-300, S7-400)

> **Note**
>
> The following control interface data is consistent for 1Count24V:
>
> - Bytes 0 ... 3
> - Bytes 4 ... 7
> - Bytes 8 ... 11 (extended user data interface)

##### Control interface assignment

The table below shows the assignment of the 1Count24V control interface (outputs) for counting modes.

| Address |  | Assignment |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Bytes 0 to 3 |  | **Load value direct, preparatory, comparison value 1 or 2** |  |  |  |  |  |
|  | Byte 0 | **Behavior of DO1, DO2 of**  **1Count24V** |  |  |  |  |  |
| Bit 2 | Bit 1 |  | Bit 0 | Function DO1 |  |  |  |
| 0 | 0 |  | 0 | Output |  |  |  |
| 0 | 0 |  | 1 | Turn on at counter status ≥ comparison value |  |  |  |
| 0 | 1 |  | 0 | Turn on at counter status ≤ comparison value |  |  |  |
| 0 | 1 |  | 1 | Pulse on reaching the comparison value |  |  |  |
| 1 | 0 |  | 0 | Switch at comparison values |  |  |  |
| 1 | 0 |  | 1 | blocked |  |  |  |
| 1 | 1 |  | 0 | blocked |  |  |  |
| 1 | 1 |  | 1 | blocked |  |  |  |
|  | Bit 5 |  | Bit 4 | Function DO2 |  |  |  |
| 0 |  | 0 | Output |  |  |  |  |
| 0 |  | 1 | Turn on when counter status ≥ comparison value |  |  |  |  |
| 1 |  | 0 | Turn on when counter status ≤ comparison value |  |  |  |  |
| 1 |  | 1 | Pulse on reaching the comparison value |  |  |  |  |
| Bits 3, 6, and 7: Reserved = 0 |  |  |  |  |  |  |  |
| Bytes 1 to 3 | Byte 1 |  | Hysteresis DO1, DO2 (value range 0 to 255) |  |  |  |  |
| Byte 2 |  | Pulse duration DO1, DO2 (value range 0 to 255) |  |  |  |  |  |
| Byte 3 |  | Reserved = 0 |  |  |  |  |  |
|  |  |  |  |  |  |  | **Name** |
| Byte 4 |  | Bit 7 |  | Error acknowledgment |  |  | EXTF_ACK |
| Bit 6 |  | Enable DO2 |  |  | CTRL_DO2 |  |  |
| Bit 5 |  | Control bit DO2 |  |  | SET_DO2 |  |  |
| Bit 4 |  | Enable DO1 |  |  | CTRL_DO1 |  |  |
| Bit 3 |  | Control bit DO1 |  |  | SET_DO1 |  |  |
| Bit 2 |  | Trigger status bits reset |  |  | RES_STS |  |  |
| Bit 1 |  | Enable synchronization |  |  | CTRL_SYN |  |  |
| Bit 0 |  | Software gate control bit |  |  | SW_GATE |  |  |
| Byte 5 |  | Bit 7 |  | Reserved = 0 |  |  |  |
| Bit 6 |  | Reserved = 0 |  |  |  |  |  |
| Bit 5 |  | Reserved = 0 |  |  |  |  |  |
| Bit 4 |  | Change function and behavior of DO1, DO2 |  |  | C_DOPARAM |  |  |
| Bit 3 |  | Load comparison value 2 |  |  | CMP_VAL2 |  |  |
| Bit 2 |  | Load comparison value 1 |  |  | CMP_VAL1 |  |  |
| Bit 1 |  | Load counter in preparation |  |  | LOAD_PREPARE |  |  |
| Bit 0 |  | Load counter direct |  |  | LOAD_VAL |  |  |
| Bytes 6 to 7 |  | Reserved = 0 <sup>1)</sup> |  |  |  |  |  |
| <sup>1) </sup>Not used for extended user interface |  |  |  |  |  |  |  |

##### Notes on the Control Bits

| Bit | Explanation |
| --- | --- |
| C_DOPARAM | Change function and behavior of DO1, DO2  The values from bytes 0 to 2 are applied as new function, hysteresis, and pulse duration of DO1, DO2. This may result in the following error: The conditions for the "Switch at comparison values" behavior are not fulfilled. |
| CMP_VAL1 | Load comparison value 1  The value from bytes 0 to 3 is transferred to comparison value 1 with the control bit "Load comparison value 1" (CMP_VAL1). |
| CMP_VAL2 | Load comparison value 2  The value from bytes 0 to 3 is transferred to comparison value 2 with the control bit "Load comparison value 2" (CMP_VAL2). |
| CTRL_DO1 | Enable DO1  You use this bit to enable the DO1 output. |
| CTRL_DO2 | Enable DO2  You use this bit to enable the DO2 output. |
| CTRL_SYN | You use this bit to enable synchronization. |
| EXTF_ACK | Error acknowledgment  The error bits must be acknowledged with the EXTF_ACK control bit after the cause has been eliminated. |
| LOAD_PREPARE | Load counter in preparation  The value from bytes 0 to 3 is applied as the load value. |
| LOAD_VAL | The value from bytes 0 to 3 is loaded directly as the new counter value. |
| RES_STS | Trigger status bits reset  The status bits are reset by the acknowledgment process between the RES_STS bit and the RES_STS_A bit. |
| SET_DO1 | Control bit DO1  Switches the DO1 digital output on and off when CRTL_DO1 is set. |
| SET_DO2 | Control bit DO2  Switches the DO2 digital output on and off when CRTL_DO2 is set. |
| SW_GATE | Software gate control bit  The software gate is opened/closed via the control interface with the SW_GATE bit. |

#### Feedback interface for counting modes (S7-300, S7-400)

> **Note**
>
> The following feedback interface data is consistent for 1Count24V:
>
> - Bytes 0 ... 3
> - Bytes 4 ... 7
> - Bytes 8 ... 11 (extended user data interface)

##### Feedback interface assignment

The table below shows the assignment of the 1Count24V feedback interface (inputs) for counting modes.

| Address | Assignment |  | Name |
| --- | --- | --- | --- |
| Bytes 0 to 3 | Count value or stored counter value in the case of the latch function on the digital input |  |  |
| Byte 4 | Bit 7 | Encoder supply short circuit | ERR_24V |
| Bit 6 | Short circuit / wire break / overtemperature | ERR_DO1 |  |
| Bit 5 | Parameter assignment error | ERR_PARA |  |
| Bit 4 | Reserved = 0 |  |  |
| Bit 3 | Reserved = 0 |  |  |
| Bit 2 | Resetting of status bits active | RES_STS_A |  |
| Bit 1 | Load function error | ERR_LOAD |  |
| Bit 0 | Load function is running | STS_LOAD |  |
| Byte 5 | Bit 7 | Status down | STS_C_DN |
| Bit 6 | Status up | STS_C_UP |  |
| Bit 5 | Reserved = 0 |  |  |
| Bit 4 | DO2 status | STS_DO2 |  |
| Bit 3 | DO1 status | STS_DO1 |  |
| Bit 2 | Reserved = 0 |  |  |
| Bit 1 | DI status | STS_DI |  |
| Bit 0 | Internal gate status | STS_GATE |  |
| Byte 6 | Bit 7 | Zero-crossing in the count range when counting without a main count direction | STS_ND |
| Bit 6 | Low count limit | STS_UFLW |  |
| Bit 5 | High count limit | STS_OFLW |  |
| Bit 4 | Comparator 2 status | STS_CMP2 |  |
| Bit 3 | Comparator 1 status | STS_CMP1 |  |
| Bit 2 | Reserved = 0 |  |  |
| Bit 1 | Reserved = 0 |  |  |
| Bit 0 | Synchronization status | STS_SYN |  |
| Byte 7 | Reserved = 0 |  |  |
| Bytes 8 to 11 | Counter value <sup>1)</sup> |  |  |
| <sup>1)</sup> Extended user data interface |  |  |  |

##### Notes on the Feedback Bits

| Bit | Explanation |
| --- | --- |
| ERR_24V | Encoder supply short circuit  The error bit must be acknowledged with the [control bit](#control-interface-for-counting-modes-s7-300-s7-400)EXTF_ACK Diagnostic alarm if parameterized. |
| ERR_DO1 | Short circuit/wire break/overtemperature due to overload at output DO1  The error bit must be acknowledged with the [control bit](#control-interface-for-counting-modes-s7-300-s7-400)EXTF_ACK Diagnostic alarm if parameterized. |
| ERR_LOAD | Load function error  The LOAD_VAL, LOAD_PREPARE, CMP_VAL1, CMP_VAL2 and C_DOPARAM[control bits](#control-interface-for-counting-modes-s7-300-s7-400) cannot be set simultaneously during transfer. As when you load an incorrect value (which is not accepted), this results in the ERR_LOAD status bit being set. |
| ERR_PARA | Errors in assigned module parameters. |
| RES_STS_A | Resetting of status bits active |
| STS_C_DN | Status down |
| STS_C_UP | Status up |
| STS_CMP1 | Comparator 1 status  The STS_CMP1 status bit indicates that the output is or was switched on. It must be acknowledged with the [control bit](#control-interface-for-counting-modes-s7-300-s7-400)RES_STS. If the status bit is acknowledged when the output is still switched on, the bit is set again immediately. This bit is also set if the SET_DO1 control bit is used when DO1 is not enabled. |
| STS_CMP2 | Comparator 2 status  The STS_CMP2 status bit indicates that the output is or was switched on. It must be acknowledged with the [control bit](#control-interface-for-counting-modes-s7-300-s7-400)RES_STS. If the status bit is acknowledged when the output is still switched on, the bit is set again immediately. This bit is also set if the SET_DO2 control bit is operated when DO2 is not enabled. |
| STS_DI | DI status  The status of the DI is indicated in all modes by the STS_DI bit in the feedback interface. |
| STS_DO1 | DO1 status  The STS_DO1 status bit indicates the status of the DO1 digital output. |
| STS_DO2 | DO2 status  The STS_DO2 status bit indicates the status of the virtual DO2 digital output. |
| STS_GATE | Internal gate status: Counting. |
| STS_LOAD | Load function is running |
| STS_ND | Zero-crossing in the count range when counting without a main count direction. The bit must be reset by the [control bit](#control-interface-for-counting-modes-s7-300-s7-400)RES_STS. |
| STS_OFLW  STS_UFLW | High count limit violated  Low count limit violated  Both bits must be reset. |
| STS_SYN | Synchronization status  The STS_SYN bit is set after successful synchronization. It must be reset by the [control bit](#control-interface-for-counting-modes-s7-300-s7-400)RES_STS. |

### Measurement parameters (S7-300, S7-400)

This section contains information on the following topics:

- [Enabling group diagnostics (S7-300, S7-400)](#enabling-group-diagnostics-s7-300-s7-400-1)
- [Selecting reaction to CPU/Master STOP (S7-300, S7-400)](#selecting-reaction-to-cpumaster-stop-s7-300-s7-400-1)
- [Signal evaluation (S7-300, S7-400)](#signal-evaluation-s7-300-s7-400-1)
- [Measuring methods (S7-300, S7-400)](#measuring-methods-s7-300-s7-400)
- [Selecting filters for input signals (S7-300, S7-400)](#selecting-filters-for-input-signals-s7-300-s7-400-1)
- [Selecting encoder inputs (S7-300, S7-400)](#selecting-encoder-inputs-s7-300-s7-400-1)
- [Selecting the count direction (S7-300, S7-400)](#selecting-the-count-direction-s7-300-s7-400-1)
- [Behavior of the output in measuring modes (S7-300, S7-400)](#behavior-of-the-output-in-measuring-modes-s7-300-s7-400)
- [Selecting substitute value DO1 (S7-300, S7-400)](#selecting-substitute-value-do1-s7-300-s7-400-1)
- [Activating DO1 diagnostics (S7-300, S7-400)](#activating-do1-diagnostics-s7-300-s7-400-1)
- [Selecting a measuring mode (S7-300, S7-400)](#selecting-a-measuring-mode-s7-300-s7-400)
- [Selecting period resolution (S7-300, S7-400)](#selecting-period-resolution-s7-300-s7-400)
- [Selecting DI function (S7-300, S7-400)](#selecting-di-function-s7-300-s7-400-1)
- [Selecting hardware gate input signal (S7-300, S7-400)](#selecting-hardware-gate-input-signal-s7-300-s7-400-1)
- [Setting low and high limit (S7-300, S7-400)](#setting-low-and-high-limit-s7-300-s7-400)
- [Specifying measuring time (S7-300, S7-400)](#specifying-measuring-time-s7-300-s7-400)
- [Entering pulses per encoder revolution (S7-300, S7-400)](#entering-pulses-per-encoder-revolution-s7-300-s7-400)

#### Enabling group diagnostics (S7-300, S7-400)

##### Group diagnostics

Channel-specific diagnostics will be carried out if you enable group diagnostics in your parameter assignment.

#### Selecting reaction to CPU/Master STOP (S7-300, S7-400)

##### Setting response to CPU/Master STOP

You can configure the response of the 1Count24V to failure of the higher-level controller.

| Parameter | Status of the 1Count24V at CPU/Master STOP | What happens when new parameters are assigned? |
| --- | --- | --- |
| Turn off DO1 | The current mode is cancelled. The gate is closed and the digital output disabled.  Comparison values 1 and 2 the load value are reset. The high and low limit, function and behavior of the digital outputs and the integration time are transferred from the parameters. | The changed parameters are accepted and become effective. |
| Continue working mode <sup>1)</sup> | The current mode will continue working. The gate and digital output status will not change. | The gate is closed. The current mode is cancelled. The digital output is disabled. The changed parameters are accepted and become effective. |
| DO 1 substitute a value | The current mode is cancelled. The gate is closed and the substitute value set for the digital output is activated. Comparison values 1 and 2 and the load value are reset. The high and low limit, function and behavior of the digital outputs and the integration time are transferred from the parameters.  If "Pulse when comparison value is reached" has been set for the output, the only available pulse duration substitute value will be 1. | The changed parameters are accepted and become effective. |
| DO 1 keep last value | The current mode is cancelled. The gate is closed and the status of the digital output is maintained. Comparison values 1 and 2 and the load value are reset. The high and low limit, function and behavior of the digital outputs and the integration time are transferred from the parameters. | The changed parameters are accepted and become effective. |
| <sup>1)</sup>The CPU/Master must not clear the outputs if the mode is to continue working upon transition from CPU/Master STOP to RUN (startup).  Possible solution: In the part of the user program that is executed during startup, set the SW_GATE control bit and transfer the values to 1Count24V. |  |  |

##### Leaving the Assigned State

Under what conditions does the 1Count24V leave the assigned state?

The CPU or master must be in RUN mode and you must make a change at the [control interface](#control-interface-for-measuring-modes-s7-300-s7-400).

##### Automatic New Parameter Assignment

New parameters are assigned to the ET 200S station by your CPU/ DP master:

- Upon power on of the CPU/DP master
- Upon IM 151‑1 / IM 151‑1 FO power on
- After failure of the DP transmission
- Once altered parameters or configuration of the ET 200S station have been loaded to the CPU/DP master
- When the 1Count24V is plugged
- Upon power on or inserting of the appropriate power module

#### Signal evaluation (S7-300, S7-400)

This section contains information on the following topics:

- [Selecting count and direction evaluation (S7-300, S7-400)](#selecting-count-and-direction-evaluation-s7-300-s7-400-1)
- ["Pulse and direction" evaluation (S7-300, S7-400)](#pulse-and-direction-evaluation-s7-300-s7-400-1)

##### Selecting count and direction evaluation (S7-300, S7-400)

###### Signal evaluation A*, B*

Signal evaluation by means of A*, B* allows direction-specific counting. Different evaluation modes are possible depending on the parameter assignment:

- [Pulse and Direction](#pulse-and-direction-evaluation-s7-300-s7-400-1)

  In the case of 24 V pulse generators with a direction level, there must be an interval of at least 5 µs/50 µs (depending on the input filter set) between the direction signal (B*) and the count signal (A*).

  The following figure shows the interval between direction signal and count signal.

  ![Signal evaluation A*, B*](images/21753136779_DV_resource.Stream@PNG-en-US.png)
- Rotary Encoder

  If you connect a 24 V rotary encoder with two tracks that are 90 degrees out of phase at the count and direction inputs, you can configure [single evaluation](Counting%20and%20measuring%20%28S7-300%2C%20S7-400%29.md#single-evaluation-s7-300-s7-400) in all measuring modes.

  You can invert the [count direction](#selecting-the-count-direction-s7-300-s7-400-1) at direction input B*.

  A range of different sensors can be connected to the encoder inputs (Sourcing output/push pull or Sinking output).

  > **Note**
  >
  > If you have selected the "Sinking output" setting with 1Count24V for the "Encoder inputs" parameter, you must use the M-switching sensors.

  > **Note**
  >
  > The count frequency of 100 kHz is the maximum frequency of the A* and B* signals.

##### "Pulse and direction" evaluation (S7-300, S7-400)

###### Pulse and direction

The level at direction input B* is used as the direction setting in this type of evaluation.

An unwired input corresponds to the "Up" count direction if you have selected "Pulse and direction" for the "Signal evaluation" parameter.

The diagram below shows the signals of a 24 V pulse generator with direction level.

![Pulse and direction](images/21757198603_DV_resource.Stream@PNG-en-US.png)

#### Measuring methods (S7-300, S7-400)

This section contains information on the following topics:

- [Overview (S7-300, S7-400)](#overview-s7-300-s7-400)
- [Measurement with integration time (S7-300, S7-400)](#measurement-with-integration-time-s7-300-s7-400)
- [Continuous measurement (S7-300, S7-400)](#continuous-measurement-s7-300-s7-400)
- [Integration Time and Update Time in Isochronous Mode (S7-300, S7-400)](#integration-time-and-update-time-in-isochronous-mode-s7-300-s7-400)

##### Overview (S7-300, S7-400)

###### Measuring methods

You can choose from the following measuring methods for the "Measuring procedure" parameter:

- [With integration time](#measurement-with-integration-time-s7-300-s7-400)
- [Continuous](#continuous-measurement-s7-300-s7-400)

##### Measurement with integration time (S7-300, S7-400)

###### Measurement with integration time

The measurement is carried out during the assigned integration time. When the integration time elapses, the measured value is updated.

The end of a measurement is indicated by the STS_CMP1[status bit](#feedback-interface-for-measuring-modes-s7-300-s7-400). This bit is reset by the [control bit](#control-interface-for-measuring-modes-s7-300-s7-400)RES_STS in the control interface.

If there were not at least two rising edges in the assigned integration time, 0 is returned as the measured value.

A value of -1 is returned up until the end of the first integration time.

You can change the integration time for the next measurement during operation.

###### Direction Reversal

If the direction of rotation is reversed during integration time, the measured value for this measurement period will be undefined. Evaluating the STS_C_UP and STS_C_DN[feedback bits](#feedback-interface-for-measuring-modes-s7-300-s7-400) (direction evaluation) allows you to respond to any process irregularities.

---

**See also**

[Integration Time and Update Time in Isochronous Mode (S7-300, S7-400)](#integration-time-and-update-time-in-isochronous-mode-s7-300-s7-400)

##### Continuous measurement (S7-300, S7-400)

###### Measuring Principle

The 1Count24V counts each positive edge of a pulse and assigns it a time value in µs.

The update time indicates the time interval at which the measured value is updated by the module in the feedback interface.

Rule for pulse sequences with one or several pulses per update time:

| Symbol | Meaning |
| --- | --- |
| Dynamic measuring time = | Time of last pulse in the current update time interval |
| minus |  |
| Time of last pulse in the previous update time interval |  |

When the update time has elapsed, a new measured value is calculated and output with the dynamic measuring time.

The following dynamic measuring time will result if the current update time does not contain a pulse:

| Symbol | Meaning |
| --- | --- |
| Dynamic measuring time = | Time of current, elapsed update time |
| minus |  |
| Time of last pulse |  |

When the update time has elapsed, an estimated measured value is calculated with the dynamic measuring time under the assumption that a pulse occurred at the end of the update time.

If the "1 Pulse per dynamic measuring time" estimated measured value is less than the last measured value during the frequency and speed measurement, this estimated measured value is output as the new measured value. With the period measurement, the dynamic measuring time is output as the estimated period if the dynamic measuring time is greater than the last measured period.

The figure below shows the measuring principle.

![Measuring Principle](images/21900016267_DV_resource.Stream@PNG-en-US.png)

The 1Count24V measures continuously. When assigning parameters, you specify an update time.

During the time until the end of the first elapsed update time, a value of "-1" is returned.

The continuous measurement begins after the gate is opened with the first pulse of the pulse train to be measured. The first measured value can be calculated after the second pulse, at the earliest.

A measured value (frequency, period, or speed) is output in the feedback interface each time the update time elapses. The end of a measurement is indicated by the STS_CMP1[status bit](#feedback-interface-for-measuring-modes-s7-300-s7-400). This bit is reset with the RES_STS and RES_STS_A bits by applying the complete acknowledgement principle.

If the direction of rotation is reversed during an update time, the measured value for this measurement period will be undefined. Evaluating the STS_C_DN and STS_C_UP[feedback bits](#feedback-interface-for-measuring-modes-s7-300-s7-400) (direction evaluation) enables you to respond to any process irregularities.

The following figure illustrates the principle of continuous measurement taking frequency measurement as an example.

![Measuring Principle](images/21900139019_DV_resource.Stream@PNG-en-US.png)

###### Gate Control

To control the 1Count24V, you have to use the gate functions.

###### Isochronous mode

In isochronous mode, the 1Count24V accepts control bits and control values from the control interface in each bus cycle and reports back the response in the same cycle.

In each cycle, the 1Count24V transfers a measured value and the status bits that were valid at time T<sub>i</sub>.

The measurement starts and ends at time T<sub>i</sub>.

---

**See also**

[Integration Time and Update Time in Isochronous Mode (S7-300, S7-400)](#integration-time-and-update-time-in-isochronous-mode-s7-300-s7-400)

##### Integration Time and Update Time in Isochronous Mode (S7-300, S7-400)

###### Integration time and update time in isochrone mode

If the integration time/update time lasts several T<sub>DP</sub> cycles, the new measured value will be indicated in the user program by the STS_CMP1[status bit](#feedback-interface-for-measuring-modes-s7-300-s7-400) (measurement completed) of the feedback interface. This enables monitoring of the measuring operation or a synchronization with the measuring operation. It takes 4 T<sub>DP</sub> cycles, however, for this alarm to be acknowledged. The minimum integration time/update time in this case is (4 x T<sub>DP</sub>).

You do not need to continually evaluate status bit STS_CMP1 if the application can tolerate a jitter in the integration time/update time of T<sub>DP</sub> and a measured value that remains constant for several cycles. Integration times/update times of (1 x T<sub>DP</sub>) to (3 x T<sub>DP</sub>) are then possible.

A loss of isochrone operation in the last T<sub>DP</sub> cycle of the integration time will increase the integration time/update time by one T<sub>DP</sub> cycle. This does not corrupt the measured value.

> **Note**
>
> The value range limits for the integration time/update time may not be exceeded (see tables for the individual measuring modes).
>
> Violation of the value range limits will result in a parameter assignment error and 1Count24V will not go into isochrone mode.

> **Note**
>
> You must always adjust the integration time/update time parameter if you want to retain the integration time/update time length when you change the configuration from non-isochrone to isochrone mode and vice versa.

#### Selecting filters for input signals (S7-300, S7-400)

##### Input filter

You can activate a filter to filter signals at count input A*, direction input B* and digital input DI in line with the minimum pulse duration or the maximum signal frequency.

You can select a minimum pulse width of 2.5 µs or 25 µs for each input.

#### Selecting encoder inputs (S7-300, S7-400)

##### Encoder inputs

A range of different sensors can be connected to the encoder inputs (Sourcing output/push pull or Sinking output).

> **Note**
>
> If you have selected the "Sinking output" setting with for the "Encoder inputs" parameter, you must use the M-switching sensors.

#### Selecting the count direction (S7-300, S7-400)

##### Count direction

To adapt the count direction to the process, you can select:

- Normal count direction:
- Inverted count direction

#### Behavior of the output in measuring modes (S7-300, S7-400)

This section contains information on the following topics:

- [Selecting behavior of output DO1 (S7-300, S7-400)](#selecting-behavior-of-output-do1-s7-300-s7-400)
- [Output (S7-300, S7-400)](#output-s7-300-s7-400-1)
- [Limit-Value Monitoring (S7-300, S7-400)](#limit-value-monitoring-s7-300-s7-400)

##### Selecting behavior of output DO1 (S7-300, S7-400)

###### Behavior of the Output in Measuring Modes

You can assign parameters for the digital output of the 1Count24V.

You can store a high and a low limit for frequency measurement, rotational speed measurement or period measurement. If the limits are violated, digital output DO1 is activated. These limit values can be assigned and changed with the load function.

You can change the function and the behavior of the digital output during operation. The new function takes effect immediately. In isochronous mode it always takes effect at time T<sub>i</sub>.

You can choose between the following functions in the drop-down list box.

- [Output](#output-s7-300-s7-400-1)
- [Outside limits](#limit-value-monitoring-s7-300-s7-400) (limit monitoring)
- [Violating low limit](#limit-value-monitoring-s7-300-s7-400) (limit monitoring)
- [Exceeding high limit](#limit-value-monitoring-s7-300-s7-400) (limit monitoring)

##### Output (S7-300, S7-400)

###### Output

If you want to switch the output on or off, you must enable it with the CTRL_DO1[control bit](#control-interface-for-measuring-modes-s7-300-s7-400).

You can switch the output on and off with the SET_DO1[control bit](#control-interface-for-measuring-modes-s7-300-s7-400).

You can query the status of the output with the STS_DO1[status bit](#feedback-interface-for-measuring-modes-s7-300-s7-400) in the feedback interface.

In isochronous mode, the output is switched at time T<sub>o</sub>.

##### Limit-Value Monitoring (S7-300, S7-400)

###### Limit monitoring

The figure below illustrates limit monitoring.

![Limit monitoring](images/17794939019_DV_resource.Stream@PNG-en-US.png)

When the integration time has elapsed, the measured value obtained (frequency, rotational speed or period) is compared with the assigned limits.

The STS_UFLW = 1 bit will be set in the [feedback](#feedback-interface-for-measuring-modes-s7-300-s7-400) interface if the current measured value is below the parameterized low limit (measured value &lt; low limit).

The STS_OFLW = 1 bit will be set in the [feedback](#feedback-interface-for-measuring-modes-s7-300-s7-400) interface if the current measured value is above the parameterized high limit (measured value &gt; high limit).

You must acknowledge these bits with the [control bit](#control-interface-for-measuring-modes-s7-300-s7-400)RES_STS.

The corresponding status bit will be set again if the measured value still or once again violates the limits after acknowledgment.

Setting the low limit to 0 switches off dynamic monitoring of "Violating low limit".

The table below shows how the enabled digital output DO1 can be set by limit monitoring in accordance with parameter assignment:

| "Function DO1" parameter | DO1 is Set ... |
| --- | --- |
| Outside limits | Measured value &lt; low limit  OR measured value &gt; high limit |
| Violating low limit | Measured value &lt; low limit |
| Exceeding high limit | Measured value &gt; high limit |

In isochronous mode the output is switched at the end of measurement at time T<sub>i</sub>.

#### Selecting substitute value DO1 (S7-300, S7-400)

##### Substitute value DO1

This is where you select the substitute value which is to be output at digital output DO1 if you have selected the parameter "DO1substitute a value" under "[Reaction to CPU/Master STOP](#selecting-reaction-to-cpumaster-stop-s7-300-s7-400-1)".

#### Activating DO1 diagnostics (S7-300, S7-400)

##### DO1 diagnostics

"DO1 diagnostics" (wire break, short circuit) are possible only with pulse lengths of &gt; 90 ms at digital output DO1.

Select the check box for diagnostics at output DO1.

#### Selecting a measuring mode (S7-300, S7-400)

##### Description

You define 1Count24V functionality by specifying a measuring mode.

|  | Description |  |
| --- | --- | --- |
| Operating mode | Measurement with integration time | Continuous measurement |
| [Frequency measurement](Counting%20and%20measuring%20%28S7-300%2C%20S7-400%29.md#frequency-measurement-s7-300-s7-400)  (with hardware or software gate) | 1Count24V counts the pulses that occur during a specified integration time. | 1Count24V counts the pulses that occur during a dynamic measurement time. |
| [Rotational speed measurement](Counting%20and%20measuring%20%28S7-300%2C%20S7-400%29.md#rotational-speed-measurement-s7-300-s7-400)  (with hardware or software gate) | 1Count24V counts the pulses received from a tachometer generator within a specified integration time and calculates the speed on the basis of this value and the number of pulses per encoder revolution. | 1Count24V counts the pulses received from a tachometer generator within a dynamic measuring time and calculates the speed on the basis of this value and the number of pulses per encoder revolution. |
| [Period measurement](Counting%20and%20measuring%20%28S7-300%2C%20S7-400%29.md#period-measurement-s7-300-s7-400)  (with hardware or software gate) | 1Count24V measures the time between two positive edges of the count signal by counting the pulses of an internal quartz accurate reference frequency (16 MHz) over a specified integration time. | 1Count24V indicates the dynamic measuring time as a period. The mean value of the period is calculated if its duration is less than the update time. |

The default setting is "Frequency measurement" mode.

#### Selecting period resolution (S7-300, S7-400)

##### Description

The value of the calculated period is displayed in 1 μs or 1/16 μs.

Select the required unit of resolution.

##### Possible Measuring Ranges with Error Indication

- Period measurement with integration time

  - Measuring ranges and errors at a resolution of 1 µs:

    | Integration time | T<sub>min</sub> ± absolute error | T<sub>min</sub> ± absolute error |
    | --- | --- | --- |
    | 100 s | 1 µs* (10 ± 0) | 1 µs* (100,000,000 ± 10,000) |
    | 10 s | 1 µs* (10 ± 0) | 1 µs* (10,000,000 ± 1,000) |
    | 1 s | 1 µs* (10 ± 0) | 1 µs* (1,000,000 ± 100) |
    | 0.1 s | 1 µs* (10 ± 0) | 1 µs* (100,000 ± 10) |
    | 0.01 s | 1 µs* (10 ± 0) | 1 µs* (10,000 ± 1) |
  - Measuring ranges and errors at a resolution of 1/16 µs:

    | Integration time | T<sub>min</sub> ± absolute error | T<sub>min</sub> ± absolute error |
    | --- | --- | --- |
    | 100 s | 1/16 µs* (160 ± 0) | 1/16 µs* (1,600,000,000 ± 160,000) |
    | 10 s | 1/16 µs* (160 ± 0) | 1/16 µs* (160,000,000 ± 16,000) |
    | 1 s | 1/16 µs* (160 ± 0) | 1/16 µs* (16,000,000 ± 1,600) |
    | 0.1 s | 1/16 µs* (160 ± 0) | 1/16 µs* (1,600,000 ± 160) |
    | 0.01 s | 1/16 µs* (160 ± 0) | 1/16 µs* (160,000 ± 16) |
- Continuous period measurement:

  - Measuring ranges and errors at a resolution of 1 µs:

    | Period T<sub>min</sub> ± Absolute error | Period T<sub>min</sub> ± Absolute error |
    | --- | --- |
    | 1 μs* (10 ± 0) | 1 μs* (100,000 ± 10) |
    | 1 μs* (100 ± 0) | 1 μs* (1 000 000 ± 100) |
    | 1 μs* (1 000 ± 0) | 1 μs* (10 000 000 ± 1 002) |
    | 1 μs* (10 000 ± 1) | 1 μs* (100,000,000 ± 10,020) |
  - Measuring ranges and errors at a resolution of 1/16 µs:

    | Period T<sub>min</sub> ± Absolute error | Period T<sub>min</sub> ± Absolute error |
    | --- | --- |
    | 1/16 μs* (160 ± 1) | 1/16 μs* (1,600,000 ± 160) |
    | 1/16 μs* (1,600 ± 1) | 1/16 μs* (16,000,000 ± 1,600) |
    | 1/16 μs* (16 000 ± 3) | 1/16 μs* (160 000 000 ± 16 000) |
    | 1/16 μs* (160 000 ± 20) | 1/16 μs* (1,600,000,000 ± 160,000) |

#### Selecting DI function (S7-300, S7-400)

##### Description

You select the digital input function with "DI function":

- Input

  The digital input operates as a "normal" input.
- [Hardware gate](Counting%20and%20measuring%20%28S7-300%2C%20S7-400%29.md#hardware-gate-s7-300-s7-400), level-controlled

  The hardware gate is opened and closed by signals at the digital input.

The default setting is "Input".

#### Selecting hardware gate input signal (S7-300, S7-400)

##### Hardware gate input signal

The level of the digital input for the "Function DI = HW gate" configuration with the parameter "Input signal HW gate" can be inverted.

The [feedback bit](#feedback-interface-for-measuring-modes-s7-300-s7-400)STS_DI indicates the level of the digital input.

#### Setting low and high limit (S7-300, S7-400)

##### Low and high limit

You can save a high and low limit for frequency measurement, speed measurement and period duration measurement. If these limits are exceeded, [digital output DO1](#selecting-behavior-of-output-do1-s7-300-s7-400) will be activated. You can configure these limits and change them using the load function.

The following value ranges are possible for the low and high limits:

| Measuring mode | Low limit (LL) | High limit |
| --- | --- | --- |
| Frequency measurement | 0 to 99,999,999 × 10<sup>-3</sup> Hz | LL+1 to 100,000,000 × 10<sup>-3</sup> Hz |
| Rotational speed measurement | 0 to 24,999,999 × 10<sup>-3</sup> /min | LL+1 to 25,000,000 × 10<sup>-3</sup> /min |
| Period duration measurement (resolution = 1 μs) | 0 to 119,999,999 μs | LL+1 to 120,000,000 μs |
| Period duration measurement (resolution = 1/16 μs) | 0 to 1 919 999 999 × 1/16 μs | LL+1 to 1 920 000 000 × 1/16 μs |

#### Specifying measuring time (S7-300, S7-400)

##### Description

If you have selected a measuring mode, the module will update the measured values on a cyclic basis. The update time/integration time is the product of measuring time x 10ms. You set the measuring time as the factor n.

Detailed descriptions of the value ranges for the measuring time can be found under "[Measuring basics](Counting%20and%20measuring%20%28S7-300%2C%20S7-400%29.md#measuring-basics-s7-300-s7-400)".

#### Entering pulses per encoder revolution (S7-300, S7-400)

##### Pulses per encoder revolution

For "[Rotational speed measurement](Counting%20and%20measuring%20%28S7-300%2C%20S7-400%29.md#rotational-speed-measurement-s7-300-s7-400)" mode, you must also configure the pulses per encoder revolution.

The value for the number of pulses per encoder revolution can be found on the rating plate, or in the technical data of your encoder.

### Control and feedback interface for measuring modes (S7-300, S7-400)

This section contains information on the following topics:

- [Control interface for measuring modes (S7-300, S7-400)](#control-interface-for-measuring-modes-s7-300-s7-400)
- [Feedback interface for measuring modes (S7-300, S7-400)](#feedback-interface-for-measuring-modes-s7-300-s7-400)

#### Control interface for measuring modes (S7-300, S7-400)

> **Note**
>
> The following control interface data is consistent for 1Count24V:
>
> - Bytes 0 ... 3
> - Bytes 4 ... 7
> - Bytes 8 ... 11 (extended user data interface)

##### Control interface assignment

The table below shows the assignment of the 1Count24V control interface (outputs) for measuring modes.

| Address | Assignment |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Bytes 0 to 3 | **Low or high limit** |  |  |  |  |
| **Function of DO1** |  |  |  |  |  |
| Byte 0 | Bit 1 | Bit 0 | Function DO1 |  |  |
| 0 | 0 | Output |  |  |  |
| 0 | 1 | Outside limits |  |  |  |
| 1 | 0 | Violating low limit |  |  |  |
| 1 | 1 | Exceeding high limit |  |  |  |
| Bytes 1 to 3 | Reserved = 0 |  |  |  |  |
| **Integration time** |  |  |  |  |  |
| Bytes 0, 1 | Integration time [n × 10 ms]  (Value range 1 to 1000/12000) |  |  |  |  |
| Bytes 2, 3 | Reserved = 0 |  |  |  |  |
|  |  |  |  |  | **Name** |
| Byte 4 | Bit 7 | Error acknowledgment |  |  | EXTF_ACK |
| Bit 6 | Reserved = 0 |  |  |  |  |
| Bit 5 | Reserved = 0 |  |  |  |  |
| Bit 4 | Enable DO1 |  |  | CTRL_DO1 |  |
| Bit 3 | Control bit DO1 |  |  | SET_DO1 |  |
| Bit 2 | Trigger status bits reset |  |  | RES_STS |  |
| Bit 1 | Reserved = 0 |  |  |  |  |
| Bit 0 | Software gate control bit |  |  | SW_GATE |  |
| Byte 5 | Bit 7 | Reserved = 0 |  |  |  |
| Bit 6 | Reserved = 0 |  |  |  |  |
| Bit 5 | Reserved = 0 |  |  |  |  |
| Bit 4 | Change function of DO1 |  |  | C_DOPARAM |  |
| Bit 3 | Reserved = 0 |  |  |  |  |
| Bit 2 | Change integration time |  |  | C_INTTIME |  |
| Bit 1 | Load high limit |  |  | LOAD_PREPARE |  |
| Bit 0 | Load low limit |  |  | LOAD_VAL |  |
| Bytes 6 to 7 | Reserved = 0 <sup>1)</sup> |  |  |  |  |
| <sup>1) </sup>Not used for extended user interface |  |  |  |  |  |

##### Notes on the control bits

| Bit | Explanation |
| --- | --- |
| C_DOPARAM | Change function of DO1  The value from byte 0 is adopted as the new function of DO1. |
| C_INTTIME | Change integration time  The value from bytes 0 and 1 is adopted as the new integration time for the next measurement. |
| CTRL_DO1 | Enable DO1  You use this bit to enable the DO1 output. |
| EXTF_ACK | Error acknowledgment  The error bits must be acknowledged with the EXTF_ACK control bit after the cause has been eliminated. |
| LOAD_PREPARE | Load high limit  The value from bytes 0 to 3 is applied as the new high limit. |
| LOAD_VAL | Load low limit  The value from bytes 0 to 3 is applied as the new low limit. |
| RES_STS | Trigger status bits reset  The status bits are reset by the acknowledgment process between the RES_STS bit and the RES_STS_A bit. |
| SET_DO1 | Control bit DO1  Switches the DO1 digital output on and off when CRTL_DO1 is set. |
| SW_GATE | Software gate control bit  The software gate is opened/closed via the control interface with the SW_GATE bit. |

#### Feedback interface for measuring modes (S7-300, S7-400)

> **Note**
>
> The following feedback interface data is consistent for 1Count24V:
>
> - Bytes 0 ... 3
> - Bytes 4 ... 7
> - Bytes 8 ... 11 (extended user data interface)

##### Feedback interface assignment

The table below shows the assignment of the 1Count24V feedback interface (inputs) for measuring modes.

| Address | Assignment |  | Name |
| --- | --- | --- | --- |
| Bytes 0 to 3 | Measured value |  |  |
| Byte 4 | Bit 7 | Encoder supply short circuit | ERR_24V |
| Bit 6 | Short circuit / wire break / overtemperature | ERR_DO1 |  |
| Bit 5 | Parameter assignment error | ERR_PARA |  |
| Bit 4 | Reserved = 0 |  |  |
| Bit 3 | Reserved = 0 |  |  |
| Bit 2 | Resetting of status bits active | RES_STS_A |  |
| Bit 1 | Load function error | ERR_LOAD |  |
| Bit 0 | Load function is running | STS_LOAD |  |
| Byte 5 | Bit 7 | Status down | STS_C_DN |
| Bit 6 | Status up | STS_C_UP |  |
| Bit 5 | Reserved = 0 |  |  |
| Bit 4 | Reserved = 0 |  |  |
| Bit 3 | DO1 status | STS_DO1 |  |
| Bit 2 | Reserved = 0 |  |  |
| Bit 1 | DI status | STS_DI |  |
| Bit 0 | Internal gate status | STS_GATE |  |
| Byte 6 | Bit 7 | Reserved = 0 |  |
| Bit 6 | Low limit, measuring range | STS_UFLW |  |
| Bit 5 | High limit, measuring range | STS_OFLW |  |
| Bit 4 | Reserved = 0 |  |  |
| Bit 3 | Measurement completed | STS_CMP1 |  |
| Bit 2 | Reserved = 0 |  |  |
| Bit 1 | Reserved = 0 |  |  |
| Bit 0 | Reserved = 0 |  |  |
| Byte 7 | Reserve = 0 |  |  |
| Bytes 8 to 11 | Counter value <sup>1)</sup> |  |  |
| <sup>1)</sup> Extended user data interface |  |  |  |

##### Notes on the feedback bits

| Bit | Explanation |
| --- | --- |
| ERR_24V | Encoder supply short circuit  The error bit must be acknowledged with the [control bit](#control-interface-for-measuring-modes-s7-300-s7-400)EXTF_ACK. Diagnostic alarm if parameterized. |
| ERR_DO1 | Short circuit/wire break/overtemperature at output DO1  The error bit must be acknowledged with the [control bit](#control-interface-for-measuring-modes-s7-300-s7-400)EXTF_ACK. Diagnostic alarm if parameterized. |
| ERR_LOAD | Load function error  The LOAD_VAL, LOAD_PREPARE, C_DOPARAM and C_INTTIME[control bits](#control-interface-for-measuring-modes-s7-300-s7-400) cannot be set simultaneously during transfer. As when you load an incorrect value (which is not accepted), this results in the ERR_LOAD status bit being set. |
| ERR_PARA | Errors in assigned module parameters. |
| RES_STS_A | Resetting of status bits active |
| STS_C_DN | Status down |
| STS_C_UP | Status up |
| STS_CMP1 | Measurement completed  The measured value is updated each time a time interval (update time/integration time) elapses.    **Measurement with integration time:**   The end of a measurement (after the interval has elapsed) is indicated by the STS_CMP1 status bit.   **Continuous measurement:**   The end of the measurement is signaled by the status bit STS_CMP1 at the end of the update time if a measured value is output. The bit remains at "0" if an estimated measured value is output.  This bit is reset by the [control bit](#control-interface-for-measuring-modes-s7-300-s7-400)RES_STS in the control interface. |
| STS_DI | DI status  The status of the DI is indicated in all modes by the STS_DI bit in the feedback interface. |
| STS_DO1 | DO1 status |
| STS_GATE | Internal gate status: Measuring. |
| STS_LOAD | Load function is running |
| STS_OFLW  STS_UFLW | High limit violated  Low limit violated  Both bits must be reset. |

### Position feedback parameters (S7-300, S7-400)

This section contains information on the following topics:

- [Enabling group diagnostics (S7-300, S7-400)](#enabling-group-diagnostics-s7-300-s7-400-2)
- [Selecting reaction to CPU/Master STOP (S7-300, S7-400)](#selecting-reaction-to-cpumaster-stop-s7-300-s7-400-2)
- [Signal evaluation (S7-300, S7-400)](#signal-evaluation-s7-300-s7-400-2)
- [Selecting filters for input signals (S7-300, S7-400)](#selecting-filters-for-input-signals-s7-300-s7-400-2)
- [Selecting encoder inputs (S7-300, S7-400)](#selecting-encoder-inputs-s7-300-s7-400-2)
- [Selecting the count direction (S7-300, S7-400)](#selecting-the-count-direction-s7-300-s7-400-2)
- [Selecting the gate function (S7-300, S7-400)](#selecting-the-gate-function-s7-300-s7-400-1)
- [DI function (S7-300, S7-400)](#di-function-s7-300-s7-400-1)
- [Selecting hardware gate input signal (S7-300, S7-400)](#selecting-hardware-gate-input-signal-s7-300-s7-400-2)
- [Selecting synchronization (S7-300, S7-400)](#selecting-synchronization-s7-300-s7-400-1)

#### Enabling group diagnostics (S7-300, S7-400)

##### Group diagnostics

Channel-specific diagnostics will be carried out if you enable group diagnostics in your parameter assignment.

#### Selecting reaction to CPU/Master STOP (S7-300, S7-400)

##### Setting response to CPU/Master STOP

You can configure the response of the 1Count24V to failure of the higher-level controller.

| Parameter | Status of the 1Count24V at CPU/Master STOP | What happens when new parameters are assigned? |
| --- | --- | --- |
| Turn off DO1 | The current mode is cancelled. The gate is closed and the digital output disabled.  Comparison values 1 and 2 the load value are reset. The high and low limit, function and behavior of the digital outputs and the integration time are transferred from the parameters. | The changed parameters are accepted and become effective. |
| Continue working mode <sup>1)</sup> | The current mode continues working. The gate and digital output status does not change. | The gate is closed. The current mode is cancelled. The digital output is disabled. The changed parameters are accepted and become effective. |
| <sup>1)</sup>The CPU/Master must not clear the outputs if the mode is to continue working on transition from CPU/Master STOP to RUN (startup).  Possible solution: In the part of the user program that is executed during startup, set the SW_GATE control bit and transfer the values to 1Count24V. |  |  |

##### Exiting parameterized status

Under what conditions does the 1Count24V exit the parameterized status?

The CPU or master must be in RUN mode and you must make a change at the [control interface](#position-feedback-control-interface-s7-300-s7-400).

##### Automatic new parameter assignment

New parameters are assigned to the ET 200S station by your CPU/ DP master:

- Upon CPU/DP master power on
- Upon IM 151‑1 / IM 151‑1 FO power on
- After failure of DP transmission
- Once altered parameters or configuration of the ET 200S station have been loaded to the CPU/DP master
- When the 1Count24V is inserted
- Upon power on or insertion of the corresponding power module

#### Signal evaluation (S7-300, S7-400)

This section contains information on the following topics:

- [Selecting count and direction evaluation (S7-300, S7-400)](#selecting-count-and-direction-evaluation-s7-300-s7-400-2)
- ["Pulse and direction" evaluation (S7-300, S7-400)](#pulse-and-direction-evaluation-s7-300-s7-400-2)

##### Selecting count and direction evaluation (S7-300, S7-400)

###### Signal evaluation A*, B*

Signal evaluation by means of A*, B* allows you to count directionally. Different evaluation modes are possible depending on the parameter assignment:

- [Pulse and Direction](#pulse-and-direction-evaluation-s7-300-s7-400-2)

  In the case of 24 V pulse generators with a direction level, there must be an interval of at least 5 µs/50 µs (depending on the input filter set) between the direction signal (B*) and the count signal (A*).

  The following figure shows the interval between direction signal and count signal.

  ![Signal evaluation A*, B*](images/21753136779_DV_resource.Stream@PNG-en-US.png)
- [Rotary Encoder](Counting%20and%20measuring%20%28S7-300%2C%20S7-400%29.md#overview-s7-300-s7-400)

  If you connect a 24 V rotary encoder with two tracks that are 90 degrees out of phase at the count and direction inputs, you can set [single evaluation](Counting%20and%20measuring%20%28S7-300%2C%20S7-400%29.md#single-evaluation-s7-300-s7-400) in all counting modes. You can alternatively set [dual](Counting%20and%20measuring%20%28S7-300%2C%20S7-400%29.md#double-evaluation-s7-300-s7-400) or [quadruple evaluation](Counting%20and%20measuring%20%28S7-300%2C%20S7-400%29.md#quadruple-evaluation-s7-300-s7-400).

  You can invert the [count direction](#selecting-the-count-direction-s7-300-s7-400-2) at direction input B* in all evaluation modes.

  A range of different sensors can be connected to the encoder inputs (Sourcing output/push pull or Sinking output).

  > **Note**
  >
  > If you have selected the "Sinking output" setting with 1Count24V for the "Encoder inputs" parameter, you must use the M-switching sensors.

  > **Note**
  >
  > The count frequency of 100 kHz is the maximum frequency of the A* and B* signals. The maximum frequency for count pulses is therefore 200 kHz in double evaluation and 400 kHz in quadruple evaluation.

##### "Pulse and direction" evaluation (S7-300, S7-400)

###### Pulse and direction

The level at direction input B* is used as the direction setting in this type of evaluation.

An unwired input corresponds to the "Up" count direction if you have selected "Pulse and direction" for the "Signal evaluation" parameter.

The diagram below shows the signals of a 24 V pulse generator with direction level.

![Pulse and direction](images/21757198603_DV_resource.Stream@PNG-en-US.png)

#### Selecting filters for input signals (S7-300, S7-400)

##### Input filter

You can activate a filter to filter signals at count input A*, direction input B* and digital input DI in line with the minimum pulse duration or the maximum signal frequency.

You can select a minimum pulse width of 2.5 µs or 25 µs for each input.

#### Selecting encoder inputs (S7-300, S7-400)

##### Encoder inputs

A range of different sensors can be connected to the encoder inputs (Sourcing output/push pull or Sinking output).

> **Note**
>
> If you have selected the "Sinking output" setting with for the "Encoder inputs" parameter, you must use the M-switching sensors.

#### Selecting the count direction (S7-300, S7-400)

##### Count direction

To adapt the count direction to the process, you can select:

- Normal count direction:
- Inverted count direction

#### Selecting the gate function (S7-300, S7-400)

##### Description

When configuring the hardware and software gates, you can specify whether the internal gate is to cancel or interrupt counting.

- [Cancel counting](Counting%20and%20measuring%20%28S7-300%2C%20S7-400%29.md#cancel-and-interrupt-function-of-the-gate-s7-300-s7-400): The counting process restarts from the beginning after gate stop and restart.
- [Interrupt counting](Counting%20and%20measuring%20%28S7-300%2C%20S7-400%29.md#cancel-and-interrupt-function-of-the-gate-s7-300-s7-400): The counting process starts from the last current counter value after gate stop and restart.

#### DI function (S7-300, S7-400)

This section contains information on the following topics:

- [Selecting DI function (S7-300, S7-400)](#selecting-di-function-s7-300-s7-400-2)
- [Latch/Retrigger with positive edge (S7-300, S7-400)](#latchretrigger-with-positive-edge-s7-300-s7-400-1)
- [Synchronization with positive edge (S7-300, S7-400)](#synchronization-with-positive-edge-s7-300-s7-400-1)
- [Latching with positive edge (S7-300, S7-400)](#latching-with-positive-edge-s7-300-s7-400-1)

##### Selecting DI function (S7-300, S7-400)

###### Description

You select the digital input function with "DI function":

- Input

  The digital input operates as a "normal" input.
- [Hardware gate](Counting%20and%20measuring%20%28S7-300%2C%20S7-400%29.md#hardware-gate-s7-300-s7-400), level-controlled

  The hardware gate is opened and closed by signals at the digital input.
- [Latch/Retrigger with positive edge](#latchretrigger-with-positive-edge-s7-300-s7-400-1)

  Counter values are saved (latched) with positive edges at the digital input. The counter is set to the load value each time the values are saved.
- [Synchronization with positive edge](#synchronization-with-positive-edge-s7-300-s7-400-1)

  The counter is set to the load value with positive edges at the digital input.
- [Latching with positive edge](#latching-with-positive-edge-s7-300-s7-400-1)

  Counter values are saved (latched) with positive edges at the digital input.

The default setting is "Input".

##### Latch/Retrigger with positive edge (S7-300, S7-400)

###### Latch/Retrigger

This function saves the current internal counter value of the 1Count24V and retriggers counting when there is a positive edge at the digital input. This means that the current internal counter value at the time of the positive edge is stored (latch value), and the 1Count24V is then loaded again with the load value, from which counting resumes.

The following figure shows latch/retrigger when load value = 0.

![Latch/Retrigger](images/21863979019_DV_resource.Stream@PNG-en-US.png)

The counting mode must be enabled with the software gate before the function can be executed. It is started with the first positive edge at the digital input.

The saved rather than the current counter value is displayed in the [feedback interface](#position-feedback-feedback-interface-s7-300-s7-400). The STS_DI bit indicates the status of the latch and retrigger signal.

The latch value is preassigned its RESET status ("0"). It is not changed when the software gate is opened.

Directly loading the counter does not alter the saved counter value displayed.

Closing the software gate only interrupts counting; this means that counting resumes when you open the software gate again. The digital input DI remains active even when the software gate is closed.

Counting is also latched and triggered in isochrone mode with each edge at the digital input. The counter status that was valid at the time of the last edge before T<sub>i</sub> is displayed in the feedback interface.

###### Extended feedback interface

If the 1Count24V is inserted behind an IM 151 that supports the reading and writing of broader user data interfaces, the current count value can be read from bytes 8 to 11 of the [feedback interface](#position-feedback-feedback-interface-s7-300-s7-400).

##### Synchronization with positive edge (S7-300, S7-400)

###### Synchronization

If you have configured "Synchronization with positive edge", the rising edge of a reference signal at the input will set 1Count24V to the load value.

You can select between once-only and periodic synchronization ("Synchronization" parameter).

The figure below shows the counter values in once-only and periodic synchronization.

![Synchronization](images/21864281867_DV_resource.Stream@PNG-en-US.png)

The following conditions apply:

- The counting mode must have been started with the SW gate.
- The "Enable synchronization" (CTRL_SYN) [control bit](#position-feedback-control-interface-s7-300-s7-400) must be set.
- Synchronize once only: If the enable bit is set, the first edge loads the 1Count24V with the load value.
- Synchronization periodically: If the enable bit is set, the first and each subsequent edge loads the 1Count24V with the load value.
- The [feedback bit](#position-feedback-feedback-interface-s7-300-s7-400)STS_SYN is set after successful synchronization. It must be reset by the [control bit](#position-feedback-control-interface-s7-300-s7-400)RES_STS.
- The signal of a bounce-free switch or the zero mark of a rotary encoder can serve as the reference signal.
- The [feedback bit](#position-feedback-feedback-interface-s7-300-s7-400)STS_DI indicates the level of the reference signal.

In isochrone mode, the set [feedback bit](#position-feedback-feedback-interface-s7-300-s7-400)STS_SYN indicates that the rising edge at the digital input was between time T<sub>i</sub> in the current cycle and time T<sub>i</sub> in the previous cycle.

##### Latching with positive edge (S7-300, S7-400)

###### Latching

Counter value and latch value are pre-assigned their RESET statuses ("0"):

The counting function is started when the software gate is opened. 1Count24V begins at the load value ("0").

The following figure shows latching when load value = 0.

![Latching](images/21864252043_DV_resource.Stream@PNG-en-US.png)

The latch value is always the exact counter value at the time of the positive edge at the digital input DI.

The saved rather than the current counter value is displayed in the [feedback interface](#position-feedback-feedback-interface-s7-300-s7-400). The STS_DI bit indicates the level of the latch signal.

Directly loading the counter does not alter the saved counter value displayed.

In isochrone mode, the counter status that was latched at the time of the last positive edge before T<sub>i</sub> is displayed in the feedback interface.

Closing the software gate will either cancel or interrupt depending on the parameter assignment. The digital input DI remains active even when the software gate is closed.

###### Extended feedback interface

If the 1Count24V is inserted behind an IM 151 that supports the reading and writing of broader user data interfaces, the current count value can be read from bytes 8 to 11 of the [feedback interface](#position-feedback-feedback-interface-s7-300-s7-400).

#### Selecting hardware gate input signal (S7-300, S7-400)

##### Hardware gate input signal

The level of the digital input for the "Function DI = HW gate" configuration with the parameter "Input signal HW gate" can be inverted.

The [feedback bit](#position-feedback-feedback-interface-s7-300-s7-400)STS_DI indicates the level of the digital input.

#### Selecting synchronization (S7-300, S7-400)

##### Synchronization

If you have selected "Synchronization with positive edge" at the "[DI function](#selecting-di-function-s7-300-s7-400-2)" parameter, this is where you can select either once-only or periodic synchronization:

- Once-only: If the enable bit is set, the first edge loads the 1Count24V with the load value.
- Periodic: If the enable bit is set, the first and each subsequent edge loads 1Count24V with the load value.

### Control and feedback interface for position feedback (S7-300, S7-400)

This section contains information on the following topics:

- [Position feedback control interface (S7-300, S7-400)](#position-feedback-control-interface-s7-300-s7-400)
- [Position feedback feedback interface (S7-300, S7-400)](#position-feedback-feedback-interface-s7-300-s7-400)

#### Position feedback control interface (S7-300, S7-400)

> **Note**
>
> The following control interface data is consistent for 1Count24V:
>
> - Bytes 0 ... 3
> - Bytes 4 ... 7
> - Bytes 8 ... 11 (extended user data interface)

##### Control interface assignment

The table below shows the assignment of the 1Count24V control interface (outputs) for position feedback.

| Address | Assignment |  | Name |
| --- | --- | --- | --- |
| Bytes 0 to 3 | Load value directly, in preparation |  |  |
| Byte 4 | Bit 7 | Error acknowledgment | EXTF_ACK |
| Bit 6 | Reserved = 0 |  |  |
| Bit 5 | Reserved = 0 |  |  |
| Bit 4 | Reserved = 0 |  |  |
| Bit 3 | Reserved = 0 |  |  |
| Bit 2 | Trigger status bits reset | RES_STS |  |
| Bit 1 | Enable synchronization | CTRL_SYN |  |
| Bit 0 | Software gate control bit | SW_GATE |  |
| Byte 5 | Bit 7 | Reserved = 0 |  |
| Bit 6 | Reserved = 0 |  |  |
| Bit 5 | Reserved = 0 |  |  |
| Bit 4 | Reserved = 0 |  |  |
| Bit 3 | Reserved = 0 |  |  |
| Bit 2 | Reserved = 0 |  |  |
| Bit 1 | Load counter in preparation | LOAD_PREPARE |  |
| Bit 0 | Load counter directly | LOAD_VAL |  |
| Bytes 6 to 7 | Reserved = 0 <sup>1)</sup> |  |  |
| <sup>1) </sup>Not used for extended user interface |  |  |  |

##### Notes on the control bits

| Bit | Explanation |
| --- | --- |
| CTRL_SYN | You use this to enable synchronization. |
| EXTF_ACK | Error acknowledgment  The error bits must be acknowledged with the EXTF_ACK control bit after the cause has been eliminated. |
| LOAD_PREPARE | Load counter in preparation  The value from bytes 0 to 3 is applied as the load value. |
| LOAD_VAL | The value from bytes 0 to 3 is loaded directly as the new counter value. |
| RES_STS | Trigger status bits reset  The status bits are reset by the acknowledgment process between the RES_STS bit and the RES_STS_A bit. |
| SW_GATE | The software gate is opened/closed via the control interface with the SW_GATE bit. |

#### Position feedback feedback interface (S7-300, S7-400)

> **Note**
>
> The following feedback interface data is consistent for 1Count24V:
>
> - Bytes 0 ... 3
> - Bytes 4 ... 7
> - Bytes 8 ... 11 (extended user data interface)

##### Feedback interface assignment

The table below shows the assignment of the 1Count24V feedback interface (inputs) for position feedback.

| Address | Assignment |  | Name |
| --- | --- | --- | --- |
| Bytes 0 to 3 | Counter value or stored counter value in the case of the latch function at the digital input |  |  |
| Byte 4 | Bit 7 | Encoder supply short circuit | ERR_24V |
| Bit 6 | Reserved = 0 |  |  |
| Bit 5 | Parameter assignment error | ERR_PARA |  |
| Bit 4 | Reserved = 0 |  |  |
| Bit 3 | Reserved = 0 |  |  |
| Bit 2 | Resetting of status bits active | RES_STS_A |  |
| Bit 1 | Load function error | ERR_LOAD |  |
| Bit 0 | Load function is running | STS_LOAD |  |
| Byte 5 | Bit 7 | Status down | STS_C_DN |
| Bit 6 | Status up | STS_C_UP |  |
| Bit 5 | Reserved = 0 |  |  |
| Bit 4 | Reserved = 0 |  |  |
| Bit 3 | Reserved = 0 |  |  |
| Bit 2 | Reserved = 0 |  |  |
| Bit 1 | DI status | STS_DI |  |
| Bit 0 | Internal gate status | STS_GATE |  |
| Byte 6 | Bit 7 | Zero pass | STS_ND |
| Bit 6 | Low count limit | STS_UFLW |  |
| Bit 5 | High count limit | STS_OFLW |  |
| Bit 4 | Reserved = 0 |  |  |
| Bit 3 | Reserved = 0 |  |  |
| Bit 2 | Reserved = 0 |  |  |
| Bit 1 | Reserved = 0 |  |  |
| Bit 0 | Synchronization status | STS_SYN |  |
| Byte 7 | Reserved = 0 |  |  |
| Bytes 8 to 11 | Counter value <sup>1)</sup> |  |  |
| <sup>1)</sup> Extended user data interface |  |  |  |

##### Notes on the feedback bits

| Bit | Explanation |
| --- | --- |
| ERR_24V | Encoder supply short circuit  The error bit must be acknowledged with the [control bit](#position-feedback-control-interface-s7-300-s7-400)EXTF_ACK. Diagnostic alarm if parameterized. |
| ERR_LOAD | Load function error  TheLOAD_VAL and LOAD_PREPARE[control bits](#position-feedback-control-interface-s7-300-s7-400) cannot be set simultaneously during transfer. As when you load an incorrect value (which is not accepted), this results in the ERR_LOAD status bit being set. |
| ERR_PARA | Errors in assigned module parameters. |
| RES_STS_A | Resetting of status bits active |
| STS_C_DN | Status down |
| STS_C_UP | Status up |
| STS_DI | DI status  The status of the DI is indicated in all modes by the STS_DI bit in the feedback interface. |
| STS_GATE | Internal gate status: Counting. |
| STS_LOAD | Load function is running |
| STS_ND | Zero pass in the counting range during counting without a main count direction. The bit must be reset by the [control bit](#position-feedback-control-interface-s7-300-s7-400)RES_STS. |
| STS_OFLW  STS_UFLW | High count limit exceeded  Low count limit violated  Both bits must be reset. |
| STS_SYN | Synchronization status:  The STS_SYN bit is set after successful synchronization. It must be reset by the [control bit](#position-feedback-control-interface-s7-300-s7-400)RES_STS. |

### Fast mode parameters (S7-300, S7-400)

This section contains information on the following topics:

- [Selecting reaction to CPU/Master STOP (S7-300, S7-400)](#selecting-reaction-to-cpumaster-stop-s7-300-s7-400-3)
- [Signal evaluation (S7-300, S7-400)](#signal-evaluation-s7-300-s7-400-3)
- [Selecting filters for input signals (S7-300, S7-400)](#selecting-filters-for-input-signals-s7-300-s7-400-3)
- [Selecting encoder inputs (S7-300, S7-400)](#selecting-encoder-inputs-s7-300-s7-400-3)
- [Selecting the count direction (S7-300, S7-400)](#selecting-the-count-direction-s7-300-s7-400-3)
- [Selecting the gate function (S7-300, S7-400)](#selecting-the-gate-function-s7-300-s7-400-2)
- [DI function (S7-300, S7-400)](#di-function-s7-300-s7-400-2)
- [Selecting hardware gate input signal (S7-300, S7-400)](#selecting-hardware-gate-input-signal-s7-300-s7-400-3)
- [Specifying load value (S7-300, S7-400)](#specifying-load-value-s7-300-s7-400)

#### Selecting reaction to CPU/Master STOP (S7-300, S7-400)

##### Setting response to CPU/Master STOP

You can configure the response of the 1Count24V to failure of the higher-level controller.

| Parameter | Status of the 1Count24V at CPU/Master STOP | What happens when new parameters are assigned? |
| --- | --- | --- |
| Turn off DO1 | The current mode is cancelled. The gate is closed and the digital output disabled.  Comparison values 1 and 2 the load value are reset. The high and low limit, function and behavior of the digital outputs and the integration time are transferred from the parameters. | The changed parameters are accepted and become effective. |
| Continue working mode <sup>1)</sup> | The current mode continues working. The gate and digital output status does not change. | The gate is closed. The current mode is cancelled. The digital output is disabled. The changed parameters are accepted and become effective. |
| <sup>1)</sup>The CPU/Master must not clear the outputs if the mode is to continue working on transition from CPU/Master STOP to RUN (startup).  Possible solution: In the part of the user program that is executed during startup, set the SW_GATE control bit and transfer the values to 1Count24V. |  |  |

##### Automatic new parameter assignment

New parameters are assigned to the ET 200S station by your CPU/ DP master:

- Upon CPU/DP master power on
- Upon IM 151‑1 / IM 151‑1 FO power on
- After failure of DP transmission
- Once altered parameters or configuration of the ET 200S station have been loaded to the CPU/DP master
- When the 1Count24V is inserted
- Upon power on or insertion of the corresponding power module

#### Signal evaluation (S7-300, S7-400)

This section contains information on the following topics:

- [Selecting count and direction evaluation (S7-300, S7-400)](#selecting-count-and-direction-evaluation-s7-300-s7-400-3)
- ["Pulse and direction" evaluation (S7-300, S7-400)](#pulse-and-direction-evaluation-s7-300-s7-400-3)

##### Selecting count and direction evaluation (S7-300, S7-400)

###### Signal evaluation A*, B*

Signal evaluation by means of A*, B* allows you to count directionally. Different evaluation modes are possible depending on the parameter assignment:

- [Pulse and Direction](#pulse-and-direction-evaluation-s7-300-s7-400-3)

  In the case of 24 V pulse generators with a direction level, there must be an interval of at least 5 µs/50 µs (depending on the input filter set) between the direction signal (B*) and the count signal (A*).

  The following figure shows the interval between direction signal and count signal.

  ![Signal evaluation A*, B*](images/21753136779_DV_resource.Stream@PNG-en-US.png)
- [Rotary Encoder](Counting%20and%20measuring%20%28S7-300%2C%20S7-400%29.md#overview-s7-300-s7-400)

  If you connect a 24 V rotary encoder with two tracks that are 90 degrees out of phase at the count and direction inputs, you can set [single evaluation](Counting%20and%20measuring%20%28S7-300%2C%20S7-400%29.md#single-evaluation-s7-300-s7-400) in all counting modes. You can alternatively set [dual](Counting%20and%20measuring%20%28S7-300%2C%20S7-400%29.md#double-evaluation-s7-300-s7-400) or [quadruple evaluation](Counting%20and%20measuring%20%28S7-300%2C%20S7-400%29.md#quadruple-evaluation-s7-300-s7-400).

  You can invert the [count direction](#selecting-the-count-direction-s7-300-s7-400-3) at direction input B* in all evaluation modes.

  A range of different sensors can be connected to the encoder inputs (Sourcing output/push pull or Sinking output).

  > **Note**
  >
  > If you have selected the "Sinking output" setting with 1Count24V for the "Encoder inputs" parameter, you must use the M-switching sensors.

  > **Note**
  >
  > The count frequency of 100 kHz is the maximum frequency of the A* and B* signals. The maximum frequency for count pulses is therefore 200 kHz in double evaluation and 400 kHz in quadruple evaluation.

##### "Pulse and direction" evaluation (S7-300, S7-400)

###### Pulse and direction

The level at direction input B* is used as the direction setting in this type of evaluation.

An unwired input corresponds to the "Up" count direction if you have selected "Pulse and direction" for the "Signal evaluation" parameter.

The diagram below shows the signals of a 24 V pulse generator with direction level.

![Pulse and direction](images/21757198603_DV_resource.Stream@PNG-en-US.png)

#### Selecting filters for input signals (S7-300, S7-400)

##### Input filter

You can activate a filter to filter signals at count input A*, direction input B* and digital input DI in line with the minimum pulse duration or the maximum signal frequency.

You can select a minimum pulse width of 2.5 µs or 25 µs for each input.

#### Selecting encoder inputs (S7-300, S7-400)

##### Encoder inputs

A range of different sensors can be connected to the encoder inputs (Sourcing output/push pull or Sinking output).

> **Note**
>
> If you have selected the "Sinking output" setting with for the "Encoder inputs" parameter, you must use the M-switching sensors.

#### Selecting the count direction (S7-300, S7-400)

##### Count direction

To adapt the count direction to the process, you can select:

- Normal count direction:
- Inverted count direction

#### Selecting the gate function (S7-300, S7-400)

##### Description

When configuring the hardware and software gates, you can specify whether the internal gate is to cancel or interrupt counting.

- [Cancel counting](Counting%20and%20measuring%20%28S7-300%2C%20S7-400%29.md#cancel-and-interrupt-function-of-the-gate-s7-300-s7-400): The counting process restarts from the beginning after gate stop and restart.
- [Interrupt counting](Counting%20and%20measuring%20%28S7-300%2C%20S7-400%29.md#cancel-and-interrupt-function-of-the-gate-s7-300-s7-400): The counting process starts from the last current counter value after gate stop and restart.

#### DI function (S7-300, S7-400)

This section contains information on the following topics:

- [Selecting DI function (S7-300, S7-400)](#selecting-di-function-s7-300-s7-400-3)
- [Synchronization with positive edge (S7-300, S7-400)](#synchronization-with-positive-edge-s7-300-s7-400-2)

##### Selecting DI function (S7-300, S7-400)

###### Description

You select the digital input function with "DI function":

- Input

  The digital input operates as a "normal" input.
- [Hardware gate](Counting%20and%20measuring%20%28S7-300%2C%20S7-400%29.md#hardware-gate-s7-300-s7-400), level-controlled

  The hardware gate is opened and closed by signals at the digital input.
- [Synchronization with positive edge](#synchronization-with-positive-edge-s7-300-s7-400-2)

  The counter is set to the load value with positive edges at the digital input.

The default setting is "Input".

##### Synchronization with positive edge (S7-300, S7-400)

###### Synchronization

If you have configured "Synchronization with positive edge", the positive edge of a reference signal at the input will set 1Count24V to the initial value (= load value).

The figure below shows the counter values for synchronization with a positive edge.

![Synchronization](images/21934076299_DV_resource.Stream@PNG-en-US.png)

The following conditions apply:

- "Fast mode" must be active (hardware gate).

  - When synchronization is activated, the first edge and each additional edge loads 1Count24V with the initial value (=load value).
- The signal of a bounce-free switch or the zero mark of a rotary encoder can serve as the reference signal.
- The STS_DI feedback bit indicates the level of the reference signal.

#### Selecting hardware gate input signal (S7-300, S7-400)

##### Hardware gate input signal

The level of the digital input for the "Function DI = HW gate" configuration with the parameter "Input signal HW gate" can be inverted.

The [feedback bit](#fast-mode-feedback-interface-s7-300-s7-400)STS_DI indicates the level of the digital input.

#### Specifying load value (S7-300, S7-400)

##### Load value

You can specify a load value for 1Count24V.

This load value is applied directly as the initial value.

Valid value range: -16777216 to +16777215

### Fast mode feedback interface (S7-300, S7-400)

> **Note**
>
> The following feedback interface data is consistent for 1Count24V:
>
> - Bytes 0 ... 3

#### Feedback interface assignment

The table below shows the assignment of the 1Count24V feedback interface (inputs) for fast mode.

| Address | Assignment |  | Name |
| --- | --- | --- | --- |
| Bytes 0 to 3 | Bit 31 | Lifebeat | LZ |
|  | Bit 30 | Isochronous mode applied | STS_TIC |
|  | Bit 29 | Parameter assignment error | ERR_PARA |
|  | Bit 28 | Group error | EXTF |
|  | Bit 27 | DI status | STS_DI |
|  | Bit 26 | Status of direction up/down | STS_DIR |
|  | Bit 25 | Internal gate status | STS_GATE |
|  | Bits 0 to 24 | Count value |  |

#### Notes on the Feedback Bits

| Bit | Explanation |
| --- | --- |
| ERR_PARA | Errors in assigned module parameters. |
| EXTF | Group error  Possible cause:  - Encoder supply short circuit   EXTF is reset when the causes of the errors have been eliminated. |
| LZ | The lifebeat is toggled each time the feedback interface is updated, i.e. the last value sent is inverted. |
| STS_DI | The bit displays the status of the digital input DI. |
| STS_DIR | Direction status:  - for encoder value change from larger to smaller encoder positions (including zero pass) → "1 " - for encoder value change from smaller to larger encoder positions (including zero pass) → "0 " |
| STS_GATE | Internal gate status: Counting. |
| STS_TIC | Isochronous mode (if assigned) was applied. |

## 1Count24V diagnostics (S7-300, S7-400)

This section contains information on the following topics:

- [Diagnostics using the LED display (S7-300, S7-400)](#diagnostics-using-the-led-display-s7-300-s7-400)
- [Error types (S7-300, S7-400)](#error-types-s7-300-s7-400)

### Diagnostics using the LED display (S7-300, S7-400)

#### LED display on the 1Count24V

![LED display on the 1Count24V](images/22616506251_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Group error (red) |
| ② | Status display for counting direction (green) |
| ③ | Status display for digital input/digital output (green) |

#### Status and error displays by means of LEDs on the 1Count24V

The table below shows the status and fault displays on the 1Count24V.

| Event (LED) |  |  |  |  | Cause | Remedy |
| --- | --- | --- | --- | --- | --- | --- |
| SF | UP | DN | 4 | 8 |  |  |
| On |  |  |  |  | No configuration or incorrect module plugged in. There is a diagnostic message. | Check the parameter assignment. Evaluate the diagnostics data. |
|  | On |  |  |  | Status of the low-order bits of the counter, if the counter counts up. |  |
|  |  | On |  |  | Status of the inverse low-order bits of the counter, if the counter counts down. |  |
|  |  |  | On |  | DO (direct control, comparator output) activated. |  |
|  |  |  |  | On | DI (HW gate, synchronization, latch) activated. |  |

### Error types (S7-300, S7-400)

For information on the structure of the channel-related diagnostics, refer to the manual on the interface module used in your ET 200S station.

#### 1Count24V error types

The following table shows the 1Count24V error types.

| Error type |  | Meaning | Remedy |
| --- | --- | --- | --- |
| 1<sub>D</sub> | 00001:  Short circuit | Short circuit of the sensor supply or the actuator. | Check the wiring to the sensor. Correct the process wiring. |
| 5<sub>D</sub> | 00101:  Overtemperature | The digital output is overloaded. | Correct the process wiring. |
| 6<sub>D</sub> | 00110:  Open circuit | Line to the actuator is interrupted. | Correct the process wiring. |
| 9<sub>D</sub> | 01001:  Error | Internal module error occurred. | Replace the module. |
| Load voltage from the power module is too low. | Correct the process wiring. Check the load voltage. |  |  |
| 16<sub>D</sub> | 10000:  Parameter assignment error | Parameters have not been assigned to the module. | Correct the parameter assignment. |

---
title: "TM41 Terminal Module"
package: stdrui201000enUS
topics: 22
source: Siemens TIA Portal Information System (offline help, en-US)
---


# TM41 Terminal Module

This section contains information on the following topics:

- [TM41 Overview](#tm41-overview)
- [Parameterize TM41](#parameterize-tm41)

## TM41 Overview

This section contains information on the following topics:

- [TM41 Creation and Configuration](#tm41-creation-and-configuration)
- [TM41 Interfaces](#tm41-interfaces)

### TM41 Creation and Configuration

#### Description

The TM41 Terminal Module is a terminal expansion module for snapping on to a standard mounting rail according to DIN 50022. With the TM41 Terminal Module, the number of available digital inputs/outputs and the number of analog outputs within a drive system can be expanded. One channel can also be used for the pulse encoder emulation, see also [TM41 Interfaces](#tm41-interfaces).

The TM41 is connected via DRIVE-CLiQ and inserted into the device view via the hardware catalog.

### TM41 Interfaces

#### Description

![TM41 Interfaces](images/147827049099_DV_resource.Stream@PNG-en-US.png)

TM41 Interfaces

## Parameterize TM41

This section contains information on the following topics:

- [Parameterize Inputs/Outputs](#parameterize-inputsoutputs)
- [TM41 control logic](#tm41-control-logic)

### Parameterize Inputs/Outputs

This section contains information on the following topics:

- [TM41 Inputs/Outputs](#tm41-inputsoutputs)
- [TM41 Analog Input](#tm41-analog-input)
- [TM41 Digital Inputs](#tm41-digital-inputs)
- [TM41 Bidirectional Digital Inputs/Outputs](#tm41-bidirectional-digital-inputsoutputs)
- [TM41 Pulse Encoder Emulation](#tm41-pulse-encoder-emulation)

#### TM41 Inputs/Outputs

##### Description

The TM41 input/output module has the following inputs/outputs:

- 4 [digital inputs](#isolated-tm41-digital-inputs)
- 4 [bidirectional digital inputs/outputs](#tm41-bidirectional-digital-inputsoutputs-1)
- 1 [analog input](#tm41-analog-inputs)
- 1 [pulse encoder emulation](#overview)

  > **Note**
  >
  > For the pulse encoder emulation, you can switch between the SIMOTION and SINAMICS modes.

#### TM41 Analog Input

This section contains information on the following topics:

- [TM41 Analog Inputs](#tm41-analog-inputs)

##### TM41 Analog Inputs

In the "Analog inputs" screen form, you can change the interconnection of the analog input on the input/output component.

- Analog inputs are used for the acquisition of external analog signals. Analog inputs are used, for example, to specify an analog definition of a speed or torque.
- Analog inputs supply a normalized analog signal (current, voltage or temperature). This analog signal is converted via the scaling to the value range -1000%...1000%. The scaling serves to adapt to the machine or to the existing components. You can define a scaling characteristic with two points. You must specify an X coordinate and a Y coordinate for each of the two points.
- Analog values are always subject to noise. You can suppress this noise with a filter. You can also smooth the input signal.

###### Parameterizing analog inputs

1. Correct in the "Offset" ([p4063](SINAMICS%20Parameter%20TB30%20%28Terminal%20Board%29%20%28sdrpa100enUS%29.md#p406301-tb30-analog-inputs-offset)) field the specified voltage value of the offset.

   The offset is added to the value of the input signal prior to scaling.
2. If you want to invert the analog signal, interconnect the signal source in the "Inversion" ([p4067](SINAMICS%20Parameter%20TB30%20%28Terminal%20Board%29%20%28sdrpa100enUS%29.md#p406701-bi-tb30-analog-inputs-invert-signal-source)) field.

   For activated inversion, the LED illuminates green and the ![Parameterizing analog inputs](images/147822431883_DV_resource.Stream@PNG-en-US.PNG) symbol becomes visible in the interconnection.
3. To define a scaling characteristic via the scaling, click the "Scaling" button.

   The "TM31 analog input AI 0 scaling" dialog opens. Specify here the following values for the X and Y coordinates of the scaling characteristic (each for the value pair 1 and 2):

   - Characteristic value x2 ([p4059](SINAMICS%20Parameter%20TB30%20%28Terminal%20Board%29%20%28sdrpa100enUS%29.md#p405901-tb30-analog-inputs-characteristic-value-x2))
   - Characteristic value y2 ([p4060](SINAMICS%20Parameter%20TB30%20%28Terminal%20Board%29%20%28sdrpa100enUS%29.md#p406001-tb30-analog-inputs-characteristic-value-y2))
   - Characteristic value y1 ([p4058](SINAMICS%20Parameter%20TB30%20%28Terminal%20Board%29%20%28sdrpa100enUS%29.md#p405801-tb30-analog-inputs-characteristic-value-y1))
   - Characteristic value x1 ([p4057](SINAMICS%20Parameter%20TB30%20%28Terminal%20Board%29%20%28sdrpa100enUS%29.md#p405701-tb30-analog-inputs-characteristic-value-x1))

   Once all necessary settings have been made, click "Close".

   The dialog closes.
4. If you want to form the absolute value of the scaled input value, click the ![Parameterizing analog inputs](images/147822448651_DV_resource.Stream@PNG-en-US.PNG) (absolute-value generation) symbol.

   An activated inversion is indicated with the following symbol: ![Parameterizing analog inputs](images/147822452619_DV_resource.Stream@PNG-en-US.PNG)
5. To compensate temporary fluctuations of the measured value at the analog input, enter a time constant in the "Smoothing" ([p4053](SINAMICS%20Parameter%20TB30%20%28Terminal%20Board%29%20%28sdrpa100enUS%29.md#p405301-tb30-analog-inputs-smoothing-time-constant)) field.

   The larger the smoothing time constant, the slower the response of the analog input to changes in the measured value.
6. If you require a noise suppression for the input signal, enter a value in the "Noise suppression" field. The noise suppression results as follows:

   - |y-x| &gt; noise suppression   
     results in y = x: The output value is set to the current input value.
   - |y-x| ≤ noise suppression   
     results in y = y<sub>old</sub>: The output value retains its value.
7. Interconnect the "Activate" ([p4069](SINAMICS%20Parameter%20TB30%20%28Terminal%20Board%29%20%28sdrpa100enUS%29.md#p406901-bi-tb30-analog-inputs-signal-source-for-enable)) signal sink for the signal to enable the analog inputs.

   When activated, the LED next to the field illuminates green.
8. Interconnect the "Analog input 0" ([p4055](SINAMICS%20Parameter%20TB30%20%28Terminal%20Board%29%20%28sdrpa100enUS%29.md#r405501-co-tb30-analog-inputs-actual-value-in-percent)) signal sink for the input value of the analog inputs.

###### Additional parameters

---

#### TM41 Digital Inputs

This section contains information on the following topics:

- [Isolated TM41 digital inputs](#isolated-tm41-digital-inputs)

##### Isolated TM41 digital inputs

Digital inputs are used for the acquisition of digital signals. For example, drive enables can be controlled externally. On the "Isolated digital inputs" screen form you can change the interconnection of digital inputs 0...3 on the input/output component. If required, you can also interconnect inverted signals.

**Simulation mode**

The selection box for the terminal evaluation/simulation switchover is only visible online.

###### Parameterizing digital inputs

1. Interconnect the signal sinks for the required digital inputs or the inverted digital inputs.

   You can interconnect up to 4 digital inputs.

#### TM41 Bidirectional Digital Inputs/Outputs

This section contains information on the following topics:

- [TM41 bidirectional digital inputs/outputs](#tm41-bidirectional-digital-inputsoutputs-1)

##### TM41 bidirectional digital inputs/outputs

Here you can change the interconnection of the bidirectional digital inputs/outputs on the input/output component.

- You can assign bidirectional digital inputs/outputs in the function. This means they can be parameterized either as an input or an output.
- Digital inputs are used for the acquisition of digital signals. For example, drive enables can be controlled externally.
- For every digital input signal there is the corresponding inverted signal which can also be used for interconnection.
- Digital outputs are used for the feedback of signals such as enables.

###### Procedure

1. If you want to simplify the view of the screen form, activate the "Optimize view" option.

   The display is then reduced to the essentials. Bidirectional digital inputs cannot be edited in the optimized view. Interconnections are still possible in every view.
2. If you want to assign digital inputs/outputs (0...3), proceed as follows:

   - Interconnect the signal sinks (r4022) for the digital inputs/outputs 0...3.
   - Interconnect the signal sinks (r4023) for the inverted digital inputs/outputs 0...3.
3. If you want to assign digital inputs (0...3), interconnect the signal sources for the digital inputs or the inverted digital inputs/outputs 0...3.

#### TM41 Pulse Encoder Emulation

This section contains information on the following topics:

- [Overview](#overview)
- [Emulation in SIMOTION mode](#emulation-in-simotion-mode)
- [Emulation in SINAMICS mode](#emulation-in-sinamics-mode)
- [Synchronization of the zero marks (SINAMICS mode)](#synchronization-of-the-zero-marks-sinamics-mode)
- [Zero mark emulation (SINAMICS mode)](#zero-mark-emulation-sinamics-mode)
- [TM41 Setpoint Filter](#tm41-setpoint-filter)
- [X520 Encoder Interface](#x520-encoder-interface)

##### Overview

###### Pulse encoder emulation in SIMOTION and SINAMICS mode

Axes can be connected to controllers with analog setpoint output and incremental position measurement via pulse encoder emulation. A controller with an analog setpoint interface can be connected using the analog input of the Terminal Module.

The following modes can be selected:

- [**SIMOTION**](#emulation-in-simotion-mode)

  If you switch from SINAMICS mode to SIMOTION mode ([p4400](SINAMICS%20Parameter%20TM41%20%28Terminal%20Module%29.md#p4400-tm41-encoder-emulation-operating-mode) = 0), the switchover takes effect only after a warm restart ([p0976](SINAMICS%20Parameter%20CU.md#p0976-reset-and-load-all-parameters-1) = 3 or [p0972](SINAMICS%20Parameter%20CU.md#p0972-drive-unit-reset-2) = 1 or a download). You must also enable pulse encoder emulation via parameter [p0840](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p08400n-bi-on-off-off1) (signal source for control word 1, bit 0). You can use [r0898](SINAMICS%20Parameter%20CU.md#r0898015-cobo-control-word-drive-object-1).0 to display the control word for sequence control, which allows you to check the status (ON/OFF1).
- [**SINAMICS**](#emulation-in-sinamics-mode)

  If you switch from SIMOTION mode to SINAMICS mode (p4400 = 1), the switchover takes effect only after a cold restart (switch device off and then on again).   
  If you change the parameters [p0408](SINAMICS%20Parameter%20SERVO.md#p04080n-rotary-encoder-pulse-number) (encoder pulse number) and [p0418](SINAMICS%20Parameter%20SERVO.md#p04180n-fine-resolution-gx_xist1-in-bits) (fine resolution) in the appropriate screen forms, proceed in the following sequence:

  - Change the mode.
  - Adapt all parameters.
  - Save all settings permanently.
  - Perform a cold restart.

The mode that is currently active is displayed in the display box next to the selection list.

###### Delayed effect

A delayed effect can also be caused by the following actions:

- If you switch from SIMOTION mode to SINAMICS mode (p4400 = 1), the switchover takes effect only after a cold restart (switch device off and then on again).
- If you change parameter p0408 (encoder pulse number) and p0418 (fine resolution) in the associated screen forms, it is better to first change the mode, adapt the parameters, save all settings by copying from RAM to ROM and then perform a cold restart.

###### Additional parameters

---

##### Emulation in SIMOTION mode

In the SIMOTION mode, the pulse encoder emulation is based on the speed setpoint.

A speed setpoint [r2060](SINAMICS%20Parameter%20SERVO.md#r2060020-co-if1-profidrive-pzd-receive-double-word) interconnected to [p1155](SINAMICS%20Parameter%20SERVO.md#p11550n-ci-speed-controller-speed-setpoint-1-1) is received with PROFIdrive telegram 3. The speed setpoint can be filtered by an activated ([p1414](SINAMICS%20Parameter%20SERVO.md#p14140n-speed-setpoint-filter-activation-1).0) PT2 element ([p1417](SINAMICS%20Parameter%20SERVO.md#p14170n-speed-setpoint-filter-1-denominator-natural-frequency-1) and [p1418](SINAMICS%20Parameter%20SERVO.md#p14180n-speed-setpoint-filter-1-denominator-damping-1)). The speed setpoint can be delayed with dead time [p1412](SINAMICS%20Parameter%20TM41%20%28Terminal%20Module%29.md#p14120n-tm41-increm-encoder-emulation-speed-setpoint-filter-deadtime). The number of encoder pulses per revolution is set with parameter [p0408](SINAMICS%20Parameter%20SERVO.md#p04080n-rotary-encoder-pulse-number). The distance of the zero marks to the position for enabling the A/B tracks ([r4402](SINAMICS%20Parameter%20TM41%20%28Terminal%20Module%29.md#r440202-cobo-tm41-encoder-emulation-status).1) is specified in parameter [p4426](SINAMICS%20Parameter%20TM41%20%28Terminal%20Module%29.md#p4426-tm41-encoder-emulation-pulses-for-zero-mark) and enabled with [p4401](SINAMICS%20Parameter%20TM41%20%28Terminal%20Module%29.md#p4401-tm41-encoder-emulation-mode).0 = 1.

The speed setpoint is provided with telegram 3 in the bus clock cycle. The bus clock cycle is usually considerably slower than the speed controller clock cycle of the SINAMICS drive and so can lead to steps. When an interpolator is used, the speed setpoint is interpolated linearly between the bus clock cycles, so that any steps that occur are eliminated from the calculation.

###### Parameterizing pulse encoder emulation

1. Select "[0] SIMOTION" mode in the "Select mode" drop-down list.

   The screen form is built for "SIMOTION" mode.
2. Interconnect the "Speed setpoint" (p1155) signal source for speed setpoint 1 of the incremental encoder emulation.
3. If you want to activate the interpolator, select the "Yes" option in the "Interpolator" ([p1189](SINAMICS%20Parameter%20SERVO.md#p11890n-speed-setpoint-configuration-1)) drop-down list.
4. Should you want to activate and parameterize a setpoint filter, click the "Setpoint filter" button.

   The "TM41 SIMOTION setpoint filter" dialog opens.
5. If required, correct the following default values:

   - Characteristic frequency ([p4117](SINAMICS%20Parameter%20TM150%20%28Terminal%20Module%29%20%28sdrpa208enUS%29.md#p411702-tm150-group-sensor-error-effect))
   - Nominal damping ([p4118](SINAMICS%20Parameter%20TM150%20%28Terminal%20Module%29%20%28sdrpa208enUS%29.md#p4118011-tm150-fault-thresholdalarm-threshold-hysteresis))
6. Activate the "Activate filter 1" option and click "OK" to confirm.

   The dialog closes. The "Setpoint filter" button now shows a curve.
7. If you want to delay the speed setpoint for the pulse encoder emulation, enter an appropriate delay time in the "Dead time" (p1412) field.
8. To parameterize the encoder emulation, click the "Encoder" button.

   The "Configuration" dialog opens.
9. Correct the following encoder default values in the dialog:

   - Encoder pulse number (p0408)

     Encoder pulse number of the leading encoder.
   - Fine resolution ([p0418](SINAMICS%20Parameter%20SERVO.md#p04180n-fine-resolution-gx_xist1-in-bits))

     The fine resolution is a multiplication factor for the encoder resolution. Each encoder pulse can be further subdivided with the fine resolution. The factory setting is 11 bits. This corresponds to 2048.
   - Zero mark offset (p4426)

     Pulse number to output the zero mark for the incremental encoder emulation.
10. Once all necessary settings have been made, click "Close".

    The dialog closes.
11. If required, also interconnect the connector output for the Gn_XIST1 actual encoder value to PROFIdrive.

###### Additional parameters

---

##### Emulation in SINAMICS mode

In the SINAMICS mode, the incremental encoder emulation is based on the actual encoder position value of the leading encoder.

The actual position values of the leading encoder are interconnected with Terminal Module 41 via a connector input ([p4420](SINAMICS%20Parameter%20TM41%20%28Terminal%20Module%29.md#p4420-ci-tm41-encoder-emulation-position-setpoint)). This is possible for every encoder irrespective of the drive object to which it is assigned. This means the actual position values at the TM41 are available as pulse encoder emulation, including the zero mark. The signals of the pulse encoder emulation appear like the signals of a TTL encoder and can be processed by an external controller or hardware.

> **Note**
>
> Connector input p4420 should be interconnected with signal source [r0479](SINAMICS%20Parameter%20SERVO.md#r047902-co-diagnostics-encoder-position-actual-value-gn_xist1) (diagnostics actual encoder position value Gn_XIST1). The value is refreshed with each DRIVE-CLiQ basic clock cycle and is displayed with sign.

The TM41 supports a pulse count increase/decrease between the output signal of the leading encoder and the output signal of the TM41. The number of encoder pulses per revolution of the leading encoder is set with [p4408](SINAMICS%20Parameter%20TM41%20%28Terminal%20Module%29.md#p4408-tm41-encoder-emulation-pulse-number-leading-encoder). The pulse count of the encoder emulation of the TM41 is set with [p0408](SINAMICS%20Parameter%20SERVO.md#p04080n-rotary-encoder-pulse-number). The parameters p4408 and p0408 may have any ratio with each other.

The zero mark signal for the TM41 is generated from the zero position of the leading encoder. Parameters [p0493](SINAMICS%20Parameter%20SERVO.md#p04930n-zero-mark-selection-input-terminal-1), [p0494](SINAMICS%20Parameter%20SERVO.md#p04940n-equivalent-zero-mark-input-terminal-1) and [p0495](SINAMICS%20Parameter%20SERVO.md#p049502-equivalent-zero-mark-input-terminal-1) of the drive object / encoder object are used to generate the zero position of the leading encoder.

###### Parameterizing pulse encoder emulation

1. Select "[1] SINAMICS" mode in the "Select mode" drop-down list.

   The screen form is built for "SINAMICS" mode.
2. Interconnect the "Position setpoint" (p4420) signal source for the position setpoint of the incremental encoder emulation.
3. If you want to invert the signal of the position setpoint, click the ![Parameterizing pulse encoder emulation](images/147822448651_DV_resource.Stream@PNG-en-US.PNG) inversion symbol.

   An activated inversion is indicated with the following symbol: ![Parameterizing pulse encoder emulation](images/147822431883_DV_resource.Stream@PNG-en-US.PNG)
4. If you want to compensate the dead time for the incremental encoder emulation, enter a factor in the "Predication factor" ([p4421](SINAMICS%20Parameter%20TM41%20%28Terminal%20Module%29.md#p4421-tm41-encoder-emulation-deadtime-compensation)) field.

   This factor determines the multiplicator with which the encoder position setpoint of the incremental encoder emulation can be offset depending on the velocity.
5. To parameterize the encoder emulation, click the "Encoder" button.

   The "Configuration" dialog opens.
6. Correct the following encoder default values in the dialog:

   - Encoder pulse number (p0408)

     Encoder pulse number of the encoder emulation.
   - Fine resolution ([p0418](SINAMICS%20Parameter%20SERVO.md#p04180n-fine-resolution-gx_xist1-in-bits))

     The fine resolution is a multiplication factor for the encoder resolution. Each encoder pulse can be further subdivided with the fine resolution. The factory setting is 11 bits. This corresponds to 2048.
   - Zero mark offset ([p4426](SINAMICS%20Parameter%20TM41%20%28Terminal%20Module%29.md#p4426-tm41-encoder-emulation-pulses-for-zero-mark))

     Pulse number to output the zero mark for the incremental encoder emulation.
   - Encoder pulse number (p4408)

     Encoder pulse number of the leading encoder.
   - Fine resolution ([p4418](SINAMICS%20Parameter%20TM41%20%28Terminal%20Module%29.md#p4418-tm41-encoder-emulation-fine-resolution-leading-encoder))

     Defines the format of the position setpoint for the TM41
7. Once all necessary settings have been made, click "Close".

   The dialog closes.
8. If required, you can display the pin assignment of the encoder interface X520 in a dialog. To do this, click the "Encoder interface X520" button.
9. If required, also interconnect the connector output for the Gn_XIST1 actual encoder value to PROFIdrive.

###### Additional parameters

---

##### Synchronization of the zero marks (SINAMICS mode)

After the drive has been powered up, a static offset is obtained as a result of the random switch-on instant of the incremental encoder emulation.

This static offset can be corrected using this function. The positions of the zero marks output at the TM41 are synchronized with the zero marks of the leading encoder. The following conditions are defined for synchronization:

- The reference mark is located at the position at which both track signals A and B have the "high" status.
- The zero position is the positive edge of the A track belonging to the reference mark, which for a positive direction of rotation comes before the zero mark.

![Example: Zero mark synchronization](images/147827275787_DV_resource.Stream@PNG-en-US.png)

Example: Zero mark synchronization

Layout of the synchronization:

- After the SINAMICS system has been powered up, the TM41 drive object requests the zero position of the leading encoder via the encoder interface. The encoder emulation follows the movements of the leading encoder and outputs the track signals A/B. At this point in time, no zero mark is output. The edges of the A track are still not in synchronism with the leading encoder.
- The TM41 receives this position after passing the zero position of the leading encoder. The output of the track signals is now corrected in such a way that the positive edge of the A track is in synchronism with the zero position.
- After successful synchronization, the zero mark is output at the zero positions.

###### Detecting the zero mark position for new synchronization

If the number of encoder pulses has not been set equal to 2<sup>n </sup>(for example [p0408](SINAMICS%20Parameter%20SERVO.md#p04080n-rotary-encoder-pulse-number) = 1000), then after the higher-level controller has been reset, it is possible that the position of the next zero mark cannot be determined from the actual position value xACT1 signaled from the TM41. For this situation, the control can query the position of the next zero mark from parameter [r4427](SINAMICS%20Parameter%20TM41%20%28Terminal%20Module%29.md#r4427-tm41-encoder-emulation-zero-mark-position) using an acyclic read request.

###### Additional parameters

---

##### Zero mark emulation (SINAMICS mode)

The referencing mode set for the leading encoder is used to determine the zero mark position for the zero mark emulation of the TM41.

Possible referencing modes are:

- Homing to the zero position of the encoder

  - Encoder zero mark of an incremental encoder
  - Zero passage of the singleturn position of an absolute encoder
  - Pole pitch of the resolver
- Homing to the zero position of the encoder with selection of the correct zero position using a BERO switching signal (CU parameter [p0493](SINAMICS%20Parameter%20SERVO.md#p04930n-zero-mark-selection-input-terminal-1))
- Homing to an external zero mark connected via an input terminal (CU parameter [p0495](SINAMICS%20Parameter%20SERVO.md#p049502-equivalent-zero-mark-input-terminal-1))

> **Note**
>
> **Original encoder with several zero marks**
>
> If the original encoder (leading encoder) has several zero marks/positions, an additional condition (BERO signal) must be selected for the required zero mark.

###### Adjustable zero mark offset at the TM41 output

An offset of the pulse grid can be set for the the zero mark position of the encoder emulation using [p4426](SINAMICS%20Parameter%20TM41%20%28Terminal%20Module%29.md#p4426-tm41-encoder-emulation-pulses-for-zero-mark).

###### Example of a pulse number step-up ratio

The leading encoder emits 12 pulses and a zero mark per revolution. However, the application requires 32 pulses per revolution. By setting [p4408](SINAMICS%20Parameter%20TM41%20%28Terminal%20Module%29.md#p4408-tm41-encoder-emulation-pulse-number-leading-encoder) and [p4418](SINAMICS%20Parameter%20TM41%20%28Terminal%20Module%29.md#p4418-tm41-encoder-emulation-fine-resolution-leading-encoder), the required 32 pulses per revolution are available at X520 of the TM41.

![Step-up ratio of the encoder pulse number](images/147827324683_DV_resource.Stream@PNG-en-US.png)

Step-up ratio of the encoder pulse number

###### Example of a pulse number step-up ratio with several zero positions

If the original encoder has several zero positions/marks per revolution (e.g. resolver with several pole pairs), the correct zero mark must be selected via an additional condition. Otherwise, there is no reproducible relationship between the position of the original encoder and the zero mark position of the encoder emulation.

![Step-up ratio with several zero positions per revolution](images/147827353099_DV_resource.Stream@PNG-en-US.png)

Step-up ratio with several zero positions per revolution

###### Parameterization

The pulse numbers of the leading encoder (the signal source) are set using p4408 and p4418. To synchronize the generated zero mark with the zero mark of the leading encoder, the pulse number per encoder revolution of the encoder at the TM41 input (p4408) must always precisely coincide with the pulse number per encoder revolution of the encoder interconnected at connector input [p4420](SINAMICS%20Parameter%20TM41%20%28Terminal%20Module%29.md#p4420-ci-tm41-encoder-emulation-position-setpoint).

The pulse numbers emulated by the TM41 are set using [p0408](SINAMICS%20Parameter%20SERVO.md#p04080n-rotary-encoder-pulse-number) and [p0418](SINAMICS%20Parameter%20SERVO.md#p04180n-fine-resolution-gx_xist1-in-bits). If p4408 = 0 is set then the values from p0408 and p0418 also apply for the output of the TM41.

###### Diagnostic options

Parameter [r4419](SINAMICS%20Parameter%20TM41%20%28Terminal%20Module%29.md#r4419-tm41-encoder-emulation-diagnostics-position-setpoint) shows the calculated position setpoint after the step-up/step-down. Using the trace function of your commissioning tool, you can check the step-up/step-down function based on r4419.

###### Enabling the zero mark output of the TM41

For [p4401](SINAMICS%20Parameter%20TM41%20%28Terminal%20Module%29.md#p4401-tm41-encoder-emulation-mode).1 = 1, the zero mark from the leading encoder is also output from the TM41. For p4401.1 = 0, TM41 outputs the zero pulse at the position at which the TM41 was located when switching on.

###### Additional parameters

---

##### TM41 Setpoint Filter

###### Description

You can parameterize the setpoint filter (PT2 low-pass) here.

**Filter effective ([p1414](SINAMICS%20Parameter%20SERVO.md#p14140n-speed-setpoint-filter-activation-1))**

- Click this option to activate the filter.

**Filter parameter**

1. At "Denominator frequency" ([p1417](SINAMICS%20Parameter%20SERVO.md#p14170n-speed-setpoint-filter-1-denominator-natural-frequency-1)), enter the frequency for the speed setpoint filter of the pulse encoder emulation.
2. At "Denominator damping" ([p1418](SINAMICS%20Parameter%20SERVO.md#p14180n-speed-setpoint-filter-1-denominator-damping-1)), enter the denominator damping for the speed setpoint filter of the pulse encoder emulation.

###### Function diagrams (FD)

- Terminal Module 41 (TM41) - Incremental encoder emulation (p4400 = 0) - 9674 -
- Terminal Module 41 (TM41) - Incremental encoder emulation (p4400 = 1) - 9676 -

###### Additional parameters

---

##### X520 Encoder Interface

###### Description

Terminal X520 is the output interface for the pulse encoder emulation.

Pin assignment of the interface:

| Pin | Signal name | Technical specifications |
| --- | --- | --- |
| 1 | A | Incremental signal A |
| 2 | R | Reference signal R |
| 3 | B | Incremental signal B |
| 4 | Reserved, do not use |  |
| 5 | Reserved, do not use |  |
| 6 | A* | Inverse incremental signal A |
| 7 | R* | Inverse reference signal R |
| 8 | B* | Inverse incremental signal B |
| 9 | M | Ground |

### TM41 control logic

The interconnections for control/status words of the faults and alarms are displayed and can be edited here.

#### Parameterizing the control logic

1. Select in the drop-down list of the "Control logic" screen form which status words (r2139) or control words (r2138) should be displayed so they can then be interconnected.
2. Then interconnect the individual bits of the status and control words displayed in the screen form.

   A green LED indicates that the corresponding bit of the control or status word is set. If the bit value of the control or status word results from the logical interconnection of several signal sources, the type of the logical interconnection is displayed by the associated logic symbol.

#### Function diagrams (FD)

- Internal control/status words - Control word faults/alarms - 2546 -
- Internal control/status words - Status word faults/alarms 1 and 2 - 2548 -

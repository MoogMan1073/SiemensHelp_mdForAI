---
title: "TM31 Terminal Module"
package: stdrui200000enUS
topics: 20
source: Siemens TIA Portal Information System (offline help, en-US)
---


# TM31 Terminal Module

This section contains information on the following topics:

- [TM31 Overview](#tm31-overview)
- [Parameterize TM31](#parameterize-tm31)

## TM31 Overview

This section contains information on the following topics:

- [TM31 Description](#tm31-description)
- [TM31 Interfaces](#tm31-interfaces)

### TM31 Description

#### Description

The TM31 Terminal Module is a terminal expansion module for snapping on to a standard mounting rail according to EN 50022. The TM31 increases the number of available digital inputs/outputs within a drive system, see also [TM31 Interfaces](#tm31-interfaces).

TM31 Terminal Modules are connected via DRIVE-CLiQ, are inserted via the project navigator after the drive configuration or automatically via a configuration macro (SINAMICS G) and displayed correspondingly in the topology.

### TM31 Interfaces

#### Description

![TM31 Interfaces](images/147822283531_DV_resource.Stream@PNG-en-US.png)

TM31 Interfaces

---

**See also**

[TM31 Description](#tm31-description)

## Parameterize TM31

This section contains information on the following topics:

- [Parameterize Inputs/Outputs](#parameterize-inputsoutputs)
- [TM31 control logic](#tm31-control-logic)

### Parameterize Inputs/Outputs

This section contains information on the following topics:

- [TM31 Inputs/Outputs](#tm31-inputsoutputs)
- [TM31 Analog Inputs](#tm31-analog-inputs)
- [TM31 Analog Outputs](#tm31-analog-outputs)
- [TM31 Digital Inputs](#tm31-digital-inputs)
- [TM31 Bidirectional Digital Inputs/Outputs](#tm31-bidirectional-digital-inputsoutputs)
- [TM31 Relay Outputs](#tm31-relay-outputs)
- [TM31 temperature sensor input](#tm31-temperature-sensor-input)

#### TM31 Inputs/Outputs

##### Description

The TM31 option module has the following input/outputs:

- 8 [Digital inputs](#isolated-tm31-digital-inputs)
- 4 [Digital inputs/outputs](#tm31-bidirectional-digital-inputsoutputs-1)
- 2 [Analog inputs](#tm31-analog-inputs-1)
- 2 [Analog outputs](#tm31-analog-outputs-1)
- 2 [Relay outputs](#tm31-relay-outputs-1)
- 1 [Thermistor input](#tm31-temperature-sensor)

#### TM31 Analog Inputs

This section contains information on the following topics:

- [TM31 Analog Inputs](#tm31-analog-inputs-1)

##### TM31 Analog Inputs

In the "Analog inputs" screen form, you can change the interconnection of the analog inputs 0 and 1 on the input/output component.

- Analog inputs are used for the acquisition of external analog signals. Analog inputs are used, for example, to specify an analog definition of a speed or torque.
- Analog inputs supply a normalized analog signal (current, voltage or temperature). This analog signal is converted via the scaling to the value range -1000%...1000%. The scaling serves to adapt to the machine or to the existing components. You can define a scaling characteristic with two points. You must specify an X coordinate and a Y coordinate for each of the two points.
- Analog values are always subject to noise. You can suppress this noise with a filter. You can also smooth the input signal.

###### Parameterizing analog inputs

1. Select in the drop-down list at the top left, the configuration of the input signal for analog input 0 ([p4056](SINAMICS%20Parameter%20TM31%20%28Terminal%20Module%29%20%28sdrpa200enUS%29.md#p405601-tm31-analog-inputs-type)):

   - Unipolar voltage input (0 V...+10 V)

     The analog input is configured as voltage input.
   - Unipolar current input (0 mA...+20 mA)

     The analog input is configured as current input.
   - Monitored unipolar current input (4 mA...+20 mA)

     The analog input is configured as current input. In addition, "wire-break monitoring" is active.
   - Bipolar voltage input (-10 V...+10 V)

     The analog input is configured as voltage input. The input range is +/-10 V.
   - Bipolar current input (-20 mA...+20 mA)

     The analog input is configured as current input. The input range is +/-20 mA.
2. Correct in the "Offset" ([p4063](SINAMICS%20Parameter%20TB30%20%28Terminal%20Board%29%20%28sdrpa100enUS%29.md#p406301-tb30-analog-inputs-offset)) field the specified voltage value of the offset.

   The offset is added to the value of the input signal prior to scaling.
3. If you want to invert the analog signal, interconnect the signal source in the "Inversion" ([p4067](SINAMICS%20Parameter%20TB30%20%28Terminal%20Board%29%20%28sdrpa100enUS%29.md#p406701-bi-tb30-analog-inputs-invert-signal-source)) field.

   For activated inversion, the LED illuminates green and the ![Parameterizing analog inputs](images/147822431883_DV_resource.Stream@PNG-en-US.PNG) symbol becomes visible in the interconnection.
4. To define a scaling characteristic via the scaling, click the "Scaling" button.

   The "TM31 analog input AI 0 scaling" dialog opens. Specify here the following values for the X and Y coordinates of the scaling characteristic (each for the value pair 1 and 2):

   - Characteristic value x2 ([p4059](SINAMICS%20Parameter%20TB30%20%28Terminal%20Board%29%20%28sdrpa100enUS%29.md#p405901-tb30-analog-inputs-characteristic-value-x2))
   - Characteristic value y2 ([p4060](SINAMICS%20Parameter%20TB30%20%28Terminal%20Board%29%20%28sdrpa100enUS%29.md#p406001-tb30-analog-inputs-characteristic-value-y2))
   - Characteristic value y1 ([p4058](SINAMICS%20Parameter%20TB30%20%28Terminal%20Board%29%20%28sdrpa100enUS%29.md#p405801-tb30-analog-inputs-characteristic-value-y1))
   - Characteristic value x1 ([p4057](SINAMICS%20Parameter%20TB30%20%28Terminal%20Board%29%20%28sdrpa100enUS%29.md#p405701-tb30-analog-inputs-characteristic-value-x1))

   Once you have made all the necessary settings, click the "Close" button.

   The dialog closes.
5. If you want to form the absolute value of the scaled input value, click the ![Parameterizing analog inputs](images/147822448651_DV_resource.Stream@PNG-en-US.PNG) (absolute-value generation) symbol.

   An activated inversion is indicated with the following symbol: ![Parameterizing analog inputs](images/147822452619_DV_resource.Stream@PNG-en-US.PNG)
6. To compensate temporary fluctuations of the measured value at the analog input, enter a time constant in the "Smoothing" ([p4053](SINAMICS%20Parameter%20TB30%20%28Terminal%20Board%29%20%28sdrpa100enUS%29.md#p405301-tb30-analog-inputs-smoothing-time-constant)) field.

   The larger the smoothing time constant, the slower the response of the analog input to changes in the measured value.
7. If you require a noise suppression for the input signal, enter a value in the "Noise suppression" field. The noise suppression results as follows:

   - |y-x| &gt; noise suppression   
     results in y = x: The output value is set to the current input value.
   - |y-x| ≤ noise suppression   
     results in y = y<sub>old</sub>: The output value retains its value.
8. Interconnect the "Activate" ([p4069](SINAMICS%20Parameter%20TB30%20%28Terminal%20Board%29%20%28sdrpa100enUS%29.md#p406901-bi-tb30-analog-inputs-signal-source-for-enable)) signal sink for the signal to enable the analog inputs.

   When activated, the LED next to the field illuminates green.
9. Interconnect the "Analog input 0" ([p4055](SINAMICS%20Parameter%20TB30%20%28Terminal%20Board%29%20%28sdrpa100enUS%29.md#r405501-co-tb30-analog-inputs-actual-value-in-percent)) signal sink for the input value of the analog inputs.
10. Repeat steps 1 to 9 for analog input 1.

###### Function diagrams (FD)

- Terminal Module 31 (TM31) - Analog input 0 (AI 0) - 9566 -
- Terminal Module 31 (TM31) - Analog input 1 (AI 1) - 9568 -
- Terminal Module 31 (TM31) - Overview - 9549 -

###### Additional parameters

---

#### TM31 Analog Outputs

This section contains information on the following topics:

- [TM31 analog outputs](#tm31-analog-outputs-1)

##### TM31 analog outputs

In the "Analog outputs" screen form, you can change the interconnection of the analog outputs 0 and 1 on the input/output component.

- Analog outputs are used for the output of analog variables, e.g. for diagnostic or feedback purposes on a higher-level controller.
- Absolute-value generation is possible and/or inversion of the output setpoint.
- Smoothing the output setpoint results in a suppression of setpoint peaks.
- A limiter ensures that the current and voltage lower limits (0 V, 4 mA and 0 mA) are not undershot.

###### Parameterizing analog outputs

1. Select in the drop-down list at the top left, the configuration of the input signal for analog output 0 ([p4076](SINAMICS%20Parameter%20TM31%20%28Terminal%20Module%29%20%28sdrpa200enUS%29.md#p407601-tm31-analog-outputs-type)):

   - Unipolar voltage input (0 V...+10 V)

     The analog input is configured as voltage input.
   - Unipolar current input (0 mA...+20 mA)

     The analog input is configured as current input.
   - Monitored unipolar current input (4 mA...+20 mA)

     The analog input is configured as current input. In addition, "wire-break monitoring" is active.
   - Bipolar voltage input (-10 V...+10 V)

     The analog input is configured as voltage input. The input range is +/-10 V.
   - Bipolar current input (-20 mA...+20 mA)

     The analog input is configured as current input. The input range is +/-20 mA.
2. Interconnect the "Analog output 0" ([p4071](SINAMICS%20Parameter%20TB30%20%28Terminal%20Board%29%20%28sdrpa100enUS%29.md#p407101-ci-tb30-analog-outputs-signal-source)) signal source for the analog outputs of Terminal Board 30 (TB30).
3. If you want to invert the analog signal, interconnect the signal source in the "Inversion" ([p4082](SINAMICS%20Parameter%20TB30%20%28Terminal%20Board%29%20%28sdrpa100enUS%29.md#p408201-bi-tb30-analog-outputs-invert-signal-source)) field.

   For activated inversion, the LED illuminates green and the ![Parameterizing analog outputs](images/147822431883_DV_resource.Stream@PNG-en-US.PNG) symbol becomes visible in the interconnection.
4. If you want to form the absolute value of the scaled input value, click the ![Parameterizing analog outputs](images/147822448651_DV_resource.Stream@PNG-en-US.PNG) (absolute-value generation) symbol.

   An activated inversion is indicated with the following symbol: ![Parameterizing analog outputs](images/147822452619_DV_resource.Stream@PNG-en-US.PNG)
5. To compensate temporary fluctuations of the measured value at the analog input, enter a time constant in the "Smoothing" ([p4073](SINAMICS%20Parameter%20TB30%20%28Terminal%20Board%29%20%28sdrpa100enUS%29.md#p407301-tb30-analog-outputs-smoothing-time-constant)) field.

   The larger the smoothing time constant, the slower the response of the analog input to changes in the measured value.
6. To define a scaling characteristic via the scaling, click the "Scaling" button.

   The "TB30 analog input A0 0 scaling" dialog opens. Specify here the following values for the X and Y coordinates of the scaling characteristic (each for the value pair 1 and 2):

   - Characteristic value x2 ([p4079](SINAMICS%20Parameter%20TB30%20%28Terminal%20Board%29%20%28sdrpa100enUS%29.md#p407901-tb30-analog-outputs-characteristic-value-x2))
   - Characteristic value y2 ([p4080](SINAMICS%20Parameter%20TB30%20%28Terminal%20Board%29%20%28sdrpa100enUS%29.md#p408001-tb30-analog-outputs-characteristic-value-y2))
   - Characteristic value y1 ([p4078](SINAMICS%20Parameter%20TB30%20%28Terminal%20Board%29%20%28sdrpa100enUS%29.md#p407801-tb30-analog-outputs-characteristic-value-y1))
   - Characteristic value x1 ([p4077](SINAMICS%20Parameter%20TB30%20%28Terminal%20Board%29%20%28sdrpa100enUS%29.md#p407701-tb30-analog-outputs-characteristic-value-x1))

   Once you have made all the necessary settings, click the "Close" button.

   The dialog closes.
7. Correct in the "Offset" ([p4083](SINAMICS%20Parameter%20TB30%20%28Terminal%20Board%29%20%28sdrpa100enUS%29.md#p408301-tb30-analog-outputs-offset)) field the specified voltage value of the offset.

   The offset is added to the value of the input signal prior to scaling.
8. Repeat steps 1 to 7 for analog output 1 of the Terminal Board.

###### Function diagrams (FD)

- Terminal Module 31 (TM31) - Analog outputs (AO 0 ... AO 1) - 9572 -
- Terminal Module 31 (TM31) - Overview - 9549 -

###### Additional parameters

---

#### TM31 Digital Inputs

This section contains information on the following topics:

- [Isolated TM31 digital inputs](#isolated-tm31-digital-inputs)

##### Isolated TM31 digital inputs

Digital inputs are used for the acquisition of digital signals. For example, drive enables can be controlled externally. On the "Isolated digital inputs" screen form you can change the interconnection of digital inputs 0...7 on the input/output component. If required, you can also interconnect inverted signals.

**Simulation mode**

The selection box for the terminal evaluation/simulation switchover is only visible online.

###### Parameterizing digital inputs

1. Interconnect the signal sinks for the required digital inputs or the inverted digital inputs.

   You can interconnect up to 8 digital inputs.

###### Function diagrams (FD)

- Terminal Module 31 (TM31) - Electrically isolated digital inputs (DI 0 ... DI 3) - 9550 -
- Terminal Module 31 (TM31) - Electrically isolated digital inputs (DI 4 ... DI 7) - 9552 -
- Terminal Module 31 (TM31) - Overview - 9549 -

###### Additional parameters

---

#### TM31 Bidirectional Digital Inputs/Outputs

This section contains information on the following topics:

- [TM31 bidirectional digital inputs/outputs](#tm31-bidirectional-digital-inputsoutputs-1)

##### TM31 bidirectional digital inputs/outputs

In the "TM31 bidirectional digital inputs/outputs" screen form you can change the interconnection of the bidirectional digital inputs/outputs on the input/output component.

- You can assign bidirectional digital inputs/outputs in the function. This means they can be parameterized either as an input or an output.
- Digital inputs are used for the acquisition of digital signals. For example, drive enables can be controlled externally.
- For every digital input signal there is the corresponding inverted signal which can also be used for interconnection.
- Digital outputs are used for the feedback of signals such as enables.

###### Parameterizing bidirectional digital inputs/outputs

1. If you want to simplify the view of the screen form, activate the "Optimize view" option.

   The display is then reduced to the essentials. Bidirectional digital inputs cannot be edited in the optimized view. Interconnections are still possible in every view.
2. If you want to assign digital inputs/outputs (8…11), proceed as follows:

   - Interconnect the signal sinks (r4022) for the digital inputs/outputs 0...3.
   - Interconnect the signal sinks (r4023) for the inverted digital inputs/outputs 0...3.
3. If you want to assign digital inputs (8…11), interconnect the signal sources for the digital inputs/outputs or the inverted digital inputs/outputs 8…11.

###### Function diagrams (FD)

- Terminal Module 31 (TM31) - Digital inputs/outputs, bidirectional (DI/DO 8 ... DI/DO 9) - 9560 -
- Terminal Module 31 (TM31) - Digital inputs/outputs, bidirectional (DI/DO 10 ... DI/DO 11) - 9562 -
- Terminal Module 31 (TM31) - Overview - 9549 -

#### TM31 Relay Outputs

This section contains information on the following topics:

- [TM31 Relay Outputs](#tm31-relay-outputs-1)

##### TM31 Relay Outputs

Relay outputs are used for isolated switching of signals. In the "Relay outputs" screen form, you can change the interconnection of the relay outputs 0 and 1 on the input/output component.

###### Parameterizing relay outputs

1. Interconnect the signal source for terminal DO 0 ([p4030](SINAMICS%20Parameter%20TB30%20%28Terminal%20Board%29%20%28sdrpa100enUS%29.md#p4030-bi-tb30-signal-source-for-terminal-do-0)) from which the value of the relay output 0 should be read.

   If required, invert the output via the ![Parameterizing relay outputs](images/147822448651_DV_resource.Stream@PNG-en-US.PNG) symbol.

   An activated inversion is indicated with the following symbol: ![Parameterizing relay outputs](images/147822641803_DV_resource.Stream@PNG-en-US.PNG)
2. Interconnect the signal source for terminal DO 1 ([p4031](SINAMICS%20Parameter%20TB30%20%28Terminal%20Board%29%20%28sdrpa100enUS%29.md#p4031-bi-tb30-signal-source-for-terminal-do-1)) from which the value of the relay output 1 should be read.

   If required, invert the output via the ![Parameterizing relay outputs](images/147822448651_DV_resource.Stream@PNG-en-US.PNG) symbol.

###### Function diagrams (FD)

- Terminal Module 31 (TM31) - Electrically isolated digital relay outputs (DO 0 ... DO 1) - 9556 -
- Terminal Module 31 (TM31) - Overview - 9549 -

###### Additional parameters

---

#### TM31 temperature sensor input

This section contains information on the following topics:

- [TM31 temperature sensor](#tm31-temperature-sensor)

##### TM31 temperature sensor

You can parameterize the temperature sensor input of the TM31 in the "Temperature sensor" screen form.

The TM31 acquires the actual temperature values and evaluates them. The fault and alarm thresholds ([p4102](SINAMICS%20Parameter%20SERVO.md#p410201-spindle-supplementary-temperature-fault-thresholdalarm-thresh)) of the actual temperature values can be set between -48° C and 251° C. You can also define a delay time ([p4103](SINAMICS%20Parameter%20SERVO.md#p4103-spindle-supplementary-temperature-delay-time)). The temperature sensor is connected at terminal X522.

Parameter settings for selecting alarms and faults

| Output | Alarm threshold p4102[0, 2] | Fault threshold p4102[1, 3] | Timer p4103[x] =  delay for delayed fault |
| --- | --- | --- | --- |
| Alarm only | ≤ 250° C | ≥ 251° C (= Off) | 0 |
| Fault only | ≥ 251° C (= Off) | ≤ 250° C | Any |
| Fault and alarm | ≤ 250° C | ≤ 250° C | 0 |
| Alarm with delayed fault | ≤ 250° C | ≤ 250° C | &gt; 0 ms |
| No messages | ≥ 251° C (= Off) | ≥ 251° C (= Off) | Any |

###### Parameterizing temperature sensors

1. Select in the "Sensor type" drop-down list the sensor type that you want to use.

   - [0] Evaluation disabled
   - [1] PTC thermistor
   - [2] KTY 84
   - [6] PT1000

   The interconnection of the screen form is adapted dynamically to the set sensor type.
2. The temperature evaluation for a fault and/or alarm message can be activated by clicking the two "Threshold" (p4102) buttons.

   Clicking one of the buttons changes its appearance. The field below the button shows a different temperature value as alarm threshold (p4102[0]) and fault threshold (p4102[1]).
3. Correct in the fields below the "Threshold" buttons the temperature values specified for alarm threshold (p4102[0]) and fault threshold (p4102[1]).
4. Click the "Delay" button to activate the delay time (p4103) as timer.

   The button changes its appearance.
5. Correct the value specified for the timer after which the fault should be output.
6. If required, interconnect the signal sink for the temperature signal ([p4105](SINAMICS%20Parameter%20SERVO.md#r4105-co-spindle-supplementary-temperature-actual-value)) for the TM31.
7. If required, interconnect the signal sinks for the following messages:

   - Alarm message for the Terminal Module ([p4104](SINAMICS%20Parameter%20SERVO.md#r410402-bo-spindle-supplementary-temperature-status).0)
   - Error message (fault) for the Terminal Module (p4104.1)

###### Function diagrams (FD)

- Terminal Module 31 (TM31) - Temperature evaluation - 9576 -
- Terminal Module 31 (TM31) - Overview - 9549 -

###### Additional parameters

---

### TM31 control logic

The interconnections for control/status words of the faults and alarms are displayed and can be edited here.

#### Parameterizing the control logic

1. Select in the drop-down list of the "Control logic" screen form which status words (r2139) or control words (r2138) should be displayed so they can then be interconnected.
2. Then interconnect the individual bits of the status and control words displayed in the screen form.

   A green LED indicates that the corresponding bit of the control or status word is set. If the bit value of the control or status word results from the logical interconnection of several signal sources, the type of the logical interconnection is displayed by the associated logic symbol.

#### Function diagrams (FD)

- Internal control/status words - Control word faults/alarms - 2546 -
- Internal control/status words - Status word faults/alarms 1 and 2 - 2548 -

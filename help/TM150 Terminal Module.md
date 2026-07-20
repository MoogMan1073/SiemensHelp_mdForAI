---
title: "TM150 Terminal Module"
package: stdrMVui208000enUS
topics: 9
source: Siemens TIA Portal Information System (offline help, en-US)
---


# TM150 Terminal Module

This section contains information on the following topics:

- [TM150 overview](#tm150-overview)
- [Parameterizing TM150](#parameterizing-tm150)

## TM150 overview

This section contains information on the following topics:

- [Description TM150](#description-tm150)
- [TM150 interfaces](#tm150-interfaces)

### Description TM150

#### Description

The Terminal Module TM150 is a DRIVE-CLiQ component for temperature evaluation without secure electrical separation. It can be used for motors when temperature sensors cannot be safely installed with protective separation, see also [TM150 interfaces](#tm150-interfaces). The TM150 is mounted in the control cabinet and can be snapped on to a standard mounting rail (EN 60715).

TM150 terminal modules are connected via DRIVE-CLiQ, inserted via the project navigator after drive configuration, and displayed correspondingly in the topology.

For more information, see [TM150 groups](#tm150-groups) and [TM150 temperature sensor inputs](#tm150-temperature-sensor-inputs).

#### Function block diagrams (FD)

- FD-9625 (51)
- FD-9626 (51)
- FD-9627 (51)

### TM150 interfaces

#### Description

A TM150 has the following interfaces:

- DRIVE-CLiQ interfaces
- Electronic power supply
- Temperature sensor inputs
- Shield connection
- Protective conductor connection M4/1.8 Nm
- LED

## Parameterizing TM150

This section contains information on the following topics:

- [Configuration](#configuration)
- [Inputs/outputs](#inputsoutputs)

### Configuration

This section contains information on the following topics:

- [TM150 groups](#tm150-groups)

#### TM150 groups

You can combine as groups the inputs for as many as 12 temperature channels. Each temperature sensor can occur simultaneously in all 3 groups. Each temperature channel be activated optionally.

The LED indicates the current status of the temperature sensor (green=active, gray=inactive). Only active temperature sensors are included for the calculation. The group assignment is retained for inactive temperature sensors (due to a defect, for example).

##### Parameterizing groupings

1. Call the required group (0...2) in the secondary navigation.
2. In the current group, activate the required temperature sensors (p4111[0].0 to p4111[0].11 for the 12 temperature channels).
3. If required, interconnect the following signal sinks:

   - Minimum value (p4113): Temperature minimum value of each group for the TM
   - Average value (p4114): Temperature average value of each group for the TM
   - Maximum value (p4112): Temperature maximum value of each group for the TM
4. Repeat steps 1...3 for all further groups.

##### Function diagrams (FD)

- FD-9625 (51)
- FD-9626 (51)
- FD-9627 (51)

##### Additional parameters

- r4105
- p4111
- r4113

Pxxxx

### Inputs/outputs

This section contains information on the following topics:

- [TM150 temperature sensor inputs](#tm150-temperature-sensor-inputs)

#### TM150 temperature sensor inputs

You can parameterize the temperature sensor inputs of the TM150 here. The number of temperature inputs depends on the configuration.

The TM150 acquires the actual temperature values and evaluates them. The fault and alarm thresholds (p4102) of the actual temperature values can be set between -48° C and 251° C. You can also define a delay time (p4103). The temperature sensors are connected at terminal strips X531 to X536 according to the following table.

Parameter settings for selecting alarms and faults

| Output | Alarm threshold p4102[0, 2] | Fault threshold p4102[1, 3] | Timer p4103[x] =  delay for delayed fault |
| --- | --- | --- | --- |
| Alarm only | ≤ 250° C | ≥ 251° C (= Off) | 0 |
| Fault only | ≥ 251° C (= Off) | ≤ 250° C | Any |
| Fault and alarm | ≤ 250° C | ≤ 250° C | 0 |
| Alarm with delayed fault | ≤ 250° C | ≤ 250° C | > 0 ms |
| No messages | ≥ 251° C (= Off) | ≥ 251° C (= Off) | Any |

##### Parameterizing temperature sensors

1. Select the temperature sensor in the secondary navigation.
2. Select the required measuring procedure from the "Measuring procedure" drop-down list:

   - 1x2-conductor evaluation

     The cable resistance must also be measured (see "Measuring the cable resistance").
   - 2x2-conductor evaluation

     The cable resistance must also be measured.
   - 3-conductor evaluation
   - 4-conductor evaluation
3. Select in the "Sensor type" drop-down list the sensor type that you want to use.

   - [0] Evaluation disabled
   - [1] PTC thermistor
   - [2] KTY 84
   - [4] Bimetallic NC contact
   - [5] Pt100
   - [6] Pt1000

   The interconnection of the screen form is adapted dynamically to the set sensor type.
4. Click the "Smoothing" button to activate a smoothing.

   An input field for a smoothing time constant appears below the button.
5. Enter the smoothing time constant.
6. The temperature evaluation for a fault and/or alarm message can be activated by clicking the two "Threshold" (p4102) buttons.

   Clicking one of the buttons changes its appearance. The field below the button shows a different temperature value as alarm threshold (p4102[0]) and fault threshold (p4102[1]).
7. Correct in the fields below the "Threshold" buttons the temperature values specified for alarm threshold (p4102[0]) and fault threshold (p4102[1]).
8. Click the "Delay time" button to activate the delay time (p4103) as timer.

   The button changes its appearance.
9. Correct the value specified for the timer after which the fault should be output.
10. If required, interconnect the signal sink for the temperature signal (p4105) for the TM120.
11. If required, interconnect the signal sinks for the following messages:

    - Alarm message for the Terminal Module (p4104.0)
    - Error message (fault) for the Terminal Module (p4104.1)
12. Repeat steps 1 to 11 for the other temperature sensors.

##### Measuring the cable resistance

When selecting one of the two measuring procedures "1x2-conductor evaluation" or "2x2-conductor evaluation", the cable resistance must be measured. The "Start measurement" button and an input field for the cable resistance are available for this purpose. The cable resistance measurement is only active online. Alternatively, you can also specify the cable resistance directly in the input field.

With 2-conductor evaluation, the entire cable resistance is measured and saved. During temperature evaluation, the temperature value is automatically determined on the basis of the measured cable resistance.

1. Select the 1x2- or 2x2-conductor evaluation measuring procedure for the relevant terminal block (p4108[0...5] = 0, 1).
2. Set the required sensor type for the relevant channel (p4100[x] = 1 ... 6, x = 0...5 or 0...11).
3. Bridge (short-circuit) the sensor to be connected.
4. Connect the sensor cables to the relevant terminals 1(+), 2(-) or 3(+), 4(-).
5. Start measurement of the cable resistance (p4109[x] = 1) for the relevant channel.
6. After p4109[x] = 0, check the measured resistance value in p4110[x].
7. Remove the bridging via the temperature sensor.

##### Function diagrams (FD)

- FD-9625 (51)
- FD-9626 (51)
- FD-9627 (51)

##### Additional parameters

Pxxxx

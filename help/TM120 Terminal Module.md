---
title: "TM120 Terminal Module"
package: stdrui207000enUS
topics: 8
source: Siemens TIA Portal Information System (offline help, en-US)
---


# TM120 Terminal Module

This section contains information on the following topics:

- [TM120 overview](#tm120-overview)
- [Parameterizing TM120](#parameterizing-tm120)

## TM120 overview

This section contains information on the following topics:

- [TM120 Description](#tm120-description)
- [TM120 Interfaces](#tm120-interfaces)

### TM120 Description

#### Description

The TM120 terminal module is a DRIVE-CLiQ component for safe electrically isolated temperature evaluation. It can be used for the 1FN, 1FW6 motors and motors from other manufacturers in which the installation of temperature sensors is not safely electrically isolated, see also [TM120 Interfaces](#tm120-interfaces). The TM120 is mounted in the cabinet and can be snapped on to a standard mounting rail (EN 60715).

TM120 Terminal Modules are connected via DRIVE-CLiQ, inserted via the project navigator after the drive configuration, and then displayed appropriately in the topology.

For further information, see [Configure TM120](#configure-tm120).

#### Function block diagrams (FD)

- Terminal Module 120 (TM120) - Temperature evaluation channels 0 and 1 - 9605 -
- Terminal Module 120 (TM120) - Temperature evaluation channels 2 and 3 - 9606 -

### TM120 Interfaces

#### Description

A TM120 has the following interfaces.

![TM120 Interfaces](images/147863377547_DV_resource.Stream@PNG-en-US.png)

TM120 Interfaces

## Parameterizing TM120

This section contains information on the following topics:

- [Configure TM120](#configure-tm120)
- [Inputs/outputs](#inputsoutputs)

### Configure TM120

This provides an overview of the configuration settings of the TM120.

#### Temperature sensor 0-3 interfaces

You can parameterize the interfaces of the temperature sensors via the "Temperature sensor 0-3" screen forms in the secondary navigation of the function view.

You can find additional information on the configuration of the temperature sensor inputs at [TM120 temperature sensors 0...3](#tm120-temperature-sensors-03).

#### Function diagrams (FD)

- Terminal Module 120 (TM120) - Temperature evaluation channels 0 and 1 - 9605 -
- Terminal Module 120 (TM120) - Temperature evaluation channels 2 and 3 - 9606 -

### Inputs/outputs

This section contains information on the following topics:

- [TM120 temperature sensors 0...3](#tm120-temperature-sensors-03)

#### TM120 temperature sensors 0...3

You can parameterize the temperature sensor inputs 0...3 of the TM120 here.

The TM120 acquires the actual temperature values and evaluates them. The fault and alarm thresholds ([p4102](SINAMICS%20Parameter%20SERVO.md#p410201-spindle-supplementary-temperature-fault-thresholdalarm-thresh)) of the actual temperature values can be set between -48° C and 251° C. You can also define a delay time ([p4103](SINAMICS%20Parameter%20SERVO.md#p4103-spindle-supplementary-temperature-delay-time)). The temperature sensors are connected at terminal X521.

Parameter settings for selecting alarms and faults

| Output | Alarm threshold p4102[0, 2] | Fault threshold p4102[1, 3] | Timer p4103[x] =  delay for delayed fault |
| --- | --- | --- | --- |
| Alarm only | ≤ 250° C | ≥ 251° C (= Off) | 0 |
| Fault only | ≥ 251° C (= Off) | ≤ 250° C | Any |
| Fault and alarm | ≤ 250° C | ≤ 250° C | 0 |
| Alarm with delayed fault | ≤ 250° C | ≤ 250° C | &gt; 0 ms |
| No messages | ≥ 251° C (= Off) | ≥ 251° C (= Off) | Any |

##### Parameterizing temperature sensors

1. Select the required temperature sensor channel (0...3).
2. Select in the "Sensor type" drop-down list the sensor type that you want to use.

   - [0] Evaluation disabled
   - [1] PTC thermistor
   - [2] KTY 84
   - [4] Bimetallic NC contact
   - [6] PT1000

   The interconnection of the screen form is adapted dynamically to the set sensor type.
3. The temperature evaluation for a fault and/or alarm message can be activated by clicking the two "Threshold" (p4102) buttons.

   Clicking one of the buttons changes its appearance. The field below the button shows a different temperature value as alarm threshold (p4102[0]) and fault threshold (p4102[1]).
4. Correct in the fields below the "Threshold" buttons the temperature values specified for alarm threshold (p4102[0]) and fault threshold (p4102[1]).
5. Click the "Delay" button to activate the delay time (p4103) as timer.

   The button changes its appearance.
6. Correct the value specified for the timer after which the fault should be output.
7. If required, interconnect the signal sink for the temperature signal ([p4105](SINAMICS%20Parameter%20SERVO.md#r4105-co-spindle-supplementary-temperature-actual-value)) for the TM120.
8. If required, interconnect the signal sinks for the following messages:

   - Alarm message for the Terminal Module ([p4104](SINAMICS%20Parameter%20SERVO.md#r410402-bo-spindle-supplementary-temperature-status).0)
   - Error message (fault) for the Terminal Module (p4104.1)
9. Repeat steps 1 to 8 for the other temperature sensors.

##### Function diagrams (FD)

- Terminal Module 120 (TM120) - Temperature evaluation channels 0 and 1 - 9605 -
- Terminal Module 120 (TM120) - Temperature evaluation channels 2 and 3 - 9606 -

##### Additional parameters

---

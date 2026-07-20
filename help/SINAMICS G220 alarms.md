---
title: "SINAMICS G220 alarms"
package: StdrInfSysOptAlaSinaG220enUS
topics: 2
source: Siemens TIA Portal Information System (offline help, en-US)
---


# SINAMICS G220 alarms

This section contains information on the following topics:

- [Explanation of faults and alarms](#explanation-of-faults-and-alarms)
- [SINAMICS G220 alarms](SINAMICS%20Alarms%20G220.md#sinamics-alarms-g220)
- [SINAMICS G220 Clean Power alarms](SINAMICS%20Alarms%20G220%20Clean%20Power.md#sinamics-alarms-g220-clean-power)

## Explanation of faults and alarms

The data in the following example have been chosen at random. As a maximum, a description can contain the information listed below. Depending on the message, some information can be eliminated.

### Example

![Example](images/155972832267_DV_resource.Stream@PNG-en-US.png)

### Explanation of the alarm numbers

A message comprises a letter followed by the relevant number.

The letters have the following meaning:

- A means "Alarm"
- F means "Fault"
- N means "No report" or "Internal report"
- C means "Safety message" (dedicated message buffer)

### Fault location (optional): Name

The fault location (optional), the name of the fault or alarm and the message number are all used to identify the message (e.g. with the commissioning software).

### Message class

Every message is assigned a message class using the following structure:

Message class text (number according to PROFIdrive)

The message classes are transferred at different interfaces to higher-level control systems and their associated display and operating units.

The message classes that are available are listed in the following table. In addition to the text of the message class and its number according to PROFIdrive – as well as a brief help text regarding the cause and remedy – they also include information about the various diagnostic interfaces:

- PN (hex)

  Specifies the "Channel error type" of the PROFINET channel diagnostics.

  When activating the channel diagnostics, using the GSDML file, the texts listed in the table can be displayed.
- DS1 (dec)

  Specifies the bit number in date set DS1 of the diagnostic alarm for SIMATIC S7.

  When the diagnostic alarms are activated, the texts listed in the table can be displayed.
- NAMUR (r3113.x)

  Specifies the bit number in parameter r3113.

For NAMUR interfaces, in some instances, the message classes are combined.

Message classes and coding of various diagnostic interfaces

| Message class text (number according to PROFIdrive) | Diagnostics interface |  |  |
| --- | --- | --- | --- |
| Cause and remedy | PN (hex) | DS1 (dec) | NAMUR (r3113.x) |
| **Hardware fault/software error (1)**   A hardware or software malfunction was detected.  - Carry out a POWER ON for the relevant component. - Contact the hotline if it reoccurs. | 9000 | 0 | 0 |
| **Line fault (2)**   A line supply fault has occurred (phase failure, voltage level...).  - Check the line supply/fuses. - Check the supply voltage. - Check the wiring. | 9001 | 1 | 1 |
| **Supply voltage fault (3)**   An electronics power supply fault (48 V, 24 V, 5 V, ...) was identified.  - Check the wiring. - Check the voltage level. | 9002 | 2 | 15 |
| **DC link overvoltage (4)**   The DC link voltage has assumed an inadmissibly high value.  - The dimensioning of the system (line supply, reactor, voltages). - Check the infeed settings. | 9003 | 3 | 2 |
| **Power electronics fault (5)**   An inadmissible operating state of the power electronics has been identified (overcurrent, overtemperature, IGBT failure,…).  - Check that the permissible duty cycles are complied with. - Check the ambient temperatures (fan). | 9004 | 4 | 3 |
| **Overtemperature of the electronic component (6)**   The temperature in the component has exceeded the highest permissible limit.  - Check the ambient temperature /control cabinet cooling. | 9005 | 5 | 4 |
| **Ground fault / interphase short-circuit detected (7)**   A ground fault/interphase short-circuit was detected in the power cables or in the motor windings.  - Check the power cables (connection). - Check the motor. | 9006 | 6 | 5 |
| **Motor overload (8)**   The motor was operated outside the permissible limits (temperature, current, torque…).  - Check the duty cycles and set limits. - Check the ambient temperature / motor cooling. | 9007 | 7 | 6 |
| **Communication to the higher-level control faulted (9)**   The communication to the higher-level control (internal coupling, PROFIBUS, PROFINET...) is faulted or interrupted.  - Check the state of the higher-level control system. - Check the communication connection/wiring. - Check the bus configuration/clock cycles. | 9008 | 8 | 7 |
| **Safety monitoring channel has detected an error (10)**   A safe operation monitoring function (Safety) has detected an error. | 9009 | 9 | 8 |
| **Actual position/speed value incorrect or not available (11)**   An illegal signal state has been detected while evaluating the encoder signals (track signals, zero marks, absolute values…).  - Check the encoder / state of the encoder signals. - Observe the maximum permissible frequencies. | 900A | 10 | 9 |
| **Internal (DRIVE-CLiQ) communication faulted (12)**   The internal communication between the SINAMICS components is faulted or interrupted.  - Check the DRIVE-CLiQ wiring. - Ensure an EMC-compliant design. - Observe the maximum quantity structure/clock cycles. | 900B | 11 | 10 |
| **Infeed fault (13)**   The infeed is faulted or has failed.   - Check the infeed and its environment (line supply, filters, reactors, fuses…). - Check the infeed control. | 900C | 12 | 11 |
| **Braking controller / Braking Module faulted (14)**   The internal or external Braking Module is faulted or has an overload condition (temperature).  - Check the connection/state of the Braking Module. - Comply with the permissible number of braking operations and their duration. | 900D | 13 | 15 |
| **Line filter fault (15)**   The line filter monitoring has identified an excessively high temperature or other inadmissible state.  - Check the temperature / temperature monitoring. - Check the configuration to ensure that it is permissible (filter type, infeed, thresholds). | 900E | 14 | 15 |
| **External measured value / signal state outside of the permissible range (16)**   A measured value / signal state read in via the input area (digital/analog/temperature) has assumed an inadmissible value/state.  - Determine and check the relevant signal. - Check the set thresholds. | 900F | 15 | 15 |
| **Application / technological function fault (17)**   The application/technological function has exceeded a (set) limit (position, speed torque, ...).  - Determine and check the relevant limit. - Check the setpoint specified by the higher-level control system. | 9010 | 16 | 15 |
| **Error in the parameterization/configuration/commissioning procedure (18)**   An error has been identified in the parameterization or in a commissioning procedure, or the parameterization does not match the actual device configuration.  - Determine the precise cause of the fault using the commissioning tool. - Adapt the parameterization or device configuration. | 9011 | 17 | 15 |
| **General drive fault (19)**   Group fault.  - Determine the precise cause of the fault using the commissioning tool. | 9012 | 18 | 15 |
| **Auxiliary unit fault (20)**   The monitoring of an auxiliary unit (incoming transformer, cooling unit…) has identified an illegal state.  - Determine the exact cause of the fault and check the relevant device. | 9013 | 19 | 15 |

### Message value:

Provides information about the composition of the fault/alarm value.

Example:

Message value: Component number: %1, fault cause: %2

In this example, the message value contains information about the component number and cause of the fault. Entries %1 and %2 are placeholders. If the commissioning software is connected to the converter, then these placeholders are populated with the appropriate values.

### Variant

Specifies the product variant in which the message exists. This information is not applicable if an alarm is the same for all product variants.

### Component

Type of hardware component that has triggered the fault or alarm. For "None", it is not possible to assign the message to a hardware component.

### Response

Specifies the response in the event of a fault.

The following table lists the fault responses and their meanings for the entire SINAMICS drive family.

Fault responses

| List | PROFIdrive | Response | Description |
| --- | --- | --- | --- |
| NONE | – | None | No response when a fault occurs. |
| OFF1 | ON/OFF | Brake along the ramp-function generator deceleration ramp followed by pulse inhibit | **Closed-loop speed control (p1300 = 20, 21)**   - The motor is braked by immediately specifying n_set = 0 at the ramp-function generator down ramp (p1121). - The pulses are canceled once standstill has been identified. - Switching on inhibited is activated.    **Torque control (p1300 = 23)**   - The following applies for torque control:   Response as for OFF2. - When switching into torque control via r1501, the following applies:   There is no separate braking response.   The pulses are canceled once standstill has been identified. - Switching on inhibited is activated. |
| OFF1_DELAYED | – | As for OFF1; however, delayed | Faults with this fault response only take effect after the delay time in p3136 has expired.  The remaining time until OFF1 is displayed in r3137.  Switching on inhibited is activated. |
| OFF2 | COASTSTOP | Internal/external pulse inhibit | **Speed control and torque control**   - Immediate pulse cancellation, the motor "coasts down " to a standstill. - Switching on inhibited is activated. |
| OFF3 | QUICKSTOP | Braking along the OFF3 down ramp followed by pulse inhibit | **Closed-loop speed control (p1300 = 20, 21)**   - The motor is braked along the OFF3 deceleration ramp (p1135) by immediately entering n_set = 0. - The pulses are canceled once standstill has been identified. - Switching on inhibited is activated.    **Torque control (p1300 = 23)**   - Switchover to closed-loop speed controlled operation and other responses as described for closed-loop speed controlled operation. |
| STOP2 | – | STOP2 | - The motor is braked along the OFF3 deceleration ramp (p1135) by immediately entering n_set = 0. - The drive remains in closed-loop speed control. |
| IASC/DCBRK | – | – | - For synchronous motors, the following applies: An internal armature short circuit is initiated if a fault occurs with this fault response. The conditions for p1231 = 4 must be complied with. - For induction motors, the following applies: If a fault occurs with this fault response, DC braking is initiated. DC braking must have already been commissioned (p1232, p1233, p1234).  The pulses are canceled once standstill has been identified.  Switching on inhibited is activated. |
| ENCODER | – | Internal/external pulse inhibit (p0491) | The ENCODER fault response is applied depending on the setting in p0491.  Factory setting:  p0491 = 0 + encoder fault results in an OFF2   **Notice**   When changing p0491, it is imperative that you carefully observe the information provided in the description of this parameter. |

### Acknowledgment

A fault can only be acknowledged if the cause has been resolved.

The acknowledgment specifies when the fault can be acknowledged.

Acknowledging faults

| Acknowledgment | Description |
| --- | --- |
| IMMEDIATELY | Acknowledgment can be immediately realized after the cause has been resolved. |
| PULSE INHIBIT | Once the cause has been resolved, the fault can only be acknowledged when the pulses are inhibited (r0899.11 = 0). |
| POWER ON | The fault can only be acknowledged using POWER ON (the converter is switched-off/switched-on). |

> **Note**
>
> - If the cause of the fault is still not resolved, then the fault is not deleted after acknowledgement. This also applies after the converter restarts.
> - Safety Integrated faults
>
>   Function STO (Safe Torque Off) must first be deselected before acknowledging these faults.

### Explanation of the message value

Explains the possible values of the variables (%n) in the message value. In this case, detailed information can be specified regarding the cause and remedy for specific values.

### Cause:

Description of the possible causes of the fault or alarm. Optionally, a message value, fault value or alarm value can be additionally specified.

### Remedy:

Generally explains possible procedures to resolve the cause of this active fault or alarm.

> **Note**
>
> In certain cases, service or maintenance personnel are responsible for selecting a suitable method to resolve this.

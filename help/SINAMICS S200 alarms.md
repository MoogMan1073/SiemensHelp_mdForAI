---
title: "SINAMICS S200 alarms"
package: StdrInfSysOptAlaSinaS200enUS
topics: 2
source: Siemens TIA Portal Information System (offline help, en-US)
---


# SINAMICS S200 alarms

This section contains information on the following topics:

- [Explanation of faults and alarms](#explanation-of-faults-and-alarms)
- [SINAMICS S200 Basic PN alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn)
- [SINAMICS S200 PN alarms](SINAMICS%20Alarms%20S200%20PN.md#sinamics-alarms-s200-pn)

## Explanation of faults and alarms

The data in the following example have been chosen at random. As a maximum, a description can contain the information listed below. Depending on the message, some information can be eliminated.

### Example

![Example](images/163075008011_DV_resource.Stream@PNG-en-US.png)

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

  Specifies the "Channel Error Type" of the PROFINET channel diagnostics.

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
| **Communication to the higher-level control faulted (9)**   The communication to the higher-level control (internal coupling, PROFINET...) is faulted or interrupted.  - Check the state of the higher-level control system. - Check the communication connection/wiring. - Check the bus configuration/clock cycles. | 9008 | 8 | 7 |
| **Safety monitoring channel has detected an error (10)**   A safe operation monitoring function (Safety) has detected an error. | 9009 | 9 | 8 |
| **Actual position/speed value incorrect or not available (11)**   An illegal signal state has been detected while evaluating the encoder signals (track signals, zero marks, absolute values…).  - Check the encoder / state of the encoder signals. - Observe the maximum permissible frequencies. | 900A | 10 | 9 |
| **Internal (DRIVE-CLiQ) communication faulted (12)**   The internal communication between the SINAMICS components is faulted or interrupted.  - Check the DRIVE-CLiQ wiring. - Ensure an EMC-compliant design. - Observe the maximum quantity structure/clock cycles. | 900B | 11 | 10 |
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

### Cause:

Description of the possible causes of the fault or alarm. Optionally, a message value, fault value or alarm value can be additionally specified.

### Remedy:

Generally explains possible procedures to resolve the cause of this active fault or alarm.

> **Note**
>
> In certain cases, service or maintenance personnel are responsible for selecting a suitable method to resolve this.

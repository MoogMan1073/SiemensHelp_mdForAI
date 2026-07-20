---
title: "SINAMICS S/G alarms, parameters and function diagrams (up to SINAMICS firmware V5.2.x)"
package: StdrAlaParaFupS120enUS
topics: 29
source: Siemens TIA Portal Information System (offline help, en-US)
---


# SINAMICS S/G alarms, parameters and function diagrams (up to SINAMICS firmware V5.2.x)

This section contains information on the following topics:

- [SINAMICS S/G alarms (up to SINAMICS firmware V5.2.x)](#sinamics-sg-alarms-up-to-sinamics-firmware-v52x)
- [SINAMICS S210 alarms (up to SINAMICS firmware V5.2.x)](#sinamics-s210-alarms-up-to-sinamics-firmware-v52x)
- [SINAMICS S/G parameters (up to SINAMICS firmware V5.2.x)](#sinamics-sg-parameters-up-to-sinamics-firmware-v52x)
- [SINAMICS S210 parameters (up to SINAMICS firmware V5.2.x)](#sinamics-s210-parameters-up-to-sinamics-firmware-v52x)
- [SINAMICS S/G function diagrams (up to SINAMICS firmware V5.2.x)](#sinamics-sg-function-diagrams-up-to-sinamics-firmware-v52x)

## SINAMICS S/G alarms (up to SINAMICS firmware V5.2.x)

This section contains information on the following topics:

- [Explanation of faults and alarms](#explanation-of-faults-and-alarms)
- [Control Units](#control-units)
- [Servo drives](#servo-drives)
- [Vector drives](#vector-drives)
- [Infeeds](#infeeds)
- [Terminal Module](#terminal-module)

### Explanation of faults and alarms

This section contains information on the following topics:

- [General/structure](#generalstructure)
- [Explanation of fault and alarm information](#explanation-of-fault-and-alarm-information)

#### General/structure

##### Displaying faults and alarms

In the case of a fault, the drive signals the corresponding fault(s) and/or alarm(s).

For example, the following methods for displaying faults and alarms are available:

- Display via the fault and alarm buffer with PROFIBUS/PROFINET.
- Display via the commissioning software in online operation.
- Display and operating unit (e.g. BOP, AOP)

##### General structure of faults and alarms

The data in the following example have been chosen at random. The information listed below is the maximum amount of information that a description can contain. Some of the information is optionally shown.

Faults and alarms are displayed as follows:

> **Note**
>
> The following basic structure refers to S120. Other modules deviate in a few details - or some fields are simply not populated. The following example shows an S120.

![Example of faults and alarms using S120 as an example](images/120227966091_DV_resource.Stream@PNG-en-US.png)

Example of faults and alarms using S120 as an example

##### Differences between faults and alarms

The differences between faults and alarms are as follows:

| Symbol | Meaning |
| --- | --- |
| **Type** | **Description** |
| Faults | What happens when a fault occurs?  - The appropriate fault response is triggered. - Status signal ZSW1.3 is set. - The fault is entered in the fault buffer.   How are faults resolved?  - Remove the cause of the fault. - Acknowledge the fault. |
| Alarms | What happens when an alarm occurs?  - Status signal ZSW1.7 is set. - The alarm is entered into the alarm buffer.   How are alarms resolved?  - Alarms acknowledge themselves.   If the cause of the alarm is no longer present, they automatically reset themselves. |

##### Fault responses

The following table lists all fault responses and their meanings used for the entire SINAMICS drive family.

The following fault response have been defined:

|  |  |  |  |
| --- | --- | --- | --- |
| **List** | **PROFIdrive** | **Response** | **Description** |
| NONE | - | None | No response when a fault occurs.   **Note**   When the "Basic positioner" function module is activated (r0108.4 = 1), the following applies:  When a fault occurs with fault response "NONE", an active traversing task is interrupted and the system switches to tracking mode until the fault has been rectified and acknowledged. |
| OFF1 | ON/OFF | Braking along the ramp-function generator down ramp followed by pulse inhibit | **Closed-loop speed control (p1300 = 20, 21)**   - n_set = 0 is input immediately to brake the drive along the deceleration ramp (p1121). - When zero speed is detected, the motor holding brake (if parameterized) is closed (p1215). The pulses are suppressed when the brake application time (p1217) expires.   Standstill is detected when the speed actual value falls below the speed threshold (p1226) or when the monitoring time (p1227) started when speed setpoint &lt;= speed threshold (p1226) has expired.    **Torque control (p1300 = 23)**   - The following applies for closed-loop torque control:   Response as for OFF2. - When the system switches to torque control with p1501, the following applies:   No separate braking response.   If the actual speed value drops below the speed threshold (p1226) or the timer stage (p1227) has expired, the motor holding brake (if one is being used) is closed. The pulses are suppressed when the brake application time (p1217) expires. |
| OFF1_DELAYED | - | As for OFF1, however delayed | Faults with this fault response only become effective after the delay time in p3136 has expired.  The remaining time up to OFF1 is displayed in r3137. |
| OFF2 | COAST STOP | Internal/external pulse disable | **Closed-loop speed and torque control**   - Immediate pulse suppression, the drive "coasts" to a standstill. - The motor holding brake (if one is being used) is closed immediately. - Switching-on inhibited is activated. |
| OFF3 | QUICK STOP | Braking along the OFF3  down ramp followed by pulse inhibit | **Closed-loop speed control (p1300 = 20, 21)**   - n_set = 0 is input immediately to brake the drive along the OFF3 down ramp (p1135). - When zero speed is detected, the motor holding brake (if parameterized) is closed. The pulses are suppressed when the holding brake closing time (p1217) expires.   Standstill is detected when the speed actual value falls below the speed threshold (p1226) or when the monitoring time (p1227) started when speed setpoint &lt;= speed threshold (p1226) has expired. - Switching-on inhibited is activated.    **Torque control (p1300 = 23)**   - Switchover to speed-controlled operation and other responses as described for speed-controlled operation. |
| STOP2 | - | n_set = 0 | - The drive is immediately braked along the OFF3 down ramp (p1135) when n_set = 0 is entered. - The drive remains in closed-loop speed control. |
| IASC / DCBRK | - | - | - For synchronous motors, the following applies:   If a fault occurs with this fault response, an internal armature short-circuit is initiated.   The conditions for p1231 = 4 must be observed. - For induction motors, the following applies:   If a fault occurs with this fault response, DC braking is initiated.   DC braking must have been commissioned (p1232, p1233, p1234). |
| ENCODER | - | Internal/external pulse inhibit (p0491) | The fault response ENCODER acts as a function of the setting in p0491.  Factory setting:  p0491 = 0 → encoder fault causes OFF2   **Notice**!  When changing p0491, it is imperative that the information in the description of this parameter is carefully observed. |

##### Acknowledging faults

The list of faults and alarms specifies how to acknowledge each fault after the cause has been eliminated.

| Symbol | Meaning |
| --- | --- |
| **Acknowledgment** | **Description** |
| POWER ON | The fault is acknowledged by a POWER ON (switch drive unit off and on again).   **Note**   If this action has not removed the fault cause, the fault is displayed again immediately after power up. |
| IMMEDIATELY | Faults can be acknowledged at an individual drive object (Points 1 to 3) or on all drive objects (Point 4) as follows:  1. Set acknowledgment by parameter:    p3981 = 0 → 1 2. Acknowledging via binector inputs:    p2103 → BI: 1. Acknowledge faults    p2104 → BI: 2 Acknowledge faults    p2105 → BI: 3 Acknowledge faults 3. Acknowledging via a PROFIdrive control signal:    STW1.7 = 0 → 1 (signal edge) 4. Acknowledge all faults    p2102 → BI: Acknowledge all faults    All of the faults on all of the drive objects of the drive system can be acknowledged using this binector input.    **Note**   - These faults can also be acknowledged with POWER ON. - If this action has not eliminated the fault cause, the fault will continue to be displayed after acknowledgment. - Safety Integrated faults   For these faults, before acknowledgment, function "STO: Safe Torque Off must be deselected. |
| PULSE INHIBIT | The fault can only be acknowledged with a pulse inhibit (r0899.11 = 0).  The same options are available for acknowledging as described under IMMEDIATE acknowledgment. |

#### Explanation of fault and alarm information

##### Message type, message number

A message comprises a letter followed by the relevant number.

| Symbol | Meaning |
| --- | --- |
| **Axxxxx** | Alarm xxxxx |
| **Axxxxx (F, N)** | Alarm xxxxx (message type can be changed to F or N) |
| **Fxxxxx** | Fault xxxxx |
| **Fxxxxx (A, N)** | Fault xxxxx (message type can be changed to A or N) |
| **Nxxxxx** | No message |
| **Nxxxxx (A)** | No message (message type can be changed to A) |
| **Cxxxxx** | Safety message (dedicated message buffer)  Does not occur for SINAMICS MV as Safety Integrated is not used there. |

A message comprises a letter followed by the relevant number.

The meaning of the letters is as follows:

- A means "Alarm"
- F means "Fault"
- N means "No message" or "Internal message"
- C means "Safety message"

The optional brackets indicate whether the type specified for this message can be changed and which message types can be set via parameters (p2118, p2119).

Information about response and acknowledgment is specified independently for a message with changeable message type (e.g. response for F, acknowledgment for F).

> **Note**
>
> You can change the default properties of a fault or alarm by setting parameters.
>
> The "List of faults and alarm" provides information referred to the properties of a message that have been set as default. If the properties of a specific message are changed, the corresponding information may have to be modified in this list.

##### Fault location (optional): Name

The fault location (optional), the name of the fault or alarm and the message number are all used to identify the message (e.g. using the commissioning software).

##### Message value

The information provided under the message value informs you about the composition of the fault/alarm value.

Example:

Message value: Component number: %1, fault cause: %2

This message value contains information about the component number and cause of the fault. The entries %1 and %2 are placeholders, which are populated appropriately in online operation (e.g. using the commissioning software).

##### Message class

For each message, specifies the associated message class with the following structure:

Text of the message class (number according to PROFIdrive)

The message classes are transferred at different interfaces to higher-level control systems and their associated display and operating units.

The available message classes are listed in Table "Message classes and coding various diagnostic interfaces". In addition to the text of the message class and its number according to PROFIdrive – as well as a brief help text regarding the cause and remedy – they also include information about the various diagnostic interfaces:

- PN (hex)

  Specifies the "Channel error type" of the PROFINET channel diagnostics.

  When activating the channel diagnostics, using the GSDML file, the texts listed in the table can be displayed.
- DS1 (dec)

  Specifies the bit number in date set DS1 of the diagnostic alarm for SIMATIC S7.

  When the diagnostic alarms are activated, the texts listed in the table can be displayed.
- DP (dec)

  Specifies the "Error type" of the channel-related diagnostics for PROFIBUS.

  When the channel diagnostics are activated, the texts listed in the standard and the GSD file can be displayed.
- ET 200 (dec)

  Specifies the "Error type" of the channel-related diagnostics for the SIMATIC ET 200pro FC-2 device.

  When the channel diagnostics are activated, the texts listed in the standard and the GSD file of the ET 200pro can be displayed.
- NAMUR (r3113.x)

  Specifies the bit number in parameter r3113.

For interfaces DP, ET 200, NAMUR, in some instances, the message classes are combined.

Message classes and coding of various diagnostic interfaces

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Text of the message class (number according to PROFIdrive)**   Cause and remedy. | **Diagnostics interface** |  |  |  |  |
| **PN**    **(hex)** | **DS1**    **(dec)** | **DP**    **(dec)** | **ET 200**    **(dec)** | **NAMUR (r3113.x)** |  |
| **Hardware/software errors (1)**   A hardware or software malfunction was detected. Carry out a POWER ON for the relevant component. If it occurs again, contact the hotline. | 9000 | 0 | 16 | 9 | 0 |
| **Line fault (2)**   A line supply fault has occurred (phase failure, voltage level...). Check the line supply/fuses. Check the supply voltage. Check the wiring. | 9001 | 1 | 17 | 24 | 1 |
| **Supply voltage fault (3)**   An electronics supply voltage fault (48 V, 24 V, 5 V…) was detected. Check the wiring. Check the voltage level. | 9002 | 2 | 2<sup>1)</sup>  3<sup>2)</sup> | 2<sup>1)</sup>  3<sup>2)</sup> | 15 |
| **DC link overvoltage (4)**   The DC link voltage has assumed an inadmissibly high value. Check the dimensioning of the system (line supply, reactor, voltages). Check the infeed settings. | 9003 | 3 | 18 | 24 | 2 |
| **Power electronics fault (5)**   An inadmissible operating state of the power electronics has been identified (overcurrent, overtemperature, IGBT failure,…). Check compliance with the permissible load cycles. Check the ambient temperatures (fan). | 9004 | 4 | 19 | 24 | 3 |
| **Overtemperature of the electronic component (6)**   The temperature in the component has exceeded the highest permissible limit. Check the ambient temperature / control cabinet ventilation. | 9005 | 5 | 20 | 5 | 4 |
| **Ground fault / interphase short-circuit detected (7)**   A ground fault/interphase short-circuit was detected in the power cables or in the motor windings. Check the power cables (connection). Check the motor. | 9006 | 6 | 21 | 20 | 5 |
| **Motor overload (8)**   The motor was operated outside the permissible limits (temperature, current, torque…). Check the load cycles and set limits. Check the ambient temperature / motor cooling. | 9007 | 7 | 22 | 24 | 6 |
| **Communication to the higher-level controller faulted (9)**   The communication to the higher-level controller (internal coupling, PROFIBUS, PROFINET...) is faulted or interrupted. Check the state of the higher-level control system. Check the communication connection/wiring. Check the bus configuration / clock cycles. | 9008 | 8 | 23 | 19 | 7 |
| **Safety monitoring channel has detected an error (10)**   A safe operation monitoring function (Safety) has detected an error. | 9009 | 9 | 24 | 25 | 8 |
| **Actual position/speed value incorrect or not available (11)**   An illegal signal state has been detected while evaluating the encoder signals (track signals, zero marks, absolute values…). Check the encoder / state of the encoder signals. Observe the maximum permissible frequencies. | 900A | 10 | 25 | 29 | 9 |
| **Internal (DRIVE-CLiQ) communication faulted (12)**   The internal communication between the SINAMICS components is faulted or interrupted. Check the DRIVE-CLiQ wiring. Ensure an EMC-compliant design. Observe the maximum quantity structure/cycles. | 900B | 11 | 26 | 31 | 10 |
| **Infeed fault (13)**   The infeed is faulted or has failed. Check the infeed and its environment (line supply, filters, reactors, fuses…).  Check the infeed control. | 900C | 12 | 27 | 24 | 11 |
| **Braking controller / Braking Module faulted (14)**   The internal or external Braking Module is faulted or overloaded (temperature). Check the connection/state of the Braking Module. Comply with the permissible number of braking operations and their duration. | 900D | 13 | 28 | 24 | 15 |
| **Line filter fault (15)**   The line filter monitoring has identified an excessively high temperature or other inadmissible state.  Check the temperature / temperature monitoring. Check the configuration to ensure that it is permissible (filter type, infeed, thresholds). | 900E | 14 | 17 | 24 | 15 |
| **External measured value / signal state outside of the permissible range (16)**   A measured value / signal state read in via the input area (digital/analog/temperature) has assumed an inadmissible value/state. Identify and check the relevant signal. Check the set thresholds. | 900F | 15 | 29 | 26 | 15 |
| **Application / technological function fault (17)**   The application / technological function has exceeded a (set) limit (position, velocity, torque…). Identify and check the relevant limit. Check the setpoint specification of the higher-level controller. | 9010 | 16 | 30 | 9 | 15 |
| **Error in the parameterization/configuration/commissioning procedure (18)**   An error has been identified in the parameterization or in a commissioning procedure, or the parameterization does not match the actual device configuration. Determine the precise cause of the fault using the commissioning tool. Adapt the parameterization or device configuration. | 9011 | 17 | 31 | 16 | 15 |
| **General drive fault (19)**   Group fault. Determine the precise cause of the fault using the commissioning tool. | 9012 | 18 | 9 | 9 | 15 |
| **Auxiliary unit fault (20)**   The monitoring of an auxiliary unit (incoming transformer, cooling unit…) has identified an illegal state. Determine the exact cause of the fault and check the relevant device. | 9013 | 19 | 29 | 26 | 15 |
| <sup>1)</sup> Undervoltage condition of the electronics power supply   <sup>2)</sup> Overvoltage condition of the electronics power supply |  |  |  |  |  |

##### Drive object

Each message (fault/alarm) specifies the drive object in which it can be found.

A message can belong to either one, several, or all drive objects.

##### Component

Type of hardware component that has triggered the fault or alarm.

With "Component: None" it is not possible to assign the message to a hardware component.

##### Propagation

In the case of faults that are, for example, triggered by the Control Unit or a Terminal Module, central functions of the drive are also often affected. Using propagation, faults that are triggered by one drive object are therefore passed on to other drive objects.

There are the following types of propagation:

- BICO

  The fault is propagated to all active drive objects with closed-loop control functions (infeed, drive) to which there is a BICO interconnection.
- DRIVE

  The fault is propagated to all active drive objects with closed-loop control functions.
- GLOBAL

  The fault is propagated to all active drive objects.
- LOCAL

  The response of this type of propagation is dependent on parameter p3116. For binector input p3116 = 0 signal (factory setting), the following applies:

  The fault is propagated to the first active drive object with closed-loop control functions.

  For binector input p3116 = 1 signal, the following applies: The fault is not propagated.

##### Response: Default fault response (adjustable fault response)

Specifies the default response in the event of a fault.

The optional parentheses indicate whether the default fault responses can be changed and which fault responses can be adjusted using parameters (p2100, p2101).

##### Acknowledgment: Default acknowledgment (adjustable acknowledgment)

Specifies the default method of acknowledging faults after the cause has been eliminated.

The optional parentheses indicate whether the default acknowledgment can be changed, and which acknowledgment can be adjusted via parameters (p2126, p2127).

##### Cause

Describes the possible causes of the fault or alarm. A fault or alarm value can also be specified (optional).

- Fault value (r0949, format):

  The fault value is entered in the fault buffer in r0949[0...63] and specifies additional, more precise information about a fault.
- Alarm value (r2124, format):

  The alarm value specifies additional, more precise information about an alarm.

  The alarm value is entered in the alarm buffer in r2124[0...7] and specifies additional, more precise information about an alarm.

##### Remedy

Describes the methods available for eliminating the cause of the active fault or alarm.

> **Note**
>
> **Procedure to rectify the cause**
>
> On a case for case basis, service and maintenance personnel are responsible for choosing a suitable method for eliminating the cause of faults.

### Control Units

This section contains information on the following topics:

- [CU320-2 Control Unit alarms](SINAMICS%20Alarms%20SINAMICS%20I.md#sinamics-alarms-sinamics-i)

### Servo drives

This section contains information on the following topics:

- [Servo interrupts](SINAMICS%20Alarms%20SERVO.md#sinamics-alarms-servo)

### Vector drives

This section contains information on the following topics:

- [Vector alarms](SINAMICS%20Alarms%20VECTOR.md#sinamics-alarms-vector)

### Infeeds

This section contains information on the following topics:

- [Infeed interrupts](SINAMICS%20Alarms%20ACTIVE%20INFEED%20CONTROL.md#sinamics-alarms-active-infeed-control)

### Terminal Module

This section contains information on the following topics:

- [TB30 alarms](SINAMICS%20Alarms%20TB30%20%28Terminal%20Board%29%20%28sdral100enUS%29.md#sinamics-alarms-tb30-terminal-board)
- [TM15 alarms](SINAMICS%20Alarms%20TM15%20%28Terminal%20Module%20for%20SINAMICS%29%20%28sdral204enUS%29.md#sinamics-alarms-tm15-terminal-module-for-sinamics)
- [TM31 alarms](SINAMICS%20Alarms%20TM31%20%28Terminal%20Module%29%20%28sdral200enUS%29.md#sinamics-alarms-tm31-terminal-module)
- [TM41 alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module)
- [TM120 alarms](SINAMICS%20Alarms%20TM120%20%28Terminal%20Module%29.md#sinamics-alarms-tm120-terminal-module)
- [TM150 alarms](SINAMICS%20Alarms%20TM150%20%28Terminal%20Module%29%20%28sdral208enUS%29.md#sinamics-alarms-tm150-terminal-module)

## SINAMICS S210 alarms (up to SINAMICS firmware V5.2.x)

This section contains information on the following topics:

- [Explanation of faults and alarms](#explanation-of-faults-and-alarms-1)
- [SINAMICS S210 alarms (up to SINAMICS RT V5.2.x)](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210)

### Explanation of faults and alarms

This section contains information on the following topics:

- [General/structure](#generalstructure-1)
- [Explanation of fault and alarm information](#explanation-of-fault-and-alarm-information-1)

#### General/structure

##### Displaying faults and alarms

In the case of a fault, the drive signals the corresponding fault(s) and/or alarm(s).

For example, the following methods for displaying faults and alarms are available:

- Display via the fault and alarm buffer with PROFIBUS/PROFINET.
- Display via the commissioning software in online operation.
- Display and operating unit (e.g. BOP, AOP)

##### General structure of faults and alarms

The data in the following example have been chosen at random. The information listed below is the maximum amount of information that a description can contain. Some of the information is optionally shown.

Faults and alarms are displayed as follows:

> **Note**
>
> The following basic structure refers to S120. Other modules deviate in a few details - or some fields are simply not populated. The following example shows an S120.

![Example of faults and alarms using S120 as an example](images/120227966091_DV_resource.Stream@PNG-en-US.png)

Example of faults and alarms using S120 as an example

##### Differences between faults and alarms

The differences between faults and alarms are as follows:

| Symbol | Meaning |
| --- | --- |
| **Type** | **Description** |
| Faults | What happens when a fault occurs?  - The appropriate fault response is triggered. - Status signal ZSW1.3 is set. - The fault is entered in the fault buffer.   How are faults resolved?  - Remove the cause of the fault. - Acknowledge the fault. |
| Alarms | What happens when an alarm occurs?  - Status signal ZSW1.7 is set. - The alarm is entered into the alarm buffer.   How are alarms resolved?  - Alarms acknowledge themselves.   If the cause of the alarm is no longer present, they automatically reset themselves. |

##### Fault responses

The following table lists all fault responses and their meanings used for the entire SINAMICS drive family.

The following fault response have been defined:

|  |  |  |  |
| --- | --- | --- | --- |
| **List** | **PROFIdrive** | **Response** | **Description** |
| NONE | - | None | No response when a fault occurs.   **Note**   When the "Basic positioner" function module is activated (r0108.4 = 1), the following applies:  When a fault occurs with fault response "NONE", an active traversing task is interrupted and the system switches to tracking mode until the fault has been rectified and acknowledged. |
| OFF1 | ON/OFF | Braking along the ramp-function generator down ramp followed by pulse inhibit | **Closed-loop speed control (p1300 = 20, 21)**   - n_set = 0 is input immediately to brake the drive along the deceleration ramp (p1121). - When zero speed is detected, the motor holding brake (if parameterized) is closed (p1215). The pulses are suppressed when the brake application time (p1217) expires.   Standstill is detected when the speed actual value falls below the speed threshold (p1226) or when the monitoring time (p1227) started when speed setpoint &lt;= speed threshold (p1226) has expired.    **Torque control (p1300 = 23)**   - The following applies for closed-loop torque control:   Response as for OFF2. - When the system switches to torque control with p1501, the following applies:   No separate braking response.   If the actual speed value drops below the speed threshold (p1226) or the timer stage (p1227) has expired, the motor holding brake (if one is being used) is closed. The pulses are suppressed when the brake application time (p1217) expires. |
| OFF1_DELAYED | - | As for OFF1, however delayed | Faults with this fault response only become effective after the delay time in p3136 has expired.  The remaining time up to OFF1 is displayed in r3137. |
| OFF2 | COAST STOP | Internal/external pulse disable | **Closed-loop speed and torque control**   - Immediate pulse suppression, the drive "coasts" to a standstill. - The motor holding brake (if one is being used) is closed immediately. - Switching-on inhibited is activated. |
| OFF3 | QUICK STOP | Braking along the OFF3  down ramp followed by pulse inhibit | **Closed-loop speed control (p1300 = 20, 21)**   - n_set = 0 is input immediately to brake the drive along the OFF3 down ramp (p1135). - When zero speed is detected, the motor holding brake (if parameterized) is closed. The pulses are suppressed when the holding brake closing time (p1217) expires.   Standstill is detected when the speed actual value falls below the speed threshold (p1226) or when the monitoring time (p1227) started when speed setpoint &lt;= speed threshold (p1226) has expired. - Switching-on inhibited is activated.    **Torque control (p1300 = 23)**   - Switchover to speed-controlled operation and other responses as described for speed-controlled operation. |
| STOP2 | - | n_set = 0 | - The drive is immediately braked along the OFF3 down ramp (p1135) when n_set = 0 is entered. - The drive remains in closed-loop speed control. |
| IASC / DCBRK | - | - | - For synchronous motors, the following applies:   If a fault occurs with this fault response, an internal armature short-circuit is initiated.   The conditions for p1231 = 4 must be observed. - For induction motors, the following applies:   If a fault occurs with this fault response, DC braking is initiated.   DC braking must have been commissioned (p1232, p1233, p1234). |
| ENCODER | - | Internal/external pulse inhibit (p0491) | The fault response ENCODER acts as a function of the setting in p0491.  Factory setting:  p0491 = 0 → encoder fault causes OFF2   **Notice**!  When changing p0491, it is imperative that the information in the description of this parameter is carefully observed. |

##### Acknowledging faults

The list of faults and alarms specifies how to acknowledge each fault after the cause has been eliminated.

| Symbol | Meaning |
| --- | --- |
| **Acknowledgment** | **Description** |
| POWER ON | The fault is acknowledged by a POWER ON (switch drive unit off and on again).   **Note**   If this action has not removed the fault cause, the fault is displayed again immediately after power up. |
| IMMEDIATELY | Faults can be acknowledged at an individual drive object (Points 1 to 3) or on all drive objects (Point 4) as follows:  1. Set acknowledgment by parameter:    p3981 = 0 → 1 2. Acknowledging via binector inputs:    p2103 → BI: 1. Acknowledge faults    p2104 → BI: 2 Acknowledge faults    p2105 → BI: 3 Acknowledge faults 3. Acknowledging via a PROFIdrive control signal:    STW1.7 = 0 → 1 (signal edge) 4. Acknowledge all faults    p2102 → BI: Acknowledge all faults    All of the faults on all of the drive objects of the drive system can be acknowledged using this binector input.    **Note**   - These faults can also be acknowledged with POWER ON. - If this action has not eliminated the fault cause, the fault will continue to be displayed after acknowledgment. - Safety Integrated faults   For these faults, before acknowledgment, function "STO: Safe Torque Off must be deselected. |
| PULSE INHIBIT | The fault can only be acknowledged with a pulse inhibit (r0899.11 = 0).  The same options are available for acknowledging as described under IMMEDIATE acknowledgment. |

#### Explanation of fault and alarm information

##### Message type, message number

A message comprises a letter followed by the relevant number.

| Symbol | Meaning |
| --- | --- |
| **Axxxxx** | Alarm xxxxx |
| **Axxxxx (F, N)** | Alarm xxxxx (message type can be changed to F or N) |
| **Fxxxxx** | Fault xxxxx |
| **Fxxxxx (A, N)** | Fault xxxxx (message type can be changed to A or N) |
| **Nxxxxx** | No message |
| **Nxxxxx (A)** | No message (message type can be changed to A) |
| **Cxxxxx** | Safety message (dedicated message buffer)  Does not occur for SINAMICS MV as Safety Integrated is not used there. |

A message comprises a letter followed by the relevant number.

The meaning of the letters is as follows:

- A means "Alarm"
- F means "Fault"
- N means "No message" or "Internal message"
- C means "Safety message"

The optional brackets indicate whether the type specified for this message can be changed and which message types can be set via parameters (p2118, p2119).

Information about response and acknowledgment is specified independently for a message with changeable message type (e.g. response for F, acknowledgment for F).

> **Note**
>
> You can change the default properties of a fault or alarm by setting parameters.
>
> The "List of faults and alarm" provides information referred to the properties of a message that have been set as default. If the properties of a specific message are changed, the corresponding information may have to be modified in this list.

##### Fault location (optional): Name

The fault location (optional), the name of the fault or alarm and the message number are all used to identify the message (e.g. using the commissioning software).

##### Message value

The information provided under the message value informs you about the composition of the fault/alarm value.

Example:

Message value: Component number: %1, fault cause: %2

This message value contains information about the component number and cause of the fault. The entries %1 and %2 are placeholders, which are populated appropriately in online operation (e.g. using the commissioning software).

##### Message class

For each message, specifies the associated message class with the following structure:

Text of the message class (number according to PROFIdrive)

The message classes are transferred at different interfaces to higher-level control systems and their associated display and operating units.

The available message classes are listed in Table "Message classes and coding various diagnostic interfaces". In addition to the text of the message class and its number according to PROFIdrive – as well as a brief help text regarding the cause and remedy – they also include information about the various diagnostic interfaces:

- PN (hex)

  Specifies the "Channel error type" of the PROFINET channel diagnostics.

  When activating the channel diagnostics, using the GSDML file, the texts listed in the table can be displayed.
- DS1 (dec)

  Specifies the bit number in date set DS1 of the diagnostic alarm for SIMATIC S7.

  When the diagnostic alarms are activated, the texts listed in the table can be displayed.
- DP (dec)

  Specifies the "Error type" of the channel-related diagnostics for PROFIBUS.

  When the channel diagnostics are activated, the texts listed in the standard and the GSD file can be displayed.
- ET 200 (dec)

  Specifies the "Error type" of the channel-related diagnostics for the SIMATIC ET 200pro FC-2 device.

  When the channel diagnostics are activated, the texts listed in the standard and the GSD file of the ET 200pro can be displayed.
- NAMUR (r3113.x)

  Specifies the bit number in parameter r3113.

For interfaces DP, ET 200, NAMUR, in some instances, the message classes are combined.

Message classes and coding of various diagnostic interfaces

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Text of the message class (number according to PROFIdrive)**   Cause and remedy. | **Diagnostics interface** |  |  |  |  |
| **PN**    **(hex)** | **DS1**    **(dec)** | **DP**    **(dec)** | **ET 200**    **(dec)** | **NAMUR (r3113.x)** |  |
| **Hardware/software errors (1)**   A hardware or software malfunction was detected. Carry out a POWER ON for the relevant component. If it occurs again, contact the hotline. | 9000 | 0 | 16 | 9 | 0 |
| **Line fault (2)**   A line supply fault has occurred (phase failure, voltage level...). Check the line supply/fuses. Check the supply voltage. Check the wiring. | 9001 | 1 | 17 | 24 | 1 |
| **Supply voltage fault (3)**   An electronics supply voltage fault (48 V, 24 V, 5 V…) was detected. Check the wiring. Check the voltage level. | 9002 | 2 | 2<sup>1)</sup>  3<sup>2)</sup> | 2<sup>1)</sup>  3<sup>2)</sup> | 15 |
| **DC link overvoltage (4)**   The DC link voltage has assumed an inadmissibly high value. Check the dimensioning of the system (line supply, reactor, voltages). Check the infeed settings. | 9003 | 3 | 18 | 24 | 2 |
| **Power electronics fault (5)**   An inadmissible operating state of the power electronics has been identified (overcurrent, overtemperature, IGBT failure,…). Check compliance with the permissible load cycles. Check the ambient temperatures (fan). | 9004 | 4 | 19 | 24 | 3 |
| **Overtemperature of the electronic component (6)**   The temperature in the component has exceeded the highest permissible limit. Check the ambient temperature / control cabinet ventilation. | 9005 | 5 | 20 | 5 | 4 |
| **Ground fault / interphase short-circuit detected (7)**   A ground fault/interphase short-circuit was detected in the power cables or in the motor windings. Check the power cables (connection). Check the motor. | 9006 | 6 | 21 | 20 | 5 |
| **Motor overload (8)**   The motor was operated outside the permissible limits (temperature, current, torque…). Check the load cycles and set limits. Check the ambient temperature / motor cooling. | 9007 | 7 | 22 | 24 | 6 |
| **Communication to the higher-level controller faulted (9)**   The communication to the higher-level controller (internal coupling, PROFIBUS, PROFINET...) is faulted or interrupted. Check the state of the higher-level control system. Check the communication connection/wiring. Check the bus configuration / clock cycles. | 9008 | 8 | 23 | 19 | 7 |
| **Safety monitoring channel has detected an error (10)**   A safe operation monitoring function (Safety) has detected an error. | 9009 | 9 | 24 | 25 | 8 |
| **Actual position/speed value incorrect or not available (11)**   An illegal signal state has been detected while evaluating the encoder signals (track signals, zero marks, absolute values…). Check the encoder / state of the encoder signals. Observe the maximum permissible frequencies. | 900A | 10 | 25 | 29 | 9 |
| **Internal (DRIVE-CLiQ) communication faulted (12)**   The internal communication between the SINAMICS components is faulted or interrupted. Check the DRIVE-CLiQ wiring. Ensure an EMC-compliant design. Observe the maximum quantity structure/cycles. | 900B | 11 | 26 | 31 | 10 |
| **Infeed fault (13)**   The infeed is faulted or has failed. Check the infeed and its environment (line supply, filters, reactors, fuses…).  Check the infeed control. | 900C | 12 | 27 | 24 | 11 |
| **Braking controller / Braking Module faulted (14)**   The internal or external Braking Module is faulted or overloaded (temperature). Check the connection/state of the Braking Module. Comply with the permissible number of braking operations and their duration. | 900D | 13 | 28 | 24 | 15 |
| **Line filter fault (15)**   The line filter monitoring has identified an excessively high temperature or other inadmissible state.  Check the temperature / temperature monitoring. Check the configuration to ensure that it is permissible (filter type, infeed, thresholds). | 900E | 14 | 17 | 24 | 15 |
| **External measured value / signal state outside of the permissible range (16)**   A measured value / signal state read in via the input area (digital/analog/temperature) has assumed an inadmissible value/state. Identify and check the relevant signal. Check the set thresholds. | 900F | 15 | 29 | 26 | 15 |
| **Application / technological function fault (17)**   The application / technological function has exceeded a (set) limit (position, velocity, torque…). Identify and check the relevant limit. Check the setpoint specification of the higher-level controller. | 9010 | 16 | 30 | 9 | 15 |
| **Error in the parameterization/configuration/commissioning procedure (18)**   An error has been identified in the parameterization or in a commissioning procedure, or the parameterization does not match the actual device configuration. Determine the precise cause of the fault using the commissioning tool. Adapt the parameterization or device configuration. | 9011 | 17 | 31 | 16 | 15 |
| **General drive fault (19)**   Group fault. Determine the precise cause of the fault using the commissioning tool. | 9012 | 18 | 9 | 9 | 15 |
| **Auxiliary unit fault (20)**   The monitoring of an auxiliary unit (incoming transformer, cooling unit…) has identified an illegal state. Determine the exact cause of the fault and check the relevant device. | 9013 | 19 | 29 | 26 | 15 |
| <sup>1)</sup> Undervoltage condition of the electronics power supply   <sup>2)</sup> Overvoltage condition of the electronics power supply |  |  |  |  |  |

##### Drive object

Each message (fault/alarm) specifies the drive object in which it can be found.

A message can belong to either one, several, or all drive objects.

##### Component

Type of hardware component that has triggered the fault or alarm.

With "Component: None" it is not possible to assign the message to a hardware component.

##### Propagation

In the case of faults that are, for example, triggered by the Control Unit or a Terminal Module, central functions of the drive are also often affected. Using propagation, faults that are triggered by one drive object are therefore passed on to other drive objects.

There are the following types of propagation:

- BICO

  The fault is propagated to all active drive objects with closed-loop control functions (infeed, drive) to which there is a BICO interconnection.
- DRIVE

  The fault is propagated to all active drive objects with closed-loop control functions.
- GLOBAL

  The fault is propagated to all active drive objects.
- LOCAL

  The response of this type of propagation is dependent on parameter p3116. For binector input p3116 = 0 signal (factory setting), the following applies:

  The fault is propagated to the first active drive object with closed-loop control functions.

  For binector input p3116 = 1 signal, the following applies: The fault is not propagated.

##### Response: Default fault response (adjustable fault response)

Specifies the default response in the event of a fault.

The optional parentheses indicate whether the default fault responses can be changed and which fault responses can be adjusted using parameters (p2100, p2101).

##### Acknowledgment: Default acknowledgment (adjustable acknowledgment)

Specifies the default method of acknowledging faults after the cause has been eliminated.

The optional parentheses indicate whether the default acknowledgment can be changed, and which acknowledgment can be adjusted via parameters (p2126, p2127).

##### Cause

Describes the possible causes of the fault or alarm. A fault or alarm value can also be specified (optional).

- Fault value (r0949, format):

  The fault value is entered in the fault buffer in r0949[0...63] and specifies additional, more precise information about a fault.
- Alarm value (r2124, format):

  The alarm value specifies additional, more precise information about an alarm.

  The alarm value is entered in the alarm buffer in r2124[0...7] and specifies additional, more precise information about an alarm.

##### Remedy

Describes the methods available for eliminating the cause of the active fault or alarm.

> **Note**
>
> **Procedure to rectify the cause**
>
> On a case for case basis, service and maintenance personnel are responsible for choosing a suitable method for eliminating the cause of faults.

## SINAMICS S/G parameters (up to SINAMICS firmware V5.2.x)

This section contains information on the following topics:

- [Explanation of parameter information](#explanation-of-parameter-information)
- [Control Units](#control-units-1)
- [Servo drives](#servo-drives-1)
- [Vector drives](#vector-drives-1)
- [Infeeds](#infeeds-1)
- [Terminal Module](#terminal-module-1)

### Explanation of parameter information

This section contains information on the following topics:

- [General/structure](#generalstructure-2)
- [Explanation of parameter information](#explanation-of-parameter-information-1)

#### General/structure

##### Basic structure of parameter information

The data in the following example have been chosen at random. The table below contains all the information that can be included in a parameter description. Some of the information is optionally shown.

> **Note**
>
> The following diagram showing the configuration refers to SINAMICS S120. For other modules, smaller deviations can occur or individual fields are simply not populated.

The "List of parameters" has the following structure:

![Example Parameterbeschr_transl](images/121419428235_DV_resource.Stream@PNG-en-US.png)

Example Parameterbeschr_transl

#### Explanation of parameter information

##### Explanation of parameter information in the parameter help

As shown in the List Manuals, the parameter help also lists a range of parameter information in abbreviated form.

A brief description of the individual types of information, and which information is used as basis, is provided below:

##### pxxxx[0...n] Parameter number

The parameter number is made up of a "p" or "r", followed by the parameter number and optionally the index or bit array.

Examples of the representation in the parameter list:

| Symbol | Meaning |
| --- | --- |
| - p... | Adjustable parameters (read and write) |
| - r... | Display parameters (read only) |
| - p0918 | Adjustable parameter 918 |
| - p0099[0...3] | Adjustable parameter 99, indices 0 to 3 |
| - p1001[0...n] | Adjustable parameter 1001, indices 0 to n (n = configurable) |
| - r0944 | Display parameter 944 |
| - r2129.0...15 | Display parameter 2129 with bit array from bit 0 (lowest bit) to bit 15 (highest bit) |

Other examples of notation in the documentation:

| Symbol | Meaning |
| --- | --- |
| - p1070[1] | Adjustable parameter 1070, index 1 |
| - p2098[1].3 | Adjustable parameter 2098, index 1 bit 3 |
| - r0945[2](3) | Display parameter 945, index 2 of drive object 3 |
| - p0795.4 | Adjustable parameter 795, bit 4 |

The following applies to adjustable parameters:

The parameter value as delivered is specified under "Factory setting" with the relevant unit in square brackets. The value can be adjusted within the range defined by "Min" and "Max".

The term "linked parameterization" is used in cases where changes to adjustable parameters affect the settings of other parameters.

Linked parameterization can occur, for example, as a result of the following actions and parameters:

- Executing macros

  p0015, p0700, p1000, p1500
- Setting the PROFIBUS telegram (BICO interconnection)

  p0922
- Setting component lists

  p0230, p0300, p0301, p0400
- Automatic calculation and pre-assignment

  p0112, p0340, p0578, p3900
- Restoring the factory settings

  p0970

The following applies to display parameters:

The fields "Min", "Max" and "Factory setting" are specified with a dash "-" and the relevant unit in square parentheses.

##### Can be changed

The "-" sign indicates that the parameter can be changed in any object state and that the change will be effective immediately.

The information "C1(x), C2(x), T, U" ((x): optional) means that the parameter can be changed only in this drive device state and that the change will not take effect until switching to another state. One or more states are possible.

The following states are possible:

|  |  |  |
| --- | --- | --- |
| - C1(x): | Device commissioning | C1: **C**ommissioning **1** |
|  | The device is being commissioned (p0009 &gt; 0).  The pulses cannot be enabled.  The parameter can only be changed in the following device commissioning settings (p0009 &gt; 0):  - C1: Can be changed for all settings p0009 &gt; 0. - C1(x): Can only be changed for settings p0009 = x.   A changed parameter value does not take effect until the device commissioning is exited with p0009 = 0. |  |
| - C2(x) | Drive object commissioning | C2: **C**ommissioning **2** |
|  | The drive is commissioned (p0009 = 0 and p0010 &gt; 0).  The pulses cannot be enabled.  The parameter can only be changed in the following drive commissioning settings (p0010 &gt; 0):  - C2: Can be changed for all settings p0010 &gt; 0. - C2(x): Can only be changed for settings p0010 = x.   A changed parameter value does not take effect until the drive commissioning mode is exited with p0010 = 0. |  |
| - U | Operation | U: R**u**n |
|  | The pulses have been enabled. |  |
| - T | Ready | T: Ready **t**o run |
|  | The pulses have not been enabled and the state "C1(x)" or "C2(x)" is not active. |  |

##### Calculated

Specifies whether the parameter is influenced by automatic calculations.

The calculation attribute defines which activities influence the parameter.

The following attributes apply:

- CALC_MOD_ALL

  p0340 = 1

  Project download with commissioning software and sending p0340 = 3
- CALC_MOD_CON

  p0340 = 1, 3, 4
- CALC_MOD_EQU

  p0340 = 1, 2
- CALC_MOD_LIM_REF

  p0340 = 1, 3, 5

  p0578 = 1
- CALC_MOD_REG

  p0340 = 1, 3

##### Access level

Specifies the minimum access level required to be able to display and change the relevant parameter. The required access level can be set using p0003.

The system uses the following access levels:

- 1: Standard
- 2: Extended
- 3: Expert
- 4: Service

##### BICO: Full parameter name / abbreviated parameter name

> **Note**
>
> Not for SINAMICS S210!

| Symbol | Meaning |
| --- | --- |
| BI: | Binector Input   This parameter selects the source of a digital signal. |
| BO: | Binector Output  This parameter is available as a digital signal for interconnection with other parameters. |
| CI: | Connector Input  This parameter selects the source of an "analog" signal. |
| CO: | Connector Output  This parameter is available as an "analog" signal for interconnection with other parameters. |
| CO/BO: | Connector/Binector Output  This parameter is available as both an "analog" and also as digital signals for interconnection with other parameters. |

> **Note**
>
> A BICO input (BI/CI) cannot be just interconnected with any BICO output (BO/CO, signal source). When interconnecting a BICO input using the commissioning software, only the corresponding possible signal sources are listed. Function diagrams 1020 ... 1030 explain the symbols for BICO parameters and how to handle BICO technology.

##### Data type

The information on the data type can comprise the following two items (separated by a slash).

- First item:

  Data type of the parameter
- Second item (for binector or connector input only)

  Data type of the signal source to be interconnected (binector/connector output).

The following data types are available for the parameters:

|  |  |  |
| --- | --- | --- |
| Integer8 | I8 | 8-bit integer |
| Integer16 | I16 | 16-bit integer |
| Integer32 | I32 | 32-bit integer |
| Unsigned8 | U8 | 8-bit without sign |
| Unsigned16 | U16 | 16-bit without sign |
| Unsigned32 | U32 | 32-bit without sign |
| FloatingPoint32 | Float | 32-bit floating-point number |

Depending on the data type of BICO input parameter (signal sink) and BICO output parameter (signal source), the following combinations are possible when creating BICO interconnections:

Possible combinations of BICO interconnections

|  |  | BICO input parameter |  |  |  |
| --- | --- | --- | --- | --- | --- |
| CI parameter |  |  | BI parameter |  |  |
| BICO output parameter |  | Unsigned32/ Integer16 | Unsigned32/ Integer32 | Unsigned32/ FloatingPoint32 | Unsigned32/ Binary |
| CO: Unsigned8 |  | x | x | – | – |
| CO: Unsigned16 |  | x | x | – | – |
| CO: Integer16 |  | x | x | r2050, r8850 | – |
| CO: Unsigned32 |  | x | x | – | – |
| CO: Integer32 |  | x | x | r2060, r8860 | – |
| CO: FloatingPoint32 |  | x | x | x | – |
| BO: Unsigned8 |  | – | – | – | x |
| BO: Unsigned16 |  | – | – | – | x |
| BO: Integer16 |  | – | – | – | x |
| BO: Unsigned32 |  | – | – | – | x |
| BO: Integer32 |  | – | – | – | x |
| BO: FloatingPoint32 |  | – | – | – | – |
| Legend: | x:   –:   rxxxx: | BICO interconnection permitted  BICO interconnection not permitted  BICO interconnection is only permitted for the specified CO parameters |  |  |  |

##### Dynamic index

For parameters with a dynamic index [0...n], the following information is specified here:

- Data set (if available).
- Parameter for the number of indices (n = number - 1).

The following information can be contained in this field:

- CDS, p0170   
  Command Data Set, CDS count

Example:

p1070[0] à main setpoint [command data set 0]

p1070[1] à main setpoint [command data set 1], etc.

- DDS, p0180  
  Drive Data Set, DDS count
- EDS, p0140  
  Encoder Data Set, EDS count
- MDS, p0130  
  Motor Data Set, MDS count
- PDS, p0120  
  Power unit Data Set, PDS count
- p2615  
  Traversing blocks count

Data sets can only be created and deleted when p0010 = 15.

##### Function diagram

The parameter is included in this function diagram. The structure of the function and its relationship with other parameters is shown in the function diagram.

##### Object (function module)

A drive object (DO) is an independent, "self-contained" functional unit that has its own parameters and, in some cases, faults and alarms.

When carrying out commissioning using the commissioning software, you can select/deselect additional functions and their parameters by activating/deactivating function modules accordingly.

The parameter list specifies the associated drive object and function module for each individual parameter.

A parameter can belong to one, several or all drive objects.

The drive object type is used to identify the drive objects in the drive system (e.g. r0107, r0975[1]).

The following information relating to "Drive object" and "Function module" can be displayed under the parameter number:

Data in the "Drive object (function module)" field

|  |  |  |
| --- | --- | --- |
| **Drive object (function module)** | **Type** | **Meaning** |
| All objects | - | This parameter is used by all drive objects. |
| A_INF | 10 | Active Infeed closed-loop control  Closed-loop controlled, self-commutated infeed/regenerative feedback unit for generating a constant DC-link voltage |
| A_INF (suppl ctrl) | - | Active Infeed with "Additional controls" function module (r0108.3) |
| A_INF (line transf) | - | Active Infeed with "Line transformer" function module (r0108.4). |
| A_INF (rec) | - | Active Infeed with "Recorder" function module (r0108.5). |
| A_INF (dyn grid support) | - | Active Infeed with "Dynamic grid support" function module (r0108.7). |
| A_INF (cos phi) |  | Active Infeed with "cosine phi" function module (r0108.10). |
| A_INF (line droop control) | - | Active Infeed with "Line droop control" function module (r0108.12). |
| A_INF (parallel) | - | Active Infeed with "Parallel connection" function module (r0108.15). |
| A_INF (master/slave) | - | Active Infeed with "Master/Slave" function module (r0108.19). |
| A_INF (SW_sts) | - | Active Infeed with "Software gating set" function module (r0108.20). |
| A_INF (brk mod ext) | - | Active Infeed with "Braking Module external" function module (r0108.26). |
| A_INF (Cooling unit) | - | Active Infeed with "Cooling unit" function module (r0108.28) |
| A_INF (PN CBE20) | - | Active Infeed with "PROFINET CBE20" function module (r0108.31). |
| B_INF | 30 | Basic Infeed closed-loop control  Unregulated line infeed unit (without regenerative feedback) for rectifying the line voltage of the DC link. |
| B_INF (Rec) | - | Basic Infeed with "Recorder" function module (r0108.5) |
| B_INF (parallel) | - | Basic Infeed with "Parallel connection" function module (r0108.15). |
| B_INF (brk mod ext) | - | Basic Infeed with "Braking Module external" function module (r0108.26). |
| B_INF (Cooling unit) | - | Basic Infeed with "Cooling unit" function module (r0108.28) |
| B_INF (PN CBE20) | - | Basic Infeed with "PROFINET CBE20" function module (r0108.31). |
| CU_I | 3 | Control Unit SINAMICS Integrated (only SIMOTION D4x5-2). |
| CU_I_D410 | 201 | Control Unit SINAMICS Integrated for SIMOTION D410-2. |
| CU_LINK | 254 | Object for Controller Extension 32 (CX32). |
| CU_NX_CX | 4 | Controller Extension for boosting the processing performance |
| CU_S_AC_DP | 2 | Control Unit SINAMICS S120 AC Drive with PROFIBUS interface. |
| CU_S_AC_PN | 3 | Control Unit SINAMICS S120 AC Drive with PROFINET interface. |
| CU_S120_DP | 6 | Control Unit SINAMICS S120 with PROFIBUS interface. |
| CU_S120_DP (CAN) | - | Control Unit SINAMICS S120 with PROFIBUS interface and function module "CAN" (p0108.29). |
| CU_S120_DP (COMM BOARD) | - | Control Unit SINAMICS S120 with PROFIBUS interface and "COMM board" function module (p0108.30). |
| CU_S120_DP (PN CBE20) | - | Control Unit SINAMICS S120 with PROFIBUS interface and "PROFINET CBE20" function module (p0108.31). |
| CU_S120_PN | 4 | Control Unit SINAMICS S120 with PROFINET interface. |
| CU_S120_DP (CAN) | - | Control Unit SINAMICS S120 with PROFINET interface and function module "CAN" (p0108.29). |
| CU_S120_PN (COMM BOARD) | - | Control Unit SINAMICS S120 with PROFINET interface and "COMM board" function module (p0108.30). |
| CU_S120_PN (PN CBE20) | - | Control Unit SINAMICS S120 with PROFINET interface and "PROFINET CBE20" function module (p0108.31). |
| CU_S150_DP | 7 | Control Unit SINAMICS S150 with PROFIBUS interface. |
| CU_S150_DP (CAN) | - | Control Unit SINAMICS S150 with PROFIBUS interface and function module "CAN" (p0108.29). |
| CU_S150_DP (COMM BOARD) | - | Control Unit SINAMICS S150 with PROFIBUS interface and "COMM board" function module (p0108.30). |
| CU_S150_DP (PN CBE20) | - | Control Unit SINAMICS S150 with PROFIBUS interface and "PROFINET CBE20" function module (p0108.31). |
| CU_S150_PN | 5 | Control Unit SINAMICS S150 with PROFINET interface. |
| CU_S150_PN (CAN) | - | Control Unit SINAMICS S150 with PROFINET interface and function module "CAN" (p0108.29). |
| CU_S150_PN (COMM BOARD) | - | Control Unit SINAMICS S150 with PROFINET interface and "COMM board" function module (p0108.30). |
| CU_S150_PN (PN CBE20) | - | Control Unit SINAMICS S150 with PROFINET interface and "PROFINET CBE20" function module (p0108.31). |
| ENC | 300 | Object for a DRIVE-CLiQ encoder. |
| ENC (lin_encoder) | 300 | Object for a DRIVE-CLiQ encoder with "Linear encoder" function module (r0108.12). |
| ENC (PN CBE20) | 300 | Object for a DRIVE-CLiQ encoder with "PROFINET CBE20" function module (r0108.31). |
| HLA | 70 | Hydraulic linear drive. |
| HLA (ESR) | - | Hydraulic linear drive with "Extended Stop and Retract" function module (r0108.9). |
| HLA (PN CBE20) | - | Hydraulic linear drive with function module "PROFINET CBE20" (r0108.31). |
| HUB | 150 | DRIVE-CLiQ Hub Module. |
| R_INF | 21 | Renewable infeed control  Closed-loop controlled, self-commutated infeed/regenerative feedback unit for generating a constant DC-link voltage |
| R_INF (suppl ctrl) | - | Renewable Infeed with "Supplementary controls" function module (r0108.3) |
| R_INF (line transformer) | - | Renewable Infeed with "Line transformer" function module (r0108.4). |
| R_INF (rec) | - | Renewable infeed with "Recorder" function module (r0108.5). |
| R_INF (dyn grid support) | - | Renewable infeed with "Dynamic grid support" function module (r0108.7). |
| R_INF (cos phi) |  | Renewable infeed with "cosine phi" function module (r0108.10). |
| R_INF (line droop control) | - | Renewable Infeed with "Line droop control" function module (r0108.12). |
| R_INF (parallel) | - | Renewable Infeed with "Parallel connection" function module (r0108.15). |
| R_INF (master/slave) | - | Renewable Infeed with "Master/Slave" function module (r0108.19). |
| R_INF (SW_sts) | - | Renewable Infeed with "Software gating unit" function module (r0108.20). |
| R_INF (brk mod ext) | - | Renewable Infeed with "Braking Module external" function module (r0108.26). |
| R_INF (Cooling unit) | - | Renewable Infeed with "Cooling unit" function module (r0108.28) |
| R_INF (PN CBE20) | - | Renewable Infeed with "PROFINET CBE20" function module (r0108.31). |
| S_INF | 20 | Smart Infeed control  Unregulated line infeed/feedback unit for generating the DC-link voltage. |
| S_INF (rec) | - | Smart Infeed with "Recorder" function module (r0108.5). |
| S_INF (parallel) | - | Smart Infeed with "Parallel connection" function module (r0108.15). |
| S_INF (brk mod ext) | - | Smart Infeed with "Braking Module external" function module (r0108.26). |
| S_INF (Cooling unit) | - | Smart Infeed with "Cooling unit" function module (r0108.28). |
| S_INF (PN CBE20) | - | Smart Infeed with "PROFINET CBE20" function module (r0108.31). |
| SERVO | 11 | Servo drive. |
| SERVO (Ext M_reg) | - | Servo drive with "Extended torque control" function module (r0108.1). |
| SERVO (pos ctrl) | - | Servo drive with "Closed-loop position control" function module (r0108.3). |
| SERVO (EPOS) | - | Servo drive with "Basic positioner" function module (r0108.4). |
| SERVO (rec) | - | Servo drive with "Recorder" function module (r0108.5). |
| SERVO (DSC Spline) | - | Servo drive with function module "DSC with Spline" (r0108.6). |
| SERVO (APC) | - | Servo drive with "Advanced Positioning Control (APC)" function module (r0108.7). |
| SERVO (ext setp) | - | Servo drive with "Extended setpoint channel" function module (r0108.8). |
| SERVO (ESR) | - | Servo drive with "Extended Stop and Retract" function module (r0108.9). |
| SERVO (J_estimator) | - | Servo drive with "Moment of inertia estimator" function module (r0108.10). |
| SERVO (spin_diag) | - | Servo drive with "Spindle diagnostics" function module (r0108.11).  This function module can only be used in conjunction with a Sensor Module Integrated 24 (SMI24). |
| SERVO (Lin) | - | Servo drive with "Linear motor" function module (r0108.12). |
| SERVO (Safety rot) | - | Servo drive with "Safety rotary axis" function module (r0108.13). |
| SERVO (ext brake) | - | Servo drive with "Extended brake control" function module (r0108.14) |
| SERVO (Tech_ctrl) | - | Servo drive with "Technology controller" function module (r0108.16). |
| SERVO (ext msg) | - | Servo drive with "Extended messages/monitoring functions" function module (r0108.17). |
| SERVO (AVS/APC-ECO) | - | Servo drive with function module "Active Vibration Suppression (AVS/APC-ECO)" (r0108.19). |
| SERVO (Ext I_setp_filt) | - | Servo drive with "Extended current setpoint filter" function module (r0108.21). |
| SERVO (cogging_M_comp) | - | Servo drive with "cogging torque compensation" function module (r0108.22). |
| SERVO (Dig IO) | - | Servo drive for SINAMICS S120M with "Digital inputs/outputs" function module (r0108.23). |
| SERVO (Cooling unit) | - | Servo drive with "Cooling unit" function module (r0108.28). |
| SERVO (CAN) | - | Servo drive with "CAN" function module (r0108.29). |
| SERVO (PN CBE20) | - | Servo drive with "PROFINET CBE20" function module (r0108.31). |
| SERVO_AC | - | Servo drive for SINAMICS S120 AC Drive. |
| SERVO_I_AC | - | Servo drive for SINAMICS Integrated in SIMOTION D410-2. |
| TB30 | 100 | Terminal Board 30. |
| TM120 | 207 | Terminal Module 120. |
| TM15 | 203 | Terminal Module 15 (SIMOTION D4xx-2 only). |
| TM150 | 208 | Terminal Module 150. |
| TM15DI_DO | 204 | Terminal Module 15 (for SINAMICS). |
| TM17 | 202 | Terminal Module 17 (SIMOTION D4xx-2 only). |
| TM31 | 200 | Terminal Module 31. |
| TM41 | 201 | Terminal Module 41. |
| TM54F_MA | 205 | Terminal Module 54F Master. |
| TM54F_SL | 206 | Terminal Module 54F Slave. |
| VECTOR | 12 | Vector drive. |
| VECTOR (n/M) | - | Vector drive with "Closed-loop speed/torque control" function module (r0108.2). |
| VECTOR (pos ctrl) | - | Vector drive with "Position control" function module (r0108.3). |
| VECTOR (EPOS) | - | Vector drive with "Basic positioner" function module (r0108.4). |
| VECTOR (rec) | - | Vector drive with "Recorder" function module (r0108.5). |
| VECTOR (J_estimator) |  | Vector drive with "Moment of inertia estimator" function module (r0108.10). |
| VECTOR (Safety rot) | - | Vector drive with "Safety rotary axis" function module (r0108.13). |
| VECTOR (ext brake) | - | Vector drive with "Extended brake control" function module (r0108.14). |
| VECTOR (parallel) | - | Vector drive with "Parallel connection" function module (r0108.15). |
| VECTOR (tech_ctrl) | - | Vector drive with "Technology controller" function module (r0108.16). |
| VECTOR (Ext msg) | - | Vector drive with "Extended messages/monitoring functions" function module (r0108.17). |
| VECTOR (F3E) | - | Vector drive with "F3E power unit" function module (r0108.26).  The power unit is the PM250 for CU310-2 CRANES. |
| VECTOR (Cooling unit) | - | Vector drive with "Cooling unit" function module (r0108.28). |
| VECTOR (CAN) | - | Vector drive with "CAN" function module (r0108.29). |
| VECTOR (PN CBE20) | - | Vector drive with "PROFINET CBE20" function module (r0108.31). |
| VECTOR_AC | - | Vector drive for SINAMICS S120 AC Drive. |
| VECTOR_I_AC | - | Vector drive for SINAMICS Integrated in SIMOTION D410-2. |

##### Not for motor type

Specifies for which motor type this parameter has no significance

| Symbol | Meaning |
| --- | --- |
| ASM | Induction motor |
| PMSM | Permanent-magnet synchronous motor |
| REL | Reluctance motor textiles / SIEMOSYN motor |
| RESM | Synchronous reluctance motor |
| SESM | Separately excited synchronous motor |

##### Scaling

Specification of the reference variable with which a signal value is automatically converted with a BICO interconnection.

The following reference variables are available:

- p2000 … p2007: Reference speed, reference voltage, etc.
- PERCENT: 1.0 = 100 %
- 4000H: 4000 hex = 100 % (word) or 4000 0000 hex = 100 % (double word)
- p0514: specific scaling

##### Expert list

Specifies whether this parameter is available in the expert list of the specified drive objects in the commissioning software.

| Symbol | Meaning |
| --- | --- |
| 1: | Parameter exists in the expert list. |
| 0: | Parameter does not exist in the expert list |

> **Note**
>
> Users assume full responsibility for using parameters marked "Expert list: 0" (parameter does not exist in the expert list).
>
> These parameters and their functionalities have not been tested and no further user documentation is available for them (e.g. description of functions). Furthermore, no support is provided for these parameters by "Technical Support" (hotline).

##### Parameter values

| Symbol | Meaning |
| --- | --- |
| **Min** | Minimum value of the parameter [unit] |
| **Max** | Maximum value of the parameter [unit] |
| **Factory setting** | Value when delivered [unit]   In the case of a binector/connector input, the signal source of the default BICO interconnection is specified. A non-indexed connector output is assigned the index [0].   When commissioned for the first time, or when restoring factory settings, it is possible that another value is visible for certain parameters (e.g. p1800). Reason:   The setting of these parameters is determined by the operating environment of the Control Unit (e.g. depending on converter type, macro, Power Module). |

##### Values

List of the possible values of a parameter.

##### Recommendation

Information about recommended settings.

##### Index

The name and meaning of each individual index is specified for indexed parameters.

The following applies to the values (Min, Max, Factory setting) of indexed adjustable parameters:

- Min, Max:

  The adjustment range and unit apply to all indices.
- Factory setting:

  When all indices have the same factory setting, index 0 is specified with the unit to represent all indices.

  When the indices have different factory settings, they are all listed individually with the unit.

##### Bit array

For parameters with bit arrays, the following information is provided about each bit:

- Bit number and signal name
- Meaning for signal states 0 and 1
- Function diagram (optional)

  The signal is shown on this function diagram.

##### Dependency

Conditions that must be fulfilled in conjunction with this parameter. Also includes special interactions that can occur between this parameter and others.

- List of other relevant parameters to be considered.
- List of faults and alarms to be considered.

### Control Units

This section contains information on the following topics:

- [CU320-2 Control Unit parameters](SINAMICS%20Parameter%20CU.md#sinamics-parameter-cu)

### Servo drives

This section contains information on the following topics:

- [Servo parameters](SINAMICS%20Parameter%20SERVO.md#sinamics-parameter-servo)

### Vector drives

This section contains information on the following topics:

- [Vector parameters](SINAMICS%20Parameter%20VECTOR.md#sinamics-parameter-vector)

### Infeeds

This section contains information on the following topics:

- [Infeed parameters](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#sinamics-parameter-active-infeed-control)

### Terminal Module

This section contains information on the following topics:

- [TB30 parameters](SINAMICS%20Parameter%20TB30%20%28Terminal%20Board%29%20%28sdrpa100enUS%29.md#sinamics-parameter-tb30-terminal-board)
- [TM15 parameters](SINAMICS%20Parameter%20TM15%20%28Terminal%20Module%20for%20SINAMICS%29%20%28sdrpa204enUS%29.md#sinamics-parameter-tm15-terminal-module-for-sinamics)
- TM31 parameters
- [TM41 parameters](SINAMICS%20Parameter%20TM41%20%28Terminal%20Module%29.md#sinamics-parameter-tm41-terminal-module)
- [TM120 parameters](SINAMICS%20Parameter%20TM120%20%28Terminal%20Module%29.md#sinamics-parameter-tm120-terminal-module)
- [TM150 parameters](SINAMICS%20Parameter%20TM150%20%28Terminal%20Module%29%20%28sdrpa208enUS%29.md#sinamics-parameter-tm150-terminal-module)

## SINAMICS S210 parameters (up to SINAMICS firmware V5.2.x)

This section contains information on the following topics:

- [Explanation of parameter information](#explanation-of-parameter-information-2)
- [SINAMICS S210 parameters (up to SINAMICS RT V5.2.x)](SINAMICS%20Parameter%20SINAMICS%20S210.md#sinamics-parameter-sinamics-s210)

### Explanation of parameter information

This section contains information on the following topics:

- [General/structure](#generalstructure-3)
- [Explanation of parameter information](#explanation-of-parameter-information-3)

#### General/structure

##### Basic structure of parameter information

The data in the following example have been chosen at random. The table below contains all the information that can be included in a parameter description. Some of the information is optionally shown.

> **Note**
>
> The following diagram showing the configuration refers to SINAMICS S120. For other modules, smaller deviations can occur or individual fields are simply not populated.

The "List of parameters" has the following structure:

![Example Parameterbeschr_transl](images/121419428235_DV_resource.Stream@PNG-en-US.png)

Example Parameterbeschr_transl

#### Explanation of parameter information

##### Explanation of parameter information in the parameter help

As shown in the List Manuals, the parameter help also lists a range of parameter information in abbreviated form.

A brief description of the individual types of information, and which information is used as basis, is provided below:

##### pxxxx[0...n] Parameter number

The parameter number is made up of a "p" or "r", followed by the parameter number and optionally the index or bit array.

Examples of the representation in the parameter list:

| Symbol | Meaning |
| --- | --- |
| - p... | Adjustable parameters (read and write) |
| - r... | Display parameters (read only) |
| - p0918 | Adjustable parameter 918 |
| - p0099[0...3] | Adjustable parameter 99, indices 0 to 3 |
| - p1001[0...n] | Adjustable parameter 1001, indices 0 to n (n = configurable) |
| - r0944 | Display parameter 944 |
| - r2129.0...15 | Display parameter 2129 with bit array from bit 0 (lowest bit) to bit 15 (highest bit) |

Other examples of notation in the documentation:

| Symbol | Meaning |
| --- | --- |
| - p1070[1] | Adjustable parameter 1070, index 1 |
| - p2098[1].3 | Adjustable parameter 2098, index 1 bit 3 |
| - r0945[2](3) | Display parameter 945, index 2 of drive object 3 |
| - p0795.4 | Adjustable parameter 795, bit 4 |

The following applies to adjustable parameters:

The parameter value as delivered is specified under "Factory setting" with the relevant unit in square brackets. The value can be adjusted within the range defined by "Min" and "Max".

The term "linked parameterization" is used in cases where changes to adjustable parameters affect the settings of other parameters.

Linked parameterization can occur, for example, as a result of the following actions and parameters:

- Executing macros

  p0015, p0700, p1000, p1500
- Setting the PROFIBUS telegram (BICO interconnection)

  p0922
- Setting component lists

  p0230, p0300, p0301, p0400
- Automatic calculation and pre-assignment

  p0112, p0340, p0578, p3900
- Restoring the factory settings

  p0970

The following applies to display parameters:

The fields "Min", "Max" and "Factory setting" are specified with a dash "-" and the relevant unit in square parentheses.

##### Can be changed

The "-" sign indicates that the parameter can be changed in any object state and that the change will be effective immediately.

The information "C1(x), C2(x), T, U" ((x): optional) means that the parameter can be changed only in this drive device state and that the change will not take effect until switching to another state. One or more states are possible.

The following states are possible:

|  |  |  |
| --- | --- | --- |
| - C1(x): | Device commissioning | C1: **C**ommissioning **1** |
|  | The device is being commissioned (p0009 &gt; 0).  The pulses cannot be enabled.  The parameter can only be changed in the following device commissioning settings (p0009 &gt; 0):  - C1: Can be changed for all settings p0009 &gt; 0. - C1(x): Can only be changed for settings p0009 = x.   A changed parameter value does not take effect until the device commissioning is exited with p0009 = 0. |  |
| - C2(x) | Drive object commissioning | C2: **C**ommissioning **2** |
|  | The drive is commissioned (p0009 = 0 and p0010 &gt; 0).  The pulses cannot be enabled.  The parameter can only be changed in the following drive commissioning settings (p0010 &gt; 0):  - C2: Can be changed for all settings p0010 &gt; 0. - C2(x): Can only be changed for settings p0010 = x.   A changed parameter value does not take effect until the drive commissioning mode is exited with p0010 = 0. |  |
| - U | Operation | U: R**u**n |
|  | The pulses have been enabled. |  |
| - T | Ready | T: Ready **t**o run |
|  | The pulses have not been enabled and the state "C1(x)" or "C2(x)" is not active. |  |

##### Calculated

Specifies whether the parameter is influenced by automatic calculations.

The calculation attribute defines which activities influence the parameter.

The following attributes apply:

- CALC_MOD_ALL

  p0340 = 1

  Project download with commissioning software and sending p0340 = 3
- CALC_MOD_CON

  p0340 = 1, 3, 4
- CALC_MOD_EQU

  p0340 = 1, 2
- CALC_MOD_LIM_REF

  p0340 = 1, 3, 5

  p0578 = 1
- CALC_MOD_REG

  p0340 = 1, 3

##### Access level

Specifies the minimum access level required to be able to display and change the relevant parameter. The required access level can be set using p0003.

The system uses the following access levels:

- 1: Standard
- 2: Extended
- 3: Expert
- 4: Service

##### BICO: Full parameter name / abbreviated parameter name

> **Note**
>
> Not for SINAMICS S210!

| Symbol | Meaning |
| --- | --- |
| BI: | Binector Input   This parameter selects the source of a digital signal. |
| BO: | Binector Output  This parameter is available as a digital signal for interconnection with other parameters. |
| CI: | Connector Input  This parameter selects the source of an "analog" signal. |
| CO: | Connector Output  This parameter is available as an "analog" signal for interconnection with other parameters. |
| CO/BO: | Connector/Binector Output  This parameter is available as both an "analog" and also as digital signals for interconnection with other parameters. |

> **Note**
>
> A BICO input (BI/CI) cannot be just interconnected with any BICO output (BO/CO, signal source). When interconnecting a BICO input using the commissioning software, only the corresponding possible signal sources are listed. Function diagrams 1020 ... 1030 explain the symbols for BICO parameters and how to handle BICO technology.

##### Data type

The information on the data type can comprise the following two items (separated by a slash).

- First item:

  Data type of the parameter
- Second item (for binector or connector input only)

  Data type of the signal source to be interconnected (binector/connector output).

The following data types are available for the parameters:

|  |  |  |
| --- | --- | --- |
| Integer8 | I8 | 8-bit integer |
| Integer16 | I16 | 16-bit integer |
| Integer32 | I32 | 32-bit integer |
| Unsigned8 | U8 | 8-bit without sign |
| Unsigned16 | U16 | 16-bit without sign |
| Unsigned32 | U32 | 32-bit without sign |
| FloatingPoint32 | Float | 32-bit floating-point number |

Depending on the data type of BICO input parameter (signal sink) and BICO output parameter (signal source), the following combinations are possible when creating BICO interconnections:

Possible combinations of BICO interconnections

|  |  | BICO input parameter |  |  |  |
| --- | --- | --- | --- | --- | --- |
| CI parameter |  |  | BI parameter |  |  |
| BICO output parameter |  | Unsigned32/ Integer16 | Unsigned32/ Integer32 | Unsigned32/ FloatingPoint32 | Unsigned32/ Binary |
| CO: Unsigned8 |  | x | x | – | – |
| CO: Unsigned16 |  | x | x | – | – |
| CO: Integer16 |  | x | x | r2050, r8850 | – |
| CO: Unsigned32 |  | x | x | – | – |
| CO: Integer32 |  | x | x | r2060, r8860 | – |
| CO: FloatingPoint32 |  | x | x | x | – |
| BO: Unsigned8 |  | – | – | – | x |
| BO: Unsigned16 |  | – | – | – | x |
| BO: Integer16 |  | – | – | – | x |
| BO: Unsigned32 |  | – | – | – | x |
| BO: Integer32 |  | – | – | – | x |
| BO: FloatingPoint32 |  | – | – | – | – |
| Legend: | x:   –:   rxxxx: | BICO interconnection permitted  BICO interconnection not permitted  BICO interconnection is only permitted for the specified CO parameters |  |  |  |

##### Dynamic index

For parameters with a dynamic index [0...n], the following information is specified here:

- Data set (if available).
- Parameter for the number of indices (n = number - 1).

The following information can be contained in this field:

- CDS, p0170   
  Command Data Set, CDS count

Example:

p1070[0] à main setpoint [command data set 0]

p1070[1] à main setpoint [command data set 1], etc.

- DDS, p0180  
  Drive Data Set, DDS count
- EDS, p0140  
  Encoder Data Set, EDS count
- MDS, p0130  
  Motor Data Set, MDS count
- PDS, p0120  
  Power unit Data Set, PDS count
- p2615  
  Traversing blocks count

Data sets can only be created and deleted when p0010 = 15.

##### Function diagram

The parameter is included in this function diagram. The structure of the function and its relationship with other parameters is shown in the function diagram.

##### Object (function module)

A drive object (DO) is an independent, "self-contained" functional unit that has its own parameters and, in some cases, faults and alarms.

When carrying out commissioning using the commissioning software, you can select/deselect additional functions and their parameters by activating/deactivating function modules accordingly.

The parameter list specifies the associated drive object and function module for each individual parameter.

A parameter can belong to one, several or all drive objects.

The drive object type is used to identify the drive objects in the drive system (e.g. r0107, r0975[1]).

The following information relating to "Drive object" and "Function module" can be displayed under the parameter number:

Data in the "Drive object (function module)" field

|  |  |  |
| --- | --- | --- |
| **Drive object (function module)** | **Type** | **Meaning** |
| All objects | - | This parameter is used by all drive objects. |
| A_INF | 10 | Active Infeed closed-loop control  Closed-loop controlled, self-commutated infeed/regenerative feedback unit for generating a constant DC-link voltage |
| A_INF (suppl ctrl) | - | Active Infeed with "Additional controls" function module (r0108.3) |
| A_INF (line transf) | - | Active Infeed with "Line transformer" function module (r0108.4). |
| A_INF (rec) | - | Active Infeed with "Recorder" function module (r0108.5). |
| A_INF (dyn grid support) | - | Active Infeed with "Dynamic grid support" function module (r0108.7). |
| A_INF (cos phi) |  | Active Infeed with "cosine phi" function module (r0108.10). |
| A_INF (line droop control) | - | Active Infeed with "Line droop control" function module (r0108.12). |
| A_INF (parallel) | - | Active Infeed with "Parallel connection" function module (r0108.15). |
| A_INF (master/slave) | - | Active Infeed with "Master/Slave" function module (r0108.19). |
| A_INF (SW_sts) | - | Active Infeed with "Software gating set" function module (r0108.20). |
| A_INF (brk mod ext) | - | Active Infeed with "Braking Module external" function module (r0108.26). |
| A_INF (Cooling unit) | - | Active Infeed with "Cooling unit" function module (r0108.28) |
| A_INF (PN CBE20) | - | Active Infeed with "PROFINET CBE20" function module (r0108.31). |
| B_INF | 30 | Basic Infeed closed-loop control  Unregulated line infeed unit (without regenerative feedback) for rectifying the line voltage of the DC link. |
| B_INF (Rec) | - | Basic Infeed with "Recorder" function module (r0108.5) |
| B_INF (parallel) | - | Basic Infeed with "Parallel connection" function module (r0108.15). |
| B_INF (brk mod ext) | - | Basic Infeed with "Braking Module external" function module (r0108.26). |
| B_INF (Cooling unit) | - | Basic Infeed with "Cooling unit" function module (r0108.28) |
| B_INF (PN CBE20) | - | Basic Infeed with "PROFINET CBE20" function module (r0108.31). |
| CU_I | 3 | Control Unit SINAMICS Integrated (only SIMOTION D4x5-2). |
| CU_I_D410 | 201 | Control Unit SINAMICS Integrated for SIMOTION D410-2. |
| CU_LINK | 254 | Object for Controller Extension 32 (CX32). |
| CU_NX_CX | 4 | Controller Extension for boosting the processing performance |
| CU_S_AC_DP | 2 | Control Unit SINAMICS S120 AC Drive with PROFIBUS interface. |
| CU_S_AC_PN | 3 | Control Unit SINAMICS S120 AC Drive with PROFINET interface. |
| CU_S120_DP | 6 | Control Unit SINAMICS S120 with PROFIBUS interface. |
| CU_S120_DP (CAN) | - | Control Unit SINAMICS S120 with PROFIBUS interface and function module "CAN" (p0108.29). |
| CU_S120_DP (COMM BOARD) | - | Control Unit SINAMICS S120 with PROFIBUS interface and "COMM board" function module (p0108.30). |
| CU_S120_DP (PN CBE20) | - | Control Unit SINAMICS S120 with PROFIBUS interface and "PROFINET CBE20" function module (p0108.31). |
| CU_S120_PN | 4 | Control Unit SINAMICS S120 with PROFINET interface. |
| CU_S120_DP (CAN) | - | Control Unit SINAMICS S120 with PROFINET interface and function module "CAN" (p0108.29). |
| CU_S120_PN (COMM BOARD) | - | Control Unit SINAMICS S120 with PROFINET interface and "COMM board" function module (p0108.30). |
| CU_S120_PN (PN CBE20) | - | Control Unit SINAMICS S120 with PROFINET interface and "PROFINET CBE20" function module (p0108.31). |
| CU_S150_DP | 7 | Control Unit SINAMICS S150 with PROFIBUS interface. |
| CU_S150_DP (CAN) | - | Control Unit SINAMICS S150 with PROFIBUS interface and function module "CAN" (p0108.29). |
| CU_S150_DP (COMM BOARD) | - | Control Unit SINAMICS S150 with PROFIBUS interface and "COMM board" function module (p0108.30). |
| CU_S150_DP (PN CBE20) | - | Control Unit SINAMICS S150 with PROFIBUS interface and "PROFINET CBE20" function module (p0108.31). |
| CU_S150_PN | 5 | Control Unit SINAMICS S150 with PROFINET interface. |
| CU_S150_PN (CAN) | - | Control Unit SINAMICS S150 with PROFINET interface and function module "CAN" (p0108.29). |
| CU_S150_PN (COMM BOARD) | - | Control Unit SINAMICS S150 with PROFINET interface and "COMM board" function module (p0108.30). |
| CU_S150_PN (PN CBE20) | - | Control Unit SINAMICS S150 with PROFINET interface and "PROFINET CBE20" function module (p0108.31). |
| ENC | 300 | Object for a DRIVE-CLiQ encoder. |
| ENC (lin_encoder) | 300 | Object for a DRIVE-CLiQ encoder with "Linear encoder" function module (r0108.12). |
| ENC (PN CBE20) | 300 | Object for a DRIVE-CLiQ encoder with "PROFINET CBE20" function module (r0108.31). |
| HLA | 70 | Hydraulic linear drive. |
| HLA (ESR) | - | Hydraulic linear drive with "Extended Stop and Retract" function module (r0108.9). |
| HLA (PN CBE20) | - | Hydraulic linear drive with function module "PROFINET CBE20" (r0108.31). |
| HUB | 150 | DRIVE-CLiQ Hub Module. |
| R_INF | 21 | Renewable infeed control  Closed-loop controlled, self-commutated infeed/regenerative feedback unit for generating a constant DC-link voltage |
| R_INF (suppl ctrl) | - | Renewable Infeed with "Supplementary controls" function module (r0108.3) |
| R_INF (line transformer) | - | Renewable Infeed with "Line transformer" function module (r0108.4). |
| R_INF (rec) | - | Renewable infeed with "Recorder" function module (r0108.5). |
| R_INF (dyn grid support) | - | Renewable infeed with "Dynamic grid support" function module (r0108.7). |
| R_INF (cos phi) |  | Renewable infeed with "cosine phi" function module (r0108.10). |
| R_INF (line droop control) | - | Renewable Infeed with "Line droop control" function module (r0108.12). |
| R_INF (parallel) | - | Renewable Infeed with "Parallel connection" function module (r0108.15). |
| R_INF (master/slave) | - | Renewable Infeed with "Master/Slave" function module (r0108.19). |
| R_INF (SW_sts) | - | Renewable Infeed with "Software gating unit" function module (r0108.20). |
| R_INF (brk mod ext) | - | Renewable Infeed with "Braking Module external" function module (r0108.26). |
| R_INF (Cooling unit) | - | Renewable Infeed with "Cooling unit" function module (r0108.28) |
| R_INF (PN CBE20) | - | Renewable Infeed with "PROFINET CBE20" function module (r0108.31). |
| S_INF | 20 | Smart Infeed control  Unregulated line infeed/feedback unit for generating the DC-link voltage. |
| S_INF (rec) | - | Smart Infeed with "Recorder" function module (r0108.5). |
| S_INF (parallel) | - | Smart Infeed with "Parallel connection" function module (r0108.15). |
| S_INF (brk mod ext) | - | Smart Infeed with "Braking Module external" function module (r0108.26). |
| S_INF (Cooling unit) | - | Smart Infeed with "Cooling unit" function module (r0108.28). |
| S_INF (PN CBE20) | - | Smart Infeed with "PROFINET CBE20" function module (r0108.31). |
| SERVO | 11 | Servo drive. |
| SERVO (Ext M_reg) | - | Servo drive with "Extended torque control" function module (r0108.1). |
| SERVO (pos ctrl) | - | Servo drive with "Closed-loop position control" function module (r0108.3). |
| SERVO (EPOS) | - | Servo drive with "Basic positioner" function module (r0108.4). |
| SERVO (rec) | - | Servo drive with "Recorder" function module (r0108.5). |
| SERVO (DSC Spline) | - | Servo drive with function module "DSC with Spline" (r0108.6). |
| SERVO (APC) | - | Servo drive with "Advanced Positioning Control (APC)" function module (r0108.7). |
| SERVO (ext setp) | - | Servo drive with "Extended setpoint channel" function module (r0108.8). |
| SERVO (ESR) | - | Servo drive with "Extended Stop and Retract" function module (r0108.9). |
| SERVO (J_estimator) | - | Servo drive with "Moment of inertia estimator" function module (r0108.10). |
| SERVO (spin_diag) | - | Servo drive with "Spindle diagnostics" function module (r0108.11).  This function module can only be used in conjunction with a Sensor Module Integrated 24 (SMI24). |
| SERVO (Lin) | - | Servo drive with "Linear motor" function module (r0108.12). |
| SERVO (Safety rot) | - | Servo drive with "Safety rotary axis" function module (r0108.13). |
| SERVO (ext brake) | - | Servo drive with "Extended brake control" function module (r0108.14) |
| SERVO (Tech_ctrl) | - | Servo drive with "Technology controller" function module (r0108.16). |
| SERVO (ext msg) | - | Servo drive with "Extended messages/monitoring functions" function module (r0108.17). |
| SERVO (AVS/APC-ECO) | - | Servo drive with function module "Active Vibration Suppression (AVS/APC-ECO)" (r0108.19). |
| SERVO (Ext I_setp_filt) | - | Servo drive with "Extended current setpoint filter" function module (r0108.21). |
| SERVO (cogging_M_comp) | - | Servo drive with "cogging torque compensation" function module (r0108.22). |
| SERVO (Dig IO) | - | Servo drive for SINAMICS S120M with "Digital inputs/outputs" function module (r0108.23). |
| SERVO (Cooling unit) | - | Servo drive with "Cooling unit" function module (r0108.28). |
| SERVO (CAN) | - | Servo drive with "CAN" function module (r0108.29). |
| SERVO (PN CBE20) | - | Servo drive with "PROFINET CBE20" function module (r0108.31). |
| SERVO_AC | - | Servo drive for SINAMICS S120 AC Drive. |
| SERVO_I_AC | - | Servo drive for SINAMICS Integrated in SIMOTION D410-2. |
| TB30 | 100 | Terminal Board 30. |
| TM120 | 207 | Terminal Module 120. |
| TM15 | 203 | Terminal Module 15 (SIMOTION D4xx-2 only). |
| TM150 | 208 | Terminal Module 150. |
| TM15DI_DO | 204 | Terminal Module 15 (for SINAMICS). |
| TM17 | 202 | Terminal Module 17 (SIMOTION D4xx-2 only). |
| TM31 | 200 | Terminal Module 31. |
| TM41 | 201 | Terminal Module 41. |
| TM54F_MA | 205 | Terminal Module 54F Master. |
| TM54F_SL | 206 | Terminal Module 54F Slave. |
| VECTOR | 12 | Vector drive. |
| VECTOR (n/M) | - | Vector drive with "Closed-loop speed/torque control" function module (r0108.2). |
| VECTOR (pos ctrl) | - | Vector drive with "Position control" function module (r0108.3). |
| VECTOR (EPOS) | - | Vector drive with "Basic positioner" function module (r0108.4). |
| VECTOR (rec) | - | Vector drive with "Recorder" function module (r0108.5). |
| VECTOR (J_estimator) |  | Vector drive with "Moment of inertia estimator" function module (r0108.10). |
| VECTOR (Safety rot) | - | Vector drive with "Safety rotary axis" function module (r0108.13). |
| VECTOR (ext brake) | - | Vector drive with "Extended brake control" function module (r0108.14). |
| VECTOR (parallel) | - | Vector drive with "Parallel connection" function module (r0108.15). |
| VECTOR (tech_ctrl) | - | Vector drive with "Technology controller" function module (r0108.16). |
| VECTOR (Ext msg) | - | Vector drive with "Extended messages/monitoring functions" function module (r0108.17). |
| VECTOR (F3E) | - | Vector drive with "F3E power unit" function module (r0108.26).  The power unit is the PM250 for CU310-2 CRANES. |
| VECTOR (Cooling unit) | - | Vector drive with "Cooling unit" function module (r0108.28). |
| VECTOR (CAN) | - | Vector drive with "CAN" function module (r0108.29). |
| VECTOR (PN CBE20) | - | Vector drive with "PROFINET CBE20" function module (r0108.31). |
| VECTOR_AC | - | Vector drive for SINAMICS S120 AC Drive. |
| VECTOR_I_AC | - | Vector drive for SINAMICS Integrated in SIMOTION D410-2. |

##### Not for motor type

Specifies for which motor type this parameter has no significance

| Symbol | Meaning |
| --- | --- |
| ASM | Induction motor |
| PMSM | Permanent-magnet synchronous motor |
| REL | Reluctance motor textiles / SIEMOSYN motor |
| RESM | Synchronous reluctance motor |
| SESM | Separately excited synchronous motor |

##### Scaling

Specification of the reference variable with which a signal value is automatically converted with a BICO interconnection.

The following reference variables are available:

- p2000 … p2007: Reference speed, reference voltage, etc.
- PERCENT: 1.0 = 100 %
- 4000H: 4000 hex = 100 % (word) or 4000 0000 hex = 100 % (double word)
- p0514: specific scaling

##### Expert list

Specifies whether this parameter is available in the expert list of the specified drive objects in the commissioning software.

| Symbol | Meaning |
| --- | --- |
| 1: | Parameter exists in the expert list. |
| 0: | Parameter does not exist in the expert list |

> **Note**
>
> Users assume full responsibility for using parameters marked "Expert list: 0" (parameter does not exist in the expert list).
>
> These parameters and their functionalities have not been tested and no further user documentation is available for them (e.g. description of functions). Furthermore, no support is provided for these parameters by "Technical Support" (hotline).

##### Parameter values

| Symbol | Meaning |
| --- | --- |
| **Min** | Minimum value of the parameter [unit] |
| **Max** | Maximum value of the parameter [unit] |
| **Factory setting** | Value when delivered [unit]   In the case of a binector/connector input, the signal source of the default BICO interconnection is specified. A non-indexed connector output is assigned the index [0].   When commissioned for the first time, or when restoring factory settings, it is possible that another value is visible for certain parameters (e.g. p1800). Reason:   The setting of these parameters is determined by the operating environment of the Control Unit (e.g. depending on converter type, macro, Power Module). |

##### Values

List of the possible values of a parameter.

##### Recommendation

Information about recommended settings.

##### Index

The name and meaning of each individual index is specified for indexed parameters.

The following applies to the values (Min, Max, Factory setting) of indexed adjustable parameters:

- Min, Max:

  The adjustment range and unit apply to all indices.
- Factory setting:

  When all indices have the same factory setting, index 0 is specified with the unit to represent all indices.

  When the indices have different factory settings, they are all listed individually with the unit.

##### Bit array

For parameters with bit arrays, the following information is provided about each bit:

- Bit number and signal name
- Meaning for signal states 0 and 1
- Function diagram (optional)

  The signal is shown on this function diagram.

##### Dependency

Conditions that must be fulfilled in conjunction with this parameter. Also includes special interactions that can occur between this parameter and others.

- List of other relevant parameters to be considered.
- List of faults and alarms to be considered.

## SINAMICS S/G function diagrams (up to SINAMICS firmware V5.2.x)

This section contains information on the following topics:

- [Read function diagrams](#read-function-diagrams)
- [Function diagrams of SINAMICS CU320-2/CU310-2 drives](Function%20diagrams%20of%20SINAMICS%20CU320-2-CU310-2%20drives.md#function-diagrams-of-sinamics-cu320-2cu310-2-drives)

### Read function diagrams

A block with function diagrams is available for each drive family. Function diagrams are signal flow charts that represent a controller, for example, and arranged side-by-side display the structure of the closed-loop control, for example. The screen forms of the program user interface are based on these function diagrams, but usually do not display all parameters for reasons of clarity.

Function diagrams have the following structure:

![Essentials of a function diagram](images/120730365195_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| **In the footer:** |  |
| ① | DO: Displays the drive objects for which the function diagram applies, e.g. SERVO or CU. |
| ② | Describes the contents of the function diagram, e.g. servo control - speed controller with encoder. |
| ③ | Displays the date when saved and the firmware version. In principle, function diagrams are only available for the current SINAMICS firmware. |
| ④ | Displays the device for which the function diagram applies.  Exception: There are no function diagrams for S210 drives. |
| ⑤ | Displays the diagram number. |
| **In the diagram:** |  |
| ⑥ | The signal path number is displayed in the footer. The function diagram is divided into 8 (not subdivided) fields. These fields are used for navigation within the diagram. Links to other function diagrams always contain the signal path number in addition to the diagram number so that it is easier to find the link target. |
| ⑦ | The links to other diagrams can also be seen in the diagram. The structure of the links is as follows:  - Function diagram number - Signal path number (separated by a dot) |
| ⑧ | Footnotes are identified in the text by square brackets, e.g. &lt;1&gt;. |
| ⑨ | If required, the sampling times that apply for this diagram are shown in the diagrams (rounded rectangle). |
| ⑩ | Signals are interconnected via BICO. |
| ⑪ | The signal flow in the function diagram is illustrated using various symbols. An overview of these symbols can be found in diagrams 1020 - 1025. |

Essentials of a function diagram

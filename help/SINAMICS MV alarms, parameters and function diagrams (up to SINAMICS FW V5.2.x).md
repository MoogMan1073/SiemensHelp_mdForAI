---
title: "SINAMICS MV alarms, parameters and function diagrams (up to SINAMICS FW V5.2.x)"
package: StdrAlaParaFupMVenUS
topics: 27
source: Siemens TIA Portal Information System (offline help, en-US)
---


# SINAMICS MV alarms, parameters and function diagrams (up to SINAMICS FW V5.2.x)

This section contains information on the following topics:

- [SINAMICS MV alarms (up to SINAMICS firmware V5.2.x)](#sinamics-mv-alarms-up-to-sinamics-firmware-v52x)
- [SINAMICS MV parameters (up to SINAMICS firmware V5.2.x)](#sinamics-mv-parameters-up-to-sinamics-firmware-v52x)
- [SINAMICS MV function diagrams (up to SINAMICS firmware V5.2.x)](#sinamics-mv-function-diagrams-up-to-sinamics-firmware-v52x)

## SINAMICS MV alarms (up to SINAMICS firmware V5.2.x)

This section contains information on the following topics:

- [Explanation of faults and alarms](#explanation-of-faults-and-alarms)
- [Control Units](#control-units)
- [Infeeds](#infeeds)
- [Vector drives](#vector-drives)
- [Terminal Modules](#terminal-modules)

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

- [CU320-2 control unit SINAMICS MV alarms](SINAMICS%20Alarms%20SINAMICS%20MV.md#sinamics-alarms-sinamics-mv)

### Infeeds

This section contains information on the following topics:

- [AFEM2C alarms](SINAMICS%20Alarms%20ACTIVE%20INFEED%20CONTROLM2C.md#sinamics-alarms-active-infeed-controlm2c)
- [ALM_MV alarms](SINAMICS%20Alarms%20ACTIVE%20INFEED%20CONTROLMV.md#sinamics-alarms-active-infeed-controlmv)
- [BIC_MV alarms](SINAMICS%20Alarms%20BASIC%20INFEED%20CONTROLMV.md#sinamics-alarms-basic-infeed-controlmv)
- [BMM2C alarms](SINAMICS%20Alarms%20BRAKE%20MODULE%20M2C.md#sinamics-alarms-brake-module-m2c)

### Vector drives

This section contains information on the following topics:

- [Vector 3P alarms](SINAMICS%20Alarms%20VECTOR3P.md#sinamics-alarms-vector3p)
- [Vector DM alarms](SINAMICS%20Alarms%20VECTORDM.md#sinamics-alarms-vectordm)
- [Vector GL alarms](SINAMICS%20Alarms%20VECTORGL.md#sinamics-alarms-vectorgl)
- [Vector M2C alarms](SINAMICS%20Alarms%20VECTORM2C.md#sinamics-alarms-vectorm2c)
- [Vector MV alarms](SINAMICS%20Alarms%20VECTORMV.md#sinamics-alarms-vectormv)
- [Vector SL alarms](SINAMICS%20Alarms%20VECTORSL.md#sinamics-alarms-vectorsl)

### Terminal Modules

This section contains information on the following topics:

- [TB30 alarms](SINAMICS%20Alarms%20TB30%20%28Terminal%20Board%29.md#sinamics-alarms-tb30-terminal-board)
- [TM15 DIDO alarms](SINAMICS%20Alarms%20TM15%20%28Terminal%20Module%20for%20SINAMICS%29.md#sinamics-alarms-tm15-terminal-module-for-sinamics)
- [TM31 alarms](SINAMICS%20Alarms%20TM31%20%28Terminal%20Module%29.md#sinamics-alarms-tm31-terminal-module)
- [TM150 alarms](SINAMICS%20Alarms%20TM150%20%28Terminal%20Module%29.md#sinamics-alarms-tm150-terminal-module)

## SINAMICS MV parameters (up to SINAMICS firmware V5.2.x)

This section contains information on the following topics:

- [Explanation of parameter information](#explanation-of-parameter-information)
- [Control Units](#control-units-1)
- [Infeeds](#infeeds-1)
- [Vector drives](#vector-drives-1)
- [Terminal Modules](#terminal-modules-1)

### Explanation of parameter information

This section contains information on the following topics:

- [General/structure](#generalstructure-1)
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

- [CU320-2 CU_MV Control Unit parameters](SINAMICS%20Parameter%20SINAMICS%20MV.md#sinamics-parameter-sinamics-mv)

### Infeeds

This section contains information on the following topics:

- [AFEM2C parameters](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROLM2C.md#sinamics-parameter-active-infeed-controlm2c)
- [ALM_MV parameters](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROLMV.md#sinamics-parameter-active-infeed-controlmv)
- [BIC_MV parameters](SINAMICS%20Parameter%20BASIC%20INFEED%20CONTROLMV.md#sinamics-parameter-basic-infeed-controlmv)
- [BMM2C parameters](SINAMICS%20Parameter%20BRAKE%20MODULE%20M2C.md#sinamics-parameter-brake-module-m2c)

### Vector drives

This section contains information on the following topics:

- [Vector 3P parameters](SINAMICS%20Parameter%20VECTOR3P.md#sinamics-parameter-vector3p)
- [Vector DM parameters](SINAMICS%20Parameter%20VECTORDM.md#sinamics-parameter-vectordm)
- [Vector GL parameters](SINAMICS%20Parameter%20VECTORGL.md#sinamics-parameter-vectorgl)
- [Vector M2C parameters](SINAMICS%20Parameter%20VECTORM2C.md#sinamics-parameter-vectorm2c)
- [Vector MV parameters](SINAMICS%20Parameter%20VECTORMV.md#sinamics-parameter-vectormv)
- [Vector SL parameters](SINAMICS%20Parameter%20VECTORSL.md#sinamics-parameter-vectorsl)

### Terminal Modules

This section contains information on the following topics:

- [TB30 parameters](SINAMICS%20Parameter%20TB30%20%28Terminal%20Board%29.md#sinamics-parameter-tb30-terminal-board)
- [TM15 DIDO parameters](SINAMICS%20Parameter%20TM15%20%28Terminal%20Module%20for%20SINAMICS%29.md#sinamics-parameter-tm15-terminal-module-for-sinamics)
- [TM31 parameters](SINAMICS%20Parameter%20TM31%20%28Terminal%20Module%29.md#sinamics-parameter-tm31-terminal-module)
- [TM150 parameters](SINAMICS%20Parameter%20TM150%20%28Terminal%20Module%29.md#sinamics-parameter-tm150-terminal-module)

## SINAMICS MV function diagrams (up to SINAMICS firmware V5.2.x)

This section contains information on the following topics:

- [Read function diagrams](#read-function-diagrams)
- [Function Block Diagrams Overview for Current SINAMICS MV Drives](#function-block-diagrams-overview-for-current-sinamics-mv-drives)
- [SINAMICS GL150/SL150](#sinamics-gl150sl150)
- [SINAMICS GM150/SM150/SM120](#sinamics-gm150sm150sm120)

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

### Function Block Diagrams Overview for Current SINAMICS MV Drives

#### Description

The structure of the drive functions and the relationship of the individual parameters with other parameters are displayed in the function diagrams.

**SINAMICS GM150/SM150/SM120 (V4.8)**

- [Function Diagrams for SINAMICS GM150 - Overview](#function-diagrams-for-sinamics-gm150---overview)
- [Function Diagrams for SINAMICS SM150 - Overview](#function-diagrams-for-sinamics-sm150---overview)
- [Function Diagrams for SINAMICS SM120 - Overview](#function-diagrams-for-sinamics-sm120---overview)

**SINAMICS GL150/SL150 (V4.8)**

- [Function Diagrams for SINAMICS GL150 - Overview](#function-diagrams-for-sinamics-gl150---overview)
- [Function Diagrams for SINAMICS SL150 - Overview](#function-diagrams-for-sinamics-sl150---overview)

### SINAMICS GL150/SL150

This section contains information on the following topics:

- [Function Diagrams for SINAMICS GL150 - Overview](#function-diagrams-for-sinamics-gl150---overview)
- [Function Diagrams for SINAMICS SL150 - Overview](#function-diagrams-for-sinamics-sl150---overview)

#### Function Diagrams for SINAMICS GL150 - Overview

The structure of the drive functions and the relationship of the individual parameters with other parameters is displayed in the function diagrams:

Explanations of the function diagrams - explanation of the symbols (Part 1) - 1020 -
  

Explanations of the function diagrams - explanation of the symbols (Part 2) - 1021 -
  

Explanations of the function diagrams - explanation of the symbols (Part 3) - 1022 -
  

Explanations of the function diagrams - handling BICO technology - 1030 -
  

Power unit topologies - topologies with 1 DC link - 1201 -
  

Power unit topologies - topologies with 2 DC links and 2 PSA - 1203 -
  

Power unit topologies - topologies with 2 DC links and 4 PSA - 1204 -
  

CU320-2 input/output terminals - overview - 2119 -
  

CU320-2 input/output terminals - electrically isolated digital inputs (DI 0 ... DI 3, DI 16, DI 17) - 2120 -
  

CU320-2 input/output terminals - electrically isolated digital inputs (DI 4 ... DI 7, DI 20, DI 21) - 2121 -
  

CU320-2 input/output terminals - digital inputs/outputs bidirect. (DI/DO 8 ... DI/DO 9) - 2130 -
  

CU320-2 input/output terminals - digital inputs/outputs bidirect. (DI/DO 10 ... DI/DO 11) - 2131 -
  

CU320-2 input/output terminals - digital inputs/outputs bidirect. (DI/DO 12 ... DI/DO 13) - 2132 -
  

CU320-2 input/output terminals - digital inputs/outputs bidirect. (DI/DO 14 ... DI/DO 15) - 2133 -
  

Control Unit communication - SINAMICS Link overview (r0108.31 = 1, p8835 = 3) - 2197 -
  

Control Unit communication - SINAMICS Link configuration (r0108.31 = 1, p8835 = 3) - 2198 -
  

Control Unit communication - SINAMICS Link receive data (r0108.31 = 1, p8835 = 3) - 2199 -
  

Control Unit communication - SINAMICS Link send data (r0108.31 = 1, p8835 = 3) - 2200 -
  

PROFIdrive - overview - 2401 -
  

PROFIdrive - PROFIBUS (PB) / PROFINET (PN), addresses and diagnostics - 2410 -
  

PROFIdrive - standard telegrams and process data (PZD) - 2415 -
  

PROFIdrive - manufacturer-specific/free telegrams and process data (PZD) - 2416 -
  

PROFIdrive - PZD receive signals, interconnection - 2439 -
  

PROFIdrive - STW1 control word, interconnection - 2442 -
  

PROFIdrive - PZD send signals, interconnection - 2449 -
  

PROFIdrive - ZSW1 status word, interconnection - 2452 -
  

PROFIdrive - IF1 receive telegram, free interconnection via BICO (p0922 = 999) - 2468 -
  

PROFIdrive - IF1 send telegram, free interconnection via BICO (p0922 = 999) - 2470 -
  

PROFIdrive - IF1 status words, free interconnection - 2472 -
  

PROFIdrive - IF1 receive telegram, free interconnection via BICO (p0922 = 999) - 2481 -
  

PROFIdrive - IF1 send telegram, free interconnection via BICO (p0922 = 999) - 2483 -
  

PROFIdrive - IF2 receive telegram, free interconnection via BICO (p0922 = 999) - 2485 -
  

PROFIdrive - IF2 send telegram, free interconnection via BICO (p0922 = 999) - 2487 -
  

PROFIdrive - IF2 status words, free interconnection - 2489 -
  

PROFIdrive - IF2 receive telegram, free interconnection via BICO (p0922 = 999) - 2491 -
  

PROFIdrive - IF2 send telegram, free interconnection via BICO (p0922 = 999) - 2493 -
  

PROFIdrive - CU_STW1 control word 1, Control Unit interconnection - 2495 -
  

PROFIdrive - CU_ZSW1 status word 1 Control Unit interconnection - 2496 -
  

PROFIdrive - O_DIGITAL interconnection - 2497 -
  

PROFIdrive - I_DIGITAL interconnection - 2498 -
  

PROFIdrive - I_DIGITAL_1 interconnection - 2500 -
  

Internal control/status words - control word, sequence control - 2501 -
  

Internal control/status words - status word, sequence control - 2503 -
  

Internal control/status words - control word, setpoint channel - 2505 -
  

Internal control/status words - control word 2, sequence control - 2511 -
  

Internal control/status words - control commands, sequence control - 2512 -
  

Internal control/status words - status word, sequence control - 2513 -
  

Internal control/status words - control word, speed controller - 2520 -
  

Internal control/status words - status word speed controller - 2522 -
  

Internal control/status words - status word, closed-loop control - 2526 -
  

Internal control/status words - status word, monitoring functions 1 - 2534 -
  

Internal control/status words - status word, monitoring functions 2 - 2536 -
  

Internal control/status words - status word, monitoring functions 3 - 2537 -
  

Internal control/status words - control word faults/alarms - 2546 -
  

Internal control/status words - status word, faults/alarms 1 and 2 - 2548 -
  

Sequence control - sequencer (1) - 2610 -
  

Sequence control - sequencer (2) - 2611 -
  

Sequence control - sequencer (3) - 2612 -
  

Sequence control - sequencer (4) - 2613 -
  

Sequence control - missing enables - 2634 -
  

Sequence control - missing enables, extended - 2635 -
  

Setpoint channel - overview - 3001 -
  

Setpoint channel - fixed speed setpoints - 3010 -
  

Setpoint channel - motorized potentiometer - 3020 -
  

Setpoint channel - main setpoint/additional setpoint, setpoint scaling, jog - 3030 -
  

Setpoint channel - direction limitation and direction reversal - 3040 -
  

Setpoint channel - skip frequency bands and speed limits - 3050 -
  

Setpoint channel - basic ramp-function generator - 3060 -
  

Setpoint channel - extended ramp-function generator - 3070 -
  

Setpoint channel - ramp-function generator selection, status word, tracking - 3080 -
  

Encoder evaluation - overview - 4702 -
  

Encoder evaluation - raw signal acquisition - 4704 -
  

Encoder evaluation - actual speed value and pole position sensing encoder 1, n_act_filter 5 - 4715 -
  

Encoder evaluation - absolute value for incremental encoder - 4750 -
  

Vector control - speed control and generation of the torque limits, overview - 6020 -
  

Vector control - speed setpoint, droop - 6030 -
  

Vector control - pre-control balancing reference/acceleration model - 6031 -
  

Vector control - speed controller with/without encoder - 6040 -
  

Vector control - speed controller adaptation (Kp_n/Tn_n adaptation) - 6050 -
  

Vector control - torque setpoint - 6060 -
  

Vector control - Vdc_max controller and Vdc_min controller - 6220 -
  

Vector control - turn mode - 6330 -
  

Vector control - speed control configuration - 6490 -
  

Vector control - excitation (SESM, p0300 = 5) - 6495 -
  

Vector control - excitation sequential control system (SESM, p0300 = 5) - 6496 -
  

Vector control - excitation switchover - 6497 -
  

Vector control - upper/lower torque limit - 6630 -
  

Vector control - current/power/torque limits - 6640 -
  

Vector control - current control, overview - 6700 -
  

Vector control - current setpoint filter - 6710 -
  

Vector control - power and torque calculation - 6714 -
  

Vector control - motor converter, control angle calculation - 6718 -
  

Vector control - flux setpoint calculation (SESM, p0300 = 5) - 6725 -
  

Vector control - flux control (SESM, p0300 = 5) - 6726 -
  

Vector control - current model (SESM, p0300 = 5) - 6727 -
  

Vector control - interface to the motor-side converter (SESM, p0300 = 5) - 6732 -
  

Vector control - line-side converter, control angle limits - 6740 -
  

Vector control - current controller - 6741 -
  

Vector control - modulation limit - 6742 -
  

Vector control - current controller precontrol - 6743 -
  

Vector control - current controller output limiting - 6744 -
  

Vector control - eLVRT status word (low component) - 6745 -
  

Vector control - eLVRT sequence control - 6746 -
  

Vector control - eLVRT status word (high component) - 6747 -
  

Vector control - interface to the line-side converter - 6750 -
  

Vector control - excitation current setpoint, negative-sequence excitation (SESM, p0300 = 5) - 6770 -
  

Vector control - damping interharmonic oscillation (DIH, Part 1) - 6775 -
  

Vector control - damping interharmonic oscillation (DIH, Part 2) - 6776 -
  

Vector control - damping interharmonic oscillation (DIH, Part 3) - 6777 -
  

Vector control - display signals - 6799 -
  

CU redundancy - status word - 6950 -
  

CU redundancy - sequence control - 6951 -
  

CU hot standby redundancy - overview - 6952 -
  

CU hot standby redundancy - status word 1 (1) - 6953 -
  

CU hot standby redundancy - status word 1 (2) - 6954 -
  

CU hot standby redundancy - status word 2 (1) - 6955 -
  

CU hot standby redundancy - status word 2 (2) - 6956 -
  

CU hot standby redundancy - status monitoring - 6957 -
  

CU hot standby redundancy - sequential control - 6958 -
  

CU hot standby redundancy - CU switchover via signals - 6959 -
  

Power unit redundancy - series/cross topology, sequence control - 6962 -
  

Technology functions - friction characteristic - 7010 -
  

Technology functions - synchronizing - 7020 -
  

General - 7200 -
  

Logic function blocks - AND (AND function block with 4 inputs) - 7210 -
  

Logic function blocks - OR (OR function block with 4 inputs) - 7212 -
  

Logic function blocks - XOR (XOR function block with 4 inputs) - 7214 -
  

Logic function blocks - NOT (inverter) - 7216 -
  

Arithmetic function blocks - ADD (adder with 4 inputs), SUB (subtractor) - 7220 -
  

Arithmetic function blocks - MUL (multiplier), DIV (divider) - 7222 -
  

Arithmetic function blocks - AVA (absolute value generator) - 7224 -
  

Timing function blocks - MFP (pulse generator), PCL (pulse contractor) - 7230 -
  

Timing function blocks - PDE (ON delay device), PDF (OFF delay device) - 7232 -
  

Timing function blocks - PST (pulse stretcher) - 7234 -
  

Memory function blocks - RSR (RS flip-flop), DFR (D flip-flop) timing function blocks - PST (pulse stretcher) - 7240 -
  

Switch function blocks - BSW (binary switch), NSW (numeric switch) - 7250 -
  

Control function blocks - LIM (limiter) - 7260 -
  

Control function blocks - PT1 (smoothing element) - 7262 -
  

Control function blocks - INT (integrator), DIF (derivative-action element) - 7264 -
  

Complex function blocks - LVM (double-sided limit monitor with hysteresis) - 7270 -
  

Technology controller - fixed values, binary selection (r0108.16 = 1 and p2216 = 2) - 7950 -
  

Technology controller - motorized potentiometer (r0108.16 = 1) - 7954 -
  

Technology controller - control (r0108.16 = 1) - 7958 -
  

Signals and monitoring functions - speed signals - 8010 -
  

Signals and monitoring functions - torque signals, motor blocked/stalled - 8012 -
  

Signals and monitoring functions - load monitoring (r0108.17 = 1) - 8013 -
  

Signals and monitoring functions - I2t motor monitoring - 8017 -
  

Signals and monitoring functions - separately-excited synchronous motor (SESM, p0300 = 5) - 8020 -
  

Signals and monitoring functions - current monitoring - 8022 -
  

Signals and monitoring functions - output voltage monitoring - 8024 -
  

Signals and monitoring functions - line voltage monitoring filter - 8025 -
  

Signals and monitoring functions - line voltage monitoring - 8026 -
  

Signals and monitoring functions - calculation positive and negative phase-sequence system - 8027 .
  

Signals and monitoring functions - external digital signals (transformer monitoring) - 8030 -
  

Signals and monitoring functions - circuit monitoring - 8032 -
  

Signals and monitoring functions - ground-fault monitoring (ELP) - 8033 -
  

Signals and monitoring functions - valve monitoring (1) - 8034 -
  

Signals and monitoring functions - valve monitoring (2) - 8035 -
  

Signals and monitoring functions - auxiliary circuit monitoring (r0172.0 = 1) - 8037 -
  

Signals and monitoring functions - I2t DC link reactor monitoring - 8038 -
  

Signals and monitoring functions - external monitoring functions - 8040 -
  

Signals and monitoring functions - inrush monitoring, time diagram - 8042 -
  

Diagnostics - overview - 8050 -
  

Diagnostics - fault buffer - 8060 -
  

Diagnostics - alarm buffer - 8065 -
  

Diagnostics - faults/alarms trigger word (r2129) - 8070 -
  

Diagnostics - faults/alarms configuration - 8075 -
  

Diagnostics - measuring sockets (T0, T1, T2) - 8134 -
  

Diagnostics - recorder overview - 8144 -
  

Diagnostics - recorder sequence control - 8145 -
  

Data sets - command data sets (CDS) - 8560 -
  

Data sets - drive data sets (DDS) - 8565 -
  

Data sets - encoder data sets (EDS) - 8570 -
  

Data sets - motor data sets (MDS) - 8575 -
  

Data sets - motor data sets (MDS) - 8575 -
  

Terminal Board 30 (TB30) - overview - 9099 -
  

Terminal Board 30 (TB30) - electrically isolated digital inputs (DI 0 ... DI 3) - 9100 -
  

Terminal Board 30 (TB30) - electrically isolated digital outputs (DO 0 ... DO 3) - 9102 -
  

Terminal Board 30 (TB30) - analog inputs (AI 0 ... AI 1) - 9104 -
  

Terminal Board 30 (TB30) - analog outputs (AO 0 ... AO 1) - 9106 -
  

Communication Board CAN10 (CBC10) - receive telegram free PDO mapping (p8744 = 2) - 9204 -
  

Communication Board CAN10 (CBC10) - receive telegram predef. conn. Set (p8744 = 1) - 9206 -
  

Communication Board CAN10 (CBC10) - send telegram free PDO mapping (p8744 = 2) - 9208 -
  

Communication Board CAN10 (CBC10) - send telegram predef. conn. Set (p8744 = 1) - 9210 -
  

Communication Board CAN10 (CBC10) - control word CANopen - 9220 -
  

Communication Board CAN10 (CBC10) - status word CANopen - 9226 -
  

Terminal Module 15 (TM15) - overview TM15DI_DO (SINAMICS) - 9399 -
  

Terminal Module 15 (TM15) - digital inputs/outputs bidirectional (DI/DO 0 ... DI/DO 7) - 9400 -
  

Terminal Module 15 (TM15) - digital inputs/outputs bidirectional (DI/DO 8 ... DI/DO 15) - 9401 -
  

Terminal Module 15 (TM15) - digital inputs/outputs, bidirectional (DI/DO 16 ... DI/DO 23) - 9402 -
  

Terminal Module 31 (TM31) - overview - 9549 -
  

Terminal Module 31 (TM31) - electrically isolated digital inputs (DI 0 ... DI 3) - 9550 -
  

Terminal Module 31 (TM31) - electrically isolated digital inputs (DI 4 ... DI 7) - 9552 -
  

Terminal Module 31 (TM31) - electrically isolated digital relay outputs (DO 0 ... DO 1) - 9556 -
  

Terminal Module 31 (TM31) - digital inputs/outputs bidirectional (DI/DO 8 ... DI/DO 9) - 9560 -
  

Terminal Module 31 (TM31) - digital inputs/outputs, bidirectional (DI/DO 10 ... DI/DO 11) - 9562 -
  

Terminal Module 31 (TM31) - analog input 0 (AI 0) - 9566 -
  

Terminal Module 31 (TM31) - analog input 1 (AI 1) - 9568 -
  

Terminal Module 31 (TM31) - analog outputs (AO 0 ... AO 1) - 9572 -
  

Terminal Module 31 (TM31) - temperature evaluation - 9576 -
  

Terminal Module 31 (TM31) - sensor monitoring KTY/PTC/PT1000 - 9577 -
  

Terminal Module 150 (TM150) - temperature evaluation structure (channel 0 ... 11) - 9625 -
  

Terminal Module 150 (TM150) - temperature evaluation 1x2-, 3-, 4-wire (channels 0 … 5) - 9626 -
  

Terminal Module 150 (TM150) - temperature evaluation 2x2-wire (channels 0 ... 11) - 9627 -
  

Auxiliaries - cooling unit, control and feedback signals (r0108.28 = 1) - 9794 -
  

Auxiliaries - cooling unit sequence control (r0108.28 = 1) - 9795 -
  

Auxiliaries - cooling unit pressure monitoring, temperature monitoring (r0108.28 = 1) - 9796 -
  

Auxiliaries - circuit breaker, time diagram - 9800 -
  

Auxiliaries - circuit breaker, control and feedback signals - 9801 -
  

Auxiliaries - circuit breaker, control and monitoring - 9802 -
  

Auxiliaries - line side switch (switch 0) switchover - 9803 -
  

Auxiliaries - motor switch (switch 1) switchover - 9804 -
  

Auxiliaries - fan, sequence control (r0108.27 = 1) - 9805 -
  

Auxiliaries - line side switch (switch 0), control and feedback signals - 9810 -
  

Auxiliaries - parallel switching unit, sequence control - 9815 -
  

Auxiliaries - parallel switching unit, setpoint calculation - 9816 -
  

Auxiliaries - parallel switching unit - 9817 -
  

Auxiliaries - demagnetization equipment - 9820 -
  

Auxiliaries - demagnetization equipment, sequence control (1) - 9821 -
  

Auxiliaries - demagnetization equipment, sequence control (2) - 9822 -
  

Auxiliaries - demagnetization equipment, time diagram - 9823 -
  

Auxiliaries - internal demagnetization, sequence control, time diagram - 9824 -
  

Auxiliaries - internal output disconnector, sequence control - 9825 -
  

Auxiliaries - door switch, grounding switch, make-proof grounding switch, input/output disconnector - 9827 -
  

Auxiliaries - step-up transformer (bypass), ramp-up variant 1, timing diagram - 9830 -
  

Auxiliaries - step-up transformer (bypass), ramp-up variant 2, timing diagram - 9831 -
  

Voltage Sensing Module (VSM) - analog inputs (AI 2 ... AI 3) - 9880 -
  

Power Stack Adapter (PSA4, PSA5) - connection overview - 9981 -
  

Power Stack Adapter (PSA4, PSA5) - digital inputs (DI 0 ... DI 7) - 9982 -
  

Power Stack Adapter (PSA4, PSA5) - digital outputs (DO 0 ... DO 7) - 9983 -
  

Power Stack Adapter (PSA4, PSA5) - analog inputs (AI 0 … AI 3) - 9984 -
  

Power Stack Adapter (PSA4, PSA5) - temperature sensor (PT100) - 9985 -
  

Power Stack Adapter (PSA4, PSA5) - analog outputs (AO 0 ... AO 7) - 9986 -
  

Power Stack Adapter (PSA4, PSA5) - digital inputs/outputs (DI/DO 0 ... DI/DO 3) - 9987 -
  

Power Stack Adapter (PSA4, PSA5) - digital inputs/outputs (DI/DO 4 ... DI/DO 7) - 9988 -

#### Function Diagrams for SINAMICS SL150 - Overview

The structure of the drive functions and the relationship of the individual parameters with other parameters is displayed in the function diagrams:

Explanations of the function diagrams - explanation of the symbols (Part 1) - 1020 -
  

Explanations of the function diagrams - explanation of the symbols (Part 2) - 1021 -
  

Explanations of the function diagrams - explanation of the symbols (Part 3) - 1022 -
  

Explanations of the function diagrams - handling BICO technology - 1030 -
  

CU320-2 input/output terminals - overview - 2119 -
  

CU320-2 input/output terminals - electrically isolated digital inputs (DI 0 ... DI 3, DI 16, DI 17) - 2120 -
  

CU320-2 input/output terminals - electrically isolated digital inputs (DI 4 ... DI 7, DI 20, DI 21) - 2121 -
  

CU320-2 input/output terminals - digital inputs/outputs bidirect. (DI/DO 8 ... DI/DO 9) - 2130 -
  

CU320-2 input/output terminals - digital inputs/outputs bidirect. (DI/DO 10 ... DI/DO 11) - 2131 -
  

CU320-2 input/output terminals - digital inputs/outputs bidirect. (DI/DO 12 ... DI/DO 13) - 2132 -
  

CU320-2 input/output terminals - digital inputs/outputs bidirect. (DI/DO 14 ... DI/DO 15) - 2133 -
  

Control Unit communication - SINAMICS Link overview (r0108.31 = 1, p8835 = 3) - 2197 -
  

Control Unit communication - SINAMICS Link configuration (r0108.31 = 1, p8835 = 3) - 2198 -
  

Control Unit communication - SINAMICS Link receive data (r0108.31 = 1, p8835 = 3) - 2199 -
  

Control Unit communication - SINAMICS Link send data (r0108.31 = 1, p8835 = 3) - 2200 -
  

PROFIdrive - overview - 2401 -
  

PROFIdrive - PROFIBUS (PB) / PROFINET (PN), addresses and diagnostics - 2410 -
  

PROFIdrive - standard telegrams and process data (PZD) - 2415 -
  

PROFIdrive - manufacturer-specific/free telegrams and process data (PZD) - 2416 -
  

PROFIdrive - PZD receive signals, interconnection - 2439 -
  

PROFIdrive - STW1 control word, interconnection - 2442 -
  

PROFIdrive - PZD send signals, interconnection - 2449 -
  

PROFIdrive - ZSW1 status word, interconnection - 2452 -
  

PROFIdrive - IF1 receive telegram, free interconnection via BICO (p0922 = 999) - 2468 -
  

PROFIdrive - IF1 send telegram, free interconnection via BICO (p0922 = 999) - 2470 -
  

PROFIdrive - IF1 status words, free interconnection - 2472 -
  

PROFIdrive - IF1 receive telegram, free interconnection via BICO (p0922 = 999) - 2481 -
  

PROFIdrive - IF1 send telegram, free interconnection via BICO (p0922 = 999) - 2483 -
  

PROFIdrive - IF2 receive telegram, free interconnection via BICO (p0922 = 999) - 2485 -
  

PROFIdrive - IF2 send telegram, free interconnection via BICO (p0922 = 999) - 2487 -
  

PROFIdrive - IF2 status words, free interconnection - 2489 -
  

PROFIdrive - IF2 receive telegram, free interconnection via BICO (p0922 = 999) - 2491 -
  

PROFIdrive - IF2 send telegram, free interconnection via BICO (p0922 = 999) - 2493 -
  

PROFIdrive - CU_STW1 control word 1, Control Unit interconnection - 2495 -
  

PROFIdrive - CU_ZSW1 status word 1 Control Unit interconnection - 2496 -
  

PROFIdrive - O_DIGITAL interconnection - 2497 -
  

PROFIdrive - I_DIGITAL interconnection - 2498 -
  

PROFIdrive - I_DIGITAL_1 interconnection - 2500 -
  

Internal control/status words - control word, sequence control - 2501 -
  

Internal control/status words - status word, sequence control - 2503 -
  

Internal control/status words - control word, setpoint channel - 2505 -
  

Internal control/status words - control commands, sequence control - 2512 -
  

Internal control/status words - status word, sequence control - 2513 -
  

Internal control/status words - control word, speed controller - 2520 -
  

Internal control/status words - status word speed controller - 2522 -
  

Internal control/status words - status word, closed-loop control - 2526 -
  

Internal control/status words - status word, monitoring functions 1 - 2534 -
  

Internal control/status words - status word, monitoring functions 2 - 2536 -
  

Internal control/status words - status word, monitoring functions 3 - 2537 -
  

Internal control/status words - control word faults/alarms - 2546 -
  

Internal control/status words - status word, faults/alarms 1 and 2 - 2548 -
  

Sequence control - sequencer (1) - 2610 -
  

Sequence control - sequencer (2) - 2611 -
  

Sequence control - sequencer (3) - 2612 -
  

Sequence control - missing enables - 2634 -
  

Setpoint channel - overview - 3001 -
  

Setpoint channel - fixed speed setpoints - 3010 -
  

Setpoint channel - motorized potentiometer - 3020 -
  

Setpoint channel - main setpoint/additional setpoint, setpoint scaling, jog - 3030 -
  

Setpoint channel - direction limitation and direction reversal - 3040 -
  

Setpoint channel - skip frequency bands and speed limits - 3050 -
  

Setpoint channel - basic ramp-function generator - 3060 -
  

Setpoint channel - extended ramp-function generator - 3070 -
  

Setpoint channel - ramp-function generator selection, status word, tracking - 3080 -
  

Encoder evaluation - overview - 4702 -
  

Encoder evaluation - raw signal acquisition - 4704 -
  

Encoder evaluation - actual speed value and pole position sensing encoder 1, n_act_filter 5 - 4715 -
  

Encoder evaluation - absolute value for incremental encoder - 4750 -
  

Vector control - speed control and generation of the torque limits, overview - 6020 -
  

Vector control - speed setpoint, droop - 6030 -
  

Vector control - pre-control balancing reference/acceleration model - 6031 -
  

Vector control - speed controller with/without encoder - 6040 -
  

Vector control - speed controller adaptation (Kp_n/Tn_n adaptation) - 6050 -
  

Vector control - torque setpoint - 6060 -
  

Vector control - switchover to encoderless operation (SESM, p0300=5) - 6070 -
  

Vector control - Vdc_max controller and Vdc_min controller - 6220 -
  

Vector control - U/f and I/f setpoint generator - 6301 -
  

Vector control - speed control configuration - 6490 -
  

Vector control - excitation (SESM, p0300 = 5) - 6495 -
  

Vector control - excitation sequential control system (SESM, p0300 = 5) - 6496 -
  

Vector control - upper/lower torque limit - 6630 -
  

Vector control - current/power/torque limits - 6640 -
  

Vector control - current control, overview - 6700 -
  

Vector control - current setpoint filter - 6710 -
  

Vector control - pre-control current controller (SESM, p0300 = 5) - 6713 -
  

Vector control - Iq and Id controllers - 6714 -
  

Vector control - flux setpoint calculation (ASM, p0300 = 1) - 6723 -
  

Vector control - field weakening controller (PMSM, p0300 = 2) - 6724 -
  

Vector control - flux setpoint calculation (SESM, p0300 = 5) - 6725 -
  

Vector control - field weakening controller, flux controller (SESM, p0300 = 5) - 6726 -
  

Vector control - current model, orientation angle selection (SESM, p0300 = 5) - 6727 -
  

Vector control - cos phi control, minimum current (SESM, p0300 = 5) - 6728 -
  

Vector control - motor model (ASM, PMSM, SESM, p0300 = 1, 2, 5) - 6729 -
  

Vector control - interface to the Motor Module (ASM, PMSM, SESM, p0300 = 1, 2, 5) - 6732 -
  

Vector control - motor control / phase current control interface - 6734 -
  

Vector control - line voltage sensing/phase control interface - 6735 -
  

Vector control - phase current preprocessing/phase current controller - 6736 -
  

Vector control - discontinuous current adaptation, dynamic voltage boost - 6737 -
  

Vector control - automatic restart and extended buffering evaluation line monitoring - 6761 -
  

Vector control - automatic restart overview - 6762 -
  

Vector control - automatic restart, sequence control - 6763 -
  

Vector control - extended buffering for short voltage dips, sequence control - 6765 -
  

Vector control - excitation current setpoint, negative-sequence excitation (SESM, p0300 = 5) - 6770 -
  

Vector control - display signals - 6799 -
  

Technology functions - friction characteristic - 7010 -
  

Technology functions - synchronizing - 7020 -
  

General - 7200 -
  

Logic function blocks - AND (AND function block with 4 inputs) - 7210 -
  

Logic function blocks - OR (OR function block with 4 inputs) - 7212 -
  

Logic function blocks - XOR (XOR function block with 4 inputs) - 7214 -
  

Logic function blocks - NOT (inverter) - 7216 -
  

Arithmetic function blocks - ADD (adder with 4 inputs), SUB (subtractor) - 7220 -
  

Arithmetic function blocks - MUL (multiplier), DIV (divider) - 7222 -
  

Arithmetic function blocks - AVA (absolute value generator) - 7224 -
  

Timing function blocks - MFP (pulse generator), PCL (pulse contractor) - 7230 -
  

Timing function blocks - PDE (ON delay device), PDF (OFF delay device) - 7232 -
  

Timing function blocks - PST (pulse stretcher) - 7234 -
  

Memory function blocks - RSR (RS flip-flop), DFR (D flip-flop) timing function blocks - PST (pulse stretcher) - 7240 -
  

Switch function blocks - BSW (binary switch), NSW (numeric switch) - 7250 -
  

Control function blocks - LIM (limiter) - 7260 -
  

Control function blocks - PT1 (smoothing element) - 7262 -
  

Control function blocks - INT (integrator), DIF (derivative-action element) - 7264 -
  

Complex function blocks - LVM (double-sided limit monitor with hysteresis) - 7270 -
  

Technology controller - fixed values, binary selection (r0108.16 = 1 and p2216 = 2) - 7950 -
  

Technology controller - motorized potentiometer (r0108.16 = 1) - 7954 -
  

Technology controller - control (r0108.16 = 1) - 7958 -
  

Signals and monitoring functions - speed signals - 8010 -
  

Signals and monitoring functions - torque signals, motor blocked/stalled - 8012 -
  

Signals and monitoring functions - load monitoring (r0108.17 = 1) - 8013 -
  

Signals and monitoring functions - I2t motor monitoring - 8017 -
  

Signals and monitoring functions - output current monitoring - 8022 -
  

Signals and monitoring functions - output voltage monitoring - 8024 -
  

Signals and monitoring functions - line voltage monitoring (1) - 8026 -
  

Signals and monitoring functions - line voltage monitoring (2) - 8027 -
  

Signals and monitoring functions - external digital messages - 8030 -
  

Signals and monitoring functions - external analog signals - 8031 -
  

Signals and monitoring functions - valve monitoring (1) - 8034 -
  

Signals and monitoring functions - valve monitoring (2) - 8035 -
  

Signals and monitoring functions - auxiliary circuit monitoring (r0172.0 = 1) - 8037 -
  

Diagnostics - overview - 8050 -
  

Diagnostics - fault buffer - 8060 -
  

Diagnostics - alarm buffer - 8065 -
  

Diagnostics - faults/alarms trigger word (r2129) - 8070 -
  

Diagnostics - faults/alarms configuration - 8075 -
  

Diagnostics - measuring sockets (T0, T1, T2) - 8134 -
  

Diagnostics - recorder overview - 8144 -
  

Diagnostics - recorder sequence control - 8145 -
  

Data sets - command data sets (CDS) - 8560 -
  

Data sets - drive data sets (DDS) - 8565 -
  

Data sets - encoder data sets (EDS) - 8570 -
  

Data sets - motor data sets (MDS) - 8575 -
  

Terminal Board 30 (TB30) - overview - 9099 -
  

Terminal Board 30 (TB30) - electrically isolated digital inputs (DI 0 ... DI 3) - 9100 -
  

Terminal Board 30 (TB30) - electrically isolated digital outputs (DO 0 ... DO 3) - 9102 -
  

Terminal Board 30 (TB30) - analog inputs (AI 0 ... AI 1) - 9104 -
  

Terminal Board 30 (TB30) - analog outputs (AO 0 ... AO 1) - 9106 -
  

Communication Board CAN10 (CBC10) - receive telegram free PDO mapping (p8744 = 2) - 9204 -
  

Communication Board CAN10 (CBC10) - receive telegram predef. conn. Set (p8744 = 1) - 9206 -
  

Communication Board CAN10 (CBC10) - send telegram free PDO mapping (p8744 = 2) - 9208 -
  

Communication Board CAN10 (CBC10) - send telegram predef. conn. Set (p8744 = 1) - 9210 -
  

Communication Board CAN10 (CBC10) - control word CANopen - 9220 -
  

Communication Board CAN10 (CBC10) - status word CANopen - 9226 -
  

Terminal Module 15 (TM15) - overview TM15DI_DO (SINAMICS) - 9399 -
  

Terminal Module 15 (TM15) - digital inputs/outputs bidirectional (DI/DO 0 ... DI/DO 7) - 9400 -
  

Terminal Module 15 (TM15) - digital inputs/outputs bidirectional (DI/DO 8 ... DI/DO 15) - 9401 -
  

Terminal Module 15 (TM15) - digital inputs/outputs, bidirectional (DI/DO 16 ... DI/DO 23) - 9402 -
  

Terminal Module 31 (TM31) - overview - 9549 -
  

Terminal Module 31 (TM31) - electrically isolated digital inputs (DI 0 ... DI 3) - 9550 -
  

Terminal Module 31 (TM31) - electrically isolated digital inputs (DI 4 ... DI 7) - 9552 -
  

Terminal Module 31 (TM31) - electrically isolated digital relay outputs (DO 0 ... DO 1) - 9556 -
  

Terminal Module 31 (TM31) - digital inputs/outputs bidirectional (DI/DO 8 ... DI/DO 9) - 9560 -
  

Terminal Module 31 (TM31) - digital inputs/outputs, bidirectional (DI/DO 10 ... DI/DO 11) - 9562 -
  

Terminal Module 31 (TM31) - analog input 0 (AI 0) - 9566 -
  

Terminal Module 31 (TM31) - analog input 1 (AI 1) - 9568 -
  

Terminal Module 31 (TM31) - analog outputs (AO 0 ... AO 1) - 9572 -
  

Terminal Module 31 (TM31) - temperature evaluation - 9576 -
  

Terminal Module 31 (TM31) - sensor monitoring KTY/PTC/PT1000 - 9577 -
  

Terminal Module 150 (TM150) - temperature evaluation structure (channel 0 ... 11) - 9625 -
  

Terminal Module 150 (TM150) - temperature evaluation 1x2-, 3-, 4-wire (channels 0 … 5) - 9626 -
  

Terminal Module 150 (TM150) - temperature evaluation 2x2-wire (channels 0 ... 11) - 9627 -
  

Auxiliaries - cooling unit, pressure monitoring, feedback signals (r0108.28 = 1) - 9796 -
  

Auxiliaries - circuit breaker, time diagram - 9800 -
  

Auxiliaries - circuit breaker, control and feedback signals - 9801 -
  

Auxiliaries - circuit breaker, control and monitoring - 9802 -
  

Auxiliaries - fan, sequence control (r0108.27 = 1) - 9805 -
  

Auxiliaries - fan differential pressure evaluation (r0108.27 = 1) - 9806 -
  

Auxiliaries - line side switch (switch 0), control and feedback signals - 9810 -
  

Auxiliaries - output disconnector, sequence control - 9825 -
  

Auxiliaries - door release - 9827 -
  

Voltage Sensing Module (VSM) - analog inputs (AI 2 ... AI 3) - 9880 -
  

Power Stack Adapter (PSA4, PSA5) - connection overview - 9981 -
  

Power Stack Adapter (PSA4, PSA5) - analog inputs (AI 0 … AI 3) - 9984 -
  

Power Stack Adapter (PSA4, PSA5) - temperature sensor (PT100) - 9985 -
  

Power Stack Adapter (PSA4, PSA5) - analog outputs (AO 0 ... AO 7) - 9986 -

### SINAMICS GM150/SM150/SM120

This section contains information on the following topics:

- [Function Diagrams for SINAMICS GM150 - Overview](#function-diagrams-for-sinamics-gm150---overview)
- [Function Diagrams for SINAMICS SM150 - Overview](#function-diagrams-for-sinamics-sm150---overview)
- [Function Diagrams for SINAMICS SM120 - Overview](#function-diagrams-for-sinamics-sm120---overview)

#### Function Diagrams for SINAMICS GM150 - Overview

The structure of the drive functions and the relationship of the individual parameters with other parameters is displayed in the function diagrams:

Explanations of the function diagrams - explanation of the symbols (Part 1) - 1020 -
  

Explanations of the function diagrams - explanation of the symbols (Part 2) - 1021 -
  

Explanations of the function diagrams - explanation of the symbols (Part 3) - 1022 -
  

Explanations of the function diagrams - handling BICO technology - 1030 -
  

CU320-2 input/output terminals - overview - 2119 -
  

CU320-2 input/output terminals - electrically isolated digital inputs (DI 0 ... DI 3, DI 16, DI 17) - 2120 -
  

CU320-2 input/output terminals - electrically isolated digital inputs (DI 4 ... DI 7, DI 20, DI 21) - 2121 -
  

CU320-2 input/output terminals - digital inputs/outputs bidirect. (DI/DO 8 ... DI/DO 9) - 2130 -
  

CU320-2 input/output terminals - digital inputs/outputs bidirect. (DI/DO 10 ... DI/DO 11) - 2131 -
  

CU320-2 input/output terminals - digital inputs/outputs bidirect. (DI/DO 12 ... DI/DO 13) - 2132 -
  

CU320-2 input/output terminals - digital inputs/outputs bidirect. (DI/DO 14 ... DI/DO 15) - 2133 -
  

Control Unit communication - SINAMICS Link overview (r0108.31 = 1, p8835 = 3) - 2197 -
  

Control Unit communication - SINAMICS Link configuration (r0108.31 = 1, p8835 = 3) - 2198 -
  

Control Unit communication - SINAMICS Link receive data (r0108.31 = 1, p8835 = 3) - 2199 -
  

Control Unit communication - SINAMICS Link send data (r0108.31 = 1, p8835 = 3) - 2200 -
  

PROFIdrive - overview - 2401 -
  

PROFIdrive - PROFIBUS (PB) / PROFINET (PN), addresses and diagnostics - 2410 -
  

PROFIdrive - standard telegrams and process data (PZD) - 2415 -
  

PROFIdrive - manufacturer-specific/free telegrams and process data (PZD) - 2416 -
  

PROFIdrive - PZD receive signals, interconnection - 2439 -
  

PROFIdrive - STW1 control word, interconnection - 2442 -
  

PROFIdrive - I_STW1 control word, infeed interconnection - 2447 -
  

PROFIdrive - PZD send signals, interconnection - 2449 -
  

PROFIdrive - ZSW1 status word, interconnection - 2452 -
  

PROFIdrive - I_ZSW1 status word, infeed interconnection - 2457 -
  

PROFIdrive - IF1 receive telegram, free interconnection via BICO (p0922 = 999) - 2468 -
  

PROFIdrive - IF1 send telegram, free interconnection via BICO (p0922 = 999) - 2470 -
  

PROFIdrive - IF1 status words, free interconnection - 2472 -
  

PROFIdrive - IF1 receive telegram, free interconnection via BICO (p0922 = 999) - 2481 -
  

PROFIdrive - IF1 send telegram, free interconnection via BICO (p0922 = 999) - 2483 -
  

PROFIdrive - IF2 receive telegram, free interconnection via BICO (p0922 = 999) - 2485 -
  

PROFIdrive - IF2 send telegram, free interconnection via BICO (p0922 = 999) - 2487 -
  

PROFIdrive - IF2 status words, free interconnection - 2489 -
  

PROFIdrive - IF2 receive telegram, free interconnection via BICO (p0922 = 999) - 2491 -
  

PROFIdrive - IF2 send telegram, free interconnection via BICO (p0922 = 999) - 2493 -
  

PROFIdrive - CU_STW1 control word 1, Control Unit interconnection - 2495 -
  

PROFIdrive - CU_ZSW1 status word 1 Control Unit interconnection - 2496 -
  

PROFIdrive - O_DIGITAL interconnection - 2497 -
  

PROFIdrive - I_DIGITAL interconnection - 2498 -
  

PROFIdrive - I_DIGITAL_1 interconnection - 2500 -
  

Internal control/status words - control word, sequence control - 2501 -
  

Internal control/status words - status word, sequence control - 2503 -
  

Internal control/status words - control word, setpoint channel - 2505 -
  

Internal control/status words - control commands, sequence control - 2512 -
  

Internal control/status words - status word 2, sequence control - 2513 -
  

Internal control/status words - control word, speed controller - 2520 -
  

Internal control/status words - status word speed controller - 2522 -
  

Internal control/status words - status word, closed-loop control - 2526 -
  

Internal control/status words - status word, monitoring functions 1 - 2534 -
  

Internal control/status words - status word, monitoring functions 2 - 2536 -
  

Internal control/status words - status word, monitoring functions 3 - 2537 -
  

Internal control/status words - control word faults/alarms - 2546 -
  

Internal control/status words - status word, faults/alarms 1 and 2 - 2548 -
  

Sequence control - sequencer (1) - 2640 -
  

Sequence control - sequencer (2) - 2641 -
  

Sequence control - sequencer (3) - 2642 -
  

Sequence control - sequencer (4) - 2643 -
  

Sequence control - sequencer (5) - 2644 -
  

Sequence control - sequencer (6) - 2645 -
  

Sequence control - missing enables - 2654 -
  

Setpoint channel - overview - 3001 -
  

Setpoint channel - fixed speed setpoints - 3010 -
  

Setpoint channel - motorized potentiometer - 3020 -
  

Setpoint channel - main setpoint/additional setpoint, setpoint scaling, jog - 3030 -
  

Setpoint channel - direction limitation and direction reversal - 3040 -
  

Setpoint channel - skip frequency bands and speed limits - 3050 -
  

Setpoint channel - basic ramp-function generator - 3060 -
  

Setpoint channel - extended ramp-function generator - 3070 -
  

Setpoint channel - ramp-function generator selection, status word, tracking - 3080 -
  

Encoder evaluation - overview - 4702 -
  

Encoder evaluation - raw signal acquisition - 4704 -
  

Encoder evaluation - actual speed value and pole position sensing encoder 1, n_act_filter 5 - 4715 -
  

Encoder evaluation - absolute value for incremental encoder - 4750 -
  

Vector control - speed control and generation of the torque limits, overview - 6020 -
  

Vector control - speed setpoint, droop - 6030 -
  

Vector control - pre-control balancing reference/acceleration model - 6031 -
  

Vector control - speed controller with/without encoder - 6040 -
  

Vector control - speed controller adaptation (Kp_n/Tn_n adaptation) - 6050 -
  

Vector control - torque setpoint - 6060 -
  

Vector control - switchover to encoderless operation (SESM, p0300=5) - 6070 -
  

Vector control - Vdc_max controller and Vdc_min controller - 6220 -
  

Vector control - U/f and I/f setpoint generator - 6301 -
  

Vector control - derating for U/f control - 6302 -
  

Vector control - speed control configuration - 6490 -
  

Vector control - excitation (SESM, p0300 = 5) - 6495 -
  

Vector control - excitation sequential control system (SESM, p0300 = 5) - 6496 -
  

Vector control - upper/lower torque limit - 6630 -
  

Vector control - current/power/torque limits - 6640 -
  

Vector control - current control, overview - 6700 -
  

Vector control - current setpoint filter - 6710 -
  

Vector control - pre-control current controller (SESM, p0300 = 5) - 6713 -
  

Vector control - Iq and Id controllers - 6714 -
  

Vector control - Vdc balancing control - 6717 -
  

Vector control - Vdc balancing control for a tandem connection, swivel angle - 6718 -
  

Vector control - Vdc balancing control for a tandem connection, structure - 6719 -
  

Vector control - flux setpoint calculation (ASM, p0300 = 1) - 6723 -
  

Vector control - field weakening controller (PMSM, p0300 = 2) - 6724 -
  

Vector control - flux setpoint calculation (SESM, p0300 = 5) - 6725 -
  

Vector control - field weakening controller, flux controller (SESM, p0300 = 5) - 6726 -
  

Vector control - current model, orientation angle selection (SESM, p0300 = 5) - 6727 -
  

Vector control - cos phi control, minimum current (SESM, p0300 = 5) - 6728 -
  

Vector control - interface to the power unit (ASM, PMSM, p0300 = 1, 2) - 6730 -
  

Vector control - interface to the power unit (SESM, p0300 = 5) - 6732 -
  

Vector control - switching frequency reduction for space vector approximation (SVA) - 6760 -
  

Vector control - automatic restart overview - 6762 -
  

Vector control - automatic restart, sequence control - 6763 -
  

Vector control - extended buffering for short voltage dips, sequence control - 6765 -
  

Vector control - excitation current setpoint, negative-sequence excitation (SESM, p0300 = 5) - 6770 -
  

Vector control - display signals - 6799 -
  

CU redundancy - status word - 6950 -
  

CU redundancy - sequence control - 6951 -
  

Technology functions - friction characteristic - 7010 -
  

Technology functions - synchronizing - 7020 -
  

General - 7200 -
  

Logic function blocks - AND (AND function block with 4 inputs) - 7210 -
  

Logic function blocks - OR (OR function block with 4 inputs) - 7212 -
  

Logic function blocks - XOR (XOR function block with 4 inputs) - 7214 -
  

Logic function blocks - NOT (inverter) - 7216 -
  

Arithmetic function blocks - ADD (adder with 4 inputs), SUB (subtractor) - 7220 -
  

Arithmetic function blocks - MUL (multiplier), DIV (divider) - 7222 -
  

Arithmetic function blocks - AVA (absolute value generator) - 7224 -
  

Timing function blocks - MFP (pulse generator), PCL (pulse contractor) - 7230 -
  

Timing function blocks - PDE (ON delay device), PDF (OFF delay device) - 7232 -
  

Timing function blocks - PST (pulse stretcher) - 7234 -
  

Memory function blocks - RSR (RS flip-flop), DFR (D flip-flop) timing function blocks - PST (pulse stretcher) - 7240 -
  

Switch function blocks - BSW (binary switch), NSW (numeric switch) - 7250 -
  

Control function blocks - LIM (limiter) - 7260 -
  

Control function blocks - PT1 (smoothing element) - 7262 -
  

Control function blocks - INT (integrator), DIF (derivative-action element) - 7264 -
  

Complex function blocks - LVM (double-sided limit monitor with hysteresis) - 7270 -
  

Technology controller - fixed values, binary selection (r0108.16 = 1 and p2216 = 2) - 7950 -
  

Technology controller - motorized potentiometer (r0108.16 = 1) - 7954 -
  

Technology controller - control (r0108.16 = 1) - 7958 -
  

Signals and monitoring functions - speed signals - 8010 -
  

Signals and monitoring functions - torque signals, motor blocked/stalled - 8012 -
  

Signals and monitoring functions - load monitoring (r0108.17 = 1) - 8013 -
  

Signals and monitoring functions - thermal monitoring power unit - 8014 -
  

Signals and monitoring functions - rotor temperature model - 8015 -
  

Signals and monitoring functions - thermal monit. power unit/motor, current reduction - 8016 -
  

Signals and monitoring functions - I2t motor monitoring - 8017 -
  

Signals and monitoring functions - output current monitoring - 8022 -
  

Signals and monitoring functions - output voltage monitoring - 8024 -
  

Signals and monitoring functions - Vdc monitoring - 8028 -
  

Signals and monitoring functions - external digital messages - 8030 -
  

Signals and monitoring functions - external analog signals - 8031 -
  

Signals and monitoring functions - auxiliary circuit monitoring (r0172.0 = 1) - 8037 -
  

Signals and monitoring functions - EMERGENCY STOP category 0 or 1 - 8044 -
  

Diagnostics - overview - 8050 -
  

Diagnostics - fault buffer - 8060 -
  

Diagnostics - alarm buffer - 8065 -
  

Diagnostics - faults/alarms trigger word (r2129) - 8070 -
  

Diagnostics - faults/alarms configuration - 8075 -
  

Diagnostics - measuring sockets (T0, T1, T2) - 8134 -
  

Diagnostics - recorder overview - 8144 -
  

Diagnostics - recorder sequence control - 8145 -
  

Diagnostics - test operation, IGCT power semiconductor (p6650 = 4) - 8146 -
  

Diagnostics - faults for power unit redundancy (option L35) - 8147 -
  

Data sets - command data sets (CDS) - 8560 -
  

Data sets - drive data sets (DDS) - 8565 -
  

Data sets - encoder data sets (EDS) - 8570 -
  

Data sets - motor data sets (MDS) - 8575 -
  

Basic Infeed - overview - 8710 -
  

Basic Infeed - control word sequence control infeed - 8720 -
  

Basic Infeed - status word, sequence control, infeed - 8726 -
  

Basic Infeed - control commands, sequence control, infeed - 8729 -
  

Basic Infeed - status word 2, sequence control, infeed - 8730 -
  

Basic Infeed - sequencer (1) - 8732 -
  

Basic Infeed - sequencer (2) - 8733 -
  

Basic Infeed - sequencer (3) - 8734 -
  

Basic Infeed - sequencer (4) - 8735 -
  

Basic Infeed - sequencer (5) - 8736 -
  

Active Infeed - missing enables - 8738 -
  

Basic Infeed - interface to the Basic Line Module - 8750 -
  

Basic Infeed - signals and monitoring functions, line voltage monitoring (1) - 8761 -
  

Basic Infeed - signals and monitoring functions, line voltage monitoring (2) - 8762 -
  

Basic Infeed - signals and monitoring functions, Vdc monitoring (1) - 8764 -
  

Basic Infeed - signals and monitoring functions, Vdc monitoring (2) - 8765 -
  

Basic Infeed - thermal monitoring, infeed, derating - 8770 -
  

Terminal Board 30 (TB30) - overview - 9099 -
  

Terminal Board 30 (TB30) - electrically isolated digital inputs (DI 0 ... DI 3) - 9100 -
  

Terminal Board 30 (TB30) - electrically isolated digital outputs (DO 0 ... DO 3) - 9102 -
  

Terminal Board 30 (TB30) - analog inputs (AI 0 ... AI 1) - 9104 -
  

Terminal Board 30 (TB30) - analog outputs (AO 0 ... AO 1) - 9106 -
  

Communication Board CAN10 (CBC10) - receive telegram free PDO mapping (p8744 = 2) - 9204 -
  

Communication Board CAN10 (CBC10) - receive telegram predef. conn. Set (p8744 = 1) - 9206 -
  

Communication Board CAN10 (CBC10) - send telegram free PDO mapping (p8744 = 2) - 9208 -
  

Communication Board CAN10 (CBC10) - send telegram predef. conn. Set (p8744 = 1) - 9210 -
  

Communication Board CAN10 (CBC10) - control word CANopen - 9220 -
  

Communication Board CAN10 (CBC10) - status word CANopen - 9226 -
  

Terminal Module 15 (TM15) - overview TM15DI_DO (SINAMICS) - 9399 -
  

Terminal Module 15 (TM15) - digital inputs/outputs bidirectional (DI/DO 0 ... DI/DO 7) - 9400 -
  

Terminal Module 15 (TM15) - digital inputs/outputs bidirectional (DI/DO 8 ... DI/DO 15) - 9401 -
  

Terminal Module 15 (TM15) - digital inputs/outputs, bidirectional (DI/DO 16 ... DI/DO 23) - 9402 -
  

Terminal Module 31 (TM31) - overview - 9549 -
  

Terminal Module 31 (TM31) - electrically isolated digital inputs (DI 0 ... DI 3) - 9550 -
  

Terminal Module 31 (TM31) - electrically isolated digital inputs (DI 4 ... DI 7) - 9552 -
  

Terminal Module 31 (TM31) - electrically isolated digital relay outputs (DO 0 ... DO 1) - 9556 -
  

Terminal Module 31 (TM31) - digital inputs/outputs bidirectional (DI/DO 8 ... DI/DO 9) - 9560 -
  

Terminal Module 31 (TM31) - digital inputs/outputs, bidirectional (DI/DO 10 ... DI/DO 11) - 9562 -
  

Terminal Module 31 (TM31) - analog input 0 (AI 0) - 9566 -
  

Terminal Module 31 (TM31) - analog input 1 (AI 1) - 9568 -
  

Terminal Module 31 (TM31) - analog outputs (AO 0 ... AO 1) - 9572 -
  

Terminal Module 31 (TM31) - temperature evaluation - 9576 -
  

Terminal Module 31 (TM31) - sensor monitoring KTY/PTC/PT1000 - 9577 -
  

Terminal Module 150 (TM150) - temperature evaluation structure (channel 0 ... 11) - 9625 -
  

Terminal Module 150 (TM150) - temperature evaluation 1x2-, 3-, 4-wire (channels 0 … 5) - 9626 -
  

Terminal Module 150 (TM150) - temperature evaluation 2x2-wire (channels 0 ... 11) - 9627 -
  

Auxiliaries - cooling unit overview (r0108.28 = 1) - 9792 -
  

Auxiliaries - cooling unit, control and feedback signals (r0108.28 = 1) - 9794 -
  

Auxiliaries - cooling unit sequence control (r0108.28 = 1) - 9795 -
  

Auxiliaries - cooling unit, conductivity monitoring (r0108.28 = 1) - 9796 -
  

Auxiliaries - cooling unit, temperature monitoring (r0108.28 = 1) - 9797 -
  

Auxiliaries - cooling unit, flow monitoring, leak monitoring (r0108.28 = 1) - 9798 -
  

Auxiliaries - cooling unit, pressure monitoring (r0108.28 = 1) - 9799 -
  

Auxiliaries - circuit breaker, time diagram - 9800 -
  

Auxiliaries - circuit breaker, control and feedback signals - 9801 -
  

Auxiliaries - circuit breaker, control and monitoring - 9802 -
  

Auxiliaries - fan, sequence control (r0108.27 = 1) - 9805 -
  

Auxiliaries - output switch, sequence control - 9806 -
  

Auxiliaries - output disconnector, sequence control - 9825 -
  

Auxiliaries - door release - 9827 -
  

Auxiliaries - precharging overview - 9833 -
  

Auxiliaries - precharging, sequence control - 9834 -
  

Auxiliaries - auxiliary fan overview (r0172.29 = 1) - 9836 -
  

Auxiliaries - auxiliary fan temperature monitoring (r0172.29 = 1) - 9837 -
  

Auxiliaries - auxiliary fan cabinet control (r0172.29 = 1) - 9838 -
  

Auxiliaries - auxiliary fan, fan control (r0172.29 = 1) - 9839 -
  

Auxiliaries - auxiliary fan OR logic operation 0 … 7 - 9840 -
  

Auxiliaries - braking controller (r0108.26 = 1, r0172.1 = 1) - 9841 -
  

Auxiliaries - external pulse inhibit - 9845 -
  

Voltage Sensing Module (VSM) - analog inputs (AI 2 ... AI 3) - 9880 -
  

Power Stack Adapter (PSA4, PSA5) - connection overview - 9981 -
  

Power Stack Adapter (PSA4, PSA5) - digital inputs (DI 0 ... DI 7) - 9982 -
  

Power Stack Adapter (PSA4, PSA5) - digital inputs (DI 0 ... DI 7) - 9982 -
  

Power Stack Adapter (PSA4, PSA5) - digital outputs (DO 0 ... DO 7) - 9983 -
  

Power Stack Adapter (PSA4, PSA5) - digital outputs (DO 0 ... DO 7) - 9983 -
  

Power Stack Adapter (PSA4, PSA5) - analog inputs (AI 0 … AI 3) - 9984 -
  

Power Stack Adapter (PSA4, PSA5) - temperature sensor (PT100) - 9985 -
  

Power Stack Adapter (PSA4, PSA5) - analog outputs (AO 0 ... AO 7) - 9986 -
  

Power Stack Adapter (PSA4, PSA5) - digital inputs/outputs (DI/DO 0 ... DI/DO 3) - 9987 -
  

Power Stack Adapter (PSA4, PSA5) - digital inputs/outputs (DI/DO 0 ... DI/DO 3) - 9987 -
  

Power Stack Adapter (PSA4, PSA5) - digital inputs/outputs (DI/DO 4 ... DI/DO 7) - 9988 -
  

Power Stack Adapter (PSA4, PSA5) - digital inputs/outputs (DI/DO 4 ... DI/DO 7) - 9988 -

#### Function Diagrams for SINAMICS SM150 - Overview

The structure of the drive functions and the relationship of the individual parameters with other parameters is displayed in the function diagrams:

Explanations of the function diagrams - explanation of the symbols (Part 1) - 1020 -
  

Explanations of the function diagrams - explanation of the symbols (Part 2) - 1021 -
  

Explanations of the function diagrams - explanation of the symbols (Part 3) - 1022 -
  

Explanations of the function diagrams - handling BICO technology - 1030 -
  

CU320-2 input/output terminals - overview - 2119 -
  

CU320-2 input/output terminals - electrically isolated digital inputs (DI 0 ... DI 3, DI 16, DI 17) - 2120 -
  

CU320-2 input/output terminals - electrically isolated digital inputs (DI 4 ... DI 7, DI 20, DI 21) - 2121 -
  

CU320-2 input/output terminals - digital inputs/outputs bidirect. (DI/DO 8 ... DI/DO 9) - 2130 -
  

CU320-2 input/output terminals - digital inputs/outputs bidirect. (DI/DO 10 ... DI/DO 11) - 2131 -
  

CU320-2 input/output terminals - digital inputs/outputs bidirect. (DI/DO 12 ... DI/DO 13) - 2132 -
  

CU320-2 input/output terminals - digital inputs/outputs bidirect. (DI/DO 14 ... DI/DO 15) - 2133 -
  

Control Unit communication - SINAMICS Link overview (r0108.31 = 1, p8835 = 3) - 2197 -
  

Control Unit communication - SINAMICS Link configuration (r0108.31 = 1, p8835 = 3) - 2198 -
  

Control Unit communication - SINAMICS Link receive data (r0108.31 = 1, p8835 = 3) - 2199 -
  

Control Unit communication - SINAMICS Link send data (r0108.31 = 1, p8835 = 3) - 2200 -
  

PROFIdrive - overview - 2401 -
  

PROFIdrive - PROFIBUS (PB) / PROFINET (PN), addresses and diagnostics - 2410 -
  

PROFIdrive - standard telegrams and process data (PZD) - 2415 -
  

PROFIdrive - manufacturer-specific/free telegrams and process data (PZD) - 2416 -
  

PROFIdrive - PZD receive signals, interconnection - 2439 -
  

PROFIdrive - STW1 control word, interconnection - 2442 -
  

PROFIdrive - I_STW1 control word, infeed interconnection - 2447 -
  

PROFIdrive - PZD send signals, interconnection - 2449 -
  

PROFIdrive - ZSW1 status word, interconnection - 2452 -
  

PROFIdrive - I_ZSW1 status word, infeed interconnection - 2457 -
  

PROFIdrive - IF1 receive telegram, free interconnection via BICO (p0922 = 999) - 2468 -
  

PROFIdrive - IF1 send telegram, free interconnection via BICO (p0922 = 999) - 2470 -
  

PROFIdrive - IF1 status words, free interconnection - 2472 -
  

PROFIdrive - IF1 receive telegram, free interconnection via BICO (p0922 = 999) - 2481 -
  

PROFIdrive - IF1 send telegram, free interconnection via BICO (p0922 = 999) - 2483 -
  

PROFIdrive - IF2 receive telegram, free interconnection via BICO (p0922 = 999) - 2485 -
  

PROFIdrive - IF2 send telegram, free interconnection via BICO (p0922 = 999) - 2487 -
  

PROFIdrive - IF2 status words, free interconnection - 2489 -
  

PROFIdrive - IF2 receive telegram, free interconnection via BICO (p0922 = 999) - 2491 -
  

PROFIdrive - IF2 send telegram, free interconnection via BICO (p0922 = 999) - 2493 -
  

PROFIdrive - CU_STW1 control word 1, Control Unit interconnection - 2495 -
  

PROFIdrive - CU_ZSW1 status word 1 Control Unit interconnection - 2496 -
  

PROFIdrive - O_DIGITAL interconnection - 2497 -
  

PROFIdrive - I_DIGITAL interconnection - 2498 -
  

PROFIdrive - I_DIGITAL_1 interconnection - 2500 -
  

Internal control/status words - control word, sequence control - 2501 -
  

Internal control/status words - status word, sequence control - 2503 -
  

Internal control/status words - control word, setpoint channel - 2505 -
  

Internal control/status words - control commands, sequence control - 2512 -
  

Internal control/status words - status word 2, sequence control - 2513 -
  

Internal control/status words - control word, speed controller - 2520 -
  

Internal control/status words - status word speed controller - 2522 -
  

Internal control/status words - status word, closed-loop control - 2526 -
  

Internal control/status words - status word, monitoring functions 1 - 2534 -
  

Internal control/status words - status word, monitoring functions 2 - 2536 -
  

Internal control/status words - status word, monitoring functions 3 - 2537 -
  

Internal control/status words - control word faults/alarms - 2546 -
  

Internal control/status words - status word, faults/alarms 1 and 2 - 2548 -
  

Sequence control - sequencer (1) - 2640 -
  

Sequence control - sequencer (2) - 2641 -
  

Sequence control - sequencer (3) - 2642 -
  

Sequence control - sequencer (4) - 2643 -
  

Sequence control - sequencer (5) - 2644 -
  

Sequence control - sequencer (6) - 2645 -
  

Sequence control - missing enables - 2654 -
  

Setpoint channel - overview - 3001 -
  

Setpoint channel - fixed speed setpoints - 3010 -
  

Setpoint channel - motorized potentiometer - 3020 -
  

Setpoint channel - main setpoint/additional setpoint, setpoint scaling, jog - 3030 -
  

Setpoint channel - direction limitation and direction reversal - 3040 -
  

Setpoint channel - skip frequency bands and speed limits - 3050 -
  

Setpoint channel - basic ramp-function generator - 3060 -
  

Setpoint channel - extended ramp-function generator - 3070 -
  

Setpoint channel - ramp-function generator selection, status word, tracking - 3080 -
  

Encoder evaluation - overview - 4702 -
  

Encoder evaluation - raw signal acquisition - 4704 -
  

Encoder evaluation - actual speed value and pole position sensing encoder 1, n_act_filter 5 - 4715 -
  

Encoder evaluation - absolute value for incremental encoder - 4750 -
  

Vector control - speed control and generation of the torque limits, overview - 6020 -
  

Vector control - speed setpoint, droop - 6030 -
  

Vector control - pre-control balancing reference/acceleration model - 6031 -
  

Vector control - speed controller with/without encoder - 6040 -
  

Vector control - speed controller adaptation (Kp_n/Tn_n adaptation) - 6050 -
  

Vector control - torque setpoint - 6060 -
  

Vector control - switchover to encoderless operation (SESM, p0300=5) - 6070 -
  

Vector control - Vdc_max controller and Vdc_min controller - 6220 -
  

Vector control - U/f and I/f setpoint generator - 6301 -
  

Vector control - derating for U/f control - 6302 -
  

Vector control - speed control configuration - 6490 -
  

Vector control - excitation (SESM, p0300 = 5) - 6495 -
  

Vector control - excitation sequential control system (SESM, p0300 = 5) - 6496 -
  

Vector control - upper/lower torque limit - 6630 -
  

Vector control - current/power/torque limits - 6640 -
  

Vector control - current control, overview - 6700 -
  

Vector control - current setpoint filter - 6710 -
  

Vector control - pre-control current controller (SESM, p0300 = 5) - 6713 -
  

Vector control - Iq and Id controllers - 6714 -
  

Vector control - Vdc balancing control - 6717 -
  

Vector control - flux setpoint calculation (ASM, p0300 = 1) - 6723 -
  

Vector control - field weakening controller (PMSM, p0300 = 2) - 6724 -
  

Vector control - flux setpoint calculation (SESM, p0300 = 5) - 6725 -
  

Vector control - field weakening controller, flux controller (SESM, p0300 = 5) - 6726 -
  

Vector control - current model, orientation angle selection (SESM, p0300 = 5) - 6727 -
  

Vector control - cos phi control, minimum current (SESM, p0300 = 5) - 6728 -
  

Vector control - interface to the power unit (ASM, PMSM, p0300 = 1, 2) - 6730 -
  

Vector control - interface to the power unit (SESM, p0300 = 5) - 6732 -
  

Vector control - switching frequency reduction for space vector approximation (SVA) - 6760 -
  

Vector control - automatic restart overview - 6762 -
  

Vector control - automatic restart, sequence control - 6763 -
  

Vector control - extended buffering for short voltage dips, sequence control - 6765 -
  

Vector control - excitation current setpoint, negative-sequence excitation (SESM, p0300 = 5) - 6770 -
  

Vector control - display signals - 6799 -
  

Technology functions - friction characteristic - 7010 -
  

Technology functions - synchronizing - 7020 -
  

General - 7200 -
  

Logic function blocks - AND (AND function block with 4 inputs) - 7210 -
  

Logic function blocks - OR (OR function block with 4 inputs) - 7212 -
  

Logic function blocks - XOR (XOR function block with 4 inputs) - 7214 -
  

Logic function blocks - NOT (inverter) - 7216 -
  

Arithmetic function blocks - ADD (adder with 4 inputs), SUB (subtractor) - 7220 -
  

Arithmetic function blocks - MUL (multiplier), DIV (divider) - 7222 -
  

Arithmetic function blocks - AVA (absolute value generator) - 7224 -
  

Timing function blocks - MFP (pulse generator), PCL (pulse contractor) - 7230 -
  

Timing function blocks - PDE (ON delay device), PDF (OFF delay device) - 7232 -
  

Timing function blocks - PST (pulse stretcher) - 7234 -
  

Memory function blocks - RSR (RS flip-flop), DFR (D flip-flop) timing function blocks - PST (pulse stretcher) - 7240 -
  

Switch function blocks - BSW (binary switch), NSW (numeric switch) - 7250 -
  

Control function blocks - LIM (limiter) - 7260 -
  

Control function blocks - PT1 (smoothing element) - 7262 -
  

Control function blocks - INT (integrator), DIF (derivative-action element) - 7264 -
  

Complex function blocks - LVM (double-sided limit monitor with hysteresis) - 7270 -
  

Technology controller - fixed values, binary selection (r0108.16 = 1 and p2216 = 2) - 7950 -
  

Technology controller - motorized potentiometer (r0108.16 = 1) - 7954 -
  

Technology controller - control (r0108.16 = 1) - 7958 -
  

Signals and monitoring functions - speed signals - 8010 -
  

Signals and monitoring functions - torque signals, motor blocked/stalled - 8012 -
  

Signals and monitoring functions - load monitoring (r0108.17 = 1) - 8013 -
  

Signals and monitoring functions - thermal monitoring power unit - 8014 -
  

Signals and monitoring functions - rotor temperature model - 8015 -
  

Signals and monitoring functions - thermal monit. power unit/motor, current reduction - 8016 -
  

Signals and monitoring functions - I2t motor monitoring - 8017 -
  

Signals and monitoring functions - output current monitoring - 8022 -
  

Signals and monitoring functions - output voltage monitoring - 8024 -
  

Signals and monitoring functions - Vdc monitoring - 8028 -
  

Signals and monitoring functions - external digital messages - 8030 -
  

Signals and monitoring functions - external analog signals - 8031 -
  

Signals and monitoring functions - auxiliary circuit monitoring (r0172.0 = 1) - 8037 -
  

Signals and monitoring functions - EMERGENCY STOP category 0 or 1 - 8044 -
  

Diagnostics - overview - 8050 -
  

Diagnostics - fault buffer - 8060 -
  

Diagnostics - alarm buffer - 8065 -
  

Diagnostics - faults/alarms trigger word (r2129) - 8070 -
  

Diagnostics - faults/alarms configuration - 8075 -
  

Diagnostics - measuring sockets (T0, T1, T2) - 8134 -
  

Diagnostics - recorder overview - 8144 -
  

Diagnostics - recorder sequence control - 8145 -
  

Diagnostics - test operation, IGCT power semiconductor (p6650 = 4) - 8146 -
  

Data sets - command data sets (CDS) - 8560 -
  

Data sets - drive data sets (DDS) - 8565 -
  

Data sets - encoder data sets (EDS) - 8570 -
  

Data sets - motor data sets (MDS) - 8575 -
  

Basic Infeed - overview - 8710 -
  

Basic Infeed - control word sequence control infeed - 8720 -
  

Basic Infeed - status word, sequence control, infeed - 8726 -
  

Basic Infeed - control commands, sequence control, infeed - 8729 -
  

Basic Infeed - status word 2, sequence control, infeed - 8730 -
  

Basic Infeed - sequencer (1) - 8732 -
  

Basic Infeed - sequencer (2) - 8733 -
  

Basic Infeed - sequencer (3) - 8734 -
  

Basic Infeed - sequencer (4) - 8735 -
  

Basic Infeed - sequencer (5) - 8736 -
  

Active Infeed - missing enables - 8738 -
  

Basic Infeed - interface to the Basic Line Module - 8750 -
  

Basic Infeed - signals and monitoring functions, line voltage monitoring (1) - 8761 -
  

Basic Infeed - signals and monitoring functions, line voltage monitoring (2) - 8762 -
  

Basic Infeed - signals and monitoring functions, Vdc monitoring (1) - 8764 -
  

Basic Infeed - signals and monitoring functions, Vdc monitoring (2) - 8765 -
  

Basic Infeed - thermal monitoring, infeed, derating - 8770 -
  

Active Infeed - overview - 8910 -
  

Active Infeed - control word sequence control infeed - 8920 -
  

Active Infeed - status word sequence control infeed - 8926 -
  

Active Infeed - status word, infeed - 8928 -
  

Active Infeed - control commands, sequence control, infeed - 8929 -
  

Active Infeed - status word 2, sequence control, infeed - 8930 -
  

Active Infeed - sequencer (1) - 8932 -
  

Active Infeed - sequencer (2) - 8933 -
  

Active Infeed - sequencer (3) - 8934 -
  

Active Infeed - sequencer (4) - 8935 -
  

Active Infeed - sequencer (5) - 8936 -
  

Active Infeed - missing enables - 8938 -
  

Active Infeed - controller, DC link voltage and reactive power - 8940 -
  

Active Infeed - power pre-control, decoupling - 8942 -
  

Active Infeed - actual value acquisition - 8944 -
  

Active Infeed - current DC component and current negative phase sequence control - 8946 -
  

Active Infeed - Vdc balancing control - 8947 -
  

Active Infeed - current control - 8949 -
  

Active Infeed - interface to the Active Line Module - 8950 -
  

Active Infeed - signals and monitoring functions - 8960 -
  

Active Infeed - signals and monitoring functions, line voltage monitoring (1) - 8961 -
  

Active Infeed - signals and monitoring functions, line voltage monitoring (2) - 8962 -
  

Active Infeed - signals and monitoring functions, Vdc monitoring - 8964 -
  

Active Infeed - thermal monitoring, infeed, derating - 8970 -
  

Active Infeed - display signals - 8999 -
  

Terminal Board 30 (TB30) - overview - 9099 -
  

Terminal Board 30 (TB30) - electrically isolated digital inputs (DI 0 ... DI 3) - 9100 -
  

Terminal Board 30 (TB30) - electrically isolated digital outputs (DO 0 ... DO 3) - 9102 -
  

Terminal Board 30 (TB30) - analog inputs (AI 0 ... AI 1) - 9104 -
  

Terminal Board 30 (TB30) - analog outputs (AO 0 ... AO 1) - 9106 -
  

Communication Board CAN10 (CBC10) - receive telegram free PDO mapping (p8744 = 2) - 9204 -
  

Communication Board CAN10 (CBC10) - receive telegram predef. conn. Set (p8744 = 1) - 9206 -
  

Communication Board CAN10 (CBC10) - send telegram free PDO mapping (p8744 = 2) - 9208 -
  

Communication Board CAN10 (CBC10) - send telegram predef. conn. Set (p8744 = 1) - 9210 -
  

Communication Board CAN10 (CBC10) - control word CANopen - 9220 -
  

Communication Board CAN10 (CBC10) - status word CANopen - 9226 -
  

Terminal Module 15 (TM15) - overview TM15DI_DO (SINAMICS) - 9399 -
  

Terminal Module 15 (TM15) - digital inputs/outputs bidirectional (DI/DO 0 ... DI/DO 7) - 9400 -
  

Terminal Module 15 (TM15) - digital inputs/outputs bidirectional (DI/DO 8 ... DI/DO 15) - 9401 -
  

Terminal Module 15 (TM15) - digital inputs/outputs, bidirectional (DI/DO 16 ... DI/DO 23) - 9402 -
  

Terminal Module 31 (TM31) - overview - 9549 -
  

Terminal Module 31 (TM31) - electrically isolated digital inputs (DI 0 ... DI 3) - 9550 -
  

Terminal Module 31 (TM31) - electrically isolated digital inputs (DI 4 ... DI 7) - 9552 -
  

Terminal Module 31 (TM31) - electrically isolated digital relay outputs (DO 0 ... DO 1) - 9556 -
  

Terminal Module 31 (TM31) - digital inputs/outputs bidirectional (DI/DO 8 ... DI/DO 9) - 9560 -
  

Terminal Module 31 (TM31) - digital inputs/outputs, bidirectional (DI/DO 10 ... DI/DO 11) - 9562 -
  

Terminal Module 31 (TM31) - analog input 0 (AI 0) - 9566 -
  

Terminal Module 31 (TM31) - analog input 1 (AI 1) - 9568 -
  

Terminal Module 31 (TM31) - analog outputs (AO 0 ... AO 1) - 9572 -
  

Terminal Module 31 (TM31) - temperature evaluation - 9576 -
  

Terminal Module 31 (TM31) - sensor monitoring KTY/PTC/PT1000 - 9577 -
  

Terminal Module 150 (TM150) - temperature evaluation structure (channel 0 ... 11) - 9625 -
  

Terminal Module 150 (TM150) - temperature evaluation 1x2-, 3-, 4-wire (channels 0 … 5) - 9626 -
  

Terminal Module 150 (TM150) - temperature evaluation 2x2-wire (channels 0 ... 11) - 9627 -
  

Auxiliaries - cooling unit overview (r0108.28 = 1) - 9792 -
  

Auxiliaries - cooling unit, control and feedback signals (r0108.28 = 1) - 9794 -
  

Auxiliaries - cooling unit sequence control (r0108.28 = 1) - 9795 -
  

Auxiliaries - cooling unit, conductivity monitoring (r0108.28 = 1) - 9796 -
  

Auxiliaries - cooling unit, temperature monitoring (r0108.28 = 1) - 9797 -
  

Auxiliaries - cooling unit, flow monitoring, leak monitoring (r0108.28 = 1) - 9798 -
  

Auxiliaries - cooling unit, pressure monitoring (r0108.28 = 1) - 9799 -
  

Auxiliaries - circuit breaker, time diagram - 9800 -
  

Auxiliaries - circuit breaker, control and feedback signals - 9801 -
  

Auxiliaries - circuit breaker, control and monitoring - 9802 -
  

Auxiliaries - fan, sequence control (r0108.27 = 1) - 9805 -
  

Auxiliaries - output switch, sequence control - 9806 -
  

Auxiliaries - output disconnector, sequence control - 9825 -
  

Auxiliaries - door release - 9827 -
  

Auxiliaries - precharging overview - 9833 -
  

Auxiliaries - precharging, sequence control - 9834 -
  

Auxiliaries - auxiliary fan overview (r0172.29 = 1) - 9836 -
  

Auxiliaries - auxiliary fan temperature monitoring (r0172.29 = 1) - 9837 -
  

Auxiliaries - auxiliary fan cabinet control (r0172.29 = 1) - 9838 -
  

Auxiliaries - auxiliary fan, fan control (r0172.29 = 1) - 9839 -
  

Auxiliaries - auxiliary fan OR logic operation 0 … 7 - 9840 -
  

Auxiliaries - braking controller (r0108.26 = 1, r0172.1 = 1) - 9841 -
  

Auxiliaries - external pulse inhibit - 9845 -
  

Voltage Sensing Module (VSM) - analog inputs (AI 2 ... AI 3) - 9880 -
  

Power Stack Adapter (PSA4, PSA5) - connection overview - 9981 -
  

Power Stack Adapter (PSA4, PSA5) - digital inputs (DI 0 ... DI 7) - 9982 -
  

Power Stack Adapter (PSA4, PSA5) - digital inputs (DI 0 ... DI 7) - 9982 -
  

Power Stack Adapter (PSA4, PSA5) - digital outputs (DO 0 ... DO 7) - 9983 -
  

Power Stack Adapter (PSA4, PSA5) - digital outputs (DO 0 ... DO 7) - 9983 -
  

Power Stack Adapter (PSA4, PSA5) - analog inputs (AI 0 … AI 3) - 9984 -
  

Power Stack Adapter (PSA4, PSA5) - temperature sensor (PT100) - 9985 -
  

Power Stack Adapter (PSA4, PSA5) - analog outputs (AO 0 ... AO 7) - 9986 -
  

Power Stack Adapter (PSA4, PSA5) - digital inputs/outputs (DI/DO 0 ... DI/DO 3) - 9987 -
  

Power Stack Adapter (PSA4, PSA5) - digital inputs/outputs (DI/DO 0 ... DI/DO 3) - 9987 -
  

Power Stack Adapter (PSA4, PSA5) - digital inputs/outputs (DI/DO 4 ... DI/DO 7) - 9988 -
  

Power Stack Adapter (PSA4, PSA5) - digital inputs/outputs (DI/DO 4 ... DI/DO 7) - 9988 -

#### Function Diagrams for SINAMICS SM120 - Overview

The structure of the drive functions and the relationship of the individual parameters with other parameters is displayed in the function diagrams:

Explanations of the function diagrams - explanation of the symbols (Part 1) - 1020 -
  

Explanations of the function diagrams - explanation of the symbols (Part 2) - 1021 -
  

Explanations of the function diagrams - explanation of the symbols (Part 3) - 1022 -
  

Explanations of the function diagrams - handling BICO technology - 1030 -
  

CU320-2 input/output terminals - overview - 2119 -
  

CU320-2 input/output terminals - electrically isolated digital inputs (DI 0 ... DI 3, DI 16, DI 17) - 2120 -
  

CU320-2 input/output terminals - electrically isolated digital inputs (DI 4 ... DI 7, DI 20, DI 21) - 2121 -
  

CU320-2 input/output terminals - digital inputs/outputs bidirect. (DI/DO 8 ... DI/DO 9) - 2130 -
  

CU320-2 input/output terminals - digital inputs/outputs bidirect. (DI/DO 10 ... DI/DO 11) - 2131 -
  

CU320-2 input/output terminals - digital inputs/outputs bidirect. (DI/DO 12 ... DI/DO 13) - 2132 -
  

CU320-2 input/output terminals - digital inputs/outputs bidirect. (DI/DO 14 ... DI/DO 15) - 2133 -
  

Control Unit communication - SINAMICS Link overview (r0108.31 = 1, p8835 = 3) - 2197 -
  

Control Unit communication - SINAMICS Link configuration (r0108.31 = 1, p8835 = 3) - 2198 -
  

Control Unit communication - SINAMICS Link receive data (r0108.31 = 1, p8835 = 3) - 2199 -
  

Control Unit communication - SINAMICS Link send data (r0108.31 = 1, p8835 = 3) - 2200 -
  

Control Unit communication - scaling for data transfer, multiplexer, overview - 2203 -
  

Control Unit communication - scaling for data transfer (rescaling) - 2204 -
  

PROFIdrive - overview - 2401 -
  

PROFIdrive - PROFIBUS (PB) / PROFINET (PN), addresses and diagnostics - 2410 -
  

PROFIdrive - standard telegrams and process data (PZD) - 2415 -
  

PROFIdrive - manufacturer-specific/free telegrams and process data (PZD) - 2416 -
  

PROFIdrive - PZD receive signals, interconnection - 2439 -
  

PROFIdrive - STW1 control word, interconnection - 2442 -
  

PROFIdrive - I_STW1 control word, infeed interconnection - 2447 -
  

PROFIdrive - PZD send signals, interconnection - 2449 -
  

PROFIdrive - ZSW1 status word, interconnection - 2452 -
  

PROFIdrive - I_ZSW1 status word, infeed interconnection - 2457 -
  

PROFIdrive - IF1 receive telegram, free interconnection via BICO (p0922 = 999) - 2468 -
  

PROFIdrive - IF1 send telegram, free interconnection via BICO (p0922 = 999) - 2470 -
  

PROFIdrive - IF1 status words, free interconnection - 2472 -
  

PROFIdrive - IF1 receive telegram, free interconnection via BICO (p0922 = 999) - 2481 -
  

PROFIdrive - IF1 send telegram, free interconnection via BICO (p0922 = 999) - 2483 -
  

PROFIdrive - IF2 receive telegram, free interconnection via BICO (p0922 = 999) - 2485 -
  

PROFIdrive - IF2 send telegram, free interconnection via BICO (p0922 = 999) - 2487 -
  

PROFIdrive - IF2 status words, free interconnection - 2489 -
  

PROFIdrive - IF2 receive telegram, free interconnection via BICO (p0922 = 999) - 2491 -
  

PROFIdrive - IF2 send telegram, free interconnection via BICO (p0922 = 999) - 2493 -
  

PROFIdrive - CU_STW1 control word 1, Control Unit interconnection - 2495 -
  

PROFIdrive - CU_ZSW1 status word 1 Control Unit interconnection - 2496 -
  

PROFIdrive - O_DIGITAL interconnection - 2497 -
  

PROFIdrive - I_DIGITAL interconnection - 2498 -
  

PROFIdrive - I_DIGITAL_1 interconnection - 2500 -
  

Internal control/status words - control word, sequence control - 2501 -
  

Internal control/status words - status word, sequence control - 2503 -
  

Internal control/status words - control word, setpoint channel - 2505 -
  

Internal control/status words - control word, sequence control - 2507 -
  

Internal control/status words - status word, sequence control - 2508 -
  

Internal control/status words - control commands, sequence control - 2512 -
  

Internal control/status words - status word 2, sequence control - 2513 -
  

Internal control/status words - control commands, sequence control - 2516 -
  

Internal control/status words - status word 2, sequence control - 2517 -
  

Internal control/status words - control word, speed controller - 2520 -
  

Internal control/status words - status word speed controller - 2522 -
  

Internal control/status words - status word, closed-loop control - 2526 -
  

Internal control/status words - status word, monitoring functions 1 - 2534 -
  

Internal control/status words - status word, monitoring functions 2 - 2536 -
  

Internal control/status words - status word, monitoring functions 3 - 2537 -
  

Internal control/status words - control word faults/alarms - 2546 -
  

Internal control/status words - status word, faults/alarms 1 and 2 - 2548 -
  

Sequence control - sequencer (1) - 2610 -
  

Sequence control - sequencer (2) - 2611 -
  

Sequence control - sequencer (3) - 2612 -
  

Sequence control - sequencer (4) - 2613 -
  

Sequence control - sequencer (5) - 2614 -
  

Sequence control - sequencer (6) - 2615 -
  

Sequence control - missing enables - 2634 -
  

Sequence control - sequencer (1) - 2660 -
  

Sequence control - sequencer (2) - 2661 -
  

Sequence control - sequencer (3) - 2662 -
  

Sequence control - sequencer (4) - 2663 -
  

Sequence control - sequencer (5) - 2664 -
  

Sequence control - sequencer (6) - 2665 -
  

Sequence control - missing enables - 2674 -
  

Sequence control - sequencer - 2680 -
  

Setpoint channel - overview - 3001 -
  

Setpoint channel - fixed speed setpoints - 3010 -
  

Setpoint channel - motorized potentiometer - 3020 -
  

Setpoint channel - main setpoint/additional setpoint, setpoint scaling, jog - 3030 -
  

Setpoint channel - direction limitation and direction reversal - 3040 -
  

Setpoint channel - skip frequency bands and speed limits - 3050 -
  

Setpoint channel - basic ramp-function generator - 3060 -
  

Setpoint channel - extended ramp-function generator - 3070 -
  

Setpoint channel - ramp-function generator selection, status word, tracking - 3080 -
  

Encoder evaluation - overview - 4702 -
  

Encoder evaluation - raw signal acquisition - 4704 -
  

Encoder evaluation - actual speed value and pole position sensing encoder 1, n_act_filter 5 - 4715 -
  

Encoder evaluation - absolute value for incremental encoder - 4750 -
  

Shaft generator - overview - 6010 -
  

Vector control - speed control and generation of the torque limits, overview - 6020 -
  

Vector control - speed setpoint, droop - 6030 -
  

Vector control - pre-control balancing reference/acceleration model - 6031 -
  

Vector control - speed controller with/without encoder - 6040 -
  

Vector control - speed controller adaptation (Kp_n/Tn_n adaptation) - 6050 -
  

Vector control - torque setpoint - 6060 -
  

Vector control - switchover to encoderless operation (SESM, p0300=5) - 6070 -
  

Vector control - Vdc_max controller and Vdc_min controller - 6220 -
  

Vector control - U/f and I/f setpoint generator - 6301 -
  

Vector control - derating for U/f control - 6302 -
  

Vector control - speed control configuration - 6490 -
  

Vector control - excitation (SESM, p0300 = 5) - 6495 -
  

Vector control - excitation sequential control system (SESM, p0300 = 5) - 6496 -
  

Vector control - upper/lower torque limit - 6630 -
  

Vector control - current/power/torque limits - 6640 -
  

Vector control - current setpoint filter - 6710 -
  

Vector control - pre-control current controller (SESM, p0300 = 5) - 6713 -
  

Vector control - flux setpoint calculation (ASM, p0300 = 1) - 6723 -
  

Vector control - flux setpoint calculation (SESM, p0300 = 5) - 6725 -
  

Vector control - field weakening controller, flux controller (SESM, p0300 = 5) - 6726 -
  

Vector control - current model, orientation angle selection (SESM, p0300 = 5) - 6727 -
  

Vector control - cos phi control, minimum current (SESM, p0300 = 5) - 6728 -
  

Vector control - interface to the power unit (ASM, PMSM, p0300 = 1, 2) - 6730 -
  

Vector control - interface to the power unit (SESM, p0300 = 5) - 6732 -
  

Vector control - automatic restart overview - 6762 -
  

Vector control - automatic restart, sequence control - 6763 -
  

Vector control - extended buffering for short voltage dips, sequence control - 6765 -
  

Vector control - excitation current setpoint, negative-sequence excitation (SESM, p0300 = 5) - 6770 -
  

Shaft generator - DC link voltage controller - 6780 -
  

Vector control - display signals - 6799 -
  

Technology functions - friction characteristic - 7010 -
  

Technology functions - synchronizing - 7020 -
  

General - 7200 -
  

Logic function blocks - AND (AND function block with 4 inputs) - 7210 -
  

Logic function blocks - OR (OR function block with 4 inputs) - 7212 -
  

Logic function blocks - XOR (XOR function block with 4 inputs) - 7214 -
  

Logic function blocks - NOT (inverter) - 7216 -
  

Arithmetic function blocks - ADD (adder with 4 inputs), SUB (subtractor) - 7220 -
  

Arithmetic function blocks - MUL (multiplier), DIV (divider) - 7222 -
  

Arithmetic function blocks - AVA (absolute value generator) - 7224 -
  

Timing function blocks - MFP (pulse generator), PCL (pulse contractor) - 7230 -
  

Timing function blocks - PDE (ON delay device), PDF (OFF delay device) - 7232 -
  

Timing function blocks - PST (pulse stretcher) - 7234 -
  

Memory function blocks - RSR (RS flip-flop), DFR (D flip-flop) timing function blocks - PST (pulse stretcher) - 7240 -
  

Switch function blocks - BSW (binary switch), NSW (numeric switch) - 7250 -
  

Control function blocks - LIM (limiter) - 7260 -
  

Control function blocks - PT1 (smoothing element) - 7262 -
  

Control function blocks - INT (integrator), DIF (derivative-action element) - 7264 -
  

Complex function blocks - LVM (double-sided limit monitor with hysteresis) - 7270 -
  

Branch current control - overview - 7601 -
  

Branch current control - complete cell voltage controller - 7603 -
  

Branch current control Iq and Id controller - 7605 -
  

Branch current control - actual value transformations, setpoint transformations - 7607 -
  

Branch current control - cell balancing control (positive sequence system) - 7609 -
  

Branch current control - cell balancing control (negative sequence system) - 7610 -
  

Braking chopper - overview - 7620 -
  

Braking chopper - calculation current setpoint - 7622 -
  

Braking chopper - calculation voltage setpoint - 7623 -
  

Braking chopper - enables, calculation pulse-width modulation - 7625 -
  

Technology controller - fixed values, binary selection (r0108.16 = 1 and p2216 = 2) - 7950 -
  

Technology controller - motorized potentiometer (r0108.16 = 1) - 7954 -
  

Technology controller - control (r0108.16 = 1) - 7958 -
  

Line transfer control/status word r1261 (bit 0 ... 15) - 7960 -
  

Line transfer control/status word r1261 (bit 16 ... 31) - 7961 -
  

Line transfer sequencer - 7962 -
  

Synchronoscope control/status word r3803 (bit 0 ... 15) - 7963 -
  

Synchronoscope control/status word r3803 (bit 16 ... 31) - 7964 -
  

Synchronoscope actual values - 7965 -
  

Internal synchronoscope sequencer - 7966 -
  

External synchronoscope sequencer - 7967 -
  

Synchronoscope setpoints - 7968 -
  

Line control - U/f and I/f setpoint generator - 7981 -
  

Line control - line droop - 7982 -
  

Signals and monitoring functions - speed signals - 8010 -
  

Signals and monitoring functions - torque signals, motor blocked/stalled - 8012 -
  

Signals and monitoring functions - load monitoring (r0108.17 = 1) - 8013 -
  

Signals and monitoring functions - thermal monitoring power unit - 8014 -
  

Signals and monitoring functions - rotor temperature model - 8015 -
  

Signals and monitoring functions - thermal monit. power unit/motor, current reduction - 8016 -
  

Signals and monitoring functions - I2t motor monitoring - 8017 -
  

Signals and monitoring functions - speed signals, excitation current monitoring - 8020 -
  

Signals and monitoring functions - line voltage monitoring (1) - 8026 -
  

Signals and monitoring functions - line voltage monitoring (2) - 8027 -
  

Signals and monitoring functions - Vdc monitoring - 8029 -
  

Signals and monitoring functions - external digital messages - 8030 -
  

Signals and monitoring functions - external analog signals - 8031 -
  

Signals and monitoring functions - circuit monitoring - 8032 -
  

Signals and monitoring functions - Vdc monitoring - 8034 -
  

Signals and monitoring functions - auxiliary circuit monitoring (r0172.0 = 1) - 8037 -
  

Signals and monitoring functions - I2t monitoring - 8038 -
  

Signals and monitoring functions - EMERGENCY STOP category 0 or 1 - 8044 -
  

Diagnostics - overview - 8050 -
  

Diagnostics - fault buffer - 8060 -
  

Diagnostics - alarm buffer - 8065 -
  

Diagnostics - faults/alarms trigger word (r2129) - 8070 -
  

Diagnostics - faults/alarms configuration - 8075 -
  

Diagnostics - measuring sockets (T0, T1, T2) - 8134 -
  

Diagnostics - recorder overview - 8144 -
  

Diagnostics - recorder sequence control - 8145 -
  

Data sets - command data sets (CDS) - 8560 -
  

Data sets - drive data sets (DDS) - 8565 -
  

Data sets - encoder data sets (EDS) - 8570 -
  

Data sets - motor data sets (MDS) - 8575 -
  

Internal control/status words - control word, sequence control - 8620 -
  

Internal control/status words - status word, sequence control - 8626 -
  

Internal control/status words - control commands, sequence control - 8629 -
  

Internal control/status words - status word 2, sequence control - 8630 -
  

Sequence control - sequencer (1) - 8632 -
  

Sequence control - sequencer (2) - 8633 -
  

Sequence control - sequencer (3) - 8634 -
  

Sequence control - sequencer (4) - 8635 -
  

Sequence control - sequencer (5) - 8636 -
  

Sequence control - sequencer (6) - 8637 -
  

Sequence control - missing enables - 8638 -
  

Basic Infeed - overview - 8710 -
  

Basic Infeed - control word sequence control infeed - 8720 -
  

Basic Infeed - status word, sequence control, infeed - 8726 -
  

Basic Infeed - control commands, sequence control, infeed - 8729 -
  

Basic Infeed - status word 2, sequence control, infeed - 8730 -
  

Basic Infeed - sequencer (1) - 8732 -
  

Basic Infeed - sequencer (2) - 8733 -
  

Basic Infeed - sequencer (3) - 8734 -
  

Basic Infeed - sequencer (4) - 8735 -
  

Basic Infeed - sequencer (5) - 8736 -
  

Active Infeed - missing enables - 8738 -
  

Basic Infeed - interface to the Basic Line Module - 8750 -
  

Basic Infeed - signals and monitoring functions, line voltage monitoring (1) - 8761 -
  

Basic Infeed - signals and monitoring functions, line voltage monitoring (2) - 8762 -
  

Basic Infeed - signals and monitoring functions, Vdc monitoring - 8765 -
  

Basic Infeed - signals and monitoring functions, phase failure monitoring - 8766 -
  

Basic Infeed - thermal monitoring, infeed, derating - 8770 -
  

Terminal Board 30 (TB30) - overview - 9099 -
  

Terminal Board 30 (TB30) - electrically isolated digital inputs (DI 0 ... DI 3) - 9100 -
  

Terminal Board 30 (TB30) - electrically isolated digital outputs (DO 0 ... DO 3) - 9102 -
  

Terminal Board 30 (TB30) - analog inputs (AI 0 ... AI 1) - 9104 -
  

Terminal Board 30 (TB30) - analog outputs (AO 0 ... AO 1) - 9106 -
  

Communication Board CAN10 (CBC10) - receive telegram free PDO mapping (p8744 = 2) - 9204 -
  

Communication Board CAN10 (CBC10) - receive telegram predef. conn. Set (p8744 = 1) - 9206 -
  

Communication Board CAN10 (CBC10) - send telegram free PDO mapping (p8744 = 2) - 9208 -
  

Communication Board CAN10 (CBC10) - send telegram predef. conn. Set (p8744 = 1) - 9210 -
  

Communication Board CAN10 (CBC10) - control word CANopen - 9220 -
  

Communication Board CAN10 (CBC10) - status word CANopen - 9226 -
  

Terminal Module 15 (TM15) - overview TM15DI_DO (SINAMICS) - 9399 -
  

Terminal Module 15 (TM15) - digital inputs/outputs bidirectional (DI/DO 0 ... DI/DO 7) - 9400 -
  

Terminal Module 15 (TM15) - digital inputs/outputs bidirectional (DI/DO 8 ... DI/DO 15) - 9401 -
  

Terminal Module 15 (TM15) - digital inputs/outputs, bidirectional (DI/DO 16 ... DI/DO 23) - 9402 -
  

Terminal Module 31 (TM31) - overview - 9549 -
  

Terminal Module 31 (TM31) - electrically isolated digital inputs (DI 0 ... DI 3) - 9550 -
  

Terminal Module 31 (TM31) - electrically isolated digital inputs (DI 4 ... DI 7) - 9552 -
  

Terminal Module 31 (TM31) - electrically isolated digital relay outputs (DO 0 ... DO 1) - 9556 -
  

Terminal Module 31 (TM31) - digital inputs/outputs bidirectional (DI/DO 8 ... DI/DO 9) - 9560 -
  

Terminal Module 31 (TM31) - digital inputs/outputs, bidirectional (DI/DO 10 ... DI/DO 11) - 9562 -
  

Terminal Module 31 (TM31) - analog input 0 (AI 0) - 9566 -
  

Terminal Module 31 (TM31) - analog input 1 (AI 1) - 9568 -
  

Terminal Module 31 (TM31) - analog outputs (AO 0 ... AO 1) - 9572 -
  

Terminal Module 31 (TM31) - temperature evaluation - 9576 -
  

Terminal Module 31 (TM31) - sensor monitoring KTY/PTC/PT1000 - 9577 -
  

Terminal Module 150 (TM150) - temperature evaluation structure (channel 0 ... 11) - 9625 -
  

Terminal Module 150 (TM150) - temperature evaluation 1x2-, 3-, 4-wire (channels 0 … 5) - 9626 -
  

Terminal Module 150 (TM150) - temperature evaluation 2x2-wire (channels 0 ... 11) - 9627 -
  

Auxiliaries - cooling unit overview (r0108.28 = 1) - 9792 -
  

Auxiliaries - cooling unit, control and feedback signals (r0108.28 = 1) - 9794 -
  

Auxiliaries - cooling unit sequence control (r0108.28 = 1) - 9795 -
  

Auxiliaries - cooling unit, conductivity monitoring (r0108.28 = 1) - 9796 -
  

Auxiliaries - cooling unit, temperature monitoring (r0108.28 = 1) - 9797 -
  

Auxiliaries - cooling unit, flow monitoring, leak monitoring (r0108.28 = 1) - 9798 -
  

Auxiliaries - cooling unit, pressure monitoring (r0108.28 = 1) - 9799 -
  

Auxiliaries - circuit breaker, time diagram - 9800 -
  

Auxiliaries - circuit breaker, control and feedback signals - 9801 -
  

Auxiliaries - circuit breaker, control and monitoring - 9802 -
  

Auxiliaries - fan, sequence control (r0108.27 = 1) - 9805 -
  

Auxiliaries - fan, monitoring (r0108.27 = 1) - 9806 -
  

Auxiliaries - fan, heat exchanger (r0108.27 = 1) - 9807 -
  

Auxiliaries - heat exchanger fan (r0108.27 = 1) inverter switch control - 9808 -
  

Auxiliaries - door release - 9827 -
  

Auxiliaries - precharging overview - 9833 -
  

Auxiliaries - precharging, sequence control - 9834 -
  

Auxiliaries - auxiliary fan overview (r0172.29 = 1) - 9836 -
  

Auxiliaries - auxiliary fan temperature monitoring (r0172.29 = 1) - 9837 -
  

Auxiliaries - auxiliary fan cabinet control (r0172.29 = 1) - 9838 -
  

Auxiliaries - auxiliary fan, fan control (r0172.29 = 1) - 9839 -
  

Auxiliaries - auxiliary fan OR logic operation 0 … 7 - 9840 -
  

Voltage Sensing Module (VSM) - analog inputs (AI 2 ... AI 3) - 9880 -
  

Power Stack Adapter (PSA4, PSA5) - connection overview - 9981 -
  

Power Stack Adapter (PSA4, PSA5) - digital inputs (DI 0 ... DI 7) - 9982 -
  

Power Stack Adapter (PSA4, PSA5) - digital outputs (DO 0 ... DO 7) - 9983 -
  

Power Stack Adapter (PSA4, PSA5) - analog inputs (AI 0 … AI 3) - 9984 -
  

Power Stack Adapter (PSA4, PSA5) - temperature sensor (PT100) - 9985 -
  

Power Stack Adapter (PSA4, PSA5) - analog outputs (AO 0 ... AO 7) - 9986 -
  

Power Stack Adapter (PSA4, PSA5) - digital inputs/outputs (DI/DO 0 ... DI/DO 3) - 9987 -
  

Power Stack Adapter (PSA4, PSA5) - digital inputs/outputs (DI/DO 4 ... DI/DO 7) - 9988 -

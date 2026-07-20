---
title: "Technology Extension DCDCCONV V2.10.13"
package: sdrpaDCDCCONV_2_10_13enUS
topics: 88
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Technology Extension DCDCCONV V2.10.13

This section contains the parameter descriptions for the Technology Extension.
In the table of contents, you will then see a separate entry for each parameter number.

## SINAMICS Parameter DCDCCONV 31660 - 32914

SINAMICS Parameter DCDCCONV 31660 - 32914

### p31660 DCDCCONV closed-loop control mode

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C1( 3) | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7461, 7463, 7473 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 2 | [ 0 ] 1 |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the closed-loop control mode.  
Using the Technology Extension DCDCCONV (TEC DCDCCONV), a Motor Module can be used
as step-down controller. This includes the measured value evaluation, the closed-loop
control itself as well as the output of the control voltage.

**Value:**
  
0:
Closed-loop voltage and closed-loop current control not active  
1:
Closed-loop voltage and closed-loop current control active  
2:
Closed-loop current control active

**Dependency:**
  
  
Refer to:
p31661

**Note:**
  
DCDCCONV: DC-DC converter  
Vdc: DC link voltage  
Output voltage/output current:  
Load voltage/load current after the smoothing element connected at the Motor Module.
The load voltage is the controlled variable for the voltage controller. The DC link
voltage is the controlled variable for the Vdc controller.  
Control voltage:  
Average voltage of the selected terminals at the Motor Module referred to terminal
DCN.  
Control current:  
Sum of the currents at the Motor Module output. The control current is the controlled
variable for the current controller.

### p31661 BI: DCDCCONV voltage control activation signal source

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 7461, 7463, 7473 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 1 |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the signal source to activate closed-loop voltage control in operation.  
BI: p31661 = 1 signal:  
- Closed-loop voltage control is active.  
BI: p31661 = 0 signal:  
- Closed-loop voltage control is not active.

**Dependency:**
  
Closed-loop voltage control can only be activated in mode "Closed-loop voltage and
current control" (p31660 = 1).  
  
Refer to:
p31660

### p31663 DCDCCONV configuration

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7467, 7477 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0000 bin |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Setting to configure the TEC DCDCCONV.

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Invert the output voltage actual value | No | Yes | 7467 |

**Note:**
  
For bit 00 = 1:  
The output voltage is inverted for the closed-loop control. This setting must be used
if the VSM senses a negative voltage value as a result of how it is connected.  
For bit 00 = 0:  
The output voltage is not inverted.  
VSM: Voltage Sensing Module

### p31664 DCDCCONV phase current difference smoothing time constant

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7465 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 [ms] | 250.00 [ms] | [ 0 ] 50.00 [ms] |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the smoothing time constant for the PT1 filter for the phase current difference.  
The filtered value is used exclusively to generate the fault F53461.

**Recommend.:**
  
The following settings are recommended for Motor Modules in the chassis format:  
p31664 = 2 * p32909

**Dependency:**
  
  
Refer to:
p32909  
Refer to:
F53461

**Note:**
  
In 3-phase operation, this value is applicable for each of the three phase current
differences.  
If the value is = 0, the filter is deactivated.

### p31665 DCDCCONV operating mode

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C1( 3) | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7460, 7467, 7468, 7472, 7478 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 1 | 4 | [ 0 ] 1 |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the operating mode and the connecting terminals that are used.  
For Motor Modules, in addition to the selected terminals, the DCN terminal must also
be connected.  
For value = 1 .. 3:  
Selection of the connecting terminals for 2-phase operation.  
If value = 4:  
Selection for 3-phase operation.

**Value:**
  
1:
2-phase operation (U and V)  
2:
2-phase operation (U and W)  
3:
2-phase operation (V and W)  
4:
3-phase operation

**Note:**
  
For 3-phase operation, the Motor Module pulse frequency (p1800) is firmly specified
by the set current controller sampling time (p0115[0]). The pulse frequency is calculated
as follows:  
p1800 = 1/p0115[0]  
Example:  
p0115[0] = 250 µs results in p1800 = 4 kHz  
This value is automatically set by the TEC DCDCCONV when running up. The pulse frequency
must be changed via p0115[0].  
The overload response of the power unit (p0290) may only be set to values where the
pulse frequency is not reduced (p0290 = 0, 1 or 10). Fault F53468 indicates an invalid
setting.

### p31666 DCDCCONV maximum phase current difference

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7465 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 [A] | 1000.00 [A] | [ 0 ] 3.00 [A] |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the maximum permissible difference between two phase currents.

**Recommend.:**
  
The value for the maximum phase current difference must be set as low as possible.
For this purpose it makes sense to monitor parameter r31667 and to apply the maximum
value in p31666.  
Typical values for the maximum phase current difference (p31666) are approx. 10% of
the rated current (r0207[0]).

**Dependency:**
  
  
Refer to:
p31665  
Refer to:
F53461

**Note:**
  
In 3-phase operation, this value is applicable for each of the three phase current
differences.  
An appropriate fault is output when exceeded. For 3-phase operation, the fault is
output when a phase current difference is exceeded.

### r31667[0...3] CO: DCDCCONV phase current difference unfiltered

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7460, 7461, 7465, 7467 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**p2002 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [A] | - [A] | [ ] - [A] |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Display and connector output for the current difference between the selected phases.

**Index:**
  
[
0]:
Phase difference 2-phase  
[
1]:
Phase difference 3-phase between Iu and Iv  
[
2]:
Phase difference 3-phase between Iv and Iw  
[
3]:
Phase difference 3-phase between Iw and Iu

**Note:**
  
For index [0]:  
2-phase operation: current difference of the two selected phases.  
3-phase operation: the value is 0.  
For index [1..3]:  
3-phase operation: current difference between the relevant phases.  
2-phase operation: the value is 0.

### p31668 BI: DCDCCONV enable signal source

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 7462 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the signal source to enable the closed-loop control.  
This is a precondition for status bit "Enable available" (r31669.18).

**Recommend.:**
  
Recommended BICO interconnection:  
BI: p31668 = r0899.11 (pulses enabled)

### r31669.0...21 CO/BO: DCDCCONV status word

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Display and BICO output for the status word from DCDCCONV.

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Closed-loop voltage control active | No | Yes | 7466 |
| 01 | Output voltage higher than the DC link voltage | No | Yes | 7468 |
| 02 | Voltage controller I component frozen | No | Yes | 7463 |
| 03 | Closed-loop current control active | No | Yes | 7464 |
| 04 | Current controller lower setpoint limit active | No | Yes | 7463 |
| 05 | Current controller upper setpoint limit active | No | Yes | 7463 |
| 06 | Current controller I component frozen | No | Yes | 7464 |
| 07 | Lower control voltage limit active | No | Yes | 7464 |
| 08 | Upper control voltage limit active | No | Yes | 7464 |
| 09 | "VSM output voltage constant" active (A53464) | No | Yes | 7467 |
| 10 | DC link voltage lower limit active | No | Yes | 7466 |
| 11 | DC link voltage upper limit active | No | Yes | 7466 |
| 12 | Command to close DC contactor active | No | Yes | 7469 |
| 13 | Voltage controller active | No | Yes | 7463 |
| 14 | DC link voltage controller active | No | Yes | 7466 |
| 15 | Energy storage device charged and ready | No | Yes | 7462 |
| 16 | ON command active | No | Yes | 7462 |
| 17 | Noise minimization pulse enable | No | Yes | 7469 |
| 18 | Enable active | No | Yes | 7462 |
| 19 | Overvoltage detected | No | Yes | 7469 |
| 20 | 3-phase operation active | No | Yes | 7478 |
| 21 | VSM measured values internally verified | No | Yes | 7469 |

**Notice:**
  
For bit 17:  
When the pulses are inhibited, as a result of the activated noise minimization, a
dead time of 1 ... 2 ms can be expected until the pulses are enabled again.  
During noise minimization, no internal switching operations are performed and no currents
flow.

**Note:**
  
Vdc: DC link voltage  
VSM: Voltage Sensing Module  
For bit 00:  
The set bit indicates that either the voltage controller or the Vdc controller can
be used.  
Conditions for this are:  
- Mode "Closed-loop voltage and current control" (p31660 = 1) is set.  
- Closed-loop voltage control is activated via signal source (p31661 = 1).  
- All enable signals are available (r31669.18 = 1).  
Additional conditions so that the particular controller is active are "Closed-loop
voltage controller active" (r31669.13 = 1) respectively "Vdc controller active" (r31669.14
= 1).  
For bit 03:  
Closed-loop current control is active if the following conditions are complied with:  
- Mode "Closed-loop voltage and current control" (p31660 = 1) or mode "Closed-loop
current control" (p31660 = 2) is set.  
- All enable signals are available (r31669.18 = 1).  
For bits 07 and 08: In 3-phase operation, the set bit indicates that the control voltage
limiting is active on at least one of the three current controllers.  
For bit 09:  
The set bit indicates that within the monitoring time (p32910) the VSM supplied constant
voltage values. This is interpreted as failure of the voltage sensing function.  
For bit 10:  
The set bit indicates that the DC link voltage r0070 has fallen below the lower threshold
voltage p31722[1]. The bit remains set until the DC link voltage has increased by
the lower hysteresis voltage p31722[3].  
For bit 11:  
The set bit indicates that the DC link voltage r0070 has increased above the upper
threshold voltage p31722[0]. The bit remains set until the DC link voltage has decreased
by the upper hysteresis voltage p31722[2].  
For bit 12:  
For r31669.12 = 0, the DC contactor is opened, therefore disconnecting the load. This
occurs if the external command to open the DC contactor is active or the maximum output
voltage is exceeded.  
For bit 13:  
The voltage controller is active if the Vdc controller is not active (r31669.14 =
0).  
An additional condition that the voltage controller is active is "Closed-loop voltage
control active" (r31669.0 = 1).  
For bit 14:  
The Vdc controller is active if the following conditions are satisfied:  
- The Vdc controller is enabled via the signal source (p31724 = 1 signal).  
- Either the lower DC link voltage limit is active (r31669.10 = 1) or the upper DC
link voltage limit is active (r31669.11 = 1).  
An additional condition that the Vdc controller is active if "Closed-loop voltage
control active" (r31669.0 = 1).  
For bit 15:  
The set bit shows that when the power fails, energy is made available using the Vdc
controller.  
For bit 16:  
Output bit of the RS flip-flop for switching-on/switching-off.  
For r31669.16 = 1, the switch-on command is active.  
For r31669.16 = 0, the switch-off command is active.  
Recommended BICO interconnection:  
BI: p0840[0...n] = r31669.16  
The parameter p0840[0...n] is the precondition for pulse enable (r1838.2).  
For bit 17:  
The set bit indicates that the Vdc controller is active (r31669.14 = 1), or the output
voltage lies below the set hysteresis.  
Recommended BICO interconnection to minimize noise:  
BI: p0852[0...n] = r31669.17  
For bit 18:  
The set bit indicates that all preconditions for the enable are satisfied:  
- The signal source is enabled (p31668 = 1 signal).  
- The power unit pulses are enabled (r1838.2 = 1).  
- DC contactor feedback signal: contactor is closed (p32900[0] = 1 signal).  
For r31669.18 = 0 the following applies:  
The closed-loop current and voltage control is not active. When the closed-loop control
is deactivated, the measured output voltage is output.  
For bit 20:  
Controlling the power unit in the 3-phase operation is active if the following conditions
are satisfied:  
- Connecting terminal uses "Terminal U, V and W" is set (p31665 = 4).  
- Software gating unit of the vector control is activated (p0108.20 = 1).

### p31670 DCDCCONV output voltage setpoint

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7461, 7462, 7463, 7473 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| -340.28235E36 [V] | 340.28235E36 [V] | [ 0 ] 0.0 [V] |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the setpoint for the voltage controller.

**Dependency:**
  
  
Refer to:
p31671

### p31671 CI: DCDCCONV output voltage supplementary setpoint signal source

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7461, 7462, 7463, 7473 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**p2001 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the signal source for the supplementary setpoint of the voltage controller.

**Dependency:**
  
  
Refer to:
p31670

### p31672[0...1] DCDCCONV output voltage setting values

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7462, 7469 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 [V] | 340.28235E36 [V] | [ 0 ] 20 [V]  [ 1 ] 20 [V] |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the output voltage hysteresis for the pulse enable and the tolerance for the
ready signal.  
For index [0]:  
Binector output r31669.17 is set = 0 once the setpoint voltage has been reached.  
Binector output r31669.17 = 1 is set if the output voltage falls below the setpoint
minus the hysteresis setting value.  
The hysteresis is inactive if p31672[0] = 0.  
For index [1]:  
Once the setpoint voltage minus the tolerance has been reached (p31672[1]) signal
"Energy storage device charged and ready" (r31669.15 = 1) is set.

**Index:**
  
[
0]:
Pulse enable hysteresis  
[
1]:
Tolerance

**Dependency:**
  
  
Refer to:
p31670, p31671, r31679

### r31679[0...1] CO: DCDCCONV output voltage display

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7463, 7467, 7469, 7470, 7477 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**p2001 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [V] | - [V] | [ ] - [V] |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Display and connector output for the active setpoint and actual value of the output
voltage.

**Index:**
  
[
0]:
Setpoint active  
[
1]:
Actual value

**Dependency:**
  
For index [0]:  
The effective voltage setpoint depends on bit voltage controller active (r31669.13).  
The following applies for r31669.13 = 0:  
The value is set to the actual value of the output voltage (r31679[1]).  
The following applies for r31669.13 = 1:  
The value is the output from the voltage controller ramp-function generator.  
  
Refer to:
p31670, p31671, p31714, p31715, p32901  
Refer to:
A53463, A53466

**Note:**
  
For index [0]:  
The effective voltage setpoint is limited to the range between 0 V and the maximum
control voltage of the power unit being used.  
The value should not be less than the active lower control voltage limit (r31729),
and not higher than the active upper control voltage limit (r31728). Otherwise, a
remaining system deviation can occur, which means that the voltage controller reaches
its limit.

### p31680 CI: DCDCCONV output voltage actual value signal source

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7460, 7462, 7467, 7469, 7472, 7477 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**p2001 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the signal source for the actual value of the output voltage.

**Dependency:**
  
  
Refer to:
r31679

**Warning:**
  
If the Voltage Sensing Module (VSM) is either incorrectly connected or incorrectly
interconnected, then this can result in an uncontrolled flow of current and voltage
increase. This can cause injury and/or material damage.  
- Connect up the VSM correctly.  
- Interconnect the BICO output of the VSM with p31680 to match the existing wiring.

**Note:**
  
The output voltage must be measured for the closed-loop voltage control.

### p31681 DCDCCONV voltage controller Kp

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7463 |
| **Object:**SERVO | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 [A/V] | 340.28235E36 [A/V] | [ 0 ] 0.80 [A/V] |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the proportional gain (Kp) of the voltage controller.  
When adaptation is deactivated, the following applies:  
- This proportional gain is effective over the complete voltage range.  
When adaptation is activated, the following applies:  
- This proportional gain is active over the voltage range 0 ... p31685.

**Dependency:**
  
  
Refer to:
p31682, p31685, p31686

**Note:**
  
Adaptation is deactivated in the following cases:  
- p31682 = 100%  
- p31685 = p31686  
Adaptation is activated if the two following conditions are satisfied:  
1. p31682 not equal to 100 %  
2. p31685 < p31686

### p31681 DCDCCONV voltage controller Kp

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7463 |
| **Object:**VECTOR | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 | 340.28235E36 | [ 0 ] 0.80 |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the proportional gain (Kp) of the voltage controller.  
When adaptation is deactivated, the following applies:  
- This proportional gain is effective over the complete voltage range.  
When adaptation is activated, the following applies:  
- This proportional gain is active over the voltage range 0 ... p31685.

**Dependency:**
  
  
Refer to:
p31682, p31685, p31686

**Note:**
  
Adaptation is deactivated in the following cases:  
- p31682 = 100%  
- p31685 = p31686  
Adaptation is activated if the two following conditions are satisfied:  
1. p31682 not equal to 100 %  
2. p31685 < p31686

### p31682 DCDCCONV voltage controller upper Kp adaptation factor

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7463 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 [%] | 10000.00 [%] | [ 0 ] 100.00 [%] |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the adaptation factor for the proportional gain (Kp) in the upper adaptation
range (> p31686).  
The value is referred to p31681.

**Dependency:**
  
  
Refer to:
p31681, p31685, p31686

**Note:**
  
For the factory setting (p31682 = 100 %), adaptation is deactivated.

### p31683 DCDCCONV voltage controller Tn

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7463 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 [ms] | 340.28235E36 [ms] | [ 0 ] 12.00 [ms] |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the integral time (Tn) of the voltage controller.  
When adaptation is deactivated, the following applies:  
- This integral time is effective over the complete voltage range.  
When adaptation is activated, the following applies:  
- This integral time is active over the voltage range 0 ... p31685.

**Dependency:**
  
  
Refer to:
p31684, p31685, p31686, p31695, p31698

**Note:**
  
Adaptation is deactivated in the following cases:  
- p31684 = 100%  
- p31685 = p31686  
Adaptation is activated if the two following conditions are satisfied:  
1. p31684 not equal to 100 %  
2. p31685 < p31686  
The integral component is held if the sum of the voltage controller output and supplementary
setpoints exceeds the upper or lower current limit.

### p31684 DCDCCONV voltage controller upper Tn adaptation factor

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7463 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 1.00 [%] | 10000.00 [%] | [ 0 ] 100.00 [%] |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the adaptation factor for the integral time (Tn) in the upper adaptation range
(> p31686).  
The value is referred to p31683.

**Dependency:**
  
  
Refer to:
p31683, p31685, p31686

**Note:**
  
For the factory setting (p31684 = 100 %), adaptation is deactivated.

### p31685 DCDCCONV voltage controller adaptation lower voltage limit

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7463 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 [V] | 340.28235E36 [V] | [ 0 ] 0.00 [V] |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the lower voltage limit for the adaptation of the proportional gain (Kp) and
the integral time (Tn) of the voltage controller.  
The following values are active below this voltage:  
- Proportional gain (Kp): p31681  
- Integral time (Tn): p31683  
The corresponding values are linearly interpolated between this voltage and the upper
adaptation voltage (p31686).

**Dependency:**
  
  
Refer to:
p31681, p31682, p31683, p31684, p31686

**Note:**
  
The following must be observed:  
p31685 < p31686

### p31686 DCDCCONV voltage controller adaptation upper voltage limit

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7463 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 [V] | 340.28235E36 [V] | [ 0 ] 0.00 [V] |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the upper voltage limit for the adaptation of the proportional gain (Kp) and
the integral time (Tn) of the voltage controller.  
The following values are active above this voltage:  
- Proportional gain (Kp): p31681 x p31682  
- Integral time (Tn): p31683 x p31684  
The corresponding values are linearly interpolated between this voltage and the lower
adaptation voltage (p31685).

**Dependency:**
  
  
Refer to:
p31681, p31682, p31683, p31684, p31685

**Note:**
  
The following must be observed:  
p31685 < p31686

### p31688 BI: DCDCCONV voltage controller hold integrator

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 7463 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the signal source to hold the integrator for the voltage controller.

### p31689 CI: DCDCCONV voltage controller integrator setting val signal source

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7463 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**p2002 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the signal source for the integrator setting value for the voltage controller.  
For binector input p31690 = 0/1 signal, the setting value is accepted.

**Dependency:**
  
  
Refer to:
p31690

### p31690 BI: DCDCCONV voltage controller accept integrator setting value

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 7463 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the signal source to accept the setting value for the integrator (p31689).  
BI: p31690 = 0/1 signal:  
The setting value available via connector input p31689 is accepted.

**Dependency:**
  
  
Refer to:
p31689

### p31692 CI: DCDCCONV output current actual value signal source

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7460, 7467, 7472, 7477 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**p2002 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the signal source for the actual value of the output current.

**Note:**
  
It is not absolutely necessary to measure the output current.  
The signal value is added to the current setpoint.

### p31693 CI: DCDCCONV control current supplementary setpoint signal source

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7463 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**p2002 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the signal source for the supplementary setpoint of the current controller.

**Note:**
  
In 3-phase operation, the supplementary setpoint is applicable for the total current
of the three current controllers.

### p31694 DCDCCONV control current upper setpoint limit fixed value

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7463, 7466 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 [A] | 340.28235E36 [A] | [ 0 ] 50.00 [A] |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the fixed upper limit of the control current.

**Dependency:**
  
  
Refer to:
p31695, r31696, p31697, p31698, r31699

### p31695 CI: DCDCCONV control current upper setpoint limit signal source

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7463, 7466 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**p2002 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the signal source for the upper control current limit.  
Only positive values are accepted.

**Dependency:**
  
  
Refer to:
p31694, r31696, p31697, p31698, r31699

**Note:**
  
When connector input p31695 is not interconnected, the following applies:  
- This connector input has no effect.  
- The permanently set setpoint limit in p31694 is active.

### r31696 CO: DCDCCONV control current upper setpoint limit active

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7463 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**p2002 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [A] | - [A] | [ ] - [A] |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Display and connector output for the active upper limit of the control current.

**Dependency:**
  
  
Refer to:
r31679, p31694, p31695, p31730, p31731, p31733, p31734

**Note:**
  
The active upper control current limit is formed from the minimum of the following
values:  
- Upper fixed value (p31694).  
- Upper control current limit signal source (p31695).  
- Positive current limit charge power.

### p31697 DCDCCONV control current lower setpoint limit fixed value

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7463, 7466 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| -340.28235E36 [A] | 0.00 [A] | [ 0 ] -50.00 [A] |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the fixed lower limit of the control current.

**Dependency:**
  
  
Refer to:
p31694, p31695, r31696, p31698, r31699

### p31698 CI: DCDCCONV control current lower setpoint limit signal source

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7463, 7466 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**p2002 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the signal source for the lower control current limit.  
Only negative values are accepted.

**Dependency:**
  
  
Refer to:
p31694, p31695, r31696, p31697, r31699

**Note:**
  
When connector input p31698 is not interconnected, the following applies:  
- This connector input has no effect.  
- The permanently set setpoint limit in p31697 is active.

### r31699 CO: DCDCCONV control current lower setpoint limit active

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7463 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**p2002 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [A] | - [A] | [ ] - [A] |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Display and connector output for the active lower limit of the control current.

**Dependency:**
  
  
Refer to:
r31679, p31697, p31698, p31737, p31738

**Note:**
  
The active lower control current limit is formed from the maximum of the following
values:  
- Lower fixed value limit (p31697).  
- Lower control current limit signal source (p31698).  
- Negative current limit discharge power.

### r31700[0...6] CO: DCDCCONV control current setpoint display

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7461, 7463, 7464, 7473, 7474 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**p2002 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [A] | - [A] | [ ] - [A] |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Display and connector output for setpoints of the control current.

**Index:**
  
[
0]:
Setpoint active  
[
1]:
Supplementary setpoint  
[
2]:
Voltage controller output  
[
3]:
Voltage controller output P component  
[
4]:
Voltage controller output I component  
[
5]:
Active setpoint per phase  
[
6]:
Setpoint correction per phase

**Dependency:**
  
  
Refer to:
r31669, p31693, p32913

**Note:**
  
For index [0]:  
Displays the effective setpoint. This value is the setpoint for the current controller.  
For index [1]:  
Displays the supplementary setpoint interconnected via connector input p31693.  
For index [2]:  
Displays the output value of the voltage controller.  
For index [3]:  
Displays the P component of the voltage controller.  
For index [4]:  
Displays the I component of the voltage controller.  
For index [5]:  
Displays the active setpoint per current controller in 3-phase operation. In 2-phase
operation, a value of 0.0 is indicated.  
The value is calculated as follows:  
p31700[5] = 31700[0] / 3 - 31700[6]  
For index [6]:  
Displays the current setpoint correction per phase in 3-phase operation. In 2-phase
operation, a value of 0.0 is indicated.  
The current setpoint correction only intervenes when the control voltage limiting
(r31669.7 or r31669.8) is active in order to avoid asymmetry of the three phase currents.
An I controller whose integral time is set using p32913 is used to achieve this.

### r31701[0...3] CO: DCDCCONV control current actual value display

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7460, 7464, 7467, 7472, 7474, 7477 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**p2002 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [A] | - [A] | [ ] - [A] |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Display and connector output for the actual value of the control current.

**Index:**
  
[
0]:
Control current actual value total  
[
1]:
Control current actual value phase U  
[
2]:
Control current actual value phase V  
[
3]:
Control current actual value phase W

**Note:**
  
For index [0]:  
Displays the total current of the three phases.  
In 2-phase operation, this value corresponds to the output current, and is the actual
value for the current controller.  
In 3-phase operation, only the actual value is displayed.  
For index [1..3]:  
Displays the currents in the individual phases. These values are the actual values
for the current controller in 3-phase operation.

### p31702 DCDCCONV current controller Kp

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7464, 7474 |
| **Object:**SERVO | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 [V/A] | 340.28235E36 [V/A] | [ 0 ] 1.00 [V/A] |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the proportional gain (Kp) of the current controller.  
When adaptation is deactivated, the following applies:  
- This proportional gain is effective over the complete current range.  
When adaptation is activated, the following applies:  
- This proportional gain is active over the current range 0 ... p31706.

**Dependency:**
  
  
Refer to:
p31703, p31706, p31707

**Note:**
  
Adaptation is deactivated in the following cases:  
- p31703 = 100%  
- p31706 = p31707  
Adaptation is activated if the two following conditions are satisfied:  
1. p31703 not equal to 100 %  
2. p31706 < p31707  
In 3-phase operation, this value is applicable for the three current controllers.

### p31702 DCDCCONV current controller Kp

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7464, 7474 |
| **Object:**VECTOR | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 | 340.28235E36 | [ 0 ] 1.00 |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the proportional gain (Kp) of the current controller.  
When adaptation is deactivated, the following applies:  
- This proportional gain is effective over the complete current range.  
When adaptation is activated, the following applies:  
- This proportional gain is active over the current range 0 ... p31706.

**Dependency:**
  
  
Refer to:
p31703, p31706, p31707

**Note:**
  
Adaptation is deactivated in the following cases:  
- p31703 = 100%  
- p31706 = p31707  
Adaptation is activated if the two following conditions are satisfied:  
1. p31703 not equal to 100 %  
2. p31706 < p31707  
In 3-phase operation, this value is applicable for the three current controllers.

### p31703 DCDCCONV current controller upper Kp adaptation factor

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7464, 7474 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 [%] | 10000.00 [%] | [ 0 ] 100.00 [%] |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the adaptation factor for the proportional gain (Kp) in the upper adaptation
range (> p31707).  
The value is referred to p31702.

**Dependency:**
  
  
Refer to:
p31702, p31706, p31707

**Note:**
  
For the factory setting (p31703 = 100 %), adaptation is deactivated.  
In 3-phase operation, this value is applicable for the three current controllers.

### p31704 DCDCCONV current controller Tn

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7464, 7474 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.000000 [ms] | 340.28235E36 [ms] | [ 0 ] 8.000000 [ms] |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the integral time (Tn) of the current controller.  
When adaptation is deactivated, the following applies:  
- This integral time is effective over the complete current range.  
When adaptation is activated, the following applies:  
- This integral time is active over the current range 0 ... p31706.

**Dependency:**
  
  
Refer to:
p31705, p31706, p31707

**Note:**
  
Adaptation is deactivated in the following cases:  
- p31705 = 100%  
- p31706 = p31707  
Adaptation is activated if the two following conditions are satisfied:  
1. p31705 not equal to 100 %  
2. p31706 < p31707  
The integral component is held if the sum of the current controller output and supplementary
setpoints exceeds the upper or lower voltage limit.  
In 3-phase operation, this value is applicable for the three current controllers.

### p31705 DCDCCONV current controller upper Tn adaptation factor

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7464, 7474 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 1.00 [%] | 10000.00 [%] | [ 0 ] 100.00 [%] |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the adaptation factor for the integral time (Tn) in the upper adaptation range
(> p31707).  
The value is referred to p31704.

**Dependency:**
  
  
Refer to:
p31704, p31706

**Note:**
  
For the factory setting (p31705 = 100 %), adaptation is deactivated.  
In 3-phase operation, this value is applicable for the three current controllers.

### p31706 DCDCCONV current controller adaptation lower current limit

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7464, 7474 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 [A] | 340.28235E36 [A] | [ 0 ] 0.00 [A] |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the lower current limit for the adaptation of the proportional gain (Kp) and
the integral time (Tn).  
Below this limit, the current controller operates with the following parameters:  
- Proportional gain (Kp): p31702  
- Integral time (Tn): p31704  
The controller parameters (Kp, Tn) are linearly interpolated between the lower current
limit (p31706) and the upper current limit (p31707).

**Dependency:**
  
  
Refer to:
p31702, p31703, p31704, p31705, p31707

**Note:**
  
The following must be observed:  
p31706 < p31707  
In 3-phase operation, this value is applicable for the three current controllers.

### p31707 DCDCCONV current controller adaptation upper current limit

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7464, 7474 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 [A] | 340.28235E36 [A] | [ 0 ] 0.00 [A] |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the upper current limit for the adaptation of the proportional gain (Kp) and
the integral time (Tn).  
Above this limit, the current controller operates with the following parameters:  
- Proportional gain (Kp): p31702 x p31703  
- Integral time (Tn): p31704 x p31705  
The controller parameters (Kp, Tn) are linearly interpolated between the lower current
limit (p31706) and the upper current limit (p31707).

**Dependency:**
  
  
Refer to:
p31702, p31703, p31704, p31705, p31706

**Note:**
  
The following must be observed:  
p31706 < p31707  
In 3-phase operation, this value is applicable for the three current controllers.

### p31709 BI: DCDCCONV current controller integrator setting value

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 7464, 7474 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the signal source to hold the integrator for the current controller.

**Note:**
  
In 3-phase operation, this value is applicable for the three current controllers.

### p31710 CI: DCDCCONV current controller integrator setting val signal source

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7464, 7474 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**p2001 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the signal source for the integrator setting value for the current controller.  
For binector input p31711 = 0/1 signal, the setting value is accepted.

**Dependency:**
  
  
Refer to:
p31711

**Note:**
  
In 3-phase operation, this value is applicable for the three current controllers.

### p31711 BI: DCDCCONV current controller integrator accept setting value

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 7464, 7474 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the signal source to accept the setting value for the integrator (p31710).  
BI: p31711 = 0/1 signal:  
The setting value available via connector input p31710 is accepted.

**Dependency:**
  
  
Refer to:
p31710

**Note:**
  
In 3-phase operation, this value is applicable for the three current controllers.

### p31712 DCDCCONV current controller disturbance input factor

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**4 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7464, 7474 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 | 1.00 | [ 0 ] 1.00 |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the factor for the disturbance input of the current controller.  
Signal value from p31680 x p31712 is added to the current controller output.

**Note:**
  
In 3-phase operation, this value is applicable for the three current controllers.

### p31713 CI: DCDCCONV control voltage upper setpoint limit signal source

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7464, 7474 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**p2001 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the signal source for the upper control voltage limit of the current controller
output.

**Dependency:**
  
  
Refer to:
p31714, r31728

**Note:**
  
The active upper control value limit is formed from the minimum of p31713, p31714
and r0070.  
Exception:  
This value is not taken into consideration for the minimum evaluation as soon as one
of the two values in p31713 or p31714 is equal to 0 V (or less than 0 V).  
For p31713 = 0 V and p31714 = 0 V, the value in r0070 acts as upper setpoint limit.  
The following applies for a VECTOR drive object in 2-phase operation:  
For the control voltage, the complete range is not available as default. To be able
to use the complete voltage range, the maximum modulation depth must be increased
to over 100%.  
The following settings are required:  
- set p1810.15 = 1  
- set p1803 > 115%

### p31714 DCDCCONV control voltage upper limit

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7464, 7474 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.0 [V] | 340.28235E36 [V] | [ 0 ] 0.0 [V] |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the upper control voltage limit of the current controller output.

**Recommend.:**
  
A value less than the maximum output voltage (p32902[1]) should be set for the upper
limit.  
This prevents the connected load from being overcharged or the DC contactor from being
opened.

**Dependency:**
  
  
Refer to:
p31713  
Refer to:
A53466

**Note:**
  
The active upper control value limit at the current controller output is formed from
the minimum of r0070, p31713 and p31714.  
Exception:  
This value is not taken into consideration for the minimum evaluation as soon as one
of the two values in p31713 or p31714 is equal to 0 V (or less than 0 V).  
For p31713 = 0 V and p31714 = 0 V, the value in r0070 acts as upper setpoint limit.  
The following applies for a VECTOR drive object in 2-phase operation:  
For the control voltage, the complete range is not available as default. To be able
to use the complete voltage range, the maximum modulation depth must be increased
to over 100%.  
The following settings are required:  
- set p1810.15 = 1  
- set p1803 > 115%

### p31715 DCDCCONV control voltage lower limit

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7464, 7474 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.0 [V] | 340.28235E36 [V] | [ 0 ] 0.0 [V] |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the lower control voltage limit of the current controller output.  
This parameter can be used as measure to prevent an undesirable total discharge of
the energy storage device.

**Dependency:**
  
  
Refer to:
p31713, p31714, p31723  
Refer to:
A53466

**Caution:**
  
The lower control voltage limit p31715 should be selected less than the upper control
voltage limit p31714 (A53466).

**Notice:**
  
The lower control voltage limit should only be set once output voltage p31680 has
exceeded the lower control voltage limit. Entering a lower control voltage limit greater
than the voltage actual value p31680 results in an immediate voltage step (voltage
jump) at the output.

**Note:**
  
The active lower control value limit at the current controller output is formed from
the maximum of p31715 and p31723. If this lower limit is greater than the upper active
control value limit, then instead, the minimum from r0070, p31713 and p31714 also
acts as lower active control value limit. In this case, the upper control value limit
therefore also acts as lower control value limit (F53466).  
The following applies for a VECTOR drive object in 2-phase operation:  
For the control voltage, the complete range is not available as default. To be able
to use the complete voltage range, the maximum modulation depth must be increased
to over 100%.  
The following settings are required:  
- set p1810.15 = 1  
- set p1803 > 115%

### r31716[0...3] CO: DCDCCONV control voltage

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7461, 7464, 7468, 7473, 7474, 7478 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**p2001 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [V] | - [V] | [ ] - [V] |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Display and connector output for the control voltage of the power unit.

**Index:**
  
[
0]:
Control voltage  
[
1]:
Control voltage U  
[
2]:
Control voltage V  
[
3]:
Control voltage W

**Dependency:**
  
  
Refer to:
p31665, p31714, p31715

**Note:**
  
In 2-phase operation:  
For index [0]: Control voltage of the two selected terminals.  
For index [1 .. 3]: No significance  
In 3-phase operation:  
For index [0]: No significance  
For index [1]: Control voltage at terminal U  
For index [2]: Control voltage at terminal V  
For index [3]: Control voltage at terminal W  
Control voltage:  
Average voltage of the selected terminals at the Motor Module referred to terminal
DCN.

### r31717 CO: DCDCCONV space vector absolute value 2-phase

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7460, 7468 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**p2001 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [Vrms] | - [Vrms] | [ ] - [Vrms] |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Display and connector output for the absolute value of the voltage space vector in
2-phase operation.

**Dependency:**
  
  
Refer to:
r31718

**Note:**
  
VECTOR:  
The following settings must be made in the basic system for the VECTOR drive object:  
- Set the "U/f control with independent voltage setpoint" operating mode (p1300 =
19).  
- Select "Output voltage angle setpoint input" (p1302.2 = 1).  
- Select "Immediate setpoint transfer for pulse enable" (p1302.6 = 1).  
- Interconnect the space vector absolute value as setpoint (CI: p1330 = r31717).  
- Interconnect the space vector angle as angle setpoint (CI: p1356 = r31718).  
SERVO:  
Additional settings and interconnections are not required for the SERVO drive object.

### r31718 CO: DCDCCONV space vector angle 2-phase

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7460, 7468 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**p2005 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [°] | - [°] | [ ] - [°] |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Display and connector output for the angle of the voltage space vector in 2-phase
operation.

**Dependency:**
  
  
Refer to:
r31717

**Note:**
  
VECTOR:  
The following settings must be made in the basic system for the VECTOR drive object:  
- Set the "U/f control with independent voltage setpoint" operating mode (p1300 =
19).  
- Select "Output voltage angle setpoint input" (p1302.2 = 1).  
- Select "Immediate setpoint transfer for pulse enable" (p1302.6 = 1).  
- Interconnect the space vector absolute value as setpoint (CI: p1330 = r31717).  
- Interconnect the space vector angle as angle setpoint (CI: p1356 = r31718).  
SERVO:  
Additional settings and interconnections are not required for the SERVO drive object.

### r31719[0...2] DCDCCONV modulation depth 3-phase display

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**4 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**PERCENT | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [%] | - [%] | [ ] - [%] |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Display and connector output for the active modulation depth of the power unit.

**Index:**
  
[
0]:
Phase U  
[
1]:
Phase V  
[
2]:
Phase W

**Dependency:**
  
  
Refer to:
p31665

**Note:**
  
This parameter is only active in 3-phase operation.

### p31720 DCDCCONV voltage sensing change max.

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**4 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7467, 7477 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 [V] | 1000000000.00 [V] | [ 0 ] 50.00 [V] |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Setting of the max. permissible change of the measured voltage per current controller
sampling time.  
If the set value is exceeded it is assumed that the voltage sensing has failed.

**Dependency:**
  
  
Refer to:
F53462

**Note:**
  
An appropriate fault is output when exceeded.

### p31721 DCDCCONV controller at its limits maximum duration

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**4 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7467, 7477 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.000 [ms] | 1000000000.000 [ms] | [ 0 ] 10.000 [ms] |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the maximum duration during which the following controllers may operate at their
limit.  
- Current controller and simultaneously voltage controller  
or  
- Current controller and simultaneously DC link voltage controller (Vdc controller)

**Dependency:**
  
  
Refer to:
p31660  
Refer to:
F53462

**Note:**
  
An appropriate fault is output when exceeded.  
In 3-phase operation, this value is applicable for the three current controllers.

### p31722[0...3] DCDCCONV Vdc controller threshold voltage

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7466 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 [V] | 2000.00 [V] | [ 0 ] 750.00 [V]  [ 1 ] 500.00 [V]  [ 2 ] 20.00 [V]  [ 3 ] 20.00 [V] |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the lower and upper threshold voltage as well as the associated hysteresis values
for the DC link voltage controller (Vdc controller).  
When the upper threshold voltage p31722[0] is reached, status bit "Upper DC link voltage
limit" (r31669.11) is set until the DC link voltage has been reduced by the upper
hysteresis voltage p31722[2].  
When the lower threshold voltage p31722[1] is reached, status bit "Lower DC link voltage
limit" (r31669.10) is set until the DC link voltage has been increased by the lower
hysteresis voltage p31722[3].

**Index:**
  
[
0]:
Vdc upper threshold voltage  
[
1]:
Vdc lower threshold voltage  
[
2]:
Vdc threshold voltage upper hysteresis  
[
3]:
Vdc threshold voltage lower hysteresis

**Dependency:**
  
  
Refer to:
r31669, p31724

### p31723 CI: DCDCCONV control voltage lower setpoint limit signal source

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7464, 7474 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**p2001 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the signal source for the lower control voltage limit.

**Dependency:**
  
  
Refer to:
p31713, p31714, p31715, r31716, r31729

**Note:**
  
The active lower setpoint limit is formed from the maximum of p31715 and p31723.  
The following applies for a VECTOR drive object in 2-phase operation:  
For the control voltage, the complete range is not available as default. To be able
to use the complete voltage range, the maximum modulation depth must be increased
to over 100%.  
The following settings are required:  
- set p1810.15 = 1  
- set p1803 > 115%

### p31724 BI: DCDCCONV Vdc controller enable signal source

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 7466 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the signal source to enable the DC link voltage controller (Vdc controller).  
For p31724 = 1 signal, the following applies:  
- The Vdc controller is enabled.  
For p31724 = 0 signal, the following applies:  
- The Vdc controller is not enabled.

### p31725 DCDCCONV Vdc controller actual value smoothing time constant

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7466 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 [ms] | 10000.00 [ms] | [ 0 ] 0.00 [ms] |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the smoothing time constant for the PT1 filter of the DC link voltage actual
value (r0070).

### p31727 DCDCCONV Vdc controller proportional gain

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7466 |
| **Object:**SERVO | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 [A/V] | 340.28235E36 [A/V] | [ 0 ] 3.00 [A/V] |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the proportional gain (Kp) of the DC link voltage controller (Vdc controller).  
The gain factor is proportional to the total capacitance of the DC link.

**Recommend.:**
  
A starting value for the proportional gain of the Vdc controller is half of the DC
link capacitance [mF].  
Kp [A/V] = 0.5 x C [mF]  
Example:  
p31727 = 3 [A/V] for p3422 = 6 [mF]

### p31727 DCDCCONV Vdc controller proportional gain

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7466 |
| **Object:**VECTOR | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 | 340.28235E36 | [ 0 ] 3.00 |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the proportional gain (Kp) of the DC link voltage controller (Vdc controller).  
The gain factor is proportional to the total capacitance of the DC link.

**Recommend.:**
  
A starting value for the proportional gain of the Vdc controller is half of the DC
link capacitance [mF].  
Kp [A/V] = 0.5 x C [mF]  
Example:  
p31727 = 3 [A/V] for p3422 = 6 [mF]

### r31728 CO: DCDCCONV control voltage upper setpoint limit active

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7464, 7474 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**p2001 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [V] | - [V] | [ ] - [V] |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Display and connector output for the active upper limit of the control voltage.

**Dependency:**
  
  
Refer to:
p31713, p31714

**Note:**
  
The active upper control voltage limit is formed from the minimum of the following
values:  
- Maximum control voltage of the power unit being used (this depends on the actual
DC link voltage and the pulse frequency)  
- Control voltage upper setpoint limit signal source (p31713)  
- Control voltage upper limit (p31714)  
In 3-phase operation, this value is applicable for the three current controllers.

### r31729 CO: DCDCCONV control voltage lower setpoint limit active

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7464, 7474 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**p2001 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [V] | - [V] | [ ] - [V] |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Display and connector output for the active lower limit of the control voltage.

**Dependency:**
  
  
Refer to:
p31715, p31723

**Note:**
  
The active lower control voltage limit is formed from the maximum of the following
values:  
- Control voltage lower limit (p31715)  
- Control voltage lower setpoint limit signal source (p31723)  
In 3-phase operation, this value is applicable for the three current controllers.

### p31730 CI: DCDCCONV charge energy storage device power limit signal source

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7470 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**r2004 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the signal source for the power limiting when charging the energy storage device.  
With the power limiting, the power when charging the energy storage device can be
limited to protect the infeed against overload.  
The power limit is formed from fixed value p31731 and the signal source of binector
input p31730.

**Dependency:**
  
  
Refer to:
p31731, r31732, p31733

### p31731 DCDCCONV charge energy storage device power limiting fixed value

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7470 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 [kW] | 340.28235E36 [kW] | [ 0 ] 10000 [kW] |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the fixed value for the power limiting when charging the energy storage device.  
With the power limiting, the power when charging the energy storage device can be
limited to protect the infeed against overload.  
The power limit is formed from fixed value p31731 and the signal source of binector
input p31730.

**Dependency:**
  
  
Refer to:
p31730, r31732, p31733

**Note:**
  
Power limiting is not active in the factory setting (p31731 = 10000).

### r31732 CO: DCDCCONV charge energy storage device power limiting active

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7470 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**r2004 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [kW] | - [kW] | [ ] - [kW] |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Display and connector output for active power limiting when charging the energy storage
device.

**Dependency:**
  
  
Refer to:
p31730, p31731, p31733, p31734

### p31733[0...4] CI: DCDCCONV active power actual value signal source

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7470 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**r2004 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the signal source for the actual power of loads 1 to 5.  
The active power limiting p31732 is reduced by the values of the individual loads.

**Recommend.:**
  
Recommended BICO interconnection:  
p31733[0...4] = r0082 (drive object)

**Index:**
  
[
0]:
Load 1  
[
1]:
Load 2  
[
2]:
Load 3  
[
3]:
Load 4  
[
4]:
Load 5

**Dependency:**
  
  
Refer to:
p31730, p31731, r31732, p31734

### p31734 DCDCCONV charge energy storage device minimum power limiting

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7470 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 [kW] | 340.28235E36 [kW] | [ 0 ] 0 [kW] |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the minimum power limiting when charging the energy storage device.

**Dependency:**
  
  
Refer to:
p31730, p31731, r31732, p31733

### p31737 CI: DCDCCONV dischrg energy storage device power limit signal source

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7470 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**r2004 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the signal source for the power limiting when discharging the energy storage
device.  
With the power limiting, the power when discharging the energy storage device can
be limited to protect the infeed against overload.  
The power limit is formed from fixed value p31738 and the signal source of binector
input p31737.

**Dependency:**
  
  
Refer to:
p31738

### p31738 DCDCCONV discharge energy storage device power limit fixed value

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7470 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| -340.28235E36 [kW] | 0 [kW] | [ 0 ] -10000 [kW] |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the fixed value for the power limiting when discharging the energy storage device.  
With the power limiting, the power when discharging the energy storage device can
be limited to protect the infeed against overload.  
The power limit is formed from fixed value p31738 and the signal source of binector
input p31737.

**Dependency:**
  
  
Refer to:
p31737

**Note:**
  
Power limiting is not active in the factory setting (p31738 = -10000).

### r31739 CO: DCDCCONV discharge energy storage device power limiting active

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7470 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**r2004 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [kW] | - [kW] | [ ] - [kW] |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Display and connector output for active power limiting when discharging the energy
storage device.

**Dependency:**
  
  
Refer to:
p31733, p31737, p31738

### p32900[0...1] BI: DCDCCONV DC contactor signal source

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 7460, 7462, 7469, 7472 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 1   [ 1 ] 1 |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the signal source for the DC contactor.  
For index [0]:  
Sets the signal source for the feedback signal from the DC contactor.  
For the factory setting p32900[0] = 1, the DC contactor is considered as being closed.  
Depending on the energy storage, the following setting must be used:  
- Batteries: p32900[0] = 1  
- Ultracapacitor Modules: p32900[0] = DC contactor feedback signal (if available)  
For index [1]:  
Sets the signal source to close the DC contactor.  
For the factory setting p32900[1] = 1, the command to close the DC contactor is active.  
Additional conditions are required to close the contactor (see status bit r31669.12).

**Recommend.:**
  
For index [0]:  
We recommend that a DC contactor with feedback signal contact is used.

**Index:**
  
[
0]:
Feedback signal  
[
1]:
Close command

**Dependency:**
  
  
Refer to:
F53465

**Caution:**
  
For index [0]:  
Fault F53465 is output when the DC contactor opens (signal changes from 1 to 0).  
Prerequisites:  
- The signal source is enabled (p31668 = 1 signal).  
- The pulses are enabled (r1838.2 = 1).

### p32901 DCDCCONV voltage controller ramp-up time/ramp-down time

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7463 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.0 [ms] | 340.28235E36 [ms] | [ 0 ] 0.0 [ms] |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the ramp-up time/ramp-down time for the active voltage setpoint (r31679[0]).  
The ramp-function generator is deactivated for value of = 0.0 ms.

**Dependency:**
  
For r31669.13 = 0, the ramp-function generator output is set to the voltage actual
value.  
  
Refer to:
r31669, p31670, p31671, r31679

**Note:**
  
The time is referred to a change of 1000 V.  
Example:  
Change by 500 V in 2 s required.  
Value to be set: 4000 ms  
(1000 V / 500 V) * 2000 ms = 4000 ms

### p32902[0...1] DCDCCONV output voltage minimum/maximum value

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7469 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 [V] | 340.28235E36 [V] | [ 0 ] 0 [V]  [ 1 ] 2000 [V] |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the minimum/maximum values for the output voltage.  
For index [0]:  
Sets the minimum value for the output voltage.  
This value is only used to calculate the available energy of capacitive energy storage
devices.  
On the other hand, p31715 should be used to provide protection against total discharge.  
For index [1]:  
Sets the maximum value for the output voltage.  
Fault F53467 is output if the maximum output voltage p32902[1] is exceeded.  
In addition, status bit r31699.12 = 0 is set, and a command is issued to open the
DC contactor. Fault F53465 is output if this is followed by feedback signal "DC contactor
open" (p32900[0] = 1/0 signal).

**Index:**
  
[
0]:
Minimum  
[
1]:
Maximum

**Dependency:**
  
  
Refer to:
r31669  
Refer to:
F53465, F53467

**Caution:**
  
For index [1]:  
If the maximum output voltage value is set too high, then the maximum permissible
voltage at the connected load can be exceeded.

### p32903 DCDCCONV total energy storage device capacitance

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 [mF] | 340.28235E36 [mF] | [ 0 ] 0 [mF] |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the total capacitance of the energy storage device (e.g. Ultracapacitor, battery).  
This value is used to calculate the available capacitive energy (r32904).

**Dependency:**
  
  
Refer to:
r32904

### r32904 CO: DCDCCONV energy storage device, energy available

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [kWh] | - [kWh] | [ ] - [kWh] |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Display and connector output for the available energy of the energy storage device.  
The available energy of the capacitors is calculated from their voltage and capacitance.

**Dependency:**
  
  
Refer to:
r31679, p32902, p32903

### r32905 CO: DCDCCONV energy storage device, output power

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**r2004 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [kW] | - [kW] | [ ] - [kW] |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Display and connector output for the actual power at the output (including smoothing
capacitance).  
The output power is calculated from the actual values for voltage (r31679[1]) and
control current (r31701).

**Dependency:**
  
  
Refer to:
r31679, r31701

### p32906 BI: DCDCCONV switch on signal source

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 7462 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the signal source to switch on DCDCCONV.  
The command to switch on/switch off the DCDCCONV is issued via an RS flip-flop. The
result of the flip-flop is indicated at binector output r31669.16. This signal can
be used for the ON/OFF command.  
BI: p32906 = 1 signal:  
- the switch-on command is active.  
BI: p32906 = 0 signal:  
- the switch-on command is not active.

**Recommend.:**
  
Recommended BICO interconnection for binector output r31669.16:  
BI: p0840[0...n] = r31669.16

**Dependency:**
  
  
Refer to:
r31669, p32907

### p32907 BI: DCDCCONV switch off signal source

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 7462 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the signal source to switch off DCDCCONV.  
The command to switch on/switch off the DCDCCONV is set via an RS flip-flop. The result
of the flip-flop is indicated at binector output r31669.16. This signal can be used
for the ON/OFF command.  
BI: p32907 = 1 signal:  
- the switch-off command is active.  
BI: p32907 = 0 signal:  
- the switch-off command is not active.

**Recommend.:**
  
Recommended BICO interconnection for binector output r31669.16:  
BI: p0840[0...n] = r31669.16

**Dependency:**
  
  
Refer to:
r31669, p32906

### p32908 DCDCCONV phase equalization controller Kp 2-phase

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7465 |
| **Object:**SERVO | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00000 [V/A] | 0.00150 [V/A] | [ 0 ] 0.00000 [V/A] |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the proportional gain (Kp) of the phase equalization controller in 2-phase operation.

**Recommend.:**
  
The following settings are recommended for Motor Modules in the chassis format:  
p32908 = 0.1 * L_p2  
L_p2 is the total inductance between the two phases being used  
Example:  
The following setting is recommended for a total phase-phase inductance of L_p2 =
1.5 mH:  
p32908 = 0.00015 V/A

**Dependency:**
  
  
Refer to:
p32909

**Notice:**
  
It is not permissible that the phase equalization controller is deactivated during
operation (p32908 = 0).

**Note:**
  
The phase equalization controller is specifically recommended for chassis format Motor
Modules.

### p32908 DCDCCONV phase equalization controller Kp 2-phase

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7465 |
| **Object:**VECTOR | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00000 | 0.00150 | [ 0 ] 0.00000 |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the proportional gain (Kp) of the phase equalization controller in 2-phase operation.

**Recommend.:**
  
The following settings are recommended for Motor Modules in the chassis format:  
p32908 = 0.1 * L_p2  
L_p2 is the total inductance between the two phases being used  
Example:  
The following setting is recommended for a total phase-phase inductance of L_p2 =
1.5 mH:  
p32908 = 0.00015 V/A

**Dependency:**
  
  
Refer to:
p32909

**Notice:**
  
It is not permissible that the phase equalization controller is deactivated during
operation (p32908 = 0).

**Note:**
  
The phase equalization controller is specifically recommended for chassis format Motor
Modules.

### p32909 DCDCCONV phase equalization controller Tn 2-phase

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7465 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.000000 [ms] | 340.28235E36 [ms] | [ 0 ] 0.000000 [ms] |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the integral time (Tn) of the phase equalization controller in 2-phase operation.

**Recommend.:**
  
The following settings are recommended for Motor Modules in the chassis format:  
p32909 = 20 ms

**Dependency:**
  
  
Refer to:
p32908

**Note:**
  
The phase equalization controller is specifically recommended for chassis format Motor
Modules.

### p32910 DCDCCONV VSM values monitoring time

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7467, 7477 |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 1.00 [ms] | 1000.00 [ms] | [ 0 ] 5.00 [ms] |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the monitoring time for the actual VSM voltage.  
If the VSM supplies a constant value for longer than the monitoring time, then the
corresponding alarm is output, and status bit 31669.9 = 1 is set.

**Dependency:**
  
  
Refer to:
r31669  
Refer to:
A53464

**Notice:**
  
If the VSM voltage sensing is faulted within the monitoring time, then under certain
circumstances, the current control operates with an incorrect voltage measured value.
For example, this can mean that voltage limits are exceeded unnoticed, and it is not
detected that the DC contactor opened due to an overvoltage condition.

**Note:**
  
VSM: Voltage Sensing Module

### r32911[0...15] CO: DCDCCONV status diagnostics switching times 3-phase

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**4 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [µs] | - [µs] | [ ] - [µs] |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Display and BICO output for the diagnostics of the switching times in 3-phase operation.
There are 16 states. There is one switching time for each state.

**Dependency:**
  
  
Refer to:
p31665, r32912

**Note:**
  
This parameter is only active in 3-phase operation.

### r32912[0...16] CO: DCDCCONV status diagnostics switching states 3-phase

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**4 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Display and BICO output for the diagnostics of the switching states in 3-phase operation.  
Index[0...15]:  
16 states. For each state, there is 1 bit per phase:  
Bit0=u, bit1=v, bit2=w  
  
Index [16]:  
Actual mode of 3-phase operation:  
1: direct mode (only upper IGBTS)  
0: phase mode  
-1: direct mode (only lower IGBTS)

**Dependency:**
  
  
Refer to:
p31665, r32911

**Note:**
  
This parameter is only active in 3-phase operation.

### p32913[0...1] DCDCCONV current setpoint correction Tn 3-phase

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**4 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.000000 [ms] | 340.28235E36 [ms] | [ 0 ] 10.000000 [ms]  [ 1 ] 100.000000 [ms] |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Sets the integral time (Tn) of the current setpoint correction in three-phase operation.
The current setpoint correction only intervenes when the control voltage limiting
(r31669.7 or r31669.8) is active in order to avoid asymmetry of the three phase currents.

**Recommend.:**
  
The factory settings only have to be changed in exceptional cases.

**Index:**
  
[
0]:
Integral time for a positive system deviation  
[
1]:
Integral time for a negative system deviation

**Note:**
  
The system deviation corresponds to the difference between the currently active setpoint
per phase and the average value of the three phase current actual values.  
If an index is set to a value of 0.0, then the complete current setpoint correction
is deactivated.  
The lowest valid value is 1.0. Values between 0.0 and 1.0 are internally set to 1.0
automatically.

### r32914 CO: DCDCCONV power unit overload I2t

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**All objects | **P-Group:**- | **Version:**2100900 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**PERCENT | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [%] | - [%] | [ ] - [%] |
| [Alarms](Technology%20Extension%20DCDCCONV%20V2.10.13.md#technology-extension-dcdcconv-v21013) |  |  |

**Valid as of version:**
  
2.1

**Description:**
  
Displays the power unit overload determined using the I2t calculation when operating
with the TEC DCDCCONV.  
A current reference value is defined for the I2t monitoring of the power unit. It
represents the current that can be conducted by the power unit without any influence
of the switching losses (e.g. the continuously permissible current of the capacitors,
inductances, busbars, etc.).  
If the I2t reference current of the power unit is not exceeded, then an overload (0
%) is not displayed. In the other case, the degree of thermal overload is calculated,
where 100% results in a trip.

**Dependency:**
  
  
Refer to:
F53755

**Note:**
  
The I2t monitoring of the TEC DCDCCONV uses parameters other than the I2t monitoring
of the power unit in the basis system.  
The I2t monitoring of the power unit in the basis system (r0036, F30005) does not
function in operation as DCDC converter.

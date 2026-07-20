---
title: "SINAMICS Parameter S200 Basic PN"
package: sdrpa423enUS
topics: 509
source: Siemens TIA Portal Information System (offline help, en-US)
---


# SINAMICS Parameter S200 Basic PN

This section contains the parameter descriptions for the devices listed below. The parameter descriptions for the various devices can differ. In the table of contents, you will then see a separate entry for each parameter number. The following device variants are taken into account in the online help:

- SINAMICS S200

## SINAMICS Parameter S200 Basic PN 00002 - 01131

SINAMICS Parameter S200 Basic PN 00002 - 01131

### r0002 Drive operating display

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Parameter group:** Status parameters, Diagnostics general, Drive enable signals |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Operating display for the drive.

**Value:** 
  
0:
Operation - Everything enabled  
10:
Operation - Set "Enable setpoint" = "1"  
11:
Operation - Set "Enable speed controller" = "1"  
12:
Operation - RFG frozen, set "RFG start" = "1"  
13:
Operation - Set "Enable ramp-function generator" = "1"  
14:
Operation - MotID, excitation running or brake opens, SS2  
15:
Operation - Open brake (p1215)  
16:
Operation - Withdraw braking with OFF1 using "ON/OFF1" = "1"  
17:
Operation - Braking with OFF3 can only be interrupted with OFF2  
18:
Operation - Brake on fault, remove fault, acknowledge  
21:
Ready for operation - Set "Enable operation" = "1"  
22:
Ready for operation - De-magnetizing running  
23:
Ready for operation - Set "Infeed operation" = "1"  
31:
Ready for switching on - Set "ON/OFF1" = "0/1"  
35:
Switching on inhibited - Carry out first commissioning  
41:
Switching on inhibited - Set "ON/OFF1" = "0"  
42:
Switching on inhibited - Set "Operating condition/OFF2" = "1"  
43:
Switching on inhibited - Set "Operating condition/OFF3" = "1"  
44:
Switching on inhibited - Supply STO terminal w/ 24 V (hardware)  
45:
Switching on inhibited - Rectify fault, acknowledge fault, STO  
46:
Switching on inhibited - Exit commissioning mode  
60:
Drive deactivated/not operational  
70:
Initialization  
200:
Wait for run-up/partial run-up  
250:
Device signals a topology error

**Dependency:** 
  
See also:
r0046

**Notice:** 
  
For several missing enable signals, the corresponding value with the highest number
is displayed.

**Note:** 
  
OC: Operating condition  
EP: Enable Pulses (pulse enable)  
RFG: Ramp-function generator  
COM: Commissioning  
MotID: Motor data identification

### r0020 Speed setpoint smoothed

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Parameter group:** Mode signals / displays |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** rpm | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the currently smoothed speed setpoint at the input of the speed controller
or U/f characteristic (after the interpolator).

**Dependency:** 
  
See also:
r1438

**Note:** 
  
Smoothing time constant = 100 ms  
The signal is not suitable as a process quantity and may only be used as a display
quantity.  
The speed setpoint is available smoothed (r0020) and unsmoothed (r1438).

### r0021 Speed actual value smoothed

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Parameter group:** Diagnostics, Mode signals / displays |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** rpm | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2000 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Display for the smoothed actual value of the motor speed.

**Dependency:** 
  
See also:
r0063

**Note:** 
  
Smoothing time constant = 100 ms  
The speed actual value is available smoothed (r0021) and unsmoothed (r0063).

### r0026 DC link voltage smoothed

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Parameter group:** Brake control, Mode signals / displays |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** V | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2001 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the smoothed actual value of the DC link voltage.

**Dependency:** 
  
See also:
r0070

**Notice:** 
  
This smoothed signal is not suitable for diagnostics or evaluation of dynamic operations.
In this case, the unsmoothed value should be used.

**Note:** 
  
Smoothing time constant = 100 ms  
The signal is not suitable as a process quantity and may only be used as a display
quantity.  
The DC link voltage is available smoothed (r0026) and unsmoothed (r0070).

### r0027 Absolute actual current smoothed

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Parameter group:** Mode signals / displays, Power unit |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Arms | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2002 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the smoothed absolute current actual value.

**Dependency:** 
  
See also:
r0068

**Notice:** 
  
This smoothed signal is not suitable for diagnostics or evaluation of dynamic operations.
In this case, the unsmoothed value should be used.

**Note:** 
  
A_INF, S_INF, VECTOR: Smoothing time constant = 300 ms  
SERVO: Smoothing time constant = 100 ms  
The signal is not suitable as a process quantity and may only be used as a display
quantity.  
The absolute current actual value is available smoothed (r0027) and unsmoothed (r0068).

### r0031 Actual torque smoothed

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Parameter group:** Brake control, Mode signals / displays |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Nm | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the smoothed torque actual value.

**Dependency:** 
  
See also:
r0080

**Note:** 
  
Smoothing time constant = 100 ms  
The signal is not suitable as a process quantity and may only be used as a display
quantity.  
The torque actual value is available smoothed (r0031) and unsmoothed (r0080).

### r0032 Active power actual value smoothed

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Parameter group:** Mode signals / displays |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** kW | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** r2004 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Display for the smoothed actual value of the active power.

**Dependency:** 
  
See also:
r0082

**Note:** 
  
The active power is available smoothed (r0032 with 100 ms, r0082[1] with 1 ms) and
unsmoothed (r0082[0]).

### r0034 Motor utilization thermal

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Parameter group:** Motor temperature, Mode signals / displays |  |  |
| **Not relevant for motor type:**Induction motor, Separately excited synchronous motor, Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** % | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** PERCENT |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the thermal motor utilization taking into account the ambient temperature
set in p0613.

**Dependency:** 
  
See also:
p0613  
See also:
F07011, A07012

**Notice:** 
  
After the drive is switched on, the system starts to determine the motor temperature
with an assumed model value. This means that the value for the motor utilization is
only valid after a stabilization time.

### r0036[0...2] Power unit overload

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Parameter group:** Mode signals / displays, Power unit |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** % | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** PERCENT |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Display when the power unit is overloaded.  
A reference value is defined for the monitoring functions.  
An overload (0 %) is not displayed if the reference value is not exceeded.  
The display value increases if the reference value is exceeded.  
An alarm is output if an overload is active over a certain time period; a fault is
output when 100% is reached.

**Index:** 
  
[
0]:
I2t (AC)  
[
1]:
Reserved  
[
2]:
Reserved

**Dependency:** 
  
See also:
p0290  
See also:
F30005, A30256, A30257, F30258, A30267, F30268

**Note:** 
  
For index [0]:  
This index shows the actual state of the I2t monitoring on the AC side.  
The reference value represents the AC current that the power unit can permanently
provide, without the influence of switching losses (e.g. the continuously permissible
current of capacitors, inductances, busbars, etc.).  
  
For index [1]:  
This index shows the actual state of the active power monitoring.  
The reference value represents the active power that the power unit can continuously
provide.  
  
For index [2]:  
This index shows the actual state of the I2t monitoring on the DC side.  
The reference value represents the DC current that can continuously flow in the DC
link.

### r0037[0...10] Power unit temperatures

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Parameter group:** Mode signals / displays, Power unit |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** °C | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2006 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Display for the temperatures in the power unit.

**Index:** 
  
[
0]:
Inverter maximum value  
[
1]:
Depletion layer maximum value  
[
2]:
Rectifier maximum value  
[
3]:
Air intake  
[
4]:
Interior of power unit  
[
5]:
Cooling unit liquid intake  
[
6]:
Capacitor air discharge  
[
7]:
Depletion layer maximum value 1  
[
8]:
Depletion layer maximum value 2  
[
9]:
Depletion layer maximum value 3  
[
10]:
Depletion layer maximum value 4

**Note:** 
  
The value of -200 indicates that there is no measuring signal.  
r0037[0]: Maximum value of the inverter temperatures.  
r0037[1]: Maximum value of the depletion layer temperatures.  
In the case of a fault, the particular shutdown threshold depends on the power unit,
and cannot be read out.

### r0039[0...2] Energy display

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Parameter group:** Mode signals / displays, Power loss optimization |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** kWh | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Display for the energy values at the drive output terminals.

**Index:** 
  
[
0]:
Energy balance (sum)  
[
1]:
Energy drawn  
[
2]:
Energy fed back

**Note:** 
  
For index [0]:  
Difference between the energy drawn and energy that is fed back.

### r0044 Thermal converter utilization

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Parameter group:** Mode signals / displays, Power unit |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** % | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** PERCENT |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the thermal converter utilization as a percentage.  
With this value, various thermal monitoring functions are taken into account.

**Dependency:** 
  
See also:
r0034

**Note:** 
  
The thermal motor utilization is displayed in parameter r0034.

### r0046.0...30 Missing enable signals

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Parameter group:** Control/status words, Drive enable signals |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source binary/numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the missing enable signals. All enable signals are required to operate the
drive. The enable signals are set by the control.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | OFF1 enable missing | No | Yes | 7954 |
| 01 | OFF2 enable missing | No | Yes | - |
| 02 | OFF3 enable missing | No | Yes | - |
| 03 | Operation enable missing | No | Yes | - |
| 08 | Safety enable missing | No | Yes | - |
| 10 | Ramp-function generator enable missing | No | Yes | - |
| 12 | Speed setpoint enable missing | No | Yes | - |
| 16 | OFF1 enable internal missing | No | Yes | - |
| 17 | OFF2 enable internal missing | No | Yes | - |
| 18 | OFF3 enable internal missing | No | Yes | - |
| 19 | Pulse enable internal missing | No | Yes | - |
| 21 | STOP2 enable internal missing | No | Yes | - |
| 26 | Drive inactive or not operational | No | Yes | - |
| 28 | Brake open missing | No | Yes | - |
| 30 | Speed controller enable missing | No | Yes | - |

**Dependency:** 
  
See also:
r0002

**Note:** 
  
The value r0046 = 0 indicates that all enable signals for this drive are present.  
Bit 00 = 1 (enable signal missing), if:  
- OFF1 from the PROFINET interface missing.  
- Switching on inhibited is active.  
  
Bit 01 = 1 (enable signal missing), if:  
- OFF2 from the PROFINET interface missing.  
  
Bit 02 = 1 (enable signal missing), if:  
- OFF3 from the PROFINET interface missing.  
  
Bit 03 = 1 (enable signal missing), if:  
- "Enable operation" from the PROFINET interface missing.  
  
Bit 08 = 1 (enable signal missing), if:  
- Safety functions have been enabled and STO is active.  
- A safety-relevant message with STO as response is active.  
STO enabled via terminals:  
- Pulse enable via the STO terminals has a 0 signal.  
- Additional details relating to the reason that STO was selected, see parameter r10352.  
  
Bit 10 = 1 (enable signal missing), if:  
- "Enable ramp-function generator" from the PROFINET interface missing.  
  
Bit 12 = 1 (enable signal missing), if:  
- "Enable setpoint" from the PROFINET interface missing.  
  
Bit 16 = 1 (enable signal missing), if:  
- There is an OFF1 fault response. The system is only enabled if the fault is removed
and was acknowledged and the "switching on inhibited" withdrawn with OFF1 = 0.  
  
Bit 17 = 1 (enable signal missing), if:  
- The commissioning mode is selected.  
- There is an OFF2 fault response.  
- The drive is inactive or not capable of operation.  
  
Bit 18 = 1 (enable signal missing), if:  
- OFF3 has still not been completed or an OFF3 fault response is present.  
  
Bit 19 = 1 (internal pulse enable missing), if:  
- Synchronization still not completed.  
  
Bit 21 = 1 (enable signal missing), if:  
The pulses have been enabled and the speed setpoint has still not been enabled, because:  
- The holding brake opening time has still not elapsed.  
- The encoder has not been calibrated (synchronous motor).  
  
Bit 26 = 1 (enable signal missing), if:  
- The drive is inactive or not capable of operation.  
- The drive device is in the "PROFIenergy energy-saving mode".  
  
Bit 28 = 1 (enable signal missing), if:  
- The holding brake is closed or has still not been opened.  
  
Bit 30 = 1 (speed controller inhibited), if one of the following applies:  
- Pulse enable missing  
- The function generator with current input is active.  
- The measuring function "current controller reference frequency characteristic" is
active.  
- The pole position identification is active.  
- Motor data identification is active (only certain steps).

### r0060 Speed setpoint before the setpoint filter

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN, S200 PN |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Parameter group:** Mode signals / displays, Speed setpoint filter |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** rpm | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2000 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the currently unsmoothed speed setpoint at the input of the speed controller
or U/f characteristic (after the interpolator).

### r0061[0...1] Actual speed unsmoothed

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN, S200 PN |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Parameter group:** Motor encoder, Mode signals / displays |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** rpm | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2000 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the unsmoothed speed actual values sensed by the encoders.

**Index:** 
  
[
0]:
Motor encoder  
[
1]:
Reserved

### r0062 Speed setpoint after the filter

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Parameter group:** U/f control, Speed controller, Mode signals / displays, Speed setpoint filter |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** rpm | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2000 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Display and numerical signal source for the speed setpoint after the setpoint filters.

### r0063 Speed actual value smoothed

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Parameter group:** U/f control, Speed controller, Speed actual value filter, Mode signals / displays |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** rpm | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2000 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Display for the smoothed speed actual value.

**Dependency:** 
  
See also:
r0021, r0061, p1441

**Note:** 
  
The smoothing time is set in p1441.  
The speed actual value is available strongly smoothed (r0021) and unsmoothed (r0061).

### r0068 Absolute current actual value

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Parameter group:** Mode signals / displays |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Arms | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2002 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays actual absolute current.

**Dependency:** 
  
See also:
r0027

**Notice:** 
  
For A_INF, S_INF the following applies:  
The value is updated with the current controller sampling time.  
The following applies for SERVO:  
The value is updated with a sampling time of 1 ms.

**Note:** 
  
Absolute current value = sqrt(Iq^2 + Id^2)  
The absolute current actual value is available smoothed (r0027) and unsmoothed (r0068).

### r0070 Actual DC link voltage

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Parameter group:** Vdc-min/max controller, Mode signals / displays, Power unit, Vdc controller |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** V | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2001 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Display and numerical signal source for the measured actual value of the DC link voltage.

**Dependency:** 
  
See also:
r0026

**Note:** 
  
The DC link voltage is available smoothed (r0026) and unsmoothed (r0070).

### r0072 Output voltage

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Parameter group:** U/f control, Current controller, Mode signals / displays, Power unit |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Vrms | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2001 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Display for the actual output voltage of the power unit.

### r0076 Current actual value field-generating

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Parameter group:** U/f control, Current controller, Mode signals / displays |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Arms | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2002 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Display for the field-generating current actual value.

### r0077 Current setpoint torque-generating

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Parameter group:** Current controller, Mode signals / displays |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Arms | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2002 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Display and numerical signal source for the torque/force-generating current setpoint.

**Note:** 
  
This value is irrelevant for the U/f control mode.

### r0078[0...1] Current actual value torque-generating

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Parameter group:** Mode signals / displays |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Arms | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2002 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Display for the actual value of the torque-generating current Iq.

**Index:** 
  
[
0]:
Unsmoothed  
[
1]:
Smoothed with 1 ms

### r0079[0...1] Torque setpoint total

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Parameter group:** Torque limiting, Mode signals / displays |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Nm | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2003 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Display for the torque setpoint at the output of the speed controller.

**Index:** 
  
[
0]:
Unsmoothed  
[
1]:
Smoothed with 1 ms

### r0080 Torque actual value

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Parameter group:** Motor model, Mode signals / displays |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Nm | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2003 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Display and numerical signal source for the torque actual value.

**Dependency:** 
  
See also:
r0031

**Note:** 
  
The value is available smoothed (r0031) and unsmoothed (r0080).

### r0081 Torque utilization

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Parameter group:** Torque limiting, Mode signals / displays |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** % | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** PERCENT |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the torque utilization as a percentage.  
The torque utilization is obtained from the required smoothed torque referred to the
torque limit.

**Note:** 
  
The torque utilization is obtained from the required torque referred to the torque
limit as follows:  
- Positive torque: r0081 = ((r0079 + p1532) / (r1538 - p1532)) * 100 %  
- Negative torque: r0081 = ((-r0079 + p1532) / (-r1539 + p1532)) * 100 %  
The calculation of the torque utilization depends on the selected smoothing time constant
(1 ms).

### r0082[0...3] Active power actual value

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Parameter group:** Mode signals / displays |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** kW | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** r2004 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the actual active power.

**Index:** 
  
[
0]:
Unsmoothed  
[
1]:
Smoothed with 1 ms  
[
2]:
Power drawn  
[
3]:
Power drawn smoothed

**Dependency:** 
  
See also:
r0032

**Note:** 
  
The mechanical active power is available smoothed (r0032 with 100 ms, r0082[1] with
1 ms) and unsmoothed (r0082[0]).  
For index [3]:  
Smoothing time constant = 0.25 ms

### r0196[0...255].0...15 Topology component status

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Parameter group:** Diagnostics general |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the status of the components.  
r0196[0]: Group status of all components  
r0196[1]: Status of component with component number 1  
...  
r0196[255]: Status of component with component number 255

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Component status bit 0 | Low | High | - |
| 01 | Component status bit 1 | Low | High | - |
| 02 | Component status bit 2 | Low | High | - |
| 03 | Component status bit 3 | Low | High | - |
| 04 | Component state | Inactive/parking | Active | - |
| 06 | Topology problem active | No | Yes | - |
| 07 | Part of the target topology | No only act topo | Yes | - |
| 08 | Alarm present | No | Yes | - |
| 09 | Safety message present | No | Yes | - |
| 10 | Fault present | No | Yes | - |
| 11 | Alarm class bit 0 | Low | High | - |
| 12 | Alarm class bit 1 | Low | High | - |
| 13 | Maintenance required | No | Yes | - |
| 14 | Maintenance urgently required | No | Yes | - |
| 15 | Fault gone/can be acknowledged | No | Yes | - |

**Note:** 
  
For bit 03 ... 00:  
Bit 3, 2, 1, 0 = 0, 0, 0, 0 --&gt; component not available.  
Bit 3, 2, 1, 0 = 0, 0, 0, 1 --&gt; run up, acyclic communications (LED = orange).  
Bit 3, 2, 1, 0 = 0, 0, 1, 0 --&gt; operating mode, cyclic communications (LED = green).  
Bit 3, 2, 1, 0 = 0, 0, 1, 1 --&gt; alarm (LED = green).  
Bit 3, 2, 1, 0 = 0, 1, 0, 0 --&gt; fault (LED = red).  
Bit 3, 2, 1, 0 = 0, 1, 0, 1 --&gt; detection via LED and operating mode (LED = green/orange).  
Bit 3, 2, 1, 0 = 0, 1, 1, 0 --&gt; detection via LED and alarm (LED = green/orange).  
Bit 3, 2, 1, 0 = 0, 1, 1, 1 --&gt; detection via LED and fault (LED = red/orange).  
Bit 3, 2, 1, 0 = 1, 0, 0, 0 --&gt; firmware being downloaded (LED = green/red with 0.5
Hz).  
Bit 3, 2, 1, 0 = 1, 0, 0, 1 --&gt; firmware download completed, wait for POWER ON (LED
= green/red with 2.0 Hz).  
For bits 12 ... 11:  
These status bits are used for the classification of internal alarm classes and are
intended for diagnostic purposes only on certain automation systems with integrated
SINAMICS functionality.

### p0201[0] Power unit code number

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Power unit |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 65535 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the actual code number of the power unit being used.

### p0210 Device supply voltage

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Power unit, Quick commissioning |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** V | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 1 [V] | 63000 [V] | [0] 400 [V] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the device supply voltage.  
The voltage between two phases should be entered as the device supply voltage.  
This setting is important for operating with voltages that are less than the voltage
range for which the drive is designed.

**Note:** 
  
Setting ranges for p0210 as a function of the rated power unit voltage:  
U_rated = 230 V:  
- p0210 = 200 ... 240 V  
U_rated = 400 V:  
- p0210 = 380 ... 480 V (wide voltage range, in addition to 200 ... 240 V)

### p0215 Braking resistor selection

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Dynamic braking, Quick commissioning |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 3 | 10 | [0] 10 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the external braking resistor.

**Value:** 
  
3:
Third-party braking resistor (with monitoring)  
10:
No monitoring (external braking resistor)

**Dependency:** 
  
See also:
p0216, p0218, p0219

**Note:** 
  
p0215 = 3:  
An externally connected braking resistor is controlled and also thermally monitored
per software.  
Parameters p0216, p0218 and p0219[0] and p0219[1] must be set in order that the monitoring
functions. Chopper operation is not possible if the values are not set.  
p0215 = 10:  
The externally connected braking resistor is not monitored.  
The internal braking resistor is monitored.

### p0216 Braking resistance value

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Dynamic braking, Quick commissioning |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ohm | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.0 [ohm] | 1000.0 [ohm] | [0] 0.0 [ohm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the resistance value of a connected external braking resistor.

**Dependency:** 
  
The parameter is only relevant for p0215 = 2, 3.

### p0218 Braking resistor maximum power duration

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Dynamic braking, Quick commissioning |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** s | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [s] | 2000.00 [s] | [0] 0.00 [s] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the maximum duration when operating the braking resistor at its maximum power
level.

**Dependency:** 
  
The parameter is only relevant for p0215 = 2, 3.

### p0219[0...1] Braking resistor braking power

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Dynamic braking, Quick commissioning |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** kW | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [kW] | 20000.00 [kW] | [0] 0.00 [kW] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the braking power of the connected braking resistor.

**Index:** 
  
[
0]:
Maximum power  
[
1]:
Rated power

### r0277[0] Power unit heat sink fan wear counter

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Parameter group:** Power unit |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** % | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the wear counter of the heat sink fan in the power unit.  
After a fan has been replaced, using an appropriate button, the value can be reset
in the commissioning tool to 0.

**Dependency:** 
  
See also:
A30042

### p0290 Power unit overload response

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Power unit |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 1 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the response to a thermal overload condition of the power unit.  
The following quantities can result in a response to thermal overload:  
- Heat sink temperature (r0037[0]).  
- Chip temperature (r0037[1]).  
- Power unit overload I2t (r0036).  
Possible measures to avoid thermal overload:  
- Reduce the output current limit r0289 and r0067 (for closed-loop speed/velocity
or torque/force control) or the output frequency (for U/f control indirectly via the
output current limit and the intervention of the current limiting controller).  
- Reduce the pulse frequency.  
A reduction, if parameterized, is always realized after an appropriate alarm is output.  
For p0290 = 0:  
When a temperature alarm threshold is exceeded, the output current is reduced, and
in turn, the output frequency. If the current reduction is not sufficient to thermally
relieve the power unit, when the drive reaches the temperature fault threshold it
switches off.  
This setting is not suitable for drives requiring a constant torque.  
Application:  
pumps, fans  
For p0290 = 1:  
The power unit operates at the required operating point. When the fault threshold
is reached, the drive switches off and an appropriate fault is output.  
Application:  
Drive applications where, as a result of the underlying process, no setpoint deviations
of individual drives in the group are permitted - or where the pulse frequency must
be strictly maintained.  
For p0290 = 2:  
The pulse frequency is reduced to a permissible minimum when a temperature alarm threshold
is exceeded. If the pulse frequency reduction is not sufficient to thermally relieve
the power unit, then the output current is also reduced.  
Application:  
Drives with a low dynamic performance and occasional overload where speed deviations
are permissible.  
For p0290 = 3:  
Only the pulse frequency is reduced to a permissible minimum when a temperature alarm
threshold is exceeded.  
Application:  
Drives with a low dynamic performance and occasional overload where a speed deviation
is not permissible.  
For p0290 = 10:  
For Booksize devices, in addition to the heat sink and chip temperatures, the difference
between the two temperatures is monitored as an additional variable. When a temperature
threshold is exceeded, the output current is reduced - and in turn, the output frequency.  
This overload response is activated as default setting for Booksize devices with a
pulse frequency higher than or equal to 16 kHz.  
For p0290 = 12:  
In this particular case, the chip temperature is evaluated based on the actual load.
If the temperature exceeds this alarm threshold, then the pulse frequency is reduced
to a permissible minimum. The output current is only reduced if the actual chip temperature
increases above a certain temperature threshold.  
Application:  
Drives that are frequently started and accelerated - and which manifest a significantly
fluctuating torque profile (e.g. centrifuges, flywheel presses, cranes).  
For p0290 = 13:  
In this particular case, the chip temperature is evaluated based on the actual load.
If the temperature exceeds this alarm threshold, then the pulse frequency is reduced
to a permissible minimum.  
Application:  
Drives that are frequently started and accelerated - and which manifest a significantly
fluctuating torque profile, and where the output current is not to be reduced (e.g.
centrifuges, flywheel presses, cranes).

**Value:** 
  
0:
Reduce output current  
1:
No reduction shutdown when overload threshold is reached

**Dependency:** 
  
For a thermal power unit overload, an appropriate alarm or fault is output and r2135.15
or r2135.13 set.  
Settings, where the pulse frequency is reduced, are not possible if the "Extended
torque control" function module (r0108.1) is activated.  
For p0290 = 2, 3:  
These responses are only applicable for blocksize power units.  
For p0290 = 10:  
This response is only applicable for booksize power units.  
See also:
r0036, r0037

**Notice:** 
  
If the thermal overload of the power unit is not sufficiently reduced by the actions
taken, the drive is always shut down. This means that the power unit is always protected
irrespective of the setting of this parameter.

**Note:** 
  
Under overload conditions, the current and torque limit are reduced, and therefore
the motor is braked and forbidden speed ranges (e.g. minimum speed p1080 and suppression
[skip] speeds p1091 ... p1094) can be passed through.  
When the motor data identification routine is selected, parameter p0290 cannot be
changed.  
For p0290 = 0, 2, 12:  
This is setting is only practical if the load decreases with decreasing speed (e.g.
for applications with variable torque such as for pumps and fans).  
For p0290 = 2, 3, 12, 13:  
The I2t overload detection of the power unit does not influence the response "Reduce
pulse frequency".  
For p0290 = 10, 12, 13:  
The possible load duty cycles, calculated based on the previous model (p0290 = 0,
1, 2, 3) for booksize power units cannot be transferred in every case. This is the
reason that we recommend that you contact our application support department if you
are uncertain about dimensioning the device.

### r0296 DC link voltage undervoltage threshold

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Parameter group:** Power unit |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** V | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Threshold to detect a DC link undervoltage.  
If the DC link voltage falls below this threshold, the drive unit is tripped due to
a DC link undervoltage condition.

**Dependency:** 
  
See also:
F30003

**Note:** 
  
The actual threshold value depends on the device type and the selected device supply
voltage (p0210).

### r0297 DC link voltage overvoltage threshold

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Parameter group:** Power unit |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** V | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Threshold to detect a DC link overvoltage.  
If the DC link voltage exceeds the threshold specified here, the drive device is tripped
due to DC link overvoltage.

**Dependency:** 
  
See also:
F30002

### p0300[0] Motor type selection

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Motor data, Quick commissioning |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 10000 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Selects the motor type or start to read in the motor parameters for a motor with self-identifying
data (p0300 = 10000).  
For p0300 &lt; 10000 the following applies:  
The first digit of the parameter value always defines the general motor type and corresponds
to the third-party motor belonging to a motor list:  
2 = rotating synchronous motor

**Value:** 
  
0:
No motor  
2:
Synchronous motor  
2120:
1FL2 synchronous motor  
10000:
Motor with data set

**Dependency:** 
  
See also:
p0301

### p0301[0] Motor code number selection

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Motor data, Quick commissioning |  |  |
| **Not relevant for motor type:**Separately excited synchronous motor |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 99999999 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Code number of the connected motor, whose data was accepted when commissioning.

**Dependency:** 
  
Code numbers are only possible for motor types that correspond to the motor type selected
in p0300.  
See also:
p0300

**Note:** 
  
For a motor with self-identifying data, p0301 cannot be changed. p0301 is automatically
written to the code number of the motor parameter read in (r0302) if p0300 is set
to 10000. For other values, the commissioning routine cannot be exited.

### r0302[0] Motor code (identified)

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Parameter group:** Motor data, Quick commissioning |  |  |
| **Not relevant for motor type:**Separately excited synchronous motor, Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the identified motor code number.  
When the drive powers up, the motor code is read out the motor. For r0302 = 0, the
motor data were not identified.

### p0304[0] Rated motor voltage

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Motor data, Quick commissioning |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Vrms | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 [Vrms] | 20000 [Vrms] | [0] 0 [Vrms] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the rated motor voltage.

### p0305[0] Rated motor current

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Motor data, Quick commissioning |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Arms | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [Arms] | 10000.00 [Arms] | [0] 0.00 [Arms] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the rated motor current.

### p0307[0] Rated motor power

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Motor data, Quick commissioning |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** kW | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [kW] | 100000.00 [kW] | [0] 0.00 [kW] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the rated motor power.

### p0311[0] Rated motor speed

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Motor data, Quick commissioning |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** rpm | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.0 [rpm] | 210000.0 [rpm] | [0] 0.0 [rpm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the rated motor speed.

### p0312[0] Rated motor torque

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Motor data |  |  |
| **Not relevant for motor type:**Induction motor, Separately excited synchronous motor, Synchronous or reluctance motor with starting cage, Synchronous reluctance motor |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Nm | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [Nm] | 1000000.00 [Nm] | [0] 0.00 [Nm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the rated motor torque.

### r0316[0] Motor torque constant

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Parameter group:** Motor data, Quick commissioning |  |  |
| **Not relevant for motor type:**Induction motor, Separately excited synchronous motor, Synchronous or reluctance motor with starting cage, Synchronous reluctance motor |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Nm/A | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the torque constant of the synchronous motor.  
r0316 = 0:  
The torque constant is calculated from the motor data.  
r0316 &gt; 0:  
The selected value is used as torque constant.

### p0318[0] Motor stall current

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Motor data |  |  |
| **Not relevant for motor type:**Induction motor, Separately excited synchronous motor, Synchronous or reluctance motor with starting cage, Synchronous reluctance motor |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Arms | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [Arms] | 10000.00 [Arms] | [0] 0.00 [Arms] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the rated motor stall current.

### p0319[0] Motor static torque

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Motor data |  |  |
| **Not relevant for motor type:**Induction motor, Separately excited synchronous motor, Synchronous or reluctance motor with starting cage, Synchronous reluctance motor |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Nm | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [Nm] | 100000.00 [Nm] | [0] 0.00 [Nm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the motor standstill/static torque.

### p0322[0] Maximum motor speed

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Motor data, Quick commissioning |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** rpm | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.0 [rpm] | 210000.0 [rpm] | [0] 0.0 [rpm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the maximum motor speed.

**Dependency:** 
  
See also:
p1082

### p0323[0] Maximum motor current

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Motor data, Quick commissioning |  |  |
| **Not relevant for motor type:**Induction motor, Separately excited synchronous motor, Synchronous reluctance motor |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Arms | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [Arms] | 20000.00 [Arms] | [0] 0.00 [Arms] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the maximum permissible motor current.

### r0341[0] Motor moment of inertia

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Parameter group:** Motor data, Speed controller |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** CALC_MOD_ALL |
| **Unit:** kgm² | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the motor moment of inertia (without load).

### p0400[0] Encoder type selection

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Motor encoder, Quick commissioning |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 10100 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Selects the encoder from the list of encoder types supported.

**Value:** 
  
0:
No encoder  
801:
Digital encoder interface AS17, singleturn  
802:
Digital encoder interface AS21, singleturn  
803:
Digital encoder interface AM21, multiturn 4096  
9999:
User defined  
10100:
Identify encoder (waiting)

**Notice:** 
  
An encoder type with p0400 &lt; 9999 defines an encoder for which there is an encoder
parameter list.  
When selecting a catalog encoder (p0400 &lt; 9999) the parameters from the encoder parameter
list cannot be changed (write protection).

**Note:** 
  
The connected encoder can be identified using p0400 = 10100. This means that the encoder
must support this.  
  
For p0400 = 10100 the following applies:  
The connected encoder is identified. If identification is not possible, then p0400
remains set = 10100, and the system waits until identification is possible.

### p0404[0].1...20 Encoder configuration effective

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Motor encoder |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| - | - | [0] 0000 0000 0000 0000 0000 0000 0000 0000 bin |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Settings for the basic encoder properties.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 01 | Absolute encoder | No | Yes | - |
| 02 | Multiturn encoder | No | Yes | - |
| 03 | Track A/B square-wave | No | Yes | - |
| 07 | Digital Encoder Interface | No | Yes | - |
| 20 | Voltage level 5 V | No | Yes | - |

**Notice:** 
  
This parameter is automatically pre-assigned for encoders from the encoder list and
for identify encoder (p0400).  
When selecting a catalog encoder, this parameter cannot be changed (write protection).
Information in p0400 should be carefully observed when removing write protection.

**Note:** 
  
For bit 01, 02 (absolute encoder, multiturn encoder):  
These bits can only be selected for a DEI encoder.

### p0408[0] Rotary encoder pulse number

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Motor encoder |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 16777215 | [0] 1024 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the number of pulses for a rotary encoder.  
In conjunction with the fine resolution, the pulse number defines the transfer format
for position actual values Gn_XIST1 (r0479).

**Notice:** 
  
This parameter is automatically pre-assigned for encoders from the encoder list and
for identify encoder (p0400).  
When selecting a catalog encoder, this parameter cannot be changed (write protection).

**Note:** 
  
The smallest permissible value is 1 pulse.  
This value does not always correspond to the pulse number of the measuring device.
For a DEI encoder, a value is entered here that facilitates optimum transfer of the
resolution (p0423).

### p0421[0] Absolute encoder rotary multiturn resolution

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Motor encoder |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 4294967295 | [0] 4096 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the number of revolutions that can be resolved for a rotary absolute encoder.

**Notice:** 
  
This parameter is automatically pre-assigned for encoders from the encoder list and
for identify encoder (p0400).  
When selecting a catalog encoder, this parameter cannot be changed (write protection).
Information in p0400 should be carefully observed when removing write protection.

### p0423[0] Absolute encoder rotary singleturn resolution

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Motor encoder |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 1073741823 | [0] 8192 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the number of measuring steps per revolution for a rotary absolute encoder.  
The resolution refers to the absolute position.

**Notice:** 
  
This parameter is automatically preset for encoders from the encoder list and for
"Encoder type selection" (p0400).  
When selecting a catalog encoder, this parameter cannot be changed (write protection).
Information in p0400 should be carefully observed when removing write protection.

### r0479[0...2] Diagnostics encoder position actual value Gn_XIST1

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN, S200 PN |  |  |
| **Data type:**Integer32 | **Visible in:**Standard display |  |
| **Parameter group:** Motor encoder |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Display for the encoder position actual value Gn_XIST1 according to PROFIdrive for
diagnostics.  
The value is displayed with sign.

**Index:** 
  
[
0]:
Motor encoder  
[
1]:
Reserved  
[
2]:
Reserved

### p0488[0...2] Measuring probe 1 input terminal

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN, S200 PN |  |  |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Measuring probe, Traversing blocks |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 210 | [0] 210  [1] 0  [2] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the input terminal to connect probe 1.

**Value:** 
  
0:
No measuring probe  
210:
DI 0 (X130.1)

**Index:** 
  
[
0]:
Motor encoder  
[
1]:
Reserved  
[
2]:
Reserved

**Dependency:** 
  
See also:
p0489, p0490

**Caution:** 
  
In order to prevent incorrect measurement values, these parameters may not be written
during an active measurement.

**Note:** 
  
DI: Digital Input  
Refer to the encoder interface for PROFIdrive.  
If parameterization is rejected, check whether the terminal is already being used
in p2517 or p2518.

### p0489[0...2] Measuring probe 2 input terminal

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN, S200 PN |  |  |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Measuring probe, Traversing blocks |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 211 | [0] 211  [1] 0  [2] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the input terminal to connect probe 2.

**Value:** 
  
0:
No measuring probe  
211:
DI 1 (X130.2)

**Index:** 
  
[
0]:
Motor encoder  
[
1]:
Reserved  
[
2]:
Reserved

**Dependency:** 
  
See also:
p0488, p0490

**Caution:** 
  
In order to prevent incorrect measurement values, these parameters may not be written
during an active measurement.

**Note:** 
  
DI: Digital Input  
Refer to the encoder interface for PROFIdrive.  
If parameterization is rejected, check whether the terminal is already being used
in p2517 or p2518.

### p0490.0...1 Invert measuring probe or equivalent zero mark

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN, S200 PN |  |  |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Measuring probe |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| - | - | [0] 0000 bin |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Setting to invert the digital input signals to connect a measuring probe or an equivalent
zero mark.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | DI 0 (X130.1) | Not inverted | Inverted | - |
| 01 | DI 1 (X130.2) | Not inverted | Inverted | - |

**Dependency:** 
  
See also:
p0488, p0489, p0494

**Note:** 
  
The terminal must be set as input.  
When the measuring probe or the equivalent zero mark is inverted, this has no effect
on the status displays of the digital inputs (r0721, r0722).  
DI: Digital Input

### p0494[0] Equivalent zero mark input terminal

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN, S200 PN |  |  |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Motor encoder, Homing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 211 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Selects the input terminal for connecting an equivalent zero mark (external encoder
zero mark).

**Value:** 
  
0:
No equivalent zero mark (evaluation of the encoder zero mark)  
210:
DI 0 (X130.1)  
211:
DI 1 (X130.2)

**Dependency:** 
  
See also:
p0490

**Caution:** 
  
In order to prevent incorrect measurement values, these parameters may not be written
during an active measurement.

**Note:** 
  
Refer to the encoder interface for PROFIdrive.

### p0550[0] Brake version

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Motor holding brake, Quick commissioning |  |  |
| **Not relevant for motor type:**Separately excited synchronous motor, Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 2 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the brake version.

**Value:** 
  
0:
No data  
1:
Holding brake  
2:
High performance holding brake

**Notice:** 
  
After entering a corresponding code number (p0551), this parameter is automatically
pre-assigned and write protected. The information in p0551 should be observed when
removing write protection.

**Note:** 
  
For p0550 = 1:  
The default value for opening time/closing time applies.  
For p0550 = 2:  
A shorter opening time/closing time is realized if the power unit supports the function.

### p0551[0] Brake code number

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Motor holding brake, Quick commissioning |  |  |
| **Not relevant for motor type:**Separately excited synchronous motor, Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 4294967295 | [0] 1 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Setting the code number for the brake.  
0 = No data  
1 = Manual entry  
&gt; 1 = valid code number  
For value = 0:  
- Parameters listed under Dependent are set to a value of zero and are write protected.  
- Parameters p1216, p1217 are set to a value of zero.  
For value = 1:  
- Write protection for the parameters listed under Dependent is withdrawn.  
For value &gt; 1:  
- Parameters listed under Dependent are automatically pre-assigned and are write protected.  
- Parameters p1216, p1217 are automatically appropriately pre-assigned.

**Dependency:** 
  
See also:
p0550

**Note:** 
  
Only code numbers can be set that are permitted for the selected motor code (p0301).

### p0613[0] Mot_temp_mod 1/3 ambient temperature

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Motor temperature |  |  |
| **Not relevant for motor type:**Induction motor, Separately excited synchronous motor, Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** CALC_MOD_ALL |
| **Unit:** °C | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| -40 [°C] | 100 [°C] | [0] 20 [°C] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
If the thermal motor model is activated for permanent-magnet synchronous motors, then
the parameter is incorporated in the model calculation if a temperature sensor is
not being used.

**Dependency:** 
  
See also:
F07011, A07012

**Note:** 
  
If the thermal motor model is activated for permanent-magnet synchronous motors, then
the parameter is incorporated in the model calculation if a temperature sensor is
not being used.

### r0721.0...3 CU digital inputs terminal actual value

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN, S200 PN |  |  |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Parameter group:** Digital inputs |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the actual value at the digital inputs.  
This means that the actual input signal can be checked at terminal DI x prior to switching
from the simulation mode (p0795.x = 1) to the terminal mode (p0795.x = 0).

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | DI 0 (X130.1) | Low | High | - |
| 01 | DI 1 (X130.2) | Low | High | - |
| 02 | DI 2 (X130.3) | Low | High | - |
| 03 | DI 3 (X130.4) | Low | High | - |

**Note:** 
  
DI: Digital Input

### r0722.0...3 Digital inputs status

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN, S200 PN |  |  |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Parameter group:** Digital inputs |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source binary/numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Display and signal source for the status of the digital inputs.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | DI 0 (X130.1) | Low | High | - |
| 01 | DI 1 (X130.2) | Low | High | - |
| 02 | DI 2 (X130.3) | Low | High | - |
| 03 | DI 3 (X130.4) | Low | High | - |

**Dependency:** 
  
See also:
p0488, p0489

**Note:** 
  
DI: Digital Input  
For bits 00, 01: DI 0 and DI 1 are fast digital inputs and can be used as measuring
probe (p0488, p0489).

### c0730 Signal for terminal DO 0

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN, S200 PN |  |  |
| **Data type:**Unsigned8 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Relay outputs, Digital outputs |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink binary |  |  |
| **Factory interconnection:** | **Fixed value:** |  |
| 899.2 | 0 |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal for terminal DO 0 (X130.11/12).

**Note:** 
  
DO: Digital Output

### r0747.0 Digital outputs status

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN |  |  |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Parameter group:** Relay outputs, Digital outputs |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the status of digital outputs.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | DO 0 (DO+: X130.11 / DO-: X130.12) | Low | High | - |

**Note:** 
  
DO: Digital Output

### p0795.0...3 Digital inputs simulation mode

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN, S200 PN |  |  |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Digital inputs |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| - | - | [0] 0000 bin |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the simulation mode for digital inputs.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | DI 0 (X130.1) | Terminal eval | Simulation | - |
| 01 | DI 1 (X130.2) | Terminal eval | Simulation | - |
| 02 | DI 2 (X130.3) | Terminal eval | Simulation | - |
| 03 | DI 3 (X130.4) | Terminal eval | Simulation | - |

**Dependency:** 
  
The setpoint for the input signals is specified using p0796.  
See also:
p0796

**Note:** 
  
This parameter is not saved when backing up data (p0977).  
DI: Digital Input

### p0796.0...3 Digital inputs simulation mode setpoint

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN, S200 PN |  |  |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Digital inputs |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| - | - | [0] 0000 bin |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the setpoint for the input signals in the digital input simulation mode.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | DI 0 (X130.1) | Low | High | - |
| 01 | DI 1 (X130.2) | Low | High | - |
| 02 | DI 2 (X130.3) | Low | High | - |
| 03 | DI 3 (X130.4) | Low | High | - |

**Dependency:** 
  
The simulation of a digital input is selected using p0795.  
See also:
p0795

**Note:** 
  
This parameter is not saved when backing up data (p0977).  
DI: Digital Input

### c0849[0] No Quick Stop / Quick Stop (OFF3)

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN, S200 PN |  |  |
| **Data type:**Unsigned8 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Shutdown functions, Drive enable signals |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink binary |  |  |
| **Factory interconnection:** | **Fixed value:** |  |
| not interconnected | 1 |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Second signal for command "No Quick Stop / Quick Stop (OFF3)"  
The following signals are AND'ed:  
- c0848 "No Quick Stop / Quick Stop (OFF3) signal 1"  
- c0849 "No Quick Stop / Quick Stop (OFF3) signal 2"  
For the PROFIdrive profile, the result of the AND logic operation corresponds to control
word 1 bit 2 (STW1.2).  
c0848 = 0 signal or c0849 = 0 signal  
- OFF3 (braking along the OFF3 ramp (p1135), then pulse cancellation and switching
on inhibited)  
c0848 = 1 signal or c0849 = 1 signal  
- No OFF3 (enable is possible)

**Caution:** 
  
When "master control from PC" is activated, then this binary signal sink is effective.

**Note:** 
  
For drives with closed-loop torque control (activated using c1501), the following
applies:  
0 signal:  
- No dedicated braking response, but pulse cancellation when standstill is detected
(p1226, p1227).

### r0898.0...14 Control word sequence control

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Standard display |  |
| **Parameter group:** Control/status words |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source binary/numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Display and numerical signal source for the control word of the sequence control.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | ON/OFF1 | No | Yes | - |
| 01 | Operating condition / OFF2 | No | Yes | - |
| 02 | Operating condition / OFF3 | No | Yes | - |
| 03 | Enable operation | No | Yes | - |
| 04 | Enable ramp-function generator | No | Yes | - |
| 05 | Continue ramp-function generator | No | Yes | - |
| 06 | Enable speed setpoint | No | Yes | - |
| 07 | Command open brake | No | Yes | - |
| 10 | Master control by PLC | No | Yes | - |
| 12 | Enable speed controller | No | Yes | - |
| 14 | Command close brake | No | Yes | - |

**Note:** 
  
OC: Operating condition

### r0899.0...13 Status word sequence control

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Standard display |  |
| **Parameter group:** Control/status words |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source binary/numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Display for the status word of the sequence control.  
The status word is cyclically sent from the drive to the higher-level control.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Ready for switching on | No | Yes | - |
| 01 | Ready | No | Yes | - |
| 02 | Operation enabled | No | Yes | - |
| 03 | Jog active | No | Yes | - |
| 04 | No coasting active | OFF2 active | OFF2 inactive | - |
| 05 | No Quick Stop active | OFF3 active | OFF3 inactive | - |
| 06 | Switching on inhibited active | No | Yes | - |
| 07 | Drive ready | No | Yes | - |
| 08 | Controller enable | No | Yes | - |
| 09 | Control requested | No | Yes | - |
| 11 | Pulses enabled | No | Yes | - |
| 12 | Motor holding brake control | No | Yes | - |
| 13 | Motor holding brake status | No | Yes | - |

**Note:** 
  
For bits 00, 01, 02, 04, 05, 06, 09:  
For PROFIdrive, these signals are used for status word 1.  
For bit 13:  
When function "SBC (Safe Brake Control)" is activated and selected, the brake is no
longer controlled using this signal.

### r0922 PROFIdrive PZD telegram selection

[S200 Basic PN](#r0922-profidrive-pzd-telegram-selection-1)

[S200 Basic PN Interpolator for EPOS](#r0922-profidrive-pzd-telegram-selection-2)

#### r0922 PROFIdrive PZD telegram selection

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN, S200 PN |  |  |
| **Data type:**Unsigned16 | **Visible in:**Standard display |  |
| **Parameter group:** Quick commissioning, Configuration |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the PROFIdrive telegram.

**Value:** 
  
1:
Standard telegram 1, PZD-2/2  
2:
Standard telegram 2, PZD-4/4  
3:
Standard telegram 3, PZD-5/9  
5:
Standard telegram 5, PZD-9/9  
102:
SIEMENS telegram 102, PZD-6/10  
105:
SIEMENS telegram 105, PZD-10/10

**Note:** 
  
The telegram is set in the commissioning tool or by the control.

#### r0922 PROFIdrive PZD telegram selection

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN (Interpolator for EPOS), S200 PN (Interpolator for EPOS) |  |  |
| **Data type:**Unsigned16 | **Visible in:**Standard display |  |
| **Parameter group:** Quick commissioning, Configuration |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the PROFIdrive telegram.

**Value:** 
  
7:
Standard telegram 7, PZD-2/2  
9:
Standard telegram 9, PZD-10/5  
111:
SIEMENS telegram 111, PZD-12/12  
112:
SIEMENS telegram 112, PZD-17/12  
999:
Free telegram configuration via signal interconnection

**Note:** 
  
The telegram is set in the commissioning tool or by the control.

### r0924[0...1] ZSW bit pulses enabled

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN, S200 PN |  |  |
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Parameter group:** Configuration |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the position of the "Pulses enabled" status signal in the PROFIdrive telegram.

**Index:** 
  
[
0]:
Signal number  
[
1]:
Bit position

### p0925 PROFIdrive clock synchronous sign-of-life tolerance

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN, S200 PN |  |  |
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Configuration |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 65535 | [0] 1 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the number of tolerated consecutive sign-of-life errors of the isochronous controller.  
The sign-of-life signal is normally received in PZD4 (control word 2) from the controller.

**Dependency:** 
  
See also:
F01912

**Note:** 
  
The sign-of-life monitoring is disabled for p0925 = 65535.

### r0930 PROFIdrive operating mode

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN, S200 PN |  |  |
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Parameter group:** Configuration |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the operating mode.  
1: Closed-loop speed controlled operation with ramp-function generator  
2: Closed-loop position controlled operation  
3: Closed-loop speed controlled operation without ramp-function generator

### r0944 Counter for fault buffer changes

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Parameter group:** Faults / alarms |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Display and numerical signal source for the counter for changes of the fault buffer.  
This counter is incremented every time the fault buffer changes.

**Recommendation:** 
  
Used to check whether the fault buffer has been read out consistently.

**Dependency:** 
  
See also:
r0945, r0947, r0948, r0949, r2109

### r0945[0...63] Fault code

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Parameter group:** Faults / alarms |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the codes of faults that have occurred.

**Dependency:** 
  
See also:
r0947, r0948, r0949, r2109, r2130, r2133, r2136, r3122

**Notice:** 
  
The properties of the fault buffer should be taken from the corresponding product
documentation.

**Note:** 
  
The buffer parameters are cyclically updated (states are indicated in r2139).  
Fault buffer structure (general principle):  
r0945[0], r0949[0] or r2133[0], r2130[0], r0948[0], r2136[0], r2109[0]  
--&gt; Fault 1 (oldest active fault) of the active incident  
. . .  
r0945[7], r0949[7] or r2133[7], r2130[7], r0948[7], r2136[7], r2109[7]  
--&gt; fault 8 (oldest active fault) of the active incident  
  
For more than 8 active faults, only the entries are overwritten at the eighth position
(index 7).  
  
History of acknowledged faults:  
If a fault incident is acknowledged, then all alarms of the 1st fault incident are
transferred into the 2nd fault incident, this becomes the 1st acknowledged fault incident.  
The 2nd incident is transferred into the 3rd, the 3rd into the 4th etc. The last incident
is rejected.  
  
r0945[8], r0949[8] or r2133[8], r2130[0], r0948[8], r2136[8], r2109[8]  
--&gt; fault 1 of the 1st acknowledged incident  
. . .  
r0945[16], r0949[16] or r2133[16], r2130[16], r0948[16], r2136[16], r2109[16]  
--&gt; fault 1 of the 2nd acknowledged incident  
. . .  
r0945[56], r0949[56] or r2133[56], r2130[56], r0948[56], r2136[56], r2109[56]  
--&gt; fault 1 of the 7th acknowledged incident  
. . .  
r0945[63], r0949[63] or r2133[63], r2130[63], r0948[63], r2136[63], r2109[63]  
--&gt; fault 8 (oldest fault that has gone) of the 7th acknowledged incident

### r0947[0...63] Fault number

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Parameter group:** Faults / alarms |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the numbers of faults that have occurred.

**Dependency:** 
  
See also:
r0945

**Notice:** 
  
The properties of the fault buffer should be taken from the corresponding product
documentation.

**Note:** 
  
The buffer parameters are cyclically updated (states are indicated in r2139).  
Fault buffer structure (general principle):  
r0945[0], r0949[0] or r2133[0], r2130[0], r0948[0], r2136[0], r2109[0] --&gt; fault 1
(oldest active fault) of the active incident  
. . .  
r0945[7], r0949[7] or r2133[7], r2130[7], r0948[7], r2136[7], r2109[7] --&gt; fault 8
(latest active fault) of the active incident  
For more than 8 active faults, only the entries are overwritten at the eighth position
(index 7).  
  
History of acknowledged faults:  
If a fault incident is acknowledged, then all alarms of the 1st fault incident are
transferred into the 2nd fault incident, this becomes the 1st acknowledged fault incident.  
The 2nd incident is transferred into the 3rd, the 3rd into the 4th etc. The last incident
is rejected.  
  
r0945[8], r0949[8] or r2133[8], r2130[0], r0948[8], r2136[8], r2109[8] --&gt; fault 1
of the 1st acknowledged incident  
. . .  
r0945[16], r0949[16] or r2133[16], r2130[16], r0948[16], r2136[16], r2109[16] --&gt;
fault 1 of the 2nd acknowledged incident  
. . .  
r0945[56], r0949[56] or r2133[56], r2130[56], r0948[56], r2136[56], r2109[56] --&gt;
fault 1 of the 7th acknowledged incident  
. . .  
r0945[63], r0949[63] or r2133[63], r2130[63], r0948[63], r2136[63], r2109[63] --&gt;
fault 8 (oldest fault that has gone) of the 7th acknowledged incident

### r0948[0...63] Fault time received in milliseconds

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Parameter group:** Faults / alarms |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the system runtime in milliseconds when the fault occurred.

**Dependency:** 
  
See also:
r0945, r0947, r0949, r2109, r2114, r2130, r2133, r2136, r3122

**Notice:** 
  
The time comprises r2130 (days) and r0948 (milliseconds).

**Note:** 
  
The buffer parameters are cyclically updated in the background (refer to status signal
in r2139).  
The structure of the fault buffer and the assignment of the indices is shown in r0945.  
When the parameter is read via PROFIdrive, the TimeDifference data type applies.

### r0949[0...63] Fault value

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer32 | **Visible in:**Extended display |  |
| **Parameter group:** Faults / alarms |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays additional information about the fault that occurred (as integer number).

**Dependency:** 
  
See also:
r0945, r0947, r0948, r2109, r2130, r2133, r2136, r3122

**Note:** 
  
The buffer parameters are cyclically updated in the background (refer to status signal
in r2139).  
The structure of the fault buffer and the assignment of the indices is shown in r0945.

### p0952 Fault cases counter

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Faults / alarms |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 65535 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Number of fault situations that have occurred since the last reset.

**Dependency:** 
  
The fault buffer is deleted (cleared) by setting p0952 to 0.  
In order that faults with "POWER ON" acknowledgment can also be cleared from the fault
buffer, POWER ON must first be carried out.  
See also:
r0945, r0947, r0948, r0949, r2109, r2130, r2133, r2136

### r0964[0...6] Device identification

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Standard display |  |
| **Parameter group:** System identification |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the device identification.

**Index:** 
  
[
0]:
Company (Siemens = 42)  
[
1]:
Device type  
[
2]:
Firmware version  
[
3]:
Firmware date (year)  
[
4]:
Firmware date (day/month)  
[
5]:
Reserved  
[
6]:
Firmware patch/hot fix

**Note:** 
  
Example:  
r0964[0] = 42 --&gt; SIEMENS  
r0964[1] = device type, see below  
r0964[2] = 602 --&gt; first part firmware version V06.02 (second part, refer to index
6)  
r0964[3] = 2023 --&gt; year 2023  
r0964[4] = 1706 --&gt; June 17  
r0964[5] = 1 --&gt; 1 (fixed value)  
r0964[6] = 0 --&gt; second part firmware version (complete version: V06.02.00.00)  
Device type:  
r0964[1] = 11200 --&gt; SINAMICS S200 PN  
r0964[1] = 11202 --&gt; SINAMICS S200 PTI  
r0964[1] = 11210 --&gt; SINAMICS S200 Basic PN  
r0964[1] = 11212 --&gt; SINAMICS S200 Basic PTI

### r0965 PROFIdrive profile number profile version

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN, S200 PN |  |  |
| **Data type:**Unsigned16 | **Visible in:**Standard display |  |
| **Parameter group:** Configuration |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the PROFIdrive profile number and profile version.  
Constant value = 032A hex.  
Byte 1: Profile number = 03 hex = PROFIdrive profile  
Byte 2: profile version = 2A hex = 42 dec = version 4.2

**Note:** 
  
When the parameter is read via PROFIdrive, the Octet String 2 data type applies.

### p0972 Drive unit reset

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Save &amp; reset |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 3 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the required procedure to execute a hardware reset for the drive unit.

**Value:** 
  
0:
Inactive  
1:
Hardware-Reset immediate  
2:
Hardware reset preparation  
3:
Hardware reset after cyclic communication has failed

**Danger:** 
  
It must be absolutely ensured that the system is in a safe condition.  
The memory card/device memory of the converter must not be accessed.

**Note:** 
  
For value = 1:  
Reset is immediately executed and communications interrupted.  
After communications have been established, check the reset operation (refer below).  
This value cannot be set in operation.  
For value = 2:  
Help to check the reset operation.  
Firstly, set p0972 = 2 and then read back. Secondly, set p0972 = 1 (it is possible
that this request is possibly no longer acknowledged). The communication is then interrupted.  
After communications have been established, check the reset operation (refer below).  
For value = 3:  
The reset is executed after interrupting cyclic communication. This setting is used
to implement a synchronized reset by a control for several drive units.  
If cyclic communication is not active, then the reset is immediately executed.  
After communications have been established, check the reset operation (refer below).  
To check the reset operation:  
After the drive unit has been restarted and communications have been established,
read p0972 and check the following:  
p0972 = 0 --&gt; the reset was successfully executed.  
p0972 &gt; 0 --&gt; the reset was not executed.

### r0975[0...10] Converter identification

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Parameter group:** System identification |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the identification of the converter. The drive internally comprises components,
device and converter. Both components require their own identification parameters
according to PROFIdrive.

**Index:** 
  
[
0]:
Company (Siemens = 42)  
[
1]:
Converter type  
[
2]:
Firmware version  
[
3]:
Firmware date (year)  
[
4]:
Firmware date (day/month)  
[
5]:
PROFIdrive converter type class  
[
6]:
PROFIdrive converter subtype class  
[
7]:
Reserved  
[
8]:
Reserved  
[
9]:
Reserved  
[
10]:
Firmware patch/hot fix

**Dependency:** 
  
See also:
r0964

**Note:** 
  
Example:  
r0975[0] = 42 --&gt; SIEMENS  
r0975[1] = 311 --&gt; SERVO converter type  
r0975[2] = 602 --&gt; first part firmware version V06.02 (second part refer to index
10)  
r0975[3] = 2023 --&gt; year 2023  
r0975[4] = 1706 --&gt; 17th of June  
r0975[5] = 1 --&gt; PROFIdrive type class = 1 (axis)  
r0975[6] = 8 --&gt; PROFIdrive subtype class = 4 (application class)  
r0975[7] = 1 --&gt; 1 (fixed value)  
r0975[8] = 0 (reserved)  
r0975[9] = 0 (reserved)  
r0975[10] = 0 --&gt; second part firmware version (complete version: V06.02.00.00)

### p0976 Reset all parameters

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Save &amp; reset |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 1 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Resets all drive system parameters to the factory settings.

**Value:** 
  
0:
Inactive  
1:
Start to reset all parameters

**Notice:** 
  
Writing to parameters is inhibited during the reset operation.

### p0977 Save all parameters

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Save &amp; reset |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 1 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Retentively saves all parameters of the drive system to the non-volatile memory.  
When saving, only the adjustable parameters intended to be saved are taken into account.

**Value:** 
  
0:
Inactive  
1:
Save in non-volatile memory - Loaded at POWER ON

**Dependency:** 
  
See also:
p0976

**Notice:** 
  
The converter power supply may only be switched off after saving has been completed
(i.e. after saving has started, wait until the parameter again has a value of 0).  
Writing to parameters is inhibited while saving.

### r0979[0...30] PROFIdrive encoder format

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN, S200 PN |  |  |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Parameter group:** System identification, Configuration |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the actual position encoder used according to PROFIdrive.

**Index:** 
  
[
0]:
Header  
[
1]:
Motor encoder type  
[
2]:
Motor encoder resolution  
[
3]:
Shift factor G1_XIST1  
[
4]:
Shift factor G1_XIST2  
[
5]:
Distinguishable revolutions motor encoder  
[
6...30]:
Reserved

**Note:** 
  
Information about the individual indices can be taken from the following literature:  
PROFIdrive Profile Drive Technology

### r0980[0...299] List of existing parameters 1

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Parameter group:** System identification |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Displays the parameters that exist for this drive.

**Note:** 
  
Modified parameters are displayed in indices 0 to 298. If an index contains the value
0, then the list ends here. In a long list, index 299 contains the parameter number
at which position the list continues.  
This list consists solely of the following parameters:  
r0980[0...299], r0981[0...299] ... r0989[0...299]  
The parameters in this list are not displayed in the parameter lists of the commissioning
tool. However, they can be read from a higher-level control system (e.g. PROFIBUS
master).

### p1082[0] Maximum speed

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Motorized potentiometer, Speed limiting, U/f control, Speed controller, Quick commissioning |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** CALC_MOD_ALL |
| **Unit:** rpm | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.000 [rpm] | 210000.000 [rpm] | [0] 1500.000 [rpm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the maximum motor speed to a value less than or equal to the maximum motor speed
(p0322).  
The set value is valid for both directions of rotation.

**Dependency:** 
  
See also:
p0322

### p1083[0] Speed limit in positive direction of rotation

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Speed limiting, U/f control, Speed controller |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** rpm | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2000 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.000 [rpm] | 210000.000 [rpm] | [0] 210000.000 [rpm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the maximum speed for the positive direction.

### p1086[0] Speed limit in negative direction of rotation

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Speed limiting, U/f control, Speed controller |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** rpm | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2000 |
| **Min:** | **Max:** | **Factory setting:** |
| -210000.000 [rpm] | 0.000 [rpm] | [0] -210000.000 [rpm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the speed limit for the negative direction.

### p1115 Ramp-function generator selection

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN, S200 PN, S200 PTI |  |  |
| **Data type:**Integer16 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Ramp-function generator |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 1 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the ramp-function generator type.

**Value:** 
  
0:
Basic ramp-function generator  
1:
Extended ramp-function generator

**Note:** 
  
Another ramp-function generator type can only be selected when the motor is at a standstill.

### p1120[0] Ramp-function generator ramp-up time

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN, S200 PN, S200 PTI |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Ramp-function generator, Quick commissioning |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** s | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.000 [s] | 999999.000 [s] | [0] 10.000 [s] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
The ramp-function generator ramps-up the speed setpoint from standstill (setpoint
= 0) up to the maximum speed (p1082) in this time.

**Dependency:** 
  
See also:
p1082

### p1121[0] OFF1 ramp-down time

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Quick commissioning |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** s | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.000 [s] | 999999.000 [s] | [0] 1.000 [s] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the ramp-down time after an OFF1 command.  
The value is referred to the maximum speed (p1082).  
After an OFF1 command, within this time, the speed setpoint is ramped down from the
maximum speed (p1082) to standstill.

**Dependency:** 
  
See also:
p1082

### p1130[0] Ramp-function generator initial rounding-off time

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN, S200 PN, S200 PTI |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Ramp-function generator |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** s | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.000 [s] | 30.000 [s] | [0] 0.000 [s] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the initial rounding-off time for the extended ramp-function generator.  
The value applies to ramp-up and ramp-down.

**Note:** 
  
Rounding-off times avoid an abrupt response and prevent damage to the mechanical system.

### p1131[0] Ramp-function generator final rounding-off time

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN, S200 PN, S200 PTI |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Ramp-function generator |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** s | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.000 [s] | 30.000 [s] | [0] 0.000 [s] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the final rounding-off time for the extended ramp generator.  
The value applies to ramp-up and ramp-down.

**Note:** 
  
Rounding-off times avoid an abrupt response and prevent damage to the mechanical system.

## SINAMICS Parameter S200 Basic PN 01135 - 02502

SINAMICS Parameter S200 Basic PN 01135 - 02502

### p1135[0] OFF3 ramp-down time

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Ramp-function generator, Shutdown functions, Setpoint addition, Quick commissioning |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** s | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.000 [s] | 600.000 [s] | [0] 0.000 [s] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the ramp-down time from the maximum speed down to zero speed for the OFF3 command.

**Note:** 
  
This time can be exceeded if the DC link voltage reaches its maximum value.

### r1196 DSC position setpoint

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN, S200 PN |  |  |
| **Data type:**Integer32 | **Visible in:**Standard display |  |
| **Parameter group:** Speed precontrol |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Display and numerical signal source of the position setpoint of DSC in fine pulses.

**Note:** 
  
DSC: Dynamic Servo Control

### p1215[0] Motor holding brake configuration

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN, S200 Basic PTI |  |  |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Motor holding brake |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 3 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the configuration for the motor holding brake.

**Value:** 
  
0:
No motor holding brake available  
3:
Motor holding brake like seq control, conn via interconnection

**Dependency:** 
  
See also:
p1216, p1217, p1226, p1227, p1228

**Caution:** 
  
For the setting p1215 = 0, if a brake is used, it remains closed. If the motor moves,
this will destroy the brake.

**Notice:** 
  
If p1215 was set to 3, then when the pulses are canceled, the brake is closed even
if the motor is still rotating. Pulses can be canceled as a result of an OFF2 or "Enable
operation" via fieldbus or a fault with OFF2 response.

**Note:** 
  
If an external motor holding brake is being used, then p1215 should be set to 3 and
r0899.12 should be used as brake control signal.  
The parameter can only be set to zero when the pulses are inhibited.

### p1216[0] Motor holding brake opening time

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Motor holding brake |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 [ms] | 10000 [ms] | [0] 100 [ms] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the opening time for the motor holding brake.  
The speed setpoint is kept at 0 for this time. The speed setpoint is then enabled.

**Dependency:** 
  
See also:
p1215, p1217

### p1217[0] Motor holding brake closing time

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Motor holding brake |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 [ms] | 10000 [ms] | [0] 100 [ms] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the time to apply the motor holding brake.  
After OFF1 or OFF3 and the holding brake is controlled (the brake closes), then the
drive remains closed-loop controlled for this time stationary with a speed setpoint/velocity
setpoint of zero. The pulses are canceled when the time expires.

**Recommendation:** 
  
This time should be set longer than the actual closing time of the brake. This ensures
that the pulses are only canceled after the brake has closed.

**Dependency:** 
  
See also:
p1215, p1216

**Notice:** 
  
If the selected closing time is too short with respect to the actual closing time
of the brake, then the load can sag.  
If the closing time is selected to be too long with respect to the actual closing
time of the brake, the control works against the brake and therefore reduces its lifetime.

**Note:** 
  
The time is preassigned with the value saved in the motor.

### p1226[0] Threshold for zero speed detection

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Motor holding brake, Shutdown functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** rpm | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [rpm] | 210000.00 [rpm] | [0] 20.00 [rpm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the speed threshold for the standstill identification.  
Acts on the actual value and setpoint monitoring.  
When braking with OFF1 or OFF3, when the threshold is undershot, standstill is identified.  
The following applies when the brake control is activated:  
When the threshold is undershot, the brake control is started and the system waits
for the brake closing time in p1217. The pulses are then canceled.  
if the brake control is not activated, the following applies:  
When the threshold is undershot, the pulses are canceled and the drive coasts down.

**Dependency:** 
  
See also:
p1215, p1216, p1217, p1227

**Notice:** 
  
For reasons relating to the compatibility to earlier firmware versions, a parameter
value of zero in indices 1 to 31 is overwritten with the parameter value in index
0 when the Control Unit boots.

**Note:** 
  
Standstill is identified in the following cases:  
- The speed actual value falls below the speed threshold in p1226 and the time started
after this in p1228 has expired.  
- The speed setpoint falls below the speed threshold in p1226 and the time started
after this in p1227 has expired.  
The actual value sensing is subject to measuring noise. For this reason, standstill
cannot be detected if the speed threshold is too low.

### p1227[0] Zero speed detection monitoring time

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Motor holding brake, Shutdown functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** s | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.000 [s] | 300.000 [s] | [0] 4.000 [s] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the monitoring time for the standstill identification.  
When braking with OFF1 or OFF3, standstill is identified after the time set here has
expired, after the setpoint speed has fallen below p1226.  
After this, the brake control is started, the system waits for the closing time in
p1217 and then the pulses are canceled.

**Dependency:** 
  
See also:
p1215, p1216, p1217, p1226

**Note:** 
  
Standstill is detected if at least one of the following conditions is satisfied:  
- The speed actual value falls below the speed threshold in p1226 and the time started
after this in p1228 has expired.  
- The speed setpoint falls below the speed threshold in p1226 and the time started
after this in p1227 has expired.  
  
For p1227 = 300.000 s the following applies:  
Monitoring is deactivated.  
For p1227 = 0.000 s, the following applies:  
With OFF1 or OFF3 and a ramp-down time = 0, the pulses are immediately canceled and
the motor "coasts" down.

### p1228[0] Pulse cancellation delay time

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Motor holding brake, Shutdown functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** s | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.000 [s] | 299.000 [s] | [0] 0.000 [s] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the delay time for pulse cancellation.  
After OFF1 or OFF3, the pulses are canceled, if at least one of the following conditions
is fulfilled:  
- The speed actual value falls below the threshold in p1226 and the time started after
this in p1228 has expired.  
- The speed setpoint falls below the threshold in p1226 and the time started after
this in p1227 has expired.

**Dependency:** 
  
See also:
p1226, p1227

**Notice:** 
  
When the motor holding brake is activated, pulse cancellation is additionally delayed
by the brake closing time (p1217).

### r1407.0...28 Status word speed controller

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Parameter group:** Torque setpoints, U/f control, Torque limiting, Speed actual value filter, Control/status words, Acceleration model, Setpoint addition, Speed precontrol, Speed setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source binary/numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the status word of the speed controller.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Reserved | No | Yes | - |
| 01 | Reserved | No | Yes | - |
| 02 | Torque control active | No | Yes | 8010 |
| 04 | Speed setpoint from DSC | No | Yes | 2522 |
| 05 | Speed controller I component frozen | No | Yes | - |
| 06 | Speed controller I component set | No | Yes | - |
| 07 | Torque limit reached | No | Yes | 5610 |
| 08 | Upper torque limit active | No | Yes | 5610 |
| 09 | Lower torque limit active | No | Yes | 5610 |
| 11 | Speed setpoint limited | No | Yes | - |
| 13 | Encoderless operation due to a fault | No | Yes | - |
| 19 | Reserved | No | Yes | 3090 |
| 20 | Reserved | No | Yes | - |
| 21 | Reserved | No | Yes | - |
| 22 | Reserved | No | Yes | - |
| 23 | Torque-speed precontrol with encoder on | No | Yes | - |
| 24 | Moment of inertia estimator active | No | Yes | - |
| 25 | Load estimate active | No | Yes | - |
| 26 | Moment of inertia estimator stabilized | No | Yes | - |
| 28 | Speed precontrol | For setp_filter 2 | For symmetrizing | - |

**Note:** 
  
For bit 01, 13:  
If, after a fault, the encoder still provides a valid commutation position (p1992.10
= 1), then a switch is not immediately made into encoderless operation. Both bits
remain at 0 for this time.  
For bit 04:  
The following conditions must be fulfilled to set to 1:  
- Connector input p1190 and p1191 must be interconnected with a signal source that
is not equal to zero.  
- OFF1, OFF3 or STOP2 must not be active.  
- It is not permissible that the motor data identification is active.  
- Master control must not be active.  
The following conditions can mean that the DSC function is not active in spite of
the fact that the bit is set:  
- Isochronous operation is not selected (r2054 not equal to 4).  
- The PROFIBUS is not isochronous (r2064[0] not equal to 1).  
- DSC is not activated on the control side, therefore KPC = 0 is transferred as value
to connector input p1191.

### p1414[0].0...1 Speed setpoint filter activation

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Speed setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| - | - | [0] 0000 bin |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Setting for activating/deactivating the speed setpoint filter.

**Recommendation:** 
  
If only one filter is required, filter 1 should be activated and filter 2 deactivated,
to avoid excessive processing time.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Activate filter 1 | No | Yes | - |
| 01 | Activate filter 2 | No | Yes | - |

**Dependency:** 
  
The individual speed setpoint filters are parameterized from p1415.

### p1415[0] Speed setpoint filter 1 type

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Speed setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 2 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the type for speed setpoint filter 1.

**Value:** 
  
0:
Low pass: PT1  
1:
Low pass: PT2  
2:
General 2nd order filter

**Dependency:** 
  
PT1 low pass: p1416  
PT2 low pass: p1417, p1418  
General filter: p1417 ... p1420

### p1416[0] Speed setpoint filter 1 time constant

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Speed setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [ms] | 5000.00 [ms] | [0] 0.00 [ms] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the time constant for the speed setpoint filter 1 (PT1).

**Dependency:** 
  
See also:
p1414, p1415

**Note:** 
  
This parameter is only effective if the filter is set as a PT1 low pass.

### p1417[0] Speed setpoint filter 1 denominator natural frequency

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Speed setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Hz | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.5 [Hz] | 16000.0 [Hz] | [0] 2000.0 [Hz] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the denominator natural frequency for speed setpoint filter 1 (PT2, general filter).

**Dependency:** 
  
See also:
p1414, p1415

**Note:** 
  
This parameter is only effective if the speed filter is parameterized as a PT2 low
pass or as general filter.  
The filter is only effective if the natural frequency is less than half of the sampling
frequency.

### p1418[0] Speed setpoint filter 1 denominator damping

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Speed setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.001 | 10.000 | [0] 0.700 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the denominator damping for speed setpoint filter 1 (PT2, general filter).

**Dependency:** 
  
See also:
p1414, p1415

**Note:** 
  
This parameter is only effective if the speed filter is parameterized as a PT2 low
pass or as general filter.

### p1419[0] Speed setpoint filter 1 numerator natural frequency

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Speed setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Hz | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.5 [Hz] | 16000.0 [Hz] | [0] 2000.0 [Hz] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the numerator natural frequency for speed setpoint filter 1 (general filter).

**Dependency:** 
  
See also:
p1414, p1415

**Note:** 
  
This parameter is only effective if the speed filter is set as a general filter.  
The filter is only effective if the natural frequency is less than half of the sampling
frequency.

### p1420[0] Speed setpoint filter 1 numerator damping

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Speed setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.000 | 10.000 | [0] 0.700 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the numerator damping for speed setpoint filter 1 (general filter).

**Dependency:** 
  
See also:
p1414, p1415

**Note:** 
  
This parameter is only effective if the speed filter is set as a general filter.

### p1421[0] Speed setpoint filter 2 type

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Speed setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 2 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the type for speed setpoint filter 2.

**Value:** 
  
0:
Low pass: PT1  
1:
Low pass: PT2  
2:
General 2nd order filter

**Dependency:** 
  
PT1 low pass: p1422  
PT2 low pass: p1423, p1424  
General filter: p1423 ... p1426

### p1422[0] Speed setpoint filter 2 time constant

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Speed setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [ms] | 5000.00 [ms] | [0] 0.00 [ms] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the time constant for the speed setpoint filter 2 (PT1).

**Dependency:** 
  
See also:
p1414, p1421

**Note:** 
  
This parameter is only effective if the speed filter is set as a PT1 low pass.

### p1423[0] Speed setpoint filter 2 denominator natural frequency

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Speed setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Hz | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.5 [Hz] | 16000.0 [Hz] | [0] 2000.0 [Hz] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the denominator natural frequency for speed setpoint filter 2 (PT2, general filter).

**Dependency:** 
  
See also:
p1414, p1421

**Note:** 
  
This parameter is only effective if the speed filter is parameterized as a PT2 low
pass or as general filter.  
The filter is only effective if the natural frequency is less than half of the sampling
frequency.

### p1424[0] Speed setpoint filter 2 denominator damping

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Speed setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.001 | 10.000 | [0] 0.700 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the denominator damping for speed setpoint filter 2 (PT2, general filter).

**Dependency:** 
  
See also:
p1414, p1421

**Note:** 
  
This parameter is only effective if the speed filter is parameterized as a PT2 low
pass or as general filter.

### p1425[0] Speed setpoint filter 2 numerator natural frequency

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Speed setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Hz | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.5 [Hz] | 16000.0 [Hz] | [0] 2000.0 [Hz] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the numerator natural frequency for speed setpoint filter 2 (general filter).

**Dependency:** 
  
See also:
p1414, p1421

**Note:** 
  
This parameter is only effective if the speed filter is set as a general filter.  
The filter is only effective if the natural frequency is less than half of the sampling
frequency.

### p1426[0] Speed setpoint filter 2 numerator damping

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Speed setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.000 | 10.000 | [0] 0.700 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the numerator damping for speed setpoint filter 2 (general filter).

**Dependency:** 
  
See also:
p1414, p1421

**Note:** 
  
This parameter is only effective if the speed filter is set as a general filter.

### p1433[0] Speed controller reference model natural frequency

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Speed controller |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Hz | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [Hz] | 8000.00 [Hz] | [0] 0.00 [Hz] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the natural frequency of a PT2 element for the reference model of the speed controller.

**Recommendation:** 
  
The reference model is finely set using p1433.

### r1438 Speed controller speed setpoint

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Parameter group:** U/f control, Speed controller |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** rpm | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2000 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the speed setpoint after setpoint limiting for the P component of the speed
controller.

### p1441[0] Actual speed smoothing time

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Speed controller, Speed actual value filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** CALC_MOD_CON |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [ms] | 50.00 [ms] | [0] 0.00 [ms] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the smoothing time constant (PT1) for the speed actual value.

**Dependency:** 
  
See also:
r0063

**Note:** 
  
The speed actual value should be smoothed for encoders with a low pulse number or
for resolvers.  
After this parameter has been changed, we recommend that the speed controller is adapted
and/or the speed controller settings checked Kp (p1460) and Tn (p1462).

### p1460[0] Speed controller P gain

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Speed controller |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** CALC_MOD_CON |
| **Unit:** Nms/rad | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.0000 [Nms/rad] | 500000000.0000 [Nms/rad] | [0] 0.3000 [Nms/rad] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the P gain of the speed controller.  
The drive determines the P gain for One Button Tuning and writes the value to p1460.  
The value can be changed.

**Dependency:** 
  
See also:
p1462

**Note:** 
  
The higher the set P gain, the faster and more unstable the control.

### p1462[0] Speed controller integral time

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Speed controller |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** CALC_MOD_CON |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [ms] | 100000.00 [ms] | [0] 10.00 [ms] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the integral time for the speed controller  
The drive determines the integral time for One Button Tuning - and writes the value
to p1462.

**Dependency:** 
  
See also:
p1460

**Note:** 
  
The shorter the integral time, the faster and more unstable the control.

### p1498[0] Load moment of inertia

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Speed controller |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** kgm² | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| - [kgm²] | - [kgm²] | [0] - [kgm²] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the load moment of inertia.  
The setting is made during commissioning while the One Button Tuning is being performed.

### p1520[0] Torque limit upper

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Torque limiting |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** CALC_MOD_LIM_REF |
| **Unit:** Nm | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2003 |
| **Min:** | **Max:** | **Factory setting:** |
| -1000000.00 [Nm] | 20000000.00 [Nm] | [0] 0.00 [Nm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Setting the upper torque limit.  
This setting is made as part of the basic commissioning.

**Dependency:** 
  
See also:
p1521, p1532, r1538, r1539

### p1521[0] Torque limit lower

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Torque limiting |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** CALC_MOD_LIM_REF |
| **Unit:** Nm | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2003 |
| **Min:** | **Max:** | **Factory setting:** |
| -20000000.00 [Nm] | 1000000.00 [Nm] | [0] 0.00 [Nm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the lower torque limit  
This setting is made as part of the basic commissioning.

**Dependency:** 
  
See also:
p1520, p1532, r1538, r1539

### p1532[0] Torque limit offset

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Torque limiting |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Nm | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2003 |
| **Min:** | **Max:** | **Factory setting:** |
| -100000.00 [Nm] | 100000.00 [Nm] | [0] 0.00 [Nm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the torque offset for the torque limit.  
The setting allows electronic weight equalization to be used for vertical axes.

**Recommendation:** 
  
The torque offset can also be used for torque precontrol or as integrator setting
value for the speed controller.

**Dependency:** 
  
See also:
p1520, p1521

**Danger:** 
  
If the offset is set higher/lower than the lower/upper torque limit, then the unloaded
drive can accelerate up to the maximum speed.

### r1538 Upper effective torque limit

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Parameter group:** Torque limiting |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Nm | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2003 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the currently effective upper torque limit.

**Note:** 
  
The value in r1538 may not exceed the value in p1520.

### r1539 Lower effective torque limit

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Parameter group:** Torque limiting |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Nm | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2003 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the currently effective lower torque limit.

**Note:** 
  
The value in r1539 may not exceed the value in p1521.

### p1558 Measure/precontrol hanging/suspended axis force due to weight

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Motor data identification routine |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| -1 | 1 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Setting to start/reset the measurement of the force due to weight for a hanging/suspended
axis.  
The measurement can be started when the pulses are inhibited or the pulses are enabled
(p1558 = 1). If it was started when the pulses were inhibited, then it is only executed
after the pulses have been enabled.  
For the measurement, the torque to hold the axis is determined and entered into p1532.  
Further, this value is used internally for the precontrol.

**Value:** 
  
-1:
Reset values  
0:
Inactive  
1:
Start measurement and activate precontrol

**Dependency:** 
  
The pulse enable is withdrawn at the end of the measurement.  
See also:
p1532

**Note:** 
  
For master control with speed setpoint input from the commissioning tool, the torque
precontrol channels are deactivated, so that the weight equalization entered here
is not active.

### r1651 Torque setpoint function generator

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Parameter group:** Current setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Nm | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2003 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the torque setpoint of the function generator.

### p1656[0].0...3 Activates current setpoint filter

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Current setpoint filter |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** CALC_MOD_CON |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| - | - | [0] 0001 bin |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Setting for activating/de-activating the current setpoint filter.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Filter 1 | Inactive | Active | - |
| 01 | Filter 2 | Inactive | Active | - |
| 02 | Filter 3 | Inactive | Active | - |
| 03 | Filter 4 | Inactive | Active | - |

**Dependency:** 
  
The individual current setpoint filters are parameterized as of p1657.

**Note:** 
  
If not all of the filters are required, then the filters should be used consecutively
starting from filter 1.

### p1657[0] Current setpoint filter 1 type

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Current setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** CALC_MOD_CON |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 1 | 2 | [0] 1 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the current setpoint filter 1 as low pass (PT2) or general 2nd-order filter.

**Value:** 
  
1:
PT2 low pass  
2:
General 2nd order filter

**Dependency:** 
  
The current setpoint filter 1 is activated via p1656.0 and parameterized via p1657
... p1661.

**Note:** 
  
For a general 2nd order filter, by inserting the same natural frequency in both the
numerator and in the denominator, i.e. bandstop frequency, a bandstop filter is implemented.
If the numerator damping of zero is selected, the bandstop frequency is completely
suppressed.  
The denominator damping can be determined from the equation for the 3 dB bandwidth:  
f_3dB bandwidth = 2 * D_denominator * f_bandstop frequency

### p1658[0] Current setpoint filter 1 denominator natural frequency

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Current setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** CALC_MOD_CON |
| **Unit:** Hz | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.5 [Hz] | 16000.0 [Hz] | [0] 1999.0 [Hz] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the denominator natural frequency for current setpoint filter 1 (PT2, general
filter).

**Dependency:** 
  
The current setpoint filter 1 is activated via p1656.0 and parameterized via p1657
... p1661.

### p1659[0] Current setpoint filter 1 denominator damping

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Current setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** CALC_MOD_CON |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.001 | 10.000 | [0] 0.700 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the denominator damping for current setpoint filter 1.

**Dependency:** 
  
The current setpoint filter 1 is activated via p1656.0 and parameterized via p1657
... p1661.

### p1660[0] Current setpoint filter 1 numerator natural frequency

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Current setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Hz | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.5 [Hz] | 16000.0 [Hz] | [0] 1999.0 [Hz] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the numerator natural frequency for current setpoint filter 1 (general filter).

**Dependency:** 
  
The current setpoint filter 1 is activated via p1656.0 and parameterized via p1657
... p1661.

### p1661[0] Current setpoint filter 1 numerator damping

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Current setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.000 | 10.000 | [0] 0.700 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the numerator damping for current setpoint filter 1.

**Dependency:** 
  
The current setpoint filter 1 is activated via p1656.0 and parameterized via p1657
... p1661.

### p1662[0] Current setpoint filter 2 type

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Current setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 1 | 2 | [0] 1 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets current setpoint filter 2 as lowpass filter (PT2) or general 2nd order filter.

**Value:** 
  
1:
PT2 low pass  
2:
General 2nd order filter

**Dependency:** 
  
Current setpoint filter 2 is activated via p1656.1 and parameterized via p1662 ...
p1666.

**Note:** 
  
For a general 2nd order filter, by inserting the same natural frequency in both the
numerator and in the denominator, i.e. bandstop frequency, a bandstop filter is implemented.
If the numerator damping of zero is selected, the bandstop frequency is completely
suppressed.  
The denominator damping can be determined from the equation for the 3 dB bandwidth:  
f_3dB bandwidth = 2 * D_denominator * f_bandstop frequency

### p1663[0] Current setpoint filter 2 denominator natural frequency

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Current setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Hz | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.5 [Hz] | 16000.0 [Hz] | [0] 1999.0 [Hz] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the denominator natural frequency for current setpoint filter 2 (PT2, general
filter).

**Dependency:** 
  
Current setpoint filter 2 is activated via p1656.1 and parameterized via p1662 ...
p1666.

### p1664[0] Current setpoint filter 2 denominator damping

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Current setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.001 | 10.000 | [0] 0.700 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the denominator damping for current setpoint filter 2.

**Dependency:** 
  
Current setpoint filter 2 is activated via p1656.1 and parameterized via p1662 ...
p1666.

### p1665[0] Current setpoint filter 2 numerator natural frequency

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Current setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Hz | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.5 [Hz] | 16000.0 [Hz] | [0] 1999.0 [Hz] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the numerator natural frequency for current setpoint filter 2 (general filter).

**Dependency:** 
  
Current setpoint filter 2 is activated via p1656.1 and parameterized via p1662 ...
p1666.

### p1666[0] Current setpoint filter 2 numerator damping

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Current setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.000 | 10.000 | [0] 0.700 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the numerator damping for current setpoint filter 2.

**Dependency:** 
  
Current setpoint filter 2 is activated via p1656.1 and parameterized via p1662 ...
p1666.

### p1667[0] Current setpoint filter 3 type

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Current setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 1 | 2 | [0] 1 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets current setpoint filter 3 as lowpass filter (PT2) or general 2nd order filter.

**Value:** 
  
1:
PT2 low pass  
2:
General 2nd order filter

**Dependency:** 
  
Current setpoint filter 3 is activated via p1656.2 and parameterized via p1667 ...
p1671.

### p1668[0] Current setpoint filter 3 denominator natural frequency

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Current setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Hz | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.5 [Hz] | 16000.0 [Hz] | [0] 1999.0 [Hz] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the denominator natural frequency for current setpoint filter 3 (PT2, general
filter).

**Dependency:** 
  
Current setpoint filter 3 is activated via p1656.2 and parameterized via p1667 ...
p1671.

### p1669[0] Current setpoint filter 3 denominator damping

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Current setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.001 | 10.000 | [0] 0.700 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the denominator damping for current setpoint filter 3.

**Dependency:** 
  
Current setpoint filter 3 is activated via p1656.2 and parameterized via p1667 ...
p1671.

### p1670[0] Current setpoint filter 3 numerator natural frequency

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Current setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Hz | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.5 [Hz] | 16000.0 [Hz] | [0] 1999.0 [Hz] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the numerator natural frequency for current setpoint filter 3 (general filter).

**Dependency:** 
  
Current setpoint filter 3 is activated via p1656.2 and parameterized via p1667 ...
p1671.

### p1671[0] Current setpoint filter 3 numerator damping

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Current setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.000 | 10.000 | [0] 0.700 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the numerator damping for current setpoint filter 3.

**Dependency:** 
  
Current setpoint filter 3 is activated via p1656.2 and parameterized via p1667 ...
p1671.

### p1672[0] Current setpoint filter 4 type

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Current setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 1 | 2 | [0] 1 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets current setpoint filter 4 as lowpass filter (PT2) or general 2nd order filter.

**Value:** 
  
1:
PT2 low pass  
2:
General 2nd order filter

**Dependency:** 
  
Current setpoint filter 4 is activated via p1656.3 and parameterized via p1672 ...
p1676.

### p1673[0] Current setpoint filter 4 denominator natural frequency

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Current setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Hz | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.5 [Hz] | 16000.0 [Hz] | [0] 1999.0 [Hz] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the denominator natural frequency for current setpoint filter 4 (PT2, general
filter).

**Dependency:** 
  
Current setpoint filter 4 is activated via p1656.3 and parameterized via p1672 ...
p1676.

### p1674[0] Current setpoint filter 4 denominator damping

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Current setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.001 | 10.000 | [0] 0.700 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the denominator damping for current setpoint filter 4.

**Dependency:** 
  
Current setpoint filter 4 is activated via p1656.3 and parameterized via p1672 ...
p1676.

### p1675[0] Current setpoint filter 4 numerator natural frequency

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Current setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Hz | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.5 [Hz] | 16000.0 [Hz] | [0] 1999.0 [Hz] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the numerator natural frequency for current setpoint filter 4 (general filter).

**Dependency:** 
  
Current setpoint filter 4 is activated via p1656.3 and parameterized via p1672 ...
p1676.

### p1676[0] Current setpoint filter 4 numerator damping

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Current setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.000 | 10.000 | [0] 0.700 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the numerator damping for current setpoint filter 4.

**Dependency:** 
  
Current setpoint filter 4 is activated via p1656.3 and parameterized via p1672 ...
p1676.

### p1703[0] Isq current controller precontrol scaling

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Current controller |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** % | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.0 [%] | 200.0 [%] | [0] 0.0 [%] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the scaling of the dynamic current controller precontrol for the torque/force-generating
current component Isq.

### p1821[0] Direction of rotation

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Motor data |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 1 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Setting to change the direction of rotation.  
If the parameter is changed, it reverses the direction of rotation of the motor and
the encoder actual value without changing the setpoint.

**Value:** 
  
0:
Clockwise  
1:
Counterclockwise

**Dependency:** 
  
See also:
F07434

**Notice:** 
  
After changing parameter p1821, the direction of rotation is not automatically adapted
in the safety area.

### p2000 Reference speed

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Reference variables |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** CALC_MOD_ALL |
| **Unit:** rpm | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 6.00 [rpm] | 210000.00 [rpm] | [0] 3000.00 [rpm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the reference quantity for the speed values.  
All speeds specified as relative values refer to this reference quantity.  
The reference quantity corresponds to 100% or 4000 hex (word) or 4000 0000 hex (double
word).

**Dependency:** 
  
See also:
p2003

### p2002 Reference current

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Reference variables |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** CALC_MOD_ALL |
| **Unit:** Arms | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.10 [Arms] | 100000.00 [Arms] | [0] 100.00 [Arms] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the reference quantity for currents.  
All currents specified as relative value are referred to this reference quantity.  
The reference quantity corresponds to 100% or 4000 hex (word) or 4000 0000 hex (double
word).

**Note:** 
  
Default value is 2 * p0305 or the motor current limit.

### p2003 Reference torque

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Reference variables |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** CALC_MOD_ALL |
| **Unit:** Nm | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.01 [Nm] | 20000000.00 [Nm] | [0] 1.00 [Nm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the reference quantity for the torque values.  
All torques specified as relative value are referred to this reference quantity.  
The reference quantity corresponds to 100% or 4000 hex (word) or 4000 0000 hex (double
word).

### r2043.0...2 PROFIdrive PZD state

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN, S200 PN |  |  |
| **Data type:**Unsigned8 | **Visible in:**Extended display |  |
| **Parameter group:** Configuration |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source binary |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the PROFIdrive PZD state.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Setpoint failure | No | Yes | - |
| 01 | Isochronous operation active | No | Yes | - |
| 02 | Fieldbus running | No | Yes | - |

**Note:** 
  
When using the "setpoint failure" signal, the bus can be monitored and an application-specific
response triggered when the setpoint fails.

### r2050[0...21].0...15 PROFIdrive PZD receive word

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN, S200 PN |  |  |
| **Data type:**Unsigned16 | **Visible in:**Standard display |  |
| **Parameter group:** Receive direction |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source binary/numeric |  | **Scaling:** 4000H |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Displays the PZD (setpoints) in the word format received from the fieldbus controller.

**Index:** 
  
[
0]:
PZD 1  
[
1]:
PZD 2  
[
2]:
PZD 3  
[
3]:
PZD 4  
[
4]:
PZD 5  
[
5]:
PZD 6  
[
6]:
PZD 7  
[
7]:
PZD 8  
[
8]:
PZD 9  
[
9]:
PZD 10  
[
10]:
PZD 11  
[
11]:
PZD 12  
[
12]:
PZD 13  
[
13]:
PZD 14  
[
14]:
PZD 15  
[
15]:
PZD 16  
[
16]:
PZD 17  
[
17]:
PZD 18  
[
18]:
PZD 19  
[
19]:
PZD 20  
[
20]:
PZD 21  
[
21]:
PZD 22

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Bit 0 | Off | On | - |
| 01 | Bit 1 | Off | On | - |
| 02 | Bit 2 | Off | On | - |
| 03 | Bit 3 | Off | On | - |
| 04 | Bit 4 | Off | On | - |
| 05 | Bit 5 | Off | On | - |
| 06 | Bit 6 | Off | On | - |
| 07 | Bit 7 | Off | On | - |
| 08 | Bit 8 | Off | On | - |
| 09 | Bit 9 | Off | On | - |
| 10 | Bit 10 | Off | On | - |
| 11 | Bit 11 | Off | On | - |
| 12 | Bit 12 | Off | On | - |
| 13 | Bit 13 | Off | On | - |
| 14 | Bit 14 | Off | On | - |
| 15 | Bit 15 | Off | On | - |

**Dependency:** 
  
See also:
r2060

### c2053[0...27] PROFIdrive PZD send word

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN, S200 PN |  |  |
| **Data type:**Unsigned16 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Send direction |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink numeric |  | **Scaling:** 4000H |
| **Factory interconnection:** | **Fixed value:** |  |
| not interconnected | 0 |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Displays the PZD (actual values) in the word format that are sent to the fieldbus
controller.

**Index:** 
  
[
0]:
PZD 1  
[
1]:
PZD 2  
[
2]:
PZD 3  
[
3]:
PZD 4  
[
4]:
PZD 5  
[
5]:
PZD 6  
[
6]:
PZD 7  
[
7]:
PZD 8  
[
8]:
PZD 9  
[
9]:
PZD 10  
[
10]:
PZD 11  
[
11]:
PZD 12  
[
12]:
PZD 13  
[
13]:
PZD 14  
[
14]:
PZD 15  
[
15]:
PZD 16  
[
16]:
PZD 17  
[
17]:
PZD 18  
[
18]:
PZD 19  
[
19]:
PZD 20  
[
20]:
PZD 21  
[
21]:
PZD 22  
[
22]:
PZD 23  
[
23]:
PZD 24  
[
24]:
PZD 25  
[
25]:
PZD 26  
[
26]:
PZD 27  
[
27]:
PZD 28

**Dependency:** 
  
See also:
c2063

### r2060[0...20] PROFIdrive PZD receive double word

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN, S200 PN |  |  |
| **Data type:**Integer32 | **Visible in:**Standard display |  |
| **Parameter group:** Receive direction |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** 4000H |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the PZD (setpoints) in the double word format received from the fieldbus
controller.

**Index:** 
  
[
0]:
PZD 1 + 2  
[
1]:
PZD 2 + 3  
[
2]:
PZD 3 + 4  
[
3]:
PZD 4 + 5  
[
4]:
PZD 5 + 6  
[
5]:
PZD 6 + 7  
[
6]:
PZD 7 + 8  
[
7]:
PZD 8 + 9  
[
8]:
PZD 9 + 10  
[
9]:
PZD 10 + 11  
[
10]:
PZD 11 + 12  
[
11]:
PZD 12 + 13  
[
12]:
PZD 13 + 14  
[
13]:
PZD 14 + 15  
[
14]:
PZD 15 + 16  
[
15]:
PZD 16 + 17  
[
16]:
PZD 17 + 18  
[
17]:
PZD 18 + 19  
[
18]:
PZD 19 + 20  
[
19]:
PZD 20 + 21  
[
20]:
PZD 21 + 22

**Dependency:** 
  
See also:
r2050

### c2063[0...26] PROFIdrive PZD send double word

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN, S200 PN |  |  |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Send direction |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink numeric |  | **Scaling:** 4000H |
| **Factory interconnection:** | **Fixed value:** |  |
| not interconnected | 0 |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Displays the PZD (actual values) in the double word format that are sent to the fieldbus
controller.

**Index:** 
  
[
0]:
PZD 1 + 2  
[
1]:
PZD 2 + 3  
[
2]:
PZD 3 + 4  
[
3]:
PZD 4 + 5  
[
4]:
PZD 5 + 6  
[
5]:
PZD 6 + 7  
[
6]:
PZD 7 + 8  
[
7]:
PZD 8 + 9  
[
8]:
PZD 9 + 10  
[
9]:
PZD 10 + 11  
[
10]:
PZD 11 + 12  
[
11]:
PZD 12 + 13  
[
12]:
PZD 13 + 14  
[
13]:
PZD 14 + 15  
[
14]:
PZD 15 + 16  
[
15]:
PZD 16 + 17  
[
16]:
PZD 17 + 18  
[
17]:
PZD 18 + 19  
[
18]:
PZD 19 + 20  
[
19]:
PZD 20 + 21  
[
20]:
PZD 21 + 22  
[
21]:
PZD 22 + 23  
[
22]:
PZD 23 + 24  
[
23]:
PZD 24 + 25  
[
24]:
PZD 25 + 26  
[
25]:
PZD 26 + 27  
[
26]:
PZD 27 + 28

**Dependency:** 
  
See also:
c2053

**Notice:** 
  
A maximum of 4 indices of the "trace" function can be used.

### c2104[0] 2nd acknowledge faults

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN, S200 PN |  |  |
| **Data type:**Unsigned8 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Faults / alarms |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink binary |  |  |
| **Factory interconnection:** | **Fixed value:** |  |
| not interconnected | 0 |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal 2 to acknowledge faults.

**Note:** 
  
A fault acknowledgment is triggered with a 0/1 signal.

### c2106[0] External fault 1

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Faults / alarms |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink binary |  |  |
| **Factory interconnection:** | **Fixed value:** |  |
| not interconnected | 1 |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal for external fault 1.

**Dependency:** 
  
See also:
F07860

**Note:** 
  
An external fault is initiated with a 1-&gt;0 edge.  
If this fault is initiated at the Control Unit, then it is transferred to all of the
drive objects available.

### r2109[0...63] Fault time removed in milliseconds

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Parameter group:** Faults / alarms |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the system runtime in milliseconds when the fault was removed.

**Dependency:** 
  
See also:
r0945, r0947, r0948, r0949, r2114, r2130, r2133, r2136, r3122

**Notice:** 
  
The time comprises r2136 (days) and r2109 (milliseconds).

**Note:** 
  
The buffer parameters are cyclically updated in the background (refer to status signal
in r2139).  
The structure of the fault buffer and the assignment of the indices is shown in r0945.

### r2111 Alarm counter

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Parameter group:** Faults / alarms |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Number of alarms that have occurred.

**Dependency:** 
  
See also:
r2122, r2123, r2124, r2125

**Note:** 
  
The parameter is reset to 0 at POWER ON.

### r2114[0...1] System runtime total

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Parameter group:** Diagnostics general |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the total system runtime of the converter.  
The time comprises r2114[0] (milliseconds) and r2114[1] (days).  
After r2114[0] has reached a value of 86.400.000 ms (24 hours) this value is reset
and r2114[1] is incremented.

**Index:** 
  
[
0]:
Milliseconds  
[
1]:
Days

**Note:** 
  
The counter values are saved when the power supply is switched off.  
After the converter is switched on, the counter continues to run with the last value
that was saved.

### r2121 Counter alarm buffer changes

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Parameter group:** Faults / alarms |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
This counter is incremented every time the alarm buffer changes.

**Dependency:** 
  
See also:
r2122, r2123, r2124, r2125

### r2122[0...63] Alarm number

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Parameter group:** Faults / alarms |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the numbers of the last 64 alarms.

**Dependency:** 
  
See also:
r2123, r2124, r2125, r2134, r2145, r2146, r3123

**Notice:** 
  
The properties of the alarm buffer should be taken from the corresponding product
documentation.

**Note:** 
  
The buffer parameters are cyclically updated in the background.  
Alarm buffer structure (general principle):  
Currently active alarms (not gone):  
r2122[0], r2124[0], r2123[0], r2125[0] --&gt; alarm 1 (the oldest)  
. . .  
r2122[7], r2124[7], r2123[7], r2125[7] --&gt; Alarm 8 (the latest)  
  
History of alarms that have gone:  
r2122[8], r2124[8], r2123[8], r2125[8] --&gt; Alarm 1 (the latest)  
. . .  
r2122[63], r2124[63], r2123[63], r2125[63] --&gt; alarm 56 (the oldest)

### r2123[0...63] Alarm time received in milliseconds

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Parameter group:** Faults / alarms |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the system runtime in milliseconds when the alarm occurred.

**Dependency:** 
  
See also:
r2114, r2122, r2124, r2125, r2134, r2145, r2146, r3123

**Notice:** 
  
The time comprises r2145 (days) and r2123 (milliseconds).

**Note:** 
  
The buffer parameters are cyclically updated in the background (refer to status signal
in r2139).  
The structure of the alarm buffer and the assignment of the indices is shown in r2122.

### r2124[0...63] Alarm value

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer32 | **Visible in:**Extended display |  |
| **Parameter group:** Faults / alarms |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays additional information about the active alarm (as integer number).

**Dependency:** 
  
See also:
r2122, r2123, r2125, r2134, r2145, r2146, r3123

**Note:** 
  
The buffer parameters are cyclically updated in the background (refer to status signal
in r2139).  
The structure of the alarm buffer and the assignment of the indices is shown in r2122.

### r2125[0...63] Alarm time removed in milliseconds

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Parameter group:** Faults / alarms |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the system runtime in milliseconds when the alarm was removed.

**Dependency:** 
  
See also:
r2114, r2122, r2123, r2124, r2134, r2145, r2146, r3123

**Notice:** 
  
The time comprises r2146 (days) and r2125 (milliseconds).

**Note:** 
  
The buffer parameters are cyclically updated in the background (refer to status signal
in r2139).  
The structure of the alarm buffer and the assignment of the indices is shown in r2122.

### r2130[0...63] Fault time received in days

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Parameter group:** Faults / alarms |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the system runtime in days when the fault occurred.

**Dependency:** 
  
See also:
r0945, r0947, r0948, r0949, r2109, r2114, r2133, r2136, r3122

**Notice:** 
  
The time comprises r2130 (days) and r0948 (milliseconds).

**Note:** 
  
The buffer parameters are cyclically updated in the background (refer to status signal
in r2139).

### r2131 Actual fault code

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Standard display |  |
| **Parameter group:** Faults / alarms |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the code of the oldest active fault.

**Note:** 
  
0: No fault present.

### r2132 Actual alarm code

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Standard display |  |
| **Parameter group:** Faults / alarms |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the code of the last alarm that occurred.

**Note:** 
  
0: No alarm present.

### r2133[0...63] Fault value for float values

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Parameter group:** Faults / alarms |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays additional information about the fault that occurred for float values.

**Dependency:** 
  
See also:
r0945, r0947, r0948, r0949, r2109, r2130, r2136

**Note:** 
  
The buffer parameters are cyclically updated in the background (refer to status signal
in r2139).

### r2134[0...63] Alarm value for float values

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Parameter group:** Faults / alarms |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays additional information about the active alarm for float values.

**Dependency:** 
  
See also:
r2122, r2123, r2124, r2125, r2145, r2146, r3123

**Note:** 
  
The buffer parameters are cyclically updated in the background (refer to status signal
in r2139).

### r2136[0...63] Fault time removed in days

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Parameter group:** Faults / alarms |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the system runtime in days when the fault was removed.

**Dependency:** 
  
See also:
r0945, r0947, r0948, r0949, r2109, r2114, r2130, r2133, r3122

**Notice:** 
  
The time comprises r2136 (days) and r2109 (milliseconds).

**Note:** 
  
The buffer parameters are cyclically updated in the background (refer to status signal
in r2139).

### r2139.0...15 Status word faults/alarms 1

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Parameter group:** Faults / alarms |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source binary/numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays status word 1 of faults and alarms.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Being acknowledged | No | Yes | - |
| 01 | Acknowledgment required | No | Yes | - |
| 03 | Fault present | No | Yes | 8060 |
| 05 | Safety message present | No | Yes | - |
| 07 | Alarm present | No | Yes | 8065 |
| 11 | Alarm class bit 0 | Low | High | - |
| 12 | Alarm class bit 1 | Low | High | - |
| 13 | Maintenance required | No | Yes | - |
| 14 | Maintenance urgently required | No | Yes | - |
| 15 | Fault gone/can be acknowledged | No | Yes | - |

**Note:** 
  
For bit 03, 05, 07:  
These bits are set if at least one fault/alarm or safety message occurs. The entry
in the fault/alarm buffer or safety message buffer is delayed. This is the reason
that the fault/alarm buffer or safety message buffer should only be read if, after
"Fault active", "Alarm active" or "Safety message active" occurs, a change is also
identified in the buffer (r0944, r2121, r60044).  
For bits 11, 12:  
These status bits are used for the classification of internal alarm classes and are
intended for diagnostic purposes only on certain automation systems with integrated
SINAMICS functionality.

### r2145[0...63] Alarm time received in days

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Parameter group:** Faults / alarms |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the system runtime in days when the alarm occurred.

**Dependency:** 
  
See also:
r2114, r2122, r2123, r2124, r2125, r2134, r2146, r3123

**Notice:** 
  
The time comprises r2145 (days) and r2123 (milliseconds).

**Note:** 
  
The buffer parameters are cyclically updated in the background (refer to status signal
in r2139).

### r2146[0...63] Alarm time cleared in days

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Parameter group:** Faults / alarms |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the system runtime in days when the alarm was cleared.

**Dependency:** 
  
See also:
r2114, r2122, r2123, r2124, r2125, r2134, r2145, r3123

**Notice:** 
  
The time comprises r2146 (days) and r2125 (milliseconds).

**Note:** 
  
The buffer parameters are cyclically updated in the background (refer to status signal
in r2139).

### p2149[0].16 Monitoring configuration

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Speed messages, Load torque monitoring |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| - | - | [0] 0000 0000 0000 0001 0000 0000 0000 0000 bin |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the configuration for messages and monitoring functions.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 16 | Line voltage failure detection | No | Yes | - |

**Note:** 
  
For bit 16:  
When the bit is set, the line voltage failure detection function is activated

### p2153[0] Speed actual value filter time constant

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Speed messages |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 [ms] | 1000000 [ms] | [0] 0 [ms] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the time constant of the PT1 element to smooth the speed / velocity actual value.  
The smoothed actual speed/velocity is compared with the threshold values and is only
used for messages and signals.

### p2161[0] Speed threshold 3

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Speed messages |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** CALC_MOD_LIM_REF |
| **Unit:** rpm | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [rpm] | 210000.00 [rpm] | [0] 5.00 [rpm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the speed threshold value for signal "|n_act| &lt; speed threshold 3".

**Dependency:** 
  
See also:
r2199

### p2162[0] Hysteresis speed n_act > n_max

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Speed messages |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** CALC_MOD_LIM_REF |
| **Unit:** rpm | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [rpm] | 60000.00 [rpm] | [0] 0.00 [rpm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the hysteresis speed (bandwidth) for signal "n_act &gt; n_max".

**Notice:** 
  
For p0322 = 0, the following applies: p2162 &lt;= 0.1 * p0311  
For p0322 &gt; 0, the following applies: p2162 &lt;= 1.02 * p0322 - p1082  
If one of the conditions is violated, p2162 is appropriately and automatically reduced
when exiting the commissioning mode.

**Note:** 
  
For a negative speed limit, the hysteresis is effective below the limit value and
for a positive speed limit, above the limit value.  
If significant overshoot occurs in the maximum speed range (e.g. due to load shedding),
you are advised to increase the dynamic response of the speed controller (if possible).
If this is insufficient, the hysteresis p2162 can only be increased by more than 10%
of the rated speed when the maximum speed (p0322) of the motor is sufficiently greater
than the speed limit p1082.

### p2175[0] Motor blocked speed threshold

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Speed messages |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** CALC_MOD_LIM_REF |
| **Unit:** rpm | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [rpm] | 210000.00 [rpm] | [0] 120.00 [rpm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the speed threshold for message "Motor blocked".  
Monitoring is deactivated with p2175 = 0.

**Dependency:** 
  
See also:
p2177  
See also:
F07900

**Note:** 
  
If the motor speed is less than the threshold value set in p2175 - and the motor is
operated for longer than 200 ms at the torque limit - then the motor is shut down
and a fault is output.

### p2177[0] Motor blocked delay time

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Speed messages |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** CALC_MOD_LIM_REF |
| **Unit:** s | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.000 [s] | 65.000 [s] | [0] 1.000 [s] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the delay time for the message "Motor blocked".

**Dependency:** 
  
See also:
p2175  
See also:
F07900

### r2199.0...11 Status word monitoring 3

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Parameter group:** Speed messages, Control/status words |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source binary/numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the third status word of the monitoring functions.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | |n_act| &lt; p2161 | No | Yes | 8010 |
| 01 | f or n comparison value reached or exceeded | No | Yes | 8010 |
| 04 | Speed setpoint - actual value deviation in tolerance t_on | No | Yes | 8011 |
| 05 | Ramp-up/ramp-down completed | No | Yes | 8011 |
| 11 | Torque utilization &lt; torque threshold value 2 | No | Yes | 8012 |

**Note:** 
  
For bit 00:  
The speed threshold 3 is set in p2161.  
For bit 01:  
The comparison value is set in p2141. We recommend setting the hysteresis (p2142)
for canceling the bit to a value lower than that in p2141. Otherwise, the bit is not
reset.  
For bit 11:  
The torque threshold value 2 is set in p2194.

### p2496 LR dimension system physical length units

[S200 Basic PN](#p2496-lr-dimension-system-physical-length-units-1)

[S200 Basic PN EPOS load side, rotating](#p2496-lr-dimension-system-physical-length-units-2)

#### p2496 LR dimension system physical length units

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Position control |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 8 | [0] 3 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the physical length units.

**Value:** 
  
0:
LU (no dimension)  
1:
km  
2:
m  
3:
mm  
4:
µm  
5:
nm  
6:
in  
7:
ft  
8:
mi

**Note:** 
  
This parameter is only of significance for visualization (e.g. using the commissioning
tool).  
Internally in the drive, the neutral length unit (LU) without dimensions is used for
calculations.

#### p2496 LR dimension system physical length units

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN (EPOS load side, rotating), S200 Basic PTI (EPOS load side, rotating), S200 PN (EPOS load side, rotating), S200 PTI (EPOS load side, rotating) |  |  |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Position control |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 10 | [0] 10 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the physical length units.

**Value:** 
  
0:
LU (no dimension)  
10:
°

**Note:** 
  
This parameter is only of significance for visualization (e.g. using the commissioning
tool).  
Internally in the drive, the neutral length unit (LU) without dimensions is used for
calculations.

### p2497 LR dimension system physical velocity

[S200 Basic PN](#p2497-lr-dimension-system-physical-velocity-1)

[S200 Basic PN EPOS load side, rotating](#p2497-lr-dimension-system-physical-velocity-2)

#### p2497 LR dimension system physical velocity

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Position control, Mechanics |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 15 | [0] 8 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the physical unit for the velocities.

**Value:** 
  
0:
1000LU/min (no dimension)  
1:
km/h  
2:
km/min  
3:
m/h  
4:
m/min  
5:
m/s  
6:
mm/h  
7:
mm/min  
8:
mm/s  
11:
in/min  
12:
in/s  
13:
ft/min  
14:
ft/s  
15:
mi/h

#### p2497 LR dimension system physical velocity

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN (EPOS load side, rotating), S200 Basic PTI (EPOS load side, rotating), S200 PN (EPOS load side, rotating), S200 PTI (EPOS load side, rotating) |  |  |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Position control, Mechanics |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 18 | [0] 18 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the physical unit for the velocities.

**Value:** 
  
0:
1000LU/min (no dimension)  
18:
°/s

### p2498 LR dimension system physical acceleration

[S200 Basic PN](#p2498-lr-dimension-system-physical-acceleration-1)

[S200 Basic PN EPOS load side, rotating](#p2498-lr-dimension-system-physical-acceleration-2)

#### p2498 LR dimension system physical acceleration

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Position control, Mechanics |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 11 | [0] 7 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the physical unit for the accelerations.

**Value:** 
  
0:
1000LU/s² (no dimension)  
6:
m/s²  
7:
mm/s²  
10:
in/s²  
11:
ft/s²

#### p2498 LR dimension system physical acceleration

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN (EPOS load side, rotating), S200 Basic PTI (EPOS load side, rotating), S200 PN (EPOS load side, rotating), S200 PTI (EPOS load side, rotating) |  |  |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Position control, Mechanics |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 18 | [0] 18 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the physical unit for the accelerations.

**Value:** 
  
0:
1000LU/s² (no dimension)  
18:
°/s²

### p2499 LR dimension system physical jerk

[S200 Basic PN](#p2499-lr-dimension-system-physical-jerk-1)

[S200 Basic PN EPOS load side, rotating](#p2499-lr-dimension-system-physical-jerk-2)

#### p2499 LR dimension system physical jerk

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Position control, Mechanics |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 11 | [0] 7 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the physical unit für jerk.

**Value:** 
  
0:
1000LU/s³ (no dimension)  
7:
mm/s³  
10:
in/s³  
11:
ft/s³

#### p2499 LR dimension system physical jerk

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN (EPOS load side, rotating), S200 Basic PTI (EPOS load side, rotating), S200 PN (EPOS load side, rotating), S200 PTI (EPOS load side, rotating) |  |  |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Position control, Mechanics |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 18 | [0] 18 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the physical unit für jerk.

**Value:** 
  
0:
1000LU/s³ (no dimension)  
18:
°/s³

### p2502[0] LR encoder assignment

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Mechanics, Actual position value preprocessing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 1 | [0] 1 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Setting to assign the encoder.  
The actual value preprocessing and the closed-loop position control are carried out
using the assigned encoder.

**Value:** 
  
0:
No encoder  
1:
Motor encoder

**Notice:** 
  
For the setting p2502 = 0 (no encoder), closed-loop position control is not possible.
This setting is only practical as supportive measure to implement encoderless closed-loop
speed control (e.g. if the motor encoder is defective).

**Note:** 
  
An encoder data set must be assigned to the assigned encoder (p2502 = 1, 2, 3).

## SINAMICS Parameter S200 Basic PN 02503 - 02605

SINAMICS Parameter S200 Basic PN 02503 - 02605

### p2503[0] LR length unit MU per 10 mm

[S200 Basic PN](#p25030-lr-length-unit-mu-per-10-mm-1)

[S200 Basic PN EPOS load side, rotating](#p25030-lr-length-unit-mu-per-10-mm-2)

#### p2503[0] LR length unit MU per 10 mm

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Position control |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.000001 [mm] | 2147483650.000000 [mm] | [0] 10.000000 [mm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the length unit MU per 10 mm set by the user.  
For a linear scale, this establishes a reference between the physical arrangement
and the neutral length units LU used in the drive.  
Example, linear scale:  
p2503 = 10000 means: 10 mm should be resolved to µm (this means that 1 LU = 1 µm).

**Note:** 
  
When selecting a physical length unit, the drive automatically preassigns the parameter
and it cannot be changed.  
The assignment to the grid spacing can be achieved using this for a rotary axis with
linear encoder.  
MU: measurement unit

#### p2503[0] LR length unit MU per 10 mm

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN (EPOS load side, rotating), S200 Basic PTI (EPOS load side, rotating), S200 PN (EPOS load side, rotating), S200 PTI (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Position control |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.000001 [°] | 2147483650.000000 [°] | [0] 10.000000 [°] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the length unit MU per 10 mm set by the user.  
For a linear scale, this establishes a reference between the physical arrangement
and the neutral length units LU used in the drive.  
Example, linear scale:  
p2503 = 10000 means: 10 mm should be resolved to µm (this means that 1 LU = 1 µm).

**Note:** 
  
When selecting a physical length unit, the drive automatically preassigns the parameter
and it cannot be changed.  
The assignment to the grid spacing can be achieved using this for a rotary axis with
linear encoder.  
MU: measurement unit

### p2504[0] LR motor/load motor revolutions

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Position control, Mechanics |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 1 | 1048576 | [0] 1 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the motor revolutions for the gearbox factor between the motor shaft and load
shaft.  
Gearbox factor = motor revolutions (p2504) / load revolutions (p2505)

**Dependency:** 
  
See also:
p2505

### p2505[0] LR motor/load load revolutions

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Position control, Mechanics |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| -1048576 | 1048576 | [0] 1 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the load revolutions for the gearbox factor between the motor shaft and load
shaft.  
Gearbox factor = motor revolutions (p2504) / load revolutions (p2505)

**Dependency:** 
  
See also:
p2504

### p2506[0] LR length unit MU per load distance

[S200 Basic PN](#p25060-lr-length-unit-mu-per-load-distance-1)

[S200 Basic PN EPOS load side, rotating](#p25060-lr-length-unit-mu-per-load-revolution)

#### p2506[0] LR length unit MU per load distance

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Position control, Mechanics |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.000001 [mm] | 2147483650.000000 [mm] | [0] 10.000000 [mm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the length unit MU per load distance set by the user.  
For a rotary encoder, this establishes a reference between the actual physical situation
and the user-specific length unit MU.  
Example:  
Rotary encoder, ballscrew with 10 mm/revolution, 10 mm should be broken down to units
of µm.  
Length unit LU (p2496 = 0)  
--&gt; One load distance corresponds to 10000 LU (i.e. 1 LU = 1 µm)  
--&gt; p2506 = 10000  
  
Physical unit µm (2496) = 4  
--&gt; One load distance corresponds to 10000 µm  
--&gt; p2506 = 10000

**Dependency:** 
  
See also:
p2496

#### p2506[0] LR length unit MU per load revolution

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN (EPOS load side, rotating), S200 Basic PTI (EPOS load side, rotating), S200 PN (EPOS load side, rotating), S200 PTI (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Position control, Mechanics |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.000001 [°] | 2147483650.000000 [°] | [0] 360.000000 [°] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the rotary unit MU per load revolution set by the user. For a rotary encoder,
this establishes a reference between the physical arrangement and the user-specific
rotating unit MU.  
Example:  
Rotating unit LU (p2496 = 0)  
Rotary encoder, 1 revolution should be broken down into mdegrees, (i.e. 1 LU = 1 mdegrees).  
--&gt; One load revolution corresponds to 360000 LU  
--&gt; p2506 = 360000

**Dependency:** 
  
See also:
p2496

**Note:** 
  
When selecting a physical length unit, the drive automatically preassigns the parameter
and it cannot be changed.

### p2507[0] LR absolute encoder adjustment status

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Position control |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 3 | [0] 1 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Activates the adjustment and display of the status of the adjustment for absolute
encoders.  
For p2507 = 2:  
This initiates encoder adjustment. The status is displayed using the other values.

**Value:** 
  
0:
Error occurred while adjusting  
1:
Absolute encoder not adjusted  
2:
Absolute encoder not adjusted and encoder adjustment initiated  
3:
Absolute encoder adjusted

**Dependency:** 
  
See also:
c2598, p2599, c11500

**Caution:** 
  
For rotating absolute encoders, when adjusting, a range is set up symmetrically around
zero with half of the encoder range, within which the position must be re-established
after switch-off/switch-on. In this range, it is only permissible that the encoder
overflows.  
After the adjustment has been completed, it must be guaranteed that the range is not
exited. The reason for this is that outside the range, there is no clear reference
any longer between the encoder actual value and mechanical system.  
If the home position (c2598) lies in this range, then the position actual value is
set when adjusting to the home position. Otherwise, adjustment is canceled with F07443.  
There is no overflow for linear absolute encoders. This means that after the adjustment,
the position can be re-established in the complete traversing range after switch-off/switch-on.
When adjusting, the position actual value is set to the home position.

**Note:** 
  
To permanently accept the determined position offset, it must be retentively saved
(p0977).  
This adjustment can only be initiated for an absolute encoder.

### c2510[0...3] LR selecting measuring probe evaluation

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Homing, Traversing blocks, Position control |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink binary |  |  |
| **Factory interconnection:** | **Fixed value:** |  |
| not interconnected | 0 |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal to select the measuring probe.  
0 signal, measuring probe 1 is used.  
1 signal, measuring probe 2 is used.

**Index:** 
  
[
0]:
Position control  
[
1]:
Motor encoder  
[
2]:
Reserved  
[
3]:
Reserved

**Dependency:** 
  
See also:
p2502, c2511

**Note:** 
  
When function "Basic positioner" is activated, the measuring probe is selected at
the 0/1 edge at r2684.1 (passive homing active).

### c2511[0...3] LR measuring probe evaluation edge

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Homing, Traversing blocks, Position control |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink binary |  |  |
| **Factory interconnection:** | **Fixed value:** |  |
| not interconnected | 0 |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal to evaluate the measuring probe edge.  
1 signal:  
The falling edge of the measuring probe (c2510) is used.  
0 signal:  
The rising edge of the measuring probe (c2510) is used.

**Index:** 
  
[
0]:
Position control  
[
1]:
Motor encoder  
[
2]:
Reserved  
[
3]:
Reserved

**Dependency:** 
  
See also:
p2502, c2510

### r2521[0...3] LR position actual value

[S200 Basic PN](#r252103-lr-position-actual-value-1)

[S200 Basic PN EPOS load side, rotating](#r252103-lr-position-actual-value-2)

#### r2521[0...3] LR position actual value

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Parameter group:** Jog, Homing, Traversing blocks, Direct setpoint input (MDI), Actual position value preprocessing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Display for the position actual value determined by the position actual value processing.

**Index:** 
  
[
0]:
Position control  
[
1]:
Motor encoder  
[
2]:
Reserved  
[
3]:
Reserved

**Dependency:** 
  
See also:
p2502, r2526

**Note:** 
  
r2526.0 = 1 --&gt; The position actual value in r2521[0] for the position control is
valid.

#### r2521[0...3] LR position actual value

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN (EPOS load side, rotating), S200 Basic PTI (EPOS load side, rotating), S200 PN (EPOS load side, rotating), S200 PTI (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Parameter group:** Jog, Homing, Traversing blocks, Direct setpoint input (MDI), Actual position value preprocessing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Display for the position actual value determined by the position actual value processing.

**Index:** 
  
[
0]:
Position control  
[
1]:
Motor encoder  
[
2]:
Reserved  
[
3]:
Reserved

**Dependency:** 
  
See also:
p2502, r2526

**Note:** 
  
r2526.0 = 1 --&gt; The position actual value in r2521[0] for the position control is
valid.

### r2522[0...3] LR velocity actual value

[S200 Basic PN](#r252203-lr-velocity-actual-value-1)

[S200 Basic PN EPOS load side, rotating](#r252203-lr-velocity-actual-value-2)

#### r2522[0...3] LR velocity actual value

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Parameter group:** Jog, Homing, Traversing blocks, Direct setpoint input (MDI), Actual position value preprocessing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm/s | **Unit group:** 11_3 | **Unit selection:** p2497 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Display for the velocity actual value determined by the position actual value processing.

**Index:** 
  
[
0]:
Position control  
[
1]:
Motor encoder  
[
2]:
Reserved  
[
3]:
Reserved

**Dependency:** 
  
See also:
p2502, r2526

**Note:** 
  
r2526.0 = 1 --&gt; The velocity actual value in r2522[0] for the position control is
valid.

#### r2522[0...3] LR velocity actual value

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN (EPOS load side, rotating), S200 Basic PTI (EPOS load side, rotating), S200 PN (EPOS load side, rotating), S200 PTI (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Parameter group:** Jog, Homing, Traversing blocks, Direct setpoint input (MDI), Actual position value preprocessing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** °/s | **Unit group:** 11_4 | **Unit selection:** p2497 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Display for the velocity actual value determined by the position actual value processing.

**Index:** 
  
[
0]:
Position control  
[
1]:
Motor encoder  
[
2]:
Reserved  
[
3]:
Reserved

**Dependency:** 
  
See also:
p2502, r2526

**Note:** 
  
r2526.0 = 1 --&gt; The velocity actual value in r2522[0] for the position control is
valid.

### r2523[0...3] LR measured value

[S200 Basic PN](#r252303-lr-measured-value-1)

[S200 Basic PN EPOS load side, rotating](#r252303-lr-measured-value-2)

#### r2523[0...3] LR measured value

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Parameter group:** Position control |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the measured values that were determined using functions "Homing mark search"
and "Measuring probe evaluation".

**Index:** 
  
[
0]:
Position control  
[
1]:
Motor encoder  
[
2]:
Reserved  
[
3]:
Reserved

**Dependency:** 
  
See also:
p2502, r2526

**Note:** 
  
r2526.2 = 1 --&gt; The measured value in r2523[0] for the position control is valid.

#### r2523[0...3] LR measured value

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN (EPOS load side, rotating), S200 Basic PTI (EPOS load side, rotating), S200 PN (EPOS load side, rotating), S200 PTI (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Parameter group:** Position control |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the measured values that were determined using functions "Homing mark search"
and "Measuring probe evaluation".

**Index:** 
  
[
0]:
Position control  
[
1]:
Motor encoder  
[
2]:
Reserved  
[
3]:
Reserved

**Dependency:** 
  
See also:
p2502, r2526

**Note:** 
  
r2526.2 = 1 --&gt; The measured value in r2523[0] for the position control is valid.

### r2526.0...12 LR status word

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Standard display |  |
| **Parameter group:** Actual position value preprocessing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source binary/numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the status word of the position controller.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Position actual value valid | No | Yes | 4010, 4015 |
| 01 | Homing active | No | Yes | 4010 |
| 02 | Measured value valid | No | Yes | 3615, 4010 |
| 03 | Position control active | No | Yes | 4015 |
| 04 | Fixed stop reached | No | Yes | 3617, 4025 |
| 05 | Fixed stop outside window | No | Yes | 3617, 4025 |
| 06 | Position controller output limited | No | Yes | 4015 |
| 07 | Request tracking mode | No | Yes | - |
| 08 | Clamping active when traveling to fixed stop | No | Yes | 4025 |
| 09 | Setting value for adjustment valid | No | Yes | - |
| 10 | Absolute encoder adjusted | No | Yes | - |
| 11 | Absolute encoder adjustment unsuccessful | No | Yes | - |
| 12 | Absolute encoder being adjusted | No | Yes | - |

**Dependency:** 
  
See also:
r2521, r2522, r2523

**Note:** 
  
For bit 04:  
The signal is influenced via p2634.  
For bit 05:  
The signal is influenced via p2635.

### c2530 LR position setpoint

[S200 Basic PN](#c2530-lr-position-setpoint-1)

[S200 Basic PN EPOS load side, rotating](#c2530-lr-position-setpoint-2)

#### c2530 LR position setpoint

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Position controller |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Sink numeric |  | **Scaling:** - |
| **Factory interconnection:** | **Fixed value:** |  |
| 2665 | 0.00 [mm] |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal for the position setpoint of the position controller.

**Dependency:** 
  
See also:
r2665

#### c2530 LR position setpoint

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN (EPOS load side, rotating), S200 Basic PTI (EPOS load side, rotating), S200 PN (EPOS load side, rotating), S200 PTI (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Position controller |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Sink numeric |  | **Scaling:** - |
| **Factory interconnection:** | **Fixed value:** |  |
| 2665 | 0.00 [°] |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal for the position setpoint of the position controller.

**Dependency:** 
  
See also:
r2665

### c2531 LR velocity setpoint

[S200 Basic PN](#c2531-lr-velocity-setpoint-1)

[S200 Basic PN EPOS load side, rotating](#c2531-lr-velocity-setpoint-2)

#### c2531 LR velocity setpoint

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Position controller |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm/s | **Unit group:** 11_3 | **Unit selection:** p2497 |
| **Type of signal interconnection:** Sink numeric |  | **Scaling:** - |
| **Factory interconnection:** | **Fixed value:** |  |
| 2666 | 0.00 [mm/s] |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal for the velocity setpoint of the position controller.

**Dependency:** 
  
See also:
r2666

#### c2531 LR velocity setpoint

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN (EPOS load side, rotating), S200 Basic PTI (EPOS load side, rotating), S200 PN (EPOS load side, rotating), S200 PTI (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Position controller |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** °/s | **Unit group:** 11_4 | **Unit selection:** p2497 |
| **Type of signal interconnection:** Sink numeric |  | **Scaling:** - |
| **Factory interconnection:** | **Fixed value:** |  |
| 2666 | 0.00 [°/s] |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal for the velocity setpoint of the position controller.

**Dependency:** 
  
See also:
r2666

### p2533[0] LR position setpoint filter time constant

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Position controller |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [ms] | 1000.00 [ms] | [0] 0.00 [ms] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the time constant for the position setpoint filter (PT1).

**Note:** 
  
The effective Kv factor (position loop gain) is reduced with the filter. This allows
a softer control behavior with improved tolerance with respect to noise/disturbances.  
Applications:  
- reduces the precontrol dynamic response.  
- jerk limiting.

### p2534[0] LR speed precontrol factor

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Position controller |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** % | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [%] | 200.00 [%] | [0] 0.00 [%] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Setting for activation and weighting of the speed precontrol value.  
Value = 0 % --&gt; The precontrol is deactivated.

**Dependency:** 
  
See also:
p2535, p2536, r2563

**Note:** 
  
When the axis control loop is optimally set as well as a precisely determined equivalent
time constant of the speed control loop, the precontrol factor is 100%.

### p2535[0] LR speed precontrol symmetrizing filter dead time

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Position controller |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 | 2.00 | [0] 0.00 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the "fractional" dead time to emulate the timing behavior of the speed control
loop.  
The selected multiplier refers to the position controller sampling time (dead time=
p2535 * position controller clock cycle).

**Dependency:** 
  
See also:
p2536

**Notice:** 
  
When speed precontrol is active (p2534 &gt; 0 %), the following applies:  
In addition to the set dead time (p2535), internally two position controller sampling
times are effective.  
When speed precontrol is inactive (p2534 = 0 %), the following applies:  
No dead time is effective (p2535 and internal).

**Note:** 
  
Together with p2536, the time response of the closed speed control loop can be emulated.

### p2536[0] LR speed precontrol symmetrizing filter PT1

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Position controller |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [ms] | 100.00 [ms] | [0] 0.00 [ms] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets a PT1 filter to emulate the time response of the closed speed control loop.

**Dependency:** 
  
See also:
p2535

**Notice:** 
  
When speed precontrol is inactive (p2534 = 0 %), the following applies:  
If a PT1 filter has been set, it is not effective.

**Note:** 
  
Together with p2535, the time response of the closed speed control loop can be emulated.

### p2538[0] LR proportional gain

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Position controller |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** 1000 rpm | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.000 [1000 rpm] | 300.000 [1000 rpm] | [0] 1.000 [1000 rpm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the proportional gain (P gain, position loop gain, Kv factor) of the position
controller.

**Dependency:** 
  
See also:
p2539, r2557, r2558

**Note:** 
  
The proportional gain is used define at which traversing velocity which following
error is obtained (without precontrol)  
Low proportional gain:  
Slow response to a setpoint - actual value difference, the following error becomes
large.  
High proportional gain:  
Fast response to the setpoint - actual value difference, the following error becomes
small.

### p2539[0] LR integral time

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Position controller |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [ms] | 100000.00 [ms] | [0] 0.00 [ms] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Setting to activate the integral time of the position controller.  
Value = 0 ms --&gt; The I component of the position controller is deactivated.

**Dependency:** 
  
See also:
p2538, r2559

### p2540 LR position controller output speed limit

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Position controller |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** rpm | **Unit group:** 3_1 | **Unit selection:** p0505 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2000 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.000 [rpm] | 210000.000 [rpm] | [0] 210000.000 [rpm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the speed limit of the position controller output.

**Dependency:** 
  
See also:
c2541

### c2541 LR position controller output speed limit signal

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Position controller |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** rpm | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink numeric |  | **Scaling:** p2000 |
| **Factory interconnection:** | **Fixed value:** |  |
| 2540 | 0.00 [rpm] |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal for limiting the position controller output.

**Dependency:** 
  
See also:
p2540

### p2542 LR standstill window

[S200 Basic PN](#p2542-lr-standstill-window-1)

[S200 Basic PN EPOS load side, rotating](#p2542-lr-standstill-window-2)

#### p2542 LR standstill window

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Position controller monitoring |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.0000 [mm] | 2147483904.0000 [mm] | [0] 0.2500 [mm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the standstill window for the standstill monitoring function.  
After the standstill monitoring time expires, it is cyclically checked whether the
difference between the setpoint and actual position is located within the standstill
window and, if required, an appropriate fault is output.  
Value = 0 --&gt; The standstill monitoring is deactivated.

**Dependency:** 
  
See also:
p2543, p2544

**Note:** 
  
The following applies for the setting of the standstill window and positioning window:  
Standstill window (p2542) &gt;= positioning window (p2544)

#### p2542 LR standstill window

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN (EPOS load side, rotating), S200 Basic PTI (EPOS load side, rotating), S200 PN (EPOS load side, rotating), S200 PTI (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Position controller monitoring |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.0000 [°] | 2147483904.0000 [°] | [0] 10.0000 [°] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the standstill window for the standstill monitoring function.  
After the standstill monitoring time expires, it is cyclically checked whether the
difference between the setpoint and actual position is located within the standstill
window and, if required, an appropriate fault is output.  
Value = 0 --&gt; The standstill monitoring is deactivated.

**Dependency:** 
  
See also:
p2543, p2544

**Note:** 
  
The following applies for the setting of the standstill window and positioning window:  
Standstill window (p2542) &gt;= positioning window (p2544)

### p2543 LR standstill monitoring time

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Position controller monitoring |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [ms] | 100000.00 [ms] | [0] 200.00 [ms] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the standstill monitoring time for the standstill monitoring function.  
After the standstill monitoring time expires, it is cyclically checked whether the
difference between the setpoint and actual position is located within the standstill
window and, if required, an appropriate fault is output.

**Dependency:** 
  
See also:
p2542, p2545

**Note:** 
  
The following applies for the setting of the standstill and positioning monitoring
time:  
Standstill monitoring time (p2543) &lt;= positioning monitoring time (p2545)

### p2544 LR positioning window

[S200 Basic PN](#p2544-lr-positioning-window-1)

[S200 Basic PN EPOS load side, rotating](#p2544-lr-positioning-window-2)

#### p2544 LR positioning window

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Position controller monitoring |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.0000 [mm] | 2147483904.0000 [mm] | [0] 0.0500 [mm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the positioning window for the positioning monitoring function.  
After the positioning monitoring time expires, it is checked once as to whether the
difference between the setpoint and actual position lies within the positioning window
and if required an appropriate fault is output.  
Value = 0 --&gt; The positioning monitoring function is deactivated.

**Dependency:** 
  
See also:
p2542, p2545, r2684

**Note:** 
  
The following applies for the setting of the standstill and positioning window:  
Standstill window (p2542) &gt;= positioning window (p2544)

#### p2544 LR positioning window

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN (EPOS load side, rotating), S200 Basic PTI (EPOS load side, rotating), S200 PN (EPOS load side, rotating), S200 PTI (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Position controller monitoring |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.0000 [°] | 2147483904.0000 [°] | [0] 2.0000 [°] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the positioning window for the positioning monitoring function.  
After the positioning monitoring time expires, it is checked once as to whether the
difference between the setpoint and actual position lies within the positioning window
and if required an appropriate fault is output.  
Value = 0 --&gt; The positioning monitoring function is deactivated.

**Dependency:** 
  
See also:
p2542, p2545, r2684

**Note:** 
  
The following applies for the setting of the standstill and positioning window:  
Standstill window (p2542) &gt;= positioning window (p2544)

### p2545 LR positioning monitoring time

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Position controller monitoring |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [ms] | 100000.00 [ms] | [0] 1000.00 [ms] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the positioning monitoring time for the positioning monitoring.  
After the positioning monitoring time expires, it is checked once as to whether the
difference between the setpoint and actual position lies within the positioning window
and if required an appropriate fault is output.

**Dependency:** 
  
See also:
p2543, p2544, r2684

**Note:** 
  
The following applies for the setting of the standstill and positioning monitoring
time:  
Standstill monitoring time (p2543) &lt;= positioning monitoring time (p2545)

### p2546[0] LR dynamic following error monitoring tolerance

[S200 Basic PN](#p25460-lr-dynamic-following-error-monitoring-tolerance-1)

[S200 Basic PN EPOS load side, rotating](#p25460-lr-dynamic-following-error-monitoring-tolerance-2)

#### p2546[0] LR dynamic following error monitoring tolerance

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Position controller monitoring |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.0000 [mm] | 2147483904.0000 [mm] | [0] 1.0000 [mm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the tolerance for the dynamic following error monitoring.  
If the dynamic following error (r2563) exceeds the selected tolerance, then an appropriate
fault is output.  
Value = 0 --&gt; The dynamic following error monitoring is deactivated.

**Dependency:** 
  
See also:
r2563, r2684

**Note:** 
  
The tolerance bandwidth is intended to prevent the dynamic following error monitoring
incorrectly responding due to operational control sequences (e.g. during load surges).

#### p2546[0] LR dynamic following error monitoring tolerance

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN (EPOS load side, rotating), S200 Basic PTI (EPOS load side, rotating), S200 PN (EPOS load side, rotating), S200 PTI (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Position controller monitoring |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.0000 [°] | 2147483904.0000 [°] | [0] 36.0000 [°] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the tolerance for the dynamic following error monitoring.  
If the dynamic following error (r2563) exceeds the selected tolerance, then an appropriate
fault is output.  
Value = 0 --&gt; The dynamic following error monitoring is deactivated.

**Dependency:** 
  
See also:
r2563, r2684

**Note:** 
  
The tolerance bandwidth is intended to prevent the dynamic following error monitoring
incorrectly responding due to operational control sequences (e.g. during load surges).

### r2556 LR position setpoint after setpoint smoothing

[S200 Basic PN](#r2556-lr-position-setpoint-after-setpoint-smoothing-1)

[S200 Basic PN EPOS load side, rotating](#r2556-lr-position-setpoint-after-setpoint-smoothing-2)

#### r2556 LR position setpoint after setpoint smoothing

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Parameter group:** Position controller |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the position setpoint after the setpoint smoothing.

#### r2556 LR position setpoint after setpoint smoothing

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN (EPOS load side, rotating), S200 Basic PTI (EPOS load side, rotating), S200 PN (EPOS load side, rotating), S200 PTI (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Parameter group:** Position controller |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the position setpoint after the setpoint smoothing.

### r2557 LR position controller input system deviation

[S200 Basic PN](#r2557-lr-position-controller-input-system-deviation-1)

[S200 Basic PN EPOS load side, rotating](#r2557-lr-position-controller-input-system-deviation-2)

#### r2557 LR position controller input system deviation

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Parameter group:** Position controller |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the difference between the position setpoint and the position actual value
at the position controller input.

#### r2557 LR position controller input system deviation

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN (EPOS load side, rotating), S200 Basic PTI (EPOS load side, rotating), S200 PN (EPOS load side, rotating), S200 PTI (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Parameter group:** Position controller |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the difference between the position setpoint and the position actual value
at the position controller input.

### r2558 LR position controller output P component

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Parameter group:** Position controller |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** rpm | **Unit group:** 3_1 | **Unit selection:** p0505 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2000 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the P component at the output of the position controller (speed setpoint).

### r2559 LR position controller output I component

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Parameter group:** Position controller |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** rpm | **Unit group:** 3_1 | **Unit selection:** p0505 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2000 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the I component at the output of the position controller (speed setpoint).

### r2560 LR speed setpoint

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Parameter group:** Position controller |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** rpm | **Unit group:** 3_1 | **Unit selection:** p0505 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2000 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the speed setpoint after limiting (c2541).

### r2561 LR speed precontrol value

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Parameter group:** Position controller |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** rpm | **Unit group:** 3_1 | **Unit selection:** p0505 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2000 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the speed setpoint due to the precontrol.

### r2562 LR total speed setpoint

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Parameter group:** Position controller |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** rpm | **Unit group:** 3_1 | **Unit selection:** p0505 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2000 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the total speed setpoint  
This value is obtained from the sum of the speed precontrol and position controller
output.

**Dependency:** 
  
See also:
r2560, r2561

### r2563 LR following error dynamic model

[S200 Basic PN](#r2563-lr-following-error-dynamic-model-1)

[S200 Basic PN EPOS load side, rotating](#r2563-lr-following-error-dynamic-model-2)

#### r2563 LR following error dynamic model

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Parameter group:** Jog, Homing, Traversing blocks, Direct setpoint input (MDI), Position controller monitoring |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the dynamic following error.  
This value is the deviation, corrected by the velocity-dependent component, between
the position setpoint and the position actual value.

**Note:** 
  
For p2534 &gt;= 100 % (precontrol activated) the following applies:  
The dynamic following error (r2563) corresponds to the system deviation (r2557) at
the position controller input.  
For 0 % &lt; p2534 &lt; 100 % (precontrol activated) or p2534 = 0 % (precontrol deactivated)
the following applies:  
The dynamic following error (r2563) is the deviation between the measured position
actual value and a value that is calculated from the position setpoint via a PT1 model.
This compensates the system-related velocity-dependent system deviation for a P controller.

#### r2563 LR following error dynamic model

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN (EPOS load side, rotating), S200 Basic PTI (EPOS load side, rotating), S200 PN (EPOS load side, rotating), S200 PTI (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Parameter group:** Jog, Homing, Traversing blocks, Direct setpoint input (MDI), Position controller monitoring |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the dynamic following error.  
This value is the deviation, corrected by the velocity-dependent component, between
the position setpoint and the position actual value.

**Note:** 
  
For p2534 &gt;= 100 % (precontrol activated) the following applies:  
The dynamic following error (r2563) corresponds to the system deviation (r2557) at
the position controller input.  
For 0 % &lt; p2534 &lt; 100 % (precontrol activated) or p2534 = 0 % (precontrol deactivated)
the following applies:  
The dynamic following error (r2563) is the deviation between the measured position
actual value and a value that is calculated from the position setpoint via a PT1 model.
This compensates the system-related velocity-dependent system deviation for a P controller.

### r2564 LR torque precontrol value

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Parameter group:** Position controller |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Nm | **Unit group:** 7_1 | **Unit selection:** p0505 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2003 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the torque precontrol value.

**Note:** 
  
The torque precontrol value is the derivation over time of the speed precontrol value
and is referred to a moment of inertia of 1 kgm^2/2 PI. When using the precontrol,
then this should be evaluated corresponding to the actual moment of inertia.

### r2565 LR following error actual

[S200 Basic PN](#r2565-lr-following-error-actual-1)

[S200 Basic PN EPOS load side, rotating](#r2565-lr-following-error-actual-2)

#### r2565 LR following error actual

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Parameter group:** Position controller |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the actual following error.  
This value is the deviation between the position setpoint - after fine interpolation
- and the position actual value.

**Notice:** 
  
When speed precontrol is active (p2534 &gt; 0 %), the following applies:  
To calculate this value, the position setpoint is delayed by two position controller
sampling times.  
When speed precontrol is inactive (p2534 = 0 %), the following applies:  
To calculate this value, the position setpoint is delayed by two position controller
clock cycles.

#### r2565 LR following error actual

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN (EPOS load side, rotating), S200 Basic PTI (EPOS load side, rotating), S200 PN (EPOS load side, rotating), S200 PTI (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Parameter group:** Position controller |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the actual following error.  
This value is the deviation between the position setpoint - after fine interpolation
- and the position actual value.

**Notice:** 
  
When speed precontrol is active (p2534 &gt; 0 %), the following applies:  
To calculate this value, the position setpoint is delayed by two position controller
sampling times.  
When speed precontrol is inactive (p2534 = 0 %), the following applies:  
To calculate this value, the position setpoint is delayed by two position controller
clock cycles.

### p2567[0] LR torque precontrol moment of inertia

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Position controller |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** kgm² | **Unit group:** 25_1 | **Unit selection:** p0100 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.000000 [kgm²] | 100000.000000 [kgm²] | [0] 0.000000 [kgm²] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the moment of inertia for the torque precontrol.

**Dependency:** 
  
See also:
p2534, r2564

**Note:** 
  
When calculating the torque precontrol value (c2654), the time derivation of the speed
precontrol value is multiplied by 2 PI * p2567.  
For reasons associated with the compatibility to earlier firmware versions, the factory
setting for p2567 = 1 kgm^2/2 PI. This means that r2564 remains as standard the derivation
over time of the speed precontrol value and is referred, as before, to a moment of
inertia of 1 kgm^2/2 PI. For torque precontrol, the moment of inertia can now be directly
entered into p2567 (instead of subsequently evaluating the precontrol value).

### c2568 EPOS hardware limit switch activation

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Limit |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink binary |  |  |
| **Factory interconnection:** | **Fixed value:** |  |
| not interconnected | 0 |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal to activate the hardware limit switch.  
For c2568 = 1 signal:  
Negative hardware limit switch (c2569) and positive hardware limit switch (c2570)
are activated.  
For c2568 = 0 signal:  
Negative hardware limit switch (c2569) and positive hardware limit switch (c2570)
are not evaluated.

**Dependency:** 
  
See also:
c2569, c2570

**Note:** 
  
The traversing range can also be limited using software limit switches.

### c2569 EPOS negative hardware limit switch

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN, S200 PN |  |  |
| **Data type:**Unsigned8 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Limit |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink binary |  |  |
| **Factory interconnection:** | **Fixed value:** |  |
| 1:722.2 | 1 |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal for the hardware limit switch in the negative direction of travel.

**Recommendation:** 
  
Set the OFF3 ramp-down time (p1135) so that after the axis reaches the hardware limit
switch at maximum velocity, the braking distance traveled by the axis is not greater
than the distance that is available.

**Dependency:** 
  
See also:
p1135, c2568, c2570, p2573, r2684

**Caution:** 
  
The hardware limit switch is low active.  
For a 0 signal, the drive stops with the OFF3 ramp-down time (p1135), status signal
r2684.13 = 1 is set, saved and the corresponding fault is output. After the fault
has been acknowledged, only motion moving away from the hardware limit switch is permitted.  
For a 0/1 signal and valid travel direction, when the hardware limit switch is exited,
this is detected and status signal r2684.13 is set to 0.

### c2570 EPOS positive hardware limit switch

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN, S200 PN |  |  |
| **Data type:**Unsigned8 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Limit |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink binary |  |  |
| **Factory interconnection:** | **Fixed value:** |  |
| 1:722.3 | 1 |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal for the hardware limit switch in the positive direction of travel.

**Recommendation:** 
  
Set the OFF3 ramp-down time (p1135) so that after the axis reaches the hardware limit
switch at maximum velocity, the braking distance traveled by the axis is not greater
than the distance that is available.

**Dependency:** 
  
See also:
p1135, c2568, c2569, p2573, r2684

**Caution:** 
  
The hardware limit switch is low active.  
For a 0 signal  
the drive stops with the OFF3 ramp-down time (p1135), status signal r2684.14 = 1 is
set, saved and the corresponding fault is output. After the fault has been acknowledged,
only motion moving away from the hardware limit switch is permitted.  
For a 0/1 signal  
and valid travel direction, when the hardware limit switch is exited, this is detected
and status signal r2684.14 is set to 0.

### p2571 EPOS maximum velocity

[S200 Basic PN](#p2571-epos-maximum-velocity-1)

[S200 Basic PN EPOS load side, rotating](#p2571-epos-maximum-velocity-2)

#### p2571 EPOS maximum velocity

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Limit |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm/s | **Unit group:** 11_3 | **Unit selection:** p2497 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.010 [mm/s] | 40000000.000 [mm/s] | [0] 500.000 [mm/s] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the maximum velocity for the "basic positioner" function (EPOS).

**Dependency:** 
  
See also:
p2503, p2504, p2505, p2506

**Note:** 
  
The maximum velocity is active in all of the operating modes of the basic positioner.  
The maximum velocity for the basic positioner should be aligned with the maximum speed/velocity
of the speed/velocity controller:  
Rotary encoders:  
p2571[1000 LU/min] = min(p1082, p1083, |p1086|)[rpm] x p2505/p2504 x p2506/1000  
Linear encoders:  
p2571[1000 LU/min] = min(p1082, p1083, |p1086|)[m/min] x p2503/10[m]

#### p2571 EPOS maximum velocity

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN (EPOS load side, rotating), S200 Basic PTI (EPOS load side, rotating), S200 PN (EPOS load side, rotating), S200 PTI (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Limit |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** °/s | **Unit group:** 11_4 | **Unit selection:** p2497 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.010 [°/s] | 40000000.000 [°/s] | [0] 18000.000 [°/s] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the maximum velocity for the "basic positioner" function (EPOS).

**Dependency:** 
  
See also:
p2503, p2504, p2505, p2506

**Note:** 
  
The maximum velocity is active in all of the operating modes of the basic positioner.  
The maximum velocity for the basic positioner should be aligned with the maximum speed/velocity
of the speed/velocity controller:  
Rotary encoders:  
p2571[1000 LU/min] = min(p1082, p1083, |p1086|)[rpm] x p2505/p2504 x p2506/1000  
Linear encoders:  
p2571[1000 LU/min] = min(p1082, p1083, |p1086|)[m/min] x p2503/10[m]

### p2572 EPOS maximum acceleration

[S200 Basic PN](#p2572-epos-maximum-acceleration-1)

[S200 Basic PN EPOS load side, rotating](#p2572-epos-maximum-acceleration-2)

#### p2572 EPOS maximum acceleration

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Limit, Jog |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm/s² | **Unit group:** 12_3 | **Unit selection:** p2498 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.001 [mm/s²] | 2000000.000 [mm/s²] | [0] 10000.000 [mm/s²] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the maximum acceleration for the "basic positioner" function (EPOS).

**Dependency:** 
  
See also:
p2619, c2644

**Note:** 
  
The maximum acceleration appears to exhibit jumps (without jerk).  
"Traversing blocks" operating mode:  
The programmed acceleration override (p2619) acts on the maximum acceleration.  
"Direct setpoint input/MDI" operating mode:  
The acceleration override is effective (c2644, 4000 hex = 100 %).  
"Jog" and "Active homing" operating modes:  
No acceleration override is active. The axis starts with the maximum acceleration.

#### p2572 EPOS maximum acceleration

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN (EPOS load side, rotating), S200 Basic PTI (EPOS load side, rotating), S200 PN (EPOS load side, rotating), S200 PTI (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Limit, Jog |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** °/s² | **Unit group:** 12_4 | **Unit selection:** p2498 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.001 [°/s²] | 2000000.000 [°/s²] | [0] 360000.000 [°/s²] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the maximum acceleration for the "basic positioner" function (EPOS).

**Dependency:** 
  
See also:
p2619, c2644

**Note:** 
  
The maximum acceleration appears to exhibit jumps (without jerk).  
"Traversing blocks" operating mode:  
The programmed acceleration override (p2619) acts on the maximum acceleration.  
"Direct setpoint input/MDI" operating mode:  
The acceleration override is effective (c2644, 4000 hex = 100 %).  
"Jog" and "Active homing" operating modes:  
No acceleration override is active. The axis starts with the maximum acceleration.

### p2573 EPOS maximum deceleration

[S200 Basic PN](#p2573-epos-maximum-deceleration-1)

[S200 Basic PN EPOS load side, rotating](#p2573-epos-maximum-deceleration-2)

#### p2573 EPOS maximum deceleration

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Limit, Jog |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm/s² | **Unit group:** 12_3 | **Unit selection:** p2498 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.001 [mm/s²] | 2000000.000 [mm/s²] | [0] 10000.000 [mm/s²] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the maximum deceleration for the "basic positioner" function (EPOS).

**Dependency:** 
  
See also:
p2620, c2645

**Note:** 
  
The maximum deceleration appears to exhibit jumps (without jerk).  
"Traversing blocks" operating mode:  
The programmed deceleration override (p2620) acts on the maximum deceleration.  
"Direct setpoint input/MDI" operating mode:  
The deceleration override is effective (c2645, 4000 hex = 100 %).  
"Jog" and "Active homing" operating modes:  
No deceleration override is effective. The axis breaks with the maximum deceleration.

#### p2573 EPOS maximum deceleration

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN (EPOS load side, rotating), S200 Basic PTI (EPOS load side, rotating), S200 PN (EPOS load side, rotating), S200 PTI (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Limit, Jog |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** °/s² | **Unit group:** 12_4 | **Unit selection:** p2498 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.001 [°/s²] | 2000000.000 [°/s²] | [0] 360000.000 [°/s²] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the maximum deceleration for the "basic positioner" function (EPOS).

**Dependency:** 
  
See also:
p2620, c2645

**Note:** 
  
The maximum deceleration appears to exhibit jumps (without jerk).  
"Traversing blocks" operating mode:  
The programmed deceleration override (p2620) acts on the maximum deceleration.  
"Direct setpoint input/MDI" operating mode:  
The deceleration override is effective (c2645, 4000 hex = 100 %).  
"Jog" and "Active homing" operating modes:  
No deceleration override is effective. The axis breaks with the maximum deceleration.

### p2574 EPOS jerk limiting

[S200 Basic PN](#p2574-epos-jerk-limiting-1)

[S200 Basic PN EPOS load side, rotating](#p2574-epos-jerk-limiting-2)

#### p2574 EPOS jerk limiting

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Limit |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm/s³ | **Unit group:** 13_3 | **Unit selection:** p2499 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.001 [mm/s³] | 100000000.000 [mm/s³] | [0] 200000.000 [mm/s³] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the jerk limiting

**Dependency:** 
  
See also:
p2572, p2573, c2575

**Note:** 
  
The jerk limiting is internally converted into a jerk time as follows:  
Jerk time Tr = max(p2572, p2573) / p2574  
The jerk time is internally limited to 1000 ms, and is rounded off to an integer multiple
of the sampling time of the basic positioner cycle.  
The jerk time is the same for the acceleration and deceleration phases, also if the
maximum acceleration (p2572) and maximum deceleration (p2573) are set differently.  
  
If the maximum acceleration and maximum deceleration are set differently, then motion
is not optimal from a time perspective as the jerk limit cannot be utilized for the
lower of the two values.  
If, in the traversing profile, the acceleration time without jerk limiting is shorter
than jerk time Tr, then motion with jerk limiting is not time-optimized.  
For traversing motion with a direct transition between acceleration and deceleration
(i.e. jerk time is greater than the constant velocity phase), jerk can increase up
to twice the parameterized jerk.  
CONTINUE_FLYING with direction reversal acts internally just like a CONTINUE_WITH_STOP
without the "Set position reached" being set. Without jerk limiting, this behavior
can hardly be noticed as, when reversing, the position setpoint is only kept at zero
for the duration of one interpolator clock cycle.  
For block change enable CONTINUE_WITH_STOP, jerk limiting results in a longer delay
time.

#### p2574 EPOS jerk limiting

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN (EPOS load side, rotating), S200 Basic PTI (EPOS load side, rotating), S200 PN (EPOS load side, rotating), S200 PTI (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Limit |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** °/s³ | **Unit group:** 13_4 | **Unit selection:** p2499 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.001 [°/s³] | 100000000.000 [°/s³] | [0] 7200000.000 [°/s³] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the jerk limiting

**Dependency:** 
  
See also:
p2572, p2573, c2575

**Note:** 
  
The jerk limiting is internally converted into a jerk time as follows:  
Jerk time Tr = max(p2572, p2573) / p2574  
The jerk time is internally limited to 1000 ms, and is rounded off to an integer multiple
of the sampling time of the basic positioner cycle.  
The jerk time is the same for the acceleration and deceleration phases, also if the
maximum acceleration (p2572) and maximum deceleration (p2573) are set differently.  
  
If the maximum acceleration and maximum deceleration are set differently, then motion
is not optimal from a time perspective as the jerk limit cannot be utilized for the
lower of the two values.  
If, in the traversing profile, the acceleration time without jerk limiting is shorter
than jerk time Tr, then motion with jerk limiting is not time-optimized.  
For traversing motion with a direct transition between acceleration and deceleration
(i.e. jerk time is greater than the constant velocity phase), jerk can increase up
to twice the parameterized jerk.  
CONTINUE_FLYING with direction reversal acts internally just like a CONTINUE_WITH_STOP
without the "Set position reached" being set. Without jerk limiting, this behavior
can hardly be noticed as, when reversing, the position setpoint is only kept at zero
for the duration of one interpolator clock cycle.  
For block change enable CONTINUE_WITH_STOP, jerk limiting results in a longer delay
time.

### c2575 EPOS jerk limiting activation

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Limit, Jog, Homing, Traversing blocks, Direct setpoint input (MDI) |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink binary |  |  |
| **Factory interconnection:** | **Fixed value:** |  |
| not interconnected | 0 |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal to activate jerk limiting.  
Activating/deactivating:  
- Using c2575 = 1 signal or 0 signal.  
- Using the JERK command in the traversing block (only for c2575 = 0 signal).

**Dependency:** 
  
See also:
p2574

**Note:** 
  
A change to the signal state is only accepted at zero speed.

### p2576 EPOS modulo correction modulo range

[S200 Basic PN](#p2576-epos-modulo-correction-modulo-range-1)

[S200 Basic PN EPOS load side, rotating](#p2576-epos-modulo-correction-modulo-range-2)

#### p2576 EPOS modulo correction modulo range

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Basic positioner, Mechanics, Actual position value preprocessing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.0001 [mm] | 2147482752.0000 [mm] | [0] 360.0000 [mm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the modulo range for axes with modulo correction.

**Dependency:** 
  
See also:
c2577

#### p2576 EPOS modulo correction modulo range

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN (EPOS load side, rotating), S200 Basic PTI (EPOS load side, rotating), S200 PN (EPOS load side, rotating), S200 PTI (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Basic positioner, Mechanics, Actual position value preprocessing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.0001 [°] | 2147482752.0000 [°] | [0] 360.0000 [°] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the modulo range for axes with modulo correction.

**Dependency:** 
  
See also:
c2577

### c2577 EPOS modulo correction activation

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Basic positioner, Mechanics, Actual position value preprocessing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink binary |  |  |
| **Factory interconnection:** | **Fixed value:** |  |
| not interconnected | 0 |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal to activate modulo correction.

**Dependency:** 
  
See also:
p2576

**Note:** 
  
When the signal state changes, this only becomes effective in the "ready for switching
on" state.  
Selecting modulo correction:  
The actual position setpoint in the modulo range is corrected. The position actual
value differs from the position setpoint by the following error and can also leave
the modulo range.  
Deselecting modulo correction:  
It is based on the actual position actual value.

### c2578 EPOS negative software limit switch

[S200 Basic PN](#c2578-epos-negative-software-limit-switch-1)

[S200 Basic PN EPOS load side, rotating](#c2578-epos-negative-software-limit-switch-2)

#### c2578 EPOS negative software limit switch

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Limit |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Sink numeric |  | **Scaling:** - |
| **Factory interconnection:** | **Fixed value:** |  |
| 2580 | -2147482648.00 [mm] |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal for the negative software limit switch.

**Dependency:** 
  
See also:
c2579, p2580, p2581, c2582

**Notice:** 
  
A change to the software limit switch immediately becomes effective.  
If the software limit switch is changed, then this results in the positions in the
traversing blocks being checked.

**Note:** 
  
The following applies for the setting of the software limit switch:  
Negative software limit switch &lt; positive software limit switch

#### c2578 EPOS negative software limit switch

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN (EPOS load side, rotating), S200 Basic PTI (EPOS load side, rotating), S200 PN (EPOS load side, rotating), S200 PTI (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Limit |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Sink numeric |  | **Scaling:** - |
| **Factory interconnection:** | **Fixed value:** |  |
| 2580 | -2147482648.00 [°] |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal for the negative software limit switch.

**Dependency:** 
  
See also:
c2579, p2580, p2581, c2582

**Notice:** 
  
A change to the software limit switch immediately becomes effective.  
If the software limit switch is changed, then this results in the positions in the
traversing blocks being checked.

**Note:** 
  
The following applies for the setting of the software limit switch:  
Negative software limit switch &lt; positive software limit switch

### c2579 EPOS positive software limit switch

[S200 Basic PN](#c2579-epos-positive-software-limit-switch-1)

[S200 Basic PN EPOS load side, rotating](#c2579-epos-positive-software-limit-switch-2)

#### c2579 EPOS positive software limit switch

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Limit |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Sink numeric |  | **Scaling:** - |
| **Factory interconnection:** | **Fixed value:** |  |
| 2581 | 2147482752.00 [mm] |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal for the positive setpoint limit switch.

**Dependency:** 
  
See also:
c2578, p2580, p2581, c2582

**Notice:** 
  
A change to the software limit switch immediately becomes effective.  
If the software limit switch is changed, then this results in the positions in the
traversing blocks being checked.

**Note:** 
  
The following applies for the setting of the software limit switch:  
Negative software limit switch &lt; positive software limit switch

#### c2579 EPOS positive software limit switch

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN (EPOS load side, rotating), S200 Basic PTI (EPOS load side, rotating), S200 PN (EPOS load side, rotating), S200 PTI (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Limit |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Sink numeric |  | **Scaling:** - |
| **Factory interconnection:** | **Fixed value:** |  |
| 2581 | 2147482752.00 [°] |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal for the positive setpoint limit switch.

**Dependency:** 
  
See also:
c2578, p2580, p2581, c2582

**Notice:** 
  
A change to the software limit switch immediately becomes effective.  
If the software limit switch is changed, then this results in the positions in the
traversing blocks being checked.

**Note:** 
  
The following applies for the setting of the software limit switch:  
Negative software limit switch &lt; positive software limit switch

### p2580 EPOS negative software limit switch

[S200 Basic PN](#p2580-epos-negative-software-limit-switch-1)

[S200 Basic PN EPOS load side, rotating](#p2580-epos-negative-software-limit-switch-2)

#### p2580 EPOS negative software limit switch

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Limit |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Min:** | **Max:** | **Factory setting:** |
| -2147482752.0000 [mm] | 2147482752.0000 [mm] | [0] -2147482752.0000 [mm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the software limit switch, in the negative direction of travel.

**Dependency:** 
  
See also:
c2578, c2579, p2581, c2582

#### p2580 EPOS negative software limit switch

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN (EPOS load side, rotating), S200 Basic PTI (EPOS load side, rotating), S200 PN (EPOS load side, rotating), S200 PTI (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Limit |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Min:** | **Max:** | **Factory setting:** |
| -2147482752.0000 [°] | 2147482752.0000 [°] | [0] -2147482752.0000 [°] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the software limit switch, in the negative direction of travel.

**Dependency:** 
  
See also:
c2578, c2579, p2581, c2582

### p2581 EPOS positive software limit switch

[S200 Basic PN](#p2581-epos-positive-software-limit-switch-1)

[S200 Basic PN EPOS load side, rotating](#p2581-epos-positive-software-limit-switch-2)

#### p2581 EPOS positive software limit switch

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Limit |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Min:** | **Max:** | **Factory setting:** |
| -2147482752.0000 [mm] | 2147482752.0000 [mm] | [0] 2147482752.0000 [mm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the software limit switch, in the positive direction of travel.

**Dependency:** 
  
See also:
c2578, c2579, p2580, c2582

#### p2581 EPOS positive software limit switch

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN (EPOS load side, rotating), S200 Basic PTI (EPOS load side, rotating), S200 PN (EPOS load side, rotating), S200 PTI (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Limit |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Min:** | **Max:** | **Factory setting:** |
| -2147482752.0000 [°] | 2147482752.0000 [°] | [0] 2147482752.0000 [°] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the software limit switch, in the positive direction of travel.

**Dependency:** 
  
See also:
c2578, c2579, p2580, c2582

### c2582 EPOS software limit switch activation

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Limit |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink binary |  |  |
| **Factory interconnection:** | **Fixed value:** |  |
| not interconnected | 0 |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal to activate the software limit switch.

**Dependency:** 
  
See also:
c2578, c2579, p2580, p2581

**Caution:** 
  
Software limit switch is effective for:  
- Axis is homed (r2684.11 = 1) and  
- c2582 = 1 signal.  
Software limit switch is ineffective for:  
- Modulo correction active (c2577 = 1 signal) or  
- "Active homing" is executed.

**Notice:** 
  
Target position for relative positioning outside software limit switch:  
The traversing block is started and the axis comes to a standstill at the software
limit switch. An appropriate alarm is output and the traversing block is interrupted.
Traversing blocks with valid position can be activated.  
  
Target position for absolute positioning outside software limit switch:  
In the "traversing blocks" mode, the traversing block is not started and an appropriate
fault is output.  
  
Axis outside the valid traversing range:  
If the axis is already outside the valid traversing range, then an appropriate fault
is output. The fault can be acknowledged at standstill. Traversing blocks with valid
position can be activated.

**Note:** 
  
The traversing range can also be limited using hardware limit switches.

### p2583 EPOS backlash compensation

[S200 Basic PN](#p2583-epos-backlash-compensation-1)

[S200 Basic PN EPOS load side, rotating](#p2583-epos-backlash-compensation-2)

#### p2583 EPOS backlash compensation

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Basic positioner |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| -200000.0000 [mm] | 200000.0000 [mm] | [0] 0.0000 [mm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the amount of play (backlash) for positive or negative play.  
0: backlash compensation is deactivated.  
&gt; 0: Positive backlash (normal case)  
When the direction is reversed, the encoder actual value leads the actual value.  
&lt; 0: Negative backlash  
When the direction is reversed, the actual value leads the encoder actual value.

**Dependency:** 
  
If a stationary axis is referenced by "setting the home position", or an adjusted
with absolute encoder is switched on, then the setting of c2604 is relevant for entering
the compensation value.  
c2604 = 1:  
Traveling in the positive direction -&gt; A compensation value is immediately entered.  
Traveling in the negative direction -&gt; A compensation value is not entered  
c2604 = 0:  
Traveling in the positive direction -&gt; A compensation value is not entered  
Traveling in the negative direction -&gt; A compensation value is immediately entered.  
When again setting the home position (a homed axis) or for "passive homing", c2604
is not relevant but instead the history of the axis.  
See also:
c2604

#### p2583 EPOS backlash compensation

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN (EPOS load side, rotating), S200 Basic PTI (EPOS load side, rotating), S200 PN (EPOS load side, rotating), S200 PTI (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Basic positioner |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| -200000.0000 [°] | 200000.0000 [°] | [0] 0.0000 [°] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the amount of play (backlash) for positive or negative play.  
0: backlash compensation is deactivated.  
&gt; 0: Positive backlash (normal case)  
When the direction is reversed, the encoder actual value leads the actual value.  
&lt; 0: Negative backlash  
When the direction is reversed, the actual value leads the encoder actual value.

**Dependency:** 
  
If a stationary axis is referenced by "setting the home position", or an adjusted
with absolute encoder is switched on, then the setting of c2604 is relevant for entering
the compensation value.  
c2604 = 1:  
Traveling in the positive direction -&gt; A compensation value is immediately entered.  
Traveling in the negative direction -&gt; A compensation value is not entered  
c2604 = 0:  
Traveling in the positive direction -&gt; A compensation value is not entered  
Traveling in the negative direction -&gt; A compensation value is immediately entered.  
When again setting the home position (a homed axis) or for "passive homing", c2604
is not relevant but instead the history of the axis.  
See also:
c2604

### p2584.0...3 EPOS functions configuration

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Basic positioner |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| - | - | [0] 0100 bin |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the configuration for additional functions for the basic positioner (EPOS).

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Activate position feedback signal | No | Yes | - |
| 01 | Hardware limit switch evaluation | Edge evaluation | Level evaluation | - |
| 02 | Travel to fixed stop - torque calculation based on the offset | No | Yes | - |
| 03 | Active homing with absolute encoder adjustment | No | Yes | - |

**Note:** 
  
For bit 00:  
When the bit is set, for traversing blocks with absolute target positions (p2617[x])
when the tolerance window (p2688) is reached, the traversing block number (p2616[x])
is output bit-coded (r2689).  
For bit 01:  
When the bit is set, the hardware limit switch is evaluated, level-triggered.  
This setting is recommended for a poor position actual value resolution, as in this
case the direction does not have to be evaluated.  
For bit 02:  
When the bit is set, for "Travel to fixed stop", the torque setpoints are calculated
based on the offset for the torque limit (p1532).  
For bit 03:  
After successful active homing, an absolute encoder is adjusted (p2507).

### p2585 EPOS jog 1 setpoint velocity

[S200 Basic PN](#p2585-epos-jog-1-setpoint-velocity-1)

[S200 Basic PN EPOS load side, rotating](#p2585-epos-jog-1-setpoint-velocity-2)

#### p2585 EPOS jog 1 setpoint velocity

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Jog |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm/s | **Unit group:** 11_3 | **Unit selection:** p2497 |
| **Min:** | **Max:** | **Factory setting:** |
| -40000000.000 [mm/s] | 40000000.000 [mm/s] | [0] -5.000 [mm/s] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the setpoint velocity for jog 1.

**Dependency:** 
  
See also:
p2587, c2589, c2591

#### p2585 EPOS jog 1 setpoint velocity

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN (EPOS load side, rotating), S200 Basic PTI (EPOS load side, rotating), S200 PN (EPOS load side, rotating), S200 PTI (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Jog |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** °/s | **Unit group:** 11_4 | **Unit selection:** p2497 |
| **Min:** | **Max:** | **Factory setting:** |
| -40000000.000 [°/s] | 40000000.000 [°/s] | [0] -180.000 [°/s] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the setpoint velocity for jog 1.

**Dependency:** 
  
See also:
p2587, c2589, c2591

### p2586 EPOS jog 2 setpoint velocity

[S200 Basic PN](#p2586-epos-jog-2-setpoint-velocity-1)

[S200 Basic PN EPOS load side, rotating](#p2586-epos-jog-2-setpoint-velocity-2)

#### p2586 EPOS jog 2 setpoint velocity

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Jog |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm/s | **Unit group:** 11_3 | **Unit selection:** p2497 |
| **Min:** | **Max:** | **Factory setting:** |
| -40000000.000 [mm/s] | 40000000.000 [mm/s] | [0] 5.000 [mm/s] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the setpoint velocity for jog 2.

**Dependency:** 
  
See also:
p2588, c2590, c2591

#### p2586 EPOS jog 2 setpoint velocity

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN (EPOS load side, rotating), S200 Basic PTI (EPOS load side, rotating), S200 PN (EPOS load side, rotating), S200 PTI (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Jog |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** °/s | **Unit group:** 11_4 | **Unit selection:** p2497 |
| **Min:** | **Max:** | **Factory setting:** |
| -40000000.000 [°/s] | 40000000.000 [°/s] | [0] 180.000 [°/s] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the setpoint velocity for jog 2.

**Dependency:** 
  
See also:
p2588, c2590, c2591

### p2587 EPOS jog 1 traversing distance

[S200 Basic PN](#p2587-epos-jog-1-traversing-distance-1)

[S200 Basic PN EPOS load side, rotating](#p2587-epos-jog-1-traversing-distance-2)

#### p2587 EPOS jog 1 traversing distance

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Jog |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.0000 [mm] | 2147482752.0000 [mm] | [0] 1.0000 [mm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the traversing distance for incremental jog 1.

**Dependency:** 
  
See also:
p2585, c2589, c2591

**Note:** 
  
Incremental jog 1 is started with c2591 = 1 signal and c2589 = 0/1 signal.  
With c2589 = 0 signal, incremental jogging is interrupted.

#### p2587 EPOS jog 1 traversing distance

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN (EPOS load side, rotating), S200 Basic PTI (EPOS load side, rotating), S200 PN (EPOS load side, rotating), S200 PTI (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Jog |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.0000 [°] | 2147482752.0000 [°] | [0] 36.0000 [°] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the traversing distance for incremental jog 1.

**Dependency:** 
  
See also:
p2585, c2589, c2591

**Note:** 
  
Incremental jog 1 is started with c2591 = 1 signal and c2589 = 0/1 signal.  
With c2589 = 0 signal, incremental jogging is interrupted.

### p2588 EPOS jog 2 traversing distance

[S200 Basic PN](#p2588-epos-jog-2-traversing-distance-1)

[S200 Basic PN EPOS load side, rotating](#p2588-epos-jog-2-traversing-distance-2)

#### p2588 EPOS jog 2 traversing distance

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Jog |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.0000 [mm] | 2147482752.0000 [mm] | [0] 1.0000 [mm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the traversing distance for incremental jog 2.

**Dependency:** 
  
See also:
p2586, c2590, c2591

**Note:** 
  
Incremental jog 2 is started with c2591 = 1 signal and c2590 = 0/1 signal.  
Incremental jogging is interrupted with c2590 = 0 signal.

#### p2588 EPOS jog 2 traversing distance

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN (EPOS load side, rotating), S200 Basic PTI (EPOS load side, rotating), S200 PN (EPOS load side, rotating), S200 PTI (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Jog |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.0000 [°] | 2147482752.0000 [°] | [0] 36.0000 [°] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the traversing distance for incremental jog 2.

**Dependency:** 
  
See also:
p2586, c2590, c2591

**Note:** 
  
Incremental jog 2 is started with c2591 = 1 signal and c2590 = 0/1 signal.  
Incremental jogging is interrupted with c2590 = 0 signal.

### c2589 EPOS jog 1

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Jog |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink binary |  |  |
| **Factory interconnection:** | **Fixed value:** |  |
| not interconnected | 0 |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal for jog 1.

**Dependency:** 
  
When jogging, the axis is accelerated or braked with the maximum acceleration/deceleration
(p2572/p2573).  
c2591 = 0 signal  
The axis endlessly moves with the setpoint velocity, jog 1 (p2585).  
c2591 = 1 signal  
The axis traverses through a parameterized distance (p2585) with the setpoint velocity,
jog 1 (p2587).  
See also:
p2572, p2573, p2585, p2587, c2591

**Notice:** 
  
The parameter may be protected as a result of r0922 and cannot be changed.

### c2590 EPOS jog 2

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Jog |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink binary |  |  |
| **Factory interconnection:** | **Fixed value:** |  |
| not interconnected | 0 |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal for jog 2.

**Dependency:** 
  
When jogging, the axis is accelerated or braked with the maximum acceleration/deceleration
(p2572/p2573).  
c2591 = 0 signal  
The axis endlessly moves with the setpoint velocity, jog 2 (p2586).  
c2591 = 1 signal  
The axis traverses through a parameterized distance (p2586) with the setpoint velocity,
jog 2 (p2588).  
See also:
p2572, p2573, p2586, p2588, c2591

**Notice:** 
  
The parameter may be protected as a result of r0922 and cannot be changed.

### c2591 EPOS jogging incremental

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Jog |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink binary |  |  |
| **Factory interconnection:** | **Fixed value:** |  |
| not interconnected | 0 |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal for incremental jogging.

**Dependency:** 
  
See also:
p2585, p2586, p2587, p2588, c2589, c2590

### c2595 EPOS homing start

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Homing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink binary |  |  |
| **Factory interconnection:** | **Fixed value:** |  |
| not interconnected | 0 |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal to start "Active homing" or "Passive homing".  
0/1 signal edge: Homing is started.  
1/0 signal edge: Homing is interrupted.

**Dependency:** 
  
See also:
c2597, c2598, p2599, r2684

**Notice:** 
  
The parameter may be protected as a result of r0922 and cannot be changed.

**Note:** 
  
Active homing (c2597 = 0 signal):  
Active homing can only be activated (0/1 edge) after traversing motion that is being
processed has been completed.  
With the start, where relevant, the state signal "home position set" (r2684.11) is
reset.  
Passive homing (c2597 = 1 signal):  
With the start, the state signal "home position set" (r2684.11) is not reset.

### c2596 EPOS set home position

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Homing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink binary |  |  |
| **Factory interconnection:** | **Fixed value:** |  |
| not interconnected | 0 |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal for "Set home position".

**Dependency:** 
  
See also:
c2598, p2599, r2684

**Notice:** 
  
The parameter may be protected as a result of r0922 and cannot be changed.

**Note:** 
  
Home position setting is effective in the following operating states:  
- In the basic state.  
- For FIXED STOP with progress condition END (corresponds to the initial state).  
- For traversing block interrupted via c2640 = 0 signal (intermediate stop).  
- For EPOS not enabled and position actual value valid

### c2597 EPOS homing type selection

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Homing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink binary |  |  |
| **Factory interconnection:** | **Fixed value:** |  |
| not interconnected | 0 |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal to select homing type.  
1 signal: Passive homing  
0 signal: Active homing

**Dependency:** 
  
See also:
c2595

**Note:** 
  
Homing is activated as follows:  
- Select homing type (c2597)  
- Start homing (c2595 = 0/1 signal edge)

### c2598[0...3] EPOS home position signal

[S200 Basic PN](#c259803-epos-home-position-signal-1)

[S200 Basic PN EPOS load side, rotating](#c259803-epos-home-position-signal-2)

#### c2598[0...3] EPOS home position signal

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Homing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Sink numeric |  | **Scaling:** - |
| **Factory interconnection:** | **Fixed value:** |  |
| 2599 | 0.00 [mm] |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal for the home position.  
This value is used as reference for the following homing operations:  
- Active homing  
- Set home position  
- Passive homing  
- Absolute value adjustment

**Index:** 
  
[
0]:
Position control  
[
1]:
Motor encoder  
[
2]:
Reserved  
[
3]:
Reserved

**Dependency:** 
  
See also:
p2502, p2507, c2595, c2596, c2597, p2599

**Note:** 
  
When function "Basic positioner" is activated, the following applies:  
Incremental measuring system:  
After the home position is reached, the drive accepts the actual axis position from
the position value received via c2598[0].  
Absolute encoder:  
When adjusting the encoder, the position received is set as the actual axis position.

#### c2598[0...3] EPOS home position signal

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN (EPOS load side, rotating), S200 Basic PTI (EPOS load side, rotating), S200 PN (EPOS load side, rotating), S200 PTI (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Homing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Sink numeric |  | **Scaling:** - |
| **Factory interconnection:** | **Fixed value:** |  |
| 2599 | 0.00 [°] |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal for the home position.  
This value is used as reference for the following homing operations:  
- Active homing  
- Set home position  
- Passive homing  
- Absolute value adjustment

**Index:** 
  
[
0]:
Position control  
[
1]:
Motor encoder  
[
2]:
Reserved  
[
3]:
Reserved

**Dependency:** 
  
See also:
p2502, p2507, c2595, c2596, c2597, p2599

**Note:** 
  
When function "Basic positioner" is activated, the following applies:  
Incremental measuring system:  
After the home position is reached, the drive accepts the actual axis position from
the position value received via c2598[0].  
Absolute encoder:  
When adjusting the encoder, the position received is set as the actual axis position.

### p2599 EPOS home position value

[S200 Basic PN](#p2599-epos-home-position-value-1)

[S200 Basic PN EPOS load side, rotating](#p2599-epos-home-position-value-2)

#### p2599 EPOS home position value

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Homing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Min:** | **Max:** | **Factory setting:** |
| -2147482752.0000 [mm] | 2147482752.0000 [mm] | [0] 0.0000 [mm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the position value for the home position.  
This value is set as the actual axis position after homing or adjustment.

**Dependency:** 
  
See also:
p2507, c2595, c2596, c2597, c2598

#### p2599 EPOS home position value

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN (EPOS load side, rotating), S200 Basic PTI (EPOS load side, rotating), S200 PN (EPOS load side, rotating), S200 PTI (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Homing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Min:** | **Max:** | **Factory setting:** |
| -2147482752.0000 [°] | 2147482752.0000 [°] | [0] 0.0000 [°] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the position value for the home position.  
This value is set as the actual axis position after homing or adjustment.

**Dependency:** 
  
See also:
p2507, c2595, c2596, c2597, c2598

### p2600 EPOS active homing home position offset

[S200 Basic PN](#p2600-epos-active-homing-home-position-offset-1)

[S200 Basic PN EPOS load side, rotating](#p2600-epos-active-homing-home-position-offset-2)

#### p2600 EPOS active homing home position offset

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Homing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| -2147482752.0000 [mm] | 2147482752.0000 [mm] | [0] 0.0000 [mm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the home position shift for active homing.

**Dependency:** 
  
See also:
c2598

#### p2600 EPOS active homing home position offset

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN (EPOS load side, rotating), S200 Basic PTI (EPOS load side, rotating), S200 PN (EPOS load side, rotating), S200 PTI (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Homing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| -2147482752.0000 [°] | 2147482752.0000 [°] | [0] 0.0000 [°] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the home position shift for active homing.

**Dependency:** 
  
See also:
c2598

### c2604 EPOS active homing start direction

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Homing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink binary |  |  |
| **Factory interconnection:** | **Fixed value:** |  |
| not interconnected | 0 |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal for the start direction for active homing.  
1 signal: Start in the negative direction.  
0 signal: Start in the positive direction.

**Dependency:** 
  
See also:
p2583, c2595, c2597

### p2605 EPOS active homing approach velocity reference cam

[S200 Basic PN](#p2605-epos-active-homing-approach-velocity-reference-cam-1)

[S200 Basic PN EPOS load side, rotating](#p2605-epos-active-homing-approach-velocity-reference-cam-2)

#### p2605 EPOS active homing approach velocity reference cam

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Homing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm/s | **Unit group:** 11_3 | **Unit selection:** p2497 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.010 [mm/s] | 40000000.000 [mm/s] | [0] 100.000 [mm/s] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the approach velocity to the reference cam for active homing.

**Dependency:** 
  
Active homing only starts with the approach velocity to the reference cam when there
is a reference cam (p2607 = 1).  
See also:
c2595, c2597, c2604, p2606, p2607

**Note:** 
  
When traversing to the reference cam, the velocity override is effective.  
If, at the start of active homing, the axis is already at the reference cam, then
the axis immediately starts to traverse to the zero mark.

#### p2605 EPOS active homing approach velocity reference cam

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN (EPOS load side, rotating), S200 Basic PTI (EPOS load side, rotating), S200 PN (EPOS load side, rotating), S200 PTI (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Homing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** °/s | **Unit group:** 11_4 | **Unit selection:** p2497 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.010 [°/s] | 40000000.000 [°/s] | [0] 3600.000 [°/s] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the approach velocity to the reference cam for active homing.

**Dependency:** 
  
Active homing only starts with the approach velocity to the reference cam when there
is a reference cam (p2607 = 1).  
See also:
c2595, c2597, c2604, p2606, p2607

**Note:** 
  
When traversing to the reference cam, the velocity override is effective.  
If, at the start of active homing, the axis is already at the reference cam, then
the axis immediately starts to traverse to the zero mark.

## SINAMICS Parameter S200 Basic PN 02606 - 05300

SINAMICS Parameter S200 Basic PN 02606 - 05300

### p2606 EPOS active homing reference cam maximum distance

[S200 Basic PN](#p2606-epos-active-homing-reference-cam-maximum-distance-1)

[S200 Basic PN EPOS load side, rotating](#p2606-epos-active-homing-reference-cam-maximum-distance-2)

#### p2606 EPOS active homing reference cam maximum distance

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Homing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.0000 [mm] | 2147482752.0000 [mm] | [0] 2147482752.0000 [mm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the maximum distance after starting active homing when traversing to the reference
cam.

**Dependency:** 
  
See also:
c2595, c2597, c2604, p2605, p2607

**Note:** 
  
When using a reversing cam, the maximum distance must be set appropriately long.

#### p2606 EPOS active homing reference cam maximum distance

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN (EPOS load side, rotating), S200 Basic PTI (EPOS load side, rotating), S200 PN (EPOS load side, rotating), S200 PTI (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Homing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.0000 [°] | 2147482752.0000 [°] | [0] 2147482752.0000 [°] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the maximum distance after starting active homing when traversing to the reference
cam.

**Dependency:** 
  
See also:
c2595, c2597, c2604, p2605, p2607

**Note:** 
  
When using a reversing cam, the maximum distance must be set appropriately long.

### p2607 EPOS active homing reference cam available

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Homing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 1 | [0] 1 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets whether or not a reference cam is available for active homing.  
Value = 1: Reference cam present.  
Value = 0: No reference cam present.

**Dependency:** 
  
See also:
c2595, c2597, c2604, p2605, p2606

### p2608 EPOS active homing approach velocity zero mark

[S200 Basic PN](#p2608-epos-active-homing-approach-velocity-zero-mark-1)

[S200 Basic PN EPOS load side, rotating](#p2608-epos-active-homing-approach-velocity-zero-mark-2)

#### p2608 EPOS active homing approach velocity zero mark

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Homing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm/s | **Unit group:** 11_3 | **Unit selection:** p2497 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.010 [mm/s] | 40000000.000 [mm/s] | [0] 25.000 [mm/s] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the approach velocity after detecting the reference cam to search for the zero
mark for active homing.

**Dependency:** 
  
If there is no reference cam (p2607 = 0), active homing starts immediately with the
axis traversing to the zero mark.  
See also:
c2595, c2597, c2604, p2607, p2609

**Caution:** 
  
If the reference cam is not adjusted so that for each active homing the same zero
mark for synchronization is detected, then an "incorrect" axis reference point is
obtained.  
After the reference cam has been left, the search for the zero mark is activated with
a time delay due to internal factors. This is the reason that the reference cam should
be adjusted in this center between two zero marks and the approach velocity should
be adapted to the distance between two zero marks.

**Note:** 
  
The velocity override is not effective when traversing to the zero mark.

#### p2608 EPOS active homing approach velocity zero mark

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN (EPOS load side, rotating), S200 Basic PTI (EPOS load side, rotating), S200 PN (EPOS load side, rotating), S200 PTI (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Homing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** °/s | **Unit group:** 11_4 | **Unit selection:** p2497 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.010 [°/s] | 40000000.000 [°/s] | [0] 900.000 [°/s] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the approach velocity after detecting the reference cam to search for the zero
mark for active homing.

**Dependency:** 
  
If there is no reference cam (p2607 = 0), active homing starts immediately with the
axis traversing to the zero mark.  
See also:
c2595, c2597, c2604, p2607, p2609

**Caution:** 
  
If the reference cam is not adjusted so that for each active homing the same zero
mark for synchronization is detected, then an "incorrect" axis reference point is
obtained.  
After the reference cam has been left, the search for the zero mark is activated with
a time delay due to internal factors. This is the reason that the reference cam should
be adjusted in this center between two zero marks and the approach velocity should
be adapted to the distance between two zero marks.

**Note:** 
  
The velocity override is not effective when traversing to the zero mark.

### p2609 EPOS active homing max distance reference cam and zero mark

[S200 Basic PN](#p2609-epos-active-homing-max-distance-reference-cam-and-zero-mark-1)

[S200 Basic PN EPOS load side, rotating](#p2609-epos-active-homing-max-distance-reference-cam-and-zero-mark-2)

#### p2609 EPOS active homing max distance reference cam and zero mark

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Homing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.0000 [mm] | 2147482752.0000 [mm] | [0] 20.0000 [mm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the maximum distance after leaving the reference cam when traversing to the zero
mark.

**Dependency:** 
  
See also:
c2595, c2597, c2604, p2607, p2608

#### p2609 EPOS active homing max distance reference cam and zero mark

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN (EPOS load side, rotating), S200 Basic PTI (EPOS load side, rotating), S200 PN (EPOS load side, rotating), S200 PTI (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Homing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.0000 [°] | 2147482752.0000 [°] | [0] 720.0000 [°] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the maximum distance after leaving the reference cam when traversing to the zero
mark.

**Dependency:** 
  
See also:
c2595, c2597, c2604, p2607, p2608

### p2611 EPOS active homing approach velocity home position

[S200 Basic PN](#p2611-epos-active-homing-approach-velocity-home-position-1)

[S200 Basic PN EPOS load side, rotating](#p2611-epos-active-homing-approach-velocity-home-position-2)

#### p2611 EPOS active homing approach velocity home position

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Homing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm/s | **Unit group:** 11_3 | **Unit selection:** p2497 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.010 [mm/s] | 40000000.000 [mm/s] | [0] 25.000 [mm/s] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the approach velocity after detecting the zero mark to approach the home position.

**Dependency:** 
  
See also:
c2595, c2597, c2604, p2607, p2609

**Note:** 
  
When traversing to the home position, the velocity override is not effective.

#### p2611 EPOS active homing approach velocity home position

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN (EPOS load side, rotating), S200 Basic PTI (EPOS load side, rotating), S200 PN (EPOS load side, rotating), S200 PTI (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Homing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** °/s | **Unit group:** 11_4 | **Unit selection:** p2497 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.010 [°/s] | 40000000.000 [°/s] | [0] 900.000 [°/s] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the approach velocity after detecting the zero mark to approach the home position.

**Dependency:** 
  
See also:
c2595, c2597, c2604, p2607, p2609

**Note:** 
  
When traversing to the home position, the velocity override is not effective.

### c2612[0...1] EPOS active homing reference cam

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Homing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink binary |  |  |
| **Factory interconnection:** | **Fixed value:** |  |
| not interconnected | 0 |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal for the reference cam.

**Index:** 
  
[
0]:
Reference cam selection 1  
[
1]:
Reference cam selection 2

**Dependency:** 
  
See also:
r0922, p2607

**Notice:** 
  
Parameter c2612[0] may be protected as a result of r0922 and cannot be changed.

**Note:** 
  
The selection of reference cam 1 or 2 can be configured using p11550.

### c2613 EPOS active homing negative reversing cam

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Homing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink binary |  |  |
| **Factory interconnection:** | **Fixed value:** |  |
| not interconnected | 1 |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal for the reversing cam in the negative direction of travel.  
1 signal: Reversing cam not reached.  
0 signal: Reversing cam reached.

**Dependency:** 
  
See also:
c2614

**Note:** 
  
If, during active homing of the positive and negative reversing cam, a 0 signal is
detected, then the axis remains at a standstill.

### c2614 EPOS active homing positive reversing cam

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Homing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink binary |  |  |
| **Factory interconnection:** | **Fixed value:** |  |
| not interconnected | 1 |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal for the reversing cam in the positive direction of travel.  
1 signal: Reversing cam not reached.  
0 signal: Reversing cam reached.

**Dependency:** 
  
See also:
c2613

**Note:** 
  
If, during active homing of the positive and negative reversing cam, a 0 signal is
detected, then the axis remains at a standstill.

### p2615 EPOS maximum number of traversing blocks

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Traversing blocks |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 1 | 32 | [0] 32 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the maximum number of traversing blocks that are available.

**Dependency:** 
  
See also:
p2616, p2617, p2618, p2619, p2620, p2621, p2622, p2623

### p2616[0...n] EPOS traversing block block number

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Traversing blocks |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:**  n defined by: p2615 |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| -1 | 31 | [0] -1 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets a block number.  
-1: Invalid block number. These blocks are not taken into account.  
0 ... 31: Valid block number.

**Dependency:** 
  
The number of indices depends on p2615.  
See also:
p2615, p2617, p2618, p2619, p2620, p2621, p2622, p2623

### p2617[0...n] EPOS traversing block position

[S200 Basic PN](#p26170n-epos-traversing-block-position-1)

[S200 Basic PN EPOS load side, rotating](#p26170n-epos-traversing-block-position-2)

#### p2617[0...n] EPOS traversing block position

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Traversing blocks |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:**  n defined by: p2615 |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| -2147482752.0000 [mm] | 2147482752.0000 [mm] | [0] 0.0000 [mm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the target position for the traversing block.

**Dependency:** 
  
The number of indices depends on p2615.  
See also:
p2615, p2616, p2618, p2619, p2620, p2621, p2622, p2623

**Note:** 
  
The target position is approached in either relative or absolute terms depending on
p2623.

#### p2617[0...n] EPOS traversing block position

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN (EPOS load side, rotating), S200 Basic PTI (EPOS load side, rotating), S200 PN (EPOS load side, rotating), S200 PTI (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Traversing blocks |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:**  n defined by: p2615 |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| -2147482752.0000 [°] | 2147482752.0000 [°] | [0] 0.0000 [°] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the target position for the traversing block.

**Dependency:** 
  
The number of indices depends on p2615.  
See also:
p2615, p2616, p2618, p2619, p2620, p2621, p2622, p2623

**Note:** 
  
The target position is approached in either relative or absolute terms depending on
p2623.

### p2618[0...n] EPOS traversing block velocity

[S200 Basic PN](#p26180n-epos-traversing-block-velocity-1)

[S200 Basic PN EPOS load side, rotating](#p26180n-epos-traversing-block-velocity-2)

#### p2618[0...n] EPOS traversing block velocity

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Traversing blocks |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:**  n defined by: p2615 |  | **Calculated:** - |
| **Unit:** mm/s | **Unit group:** 11_3 | **Unit selection:** p2497 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.010 [mm/s] | 40000000.000 [mm/s] | [0] 100.000 [mm/s] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the velocity for the traversing block.

**Dependency:** 
  
The number of indices depends on p2615.  
See also:
p2615, p2616, p2617, p2619, p2620, p2621, p2622, p2623, c2646

**Note:** 
  
The velocity can be influenced using the velocity override (c2646).

#### p2618[0...n] EPOS traversing block velocity

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN (EPOS load side, rotating), S200 Basic PTI (EPOS load side, rotating), S200 PN (EPOS load side, rotating), S200 PTI (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Traversing blocks |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:**  n defined by: p2615 |  | **Calculated:** - |
| **Unit:** °/s | **Unit group:** 11_4 | **Unit selection:** p2497 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.010 [°/s] | 40000000.000 [°/s] | [0] 3600.000 [°/s] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the velocity for the traversing block.

**Dependency:** 
  
The number of indices depends on p2615.  
See also:
p2615, p2616, p2617, p2619, p2620, p2621, p2622, p2623, c2646

**Note:** 
  
The velocity can be influenced using the velocity override (c2646).

### p2619[0...n] EPOS traversing block acceleration override

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Traversing blocks |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:**  n defined by: p2615 |  | **Calculated:** - |
| **Unit:** % | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 1.0 [%] | 100.0 [%] | [0] 100.0 [%] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the acceleration override for the traversing block.  
The override refers to the maximum acceleration (p2572).

**Dependency:** 
  
The number of indices depends on p2615.  
See also:
p2572, p2615, p2616, p2617, p2618, p2620, p2621, p2622, p2623

### p2620[0...n] EPOS traversing deceleration override

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Traversing blocks |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:**  n defined by: p2615 |  | **Calculated:** - |
| **Unit:** % | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 1.0 [%] | 100.0 [%] | [0] 100.0 [%] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the deceleration override for the traversing block.  
The override refers to the maximum deceleration (p2573).

**Dependency:** 
  
The number of indices depends on p2615.  
See also:
p2573, p2615, p2616, p2617, p2618, p2619, p2621, p2622, p2623

**Notice:** 
  
If, when calculating the traversing profile, it is identified that the target position
of the next block with the programmed deceleration override will not be reached without
direction reversal (flying block change), then the old (actual) deceleration override
remains effective.

### p2621[0...n] EPOS traversing block task

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Traversing blocks |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:**  n defined by: p2615 |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 1 | 9 | [0] 1 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the required task for the traversing block.

**Value:** 
  
1:
POSITIONING  
2:
FIXED STOP  
3:
ENDLESS_POS  
4:
ENDLESS_NEG  
5:
WAITING  
6:
GOTO  
7:
SET_O  
8:
RESET_O  
9:
JERK

**Dependency:** 
  
The number of indices depends on p2615.  
See also:
p2615, p2616, p2617, p2618, p2619, p2620, p2622, p2623

### p2622[0...n] EPOS traversing block task parameter

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Traversing blocks |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:**  n defined by: p2615 |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| -2147483648 | 2147483647 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets additional information/data of the appropriate task for the traversing block.

**Dependency:** 
  
The number of indices depends on p2615.  
See also:
p2615, p2616, p2617, p2618, p2619, p2620, p2621, p2623

**Note:** 
  
The following should be set depending on the task:  
FIXED STOP: Clamping torque and clamping force (rotary 0...65536 [0.01 Nm], linear
0...65536 [N])  
WAIT: Wait time [ms]  
GOTO: Block number  
SET_O: 1, 2 or 3 - set direct output 1, 2 or 3 (both)  
RESET_O: 1, 2 or 3 - reset direct output 1, 2 or 3 (both)  
JERK: 0 - deactivate, 1 - activate

### p2623[0...n] EPOS traversing block task mode

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Traversing blocks |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:**  n defined by: p2615 |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 65535 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the influence of the task for the traversing block.  
Value = 0000 cccc bbbb aaaa  
cccc: Positioning mode  
cccc = 0000 --&gt; ABSOLUTE  
cccc = 0001 --&gt; RELATIVE  
cccc = 0010 --&gt; ABS_POS (only for a rotary axis with modulo correction)  
cccc = 0011 --&gt; ABS_NEG (only for a rotary axis with modulo correction)  
bbbb: Progression condition  
bbbb = 0000 --&gt; END  
bbbb = 0001 --&gt; CONTINUE_WITH_STOP  
bbbb = 0010 --&gt; CONTINUE_FLYING  
bbbb = 0011 --&gt; CONTINUE_EXTERNAL  
bbbb = 0100 --&gt; CONTINUE_EXTERNAL_WAIT  
bbbb = 0101 --&gt; CONTINUE_EXTERNAL_ALARM  
aaaa: IDs  
aaaa = 000x --&gt; show/hide block (x = 0: show, x = 1: hide)

**Dependency:** 
  
The number of indices depends on p2615.  
See also:
p2615, p2616, p2617, p2618, p2619, p2620, p2621, p2622

### c2625 EPOS traversing block selection bit 0

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN, S200 Basic PTI, S200 PN |  |  |
| **Data type:**Unsigned8 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Traversing blocks |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink binary |  |  |
| **Factory interconnection:** | **Fixed value:** |  |
| not interconnected | 0 |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal to select the traversing block, bit 0.

**Dependency:** 
  
Parameters c2625, c2626, c2627, c2628 and c2629 are used to select one of the maximum
64 traversing blocks.  
See also:
c2626, c2627, c2628, c2629

### c2626 EPOS traversing block selection bit 1

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN, S200 Basic PTI, S200 PN |  |  |
| **Data type:**Unsigned8 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Traversing blocks |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink binary |  |  |
| **Factory interconnection:** | **Fixed value:** |  |
| not interconnected | 0 |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal to select the traversing block, bit 1.

**Dependency:** 
  
Parameters c2625, c2626, c2627, c2628 and c2629 are used to select one of the maximum
64 traversing blocks.  
See also:
c2625, c2627, c2628, c2629

### c2627 EPOS traversing block selection bit 2

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN, S200 Basic PTI, S200 PN |  |  |
| **Data type:**Unsigned8 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Traversing blocks |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink binary |  |  |
| **Factory interconnection:** | **Fixed value:** |  |
| not interconnected | 0 |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal to select the traversing block, bit 2.

**Dependency:** 
  
Parameters c2625, c2626, c2627, c2628 and c2629 are used to select one of the maximum
64 traversing blocks.  
See also:
c2625, c2626, c2628, c2629

### c2628 EPOS traversing block selection bit 3

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Traversing blocks |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink binary |  |  |
| **Factory interconnection:** | **Fixed value:** |  |
| not interconnected | 0 |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal to select the traversing block, bit 3.

**Dependency:** 
  
Parameters c2625, c2626, c2627, c2628 and c2629 are used to select one of the maximum
64 traversing blocks.  
See also:
c2625, c2626, c2627, c2629

### c2629 EPOS traversing block selection bit 4

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Traversing blocks |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink binary |  |  |
| **Factory interconnection:** | **Fixed value:** |  |
| not interconnected | 0 |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal to select the traversing block, bit 4.

**Dependency:** 
  
Parameters c2625, c2626, c2627, c2628 and c2629 are used to select one of the maximum
64 traversing blocks.  
See also:
c2625, c2626, c2627, c2628

### c2631 EPOS activate traversing task (0 -> 1)

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Traversing blocks |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink binary |  |  |
| **Factory interconnection:** | **Fixed value:** |  |
| not interconnected | 0 |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal for "Activate traversing task".  
c2631 = 0/1 signal  
The traversing task, selected using c2625 ... c2629, is started.

**Dependency:** 
  
See also:
c2625, c2626, c2627, c2628, c2629, c2640, c2641

**Notice:** 
  
The parameter may be protected as a result of r0922 and cannot be changed.

**Note:** 
  
To start a traversing block, the axis must be referenced (r2684.11 = 1).  
The status signal r2684.12 = 0/1 signal is used for acknowledgment.  
A traversing task can be influenced using the following signals:  
- Intermediate stop via c2640.  
- Reject traversing task via c2641.

### p2632 EPOS external block change evaluation

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Traversing blocks |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 1 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the mode to evaluate "external block change".

**Value:** 
  
0:
External block change via a measuring probe  
1:
External block change via c2633

**Dependency:** 
  
See also:
p2623, c2633, r2677, r2678

**Note:** 
  
In the mode "external block change via measuring probe" (p2632 = 0), the following
applies:  
When starting a traversing block with the block change enable CONTINUE_EXTERNAL, CONTINUE_EXTERNAL_WAIT
and CONTINUE_EXTERNAL_ALARM, an activated "passive homing" is interrupted.  
After ending the block, "Passive homing" must be reactivated using a 0/1 edge in c2595.

### c2633 EPOS external block change (0 -> 1)

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Traversing blocks |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink binary |  |  |
| **Factory interconnection:** | **Fixed value:** |  |
| not interconnected | 0 |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal for the "External block change".  
c2633 = 0/1 signal

**Dependency:** 
  
The evaluation of the signal is only active p2632 = 1.  
See also:
p2623, p2632, c2640, c2641, r2677, r2678

**Notice:** 
  
The parameter may be protected as a result of r0922 and cannot be changed.

**Note:** 
  
A 0/1 edge initiates a flying block change in the subsequent traversing block.  
When the external block change is identified, the actual position is saved in r2678.  
A traversing task can be influenced using the following signals:  
- Intermediate stop via c2640.  
- Reject traversing task via c2641.

### p2634[0] EPOS fixed stop maximum following error

[S200 Basic PN](#p26340-epos-fixed-stop-maximum-following-error-1)

[S200 Basic PN EPOS load side, rotating](#p26340-epos-fixed-stop-maximum-following-error-2)

#### p2634[0] EPOS fixed stop maximum following error

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Traversing blocks |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.0000 [mm] | 2147482752.0000 [mm] | [0] 1.0000 [mm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the following error to detect the "fixed stop reached" state (r2526.4).

**Dependency:** 
  
See also:
r2526, p2621, r2675

**Note:** 
  
The state "fixed stop reached" is detected if the following error exceeds the theoretically
calculated following error value by p2634.

#### p2634[0] EPOS fixed stop maximum following error

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN (EPOS load side, rotating), S200 Basic PTI (EPOS load side, rotating), S200 PN (EPOS load side, rotating), S200 PTI (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Traversing blocks |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.0000 [°] | 2147482752.0000 [°] | [0] 36.0000 [°] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the following error to detect the "fixed stop reached" state (r2526.4).

**Dependency:** 
  
See also:
r2526, p2621, r2675

**Note:** 
  
The state "fixed stop reached" is detected if the following error exceeds the theoretically
calculated following error value by p2634.

### p2635 EPOS fixed stop monitoring window

[S200 Basic PN](#p2635-epos-fixed-stop-monitoring-window-1)

[S200 Basic PN EPOS load side, rotating](#p2635-epos-fixed-stop-monitoring-window-2)

#### p2635 EPOS fixed stop monitoring window

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Traversing blocks |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.0000 [mm] | 2147482752.0000 [mm] | [0] 0.1250 [mm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the monitoring window of the actual position after the fixed stop is reached.

**Dependency:** 
  
See also:
r2526, r2683

**Note:** 
  
If, after the fixed stop is reached, the end stop shifts in either the positive or
negative direction by more than the value set here, then r2526.5 is set to 1 and an
appropriate message is output.

#### p2635 EPOS fixed stop monitoring window

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN (EPOS load side, rotating), S200 Basic PTI (EPOS load side, rotating), S200 PN (EPOS load side, rotating), S200 PTI (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Traversing blocks |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.0000 [°] | 2147482752.0000 [°] | [0] 3.6000 [°] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the monitoring window of the actual position after the fixed stop is reached.

**Dependency:** 
  
See also:
r2526, r2683

**Note:** 
  
If, after the fixed stop is reached, the end stop shifts in either the positive or
negative direction by more than the value set here, then r2526.5 is set to 1 and an
appropriate message is output.

### c2640 EPOS intermediate stop (0 signal)

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Traversing blocks, Direct setpoint input (MDI) |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink binary |  |  |
| **Factory interconnection:** | **Fixed value:** |  |
| not interconnected | 0 |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal for "No intermediate stop/intermediate stop".  
1 signal: No intermediate stop  
0 signal: Intermediate stop.

**Dependency:** 
  
See also:
c2631, c2641, c2647, c2649

**Caution:** 
  
For c2649 = 1 signal, the following applies:  
Motion starts without any explicit control signal.

**Notice:** 
  
The parameter may be protected as a result of r0922 and cannot be changed.

**Note:** 
  
This signal is only effective in the modes "traversing blocks" and "direct setpoint
input/MDI".  
When the intermediate stop is activated, then the axis brakes with the parameterized
deceleration (p2620 or c2645).

### c2641 EPOS reject traversing task (0 signal)

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Traversing blocks, Direct setpoint input (MDI) |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink binary |  |  |
| **Factory interconnection:** | **Fixed value:** |  |
| not interconnected | 0 |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal for "Do not reject traversing task/reject traversing task".  
1 signal: Do not reject traversing task.  
0 signal: Reject traversing task

**Dependency:** 
  
See also:
c2631, c2640, c2647, c2649

**Caution:** 
  
For c2649 = 1 signal, the following applies:  
Motion starts without any explicit control signal.

**Notice:** 
  
The parameter may be protected as a result of r0922 and cannot be changed.

**Note:** 
  
This signal is only effective in the modes "traversing blocks" and "direct setpoint
input/MDI".  
When activating reject traversing tasks, then the axis brakes with the maximum deceleration
(p2573).

### c2642 EPOS direct setpoint input/MDI position setpoint

[S200 Basic PN](#c2642-epos-direct-setpoint-inputmdi-position-setpoint-1)

[S200 Basic PN EPOS load side, rotating](#c2642-epos-direct-setpoint-inputmdi-position-setpoint-2)

#### c2642 EPOS direct setpoint input/MDI position setpoint

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Direct setpoint input (MDI) |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Sink numeric |  | **Scaling:** - |
| **Factory interconnection:** | **Fixed value:** |  |
| not interconnected | 0.00 [mm] |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal for the position setpoint in the mode "direct setpoint input/MDI".

**Dependency:** 
  
See also:
c2648, c2649, c2650

**Notice:** 
  
The parameter may be protected as a result of r0922 and cannot be changed.

**Note:** 
  
Depending on c2649, the position setpoint is either transferred continuously or edge-triggered.  
The position setpoint input is interpreted as length unit [LU].

#### c2642 EPOS direct setpoint input/MDI position setpoint

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN (EPOS load side, rotating), S200 Basic PTI (EPOS load side, rotating), S200 PN (EPOS load side, rotating), S200 PTI (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Direct setpoint input (MDI) |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Sink numeric |  | **Scaling:** - |
| **Factory interconnection:** | **Fixed value:** |  |
| not interconnected | 0.00 [°] |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal for the position setpoint in the mode "direct setpoint input/MDI".

**Dependency:** 
  
See also:
c2648, c2649, c2650

**Notice:** 
  
The parameter may be protected as a result of r0922 and cannot be changed.

**Note:** 
  
Depending on c2649, the position setpoint is either transferred continuously or edge-triggered.  
The position setpoint input is interpreted as length unit [LU].

### c2643 EPOS direct setpoint input/MDI velocity setpoint

[S200 Basic PN](#c2643-epos-direct-setpoint-inputmdi-velocity-setpoint-1)

[S200 Basic PN EPOS load side, rotating](#c2643-epos-direct-setpoint-inputmdi-velocity-setpoint-2)

#### c2643 EPOS direct setpoint input/MDI velocity setpoint

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Direct setpoint input (MDI) |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm/s | **Unit group:** 11_3 | **Unit selection:** p2497 |
| **Type of signal interconnection:** Sink numeric |  | **Scaling:** - |
| **Factory interconnection:** | **Fixed value:** |  |
| not interconnected | 100.00 [mm/s] |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal for the velocity setpoint in the mode "Direct setpoint input/MDI".

**Dependency:** 
  
See also:
c2649, c2650

**Notice:** 
  
The parameter may be protected as a result of r0922 and cannot be changed.

**Note:** 
  
Depending on c2649, the velocity setpoint is either transferred continuously or edge-triggered.  
The velocity setpoint input is interpreted as [1000 LU/min].

#### c2643 EPOS direct setpoint input/MDI velocity setpoint

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN (EPOS load side, rotating), S200 Basic PTI (EPOS load side, rotating), S200 PN (EPOS load side, rotating), S200 PTI (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Direct setpoint input (MDI) |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** °/s | **Unit group:** 11_4 | **Unit selection:** p2497 |
| **Type of signal interconnection:** Sink numeric |  | **Scaling:** - |
| **Factory interconnection:** | **Fixed value:** |  |
| not interconnected | 3600.00 [°/s] |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal for the velocity setpoint in the mode "Direct setpoint input/MDI".

**Dependency:** 
  
See also:
c2649, c2650

**Notice:** 
  
The parameter may be protected as a result of r0922 and cannot be changed.

**Note:** 
  
Depending on c2649, the velocity setpoint is either transferred continuously or edge-triggered.  
The velocity setpoint input is interpreted as [1000 LU/min].

### c2644 EPOS direct setpoint input/MDI acceleration override

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Direct setpoint input (MDI) |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** % | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink numeric |  | **Scaling:** PERCENT |
| **Factory interconnection:** | **Fixed value:** |  |
| not interconnected | 100.00 [%] |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal for acceleration override in the operating mode "direct setpoint input/MDI".

**Dependency:** 
  
See also:
c2649, c2650, c11560

**Notice:** 
  
The parameter may be protected as a result of r0922 and cannot be changed.

**Note:** 
  
Depending on c2649, the acceleration override is either transferred continuously or
edge-triggered.  
The signal value 4000 hex (16384 dec) corresponds to 100 %.

### c2645 EPOS direct setpoint input/MDI deceleration override

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Traversing blocks |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** % | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink numeric |  | **Scaling:** PERCENT |
| **Factory interconnection:** | **Fixed value:** |  |
| not interconnected | 100.00 [%] |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal for the deceleration override in the operating mode "Direct setpoint input/MDI".

**Dependency:** 
  
See also:
c2649, c2650, c11561

**Notice:** 
  
If, when calculating the traversing profile, it is identified that the target position
with the programmed deceleration override cannot be reached without reversing the
direction, then when accepting the dynamic values, the larger deceleration override
is accepted and becomes effective.  
The parameter may be protected as a result of r0922 and cannot be changed.

**Note:** 
  
Depending on c2649, the deceleration override is either transferred continuously or
edge-triggered.  
The signal value 4000 hex (16384 dec) corresponds to 100 %.

### c2646 EPOS velocity override

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Jog, Homing, Traversing blocks, Direct setpoint input (MDI) |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** % | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink numeric |  | **Scaling:** PERCENT |
| **Factory interconnection:** | **Fixed value:** |  |
| not interconnected | 100.00 [%] |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal for the velocity override.  
This velocity override is effective in the following operating modes "Direct setpoint
input/MDI", "Traversing blocks", "Jogging" and "Active homing" (when approaching the
reference cam).

**Dependency:** 
  
See also:
p2571, p2585, p2586, p2605, p2618, c2643, r2681

**Notice:** 
  
The parameter may be protected as a result of r0922 and cannot be changed.

**Note:** 
  
The effective override (r2681) can differ from the specified override due to limits
(e.g. maximum velocity).

### c2647 EPOS direct setpoint input/MDI selection

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Direct setpoint input (MDI) |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink binary |  |  |
| **Factory interconnection:** | **Fixed value:** |  |
| not interconnected | 0 |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal to select operating mode "Direct setpoint input/MDI".

**Dependency:** 
  
See also:
c2640, c2641, c2642, c2643, c2644, c2645, c2646, c2648, c2649, c2650, c2651, c2652,
c2653

**Note:** 
  
In this mode, using c2653, a flying changeover can be made between setting-up and
positioning.  
In this mode, even if the axis is not referenced (r2684.11 = 0) relative positioning
is possible.

### c2648 EPOS direct setpoint input/MDI positioning type

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Direct setpoint input (MDI) |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink binary |  |  |
| **Factory interconnection:** | **Fixed value:** |  |
| not interconnected | 0 |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal for the positioning type in mode "Direct setpoint input/MDI".  
1 signal: Absolute positioning is selected.  
0 signal: Relative positioning is selected.

**Dependency:** 
  
See also:
c2649, c2650, c2654

**Notice:** 
  
Absolute positioning:  
To traverse, the home position must be set (r2684.11 = 1).  
Relative positioning:  
To traverse, "Home position set" is not required.

**Note:** 
  
Depending on c2649, the positioning type is either transferred continuously or edge-triggered.  
This parameter is only evaluated for c2654 = 0.  
This parameter is possibly not evaluated as a result of the selected telegram.

### c2649 EPOS direct setpoint input/MDI transfer type selection

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Direct setpoint input (MDI) |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink binary |  |  |
| **Factory interconnection:** | **Fixed value:** |  |
| not interconnected | 0 |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal to define how values are transferred in operating mode "Direct setpoint input/MDI".  
1 signal: Values are continually transferred (refer to parameter under dependency).  
0 signal: The values are transferred for c2650 = 0/1 signal.

**Dependency:** 
  
See also:
c2642, c2643, c2644, c2645, c2648, c2650, c2651, c2652

**Caution:** 
  
For a 1 signal, the following applies:  
Motion starts without any explicit control signal.

**Note:** 
  
Parameter c2649 can only be changed when r0922 = 999.

### c2650 EPOS direct setpoint input/MDI setpoint acceptance edge

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Direct setpoint input (MDI) |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink binary |  |  |
| **Factory interconnection:** | **Fixed value:** |  |
| not interconnected | 0 |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal to accept the values for edge-triggered selection (c2649 = 0 signal) in the
operating mode "Direct setpoint input/MDI".  
c2650 = 0/1 signal and c2649 = 0 signal  
Values are accepted, edge-triggered (refer to parameter under dependency).

**Dependency:** 
  
See also:
c2640, c2641, c2642, c2643, c2644, c2645, c2648, c2649, c2651, c2652, r2684

**Notice:** 
  
The parameter may be protected as a result of r0922 and cannot be changed.

**Note:** 
  
The status signal r2684.12 = 0/1 signal is used for acknowledgment.  
The operating mode "direct setpoint input/MDI" can be influenced via the following
signals:  
- Intermediate stop via c2640.  
- Reject traversing task via c2641.

### c2651 EPOS direct setpoint input/MDI direction selection, positive

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Direct setpoint input (MDI) |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink binary |  |  |
| **Factory interconnection:** | **Fixed value:** |  |
| not interconnected | 0 |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal for the positive direction selection in operating mode "Direct setpoint input/MDI".

**Dependency:** 
  
See also:
p2576, c2648, c2649, c2650, c2652, c2653, c2654

**Note:** 
  
For "setting up" (c2653 = 1 signal), the following applies:  
- The traversing direction can be specified using this parameter.  
- If both directions (c2651, c2652) are selected, then the axis remains stationary
(zero speed).  
- If both directions (c2651, c2652) are deselected, then the axis remains stationary
(zero speed).  
For "Positioning" (c2653 = 0 signal), the following applies:  
Using parameters c2651 and c2652, when the modulo correction (c2577 = 1 signal) is
activated and absolute positioning (c2648 = 1 signal), the travel direction is specified
as follows:  
c2651 / c2652  
0 signal / 0 signal: Absolute positioning through the shortest distance.  
1 signal / 0 signal: Absolute positioning in the positive direction.  
0 signal / 1 signal: Absolute positioning in the negative direction.  
1 signal / 1 signal: Absolute positioning through the shortest distance.

### c2652 EPOS direct setpoint input/MDI direction selection negative

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Direct setpoint input (MDI) |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink binary |  |  |
| **Factory interconnection:** | **Fixed value:** |  |
| not interconnected | 0 |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
The signal for the negative direction selection in the operating mode "Direct setpoint
input/MDI".

**Dependency:** 
  
See also:
p2576, c2648, c2649, c2650, c2651, c2653, c2654

**Note:** 
  
For "setting up" (c2653 = 1 signal), the following applies:  
- The travel direction is specified using this signal.  
- If both directions (c2651, c2652) are selected, then the axis remains stationary
(zero speed).  
- If both directions (c2651, c2652) are deselected, then the axis remains stationary
(zero speed).  
For "Positioning" (c2653 = 0 signal), the following applies:  
Using c2651 and c2652, when the modulo correction (c2577 = 1 signal) is activated
and absolute positioning (c2648 = 1 signal), the travel direction can be specified
as follows:  
c2651 / c2652  
0 signal / 0 signal: Absolute positioning through the shortest distance.  
1 signal / 0 signal: Absolute positioning in the positive direction.  
0 signal / 1 signal: Absolute positioning in the negative direction.  
1 signal / 1 signal: Absolute positioning through the shortest distance.

### c2653 EPOS direct setpoint input/MDI setting-up selection

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Direct setpoint input (MDI) |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink binary |  |  |
| **Factory interconnection:** | **Fixed value:** |  |
| not interconnected | 0 |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal for setting-up in operating mode "Direct setpoint input/MDI".  
1 signal: Setting-up selected.  
0 signal: Positioning selected.

**Dependency:** 
  
See also:
c2651, c2652

**Note:** 
  
In the operating mode "direct setpoint input/MDI", it is possible to make a flying
changeover between setting-up and positioning.  
For "setting up" (c2653 = 1 signal), the following applies:  
A traversing direction must be selected using parameters c2651 and c2652.

### c2654 EPOS direct setpoint input/MDI mode adaptation

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Direct setpoint input (MDI) |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink numeric |  | **Scaling:** - |
| **Factory interconnection:** | **Fixed value:** |  |
| not interconnected | 0 |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal of the MDI mode via PROFIBUS telegram 110 in operating mode "direct setpoint
input/MDI".  
c2654 = 0: Signals are evaluated.  
c2654 &gt; 0: Signals are not evaluated.  
The evaluation involves the following signals:  
- c2648 (positioning type)  
- c2651 (positive direction selection)  
- c2652 (negative direction selection)  
In this case, the following definitions apply:  
Signal via c2654 = xx0x hex -&gt; absolute  
Signal via c2654 = xx1x hex -&gt; relative  
Signal via c2654 = xx2x hex -&gt; abs_pos (only for modulo correction)  
Signal via c2654 = xx3x hex -&gt; abs_neg (only for modulo correction)

**Dependency:** 
  
See also:
c2648, c2651, c2652

### c2655[0...1] EPOS select tracking mode

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Basic positioner |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink binary |  |  |
| **Factory interconnection:** | **Fixed value:** |  |
| [0] not interconnected | 1 |  |
| [1] 2526.7 | 1 |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal to select tracking operation.  
c2655[0] or c2655[1] = 1 signal  
Tracking mode after withdrawing the enable signal from EPOS (c2656 = 0 signal).  
c2655[0] and c2655[1] = 0 signal  
No tracking mode after withdrawing the enable signal from EPOS (c2656 = 0 signal).

**Notice:** 
  
The parameter may be protected as a result of r0922 and cannot be changed.

**Note:** 
  
For the following events, independent of the signal that is present, tracking mode
is selected:  
- After booting.  
- After a 0/1 signal at c2658 (EPOS position actual value, valid feedback signal).  
- While a fault is present.

### r2665 EPOS position setpoint

[S200 Basic PN](#r2665-epos-position-setpoint-1)

[S200 Basic PN EPOS load side, rotating](#r2665-epos-position-setpoint-2)

#### r2665 EPOS position setpoint

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Parameter group:** Jog, Homing, Traversing blocks, Direct setpoint input (MDI) |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the actual absolute position setpoint.

**Dependency:** 
  
See also:
c2530

**Note:** 
  
As default, c2530 is interconnected with r2665.

#### r2665 EPOS position setpoint

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN (EPOS load side, rotating), S200 Basic PTI (EPOS load side, rotating), S200 PN (EPOS load side, rotating), S200 PTI (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Parameter group:** Jog, Homing, Traversing blocks, Direct setpoint input (MDI) |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the actual absolute position setpoint.

**Dependency:** 
  
See also:
c2530

**Note:** 
  
As default, c2530 is interconnected with r2665.

### r2666 EPOS velocity setpoint

[S200 Basic PN](#r2666-epos-velocity-setpoint-1)

[S200 Basic PN EPOS load side, rotating](#r2666-epos-velocity-setpoint-2)

#### r2666 EPOS velocity setpoint

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Parameter group:** Jog, Homing, Traversing blocks, Direct setpoint input (MDI) |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm/s | **Unit group:** 11_3 | **Unit selection:** p2497 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the actual velocity setpoint.

**Dependency:** 
  
See also:
c2531

**Note:** 
  
As default, c2531 is interconnected with r2666.

#### r2666 EPOS velocity setpoint

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN (EPOS load side, rotating), S200 Basic PTI (EPOS load side, rotating), S200 PN (EPOS load side, rotating), S200 PTI (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Parameter group:** Jog, Homing, Traversing blocks, Direct setpoint input (MDI) |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** °/s | **Unit group:** 11_4 | **Unit selection:** p2497 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the actual velocity setpoint.

**Dependency:** 
  
See also:
c2531

**Note:** 
  
As default, c2531 is interconnected with r2666.

### r2669.0...5 EPOS actual operating mode

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Parameter group:** Jog, Homing, Traversing blocks, Direct setpoint input (MDI) |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source binary/numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the actual active operating mode.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Jog operating mode | Not active | Active | - |
| 01 | Operating mode active homing | Not active | Active | - |
| 02 | Operating mode traversing blocks | Not active | Active | - |
| 03 | Operating mode positioning for direct setpoint input / MDI | Not active | Active | - |
| 04 | Operating mode setting up for direct setpoint input / MDI | Not active | Active | - |
| 05 | Option passive homing | Not active | Active | - |

**Dependency:** 
  
See also:
c2589, c2590, c2595, c2631, c2647, c2653

### r2670.0...15 EPOS status word active traversing block

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Parameter group:** Traversing blocks |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source binary/numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the status word for the active traversing block.  
r2670.0: Active traversing block, bit 0  
...  
r2670.5: Active traversing block, bit 5  
r2670.15: MDI active

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Active traversing block bit 0 | Not active | Active | - |
| 01 | Active traversing block bit 1 | Not active | Active | - |
| 02 | Active traversing block bit 2 | Not active | Active | - |
| 03 | Active traversing block bit 3 | Not active | Active | - |
| 04 | Active traversing block bit 4 | Not active | Active | - |
| 05 | Active traversing block bit 5 | Not active | Active | - |
| 15 | MDI active | Not active | Active | - |

**Dependency:** 
  
See also:
c2631, c2647

**Note:** 
  
For bit 00 ... 05:  
Displays the active traversing block in the traversing blocks operating mode.  
For bit 15:  
For a 1 signal, the operating mode - direct setpoint input/MDI - is active

### r2671 EPOS actual position setpoint

[S200 Basic PN](#r2671-epos-actual-position-setpoint-1)

[S200 Basic PN EPOS load side, rotating](#r2671-epos-actual-position-setpoint-2)

#### r2671 EPOS actual position setpoint

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Parameter group:** Jog, Traversing blocks, Direct setpoint input (MDI) |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the position setpoint presently being processed.

**Note:** 
  
A position of 0 is displayed for non position-related tasks (e.g. ENDLESS_POS, ENDLESS_NEG).

#### r2671 EPOS actual position setpoint

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN (EPOS load side, rotating), S200 Basic PTI (EPOS load side, rotating), S200 PN (EPOS load side, rotating), S200 PTI (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Parameter group:** Jog, Traversing blocks, Direct setpoint input (MDI) |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the position setpoint presently being processed.

**Note:** 
  
A position of 0 is displayed for non position-related tasks (e.g. ENDLESS_POS, ENDLESS_NEG).

### r2672 EPOS actual velocity setpoint

[S200 Basic PN](#r2672-epos-actual-velocity-setpoint-1)

[S200 Basic PN EPOS load side, rotating](#r2672-epos-actual-velocity-setpoint-2)

#### r2672 EPOS actual velocity setpoint

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Parameter group:** Jog, Homing, Traversing blocks, Direct setpoint input (MDI) |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm/s | **Unit group:** 11_3 | **Unit selection:** p2497 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the velocity setpoint presently being processed.

#### r2672 EPOS actual velocity setpoint

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN (EPOS load side, rotating), S200 Basic PTI (EPOS load side, rotating), S200 PN (EPOS load side, rotating), S200 PTI (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Parameter group:** Jog, Homing, Traversing blocks, Direct setpoint input (MDI) |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** °/s | **Unit group:** 11_4 | **Unit selection:** p2497 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the velocity setpoint presently being processed.

### r2673 EPOS actual acceleration override

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Parameter group:** Jog, Traversing blocks, Direct setpoint input (MDI) |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** % | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the acceleration override presently being processed.

**Note:** 
  
An override of 100% is effective in the "Jogging" and "Active homing" operating modes.

### r2674 EPOS actual deceleration override

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Parameter group:** Jog, Traversing blocks, Direct setpoint input (MDI) |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** % | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the deceleration override presently being processed.

**Note:** 
  
An override of 100% is effective in the "Jogging" and "Active homing" operating modes.

### r2675 EPOS actual task

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Parameter group:** Traversing blocks |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Display for the task presently being processed.

**Value:** 
  
0:
Inactive  
1:
POSITIONING  
2:
FIXED STOP  
3:
ENDLESS_POS  
4:
ENDLESS_NEG  
5:
WAITING  
6:
GOTO  
7:
SET_O  
8:
RESET_O  
9:
JERK

**Dependency:** 
  
See also:
p2621

### r2676 EPOS actual task parameter

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer32 | **Visible in:**Standard display |  |
| **Parameter group:** Traversing blocks |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the task parameter presently being processed in the "traversing blocks" operating
mode.

**Dependency:** 
  
See also:
p2622

**Note:** 
  
The following is displayed depending on the task:  
FIXED STOP: Clamping torque (0 ... 65536 [0.01 Nm]) or clamping force (0 ... 65536
[N])  
WAIT: Wait time [ms]  
GOTO: Block number  
SET_O: 1, 2, 3 --&gt; direct output 1, 2 or 3 (both) is set  
RESET_O: 1, 2, 3 --&gt; direct output 1, 2 or 3 (both) is reset  
JERK: 0 --&gt; deactivate, 1 --&gt; activate

### r2677 EPOS actual task mode

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Standard display |  |
| **Parameter group:** Traversing blocks |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the task mode presently being processed.

**Dependency:** 
  
See also:
p2623

### r2678 EPOS external block change actual position

[S200 Basic PN](#r2678-epos-external-block-change-actual-position-1)

[S200 Basic PN EPOS load side, rotating](#r2678-epos-external-block-change-actual-position-2)

#### r2678 EPOS external block change actual position

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Parameter group:** Traversing blocks, Direct setpoint input (MDI) |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the actual position for the following events:  
- External block change via measuring probe (p2632 = 0, c2661 = 0/1 signal).  
- External block change via c2633 (p2632 = 1, c2633 = 0/1 signal).  
- Activate traversing task (c2631 = 0/1 signal).

**Dependency:** 
  
See also:
c2631, p2632, c2633

#### r2678 EPOS external block change actual position

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN (EPOS load side, rotating), S200 Basic PTI (EPOS load side, rotating), S200 PN (EPOS load side, rotating), S200 PTI (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Parameter group:** Traversing blocks, Direct setpoint input (MDI) |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the actual position for the following events:  
- External block change via measuring probe (p2632 = 0, c2661 = 0/1 signal).  
- External block change via c2633 (p2632 = 1, c2633 = 0/1 signal).  
- Activate traversing task (c2631 = 0/1 signal).

**Dependency:** 
  
See also:
c2631, p2632, c2633

### r2680 EPOS clearance reference cam and zero mark

[S200 Basic PN](#r2680-epos-clearance-reference-cam-and-zero-mark-1)

[S200 Basic PN EPOS load side, rotating](#r2680-epos-clearance-reference-cam-and-zero-mark-2)

#### r2680 EPOS clearance reference cam and zero mark

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Parameter group:** Homing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Display for the distance (clearance) between the reference cam and zero mark.  
The value is determined for active homing.

#### r2680 EPOS clearance reference cam and zero mark

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN (EPOS load side, rotating), S200 Basic PTI (EPOS load side, rotating), S200 PN (EPOS load side, rotating), S200 PTI (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Parameter group:** Homing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Display for the distance (clearance) between the reference cam and zero mark.  
The value is determined for active homing.

### r2681 EPOS velocity override effective

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Parameter group:** Jog, Homing, Traversing blocks, Direct setpoint input (MDI) |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** % | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the actual effective velocity override.

**Dependency:** 
  
See also:
p2571, c2646

**Note:** 
  
The effective override can differ from the specified override due to limits (e.g.
p2571, maximum velocity).

### r2682 EPOS residual distance to go

[S200 Basic PN](#r2682-epos-residual-distance-to-go-1)

[S200 Basic PN EPOS load side, rotating](#r2682-epos-residual-distance-to-go-2)

#### r2682 EPOS residual distance to go

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Parameter group:** Jog, Traversing blocks, Direct setpoint input (MDI) |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the current residual distance.  
The remaining distance is the distance to still to be moved through up to the end
of the actual positioning task.

**Dependency:** 
  
See also:
r2665, r2671, r2678

#### r2682 EPOS residual distance to go

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN (EPOS load side, rotating), S200 Basic PTI (EPOS load side, rotating), S200 PN (EPOS load side, rotating), S200 PTI (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Parameter group:** Jog, Traversing blocks, Direct setpoint input (MDI) |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the current residual distance.  
The remaining distance is the distance to still to be moved through up to the end
of the actual positioning task.

**Dependency:** 
  
See also:
r2665, r2671, r2678

### r2683.0...14 EPOS status word 1

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Standard display |  |
| **Parameter group:** Control/status words, Jog, Homing, Traversing blocks, Direct setpoint input (MDI), Position controller monitoring |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source binary/numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Display for status word 1 of the basic positioner (EPOS).

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Tracking mode active | No | Yes | 3635, 4020 |
| 01 | Speed limiting active | No | Yes | 3630 |
| 02 | Setpoint fixed | No | Yes | 3635 |
| 03 | Set position reached | No | Yes | 3635 |
| 04 | Axis moves forward | No | Yes | 3635 |
| 05 | Axis moves backward | No | Yes | 3635 |
| 06 | Negative software limit switch reached | No | Yes | 3635 |
| 07 | Positive software limit switch reached | No | Yes | 3635 |
| 10 | Direct output 1 via traversing block | No | Yes | 3616 |
| 11 | Direct output 2 via traversing block | No | Yes | 3616 |
| 12 | Fixed stop reached | No | Yes | 3616, 3617 |
| 13 | Fixed stop clamping torque reached | No | Yes | 3616, 3617 |
| 14 | Travel to fixed stop active | No | Yes | 3616, 3617 |

**Dependency:** 
  
See also:
r2684

**Note:** 
  
For bit 02, 04, 05, 06, 07:  
This signals designate the state after jerk limiting.  
For bits 08, 09:  
These signals are generated in function "Closed-loop position control".

### r2684.0...15 EPOS status word 2

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Standard display |  |
| **Parameter group:** Control/status words, Limit, Jog, Homing, Traversing blocks, Direct setpoint input (MDI), Mechanics, Position controller monitoring |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source binary/numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Display for status word 2 of the basic positioner (EPOS).

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Active homing active | Not active | Active | 3612 |
| 01 | Passive homing active | Not active | Active | 3614 |
| 02 | Homing active | Not active | Active | - |
| 03 | Printing mark outside outer window | No | Yes | 3614 |
| 04 | Axis accelerating | No | Yes | 3635 |
| 05 | Axis decelerating | No | Yes | 3635 |
| 06 | Jerk limiting active | No | Yes | 3635 |
| 07 | Activate correction | No | Yes | 3635 |
| 08 | Following error in tolerance | No | Yes | 4025 |
| 09 | Modulo correction active | No | Yes | - |
| 10 | Target position reached | No | Yes | 4020 |
| 11 | Home position set | No | Yes | 3612, 3614, 3630 |
| 12 | Acknowledgment traversing block activated | No | Yes | 3616, 3620 |
| 13 | Positive hardware limit switch reached | No | Yes | 3630 |
| 14 | Negative hardware limit switch reached | No | Yes | 3630 |
| 15 | Traversing command active | No | Yes | 3635 |

**Note:** 
  
For bit 02:  
The "homing active" signal is an OR logic operation of "active homing active" and
"passive homing active"  
For bit 00 ... 07 and 11 ... 14:  
For bit 08:  
The signal is generated in function "Closed-loop position control".

### r2685 EPOS corrective value

[S200 Basic PN](#r2685-epos-corrective-value-1)

[S200 Basic PN EPOS load side, rotating](#r2685-epos-corrective-value-2)

#### r2685 EPOS corrective value

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Parameter group:** Basic positioner |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Display for the correction value of the position actual value.

**Dependency:** 
  
See also:
r2684

**Note:** 
  
Using this value, for example, modulo corrections are carried out.

#### r2685 EPOS corrective value

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN (EPOS load side, rotating), S200 Basic PTI (EPOS load side, rotating), S200 PN (EPOS load side, rotating), S200 PTI (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Parameter group:** Basic positioner |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Display for the correction value of the position actual value.

**Dependency:** 
  
See also:
r2684

**Note:** 
  
Using this value, for example, modulo corrections are carried out.

### r2686[0...1] EPOS torque limiting effective

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Parameter group:** Basic positioner |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** % | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the effective torque limiting.  
r2686[0]:  
Displays the active upper torque limiting when traversing to fixed stop.  
r2686[1]:  
Displays the active lower torque limiting when traversing to fixed stop.

**Index:** 
  
[
0]:
Upper  
[
1]:
Lower

**Dependency:** 
  
See also:
p1520, p1521, r2676

### r2687 EPOS torque setpoint

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Parameter group:** Traversing blocks |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Nm | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the active torque setpoint when reaching the fixed stop.

**Dependency:** 
  
See also:
p1520, p1521, r2676

### p2688 EPOS position feedback signal tolerance window

[S200 Basic PN](#p2688-epos-position-feedback-signal-tolerance-window-1)

[S200 Basic PN EPOS load side, rotating](#p2688-epos-position-feedback-signal-tolerance-window-2)

#### p2688 EPOS position feedback signal tolerance window

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Basic positioner |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.0000 [mm] | 2147482750.0000 [mm] | [0] 0.0500 [mm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the tolerance window for the position feedback signal.  
If, for a positioning operation, the actual value (r2521) lies within this tolerance
window of the target position, then the traversing block number is displayed at connector
output r2689.

**Dependency:** 
  
This parameter is only active when the "Position feedback signal" function is activated
(p2584.0 = 1).  
See also:
p2584, r2689

#### p2688 EPOS position feedback signal tolerance window

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN (EPOS load side, rotating), S200 Basic PTI (EPOS load side, rotating), S200 PN (EPOS load side, rotating), S200 PTI (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Basic positioner |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.0000 [°] | 2147482750.0000 [°] | [0] 1.5000 [°] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the tolerance window for the position feedback signal.  
If, for a positioning operation, the actual value (r2521) lies within this tolerance
window of the target position, then the traversing block number is displayed at connector
output r2689.

**Dependency:** 
  
This parameter is only active when the "Position feedback signal" function is activated
(p2584.0 = 1).  
See also:
p2584, r2689

### r2689[0...1] EPOS position feedback signal display

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Parameter group:** Basic positioner |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the traversing block numbers for bit-coded position feedback whose absolute
target positions lie within the tolerance window around the actual position.

**Index:** 
  
[
0]:
Position feedback signal low  
[
1]:
Position feedback signal high

**Dependency:** 
  
This parameter is only active when the "Position feedback signal" function is activated
(p2584.0 = 1).  
See also:
p2584, p2688

**Note:** 
  
r2689[0]:  
Bit-coded display of traversing block numbers 0 to 31  
r2689[1]:  
Bit-coded display of traversing block numbers 32 to 63

### r2741 LR acceleration precontrol value

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Parameter group:** Position controller |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** rev/s² | **Unit group:** 39_1 | **Unit selection:** p0505 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2007 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the acceleration precontrol value.

**Note:** 
  
The acceleration precontrol value is a derivation of the speed precontrol value with
respect to time.

### r3122[0...63].0...20 Diagnostic attribute fault

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Parameter group:** Faults / alarms |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the diagnostic attribute of the fault which has occurred.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Hardware replacement recommended | No | Yes | - |
| 15 | Message has gone | No | Yes | - |
| 16 | PROFIdrive fault class bit 0 | Low | High | - |
| 17 | PROFIdrive fault class bit 1 | Low | High | - |
| 18 | PROFIdrive fault class bit 2 | Low | High | - |
| 19 | PROFIdrive fault class bit 3 | Low | High | - |
| 20 | PROFIdrive fault class bit 4 | Low | High | - |

**Dependency:** 
  
See also:
r0945, r0947, r0948, r0949, r2109, r2130, r2133, r2136

**Note:** 
  
The buffer parameters are cyclically updated in the background (refer to status signal
in r2139).  
The structure of the fault buffer and the assignment of the indices is shown in r0945.  
For bits 20 ... 16:  
Bits 20, 19, 18, 17, 16 = 0, 0, 0, 0, 0 --&gt; PROFIdrive message class 0: not assigned  
Bits 20, 19, 18, 17, 16 = 0, 0, 0, 0, 1 --&gt; PROFIdrive message class 1: hardware fault/software
error  
Bits 20, 19, 18, 17, 16 = 0, 0, 0, 1, 0 --&gt; PROFIdrive message class 2: line fault  
Bits 20, 19, 18, 17, 16 = 0, 0, 0, 1, 1 --&gt; PROFIdrive message class 3: supply voltage
fault  
Bits 20, 19, 18, 17, 16 = 0, 0, 1, 0, 0 --&gt; PROFIdrive message class 4: DC link fault  
Bits 20, 19, 18, 17, 16 = 0, 0, 1, 0, 1 --&gt; PROFIdrive message class 5: power electronics
faulted  
Bits 20, 19, 18, 17, 16 = 0, 0, 1, 1, 0 --&gt; PROFIdrive message class 6: overtemperature
electronic components  
Bits 20, 19, 18, 17, 16 = 0, 0, 1, 1, 1 --&gt; PROFIdrive message class 7: ground fault/phase
fault detected  
Bits 20, 19, 18, 17, 16 = 0, 1, 0, 0, 0 --&gt; PROFIdrive message class 8: motor overload  
Bits 20, 19, 18, 17, 16 = 0, 1, 0, 0, 1 --&gt; PROFIdrive message class 9: communication
error to the higher-level control  
Bits 20, 19, 18, 17, 16 = 0, 1, 0, 1, 0 --&gt; PROFIdrive message class 10: safe monitoring
channel has identified an error  
Bits 20, 19, 18, 17, 16 = 0, 1, 0, 1, 1 --&gt; PROFIdrive message class 11: incorrect
position actual value/speed actual value or not available  
Bits 20, 19, 18, 17, 16 = 0, 1, 1, 0, 0 --&gt; PROFIdrive message class 12: internal
(DRIVE-CLiQ) communication error  
Bits 20, 19, 18, 17, 16 = 0, 1, 1, 0, 1 --&gt; PROFIdrive message class 13: infeed unit
faulted  
Bits 20, 19, 18, 17, 16 = 0, 1, 1, 1, 0 --&gt; PROFIdrive message class 14: braking controller/Braking
Module faulted  
Bits 20, 19, 18, 17, 16 = 0, 1, 1, 1, 1 --&gt; PROFIdrive message class 15: line filter
faulted  
Bits 20, 19, 18, 17, 16 = 1, 0, 0, 0, 0 --&gt; PROFIdrive message class 16: external
measured value/signal state outside the permissible range  
Bits 20, 19, 18, 17, 16 = 1, 0, 0, 0, 1 --&gt; PROFIdrive message class 17: application/technology
function faulted  
Bits 20, 19, 18, 17, 16 = 1, 0, 0, 1, 0 --&gt; PROFIdrive message class 18: error in
the parameterization/configuration/commissioning sequence  
Bits 20, 19, 18, 17, 16 = 1, 0, 0, 1, 1 --&gt; PROFIdrive message class 19: general drive
fault  
Bits 20, 19, 18, 17, 16 = 0, 1, 1, 0, 0 --&gt; PROFIdrive message class 20: auxiliary
unit faulted

### r3123[0...63].0...20 Diagnostic attribute alarm

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Parameter group:** Faults / alarms |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the diagnostic attribute of the alarm which has occurred.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Hardware replacement recommended | No | Yes | - |
| 11 | Alarm class bit 0 | Low | High | - |
| 12 | Alarm class bit 1 | Low | High | - |
| 13 | Maintenance required | No | Yes | - |
| 14 | Maintenance urgently required | No | Yes | - |
| 15 | Message has gone | No | Yes | - |
| 16 | PROFIdrive fault class bit 0 | Low | High | - |
| 17 | PROFIdrive fault class bit 1 | Low | High | - |
| 18 | PROFIdrive fault class bit 2 | Low | High | - |
| 19 | PROFIdrive fault class bit 3 | Low | High | - |
| 20 | PROFIdrive fault class bit 4 | Low | High | - |

**Dependency:** 
  
See also:
r2122, r2123, r2124, r2125, r2134, r2145, r2146

**Note:** 
  
The buffer parameters are cyclically updated in the background (refer to status signal
in r2139).  
The structure of the alarm buffer and the assignment of the indices is shown in r2122.  
For bit 12, 11:  
These status bits are used for the classification of internal alarm classes and are
intended for diagnostic purposes only on certain automation systems with integrated
SINAMICS functionality.  
For bits 20 ... 16:  
Bits 20, 19, 18, 17, 16 = 0, 0, 0, 0, 0 --&gt; PROFIdrive message class 0: not assigned  
Bits 20, 19, 18, 17, 16 = 0, 0, 0, 0, 1 --&gt; PROFIdrive message class 1: hardware fault/software
error  
Bits 20, 19, 18, 17, 16 = 0, 0, 0, 1, 0 --&gt; PROFIdrive message class 2: line fault  
Bits 20, 19, 18, 17, 16 = 0, 0, 0, 1, 1 --&gt; PROFIdrive message class 3: supply voltage
fault  
Bits 20, 19, 18, 17, 16 = 0, 0, 1, 0, 0 --&gt; PROFIdrive message class 4: DC link fault  
Bits 20, 19, 18, 17, 16 = 0, 0, 1, 0, 1 --&gt; PROFIdrive message class 5: power electronics
faulted  
Bits 20, 19, 18, 17, 16 = 0, 0, 1, 1, 0 --&gt; PROFIdrive message class 6: overtemperature
electronic components  
Bits 20, 19, 18, 17, 16 = 0, 0, 1, 1, 1 --&gt; PROFIdrive message class 7: ground fault/phase
fault detected  
Bits 20, 19, 18, 17, 16 = 0, 1, 0, 0, 0 --&gt; PROFIdrive message class 8: motor overload  
Bits 20, 19, 18, 17, 16 = 0, 1, 0, 0, 1 --&gt; PROFIdrive message class 9: communication
error to the higher-level control  
Bits 20, 19, 18, 17, 16 = 0, 1, 0, 1, 0 --&gt; PROFIdrive message class 10: safe monitoring
channel has identified an error  
Bits 20, 19, 18, 17, 16 = 0, 1, 0, 1, 1 --&gt; PROFIdrive message class 11: incorrect
position actual value/speed actual value or not available  
Bits 20, 19, 18, 17, 16 = 0, 1, 1, 0, 0 --&gt; PROFIdrive message class 12: internal
(DRIVE-CLiQ) communication error  
Bits 20, 19, 18, 17, 16 = 0, 1, 1, 0, 1 --&gt; PROFIdrive message class 13: infeed unit
faulted  
Bits 20, 19, 18, 17, 16 = 0, 1, 1, 1, 0 --&gt; PROFIdrive message class 14: braking controller/Braking
Module faulted  
Bits 20, 19, 18, 17, 16 = 0, 1, 1, 1, 1 --&gt; PROFIdrive message class 15: line filter
faulted  
Bits 20, 19, 18, 17, 16 = 1, 0, 0, 0, 0 --&gt; PROFIdrive message class 16: external
measured value/signal state outside the permissible range  
Bits 20, 19, 18, 17, 16 = 1, 0, 0, 0, 1 --&gt; PROFIdrive message class 17: application/technology
function faulted  
Bits 20, 19, 18, 17, 16 = 1, 0, 0, 1, 0 --&gt; PROFIdrive message class 18: error in
the parameterization/configuration/commissioning sequence  
Bits 20, 19, 18, 17, 16 = 1, 0, 0, 1, 1 --&gt; PROFIdrive message class 19: general drive
fault  
Bits 20, 19, 18, 17, 16 = 0, 1, 1, 0, 0 --&gt; PROFIdrive message class 20: auxiliary
unit faulted

### p3234 Delay line voltage failure detection

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Load torque monitoring |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 [ms] | 100 [ms] | [0] 10 [ms] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the time delay for detecting the line voltage failure.  
The function must be activated via p2149.16.

**Dependency:** 
  
See also:
p2149  
See also:
F30265

### r3988 Final boot state

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Extended display |  |
| **Parameter group:** System identification |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the final boot states.  
001 - Software error  
200 - Carry out first commissioning  
250 - Topology error (check the connected hardware)  
800 - Ready  
The following options are available to reach the "Ready" state:  
- Check the project and load again.  
- Restore factory setting.  
- Check the hardware.  
- Carry out a POWER ON (switch-off/switch-on).

### r4479 PTO diagnostics position actual value

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer32 | **Visible in:**Standard display |  |
| **Parameter group:** Pulse encoder emulation |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Display and numerical signal source for the PTO position actual value.

### p5271[0].0...7 Online / One Button Tuning configuration

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| - | - | [0] 0000 1100 bin |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the configuration for online tuning / One Button Tuning.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | PD controller for large load moments of inertia | No | Yes | - |
| 01 | Reduce gain at low speeds | No | Yes | - |
| 02 | Load adaptation Kp | No | Yes | 5045 |
| 03 | Setting the speed precontrol | No | Yes | 5045 |
| 04 | Setting the torque precontrol | No | Yes | 5045 |
| 05 | Setting the maximum acceleration for the basic positioner | No | Yes | 5045 |
| 06 | Do not change Kp | No | Yes | - |
| 07 | Setting the voltage precontrol | No | Yes | - |

**Dependency:** 
  
See also:
p5272, r5274, p5275

**Note:** 
  
For bit 00:  
For significant differences between the motor moment of inertia and load moment of
inertia - or for a low controller dynamic response - the P controller in the position
control loop is transformed into a PD controller. As a consequence, the dynamic performance
of the position controller is increased.  
This function should only be set when the speed precontrol (bit 3 = 1) or the torque
precontrol (bit 4 = 1) is active.  
For bit 01:  
At low speeds, the controller gain factors are automatically reduced in order to avoid
noise and oscillation at standstill.  
For bit 02:  
The estimated load moment of inertia is taken into account for the speed controller
gain.  
For bit 03:  
Activates the speed precontrol for the basic positioner (EPOS).  
For bit 04:  
Activation of the torque precontrol for the basic positioner (EPOS); if this is not
active, then the internal drive speed/torque precontrol is parameterized.  
For bit 05:  
The maximum acceleration (p2572) and maximum deceleration (p2573) for the basic positioner
(EPOS) are determined using the estimated moment of inertia. This is only realized
once by setting the bit.  
Prerequisite:  
The drive pulses are inhibited and the moment of inertia was previously determined.  
For bit 06:  
The speed controller gain set in p1460 is not changed when calculating the controller
data.  
For bit 07:  
Activation of the voltage precontrol.

### p5272[0] Online tuning dynamic factor

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** % | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 5.0 [%] | 1000.0 [%] | [0] 100.0 [%] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the dynamic factor for the proportional gain of the speed controller for online
tuning.

**Dependency:** 
  
See also:
p5271, r5274, p5275

**Notice:** 
  
The speed control can become unstable for excessively high values.

**Note:** 
  
The stiffer the mechanical load coupling, the higher the dynamic factor can be set.

### r5274 Online / One Button Tuning dynamic response estimated

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Parameter group:** |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Display and signal source for the estimated dynamic response of the speed control
loop as PT1 time constant for online tuning/One Button Tuning.  
This position controller setting is required if the closed-loop position control is
in an external control system.

**Dependency:** 
  
See also:
p5271, p5272, p5275

### p5275[0] Online / One Button Tuning dynamic response time constant

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.0 [ms] | 60.0 [ms] | [0] 7.5 [ms] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the time constant for the precontrol symmetrization for online tuning / One Button
Tuning.  
As a consequence, the drive is allocated a defined, dynamic response via its precontrol.  
For axes, which must interpolate with one another, the same value must be entered.  
Examples:  
0 ms = travel without following error (Kv factor is infinity)  
5 ms = settling behavior as for PT1 with 5 ms (Kv factor = 12 [1000/min])

**Dependency:** 
  
See also:
p5271, p5272, r5274

**Note:** 
  
This time constant is only effective if p5302.7 is set = 1.  
Otherwise, the precontrol symmetrization is adapted to the estimated dynamic response,
therefore setting positioning without any overshoot.

### r5276[0] Online / One Button Tuning maximum Kv factor estimated

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Parameter group:** |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** 1000 rpm | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the estimated maximum position controller gain for online tuning/One Button
Tuning.

**Dependency:** 
  
See also:
p5271, p5272, p5275

**Warning:** 
  
The calculation assumes that the DSC is activated in the drive and is controlled on
the motor measuring system.  
If this is not the case, then excessively high values are displayed.  
The value that is displayed does not take into account low-frequency resonance effects
in the drive train. If necessary, the value must be significantly reduced.

**Note:** 
  
The value for the closed-loop position control is required by a higher-level control
system.

### r5277[0] Online/One Button Tuning precontrol symmetrizing time estimated

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Parameter group:** |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the estimated time constant for symmetrization of the speed precontrol.  
This is required to symmetrize the position controller for online tuning / One Button
Tuning if the position control is realized in an external control system.

**Dependency:** 
  
See also:
p5271, p5272, p5275

**Warning:** 
  
The calculation assumes that the DSC is activated in the drive and is controlled on
the motor measuring system.  
If this is not the case, then the time is not correctly calculated.

### p5291.0...16 FFT tuning configuration

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| - | - | [0] 0000 0000 0000 0000 0000 0000 0011 1001 bin |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the configuration for the "FFT tuning" function.  
This function is used for One Button Tuning (p5300 = 1).

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Noise excitation after pulse enable | No | Yes | - |
| 01 | Set current setpoint filter (HF) | No | Yes | - |
| 02 | Set speed controller gain (HF) | No | Yes | - |
| 03 | Length of FFT window bit 0 (LF, HF) | No | Yes | - |
| 04 | Length of FFT window bit 1 (LF, HF) | No | Yes | - |
| 05 | Windowing the time signals using a Hamming window (LF, HF) | No | Yes | - |
| 06 | Measure current controller | No | Yes | - |
| 07 | Bandwidth bit 0 (LF) | No | Yes | - |
| 08 | Bandwidth bit 1 (LF) | No | Yes | - |
| 09 | Bandwidth bit 2 (LF) | No | Yes | - |
| 10 | Measuring periods bit 0 | No | Yes | - |
| 11 | Measuring periods bit 1 | No | Yes | - |
| 12 | Inject noise onto speed setpoint | No | Yes | - |
| 13 | Do not reduce Kp for measurement | No | Yes | - |
| 14 | Set the current setpoint filter with loop compensation | No | Yes | - |
| 16 | Torque in front of the current setpoint filter | No | Yes | - |

**Dependency:** 
  
See also:
r5293, p5296

**Note:** 
  
HF: high frequency  
LF: low frequency  
For bit 00:  
A PRBS signal (pseudo random binary signal) is superimposed on the current setpoint
to be able to better identify the mechanical controlled system.  
For bit 01:  
The identified mechanical resonance points are suppressed using current setpoint filters.  
For bit 02:  
The maximum speed controller gain is determined from the identified mechanical controlled
system.  
For bits 03, 04:  
The measured value buffer length is set using these bits:  
Bit 04 = 0 and bit 03 = 0 -&gt; buffer length = 256  
Bit 04 = 0 and bit 03 = 1 -&gt; buffer length = 512  
Bit 04 = 1 and bit 03 = 0 -&gt; buffer length = 1024  
Bit 04 = 1 and bit 03 = 1 -&gt; buffer length = 2048  
For bit 05:  
A Hamming window is used to filter the measured time signals.  
For bit 06:  
The measurement checks the current controller frequency response and this is taken
into account in the speed controller loop.  
For bits 07, 08, 09:  
The measurement bandwidth is set using these bits:  
Bit 09 = 0, bit 08 = 0, bit 07 = 0 -&gt; bandwidth = 50 Hz  
Bit 09 = 0, bit 08 = 0, bit 07 = 1 -&gt; bandwidth = 100 Hz  
Bit 09 = 0, bit 08 = 1, bit 07 = 0 -&gt; bandwidth = 200 Hz  
Bit 09 = 0, bit 08 = 1, bit 07 = 1 -&gt; bandwidth = 400 Hz  
Bit 09 = 1, bit 08 = 0, bit 07 = 0 -&gt; bandwidth = 800 Hz  
Bit 09 = 1, bit 08 = 0, bit 07 = 1 -&gt; bandwidth = 1600 Hz  
For bits 10, 11:  
Number of measuring periods.  
Bit 11 = 0 and bit 10 = 0 -&gt; number of measurements = 1  
Bit 11 = 0 and bit 10 = 1 -&gt; number of measurements = 2  
Bit 11 = 1 and bit 10 = 0 -&gt; number of measurements = 4  
Bit 11 = 1 and bit 10 = 1 -&gt; number of measurements = 8  
For bit 12:  
The PRBS signal is switched to the speed setpoint (in front of the filter).  
For bit 13:  
The input signal for the torque actual value is taken from in front of the current
setpoints filters.  
For bit 14:  
When the bit is set, a current setpoint filter is used to partially compensate the
mechanical system.  
This is recommended for the following machine attributes:  
- The load moment of inertia is significantly higher than the motor moment of inertia
(e.g. &gt; 6x).  
- The coupling between the machine elements has almost no backlash (no play).  
- The stiffness of the mechanical transmission elements does not change significantly
in the traversing range.

### p5292 FFT tuning dynamic factor

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** % | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 25.0 [%] | 125.0 [%] | [0] 80.0 [%] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the dynamic factor for the proportional gain of the speed controller for FFT
tuning.  
This function is used for One Button Tuning (p5300 = 1).

**Dependency:** 
  
See also:
p5291

### r5293 FFT tuning speed controller P gain identified

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Parameter group:** |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Nms/rad | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the determined proportional gain Kp of the speed controller before FFT tuning.  
This function is used for One Button Tuning (p5300 = 1).

**Dependency:** 
  
See also:
p5291

### p5296[0...2] Controller optimization noise amplitude

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** % | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 1.0 [%] | 300.0 [%] | [0] 10.0 [%] [1] 30.0 [%] [2] 5.0 [%] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
The drive determines the noise amplitude for One Button Tuning and writes the value
to p5296.

**Dependency:** 
  
See also:
p5291

### p5300[0] Autotuning selection

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| -1 | 2 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Setting to activate/deactivate the One Button Tuning function. For p5300 = 1: Function
One Button Tuning is configured using p5271 and p5301.  
If p5300 = 2:  
The "Online tuning" function is configured using p5302.

**Value:** 
  
-1:
Reset controller parameters  
0:
Inactive  
1:
One Button Tuning  
2:
Online tuning

**Dependency:** 
  
The motor must have already been commissioned so that One Button Tuning functions
perfectly.  
The One Button Tuning function is configured using p5271 and p5301. The required dynamic
performance of the control loop is set in p5292. The traversing path for the test
signal is parameterized in p5308.  
Online tuning:  
p5302 configures the "Online tuning" function.  
p5272 if the required dynamic response of the control loops is set.  
Other relevant parameters: p5271, p5275, r5274  
See also:
p5271, p5272, r5274, p5275, p5292, r5293, p5296, p5301, p5302, p5308, p5309

**Caution:** 
  
For some drive trains, the "online tuning" function can result in unstable settings
(motor makes a whistling sound). This is especially the case for high load moments
of inertia, which are coupled to the motor through a low-frequency connection/coupling.
In this case, the value in parameter p5272 must be reduced.

**Note:** 
  
For p5300 = -1:  
Autotuning is deactivated, and p5300 is automatically set to 0. In addition, the default
setting values for the speed and position controller are restored.  
For p5300 = 0:  
Online tuning is inactive.  
To permanently save the values determined for the speed and position controllers,
the parameters must be saved in a non-volatile manner (p0977 = 1 or "copy RAM to ROM").  
For p5300 = 1:  
One Button Tuning is active.  
The moment of inertia is determined once using a test signal. The controller parameters
and current setpoint filters are additionally determined once using a noise signal
as excitation source. The steps to be executed can be configured using p5301.  
If p5300 = 2:  
Online tuning is active.  
The moment of inertia is estimated. The controller parameters are recalculated if
the moment of inertia noticeably changes. The steps to be executed can be configured
using p5302.

## SINAMICS Parameter S200 Basic PN 05301 - 61001

SINAMICS Parameter S200 Basic PN 05301 - 61001

### p5301[0].0...8 One Button Tuning configuration 2

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| - | - | [0] 0000 0000 0000 0111 bin |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Setting the functions for One Button Tuning (p5300 = 1).  
A test signal is required for some functions. To do this, observe parameters p5308
and p5309.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Setting the proportional gain Kp | No | Yes | - |
| 01 | Setting current setpoint filter | No | Yes | - |
| 02 | Estimate moment of inertia | No | Yes | - |
| 08 | Moment of inertia determination from frequency response | No | Yes | - |

**Dependency:** 
  
It is only possible to change the configuration if One Button Tuning is not active
(p5300 = 0).  
See also:
p5292, r5293, p5296, p5300, p5308, p5309

**Note:** 
  
For bit 00:  
The speed controller gain is determined and set using a noise signal.  
For bit 01:  
Possibly required current setpoint filters are determined and set using a noise signal.  
As a consequence, a higher dynamic performance can be achieved in the speed control
loop.  
For bit 02:  
Using this bit, the moment of inertia is determined using a test signal. If this bit
is not set, then the load moment of inertia must be manually set using parameter p1498.
The test signal must have been previously set using parameters p5308 and p5309.  
For bit 08:  
Using this bit, the moment of inertia is determined from the frequency characteristic
using a test signal, and is transferred to p1498. The traversing path must first be
set using parameter p5308.

### p5302[0].2...8 Online tuning configuration

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| - | - | [0] 0000 0000 0000 1100 bin |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Setting the functions for online tuning (p5300 = 2).

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 02 | Estimate moment of inertia | No | Yes | - |
| 03 | Configuring the moment of inertia estimator | Once | Cyclic | - |
| 06 | Activating the current setpoint filter adaptation | No | Yes | - |
| 07 | Activating synchronized axes | No | Yes | - |
| 08 | Moment of inertia determination from frequency response | No | Yes | - |

**Dependency:** 
  
It is only possible to change the configuration if autotuning is not active (p5300
= 0).  
See also:
p5271, p5272, r5274, p5275, p5300

**Caution:** 
  
Please note the general conditions for the moment of inertia estimator, online tuning
as well as adaptive resonance filter in the following reference:  
SINAMICS S120 Function Manual Drive Functions

**Note:** 
  
For bit 00:  
The speed controller gain is determined and set using a noise signal.  
For bit 01:  
Possibly required current setpoint filters are determined and set using a noise signal.  
As a consequence, a higher dynamic performance can be achieved in the speed control
loop.  
For bit 02:  
Using this bit, the moment of inertia is determined using a test signal. If this bit
is not set, then the  
load moment of inertia must be manually set using parameter p1498. The test signal
must be previously set via parameters p5308  
and p5309.  
For bit 08:  
Using this bit, the moment of inertia is determined from the frequency characteristic
using a test signal, and is transferred to p1498.  
The traversing path must first be set using parameter p5308.

### r5306[0].0...14 Autotuning status

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Standard display |  |
| **Parameter group:** |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the status of the auto tuning functions performed - "Online tuning" and "One
Button Tuning".  
The functions can be activated via p5300.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Proportional gain Kp set | No | Yes | - |
| 01 | Current setpoint filter set | No | Yes | - |
| 02 | Moment of inertia estimation carried out | No | Yes | - |
| 04 | Load vibration detection performed | No | Yes | - |
| 05 | Detected load oscillation set | No | Yes | - |
| 06 | Current setpoint filter adaptation active | No | Yes | - |
| 07 | EPOS set | No | Yes | - |
| 12 | Online tuning active | No | Yes | - |
| 13 | One Button Tuning successfully completed | No | Yes | - |
| 14 | Controller parameters reset due to fault | No | Yes | - |

**Dependency:** 
  
See also:
p5300, p5301, p5302

**Note:** 
  
For bit 00 = 1: The speed controller gain was set using One Button Tuning.  
For bit 01 = 1: The current setpoint filter was set using One Button Tuning  
For bit 02 = 1: The moment of inertia was determined.  
For bit 04 = 1: Load oscillation detection was performed using One Button Tuning  
For bit 05 = 1: Detected load oscillation suppression was set using One Button Tuning.  
For bit 06 = 1: Adaptive resonance filters of the online tuning are active.  
For bit 12 = 1: Online tuning is active and modifies the controller.

### p5308[0] One Button Tuning distance limiting

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| -30000 [°] | 30000 [°] | [0] 0 [°] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Setting the distance limiting (permissible traversing range of the motor).  
The traversing range is limited in the positive and negative directions.

**Note:** 
  
A value of 360 degrees corresponds to one motor revolution.  
The position before the pulse enable is used as zero point.

### p5309[0] One Button Tuning test signal duration

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 [ms] | 5000 [ms] | [0] 2000 [ms] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the test signal sequence duration (several acceleration operations).  
This function is used for One Button Tuning (p5300 = 1) to identify the total moment
of inertia of the drive train.

**Dependency:** 
  
See also:
F07093

### p5375[0].0...1 Additional motor overload protection configuration

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Motor temperature |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| - | - | [0] 0000 bin |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the configuration for additional motor overload protection.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Activate monitoring | No | Yes | - |
| 01 | Activation of speed dependency | No | Yes | - |

**Note:** 
  
To comply with standard UL 61800-5-1 Ed. 2, bit 0 and bit 1 must be set.  
These bits activate electronic motor overload protection according to IEC 61800-5-1
Ed. 3 / UL 61800-5-1 Ed. 2, with the emulation of an electronic overload relay, Class
20 and the speed sensitivity.  
For bit 00:  
This bit activates electronic motor overload protection with emulation of an electronic
overload relay, Class 20.  
For bit 01:  
This bit activates the speed dependency of the electronic motor overload protection.
Not active, if bit 00 is also set.

### r8400[0...2] Date

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN, S200 PN |  |  |
| **Data type:**Unsigned16 | **Visible in:**Standard display |  |
| **Parameter group:** Diagnostics general |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the actual date in year, month and day.

**Index:** 
  
[
0]:
Year (YYYY)  
[
1]:
Month (1 ... 12)  
[
2]:
Day (1 ... 31)

**Note:** 
  
The time in r8400 and r8401 is used to display the fault and alarm times.  
Possible date/time setting:  
- Web server (manually)  
- NTP (Network Time Protocol)  
When the converter is switched off, date/time are not updated.  
After the converter has restarted, the date and time that the converter was in a no-current
condition applies.

### r8401[0...2] Time

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN, S200 PN |  |  |
| **Data type:**Unsigned16 | **Visible in:**Standard display |  |
| **Parameter group:** Diagnostics general |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the current time in hours, minutes and seconds.

**Index:** 
  
[
0]:
Hour (0 ... 23)  
[
1]:
Minute (0 ... 59)  
[
2]:
Second (0 ... 59)

**Note:** 
  
The time in r8400 and r8401 is used to display the fault and alarm times.  
The time is displayed in the 24-hour format.  
Possible date/time setting:  
- Web server (manually)  
- NTP (Network Time Protocol)  
When the converter is switched off, date/time are not updated. After power on the
instant of the previous power off is valid.

### r8600[0...20] PROFIdrive PZD receive Float32

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN, S200 PN |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Parameter group:** Configuration |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the PZD (setpoints) in the Float32 format received from the fieldbus controller.

**Index:** 
  
[
0]:
PZD 1 + 2  
[
1]:
PZD 2 + 3  
[
2]:
PZD 3 + 4  
[
3]:
PZD 4 + 5  
[
4]:
PZD 5 + 6  
[
5]:
PZD 6 + 7  
[
6]:
PZD 7 + 8  
[
7]:
PZD 8 + 9  
[
8]:
PZD 9 + 10  
[
9]:
PZD 10 + 11  
[
10]:
PZD 11 + 12  
[
11]:
PZD 12 + 13  
[
12]:
PZD 13 + 14  
[
13]:
PZD 14 + 15  
[
14]:
PZD 15 + 16  
[
15]:
PZD 16 + 17  
[
16]:
PZD 17 + 18  
[
17]:
PZD 18 + 19  
[
18]:
PZD 19 + 20  
[
19]:
PZD 20 + 21  
[
20]:
PZD 21 + 22

### c8601[0...26] PROFIdrive PZD send Float32

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN, S200 PN |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Configuration |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink numeric |  | **Scaling:** - |
| **Factory interconnection:** | **Fixed value:** |  |
| not interconnected | 0.00 |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the PZD (actual values) in the Float32 format that are sent to the fieldbus
controller.

**Index:** 
  
[
0]:
PZD 1 + 2  
[
1]:
PZD 2 + 3  
[
2]:
PZD 3 + 4  
[
3]:
PZD 4 + 5  
[
4]:
PZD 5 + 6  
[
5]:
PZD 6 + 7  
[
6]:
PZD 7 + 8  
[
7]:
PZD 8 + 9  
[
8]:
PZD 9 + 10  
[
9]:
PZD 10 + 11  
[
10]:
PZD 11 + 12  
[
11]:
PZD 12 + 13  
[
12]:
PZD 13 + 14  
[
13]:
PZD 14 + 15  
[
14]:
PZD 15 + 16  
[
15]:
PZD 16 + 17  
[
16]:
PZD 17 + 18  
[
17]:
PZD 18 + 19  
[
18]:
PZD 19 + 20  
[
19]:
PZD 20 + 21  
[
20]:
PZD 21 + 22  
[
21]:
PZD 22 + 23  
[
22]:
PZD 23 + 24  
[
23]:
PZD 24 + 25  
[
24]:
PZD 25 + 26  
[
25]:
PZD 26 + 27  
[
26]:
PZD 27 + 28

### r8936[0...1] PN cyclic connection state

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN, S200 PN |  |  |
| **Data type:**Integer16 | **Visible in:**Extended display |  |
| **Parameter group:** |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the status of the cyclic PROFINET connection.

**Value:** 
  
0:
Canceled  
1:
Not connected  
2:
Connection starts to be established  
3:
Module information expected  
4:
Module information received  
5:
Module address expected  
6:
Module address received  
7:
Parameterization data expected  
8:
Parameterization data received  
9:
Evaluate parameterization data  
10:
Connection being established completion expected  
12:
Configured controller STOP  
13:
Configured controller RUN

**Index:** 
  
[
0]:
Controller 1  
[
1]:
Reserved

**Dependency:** 
  
See also:
r8961

**Note:** 
  
For value = 10:  
If the connection remains in this state, then when using PROFINET IRT the following
can apply:  
- Topology error (incorrect port assignment).  
- Synchronization missing.

### r8937[0...5] PN cyclic connection diagnostics

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN, S200 PN |  |  |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Parameter group:** |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Display to diagnose the cyclic PROFINET connection.

**Index:** 
  
[
0]:
Number of cyclic connections  
[
1]:
Number of send subslots of all connections  
[
2]:
Number of send net data (bytes) of all connections  
[
3]:
Number of receive subslots of all connections  
[
4]:
Number of receive net data (bytes) of all connections  
[
5]:
Connection type (RT, IRT)

**Note:** 
  
The parameter is active when the "PROFINET Device" protocol is selected.  
For index [5]:  
Bit 0 = 1: there is at least one RT connection.  
Bit 1 = 1: there is an IRT connection.

### r8961[0...3] PN controller IP address

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN, S200 PN |  |  |
| **Data type:**Unsigned8 | **Visible in:**Extended display |  |
| **Parameter group:** Configuration |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the IP address of the PROFINET controller.

### c8995[0...3] Ethernet X127 enable

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Configuration |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink binary |  |  |
| **Factory interconnection:** | **Fixed value:** |  |
| [0] not interconnected | 1 |  |
| [1] not interconnected | 1 |  |
| [2] not interconnected | 0 |  |
| [3] not interconnected | 0 |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal to enable the Ethernet interface X127 for applications.

**Index:** 
  
[
0]:
Secure S7 Protocol Startdrive  
[
1]:
Web server HTTPS  
[
2]:
S7 protocol PCS7  
[
3]:
Web server HTTP

**Note:** 
  
The parameter influences the access from applications.  
1 signal:  
Ethernet interface X127 is enabled for access.  
0 signal:  
Ethernet interface X127 is blocked and cannot be accessed.  
The signal is not influenced by restoring the factory settings.

### c8997[0...2] PROFINET X150 enable

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN, S200 PN |  |  |
| **Data type:**Unsigned8 | **Visible in:**Extended display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Configuration |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink binary |  |  |
| **Factory interconnection:** | **Fixed value:** |  |
| [0] not interconnected | 1 |  |
| [1] not interconnected | 1 |  |
| [2] not interconnected | 0 |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal to enable PROFINET interface X150 for applications.

**Index:** 
  
[
0]:
Secure S7 Protocol Startdrive  
[
1]:
Web server HTTPS  
[
2]:
S7 protocol PCS7

**Note:** 
  
The parameter influences the access from applications.  
1 signal:  
PROFINET interface X150 is enabled for access.  
0 signal:  
PROFINET interface X150 is inhibited for access.  
The signal is not influenced by restoring the factory settings.

### r9750[0...63].0...20 SI diagnostic attributes

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the diagnostic attributes of the safety messages that have occurred.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Hardware replacement recommended | No | Yes | - |
| 15 | Message has gone | No | Yes | - |
| 16 | PROFIdrive fault class bit 0 | Low | High | - |
| 17 | PROFIdrive fault class bit 1 | Low | High | - |
| 18 | PROFIdrive fault class bit 2 | Low | High | - |
| 19 | PROFIdrive fault class bit 3 | Low | High | - |
| 20 | PROFIdrive fault class bit 4 | Low | High | - |

**Note:** 
  
The buffer parameters are cyclically updated in the background (refer to status signal
in r2139).  
The structure of the safety message buffer and the assignment of the indices is shown
in r60045.  
For bits 20 ... 16:  
Bits 20, 19, 18, 17, 16 = 0, 0, 0, 0, 0 --&gt; PROFIdrive message class 0: not assigned  
Bit 20, 19, 18, 17, 16 = 0, 0, 0, 0, 1 --&gt; PROFIdrive message class 1: hardware fault/software
error  
Bits 20, 19, 18, 17, 16 = 0, 0, 0, 1, 0 --&gt; PROFIdrive message class 2: line fault  
Bits 20, 19, 18, 17, 16 = 0, 0, 0, 1, 1 --&gt; PROFIdrive message class 3: supply voltage
fault  
Bits 20, 19, 18, 17, 16 = 0, 0, 1, 0, 0 --&gt; PROFIdrive message class 4: DC link fault  
Bits 20, 19, 18, 17, 16 = 0, 0, 1, 0, 1 --&gt; PROFIdrive message class 5: power electronics
faulted  
Bits 20, 19, 18, 17, 16 = 0, 0, 1, 1, 0 --&gt; PROFIdrive message class 6: overtemperature
electronic components  
Bits 20, 19, 18, 17, 16 = 0, 0, 1, 1, 1 --&gt; PROFIdrive message class 7: ground fault/phase
fault detected  
Bits 20, 19, 18, 17, 16 = 0, 1, 0, 0, 0 --&gt; PROFIdrive message class 8: motor overload  
Bits 20, 19, 18, 17, 16 = 0, 1, 0, 0, 1 --&gt; PROFIdrive message class 9: communication
error to the higher-level control  
Bits 20, 19, 18, 17, 16 = 0, 1, 0, 1, 0 --&gt; PROFIdrive message class 10: safe monitoring
channel has identified an error  
Bits 20, 19, 18, 17, 16 = 0, 1, 0, 1, 1 --&gt; PROFIdrive message class 11: incorrect
position actual value/speed actual value or not available  
Bits 20, 19, 18, 17, 16 = 0, 1, 1, 0, 0 --&gt; PROFIdrive message class 12: internal
(DRIVE-CLiQ) communication error  
Bits 20, 19, 18, 17, 16 = 0, 1, 1, 0, 1 --&gt; PROFIdrive message class 13: infeed unit
faulted  
Bits 20, 19, 18, 17, 16 = 0, 1, 1, 1, 0 --&gt; PROFIdrive message class 14: braking controller/Braking
Module faulted  
Bits 20, 19, 18, 17, 16 = 0, 1, 1, 1, 1 --&gt; PROFIdrive message class 15: line filter
faulted  
Bits 20, 19, 18, 17, 16 = 1, 0, 0, 0, 0 --&gt; PROFIdrive message class 16: external
measured value/signal state outside the permissible range  
Bits 20, 19, 18, 17, 16 = 1, 0, 0, 0, 1 --&gt; PROFIdrive message class 17: application/technology
function faulted  
Bits 20, 19, 18, 17, 16 = 1, 0, 0, 1, 0 --&gt; PROFIdrive message class 18: error in
the parameterization/configuration/commissioning sequence  
Bits 20, 19, 18, 17, 16 = 1, 0, 0, 1, 1 --&gt; PROFIdrive message class 19: general drive
fault  
Bits 20, 19, 18, 17, 16 = 0, 1, 1, 0, 0 --&gt; PROFIdrive message class 20: auxiliary
unit faulted

### c11500[0...3] LR initiate absolute encoder adjustment

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Position control |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink binary |  |  |
| **Factory interconnection:** | **Fixed value:** |  |
| not interconnected | 0 |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Initiate adjustment for absolute encoder  
A 0/1 signal starts the absolute encoder adjustment.

**Index:** 
  
[
0]:
Position control  
[
1]:
Motor encoder  
[
2]:
Reserved  
[
3]:
Reserved

**Dependency:** 
  
See also:
p2507, r2526, c2598, p2599

**Caution:** 
  
For rotating absolute encoders, when adjusting, a range is set up symmetrically around
zero with half of the encoder range, within which the position must be re-established
after switch-off/switch-on. In this range, it is only permissible that the encoder
overflows.  
After the adjustment has been completed, it must be guaranteed that the range is not
exited. The reason for this is that outside the range, there is no clear reference
any longer between the encoder actual value and mechanical system.  
If the home position (c2598) lies in this range, then the position actual value is
set when adjusting to the home position. Otherwise, adjustment is canceled with F07443.  
There is no overflow for linear absolute encoders. This means that after the adjustment,
the position can be re-established in the complete traversing range after switch-off/switch-on.
When adjusting, the position actual value is set to the home position.

**Note:** 
  
The status of the absolute encoder adjustment is indicated via p2507 and in status
word r2526.  
To permanently accept the determined position offset, it must be retentively saved
(p0977).  
This adjustment can only be initiated for an absolute encoder.

### p11550 EPOS active homing reference cam selection

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Homing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 1 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal to evaluate "Active homing reference cam".

**Value:** 
  
0:
Reference cam selection 1  
1:
Reference cam selection 2

**Dependency:** 
  
See also:
p2607, c2612

### c11560 EPOS direct setpoint input/MDI acceleration setpoint

[S200 Basic PN](#c11560-epos-direct-setpoint-inputmdi-acceleration-setpoint-1)

[S200 Basic PN EPOS load side, rotating](#c11560-epos-direct-setpoint-inputmdi-acceleration-setpoint-2)

#### c11560 EPOS direct setpoint input/MDI acceleration setpoint

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Direct setpoint input (MDI) |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm/s² | **Unit group:** 12_3 | **Unit selection:** p2498 |
| **Type of signal interconnection:** Sink numeric |  | **Scaling:** - |
| **Factory interconnection:** | **Fixed value:** |  |
| 2572 | 0.00 [mm/s²] |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal for the acceleration setpoint in mode "direct setpoint input/MDI".

**Dependency:** 
  
See also:
c2649, c2650

**Notice:** 
  
The parameter may be protected as a result of r0922 and cannot be changed.

**Note:** 
  
Depending on c2649, the acceleration setpoint is either transferred continuously or
edge-triggered.

#### c11560 EPOS direct setpoint input/MDI acceleration setpoint

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN (EPOS load side, rotating), S200 Basic PTI (EPOS load side, rotating), S200 PN (EPOS load side, rotating), S200 PTI (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Direct setpoint input (MDI) |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** °/s² | **Unit group:** 12_4 | **Unit selection:** p2498 |
| **Type of signal interconnection:** Sink numeric |  | **Scaling:** - |
| **Factory interconnection:** | **Fixed value:** |  |
| 2572 | 0.00 [°/s²] |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal for the acceleration setpoint in mode "direct setpoint input/MDI".

**Dependency:** 
  
See also:
c2649, c2650

**Notice:** 
  
The parameter may be protected as a result of r0922 and cannot be changed.

**Note:** 
  
Depending on c2649, the acceleration setpoint is either transferred continuously or
edge-triggered.

### c11561 EPOS direct setpoint input/MDI deceleration setpoint

[S200 Basic PN](#c11561-epos-direct-setpoint-inputmdi-deceleration-setpoint-1)

[S200 Basic PN EPOS load side, rotating](#c11561-epos-direct-setpoint-inputmdi-deceleration-setpoint-2)

#### c11561 EPOS direct setpoint input/MDI deceleration setpoint

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Traversing blocks |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm/s² | **Unit group:** 12_3 | **Unit selection:** p2498 |
| **Type of signal interconnection:** Sink numeric |  | **Scaling:** - |
| **Factory interconnection:** | **Fixed value:** |  |
| 2573 | 0.00 [mm/s²] |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal for the deceleration setpoint in mode "direct setpoint input/MDI".

**Dependency:** 
  
See also:
c2649, c2650

**Notice:** 
  
If, when calculating the traversing profile, it is identified that the target position
with the programmed deceleration setpoint cannot be reached without reversing the
direction, then when accepting the dynamic response values, the higher deceleration
setpoint is accepted and becomes effective.  
The parameter may be protected as a result of r0922 and cannot be changed.

**Note:** 
  
Depending on c2649, the deceleration setpoint is either transferred continuously or
edge-triggered.

#### c11561 EPOS direct setpoint input/MDI deceleration setpoint

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN (EPOS load side, rotating), S200 Basic PTI (EPOS load side, rotating), S200 PN (EPOS load side, rotating), S200 PTI (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Traversing blocks |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** °/s² | **Unit group:** 12_4 | **Unit selection:** p2498 |
| **Type of signal interconnection:** Sink numeric |  | **Scaling:** - |
| **Factory interconnection:** | **Fixed value:** |  |
| 2573 | 0.00 [°/s²] |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Signal for the deceleration setpoint in mode "direct setpoint input/MDI".

**Dependency:** 
  
See also:
c2649, c2650

**Notice:** 
  
If, when calculating the traversing profile, it is identified that the target position
with the programmed deceleration setpoint cannot be reached without reversing the
direction, then when accepting the dynamic response values, the higher deceleration
setpoint is accepted and becomes effective.  
The parameter may be protected as a result of r0922 and cannot be changed.

**Note:** 
  
Depending on c2649, the deceleration setpoint is either transferred continuously or
edge-triggered.

### r11570 EPOS actual acceleration

[S200 Basic PN](#r11570-epos-actual-acceleration-1)

[S200 Basic PN EPOS load side, rotating](#r11570-epos-actual-acceleration-2)

#### r11570 EPOS actual acceleration

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Parameter group:** Jog, Traversing blocks, Direct setpoint input (MDI) |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm/s² | **Unit group:** 12_3 | **Unit selection:** p2498 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the acceleration value currently being processed.

**Dependency:** 
  
See also:
p2572

**Note:** 
  
The maximum acceleration from p2572 is effective in operating mode "Jog" and "Active
homing".

#### r11570 EPOS actual acceleration

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN (EPOS load side, rotating), S200 Basic PTI (EPOS load side, rotating), S200 PN (EPOS load side, rotating), S200 PTI (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Parameter group:** Jog, Traversing blocks, Direct setpoint input (MDI) |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** °/s² | **Unit group:** 12_4 | **Unit selection:** p2498 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the acceleration value currently being processed.

**Dependency:** 
  
See also:
p2572

**Note:** 
  
The maximum acceleration from p2572 is effective in operating mode "Jog" and "Active
homing".

### r11571 EPOS actual deceleration

[S200 Basic PN](#r11571-epos-actual-deceleration-1)

[S200 Basic PN EPOS load side, rotating](#r11571-epos-actual-deceleration-2)

#### r11571 EPOS actual deceleration

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Parameter group:** Jog, Traversing blocks, Direct setpoint input (MDI) |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm/s² | **Unit group:** 12_3 | **Unit selection:** p2498 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the deceleration value currently being processed.

**Dependency:** 
  
See also:
p2573

**Note:** 
  
The maximum deceleration from p2573 is effective in operating mode "Jog" and "Active
homing".

#### r11571 EPOS actual deceleration

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN (EPOS load side, rotating), S200 Basic PTI (EPOS load side, rotating), S200 PN (EPOS load side, rotating), S200 PTI (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Parameter group:** Jog, Traversing blocks, Direct setpoint input (MDI) |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** °/s² | **Unit group:** 12_4 | **Unit selection:** p2498 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the deceleration value currently being processed.

**Dependency:** 
  
See also:
p2573

**Note:** 
  
The maximum deceleration from p2573 is effective in operating mode "Jog" and "Active
homing".

### c29048 Torque limit selection bit 0

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Torque limiting, Technology Extensions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink binary |  |  |
| **Factory interconnection:** | **Fixed value:** |  |
| not interconnected | 0 |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603004000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.016

**Description:** 
  
Signal of bit 0 for the torque limit.

### c29049 Torque limit selection bit 1

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Torque limiting, Technology Extensions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink binary |  |  |
| **Factory interconnection:** | **Fixed value:** |  |
| not interconnected | 0 |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603004000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.016

**Description:** 
  
Signal of bit 1 for the torque limit.

### p29050[0...3] Upper torque limit

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Technology Extensions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** % | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| -150.0 [%] | 350.0 [%] | [0] 350.0 [%] |
| **Version:**603004000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.016

**Description:** 
  
Sets the upper torque limit.  
Three internal torque limits in total are available.  
With the combination of the digital input signals Torque limit selection bit 0 and
Torque limit selection bit 1, you can select one of the three internal torque limits
as the source of the upper torque limit.

**Index:** 
  
[
0]:
Upper torque limit 0  
[
1]:
Upper torque limit 1  
[
2]:
Upper torque limit 2  
[
3]:
Upper torque limit 3

### p29051[0...3] Lower torque limit

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Technology Extensions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** % | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| -350.0 [%] | 150.0 [%] | [0] -350.0 [%] |
| **Version:**603004000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.016

**Description:** 
  
Sets the lower torque limit.  
Three internal torque limits in total are available.  
With the combination of the digital input signals Torque limit selection bit 0 and
Torque limit selection bit 1, you can select one of the three internal torque limits
as the source of the lower torque limit.

**Index:** 
  
[
0]:
Lower torque limit 0  
[
1]:
Lower torque limit 1  
[
2]:
Lower torque limit 2  
[
3]:
Lower torque limit 3

### c29063 Speed limit selection bit 0

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Speed limiting, Technology Extensions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink binary |  |  |
| **Factory interconnection:** | **Fixed value:** |  |
| not interconnected | 0 |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603004000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.016

**Description:** 
  
Signal of bit 0 for the speed limit.

### c29064 Speed limit selection bit 1

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Speed limiting, Technology Extensions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink binary |  |  |
| **Factory interconnection:** | **Fixed value:** |  |
| not interconnected | 0 |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603004000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.016

**Description:** 
  
Signal of bit 1 for the speed limit.

### p29070[0...3] Speed limit in positive direction of rotation

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Technology Extensions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** rpm | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [rpm] | 210000.00 [rpm] | [0] 210000.00 [rpm] |
| **Version:**603004000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.016

**Description:** 
  
Sets the maximum speed for the positive direction.  
Three internal speed limits in total are available.  
With the combination of the digital input signals Speed limit selection bit 0 and
Speed limit selection bit 1, you can select one of the three internal speed limits
as the source of the speed limit.

**Index:** 
  
[
0]:
Speed limit for positive direction 0  
[
1]:
Speed limit for positive direction 1  
[
2]:
Speed limit for positive direction 2  
[
3]:
Speed limit for positive direction 3

**Dependency:** 
  
The default value depends on the maximum motor speed.

### p29071[0...3] Speed limit in negative direction of rotation

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Technology Extensions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** rpm | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| -210000.00 [rpm] | 0.00 [rpm] | [0] -210000.00 [rpm] |
| **Version:**603004000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.016

**Description:** 
  
Sets the maximum speed for the negative direction.  
Three internal speed limits in total are available.  
With the combination of the digital input signals Speed limit selection bit 0 and
Speed limit selection bit 1, you can select one of the three internal speed limits
as the source of the speed limit.

**Index:** 
  
[
0]:
Speed limit for negative direction 0  
[
1]:
Speed limit for negative direction 1  
[
2]:
Speed limit for negative direction 2  
[
3]:
Speed limit for negative direction 3

**Dependency:** 
  
The default value depends on the maximum motor speed.

### r29404.0...5 DO status word

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Parameter group:** Technology Extensions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source binary/numeric |  | **Scaling:** - |
| **Version:**603004000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.016

**Description:** 
  
Displays the status word of the digital outputs.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | ready for servo on |  |  | - |
| 01 | current control mode |  |  | - |
| 02 | overload level reached |  |  | - |
| 03 | speed reached |  |  | - |
| 04 | warnning1 |  |  | - |
| 05 | warnning2 |  |  | - |

### r60000 PROFIdrive reference speed

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN, S200 PN |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Parameter group:** |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** CALC_MOD_ALL |
| **Unit:** rpm | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Sets the reference quantity for the speed values.  
All speeds specified as relative values refer to this reference quantity.  
The reference quantity corresponds to 100% or 4000 hex (word) or 4000 0000 hex (double
word).

**Dependency:** 
  
See also:
p2000

**Note:** 
  
Parameter r60000 is an image of parameter p2000 in conformance with PROFIdrive.

### r60100[0...4] PROFIdrive telegram display total

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN, S200 PN |  |  |
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Parameter group:** Configuration |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays the send and receive telegrams.

**Index:** 
  
[
0]:
Subslot 1: MAP  
[
1]:
-  
[
2]:
Subslot 3: standard/SIEMENS  
[
3]:
Subslot 4: supplementary telegram  
[
4]:
Subslot 5: supplementary telegram

**Dependency:** 
  
See also:
r0922

**Note:** 
  
Value = 65534: No telegram  
Value = 65535: MAP "Module Access Point"

### r61000[0...239] PROFINET Name of Station

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN, S200 PN |  |  |
| **Data type:**Unsigned8 | **Visible in:**Extended display |  |
| **Parameter group:** Configuration |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays PROFINET Name of Station.

### r61001[0...3] PROFINET IP of Station

|  |  |  |
| --- | --- | --- |
| **Variant:**S200 Basic PN, S200 PN |  |  |
| **Data type:**Unsigned8 | **Visible in:**Extended display |  |
| **Parameter group:** Configuration |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S200%20Basic%20PN.md#sinamics-alarms-s200-basic-pn) |  |  |

**Valid as of version:**
  
06.02.015

**Description:** 
  
Displays PROFINET IP of Station.

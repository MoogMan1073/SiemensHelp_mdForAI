---
title: "SINAMICS Parameter S210"
package: sdrpa401enUS
topics: 708
source: Siemens TIA Portal Information System (offline help, en-US)
---


# SINAMICS Parameter S210

This section contains the parameter descriptions for the devices listed below. The parameter descriptions for the various devices can differ. In the table of contents, you will then see a separate entry for each parameter number. The following device variants are taken into account in the online help:

- SINAMICS S210 (from SINAMICS RT V6.1)

## SINAMICS Parameter S210 00002 - 01278

SINAMICS Parameter S210 00002 - 01278

### r0002 Operating display

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Status parameters, Diagnostics general, Drive enable signals |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
Operation - Speed setpoint not enabled  
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
31:
Ready for switching on - Set "ON/OFF1" = "0/1"  
35:
Switching on inhibited - Commissioning not possible, check motor  
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
  
For a display not equal to 0, the drive is either powering up or an enable signal
is missing. The control sends these enable signals.  
For several missing enable signals, the corresponding value with the highest number
is displayed.

**Note:** 
  
The drive only controls the motor speed in the "Operation" state (r0002 = 0).  
OC: Operating condition  
EP: Enable Pulses (pulse enable)  
RFG: Ramp-function generator  
COM: Commissioning  
MotID: Motor data identification  
SS2: Safe Stop 2  
STO: Safe Torque Off

### r0020 Speed setpoint smoothed

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Mode signals / displays |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** rpm | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the smoothed speed setpoint at the speed controller input.

**Dependency:** 
  
See also:
r1438

### r0021 Speed actual value smoothed

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Diagnostics, Mode signals / displays |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** rpm | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2000 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Brake control, Mode signals / displays |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** V | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2001 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the smoothed actual value of the DC link voltage.

**Dependency:** 
  
See also:
r0070

### r0027 Absolute actual current smoothed

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Mode signals / displays |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Arms | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2002 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the smoothed absolute current actual value.

**Dependency:** 
  
See also:
r0068

### r0031 Actual torque smoothed

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Brake control, Mode signals / displays |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Nm | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the smoothed torque actual value.

**Dependency:** 
  
See also:
r0080

### r0032 Active power actual value smoothed

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Mode signals / displays |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** kW | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** r2004 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Motor temperature, Mode signals / displays |  |  |
| **Not relevant for motor type:**Induction motor, Separately excited synchronous motor, Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** % | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** PERCENT |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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

### r0037[0...10] Drive temperatures

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Mode signals / displays |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** °C | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2006 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the temperatures of the drive components.

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Mode signals / displays, Power loss optimization |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** kWh | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Mode signals / displays, Power unit |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** % | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** PERCENT |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Control/status words, Drive enable signals |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source binary/numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the missing enable signals.  
All enable signals are required to operate the drive. The enable signals are set by
the control.

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
STO enabled via PROFIsafe:  
- STO is selected via PROFIsafe.  
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
- The holding brake opening time (r1216) has still not elapsed.  
- The encoder has not been calibrated (synchronous motor).  
  
Bit 26 = 1 (enable signal missing), if:  
- The drive is inactive or not capable of operation.  
- The drive device is in the "PROFIenergy energy-saving mode" (r5600, CU-specific).  
  
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
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Mode signals / displays, Speed setpoint filter |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** rpm | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2000 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Displays the currently unsmoothed speed setpoint at the input of the speed controller
or U/f characteristic (after the interpolator).

### r0061[0...1] Actual speed unsmoothed

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Motor encoder, Mode signals / displays |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** rpm | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2000 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the unsmoothed speed actual value sensed by the encoder.

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Mode signals / displays |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** rpm | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2000 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Display for the speed setpoint after the setpoint filters.

### r0063 Speed actual value smoothed

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** U/f control, Speed controller, Speed actual value filter, Mode signals / displays |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** rpm | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2000 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Mode signals / displays |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Arms | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2002 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays actual absolute current.

**Dependency:** 
  
See also:
r0027

**Notice:** 
  
The value is updated with a sampling time of 1 ms.

**Note:** 
  
Absolute current value = sqrt(Iq^2 + Id^2)  
The absolute current actual value is available smoothed (r0027) and unsmoothed (r0068).

### r0070 Actual DC link voltage

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Mode signals / displays |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** V | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2001 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Display for the measured actual value of the DC link voltage.

**Dependency:** 
  
See also:
r0026

**Note:** 
  
The DC link voltage is available smoothed (r0026) and unsmoothed (r0070).

### r0076 Current actual value field-generating

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** U/f control, Current controller, Mode signals / displays |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Arms | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2002 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Display for the field-generating current actual value.

### r0077 Current setpoint torque-generating

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Current controller, Mode signals / displays |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Arms | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2002 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the torque/force-generating current setpoint.

### r0078[0...1] Current actual value torque-generating

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Mode signals / displays |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Arms | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2002 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Torque limiting, Mode signals / displays |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Nm | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2003 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Mode signals / displays |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Nm | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2003 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Display for the actual torque.

**Dependency:** 
  
See also:
r0031

**Note:** 
  
The value is available smoothed (r0031) and unsmoothed (r0080).

### r0081 Torque utilization

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Torque limiting, Mode signals / displays |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** % | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** PERCENT |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Displays the torque utilization as a percentage.  
The torque utilization is obtained from the required smoothed torque referred to the
torque limit.

**Note:** 
  
The torque utilization is available smoothed (r0033) and unsmoothed (r0081).  
The torque utilization is obtained from the required torque referred to the torque
limit as follows:  
- Positive torque: r0081 = ((r0079 + p1532) / (r1538 - p1532)) * 100 %  
- Negative torque: r0081 = ((-r0079 + p1532) / (-r1539 + p1532)) * 100 %  
The calculation of the torque utilization depends on the selected smoothing time constant
(p0045).

### r0082[0...3] Active power actual value

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Mode signals / displays |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** kW | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** r2004 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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

### p0140 Number of Encoder Data Sets (EDS)

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Commissioning |  |  |
| **Parameter group:** Data sets |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 1 | 2 | [0] 1 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the number of Encoder Data Sets (EDS).

**Note:** 
  
When parameterizing the drive with "no encoder" there must be at least one encoder
data set (p0140 >= 1).

### p0187[0] Motor encoder encoder data set number

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Commissioning |  |  |
| **Parameter group:** Data sets |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 99 | [0] 99 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Assigns a drive data set (= index) the associated encoder data set (EDS) for the motor
encoder.  
The value corresponds to the number of the assigned encoder data set.  
Example:  
Motor encoder in drive data set 2 should be assigned encoder data set 0.  
--> p0187[2] = 0

**Note:** 
  
A value of 99 means that no encoder has been assigned to this drive data set (not
configured).

### p0188[0] Encoder 2 encoder data set number

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Commissioning |  |  |
| **Parameter group:** Data sets |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 99 | [0] 99 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Assign a drive data set (= index) the corresponding encoder data set (EDS) for encoder
2.  
The value corresponds to the number of the assigned encoder data set.  
Example:  
Encoder 2 in drive data set 2 should be assigned to encoder data set 1.  
--> p0188[2] = 1

**Note:** 
  
A value of 99 means that no encoder has been assigned to this drive data set (not
configured).

### r0196[0...255].4...15 Topology component status

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Diagnostics general |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
| 04 | Component state | Inactive/parking | Active | - |
| 06 | Topology problem active | No | Yes | - |
| 07 | Part of the target topology | No only act topo | Yes | - |
| 08 | Alarm present | No | Yes | - |
| 10 | Fault present | No | Yes | - |
| 13 | Maintenance required | No | Yes | - |
| 14 | Maintenance urgently required | No | Yes | - |
| 15 | Fault gone/can be acknowledged | No | Yes | - |

**Note:** 
  
For bits 12 ... 11:  
These status bits are used for the classification of internal alarm classes and are
intended for diagnostic purposes only on certain automation systems with integrated
SINAMICS functionality.

### p0201[0] Power unit code number

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Commissioning |  |  |
| **Parameter group:** Power unit |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 65535 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the actual code number of the power unit being used.

### r0208 Rated power unit line voltage

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** System identification, Power unit |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Vrms | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the rated line voltage of the power unit.  
r0208 = 230: 200 - 240 V (line voltage tolerance: +/-10 %)  
r0208 = 400: 380 - 480 V (line voltage tolerance: +/-10 %)

### p0210 Device supply voltage

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Ready for operation |  |  |
| **Parameter group:** Power unit, Quick commissioning |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** V | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 1 [V] | 63000 [V] | [0] 400 [V] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Commissioning |  |  |
| **Parameter group:** Dynamic braking, Quick commissioning |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 3 | 10 | [0] 10 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Commissioning |  |  |
| **Parameter group:** Dynamic braking, Quick commissioning |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ohm | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.0 [ohm] | 1000.0 [ohm] | [0] 0.0 [ohm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Commissioning |  |  |
| **Parameter group:** Dynamic braking, Quick commissioning |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** s | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [s] | 2000.00 [s] | [0] 0.00 [s] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Commissioning |  |  |
| **Parameter group:** Dynamic braking, Quick commissioning |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** kW | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [kW] | 20000.00 [kW] | [0] 0.00 [kW] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

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

### p0251[0] Power unit heat sink fan operating hours counter

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Ready for operation |  |  |
| **Parameter group:** System identification, Power unit |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** h | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 [h] | 4294967295 [h] | [0] 0 [h] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the operating hours of the heat sink fan in the power unit.  
The number of hours operated can only be reset to 0 in this parameter (e.g. after
a fan has been replaced).

**Dependency:** 
  
See also:
r0277  
See also:
A30042

**Note:** 
  
This parameter is only available/included in the customer interface for compatibility
reasons.  
In the future, use parameter r0277 (power unit heat sink-fan wear counter).

### r0277[0] Power unit heat sink fan wear counter

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Power unit |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** % | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the wear counter of the heat sink fan in the power unit.  
After a fan has been replaced, using an appropriate button, the value can be reset
in the commissioning tool to 0.

**Dependency:** 
  
See also:
A30042

### p0300[0] Motor type selection

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Commissioning |  |  |
| **Parameter group:** Motor data, Quick commissioning |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 10000 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Selects the motor type or start to read in the motor parameters for a motor with DRIVE-CLiQ
(p0300 = 10000).  
For p0300 < 10000 the following applies:  
The first digit of the parameter value always defines the general motor type and corresponds
to the third-party motor belonging to a motor list:  
2 = rotating synchronous motor

**Value:** 
  
0:
No motor  
2:
Synchronous motor  
203:
1FT2 synchronous motor  
237:
1FK7 synchronous motor  
272:
1FK2 synchronous motor  
295:
1FS2 synchronous motor  
2024:
1FK7 synchronous motor  
2030:
1FT2 synchronous motor  
2031:
1FK2 synchronous motor  
2032:
1FS2 synchronous motor  
10000:
Motor with DRIVE-CLiQ

**Dependency:** 
  
See also:
p0301

### p0301[0] Motor code number selection

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Commissioning |  |  |
| **Parameter group:** Motor data, Quick commissioning |  |  |
| **Not relevant for motor type:**Separately excited synchronous motor |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 99999999 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Motor data, Quick commissioning |  |  |
| **Not relevant for motor type:**Separately excited synchronous motor, Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the identified motor code number.  
When the drive powers up, the motor code is read out the motor. For r0302 = 0, the
motor data were not identified.

### r0304[0] Rated motor voltage

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Motor data, Quick commissioning |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Vrms | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the rated motor voltage.

### r0305[0] Rated motor current

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Motor data, Quick commissioning |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Arms | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the rated motor current.

### r0307[0] Rated motor power

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Motor data, Quick commissioning |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** kW | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the rated motor power.

### r0311[0] Rated motor speed

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Motor data, Quick commissioning |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** rpm | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the rated motor speed.

### r0312[0] Rated motor torque

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Motor data |  |  |
| **Not relevant for motor type:**Induction motor, Separately excited synchronous motor, Synchronous or reluctance motor with starting cage, Synchronous reluctance motor |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Nm | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the rated motor torque.

### r0316[0] Motor torque constant

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Motor data, Quick commissioning |  |  |
| **Not relevant for motor type:**Induction motor, Separately excited synchronous motor, Synchronous or reluctance motor with starting cage, Synchronous reluctance motor |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Nm/A | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the torque constant of the synchronous motor.  
r0316 = 0:  
The torque constant is calculated from the motor data.  
r0316 > 0:  
The selected value is used as torque constant.

### r0318[0] Motor stall current

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Motor data |  |  |
| **Not relevant for motor type:**Induction motor, Separately excited synchronous motor, Synchronous or reluctance motor with starting cage, Synchronous reluctance motor |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Arms | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the rated motor stall current.

### r0319[0] Motor static torque

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Motor data |  |  |
| **Not relevant for motor type:**Induction motor, Separately excited synchronous motor, Synchronous or reluctance motor with starting cage, Synchronous reluctance motor |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Nm | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the motor standstill/static torque.

### r0322[0] Maximum motor speed

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Motor data, Quick commissioning |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** rpm | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the maximum motor speed.

**Dependency:** 
  
See also:
p1082

### r0323[0] Maximum motor current

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Motor data, Quick commissioning |  |  |
| **Not relevant for motor type:**Induction motor, Separately excited synchronous motor, Synchronous reluctance motor |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Arms | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the maximum permissible motor current.

### r0341[0] Motor moment of inertia

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Motor data, Speed controller |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** CALC_MOD_ALL |
| **Unit:** kgm² | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the motor moment of inertia (without load).

### p0400[0...n] Encoder type selection

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Commissioning |  |  |
| **Parameter group:** Motor encoder, Quick commissioning |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** EDS n defined by: p0140 |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 10100 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Selects the encoder from the list of encoder types supported.

**Value:** 
  
0:
No encoder  
202:
DRIVE-CLiQ encoder AS20, singleturn  
204:
DRIVE-CLiQ encoder AM20, multiturn 4096  
222:
DRIVE-CLiQ encoder AS22, singleturn  
224:
DRIVE-CLiQ encoder AM22, multiturn 4096  
242:
DRIVE-CLiQ encoder AS24, singleturn  
244:
DRIVE-CLiQ encoder AM24, multiturn 4096  
262:
DRIVE-CLiQ encoder AS26, singleturn  
264:
DRIVE-CLiQ encoder AM26, multiturn 4096  
10100:
Identify encoder (waiting)

**Notice:** 
  
An encoder type with p0400 < 9999 defines an encoder for which there is an encoder
parameter list.  
When selecting a catalog encoder (p0400 < 9999) the parameters from the encoder parameter
list cannot be changed (write protection).

**Note:** 
  
The connected encoder can be identified using p0400 = 10100. This means that the encoder
must support this, and is possible in the following cases:  
- Motor with DRIVE-CLiQ  
- Encoder with EnDat interface  
- DRIVE-CLiQ encoder  
  
For p0400 = 10100 the following applies:  
The connected encoder is identified. If identification is not possible, then p0400
remains set = 10100, and the system waits until identification is possible.

### p0404[0...n].1...10 Encoder configuration effective

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Commissioning |  |  |
| **Parameter group:** Motor encoder |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** EDS n defined by: p0140 |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| - | - | [0] 0000 0000 0000 0000 bin |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

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
| 10 | DRIVE-CLiQ encoder | No | Yes | - |

**Notice:** 
  
This parameter is automatically pre-assigned for encoders from the encoder list and
for identify encoder (p0400).  
When selecting a catalog encoder, this parameter cannot be changed (write protection).
Information in p0400 should be carefully observed when removing write protection.

**Note:** 
  
For bit 01, 02 (absolute encoder, multiturn encoder):  
These bits can only be selected for a DRIVE-CLiQ encoder.  
For bit 10 (DRIVE-CLiQ encoder):  
This bit is only used for the large-scale integrated DRIVE-CLiQ encoders that provide
their encoder data directly in DRIVE-CLiQ format without converting this data. Therefore,
this bit is not set for first generation DRIVE-CLiQ encoders.

### p0408[0...n] Rotary encoder pulse number

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Commissioning |  |  |
| **Parameter group:** Motor encoder |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** EDS n defined by: p0140 |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 16777215 | [0] 2048 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
For a DRIVE-CLiQ encoder, a value is entered here that facilitates optimum transfer
of the resolution (p0423).

### p0421[0...n] Absolute encoder rotary multiturn resolution

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Commissioning |  |  |
| **Parameter group:** Motor encoder |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** EDS n defined by: p0140 |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 4294967295 | [0] 4096 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Maximum number of revolutions that can be resolved for a rotary absolute encoder to
determine the position.  
The value of p0421 is read out when the drive powers up and cannot be changed.

### p0423[0...n] Absolute encoder rotary singleturn resolution

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Commissioning |  |  |
| **Parameter group:** Motor encoder |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** EDS n defined by: p0140 |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 1073741823 | [0] 8192 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Data type:**Integer32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Motor encoder |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
Encoder 2  
[
2]:
Reserved

### p0488[0...2] Activate measuring probe 1

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Measuring probe |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 210 | [0] 210 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Setting to activate/deactivate measuring probe 1.  
The inversion of probe 1 is set in p0490.0.

**Value:** 
  
0:
No measuring probe  
210:
DI 0 (X130 / 1.2)

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

### p0489[0...2] Activate measuring probe 2

[S210](#p048902-activate-measuring-probe-2-1)

[S210 Interpolator for EPOS](#p048902-activate-measuring-probe-2-2)

#### p0489[0...2] Activate measuring probe 2

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Measuring probe |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 211 | [0] 211 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Setting to activate/deactivate measuring probe 2.  
The inversion of probe 2 is set in p0490.1.

**Value:** 
  
0:
No measuring probe  
211:
DI 1 (X130 / 1.5)

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

#### p0489[0...2] Activate measuring probe 2

|  |  |  |
| --- | --- | --- |
| **Variant:**S210 (Interpolator for EPOS) |  |  |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Measuring probe |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 211 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Setting to activate/deactivate measuring probe 2.  
The inversion of probe 2 is set in p0490.1.

**Value:** 
  
0:
No measuring probe  
211:
DI 1 (X130 / 1.5)

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

### p0490.0...1 Invert measuring probe

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Measuring probe |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| - | - | [0] 0000 bin |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Setting to invert digital input 0 or 1 (probe 1, 2).

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | DI 0 (X130 / 1.2) | Not inverted | Inverted | - |
| 01 | DI 1 (X130 / 1.5) | Not inverted | Inverted | - |

**Dependency:** 
  
See also:
p0488, p0489

**Note:** 
  
DI: Digital Input  
The inversion has no effect on the status display of the digital inputs (r0722).

### p0494[0...n] Equivalent zero mark input terminal

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Motor encoder |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** EDS n defined by: p0140 |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 211 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Selects the input terminal for connecting an equivalent zero mark (external encoder
zero mark).

**Value:** 
  
0:
No equivalent zero mark (evaluation of the encoder zero mark)  
210:
DI 0 (X130 / 1.2)  
211:
DI 1 (X130 / 1.5)

**Dependency:** 
  
See also:
p0490

**Caution:** 
  
In order to prevent incorrect measurement values, these parameters may not be written
during an active measurement.

**Note:** 
  
Refer to the encoder interface for PROFIdrive.

### r0550[0] Brake status

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Motor holding brake, Quick commissioning |  |  |
| **Not relevant for motor type:**Separately excited synchronous motor, Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the status of the brake.  
This value is read when the drive runs up.

**Value:** 
  
0:
No data  
1:
Holding brake  
2:
High performance holding brake

**Dependency:** 
  
See also:
p1215, r1216, r1217

**Note:** 
  
For value = 1:  
The default value for opening time/closing time applies.  
For value = 2:  
A shorter opening time/closing time is realized if the drive satisfies the preconditions.

### p0551[0] Brake code number

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Commissioning |  |  |
| **Parameter group:** Motor holding brake, Quick commissioning |  |  |
| **Not relevant for motor type:**Separately excited synchronous motor, Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 4294967295 | [0] 1 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Display and setting the code number for the brake.  
0 = No data  
1 = Manual entry  
> 1 = valid code number  
For value = 0:  
- Parameters listed under Dependent are set to a value of zero and are write protected.  
- Parameters r1216, r1217 are set to a value of zero.  
For value = 1:  
- Write protection for the parameters listed under Dependent is withdrawn.  
For value > 1:  
- Parameters listed under Dependent are automatically pre-assigned and are write protected.  
- Parameters r1216, r1217 are automatically preassigned the appropriate values.

**Dependency:** 
  
See also:
r0550

**Note:** 
  
Only code numbers can be set that are permitted for the selected motor code (p0301).

### p0613[0] Motor temperature model ambient temperature

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Motor temperature |  |  |
| **Not relevant for motor type:**Induction motor, Separately excited synchronous motor, Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** CALC_MOD_ALL |
| **Unit:** °C | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| -40 [°C] | 100 [°C] | [0] 40 [°C] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the motor ambient temperature.  
Based on this value, the motor temperature model calculates the thermal motor utilization
(r0034).

**Dependency:** 
  
See also:
r0034  
See also:
F07011, A07012

**Note:** 
  
If the thermal motor model is activated for permanent-magnet synchronous motors, then
the parameter is incorporated in the model calculation if a temperature sensor is
not being used.

### r0722.0...4 Digital inputs status

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Digital inputs |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source binary/numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the status of the digital inputs.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | DI 0 (X130 / 1.2) | Low | High | - |
| 01 | DI 1 (X130 / 1.5) | Low | High | - |
| 02 | DI 2 (X130 / 2.1-2) | Low | High | - |
| 03 | DI 3 (X130 / 2.3-4) | Low | High | - |
| 04 | DI 4 (X130 / 2.6) | Low | High | - |

**Dependency:** 
  
See also:
p0488, p0489

**Note:** 
  
DI: Digital Input  
For bit 00, 01:  
DI 0 and DI 1 are fast digital inputs and can be used to connect a measuring probe
(p0488, p0489).  
For bits 02, 03:  
DI 2 and DI 3 form a failsafe digital input.  
For bit 04:  
DI 4 is intended to monitor the temperature of the external brake resistor.

### r0898.0...14 Control word sequence control

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Control/status words |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source binary/numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Display for the control word of the sequence control.  
The higher-level control cyclically sends the control word to the drive.

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
| 08 | Jog 1 | No | Yes | 3001 |
| 09 | Jog 2 | No | Yes | 3001 |
| 10 | Master control by PLC | No | Yes | - |
| 12 | Enable speed controller | No | Yes | - |
| 14 | Command close brake | No | Yes | - |

### r0899.0...13 Status word sequence control

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Control/status words |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source binary/numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
| 12 | Open holding brake | No | Yes | - |
| 13 | Command close holding brake | No | Yes | - |

**Note:** 
  
For bits 00, 01, 02, 04, 05, 06, 09:  
For PROFIdrive, these signals are used for status word 1.  
For bit 13:  
When function "SBC (Safe Brake Control)" is activated and selected, the brake is no
longer controlled using this signal.

### r0922 PROFIdrive PZD telegram selection

[S210](#r0922-profidrive-pzd-telegram-selection-1)

[S210 Interpolator for EPOS](#r0922-profidrive-pzd-telegram-selection-2)

#### r0922 PROFIdrive PZD telegram selection

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Quick commissioning, Configuration |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the PROFIdrive telegram.

**Value:** 
  
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
| **Variant:**S210 (Interpolator for EPOS) |  |  |
| **Data type:**Unsigned16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Quick commissioning, Configuration |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Configuration |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Configuration |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 65535 | [0] 1 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Configuration |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the operating mode.  
3: Closed-loop speed controlled operation without ramp-function generator

### r0944 Counter for fault buffer changes

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Faults / alarms |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Display the counter for fault buffer changes.

**Recommendation:** 
  
Used to check whether the fault buffer has been read out consistently.

**Dependency:** 
  
See also:
r0945, r0947, r0948, r0949, r2109

### r0945[0...63] Fault code

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Faults / alarms |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
--> Fault 1 (oldest active fault) of the active incident  
. . .  
r0945[7], r0949[7] or r2133[7], r2130[7], r0948[7], r2136[7], r2109[7]  
--> fault 8 (oldest active fault) of the active incident  
  
For more than 8 active faults, only the entries are overwritten at the eighth position
(index 7).  
  
History of acknowledged faults:  
If a fault incident is acknowledged, then all alarms of the 1st fault incident are
transferred into the 2nd fault incident, this becomes the 1st acknowledged fault incident.  
The 2nd incident is transferred into the 3rd, the 3rd into the 4th etc. The last incident
is rejected.  
  
r0945[8], r0949[8] or r2133[8], r2130[0], r0948[8], r2136[8], r2109[8]  
--> fault 1 of the 1st acknowledged incident  
. . .  
r0945[16], r0949[16] or r2133[16], r2130[16], r0948[16], r2136[16], r2109[16]  
--> fault 1 of the 2nd acknowledged incident  
. . .  
r0945[56], r0949[56] or r2133[56], r2130[56], r0948[56], r2136[56], r2109[56]  
--> fault 1 of the 7th acknowledged incident  
. . .  
r0945[63], r0949[63] or r2133[63], r2130[63], r0948[63], r2136[63], r2109[63]  
--> fault 8 (oldest fault that has gone) of the 7th acknowledged incident

### r0947[0...63] Fault number

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Faults / alarms |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
r0945[0], r0949[0] or r2133[0], r2130[0], r0948[0], r2136[0], r2109[0] --> fault 1
(oldest active fault) of the active incident  
. . .  
r0945[7], r0949[7] or r2133[7], r2130[7], r0948[7], r2136[7], r2109[7] --> fault 8
(latest active fault) of the active incident  
For more than 8 active faults, only the entries are overwritten at the eighth position
(index 7).  
  
History of acknowledged faults:  
If a fault incident is acknowledged, then all alarms of the 1st fault incident are
transferred into the 2nd fault incident, this becomes the 1st acknowledged fault incident.  
The 2nd incident is transferred into the 3rd, the 3rd into the 4th etc. The last incident
is rejected.  
  
r0945[8], r0949[8] or r2133[8], r2130[0], r0948[8], r2136[8], r2109[8] --> fault 1
of the 1st acknowledged incident  
. . .  
r0945[16], r0949[16] or r2133[16], r2130[16], r0948[16], r2136[16], r2109[16] -->
fault 1 of the 2nd acknowledged incident  
. . .  
r0945[56], r0949[56] or r2133[56], r2130[56], r0948[56], r2136[56], r2109[56] -->
fault 1 of the 7th acknowledged incident  
. . .  
r0945[63], r0949[63] or r2133[63], r2130[63], r0948[63], r2136[63], r2109[63] -->
fault 8 (oldest fault that has gone) of the 7th acknowledged incident

### r0948[0...63] Fault received in milliseconds

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Faults / alarms |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the system runtime in milliseconds referred to the day that the fault occurred.

**Dependency:** 
  
See also:
r0945, r0947, r0949, r2109, r2114, r2130, r2133, r2136, r3122

**Notice:** 
  
The time comprises r2130 (complete days) and r0948 (milliseconds, incomplete day).

### r0949[0...63] Fault value

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Faults / alarms |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays additional information about the fault that occurred (as integer number).  
The fault causes can be found under the fault values of the particular fault number.

**Dependency:** 
  
See also:
r0945, r0947, r0948, r2109, r2130, r2133, r2136, r3122

**Note:** 
  
The buffer parameters are cyclically updated in the background.  
The structure of the fault buffer and the assignment of the indices is shown in r0945.

### p0952 Fault cases counter

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Faults / alarms |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 65535 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Number of fault situations since the last reset.

**Dependency:** 
  
The counter is reset with p0952 = 0.  
See also:
r0945, r0947, r0948, r0949, r2109, r2130, r2133, r2136

### r0964[0...6] Device identification

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** System identification |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
r0964[0] = 42 --> SIEMENS  
r0964[1] = device type, see below  
r0964[2] = 602 --> first part firmware version V06.02 (second part, refer to index
6)  
r0964[3] = 2023 --> year 2023  
r0964[4] = 1706 --> June 17  
r0964[5] = 1 --> 1 (fixed value)  
r0964[6] = 0 --> second part firmware version (complete version: V06.02.00.00)  
Device type:  
r0964[1] = 5410 --> SINAMICS S210

### r0965 PROFIdrive profile number profile version

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Configuration |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Ready for operation |  |  |
| **Parameter group:** Save & reset |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 3 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
p0972 = 0 --> the reset was successfully executed.  
p0972 > 0 --> the reset was not executed.

### r0975[0...10] Converter identification

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** System identification |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
r0975[0] = 42 --> SIEMENS  
r0975[1] = 311 --> SERVO converter type  
r0975[2] = 602 --> first part firmware version V06.02 (second part refer to index
10)  
r0975[3] = 2023 --> year 2023  
r0975[4] = 1706 --> 17th of June  
r0975[5] = 1 --> PROFIdrive type class = 1 (axis)  
r0975[6] = 8 --> PROFIdrive subtype class = 4 (application class)  
r0975[7] = 1 --> 1 (fixed value)  
r0975[8] = 0 (reserved)  
r0975[9] = 0 (reserved)  
r0975[10] = 0 --> second part firmware version (complete version: V06.02.00.00)

### p0976 Reset all parameters

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Ready for operation |  |  |
| **Parameter group:** Save & reset |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 1 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Save & reset |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 1 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
  
The drive power supply may only be switched off after data has been saved (i.e. after
data save has been started, wait until the parameter again has the value 0).  
Writing to parameters is inhibited while saving.

### r0979[0...30] PROFIdrive encoder format

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** System identification, Configuration |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** System identification |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Ready for operation |  |  |
| **Parameter group:** Motorized potentiometer, Speed limiting, U/f control, Speed controller, Quick commissioning |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** CALC_MOD_ALL |
| **Unit:** rpm | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.000 [rpm] | 210000.000 [rpm] | [0] 1500.000 [rpm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the maximum speed of the motor to a value less than or equal to the maximum motor
speed (r0322).  
The set value is valid for both directions of rotation.

**Dependency:** 
  
See also:
r0322

### p1083[0] Positive speed limit

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Speed controller |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** rpm | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2000 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.000 [rpm] | 210000.000 [rpm] | [0] 210000.000 [rpm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the maximum speed for the positive direction.  
The set value must be less than or equal to the maximum speed (p1082).

### p1086[0] Negative speed limit

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Speed controller |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** rpm | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2000 |
| **Min:** | **Max:** | **Factory setting:** |
| -210000.000 [rpm] | 0.000 [rpm] | [0] -210000.000 [rpm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the maximum speed for the negative direction.  
The set value must be less than or equal to the maximum speed (p1082).

### p1121[0] OFF1 ramp-down time

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Quick commissioning |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** s | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.000 [s] | 999999.000 [s] | [0] 1.000 [s] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the ramp-down time after an OFF1 command.  
The value is referred to the maximum speed (p1082).  
After an OFF1 command, within this time, the speed setpoint is ramped down from the
maximum speed (p1082) to standstill.

**Dependency:** 
  
See also:
p1082

### p1135[0] OFF3 ramp-down time

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Shutdown functions, Safety Integrated, Quick commissioning |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** s | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.000 [s] | 600.000 [s] | [0] 0.000 [s] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the ramp-down time for Quick Stop.  
In this time, after an OFF3, the speed setpoint is reduced from the maximum speed
(p1082) down to standstill.

**Note:** 
  
This time can be exceeded if the DC link voltage reaches its maximum value.

### r1196 DSC position setpoint

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the position setpoint of Dynamic Servo Control in fine pulses.

**Note:** 
  
DSC: Dynamic Servo Control

### p1215[0] Motor holding brake configuration

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Ready for operation |  |  |
| **Parameter group:** Motor holding brake |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 2 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the configuration for the motor holding brake.  
For value 2:  
This setting allows the motor shaft to be rotated for installation purposes.

**Value:** 
  
0:
No motor holding brake available  
1:
Motor holding brake acc. to sequence control  
2:
Motor holding brake always open

**Dependency:** 
  
See also:
r1216, r1217, p1226, p1227, p1228, p1278

**Caution:** 
  
For the setting p1215 = 0, if a brake is used, it remains closed. If the motor moves,
this will destroy the brake.  
Setting p1215 = 2 is not permissible if the brake is used to hold loads.

### r1216[0] Motor holding brake opening time

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Motor holding brake |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the opening time for the motor holding brake.  
The speed setpoint is kept at 0 for this time. The speed setpoint is then enabled.

**Dependency:** 
  
See also:
p1215, r1217

### r1217[0] Motor holding brake closing time

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Motor holding brake |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the time to close the motor holding brake.  
If the drive signals that the motor is at a standstill, if the holding brake is activated,
after the closing time has expired, the pulses are canceled. This prevents the load
from sagging, for example.

**Dependency:** 
  
See also:
p1215, r1216

### p1226[0] Threshold for zero speed detection

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Motor holding brake, Shutdown functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** rpm | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [rpm] | 210000.00 [rpm] | [0] 20.00 [rpm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the speed threshold for the standstill identification.  
The following applies when the motor holding brake is activated:  
The motor is shut down and held by the brake after the closing time for the brake
in r1217 has elapsed.  
The following applies when the motor holding brake is not activated:  
The motor is shut down and it then coasts down.

**Dependency:** 
  
See also:
p1215, r1216, r1217, p1227

**Note:** 
  
In order that standstill is identified, the speed threshold in p1226 must be somewhat
higher than the noise on the speed actual value signal.

### p1227[0] Zero speed detection monitoring time

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Motor holding brake, Shutdown functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** s | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.000 [s] | 300.000 [s] | [0] 4.000 [s] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the monitoring time for the standstill identification.  
When braking with OFF1 or OFF3, standstill is detected after the monitoring time has
expired, after the setpoint speed has fallen below p1226.  
After this, the brake control is started, the system waits for the closing time in
r1217 and then the pulses are canceled.

**Dependency:** 
  
See also:
p1215, r1216, r1217, p1226

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Motor holding brake, Shutdown functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** s | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.000 [s] | 299.000 [s] | [0] 0.000 [s] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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

### p1278[0] Brake control diagnostics evaluation

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Motor holding brake |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 1 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the brake control type (with or without diagnostics evaluation).

**Value:** 
  
0:
Brake control with diagnostics evaluation  
1:
Brake control without diagnostics evaluation

**Note:** 
  
If the configuration of the motor holding brake (p1215 = 0) is set to "No holding
brake present" when running up, then an automatic identification of the motor holding
brake will be carried out.  
If a brake control is detected without diagnostics evaluation, then the parameter
is set to "Brake control without diagnostics evaluation".  
It is not permissible to parameterize "Brake control without diagnostics evaluation"
and enable "SBC (Safe Brake Control)" (p1278 = 1, p9603 > 0, p9604.1 = 1).

## SINAMICS Parameter S210 01407 - 02523

SINAMICS Parameter S210 01407 - 02523

### r1407.0...28 Status word speed controller

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Torque setpoints, U/f control, Torque limiting, Speed actual value filter, Control/status words, Acceleration model, Setpoint addition, Speed precontrol, Speed setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source binary/numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Speed setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| - | - | [0] 0001 bin |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Speed setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 2 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Speed setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [ms] | 5000.00 [ms] | [0] 0.00 [ms] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the time constant for the speed setpoint filter (PT1).

**Dependency:** 
  
See also:
p1414, p1415

**Note:** 
  
The speed setpoint filter is activated with a time constant greater than zero.

### p1417[0] Speed setpoint filter 1 denominator natural frequency

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Speed setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Hz | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.5 [Hz] | 16000.0 [Hz] | [0] 2000.0 [Hz] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Speed setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.001 | 10.000 | [0] 0.700 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Speed setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Hz | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.5 [Hz] | 16000.0 [Hz] | [0] 2000.0 [Hz] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Speed setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.000 | 10.000 | [0] 0.700 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Speed setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 2 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Speed setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [ms] | 5000.00 [ms] | [0] 0.00 [ms] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Speed setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Hz | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.5 [Hz] | 16000.0 [Hz] | [0] 2000.0 [Hz] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Speed setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.001 | 10.000 | [0] 0.700 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Speed setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Hz | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.5 [Hz] | 16000.0 [Hz] | [0] 2000.0 [Hz] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Speed setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.000 | 10.000 | [0] 0.700 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Speed controller |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Hz | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [Hz] | 8000.00 [Hz] | [0] 0.00 [Hz] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the natural frequency of a PT2 element for the reference model of the speed controller.

**Recommendation:** 
  
The reference model is finely set using p1433.

### r1438 Speed controller speed setpoint

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** U/f control, Speed controller |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** rpm | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2000 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the speed setpoint after setpoint limiting for the P component of the speed
controller.

### p1441[0] Actual speed smoothing time

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Speed controller |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** CALC_MOD_CON |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [ms] | 50.00 [ms] | [0] 0.00 [ms] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the smoothing time constant (PT1) for the speed actual value.

**Dependency:** 
  
See also:
r0063

### p1460[0] Speed controller P gain

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Speed controller |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** CALC_MOD_CON |
| **Unit:** Nms/rad | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.0000 [Nms/rad] | 500000000.0000 [Nms/rad] | [0] 0.3000 [Nms/rad] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Speed controller |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** CALC_MOD_CON |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [ms] | 100000.00 [ms] | [0] 10.00 [ms] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Speed controller |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** kgm² | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| - [kgm²] | - [kgm²] | [0] - [kgm²] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the load moment of inertia.  
The setting is made during commissioning while the One Button Tuning is being performed.

### p1520[0] Torque limit upper

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Torque limiting |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** CALC_MOD_LIM_REF |
| **Unit:** Nm | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2003 |
| **Min:** | **Max:** | **Factory setting:** |
| -1000000.00 [Nm] | 20000000.00 [Nm] | [0] 0.00 [Nm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Torque limiting |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** CALC_MOD_LIM_REF |
| **Unit:** Nm | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2003 |
| **Min:** | **Max:** | **Factory setting:** |
| -20000000.00 [Nm] | 1000000.00 [Nm] | [0] 0.00 [Nm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Torque limiting |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Nm | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2003 |
| **Min:** | **Max:** | **Factory setting:** |
| -100000.00 [Nm] | 100000.00 [Nm] | [0] 0.00 [Nm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the offset for the torque limit.  
The setting allows electronic weight equalization to be used for vertical axes.  
Parameters p1520 and p1521 are offset by the set value in the same direction.

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Torque limiting |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Nm | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2003 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the currently effective upper torque limit.

**Note:** 
  
The value in r1538 may not exceed the value in p1520.

### r1539 Lower effective torque limit

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Torque limiting |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Nm | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2003 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the currently effective lower torque limit.

**Note:** 
  
The value in r1539 may not exceed the value in p1521.

### p1558 Measure/precontrol hanging/suspended axis force due to weight

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Motor data identification routine |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| -1 | 1 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Current setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Nm | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2003 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the torque setpoint of the function generator.

### p1656[0].0...3 Activates current setpoint filter

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Current setpoint filter |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** CALC_MOD_CON |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| - | - | [0] 0001 bin |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Current setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** CALC_MOD_CON |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 1 | 2 | [0] 1 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Current setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** CALC_MOD_CON |
| **Unit:** Hz | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.5 [Hz] | 16000.0 [Hz] | [0] 1999.0 [Hz] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Current setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** CALC_MOD_CON |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.001 | 10.000 | [0] 0.700 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the denominator damping for current setpoint filter 1.

**Dependency:** 
  
The current setpoint filter 1 is activated via p1656.0 and parameterized via p1657
... p1661.

### p1660[0] Current setpoint filter 1 numerator natural frequency

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Current setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Hz | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.5 [Hz] | 16000.0 [Hz] | [0] 1999.0 [Hz] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the numerator natural frequency for current setpoint filter 1 (general filter).

**Dependency:** 
  
The current setpoint filter 1 is activated via p1656.0 and parameterized via p1657
... p1661.

### p1661[0] Current setpoint filter 1 numerator damping

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Current setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.000 | 10.000 | [0] 0.700 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the numerator damping for current setpoint filter 1.

**Dependency:** 
  
The current setpoint filter 1 is activated via p1656.0 and parameterized via p1657
... p1661.

### p1662[0] Current setpoint filter 2 type

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Current setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 1 | 2 | [0] 1 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Current setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Hz | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.5 [Hz] | 16000.0 [Hz] | [0] 1999.0 [Hz] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Current setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.001 | 10.000 | [0] 0.700 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the denominator damping for current setpoint filter 2.

**Dependency:** 
  
Current setpoint filter 2 is activated via p1656.1 and parameterized via p1662 ...
p1666.

### p1665[0] Current setpoint filter 2 numerator natural frequency

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Current setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Hz | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.5 [Hz] | 16000.0 [Hz] | [0] 1999.0 [Hz] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the numerator natural frequency for current setpoint filter 2 (general filter).

**Dependency:** 
  
Current setpoint filter 2 is activated via p1656.1 and parameterized via p1662 ...
p1666.

### p1666[0] Current setpoint filter 2 numerator damping

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Current setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.000 | 10.000 | [0] 0.700 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the numerator damping for current setpoint filter 2.

**Dependency:** 
  
Current setpoint filter 2 is activated via p1656.1 and parameterized via p1662 ...
p1666.

### p1667[0] Current setpoint filter 3 type

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Current setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 1 | 2 | [0] 1 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Current setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Hz | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.5 [Hz] | 16000.0 [Hz] | [0] 1999.0 [Hz] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Current setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.001 | 10.000 | [0] 0.700 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the denominator damping for current setpoint filter 3.

**Dependency:** 
  
Current setpoint filter 3 is activated via p1656.2 and parameterized via p1667 ...
p1671.

### p1670[0] Current setpoint filter 3 numerator natural frequency

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Current setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Hz | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.5 [Hz] | 16000.0 [Hz] | [0] 1999.0 [Hz] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the numerator natural frequency for current setpoint filter 3 (general filter).

**Dependency:** 
  
Current setpoint filter 3 is activated via p1656.2 and parameterized via p1667 ...
p1671.

### p1671[0] Current setpoint filter 3 numerator damping

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Current setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.000 | 10.000 | [0] 0.700 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the numerator damping for current setpoint filter 3.

**Dependency:** 
  
Current setpoint filter 3 is activated via p1656.2 and parameterized via p1667 ...
p1671.

### p1672[0] Current setpoint filter 4 type

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Current setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 1 | 2 | [0] 1 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Current setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Hz | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.5 [Hz] | 16000.0 [Hz] | [0] 1999.0 [Hz] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Current setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.001 | 10.000 | [0] 0.700 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the denominator damping for current setpoint filter 4.

**Dependency:** 
  
Current setpoint filter 4 is activated via p1656.3 and parameterized via p1672 ...
p1676.

### p1675[0] Current setpoint filter 4 numerator natural frequency

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Current setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Hz | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.5 [Hz] | 16000.0 [Hz] | [0] 1999.0 [Hz] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the numerator natural frequency for current setpoint filter 4 (general filter).

**Dependency:** 
  
Current setpoint filter 4 is activated via p1656.3 and parameterized via p1672 ...
p1676.

### p1676[0] Current setpoint filter 4 numerator damping

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Current setpoint filter |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.000 | 10.000 | [0] 0.700 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the numerator damping for current setpoint filter 4.

**Dependency:** 
  
Current setpoint filter 4 is activated via p1656.3 and parameterized via p1672 ...
p1676.

### p1703[0] Isq current controller precontrol scaling

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Current controller |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** % | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.0 [%] | 200.0 [%] | [0] 0.0 [%] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the scaling of the dynamic current controller precontrol for the torque-generating
current component Isq.

### p1821[0] Direction of rotation

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Commissioning |  |  |
| **Parameter group:** Motor data |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 1 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Ready for operation |  |  |
| **Parameter group:** Reference variables |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** CALC_MOD_ALL |
| **Unit:** rpm | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 6.00 [rpm] | 210000.00 [rpm] | [0] 3000.00 [rpm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Ready for operation |  |  |
| **Parameter group:** Reference variables |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** CALC_MOD_ALL |
| **Unit:** Arms | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.10 [Arms] | 100000.00 [Arms] | [0] 100.00 [Arms] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the reference quantity for currents.  
All currents specified as relative value are referred to this reference quantity.  
The reference quantity corresponds to 100% or 4000 hex (word) or 4000 0000 hex (double
word).

**Note:** 
  
Default value is 2 * r0305 or the motor current limit.

### p2003 Reference torque

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Ready for operation |  |  |
| **Parameter group:** Reference variables |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** CALC_MOD_ALL |
| **Unit:** Nm | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.01 [Nm] | 20000000.00 [Nm] | [0] 1.00 [Nm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the reference quantity for the torque values.  
All torques specified as relative value are referred to this reference quantity.  
The reference quantity corresponds to 100% or 4000 hex (word) or 4000 0000 hex (double
word).

### r2043.0...2 PROFIdrive PZD state

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Configuration |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source binary |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
| **Data type:**Unsigned16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Receive direction |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source binary/numeric |  | **Scaling:** 4000H |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

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
| **Data type:**Unsigned16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

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
| **Data type:**Integer32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Receive direction |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** 4000H |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

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

### r2109[0...63] Fault removed in milliseconds

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Faults / alarms |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the time in milliseconds referred to the day that the fault was removed.

**Dependency:** 
  
See also:
r0945, r0947, r0948, r0949, r2114, r2130, r2133, r2136, r3122

**Notice:** 
  
The time comprises r2136 (days) and r2109 (milliseconds).

**Note:** 
  
The buffer parameters are cyclically updated in the background.  
The structure of the fault buffer and the assignment of the indices is shown in r0945.

### r2111 Alarm counter

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Faults / alarms |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Diagnostics general |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Faults / alarms |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
This counter is incremented every time the alarm buffer changes.

**Dependency:** 
  
See also:
r2122, r2123, r2124, r2125

### r2122[0...63] Alarm number

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Faults / alarms |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
r2122[0], r2124[0], r2123[0], r2125[0] --> alarm 1 (the oldest)  
. . .  
r2122[7], r2124[7], r2123[7], r2125[7] --> Alarm 8 (the latest)  
  
History of alarms that have gone:  
r2122[8], r2124[8], r2123[8], r2125[8] --> Alarm 1 (the latest)  
. . .  
r2122[63], r2124[63], r2123[63], r2125[63] --> alarm 56 (the oldest)

### r2123[0...63] Alarm received in milliseconds

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Faults / alarms |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the time in milliseconds referred to the day that the alarm occurred.

**Dependency:** 
  
See also:
r2114, r2122, r2124, r2125, r2134, r2145, r2146, r3123

**Notice:** 
  
The time comprises r2145 (days) and r2123 (milliseconds).

**Note:** 
  
The buffer parameters are cyclically updated in the background.  
The structure of the alarm buffer and the assignment of the indices is shown in r2122.

### r2124[0...63] Alarm value

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Faults / alarms |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays additional information about the active alarm (as integer number).

**Dependency:** 
  
See also:
r2122, r2123, r2125, r2134, r2145, r2146, r3123

**Note:** 
  
The buffer parameters are cyclically updated in the background.  
The structure of the alarm buffer and the assignment of the indices are shown in r2122.

### r2125[0...63] Alarm removed in milliseconds

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Faults / alarms |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the time in milliseconds referred to the day that the alarm was removed.

**Dependency:** 
  
See also:
r2114, r2122, r2123, r2124, r2134, r2145, r2146, r3123

**Notice:** 
  
The time comprises r2146 (days) and r2125 (milliseconds).

**Note:** 
  
The buffer parameters are cyclically updated in the background.  
The structure of the alarm buffer and the assignment of the indices is shown in r2122.

### r2130[0...63] Fault received in days

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Faults / alarms |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the time in days referred to the day that the fault occurred.

**Dependency:** 
  
See also:
r0945, r0947, r0948, r0949, r2109, r2114, r2133, r2136, r3122

**Notice:** 
  
The time comprises r2130 (days) and r0948 (milliseconds).

**Note:** 
  
The buffer parameters are cyclically updated in the background.

### r2131 Actual fault number

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Faults / alarms |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the number of the active fault that last occurred.

**Note:** 
  
0: No fault present.

### r2132 Actual alarm number

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Faults / alarms |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the number of the alarm that last occurred.

**Note:** 
  
0: No alarm present.

### r2133[0...63] Fault value for float values

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Faults / alarms |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the additional information about the fault that occurred for float values.  
Refer to the fault for the interpretation of the fault value.

**Dependency:** 
  
See also:
r0945, r0947, r0948, r0949, r2109, r2130, r2136

**Note:** 
  
The buffer parameters are cyclically updated in the background.

### r2134[0...63] Alarm value for float values

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Faults / alarms |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the additional information about the alarm that occurred for float values.  
Refer to the alarm for an interpretation of the alarm value.

**Dependency:** 
  
See also:
r2122, r2123, r2124, r2125, r2145, r2146, r3123

**Note:** 
  
The buffer parameters are cyclically updated in the background.

### r2136[0...63] Fault removed in days

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Faults / alarms |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the time in days referred to the day when the fault was removed.

**Dependency:** 
  
See also:
r0945, r0947, r0948, r0949, r2109, r2114, r2130, r2133, r3122

**Notice:** 
  
The time comprises r2136 (days) and r2109 (milliseconds).

**Note:** 
  
The buffer parameters are cyclically updated in the background.

### r2139.0...15 Status word faults/alarms

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Faults / alarms |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source binary/numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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

### r2145[0...63] Alarm received in days

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Faults / alarms |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the time in days referred to the day that the alarm occurred.

**Dependency:** 
  
See also:
r2114, r2122, r2123, r2124, r2125, r2134, r2146, r3123

**Notice:** 
  
The time comprises r2145 (days) and r2123 (milliseconds).

**Note:** 
  
The buffer parameters are cyclically updated in the background.

### r2146[0...63] Alarm cleared in days

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Faults / alarms |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the time in days referred to the day when the alarm was cleared.

**Dependency:** 
  
See also:
r2114, r2122, r2123, r2124, r2125, r2134, r2145, r3123

**Notice:** 
  
The time comprises r2146 (days) and r2125 (milliseconds).

**Note:** 
  
The buffer parameters are cyclically updated in the background.

### p2175[0] Motor blocked speed threshold

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Speed messages |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** CALC_MOD_LIM_REF |
| **Unit:** rpm | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [rpm] | 210000.00 [rpm] | [0] 120.00 [rpm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the speed threshold for message "Motor blocked".  
Monitoring is deactivated with p2175 = 0.

**Dependency:** 
  
See also:
F07900

**Note:** 
  
If the motor speed is less than the threshold value set in p2175 - and the motor is
operated for longer than 200 ms at the torque limit - then the motor is shut down
and a fault is output.

### r2199.0...11 Status word monitoring 3

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Speed messages, Control/status words |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source binary/numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Displays the third status word of the monitoring functions.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | |n_act| < p2161 | No | Yes | 8010 |
| 01 | f or n comparison value reached or exceeded | No | Yes | 8010 |
| 04 | Speed setpoint - actual value deviation in tolerance t_on | No | Yes | 8011 |
| 05 | Ramp-up/ramp-down completed | No | Yes | 8011 |
| 11 | Torque utilization < torque threshold value 2 | No | Yes | 8012 |

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

[S210](#p2496-lr-dimension-system-physical-length-units-1)

[S210 EPOS load side, rotating](#p2496-lr-dimension-system-physical-length-units-2)

#### p2496 LR dimension system physical length units

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Commissioning |  |  |
| **Parameter group:** Position control |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 8 | [0] 3 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Variant:**S210 (EPOS load side, rotating) |  |  |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Commissioning |  |  |
| **Parameter group:** Position control |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 10 | [0] 10 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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

[S210](#p2497-lr-dimension-system-physical-velocity-1)

[S210 EPOS load side, rotating](#p2497-lr-dimension-system-physical-velocity-2)

#### p2497 LR dimension system physical velocity

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Commissioning |  |  |
| **Parameter group:** Position control, Mechanics |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 15 | [0] 8 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Variant:**S210 (EPOS load side, rotating) |  |  |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Commissioning |  |  |
| **Parameter group:** Position control, Mechanics |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 18 | [0] 18 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the physical unit for the velocities.

**Value:** 
  
0:
1000LU/min (no dimension)  
18:
°/s

### p2498 LR dimension system physical acceleration

[S210](#p2498-lr-dimension-system-physical-acceleration-1)

[S210 EPOS load side, rotating](#p2498-lr-dimension-system-physical-acceleration-2)

#### p2498 LR dimension system physical acceleration

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Commissioning |  |  |
| **Parameter group:** Position control, Mechanics |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 11 | [0] 7 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Variant:**S210 (EPOS load side, rotating) |  |  |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Commissioning |  |  |
| **Parameter group:** Position control, Mechanics |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 18 | [0] 18 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the physical unit for the accelerations.

**Value:** 
  
0:
1000LU/s² (no dimension)  
18:
°/s²

### p2499 LR dimension system physical jerk

[S210](#p2499-lr-dimension-system-physical-jerk-1)

[S210 EPOS load side, rotating](#p2499-lr-dimension-system-physical-jerk-2)

#### p2499 LR dimension system physical jerk

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Commissioning |  |  |
| **Parameter group:** Position control, Mechanics |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 11 | [0] 7 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Variant:**S210 (EPOS load side, rotating) |  |  |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Commissioning |  |  |
| **Parameter group:** Position control, Mechanics |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 18 | [0] 18 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Commissioning |  |  |
| **Parameter group:** Mechanics, Actual position value preprocessing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 1 | [0] 1 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Setting to assign the encoder.  
The actual value preprocessing and the closed-loop position control are carried out
using the assigned encoder.

**Value:** 
  
0:
No encoder  
1:
Motor encoder

**Dependency:** 
  
See also:
p0187, p0188

**Notice:** 
  
For the setting p2502 = 0 (no encoder), closed-loop position control is not possible.
This setting is only practical as supportive measure to implement encoderless closed-loop
speed control (e.g. if the motor encoder is defective).

**Note:** 
  
An encoder data set must be assigned to the assigned encoder (p2502 = 1, 2, 3).

### p2503[0] LR length unit MU per 10 mm

[S210](#p25030-lr-length-unit-mu-per-10-mm-1)

[S210 EPOS load side, rotating](#p25030-lr-length-unit-mu-per-10-mm-2)

#### p2503[0] LR length unit MU per 10 mm

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Commissioning |  |  |
| **Parameter group:** Position control |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.000001 [mm] | 2147483650.000000 [mm] | [0] 10.000000 [mm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Variant:**S210 (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Commissioning |  |  |
| **Parameter group:** Position control |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.000001 [°] | 2147483650.000000 [°] | [0] 10.000000 [°] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Commissioning |  |  |
| **Parameter group:** Position control, Mechanics |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 1 | 1048576 | [0] 1 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Commissioning |  |  |
| **Parameter group:** Position control, Mechanics |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| -1048576 | 1048576 | [0] 1 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the load revolutions for the gearbox factor between the motor shaft and load
shaft.  
Gearbox factor = motor revolutions (p2504) / load revolutions (p2505)

**Dependency:** 
  
See also:
p2504

### p2506[0] LR length unit MU per load distance

[S210](#p25060-lr-length-unit-mu-per-load-distance-1)

[S210 EPOS load side, rotating](#p25060-lr-length-unit-mu-per-load-revolution)

#### p2506[0] LR length unit MU per load distance

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Commissioning |  |  |
| **Parameter group:** Position control, Mechanics |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.000001 [mm] | 2147483650.000000 [mm] | [0] 10.000000 [mm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the length unit MU per load distance set by the user.  
For a rotary encoder, this establishes a reference between the actual physical situation
and the user-specific length unit MU.  
Example:  
Rotary encoder, ballscrew with 10 mm/revolution, 10 mm should be broken down to units
of µm.  
Length unit LU (p2496 = 0)  
--> One load distance corresponds to 10000 LU (i.e. 1 LU = 1 µm)  
--> p2506 = 10000  
  
Physical unit µm (2496) = 4  
--> One load distance corresponds to 10000 µm  
--> p2506 = 10000

**Dependency:** 
  
See also:
p2496

#### p2506[0] LR length unit MU per load revolution

|  |  |  |
| --- | --- | --- |
| **Variant:**S210 (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Commissioning |  |  |
| **Parameter group:** Position control, Mechanics |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.000001 [°] | 2147483650.000000 [°] | [0] 360.000000 [°] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the rotary unit MU per load revolution set by the user. For a rotary encoder,
this establishes a reference between the physical arrangement and the user-specific
rotating unit MU.  
Example:  
Rotating unit LU (p2496 = 0)  
Rotary encoder, 1 revolution should be broken down into mdegrees, (i.e. 1 LU = 1 mdegrees).  
--> One load revolution corresponds to 360000 LU  
--> p2506 = 360000

**Dependency:** 
  
See also:
p2496

**Note:** 
  
When selecting a physical length unit, the drive automatically preassigns the parameter
and it cannot be changed.

### p2507[0...n] LR absolute encoder adjustment status

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Position control |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** EDS n defined by: p0140 |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 4 | [0] 1 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Activates the adjustment and display of the status of the adjustment for absolute
encoders.  
For p2507 = 2:  
This initiates encoder adjustment. The status is displayed using the other values.  
For p2507 = 4:  
This means that the encoder adjustment offset (p2525) can be directly accepted after
new commissioning, without having to approach the adjustment point.

**Value:** 
  
0:
Error occurred while adjusting  
1:
Absolute encoder not adjusted  
2:
Absolute encoder not adjusted and encoder adjustment initiated  
3:
Absolute encoder adjusted  
4:
Absolute encoder adjustment by accepting the offset

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
For p2507 = 4:  
For an adjustment where the offset is accepted, the position actual value manifests
a step.

**Note:** 
  
To permanently accept the determined position offset (p2525) and the DDS number, they
must be saved in a non-volatile fashion (p0977).  
This adjustment can only be initiated for an absolute encoder.

### c2510[0...3] LR selecting measuring probe evaluation

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
Encoder 2  
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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
Encoder 2  
[
3]:
Reserved

**Dependency:** 
  
See also:
p2502, c2510

### r2521[0...3] LR position actual value

[S210](#r252103-lr-position-actual-value-1)

[S210 EPOS load side, rotating](#r252103-lr-position-actual-value-2)

#### r2521[0...3] LR position actual value

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Jog, Homing, Traversing blocks, Direct setpoint input (MDI), Actual position value preprocessing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
Encoder 2  
[
3]:
Reserved

**Dependency:** 
  
See also:
p2502, r2526

**Note:** 
  
r2526.0 = 1 --> The position actual value in r2521[0] for the position control is
valid.  
r2527.0 = 1 --> The position actual value in r2521[1] for encoder 1 is valid.  
r2528.0 = 1 --> The position actual value in r2521[2] for encoder 2 is valid.  
r2529.0 = 1 --> The position actual value in r2521[3] for encoder 3 is valid.

#### r2521[0...3] LR position actual value

|  |  |  |
| --- | --- | --- |
| **Variant:**S210 (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Jog, Homing, Traversing blocks, Direct setpoint input (MDI), Actual position value preprocessing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
Encoder 2  
[
3]:
Reserved

**Dependency:** 
  
See also:
p2502, r2526

**Note:** 
  
r2526.0 = 1 --> The position actual value in r2521[0] for the position control is
valid.  
r2527.0 = 1 --> The position actual value in r2521[1] for encoder 1 is valid.  
r2528.0 = 1 --> The position actual value in r2521[2] for encoder 2 is valid.  
r2529.0 = 1 --> The position actual value in r2521[3] for encoder 3 is valid.

### r2522[0...3] LR velocity actual value

[S210](#r252203-lr-velocity-actual-value-1)

[S210 EPOS load side, rotating](#r252203-lr-velocity-actual-value-2)

#### r2522[0...3] LR velocity actual value

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Jog, Homing, Traversing blocks, Direct setpoint input (MDI), Actual position value preprocessing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm/s | **Unit group:** 11_3 | **Unit selection:** p2497 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
Encoder 2  
[
3]:
Reserved

**Dependency:** 
  
See also:
p2502, r2526

**Note:** 
  
r2526.0 = 1 --> The velocity actual value in r2522[0] for the position control is
valid.  
r2527.0 = 1 --> The velocity actual value in r2522[1] for encoder 1 is valid.  
r2528.0 = 1 --> The velocity actual value in r2522[2] for encoder 2 is valid.  
r2529.0 = 1 --> The velocity actual value in r2522[3] for encoder 3 is valid.

#### r2522[0...3] LR velocity actual value

|  |  |  |
| --- | --- | --- |
| **Variant:**S210 (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Jog, Homing, Traversing blocks, Direct setpoint input (MDI), Actual position value preprocessing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** °/s | **Unit group:** 11_4 | **Unit selection:** p2497 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
Encoder 2  
[
3]:
Reserved

**Dependency:** 
  
See also:
p2502, r2526

**Note:** 
  
r2526.0 = 1 --> The velocity actual value in r2522[0] for the position control is
valid.  
r2527.0 = 1 --> The velocity actual value in r2522[1] for encoder 1 is valid.  
r2528.0 = 1 --> The velocity actual value in r2522[2] for encoder 2 is valid.  
r2529.0 = 1 --> The velocity actual value in r2522[3] for encoder 3 is valid.

### r2523[0...3] LR measured value

[S210](#r252303-lr-measured-value-1)

[S210 EPOS load side, rotating](#r252303-lr-measured-value-2)

#### r2523[0...3] LR measured value

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Position control |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
Encoder 2  
[
3]:
Reserved

**Dependency:** 
  
See also:
p2502, r2526

**Note:** 
  
r2526.2 = 1 --> The measured value in r2523[0] for the position control is valid.  
r2527.2 = 1 --> The measured value in r2523[1] for encoder 1 is valid.  
r2528.2 = 1 --> The measured value in r2523[2] for encoder 2 is valid.  
r2529.2 = 1 --> The measured value in r2523[3] for encoder 3 is valid.

#### r2523[0...3] LR measured value

|  |  |  |
| --- | --- | --- |
| **Variant:**S210 (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Position control |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
Encoder 2  
[
3]:
Reserved

**Dependency:** 
  
See also:
p2502, r2526

**Note:** 
  
r2526.2 = 1 --> The measured value in r2523[0] for the position control is valid.  
r2527.2 = 1 --> The measured value in r2523[1] for encoder 1 is valid.  
r2528.2 = 1 --> The measured value in r2523[2] for encoder 2 is valid.  
r2529.2 = 1 --> The measured value in r2523[3] for encoder 3 is valid.

## SINAMICS Parameter S210 02526 - 02617

SINAMICS Parameter S210 02526 - 02617

### r2526.0...12 LR status word

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Actual position value preprocessing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source binary/numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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

[S210](#c2530-lr-position-setpoint-1)

[S210 EPOS load side, rotating](#c2530-lr-position-setpoint-2)

#### c2530 LR position setpoint

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Signal for the position setpoint of the position controller.

**Dependency:** 
  
See also:
r2665

#### c2530 LR position setpoint

|  |  |  |
| --- | --- | --- |
| **Variant:**S210 (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Signal for the position setpoint of the position controller.

**Dependency:** 
  
See also:
r2665

### c2531 LR velocity setpoint

[S210](#c2531-lr-velocity-setpoint-1)

[S210 EPOS load side, rotating](#c2531-lr-velocity-setpoint-2)

#### c2531 LR velocity setpoint

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Signal for the velocity setpoint of the position controller.

**Dependency:** 
  
See also:
r2666

#### c2531 LR velocity setpoint

|  |  |  |
| --- | --- | --- |
| **Variant:**S210 (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Signal for the velocity setpoint of the position controller.

**Dependency:** 
  
See also:
r2666

### p2533[0] LR position setpoint filter time constant

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Position controller |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [ms] | 1000.00 [ms] | [0] 0.00 [ms] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Position controller |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** % | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [%] | 200.00 [%] | [0] 0.00 [%] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Setting for activation and weighting of the speed precontrol value.  
Value = 0 % --> The precontrol is deactivated.

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Position controller |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 | 2.00 | [0] 0.00 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the "fractional" dead time to emulate the timing behavior of the speed control
loop.  
The selected multiplier refers to the position controller sampling time (dead time=
p2535 * position controller clock cycle).

**Dependency:** 
  
See also:
p2536

**Notice:** 
  
When speed precontrol is active (p2534 > 0 %), the following applies:  
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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Position controller |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [ms] | 100.00 [ms] | [0] 0.00 [ms] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Position controller |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** 1000 rpm | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.000 [1000 rpm] | 300.000 [1000 rpm] | [0] 1.000 [1000 rpm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Position controller |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [ms] | 100000.00 [ms] | [0] 0.00 [ms] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Setting to activate the integral time of the position controller.  
Value = 0 ms --> The I component of the position controller is deactivated.

**Dependency:** 
  
See also:
p2538, r2559

### p2540 LR position controller output speed limit

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Position controller |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** rpm | **Unit group:** 3_1 | **Unit selection:** p0505 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2000 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.000 [rpm] | 210000.000 [rpm] | [0] 210000.000 [rpm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the speed limit of the position controller output.

**Dependency:** 
  
See also:
c2541

### c2541 LR position controller output speed limit signal

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Signal for limiting the position controller output.

**Dependency:** 
  
See also:
p2540

### p2542 LR standstill window

[S210](#p2542-lr-standstill-window-1)

[S210 EPOS load side, rotating](#p2542-lr-standstill-window-2)

#### p2542 LR standstill window

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Position controller monitoring |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.0000 [mm] | 2147483904.0000 [mm] | [0] 0.2500 [mm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the standstill window for the standstill monitoring function.  
After the standstill monitoring time expires, it is cyclically checked whether the
difference between the setpoint and actual position is located within the standstill
window and, if required, an appropriate fault is output.  
Value = 0 --> The standstill monitoring is deactivated.

**Dependency:** 
  
See also:
p2543, p2544

**Note:** 
  
The following applies for the setting of the standstill window and positioning window:  
Standstill window (p2542) >= positioning window (p2544)

#### p2542 LR standstill window

|  |  |  |
| --- | --- | --- |
| **Variant:**S210 (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Position controller monitoring |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.0000 [°] | 2147483904.0000 [°] | [0] 10.0000 [°] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the standstill window for the standstill monitoring function.  
After the standstill monitoring time expires, it is cyclically checked whether the
difference between the setpoint and actual position is located within the standstill
window and, if required, an appropriate fault is output.  
Value = 0 --> The standstill monitoring is deactivated.

**Dependency:** 
  
See also:
p2543, p2544

**Note:** 
  
The following applies for the setting of the standstill window and positioning window:  
Standstill window (p2542) >= positioning window (p2544)

### p2543 LR standstill monitoring time

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Position controller monitoring |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [ms] | 100000.00 [ms] | [0] 200.00 [ms] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
Standstill monitoring time (p2543) <= positioning monitoring time (p2545)

### p2544 LR positioning window

[S210](#p2544-lr-positioning-window-1)

[S210 EPOS load side, rotating](#p2544-lr-positioning-window-2)

#### p2544 LR positioning window

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Position controller monitoring |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.0000 [mm] | 2147483904.0000 [mm] | [0] 0.0500 [mm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the positioning window for the positioning monitoring function.  
After the positioning monitoring time expires, it is checked once as to whether the
difference between the setpoint and actual position lies within the positioning window
and if required an appropriate fault is output.  
Value = 0 --> The positioning monitoring function is deactivated.

**Dependency:** 
  
See also:
p2542, p2545, r2684

**Note:** 
  
The following applies for the setting of the standstill and positioning window:  
Standstill window (p2542) >= positioning window (p2544)

#### p2544 LR positioning window

|  |  |  |
| --- | --- | --- |
| **Variant:**S210 (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Position controller monitoring |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.0000 [°] | 2147483904.0000 [°] | [0] 2.0000 [°] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the positioning window for the positioning monitoring function.  
After the positioning monitoring time expires, it is checked once as to whether the
difference between the setpoint and actual position lies within the positioning window
and if required an appropriate fault is output.  
Value = 0 --> The positioning monitoring function is deactivated.

**Dependency:** 
  
See also:
p2542, p2545, r2684

**Note:** 
  
The following applies for the setting of the standstill and positioning window:  
Standstill window (p2542) >= positioning window (p2544)

### p2545 LR positioning monitoring time

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Position controller monitoring |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [ms] | 100000.00 [ms] | [0] 1000.00 [ms] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
Standstill monitoring time (p2543) <= positioning monitoring time (p2545)

### p2546[0] LR dynamic following error monitoring tolerance

[S210](#p25460-lr-dynamic-following-error-monitoring-tolerance-1)

[S210 EPOS load side, rotating](#p25460-lr-dynamic-following-error-monitoring-tolerance-2)

#### p2546[0] LR dynamic following error monitoring tolerance

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Position controller monitoring |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.0000 [mm] | 2147483904.0000 [mm] | [0] 1.0000 [mm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the tolerance for the dynamic following error monitoring.  
If the dynamic following error (r2563) exceeds the selected tolerance, then an appropriate
fault is output.  
Value = 0 --> The dynamic following error monitoring is deactivated.

**Dependency:** 
  
See also:
r2563, r2684

**Note:** 
  
The tolerance bandwidth is intended to prevent the dynamic following error monitoring
incorrectly responding due to operational control sequences (e.g. during load surges).

#### p2546[0] LR dynamic following error monitoring tolerance

|  |  |  |
| --- | --- | --- |
| **Variant:**S210 (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Position controller monitoring |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.0000 [°] | 2147483904.0000 [°] | [0] 36.0000 [°] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the tolerance for the dynamic following error monitoring.  
If the dynamic following error (r2563) exceeds the selected tolerance, then an appropriate
fault is output.  
Value = 0 --> The dynamic following error monitoring is deactivated.

**Dependency:** 
  
See also:
r2563, r2684

**Note:** 
  
The tolerance bandwidth is intended to prevent the dynamic following error monitoring
incorrectly responding due to operational control sequences (e.g. during load surges).

### r2556 LR position setpoint after setpoint smoothing

[S210](#r2556-lr-position-setpoint-after-setpoint-smoothing-1)

[S210 EPOS load side, rotating](#r2556-lr-position-setpoint-after-setpoint-smoothing-2)

#### r2556 LR position setpoint after setpoint smoothing

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Position controller |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Displays the position setpoint after the setpoint smoothing.

#### r2556 LR position setpoint after setpoint smoothing

|  |  |  |
| --- | --- | --- |
| **Variant:**S210 (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Position controller |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Displays the position setpoint after the setpoint smoothing.

### r2557 LR position controller input system deviation

[S210](#r2557-lr-position-controller-input-system-deviation-1)

[S210 EPOS load side, rotating](#r2557-lr-position-controller-input-system-deviation-2)

#### r2557 LR position controller input system deviation

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Position controller |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Displays the difference between the position setpoint and the position actual value
at the position controller input.

#### r2557 LR position controller input system deviation

|  |  |  |
| --- | --- | --- |
| **Variant:**S210 (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Position controller |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Displays the difference between the position setpoint and the position actual value
at the position controller input.

### r2558 LR position controller output P component

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Position controller |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** rpm | **Unit group:** 3_1 | **Unit selection:** p0505 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2000 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Displays the P component at the output of the position controller (speed setpoint).

### r2559 LR position controller output I component

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Position controller |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** rpm | **Unit group:** 3_1 | **Unit selection:** p0505 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2000 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Displays the I component at the output of the position controller (speed setpoint).

### r2560 LR speed setpoint

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Position controller |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** rpm | **Unit group:** 3_1 | **Unit selection:** p0505 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2000 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Displays the speed setpoint after limiting (c2541).

### r2561 LR speed precontrol value

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Position controller |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** rpm | **Unit group:** 3_1 | **Unit selection:** p0505 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2000 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Displays the speed setpoint due to the precontrol.

### r2562 LR total speed setpoint

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Position controller |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** rpm | **Unit group:** 3_1 | **Unit selection:** p0505 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2000 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Displays the total speed setpoint  
This value is obtained from the sum of the speed precontrol and position controller
output.

**Dependency:** 
  
See also:
r2560, r2561

### r2563 LR following error dynamic model

[S210](#r2563-lr-following-error-dynamic-model-1)

[S210 EPOS load side, rotating](#r2563-lr-following-error-dynamic-model-2)

#### r2563 LR following error dynamic model

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Jog, Homing, Traversing blocks, Direct setpoint input (MDI), Position controller monitoring |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Displays the dynamic following error.  
This value is the deviation, corrected by the velocity-dependent component, between
the position setpoint and the position actual value.

**Note:** 
  
For p2534 >= 100 % (precontrol activated) the following applies:  
The dynamic following error (r2563) corresponds to the system deviation (r2557) at
the position controller input.  
For 0 % < p2534 < 100 % (precontrol activated) or p2534 = 0 % (precontrol deactivated)
the following applies:  
The dynamic following error (r2563) is the deviation between the measured position
actual value and a value that is calculated from the position setpoint via a PT1 model.
This compensates the system-related velocity-dependent system deviation for a P controller.

#### r2563 LR following error dynamic model

|  |  |  |
| --- | --- | --- |
| **Variant:**S210 (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Jog, Homing, Traversing blocks, Direct setpoint input (MDI), Position controller monitoring |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Displays the dynamic following error.  
This value is the deviation, corrected by the velocity-dependent component, between
the position setpoint and the position actual value.

**Note:** 
  
For p2534 >= 100 % (precontrol activated) the following applies:  
The dynamic following error (r2563) corresponds to the system deviation (r2557) at
the position controller input.  
For 0 % < p2534 < 100 % (precontrol activated) or p2534 = 0 % (precontrol deactivated)
the following applies:  
The dynamic following error (r2563) is the deviation between the measured position
actual value and a value that is calculated from the position setpoint via a PT1 model.
This compensates the system-related velocity-dependent system deviation for a P controller.

### r2564 LR torque precontrol value

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Position controller |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Nm | **Unit group:** 7_1 | **Unit selection:** p0505 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2003 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Displays the torque precontrol value.

**Note:** 
  
The torque precontrol value is the derivation over time of the speed precontrol value
and is referred to a moment of inertia of 1 kgm^2/2 PI. When using the precontrol,
then this should be evaluated corresponding to the actual moment of inertia.

### r2565 LR following error actual

[S210](#r2565-lr-following-error-actual-1)

[S210 EPOS load side, rotating](#r2565-lr-following-error-actual-2)

#### r2565 LR following error actual

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Position controller |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Displays the actual following error.  
This value is the deviation between the position setpoint - after fine interpolation
- and the position actual value.

**Notice:** 
  
When speed precontrol is active (p2534 > 0 %), the following applies:  
To calculate this value, the position setpoint is delayed by two position controller
sampling times.  
When speed precontrol is inactive (p2534 = 0 %), the following applies:  
To calculate this value, the position setpoint is delayed by two position controller
clock cycles.

#### r2565 LR following error actual

|  |  |  |
| --- | --- | --- |
| **Variant:**S210 (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Position controller |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Displays the actual following error.  
This value is the deviation between the position setpoint - after fine interpolation
- and the position actual value.

**Notice:** 
  
When speed precontrol is active (p2534 > 0 %), the following applies:  
To calculate this value, the position setpoint is delayed by two position controller
sampling times.  
When speed precontrol is inactive (p2534 = 0 %), the following applies:  
To calculate this value, the position setpoint is delayed by two position controller
clock cycles.

### p2567[0] LR torque precontrol moment of inertia

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Position controller |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** kgm² | **Unit group:** 25_1 | **Unit selection:** p0100 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.000000 [kgm²] | 100000.000000 [kgm²] | [0] 0.000000 [kgm²] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Data type:**Unsigned8 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Limit |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink binary |  |  |
| **Factory interconnection:** | **Fixed value:** |  |
| 1:722.1 | 1 |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Signal for the hardware limit switch in the negative direction of travel.

**Recommendation:** 
  
Set the OFF3 ramp-down time (p1135) so that after the axis reaches the hardware limit
switch at maximum velocity, the braking distance traveled by the axis is not greater
than the distance that is available.  
Sets message 07491 as alarm (A07491):  
Set the maximum deceleration (p2573) so that after the axis reaches the hardware limit
switch at maximum velocity, the braking distance traveled by the axis is not greater
than the distance that is available.

**Dependency:** 
  
See also:
p1135, c2568, c2570, p2573, r2684

**Caution:** 
  
The hardware limit switch is low active.  
Sets message 07491 as fault (F07491):  
For a 0 signal, the drive stops with the OFF3 ramp-down time (p1135), status signal
r2684.13 = 1 is set, saved and the corresponding fault is output. After the fault
has been acknowledged, only motion moving away from the hardware limit switch is permitted.  
For a 0/1 signal and valid travel direction, when the hardware limit switch is exited,
this is detected and status signal r2684.13 is set to 0.  
Sets message 07491 as alarm (A07491):  
For a 0 signal, the axis is stopped with the maximum deceleration (p2573), status
signal r2684.13 is set to 1, saved and the appropriate alarm is output. Only motion
away from the hardware limit switch is permitted.  
For a 0/1 signal and valid travel direction, when the hardware limit switch is exited,
this is detected and status signal r2684.13 is set to 0 and the alarm is cleared.

### c2570 EPOS positive hardware limit switch

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Limit |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink binary |  |  |
| **Factory interconnection:** | **Fixed value:** |  |
| 1:722.4 | 1 |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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

[S210](#p2571-epos-maximum-velocity-1)

[S210 EPOS load side, rotating](#p2571-epos-maximum-velocity-2)

#### p2571 EPOS maximum velocity

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Limit |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm/s | **Unit group:** 11_3 | **Unit selection:** p2497 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.010 [mm/s] | 40000000.000 [mm/s] | [0] 500.000 [mm/s] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Variant:**S210 (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Limit |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** °/s | **Unit group:** 11_4 | **Unit selection:** p2497 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.010 [°/s] | 40000000.000 [°/s] | [0] 18000.000 [°/s] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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

[S210](#p2572-epos-maximum-acceleration-1)

[S210 EPOS load side, rotating](#p2572-epos-maximum-acceleration-2)

#### p2572 EPOS maximum acceleration

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Ready for operation |  |  |
| **Parameter group:** Limit, Jog |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm/s² | **Unit group:** 12_3 | **Unit selection:** p2498 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.001 [mm/s²] | 2000000.000 [mm/s²] | [0] 10000.000 [mm/s²] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Variant:**S210 (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Ready for operation |  |  |
| **Parameter group:** Limit, Jog |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** °/s² | **Unit group:** 12_4 | **Unit selection:** p2498 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.001 [°/s²] | 2000000.000 [°/s²] | [0] 360000.000 [°/s²] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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

[S210](#p2573-epos-maximum-deceleration-1)

[S210 EPOS load side, rotating](#p2573-epos-maximum-deceleration-2)

#### p2573 EPOS maximum deceleration

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Ready for operation |  |  |
| **Parameter group:** Limit, Jog |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm/s² | **Unit group:** 12_3 | **Unit selection:** p2498 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.001 [mm/s²] | 2000000.000 [mm/s²] | [0] 10000.000 [mm/s²] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Variant:**S210 (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Ready for operation |  |  |
| **Parameter group:** Limit, Jog |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** °/s² | **Unit group:** 12_4 | **Unit selection:** p2498 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.001 [°/s²] | 2000000.000 [°/s²] | [0] 360000.000 [°/s²] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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

[S210](#p2574-epos-jerk-limiting-1)

[S210 EPOS load side, rotating](#p2574-epos-jerk-limiting-2)

#### p2574 EPOS jerk limiting

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Limit |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm/s³ | **Unit group:** 13_3 | **Unit selection:** p2499 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.001 [mm/s³] | 100000000.000 [mm/s³] | [0] 200000.000 [mm/s³] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Variant:**S210 (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Limit |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** °/s³ | **Unit group:** 13_4 | **Unit selection:** p2499 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.001 [°/s³] | 100000000.000 [°/s³] | [0] 7200000.000 [°/s³] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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

[S210](#p2576-epos-modulo-correction-modulo-range-1)

[S210 EPOS load side, rotating](#p2576-epos-modulo-correction-modulo-range-2)

#### p2576 EPOS modulo correction modulo range

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Ready for operation |  |  |
| **Parameter group:** Basic positioner, Mechanics, Actual position value preprocessing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.0001 [mm] | 2147482752.0000 [mm] | [0] 360.0000 [mm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the modulo range for axes with modulo correction.

**Dependency:** 
  
See also:
c2577

#### p2576 EPOS modulo correction modulo range

|  |  |  |
| --- | --- | --- |
| **Variant:**S210 (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Ready for operation |  |  |
| **Parameter group:** Basic positioner, Mechanics, Actual position value preprocessing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.0001 [°] | 2147482752.0000 [°] | [0] 360.0000 [°] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the modulo range for axes with modulo correction.

**Dependency:** 
  
See also:
c2577

### c2577 EPOS modulo correction activation

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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

[S210](#c2578-epos-negative-software-limit-switch-1)

[S210 EPOS load side, rotating](#c2578-epos-negative-software-limit-switch-2)

#### c2578 EPOS negative software limit switch

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
Negative software limit switch < positive software limit switch

#### c2578 EPOS negative software limit switch

|  |  |  |
| --- | --- | --- |
| **Variant:**S210 (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
Negative software limit switch < positive software limit switch

### c2579 EPOS positive software limit switch

[S210](#c2579-epos-positive-software-limit-switch-1)

[S210 EPOS load side, rotating](#c2579-epos-positive-software-limit-switch-2)

#### c2579 EPOS positive software limit switch

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
Negative software limit switch < positive software limit switch

#### c2579 EPOS positive software limit switch

|  |  |  |
| --- | --- | --- |
| **Variant:**S210 (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
Negative software limit switch < positive software limit switch

### p2580 EPOS negative software limit switch

[S210](#p2580-epos-negative-software-limit-switch-1)

[S210 EPOS load side, rotating](#p2580-epos-negative-software-limit-switch-2)

#### p2580 EPOS negative software limit switch

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Limit |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Min:** | **Max:** | **Factory setting:** |
| -2147482752.0000 [mm] | 2147482752.0000 [mm] | [0] -2147482752.0000 [mm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the software limit switch, in the negative direction of travel.

**Dependency:** 
  
See also:
c2578, c2579, p2581, c2582

#### p2580 EPOS negative software limit switch

|  |  |  |
| --- | --- | --- |
| **Variant:**S210 (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Limit |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Min:** | **Max:** | **Factory setting:** |
| -2147482752.0000 [°] | 2147482752.0000 [°] | [0] -2147482752.0000 [°] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the software limit switch, in the negative direction of travel.

**Dependency:** 
  
See also:
c2578, c2579, p2581, c2582

### p2581 EPOS positive software limit switch

[S210](#p2581-epos-positive-software-limit-switch-1)

[S210 EPOS load side, rotating](#p2581-epos-positive-software-limit-switch-2)

#### p2581 EPOS positive software limit switch

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Limit |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Min:** | **Max:** | **Factory setting:** |
| -2147482752.0000 [mm] | 2147482752.0000 [mm] | [0] 2147482752.0000 [mm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the software limit switch, in the positive direction of travel.

**Dependency:** 
  
See also:
c2578, c2579, p2580, c2582

#### p2581 EPOS positive software limit switch

|  |  |  |
| --- | --- | --- |
| **Variant:**S210 (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Limit |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Min:** | **Max:** | **Factory setting:** |
| -2147482752.0000 [°] | 2147482752.0000 [°] | [0] 2147482752.0000 [°] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the software limit switch, in the positive direction of travel.

**Dependency:** 
  
See also:
c2578, c2579, p2580, c2582

### c2582 EPOS software limit switch activation

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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

[S210](#p2583-epos-backlash-compensation-1)

[S210 EPOS load side, rotating](#p2583-epos-backlash-compensation-2)

#### p2583 EPOS backlash compensation

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Basic positioner |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| -200000.0000 [mm] | 200000.0000 [mm] | [0] 0.0000 [mm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the amount of play (backlash) for positive or negative play.  
0: backlash compensation is deactivated.  
> 0: Positive backlash (normal case)  
When the direction is reversed, the encoder actual value leads the actual value.  
< 0: Negative backlash  
When the direction is reversed, the actual value leads the encoder actual value.

**Dependency:** 
  
If a stationary axis is referenced by "setting the home position", or an adjusted
with absolute encoder is switched on, then the setting of c2604 is relevant for entering
the compensation value.  
c2604 = 1:  
Traveling in the positive direction -> A compensation value is immediately entered.  
Traveling in the negative direction -> A compensation value is not entered  
c2604 = 0:  
Traveling in the positive direction -> A compensation value is not entered  
Traveling in the negative direction -> A compensation value is immediately entered.  
When again setting the home position (a homed axis) or for "passive homing", c2604
is not relevant but instead the history of the axis.  
See also:
c2604

#### p2583 EPOS backlash compensation

|  |  |  |
| --- | --- | --- |
| **Variant:**S210 (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Basic positioner |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| -200000.0000 [°] | 200000.0000 [°] | [0] 0.0000 [°] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the amount of play (backlash) for positive or negative play.  
0: backlash compensation is deactivated.  
> 0: Positive backlash (normal case)  
When the direction is reversed, the encoder actual value leads the actual value.  
< 0: Negative backlash  
When the direction is reversed, the actual value leads the encoder actual value.

**Dependency:** 
  
If a stationary axis is referenced by "setting the home position", or an adjusted
with absolute encoder is switched on, then the setting of c2604 is relevant for entering
the compensation value.  
c2604 = 1:  
Traveling in the positive direction -> A compensation value is immediately entered.  
Traveling in the negative direction -> A compensation value is not entered  
c2604 = 0:  
Traveling in the positive direction -> A compensation value is not entered  
Traveling in the negative direction -> A compensation value is immediately entered.  
When again setting the home position (a homed axis) or for "passive homing", c2604
is not relevant but instead the history of the axis.  
See also:
c2604

### p2584.0...3 EPOS functions configuration

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Ready for operation |  |  |
| **Parameter group:** Basic positioner |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| - | - | [0] 0100 bin |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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

[S210](#p2585-epos-jog-1-setpoint-velocity-1)

[S210 EPOS load side, rotating](#p2585-epos-jog-1-setpoint-velocity-2)

#### p2585 EPOS jog 1 setpoint velocity

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Jog |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm/s | **Unit group:** 11_3 | **Unit selection:** p2497 |
| **Min:** | **Max:** | **Factory setting:** |
| -40000000.000 [mm/s] | 40000000.000 [mm/s] | [0] -5.000 [mm/s] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the setpoint velocity for jog 1.

**Dependency:** 
  
See also:
p2587, c2589, c2591

#### p2585 EPOS jog 1 setpoint velocity

|  |  |  |
| --- | --- | --- |
| **Variant:**S210 (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Jog |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** °/s | **Unit group:** 11_4 | **Unit selection:** p2497 |
| **Min:** | **Max:** | **Factory setting:** |
| -40000000.000 [°/s] | 40000000.000 [°/s] | [0] -180.000 [°/s] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the setpoint velocity for jog 1.

**Dependency:** 
  
See also:
p2587, c2589, c2591

### p2586 EPOS jog 2 setpoint velocity

[S210](#p2586-epos-jog-2-setpoint-velocity-1)

[S210 EPOS load side, rotating](#p2586-epos-jog-2-setpoint-velocity-2)

#### p2586 EPOS jog 2 setpoint velocity

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Jog |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm/s | **Unit group:** 11_3 | **Unit selection:** p2497 |
| **Min:** | **Max:** | **Factory setting:** |
| -40000000.000 [mm/s] | 40000000.000 [mm/s] | [0] 5.000 [mm/s] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the setpoint velocity for jog 2.

**Dependency:** 
  
See also:
p2588, c2590, c2591

#### p2586 EPOS jog 2 setpoint velocity

|  |  |  |
| --- | --- | --- |
| **Variant:**S210 (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Jog |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** °/s | **Unit group:** 11_4 | **Unit selection:** p2497 |
| **Min:** | **Max:** | **Factory setting:** |
| -40000000.000 [°/s] | 40000000.000 [°/s] | [0] 180.000 [°/s] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the setpoint velocity for jog 2.

**Dependency:** 
  
See also:
p2588, c2590, c2591

### p2587 EPOS jog 1 traversing distance

[S210](#p2587-epos-jog-1-traversing-distance-1)

[S210 EPOS load side, rotating](#p2587-epos-jog-1-traversing-distance-2)

#### p2587 EPOS jog 1 traversing distance

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Jog |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.0000 [mm] | 2147482752.0000 [mm] | [0] 1.0000 [mm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Variant:**S210 (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Jog |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.0000 [°] | 2147482752.0000 [°] | [0] 36.0000 [°] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the traversing distance for incremental jog 1.

**Dependency:** 
  
See also:
p2585, c2589, c2591

**Note:** 
  
Incremental jog 1 is started with c2591 = 1 signal and c2589 = 0/1 signal.  
With c2589 = 0 signal, incremental jogging is interrupted.

### p2588 EPOS jog 2 traversing distance

[S210](#p2588-epos-jog-2-traversing-distance-1)

[S210 EPOS load side, rotating](#p2588-epos-jog-2-traversing-distance-2)

#### p2588 EPOS jog 2 traversing distance

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Jog |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.0000 [mm] | 2147482752.0000 [mm] | [0] 1.0000 [mm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Variant:**S210 (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Jog |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.0000 [°] | 2147482752.0000 [°] | [0] 36.0000 [°] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Signal for incremental jogging.

**Dependency:** 
  
See also:
p2585, p2586, p2587, p2588, c2589, c2590

### c2595 EPOS homing start

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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

[S210](#c259803-epos-home-position-signal-1)

[S210 EPOS load side, rotating](#c259803-epos-home-position-signal-2)

#### c2598[0...3] EPOS home position signal

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
Encoder 2  
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
| **Variant:**S210 (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
Encoder 2  
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

[S210](#p2599-epos-home-position-value-1)

[S210 EPOS load side, rotating](#p2599-epos-home-position-value-2)

#### p2599 EPOS home position value

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Homing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Min:** | **Max:** | **Factory setting:** |
| -2147482752.0000 [mm] | 2147482752.0000 [mm] | [0] 0.0000 [mm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the position value for the home position.  
This value is set as the actual axis position after homing or adjustment.

**Dependency:** 
  
See also:
p2507, c2595, c2596, c2597, c2598

#### p2599 EPOS home position value

|  |  |  |
| --- | --- | --- |
| **Variant:**S210 (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Homing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Min:** | **Max:** | **Factory setting:** |
| -2147482752.0000 [°] | 2147482752.0000 [°] | [0] 0.0000 [°] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the position value for the home position.  
This value is set as the actual axis position after homing or adjustment.

**Dependency:** 
  
See also:
p2507, c2595, c2596, c2597, c2598

### p2600 EPOS active homing home position offset

[S210](#p2600-epos-active-homing-home-position-offset-1)

[S210 EPOS load side, rotating](#p2600-epos-active-homing-home-position-offset-2)

#### p2600 EPOS active homing home position offset

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Homing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| -2147482752.0000 [mm] | 2147482752.0000 [mm] | [0] 0.0000 [mm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the home position shift for active homing.

**Dependency:** 
  
See also:
c2598

#### p2600 EPOS active homing home position offset

|  |  |  |
| --- | --- | --- |
| **Variant:**S210 (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Homing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| -2147482752.0000 [°] | 2147482752.0000 [°] | [0] 0.0000 [°] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the home position shift for active homing.

**Dependency:** 
  
See also:
c2598

### c2604 EPOS active homing start direction

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Signal for the start direction for active homing.  
1 signal: Start in the negative direction.  
0 signal: Start in the positive direction.

**Dependency:** 
  
See also:
p2583, c2595, c2597

### p2605 EPOS active homing approach velocity reference cam

[S210](#p2605-epos-active-homing-approach-velocity-reference-cam-1)

[S210 EPOS load side, rotating](#p2605-epos-active-homing-approach-velocity-reference-cam-2)

#### p2605 EPOS active homing approach velocity reference cam

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Homing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm/s | **Unit group:** 11_3 | **Unit selection:** p2497 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.010 [mm/s] | 40000000.000 [mm/s] | [0] 100.000 [mm/s] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Variant:**S210 (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Homing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** °/s | **Unit group:** 11_4 | **Unit selection:** p2497 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.010 [°/s] | 40000000.000 [°/s] | [0] 3600.000 [°/s] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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

### p2606 EPOS active homing reference cam maximum distance

[S210](#p2606-epos-active-homing-reference-cam-maximum-distance-1)

[S210 EPOS load side, rotating](#p2606-epos-active-homing-reference-cam-maximum-distance-2)

#### p2606 EPOS active homing reference cam maximum distance

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Homing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.0000 [mm] | 2147482752.0000 [mm] | [0] 2147482752.0000 [mm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Variant:**S210 (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Homing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.0000 [°] | 2147482752.0000 [°] | [0] 2147482752.0000 [°] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Homing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 1 | [0] 1 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets whether or not a reference cam is available for active homing.  
Value = 1: Reference cam present.  
Value = 0: No reference cam present.

**Dependency:** 
  
See also:
c2595, c2597, c2604, p2605, p2606

### p2608 EPOS active homing approach velocity zero mark

[S210](#p2608-epos-active-homing-approach-velocity-zero-mark-1)

[S210 EPOS load side, rotating](#p2608-epos-active-homing-approach-velocity-zero-mark-2)

#### p2608 EPOS active homing approach velocity zero mark

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Homing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm/s | **Unit group:** 11_3 | **Unit selection:** p2497 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.010 [mm/s] | 40000000.000 [mm/s] | [0] 25.000 [mm/s] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Variant:**S210 (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Homing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** °/s | **Unit group:** 11_4 | **Unit selection:** p2497 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.010 [°/s] | 40000000.000 [°/s] | [0] 900.000 [°/s] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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

[S210](#p2609-epos-active-homing-max-distance-reference-cam-and-zero-mark-1)

[S210 EPOS load side, rotating](#p2609-epos-active-homing-max-distance-reference-cam-and-zero-mark-2)

#### p2609 EPOS active homing max distance reference cam and zero mark

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Homing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.0000 [mm] | 2147482752.0000 [mm] | [0] 20.0000 [mm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the maximum distance after leaving the reference cam when traversing to the zero
mark.

**Dependency:** 
  
See also:
c2595, c2597, c2604, p2607, p2608

#### p2609 EPOS active homing max distance reference cam and zero mark

|  |  |  |
| --- | --- | --- |
| **Variant:**S210 (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Homing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.0000 [°] | 2147482752.0000 [°] | [0] 720.0000 [°] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the maximum distance after leaving the reference cam when traversing to the zero
mark.

**Dependency:** 
  
See also:
c2595, c2597, c2604, p2607, p2608

### p2611 EPOS active homing approach velocity home position

[S210](#p2611-epos-active-homing-approach-velocity-home-position-1)

[S210 EPOS load side, rotating](#p2611-epos-active-homing-approach-velocity-home-position-2)

#### p2611 EPOS active homing approach velocity home position

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Homing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm/s | **Unit group:** 11_3 | **Unit selection:** p2497 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.010 [mm/s] | 40000000.000 [mm/s] | [0] 25.000 [mm/s] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Variant:**S210 (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Homing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** °/s | **Unit group:** 11_4 | **Unit selection:** p2497 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.010 [°/s] | 40000000.000 [°/s] | [0] 900.000 [°/s] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Commissioning |  |  |
| **Parameter group:** Traversing blocks |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 1 | 64 | [0] 64 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the maximum number of traversing blocks that are available.

**Dependency:** 
  
See also:
p2616, p2617, p2618, p2619, p2620, p2621, p2622, p2623

### p2616[0...n] EPOS traversing block block number

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Traversing blocks |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:**  n defined by: p2615 |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| -1 | 63 | [0] -1 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets a block number.  
-1: Invalid block number. These blocks are not taken into account.  
0 ... 63: valid block number.

**Dependency:** 
  
The number of indices depends on p2615.  
See also:
p2615, p2617, p2618, p2619, p2620, p2621, p2622, p2623

### p2617[0...n] EPOS traversing block position

[S210](#p26170n-epos-traversing-block-position-1)

[S210 EPOS load side, rotating](#p26170n-epos-traversing-block-position-2)

#### p2617[0...n] EPOS traversing block position

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Traversing blocks |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:**  n defined by: p2615 |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| -2147482752.0000 [mm] | 2147482752.0000 [mm] | [0] 0.0000 [mm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Variant:**S210 (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Traversing blocks |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:**  n defined by: p2615 |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| -2147482752.0000 [°] | 2147482752.0000 [°] | [0] 0.0000 [°] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the target position for the traversing block.

**Dependency:** 
  
The number of indices depends on p2615.  
See also:
p2615, p2616, p2618, p2619, p2620, p2621, p2622, p2623

**Note:** 
  
The target position is approached in either relative or absolute terms depending on
p2623.

## SINAMICS Parameter S210 02617 - 09502

SINAMICS Parameter S210 02617 - 09502

### p2618[0...n] EPOS traversing block velocity

[S210](#p26180n-epos-traversing-block-velocity-1)

[S210 EPOS load side, rotating](#p26180n-epos-traversing-block-velocity-2)

#### p2618[0...n] EPOS traversing block velocity

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Traversing blocks |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:**  n defined by: p2615 |  | **Calculated:** - |
| **Unit:** mm/s | **Unit group:** 11_3 | **Unit selection:** p2497 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.010 [mm/s] | 40000000.000 [mm/s] | [0] 100.000 [mm/s] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Variant:**S210 (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Traversing blocks |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:**  n defined by: p2615 |  | **Calculated:** - |
| **Unit:** °/s | **Unit group:** 11_4 | **Unit selection:** p2497 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.010 [°/s] | 40000000.000 [°/s] | [0] 3600.000 [°/s] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Traversing blocks |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:**  n defined by: p2615 |  | **Calculated:** - |
| **Unit:** % | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 1.0 [%] | 100.0 [%] | [0] 100.0 [%] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Traversing blocks |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:**  n defined by: p2615 |  | **Calculated:** - |
| **Unit:** % | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 1.0 [%] | 100.0 [%] | [0] 100.0 [%] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Traversing blocks |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:**  n defined by: p2615 |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 1 | 9 | [0] 1 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Traversing blocks |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:**  n defined by: p2615 |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| -2147483648 | 2147483647 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Traversing blocks |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:**  n defined by: p2615 |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 65535 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the influence of the task for the traversing block.  
Value = 0000 cccc bbbb aaaa  
cccc: Positioning mode  
cccc = 0000 --> ABSOLUTE  
cccc = 0001 --> RELATIVE  
cccc = 0010 --> ABS_POS (only for a rotary axis with modulo correction)  
cccc = 0011 --> ABS_NEG (only for a rotary axis with modulo correction)  
bbbb: Progression condition  
bbbb = 0000 --> END  
bbbb = 0001 --> CONTINUE_WITH_STOP  
bbbb = 0010 --> CONTINUE_FLYING  
bbbb = 0011 --> CONTINUE_EXTERNAL  
bbbb = 0100 --> CONTINUE_EXTERNAL_WAIT  
bbbb = 0101 --> CONTINUE_EXTERNAL_ALARM  
aaaa: IDs  
aaaa = 000x --> show/hide block (x = 0: show, x = 1: hide)

**Dependency:** 
  
The number of indices depends on p2615.  
See also:
p2615, p2616, p2617, p2618, p2619, p2620, p2621, p2622

### c2625 EPOS traversing block selection bit 0

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Data type:**Unsigned8 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Data type:**Unsigned8 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Ready for operation |  |  |
| **Parameter group:** Traversing blocks |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 1 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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

[S210](#p26340-epos-fixed-stop-maximum-following-error-1)

[S210 EPOS load side, rotating](#p26340-epos-fixed-stop-maximum-following-error-2)

#### p2634[0] EPOS fixed stop maximum following error

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Traversing blocks |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.0000 [mm] | 2147482752.0000 [mm] | [0] 1.0000 [mm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Variant:**S210 (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Traversing blocks |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.0000 [°] | 2147482752.0000 [°] | [0] 36.0000 [°] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the following error to detect the "fixed stop reached" state (r2526.4).

**Dependency:** 
  
See also:
r2526, p2621, r2675

**Note:** 
  
The state "fixed stop reached" is detected if the following error exceeds the theoretically
calculated following error value by p2634.

### p2635 EPOS fixed stop monitoring window

[S210](#p2635-epos-fixed-stop-monitoring-window-1)

[S210 EPOS load side, rotating](#p2635-epos-fixed-stop-monitoring-window-2)

#### p2635 EPOS fixed stop monitoring window

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Traversing blocks |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.0000 [mm] | 2147482752.0000 [mm] | [0] 0.1250 [mm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Variant:**S210 (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Traversing blocks |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.0000 [°] | 2147482752.0000 [°] | [0] 3.6000 [°] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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

[S210](#c2642-epos-direct-setpoint-inputmdi-position-setpoint-1)

[S210 EPOS load side, rotating](#c2642-epos-direct-setpoint-inputmdi-position-setpoint-2)

#### c2642 EPOS direct setpoint input/MDI position setpoint

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Variant:**S210 (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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

[S210](#c2643-epos-direct-setpoint-inputmdi-velocity-setpoint-1)

[S210 EPOS load side, rotating](#c2643-epos-direct-setpoint-inputmdi-velocity-setpoint-2)

#### c2643 EPOS direct setpoint input/MDI velocity setpoint

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Variant:**S210 (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Signal of the MDI mode via PROFIBUS telegram 110 in operating mode "direct setpoint
input/MDI".  
c2654 = 0: Signals are evaluated.  
c2654 > 0: Signals are not evaluated.  
The evaluation involves the following signals:  
- c2648 (positioning type)  
- c2651 (positive direction selection)  
- c2652 (negative direction selection)  
In this case, the following definitions apply:  
Signal via c2654 = xx0x hex -> absolute  
Signal via c2654 = xx1x hex -> relative  
Signal via c2654 = xx2x hex -> abs_pos (only for modulo correction)  
Signal via c2654 = xx3x hex -> abs_neg (only for modulo correction)

**Dependency:** 
  
See also:
c2648, c2651, c2652

### c2655[0...1] EPOS select tracking mode

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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

[S210](#r2665-epos-position-setpoint-1)

[S210 EPOS load side, rotating](#r2665-epos-position-setpoint-2)

#### r2665 EPOS position setpoint

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Jog, Homing, Traversing blocks, Direct setpoint input (MDI) |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Variant:**S210 (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Jog, Homing, Traversing blocks, Direct setpoint input (MDI) |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Displays the actual absolute position setpoint.

**Dependency:** 
  
See also:
c2530

**Note:** 
  
As default, c2530 is interconnected with r2665.

### r2666 EPOS velocity setpoint

[S210](#r2666-epos-velocity-setpoint-1)

[S210 EPOS load side, rotating](#r2666-epos-velocity-setpoint-2)

#### r2666 EPOS velocity setpoint

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Jog, Homing, Traversing blocks, Direct setpoint input (MDI) |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm/s | **Unit group:** 11_3 | **Unit selection:** p2497 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Variant:**S210 (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Jog, Homing, Traversing blocks, Direct setpoint input (MDI) |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** °/s | **Unit group:** 11_4 | **Unit selection:** p2497 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Jog, Homing, Traversing blocks, Direct setpoint input (MDI) |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source binary/numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Traversing blocks |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source binary/numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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

[S210](#r2671-epos-actual-position-setpoint-1)

[S210 EPOS load side, rotating](#r2671-epos-actual-position-setpoint-2)

#### r2671 EPOS actual position setpoint

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Jog, Traversing blocks, Direct setpoint input (MDI) |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Displays the position setpoint presently being processed.

**Note:** 
  
A position of 0 is displayed for non position-related tasks (e.g. ENDLESS_POS, ENDLESS_NEG).

#### r2671 EPOS actual position setpoint

|  |  |  |
| --- | --- | --- |
| **Variant:**S210 (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Jog, Traversing blocks, Direct setpoint input (MDI) |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Displays the position setpoint presently being processed.

**Note:** 
  
A position of 0 is displayed for non position-related tasks (e.g. ENDLESS_POS, ENDLESS_NEG).

### r2672 EPOS actual velocity setpoint

[S210](#r2672-epos-actual-velocity-setpoint-1)

[S210 EPOS load side, rotating](#r2672-epos-actual-velocity-setpoint-2)

#### r2672 EPOS actual velocity setpoint

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Jog, Homing, Traversing blocks, Direct setpoint input (MDI) |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm/s | **Unit group:** 11_3 | **Unit selection:** p2497 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Displays the velocity setpoint presently being processed.

#### r2672 EPOS actual velocity setpoint

|  |  |  |
| --- | --- | --- |
| **Variant:**S210 (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Jog, Homing, Traversing blocks, Direct setpoint input (MDI) |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** °/s | **Unit group:** 11_4 | **Unit selection:** p2497 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Displays the velocity setpoint presently being processed.

### r2673 EPOS actual acceleration override

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Jog, Traversing blocks, Direct setpoint input (MDI) |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** % | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Displays the acceleration override presently being processed.

**Note:** 
  
An override of 100% is effective in the "Jogging" and "Active homing" operating modes.

### r2674 EPOS actual deceleration override

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Jog, Traversing blocks, Direct setpoint input (MDI) |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** % | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Displays the deceleration override presently being processed.

**Note:** 
  
An override of 100% is effective in the "Jogging" and "Active homing" operating modes.

### r2675 EPOS actual task

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Traversing blocks |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Traversing blocks |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
SET_O: 1, 2, 3 --> direct output 1, 2 or 3 (both) is set  
RESET_O: 1, 2, 3 --> direct output 1, 2 or 3 (both) is reset  
JERK: 0 --> deactivate, 1 --> activate

### r2677 EPOS actual task mode

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Traversing blocks |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Displays the task mode presently being processed.

**Dependency:** 
  
See also:
p2623

### r2678 EPOS external block change actual position

[S210](#r2678-epos-external-block-change-actual-position-1)

[S210 EPOS load side, rotating](#r2678-epos-external-block-change-actual-position-2)

#### r2678 EPOS external block change actual position

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Traversing blocks, Direct setpoint input (MDI) |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Variant:**S210 (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Traversing blocks, Direct setpoint input (MDI) |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Displays the actual position for the following events:  
- External block change via measuring probe (p2632 = 0, c2661 = 0/1 signal).  
- External block change via c2633 (p2632 = 1, c2633 = 0/1 signal).  
- Activate traversing task (c2631 = 0/1 signal).

**Dependency:** 
  
See also:
c2631, p2632, c2633

### r2680 EPOS clearance reference cam and zero mark

[S210](#r2680-epos-clearance-reference-cam-and-zero-mark-1)

[S210 EPOS load side, rotating](#r2680-epos-clearance-reference-cam-and-zero-mark-2)

#### r2680 EPOS clearance reference cam and zero mark

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Homing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Display for the distance (clearance) between the reference cam and zero mark.  
The value is determined for active homing.

#### r2680 EPOS clearance reference cam and zero mark

|  |  |  |
| --- | --- | --- |
| **Variant:**S210 (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Homing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Display for the distance (clearance) between the reference cam and zero mark.  
The value is determined for active homing.

### r2681 EPOS velocity override effective

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Jog, Homing, Traversing blocks, Direct setpoint input (MDI) |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** % | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Displays the actual effective velocity override.

**Dependency:** 
  
See also:
p2571, c2646

**Note:** 
  
The effective override can differ from the specified override due to limits (e.g.
p2571, maximum velocity).

### r2682 EPOS residual distance to go

[S210](#r2682-epos-residual-distance-to-go-1)

[S210 EPOS load side, rotating](#r2682-epos-residual-distance-to-go-2)

#### r2682 EPOS residual distance to go

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Jog, Traversing blocks, Direct setpoint input (MDI) |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Variant:**S210 (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Jog, Traversing blocks, Direct setpoint input (MDI) |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Control/status words, Jog, Homing, Traversing blocks, Direct setpoint input (MDI), Position controller monitoring |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source binary/numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| 08 | Position actual value <= cam switching position 1 | No | Yes | 4025 |
| 09 | Position actual value <= cam switching position 2 | No | Yes | 4025 |
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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Control/status words, Limit, Jog, Homing, Traversing blocks, Direct setpoint input (MDI), Mechanics, Position controller monitoring |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source binary/numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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

[S210](#r2685-epos-corrective-value-1)

[S210 EPOS load side, rotating](#r2685-epos-corrective-value-2)

#### r2685 EPOS corrective value

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Basic positioner |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Variant:**S210 (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Basic positioner |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Basic positioner |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** % | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Traversing blocks |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Nm | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Displays the active torque setpoint when reaching the fixed stop.

**Dependency:** 
  
See also:
p1520, p1521, r2676

### p2688 EPOS position feedback signal tolerance window

[S210](#p2688-epos-position-feedback-signal-tolerance-window-1)

[S210 EPOS load side, rotating](#p2688-epos-position-feedback-signal-tolerance-window-2)

#### p2688 EPOS position feedback signal tolerance window

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Basic positioner |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** 10_3 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.0000 [mm] | 2147482750.0000 [mm] | [0] 0.0500 [mm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Variant:**S210 (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Basic positioner |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** 10_4 | **Unit selection:** p2496 |
| **Min:** | **Max:** | **Factory setting:** |
| 0.0000 [°] | 2147482750.0000 [°] | [0] 1.5000 [°] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Basic positioner |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Position controller |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** rev/s² | **Unit group:** 39_1 | **Unit selection:** p0505 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2007 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Displays the acceleration precontrol value.

**Note:** 
  
The acceleration precontrol value is a derivation of the speed precontrol value with
respect to time.

### p3117 Change safety message type

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Safety Integrated, Faults / alarms |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 1 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the re-parameterization of all safety messages for faults and alarms.  
The relevant message type during changeover is selected by the firmware.  
0: Safety messages are not reparameterized (safety message buffer)  
1: Safety messages are reparameterized (no safety message buffer)

**Note:** 
  
When online safety commissioning has been completed, a change results in an automatic
restart.

### r3122[0...63].0...20 Diagnostic attribute fault

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Faults / alarms |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
Bits 20, 19, 18, 17, 16 = 0, 0, 0, 0, 0 --> PROFIdrive message class 0: not assigned  
Bits 20, 19, 18, 17, 16 = 0, 0, 0, 0, 1 --> PROFIdrive message class 1: hardware fault/software
error  
Bits 20, 19, 18, 17, 16 = 0, 0, 0, 1, 0 --> PROFIdrive message class 2: line fault  
Bits 20, 19, 18, 17, 16 = 0, 0, 0, 1, 1 --> PROFIdrive message class 3: supply voltage
fault  
Bits 20, 19, 18, 17, 16 = 0, 0, 1, 0, 0 --> PROFIdrive message class 4: DC link fault  
Bits 20, 19, 18, 17, 16 = 0, 0, 1, 0, 1 --> PROFIdrive message class 5: power electronics
faulted  
Bits 20, 19, 18, 17, 16 = 0, 0, 1, 1, 0 --> PROFIdrive message class 6: overtemperature
electronic components  
Bits 20, 19, 18, 17, 16 = 0, 0, 1, 1, 1 --> PROFIdrive message class 7: ground fault/phase
fault detected  
Bits 20, 19, 18, 17, 16 = 0, 1, 0, 0, 0 --> PROFIdrive message class 8: motor overload  
Bits 20, 19, 18, 17, 16 = 0, 1, 0, 0, 1 --> PROFIdrive message class 9: communication
error to the higher-level control  
Bits 20, 19, 18, 17, 16 = 0, 1, 0, 1, 0 --> PROFIdrive message class 10: safe monitoring
channel has identified an error  
Bits 20, 19, 18, 17, 16 = 0, 1, 0, 1, 1 --> PROFIdrive message class 11: incorrect
position actual value/speed actual value or not available  
Bits 20, 19, 18, 17, 16 = 0, 1, 1, 0, 0 --> PROFIdrive message class 12: internal
(DRIVE-CLiQ) communication error  
Bits 20, 19, 18, 17, 16 = 0, 1, 1, 0, 1 --> PROFIdrive message class 13: infeed unit
faulted  
Bits 20, 19, 18, 17, 16 = 0, 1, 1, 1, 0 --> PROFIdrive message class 14: braking controller/Braking
Module faulted  
Bits 20, 19, 18, 17, 16 = 0, 1, 1, 1, 1 --> PROFIdrive message class 15: line filter
faulted  
Bits 20, 19, 18, 17, 16 = 1, 0, 0, 0, 0 --> PROFIdrive message class 16: external
measured value/signal state outside the permissible range  
Bits 20, 19, 18, 17, 16 = 1, 0, 0, 0, 1 --> PROFIdrive message class 17: application/technology
function faulted  
Bits 20, 19, 18, 17, 16 = 1, 0, 0, 1, 0 --> PROFIdrive message class 18: error in
the parameterization/configuration/commissioning sequence  
Bits 20, 19, 18, 17, 16 = 1, 0, 0, 1, 1 --> PROFIdrive message class 19: general drive
fault  
Bits 20, 19, 18, 17, 16 = 0, 1, 1, 0, 0 --> PROFIdrive message class 20: auxiliary
unit faulted

### r3123[0...63].0...20 Diagnostic attribute alarm

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Faults / alarms |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
Bits 20, 19, 18, 17, 16 = 0, 0, 0, 0, 0 --> PROFIdrive message class 0: not assigned  
Bits 20, 19, 18, 17, 16 = 0, 0, 0, 0, 1 --> PROFIdrive message class 1: hardware fault/software
error  
Bits 20, 19, 18, 17, 16 = 0, 0, 0, 1, 0 --> PROFIdrive message class 2: line fault  
Bits 20, 19, 18, 17, 16 = 0, 0, 0, 1, 1 --> PROFIdrive message class 3: supply voltage
fault  
Bits 20, 19, 18, 17, 16 = 0, 0, 1, 0, 0 --> PROFIdrive message class 4: DC link fault  
Bits 20, 19, 18, 17, 16 = 0, 0, 1, 0, 1 --> PROFIdrive message class 5: power electronics
faulted  
Bits 20, 19, 18, 17, 16 = 0, 0, 1, 1, 0 --> PROFIdrive message class 6: overtemperature
electronic components  
Bits 20, 19, 18, 17, 16 = 0, 0, 1, 1, 1 --> PROFIdrive message class 7: ground fault/phase
fault detected  
Bits 20, 19, 18, 17, 16 = 0, 1, 0, 0, 0 --> PROFIdrive message class 8: motor overload  
Bits 20, 19, 18, 17, 16 = 0, 1, 0, 0, 1 --> PROFIdrive message class 9: communication
error to the higher-level control  
Bits 20, 19, 18, 17, 16 = 0, 1, 0, 1, 0 --> PROFIdrive message class 10: safe monitoring
channel has identified an error  
Bits 20, 19, 18, 17, 16 = 0, 1, 0, 1, 1 --> PROFIdrive message class 11: incorrect
position actual value/speed actual value or not available  
Bits 20, 19, 18, 17, 16 = 0, 1, 1, 0, 0 --> PROFIdrive message class 12: internal
(DRIVE-CLiQ) communication error  
Bits 20, 19, 18, 17, 16 = 0, 1, 1, 0, 1 --> PROFIdrive message class 13: infeed unit
faulted  
Bits 20, 19, 18, 17, 16 = 0, 1, 1, 1, 0 --> PROFIdrive message class 14: braking controller/Braking
Module faulted  
Bits 20, 19, 18, 17, 16 = 0, 1, 1, 1, 1 --> PROFIdrive message class 15: line filter
faulted  
Bits 20, 19, 18, 17, 16 = 1, 0, 0, 0, 0 --> PROFIdrive message class 16: external
measured value/signal state outside the permissible range  
Bits 20, 19, 18, 17, 16 = 1, 0, 0, 0, 1 --> PROFIdrive message class 17: application/technology
function faulted  
Bits 20, 19, 18, 17, 16 = 1, 0, 0, 1, 0 --> PROFIdrive message class 18: error in
the parameterization/configuration/commissioning sequence  
Bits 20, 19, 18, 17, 16 = 1, 0, 0, 1, 1 --> PROFIdrive message class 19: general drive
fault  
Bits 20, 19, 18, 17, 16 = 0, 1, 1, 0, 0 --> PROFIdrive message class 20: auxiliary
unit faulted

### p3941[0] Motor code number 2

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Commissioning |  |  |
| **Parameter group:** Motor data, Quick commissioning |  |  |
| **Not relevant for motor type:**Separately excited synchronous motor, Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 99999999 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Second motor code number.

**Dependency:** 
  
See also:
p0301

### r3988 Final boot state

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** System identification |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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

### p5271[0].3...7 One Button Tuning configuration 1

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Ready for operation |  |  |
| **Parameter group:** |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| - | - | [0] 0001 1100 bin |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the configuration for One Button Tuning.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 03 | Setting the speed precontrol | No | Yes | 5045 |
| 04 | Setting the torque precontrol | No | Yes | 5045 |
| 07 | Setting the voltage precontrol | No | Yes | - |

**Dependency:** 
  
See also:
r5274

**Note:** 
  
For bit 03:  
Activation of speed precontrol.  
For bit 04:  
Activation of speed/torque precontrol in the drive.  
For bit 07:  
Activation of the voltage precontrol.

### r5274 One Button Tuning dynamic response estimated

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the estimated dynamic response of the speed control loop as PT1 time constant
for One Button Tuning.  
The lower the time constant, the higher the dynamic performance.

**Dependency:** 
  
See also:
p5271

### r5276[0] One Button Tuning Kv factor estimated

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** 1000 rpm | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the estimated position controller gain (Kv factor) for One Button Tuning.

**Dependency:** 
  
See also:
p5271

**Note:** 
  
The value for the closed-loop position control is required by a higher-level control
system.

### r5277[0] One Button Tuning precontrol symmetrizing time estimated

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the estimated precontrol symmetrizing time for One Button Tuning.  
This is required to symmetrize the position controller if the closed-loop position
control is in an external control system.

**Dependency:** 
  
See also:
p5271

### p5291.0...16 FFT tuning configuration

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| - | - | [0] 0000 0000 0000 0000 0000 0000 0011 1001 bin |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
Bit 04 = 0 and bit 03 = 0 -> buffer length = 256  
Bit 04 = 0 and bit 03 = 1 -> buffer length = 512  
Bit 04 = 1 and bit 03 = 0 -> buffer length = 1024  
Bit 04 = 1 and bit 03 = 1 -> buffer length = 2048  
For bit 05:  
A Hamming window is used to filter the measured time signals.  
For bit 06:  
The measurement checks the current controller frequency response and this is taken
into account in the speed controller loop.  
For bits 07, 08, 09:  
The measurement bandwidth is set using these bits:  
Bit 09 = 0, bit 08 = 0, bit 07 = 0 -> bandwidth = 50 Hz  
Bit 09 = 0, bit 08 = 0, bit 07 = 1 -> bandwidth = 100 Hz  
Bit 09 = 0, bit 08 = 1, bit 07 = 0 -> bandwidth = 200 Hz  
Bit 09 = 0, bit 08 = 1, bit 07 = 1 -> bandwidth = 400 Hz  
Bit 09 = 1, bit 08 = 0, bit 07 = 0 -> bandwidth = 800 Hz  
Bit 09 = 1, bit 08 = 0, bit 07 = 1 -> bandwidth = 1600 Hz  
For bits 10, 11:  
Number of measuring periods.  
Bit 11 = 0 and bit 10 = 0 -> number of measurements = 1  
Bit 11 = 0 and bit 10 = 1 -> number of measurements = 2  
Bit 11 = 1 and bit 10 = 0 -> number of measurements = 4  
Bit 11 = 1 and bit 10 = 1 -> number of measurements = 8  
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
(e.g. > 6x).  
- The coupling between the machine elements has almost no backlash (no play).  
- The stiffness of the mechanical transmission elements does not change significantly
in the traversing range.

### p5292 Controller optimization dynamic factor

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** % | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 25.0 [%] | 125.0 [%] | [0] 80.0 [%] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the dynamic factor for optimizing the speed controller when One Button Tuning
is activated (p5300 = 1).

**Dependency:** 
  
The higher the value in p5292, the lower the value in r5274.  
See also:
p5291

**Note:** 
  
The higher the dynamic factor, the faster and more unstable the control.

### r5293 FFT tuning speed controller P gain identified

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Nms/rad | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** % | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 1.0 [%] | 300.0 [%] | [0] 10.0 [%] [1] 30.0 [%] [2] 5.0 [%] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
The drive determines the noise amplitude for One Button Tuning and writes the value
to p5296.

**Dependency:** 
  
See also:
p5291

### p5300[0] One Button Tuning selection

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Ready for operation |  |  |
| **Parameter group:** |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| -1 | 1 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Setting to activate/deactivate the One Button Tuning function.  
For p5300 = 1:  
The One Button Tuning function is configured using p5271 and p5301.

**Value:** 
  
-1:
Reset controller parameters  
0:
Inactive  
1:
One Button Tuning

**Dependency:** 
  
The motor must have already been commissioned so that One Button Tuning functions
perfectly.  
The One Button Tuning function is configured using p5271 and p5301.  
The required dynamic performance of the control loop is set in p5292.  
The traversing path for the test signal is parameterized in p5308.  
See also:
p5271, r5274, p5292, r5293, p5296, p5301, p5308, p5309

**Note:** 
  
For p5300 = -1:  
One Button Tuning is deactivated and p5300 is automatically set = 0. Further, the
presetting values for the speed controller are restored.  
For p5300 = 0:  
To permanently save the values for the speed controller that have been determined,
the parameters must be saved in a non-volatile memory.  
For p5300 = 1:  
One Button Tuning is active.  
The moment of inertia is determined once using a test signal. The controller parameters
and current setpoint filters are additionally determined once using a noise signal
as excitation source. The steps to be executed can be configured using p5301.

### p5301[0].0...8 One Button Tuning configuration 2

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| - | - | [0] 0000 0000 0000 0111 bin |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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

### r5306[0].0...14 One Button Tuning status

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** |  |  |
| **Not relevant for motor type:**Synchronous or reluctance motor with starting cage |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the status of the functions performed using One Button Tuning.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Proportional gain Kp set | No | Yes | - |
| 01 | Current setpoint filter set | No | Yes | - |
| 02 | Moment of inertia estimation carried out | No | Yes | - |
| 13 | One Button Tuning successfully completed | No | Yes | - |
| 14 | Controller parameters reset due to fault | No | Yes | - |

**Dependency:** 
  
See also:
p5300, p5301

**Note:** 
  
For bit 00 = 1: The speed controller gain was set using One Button Tuning.  
For bit 01 = 1: The current setpoint filter was set using One Button Tuning  
For bit 02 = 1: The moment of inertia was determined.

### p5308[0] One Button Tuning distance limiting

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Ready for operation |  |  |
| **Parameter group:** |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| -30000 [°] | 30000 [°] | [0] 0 [°] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Setting the distance limiting (permissible traversing range of the motor).  
The traversing range is limited in the positive and negative directions.

**Note:** 
  
A value of 360 degrees corresponds to one motor revolution.  
The position before the pulse enable is used as zero point.

### p5309[0] One Button Tuning duration

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Ready for operation |  |  |
| **Parameter group:** |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 [ms] | 5000 [ms] | [0] 2000 [ms] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the duration for One Button Tuning (several acceleration operations)  
This function is used for One Button Tuning (p5300 = 1) to identify the total moment
of inertia of the drive train.

**Dependency:** 
  
See also:
F07093

**Note:** 
  
If, within this time, no setting values can be determined, then the drive is shut
down with the corresponding fault.

### p5375[0].0...1 Additional motor overload protection configuration

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Motor temperature |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| - | - | [0] 0000 bin |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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

### r5600 PROFIenergy energy-saving mode ID

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the PROFIenergy mode ID of the effective energy-saving mode.

**Value:** 
  
0:
POWER OFF  
2:
Energy-saving mode  
240:
Operation  
255:
Ready

### p5611.0...2 PROFIenergy energy-saving properties general

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Ready for operation |  |  |
| **Parameter group:** |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| - | - | [0] 0000 bin |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the general properties for energy-saving.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Inhibit PROFIenergy control commands | No | Yes | - |
| 01 | Drive initiates OFF1 when transitioning to energy-saving mode | No | Yes | - |
| 02 | Trans to energy-saving mode from PROFIdrive state S3/4 poss | No | Yes | - |

**Note:** 
  
PROFIenergy is a profile for energy management in production systems.  
PROFIdrive state S3: ready  
PROFIdrive state S4: operation

### r5613.0...1 PROFIenergy energy saving active/inactive

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source binary/numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
State displays as to whether PROFIenergy energy saving is active or inactive.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | PROFIenergy active | No | Yes | - |
| 01 | PROFIenergy inactive | No | Yes | - |

**Note:** 
  
Bit 0 and bit 1 are inverse of one another.

### r8400[0...2] Date

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Diagnostics general |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
| **Data type:**Unsigned16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Diagnostics general |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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

### r8936[0...1] PN cyclic connection state

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
11:
Reserved  
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
Controller 2

**Dependency:** 
  
See also:
r8961

**Note:** 
  
The parameter is active when the "PROFINET Device" protocol is selected.  
For two connections (shared device) the display in the index depends on the sequence
in which the connections are established.  
For value = 10:  
If the connection remains in this state, then when using PROFINET IRT the following
can apply:  
- Topology error (incorrect port assignment).  
- Synchronization missing.

### r8937[0...5] PN cyclic connection diagnostics

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
  
For index [5]:  
Bit 0 = 1: there is at least one RT connection.  
Bit 1 = 1: there is an IRT connection.

### r8961[0...3] PN controller IP address

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Configuration |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the IP address of the PROFINET controller.

**Note:** 
  
For a shared device, the IP address of the automation controller is displayed.

### c8995[0...3] Ethernet X127 enable

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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
| **Data type:**Unsigned8 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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

### p9500 SI monitoring clock cycle

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 4.00000 [ms] | 4.00000 [ms] | [0] 4.00000 [ms] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the monitoring clock cycle for safe motion monitoring.

**Dependency:** 
  
See also:
p9511  
See also:
C01652

**Note:** 
  
When online safety commissioning has been completed, a change results in an automatic
restart.  
The monitoring cycle must be a multiple of the actual value sensing clock cycle (p9511).

### r9502 SI axis type

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the axis type (linear axis or rotary axis/spindle).

**Value:** 
  
0:
Linear axis  
1:
Rotary axis/spindle

**Note:** 
  
The axis type is set in the commissioning tool.  
Safety parameters whose units are dependent on the axis type change after switching
over the axis type.

## SINAMICS Parameter S210 09507 - 09770

SINAMICS Parameter S210 09507 - 09770

### p9507.8...9 SI function configuration

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| - | - | [0] 0000 0000 0000 0000 bin |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the function configuration for the safe motion monitoring functions.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 08 | No STO after encoder fault for 1-encoder safety | No | Yes | - |
| 09 | Status bit 'SSM below the limit' initial value when running up | SSM status=1 | SSM status=0 | - |

**Dependency:** 
  
See also:
C01711

**Note:** 
  
For bit 08:  
When the function is activated, after an encoder fault for 1-encoder safety and when
a safety function is selected, an STO is not triggered.  
SCF: Safety Channel Failed  
For bit 09:  
When the function is activated, the SSM status signal is initialized with "0" when
running up.  
When the function is deactivated, when running up the SSM status signal is initialized
with "1".  
SSM: Safety Speed Monitoring

### p9511 SI actual value sensing cycle

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 1.00000 [ms] | 1.00000 [ms] | [0] 1.00000 [ms] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the clock cycle time of the actual value sensing for safe motion monitoring.  
Setting criteria if the motion monitoring functions are executed with an encoder.  
- A slower cycle time reduces the maximum permissible speed; however, it ensures a
lower system utilization level.  
- The maximum permissible velocity, which, when exceeded, can mean that errors occur
in the safe actual value sensing, is displayed in r9730.

**Dependency:** 
  
See also:
C01652

**Note:** 
  
The monitoring clock cycle from p9500 must be an integer multiple of this parameter.  
For motion monitoring functions with encoder, the cycle time of the actual value sensing
must be an integer multiple of the current controller cycle.  
When online safety commissioning has been completed, a change results in an automatic
restart.

### p9516.1 SI encoder configuration, safety functions

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| - | - | [0] 0000 bin |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the configuration for the position actual value.  
The encoder that is used for the safe motion monitoring function must be parameterized
in this parameter.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 01 | Position actual value sign change | No | Yes | - |

**Dependency:** 
  
See also:
p0404  
See also:
C01671

**Note:** 
  
In the standard case, p9516.1 should be set equal to p0410.1.

### p9520 SI leadscrew pitch

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.1000 [mm] | 8388.0000 [mm] | [0] 10.0000 [mm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the gear ratio between SI encoder 1 and load in mm/revolution for a linear axis
with rotary encoder.

**Notice:** 
  
The fourth decimal point can be rounded-off depending on the size of the entered number
(from 3 places before the decimal point).

### p9521[0...7] SI gearbox encoder (motor)/load denominator

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 1 | 2147000000 | [0] 1 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the denominator for the selected gearbox between SI encoder 1 and the load.

**Index:** 
  
[
0]:
Gearbox 1  
[
1...7]:
Reserved

**Dependency:** 
  
See also:
p9522

**Note:** 
  
The gearbox ratio is obtained from p9522 / p9521.

### p9522[0...7] SI gearbox encoder (motor)/load numerator

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 1 | 2147000000 | [0] 1 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the numerator for the selected gearbox between SI encoder 1 and the load.

**Index:** 
  
[
0]:
Gearbox 1  
[
1...7]:
Reserved

**Dependency:** 
  
See also:
p9521

**Note:** 
  
The gearbox ratio is obtained from p9522 / p9521.

### p9530 SI SOS standstill tolerance

[S210](#p9530-si-sos-standstill-tolerance-1)

[S210 Safety rot](#p9530-si-sos-standstill-tolerance-2)

#### p9530 SI SOS standstill tolerance

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.000 [mm] | 100.000 [mm] | [0] 1.000 [mm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the tolerance for the function "Safe Operating Stop" (SOS).

**Dependency:** 
  
See also:
C01707

**Note:** 
  
SOS: Safe Operating Stop

#### p9530 SI SOS standstill tolerance

|  |  |  |
| --- | --- | --- |
| **Variant:**S210 (Safety rot) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.000 [°] | 100.000 [°] | [0] 1.000 [°] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the tolerance for the function "Safe Operating Stop" (SOS).

**Dependency:** 
  
See also:
C01707

**Note:** 
  
SOS: Safe Operating Stop

### p9531[0...3] SI SLS limit values

[S210](#p953103-si-sls-limit-values-1)

[S210 Safety rot](#p953103-si-sls-limit-values-2)

#### p9531[0...3] SI SLS limit values

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm/min | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [mm/min] | 1000000.00 [mm/min] | [0] 2000.00 [mm/min] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the limit values for function SLS (Safely-Limited Speed).

**Index:** 
  
[
0]:
Limit value SLS1  
[
1]:
Limit value SLS2  
[
2]:
Limit value SLS3  
[
3]:
Limit value SLS4

**Dependency:** 
  
See also:
p9563  
See also:
C01714

#### p9531[0...3] SI SLS limit values

|  |  |  |
| --- | --- | --- |
| **Variant:**S210 (Safety rot) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** rpm | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [rpm] | 1000000.00 [rpm] | [0] 2000.00 [rpm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the limit values for function SLS (Safely-Limited Speed).

**Index:** 
  
[
0]:
Limit value SLS1  
[
1]:
Limit value SLS2  
[
2]:
Limit value SLS3  
[
3]:
Limit value SLS4

**Dependency:** 
  
See also:
p9563  
See also:
C01714

### p9533 SI SLS setpoint speed limiting

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** % | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.000 [%] | 100.000 [%] | [0] 80.000 [%] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the evaluation factor to define the setpoint limit from the selected actual velocity
limit.  
The active SLS (Safely-Limited Speed) limit value is evaluated with this factor and
is made available as setpoint limit in r9733.  
A value of 0 signifies that the setpoint speed limiting is not active.

**Dependency:** 
  
r9733[0] = p9531[x] x p9533 (converted from the load side to the encoder side)  
r9733[1] = p9531[x] x p9533 (converted from the load side to the encoder side)  
[x] = selected SLS limit value  
Conversion factor from the encoder side to the load side:  
- Motor type = rotary and axis type = linear: p9522 / (p9521 x p9520)  
- Otherwise: p9522 / p9521  
See also:
p9531

**Note:** 
  
The active actual velocity limit is selected via safety-relevant inputs (SGE).  
When selecting a safety function, where standstill is reached or required (e.g. STO,
SS1), then setpoint 0 is specified in r9733.

### p9539[0...7] SI gearbox rotation reversal

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 1 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the direction of rotation reversal for the gearbox.  
0: No direction of rotation reversal  
1: Direction of rotation reversal

**Value:** 
  
0:
No direction of rotation reversal  
1:
Direction of rotation reversal

**Index:** 
  
[
0]:
Gearbox 1  
[
1...7]:
Reserved

**Dependency:** 
  
See also:
p9521

### p9545 SI SSM filter time

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [ms] | 500.00 [ms] | [0] 0.00 [ms] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the filter time for the SSM feedback signal to detect standstill.

**Note:** 
  
The filter time is only active if the function is enabled (p9604.12 = 1).  
SSM: Safe Speed Monitor (safety-relevant feedback signal from the speed monitoring)

### p9546 SI SSM velocity limit

[S210](#p9546-si-ssm-velocity-limit-1)

[S210 Safety rot](#p9546-si-ssm-velocity-limit-2)

#### p9546 SI SSM velocity limit

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm/min | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.002 [mm/min] | 1000000.000 [mm/min] | [0] 60.000 [mm/min] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the velocity limit for the SSM feedback signal to detect standstill.  
When this limit value is undershot (take into account the parameterized hysteresis),
signal "SSM feedback signal active" is set.

**Note:** 
  
SSM: Safe Speed Monitor (safety-relevant feedback signal from the speed monitoring)

#### p9546 SI SSM velocity limit

|  |  |  |
| --- | --- | --- |
| **Variant:**S210 (Safety rot) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** rpm | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.002 [rpm] | 1000000.000 [rpm] | [0] 60.000 [rpm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the velocity limit for the SSM feedback signal to detect standstill.  
When this limit value is undershot (take into account the parameterized hysteresis),
signal "SSM feedback signal active" is set.

**Note:** 
  
SSM: Safe Speed Monitor (safety-relevant feedback signal from the speed monitoring)

### p9547 SI SSM velocity hysteresis

[S210](#p9547-si-ssm-velocity-hysteresis-1)

[S210 Safety rot](#p9547-si-ssm-velocity-hysteresis-2)

#### p9547 SI SSM velocity hysteresis

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm/min | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.0010 [mm/min] | 500.0000 [mm/min] | [0] 30.0000 [mm/min] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the velocity hysteresis for the SSM feedback signal to detect standstill (n <
nx).

**Dependency:** 
  
See also:
C01711

**Note:** 
  
The following applies when parameterizing the hysteresis:  
- Set parameters p9546 and p9547 according to the following rule: p9546 * 0.75 >=
p9547  
  
SSM: Safe Speed Monitor (safety-relevant feedback signal from the speed monitoring)

#### p9547 SI SSM velocity hysteresis

|  |  |  |
| --- | --- | --- |
| **Variant:**S210 (Safety rot) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** rpm | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.0010 [rpm] | 500.0000 [rpm] | [0] 30.0000 [rpm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the velocity hysteresis for the SSM feedback signal to detect standstill (n <
nx).

**Dependency:** 
  
See also:
C01711

**Note:** 
  
The following applies when parameterizing the hysteresis:  
- Set parameters p9546 and p9547 according to the following rule: p9546 * 0.75 >=
p9547  
  
SSM: Safe Speed Monitor (safety-relevant feedback signal from the speed monitoring)

### p9548 SI SAM velocity tolerance

[S210](#p9548-si-sam-velocity-tolerance-1)

[S210 Safety rot](#p9548-si-sam-velocity-tolerance-2)

#### p9548 SI SAM velocity tolerance

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm/min | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [mm/min] | 120000.00 [mm/min] | [0] 300.00 [mm/min] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the velocity tolerance for function "SAM (Safe Acceleration Monitor)".  
If the drive velocity increases during the down ramp by more than this tolerance,
then SAM identifies this and STO (Safe Torque Off) is initiated.

**Dependency:** 
  
See also:
C01706

#### p9548 SI SAM velocity tolerance

|  |  |  |
| --- | --- | --- |
| **Variant:**S210 (Safety rot) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** rpm | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [rpm] | 120000.00 [rpm] | [0] 300.00 [rpm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the velocity tolerance for function "SAM (Safe Acceleration Monitor)".  
If the drive velocity increases during the down ramp by more than this tolerance,
then SAM identifies this and STO (Safe Torque Off) is initiated.

**Dependency:** 
  
See also:
C01706

### p9551 SI SLS delay time for limit value change

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [ms] | 600000.00 [ms] | [0] 100.00 [ms] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the delay time for the limit value change for function SLS (Safely-Limited Speed).  
When transitioning from a higher to a lower safely-limited velocity/speed stage, within
this delay time, the "old" velocity stage remains active.  
Even if SLS is activated from the state "SLS inactive", then this delay time is still
applied.

**Note:** 
  
The set time is rounded internally to an integer multiple of the monitoring clock
cycle.

### p9552 SI transition time SS2 to SOS

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [ms] | 600000.00 [ms] | [0] 100.00 [ms] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the transition time from SS2 to SOS.

**Note:** 
  
The set time is rounded internally to an integer multiple of the monitoring clock
cycle.  
SS2: Safe Stop 2  
SOS: Safe Operating Stop

### p9553 SI transition time SS2E to SOS

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [ms] | 600000.00 [ms] | [0] 100.00 [ms] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the transition time from SS2E to SOS.

**Note:** 
  
The set time is rounded internally to an integer multiple of the monitoring clock
cycle.  
SS2E: Safe Stop 2 External (Safe Stop 2 with external stop)  
SOS: Safe Operating Stop

### p9555 SI transition time SCF to SS1/SS1E

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [ms] | 600000.00 [ms] | [0] 0.00 [ms] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the transition time from SCF (Safety Channel Failure) to SS1 (Safe Stop 1) /
SS1E (Safe Stop 1 with external Stop).

**Dependency:** 
  
See also:
p9561  
See also:
C01701, C01702, C01711

**Note:** 
  
The set time is rounded internally to an integer multiple of the monitoring clock
cycle.

### p9556 SI transition time SS1 to STO

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [ms] | 3600000.00 [ms] | [0] 100.00 [ms] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the transition time from SS1 (Safe Stop 1) to STO (Safe Torque Off).  
The parameter has no effect for motion monitoring functions with safe brake ramp monitoring
(p9606 = 2).

**Dependency:** 
  
See also:
p9560  
See also:
C01701

**Note:** 
  
The set time is rounded internally to an integer multiple of the monitoring clock
cycle.

### p9560 SI STO shutdown velocity

[S210](#p9560-si-sto-shutdown-velocity-1)

[S210 Safety rot](#p9560-si-sto-shutdown-velocity-2)

#### p9560 SI STO shutdown velocity

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm/min | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [mm/min] | 6000.00 [mm/min] | [0] 0.00 [mm/min] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the shutdown velocity for activating STO (Safe Torque Off).  
Below this velocity, "standstill" is assumed, and for SS1/SS1E (Safe Stop 1/Safe Stop
1 External), STO is initiated.  
For motion monitoring functions with safe brake ramp monitoring (p9606 = 2), the parameter
must be > 0, as it is the only cancel criterion for SBR (Safe Brake Ramp).

**Dependency:** 
  
See also:
p9556

**Note:** 
  
The shutdown velocity has no effect for a value = 0.

#### p9560 SI STO shutdown velocity

|  |  |  |
| --- | --- | --- |
| **Variant:**S210 (Safety rot) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** rpm | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [rpm] | 6000.00 [rpm] | [0] 0.00 [rpm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the shutdown velocity for activating STO (Safe Torque Off).  
Below this velocity, "standstill" is assumed, and for SS1/SS1E (Safe Stop 1/Safe Stop
1 External), STO is initiated.  
For motion monitoring functions with safe brake ramp monitoring (p9606 = 2), the parameter
must be > 0, as it is the only cancel criterion for SBR (Safe Brake Ramp).

**Dependency:** 
  
See also:
p9556

**Note:** 
  
The shutdown velocity has no effect for a value = 0.

### p9561 SI SCF stop response

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 1 | 2 | [0] 1 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the stop response after SCF (Safety Channel Failure).

**Value:** 
  
1:
SS1 (Safe Stop 1)  
2:
SS1E (Safe Stop 1 External)

**Dependency:** 
  
See also:
p9555  
See also:
C01701, C01702, C01711

**Note:** 
  
SI: Safety Integrated  
SS1: Safe Stop 1  
SS1E: Safe Stop 1 External (Safe Stop 1 with external stop)

### p9563[0...3] SI SLS stop response

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 4 | [0] 1 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the specific stop response for the SLS function.  
These settings apply to the individual limit values for SLS.

**Value:** 
  
0:
STO (Safe Torque Off)  
1:
SS1 (Safe Stop 1)  
2:
SS1E (Safe Stop 1 External)  
3:
SS2 (Safe Stop 2)  
4:
SS2E (Safe Stop 2 External)

**Index:** 
  
[
0]:
Limit value SLS1  
[
1]:
Limit value SLS2  
[
2]:
Limit value SLS3  
[
3]:
Limit value SLS4

**Dependency:** 
  
See also:
p9531, p9561

**Note:** 
  
SI: Safety Integrated  
SLS: Safely-Limited Speed  
SS1: Safe Stop 1  
SS1E: Safe Stop 1 External (Safe Stop 1 with external Stop)  
SS2: Safe Stop 2  
SS2E: Safe Stop 2 External  
STO: Safe Torque Off

### p9564 SI SDI tolerance

[S210](#p9564-si-sdi-tolerance-1)

[S210 Safety rot](#p9564-si-sdi-tolerance-2)

#### p9564 SI SDI tolerance

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.001 [mm] | 360.000 [mm] | [0] 12.000 [mm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the tolerance for function SDI (Safe Direction).  
This motion in the monitored direction is still permissible without a stop response
occurring and safety message C01716 being output.

**Dependency:** 
  
See also:
p9565, p9566  
See also:
C01716

#### p9564 SI SDI tolerance

|  |  |  |
| --- | --- | --- |
| **Variant:**S210 (Safety rot) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.001 [°] | 360.000 [°] | [0] 12.000 [°] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the tolerance for function SDI (Safe Direction).  
This motion in the monitored direction is still permissible without a stop response
occurring and safety message C01716 being output.

**Dependency:** 
  
See also:
p9565, p9566  
See also:
C01716

### p9565 SI SDI delay time

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [ms] | 600000.00 [ms] | [0] 100.00 [ms] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the delay time for function SDI (Safe Direction).  
After selecting the SDI function, then for a maximum of this time, motion in the monitored
direction is permissible. This time can therefore be used for braking any motion.

**Dependency:** 
  
See also:
p9564, p9566  
See also:
C01716

**Note:** 
  
The set time is rounded internally to an integer multiple of the monitoring clock
cycle.

### p9566 SI SDI stop response

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 4 | [0] 1 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the stop response for the SDI function (Safe Direction).  
This setting applies to both directions of motion.

**Value:** 
  
0:
STO (Safe Torque Off)  
1:
SS1 (Safe Stop 1)  
2:
SS1E (Safe Stop 1 External)  
3:
SS2 (Safe Stop 2)  
4:
SS2E (Safe Stop 2 External)

**Dependency:** 
  
See also:
p9564, p9565  
See also:
C01716

### p9568 SI SAM velocity limit

[S210](#p9568-si-sam-velocity-limit-1)

[S210 Safety rot](#p9568-si-sam-velocity-limit-2)

#### p9568 SI SAM velocity limit

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm/min | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [mm/min] | 1000.00 [mm/min] | [0] 0.00 [mm/min] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the velocity limit for the "SAM (Safe Acceleration Monitor)" function.  
The SAM limit value is limited downward to this value.

#### p9568 SI SAM velocity limit

|  |  |  |
| --- | --- | --- |
| **Variant:**S210 (Safety rot) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** rpm | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [rpm] | 1000.00 [rpm] | [0] 0.00 [rpm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the velocity limit for the "SAM (Safe Acceleration Monitor)" function.  
The SAM limit value is limited downward to this value.

### p9576 SI SLA filter time

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [ms] | 500.00 [ms] | [0] 0.00 [ms] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the filter time for the acceleration monitoring with a fine resolution of the
acceleration.

**Note:** 
  
The filter time is only active if the function is enabled (p9604.13 = 1).  
SLA: Safely-Limited Acceleration

### p9578 SI SLA acceleration limit

[S210](#p9578-si-sla-acceleration-limit-1)

[S210 Safety rot](#p9578-si-sla-acceleration-limit-2)

#### p9578 SI SLA acceleration limit

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** m/s² | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [m/s²] | 1000.00 [m/s²] | [0] 1.00 [m/s²] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the acceleration limit for function SLA.

**Dependency:** 
  
See also:
p9579  
See also:
C01717

**Note:** 
  
SLA: Safely-Limited Acceleration

#### p9578 SI SLA acceleration limit

|  |  |  |
| --- | --- | --- |
| **Variant:**S210 (Safety rot) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** rev/s² | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [rev/s²] | 1000.00 [rev/s²] | [0] 1.00 [rev/s²] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the acceleration limit for function SLA.

**Dependency:** 
  
See also:
p9579  
See also:
C01717

**Note:** 
  
SLA: Safely-Limited Acceleration

### p9579 SI SLA stop response

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 4 | [0] 1 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the stop response for function SLA.

**Value:** 
  
0:
STO (Safe Torque Off)  
1:
SS1 (Safe Stop 1)  
2:
SS1E (Safe Stop 1 External)  
3:
SS2 (Safe Stop 2)  
4:
SS2E (Safe Stop 2 External)

**Dependency:** 
  
See also:
p9578  
See also:
C01717

**Note:** 
  
SI: Safety Integrated  
SLA: Safely-Limited Acceleration  
SS1: Safe Stop 1  
SS1E: Safe Stop 1 External (Safe Stop 1 with external stop)  
SS2: Safe Stop 2  
SS2E: Safe Stop 2 External (Safe Stop 2 with external stop)  
STO: Safe Torque Off

### p9581 SI SBR reference velocity for SS1 and SS2

[S210](#p9581-si-sbr-reference-velocity-for-ss1-and-ss2-1)

[S210 Safety rot](#p9581-si-sbr-reference-velocity-for-ss1-and-ss2-2)

#### p9581 SI SBR reference velocity for SS1 and SS2

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm/min | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 600.0000 [mm/min] | 1000000.0000 [mm/min] | [0] 1500.0000 [mm/min] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the reference velocity for monitoring SBR (Safe Brake Ramp) for SS1 and SS2.  
The SBR brake ramp gradient depends on p9581 (reference velocity ) and p9583 (reference
time).

**Dependency:** 
  
See also:
p9582, p9583

#### p9581 SI SBR reference velocity for SS1 and SS2

|  |  |  |
| --- | --- | --- |
| **Variant:**S210 (Safety rot) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** rpm | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 600.0000 [rpm] | 1000000.0000 [rpm] | [0] 1500.0000 [rpm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the reference velocity for monitoring SBR (Safe Brake Ramp) for SS1 and SS2.  
The SBR brake ramp gradient depends on p9581 (reference velocity ) and p9583 (reference
time).

**Dependency:** 
  
See also:
p9582, p9583

### p9582 SI SAM/SBR delay time for SS1 and SS2

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 10.00 [ms] | 99000.00 [ms] | [0] 50.00 [ms] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the delay time for monitoring SAM (Safe Acceleration Monitor) / SBR (Safe Brake
Ramp) for SS1 and SS2.  
The SAM/SBR monitoring is started once the delay time has expired.

**Dependency:** 
  
See also:
p9581, p9583

**Note:** 
  
The set time is rounded internally to an integer multiple of the monitoring clock
cycle.  
Internally, the set time is limited downwards (lower limit) to 2 safety monitoring
clock cycles (2 * p9500).

### p9583 SI SBR reference time for SS1 and SS2

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** s | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.50 [s] | 3600.00 [s] | [0] 10.00 [s] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the reference time for monitoring SBR (Safe Brake Ramp) for SS1 and SS2.  
The SBR brake ramp gradient depends on p9581 (reference velocity ) and p9583 (reference
time).

**Dependency:** 
  
See also:
p9581, p9582

**Note:** 
  
The set time is rounded internally to an integer multiple of the monitoring clock
cycle.

### p9584 SI SBR velocity limit

[S210](#p9584-si-sbr-velocity-limit-1)

[S210 Safety rot](#p9584-si-sbr-velocity-limit-2)

#### p9584 SI SBR velocity limit

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm/min | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [mm/min] | 1000.00 [mm/min] | [0] 0.00 [mm/min] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the velocity limit for function "SBR (Safe Brake Ramp)".  
The SBR lower limit value is limited to this value.

**Dependency:** 
  
See also:
p9568

#### p9584 SI SBR velocity limit

|  |  |  |
| --- | --- | --- |
| **Variant:**S210 (Safety rot) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** rpm | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [rpm] | 1000.00 [rpm] | [0] 0.00 [rpm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the velocity limit for function "SBR (Safe Brake Ramp)".  
The SBR lower limit value is limited to this value.

**Dependency:** 
  
See also:
p9568

### p9591 SI SBR reference velocity for SS1E and SS2E

[S210](#p9591-si-sbr-reference-velocity-for-ss1e-and-ss2e-1)

[S210 Safety rot](#p9591-si-sbr-reference-velocity-for-ss1e-and-ss2e-2)

#### p9591 SI SBR reference velocity for SS1E and SS2E

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm/min | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 600.0000 [mm/min] | 1000000.0000 [mm/min] | [0] 1500.0000 [mm/min] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the reference velocity for monitoring SBR (Safe Brake Ramp) for SS1E and SS2E.  
The gradient of the SBR braking ramp depends on p9591 (reference velocity) and p9593
(reference time).

**Dependency:** 
  
See also:
p9592, p9593

#### p9591 SI SBR reference velocity for SS1E and SS2E

|  |  |  |
| --- | --- | --- |
| **Variant:**S210 (Safety rot) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** rpm | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 600.0000 [rpm] | 1000000.0000 [rpm] | [0] 1500.0000 [rpm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the reference velocity for monitoring SBR (Safe Brake Ramp) for SS1E and SS2E.  
The gradient of the SBR braking ramp depends on p9591 (reference velocity) and p9593
(reference time).

**Dependency:** 
  
See also:
p9592, p9593

### p9592 SI SAM/SBR delay time for SS1E and SS2E

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 10.00 [ms] | 99000.00 [ms] | [0] 50.00 [ms] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the delay time for monitoring SAM (Safe Acceleration Monitor) / SBR (Safe Brake
Ramp) for SS1E and SS2E.  
The SAM/SBR monitoring is started once the delay time has expired.

**Dependency:** 
  
See also:
p9591, p9593

**Note:** 
  
The set time is rounded internally to an integer multiple of the monitoring clock
cycle.  
Internally, the set time is limited downwards (lower limit) to 2 safety monitoring
clock cycles (2 * p9500).

### p9593 SI SBR reference time for SS1E and SS2E

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** s | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.50 [s] | 3600.00 [s] | [0] 10.00 [s] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the reference time for monitoring SBR (Safe Brake Ramp) for SS1E and SS2E.  
The gradient of the SBR braking ramp depends on p9591 (reference velocity) and p9593
(reference time).

**Dependency:** 
  
See also:
p9591, p9592

**Note:** 
  
The set time is rounded internally to an integer multiple of the monitoring clock
cycle.

### p9594 SI transition time SS1E to STO

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [ms] | 3600000.00 [ms] | [0] 100.00 [ms] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the transition time from SS1E (Safe Stop 1 External) to STO (Safe Torque Off).  
The parameter has no effect for motion monitoring functions with safe brake ramp monitoring
(p9607 = 2).

**Dependency:** 
  
See also:
p9560  
See also:
C01702

**Note:** 
  
The set time is rounded internally to an integer multiple of the monitoring clock
cycle.

### p9595 SI SLA delay time

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [ms] | 600000.00 [ms] | [0] 100.00 [ms] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the delay time for function SLA (Safely-Limited Acceleration).  
SLA is activated from state "SLA inactive" with this delay time.

**Note:** 
  
The set time is rounded internally to an integer multiple of the monitoring clock
cycle.

### p9596 SI SOS delay time

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [ms] | 600000.00 [ms] | [0] 100.00 [ms] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the delay time for the SOS function (Safe Operating Stop).  
Activating SOS from state "SOS inactive" is always realized with this delay time.

**Dependency:** 
  
See also:
p9530

**Note:** 
  
The set time is rounded internally to an integer multiple of the monitoring clock
cycle.

### p9603.0...1 SI control

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| - | - | [0] 0000 bin |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the type of control for the safety functions integrated in the drive.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Control via F-DI | Inhibit | Enable | - |
| 01 | Control via PROFIsafe | Inhibit | Enable | - |

**Note:** 
  
When online safety commissioning has been completed, a change results in an automatic
restart.  
If no bit is set, then Safety Integrated is inhibited for this drive.  
When controlled via terminal (bit 00 = 1 signal), only STO / SS1 / SS1E may be interconnected.

### p9604.0...30 SI enable

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| - | - | [0] 0000 0000 0000 0000 0000 0000 0000 0000 bin |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the enable signal for the safety functions integrated in the drive.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Enable STO | Inhibit | Enable | - |
| 01 | Enable SBC | Inhibit | Enable | - |
| 02 | Enable SS1 | Inhibit | Enable | - |
| 03 | Enable SS1E | Inhibit | Enable | - |
| 04 | Enable SS2 | Inhibit | Enable | - |
| 05 | Enable SS2E | Inhibit | Enable | - |
| 07 | Enable SOS | Inhibit | Enable | - |
| 08 | Enable SLS | Inhibit | Enable | - |
| 09 | Enable SLS dynamic | Inhibit | Enable | - |
| 11 | Enable SDI | Inhibit | Enable | - |
| 12 | Enable SSM | Inhibit | Enable | - |
| 13 | Enable SLA | Inhibit | Enable | - |
| 23 | Enable SBT | Inhibit | Enable | - |
| 30 | Enable F-DI in PROFIsafe telegram | Inhibit | Enable | - |

### p9606 SI SS1 function specification

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 2 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the function specification of the SS1 (Safe Stop 1) safety function integrated
in the drive.

**Value:** 
  
0:
SSX-t time-controlled  
1:
SSX-a acceleration-monitored  
2:
SSX-r ramp-monitored

### p9607 SI SS1E function specification

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 2 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the function specification of the SS1E (Safe Stop 1 External) safety function
integrated in the drive.

**Value:** 
  
0:
SSX-t time-controlled  
1:
SSX-a acceleration-monitored  
2:
SSX-r ramp-monitored

### p9608 SI SS2 function specification

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 2 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the function specification of the SS2 (Safe Stop 2) safety function integrated
in the drive.

**Value:** 
  
0:
SSX-t time-controlled  
1:
SSX-a acceleration-monitored  
2:
SSX-r ramp-monitored

### p9609 SI SS2E function specification

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 2 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the function specification of the SS2E (Safe Stop 2 External) safety function
integrated in the drive.

**Value:** 
  
0:
SSX-t time-controlled  
1:
SSX-a acceleration-monitored  
2:
SSX-r ramp-monitored

### p9610 SI PROFIsafe destination address

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 65534 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the PROFIsafe destination address (F_Dest_Add).

**Note:** 
  
When online safety commissioning has been completed, a change results in an automatic
restart.

### p9611 SI PROFIsafe telegram selection

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 901 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the PROFIsafe telegram number.

**Value:** 
  
0:
No PROFIsafe telegram selected  
30:
PROFIsafe standard telegram 30, PZD-1/1  
901:
PROFIsafe SIEMENS telegram 901, PZD-3/5

**Dependency:** 
  
See also:
r60022

### p9612 SI stop response for failure or control fault

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 1 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the stop response for failure or control fault (e.g. PROFIsafe communication).

**Value:** 
  
0:
STO  
1:
SS1

**Note:** 
  
For p9612 = 0 (STO):  
The drive safely switches off the motor, the motor coasts down.  
For p9612 = 1 (SS1):  
The drive brakes the motor with OFF3 ramp-down time until standstill is detected.
A switchover is then made to STO.

### p9613 SI PROFIsafe source address

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 65534 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the PROFIsafe source address (F_Source_Add).

**Note:** 
  
When online safety commissioning has been completed, a change results in an automatic
restart.

### p9614 SI PROFIsafe F_watchdog time

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 [ms] | 65535 [ms] | [0] 0 [ms] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the PROFIsafe monitoring time (F_WD_Time).

### p9619 SI PROFIsafe compatibility mode SS1 / SS1E

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 1 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the project conversion for the correct response of function Safe Stop 1 (SS1)
or Safe Stop 1 External (SS1E).  
When importing projects with V5.2 and configuring SS1/SS1E, this parameter is automatically
set to the correct value.  
  
For value = 0:  
All safety settings and displays correspond to the standard response of the firmware
used.  
  
For value = 1:  
A project with FW version V5.2 and SS1E was detected and converted.  
The significance of the following parameter was changed:  
- SI PROFIsafe control word (channels A and B) r10075/r10175  
Bit 01: Selection and deselection of SS1E  
Bit 18: is not evaluated.  
- SI Safety Info Channel status word S_ZSW1B (r9734.0...15)  
Bit 01: Display of SS1E active or SS1 as stop response  
- SI Safety Info Channel status word S_ZSW2B (r9743.3...9)  
Bit 03: A 0 signal is always displayed.

**Value:** 
  
0:
No compatibility mode   
1:
Compatibility mode SS1/SS1E for project imports with V5.2

### p9630 SI safe maximum speed encoder (rotary)

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** rpm | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 [rpm] | 300000000 [rpm] | [0] 0 [rpm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the safe maximum speed for the rotary encoder (encoder side).

### p9631 SI safe position accuracy encoder (rotary)

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.000 [°] | 360.000 [°] | [0] 0.000 [°] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the safe position accuracy for the rotary encoder (encoder side).

### r9634 SI safe maximum speed encoder detected (rotary)

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** rpm | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the safe maximum speed for the rotary encoder (encoder side) that was detected.

### r9635 SI safe position accuracy encoder detected (rotary)

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the safe position accuracy for the rotary encoder (encoder side) that was
detected.

### p9659 SI brake output test timer

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** h | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.00 [h] | 9000.00 [h] | [0] 2160.00 [h] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the time interval for carrying out the forced checking procedure and testing
the safety brake control.  
Within the parameterized time, when the SBC function is enabled, the brake must have
been closed or opened at least once. The monitoring time is reset each time the brake
is opened or closed.

**Note:** 
  
SBC: Safe Brake Control

### r9660 SI brake output test remaining time

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** h | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the time remaining before the brake output is tested.

### p9670 SI module identification drive

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Ready for operation |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 4294967295 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Safety Integrated module identifier for the drive.  
Replacement of the drive is identified when the safety functions are activated.

**Dependency:** 
  
See also:
A01641

**Note:** 
  
After replacement, when the drive runs up, an alarm is output

### p9674 SI module identifier Sensor Module

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Ready for operation |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 4294967295 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Module identifier of the Sensor Module.

### p9675 SI module identifier encoder

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Ready for operation |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 4294967295 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Module identifier of the encoder.

**Note:** 
  
The value = 0 when using an encoder without its own serial number.

### p9676 SI identifier encoder properties

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Ready for operation |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 4294967295 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Identifier for the encoder properties.

### p9677 SI offset POS1 POS2 encoder

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Ready for operation |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| -2147483648 | 2147483647 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the offset between encoder positions POS1 and POS2.  
This value is used only once to perform a check after running up.

### p9699 SI configuration alarm filtering

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Ready for operation |  |  |
| **Parameter group:** Basic functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 1 | [0] 1 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the enable for the "Alarm filtering" function.

**Value:** 
  
0:
Deactivate alarm filtering  
1:
Activate alarm filtering

**Note:** 
  
Parameter is active after a POWER ON

### r9708 SI diagnostics safe position

[S210](#r9708-si-diagnostics-safe-position-1)

[S210 Safety rot](#r9708-si-diagnostics-safe-position-2)

#### r9708 SI diagnostics safe position

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the actual load-side actual value.

**Note:** 
  
The display of the load-side position actual value is updated in the monitoring clock
cycle.

#### r9708 SI diagnostics safe position

|  |  |  |
| --- | --- | --- |
| **Variant:**S210 (Safety rot) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the actual load-side actual value.

**Note:** 
  
The display of the load-side position actual value is updated in the monitoring clock
cycle.

### r9714[0...7] SI diagnostics velocity

[S210](#r971407-si-diagnostics-velocity-1)

[S210 Safety rot](#r971407-si-diagnostics-velocity-2)

#### r9714[0...7] SI diagnostics velocity

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm/min | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Displays the velocity actual values for motion monitoring functions.

**Index:** 
  
[
0]:
Load side velocity actual value  
[
1]:
SS1: Actual SAM/SBR velocity limit  
[
2]:
Actual SLS velocity limit  
[
3]:
Actual SLA velocity limit  
[
4]:
Load side filtered velocity actual value  
[
5]:
SS2: Actual SAM/SBR velocity limit  
[
6]:
SS1E: Actual SAM/SBR velocity limit  
[
7]:
SS2E: Actual SAM/SBR velocity limit

**Dependency:** 
  
See also:
r9732

**Notice:** 
  
For index [2]:  
This SLS velocity limit can, as a result of conversion into the internal monitoring
format, deviate from the specified SLS velocity limit (see r9732).

**Note:** 
  
The display is updated in the SI monitoring clock cycle.

#### r9714[0...7] SI diagnostics velocity

|  |  |  |
| --- | --- | --- |
| **Variant:**S210 (Safety rot) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** rpm | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Displays the velocity actual values for motion monitoring functions.

**Index:** 
  
[
0]:
Load side velocity actual value  
[
1]:
SS1: Actual SAM/SBR velocity limit  
[
2]:
Actual SLS velocity limit  
[
3]:
Actual SLA velocity limit  
[
4]:
Load side filtered velocity actual value  
[
5]:
SS2: Actual SAM/SBR velocity limit  
[
6]:
SS1E: Actual SAM/SBR velocity limit  
[
7]:
SS2E: Actual SAM/SBR velocity limit

**Dependency:** 
  
See also:
r9732

**Notice:** 
  
For index [2]:  
This SLS velocity limit can, as a result of conversion into the internal monitoring
format, deviate from the specified SLS velocity limit (see r9732).

**Note:** 
  
The display is updated in the SI monitoring clock cycle.

### r9720.0...28 SI control word

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source binary/numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Control signals for safety functions integrated in the drive.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Deselect STO | No | Yes | - |
| 01 | Deselect SS1 | No | Yes | - |
| 02 | Deselect SS2 | No | Yes | - |
| 03 | Deselect SOS | No | Yes | - |
| 04 | Deselect SLS | No | Yes | - |
| 07 | Acknowledgment | No | Signal edge active | - |
| 08 | Deselect SLA | No | Yes | 2838 |
| 09 | Select SLS bit 0 | Not set | Set | - |
| 10 | Select SLS bit 1 | Not set | Set | - |
| 12 | Deselect SDI positive | No | Yes | 2824 |
| 13 | Deselect SDI negative | No | Yes | 2824 |
| 15 | Deselect SSM | No | Yes | - |
| 18 | Deselect SS1E | No | Yes | - |
| 28 | Deselect SS2E | No | Yes | - |

**Note:** 
  
Note: only the control signals of the available and enabled functions (see p9604)
are updated. All others are 1 across the board.

### r9722.0...28 SI status signals

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source binary/numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Display for the status signals of the safety functions (synchronized signal).

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | STO or safe pulse cancellation active | No | Yes | - |
| 01 | SS1 active | No | Yes | - |
| 02 | SS2 active | No | Yes | - |
| 03 | SOS active | No | Yes | - |
| 04 | SLS active | No | Yes | - |
| 07 | Internal event | Yes | No | - |
| 08 | SLA active | No | Yes | 2838 |
| 09 | Active SLS limit value bit 0 | Not set | Set | - |
| 10 | Active SLS limit value bit 1 | Not set | Set | - |
| 11 | SOS selected | No | Yes | - |
| 12 | SDI positive active | No | Yes | 2824 |
| 13 | SDI negative active | No | Yes | 2824 |
| 15 | SSM (speed below limit value) | No | Yes | 2823 |
| 18 | SS1E active | No | Yes | - |
| 28 | SS2E active | No | Yes | - |

**Notice:** 
  
For bit 07:  
An internal event is displayed if a stop function is active.  
The signal state behaves in an opposite way to the PROFIsafe Standard.

**Note:** 
  
Only the status signals of the enabled functions (see p9604) are updated, all others
are 0 across the board.  
Bit 09 and bit 10 together determine the selected SLS limit value.

### r9725[0...2] SI diagnostics data cross-check

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the diagnostics of the data cross-check.  
For index [0]  
Number of the data, which, for the data cross-check between the two monitoring channels,
led to the SCF (Safety Channel Failure) on the drive.  
For index [1]:  
Displays the value from channel A for a KDV error.  
For index [2]:  
Displays the value from channel B for a KDV error.

**Index:** 
  
[
0]:
Message value for KDV  
[
1]:
KDV actual value channel A  
[
2]:
KDV actual value channel B

**Dependency:** 
  
See also:
C01769

**Note:** 
  
KDV: Data cross-check

### r9728 SI actual checksum configuration of the safety functions

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the checksum over the checked parameters used to configure safety functions
(actual checksum).

**Dependency:** 
  
See also:
p9729

### p9729 SI reference checksum configuration of the safety functions

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0000 hex | FFFF FFFF hex | [0] A1A1 A1A1 hex |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the checksum over the checked parameters used to configure safety functions (reference
checksum).

**Dependency:** 
  
See also:
r9728

### r9730 SI Safe maximum velocity

[S210](#r9730-si-safe-maximum-velocity-1)

[S210 Safety rot](#r9730-si-safe-maximum-velocity-2)

#### r9730 SI Safe maximum velocity

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm/min | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the safe maximum velocity (on the load side) that is permissible for the
safe motion monitoring functions as a result of the actual value sensing.  
This parameter indicates up to which load velocity the safe encoder actual values
(redundant encoder coarse position) can still be correctly detected as a result of
the particular encoder parameterization.  
This parameter is only of significance for enabled safety with encoder (otherwise
"0").

#### r9730 SI Safe maximum velocity

|  |  |  |
| --- | --- | --- |
| **Variant:**S210 (Safety rot) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** rpm | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the safe maximum velocity (on the load side) that is permissible for the
safe motion monitoring functions as a result of the actual value sensing.  
This parameter indicates up to which load velocity the safe encoder actual values
(redundant encoder coarse position) can still be correctly detected as a result of
the particular encoder parameterization.  
This parameter is only of significance for enabled safety with encoder (otherwise
"0").

### r9731 SI safe position accuracy

[S210](#r9731-si-safe-position-accuracy-1)

[S210 Safety rot](#r9731-si-safe-position-accuracy-2)

#### r9731 SI safe position accuracy

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the safe position accuracy (load side).  
As a result of the actual value sensing for safe motion monitoring functions, this
accuracy can be achieved as the maximum.

**Note:** 
  
The parameter is only of significance for enabled safety with encoder (otherwise "0").

#### r9731 SI safe position accuracy

|  |  |  |
| --- | --- | --- |
| **Variant:**S210 (Safety rot) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the safe position accuracy (load side).  
As a result of the actual value sensing for safe motion monitoring functions, this
accuracy can be achieved as the maximum.

**Note:** 
  
The parameter is only of significance for enabled safety with encoder (otherwise "0").

### r9732[0...1] SI velocity resolution

[S210](#r973201-si-velocity-resolution-1)

[S210 Safety rot](#r973201-si-velocity-resolution-2)

#### r9732[0...1] SI velocity resolution

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm/min | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the velocity resolution for safety-relevant motion monitoring functions.  
For index [0]:  
Displays the safe velocity resolution (load side). Setpoints for velocity limits or
parameter changes for velocities below this threshold have no effect.  
For index [1]:  
Displays the safe velocity accuracy based on the safe encoder accuracy

**Index:** 
  
[
0]:
Actual velocity resolution  
[
1]:
Minimum velocity resolution

**Note:** 
  
For index [0]:  
This parameter does not provide any information about the actual accuracy of the velocity
sensing. This depends on the type of actual value sensing, the gear factors as well
as the quality of the encoder being used.  
Conversion of:  
(internal fixed value / Tsi) to mm/min (linear) or rpm (rotary) with Tsi = p9500 (SI
monitoring cycle).  
Example:  
For Tsi = 4 ms, r9732[0] = 15 mm/min (linear) or 1/24 rpm (rotary) is obtained.  
  
For index [1]:  
- Only takes into account the coarse encoder resolution and is an internal calculation,
which also incorporates the factor for the motor-load side conversion, the gear ratio
and the SI monitoring clock cycle.

#### r9732[0...1] SI velocity resolution

|  |  |  |
| --- | --- | --- |
| **Variant:**S210 (Safety rot) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** rpm | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the velocity resolution for safety-relevant motion monitoring functions.  
For index [0]:  
Displays the safe velocity resolution (load side). Setpoints for velocity limits or
parameter changes for velocities below this threshold have no effect.  
For index [1]:  
Displays the safe velocity accuracy based on the safe encoder accuracy

**Index:** 
  
[
0]:
Actual velocity resolution  
[
1]:
Minimum velocity resolution

**Note:** 
  
For index [0]:  
This parameter does not provide any information about the actual accuracy of the velocity
sensing. This depends on the type of actual value sensing, the gear factors as well
as the quality of the encoder being used.  
Conversion of:  
(internal fixed value / Tsi) to mm/min (linear) or rpm (rotary) with Tsi = p9500 (SI
monitoring cycle).  
Example:  
For Tsi = 4 ms, r9732[0] = 15 mm/min (linear) or 1/24 rpm (rotary) is obtained.  
  
For index [1]:  
- Only takes into account the coarse encoder resolution and is an internal calculation,
which also incorporates the factor for the motor-load side conversion, the gear ratio
and the SI monitoring clock cycle.

### r9733[0...2] SI effective setpoint velocity limiting

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** rpm | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** p2000 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the necessary setpoint velocity limit as a result of the selected motion
monitoring functions.  
Contrary to the parameterization of the SI limit values, this parameter specifies
the motor-side limit value and not the load-side limit value.

**Index:** 
  
[
0]:
Setpoint limiting positive  
[
1]:
Setpoint limiting negative  
[
2]:
Setpoint limit absolute

**Dependency:** 
  
For SLS: r9733[0] = p9531[x] x p9533 (converted from the load side to the motor side)  
For SDI negative: r9733[0] = 0  
For SLS: r9733[1] = - p9531[x] x p9533 (converted from the load side to the motor
side)  
For SDI positive: r9733[1] = 0  
[x] = selected SLS limit value  
Conversion factor from the load side to the motor side:  
- Motor type = rotary and axis type = linear: p9522 / (p9521 x p9520)  
- Otherwise: p9522 / p9521  
See also:
p9531, p9533

**Notice:** 
  
If only the absolute value of the setpoint velocity limiting is required, then r9733[2]
must be selected.

**Note:** 
  
The unit changeover between linear and rotary axis is not implemented via the safety
changeover (r9502) but by the linear motor changeover.  
If the "SLS" or "SDI" function is not selected, r9733[0] shows p1082 and r9733[1]
shows -p1082.  
The display in r9733 can be delayed by up to one SI monitoring clock cycle as compared
to the display in r9720 and r9722.  
When selecting a safety function, where standstill is reached or required (e.g. STO,
SS1), then setpoint 0 is specified in r9733.

### r9734.0...15 SI Safety Information Channel status word S_ZSW1B

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source binary/numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Display for status word S_ZSW1B of the Safety Information Channel.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | STO selected or active | No | Yes | - |
| 01 | SS1 active | No | Yes | - |
| 02 | SS2 active | No | Yes | - |
| 03 | SOS active | No | Yes | - |
| 04 | SLS active | No | Yes | - |
| 05 | SOS selected | No | Yes | - |
| 06 | SLS selected | No | Yes | - |
| 07 | Internal event | No | Yes | - |
| 08 | SLA selected | No | Yes | - |
| 09 | Select SLS bit0 | No | Yes | - |
| 10 | Select SLS bit1 | No | Yes | - |
| 12 | SDI positive selected | No | Yes | - |
| 13 | SDI negative selected | No | Yes | - |
| 14 | ESR retract requested | No | Yes | - |
| 15 | Safety message present | No | Yes | - |

**Note:** 
  
SIC: Safety Information Channel  
For bit 07:  
An internal event is displayed if a stop function is active.

### r9743.3...9 SI Safety Information Channel status word S_ZSW2B

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source binary/numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Display for status word S_ZSW2B of the Safety Info Channel.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 03 | SS1E active | No | Yes | - |
| 08 | SDI positive selected | No | Yes | - |
| 09 | SDI negative selected | No | Yes | - |

**Note:** 
  
SIC: Safety Information Channel

### r9750[0...63].0...20 SI diagnostic attributes

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
Bits 20, 19, 18, 17, 16 = 0, 0, 0, 0, 0 --> PROFIdrive message class 0: not assigned  
Bit 20, 19, 18, 17, 16 = 0, 0, 0, 0, 1 --> PROFIdrive message class 1: hardware fault/software
error  
Bits 20, 19, 18, 17, 16 = 0, 0, 0, 1, 0 --> PROFIdrive message class 2: line fault  
Bits 20, 19, 18, 17, 16 = 0, 0, 0, 1, 1 --> PROFIdrive message class 3: supply voltage
fault  
Bits 20, 19, 18, 17, 16 = 0, 0, 1, 0, 0 --> PROFIdrive message class 4: DC link fault  
Bits 20, 19, 18, 17, 16 = 0, 0, 1, 0, 1 --> PROFIdrive message class 5: power electronics
faulted  
Bits 20, 19, 18, 17, 16 = 0, 0, 1, 1, 0 --> PROFIdrive message class 6: overtemperature
electronic components  
Bits 20, 19, 18, 17, 16 = 0, 0, 1, 1, 1 --> PROFIdrive message class 7: ground fault/phase
fault detected  
Bits 20, 19, 18, 17, 16 = 0, 1, 0, 0, 0 --> PROFIdrive message class 8: motor overload  
Bits 20, 19, 18, 17, 16 = 0, 1, 0, 0, 1 --> PROFIdrive message class 9: communication
error to the higher-level control  
Bits 20, 19, 18, 17, 16 = 0, 1, 0, 1, 0 --> PROFIdrive message class 10: safe monitoring
channel has identified an error  
Bits 20, 19, 18, 17, 16 = 0, 1, 0, 1, 1 --> PROFIdrive message class 11: incorrect
position actual value/speed actual value or not available  
Bits 20, 19, 18, 17, 16 = 0, 1, 1, 0, 0 --> PROFIdrive message class 12: internal
(DRIVE-CLiQ) communication error  
Bits 20, 19, 18, 17, 16 = 0, 1, 1, 0, 1 --> PROFIdrive message class 13: infeed unit
faulted  
Bits 20, 19, 18, 17, 16 = 0, 1, 1, 1, 0 --> PROFIdrive message class 14: braking controller/Braking
Module faulted  
Bits 20, 19, 18, 17, 16 = 0, 1, 1, 1, 1 --> PROFIdrive message class 15: line filter
faulted  
Bits 20, 19, 18, 17, 16 = 1, 0, 0, 0, 0 --> PROFIdrive message class 16: external
measured value/signal state outside the permissible range  
Bits 20, 19, 18, 17, 16 = 1, 0, 0, 0, 1 --> PROFIdrive message class 17: application/technology
function faulted  
Bits 20, 19, 18, 17, 16 = 1, 0, 0, 1, 0 --> PROFIdrive message class 18: error in
the parameterization/configuration/commissioning sequence  
Bits 20, 19, 18, 17, 16 = 1, 0, 0, 1, 1 --> PROFIdrive message class 19: general drive
fault  
Bits 20, 19, 18, 17, 16 = 0, 1, 1, 0, 0 --> PROFIdrive message class 20: auxiliary
unit faulted

### r9753[0...63] SI message value for float values

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays additional information about the safety message that has occurred for float
values.

**Dependency:** 
  
See also:
r9754, r9755, r9756, r60044, r60045, r60048, r60049, p60052

### r9754[0...63] SI message time received in days

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the relative system runtime in days when the safety message occurred.

**Dependency:** 
  
See also:
r9753, r9755, r9756, r60044, r60045, r60048, r60049, p60052

### r9755[0...63] SI message time removed in milliseconds

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the relative system runtime in milliseconds when the safety message was removed.

**Dependency:** 
  
See also:
r9753, r9754, r9756, r60044, r60045, r60048, r60049, p60052

### r9756[0...63] SI message time removed in days

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the relative system runtime in days when the safety message was removed.

**Dependency:** 
  
See also:
r9753, r9754, r9755, r60044, r60045, r60048, r60049, p60052

### r9768[0...8] Receive SI PROFIsafe control words

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the received PROFIsafe telegram.

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

**Dependency:** 
  
See also:
r9769

**Note:** 
  
The PROFIsafe trailer at the end of the telegram is also displayed (5 bytes).

### r9769[0...8] Send SI PROFIsafe status words

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the PROFIsafe telegram to be sent.

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

**Dependency:** 
  
See also:
r9768

**Note:** 
  
The PROFIsafe trailer at the end of the telegram is also displayed (5 bytes).

### r9770[0...7] SI PROFIsafe configuration of the F-PLC

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the configuration data received from the F-PLC (when control via PROFIsafe
is enabled).

**Index:** 
  
[
0]:
Telegram number  
[
1]:
Control telegram length from the F-PLC in bytes  
[
2]:
Status telegram length to the F-PLC in bytes  
[
3]:
F_PRM_FLAG1, F_PRM_FLAG2  
[
4]:
F_Source_Add  
[
5]:
F_Dest_Add  
[
6]:
F_WD_Time  
[
7]:
F_Par_CRC

## SINAMICS Parameter S210 09771 - 11571

SINAMICS Parameter S210 09771 - 11571

### r9771[0...43] SI PROFIsafe diagnostics information CRC error

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Diagnostics data for CRC error in the cyclic PROFIsafe communication. The information
regarding the last signaled CRC error is always displayed.  
  
Structure of the diagnostic information:  
Bytes 0 to 1: diagnostic data structure version  
Bytes 2 to 9: IncNo_1: used in the V2.6.1 mode  
Bytes 10 to 17: IncNo_2: used in the V2.6.1 mode  
Bytes 18 to 21: received telegram CRC  
Bytes 22 to 25: expected telegram CRC  
Bytes 26 to 29: VirtualConsecutiveNo: used in the V2.4 mode  
Bytes 30 to 33: Code name: used in the V2.6.1 mode  
Bytes 34 to 37: Modifier: used in the V2.6.1 mode  
Bytes 38 to 41: CRC of the iParameters (not used)  
Bytes 42 to 43: CRC of the F-parameters

### r9776.0...4 SI diagnostics

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source binary |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the operating state, referred to the safety functions. The parameter is used
for diagnostics.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Safety parameter changed | No | Yes | - |
| 01 | Safety functions enabled | No | Yes | - |
| 02 | Safety component replaced and data save required | No | Yes | - |
| 04 | Safety commissioning mode active | No | Yes | - |

**Note:** 
  
For bit 00 = 1:  
At least one safety parameter was changed. The change only becomes effective after
a restart, which is automatically performed after exiting safety commissioning.  
For bit 01 = 1:  
Safety functions have been enabled and are active.  
For bit 02 = 1:  
A safety-relevant component has been replaced. Retentively save (save all parameters,
p0977 = 1)  
For bit 04 = 1:  
The safety commissioning mode is selected.

### r9780[0...1] SI checksum to check changes

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the checksum to track changes for Safety Integrated.  
These are additional checksums that are created to track changes to relevant safety
parameters (fingerprint for the "safety logbook" functionality).

**Index:** 
  
[
0]:
SI checksum to track functional changes  
[
1]:
SI checksum to track hardware-specific changes

**Dependency:** 
  
See also:
p9729, p9797

### r9781[0...1] SI change control time stamp days

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the day component of the time stamp for the checksums for tracking changes
for Safety Integrated.  
The time stamps are generated for the checksums (r9780[0...1]) (fingerprint for the
"safety logbook" functionality)

**Index:** 
  
[
0]:
SI time stamp for checksum to track functional changes  
[
1]:
SI time stamp for checksum to track hardware-specific changes

**Dependency:** 
  
See also:
p9729, p9797, p9799  
See also:
C01690

**Note:** 
  
The time comprises r9781 (days) and r9782 (milliseconds).

### r9782[0...1] SI change control time stamp milliseconds

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the millisecond component of the time stamp for the checksums for tracking
changes for Safety Integrated.  
The time stamps are generated for the checksums (r9780[0...1]) (fingerprint for the
"safety logbook" functionality)

**Index:** 
  
[
0]:
SI time stamp for checksum to track functional changes  
[
1]:
SI time stamp for checksum to track hardware-specific changes

**Dependency:** 
  
See also:
p9729, p9797, p9799  
See also:
C01690

**Note:** 
  
The time comprises r9781 (days) and r9782 (milliseconds).

### r9789[0...2] SI SLA acceleration diagnostics

[S210](#r978902-si-sla-acceleration-diagnostics-1)

[S210 Safety rot](#r978902-si-sla-acceleration-diagnostics-2)

#### r9789[0...2] SI SLA acceleration diagnostics

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** m/s² | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Display for the actual acceleration values and limit values for SLA.

**Index:** 
  
[
0]:
Acceleration actual value on the load side  
[
1]:
Lower acceleration limit  
[
2]:
Upper acceleration limit

**Note:** 
  
The display is updated in the safety monitoring clock cycle.  
Unit for linear axis: meters / (second * second)  
Unit for rotary axis: revolution / (second * second)  
  
SLA: Safely-Limited Acceleration

#### r9789[0...2] SI SLA acceleration diagnostics

|  |  |  |
| --- | --- | --- |
| **Variant:**S210 (Safety rot) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** rev/s² | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Display for the actual acceleration values and limit values for SLA.

**Index:** 
  
[
0]:
Acceleration actual value on the load side  
[
1]:
Lower acceleration limit  
[
2]:
Upper acceleration limit

**Note:** 
  
The display is updated in the safety monitoring clock cycle.  
Unit for linear axis: meters / (second * second)  
Unit for rotary axis: revolution / (second * second)  
  
SLA: Safely-Limited Acceleration

### r9790[0...1] SI SLA acceleration resolution

[S210](#r979001-si-sla-acceleration-resolution-1)

[S210 Safety rot](#r979001-si-sla-acceleration-resolution-2)

#### r9790[0...1] SI SLA acceleration resolution

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** m/s² | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Displays the acceleration resolution (load side) for function SLA.  
Setpoints for acceleration limits or parameter changes for acceleration levels below
this threshold have no effect.

**Index:** 
  
[
0]:
Coarse resolution  
[
1]:
Fine resolution

**Note:** 
  
This parameter does not provide any information about the actual accuracy of the acceleration
sensing. This depends on the type of actual value sensing, the gear factors as well
as the quality of the encoder being used.  
Conversion of:  
(internal fixed value/ Tsi²) to m/s² (linear) or 1/s² (rotary) with Tsi = p9500 (SI
monitoring clock cycle)  
Example:  
Coarse resolution: for Tsi = 4 ms, r9790[0] = 0.0625 m/s² (linear) or 0.173611 1/s²
(rotary) is obtained.  
Fine resolution: for Tsi = 4 ms, r9790[1] = 0.0000625 m/s² (linear) or 0.000173611
1/s² (rotary) is obtained.  
  
SLA: Safely-Limited Acceleration

#### r9790[0...1] SI SLA acceleration resolution

|  |  |  |
| --- | --- | --- |
| **Variant:**S210 (Safety rot) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** rev/s² | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Displays the acceleration resolution (load side) for function SLA.  
Setpoints for acceleration limits or parameter changes for acceleration levels below
this threshold have no effect.

**Index:** 
  
[
0]:
Coarse resolution  
[
1]:
Fine resolution

**Note:** 
  
This parameter does not provide any information about the actual accuracy of the acceleration
sensing. This depends on the type of actual value sensing, the gear factors as well
as the quality of the encoder being used.  
Conversion of:  
(internal fixed value/ Tsi²) to m/s² (linear) or 1/s² (rotary) with Tsi = p9500 (SI
monitoring clock cycle)  
Example:  
Coarse resolution: for Tsi = 4 ms, r9790[0] = 0.0625 m/s² (linear) or 0.173611 1/s²
(rotary) is obtained.  
Fine resolution: for Tsi = 4 ms, r9790[1] = 0.0000625 m/s² (linear) or 0.000173611
1/s² (rotary) is obtained.  
  
SLA: Safely-Limited Acceleration

### r9794 SI actual checksum safety enable

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Basic functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the checksum over the parameters to enable the safety functions (actual checksum).

**Dependency:** 
  
See also:
p9795

### p9795 SI reference checksum safety enable

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Basic functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0000 hex | FFFF FFFF hex | [0] A1A1 A1A1 hex |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the checksum over the parameters for enabling the safety functions (reference
checksum).

**Dependency:** 
  
See also:
r9794

### r9796 SI actual checksum PROFIsafe addresses

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the checksum over the parameters for the PROFIsafe addresses (actual checksum).

**Dependency:** 
  
See also:
p9797

### p9797 SI reference checksum PROFIsafe addresses

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0000 hex | FFFF FFFF hex | [0] A1A1 A1A1 hex |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the checksum over the parameters for the PROFIsafe addresses (reference checksum).

**Dependency:** 
  
See also:
r9796

### r9798 SI actual checksum over the drive configuration

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Basic functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the checksum over the checksum-checked parameters to configure the drive
(actual checksum).

**Dependency:** 
  
See also:
p9799

### p9799 SI reference checksum over the configuration of the drive

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Basic functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0000 hex | FFFF FFFF hex | [0] A1A1 A1A1 hex |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the checksum over the checksum-checked parameters to configure the drive (reference
checksum).

**Dependency:** 
  
See also:
r9798

### r9828 SI actual checksum configuration of safety functions channel B

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the checksum over the checksum-checked parameters to configure safety functions
(actual checksum) channel B.

**Dependency:** 
  
See also:
p9829

### p9829 SI reference checksum configuration of safety functions chan. B

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0000 hex | FFFF FFFF hex | [0] B2B2 B2B2 hex |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the checksum over the checked parameters used to configure safety functions (reference
checksum).

**Dependency:** 
  
See also:
r9828

### r9894 SI actual checksum safety enable channel B

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the checksum over the parameters to enable the safety functions (actual checksum)
channel B.

**Dependency:** 
  
See also:
p9895

### p9895 SI reference checksum safety enable channel B

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0000 hex | FFFF FFFF hex | [0] B2B2 B2B2 hex |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the checksum over the parameters for enabling the safety functions (reference
checksum) channel B.

**Dependency:** 
  
See also:
r9894

### r9896 SI actual checksum PROFIsafe addresses channel B

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the checksum over the parameters for the PROFIsafe addresses (act checksum)
chan B.

**Dependency:** 
  
See also:
p9897

### p9897 SI reference checksum PROFIsafe addresses channel B

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0000 hex | FFFF FFFF hex | [0] B2B2 B2B2 hex |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the checksum over the parameters for the PROFIsafe addresses (reference checksum)
channel B

**Dependency:** 
  
See also:
r9896

### r9898 SI actual checksum configuration of the drive, channel B

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Basic functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the checksum over the checksum-checked parameters to configure the drive
(actual checksum) channel B.

**Dependency:** 
  
See also:
p9899

### p9899 SI reference checksum over the drive configuration, channel B

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Basic functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0000 hex | FFFF FFFF hex | [0] B2B2 B2B2 hex |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the checksum over the checksum-checked parameters to configure the drive (reference
checksum) channel B.

**Dependency:** 
  
See also:
r9898

### p10000.0 SI F-DI enable

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| - | - | [0] 0000 bin |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the enable signal for the failsafe digital inputs.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | F-DI 0 (X130/2.1, X130/2.3) | Not enabled | Enabled | - |

**Note:** 
  
- Digital inputs of F-DI that have not been enabled can be used for non-safety-related
functions.  
- Only F-DI that have been enabled are monitored in a safety-relevant way. It is not
permissible that the associated DI are used as non-safety-related functions, as they
can be subject to test pulses.

### p10002 SI F-DI changeover discrepancy time

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 1.00 [ms] | 2000.00 [ms] | [0] 500.00 [ms] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the discrepancy time for digital inputs.  
The signal states at the two associated digital inputs (F-DI) must assume the same
state within this discrepancy time.

**Note:** 
  
The time must be set longer than the SI monitoring clock cycle.

### p10017[0...2] SI digital inputs input filter

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 1.00 [ms] | 100.00 [ms] | [0] 4.00 [ms] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Setting of the input filter for the digital inputs.  
The input filter is rounded off to whole milliseconds and accepted.  
The input filter acts on the following digital inputs:  
- Failsafe digital inputs (F-DI).  
  
Example:  
Input filter = 1 ms: Fault pulses of 1 ms are filtered; only pulses longer than 2
ms are processed.  
Input filter = 3 ms: Fault pulses of 3 ms are filtered; only pulses longer than 4
ms are processed.  
The input filtering result can be read in r10051 and r10151.  
The set input filter impacts the response time of the safety function.

**Index:** 
  
[
0]:
F-DI 0  
[
1]:
Reserved  
[
2]:
Reserved

**Note:** 
  
If the self test is enabled using externally specified dark pulses (p10041 = 3) for
at least one F-DI, then p10017 must be set longer than the maximum duration of the
dark pulses + 2 ms. If the test pulses are specified using the switchable power supply
(p10041 = 1), then this means p10017 > p10018 + 2 ms.

### p10018 SI F-DI self test length dark pulses VS+

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 [ms] | 50 [ms] | [0] 0 [ms] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the dark pulse length of the switchable power supply for the self test using
specified dark pulses (p10041) of the F-DI.  
Value = 0: switchable power supply, permanently switched on.  
Value > 0: dark pulse length for the switchable power supply. The test cycle is fixed
at 5 s.

**Note:** 
  
The dark pulses of the switchable power supply are only enabled for the self test
using specified dark pulses (p10041 = 1).  
The switchable power supply is continuously switched on if another self test was set

### p10019 SI F-DI self test external dark pulses wait time

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** s | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 10 [s] | 3600 [s] | [0] 1020 [s] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the maximum wait time for the dark pulses for the F-DI self test using an externally
specified test pulses.

**Note:** 
  
This parameter is only active for F-DIs that are tested using external test pulses
(p10041[x] = 3).

### c10022 SI STO input terminal

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink binary |  |  |
| **Factory interconnection:** | **Fixed value:** |  |
| not interconnected | 1 |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Signal for the axis-specific selection of function "STO (Safe Torque Off)" (control
via F-DI).

**Note:** 
  
F-DI: Failsafe Digital Input

### c10023 SI SS1 input terminal

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink binary |  |  |
| **Factory interconnection:** | **Fixed value:** |  |
| not interconnected | 1 |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Signal for selecting function "SS1 (Safe Stop 1)".

**Note:** 
  
F-DI: Failsafe Digital Input

### p10040.0 SI F-DI input mode

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| - | - | [0] 0000 bin |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Sets the input mode for the safety digital inputs (F-DI).

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | F-DI 0, DI 3+ (X130/2.3) | NC contact | NO contact | - |

**Note:** 
  
Only an NC contact can be connected for the safety digital inputs not listed.

### p10041[0...2] SI F-DI self test mode selection

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 3 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Enable for the F-DI self test.

**Value:** 
  
0:
Self test using internal test signals  
1:
Self test using specified dark pulses (VS+)  
3:
Self test using externally specified dark pulses

**Index:** 
  
[
0]:
F-DI 0  
[
1]:
Reserved  
[
2]:
Reserved

**Note:** 
  
Mode 1:  
A check is made whether p10017 is > p10018 + 2 ms and whether p10018 is set > 0.

### c10050[0...2] SI status F-DI via PROFIsafe

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink binary |  |  |
| **Factory interconnection:** | **Fixed value:** |  |
| not interconnected | 0 |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
The state of the selected failsafe digital inputs F-DIs is transferred to the F-control
via PROFIsafe.

**Index:** 
  
[
0]:
F-DI via Profisafe status 1  
[
1]:
Reserved  
[
2]:
Reserved

**Note:** 
  
F-DI: Failsafe Digital Input

### r10051.0 SI digital inputs status channel A

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source binary/numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Display for the single-channel, logical and debounced status of the failsafe digital
inputs of channel A.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Status of DI 2+ (X130/2.1) | Logical 0 | Logical 1 | - |

**Dependency:** 
  
See also:
p10017

**Note:** 
  
The relationship between the logic level and the external voltage level at the input
is intended for the use of a safety function:  
With 24 V at the input, NC contacts have a logical "1" level, for 0 V at the input,
a logical "0" level.  
This means that an NC/NC contact parameterization for 0 V at both inputs of the F-DI
leads to a status of the F-DI equal to "0" (safety function selected), for 24 V at
both inputs of the F-DI, to a status of the F-DI equal to "1" (safety function deselected).  
F-DI: Failsafe Digital Input  
  
NC contact:  
24V at the input -> logical "1"  
0V at the input -> logical "0"

### c10060 SI SS1E input terminal

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink binary |  |  |
| **Factory interconnection:** | **Fixed value:** |  |
| not interconnected | 1 |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Signal for selecting function "SS1E (Safe Stop 1 External)".

**Note:** 
  
F-DI: Failsafe Digital Input

### r10071.0 SI F-DI status

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source binary/numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Display for the status of the failsafe digital inputs.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Status of the F-DI 0 | Logical 0 | Logical 1 | - |

**Note:** 
  
The following applies:  
- Logical "0": Safety function is selected  
- Logical "1": safety function is deselected  
F-DI: Failsafe Digital Input

### r10075.0...28 SI PROFIsafe control word

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source binary/numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Displays the control signals for safety functions integrated in the drive only via
PROFIsafe.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Deselect STO | No | Yes | - |
| 01 | Deselect SS1 | No | Yes | - |
| 02 | Deselect SS2 | No | Yes | - |
| 03 | Deselect SOS | No | Yes | - |
| 04 | Deselect SLS | No | Yes | - |
| 07 | Acknowledgment | No | Signal edge active | - |
| 08 | Deselect SLA | No | Yes | 2838 |
| 09 | Select SLS bit 0 | Not set | Set | - |
| 10 | Select SLS bit 1 | Not set | Set | - |
| 12 | Deselect SDI positive | No | Yes | 2824 |
| 13 | Deselect SDI negative | No | Yes | 2824 |
| 15 | Deselect SSM | No | Yes | - |
| 18 | Deselect SS1E | No | Yes | - |
| 28 | Deselect SS2E | No | Yes | - |

### r10076 SI PROFIsafe SLS-LIMIT

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Scaling for limit value SLS1 via PROFIsafe telegram 901.  
The value range 1 ... 32767 corresponds to 0.01 % ... 100 % of limit value SLS1.  
An invalid value results in the stop response parameterized in p9563[0].  
  
Also for scaled limit value SLS1, the SLS2, SLS3 and SLS4 limit values can be selected
using r9720.9 and r9720.10.

### r10080.0...28 SI status signals channel A

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source binary/numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Status signals (channel A) for safety-relevant motion monitoring functions integrated
in the drive.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | STO or safe pulse cancellation active | No | Yes | - |
| 01 | SS1 active | No | Yes | - |
| 02 | SS2 active | No | Yes | - |
| 03 | SOS active | No | Yes | - |
| 04 | SLS active | No | Yes | - |
| 07 | Internal event | Yes | No | - |
| 08 | SLA active | No | Yes | 2838 |
| 09 | Active SLS limit value bit 0 | Not set | Set | - |
| 10 | Active SLS limit value bit 1 | Not set | Set | - |
| 11 | SOS selected | No | Yes | - |
| 12 | SDI positive active | No | Yes | 2824 |
| 13 | SDI negative active | No | Yes | 2824 |
| 15 | SSM (speed below limit value) | No | Yes | 2823 |
| 18 | SS1E active | No | Yes | - |
| 28 | SS2E active | No | Yes | - |

**Notice:** 
  
For bit 07:  
An internal event is displayed if a stop function is active.  
The signal state behaves in an opposite way to the PROFIsafe Standard.

**Note:** 
  
Only the status signals of the available and enabled functions (see p9604) are updated.
All others are 0 across the board.

### r10098 SI actual checksum across device-specific parameters

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Basic functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the checksum over the checksum-checked parameters for the device-specific
parameters of the drive system (actual checksum).

**Dependency:** 
  
See also:
p10099

### p10099 SI reference checksum across device-specific parameters

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Basic functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0000 hex | FFFF FFFF hex | [0] A1A1 A1A1 hex |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the checksum over the checksum-checked parameters for the device-specific
parameters of the drive system (reference checksum).

**Dependency:** 
  
See also:
r10098

### r10151.0 SI digital inputs status channel B

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source binary/numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Display for the single-channel, logical and debounced status of the failsafe digital
inputs of channel B.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Status of the DI 3+ (X130/2.3) | Logical 0 | Logical 1 | - |

**Dependency:** 
  
See also:
p10017, p10040

**Note:** 
  
The relationship between the logic level and the external voltage level at the input
depends on the parameterization (see p10040) of the input as NC contact or NO contact,
and is aligned to the use of a safety function:  
With 24 V at the input, NC contacts have a logical "1" level, for 0 V at the input,
a logical "0" level.  
This means that an NC/NC contact parameterization of 0 V at both inputs of the F-DI
leads to a status of the F-DI equal to "0" (safety function selected), for 24 V at
both inputs of the F-DI, to a status of the F-DI equal to "1" (safety function deselected).  
With 24 V at the input, NO contacts have a logical "0" level, for 0 V at the input,
a logical "1" level. This means that for an NC/NO contact parameterization, the level
0 V/24 V leads to a status of the F-DI equal to "0" (safety function selected), the
level 24 V/0 V leads to status of the F-DI equal to "1" (safety function deselected).  
F-DI: Failsafe Digital Input

### r10171.0 SI F-DI status channel B

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Display for the status of the failsafe digital inputs.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Status of the F-DI 0 | Logical 0 | Logical 1 | - |

**Note:** 
  
If a safety function (e.g. via c10022) is controlled via an F-DI, then the following
applies:  
- Logical "0": Safety function is selected  
- Logical "1": safety function is deselected  
F-DI: Failsafe Digital Input

### r10175.0...28 SI PROFIsafe control word channel B

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Displays the control signals for safety-related motion monitoring functions integrated
in the drive via PROFIsafe.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Deselect STO | No | Yes | - |
| 01 | Deselect SS1 | No | Yes | - |
| 02 | Deselect SS2 | No | Yes | - |
| 03 | Deselect SOS | No | Yes | - |
| 04 | Deselect SLS | No | Yes | - |
| 07 | Acknowledgment | No | Signal edge active | - |
| 08 | Deselect SLA | No | Yes | 2838 |
| 09 | Select SLS bit 0 | Not set | Set | - |
| 10 | Select SLS bit 1 | Not set | Set | - |
| 12 | Deselect SDI positive | No | Yes | 2824 |
| 13 | Deselect SDI negative | No | Yes | 2824 |
| 15 | Deselect SSM | No | Yes | - |
| 18 | Deselect SS1E | No | Yes | - |
| 28 | Deselect SS2E | No | Yes | - |

### r10176 SI PROFIsafe S_SLS_LIMIT_A channel B

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Dynamic limit value input for SLS (Safely-Limited Speed) via PROFIsafe.

### r10180.0...28 SI status signals channel B

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source binary/numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Status signals (channel B) for safety-relevant motion monitoring functions integrated
in the drive.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | STO or safe pulse cancellation active | No | Yes | - |
| 01 | SS1 active | No | Yes | - |
| 02 | SS2 active | No | Yes | - |
| 03 | SOS active | No | Yes | - |
| 04 | SLS active | No | Yes | - |
| 07 | Internal event | Yes | No | - |
| 08 | SLA active | No | Yes | 2838 |
| 09 | Active SLS limit value bit 0 | Not set | Set | - |
| 10 | Active SLS limit value bit 1 | Not set | Set | - |
| 11 | SOS selected | No | Yes | - |
| 12 | SDI positive active | No | Yes | 2824 |
| 13 | SDI negative active | No | Yes | 2824 |
| 15 | SSM (speed below limit value) | No | Yes | 2823 |
| 18 | SS1E active | No | Yes | - |
| 28 | SS2E active | No | Yes | - |

**Notice:** 
  
For bit 07:  
An internal event is displayed if a stop function is active.  
The signal state behaves in an opposite way to the PROFIsafe Standard.

**Note:** 
  
Only the function status signals of the available and enabled functions (see p9604)
are updated. All others are 0 across the board.

### r10198 SI actual checksum across device-specific parameters channel B

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Basic functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the checksum over the checksum-checked parameters for the device-specific
parameters of the drive system (actual checksum) channel B.

**Dependency:** 
  
See also:
p10199

### p10199 SI reference checksum across device-specific parameters chan B

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Basic functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0000 hex | FFFF FFFF hex | [0] B2B2 B2B2 hex |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the checksum over the checksum-checked parameters for the device-specific
parameters of the drive system (reference checksum) channel B.

**Dependency:** 
  
See also:
r10198

### p10202[0...1] SI SBT brake selection

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 1 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Selects the brakes to be tested.  
p10202[0] must be set to 1 to test the brake.

**Value:** 
  
0:
Inhibit  
1:
Test motor holding brake

**Index:** 
  
[
0]:
Brake 1  
[
1]:
Reserved

**Dependency:** 
  
See also:
C01785

### p10208[0...1] SI SBT test torque ramp time

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 20 [ms] | 10000 [ms] | [0] 1000 [ms] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the time, during which the test torque is ramped up against the closed brake.  
The test torque is then ramped down after the safe brake test.

**Index:** 
  
[
0]:
Brake 1  
[
1]:
Reserved

**Note:** 
  
The set time is rounded internally to an integer multiple of the monitoring clock
cycle.

### p10209[0...1] SI SBT brake holding torque

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Nm | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.05 [Nm] | 60000.00 [Nm] | [0] 10.00 [Nm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the effective holding torque on the motor side of the brake to be tested.

**Index:** 
  
[
0]:
Brake 1  
[
1]:
Reserved

**Dependency:** 
  
See also:
p10210, p10220

**Note:** 
  
The test torque effective for the brake test can be set for each sequence using a
factor (p10210, p10220).

### p10210[0...1] SI SBT test torque factor sequence 1

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.30 | 1.00 | [0] 1.00 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the factor for the test torque of sequence 1 for the safe brake test.  
The factor is referred to the holding torque of the brake (p10209).

**Index:** 
  
[
0]:
Brake 1  
[
1]:
Reserved

**Dependency:** 
  
See also:
p10209, c10235

**Note:** 
  
The test sequence is selected using p10235.4.

### p10211[0...1] SI SBT test duration sequence 1

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 20 [ms] | 10000 [ms] | [0] 1000 [ms] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the test duration for sequence 1 for the safe brake test.  
The test torque is available for this time at the closed brake.

**Index:** 
  
[
0]:
Brake 1  
[
1]:
Reserved

**Dependency:** 
  
See also:
c10235

**Note:** 
  
The test sequence is selected using p10235.4.  
The set time is rounded internally to an integer multiple of the monitoring clock
cycle.

### p10212[0...1] SI SBT position tolerance sequence 1

[S210](#p1021201-si-sbt-position-tolerance-sequence-1-1)

[S210 Safety rot](#p1021201-si-sbt-position-tolerance-sequence-1-2)

#### p10212[0...1] SI SBT position tolerance sequence 1

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.001 [mm] | 360.000 [mm] | [0] 1.000 [mm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the tolerated position deviation for sequence 1 for the safe brake test.

**Index:** 
  
[
0]:
Brake 1  
[
1]:
Reserved

**Note:** 
  
The test sequence is selected using p10235.4.

#### p10212[0...1] SI SBT position tolerance sequence 1

|  |  |  |
| --- | --- | --- |
| **Variant:**S210 (Safety rot) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.001 [°] | 360.000 [°] | [0] 1.000 [°] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the tolerated position deviation for sequence 1 for the safe brake test.

**Index:** 
  
[
0]:
Brake 1  
[
1]:
Reserved

**Note:** 
  
The test sequence is selected using p10235.4.

### p10220[0...1] SI SBT test torque factor sequence 2

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.30 | 1.00 | [0] 1.00 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the factor for the test torque of sequence 2 for the safe brake test.  
The factor is referred to the holding torque of the brake (p10209).

**Index:** 
  
[
0]:
Brake 1  
[
1]:
Reserved

**Dependency:** 
  
See also:
p10209, c10235

**Note:** 
  
The test sequence is selected using p10235.4.

### p10221[0...1] SI SBT test duration sequence 2

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 20 [ms] | 10000 [ms] | [0] 1000 [ms] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the test duration for sequence 2 for the safe brake test.  
The test torque is available for this time at the closed brake.

**Index:** 
  
[
0]:
Brake 1  
[
1]:
Reserved

**Dependency:** 
  
See also:
c10235

**Note:** 
  
The test sequence is selected using p10235.4.  
The set time is rounded internally to an integer multiple of the monitoring clock
cycle.

### p10222[0...1] SI SBT position tolerance sequence 2

[S210](#p1022201-si-sbt-position-tolerance-sequence-2-1)

[S210 Safety rot](#p1022201-si-sbt-position-tolerance-sequence-2-2)

#### p10222[0...1] SI SBT position tolerance sequence 2

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.001 [mm] | 360.000 [mm] | [0] 1.000 [mm] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the tolerated position deviation for sequence 2 for the safe brake test.

**Index:** 
  
[
0]:
Brake 1  
[
1]:
Reserved

**Dependency:** 
  
See also:
c10235

**Note:** 
  
The test sequence is selected using p10235.4.

#### p10222[0...1] SI SBT position tolerance sequence 2

|  |  |  |
| --- | --- | --- |
| **Variant:**S210 (Safety rot) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit Safety Integrated application |  |  |
| **Can be changed in the operating state:**Commissioning (Safety Integrated) |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ° | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0.001 [°] | 360.000 [°] | [0] 1.000 [°] |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Sets the tolerated position deviation for sequence 2 for the safe brake test.

**Index:** 
  
[
0]:
Brake 1  
[
1]:
Reserved

**Dependency:** 
  
See also:
c10235

**Note:** 
  
The test sequence is selected using p10235.4.

### r10231.0...4 SI SBT control word diagnostics

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Displays the diagnostic bits for the control word of the safe brake test

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Select brake test | No | Yes | - |
| 01 | Start brake test | No | Yes | - |
| 03 | Select test torque sign | Positive | Negative | - |
| 04 | Select test sequence | Test sequence 1 | Test sequence 2 | - |

### r10234.0...15 SI Safety Information Channel status word S_ZSW3B

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source binary/numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Display for status word S_ZSW3B of the Safety Info Channel.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Brake test selected | No | Yes | - |
| 01 | Setpoint input drive/external | External | Drive | - |
| 02 | Active brake | Brake 1 | Brake 2 | - |
| 03 | Brake test active | No | Yes | - |
| 04 | Brake test result | Erroneous/not | Successful | - |
| 05 | Brake test completed | No | Yes | - |
| 07 | Actual load sign | Positive | Negative | - |
| 11 | SS2E active | No | Yes | - |
| 15 | Acceptance test mode selected | No | Yes | - |

**Note:** 
  
For bits 05, 04:  
A combination of bit 04 and bit 05 indicates whether a brake test returned an error
or has still not been performed.  
Bit 05/04 = 0/0: The brake test has still not been performed since the last restart.  
Bit 05/04 = 1/0: The last brake test that was executed failed (error)  
For bit 07:  
Sign for the static hanging/suspended load at the motor axis; the bit can fluctuate
if the axis has no connected load.  
  
SIC: Safety Information Channel  
SLP: Safely-Limited Position / SE: Safe software limit switches  
SS2E: Safe Stop 2 External (Safe Stop 2 with external stop)  
SS2ESR: Safe Stop 2 Extended Stop and Retract

### c10235 SI Safety Control Channel control word S_STW3B

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink numeric |  | **Scaling:** - |
| **Factory interconnection:** | **Fixed value:** |  |
| not interconnected | 0 |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Signal for control word S_STW3B of the Safety Control Channel.

**Dependency:** 
  
This parameter is used as control word for the safe brake test.

**Note:** 
  
SBT: Safe Brake Test  
SCC: Safety Control Channel

### r10240 SI Motion SBT test torque diagnostics

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Nm | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Displays the effective maximum test torque on the motor side for a safe brake test.

**Dependency:** 
  
See also:
p10210, p10220

**Note:** 
  
The value remains displayed until the start of the next test sequence.

### r10241 SI Motion SBT load torque diagnostics

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** Nm | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Displays the load torque for a safe brake test.  
When initializing the brake test, this load torque is available at the drive.

**Note:** 
  
The value remains displayed until the brake test is deselected.

### r10242 SI Motion SBT state diagnostics

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer16 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Displays the actual state of the safe brake test.

**Value:** 
  
0:
Brake test inactive, wait for SBT selection  
1:
Setpoint input drive  
2:
Determining the load  
3:
Brake test is initialized, wait for start of test sequence  
4:
Start test sequence  
5:
Closing the brake, establishing the test torque  
6:
Brake test active, wait for test duration sequence  
7:
Reduce test torque  
8:
Wait for the brake to open  
9:
Brake test successfully completed, wait for start deselection  
10:
Change to brake test initialized - fault acknowledgment  
11:
Brake test canceled, torque is reduced  
12:
Brake test canceled, wait for brake to open  
13:
Brake test ended with error, wait for acknowledgment  
14:
Brake opening timer elapsed  
15:
Error when initializing the brake test, wait for acknowledgment  
16:
Change to brake test inactive, acknowledgment active

### c10250 SI Safety Control Channel control word S_STW1B

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**- |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Sink numeric |  | **Scaling:** - |
| **Factory interconnection:** | **Fixed value:** |  |
| not interconnected | 0 |  |
| **Min:** | **Max:** | **Factory setting:** |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Signal for control word S_STW1B of the Safety Control Channel.

**Dependency:** 
  
See also:
r10251

**Note:** 
  
SCC: Safety Control Channel

### r10251.13 SI Safety Control Channel control word S_STW1B diagnostics

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source binary/numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Display for the diagnostics of control word S_STW1B of the Safety Control Channel.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 13 | Close brake from control | Not selected | Selected | - |

**Dependency:** 
  
See also:
c10250

### r10352.0...17 SI STO select cause

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source binary/numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Reason that STO (Safe Torque Off) function was selected.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Selection via F-DI | Low | High | - |
| 01 | Selection via PROFIsafe | Low | High | - |
| 04 | Safety commissioning mode active | Low | High | - |
| 05 | Axis parking active / missing actual value | Low | High | - |
| 07 | Response to SS1 | Low | High | - |
| 08 | Response to SS1E | Low | High | - |
| 09 | Response to SS2 | Low | High | - |
| 10 | Response to SS2E | Low | High | - |
| 12 | Stop response | Low | High | - |
| 14 | Response to parameterizing error | Low | High | - |
| 15 | Response to internal software error | Low | High | - |
| 17 | No communication via PROFIsafe | Low | High | - |

### r10353.0...17 SI SS1 select cause

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source binary/numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Reason for the selection of function SS1 (Safe Stop 1).

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Selection via F-DI | Low | High | - |
| 01 | Selection via PROFIsafe | Low | High | - |
| 12 | Stop response | Low | High | - |
| 13 | Selection when transitioning to following function | Low | High | - |
| 17 | No communication via PROFIsafe | Low | High | - |

### r10354.0...13 SI SS2 selection cause

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source binary/numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Reason for the selection of function SS2 (Safe Stop 2).

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Selection via F-DI | Low | High | - |
| 01 | Selection via PROFIsafe | Low | High | - |
| 12 | Stop response | Low | High | - |
| 13 | Selection when transitioning to following function | Low | High | - |

### r10355.0...10 SI SOS selection cause

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source binary/numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Reason for the selection of function SOS (Safe Operating Stop).

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Selection via F-DI | Low | High | - |
| 01 | Selection via PROFIsafe | Low | High | - |
| 09 | Response to SS2 | Low | High | - |
| 10 | Response to SS2E | Low | High | - |

### r10356.0...1 SI SLS select cause

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source binary/numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Reason for the selection of function SLS (Safely-Limited Speed).

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Selection via F-DI | Low | High | - |
| 01 | Selection via PROFIsafe | Low | High | - |

### r10360.0...1 SI SDI positive select cause

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source binary/numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Reason for the selection of SDI (Safe Direction) positive.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Selection via F-DI | Low | High | - |
| 01 | Selection via PROFIsafe | Low | High | - |

### r10361.0...1 SI SDI negative select cause

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source binary/numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Reason for the selection of SDI (Safe Direction) negative.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Selection via F-DI | Low | High | - |
| 01 | Selection via PROFIsafe | Low | High | - |

### r10365.0...1 SI SSM select cause

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source binary/numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Reason for the selection of function SSM (Safe Speed Monitor).

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Selection via F-DI | Low | High | - |
| 01 | Selection via PROFIsafe | Low | High | - |

### r10366.0...1 SI SLA selection cause

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source binary/numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Displays the reason for the selection of SI function SLA.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Selection via F-DI | Low | High | - |
| 01 | Selection via PROFIsafe | Low | High | - |

### r10369.6 SI SBC selection cause

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source binary/numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Reason for the selection of function SBC (Safe Brake Control)

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 06 | Response to STO | Low | High | - |

### r10370.0...13 SI SS1E selection cause

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source binary/numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Reason for the selection of function SS1E (Safe Stop 1 External).

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Selection via F-DI | Low | High | - |
| 01 | Selection via PROFIsafe | Low | High | - |
| 12 | Stop response | Low | High | - |
| 13 | Selection when transitioning to following function | Low | High | - |

### r10372.0...13 SI SS2E select cause

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Type of signal interconnection:** Source binary/numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Reason for the selection of function SS2E (Safe Stop 2 External).

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Selection via F-DI | Low | High | - |
| 01 | Selection via PROFIsafe | Low | High | - |
| 12 | Stop response | Low | High | - |
| 13 | Selection when transitioning to following function | Low | High | - |

### r10452.0...17 SI STO select cause channel B

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Reason for the selection of function STO (Safe Torque Off) on channel B.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Selection via F-DI | Low | High | - |
| 01 | Selection via PROFIsafe | Low | High | - |
| 04 | Safety commissioning mode active | Low | High | - |
| 05 | Axis parking active / missing actual value | Low | High | - |
| 07 | Response to SS1 | Low | High | - |
| 08 | Response to SS1E | Low | High | - |
| 09 | Response to SS2 | Low | High | - |
| 10 | Response to SS2E | Low | High | - |
| 12 | Stop response | Low | High | - |
| 14 | Response to parameterizing error | Low | High | - |
| 15 | Response to internal software error | Low | High | - |
| 17 | No communication via PROFIsafe | Low | High | - |

### r10453.0...17 SI SS1 select cause channel B

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Reason for the selection of function SS1 (Safe Stop 1) on channel B.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Selection via F-DI | Low | High | - |
| 01 | Selection via PROFIsafe | Low | High | - |
| 12 | Stop response | Low | High | - |
| 13 | Selection when transitioning to following function | Low | High | - |
| 17 | No communication via PROFIsafe | Low | High | - |

### r10454.0...13 SI SS2 selection cause channel B

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Reason for the selection of function SS2 (Safe Stop 2) on channel B.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Selection via F-DI | Low | High | - |
| 01 | Selection via PROFIsafe | Low | High | - |
| 12 | Stop response | Low | High | - |
| 13 | Selection when transitioning to following function | Low | High | - |

### r10455.0...10 SI SOS select cause channel B

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Reason for the selection of function SOS (Safe Operating Stop) on channel B.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Selection via F-DI | Low | High | - |
| 01 | Selection via PROFIsafe | Low | High | - |
| 09 | Response to SS2 | Low | High | - |
| 10 | Response to SS2E | Low | High | - |

### r10456.0...1 SI SLS select cause channel B

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Reason for the selection of function SLS (Safely-Limited Speed) on channel B.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Selection via F-DI | Low | High | - |
| 01 | Selection via PROFIsafe | Low | High | - |

### r10460.0...1 SI SDI positive select cause channel B

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Reason for the selection of SDI (Safe Direction) positive on channel B.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Selection via F-DI | Low | High | - |
| 01 | Selection via PROFIsafe | Low | High | - |

### r10461.0...1 SI SDI negative select cause channel B

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Reason for the selection of SDI (Safe Direction) negative on channel B.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Selection via F-DI | Low | High | - |
| 01 | Selection via PROFIsafe | Low | High | - |

### r10465.0...1 SI SSM select cause channel B

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Reason for the selection of function SSM (Safe Speed Monitor) on channel B.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Selection via F-DI | Low | High | - |
| 01 | Selection via PROFIsafe | Low | High | - |

### r10466.0...1 SI SLA select cause channel B

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Reason for the selection of function SLA on channel B.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Selection via F-DI | Low | High | - |
| 01 | Selection via PROFIsafe | Low | High | - |

### r10469.6 SI SBC selection cause channel B

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Reason for the selection of function SBC (Safe Brake Control) on Channel B.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 06 | Response to STO | Low | High | - |

### r10470.0...13 SI SS1E select cause channel B

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Reason for the selection of function SS1E (Safe Stop 1 External) on channel B.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Selection via F-DI | Low | High | - |
| 01 | Selection via PROFIsafe | Low | High | - |
| 12 | Stop response | Low | High | - |
| 13 | Selection when transitioning to following function | Low | High | - |

### r10472.0...13 SI SS2E select cause channel B

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Safety Integrated |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Reason for the selection of function SS2E (Safe Stop 2 External) on channel B.

**Bit array:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Selection via F-DI | Low | High | - |
| 01 | Selection via PROFIsafe | Low | High | - |
| 12 | Stop response | Low | High | - |
| 13 | Selection when transitioning to following function | Low | High | - |

### c11500[0...3] LR initiate absolute encoder adjustment

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
Encoder 2  
[
3]:
Encoder 3

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
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Ready for operation |  |  |
| **Parameter group:** Homing |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 1 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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

[S210](#c11560-epos-direct-setpoint-inputmdi-acceleration-setpoint-1)

[S210 EPOS load side, rotating](#c11560-epos-direct-setpoint-inputmdi-acceleration-setpoint-2)

#### c11560 EPOS direct setpoint input/MDI acceleration setpoint

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Variant:**S210 (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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

[S210](#c11561-epos-direct-setpoint-inputmdi-deceleration-setpoint-1)

[S210 EPOS load side, rotating](#c11561-epos-direct-setpoint-inputmdi-deceleration-setpoint-2)

#### c11561 EPOS direct setpoint input/MDI deceleration setpoint

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Variant:**S210 (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
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
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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

[S210](#r11570-epos-actual-acceleration-1)

[S210 EPOS load side, rotating](#r11570-epos-actual-acceleration-2)

#### r11570 EPOS actual acceleration

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Jog, Traversing blocks, Direct setpoint input (MDI) |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm/s² | **Unit group:** 12_3 | **Unit selection:** p2498 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Variant:**S210 (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Jog, Traversing blocks, Direct setpoint input (MDI) |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** °/s² | **Unit group:** 12_4 | **Unit selection:** p2498 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Displays the acceleration value currently being processed.

**Dependency:** 
  
See also:
p2572

**Note:** 
  
The maximum acceleration from p2572 is effective in operating mode "Jog" and "Active
homing".

### r11571 EPOS actual deceleration

[S210](#r11571-epos-actual-deceleration-1)

[S210 EPOS load side, rotating](#r11571-epos-actual-deceleration-2)

#### r11571 EPOS actual deceleration

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Jog, Traversing blocks, Direct setpoint input (MDI) |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** mm/s² | **Unit group:** 12_3 | **Unit selection:** p2498 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

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
| **Variant:**S210 (EPOS load side, rotating) |  |  |
| **Data type:**FloatingPoint32 | **Visible in:**Standard display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Jog, Traversing blocks, Direct setpoint input (MDI) |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** °/s² | **Unit group:** 12_4 | **Unit selection:** p2498 |
| **Type of signal interconnection:** Source numeric |  | **Scaling:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.03.014

**Description:** 
  
Displays the deceleration value currently being processed.

**Dependency:** 
  
See also:
p2573

**Note:** 
  
The maximum deceleration from p2573 is effective in operating mode "Jog" and "Active
homing".

## SINAMICS Parameter S210 60000 - 61001

SINAMICS Parameter S210 60000 - 61001

### r60000 PROFIdrive reference speed

|  |  |  |
| --- | --- | --- |
| **Data type:**FloatingPoint32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** CALC_MOD_ALL |
| **Unit:** rpm | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

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

### r60022 PROFIsafe telegram

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Safety Integrated, Configuration |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the PROFIsafe telegram.

**Value:** 
  
0:
No PROFIsafe telegram selected  
30:
PROFIsafe standard telegram 30, PZD-1/1  
901:
PROFIsafe SIEMENS telegram 901, PZD-3/5

**Dependency:** 
  
See also:
p9611

**Note:** 
  
When reading the parameter via PROFIdrive, value 65534 is applicable for "No PROFIsafe
telegram".

### r60044 SI message buffer counter changes

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the changes of the safety message buffer.  
This counter is incremented every time that the safety message buffer changes.

**Recommendation:** 
  
This is used to check whether the safety message buffer has been read out consistently.

**Dependency:** 
  
See also:
r9753, r9754, r9755, r9756, r60045, r60048, r60049, p60052

### r60045[0...63] SI message code

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the numbers of safety messages that have occurred.

**Dependency:** 
  
See also:
r9753, r9754, r9755, r9756, r60044, r60048, r60049, p60052

**Note:** 
  
The messages type "safety message" (Cxxxxx) are entered in the message fault buffer.  
Message buffer structure (principle):  
r60045[0], r60048[0], r60049[0], r9753[0], r9754[0], r9755[0], r9756[0] --> safety
message 1 (oldest active message) of the actual message case.  
...  
r60045[7], r60048[7], r60049[7], r9753[7], r9754[7], r9755[7], r9756[7] --> safety
message 8 (latest active message) of the actual message case,  
  
Safety messages that have gone are automatically acknowledged.  
History of acknowledged messages:  
r60045[8], r60048[8], r60049[8], r9753[8], r9754[8], r9755[8], r9756[8] --> safety
message 1 of the 1st acknowledged message case,  
...  
r60045[16], r60048[16], r60049[16], r9753[16], r9754[16], r9755[16], r9756[16] -->
safety message 1 of the 2nd acknowledged message case,  
...  
r60045[56], r60048[56], r60049[56], r9753[56], r9754[56], r9755[56], r9756[56] -->
safety message 1 of the 7th acknowledged message case,  
...  
r60045[63], r60048[63], r60049[63], r9753[63], r9754[63], r9755[63], r9756[63] -->
safety message 8 (oldest gone message) of the 7th acknowledged message case,

### r60047[0...63] SI message number

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the numbers of safety messages that have occurred.

**Dependency:** 
  
See also:
r9753, r9754, r9755, r9756, r60044, r60048, r60049, p60052

**Note:** 
  
The messages type "safety message" (Cxxxxx) are entered in the message fault buffer.  
Message buffer structure (principle):  
r60045[0], r60048[0], r60049[0], r9753[0], r9754[0], r9755[0], r9756[0] --> safety
message 1 (oldest active message) of the actual message case.  
...  
r60045[7], r60048[7], r60049[7], r9753[7], r9754[7], r9755[7], r9756[7] --> safety
message 8 (latest active message) of the actual message case,  
  
Safety messages that have gone are automatically acknowledged.  
History of acknowledged messages:  
r60045[8], r60048[8], r60049[8], r9753[8], r9754[8], r9755[8], r9756[8] --> safety
message 1 of the 1st acknowledged message case,  
...  
r60045[16], r60048[16], r60049[16], r9753[16], r9754[16], r9755[16], r9756[16] -->
safety message 1 of the 2nd acknowledged message case,  
...  
r60045[56], r60048[56], r60049[56], r9753[56], r9754[56], r9755[56], r9756[56] -->
safety message 1 of the 7th acknowledged message case,  
...  
r60045[63], r60048[63], r60049[63], r9753[63], r9754[63], r9755[63], r9756[63] -->
safety message 8 (oldest gone message) of the 7th acknowledged message case,

### r60048[0...63] SI message time received in milliseconds

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** ms | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the relative system runtime in milliseconds when the safety message occurred.

**Dependency:** 
  
See also:
r9753, r9754, r9755, r9756, r60044, r60045, r60049, p60052

### r60049[0...63] SI message value

|  |  |  |
| --- | --- | --- |
| **Data type:**Integer32 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the additional information about the safety message that occurred (as integer
number).

**Dependency:** 
  
See also:
r9753, r9754, r9755, r9756, r60044, r60045, r60048, p60052

### p60052 SI message cases counter

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Can be changed in the operating state:**Operation |  |  |
| **Parameter group:** Extended functions |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Min:** | **Max:** | **Factory setting:** |
| 0 | 65535 | [0] 0 |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Number of safety message cases that have occurred since the last reset.

**Dependency:** 
  
The safety message buffer is cleared by resetting the parameter to 0.  
See also:
r9753, r9754, r9755, r9756, r60044, r60045, r60048, r60049

### r60100[0...4] PROFIdrive telegram display total

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Configuration |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the send and receive telegrams.

**Index:** 
  
[
0]:
Subslot 1: MAP  
[
1]:
Subslot 2: PROFIsafe  
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
r0922, r60022, r60122

**Note:** 
  
Value = 65534: No telegram  
Value = 65535: MAP "Module Access Point"

### r60122 PROFIdrive SIC/SCC telegram

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned16 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Safety Integrated, Configuration |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays the telegram for the Safety Information Channel (SIC) / Safety Control Channel
(SCC).

**Value:** 
  
700:
Supplementary telegram 700, PZD-0/3  
701:
Supplementary telegram 701, PZD-2/5  
32766:
No telegram

**Note:** 
  
When reading the parameter via PROFIdrive, value 65534 is applicable for "No telegram".

### r61000[0...239] PROFINET Name of Station

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Configuration |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays PROFINET Name of Station.

### r61001[0...3] PROFINET IP of Station

|  |  |  |
| --- | --- | --- |
| **Data type:**Unsigned8 | **Visible in:**Extended display |  |
| **Read permission:** Read drive data or acknowledge messages |  |  |
| **Write permission:** Edit device configuration or drive applications |  |  |
| **Parameter group:** Configuration |  |  |
| **Not relevant for motor type:**- |  |  |
| **Dyn. index [0…n]:** - |  | **Calculated:** - |
| **Unit:** - | **Unit group:** - | **Unit selection:** - |
| **Version:**603013000 |  |  |
| [Alarms](SINAMICS%20Alarms%20S210.md#sinamics-alarms-s210) |  |  |

**Valid as of version:**
  
06.01.122

**Description:** 
  
Displays PROFINET IP of Station.

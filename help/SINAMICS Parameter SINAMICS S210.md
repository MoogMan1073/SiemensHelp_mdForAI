---
title: "SINAMICS Parameter SINAMICS S210"
package: sdrpa400enUS
topics: 563
source: Siemens TIA Portal Information System (offline help, en-US)
---


# SINAMICS Parameter SINAMICS S210

This section contains the parameter descriptions for the devices listed below. The parameter descriptions for the various devices can differ. If this is the case, then in the topic under "Object", the Control Unit is listed for which the description applies. In the table of contents, you will then see a separate entry for each parameter number. The following Control Units are taken into account in the online help:

- SINAMICS S210

## SINAMICS Parameter SINAMICS S210 00002 - 02111

SINAMICS Parameter SINAMICS S210 00002 - 02111

### r0002 Operating display

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**- | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 250 | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Operating display for the drive.

**Value:**
  
0:
Operation - everything enabled  
10:
Operation - set "enable setpoint" = "1"  
11:
Operation - set "Enable speed controller" = "1"  
12:
Operation - RFG frozen, set "RFG start" = "1"  
13:
Operation - set "enable RFG" = "1"  
14:
Operation - speed setpoint not enabled  
15:
Operation - open brake (p1215)  
16:
Operation - withdraw braking with OFF1 using "ON/OFF1" = "1"  
17:
Operation - braking with OFF3 can only be interrupted with OFF2  
18:
Operation - brake on fault, remove fault, acknowledge  
21:
Ready for operation - set "Enable operation" = "1"  
31:
Ready for switching on - set "ON/OFF1" = "0/1"  
41:
Switching on inhibited - set "ON/OFF1" = "0"  
42:
Switching on inhibited - set "OC/OFF2" = "1"  
43:
Switching on inhibited - set "OC/OFF3" = "1"  
44:
Switching on inhibited - supply STO terminal w/ 24 V (hardware)  
45:
Switching on inhibited - rectify fault, acknowledge fault, STO  
46:
Switching on inhibited - exit commissioning mode (p0009, p0010)  
60:
Drive deactivated/not operational  
70:
Initialization  
200:
Wait for booting/partial booting  
250:
Device signals a topology error

**Dependency:**
  
  
Refer to:
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
COMM: Commissioning  
MotID: Motor data identification  
SS2: Safe Stop 2  
STO: Safe Torque Off

### p0009 Drive commissioning parameter filter 1

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C1( ) T | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**All groups | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 30 | [ 0 ] 1 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Setting parameter filter 1 to commission the drive.

**Value:**
  
0:
Ready  
1:
Device configuration  
30:
Parameter reset

**Note:**
  
The drive can only be switched on when in the "Ready" state (p0009 = 0).

### p0010 Drive commissioning parameter filter 2

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 1) T | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 2800, 2818 |
| **Object:**S210 | **P-Group:**All groups | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 95 | [ 0 ] 1 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Setting parameter filter 2 for commissioning the drive.

**Value:**
  
0:
Ready  
1:
Only Siemens internal  
3:
Motor commissioning  
95:
Safety Integrated commissioning

**Notice:**
  
For p0010 = 95:  
The safety commissioning Wizard must be carried out in the web server after changing
safety parameters. These changes become effective after carry out all of the commissioning
steps of the wizards.

**Note:**
  
The drive can only be switched on when in the "Ready" state (p0010 = 0).

### r0020 Speed setpoint smoothed

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**2 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 5020, 6799 |
| **Object:**S210 | **P-Group:**Displays, signals | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**p2000 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [rpm] | - [rpm] | [ ] - [rpm] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the smoothed speed setpoint at the speed controller input.

### r0021 Actual speed smoothed

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**2 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 4700, 4710 |
| **Object:**S210 | **P-Group:**Displays, signals | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**p2000 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [rpm] | - [rpm] | [ ] - [rpm] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the smoothed actual value of the motor speed.

**Dependency:**
  
  
Refer to:
r0063

### r0026 DC link voltage smoothed

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**2 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 5730, 8750, 8850, 8950 |
| **Object:**S210 | **P-Group:**Displays, signals | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**p2001 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [V] | - [V] | [ ] - [V] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the smoothed actual value of the DC link voltage.

**Dependency:**
  
  
Refer to:
r0070

### r0027 Absolute actual current smoothed

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**2 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 5730, 6799, 8850, 8950 |
| **Object:**S210 | **P-Group:**Displays, signals | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**p2002 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [Arms] | - [Arms] | [ ] - [Arms] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the smoothed absolute current actual value.

**Dependency:**
  
  
Refer to:
r0068

### r0031 Actual torque smoothed

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**2 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 5730, 6799 |
| **Object:**S210 | **P-Group:**Displays, signals | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**p2003 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [Nm] | - [Nm] | [ ] - [Nm] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the smoothed torque actual value.

**Dependency:**
  
  
Refer to:
r0080

### r0032 Active power actual value smoothed

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**2 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 5730, 6799, 8750, 8850, 8950 |
| **Object:**S210 | **P-Group:**Displays, signals | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**r2004 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [kW] | - [kW] | [ ] - [kW] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Display for the smoothed actual value of the active power.

**Dependency:**
  
  
Refer to:
r0082

### r0034 Motor utilization thermal

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**2 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Displays, signals | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**ASM, SESM, REL | **Scaling:**PERCENT | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [%] | - [%] | [ ] - [%] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the thermal motor utilization taking into account the ambient temperature
set in p0613.

**Dependency:**
  
  
Refer to:
p0613  
Refer to:
F07011, A07012

**Notice:**
  
After the drive is switched on, the system starts to determine the motor temperature
with an assumed model value. This means that the value for the motor utilization is
only valid after a stabilization time.

### r0037[0...20] Drive temperatures

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Displays, signals | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**p2006 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [°C] | - [°C] | [ ] - [°C] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

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
Reserved  
[
3]:
Reserved  
[
4]:
Interior of power unit  
[
5]:
Inverter 1  
[
6...12]:
Reserved  
[
13]:
Depletion layer 1  
[
14...20]:
Reserved

**Note:**
  
The value of -200 indicates that there is no measuring signal.  
For index [0]:  
Maximum value of the inverter temperatures (r0037[5...10]).  
For index [1]:  
Maximum value of the depletion layer temperatures (r0037[13...18]).  
The maximum value is the temperature of the hottest inverter or depletion layer.  
In the case of a fault, the particular shutdown threshold depends on the power unit,
and cannot be read out.

### r0039[0...2] Energy display

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**2 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Displays, signals | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [kWh] | - [kWh] | [ ] - [kWh] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

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
| **Can be changed:**- | **Calculated:**- | **Access level:**2 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Displays, signals | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**PERCENT | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [%] | - [%] | [ ] - [%] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
9.5

**Description:**
  
Displays the thermal converter utilization as a percentage.  
With this value, various thermal monitoring functions are taken into account.

**Dependency:**
  
  
Refer to:
r0034

**Note:**
  
The thermal motor utilization is displayed in parameter r0034.

### r0046.0...30 Missing enable signal

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 2634 |
| **Object:**S210 | **P-Group:**Displays, signals | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.2

**Description:**
  
Displays the missing enable signals.  
All enable signals are required to operate the drive. The enable signals are set by
the control.

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | OFF1 enable missing | No | Yes | 7954 |
| 01 | OFF2 enable missing | No | Yes | - |
| 02 | OFF3 enable missing | No | Yes | - |
| 03 | Operation enable missing | No | Yes | - |
| 05 | STOP2 enable missing | No | Yes | - |
| 08 | Safety enable missing | No | Yes | - |
| 10 | Ramp-function generator enable missing | No | Yes | - |
| 11 | Ramp-function generator start missing | No | Yes | - |
| 12 | Setpoint enable missing | No | Yes | - |
| 16 | OFF1 enable internal missing | No | Yes | - |
| 17 | OFF2 enable internal missing | No | Yes | - |
| 18 | OFF3 enable internal missing | No | Yes | - |
| 19 | Pulse enable internal missing | No | Yes | - |
| 21 | STOP2 enable internal missing | No | Yes | - |
| 26 | Drive inactive or not operational | No | Yes | - |
| 28 | Brake open missing | No | Yes | - |
| 30 | Speed controller inhibited | No | Yes | - |

**Dependency:**
  
  
Refer to:
r0002

**Note:**
  
The value r0046 = 0 indicates that all enable signals for this drive are present.  
Bit 00 = 1 (enable signal missing), if:  
- the signal source in p0840 is a 0 signal.  
- there is a "switching on inhibited".  
Bit 01 = 1 (enable signal missing), if:  
- the signal source in p0844 or p0845 is a 0 signal.  
Bit 02 = 1 (enable signal missing), if:  
- the signal source in p0848 or p0849 is a 0 signal.  
Bit 03 = 1 (enable signal missing), if:  
- the signal source in p0852 is a 0 signal.  
Bit 04 =1 (armature short-circuit active), if:  
- the signal source in p1230 has a 1 signal  
Bit 05, Bit 06: Being prepared  
Bit 08 = 1 (enable signal missing), if:  
- safety functions have been enabled and STO is active.  
- a safety-relevant message with STO as response is active.  
STO enabled via terminals:  
- pulse enable via the STO terminals has a 0 signal.  
STO enabled via PROFIsafe:  
- STO is selected via PROFIsafe.  
Bit 09 = 1 (enable signal missing), if:  
- the signal source in p0864 is a 0 signal.  
Bit 10 = 1 (enable signal missing), if:  
- the signal source in p1140 is a 0 signal.  
Bit 11 = 1 (enable signal missing) if the speed setpoint is frozen, because:  
- the signal source in p1141 is a 0 signal.  
- the speed setpoint is entered from jogging and the two signal sources for jogging,
bit 0 (p1055) and bit 1 (p1056) have a 1 signal.  
Bit 12 = 1 (enable signal missing), if:  
- the signal source in p1142 is a 0 signal.  
Bit 16 = 1 (enable signal missing), if:  
- there is an OFF1 fault response. The system is only enabled if the fault is removed
and was acknowledged and the "switching on inhibited" withdrawn with OFF1 = 0.  
Bit 17 = 1 (enable signal missing), if:  
- commissioning mode is selected (p0009 &gt; 0 or p0010 &gt; 0).  
- there is an OFF2 fault response.  
- the drive is inactive (p0105 = 0) or is not operational (r7850[DO-Index]=0).  
Bit 18 = 1 (enable signal missing), if:  
- OFF3 has still not been completed or an OFF3 fault response is present.  
Bit 19 = 1 (internal pulse enable missing), if:  
- synchronization is running between the basic clock cycle, DRIVE-CLiQ clock cycle
and application clock cycle.  
Bit 20 =1 (internal armature short-circuit active), if:  
- The drive is not in state "S4: operation" or "S5x".  
- the internal pulse enable is missing (r0046.19 = 0).  
Bit 21 = 1 (enable signal missing), if:  
The pulses have been enabled and the speed setpoint has still not been enabled, because:  
- the holding brake opening time (p1216) has still not expired.  
- the motor has still not been magnetized (induction motor).  
- the encoder has not been calibrated (U/f vector and synchronous motor)  
Bit 22: Being prepared  
Bit 26 = 1 (enable signal missing), if:  
- the drive is inactive (p0105 = 0) or is not operational (r7850[DO-Index]=0).  
- the drive device is in the "PROFIenergy energy-saving mode" (r5600, CU-specific).  
Bit 27 = 1 (enable signal missing), if:  
- de-magnetizing has still not been completed (only for vector).  
Bit 28 = 1 (enable signal missing), if:  
- the holding brake is closed or has still not been opened.  
Bit 29: being prepared  
Bit 30 = 1 (speed controller inhibited), if one of the following reasons is present:  
- a 0 signal is available via binector input p0856.  
- the function generator with current input is active.  
- the measuring function "current controller reference frequency characteristic" is
active.  
- the pole position identification is active.  
- motor data identification is active (only certain steps).  
Bit 31 = 1 (enable signal missing), if:  
- the speed setpoint from jog 1 or 2 is entered.

### r0061[0...1] Actual speed unsmoothed

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**2 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 4700, 4710, 4715 |
| **Object:**S210 | **P-Group:**Displays, signals | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**p2000 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [rpm] | - [rpm] | [ ] - [rpm] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.2

**Description:**
  
Displays the unsmoothed speed actual value sensed by the encoder.

**Index:**
  
[
0]:
Encoder 1  
[
1]:
Reserved

### r0062 Speed setpoint after the filter

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Displays, signals | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**p2000 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [rpm] | - [rpm] | [ ] - [rpm] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Display for the speed setpoint after the setpoint filters.

### r0063 Actual speed smoothed

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Displays, signals | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**p2000 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [rpm] | - [rpm] | [ ] - [rpm] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Display for the speed actual value.

**Dependency:**
  
  
Refer to:
r0021, r0061, p1441

### r0068 Absolute current actual value

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Displays, signals | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**p2002 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [Arms] | - [Arms] | [ ] - [Arms] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays actual absolute current.

**Dependency:**
  
  
Refer to:
r0027

**Notice:**
  
The value is updated with a sampling time of 1 ms.

**Note:**
  
Absolute current value = sqrt(Iq^2 + Id^2)  
The absolute current actual value is available smoothed (r0027) and unsmoothed (r0068).

### r0070 Actual DC link voltage

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Displays, signals | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**p2001 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [V] | - [V] | [ ] - [V] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Display for the measured actual value of the DC link voltage.

**Dependency:**
  
  
Refer to:
r0026

**Note:**
  
The DC link voltage is available smoothed (r0026) and unsmoothed (r0070).

### r0076 Current actual value field-generating

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Displays, signals | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**p2002 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [Arms] | - [Arms] | [ ] - [Arms] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Display for the actual value of the field-generating current Id.

### r0077 Current setpoint torque-generating

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 5700, 5714, 5722 |
| **Object:**S210 | **P-Group:**Displays, signals | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**REL | **Scaling:**p2002 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [Arms] | - [Arms] | [ ] - [Arms] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.2

**Description:**
  
Displays the torque/force-generating current setpoint.

### r0078[0...1] Current actual value torque-generating

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Displays, signals | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**p2002 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [Arms] | - [Arms] | [ ] - [Arms] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Display for the actual value of the torque-generating current Iq.

**Index:**
  
[
0]:
Unsmoothed  
[
1]:
Smoothed

### r0079[0...1] Torque setpoint total

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Displays, signals | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**REL | **Scaling:**p2003 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [Nm] | - [Nm] | [ ] - [Nm] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Display for the torque setpoint at the output of the speed controller.

**Index:**
  
[
0]:
Unsmoothed  
[
1]:
Smoothed

### r0080 Torque actual value

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Displays, signals | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**p2003 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [Nm] | - [Nm] | [ ] - [Nm] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Display for the actual torque.

**Dependency:**
  
  
Refer to:
r0031

**Note:**
  
The value is available smoothed (r0031) and unsmoothed (r0080).

### r0082[0...3] Active power actual value

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Displays, signals | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**r2004 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [kW] | - [kW] | [ ] - [kW] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the actual active power.

**Index:**
  
[
0]:
Unsmoothed  
[
1]:
Smoothed  
[
2]:
Power drawn  
[
3]:
Power drawn smoothed

**Dependency:**
  
  
Refer to:
r0032

**Note:**
  
The mechanical active power is available smoothed (r0032 with 100 ms, r0082[1] with
p0045) and unsmoothed (r0082[0]).  
For index [3]:  
Smoothing time constant = 4 ms

### r0196[0...255] Topology component status

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**- | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.2

**Description:**
  
Displays the status of the components.  
r0196[0]: group status of all components  
r0196[1]: Status of component with component number 1  
...  
r0196[255]: Status of component with component number 255

**Bit field:**

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

### p0210 Drive unit line supply voltage

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Converter | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 1 [V] | 63000 [V] | [ 0 ] 600 [V] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the drive unit supply voltage.  
The voltage between two phases should be entered as the device supply voltage.  
This setting is important for operating with voltages that are less than the voltage
range intended for the drive.

**Notice:**
  
If, in the switched-off state (pulse inhibit), the supply voltage is higher than the
entered value, the Vdc controller may be automatically deactivated in some cases to
prevent the motor from accelerating the next time the system is switched on. In this
case, an appropriate alarm A07401 is output.

**Note:**
  
Setting ranges for p0210 as a function of the rated power unit voltage:  
U_rated = 400 V:  
- p0210 = 380 ... 480 V (AC/AC), 510 ... 720 V (DC/AC)  
U_rated = 500 V:  
- p0210 = 500 ... 600 V (AC/AC), 675 ... 900 V (DC/AC)  
U_rated = 660 ... 690 V:  
- p0210 = 660 ... 690 V (AC/AC), 890 ... 1035 V (DC/AC)  
U_rated = 500 ... 690 V:  
- p0210 = 500 ... 690 V (AC/AC), 675 ... 1035 V (DC/AC)  
The precharging switch-in threshold for the DC link voltage (Vdc) is calculated from
p0210:  
Vdc_pre = p0210 * 0.82 * 1.35 (AC/AC)  
Vdc_pre = p0210 * 0.82 (DC/AC)  
The undervoltage thresholds for the DC link voltage (Vdc) are calculated from p0210
as a function of the rated power unit voltage:  
U_rated = 400 V:  
- U_min = p0210 * 0.78 (AC/AC) &gt; 330 V, p0210 * 0.60 (DC/AC) &gt; 380 V  
U_rated = 500 V:  
- U_min = p0210 * 0.76 (AC/AC) &gt; 410 V  
U_rated = 660 ... 690 V:  
- U_min = p0210 * 0.82 (AC/AC) &gt; 565 V, p0210 * 0.63 (DC/AC) &gt; 650 V  
U_rated = 500 ... 690 V:  
- U_min = p0210 * 0.82 (AC/AC) &gt; 420 V, p0210 * 0.63 (DC/AC) &gt; 480 V

### p0251[0] Power unit heat sink fan operating hours counter

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Modulation | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 [h] | 4294967295 [h] | [ 0 ] 0 [h] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
9.5

**Description:**
  
Displays the operating hours of the heat sink fan in the power unit.  
The number of hours operated can only be reset to 0 in this parameter (e.g. after
a fan has been replaced).

**Dependency:**
  
  
Refer to:
A30042

### r0302[0] motor code DRIVE-CLiQ

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**2 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Motor | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the number of the motor with DRIVE-CLiQ  
When the drive powers up, the motor code is read out the motor.  
For r0302 = 0, the motor was not identified.

### r0304[0] Rated motor voltage

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Motor | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [Vrms] | - [Vrms] | [ ] - [Vrms] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the rated motor voltage.

### r0305[0] Rated motor current

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Motor | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [Arms] | - [Arms] | [ ] - [Arms] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the rated motor current.

### r0307[0] Rated motor power

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Motor | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [kW] | - [kW] | [ ] - [kW] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the rated motor power.

### r0311[0] Rated motor speed

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Motor | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [rpm] | - [rpm] | [ ] - [rpm] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the rated motor speed.

### r0312[0] Rated motor torque

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Motor | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**ASM, SESM, REL, RESM | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [Nm] | - [Nm] | [ ] - [Nm] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the rated motor torque.

### r0316[0] Motor torque constant

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Motor | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**ASM, SESM, REL, RESM | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [Nm/A] | - [Nm/A] | [ ] - [Nm/A] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.2

**Description:**
  
Sets the torque constant of the synchronous motor.  
p0316 = 0:  
The torque constant is calculated from the motor data.  
p0316 &gt; 0:  
The selected value is used as torque constant.

**Notice:**
  
When selecting a catalog motor (p0301), this parameter is automatically pre-assigned
and is write protected. Information in p0300 should be carefully observed when removing
write protection.

**Note:**
  
This parameter is not used for induction motors (p0300 = 1xx).

### r0318[0] Motor stall current

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 8017 |
| **Object:**S210 | **P-Group:**Motor | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**ASM, SESM, REL, RESM | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [Arms] | - [Arms] | [ ] - [Arms] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the rated motor stall current.

### r0319[0] Motor stall torque

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Motor | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**ASM, SESM, REL, RESM | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [Nm] | - [Nm] | [ ] - [Nm] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the motor standstill/stall torque.

### r0322[0] Maximum motor speed

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Motor | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [rpm] | - [rpm] | [ ] - [rpm] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the maximum motor speed.

**Dependency:**
  
  
Refer to:
p1082

### r0323[0] Maximum motor current

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 5722 |
| **Object:**S210 | **P-Group:**Motor | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**ASM, SESM, RESM | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [Arms] | - [Arms] | [ ] - [Arms] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the maximum permissible motor current.

### r0338[0] Motor limit current

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**2 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Motor | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**ASM, SESM, REL, RESM | **Scaling:**- | **Expert list:**0 |
| **Min** | **Max** | **Factory setting** |
| - [Arms] | - [Arms] | [ ] - [Arms] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.2

**Description:**
  
Sets the motor limit current for synchronous motors (for a 600 V DC link voltage).  
Using this current, the maximum torque is achieved at the rated speed (voltage limit
characteristic).

**Dependency:**
  
If p0338 is changed during quick commissioning (p0010 = 1), then the maximum current
p0640 is appropriately pre-assigned. This is not the case when commissioning the motor
(p0010 = 3).

**Notice:**
  
When selecting a catalog motor (p0301), this parameter is automatically pre-assigned
and is write protected. Information in p0300 should be carefully observed when removing
write protection.

### r0341[0] Motor moment of inertia

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**CALC_MOD_ALL | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 5042, 5210, 6020, 6030, 6031 |
| **Object:**S210 | **P-Group:**Motor | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**REL | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [kgm²] | - [kgm²] | [ ] - [kgm²] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the motor moment of inertia (without load).

### r0479[0...2] Diagnostics encoder position actual value Gn_XIST1

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Encoder | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Display for the encoder actual position value Gn_XIST1 according to PROFIdrive for
diagnostics.  
The value of r0479 is updated in each DRIVE-CLiQ basic clock cycle and displayed with
sign.

**Index:**
  
[
0]:
Encoder 1  
[
1]:
Reserved  
[
2]:
Reserved

### p0488[0...2] Activate measuring probe 1

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Encoder | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 210 | [ 0 ] 210 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

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
Encoder 1  
[
1]:
Reserved  
[
2]:
Reserved

**Dependency:**
  
  
Refer to:
p0489, p0490

**Caution:**
  
In order to prevent incorrect measurement values, these parameters may not be written
during an active measurement.

**Note:**
  
DI: Digital Input  
Refer to the encoder interface for PROFIdrive.

### p0489[0...2] Activate measuring probe 2

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Encoder | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 211 | [ 0 ] 211 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

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
Encoder 1  
[
1]:
Reserved  
[
2]:
Reserved

**Dependency:**
  
  
Refer to:
p0488, p0490

**Caution:**
  
In order to prevent incorrect measurement values, these parameters may not be written
during an active measurement.

**Note:**
  
DI: Digital Input  
Refer to the encoder interface for PROFIdrive.

### p0490 Invert measuring probe

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Encoder | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0000 bin |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Setting to invert digital input 0 or 1 (probe 1, 2).

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | DI 0 (X130 / 1.2) | Not inverted | Inverted | - |
| 01 | DI 1 (X130 / 1.5) | Not inverted | Inverted | - |

**Dependency:**
  
  
Refer to:
p0488, p0489

**Note:**
  
DI: Digital Input  
The inversion has no effect on the status display of the digital inputs (r0722).

### p0494[0] Equivalent zero mark input terminal

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Encoder | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 211 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.2

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
  
  
Refer to:
p0490

**Caution:**
  
In order to prevent incorrect measurement values, these parameters may not be written
during an active measurement.

**Note:**
  
Refer to the encoder interface for PROFIdrive.

### r0550[0] Brake status

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**2 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Motor | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**SESM, REL, RESM | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 2 | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the status of the brake.  
The value of r0550 is read when the drive powers up.

**Value:**
  
0:
No data  
1:
Holding brake  
2:
High performance holding brake

**Dependency:**
  
  
Refer to:
p1215, r1216, r1217

**Note:**
  
For p0550 = 1:  
The default value for opening time/closing time applies.  
For p0550 = 2:  
A shorter opening time/closing time is realized if the drive satisfies the preconditions.

### p0613[0] Motor temperature model ambient temperature

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**2 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Motor | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**ASM, SESM, REL | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| -40 [°C] | 100 [°C] | [ 0 ] 40 [°C] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the motor ambient temperature.  
Based on this value, the motor temperature model calculates the thermal motor utilization
(r0034).

**Dependency:**
  
  
Refer to:
r0034  
Refer to:
F07011, A07012

### r0722.0...4 Digital inputs status

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Commands | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the status of the digital inputs.

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | DI 0 (X130 / 1.2) | Low | High | - |
| 01 | DI 1 (X130 / 1.5) | Low | High | - |
| 02 | DI 2 (X130 / 2.1-2) | Low | High | - |
| 03 | DI 3 (X130 / 2.3-4) | Low | High | - |
| 04 | DI 4 (X130 / 2.6) | Low | High | - |

**Dependency:**
  
  
Refer to:
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
| **Can be changed:**- | **Calculated:**- | **Access level:**2 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 2501 |
| **Object:**S210 | **P-Group:**Displays, signals | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Display for the control word of the sequence control.  
The higher-level control cyclically sends the control word to the drive.

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | ON/OFF1 | No | Yes | - |
| 01 | OC / OFF2 | No | Yes | - |
| 02 | OC / OFF3 | No | Yes | - |
| 03 | Enable operation | No | Yes | - |
| 04 | Enable ramp-function generator | No | Yes | - |
| 05 | Continue ramp-function generator | No | Yes | - |
| 06 | Enable speed setpoint | No | Yes | - |
| 07 | Command open brake | No | Yes | - |
| 08 | Jog 1 | No | Yes | 3001 |
| 09 | Jog 2 | No | Yes | 3001 |
| 10 | Master control by PLC | No | Yes | - |
| 12 | Speed controller enable | No | Yes | - |
| 14 | Command close brake | No | Yes | - |

### r0899.0...15 Status word sequence control

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**2 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 2503 |
| **Object:**S210 | **P-Group:**Displays, signals | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Display for the status word of the sequence control.  
The status word is cyclically sent from the drive to the higher-level control.

**Bit field:**

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
| 09 | Control request | No | Yes | - |
| 11 | Pulses enabled | No | Yes | - |
| 12 | Open holding brake | No | Yes | - |
| 13 | Command close holding brake | No | Yes | - |
| 14 | Pulse enable from the brake control | No | Yes | - |
| 15 | Setpoint enable from the brake control | No | Yes | - |

**Note:**
  
For bits 00, 01, 02, 04, 05, 06, 09:  
For PROFIdrive, these signals are used for status word 1.  
For bit 13:  
When the "Safe Brake Control" (SBC) is activated and selected, the brake is no longer
controlled using this signal.  
For bit 14, 15:  
These signals are only of significance when the "extended brake control" function
module is activated (r0108.14 = 1).

### r0922 PROFIdrive PZD telegram selection

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 3 | 105 | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the send and receive telegram.  
The telegram settings are taken from the higher-level control system.

**Value:**
  
3:
Standard telegram 3, PZD-5/9  
5:
Standard telegram 5, PZD-9/9  
102:
SIEMENS telegram 102, PZD-6/10  
105:
SIEMENS telegram 105, PZD-10/10

### r0924[0...1] ZSW bit pulses enabled

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 2454, 2456 |
| **Object:**S210 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

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
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 2410 |
| **Object:**S210 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 65535 | [ 0 ] 1 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the number of tolerated consecutive sign-of-life errors of the isochronous controller.  
The sign-of-life signal is normally received in PZD4 (control word 2) from the controller.

**Dependency:**
  
  
Refer to:
F01912

**Note:**
  
The sign-of-life monitoring is disabled for p0925 = 65535.

### r0930 PROFIdrive operating mode

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Setpoints | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the operating mode.  
3: Closed-loop speed controlled operation without ramp-function generator

### r0944 Fault buffer counter

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**2 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 8060 |
| **Object:**S210 | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Display for the fault buffer counter  
This counter is incremented every time that a fault occurs.

**Recommend.:**
  
This is used to check whether an additional fault has occurred while reading out the
fault buffer.

**Dependency:**
  
  
Refer to:
r0945, r0947, r0948, r0949, r2109

### r0945[0...63] Fault code

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**2 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 8050, 8060 |
| **Object:**S210 | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the numbers of faults that have occurred.

**Dependency:**
  
  
Refer to:
r0947, r0948, r0949, r2109, r2130, r2133, r2136

**Notice:**
  
The properties of the fault buffer should be taken from the corresponding product
documentation.

**Note:**
  
The buffer parameters are cyclically updated in the background.  
Drive faults are signaled using parameters r0945, r0947, r0948 and r0949.

### r0947[0...63] Fault code

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 8050, 8060 |
| **Object:**S210 | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
This parameter is identical to r0945.

### r0948[0...63] Fault received in milliseconds

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 8050, 8060 |
| **Object:**S210 | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [ms] | - [ms] | [ ] - [ms] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the system runtime in milliseconds referred to the day that the fault occurred.

**Dependency:**
  
  
Refer to:
r0945, r0947, r0949, r2109, r2130, r2133, r2136

**Notice:**
  
The time comprises r2130 (complete days) and r0948 (milliseconds, incomplete day).

### r0949[0...63] Fault value

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer32 | **Dynamic index:**- | **Func. diagram:** 8050, 8060 |
| **Object:**S210 | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays additional information about the fault that occurred (as integer number).  
The fault causes can be found under the fault values of the particular fault number.

**Dependency:**
  
  
Refer to:
r0945, r0947, r0948, r2109, r2130, r2133, r2136

**Note:**
  
The buffer parameters are cyclically updated in the background.  
The structure of the fault buffer and the assignment of the indices is shown in r0945.

### p0952 Fault cases counter

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 6700, 8060 |
| **Object:**S210 | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 65535 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Number of fault situations since the last reset.

**Dependency:**
  
The counter is reset with p0952 = 0.  
  
Refer to:
r0945, r0947, r0948, r0949, r2109, r2130, r2133, r2136

### r0964[0...6] Device identification

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**2 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the device identification.  
The drive internally comprises components, device and drive object. Both components
require their own identification parameters according to PROFIdrive

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
Number of drive objects  
[
6]:
Firmware patch/hot fix

**Dependency:**
  
  
Refer to:
r0975

**Note:**
  
Example:  
r0964[0] = 42 --&gt; SIEMENS  
r0964[1] = 5410 --&gt; SINAMICS S210 PN  
r0964[2] = 501 --&gt; first part firmware version V05.01 (second part, refer to index
6)  
r0964[3] = 2018 --&gt; year 2018  
r0964[4] = 1705 --&gt; 17th of May  
r0964[5] = 1 --&gt; 1 drive object  
r0964[6] = 100 --&gt; second part firmware version (complete version: V05.01.01.00)

### r0965 PROFIdrive profile number profile version

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the PROFIdrive profile number and profile version.  
Constant value = 032A hex.  
Byte 1: Profile number = 03 hex = PROFIdrive profile  
Byte 2: profile version = 2A hex = 42 dec = version 4.2

**Note:**
  
When the parameter is read via PROFIdrive, the Octet String 2 data type applies.

### r0975[0...10] Drive object identification

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**2 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the identification of the drive object.  
The drive internally comprises components, device and drive object. Both components
require their own identification parameters according to PROFIdrive

**Index:**
  
[
0]:
Company (Siemens = 42)  
[
1]:
Drive object type  
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
PROFIdrive drive object type class  
[
6]:
PROFIdrive drive object sub-type Class 1  
[
7]:
Drive object number  
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
  
  
Refer to:
r0964

**Note:**
  
Example:  
r0975[0] = 42 --&gt; SIEMENS  
r0975[1] = 11 --&gt; SERVO drive object type  
r0975[2] = 102 --&gt; first part, firmware version V01.02 (second part, refer to index
10)  
r0975[3] = 2003 --&gt; year 2003  
r0975[4] = 1401 --&gt; 14th of January  
r0975[5] = 1 --&gt; PROFIdrive drive object, type class  
r0975[6] = 9 --&gt; PROFIdrive drive object sub-type class 1  
r0975[7] = 2 --&gt; drive object number = 2  
r0975[8] = 0 (reserved)  
r0975[9] = 0 (reserved)  
r0975[10] = 600 --&gt; second part, firmware version (complete version: V01.02.06.00)

### p0976 Reset all parameters

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C1( 30) C2( 30) | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Factory settings | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 1 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Resets all parameters of the drive system.

**Value:**
  
0:
Inactive  
1:
Start reset of all parameters to factory setting

**Dependency:**
  
  
Refer to:
p0977

**Notice:**
  
After changing the value, it is not possible to change parameters until the operation
has been completed.

**Note:**
  
After all of the parameters have been reset to their factory setting, the system must
be commissioned for the first time again.  
Reset is realized in the non-volatile memory.  
Procedure:  
1. Set p0009 = 30 (parameter reset).  
2. Set p0976 = 1 The system is powered up again.  
p0976 is automatically set to 0 and p0009 is automatically set to 1 after this has
been carried out.

### p0977 Save all parameters

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Factory settings | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 1 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Saves all parameters of the drive system to the non-volatile memory.  
When saving, only the adjustable parameters intended to be saved are taken into account.

**Value:**
  
0:
Inactive  
1:
Save in non-volatile memory - loaded at POWER ON

**Dependency:**
  
  
Refer to:
p0976

**Notice:**
  
The drive power supply may only be switched off after data has been saved (i.e. after
data save has been started, wait until the parameter again has the value 0).  
Writing to parameters is inhibited while saving.

### r0979[0...30] PROFIdrive encoder format

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 4704 |
| **Object:**S210 | **P-Group:**Encoder | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the actual position encoder used according to PROFIdrive.

**Index:**
  
[
0]:
Header  
[
1]:
Type encoder 1  
[
2]:
Resolution encoder 1  
[
3]:
Shift factor G1_XIST1  
[
4]:
Shift factor G1_XIST2  
[
5]:
Distinguishable revolutions encoder 1  
[
6...30]:
Reserved

**Note:**
  
Information about the individual indices can be taken from the following literature:  
PROFIdrive Profile Drive Technology

### p1082[0] Maximum speed

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 1) T | **Calculated:**CALC_MOD_ALL | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 2820, 3020, 3050, 3060, 3070, 3095 |
| **Object:**S210 | **P-Group:**Setpoints | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.000 [rpm] | 210000.000 [rpm] | [ 0 ] 1500.000 [rpm] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the maximum motor speed to a value less than or equal to the maximum motor speed
(r0322).  
The set value is valid for both directions of rotation.

**Dependency:**
  
  
Refer to:
r0322

### p1083[0] Speed limit positive

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**2 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 3050, 3095 |
| **Object:**S210 | **P-Group:**Setpoints | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**p2000 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.000 [rpm] | 210000.000 [rpm] | [ 0 ] 210000.000 [rpm] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the maximum speed for the positive direction.  
The set value must be less than or equal to the maximum speed (p1082).

### p1086[0] Speed limit negative

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**2 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 3050, 3095 |
| **Object:**S210 | **P-Group:**Setpoints | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**p2000 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| -210000.000 [rpm] | 0.000 [rpm] | [ 0 ] -210000.000 [rpm] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the maximum speed for the negative direction.  
The set value must be less than or equal to the maximum speed (p1082).

### p1121[0] OFF1 ramp-down time

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 1) UT | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 3060, 3070 |
| **Object:**S210 | **P-Group:**Setpoints | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.000 [s] | 999999.000 [s] | [ 0 ] 1.000 [s] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the ramp-down time after an OFF1 command.  
The value is referred to the maximum speed (p1082).  
After an OFF1 command, within this time, the speed setpoint is ramped down from the
maximum speed (p1082) to standstill.

**Dependency:**
  
  
Refer to:
p1082

### p1135[0] OFF3 ramp-down time

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 1) UT | **Calculated:**- | **Access level:**2 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 3060, 3070 |
| **Object:**S210 | **P-Group:**Setpoints | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.000 [s] | 600.000 [s] | [ 0 ] 0.000 [s] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the ramp-down time for quick stop.  
In this time, after an OFF3, the speed setpoint is reduced from the maximum speed
(p1082) down to standstill.

**Note:**
  
This time can be exceeded if the DC link voltage reaches its maximum value.

### r1196 DSC position setpoint

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer32 | **Dynamic index:**- | **Func. diagram:** 3090 |
| **Object:**S210 | **P-Group:**Encoder | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the position setpoint of Dynamic Servo Control in fine pulses.

**Note:**
  
DSC: Dynamic Servo Control

### p1215 Motor holding brake configuration

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**2 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 2701, 2707, 2711 |
| **Object:**S210 | **P-Group:**Functions | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 2 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the configuration for the motor holding brake.  
Re value 2:  
This setting allows the motor shaft to be rotated for installation purposes.

**Value:**
  
0:
No motor holding brake available  
1:
Motor holding brake acc. to sequence control  
2:
Motor holding brake always open

**Dependency:**
  
  
Refer to:
r1216, r1217, p1226, p1227, p1228

**Caution:**
  
For the setting p1215 = 0, if a brake is used, it remains closed. If the motor moves,
this will destroy the brake.  
Setting p1215 = 2 is not permissible if the brake is used to hold loads.

### r1216 Motor holding brake opening time

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**2 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 2701, 2711 |
| **Object:**S210 | **P-Group:**Functions | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [ms] | - [ms] | [ ] - [ms] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the opening time for the motor holding brake.  
The speed setpoint is kept at 0 for this time. The speed setpoint is then enabled.

**Dependency:**
  
  
Refer to:
p1215, r1217

### r1217 Motor holding brake closing time

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**2 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 2701, 2711 |
| **Object:**S210 | **P-Group:**Functions | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [ms] | - [ms] | [ ] - [ms] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the time to close the motor holding brake.  
If the drive signals that the motor is at a standstill, if the holding brake is activated,
after the closing time has expired, the pulses are canceled. This prevents the load
from sagging, for example.

**Dependency:**
  
  
Refer to:
p1215, r1216

### p1226[0] Threshold for zero speed detection

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**2 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 2701, 2704 |
| **Object:**S210 | **P-Group:**Functions | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 [rpm] | 210000.00 [rpm] | [ 0 ] 20.00 [rpm] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the speed threshold for the standstill identification.  
The following applies when the motor holding brake is activated:  
The motor is shut down and held by the brake after the closing time for the brake
in p1217 has elapsed.  
The following applies when the motor holding brake is not activated:  
The motor is shut down and it then coasts down.

**Dependency:**
  
  
Refer to:
p1215, r1216, r1217, p1227

**Note:**
  
In order that standstill is identified, the speed threshold in p1226 must be somewhat
higher than the speed actual value noise level.

### p1227 Zero speed detection monitoring time

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**2 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 2701, 2704 |
| **Object:**S210 | **P-Group:**Functions | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.000 [s] | 300.000 [s] | [ 0 ] 4.000 [s] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the monitoring time for the standstill identification.  
When the speed setpoint falls below the speed threshold p1226 after OFF1 or OFF3,
after the monitoring time that has been set expires, the drive signals that the motor
at a standstill.

**Dependency:**
  
  
Refer to:
p1215, r1216, r1217, p1226

**Note:**
  
The monitoring is deactivated with p1227 = maximum value.

### p1228 Pulse suppression delay time

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**2 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 2701, 2704 |
| **Object:**S210 | **P-Group:**Functions | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.000 [s] | 299.000 [s] | [ 0 ] 0.000 [s] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the delay time for pulse suppression.  
When the speed actual value falls below the speed threshold p1226 after OFF1 or OFF3,
after the delay time that has been set expires, the drive signals that the motor at
a standstill.

**Dependency:**
  
  
Refer to:
p1226, p1227

### p1416[0] Speed setpoint filter 1 time constant

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 5020 |
| **Object:**S210 | **P-Group:**Closed-loop control | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**REL | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 [ms] | 5000.00 [ms] | [ 0 ] 0.00 [ms] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the time constant for the speed setpoint filter (PT1).

**Note:**
  
The speed setpoint filter is activated with a time constant greater than zero.

### r1438 Speed controller speed setpoint

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Closed-loop control | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**REL | **Scaling:**p2000 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [rpm] | - [rpm] | [ ] - [rpm] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.2

**Description:**
  
Displays the speed setpoint after setpoint limiting for the P component of the speed
controller.

### p1441[0] Actual speed smoothing time

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**CALC_MOD_CON | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 4710, 4715 |
| **Object:**S210 | **P-Group:**Closed-loop control | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**REL | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 [ms] | 50.00 [ms] | [ 0 ] 0.00 [ms] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the smoothing time constant (PT1) for the speed actual value.

**Dependency:**
  
  
Refer to:
r0063

### p1460[0] Speed controller P gain

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**CALC_MOD_CON | **Access level:**2 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 5040, 5042 |
| **Object:**S210 | **P-Group:**Closed-loop control | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**REL | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.0000 [Nms/rad] | 500000000.0000 [Nms/rad] | [ 0 ] 0.3000 [Nms/rad] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the P gain of the speed controller.  
The drive determines the P gain for One Button Tuning and writes the value to p1460.  
The value can be changed.

**Dependency:**
  
  
Refer to:
p1462

**Note:**
  
The higher the set P gain, the faster and more unstable the control.

### p1462[0] Speed controller integral time

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**CALC_MOD_CON | **Access level:**2 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 5040, 5042, 6020, 6040 |
| **Object:**S210 | **P-Group:**Closed-loop control | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**REL | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 [ms] | 100000.00 [ms] | [ 0 ] 10.00 [ms] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the integral time for the speed controller  
The drive determines the integral time for One Button Tuning - and writes the value
to p1462.

**Dependency:**
  
  
Refer to:
p1460

**Note:**
  
The shorter the integral time, the faster and more unstable the control.

### p1498[0] Load moment of inertia

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 5042, 5210 |
| **Object:**S210 | **P-Group:**Closed-loop control | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [kgm²] | - [kgm²] | [ 0 ] - [kgm²] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the load moment of inertia.  
The setting is made during commissioning while the One Button Tuning is being performed.

### p1520[0] Torque limit upper

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**CALC_MOD_LIM_REF | **Access level:**2 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Closed-loop control | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**REL | **Scaling:**p2003 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| -1000000.00 [Nm] | 20000000.00 [Nm] | [ 0 ] 0.00 [Nm] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Setting the upper torque limit.  
This setting is made as part of the basic commissioning.

**Dependency:**
  
  
Refer to:
p1521, p1532, r1538, r1539

### p1521[0] Torque limit lower

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**CALC_MOD_LIM_REF | **Access level:**2 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Closed-loop control | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**REL | **Scaling:**p2003 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| -20000000.00 [Nm] | 1000000.00 [Nm] | [ 0 ] 0.00 [Nm] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the lower torque limit  
This setting is made as part of the basic commissioning.

**Dependency:**
  
  
Refer to:
p1520, p1532, r1538, r1539

### p1532[0] Torque limit offset

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 5620, 5630, 5650, 7010, 8012 |
| **Object:**S210 | **P-Group:**Closed-loop control | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**REL | **Scaling:**p2003 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| -100000.00 [Nm] | 100000.00 [Nm] | [ 0 ] 0.00 [Nm] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the offset for the torque limit.  
The setting allows electronic weight equalization to be used for vertical axes.  
Parameters p1520 and p1521 are offset by the set value in the same direction.

**Dependency:**
  
  
Refer to:
p1520, p1521

**Danger:**
  
If the offset is set higher/lower than the lower/upper torque limit, then the unloaded
drive can accelerate up to the maximum speed.

### r1538 Upper effective torque limit

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**2 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Closed-loop control | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**REL | **Scaling:**p2003 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [Nm] | - [Nm] | [ ] - [Nm] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the currently effective upper torque limit.

**Note:**
  
The value in r1538 may not exceed the value in p1520.

### r1539 Lower effective torque limit

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**2 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Closed-loop control | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**REL | **Scaling:**p2003 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [Nm] | - [Nm] | [ ] - [Nm] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the currently active lower torque limit.

**Note:**
  
The value in r1539 may not exceed the value in p1521.

### p1558 Measure/precontrol hanging/suspended axis force due to weight

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Motor identification | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| -1 | 1 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.2

**Description:**
  
Setting to start/reset the measurement of the force due to weight for a hanging/suspended
axis.  
The measurement can be started when the pulses are inhibited or the pulses are enabled
(p1558 = 1). If it was started when the pulses were inhibited, then it is only executed
after the pulses have been enabled. In both cases, alarm A07991 is output after starting.  
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
  
Refer to:
p1532

**Note:**
  
For master control with speed setpoint input from the commissioning tool, the torque
precontrol channels are deactivated, so that the weight equalization entered here
is not active.

### p1703[0] Isq current controller precontrol scaling

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Closed-loop control | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**REL | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.0 [%] | 200.0 [%] | [ 0 ] 0.0 [%] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the scaling of the dynamic current controller precontrol for the torque-generating
current component Isq.

### p1821[0] Direction of rotation

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 3) | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Motor | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 1 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Setting to change the direction of rotation.  
If the parameter is changed, it reverses the direction of rotation of the motor and
the encoder actual value without changing the setpoint.

**Value:**
  
0:
Clockwise  
1:
Counter-clockwise

**Dependency:**
  
  
Refer to:
F07434

**Notice:**
  
After changing parameter p1821, the direction of rotation is not automatically adapted
in the safety area. The following parameters can be used to set the direction of rotation
for safety monitoring:  
- p9516.1 "Position actual value sign change" (only for operation with encoder)

### p2000 Reference speed

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**CALC_MOD_ALL | **Access level:**2 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 6.00 [rpm] | 210000.00 [rpm] | [ 0 ] 3000.00 [rpm] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the reference quantity for the speed values.  
All speeds specified as relative values refer to this reference quantity.  
The reference quantity corresponds to 100% or 4000 hex (word) or 4000 0000 hex (double
word).

**Dependency:**
  
  
Refer to:
p2003

### p2003 Reference torque

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**CALC_MOD_ALL | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.01 [Nm] | 20000000.00 [Nm] | [ 0 ] 1.00 [Nm] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the reference quantity for the torque values.  
All torques specified as relative value are referred to this reference quantity.  
The reference quantity corresponds to 100% or 4000 hex (word) or 4000 0000 hex (double
word).

### r2050[0...21] Diagnostics PZD receive word

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**4000H | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.2

**Description:**
  
Displays the received process data (setpoints) in the word format.

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

**Dependency:**
  
  
Refer to:
r2060

### r2053[0...27] Diagnostics PZD send word

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the send process data (actual values) in the word format.

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

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Bit 0 | OFF | ON | - |
| 01 | Bit 1 | OFF | ON | - |
| 02 | Bit 2 | OFF | ON | - |
| 03 | Bit 3 | OFF | ON | - |
| 04 | Bit 4 | OFF | ON | - |
| 05 | Bit 5 | OFF | ON | - |
| 06 | Bit 6 | OFF | ON | - |
| 07 | Bit 7 | OFF | ON | - |
| 08 | Bit 8 | OFF | ON | - |
| 09 | Bit 9 | OFF | ON | - |
| 10 | Bit 10 | OFF | ON | - |
| 11 | Bit 11 | OFF | ON | - |
| 12 | Bit 12 | OFF | ON | - |
| 13 | Bit 13 | OFF | ON | - |
| 14 | Bit 14 | OFF | ON | - |
| 15 | Bit 15 | OFF | ON | - |

### r2060[0...20] Diagnostics PZD receive double word

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**4000H | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.2

**Description:**
  
Displays the received process data (setpoints) in the double word format.

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
  
  
Refer to:
r2050

### r2063[0...26] Diagnostics PZD send double word

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 2450, 2470 |
| **Object:**S210 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the send process data (actual values) in the double word format.

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

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Bit 0 | OFF | ON | - |
| 01 | Bit 1 | OFF | ON | - |
| 02 | Bit 2 | OFF | ON | - |
| 03 | Bit 3 | OFF | ON | - |
| 04 | Bit 4 | OFF | ON | - |
| 05 | Bit 5 | OFF | ON | - |
| 06 | Bit 6 | OFF | ON | - |
| 07 | Bit 7 | OFF | ON | - |
| 08 | Bit 8 | OFF | ON | - |
| 09 | Bit 9 | OFF | ON | - |
| 10 | Bit 10 | OFF | ON | - |
| 11 | Bit 11 | OFF | ON | - |
| 12 | Bit 12 | OFF | ON | - |
| 13 | Bit 13 | OFF | ON | - |
| 14 | Bit 14 | OFF | ON | - |
| 15 | Bit 15 | OFF | ON | - |
| 16 | Bit 16 | OFF | ON | - |
| 17 | Bit 17 | OFF | ON | - |
| 18 | Bit 18 | OFF | ON | - |
| 19 | Bit 19 | OFF | ON | - |
| 20 | Bit 20 | OFF | ON | - |
| 21 | Bit 21 | OFF | ON | - |
| 22 | Bit 22 | OFF | ON | - |
| 23 | Bit 23 | OFF | ON | - |
| 24 | Bit 24 | OFF | ON | - |
| 25 | Bit 25 | OFF | ON | - |
| 26 | Bit 26 | OFF | ON | - |
| 27 | Bit 27 | OFF | ON | - |
| 28 | Bit 28 | OFF | ON | - |
| 29 | Bit 29 | OFF | ON | - |
| 30 | Bit 30 | OFF | ON | - |
| 31 | Bit 31 | OFF | ON | - |

### r2109[0...63] Fault removed in milliseconds

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 8050, 8060 |
| **Object:**S210 | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [ms] | - [ms] | [ ] - [ms] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the time in milliseconds referred to the day that the fault was resolved.

**Dependency:**
  
  
Refer to:
r0945, r0947, r0948, r0949, r2130, r2133, r2136

**Notice:**
  
The time comprises r2136 (days) and r2109 (milliseconds).

**Note:**
  
The buffer parameters are cyclically updated in the background.  
The structure of the fault buffer and the assignment of the indices is shown in r0945.

### p2111 Alarm counter

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 8050, 8065 |
| **Object:**S210 | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 65535 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Number of alarms that have occurred after the last reset.

**Dependency:**
  
When setting p2111 = 0, all of the alarms that have been removed from the alarm buffer
[0...7] are transferred into the alarm history [8...63] - and alarm buffer [0...7]
is deleted.  
  
Refer to:
r2122, r2123, r2124, r2125

**Note:**
  
The parameter is reset to 0 at POWER ON.

## SINAMICS Parameter SINAMICS S210 02121 - 09652

SINAMICS Parameter SINAMICS S210 02121 - 09652

### r2121 Counter alarm buffer changes

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 8065 |
| **Object:**S210 | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
This counter is incremented every time the alarm buffer changes.

**Dependency:**
  
  
Refer to:
r2122, r2123, r2124, r2125

### r2122[0...63] Alarm number

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**2 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 8050, 8065 |
| **Object:**S210 | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the number of the last 64 alarms.

**Dependency:**
  
  
Refer to:
r2123, r2124, r2125, r2134, r2145, r2146

**Notice:**
  
The properties of the alarm buffer should be taken from the corresponding product
documentation.

**Note:**
  
The buffer parameters are cyclically updated in the background.  
Alarm buffer structure (general principle):  
r2122[0], r2124[0], r2123[0], r2125[0] --&gt; alarm 1 (the oldest)  
. . .  
r2122[7], r2124[7], r2123[7], r2125[7] --&gt; Alarm 8 (the latest)  
When the alarm buffer is full, the alarms that have gone are entered into the alarm
history:  
r2122[8], r2124[8], r2123[8], r2125[8] --&gt; Alarm 1 (the latest)  
. . .  
r2122[63], r2124[63], r2123[63], r2125[63] --&gt; alarm 56 (the oldest)

### r2123[0...63] Alarm received in milliseconds

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 8050, 8065 |
| **Object:**S210 | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [ms] | - [ms] | [ ] - [ms] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the time in milliseconds referred to the day that the alarm occurred.

**Dependency:**
  
  
Refer to:
r2122, r2124, r2125, r2134, r2145, r2146

**Notice:**
  
The time comprises r2145 (days) and r2123 (milliseconds).

**Note:**
  
The buffer parameters are cyclically updated in the background.  
The structure of the alarm buffer and the assignment of the indices is shown in r2122.

### r2124[0...63] Alarm value

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer32 | **Dynamic index:**- | **Func. diagram:** 8050, 8065 |
| **Object:**S210 | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays additional information about the active alarm (as integer number).

**Dependency:**
  
  
Refer to:
r2122, r2123, r2125, r2134, r2145, r2146

**Note:**
  
The buffer parameters are cyclically updated in the background.  
The structure of the alarm buffer and the assignment of the indices are shown in r2122.

### r2125[0...63] Alarm removed in milliseconds

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 8050, 8065 |
| **Object:**S210 | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [ms] | - [ms] | [ ] - [ms] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the time in milliseconds referred to the day that the alarm was resolved.

**Dependency:**
  
  
Refer to:
r2122, r2123, r2124, r2134, r2145, r2146

**Notice:**
  
The time comprises r2146 (days) and r2125 (milliseconds).

**Note:**
  
The buffer parameters are cyclically updated in the background.  
The structure of the alarm buffer and the assignment of the indices is shown in r2122.

### r2130[0...63] Fault received in days

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 8060 |
| **Object:**S210 | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the time in days referred to the day that the fault occurred.

**Dependency:**
  
  
Refer to:
r0945, r0947, r0948, r0949, r2109, r2133, r2136

**Notice:**
  
The time comprises r2130 (days) and r0948 (milliseconds).

**Note:**
  
The buffer parameters are cyclically updated in the background.

### r2131 Actual fault number

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 8060 |
| **Object:**S210 | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the number of the active fault that occurred last.

**Note:**
  
0: No fault present.

### r2132 Actual alarm number

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 8065 |
| **Object:**S210 | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the number of the alarm that last occurred.

**Note:**
  
0: No alarm present.

### r2133[0...63] Fault value for float values

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the additional information about the fault that occurred for float values.  
Refer to the fault for the interpretation of the fault value.

**Dependency:**
  
  
Refer to:
r0945, r0947, r0948, r0949, r2109, r2130, r2136

**Note:**
  
The buffer parameters are cyclically updated in the background.

### r2134[0...63] Alarm value for float values

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the additional information about the alarm that occurred for float values.  
Refer to the alarm for an interpretation of the alarm value.

**Dependency:**
  
  
Refer to:
r2122, r2123, r2124, r2125, r2145, r2146

**Note:**
  
The buffer parameters are cyclically updated in the background.

### r2136[0...63] Fault removed in days

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 8060 |
| **Object:**S210 | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the time in days referred to the day when the fault was rectified.

**Dependency:**
  
  
Refer to:
r0945, r0947, r0948, r0949, r2109, r2130, r2133

**Notice:**
  
The time comprises r2136 (days) and r2109 (milliseconds).

**Note:**
  
The buffer parameters are cyclically updated in the background.

### r2145[0...63] Alarm received in days

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 8065 |
| **Object:**S210 | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the time in days referred to the day that the alarm occurred.

**Dependency:**
  
  
Refer to:
r2122, r2123, r2124, r2125, r2134, r2146

**Notice:**
  
The time comprises r2145 (days) and r2123 (milliseconds).

**Note:**
  
The buffer parameters are cyclically updated in the background.

### r2146[0...63] Alarm removed in days

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 8065 |
| **Object:**S210 | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the time in days referred to the day when the alarm was cleared.

**Dependency:**
  
  
Refer to:
r2122, r2123, r2124, r2125, r2134, r2145

**Notice:**
  
The time comprises r2146 (days) and r2125 (milliseconds).

**Note:**
  
The buffer parameters are cyclically updated in the background.

### p2175[0] Motor blocked speed threshold

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**CALC_MOD_LIM_REF | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 8012 |
| **Object:**S210 | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 [rpm] | 210000.00 [rpm] | [ 0 ] 120.00 [rpm] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the speed threshold for the message "Motor locked".  
Monitoring is deactivated with p2175 = 0.

**Dependency:**
  
  
Refer to:
F07900

**Note:**
  
If the motor speed is less than the threshold value set in p2175 - and the motor is
operated for longer than 200 ms at the torque limit - then the motor is shut down
and a fault is output.

### p3103 UTC synchronization process

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**- | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 4 | 99 | [ 0 ] 4 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Setting the synchronization process.

**Value:**
  
4:
Network Time Protocol  
99:
No synchronization

**Note:**
  
If value = 4:  
Synchronization of the time in the drive with the time specified by the higher-level
control system.

### p3106 NTP time zone

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**- | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 38 | [ 0 ] 14 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the local time zone for NTP (Network Time Protocol).

**Value:**
  
0:
UTC-12 (AOE)  
1:
UTC-11 (NURT)  
2:
UTC-10 (HAST)  
3:
UTC-9:30 (MART)  
4:
UTC-9 (AKST)  
5:
UTC-8 (PST)  
6:
UTC-7 (MST)  
7:
UTC-6 (CST)  
8:
UTC-5 (EST)  
9:
UTC-4 (VET)  
10:
UTC-3:30 (NST)  
11:
UTC-3 (ART)  
12:
UTC-2 (GST)  
13:
UTC-1 (CVT)  
14:
UTC+0 (GMT)  
15:
UTC+1 (CET)  
16:
UTC+2 (EEK)  
17:
UTC+3 (MISK)  
18:
UTC+3:30 (IRST)  
19:
UTC+4 (GST)  
20:
UTC+4:30 (AFT)  
21:
UTC+5 (UZT)  
22:
UTC+5:30 (IST)  
23:
UTC+5:45 (NPT)  
24:
UTC+6 (BST)  
25:
UTC+6:30 (MMT)  
26:
UTC+7 (WIB)  
27:
UTC+8 (CST)  
28:
UTC+8:30 (PYT)  
29:
UTC+8:45 (ACWST)  
30:
UTC+9 (JST)  
31:
UTC+9:30 (ACST)  
32:
UTC+10 (AEST)  
33:
UTC+10:30 (ACDT)  
34:
UTC+11 (AEDT)  
35:
UTC+12 (ANAT)  
36:
UTC+13 (NZDT)  
37:
UTC+13:45 (CHADT)  
38:
UTC+14 (LINT)

**Dependency:**
  
  
Refer to:
p3103

### p3117 Change safety message type

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C1( 1) | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 1 | [ 0 ] 1 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.2

**Description:**
  
Sets the re-parameterization of all safety messages for faults and alarms.  
The relevant message type during changeover is selected by the firmware.  
0: Safety messages are not reparameterized (safety message buffer)  
1: Safety messages are reparameterized (no safety message buffer)

**Note:**
  
A change only becomes effective after a POWER ON.

### p5271[0] One Button Tuning configuration 1

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**- | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**REL | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0001 1100 bin |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the configuration for One Button Tuning.

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 03 | Setting the speed precontrol | No | Yes | 5045 |
| 04 | Setting the torque precontrol | No | Yes | 5045 |
| 07 | Setting the voltage precontrol | No | Yes | - |

**Dependency:**
  
  
Refer to:
r5274

**Note:**
  
For bit 03:  
Activation of speed feedforward control.  
For bit 04:  
Activation of speed/torque precontrol in the drive.  
For bit 07:  
Activation of the voltage precontrol.

### r5274 One Button Tuning dynamic response estimated

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 5045 |
| **Object:**S210 | **P-Group:**- | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**REL | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [ms] | - [ms] | [ ] - [ms] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the estimated dynamic response of the speed control loop as PT1 time constant
for One Button Tuning.  
The lower the time constant, the higher the dynamic performance.

**Dependency:**
  
  
Refer to:
p5271

### r5276[0] One Button Tuning Kv factor estimated

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**- | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**REL | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 [1000 rpm] | 100000.00 [1000 rpm] | [ ] - [1000 rpm] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the estimated position controller gain (Kv factor) for One Button Tuning.

**Dependency:**
  
  
Refer to:
p5271

**Note:**
  
The value for the closed-loop position control is required by a higher-level control
system.

### r5277[0] One Button Tuning precontrol symmetrizing time estimated

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 5045 |
| **Object:**S210 | **P-Group:**- | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**REL | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 [ms] | 100000.00 [ms] | [ ] - [ms] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the estimated precontrol symmetrizing time for One Button Tuning.  
This is required to symmetrize the position controller if the closed-loop position
control is in an external control system.

**Dependency:**
  
  
Refer to:
p5271

### p5291 FFT tuning configuration

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**- | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**REL | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0000 0000 0000 0000 0000 0000 0011 1001 bin |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the configuration for the "FFT tuning" function.  
This function is used for One Button Tuning (p5300 = 1).

**Bit field:**

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
  
  
Refer to:
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
into account in the speed controller loop. For high amplitudes in p5298, it is possible
that the measurement is unsuccessful, as the converter reaches its voltage limit.  
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
- the load moment of inertia is significantly higher than the motor moment of inertia
(e.g. &gt; 6x).  
- the coupling between the machine elements has almost no backlash (no play).  
- the stiffness of the mechanical transmission elements does not change significantly
in the traversing range.

### p5292 Controller optimization dynamic factor

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**2 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**- | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**REL | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 25.0 [%] | 125.0 [%] | [ 0 ] 80.0 [%] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the dynamic factor for optimizing the speed controller when One Button Tuning
is activated (p5300 = 1).

**Dependency:**
  
The higher the value in p5292, the lower the value in r5274.  
  
Refer to:
p5291

**Note:**
  
The higher the dynamic factor, the faster and more unstable the control.

### r5293 FFT tuning speed controller P gain identified

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Closed-loop control | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [Nms/rad] | - [Nms/rad] | [ ] - [Nms/rad] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the determined proportional gain Kp of the speed controller before FFT tuning.  
This function is used for One Button Tuning (p5300 = 1).

**Dependency:**
  
  
Refer to:
p5291

### p5296[0...2] Controller optimization noise amplitude

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**- | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**REL | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 1.0 [%] | 300.0 [%] | [ 0 ] 10.0 [%]  [ 1 ] 30.0 [%]  [ 2 ] 5.0 [%] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
The drive determines the noise amplitude for One Button Tuning and writes the value
to p5296.

**Dependency:**
  
  
Refer to:
p5291

### p5300[0] One Button Tuning selection

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**2 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**- | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**REL | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| -1 | 1 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Setting to activate/deactivate the One Button Tuning function.  
If p5300 = 1:  
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
Additional relevant parameters  
p5309, p5296, p5297, r5274  
  
Refer to:
p5271, r5274, p5292, r5293, p5296, p5301, p5308, p5309

**Notice:**
  
When executing One Button Tuning, the motor can be accelerated with its rated torque
if the torque limit (p1520, p1521) does not limit this to lower values. If the mechanical
system is sensitive, then it is recommended that the torque limits are appropriately
reduced before executing One Button Tuning.

**Note:**
  
If p5300 = -1:  
One Button Tuning is deactivated and p5300 is automatically set = 0. Further, the
presetting values for the speed controller are restored.  
If p5300 = 0:  
To permanently save the values for the speed controller that have been determined,
the parameters must be saved in a non-volatile memory.  
If p5300 = 1:  
One Button Tuning is active.  
The moment of inertia is determined once using a test signal. The controller parameters
and current setpoint filters are additionally determined once using a noise signal
as excitation source. The steps to be executed can be configured using p5301.

### p5301[0] One Button Tuning configuration 2

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**- | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**REL | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0000 0000 0000 0111 bin |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the functions for One Button Tuning (p5300 = 1).  
A test signal is required for some functions. To do this, observe parameters p5308
and p5309.

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Setting the proportional gain Kp | No | Yes | - |
| 01 | Setting current setpoint filter | No | Yes | - |
| 02 | Estimate moment of inertia | No | Yes | - |
| 07 | Activating synchronized axes | No | Yes | - |
| 08 | Moment of inertia determination from frequency response | No | Yes | - |

**Dependency:**
  
It is only possible to change the configuration if One Button Tuning is not active
(p5300 = 0).  
  
Refer to:
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
For bit 07:  
With this function, these axes are adapted to the dynamic response set in p5275. This
is necessary for interpolating axes. The time in p5275 should be set according to
the axis with the lowest dynamic response.  
For bit 08:  
Using this bit, the moment of inertia is determined from the frequency characteristic
using a test signal, and is transferred to p1498. The traversing path must first be
set using parameter p5308.

### r5306[0] One Button Tuning status

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**2 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**- | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**REL | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the status of the functions performed using One Button Tuning.

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Proportional gain Kp set | No | Yes | - |
| 01 | Current setpoint filter set | No | Yes | - |
| 02 | Moment of inertia estimation carried out | No | Yes | - |
| 13 | One Button Tuning successfully completed | No | Yes | - |
| 14 | Controller parameters reset due to fault | No | Yes | - |

**Dependency:**
  
  
Refer to:
p5300, p5301

**Note:**
  
For bit 00 = 1: The speed controller gain was set using One Button Tuning.  
For bit 01 = 1: The current setpoint filter was set using One Button Tuning  
For bit 02 = 1: The moment of inertia was determined.

### p5308[0] One Button Tuning distance limiting

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**- | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| -30000 [°] | 30000 [°] | [ 0 ] 0 [°] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Setting the distance limiting (permissible traversing range des motor).  
The traversing range is limited in the positive and negative directions.

**Note:**
  
A value of 360 degrees corresponds to one motor revolution.  
The position before the pulse enable is used as zero point.

### p5309[0] One Button Tuning duration

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**- | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 [ms] | 5000 [ms] | [ 0 ] 2000 [ms] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the duration for One Button Tuning (several acceleration operations)  
This function is used for One Button Tuning (p5300 = 1) to identify the total moment
of inertia of the drive train.

**Dependency:**
  
  
Refer to:
F07093

**Note:**
  
If, within this time, no setting values can be determined, then the drive is shut
down with the corresponding fault.

### r5600 Pe energy-saving mode ID

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 2381, 2382 |
| **Object:**S210 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 255 | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

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

**Note:**
  
Pe: PROFIenergy profiles  
For value = 0: This value is displayed in the "First commissioning" state.

### p5611 Pe energy-saving properties general

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 2381, 2382 |
| **Object:**S210 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0000 bin |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the general properties for energy-saving.

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Inhibit PROFIenergy control commands | No | Yes | - |

**Note:**
  
Pe: PROFIenergy profiles

### r8936[0...1] Cyclic connection status

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**- | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 13 | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the status of cyclic connections.

**Value:**
  
0:
Interrupted  
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
Configured controller RUN expected  
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

**Note:**
  
The parameter is active when the "PROFINET Device" and "EtherNet/IP" protocols are
selected (p2030 = 7, 10).  
For PROFINET, the following applies:  
For two connections (Shared Device or system redundancy) the display in the index
depends on the sequence in which the connections are established.  
The IP addresses of controllers 1 and 2 are displayed in r8961 and r8962.  
The following states are displayed for system redundancy:  
Primary controller: r8936[x] = 13  
Backup controller: r8936[x] = 11  
If value = 10:  
If the connection remains in this state, then when using PROFINET IRT the following
can apply:  
- topology error (incorrect port assignment).  
- synchronization missing.  
For EtherNet/IP, the following applies:  
Only a cyclic connection is possible for EtherNet/IP. Index 0 indicates the status
of the cyclic connection.

### r8937[0...5] Cyclic connection diagnostics

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**- | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Display for the cyclic connection diagnostics.

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
  
The parameter is active when the "PROFINET Device" and "EtherNet/IP" protocols are
selected (p2030 = 7, 10).  
For PROFINET, the following applies:  
For index [5]:  
Bit 0 = 1: there is at least one RT connection.  
Bit 1 = 1: there is an IRT connection.  
For EtherNet/IP, the following applies:  
For index [1, 3, 5]:  
These indices are not relevant.

### p8979 Activate SNMP

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 1 | [ 0 ] 1 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.2

**Description:**
  
The setting to activate/deactivate SNMP for the Industrial Ethernet interface (X127)
and the onboard PROFINET interface (X150).  
Facilitates SNMP access for network diagnostic tools (e.g. PRONETA).

**Value:**
  
0:
No  
1:
Yes

**Notice:**
  
When SNMP is activated, carefully note the impact relating to Industrial Security.

**Note:**
  
SNMP: Simple Network Management Protocol  
A change only becomes effective after a POWER ON or reset.

### p8984[0...1] Web server interface enable

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**- | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**0 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 1   [ 1 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.2

**Description:**
  
Setting to enable the interface for access via the web server.

**Index:**
  
[
0]:
Reserved  
[
1]:
PROFINET X150

**Note:**
  
p8984[1] = 65536:  
PROFINET interface X150 is enabled for access to the web server.  
p8984[1] = 0:  
PROFINET interface X150 is blocked for access to the web server.

### p9370 SI Motion acceptance test mode

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0000 hex | 00AC hex | [ 0 ] 0000 hex |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Setting to select and deselect the acceptance test mode.

**Value:**
  
0:
[00 hex] Deselect the acceptance test mode  
172:
[AC hex] Select the acceptance test mode

**Dependency:**
  
  
Refer to:
A01799

**Note:**
  
The acceptance test mode can only be selected if the motion monitoring functions integrated
in the drive are enabled (p9601.2).

### r9371 SI Motion acceptance test status

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0000 hex | 00AC hex | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the status of the acceptance test mode.

**Value:**
  
0:
[00 hex] Acc_mode inactive  
12:
[0C hex] Acc_mode not possible due to POWER ON fault  
13:
[0D hex] Acc_mode not possible due to incorrect ID in p9370  
15:
[0F hex] Acc_mode not possible due to expired Acc_timer  
172:
[AC hex] Acc_mode active

**Dependency:**
  
  
Refer to:
p9370  
Refer to:
A01799

### p9501 SI Motion enable safety functions

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0000 0000 0000 0000 0000 0000 0000 0000 bin |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the enable signals for the safe motion monitoring.

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Enable SOS/SLS | Inhibit | Enable | - |
| 16 | Enable SSM | Inhibit | Enable | - |
| 17 | Enable SDI | Inhibit | Enable | 2824 |
| 18 | Enable SS2E | Inhibit | Enable | - |
| 20 | Enable SLA | Inhibit | Enable | - |
| 24 | Enable transfer SLS limit value via PROFIsafe | Inhibit | Enable | - |

**Dependency:**
  
  
Refer to:
F01682, F01683

**Note:**
  
A change only becomes effective after a POWER ON.  
SDI: Safe Direction (safe motion direction)  
SLA: Safely-Limited Acceleration  
SLS: Safely-Limited Speed  
SOS: Safe Operating Stop  
SS2E: Safe Stop 2 External (Safe Stop 2 with external stop)  
SSM: Safe Speed Monitor (safety-relevant feedback signal from the speed monitoring)

### p9502 SI Motion axis type

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 1 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the axis type (linear axis or rotary axis/spindle).

**Value:**
  
0:
Linear axis  
1:
Rotary axis/spindle

**Note:**
  
For the commissioning tool, after changing over the axis type, the units dependent
on the axis type are only updated after a project upload.  
A change only becomes effective after a POWER ON.

### p9505 SI Motion SP modulo value

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 [°] | 737280 [°] | [ 0 ] 0 [°] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the modulo value in degrees for rotary axes.  
This setting is only used to correctly display the diagnostics information in r9708.  
The value should be set so that it is precisely at 2^n revolutions, so that when the
range that can be represented (+/-2048) overflows, this does not cause the position
actual value to jump.  
The modulo function is deactivated for a value = 0.

**Dependency:**
  
  
Refer to:
p9501  
Refer to:
F01681

**Note:**
  
SP: Safe Position

### p9506 SI Motion function specification

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 2 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the function specification for the safe motion monitoring.

**Value:**
  
0:
Safety with encoder and acceleration monitoring (SAM)  
2:
Safety with encoder with brake ramp (SBR)

**Dependency:**
  
  
Refer to:
A01711

**Note:**
  
A change only becomes effective after a POWER ON.  
SAM: Safe Acceleration Monitor (safe acceleration monitoring)  
SBR: Safe Brake Ramp (safe brake ramp monitoring)  
SI: Safety Integrated

### p9507 SI Motion function configuration

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0100 0001 bin |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the function configuration for the safe motion monitoring functions.

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Extended message acknowledgment | No | Yes | - |
| 01 | Setpoint speed limiting for A01711 | Yes | No | - |
| 03 | SS1 with OFF3 (brake response) | SS1 with OFF3 | SS1E external stop | - |

**Dependency:**
  
  
Refer to:
A01711

**Note:**
  
For bit 00:  
When the function is activated, a safety-relevant acknowledgment (internal event acknowledge)
can be performed by selecting/deselecting STO.  
For bit 01:  
When the function is activated, the active setpoint velocity limiting (r9733) for
active A01711 is set to zero.  
For bit 03:  
When the bit is activated, for a fault response with SS1 or when SS1 is selected,
an SS1E is initiated. As a consequence, brake monitoring (SBR, SAM) is deactivated.  
SS1: Safe Stop 1  
SS1E: Safe Stop 1 external (Safe Stop 1 with external stop)  
STO: Safe Torque Off

### p9515 SI Motion encoder coarse position value configuration

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0000 0000 0000 0000 0000 0000 0000 0000 bin |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the encoder configuration for the redundant coarse position value.  
The encoder that is used for the safe motion monitoring function must be parameterized
in this parameter.

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Incrementer | No | Yes | - |
| 01 | Encoder CRC least significant byte first | No | Yes | - |
| 02 | Redundant coarse position val. most significant bit left-aligned | No | Yes | - |
| 04 | Binary comparison not possible | No | Yes | - |
| 05 | Single-channel encoder | No | Yes | - |
| 16 | DRIVE-CLiQ encoder | No | Yes | - |

**Note:**
  
- after starting the copy function (p9700 = 57 hex), p9515.0...5 are set according
to the encoder.  
For safety functions that are not enabled (p9501 = 0), the following applies:  
- p9515.16 is automatically set when the system powers up.  
For safety functions that are enabled (p9501 &gt; 0), the following applies:  
- p9515.16 is checked to see that it matches the encoder.

### p9516 SI Motion encoder configuration safety functions

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0000 0000 bin |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the configuration for the motor encoder and position actual value.  
The encoder that is used for the safe motion monitoring function must be parameterized
in this parameter.

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 01 | Position actual value sign change | No | Yes | - |
| 04 | No STO after encoder fault | No | Yes | - |

**Dependency:**
  
  
Refer to:
F01671

### p9518 SI Motion encoder pulses per revolution

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 16777215 | [ 0 ] 2048 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the number of encoder pulses per revolution.  
The encoder that is used for the safe motion monitoring function must be parameterized
in this parameter.

**Dependency:**
  
  
Refer to:
F01671

**Note:**
  
For safety functions that are not enabled (p9501 = 0), the following applies:  
- p9518 is automatically set when the system powers up.  
For safety functions that are enabled (p9501 &gt; 0), the following applies:  
- p9518 is checked to see that it matches the encoder.

### p9519 SI Motion fine resolution G1_XIST1

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 2 | 18 | [ 0 ] 11 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the fine resolution for G1_XIST1 in bits.  
The encoder that is used for the safe motion monitoring function must be parameterized
in this parameter.

**Dependency:**
  
  
Refer to:
F01671

**Note:**
  
G1_XIST1: encoder 1 position actual value 1 (PROFIdrive)  
For safety functions that are not enabled (p9501 = 0), the following applies:  
- p9519 is automatically set when the system powers up.  
For safety functions that are enabled (p9501 &gt; 0), the following applies:  
- p9519 is checked to see that it matches the encoder.

### p9520 SI Motion spindle pitch

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.1000 [mm] | 8388.0000 [mm] | [ 0 ] 10.0000 [mm] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the gear ratio between the encoder and load in mm/revolution for a linear axis
with rotary encoder.

**Notice:**
  
The fourth decimal point can be rounded-off depending on the size of the entered number
(from 3 places before the decimal point).

### p9521[0...7] SI Motion gearbox encoder (motor)/load denominator

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 1 | 2147000000 | [ 0 ] 1 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the denominator for the gearbox between the encoder and load.

**Index:**
  
[
0]:
Gearbox 1  
[
1...7]:
Reserved

**Dependency:**
  
  
Refer to:
p9522

### p9522[0...7] SI Motion gearbox encoder (motor)/load numerator

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 1 | 2147000000 | [ 0 ] 1 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the numerator for the gearbox between the encoder and load.

**Index:**
  
[
0]:
Gearbox 1  
[
1...7]:
Reserved

**Dependency:**
  
  
Refer to:
p9521

### p9530 SI Motion standstill tolerance

[S210](#p9530-si-motion-standstill-tolerance-1)

[S210 Safety rotary axis](#p9530-si-motion-standstill-tolerance-2)

#### p9530 SI Motion standstill tolerance

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.000 [mm] | 100.000 [mm] | [ 0 ] 1.000 [mm] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the tolerance for the "SOS" function.

**Dependency:**
  
  
Refer to:
A01707

**Note:**
  
SOS: Safe Operating Stop

#### p9530 SI Motion standstill tolerance

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 (Safety rot) | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.000 [°] | 100.000 [°] | [ 0 ] 1.000 [°] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the tolerance for the "SOS" function.

**Dependency:**
  
  
Refer to:
A01707

**Note:**
  
SOS: Safe Operating Stop

### p9531[0...3] SI Motion SLS limit values

[S210](#p953103-si-motion-sls-limit-values-1)

[S210 Safety rotary axis](#p953103-si-motion-sls-limit-values-2)

#### p9531[0...3] SI Motion SLS limit values

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 [mm/min] | 1000000.00 [mm/min] | [ 0 ] 2000.00 [mm/min] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the limit values for the "SLS" function.

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
  
  
Refer to:
p9563  
Refer to:
A01714

**Note:**
  
SLS: Safely-Limited Speed

#### p9531[0...3] SI Motion SLS limit values

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 (Safety rot) | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 [rpm] | 1000000.00 [rpm] | [ 0 ] 2000.00 [rpm] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the limit values for the "SLS" function.

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
  
  
Refer to:
p9563  
Refer to:
A01714

**Note:**
  
SLS: Safely-Limited Speed

### p9533 SI Motion SLS setpoint speed limiting

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.000 [%] | 100.000 [%] | [ 0 ] 80.000 [%] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
This is an evaluation factor to define the setpoint limit from the selected actual
speed limit.  
The active SLS limit value is evaluated with this factor and is made available as
setpoint limit in r9733.

**Dependency:**
  
This parameter only has to be parameterized for the motion monitoring functions integrated
in the drive (p9601.2 = 1)  
r9733[0] = p9531[x] x p9533 (converted from the load side to the motor side)  
r9733[1] = - p9531[x] x p9533 (converted from the load side to the motor side)  
[x] = Selected SLS stage  
Conversion factor from the motor side to the load side:  
- motor type = rotary and axis type = linear: p9522 / (p9521 x p9520)  
- otherwise: p9522 / p9521  
  
Refer to:
p9501, p9531, p9601

**Note:**
  
The active actual speed limit is selected via safety-relevant inputs.  
When SOS is selected or an STO, SS1, SS2, SS2E, a setpoint of 0 is entered in r9733.  
SLS: Safely-Limited Speed

### p9539[0...7] SI Motion gearbox direction of rotation reversal

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 1 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the direction of rotation reversal for the gearbox.  
0: No direction of rotation reversal  
1: Direction of rotation reversal

**Index:**
  
[
0]:
Gearbox 1  
[
1...7]:
Reserved

**Dependency:**
  
  
Refer to:
p9521

### p9542 SI Motion actual value comparison tolerance (cross-check)

[S210](#p9542-si-motion-actual-value-comparison-tolerance-cross-check-1)

[S210 Safety rotary axis](#p9542-si-motion-actual-value-comparison-tolerance-cross-check-2)

#### p9542 SI Motion actual value comparison tolerance (cross-check)

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.0010 [mm] | 360.0000 [mm] | [ 0 ] 0.1000 [mm] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the tolerance for the data cross-check of the actual position between the two
monitoring channels.

**Dependency:**
  
  
Refer to:
A01711

**Note:**
  
For a "linear axis with rotating motor" configuration and factory setting of p9520,
p9521 and p9522, the factory setting of p9542 corresponds to a position tolerance
of 36 ° on the motor side.

#### p9542 SI Motion actual value comparison tolerance (cross-check)

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 (Safety rot) | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.0010 [°] | 360.0000 [°] | [ 0 ] 0.1000 [°] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the tolerance for the data cross-check of the actual position between the two
monitoring channels.

**Dependency:**
  
  
Refer to:
A01711

### p9545 SI Motion SSM filter time

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 [ms] | 500.00 [ms] | [ 0 ] 0.00 [ms] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the filter time for the SSM feedback signal to detect standstill.

**Note:**
  
The filter time is effective only if the function is enabled (p9501.16 = 1).  
The parameter is included in the data cross-check of the two monitoring channels.  
The set time is rounded internally to an integer multiple of the monitoring clock
cycle.  
SSM: Safe Speed Monitor (safety-relevant feedback signal from the speed monitoring)

### p9546 SI Motion SSM velocity limit

[S210](#p9546-si-motion-ssm-velocity-limit-1)

[S210 Safety rotary axis](#p9546-si-motion-ssm-velocity-limit-2)

#### p9546 SI Motion SSM velocity limit

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 [mm/min] | 1000000.00 [mm/min] | [ 0 ] 20.00 [mm/min] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the velocity limit for the SSM feedback signal to detect standstill.  
When this limit value is undershot, the signal "SSM feedback signal active" is set.  
For p9568 = 0, the value in p9546 is also applicable for SAM/SBR.

**Note:**
  
SAM: Safe Acceleration Monitor (safe acceleration monitoring)  
SBR: Safe Brake Ramp (safe brake ramp monitoring)  
SSM: Safe Speed Monitor (safety-relevant feedback signal from the speed monitoring)

#### p9546 SI Motion SSM velocity limit

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 (Safety rot) | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 [rpm] | 1000000.00 [rpm] | [ 0 ] 20.00 [rpm] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the velocity limit for the SSM feedback signal to detect standstill.  
When this limit value is undershot, the signal "SSM feedback signal active" is set.  
For p9568 = 0, the value in p9546 is also applicable for SAM/SBR.

**Note:**
  
SAM: Safe Acceleration Monitor (safe acceleration monitoring)  
SBR: Safe Brake Ramp (safe brake ramp monitoring)  
SSM: Safe Speed Monitor (safety-relevant feedback signal from the speed monitoring)

### p9547 SI Motion SSM velocity hysteresis

[S210](#p9547-si-motion-ssm-velocity-hysteresis-1)

[S210 Safety rotary axis](#p9547-si-motion-ssm-velocity-hysteresis-2)

#### p9547 SI Motion SSM velocity hysteresis

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.0010 [mm/min] | 500.0000 [mm/min] | [ 0 ] 10.0000 [mm/min] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the velocity hysteresis for the SSM feedback signal to detect standstill.

**Dependency:**
  
  
Refer to:
A01711

**Note:**
  
The velocity hysteresis is effective only if the function is enabled (p9501.16 = 1).  
The parameter is included in the data cross-check of the two monitoring channels.  
SSM: Safe Speed Monitor (safety-relevant feedback signal from the speed monitoring)

#### p9547 SI Motion SSM velocity hysteresis

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 (Safety rot) | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.0010 [rpm] | 500.0000 [rpm] | [ 0 ] 10.0000 [rpm] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the velocity hysteresis for the SSM feedback signal to detect standstill.

**Dependency:**
  
  
Refer to:
A01711

**Note:**
  
The velocity hysteresis is effective only if the function is enabled (p9501.16 = 1).  
The parameter is included in the data cross-check of the two monitoring channels.  
SSM: Safe Speed Monitor (safety-relevant feedback signal from the speed monitoring)

### p9548 SI Motion SAM actual speed tolerance

[S210](#p9548-si-motion-sam-actual-speed-tolerance-1)

[S210 Safety rotary axis](#p9548-si-motion-sam-actual-speed-tolerance-2)

#### p9548 SI Motion SAM actual speed tolerance

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 [mm/min] | 120000.00 [mm/min] | [ 0 ] 300.00 [mm/min] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the velocity tolerance for the "SAM" function.

**Dependency:**
  
  
Refer to:
A01706

**Note:**
  
SAM: Safe Acceleration Monitor (safe acceleration monitoring)

#### p9548 SI Motion SAM actual speed tolerance

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 (Safety rot) | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 [rpm] | 120000.00 [rpm] | [ 0 ] 300.00 [rpm] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the velocity tolerance for the "SAM" function.

**Dependency:**
  
  
Refer to:
A01706

**Note:**
  
SAM: Safe Acceleration Monitor (safe acceleration monitoring)

### p9551 SI Motion SLS switchover/SOS delay time

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 [ms] | 600000.00 [ms] | [ 0 ] 100.00 [ms] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the delay time for the SLS changeover and for the activation of SOS for the "SLS"
and "SOS" functions.  
When transitioning from a higher to a lower Safely-Limited Speed level, and when activating
SOS, within this delay time, the "old" speed level remains active.  
This delay is also applicable when activating SLS from the state "SOS and SLS inactive"
and activating SOS from the state "SOS inactive".

**Note:**
  
The set time is rounded internally to an integer multiple of the monitoring clock
cycle.  
SLS: Safely-Limited Speed  
SOS: Safe Operating Stop

### p9552 SI Motion transition time SS2 to SOS

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 [ms] | 600000.00 [ms] | [ 0 ] 100.00 [ms] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the transition time from SS2 to SOS.

**Note:**
  
The set time is rounded internally to an integer multiple of the monitoring clock
cycle.  
SOS: Safe Operating Stop  
SS2: Safe Stop 2

### p9553 SI Motion transition time SS2E to SOS

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 [ms] | 600000.00 [ms] | [ 0 ] 100.00 [ms] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the transition time from SS2E to SOS.

**Note:**
  
The set time is rounded internally to an integer multiple of the monitoring clock
cycle.  
SI: Safety Integrated  
SOS: Safe Operating Stop  
SS2E: Safe Stop 2 External (Safe Stop 2 with external stop)

### p9555 SI Motion transition time A01711 to SS1

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 [ms] | 600000.00 [ms] | [ 0 ] 0.00 [ms] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the transition time from A01711 to SS1.

**Dependency:**
  
  
Refer to:
A01711

**Note:**
  
The set time is rounded internally to an integer multiple of the monitoring clock
cycle.

### p9556 SI Motion SS1 to STO delay time

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 [ms] | 3600000.00 [ms] | [ 0 ] 100.00 [ms] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the delay time for STO after an SS1.

**Dependency:**
  
  
Refer to:
p9560  
Refer to:
F01701

**Note:**
  
The set time is rounded internally to an integer multiple of the monitoring clock
cycle.

### p9557 SI Motion STO test time

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 [ms] | 10000.00 [ms] | [ 0 ] 100.00 [ms] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the time after which STO must be active when initiating the test stop.

**Dependency:**
  
  
Refer to:
A01798

**Note:**
  
The set time is rounded internally to an integer multiple of the monitoring clock
cycle.  
STO: Safe Torque Off

### p9558 SI Motion acceptance test mode, time limit

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 5000.00 [ms] | 100000.00 [ms] | [ 0 ] 40000.00 [ms] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the maximum time for the acceptance test mode.  
If the acceptance test mode takes longer than the selected time limit, then the mode
is automatically terminated.

**Dependency:**
  
  
Refer to:
A01799

**Note:**
  
The set time is rounded internally to an integer multiple of the monitoring clock
cycle.

### p9559 SI Motion forced checking procedure timer

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 [h] | 9000.00 [h] | [ 0 ] 8600.00 [h] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the time interval for carrying out the forced checking procedure and testing
the safety motion monitoring functions integrated in the drives.  
Within the parameterized time, the safety functions must have been tested at least
once (including deselection of the "STO" function).  
This monitoring time is reset each time the test is carried out.  
The signal source to initiate the forced checking procedure is set in p9705.

**Dependency:**
  
  
Refer to:
A01697, A01798

**Note:**
  
STO: Safe Torque Off

### p9560 SI Motion STO shutdown speed

[S210](#p9560-si-motion-sto-shutdown-speed-1)

[S210 Safety rotary axis](#p9560-si-motion-sto-shutdown-speed-2)

#### p9560 SI Motion STO shutdown speed

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 [mm/min] | 6000.00 [mm/min] | [ 0 ] 0.00 [mm/min] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the shutdown velocity for activating STO.  
Below this velocity, "standstill" is assumed, and for an SS1, STO is selected.

**Dependency:**
  
  
Refer to:
p9556

**Note:**
  
The shutdown velocity has no effect for a value = 0.  
SS1: Safe Stop 1  
STO: Safe Torque Off

#### p9560 SI Motion STO shutdown speed

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 (Safety rot) | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 [rpm] | 6000.00 [rpm] | [ 0 ] 0.00 [rpm] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the shutdown velocity for activating STO.  
Below this velocity, "standstill" is assumed, and for an SS1, STO is selected.

**Dependency:**
  
  
Refer to:
p9556

**Note:**
  
The shutdown velocity has no effect for a value = 0.  
SS1: Safe Stop 1  
STO: Safe Torque Off

### p9563[0...3] SI Motion SLS-specific stop response

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 3 | [ 0 ] 1 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the SLS-specific stop response for the SLS function.  
These settings apply to the individual limit values for SLS.  
An input value of less than 5 signifies personnel protection, from 10 and upwards,
machine protection.

**Value:**
  
0:
STO  
1:
SS1  
2:
SS2  
3:
SS2E

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
  
  
Refer to:
p9531

**Note:**
  
In an extended sense, bus failure is interpreted here as a communication error in
the control signals of the safety functions (e.g. via PROFIsafe).  
SI: Safety Integrated  
SLS: Safely-Limited Speed  
SS1: Safe Stop 1  
SS2: Safe Stop 2  
SS2E: Safe Stop 2 External (Safe Stop 2 with external stop)  
STO: Safe Torque Off

### p9564 SI Motion SDI tolerance

[S210](#p9564-si-motion-sdi-tolerance-1)

[S210 Safety rotary axis](#p9564-si-motion-sdi-tolerance-2)

#### p9564 SI Motion SDI tolerance

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.001 [mm] | 360.000 [mm] | [ 0 ] 12.000 [mm] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the tolerance for the "SDI" function.  
This motion in the monitored direction is still permissible before message A01716
is initiated.

**Dependency:**
  
  
Refer to:
p9565, p9566  
Refer to:
A01716

**Note:**
  
SDI: Safe Direction (safe motion direction)

#### p9564 SI Motion SDI tolerance

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 (Safety rot) | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.001 [°] | 360.000 [°] | [ 0 ] 12.000 [°] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the tolerance for the "SDI" function.  
This motion in the monitored direction is still permissible before message A01716
is initiated.

**Dependency:**
  
  
Refer to:
p9565, p9566  
Refer to:
A01716

**Note:**
  
SDI: Safe Direction (safe motion direction)

### p9565 SI Motion SDI delay time

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 [ms] | 600000.00 [ms] | [ 0 ] 100.00 [ms] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the delay time for the "SDI" function.  
After selecting the SDI function, then for a maximum of this time, motion in the monitored
direction is permissible. This time can therefore be used for braking any motion.

**Dependency:**
  
  
Refer to:
p9564, p9566  
Refer to:
A01716

**Note:**
  
The set time is rounded internally to an integer multiple of the monitoring clock
cycle.  
SDI: Safe Direction (safe motion direction)

### p9566 SI Motion SDI stop response

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 3 | [ 0 ] 1 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the stop response for the SDI function.  
This setting applies to both directions of motion.

**Value:**
  
0:
STO  
1:
SS1  
2:
SS2  
3:
SS2E

**Dependency:**
  
  
Refer to:
p9564, p9565  
Refer to:
A01716

**Note:**
  
In an extended sense, bus failure is interpreted here as a communication fault in
the control signals of the safety functions (e.g. via PROFIsafe).  
SDI: Safe Direction (safe motion direction)

### p9568 SI Motion SAM/SBR speed limit

[S210](#p9568-si-motion-samsbr-speed-limit-1)

[S210 Safety rotary axis](#p9568-si-motion-samsbr-speed-limit-2)

#### p9568 SI Motion SAM/SBR speed limit

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 [mm/min] | 1000.00 [mm/min] | [ 0 ] 0.00 [mm/min] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the velocity limit for the "SAM" and "SBR" functions.  
If the drive accelerates during the down ramp by the tolerance in p9548, then SAM
identifies this and STO is initiated.  
The monitoring operates as follows:  
- SAM monitoring is activated for SS1 and SS2.  
- the SAM limit value is frozen after the velocity limit in p9568 is undershot.  
- SAM monitoring is still executed until the transition time to SOS/STO has expired.

**Note:**
  
For p9568 = 0, the following applies:  
The value in p9546 (SSM) is applied as the velocity limit for SAM/SBR.  
SAM: Safe Acceleration Monitor (safe acceleration monitoring)  
SBR: Safe Brake Ramp (safe brake ramp monitoring)  
SSM: Safe Speed Monitor (safety-relevant feedback signal from the speed monitoring)

#### p9568 SI Motion SAM/SBR speed limit

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 (Safety rot) | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 [rpm] | 1000.00 [rpm] | [ 0 ] 0.00 [rpm] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the velocity limit for the "SAM" and "SBR" functions.  
If the drive accelerates during the down ramp by the tolerance in p9548, then SAM
identifies this and STO is initiated.  
The monitoring operates as follows:  
- SAM monitoring is activated for SS1 and SS2.  
- the SAM limit value is frozen after the velocity limit in p9568 is undershot.  
- SAM monitoring is still executed until the transition time to SOS/STO has expired.

**Note:**
  
For p9568 = 0, the following applies:  
The value in p9546 (SSM) is applied as the velocity limit for SAM/SBR.  
SAM: Safe Acceleration Monitor (safe acceleration monitoring)  
SBR: Safe Brake Ramp (safe brake ramp monitoring)  
SSM: Safe Speed Monitor (safety-relevant feedback signal from the speed monitoring)

### p9570 SI Motion acceptance test mode

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0000 hex | 00AC hex | [ 0 ] 0000 hex |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Setting to select and deselect the acceptance test mode.

**Value:**
  
0:
[00 hex] Deselect the acceptance test mode  
172:
[AC hex] Select the acceptance test mode

**Dependency:**
  
  
Refer to:
p9558, r9571, p9601  
Refer to:
A01799

**Note:**
  
Acceptance test mode can only be selected if the safe motion monitoring functions
are enabled.

### r9571 SI Motion acceptance test status

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0000 hex | 00AC hex | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the status of the acceptance test mode.

**Value:**
  
0:
[00 hex] Acc_mode inactive  
12:
[0C hex] Acc_mode not possible due to POWER ON fault  
13:
[0D hex] Acc_mode not possible due to incorrect ID in p9570  
15:
[0F hex] Acc_mode not possible due to expired Acc_timer  
172:
[AC hex] Acc_mode active

**Dependency:**
  
  
Refer to:
p9558, p9570  
Refer to:
A01799

### p9576 SI Motion SLA filter time

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 [ms] | 500.00 [ms] | [ 0 ] 0.00 [ms] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.2

**Description:**
  
Sets the filter time for the acceleration monitoring with a fine resolution of the
acceleration.

**Note:**
  
The filter time is only effective if the function is enabled (p9501.20 = 1).  
The set time is rounded internally to an integer multiple of the monitoring clock
cycle.  
The parameter is included in the data cross-check of the two monitoring channels.  
SLA: Safely-Limited Acceleration

### p9578 SI Motion SLA acceleration limit

[S210](#p9578-si-motion-sla-acceleration-limit-1)

[S210 Safety rotary axis](#p9578-si-motion-sla-acceleration-limit-2)

#### p9578 SI Motion SLA acceleration limit

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 [m/s²] | 1000.00 [m/s²] | [ 0 ] 1.00 [m/s²] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the acceleration limit for the "Safely-Limited Acceleration" function (SLA).

**Dependency:**
  
  
Refer to:
p9579

**Note:**
  
The set time is rounded internally to an integer multiple of the monitoring clock
cycle.  
SLA: Safely-Limited Acceleration

#### p9578 SI Motion SLA acceleration limit

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 (Safety rot) | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 [rev/s²] | 1000.00 [rev/s²] | [ 0 ] 1.00 [rev/s²] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the acceleration limit for the "Safely-Limited Acceleration" function (SLA).

**Dependency:**
  
  
Refer to:
p9579

**Note:**
  
The set time is rounded internally to an integer multiple of the monitoring clock
cycle.  
SLA: Safely-Limited Acceleration

### p9579 SI Motion SLA stop response

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 3 | [ 0 ] 1 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the stop response for the "Safely-Limited Acceleration" function (SLA).

**Value:**
  
0:
STO  
1:
SS1  
2:
SS2  
3:
SS2E

**Dependency:**
  
  
Refer to:
p9578

**Note:**
  
The set time is rounded internally to an integer multiple of the monitoring clock
cycle.  
SLA: Safely-Limited Acceleration

### p9581 SI Motion brake ramp reference value

[S210](#p9581-si-motion-brake-ramp-reference-value-1)

[S210 Safety rotary axis](#p9581-si-motion-brake-ramp-reference-value-2)

#### p9581 SI Motion brake ramp reference value

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 600.0000 [mm/min] | 1000000.0000 [mm/min] | [ 0 ] 1500.0000 [mm/min] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the reference value to define the brake ramp.  
The rate of rise of the brake ramp depends upon p9581 (reference value) and p9583
(monitoring time).

**Dependency:**
  
  
Refer to:
p9582, p9583

#### p9581 SI Motion brake ramp reference value

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 (Safety rot) | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 600.0000 [rpm] | 1000000.0000 [rpm] | [ 0 ] 1500.0000 [rpm] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the reference value to define the brake ramp.  
The rate of rise of the brake ramp depends upon p9581 (reference value) and p9583
(monitoring time).

**Dependency:**
  
  
Refer to:
p9582, p9583

### p9582 SI Motion brake ramp delay time

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 10.00 [ms] | 99000.00 [ms] | [ 0 ] 250.00 [ms] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the delay time for monitoring the brake ramp.  
Monitoring of the brake ramp starts once the delay time has elapsed.

**Dependency:**
  
  
Refer to:
p9581, p9583

**Note:**
  
The set time is rounded internally to an integer multiple of the monitoring clock
cycle.  
The set time is internally limited (lower limit) to 2 safety monitoring clock cycles.

### p9583 SI Motion brake ramp monitoring time

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.50 [s] | 3600.00 [s] | [ 0 ] 10.00 [s] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the monitoring time to define the brake ramp.  
The rate of rise of the brake ramp depends upon p9581 (reference value) and p9583
(monitoring time).

**Dependency:**
  
  
Refer to:
p9581, p9582

**Note:**
  
The set time is rounded internally to an integer multiple of the monitoring clock
cycle.

### r9590[0...3] SI Motion version, safe motion monitoring functions

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the Safety Integrated version for the safe monitoring functions.

**Index:**
  
[
0]:
Safety Version (major release)  
[
1]:
Safety Version (minor release)  
[
2]:
Safety Version (baselevel or patch)  
[
3]:
Safety Version (hotfix)

**Dependency:**
  
  
Refer to:
r9770

**Note:**
  
Example:  
r9590[0] = 5, r9590[1] = 10, r9590[2] = 1, r9590[3] = 0 --&gt; SI Motion version V05.10.01.00

### p9601 SI enable, functions integrated in the drive

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0000 bin |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the enable signals for the safety functions integrated in the drive and the type
of selection.  
Only a selection of the subsequently listed settings is permissible:  
0000 hex:  
Safety functions integrated in the drive inhibited (no safety function).  
0001 hex:  
Basis functions are enabled via the onboard terminals.  
0008 hex:  
Basis functions are enabled via PROFIsafe.  
0009 hex:  
Basis functions are enabled via PROFIsafe and onboard terminals.  
000C hex:  
Extended functions via PROFIsafe are enabled.  
000D hex:  
Extended functions via PROFIsafe and basic functions via onboard terminals are enabled.

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | STO enabled via terminals: | Inhibit | Enable | - |
| 02 | Enable motion monitoring functions integrated in drive | Inhibit | Enable | - |
| 03 | Enable PROFIsafe | Inhibit | Enable | - |

**Note:**
  
A change only becomes effective after a POWER ON.  
Exception:  
A change to p9601.0 takes effect immediately.  
STO: Safe Torque Off  
SS1: Safe Stop 1  
SI: Safety Integrated

### p9602 SI enable safe brake control

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 1 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the enable for the "SBC" function.

**Value:**
  
0:
Inhibit SBC  
1:
Enable SBC

**Note:**
  
The "SBC" function is not activated until at least one safety monitoring function
has been enabled (i.e. p9501 not equal to 0 and/or p9601 not equal to 0).  
The parameterization "No motor holding brake available" and "Safe Brake Control" enabled
(p1215 = 0, p9602 = 1) does not make sense if a motor holding brake is not being used.  
SBC: Safe Brake Control  
SI: Safety Integrated

### p9610 SI PROFIsafe address

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 65534 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the PROFIsafe address.

**Note:**
  
A change only becomes effective after a POWER ON.  
The PROFIsafe address in the drive must be identical with the address in the control.

### p9611 SI PROFIsafe telegram selection

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 901 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

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
  
  
Refer to:
r60022

**Note:**
  
A change only becomes effective after a POWER ON.  
To select the PROFIdrive telegram, PROFIsafe must have been enabled (p9601.3 = 1).

### p9612 SI PROFIsafe failure response

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 1 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the stop response when PROFIsafe communication fails.

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
The following must be observed:  
- the transition time F01611 to STO (p9658) must be set higher or equal to the delay
time (p9652).

### p9650 SI F-DI discrepancy time

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 [ms] | 2000.00 [ms] | [ 0 ] 500.00 [ms] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the time during which the drive tolerates different signal states of the failsafe
digital input.

**Note:**
  
F-DI: Failsafe Digital Input

### p9651 SI STO/SBC/SS1 t_debounce time

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 [ms] | 100.00 [ms] | [ 0 ] 0.00 [ms] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the debounce time for the failsafe digital input used to control STO/SBC/SS1.  
The debounce time specifies the duration of a fault (noise) pulse at a failsafe digital
input that does not change the drive state.

**Note:**
  
The debounce time is rounded to whole milliseconds.  
Example:  
Debounce time = 1 ms: Fault pulses of 1 ms are tolerated; only pulses longer than
2 ms result in a response.  
Debounce time = 3 ms: Fault pulses of 3 ms are tolerated; only pulses longer than
4 ms result in a response.  
The set debounce time impacts the response time of the safety function.

### p9652 SI SS1 delay time

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 [s] | 300.00 [s] | [ 0 ] 0.00 [s] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the delay time of the pulse suppression for the "Safe Stop 1" (SS1) function
to brake along the OFF3 down ramp (p1135).

**Recommend.:**
  
In order that the drive can completely ramp-down along the OFF3 ramp and a motor holding
brake that is possibly available can close, then the delay time should be set as follows:  
Motor holding brake parameterized: delay time &gt;= p1135 + p1228 + p1217  
Motor holding brake not parameterized: delay time &gt;= p1135 + p1228

**Dependency:**
  
  
Refer to:
p1135

**Note:**
  
For a stop response SS1 set for PROFIsafe failure (p9612 = 1), pulse cancellation
after failure of PROFIsafe communication is delayed by this time.  
SS1: Safe Stop 1

## SINAMICS Parameter SINAMICS S210 09653 - 20063

SINAMICS Parameter SINAMICS S210 09653 - 20063

### p9653 SI SS1 drive-based braking response

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 1 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the drive-based braking response for the "SS1" function.  
In the factory setting, SS1 uses the OFF3 ramp.

**Value:**
  
0:
SS1 with OFF3  
1:
SS1E external stop

**Note:**
  
For p9653 = 1, a switchover is made from SS1 to SS1E - and the SS1 response is transferred
to the control system.  
SS1E requires the externally initiated stop in order to be in conformance with stop
Category 1 according to EN60204.  
SS1: Safe Stop 1  
SS1E: Safe Stop 1 external (Safe Stop 1 with external stop)

### p9658 SI transition time F01611 to STO

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 [ms] | 30000.00 [ms] | [ 0 ] 0.00 [ms] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the transition time from F01611 to STO.

**Dependency:**
  
  
Refer to:
r9795  
Refer to:
F01611

**Note:**
  
The set time is rounded internally to an integer multiple of the monitoring clock
cycle.  
STO: Safe Torque Off

### p9659 SI forced checking procedure timer

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 [h] | 9000.00 [h] | [ 0 ] 8760.00 [h] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Setting the time interval in order to test Safe Torque Off (STO).  
During the test, within the parameterized time, an STO is selected and then again
deselected, e.g. by activating and deactivating Emergency Stop.  
The monitoring time in r9660 is reset each time that STO is deselected.

**Dependency:**
  
  
Refer to:
A01699

**Note:**
  
STO: Safe Torque Off

### r9660 SI forced checking procedure remaining time

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [h] | - [h] | [ ] - [h] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the remaining time until the next forced checking procedure of the safety
functions.

**Dependency:**
  
  
Refer to:
A01699

### p9670 SI module identification drive

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**- | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 4294967295 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Safety Integrated module identifier for the drive.  
Replacement of the drive is identified when the safety functions are activated.

**Dependency:**
  
  
Refer to:
F01641

**Note:**
  
After replacement, when the drive powers up a fault is output.

### p9673 SI module identifier motor encoder evaluation

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 4294967295 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Safety Integrated module identifier for the encoder in the motor.  
Replacement of the motor is identified when the safety functions are activated.

**Dependency:**
  
  
Refer to:
F01641

**Note:**
  
After replacement, when the drive powers up a fault is output.

### p9675 SI module identifier motor encoder

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 4294967295 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Safety Integrated module identifier for the encoder in the motor.  
Replacement of the motor is identified when the safety functions are activated.

**Dependency:**
  
  
Refer to:
F01641

**Note:**
  
After replacement, when the drive powers up a fault is output.

### p9702 SI Acknowledge component replacement

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 29 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Setting to acknowledge that a component has been replaced.  
By writing 29 to this parameter, the unique identifier of a safety-relevant component
is transferred into the drive parameterization.

**Value:**
  
0:
[00 hex] hardware replacement acknowledge ready  
29:
[1D hex] hardware replacement acknowledgment

**Notice:**
  
It is not permissible that the safety commissioning mode is set in order to write
to this parameter.

**Note:**
  
After successful execution, this parameter is automatically reset to zero.  
Parameters must be saved.  
The parameter cannot be written to using a project download, and cannot be set in
an offline project.

### r9708[0...5] SI Motion diagnostics safe position

[S210](#r970805-si-motion-diagnostics-safe-position-1)

[S210 Safety rotary axis](#r970805-si-motion-diagnostics-safe-position-2)

#### r9708[0...5] SI Motion diagnostics safe position

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [mm] | - [mm] | [ ] - [mm] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the actual load-side actual values of both monitoring channels and their
difference.

**Index:**
  
[
0]:
Load-side actual value on the CU  
[
1]:
Load-side actual value on the second channel  
[
2]:
Load-side actual value difference CU - second channel  
[
3]:
Load-side max. actual value difference CU - second channel  
[
4]:
Reserved  
[
5]:
Reserved

**Dependency:**
  
  
Refer to:
r9713

**Note:**
  
For index [0]:  
The display of the load-side position actual value on the first channel is updated
in the monitoring clock cycle.  
For index [1]:  
The display of the load-side position actual value on the second channel is updated
in the KDV clock cycle (r9724) and delayed by one KDV clock cycle.  
For index [2]:  
The difference between the load-side position actual value in the first channel and
load-side position actual value in the second channel is updated in the KDV clock
cycle (r9724) and delayed by one KDV clock cycle.  
For index [3]:  
The maximum difference between the load-side position actual value in the first channel
and the load-side position actual value in the second channel.  
KDV: Data cross-check

#### r9708[0...5] SI Motion diagnostics safe position

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 (Safety rot) | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [°] | - [°] | [ ] - [°] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the actual load-side actual values of both monitoring channels and their
difference.

**Index:**
  
[
0]:
Load-side actual value on the CU  
[
1]:
Load-side actual value on the second channel  
[
2]:
Load-side actual value difference CU - second channel  
[
3]:
Load-side max. actual value difference CU - second channel  
[
4]:
Reserved  
[
5]:
Reserved

**Dependency:**
  
  
Refer to:
r9713

**Note:**
  
For index [0]:  
The display of the load-side position actual value on the first channel is updated
in the monitoring clock cycle.  
For index [1]:  
The display of the load-side position actual value on the second channel is updated
in the KDV clock cycle (r9724) and delayed by one KDV clock cycle.  
For index [2]:  
The difference between the load-side position actual value in the first channel and
load-side position actual value in the second channel is updated in the KDV clock
cycle (r9724) and delayed by one KDV clock cycle.  
For index [3]:  
The maximum difference between the load-side position actual value in the first channel
and the load-side position actual value in the second channel.  
KDV: Data cross-check

### r9710[0...1] SI Motion diagnostics result list 1

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays result list 1 that, for the data cross-check between the monitoring channels,
led to the fault.

**Index:**
  
[
0]:
Result list channel 2  
[
1]:
Result list channel 1

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Actual value &gt; upper limit SOS | No | Yes | - |
| 01 | Actual value &gt; lower limit SOS | No | Yes | - |
| 06 | Actual value &gt; upper limit SLS1 | No | Yes | - |
| 07 | Actual value &gt; lower limit SLS1 | No | Yes | - |
| 08 | Actual value &gt; upper limit SLS2 | No | Yes | - |
| 09 | Actual value &gt; lower limit SLS2 | No | Yes | - |
| 10 | Actual value &gt; upper limit SLS3 | No | Yes | - |
| 11 | Actual value &gt; lower limit SLS3 | No | Yes | - |
| 12 | Actual value &gt; upper limit SLS4 | No | Yes | - |
| 13 | Actual value &gt; lower limit SLS4 | No | Yes | - |
| 14 | Actual value &gt; upper limit test stop | No | Yes | - |
| 15 | Actual value &gt; lower limit test stop | No | Yes | - |
| 16 | Actual value &gt; upper limit SAM/SBR | No | Yes | - |
| 17 | Actual value &gt; lower limit SAM/SBR | No | Yes | - |
| 18 | Actual value &gt; upper limit SDI positive | No | Yes | - |
| 19 | Actual value &gt; lower limit SDI positive | No | Yes | - |
| 20 | Actual value &gt; upper limit SDI negative | No | Yes | - |
| 21 | Actual value &gt; lower limit SDI negative | No | Yes | - |
| 22 | Actual value &gt; upper limit SLA1 | No | Yes | - |
| 23 | Actual value &gt; lower limit SLA1 | No | Yes | - |
| 24 | Actual value &gt; fine upper limit SLA1 | No | Yes | - |
| 25 | Actual value &gt; fine lower limit SLA1 | No | Yes | - |

**Dependency:**
  
  
Refer to:
A01711

**Note:**
  
SBR: Safe Brake Ramp (safe brake ramp monitoring)  
SDI: Safe Direction (safe motion direction)  
SLA: Safely-Limited Acceleration  
SLS: Safely-Limited Speed  
SOS: Safe Operating Stop

### r9711[0...1] SI Motion diagnostics result list 2

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays result list 2 that, for the data cross-check between the monitoring channels,
led to the fault.

**Index:**
  
[
0]:
Result list channel 2  
[
1]:
Result list channel 1

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 16 | Actual value &gt; upper limit SSM+ | No | Yes | - |
| 17 | Actual value &gt; lower limit SSM+ | No | Yes | - |
| 18 | Actual value &gt; upper limit SSM- | No | Yes | - |
| 19 | Actual value &gt; lower limit SSM- | No | Yes | - |
| 20 | Actual value &gt; upper limit modulo | No | Yes | - |
| 21 | Actual value &gt; lower limit modulo | No | Yes | - |

**Dependency:**
  
  
Refer to:
A01711

**Note:**
  
SSM: Safe Speed Monitor (safety-relevant feedback signal from the speed monitoring)

### r9712 SI Motion diagnostics position actual value motor side

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the position actual value on the motor side for motion monitoring functions.

**Note:**
  
The display is updated in the safety monitoring clock cycle.

### r9713[0...5] SI Motion diagnostics position actual value load side

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the actual load-side actual values of both monitoring channels and their
difference.

**Index:**
  
[
0]:
Load-side actual value on the CU  
[
1]:
Load-side actual value on the second channel  
[
2]:
Load-side actual value difference CU - second channel  
[
3]:
Load-side max. actual value difference CU - second channel  
[
4]:
Reserved  
[
5]:
Reserved

**Dependency:**
  
  
Refer to:
r9708

**Note:**
  
Regarding the units, this parameter should be interpreted as follows:  
- linear axis: µm  
- rotary axis: mdegrees  
The value of this parameter is displayed in r9708 with units (mm or degrees).  
The display is updated in the safety monitoring clock cycle.  
For index [0]:  
The display of the load-side position actual value on the first channel is updated
in the monitoring clock cycle.  
For index [1]:  
The display of the load-side position actual value on the second channel is updated
in the KDV clock cycle (r9724) and delayed by one KDV clock cycle.  
For index [2]:  
The difference between the load-side position actual value in the first channel and
load-side position actual value in the second channel is updated in the KDV clock
cycle (r9724) and delayed by one KDV clock cycle.  
For index [3]:  
The maximum difference between the load-side position actual value in the first channel
and the load-side position actual value in the second channel.  
KDV: Data cross-check

### r9714[0...3] SI motion diagnostics velocity

[S210](#r971403-si-motion-diagnostics-velocity-1)

[S210 Safety rotary axis](#r971403-si-motion-diagnostics-velocity-2)

#### r9714[0...3] SI motion diagnostics velocity

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [mm/min] | - [mm/min] | [ ] - [mm/min] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the velocity actual values for motion monitoring functions.

**Index:**
  
[
0]:
Load side speed actual value  
[
1]:
Actual SAM/SBR speed limit  
[
2]:
Actual SLS speed limit  
[
3]:
Actual SLA velocity limit

**Note:**
  
The display is updated in the safety monitoring clock cycle.  
For linear axes, the following unit applies: millimeters per minute  
For rotary axes, the following unit applies: revolutions per minute

#### r9714[0...3] SI motion diagnostics velocity

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 (Safety rot) | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [rpm] | - [rpm] | [ ] - [rpm] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the velocity actual values for motion monitoring functions.

**Index:**
  
[
0]:
Load side speed actual value  
[
1]:
Actual SAM/SBR speed limit  
[
2]:
Actual SLS speed limit  
[
3]:
Actual SLA velocity limit

**Note:**
  
The display is updated in the safety monitoring clock cycle.  
For linear axes, the following unit applies: millimeters per minute  
For rotary axes, the following unit applies: revolutions per minute

### r9720.0...28 SI Motion control signals integrated in the drive

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Control signals for safety-relevant motion monitoring functions integrated in the
drive.

**Bit field:**

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
| 28 | Deselect SS2E | No | Yes | - |

**Note:**
  
This parameter is only supplied with actual values in the case of Safety Integrated
Extended Functions. For Safety Integrated Basic Functions (SBC, SS1, STO), the value
is equal to zero.

### r9722.0...28 SI Motion drive-integrated status signals

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Status signal for safety-relevant motion monitoring functions integrated in the drive.

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | STO or safe pulse suppression active | No | Yes | - |
| 01 | SS1 active | No | Yes | - |
| 02 | SS2 active | No | Yes | - |
| 03 | SOS active | No | Yes | - |
| 04 | SLS active | No | Yes | - |
| 07 | Internal event | Yes | No | - |
| 08 | SLA active | No | Yes | 2838 |
| 09 | Active SLS stage bit 0 | Not set | Set | - |
| 10 | Active SLS stage bit 1 | Not set | Set | - |
| 11 | SOS selected | No | Yes | - |
| 12 | SDI positive active | No | Yes | 2824 |
| 13 | SDI negative active | No | Yes | 2824 |
| 15 | SSM (speed below limit value) | No | Yes | 2823 |
| 28 | SS2E active | No | Yes | - |

**Dependency:**
  
  
Refer to:
p9501

**Notice:**
  
For bit 07:  
The signal state behaves in an opposite way to the PROFIsafe Standard.

**Note:**
  
This parameter is only supplied with actual values in the case of Safety Integrated
Extended Functions.  
For Safety Integrated Basic Functions (SBC, SS1, STO), the value is equal to zero.  
For bit 07:  
An internal event is displayed if a fault response STO, SS1, SS2, SS2E, A01711 is
active.  
For bit 15:  
This bit is only supplied for activated SSM hysteresis and filtering (p9501.16 = 1).

### r9723.0...16 SI Motion diagnostic signals integrated in the drive

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the diagnostic signals for safety-relevant motion monitoring functions integrated
in the drive.

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Forced checking procedure required | No | Yes | - |
| 01 | A01711 and then SS1 becomes active | No | Yes | 2819 |
| 02 | Communication failure delay time active | No | Yes | - |
| 03 | Actual value sensing supplies valid value | No | Yes | 2821 |
| 12 | Test stop active | No | Yes | - |
| 16 | SAM/SBR active | No | Yes | 2820 |

**Note:**
  
For bit 00:  
A required dynamization is also displayed via alarm A01679.  
For bit 01:  
This bit can be used to execute a control-managed response (e.g. emergency retraction).  
For bit 02:  
This bit is set if communication fails and the delay time of the stop response is
running.  
For bit 12:  
Test stop active, is also displayed using message A01798.  
SAM: Safe Acceleration Monitor (safe acceleration monitoring)  
SBR: Safe Brake Ramp (safe brake ramp monitoring)

### r9725[0...2] SI Motion diagnostics A01711

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
For index [0]:  
Displays the message value that resulted in message A01711 at the drive.  
Value = 0:  
Message A01711 was communicated from the first channel.  
Value = 1 ... 999:  
Number of the incorrect date in the data cross-check between the monitoring channels.  
Value &gt;= 1000:  
Additional diagnostic values of the drive.  
For index [1]:  
Displays the value from the first channel that resulted in message A01711.  
For index [2]:  
Displays the value from the second channel that resulted in message A01711.

**Index:**
  
[
0]:
Message value for KDV  
[
1]:
Channel 1 KDV actual value  
[
2]:
Channel 2 KDV actual value

**Dependency:**
  
  
Refer to:
A01711

**Note:**
  
The significance of the individual message values is described in message A01711.  
KDV: Data cross-check  
For index [1, 2]:  
When message A01711 is output with message value &gt;= 1000, then these indices are not
supplied with values.

### r9733[0...2] SI Motion setpoint speed limit effective

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**p2000 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [rpm] | - [rpm] | [ ] - [rpm] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the necessary setpoint speed limit as a result of the selected motion monitoring
functions.  
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
[x] = Selected SLS stage  
Conversion factor from the motor side to the load side:  
- motor type = rotary and axis type = linear: p9522 / (p9521 x p9520)  
- otherwise: p9522 / p9521  
  
Refer to:
p9531, p9533

**Note:**
  
This parameter is not influenced by setting the axis type (p9502).  
If the "SLS" or "SDI" function is not selected, r9733[0] shows p1082 and r9733[1]
shows -p1082.  
The display in r9733 can be delayed by up to one Safety monitoring clock cycle as
compared to the display in r9719/r9720 and r9721/r9722.  
When SOS is selected or an STO, SS1, SS2, SS2E, a setpoint of 0 is entered in r9733.

### r9734.0...15 SI Safety Information Channel status word S_ZSW1B

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Display for the status word of safety functions (S_ZSW1B).

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | STO active | No | Yes | - |
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
| 15 | Safety message present | No | Yes | - |

**Note:**
  
For bit 07:  
An internal event is displayed if a fault response STO, SS1, SS2, SS2E, A01711 is
active.

### r9743.8...13 SI Safety Information Channel status word S_ZSW2B

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Display for the status word of the safety functions (S_ZSW2B).

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 08 | SDI positive selected | No | Yes | - |
| 09 | SDI negative selected | No | Yes | - |
| 12 | Test stop active | No | Yes | - |
| 13 | Test stop required | No | Yes | - |

### r9753[0...63] SI message value for float values

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.2

**Description:**
  
Displays additional information about the safety message that has occurred for float
values.

### r9754[0...63] SI message time received in days

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.2

**Description:**
  
Displays the relative system runtime in days when the safety message occurred.

### r9755[0...63] SI message time removed in milliseconds

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [ms] | - [ms] | [ ] - [ms] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.2

**Description:**
  
Displays the relative system runtime in milliseconds when the safety message was removed.

### r9756[0...63] SI message time removed in days

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.2

**Description:**
  
Displays the relative system runtime in days when the safety message was removed.

### r9765 SI Motion forced checking procedure remaining time

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [h] | - [h] | [ ] - [h] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the time remaining until the next dynamization and testing of the safety
motion monitoring functions integrated in the drives.  
The signal source to initiate the forced checking procedure is parameterized in p9705.

**Dependency:**
  
  
Refer to:
A01798

### r9767.0...1 SI Safety password status

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Display and binector output for the status of the safety password.

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Assign password | No | Yes | - |
| 01 | Password entered | No | Yes | - |

**Note:**
  
For bit 00 = 1:  
- a valid safety password was assigned.  
For bit 01 = 1:  
- a valid safety password was assigned (bit 0 = 1).  
- safety parameters can be set.

### r9768[0...7] Receive SI PROFIsafe control words

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the received PROFIsafe telegram from the control.

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

**Dependency:**
  
  
Refer to:
r9769

**Note:**
  
The PROFIsafe trailer at the end of the telegram is also displayed (2 words).

### r9769[0...7] Send SI PROFIsafe status words

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the PROFIsafe telegram to be sent to the control.

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

**Dependency:**
  
  
Refer to:
r9768

**Note:**
  
The PROFIsafe trailer at the end of the telegram is also displayed (2 words).

### r9770[0...3] SI version safety functions integrated in the drive

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the Safety Integrated version for the drive-integrated safety functions

**Index:**
  
[
0]:
Safety Version (major release)  
[
1]:
Safety Version (minor release)  
[
2]:
Safety Version (baselevel or patch)  
[
3]:
Safety Version (hotfix)

**Note:**
  
Example:  
r9770[0] = 5, r9770[1] = 10, r9770[2] = 1, r9770[3] = 0 --&gt; safety version V05.10.01.00

### r9776.0...3 SI diagnostics

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the operating state, referred to the safety functions.

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Safety parameter changed POWER ON required | No | Yes | - |
| 01 | Safety functions enabled | No | Yes | - |
| 02 | Safety component replaced and data save required | No | Yes | - |
| 03 | Safety component replaced and acknowledge/save required | No | Yes | - |

**Note:**
  
For bit 00 = 1:  
At least one Safety parameter has been changed that will only take effect after a
POWER ON.  
For bit 01 = 1:  
Safety functions (basic functions or extended functions) have been enabled and are
active.  
For bit 02 = 1:  
A safety-relevant component has been replaced. Saving required (p0977 = 1).  
For bit 03 = 1:  
A safety-relevant component has been replaced. Acknowledging (p9702 = 29) and saving
(p0977 = 1) required.

### r9781[0...1] SI checksum to check changes

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the checksum to track changes for safety functions.

**Index:**
  
[
0]:
SI checksum to track functional changes  
[
1]:
SI checksum to track hardware-specific changes

**Dependency:**
  
  
Refer to:
p9601  
Refer to:
F01690

**Note:**
  
The checksum changes when configuring safety functions.

### r9782[0...1] SI change control time stamp

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [h] | - [h] | [ ] - [h] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the time stamps for the checksums for tracking changes for safety functions.  
Each new checksum is assigned a time stamp (r9781).

**Index:**
  
[
0]:
SI time stamp for checksum to track functional changes  
[
1]:
SI time stamp for checksum to track hardware-specific changes

**Dependency:**
  
  
Refer to:
p9601  
Refer to:
F01690

### r9790[0...1] SI Motion SLA acceleration resolution

[S210](#r979001-si-motion-sla-acceleration-resolution-1)

[S210 Safety rotary axis](#r979001-si-motion-sla-acceleration-resolution-2)

#### r9790[0...1] SI Motion SLA acceleration resolution

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [m/s²] | - [m/s²] | [ ] - [m/s²] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.2

**Description:**
  
Displays the acceleration resolution (load side) for the "SLA" function.  
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
sensing. This depends on the type of actual value sensing, the gearbox ratios as well
as the quality of the encoder being used.  
Conversion from internal fixed values to m/s² (linear) or 1/s² (rotary).  
Dependent on the task type, the following is obtained:  
r9790[0] = 0.0625 m/s² (linear) or 0.173611 1/s² (rotary)  
r9790[1] = 0.0000625 m/s² (linear) or 0.0001736 1/s² (rotary)  
SLA: Safely-Limited Acceleration

#### r9790[0...1] SI Motion SLA acceleration resolution

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 (Safety rot) | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [rev/s²] | - [rev/s²] | [ ] - [rev/s²] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.2

**Description:**
  
Displays the acceleration resolution (load side) for the "SLA" function.  
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
sensing. This depends on the type of actual value sensing, the gearbox ratios as well
as the quality of the encoder being used.  
Conversion from internal fixed values to m/s² (linear) or 1/s² (rotary).  
Dependent on the task type, the following is obtained:  
r9790[0] = 0.0625 m/s² (linear) or 0.173611 1/s² (rotary)  
r9790[1] = 0.0000625 m/s² (linear) or 0.0001736 1/s² (rotary)  
SLA: Safely-Limited Acceleration

### r9795 SI diagnostics F01611

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**2 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the number of the cross-checked data, which resulted in fault F01611.

**Dependency:**
  
  
Refer to:
F01611

**Note:**
  
A complete list of numbers for cross-checked data items appears in fault F01611.

### p10201 SI Motion SBT enable

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0000 bin |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the enable for the safe brake test.

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Enable safe brake test | No | Yes | - |

**Note:**
  
SBT: Safe Brake Test

### p10202[0...1] SI Motion SBT brake

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 1 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Selecting the brake to be tested.  
p10202[0] must be set = 1 to test the brake.

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
  
  
Refer to:
A01785

### p10208[0...1] SI Motion SBT test torque ramp time

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 20 [ms] | 10000 [ms] | [ 0 ] 1000 [ms] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

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

### p10209[0...1] SI Motion SBT brake holding torque

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.05 [Nm] | 60000.00 [Nm] | [ 0 ] 10.00 [Nm] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

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
  
  
Refer to:
p10210, p10220

**Note:**
  
The test torque effective for the brake test can be set for each sequence using a
factor (p10210, p10220).

### p10210[0...1] SI Motion SBT test torque factor sequence 1

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.30 | 1.00 | [ 0 ] 1.00 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

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
  
  
Refer to:
p10209

### p10211[0...1] SI Motion SBT test duration sequence 1

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 20 [ms] | 10000 [ms] | [ 0 ] 1000 [ms] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

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

**Note:**
  
The set time is rounded internally to an integer multiple of the monitoring clock
cycle.

### p10212[0...1] SI Motion SBT position tolerance sequence 1

[S210](#p1021201-si-motion-sbt-position-tolerance-sequence-1-1)

[S210 Safety rotary axis](#p1021201-si-motion-sbt-position-tolerance-sequence-1-2)

#### p10212[0...1] SI Motion SBT position tolerance sequence 1

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.001 [mm] | 360.000 [mm] | [ 0 ] 1.000 [mm] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the tolerated position deviation for sequence 1 for the safe brake test.

**Index:**
  
[
0]:
Brake 1  
[
1]:
Reserved

#### p10212[0...1] SI Motion SBT position tolerance sequence 1

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 (Safety rot) | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.001 [°] | 360.000 [°] | [ 0 ] 1.000 [°] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the tolerated position deviation for sequence 1 for the safe brake test.

**Index:**
  
[
0]:
Brake 1  
[
1]:
Reserved

### p10220[0...1] SI Motion SBT test torque factor sequence 2

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.30 | 1.00 | [ 0 ] 1.00 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

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
  
  
Refer to:
p10209

### p10221[0...1] SI Motion SBT test duration sequence 2

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 20 [ms] | 10000 [ms] | [ 0 ] 1000 [ms] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

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

**Note:**
  
The set time is rounded internally to an integer multiple of the monitoring clock
cycle.

### p10222[0...1] SI Motion SBT position tolerance sequence 2

[S210](#p1022201-si-motion-sbt-position-tolerance-sequence-2-1)

[S210 Safety rotary axis](#p1022201-si-motion-sbt-position-tolerance-sequence-2-2)

#### p10222[0...1] SI Motion SBT position tolerance sequence 2

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.001 [mm] | 360.000 [mm] | [ 0 ] 1.000 [mm] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the tolerated position deviation for sequence 2 for the safe brake test.

**Index:**
  
[
0]:
Brake 1  
[
1]:
Reserved

#### p10222[0...1] SI Motion SBT position tolerance sequence 2

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 95) | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 (Safety rot) | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.001 [°] | 360.000 [°] | [ 0 ] 1.000 [°] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the tolerated position deviation for sequence 2 for the safe brake test.

**Index:**
  
[
0]:
Brake 1  
[
1]:
Reserved

### r10231 SI Motion SBT control word diagnostics

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the diagnostic bits for the control word of the safe brake test

**Bit field:**

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
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Display for the status word of the safety functions (S_ZSW3B).

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Brake test selected | No | Yes | - |
| 01 | Setpoint input drive/external | External | Drive | - |
| 03 | Brake test active | No | Yes | - |
| 04 | Brake test result | Erroneous/not | Successful | - |
| 05 | Brake test completed | No | Yes | - |
| 07 | Actual load sign | Positive | Negative | - |
| 11 | SS2E active | No | Yes | - |
| 15 | Acceptance test mode selected | No | Yes | - |

**Note:**
  
SS2E: Safe Stop 2 External (Safe Stop 2 with external stop)  
For bits 05, 04:  
For r10234.4 = 0 signal, it is possible to make a distinction as to whether the brake
test was executed with error - or has still not been executed - using bit 5.  
Bit 5/4 = 0/0: The brake test has still not been executed since the last warm restart
or POWER ON.  
Bit 5/4 = 1/0: The last brake test that was executed had an error.

### r10240 SI Motion SBT test torque diagnostics

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [Nm] | - [Nm] | [ ] - [Nm] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the effective maximum test torque on the motor side for a safe brake test.

**Dependency:**
  
  
Refer to:
p10210, p10220

**Note:**
  
The value remains displayed until the start of the next test sequence.

### r10241 SI Motion SBT load torque diagnostics

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [Nm] | - [Nm] | [ ] - [Nm] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the load torque for a safe brake test.  
When initializing the brake test, this load torque is available at the drive.

**Note:**
  
The value remains displayed until the brake test is deselected.

### r10242 SI Motion SBT state diagnostics

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 16 | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

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

### r10251.8...13 SI Safety Control Channel control word S_STW1B diagnostics

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**- | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.2

**Description:**
  
Displays the diagnostics of control word S_STW1 of the Safety Control Channel.

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 08 | Extended Functions test stop selection | Not selected | Selected | 2837 |
| 12 | Extended Functions, premature SOS after SS2E | Not selected | Selected | - |
| 13 | Close brake from control | Not selected | Selected | - |

**Note:**
  
SCC: Safety Control Channel  
For bit 13:  
The following BICO interconnection is required for brake control via SCC:  
BI: p0858 = r10251.13

### p20000[0...9] Runtime group property

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 9003 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Allocates properties to runtime groups 0 to 9.  
This property comprises the sampling time and for p20000[x] = 9003, the instant of
the call within the sampling time.  
Index x of p20000 corresponds to the number of the runtime group.  
p20000[0] is used to set the property of runtime group 0.  
...  
p20000[9] is used to set the property of runtime group 9.  
  
p20000[x] = 0 runtime group is not calculated.  
p20000[x] = 1 free runtime group T_sample = 1 * r20002  
p20000[x] = 2 free runtime group T_sample = 2 * r20002  
p20000[x] = 3 free runtime group T_sample = 3 * r20002  
p20000[x] = 4 free runtime group T_sample = 4 * r20002  
...  
p20000[x] = 255 free runtime group T_sample = 255 * r20002  
p20000[x] = 256 free runtime group T_sample = 256 * r20002  
p20000[x] = 1001 free runtime group T_sample = 1 * r20003  
p20000[x] = 1002 free runtime group T_sample = 2 * r20003  
p20000[x] = 1003 free runtime group T_sample = 3 * r20003  
p20000[x] = 1004 free runtime group T_sample = 4 * r20003  
p20000[x] = 1005 free runtime group T_sample = 5 * r20003  
p20000[x] = 1006 free runtime group T_sample = 6 * r20003  
p20000[x] = 1008 free runtime group T_sample = 8 * r20003  
p20000[x] = 1010 free runtime group T_sample = 10 * r20003  
p20000[x] = 1012 free runtime group T_sample = 12 * r20003  
p20000[x] = 1016 free runtime group T_sample = 16 * r20003  
p20000[x] = 1020 free runtime group T_sample = 20 * r20003  
p20000[x] = 1024 free runtime group T_sample = 24 * r20003  
p20000[x] = 1032 free runtime group T_sample = 32 * r20003  
p20000[x] = 1040 free runtime group T_sample = 40 * r20003  
p20000[x] = 1048 free runtime group T_sample = 48 * r20003  
p20000[x] = 1064 free runtime group T_sample = 64 * r20003  
p20000[x] = 1096 free runtime group T_sample = 96 * r20003  
p20000[x] = 9003 fixed runtime group "calculate before setpoint channel" (only VECTOR,
SERVO)

**Value:**
  
0:
Do not calculate  
1:
T = 1 * r20002  
2:
T = 2 * r20002  
3:
T = 3 * r20002  
4:
T = 4 * r20002  
5:
T = 5 * r20002  
6:
T = 6 * r20002  
7:
T = 7 * r20002  
8:
T = 8 * r20002  
9:
T = 9 * r20002  
10:
T = 10 * r20002  
11:
T = 11 * r20002  
12:
T = 12 * r20002  
13:
T = 13 * r20002  
14:
T = 14 * r20002  
15:
T = 15 * r20002  
16:
T = 16 * r20002  
17:
T = 17 * r20002  
18:
T = 18 * r20002  
19:
T = 19 * r20002  
20:
T = 20 * r20002  
21:
T = 21 * r20002  
22:
T = 22 * r20002  
23:
T = 23 * r20002  
24:
T = 24 * r20002  
25:
T = 25 * r20002  
26:
T = 26 * r20002  
27:
T = 27 * r20002  
28:
T = 28 * r20002  
29:
T = 29 * r20002  
30:
T = 30 * r20002  
31:
T = 31 * r20002  
32:
T = 32 * r20002  
33:
T = 33 * r20002  
34:
T = 34 * r20002  
35:
T = 35 * r20002  
36:
T = 36 * r20002  
37:
T = 37 * r20002  
38:
T = 38 * r20002  
39:
T = 39 * r20002  
40:
T = 40 * r20002  
41:
T = 41 * r20002  
42:
T = 42 * r20002  
43:
T = 43 * r20002  
44:
T = 44 * r20002  
45:
T = 45 * r20002  
46:
T = 46 * r20002  
47:
T = 47 * r20002  
48:
T = 48 * r20002  
49:
T = 49 * r20002  
50:
T = 50 * r20002  
51:
T = 51 * r20002  
52:
T = 52 * r20002  
53:
T = 53 * r20002  
54:
T = 54 * r20002  
55:
T = 55 * r20002  
56:
T = 56 * r20002  
57:
T = 57 * r20002  
58:
T = 58 * r20002  
59:
T = 59 * r20002  
60:
T = 60 * r20002  
61:
T = 61 * r20002  
62:
T = 62 * r20002  
63:
T = 63 * r20002  
64:
T = 64 * r20002  
65:
T = 65 * r20002  
66:
T = 66 * r20002  
67:
T = 67 * r20002  
68:
T = 68 * r20002  
69:
T = 69 * r20002  
70:
T = 70 * r20002  
71:
T = 71 * r20002  
72:
T = 72 * r20002  
73:
T = 73 * r20002  
74:
T = 74 * r20002  
75:
T = 75 * r20002  
76:
T = 76 * r20002  
77:
T = 77 * r20002  
78:
T = 78 * r20002  
79:
T = 79 * r20002  
80:
T = 80 * r20002  
81:
T = 81 * r20002  
82:
T = 82 * r20002  
83:
T = 83 * r20002  
84:
T = 84 * r20002  
85:
T = 85 * r20002  
86:
T = 86 * r20002  
87:
T = 87 * r20002  
88:
T = 88 * r20002  
89:
T = 89 * r20002  
90:
T = 90 * r20002  
91:
T = 91 * r20002  
92:
T = 92 * r20002  
93:
T = 93 * r20002  
94:
T = 94 * r20002  
95:
T = 95 * r20002  
96:
T = 96 * r20002  
97:
T = 97 * r20002  
98:
T = 98 * r20002  
99:
T = 99 * r20002  
100:
T = 100 * r20002  
101:
T = 101 * r20002  
102:
T = 102 * r20002  
103:
T = 103 * r20002  
104:
T = 104 * r20002  
105:
T = 105 * r20002  
106:
T = 106 * r20002  
107:
T = 107 * r20002  
108:
T = 108 * r20002  
109:
T = 109 * r20002  
110:
T = 110 * r20002  
111:
T = 111 * r20002  
112:
T = 112 * r20002  
113:
T = 113 * r20002  
114:
T = 114 * r20002  
115:
T = 115 * r20002  
116:
T = 116 * r20002  
117:
T = 117 * r20002  
118:
T = 118 * r20002  
119:
T = 119 * r20002  
120:
T = 120 * r20002  
121:
T = 121 * r20002  
122:
T = 122 * r20002  
123:
T = 123 * r20002  
124:
T = 124 * r20002  
125:
T = 125 * r20002  
126:
T = 126 * r20002  
127:
T = 127 * r20002  
128:
T = 128 * r20002  
129:
T = 129 * r20002  
130:
T = 130 * r20002  
131:
T = 131 * r20002  
132:
T = 132 * r20002  
133:
T = 133 * r20002  
134:
T = 134 * r20002  
135:
T = 135 * r20002  
136:
T = 136 * r20002  
137:
T = 137 * r20002  
138:
T = 138 * r20002  
139:
T = 139 * r20002  
140:
T = 140 * r20002  
141:
T = 141 * r20002  
142:
T = 142 * r20002  
143:
T = 143 * r20002  
144:
T = 144 * r20002  
145:
T = 145 * r20002  
146:
T = 146 * r20002  
147:
T = 147 * r20002  
148:
T = 148 * r20002  
149:
T = 149 * r20002  
150:
T = 150 * r20002  
151:
T = 151 * r20002  
152:
T = 152 * r20002  
153:
T = 153 * r20002  
154:
T = 154 * r20002  
155:
T = 155 * r20002  
156:
T = 156 * r20002  
157:
T = 157 * r20002  
158:
T = 158 * r20002  
159:
T = 159 * r20002  
160:
T = 160 * r20002  
161:
T = 161 * r20002  
162:
T = 162 * r20002  
163:
T = 163 * r20002  
164:
T = 164 * r20002  
165:
T = 165 * r20002  
166:
T = 166 * r20002  
167:
T = 167 * r20002  
168:
T = 168 * r20002  
169:
T = 169 * r20002  
170:
T = 170 * r20002  
171:
T = 171 * r20002  
172:
T = 172 * r20002  
173:
T = 173 * r20002  
174:
T = 174 * r20002  
175:
T = 175 * r20002  
176:
T = 176 * r20002  
177:
T = 177 * r20002  
178:
T = 178 * r20002  
179:
T = 179 * r20002  
180:
T = 180 * r20002  
181:
T = 181 * r20002  
182:
T = 182 * r20002  
183:
T = 183 * r20002  
184:
T = 184 * r20002  
185:
T = 185 * r20002  
186:
T = 186 * r20002  
187:
T = 187 * r20002  
188:
T = 188 * r20002  
189:
T = 189 * r20002  
190:
T = 190 * r20002  
191:
T = 191 * r20002  
192:
T = 192 * r20002  
193:
T = 193 * r20002  
194:
T = 194 * r20002  
195:
T = 195 * r20002  
196:
T = 196 * r20002  
197:
T = 197 * r20002  
198:
T = 198 * r20002  
199:
T = 199 * r20002  
200:
T = 200 * r20002  
201:
T = 201 * r20002  
202:
T = 202 * r20002  
203:
T = 203 * r20002  
204:
T = 204 * r20002  
205:
T = 205 * r20002  
206:
T = 206 * r20002  
207:
T = 207 * r20002  
208:
T = 208 * r20002  
209:
T = 209 * r20002  
210:
T = 210 * r20002  
211:
T = 211 * r20002  
212:
T = 212 * r20002  
213:
T = 213 * r20002  
214:
T = 214 * r20002  
215:
T = 215 * r20002  
216:
T = 216 * r20002  
217:
T = 217 * r20002  
218:
T = 218 * r20002  
219:
T = 219 * r20002  
220:
T = 220 * r20002  
221:
T = 221 * r20002  
222:
T = 222 * r20002  
223:
T = 223 * r20002  
224:
T = 224 * r20002  
225:
T = 225 * r20002  
226:
T = 226 * r20002  
227:
T = 227 * r20002  
228:
T = 228 * r20002  
229:
T = 229 * r20002  
230:
T = 230 * r20002  
231:
T = 231 * r20002  
232:
T = 232 * r20002  
233:
T = 233 * r20002  
234:
T = 234 * r20002  
235:
T = 235 * r20002  
236:
T = 236 * r20002  
237:
T = 237 * r20002  
238:
T = 238 * r20002  
239:
T = 239 * r20002  
240:
T = 240 * r20002  
241:
T = 241 * r20002  
242:
T = 242 * r20002  
243:
T = 243 * r20002  
244:
T = 244 * r20002  
245:
T = 245 * r20002  
246:
T = 246 * r20002  
247:
T = 247 * r20002  
248:
T = 248 * r20002  
249:
T = 249 * r20002  
250:
T = 250 * r20002  
251:
T = 251 * r20002  
252:
T = 252 * r20002  
253:
T = 253 * r20002  
254:
T = 254 * r20002  
255:
T = 255 * r20002  
256:
T = 256 * r20002  
1001:
T = 1 * r20003  
1002:
T = 2 * r20003  
1003:
T = 3 * r20003  
1004:
T = 4 * r20003  
1005:
T = 5 * r20003  
1006:
T = 6 * r20003  
1008:
T = 8 * r20003  
1010:
T = 10 * r20003  
1012:
T = 12 * r20003  
1016:
T = 16 * r20003  
1020:
T = 20 * r20003  
1024:
T = 24 * r20003  
1032:
T = 32 * r20003  
1040:
T = 40 * r20003  
1048:
T = 48 * r20003  
1064:
T = 64 * r20003  
1080:
T = 80 * r20003  
1096:
T = 96 * r20003  
9003:
Before setpoint channel

**Index:**
  
[
0]:
Runtime group 0  
[
1]:
Runtime group 1  
[
2]:
Runtime group 2  
[
3]:
Runtime group 3  
[
4]:
Runtime group 4  
[
5]:
Runtime group 5  
[
6]:
Runtime group 6  
[
7]:
Runtime group 7  
[
8]:
Runtime group 8  
[
9]:
Runtime group 9

**Dependency:**
  
  
Refer to:
r20008

**Caution:**
  
The assignment of the properties of the runtime groups should not be changed on drives
in operation as this could result in discontinuous signal transitions depending on
the blocks used. At the 1st arithmetic cycle after the change, the respective internal
initialization value is present at the block connections and in each subsequent cycle
the calculated value is then present.

**Note:**
  
For value = 1 ... 256:  
This value can only be set if, for sampling time T_sample of this runtime group, the
following applies: 1 ms &lt;= T_sample &lt;= r20003. At download, a value that violates
this condition is not rejected, but a permissible equivalent value is set automatically
and fault F50518 is output.  
If value = 9003:  
The fixed runtime groups p20000[x] = 9003 log on with the sampling time of the setpoint
channel, although the sampling time must be at least 1 ms. If, as a result of this
limit, the actual sampling time deviates from the sampling time of the setpoint channel
p0115[3], alarm A20103 is output. Another runtime group with a sampling time &gt;= 1
ms should be selected. "Calculate before setpoint channel" means before function diagrams
3010, 3020, 3030, 3040, etc. are calculated, if the setpoint channel is activated
(p0108.8 = 1). If, e.g. for SERVO, a setpoint channel has not been configured (p0108.8
= 0), then the calculation is made before function diagram 3095.

### r20001[0...9] Runtime group sampling time

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [ms] | - [ms] | [ ] - [ms] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the current sampling time of the runtime group 0 to 9.

**Index:**
  
[
0]:
Runtime group 0  
[
1]:
Runtime group 1  
[
2]:
Runtime group 2  
[
3]:
Runtime group 3  
[
4]:
Runtime group 4  
[
5]:
Runtime group 5  
[
6]:
Runtime group 6  
[
7]:
Runtime group 7  
[
8]:
Runtime group 8  
[
9]:
Runtime group 9

### r20002 Basis sampling time, hardware

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [ms] | - [ms] | [ ] - [ms] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the lowest sampling time effective at this drive object for values 1 to 256
of p20000.  
T_sample = p20000 * r20002

### r20003 Basis sampling time, software

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [ms] | - [ms] | [ ] - [ms] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the sampling time as factor effective on this drive object for values 1001
to 1096 of p20000.  
T_sample = (p20000 - 1000) * r20003

### r20005[0...9] Average computing time load of the runtime groups

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [%] | - [%] | [ ] - [%] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
4.5

**Description:**
  
Share of the average computing time load which the FBLOCKS runtime group contributes
to the overall computing time load for the drive unit (r9976).

**Index:**
  
[
0]:
Runtime group 0  
[
1]:
Runtime group 1  
[
2]:
Runtime group 2  
[
3]:
Runtime group 3  
[
4]:
Runtime group 4  
[
5]:
Runtime group 5  
[
6]:
Runtime group 6  
[
7]:
Runtime group 7  
[
8]:
Runtime group 8  
[
9]:
Runtime group 9

**Note:**
  
The runtime group to be measured has to be logged on (p20000[x] &gt; 0).  
The value for the computation time load is calculated in the drive unit using the
project loaded. As such, the r20005[x] values are not available in the expert list
in SCOUT/STARTER offline mode.

### r20008[0...12] Hardware sampling times available

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [ms] | - [ms] | [ ] - [ms] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the assignment of the available hardware sampling times of the drive unit.  
The term "hardware sampling times" refers to those r20002 sampling times that are
formed as a multiple of the basic sampling time and always &lt; r20003.

**Dependency:**
  
  
Refer to:
p20000

**Notice:**
  
For internal purposes, the drive unit always requires at least two (or several, depending
on the parameterization of p0115 of the drive objects) free hardware sampling times.
Therefore, the current number of hardware sampling times that are still free can be
read out in r7903.  
If r7903=0, no additional sampling time that differs from r20008[0...12] can be provided
from the Control Unit. If, when selecting in this state, a runtime group with a sampling
time &lt; r20003 (p20000 &lt;= 255) is to be set in p20000, only runtime groups whose sampling
time is already provided in r20008[0...12] can be selected.

**Note:**
  
The 13 different sampling times available are displayed in r20008[0...12].  
If the value of r20008[0...12] is not equal to 0, then it specifies the sampling time
in ms.  
A sampling time that is provided can be simultaneously used by system functions, several
FBLOCKS runtime groups, and several DCC runtime groups.  
If the value of r20008[0...12] = 0, then this sampling time can still be freely assigned.
It should be noted that the basic system, depending on the selected basic sampling
times p0115[0], requires at least two (sometimes several) freely assignable hardware
sampling times for internal functions. The number of hardware sampling times that
can still be freely assigned can be read out in r7903.  
r20008[11] = 99999.00000 --&gt; Hardware sampling time is not supported.  
r20008[12] = 99999.00000 --&gt; Hardware sampling time is not supported.  
The sampling time of runtime groups that have been assigned to the PROFIBUS runtime
groups (p20000 = 4000 ... 4004) is not displayed in r20008. For this sampling time,
one of the internally and permanently assigned hardware sampling times is used.

### p20020 Computing time measurement runtime group

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**4 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 10 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
4.5

**Description:**
  
Only for internal Siemens service purposes.

### p20022 Computing time measurement, duration

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**4 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 60 [s] | 10000 [s] | [ 0 ] 60 [s] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
4.5

**Description:**
  
Only for internal Siemens service purposes.

### r20024[0...9] Computing time, minimum value

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**4 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [µs] | - [µs] | [ ] - [µs] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
4.5

**Description:**
  
Only for internal Siemens service purposes.

**Index:**
  
[
0]:
Runtime group 0  
[
1]:
Runtime group 1  
[
2]:
Runtime group 2  
[
3]:
Runtime group 3  
[
4]:
Runtime group 4  
[
5]:
Runtime group 5  
[
6]:
Runtime group 6  
[
7]:
Runtime group 7  
[
8]:
Runtime group 8  
[
9]:
Runtime group 9

### r20025[0...9] Computing time, average value

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**4 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [µs] | - [µs] | [ ] - [µs] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
4.5

**Description:**
  
Only for internal Siemens service purposes.

**Index:**
  
[
0]:
Runtime group 0  
[
1]:
Runtime group 1  
[
2]:
Runtime group 2  
[
3]:
Runtime group 3  
[
4]:
Runtime group 4  
[
5]:
Runtime group 5  
[
6]:
Runtime group 6  
[
7]:
Runtime group 7  
[
8]:
Runtime group 8  
[
9]:
Runtime group 9

### r20026[0...9] Computing time, maximum value

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**4 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [µs] | - [µs] | [ ] - [µs] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
4.5

**Description:**
  
Only for internal Siemens service purposes.

**Index:**
  
[
0]:
Runtime group 0  
[
1]:
Runtime group 1  
[
2]:
Runtime group 2  
[
3]:
Runtime group 3  
[
4]:
Runtime group 4  
[
5]:
Runtime group 5  
[
6]:
Runtime group 6  
[
7]:
Runtime group 7  
[
8]:
Runtime group 8  
[
9]:
Runtime group 9

### p20030[0...3] BI: AND 0 inputs

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 7210 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source of input quantities I0, I1, I2, I3 of instance AND 0 of the
AND function block.

**Index:**
  
[
0]:
Input I0  
[
1]:
Input I1  
[
2]:
Input I2  
[
3]:
Input I3

### r20031 BO: AND 0 output Q

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7210 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for binary quantity Q = I0 &amp; I1 &amp; I2 &amp; I3 of instance AND 0 of the
AND function block.

### p20032 AND 0 runtime group

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7210 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 9999 | [ 0 ] 9999 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the runtime group in which the instance AND 0 of the AND function
block is to be called.

**Value:**
  
0:
Runtime group 0  
1:
Runtime group 1  
2:
Runtime group 2  
3:
Runtime group 3  
4:
Runtime group 4  
5:
Runtime group 5  
6:
Runtime group 6  
7:
Runtime group 7  
8:
Runtime group 8  
9:
Runtime group 9  
9999:
Do not calculate

### p20033 AND 0 run sequence

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 7210 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 32000 | [ 0 ] 10 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the run sequence of instance AND 0 within the runtime group
set in p20032.

**Note:**
  
The function blocks with a lower run sequence value are calculated before function
blocks with a higher run sequence value.

### p20034[0...3] BI: AND 1 inputs

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 7210 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source of input quantities I0, I1, I2, I3 of instance AND 1 of the
AND function block.

**Index:**
  
[
0]:
Input I0  
[
1]:
Input I1  
[
2]:
Input I2  
[
3]:
Input I3

### r20035 BO: AND 1 output Q

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7210 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for binary quantity Q = I0 &amp; I1 &amp; I2 &amp; I3 of instance AND 1 of the
AND function block.

### p20036 AND 1 runtime group

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7210 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 9999 | [ 0 ] 9999 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the runtime group in which the instance AND 1 of the AND function
block is to be called.

**Value:**
  
0:
Runtime group 0  
1:
Runtime group 1  
2:
Runtime group 2  
3:
Runtime group 3  
4:
Runtime group 4  
5:
Runtime group 5  
6:
Runtime group 6  
7:
Runtime group 7  
8:
Runtime group 8  
9:
Runtime group 9  
9999:
Do not calculate

### p20037 AND 1 run sequence

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 7210 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 32000 | [ 0 ] 20 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the run sequence of instance AND 1 within the runtime group
set in p20036.

**Note:**
  
The function blocks with a lower run sequence value are calculated before function
blocks with a higher run sequence value.

### p20038[0...3] BI: AND 2 inputs

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 7210 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source of input quantities I0, I1, I2, I3 of instance AND 2 of the
AND function block.

**Index:**
  
[
0]:
Input I0  
[
1]:
Input I1  
[
2]:
Input I2  
[
3]:
Input I3

### r20039 BO: AND 2 output Q

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7210 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for binary quantity Q = I0 &amp; I1 &amp; I2 &amp; I3 of instance AND 2 of the
AND function block.

### p20040 AND 2 runtime group

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7210 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 9999 | [ 0 ] 9999 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the runtime group in which the instance AND 2 of the AND function
block is to be called.

**Value:**
  
0:
Runtime group 0  
1:
Runtime group 1  
2:
Runtime group 2  
3:
Runtime group 3  
4:
Runtime group 4  
5:
Runtime group 5  
6:
Runtime group 6  
7:
Runtime group 7  
8:
Runtime group 8  
9:
Runtime group 9  
9999:
Do not calculate

### p20041 AND 2 run sequence

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 7210 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 32000 | [ 0 ] 30 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the run sequence of instance AND 2 within the runtime group
set in p20040.

**Note:**
  
The function blocks with a lower run sequence value are calculated before function
blocks with a higher run sequence value.

### p20042[0...3] BI: AND 3 inputs

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 7210 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source of input quantities I0, I1, I2, I3 of instance AND 3 of the
AND function block.

**Index:**
  
[
0]:
Input I0  
[
1]:
Input I1  
[
2]:
Input I2  
[
3]:
Input I3

### r20043 BO: AND 3 output Q

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7210 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for binary quantity Q = I0 &amp; I1 &amp; I2 &amp; I3 of instance AND 3 of the
AND function block.

### p20044 AND 3 runtime group

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7210 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 9999 | [ 0 ] 9999 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the runtime group in which the instance AND 3 of the AND function
block is to be called.

**Value:**
  
0:
Runtime group 0  
1:
Runtime group 1  
2:
Runtime group 2  
3:
Runtime group 3  
4:
Runtime group 4  
5:
Runtime group 5  
6:
Runtime group 6  
7:
Runtime group 7  
8:
Runtime group 8  
9:
Runtime group 9  
9999:
Do not calculate

### p20045 AND 3 run sequence

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 7210 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 32000 | [ 0 ] 40 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the run sequence of instance AND 3 within the runtime group
set in p20044.

**Note:**
  
The function blocks with a lower run sequence value are calculated before function
blocks with a higher run sequence value.

### p20046[0...3] BI: OR 0 inputs

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 7212 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source of input quantities I0, I1, I2, I3 of instance OR 0 of the
OR function block.

**Index:**
  
[
0]:
Input I0  
[
1]:
Input I1  
[
2]:
Input I2  
[
3]:
Input I3

### r20047 BO: OR 0 output Q

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7212 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for binary quantity Q = I0 | I1 | I2 | I3 of instance OR 0 of the
OR function block.

### p20048 OR 0 runtime group

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7212 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 9999 | [ 0 ] 9999 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the runtime group in which the instance OR 0 of the OR function
block is to be called.

**Value:**
  
0:
Runtime group 0  
1:
Runtime group 1  
2:
Runtime group 2  
3:
Runtime group 3  
4:
Runtime group 4  
5:
Runtime group 5  
6:
Runtime group 6  
7:
Runtime group 7  
8:
Runtime group 8  
9:
Runtime group 9  
9999:
Do not calculate

### p20049 OR 0 run sequence

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 7212 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 32000 | [ 0 ] 60 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the run sequence of instance OR 0 within the runtime group set
in p20048.

**Note:**
  
The function blocks with a lower run sequence value are calculated before function
blocks with a higher run sequence value.

### p20050[0...3] BI: OR 1 inputs

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 7212 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source of input quantities I0, I1, I2, I3 of instance OR 1 of the
OR function block.

**Index:**
  
[
0]:
Input I0  
[
1]:
Input I1  
[
2]:
Input I2  
[
3]:
Input I3

### r20051 BO: OR 1 output Q

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7212 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for binary quantity Q = I0 | I1 | I2 | I3 of instance OR 1 of the
OR function block.

### p20052 OR 1 runtime group

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7212 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 9999 | [ 0 ] 9999 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the runtime group in which the instance OR 1 of the OR function
block is to be called.

**Value:**
  
0:
Runtime group 0  
1:
Runtime group 1  
2:
Runtime group 2  
3:
Runtime group 3  
4:
Runtime group 4  
5:
Runtime group 5  
6:
Runtime group 6  
7:
Runtime group 7  
8:
Runtime group 8  
9:
Runtime group 9  
9999:
Do not calculate

### p20053 OR 1 run sequence

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 7212 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 32000 | [ 0 ] 70 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the run sequence of instance OR 1 within the runtime group set
in p20052.

**Note:**
  
The function blocks with a lower run sequence value are calculated before function
blocks with a higher run sequence value.

### p20054[0...3] BI: OR 2 inputs

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 7212 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source of input quantities I0, I1, I2, I3 of instance OR 2 of the
OR function block.

**Index:**
  
[
0]:
Input I0  
[
1]:
Input I1  
[
2]:
Input I2  
[
3]:
Input I3

### r20055 BO: OR 2 output Q

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7212 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for binary quantity Q = I0 | I1 | I2 | I3 of instance OR 2 of the
OR function block.

### p20056 OR 2 runtime group

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7212 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 9999 | [ 0 ] 9999 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the runtime group in which the instance OR 2 of the OR function
block is to be called.

**Value:**
  
0:
Runtime group 0  
1:
Runtime group 1  
2:
Runtime group 2  
3:
Runtime group 3  
4:
Runtime group 4  
5:
Runtime group 5  
6:
Runtime group 6  
7:
Runtime group 7  
8:
Runtime group 8  
9:
Runtime group 9  
9999:
Do not calculate

### p20057 OR 2 run sequence

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 7212 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 32000 | [ 0 ] 80 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the run sequence of instance OR 2 within the runtime group set
in p20056.

**Note:**
  
The function blocks with a lower run sequence value are calculated before function
blocks with a higher run sequence value.

### p20058[0...3] BI: OR 3 inputs

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 7212 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source of input quantities I0, I1, I2, I3 of instance OR 3 of the
OR function block.

**Index:**
  
[
0]:
Input I0  
[
1]:
Input I1  
[
2]:
Input I2  
[
3]:
Input I3

### r20059 BO: OR 3 output Q

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7212 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for binary quantity Q = I0 | I1 | I2 | I3 of instance OR 3 of the
OR function block.

### p20060 OR 3 runtime group

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7212 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 9999 | [ 0 ] 9999 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the runtime group in which the instance OR 3 of the OR function
block is to be called.

**Value:**
  
0:
Runtime group 0  
1:
Runtime group 1  
2:
Runtime group 2  
3:
Runtime group 3  
4:
Runtime group 4  
5:
Runtime group 5  
6:
Runtime group 6  
7:
Runtime group 7  
8:
Runtime group 8  
9:
Runtime group 9  
9999:
Do not calculate

### p20061 OR 3 run sequence

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 7212 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 32000 | [ 0 ] 90 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the run sequence of instance OR 3 within the runtime group set
in p20060.

**Note:**
  
The function blocks with a lower run sequence value are calculated before function
blocks with a higher run sequence value.

### p20062[0...3] BI: XOR 0 inputs

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 7214 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source of input quantities I0, I1, I2, I3 of instance XOR 0 of the
XOR function block.

**Index:**
  
[
0]:
Input I0  
[
1]:
Input I1  
[
2]:
Input I2  
[
3]:
Input I3

### r20063 BO: XOR 0 output Q

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7214 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for binary quantity Q of instance XOR 0 of the XOR function block.

## SINAMICS Parameter SINAMICS S210 20064 - 20164

SINAMICS Parameter SINAMICS S210 20064 - 20164

### p20064 XOR 0 runtime group

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7214 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 9999 | [ 0 ] 9999 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the runtime group in which the instance XOR 0 of the XOR function
block is to be called.

**Value:**
  
0:
Runtime group 0  
1:
Runtime group 1  
2:
Runtime group 2  
3:
Runtime group 3  
4:
Runtime group 4  
5:
Runtime group 5  
6:
Runtime group 6  
7:
Runtime group 7  
8:
Runtime group 8  
9:
Runtime group 9  
9999:
Do not calculate

### p20065 XOR 0 run sequence

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 7214 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 32000 | [ 0 ] 110 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the run sequence of instance XOR 0 within the runtime group
set in p20064.

**Note:**
  
The function blocks with a lower run sequence value are calculated before function
blocks with a higher run sequence value.

### p20066[0...3] BI: XOR 1 inputs

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 7214 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source of input quantities I0, I1, I2, I3 of instance XOR 1 of the
XOR function block.

**Index:**
  
[
0]:
Input I0  
[
1]:
Input I1  
[
2]:
Input I2  
[
3]:
Input I3

### r20067 BO: XOR 1 output Q

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7214 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for binary quantity Q of instance XOR 1 of the XOR function block.

### p20068 XOR 1 runtime group

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7214 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 9999 | [ 0 ] 9999 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the runtime group in which the instance XOR 1 of the XOR function
block is to be called.

**Value:**
  
0:
Runtime group 0  
1:
Runtime group 1  
2:
Runtime group 2  
3:
Runtime group 3  
4:
Runtime group 4  
5:
Runtime group 5  
6:
Runtime group 6  
7:
Runtime group 7  
8:
Runtime group 8  
9:
Runtime group 9  
9999:
Do not calculate

### p20069 XOR 1 run sequence

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 7214 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 32000 | [ 0 ] 120 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the run sequence of instance XOR 1 within the runtime group
set in p20068.

**Note:**
  
The function blocks with a lower run sequence value are calculated before function
blocks with a higher run sequence value.

### p20070[0...3] BI: XOR 2 inputs

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 7214 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source of input quantities I0, I1, I2, I3 of instance XOR 2 of the
XOR function block.

**Index:**
  
[
0]:
Input I0  
[
1]:
Input I1  
[
2]:
Input I2  
[
3]:
Input I3

### r20071 BO: XOR 2 output Q

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7214 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for binary quantity Q of instance XOR 2 of the XOR function block.

### p20072 XOR 2 runtime group

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7214 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 9999 | [ 0 ] 9999 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the runtime group in which the instance XOR 2 of the XOR function
block is to be called.

**Value:**
  
0:
Runtime group 0  
1:
Runtime group 1  
2:
Runtime group 2  
3:
Runtime group 3  
4:
Runtime group 4  
5:
Runtime group 5  
6:
Runtime group 6  
7:
Runtime group 7  
8:
Runtime group 8  
9:
Runtime group 9  
9999:
Do not calculate

### p20073 XOR 2 run sequence

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 7214 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 32000 | [ 0 ] 130 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the run sequence of instance XOR 2 within the runtime group
set in p20072.

**Note:**
  
The function blocks with a lower run sequence value are calculated before function
blocks with a higher run sequence value.

### p20074[0...3] BI: XOR 3 inputs

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 7214 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source of input quantities I0, I1, I2, I3 of instance XOR 3 of the
XOR function block.

**Index:**
  
[
0]:
Input I0  
[
1]:
Input I1  
[
2]:
Input I2  
[
3]:
Input I3

### r20075 BO: XOR 3 output Q

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7214 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for binary quantity Q of instance XOR 3 of the XOR function block.

### p20076 XOR 3 runtime group

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7214 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 9999 | [ 0 ] 9999 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the runtime group in which the instance XOR 3 of the XOR function
block is to be called.

**Value:**
  
0:
Runtime group 0  
1:
Runtime group 1  
2:
Runtime group 2  
3:
Runtime group 3  
4:
Runtime group 4  
5:
Runtime group 5  
6:
Runtime group 6  
7:
Runtime group 7  
8:
Runtime group 8  
9:
Runtime group 9  
9999:
Do not calculate

### p20077 XOR 3 run sequence

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 7214 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 32000 | [ 0 ] 140 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the run sequence of instance XOR 3 within the runtime group
set in p20076.

**Note:**
  
The function blocks with a lower run sequence value are calculated before function
blocks with a higher run sequence value.

### p20078 BI: NOT 0 input I

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 7216 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source of input quantity I of instance NOT 0 of the inverter.

### r20079 BO: NOT 0 inverted output

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7216 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for the inverted output of instance NOT 0 of the inverter.

### p20080 NOT 0 runtime group

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7216 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 9999 | [ 0 ] 9999 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the runtime group in which the instance NOT 0 of the inverter
is to be called.

**Value:**
  
0:
Runtime group 0  
1:
Runtime group 1  
2:
Runtime group 2  
3:
Runtime group 3  
4:
Runtime group 4  
5:
Runtime group 5  
6:
Runtime group 6  
7:
Runtime group 7  
8:
Runtime group 8  
9:
Runtime group 9  
9999:
Do not calculate

### p20081 NOT 0 run sequence

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 7216 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 32000 | [ 0 ] 160 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the run sequence of instance NOT 0 within the runtime group
set in p20080.

**Note:**
  
The function blocks with a lower run sequence value are calculated before function
blocks with a higher run sequence value.

### p20082 BI: NOT 1 input I

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 7216 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source of input quantity I of instance NOT 1 of the inverter.

### r20083 BO: NOT 1 inverted output

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7216 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for the inverted output of instance NOT 1 of the inverter.

### p20084 NOT 1 runtime group

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7216 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 9999 | [ 0 ] 9999 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the runtime group in which the instance NOT 1 of the inverter
is to be called.

**Value:**
  
0:
Runtime group 0  
1:
Runtime group 1  
2:
Runtime group 2  
3:
Runtime group 3  
4:
Runtime group 4  
5:
Runtime group 5  
6:
Runtime group 6  
7:
Runtime group 7  
8:
Runtime group 8  
9:
Runtime group 9  
9999:
Do not calculate

### p20085 NOT 1 run sequence

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 7216 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 32000 | [ 0 ] 170 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the run sequence of instance NOT 1 within the runtime group
set in p20084.

**Note:**
  
The function blocks with a lower run sequence value are calculated before function
blocks with a higher run sequence value.

### p20086 BI: NOT 2 input I

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 7216 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source of input quantity I of instance NOT 2 of the inverter.

### r20087 BO: NOT 2 inverted output

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7216 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for the inverted output of instance NOT 2 of the inverter.

### p20088 NOT 2 runtime group

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7216 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 9999 | [ 0 ] 9999 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the runtime group in which the instance NOT 2 of the inverter
is to be called.

**Value:**
  
0:
Runtime group 0  
1:
Runtime group 1  
2:
Runtime group 2  
3:
Runtime group 3  
4:
Runtime group 4  
5:
Runtime group 5  
6:
Runtime group 6  
7:
Runtime group 7  
8:
Runtime group 8  
9:
Runtime group 9  
9999:
Do not calculate

### p20089 NOT 2 run sequence

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 7216 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 32000 | [ 0 ] 180 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the run sequence of instance NOT 2 within the runtime group
set in p20088.

**Note:**
  
The function blocks with a lower run sequence value are calculated before function
blocks with a higher run sequence value.

### p20090 BI: NOT 3 input I

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 7216 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source of input quantity I of instance NOT 3 of the inverter.

### r20091 BO: NOT 3 inverted output

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7216 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for the inverted output of instance NOT 3 of the inverter.

### p20092 NOT 3 runtime group

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7216 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 9999 | [ 0 ] 9999 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the runtime group in which the instance NOT 3 of the inverter
is to be called.

**Value:**
  
0:
Runtime group 0  
1:
Runtime group 1  
2:
Runtime group 2  
3:
Runtime group 3  
4:
Runtime group 4  
5:
Runtime group 5  
6:
Runtime group 6  
7:
Runtime group 7  
8:
Runtime group 8  
9:
Runtime group 9  
9999:
Do not calculate

### p20093 NOT 3 run sequence

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 7216 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 32000 | [ 0 ] 190 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the run sequence of instance NOT 3 within the runtime group
set in p20092.

**Note:**
  
The function blocks with a lower run sequence value are calculated before function
blocks with a higher run sequence value.

### p20094[0...3] CI: ADD 0 inputs

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7220 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**PERCENT | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source of input quantities X0, X1, X2, X3 of instance ADD 0 of the
adder.

**Index:**
  
[
0]:
Input X0  
[
1]:
Input X1  
[
2]:
Input X2  
[
3]:
Input X3

### r20095 CO: ADD 0 output Y

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7220 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**PERCENT | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for the output quantity Y = X0 + X1 + X2 + X3 of instance ADD 0
of the adder.

### p20096 ADD 0 runtime group

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7220 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 9999 | [ 0 ] 9999 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the runtime group in which the instance ADD 0 of the adder is
to be called.

**Value:**
  
0:
Runtime group 0  
1:
Runtime group 1  
2:
Runtime group 2  
3:
Runtime group 3  
4:
Runtime group 4  
5:
Runtime group 5  
6:
Runtime group 6  
7:
Runtime group 7  
8:
Runtime group 8  
9:
Runtime group 9  
9999:
Do not calculate

### p20097 ADD 0 run sequence

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 7220 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 32000 | [ 0 ] 210 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the run sequence of instance ADD 0 within the runtime group
set in p20096.

**Note:**
  
The function blocks with a lower run sequence value are calculated before function
blocks with a higher run sequence value.

### p20098[0...3] CI: ADD 1 inputs

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7220 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**PERCENT | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source of input quantities X0, X1, X2, X3 of instance ADD 1 of the
adder.

**Index:**
  
[
0]:
Input X0  
[
1]:
Input X1  
[
2]:
Input X2  
[
3]:
Input X3

### r20099 CO: ADD 1 output Y

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7220 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**PERCENT | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for the output quantity Y = X0 + X1 + X2 + X3 of instance ADD 1
of the adder.

### p20100 ADD 1 runtime group

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7220 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 9999 | [ 0 ] 9999 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the runtime group in which the instance ADD 1 of the adder is
to be called.

**Value:**
  
0:
Runtime group 0  
1:
Runtime group 1  
2:
Runtime group 2  
3:
Runtime group 3  
4:
Runtime group 4  
5:
Runtime group 5  
6:
Runtime group 6  
7:
Runtime group 7  
8:
Runtime group 8  
9:
Runtime group 9  
9999:
Do not calculate

### p20101 ADD 1 run sequence

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 7220 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 32000 | [ 0 ] 220 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the run sequence of instance ADD 1 within the runtime group
set in p20100.

**Note:**
  
The function blocks with a lower run sequence value are calculated before function
blocks with a higher run sequence value.

### p20102[0...1] CI: SUB 0 inputs

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7220 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**PERCENT | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source of minuend X1 and subtrahend X2 of instance SUB 0 of the subtractor.

**Index:**
  
[
0]:
Minuend X1  
[
1]:
Subtrahend X2

### r20103 CO: SUB 0 difference Y

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7220 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**PERCENT | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for the difference Y = X1 - X2 of instance SUB 0 of the subtractor.

### p20104 SUB 0 runtime group

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7220 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 9999 | [ 0 ] 9999 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the runtime group in which instance SUB 0 of the subtractor
is to be called.

**Value:**
  
0:
Runtime group 0  
1:
Runtime group 1  
2:
Runtime group 2  
3:
Runtime group 3  
4:
Runtime group 4  
5:
Runtime group 5  
6:
Runtime group 6  
7:
Runtime group 7  
8:
Runtime group 8  
9:
Runtime group 9  
9999:
Do not calculate

### p20105 SUB 0 run sequence

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 7220 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 32000 | [ 0 ] 240 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the run sequence of instance SUB 0 within the runtime group
set in p20104.

**Note:**
  
The function blocks with a lower run sequence value are calculated before function
blocks with a higher run sequence value.

### p20106[0...1] CI: SUB 1 inputs

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7220 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**PERCENT | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source of minuend X1 and subtrahend X2 of instance SUB 1 of the subtractor.

**Index:**
  
[
0]:
Minuend X1  
[
1]:
Subtrahend X2

### r20107 CO: SUB 1 difference Y

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7220 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**PERCENT | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for the difference Y = X1 - X2 of instance SUB 1 of the subtractor.

### p20108 SUB 1 runtime group

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7220 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 9999 | [ 0 ] 9999 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the runtime group in which instance SUB 1 of the subtractor
is to be called.

**Value:**
  
0:
Runtime group 0  
1:
Runtime group 1  
2:
Runtime group 2  
3:
Runtime group 3  
4:
Runtime group 4  
5:
Runtime group 5  
6:
Runtime group 6  
7:
Runtime group 7  
8:
Runtime group 8  
9:
Runtime group 9  
9999:
Do not calculate

### p20109 SUB 1 run sequence

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 7220 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 32000 | [ 0 ] 250 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the run sequence of instance SUB 1 within the runtime group
set in p20108.

**Note:**
  
The function blocks with a lower run sequence value are calculated before function
blocks with a higher run sequence value.

### p20110[0...3] CI: MUL 0 inputs

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7222 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**PERCENT | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source of the factors X0, X1, X2, X3 of instance MUL 0 of the multiplier.

**Index:**
  
[
0]:
Factor X0  
[
1]:
Factor X1  
[
2]:
Factor X2  
[
3]:
Factor X3

### r20111 CO: MUL 0 product Y

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7222 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**PERCENT | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for the product Y = X0 * X1 * X2 * X3 of instance MUL 0 of the multiplier.

### p20112 MUL 0 runtime group

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7222 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 9999 | [ 0 ] 9999 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the runtime group in which instance MUL 0 of the multiplier
is to be called.

**Value:**
  
0:
Runtime group 0  
1:
Runtime group 1  
2:
Runtime group 2  
3:
Runtime group 3  
4:
Runtime group 4  
5:
Runtime group 5  
6:
Runtime group 6  
7:
Runtime group 7  
8:
Runtime group 8  
9:
Runtime group 9  
9999:
Do not calculate

### p20113 MUL 0 run sequence

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 7222 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 32000 | [ 0 ] 270 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the run sequence of instance MUL 0 within the runtime group
set in p20112.

**Note:**
  
The function blocks with a lower run sequence value are calculated before function
blocks with a higher run sequence value.

### p20114[0...3] CI: MUL 1 inputs

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7222 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**PERCENT | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source of the factors X0, X1, X2, X3 of instance MUL 1 of the multiplier.

**Index:**
  
[
0]:
Factor X0  
[
1]:
Factor X1  
[
2]:
Factor X2  
[
3]:
Factor X3

### r20115 CO: MUL 1 product Y

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7222 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**PERCENT | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for the product Y = X0 * X1 * X2 * X3 of instance MUL 1 of the multiplier.

### p20116 MUL 1 runtime group

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7222 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 9999 | [ 0 ] 9999 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the runtime group in which instance MUL 1 of the multiplier
is to be called.

**Value:**
  
0:
Runtime group 0  
1:
Runtime group 1  
2:
Runtime group 2  
3:
Runtime group 3  
4:
Runtime group 4  
5:
Runtime group 5  
6:
Runtime group 6  
7:
Runtime group 7  
8:
Runtime group 8  
9:
Runtime group 9  
9999:
Do not calculate

### p20117 MUL 1 run sequence

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 7222 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 32000 | [ 0 ] 280 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the run sequence of instance MUL 1 within the runtime group
set in p20116.

**Note:**
  
The function blocks with a lower run sequence value are calculated before function
blocks with a higher run sequence value.

### p20118[0...1] CI: DIV 0 inputs

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7222 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**PERCENT | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source of dividend X0 and divisor X1 of instance DIV 0 of the divider.

**Index:**
  
[
0]:
Dividend X0  
[
1]:
Divisor X1

### r20119[0...2] CO: DIV 0 quotient

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7222 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**PERCENT | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for quotients Y = X0 / X1, integer number quotients YIN, and division
remainder MOD = (Y - YIN) x X1 of instance DIV 0 of the divider.

**Index:**
  
[
0]:
Quotient Y  
[
1]:
Integer number quotient YIN  
[
2]:
Div remainder MOD

### r20120 BO: DIV 0 divisor is zero QF

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7222 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for the signal QF that the divisor X1 of instance DIV 0 of the divider
is zero.  
X1 = 0.0 =&gt; QF = 1

### p20121 DIV 0 runtime group

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7222 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 9999 | [ 0 ] 9999 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the runtime group in which instance DIV 0 of the divider is
to be called.

**Value:**
  
0:
Runtime group 0  
1:
Runtime group 1  
2:
Runtime group 2  
3:
Runtime group 3  
4:
Runtime group 4  
5:
Runtime group 5  
6:
Runtime group 6  
7:
Runtime group 7  
8:
Runtime group 8  
9:
Runtime group 9  
9999:
Do not calculate

### p20122 DIV 0 run sequence

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 7222 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 32000 | [ 0 ] 300 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the run sequence of instance DIV 0 within the runtime group
set in p20121.

**Note:**
  
The function blocks with a lower run sequence value are calculated before function
blocks with a higher run sequence value.

### p20123[0...1] CI: DIV 1 inputs

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7222 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**PERCENT | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source of dividend X0 and divisor X1 of instance DIV 1 of the divider.

**Index:**
  
[
0]:
Dividend X0  
[
1]:
Divisor X1

### r20124[0...2] CO: DIV 1 quotient

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7222 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**PERCENT | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for quotients Y = X0 / X1, the integer number quotients YIN, and
division remainder MOD = (Y - YIN) x X1 of instance DIV 1 of the divider.

**Index:**
  
[
0]:
Quotient Y  
[
1]:
Integer number quotient YIN  
[
2]:
Div remainder MOD

### r20125 BO: DIV 1 divisor is zero QF

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7222 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for the signal QF that the divisor X1 of instance DIV 1 of the divider
is zero.  
X1 = 0.0 =&gt; QF = 1

### p20126 DIV 1 runtime group

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7222 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 9999 | [ 0 ] 9999 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the runtime group in which instance DIV 1 of the divider is
to be called.

**Value:**
  
0:
Runtime group 0  
1:
Runtime group 1  
2:
Runtime group 2  
3:
Runtime group 3  
4:
Runtime group 4  
5:
Runtime group 5  
6:
Runtime group 6  
7:
Runtime group 7  
8:
Runtime group 8  
9:
Runtime group 9  
9999:
Do not calculate

### p20127 DIV 1 run sequence

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 7222 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 32000 | [ 0 ] 310 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the run sequence of instance DIV 1 within the runtime group
set in p20126.

**Note:**
  
The function blocks with a lower run sequence value are calculated before function
blocks with a higher run sequence value.

### p20128 CI: AVA 0 input X

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7224 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**PERCENT | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source of the input quantity X of instance AVA 0 of the absolute value
generator with sign evaluation.

### r20129 CO: AVA 0 output Y

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7224 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**PERCENT | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for output quantity Y of instance AVA 0 of the absolute value generator
with sign evaluation.

### r20130 BO: AVA 0 input negative SN

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7224 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for signal SN that the input quantity X of instance AVA 0 of the
absolute value generator with sign evaluation is negative.  
X &lt; 0.0 =&gt; SN = 1

### p20131 AVA 0 runtime group

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7224 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 9999 | [ 0 ] 9999 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the runtime group in which instance AVA 0 of the absolute value
generator with sign evaluation is to be called.

**Value:**
  
0:
Runtime group 0  
1:
Runtime group 1  
2:
Runtime group 2  
3:
Runtime group 3  
4:
Runtime group 4  
5:
Runtime group 5  
6:
Runtime group 6  
7:
Runtime group 7  
8:
Runtime group 8  
9:
Runtime group 9  
9999:
Do not calculate

### p20132 AVA 0 run sequence

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 7224 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 32000 | [ 0 ] 340 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the run sequence of instance AVA 0 within the runtime group
set in p20131.

**Note:**
  
The function blocks with a lower run sequence value are calculated before function
blocks with a higher run sequence value.

### p20133 CI: AVA 1 input X

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7224 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**PERCENT | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source of the input quantity X of instance AVA 1 of the absolute value
generator with sign evaluation.

### r20134 CO: AVA 1 output Y

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7224 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**PERCENT | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for output quantity Y of instance AVA 1 of the absolute value generator
with sign evaluation.

### r20135 BO: AVA 1 input negative SN

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7224 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for signal SN that the input quantity X of instance AVA 1 of the
absolute value generator with sign evaluation is negative.  
X &lt; 0.0 =&gt; SN = 1

### p20136 AVA 1 runtime group

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7224 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 9999 | [ 0 ] 9999 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the runtime group in which instance AVA 1 of the absolute value
generator with sign evaluation is to be called.

**Value:**
  
0:
Runtime group 0  
1:
Runtime group 1  
2:
Runtime group 2  
3:
Runtime group 3  
4:
Runtime group 4  
5:
Runtime group 5  
6:
Runtime group 6  
7:
Runtime group 7  
8:
Runtime group 8  
9:
Runtime group 9  
9999:
Do not calculate

### p20137 AVA 1 run sequence

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 7224 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 32000 | [ 0 ] 350 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the run sequence of instance AVA 1 within the runtime group
set in p20136.

**Note:**
  
The function blocks with a lower run sequence value are calculated before function
blocks with a higher run sequence value.

### p20138 BI: MFP 0 input pulse I

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 7230 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source for the input pulse I of instance MFP 0 of the pulse generator.

### p20139 MFP 0 pulse duration in ms

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7230 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 | 5400000.00 | [ 0 ] 0.00 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for pulse duration T in milliseconds of instance MFP 0 of the pulse
generator.

### r20140 BO: MFP 0 output Q

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7230 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for output pulse Q of instance MFP 0 of the pulse generator.

### p20141 MFP 0 runtime group

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7230 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 9999 | [ 0 ] 9999 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the runtime group in which the instance MFP 0 of the pulse generator
is to be called.

**Value:**
  
0:
Runtime group 0  
1:
Runtime group 1  
2:
Runtime group 2  
3:
Runtime group 3  
4:
Runtime group 4  
5:
Runtime group 5  
6:
Runtime group 6  
7:
Runtime group 7  
8:
Runtime group 8  
9:
Runtime group 9  
9999:
Do not calculate

### p20142 MFP 0 run sequence

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 7230 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 32000 | [ 0 ] 370 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the run sequence of instance MFP 0 within the runtime group
set in p20141.

**Note:**
  
The function blocks with a lower run sequence value are calculated before function
blocks with a higher run sequence value.

### p20143 BI: MFP 1 input pulse I

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 7230 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source for the input pulse I of instance MFP 1 of the pulse generator.

### p20144 MFP 1 pulse duration in ms

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7230 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 | 5400000.00 | [ 0 ] 0.00 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for pulse duration T in milliseconds of instance MFP 1 of the pulse
generator.

### r20145 BO: MFP 1 output Q

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7230 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for output pulse Q of instance MFP 1 of the pulse generator.

### p20146 MFP 1 runtime group

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7230 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 9999 | [ 0 ] 9999 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the runtime group in which the instance MFP 1 of the pulse generator
is to be called.

**Value:**
  
0:
Runtime group 0  
1:
Runtime group 1  
2:
Runtime group 2  
3:
Runtime group 3  
4:
Runtime group 4  
5:
Runtime group 5  
6:
Runtime group 6  
7:
Runtime group 7  
8:
Runtime group 8  
9:
Runtime group 9  
9999:
Do not calculate

### p20147 MFP 1 run sequence

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 7230 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 32000 | [ 0 ] 380 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the run sequence of instance MFP 1 within the runtime group
set in p20146.

**Note:**
  
The function blocks with a lower run sequence value are calculated before function
blocks with a higher run sequence value.

### p20148 BI: PCL 0 input pulse I

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 7230 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source for the input pulse I of instance PCL 0 of the pulse shortener.

### p20149 PCL 0 pulse duration in ms

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7230 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 | 5400000.00 | [ 0 ] 0.00 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for pulse duration T in milliseconds of instance PCL 0 of the pulse
shortener.

### r20150 BO: PCL 0 output Q

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7230 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for output pulse Q of instance PCL 0 of the pulse shortener.

### p20151 PCL 0 runtime group

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7230 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 9999 | [ 0 ] 9999 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the runtime group in which the instance PCL 0 of the pulse shortener
is to be called.

**Value:**
  
0:
Runtime group 0  
1:
Runtime group 1  
2:
Runtime group 2  
3:
Runtime group 3  
4:
Runtime group 4  
5:
Runtime group 5  
6:
Runtime group 6  
7:
Runtime group 7  
8:
Runtime group 8  
9:
Runtime group 9  
9999:
Do not calculate

### p20152 PCL 0 run sequence

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 7230 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 32000 | [ 0 ] 400 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the run sequence of instance PCL 0 within the runtime group
set in p20151.

**Note:**
  
The function blocks with a lower run sequence value are calculated before function
blocks with a higher run sequence value.

### p20153 BI: PCL 1 input pulse I

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 7230 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source for the input pulse I of instance PCL 1 of the pulse shortener.

### p20154 PCL 1 pulse duration in ms

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7230 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 | 5400000.00 | [ 0 ] 0.00 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for pulse duration T in milliseconds of instance PCL 1 of the pulse
shortener.

### r20155 BO: PCL 1 output Q

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7230 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for output pulse Q of instance PCL 1 of the pulse shortener.

### p20156 PCL 1 runtime group

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7230 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 9999 | [ 0 ] 9999 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the runtime group in which the instance PCL 1 of the pulse shortener
is to be called.

**Value:**
  
0:
Runtime group 0  
1:
Runtime group 1  
2:
Runtime group 2  
3:
Runtime group 3  
4:
Runtime group 4  
5:
Runtime group 5  
6:
Runtime group 6  
7:
Runtime group 7  
8:
Runtime group 8  
9:
Runtime group 9  
9999:
Do not calculate

### p20157 PCL 1 run sequence

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 7230 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 32000 | [ 0 ] 410 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the run sequence of instance PCL 1 within the runtime group
set in p20156.

**Note:**
  
The function blocks with a lower run sequence value are calculated before function
blocks with a higher run sequence value.

### p20158 BI: PDE 0 input pulse I

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 7232 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source for the input pulse I of instance PDE 0 of the closing delay
device.

### p20159 PDE 0 pulse delay time in ms

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7232 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 | 5400000.00 | [ 0 ] 0.00 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for pulse delay time T in milliseconds of instance PDE 0 of the
closing delay device.

### r20160 BO: PDE 0 output Q

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7232 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for output pulse Q of instance PDE 0 of the closing delay device.

### p20161 PDE 0 runtime group

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7232 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 9999 | [ 0 ] 9999 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the runtime group in which instance PDE 0 of the closing delay
device is to be called.

**Value:**
  
0:
Runtime group 0  
1:
Runtime group 1  
2:
Runtime group 2  
3:
Runtime group 3  
4:
Runtime group 4  
5:
Runtime group 5  
6:
Runtime group 6  
7:
Runtime group 7  
8:
Runtime group 8  
9:
Runtime group 9  
9999:
Do not calculate

### p20162 PDE 0 run sequence

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 7232 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 32000 | [ 0 ] 430 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the run sequence of instance PDE 0 within the runtime group
set in p20161.

**Note:**
  
The function blocks with a lower run sequence value are calculated before function
blocks with a higher run sequence value.

### p20163 BI: PDE 1 input pulse I

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 7232 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source for the input pulse I of instance PDE 1 of the closing delay
device.

### p20164 PDE 1 pulse delay time in ms

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7232 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 | 5400000.00 | [ 0 ] 0.00 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for pulse delay time T in milliseconds of instance PDE 1 of the
closing delay device.

## SINAMICS Parameter SINAMICS S210 20165 - 20265

SINAMICS Parameter SINAMICS S210 20165 - 20265

### r20165 BO: PDE 1 output Q

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7232 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for output pulse Q of instance PDE 1 of the closing delay device.

### p20166 PDE 1 runtime group

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7232 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 9999 | [ 0 ] 9999 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the runtime group in which instance PDE 1 of the closing delay
device is to be called.

**Value:**
  
0:
Runtime group 0  
1:
Runtime group 1  
2:
Runtime group 2  
3:
Runtime group 3  
4:
Runtime group 4  
5:
Runtime group 5  
6:
Runtime group 6  
7:
Runtime group 7  
8:
Runtime group 8  
9:
Runtime group 9  
9999:
Do not calculate

### p20167 PDE 1 run sequence

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 7232 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 32000 | [ 0 ] 440 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the run sequence of instance PDE 1 within the runtime group
set in p20166.

**Note:**
  
The function blocks with a lower run sequence value are calculated before function
blocks with a higher run sequence value.

### p20168 BI: PDF 0 input pulse I

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 7232 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source for the input pulse I of instance PDF 0 of the breaking delay
device.

### p20169 PDF 0 pulse extension time in ms

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7232 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 | 5400000.00 | [ 0 ] 0.00 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for pulse extension time T in milliseconds of instance PDF 0 of
the breaking delay device.

### r20170 BO: PDF 0 output Q

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7232 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for output pulse Q of instance PDF 0 of the breaking delay device.

### p20171 PDF 0 runtime group

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7232 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 9999 | [ 0 ] 9999 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the runtime group in which the instance PDF 0 of the breaking
delay device is to be called.

**Value:**
  
0:
Runtime group 0  
1:
Runtime group 1  
2:
Runtime group 2  
3:
Runtime group 3  
4:
Runtime group 4  
5:
Runtime group 5  
6:
Runtime group 6  
7:
Runtime group 7  
8:
Runtime group 8  
9:
Runtime group 9  
9999:
Do not calculate

### p20172 PDF 0 run sequence

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 7232 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 32000 | [ 0 ] 460 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the run sequence of instance PDF 0 within the runtime group
set in p20171.

**Note:**
  
The function blocks with a lower run sequence value are calculated before function
blocks with a higher run sequence value.

### p20173 BI: PDF 1 input pulse I

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 7232 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source for the input pulse I of instance PDF 1 of the breaking delay
device.

### p20174 PDF 1 pulse extension time in ms

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7232 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 | 5400000.00 | [ 0 ] 0.00 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for pulse extension time T in milliseconds of instance PDF 1 of
the breaking delay device.

### r20175 BO: PDF 1 output Q

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7232 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for output pulse Q of instance PDF 1 of the breaking delay device.

### p20176 PDF 1 runtime group

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7232 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 9999 | [ 0 ] 9999 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the runtime group in which the instance PDF 1 of the breaking
delay device is to be called.

**Value:**
  
0:
Runtime group 0  
1:
Runtime group 1  
2:
Runtime group 2  
3:
Runtime group 3  
4:
Runtime group 4  
5:
Runtime group 5  
6:
Runtime group 6  
7:
Runtime group 7  
8:
Runtime group 8  
9:
Runtime group 9  
9999:
Do not calculate

### p20177 PDF 1 run sequence

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 7232 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 32000 | [ 0 ] 470 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the run sequence of instance PDF 1 within the runtime group
set in p20176.

**Note:**
  
The function blocks with a lower run sequence value are calculated before function
blocks with a higher run sequence value.

### p20178[0...1] BI: PST 0 inputs

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 7234 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source for input pulse I and the reset input R of instance PST 0 of
the pulse extension element.

**Index:**
  
[
0]:
Input pulse I  
[
1]:
Reset input R

### p20179 PST 0 pulse duration in ms

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7234 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 | 5400000.00 | [ 0 ] 0.00 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for pulse duration T in milliseconds of instance PST 0 of the pulse
extension element.

### r20180 BO: PST 0 output Q

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7234 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for output pulse Q of instance PST 0 of the pulse extension element.

### p20181 PST 0 runtime group

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7234 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 9999 | [ 0 ] 9999 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the runtime group in which the instance PST 0 of the pulse extension
element is to be called.

**Value:**
  
0:
Runtime group 0  
1:
Runtime group 1  
2:
Runtime group 2  
3:
Runtime group 3  
4:
Runtime group 4  
5:
Runtime group 5  
6:
Runtime group 6  
7:
Runtime group 7  
8:
Runtime group 8  
9:
Runtime group 9  
9999:
Do not calculate

### p20182 PST 0 run sequence

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 7234 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 7999 | [ 0 ] 490 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the run sequence of instance PST 0 within the runtime group
set in p20181.

**Note:**
  
The function blocks with a lower run sequence value are calculated before function
blocks with a higher run sequence value.

### p20183[0...1] BI: PST 1 inputs

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 7234 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source for input pulse I and the reset input R of instance PST 1 of
the pulse extension element.

**Index:**
  
[
0]:
Input pulse I  
[
1]:
Reset input R

### p20184 PST 1 pulse duration in ms

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7234 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 | 5400000.00 | [ 0 ] 0.00 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for pulse duration T in milliseconds of instance PST 1 of the pulse
extension element.

### r20185 BO: PST 1 output Q

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7234 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for output pulse Q of instance PST 1 of the pulse extension element.

### p20186 PST 1 runtime group

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7234 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 9999 | [ 0 ] 9999 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the runtime group in which the instance PST 1 of the pulse extension
element is to be called.

**Value:**
  
0:
Runtime group 0  
1:
Runtime group 1  
2:
Runtime group 2  
3:
Runtime group 3  
4:
Runtime group 4  
5:
Runtime group 5  
6:
Runtime group 6  
7:
Runtime group 7  
8:
Runtime group 8  
9:
Runtime group 9  
9999:
Do not calculate

### p20187 PST 1 run sequence

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 7234 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 7999 | [ 0 ] 500 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the run sequence of instance PST 1 within the runtime group
set in p20186.

**Note:**
  
The function blocks with a lower run sequence value are calculated before function
blocks with a higher run sequence value.

### p20188[0...1] BI: RSR 0 inputs

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 7240 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source for set input S and reset input R of instance RSR 0 of the
RS flipflop.

**Index:**
  
[
0]:
Set S  
[
1]:
Reset R

### r20189 BO: RSR 0 output Q

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7240 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for output Q of instance RSR 0 of the RS flipflop

### r20190 BO: RSR 0 inverted output QN

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7240 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for inverted output QN of instance RSR 0 of the RS flipflop.

### p20191 RSR 0 runtime group

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7240 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 9999 | [ 0 ] 9999 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the runtime group in which instance RSR 0 of the RS flipflop
is to be called.

**Value:**
  
0:
Runtime group 0  
1:
Runtime group 1  
2:
Runtime group 2  
3:
Runtime group 3  
4:
Runtime group 4  
5:
Runtime group 5  
6:
Runtime group 6  
7:
Runtime group 7  
8:
Runtime group 8  
9:
Runtime group 9  
9999:
Do not calculate

### p20192 RSR 0 run sequence

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 7240 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 7999 | [ 0 ] 520 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the run sequence of instance RSR 0 within the runtime group
set in p20191.

**Note:**
  
The function blocks with a lower run sequence value are calculated before function
blocks with a higher run sequence value.

### p20193[0...1] BI: RSR 1 inputs

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 7240 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source for set input S and reset input R of instance RSR 1 of the
RS flipflop.

**Index:**
  
[
0]:
Set S  
[
1]:
Reset R

### r20194 BO: RSR 1 output Q

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7240 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for output Q of instance RSR 1 of the RS flipflop

### r20195 BO: RSR 1 inverted output QN

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7240 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for inverted output QN of instance RSR 1 of the RS flipflop.

### p20196 RSR 1 runtime group

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7240 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 9999 | [ 0 ] 9999 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the runtime group in which instance RSR 1 of the RS flipflop
is to be called.

**Value:**
  
0:
Runtime group 0  
1:
Runtime group 1  
2:
Runtime group 2  
3:
Runtime group 3  
4:
Runtime group 4  
5:
Runtime group 5  
6:
Runtime group 6  
7:
Runtime group 7  
8:
Runtime group 8  
9:
Runtime group 9  
9999:
Do not calculate

### p20197 RSR 1 run sequence

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 7240 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 7999 | [ 0 ] 530 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the run sequence of instance RSR 1 within the runtime group
set in p20196.

**Note:**
  
The function blocks with a lower run sequence value are calculated before function
blocks with a higher run sequence value.

### p20198[0...3] BI: DFR 0 inputs

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 7240 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source for trigger input I, D input D, set input S, and reset input
R of instance DFR 0 of the D flipflop.

**Index:**
  
[
0]:
Trigger input I  
[
1]:
D input D  
[
2]:
Set S  
[
3]:
Reset R

### r20199 BO: DFR 0 output Q

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7240 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for output Q of instance DFR 0 of the D flipflop.

### r20200 BO: DFR 0 inverted output QN

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7240 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for the inverted output QN of instance DFR 0 of the D flipflop.

### p20201 DFR 0 runtime group

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7240 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 9999 | [ 0 ] 9999 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the runtime group in which instance DFR 0 of the D flipflop
is to be called.

**Value:**
  
0:
Runtime group 0  
1:
Runtime group 1  
2:
Runtime group 2  
3:
Runtime group 3  
4:
Runtime group 4  
5:
Runtime group 5  
6:
Runtime group 6  
7:
Runtime group 7  
8:
Runtime group 8  
9:
Runtime group 9  
9999:
Do not calculate

### p20202 DFR 0 run sequence

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 7240 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 32000 | [ 0 ] 550 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the run sequence of instance DFR 0 within the runtime group
set in p20201.

**Note:**
  
The function blocks with a lower run sequence value are calculated before function
blocks with a higher run sequence value.

### p20203[0...3] BI: DFR 1 inputs

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 7240 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source for trigger input I, D input D, set input S, and reset input
R of instance DFR 1 of the D flipflop.

**Index:**
  
[
0]:
Trigger input I  
[
1]:
D input D  
[
2]:
Set S  
[
3]:
Reset R

### r20204 BO: DFR 1 output Q

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7240 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for output Q of instance DFR 1 of the D flipflop.

### r20205 BO: DFR 1 inverted output QN

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7240 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for the inverted output QN of instance DFR 1 of the D flipflop.

### p20206 DFR 1 runtime group

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7240 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 9999 | [ 0 ] 9999 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the runtime group in which instance DFR 1 of the D flipflop
is to be called.

**Value:**
  
0:
Runtime group 0  
1:
Runtime group 1  
2:
Runtime group 2  
3:
Runtime group 3  
4:
Runtime group 4  
5:
Runtime group 5  
6:
Runtime group 6  
7:
Runtime group 7  
8:
Runtime group 8  
9:
Runtime group 9  
9999:
Do not calculate

### p20207 DFR 1 run sequence

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 7240 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 32000 | [ 0 ] 560 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the runtime group of instance DFR 1 within the runtime group
set in p20206.

**Note:**
  
The function blocks with a lower run sequence value are calculated before function
blocks with a higher run sequence value.

### p20208[0...1] BI: BSW 0 inputs

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 7250 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source of input quantities I0 and I1 of instance BSW 0 of the binary
changeover switch.

**Index:**
  
[
0]:
Input I0  
[
1]:
Input I1

### p20209 BI: BSW 0 switch setting I

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 7250 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source of the switch setting I of instance BSW 0 of the binary changeover
switch.

### r20210 BO: BSW 0 output Q

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7250 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for output quantity Q of instance BSW 0 of the binary changeover
switch.

### p20211 BSW 0 runtime group

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7250 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 9999 | [ 0 ] 9999 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the runtime group in which the instance BSW 0 of the binary
changeover switch is to be called.

**Value:**
  
0:
Runtime group 0  
1:
Runtime group 1  
2:
Runtime group 2  
3:
Runtime group 3  
4:
Runtime group 4  
5:
Runtime group 5  
6:
Runtime group 6  
7:
Runtime group 7  
8:
Runtime group 8  
9:
Runtime group 9  
9999:
Do not calculate

### p20212 BSW 0 run sequence

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 7250 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 7999 | [ 0 ] 580 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the run sequence of instance BSW 0 within the runtime group
set in p20211.

**Note:**
  
The function blocks with a lower run sequence value are calculated before function
blocks with a higher run sequence value.

### p20213[0...1] BI: BSW 1 inputs

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 7250 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source of input quantities I0 and I1 of instance BSW 1 of the binary
changeover switch.

**Index:**
  
[
0]:
Input I0  
[
1]:
Input I1

### p20214 BI: BSW 1 switch setting I

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 7250 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source of the switch setting I of instance BSW 1 of the binary changeover
switch.

### r20215 BO: BSW 1 output Q

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7250 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for output quantity Q of instance BSW 1 of the binary changeover
switch.

### p20216 BSW 1 runtime group

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7250 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 9999 | [ 0 ] 9999 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the runtime group in which the instance BSW 1 of the binary
changeover switch is to be called.

**Value:**
  
0:
Runtime group 0  
1:
Runtime group 1  
2:
Runtime group 2  
3:
Runtime group 3  
4:
Runtime group 4  
5:
Runtime group 5  
6:
Runtime group 6  
7:
Runtime group 7  
8:
Runtime group 8  
9:
Runtime group 9  
9999:
Do not calculate

### p20217 BSW 1 run sequence

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 7250 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 7999 | [ 0 ] 590 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the run sequence of instance BSW 1 within the runtime group
set in p20216.

**Note:**
  
The function blocks with a lower run sequence value are calculated before function
blocks with a higher run sequence value.

### p20218[0...1] CI: NSW 0 inputs

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7250 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**PERCENT | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source of input quantities X0 and X1 of instance NSW 0 of the numeric
changeover switch.

**Index:**
  
[
0]:
Input X0  
[
1]:
Input X1

### p20219 BI: NSW 0 switch setting I

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 7250 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source of the switch setting I of instance NSW 0 of the numeric changeover
switch.

### r20220 CO: NSW 0 output Y

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7250 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**PERCENT | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for output quantity Y of instance NSW 0 of the numeric changeover
switch.

### p20221 NSW 0 runtime group

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7250 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 9999 | [ 0 ] 9999 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the runtime group in which the instance NSW 0 of the numeric
changeover switch is to be called.

**Value:**
  
0:
Runtime group 0  
1:
Runtime group 1  
2:
Runtime group 2  
3:
Runtime group 3  
4:
Runtime group 4  
5:
Runtime group 5  
6:
Runtime group 6  
7:
Runtime group 7  
8:
Runtime group 8  
9:
Runtime group 9  
9999:
Do not calculate

### p20222 NSW 0 run sequence

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 7250 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 32000 | [ 0 ] 610 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the run sequence of instance NSW 0 within the runtime group
set in p20221.

**Note:**
  
The function blocks with a lower run sequence value are calculated before function
blocks with a higher run sequence value.

### p20223[0...1] CI: NSW 1 inputs

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7250 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**PERCENT | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source of input quantities X0 and X1 of instance NSW 1 of the numeric
changeover switch.

**Index:**
  
[
0]:
Input X0  
[
1]:
Input X1

### p20224 BI: NSW 1 switch setting I

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 7250 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source of the switch setting I of instance NSW 1 of the numeric changeover
switch.

### r20225 CO: NSW 1 output Y

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7250 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**PERCENT | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for output quantity Y of instance NSW 1 of the numeric changeover
switch.

### p20226 NSW 1 runtime group

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7250 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 9999 | [ 0 ] 9999 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the runtime group in which the instance NSW 1 of the numeric
changeover switch is to be called.

**Value:**
  
0:
Runtime group 0  
1:
Runtime group 1  
2:
Runtime group 2  
3:
Runtime group 3  
4:
Runtime group 4  
5:
Runtime group 5  
6:
Runtime group 6  
7:
Runtime group 7  
8:
Runtime group 8  
9:
Runtime group 9  
9999:
Do not calculate

### p20227 NSW 1 run sequence

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 7250 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 32000 | [ 0 ] 620 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the run sequence of instance NSW 1 within the runtime group
set in p20226.

**Note:**
  
The function blocks with a lower run sequence value are calculated before function
blocks with a higher run sequence value.

### p20228 CI: LIM 0 input X

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7260 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**PERCENT | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source of input quantity X of instance LIM 0 of the limiter.

### p20229 LIM 0 upper limit value LU

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7260 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| -340.28235E36 | 340.28235E36 | [ 0 ] 0.0000 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the upper limit value LU of instance LIM 0 of the limiter.

### p20230 LIM 0 lower limit value LL

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7260 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| -340.28235E36 | 340.28235E36 | [ 0 ] 0.0000 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the lower limit value LL of instance LIM 0 of the limiter.

### r20231 CO: LIM 0 output Y

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7260 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**PERCENT | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for the limited output quantity Y of instance LIM 0 of the limiter.

### r20232 BO: LIM 0 input quantity at the upper limit QU

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7260 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter of instance LIM 0 of limiter QU (upper limit reached), i.e. QU =
1 for X &gt;= LU.

### r20233 BO: LIM 0 input quantity at the lower limit QL

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7260 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter of instance LIM 0 of limiter QL (lower limit reached), i.e. QL =
1 for X &lt;= LL.

### p20234 LIM 0 runtime group

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7260 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 9999 | [ 0 ] 9999 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the runtime group in which instance LIM 0 of the limiter is
to be called.

**Value:**
  
0:
Runtime group 0  
1:
Runtime group 1  
2:
Runtime group 2  
3:
Runtime group 3  
4:
Runtime group 4  
5:
Runtime group 5  
6:
Runtime group 6  
7:
Runtime group 7  
8:
Runtime group 8  
9:
Runtime group 9  
9999:
Do not calculate

### p20235 LIM 0 run sequence

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 7260 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 32000 | [ 0 ] 640 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the run sequence of instance LIM 0 within the runtime group
set in p20234.

**Note:**
  
The function blocks with a lower run sequence value are calculated before function
blocks with a higher run sequence value.

### p20236 CI: LIM 1 input X

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7260 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**PERCENT | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source of input quantity X of instance LIM 1 of the limiter.

### p20237 LIM 1 upper limit value LU

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7260 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| -340.28235E36 | 340.28235E36 | [ 0 ] 0.0000 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the upper limit value LU of instance LIM 1 of the limiter.

### p20238 LIM 1 lower limit value LL

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7260 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| -340.28235E36 | 340.28235E36 | [ 0 ] 0.0000 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the lower limit value LL of instance LIM 1 of the limiter.

### r20239 CO: LIM 1 output Y

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7260 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**PERCENT | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for the limited output quantity Y of instance LIM 1 of the limiter.

### r20240 BO: LIM 1 input quantity at the upper limit QU

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7260 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter of instance LIM 1 of limiter QU (upper limit reached), i.e. QU =
1 for X &gt;= LU.

### r20241 BO: LIM 1 input quantity at the lower limit QL

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7260 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter of instance LIM 1 of limiter QL (lower limit reached), i.e. QL =
1 for X &lt;= LL.

### p20242 LIM 1 runtime group

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7260 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 9999 | [ 0 ] 9999 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the runtime group in which instance LIM 1 of the limiter is
to be called.

**Value:**
  
0:
Runtime group 0  
1:
Runtime group 1  
2:
Runtime group 2  
3:
Runtime group 3  
4:
Runtime group 4  
5:
Runtime group 5  
6:
Runtime group 6  
7:
Runtime group 7  
8:
Runtime group 8  
9:
Runtime group 9  
9999:
Do not calculate

### p20243 LIM 1 run sequence

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 7260 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 32000 | [ 0 ] 650 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the run sequence of instance LIM 1 within the runtime group
set in p20242.

**Note:**
  
The function blocks with a lower run sequence value are calculated before function
blocks with a higher run sequence value.

### p20244[0...1] CI: PT1 0 inputs

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7262 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**PERCENT | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source of input quantity X and of setting value SV of instance PT1
0 of the smoothing element.

**Index:**
  
[
0]:
Input X  
[
1]:
Setting value SV

### p20245 BI: PT1 0 accept setting value S

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 7262 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source for the "accept setting value" signal of instant PT1 0 of the
smoothing element.

### p20246 PT1 0 smoothing time constant in ms

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7262 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 | 340.28235E36 | [ 0 ] 0.00 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the smoothing time constant T in milliseconds of instance PT1 0 of the smoothing
element.

### r20247 CO: PT1 0 output Y

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7262 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**PERCENT | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for the smoothed output quantity Y of instance PT1 0 of the smoothing
element.

### p20248 PT1 0 runtime group

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7262 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 9999 | [ 0 ] 9999 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the runtime group in which instance PT1 0 of the smoothing element
is to be called.

**Value:**
  
0:
Runtime group 0  
1:
Runtime group 1  
2:
Runtime group 2  
3:
Runtime group 3  
4:
Runtime group 4  
5:
Runtime group 5  
6:
Runtime group 6  
7:
Runtime group 7  
8:
Runtime group 8  
9:
Runtime group 9  
9999:
Do not calculate

### p20249 PT1 0 run sequence

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 7262 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 32000 | [ 0 ] 670 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the run sequence of instance PT1 0 within the runtime group
set in p20248.

**Note:**
  
The function blocks with a lower run sequence value are calculated before function
blocks with a higher run sequence value.

### p20250[0...1] CI: PT1 1 inputs

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7262 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**PERCENT | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source of input quantity X and of setting value SV of instance PT1
1 of the smoothing element.

**Index:**
  
[
0]:
Input X  
[
1]:
Setting value SV

### p20251 BI: PT1 1 accept setting value S

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 7262 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source for the "accept setting value" signal of instant PT1 1 of the
smoothing element.

### p20252 PT1 1 smoothing time constant in ms

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7262 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 | 340.28235E36 | [ 0 ] 0.00 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the smoothing time constant T in milliseconds of instance PT1 1 of the smoothing
element.

### r20253 CO: PT1 1 output Y

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7262 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**PERCENT | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for the smoothed output quantity Y of instance PT1 1 of the smoothing
element.

### p20254 PT1 1 runtime group

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7262 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 9999 | [ 0 ] 9999 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the runtime group in which instance PT1 1 of the smoothing element
is to be called.

**Value:**
  
0:
Runtime group 0  
1:
Runtime group 1  
2:
Runtime group 2  
3:
Runtime group 3  
4:
Runtime group 4  
5:
Runtime group 5  
6:
Runtime group 6  
7:
Runtime group 7  
8:
Runtime group 8  
9:
Runtime group 9  
9999:
Do not calculate

### p20255 PT1 1 run sequence

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 7262 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 32000 | [ 0 ] 680 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the run sequence of instance PT1 1 within the runtime group
set in p20254.

**Note:**
  
The function blocks with a lower run sequence value are calculated before function
blocks with a higher run sequence value.

### p20256[0...1] CI: INT 0 inputs

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7264 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**PERCENT | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source of input quantity X and of setting value SV of instance INT
0 of the integrator.

**Index:**
  
[
0]:
Input X  
[
1]:
Setting value SV

### p20257 INT 0 upper limit value LU

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7264 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| -340.28235E36 | 340.28235E36 | [ 0 ] 0.0000 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the upper limit value LU of instance INT 0 of the integrator.

### p20258 INT 0 lower limit value LL

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7264 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| -340.28235E36 | 340.28235E36 | [ 0 ] 0.0000 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the lower limit value LL of instance INT 0 of the integrator.

### p20259 INT 0 integrating time constant in ms

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7264 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 | 340.28235E36 | [ 0 ] 0.00 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the integrating time constant Ti in milliseconds of instance INT 0 of the integrator.

### p20260 BI: INT 0 accept setting value S

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 7264 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source for the "accept setting value" signal of instant INT 0 of the
integrator.

### r20261 CO: INT 0 output Y

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7264 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**PERCENT | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for output quantity Y of instance INT 0 of the integrator.  
If LL&gt;= LU, then the output quantity Y = LU.

### r20262 BO: INT 0 integrator at the upper limit QU

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7264 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for the signal QU that output quantity Y of instance INT 0 of the
integrator has reached the upper limit value LU.

### r20263 BO: INT 0 integrator at the lower limit QL

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7264 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for the signal QL that output quantity Y of instance INT 0 of the
integrator has reached the lower limit value LL.

### p20264 INT 0 runtime group

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7264 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 9999 | [ 0 ] 9999 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the runtime group in which instance INT 0 of the integrator
is to be called.

**Value:**
  
0:
Runtime group 0  
1:
Runtime group 1  
2:
Runtime group 2  
3:
Runtime group 3  
4:
Runtime group 4  
5:
Runtime group 5  
6:
Runtime group 6  
7:
Runtime group 7  
8:
Runtime group 8  
9:
Runtime group 9  
9999:
Do not calculate

### p20265 INT 0 run sequence

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 7264 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 32000 | [ 0 ] 700 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the run sequence of instance INT 0 within the runtime group
set in p20264.

**Note:**
  
The function blocks with a lower run sequence value are calculated before function
blocks with a higher run sequence value.

## SINAMICS Parameter SINAMICS S210 20266 - 61001

SINAMICS Parameter SINAMICS S210 20266 - 61001

### p20266 CI: LVM 0 input X

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7270 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**PERCENT | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source of input quantity X of instance LVM 0 of the double-sided limiter.

### p20267 LVM 0 interval average value M

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7270 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| -340.28235E36 | 340.28235E36 | [ 0 ] 0.0000 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the interval average M of instance LVM 0 of the double-sided
limiter.

### p20268 LVM 0 interval limit L

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7270 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| -340.28235E36 | 340.28235E36 | [ 0 ] 0.0000 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the interval limit L of instance LVM 0 of the double-sided limiter.

### p20269 LVM 0 hyst HY

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7270 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| -340.28235E36 | 340.28235E36 | [ 0 ] 0.0000 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for hysteresis HY of instance LVM 0 of the double-sided limiter.

### r20270 BO: LVM 0 input quantity above interval QU

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7270 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter of instance LVM 0 of the double-sided limiter that input quantity
X was at least once X &gt; M + L and X is &gt;= M + L - HY.

### r20271 BO: LVM 0 input quantity within interval QM

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7270 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter of instance LVM 0 of the double-sided limiter that the input quantity
X lies within the interval.

### r20272 BO: LVM 0 input quantity below interval QL

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7270 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter of instance LVM 0 of the double-sided limiter that input quantity
X was at least once X &lt; M - L and X is &lt;= M - L + HY.

### p20273 LVM 0 runtime group

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7270 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 9999 | [ 0 ] 9999 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the runtime group in which instance LVM 0 of the double-sided
limiter is to be called.

**Value:**
  
0:
Runtime group 0  
1:
Runtime group 1  
2:
Runtime group 2  
3:
Runtime group 3  
4:
Runtime group 4  
5:
Runtime group 5  
6:
Runtime group 6  
7:
Runtime group 7  
8:
Runtime group 8  
9:
Runtime group 9  
9999:
Do not calculate

### p20274 LVM 0 run sequence

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 7270 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 7999 | [ 0 ] 720 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the run sequence of instance LVM 0 within the runtime group
set in p20273.

**Note:**
  
The function blocks with a lower run sequence value are calculated before function
blocks with a higher run sequence value.

### p20275 CI: LVM 1 input X

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7270 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**PERCENT | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source of input quantity X of instance LVM 1 of the double-sided limiter.

### p20276 LVM 1 interval average value M

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7270 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| -340.28235E36 | 340.28235E36 | [ 0 ] 0.0000 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the interval average M of instance LVM 1 of the double-sided
limiter.

### p20277 LVM 1 interval limit L

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7270 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| -340.28235E36 | 340.28235E36 | [ 0 ] 0.0000 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the interval limit L of instance LVM 1 of the double-sided limiter.

### p20278 LVM 1 hyst HY

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7270 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| -340.28235E36 | 340.28235E36 | [ 0 ] 0.0000 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for hysteresis HY of instance LVM 1 of the double-sided limiter.

### r20279 BO: LVM 1 input quantity above interval QU

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7270 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter of instance LVM 1 of the double-sided limiter that input quantity
X was at least once X &gt; M + L and X is &gt;= M + L - HY.

### r20280 BO: LVM 1 input quantity within interval QM

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7270 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter of instance LVM 1 of the double-sided limiter that the input quantity
X lies within the interval.

### r20281 BO: LVM 1 input quantity below interval QL

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7270 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter of instance LVM 1 of the double-sided limiter that input quantity
X was at least once X &lt; M - L and X is &lt;= M - L + HY.

### p20282 LVM 1 runtime group

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7270 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 9999 | [ 0 ] 9999 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the runtime group in which instance LVM 1 of the double-sided
limiter is to be called.

**Value:**
  
0:
Runtime group 0  
1:
Runtime group 1  
2:
Runtime group 2  
3:
Runtime group 3  
4:
Runtime group 4  
5:
Runtime group 5  
6:
Runtime group 6  
7:
Runtime group 7  
8:
Runtime group 8  
9:
Runtime group 9  
9999:
Do not calculate

### p20283 LVM 1 run sequence

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 7270 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 7999 | [ 0 ] 730 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the run sequence of instance LVM 1 within the runtime group
set in p20282.

**Note:**
  
The function blocks with a lower run sequence value are calculated before function
blocks with a higher run sequence value.

### p20284 CI: DIF 0 input X

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7264 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**PERCENT | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source of input quantity X of instance DIF 0 of the differentiating
element.

### p20285 DIF 0 differentiating time constant in ms

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7264 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 | 340.28235E36 | [ 0 ] 0.00 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the differentiating time constant Td in milliseconds of instance DIF 0 of the
differentiating element.

### r20286 CO: DIF 0 output Y

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7264 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**PERCENT | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for output quantity Y of instance DIF 0 of the differentiating element.

### p20287 DIF 0 runtime group

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7264 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 9999 | [ 0 ] 9999 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the runtime group in which instance DIF 0 of the differentiating
element is to be called.

**Value:**
  
0:
Runtime group 0  
1:
Runtime group 1  
2:
Runtime group 2  
3:
Runtime group 3  
4:
Runtime group 4  
5:
Runtime group 5  
6:
Runtime group 6  
7:
Runtime group 7  
8:
Runtime group 8  
9:
Runtime group 9  
9999:
Do not calculate

### p20288 DIF 0 run sequence

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 7264 |
| **Object:**All objects (FBLOCKS) | **P-Group:**Free function blocks | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 32000 | [ 0 ] 750 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the run sequence of instance DIF 0 within the runtime group
set in p20287.

**Note:**
  
The function blocks with a lower run sequence value are calculated before function
blocks with a higher run sequence value.

### p60000 PROFIdrive reference speed

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**CALC_MOD_ALL | **Access level:**2 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 6.00 [rpm] | 210000.00 [rpm] | [ 0 ] 3000.00 [rpm] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Sets the reference quantity for the speed values.  
All speeds specified as relative values refer to this reference quantity.  
The reference quantity corresponds to 100% or 4000 hex (word) or 4000 0000 hex (double
word).

**Dependency:**
  
  
Refer to:
p2000

**Note:**
  
Parameter p60000 is an image of parameter p2000 in conformance with PROFIdrive.  
A change always effects both parameters.

### r60022 PROFIsafe telegram selection

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Safety Integrated | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 901 | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the number of the PROFIsafe send and receive telegrams.  
The telegram settings are taken from the higher-level control system.

**Value:**
  
0:
No PROFIsafe telegram selected  
30:
PROFIsafe standard telegram 30, PZD-1/1  
901:
PROFIsafe SIEMENS telegram 901, PZD-3/5

**Dependency:**
  
  
Refer to:
p9611

### r60044 SI message buffer changes counter

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.2

**Description:**
  
Displays the changes of the safety message buffer.  
This counter is incremented every time that the safety message buffer changes.

**Recommend.:**
  
This is used to check whether the safety message buffer has been read out consistently.

### r60045[0...63] SI message code

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.2

**Description:**
  
Displays the numbers of safety messages that have occurred.

**Note:**
  
The messages type "safety message" (Cxxxxx) are entered in the message fault buffer.  
Message buffer structure (principle):  
r60047[0], r60048[0], r60049[0], r9753[0], r9754[0], r9755[0], r9756[0] --&gt; actual
message case, safety message 1  
...  
r60047[7], r60048[7], r60049[7], r9753[7], r9754[7], r9755[7], r9756[7] --&gt; actual
message case, safety message 8  
r60047[8], r60048[8], r60049[8], r9753[8], r9754[8], r9755[8], r9756[8] --&gt; 1st acknowledged
message case, safety message 1  
...  
r60047[15], r60048[15], r60049[15], r9753[15], r9754[15], r9755[15], r9756[15] --&gt;
1st acknowledged message case, safety message 8  
...  
r60047[56], r60048[56], r60049[56], r9753[56], r9754[56], r9755[56], r9756[56] --&gt;
7th acknowledged message case, safety message 1  
...  
r60047[63], r60048[63], r60049[63], r9753[63], r9754[63], r9755[63], r9756[63] --&gt;
7th acknowledged message case, safety message 8  
Parameter r60047[0...63] has the same content as r60045[0...63].

### r60047[0...63] SI message number

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.2

**Description:**
  
Displays the numbers of safety messages that have occurred.

**Note:**
  
The messages type "safety message" (Cxxxxx) are entered in the message fault buffer.  
Message buffer structure (principle):  
r60047[0], r60048[0], r60049[0], r9753[0], r9754[0], r9755[0], r9756[0] --&gt; actual
message case, safety message 1  
...  
r60047[7], r60048[7], r60049[7], r9753[7], r9754[7], r9755[7], r9756[7] --&gt; actual
message case, safety message 8  
r60047[8], r60048[8], r60049[8], r9753[8], r9754[8], r9755[8], r9756[8] --&gt; 1st acknowledged
message case, safety message 1  
...  
r60047[15], r60048[15], r60049[15], r9753[15], r9754[15], r9755[15], r9756[15] --&gt;
1st acknowledged message case, safety message 8  
...  
r60047[56], r60048[56], r60049[56], r9753[56], r9754[56], r9755[56], r9756[56] --&gt;
7th acknowledged message case, safety message 1  
...  
r60047[63], r60048[63], r60049[63], r9753[63], r9754[63], r9755[63], r9756[63] --&gt;
7th acknowledged message case, safety message 8  
Parameter r60047[0...63] has the same content as r60045[0...63].

### r60048[0...63] SI message time received in milliseconds

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [ms] | - [ms] | [ ] - [ms] |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.2

**Description:**
  
Displays the relative system runtime in milliseconds when the safety message occurred.

### r60049[0...63] SI message value

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.2

**Description:**
  
Displays the additional information about the safety message that occurred (as integer
number).

### p60052 SI message cases counter

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 65535 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.2

**Description:**
  
Number of safety messages that have occurred since the last reset.

**Dependency:**
  
The safety message buffer is cleared by resetting the parameter to 0.

**Note:**
  
The parameter is reset to 0 at POWER ON.

### r60100[0...4] PROFIdrive telegram display total

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**0 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.2

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
  
  
Refer to:
r0922, r60022, r60122

**Note:**
  
Value = 65564: no telegram active  
Value = 65565: MAP "Module Access Point"

### r60122 PROFIdrive SIC/SCC telegram selection

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 700 | 999 | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the telegram for the Safety Information Channel (SIC) / Safety Control Channel
(SCC).  
The telegram settings are taken from the higher-level control system.

**Value:**
  
700:
Supplementary telegram 700, PZD-0/3  
701:
Supplementary telegram 701, PZD-2/5  
999:
No telegram

### r61000[0...239] PROFINET Name of Station

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned8 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**- | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**0 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.2

**Description:**
  
Displays PROFINET Name of Station.

### r61001[0...3] PROFINET IP of Station

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned8 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**S210 | **P-Group:**- | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**0 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20SINAMICS%20S210.md#sinamics-alarms-sinamics-s210) |  |  |

**Valid as of version:**
  
5.2

**Description:**
  
Displays PROFINET IP of Station.

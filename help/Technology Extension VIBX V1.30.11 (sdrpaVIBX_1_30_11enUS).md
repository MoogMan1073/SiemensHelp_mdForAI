---
title: "Technology Extension VIBX V1.30.11"
package: sdrpaVIBX_1_30_11enUS
topics: 26
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Technology Extension VIBX V1.30.11

This section contains the parameter descriptions for the Technology Extension.
In the table of contents, you will then see a separate entry for each parameter number.

## SINAMICS Parameter VIBX 31580 - 31615

SINAMICS Parameter VIBX 31580 - 31615

### p31580 VIBX application mode

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C1( 3) | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7314, 7315 |
| **Object:**All objects | **P-Group:**Functions | **Version:**1301100 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 2 | [ 0 ] 0 |
| [Alarms](Technology%20Extension%20VIBX%20V1.30.11.md#technology-extension-vibx-v13011) |  |  |

**Valid as of version:**
  
1.4

**Description:**
  
Sets the application mode for VIBX.  
The VIBX technology extension implements a setpoint filter to reduce the natural vibrations
of a mechanical system. The position setpoint and the velocity setpoint are filtered.  
The "EPOS and LR" mode is the standard application. It is employed when the drive-internal
positioning is used ("basic positioner, EPOS" and "position controller LR" function
modules).  
The "DSC" mode is recommended when using an external position controller in a higher-level
control in conjunction with the DSC position controller.  
The "Inactive" mode deactivates the filter function. Status bit "Setpoint fixed" is
set (r32600.8 = 1), all filter outputs set to zero (r31601 = r31602 = r31603 = 0)
and alarm A52433 output.

**Value:**
  
0:
Inactive  
1:
EPOS and LR  
2:
DSC

**Dependency:**
  
  
Refer to:
A53433

**Note:**
  
DSC: Dynamic Servo Control  
VIBX: VIBration eXtinction (vibration absorber)  
If value = 1:  
The VIBX filter acts between the function modules "basic positioner, EPOS" and "position
controller (LR)".  
The following parameters are not effective:  
p31593, r31603  
If value = 2:  
The VIBX filter acts in front of the DSC position controller.  
The following parameters are not effective:  
p31592, p31595, r31602

### p31581 VIBX filter type

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7314, 7315 |
| **Object:**All objects | **P-Group:**Functions | **Version:**1301100 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 1 | [ 0 ] 0 |
| [Alarms](Technology%20Extension%20VIBX%20V1.30.11.md#technology-extension-vibx-v13011) |  |  |

**Valid as of version:**
  
1.4

**Description:**
  
Sets the filter type for VIBX.  
Depending on the selected filter type, the VIBX filter results in motion sequences
that take somewhat longer.

**Value:**
  
0:
Rugged  
1:
Sensitive

**Note:**
  
If value = 0:  
The rugged VIBX filter has a lower sensitivity to frequency offsets compared with
the sensitive filter type, but results in a higher delay of the motion sequence.  
The total motion sequence is extended by the time period Td (Td = 1/fd).  
If value = 1:  
The sensitive VIBX filter has a higher sensitivity to frequency offsets compared with
the rugged filter type, but results in a lower delay of the motion sequence.  
The total motion sequence is extended by half the time period Td/2 (Td = 1/fd).

### p31585[0...1] VIBX frequency fd

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7314, 7315, 7316 |
| **Object:**All objects | **P-Group:**Functions | **Version:**1301100 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.500 [Hz] | 10000.000 [Hz] | [ 0 ] 1.000 [Hz] |
| [Alarms](Technology%20Extension%20VIBX%20V1.30.11.md#technology-extension-vibx-v13011) |  |  |

**Valid as of version:**
  
1.4

**Description:**
  
Sets the frequency bandwidth of the damped natural vibration of the mechanical system.  
These frequencies can be determined by making the appropriate measurements.  
Value CI: p31610 = 0.0 (factory setting):  
The lower frequency applies (p31585[0]).  
0.0 <value CI: p31610 < 1.0:  
Linear interpolation is carried out between the lower and upper frequency.  
Value CI: p31610 = 1.0:  
The upper frequency applies (p31585[1]).

**Index:**
  
[
0]:
Lower frequency  
[
1]:
Upper frequency

**Dependency:**
  
  
Refer to:
p31610, p31611, r31613  
Refer to:
F53432

**Note:**
  
The maximum frequency that can be set depends on the filter sampling time.  
f_max = 1 / (2 * r31587)

### p31586 VIBX damping

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7314, 7315 |
| **Object:**All objects | **P-Group:**Functions | **Version:**1301100 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00000 | 0.99000 | [ 0 ] 0.00100 |
| [Alarms](Technology%20Extension%20VIBX%20V1.30.11.md#technology-extension-vibx-v13011) |  |  |

**Valid as of version:**
  
1.4

**Description:**
  
Sets the value for the damping of the natural mechanical vibration to be filtered.

**Note:**
  
The value for damping lies typically between 0.1... 3 % (D = 0.001 ... 0.03).

### r31587 VIBX sampling time effective

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7314, 7315 |
| **Object:**All objects | **P-Group:**Functions | **Version:**1301100 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [µs] | - [µs] | [ ] - [µs] |
| [Alarms](Technology%20Extension%20VIBX%20V1.30.11.md#technology-extension-vibx-v13011) |  |  |

**Valid as of version:**
  
1.4

**Description:**
  
Displays the effective sampling time of the VIBX filter.  
The value is automatically determined, and depends on the selected application mode
(p31580) and the corresponding setpoint channel.

### p31590 BI: VIBX activation

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 7314, 7315 |
| **Object:**All objects | **P-Group:**Functions | **Version:**1301100 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](Technology%20Extension%20VIBX%20V1.30.11.md#technology-extension-vibx-v13011) |  |  |

**Valid as of version:**
  
1.4

**Description:**
  
Sets the signal source to activate the VIBX filter.  
BI: p31590 = 1 signal:  
The setpoint filter is activated.  
For the transition from 0 to 1, the setpoint filter is coupled in (r31600.3 = 1).
Coupling-in has been completed when the "Filter active" status bit is set (r31600.4
= 1).  
BI: p31590 = 0 signal:  
The setpoint filter is deactivated.  
For the transition from 1 to 0, the setpoint filter is coupled out (r31600.5 = 1).
Coupling-out has been completed when the "Filter ready" status bit is set (r31600.2
= 1).

**Dependency:**
  
  
Refer to:
r31600

### p31591 CI: VIBX filter input position setpoint EPOS_LR/DSC

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Integer32 | **Dynamic index:**- | **Func. diagram:** 7314, 7315 |
| **Object:**All objects | **P-Group:**Functions | **Version:**1301100 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](Technology%20Extension%20VIBX%20V1.30.11.md#technology-extension-vibx-v13011) |  |  |

**Valid as of version:**
  
1.4

**Description:**
  
Sets the signal source for the position setpoint for the application mode "EPOS and
LR" (p31580 = 1) and "DSC" (p31580 = 2).

**Recommend.:**
  
The following BICO interconnection should be set as standard:  
- Application mode "EPOS and LR"  
CI: p31591 = r2665  
- application mode "DSC"  
CI: p31591 = r2060[x], x = 6, 7, 8 (depending on the selected PROFIdrive telegram
with XERR)

**Dependency:**
  
  
Refer to:
r31601

**Note:**
  
In application mode "DSC" (p31580 = 2) the signal is interpreted as position deviation
(XERR).

### p31592 CI: VIBX filter input velocity setpoint EPOS_LR

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Integer32 | **Dynamic index:**- | **Func. diagram:** 7314 |
| **Object:**All objects | **P-Group:**Functions | **Version:**1301100 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](Technology%20Extension%20VIBX%20V1.30.11.md#technology-extension-vibx-v13011) |  |  |

**Valid as of version:**
  
1.4

**Description:**
  
Sets the signal source for the velocity setpoint for the application mode "EPOS and
LR" (p31580 = 1).

**Recommend.:**
  
The following BICO interconnection should be set as standard:  
CI: p31592 = r2666

**Dependency:**
  
  
Refer to:
r31602

### p31593 CI: VIBX filter input velocity setpoint DSC

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7315 |
| **Object:**All objects | **P-Group:**Functions | **Version:**1301100 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**p2000 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](Technology%20Extension%20VIBX%20V1.30.11.md#technology-extension-vibx-v13011) |  |  |

**Valid as of version:**
  
1.4

**Description:**
  
Sets the signal source for the velocity setpoint for application mode "DSC" (p31580
= 2).

**Recommend.:**
  
The following BICO interconnection should be set as standard:  
CI: p31593 = r2060[1] (index corresponds to NSOLL_B in the PROFIdrive telegram)

**Dependency:**
  
  
Refer to:
r31603

### p31595 CI: VIBX input word EPOS

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Integer16 | **Dynamic index:**- | **Func. diagram:** 7314 |
| **Object:**All objects | **P-Group:**Functions | **Version:**1301100 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](Technology%20Extension%20VIBX%20V1.30.11.md#technology-extension-vibx-v13011) |  |  |

**Valid as of version:**
  
1.4

**Description:**
  
Sets the signal source for input word EPOS for application mode "EPOS and LR" (p31580
= 1).  
The signal "Setpoint fixed" (bit 2) is required from this input word (EPOS status
word 1).

**Recommend.:**
  
The following BICO interconnection should be set as standard:  
CI: p31595 = r2683

**Dependency:**
  
  
Refer to:
r31600

### p31596 CI: VIBX filter input position controller gain DSC

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7315 |
| **Object:**All objects | **P-Group:**Functions | **Version:**1301100 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](Technology%20Extension%20VIBX%20V1.30.11.md#technology-extension-vibx-v13011) |  |  |

**Valid as of version:**
  
1.4

**Description:**
  
Sets the signal source for the position controller gain "KPC" in application mode
"DSC" (p31580 = 2).

**Recommend.:**
  
The following BICO interconnection should be set as standard:  
CI: p31596 = r2060[9] (index corresponds to KPC in PROFIdrive telegram)

### r31600.0...13 CO/BO: VIBX status word

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 7314, 7315, 7316 |
| **Object:**All objects | **P-Group:**Functions | **Version:**1301100 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](Technology%20Extension%20VIBX%20V1.30.11.md#technology-extension-vibx-v13011) |  |  |

**Valid as of version:**
  
1.3

**Description:**
  
Display and BICO output for the status word for VIBX.

**Recommend.:**
  
For bit 08:  
For application mode "EPOS and LR", the following BICO interconnection should be set:  
BI: p2551 = r31600.8  
This bit is not interconnected for application mode "DSC".

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | "Filter not initialized" state | No | Yes | - |
| 02 | "Filter ready" state | No | Yes | - |
| 03 | "Filter being activated" state | No | Yes | - |
| 04 | "Filter active" state | No | Yes | - |
| 05 | "Filter being deactivated" state | No | Yes | - |
| 08 | Setpoint fixed | No | Yes | - |
| 09 | Frequency being changed | No | Yes | - |
| 10 | Frequency change limiting active | No | Yes | - |
| 11 | Dead time symmetrization activated | No | Yes | - |
| 12 | Immediate coupling-in possible | No | Yes | - |
| 13 | Tracking active | No | Yes | - |

**Dependency:**
  
  
Refer to:
p31590, p31595

**Note:**
  
For bit 00:  
An application mode has not been set (p31580).  
For bit 02:  
The setpoint filter is ready and can be coupled in.  
For bit 03:  
The filter is being coupled into the setpoint channel.  
For bit 04:  
The setpoint filter is activated.  
For bit 05:  
The filter is being coupled out of the setpoint channel.  
For bit 08:  
This bit is continually set in the "Inactive" mode (p32580 = 0).  
For bit 09:  
This bit is set while the effective frequency is being changed (CI: p31610).  
For bit 10:  
This bit is set if the change of the effective frequency is limited using p31611.  
For bit 11:  
Dead time symmetrization is activated via binector input p31612 = 1 signal.

### r31601 CO: VIBX filter output position setpoint EPOS_LR/DSC

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer32 | **Dynamic index:**- | **Func. diagram:** 7314, 7315 |
| **Object:**All objects | **P-Group:**Functions | **Version:**1301100 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](Technology%20Extension%20VIBX%20V1.30.11.md#technology-extension-vibx-v13011) |  |  |

**Valid as of version:**
  
1.4

**Description:**
  
Display and connector output for the position setpoint (filter output) for the application
mode "EPOS and LR" (p31580 = 1) and "DSC" (p31580 = 2).

**Recommend.:**
  
The following BICO interconnection should be set as standard:  
- Application mode "EPOS and LR"  
CI: p2530 = r31601  
- application mode "DSC"  
CI: p1190 = r31601

**Dependency:**
  
  
Refer to:
p31591

### r31602 CO: VIBX filter output velocity setpoint EPOS_LR

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer32 | **Dynamic index:**- | **Func. diagram:** 7314 |
| **Object:**All objects | **P-Group:**Functions | **Version:**1301100 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](Technology%20Extension%20VIBX%20V1.30.11.md#technology-extension-vibx-v13011) |  |  |

**Valid as of version:**
  
1.4

**Description:**
  
Display and connector output for velocity setpoint (filter output) for application
mode "EPOS and LR" (p31580 = 1).

**Recommend.:**
  
The following BICO interconnection should be set as standard:  
CI: p2531 = r31602

**Dependency:**
  
  
Refer to:
p31592

### r31603 CO: VIBX filter output velocity setpoint DSC

[SERVO](#r31603-co-vibx-filter-output-velocity-setpoint-dsc-1)

[SERVO Linear motor](#r31603-co-vibx-filter-output-velocity-setpoint-dsc-2)

#### r31603 CO: VIBX filter output velocity setpoint DSC

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7315 |
| **Object:**All objects | **P-Group:**Functions | **Version:**1301100 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**p2000 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [rpm] | - [rpm] | [ ] - [rpm] |
| [Alarms](Technology%20Extension%20VIBX%20V1.30.11.md#technology-extension-vibx-v13011) |  |  |

**Valid as of version:**
  
1.4

**Description:**
  
Display and connector output for velocity setpoint (filter output) for application
mode "DSC" (p31580 = 2).

**Recommend.:**
  
The following BICO interconnection should be set as standard:  
CI: p1430 = r31603

**Dependency:**
  
  
Refer to:
p31593

#### r31603 CO: VIBX filter output velocity setpoint DSC

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7315 |
| **Object:**SERVO (Lin) | **P-Group:**Functions | **Version:**1301100 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**p2000 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [m/min] | - [m/min] | [ ] - [m/min] |
| [Alarms](Technology%20Extension%20VIBX%20V1.30.11.md#technology-extension-vibx-v13011) |  |  |

**Valid as of version:**
  
1.4

**Description:**
  
Display and connector output for velocity setpoint (filter output) for application
mode "DSC" (p31580 = 2).

**Recommend.:**
  
The following BICO interconnection should be set as standard:  
CI: p1430 = r31603

**Dependency:**
  
  
Refer to:
p31593

### r31605 CO: VIBX filter difference position setpoint

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**4 |
| **Data type:**Integer32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**All objects | **P-Group:**Functions | **Version:**1301100 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](Technology%20Extension%20VIBX%20V1.30.11.md#technology-extension-vibx-v13011) |  |  |

**Valid as of version:**
  
1.3

**Description:**
  
Display and connector output for the position setpoint difference between the filter
input and filter output.

**Dependency:**
  
  
Refer to:
p31591, r31601

### p31610 CI: VIBX frequency fd interpolation signal source

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7314, 7315, 7316 |
| **Object:**All objects | **P-Group:**Functions | **Version:**1301100 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**PERCENT | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](Technology%20Extension%20VIBX%20V1.30.11.md#technology-extension-vibx-v13011) |  |  |

**Valid as of version:**
  
1.4

**Description:**
  
Sets the signal source for the interpolation of the active frequency fd.  
A frequency change is indicated in r31600.9.

**Dependency:**
  
If the frequency is to be changed while the axis is traversing, then dead time symmetrization
must be activated (BI: p31612 = 1).  
  
Refer to:
p31585, r31600, p31611, r31613

**Note:**
  
For value <= 0.0, frequency p31585[0] is active.  
For value >= 1.0, frequency p31585[1] is active.  
For 0.0 < value < 1.0, a linear interpolation is made between frequencies p31585[0]
and p31585[1].

### p31611 VIBX frequency fd maximum rate of change

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**4 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**All objects | **P-Group:**Functions | **Version:**1301100 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 20.0 [%] | 500.0 [%] | [ 0 ] 100.0 [%] |
| [Alarms](Technology%20Extension%20VIBX%20V1.30.11.md#technology-extension-vibx-v13011) |  |  |

**Valid as of version:**
  
1.4

**Description:**
  
Sets the maximum rate of change for the active frequency fd.  
Limiting becomes effective if the signal source of p31610 changes its value to quickly.  
Limiting is indicated in status bit r31600.10.

**Dependency:**
  
  
Refer to:
r31600, p31610, r31613

**Note:**
  
The lower this value, the slower the frequency can be changed.

### p31612 BI: VIBX dead time symmetrization activation

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 7314, 7315, 7316 |
| **Object:**All objects | **P-Group:**Functions | **Version:**1301100 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](Technology%20Extension%20VIBX%20V1.30.11.md#technology-extension-vibx-v13011) |  |  |

**Valid as of version:**
  
1.4

**Description:**
  
Sets the signal source to activate the dead time symmetrization when frequency fd
changes.  
BI: p31612 = 0 signal:  
Dead time symmetrization is deactivated. When the frequency changes, the filter dead
time also changes.  
BI: p31612 = 1 signal:  
Dead time symmetrization is activated. Symmetrization is carried out for a constant
dead time.

**Dependency:**
  
Dead time symmetrization must be activated in the following cases (BI: p31612 = 1):  
- for a frequency change of a traversing axis.  
- for interpolating axes. In this case, p31614 must also be set.  
  
Refer to:
p31585, p31614

**Note:**
  
A signal change only becomes effective when the axis comes to a standstill.

### r31613 CO: VIBX frequency fd active

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**All objects | **P-Group:**Functions | **Version:**1301100 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [Hz] | - [Hz] | [ ] - [Hz] |
| [Alarms](Technology%20Extension%20VIBX%20V1.30.11.md#technology-extension-vibx-v13011) |  |  |

**Valid as of version:**
  
1.4

**Description:**
  
Display and connector output for the active frequency fd.

**Dependency:**
  
  
Refer to:
p31585, p31610, p31611

### p31614 VIBX dead time symmetrization interpolating axes min. frequency

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**All objects | **P-Group:**Functions | **Version:**1301100 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.500 [Hz] | 10000.000 [Hz] | [ 0 ] 10000.000 [Hz] |
| [Alarms](Technology%20Extension%20VIBX%20V1.30.11.md#technology-extension-vibx-v13011) |  |  |

**Valid as of version:**
  
1.4

**Description:**
  
Sets the minimum frequency for the dead time symmetrization for interpolating axes.  
The minimum frequency should be kept to the factory setting for non-interpolating
axes.  
The following conditions must be satisfied for interpolating axes:  
1. The frequency set here must be less than or equal to the lowest frequency in p31585
for all interpolating axes.  
2. The filter type in p31581 must be set the same for all interpolating axes.  
3. Dead time symmetrization must be activated (BI: p31612 = 1 signal).

**Dependency:**
  
  
Refer to:
r31615

### r31615 CO: VIBX delay time additional sum

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**4 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**All objects | **P-Group:**Functions | **Version:**1301100 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [ms] | - [ms] | [ ] - [ms] |
| [Alarms](Technology%20Extension%20VIBX%20V1.30.11.md#technology-extension-vibx-v13011) |  |  |

**Valid as of version:**
  
1.4

**Description:**
  
Display and connector output for the delay time.  
The value comprises the delay time of the dead time symmetrization and the selected
symmetrization frequency (p31614).

**Dependency:**
  
  
Refer to:
p31612, p31614

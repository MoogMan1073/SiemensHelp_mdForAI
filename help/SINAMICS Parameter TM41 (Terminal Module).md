---
title: "SINAMICS Parameter TM41 (Terminal Module)"
package: sdrpa201enUS
topics: 578
source: Siemens TIA Portal Information System (offline help, en-US)
---


# SINAMICS Parameter TM41 (Terminal Module)

This section contains the parameter descriptions for the devices listed below. The parameter descriptions for the various devices can differ. If this is the case, then in the topic under "Object", the Control Unit is listed for which the description applies. In the table of contents, you will then see a separate entry for each parameter number. The following Control Units are taken into account in the online help:

- SINAMICS G120

## SINAMICS Parameter TM41 (Terminal Module) 00002 - 02083

SINAMICS Parameter TM41 (Terminal Module) 00002 - 02083

### r0002 TM41 operating display

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**TM41 | **P-Group:**- | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 250 | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Operating display for Terminal Module 41 (TM41).

**Value:**
  
0:
Operation - everything enabled  
10:
Operation - set "enable setpoint" = "1" (p1142)  
12:
Operation - RFG frozen, set "RFG start" = "1" (p1141)  
13:
Operation - set "enable RFG" = "1" (p1140)  
18:
Operation - brake on fault, remove fault, acknowledge  
21:
Ready for operation - set "Enable operation" = "1" (p0852)  
31:
Ready for switching on - set "ON/OFF1" = "0/1" (p0840)  
41:
Switching on inhibited - set "ON/OFF1" = "1/0" (p0840)  
42:
Switching on inhibited - set "OC/OFF2" = "1" (p0844)  
43:
Switching on inhibited - set "OC/OFF3" = "1" (p0848)  
45:
Switching on inhibited - remove fault cause, acknowledge fault  
46:
Switching on inhibited - exit commissioning mode (p0009, p0010)  
70:
Initialization  
120:
Module deactivated  
200:
Wait for booting/partial booting  
250:
Device signals a topology error

**Notice:**
  
For several missing enable signals, the corresponding value with the highest number
is displayed.

**Note:**
  
OC: Operating condition  
RFG: Ramp-function generator  
COMM: Commissioning

### p0005[0...1] BOP operating display selection

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**2 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, HUB | **P-Group:**- | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 65535 | [ 0 ] 2   [ 1 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the parameter number and parameter index for display for p0006 = 2, 4 for the
Basic Operator Panel (BOP).  
Examples for the SERVO drive object:  
p0005[0] = 21, p0005[1] = 0: Actual speed smoothed (r0021)  
p0005[0] = 25, p0005[1] = 0: Output voltage smoothed (r0025)

**Index:**
  
[
0]:
Parameter number  
[
1]:
Parameter index

**Dependency:**
  
  
Refer to:
p0006

**Note:**
  
Procedure:  
1.  
The parameter number to be displayed should be set in index 0. Only the monitoring
parameters (read-only parameters) can be set that actually exist for the actual drive
object.  
If the set parameter number is not indexed, or if there is an index in index 1 that
lies outside the valid range of the set parameter, then index 1 is automatically set
to 0.  
2.  
The index that belongs to the parameter set in index 0 should be set in index 1. The
permissible changes in index 1 always depend on the parameter number set in index
0.

### p0006 BOP operating display mode

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, HLA, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, HUB | **P-Group:**- | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 4 | 4 | [ 0 ] 4 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the mode of the operating display for the Basic Operator Panel (BOP) in the operating
states "ready for operation" and "operation".

**Value:**
  
4:
p0005

**Dependency:**
  
  
Refer to:
p0005

**Note:**
  
Mode 0 ... 3 can only be selected if also r0020, r0021 are available on the drive
object.  
Mode 4 is available for all drive objects.

### p0010 TM41 commissioning parameter filter

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 1) T | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**TM41 | **P-Group:**All groups | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 30 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the parameter filter for commissioning a Terminal Module 41 (TM41).  
Setting this parameter filters out the parameters that can be written into in the
various commissioning steps.  
For the BOP, this setting also causes the read access operations to be filtered.

**Value:**
  
0:
Ready  
4:
Encoder commissioning  
5:
Technological application/units  
29:
Only Siemens internal  
30:
Parameter reset

**Dependency:**
  
  
Refer to:
p0970

**Note:**
  
Procedure for "Reset parameter": Set p0010 to 30 and p0970 to 1.

### p0013[0...49] BOP user-defined list

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, HUB | **P-Group:**Functions | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 65535 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the required parameters to read and write via the Basic Operator Panel (BOP).  
Activation:  
1. p0003 = 3 (expert).  
2. p0013[0...49] = requested parameter number.  
3. If required, enter p0011 = password in order to prevent non-authorized deactivation.  
4. p0016 = 1 --&gt; activates the selected user-defined list.  
Deactivation/change:  
1. p0003 = 3 (expert).  
2. If required, p0012 = p0011, in order to be authorized to change or deactivate the
list.  
3. If required p0013[0...49] = required parameter number.  
4. p0016 = 1 --&gt; activates the modified user-defined list.  
5. p0003 = 0 --&gt; deactivates the user-defined list.

**Dependency:**
  
  
Refer to:
p0009, p0011, p0012, p0976

**Note:**
  
The following parameters can be read and written on the Control Unit drive object:  
- p0003 (access stage)  
- p0009 (device commissioning, parameter filter)  
- p0012 (BOP password acknowledgment (p0013))  
The following applies for the user-defined list:  
- password protection is only available on the drive object Control Unit and is valid
for all of the drive objects.  
- p0013 cannot be included in the user-defined list for all drive objects.  
- p0003, p0009, p0011, p0012, p0976 cannot, for the drive object Control Unit, be
included in the user-defined list.  
- the user-defined list can be cleared and deactivated "restore factory setting".  
A value of 0 means: Entry is empty.

### r0050.0...3 CO/BO: Command Data Set CDS effective

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**2 |
| **Data type:**Unsigned8 | **Dynamic index:**- | **Func. diagram:** 8560 |
| **Object:**SERVO, VECTOR, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_840, SERVO_COMBI, SERVO_828, SERVO_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM41 | **P-Group:**Displays, signals | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the effective Command Data Set (CDS).

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | CDS effective bit 0 | OFF | ON | - |
| 01 | CDS effective bit 1 | OFF | ON | - |
| 02 | CDS effective bit 2 | OFF | ON | - |
| 03 | CDS effective bit 3 | OFF | ON | - |

**Dependency:**
  
  
Refer to:
p0810, p0811, r0836

**Note:**
  
The Command Data Set selected using a binector input (e.g. p0810) is displayed using
r0836.

### r0051.0...4 CO/BO: Drive Data Set DDS effective

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**2 |
| **Data type:**Unsigned8 | **Dynamic index:**- | **Func. diagram:** 8565 |
| **Object:**SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, TM41, ENC, ENC_840 | **P-Group:**Displays, signals | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the effective Drive Data Set (DDS).

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | DDS effective bit 0 | OFF | ON | - |
| 01 | DDS effective bit 1 | OFF | ON | - |
| 02 | DDS effective bit 2 | OFF | ON | - |
| 03 | DDS effective bit 3 | OFF | ON | - |
| 04 | DDS effective bit 4 | OFF | ON | - |

**Dependency:**
  
  
Refer to:
p0820, p0821, p0822, p0823, p0824, r0837

**Note:**
  
The drive data set changeover is suppressed when selecting the motor identification,
during the rotating measurement, the encoder calibration and the friction characteristic
record.

### r0063 CO: Speed actual value

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**TM41 | **P-Group:**Displays, signals | **Version:**5207320 |
| **Units group:**3_1 | **Unit selection:**p0505 |  |
| **Not for motor type:**- | **Scaling:**p2000 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [rpm] | - [rpm] | [ ] - [rpm] |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display and connector output for the smoothed speed actual value.

**Note:**
  
For Terminal Module 41 (TM41), this value is used to interconnect with standard telegram
3 and is always zero.

### p0105 Activate/deactivate drive object

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**2 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**TM31, TM41, TM15 | **P-Group:**Closed-loop control | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 2 | [ 0 ] 1 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting to activate/deactivate a drive object.

**Value:**
  
0:
Deactivate drive object  
1:
Activate drive object  
2:
Drive object deactivate and not present

**Dependency:**
  
  
Refer to:
r0106  
Refer to:
A01314

**Warning:**
  
A drive that is moved by simulating the inputs of a Terminal Module is brought to
a standstill while this parameter is being changed over.

**Notice:**
  
The following applies when activating:  
If components are inserted for the first time and the appropriate drive object is
activated, then the drive system is automatically booted. To do this, the pulses of
all of the drive objects must be suppressed.

**Note:**
  
For value = 0, 2:  
When a drive object is deactivated it no longer outputs any errors.  
If value = 0:  
All components of the drive object were completely commissioned and are deactivated
using this value. They can be removed from the DRIVE-CLiQ without any error.  
If a component has been deactivated, only the component with the correct serial number
may be inserted, or none at all.  
If value = 1:  
All components of the drive object must be available for error-free operation.  
If value = 2:  
Components of a drive object in a project generated offline and set to this value
must never be inserted in the actual topology from the very start. This means that
the components are marked to be bypassed in the DRIVE-CLiQ line.  
For components that comprise several individual components (e.g. Double Motor Modules),
it is not permissible to set just one subset to this value.

### r0106 Drive object active/inactive

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**2 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, ENC, ENC_840, HUB, CU_LINK | **P-Group:**Closed-loop control | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 1 | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the "active/inactive" state of a drive object.

**Value:**
  
0:
Drive object inactive  
1:
Drive object active

**Dependency:**
  
  
Refer to:
p0105

### r0107 Drive object type

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**2 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**TM41 | **P-Group:**Closed-loop control | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 201 | 201 | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the type of each drive object.

**Value:**
  
201:
TM41 (Terminal Module)

**Dependency:**
  
  
Refer to:
p0103

**Note:**
  
DO: Drive Object

### r0108 Drive objects function module

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**2 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**TM31, TM41, TM15DI_DO, TM120, TM150, TB30 | **P-Group:**Closed-loop control | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the activated function module for the particular drive object.

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 18 | Free function blocks / FBLOCKS | Not activated | Activated | - |
| 31 | PROFINET CBE20 / PN CBE20 | Not activated | Activated | - |

**Dependency:**
  
  
Refer to:
r0171, r0172, r0173

**Note:**
  
A "function module" is a functional expansion of a drive object that can be activated
when commissioning.  
DO: Drive Object

### p0115[0] Sampling time for supplementary functions

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C1( 3) | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**TM41 | **P-Group:**Closed-loop control | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 [µs] | 16000.00 [µs] | [ 0 ] 4000.00 [µs] |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the sampling times for supplementary functions (DCC, free function blocks) on
this object.  
Only setting values that are an integer multiple of 125 µs are permissible.

**Index:**
  
[
0]:
Basic sampling time

**Note:**
  
This parameter only applies to set the sampling times of possible supplementary functions.  
The sampling times for inputs/outputs or encoder emulation must be set in p4099.

### r0116[0...1] Drive object clock cycle recommended

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TB30 | **P-Group:**Closed-loop control | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [µs] | - [µs] | [ ] - [µs] |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the recommended sampling time for the drive objects.  
r00116[0] = recommended sampling time:  
Recommended value which would then make the complete system operational.  
r00116[1] = recommended sampling time:  
Recommended value, which after changing other clock cycles on the DRIVE-CLiQ line,
would result in an operational system.

**Index:**
  
[
0]:
Change only for the actual drive object  
[
1]:
Changing all objects on the DRIVE-CLiQ line

**Dependency:**
  
  
Refer to:
p0115

### p0120 Number of Power unit Data Sets (PDS)

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C1( 3) C2( 15) | **Calculated:**- | **Access level:**2 |
| **Data type:**Unsigned8 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**SERVO, VECTOR, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_840, SERVO_828, SERVO_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM41 | **P-Group:**Data sets | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 1 | 8 | [ 0 ] 1 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the number of Power unit Data Sets (PDS).  
The value corresponds to the number of power units connected together for a parallel
circuit configuration.

**Dependency:**
  
  
Refer to:
r0107

**Note:**
  
This parameter is only significant for drive objects A_INF and VECTOR with a parallel
circuit configuration.

### p0151 Terminal Module component number

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C1( 4) C2( 15) | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned8 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TM54F_MA, TM54F_SL | **P-Group:**Data sets | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 199 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the component number for the Terminal Module.  
This unique component number is assigned when parameterizing the topology.  
Only component numbers can be entered into this parameter that correspond to a Terminal
Module.

### p0154 Terminal Module detection via LED

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**2 |
| **Data type:**Unsigned8 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TM54F_MA, TM54F_SL | **P-Group:**Terminals | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 1 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Detects the Terminal Module assigned to this drive and data set.

**Note:**
  
While p0154 = 1, the READY LED flashes green/orange or red/orange with 2 Hz at the
appropriate Terminal Module.

### r0157 Terminal Module EEPROM data version

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TM54F_MA, TM54F_SL | **P-Group:**Terminals | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the version of the EEPROM data of the Terminal Module.

**Dependency:**
  
  
Refer to:
r0127, r0147

**Note:**
  
Example:  
The value 1010100 should be interpreted as V01.01.01.00.

### r0158 Terminal Module firmware version

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TM54F_MA, TM54F_SL | **P-Group:**Terminals | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the firmware version of the Terminal Module.

**Dependency:**
  
  
Refer to:
r0018, r0128, r0148, r0197, r0198

**Note:**
  
Example:  
The value 1010100 should be interpreted as V01.01.01.00.

### p0170 Number of Command Data Sets (CDS)

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C1( 3) | **Calculated:**- | **Access level:**2 |
| **Data type:**Unsigned8 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**HLA, HLA_840, HLA_828, HLA_DBSI, TM41 | **P-Group:**Commands | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 1 | 1 | [ 0 ] 1 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the number of Command Data Sets (CDS).

**Note:**
  
It is possible to toggle between command parameters (BICO parameters) using this data
set changeover.

### r0171 Drive objects function module 1

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**2 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**VECTOR, HLA, VECTOR_G, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, HLA_840, HLA_828, HLA_DBSI, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM15DI_DO, TM120, TM150, TB30, ENC, ENC_840 | **P-Group:**Closed-loop control | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.7

**Description:**
  
Displays the activated function module for the particular drive object.

**Dependency:**
  
  
Refer to:
r0108, r0172, r0173

**Note:**
  
A "function module" is a functional expansion of a drive object that can be activated
when commissioning.

### r0172 Drive objects function module 2

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**2 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM15DI_DO, TM120, TM150, TB30, ENC, ENC_840 | **P-Group:**Closed-loop control | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.7

**Description:**
  
Displays the activated function module for the particular drive object.

**Dependency:**
  
  
Refer to:
r0108, r0171, r0173

**Note:**
  
A "function module" is a functional expansion of a drive object that can be activated
when commissioning.

### r0173 Drive objects function module 3

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**2 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM15DI_DO, TM120, TM150, TB30, ENC, ENC_840 | **P-Group:**Closed-loop control | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.7

**Description:**
  
Displays the activated function module for the particular drive object.

**Dependency:**
  
  
Refer to:
r0108, r0171, r0172

**Note:**
  
A "function module" is a functional expansion of a drive object that can be activated
when commissioning.

### p0180 Number of Drive Data Sets (DDS)

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C1( 3) C2( 15) | **Calculated:**- | **Access level:**2 |
| **Data type:**Unsigned8 | **Dynamic index:**- | **Func. diagram:** 8565 |
| **Object:**SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, TM41 | **P-Group:**Data sets | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 1 | 32 | [ 0 ] 1 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the number of Drive Data Sets (DDS).

### p0199[0...24] Drive object name

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C1( ) | **Calculated:**- | **Access level:**2 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**- | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 65535 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Freely assignable name for a drive object.  
For the commissioning tool, this name cannot be entered using the expert list, but
is specified in the configuration wizards. The object name can be subsequently modified
in the Project Navigator using standard Windows resources.

**Note:**
  
The parameter is not influenced by setting the factory setting.

### p0408 TM41 encoder emulation pulse number

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 4) | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 9674, 9676 |
| **Object:**TM41 | **P-Group:**Encoder | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 32 | 16384 | [ 0 ] 2048 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the pulse number output from the encoder emulation.

**Note:**
  
For p4408 = 0, the following applies:  
Parameters p0408 and p0418 have a double significance. They define the format of the
position actual value from the original encoder (TM41 input) and the format of the
TM41 output.  
In this case, the zero mark is only correctly output, if the two parameters p0408
and p0418 for the TM41 and the encoder interconnected at p4420 have the same setting.

### p0418 TM41 encoder emulation fine resolution Gx_XIST1 (in bits)

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 4) | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned8 | **Dynamic index:**- | **Func. diagram:** 9674, 9676 |
| **Object:**TM41 | **P-Group:**Encoder | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 2 | 18 | [ 0 ] 11 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the fine resolution in bits of the position actual value (r0479, r0482).

**Note:**
  
For p4408 = 0, the following applies:  
Parameters p0408 and p0418 have a double significance. They define the format of the
position actual value from the original encoder (TM41 input) and the format of the
TM41 output.  
In this case, the zero mark is only correctly output, if the two parameters p0408
and p0418 for the TM41 and the encoder interconnected at p4420 have the same setting.

### r0479 CO: TM41 encoder emulation diagnostics Gn_XIST1

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer32 | **Dynamic index:**- | **Func. diagram:** 9674, 9676 |
| **Object:**TM41 | **P-Group:**Encoder | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display and connector output for the encoder actual position value Gn_XIST1 according
to PROFIdrive for diagnostics.  
In contrast to r0482, the value is updated in each DRIVE-CLiQ basic clock cycle and
displayed with sign.

### r0481 CO: TM41 encoder emulation status word Gn_ZSW

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 9676 |
| **Object:**TM41 | **P-Group:**Encoder | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the encoder status word Gn_ZSW according to PROFIdrive.

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Function 1 active | No | Yes | - |
| 01 | Function 2 active | No | Yes | - |
| 02 | Function 3 active | No | Yes | - |
| 03 | Function 4 active | No | Yes | - |
| 04 | Value 1 | Not present | Displayed in r0483 | - |
| 05 | Value 2 | Not present | Displayed in r0483 | - |
| 06 | Value 3 | Not present | Displayed in r0483 | - |
| 07 | Value 4 | Not present | Displayed in r0483 | - |
| 08 | Measuring probe 1 deflected | No | Yes | - |
| 09 | Measuring probe 2 deflected | No | Yes | - |
| 11 | Encoder fault acknowledge active | No | Yes | 9676 |
| 13 | Absolute value cyclically | No | Displayed in r0483 | - |
| 14 | Parking encoder active | No | Yes | - |
| 15 | Encoder fault | None | Displayed in r0483 | - |

**Notice:**
  
Information on Gn_STW/Gn_ZSW can, e.g. be found in the following literature:  
SINAMICS S120 Function Manual Drive Functions

**Note:**
  
For p4401 = 0, the following applies:  
For Terminal Module 41 (TM41), this value is used to interconnect with standard telegram
3 and is always zero.  
For p4401 = 1, the following applies:  
r0481.0 indicates as to whether the zero mark synchronization is active.  
r0481.4 indicates whether the zero mark of the incremental encoder was found.  
r0481.14 indicates whether the output of track A/B is activated.

### r0482 CO: TM41 encoder emulation position actual value Gn_XIST1

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**TM41 | **P-Group:**Encoder | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display and connector output for the encoder actual position value Gn_XIST1 according
to PROFIdrive.

### r0483 CO: TM41 encoder emulation position actual value Gn_XIST2

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**TM41 | **P-Group:**Encoder | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the encoder actual position value Gn_XIST2 according to PROFIdrive.

**Notice:**
  
The encoder position actual value must be requested using the encoder control word
Gn_STW.13.

**Note:**
  
SIMOTION (p4400 = 0) operating mode:  
This value is used for interconnection with standard telegram 3 and is always zero.  
SINAMICS (p4400 = 1) operating mode:  
Once automatic zero mark synchronization is complete, the position of the zero mark
of the leading encoder is displayed in this parameter. The leading encoder is interconnected
via connector input p4420.

### p0491 Motor encoder fault response ENCODER

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**HLA, HLA_840, HLA_828, HLA_DBSI, TM41 | **P-Group:**Encoder | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 6 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the behavior for the ENCODER fault response (motor encoder).  
This means, for example, if an encoder fault occurs, encoderless operation can be
automatically selected with a shutdown behavior that can be selected.

**Value:**
  
0:
Encoder fault results in OFF2  
1:
Enc fault results in encoderless oper. and oper. continues  
2:
Encoder fault results in encoderless operation and OFF1  
3:
Encoder fault results in encoderless operation and OFF3  
4:
Encoder fault results in an armature short-cct int/DC braking  
5:
Enc fault results in encoderless op, operation continues, alarm  
6:
An encoder fault results in encoderless operation, alarm

**Dependency:**
  
The following parameters are relevant for encoderless operation.  
  
Refer to:
p0341, p0342, p1470, p1472, p1517, p1612, p1755  
Refer to:
F07575

**Caution:**
  
For a value = 1, 2, 3, 5, 6 the following applies:  
- encoderless operation must have been started.  
- if, for synchronous motors, an encoder fault occurs below the switchover speed p1755,
when switching over to encoderless operation, the motor can stall.  
For a value = 1, 5, 6, the following applies:  
- in spite of the motor encoder fault that has occurred, the motor continues to operate.

**Note:**
  
For a value = 1, 2, 3, 5, 6 the following applies:  
- Refer to the status signal "encoderless operation due to a fault" (BO: r1407.13).  
- if, with r1407.13 = 1, a different drive data set is selected (e.g. interconnection
from p0820), then the open-loop/closed-loop control mode p1300 of this data set must
match that of the original data set (e.g. p1300 = 21). Encoderless closed-loop controlled
operation is kept when changing over.  
For a value = 4, the following applies:  
- the value can only be set for all motor data sets when p1231 = 3, 4.  
- For synchronous motors, an armature short circuit is initiated on an encoder fault.  
- For induction motors, DC braking is initiated on an encoder fault. DC braking must
be commissioned (p1232, p1233, p1234).  
For a value = 5, 6 the following applies:  
Same function as for value = 1.  
However, faults are output as alarm and the message bit "Fault active" (r2139.3) is
not set. The encoder fault has to be acknowledged via the encoder interface in order
to resume operation with encoder.  
For a value 6, the following applies:  
The drive can be switched on again even with encoder malfunction - except for a topology
error.

### p0505 Selecting the system of units

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 5) | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_840, HLA_840, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, TM41, ENC, ENC_840 | **P-Group:**Applications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 1 | 4 | [ 0 ] 1 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the actual system of units.

**Value:**
  
1:
SI system of units  
2:
System of units referred/SI  
3:
US system of units  
4:
System of units referred/US

**Dependency:**
  
The parameter can only be changed in an offline project using the commissioning tool.

**Caution:**
  
If a per unit representation is selected and if the reference parameters (e.g. p2000)
are subsequently changed, then the physical significance of several control parameters
is also adapted at the same time. As a consequence, the control behavior can change
(see p1576, p1621, p1744, p1752, p1755 and p1609, p1612, p1619, p1620).

**Note:**
  
Reference parameter for the unit system % are, for example, p2000 ... p2004. Depending
on what has been selected, these are displayed using either SI or US units.

### p0528 Controller gain system of units

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 5) | **Calculated:**- | **Access level:**4 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**SERVO, HLA, SERVO_AC, SERVO_840, HLA_840, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, TM41, ENC, ENC_840 | **P-Group:**Applications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 1 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the system of units for the controller gains.

**Value:**
  
0:
Representation physical/% (p0505)  
1:
Representation no dimensions (referred)

**Note:**
  
The parameter is pre-assigned a value of 0 and cannot be changed.

### p0573 Inhibit automatic reference value calculation

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**2 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM41 | **P-Group:**Applications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 1 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting to inhibit the calculation of reference parameters (e.g. p2000) when automatically
calculating the motor and closed-loop control parameters (p0340, p3900).

**Value:**
  
0:
No  
1:
Yes

**Notice:**
  
The inhibit for the reference value calculation is canceled when new motor parameters
(e.g. p0305) are entered and only one drive data set exists (p0180 = 1). This is the
case during initial commissioning.  
Once the motor and control parameters have been calculated (p0340, p3900), the inhibit
for the reference value calculation is automatically re-activated.

**Note:**
  
If value = 0:  
The automatic calculation (p0340, p3900) overwrites the reference parameters.  
If value = 1:  
The automatic calculation (p0340, p3900) does not overwrite the reference parameters.

### p0819[0...2] Copy Drive Data Set DDS

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 15) | **Calculated:**- | **Access level:**2 |
| **Data type:**Unsigned8 | **Dynamic index:**- | **Func. diagram:** 8565 |
| **Object:**SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, TM41 | **P-Group:**Data sets | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 31 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Copies one Drive Data Set (DDS) into another.

**Index:**
  
[
0]:
Source Drive Data Set  
[
1]:
Target Drive Data Set  
[
2]:
Start copying procedure

**Note:**
  
Procedure:  
1. In Index 0, enter which drive data set is to be copied.  
2. In index 1, enter the drive data set data that is to be copied into.  
3. Start copying: set index 2 from 0 to 1.  
p0819[2] is automatically set to 0 when copying is completed.

### p0820[0...n] BI: Drive Data Set selection DDS bit 0

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**CDS, p0170 | **Func. diagram:** 8565, 8575 |
| **Object:**SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, TM41 | **P-Group:**Data sets | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source to select the Drive Data Set, bit 0 (DDS, bit 0).

**Dependency:**
  
  
Refer to:
r0051, r0837

**Notice:**
  
The parameter may be protected as a result of p0922 or p2079 and cannot be changed.

### p0821[0...n] BI: Drive Data Set selection DDS bit 1

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**CDS, p0170 | **Func. diagram:** 8565, 8570 |
| **Object:**SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, TM41 | **P-Group:**Data sets | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source to select the Drive Data Set, bit 1 (DDS, bit 1).

**Dependency:**
  
  
Refer to:
r0051, r0837

**Notice:**
  
The parameter may be protected as a result of p0922 or p2079 and cannot be changed.

### p0822[0...n] BI: Drive Data Set selection DDS bit 2

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**CDS, p0170 | **Func. diagram:** 8565 |
| **Object:**SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, TM41 | **P-Group:**Data sets | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source to select the Drive Data Set, bit 2 (DDS, bit 2).

**Dependency:**
  
  
Refer to:
r0051, r0837

**Notice:**
  
The parameter may be protected as a result of p0922 or p2079 and cannot be changed.

### p0823[0...n] BI: Drive Data Set selection DDS bit 3

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**CDS, p0170 | **Func. diagram:** 8565 |
| **Object:**SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, TM41 | **P-Group:**Data sets | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source to select the Drive Data Set, bit 3 (DDS, bit 3).

**Dependency:**
  
  
Refer to:
r0051, r0837

**Notice:**
  
The parameter may be protected as a result of p0922 or p2079 and cannot be changed.

### p0824[0...n] BI: Drive Data Set selection DDS bit 4

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**CDS, p0170 | **Func. diagram:** 8565, 8575 |
| **Object:**SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, TM41 | **P-Group:**Data sets | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source to select the Drive Data Set, bit 4 (DDS, bit 4).

**Dependency:**
  
  
Refer to:
r0051, r0837

**Notice:**
  
The parameter may be protected as a result of p0922 or p2079 and cannot be changed.

### r0835.2 CO/BO: Data set changeover status word

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**2 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 8575 |
| **Object:**EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, TM41, ENC, ENC_840 | **P-Group:**Displays, signals | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.4

**Description:**
  
Display and BICO output for the status word of the data set switchover.

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 02 | Internal parameter calculation active | No | Yes | - |

**Note:**
  
For bit 02:  
A data set changeover is delayed by the time required for the internal parameter calculation.

### r0836.0...3 CO/BO: Command Data Set CDS selected

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**2 |
| **Data type:**Unsigned8 | **Dynamic index:**- | **Func. diagram:** 8560 |
| **Object:**SERVO, VECTOR, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_840, SERVO_828, SERVO_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM41 | **P-Group:**Displays, signals | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the command data set (CDS) selected via the binector input.

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | CDS selection bit 0 | OFF | ON | - |
| 01 | CDS selection bit 1 | OFF | ON | - |
| 02 | CDS selection bit 2 | OFF | ON | - |
| 03 | CDS selection bit 3 | OFF | ON | - |

**Dependency:**
  
  
Refer to:
r0050, p0810, p0811

**Note:**
  
Command data sets are selected via binector input p0810 and following.  
The currently effective command data set is displayed in r0050.

### r0837.0...4 CO/BO: Drive Data Set DDS selected

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**2 |
| **Data type:**Unsigned8 | **Dynamic index:**- | **Func. diagram:** 8565 |
| **Object:**SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, TM41, ENC, ENC_840 | **P-Group:**Displays, signals | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the drive data set (DDS) selected via the binector input.

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | DDS selection bit 0 | OFF | ON | - |
| 01 | DDS selection bit 1 | OFF | ON | - |
| 02 | DDS selection bit 2 | OFF | ON | - |
| 03 | DDS selection bit 3 | OFF | ON | - |
| 04 | DDS selection bit 4 | OFF | ON | - |

**Dependency:**
  
  
Refer to:
r0051, p0820, p0821, p0822, p0823, p0824

**Note:**
  
Drive data sets are selected via binector input p0820 and following.  
The currently effective drive data set is displayed in r0051.  
If there is only one data set, then a value of 0 is displayed in this parameter and
not the selection via binector inputs.

### p0840 BI: ON / OFF (OFF1)

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 9677 |
| **Object:**TM41 | **P-Group:**Commands | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source for the command "ON/OFF (OFF1)".  
For the PROFIdrive profile, this command corresponds to control word 1 bit 0 (STW1.0).

**Recommend.:**
  
When the setting for this binector input is changed, the motor can only be switched
on by means of an appropriate signal change of the source.

**Dependency:**
  
  
Refer to:
p1055, p1056

**Caution:**
  
When "master control from PC" is activated, this binector input is ineffective.

**Notice:**
  
Only the signal source that originally switched on can also switch off again.  
The parameter may be protected as a result of p0922 or p2079 and cannot be changed.

**Note:**
  
BI: p0840 = 0 signal: OFF1 (pulse suppression and switching on inhibited)  
BI: p0840 = 0/1 signal: ON (pulses can be enabled)  
This parameter has no function in the "SINAMICS" (p4400 = 1) operating mode.

### p0844 BI: No coast-down / coast-down (OFF2)

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 9677 |
| **Object:**TM41 | **P-Group:**Commands | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 1 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source for the command "No coast down/coast down (OFF2)".  
For the PROFIdrive profile, this command corresponds to control word 1 bit 1 (STW1.1).  
BI: p0844 = 0 signal  
- OFF2 (immediate pulse suppression and switching on inhibited)  
BI: p0844 = 1 signal  
- no OFF2 (enable is possible)

**Caution:**
  
When "master control from PC" is activated, this binector input is ineffective.

**Notice:**
  
The parameter may be protected as a result of p0922 or p2079 and cannot be changed.

**Note:**
  
This parameter has no function in the "SINAMICS" (p4400 = 1) operating mode.

### p0848 BI: No Quick Stop / Quick Stop (OFF3)

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 9677 |
| **Object:**TM41 | **P-Group:**Commands | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 1 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the first signal source for the command "No quick stop/quick stop (OFF3)".  
For the PROFIdrive profile, this command corresponds to control word 1 bit 2 (STW1.2).  
BI: p0848 = 0 signal  
- OFF3 (braking along the OFF3 ramp (p1135), then pulse suppression and switching
on inhibited)  
BI: p0848 = 1 signal  
- no OFF3 (enable is possible)

**Caution:**
  
When "master control from PC" is activated, this binector input is ineffective.

**Notice:**
  
The parameter may be protected as a result of p0922 or p2079 and cannot be changed.

**Note:**
  
This parameter has no function in the "SINAMICS" (p4400 = 1) operating mode.

### p0852 BI: Enable operation/inhibit operation

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 9677 |
| **Object:**TM41 | **P-Group:**Commands | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 1 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source for the command "enable operation/inhibit operation".  
For the PROFIdrive profile, this command corresponds to control word 1 bit 3 (STW1.3).  
BI: p0852 = 0 signal  
Inhibit operation (suppress pulses).  
BI: p0852 = 1 signal  
Enable operation (pulses can be enabled).

**Caution:**
  
When "master control from PC" is activated, this binector input is ineffective.

**Notice:**
  
The parameter may be protected as a result of p0922 or p2079 and cannot be changed.

**Note:**
  
This parameter has no function in the "SINAMICS" (p4400 = 1) operating mode.

### p0854 BI: Control by PLC/no control by PLC

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 9677, 9678 |
| **Object:**TM41 | **P-Group:**Commands | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 1 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source for the command "control by PLC/no control by PLC".  
For the PROFIdrive profile, this command corresponds to control word 1 bit 10 (STW1.10).  
BI: p0854 = 0 signal  
No control by PLC  
BI: p0854 = 1 signal  
Master control by PLC.

**Dependency:**
  
  
Refer to:
p1155

**Caution:**
  
When "master control from PC" is activated, this binector input is ineffective.

**Notice:**
  
The parameter may be protected as a result of p0922 or p2079 and cannot be changed.

**Note:**
  
For the TM41, a response can be initiated using this bit if the control fails.  
The parameter is only effective in the "SIMOTION" operating mode (p4400 = 0).  
In the "SINAMICS" operating mode, the setpoints at connector input p4420 are evaluated
independently of p0854.  
Further, the setting of p2037 should be observed.

### r0898.0...13 CO/BO: Control word sequence control

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**2 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 9678 |
| **Object:**TM41 | **P-Group:**Displays, signals | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display and connector output for the control word of the sequence control.

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | ON/OFF1 | No | Yes | - |
| 01 | OC / OFF2 | No | Yes | - |
| 02 | OC / OFF3 | No | Yes | - |
| 03 | Enable operation | No | Yes | - |
| 04 | Enable ramp-function generator | No | Yes | - |
| 05 | Start ramp-function generator | No | Yes | - |
| 06 | Enable speed setpoint | No | Yes | - |
| 07 | Acknowledge fault | No | Yes | - |
| 10 | Master control by PLC | No | Yes | - |
| 13 | Zero mark enable | No | Yes | - |

**Note:**
  
OC: Operating condition

### r0899.0...15 CO/BO: Status word sequence control

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**2 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 9680 |
| **Object:**TM41 | **P-Group:**Displays, signals | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display and BICO output for the status word of the sequence control.

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Ready for switching on | No | Yes | - |
| 01 | Ready | No | Yes | - |
| 02 | Operation enabled | No | Yes | - |
| 04 | Coast down active | Yes | No | - |
| 05 | Quick Stop active | Yes | No | - |
| 06 | Switching on inhibited | No | Yes | - |
| 07 | Drive ready | No | Yes | - |
| 09 | Control request | No | Yes | - |
| 13 | Zero mark enabled | No | Yes | - |
| 14 | Track A/B enabled | No | Yes | - |
| 15 | Interface encoder emulation enabled | No | Yes | - |

**Note:**
  
For bit 00, 01, 02, 06:  
For PROFIdrive, these bits are used for status word 1.  
For bit 14, 15:  
These bits are set as soon as the following conditions are fulfilled:  
- STW.3 "Enable operation" is present (BI: p0852 = 1 signal).  
- Connector input p4420 is interconnected.  
- there are no disturbances/faults.

### p0922 IF1 PROFIdrive PZD telegram selection

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 1) T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 2401, 9677, 9679, 9681, 9683 |
| **Object:**TM41 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 3 | 999 | [ 0 ] 999 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the send and receive telegram.

**Value:**
  
3:
Standard telegram 3, PZD-5/9  
999:
Free telegram configuration with BICO

**Note:**
  
If a value is not equal to 999, a telegram is set and the automatically set interconnections
in the telegram are inhibited.  
The inhibited interconnections can only be changed again after setting value 999.

### p0925 PROFIdrive clock synchronous sign-of-life tolerance

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 2410 |
| **Object:**CU_I, CU_NX_CX, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_S150_PN, CU_S120_DP, CU_S150_DP, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR (n/M), HLA, VECTOR_G (n/M), SERVO_AC, VECTOR_AC (n/M), SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC (n/M), TM41, ENC, ENC_840 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 65535 | [ 0 ] 1 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the number of tolerated consecutive sign-of-life errors of the isochronous master.  
The sign-of-life signal is normally received in PZD4 (control word 2) from the master.

**Dependency:**
  
  
Refer to:
p2045, r2065  
Refer to:
F01912

**Note:**
  
The sign-of-life monitoring is disabled for p0925 = 65535.

### r0944 CO: Counter for fault buffer changes

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**2 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 8060 |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display and connector output for the counter for changes of the fault buffer.  
This counter is incremented every time the fault buffer changes.

**Recommend.:**
  
Used to check whether the fault buffer has been read out consistently.

**Dependency:**
  
  
Refer to:
r0945, r0947, r0948, r0949, r2109

### r0945[0...63] Fault code

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**2 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 8050, 8060 |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the numbers of faults that have occurred.

**Dependency:**
  
  
Refer to:
r0947, r0948, r0949, r2109, r2130, r2133, r2136, r3120, r3122

**Notice:**
  
The properties of the fault buffer should be taken from the corresponding product
documentation.

**Note:**
  
The buffer parameters are cyclically updated in the background (refer to status signal
in r2139).  
Fault buffer structure (general principle):  
r0945[0], r0949[0], r0948[0], r2109[0], r3115[0] --&gt; actual fault case, fault 1  
. . .  
r0945[7], r0949[7], r0948[7], r2109[7], r3115[7] --&gt; actual fault case, fault 8  
r0945[8], r0949[8], r0948[8], r2109[8], r3115[8] --&gt; 1st acknowledged fault case,
fault 1  
. . .  
r0945[15], r0949[15], r0948[15], r2109[15], r3115[15] --&gt; 1st acknowledged fault case,
fault 8  
. . .  
r0945[56], r0949[56], r0948[56], r2109[56], r3115[56] --&gt; 7th acknowledged fault case,
fault 1  
. . .  
r0945[63], r0949[63], r0948[63], r2109[63], r3115[63] --&gt; 7th acknowledged fault case,
fault 8

### r0947[0...63] Fault number

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 8050, 8060 |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
This parameter is identical to r0945.

### r0948[0...63] Fault time received in milliseconds

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 8050, 8060 |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [ms] | - [ms] | [ ] - [ms] |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the system runtime in milliseconds when the fault occurred.

**Dependency:**
  
  
Refer to:
r0945, r0947, r0949, r2109, r2114, r2130, r2133, r2136, r3115, r3120, r3122

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
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer32 | **Dynamic index:**- | **Func. diagram:** 8050, 8060 |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays additional information about the fault that occurred (as integer number).

**Dependency:**
  
  
Refer to:
r0945, r0947, r0948, r2109, r2130, r2133, r2136, r3115, r3120, r3122

**Note:**
  
The buffer parameters are cyclically updated in the background (refer to status signal
in r2139).  
The structure of the fault buffer and the assignment of the indices is shown in r0945.

### p0952 Fault cases counter

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 6700, 8060 |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 65535 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Number of fault situations that have occurred since the last reset.

**Dependency:**
  
The fault buffer is deleted (cleared) by setting p0952 to 0.  
In order that faults with "POWER ON" acknowledgment can also be cleared from the fault
buffer, POWER ON must first be carried out.  
  
Refer to:
r0945, r0947, r0948, r0949, r2109, r2130, r2133, r2136

### p0970 TM41 reset parameters

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 30) | **Calculated:**- | **Access level:**2 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**TM41 | **P-Group:**Factory settings | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 100 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
The parameter is used to initiate a reset of the parameters on Terminal Module 41
(TM41).  
Parameter p0151 is not reset. It is only reset if the entire drive unit is reset to
the factory settings (p0976).

**Value:**
  
0:
Inactive  
1:
Start a parameter reset  
100:
Start a BICO interconnection reset

**Dependency:**
  
  
Refer to:
p0010

**Notice:**
  
After the value has been modified, no further parameter modifications can be made
and the status is shown in r3996. Modifications can be made again when r3996 = 0.

**Note:**
  
A factory setting run can only be started if p0010 was first set to 30 (parameter
reset).  
At the end of the calculations, p0970 is automatically set to 0.

### p0971 Save drive object parameters

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**Factory settings | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 1 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting to save the parameter of the particular drive object in the non-volatile memory.  
When saving, only the adjustable parameters intended to be saved are taken into account.

**Value:**
  
0:
Inactive  
1:
Save drive object

**Dependency:**
  
  
Refer to:
p0977, p1960, p3845, r3996

**Warning:**
  
If the Control Unit power supply is switched off while data is being saved, then the
backup of all adjustable parameters can be lost, and the Control Unit must be recommissioned.

**Notice:**
  
The Control Unit power supply may only be switched off after data has been saved (i.e.
after data save has been started, wait until the parameter again has the value 0).  
Writing to parameters is inhibited while saving.  
The progress while saving is displayed in r3996.

**Note:**
  
Starting from the particular drive object, the following parameters are saved:  
CU3xx: Device-specific parameters and PROFIBUS device parameters.  
Other objects: Parameters of the actual object and PROFIBUS device parameters.  
Prerequisite:  
Before saving with p0971, all parameters (topology, all drive objects) must have been
saved at least once using p0977 = 1.

### r0975[0...10] Drive object identification

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**2 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the identification of the drive object.

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

### r0979[0...10] PROFIdrive encoder format

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 4704 |
| **Object:**TM41, ENC, ENC_840 | **P-Group:**Encoder | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

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
6...10]:
Reserved

**Note:**
  
Information about the individual indices can be taken from the following literature:  
PROFIdrive Profile Drive Technology

### p1035 BI: Zero marks enable

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 9677 |
| **Object:**TM41 | **P-Group:**Setpoints | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source to enable the zero marks.

**Notice:**
  
The parameter may be protected as a result of p0922 or p2079 and cannot be changed.

**Note:**
  
For TM41, this parameter has no function.  
The zero mark can only be switched in or switched out using p4401.

### r1082[0...n] Encoder emulation maximum speed

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**DDS, p0180 | **Func. diagram:** 9674, 9676 |
| **Object:**TM41 | **P-Group:**- | **Version:**5207320 |
| **Units group:**3_1 | **Unit selection:**p0505 |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [rpm] | - [rpm] | [ ] - [rpm] |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.4

**Description:**
  
Displays the frequency limit of the signal output as maximum speed for the encoder
emulation.  
The value is displayed independent of the operating mode set (p4400).

**Dependency:**
  
  
Refer to:
p0115  
Refer to:
F35220

### p1140 BI: Enable ramp-function generator/inhibit ramp-function generator

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 9678 |
| **Object:**TM41 | **P-Group:**Setpoints | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 1 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source for the command "enable ramp-function generator/inhibit ramp-function
generator".  
For the PROFIdrive profile, this command corresponds to control word 1 bit 4 (STW1.4).  
BI: p1140 = 0 signal:  
Inhibits the ramp-function generator (the ramp-function generator output is set to
zero).  
BI: p1140 = 1 signal:  
Enable ramp-function generator.

**Dependency:**
  
  
Refer to:
p1141, p1142

**Caution:**
  
When "master control from PC" is activated, this binector input is ineffective.

**Notice:**
  
The parameter may be protected as a result of p0922 or p2079 and cannot be changed.

**Note:**
  
This parameter has no function in the "SINAMICS" (p4400 = 1) operating mode.

### p1141 BI: Continue ramp-function generator/freeze ramp-function generator

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 9678 |
| **Object:**TM41 | **P-Group:**Setpoints | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 1 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source for the command "continue ramp-function generator/freeze ramp-function
generator".  
For the PROFIdrive profile, this command corresponds to control word 1 bit 5 (STW1.5).  
BI: p1141 = 0 signal:  
Freezes the ramp-function generator.  
BI: p1141 = 1 signal:  
Continue ramp-function generator.

**Dependency:**
  
  
Refer to:
p1140, p1142

**Caution:**
  
When "master control from PC" is activated, this binector input is ineffective.

**Notice:**
  
The parameter may be protected as a result of p0922 or p2079 and cannot be changed.

**Note:**
  
This parameter has no function in the "SINAMICS" (p4400 = 1) operating mode.

### p1142 BI: Enable setpoint/inhibit setpoint

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 9674, 9678 |
| **Object:**TM41 | **P-Group:**Setpoints | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 1 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source for the command "enable setpoint/inhibit setpoint".  
For the PROFIdrive profile, this command corresponds to control word 1 bit 6 (STW1.6).  
BI: p1142 = 0 signal  
Inhibits the setpoint (the ramp-function generator input is set to zero).  
BI: p1142 = 1 signal  
Setpoint enable.

**Dependency:**
  
  
Refer to:
p1140, p1141

**Caution:**
  
When "master control from PC" is activated, this binector input is ineffective.

**Notice:**
  
The parameter may be protected as a result of p0922 or p2079 and cannot be changed.

**Note:**
  
This parameter has no function in the "SINAMICS" (p4400 = 1) operating mode.

### p1155 CI: TM41 encoder emulation speed setpoint 1

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 9674 |
| **Object:**TM41 | **P-Group:**Setpoints | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**p2000 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source for speed setpoint 1 of the encoder emulation.  
The speed setpoint is processed corresponding to the sequencer of the TM41.

**Dependency:**
  
The effectiveness of this setpoint depends on control word 1 (STW1).  
  
Refer to:
r0898

**Notice:**
  
The parameter may be protected as a result of p0922 or p2079 and cannot be changed.

### p1189 TM41 encoder simulation configuration

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**2 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 9674 |
| **Object:**TM41 | **P-Group:**Setpoints | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0010 bin |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the configuration for the incremental encoder emulation.

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 01 | Interpol. op-loop ctrl /speed controller active | No | Yes | 9674 |

**Note:**
  
The parameter is not effective in the SINAMICS operating mode (p4400 = 1).  
For bit 01:  
The interpolator is only effective for isochronous PROFIBUS operation and when the
master receives a sign-of-life (STW 2.12 ... STW 2.15).

### p1412[0...n] TM41 increm. encoder emulation, speed setpoint filter deadtime

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**DDS, p0180 | **Func. diagram:** 9674 |
| **Object:**TM41 | **P-Group:**Closed-loop control | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**REL | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.000 [ms] | 1.000 [ms] | [ 0 ] 0.000 [ms] |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the delay of the speed setpoint for the incremental encoder emulation.

**Note:**
  
The parameter is not effective in the SINAMICS operating mode (p4400 = 1).

### p1414[0...n] TM41 incr. encoder emulation speed setpoint filter activation

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**DDS, p0180 | **Func. diagram:** 9674 |
| **Object:**TM41 | **P-Group:**Closed-loop control | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**REL | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0000 bin |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting for activating/deactivating speed setpoint filter 1 for the incremental encoder
emulation.

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Activate filter 1 | No | Yes | 9674 |

**Dependency:**
  
The speed setpoint filter can be parameterized using p1417 and p1418.  
  
Refer to:
p1417, p1418

**Note:**
  
The parameter is not effective in the SINAMICS operating mode (p4400 = 1).

### p1417[0...n] TM41 Speed setpoint filter 1 denominator natural frequency

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**DDS, p0180 | **Func. diagram:** 9674 |
| **Object:**TM41 | **P-Group:**Closed-loop control | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**REL | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.5 [Hz] | 16000.0 [Hz] | [ 0 ] 2000.0 [Hz] |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the denominator natural frequency for the speed setpoint filter 1 (PT2) of the
incremental encoder emulation.

**Dependency:**
  
  
Refer to:
p1414

**Note:**
  
The parameter is not effective in the SINAMICS operating mode (p4400 = 1).  
This parameter is only effective if the speed setpoint filter in p1414 is activated.  
The filter is only effective if the natural frequency is less than half of the sampling
frequency.

### p1418[0...n] TM41 Speed setpoint filter 1 denominator damping

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**DDS, p0180 | **Func. diagram:** 9674 |
| **Object:**TM41 | **P-Group:**Closed-loop control | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**REL | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.001 | 1.000 | [ 0 ] 0.700 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the denominator damping for the speed setpoint filter 1 (PT2) of the incremental
encoder emulation.

**Dependency:**
  
  
Refer to:
p1414

**Note:**
  
The parameter is not effective in the SINAMICS operating mode (p4400 = 1).  
This parameter is only effective if the speed setpoint filter in p1414 is activated.

### p2000 Reference speed reference frequency

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**2 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**TM41 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 6.00 [rpm] | 210000.00 [rpm] | [ 0 ] 3000.00 [rpm] |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the reference quantity for speed and frequency.  
All speeds or frequencies specified as relative value are referred to this reference
quantity.  
The reference quantity corresponds to 100% or 4000 hex (word) or 4000 0000 hex (double
word).

**Dependency:**
  
  
Refer to:
p2001, p2002, p2003, r2004

**Note:**
  
For the automatic calculation (p0340 = 1, p3900 &gt; 0) an appropriate pre-assignment
is only made if the parameter is not inhibited from being overwritten using p0573
= 1.  
If a BICO interconnection is established between different physical quantities, then
the particular reference quantities are used as internal conversion factor.  
Example 1:  
The signal of an analog input (e.g. r4055[0]) is connected to a speed setpoint (e.g.
p1070[0]). The actual percentage input value is cyclically converted into the absolute
speed setpoint using the reference speed (p2000).  
Example 2:  
The setpoint from PROFIBUS (r2050[1]) is connected to a speed setpoint (e.g. p1070[0]).
The actual input value is cyclically converted into a percentage value via the pre-specified
scaling 4000 hex. This percentage value is converted to the absolute speed setpoint
via reference speed (p2000).

### p2001 Reference voltage

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**CALC_MOD_ALL | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**SERVO, VECTOR, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_840, SERVO_COMBI, SERVO_828, SERVO_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM41 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 10 [Vrms] | 100000 [Vrms] | [ 0 ] 1000 [Vrms] |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the reference quantity for voltages.  
All voltages specified as relative value are referred to this reference quantity.
This also applies for direct voltage values (= rms value) like the DC link voltage.  
The reference quantity corresponds to 100% or 4000 hex (word) or 4000 0000 hex (double
word).  
Note:  
This reference quantity also applies to direct voltage values. It is not interpreted
as rms value, but as DC voltage value.

**Note:**
  
For the automatic calculation (p0340 = 1, p3900 &gt; 0) an appropriate pre-assignment
is only made if the parameter is not inhibited from being overwritten using p0573
= 1.  
If a BICO interconnection is established between different physical quantities, then
the particular reference quantities are used as internal conversion factor.  
For infeed units, the parameterized device supply voltage (p0210) is pre-assigned
as the reference quantity.  
Example:  
The actual value of the DC link voltage (r0070) is connected to a test socket (e.g.
p0771[0]). The actual voltage value is cyclically converted into a percentage of the
reference voltage (p2001) and output according to the parameterized scaling.

### p2002 Reference current

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**CALC_MOD_ALL | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**SERVO, VECTOR, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_840, SERVO_COMBI, SERVO_828, SERVO_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM41 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.10 [Arms] | 100000.00 [Arms] | [ 0 ] 100.00 [Arms] |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the reference quantity for currents.  
All currents specified as relative value are referred to this reference quantity.  
The reference quantity corresponds to 100% or 4000 hex (word) or 4000 0000 hex (double
word).

**Notice:**
  
If various DDS are used with different motor data, then the reference quantities remain
the same as these are not changed over with the DDS. The resulting conversion factor
should be taken into account (e.g. for trace records).  
Example:  
p2002 = 100 A  
Reference quantity 100 A corresponds to 100 %  
p0305[0] = 100 A  
Rated motor current 100 A for MDS0 in DDS0 --&gt; 100 % corresponds to 100 % of the rated
motor current  
p0305[1] = 50 A  
Rated motor current 50 A for MDS1 in DDS1 --&gt; 100 % corresponds to 200 % of the rated
motor current

**Note:**
  
For the automatic calculation (p0340 = 1, p3900 &gt; 0) an appropriate pre-assignment
is only made if the parameter is not inhibited from being overwritten using p0573
= 1.  
SERVO:  
Pre-assigned value for p0338 &gt; 0.001 is p0338, otherwise 2 * p0305.  
VECTOR:  
Pre-assigned value is p0640.  
If a BICO interconnection is established between different physical quantities, then
the particular reference quantities are used as internal conversion factor.  
For infeed units, the rated line current, which is obtained from the rated power and
parameterized rated line supply voltage (p2002 = r0206 / p0210 / 1.73) is pre-assigned
as the reference quantity.  
Example:  
The actual value of a phase current (r0069[0]) is connected to a test socket (e.g.
p0771[0]). The current actual value is cyclically converted into a percentage of the
reference current (p2002) and output according to the parameterized scaling.

### p2003 Reference torque

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**CALC_MOD_ALL | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**SERVO, VECTOR, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_840, SERVO_COMBI, SERVO_828, SERVO_DBSI, SERVO_I_AC, VECTOR_I_AC, TM41 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**7_2 | **Unit selection:**p0505 |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.01 [Nm] | 20000000.00 [Nm] | [ 0 ] 1.00 [Nm] |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the reference quantity for torque.  
All torques specified as relative value are referred to this reference quantity.  
The reference quantity corresponds to 100% or 4000 hex (word) or 4000 0000 hex (double
word).

**Note:**
  
For the automatic calculation (p0340 = 1, p3900 &gt; 0) an appropriate pre-assignment
is only made if the parameter is not inhibited from being overwritten using p0573
= 1.  
SERVO:  
Pre-assigned value for p0338 and p0334 &gt; 0.001 is p0338 * p0334, otherwise 2 * p0333.  
VECTOR:  
Pre-assigned value is 2 * p0333.  
If a BICO interconnection is established between different physical quantities, then
the particular reference quantities are used as internal conversion factor.  
Example:  
The actual value of the total torque (r0079) is connected to a test socket (e.g. p0771[0]).
The actual torque is cyclically converted into a percentage of the reference torque
(p2003) and output according to the parameterized scaling.

### r2004 Reference power

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**SERVO, VECTOR, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_840, SERVO_COMBI, SERVO_828, SERVO_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM41 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**14_10 | **Unit selection:**p0505 |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [kW] | - [kW] | [ ] - [kW] |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the reference quantity for power.  
All power ratings specified as relative value are referred to this reference quantity.  
The reference quantity corresponds to 100% or 4000 hex (word) or 4000 0000 hex (double
word).

**Dependency:**
  
This value is calculated as follows:  
Infeed: Calculated from voltage times current.  
Closed-loop control: Calculated from torque times speed.  
  
Refer to:
p2000, p2001, p2002, p2003

**Note:**
  
If a BICO interconnection is established between different physical quantities, then
the particular reference quantities are used as internal conversion factor.  
The reference power is calculated as follows:  
- 2 * Pi * reference speed / 60 * reference torque (motor)  
- reference voltage * reference current * root(3) (infeed)

### p2005 Reference angle

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**CALC_MOD_ALL | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM41 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 90.00 [°] | 180.00 [°] | [ 0 ] 90.00 [°] |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the reference quantity for angle.  
All angles specified as relative value are referred to this reference quantity.  
The reference quantity corresponds to 100% or 4000 hex (word) or 4000 0000 hex (double
word).

**Note:**
  
For the automatic calculation (p0340 = 1, p3900 &gt; 0) an appropriate pre-assignment
is only made if the parameter is not inhibited from being overwritten using p0573
= 1.  
If a BICO interconnection is established between different physical quantities, then
the particular reference quantities are used as internal conversion factor.

### p2006 Reference temperature

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**CALC_MOD_ALL | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM41 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**21_1 | **Unit selection:**p0505 |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 50.00 [°C] | 300.00 [°C] | [ 0 ] 100.00 [°C] |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.4

**Description:**
  
Sets the reference quantity for temperature.  
All temperatures specified as relative value are referred to this reference quantity.  
The reference quantity corresponds to 100% or 4000 hex (word) or 4000 0000 hex (double
word).

### p2007 Reference acceleration

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**CALC_MOD_ALL | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**SERVO, VECTOR, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_840, SERVO_COMBI, SERVO_828, SERVO_DBSI, SERVO_I_AC, VECTOR_I_AC, TM41 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.01 [rev/s²] | 500000.00 [rev/s²] | [ 0 ] 0.01 [rev/s²] |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the reference quantity for acceleration rates.  
All acceleration rates specified as relative value are referred to this reference
quantity.  
The reference quantity corresponds to 100% or 4000 hex (word) or 4000 0000 hex (double
word).

**Note:**
  
For the automatic calculation (p0340 = 1, p3900 &gt; 0) an appropriate pre-assignment
is only made if the parameter is not inhibited from being overwritten using p0573
= 1. If a BICO interconnection is established between different physical quantities,
then the particular reference quantities are used as internal conversion factor.  
The reference acceleration is calculated as follows:  
Reference speed (p2000) converted from 1/min to 1/s divided by 1 s  
--&gt; p2007 = p2000 [rpm] / (60 [s/min] * 1 [s])

### p2037 IF1 PROFIdrive STW1.10 = 0 mode

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM41, ENC, ENC_840 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 2 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the processing mode for PROFIdrive STW1.10 "master control by PLC".  
Generally, control world 1 is received with the first receive word (PZD1) (this is
in conformance to the PROFIdrive profile). The behavior of STW1.10 = 0 corresponds
to that of the PROFIdrive profile. For other applications that deviate from this,
the behavior can be adapted using this particular parameter.

**Recommend.:**
  
Do not change the setting p2037 = 0.

**Value:**
  
0:
Freeze setpoints and continue to process sign-of-life  
1:
Freeze setpoints and sign-of-life  
2:
Do not freeze setpoints

**Note:**
  
If the STW1 is not transferred according to the PROFIdrive with PZD1 (with bit 10
"master control by PLC"), then p2037 should be set to 2.

### p2044 IF1 PROFIdrive fault delay

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 2410 |
| **Object:**SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM41, ENC, ENC_840 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 [s] | 100 [s] | [ 0 ] 0 [s] |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the delay time to initiate fault F01910 after a setpoint failure.  
The time until the fault is initiated can be used by the application. This means that
it is possible to respond to the failure while the drive is still operational (e.g.
emergency retraction).

**Dependency:**
  
  
Refer to:
r2043  
Refer to:
F01910

### p2045 CI: PB/PN clock synchronous controller sign-of-life signal source

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Integer16 | **Dynamic index:**- | **Func. diagram:** 2410 |
| **Object:**CU_I, CU_NX_CX, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_S150_PN, CU_S120_DP, CU_S150_DP, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR (n/M), HLA, VECTOR_G (n/M), SERVO_AC, VECTOR_AC (n/M), SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC (n/M), TM41, ENC, ENC_840 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Connector input for the sign-of-life of the clock synchronous PROFIBUS/PROFINET controller.  
The sign-of-life is expected at bits 12 to 15. Bits 0 to 11 are not evaluated.  
The sign-of-life signal is normally received in PZD4 (control word 2) from the controller.

**Dependency:**
  
  
Refer to:
p0925, r2065

**Notice:**
  
The parameter may be protected as a result of p0922 or p2079 and cannot be changed.

### r2050[0...21] CO: IF1 PROFIdrive PZD receive word

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 2440, 2468 |
| **Object:**SERVO, HLA, SERVO_AC, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, TM41 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**4000H | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
5.2

**Description:**
  
Connector output to interconnect PZD (setpoints) with word format received from the
fieldbus controller.

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

**Notice:**
  
Where there is a multiple interconnection of a connector output, all the connector
inputs must either have Integer or FloatingPoint data types.  
A BICO interconnection for a single PZD can only take place either on r2050 or r2060.

**Note:**
  
IF1: Interface 1

### p2051[0...27] CI: IF1 PROFIdrive PZD send word

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Integer16 | **Dynamic index:**- | **Func. diagram:** 2470 |
| **Object:**SERVO, HLA, SERVO_AC, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, TM41 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**4000H | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0...27 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.4

**Description:**
  
Selects the PZD (actual values) with word format to be sent to the fieldbus controller.

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
  
  
Refer to:
p2061

**Notice:**
  
The parameter may be protected as a result of p0922 or p2079 and cannot be changed.

**Note:**
  
IF1: Interface 1

### r2053[0...27] IF1 PROFIdrive diagnostics PZD send word

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 2450, 2470 |
| **Object:**SERVO, HLA, SERVO_AC, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, TM41 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.4

**Description:**
  
Displays the PZD (actual values) with word format sent to the fieldbus controller.

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

**Dependency:**
  
  
Refer to:
p2051, p2061

**Note:**
  
IF1: Interface 1

### r2060[0...20] CO: IF1 PROFIdrive PZD receive double word

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer32 | **Dynamic index:**- | **Func. diagram:** 2440, 2468 |
| **Object:**SERVO, HLA, SERVO_AC, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, TM41 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**4000H | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
5.2

**Description:**
  
Connector output to interconnect PZD (setpoints) with double word format received
from the fieldbus controller.

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

**Notice:**
  
Where there is a multiple interconnection of a connector output, all the connector
inputs must either have Integer or FloatingPoint data types.  
A BICO interconnection for a single PZD can only take place either on r2050 or r2060.  
A maximum of 4 indices of the "trace" function can be used.

**Note:**
  
IF1: Interface 1

### p2061[0...26] CI: IF1 PROFIdrive PZD send double word

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Integer32 | **Dynamic index:**- | **Func. diagram:** 2470 |
| **Object:**SERVO, HLA, SERVO_AC, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, TM41 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**4000H | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.4

**Description:**
  
Selects the PZD (actual values) with double word format to be sent to the fieldbus
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
  
  
Refer to:
p2051

**Notice:**
  
A BICO interconnection for a single PZD can only take place either on p2051 or p2061.  
The parameter may be protected as a result of p0922 or p2079 and cannot be changed.

**Note:**
  
IF1: Interface 1

### r2063[0...26] IF1 PROFIdrive diagnostics PZD send double word

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 2450, 2470 |
| **Object:**SERVO, HLA, SERVO_AC, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, TM41 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.4

**Description:**
  
Displays the PZD (actual values) with double word format sent to the fieldbus controller.

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

**Notice:**
  
A maximum of 4 indices of the "trace" function can be used.

**Note:**
  
IF1: Interface 1

### r2065 PB/PN controller sign of life diagnostics

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 2410 |
| **Object:**CU_I, CU_NX_CX, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_S150_PN, CU_S120_DP, CU_S150_DP, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR (n/M), HLA, VECTOR_G (n/M), SERVO_AC, VECTOR_AC (n/M), SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC (n/M), TM41, ENC, ENC_840 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays how often the sign-of-life from the clock synchronous PROFIBUS/PROFINET controller
last failed.  
An appropriate fault is output when the tolerance, specified in p0925, is exceeded.

**Dependency:**
  
  
Refer to:
F01912

### r2067[0...1] IF1 PZD maximum interconnected

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM15DI_DO, TM120, TM150, TB30, ENC, ENC_840 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.5

**Description:**
  
Display for the maximum interconnected PZD in the receive/send direction  
Index 0: receive (r2050, r2060)  
Index 1: send (p2051, p2061)

### r2074[0...21] IF1 PROFIdrive diagnostics bus address PZD receive

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**SERVO, HLA, SERVO_AC, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, TM41 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
5.2

**Description:**
  
Displays the PROFIBUS address of the sender from which the process data (PZD) is received.

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

**Note:**
  
IF1: Interface 1  
Value range:  
0 - 125: Bus address of the sender  
65535: Not assigned

### r2075[0...21] IF1 PROFIdrive diagnostics telegram offset PZD receive

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 2410 |
| **Object:**SERVO, HLA, SERVO_AC, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, TM41 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
5.2

**Description:**
  
Displays the PZD byte offset in the PROFIdrive receive telegram (controller output).

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

**Note:**
  
IF1: Interface 1  
Value range:  
0 - 242: Byte offset  
65535: Not assigned

### r2076[0...27] IF1 PROFIdrive diagnostics telegram offset PZD send

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 2410 |
| **Object:**SERVO, HLA, SERVO_AC, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, TM41 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.4

**Description:**
  
Displays the PZD byte offset in the PROFIdrive send telegram (controller input).

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

**Note:**
  
IF1: Interface 1  
Value range:  
0 - 242: Byte offset  
65535: Not assigned

### p2079 IF1 PROFIdrive PZD telegram selection extended

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**TM41 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 3 | 999 | [ 0 ] 999 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the send and receive telegram.  
Contrary to p0922, a telegram can be selected using p2079 and subsequently expanded.

**Value:**
  
3:
Standard telegram 3, PZD-5/9  
999:
Free telegram configuration with BICO

**Dependency:**
  
  
Refer to:
p0922

**Note:**
  
For p0922 &lt; 999 the following applies:  
p2079 has the same value and is inhibited. All of the interconnections and extensions
contained in the telegram are inhibited.  
For p0922 = 999 the following applies:  
p2079 can be freely set. If p2079 is also set to 999, then all of the interconnections
can be set.  
For p0922 = 999 and p2079 &lt; 999 the following applies:  
The interconnections contained in the telegram are inhibited. However, the telegram
can be extended.

### p2080[0...15] BI: IF1 binector-connector converter status word 1

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 2472 |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM15DI_DO, TM120, TM150, TB30, ENC, ENC_840 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Selects bits to be sent to the PROFIdrive controller.  
The individual bits are combined to form status word 1.

**Index:**
  
[
0]:
Bit 0  
[
1]:
Bit 1  
[
2]:
Bit 2  
[
3]:
Bit 3  
[
4]:
Bit 4  
[
5]:
Bit 5  
[
6]:
Bit 6  
[
7]:
Bit 7  
[
8]:
Bit 8  
[
9]:
Bit 9  
[
10]:
Bit 10  
[
11]:
Bit 11  
[
12]:
Bit 12  
[
13]:
Bit 13  
[
14]:
Bit 14  
[
15]:
Bit 15

**Dependency:**
  
  
Refer to:
p2088, r2089

**Notice:**
  
The parameter may be protected as a result of p0922 or p2079 and cannot be changed.

### p2081[0...15] BI: IF1 binector-connector converter status word 2

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 2472 |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM15DI_DO, TM120, TM150, TB30, ENC, ENC_840 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Selects bits to be sent to the PROFIdrive controller.  
The individual bits are combined to form status word 2.

**Index:**
  
[
0]:
Bit 0  
[
1]:
Bit 1  
[
2]:
Bit 2  
[
3]:
Bit 3  
[
4]:
Bit 4  
[
5]:
Bit 5  
[
6]:
Bit 6  
[
7]:
Bit 7  
[
8]:
Bit 8  
[
9]:
Bit 9  
[
10]:
Bit 10  
[
11]:
Bit 11  
[
12]:
Bit 12  
[
13]:
Bit 13  
[
14]:
Bit 14  
[
15]:
Bit 15

**Dependency:**
  
  
Refer to:
p2088, r2089

**Notice:**
  
The parameter may be protected as a result of p0922 or p2079 and cannot be changed.

**Note:**
  
For clock synchronous operation, bit 12 to 15 to transfer the sign-of-life are reserved
in status word 2 - and may not be freely interconnected.

### p2082[0...15] BI: IF1 binector-connector converter status word 3

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 2472 |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM15DI_DO, TM120, TM150, TB30, ENC, ENC_840 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Selects bits to be sent to the PROFIdrive controller.  
The individual bits are combined to form free status word 3.

**Index:**
  
[
0]:
Bit 0  
[
1]:
Bit 1  
[
2]:
Bit 2  
[
3]:
Bit 3  
[
4]:
Bit 4  
[
5]:
Bit 5  
[
6]:
Bit 6  
[
7]:
Bit 7  
[
8]:
Bit 8  
[
9]:
Bit 9  
[
10]:
Bit 10  
[
11]:
Bit 11  
[
12]:
Bit 12  
[
13]:
Bit 13  
[
14]:
Bit 14  
[
15]:
Bit 15

**Dependency:**
  
  
Refer to:
p2088, r2089

**Notice:**
  
The parameter may be protected as a result of p0922 or p2079 and cannot be changed.

### p2083[0...15] BI: IF1 binector-connector converter status word 4

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 2472 |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM15DI_DO, TM120, TM150, TB30, ENC, ENC_840 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Selects bits to be sent to the PROFIdrive controller.  
The individual bits are combined to form free status word 4.

**Index:**
  
[
0]:
Bit 0  
[
1]:
Bit 1  
[
2]:
Bit 2  
[
3]:
Bit 3  
[
4]:
Bit 4  
[
5]:
Bit 5  
[
6]:
Bit 6  
[
7]:
Bit 7  
[
8]:
Bit 8  
[
9]:
Bit 9  
[
10]:
Bit 10  
[
11]:
Bit 11  
[
12]:
Bit 12  
[
13]:
Bit 13  
[
14]:
Bit 14  
[
15]:
Bit 15

**Dependency:**
  
  
Refer to:
p2088, r2089

## SINAMICS Parameter TM41 (Terminal Module) 02084 - 04154

SINAMICS Parameter TM41 (Terminal Module) 02084 - 04154

### p2084[0...15] BI: IF1 binector-connector converter status word 5

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 2472 |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM15DI_DO, TM120, TM150, TB30, ENC, ENC_840 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Selects bits to be sent to the PROFIdrive controller.  
The individual bits are combined to form free status word 5.

**Index:**
  
[
0]:
Bit 0  
[
1]:
Bit 1  
[
2]:
Bit 2  
[
3]:
Bit 3  
[
4]:
Bit 4  
[
5]:
Bit 5  
[
6]:
Bit 6  
[
7]:
Bit 7  
[
8]:
Bit 8  
[
9]:
Bit 9  
[
10]:
Bit 10  
[
11]:
Bit 11  
[
12]:
Bit 12  
[
13]:
Bit 13  
[
14]:
Bit 14  
[
15]:
Bit 15

**Dependency:**
  
  
Refer to:
p2088, r2089

### p2088[0...4] IF1 invert binector-connector converter status word

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 2472 |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM15DI_DO, TM120, TM150, TB30, ENC, ENC_840 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0000 0000 0000 0000 bin |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting to invert the individual binector inputs of the binector-connector converter.

**Index:**
  
[
0]:
Status word 1  
[
1]:
Status word 2  
[
2]:
Free status word 3  
[
3]:
Free status word 4  
[
4]:
Free status word 5

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Bit 0 | Not inverted | Inverted | - |
| 01 | Bit 1 | Not inverted | Inverted | - |
| 02 | Bit 2 | Not inverted | Inverted | - |
| 03 | Bit 3 | Not inverted | Inverted | - |
| 04 | Bit 4 | Not inverted | Inverted | - |
| 05 | Bit 5 | Not inverted | Inverted | - |
| 06 | Bit 6 | Not inverted | Inverted | - |
| 07 | Bit 7 | Not inverted | Inverted | - |
| 08 | Bit 8 | Not inverted | Inverted | - |
| 09 | Bit 9 | Not inverted | Inverted | - |
| 10 | Bit 10 | Not inverted | Inverted | - |
| 11 | Bit 11 | Not inverted | Inverted | - |
| 12 | Bit 12 | Not inverted | Inverted | - |
| 13 | Bit 13 | Not inverted | Inverted | - |
| 14 | Bit 14 | Not inverted | Inverted | - |
| 15 | Bit 15 | Not inverted | Inverted | - |

**Dependency:**
  
  
Refer to:
p2080, p2081, p2082, p2083, r2089

### r2089[0...4] CO: IF1 send binector-connector converter status word

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 2472 |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM15DI_DO, TM120, TM150, TB30, ENC, ENC_840 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Connector output to interconnect the status words to a PZD send word.

**Index:**
  
[
0]:
Status word 1  
[
1]:
Status word 2  
[
2]:
Free status word 3  
[
3]:
Free status word 4  
[
4]:
Free status word 5

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

**Dependency:**
  
  
Refer to:
p2051, p2080, p2081, p2082, p2083

**Note:**
  
r2089 together with p2080 to p2084 forms five binector-connector converters.

### r2090.0...15 BO: IF1 PROFIdrive PZD1 receive bit-serial

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 2468 |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM15DI_DO, TM120, TM150, TB30, ENC, ENC_840 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Binector output for bit-serial interconnection of PZD1 (normally control word 1) received
from the PROFIdrive controller.

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

**Note:**
  
IF1: Interface 1

### r2091.0...15 BO: IF1 PROFIdrive PZD2 receive bit-serial

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 2468 |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM15DI_DO, TM120, TM150, TB30, ENC, ENC_840 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Binector output for bit-serial interconnection of PZD2 received from the PROFIdrive
controller.

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

**Note:**
  
IF1: Interface 1

### r2092.0...15 BO: IF1 PROFIdrive PZD3 receive bit-serial

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 2468 |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, TM41, ENC, ENC_840 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Binector output for bit-serial interconnection of PZD3 received from the PROFIdrive
controller.

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

**Note:**
  
IF1: Interface 1

### r2093.0...15 BO: IF1 PROFIdrive PZD4 receive bit-serial

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 2468 |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, TM41, ENC, ENC_840 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Binector output for bit-serial interconnection of PZD4 (normally control word 2) received
from the PROFIdrive controller.

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

**Note:**
  
IF1: Interface 1

### r2094.0...15 BO: IF1 connector-binector converter binector output

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 2468 |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM15DI_DO, TM120, TM150, TB30, ENC, ENC_840 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Binector output for bit-serial onward interconnection of a PZD word received from
the PROFIdrive controller.  
The PZD is selected via p2099[0].

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

**Dependency:**
  
  
Refer to:
p2099

### r2095.0...15 BO: IF1 connector-binector converter binector output

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 2468 |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM15DI_DO, TM120, TM150, TB30, ENC, ENC_840 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Binector output for bit-serial interconnection of a PZD word received from the PROFIdrive
controller.  
The PZD is selected via p2099[1].

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

**Dependency:**
  
  
Refer to:
p2099

### p2098[0...1] IF1 invert connector-binector converter binector output

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 2468 |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM15DI_DO, TM120, TM150, TB30, ENC, ENC_840 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0000 0000 0000 0000 bin |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting to invert the individual binector outputs of the connector-binector converter.  
Using p2098[0], the signals of connector input p2099[0] are influenced.  
Using p2098[1], the signals of connector input p2099[1] are influenced.

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Bit 0 | Not inverted | Inverted | - |
| 01 | Bit 1 | Not inverted | Inverted | - |
| 02 | Bit 2 | Not inverted | Inverted | - |
| 03 | Bit 3 | Not inverted | Inverted | - |
| 04 | Bit 4 | Not inverted | Inverted | - |
| 05 | Bit 5 | Not inverted | Inverted | - |
| 06 | Bit 6 | Not inverted | Inverted | - |
| 07 | Bit 7 | Not inverted | Inverted | - |
| 08 | Bit 8 | Not inverted | Inverted | - |
| 09 | Bit 9 | Not inverted | Inverted | - |
| 10 | Bit 10 | Not inverted | Inverted | - |
| 11 | Bit 11 | Not inverted | Inverted | - |
| 12 | Bit 12 | Not inverted | Inverted | - |
| 13 | Bit 13 | Not inverted | Inverted | - |
| 14 | Bit 14 | Not inverted | Inverted | - |
| 15 | Bit 15 | Not inverted | Inverted | - |

**Dependency:**
  
  
Refer to:
r2094, r2095, p2099

### p2099[0...1] CI: IF1 connector-binector converter signal source

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Integer16 | **Dynamic index:**- | **Func. diagram:** 2468 |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM15DI_DO, TM120, TM150, TB30, ENC, ENC_840 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source for the connector-binector converter.  
A PZD receive word can be selected as signal source. The signals are available to
be serially passed-on (interconnection).

**Dependency:**
  
  
Refer to:
r2094, r2095

**Note:**
  
From the signal source set via the connector input, the corresponding lower 16 bits
are converted.  
p2099[0...1] together with r2094.0...15 and r2095.0...15 forms two connector-binector
converters:  
Connector input p2099[0] to binector output in r2094.0...15  
Connector input p2099[1] to binector output in r2095.0...15

### p2100[0...19] Change fault response fault number

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 8050, 8075 |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 65535 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Selects the faults for which the fault response should be changed

**Dependency:**
  
The fault is selected and the required response is set under the same index.  
  
Refer to:
p2101

**Note:**
  
Re-parameterization is also possible if a fault is present. The change only becomes
effective after the fault has been resolved.

### p2101[0...19] Change fault response response

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 8050, 8075 |
| **Object:**SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_I_AC, VECTOR_I_AC, TM41 | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 7 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the fault response for the selected fault.

**Value:**
  
0:
NONE  
1:
OFF1  
2:
OFF2  
3:
OFF3  
5:
STOP2  
6:
Internal armature short-circuit / DC braking  
7:
ENCODER (p0491)

**Dependency:**
  
The fault is selected and the required response is set under the same index.  
  
Refer to:
p2100

**Notice:**
  
For the following cases, it is not possible to re-parameterize the fault response
to a fault:  
- fault number does not exist (exception value = 0).  
- Message type is not "fault" (F).  
- fault response is not permissible for the set fault number.

**Note:**
  
Re-parameterization is also possible if a fault is present. The change only becomes
effective after the fault has been resolved.  
The fault response can only be changed for faults with the appropriate identification
(see the List Manual, chapter "Faults and alarms").  
Example:  
F12345 and fault response = OFF3 (OFF1, OFF2, NONE)  
--&gt; The default fault response OFF3 can be changed to OFF1, OFF2 or NONE.  
For value = 1 (OFF1):  
Braking along the ramp-function generator down ramp followed by a pulse inhibit.  
For value = 2 (OFF2):  
Internal/external pulse inhibit.  
For value = 3 (OFF3):  
Braking along the OFF3 down ramp followed by a pulse inhibit.  
For value = 5 (STOP2):  
n_set = 0  
For value = 6 (armature short-circuit, internal/DC braking):  
The value can only be set for all motor data sets when p1231 = 3, 4.  
a) For synchronous motors (p0300 = 2xx, 4xx), an internal armature short-circuit is
executed.  
b) For induction motors (p0300 = 1xx), a DC braking is initiated.  
For value = 7 (ENCODER (p0491)):  
The fault response set in p0491 is executed if applicable.  
Note:  
IASC: Internal Armature Short Circuit  
DCBRK: DC braking

### p2103[0...n] BI: 1st acknowledge faults

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**CDS, p0170 | **Func. diagram:** 2441, 2442, 2443, 2447, 2475, 2546, 9220, 9677, 9678 |
| **Object:**SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM41 | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the first signal source to acknowledge faults.

**Notice:**
  
The parameter may be protected as a result of p0922 or p2079 and cannot be changed.

**Note:**
  
A fault acknowledgment is triggered with a 0/1 signal.

### p2104[0...n] BI: 2nd acknowledge faults

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**CDS, p0170 | **Func. diagram:** 2546, 8060 |
| **Object:**SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM41 | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the second signal source to acknowledge faults.

**Note:**
  
A fault acknowledgment is triggered with a 0/1 signal.

### p2105[0...n] BI: 3rd acknowledge faults

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**CDS, p0170 | **Func. diagram:** 2546, 8060 |
| **Object:**SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM41 | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the third signal source to acknowledge faults.

**Note:**
  
A fault acknowledgment is triggered with a 0/1 signal.

### p2106[0...n] BI: External fault 1

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**CDS, p0170 | **Func. diagram:** 2546 |
| **Object:**SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM41 | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 1 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source for external fault 1.

**Dependency:**
  
  
Refer to:
F07860

**Note:**
  
An external fault is triggered with a 0 signal.  
If this fault is output at the Control Unit, then it is transferred to all existing
drive objects.

### p2107[0...n] BI: External fault 2

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**CDS, p0170 | **Func. diagram:** 2546 |
| **Object:**SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM41 | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 1 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source for external fault 2.

**Dependency:**
  
  
Refer to:
F07861

**Note:**
  
An external fault is triggered with a 0 signal.  
If this fault is output at the Control Unit, then it is transferred to all existing
drive objects.

### p2108[0...n] BI: External fault 3

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**CDS, p0170 | **Func. diagram:** 2546 |
| **Object:**SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, TM41 | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 1 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source for external fault 3.  
External fault 3 is initiated by the following AND logic operation:  
- BI: p2108 negated  
- BI: p3111  
- BI: p3112 negated

**Dependency:**
  
  
Refer to:
p3110, p3111, p3112  
Refer to:
F07862

**Note:**
  
An external fault is triggered with a 0 signal.  
If this fault is output at the Control Unit, then it is transferred to all existing
drive objects.

### r2109[0...63] Fault time removed in milliseconds

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 8050, 8060 |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [ms] | - [ms] | [ ] - [ms] |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the system runtime in milliseconds when the fault was removed.

**Dependency:**
  
  
Refer to:
r0945, r0947, r0948, r0949, r2114, r2130, r2133, r2136, r3115, r3120, r3122

**Notice:**
  
The time comprises r2136 (days) and r2109 (milliseconds).

**Note:**
  
The buffer parameters are cyclically updated in the background (refer to status signal
in r2139).  
The structure of the fault buffer and the assignment of the indices is shown in r0945.

### r2110[0...63] Alarm number

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**2 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 8065 |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
This parameter is identical to r2122.

### p2111 Alarm counter

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 8050, 8065 |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 65535 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Number of alarms that have occurred after the last reset.

**Dependency:**
  
When p2111 is set to 0, the following is initiated:  
- all of the alarms of the alarm buffer that have gone [0...7] are transferred into
the alarm history [8...63].  
- the alarm buffer [0...7] is deleted.  
  
Refer to:
r2110, r2122, r2123, r2124, r2125

**Note:**
  
The parameter is reset to 0 at POWER ON.

### p2112[0...n] BI: External alarm 1

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**CDS, p0170 | **Func. diagram:** 2546 |
| **Object:**SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM41 | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 1 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source for external alarm 1.

**Dependency:**
  
  
Refer to:
A07850

**Note:**
  
An external alarm is triggered with a 0 signal.

### p2116[0...n] BI: External alarm 2

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**CDS, p0170 | **Func. diagram:** 2546 |
| **Object:**SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM41 | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 1 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source for external alarm 2.

**Dependency:**
  
  
Refer to:
A07851

**Note:**
  
An external alarm is triggered with a 0 signal.

### p2117[0...n] BI: External alarm 3

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**CDS, p0170 | **Func. diagram:** 2546 |
| **Object:**SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM41 | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 1 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source for external alarm 3.

**Dependency:**
  
  
Refer to:
A07852

**Note:**
  
An external alarm is triggered with a 0 signal.

### p2118[0...19] Change message type message number

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 8050, 8075 |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 65535 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Selects faults or alarms for which the message type should be changed.

**Dependency:**
  
Selects the fault or alarm selection and sets the required type of message realized
under the same index.  
  
Refer to:
p2119

**Note:**
  
Re-parameterization is also possible if a message is present. The change only becomes
effective after the message has gone.

### p2119[0...19] Change message type type

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 8050, 8075 |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 1 | 3 | [ 0 ] 1 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the message type for the selected fault or alarm.

**Value:**
  
1:
Fault (F)  
2:
Alarm (A)  
3:
No message (N)

**Dependency:**
  
Selects the fault or alarm selection and sets the required type of message realized
under the same index.  
  
Refer to:
p2118

**Note:**
  
Re-parameterization is also possible if a message is present. The change only becomes
effective after the message has gone.  
The message type can only be changed for messages with the appropriate identification
(exception, value = 0).  
Example:  
F12345(A) --&gt; Fault F12345 can be changed to alarm A12345.  
In this case, the message number that may be possibly entered in p2100[0...19] and
p2126[0...19] is automatically removed.

### r2120 CO: Sum of fault and alarm buffer changes

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**4 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 8065 |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the sum of all of the fault and alarm buffer changes in the drive unit.

**Dependency:**
  
  
Refer to:
r0944, r2121

### r2121 CO: Counter alarm buffer changes

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 8065 |
| **Object:**All objects | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
This counter is incremented every time the alarm buffer changes.

**Dependency:**
  
  
Refer to:
r2110, r2122, r2123, r2124, r2125

### r2122[0...63] Alarm code

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**2 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 8050, 8065 |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the number of alarms that have occurred.

**Dependency:**
  
  
Refer to:
r2110, r2123, r2124, r2125, r2134, r2145, r2146, r3121, r3123

**Notice:**
  
The properties of the alarm buffer should be taken from the corresponding product
documentation.

**Note:**
  
The buffer parameters are cyclically updated in the background (refer to status signal
in r2139).  
Alarm buffer structure (general principle):  
r2122[0], r2124[0], r2123[0], r2125[0] --&gt; alarm 1 (the oldest)  
. . .  
r2122[7], r2124[7], r2123[7], r2125[7] --&gt; Alarm 8 (the latest)  
When the alarm buffer is full, the alarms that have gone are entered into the alarm
history:  
r2122[8], r2124[8], r2123[8], r2125[8] --&gt; Alarm 1 (the latest)  
. . .  
r2122[63], r2124[63], r2123[63], r2125[63] --&gt; alarm 56 (the oldest)

### r2123[0...63] Alarm time received in milliseconds

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 8050, 8065 |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [ms] | - [ms] | [ ] - [ms] |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the system runtime in milliseconds when the alarm occurred.

**Dependency:**
  
  
Refer to:
r2110, r2114, r2122, r2124, r2125, r2134, r2145, r2146, r3121, r3123

**Notice:**
  
The time comprises r2145 (days) and r2123 (milliseconds).

**Note:**
  
The buffer parameters are cyclically updated in the background (refer to status signal
in r2139).  
The structure of the alarm buffer and the assignment of the indices is shown in r2122.

### r2124[0...63] Alarm value

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer32 | **Dynamic index:**- | **Func. diagram:** 8050, 8065 |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays additional information about the active alarm (as integer number).

**Dependency:**
  
  
Refer to:
r2110, r2122, r2123, r2125, r2134, r2145, r2146, r3121, r3123

**Note:**
  
The buffer parameters are cyclically updated in the background (refer to status signal
in r2139).  
The structure of the alarm buffer and the assignment of the indices is shown in r2122.

### r2125[0...63] Alarm time removed in milliseconds

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 8050, 8065 |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [ms] | - [ms] | [ ] - [ms] |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the system runtime in milliseconds when the alarm was cleared.

**Dependency:**
  
  
Refer to:
r2110, r2114, r2122, r2123, r2124, r2134, r2145, r2146, r3121, r3123

**Notice:**
  
The time comprises r2146 (days) and r2125 (milliseconds).

**Note:**
  
The buffer parameters are cyclically updated in the background (refer to status signal
in r2139).  
The structure of the alarm buffer and the assignment of the indices is shown in r2122.

### p2126[0...19] Change acknowledge mode fault number

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 8050, 8075 |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 65535 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Selects the faults for which the acknowledge mode is to be changed

**Dependency:**
  
Selects the faults and sets the required acknowledge mode realized under the same
index  
  
Refer to:
p2127

**Note:**
  
Re-parameterization is also possible if a fault is present. The change only becomes
effective after the fault has been resolved.

### p2127[0...19] Change acknowledge mode mode

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 8050, 8075 |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 1 | 3 | [ 0 ] 1 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the acknowledge mode for selected fault.

**Value:**
  
1:
Acknowledgment only using POWER ON  
2:
Ack IMMEDIATELY after the fault cause has been removed  
3:
Acknowledgment only for PULSE INHIBIT

**Dependency:**
  
Selects the faults and sets the required acknowledge mode realized under the same
index  
  
Refer to:
p2126

**Notice:**
  
It is not possible to re-parameterize the acknowledge mode for a fault in the following
cases:  
- fault number does not exist (exception value = 0).  
- Message type is not "fault" (F).  
- Acknowledge mode is not permissible for the set fault number.

**Note:**
  
Re-parameterization is also possible if a fault is present. The change only becomes
effective after the fault has been resolved.  
The acknowledge mode can only be changed for faults with the appropriate identification.  
Example:  
F12345 and acknowledge mode = IMMEDIATELY (POWER ON)  
--&gt; The acknowledge mode can be changed from IMMEDIATELY to POWER ON.

### p2128[0...15] Faults/alarms trigger selection

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 8050, 8070 |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 65535 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the faults/alarms for which a trigger signal should be generated in r2129.0...15.

**Dependency:**
  
If the fault/alarm set in p2128[0...15] occurs, then the particular binector output
r2129.0...15 is set.  
  
Refer to:
r2129

### r2129.0...15 CO/BO: Faults/alarms trigger word

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 8070 |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display and BICO output for the trigger signals of the faults/alarms set in p2128[0...15].

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Trigger signal p2128[0] | OFF | ON | - |
| 01 | Trigger signal p2128[1] | OFF | ON | - |
| 02 | Trigger signal p2128[2] | OFF | ON | - |
| 03 | Trigger signal p2128[3] | OFF | ON | - |
| 04 | Trigger signal p2128[4] | OFF | ON | - |
| 05 | Trigger signal p2128[5] | OFF | ON | - |
| 06 | Trigger signal p2128[6] | OFF | ON | - |
| 07 | Trigger signal p2128[7] | OFF | ON | - |
| 08 | Trigger signal p2128[8] | OFF | ON | - |
| 09 | Trigger signal p2128[9] | OFF | ON | - |
| 10 | Trigger signal p2128[10] | OFF | ON | - |
| 11 | Trigger signal p2128[11] | OFF | ON | - |
| 12 | Trigger signal p2128[12] | OFF | ON | - |
| 13 | Trigger signal p2128[13] | OFF | ON | - |
| 14 | Trigger signal p2128[14] | OFF | ON | - |
| 15 | Trigger signal p2128[15] | OFF | ON | - |

**Dependency:**
  
If the fault/alarm set in p2128[0...15] occurs, then the particular binector output
r2129.0...15 is set.  
  
Refer to:
p2128

**Note:**
  
CO: r2129 = 0 --&gt; None of the selected messages has occurred.  
CO: r2129 &gt; 0 --&gt; At least one of the selected messages has occurred.

### r2130[0...63] Fault time received in days

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 8060 |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the system runtime in days when the fault occurred.

**Dependency:**
  
  
Refer to:
r0945, r0947, r0948, r0949, r2109, r2114, r2133, r2136, p3100, r3115, r3120, r3122

**Notice:**
  
The time comprises r2130 (days) and r0948 (milliseconds).  
The time display depends on the selected mode (p3100).

**Note:**
  
The buffer parameters are cyclically updated in the background (refer to status signal
in r2139).

### r2131 CO: Actual fault code

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 8060 |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the code of the oldest active fault.

**Dependency:**
  
  
Refer to:
r3131, r3132

**Note:**
  
0: No fault present.

### r2132 CO: Actual alarm code

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 8065 |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the code of the last alarm that occurred.

**Note:**
  
0: No alarm present.

### r2133[0...63] Fault value for float values

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 8060 |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays additional information about the fault that occurred for float values.

**Dependency:**
  
  
Refer to:
r0945, r0947, r0948, r0949, r2109, r2130, r2136, r3115

**Note:**
  
The buffer parameters are cyclically updated in the background (refer to status signal
in r2139).

### r2134[0...63] Alarm value for float values

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 8065 |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays additional information about the active alarm for float values.

**Dependency:**
  
  
Refer to:
r2110, r2122, r2123, r2124, r2125, r2145, r2146, r3121, r3123

**Note:**
  
The buffer parameters are cyclically updated in the background (refer to status signal
in r2139).

### r2135.0...15 CO/BO: Status word faults/alarms 2

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**2 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 2548 |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**Displays, signals | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display and BICO output for the second status word of faults and alarms.

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Fault encoder 1 | No | Yes | - |
| 01 | Fault encoder 2 | No | Yes | - |
| 02 | Fault encoder 3 | No | Yes | - |
| 12 | Fault motor overtemperature | No | Yes | 8016 |
| 13 | Fault power unit thermal overload | No | Yes | 8021 |
| 14 | Alarm motor overtemperature | No | Yes | 8016 |
| 15 | Alarm power unit thermal overload | No | Yes | 8021 |

### r2136[0...63] Fault time removed in days

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 8060 |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the system runtime in days when the fault was removed.

**Dependency:**
  
  
Refer to:
r0945, r0947, r0948, r0949, r2109, r2114, r2130, r2133, r3115, r3120, r3122

**Notice:**
  
The time comprises r2136 (days) and r2109 (milliseconds).

**Note:**
  
The buffer parameters are cyclically updated in the background (refer to status signal
in r2139).

### r2138.7...15 CO/BO: Control word faults/alarms

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**2 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 2546 |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**Displays, signals | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display and BICO output for the control word of faults and alarms.

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 07 | Acknowledge fault | No | Yes | 8060 |
| 10 | External alarm 1 (A07850) effective | No | Yes | 8065 |
| 11 | External alarm 2 (A07851) effective | No | Yes | 8065 |
| 12 | External alarm 3 (A07852) effective | No | Yes | 8065 |
| 13 | External fault 1 (F07860) effective | No | Yes | 8060 |
| 14 | External fault 2 (F07861) effective | No | Yes | 8060 |
| 15 | External fault 3 (F07862) effective | No | Yes | 8060 |

**Dependency:**
  
  
Refer to:
p2103, p2104, p2105, p2106, p2107, p2108, p2112, p2116, p2117, p3110, p3111, p3112

### r2139.0...15 CO/BO: Status word faults/alarms 1

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**2 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 2548 |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**Displays, signals | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.7

**Description:**
  
Display and BICO output for status word 1 of faults and alarms.

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Being acknowledged | No | Yes | - |
| 01 | Acknowledgment required | No | Yes | - |
| 03 | Fault present | No | Yes | 8060 |
| 05 | Safety message present | No | Yes | - |
| 06 | Internal message 1 present | No | Yes | - |
| 07 | Alarm present | No | Yes | 8065 |
| 08 | Internal message 2 present | No | Yes | - |
| 11 | Alarm class bit 0 | Low | High | - |
| 12 | Alarm class bit 1 | Low | High | - |
| 13 | Maintenance required | No | Yes | - |
| 14 | Maintenance urgently required | No | Yes | - |
| 15 | Fault gone/can be acknowledged | No | Yes | - |

**Note:**
  
For bit 03, 05, 07:  
These bits are set if at least one fault/alarm occurs. Data is entered into the fault/alarm
buffer with delay. For this reason, the fault/alarm buffer should only be read if,
after "Fault active" or "Alarm active" occurs, a change is also identified in the
buffer (r0944, r9744, r2121).  
For bit 06, 08:  
These status bits are used for internal diagnostic purposes only.  
For bit 12, 11:  
These status bits are used for the classification of internal alarm classes and are
intended for diagnostic purposes only on certain automation systems with integrated
SINAMICS functionality.

### r2145[0...63] Alarm time received in days

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 8065 |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the system runtime in days when the alarm occurred.

**Dependency:**
  
  
Refer to:
r2110, r2114, r2122, r2123, r2124, r2125, r2134, r2146, r3121, r3123

**Notice:**
  
The time comprises r2145 (days) and r2123 (milliseconds).

**Note:**
  
The buffer parameters are cyclically updated in the background (refer to status signal
in r2139).

### r2146[0...63] Alarm time removed in days

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 8065 |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the system runtime in days when the alarm was cleared.

**Dependency:**
  
  
Refer to:
r2110, r2114, r2122, r2123, r2124, r2125, r2134, r2145, r3121, r3123

**Notice:**
  
The time comprises r2146 (days) and r2125 (milliseconds).

**Note:**
  
The buffer parameters are cyclically updated in the background (refer to status signal
in r2139).

### r2700 CO: Reference speed/reference frequency

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**2 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, TM41, ENC, ENC_840 | **P-Group:**- | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display and connector output for the reference quantity for speed and frequency (p2000).  
All speeds or frequencies specified as relative value are referred to this reference
quantity.  
The reference quantity corresponds to 100% or 4000 hex (word) or 4000 0000 hex (double
word).  
This parameter has the unit rpm.  
The following applies:  
Reference frequency (in Hz) = reference speed (in rpm) / 60

**Dependency:**
  
  
Refer to:
p2000

**Note:**
  
This BICO parameter provides the numerical value of the reference quantity p2000 as
a connector output for interconnection with Drive Control Chart (DCC). The numerical
value can be adopted unchanged from this connector output in DCC.  
This BICO parameter is not suitable for interconnecting for cyclic communication.

### r2701 CO: Reference voltage

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**SERVO, VECTOR, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_840, SERVO_COMBI, SERVO_828, SERVO_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM41 | **P-Group:**- | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Connector output of the reference quantity for voltages p2001.  
All voltages specified as relative value are referred to this reference quantity.  
The reference quantity corresponds to 100% or 4000 hex (word) or 4000 0000 hex (double
word).  
This parameter has the unit Vrms.

**Dependency:**
  
  
Refer to:
p2001

**Note:**
  
This BICO parameter provides the numerical value of the reference quantity p2001 as
a connector output for interconnection with Drive Control Chart (DCC). The numerical
value can be adopted unchanged from this connector output in DCC.  
This BICO parameter is not suitable for interconnecting for cyclic communication.

### r2702 CO: Reference current

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM41 | **P-Group:**- | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Connector output of the reference quantity for currents p2002.  
All currents specified as relative value are referred to this reference quantity.  
The reference quantity corresponds to 100% or 4000 hex (word) or 4000 0000 hex (double
word).  
This parameter has the unit Arms.

**Dependency:**
  
  
Refer to:
p2002

**Note:**
  
This BICO parameter provides the numerical value of the reference quantity p2002 as
a connector output for interconnection with Drive Control Chart (DCC). The numerical
value can be adopted unchanged from this connector output in DCC.  
This BICO parameter is not suitable for interconnecting for cyclic communication.

### r2703 CO: Reference torque

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**SERVO, VECTOR, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_840, SERVO_COMBI, SERVO_828, SERVO_DBSI, SERVO_I_AC, VECTOR_I_AC, TM41 | **P-Group:**- | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Connector output of the reference quantity p2003 for torque (r0108.12 = 0) or force
(r0108.12 = 1).  
All torques specified as relative values (r0108.12 = 0) or forces (r0108.12 = 1) are
referred to this reference quantity.  
The reference quantity corresponds to 100% or 4000 hex (word) or 4000 0000 hex (double
word).  
The unit of this parameter is the same as the unit selected for p2003.

**Dependency:**
  
p0505, r0108.12  
  
Refer to:
p2003

**Note:**
  
This BICO parameter provides the numerical value of the reference quantity p2003 in
the currently selected unit as a connector output for interconnection with Drive Control
Chart (DCC). The numerical value can be adopted unchanged from this connector output
in DCC.  
This BICO parameter is not suitable for interconnecting for cyclic communication.

### r2704 CO: Reference power

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM41 | **P-Group:**- | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Connector output of the reference quantity for powers p2004.  
All power ratings specified as relative value are referred to this reference quantity.  
The reference quantity corresponds to 100% or 4000 hex (word) or 4000 0000 hex (double
word).  
The unit of this parameter is the same as the unit selected for p2004.

**Dependency:**
  
This value is calculated as voltage x current for the infeed and as torque x speed
for closed-loop controls.  
  
Refer to:
r2004

**Note:**
  
This BICO parameter provides the numerical value of the reference quantity p2004 in
the currently selected unit as a connector output for interconnection with Drive Control
Chart (DCC). The numerical value can be adopted unchanged from this connector output
in DCC.  
This BICO parameter is not suitable for interconnecting for cyclic communication.  
The reference power is calculated as follows:  
- 2 * Pi * reference speed / 60 * reference torque (motor)  
- reference voltage * reference current * root(3) (infeed)

### r2705 CO: Reference angle

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM41 | **P-Group:**- | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Connector output of the reference quantity for angles p2005.  
All angles specified as relative value are referred to this reference quantity.  
The reference quantity corresponds to 100% or 4000 hex (word) or 4000 0000 hex (double
word).  
This parameter has the unit degree.

**Dependency:**
  
  
Refer to:
p2005

**Note:**
  
This BICO parameter provides the numerical value of the reference quantity p2005 as
a connector output for interconnection with Drive Control Chart (DCC). The numerical
value can be adopted unchanged from this connector output in DCC.  
This BICO parameter is not suitable for interconnecting for cyclic communication.

### r2706 CO: Reference temperature

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM120, TM150 | **P-Group:**- | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Connector output of the reference quantity for temperatures.  
All temperatures specified as relative value are referred to this reference quantity.  
The reference quantity corresponds to 100% or 4000 hex (word) or 4000 0000 hex (double
word).  
This parameter has the unit degree Celsius.

**Note:**
  
This BICO parameter provides the numerical value of the reference quantity for the
temperature as a connector output for interconnection with Drive Control Chart (DCC).
The numerical value can be adopted unchanged from this connector output in DCC.  
This BICO parameter is not suitable for interconnecting for cyclic communication.

### r2707 CO: Reference acceleration

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, TM41 | **P-Group:**- | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Connector output of the reference quantity for accelerations p2007.  
All acceleration rates specified as relative value are referred to this reference
quantity.  
The reference quantity corresponds to 100% or 4000 hex (word) or 4000 0000 hex (double
word).  
The unit of this parameter is the same as the unit selected for p2007.

**Dependency:**
  
r0108.12, p0505  
  
Refer to:
p2007

**Note:**
  
This BICO parameter provides the numerical value of the reference quantity p2007 as
a connector output for interconnection with Drive Control Chart (DCC). The numerical
value in the currently selected unit can be adopted unchanged from this connector
output in DCC.  
This BICO parameter is not suitable for interconnecting for cyclic communication.

### p3110 External fault 3 switch-on delay

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 2546 |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 [ms] | 1000 [ms] | [ 0 ] 0 [ms] |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the delay time for external fault 3.

**Dependency:**
  
  
Refer to:
p2108, p3111, p3112  
Refer to:
F07862

### p3111[0...n] BI: External fault 3 enable

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**CDS, p0170 | **Func. diagram:** - |
| **Object:**SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, TM41 | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 1 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source for the enable signal of external fault 3.  
External fault 3 is initiated by the following AND logic operation:  
- BI: p2108 negated  
- BI: p3111  
- BI: p3112 negated

**Dependency:**
  
  
Refer to:
p2108, p3110, p3112  
Refer to:
F07862

### p3112[0...n] BI: External fault 3 enable negated

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**CDS, p0170 | **Func. diagram:** - |
| **Object:**SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM41 | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source for the negated enable signal of external fault 3.  
External fault 3 is initiated by the following AND logic operation:  
- BI: p2108 negated  
- BI: p3111  
- BI: p3112 negated

**Dependency:**
  
  
Refer to:
p2108, p3110, p3111  
Refer to:
F07862

### r3113.0...15 CO/BO: NAMUR message bit bar

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display and BICO output for the status of the NAMUR message bit bar.  
The faults and alarms are assigned to the appropriate signaling/message classes and
influence a specific message bit.

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Fault converter information electronics/software error | No | Yes | - |
| 01 | Network fault | No | Yes | - |
| 02 | DC link overvoltage | No | Yes | - |
| 03 | Fault drive converter power electronics | No | Yes | - |
| 04 | Drive converter overtemperature | No | Yes | - |
| 05 | Ground fault | No | Yes | - |
| 06 | Motor overload | No | Yes | - |
| 07 | Bus error | No | Yes | - |
| 08 | External safety-relevant shutdown | No | Yes | - |
| 09 | Mot encoder fault | No | Yes | - |
| 10 | Error communication internal | No | Yes | - |
| 11 | Fault infeed | No | Yes | - |
| 15 | Other faults | No | Yes | - |

**Note:**
  
For bit 00:  
Hardware or software malfunction was identified. Carry out a POWER ON of the component
involved. If it occurs again, contact Technical Support.  
For bit 01:  
A line supply fault has occurred (phase failure, voltage level, ...). Check the line
supply / fuses. Check the supply voltage. Check the wiring.  
For bit 02:  
The DC link voltage has assumed an inadmissibly high value. Check the dimensioning
of the system (line supply, reactor, voltages). Check the infeed settings.  
For bit 03:  
An inadmissible operating state of the power electronics was identified (overcurrent,
overtemperature, IGBT failure, ...). Check that the permissible load cycles are maintained.
Check the ambient temperatures (fan).  
For bit 04:  
The temperature in the component has exceeded the highest permissible limit. Check
the ambient temperature / control cabinet cooling.  
For bit 05:  
A ground fault / inter-phase short-circuit was detected in the power cables or in
the motor windings. Check the power cables (connection). Check the motor.  
For bit 06:  
The motor was operated outside the permissible limits (temperature, current, torque,
...). Check the load cycles and limits that have been set. Check the ambient temperature
/ motor cooling.  
For bit 07:  
The communication to the higher-level control system (internal coupling, PROFIBUS,
PROFINET, ...) is either faulted or interrupted. Check the state of the higher-level
control system. Check the communication connection/wiring. Check the bus configuration
/ clock cycles.  
For bit 08:  
A safety operation monitoring function (Safety) has detected an error.  
For bit 09:  
When evaluating the encoder signals (track signals, zero marks, absolute values, ...)
an illegal signal state was detected. Check the encoder / state of the encoder signals.
Observe the maximum frequencies.  
For bit 10:  
The internal communication between the SINAMICS components is faulted or interrupted.
Check the DRIVE-CLiQ wiring. Ensure an EMC-compliant design. Observe the maximum permissible
quantity structure / clock cycles.  
For bit 11:  
The infeed is faulted or has failed. Check the infeed and the surroundings (line supply,
filter, reactors, fuses, ...). Check the closed-loop infeed control.  
For bit 15:  
Group fault. Determine the precise cause of the fault using the commissioning tool.

### r3115[0...63] Fault drive object initiating

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer32 | **Dynamic index:**- | **Func. diagram:** 8050, 8060 |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the drive object number of the initiating drive object for this fault as
integer number.  
Value = 63:  
The fault was initiated by the drive object itself.

**Dependency:**
  
  
Refer to:
r0945, r0947, r0948, r0949, r2109, r2130, r2133, r2136, r3120, r3122

**Notice:**
  
The values of this parameter are only saved in a volatile fashion and are lost when
switching off or for a warm restart.

**Note:**
  
The buffer parameters are cyclically updated in the background (refer to status signal
in r2139).  
The structure of the fault buffer and the assignment of the indices is shown in r0945.

### r3120[0...63] Component fault

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 8060 |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.4

**Description:**
  
Displays the component of the fault which has occurred.

**Dependency:**
  
  
Refer to:
r0945, r0947, r0948, r0949, r2109, r2130, r2133, r2136, r3122

**Note:**
  
Value = 0: Assignment to a component not possible.  
The buffer parameters are cyclically updated in the background (refer to status signal
in r2139).  
The structure of the fault buffer and the assignment of the indices is shown in r0945.

### r3121[0...63] Component alarm

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 8065 |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.4

**Description:**
  
Displays the component of the alarm which has occurred.

**Dependency:**
  
  
Refer to:
r2110, r2122, r2123, r2124, r2125, r2134, r2145, r2146, r3123

**Note:**
  
Value = 0: Assignment to a component not possible.  
The buffer parameters are cyclically updated in the background (refer to status signal
in r2139).  
The structure of the alarm buffer and the assignment of the indices is shown in r2122.

### r3122[0...63] Diagnostic attribute fault

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 8060 |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.4

**Description:**
  
Displays the diagnostic attribute of the fault which has occurred.

**Bit field:**

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
  
  
Refer to:
r0945, r0947, r0948, r0949, r2109, r2130, r2133, r2136, r3120

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

### r3123[0...63] Diagnostic attribute alarm

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 8065 |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.4

**Description:**
  
Displays the diagnostic attribute of the alarm which has occurred.

**Bit field:**

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
  
  
Refer to:
r2110, r2122, r2123, r2124, r2125, r2134, r2145, r2146, r3121

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

### r3131 CO: Actual fault value

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer32 | **Dynamic index:**- | **Func. diagram:** 8060 |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.4

**Description:**
  
Displays the fault value of the oldest active fault.

**Dependency:**
  
  
Refer to:
r2131, r3132

### r3132 CO: Actual component number

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer32 | **Dynamic index:**- | **Func. diagram:** 8060 |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.4

**Description:**
  
Displays the component number of the oldest fault that is still active.

**Dependency:**
  
  
Refer to:
r2131, r3131

### p3135 Suppress active fault

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**4 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 8060 |
| **Object:**SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM41 | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0000 0000 0000 0000 bin |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the suppression of r2139.3 "Fault present" for certain fault responses.

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 08 | Suppression of fault response ENCODER | OFF | ON | - |
| 10 | Suppression of fault response NONE | OFF | ON | - |

**Dependency:**
  
  
Refer to:
p0491, r2139

**Note:**
  
Depending on the suppression of a fault reaction in this parameter, r2139.1 "Acknowledgment
required" is set when at least one fault occurs.  
For bit 08:  
The suppression is only effective if p0491 = 1.

### r3979 BICO counter drive object

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**4 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**Commands | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the counter reading for modified BICO interconnections on this drive object.  
The counter is incremented by one for each modified BICO interconnection.

### p3981 Acknowledge drive object faults

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**2 |
| **Data type:**Unsigned8 | **Dynamic index:**- | **Func. diagram:** 8060 |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**Messages | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 1 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting to acknowledge all active faults of a drive object.

**Notice:**
  
Safety messages cannot be acknowledged using this parameter.

**Note:**
  
Parameter should be set from 0 to 1 to acknowledge.  
After acknowledgment, the parameter is automatically reset to 0.

### r3986 Number of parameters

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**- | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the number of parameters for this drive unit.  
The number comprises the device-specific and the drive-specific parameters.

### r3996[0...1] Parameter write inhibit status

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned8 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**- | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.5

**Description:**
  
Displays whether writing to parameters is inhibited.  
r3996[0] = 0:  
Parameter write not inhibited.  
0 &lt; r3996[0] &lt; 100:  
Parameter write inhibited. The value shows how the calculations are progressing.

**Index:**
  
[
0]:
Progress calculations  
[
1]:
Cause

**Note:**
  
For index [1]:  
Only for internal Siemens troubleshooting.

### r4021 TM41 digital inputs terminal actual value

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**2 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**TM41 | **P-Group:**Commands | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the actual value at the digital inputs.  
This means that the actual input signal can be checked at terminal DI x or DI/DO x
prior to switching from the simulation mode (p4095.x = 1) to terminal mode (p4095.x
= 0).

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | DI 0 (X522.1) | Low | High | 9660 |
| 01 | DI 1 (X522.2) | Low | High | 9660 |
| 02 | DI 2 (X522.3) | Low | High | 9660 |
| 03 | DI 3 (X522.4) | Low | High | 9660 |
| 08 | DI/DO 0 (X521.1) | Low | High | 9661 |
| 09 | DI/DO 1 (X521.2) | Low | High | 9661 |
| 10 | DI/DO 2 (X521.3) | Low | High | 9662 |
| 11 | DI/DO 3 (X521.4) | Low | High | 9662 |

**Note:**
  
If a DI/DO is parameterized as output (p4028.x = 1), then r4021.x = 0 is displayed.  
DI: Digital Input  
DI/DO: Bidirectional Digital Input/Output

### r4022.0...11 CO/BO: TM41 digital inputs status

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 9659, 9660, 9661, 9662 |
| **Object:**TM41 | **P-Group:**Commands | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the status of the digital inputs of Terminal Module 41 (TM41).

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | DI 0 (X522.1) | Low | High | 9660 |
| 01 | DI 1 (X522.2) | Low | High | 9660 |
| 02 | DI 2 (X522.3) | Low | High | 9660 |
| 03 | DI 3 (X522.4) | Low | High | 9660 |
| 08 | DI/DO 0 (X521.1) | Low | High | 9661 |
| 09 | DI/DO 1 (X521.2) | Low | High | 9661 |
| 10 | DI/DO 2 (X521.3) | Low | High | 9662 |
| 11 | DI/DO 3 (X521.4) | Low | High | 9662 |

**Dependency:**
  
  
Refer to:
r4023

**Note:**
  
DI: Digital Input  
DI/DO: Bidirectional Digital Input/Output

### r4023.0...11 BO: TM41 digital inputs status inverted

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 9659, 9660, 9661, 9662 |
| **Object:**TM41 | **P-Group:**Commands | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the inverted status of the digital inputs of Terminal Module 41 (TM41).

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | DI 0 (X522.1) | Low | High | 9660 |
| 01 | DI 1 (X522.2) | Low | High | 9660 |
| 02 | DI 2 (X522.3) | Low | High | 9660 |
| 03 | DI 3 (X522.4) | Low | High | 9660 |
| 08 | DI/DO 0 (X521.1) | Low | High | 9661 |
| 09 | DI/DO 1 (X521.2) | Low | High | 9661 |
| 10 | DI/DO 2 (X521.3) | Low | High | 9662 |
| 11 | DI/DO 3 (X521.4) | Low | High | 9662 |

**Dependency:**
  
  
Refer to:
r4022

**Note:**
  
DI: Digital Input  
DI/DO: Bidirectional Digital Input/Output

### p4028 TM41 set input or output

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 9659, 9661, 9662 |
| **Object:**TM41 | **P-Group:**Commands | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0000 0000 0000 0000 bin |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the bidirectional digital inputs/outputs on the Terminal Module 41 (TM41) as
input or output.

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 08 | DI/DO 0 (X521.1) | Input | Output | 9661 |
| 09 | DI/DO 1 (X521.2) | Input | Output | 9661 |
| 10 | DI/DO 2 (X521.3) | Input | Output | 9662 |
| 11 | DI/DO 3 (X521.4) | Input | Output | 9662 |

**Note:**
  
DI/DO: Bidirectional Digital Input/Output

### p4038 BI: TM41 signal source for terminal DI/DO 0

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 9661 |
| **Object:**TM41 | **P-Group:**Commands | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source for terminal DI/DO 0 (X521.1) of Terminal Module 41 (TM41).

**Note:**
  
Prerequisite: The DI/DO must be set as an output (p4028.8 = 1).  
DI/DO: Bidirectional Digital Input/Output

### p4039 BI: TM41 signal source for terminal DI/DO 1

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 9661 |
| **Object:**TM41 | **P-Group:**Commands | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source for terminal DI/DO 1 (X541.2) of Terminal Module 41 (TM41).

**Note:**
  
Prerequisite: The DI/DO must be set as an output (p4028.9 = 1).  
DI/DO: Bidirectional Digital Input/Output

### p4040 BI: TM41 signal source for terminal DI/DO 2

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 9662 |
| **Object:**TM41 | **P-Group:**Commands | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source for terminal DI/DO 2 (X521.3) of Terminal Module 41 (TM41).

**Note:**
  
Prerequisite: The DI/DO must be set as an output (p4028.10 = 1).  
DI/DO: Bidirectional Digital Input/Output

### p4041 BI: TM41 signal source for terminal DI/DO 3

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 9662 |
| **Object:**TM41 | **P-Group:**Commands | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source for terminal DI/DO 3 (X521.4) of Terminal Module 41 (TM41).

**Note:**
  
Prerequisite: The DI/DO must be set as an output (p4028.11 = 1).  
DI/DO: Bidirectional Digital Input/Output

### r4047 TM41 digital outputs status

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**TM41 | **P-Group:**Commands | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the status of the digital outputs of Terminal Module 41 (TM41).

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 08 | DI/DO 0 (X521.1) | Low | High | 9661 |
| 09 | DI/DO 1 (X521.2) | Low | High | 9661 |
| 10 | DI/DO 2 (X521.3) | Low | High | 9662 |
| 11 | DI/DO 3 (X521.4) | Low | High | 9662 |

**Note:**
  
Inversion using p4048 has been taken into account.  
The setting of the DI/DO as either input or output is of no significance (p4028).  
DO: Digital Output  
DI/DO: Bidirectional Digital Input/Output

### p4048 TM41 invert digital outputs

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**TM41 | **P-Group:**Commands | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0000 0000 0000 0000 bin |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting to invert the signals at the digital outputs of Terminal Module 41 (TM41).

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 08 | DI/DO 0 (X521.1) | Not inverted | Inverted | 9661 |
| 09 | DI/DO 1 (X521.2) | Not inverted | Inverted | 9661 |
| 10 | DI/DO 2 (X521.3) | Not inverted | Inverted | 9662 |
| 11 | DI/DO 3 (X521.4) | Not inverted | Inverted | 9662 |

**Note:**
  
DO: Digital Output  
DI/DO: Bidirectional Digital Input/Output

### r4052[0] CO: TM41 analog inputs actual input voltage

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 9663 |
| **Object:**TM41 | **P-Group:**Terminals | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [V] | - [V] | [ ] - [V] |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the actual input voltage in V.

**Index:**
  
[
0]:
AI 0 (X523.1/X523.2)

**Note:**
  
AI: Analog Input

### p4053[0] TM41 analog inputs smoothing time constant

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 9663 |
| **Object:**TM41 | **P-Group:**Terminals | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.0 [ms] | 1000.0 [ms] | [ 0 ] 0.0 [ms] |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the smoothing time constant of the 1st order lowpass filter for the analog input
of Terminal Module 41 (TM41).

**Index:**
  
[
0]:
AI 0 (X523.1/X523.2)

**Note:**
  
AI: Analog Input

### r4055[0] CO: TM41 analog inputs actual value in percent

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 9663 |
| **Object:**TM41 | **P-Group:**Terminals | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**PERCENT | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [%] | - [%] | [ ] - [%] |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the currently referred input value of the analog inputs of Terminal Module
41 (TM41).  
When interconnected, the signals are referred to the reference quantities p200x and
p205x.

**Index:**
  
[
0]:
AI 0 (X523.1/X523.2)

**Note:**
  
AI: Analog Input

### r4056 TM41 analog input type

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**TM41 | **P-Group:**Terminals | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 4 | 4 | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the type of the analog input.

**Value:**
  
4:
Bipolar voltage input (-10 V ... +10 V)

### p4057[0] TM41 analog input characteristic value x1

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**2 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 9663 |
| **Object:**TM41 | **P-Group:**Terminals | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| -20.000 [V] | 20.000 [V] | [ 0 ] 0.000 [V] |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the scaling characteristic for the analog input of Terminal Module 41 (TM41).  
The scaling characteristic for the analog input is defined using 2 points.  
This parameter specifies the x coordinate (input voltage in V) of the 1st value pair
of the characteristic.

**Index:**
  
[
0]:
AI 0 (X523.1/X523.2)

**Note:**
  
The parameters for the characteristic do not have a limiting effect.

### p4058[0] TM41 analog input characteristic value y1

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**2 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 9663 |
| **Object:**TM41 | **P-Group:**Terminals | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| -1000.00 [%] | 1000.00 [%] | [ 0 ] 0.00 [%] |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the scaling characteristic for the analog input of Terminal Module 41 (TM41).  
The scaling characteristic for the analog inputs is defined using 2 points.  
This parameter specifies the y coordinate (percentage) of the 1st value pair of the
characteristic.

**Index:**
  
[
0]:
AI 0 (X523.1/X523.2)

**Note:**
  
The parameters for the characteristic do not have a limiting effect.

### p4059[0] TM41 analog input characteristic value x2

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**2 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 9663 |
| **Object:**TM41 | **P-Group:**Terminals | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| -20.000 [V] | 20.000 [V] | [ 0 ] 10.000 [V] |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the scaling characteristic for the analog input of Terminal Module 41 (TM41).  
The scaling characteristic for the analog inputs is defined using 2 points.  
This parameter specifies the x coordinate (input voltage in V) of the 2nd value pair
of the characteristic.

**Index:**
  
[
0]:
AI 0 (X523.1/X523.2)

**Note:**
  
The parameters for the characteristic do not have a limiting effect.

### p4060[0] TM41 analog input characteristic value y2

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**2 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 9663 |
| **Object:**TM41 | **P-Group:**Terminals | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| -1000.00 [%] | 1000.00 [%] | [ 0 ] 100.00 [%] |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the scaling characteristic for the analog input of Terminal Module 41 (TM41).  
The scaling characteristic for the analog inputs is defined using 2 points.  
This parameter specifies the y coordinate (percentage) of the 2nd value pair of the
characteristic.

**Index:**
  
[
0]:
AI 0 (X523.1/X523.2)

**Note:**
  
The parameters for the characteristic do not have a limiting effect.

### p4063[0] TM41 analog input offset

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**2 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 9663 |
| **Object:**TM41 | **P-Group:**Terminals | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| -20.000 [V] | 20.000 [V] | [ 0 ] 0.000 [V] |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the offset for the analog input of Terminal Module 41 (TM41).  
The offset is added to the input signal before the scaling characteristic.

**Index:**
  
[
0]:
AI 0 (X523.1/X523.2)

### p4066[0] TM41 analog input activate absolute value generation

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 9663 |
| **Object:**TM41 | **P-Group:**Terminals | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 1 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Activates the absolute value generation of the analog input signal of Terminal Module
41 (TM41).

**Value:**
  
0:
No absolute value generation  
1:
Absolute value generation switched in

**Index:**
  
[
0]:
AI 0 (X523.1/X523.2)

### p4067[0] BI: TM41 analog input invert signal source

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 9663 |
| **Object:**TM41 | **P-Group:**Terminals | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source to invert the analog input signal of Terminal Module 41 (TM41).

**Index:**
  
[
0]:
AI 0 (X523.1/X523.2)

### p4068[0] TM41 analog input window to suppress noise

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 9663 |
| **Object:**TM41 | **P-Group:**Terminals | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 [%] | 20.00 [%] | [ 0 ] 0.00 [%] |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the noise suppression window of the analog input for Terminal Module 41 (TM41).  
Changes less than the window are suppressed.

**Index:**
  
[
0]:
AI 0 (X523.1/X523.2)

**Note:**
  
AI: Analog Input

### p4069[0] BI: TM41 analog input signal source for enable

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 9663 |
| **Object:**TM41 | **P-Group:**Terminals | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 1 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source for the enable signal of the analog input of Terminal Module
41 (TM41).

**Index:**
  
[
0]:
AI 0 (X523.1/X523.2)

### p4095 TM41 digital inputs simulation mode

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**2 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**TM41 | **P-Group:**Terminals | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0000 0000 0000 0000 bin |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the simulation mode for the digital inputs of Terminal Module 41 (TM41).

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | DI 0 (X522.1) | Terminal eval | Simulation | 9660 |
| 01 | DI 1 (X522.2) | Terminal eval | Simulation | 9660 |
| 02 | DI 2 (X522.3) | Terminal eval | Simulation | 9660 |
| 03 | DI 3 (X522.4) | Terminal eval | Simulation | 9660 |
| 08 | DI/DO 0 (X521.1) | Terminal eval | Simulation | 9661 |
| 09 | DI/DO 1 (X521.2) | Terminal eval | Simulation | 9661 |
| 10 | DI/DO 2 (X521.3) | Terminal eval | Simulation | 9662 |
| 11 | DI/DO 3 (X521.4) | Terminal eval | Simulation | 9662 |

**Dependency:**
  
The setpoint for the input signals is specified using p4096.  
  
Refer to:
p4096

**Warning:**
  
A drive that is moved by simulating the inputs of a Terminal Module is brought to
a standstill while the Terminal Module is being activated or deactivated.

**Note:**
  
This parameter is not saved when data is backed-up (p0971, p0977).  
DI: Digital Input  
DI/DO: Bidirectional Digital Input/Output

### p4096 TM41 digital inputs simulation mode setpoint

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**2 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**TM41 | **P-Group:**Terminals | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0000 0000 0000 0000 bin |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the setpoint for the input signals in the simulation mode of the digital inputs
of Terminal Module 41 (TM41).

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | DI 0 (X522.1) | Low | High | 9660 |
| 01 | DI 1 (X522.2) | Low | High | 9660 |
| 02 | DI 2 (X522.3) | Low | High | 9660 |
| 03 | DI 3 (X522.4) | Low | High | 9660 |
| 08 | DI/DO 0 (X521.1) | Low | High | 9661 |
| 09 | DI/DO 1 (X521.2) | Low | High | 9661 |
| 10 | DI/DO 2 (X521.3) | Low | High | 9662 |
| 11 | DI/DO 3 (X521.4) | Low | High | 9662 |

**Dependency:**
  
The simulation of a digital input is selected using p4095.  
  
Refer to:
p4095

**Note:**
  
This parameter is not saved when data is backed-up (p0971, p0977).  
DI: Digital Input  
DI/DO: Bidirectional Digital Input/Output

### p4097[0] TM41 analog input simulation mode

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**2 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 9663 |
| **Object:**TM41 | **P-Group:**Terminals | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 1 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the simulation mode for the analog input of Terminal Module 41 (TM41).

**Value:**
  
0:
Terminal evaluation for analog input x  
1:
Simulation for analog input x

**Index:**
  
[
0]:
AI 0 (X523.1/X523.2)

**Dependency:**
  
The setpoint for the input voltage is specified via p4098.  
  
Refer to:
p4098

**Note:**
  
This parameter is not saved when data is backed-up (p0971, p0977).  
AI: Analog Input

### p4098[0] TM41 analog input simulation mode setpoint

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**2 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 9663 |
| **Object:**TM41 | **P-Group:**Terminals | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| -20.000 [V] | 20.000 [V] | [ 0 ] 0.000 [V] |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the setpoint for the input value in simulation mode of the analog input of Terminal
Module 41 (TM41).

**Index:**
  
[
0]:
AI 0 (X523.1/X523.2)

**Dependency:**
  
The simulation of the analog input is selected using p4097.  
If AI x is parameterized as voltage input (p4056), then the setpoint is a voltage
in V.  
If AI x is parameterized as current input (p4056), then the setpoint is a current
in mA.  
  
Refer to:
p4097

**Note:**
  
This parameter is not saved when data is backed-up (p0971, p0977).  
AI: Analog Input

### p4099[0...3] TM41 inputs/outputs sampling time

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C1( 3) | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 9659, 9660 |
| **Object:**TM41 | **P-Group:**Commands | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 [µs] | 5000.00 [µs] | [ 0 ] 4000.00 [µs]  [ 1 ] 4000.00 [µs]  [ 2 ] 0.00 [µs]  [ 3 ] 125.00 [µs] |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the sampling time for the inputs and outputs of Terminal Module 41 (TM41).

**Index:**
  
[
0]:
Digital inputs/outputs (DI/DO)  
[
1]:
Analog inputs (AI)  
[
2]:
Not present  
[
3]:
Incremental encoder emulation

**Dependency:**
  
The parameter can only be modified for p0009 = 3, 29.  
The sampling times can only be set as an integer multiple of the DRIVE-CLiQ clock
cycle.  
The minimum permissible sampling time for index 0 (digital inputs/outputs) is 125
µs.  
The minimum permissible sampling time for index 1 (analog inputs) is 62.5 µs.  
  
Refer to:
p0009, r0110, r0111  
Refer to:
A35228

**Note:**
  
The value of the sampling time of the incremental encoder emulation p4099[3] can be
pre-set in both operating modes (p4400). The next time that the system boots, the
validity of the value is checked. For an invalid value, message F35228 and/or A01223
is output.  
The changed sampling time is immediately effective after a completed sub-boot (p0009
-&gt; 0).  
The sampling time of a TM41 in the SINAMICS mode (p4400 = 1) must be the same as that
of the emulated encoder.  
The sampling time of a TM41 in the SIMOTION mode (p4400 = 0) is determined by the
topology used

### r4154 TM41 diagnostics speed setpoint non-filtered

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**TM41 | **P-Group:**- | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [rpm] | - [rpm] | [ ] - [rpm] |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the unfiltered speed setpoint N_SETPT in revolutions per minute for diagnostic
purposes.  
In contrast to p1155, this value is updated in each DRIVE-CLiQ basic clock cycle and
displayed with sign.

**Dependency:**
  
  
Refer to:
r4155

**Note:**
  
The parameter is not effective in the SINAMICS operating mode (p4400 = 1).

## SINAMICS Parameter TM41 (Terminal Module) 04155 - 20039

SINAMICS Parameter TM41 (Terminal Module) 04155 - 20039

### r4155 TM41 diagnostics speed setpoint

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 9674 |
| **Object:**TM41 | **P-Group:**- | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [rpm] | - [rpm] | [ ] - [rpm] |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the filtered speed setpoint N_SETPT in revolutions per minute for diagnostic
purposes.  
In contrast to p1155, this value is updated in each DRIVE-CLiQ basic clock cycle and
displayed with sign.

**Dependency:**
  
  
Refer to:
r4154

**Note:**
  
The parameter is not effective in the SINAMICS operating mode (p4400 = 1).

### p4400 TM41 encoder emulation operating mode

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 9674, 9676 |
| **Object:**TM41 | **P-Group:**Closed-loop control | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 1 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the operating mode for the incremental encoder emulation.

**Value:**
  
0:
SIMOTION  
1:
SINAMICS

**Note:**
  
A change only becomes effective after the next boot.  
If value = 0:  
Incremental encoder emulation using speed setpoint (p1155).  
If value = 1:  
Incremental encoder emulation using encoder position setpoint (p4420).

### p4401 TM41 encoder emulation mode

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 9674, 9676 |
| **Object:**TM41 | **P-Group:**Closed-loop control | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 1111 0011 bin |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the mode for the incremental encoder emulation.

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Zero mark enable | No | Yes | 9674 |
| 01 | Zero marks synchronized with zero position of absolute encoders | No | Yes | 9674 |
| 04 | Activate higher actual value resolution | No | Yes | - |
| 05 | Activate higher setpoint resolution | No | Yes | - |
| 06 | Deactivate residual value handling in the setpoint channel | No | Yes | - |
| 07 | Activate output frequencies greater than 750 kHz | No | Yes | - |

**Note:**
  
For bit 00, 01:  
This bit is used to configure the zero mark via X520.  
When the TM41 is operated in the SINAMICS mode (p4400 = 1), the following applies:  
A new zero mark search is initiated by switching in the zero mark at the TM41 (p4401.0
= 1). The zero mark is output at the TM41 as soon as it was synchronized with the
zero position/zero mark of the leading encoder.  
For p4401.1 = 1, the following applies:  
The zero pulse is only output via X520 when the absolute encoder passes the zero position
of the absolute position (modulo converted).  
For p4401.1 = 0, the following applies:  
The zero pulse is output via X520 compatible with previous firmware versions (&lt; V4.3).
The zero pulse is output when the TM41 (modulo converted) passes the position it was
in when the 24 V supply was switched on.  
For bit 07:  
For hardware versions A and B, this bit has no significance (output frequency = 512
kHz).  
For p4401.7 = 0, the following applies:  
The maximum output frequency is 750 kHz (from hardware version C).  
For p4401.7 = 1, the following applies:  
The maximum output frequency is 1024 kHz (from hardware version C).

### r4402.0...2 CO/BO: TM41 encoder emulation status

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 9674, 9676 |
| **Object:**TM41 | **P-Group:**Closed-loop control | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the status of the incremental encoder emulation on Terminal Module 41 (TM41).

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Zero mark enabled | No | Yes | - |
| 01 | Tracks A/B enabled | No | Yes | - |
| 02 | Interface encoder emulation enabled | No | Yes | - |

### r4403 TM41 encoder emulation operating mode active

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 9674, 9676 |
| **Object:**TM41 | **P-Group:**Closed-loop control | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the actual operating mode of Terminal Module 41 (TM41).

**Dependency:**
  
  
Refer to:
p4400

### p4404 TM41 encoder emulation controller options

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 4) | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**TM41 | **P-Group:**Encoder | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0001 bin |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the controller option for incremental encoder emulation on Terminal Module 41
(TM41).  
p4404.0 = 1:  
Control with minimum following error (precontrol active) for synchronous position
and synchronous zero-mark emulation.  
p4404.1 = 1:  
In the case of TTL encoders, the control response improves at slow velocities.  
p4404.0 = p4404.1 = 0  
Control with fixed following error.

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Precontrol | Inactive | Active | - |
| 01 | Precontrol with adaptation for TTL encoder | Inactive | Active | - |

**Note:**
  
The parameter is only effective in the "SINAMICS" operating mode (p4400 = 1).

### p4408 TM41 encoder emulation pulse number leading encoder

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 4) | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 9674, 9676 |
| **Object:**TM41 | **P-Group:**Encoder | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 16384 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.4

**Description:**
  
Parameters p4408 and p4418 define the position setpoint format for the TM41 (CI: p4420).  
The two parameters p4408 and p4418 of the TM41 must be set the same as parameters
p0408 and p0418 of the encoder interconnected at connector input p4420. The zero mark
is only correctly output if this condition is maintained.  
For p4408 = 0, the following applies:  
Parameters p0408 and p0418 in addition assume the function of p4408 and p4418.

### p4418 TM41 encoder emulation fine resolution leading encoder

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 4) | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned8 | **Dynamic index:**- | **Func. diagram:** 9676 |
| **Object:**TM41 | **P-Group:**Encoder | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 2 | 18 | [ 0 ] 11 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.4

**Description:**
  
Parameters p4408 and p4418 define the position setpoint format for the TM41 (CI: p4420).  
The two parameters p4408 and p4418 of the TM41 must be set the same as parameters
p0408 and p0418 of the encoder interconnected at connector input p4420. The zero mark
is only correctly output if this condition is maintained.  
For p4408 = 0, the following applies:  
Parameters p0408 and p0418 in addition assume the function of p4408 and p4418.

### r4419 TM41 encoder emulation diagnostics position setpoint

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer32 | **Dynamic index:**- | **Func. diagram:** 9676 |
| **Object:**TM41 | **P-Group:**Encoder | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.4

**Description:**
  
Displays the position setpoint after taking into account the step up / step down.  
The format of this parameter is defined by p0408/p0418.

### p4420 CI: TM41 encoder emulation position setpoint

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Integer32 | **Dynamic index:**- | **Func. diagram:** 9676 |
| **Object:**TM41 | **P-Group:**Setpoints | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the signal source for the incremental encoder emulation position setpoint.

**Recommend.:**
  
The position actual value of the leading encoder in the current controller clock cycle
is available in r0479.  
This is the reason that the following BICO interconnection should be preferably set:  
CI: p4420 (TM41) = r0479 (e.g. SERVO)

**Dependency:**
  
  
Refer to:
p4400, r4403

**Notice:**
  
General conditions for incremental encoder emulation can be found in the following
literature:  
SINAMICS S120 Function Manual Drive Functions

**Note:**
  
The parameter is not effective in the SIMOTION operating mode (p4400 = 0).  
An encoder actual value (r0479) can only be interconnected once on a TM41.  
For p4401.0 = 1(enable zero mark), the following applies:  
In this case, p4420 must be interconnected with r0479 of the leading encoder.  
After successful internal, automatic synchronization, the zero mark of the incremental
encoder emulation is output in synchronism to the zero position/zero mark of the leading
encoder.  
The zero position of the leading encoder depends on the encoder type and the selected
referencing technique (p0493, p0494, p0495).

### p4421 TM41 encoder emulation deadtime compensation

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 9676 |
| **Object:**TM41 | **P-Group:**Setpoints | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| -10.00 | 10.00 | [ 0 ] 0.00 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the deadtime compensation for incremental encoder emulation.  
This factor defines the multiplier in which the encoder position setpoint of the incremental
encoder emulation is shifted depending on the velocity.

**Dependency:**
  
For p4421 = 0, the deadtime compensation for the position setpoint is switched out.  
For p4421 &lt;&gt; 0, the deadtime compensation is taken into account as follows:  
Setpoint new = setpoint via CI: p4420 + delta s * p4421  
delta s: Position change per sampling time (p4099[3]), internally smoothed  
  
Refer to:
p4400

**Note:**
  
The parameter is not effective in the SIMOTION operating mode (p4400 = 0).

### p4422 TM41 encoder emulation position setpoint inversion

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 4) | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 9676 |
| **Object:**TM41 | **P-Group:**Encoder | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 1 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting to invert the position setpoint for Terminal Module 41 (TM41).  
0 -&gt; Position setpoint (CI: p4420) is evaluated as normal.  
1 -&gt; Position setpoint (CI: p4420) is processed inverted.

**Dependency:**
  
  
Refer to:
p4420

### p4423 TM41 encoder emulation standstill adaptation

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C2( 4) | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 9676 |
| **Object:**TM41 | **P-Group:**Encoder | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 2000 | [ 0 ] 4 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets standstill adaptation on Terminal Module 41 (TM41).  
p4423 is used to specify the number of clock cycles (one clock cycle = p4099[3]) used
for encoder standstill detection. Once this time has elapsed, any potential deviation
is compensated when adaptation is active.  
Parameter value = 0: adaptation inactive  
Parameter value &gt; 0: adaptation active

**Dependency:**
  
  
Refer to:
r4403, p4404, p4420

**Danger:**
  
The option p4404.1 = 1 is only effective if TM41 DAC is being used.  
If the possibility of a TM41 DAC (new) being replaced by a TM41 SAC (old) cannot be
excluded, this option should not be set.  
TM41 SAC: Article No. = 6SL3055-0AA00-3PA0  
TM41 DAC: Article No. = 6SL3055-0AA00-3PA1

**Note:**
  
The parameter is only effective in the SINAMICS operating mode (p4400 = 1).  
The parameter value must be assigned a value of 4 or more to ensure that the system
functions properly.  
This parameter is only relevant in the following cases:  
- TTL encoder is available  
- the controller option "Precontrol with adaptation for TTL encoder" has been activated
(p4404.1 = 1)

### p4426 TM41 encoder emulation pulses for zero mark

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 9674, 9676 |
| **Object:**TM41 | **P-Group:**Encoder | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 16384 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets pulse number to output the zero mark for the incremental encoder simulation/emulation.  
Example:  
p0408 = 2048 (encoder pulses)  
p4426 = 512 (pulses for the zero mark)  
--&gt; Position direction: The zero mark is output after 512 pulses.  
--&gt; Negative direction: The zero mark is output after 1536 pulses.

**Dependency:**
  
  
Refer to:
p0408

**Note:**
  
The pulses for the zero mark (p4426) must be less than the encoder pulse number (p0408).

### r4427 TM41 encoder emulation zero mark position

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**4 |
| **Data type:**Integer32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**TM41 | **P-Group:**Encoder | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.4

**Description:**
  
Displays the position of the next zero mark in a positive traversing direction.  
The format of this parameter is defined by p0408/p0418 (the same as the position actual
value Xact1).

### r4899 Status word sequence control

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**2 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**TM41 | **P-Group:**Displays, signals | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the status word of the sequence control from Terminal Module 41 (TM41).

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Ready for switching on | No | Yes | - |
| 01 | Ready | No | Yes | - |
| 02 | Operation enabled | No | Yes | - |
| 03 | Fault present | No | Yes | - |
| 04 | Coast down active | Yes | No | - |
| 05 | Quick Stop active | Yes | No | - |
| 06 | Switching on inhibited | No | Yes | - |
| 07 | Alarm present | No | Yes | - |
| 09 | Control request | No | Yes | - |
| 14 | Motor rotates forwards | No | Yes | - |

### r4950 TEC DO-specific number

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**4 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**OEM range | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 32 | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.4

**Description:**
  
Number of Technology Extensions installed on this drive object.

**Dependency:**
  
  
Refer to:
r4951, r4952, r4955, p4956, r4957, r4958, r4959, r4960

**Note:**
  
DO: Drive Object  
TEC: Technology Extension

### r4951 TEC DO-specific identifier total length

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**4 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**OEM range | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 288 | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.4

**Description:**
  
Displays the total length of the identifier of the Technology Extensions installed
on this drive object.

**Dependency:**
  
  
Refer to:
r4950, r4952, r4955, p4956, r4957, r4958, r4959, r4960

**Note:**
  
The identifier of a Technology Extension comprises a maximum of 8 characters plus
separator.  
TEC: Technology Extension

### r4952 TEC DO-specific GUID total length

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**4 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**OEM range | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 576 | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.4

**Description:**
  
Displays the total length of the GUIDs of the Technology Extensions installed on this
drive object.

**Dependency:**
  
  
Refer to:
r4950, r4951, r4955, p4956, r4957, r4958, r4959, r4960

**Note:**
  
The GUID of a Technology Extension comprises 16 characters plus 1 character major
information plus 1 character, minor information.  
GUID: Globally Unique IDentifier  
TEC: Technology Extension

### r4955[0...n] TEC DO-specific identifier

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**4 |
| **Data type:**Unsigned8 | **Dynamic index:**r4951 | **Func. diagram:** - |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**OEM range | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.4

**Description:**
  
Displays the identifier of the Technology Extensions installed on this drive object.  
r4955[0...8]: Identifier of Technology Extension 1  
r4955[9...17]: Identifier of Technology Extension 2, ...

**Dependency:**
  
  
Refer to:
r4950, r4951, r4952, p4956, r4957, r4958, r4959, r4960

**Notice:**
  
This parameter is only indexed if at least one drive object-specific Technology Extension
exists (p4950 &gt; 0).

**Note:**
  
TEC: Technology Extension

### p4956[0...n] TEC DO-specific activation

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C1( ) T | **Calculated:**- | **Access level:**4 |
| **Data type:**Integer16 | **Dynamic index:**r4950 | **Func. diagram:** - |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**OEM range | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 1 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.4

**Description:**
  
Setting to activate the Technology Extensions installed on this drive object.  
r4956[0]: Activation of Technology Extension 1  
r4956[1]: Activation of Technology Extension 2, ...

**Value:**
  
0:
Technology Extension inactive  
1:
Technology Extension active

**Dependency:**
  
  
Refer to:
r4950, r4951, r4952, r4955, r4957, r4958, r4959, r4960

**Notice:**
  
This parameter is only indexed if at least one drive object-specific Technology Extension
exists (p4950 &gt; 0).

**Note:**
  
TEC: Technology Extension

### r4957[0...n] TEC DO-specific version

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**4 |
| **Data type:**Unsigned32 | **Dynamic index:**r4950 | **Func. diagram:** - |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**OEM range | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 4294967295 | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.4

**Description:**
  
Displays the version of the Technology Extensions installed on this drive object.  
r4957[0]: Version of Technology Extension 1  
r4957[1]: Version of Technology Extension 2, ...

**Dependency:**
  
  
Refer to:
r4950, r4951, r4952, r4955, p4956, r4958, r4959, r4960

**Notice:**
  
This parameter is only indexed if at least one drive object-specific Technology Extension
exists (p4950 &gt; 0).

**Note:**
  
TEC: Technology Extension  
Example:  
The value 1010100 should be interpreted as V01.01.01.00.

### r4958[0...n] TEC DO-specific interface version

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**4 |
| **Data type:**Unsigned32 | **Dynamic index:**r4950 | **Func. diagram:** - |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**OEM range | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.4

**Description:**
  
Displays the interface version of Technology Extensions installed on this drive object.  
r4958[0]: Interface version of Technology Extension 1  
r4958[1]: Interface version of Technology Extension 2, ...

**Dependency:**
  
  
Refer to:
r4950, r4951, r4952, r4955, p4956, r4957, r4959, r4960

**Notice:**
  
This parameter is only indexed if at least one drive object-specific Technology Extension
exists (p4950 &gt; 0).

**Note:**
  
TEC: Technology Extension  
Example:  
The value 1010100 should be interpreted as V01.01.01.00.

### r4959[0...n] TEC DO-specific GUID

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**4 |
| **Data type:**Unsigned8 | **Dynamic index:**r4952 | **Func. diagram:** - |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**OEM range | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.4

**Description:**
  
Displays the GUIDs of the Technology Extensions installed on this drive object.  
r4959[0...15]: GUID of Technology Extension 1  
r4959[16]: Major information of Technology Extension 1  
r4959[17]: Minor information of Technology Extension 1  
r4959[18...33]: GUID of Technology Extension 2  
r4959[34]: Major information of Technology Extension 2  
r4959[35]: Minor information of Technology Extension 2, ...

**Dependency:**
  
  
Refer to:
r4950, r4951, r4952, r4955, p4956, r4957, r4958, r4960

**Notice:**
  
This parameter is only indexed if at least one drive object-specific Technology Extension
exists (p4950 &gt; 0).

**Note:**
  
TEC: Technology Extension

### r4960[0...n] TEC DO-specific GUID drive object

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**4 |
| **Data type:**Unsigned8 | **Dynamic index:**r4952 | **Func. diagram:** - |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**OEM range | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.4

**Description:**
  
Displays the GUIDs of this drive object of the Technology Extensions installed on
the memory card/device memory.  
r4960[0...15]: GUID of this drive object of Technology Extension 1  
r4960[16]: Major information of this drive object of Technology Extension 1  
r4960[17]: Minor information of this drive object of Technology Extension 1  
r4960[18...33]: GUID of this drive object of Technology Extension 2  
r4960[34]: Major information of this drive object of Technology Extension 2  
r4960[35]: Minor information of this drive object of Technology Extension 2, ...

**Dependency:**
  
  
Refer to:
r4950, r4951, r4952, r4955, p4956, r4957, r4958, r4959

**Notice:**
  
This parameter is only indexed if at least one drive object-specific Technology Extension
exists (p4950 &gt; 0).

**Note:**
  
TEC: Technology Extension

### p4961[0...n] TEC DO-specific logbook module selection

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**4 |
| **Data type:**Unsigned32 | **Dynamic index:**r4950 | **Func. diagram:** - |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**OEM range | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0000 hex | FFFF FFFF hex | [ 0 ] 0000 hex |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.4

**Description:**
  
Only for service purposes.

**Note:**
  
TEC: Technology Extension

### r7760 Write protection/know-how protection status

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**- | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.4

**Description:**
  
Displays the status for the write protection and know-how protection.

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Write protection active | No | Yes | - |
| 01 | Know-how protection active | No | Yes | - |
| 02 | Know-how protection temporarily withdrawn | No | Yes | - |
| 03 | Know-how protection cannot be deactivated | No | Yes | - |
| 04 | Extended copy protection is active | No | Yes | - |
| 05 | Basic copy protection is active | No | Yes | - |
| 06 | Trace and measuring functions for diagnostic purposes active | No | Yes | - |
| 12 | Reserved, Siemens-internal | No | Yes | - |

**Dependency:**
  
  
Refer to:
p7761, p7765

**Note:**
  
KHP: Know-How Protection  
For bit 00:  
Write protection can be activated/deactivated via p7761 on the Control Unit.  
For bit 01:  
The know-how protection can be activated by entering a password (p7766 ... p7768).  
For bit 02:  
If it has already been activated, know-how protection can be temporarily deactivated
by entering the valid password in p7766. In this case, bit 1 = 0 and bit 2 = 1 offset.  
For bit 03:  
Know-how protection cannot be deactivated, as p7766 is not entered in the OEM exception
list (only the factory setting is possible). This bit is only set if know-how protection
is active (bit 1 = 1) and p7766 has not been entered in the OEM exception list.  
For bit 04:  
When know-how protection has been activated, the contents of the memory card (parameter
and DCC data) can be additionally protected against being used with other memory cards/Control
Units. This bit is only set if know-how protection is active and in p7765.0 is set
= 1.  
For bit 05:  
When know-how protection has been activated, the contents of the memory card (parameter
and DCC data) can be additionally protected against being used with other memory cards.
This bit is only set if know-how protection is active and p7765.1 is set = 1 and p7765.0
is set = 0.  
For bit 06:  
When know-how protection is activated, the drive data can be traced using the device
trace function. This bit is only set if know-how protection is active and p7765.2
is set = 1.  
For bit 12:  
Together with p7755, the bit is used to monitor write protection.  
Bit = 1, if p7755 is not equal to 0 and write protection is active (r7760.0 = 1).  
Bit = 0, if write protection was deactivated. p7755 is set to 0, and when write protection
is activated again, bit 12 remains at 0.

### p7763 KHP OEM exception list number of indices for p7764

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**- | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 1 | 500 | [ 0 ] 1 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.5

**Description:**
  
Sets the number of parameters for the OEM exception list (p7764[0...n]).  
p7764[0...n], with n = p7763 - 1

**Dependency:**
  
  
Refer to:
p7764

**Note:**
  
KHP: Know-How Protection  
Even if know-how protection is set, parameters in this list can be read and written
to.

### p7764[0...n] KHP OEM exception list

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**p7763 | **Func. diagram:** - |
| **Object:**SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, HUB, CU_LINK | **P-Group:**- | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 65535 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.5

**Description:**
  
OEM exception list (p7764[0...n] for setting parameters that should be excluded from
know-how protection.  
p7764[0...n], with n = p7763 - 1

**Dependency:**
  
The number of indices depends on p7763.  
  
Refer to:
p7763

**Note:**
  
KHP: Know-How Protection  
Even if know-how protection is set, parameters in this list can be read and written
to.

### p7770 NVRAM action

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB | **P-Group:**- | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 3 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.4

**Description:**
  
Sets the action to be executed for NVRAM data.  
At the end of the action the value is automatically set to 0.

**Value:**
  
0:
Inactive  
1:
Load NVRAM data to parameters  
2:
Load parameters to NVRAM  
3:
Reset

**Notice:**
  
After action p7770 = 1 no more pulses may be enabled.  
After action p7770 = 2, it is essential that parameters are backed up (p0977 = 1)
and that a warm restart is then performed (p0009 = 30, p0976 = 2, 3). This will apply
the values written.

**Note:**
  
If value = 1:  
This action loads the NVRAM data to the parameters.  
If value = 2:  
This action loads the parameters to the NVRAM.  
If value = 3:  
This action sets parameters p7771 ... p7774 to the factory setting.  
It is recommended to avoid placing unnecessary load on the subsequent upload/download
operation.

### p7857 Sub-boot mode

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**4 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**- | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 1 | [ 0 ] 1 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the mode for the sub-boot.

**Value:**
  
0:
Sub-boot manual  
1:
Sub-boot automatic

**Note:**
  
For p7857 = 0 (manual sub-boot) the following applies:  
The parameter should be set to 1 to start the sub-boot.

### r7871[0...15] Configuration changes drive object

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**4 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, HUB, CU_LINK | **P-Group:**- | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.6

**Description:**
  
Displays the configuration changes on the drive object.

**Index:**
  
[
0]:
Sum of the following indices  
[
1]:
p0010, p0107, p0108  
[
2]:
Drive object name (p0199)  
[
3]:
Structure-relevant parameters (e.g. p0180)  
[
4]:
BICO interconnections  
[
5]:
Activate/deactivate drive object  
[
6]:
Data backup required  
[
7]:
Reserved  
[
8]:
Reference or changeover parameters (e.g. p2000)  
[
9]:
Parameter count through Drive Control Chart (DCC)  
[
10]:
p0107, p0108  
[
11]:
Reserved  
[
12]:
Write protection and know-how protection status  
[
13]:
Reserved  
[
14]:
Reserved  
[
15]:
Reserved

**Dependency:**
  
  
Refer to:
r7868, r7870

**Note:**
  
For index [0]:  
When changing one of the following indices, then the value in this index is incremented.  
For index [1]:  
Drive object commissioning: When changing p0010, p0107 or p0108, the value in this
index is incremented.  
For index [2]:  
Drive object name. When changing p0199, the value in this index is incremented.  
For index [3]:  
Drive object structure. When changing a parameter that is relevant for the structure
(e.g. number of data sets), the value in this index is incremented.  
For index [4]:  
Drive object BICO interconnections. When changing r3977, the value in this index is
incremented.  
For index [5]:  
Drive object activity: When changing p0105, the value in this index is incremented.  
For index [6]:  
Drive object, data save.  
0: There are no parameter changes to save.  
1: There are parameter changes to save.  
For index [8]:  
Drive object changeover of units. When changing reference or changeover parameters
(e.g. p2000, p0304), the value in this index is incremented.  
For index [9]:  
Drive object parameter count. When changing the number of parameters by loading Drive
Control Chart (DCC), the value in this index is incremented.  
For index [10]:  
Drive object configuration. When changing either p0107 or p0108, the value in this
index is incremented.  
For index [12]:  
Drive object configuration. When activating/deactivating write protection or know-how
protection, the value in this index is incremented.

### r7872[0...3] Drive object status changes

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**4 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**- | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the status changes on the drive object.

**Index:**
  
[
0]:
Sum of the following indices  
[
1]:
Faults (r0944)  
[
2]:
Alarms (r2121)  
[
3]:
Safety messages (r9744)

**Dependency:**
  
  
Refer to:
r7869

**Note:**
  
For index [0]:  
When changing one of the following indices, then the value in this index is incremented.  
For index [1]:  
Drive object faults. When changing r0944, the value in this index is incremented.  
For index [2]:  
Drive object alarms. When changing r2121, the value in this index is incremented.  
For index [3]:  
Drive object safety messages. When changing r9744, the value in this index is incremented.

### p8837 IF2 STW1.10 = 0 mode

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM41, ENC, ENC_840 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 2 | [ 0 ] 2 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.4

**Description:**
  
Sets the processing mode for PROFIdrive STW1.10 "master control by PLC".  
Generally, control world 1 is received with the first receive word (PZD1) (this is
in conformance to the PROFIdrive profile). The behavior of STW1.10 = 0 corresponds
to that of the PROFIdrive profile. For other applications that deviate from this,
the behavior can be adapted using this particular parameter.

**Recommend.:**
  
Do not change the setting p2037 = 0.

**Value:**
  
0:
Freeze setpoints and continue to process sign-of-life  
1:
Freeze setpoints and sign-of-life  
2:
Do not freeze setpoints

**Note:**
  
If the STW1 is not transferred according to the PROFIdrive with PZD1 (with bit 10
"master control by PLC"), then p2037 should be set to 2.

### p8844 IF2 fault delay

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 2410 |
| **Object:**SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM41, ENC, ENC_840 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 [s] | 100 [s] | [ 0 ] 0 [s] |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.4

**Description:**
  
Sets the delay time to initiate fault F01910 after a setpoint failure.  
The time until the fault is initiated can be used by the application. This means that
it is possible to respond to the failure while the drive is still operational (e.g.
emergency retraction).

**Dependency:**
  
  
Refer to:
r2043  
Refer to:
F01910

### r8850[0...21] CO: IF2 PZD receive word

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 2485, 2491, 9204, 9206 |
| **Object:**SERVO, HLA, SERVO_AC, SERVO_840, HLA_840, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, TM41 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**4000H | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
5.2

**Description:**
  
Connector output for interconnecting the PZD (setpoints) received via interface 2
in the word format.

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
r8860, r8890, r8891, r8892, r8893

**Notice:**
  
Where there is a multiple interconnection of a connector output, all the connector
inputs must either have Integer or FloatingPoint data types.  
A BICO interconnection for a single PZD can only take place either on r8850 or r8860.

**Note:**
  
IF2: Interface 2  
PZD1 to PZD4 are displayed bit-serially in r8890 to r8893.

### p8851[0...27] CI: IF2 PZD send word

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Integer16 | **Dynamic index:**- | **Func. diagram:** 2487, 9208 |
| **Object:**SERVO, HLA, SERVO_AC, SERVO_840, HLA_840, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, TM41 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**4000H | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.4

**Description:**
  
Selects the PZD (actual values) to be sent via interface 2 in the word format.

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
  
  
Refer to:
p8861

**Note:**
  
IF2: Interface 2

### r8853[0...27] IF2 diagnostics PZD send

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 2487, 9208, 9210 |
| **Object:**SERVO, HLA, SERVO_AC, SERVO_840, HLA_840, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, TM41 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.4

**Description:**
  
Displays the sent PZD (actual values) sent via interface 2.

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

**Dependency:**
  
  
Refer to:
p8851, p8861

**Note:**
  
IF2: Interface 2

### r8860[0...20] CO: IF2 PZD receive double word

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer32 | **Dynamic index:**- | **Func. diagram:** 2485, 9204, 9206 |
| **Object:**SERVO, HLA, SERVO_AC, SERVO_840, HLA_840, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, TM41 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**4000H | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
5.2

**Description:**
  
Connector output for interconnecting the PZD (setpoints) received via interface 2
in the double word format.

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
r8850

**Notice:**
  
Where there is a multiple interconnection of a connector output, all the connector
inputs must either have Integer or FloatingPoint data types.  
A BICO interconnection for a single PZD can only take place either on r8850 or r8860.  
A maximum of 4 indices of the "trace" function can be used.

**Note:**
  
IF2: Interface 2

### p8861[0...26] CI: IF2 PZD send double word

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Integer32 | **Dynamic index:**- | **Func. diagram:** 2487, 9208, 9210 |
| **Object:**SERVO, HLA, SERVO_AC, SERVO_840, HLA_840, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, TM41 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**4000H | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.4

**Description:**
  
Selects the PZD (actual values) to be sent via interface 2 in the double word format.

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
  
  
Refer to:
p8851

**Notice:**
  
A BICO interconnection for a single PZD can only take place either on p8851 or p8861.

**Note:**
  
IF2: Interface 2

### r8863[0...26] IF2 diagnostics PZD send double word

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 2487 |
| **Object:**SERVO, HLA, SERVO_AC, SERVO_840, HLA_840, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, TM41 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.4

**Description:**
  
Displays the PZD sent via interface 2 (actual values) with double word format.

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

**Notice:**
  
A maximum of 4 indices of the "trace" function can be used.

**Note:**
  
IF2: Interface 2

### r8867[0...1] IF2 PZD maximum interconnected

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM15DI_DO, TM120, TM150, TB30, ENC, ENC_840 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.5

**Description:**
  
Display for the maximum interconnected PZD in the receive/send direction  
Index 0: receive (r8850, r8860)  
Index 1: send (p8851, p8861)

### p8870[0...15] SINAMICS Link PZD receive word

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 2198, 2199 |
| **Object:**CU_G130_PN (PN CBE20), CU_S120_PN (PN CBE20), CU_G150_PN (PN CBE20), CU_S150_PN (PN CBE20), CU_G130_DP (PN CBE20), CU_S120_DP (PN CBE20), CU_G150_DP (PN CBE20), CU_S150_DP (PN CBE20), CU_DC_S (PN CBE20), CU_DC_R_S (PN CBE20), CU_DC (PN CBE20), CU_DC_R (PN CBE20), SERVO (PN CBE20), HLA (PN CBE20), SERVO_840 (PN CBE20), HLA_840 (PN CBE20), HLA_828 (PN CBE20), SERVO_DBSI (PN CBE20), HLA_DBSI (PN CBE20), A_INF (PN CBE20), S_INF (PN CBE20), R_INF (PN CBE20), B_INF (PN CBE20), A_INF_840 (PN CBE20), S_INF_840 (PN CBE20), B_INF_840 (PN CBE20), A_INF_828 (PN CBE20), S_INF_828 (PN CBE20), B_INF_828 (PN CBE20), TM31 (PN CBE20), TM41 (PN CBE20), TM17 (PN CBE20), TM15 (PN CBE20), TM15DI_DO (PN CBE20), TM120 (PN CBE20), TM150 (PN CBE20), TB30 (PN CBE20), ENC (PN CBE20), ENC_840 (PN CBE20) | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 32 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.4

**Description:**
  
Assignment of a PZD to a telegram word from a SINAMICS Link receive telegram.  
For p8839[0] = 2 (COMM BOARD via interface 1), the following applies:  
- PZD p2050[index] is assigned by means of p8870[index], p8872[index].  
For p8839[1] = 2 (COMM BOARD via interface 2), the following applies:  
- using p8870[index], p8872[index], the PZD is assigned r8850[Index].

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

**Dependency:**
  
  
Refer to:
p8872

**Note:**
  
Value range:  
0: Not used  
1 ... 32: telegram word  
A pair of values p8870[index], p8872[index] may only be used once in single a device.  
A change only becomes effective after POWER ON, reset, project download or p8842 =
1.

### p8871[0...15] SINAMICS Link PZD send word

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 2198, 2199 |
| **Object:**CU_G130_PN (PN CBE20), CU_S120_PN (PN CBE20), CU_G150_PN (PN CBE20), CU_S150_PN (PN CBE20), CU_G130_DP (PN CBE20), CU_S120_DP (PN CBE20), CU_G150_DP (PN CBE20), CU_S150_DP (PN CBE20), CU_DC_S (PN CBE20), CU_DC_R_S (PN CBE20), CU_DC (PN CBE20), CU_DC_R (PN CBE20), SERVO (PN CBE20), HLA (PN CBE20), SERVO_840 (PN CBE20), HLA_840 (PN CBE20), HLA_828 (PN CBE20), SERVO_DBSI (PN CBE20), HLA_DBSI (PN CBE20), A_INF (PN CBE20), S_INF (PN CBE20), R_INF (PN CBE20), B_INF (PN CBE20), A_INF_840 (PN CBE20), S_INF_840 (PN CBE20), B_INF_840 (PN CBE20), A_INF_828 (PN CBE20), S_INF_828 (PN CBE20), B_INF_828 (PN CBE20), TM31 (PN CBE20), TM41 (PN CBE20), TM17 (PN CBE20), TM15 (PN CBE20), TM15DI_DO (PN CBE20), TM120 (PN CBE20), TM150 (PN CBE20), TB30 (PN CBE20), ENC (PN CBE20), ENC_840 (PN CBE20) | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 32 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.4

**Description:**
  
Assigns a PZD to a telegram word in the SINAMICS Link send telegram.  
For p8839[0] = 2 (COMM BOARD via interface 1), the following applies:  
- p8871[index] assigns PZD p2051[index].  
For p8839[1] = 2 (COMM BOARD via interface 2), the following applies:  
- p8871[index] assigns PZD p8851[index].

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

**Dependency:**
  
  
Refer to:
p2051, p8851  
Refer to:
A50002

**Note:**
  
Value range:  
0: Not used  
1 ... 32: send telegram word  
A specific telegram word send may only be used once within a single device.  
A change only becomes effective after POWER ON, reset, project download or p8842 =
1.

### p8872[0...15] SINAMICS Link PZD receive address

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 2198, 2199 |
| **Object:**CU_G130_PN (PN CBE20), CU_S120_PN (PN CBE20), CU_G150_PN (PN CBE20), CU_S150_PN (PN CBE20), CU_G130_DP (PN CBE20), CU_S120_DP (PN CBE20), CU_G150_DP (PN CBE20), CU_S150_DP (PN CBE20), CU_DC_S (PN CBE20), CU_DC_R_S (PN CBE20), CU_DC (PN CBE20), CU_DC_R (PN CBE20), SERVO (PN CBE20), HLA (PN CBE20), SERVO_840 (PN CBE20), HLA_840 (PN CBE20), HLA_828 (PN CBE20), SERVO_DBSI (PN CBE20), HLA_DBSI (PN CBE20), A_INF (PN CBE20), S_INF (PN CBE20), R_INF (PN CBE20), B_INF (PN CBE20), A_INF_840 (PN CBE20), S_INF_840 (PN CBE20), B_INF_840 (PN CBE20), A_INF_828 (PN CBE20), S_INF_828 (PN CBE20), B_INF_828 (PN CBE20), TM31 (PN CBE20), TM41 (PN CBE20), TM17 (PN CBE20), TM15 (PN CBE20), TM15DI_DO (PN CBE20), TM120 (PN CBE20), TM150 (PN CBE20), TB30 (PN CBE20), ENC (PN CBE20), ENC_840 (PN CBE20) | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 64 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.4

**Description:**
  
Selects the address of the SINAMICS Link sender from which the process data (PZD)
is received.

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

**Dependency:**
  
  
Refer to:
p8870

**Note:**
  
Value range:  
0: Not used  
1 ... 64: address  
A change only becomes effective after POWER ON, reset, project download or p8842 =
1.

### r8874[0...21] IF2 diagnostics bus address PZD receive

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**SERVO, HLA, SERVO_AC, SERVO_840, HLA_840, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, TM41 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
5.2

**Description:**
  
Displays the bus address of sender from which the PZD is received.

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

**Note:**
  
IF2: Interface 2  
Value range:  
0 - 125: Bus address of the sender  
255: Not assigned

### r8875[0...21] IF2 diagnostics telegram offset PZD receive

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**SERVO, HLA, SERVO_AC, SERVO_840, HLA_840, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, TM41 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
5.2

**Description:**
  
Displays the byte offset of the PZD in the receive telegram.

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

**Note:**
  
IF2: Interface 2  
Value range:  
0 - 242: Byte offset  
255: Not assigned

### r8876[0...27] IF2 diagnostics telegram offset PZD send

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**SERVO, HLA, SERVO_AC, SERVO_840, HLA_840, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, TM41 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.4

**Description:**
  
Displays the byte offset of the PZD in the send telegram.

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

**Note:**
  
IF2: Interface 2  
Value range:  
0 - 242: Byte offset  
255: Not assigned

### p8880[0...15] BI: IF2 binector-connector converter status word 1

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 2489 |
| **Object:**CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM15DI_DO, TM120, TM150, ENC, ENC_840 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.8

**Description:**
  
Selects bits to be sent via interface 2.  
The individual bits are combined to form status word 1.

**Index:**
  
[
0]:
Bit 0  
[
1]:
Bit 1  
[
2]:
Bit 2  
[
3]:
Bit 3  
[
4]:
Bit 4  
[
5]:
Bit 5  
[
6]:
Bit 6  
[
7]:
Bit 7  
[
8]:
Bit 8  
[
9]:
Bit 9  
[
10]:
Bit 10  
[
11]:
Bit 11  
[
12]:
Bit 12  
[
13]:
Bit 13  
[
14]:
Bit 14  
[
15]:
Bit 15

**Dependency:**
  
  
Refer to:
p8888, r8889

### p8881[0...15] BI: IF2 binector-connector converter status word 2

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 2489 |
| **Object:**CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM15DI_DO, TM120, TM150, ENC, ENC_840 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.8

**Description:**
  
Selects bits to be sent via interface 2.  
The individual bits are combined to form status word 2.

**Index:**
  
[
0]:
Bit 0  
[
1]:
Bit 1  
[
2]:
Bit 2  
[
3]:
Bit 3  
[
4]:
Bit 4  
[
5]:
Bit 5  
[
6]:
Bit 6  
[
7]:
Bit 7  
[
8]:
Bit 8  
[
9]:
Bit 9  
[
10]:
Bit 10  
[
11]:
Bit 11  
[
12]:
Bit 12  
[
13]:
Bit 13  
[
14]:
Bit 14  
[
15]:
Bit 15

**Dependency:**
  
  
Refer to:
p8888, r8889

### p8882[0...15] BI: IF2 binector-connector converter status word 3

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 2489 |
| **Object:**CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM15DI_DO, TM120, TM150, ENC, ENC_840 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.8

**Description:**
  
Selects bits to be sent via interface 2.  
The individual bits are combined to form free status word 3.

**Index:**
  
[
0]:
Bit 0  
[
1]:
Bit 1  
[
2]:
Bit 2  
[
3]:
Bit 3  
[
4]:
Bit 4  
[
5]:
Bit 5  
[
6]:
Bit 6  
[
7]:
Bit 7  
[
8]:
Bit 8  
[
9]:
Bit 9  
[
10]:
Bit 10  
[
11]:
Bit 11  
[
12]:
Bit 12  
[
13]:
Bit 13  
[
14]:
Bit 14  
[
15]:
Bit 15

**Dependency:**
  
  
Refer to:
p8888, r8889

### p8883[0...15] BI: IF2 binector-connector converter status word 4

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 2489 |
| **Object:**CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM15DI_DO, TM120, TM150, ENC, ENC_840 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.8

**Description:**
  
Selects bits to be sent via interface 2.  
The individual bits are combined to form free status word 4.

**Index:**
  
[
0]:
Bit 0  
[
1]:
Bit 1  
[
2]:
Bit 2  
[
3]:
Bit 3  
[
4]:
Bit 4  
[
5]:
Bit 5  
[
6]:
Bit 6  
[
7]:
Bit 7  
[
8]:
Bit 8  
[
9]:
Bit 9  
[
10]:
Bit 10  
[
11]:
Bit 11  
[
12]:
Bit 12  
[
13]:
Bit 13  
[
14]:
Bit 14  
[
15]:
Bit 15

**Dependency:**
  
  
Refer to:
p8888, r8889

### p8884[0...15] BI: IF2 binector-connector converter status word 5

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 2489 |
| **Object:**CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM15DI_DO, TM120, TM150, ENC, ENC_840 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.8

**Description:**
  
Selects bits to be sent via interface 2.  
The individual bits are combined to form free status word 5.

**Index:**
  
[
0]:
Bit 0  
[
1]:
Bit 1  
[
2]:
Bit 2  
[
3]:
Bit 3  
[
4]:
Bit 4  
[
5]:
Bit 5  
[
6]:
Bit 6  
[
7]:
Bit 7  
[
8]:
Bit 8  
[
9]:
Bit 9  
[
10]:
Bit 10  
[
11]:
Bit 11  
[
12]:
Bit 12  
[
13]:
Bit 13  
[
14]:
Bit 14  
[
15]:
Bit 15

**Dependency:**
  
  
Refer to:
p8888, r8889

### p8888[0...4] IF2 invert binector-connector converter status word

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 2489 |
| **Object:**CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM15DI_DO, TM120, TM150, ENC, ENC_840 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0000 0000 0000 0000 bin |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.8

**Description:**
  
Setting to invert the individual binector inputs of the binector-connector converter.

**Index:**
  
[
0]:
Status word 1  
[
1]:
Status word 2  
[
2]:
Free status word 3  
[
3]:
Free status word 4  
[
4]:
Free status word 5

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Bit 0 | Not inverted | Inverted | - |
| 01 | Bit 1 | Not inverted | Inverted | - |
| 02 | Bit 2 | Not inverted | Inverted | - |
| 03 | Bit 3 | Not inverted | Inverted | - |
| 04 | Bit 4 | Not inverted | Inverted | - |
| 05 | Bit 5 | Not inverted | Inverted | - |
| 06 | Bit 6 | Not inverted | Inverted | - |
| 07 | Bit 7 | Not inverted | Inverted | - |
| 08 | Bit 8 | Not inverted | Inverted | - |
| 09 | Bit 9 | Not inverted | Inverted | - |
| 10 | Bit 10 | Not inverted | Inverted | - |
| 11 | Bit 11 | Not inverted | Inverted | - |
| 12 | Bit 12 | Not inverted | Inverted | - |
| 13 | Bit 13 | Not inverted | Inverted | - |
| 14 | Bit 14 | Not inverted | Inverted | - |
| 15 | Bit 15 | Not inverted | Inverted | - |

**Dependency:**
  
  
Refer to:
p8880, p8881, p8882, p8883, p8884, r8889

### r8889[0...4] CO: IF2 send binector-connector converter status word

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM15DI_DO, TM120, TM150, ENC, ENC_840 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.8

**Description:**
  
Connector output to interconnect the status words to a PZD send word.

**Index:**
  
[
0]:
Status word 1  
[
1]:
Status word 2  
[
2]:
Free status word 3  
[
3]:
Free status word 4  
[
4]:
Free status word 5

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

**Dependency:**
  
  
Refer to:
p8851, p8880, p8881, p8882, p8883, p8884, p8888

**Note:**
  
r8889 together with p8880 to p8884 forms five binector-connector converters.

### r8890.0...15 BO: IF2 PZD1 receive bit-serial

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 2485, 2491, 9204, 9206 |
| **Object:**CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM15DI_DO, TM120, TM150, TB30, ENC, ENC_840 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.4

**Description:**
  
Binector output for bit-serial interconnection of PZD1 (normally control word 1) received
via interface 2.

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

**Dependency:**
  
  
Refer to:
r8850

**Note:**
  
IF2: Interface 2

### r8891.0...15 BO: IF2 PZD2 receive bit-serial

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 2485, 2491, 9204, 9206 |
| **Object:**CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM15DI_DO, TM120, TM150, TB30, ENC, ENC_840 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.4

**Description:**
  
Binector output for bit-serial interconnection of PZD2 received via interface 2.

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

**Dependency:**
  
  
Refer to:
r8850

**Note:**
  
IF2: Interface 2

### r8892.0...15 BO: IF2 PZD3 receive bit-serial

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 2485, 9204, 9206 |
| **Object:**CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, TM41, ENC, ENC_840 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.4

**Description:**
  
Binector output for bit-serial interconnection of PZD3 received via interface 2.

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

**Dependency:**
  
  
Refer to:
r8850

**Note:**
  
IF2: Interface 2

### r8893.0...15 BO: IF2 PZD4 receive bit-serial

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 2485, 9204, 9206 |
| **Object:**CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, TM41, ENC, ENC_840 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.4

**Description:**
  
Binector output for bit-serial interconnection of PZD4 (normally control word 2) received
via interface 2.

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

**Dependency:**
  
  
Refer to:
r8850

**Note:**
  
IF2: Interface 2

### r8894.0...15 BO: IF2 connector-binector converter binector output

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 2485, 2491 |
| **Object:**CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM15DI_DO, TM120, TM150, ENC, ENC_840 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.8

**Description:**
  
Binector output for bit-serial interconnection of a PZD word received via interface
2.  
The PZD is selected via p8899[0].

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

**Dependency:**
  
  
Refer to:
p8899

### r8895.0...15 BO: IF2 connector-binector converter binector output

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 2485, 2491 |
| **Object:**CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM15DI_DO, TM120, TM150, ENC, ENC_840 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.8

**Description:**
  
Binector output for bit-serial interconnection of a PZD word received via interface
2.  
The PZD is selected via p8899[1].

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

**Dependency:**
  
  
Refer to:
p8898, p8899

### p8898[0...1] IF2 invert connector-binector converter binector output

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 2485, 2491 |
| **Object:**CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM15DI_DO, TM120, TM150, ENC, ENC_840 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0000 0000 0000 0000 bin |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.8

**Description:**
  
Setting to invert the individual binector outputs of the connector-binector converter.  
Using p8898[0], the signals of CI: p8899[0] are influenced.  
Using p8898[1], the signals of CI: p8899[1] are influenced.

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Bit 0 | Not inverted | Inverted | - |
| 01 | Bit 1 | Not inverted | Inverted | - |
| 02 | Bit 2 | Not inverted | Inverted | - |
| 03 | Bit 3 | Not inverted | Inverted | - |
| 04 | Bit 4 | Not inverted | Inverted | - |
| 05 | Bit 5 | Not inverted | Inverted | - |
| 06 | Bit 6 | Not inverted | Inverted | - |
| 07 | Bit 7 | Not inverted | Inverted | - |
| 08 | Bit 8 | Not inverted | Inverted | - |
| 09 | Bit 9 | Not inverted | Inverted | - |
| 10 | Bit 10 | Not inverted | Inverted | - |
| 11 | Bit 11 | Not inverted | Inverted | - |
| 12 | Bit 12 | Not inverted | Inverted | - |
| 13 | Bit 13 | Not inverted | Inverted | - |
| 14 | Bit 14 | Not inverted | Inverted | - |
| 15 | Bit 15 | Not inverted | Inverted | - |

**Dependency:**
  
  
Refer to:
r8894, r8895, p8899

### p8899[0...1] CI: IF2 connector-binector converter signal source

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Integer16 | **Dynamic index:**- | **Func. diagram:** 2485, 2491 |
| **Object:**CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM15DI_DO, TM120, TM150, ENC, ENC_840 | **P-Group:**Communications | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.8

**Description:**
  
Sets the signal source for the connector-binector converter.  
A PZD receive word can be selected as signal source. The signals are available to
be serially passed-on (interconnection).

**Dependency:**
  
  
Refer to:
r8850, r8894, r8895, p8898

**Note:**
  
From the signal source set via the connector input, the corresponding lower 16 bits
are converted.  
p8899[0...1] together with r8894.0...15 and r8895.0...15 forms two connector-binector
converters:  
Connector input p8899[0] to binector output in r8894.0...15  
Connector input p8899[1] to binector output in r8895.0...15

### r8960[0...3] PN subslot controller assignment

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned8 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM15DI_DO, TM120, TM150, TB30, ENC, ENC_840 | **P-Group:**- | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 8 | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.9

**Description:**
  
Displays the controller assignment of a PROFINET subslot on the actual drive object.  
The display is only relevant for Shared Device.

**Index:**
  
[
0]:
Subslot 2 PROFIsafe  
[
1]:
Subslot 3 PZD telegram  
[
2]:
Subslot 4 PZD supplementary data  
[
3]:
Subslot 5 PZD supplementary data

**Dependency:**
  
  
Refer to:
r8961, r8962

**Note:**
  
Example:  
If the parameter contains the value 2 in index [1], then this means that subslot 3
is assigned to controller 2.

### r8970[0...3] CBExx subslot controller assignment

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned8 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**CU_G130_PN (PN CBE20), CU_S_AC_DP (CBE41 TSN), CU_S_AC_PN (CBE41 TSN), CU_S120_PN (CBE41 TSN, PN CBE20, PN CBE25), CU_G150_PN (PN CBE20), CU_S150_PN (CBE41 TSN, PN CBE20, PN CBE25), CU_G130_DP (PN CBE20), CU_S120_DP (CBE41 TSN, PN CBE20, PN CBE25), CU_G150_DP (PN CBE20), CU_S150_DP (CBE41 TSN, PN CBE20, PN CBE25), EXC1 (PN CBE20), CU_DC_S (PN CBE20), CU_DC_R_S (PN CBE20), CU_DC (PN CBE20), CU_DC_R (PN CBE20), SERVO (PN CBE20), VECTOR (PN CBE20), HLA (PN CBE20), VECTOR_G (PN CBE20), SERVO_AC (PN CBE20), VECTOR_AC (PN CBE20), EXC2 (PN CBE20), DC_CTRL_S (PN CBE20), DC_CTRL_R_S (PN CBE20), DC_CTRL (PN CBE20), DC_CTRL_R (PN CBE20), SERVO_840 (PN CBE20), HLA_840 (PN CBE20), HLA_828 (PN CBE20), SERVO_DBSI (PN CBE20), HLA_DBSI (PN CBE20), SERVO_I_AC (PN CBE20), VECTOR_I_AC (PN CBE20), A_INF (PN CBE20), S_INF (PN CBE20), R_INF (PN CBE20), B_INF (PN CBE20), A_INF_840 (PN CBE20), S_INF_840 (PN CBE20), B_INF_840 (PN CBE20), A_INF_828 (PN CBE20), S_INF_828 (PN CBE20), B_INF_828 (PN CBE20), TM31 (PN CBE20), TM41 (PN CBE20), TM17 (PN CBE20), TM15 (PN CBE20), TM15DI_DO (PN CBE20), TM120 (PN CBE20), TM150 (PN CBE20), TB30 (PN CBE20), ENC (PN CBE20), ENC_840 (PN CBE20) | **P-Group:**- | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 8 | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.9

**Description:**
  
Displays the controller assignment of a PROFINET subslot on the actual drive object.

**Index:**
  
[
0]:
Subslot 2 PROFIsafe  
[
1]:
Subslot 3 PZD telegram  
[
2]:
Subslot 4 PZD supplementary data  
[
3]:
Subslot 5 PZD supplementary data

**Dependency:**
  
  
Refer to:
r8971, r8972

**Note:**
  
Example:  
If the parameter contains the value 2 in index [1], then this means that subslot 3
is assigned to controller 2.

### r9406[0...19] PS file parameter number parameter not transferred

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**- | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the parameters that were not able to be transferred when reading the parameter
back-up files (PS files) from the non-volatile memory (e.g. memory card).  
r9406[0] = 0  
--&gt; All of the parameter values were able to be transferred error-free.  
r9406[0...x] &gt; 0  
--&gt; indicates the parameter number in the following cases:  
- parameter, whose value was not able to be completely accepted.  
- indexed parameter, where at least 1 index was not able to be accepted. The first
index that is not transferred is displayed in r9407.

**Dependency:**
  
  
Refer to:
r9407, r9408

**Note:**
  
All indices from r9406 to r9408 designate the same parameter.  
r9406[x] parameter number, parameter not accepted  
r9407[x] parameter index, parameter not accepted  
r9408[x] fault code, parameter not accepted

### r9407[0...19] PS file parameter index parameter not transferred

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**- | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the first index of the parameters that could not be transferred when the
parameter backup files (PS files) were read from the non-volatile memory (e.g. memory
card).  
If, from an indexed parameter, at least one index was not able to be transferred,
then the parameter number is displayed in r9406[n] and the first index that was not
transferred is displayed in r9407[n].  
r9406[0] = 0  
--&gt; All of the parameter values were able to be transferred error-free.  
r9406[n] &gt; 0  
--&gt; Displays r9407[n] the first index of the parameter number r9406[n] that was not
transferred.

**Dependency:**
  
  
Refer to:
r9406, r9408

**Note:**
  
All indices from r9406 to r9408 designate the same parameter.  
r9406[x] parameter number, parameter not accepted  
r9407[x] parameter index, parameter not accepted  
r9408[x] fault code, parameter not accepted

### r9408[0...19] PS file fault code parameter not transferred

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_COMBI, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**- | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Only for internal Siemens service purposes.

**Dependency:**
  
  
Refer to:
r9406, r9407

**Note:**
  
All indices from r9406 to r9408 designate the same parameter.  
r9406[x] parameter number, parameter not accepted  
r9407[x] parameter index, parameter not accepted  
r9408[x] fault code, parameter not accepted

### r9409 Number of parameters to be saved

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**4 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**- | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the number of modified parameters and those that have still not be saved
for this drive object.

**Dependency:**
  
  
Refer to:
p0971, p0977

**Notice:**
  
Inherent to the system, the list of the parameters to be backed up is empty after
the following actions:  
- Download  
- Warm restart  
- Factory setting  
In these cases, a new parameter backup must be initiated, which is then the starting
point for the list of modified parameters.

**Note:**
  
The modified parameters that still need to be saved are internally listed in r9410
... r9419.

### r9450[0...29] Reference value change parameter with unsuccessful calculation

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**2 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM41, ENC, ENC_840 | **P-Group:**- | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the parameters for which the re-calculation was unsuccessful after an internal
system reference value change.

**Dependency:**
  
  
Refer to:
F07086

### r9451[0...29] Units changeover adapted parameters

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM41, ENC, ENC_840 | **P-Group:**- | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the parameters whose parameter would have to be changed during a units changeover.

**Dependency:**
  
  
Refer to:
F07088

### r9490 Number of BICO interconnections to other drives

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**Commands | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the number of signal sources from this drive to other drives/drive objects
(Binector Output/Connector Output, BO/CO).

**Dependency:**
  
  
Refer to:
r9491, r9492, p9493

### r9491[0...9] BI/CI of BICO interconnections to other drives

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**Commands | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the signal receiver list (Binector Input/Connector Input, BI/CI) for the
first interconnections between this drive and other drives/drive objects.

**Dependency:**
  
  
Refer to:
r9490, r9492, p9493

**Notice:**
  
A drive cannot be deleted if this list is not empty!  
Otherwise, another drive would continue to attempt to read a signal from a drive that
no longer existed.

**Note:**
  
All indices of r9491 to p9493 designate the same interconnection.  
r9491[x] contains the signal receiver and r9492[x] the matching signal source; p9493[x]
can be set to modify the interconnection.

### r9492[0...9] BO/CO of BICO interconnections to other drives

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**Commands | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the signal source list (Binector Output/Connector Output, BO/CO) for the
first interconnections between this drive and other drives/drive objects.

**Dependency:**
  
  
Refer to:
r9490, r9491, p9493

**Notice:**
  
A drive cannot be deleted if this list is not empty!  
Otherwise, another drive would continue to attempt to read a signal from a drive that
no longer existed.

**Note:**
  
All indices of r9491 to p9493 designate the same interconnection.  
r9491[x] contains the signal receiver and r9492[x] the matching signal source; p9493[x]
can be set to modify the interconnection.

### p9493[0...9] Reset BICO interconnections to other drives

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, TM54F_MA, TM54F_SL, ENC, ENC_840, HUB, CU_LINK | **P-Group:**- | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 15 | [ 0 ] 15 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting to reset the BICO interconnections to other drives.  
Each interconnection can be individually reset.

**Value:**
  
0:
Set connection to 0  
1:
Set connection to 1 (100 %)  
2:
Set connection to factory setting  
15:
Finished

**Dependency:**
  
  
Refer to:
r9490, r9491, r9492

**Note:**
  
All indices of r9491 to p9493 designate the same interconnection.  
r9491[x] contains the signal receiver and r9492[x] the matching signal source; p9493[x]
can be set to modify the interconnection.

### p9495 BICO behavior for deactivated drive objects

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, ENC, ENC_840, CU_LINK | **P-Group:**- | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 2 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the behavior for BICO interconnections to drive objects that are either not capable
of operation or have been deactivated.  
BO/CO parameters are on the drive object that is either not capable of operation or
has been deactivated (signal source).

**Value:**
  
0:
Inactive  
1:
Save interconnections  
2:
Save interconnections and establish the factory setting

**Dependency:**
  
  
Refer to:
p9496, p9497, p9498, p9499  
Refer to:
A01318, A01507

**Note:**
  
For p9495 = 0, the following applies:  
- the number of interconnections is zero (p9497 = 0).  
For p9495 not equal to 0, the following applies:  
- the BI/CI parameters involved are listed in p9498[0...29] (signal sink).  
- the associated BO/CO parameters are listed in p9499[0...29] (signal source).

### p9496 BICO behavior when activating drive objects

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, ENC, ENC_840, CU_LINK | **P-Group:**- | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 2 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Sets the behavior when activating BICO interconnections to drive objects that are
either not capable of operation or have been deactivated.

**Value:**
  
0:
Inactive  
1:
Restore the interconnections from the list  
2:
Delete the interconnections from the list

**Dependency:**
  
  
Refer to:
p9495, p9497, p9498, p9499  
Refer to:
A01318, A01507

**Note:**
  
The BI/CI parameters involved are listed in p9498[0...29] (signal sink).  
The associated BO/CO parameters are listed in p9499[0...29] (signal source).  
After p9496 = 1, 2 the following applies:  
- p9497 = 0  
- p9496 = 0

### p9497 BICO interconnections to deactivated drive objects number

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, ENC, ENC_840, CU_LINK | **P-Group:**Commands | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 65535 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the number of saved BICO interconnections to drive objects that are either
not capable of operation or have been deactivated.  
BO/CO parameters are on the drive object that is either not capable of operation or
has been deactivated (signal source).

**Dependency:**
  
  
Refer to:
p9495, p9496, p9498, p9499  
Refer to:
A01318, A01507

### p9498[0...29] BICO BI/CI parameters to deactivated drive objects

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, ENC, ENC_840, CU_LINK | **P-Group:**Commands | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the saved BI/CI parameters (signal sink), whose source is located on drive
objects that are either not capable of operation or have been deactivated.

**Dependency:**
  
  
Refer to:
p9495, p9496, p9497, p9499  
Refer to:
A01318, A01507

**Note:**
  
A BICO interconnection (signal sink, signal source) is displayed in the same index
of p9498 and p9499.

### p9499[0...29] BICO BO/CO parameters to deactivated drive objects

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**CU_I, CU_NX_CX, CU_G130_PN, CU_S_AC_DP, CU_S_AC_PN, CU_S120_PN, CU_G150_PN, CU_S150_PN, CU_G130_DP, CU_S120_DP, CU_G150_DP, CU_S150_DP, EXC1, CU_DC_S, CU_DC_R_S, CU_DC, CU_DC_R, CU_I_840, CU_NX_840, CU_I_COMBI, CU_NX_COMBI, CU_I_828, CU_NX_828, CU_I_D410, SERVO, VECTOR, HLA, VECTOR_G, SERVO_AC, VECTOR_AC, EXC2, DC_CTRL_S, DC_CTRL_R_S, DC_CTRL, DC_CTRL_R, SERVO_840, HLA_840, SERVO_828, HLA_828, SERVO_DBSI, HLA_DBSI, SERVO_I_AC, VECTOR_I_AC, A_INF, S_INF, R_INF, B_INF, A_INF_840, S_INF_840, B_INF_840, S_INF_COMBI, A_INF_828, S_INF_828, B_INF_828, TM31, TM41, TM17, TM15, TM15DI_DO, TM120, TM150, TB30, ENC, ENC_840, CU_LINK | **P-Group:**Commands | **Version:**5207320 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the saved BO/CO parameters (signal source), which are located on drive objects
that are either not capable of operation or have been deactivated.

**Dependency:**
  
  
Refer to:
p9495, p9496, p9497, p9498  
Refer to:
A01318, A01507

**Note:**
  
A BICO interconnection (signal sink, signal source) is displayed in the same index
of p9498 and p9499.

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for binary quantity Q = I0 &amp; I1 &amp; I2 &amp; I3 of instance AND 2 of the
AND function block.

## SINAMICS Parameter TM41 (Terminal Module) 20040 - 20140

SINAMICS Parameter TM41 (Terminal Module) 20040 - 20140

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for binary quantity Q of instance XOR 0 of the XOR function block.

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter for output pulse Q of instance MFP 0 of the pulse generator.

## SINAMICS Parameter TM41 (Terminal Module) 20141 - 20241

SINAMICS Parameter TM41 (Terminal Module) 20141 - 20241

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for pulse delay time T in milliseconds of instance PDE 1 of the
closing delay device.

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Display parameter of instance LIM 1 of limiter QL (lower limit reached), i.e. QL =
1 for X &lt;= LL.

## SINAMICS Parameter TM41 (Terminal Module) 20242 - 21046

SINAMICS Parameter TM41 (Terminal Module) 20242 - 21046

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the run sequence of instance INT 0 within the runtime group
set in p20264.

**Note:**
  
The function blocks with a lower run sequence value are calculated before function
blocks with a higher run sequence value.

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

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
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Setting parameter for the run sequence of instance DIF 0 within the runtime group
set in p20287.

**Note:**
  
The function blocks with a lower run sequence value are calculated before function
blocks with a higher run sequence value.

### p21000[0...9] Runtime group properties

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**DCC | **P-Group:**- | **Version:**5201400 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 4004 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Allocates properties to runtime groups 1 to 10.  
This property comprises the sampling time and, for p21000[x] &gt;= 2000, the instant
of the call within the sampling time.  
The index x + 1 of p21000 corresponds to the number of the runtime group:  
- p21000[0] is used to set the property of the runtime group 1  
...  
- p21000[9] is used to set the property of the runtime group 10

**Recommend.:**
  
On the drive objects of CU, TB30, TM15DI_DO, TM31, TM41, TM120, the sampling time
for supplementary functions is preset to p0115[0] = 4 ms. If you wish to configure
a DCC runtime group with a shorter sampling time on these drive objects, then you
should first set the sampling time for supplementary functions p0115[0] on this drive
object to the value of the shortest sampling time required.

**Value:**
  
0:
Do not calculate runtime group  
1:
T = 1 * r21002  
2:
T = 2 * r21002  
3:
T = 3 * r21002  
4:
T = 4 * r21002  
5:
T = 5 * r21002  
6:
T = 6 * r21002  
7:
T = 7 * r21002  
8:
T = 8 * r21002  
9:
T = 9 * r21002  
10:
T = 10 * r21002  
11:
T = 11 * r21002  
12:
T = 12 * r21002  
13:
T = 13 * r21002  
14:
T = 14 * r21002  
15:
T = 15 * r21002  
16:
T = 16 * r21002  
17:
T = 17 * r21002  
18:
T = 18 * r21002  
19:
T = 19 * r21002  
20:
T = 20 * r21002  
21:
T = 21 * r21002  
22:
T = 22 * r21002  
23:
T = 23 * r21002  
24:
T = 24 * r21002  
25:
T = 25 * r21002  
26:
T = 26 * r21002  
27:
T = 27 * r21002  
28:
T = 28 * r21002  
29:
T = 29 * r21002  
30:
T = 30 * r21002  
31:
T = 31 * r21002  
32:
T = 32 * r21002  
33:
T = 33 * r21002  
34:
T = 34 * r21002  
35:
T = 35 * r21002  
36:
T = 36 * r21002  
37:
T = 37 * r21002  
38:
T = 38 * r21002  
39:
T = 39 * r21002  
40:
T = 40 * r21002  
41:
T = 41 * r21002  
42:
T = 42 * r21002  
43:
T = 43 * r21002  
44:
T = 44 * r21002  
45:
T = 45 * r21002  
46:
T = 46 * r21002  
47:
T = 47 * r21002  
48:
T = 48 * r21002  
49:
T = 49 * r21002  
50:
T = 50 * r21002  
51:
T = 51 * r21002  
52:
T = 52 * r21002  
53:
T = 53 * r21002  
54:
T = 54 * r21002  
55:
T = 55 * r21002  
56:
T = 56 * r21002  
57:
T = 57 * r21002  
58:
T = 58 * r21002  
59:
T = 59 * r21002  
60:
T = 60 * r21002  
61:
T = 61 * r21002  
62:
T = 62 * r21002  
63:
T = 63 * r21002  
64:
T = 64 * r21002  
65:
T = 65 * r21002  
66:
T = 66 * r21002  
67:
T = 67 * r21002  
68:
T = 68 * r21002  
69:
T = 69 * r21002  
70:
T = 70 * r21002  
71:
T = 71 * r21002  
72:
T = 72 * r21002  
73:
T = 73 * r21002  
74:
T = 74 * r21002  
75:
T = 75 * r21002  
76:
T = 76 * r21002  
77:
T = 77 * r21002  
78:
T = 78 * r21002  
79:
T = 79 * r21002  
80:
T = 80 * r21002  
81:
T = 81 * r21002  
82:
T = 82 * r21002  
83:
T = 83 * r21002  
84:
T = 84 * r21002  
85:
T = 85 * r21002  
86:
T = 86 * r21002  
87:
T = 87 * r21002  
88:
T = 88 * r21002  
89:
T = 89 * r21002  
90:
T = 90 * r21002  
91:
T = 91 * r21002  
92:
T = 92 * r21002  
93:
T = 93 * r21002  
94:
T = 94 * r21002  
95:
T = 95 * r21002  
96:
T = 96 * r21002  
97:
T = 97 * r21002  
98:
T = 98 * r21002  
99:
T = 99 * r21002  
100:
T = 100 * r21002  
101:
T = 101 * r21002  
102:
T = 102 * r21002  
103:
T = 103 * r21002  
104:
T = 104 * r21002  
105:
T = 105 * r21002  
106:
T = 106 * r21002  
107:
T = 107 * r21002  
108:
T = 108 * r21002  
109:
T = 109 * r21002  
110:
T = 110 * r21002  
111:
T = 111 * r21002  
112:
T = 112 * r21002  
113:
T = 113 * r21002  
114:
T = 114 * r21002  
115:
T = 115 * r21002  
116:
T = 116 * r21002  
117:
T = 117 * r21002  
118:
T = 118 * r21002  
119:
T = 119 * r21002  
120:
T = 120 * r21002  
121:
T = 121 * r21002  
122:
T = 122 * r21002  
123:
T = 123 * r21002  
124:
T = 124 * r21002  
125:
T = 125 * r21002  
126:
T = 126 * r21002  
127:
T = 127 * r21002  
128:
T = 128 * r21002  
129:
T = 129 * r21002  
130:
T = 130 * r21002  
131:
T = 131 * r21002  
132:
T = 132 * r21002  
133:
T = 133 * r21002  
134:
T = 134 * r21002  
135:
T = 135 * r21002  
136:
T = 136 * r21002  
137:
T = 137 * r21002  
138:
T = 138 * r21002  
139:
T = 139 * r21002  
140:
T = 140 * r21002  
141:
T = 141 * r21002  
142:
T = 142 * r21002  
143:
T = 143 * r21002  
144:
T = 144 * r21002  
145:
T = 145 * r21002  
146:
T = 146 * r21002  
147:
T = 147 * r21002  
148:
T = 148 * r21002  
149:
T = 149 * r21002  
150:
T = 150 * r21002  
151:
T = 151 * r21002  
152:
T = 152 * r21002  
153:
T = 153 * r21002  
154:
T = 154 * r21002  
155:
T = 155 * r21002  
156:
T = 156 * r21002  
157:
T = 157 * r21002  
158:
T = 158 * r21002  
159:
T = 159 * r21002  
160:
T = 160 * r21002  
161:
T = 161 * r21002  
162:
T = 162 * r21002  
163:
T = 163 * r21002  
164:
T = 164 * r21002  
165:
T = 165 * r21002  
166:
T = 166 * r21002  
167:
T = 167 * r21002  
168:
T = 168 * r21002  
169:
T = 169 * r21002  
170:
T = 170 * r21002  
171:
T = 171 * r21002  
172:
T = 172 * r21002  
173:
T = 173 * r21002  
174:
T = 174 * r21002  
175:
T = 175 * r21002  
176:
T = 176 * r21002  
177:
T = 177 * r21002  
178:
T = 178 * r21002  
179:
T = 179 * r21002  
180:
T = 180 * r21002  
181:
T = 181 * r21002  
182:
T = 182 * r21002  
183:
T = 183 * r21002  
184:
T = 184 * r21002  
185:
T = 185 * r21002  
186:
T = 186 * r21002  
187:
T = 187 * r21002  
188:
T = 188 * r21002  
189:
T = 189 * r21002  
190:
T = 190 * r21002  
191:
T = 191 * r21002  
192:
T = 192 * r21002  
193:
T = 193 * r21002  
194:
T = 194 * r21002  
195:
T = 195 * r21002  
196:
T = 196 * r21002  
197:
T = 197 * r21002  
198:
T = 198 * r21002  
199:
T = 199 * r21002  
200:
T = 200 * r21002  
201:
T = 201 * r21002  
202:
T = 202 * r21002  
203:
T = 203 * r21002  
204:
T = 204 * r21002  
205:
T = 205 * r21002  
206:
T = 206 * r21002  
207:
T = 207 * r21002  
208:
T = 208 * r21002  
209:
T = 209 * r21002  
210:
T = 210 * r21002  
211:
T = 211 * r21002  
212:
T = 212 * r21002  
213:
T = 213 * r21002  
214:
T = 214 * r21002  
215:
T = 215 * r21002  
216:
T = 216 * r21002  
217:
T = 217 * r21002  
218:
T = 218 * r21002  
219:
T = 219 * r21002  
220:
T = 220 * r21002  
221:
T = 221 * r21002  
222:
T = 222 * r21002  
223:
T = 223 * r21002  
224:
T = 224 * r21002  
225:
T = 225 * r21002  
226:
T = 226 * r21002  
227:
T = 227 * r21002  
228:
T = 228 * r21002  
229:
T = 229 * r21002  
230:
T = 230 * r21002  
231:
T = 231 * r21002  
232:
T = 232 * r21002  
233:
T = 233 * r21002  
234:
T = 234 * r21002  
235:
T = 235 * r21002  
236:
T = 236 * r21002  
237:
T = 237 * r21002  
238:
T = 238 * r21002  
239:
T = 239 * r21002  
240:
T = 240 * r21002  
241:
T = 241 * r21002  
242:
T = 242 * r21002  
243:
T = 243 * r21002  
244:
T = 244 * r21002  
245:
T = 245 * r21002  
246:
T = 246 * r21002  
247:
T = 247 * r21002  
248:
T = 248 * r21002  
249:
T = 249 * r21002  
250:
T = 250 * r21002  
251:
T = 251 * r21002  
252:
T = 252 * r21002  
253:
T = 253 * r21002  
254:
T = 254 * r21002  
255:
T = 255 * r21002  
256:
T = 256 * r21002  
1001:
T = 1 * r21003  
1002:
T = 2 * r21003  
1003:
T = 3 * r21003  
1004:
T = 4 * r21003  
1005:
T = 5 * r21003  
1006:
T = 6 * r21003  
1008:
T = 8 * r21003  
1010:
T = 10 * r21003  
1012:
T = 12 * r21003  
1016:
T = 16 * r21003  
1020:
T = 20 * r21003  
1024:
T = 24 * r21003  
1032:
T = 32 * r21003  
1040:
T = 40 * r21003  
1048:
T = 48 * r21003  
1064:
T = 64 * r21003  
1080:
T = 80 * r21003  
1096:
T = 96 * r21003  
2000:
Read-in AFTER digital inputs  
2001:
Output BEFORE digital outputs  
2002:
Read-in AFTER analog inputs  
4000:
Receive AFTER IF1 PROFIdrive PZD  
4001:
Send BEFORE IF1 PROFIdrive PZD  
4004:
Receive AFTER IF1 PROFIdrive flexible PZD

**Index:**
  
[
0]:
Runtime group 1  
[
1]:
Runtime group 2  
[
2]:
Runtime group 3  
[
3]:
Runtime group 4  
[
4]:
Runtime group 5  
[
5]:
Runtime group 6  
[
6]:
Runtime group 7  
[
7]:
Runtime group 8  
[
8]:
Runtime group 9  
[
9]:
Runtime group 10

**Dependency:**
  
See also: r7903, r21008

**Caution:**
  
The properties of the runtime groups must not be changed during operation as this
could result in discontinuous signal transitions.

**Note:**
  
For value = 1 ... 256 (free runtime group):  
This selection value can only be selected online if the following applies for sampling
time T_sample of this runtime group:  
1 ms &lt;= T_sample &lt; r21003.  
At download, a value that violates this condition is not rejected, but a permissible
equivalent value is set automatically and fault F51004 is output.  
For value &gt; 2000 (fixed runtime group):  
The fixed runtime groups p21000[x] &gt;= 2000 log on with the sampling time of the associated
basic system function, subject to a minimum sampling time of 1 ms. If, as a result
of this limit, the actual sampling time deviates from the sampling time of the basic
system function, then fault F51005 (during F51006 download) is output. In this case,
another runtime group with a sampling time &gt;= 1 ms should be selected. When selecting
the fixed runtime groups, a check is not made as to whether the associated system
block exists.  
Example:  
"BEFORE speed setpoint channel" means before function charts 3010, 3020, 3030, 3040,
etc. are calculated, if the setpoint channel is activated. If, e.g. for SERVO, a setpoint
channel has not been configured (p0108.8 = 0), the calculation is made before function
chart 3095.

### r21001[0...9] Runtime group sampling time

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**All objects | **P-Group:**- | **Version:**5201400 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [ms] | - [ms] | [ ] - [ms] |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the current sampling time of the runtime groups.

**Index:**
  
[
0]:
Runtime group 1  
[
1]:
Runtime group 2  
[
2]:
Runtime group 3  
[
3]:
Runtime group 4  
[
4]:
Runtime group 5  
[
5]:
Runtime group 6  
[
6]:
Runtime group 7  
[
7]:
Runtime group 8  
[
8]:
Runtime group 9  
[
9]:
Runtime group 10

### r21002 Basis sampling time, hardware

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**All objects | **P-Group:**- | **Version:**5201400 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [ms] | - [ms] | [ ] - [ms] |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the basis sampling time effective at this drive object for values 1 to 256
of p21000.  
Sampling time T = p21000 * r21002

### r21003 Basis sampling time, software

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**1 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**All objects | **P-Group:**- | **Version:**5201400 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [ms] | - [ms] | [ ] - [ms] |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
2.6

**Description:**
  
Displays the basis sampling time effective at this drive object for p21000 = 1002
to 1096 as factor.  
Sampling time T = (p21000 - 1000) * r21003

**Dependency:**
  
Ensure that the basis sampling time on the SIMOTION D410 for the software time slices
is always the same as the configured PROFIBUS/PROFINET clock cycle.

### r21005[0...9] Computing time load of the runtime group

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**All objects | **P-Group:**- | **Version:**5201400 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [%] | - [%] | [ ] - [%] |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.4

**Description:**
  
Share of the computing time load with which the DCC runtime group contributes to the
utilization of the sampling time during which it is called.

**Index:**
  
[
0]:
Runtime group 1  
[
1]:
Runtime group 2  
[
2]:
Runtime group 3  
[
3]:
Runtime group 4  
[
4]:
Runtime group 5  
[
5]:
Runtime group 6  
[
6]:
Runtime group 7  
[
7]:
Runtime group 8  
[
8]:
Runtime group 9  
[
9]:
Runtime group 10

**Note:**
  
The computing time load can only be displayed for the runtime groups which are logged
on (p21000[x] &gt; 0). The value for the computing time load is calculated in the drive
unit based on the project loaded plus DCC chart. Therefore, the values r21005[x] are
not available in the offline mode of the SCOUT/STARTER.  
  
In r21005 the computing time load is displayed, with which the DCC runtime group utilizes
the sampling time in which it is called. The runtime groups "Receive AFTER IF1 PROFIdrive
PZD" (p21000 = 4000), "Send BEFORE IF1 PROFIdrive PZD" (p21000 = 4001), "Receive BEFORE
IF2 PZD" (p21000 = 4002) and "Send BEFORE IF2 PZD" (p21000 = 4003) are called in the
isochronous mode and in the non-isochronous mode, in different sampling times.  
In the non-isochronous mode, these are IF1 / IF2 PZD sampling time (p2048 for p21000
= 4000 or 4001, p8848 for p21000 = 4002 or 4003). In the isochronous mode, this is
the current controller sampling time (p115[0]) which is periodically called with the
isochronous bus cycle time. The computing time load displayed in r21005 is always
calculated for the (more unfavorable) case of isochronous operation. This is why this
value does not (always) act to the full amount on the computing time load of the complete
system.

### r21008[0...31] Hardware sampling times available

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**All objects | **P-Group:**- | **Version:**5201400 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [ms] | - [ms] | [ ] - [ms] |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
5.1

**Description:**
  
Displays the assignment of the available hardware sampling times of the drive unit.  
The designated sampling times are those created as a multiple of the hardware basis
sampling time (r21002) and which are always &lt; r21003.

**Index:**
  
[
0]:
Hardware 1  
[
1]:
Hardware 2  
[
2]:
Hardware 3  
[
3]:
Hardware 4  
[
4]:
Hardware 5  
[
5]:
Hardware 6  
[
6]:
Hardware 7  
[
7]:
Hardware 8  
[
8]:
Hardware 9  
[
9]:
Hardware 10  
[
10]:
Hardware 11  
[
11]:
Hardware 12  
[
12]:
Hardware 13  
[
13]:
Hardware 14  
[
14]:
Hardware 15  
[
15]:
Hardware 16  
[
16]:
Hardware 17  
[
17]:
Hardware 18  
[
18]:
Hardware 19  
[
19]:
Hardware 20  
[
20]:
Hardware 21  
[
21]:
Hardware 22  
[
22]:
Hardware 23  
[
23]:
Hardware 24  
[
24]:
Hardware 25  
[
25]:
Hardware 26  
[
26]:
Hardware 27  
[
27]:
Hardware 28  
[
28]:
Hardware 29  
[
29]:
Hardware 30  
[
30]:
Hardware 31  
[
31]:
Hardware 32

**Dependency:**
  
See also: r7903, p21000  
  
Refer to:
F51001

**Notice:**
  
For internal purposes, the drive unit always requires several free hardware sampling
times. Therefore the current number of free hardware sampling times can be read out
in r7903.  
If r7903=0, no additional sampling time different from r21008[0...31] may be provided
from the Control Unit. When selecting in this state, if a runtime group with a sampling
time &lt; r21003 (p21000 &lt;= 255) is selected in p21000, only runtime groups whose sampling
time is already provided in r21008[0...31] may be selected.

**Note:**
  
A sampling time that is provided can be simultaneously used by system functions, several
FBLOCK runtime groups and several DCC runtime groups.  
The sampling time of runtime groups that have been assigned to the PROFIBUS runtime
groups (p21000 = 4000 ... 4004) is not displayed in r21008. For this sampling time,
one of the internally and permanently assigned hardware sampling times is used.  
If the value of r21008[x] != 0 (not equal to 0), then the sampling time is specified
in ms.  
If the value of r21008[x] = 0, this sampling time can still be freely assigned. It
should be noted that the basic system requires several freely assignable hardware
sampling times for internal functions. The number of hardware sampling times that
can still be freely assigned can be read out in r7903.  
If the value r21008[x] = 99999.00000, this hardware sampling time is not supported.

### p21030 Runtime group, computing time measurement

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**4 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**All objects | **P-Group:**- | **Version:**5201400 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 65535 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.4

**Description:**
  
Only for internal Siemens service purposes.

**Dependency:**
  
  
Refer to:
p21032, r21035, r21036, r21037

### p21031 Computing time measurement, blocks

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**4 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**All objects | **P-Group:**- | **Version:**5201400 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 4294967295 | [ 0 ] 0 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.6

**Description:**
  
Only for internal Siemens service purposes.

### p21032 Computing time measurement, duration

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**4 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**All objects | **P-Group:**- | **Version:**5201400 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 60 [s] | 10000 [s] | [ 0 ] 60 [s] |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.4

**Description:**
  
Only for internal Siemens service purposes.

**Dependency:**
  
  
Refer to:
p21030, r21035, r21036, r21037

### p21033 Computing time measurement, number of individual measurements

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**4 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**All objects | **P-Group:**- | **Version:**5201400 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 1 | 4294967295 | [ 0 ] 10000 |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.6

**Description:**
  
Setting for the number of calls during the measurement of the individual blocks.

**Dependency:**
  
  
Refer to:
p21031

### r21035[0...9] Computing time, minimum value

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**4 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**All objects | **P-Group:**- | **Version:**5201400 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [µs] | - [µs] | [ ] - [µs] |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.4

**Description:**
  
Only for internal Siemens service purposes.

**Index:**
  
[
0]:
Runtime group 1  
[
1]:
Runtime group 2  
[
2]:
Runtime group 3  
[
3]:
Runtime group 4  
[
4]:
Runtime group 5  
[
5]:
Runtime group 6  
[
6]:
Runtime group 7  
[
7]:
Runtime group 8  
[
8]:
Runtime group 9  
[
9]:
Runtime group 10

**Dependency:**
  
  
Refer to:
p21030, p21032, r21036, r21037

### r21036[0...9] Computing time, mean value

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**4 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**All objects | **P-Group:**- | **Version:**5201400 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [µs] | - [µs] | [ ] - [µs] |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.4

**Description:**
  
Only for internal Siemens service purposes.

**Index:**
  
[
0]:
Runtime group 1  
[
1]:
Runtime group 2  
[
2]:
Runtime group 3  
[
3]:
Runtime group 4  
[
4]:
Runtime group 5  
[
5]:
Runtime group 6  
[
6]:
Runtime group 7  
[
7]:
Runtime group 8  
[
8]:
Runtime group 9  
[
9]:
Runtime group 10

### r21037[0...9] Computing time, maximum value

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**4 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**All objects | **P-Group:**- | **Version:**5201400 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [µs] | - [µs] | [ ] - [µs] |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.4

**Description:**
  
Only for internal Siemens service purposes.

**Index:**
  
[
0]:
Runtime group 1  
[
1]:
Runtime group 2  
[
2]:
Runtime group 3  
[
3]:
Runtime group 4  
[
4]:
Runtime group 5  
[
5]:
Runtime group 6  
[
6]:
Runtime group 7  
[
7]:
Runtime group 8  
[
8]:
Runtime group 9  
[
9]:
Runtime group 10

**Dependency:**
  
  
Refer to:
p21030, p21032, r21035, r21036

### r21041[0...49] Block ID of the measured block

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**4 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**All objects | **P-Group:**- | **Version:**5201400 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.6

**Description:**
  
Block ID of the measured block (block runtime measurement via parameter p21031. The
blocks are measured in the same sequence as they have been programmed in the execution
sequence.  
The parameter is designed for the measurement of 50 block instances

**Index:**
  
[
0]:
Block 1  
[
1]:
Block 2  
[
2]:
Block 3  
[
3]:
Block 4  
[
4]:
Block 5  
[
5]:
Block 6  
[
6]:
Block 7  
[
7]:
Block 8  
[
8]:
Block 9  
[
9]:
Block 10  
[
10]:
Block 11  
[
11]:
Block 12  
[
12]:
Block 13  
[
13]:
Block 14  
[
14]:
Block 15  
[
15]:
Block 16  
[
16]:
Block 17  
[
17]:
Block 18  
[
18]:
Block 19  
[
19]:
Block 20  
[
20]:
Block 21  
[
21]:
Block 22  
[
22]:
Block 23  
[
23]:
Block 24  
[
24]:
Block 25  
[
25]:
Block 26  
[
26]:
Block 27  
[
27]:
Block 28  
[
28]:
Block 29  
[
29]:
Block 30  
[
30]:
Block 31  
[
31]:
Block 32  
[
32]:
Block 33  
[
33]:
Block 34  
[
34]:
Block 35  
[
35]:
Block 36  
[
36]:
Block 37  
[
37]:
Block 38  
[
38]:
Block 39  
[
39]:
Block 40  
[
40]:
Block 41  
[
41]:
Block 42  
[
42]:
Block 43  
[
43]:
Block 44  
[
44]:
Block 45  
[
45]:
Block 46  
[
46]:
Block 47  
[
47]:
Block 48  
[
48]:
Block 49  
[
49]:
Block 50

### r21042[0...49] First run / subsequent run identifiers

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**4 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**All objects | **P-Group:**- | **Version:**5201400 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.6

**Description:**
  
In the block runtime measurements, the block runtimes are measured. R21039 indicates
whether the measurement is the first or a subsequent call.  
If the block type occurs only once in the runtime group, only the measured value for
the first run will be supplied.  
The parameter is designed for the measurement of 50 block instances

**Index:**
  
[
0]:
Block 1  
[
1]:
Block 2  
[
2]:
Block 3  
[
3]:
Block 4  
[
4]:
Block 5  
[
5]:
Block 6  
[
6]:
Block 7  
[
7]:
Block 8  
[
8]:
Block 9  
[
9]:
Block 10  
[
10]:
Block 11  
[
11]:
Block 12  
[
12]:
Block 13  
[
13]:
Block 14  
[
14]:
Block 15  
[
15]:
Block 16  
[
16]:
Block 17  
[
17]:
Block 18  
[
18]:
Block 19  
[
19]:
Block 20  
[
20]:
Block 21  
[
21]:
Block 22  
[
22]:
Block 23  
[
23]:
Block 24  
[
24]:
Block 25  
[
25]:
Block 26  
[
26]:
Block 27  
[
27]:
Block 28  
[
28]:
Block 29  
[
29]:
Block 30  
[
30]:
Block 31  
[
31]:
Block 32  
[
32]:
Block 33  
[
33]:
Block 34  
[
34]:
Block 35  
[
35]:
Block 36  
[
36]:
Block 37  
[
37]:
Block 38  
[
38]:
Block 39  
[
39]:
Block 40  
[
40]:
Block 41  
[
41]:
Block 42  
[
42]:
Block 43  
[
43]:
Block 44  
[
44]:
Block 45  
[
45]:
Block 46  
[
46]:
Block 47  
[
47]:
Block 48  
[
48]:
Block 49  
[
49]:
Block 50

### r21043[0...49] Minimum measured block runtime in us

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**4 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**All objects | **P-Group:**- | **Version:**5201400 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [µs] | - [µs] | [ ] - [µs] |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.6

**Description:**
  
Minimum measured runtime of the measured block (block runtime measurement via parameter
p21031. The blocks are measured in the same sequence as they have been programmed
in the execution sequence.  
The parameter is designed for the measurement of 50 block instances

**Index:**
  
[
0]:
Block 1  
[
1]:
Block 2  
[
2]:
Block 3  
[
3]:
Block 4  
[
4]:
Block 5  
[
5]:
Block 6  
[
6]:
Block 7  
[
7]:
Block 8  
[
8]:
Block 9  
[
9]:
Block 10  
[
10]:
Block 11  
[
11]:
Block 12  
[
12]:
Block 13  
[
13]:
Block 14  
[
14]:
Block 15  
[
15]:
Block 16  
[
16]:
Block 17  
[
17]:
Block 18  
[
18]:
Block 19  
[
19]:
Block 20  
[
20]:
Block 21  
[
21]:
Block 22  
[
22]:
Block 23  
[
23]:
Block 24  
[
24]:
Block 25  
[
25]:
Block 26  
[
26]:
Block 27  
[
27]:
Block 28  
[
28]:
Block 29  
[
29]:
Block 30  
[
30]:
Block 31  
[
31]:
Block 32  
[
32]:
Block 33  
[
33]:
Block 34  
[
34]:
Block 35  
[
35]:
Block 36  
[
36]:
Block 37  
[
37]:
Block 38  
[
38]:
Block 39  
[
39]:
Block 40  
[
40]:
Block 41  
[
41]:
Block 42  
[
42]:
Block 43  
[
43]:
Block 44  
[
44]:
Block 45  
[
45]:
Block 46  
[
46]:
Block 47  
[
47]:
Block 48  
[
48]:
Block 49  
[
49]:
Block 50

### r21044[0...49] Average measured block runtime in us

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**4 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**All objects | **P-Group:**- | **Version:**5201400 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [µs] | - [µs] | [ ] - [µs] |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.6

**Description:**
  
Average measured runtime of the measured block (block runtime measurement via parameter
p21031. The blocks are measured in the same sequence as they have been programmed
in the execution sequence.  
The parameter is designed for the measurement of 50 block instances

**Index:**
  
[
0]:
Block 1  
[
1]:
Block 2  
[
2]:
Block 3  
[
3]:
Block 4  
[
4]:
Block 5  
[
5]:
Block 6  
[
6]:
Block 7  
[
7]:
Block 8  
[
8]:
Block 9  
[
9]:
Block 10  
[
10]:
Block 11  
[
11]:
Block 12  
[
12]:
Block 13  
[
13]:
Block 14  
[
14]:
Block 15  
[
15]:
Block 16  
[
16]:
Block 17  
[
17]:
Block 18  
[
18]:
Block 19  
[
19]:
Block 20  
[
20]:
Block 21  
[
21]:
Block 22  
[
22]:
Block 23  
[
23]:
Block 24  
[
24]:
Block 25  
[
25]:
Block 26  
[
26]:
Block 27  
[
27]:
Block 28  
[
28]:
Block 29  
[
29]:
Block 30  
[
30]:
Block 31  
[
31]:
Block 32  
[
32]:
Block 33  
[
33]:
Block 34  
[
34]:
Block 35  
[
35]:
Block 36  
[
36]:
Block 37  
[
37]:
Block 38  
[
38]:
Block 39  
[
39]:
Block 40  
[
40]:
Block 41  
[
41]:
Block 42  
[
42]:
Block 43  
[
43]:
Block 44  
[
44]:
Block 45  
[
45]:
Block 46  
[
46]:
Block 47  
[
47]:
Block 48  
[
48]:
Block 49  
[
49]:
Block 50

### r21045[0...49] Maximum measured block runtime in us

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**4 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**All objects | **P-Group:**- | **Version:**5201400 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [µs] | - [µs] | [ ] - [µs] |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.6

**Description:**
  
Average measured runtime of the measured block (block runtime measurement via parameter
p21031. The blocks are measured in the same sequence as they have been programmed
in the execution sequence.  
The parameter is designed for the measurement of 50 block instances

**Index:**
  
[
0]:
Block 1  
[
1]:
Block 2  
[
2]:
Block 3  
[
3]:
Block 4  
[
4]:
Block 5  
[
5]:
Block 6  
[
6]:
Block 7  
[
7]:
Block 8  
[
8]:
Block 9  
[
9]:
Block 10  
[
10]:
Block 11  
[
11]:
Block 12  
[
12]:
Block 13  
[
13]:
Block 14  
[
14]:
Block 15  
[
15]:
Block 16  
[
16]:
Block 17  
[
17]:
Block 18  
[
18]:
Block 19  
[
19]:
Block 20  
[
20]:
Block 21  
[
21]:
Block 22  
[
22]:
Block 23  
[
23]:
Block 24  
[
24]:
Block 25  
[
25]:
Block 26  
[
26]:
Block 27  
[
27]:
Block 28  
[
28]:
Block 29  
[
29]:
Block 30  
[
30]:
Block 31  
[
31]:
Block 32  
[
32]:
Block 33  
[
33]:
Block 34  
[
34]:
Block 35  
[
35]:
Block 36  
[
36]:
Block 37  
[
37]:
Block 38  
[
38]:
Block 39  
[
39]:
Block 40  
[
40]:
Block 41  
[
41]:
Block 42  
[
42]:
Block 43  
[
43]:
Block 44  
[
44]:
Block 45  
[
45]:
Block 46  
[
46]:
Block 47  
[
47]:
Block 48  
[
48]:
Block 49  
[
49]:
Block 50

### r21046[0...49] Library IDs of the measured blocks

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**4 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**All objects | **P-Group:**- | **Version:**5201400 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](SINAMICS%20Alarms%20TM41%20%28Terminal%20Module%29.md#sinamics-alarms-tm41-terminal-module) |  |  |

**Valid as of version:**
  
4.6

**Description:**
  
Library ID of the measured block (block runtime measurement via parameter p21031).  
Measurements with blocks from different libraries can thereby be carried out in one
runtime group.  
The blocks are measured in the same sequence as they have been programmed in the execution
sequence.  
The parameter is designed for the measurement of 50 block instances  
Indices 0..49

**Index:**
  
[
0]:
Block 1  
[
1]:
Block 2  
[
2]:
Block 3  
[
3]:
Block 4  
[
4]:
Block 5  
[
5]:
Block 6  
[
6]:
Block 7  
[
7]:
Block 8  
[
8]:
Block 9  
[
9]:
Block 10  
[
10]:
Block 11  
[
11]:
Block 12  
[
12]:
Block 13  
[
13]:
Block 14  
[
14]:
Block 15  
[
15]:
Block 16  
[
16]:
Block 17  
[
17]:
Block 18  
[
18]:
Block 19  
[
19]:
Block 20  
[
20]:
Block 21  
[
21]:
Block 22  
[
22]:
Block 23  
[
23]:
Block 24  
[
24]:
Block 25  
[
25]:
Block 26  
[
26]:
Block 27  
[
27]:
Block 28  
[
28]:
Block 29  
[
29]:
Block 30  
[
30]:
Block 31  
[
31]:
Block 32  
[
32]:
Block 33  
[
33]:
Block 34  
[
34]:
Block 35  
[
35]:
Block 36  
[
36]:
Block 37  
[
37]:
Block 38  
[
38]:
Block 39  
[
39]:
Block 40  
[
40]:
Block 41  
[
41]:
Block 42  
[
42]:
Block 43  
[
43]:
Block 44  
[
44]:
Block 45  
[
45]:
Block 46  
[
46]:
Block 47  
[
47]:
Block 48  
[
48]:
Block 49  
[
49]:
Block 50

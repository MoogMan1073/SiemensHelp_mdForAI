---
title: "Technology Extension SETPGEN V1.30.11"
package: sdrpaSETPGEN_1_30_11enUS
topics: 18
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Technology Extension SETPGEN V1.30.11

This section contains the parameter descriptions for the Technology Extension.
In the table of contents, you will then see a separate entry for each parameter number.

## SINAMICS Parameter SETPGEN 31200 - 31224

SINAMICS Parameter SETPGEN 31200 - 31224

### p31200 SETPGEN sampling time

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C1( 3) | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7310 |
| **Object:**All objects | **P-Group:**Functions | **Version:**1300800 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 64 | [ 0 ] 1 |
| [Alarms](Technology%20Extension%20SETPGEN%20V1.30.11.md#technology-extension-setpgen-v13011) |  |  |

**Valid as of version:**
  
1.3

**Description:**
  
Sets the sampling time T for the setpoint generator.  
The sampling time must be set as a multiple of the current controller sampling time
(p0115[0]).

**Value:**
  
0:
Do not calculate  
1:
T = 1 * p0115[0]  
2:
T = 2 * p0115[0]  
4:
T = 4 * p0115[0]  
8:
T = 8 * p0115[0]  
16:
T = 16 * p0115[0]  
32:
T = 32 * p0115[0]  
64:
T = 64 * p0115[0]

**Note:**
  
SETPGEN: setpoint generator

### p31201 BI: SETPGEN enable

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 7310 |
| **Object:**All objects | **P-Group:**Functions | **Version:**1300800 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](Technology%20Extension%20SETPGEN%20V1.30.11.md#technology-extension-setpgen-v13011) |  |  |

**Valid as of version:**
  
1.3

**Description:**
  
Sets the signal source to enable the calculated values of the signal generators.  
p31201 = 0 signal:  
A value of 0 is output at connector output r31215[0...2]/r31220/r31222.  
p31201 = 1 signal:  
The calculated value is output at connector outputs r31215[0...2]/r31220/r31222.

**Note:**
  
For a synchronous behavior of the signal generators, the enable may have to be disabled
and reissued after re-parameterization of the frequency p31211.

### p31205 SETPGEN reference frequency

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7310 |
| **Object:**All objects | **P-Group:**Functions | **Version:**1300800 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| -340.28235E36 [Hz] | 340.28235E36 [Hz] | [ 0 ] 100.000000 [Hz] |
| [Alarms](Technology%20Extension%20SETPGEN%20V1.30.11.md#technology-extension-setpgen-v13011) |  |  |

**Valid as of version:**
  
1.3

**Description:**
  
Sets the reference frequency for the setpoint generator.  
The frequency setpoints of the three signal generators (CI: p31211[0...2] on a drive
object refer to this reference frequency.

**Dependency:**
  
  
Refer to:
p31211

**Note:**
  
Example:  
p31205 = 500 Hz  
--> 100 % corresponds to 500 Hz for the signal to be output.

### p31206 SETPGEN reference angle

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7310 |
| **Object:**All objects | **P-Group:**Functions | **Version:**1300800 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| -340.28235E36 [°] | 340.28235E36 [°] | [ 0 ] 360.000000 [°] |
| [Alarms](Technology%20Extension%20SETPGEN%20V1.30.11.md#technology-extension-setpgen-v13011) |  |  |

**Valid as of version:**
  
1.3

**Description:**
  
Sets the reference angle for the setpoint generator.  
The phase offset of the three signal generators (CI: p31213[0...2]) on a drive object
refer to this reference angle.

**Dependency:**
  
  
Refer to:
p31213

**Note:**
  
Example:  
p31206 = 360 °  
--> 100 % corresponds to a phase offset of 360 ° for the signal to be output.  
--> 50 % corresponds to a phase offset of 180 ° for the signal to be output.

### p31210[0...2] SETPGEN signal waveform

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7310 |
| **Object:**All objects | **P-Group:**Functions | **Version:**1300800 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 4 | [ 0 ] 1   [ 1 ] 0   [ 2 ] 0 |
| [Alarms](Technology%20Extension%20SETPGEN%20V1.30.11.md#technology-extension-setpgen-v13011) |  |  |

**Valid as of version:**
  
1.3

**Description:**
  
Sets the signal waveform for the individual signal generators.

**Value:**
  
0:
Signal generator deactivated  
1:
Sine wave  
2:
Square wave  
3:
50 % sawtooth  
4:
Sawtooth

**Index:**
  
[
0]:
Signal generator 0  
[
1]:
Signal generator 1  
[
2]:
Signal generator 2

### p31211[0...2] CI: SETPGEN signal waveform frequency

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7310 |
| **Object:**All objects | **P-Group:**Functions | **Version:**1300800 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**PERCENT | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](Technology%20Extension%20SETPGEN%20V1.30.11.md#technology-extension-setpgen-v13011) |  |  |

**Valid as of version:**
  
1.3

**Description:**
  
Sets the signal source for the frequency of the individual signal generators.  
This value refers to p31205.

**Recommend.:**
  
For a sinusoidal signal that can be used in practice, the frequency should be set
so that the period of the signal to be generated is always greater or equal to 10x
the sampling time (p31200).  
Example:  
For sampling time p31200 = 1 and p0115[0] = 125 µs, it follows:  
--> minimum period T = 1250 µs  
--> maximum frequency f = 1/T = 800 Hz  
--> for p31205 = 400 Hz, the signal source of p31211[0...2] may assume a maximum value
of 200 %.

**Index:**
  
[
0]:
Signal generator 0  
[
1]:
Signal generator 1  
[
2]:
Signal generator 2

**Dependency:**
  
  
Refer to:
p31201, p31205

**Note:**
  
The frequency is internally limited to half the sampling frequency.  
  
For a synchronous behavior of the signal generators, the enable p31201 may have to
be disabled and reissued after parameterization of the frequency.

### p31212[0...2] CI: SETPGEN signal waveform amplitude

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7310 |
| **Object:**All objects | **P-Group:**Functions | **Version:**1300800 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**PERCENT | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 1 |
| [Alarms](Technology%20Extension%20SETPGEN%20V1.30.11.md#technology-extension-setpgen-v13011) |  |  |

**Valid as of version:**
  
1.3

**Description:**
  
Sets the signal source for the amplitude of the individual signal generators.

**Index:**
  
[
0]:
Signal generator 0  
[
1]:
Signal generator 1  
[
2]:
Signal generator 2

**Note:**
  
For offset = 0 % (p31214[x] = 0), the signal is output between -p31212[x] and +p31212[x].

### p31213[0...2] CI: SETPGEN signal waveform phase offset

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7310 |
| **Object:**All objects | **P-Group:**Functions | **Version:**1300800 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**PERCENT | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](Technology%20Extension%20SETPGEN%20V1.30.11.md#technology-extension-setpgen-v13011) |  |  |

**Valid as of version:**
  
1.3

**Description:**
  
Sets the signal source for the phase offset of the individual signal generators.  
This value refers to p31206.

**Index:**
  
[
0]:
Signal generator 0  
[
1]:
Signal generator 1  
[
2]:
Signal generator 2

**Dependency:**
  
  
Refer to:
p31206

### p31214[0...2] CI: SETPGEN signal waveform offset

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7310 |
| **Object:**All objects | **P-Group:**Functions | **Version:**1300800 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**PERCENT | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](Technology%20Extension%20SETPGEN%20V1.30.11.md#technology-extension-setpgen-v13011) |  |  |

**Valid as of version:**
  
1.3

**Description:**
  
Sets the signal source for the offset of the individual signal generators.

**Index:**
  
[
0]:
Signal generator 0  
[
1]:
Signal generator 1  
[
2]:
Signal generator 2

### r31215[0...2] CO: SETPGEN signal waveform output

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7310 |
| **Object:**All objects | **P-Group:**Functions | **Version:**1300800 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**PERCENT | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [%] | - [%] | [ ] - [%] |
| [Alarms](Technology%20Extension%20SETPGEN%20V1.30.11.md#technology-extension-setpgen-v13011) |  |  |

**Valid as of version:**
  
1.3

**Description:**
  
Display and connector output for the output value of the individual signal generators.

**Index:**
  
[
0]:
Signal generator 0  
[
1]:
Signal generator 1  
[
2]:
Signal generator 2

### p31216[0...9] CO: SETPGEN fixed value [%]

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7310 |
| **Object:**All objects | **P-Group:**Functions | **Version:**1300800 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**PERCENT | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| -340.28235E36 [%] | 340.28235E36 [%] | [ 0 ] 0.000 [%] |
| [Alarms](Technology%20Extension%20SETPGEN%20V1.30.11.md#technology-extension-setpgen-v13011) |  |  |

**Valid as of version:**
  
1.3

**Description:**
  
Setting, display and connector output for fixed percentage values.  
These fixed values can be freely used in the drive system for BICO interconnections.

**Index:**
  
[
0]:
Value 0  
[
1]:
Value 1  
[
2]:
Value 2  
[
3]:
Value 3  
[
4]:
Value 4  
[
5]:
Value 5  
[
6]:
Value 6  
[
7]:
Value 7  
[
8]:
Value 8  
[
9]:
Value 9

**Note:**
  
Examples for BICO interconnections with the SETPGEN Technology Extension:  
CI: p31211[0] = p31216[0]  
CI: p31212[0] = p31216[1]  
CI: p31213[0] = p31216[2]  
CI: p31214[0] = p31216[3]

### r31220 CO: SETPGEN output total

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7310 |
| **Object:**All objects | **P-Group:**Functions | **Version:**1300800 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**PERCENT | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [%] | - [%] | [ ] - [%] |
| [Alarms](Technology%20Extension%20SETPGEN%20V1.30.11.md#technology-extension-setpgen-v13011) |  |  |

**Valid as of version:**
  
1.3

**Description:**
  
Display and connector output for the output value of the setpoint generator.  
The value is the sum of the output values of all three signal generators.

**Dependency:**
  
  
Refer to:
r31222

### p31221 SETPGEN output integer number scaling

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer32 | **Dynamic index:**- | **Func. diagram:** 7310 |
| **Object:**All objects | **P-Group:**Functions | **Version:**1300800 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| -2147483648 | 2147483647 | [ 0 ] 1 |
| [Alarms](Technology%20Extension%20SETPGEN%20V1.30.11.md#technology-extension-setpgen-v13011) |  |  |

**Valid as of version:**
  
1.3

**Description:**
  
Sets the scaling for the display of the output signal of the setpoint generator as
integer number.

**Dependency:**
  
  
Refer to:
r31220, r31222

### r31222 CO/BO: SETPGEN output total integer number

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer32 | **Dynamic index:**- | **Func. diagram:** 7310 |
| **Object:**All objects | **P-Group:**Functions | **Version:**1300800 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](Technology%20Extension%20SETPGEN%20V1.30.11.md#technology-extension-setpgen-v13011) |  |  |

**Valid as of version:**
  
1.3

**Description:**
  
Display and connector output for the output signal of the setpoint generator as integer
number.

**Dependency:**
  
  
Refer to:
r31220, p31221

**Note:**
  
r31222 = (r31220 / 100 %) * p31221

### p31223[0...2] SETPGEN signal waveform integer number scaling

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer32 | **Dynamic index:**- | **Func. diagram:** 7310 |
| **Object:**All objects | **P-Group:**- | **Version:**1300800 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| -2147483648 | 2147483647 | [ 0 ] 1 |
| [Alarms](Technology%20Extension%20SETPGEN%20V1.30.11.md#technology-extension-setpgen-v13011) |  |  |

**Valid as of version:**
  
1.3

**Description:**
  
Sets the scaling for the output value of the individual signal generators as integer
number.

**Index:**
  
[
0]:
Signal generator 0  
[
1]:
Signal generator 1  
[
2]:
Signal generator 2

**Dependency:**
  
  
Refer to:
r31215, r31224

### r31224[0...2] CO: SETPGEN signal waveform output integer number

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer32 | **Dynamic index:**- | **Func. diagram:** 7310 |
| **Object:**All objects | **P-Group:**Functions | **Version:**1300800 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](Technology%20Extension%20SETPGEN%20V1.30.11.md#technology-extension-setpgen-v13011) |  |  |

**Valid as of version:**
  
1.3

**Description:**
  
Display and connector output for the output signal of the individual signal generators
as integer number.

**Index:**
  
[
0]:
Signal generator 0  
[
1]:
Signal generator 1  
[
2]:
Signal generator 2

**Dependency:**
  
  
Refer to:
r31215, p31223

**Note:**
  
r31224[x] = (r31215[x] / 100 %) * p31223[x]

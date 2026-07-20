---
title: "Technology Extension POLYGON V1.10.13"
package: sdrpaPOLYGON_1_10_13enUS
topics: 20
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Technology Extension POLYGON V1.10.13

This section contains the parameter descriptions for the Technology Extension.
In the table of contents, you will then see a separate entry for each parameter number.

## SINAMICS Parameter POLYGON 31230 - 31251

SINAMICS Parameter POLYGON 31230 - 31251

### p31230 POLYGON sampling time

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C1( 3) | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7331 |
| **Object:**Alle Objekte | **P-Group:**Funktionen | **Version:**1101200 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 64 | [ 0 ] 1 |
| Alarms |  |  |

**Valid as of version:**
  
1.1

**Description:**
  
Sets the sampling time T for the OA application POLYGON.  
The sampling time must be set a multiple of the current controller sampling time (p0115[0]).

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
  
POLYGON: Polygonal line (characteristic functionality dependent on the master value)  
The characteristic is defined via the modulo length using equidistant interpolation
points. The characteristic is linearly interpolated between the interpolation points.  
Typical characteristics:  
Position-position-reference, position-speed-reference, position-torque-reference

### p31231 BI: POLYGON enable

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 7331 |
| **Object:**Alle Objekte | **P-Group:**Funktionen | **Version:**1101200 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| Alarms |  |  |

**Valid as of version:**
  
1.1

**Description:**
  
Sets the signal source to enable the calculated values.  
p31231 = 0 signal:  
A value of 0 is output at connector output r31249/r31251.  
p31231 = 1 signal:  
The calculated value is output at connector output r31249/r31251.

**Dependency:**
  
  
Refer to:
p31230

**Note:**
  
The characteristic is calculated depending on the sampling time setting in p31230.

### p31234 CI: POLYGON master value raw value

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Integer32 | **Dynamic index:**- | **Func. diagram:** 7331 |
| **Object:**Alle Objekte | **P-Group:**Funktionen | **Version:**1101200 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 479[0] |
| Alarms |  |  |

**Valid as of version:**
  
1.1

**Description:**
  
Sets the signal source for the master value.  
Typical BICO interconnections:  
- master value of a real axis  
CI: p31234 = r0479[0] (diagnostics encoder position value Gn_XIST1, encoder 1)  
- virtual master value based on OA SETPGEN  
CI: p31234 = r31222 (SETPGEN output complete integer number)  
- virtual master value based on EPOS  
CI: p31234 = r2665 (EPOS position setpoint)

**Note:**
  
EPOS: Basic positioner  
SETPGEN: Setpoint generator

### p31235 POLYGON master value scaling numerator

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer32 | **Dynamic index:**- | **Func. diagram:** 7331 |
| **Object:**Alle Objekte | **P-Group:**Funktionen | **Version:**1101200 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| -2147483648 | 2147483647 | [ 0 ] 1 |
| Alarms |  |  |

**Valid as of version:**
  
1.1

**Description:**
  
Sets the numerator to scale the master value.  
With p31235 and p31236, the master value of intrinsic units of the raw signal (e.g.
encoder increments) are converted into length or angular units that match the particular
application (e.g. millidegrees for rotational movement).  
Example of rotational movement:  
Master value p31234 = r0479[0] (default setting)  
p31235 = 360000 (numerical value for one revolution in millidegrees)  
p31236 = p0408[0] * 2^p0418[0] (numerical value for one revolution in encoder increments)  
In addition, gearbox ratios can also be taken into account.

**Dependency:**
  
  
Refer to:
p31234, p31236, p31244

**Note:**
  
LU: Length Unit  
The following should be observed:  
p31235 / p31236 &lt; p31244

### p31236 POLYGON master value scaling denominator

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer32 | **Dynamic index:**- | **Func. diagram:** 7331 |
| **Object:**Alle Objekte | **P-Group:**Funktionen | **Version:**1101200 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| -2147483648 | 2147483647 | [ 0 ] 1 |
| Alarms |  |  |

**Valid as of version:**
  
1.1

**Description:**
  
Sets the denominator to scale the master value.  
With p31235 and p31236, the master value of intrinsic units of the raw signal (e.g.
encoder increments) are converted into length or angular units that match the particular
application (e.g. millidegrees for rotational movement).  
Example of rotational movement:  
Master value p31234 = r0479[0] (default setting)  
p31235 = 360000 (numerical value for one revolution in millidegrees)  
p31236 = p0408[0] * 2^p0418[0] (numerical value for one revolution in encoder increments)  
In addition, gearbox ratios can also be taken into account.

**Dependency:**
  
  
Refer to:
p31234, p31235, p31244

**Note:**
  
LU: Length Unit  
The following should be observed:  
p31235 / p31236 &lt; p31244

### p31238 CI: POLYGON master value setting value

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Integer32 | **Dynamic index:**- | **Func. diagram:** 7331 |
| **Object:**Alle Objekte | **P-Group:**Funktionen | **Version:**1101200 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 31241[0] |
| Alarms |  |  |

**Valid as of version:**
  
1.1

**Description:**
  
Sets the signal source for the setting value of the master value.  
The setting value is used to reference the master value and is accepted for binector
input p31239 = 0/1 signal.  
The master value offset is entered in the length or angular unit selected by the user.
The corresponding numerical value is saved, for example in fixed value p31241[0...2].  
After being transferred, it is used as basis for future changes (using p31235/p31236)
to the scaled master value (master value after setting value = scaled master value
+ setting value - scaled master value for accepting the setting value).

**Dependency:**
  
  
Refer to:
p31239, p31241, r31242

**Note:**
  
The setting value is not scaled according to p31235/p31236.  
It acts directly on the active master value (r31242[0...1]) before the modulo correction.

### p31239 BI: POLYGON master value accept setting value

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 7331 |
| **Object:**Alle Objekte | **P-Group:**Funktionen | **Version:**1101200 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| Alarms |  |  |

**Valid as of version:**
  
1.1

**Description:**
  
Sets the signal source to accept the setting value for the master value (signal edge).  
BI: p31239 = 0/1 signal:  
The setting value available via connector input p31238 is accepted.  
BI: p31239 = 1/0 signal:  
No effect. The setting value remains valid.

**Dependency:**
  
  
Refer to:
p31238

### p31240 CI: POLYGON master value offset

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Integer32 | **Dynamic index:**- | **Func. diagram:** 7331 |
| **Object:**Alle Objekte | **P-Group:**Funktionen | **Version:**1101200 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| Alarms |  |  |

**Valid as of version:**
  
1.1

**Description:**
  
Sets the signal source for the dynamic offset of the master value.  
Examples:  
- phase offset.  
- for taking into account the phase response of subordinate control loops as a function
of the frequency.  
The master value offset is entered in the length or angular unit selected by the user.  
One of the fixed values p31241[0...2] can be used to statically enter the master value
offset.

**Dependency:**
  
  
Refer to:
r31242

**Note:**
  
It acts directly on the effective master value r31242[0].

### p31241[0...2] CO: POLYGON fixed value

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer32 | **Dynamic index:**- | **Func. diagram:** 7331 |
| **Object:**Alle Objekte | **P-Group:**Funktionen | **Version:**1101200 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| -2147483648 | 2147483647 | [ 0 ] 0 |
| Alarms |  |  |

**Valid as of version:**
  
1.1

**Description:**
  
Setting, display and connector output for the fixed values.

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

**Note:**
  
Typical BICO interconnections can be established for commissioning and testing:  
CI: p31234 = p31241[0...2]  
CI: p31238 = p31241[0...2] (factory setting: CI: p31238 = p31241[0])  
CI: p31240 = p31241[0...2]

### r31242[0...1] CO: POLYGON master value active

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer32 | **Dynamic index:**- | **Func. diagram:** 7331 |
| **Object:**Alle Objekte | **P-Group:**Funktionen | **Version:**1101200 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| Alarms |  |  |

**Valid as of version:**
  
1.1

**Description:**
  
Display and connector output for the active master value (x value).  
The value is based on the master value (p31234) and takes into account the selected
scaling (p31235, p31236), the setting value (p31238) and the offset (p31240).

**Index:**
  
[
0]:
Master value before offset  
[
1]:
Master value after offset

**Dependency:**
  
  
Refer to:
p31234, p31235, p31236, p31238, p31240

### p31244 POLYGON modulo length

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7331 |
| **Object:**Alle Objekte | **P-Group:**Funktionen | **Version:**1101200 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 1 | 7200000 | [ 0 ] 360000 |
| Alarms |  |  |

**Valid as of version:**
  
1.1

**Description:**
  
Setting the modulo length.  
The characteristic is periodically repeated depending on the modulo length.  
Example:  
p31244 = 360000 (master value, which corresponds to one mechanical revolution)  
In this case, the active master value has a value range from 0 to 359999.

**Dependency:**
  
  
Refer to:
p31235, p31236

**Note:**
  
The following should be observed:  
p31235 / p31236 &lt; p31244

### p31245 POLYGON characteristic number of interpolation points

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 7331 |
| **Object:**Alle Objekte | **P-Group:**Funktionen | **Version:**1101200 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 1 | 10000 | [ 0 ] 360 |
| Alarms |  |  |

**Valid as of version:**
  
1.1

**Description:**
  
Sets the number of interpolation points for the characteristic.

**Dependency:**
  
  
Refer to:
p31246

**Note:**
  
The interpolation points are equidistantly distributed over the modulo length.

### p31246[0...n] POLYGON characteristic y values

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**p31245 | **Func. diagram:** 7331 |
| **Object:**Alle Objekte | **P-Group:**Funktionen | **Version:**1101200 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| -340.28235E36 | 340.28235E36 | [ 0 ] 0.000000 |
| Alarms |  |  |

**Valid as of version:**
  
1.1

**Description:**
  
Sets the y values for the interpolation points of the characteristic.

**Dependency:**
  
  
Refer to:
p31245

**Note:**
  
The characteristic is linearly interpolated between the interpolation points (y values).

### p31247 CI: POLYGON amplitude

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7331 |
| **Object:**Alle Objekte | **P-Group:**Funktionen | **Version:**1101200 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**PERCENT | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 1 |
| Alarms |  |  |

**Valid as of version:**
  
1.1

**Description:**
  
Sets the signal source for the amplitude to dynamically scale the characteristic.

### p31248 CI: POLYGON offset

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7331 |
| **Object:**Alle Objekte | **P-Group:**Funktionen | **Version:**1101200 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**PERCENT | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| Alarms |  |  |

**Valid as of version:**
  
1.1

**Description:**
  
Sets the signal source for the offset to dynamically offset the characteristic.

### r31249 CO: POLYGON output

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7331 |
| **Object:**Alle Objekte | **P-Group:**Funktionen | **Version:**1101200 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**PERCENT | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [%] | - [%] | [ ] - [%] |
| Alarms |  |  |

**Valid as of version:**
  
1.1

**Description:**
  
Display and connector output for the output value.  
The value is calculated as follows:  
Output p31249 = amplitude * y(x) + offset  
Amplitude: p31247  
y: p31246  
x: r31242[1] (master value effectively offset by p31240)  
Offset. p31248

**Note:**
  
The characteristic is linearly interpolated between the interpolation points (y values).

### p31250 POLYGON output integer number scaling

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer32 | **Dynamic index:**- | **Func. diagram:** 7331 |
| **Object:**Alle Objekte | **P-Group:**Funktionen | **Version:**1101200 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| -2147483648 | 2147483647 | [ 0 ] 1 |
| Alarms |  |  |

**Valid as of version:**
  
1.1

**Description:**
  
Sets the scaling of the output value for display as integer number.

**Dependency:**
  
  
Refer to:
r31249, r31251

### r31251 CO: POLYGON output integer number

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer32 | **Dynamic index:**- | **Func. diagram:** 7331 |
| **Object:**Alle Objekte | **P-Group:**Funktionen | **Version:**1101200 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| Alarms |  |  |

**Valid as of version:**
  
1.1

**Description:**
  
Display and connector output for the output value as integer number.

**Dependency:**
  
  
Refer to:
r31249, p31250

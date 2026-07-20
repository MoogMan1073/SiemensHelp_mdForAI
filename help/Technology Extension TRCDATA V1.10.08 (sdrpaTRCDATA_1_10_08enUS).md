---
title: "Technology Extension TRCDATA V1.10.08"
package: sdrpaTRCDATA_1_10_08enUS
topics: 19
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Technology Extension TRCDATA V1.10.08

This section contains the parameter descriptions for the Technology Extension.
In the table of contents, you will then see a separate entry for each parameter number.

## SINAMICS Parameter TRCDATA 32040 - 32099

SINAMICS Parameter TRCDATA 32040 - 32099

### p32040 TRCDATA recording mode

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C1( 3) | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7355 |
| **Object:**General OA obj | **P-Group:**- | **Version:**1100802 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 1 | 2 | [ 0 ] 1 |
| [Alarms](Technology%20Extension%20TRCDATA%20V1.10.08.md#technology-extension-trcdata-v11008) |  |  |

**Valid as of version:**
  
1.1

**Description:**
  
Setting the recording mode.  
The TRCDATA OA application is a deterministic, consistent data recording function.
The recorded values are output on the basis of indexed parameters. The recording mode
can be selected.  
An alternating buffer system is used to continuously record data. In this case, the
most recent consistent data set is displayed.  
For a single recording, data recording stops automatically and the values are kept
up to the next activation.  
After a complete recording interval, in both cases the recorded data points can be
read using an S7 variable service, for example.

**Value:**
  
1:
Continuous recording  
2:
Single recording

**Dependency:**
  
The OA application TRCDATA can be activated for several drive objects on a Control
Unit. The number of signals and data points to be recorded can be set differently
for each of these drive objects.  
For each drive object, a configuration attribute is calculated based on the following
formula:  
Configuration attribute = p32044 * (p32045 + p32046) / p32040  
The sum of all configuration attributes may not exceed a value of 325000.  
Refer to parameter p32044 for examples of valid maximum configurations.

**Note:**
  
TRCDATA: Trace Data (data recording)

### p32041 TRCDATA sampling time factor signal sampling

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C1( 3) | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7355 |
| **Object:**General OA obj | **P-Group:**- | **Version:**1100802 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 64 | [ 0 ] 32 |
| [Alarms](Technology%20Extension%20TRCDATA%20V1.10.08.md#technology-extension-trcdata-v11008) |  |  |

**Valid as of version:**
  
1.1

**Description:**
  
Sets the sampling time factor with which the values are recorded.  
The sampling time must be set as a multiple of p0115[0] (current controller sampling
time or basis sampling time).  
p0115[0] * p32041 defines the signal recording time.

**Value:**
  
0:
Do not calculate  
1:
T = p0115[0] * 1  
2:
T = p0115[0] * 2  
4:
T = p0115[0] * 4  
8:
T = p0115[0] * 8  
16:
T = p0115[0] * 16  
32:
T = p0115[0] * 32  
64:
T = p0115[0] * 64

**Dependency:**
  
  
Refer to:
p32042, r32043, p32047, p32048

### p32042 TRCDATA sampling time factor trace buffer

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C1( 3) | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7355 |
| **Object:**General OA obj | **P-Group:**- | **Version:**1100802 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 1 | 32000 | [ 0 ] 1000 |
| [Alarms](Technology%20Extension%20TRCDATA%20V1.10.08.md#technology-extension-trcdata-v11008) |  |  |

**Valid as of version:**
  
1.1

**Description:**
  
Sets the factor for the sampling time at the output as an integer multiple of the
sampling time at the input.  
The time between two data points that are output in the trace buffer is defined using
p0115[0] * p32041 * p32042.  
In addition, the sampling time at the output is indicated in ms in r32043.  
The trace buffer comprises parameters r32060 to r32095 and r32100 to r32111.

**Dependency:**
  
  
Refer to:
p32041, r32043

**Note:**
  
For p32042 = 1, the following applies:  
Each recorded data point is output to a trace buffer.  
For p32042 > 1, the following applies:  
The data points are appropriately combined. p32047 or p32048 is used to set the mode
when combining.

### r32043 TRCDATA sampling time trace buffer display

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7355 |
| **Object:**General OA obj | **P-Group:**- | **Version:**1100802 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [ms] | - [ms] | [ ] - [ms] |
| [Alarms](Technology%20Extension%20TRCDATA%20V1.10.08.md#technology-extension-trcdata-v11008) |  |  |

**Valid as of version:**
  
1.1

**Description:**
  
Displays the calculated sampling time for values in the trace buffer.  
The sampling time is defined by p0115[0] * p32041 * p32042.

**Dependency:**
  
  
Refer to:
p32041, p32042

### p32044 TRCDATA trace buffer number of data points

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C1( 3) | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 7355 |
| **Object:**General OA obj | **P-Group:**- | **Version:**1100802 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 1 | 65535 | [ 0 ] 60 |
| [Alarms](Technology%20Extension%20TRCDATA%20V1.10.08.md#technology-extension-trcdata-v11008) |  |  |

**Valid as of version:**
  
1.1

**Description:**
  
Sets the number of data points in the trace buffer.

**Dependency:**
  
The OA application TRCDATA can be activated for several drive objects on a Control
Unit. The number of signals and data points to be recorded can be set differently
for each of these drive objects.  
For each drive object, a configuration attribute is calculated based on the following
formula:  
Configuration attribute = p32044 * (p32045 + p32046) / p32040  
The sum of all configuration attributes may not exceed a value of 325000.  
- - - - - - - - - - - - - - -  
Example 1 for maximum configuration:  
Drive object 1 with TRCDATA  
p32040 = 2 (single)  
p32044 = 65000  
p32045 = 8  
p32046 = 2  
--> 65000 * (8 + 2) / 2 = 325000  
- - - - - - - - - - - - - - -  
Example 2 for maximum configuration:  
Drive object 1 with TRCDATA  
p32040 = 1 (continuous)  
p32044 = 65000  
p32045 = 4  
p32046 = 1  
--> 65000 * (4 + 1) / 1 = 325000  
- - - - - - - - - - - - - - -  
Example 3 for maximum configuration:  
Drive object 1 with TRCDATA  
p32040 = 2 (single)  
p32044 = 65000  
p32045 = 8  
p32046 = 1  
Drive object 2 with TRCDATA  
p32040 = 1 (continuous)  
p32044 = 1300  
p32045 = 20  
p32046 = 5  
--> drive object 1: 65000 * (8 + 1) / 2 = 292500  
--> drive object 2: 1300 * (20 + 5) / 1 = 32500  
--> drive object 1 + drive object 2: 292500 + 32500 = 325000  
  
Refer to:
A53510

### p32045 TRCDATA float signal sources number

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C1( 3) | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 7355 |
| **Object:**General OA obj | **P-Group:**- | **Version:**1100802 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 36 | [ 0 ] 8 |
| [Alarms](Technology%20Extension%20TRCDATA%20V1.10.08.md#technology-extension-trcdata-v11008) |  |  |

**Valid as of version:**
  
1.1

**Description:**
  
Sets the number of signals to be recorded with data type FloatingPoint32.

**Dependency:**
  
The OA application TRCDATA can be activated for several drive objects on a Control
Unit. The number of signals and data points to be recorded can be set differently
for each of these drive objects.  
For each drive object, a configuration attribute is calculated based on the following
formula:  
Configuration attribute = p32044 * (p32045 + p32046) / p32040  
The sum of all configuration attributes may not exceed a value of 325000.  
Refer to parameter p32044 for examples of valid maximum configurations.  
Parameters r32047 and r32049 are only displayed in the expert list of the STARTER
commissioning tool  
if p32045 is > 0.  
After changing the value in the online mode, the "Load project to PG" function must
be executed in the STARTER commissioning tool in order to update the expert list.  
The expert list is immediately updated when the value is changed in the offline mode.  
  
Refer to:
p32047, p32049  
Refer to:
A53510

### p32046 TRCDATA integer signal sources number

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C1( 3) | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 7355 |
| **Object:**General OA obj | **P-Group:**- | **Version:**1100802 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 12 | [ 0 ] 4 |
| [Alarms](Technology%20Extension%20TRCDATA%20V1.10.08.md#technology-extension-trcdata-v11008) |  |  |

**Valid as of version:**
  
1.1

**Description:**
  
Sets the number of signals to be traced with data type integer.

**Dependency:**
  
The OA application TRCDATA can be activated for several drive objects on a Control
Unit. The number of signals and data points to be recorded can be set differently
for each of these drive objects.  
For each drive object, a configuration attribute is calculated based on the following
formula:  
Configuration attribute = p32044 * (p32045 + p32046) / p32040  
The sum of all configuration attributes may not exceed a value of 325000.  
Refer to parameter p32044 for examples of valid maximum configurations.  
Parameters r32048 and r32050 are only displayed in the expert list of the STARTER
commissioning tool  
if p32046 > 0.  
After changing the value in the online mode, the "Load project to PG" function must
be executed in the STARTER commissioning tool in order to update the expert list.  
The expert list is immediately updated when the value is changed in the offline mode.  
  
Refer to:
p32048, p32050  
Refer to:
A53510

### p32047[0...n] TRCDATA float signals compression operation

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**p32045 | **Func. diagram:** 7355 |
| **Object:**General OA obj | **P-Group:**- | **Version:**1100802 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 3 | [ 0 ] 3 |
| [Alarms](Technology%20Extension%20TRCDATA%20V1.10.08.md#technology-extension-trcdata-v11008) |  |  |

**Valid as of version:**
  
1.1

**Description:**
  
Sets the compression operation for signals with data type FloatingPoint32.

**Value:**
  
0:
Inactive  
1:
Minimum value  
2:
Maximum value  
3:
Mean value

**Dependency:**
  
This parameter is only displayed in the expert list of the STARTER commissioning tool
if the number of float signal sources has been set to greater than 0 (p32045 > 0).

### p32048[0...n] TRCDATA integer signals compression operation

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**p32046 | **Func. diagram:** 7355 |
| **Object:**General OA obj | **P-Group:**- | **Version:**1100802 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 8 | [ 0 ] 3 |
| [Alarms](Technology%20Extension%20TRCDATA%20V1.10.08.md#technology-extension-trcdata-v11008) |  |  |

**Valid as of version:**
  
1.1

**Description:**
  
Sets the compression operation for signals with data type integer.

**Value:**
  
0:
Inactive  
1:
Minimum value  
2:
Maximum value  
3:
Mean value  
4:
Bit by bit OR  
5:
Bit by bit AND  
6:
Minimum value unsigned  
7:
Maximum value unsigned  
8:
Mean value unsigned

**Dependency:**
  
This parameter is only displayed in the expert list of the STARTER commissioning tool
if the number of integer signal sources has been set to greater than 0 (p32046 > 0).

### p32049[0...n] CI: TRCDATA float signals signal source

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / FloatingPoint32 | **Dynamic index:**p32045 | **Func. diagram:** 7355 |
| **Object:**General OA obj | **P-Group:**- | **Version:**1100802 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](Technology%20Extension%20TRCDATA%20V1.10.08.md#technology-extension-trcdata-v11008) |  |  |

**Valid as of version:**
  
1.1

**Description:**
  
Sets the signal source for signals to be recorded with data type FloatingPoint32.  
All signal sources can be interconnected, also those that can be recorded using the
STARTER commissioning tool. These especially include connector outputs (CO).

**Recommend.:**
  
The signal sources that have been set can be modified in operation. However, for a
consistent trace buffer, we recommend that deactivation/activation is realized via
the signal source of binector input p32055.

**Dependency:**
  
This parameter is only displayed in the expert list of the STARTER commissioning tool
if the number of float signal sources has been set to greater than 0 (p32045 > 0).  
  
Refer to:
p32041, p32042, r32043, p32045, p32047, p32055

### p32050[0...n] CI: TRCDATA integer signals signal source

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Integer32 | **Dynamic index:**p32046 | **Func. diagram:** 7355 |
| **Object:**General OA obj | **P-Group:**- | **Version:**1100802 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](Technology%20Extension%20TRCDATA%20V1.10.08.md#technology-extension-trcdata-v11008) |  |  |

**Valid as of version:**
  
1.1

**Description:**
  
Sets the signal source for signals to be recorded with data type integer.  
All signal sources can be interconnected, also those that can be recorded using the
STARTER commissioning tool. These especially include connector outputs (CO) and binector
outputs (BO).

**Recommend.:**
  
The signal sources that have been set can be modified in operation. However, for a
consistent trace buffer, we recommend that deactivation/activation is realized via
the signal source of binector input p32055.

**Dependency:**
  
This parameter is only displayed in the expert list of the STARTER commissioning tool
if the number of integer signal sources has been set to greater than 0 (p32046 > 0).  
  
Refer to:
p32041, p32042, r32043, p32046, p32048, p32055

### p32055 BI: TRCDATA enable

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 7355 |
| **Object:**General OA obj | **P-Group:**- | **Version:**1100802 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](Technology%20Extension%20TRCDATA%20V1.10.08.md#technology-extension-trcdata-v11008) |  |  |

**Valid as of version:**
  
1.1

**Description:**
  
Sets the signal source to enable recording.  
p32055 = 0 signal:  
No values are traced.  
p32055 = 1 signal:  
Values are recorded corresponding to the recording mode that has been set.

**Dependency:**
  
  
Refer to:
p32040

**Note:**
  
For a 0/1 edge, the interval counter r32059 is set = 0.  
For a 1/0 edge, recording is immediately stopped. The last consistent data set is
displayed.

### r32056.0...4 CO/BO: TRCDATA status word

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7355 |
| **Object:**General OA obj | **P-Group:**- | **Version:**1100802 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](Technology%20Extension%20TRCDATA%20V1.10.08.md#technology-extension-trcdata-v11008) |  |  |

**Valid as of version:**
  
1.1

**Description:**
  
Display and BICO output for the status word.

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Enable active | No | Yes | - |
| 01 | Recording running | No | Yes | - |
| 02 | "Continuous" recording mode selected | No | Yes | - |
| 03 | "Single" recording mode selected | No | Yes | - |
| 04 | Recorded data can be read | No | Yes | - |

### r32057 CO: TRCDATA data buffer internal level

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7355 |
| **Object:**General OA obj | **P-Group:**- | **Version:**1100802 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [%] | - [%] | [ ] - [%] |
| [Alarms](Technology%20Extension%20TRCDATA%20V1.10.08.md#technology-extension-trcdata-v11008) |  |  |

**Valid as of version:**
  
1.1

**Description:**
  
Displays the level of the trace buffer that can be written to as a percentage.  
For a level = 100 %, the read buffer, time stamp and interval counter are updated.

**Dependency:**
  
  
Refer to:
r32059

### r32058[0...1] CO: TRCDATA trace buffer time stamp

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7355 |
| **Object:**General OA obj | **P-Group:**- | **Version:**1100802 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](Technology%20Extension%20TRCDATA%20V1.10.08.md#technology-extension-trcdata-v11008) |  |  |

**Valid as of version:**
  
1.1

**Description:**
  
Displays the time stamp from the recording interval that can be read out.  
The time stamp refers to the start of the trace interval that can be read out corresponding
to index 0 of buffer parameters r32060 up to r32111.  
The time is taken from r2114 and comprises milliseconds (r32058[0]) and days (r32058[1]).

**Index:**
  
[
0]:
Milliseconds  
[
1]:
Days

**Dependency:**
  
  
Refer to:
r32059

### r32059 CO: TRCDATA trace buffer interval counter

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7355 |
| **Object:**General OA obj | **P-Group:**- | **Version:**1100802 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](Technology%20Extension%20TRCDATA%20V1.10.08.md#technology-extension-trcdata-v11008) |  |  |

**Valid as of version:**
  
1.1

**Description:**
  
Displaying the interval number of the recording interval that can be read out.  
The intervals are numbered in ascending order starting with 1.  
A value of 0 signals that no valid data can be read out.  
After switching on or after deactivating/activating, the interval counter starts at
0.  
The counter jumps to 1 when the value range overflows (2^32-1).

**Dependency:**
  
  
Refer to:
r32057, r32058

### r32099[0...99] TRCDATA trace buffer float signal 0 test output

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**4 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**General OA obj | **P-Group:**- | **Version:**1100802 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](Technology%20Extension%20TRCDATA%20V1.10.08.md#technology-extension-trcdata-v11008) |  |  |

**Valid as of version:**
  
1.1

**Description:**
  
Displaying the first 100 values of the trace buffer r32060 with data type FloatingPoint32
for test purposes.

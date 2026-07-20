---
title: "Technology Extension HEM V1.20.13"
package: sdrpaHEM_1_20_13enUS
topics: 27
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Technology Extension HEM V1.20.13

This section contains the parameter descriptions for the Technology Extension.
In the table of contents, you will then see a separate entry for each parameter number.

## SINAMICS Parameter HEM 32430 - 32457

SINAMICS Parameter HEM 32430 - 32457

### p32430 HEM ordering options

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** 7395 |
| **Object:**TM31 | **P-Group:**All groups | **Version:**1201200 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0001 bin |
| [Alarms](Technology%20Extension%20HEM%20V1.20.13.md#technology-extension-hem-v12013) |  |  |

**Valid as of version:**
  
1.2

**Description:**
  
Sets the available ordering options with software relevance.  
For bit 00:  
Option W01 includes two pumps installed in the converter-side fine water circuit.
The alternating operation of the pumps increases the operational reliability.  
For bit 01:  
Option W62 includes a flowmeter and a temperature acquisition (sensory system) in
the plant-side raw water circuit.

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | W01 - Heat Exchanger Module, partially redundant with two pumps | Inactive | Active | - |
| 01 | W62 - sensory system in the plant-side circuit raw water circuit | Inactive | Active | - |

**Dependency:**
  
  
Refer to:
p32432, p32433

**Note:**
  
HEM: Heat Exchanger Module  
Heat Exchanger Modules dissipate the heat loss from the converter. They consist of
a converter-side fine water circuit and a plant-side raw water circuit.

### p32431 HEM function selection

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**TM31 | **P-Group:**- | **Version:**1201200 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0000 1011 bin |
| [Alarms](Technology%20Extension%20HEM%20V1.20.13.md#technology-extension-hem-v12013) |  |  |

**Valid as of version:**
  
1.2

**Description:**
  
Sets the selection of the individual functions for the Heat Exchanger Module (HEM).  
For bit 00:  
For activated function, warning A53562 is issued when the difference between the actual
temperature value in the cabinet (r32451[1]) and the actual temperature value in the
fine water circuit (r32451[0]) exceeds the set value (p32435[3]).  
For bit 01:  
For activated function, the temperature setpoint is increased when there is risk of
condensation and this is indicated in status word 1 (r32452.8). The resulting temperature
setpoint (r32454) is then increased by 2 K (r32451[1] + 2 K).  
For bit 02:  
For activated function, the Heat Exchanger Module is switched on automatically when
there is risk of condensation. The automatic operation and the resulting temperature
rise in the fine water circuit (r32451[0]) reduces the risk of condensation.  
For bit 03:  
For activated function, the temperature in the fine water circuit is regulated to
the resulting temperature setpoint (r32454) using the control valve.  
For deactivated function, the set setpoint affects the control valve (p32440).  
For bit 04:  
For activated function, the Heat Exchanger Module is automatically switched on again
after 5 seconds after acknowledgment of a fault (r32452.4 = 0) if the switch-on command
is still active (p32432[0] = 1).

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Display condensation alarm | Inactive | Active | - |
| 01 | Increase temperature setpoint to prevent condensation | Inactive | Active | 7393, 7394 |
| 02 | Automatic operation for condensation prevention | Inactive | Active | 7393 |
| 03 | Temperature control | Inactive | Active | - |
| 04 | Automatic restart after HEM fault | Inactive | Active | - |

**Dependency:**
  
For bit 00 ... 02:  
At least one connector input p32433[15] must be connected to a signal source for the
temperature in the cabinet.  
  
Refer to:
p32437, p32440, r32454  
Refer to:
A53562

**Caution:**
  
For bit 02:  
For activated function, the Heat Exchanger Module starts automatically without a switch-on
command (p32432[0]).

### p32432[0...10] BI: HEM signal sources

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**1 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** 7390, 7398 |
| **Object:**TM31 | **P-Group:**- | **Version:**1201200 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0   [ 1 ] 0   [ 2 ] 1   [ 3...7 ] 0   [ 8 ] 1   [ 9 ] 1   [ 10 ] 1 |
| [Alarms](Technology%20Extension%20HEM%20V1.20.13.md#technology-extension-hem-v12013) |  |  |

**Valid as of version:**
  
1.2

**Description:**
  
Sets the signal sources to control the Heat Exchanger Module (HEM).  
For index [0]:  
Signal for activating/deactivating the Heat Exchanger Module. After switch off, the
run-on time set in p32441 acts.  
For index [1]:  
Signal for acknowledging Heat Exchanger Module faults. Faults are also reset when
the drive object is acknowledged.  
For index [2]:  
Signal for stopping the Heat Exchanger Module immediately.  
For index [3]:  
Selector switch signal to switch the operating modes MANUAL=0-signal/AUTO=1-signal.  
For index [4]:  
Pump 1 motor circuit-breaker feedback signal.  
For index [5]:  
Pump 2 motor circuit-breaker feedback signal (only for Option W01).  
For index [6]:  
Pump 1 contactor feedback signal.  
For index [7]:  
Pump 2 contactor feedback signal (only for Option W01).  
For index [8]:  
Signal for the leakage evaluation unit in the converter cabinet.  
For index [9]:  
Signal for the leakage evaluation unit in the Heat Exchanger Module (only for Option
W49).  
For index [10]:  
Feedback signal of the flow sensor in the plant-side raw water circuit (only for Option
W62).

**Index:**
  
[
0]:
HEM On/Off  
[
1]:
Acknowledge HEM fault  
[
2]:
HEM immediate stop  
[
3]:
HEM MANUAL/AUTO  
[
4]:
Pump 1 motor circuit-breaker  
[
5]:
Pump 2 motor circuit-breaker  
[
6]:
Pump 1 operation  
[
7]:
Pump 2 operation  
[
8]:
Frequency converter leakage  
[
9]:
HEM leakage  
[
10]:
Plant-side raw water circuit flow outside tolerance

**Dependency:**
  
  
Refer to:
p32430

### p32433[0...6] CI: HEM temperature signal source

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7397 |
| **Object:**TM31 | **P-Group:**- | **Version:**1201200 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](Technology%20Extension%20HEM%20V1.20.13.md#technology-extension-hem-v12013) |  |  |

**Valid as of version:**
  
1.2

**Description:**
  
Sets the signal source for the actual temperature values.  
For index [0]:  
Signal source for the actual temperature value of the converter-side fine water circuit.  
For index [1...5]:  
Signal sources for the actual temperature values in the cabinet.  
The maximum actual temperature value is displayed in r32541[1].  
For index [6]:  
Signal source for the actual temperature value of the plant-side raw water circuit
(only for Option W62).

**Index:**
  
[
0]:
Fine water circuit  
[
1]:
Cabinet 1  
[
2]:
Cabinet 2  
[
3]:
Cabinet 3  
[
4]:
Cabinet 4  
[
5]:
Cabinet 5  
[
6]:
Raw water circuit

**Dependency:**
  
  
Refer to:
p32430, r32451

**Note:**
  
For index [1...5]:  
At least one signal source must be interconnected if one of the functions p32431 bit
00 ... 02 is activated.

### p32434[0...1] CI: HEM fine water circuit actual pressure value signal source

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7395 |
| **Object:**TM31 | **P-Group:**- | **Version:**1201200 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](Technology%20Extension%20HEM%20V1.20.13.md#technology-extension-hem-v12013) |  |  |

**Valid as of version:**
  
1.2

**Description:**
  
Sets the signal source for the actual pressure values in the converter-side fine water
circuit.  
For index [0]:  
Signal source for the actual pressure value at the intake.  
For index [1]:  
Signal source for the actual pressure value in the return flow.

**Index:**
  
[
0]:
Intake  
[
1]:
Return flow

**Dependency:**
  
  
Refer to:
r32450

### p32435[0...3] HEM actual temperature value alarm thresholds

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7397 |
| **Object:**TM31 | **P-Group:**- | **Version:**1201200 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.0 [°C] | 58.0 [°C] | [ 0 ] 46.0 [°C]  [ 1 ] 50.0 [°C]  [ 2 ] 45.0 [°C]  [ 3 ] 1.0 [°C] |
| [Alarms](Technology%20Extension%20HEM%20V1.20.13.md#technology-extension-hem-v12013) |  |  |

**Valid as of version:**
  
1.2

**Description:**
  
Sets the alarm thresholds for the actual temperature values.  
For index [0]:  
If the actual temperature value of the fine water circuit (r32451[0]) exceeds the
selected alarm threshold, an appropriate alarm is issued.  
For index [1]:  
An appropriate alarm is issued if the actual temperature value in the cabinet (r32451[1])
exceeds the alarm threshold specified here.  
For index [2]:  
For activated Option W62 (p32430.1 = 1):  
If the actual temperature value of the raw water circuit (r32451[2]) exceeds the selected
alarm threshold, an appropriate alarm is issued.  
For index [3]:  
An appropriate alarm is issued if the difference between the actual temperature value
in the cabinet (r32451[1]) and the actual temperature value in the fine water circuit
(r32451[0]) exceeds the set value.

**Recommend.:**
  
For index [3]:  
The value must be set appropriate for the ambient air humidity.

**Index:**
  
[
0]:
Fine water circuit temperature alarm threshold  
[
1]:
Cabinet temperature alarm threshold  
[
2]:
Raw water circuit temperature alarm threshold  
[
3]:
Temperature difference condensation alarm

**Dependency:**
  
  
Refer to:
r32451  
Refer to:
A53559, A53562

### p32436[0...5] HEM fine water circuit pressure alarm thresholds

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7395, 7396 |
| **Object:**TM31 | **P-Group:**- | **Version:**1201200 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.3 [bar] | 6.0 [bar] | [ 0 ] 0.4 [bar]  [ 1 ] 5.5 [bar]  [ 2 ] 0.5 [bar]  [ 3 ] 4.5 [bar]  [ 4 ] 0.7 [bar]  [ 5 ] 2.5 [bar] |
| [Alarms](Technology%20Extension%20HEM%20V1.20.13.md#technology-extension-hem-v12013) |  |  |

**Valid as of version:**
  
1.2

**Description:**
  
Sets the alarm limits for the pressure in the converter-side fine water circuit.  
If the pressure exceeds or undershoots one of these pressure limits, an appropriate
alarm is generated.

**Index:**
  
[
0]:
Intake lower threshold  
[
1]:
Intake upper threshold  
[
2]:
Return flow lower threshold  
[
3]:
Return flow upper threshold  
[
4]:
Difference lower threshold  
[
5]:
Difference upper threshold

**Dependency:**
  
  
Refer to:
A53556

### p32437 HEM fine water circuit temperature setpoint

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7393 |
| **Object:**TM31 | **P-Group:**- | **Version:**1201200 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 10.0 [°C] | 50.0 [°C] | [ 0 ] 40.0 [°C] |
| [Alarms](Technology%20Extension%20HEM%20V1.20.13.md#technology-extension-hem-v12013) |  |  |

**Valid as of version:**
  
1.2

**Description:**
  
Setpoint for the temperature in the converter-side fine water circuit.

**Dependency:**
  
  
Refer to:
p32431, p32438, p32439

### p32438 HEM thermostat proportional gain

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7394 |
| **Object:**TM31 | **P-Group:**- | **Version:**1201200 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.000 | 100.000 | [ 0 ] 0.020 |
| [Alarms](Technology%20Extension%20HEM%20V1.20.13.md#technology-extension-hem-v12013) |  |  |

**Valid as of version:**
  
1.2

**Description:**
  
Sets the proportional gain Kp of the thermostat for the 3-way valve.

### p32439 HEM thermostat integral time

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7394 |
| **Object:**TM31 | **P-Group:**- | **Version:**1201200 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 1.0 [s] | 60.0 [s] | [ 0 ] 22.0 [s] |
| [Alarms](Technology%20Extension%20HEM%20V1.20.13.md#technology-extension-hem-v12013) |  |  |

**Valid as of version:**
  
1.2

**Description:**
  
Sets the integral time Tn of the thermostat for the 3-way valve.

### p32440 HEM control valve setpoint

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7394 |
| **Object:**TM31 | **P-Group:**- | **Version:**1201200 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 [%] | 100 [%] | [ 0 ] 0 [%] |
| [Alarms](Technology%20Extension%20HEM%20V1.20.13.md#technology-extension-hem-v12013) |  |  |

**Valid as of version:**
  
1.2

**Description:**
  
Sets the setpoint for the control valve.  
For deactivated "Temperature control" function (p32431.3 = 0), the set setpoint affects
the control valve.  
This function can be used to test the control valve.

**Note:**
  
The following applies:  
0 % corresponds to internal circulation (flow via plate heat exchanger is 0 %).  
100 % corresponds to full cooling capacity (flow via plate heat exchanger is 100 %).

### p32441 HEM run-on time

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7398 |
| **Object:**TM31 | **P-Group:**- | **Version:**1201200 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 [s] | 600 [s] | [ 0 ] 60 [s] |
| [Alarms](Technology%20Extension%20HEM%20V1.20.13.md#technology-extension-hem-v12013) |  |  |

**Valid as of version:**
  
1.2

**Description:**
  
Sets the run-on time.  
After deactivation via binector input p32432[0] = 0-signal, this time acts before
the Heat Exchanger Module is switched off.

### p32442[0...1] HEM pump run time until automatic switching

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7395 |
| **Object:**TM31 | **P-Group:**- | **Version:**1201200 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 1 [h] | 10000 [h] | [ 0 ] 3 [h] |
| [Alarms](Technology%20Extension%20HEM%20V1.20.13.md#technology-extension-hem-v12013) |  |  |

**Valid as of version:**
  
1.2

**Description:**
  
Sets the run times until automatic switching to the other pump.  
Different run times can be selected for the pumps. The different wear on the pumps
simplifies preventative maintenance.

**Index:**
  
[
0]:
Switching time pump 1 to 2  
[
1]:
Switching time pump 2 to 1

**Dependency:**
  
Only for Option W01 (p32430.0 = 1).  
  
Refer to:
p32430

### p32445 HEM pressure scaling

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**4 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7395 |
| **Object:**TM31 | **P-Group:**- | **Version:**1201200 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.0 [bar] | 30.0 [bar] | [ 0 ] 30.0 [bar] |
| [Alarms](Technology%20Extension%20HEM%20V1.20.13.md#technology-extension-hem-v12013) |  |  |

**Valid as of version:**
  
1.2

**Description:**
  
Sets the unit scaling for actual pressure values (r32450).  
100% corresponds to the set value in bar.

**Dependency:**
  
  
Refer to:
p32434, r32450

### p32446[0...5] HEM fine water circuit pressure fault limits

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**4 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7395, 7396 |
| **Object:**TM31 | **P-Group:**- | **Version:**1201200 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.0 [bar] | 6.0 [bar] | [ 0 ] 0.1 [bar]  [ 1 ] 5.9 [bar]  [ 2 ] 0.2 [bar]  [ 3 ] 5.9 [bar]  [ 4 ] 0.3 [bar]  [ 5 ] 3.0 [bar] |
| [Alarms](Technology%20Extension%20HEM%20V1.20.13.md#technology-extension-hem-v12013) |  |  |

**Valid as of version:**
  
1.2

**Description:**
  
Sets the fault limits for the pressure in the converter-side fine water circuit.  
If the pressure exceeds or undershoots one of these pressure limits, an appropriate
fault is generated.

**Index:**
  
[
0]:
Intake lower threshold  
[
1]:
Intake upper threshold  
[
2]:
Return flow lower threshold  
[
3]:
Return flow upper threshold  
[
4]:
Difference lower threshold  
[
5]:
Difference upper threshold

**Dependency:**
  
  
Refer to:
p32442  
Refer to:
A53557, F53558

**Note:**
  
For activated Option W01 (p32430.0 = 1), the violation of a pressure fault threshold
causes an alarm to be generated and switching to the second pump. If the second pump
also reaches a fault threshold, the Heat Exchanger Module is shutdown.  
The alarm is automatically withdrawn for the following cases:  
- The associated pump starts without violating fault thresholds (e.g. after reaching
the switching time to the redundant pump).  
- The Heat Exchanger Module is switched off.

### p32447 HEM fine water circuit temperature fault threshold

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**4 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7397 |
| **Object:**TM31 | **P-Group:**- | **Version:**1201200 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 45.0 [°C] | 100.0 [°C] | [ 0 ] 58.0 [°C] |
| [Alarms](Technology%20Extension%20HEM%20V1.20.13.md#technology-extension-hem-v12013) |  |  |

**Valid as of version:**
  
1.2

**Description:**
  
Sets the fault threshold for the temperature of the fine water circuit.  
If the temperature of the fine water circuit exceeds the set value, an appropriate
fault is issued and the Heat Exchanger Module switched off.

**Dependency:**
  
  
Refer to:
F53560

### p32448 HEM fine water circuit pressure difference suppression time

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**4 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7396 |
| **Object:**TM31 | **P-Group:**- | **Version:**1201200 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 [s] | 20 [s] | [ 0 ] 3 [s] |
| [Alarms](Technology%20Extension%20HEM%20V1.20.13.md#technology-extension-hem-v12013) |  |  |

**Valid as of version:**
  
1.2

**Description:**
  
Sets the suppression time for monitoring the pressure difference in the fine water
circuit.  
This time acts when starting and switching the pumps.

**Notice:**
  
The monitoring of the pressure difference is deactivated during this time.

### r32450[0...2] HEM fine water circuit actual pressure values

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7395, 7396 |
| **Object:**TM31 | **P-Group:**- | **Version:**1201200 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [bar] | - [bar] | [ ] - [bar] |
| [Alarms](Technology%20Extension%20HEM%20V1.20.13.md#technology-extension-hem-v12013) |  |  |

**Valid as of version:**
  
1.2

**Description:**
  
Display and connector output for the actual pressure values in the fine water circuit.

**Index:**
  
[
0]:
Intake  
[
1]:
Return flow  
[
2]:
Difference between intake and return flow

**Dependency:**
  
  
Refer to:
p32445

### r32451[0...2] CO: HEM actual temperature values

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7393, 7394, 7397 |
| **Object:**TM31 | **P-Group:**- | **Version:**1201200 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**p2006 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [°C] | - [°C] | [ ] - [°C] |
| [Alarms](Technology%20Extension%20HEM%20V1.20.13.md#technology-extension-hem-v12013) |  |  |

**Valid as of version:**
  
1.2

**Description:**
  
Display and connector output for the actual temperature values.  
For index [0]:  
Actual temperature value in the converter-side fine water circuit. The sensor is at
the intake and is used for actual value sensing for the integrated thermostat.  
For index [1]:  
The sensor is located behind the control box of the Heat Exchanger Module. It is used
for condensation monitoring and condensation prevention.  
For index [2]:  
Only for activated Option W62 (p32430.1 = 1).  
Actual temperature value in the raw water circuit. The sensor is at the intake. The
monitoring of the temperature in the raw water circuit reduces failure causes because
temperature problems are detected early.

**Index:**
  
[
0]:
Fine water circuit  
[
1]:
Cabinet  
[
2]:
Raw water circuit

**Dependency:**
  
  
Refer to:
p32430

### r32452.0...13 CO/BO: HEM status word 1

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7390, 7391 |
| **Object:**TM31 | **P-Group:**- | **Version:**1201200 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](Technology%20Extension%20HEM%20V1.20.13.md#technology-extension-hem-v12013) |  |  |

**Valid as of version:**
  
1.2

**Description:**
  
Display and BICO output for status word 1 of the Heat Exchanger Module.

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Operation | No | Yes | 7395, 7396, 7398 |
| 01 | Immediate stop active | No | Yes | 7398 |
| 02 | Ready for switching on | No | Yes | 7398 |
| 03 | Alarm active | Yes | No | - |
| 04 | Fault active | Yes | No | 7398 |
| 05 | Run-on time active | No | Yes | 7396, 7398 |
| 06 | Pump 1 actuated | No | Yes | 7396 |
| 07 | Pump 2 actuated | No | Yes | 7396 |
| 08 | Increase temperature setpoint to prevent condensation active | No | Yes | 7393 |
| 09 | Automatic operation for condensation prevention active | No | Yes | 7393, 7398 |
| 10 | Control valve setpoint specification active | No | Yes | - |
| 11 | MANUAL operation active | No | Yes | 7398 |
| 12 | Raw water circuit flow outside tolerance | No | Yes | - |
| 13 | Leakage detected | No | Yes | - |

### r32453.0...3 CO/BO: HEM status word 2

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** 7390, 7392 |
| **Object:**TM31 | **P-Group:**- | **Version:**1201200 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](Technology%20Extension%20HEM%20V1.20.13.md#technology-extension-hem-v12013) |  |  |

**Valid as of version:**
  
1.2

**Description:**
  
Display and BICO output for status word 2 of the Heat Exchanger Module.

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Pump 1 motor circuit-breaker | Inactive | Active | 7398 |
| 01 | Pump 2 motor circuit-breaker | Inactive | Active | 7398 |
| 02 | Pump 1 operation | Inactive | Active | - |
| 03 | Pump 2 operation | Inactive | Active | - |

### r32454 CO: HEM resulting temperature setpoint

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7393, 7394 |
| **Object:**TM31 | **P-Group:**- | **Version:**1201200 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [°C] | - [°C] | [ ] - [°C] |
| [Alarms](Technology%20Extension%20HEM%20V1.20.13.md#technology-extension-hem-v12013) |  |  |

**Valid as of version:**
  
1.2

**Description:**
  
Display and connector output for the resulting temperature setpoint.  
The setpoint set in p32437 acts generally. For activated "Condensation prevention,
increase temperature setpoint" function (p32431.1 = 1), the resulting setpoint can
be increased to maximum 45° C.

**Dependency:**
  
  
Refer to:
p32431, p32437

### r32455 CO: HEM control valve setpoint display

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7394 |
| **Object:**TM31 | **P-Group:**- | **Version:**1201200 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [%] | - [%] | [ ] - [%] |
| [Alarms](Technology%20Extension%20HEM%20V1.20.13.md#technology-extension-hem-v12013) |  |  |

**Valid as of version:**
  
1.2

**Description:**
  
Display and connector output of the setpoint resulting from the temperature control
for the 3-way valve.

**Dependency:**
  
  
Refer to:
A53561

**Notice:**
  
The 3-way valve closes automatically to 0% if a wire break between TM31 and the valve
is detected (provided the power supply is still active).  
In the case of a wire break to the temperature sensor in the fine water circuit, the
last active setpoint is retained and an appropriate alarm issued.

**Note:**
  
The following applies:  
0 % corresponds to internal circulation (flow via plate heat exchanger is 0 %).  
100 % corresponds to full cooling capacity (flow via plate heat exchanger is 100 %).

### p32456[0...2] HEM maintenance intervals

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**TM31 | **P-Group:**- | **Version:**1201200 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 [h] | 10000 [h] | [ 0 ] 0 [h]  [ 1 ] 2500 [h]  [ 2 ] 2500 [h] |
| [Alarms](Technology%20Extension%20HEM%20V1.20.13.md#technology-extension-hem-v12013) |  |  |

**Valid as of version:**
  
1.2

**Description:**
  
Sets the time for the individual maintenance intervals.  
An appropriate alarm is issued when the times set here are reached.  
Procedure when the alarm is initiated:  
- Perform the appropriate maintenance.  
- Set the operating hours of the associated maintenance to 0 (p32457[x]).

**Index:**
  
[
0]:
Heat Exchanger Module  
[
1]:
Pump 1  
[
2]:
Pump 2

**Dependency:**
  
  
Refer to:
p32457  
Refer to:
A53568

**Note:**
  
For value = 0, the associated function is deactivated.

### p32457[0...5] CO: HEM operating hours

|  |  |  |
| --- | --- | --- |
| **Can be changed:**UT | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**TM31 | **P-Group:**- | **Version:**1201200 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 [h] | 340.28235E36 [h] | [ 0 ] 0.00 [h] |
| [Alarms](Technology%20Extension%20HEM%20V1.20.13.md#technology-extension-hem-v12013) |  |  |

**Valid as of version:**
  
1.2

**Description:**
  
Display and connector output for the operating hours.  
The value can only be set to 0.  
Total operating hours:  
- Display of the total elapsed operating hours.  
- The value for pump 1 or 2 must be reset to 0 after a pump replacement.  
Maintenance operating hours:  
- Display the elapsed operating hours since the last maintenance.  
- After performing the appropriate maintenance, the value must be reset to 0.

**Index:**
  
[
0]:
Heat Exchanger Module total  
[
1]:
Heat Exchanger Module maintenance  
[
2]:
Pump 1 total  
[
3]:
Pump 1 maintenance  
[
4]:
Pump 2 total  
[
5]:
Pump 2 maintenance

**Dependency:**
  
  
Refer to:
p32456  
Refer to:
A53568

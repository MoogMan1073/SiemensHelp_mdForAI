---
title: "Technology Extension HEM V1.20.13"
package: sdralHEM_1_20_13enUS
topics: 20
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Technology Extension HEM V1.20.13

This section contains the alarm descriptions for the Technology Extension.
In the table of contents, you will then see a separate entry for each alarm number.

## SINAMICS Alarms HEM 53555 - 53572

SINAMICS Alarms HEM 53555 - 53572

### A53555 HEM Operating mode, MANUAL selected

**Drive object:**
  
All objects

**Valid as of version:**
  
1.2

**Message value:**
  
-

**Message class:**
  
Application / technological function faulted (17)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The Heat Exchanger Module is in MANUAL operating mode. This is activated by the selection
lever on the control box.  
Note:  
Activation via the HEM Technology Extension is not possible.  
Deactivation is not possible when the pressure and temperature thresholds are violated.  
HEM: Heat Exchanger Module

**Remedy:**
  
Not necessary.  
The alarm is withdrawn automatically after switching to AUTO operating mode.

### A53556 HEM alarm threshold for pressure in the fine water circuit violated

**Drive object:**
  
All objects

**Valid as of version:**
  
1.2

**Message value:**
  
Fault cause: %1 bin

**Message class:**
  
Application / technological function faulted (17)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
A measured quantity in the fine water circuit has undershot or exceeded the set alarm
threshold.  
Fault cause:  
Bit 00 = 1:  
The actual pressure value at the intake of the fine water circuit has undershot the
lower alarm threshold (p32436[0]).  
Bit 01 = 1:  
The actual pressure value at the intake of the fine water circuit has exceeded the
upper alarm threshold (p32436[1]).  
Bit 02 = 1:  
The actual pressure value in the return flow of the fine water circuit has undershot
the lower alarm threshold (p32436[2]).  
Bit 03 = 1:  
The actual pressure value in the return flow of the fine water circuit has exceeded
the upper alarm threshold (p32436[3]).  
Bit 04 = 1:  
The pressure difference (intake/return flow) of the fine water circuit has undershot
the lower alarm threshold (p32436[4]).  
Bit 05 = 1:  
The pressure difference (intake/return flow) of the fine water circuit has exceeded
the upper alarm threshold (p32436[5]).  
Note:  
The fault cause is also displayed as alarm value (r2124).  
HEM: Heat Exchanger Module  
See also: p32434 (HEM fine water circuit actual pressure value signal source), p32436 (HEM fine
water circuit pressure alarm thresholds)

**Remedy:**
  
- Check the associated actual pressure values.  
- Check the converter fine water circuit.  
- If necessary, adapt the associated alarm threshold (p32436[0...5]).

### A53557 HEM fault threshold for pressure violated, switching made to another pump

**Drive object:**
  
All objects

**Valid as of version:**
  
1.2

**Message value:**
  
Fault cause: %1 bin

**Message class:**
  
Application / technological function faulted (17)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
A fault threshold for the pressure was violated in the fine water circuit. Consequently,
switching was made to another pump.  
Fault cause:  
Bit 00 = 1:  
Pump 1 was switched off.  
Bit 01 = 1:  
Pump 2 was switched off.  
Note:  
The fault cause is also displayed as alarm value (r2124).  
HEM: Heat Exchanger Module

**Remedy:**
  
- Check the converter fine water circuit pump displayed in the alarm value.  
- Check the power supply of the pump displayed in the alarm value.  
- This alarm is withdrawn automatically when after the automatic switching (p32442[0...1])
no fault threshold is violated in the pump displayed in the alarm value.

### F53558 HEM fault threshold for pressure in the fine water circuit violated

**Drive object:**
  
All objects

**Valid as of version:**
  
1.2

**Message value:**
  
-

**Message class:**
  
Application / technological function faulted (17)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A fault threshold for the pressure was violated in the fine water circuit.  
In partial-redundant operation (Option W01):  
- A fault threshold for the pressure was violated at both pumps.  
For operation with one pump:  
- A fault threshold for the pressure was violated at pump 1.  
Note:  
HEM: Heat Exchanger Module  
See also: p32430 (HEM ordering options), p32434 (HEM fine water circuit actual pressure value
signal source), p32446 (HEM fine water circuit pressure fault limits)

**Remedy:**
  
- Check the pumps.  
- Check the power supply of the pumps.  
- Check the fine water circuit (e.g. leakage, valves).  
- See also the alarm value for A53557.

### A53559 HEM alarm threshold for temperature exceeded

**Drive object:**
  
All objects

**Valid as of version:**
  
1.2

**Message value:**
  
Fault cause: %1 bin

**Message class:**
  
Application / technological function faulted (17)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
A temperature has exceeded the set alarm threshold.  
Fault cause:  
Bit 00 = 1:  
The temperature at the intake of the fine water circuit has exceeded the alarm threshold
(p32435[0]).  
Bit 01 = 1:  
The internal cabinet temperature has exceeded the alarm threshold (p32435[1]).  
Bit 02 = 1:  
The temperature in the raw water circuit has exceeded the alarm threshold (p32435[2]).  
Note:  
The fault cause is also displayed as alarm value (r2124).  
HEM: Heat Exchanger Module  
See also: p32435 (HEM actual temperature value alarm thresholds), r32451 (HEM actual temperature
values)

**Remedy:**
  
General:  
- Check and correct the cause for the temperature increase (e.g. control valve, raw
water circuit).  
For bit 00 = 1:  
- Check the "Temperature control" function selection (p32431.3).  
See also: p32431 (HEM function selection)

### F53560 HEM fault threshold for temperature in the fine water circuit exceeded

**Drive object:**
  
All objects

**Valid as of version:**
  
1.2

**Message value:**
  
-

**Message class:**
  
Application / technological function faulted (17)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The temperature of the fine water circuit has exceeded the fault threshold of 58°
C.  
Operation of the Heat Exchanger Module is not possible, the pumps are switched off.  
Note:  
HEM: Heat Exchanger Module  
See also: r32451 (HEM actual temperature values)

**Remedy:**
  
- Check and correct the cause for the temperature increase (e.g. control valve, raw
water circuit).  
- Check the "Temperature control" function selection (p32431.3).  
See also: p32431 (HEM function selection)

### A53561 HEM temperature input wire break

**Drive object:**
  
All objects

**Valid as of version:**
  
1.2

**Message value:**
  
Fault cause: %1 bin

**Message class:**
  
Application / technological function faulted (17)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
A wire break in at least one temperature input was detected.  
Fault cause:  
Bit 00 = 1:  
Fine water circuit actual temperature value (p32433[0]).  
Bit 01 = 1:  
Actual temperature value cabinet 1 (p32433[1]).  
Bit 02 = 1:  
Actual temperature value cabinet 2 (p32433[2]).  
Bit 03 = 1:  
Actual temperature value cabinet 3 (p32433[3]).  
Bit 04 = 1:  
Actual temperature value cabinet 4 (p32433[4]).  
Bit 05 = 1:  
Actual temperature value cabinet 5 (p32433[5]).  
Note:  
The fault cause is also displayed as alarm value (r2124).  
HEM: Heat Exchanger Module  
See also: p32433 (HEM temperature signal source)

**Remedy:**
  
Check the wiring of the associated temperature sensors.

### A53562 HEM potential risk of condensation detected

**Drive object:**
  
All objects

**Valid as of version:**
  
1.2

**Message value:**
  
-

**Message class:**
  
Application / technological function faulted (17)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The difference between the actual temperature value in the cabinet (r32451[1]) and
the actual temperature value in the fine water circuit (r32451[0]) exceeds the set
temperature difference (p32435[3]). Consequently, plant condensation is possible.  
Note:  
HEM: Heat Exchanger Module  
See also: p32431 (HEM function selection), r32451 (HEM actual temperature values)

**Remedy:**
  
- Check the "Increase temperature setpoint to prevent condensation" function selection
(p32431.1).  
- Check the "Automatic operation for condensation prevention" function selection (p32431.2).  
- Check the "Temperature control" function selection (p32431.3).  
See also: p32431 (HEM function selection)

### A53563 HEM plant-side raw water circuit flow outside the tolerance

**Drive object:**
  
All objects

**Valid as of version:**
  
1.2

**Message value:**
  
-

**Message class:**
  
Application / technological function faulted (17)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The flow sensor signals a value outside the set range.  
Note:  
HEM: Heat Exchanger Module  
See also: p32430 (HEM ordering options), p32432 (HEM signal sources)

**Remedy:**
  
- Check the raw water flow in the plant-side circuit raw water circuit.  
- Check the sensor parameterization. The nominal flow for the plant-side circuit raw
water circuit is printed on the rating plate of the Heat Exchanger Module.

### A53564 (F) HEM converter cabinet leakage detected

**Drive object:**
  
All objects

**Valid as of version:**
  
1.2

**Message value:**
  
-

**Message class:**
  
Application / technological function faulted (17)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
A leakage within the converter cabinet was detected.  
Note:  
HEM: Heat Exchanger Module  
See also: p32432 (HEM signal sources)

**Remedy:**
  
- Check the converter cabinet for leakage.  
- Check the settings and wiring of the evaluation units.

Reaction upon F:  
 NONE

Acknowl. upon F:  
IMMEDIATELY

### A53565 (F) HEM Heat Exchanger Module leakage detected

**Drive object:**
  
All objects

**Valid as of version:**
  
1.2

**Message value:**
  
-

**Message class:**
  
Application / technological function faulted (17)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
A leakage was detected in the Heat Exchanger Module.  
Note:  
HEM: Heat Exchanger Module  
See also: p32432 (HEM signal sources)

**Remedy:**
  
- Check the Heat Exchanger Module for leakage.  
- Check the settings and wiring of the evaluation units.

Reaction upon F:  
 NONE

Acknowl. upon F:  
IMMEDIATELY

### A53566 HEM feedback signal of a motor circuit-breaker missing

**Drive object:**
  
All objects

**Valid as of version:**
  
1.2

**Message value:**
  
Fault cause: %1 bin

**Message class:**
  
Application / technological function faulted (17)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
Partial-redundant operation is no longer possible.  
Fault cause:  
Bit 00 = 1:  
Feedback signal from the motor circuit-breaker of pump 1 missing.  
Bit 01 = 1:  
Feedback signal from the motor circuit-breaker of pump 2 missing.  
Note:  
The fault cause is also displayed as alarm value (r2124).  
HEM: Heat Exchanger Module  
See also: p32430 (HEM ordering options), p32432 (HEM signal sources)

**Remedy:**
  
- Check the motor circuit-breaker of the associated pump.  
- Check the voltage supply of the associated pump.  
- Check the pump.

### F53567 HEM motor circuit-breaker feedback signal missing

**Drive object:**
  
All objects

**Valid as of version:**
  
1.2

**Message value:**
  
-

**Message class:**
  
Application / technological function faulted (17)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
For partial-redundant operation (Option W01):  
The feedback signals from the motor circuit-breaker of both pumps are missing.  
For operation of a single pump:  
Feedback signal from the motor circuit-breaker of pump 1 missing.  
Note:  
HEM: Heat Exchanger Module  
See also: p32430 (HEM ordering options), p32432 (HEM signal sources)

**Remedy:**
  
- Check the motor circuit-breaker of the pumps.  
- Check the power supply of the pumps.  
- Check the pump.

### A53568 HEM maintenance required

**Drive object:**
  
All objects

**Valid as of version:**
  
1.2

**Message value:**
  
Fault cause: %1 bin

**Message class:**
  
Application / technological function faulted (17)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
At least one maintenance interval (p32456[0...2]) has elapsed. An appropriate maintenance
is required.  
Fault cause:  
Bit 00 = 1:  
Maintenance for the Heat Exchanger Module is required.  
The operating hours counter for maintenance of the Heat Exchanger Module (p32457[1])
has exceeded the set maintenance interval (p32456[0]).  
Bit 01 = 1:  
Maintenance for pump 1 is required.  
The operating hours counter for maintenance of pump 1 (p32457[3]) has exceeded the
set maintenance interval (p32456[1]).  
Bit 02 = 1:  
Maintenance for pump 2 is required.  
The operating hours counter for maintenance of pump 2 (p32457[5]) has exceeded the
set maintenance interval (p32456[2]).  
Note:  
The fault cause is also displayed as alarm value (r2124).  
HEM: Heat Exchanger Module  
See also: p32456 (HEM maintenance intervals), p32457 (HEM operating hours)

**Remedy:**
  
- Perform the appropriate maintenance.  
- Set the associated operating hours counter for maintenance to 0 (p32457[1, 3, 5]).  
See also: p32457 (HEM operating hours)

### A53569 HEM immediate stop active

**Drive object:**
  
All objects

**Valid as of version:**
  
1.2

**Message value:**
  
-

**Message class:**
  
Application / technological function faulted (17)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The immediate stop for the Heat Exchanger Module was activated with the binector input
p32432[2] = 0-signal.  
Operation of the Heat Exchanger Module is not possible.  
Note:  
HEM: Heat Exchanger Module  
See also: p32432 (HEM signal sources)

**Remedy:**
  
None required.  
This alarm is withdrawn automatically after deselecting the immediate stop (p32432[2]
= 1-signal).

### F53570 HEM feedback pump in operation missing

**Drive object:**
  
All objects

**Valid as of version:**
  
1.2

**Message value:**
  
-

**Message class:**
  
Application / technological function faulted (17)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
Despite controlling the motor circuit-breaker via binector input p32432[4], no feedback
signal via binector input p32432[6] could be detected.  
In partial-redundant operation (option W01, p32430.0 = 1), the feedback signal via
binector input p32432[7] is also missing when the second pump is controlled via binector
input p32432[5].  
Note:  
HEM: Heat Exchanger Module  
See also: p32430 (HEM ordering options), p32432 (HEM signal sources)

**Remedy:**
  
- Check wiring (control and feedback).  
- Check the motor contactor of the pumps.

### A53571 - HEM cabinet temperature signal source missing

**Drive object:**
  
All objects

**Valid as of version:**
  
1.2

**Message value:**
  
-

**Message class:**
  
Application / technological function faulted (17)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
At least one of the following functions has been selected although no actual temperature
value for the cabinet is connected in p32433[1...5]:  
- p32431.0: Display condensation alarm  
- p32431.1: Increase temperature setpoint to prevent condensation  
- p32431.2: Automatic operation for condensation prevention  
Note:  
HEM: Heat Exchanger Module  
See also: p32431 (HEM function selection)

**Remedy:**
  
- Interconnect at least one signal source for the temperature in the cabinet in p32433[1...5].  
- Deactivate the functions in p32431.  
See also: p32431 (HEM function selection), p32433 (HEM temperature signal source)

### A53572 HEM temperature control not in the expected range

**Drive object:**
  
All objects

**Valid as of version:**
  
1.2

**Message value:**
  
-

**Message class:**
  
Application / technological function faulted (17)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The setpoint of the control valve r32455 has reached limit. The actual temperature
value of the fine water circuit in r32451[0] has not changed as expected and deviates
by over 3 K from the setpoint.  
Possible causes of the fault:  
- After upgrading the Technology Extension HEM from V1.1 to V1.2, the direction of
action of the control valve was not adjusted.  
- Control valve defective.  
- Lack of circulation in the raw water circuit (flow insufficient).  
- Temperature raw water circuit too warm.  
Note:  
HEM: Heat Exchanger Module

**Remedy:**
  
- Check the direction of action of the Heat Exchanger Module (see r32455).  
- Check the parameterization of analog output 0 of Terminal Module TM31.  
- Check the control valve.  
- Check the raw water circuit  
- Contact Technical Support.

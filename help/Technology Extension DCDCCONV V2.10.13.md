---
title: "Technology Extension DCDCCONV V2.10.13"
package: sdralDCDCCONV_2_10_13enUS
topics: 13
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Technology Extension DCDCCONV V2.10.13

This section contains the alarm descriptions for the Technology Extension.
In the table of contents, you will then see a separate entry for each alarm number.

## SINAMICS Alarms DCDCCONV 53460 - 53755

SINAMICS Alarms DCDCCONV 53460 - 53755

### A53460 DCDCCONV output voltage higher than DC link voltage

**Drive object:**
  
All objects

**Valid as of version:**
  
2.1

**Message value:**
  
-

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** DRIVE |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The output voltage at the load is higher than the DC link voltage of the Motor Module.  
Possible causes:  
- DC link voltage has dropped/collapsed.  
- The load causes the drive to regenerate and feeds back energy.  
Note:  
The drive is not shut down as a pulse inhibit in this operating state has no effect.
This operating state should be avoided using an external circuit.  
DCDCCONV: DC-DC converter

**Remedy:**
  
Not necessary.  
The alarm is automatically withdrawn when the output voltage is less than the DC link
voltage.

### F53461 DCDCCONV phase current difference exceeded

**Drive object:**
  
All objects

**Valid as of version:**
  
2.1

**Message value:**
  
-

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** DRIVE |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
PULSE INHIBIT

**Cause:**
  
The difference between two phase currents at the Motor Module is too high.  
2-phase operation: Excessively high difference between the phase currents of the selected
terminals.  
3-phase operation: Excessively high difference between two of the three phase currents.  
Possible causes:  
- One of the selected terminals is not connected.  
- Asymmetry for the connected coils.  
- Switching differences for the transistor bridges.  
Note:  
DCDCCONV: DC-DC converter

**Remedy:**
  
- Check the connection terminal wiring of the Motor Modules (p31665).  
- Use symmetrical coils.  
- Adapt the maximum phase current difference (p31666).  
- Increase the smoothing time constant for the PT1 filter for the phase current difference
(p31664).  
Note:  
The enable must be de-activated for acknowledgment (BI: p31668 = 0 signal).  
See also: p31664 (DCDCCONV phase current difference smoothing time constant), p31665 (DCDCCONV
operating mode), p31666 (DCDCCONV maximum phase current difference)

### F53462 (A) DCDCCONV current/voltage sensing failed

**Drive object:**
  
All objects

**Valid as of version:**
  
2.1

**Message value:**
  
Fault cause: %1

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** DRIVE |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
PULSE INHIBIT

**Cause:**
  
The current or voltage sensing is faulty.  
When changing the message type from fault to alarm, a pending alarm remains until
the next pulse inhibit.  
Fault cause:  
2 (= 02 hex):  
- Wire breakage at the VSM.  
- Max. permissible change of the actual voltage value is set too low (p31720).  
- DRIVE-CLiQ connection error to the VSM.  
3 (= 03 hex):  
- Current controllers and voltage controllers or DC link voltage controllers (Vdc
controllers) are operated for longer than allowed at their limits (p31721).  
- Motor Module not ready (e.g. missing enables).  
- Wire breakage at the VSM.  
- DRIVE-CLiQ connection error to the VSM.  
4 (= 04 hex)  
- Discrepancy between the set operating mode and wiring of the output terminals. As
a consequence, a current actual value that is close to 0 A is measured in a phase.  
Note:  
DCDCCONV: DC-DC converter  
VSM: Voltage Sensing Module

**Remedy:**
  
For fault cause = 2:  
- Check the voltage measurement at the VSM.  
- Increase max. permissible voltage change of voltage sensing (p31720).  
- Check the DRIVE-CLiQ connection to the VSM.  
- Check the setting of the phase equalization controller (p32908, p32909).  
For fault cause = 3:  
- Increase maximum duration for controllers at their limits (p31721).  
- Check missing enables of the Motor Module (r0046).  
- Check the voltage measurement at the VSM.  
- Check the DRIVE-CLiQ connection to the VSM.  
For fault cause = 4:  
- Check the setting of the operating mode (p31665).  
- Check the wiring of the output terminals.  
Note:  
The enable must be deactivated for acknowledgment (p31668 = 0 signal).  
See also: p31665 (DCDCCONV operating mode), p31680 (DCDCCONV output voltage actual value signal
source), p31720 (DCDCCONV voltage sensing change max.), p31721 (DCDCCONV controller
at its limits maximum duration)

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

### A53463 DCDCCONV output voltage setpoint greater than the maximum control voltage

**Drive object:**
  
All objects

**Valid as of version:**
  
2.1

**Message value:**
  
-

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** DRIVE |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The sum of the output voltage setpoints p31670 and p31671 is higher than the maximum
control voltage of the power unit being used. As a consequence, the setpoint cannot
be reached and is limited to the maximum control voltage.  
The maximum control voltage of the power unit being used depends on the actual DC
link voltage and the pulse frequency.  
Note:  
DCDCCONV: DC-DC converter

**Remedy:**
  
The setpoints of output voltages p31670 and p31671 should be reduced until the sum
falls below the maximum control voltage of the power unit being used.

### A53464 (F) DCDCCONV VSM output voltage constant

**Drive object:**
  
All objects

**Valid as of version:**
  
2.1

**Message value:**
  
-

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** DRIVE |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The voltage sensing is faulty.  
The measured VSM voltage values are constant for longer than monitoring time p32910.
This can temporarily occur and is interpreted by DCDCCONV as a DRIVE-CLiQ interruption.  
This message is also indicated using status bit r31669.9 = 1. At the same time, the
upper active control current setpoint limit (r31696) is set to 0 A.  
Note:  
DCDCCONV: DC-DC converter  
VSM: Voltage Sensing Module  
See also: r31669 (DCDCCONV status word), p32910 (DCDCCONV VSM values monitoring time)

**Remedy:**
  
- Set the current controller sampling time for the Motor Module and infeed the same
(p0115[0]).  
- Restore or check the DRIVE-CLiQ connection to the VSM.  
- Check or replace the VSM.

Reaction upon F:  
 NONE

Acknowl. upon F:  
IMMEDIATELY

### F53465 DCDCCONV DC contactor was opened

**Drive object:**
  
All objects

**Valid as of version:**
  
2.1

**Message value:**
  
-

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** DRIVE |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
PULSE INHIBIT

**Cause:**
  
The DC contactor was opened (feedback signal p32900[0] = 1/0 signal) while the enable
was active p31669.18.  
Possible causes:  
- One of the conditions for the close command is no longer fulfilled.  
- The output voltage (p31680) is higher than the maximum output voltage (p32902[1]).  
- The close command was withdrawn via its signal source (BI: 32900[1] = 0 signal).  
Note:  
DCDCCONV: DC-DC converter  
See also: r31669 (DCDCCONV status word), p32900 (DCDCCONV DC contactor signal source)

**Remedy:**
  
- Check the maximum output voltage (p32902[1]).  
- Issue a close command (p32900[1]).  
Note:  
The enable must be deactivated to acknowledge this fault (BI: p31668 = 0 signal).  
See also: p32900 (DCDCCONV DC contactor signal source), p32902 (DCDCCONV output voltage minimum/maximum
value)

### A53466 DCDCCONV voltage limits not plausible

**Drive object:**
  
All objects

**Valid as of version:**
  
2.1

**Message value:**
  
Fault cause: %1

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** DRIVE |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The settings of the control voltage limits are not plausible.  
Fault cause:  
1 (= 01 hex):  
- Resulting voltage setpoint (r31679[0]) > active upper control value limit (r31728)  
Note:  
The difference between the voltage setpoint and active, upper control voltage limit
can result in a remaining system deviation. As a consequence, the current and voltage
controllers can go to their associated limits.  
2 (= 02 hex):  
- Resulting voltage setpoint (r31679[0]) < active lower control voltage limit (r31729)  
Note:  
The difference between the voltage setpoint and active, lower control voltage limit
can result in a remaining system deviation. As a consequence, the current and voltage
controllers can go to their associated limits.  
3 (= 03 hex):  
- Control voltage upper limit (p31714) < control voltage lower limit (p31715)  
4 (= 04 hex):  
- Active upper control voltage limit (r31728) < active lower control voltage limit
(r31729)  
Internally, the lower control voltage limit is set equal to the active upper control
voltage limit. As a consequence, the output voltage is provided directly.  
Note:  
DCDCCONV: DC-DC converter  
See also: r31679 (DCDCCONV output voltage display), p31714 (DCDCCONV control voltage upper limit),
p31715 (DCDCCONV control voltage lower limit), r31728 (DCDCCONV control voltage upper
setpoint limit active), r31729 (DCDCCONV control voltage lower setpoint limit active)

**Remedy:**
  
For fault cause = 1:  
- Check the voltage setpoints (p31670, p31671).  
- Check the upper control voltage limits (p31713, p31714).  
For fault cause = 2:  
- Check the voltage setpoints (p31670, p31671).  
- Check the lower control voltage limits (p31715, p31723).  
For fault cause = 3:  
- Set the lower control voltage limit (p31715) less than the upper control voltage
limit (p31714).  
For fault cause = 4:  
- Check all control voltage limits (p31713, p31714, p31715, p31723).  
See also: p31670 (DCDCCONV output voltage setpoint), p31671 (DCDCCONV output voltage supplementary
setpoint signal source), p31713 (DCDCCONV control voltage upper setpoint limit signal
source), p31714 (DCDCCONV control voltage upper limit), p31715 (DCDCCONV control voltage
lower limit), p31723 (DCDCCONV control voltage lower setpoint limit signal source)

### F53467 (A) DCDCCONV overvoltage at the load

**Drive object:**
  
All objects

**Valid as of version:**
  
2.1

**Message value:**
  
-

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** DRIVE |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
PULSE INHIBIT

**Cause:**
  
The output voltage (p31680), measured at the load using the Voltage Sensing Module
(VSM), exceeds the set maximum output voltage (p32902[1]).  
Status bit r31669.19 = 1 is set during the overvoltage.  
Note:  
DCDCCONV: DC-DC converter  
See also: r31669 (DCDCCONV status word), p31680 (DCDCCONV output voltage actual value signal
source)

**Remedy:**
  
Check the maximum output voltage (p32902[1]).  
Note:  
The enable must be deactivated to acknowledge this fault (BI: p31668 = 0 signal).  
See also: p32902 (DCDCCONV output voltage minimum/maximum value)

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

### F53468 (A) DCDCCONV drive configuration not correct

**Drive object:**
  
All objects

**Valid as of version:**
  
2.1

**Message value:**
  
Fault cause: %1

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** DRIVE |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The drive configuration is not correct.  
Fault cause:  
1 (= 01 hex):  
- 3-phase operation is only possible on a chassis power unit.  
2 (= 02 hex):  
- 3-phase operation is only possible on a VECTOR drive object.  
3 (= 03 hex):  
- 3-phase operation is only possible when the software gating unit is activated.  
4 (= 04 hex):  
- p1800 cannot be automatically parameterized.  
Note:  
For 3-phase operation, the switching frequency is automatically derived based on the
current controller cycle p0115[0].  
5 (= 05 hex):  
- p1910 parameterization error.  
6 (= 06 hex):  
- p0290 parameterization error.  
Note:  
For DCDCCONV, neither in 2-phase nor in 3-phase operation is it permissible that the
overload response of the power unit influences the pulse frequency.  
7 (= 07 hex):  
- The parameterization of 2-phase operation on a VECTOR drive object is incorrect.  
Note:  
DCDCCONV: DC-DC converter  
See also: p31665 (DCDCCONV operating mode)

**Remedy:**
  
For fault cause = 1:  
Use a chassis power unit  
For fault cause = 2:  
Activate vector control on the corresponding drive object.  
For fault cause = 3:  
All of the following conditions must be satisfied in order to activate the software
gating unit:  
- In the modulator configuration, activate the DC link voltage compensation in the
closed-loop current control (p1810.01)  
- In the modulator configuration, activate wobbulation (p1810.02)  
- For the modulator mode, select the optimized pulse pattern (p1802 = 19)  
The software gating unit is only activated once a warm restart or save with subsequent
power off/on has been carried out.  
For fault cause = 4:  
Set the current controller sampling time (p0115[0]) to a value that matches the maximum
switching frequency of the chassis power unit.  
Note:  
For 3-phase operation, the Motor Module pulse frequency (p1800) is firmly specified
by the set current controller sampling time (p0115[0]). The pulse frequency is calculated
as follows: p1800 = 1/p0115[0].  
Example:  
The following applies for a maximum power unit switching frequency of 7.5 kHz:  
p0115[0] = 250 µs results in p1800 = 4 kHz --> value valid  
p0115[0] = 125 µs results in p1800 = 8 kHz --> value not valid  
For fault cause = 5:  
Deactivate motor data identification (p1910 = 0).  
For fault cause = 6:  
Set the overload response of the power unit (p0290) to a valid value (0, 1 or 10).  
For fault cause = 7:  
Correctly set the following parameters in all of the data sets that have been created:  
p1300 = 19 (U/f control with independent voltage setpoint)  
p1330 = p31717 (DCDCCONV space vector absolute value 2-phase)  
p1356 = p31718 (DCDCCONV space vector angle 2-phase)

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

### A53469 DCDCCONV temperature model switchover not possible

**Drive object:**
  
All objects

**Valid as of version:**
  
2.1

**Message value:**
  
-

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** DRIVE |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
It was not possible to switch over the temperature model in the power unit. The current
load capability is possibly restricted.  
Note:  
DCDCCONV: DC-DC converter

**Remedy:**
  
Upgrade the firmware version of the SINAMICS basic system to a compatible version,
at the least version 5.2 SP3 HF9.

### F53755 DCDCCONV power unit: Overload I2t

**Drive object:**
  
All objects

**Valid as of version:**
  
2.1

**Message value:**
  
-

**Message class:**
  
Power electronics faulted (5)

| Symbol | Meaning |
| --- | --- |
| **Component:** Power Module | **Propagation:** LOCAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
PULSE INHIBIT

**Cause:**
  
The power unit was overloaded when operated with the TEC DCDCCONV (r32914 = 100 %).  
- The permissible rated DC current of the power unit from the application description
was exceeded for an inadmissibly long time.  
- The permissible load duty cycle as specified in the application description was
not maintained.  
Note:  
DCDCCONV: DC-DC converter  
See also: r32914 (DCDCCONV power unit overload I2t)

**Remedy:**
  
- Reduce the continuous load.  
- Adapt the load duty cycle.  
- Check the rated DC current and maximum DC current of the power unit.  
- If necessary, use a larger power unit.

---
title: "Technology Extension SERVCOUP V1.20.14"
package: sdrpaSERVCOUP_1_20_14enUS
topics: 41
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Technology Extension SERVCOUP V1.20.14

This section contains the parameter descriptions for the Technology Extension.
In the table of contents, you will then see a separate entry for each parameter number.

## SINAMICS Parameter SERVCOUP 31740 - 31758

SINAMICS Parameter SERVCOUP 31740 - 31758

### p31740 SERVCOUP operating mode

[SERVO](#p31740-servcoup-operating-mode-1)

[SERVO Linear motor](#p31740-servcoup-operating-mode-2)

#### p31740 SERVCOUP operating mode

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C1( 3) | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7335 |
| **Object:**SERVO | **P-Group:**- | **Version:**1201100 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 2 | [ 0 ] 0 |
| [Alarms](Technology%20Extension%20SERVCOUP%20V1.20.14.md#technology-extension-servcoup-v12014) |  |  |

**Valid as of version:**
  
1.2

**Description:**
  
Setting the operating mode for the SERVCOUP Technology Extension  
Master and follower drive objects of the SERVO type are coupled using SERVCOUP (SERVO
coupling). The torque setpoint, speed actual value and electrical pole position angle
for the follower drive objects are specified by the master drive object.

**Value:**
  
0:
Inactive  
1:
Master drive object  
2:
Follower drive object

**Note:**
  
SERVCOUP: SERVO COUPLING (SERVO coupling)  
A SERVO coupling must contain precisely 1 master drive object (master DO) and 1 to
5 follower drive objects (follower DO).

#### p31740 SERVCOUP operating mode

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C1( 3) | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7335 |
| **Object:**SERVO (Lin) | **P-Group:**- | **Version:**1201100 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 2 | [ 0 ] 0 |
| [Alarms](Technology%20Extension%20SERVCOUP%20V1.20.14.md#technology-extension-servcoup-v12014) |  |  |

**Valid as of version:**
  
1.2

**Description:**
  
Setting the operating mode for the SERVCOUP Technology Extension  
Master and follower drive objects of the SERVO type are coupled using SERVCOUP (SERVO
coupling). The force setpoint, velocity actual value and electrical pole position
angle for the follower drive objects are specified by the master drive object.

**Value:**
  
0:
Inactive  
1:
Master drive object  
2:
Follower drive object

**Note:**
  
SERVCOUP: SERVO COUPLING (SERVO coupling)  
A SERVO coupling must contain precisely 1 master drive object (master DO) and 1 to
5 follower drive objects (follower DO).

### p31741 SERVCOUP number of encoders

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C1( 3) | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**SERVO | **P-Group:**- | **Version:**1201100 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 1 | [ 0 ] 0 |
| [Alarms](Technology%20Extension%20SERVCOUP%20V1.20.14.md#technology-extension-servcoup-v12014) |  |  |

**Valid as of version:**
  
1.2

**Description:**
  
Sets the number of encoders that are used for the closed-loop motor control.  
For the master drive object, p31741 must be set = 1.  
For the follower drive object, p31741 must be kept = 0.

**Value:**
  
0:
No encoder  
1:
One encoder (encoder 1)

**Dependency:**
  
  
Refer to:
A53470

### p31742 SERVCOUP follower maximum speed monitoring

[SERVO](#p31742-servcoup-follower-maximum-speed-monitoring-1)

[SERVO Linear motor](#p31742-servcoup-follower-maximum-velocity-monitoring)

#### p31742 SERVCOUP follower maximum speed monitoring

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C1( 3) | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**SERVO | **P-Group:**- | **Version:**1201100 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.000 [rpm] | 340.28235E36 [rpm] | [ 0 ] 0.000 [rpm] |
| [Alarms](Technology%20Extension%20SERVCOUP%20V1.20.14.md#technology-extension-servcoup-v12014) |  |  |

**Valid as of version:**
  
1.2

**Description:**
  
Sets the maximum speed for operation of a multi-winding motor with missing enables
at the follower motor module.  
On multi-winding motors operation with missing enables at the follower drive object
is only permissible up to a certain speed because not all the windings are energized.  
Monitoring is only realized at the assigned master drive object when the following
preconditions are satisfied:  
1. Setting p31742 &gt; 0.  
2. Setting p31743 = 0 (multiple separate winding systems in one enclosure).  
3: The actual speed of the master drive object is greater than that of the value set
in p31742.  
4. The follower drive object is not enabled, e.g. due to missing enable signal or
due to an active fault with fault response OFF2.  
If all these conditions are met, fault F53473 is output at the master drive object
with fault response OFF2. Fault F53471 is then initiated on all follower drive objects.

**Dependency:**
  
The monitoring time in p1227 is active for the follower drive object. If the fault
should be immediately output after the speed is exceeded, then p1227 must be set =
0.  
  
Refer to:
F53473

**Note:**
  
This parameter is only relevant for follower drive objects (p31740 = 2). This parameter
is ignored for a master drive object (p31740 = 1).  
This monitoring is deactivated for the setting p31742 = 0.

#### p31742 SERVCOUP follower maximum velocity monitoring

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C1( 3) | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**SERVO (Lin) | **P-Group:**- | **Version:**1201100 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.000 [m/min] | 340.28235E36 [m/min] | [ 0 ] 0.000 [m/min] |
| [Alarms](Technology%20Extension%20SERVCOUP%20V1.20.14.md#technology-extension-servcoup-v12014) |  |  |

**Valid as of version:**
  
1.2

**Description:**
  
Sets the maximum velocity for operation of a multi-winding motor with missing enables
at the follower motor module.  
On multi-winding motors operation with missing enables at the follower drive object
is only permissible up to a certain velocity because not all the windings are energized.  
Monitoring is only realized at the assigned master drive object when the following
preconditions are satisfied:  
1. Setting p31742 &gt; 0.  
2. Setting p31743 = 0 (multiple separate winding systems in one enclosure).  
3: The actual velocity of the master drive object is greater than the value set in
p31742.  
4. The follower drive object is not enabled, e.g. due to missing enable signal or
due to an active fault with fault response OFF2.  
If all these conditions are met, fault F53473 is output at the master drive object
with fault response OFF2. Fault F53471 is then initiated on all follower drive objects.

**Dependency:**
  
The monitoring time in p1227 is active for the follower drive object. If the fault
should be immediately output after the velocity is exceeded, then p1227 must be set
= 0.  
  
Refer to:
F53473

**Note:**
  
This parameter is only relevant for follower drive objects (p31740 = 2). This parameter
is ignored for a master drive object (p31740 = 1).  
This monitoring is deactivated for the setting p31742 = 0.

### p31743 SERVCOUP motor type

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C1( 3) | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**SERVO | **P-Group:**- | **Version:**1201100 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 1 | [ 0 ] 0 |
| [Alarms](Technology%20Extension%20SERVCOUP%20V1.20.14.md#technology-extension-servcoup-v12014) |  |  |

**Valid as of version:**
  
1.2

**Description:**
  
Sets the motor type.  
Depending on the motor type, offset clocking is either permitted or inhibited.  
If value = 0:  
For motors with windings in a common enclosure (e.g. 1FW4, 1FE2), the following applies:  
- Offset clocking is not permitted.  
- The parameters for the offset clocking should be appropriately set (p1815, p1816,
p1819).  
- The plausibility of the parameter setting for offset clocking is checked.  
If value = 1:  
For motors with windings in a separate enclosure (e.g. 1FW6, 1FN3, segment motors),
the following applies:  
- Offset clocking is permitted (p1815, p1816, p1819).  
- the parameter setting for offset clocking is not checked.

**Value:**
  
0:
Multiple separate winding systems in one enclosure  
1:
Multiple separate winding systems in separate enclosures

**Dependency:**
  
  
Refer to:
p31748  
Refer to:
A53470

### p31744 SERVCOUP follower torque scaling

[SERVO](#p31744-servcoup-follower-torque-scaling-1)

[SERVO Linear motor](#p31744-servcoup-follower-force-setpoint-scaling)

#### p31744 SERVCOUP follower torque scaling

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7335 |
| **Object:**SERVO | **P-Group:**- | **Version:**1201100 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.10 [%] | 100.00 [%] | [ 0 ] 100.00 [%] |
| [Alarms](Technology%20Extension%20SERVCOUP%20V1.20.14.md#technology-extension-servcoup-v12014) |  |  |

**Valid as of version:**
  
1.2

**Description:**
  
Sets the scaling factor for the torque setpoint specified by the master drive object
for the follower drive object.

**Note:**
  
This parameter is only effective for a follower drive object; it is always 100 % for
master drive objects.  
The torque obtained at the follower drive object depends on the setpoint from the
higher-level speed controller of the master drive object and the torque limits set
there.

#### p31744 SERVCOUP follower force setpoint scaling

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7335 |
| **Object:**SERVO (Lin) | **P-Group:**- | **Version:**1201100 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.10 [%] | 100.00 [%] | [ 0 ] 100.00 [%] |
| [Alarms](Technology%20Extension%20SERVCOUP%20V1.20.14.md#technology-extension-servcoup-v12014) |  |  |

**Valid as of version:**
  
1.2

**Description:**
  
Sets the scaling factor for the force setpoint specified by the master drive object
for the follower drive object.

**Note:**
  
This parameter is only effective for a follower drive object; it is always 100 % for
master drive objects.  
The force obtained at the follower drive object depends on the setpoint from the higher-level
speed controller of the master drive object and the force limits set there.

### r31745 CO: SERVCOUP master coupling assignment

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** 7335 |
| **Object:**SERVO | **P-Group:**- | **Version:**1201100 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](Technology%20Extension%20SERVCOUP%20V1.20.14.md#technology-extension-servcoup-v12014) |  |  |

**Valid as of version:**
  
1.2

**Description:**
  
Display and connector output for the coupling between the master and follower drive
object.

**Dependency:**
  
  
Refer to:
p31746  
Refer to:
A53470

**Note:**
  
This parameter is only relevant for a master drive object.  
No signals are transferred via the BICO interconnection CI: p31746 (follower drive
object) = r31745 (master drive object). The interconnection is only used for the master-follower
drive object assignment.

### p31746 CI: SERVCOUP follower coupling assignment signal source

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C1( 3) | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Integer16 | **Dynamic index:**- | **Func. diagram:** 7335 |
| **Object:**SERVO | **P-Group:**- | **Version:**1201100 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](Technology%20Extension%20SERVCOUP%20V1.20.14.md#technology-extension-servcoup-v12014) |  |  |

**Valid as of version:**
  
1.2

**Description:**
  
Sets the signal source for the coupling between the master and follower drive object.  
Example:  
The following BICO interconnections are required for one master and two follower drive
objects:  
CI: p31746 (follower drive object 1) = r31745 (master drive object)  
CI: p31746 (follower drive object 2) = r31745 (master drive object)

**Dependency:**
  
  
Refer to:
r31745  
Refer to:
A53470

**Note:**
  
This parameter is only relevant for a follower drive object.  
No signals are transferred via the BICO interconnection CI: p31746 (follower drive
object) = r31745 (master drive object). The interconnection is only used for the master-follower
drive object assignment.

### r31747 SERVCOUP follower assignment to master drive object display

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**SERVO | **P-Group:**- | **Version:**1201100 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](Technology%20Extension%20SERVCOUP%20V1.20.14.md#technology-extension-servcoup-v12014) |  |  |

**Valid as of version:**
  
1.2

**Description:**
  
Displays the drive object number of the assigned master drive object.

**Dependency:**
  
  
Refer to:
r31745, p31746

**Note:**
  
This parameter is only relevant for follower drive objects; it is always 0 for a master
drive object.

### p31748 SERVCOUP follower angular offset

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** 7335 |
| **Object:**SERVO | **P-Group:**- | **Version:**1201100 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| -180.00 [°] | 180.00 [°] | [ 0 ] 0.00 [°] |
| [Alarms](Technology%20Extension%20SERVCOUP%20V1.20.14.md#technology-extension-servcoup-v12014) |  |  |

**Valid as of version:**
  
1.2

**Description:**
  
Sets an angular offset between the master and follower drive objects.  
For motors with multiple separate winding systems in separate enclosures (p31743 =
1), using this parameter, a possible mechanical offset can be compensated therefore
ensuring correct commutation.

**Dependency:**
  
  
Refer to:
p31743

**Warning:**
  
For an incorrectly set angular offset, the motor component is incorrectly oriented,
which can result in injury and/or material damage.

**Note:**
  
This parameter is only active for the particular follower drive object.  
For a master drive object, correct alignment to the encoder system is achieved via
the angular commutation offset (p0431).

### p31749 SERVCOUP master alarm propagation

[SERVO](#p31749-servcoup-master-alarm-propagation-1)

[SERVO Linear motor](#p31749-servcoup-master-alarm-propagation-2)

#### p31749 SERVCOUP master alarm propagation

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C1( 3) | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**SERVO | **P-Group:**- | **Version:**1201100 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 2 | [ 0 ] 1 |
| [Alarms](Technology%20Extension%20SERVCOUP%20V1.20.14.md#technology-extension-servcoup-v12014) |  |  |

**Valid as of version:**
  
1.2

**Description:**
  
Setting to activate the propagation of faults from the follower to the master drive
object.  
If a fault response occurs for a follower drive object, then it can be set so that
it is propagated to the master drive object.  
If value = 0:  
In the case of a fault, the drive group continues to operate with reduced torque.
The magnitude of the total torque is reduced by the torque of the follower drive object
that failed.  
If value = 1:  
A fault with OFF2 fault response is sent to the master and to the associated follower
drive objects. The drive group coasts down.  
If value = 2:  
A fault with OFF3 fault response is sent to the master drive object. The master drive
object brakes the drive group along the OFF3 ramp. A fault with OFF2 fault response
is then output on the associated follower drive objects.

**Value:**
  
0:
Follower to master DO: propagation deactivated  
1:
Follower to master DO: propagation activated with OFF2  
2:
Follower to master DO: propagation activated with OFF3

**Dependency:**
  
  
Refer to:
F53471, F53475

**Notice:**
  
If value = 0:  
It must be guaranteed that the drive group is able to operate the load, even without
the follower drive object that has failed (for a certain length of time).  
If value = 2:  
It must be guaranteed that the drive group is able to brake the load along the OFF3
ramp, even without the follower drive object that has failed.

**Note:**
  
The parameter is only relevant for master drive objects.

#### p31749 SERVCOUP master alarm propagation

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C1( 3) | **Calculated:**- | **Access level:**3 |
| **Data type:**Integer16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**SERVO (Lin) | **P-Group:**- | **Version:**1201100 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0 | 2 | [ 0 ] 1 |
| [Alarms](Technology%20Extension%20SERVCOUP%20V1.20.14.md#technology-extension-servcoup-v12014) |  |  |

**Valid as of version:**
  
1.2

**Description:**
  
Setting to activate the propagation of faults from the follower to the master drive
object.  
If a fault response occurs for a follower drive object, then it can be set so that
it is propagated to the master drive object.  
If value = 0:  
In the case of a fault, the drive group continues to operate with reduced force. The
magnitude of the total force is reduced by the force of the follower drive object
that failed.  
If value = 1:  
A fault with OFF2 fault response is sent to the master and to the associated follower
drive objects.  
If value = 2:  
A fault with OFF3 fault response is sent to the master drive object. The master drive
object brakes the drive group along the OFF3 ramp. A fault with OFF2 fault response
is then output on the associated follower drive objects.

**Value:**
  
0:
Follower to master DO: propagation deactivated  
1:
Follower to master DO: propagation activated with OFF2  
2:
Follower to master DO: propagation activated with OFF3

**Dependency:**
  
  
Refer to:
F53471, F53475

**Notice:**
  
If value = 0:  
It must be guaranteed that the drive group is able to operate the load, even without
the follower drive object that has failed (for a certain length of time).  
If value = 2:  
It must be guaranteed that the drive group is able to brake the load along the OFF3
ramp, even without the follower drive object that has failed.

**Note:**
  
The parameter is only relevant for master drive objects.

### r31750.0...15 CO/BO: SERVCOUP status word

[SERVO](#r31750015-cobo-servcoup-status-word-1)

[SERVO Linear motor](#r31750015-cobo-servcoup-status-word-2)

#### r31750.0...15 CO/BO: SERVCOUP status word

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**SERVO | **P-Group:**- | **Version:**1201100 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](Technology%20Extension%20SERVCOUP%20V1.20.14.md#technology-extension-servcoup-v12014) |  |  |

**Valid as of version:**
  
1.2

**Description:**
  
Display and BICO output for the status word.

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Inactive | No | Yes | - |
| 01 | Master drive object | No | Yes | - |
| 02 | Follower drive object | No | Yes | - |
| 03 | Master incremental encoder available | No | Yes | - |
| 04 | Master absolute encoder available | No | Yes | - |
| 05 | Induction motor | No | Yes | - |
| 06 | Master incremental encoder with C/D track available | No | Yes | - |
| 07 | Copy follower torque setpoint function generator / SBT | No | Yes | - |
| 08 | Follower coarse synchronization acceptance running | No | Yes | - |
| 09 | Follower coarse synchronization accepted | No | Yes | - |
| 10 | Master torque coupling tolerance OK | No | Yes | - |
| 11 | Follower drive ready to start | No | Yes | - |
| 12 | Master status OK | No | Yes | - |
| 13 | Master status rundown | No | Yes | - |
| 14 | Master status inhibit pulses | No | Yes | - |
| 15 | Master status acknowledge message | No | Yes | - |

**Note:**
  
Bits 00 and 05 are of significance for master and follower drive objects.  
Bits 01, 03, 04, 06, 10, 12...15 are only of significance for a master drive object.
They have a 0 signal for a follower drive object.  
Bits 02, 07, 08, 09, 11 are only of significance for a follower drive object; otherwise
they have a 0 signal.  
  
For bit 07:  
The bit is set if one of the following conditions is satisfied:  
- a monitoring cycle (p9500) was detected on the assigned master drive object before
the start of the brake test (r10231.1 = 1 signal).  
- the parameter p31757 = 1 signal was set on the follower drive object.  
If the bit is set r1651 of the master drive object is scaled using p31744 and acts
on the follower drive object as function generator torque setpoint r1651.  
  
For bit 10:  
The bit is set if the absolute deviation between master and follower torque actual
values is smaller than the tolerance set in p31758.  
An overshoot or undershoot of the follower torque actual value to the master torque
actual value by the tolerance set in p31758 sets the bit equal to 0.  
The bit can also be used for the SBT for automatic evaluation.  
  
  
SBT: Safe Brake Test (Safety Integrated Extended Function)

#### r31750.0...15 CO/BO: SERVCOUP status word

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**SERVO (Lin) | **P-Group:**- | **Version:**1201100 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](Technology%20Extension%20SERVCOUP%20V1.20.14.md#technology-extension-servcoup-v12014) |  |  |

**Valid as of version:**
  
1.2

**Description:**
  
Display and BICO output for the status word.

**Bit field:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bit | Signal name | 0 signal | 1 signal | Function diagram |
| 00 | Inactive | No | Yes | - |
| 01 | Master drive object | No | Yes | - |
| 02 | Follower drive object | No | Yes | - |
| 03 | Master incremental encoder available | No | Yes | - |
| 04 | Master absolute encoder available | No | Yes | - |
| 05 | Induction motor | No | Yes | - |
| 06 | Master incremental encoder with C/D track available | No | Yes | - |
| 07 | Copy follower force setpoint function generator / SBT | No | Yes | - |
| 08 | Follower coarse synchronization acceptance running | No | Yes | - |
| 09 | Follower coarse synchronization accepted | No | Yes | - |
| 10 | Master force coupling tolerance OK | No | Yes | - |
| 11 | Follower drive ready to start | No | Yes | - |
| 12 | Master status OK | No | Yes | - |
| 13 | Master status rundown | No | Yes | - |
| 14 | Master status inhibit pulses | No | Yes | - |
| 15 | Master status acknowledge message | No | Yes | - |

**Note:**
  
Bits 00 and 05 are of significance for master and follower drive objects.  
Bits 01, 03, 04, 06, 10, 12...15 are only of significance for a master drive object.
They have a 0 signal for a follower drive object.  
Bits 02, 07, 08, 09, 11 are only of significance for a follower drive object; otherwise
they have a 0 signal.  
  
For bit 07:  
The bit is set if one of the following conditions is satisfied:  
- a monitoring cycle (p9500) was detected on the assigned master drive object before
the start of the brake test (r10231.1 = 1 signal).  
- the parameter p31757 = 1 signal was set on the follower drive object.  
If the bit is set r1651 of the master drive object is scaled using p31744 and acts
on the follower drive object as function generator force setpoint r1651.  
  
For bit 10:  
The bit is set if the absolute deviation between master and follower force actual
values is smaller than the tolerance set in p31758.  
An overshoot or undershoot of the follower force actual value to the master force
actual value by the tolerance set in p31758 sets the bit equal to 0.  
The bit can also be used for the SBT for automatic evaluation.  
  
  
SBT: Safe Brake Test (Safety Integrated Extended Function)

### r31751[0...9] SERVCOUP configuration error

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned16 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**SERVO | **P-Group:**- | **Version:**1201100 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ ] - |
| [Alarms](Technology%20Extension%20SERVCOUP%20V1.20.14.md#technology-extension-servcoup-v12014) |  |  |

**Valid as of version:**
  
1.2

**Description:**
  
Displays the number of incorrectly set parameters in the basic system.  
The entered parameter numbers are deleted when the system powers up next time.

**Index:**
  
[
0]:
1st parameter number  
[
1]:
2nd parameter number  
[
2]:
3rd parameter number  
[
3]:
4th parameter number  
[
4]:
5th parameter number  
[
5]:
6th parameter number  
[
6]:
7th parameter number  
[
7]:
8th parameter number  
[
8]:
9th parameter number  
[
9]:
10th parameter number

**Dependency:**
  
The parameter numbers are entered after alarm A53470 occurs.  
  
Refer to:
A53470

### r31752 CO: SERVCOUP master torque actual value total display

[SERVO](#r31752-co-servcoup-master-torque-actual-value-total-display-1)

[SERVO Linear motor](#r31752-co-servcoup-master-force-actual-value-total-display)

#### r31752 CO: SERVCOUP master torque actual value total display

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**SERVO | **P-Group:**- | **Version:**1201100 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**p2003 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [Nm] | - [Nm] | [ ] - [Nm] |
| [Alarms](Technology%20Extension%20SERVCOUP%20V1.20.14.md#technology-extension-servcoup-v12014) |  |  |

**Valid as of version:**
  
1.2

**Description:**
  
Display and connector output for current torque actual value.  
The value is the sum of the torques r0080 of all connected power units.

**Dependency:**
  
  
Refer to:
p31744, p31756

**Note:**
  
This parameter is only relevant for master drive objects. It is always 0 for a follower
drive object.  
The display is delayed by one speed controller clock cycle p0115[1].

#### r31752 CO: SERVCOUP master force actual value total display

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**SERVO (Lin) | **P-Group:**- | **Version:**1201100 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**p2003 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [N] | - [N] | [ ] - [N] |
| [Alarms](Technology%20Extension%20SERVCOUP%20V1.20.14.md#technology-extension-servcoup-v12014) |  |  |

**Valid as of version:**
  
1.2

**Description:**
  
Display and connector output for actual force value.  
The value is the sum of the forces r0080 of all connected power units.

**Dependency:**
  
  
Refer to:
p31744, p31756

**Note:**
  
This parameter is only relevant for master drive objects. It is always 0 for a follower
drive object.  
The display is delayed by one velocity controller clock cycle p0115[1].

### r31753 SERVCOUP master scaling factor total display

[SERVO](#r31753-servcoup-master-scaling-factor-total-display-1)

[SERVO Linear motor](#r31753-servcoup-master-scaling-factor-total-display-2)

#### r31753 SERVCOUP master scaling factor total display

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**SERVO | **P-Group:**- | **Version:**1201100 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [%] | - [%] | [ ] - [%] |
| [Alarms](Technology%20Extension%20SERVCOUP%20V1.20.14.md#technology-extension-servcoup-v12014) |  |  |

**Valid as of version:**
  
1.2

**Description:**
  
Displays the scaling factor for the total torque of the drive group.  
Using this factor, the total torque of the drive group can be calculated from the
master drive object torque. The scaling factor is valid for setpoint and actual value
(r0079, r0080).  
The factor is calculated from the set scaling factors of the follower drive objects
(p31744) plus 100 % from the master drive object.  
Example:  
Master drive object: p31744 = 100 % (reference value)  
Follower drive object 1: p31744 = 100 %  
Follower drive object 2: p31744 = 100 %  
Follower drive object 3: p31744 = 100 %  
Follower drive object 4: p31744 = 50 %  
--&gt; Master drive object: r31753 = 450 %

**Dependency:**
  
  
Refer to:
p31744

**Note:**
  
This parameter is only relevant for master drive objects. It is always 0 for a follower
drive object.

#### r31753 SERVCOUP master scaling factor total display

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**3 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**SERVO (Lin) | **P-Group:**- | **Version:**1201100 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [%] | - [%] | [ ] - [%] |
| [Alarms](Technology%20Extension%20SERVCOUP%20V1.20.14.md#technology-extension-servcoup-v12014) |  |  |

**Valid as of version:**
  
1.2

**Description:**
  
Displays the scaling factor for the total force of the drive group.  
Using this factor, the total force of the drive group can be calculated from the master
drive object force. The scaling factor is valid for setpoint and actual value (r0079,
r0080).  
The factor is calculated from the set scaling factors of the follower drive objects
(p31744) plus 100 % from the master drive object.  
Example:  
Master drive object: p31744 = 100 % (reference value)  
Follower drive object 1: p31744 = 100 %  
Follower drive object 2: p31744 = 100 %  
Follower drive object 3: p31744 = 100 %  
Follower drive object 4: p31744 = 50 %  
--&gt; Master drive object: r31753 = 450 %

**Dependency:**
  
  
Refer to:
p31744

**Note:**
  
This parameter is only relevant for master drive objects. It is always 0 for a follower
drive object.

### p31754 SERVCOUP follower ASM slip controller integral time

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**4 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**SERVO | **P-Group:**- | **Version:**1201100 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 [ms] | 250.00 [ms] | [ 0 ] 12.00 [ms] |
| [Alarms](Technology%20Extension%20SERVCOUP%20V1.20.14.md#technology-extension-servcoup-v12014) |  |  |

**Valid as of version:**
  
1.2

**Description:**
  
Sets the integral time for the slip controller of the master and follower drive object.  
The angle of slip difference between master and follower drive object is corrected
on the angle offset p31748. The values of the slip controller are displayed in parameter
r31755.

**Recommend.:**
  
Recommended initial value: p31754 = 12 ms.

**Dependency:**
  
  
Refer to:
p31748, r31755

**Notice:**
  
Possible effects if parameter assignments are inappropriate:  
- If the integral time is too long, the slip controller is too slow and the angle
of slip difference can increase. This can produce different torques at the master
and follower drive object.  
- If the integral time is too short, the angle of slip difference can oscillate and
the control can become unstable.

**Note:**
  
The parameter is only relevant for follower drive objects and should only be used
for induction motors of identical design.

### r31755[0...1] SERVCOUP follower ASM slip controller display

|  |  |  |
| --- | --- | --- |
| **Can be changed:**- | **Calculated:**- | **Access level:**4 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**SERVO | **P-Group:**- | **Version:**1201100 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - [°] | - [°] | [ ] - [°] |
| [Alarms](Technology%20Extension%20SERVCOUP%20V1.20.14.md#technology-extension-servcoup-v12014) |  |  |

**Valid as of version:**
  
1.2

**Description:**
  
Display of the input and output of the slip controller.

**Index:**
  
[
0]:
Slip controller input  
[
1]:
Slip controller output

**Dependency:**
  
  
Refer to:
p31748, p31754

**Note:**
  
For index 0:  
Displays the angle difference between master and follower drive object minus the angle
offset r31748.  
For index 1:  
Displays the integrator value at the output of the slip controller. This is added
to the commutation angle r0093 of the follower drive object.  
  
This parameter is only displayed on the particular follower drive object and only
for induction motors.  
Otherwise it is always 0.

### p31756 CI: SERVCOUP follower supplementary torque signal source

[SERVO](#p31756-ci-servcoup-follower-supplementary-torque-signal-source-1)

[SERVO Linear motor](#p31756-ci-servcoup-follower-supplementary-force-signal-source)

#### p31756 CI: SERVCOUP follower supplementary torque signal source

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C1( 3) | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**SERVO | **P-Group:**- | **Version:**1201100 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**p2003 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](Technology%20Extension%20SERVCOUP%20V1.20.14.md#technology-extension-servcoup-v12014) |  |  |

**Valid as of version:**
  
1.2

**Description:**
  
Sets the signal source for a supplementary torque at the follower drive object.  
The value of the signal source is multiplied by the scaling factor p31744 and then
added to the torque setpoint.

**Recommend.:**
  
The set supplementary torque r31756 only acts on this drive object, but influences
the behavior of the complete group.  
p1511 of the master drive object should be used for identical supplementary torques
at all coupled drive objects.

**Dependency:**
  
  
Refer to:
p31744

**Note:**
  
This parameter is only active for the particular follower drive object.

#### p31756 CI: SERVCOUP follower supplementary force signal source

|  |  |  |
| --- | --- | --- |
| **Can be changed:** C1( 3) | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**SERVO (Lin) | **P-Group:**- | **Version:**1201100 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**p2003 | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](Technology%20Extension%20SERVCOUP%20V1.20.14.md#technology-extension-servcoup-v12014) |  |  |

**Valid as of version:**
  
1.2

**Description:**
  
Sets the signal source for a supplementary force at the follower drive object.  
The value of the signal source is multiplied by the scaling factor p31744 and then
added to the force setpoint.

**Recommend.:**
  
The set supplementary force r31756 only acts on this drive object, but influences
the behavior of the complete group.  
p1511 of the master drive object should be used for identical supplementary forces
at all coupled drive objects.

**Dependency:**
  
  
Refer to:
p31744

**Note:**
  
This parameter is only active for the particular follower drive object.

### p31757 BI: SERVCOUP follower disturbing torque copying signal source

[SERVO](#p31757-bi-servcoup-follower-disturbing-torque-copying-signal-source-1)

[SERVO Linear motor](#p31757-bi-servcoup-follower-disturbing-force-copying-signal-source)

#### p31757 BI: SERVCOUP follower disturbing torque copying signal source

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**SERVO | **P-Group:**- | **Version:**1201100 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](Technology%20Extension%20SERVCOUP%20V1.20.14.md#technology-extension-servcoup-v12014) |  |  |

**Valid as of version:**
  
1.2

**Description:**
  
Sets the signal source to copy the disturbing torque.  
When function generator/metering functions are used, the follower drive object may
be loaded with the disturbing torque of the master drive object (r1651).  
The disturbing torque of the follower drive object is additionally scaled using p31744.  
For p31757 = 0 signal, the following applies:  
- Master drive object disturbing torque is not copied.  
For p31757 = 1 signal, the following applies:  
- r1651 of master drive object is scaled using p31744 and acts on the follower drive
object as function generator torque setpoint r1651.  
- Status bit r31750.7 = 1

**Dependency:**
  
  
Refer to:
p31744

**Note:**
  
This parameter is only relevant for follower drive objects.

#### p31757 BI: SERVCOUP follower disturbing force copying signal source

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**3 |
| **Data type:**Unsigned32 / Binary | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**SERVO (Lin) | **P-Group:**- | **Version:**1201100 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| - | - | [ 0 ] 0 |
| [Alarms](Technology%20Extension%20SERVCOUP%20V1.20.14.md#technology-extension-servcoup-v12014) |  |  |

**Valid as of version:**
  
1.2

**Description:**
  
Sets the signal source to copy the disturbing force.  
When function generator/metering functions are used, the follower drive object may
be loaded with the disturbing force of the master drive object (r1651).  
The disturbing force of the follower drive object is additionally scaled using p31744.  
For p31757 = 0 signal, the following applies:  
- No disturbing force of the master drive object is copied.  
For p31757 = 1 signal, the following applies:  
- r1651 of master drive object is scaled using p31744 and acts on the follower drive
object as function generator force setpoint r1651.  
- Status bit r31750.7 = 1

**Dependency:**
  
  
Refer to:
p31744

**Note:**
  
This parameter is only relevant for follower drive objects.

### p31758 SERVCOUP master torque coupling tolerance permissible

[SERVO](#p31758-servcoup-master-torque-coupling-tolerance-permissible-1)

[SERVO Linear motor](#p31758-servcoup-master-force-coupling-tolerance-permissible)

#### p31758 SERVCOUP master torque coupling tolerance permissible

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**4 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**SERVO | **P-Group:**- | **Version:**1201100 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 [%] | 50.00 [%] | [ 0 ] 10.00 [%] |
| [Alarms](Technology%20Extension%20SERVCOUP%20V1.20.14.md#technology-extension-servcoup-v12014) |  |  |

**Valid as of version:**
  
1.2

**Description:**
  
Sets the tolerance of the torque actual values of all coupled follower drive objects.  
The percentage value refers to the current torque actual value r0080 of the master
drive object.  
  
If the absolute deviation between master and follower torque actual values is smaller
than the set tolerance, r31750.10 = 1 is set.  
An overshoot or undershoot of the follower torque actual value to the master torque
actual value by the set tolerance sets bit r31750.10 = 0.  
  
The torque scaling r31744 of the follower drive objects is taken into account.  
The follower supplementary torque p31756 is not monitored. When interconnecting p31756,
the percentage value p31758 must be increased if necessary.

**Dependency:**
  
  
Refer to:
p31744, r31750, r31752, p31756

**Note:**
  
This parameter is only relevant for a master drive object.

#### p31758 SERVCOUP master force coupling tolerance permissible

|  |  |  |
| --- | --- | --- |
| **Can be changed:**T | **Calculated:**- | **Access level:**4 |
| **Data type:**FloatingPoint32 | **Dynamic index:**- | **Func. diagram:** - |
| **Object:**SERVO (Lin) | **P-Group:**- | **Version:**1201100 |
| **Units group:**- | **Unit selection:**- |  |
| **Not for motor type:**- | **Scaling:**- | **Expert list:**1 |
| **Min** | **Max** | **Factory setting** |
| 0.00 [%] | 50.00 [%] | [ 0 ] 10.00 [%] |
| [Alarms](Technology%20Extension%20SERVCOUP%20V1.20.14.md#technology-extension-servcoup-v12014) |  |  |

**Valid as of version:**
  
1.2

**Description:**
  
Sets the tolerance of the force actual values of all coupled follower drive objects.  
The percentage value refers to the current force actual value r0080 of the master
drive object.  
  
If the absolute deviation between master and follower force actual values is smaller
than the set tolerance, r31750.10 = 1 is set.  
An overshoot or undershoot of the follower force actual value to the master force
actual value by the set tolerance sets bit r31750.10 = 0.  
  
The force setpoint scaling r31744 of the follower drive objects is taken into account.  
The follower supplementary force p31756 is not monitored. When interconnecting p31756,
the percentage value p31758 must be increased if necessary.

**Dependency:**
  
  
Refer to:
p31744, r31750, r31752, p31756

**Note:**
  
This parameter is only relevant for a master drive object.

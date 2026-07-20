---
title: "Technology Extension SERVCOUP V1.20.14"
package: sdralSERVCOUP_1_20_14enUS
topics: 6
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Technology Extension SERVCOUP V1.20.14

This section contains the alarm descriptions for the Technology Extension.
In the table of contents, you will then see a separate entry for each alarm number.

## SINAMICS Alarms SERVCOUP 53470 - 53475

SINAMICS Alarms SERVCOUP 53470 - 53475

### A53470 SERVCOUP configuration error

**Drive object:**
  
SERVO

**Valid as of version:**
  
1.2

**Message value:**
  
%1

| Symbol | Meaning |
| --- | --- |
| **Component:** Motor | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The configuration of the SERVCOUP Technology Extension is incorrect.  
In this state, the servo coupling is not ready for operation, and can only be activated
once the cause has been resolved.  
Alarm value (r2124, interpret decimal):  
1: No master drive object set, or drive object is not interconnected with another
master drive object via p31746.  
2: No follower drive object set.  
3: The drive object number of the master drive object is larger than that of the follower
drive object.  
4: No encoder is set on the master drive object.  
6: The master drive object is interconnected with another master drive object via
p31746.  
7: The rule p0115[0] = p0115[1] has been violated on at least one of the drive objects
involved.  
8: On the master drive object, p1460[D] is set to > 0.0 or p1462[D] is set to > 0.0.  
9: Parameter p0115[0] or p0115[1] is different on the master drive object and follower
drive object.  
10: Number of data sets (p0180) is different on the master drive object and follower
drive object.  
11: Motor type p31743 is different between the master drive object and follower drive
object.  
12: Parameter p1815.0 is different on the follower drive object and master drive object.  
13: Parameter p1816 is different on the follower drive object and master drive object.  
14: Parameter p1819 is different on the follower drive object and master drive object.  
15: A speed or velocity to monitor the enable signal is set in parameter p31742. However,
no propagation of faults was set in parameter p31749.  
16: Parameter p0300 of the master drive object is not identical for all MDS. The configured
motor type (SM / ASM) differs between the MDS of the same motor module.  
17: Parameter p0300 differs between master and follower drive objects. The configured
motor type (SM / ASM) differs between the MDS on at least one follower drive object.  
18: Parameter p0290 value 2, 3, 12, 13 not permissible.  
19: Parameter p0290 is different on the master drive object and follower drive object.  
  
Note:  
This alarm can also initiate the display of incorrectly set parameters in r31751.  
MDS: Motor Data Set

**Remedy:**
  
For alarm value = 1:  
For a drive object, set the operating mode – master drive object (p31740 = 1).  
For alarm value = 2:  
For one or several drive objects, set the operating mode – follower drive object (p31740
= 2).  
For alarm value = 3:  
Use the drive object with the lowest drive object number as master drive object (p31740).  
For alarm value = 4:  
For the master drive object, correctly set the number of encoders (p31741).  
For alarm value = 6:  
For the master drive object, deactivate the coupling to an additional drive object
(p31746 = 0).  
For alarm value = 7:  
Set p0115[0] = p0115[1] on all of the drive objects involved.  
For alarm value = 8:  
On the follower drive objects, set p1460[D] = p1462[D] = 0.0 in all drive data sets
(DDS).  
For alarm value = 9:  
On all of the follower drive objects involved, set p0115[0] and p0115[1] the same
as the master drive object.  
For alarm value = 10:  
Set the number of drive data sets (p0180) the same on all drive objects involved.  
For alarm value = 11:  
On all follower drive objects, set p31743 the same as the master drive object.  
For alarm value = 12:  
Set parameter p1815.0 the same on all of the drive objects involved.  
For alarm value = 13:  
Set parameter p1816 the same on all of the drive objects involved.  
For alarm value = 14:  
Set parameter p1819 the same on all of the drive objects involved.  
For alarm value = 15:  
Set an appropriate propagation in parameter p31749, or with p31742 = 0, deactivate
monitoring the enable signal.  
For alarm value = 16:  
In parameter p300 of the master drive object, configure the same motor type for all
MDS.  
For alarm value = 17:  
In parameter p0300 of all follower drive objects, configure the same motor type as
that of the master drive object for all MDS.  
For alarm value = 18:  
In parameter p0290 of all master and follower drive objects, configure another power
unit overload response with the value 0, 1 or 10.  
For alarm value = 19:  
Set parameter p0290 the same on all of the drive objects involved.  
  
Note:  
SERVCOUP: SERVO COUPLING (SERVO coupling)  
MDS: Motor Data Set  
See also: p31740, p31741, p31743, r31745, p31746, r31751

### F53471 SERVCOUP fault detected at the drive object

**Drive object:**
  
SERVO

**Valid as of version:**
  
1.2

**Message value:**
  
%1

| Symbol | Meaning |
| --- | --- |
| **Component:** Motor | **Propagation:** GLOBAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A fault with pulse cancellation was detected on a drive object. As a consequence,
a fault was output at all coupled drive objects.  
Fault value (r0949, interpret decimal):  
Drive object number.  
Note:  
This fault can only be acknowledged at all of the other drive objects if, at the specified
drive object, the cause of the fault was removed.  
This fault can occur as response to F53475.  
See also: p31749 (SERVCOUP master alarm propagation)

**Remedy:**
  
Resolve the fault at the specified drive object and acknowledge.  
Note:  
SERVCOUP: SERVO COUPLING (SERVO coupling)

### F53473 SERVCOUP follower maximum velocity exceeded

**Drive object:**
  
SERVO

**Valid as of version:**
  
1.2

**Message value:**
  
-

| Symbol | Meaning |
| --- | --- |
| **Component:** Power Module | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The maximum speed or maximum velocity set in p31742 on a follower drive object that
has not been enabled has been exceeded. As a consequence, this fault is output at
the master drive object.  
See also: p31742

**Remedy:**
  
- Check enable signals for the follower drive object and activate if necessary.  
- Resolve the cause of the fault on the follower drive object.  
- Check the setting of the maximum speed or maximum velocity in p31742 and change
it if necessary.  
Note:  
SERVCOUP: SERVO COUPLING (SERVO coupling)

### F53475 SERVCOUP fault detected on the follower drive object

**Drive object:**
  
SERVO

**Valid as of version:**
  
1.2

**Message value:**
  
%1

| Symbol | Meaning |
| --- | --- |
| **Component:** Motor | **Propagation:** GLOBAL |

  

**Reaction:**
  
 OFF3

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A fault with pulse cancellation was detected on a follower drive object. As a consequence,
a fault was output by the master drive object.  
Fault value (r0949, interpret decimal):  
Drive object number.  
Note:  
This fault can only be acknowledged at the master drive object if, at the specified
drive object, the cause of the fault was removed.  
This fault sets fault F53471 at all associated follower drive objects.  
See also: p31749 (SERVCOUP master alarm propagation)

**Remedy:**
  
Resolve the fault at the specified follower drive object and acknowledge.  
Note:  
SERVCOUP: SERVO COUPLING (SERVO coupling)

---
title: "Technology Extension VIBX V1.30.11"
package: sdralVIBX_1_30_11enUS
topics: 6
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Technology Extension VIBX V1.30.11

This section contains the alarm descriptions for the Technology Extension.
In the table of contents, you will then see a separate entry for each alarm number.

## SINAMICS Alarms VIBX 53430 - 53434

SINAMICS Alarms VIBX 53430 - 53434

### F53430 VIBX EPOS not activated

**Drive object:**
  
All objects

**Valid as of version:**
  
1.4

**Message value:**
  
-

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
In the application mode "EPOS and LR" (p31580 = 1), it was identified that the function
module "Basic positioner, EPOS" (r0108.4) is not activated.  
The function module "Basic positioner, EPOS" must be activated in this application
mode.

**Remedy:**
  
Activate the function module "Basic positioner, EPOS" (r0108.4).  
Note:  
VIBX: VIBration eXtinction (vibration absorber)

### F53432 VIBX frequency fd > Shannon frequency

**Drive object:**
  
All objects

**Valid as of version:**
  
1.4

**Message value:**
  
-

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The VIBX filter frequency is greater than the Shannon frequency.  
The Shannon frequency is calculated according to the following formula:  
Shannon frequency = 0.5 / r31587

**Remedy:**
  
Reduce the VIBX filter frequency (p31585).  
Note:  
VIBX: VIBration eXtinction (vibration absorber)

### A53433 (F) VIBX configuration not complete/configuration missing

**Drive object:**
  
All objects

**Valid as of version:**
  
1.4

**Message value:**
  
-

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The VIBX technology extension is activated. However, an application mode has still
not been set (p31580 = 0).  
The following signals are constantly evaluated:  
r32600.8 = 1, r31601 = r31602 = r31603 = 0  
See also: p31580 (VIBX application mode)

**Remedy:**
  
Set the required application mode (p31580 &gt; 0).  
Note:  
VIBX: VIBration eXtinction (vibration absorber)

Reaction upon F:  
 OFF2

Acknowl. upon F:  
IMMEDIATELY

### A53434 (F) VIBX not sufficient system memory

**Drive object:**
  
All objects

**Valid as of version:**
  
1.4

**Message value:**
  
-

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The VIBX technology extension cannot be activated due to lack of memory.  
The following signals are constantly evaluated:  
r32600.8 = 1, r31601 = r31602 = r31603 = 0  
See also: p31580 (VIBX application mode)

**Remedy:**
  
- de-activate unused technology extensions.  
- de-activate unused DCC charts.  
Note:  
VIBX: VIBration eXtinction (vibration absorber)

Reaction upon F:  
 OFF2

Acknowl. upon F:  
IMMEDIATELY

---
title: "Technology Extension SETPGEN V1.30.11"
package: sdralSETPGEN_1_30_11enUS
topics: 3
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Technology Extension SETPGEN V1.30.11

This section contains the alarm descriptions for the Technology Extension.
In the table of contents, you will then see a separate entry for each alarm number.

## SINAMICS Alarms SETPGEN 53340 - 53340

SINAMICS Alarms SETPGEN 53340 - 53340

### A53340 SETPGEN frequency limiting active

**Drive object:**
  
All objects

**Valid as of version:**
  
1.3

**Message value:**
  
-

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The reference frequency set in parameter p31205 exceeds the maximum possible frequency.  
Due to the sampling theorem, the frequency is limited to half of the sampling rate.
The sampling rate can be set via parameter p31200.

**Remedy:**
  
To increase the maximum possible reference frequency, the sampling time in parameter
p31200 must be reduced.

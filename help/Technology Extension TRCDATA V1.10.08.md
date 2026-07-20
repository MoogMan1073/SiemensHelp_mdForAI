---
title: "Technology Extension TRCDATA V1.10.08"
package: sdralTRCDATA_1_10_08enUS
topics: 4
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Technology Extension TRCDATA V1.10.08

This section contains the alarm descriptions for the Technology Extension.
In the table of contents, you will then see a separate entry for each alarm number.

## SINAMICS Alarms TRCDATA 53510 - 53511

SINAMICS Alarms TRCDATA 53510 - 53511

### A53510 TRCDATA: maximum number of configuration attributes exceeded

**Drive object:**
  
General OA obj

**Valid as of version:**
  
1.1

**Message value:**
  
-

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The setting exceeds the maximum number of signals and data points to be recorded.
The sum of the configuration attributes across all drive objects has exceeded the
value of 325000.  
For each drive object, the configuration attribute is calculated based on the following
formula:  
Configuration attribute = p32044 * (p32045 + p32046) / p32040  
Note:  
No signals are recorded when this alarm is active.  
See also: p32040 (TRCDATA recording mode), p32044 (TRCDATA trace buffer number of data points),
p32045 (TRCDATA float signal sources number), p32046 (TRCDATA integer signal sources
number), r32056 (TRCDATA status word)

**Remedy:**
  
- Reduce the number of signals to be recorded (p32045, p32046).  
- Reduce the number of data points (p32044).  
- If required change the recording mode to "Single" (p32040).  
- If required reduce the number of drive objects with TRCDATA activated.  
Note:  
TRCDATA: Trace Data (data recording)  
Refer to parameter p32044 for examples of valid maximum configurations.

### A53511 TRCDATA: remaining memory critical

**Drive object:**
  
General OA obj

**Valid as of version:**
  
1.1

**Message value:**
  
-

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
When the Control Unit ran up it was identified that the remaining system memory had
reached a critical size.  
It is possible that system functions are restricted.

**Remedy:**
  
- Reduce the set values for the following parameters: p32044, p32045, p32046  
- If required change the recording mode to "Single" (p32040).  
- If required deactivate the OA application TRCDATA.  
Note:  
TRCDATA: Trace Data (data recording)  
See also: p32040 (TRCDATA recording mode), p32044 (TRCDATA trace buffer number of data points),
p32045 (TRCDATA float signal sources number), p32046 (TRCDATA integer signal sources
number)

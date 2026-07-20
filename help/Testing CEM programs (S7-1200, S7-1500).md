---
title: "Testing CEM programs (S7-1200, S7-1500)"
package: ProgTestCEMenUS
topics: 5
devices: [S7-1200, S7-1500, S7-1500T]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Testing CEM programs (S7-1200, S7-1500)

This section contains information on the following topics:

- [Basic information on testing CEM (S7-1200, S7-1500)](#basic-information-on-testing-cem-s7-1200-s7-1500)
- [Program status for causes and effects (S7-1200, S7-1500)](#program-status-for-causes-and-effects-s7-1200-s7-1500)
- [Program status display for intersections (S7-1200, S7-1500)](#program-status-display-for-intersections-s7-1200-s7-1500)
- [Examples of program status display in CEM (S7-1200, S7-1500)](#examples-of-program-status-display-in-cem-s7-1200-s7-1500)

## Basic information on testing CEM (S7-1200, S7-1500)

### Overview

You can display the program status of a CEM program to check the logic, consistency and function of the program.

To be able to test a user program, an online connection to the CPU must be available.

| Symbol | Meaning |
| --- | --- |
|  | **Danger** |
| **Danger when testing during plant operation**  Changing of the tag values during plant runtime can result in inconsistencies between the program and the actual process. This can cause serious damage to property and personal injury.   - Make sure that the plant is in a safe state before you overwrite the tag values. - Make sure that snapshots are taken at a time when the system was in a safe state. - Select individual tags as setpoints to selectively edit the actual values of these tags in the online program. - Make sure that the program does not read or write the affected data during transmission. - You may want to use the "Modify tag" function in the watch table or in the DB editor as an alternative. |  |

### Test functions of CEM

The following test functions are available for testing a cause-effect matrix:

- Program status for causes, intersections and effects

  In the program status you can see which causes, effects and intersections are active or inactive. This allows you to find and fix logical errors in your program.

  See also:

  [Program status for causes and effects](#program-status-for-causes-and-effects-s7-1200-s7-1500)

  [Program status display for intersections](#program-status-display-for-intersections-s7-1200-s7-1500)
- Testing with the watch table

  With the watch table, you can monitor and modify the current values of multiple tags in the user program or on a CPU. You can assign values to tags for testing and run the program in a variety of different situations. You can also assign fixed values to the I/O outputs of a CPU in STOP mode, for example to check the wiring.

  See also: [Introduction to testing with the watch table](Testing%20with%20the%20watch%20table.md#introduction-to-testing-with-the-watch-table)
- Testing with the force table

  With the force table, you can monitor and force the current values of multiple tags in the user program or on a CPU. When you force, you overwrite individual tags with specified values. This allows you to test your user program and run through various situations.

  See also: [Introduction for testing with the force table](Testing%20with%20the%20force%20table.md#introduction-for-testing-with-the-force-table)

### General Information on testing user programs

General information on testing user programs can be found in the section "Testing the user program".

See also: [Testing with program status](Testing%20the%20user%20program.md#testing-with-program-status)

## Program status for causes and effects (S7-1200, S7-1500)

### Displays in the program status

You can display the program status of causes and effects to monitor the program sequence. The program status is updated cyclically.

The display corresponds to the program status display for FBD programs:

- Green markings indicate that a signal state of "1" is pending at the element.
- Blue markings indicate the signal state "0".
- The values of the operands are displayed above the operand in a gray box.
- The current timer values are displayed in the top left area of the cause.

### Program status for causes

The following table shows the display of the program status for causes:

| Representation | Program status |
| --- | --- |
| ![Program status for causes](images/140011631243_DV_resource.Stream@PNG-de-DE.png) | The cause is inactive. The signal state at the output of the cause is "0". |
| ![Program status for causes](images/140011686155_DV_resource.Stream@PNG-de-DE.png) | The cause is active. The signal state at the output of the cause is "1". |

The following table shows the display of the program status for causes with a programmed time delay:

| Representation | Program status |
| --- | --- |
| ![Program status for causes](images/140210536459_DV_resource.Stream@PNG-de-DE.png) | The condition of the cause is satisfied.  The programmed time delay has not expired yet.  The signal state at the output of the cause is 0. |
| ![Program status for causes](images/140210543883_DV_resource.Stream@PNG-de-DE.png) | The condition of the cause is satisfied.  The programmed time delay has expired.  The signal state at the output of the cause is "1". |

The following table shows the display of the program status for causes with inverted output:

| Representation | Program status |
| --- | --- |
| ![Program status for causes](images/140011696779_DV_resource.Stream@PNG-de-DE.png) | The signal state at the input of the cause is "1". The condition of the cause is satisfied.  The signal at the output of the cause is inverted, however, and transferred as a "0" signal to the intersection.  The intersection is not active. |

### Program status for effects

The following table shows the program status for effects:

| Representation | Program status |
| --- | --- |
| ![Program status for effects](images/140011815435_DV_resource.Stream@PNG-de-DE.png) | The signal state at the input of the effect is "0".  The effect is not active. |
| ![Program status for effects](images/140011819147_DV_resource.Stream@PNG-de-DE.png) | The signal state at the input of the effect is "1".  The effect is active. |

The following table shows the program status for effects with inverted input:

| Representation | Program status |
| --- | --- |
| ![Program status for effects](images/140011822859_DV_resource.Stream@PNG-de-DE.png) | The signal state at the input of the effect is "1" but is inverted and transferred as "0" signal to the effect.   The effect is not active. |

---

**See also**

[Testing with program status](Testing%20the%20user%20program.md#testing-with-program-status)
  
[Program status display for intersections (S7-1200, S7-1500)](#program-status-display-for-intersections-s7-1200-s7-1500)
  
[Examples of program status display in CEM (S7-1200, S7-1500)](#examples-of-program-status-display-in-cem-s7-1200-s7-1500)

## Program status display for intersections (S7-1200, S7-1500)

### Displays in the program status

You can read out the following information in the program status display of intersections:

- The filling shows the status of the intersection.

  - Active intersections have a green filling.
  - Inactive intersections have a blue filling.
- The border indicates whether the intersection has an influence on the effect.

  - Intersections with a green border set the effect to "1".
  - A blue border shows that the effect is set to "0".
  - A gray border indicates that the intersection does not influence the effect because the intersection is not active or the column contains active intersections with a higher priority.

### Program status for intersections

The following table shows the display of the program status for intersections with the N action:

| Representation | Program status |
| --- | --- |
| ![Program status for intersections](images/138178355339_DV_resource.Stream@PNG-de-DE.png) | The intersection is active and sets the effect to "1". |
| ![Program status for intersections](images/138178359051_DV_resource.Stream@PNG-de-DE.png) | The intersection is active and resets the effect to "0". |

The following table shows the display of the program status for intersections with the S action:

| Representation | Program status |
| --- | --- |
| ![Program status for intersections](images/138173316235_DV_resource.Stream@PNG-de-DE.png) | The intersection is active and sets the effect to "1". |
| ![Program status for intersections](images/138173323659_DV_resource.Stream@PNG-de-DE.png) | The intersection is not active. |
| ![Program status for intersections](images/138173621771_DV_resource.Stream@PNG-de-DE.png) | The intersection was active in an earlier cycle and set the effect to "1". The effect was not been reset since then. |

The following table shows the display of the program status for intersections with the R action:

| Representation | Program status |
| --- | --- |
| ![Program status for intersections](images/138173625483_DV_resource.Stream@PNG-de-DE.png) | The intersection is active and sets the effect permanently to "0". |
| ![Program status for intersections](images/138168140939_DV_resource.Stream@PNG-de-DE.png) | The intersection is active but does not influence the effect because the column contains active intersections with a higher priority. |
| ![Program status for intersections](images/138173629195_DV_resource.Stream@PNG-de-DE.png) | The intersection is not active. |

The following table shows the display of the program status for action groups:

| Representation | Program status |
| --- | --- |
| ![Program status for intersections](images/138173658507_DV_resource.Stream@PNG-de-DE.png) | The required number of intersections in the action group is active and sets the effect to "1". |
| ![Program status for intersections](images/138173662219_DV_resource.Stream@PNG-de-DE.png) | The required number of intersections in the action group is reset active.  The effect is set to "0". |
| ![Program status for intersections](images/138173665931_DV_resource.Stream@PNG-de-DE.png) | The actual intersection is active. However, the action group is only partially fulfilled, as not all required intersections in the group are active.  The effect is set to "0". |
| ![Program status for intersections](images/138173669643_DV_resource.Stream@PNG-de-DE.png) | The required number of intersections in the action group is active and sets the effect permanently to "1". |
| ![Program status for intersections](images/138173686155_DV_resource.Stream@PNG-de-DE.png) | The actual intersection is active. However, the action group is only partially fulfilled as not all required intersections in the group are active.  The effect is set permanently to "1" when the required number is reached. |
| ![Program status for intersections](images/138173689867_DV_resource.Stream@PNG-de-DE.png) | The intersection is not active. |
| ![Program status for intersections](images/138168149131_DV_resource.Stream@PNG-de-DE.png) | The required number of intersections in the action group is active.   Some of the intersections were set to "1" in the current cycle. The signal was set in an earlier cycle for a part of the intersections.   The effect is permanently set to "1". |
| ![Program status for intersections](images/138173693579_DV_resource.Stream@PNG-de-DE.png) | The required number of intersections in the action group is active and sets the effect permanently to "0". |
| ![Program status for intersections](images/138173710091_DV_resource.Stream@PNG-de-DE.png) | The actual intersection is active. However, the action group is only partially fulfilled, as not all required intersections in the group are active.   The effect is set permanently to "0" with memory when the required number is reached and no higher-priority actions are active in the column. |
| ![Program status for intersections](images/138173713803_DV_resource.Stream@PNG-de-DE.png) | The intersection is not active. |

---

**See also**

[Testing with program status](Testing%20the%20user%20program.md#testing-with-program-status)
  
[Program status for causes and effects (S7-1200, S7-1500)](#program-status-for-causes-and-effects-s7-1200-s7-1500)
  
[Examples of program status display in CEM (S7-1200, S7-1500)](#examples-of-program-status-display-in-cem-s7-1200-s7-1500)

## Examples of program status display in CEM (S7-1200, S7-1500)

### Example of the N action

The following example shows the program status of the N action:

| Representation | Description |
| --- | --- |
| ![Example of the N action](images/140212425867_DV_resource.Stream@PNG-en-US.png) | "Cause1" is active. The N action sets the signal state at the input of the effect to "1".  "Cause2" is not active. The N action sets the signal state at the input of the effect to "0". |

### Example for the interaction of the S and R actions

The following example shows the program status of the S and R actions:

| Representation | Description |
| --- | --- |
| ![Example for the interaction of the S and R actions](images/140012280203_DV_resource.Stream@PNG-en-US.png) | "Cause1" was active in an earlier cycle. S has set the signal state at the input of the effect permanently to "1".  In the current cycle neither "Cause1" nor "Cause2" are active, which means the signal state at the input of the effect remains set. The intersection that was responsible for setting the effect is highlighted in color.   When "Cause2" becomes active, the signal state is set permanently to "0". |

### Example for the interaction of N, S and R actions

The following example shows how the N, S and R actions interact:

| Representation | Description |
| --- | --- |
| ![Example for the interaction of N, S and R actions](images/140012276491_DV_resource.Stream@PNG-en-US.png) | "Cause1" is reset active. However, the N action does not affect the signal state at the input of the effect, because the higher-priority S action is also active in the column.  "Cause2" is active. The S action sets the signal state at the input of the effect to "1".  "Cause3" is active. However, the R action does not affect the signal state at the input of the effect, because the higher-priority S action is also active in the column. |

### Example of the R action

The following example shows the program status of the R action:

| Representation | Description |
| --- | --- |
| ![Example of the R action](images/140012283915_DV_resource.Stream@PNG-en-US.png) | "Cause2" is active. The R action sets the signal state at the input of the effect permanently to "0". |

### Example for an action group

The following example shows the program status of an action group:

| Representation | Description |
| --- | --- |
| ![Example for an action group](images/140212398859_DV_resource.Stream@PNG-en-US.png) | "Cause1" and "Cause3" are active. The "3S" action sets the signal state at the input of the effect only permanently to "1" if at least three intersections from the action group are active. |

---

**See also**

[Program status display for intersections (S7-1200, S7-1500)](#program-status-display-for-intersections-s7-1200-s7-1500)
  
[Program status for causes and effects (S7-1200, S7-1500)](#program-status-for-causes-and-effects-s7-1200-s7-1500)

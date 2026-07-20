---
title: "PC systems"
package: ProgAWLShtDWN15enUS
topics: 2
source: Siemens TIA Portal Information System (offline help, en-US)
---


# PC systems

This section contains information on the following topics:

- [SHUT_DOWN: Shut down target system](#shut_down-shut-down-target-system)

## SHUT_DOWN: Shut down target system

### Description

You can use the instruction "SHUT_DOWN: Shut down target system" to shut down the PC-based automation system and restart the S7 software controller CPU 150xS or the operating system (Windows or Linux) on the PC-based automation system.

The instruction is available in the "Instructions" task card under Basic instructions > Program control > Runtime control.

A restart is, for example, advisable in the following situations:

- An industrial UPS (uninterruptible power supply) reports a power failure via a digital input.
- Operating system stops responding or

  - Windows operating system shows a "blue screen"
  - Linux operating system shows a "Kernel panic"
- Too many error OBs are called in the user program.

### **Parameter**

The following table shows the parameters of the "Shut down target system" instruction:

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Parameter** | **Declaration** | **Data type** | **Memory area** | **Description** | **Windows** | **Linux** |
| MODE | Input | UINT | I, Q, M, D, L or constant | MODE = 1: Shut down CPU 150xS and operating system. The CPU goes to STOP and saves the retentive data. Then the CPU and the operating system are shut down. The system must be restarted manually. | x | - |
| MODE = 2: Restart CPU 150xS. The CPU goes to STOP and saves the retentive data. Then the CPU is shut down and restarted. | x | x |  |  |  |  |
| MODE = 3: Restart operating system. The CPU remains in RUN. Operating system is restarted  (as of TIA Portal V14, MODE 3 is only retained for backward compatibility. We recommend using MODE 4 or MODE 5). | x | - |  |  |  |  |
| MODE = 4: Operating system is correctly shut down and restarted. The CPU remains in RUN. | x | - |  |  |  |  |
| MODE = 5: Restart operating system. (Comparable with MODE 3) **Exception:** MODE 5 should only be used if the operating system has crashed. | x | - |  |  |  |  |
| COMMENT | Input | STRING | I, Q, M, D, L | With Mode = 1, 3 and 4, you can specify a reason for the restart. The reason is shown in the Event Viewer.    **Only use the STRING data type.**   When using a data type other than STRING, note that the display in the Event Viewer **remains empty**. | x | - |
| Ret_Val | Return | WORD | Q, M, D, L | Ret_Val = 0: No faults | x | x |
| Ret_Val = 8090: The value passed to MODE is not supported. | x | x |  |  |  |  |
| Ret_Val = 8091: Operating system does not respond to the call of the Shut_Down instruction (only applies to Mode 3 and Mode 4). | x | - |  |  |  |  |
| Ret_Val = 8092: Please contact SIMATIC Customer Support if this error occurs (only applies to Mode 3 and Mode 4). | x | - |  |  |  |  |

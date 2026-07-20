---
title: "SINAMICS Alarms TM31 (Terminal Module)"
package: sdrMVal200enUS
topics: 469
source: Siemens TIA Portal Information System (offline help, en-US)
---


# SINAMICS Alarms TM31 (Terminal Module)

This section contains the alarm descriptions for the devices listed below. The alarm descriptions for the various devices can differ. If this is the case, then in the topic under "Drive object", the Control Unit is listed for which the description applies. In the table of contents, you will then see a separate entry for each alarm number. The following Control Units are taken into account in the online help:

- SINAMICS MV

## SINAMICS Alarms TM31 (Terminal Module) 01000 - 01389

SINAMICS Alarms TM31 (Terminal Module) 01000 - 01389

### F01000 Internal software error

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Module: %1, line: %2

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** GLOBAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
POWER ON

**Cause:**
  
An internal software error has occurred.  
Fault value (r0949, interpret hexadecimal):  
Only for internal Siemens troubleshooting.

**Remedy:**
  
- Evaluate fault buffer (r0945).  
- Carry out a POWER ON (switch-off/switch-on) for all components.  
- If required, check the data on the non-volatile memory (e.g. memory card).  
- Upgrade firmware to later version.  
- Contact Technical Support.  
- Replace the Control Unit.

### F01001 FloatingPoint exception

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** GLOBAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
POWER ON

**Cause:**
  
An exception occurred for an operation with floating point data type.  
The error can be caused by the basic system or a technology function (e.g. FBLOCKS,
DCC, TEC).  
Fault value (r0949, interpret hexadecimal):  
Only for internal Siemens troubleshooting.  
Note:  
Refer to r9999 for additional information about this fault.  
r9999[0]: Fault number.  
r9999[1]: Program counter at the time when the exception occurred.  
r9999[2]: Cause of the FloatingPoint exception.  
Bit 0 = 1: Operation invalid  
Bit 1 = 1: Division by zero  
Bit 2 = 1: Overflow  
Bit 3 = 1: Underflow  
Bit 4 = 1: Inaccurate result

**Remedy:**
  
- Carry out a POWER ON (switch-off/switch-on) for all components.  
- Check configuration and signals of the blocks in FBLOCKS.  
- Check configuration and signals of DCC charts.  
- Check configuration and signals of TEC charts.  
- Upgrade firmware to later version.  
- Contact Technical Support.

### F01002 Internal software error

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** GLOBAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
An internal software error has occurred.  
Fault value (r0949, interpret hexadecimal):  
Only for internal Siemens troubleshooting.

**Remedy:**
  
- Carry out a POWER ON (switch-off/switch-on) for all components.  
- Upgrade firmware to later version.  
- Contact Technical Support.

### F01003 Acknowledgment delay when accessing the memory

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** GLOBAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A memory area was accessed that does not return a "READY".  
Fault value (r0949, interpret hexadecimal):  
Only for internal Siemens troubleshooting.

**Remedy:**
  
- Carry out a POWER ON (switch-off/switch-on) for all components.  
- Contact Technical Support.

### N01004 (F, A) Internal software error

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
An internal software error has occurred.  
Fault value (r0949, hexadecimal):  
Only for internal Siemens troubleshooting.

**Remedy:**
  
- Read out diagnostics parameter (r9999).  
- Contact Technical Support.  
See also: r9999 (Software error internal supplementary diagnostics)

Reaction upon F:  
 OFF2

Acknowl. upon F:  
POWER ON

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

### F01005 Firmware download for DRIVE-CLiQ component unsuccessful

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, ENC, HUB, TB30, TECBASE, TM150, TM15DI_DO, TM31,
VECTOR3P, VECTORDM, VECTORGL, VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
2.6

**Message value:**
  
Component number: %1, fault cause: %2

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |
| %2 | 11 | DRIVE-CLiQ component has detected a checksum error. | After POWER ON has been carried out again for the DRIVE-CLiQ component, download firmware again. |
| 15 | The selected DRIVE-CLiQ component did not accept the contents of the firmware file. | Save suitable firmware file for download in the directory /siemens/sinamics/code/sac/. |  |
| 18 | Firmware version is too old and is not accepted by the component. | Save suitable firmware file for download in the directory /siemens/sinamics/code/sac/. |  |
| 19 | Firmware version is not suitable for the hardware release of the component. | Save suitable firmware file for download in the directory /siemens/sinamics/code/sac/. |  |
| 101 | After several communication attempts, no response from the DRIVE-CLiQ component. | Check the DRIVE-CLiQ wiring. |  |
| 139 | Initially, only one new boot loader was loaded. | After POWER ON has been carried out again for the DRIVE-CLiQ component, download firmware again. |  |
| 140 | Firmware file for the DRIVE-CLiQ component not available on the memory card. | Save suitable firmware file for download in the directory /siemens/sinamics/code/sac/. |  |
| 141 | An inconsistent length of the firmware file was signaled. | Save suitable firmware file for download in the directory /siemens/sinamics/code/sac. |  |
| 142 | Component has not changed to the mode for firmware download. | After POWER ON has been carried out again for the DRIVE-CLiQ component, download firmware again. |  |
| 156 | Component with the specified component number is not available (p7828). | Check the selected component number (p7828). |  |

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
It was not possible to download the firmware to a DRIVE-CLiQ component.  
Fault value (r0949, interpret hexadecimal):  
yyxxxx hex: yy = component number, xxxx = fault cause  
xxxx = 000B hex = 11 dec:  
DRIVE-CLiQ component has detected a checksum error.  
xxxx = 000F hex = 15 dec:  
The selected DRIVE-CLiQ component did not accept the contents of the firmware file.  
xxxx = 0012 hex = 18 dec:  
Firmware version is too old and is not accepted by the component.  
xxxx = 0013 hex = 19 dec:  
Firmware version is not suitable for the hardware release of the component.  
xxxx = 0065 hex = 101 dec:  
After several communication attempts, no response from the DRIVE-CLiQ component.  
xxxx = 008B hex = 139 dec:  
Initially, a new boot loader is loaded (must be repeated after POWER ON).  
xxxx = 008C hex = 140 dec:  
Firmware file for the DRIVE-CLiQ component not available on the memory card.  
xxxx = 008D hex = 141 dec:  
An inconsistent length of the firmware file was signaled. The firmware download may
have been caused by a loss of connection to the firmware file. This can occur during
a project download/reset in the case of a SINAMICS Integrated Control Unit, for example.  
xxxx = 008F hex = 143 dec:  
Component has not changed to the mode for firmware download. It was not possible to
delete the existing firmware.  
xxxx = 0090 hex = 144 dec:  
When checking the firmware that was downloaded (checksum), the component detected
a fault. It is possible that the file on the memory card is defective.  
xxxx = 0091 hex = 145 dec:  
Checking the loaded firmware (checksum) was not completed by the component in the
appropriate time.  
xxxx = 009C hex = 156 dec:  
Component with the specified component number is not available (p7828).  
xxxx = Additional values:  
Only for internal Siemens troubleshooting.

**Remedy:**
  
- Check the selected component number (p7828).  
- Check the DRIVE-CLiQ wiring.  
- Save suitable firmware file for download in the directory "/siemens/sinamics/code/sac/".  
- Use a component with a suitable hardware version  
- After POWER ON has been carried out again for the DRIVE-CLiQ component, download
firmware again. Depending on p7826, the firmware will be automatically downloaded.

### A01006 Firmware update for DRIVE-CLiQ component required

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Component number: %1

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The firmware of a DRIVE-CLiQ component must be updated as there is no suitable firmware
or firmware version in the component for operation with the Control Unit.  
Alarm value (r2124, interpret decimal):  
Component number of the DRIVE-CLiQ component.

**Remedy:**
  
Update the firmware using the commissioning tool:  
The firmware version of all of the components on the "Version overview" page can be
read in the Project Navigator under "Configuration" of the associated drive unit and
an appropriate firmware update can be carried out.  
Firmware update via parameter:  
- Take the component number from the alarm value and enter into p7828.  
- Start the firmware download with p7829 = 1.

### A01007 POWER ON for DRIVE-CLiQ component required

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Component number: %1

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
A DRIVE-CLiQ component must be switched on again (POWER ON) (e.g. due to a firmware
update).  
Alarm value (r2124, interpret decimal):  
Component number of the DRIVE-CLiQ component.  
Note:  
For a component number = 1, a POWER ON of the Control Unit is required.

**Remedy:**
  
- Switch off the power supply of the specified DRIVE-CLiQ component and switch it
on again.  
- For SINUMERIK, auto commissioning is prevented. In this case, a POWER ON is required
for all components and the auto commissioning must be restarted.

### A01009 (N) CU: Control module overtemperature

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Overtemperature of the electronic components (6)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The temperature (r0037[0]) of the control module (Control Unit) has exceeded the specified
limit value.

**Remedy:**
  
- Check the air intake for the Control Unit.  
- Check the Control Unit fan.  
Note:  
The alarm is automatically withdrawn once the limit value has been fallen below.

Reaction upon N:  
 NONE

Acknowl. upon N:  
NONE

### F01010 Drive type unknown

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
An unknown drive type was found.  
Fault value (r0949, interpret decimal):  
Drive object number (refer to p0101, p0107).

**Remedy:**
  
- Replace Power Module.  
- Carry out a POWER ON (switch-off/switch-on) for all components.  
- Upgrade firmware to later version.  
- Contact Technical Support.

### F01011 (N) Download interrupted

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The project download was interrupted.  
Fault value (r0949, interpret decimal):  
1: The user prematurely interrupted the project download.  
2: The communication cable was interrupted (e.g. cable breakage, cable withdrawn).  
3: The project download was prematurely exited by the commissioning tool.  
100: Different versions between the firmware version and project files which were
loaded by loading into the file system "Download from memory card".  
Note:  
The response to an interrupted download is the state "first commissioning".

**Remedy:**
  
- Check the communication cable.  
- Download the project again.  
- Boot from previously saved files (switch off / switch on or p0976).  
- When loading into the file system (download from memory card), use the matching
version.

Reaction upon N:  
 NONE

Acknowl. upon N:  
NONE

### F01014 Topology: DRIVE-CLiQ component property changed

**Drive object:**
  
All objects

**Valid as of version:**
  
5.2

**Message value:**
  
Component number: %1

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The properties of the DRIVE-CLiQ component have fundamentally changed.  
Fault value (r0949, interpret hexadecimal):  
Component number.

**Remedy:**
  
- Check the DRIVE-CLiQ component, and if required replace.  
- Carry out a warm restart (p0009 = 30, p0976 = 2, 3).

### F01015 Internal software error

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** GLOBAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
POWER ON

**Cause:**
  
An internal software error has occurred.  
Fault value (r0949, interpret decimal):  
Only for internal Siemens troubleshooting.

**Remedy:**
  
- Carry out a POWER ON (switch-off/switch-on) for all components.  
- Upgrade firmware to later version.  
- Contact Technical Support.

### A01016 (F) Firmware changed

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
At least one firmware file in the directory was illegally changed on the non-volatile
memory (memory card/device memory) with respect to the version when shipped from the
factory.  
Alarm value (r2124, interpret decimal):  
0: Checksum of one file is incorrect.  
1: File missing.  
2: File too many.  
3: Incorrect firmware version.  
4: Incorrect checksum of the back-up file.

**Remedy:**
  
For the non-volatile memory for the firmware (memory card/device memory), restore
the delivery condition.  
Note:  
The file involved can be read out using parameter r9925.  
The status of the firmware check is displayed using r9926.  
See also: r9925 (Firmware file incorrect), r9926 (Firmware check status)

Reaction upon F:  
 OFF2

Acknowl. upon F:  
POWER ON

### A01017 Component lists changed

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
On the memory card, one file in the directory /SIEMENS/SINAMICS/DATA or /ADDON/SINAMICS/DATA
has been illegally changed with respect to that supplied from the factory. No changes
are permitted in this directory.  
Alarm value (r2124, interpret decimal):  
xyz dec: x = problem, y = directory, z = file name  
x = 1: File does not exist.  
x = 2: Firmware version of the file does not match the software version.  
x = 3: File checksum is incorrect.  
y = 0: Directory /SIEMENS/SINAMICS/DATA/  
y = 1: Directory /ADDON/SINAMICS/DATA/  
z = 0: File MOTARM.ACX  
z = 1: File MOTSRM.ACX  
z = 2: File MOTSLM.ACX  
z = 3: File ENCDATA.ACX  
z = 4: File FILTDATA.ACX  
z = 5: File BRKDATA.ACX  
z = 6: File DAT_BEAR.ACX  
z = 7: File CFG_BEAR.ACX  
z = 8: File ENC_GEAR.ACX  
z = 9: File CFG_BRK.ACX  
z = 10: File THERMMOTMOD.ACX  
z = 11: File MAPPING.ACX  
z = 12: File LOADGEAR.ACX  
z = 13: File MOTRSM.ACX

**Remedy:**
  
For the file on the memory card involved, restore the status originally supplied from
the factory.

### A01019 Writing to the removable data medium unsuccessful

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, ENC, HUB, TB30, TECBASE, TM150, TM15DI_DO, TM31,
VECTOR3P, VECTORDM, VECTORGL, VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
4.4

**Message value:**
  
-

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The write access to the removable data medium was unsuccessful.

**Remedy:**
  
- Check the removable data medium and if required replace.  
- Disconnect any existing USB connection.  
- Repeat the data backup.

### A01020 Writing to RAM disk unsuccessful

**Drive object:**
  
All objects

**Valid as of version:**
  
4.4

**Message value:**
  
-

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
A write access to the internal RAM disk was unsuccessful.

**Remedy:**
  
Adapt the file size for the system logbook to the internal RAM disk (p9930).  
See also: p9930 (System logbook activation)

### F01023 Software timeout (internal)

**Drive object:**
  
All objects

**Valid as of version:**
  
4.4

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
An internal software timeout has occurred.  
Fault value (r0949, interpret decimal):  
Only for internal Siemens troubleshooting.

**Remedy:**
  
- Carry out a POWER ON (switch-off/switch-on) for all components.  
- Upgrade firmware to later version.  
- Contact Technical Support.

### A01032 (F) ACX: all parameters must be saved

**Drive object:**
  
All objects

**Valid as of version:**
  
4.5

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The parameters of an individual drive object were saved (p0971 = 1), although there
is still no backup of all drive system parameters.  
The saved object-specific parameters are not loaded the next time that the system
powers up.  
For the system to successfully power up, all of the parameters must have been completely
backed up.  
Alarm value (r2124, interpret decimal):  
Only for internal Siemens troubleshooting.  
See also: p0971 (Save drive object parameters)

**Remedy:**
  
Save all parameters (p0977 = 1 or "copy RAM to ROM").  
See also: p0977 (Save all parameters)

Reaction upon F:  
Vector: NONE (OFF1, OFF2, OFF3)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF1, OFF2)

Acknowl. upon F:  
IMMEDIATELY

### A01035 (F) ACX: Parameter back-up file corrupted

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
When the Control Unit was booted, no complete data set was found from the parameter
back-up files. The last time that the parameterization was saved, it was not completely
carried out.  
It is possible that the backup was interrupted by switching off or withdrawing the
memory card.  
Alarm value (r2124, interpret hexadecimal):  
ddccbbaa hex:  
aa = 01 hex:  
Power up was realized without data backup. The drive is in the factory setting.  
aa = 02 hex:  
The last available backup data record was loaded. The parameterization must be checked.
It is recommended that the parameterization is downloaded again.  
dd, cc, bb:  
Only for internal Siemens troubleshooting.  
See also: p0971 (Save drive object parameters), p0977 (Save all parameters)

**Remedy:**
  
- Download the project again using the commissioning tool.  
- Save all parameters (p0977 = 1 or "copy RAM to ROM").  
See also: p0977 (Save all parameters)

Reaction upon F:  
Vector: NONE (OFF1, OFF2, OFF3)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF1, OFF2)

Acknowl. upon F:  
IMMEDIATELY

### F01036 (A) ACX: Parameter back-up file missing

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** LOCAL |

  

**Reaction:**
  
Vector: NONE (OFF1, OFF2, OFF3)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF2)

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
When downloading the device parameterization, a parameter back-up file PSxxxyyy.ACX
associated with a drive object cannot be found.  
Fault value (r0949, interpret hexadecimal):  
Byte 1: yyy in the file name PSxxxyyy.ACX  
yyy = 000 --&gt; consistency back-up file  
yyy = 001 ... 062 --&gt; drive object number  
yyy = 099 --&gt; PROFIBUS parameter back-up file  
Byte 2, 3, 4:  
Only for internal Siemens troubleshooting.

**Remedy:**
  
If you have saved your project data using the commissioning tool, carry-out a new
download for your project.  
Save using the function "Copy RAM to ROM" or with p0977 = 1.  
This means that the parameter files are again completely written into the non-volatile
memory.  
Note:  
If the project data have not been backed up, then a new first commissioning is required.

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

### F01038 (A) ACX: Loading the parameter back-up file unsuccessful

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** LOCAL |

  

**Reaction:**
  
Vector: NONE (OFF1, OFF2, OFF3)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF2)

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
An error has occurred when downloading PSxxxyyy.ACX or PTxxxyyy.ACX files from the
non-volatile memory.  
Fault value (r0949, interpret hexadecimal):  
Byte 1: yyy in the file name PSxxxyyy.ACX  
yyy = 000 --&gt; consistency back-up file  
yyy = 001 ... 062 --&gt; drive object number  
yyy = 099 --&gt; PROFIBUS parameter back-up file  
Byte 2:  
255: Incorrect drive object type.  
254: Topology comparison unsuccessful -&gt; drive object type was not able to be identified.  
Reasons could be:  
- Incorrect component type in the actual topology  
- Component does not exist in the actual topology.  
- Component not active.  
Additional values:  
Only for internal Siemens troubleshooting.  
Byte 4, 3:  
Only for internal Siemens troubleshooting.

**Remedy:**
  
- If you have saved the project data using the commissioning tool, download the project
again. Save using the function "Copy RAM to ROM" or with p0977 = 1. This means that
the parameter files are again completely written to the non-volatile memory.  
- Replace the memory card or Control Unit.  
For byte 2 = 255:  
- Correct the drive object type (see p0107).

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

### F01039 (A) ACX: Writing to the parameter back-up file was unsuccessful

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** LOCAL |

  

**Reaction:**
  
Vector: NONE (OFF1, OFF2, OFF3)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF2)

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
Writing to at least one parameter back-up file PSxxxyyy.*** in the non-volatile memory
was unsuccessful.  
- In the directory /USER/SINAMICS/DATA/ at least one parameter back-up file PSxxxyyy.***
has the "read only" file attribute and cannot be overwritten.  
- There is not sufficient free memory space available.  
- The non-volatile memory is defective and cannot be written to.  
Fault value (r0949, interpret hexadecimal):  
dcba hex  
a = yyy in the file names PSxxxyyy.***  
a = 000 --&gt; consistency back-up file  
a = 001 ... 062 --&gt; drive object number  
a = 070 --&gt; FEPROM.BIN  
a = 080 --&gt; DEL4BOOT.TXT  
a = 099 --&gt; PROFIBUS parameter back-up file  
b = xxx in the file names PSxxxyyy.***  
b = 000 --&gt; data save started with p0977 = 1 or p0971 = 1  
b = 010 --&gt; data save started with p0977 = 10  
b = 011 --&gt; data save started with p0977 = 11  
b = 012 --&gt; data save started with p0977 = 12  
d, c:  
Only for internal Siemens troubleshooting.

**Remedy:**
  
- Check the file attribute of the files (PSxxxyyy.***, CAxxxyyy.***, CCxxxyyy.***)
and, if required, change from "read only" to "writeable".  
- Check the free memory space in the non-volatile memory. Approx. 80 kbyte of free
memory space is required for every drive object in the system.  
- Replace the memory card or Control Unit.

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

### F01040 Save parameter settings and carry out a POWER ON

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, CU_MV_DP, CU_MV_PN, ENC, HUB, TB30, TECBASE, TM150,
TM15DI_DO, TM31

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
POWER ON

**Cause:**
  
A parameter was changed, which means that it is necessary to save the parameters and
restart the system.

**Remedy:**
  
- Save parameters (p0971, p0977).  
- Carry out a POWER ON (switch-off/switch-on) for all components.  
Then:  
- Upload the drive unit (commissioning tool).

### F01041 Parameter save necessary

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
Defective or missing files were detected on the memory card when booting.  
Fault value (r0949, interpret decimal):  
1: Source file cannot be opened.  
2: Source file cannot be read.  
3: Target directory cannot be set up.  
4. Target file cannot be set up/opened.  
5. Target file cannot be written to.  
Additional values:  
Only for internal Siemens troubleshooting.

**Remedy:**
  
- Save the parameters.  
- Download the project again to the drive unit.  
- Update the firmware  
- If required, replace the Control Unit and/or memory card.

### F01042 Parameter error during project download

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Parameter: %1, Index: %2, fault cause: %3

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
Vector: OFF2 (NONE, OFF1, OFF3)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF1, OFF2)

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
An error was detected when downloading a project using the commissioning software
(e.g. incorrect parameter value). It is possible that the parameter limits are dependent
on other parameters.  
The detailed cause of the fault can be determined using the fault value.  
Fault value (r0949, interpret hexadecimal):  
ccbbaaaa hex  
aaaa = Parameter  
bb = Index  
cc = fault cause  
0: Parameter number illegal.  
1: Parameter value cannot be changed.  
2: Lower or upper value limit exceeded.  
3: Sub-index incorrect.  
4: No array, no sub-index.  
5: Data type incorrect.  
6: Setting not permitted (only resetting).  
7: Descriptive element cannot be changed.  
9: Description data not available.  
11: No master control.  
15: No text array available.  
17: Task cannot be executed due to operating state.  
20: Illegal value.  
21: Response too long.  
22: Parameter address illegal.  
23: Format illegal.  
24: Number of values not consistent.  
25: Drive object does not exist.  
101: Presently deactivated.  
104: Illegal value.  
107: Write access not permitted when controller enabled.  
108: Unit unknown.  
109: Write access only in the commissioning state, encoder (p0010 = 4).  
110: Write access only in the commissioning state, motor (p0010 = 3).  
111: Write access only in the commissioning state, power unit (p0010 = 2).  
112: Write access only in the quick commissioning mode (p0010 = 1).  
113: Write access only in the ready mode (p0010 = 0).  
114: Write access only in the commissioning state, parameter reset (p0010 = 30).  
115: Write access only in the Safety Integrated commissioning state (p0010 = 95).  
116: Write access only in the commissioning state, technological application/units
(p0010 = 5).  
117: Write access only in the commissioning state (p0010 not equal to 0).  
118: Write access only in the commissioning state, download (p0010 = 29).  
119: Parameter may not be written in download.  
120: Write access only in the commissioning state, drive basic configuration (device:
p0009 = 3).  
121: Write access only in the commissioning state, define drive type (device: p0009
= 2).  
122: Write access only in the commissioning state, data set basic configuration (device:
p0009 = 4).  
123: Write access only in the commissioning state, device configuration (device: p0009
= 1).  
124: Write access only in the commissioning state, device download (device: p0009
= 29).  
125: Write access only in the commissioning state, device parameter reset (device:
p0009 = 30).  
126: Write access only in the commissioning state, device ready (device: p0009 = 0).  
127: Write access only in the commissioning state, device (device: p0009 not equal
to 0).  
129: Parameter may not be written in download.  
130: Transfer of the master control is inhibited via binector input p0806.  
131: Required BICO interconnection not possible because BICO output does not supply
floating value  
132: Free BICO interconnection inhibited via p0922.  
133: Access method not defined.  
200: Below the valid values.  
201: Above the valid values.  
202: Cannot be accessed from the Basic Operator Panel (BOP).  
203: Cannot be read from the Basic Operator Panel (BOP).  
204: Write access not permitted.

**Remedy:**
  
- Correct the parameterization in the commissioning tool and download the project
again.  
- Enter the correct value in the specified parameter.  
- Identify the parameter that restricts the limits of the specified parameter.

### F01043 Fatal error at project download

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Fault cause: %1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
Vector: NONE (OFF1, OFF2, OFF3)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF1, OFF2)

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A fatal error was detected when downloading a project using the commissioning tool.  
Fault value (r0949, interpret decimal):  
1: Device status cannot be changed to Device Download (drive object ON?).  
2: Incorrect drive object number.  
3: A drive object that has already been deleted is deleted again.  
4: Deleting a drive object that has already been registered for generation.  
5: Deleting a drive object that does not exist.  
6: Generating an undeleted drive object that already existed.  
7: Regenerating a drive object already registered for generation.  
8: Maximum number of drive objects that can be generated exceeded.  
9: Error while generating a device drive object.  
10: Error while generating target topology parameters (p9902 and p9903).  
11: Error when generating a drive object (global component).  
12: Error when generating a drive object (drive component).  
13: Unknown drive object type.  
14: Drive status cannot be changed to "ready for operation" (r0947 and r0949).  
15: Drive status cannot be changed to drive download.  
16: Device status cannot be changed to "ready for operation".  
17: It is not possible to download the topology. The component wiring should be checked,
taking into account the various messages/signals.  
18: A new download is only possible if the factory settings are restored for the drive
unit.  
19: The slot for the option module has been configured several times (e.g. CAN and
COMM BOARD)  
20: The configuration is inconsistent (e.g. CAN for Control Unit, however no CAN configured
for drive objects A_INF, SERVO or VECTOR).  
21: Error when accepting the download parameters.  
22: Software-internal download error.  
23: Download not possible when know-how protection is activated.  
24: Download not possible during a partial power up after inserting a component.  
25: The configuration is inconsistent. Know-how protection is either not activated
or only partially.  
Additional values:  
Only for internal Siemens troubleshooting.

**Remedy:**
  
- Use the current version of the commissioning tool.  
- Modify the offline project and carry out a new download (e.g. compare the number
of drive objects, motor, encoder, power unit in the offline project and at the drive).  
- Change the drive state (is a drive rotating or is there a message/signal?).  
- Observe additional active messages/signals and remove their cause (e.g. correct
any incorrectly set parameters).  
- Automatically calculate the control parameters (p0340). Then set p0010 = 0.  
- Boot from previously saved files (switch off / switch on or p0976).  
- Before a new download, restore the factory setting if the know-how protection was
not activated on all drive objects.

### F01044 CU: Description data error

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** GLOBAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
POWER ON

**Cause:**
  
An error was detected when loading the description data saved in the non-volatile
memory.

**Remedy:**
  
Replace the memory card or Control Unit.

### A01045 CU: Configuring data invalid

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
An error was detected when evaluating the parameter files PSxxxyyy.ACX, PTxxxyyy.ACX,
CAxxxyyy.ACX, or CCxxxyyy.ACX saved in the non-volatile memory. Because of this, under
certain circumstances, several of the saved parameter values were not able to be accepted.  
Also see r9406 up to r9408.  
Alarm value (r2124, interpret hexadecimal):  
Only for internal Siemens troubleshooting.

**Remedy:**
  
- Check the parameters displayed in r9406 up to r9408, and correct these if required.  
- Restore the factory setting (p0976 = 1) and reload the project into the converter.  
Then save the parameterization in STARTER using the function "Copy RAM to ROM" or
with p0977 = 1. This overwrites the incorrect parameter files in the non-volatile
memory – and this alarm is withdrawn.  
See also: r9406 (PS file parameter number parameter not transferred), r9407 (PS file parameter
index parameter not transferred), r9408 (PS file fault code parameter not transferred)

### A01049 CU: It is not possible to write to file

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
It is not possible to write into a write-protected file (PSxxxxxx.acx). The write
request was interrupted.  
Alarm value (r2124, interpret decimal):  
Drive object number.

**Remedy:**
  
Check whether the "write protected" attribute has been set for the files in the non-volatile
memory under .../USER/SINAMICS/DATA/...  
When required, remove write protection and repeat the save operation (e.g. set p0977
= 1).

### F01050 Memory card and device incompatible

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** GLOBAL |

  

**Reaction:**
  
Vector: OFF2 (NONE, OFF1, OFF3)  
Chopper: OFF2 (NONE)  
Infeed: OFF2 (NONE, OFF1)

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The memory card and the device type do not match (e.g. a memory card for SINAMICS
S is inserted in SINAMICS G).

**Remedy:**
  
- Insert the matching memory card.  
- Use the matching Control Unit or power unit.

### F01054 CU: System limit exceeded

**Drive object:**
  
All objects

**Valid as of version:**
  
4.4

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** GLOBAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
At least one system overload has been identified.  
Fault value (r0949, interpret decimal):  
1: Computing time load too high (r9976[1]).  
5: Peak load too high (r9976[5]).  
Note:  
As long as this fault is present, it is not possible to save the parameters (p0971,
p0977).  
See also: r9976 (System utilization)

**Remedy:**
  
For fault value = 1, 5:  
- Reduce the computing time load of the drive unit (r9976[1] and r9976[5]) to under
100 %.  
- Check the sampling times and adjust if necessary (p0115, p0799, p4099).  
- Deactivate function modules.  
- Deactivate drive objects.  
- Remove drive objects from the target topology.  
- Note the DRIVE-CLiQ topology rules and if required, change the DRIVE-CLiQ topology.  
When using the Drive Control Chart (DCC) or free function blocks (FBLOCKS), the following
applies:  
- The computing time load of the individual runtime groups on a drive object can be
read out in r21005 (DCC) or r20005 (FBLOCKS).  
- If necessary, the assignment of the runtime group (p21000, p20000) can be changed
in order to increase the sampling time (r21001, r20001).  
- If necessary, reduce the number of cyclically calculated blocks (DCC) and/or function
blocks (FBLOCKS).

### F01068 CU: Data memory memory overflow

**Drive object:**
  
All objects

**Valid as of version:**
  
4.4

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** GLOBAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The utilization for a data memory area is too large.  
Fault value (r0949, interpret binary):  
Bit 0 = 1: High-speed data memory 1 overloaded  
Bit 1 = 1: High-speed data memory 2 overloaded  
Bit 2 = 1: High-speed data memory 3 overloaded  
Bit 3 = 1: High-speed data memory 4 overloaded

**Remedy:**
  
- Deactivate the function module.  
- Deactivate drive object.  
- Remove the drive object from the target topology.

### A01069 Parameter backup and device incompatible

**Drive object:**
  
All objects

**Valid as of version:**
  
4.4

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The parameter backup on the memory card and the drive unit do not match.  
The module boots with the factory settings.  
Example:  
Devices A and B. are not compatible and a memory card with the parameter backup for
device A is inserted in device B.

**Remedy:**
  
- Insert a memory card with compatible parameter backup and carry out a POWER ON.  
- Insert a memory card without parameter backup and carry out a POWER ON.  
- Save the parameters (p0977 = 1).

### F01070 Project/firmware is being downloaded to the memory card

**Drive object:**
  
All objects

**Valid as of version:**
  
4.5

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** GLOBAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
An upgrade (project/firmware download) was initiated on the memory card.  
While this fault is present, the corresponding update takes place with plausibility
and consistency checks. After this, depending on the command option, a new boot (reset)
for the Control Unit is initiated.  
Caution:  
During the upgrade and while this fault is present, it is not permissible to switch
off the Control Unit.  
If the operation is interrupted, this can destroy the file system on the memory card.
The memory card will then no longer work properly and must be repaired.

**Remedy:**
  
Not necessary.  
The fault is automatically withdrawn after the upgrade has been completed.

### F01072 Memory card restored from the backup copy

**Drive object:**
  
All objects

**Valid as of version:**
  
4.6

**Message value:**
  
-

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The Control Unit was switched-off while writing to the memory card. This is why the
visible partition became defective.  
After switching on, the data from the non-visible partition (backup copy) were written
to the visible partition.

**Remedy:**
  
Check that the firmware and parameterization is up-to-date.

### A01073 (N) POWER ON required for backup copy on memory card

**Drive object:**
  
All objects

**Valid as of version:**
  
4.6

**Message value:**
  
-

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The parameter assignment on the visible partition of the memory card has changed.  
In order that the backup copy on the memory card is updated on the non-visible partition,
it is necessary to carry out a POWER ON or hardware reset (p0972) of the Control Unit.  
Note:  
It is possible that a new POWER ON is requested via this alarm (e.g. after saving
with p0971 = 1).

**Remedy:**
  
- Carry out a POWER ON (switch-off/switch-on) for the Control Unit.  
- Carry out a hardware reset (RESET button, p0972).

Reaction upon N:  
 NONE

Acknowl. upon N:  
NONE

### F01082 Parameter error when powering up from data backup

**Drive object:**
  
All objects

**Valid as of version:**
  
4.8

**Message value:**
  
Parameter: %1, Index: %2, fault cause: %3

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
Vector: OFF2 (NONE, OFF1, OFF3)  
Chopper: OFF2 (NONE)  
Infeed: OFF2 (NONE, OFF1)

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
Parameterizing errors have been detected (e.g. incorrect parameter value). It is possible
that the parameter limits are dependent on other parameters.  
The detailed cause of the fault can be determined using the fault value.  
Fault value (r0949, interpret hexadecimal):  
ccbbaaaa hex  
aaaa = Parameter  
bb = Index  
cc = fault cause  
0: Parameter number illegal.  
1: Parameter value cannot be changed.  
2: Lower or upper value limit exceeded.  
3: Sub-index incorrect.  
4: No array, no sub-index.  
5: Data type incorrect.  
6: Setting not permitted (only resetting).  
7: Descriptive element cannot be changed.  
9: Description data not available.  
11: No master control.  
15: No text array available.  
17: Task cannot be executed due to operating state.  
20: Illegal value.  
21: Response too long.  
22: Parameter address illegal.  
23: Format illegal.  
24: Number of values not consistent.  
25: Drive object does not exist.  
101: Presently deactivated.  
104: Illegal value.  
107: Write access not permitted when controller enabled.  
108: Unit unknown.  
109: Write access only in the commissioning state, encoder (p0010 = 4).  
110: Write access only in the commissioning state, motor (p0010 = 3).  
111: Write access only in the commissioning state, power unit (p0010 = 2).  
112: Write access only in the quick commissioning mode (p0010 = 1).  
113: Write access only in the ready mode (p0010 = 0).  
114: Write access only in the commissioning state, parameter reset (p0010 = 30).  
115: Write access only in the Safety Integrated commissioning state (p0010 = 95).  
116: Write access only in the commissioning state, technological application/units
(p0010 = 5).  
117: Write access only in the commissioning state (p0010 not equal to 0).  
118: Write access only in the commissioning state, download (p0010 = 29).  
119: Parameter may not be written in download.  
120: Write access only in the commissioning state, drive basic configuration (device:
p0009 = 3).  
121: Write access only in the commissioning state, define drive type (device: p0009
= 2).  
122: Write access only in the commissioning state, data set basic configuration (device:
p0009 = 4).  
123: Write access only in the commissioning state, device configuration (device: p0009
= 1).  
124: Write access only in the commissioning state, device download (device: p0009
= 29).  
125: Write access only in the commissioning state, device parameter reset (device:
p0009 = 30).  
126: Write access only in the commissioning state, device ready (device: p0009 = 0).  
127: Write access only in the commissioning state, device (device: p0009 not equal
to 0).  
129: Parameter may not be written in download.  
130: Transfer of the master control is inhibited via binector input p0806.  
131: Required BICO interconnection not possible because BICO output does not supply
floating value  
132: Free BICO interconnection inhibited via p0922.  
133: Access method not defined.  
200: Below the valid values.  
201: Above the valid values.  
202: Cannot be accessed from the Basic Operator Panel (BOP).  
203: Cannot be read from the Basic Operator Panel (BOP).  
204: Write access not permitted.

**Remedy:**
  
- Correct the parameterization in the commissioning tool and download the project
again.  
- Enter the correct value in the specified parameter.  
- Identify the parameter that restricts the limits of the specified parameter.

### A01097 (N) NTP server cannot be accessed

**Drive object:**
  
All objects

**Valid as of version:**
  
5.1

**Message value:**
  
-

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The selected NTP server (p3105[0...3]) cannot be accessed. Time synchronization cannot
be performed.  
Note:  
NTP: Network Time Protocol  
See also: p3105 (NTP server IP address)

**Remedy:**
  
Correctly set the IP address of the NTP server, and check the connection to the NTP
server.  
See also: p3105 (NTP server IP address)

Reaction upon N:  
 NONE

Acknowl. upon N:  
NONE

### A01099 (N) UTC synchronization tolerance violated

**Drive object:**
  
All objects

**Valid as of version:**
  
4.8

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The tolerance (p3109) set for UTC synchronization was violated.  
Note:  
UTC: Universal Time Coordinates  
See also: p3109 (UTC synchronization tolerance)

**Remedy:**
  
Select the synchronization intervals shorter so that the deviation between the time
of day master and drive system lies within the tolerance.  
Note:  
The deviation when synchronizing is shown in r3107.  
See also: r3107 (UTC synchronization time out of tolerance)

Reaction upon N:  
 NONE

Acknowl. upon N:  
NONE

### A01100 CU: Memory card withdrawn

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The memory card (non-volatile memory) was withdrawn during operation.  
Notice:  
It is not permissible for the memory card to be withdrawn or inserted under voltage.

**Remedy:**
  
- Switch off the drive system.  
- Re-insert the memory card that was withdrawn - this card must match the drive system.  
- Switch on the drive system again.

### F01105 (A) CU: Insufficient memory

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** GLOBAL |

  

**Reaction:**
  
Vector: OFF1  
Chopper: OFF2  
Infeed: OFF1

**Acknowledge:**
  
POWER ON

**Cause:**
  
Too many functions have been configured on this Control Unit (e.g. too many drives,
function modules, data sets, Technology Extensions, blocks, etc).  
Fault value (r0949, interpret decimal):  
Only for internal Siemens troubleshooting.

**Remedy:**
  
- Change the configuration on this Control Unit (e.g. fewer drives, function modules,
data sets, Technology Extensions, blocks, etc).  
- Use an additional Control Unit.

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

### F01107 CU: Save to memory card unsuccessful

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A data save in the non-volatile memory was not able to be successfully carried out.  
- Non-volatile memory is defective.  
- Insufficient space in the non-volatile memory.  
Fault value (r0949, interpret decimal):  
Only for internal Siemens troubleshooting.

**Remedy:**
  
- Try to save again.  
- Replace the memory card or Control Unit.

### F01110 CU: More than one SINAMICS G on one Control Unit

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
More than one SINAMICS G type power unit is being operated from the Control Unit.  
Fault value (r0949, interpret decimal):  
Number of the second drive with a SINAMICS G type power unit.

**Remedy:**
  
Only one SINAMICS G drive type is permitted.

### F01111 CU: Mixed operation of drive units illegal

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
Illegal operation of various drive units on one Control Unit:  
- SINAMICS S together with SINAMICS G  
- SINAMICS S together with SINAMICS S Value or Combi  
Fault value (r0949, interpret decimal):  
Number of the first drive object with a different power unit type.

**Remedy:**
  
Only power units of one particular drive type may be operated with one Control Unit.

### F01112 CU: Power unit not permissible

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The connected power unit cannot be used together with this Control Unit.  
Fault value (r0949, interpret decimal):  
1: Power unit is not supported (e.g. PM240).  
2: DC/AC power unit connected to CU310 not permissible.  
3: Power unit (S120M) not permitted for vector control.

**Remedy:**
  
Replace the power unit that is not permissible by a component that is permissible.

### F01120 (A) Terminal initialization has failed

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** BICO |

  

**Reaction:**
  
Vector: OFF1 (OFF2)  
Chopper: OFF2  
Infeed: OFF1 (OFF2)

**Acknowledge:**
  
IMMEDIATELY (POWER ON)

**Cause:**
  
An internal software error occurred while the terminal functions were being initialized.  
Fault value (r0949, interpret hexadecimal):  
Only for internal Siemens troubleshooting.

**Remedy:**
  
- Carry out a POWER ON (switch-off/switch-on) for all components.  
- Upgrade firmware to later version.  
- Contact Technical Support.  
- Replace the Control Unit.

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

### F01122 (A) Frequency at the measuring probe input too high

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Application/technological function faulted (17)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** BICO |

  

**Reaction:**
  
Vector: OFF1 (OFF2)  
Chopper: OFF2  
Infeed: OFF1 (OFF2)

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The frequency of the pulses at the measuring probe input is too high.  
Fault value (r0949, interpret decimal):  
1: DI/DO 9 (X122.8)  
2: DI/DO 10 (X122.10)  
4: DI/DO 11 (X122.11)  
8: DI/DO 13 (X132.8)  
16: DI/DO 14 (X132.10)  
32: DI/DO 15 (X132.11)  
64: DI/DO 8 (X122.7)  
128: DI/DO 12 (X132.7)

**Remedy:**
  
Reduce the frequency of the pulses at the measuring probe input.

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

### F01150 CU: Number of instances of a drive object type exceeded

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Drive object type: %1, number permitted: %2, actual number: %3

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The maximum permissible number of instances of a drive object type was exceeded.  
Drive object type:  
Drive object type (p0107), for which the maximum permissible number of instances was
exceeded.  
Number permitted:  
Max. permissible number of instances for this drive object type.  
Actual number:  
Current number of instances for this drive object type.  
Note regarding the message value:  
The individual information is coded as follows in the message value (r0949/r2124):  
ddccbbaa hex: aa = drive object type, bb = number limited, cc = actual number, dd
= no significance

**Remedy:**
  
- Switch off the unit.  
- Suitably restrict the number of instances of a drive object type by reducing the
number of inserted components.  
- Re-commission the unit.

### F01151 CU: Number of drive objects of a category exceeded

**Drive object:**
  
All objects

**Valid as of version:**
  
4.4

**Message value:**
  
Drive object category: %1, number permitted: %2, actual number: %3

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The maximum permissible number of drive objects of a category was exceeded.  
Drive object category:  
Drive object category, for which the maximum permissible number of drive objects was
exceeded.  
Number permitted:  
Max. permissible number for this drive object category.  
Actual number:  
Actual number for this drive object category.  
Note regarding the message value:  
The individual information is coded as follows in the message value (r0949/r2124):  
ddccbbaa hex: aa = drive object category, bb = number limited, cc = actual number,
dd = no significance

**Remedy:**
  
- Switch off the unit.  
- Suitably restrict the number of drive objects of the specified category by reducing
the number of inserted components.  
- Re-commission the unit.

### F01152 CU: Invalid constellation of drive object types

**Drive object:**
  
All objects

**Valid as of version:**
  
4.7

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
POWER ON

**Cause:**
  
It is not possible to simultaneously operate drive object types SERVO, VECTOR and
HLA.  
A maximum of 2 of these drive object types can be operated on a Control Unit.

**Remedy:**
  
- Switch off the unit.  
- Restrict the use of drive object types SERVO, VECTOR, HLA to a maximum of 2.  
- Re-commission the unit.

### F01200 CU: Time slice management internal software error

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** GLOBAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY (POWER ON)

**Cause:**
  
A time slice management error has occurred.  
It is possible that the sampling times have been inadmissibly set.  
Fault value (r0949, interpret hexadecimal):  
998:  
Too many time slices occupied by technology functions (e.g. DCC).  
999:  
Too many time slices occupied by the basic system. Too many different sampling times
may have been set.  
Additional values:  
Only for internal Siemens troubleshooting.

**Remedy:**
  
- Check the sampling time setting (p0112, p0115, p4099, p9500, p9511).  
- Contact Technical Support.

### F01205 CU: Time slice overflow

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** GLOBAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
POWER ON

**Cause:**
  
Insufficient processing time is available for the existing topology.  
Fault value (r0949, interpret hexadecimal):  
Only for internal Siemens troubleshooting.

**Remedy:**
  
- Reduce the number of drives.  
- Increase the sampling times.

### F01221 CU: Basic clock cycle too low

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The closed-loop control / monitoring cannot maintain the envisaged clock cycle.  
The runtime of the closed-loop control/monitoring is too long for the particular clock
cycle or the computing time remaining in the system is not sufficient for the closed-loop
control/monitoring.  
Fault value (r0949, interpret hexadecimal):  
Only for internal Siemens troubleshooting.

**Remedy:**
  
Increase the basic clock cycle of DRIVE-CLiQ communication.  
See also: p0112

### A01223 CU: Sampling time inconsistent

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
When changing a sampling time (p0115[0], p0799 or p4099), inconsistency between the
clock cycles has been identified.  
Alarm value (r2124, interpret decimal):  
1: Value lower than minimum value.  
2: Value higher than maximum value.  
3: Value not a multiple of 1.25 µs.  
4: Value does not match clock-cycle synchronous PROFIBUS operation.  
5: Value not a multiple of 125 µs.  
6: Value not a multiple of 250 µs.  
7: Value not a multiple of 375 µs.  
8: Value not a multiple of 400 µs.  
10: Special restriction of the drive object violated.  
20: On a SERVO with a sampling time of 62.5 µs, more than two drive objects or one
drive object of a type other than SERVO have been detected on the same DRIVE-CLiQ
line (a maximum of two SERVO type drive objects are permitted).  
21: Value can be a multiple of the current controller sampling time of a servo or
vector drive in the system (e.g. for TB30, the values of all of the indices should
be taken into account).  
30: Value less than 31.25 µs.  
31: Value less than 62.5 µs (31.25 µs is not supported for SMC10, SMC30, SMI10 and
Double Motor Modules).  
32: Value less than 125 µs.  
33: Value less than 250 µs.  
40: Nodes have been identified on the DRIVE-CLiQ line whose highest common denominator
of the sampling times is less than 125 µs. Further, none of the nodes has a sampling
time of less than 125 µs.  
41: A chassis unit was identified on the DRIVE-CLiQ line as a node. Further, the highest
common denominator of the sampling times of all of the nodes connected to the line
is less than 250 µs.  
42: An Active Line Module was identified on the DRIVE-CLiQ line as a node. Further,
the highest common denominator of the sampling times of all of the nodes connected
to the line is less than 125 µs.  
43: A Voltage Sensing Module (VSM) was identified on the DRIVE-CLiQ line as a node.
Further, the highest common denominator of the sampling times of all of the nodes
connected to the line is not equal to the current controller sampling time of the
drive object of the VSM.  
44: The highest common denominator of the sampling times of all of the components
connected to the DRIVE-CLiQ line is not the same for all components of this drive
object (e.g. there are components on different DRIVE-CLiQ lines on which different
highest common denominators are generated).  
45: A chassis parallel unit was identified on the DRIVE-CLiQ line as a node. Further,
the highest common denominator of the sampling times of all of the nodes connected
to the line is less than 162.5 µs or 187.5 µs (for a 2x or 3x parallel connection).  
46: A node has been identified on the DRIVE-CLiQ line whose sampling time is not a
multiple of the lowest sampling time on this line.  
52: Nodes have been identified on the DRIVE-CLiQ line whose highest common denominator
of the sampling times is less than 31.25 µs.  
54: Nodes have been identified on the DRIVE-CLiQ line whose highest common denominator
of the sampling times is less than 62.5 µs.  
56: Nodes have been identified on the DRIVE-CLiQ line whose highest common denominator
of the sampling times is less than 125 µs.  
58: Nodes have been identified on the DRIVE-CLiQ line whose highest common denominator
of the sampling times is less than 250 µs.  
99: Inconsistency of cross drive objects detected.  
116: Recommended clock cycle in r0116[0...1].  
General note:  
The topology rules should be noted when connecting up DRIVE-CLiQ (refer to the appropriate
product documentation).  
The parameters of the sampling times can also be changed with automatic calculations.  
Example for highest common denominator: 125 s, 125 µs, 62.5 µs --&gt; 62.5 µs

**Remedy:**
  
- Check the DRIVE-CLiQ cables.  
- Set a valid sampling time.  
See also: p0115, p0799, p4099

### A01224 CU: Pulse frequency inconsistent

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
When changing the minimum pulse frequency (p0113) inconsistency between the pulse
frequencies was identified.  
Alarm value (r2124, interpret decimal):  
1: Value lower than minimum value.  
2: Value higher than maximum value.  
3: Resulting sampling time is not a multiple of 1.25 µs.  
4: Value does not match clock-cycle synchronous PROFIBUS operation.  
10: Special restriction of the drive object violated.  
99: Inconsistency of cross drive objects detected.  
116: Recommended clock cycle in r0116[0...1].

**Remedy:**
  
Set a valid pulse frequency.

### F01250 CU: CU-EEPROM incorrect read-only data

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE (OFF2)

**Acknowledge:**
  
POWER ON

**Cause:**
  
Error when reading the read-only data of the EEPROM in the Control Unit.  
Fault value (r0949, interpret decimal):  
Only for internal Siemens troubleshooting.

**Remedy:**
  
- Carry out a POWER ON (switch-off/switch-on).  
- Replace the Control Unit.

### A01251 CU: CU-EEPROM incorrect read-write data

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
Error when reading the read-write data of the EEPROM in the Control Unit.  
Alarm value (r2124, interpret decimal):  
Only for internal Siemens troubleshooting.

**Remedy:**
  
For alarm value r2124 &lt; 256, the following applies:  
- Carry out a POWER ON (switch-off/switch-on).  
- Replace the Control Unit.  
For alarm value r2124 &gt;= 256, the following applies:  
- For the drive object with this alarm, clear the fault memory (p0952 = 0).  
- As an alternative, clear the fault memory of all drive objects (p2147 = 1).  
- Replace the Control Unit.

### F01255 CU: Option Board EEPROM read-only data error

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE (OFF2)

**Acknowledge:**
  
POWER ON

**Cause:**
  
Error when reading the read-only data of the EEPROM in the Option Board.  
Fault value (r0949, interpret decimal):  
Only for internal Siemens troubleshooting.

**Remedy:**
  
- Carry out a POWER ON (switch-off/switch-on).  
- Replace the Control Unit.

### A01256 CU: Option Board EEPROM read-write data error

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
Error when reading the read-write data of the EEPROM in the Option Board.  
Alarm value (r2124, interpret decimal):  
Only for internal Siemens troubleshooting.

**Remedy:**
  
- Carry out a POWER ON (switch-off/switch-on).  
- Replace the Control Unit.

### F01260 Software not released

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, CU_MV_DP, CU_MV_PN, ENC, HUB, TB30, TECBASE, TM150,
TM15DI_DO, TM31, VECTOR3P, VECTORGL, VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
4.6

**Message value:**
  
-

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** GLOBAL |

  

**Reaction:**
  
Vector: OFF3  
Chopper: OFF2  
Infeed: OFF1

**Acknowledge:**
  
POWER ON

**Cause:**
  
The runtime software (RT-SW) has not been released.

**Remedy:**
  
Only for internal Siemens troubleshooting.

### F01275 Hardware description error

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, CU_MV_DP, CU_MV_PN, ENC, HUB, TB30, TECBASE, TM150,
TM15DI_DO, TM31, VECTOR3P, VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
4.4

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** DRIVE |

  

**Reaction:**
  
Vector: OFF3  
Chopper: OFF2  
Infeed: OFF2

**Acknowledge:**
  
POWER ON

**Cause:**
  
An error has occurred while accessing the hardware description file on the CompactFlash
card.  
Directory and file name: ADDON/SINAMICS/DATA/HW_DESC/&lt;DOType&gt;/DESC0000  
Fault value (r0949, interpret decimal):  
22: File not found.  
24: File read access error.  
26: Format error.  
28: Version error.  
30: Internal reader error.  
40: Content error.  
45: Hardware description not consistent.  
60: Inconsistency: Number of Power Stack Adapters (PSA).  
61: Inconsistency: Number of Sensor Module Cabinets (SMC).  
62: Inconsistency: Number of Voltage Sensing Modules (VSM).  
63: Inconsistency: Number of Terminal Modules (TM).  
64: Inconsistency: Number of Terminal Boards (TB).

**Remedy:**
  
Only for internal Siemens troubleshooting.  
See also: r0107 (Drive object type)

### A01276 (N) Hardware description not fully compatible

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, CU_MV_DP, CU_MV_PN, ENC, HUB, TB30, TECBASE, TM150,
TM15DI_DO, TM31, VECTOR3P, VECTORDM, VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
5.2

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** DRIVE |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The hardware description file contains more data than the firmware requires.

**Remedy:**
  
Not necessary.

Reaction upon N:  
 NONE

Acknowl. upon N:  
NONE

### F01303 Component does not support the required function

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** BICO |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A function requested by the Control Unit is not supported by a DRIVE-CLiQ component.  
Fault value (r0949, interpret decimal):  
1: The component does not support the deactivation.  
101: The Motor Module does not support an internal armature short-circuit.  
102: The Motor Module does not support the deactivation.  
201: The Sensor Module does not support actual value inversion (p0410.0 = 1) when
using a Hall sensor (p0404.6 = 1) for the commutation.  
202: The Sensor Module does not support parking/unparking.  
203: The Sensor Module does not support the deactivation.  
204: The firmware of this Terminal Module 15 (TM15) does not support the application
TM15DI/DO.  
205: The Sensor Module does not support the selected temperature evaluation (r0458,
r0459).  
206: The firmware of this Terminal Modules TM41/TM31/TM15 refers to an old firmware
version. It is urgently necessary to upgrade the firmware to ensure disturbance-free
operation.  
207: The power unit with this hardware version does not support operation with device
supply voltages of less than 380 V.  
208: The Sensor Module does not support de-selection of commutation with zero mark
(via p0430.23).  
211: The Sensor Module does not support single-track encoders (r0459.10).  
212: The Sensor Module does not support LVDT sensors (p4677.0).  
213: The Sensor Module does not support the characteristic type (p4662).  
214: The power unit does not support the temperature evaluation via PT1000 (r0193).  
215: The Terminal Module does not support the temperature evaluation via PT1000  
216: The Voltage Sensing Module (VSM) does not support operation with a PT1000 temperature
sensor.

**Remedy:**
  
Upgrade the firmware of the DRIVE-CLiQ component involved.  
For fault value = 205, 214, 215:  
- Check parameters p0600 and p0601 and if required, adapt.  
For fault value = 207:  
- Replace the power unit or if required set the device supply voltage higher (p0210).  
For fault value = 208:  
- Check parameter p0430.23 and reset if necessary.  
For fault value = 216:  
- Check the setting of the sensor type (p3665).  
- Use a Voltage Sensing module that supports operation with PT1000 (MLFB ...-xxx1).

### A01304 (F) Firmware version of DRIVE-CLiQ component is not up-to-date

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The non-volatile memory has a more recent firmware version than the one in the connected
DRIVE-CLiQ component.  
Alarm value (r2124, interpret decimal):  
Component number of the DRIVE-CLiQ component involved.

**Remedy:**
  
Update the firmware (p7828, p7829 - or commissioning tool).

Reaction upon F:  
 NONE

Acknowl. upon F:  
IMMEDIATELY

### F01305 Topology: Component number missing

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The component number from the topology was not parameterized (p0121 (for power unit,
refer to p0107), p0131 (for servo/vector drives, refer to p0107), p0141, p0151, p0161).  
Fault value (r0949, interpret decimal):  
Data set number.  
Note:  
The fault also occurs if encoders have been configured (p0187 to p0189) but no component
numbers exist for them.  
In this case, the fault value includes the drive data set number plus 100 * encoder
number (e.g. 3xx, if a component number was not entered in p0141 for encoder 3 (p0189)).  
See also: p0121, p0131, p0141, p0142, p0151, p0161, p0186, p0187, p0188, p0189

**Remedy:**
  
- Enter missing component number.  
- If required, remove the component and restart commissioning.  
See also: p0121, p0131, p0141, p0142, p0151, p0161, p0186, p0187, p0188, p0189

### A01306 Firmware of the DRIVE-CLiQ component being updated

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
Firmware update is active for at least one DRIVE-CLiQ component.  
Alarm value (r2124, interpret decimal):  
Component number of the DRIVE-CLiQ component.

**Remedy:**
  
Not necessary.  
This alarm is automatically withdrawn after the firmware update has been completed.

### A01314 Topology: Component must not be present

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1, to %2, %3, connection: %4

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |
| %1, %2 | 0 | Component unknown |  |
| 1 | Control Unit |  |  |
| 2 | Motor Module |  |  |
| 3 | Line Module |  |  |
| 4 | Sensor Module |  |  |
| 5 | Voltage Sensing Module |  |  |
| 6 | Terminal Module |  |  |
| 7 | DRIVE-CLiQ Hub Module |  |  |
| 8 | Controller Extension |  |  |
| 9 | Filter module |  |  |
| 10 | Hydraulic Module |  |  |
| 49 | DRIVE-CLiQ component |  |  |
| 50 | Option slot |  |  |
| 60 | Encoder |  |  |
| 70 | DRIVE-CLiQ motor |  |  |
| 71 | Hydraulic cylinder |  |  |
| 72 | Hydraulic valve |  |  |
| 80 | Motor |  |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |
| %4 | 0 | Port 0 |  |
| 1 | Port 1 |  |  |
| 2 | Port 2 |  |  |
| 3 | Port 3 |  |  |
| 4 | Port 4 |  |  |
| 5 | Port 5 |  |  |
| 6 | Port 6 |  |  |
| 7 | Port 7 |  |  |
| 8 | Port 8 |  |  |
| 9 | Port 9 |  |  |
| 10 | X100 |  |  |
| 11 | X101 |  |  |
| 12 | X102 |  |  |
| 13 | X103 |  |  |
| 14 | X104 |  |  |
| 15 | X105 |  |  |
| 20 | X200 |  |  |
| 21 | X201 |  |  |
| 22 | X202 |  |  |
| 23 | X203 |  |  |
| 24 | X204 |  |  |
| 25 | X205 |  |  |
| 40 | X400 |  |  |
| 41 | X401 |  |  |
| 42 | X402 |  |  |
| 50 | X500 |  |  |
| 51 | X501 |  |  |
| 52 | X502 |  |  |
| 53 | X503 |  |  |
| 54 | X504 |  |  |
| 55 | X505 |  |  |
| 56 | X506 |  |  |
| 57 | X507 |  |  |

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
For a component, "deactivate and not present" is set but this component is still in
the topology.  
Alarm value (r2124, interpret hexadecimal):  
ddccbbaa hex:  
aa = component number  
bb = component class of the component  
cc = connection number  
Note:  
Component class and connection number are described in F01375.

**Remedy:**
  
- Remove the corresponding component.  
- Change the setting "deactivate and not present".  
Note:  
Under "Topology --&gt; Topology view", the commissioning tool where relevant offers improved
diagnostics capability (e.g. setpoint/actual value comparison).  
See also: p0105, p0125, p0145, p0155

### A01317 (N) Deactivated component again present

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
If a component of the target topology for an active drive object is inserted and the
associated parameter of the component is set to "deactivate" (p0125, p0145, p0155,
p0165).  
Note:  
This is the only message that is displayed for a deactivated component.

**Remedy:**
  
The alarm is automatically withdrawn for the following actions:  
- Activate the components involved (p0125 = 1, p0145 = 1, p0155 = 1, p0165 = 1).  
- Again withdraw the component involved.  
See also: p0125 (Activate/deactivate power unit components), p0145, p0155 (Voltage Sensing Module
activate/deactivate)

Reaction upon N:  
 NONE

Acknowl. upon N:  
NONE

### A01318 BICO: Deactivated interconnections present

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
This alarm is used in the following cases:  
- If an inactive/non-operational drive object is active again/ready for operation  
- If there are items in the list of BI/CI parameters (r9498[0...29], r9499[0...29])  
- If the BICO interconnections saved in the list of BI/CI parameters (r9498[0...29],
r9499[0...29]) have actually been changed

**Remedy:**
  
Reset alarm:  
- Set p9496 to 1 or 2  
or  
- Deactivate the drive object again.

### A01319 Inserted component not initialized

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, ENC, HUB, TB30, TECBASE, TM150, TM15DI_DO, TM31,
VECTOR3P, VECTORDM, VECTORGL, VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
Initialization is required for at least one inserted component.  
This is only possible if the pulses are inhibited for all the drive objects.

**Remedy:**
  
Activate pulse inhibit for all drive objects.

### A01320 Topology: Drive object number does not exist in configuration

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
A drive object number is missing in p0978  
Alarm value (r2124, interpret decimal):  
Index of p0101 under which the missing drive object number can be determined.

**Remedy:**
  
Set p0009 to 1 and change p0978:  
Rules:  
- p0978 must include all of the drive object numbers (p0101).  
- It is not permissible for a drive object number to be repeated.  
- By entering a 0, the drive objects with PZD are separated from those without PZD.  
- Only 2 partial lists are permitted. After the second 0, all values must be 0.  
- Dummy drive object numbers (255) are only permitted in the first partial list.

### A01321 Topology: Drive object number does not exist in configuration

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
p0978 contains a drive object number that does not exist.  
Alarm value (r2124, interpret decimal):  
Index of p0978 under which the drive object number can be determined.

**Remedy:**
  
Set p0009 to 1 and change p0978:  
Rules:  
- p0978 must include all of the drive object numbers (p0101).  
- It is not permissible for a drive object number to be repeated.  
- By entering a 0, the drive objects with PZD are separated from those without PZD.  
- Only 2 partial lists are permitted. After the second 0, all values must be 0.  
- Dummy drive object numbers (255) are only permitted in the first partial list.

### A01322 Topology: Drive object number present twice in configuration

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
A drive object number is present more than once in p0978.  
Alarm value (r2124, interpret decimal):  
Index of p0978 under which the involved drive object number is located.

**Remedy:**
  
Set parameter p0009 = 1 and change p0978:  
Rules:  
- p0978 must include all of the drive object numbers (p0101).  
- It is not permissible for a drive object number to be repeated.  
- By entering a 0, the drive objects with PZD are separated from those without PZD.  
- Only 2 partial lists are permitted. After the second 0, all values must be 0.  
- Dummy drive object numbers (255) are only permitted in the first partial list.

### A01323 Topology: More than two partial lists created

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
Partial lists are available more than twice in p0978. After the second 0, all must
be 0.  
Alarm value (r2124, interpret decimal):  
Index of p0978 under which the illegal value is located.

**Remedy:**
  
Set p0009 to 1 and change p0978:  
Rules:  
- p0978 must include all of the drive object numbers (p0101).  
- It is not permissible for a drive object number to be repeated.  
- By entering a 0, the drive objects with PZD are separated from those without PZD.  
- Only 2 partial lists are permitted. After the second 0, all values must be 0.  
- Dummy drive object numbers (255) are only permitted in the first partial list.

### A01324 Topology: Dummy drive object number incorrectly created

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
In p0978, dummy drive object numbers (255) are only permitted in the first partial
list.  
Alarm value (r2124, interpret decimal):  
Index of p0978 under which the illegal value is located.

**Remedy:**
  
Set p0009 to 1 and change p0978:  
Rules:  
- p0978 must include all of the drive object numbers (p0101).  
- It is not permissible for a drive object number to be repeated.  
- By entering a 0, the drive objects with PZD are separated from those without PZD.  
- Only 2 partial lists are permitted. After the second 0, all values must be 0.  
- Dummy drive object numbers (255) are only permitted in the first partial list.

### F01325 Topology: Component number not present in target topology

**Drive object:**
  
All objects

**Valid as of version:**
  
4.4

**Message value:**
  
Component number: %1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The component configured in a parameter (e.g. p0121, p0131, etc.) is not present in
the target topology.  
Fault value (r0949, interpret decimal):  
Configured component number that is not present in target topology.

**Remedy:**
  
Establish topology and DO configuration consistency.

### A01330 Topology: Quick commissioning not possible

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Fault cause: %1, supplementary information: %2, preliminary component number: %3

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
Unable to carry out a quick commissioning. The existing actual topology does not fulfill
the requirements.  
Alarm value (r2124, interpret hexadecimal):  
ccccbbaa hex: cccc = preliminary component number, bb = supplementary information,
aa = fault cause  
aa = 01 hex = 1 dec:  
On one component illegal connections were detected.  
- bb = 01 hex = 1 dec: For a Motor Module, more than one motor with DRIVE-CLiQ was
detected.  
- bb = 02 hex = 2 dec: For a motor with DRIVE-CLiQ, the DRIVE-CLiQ cable is not connected
to a Motor Module.  
aa = 02 hex = 2 dec:  
The topology contains too many components of a particular type.  
- bb = 01 hex = 1 dec: There is more than one master Control Unit.  
- bb = 02 hex = 2 dec: There is more than 1 infeed (8 for a parallel circuit configuration).  
- bb = 03 hex = 3 dec: There are more than 10 Motor Modules (8 for a parallel circuit
configuration).  
- bb = 04 hex = 4 dec: There are more than 9 encoders.  
- bb = 05 hex = 5 dec: There are more than 8 Terminal Modules.  
- bb = 07 hex = 7 dec: Unknown component type  
- bb = 08 hex = 8 dec: There are more than 6 drive slaves.  
- bb = 09 hex = 9 dec: Connection of a drive slave not permitted.  
- bb = 0a hex = 10 dec: There is no drive master.  
- bb = 0b hex = 11 dec: There is more than one motor with DRIVE-CLiQ for a parallel
circuit.  
- bb = 0c hex = 12 dec: Different power units are being used in a parallel connection.  
- cccc: Not used.  
aa = 03 hex = 3 dec:  
More than 16 components are connected at a DRIVE-CLiQ socket of the Control Unit.  
- bb = 0, 1, 2, 3 means e.g. detected at the DRIVE-CLiQ socket X100, X101, X102, X103.  
- cccc: Not used.  
aa = 04 hex = 4 dec:  
The number of components connected one after the other is greater than 125.  
- bb: Not used.  
- cccc = preliminary component number of the first component and component that resulted
in the fault.  
aa = 05 hex = 5 dec:  
The component is not permissible for SERVO.  
- bb = 01 hex = 1 dec: SINAMICS G available.  
- bb = 02 hex = 2 dec: Chassis available.  
- cccc = preliminary component number of the first component and component that resulted
in the fault.  
aa = 06 hex = 6 dec:  
On one component illegal EEPROM data was detected. These must be corrected before
the system continues to boot.  
- bb = 01 hex = 1 dec: The Article No. [MLFB] of the power unit that was replaced
includes a space retainer. The space retainer (*) must be replaced by a correct character.  
- cccc = preliminary component number of the component with illegal EEPROM data.  
aa = 07 hex = 7 dec:  
The actual topology contains an illegal combination of components.  
- bb = 01 hex = 1 dec: Active Line Module (ALM) and Basic Line Module (BLM).  
- bb = 02 hex = 2 dec: Active Line Module (ALM) and Smart Line Module (SLM).  
- bb = 03 hex = 3 dec: SIMOTION control (e.g. SIMOTION D445) and SINUMERIK component
(e.g. NX15).  
- bb = 04 hex = 4 dec: SINUMERIK control (e.g. SINUMERIK 730.net) and SIMOTION component
(e.g. CX32).  
- cccc: Not used.  
aa = 08 hex = 8 dec:  
The motor is not completely connected.  
- bb: Not used.  
- cccc: Not used.  
Note:  
Connection type and connection number are described in F01375.  
See also: p0097 (Select drive object type), r0098 (Actual device topology), p0099 (Device target
topology)

**Remedy:**
  
- Adapt the output topology to the permissible requirements.  
- Commission the device using the commissioning tool.  
- For motors with DRIVE-CLiQ, connect the power and DRIVE-CLiQ cable to the same Motor
Module (Single Motor Module: DRIVE-CLiQ at X202, Double Motor Module: DRIVE-CLiQ from
motor 1 (X1) to X202, from motor 2 (X2) to X203).  
For aa = 06 hex = 6 dec and bb = 01 hex = 1 dec:  
Correct the Article No. when commissioning using the commissioning tool.  
See also: p0097 (Select drive object type), r0098 (Actual device topology), p0099 (Device target
topology)

### A01331 Topology: At least one component not assigned to a drive object

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Component number: %1

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
At least one component is not assigned to a drive object.  
- When commissioning, a component was not able to be automatically assigned to a drive
object.  
- The parameters for the data sets are not correctly set.  
Alarm value (r2124, interpret decimal):  
Component number of the unassigned component.

**Remedy:**
  
This component is assigned to a drive object.  
Check the parameters for the data sets.  
Examples:  
- Power unit (p0121).  
- Motor (p0131, p0186).  
- Encoder interface (p0140, p0141, p0187 ... p0189).  
- Encoder (p0140, p0142, p0187 ... p0189).  
- Terminal Module (p0151).  
- Option board (p0161).

### F01340 Topology: Too many components on one line

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Component number or connection number: %1, fault cause: %2

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
For the selected communications clock cycle, too many DRIVE-CLiQ components are connected
to one line of the Control Unit.  
Fault value (r0949, interpret hexadecimal):  
xyy hex: x = fault cause, yy = component number or connection number.  
1yy:  
The communications clock cycle of the DRIVE-CLiQ connection on the Control Unit is
not sufficient for all read transfers.  
2yy:  
The communications clock cycle of the DRIVE-CLiQ connection on the Control Unit is
not sufficient for all write transfers.  
3yy:  
Cyclic communication is fully utilized.  
4yy:  
The DRIVE-CLiQ cycle starts before the earliest end of the application. An additional
dead time must be added to the control. Sign-of-life errors can be expected.  
The conditions of operation with a current controller sampling time of 31.25 µs have
not been maintained.  
5yy:  
Internal buffer overflow for net data of a DRIVE-CLiQ connection.  
6yy:  
Internal buffer overflow for receive data of a DRIVE-CLiQ connection.  
7yy:  
Internal buffer overflow for send data of a DRIVE-CLiQ connection.  
8yy:  
The component clock cycles cannot be combined with one another  
900:  
The lowest common multiple of the clock cycles in the system is too high to be determined.  
901:  
The lowest common multiple of the clock cycles in the system cannot be generated with
the hardware.

**Remedy:**
  
- Check the DRIVE-CLiQ wiring.  
- Reduce the number of components on the DRIVE-CLiQ line involved and distribute these
to other DRIVE-CLiQ sockets of the Control Unit. This means that communication is
uniformly distributed over several lines.  
For fault value = 1yy - 4yy in addition:  
- Increase the sampling times (p0112, p0115, p4099). If necessary, for DCC or FBLOCKS,
change the assignment of the runtime group (p21000, p20000) so that the sampling time
(r21001, r20001) is increased.  
- If necessary, reduce the number of cyclically calculated blocks (DCC) and/or function
blocks (FBLOCKS).  
- Reduce the function modules (r0108).  
- Establish the conditions for operation with a current controller sampling time of
31.25 µs (at the DRIVE-CLiQ line, only operate Motor Modules and Sensor Modules with
this sampling time and only use a permitted Sensor Module (e.g. SMC20, this means
a 3 at the last position of the Article No.)).  
- For an NX, the corresponding Sensor Module for a possibly existing second measuring
system should be connected to a free DRIVE-CLiQ socket of the NX.  
- For BSR Motor Modules, the following applies: If Safety Extended Functions is enabled,
and 6 axes are operated on the DRIVE-CLiQ line, then the clock cycle for the actual
value sensing must be set as follows: p9511 &gt;= 8 * current controller sampling time
(p0115[0]).  
For fault value = 8yy in addition:  
- Check the clock cycles settings (p0112, p0115, p4099). Clock cycles on a DRIVE-CLiQ
line must be perfect integer multiples of one another. As clock cycle on a line, all
clock cycles of all drive objects in the previously mentioned parameters apply, which
have components on the line involved.  
For fault value = 9yy in addition:  
- Check the clock cycles settings (p0112, p0115, p4099). The lower the numerical value
difference between two clock cycles, the higher the lowest common multiple. This behavior
has a significantly stronger influence, the higher the numerical values of the clock
cycles.

### F01341 Topology: Maximum number of DRIVE-CLiQ components exceeded

**Drive object:**
  
All objects

**Valid as of version:**
  
4.5

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
Too many DRIVE-CLiQ components were defined in the actual topology.  
Note:  
Pulse enable is withdrawn and prevented.

**Remedy:**
  
- Check the DRIVE-CLiQ wiring.  
- Reduce the number components on the DRIVE-CLiQ line involved in order to maintain
the maximum quantity structure.

### F01354 Topology: Actual topology indicates an illegal component

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Fault cause: %1, component number: %2

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The actual topology indicates at least one illegal component.  
Fault value (r0949, interpret hexadecimal):  
yyxx hex: yy = component number, xx = cause.  
xx = 1: Component at this Control Unit not permissible.  
xx = 2: Component in combination with another component not permissible.  
Note:  
Pulse enable is prevented.

**Remedy:**
  
Remove the illegal components and restart the system.

### F01355 Topology: Actual topology changed

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The device target topology (p0099) does not correspond to the device actual topology
(r0098).  
The fault only occurs if the topology was commissioned using the automatic internal
device mechanism and not using the commissioning tool.  
Fault value (r0949, interpret decimal):  
Only for internal Siemens troubleshooting.  
See also: r0098 (Actual device topology), p0099 (Device target topology)

**Remedy:**
  
One of the following counter-measures can be selected if no faults have occurred in
the topology detection itself:  
If commissioning is still not completed:  
- Carry out a self-commissioning routine (starting from p0009 = 1).  
In general:  
Set p0099 = r0098, set p0009 = 0; for existing Motor Modules, this results in servo
drives being automatically generated (p0107).  
Generating servo drives: Set p0097 to 1, set p0009 to 0.  
Generating vector drives: Set p0097 to 2, set p0009 to 0.  
Generating vector drives with parallel connection: set p0097 to 12, set p0009 to 0.  
In order to set configurations in p0108, before setting p0009 to 0, it is possible
to first set p0009 to 2 and modify p0108. The index corresponds to the drive object
(p0107).  
If commissioning has already been completed:  
- Re-establish the original connections and re-connect power to the Control Unit.  
- Restore the factory setting for the complete equipment (all of the drives) and allow
automatic self-commissioning again.  
- Change the device parameterization to match the connections (this is only possible
using the commissioning tool).  
Notice:  
Topology changes that result in this fault being generated cannot be accepted by the
automatic function in the device, but must be transferred using the commissioning
tool and parameter download. The automatic function in the device only allows constant
topology to be used. Otherwise, when the topology is changed, all of the previous
parameter settings are lost and replaced by the factory setting.  
See also: r0098 (Actual device topology)

### F01356 Topology: There is a defective DRIVE-CLiQ component

**Drive object:**
  
All objects

**Valid as of version:**
  
4.4

**Message value:**
  
Fault cause: %1, Component number: %2, Connection number: %3

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE (OFF2)

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The actual topology indicates at least one defective DRIVE-CLiQ component.  
Fault value (r0949, interpret hexadecimal):  
zzyyxx hex:  
zz = connection number of the component at which the defective component is connected  
yy = component number of the component at which the defective component is connected  
xx = fault cause  
xx = 1: Component at this Control Unit not permissible.  
xx = 2: component with communication defect.  
Note:  
Pulse enable is withdrawn and prevented.

**Remedy:**
  
Replace the defective component and restart the system.

### F01357 Topology: Two Control Units identified on the DRIVE-CLiQ line

**Drive object:**
  
All objects

**Valid as of version:**
  
4.5

**Message value:**
  
component number: %1, connection number: %2

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE (OFF2)

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
In the actual topology, 2 Control Units are connected with one another through DRIVE-CLiQ.  
As standard, this is not permitted.  
This is only permitted if the Technology Extension OALINK has already been installed
on the two Control Units and has been commissioned online.  
Fault value (r0949, interpret hexadecimal):  
yyxx hex:  
yy = connection number of the Control Unit at which the second Control Unit is connected  
xx = component number of the Control Unit at which the second Control Unit is connected  
Note:  
Pulse enable is withdrawn and prevented.

**Remedy:**
  
In general:  
- Remove the connection to the second Control Unit and restart.  
- For the S120M component DRIVE-CLiQ extension, interchange the hybrid cable (IN/OUT).  
When using OALINK:  
- Remove the DRIVE-CLiQ connection and restart the systems.  
- Install OALINK on both Control Units and activate.  
- Check the configuration of the DRIVE-CLiQ sockets in OALINK.

### A01358 Topology: Line termination not available

**Drive object:**
  
All objects

**Valid as of version:**
  
4.5

**Message value:**
  
CU connection number: %1, component number: %2, connection number: %3

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
At least one line with distributed drives is not terminated. The last participant
on the line must be terminated with a line termination connector.  
This therefore ensures the degree of protection of the distributed drives.  
Alarm value (r2124, interpret hexadecimal):  
zzyyxx hex:  
zz = connection number of the distributed drive where there is no terminating connector  
yy = component number  
xx = CU connection number

**Remedy:**
  
Install the line terminating connector for the last distributed drive.

### F01359 Topology: DRIVE-CLiQ performance not sufficient

**Drive object:**
  
All objects

**Valid as of version:**
  
4.6

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The DRIVE-CLiQ performance is not sufficient at one line in order to identify an inserted
component.  
Fault value (r0949, interpret hexadecimal):  
Only for internal Siemens troubleshooting.

**Remedy:**
  
- Carry out a POWER ON (switch-off/switch-on).  
- Distribute components across several DRIVE-CLiQ lines.  
Note:  
For this topology, do not withdraw and insert components in operation.

### F01360 Topology: Actual topology not permissible

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Fault cause: %1, preliminary component number: %2

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The detected actual topology is not permissible.  
Fault value (r0949, interpret hexadecimal):  
ccccbbaa hex:  
cccc = preliminary component number, bb = no significance, aa = fault cause  
aa = 01 hex = 1 dec:  
Too many components were detected at the Control Unit. A maximum of 199 components
is permissible.  
aa = 02 hex = 2 dec:  
The component type of a component is not known.  
aa = 03 hex = 3 dec:  
It is illegal to combine ALM and BLM.  
aa = 04 hex = 4 dec:  
It is illegal to combine ALM and SLM.  
aa = 05 hex = 5 dec:  
It is illegal to combine BLM and SLM.  
aa = 06 hex = 6 dec:  
A CX32 was not directly connected to a permitted Control Unit.  
aa = 07 hex = 7 dec:  
An NX10 or NX15 was not directly connected to a permitted Control Unit.  
aa = 08 hex = 8 dec:  
A component was connected to a Control Unit that is not permitted for this purpose.  
aa = 09 hex = 9 dec:  
A component was connected to a Control Unit with out-of-date firmware.  
aa = 0A hex = 10 dec:  
Too many components of a particular type detected.  
aa = 0B hex = 11 dec:  
Too many components of a particular type detected on a single line.  
Note:  
The drive system is no longer booted. In this state, the drive control (closed-loop)
cannot be enabled.

**Remedy:**
  
For fault cause = 1:  
Change the configuration. Connect less than 199 components to the Control Unit.  
For fault cause = 2:  
Remove the component with unknown component type.  
For fault cause = 3, 4, 5:  
Establish a valid combination.  
For fault cause = 6, 7:  
Connect the expansion module directly to a permitted Control Unit.  
For fault cause = 8:  
Remove component or use a permissible component.  
For fault cause = 9:  
Upgrade the firmware of the Control Unit to a later version.  
For fault cause = 10, 11:  
Reduce the number of components.

### A01361 Topology: Actual topology contains SINUMERIK and SIMOTION components

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The detected actual topology contains SINUMERIK and SIMOTION components.  
The drive system is no longer booted. In this state, the drive control (closed-loop)
cannot be enabled.  
Alarm value (r2124, interpret hexadecimal):  
ddccbbaa hex: cc = fault cause, bb = component class of the actual topology, aa =
component number of the component  
cc = 01 hex = 1 dec:  
An NX10 or NX15 was connected to a SIMOTION control.  
cc = 02 hex = 2 dec:  
A CX32 was connected to a SINUMERIK control.

**Remedy:**
  
For alarm value = 1:  
Replace all NX10 or NX15 by a CX32.  
For alarm value = 2:  
Replace all CX32 by an NX10 or NX15.

### A01362 Topology: Topology rule(s) broken

**Drive object:**
  
All objects

**Valid as of version:**
  
4.4

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
At least one topology rule for the SINAMICS S120 Combi has been broken.  
In the event of a fault, the ramping up of the drive system is aborted and closed-loop
drive control is not enabled.  
Alarm value (r2124, interpret decimal):  
The alarm value indicates which rule has been violated.  
1: The S120 Combi may only be wired via DRIVE-CLiQ socket X200 to X100 on the NCU.  
2: In DRIVE-CLiQ socket X101 on the NCU, only one Single Motor Module (SMM) may be
connected via X200, one Double Motor Module (DMM) via X200, one Terminal Module 54F
(TM54F) via X500 or one DRIVE-CLiQ Hub Module (DMC20, DME20) via X500.  
3: In DRIVE-CLiQ socket X102 on the NCU, only one Terminal Module 54F (TM54F) may
be connected via X500, one DRIVE-CLiQ Hub Module (Hub) via X500 or one NX15 via X100.  
4: Only Sensor Modules may be connected to DRIVE-CLiQ sockets X201 up to X203 (3-axis)
or X204 (4-axis) on the S120 Combi.  
5: In DRIVE-CLiQ socket X205 (X204 is not available for 3 axes), only SMC / SME Sensor
Modules and DRIVE-CLiQ encoders may be connected.  
6: In the case of a Single Motor Module as first expansion axis, only one additional
Single Motor Module may be connected in the DRIVE-CLiQ socket X201 via X200, one Terminal
Module 54F (TM54F) via X500 or one DRIVE-CLiQ Hub Module (DMC20, DME20) via X500.  
7: Only Sensor Modules or DRIVE-CLiQ encoders may be connected in the DRIVE-CLiQ socket
X202 on possibly available Single Motor Modules.  
8: For a second Single Motor Module or for a Double Motor Module, at X201 a 54F Terminal
Module (TM54F) or a DRIVE-CLiQ Hub Module (DMC20, DME20) may be connected via X500.  
9: If a Double Motor Module is used as an expansion axis, only Sensor Modules may
be connected to X202 and X203.  
10: If a Terminal Module 54F (TM54F) is configured, only one DRIVE-CLiQ Hub Module
(DMC20, DME20) may be connected to X501 of the TM54F module via DRIVE-CLiQ socket
X500. In this case, it is not permissible that an existing Hub Module is connected
elsewhere.  
11: For DRIVE-CLiQ Hub Modules, only Sensor Modules (SMC, SME) and DRIVE-CLiQ encoders
may be connected to X501 to X505.  
12: Only certain Motor Modules may be used for expansion axes.  
13: For an S120 Combi with 3 axes, nothing must be connected at the DRIVE-CLiQ Hub
Module at X503.  
14: A maximum of one Terminal Module 54F (TM54F) is permitted.  
15: A maximum of one DRIVE-CLiQ Hub Module (DMC20, DME20) is permitted.  
16: DRIVE-CLiQ socket X100 of NX15 must be connected with the NCU via X102.  
17: The S120 Combi may only be connected to X101 of the NX15 via the DRIVE-CLiQ socket
X200.  
18: In DRIVE-CLiQ socket X102 on the NX15, only one Single Motor Module (SMM) may
be connected via X200, one Double Motor Module (DMM) via X200, one Terminal Module
54F (TM54F) via X500 or one DRIVE-CLiQ Hub Module (DMC20, DME20) via X500.  
19: It is not permissible that anything is connected at DRIVE-CLiQ socket X103 on
the NX15.

**Remedy:**
  
Evaluate the alarm value and ensure compliance with the corresponding topology rule(s).

### F01375 Topology: Connection duplicated between two components

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Component: %1, %2, connection: %3

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |
| %2 | 0 | Component unknown |  |
| 1 | Control Unit |  |  |
| 2 | Motor Module |  |  |
| 3 | Line Module |  |  |
| 4 | Sensor Module |  |  |
| 5 | Voltage Sensing Module |  |  |
| 6 | Terminal Module |  |  |
| 7 | DRIVE-CLiQ Hub Module |  |  |
| 8 | Controller Extension |  |  |
| 9 | Filter module |  |  |
| 10 | Hydraulic Module |  |  |
| 49 | DRIVE-CLiQ component |  |  |
| 50 | Option slot |  |  |
| 60 | Encoder |  |  |
| 70 | DRIVE-CLiQ motor |  |  |
| 71 | Hydraulic cylinder |  |  |
| 72 | Hydraulic valve |  |  |
| 80 | Motor |  |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |
| %3 | 0 | Port 0 |  |
| 1 | Port 1 |  |  |
| 2 | Port 2 |  |  |
| 3 | Port 3 |  |  |
| 4 | Port 4 |  |  |
| 5 | Port 5 |  |  |
| 6 | Port 6 |  |  |
| 7 | Port 7 |  |  |
| 8 | Port 8 |  |  |
| 9 | Port 9 |  |  |
| 10 | X100 |  |  |
| 11 | X101 |  |  |
| 12 | X102 |  |  |
| 13 | X103 |  |  |
| 14 | X104 |  |  |
| 15 | X105 |  |  |
| 20 | X200 |  |  |
| 21 | X201 |  |  |
| 22 | X202 |  |  |
| 23 | X203 |  |  |
| 24 | X204 |  |  |
| 25 | X205 |  |  |
| 40 | X400 |  |  |
| 41 | X401 |  |  |
| 42 | X402 |  |  |
| 50 | X500 |  |  |
| 51 | X501 |  |  |
| 52 | X502 |  |  |
| 53 | X503 |  |  |
| 54 | X504 |  |  |
| 55 | X505 |  |  |
| 56 | X506 |  |  |
| 57 | X507 |  |  |

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
When checking the actual topology, a ring-type connection was detected.  
The fault value describes a component contained in the ring.  
Fault value (r0949, interpret hexadecimal):  
ccbbaaaa hex:  
cc = connection number (%3)  
bb = component class (% 2)  
aaaa = preliminary component number (%1)  
Component class:  
0: Component unknown.  
1: Control Unit  
2: Motor Module  
3: Line Module  
4: Sensor Module  
5: Voltage Sensing Module  
6: Terminal Module  
7: DRIVE-CLiQ Hub Module  
8: Controller Extension  
9: Filter Module  
10: Hydraulic Module.  
49: DRIVE-CLiQ component  
50: Option slot  
60: Encoder  
70: DRIVE-CLiQ motor  
71: Hydraulic cylinder  
72: Hydraulic valve  
80: Motor  
Connection number:  
0: Port 0, 1: Port 1, 2: Port 2, 3: Port 3, 4: Port 4, 5: Port 5  
10: X100, 11: X101, 12: X102, 13: X103, 14: X104, 15: X105  
20: X200, 21: X201, 22: X202, 23: X203  
50: X500, 51: X501, 52: X502, 53: X503, 54: X504, 55: X505

**Remedy:**
  
Output the fault value and remove the specified connection.  
Note:  
Under "Topology --&gt; Topology view" the commissioning tool where relevant offers improved
diagnostics capability (e.g. setpoint/actual value comparison).

### F01380 Topology: Actual topology EEPROM defective

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Preliminary component number: %1

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
POWER ON

**Cause:**
  
When detecting the actual topology, a component with a defective EEPROM was detected.  
Fault value (r0949, interpret hexadecimal):  
bbbbaaaa hex:  
bbbb = reserved  
aaaa = preliminary component number of the defective components

**Remedy:**
  
Output the fault value and remove the defected component.

### A01381 Topology: power unit incorrectly inserted

**Drive object:**
  
BMM2C, CU_MV_DP, CU_MV_PN, ENC, HUB, TB30, TECBASE, TM150, TM15DI_DO, TM31

**Valid as of version:**
  
2.6

**Message value:**
  
Component: %1, to %2, %3, connection: %4

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |
| %2 | 0 | Component unknown |  |
| 1 | Control Unit |  |  |
| 2 | Motor Module |  |  |
| 3 | Line Module |  |  |
| 4 | Sensor Module |  |  |
| 5 | Voltage Sensing Module |  |  |
| 6 | Terminal Module |  |  |
| 7 | DRIVE-CLiQ Hub Module |  |  |
| 8 | Controller Extension |  |  |
| 9 | Filter module |  |  |
| 10 | Hydraulic Module |  |  |
| 49 | DRIVE-CLiQ component |  |  |
| 50 | Option slot |  |  |
| 60 | Encoder |  |  |
| 70 | DRIVE-CLiQ motor |  |  |
| 71 | Hydraulic cylinder |  |  |
| 72 | Hydraulic valve |  |  |
| 80 | Motor |  |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |
| %4 | 0 | Port 0 |  |
| 1 | Port 1 |  |  |
| 2 | Port 2 |  |  |
| 3 | Port 3 |  |  |
| 4 | Port 4 |  |  |
| 5 | Port 5 |  |  |
| 6 | Port 6 |  |  |
| 7 | Port 7 |  |  |
| 8 | Port 8 |  |  |
| 9 | Port 9 |  |  |
| 10 | X100 |  |  |
| 11 | X101 |  |  |
| 12 | X102 |  |  |
| 13 | X103 |  |  |
| 14 | X104 |  |  |
| 15 | X105 |  |  |
| 20 | X200 |  |  |
| 21 | X201 |  |  |
| 22 | X202 |  |  |
| 23 | X203 |  |  |
| 24 | X204 |  |  |
| 25 | X205 |  |  |
| 40 | X400 |  |  |
| 41 | X401 |  |  |
| 42 | X402 |  |  |
| 50 | X500 |  |  |
| 51 | X501 |  |  |
| 52 | X502 |  |  |
| 53 | X503 |  |  |
| 54 | X504 |  |  |
| 55 | X505 |  |  |
| 56 | X506 |  |  |
| 57 | X507 |  |  |

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The topology comparison has detected a power unit in the actual topology that has
been incorrectly inserted.  
Alarm value (r2124, interpret hexadecimal):  
ddccbbaa hex:  
dd = connection number (%4)  
cc = component number (%3)  
bb = component class (% 2)  
aa = component number of the incorrectly inserted component (% 1)  
Note:  
The component is described in dd, cc and bb, where the component involved is incorrectly
inserted.  
Component class and connection number are described in F01375.  
The drive system is no longer booted. In this state, the drive control (closed-loop)
cannot be enabled.

**Remedy:**
  
Adapting topologies:  
- Insert the components involved at the right connection (correct the actual topology).  
- Adapt the project/parameterizing in the commissioning tool (correct the target topology).  
- Automatically remove the topology error (p9904).  
Note:  
Under "Topology --&gt; Topology view" the commissioning tool where relevant offers improved
diagnostics capability (e.g. setpoint/actual value comparison).

### A01382 Topology: Sensor Module incorrectly inserted

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Component: %1, to %2, %3, connection: %4

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |
| %2 | 0 | Component unknown |  |
| 1 | Control Unit |  |  |
| 2 | Motor Module |  |  |
| 3 | Line Module |  |  |
| 4 | Sensor Module |  |  |
| 5 | Voltage Sensing Module |  |  |
| 6 | Terminal Module |  |  |
| 7 | DRIVE-CLiQ Hub Module |  |  |
| 8 | Controller Extension |  |  |
| 9 | Filter module |  |  |
| 10 | Hydraulic Module |  |  |
| 49 | DRIVE-CLiQ component |  |  |
| 50 | Option slot |  |  |
| 60 | Encoder |  |  |
| 70 | DRIVE-CLiQ motor |  |  |
| 71 | Hydraulic cylinder |  |  |
| 72 | Hydraulic valve |  |  |
| 80 | Motor |  |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |
| %4 | 0 | Port 0 |  |
| 1 | Port 1 |  |  |
| 2 | Port 2 |  |  |
| 3 | Port 3 |  |  |
| 4 | Port 4 |  |  |
| 5 | Port 5 |  |  |
| 6 | Port 6 |  |  |
| 7 | Port 7 |  |  |
| 8 | Port 8 |  |  |
| 9 | Port 9 |  |  |
| 10 | X100 |  |  |
| 11 | X101 |  |  |
| 12 | X102 |  |  |
| 13 | X103 |  |  |
| 14 | X104 |  |  |
| 15 | X105 |  |  |
| 20 | X200 |  |  |
| 21 | X201 |  |  |
| 22 | X202 |  |  |
| 23 | X203 |  |  |
| 24 | X204 |  |  |
| 25 | X205 |  |  |
| 40 | X400 |  |  |
| 41 | X401 |  |  |
| 42 | X402 |  |  |
| 50 | X500 |  |  |
| 51 | X501 |  |  |
| 52 | X502 |  |  |
| 53 | X503 |  |  |
| 54 | X504 |  |  |
| 55 | X505 |  |  |
| 56 | X506 |  |  |
| 57 | X507 |  |  |

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The topology comparison has detected a Sensor Module in the actual topology that has
been incorrectly inserted with respect to the target technology.  
Alarm value (r2124, interpret hexadecimal):  
ddccbbaa hex:  
dd = connection number (%4)  
cc = component number (%3)  
bb = component class (% 2)  
aa = component number of the incorrectly inserted component (% 1)  
Note:  
The component is described in dd, cc and bb, where the component involved is incorrectly
inserted.  
Component class and connection number are described in F01375.  
The drive system is no longer booted. In this state, the drive control (closed-loop)
cannot be enabled.

**Remedy:**
  
Adapting topologies:  
- Insert the components involved at the right connection (correct the actual topology).  
- Adapt the project/parameterizing in the commissioning tool (correct the target topology).  
- Automatically remove the topology error (p9904).  
Note:  
Under "Topology --&gt; Topology view" the commissioning tool where relevant offers improved
diagnostics capability (e.g. setpoint/actual value comparison).

### A01383 Topology: Terminal Module incorrectly inserted

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Component: %1, to %2, %3, connection: %4

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |
| %2 | 0 | Component unknown |  |
| 1 | Control Unit |  |  |
| 2 | Motor Module |  |  |
| 3 | Line Module |  |  |
| 4 | Sensor Module |  |  |
| 5 | Voltage Sensing Module |  |  |
| 6 | Terminal Module |  |  |
| 7 | DRIVE-CLiQ Hub Module |  |  |
| 8 | Controller Extension |  |  |
| 9 | Filter module |  |  |
| 10 | Hydraulic Module |  |  |
| 49 | DRIVE-CLiQ component |  |  |
| 50 | Option slot |  |  |
| 60 | Encoder |  |  |
| 70 | DRIVE-CLiQ motor |  |  |
| 71 | Hydraulic cylinder |  |  |
| 72 | Hydraulic valve |  |  |
| 80 | Motor |  |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |
| %4 | 0 | Port 0 |  |
| 1 | Port 1 |  |  |
| 2 | Port 2 |  |  |
| 3 | Port 3 |  |  |
| 4 | Port 4 |  |  |
| 5 | Port 5 |  |  |
| 6 | Port 6 |  |  |
| 7 | Port 7 |  |  |
| 8 | Port 8 |  |  |
| 9 | Port 9 |  |  |
| 10 | X100 |  |  |
| 11 | X101 |  |  |
| 12 | X102 |  |  |
| 13 | X103 |  |  |
| 14 | X104 |  |  |
| 15 | X105 |  |  |
| 20 | X200 |  |  |
| 21 | X201 |  |  |
| 22 | X202 |  |  |
| 23 | X203 |  |  |
| 24 | X204 |  |  |
| 25 | X205 |  |  |
| 40 | X400 |  |  |
| 41 | X401 |  |  |
| 42 | X402 |  |  |
| 50 | X500 |  |  |
| 51 | X501 |  |  |
| 52 | X502 |  |  |
| 53 | X503 |  |  |
| 54 | X504 |  |  |
| 55 | X505 |  |  |
| 56 | X506 |  |  |
| 57 | X507 |  |  |

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The topology comparison has detected a Terminal Module in the actual topology that
has been incorrectly inserted with respect to the target technology.  
Alarm value (r2124, interpret hexadecimal):  
ddccbbaa hex:  
dd = connection number (%4)  
cc = component number (%3)  
bb = component class (% 2)  
aa = component number of the incorrectly inserted component (% 1)  
Note:  
The component is described in dd, cc and bb, where the component involved is incorrectly
inserted.  
Component class and connection number are described in F01375.  
The drive system is no longer booted. In this state, the drive control (closed-loop)
cannot be enabled.

**Remedy:**
  
Adapting topologies:  
- Insert the components involved at the right connection (correct the actual topology).  
- Adapt the project/parameterizing in the commissioning tool (correct the target topology).  
- Automatically remove the topology error (p9904).  
Note:  
Under "Topology --&gt; Topology view" the commissioning tool where relevant offers improved
diagnostics capability (e.g. setpoint/actual value comparison).

### A01384 Topology: DRIVE-CLiQ Hub Module incorrectly inserted

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Component: %1, to %2, %3, connection: %4

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |
| %2 | 0 | Component unknown |  |
| 1 | Control Unit |  |  |
| 2 | Motor Module |  |  |
| 3 | Line Module |  |  |
| 4 | Sensor Module |  |  |
| 5 | Voltage Sensing Module |  |  |
| 6 | Terminal Module |  |  |
| 7 | DRIVE-CLiQ Hub Module |  |  |
| 8 | Controller Extension |  |  |
| 9 | Filter module |  |  |
| 10 | Hydraulic Module |  |  |
| 49 | DRIVE-CLiQ component |  |  |
| 50 | Option slot |  |  |
| 60 | Encoder |  |  |
| 70 | DRIVE-CLiQ motor |  |  |
| 71 | Hydraulic cylinder |  |  |
| 72 | Hydraulic valve |  |  |
| 80 | Motor |  |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |
| %4 | 0 | Port 0 |  |
| 1 | Port 1 |  |  |
| 2 | Port 2 |  |  |
| 3 | Port 3 |  |  |
| 4 | Port 4 |  |  |
| 5 | Port 5 |  |  |
| 6 | Port 6 |  |  |
| 7 | Port 7 |  |  |
| 8 | Port 8 |  |  |
| 9 | Port 9 |  |  |
| 10 | X100 |  |  |
| 11 | X101 |  |  |
| 12 | X102 |  |  |
| 13 | X103 |  |  |
| 14 | X104 |  |  |
| 15 | X105 |  |  |
| 20 | X200 |  |  |
| 21 | X201 |  |  |
| 22 | X202 |  |  |
| 23 | X203 |  |  |
| 24 | X204 |  |  |
| 25 | X205 |  |  |
| 40 | X400 |  |  |
| 41 | X401 |  |  |
| 42 | X402 |  |  |
| 50 | X500 |  |  |
| 51 | X501 |  |  |
| 52 | X502 |  |  |
| 53 | X503 |  |  |
| 54 | X504 |  |  |
| 55 | X505 |  |  |
| 56 | X506 |  |  |
| 57 | X507 |  |  |

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The topology comparison has detected a DRIVE-CLiQ Hub Module in the actual topology
that has been incorrectly inserted with respect to the target topology.  
Alarm value (r2124, interpret hexadecimal):  
ddccbbaa hex:  
dd = connection number (%4)  
cc = component number (%3)  
bb = component class (% 2)  
aa = component number of the incorrectly inserted component (% 1)  
Note:  
The component is described in dd, cc and bb, where the component involved is incorrectly
inserted.  
Component class and connection number are described in F01375.  
The drive system is no longer booted. In this state, the drive control (closed-loop)
cannot be enabled.

**Remedy:**
  
Adapting topologies:  
- Insert the components involved at the right connection (correct the actual topology).  
- Adapt the project/parameterizing in the commissioning tool (correct the target topology).  
- Automatically remove the topology error (p9904).  
Note:  
Under "Topology --&gt; Topology view" the commissioning tool where relevant offers improved
diagnostics capability (e.g. setpoint/actual value comparison).

### A01385 Topology: Controller Extension incorrectly inserted

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Component: %1, to %2, %3, connection: %4

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |
| %2 | 0 | Component unknown |  |
| 1 | Control Unit |  |  |
| 2 | Motor Module |  |  |
| 3 | Line Module |  |  |
| 4 | Sensor Module |  |  |
| 5 | Voltage Sensing Module |  |  |
| 6 | Terminal Module |  |  |
| 7 | DRIVE-CLiQ Hub Module |  |  |
| 8 | Controller Extension |  |  |
| 9 | Filter module |  |  |
| 10 | Hydraulic Module |  |  |
| 49 | DRIVE-CLiQ component |  |  |
| 50 | Option slot |  |  |
| 60 | Encoder |  |  |
| 70 | DRIVE-CLiQ motor |  |  |
| 71 | Hydraulic cylinder |  |  |
| 72 | Hydraulic valve |  |  |
| 80 | Motor |  |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |
| %4 | 0 | Port 0 |  |
| 1 | Port 1 |  |  |
| 2 | Port 2 |  |  |
| 3 | Port 3 |  |  |
| 4 | Port 4 |  |  |
| 5 | Port 5 |  |  |
| 6 | Port 6 |  |  |
| 7 | Port 7 |  |  |
| 8 | Port 8 |  |  |
| 9 | Port 9 |  |  |
| 10 | X100 |  |  |
| 11 | X101 |  |  |
| 12 | X102 |  |  |
| 13 | X103 |  |  |
| 14 | X104 |  |  |
| 15 | X105 |  |  |
| 20 | X200 |  |  |
| 21 | X201 |  |  |
| 22 | X202 |  |  |
| 23 | X203 |  |  |
| 24 | X204 |  |  |
| 25 | X205 |  |  |
| 40 | X400 |  |  |
| 41 | X401 |  |  |
| 42 | X402 |  |  |
| 50 | X500 |  |  |
| 51 | X501 |  |  |
| 52 | X502 |  |  |
| 53 | X503 |  |  |
| 54 | X504 |  |  |
| 55 | X505 |  |  |
| 56 | X506 |  |  |
| 57 | X507 |  |  |

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The topology comparison has detected a controller extension 32 (CX32) in the actual
topology that has been incorrectly inserted with respect to the target topology.  
Alarm value (r2124, interpret hexadecimal):  
ddccbbaa hex:  
dd = connection number (%4)  
cc = component number (%3)  
bb = component class (% 2)  
aa = component number of the incorrectly inserted component (% 1)  
Note:  
The component is described in dd, cc and bb, where the component involved is incorrectly
inserted.  
Component class and connection number are described in F01375.  
The drive system is no longer booted. In this state, the drive control (closed-loop)
cannot be enabled.

**Remedy:**
  
Adapting topologies:  
- Insert the components involved at the right connection (correct the actual topology).  
- Adapt the project/parameterizing in the commissioning tool (correct the target topology).  
- Automatically remove the topology error (p9904).  
Note:  
Under "Topology --&gt; Topology view" the commissioning tool where relevant offers improved
diagnostics capability (e.g. setpoint/actual value comparison).

### A01386 Topology: DRIVE-CLiQ component incorrectly inserted

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Component: %1, to %2, %3, connection: %4

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |
| %2 | 0 | Component unknown |  |
| 1 | Control Unit |  |  |
| 2 | Motor Module |  |  |
| 3 | Line Module |  |  |
| 4 | Sensor Module |  |  |
| 5 | Voltage Sensing Module |  |  |
| 6 | Terminal Module |  |  |
| 7 | DRIVE-CLiQ Hub Module |  |  |
| 8 | Controller Extension |  |  |
| 9 | Filter module |  |  |
| 10 | Hydraulic Module |  |  |
| 49 | DRIVE-CLiQ component |  |  |
| 50 | Option slot |  |  |
| 60 | Encoder |  |  |
| 70 | DRIVE-CLiQ motor |  |  |
| 71 | Hydraulic cylinder |  |  |
| 72 | Hydraulic valve |  |  |
| 80 | Motor |  |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |
| %4 | 0 | Port 0 |  |
| 1 | Port 1 |  |  |
| 2 | Port 2 |  |  |
| 3 | Port 3 |  |  |
| 4 | Port 4 |  |  |
| 5 | Port 5 |  |  |
| 6 | Port 6 |  |  |
| 7 | Port 7 |  |  |
| 8 | Port 8 |  |  |
| 9 | Port 9 |  |  |
| 10 | X100 |  |  |
| 11 | X101 |  |  |
| 12 | X102 |  |  |
| 13 | X103 |  |  |
| 14 | X104 |  |  |
| 15 | X105 |  |  |
| 20 | X200 |  |  |
| 21 | X201 |  |  |
| 22 | X202 |  |  |
| 23 | X203 |  |  |
| 24 | X204 |  |  |
| 25 | X205 |  |  |
| 40 | X400 |  |  |
| 41 | X401 |  |  |
| 42 | X402 |  |  |
| 50 | X500 |  |  |
| 51 | X501 |  |  |
| 52 | X502 |  |  |
| 53 | X503 |  |  |
| 54 | X504 |  |  |
| 55 | X505 |  |  |
| 56 | X506 |  |  |
| 57 | X507 |  |  |

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The topology comparison has detected a DRIVE-CLiQ component in the actual topology
that has been incorrectly inserted with respect to the target topology.  
Alarm value (r2124, interpret hexadecimal):  
ddccbbaa hex:  
dd = connection number (%4)  
cc = component number (%3)  
bb = component class (% 2)  
aa = component number of the incorrectly inserted component (% 1)  
Note:  
The component is described in dd, cc and bb, where the component involved is incorrectly
inserted.  
Component class and connection number are described in F01375.  
The drive system is no longer booted. In this state, the drive control (closed-loop)
cannot be enabled.

**Remedy:**
  
Adapting topologies:  
- Insert the components involved at the right connection (correct the actual topology).  
- Adapt the project/parameterizing in the commissioning tool (correct the target topology).  
- Automatically remove the topology error (p9904).  
Note:  
Under "Topology --&gt; Topology view" the commissioning tool where relevant offers improved
diagnostics capability (e.g. setpoint/actual value comparison).

### A01387 Topology: Option slot component incorrectly inserted

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Component: %1, to %2, %3, connection: %4

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |
| %2 | 0 | Component unknown |  |
| 1 | Control Unit |  |  |
| 2 | Motor Module |  |  |
| 3 | Line Module |  |  |
| 4 | Sensor Module |  |  |
| 5 | Voltage Sensing Module |  |  |
| 6 | Terminal Module |  |  |
| 7 | DRIVE-CLiQ Hub Module |  |  |
| 8 | Controller Extension |  |  |
| 9 | Filter module |  |  |
| 10 | Hydraulic Module |  |  |
| 49 | DRIVE-CLiQ component |  |  |
| 50 | Option slot |  |  |
| 60 | Encoder |  |  |
| 70 | DRIVE-CLiQ motor |  |  |
| 71 | Hydraulic cylinder |  |  |
| 72 | Hydraulic valve |  |  |
| 80 | Motor |  |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |
| %4 | 0 | Port 0 |  |
| 1 | Port 1 |  |  |
| 2 | Port 2 |  |  |
| 3 | Port 3 |  |  |
| 4 | Port 4 |  |  |
| 5 | Port 5 |  |  |
| 6 | Port 6 |  |  |
| 7 | Port 7 |  |  |
| 8 | Port 8 |  |  |
| 9 | Port 9 |  |  |
| 10 | X100 |  |  |
| 11 | X101 |  |  |
| 12 | X102 |  |  |
| 13 | X103 |  |  |
| 14 | X104 |  |  |
| 15 | X105 |  |  |
| 20 | X200 |  |  |
| 21 | X201 |  |  |
| 22 | X202 |  |  |
| 23 | X203 |  |  |
| 24 | X204 |  |  |
| 25 | X205 |  |  |
| 40 | X400 |  |  |
| 41 | X401 |  |  |
| 42 | X402 |  |  |
| 50 | X500 |  |  |
| 51 | X501 |  |  |
| 52 | X502 |  |  |
| 53 | X503 |  |  |
| 54 | X504 |  |  |
| 55 | X505 |  |  |
| 56 | X506 |  |  |
| 57 | X507 |  |  |

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The topology comparison has detected an option slot component in the actual topology
that has been incorrectly inserted with respect to the target topology.  
Alarm value (r2124, interpret hexadecimal):  
ddccbbaa hex:  
dd = connection number (%4)  
cc = component number (%3)  
bb = component class (% 2)  
aa = component number of the incorrectly inserted component (% 1)  
Note:  
The component is described in dd, cc and bb, where the component involved is incorrectly
inserted.  
Component class and connection number are described in F01375.  
The drive system is no longer booted. In this state, the drive control (closed-loop)
cannot be enabled.

**Remedy:**
  
Adapting topologies:  
- Insert the components involved at the right connection (correct the actual topology).  
- Adapt the project/parameterizing in the commissioning tool (correct the target topology).  
- Automatically remove the topology error (p9904).  
Note:  
Under "Topology --&gt; Topology view" the commissioning tool where relevant offers improved
diagnostics capability (e.g. setpoint/actual value comparison).

### A01388 Topology: EnDat encoder incorrectly inserted

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Component: %1, to %2, %3, connection: %4

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |
| %2 | 0 | Component unknown |  |
| 1 | Control Unit |  |  |
| 2 | Motor Module |  |  |
| 3 | Line Module |  |  |
| 4 | Sensor Module |  |  |
| 5 | Voltage Sensing Module |  |  |
| 6 | Terminal Module |  |  |
| 7 | DRIVE-CLiQ Hub Module |  |  |
| 8 | Controller Extension |  |  |
| 9 | Filter module |  |  |
| 10 | Hydraulic Module |  |  |
| 49 | DRIVE-CLiQ component |  |  |
| 50 | Option slot |  |  |
| 60 | Encoder |  |  |
| 70 | DRIVE-CLiQ motor |  |  |
| 71 | Hydraulic cylinder |  |  |
| 72 | Hydraulic valve |  |  |
| 80 | Motor |  |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |
| %4 | 0 | Port 0 |  |
| 1 | Port 1 |  |  |
| 2 | Port 2 |  |  |
| 3 | Port 3 |  |  |
| 4 | Port 4 |  |  |
| 5 | Port 5 |  |  |
| 6 | Port 6 |  |  |
| 7 | Port 7 |  |  |
| 8 | Port 8 |  |  |
| 9 | Port 9 |  |  |
| 10 | X100 |  |  |
| 11 | X101 |  |  |
| 12 | X102 |  |  |
| 13 | X103 |  |  |
| 14 | X104 |  |  |
| 15 | X105 |  |  |
| 20 | X200 |  |  |
| 21 | X201 |  |  |
| 22 | X202 |  |  |
| 23 | X203 |  |  |
| 24 | X204 |  |  |
| 25 | X205 |  |  |
| 40 | X400 |  |  |
| 41 | X401 |  |  |
| 42 | X402 |  |  |
| 50 | X500 |  |  |
| 51 | X501 |  |  |
| 52 | X502 |  |  |
| 53 | X503 |  |  |
| 54 | X504 |  |  |
| 55 | X505 |  |  |
| 56 | X506 |  |  |
| 57 | X507 |  |  |

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The topology comparison has detected an EnDat encoder in the actual topology that
has been incorrectly inserted with respect to the target topology.  
Alarm value (r2124, interpret hexadecimal):  
ddccbbaa hex:  
dd = connection number (%4)  
cc = component number (%3)  
bb = component class (% 2)  
aa = component number of the incorrectly inserted component (% 1)  
Note:  
The component is described in dd, cc and bb, where the component involved is incorrectly
inserted.  
Component class and connection number are described in F01375.  
The drive system is no longer booted. In this state, the drive control (closed-loop)
cannot be enabled.

**Remedy:**
  
Adapting topologies:  
- Insert the components involved at the right connection (correct the actual topology).  
- Adapt the project/parameterizing in the commissioning tool (correct the target topology).  
- Automatically remove the topology error (p9904).  
Note:  
Under "Topology --&gt; Topology view" the commissioning tool where relevant offers improved
diagnostics capability (e.g. setpoint/actual value comparison).

### A01389 Topology: Motor with DRIVE-CLiQ incorrectly inserted

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Component: %1, to %2, %3, connection: %4

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |
| %2 | 0 | Component unknown |  |
| 1 | Control Unit |  |  |
| 2 | Motor Module |  |  |
| 3 | Line Module |  |  |
| 4 | Sensor Module |  |  |
| 5 | Voltage Sensing Module |  |  |
| 6 | Terminal Module |  |  |
| 7 | DRIVE-CLiQ Hub Module |  |  |
| 8 | Controller Extension |  |  |
| 9 | Filter module |  |  |
| 10 | Hydraulic Module |  |  |
| 49 | DRIVE-CLiQ component |  |  |
| 50 | Option slot |  |  |
| 60 | Encoder |  |  |
| 70 | DRIVE-CLiQ motor |  |  |
| 71 | Hydraulic cylinder |  |  |
| 72 | Hydraulic valve |  |  |
| 80 | Motor |  |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |
| %4 | 0 | Port 0 |  |
| 1 | Port 1 |  |  |
| 2 | Port 2 |  |  |
| 3 | Port 3 |  |  |
| 4 | Port 4 |  |  |
| 5 | Port 5 |  |  |
| 6 | Port 6 |  |  |
| 7 | Port 7 |  |  |
| 8 | Port 8 |  |  |
| 9 | Port 9 |  |  |
| 10 | X100 |  |  |
| 11 | X101 |  |  |
| 12 | X102 |  |  |
| 13 | X103 |  |  |
| 14 | X104 |  |  |
| 15 | X105 |  |  |
| 20 | X200 |  |  |
| 21 | X201 |  |  |
| 22 | X202 |  |  |
| 23 | X203 |  |  |
| 24 | X204 |  |  |
| 25 | X205 |  |  |
| 40 | X400 |  |  |
| 41 | X401 |  |  |
| 42 | X402 |  |  |
| 50 | X500 |  |  |
| 51 | X501 |  |  |
| 52 | X502 |  |  |
| 53 | X503 |  |  |
| 54 | X504 |  |  |
| 55 | X505 |  |  |
| 56 | X506 |  |  |
| 57 | X507 |  |  |

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The topology comparison has detected a motor with DRIVE-CLiQ in the actual topology
that has been incorrectly inserted with respect to the target topology.  
Alarm value (r2124, interpret hexadecimal):  
ddccbbaa hex:  
dd = connection number (%4)  
cc = component number (%3)  
bb = component class (% 2)  
aa = component number of the incorrectly inserted component (% 1)  
Note:  
The component is described in dd, cc and bb, where the component involved is incorrectly
inserted.  
Component class and connection number are described in F01375.  
The drive system is no longer booted. In this state, the drive control (closed-loop)
cannot be enabled.

**Remedy:**
  
Adapting topologies:  
- Insert the components involved at the right connection (correct the actual topology).  
- Adapt the project/parameterizing in the commissioning tool (correct the target topology).  
- Automatically remove the topology error (p9904).  
Note:  
Under "Topology --&gt; Topology view" the commissioning tool where relevant offers improved
diagnostics capability (e.g. setpoint/actual value comparison).

## SINAMICS Alarms TM31 (Terminal Module) 01416 - 02152

SINAMICS Alarms TM31 (Terminal Module) 01416 - 02152

### A01416 Topology: Component additionally inserted

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1, to %2, %3, connection: %4

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |
| %1, %2 | 0 | Component unknown |  |
| 1 | Control Unit |  |  |
| 2 | Motor Module |  |  |
| 3 | Line Module |  |  |
| 4 | Sensor Module |  |  |
| 5 | Voltage Sensing Module |  |  |
| 6 | Terminal Module |  |  |
| 7 | DRIVE-CLiQ Hub Module |  |  |
| 8 | Controller Extension |  |  |
| 9 | Filter module |  |  |
| 10 | Hydraulic Module |  |  |
| 49 | DRIVE-CLiQ component |  |  |
| 50 | Option slot |  |  |
| 60 | Encoder |  |  |
| 70 | DRIVE-CLiQ motor |  |  |
| 71 | Hydraulic cylinder |  |  |
| 72 | Hydraulic valve |  |  |
| 80 | Motor |  |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |
| %4 | 0 | Port 0 |  |
| 1 | Port 1 |  |  |
| 2 | Port 2 |  |  |
| 3 | Port 3 |  |  |
| 4 | Port 4 |  |  |
| 5 | Port 5 |  |  |
| 6 | Port 6 |  |  |
| 7 | Port 7 |  |  |
| 8 | Port 8 |  |  |
| 9 | Port 9 |  |  |
| 10 | X100 |  |  |
| 11 | X101 |  |  |
| 12 | X102 |  |  |
| 13 | X103 |  |  |
| 14 | X104 |  |  |
| 15 | X105 |  |  |
| 20 | X200 |  |  |
| 21 | X201 |  |  |
| 22 | X202 |  |  |
| 23 | X203 |  |  |
| 24 | X204 |  |  |
| 25 | X205 |  |  |
| 40 | X400 |  |  |
| 41 | X401 |  |  |
| 42 | X402 |  |  |
| 50 | X500 |  |  |
| 51 | X501 |  |  |
| 52 | X502 |  |  |
| 53 | X503 |  |  |
| 54 | X504 |  |  |
| 55 | X505 |  |  |
| 56 | X506 |  |  |
| 57 | X507 |  |  |

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The topology comparison has found a component in the actual topology which is not
specified in the target topology.  
Alarm value (r2124, interpret hexadecimal):  
ddccbbaa hex:  
dd = component class (% 2)  
cc = connection number (%4)  
bb = component class of the additional component (%1)  
aa = component number (%3)  
Note:  
The component class of the additional component is contained in bb.  
The component is described in dd, cc and aa, where the additional component is inserted.  
Component class and connection number are described in F01375.

**Remedy:**
  
Adapting topologies:  
- Remove the additional component (correct the actual topology).  
- Adapt the project/parameterizing in the commissioning tool (correct the target topology).  
Note:  
Under "Topology --&gt; Topology view" the commissioning tool where relevant offers improved
diagnostics capability (e.g. setpoint/actual value comparison).

### A01420 Topology: Component different

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Component: %1, target: %2, actual: %3, difference: %4

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |
| %2, %3 | 0 | Component unknown |  |
| 1 | Control Unit |  |  |
| 2 | Motor Module |  |  |
| 3 | Line Module |  |  |
| 4 | Sensor Module |  |  |
| 5 | Voltage Sensing Module |  |  |
| 6 | Terminal Module |  |  |
| 7 | DRIVE-CLiQ Hub Module |  |  |
| 8 | Controller Extension |  |  |
| 9 | Filter module |  |  |
| 10 | Hydraulic Module |  |  |
| 49 | DRIVE-CLiQ component |  |  |
| 50 | Option slot |  |  |
| 60 | Encoder |  |  |
| 70 | DRIVE-CLiQ motor |  |  |
| 71 | Hydraulic cylinder |  |  |
| 72 | Hydraulic valve |  |  |
| 80 | Motor |  |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |
| %4 | 1 | Component type |  |
| 2 | Article number |  |  |
| 3 | Manufacturer |  |  |
| 4 | Incorrect subcomponent connected |  |  |
| 5 | NX instead of CX |  |  |
| 6 | CX instead of NX |  |  |
| 7 | Number of connections |  |  |

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The topology comparison has detected differences in the actual topology and target
topologies relating to the electronic rating plate.  
Alarm value (r2124, interpret hexadecimal):  
ddccbbaa hex: aa = component number (%1), bb = component class of the target topology
(%2), cc = component class of the actual topology (%3), dd = difference (%4)  
dd = 01 hex = 1 dec:  
Different component type.  
dd = 02 hex = 2 dec:  
Different article number.  
dd = 03 hex = 3 dec:  
Different manufacturer.  
dd = 04 hex = 4 dec:  
For a multi-component slave, the incorrect subcomponent (index) is connected (e.g.
Double Motor Module X201 instead of X200) - or only a part of a multi-component slave
is set to "deactivate and not available".  
dd = 05 hex = 5 dec:  
NX10 or NX15 used instead of CX32.  
dd = 06 hex = 6 dec:  
NX10 or NX15 used instead of CX32.  
dd = 07 hex = 7 dec:  
Different number of connections.  
Note:  
The component class is described in F01375.  
The drive system is no longer booted. In this state, the drive control (closed-loop)
cannot be enabled.

**Remedy:**
  
Adapting topologies:  
- Connect the expected component (correct the actual topology).  
- Adapt the project/parameterizing in the commissioning tool (correct the target topology).  
Topology comparison - If required, adapt the comparison level:  
- Parameterize the topology comparison of all components (p9906).  
- Parameterize the topology comparison of one components (p9907, p9908).  
Note:  
Under "Topology --&gt; Topology view" the commissioning tool where relevant offers improved
diagnostics capability (e.g. setpoint/actual value comparison).

### A01425 Topology: Serial number different

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Component: %1, %2, differences: %3

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |
| %2 | 0 | Component unknown |  |
| 1 | Control Unit |  |  |
| 2 | Motor Module |  |  |
| 3 | Line Module |  |  |
| 4 | Sensor Module |  |  |
| 5 | Voltage Sensing Module |  |  |
| 6 | Terminal Module |  |  |
| 7 | DRIVE-CLiQ Hub Module |  |  |
| 8 | Controller Extension |  |  |
| 9 | Filter module |  |  |
| 10 | Hydraulic Module |  |  |
| 49 | DRIVE-CLiQ component |  |  |
| 50 | Option slot |  |  |
| 60 | Encoder |  |  |
| 70 | DRIVE-CLiQ motor |  |  |
| 71 | Hydraulic cylinder |  |  |
| 72 | Hydraulic valve |  |  |
| 80 | Motor |  |  |

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The topology comparison has detected differences in the actual and target topologies
in relation to one component. The serial number is different.  
Alarm value (r2124, interpret hexadecimal):  
ddccbbaa hex:  
dd = reserved  
cc = number of differences (%3)  
bb = component class (% 2)  
aa = component number (%1)  
Note:  
The component class is described in F01375.  
The drive system is no longer booted. In this state, the drive control (closed-loop)
cannot be enabled.

**Remedy:**
  
Adapting topologies:  
- Change over the actual topology to match the target topology.  
- Load the target topology that matches the actual topology (commissioning tool).  
For byte cc:  
cc = 1 --&gt; can be acknowledged using p9904 or p9905.  
cc &gt; 1 --&gt; can be acknowledged using p9905 and can be deactivated using p9906 or p9907/p9908.  
Note:  
Under "Topology --&gt; Topology view" the commissioning tool where relevant offers improved
diagnostics capability (e.g. setpoint/actual value comparison).  
See also: p9904 (Topology comparison acknowledge differences), p9905 (Device specialization),
p9906 (Topology comparison all components comparison level), p9907 (Topology comparison
component number), p9908 (Topology comparison of a component comparison level)

### A01428 Topology: Incorrect connection used

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Component: %1, %2, connection (actual): %3, connection (target): %4

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |
| %2 | 0 | Component unknown |  |
| 1 | Control Unit |  |  |
| 2 | Motor Module |  |  |
| 3 | Line Module |  |  |
| 4 | Sensor Module |  |  |
| 5 | Voltage Sensing Module |  |  |
| 6 | Terminal Module |  |  |
| 7 | DRIVE-CLiQ Hub Module |  |  |
| 8 | Controller Extension |  |  |
| 9 | Filter module |  |  |
| 10 | Hydraulic Module |  |  |
| 49 | DRIVE-CLiQ component |  |  |
| 50 | Option slot |  |  |
| 60 | Encoder |  |  |
| 70 | DRIVE-CLiQ motor |  |  |
| 71 | Hydraulic cylinder |  |  |
| 72 | Hydraulic valve |  |  |
| 80 | Motor |  |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |
| %3, %4 | 0 | Port 0 |  |
| 1 | Port 1 |  |  |
| 2 | Port 2 |  |  |
| 3 | Port 3 |  |  |
| 4 | Port 4 |  |  |
| 5 | Port 5 |  |  |
| 6 | Port 6 |  |  |
| 7 | Port 7 |  |  |
| 8 | Port 8 |  |  |
| 9 | Port 9 |  |  |
| 10 | X100 |  |  |
| 11 | X101 |  |  |
| 12 | X102 |  |  |
| 13 | X103 |  |  |
| 14 | X104 |  |  |
| 15 | X105 |  |  |
| 20 | X200 |  |  |
| 21 | X201 |  |  |
| 22 | X202 |  |  |
| 23 | X203 |  |  |
| 24 | X204 |  |  |
| 25 | X205 |  |  |
| 40 | X400 |  |  |
| 41 | X401 |  |  |
| 42 | X402 |  |  |
| 50 | X500 |  |  |
| 51 | X501 |  |  |
| 52 | X502 |  |  |
| 53 | X503 |  |  |
| 54 | X504 |  |  |
| 55 | X505 |  |  |
| 56 | X506 |  |  |
| 57 | X507 |  |  |

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The topology comparison has detected differences in the actual and target topologies
in relation to one component. For a component, another connection was used.  
The different connections of a component are described in the alarm value.  
Alarm value (r2124, interpret hexadecimal):  
ddccbbaa hex:  
dd = connection number of the target topology (%4)  
cc = connection number of the actual topology (%3)  
bb = component class (% 2)  
aa = component number (%1)  
Note:  
Component class and connection number are described in F01375.  
The drive system is no longer booted. In this state, the drive control (closed-loop)
cannot be enabled.

**Remedy:**
  
Adapting topologies:  
- Reinsert the DRIVE-CLiQ cable to the component (correct the actual topology).  
- Adapt the project/parameterizing in the commissioning tool (correct the target topology).  
- Automatically remove the topology error (p9904).  
Note:  
Under "Topology --&gt; Topology view" the commissioning tool where relevant offers improved
diagnostics capability (e.g. setpoint/actual value comparison).  
See also: p9904 (Topology comparison acknowledge differences)

### A01429 Topology: Comparison connection is different for more than one component

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Component: %1, %2, connection (actual): %3, connection (target): %4

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |
| %2 | 0 | Component unknown |  |
| 1 | Control Unit |  |  |
| 2 | Motor Module |  |  |
| 3 | Line Module |  |  |
| 4 | Sensor Module |  |  |
| 5 | Voltage Sensing Module |  |  |
| 6 | Terminal Module |  |  |
| 7 | DRIVE-CLiQ Hub Module |  |  |
| 8 | Controller Extension |  |  |
| 9 | Filter module |  |  |
| 10 | Hydraulic Module |  |  |
| 49 | DRIVE-CLiQ component |  |  |
| 50 | Option slot |  |  |
| 60 | Encoder |  |  |
| 70 | DRIVE-CLiQ motor |  |  |
| 71 | Hydraulic cylinder |  |  |
| 72 | Hydraulic valve |  |  |
| 80 | Motor |  |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |
| %3, %4 | 0 | Port 0 |  |
| 1 | Port 1 |  |  |
| 2 | Port 2 |  |  |
| 3 | Port 3 |  |  |
| 4 | Port 4 |  |  |
| 5 | Port 5 |  |  |
| 6 | Port 6 |  |  |
| 7 | Port 7 |  |  |
| 8 | Port 8 |  |  |
| 9 | Port 9 |  |  |
| 10 | X100 |  |  |
| 11 | X101 |  |  |
| 12 | X102 |  |  |
| 13 | X103 |  |  |
| 14 | X104 |  |  |
| 15 | X105 |  |  |
| 20 | X200 |  |  |
| 21 | X201 |  |  |
| 22 | X202 |  |  |
| 23 | X203 |  |  |
| 24 | X204 |  |  |
| 25 | X205 |  |  |
| 40 | X400 |  |  |
| 41 | X401 |  |  |
| 42 | X402 |  |  |
| 50 | X500 |  |  |
| 51 | X501 |  |  |
| 52 | X502 |  |  |
| 53 | X503 |  |  |
| 54 | X504 |  |  |
| 55 | X505 |  |  |
| 56 | X506 |  |  |
| 57 | X507 |  |  |

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
A topology comparison has found differences between the actual and target topology
for several components. A component was connected to another connection.  
The different connections of a component are described in the alarm value:  
Alarm value (r2124, interpret hexadecimal):  
ddccbbaa hex:  
dd = connection number of the target topology  
cc = connection number of the actual topology  
bb = component class  
aa = component number  
Note:  
Connection number is described in F01375.  
The drive system is no longer booted. In this state, the drive control (closed-loop)
cannot be enabled.

**Remedy:**
  
Adapting topologies:  
- Change over the actual topology to match the target topology.  
- Load the target topology that matches the actual topology (commissioning tool).  
Note:  
In the software, a Double Motor Module behaves just like two separate DRIVE-CLiQ nodes.
If a Double Motor Module is re-inserted, this can result in several differences in
the actual topology.  
Under "Topology --&gt; Topology view" the commissioning tool where relevant offers improved
diagnostics capability (e.g. setpoint/actual value comparison).

### F01451 Topology: Target topology is invalid

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
An error was detected in the target topology.  
The target topology is invalid.  
Fault value (r0949, interpret hexadecimal):  
ccccbbaa hex: cccc = index error, bb = component number, aa = fault cause  
aa = 1B hex = 27 dec: Error not specified.  
aa = 1C hex = 28 dec: Value illegal.  
aa = 1D hex = 29 dec: Incorrect ID.  
aa = 1E hex = 30 dec: Incorrect ID length.  
aa = 1F hex = 31 dec: Too few indices left.  
aa = 20 hex = 32 dec: component not connected to Control Unit.

**Remedy:**
  
Download the target topology again using the commissioning tool.

### F01470 Topology:Target topology ring-type connection detected

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1, to %2, %3, connection: %4

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |
| %1, %2 | 0 | Component unknown |  |
| 1 | Control Unit |  |  |
| 2 | Motor Module |  |  |
| 3 | Line Module |  |  |
| 4 | Sensor Module |  |  |
| 5 | Voltage Sensing Module |  |  |
| 6 | Terminal Module |  |  |
| 7 | DRIVE-CLiQ Hub Module |  |  |
| 8 | Controller Extension |  |  |
| 9 | Filter module |  |  |
| 10 | Hydraulic Module |  |  |
| 49 | DRIVE-CLiQ component |  |  |
| 50 | Option slot |  |  |
| 60 | Encoder |  |  |
| 70 | DRIVE-CLiQ motor |  |  |
| 71 | Hydraulic cylinder |  |  |
| 72 | Hydraulic valve |  |  |
| 80 | Motor |  |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |
| %4 | 0 | Port 0 |  |
| 1 | Port 1 |  |  |
| 2 | Port 2 |  |  |
| 3 | Port 3 |  |  |
| 4 | Port 4 |  |  |
| 5 | Port 5 |  |  |
| 6 | Port 6 |  |  |
| 7 | Port 7 |  |  |
| 8 | Port 8 |  |  |
| 9 | Port 9 |  |  |
| 10 | X100 |  |  |
| 11 | X101 |  |  |
| 12 | X102 |  |  |
| 13 | X103 |  |  |
| 14 | X104 |  |  |
| 15 | X105 |  |  |
| 20 | X200 |  |  |
| 21 | X201 |  |  |
| 22 | X202 |  |  |
| 23 | X203 |  |  |
| 24 | X204 |  |  |
| 25 | X205 |  |  |
| 40 | X400 |  |  |
| 41 | X401 |  |  |
| 42 | X402 |  |  |
| 50 | X500 |  |  |
| 51 | X501 |  |  |
| 52 | X502 |  |  |
| 53 | X503 |  |  |
| 54 | X504 |  |  |
| 55 | X505 |  |  |
| 56 | X506 |  |  |
| 57 | X507 |  |  |

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A ring-type connection was detected when writing to the target topology.  
Fault value (r0949, interpret hexadecimal):  
ddccbbaa hex:  
cc = connection number  
bb = component class  
aa = component number of a component included in the ring  
Note:  
Connection number is described in F01375.

**Remedy:**
  
Read out the fault value and remove one of the specified connections.  
Then download the target topology again using the commissioning tool.  
Note:  
Under "Topology --&gt; Topology view" the commissioning tool where relevant offers improved
diagnostics capability (e.g. setpoint/actual value comparison).

### F01475 Topology: Target topology duplicate connection between two components

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Component: %1, %2, connection (actual): %3, connection (target): %4

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |
| %2 | 0 | Component unknown |  |
| 1 | Control Unit |  |  |
| 2 | Motor Module |  |  |
| 3 | Line Module |  |  |
| 4 | Sensor Module |  |  |
| 5 | Voltage Sensing Module |  |  |
| 6 | Terminal Module |  |  |
| 7 | DRIVE-CLiQ Hub Module |  |  |
| 8 | Controller Extension |  |  |
| 9 | Filter module |  |  |
| 10 | Hydraulic Module |  |  |
| 49 | DRIVE-CLiQ component |  |  |
| 50 | Option slot |  |  |
| 60 | Encoder |  |  |
| 70 | DRIVE-CLiQ motor |  |  |
| 71 | Hydraulic cylinder |  |  |
| 72 | Hydraulic valve |  |  |
| 80 | Motor |  |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |
| %3, %4 | 0 | Port 0 |  |
| 1 | Port 1 |  |  |
| 2 | Port 2 |  |  |
| 3 | Port 3 |  |  |
| 4 | Port 4 |  |  |
| 5 | Port 5 |  |  |
| 6 | Port 6 |  |  |
| 7 | Port 7 |  |  |
| 8 | Port 8 |  |  |
| 9 | Port 9 |  |  |
| 10 | X100 |  |  |
| 11 | X101 |  |  |
| 12 | X102 |  |  |
| 13 | X103 |  |  |
| 14 | X104 |  |  |
| 15 | X105 |  |  |
| 20 | X200 |  |  |
| 21 | X201 |  |  |
| 22 | X202 |  |  |
| 23 | X203 |  |  |
| 24 | X204 |  |  |
| 25 | X205 |  |  |
| 40 | X400 |  |  |
| 41 | X401 |  |  |
| 42 | X402 |  |  |
| 50 | X500 |  |  |
| 51 | X501 |  |  |
| 52 | X502 |  |  |
| 53 | X503 |  |  |
| 54 | X504 |  |  |
| 55 | X505 |  |  |
| 56 | X506 |  |  |
| 57 | X507 |  |  |

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
When writing the target topology, a duplicate connection between two components was
detected.  
Fault value (r0949, interpret hexadecimal):  
ddccbbaa hex:  
dd = connection number 2 of the duplicate connection  
cc = connection number 1 of the duplicate connection  
bb = component class  
aa = component number of one of the components connected twice  
Note:  
Connection number is described in F01375.

**Remedy:**
  
Read out the fault value and remove one of the two specified connections.  
Then download the target topology again using the commissioning tool.  
Note:  
Under "Topology --&gt; Topology view" the commissioning tool where relevant offers improved
diagnostics capability (e.g. setpoint/actual value comparison).

### A01481 (N) Topology: power unit not connected

**Drive object:**
  
BMM2C, CU_MV_DP, CU_MV_PN, ENC, HUB, TB30, TECBASE, TM150, TM15DI_DO, TM31

**Valid as of version:**
  
4.7

**Message value:**
  
Component: %1, to %2, %3, connection: %4

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |
| %2 | 0 | Component unknown |  |
| 1 | Control Unit |  |  |
| 2 | Motor Module |  |  |
| 3 | Line Module |  |  |
| 4 | Sensor Module |  |  |
| 5 | Voltage Sensing Module |  |  |
| 6 | Terminal Module |  |  |
| 7 | DRIVE-CLiQ Hub Module |  |  |
| 8 | Controller Extension |  |  |
| 9 | Filter module |  |  |
| 10 | Hydraulic Module |  |  |
| 49 | DRIVE-CLiQ component |  |  |
| 50 | Option slot |  |  |
| 60 | Encoder |  |  |
| 70 | DRIVE-CLiQ motor |  |  |
| 71 | Hydraulic cylinder |  |  |
| 72 | Hydraulic valve |  |  |
| 80 | Motor |  |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |
| %4 | 0 | Port 0 |  |
| 1 | Port 1 |  |  |
| 2 | Port 2 |  |  |
| 3 | Port 3 |  |  |
| 4 | Port 4 |  |  |
| 5 | Port 5 |  |  |
| 6 | Port 6 |  |  |
| 7 | Port 7 |  |  |
| 8 | Port 8 |  |  |
| 9 | Port 9 |  |  |
| 10 | X100 |  |  |
| 11 | X101 |  |  |
| 12 | X102 |  |  |
| 13 | X103 |  |  |
| 14 | X104 |  |  |
| 15 | X105 |  |  |
| 20 | X200 |  |  |
| 21 | X201 |  |  |
| 22 | X202 |  |  |
| 23 | X203 |  |  |
| 24 | X204 |  |  |
| 25 | X205 |  |  |
| 40 | X400 |  |  |
| 41 | X401 |  |  |
| 42 | X402 |  |  |
| 50 | X500 |  |  |
| 51 | X501 |  |  |
| 52 | X502 |  |  |
| 53 | X503 |  |  |
| 54 | X504 |  |  |
| 55 | X505 |  |  |
| 56 | X506 |  |  |
| 57 | X507 |  |  |

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The topology comparison has detected a power unit that is missing in the actual topology
with respect to the target topology.  
Alarm value (r2124, interpret hexadecimal):  
ddccbbaa hex:  
dd = connection number (%4)  
cc = component number (%3)  
bb = component class (% 2)  
aa = component number of the component that has not been inserted (% 1)  
Note:  
The component is described in dd, cc and bb, where the component has not been inserted.  
Component class and connection number are described in F01375.

**Remedy:**
  
Adapting topologies:  
- Insert the components involved at the right connection (correct the actual topology).  
- Adapt the project/parameterizing in the commissioning tool (correct the target topology).  
Check the hardware:  
- Check the 24 V supply voltage.  
- Check DRIVE-CLiQ cables for interruption and contact problems.  
- Check that the component is working properly.  
Note:  
Under "Topology --&gt; Topology view" the commissioning tool where relevant offers improved
diagnostics capability (e.g. setpoint/actual value comparison).

Reaction upon N:  
 NONE

Acknowl. upon N:  
NONE

### A01482 Topology: Sensor Module not connected

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Component: %1, to %2, %3, connection: %4

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |
| %2 | 0 | Component unknown |  |
| 1 | Control Unit |  |  |
| 2 | Motor Module |  |  |
| 3 | Line Module |  |  |
| 4 | Sensor Module |  |  |
| 5 | Voltage Sensing Module |  |  |
| 6 | Terminal Module |  |  |
| 7 | DRIVE-CLiQ Hub Module |  |  |
| 8 | Controller Extension |  |  |
| 9 | Filter module |  |  |
| 10 | Hydraulic Module |  |  |
| 49 | DRIVE-CLiQ component |  |  |
| 50 | Option slot |  |  |
| 60 | Encoder |  |  |
| 70 | DRIVE-CLiQ motor |  |  |
| 71 | Hydraulic cylinder |  |  |
| 72 | Hydraulic valve |  |  |
| 80 | Motor |  |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |
| %4 | 0 | Port 0 |  |
| 1 | Port 1 |  |  |
| 2 | Port 2 |  |  |
| 3 | Port 3 |  |  |
| 4 | Port 4 |  |  |
| 5 | Port 5 |  |  |
| 6 | Port 6 |  |  |
| 7 | Port 7 |  |  |
| 8 | Port 8 |  |  |
| 9 | Port 9 |  |  |
| 10 | X100 |  |  |
| 11 | X101 |  |  |
| 12 | X102 |  |  |
| 13 | X103 |  |  |
| 14 | X104 |  |  |
| 15 | X105 |  |  |
| 20 | X200 |  |  |
| 21 | X201 |  |  |
| 22 | X202 |  |  |
| 23 | X203 |  |  |
| 24 | X204 |  |  |
| 25 | X205 |  |  |
| 40 | X400 |  |  |
| 41 | X401 |  |  |
| 42 | X402 |  |  |
| 50 | X500 |  |  |
| 51 | X501 |  |  |
| 52 | X502 |  |  |
| 53 | X503 |  |  |
| 54 | X504 |  |  |
| 55 | X505 |  |  |
| 56 | X506 |  |  |
| 57 | X507 |  |  |

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The topology comparison has detected a Sensor Module that is missing in the actual
topology with respect to the target topology.  
Alarm value (r2124, interpret hexadecimal):  
ddccbbaa hex:  
dd = connection number (%4)  
cc = component number (%3)  
bb = component class (% 2)  
aa = component number of the component that has not been inserted (% 1)  
Note:  
The component is described in dd, cc and bb, where the component has not been inserted.  
Component class and connection number are described in F01375.

**Remedy:**
  
Adapting topologies:  
- Insert the components involved at the right connection (correct the actual topology).  
- Adapt the project/parameterizing in the commissioning tool (correct the target topology).  
Check the hardware:  
- Check the 24 V supply voltage.  
- Check DRIVE-CLiQ cables for interruption and contact problems.  
- Check that the component is working properly.  
Note:  
Under "Topology --&gt; Topology view" the commissioning tool where relevant offers improved
diagnostics capability (e.g. setpoint/actual value comparison).

### A01483 Topology: Terminal Module not connected

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Component: %1, to %2, %3, connection: %4

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |
| %2 | 0 | Component unknown |  |
| 1 | Control Unit |  |  |
| 2 | Motor Module |  |  |
| 3 | Line Module |  |  |
| 4 | Sensor Module |  |  |
| 5 | Voltage Sensing Module |  |  |
| 6 | Terminal Module |  |  |
| 7 | DRIVE-CLiQ Hub Module |  |  |
| 8 | Controller Extension |  |  |
| 9 | Filter module |  |  |
| 10 | Hydraulic Module |  |  |
| 49 | DRIVE-CLiQ component |  |  |
| 50 | Option slot |  |  |
| 60 | Encoder |  |  |
| 70 | DRIVE-CLiQ motor |  |  |
| 71 | Hydraulic cylinder |  |  |
| 72 | Hydraulic valve |  |  |
| 80 | Motor |  |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |
| %4 | 0 | Port 0 |  |
| 1 | Port 1 |  |  |
| 2 | Port 2 |  |  |
| 3 | Port 3 |  |  |
| 4 | Port 4 |  |  |
| 5 | Port 5 |  |  |
| 6 | Port 6 |  |  |
| 7 | Port 7 |  |  |
| 8 | Port 8 |  |  |
| 9 | Port 9 |  |  |
| 10 | X100 |  |  |
| 11 | X101 |  |  |
| 12 | X102 |  |  |
| 13 | X103 |  |  |
| 14 | X104 |  |  |
| 15 | X105 |  |  |
| 20 | X200 |  |  |
| 21 | X201 |  |  |
| 22 | X202 |  |  |
| 23 | X203 |  |  |
| 24 | X204 |  |  |
| 25 | X205 |  |  |
| 40 | X400 |  |  |
| 41 | X401 |  |  |
| 42 | X402 |  |  |
| 50 | X500 |  |  |
| 51 | X501 |  |  |
| 52 | X502 |  |  |
| 53 | X503 |  |  |
| 54 | X504 |  |  |
| 55 | X505 |  |  |
| 56 | X506 |  |  |
| 57 | X507 |  |  |

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The topology comparison has detected a Terminal Module that is missing in the actual
topology with respect to the target topology.  
Alarm value (r2124, interpret hexadecimal):  
ddccbbaa hex:  
dd = connection number (%4)  
cc = component number (%3)  
bb = component class (% 2)  
aa = component number of the component that has not been inserted (% 1)  
Note:  
The component is described in dd, cc and bb, where the component has not been inserted.  
Component class and connection number are described in F01375.

**Remedy:**
  
Adapting topologies:  
- Insert the components involved at the right connection (correct the actual topology).  
- Adapt the project/parameterizing in the commissioning tool (correct the target topology).  
Check the hardware:  
- Check the 24 V supply voltage.  
- Check DRIVE-CLiQ cables for interruption and contact problems.  
- Check that the component is working properly.  
Note:  
Under "Topology --&gt; Topology view" the commissioning tool where relevant offers improved
diagnostics capability (e.g. setpoint/actual value comparison).

### A01484 Topology: DRIVE-CLiQ Hub Module not connected

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Component: %1, to %2, %3, connection: %4

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |
| %2 | 0 | Component unknown |  |
| 1 | Control Unit |  |  |
| 2 | Motor Module |  |  |
| 3 | Line Module |  |  |
| 4 | Sensor Module |  |  |
| 5 | Voltage Sensing Module |  |  |
| 6 | Terminal Module |  |  |
| 7 | DRIVE-CLiQ Hub Module |  |  |
| 8 | Controller Extension |  |  |
| 9 | Filter module |  |  |
| 10 | Hydraulic Module |  |  |
| 49 | DRIVE-CLiQ component |  |  |
| 50 | Option slot |  |  |
| 60 | Encoder |  |  |
| 70 | DRIVE-CLiQ motor |  |  |
| 71 | Hydraulic cylinder |  |  |
| 72 | Hydraulic valve |  |  |
| 80 | Motor |  |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |
| %4 | 0 | Port 0 |  |
| 1 | Port 1 |  |  |
| 2 | Port 2 |  |  |
| 3 | Port 3 |  |  |
| 4 | Port 4 |  |  |
| 5 | Port 5 |  |  |
| 6 | Port 6 |  |  |
| 7 | Port 7 |  |  |
| 8 | Port 8 |  |  |
| 9 | Port 9 |  |  |
| 10 | X100 |  |  |
| 11 | X101 |  |  |
| 12 | X102 |  |  |
| 13 | X103 |  |  |
| 14 | X104 |  |  |
| 15 | X105 |  |  |
| 20 | X200 |  |  |
| 21 | X201 |  |  |
| 22 | X202 |  |  |
| 23 | X203 |  |  |
| 24 | X204 |  |  |
| 25 | X205 |  |  |
| 40 | X400 |  |  |
| 41 | X401 |  |  |
| 42 | X402 |  |  |
| 50 | X500 |  |  |
| 51 | X501 |  |  |
| 52 | X502 |  |  |
| 53 | X503 |  |  |
| 54 | X504 |  |  |
| 55 | X505 |  |  |
| 56 | X506 |  |  |
| 57 | X507 |  |  |

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The topology comparison has detected a DRIVE-CLiQ Hub Module missing in the actual
topology with respect to the target topology.  
Alarm value (r2124, interpret hexadecimal):  
ddccbbaa hex:  
dd = connection number (%4)  
cc = component number (%3)  
bb = component class (% 2)  
aa = component number of the component that has not been inserted (% 1)  
Note:  
The component is described in dd, cc and bb, where the component has not been inserted.  
Component class and connection number are described in F01375.

**Remedy:**
  
Adapting topologies:  
- Insert the components involved at the right connection (correct the actual topology).  
- Adapt the project/parameterizing in the commissioning tool (correct the target topology).  
Check the hardware:  
- Check the 24 V supply voltage.  
- Check DRIVE-CLiQ cables for interruption and contact problems.  
- Check that the component is working properly.  
Note:  
Under "Topology --&gt; Topology view" the commissioning tool where relevant offers improved
diagnostics capability (e.g. setpoint/actual value comparison).

### A01485 Topology: Controller Extension not connected

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Component: %1, to %2, %3, connection: %4

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |
| %2 | 0 | Component unknown |  |
| 1 | Control Unit |  |  |
| 2 | Motor Module |  |  |
| 3 | Line Module |  |  |
| 4 | Sensor Module |  |  |
| 5 | Voltage Sensing Module |  |  |
| 6 | Terminal Module |  |  |
| 7 | DRIVE-CLiQ Hub Module |  |  |
| 8 | Controller Extension |  |  |
| 9 | Filter module |  |  |
| 10 | Hydraulic Module |  |  |
| 49 | DRIVE-CLiQ component |  |  |
| 50 | Option slot |  |  |
| 60 | Encoder |  |  |
| 70 | DRIVE-CLiQ motor |  |  |
| 71 | Hydraulic cylinder |  |  |
| 72 | Hydraulic valve |  |  |
| 80 | Motor |  |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |
| %4 | 0 | Port 0 |  |
| 1 | Port 1 |  |  |
| 2 | Port 2 |  |  |
| 3 | Port 3 |  |  |
| 4 | Port 4 |  |  |
| 5 | Port 5 |  |  |
| 6 | Port 6 |  |  |
| 7 | Port 7 |  |  |
| 8 | Port 8 |  |  |
| 9 | Port 9 |  |  |
| 10 | X100 |  |  |
| 11 | X101 |  |  |
| 12 | X102 |  |  |
| 13 | X103 |  |  |
| 14 | X104 |  |  |
| 15 | X105 |  |  |
| 20 | X200 |  |  |
| 21 | X201 |  |  |
| 22 | X202 |  |  |
| 23 | X203 |  |  |
| 24 | X204 |  |  |
| 25 | X205 |  |  |
| 40 | X400 |  |  |
| 41 | X401 |  |  |
| 42 | X402 |  |  |
| 50 | X500 |  |  |
| 51 | X501 |  |  |
| 52 | X502 |  |  |
| 53 | X503 |  |  |
| 54 | X504 |  |  |
| 55 | X505 |  |  |
| 56 | X506 |  |  |
| 57 | X507 |  |  |

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The topology comparison has detected a Control Extension (CX32) missing in the actual
topology with respect to the target topology.  
Alarm value (r2124, interpret hexadecimal):  
ddccbbaa hex:  
dd = connection number (%4)  
cc = component number (%3)  
bb = component class (% 2)  
aa = component number of the component that has not been inserted (% 1)  
Note:  
The component is described in dd, cc and bb, where the component has not been inserted.  
Component class and connection number are described in F01375.

**Remedy:**
  
Adapting topologies:  
- Insert the components involved at the right connection (correct the actual topology).  
- Adapt the project/parameterizing in the commissioning tool (correct the target topology).  
Check the hardware:  
- Check the 24 V supply voltage.  
- Check DRIVE-CLiQ cables for interruption and contact problems.  
- Check that the component is working properly.  
Note:  
Under "Topology --&gt; Topology view" the commissioning tool where relevant offers improved
diagnostics capability (e.g. setpoint/actual value comparison).

### A01486 Topology: DRIVE-CLiQ component not connected

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Component: %1, to %2, %3, connection: %4

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |
| %2 | 0 | Component unknown |  |
| 1 | Control Unit |  |  |
| 2 | Motor Module |  |  |
| 3 | Line Module |  |  |
| 4 | Sensor Module |  |  |
| 5 | Voltage Sensing Module |  |  |
| 6 | Terminal Module |  |  |
| 7 | DRIVE-CLiQ Hub Module |  |  |
| 8 | Controller Extension |  |  |
| 9 | Filter module |  |  |
| 10 | Hydraulic Module |  |  |
| 49 | DRIVE-CLiQ component |  |  |
| 50 | Option slot |  |  |
| 60 | Encoder |  |  |
| 70 | DRIVE-CLiQ motor |  |  |
| 71 | Hydraulic cylinder |  |  |
| 72 | Hydraulic valve |  |  |
| 80 | Motor |  |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |
| %4 | 0 | Port 0 |  |
| 1 | Port 1 |  |  |
| 2 | Port 2 |  |  |
| 3 | Port 3 |  |  |
| 4 | Port 4 |  |  |
| 5 | Port 5 |  |  |
| 6 | Port 6 |  |  |
| 7 | Port 7 |  |  |
| 8 | Port 8 |  |  |
| 9 | Port 9 |  |  |
| 10 | X100 |  |  |
| 11 | X101 |  |  |
| 12 | X102 |  |  |
| 13 | X103 |  |  |
| 14 | X104 |  |  |
| 15 | X105 |  |  |
| 20 | X200 |  |  |
| 21 | X201 |  |  |
| 22 | X202 |  |  |
| 23 | X203 |  |  |
| 24 | X204 |  |  |
| 25 | X205 |  |  |
| 40 | X400 |  |  |
| 41 | X401 |  |  |
| 42 | X402 |  |  |
| 50 | X500 |  |  |
| 51 | X501 |  |  |
| 52 | X502 |  |  |
| 53 | X503 |  |  |
| 54 | X504 |  |  |
| 55 | X505 |  |  |
| 56 | X506 |  |  |
| 57 | X507 |  |  |

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The topology comparison has detected a DRIVE-CLiQ component missing in the actual
topology with respect to the target topology.  
Alarm value (r2124, interpret hexadecimal):  
ddccbbaa hex:  
dd = connection number (%4)  
cc = component number (%3)  
bb = component class (% 2)  
aa = component number of the component that has not been inserted (% 1)  
Note:  
The component is described in dd, cc and bb, where the component has not been inserted.  
Component class and connection number are described in F01375.

**Remedy:**
  
Adapting topologies:  
- Insert the components involved at the right connection (correct the actual topology).  
- Adapt the project/parameterizing in the commissioning tool (correct the target topology).  
Check the hardware:  
- Check the 24 V supply voltage.  
- Check DRIVE-CLiQ cables for interruption and contact problems.  
- Check that the component is working properly.  
Note:  
Under "Topology --&gt; Topology view" the commissioning tool where relevant offers improved
diagnostics capability (e.g. setpoint/actual value comparison).

### A01487 Topology: Option slot component not inserted

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Component: %1, to %2, %3, connection: %4

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |
| %2 | 0 | Component unknown |  |
| 1 | Control Unit |  |  |
| 2 | Motor Module |  |  |
| 3 | Line Module |  |  |
| 4 | Sensor Module |  |  |
| 5 | Voltage Sensing Module |  |  |
| 6 | Terminal Module |  |  |
| 7 | DRIVE-CLiQ Hub Module |  |  |
| 8 | Controller Extension |  |  |
| 9 | Filter module |  |  |
| 10 | Hydraulic Module |  |  |
| 49 | DRIVE-CLiQ component |  |  |
| 50 | Option slot |  |  |
| 60 | Encoder |  |  |
| 70 | DRIVE-CLiQ motor |  |  |
| 71 | Hydraulic cylinder |  |  |
| 72 | Hydraulic valve |  |  |
| 80 | Motor |  |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |
| %4 | 0 | Port 0 |  |
| 1 | Port 1 |  |  |
| 2 | Port 2 |  |  |
| 3 | Port 3 |  |  |
| 4 | Port 4 |  |  |
| 5 | Port 5 |  |  |
| 6 | Port 6 |  |  |
| 7 | Port 7 |  |  |
| 8 | Port 8 |  |  |
| 9 | Port 9 |  |  |
| 10 | X100 |  |  |
| 11 | X101 |  |  |
| 12 | X102 |  |  |
| 13 | X103 |  |  |
| 14 | X104 |  |  |
| 15 | X105 |  |  |
| 20 | X200 |  |  |
| 21 | X201 |  |  |
| 22 | X202 |  |  |
| 23 | X203 |  |  |
| 24 | X204 |  |  |
| 25 | X205 |  |  |
| 40 | X400 |  |  |
| 41 | X401 |  |  |
| 42 | X402 |  |  |
| 50 | X500 |  |  |
| 51 | X501 |  |  |
| 52 | X502 |  |  |
| 53 | X503 |  |  |
| 54 | X504 |  |  |
| 55 | X505 |  |  |
| 56 | X506 |  |  |
| 57 | X507 |  |  |

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The topology comparison has detected an option slot component missing in the actual
topology with respect to the target topology.  
Alarm value (r2124, interpret hexadecimal):  
ddccbbaa hex:  
dd = connection number (%4)  
cc = component number (%3)  
bb = component class (% 2)  
aa = component number of the component that has not been inserted (% 1)  
Note:  
The component is described in dd, cc and bb, where the component has not been inserted.  
Component class and connection number are described in F01375.

**Remedy:**
  
Adapting topologies:  
- Insert the components involved at the right connection (correct the actual topology).  
- Adapt the project/parameterizing in the commissioning tool (correct the target topology).  
Check the hardware:  
- Check the 24 V supply voltage.  
- Check DRIVE-CLiQ cables for interruption and contact problems.  
- Check that the component is working properly.  
Note:  
Under "Topology --&gt; Topology view" the commissioning tool where relevant offers improved
diagnostics capability (e.g. setpoint/actual value comparison).

### A01488 Topology: EnDat encoder not connected

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Component: %1, to %2, %3, connection: %4

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |
| %2 | 0 | Component unknown |  |
| 1 | Control Unit |  |  |
| 2 | Motor Module |  |  |
| 3 | Line Module |  |  |
| 4 | Sensor Module |  |  |
| 5 | Voltage Sensing Module |  |  |
| 6 | Terminal Module |  |  |
| 7 | DRIVE-CLiQ Hub Module |  |  |
| 8 | Controller Extension |  |  |
| 9 | Filter module |  |  |
| 10 | Hydraulic Module |  |  |
| 49 | DRIVE-CLiQ component |  |  |
| 50 | Option slot |  |  |
| 60 | Encoder |  |  |
| 70 | DRIVE-CLiQ motor |  |  |
| 71 | Hydraulic cylinder |  |  |
| 72 | Hydraulic valve |  |  |
| 80 | Motor |  |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |
| %4 | 0 | Port 0 |  |
| 1 | Port 1 |  |  |
| 2 | Port 2 |  |  |
| 3 | Port 3 |  |  |
| 4 | Port 4 |  |  |
| 5 | Port 5 |  |  |
| 6 | Port 6 |  |  |
| 7 | Port 7 |  |  |
| 8 | Port 8 |  |  |
| 9 | Port 9 |  |  |
| 10 | X100 |  |  |
| 11 | X101 |  |  |
| 12 | X102 |  |  |
| 13 | X103 |  |  |
| 14 | X104 |  |  |
| 15 | X105 |  |  |
| 20 | X200 |  |  |
| 21 | X201 |  |  |
| 22 | X202 |  |  |
| 23 | X203 |  |  |
| 24 | X204 |  |  |
| 25 | X205 |  |  |
| 40 | X400 |  |  |
| 41 | X401 |  |  |
| 42 | X402 |  |  |
| 50 | X500 |  |  |
| 51 | X501 |  |  |
| 52 | X502 |  |  |
| 53 | X503 |  |  |
| 54 | X504 |  |  |
| 55 | X505 |  |  |
| 56 | X506 |  |  |
| 57 | X507 |  |  |

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The topology comparison has detected an EnDat encoder missing in the actual topology
with respect to the target topology.  
Alarm value (r2124, interpret hexadecimal):  
ddccbbaa hex:  
dd = connection number (%4)  
cc = component number (%3)  
bb = component class (% 2)  
aa = component number of the component that has not been inserted (% 1)  
Note:  
The component is described in dd, cc and bb, where the component has not been inserted.  
Component class and connection number are described in F01375.

**Remedy:**
  
Adapting topologies:  
- Insert the components involved at the right connection (correct the actual topology).  
- Adapt the project/parameterizing in the commissioning tool (correct the target topology).  
Check the hardware:  
- Check the 24 V supply voltage.  
- Check DRIVE-CLiQ cables for interruption and contact problems.  
- Check that the component is working properly.  
Note:  
Under "Topology --&gt; Topology view" the commissioning tool where relevant offers improved
diagnostics capability (e.g. setpoint/actual value comparison).

### A01489 Topology: motor with DRIVE-CLiQ not connected

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Component: %1, to %2, %3, connection: %4

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |
| %2 | 0 | Component unknown |  |
| 1 | Control Unit |  |  |
| 2 | Motor Module |  |  |
| 3 | Line Module |  |  |
| 4 | Sensor Module |  |  |
| 5 | Voltage Sensing Module |  |  |
| 6 | Terminal Module |  |  |
| 7 | DRIVE-CLiQ Hub Module |  |  |
| 8 | Controller Extension |  |  |
| 9 | Filter module |  |  |
| 10 | Hydraulic Module |  |  |
| 49 | DRIVE-CLiQ component |  |  |
| 50 | Option slot |  |  |
| 60 | Encoder |  |  |
| 70 | DRIVE-CLiQ motor |  |  |
| 71 | Hydraulic cylinder |  |  |
| 72 | Hydraulic valve |  |  |
| 80 | Motor |  |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |
| %4 | 0 | Port 0 |  |
| 1 | Port 1 |  |  |
| 2 | Port 2 |  |  |
| 3 | Port 3 |  |  |
| 4 | Port 4 |  |  |
| 5 | Port 5 |  |  |
| 6 | Port 6 |  |  |
| 7 | Port 7 |  |  |
| 8 | Port 8 |  |  |
| 9 | Port 9 |  |  |
| 10 | X100 |  |  |
| 11 | X101 |  |  |
| 12 | X102 |  |  |
| 13 | X103 |  |  |
| 14 | X104 |  |  |
| 15 | X105 |  |  |
| 20 | X200 |  |  |
| 21 | X201 |  |  |
| 22 | X202 |  |  |
| 23 | X203 |  |  |
| 24 | X204 |  |  |
| 25 | X205 |  |  |
| 40 | X400 |  |  |
| 41 | X401 |  |  |
| 42 | X402 |  |  |
| 50 | X500 |  |  |
| 51 | X501 |  |  |
| 52 | X502 |  |  |
| 53 | X503 |  |  |
| 54 | X504 |  |  |
| 55 | X505 |  |  |
| 56 | X506 |  |  |
| 57 | X507 |  |  |

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The topology comparison has detected a motor with DRIVE-CLiQ missing in the actual
topology with respect to the target topology.  
Alarm value (r2124, interpret hexadecimal):  
ddccbbaa hex:  
dd = connection number (%4)  
cc = component number (%3)  
bb = component class (% 2)  
aa = component number of the component that has not been inserted (% 1)  
Note:  
The component is described in dd, cc and bb, where the component has not been inserted.  
Component class and connection number are described in F01375.

**Remedy:**
  
Adapting topologies:  
- Insert the components involved at the right connection (correct the actual topology).  
- Adapt the project/parameterizing in the commissioning tool (correct the target topology).  
Check the hardware:  
- Check the 24 V supply voltage.  
- Check DRIVE-CLiQ cables for interruption and contact problems.  
- Check that the component is working properly.  
Note:  
Under "Topology --&gt; Topology view" the commissioning tool where relevant offers improved
diagnostics capability (e.g. setpoint/actual value comparison).

### A01507 (F, N) BICO: Interconnections to inactive objects present

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** BICO |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
There are BICO interconnections to an inactive/inoperable drive object.  
The BI/CI parameters involved are listed in r9498.  
The associated BO/CO parameters are listed in r9499.  
The list of the BICO interconnections to other drive objects is displayed in r9491
and r9492 of the deactivated drive object.  
Note:  
r9498 and r9499 are only written to, if p9495 is not set to 0.  
Alarm value (r2124, interpret decimal):  
Number of BICO interconnections found to inactive drive objects.

**Remedy:**
  
- Set all open BICO interconnections centrally to the factory setting with p9495 =
2.  
- Make the non-operational drive object active/operational again (re-insert or activate
components).

Reaction upon F:  
Vector: OFF2 (NONE, OFF1, OFF3)  
Chopper: OFF2 (NONE)  
Infeed: OFF2 (NONE, OFF1)

Acknowl. upon F:  
IMMEDIATELY

Reaction upon N:  
 NONE

Acknowl. upon N:  
NONE

### A01508 BICO: Interconnections to inactive objects exceeded

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** BICO |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The maximum number of BICO interconnections (signal sinks) when deactivating a drive
object was exceeded.  
When deactivating a drive object, all BICO interconnections (signal sinks) are listed
in the following parameters:  
- r9498[0...29]: List of the BI/CI parameters involved.  
- r9499[0...29]: List of the associated BO/CO parameters.

**Remedy:**
  
Not necessary.  
This alarm is automatically withdrawn as soon as no BICO interconnection is entered
in r9498[29] and r9499[29] (value = 0).  
Notice:  
When re-activating the drive object, all BICO interconnections should be checked and
if required, re-established.

### F01510 BICO: Signal source is not float type

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Parameter: %1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** BICO |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The requested connector output does not have the correct data type. This interconnection
is not established.  
Fault value (r0949, interpret decimal):  
Parameter number to which an interconnection should be made (connector output).

**Remedy:**
  
Interconnect this connector input with a connector output having a float data type.

### F01511 (A) BICO: Interconnection with different scalings

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Parameter: %1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** BICO |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The requested BICO interconnection was established. However, a conversion is made
between the BICO output and BICO input using the reference values.  
- The BICO output has different normalized units than the BICO input.  
- Message only for interconnections within a drive object.  
Example:  
The BICO output has, as normalized unit, voltage and the BICO input has current.  
This means that the factor p2002/p2001 is calculated between the BICO output and the
BICO input.  
p2002: contains the reference value for current  
p2001: contains the reference value for voltage  
Fault value (r0949, interpret decimal):  
Parameter number of the BICO input (signal sink).

**Remedy:**
  
Not necessary.

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

### F01512 BICO: No scaling available

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** BICO |

  

**Reaction:**
  
Vector: OFF2  
Chopper: OFF2  
Infeed: OFF2 (OFF1)

**Acknowledge:**
  
POWER ON

**Cause:**
  
An attempt was made to determine a conversion factor for a scaling that does not exist.  
Fault value (r0949, interpret decimal):  
Unit (e.g. corresponding to SPEED) for which an attempt was made to determine a factor.

**Remedy:**
  
Apply scaling or check the transfer value.

### F01513 (N, A) BICO: Interconnection cross DO with different scalings

**Drive object:**
  
All objects

**Valid as of version:**
  
4.6

**Message value:**
  
Parameter: %1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** BICO |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The requested BICO interconnection was established. However, a conversion is made
between the BICO output and BICO input using the reference values.  
An interconnection is made between different drive objects and the BICO output has
different normalized units than the BICO input or the normalized units are the same
but the reference values are different.  
Example 1:  
BICO output with voltage normalized unit, BICO input with current normalized unit,
BICO output and BICO input lie in different drive objects. This means that the factor
p2002/p2001 is calculated between the BICO output and the BICO input.  
p2002: contains the reference value for current  
p2001: contains the reference value for voltage  
Example 2:  
BICO output with voltage normalized unit in drive object 1 (DO1), BICO input with
voltage normalized unit in drive object 2 (DO2). The reference values for voltage
(p2001) of the two drive objects have different values. This means that the factor
p2001(DO1)/p2001(DO2) is calculated between the BICO output and the BICO input.  
p2001: contains the reference value for voltage, drive objects 1, 2  
Fault value (r0949, interpret decimal):  
Parameter number of the BICO input (signal sink).

**Remedy:**
  
Not necessary.

Reaction upon N:  
 NONE

Acknowl. upon N:  
NONE

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

### A01514 (F) BICO: Error when writing during a reconnect

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Parameter: %1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** BICO |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
During a reconnect operation (e.g. while booting or downloading - but can also occur
in normal operation) a parameter was not able to be written to.  
Example:  
When writing to BICO input with double word format (DWORD), in the second index, the
memory areas overlap (e.g. p8861). The parameter is then reset to the factory setting.  
Alarm value (r2124, interpret decimal):  
Parameter number of the BICO input (signal sink).

**Remedy:**
  
Not necessary.

Reaction upon F:  
 NONE

Acknowl. upon F:  
IMMEDIATELY

### F01515 (A) BICO: Writing to parameter not permitted as the master control is active

**Drive object:**
  
All objects

**Valid as of version:**
  
4.8

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
When changing the number of CDS or when copying from CDS, the master control is active.

**Remedy:**
  
If required, return the master control and repeat the operation.

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

### A01590 (F) Drive: Motor maintenance interval expired

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Fault cause: %1 bin

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** Motor | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The selected service/maintenance interval for this motor was reached.  
Alarm value (r2124, interpret decimal):  
Motor data set number.  
See also: p0650 (Actual motor operating hours), p0651 (Motor operating hours maintenance interval)

**Remedy:**
  
carry out service/maintenance and reset the service/maintenance interval (p0651).

Reaction upon F:  
 NONE

Acknowl. upon F:  
IMMEDIATELY

### F01800 (A) DRIVE-CLiQ: Hardware/configuration error

**Drive object:**
  
All objects

**Valid as of version:**
  
5.1

**Message value:**
  
%1

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
Vector: NONE (OFF1, OFF2, OFF3)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF1, OFF2)

**Acknowledge:**
  
IMMEDIATELY (POWER ON)

**Cause:**
  
A DRIVE-CLiQ connection fault has occurred.  
Fault value (r0949, interpret decimal):  
100 ... 107:  
Communication via DRIVE-CLiQ socket X100 ... X107 has not been switched to cyclic
operation. The cause may be an incorrect structure or a configuration that results
in an impossible bus timing.  
10:  
Loss of the DRIVE-CLiQ connection. The cause may be, for example, that the DRIVE-CLiQ
cable was withdrawn from the Control Unit or as a result of a short-circuit for motors
with DRIVE-CLiQ. This fault can only be acknowledged in cyclic communication.  
11:  
Repeated faults when detecting the connection. This fault can only be acknowledged
in cyclic communication.  
12:  
A connection was detected but the node ID exchange mechanism does not function. The
reason is probably that the component is defective. This fault can only be acknowledged
in cyclic communication.

**Remedy:**
  
For fault value = 100 ... 107:  
- Ensure that the DRIVE-CLiQ components have the same firmware versions.  
- Avoid longer topologies for short current controller sampling times.  
For fault value = 10:  
- Check the DRIVE-CLiQ cables at the Control Unit.  
- Remove any short-circuit for motors with DRIVE-CLiQ.  
- Carry out a POWER ON.  
For fault value = 11:  
- Check the electrical cabinet design and cable routing for EMC compliance.  
For fault value = 12:  
- Replace the component involved.

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

### A01839 DRIVE-CLiQ diagnostics: cable fault to the component

**Drive object:**
  
All objects

**Valid as of version:**
  
4.6

**Message value:**
  
Component number: %1

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The fault counter (r9936[0...199]) to monitor the DRIVE-CLiQ connections/cables has
been incremented.  
Alarm value (r2124, interpret decimal):  
Component number.  
Note:  
The component number specifies the component whose feeder cable from the direction
of the Control Unit is faulted.  
The alarm is automatically withdrawn after 5 seconds, assuming that no other data
transfer error has occurred.  
See also: r9936 (DRIVE-CLiQ diagnostic error counter connection)

**Remedy:**
  
- Check the corresponding DRIVE-CLiQ cables.  
- Check the electrical cabinet design and cable routing for EMC compliance.

### A01840 SMI: Component found without motor data

**Drive object:**
  
All objects

**Valid as of version:**
  
4.4

**Message value:**
  
Component number: %1

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** DRIVE |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
An SMI/DQI without motor data has been found (e.g. SMI installed as replacement part).  
Alarm value (r2124, interpret decimal):  
Component number from target topology.

**Remedy:**
  
1. Download the SMI/DQI data (motor/encoder data) from the data backup again (p4690,
p4691).  
2. Carry out a POWER ON (switch-off/switch-on) for this component.  
Note:  
DQI: DRIVE-CLiQ Sensor Integrated  
SMI: SINAMICS Sensor Module Integrated  
See also: p4690 (SMI spare part component number), p4691 (SMI spare part save/download data)

### A01900 (F) PB/PN: Configuration telegram error

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
A controller attempts to establish a connection using an incorrect configuring telegram.  
Alarm value (r2124, interpret decimal):  
1:  
Connection established to more drive objects than configured in the device. The drive
objects for process data exchange and their sequence are defined in p0978.  
2:  
Too many PZD data words for output or input to a drive object. The number of possible
PZD items in a drive object is determined by the number of indices in r2050/p2051.  
3:  
Uneven number of bytes for input or output.  
4:  
Setting data for synchronization not accepted. For more information, see A01902.  
211:  
Unknown parameterizing block.  
223:  
Clock synchronization for the PZD interface set in p8815[0] is not permissible.  
More than one PZD interface is operated in clock synchronism.  
253:  
PN Shared Device: Illegal mixed configuration of PROFIsafe and PZD.  
254:  
PN Shared Device: Illegal double assignment of a slot/subslot.  
255:  
PN: Configured drive object and existing drive object do not match.  
256:  
PN: Configured telegram cannot be set.  
257:  
PN Shared Device: Too many PZD data words for the output or input in the overall device.  
500:  
Illegal PROFIsafe configuration for the interface set in p8815[1].  
More than one PZD interface is operated with PROFIsafe.  
501:  
PROFIsafe parameter error (e.g. F_dest).  
502:  
PROFIsafe telegram does not match.  
503:  
PROFIsafe connection is rejected as long as there is no isochronous connection (p8969).  
Additional values:  
Only for internal Siemens troubleshooting.

**Remedy:**
  
Check the bus configuration on the master and the slave sides.  
For alarm value = 1, 2:  
- Check the list of the drive objects with process data exchange (p0978).  
Note:  
With p0978[x] = 0, all of the following drive objects in the list are excluded from
the process data exchange.  
For alarm value = 2:  
- Check the number of data words for output and input to a drive object.  
For alarm value = 211:  
- Ensure offline version &lt;= online version.  
For alarm value = 223, 500:  
- Check the setting in p8839 and p8815.  
- Check for inserted but not configured CBE20.  
- Ensure that only one PZD interface is operated in clock synchronism or with PROFIsafe.  
For alarm value = 255:  
- Check configured drive objects.  
For alarm value = 256:  
- Check the configured telegram.  
For alarm value = 257:  
- Check the number of data words for output and input to the complete device.  
For alarm value = 501:  
- Check the set PROFIsafe address (p9610).  
For alarm value = 502:  
- Check the set PROFIsafe telegram (p60022, p9611).

Reaction upon F:  
Vector: NONE (OFF1)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF1)

Acknowl. upon F:  
IMMEDIATELY

### A01902 PB/PN: parameterization for isochronous operation not permissible

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
Parameterization for isochronous operation is not permissible.  
Alarm value (r2124, interpret decimal):  
0: Bus cycle time Tdp &lt; 0.5 ms.  
1: Bus cycle time Tdp &gt; 32 ms.  
2: Bus cycle time Tdp is not an integer multiple of the current controller sampling
time.  
3: Instant of the actual value sensing Ti &gt; Bus cycle time Tdp or Ti = 0.  
4: Instant of the actual value sensing Ti is not an integer multiple of the current
controller sampling time.  
5: Instant of the setpoint acceptance To &gt;= Bus cycle time Tdp or To = 0.  
6: Instant of the setpoint acceptance To is not an integer multiple of the current
controller sampling time.  
7: Master application cycle time Tmapc is not an integer multiple of the speed controller
sampling time.  
8: Bus reserve bus cycle time Tdp - Data exchange time Tdx less than two current controller
sampling times.  
10: Instant of the setpoint acceptance To &lt;= data exchange time Tdx + current controller
sampling time  
11: Master application cycle time Tmapc &gt; 14 x Tdp or Tmapc = 0.  
12: PLL tolerance window Tpll_w &gt; Tpll_w_max.  
13: Bus cycle time Tdp is not a multiple of all basic clock cycles p0110[x].  
16: For COMM BOARD, the instant in time for the actual value sensing Ti is less than
two current controller sampling times.

**Remedy:**
  
- Adapt the bus parameterization Tdp, Ti, To.  
- Adapt the sampling time for the current controller or speed controller.  
For alarm value = 10:  
- Reduce Tdx by using fewer bus participants or shorter telegrams.  
Note:  
PB: PROFIBUS  
PN: PROFINET

### A01906 (F) EtherNet/IP: configuration error

**Drive object:**
  
All objects

**Valid as of version:**
  
5.1

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
An EtherNet/IP controller attempts to establish a connection using an incorrect configuring
telegram.  
The telegram length set in the controller does not match the parameterization in the
drive device.

**Remedy:**
  
Check the set telegram length.  
Note:  
PZD interface 1:  
For p0922 not equal to 999, then the length of the selected telegram applies.  
For p0922 = 999, the maximum interconnected PZD (r2067) applies.  
PZD interface 2:  
The maximum interconnected PZD (r8867) applies.

Reaction upon F:  
Vector: NONE (OFF1)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF1)

Acknowl. upon F:  
IMMEDIATELY

### F01910 (N, A) Fieldbus: setpoint timeout

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, CU_MV_DP, CU_MV_PN, ENC, HUB, TB30, TECBASE, TM150,
TM15DI_DO, TM31, VECTOR3P, VECTORGL, VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
Vector: OFF3 (NONE, OFF1, OFF2)  
Chopper: NONE (OFF2)  
Infeed: OFF2 (NONE, OFF1)

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The reception of setpoints from the fieldbus interface (onboard, PROFIBUS/PROFINET/USS)
has been interrupted.  
- Bus connection interrupted.  
- Controller switched off.  
- Controller set into the STOP state.  
See also: p2040 (Fieldbus interface monitoring time), p2047 (PROFIBUS additional monitoring
time)

**Remedy:**
  
Restore the bus connection and set the controller to RUN.  
Note regarding PROFIBUS slave redundancy:  
For operation on a Y-Link, it must be ensured that "DP alarm mode = DPV1" is set in
the slave parameterization.

Reaction upon N:  
 NONE

Acknowl. upon N:  
NONE

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

### F01911 (N, A) PB/PN: isochronous operation clock cycle failure

**Drive object:**
  
All objects

**Valid as of version:**
  
4.4

**Message value:**
  
-

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
Vector: OFF1 (OFF3)  
Chopper: NONE (OFF2)  
Infeed: OFF1

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The global control telegram to synchronize the clock cycles has failed - In cyclic
operation - For several DP clock cycles or has violated the time grid specified in
the parameterizing telegram over several consecutive DP clock cycles (refer to the
bus cycle time, Tdp and Tpllw).

**Remedy:**
  
- Check the physical bus configuration (cable, connector, terminating resistor, shielding,
etc.).  
- Check whether communication was briefly or permanently interrupted.  
- Check the utilization level of the bus and controller (e.g. bus cycle time Tdp was
set too short).  
Note:  
PB: PROFIBUS  
PN: PROFINET

Reaction upon N:  
 NONE

Acknowl. upon N:  
NONE

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

### F01915 (N, A) PB/PN: isochronous operation sign-of-life failure drive object 1

**Drive object:**
  
All objects

**Valid as of version:**
  
4.4

**Message value:**
  
-

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
Group display for problems with the sign-of-life of the master (clock-cycle synchronous
operation) on the drive object 1 (Control Unit).  
For central measurements, synchronism with the central master is lost.

**Remedy:**
  
Note:  
PB: PROFIBUS  
PN: PROFINET

Reaction upon N:  
 NONE

Acknowl. upon N:  
NONE

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

### A01920 (F) PROFIBUS: Interruption cyclic connection

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The cyclic connection to the PROFIBUS master is interrupted.

**Remedy:**
  
Establish the PROFIBUS connection and activate the PROFIBUS master in the cyclic mode.  
Note:  
If there is no communication to a higher-level control system, then p2030 should be
set = 0 to suppress this message.  
See also: p2030 (Field bus interface protocol selection)

Reaction upon F:  
Vector: NONE (OFF1)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF1)

Acknowl. upon F:  
IMMEDIATELY

### A01921 (F) PROFIBUS: Receive setpoints after To

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
Output data of PROFIBUS master (setpoints) received at the incorrect instant in time
within the PROFIBUS clock cycle.

**Remedy:**
  
- Check bus configuration.  
- Check parameters for clock cycle synchronization (ensure To &gt; Tdx).  
Note:  
To: Time of setpoint acceptance  
Tdx: Data exchange time

Reaction upon F:  
Vector: NONE (OFF1)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF1)

Acknowl. upon F:  
IMMEDIATELY

### A01925 (F) Modbus TCP: connection interrupted

**Drive object:**
  
All objects

**Valid as of version:**
  
4.8

**Message value:**
  
-

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The Ethernet connection to the Modbus controller is interrupted.

**Remedy:**
  
- Establish an Ethernet connection.  
- Activate the Modbus controller.

Reaction upon F:  
Vector: NONE (OFF1)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF1)

Acknowl. upon F:  
IMMEDIATELY

### A01926 (F) EtherNet/IP: connection interrupted

**Drive object:**
  
All objects

**Valid as of version:**
  
5.1

**Message value:**
  
-

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The EtherNet connection to the EtherNet/IP controller is interrupted.

**Remedy:**
  
- Establish an EtherNet connection.  
- Activate the EtherNet/IP controller.

Reaction upon F:  
Vector: NONE (OFF1)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF1)

Acknowl. upon F:  
IMMEDIATELY

### A01930 PB/PN: current controller sampling time clock cycle synchronization not equal

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The current controller sampling time of all drives must be set the same for the clock
cycle synchronous operation.  
Alarm value (r2124, interpret decimal):  
Number of the drive object with different current controller sampling time.

**Remedy:**
  
Set current controller sampling time to identical values (p0115[0]).  
Note:  
PB: PROFIBUS  
PN: PROFINET  
See also: p0115

### A01931 PB/PN: speed controller sampling time clock cycle synchronization not equal

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The speed controller sampling time of all drives must be set the same for the clock
cycle synchronous operation.  
Alarm value (r2124, interpret decimal):  
Number of the drive object with the different speed controller sampling time.

**Remedy:**
  
Set the speed controller sampling times to identical values (p0115[1]).  
Note:  
PB: PROFIBUS  
PN: PROFINET  
See also: p0115

### A01940 PB/PN: isochronous operation not attained

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The bus is in the data exchange state and clock synchronous operation has been selected
using the parameterizing telegram. It was not possible to synchronize to the clock
cycle specified by the master.  
- The master does not send a clock synchronous global control telegram although clock
synchronous operation was selected when configuring the bus.  
- The master is using another clock synchronous DP clock cycle than was transferred
to the slave in the parameterizing telegram.  
- At least one drive object has a pulse enable (also not controlled from PROFIBUS/PROFINET).

**Remedy:**
  
- Check the master application and bus configuration.  
- Check the consistency between the clock cycle input when configuring the slave and
clock cycle setting at the master.  
- Check that no drive object has a pulse enable. Only enable the pulses after synchronizing
the PROFIBUS/PROFINET drives.  
Note:  
PB: PROFIBUS  
PN: PROFINET

### A01941 PB/PN: clock cycle signal missing when establishing bus communication

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The bus is in the data exchange state and clock synchronous operation has been selected
using the parameterizing telegram. The global control telegram for synchronization
is not being received.

**Remedy:**
  
Check the master application and bus configuration.  
Note:  
PB: PROFIBUS  
PN: PROFINET

### A01943 PB/PN: clock cycle signal error when establishing bus communication

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The bus is in the data exchange state and clock synchronous operation has been selected
using the parameterizing telegram.  
The global control telegram for synchronization is being irregularly received.  
- The master is sending an irregular global control telegram.  
- The master is using another clock synchronous DP clock cycle than was transferred
to the slave in the parameterizing telegram.

**Remedy:**
  
- Check the master application and bus configuration.  
- Check the consistency between the clock cycle input when configuring the slave and
clock cycle setting at the master.  
Note:  
PB: PROFIBUS  
PN: PROFINET

### A01945 PROFIBUS: Connection to the Publisher failed

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Fault cause: %1 bin

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
For PROFIBUS peer-to-peer data transfer, the connection to at least one Publisher
has failed.  
Alarm value (r2124, interpret binary):  
Bit 0 = 1: Publisher with address in r2077[0], connection failed.  
...  
Bit 15 = 1: Publisher with address in r2077[15], connection failed.

**Remedy:**
  
- Check the PROFIBUS cables.  
- Carry out a first commissioning of the Publisher that has the failed connection.  
See also: r2077 (PROFIBUS diagnostics peer-to-peer data transfer addresses)

### F01946 (A) PROFIBUS: Connection to the Publisher aborted

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Fault cause: %1 bin

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
Vector: OFF1 (NONE, OFF2, OFF3)  
Chopper: NONE (OFF2)  
Infeed: OFF1 (NONE, OFF2)

**Acknowledge:**
  
IMMEDIATELY (POWER ON)

**Cause:**
  
At this drive object, the connection to at least one Publisher for PROFIBUS peer-to-peer
data transfer in cyclic operation has been aborted.  
Fault value (r0949, interpret binary):  
Bit 0 = 1: Publisher with address in r2077[0], connection aborted.  
...  
Bit 15 = 1: Publisher with address in r2077[15], connection aborted.

**Remedy:**
  
- Check the PROFIBUS cables.  
- Check the state of the Publisher that has the interrupted connection.  
See also: r2077 (PROFIBUS diagnostics peer-to-peer data transfer addresses)

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

### F01950 (N, A) PB/PN: isochronous operation synchronization unsuccessful

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
Vector: OFF1 (NONE)  
Chopper: NONE (OFF2)  
Infeed: OFF1 (NONE)

**Acknowledge:**
  
IMMEDIATELY (POWER ON)

**Cause:**
  
Synchronization of the internal clock cycle to the global control telegram has failed.
The internal clock cycle exhibits an unexpected shift.

**Remedy:**
  
Only for internal Siemens troubleshooting.  
Note:  
PB: PROFIBUS  
PN: PROFINET

Reaction upon N:  
 NONE

Acknowl. upon N:  
NONE

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

### F01951 CU SYNC: Synchronization application clock cycle missing

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
Vector: OFF2 (NONE)  
Chopper: NONE (OFF2)  
Infeed: OFF2 (NONE)

**Acknowledge:**
  
IMMEDIATELY (POWER ON)

**Cause:**
  
If DRIVE-CLiQ components with different application clock cycle are operated on a
DRIVE-CLiQ port, this requires synchronization with the Control Unit. This synchronization
routine was unsuccessful.  
Fault value (r0949, interpret decimal):  
Only for internal Siemens troubleshooting.

**Remedy:**
  
- Carry out a POWER ON (switch-off/switch-on) for all components.  
- Upgrade the software of the DRIVE-CLiQ components.  
- Upgrade the Control Unit software.  
Note:  
If a Controller Extension is being used (e.g. CX32, NX10), then the following applies:  
Check whether the Controller Extension is issuing error messages, and if required,
remove these.

### F01952 CU DRIVE-CLiQ: Synchronization of component not supported

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** DRIVE |

  

**Reaction:**
  
Vector: OFF2 (NONE)  
Chopper: NONE (OFF2)  
Infeed: OFF2 (NONE)

**Acknowledge:**
  
IMMEDIATELY (POWER ON)

**Cause:**
  
The existing system configuration requires that the connected DRIVE-CLiQ components
support the synchronization between the basic clock cycle, DRIVE-CLiQ clock cycle
and the application clock cycle.  
However, not all DRIVE-CLiQ components have this functionality.  
Fault value (r0949, interpret decimal):  
Component number of the first faulty DRIVE-CLiQ component.

**Remedy:**
  
Upgrade the firmware of the component specified in the fault value.  
Note:  
If required, also upgrade additional components in the DRIVE-CLiQ line.

### A01953 CU SYNC: Synchronization not completed

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
After the drive system is switched on, the synchronization between the basic clock
cycle, DRIVE-CLiQ clock cycle and application clock cycle was started but was not
completed within the selected time tolerance.  
Alarm value (r2124, interpret decimal):  
Only for internal Siemens troubleshooting.

**Remedy:**
  
Carry out a POWER ON (switch-off/switch-on) for all components.  
If the error occurs after the drive sampling times were changed, and if a Terminal
Module 31 (TM31) is being used, the sampling times (p0115, p4099) should be set as
integer multiples to the drive clock cycles (p0115).

### F01954 CU DRIVE-CLiQ: Synchronization unsuccessful

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
Vector: OFF2  
Chopper: NONE (OFF2)  
Infeed: OFF2

**Acknowledge:**
  
IMMEDIATELY (POWER ON)

**Cause:**
  
Synchronization between the basic clock cycle, DRIVE-CLiQ clock cycle and application
clock cycle was started and was not able to be successfully completed (e.g. after
switch-on).  
Fault value (r0949, interpret decimal):  
Only for internal Siemens troubleshooting.

**Remedy:**
  
1. Remove the cause of a possible DRIVE-CLiQ fault.  
2. Initiate a new synchronization, e.g. as follows:  
- Remove the PROFIBUS master and re-insert again.  
- Restart the PROFIBUS master.  
- Switch off the Control Unit and switch on again.  
- Carry out a Control Unit hardware reset (RESET button, p0972).  
- Carry out a parameter reset and download the saved parameters (p0009 = 30, p0976
= 2, 3).

### A01955 CU DRIVE-CLiQ: Synchronization DO not completed

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
After the drive system is switched on, the synchronization between the basic clock
cycle, DRIVE-CLiQ clock cycle and application clock cycle was started but was not
completed within the selected time tolerance.  
Alarm value (r2124, interpret decimal):  
Only for internal Siemens troubleshooting.

**Remedy:**
  
Carry out a POWER ON (switch-off/switch-on) for all components of the DO.

### A01970 CBExx: cyclic connection interrupted

**Drive object:**
  
All objects

**Valid as of version:**
  
4.7

**Message value:**
  
%1

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The cyclic connection to the PROFINET controller is interrupted.  
See also: r8956 (CBExx cyclic connection state)

**Remedy:**
  
Establish the PROFINET connection and activate the PROFINET controller in the cyclic
mode.

### A01971 CBExx: maximum number of controllers exceeded

**Drive object:**
  
All objects

**Valid as of version:**
  
4.7

**Message value:**
  
Info. 1: %1, info. 2: %2

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
A controller attempts to establish a connection to the drive, and as a consequence
exceeds the permitted number of PROFINET connections.  
The alarm is automatically withdrawn after approx. 30 seconds.  
Alarm value (r2124, interpret hexadecimal):  
yyyyxxxx hex: yyyy = info. 1, xxxx = info. 2  
Info 1 = 0: number of RT connections exceeded  
Info 1 &gt; 0: number of IRT connections exceeded  
Info 2: permitted number of connections

**Remedy:**
  
Check the configuration of the PROFINET controllers.

### A01979 CBExx: internal error for cyclic data transfer

**Drive object:**
  
All objects

**Valid as of version:**
  
4.7

**Message value:**
  
%1

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The cyclic actual values and/or setpoints were not transferred within the specified
times.  
Alarm value (r2124, interpret hexadecimal):  
Only for internal Siemens troubleshooting.

**Remedy:**
  
Correctly set T_io_input or T_io_output.

### A01980 PN: cyclic connection interrupted

**Drive object:**
  
All objects

**Valid as of version:**
  
4.4

**Message value:**
  
%1

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The cyclic connection to the PROFINET controller is interrupted.  
See also: r8936 (Cyclic connection status)

**Remedy:**
  
Establish the PROFINET connection and activate the PROFINET controller in the cyclic
mode.

### A01981 PN: Maximum number of controllers exceeded

**Drive object:**
  
All objects

**Valid as of version:**
  
4.4

**Message value:**
  
Info. 1: %1, info. 2: %2

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
A controller attempts to establish a connection to the drive, and as a consequence
exceeds the permitted number of PROFINET connections.  
The alarm is automatically withdrawn after approx. 30 seconds.  
Alarm value (r2124, interpret hexadecimal):  
yyyyxxxx hex: yyyy = info. 1, xxxx = info. 2  
Info 1 = 0: number of RT connections exceeded  
Info 1 &gt; 0: number of IRT connections exceeded  
Info 2: permitted number of connections

**Remedy:**
  
Check the configuration of the PROFINET controllers.

### A01982 PN: second controller missing

**Drive object:**
  
All objects

**Valid as of version:**
  
4.4

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
Connections to two PROFINET controllers are expected. However, only the connection
to a PROFINET controller is available or the controller is in the STOP state.  
- System redundancy is activated.

**Remedy:**
  
Check the PROFINET controller.

### A01983 PN: system redundancy switchover running

**Drive object:**
  
All objects

**Valid as of version:**
  
4.8

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The "PROFINET system redundancy" function is configured and the connection between
the primary controller and drive device is interrupted. The backup controller assumes
control of the drive device.

**Remedy:**
  
Not necessary.  
This alarm is automatically withdrawn after switchover has been completed.

### A01989 PN: Internal cyclic data transfer error

**Drive object:**
  
All objects

**Valid as of version:**
  
4.4

**Message value:**
  
%1

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The cyclic actual values and/or setpoints were not transferred within the specified
times.  
Alarm value (r2124, interpret hexadecimal):  
Only for internal Siemens troubleshooting.

**Remedy:**
  
Correctly set T_io_input or T_io_output.

### A01990 (F) USS: PZD configuration error

**Drive object:**
  
All objects

**Valid as of version:**
  
4.4

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The configuration of the process data (PZD) for the USS protocol is incorrect.  
Alarm value (r2124, interpret decimal):  
2: PZD amount (p2022) too great for the first drive object (p978[0]).  
The number of possible PZD items in a drive object is determined by the number of
indices in r2050/p2051.

**Remedy:**
  
For alarm value = 2:  
Check the amount of USS PZD (p2022) and the maximum PZD amount (r2050/p2051) for the
first drive object (p0978[0]).

Reaction upon F:  
Vector: NONE (OFF1)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF1)

Acknowl. upon F:  
IMMEDIATELY

### A02000 Function generator: Start not possible

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** BICO |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The function generator has already been started.

**Remedy:**
  
Stop the function generator and restart again if necessary.  
Note:  
The alarm is reset as follows:  
- Remove the cause of this alarm.  
- Restart the function generator.  
See also: p4800 (Function generator control)

### A02005 Function generator: Drive does not exist

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** BICO |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The drive object specified for connection does not exist.

**Remedy:**
  
Use the existing drive object with the corresponding number.  
Note:  
The alarm is reset as follows:  
- Remove the cause of this alarm.  
- Restart the function generator.

### A02006 Function generator: No drive specified for connection

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** BICO |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
No drive specified for connection in p4815.

**Remedy:**
  
At least one drive to be connected must be specified in p4815.  
Note:  
The alarm is reset as follows:  
- Remove the cause of this alarm.  
- Restart the function generator.

### A02007 Function generator: Drive not SERVO / VECTOR / DC_CTRL

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** BICO |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The drive object specified for connection is not a SERVO / VECTOR or DC_CTRL.

**Remedy:**
  
Use a SERVO / VECTOR / DC_CTRL drive object with the corresponding number.  
Note:  
The alarm is reset as follows:  
- Remove the cause of this alarm.  
- Restart the function generator.

### A02008 Function generator: Drive specified a multiple number of times

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** BICO |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The drive object specified for connection is already specified.  
Alarm value (r2124, interpret decimal):  
Drive object number of the drive object that is specified a multiple number of times.

**Remedy:**
  
Specify a different drive object.  
Note:  
The alarm is reset as follows:  
- Remove the cause of this alarm.  
- Restart the function generator.

### A02009 Function generator: Illegal mode

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** BICO |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The set operating mode (p1300) of the drive object is not permissible when using the
function generator.  
Alarm value (r2124, interpret decimal):  
Number of the drive object involved.

**Remedy:**
  
Change the operating mode for this drive object to p1300 = 20 (encoderless speed control)
or p1300 = 21 (speed control with encoder).  
Note:  
The alarm is reset as follows:  
- Remove the cause of this alarm.  
- Restart the function generator.

### A02010 Function generator: Speed setpoint from the drive is not zero

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** BICO |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The speed setpoint of a drive selected for connection is greater than the value for
the standstill detection set using p1226.

**Remedy:**
  
For all of the drives specified for connection, set the speed setpoints to zero.  
Note:  
The alarm is reset as follows:  
- Remove the cause of this alarm.  
- Restart the function generator.

### A02011 Function generator: The actual drive speed is not zero

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** BICO |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The speed actual value of a drive selected for connection is greater than the value
for the standstill detection set using p1226.

**Remedy:**
  
Set the relevant drives to zero speed before starting the function generator.  
Note:  
The alarm is reset as follows:  
- Remove the cause of this alarm.  
- Restart the function generator.

### A02015 Function generator: Drive enable signals missing

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** BICO |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The master control and/or enable signals are missing to connect to the specified drive.

**Remedy:**
  
Fetch the master control to the specified drive object and set all enable signals.  
Note:  
The alarm is reset as follows:  
- Remove the cause of this alarm.  
- Restart the function generator.

### A02016 Function generator: Magnetizing running

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** BICO |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
Magnetizing has not yet been completed on a drive object specified for connection.  
Alarm value (r2124, interpret decimal):  
Number of the drive object involved.

**Remedy:**
  
Wait for magnetizing of the motor (r0056.4).  
Note:  
The alarm is reset as follows:  
- Restart the function generator.  
See also: r0056 (Status word, closed-loop control)

### A02020 Function generator: Parameter cannot be changed

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** BICO |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
This parameter setting cannot be changed when the function generator is active (p4800
= 1).  
See also: p4810, p4812, p4813, p4820, p4821, p4822, p4823, p4824, p4825, p4826, p4827, p4828,
p4829

**Remedy:**
  
- Stop the function generator before parameterizing (p4800 = 0).  
- If required, start the function generator (p4800 = 1).  
Note:  
The alarm is reset as follows:  
- Remove the cause of this alarm.  
- Restart the function generator.  
See also: p4800 (Function generator control)

### A02025 Function generator: Period too short

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** BICO |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The value for the period is too short.  
See also: p4821 (Function generator period)

**Remedy:**
  
Check and adapt the value for the period.  
Note:  
The alarm is reset as follows:  
- Remove the cause of this alarm.  
- Restart the function generator.  
See also: p4821 (Function generator period)

### A02026 Function generator: Pulse width too high

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** BICO |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The selected pulse width is too high.  
The pulse width must be less than the period duration.  
See also: p4822 (Function generator pulse width)

**Remedy:**
  
Reduce pulse width.  
Note:  
The alarm is reset as follows:  
- Remove the cause of this alarm.  
- Restart the function generator.  
See also: p4821 (Function generator period), p4822 (Function generator pulse width)

### A02030 Function generator: Physical address equals zero

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** BICO |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The specified physical address is zero.  
See also: p4812 (Function generator physical address)

**Remedy:**
  
Set a physical address with a value other than zero.  
Note:  
The alarm is reset as follows:  
- Remove the cause of this alarm.  
- Restart the function generator.  
See also: p4812 (Function generator physical address)

### A02040 Function generator: Illegal value for offset

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** BICO |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The value for the offset is higher than the value for the upper limit or lower than
the value for the lower limit.  
See also: p4826 (Function generator offset)

**Remedy:**
  
Adjust the offset value accordingly.  
Note:  
The alarm is reset as follows:  
- Remove the cause of this alarm.  
- Restart the function generator.  
See also: p4826 (Function generator offset), p4828 (Function generator lower limit), p4829 (Function
generator upper limit)

### A02041 Function generator: Illegal value for bandwidth

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** BICO |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The bandwidth referred to the time slice clock cycle of the function generator has
either been set too low or too high.  
Depending on the time slice clock cycle, the bandwidth is defined as follows:  
Bandwidth_max = 1 / (2 x time slice clock cycle)  
Bandwidth_min = Bandwidth_max / 100000  
Example:  
Assumption: p4830 = 125 µs  
--&gt; Bandwidth_max = 1 / (2 x 125 µs) = 4000 Hz  
--&gt; Bandwidth_min = 4000 Hz / 100000 = 0.04 Hz  
Note:  
p4823: Function generator bandwidth  
p4830: Function generator time slice clock cycle  
See also: p4823 (Function generator bandwidth), p4830 (Function generator time slice cycle)

**Remedy:**
  
Check the value for the bandwidth and adapt accordingly.  
Note:  
The alarm is reset as follows:  
- Remove the cause of this alarm.  
- Restart the function generator.

### A02047 Function generator: Time slice clock cycle invalid

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** BICO |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The time slice clock cycle selected does not match any of the existing time slices.  
See also: p4830 (Function generator time slice cycle)

**Remedy:**
  
Enter an existing time slice clock cycle. The existing time slices can be read out
via p7901.  
Note:  
The alarm is reset as follows:  
- Remove the cause of this alarm.  
- Restart the function generator.  
See also: r7901 (Sampling times)

### A02050 Trace: Start not possible

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** BICO |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The trace has already been started.

**Remedy:**
  
Stop the trace and, if necessary, start again.

### A02051 Trace: recording not possible as a result of know-how protection

**Drive object:**
  
All objects

**Valid as of version:**
  
4.7

**Message value:**
  
initiating recorder: %1, parameter %2

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |
| %1 | 1 | Recorder 0 |  |
| 2 | Recorder 1 |  |  |
| 3 | Recorders 0 and 1 |  |  |

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** BICO |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
TRACE recording is not possible as at least one signal or trigger signal being used
is under know-how protection.  
Alarm value (r2124, interpret hexadecimal):  
bbbbaaaa hex:  
aaaa = 1: recorder 0  
aaaa = 2: recorder 1  
aaaa = 3: recorders 0 and 1  
bbbb = parameter number (hexadecimal), that was not able to be written to.

**Remedy:**
  
- Temporarily activate or deactivate know-how protection (p7766).  
- Include the signal in the OEM exception list (p7763, p7764).  
- Where relevant do not record the signal.  
See also: p7763 (KHP OEM exception list number of indices for p7764), p7764 (KHP OEM exception
list)

### A02055 Trace: Recording time too short

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** BICO |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The trace duration is too short.  
The minimum is twice the value of the trace clock cycle.

**Remedy:**
  
Check the selected recording time and, if necessary, adjust.

### A02056 Trace: Recording cycle too short

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** BICO |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The selected recording cycle is shorter than the selected basic clock cycle 0 (p0110[0]).

**Remedy:**
  
Increase the value for the trace cycle.

### A02057 Trace: Time slice clock cycle invalid

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** BICO |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The time slice clock cycle selected does not match any of the existing time slices.

**Remedy:**
  
Enter an existing time slice clock cycle. The existing time slices can be read out
via p7901.  
See also: r7901 (Sampling times)

### A02058 Trace: Time slice clock cycle for endless trace not valid

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** BICO |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The selected time slice clock cycle cannot be used for the endless trace

**Remedy:**
  
Enter the clock cycle of an existing time slice with a cycle time &gt;= 2 ms for up to
4 recording channels or &gt;= 4 ms from 5 recording channels per trace.  
The existing time slices can be read out via p7901.  
See also: r7901 (Sampling times)

### A02059 Trace: Time slice clock cycle for 2 x 8 recording channels not valid

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** BICO |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The selected time slice clock cycle cannot be used for more than 4 recording channels.

**Remedy:**
  
Enter the clock cycle of an existing time slice with a cycle time &gt;= 4 ms or reduce
the number of recording channels to 4 per trace.  
The existing time slices can be read out via p7901.  
See also: r7901 (Sampling times)

### A02060 Trace: Signal to be traced missing

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** BICO |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
- A signal to be traced was not specified.  
- The specified signals are not valid.

**Remedy:**
  
- Specify the signal to be traced.  
- Check whether the relevant signal can be traced.

### A02061 Trace: Invalid signal

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** BICO |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
- The specified signal does not exist.  
- The specified signal can no longer be traced (recorded).

**Remedy:**
  
- Specify the signal to be traced.  
- Check whether the relevant signal can be traced.

### A02062 Trace: Invalid trigger signal

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** BICO |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
- A trigger signal was not specified.  
- The specified signal does not exist.  
- The specified signal is not a fixed-point signal.  
- The specified signal cannot be used as a trigger signal for the trace.

**Remedy:**
  
Specify a valid trigger signal.

### A02063 Trace: Invalid data type

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** BICO |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The specified data type to select a signal using a physical address is invalid.

**Remedy:**
  
Use a valid data type.

### A02070 Trace: Parameter cannot be changed

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** BICO |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The trace parameter settings cannot be changed when the trace is active.

**Remedy:**
  
- Stop the trace before parameterization.  
- If required, start the trace.

### A02075 Trace: Pretrigger time too long

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** BICO |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The selected pretrigger time must be shorter than the trace time.

**Remedy:**
  
Check the pretrigger time setting and change if necessary.

### F02080 Trace: Parameterization deleted due to unit changeover

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The trace parameterization in the drive unit was deleted due to a unit changeover
or a change in the reference parameters.

**Remedy:**
  
Restart trace.

### A02095 MTrace 0: multiple trace cannot be activated

**Drive object:**
  
All objects

**Valid as of version:**
  
4.7

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The following functions or settings are not permissible in conjunction with a multiple
trace (trace recorder 0):  
- Measuring function  
- Long-time trace  
- Trigger condition "immediate recording start" (IMMEDIATE)  
- Trigger condition "start with function generator" (FG_START)

**Remedy:**
  
- If required, deactivate the multiple trace (p4840[0] = 0).  
- Deactivate function or setting that is not permissible

### A02096 MTrace 0: cannot be saved

**Drive object:**
  
All objects

**Valid as of version:**
  
4.7

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
It is not possible to save the measurement results of a multiple trace on the memory
card (trace recorder 0).  
A multiple trace is not started or is canceled.  
Alarm value (r2124, interpret decimal):  
1: Memory card cannot be accessed.  
- Card is not inserted or is blocked by a mounted USB drive.  
3: Data save operation to slow.  
- A second trace has been completed before the measurement results of the first trace
were able to be saved.  
- Writing the measurement result files to the card is blocked by the parameter save.  
4: Data save operation canceled.  
- For instance, the file required for the data save operation was not able to be found.

**Remedy:**
  
- Insert or remove the memory card.  
- Use a larger memory card.  
- Configure a longer trace time or use an endless trace.  
- Avoid saving parameters while a multiple trace is running.  
- Check whether other functions are presently accessing measurement result files.

### A02097 MTrace 1: multiple trace cannot be activated

**Drive object:**
  
All objects

**Valid as of version:**
  
4.6

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The following functions or settings are not permissible in conjunction with a multiple
trace (trace recorder 1):  
- Measuring function  
- Long-time trace  
- Trigger condition "immediate recording start" (IMMEDIATE)  
- Trigger condition "start with function generator" (FG_START)

**Remedy:**
  
- If required, deactivate the multiple trace (p4840[1] = 0).  
- Deactivate function or setting that is not permissible

### A02098 MTrace 1: cannot be saved

**Drive object:**
  
All objects

**Valid as of version:**
  
4.6

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
It is not possible to save the measurement results of a multiple trace on the memory
card (trace recorder 1).  
A multiple trace is not started or is canceled.  
Alarm value (r2124, interpret decimal):  
1: Memory card cannot be accessed.  
- Card is not inserted or is blocked by a mounted USB drive.  
3: Data save operation to slow.  
- A second trace has been completed before the measurement results of the first trace
were able to be saved.  
- Writing the measurement result files to the card is blocked by the parameter save.  
4: Data save operation canceled.  
- For instance, the file required for the data save operation was not able to be found.

**Remedy:**
  
- Insert or remove the memory card.  
- Use a larger memory card.  
- Configure a longer trace time or use an endless trace.  
- Avoid saving parameters while a multiple trace is running.  
- Check whether other functions are presently accessing measurement result files.

### A02099 Trace: Insufficient Control Unit memory

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** BICO |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The memory space still available on the Control Unit is no longer sufficient for the
trace function.

**Remedy:**
  
Reduce the memory required, e.g. as follows:  
- Reduce the trace time.  
- Increase the trace clock cycle.  
- Reduce the number of signals to be traced.

### A02100 Drive: Computing dead time current controller too short

**Drive object:**
  
All objects

**Valid as of version:**
  
4.8

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The value in p0118 produces a dead time of one clock cycle because it is prior to
the setpoint becoming available.  
Possible causes:  
- A parameter backup with a version higher than 4.3 was loaded to a version less than
or equal to 4.3.  
- The system properties after replacing a component no longer match the parameter
assignment.  
Alarm value (r2134, floating point):  
Minimum value for p0118 where dead time no longer occurs.

**Remedy:**
  
- Set p0118 to zero.  
- Set p0118 to a value greater than or equal to the alarm value (for p1810.11 = 1)  
- Set p0117 (from the device) to an automatic setting (p0117 = 1).  
- Check the firmware versions of the components involved.  
See also: p0117 (Current controller computing dead time mode), p0118 (Current controller computing
dead time)

### A02150 TEC: Technology Extension cannot be loaded

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The system was not able to load a Technology Extension.  
Alarm value (r2124, interpret hexadecimal):  
10 hex (16 dec):  
The interface version in the DCB user library is not compatible to the DCC standard
library that has been loaded.  
12 hex (18 dec):  
A technology package was not able to be downloaded to a Control Unit because the warm
restart necessary was not able to be performed.  
Only for internal Siemens troubleshooting.

**Remedy:**
  
- Carry out a warm restart (p0009 = 30, p0976 = 2, 3).  
- Carry out a POWER ON (switch-off/switch-on) for all components.  
- Upgrade firmware to later version.  
- Contact Technical Support.  
For alarm value = 10 hex (16 dec):  
Load a compatible DCB user library (compatible to the interface of the DCC standard
library).  
For alarm value = 12 hex (18 dec):  
Carry out a POWER ON (switch-off/switch-on) for all components.  
Note:  
DCB: Drive Control Block  
DCC: Drive Control Chart  
TEC: Technology Extension  
See also: r4950, r4955, p4956, r4957

### F02151 (A) TEC: internal software error

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
Vector: OFF2 (NONE, OFF1, OFF3)  
Chopper: OFF2 (NONE)  
Infeed: OFF2 (NONE, OFF1)

**Acknowledge:**
  
IMMEDIATELY (POWER ON)

**Cause:**
  
An internal software error has occurred within a Technology Extension.  
Fault value (r0949, interpret hexadecimal):  
Only for internal Siemens troubleshooting.

**Remedy:**
  
- Carry out a POWER ON (switch-off/switch-on) for all components.  
- Upgrade firmware to later version.  
- Contact Technical Support.  
- Replace the Control Unit.  
Note:  
TEC: Technology Extension  
See also: r4950, r4955, p4956, r4957

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

### F02152 (A) TEC: insufficient memory

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
Vector: OFF1  
Chopper: OFF2  
Infeed: OFF1

**Acknowledge:**
  
IMMEDIATELY (POWER ON)

**Cause:**
  
Too many functions have been configured on this Control Unit (e.g. too many drives,
function modules, data sets, Technology Extensions, blocks, etc).  
Fault value (r0949, interpret decimal):  
Only for internal Siemens troubleshooting.

**Remedy:**
  
- Change the configuration on this Control Unit (e.g. fewer drives, function modules,
data sets, Technology Extensions, blocks, etc).  
- Use an additional Control Unit.  
Note:  
TEC: Technology Extension

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

## SINAMICS Alarms TM31 (Terminal Module) 02153 - 35801

SINAMICS Alarms TM31 (Terminal Module) 02153 - 35801

### F02153 TEC: technology function does not exist

**Drive object:**
  
All objects

**Valid as of version:**
  
4.8

**Message value:**
  
-

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A technology function (e.g. Technology Extension, DCB library) does not exist on the
drive device.  
When configuring, a technology function is activated, which does not exist on the
drive device. This can occur when downloading a project or when powering up.

**Remedy:**
  
- Load the required technology function to the drive device.  
- If required, deactivate the technology function not required in the configuration.  
Note:  
DCB: Drive Control Block  
TEC: Technology Extension

### F03000 NVRAM fault on action

**Drive object:**
  
All objects

**Valid as of version:**
  
4.4

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A fault occurred during execution of action p7770 = 1 or 2 for the NVRAM data.  
Fault value (r0949, interpret hexadecimal):  
yyxx hex: yy = fault cause, xx = application ID  
yy = 1:  
The action p7770 = 1 is not supported by this version if Drive Control Chart (DCC)
is activated for the drive object concerned.  
yy = 2:  
The data length of the specified application is not the same in the NVRAM and the
backup.  
yy = 3:  
The data checksum in p7774 is not correct.  
yy = 4:  
No data available to load.  
See also: p7770 (NVRAM action)

**Remedy:**
  
- Perform the remedy according to the results of the troubleshooting.  
- If necessary, start the action again.

### F03001 NVRAM checksum incorrect

**Drive object:**
  
All objects

**Valid as of version:**
  
4.4

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A checksum error occurred when evaluating the non-volatile data (NVRAM) on the Control
Unit.  
The NVRAM data affected was deleted.

**Remedy:**
  
Carry out a POWER ON (switch-off/switch-on) for all components.

### F03500 (A) TM: Initialization

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** Terminal Module (TM) | **Propagation:** BICO |

  

**Reaction:**
  
Vector: OFF1 (OFF2)  
Chopper: OFF2  
Infeed: OFF1 (OFF2)

**Acknowledge:**
  
IMMEDIATELY (POWER ON)

**Cause:**
  
When initializing the Terminal Modules, the terminals of the Control Unit or the Terminal
Board 30, an internal software error has occurred.  
Fault value (r0949, interpret decimal):  
yxxx dex  
y = Only for internal Siemens troubleshooting  
xxx = component number (p0151)

**Remedy:**
  
- Switch off / switch on the power supply for the Control Unit.  
- Check the DRIVE-CLiQ connection.  
- If required, replace the Terminal Module.  
The Terminal Module should be directly connected to a DRIVE-CLiQ socket of the Control
Unit.  
If the fault occurs again, replace the Terminal Module.

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

### A03501 TM: Sampling time change

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** Terminal Module (TM) | **Propagation:** BICO |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The sampling times of the inputs/outputs were changed.  
This change only becomes valid after the next boot.

**Remedy:**
  
Carry out a POWER ON.

### F03505 (N, A) TM: Analog input wire breakage

**Drive object:**
  
TM150, TM15DI_DO, TM31

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
External measured value / signal state outside the permissible range (16)

| Symbol | Meaning |
| --- | --- |
| **Component:** Terminal Module (TM) | **Propagation:** BICO |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY (POWER ON)

**Cause:**
  
The wire-break monitoring for an analog input has responded.  
The input value of the analog input has exceeded the threshold value parameterized
in p4061[x].  
Index x = 0: Analog input 0 (X521.1/X521.2)  
Index x = 1: Analog input 1 (X521.3/X521.4)  
Fault value (r0949, interpret decimal):  
yxxx dec  
y = analog input (0 = analog input 0 (AI 0), 1 = analog input 1 (AI 1))  
xxx = component number (p0151)  
Note:  
For the following analog input type, the wire breakage monitoring is active:  
p4056[x] = 3 (unipolar current input monitored (+4 ... +20 mA)

**Remedy:**
  
- Check the wiring for interruptions.  
- Check the magnitude of the injected current - It is possible that the infed signal
is too low.  
- Check the load resistor (250 Ohm).  
Note:  
The input current measured by the Terminal Module can be read out from r4052[x].  
For p4056[x] = 3 (unipolar current input monitored (+4 ... +20 mA)) the following
applies:  
A current less than 4 mA is not displayed in r4052[x] - but instead r4052[x] = 4 mA
is output.

Reaction upon N:  
 NONE

Acknowl. upon N:  
NONE

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

### A03506 (F, N) 24 V power supply missing

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Supply voltage fault (undervoltage) (3)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** BICO |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The 24 V power supply for the digital outputs (X124) is missing.

**Remedy:**
  
Check the terminals for the power supply voltage (X124, L1+, M).

Reaction upon F:  
 NONE

Acknowl. upon F:  
IMMEDIATELY (POWER ON)

Reaction upon N:  
 NONE

Acknowl. upon N:  
NONE

### A03507 (F, N) Digital output not set

**Drive object:**
  
ENC, HUB, TB30, TECBASE, TM150, TM15DI_DO, TM31

**Valid as of version:**
  
4.4

**Message value:**
  
%1

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** BICO |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
Despite specification by the signal source the digital output has not been set.  
Possible causes:  
- Power supply missing.  
- The digital output is in current limiting (e.g. due to short-circuit).  
- The digital output is being used for Safety Extended Functions.  
- The control has authority to access the digital output by means of direct access
(see also r0729).  
Alarm value (r2124, interpret bitwise binary):  
Digital output involved (structured the same as r0747).

**Remedy:**
  
- Check the 24 V power supply (e.g. X130.6 for CU310-2, ground is X130.5).  
- Check the output terminals for short-circuits.  
- Reset the signal source of the digital output for use by Safety Extended Functions.  
- Carry out a POWER ON (switch-off/switch-on).

Reaction upon F:  
 NONE

Acknowl. upon F:  
IMMEDIATELY (POWER ON)

Reaction upon N:  
 NONE

Acknowl. upon N:  
NONE

### A03510 (F, N) TM: Calibration data not plausible

**Drive object:**
  
TM150, TM15DI_DO, TM31

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** Terminal Module (TM) | **Propagation:** BICO |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
During ramp-up, the Terminal Module 31 (TM31) calibration data is read in and checked
for plausibility.  
At least one calibration data point was determined to be invalid.  
Alarm value (r2124, interpret binary):  
Bit 1: 10 V value, analog input 0 invalid.  
Bit 3: 10 V value, analog input 1 invalid.  
Bit 4: Offset, analog output 0 invalid.  
Bit 5: 10 V value, analog output 0 invalid.  
Bit 6: Offset, analog output 1 invalid.  
Bit 7: 10 V value, analog input 1 invalid.

**Remedy:**
  
- Switch off / switch on the power supply for the Control Unit.  
- Check the DRIVE-CLiQ wiring.  
Note:  
If it reoccurs, then replace the module.  
In principle, operation could continue.  
The analog channel involved possibly does not achieve the specified accuracy.

Reaction upon F:  
 NONE

Acknowl. upon F:  
IMMEDIATELY (POWER ON)

Reaction upon N:  
 NONE

Acknowl. upon N:  
NONE

### A03550 TM: Speed setpoint filter natural frequency > Shannon frequency

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** BICO |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The natural filter frequency of the speed setpoint filter (p1417) is greater than
or equal to the Shannon frequency.  
The Shannon frequency is calculated according to the following formula:  
0.5 / p4099[3]

**Remedy:**
  
Reduce the natural frequency of the speed setpoint filter (PT2 low pass) (p1417).

### F03590 (N, A) TM: Module not ready

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** Terminal Module (TM) | **Propagation:** GLOBAL |

  

**Reaction:**
  
 OFF2 (NONE)

**Acknowledge:**
  
IMMEDIATELY (POWER ON)

**Cause:**
  
The Terminal Module involved does not send a ready signal and no valid cyclic data.  
Fault value (r0949, interpret decimal):  
Drive object number of the Terminal Module involved.

**Remedy:**
  
- Check the 24 V power supply.  
- Check the DRIVE-CLiQ wiring.  
- Check whether the sampling time of the drive object involved is not equal to zero
(p4099[0]).

Reaction upon N:  
 NONE

Acknowl. upon N:  
NONE

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

### F07080 Drive: Incorrect control parameter

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, ENC, HUB, TB30, TECBASE, TM150, TM15DI_DO, TM31,
VECTOR3P, VECTORDM, VECTORGL, VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
4.4

**Message value:**
  
Parameter: %1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY (POWER ON)

**Cause:**
  
The closed-loop control parameters have been parameterized incorrectly (e.g. p0356
= L_spread = 0).  
Fault value (r0949, interpret decimal):  
The fault value includes the parameter number involved.  
See also: p0310, p0311, p0341, p0344, p0350, p0354, p0356, p0357, p0358, p0360, p0400, p0404,
p0408, p0640, p1082, p1300

**Remedy:**
  
Modify the parameter indicated in the fault value (r0949) (e.g. p0640 = current limit
&gt; 0).  
See also: p0311, p0341, p0344, p0350, p0354, p0356, p0358, p0360, p0400, p0404, p0408, p0640,
p1082

### F07082 Macro: Execution not possible

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Fault cause: %1, supplementary information: %2, preliminary parameter number: %3

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The macro cannot be executed.  
Fault value (r0949, interpret hexadecimal):  
ccccbbaa hex:  
cccc = preliminary parameter number, bb = supplementary information, aa = fault cause  
Fault causes for the trigger parameter itself:  
19: Called file is not valid for the trigger parameter.  
20: Called file is not valid for parameter 15.  
21: Called file is not valid for parameter 700.  
22: Called file is not valid for parameter 1000.  
23: Called file is not valid for parameter 1500.  
24: Data type of a TAG is incorrect (e.g. Index, number or bit is not U16).  
Fault causes for the parameters to be set:  
25: Error level has an undefined value.  
26: Mode has an undefined value.  
27: A value was entered as string in the tag value that is not "DEFAULT".  
31: Entered drive object type unknown.  
32: A device was not able to be found for the determined drive object number.  
34: A trigger parameter was recursively called.  
35: It is not permissible to write to the parameter via macro.  
36: Check, writing to a parameter unsuccessful, parameter can only be read, not available,
incorrect data type, value range or assignment incorrect.  
37: Source parameter for a BICO interconnection was not able to be determined.  
38: An index was set for a non-indexed (or CDS-dependent) parameter.  
39: No index was set for an indexed parameter.  
41: A bit operation is only permissible for parameters with the parameter format DISPLAY_BIN.  
42: A value not equal to 0 or 1 was set for a BitOperation.  
43: Reading the parameter to be changed by the BitOperation was unsuccessful.  
51: Factory setting for DEVICE may only be executed on the DEVICE.  
61: The setting of a value was unsuccessful.

**Remedy:**
  
- Check the parameter involved.  
- Check the macro file and BICO interconnection.  
See also: p0015, p0700 (Macro Binector Input (BI)), p1000 (Macro Connector Inputs (CI) for speed
setpoints), p1500 (Macro Connector Inputs (CI) for torque setpoints)

### F07083 Macro: ACX file not found

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Parameter: %1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The ACX file (macro) to be executed was not able to be found in the appropriate directory.  
Fault value (r0949, interpret decimal):  
Parameter number with which the execution was started.  
See also: p0015, p0700 (Macro Binector Input (BI)), p1000 (Macro Connector Inputs (CI) for speed
setpoints), p1500 (Macro Connector Inputs (CI) for torque setpoints)

**Remedy:**
  
- Check whether the file is saved in the appropriate directory on the memory card.  
Example:  
If p0015 is set to 1501, then the selected ACX file must be located in the following
directory:  
... /PMACROS/DEVICE/P15/PM001501.ACX

### F07084 Macro: Condition for WaitUntil not fulfilled

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Parameter: %1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The WaitUntil condition set in the macro was not fulfilled in a certain number of
attempts.  
Fault value (r0949, interpret decimal):  
Parameter number for which the condition was set.

**Remedy:**
  
Check and correct the conditions for the WaitUntil loop.

### A07089 Changing over units: Function module activation is blocked because the units have been changed over

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
An attempt was made to activate a function module. This is not permissible if the
units have already been changed over.  
See also: p0100 (IEC/NEMA standards), p0349 (System of units motor equivalent circuit diagram
data), p0505 (Selecting the system of units)

**Remedy:**
  
Restore units that have been changed over to the factory setting.

### A07094 General parameter limit violation

**Drive object:**
  
All objects

**Valid as of version:**
  
4.8

**Message value:**
  
Parameter: %1

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
As a result of the violation of a parameter limit, the parameter value was automatically
corrected.  
Minimum limit violated --&gt; parameter is set to the minimum value.  
Maximum limit violated --&gt; parameter is set to the maximum value.  
Alarm value (r2124, interpret decimal):  
Parameter number, whose value had to be adapted.

**Remedy:**
  
Check the adapted parameter values and if required correct.

### F07110 Drive: Sampling times and basic clock cycle do not match

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Parameter: %1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The parameterized sampling times do not match the basic clock cycle.  
Fault value (r0949, interpret decimal):  
The fault value specifies the parameter involved.  
See also: r0110, r0111, p0115

**Remedy:**
  
Enter the current controller sampling times so that they are identical to the basic
clock cycle, e.g. by selecting p0112. Note which basic clock cycle is selected in
p0111.  
The sampling times in p0115 can only be changed manually in the sampling times pre-setting
"Expert" (p0112).  
See also: r0110, r0111, p0112, p0115

### A07350 (F) Drive: Measuring probe parameterized to a digital output

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The measuring probe is connected to a bi-directional digital input/output and the
terminal is set as output.  
Alarm value (r2124, interpret decimal):  
8: DI/DO 8 (X122.9/X132.1)  
9: DI/DO 9 (X122.10/X132.2)  
10: DI/DO 10 (X122.12/X132.3)  
11: DI/DO 11 (X122.13/X132.4)  
12: DI/DO 12 (X132.9)  
13: DI/DO 13 (X132.10)  
14: DI/DO 14 (X132.12)  
15: DI/DO 15 (X132.13)  
Regarding the terminal designation:  
The first designation is valid for CU320, the second for CU305.

**Remedy:**
  
- Set the terminal as input (p0728).  
- De-select the measuring probe (p0488, p0489, p0580).

Reaction upon F:  
Vector: OFF1  
Chopper: NONE (OFF2)  
Infeed: OFF1

Acknowl. upon F:  
IMMEDIATELY

### F07500 Drive: Power unit data set PDS not configured

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Drive data set: %1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
Only for controlled line supply infeed/regenerative feedback units:  
The power unit data set was not configured - this means that a data set number was
not entered into the drive data set.  
Fault value (r0949, interpret decimal):  
Drive data set number of p0185.

**Remedy:**
  
The index of the power unit data set associated with the drive data set should be
entered into p0185.

### F07501 Drive: Motor Data Set MDS not configured

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Drive data set: %1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
Only for power units:  
The motor data set was not configured - this means that a data set number was not
entered into the associated drive data set.  
Fault value (r0949, interpret decimal):  
The fault value includes the drive data set number of p0186.

**Remedy:**
  
The index of the motor data set associated with the drive data set should be entered
into p0186.  
See also: p0186 (Motor Data Sets (MDS) number)

### F07502 Drive: Encoder Data Set EDS not configured

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Drive data set: %1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
Only for power units:  
The encoder data set was not configured - this means that a data set number was not
entered into the associated drive data set.  
Fault value (r0949, interpret decimal):  
The fault value includes the drive data set number of p0187, p0188 and p0189.  
The fault value is increased by 100 * encoder number (e.g. for p0189: Fault value
3xx with xx = data set number).

**Remedy:**
  
The index of the encoder data set associated with the drive data set should be entered
into p0187 (1st encoder), p0188 (2nd encoder) and p0189 (3rd encoder).

### F07510 Drive: Identical encoder in the drive data set

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
Vector: OFF2  
Chopper: NONE  
Infeed: OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
More than one encoder with identical component number is assigned to a single drive
data set. In one drive data set, it is not permissible that identical encoders are
operated together.  
Fault value (r0949, interpret decimal):  
1000 * first identical encoder + 100 * second identical encoder + drive data set.  
Example:  
Fault value = 1203 means:  
In drive data set 3, the first (p0187[3]) and second encoder (p0188[3]) are identical.

**Remedy:**
  
Assign the drive data set to different encoders.  
See also: p0141, p0187, p0188, p0189

### F07511 Drive: Encoder used a multiple number of times

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
Each encoder may only be assigned to one drive and within a drive must - In each drive
data set - either always be encoder 1, always encoder 2 or always encoder 3. This
unique assignment has been violated.  
Fault value (r0949, interpret decimal):  
The two parameters in coded form, that refer to the same component number.  
First parameter:  
Index: First and second decimal place (99 for EDS, not assigned DDS)  
Parameter number: Third decimal place (1 for p0187, 2 for p0188, 3 for p0189, 4 for
EDS not assigned DDS)  
Drive number: Fourth and fifth decimal place  
Second parameter:  
Index: Sixth and seventh decimal place (99 for EDS, not assigned DDS)  
Parameter number: Eighth decimal place (1 for p0187, 2 for p0188, 3 for p0189, 4 for
EDS, not assigned DDS)  
Drive number: Ninth and tenth decimal place  
See also: p0141

**Remedy:**
  
Correct the double use of a component number using the two parameters coded in the
fault value.

### A07531 Drive: Command Data Set CDS not present

**Drive object:**
  
All objects

**Valid as of version:**
  
4.4

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The selected command data set is not available (p0836 &gt; p0170). The command data set
was not changed over.  
See also: p0810, p0811, r0836

**Remedy:**
  
- Select the existing command data set.  
- Set up additional command data sets.

### A07850 (F) External alarm 1

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
External measured value / signal state outside the permissible range (16)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The condition for "External alarm 1" is satisfied.  
Note:  
The "External alarm 1" is initiated by a 1/0 edge via binector input p2112.  
See also: p2112 (External alarm 1)

**Remedy:**
  
Eliminate the causes of this alarm.

Reaction upon F:  
Vector: NONE (OFF1, OFF2, OFF3)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF1, OFF2)

Acknowl. upon F:  
IMMEDIATELY (POWER ON)

### A07851 (F) External alarm 2

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
External measured value / signal state outside the permissible range (16)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The condition for "External alarm 2" is satisfied.  
Note:  
The "External alarm 2" is initiated by a 1/0 edge via binector input p2116.  
See also: p2116 (External alarm 2)

**Remedy:**
  
Eliminate the causes of this alarm.

Reaction upon F:  
Vector: NONE (OFF1, OFF2, OFF3)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF1, OFF2)

Acknowl. upon F:  
IMMEDIATELY (POWER ON)

### A07852 (F) External alarm 3

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
External measured value / signal state outside the permissible range (16)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The condition for "External alarm 3" is satisfied.  
Note:  
The "External alarm 3" is initiated by a 1/0 edge via binector input p2117.  
See also: p2117 (External alarm 3)

**Remedy:**
  
Eliminate the causes of this alarm.

Reaction upon F:  
Vector: NONE (OFF1, OFF2, OFF3)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF1, OFF2)

Acknowl. upon F:  
IMMEDIATELY (POWER ON)

### F07860 (A) External fault 1

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
External measured value / signal state outside the permissible range (16)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
Vector: OFF2 (NONE, OFF1, OFF3)  
Chopper: NONE (OFF2)  
Infeed: OFF2 (NONE, OFF1)

**Acknowledge:**
  
IMMEDIATELY (POWER ON)

**Cause:**
  
The condition for "External fault 1" is satisfied.  
Note:  
The "External fault 1" is initiated by a 1/0 edge via binector input p2106.  
See also: p2106 (External fault 1)

**Remedy:**
  
- Eliminate the causes of this fault.  
- Acknowledge fault.

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

### F07861 (A) External fault 2

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
External measured value / signal state outside the permissible range (16)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
Vector: OFF2 (NONE, OFF1, OFF3)  
Chopper: NONE (OFF2)  
Infeed: OFF2 (NONE, OFF1)

**Acknowledge:**
  
IMMEDIATELY (POWER ON)

**Cause:**
  
The condition for "External fault 2" is satisfied.  
Note:  
The "External fault 2" is initiated by a 1/0 edge via binector input p2107.  
See also: p2107 (External fault 2)

**Remedy:**
  
- Eliminate the causes of this fault.  
- Acknowledge fault.

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

### F07862 (A) External fault 3

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
External measured value / signal state outside the permissible range (16)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
Vector: OFF2 (NONE, OFF1, OFF3)  
Chopper: NONE (OFF2)  
Infeed: OFF2 (NONE, OFF1)

**Acknowledge:**
  
IMMEDIATELY (POWER ON)

**Cause:**
  
The condition for "External fault 3" is satisfied.  
Note:  
The "External fault 3" is initiated by a 1/0 edge via the following parameters.  
- AND logic operation, binector input p2108, p3111, p3112.  
- Switch-on delay p3110.  
See also: p2108, p3110, p3111, p3112

**Remedy:**
  
- Eliminate the causes of this fault.  
- Acknowledge fault.

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

### F08000 (N, A) TB: +/-15 V power supply faulted

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Supply voltage fault (undervoltage) (3)

| Symbol | Meaning |
| --- | --- |
| **Component:** Controller Extension (CX) | **Propagation:** LOCAL |

  

**Reaction:**
  
Vector: NONE (OFF1, OFF2, OFF3)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF1, OFF2)

**Acknowledge:**
  
IMMEDIATELY (POWER ON)

**Cause:**
  
Terminal Board 30 detects an incorrect internal power supply voltage.  
Fault value (r0949, interpret decimal):  
0: Error when testing the monitoring circuit.  
1: Fault in normal operation.

**Remedy:**
  
- Replace Terminal Board 30.  
- Replace Control Unit.

Reaction upon N:  
 NONE

Acknowl. upon N:  
NONE

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

### F08010 (N, A) TB: Analog-digital converter

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, CU_MV_DP, CU_MV_PN, ENC, HUB, TB30, TECBASE, TM150, TM15DI_DO,
TM31, VECTOR3P, VECTORDM, VECTORGL, VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** Controller Extension (CX) | **Propagation:** LOCAL |

  

**Reaction:**
  
Vector: OFF1 (NONE, OFF2, OFF3)  
Infeed: NONE (OFF1, OFF2)

**Acknowledge:**
  
IMMEDIATELY (POWER ON)

**Cause:**
  
The analog/digital converter on Terminal Board 30 has not supplied any converted data.

**Remedy:**
  
- Check the power supply.  
- Replace Terminal Board 30.

Reaction upon N:  
 NONE

Acknowl. upon N:  
NONE

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

### F08500 (A) COMM BOARD: Monitoring time configuration expired

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
Vector: OFF1 (OFF2, OFF3)  
Chopper: NONE (OFF2)  
Infeed: OFF1 (OFF2)

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The monitoring time for the configuration has expired.  
Fault value (r0949, interpret decimal):  
0: The transfer time of the send configuration data has been exceeded.  
1: The transfer time of the receive configuration data has been exceeded.

**Remedy:**
  
Check communications link.

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

### F08501 (N, A) PN/COMM BOARD: Setpoint timeout

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, CU_MV_DP, CU_MV_PN, ENC, HUB, TB30, TECBASE, TM150,
TM15DI_DO, TM31, VECTOR3P, VECTORGL, VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
Vector: OFF3 (NONE, OFF1, OFF2)  
Chopper: NONE (OFF2)  
Infeed: OFF1 (OFF2)

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The reception of setpoints from the COMM BOARD has been interrupted.  
- Bus connection interrupted.  
- Controller switched off.  
- Controller set into the STOP state.  
- COMM BOARD defective.

**Remedy:**
  
- Restore the bus connection and set the controller to RUN.  
- If the error is repeated, check the update time set in the bus configuration (HW
Config).  
See also: p8840 (COMM BOARD monitoring time)

Reaction upon N:  
 NONE

Acknowl. upon N:  
NONE

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

### F08502 (A) PN/COMM BOARD: Monitoring time sign-of-life expired

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
Vector: OFF1 (OFF2, OFF3)  
Chopper: NONE (OFF2)  
Infeed: OFF1 (OFF2)

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The monitoring time for the sign-of-life counter has expired.  
The connection to the COMM BOARD was interrupted.

**Remedy:**
  
- Check communications link.  
- Check COMM BOARD.

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

### A08503 (F) PN/COMM BOARD: Monitoring time non-cyclic channel expired

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The reply to an acyclic request has not been received within the monitoring time.

**Remedy:**
  
- Check the length and contents of the sent data.  
- Check communications link.

Reaction upon F:  
Vector: NONE (OFF1, OFF2, OFF3)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF1, OFF2)

Acknowl. upon F:  
IMMEDIATELY

### A08504 (F) PN/COMM BOARD: Internal cyclic data transfer error

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The cyclic actual and/or setpoint values were not transferred within the specified
times.  
Alarm value (r2124, interpret decimal):  
Only for internal Siemens troubleshooting.

**Remedy:**
  
Check the parameterizing telegram (Ti, To, Tdp, etc.).

Reaction upon F:  
Vector: NONE (OFF1, OFF2, OFF3)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF1, OFF2)

Acknowl. upon F:  
IMMEDIATELY

### F08510 (A) PN/COMM BOARD: Send configuration data invalid

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
Vector: OFF1 (OFF2, OFF3)  
Chopper: NONE (OFF2)  
Infeed: OFF1 (OFF2)

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
COMM BOARD did not accept the send-configuration data.  
Fault value (r0949, interpret decimal):  
Return value of the send-configuration data check.

**Remedy:**
  
Check the send configuration data.

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

### A08511 (F) PN/COMM BOARD: Receive configuration data invalid

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The drive unit did not accept the receive configuration data.  
Alarm value (r2124, interpret decimal):  
Return value of the receive configuration data check.  
1: Connection established to more drive objects than configured in the device. The
drive objects for process data exchange and their sequence are defined in p0978.  
2: Too many PZD data words for output or input to a drive object. The number of possible
PZD items in a drive object is determined by the number of indices in r2050/p2051
for PZD IF1, and in r8850/p8851 for PZD IF2.  
3: Uneven number of bytes for input or output.  
4: Setting data for synchronization not accepted. For more information, see A01902.  
5: Cyclic operation not active.  
17: CBE20 Shared Device: Configuration of the F-CPU has been changed.  
223: Illegal clock synchronization for the PZD interface set in p8815[0].  
257: PN Shared Device: Too many PZD data words for output or input in the overall
device.  
500: Illegal PROFIsafe configuration for the interface set in p8815[1].  
501: PROFIsafe parameter error (e.g. F_dest).  
503: PROFIsafe connection is rejected as long as there is no isochronous connection
(p8969).  
Additional values:  
Only for internal Siemens troubleshooting.

**Remedy:**
  
Check the receive configuration data.  
For alarm value = 1, 2:  
- Check the list of the drive objects with process data exchange (p0978). With p0978[x]
= 0, all of the following drive objects in the list are excluded from the process
data exchange.  
For alarm value = 2:  
- Check the number of data words for output and input to a drive object.  
For alarm value = 17:  
- CBE20 Shared Device: Unplug/plug A-CPU.  
For alarm value = 223, 500:  
- Check the setting in p8839 and p8815.  
- Ensure that only one PZD interface is operated in clock synchronism or with PROFIsafe.  
For alarm value = 257:  
- Check the number of data words for output and input to the complete device.  
For alarm value = 501:  
- Check the set PROFIsafe address (p9610).

Reaction upon F:  
Vector: NONE (OFF1, OFF2, OFF3)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF1, OFF2)

Acknowl. upon F:  
IMMEDIATELY

### A08520 (F) PN/COMM BOARD: Non-cyclic channel error

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The memory or the buffer status of the non-cyclic channel has an error.  
Alarm value (r2124, interpret decimal):  
0: Error in the buffer status.  
1: Error in the memory.

**Remedy:**
  
Check communications link.

Reaction upon F:  
Vector: NONE (OFF1, OFF2, OFF3)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF1, OFF2)

Acknowl. upon F:  
IMMEDIATELY

### A08526 (F) PN/COMM BOARD: No cyclic connection

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
There is no cyclic connection to the control.

**Remedy:**
  
Establish the cyclic connection and activate the control with cyclic operation.  
For PROFINET, check the parameters "Name of Station" and "IP of Station" (r61000,
r61001).  
If a CBE20 is inserted and PROFIBUS is to communicate via PZD Interface 1, then this
must be parameterized using the STARTER commissioning tool or directly using p8839.

Reaction upon F:  
Vector: NONE (OFF1)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF1)

Acknowl. upon F:  
IMMEDIATELY

### A08530 (F) PN/COMM BOARD: Message channel error

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The memory or the buffer status of the message channel has an error.  
Alarm value (r2124, interpret decimal):  
0: Error in the buffer status.  
1: Error in the memory.

**Remedy:**
  
Check communications link.

Reaction upon F:  
Vector: NONE (OFF1, OFF2, OFF3)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF1, OFF2)

Acknowl. upon F:  
IMMEDIATELY

### A08531 (F) CBE20 POWER ON required

**Drive object:**
  
All objects

**Valid as of version:**
  
4.8

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
At least one parameter of the CBE20 (e.g. a parameter associated with SINAMICS Link)
was changed as a result of a project download. A POWER ON is required to activate
the values.  
Note:  
CBE20: Communication Board Ethernet 20  
See also: p8811 (SINAMICS Link project selection), p8812 (SINAMICS Link clock cycle settings),
p8835 (CBE20 firmware selection), p8836 (SINAMICS link node address)

**Remedy:**
  
Back up the parameters and carry out a POWER ON (switch off/switch on).

Reaction upon F:  
Vector: NONE (OFF1, OFF2, OFF3)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF1, OFF2)

Acknowl. upon F:  
IMMEDIATELY

### A08550 PZD Interface Hardware assignment error

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The assignment of the hardware to the PZD interface has been incorrectly parameterized.  
Alarm value (r2124, interpret decimal):  
1: Only one of the two indices is not equal to 99 (automatic).  
2: Both PZD interfaces are assigned to the same hardware.  
3: Assigned COMM BOARD missing.  
4: CBC10 is assigned to interface 1.  
See also: p8839 (PZD interface hardware assignment)

**Remedy:**
  
Check the parameterization and if required, correct (p8839).

### A08555 Modbus TCP: commissioning error

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, ENC, HUB, TB30, TECBASE, TM150, TM15DI_DO, TM31,
VECTOR3P, VECTORDM, VECTORGL, VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
4.8

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
A setting for the "Modbus TCP" protocol is incorrect.  
Alarm value (r2124, interpret decimal):  
1: Modbus simultaneously activated on the onboard interface (p2030) and CBE20 (p8835).
CBE20 is not activated.  
2: A drive object supported by Modbus is not available under p0978[0]. Modbus is not
activated.  
3: Drive object SERVO is under p0978[0] - and FM bit LINMOT is set, Modbus is not
activated.  
See also: p0978 (List of drive objects), p2030 (Field bus interface protocol selection), p8835
(CBE20 firmware selection)

**Remedy:**
  
For alarm value = 1:  
Check the parameterization and if required, correct (p2030, p8835).  
For alarm value = 2:  
Appropriately resort the list of drive objects in p0978.

### A08560 IE: Syntax error in configuration file

**Drive object:**
  
All objects

**Valid as of version:**
  
4.4

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
A syntax error has been detected in the ASCII configuration file for the Industrial
Ethernet interface (X127). The saved configuration file has not been loaded.  
Note:  
IE: Industrial Ethernet

**Remedy:**
  
- Check the interface configuration (p8900 and following), correct if necessary, and
activate (p8905 = 1).  
- Save the parameters for interface configuration (e.g. p8905 = 2)  
or  
- Reinitialize the station using the "Edit Ethernet node" screen form (e.g. with STARTER
commissioning tool).  
See also: p8905 (Activate IE interface configuration)

### A08561 IE: Consistency error affecting adjustable parameters

**Drive object:**
  
All objects

**Valid as of version:**
  
4.4

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
A consistency error was detected when activating the configuration (p8905) for the
Industrial Ethernet interface (X127).  
Alarm value (r2124, interpret decimal):  
0: General consistency error  
1: Error in the IP configuration (IP address, subnet mask or standard gateway).  
2: Error in the station names.  
5: Standard gateway is also set at the PROFINET onboard interface.  
6: The station name is also set at the PROFINET onboard interface.  
7: IP address is located in the same subnet as the IP address of the PROFINET onboard
interface.  
Note:  
For alarm value = 0, 1, 2, 5, 7 the following applies: the configuration was not changed.  
For alarm value = 6 the following applies: The new configuration was however activated.  
IE: Industrial Ethernet  
See also: p8900 (IE Name of Station), p8901 (IE IP address), p8902 (IE Default Gateway), p8903
(IE Subnet Mask)

**Remedy:**
  
- Check the required interface configuration (p8900 and following), correct if necessary,
and activate (p8905).  
or  
- Reinitialize the station using the "Edit Ethernet node" screen form (e.g. with STARTER
commissioning tool).  
See also: p8905 (Activate IE interface configuration)

### A08562 PROFINET: Syntax error in configuration file

**Drive object:**
  
All objects

**Valid as of version:**
  
4.4

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
A syntax error has been detected in the ASCII configuration file for the onboard PROFINET
interface. The saved configuration file has not been loaded.

**Remedy:**
  
- Check the interface configuration (p8920 and following), correct if necessary, and
activate (p8925 = 1).  
- Save the parameters for interface configuration (e.g. p8925 = 2).  
or  
- Reinitialize the station using the "Edit Ethernet node" screen form (e.g. with STARTER
commissioning tool).  
See also: p8925 (Activate PN interface configuration)

### A08563 PROFINET: Consistency error affecting adjustable parameters

**Drive object:**
  
All objects

**Valid as of version:**
  
4.4

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
A consistency error was detected when activating the configuration (p8925) for the
PROFINET interface.  
Alarm value (r2124, interpret decimal):  
0: General consistency error  
1: Error in the IP configuration (IP address, subnet mask or standard gateway).  
2: Name of station error.  
3: DHCP was not able to be activated, as a cyclic PROFINET connection already exists.  
4: A cyclic PROFINET connection is not possible as DHCP is activated.  
5: Standard gateway is also set at the Industrial Ethernet interface (X127).  
6: Standard station name is also set at the Industrial Ethernet interface (X127).  
7: IP address is located in the same subnet as the IP address of the Industrial Ethernet
interface (X127).  
Note:  
For alarm value = 0, 1, 2, 3, 4, 5, 7, the following applies: the configuration was
not changed.  
For alarm value = 6 the following applies: The new configuration was however activated.  
DHCP: Dynamic Host Configuration Protocol  
See also: p8920 (PN Name of Station), p8921 (PN IP address), p8922 (PN Default Gateway), p8923
(PN Subnet Mask)

**Remedy:**
  
- Check the required interface configuration (p8940 and following), correct if necessary,
and activate (p8945).  
or  
- Reinitialize the station using the "Edit Ethernet node" screen form (e.g. with STARTER
commissioning tool).  
See also: p8925 (Activate PN interface configuration)

### A08564 PN/COMM BOARD: syntax error in the configuration file

**Drive object:**
  
All objects

**Valid as of version:**
  
4.4

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
A syntax error has been detected in the ASCII configuration file for the Communication
Board Ethernet 20/25/41 (CBE20/CBE25/CBE41). The saved configuration file has not
been loaded.

**Remedy:**
  
- Correct and activate the CBExx configuration (p8940 and following) (p8945 = 2).  
- Reinitialize the CBExx (e.g. using the STARTER commissioning tool)  
Note:  
The configuration is not applied until the next POWER ON!  
See also: p8945 (CBExx activate configuration of interfaces)

### A08565 PNCOMM BOARD: Consistency error affecting adjustable parameters

**Drive object:**
  
All objects

**Valid as of version:**
  
4.4

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
A consistency error was detected when activating the configuration (p8945) for the
Communication Board Ethernet 20/25/41 (CBE20/CBE25/CBE41).  
Alarm value (r2124, interpret decimal):  
0: General consistency error  
1: Error in the IP configuration (IP address, subnet mask or standard gateway).  
2: Error in the station names.  
3: DHCP was not able to be activated, as a cyclic PROFINET connection already exists.  
4: A cyclic PROFINET connection is not possible as DHCP is activated.  
Note:  
For all alarm values, the following applies: currently set configuration has not been
activated.  
DHCP: Dynamic Host Configuration Protocol  
See also: p8940 (CBExx name of station), p8941 (CBExx IP address), p8942 (CBExx default gateway),
p8943 (CBExx subnet mask), p8944 (CBExx DHCP mode)

**Remedy:**
  
- Check the required interface configuration (p8940 and following), correct if necessary,
and activate (p8945).  
or  
- Reinitialize the station using the "Edit Ethernet node" screen form (e.g. with STARTER
commissioning tool).  
See also: p8945 (CBExx activate configuration of interfaces)

### F08700 (A) CAN: Communications error

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, CU_MV_DP, CU_MV_PN, ENC, HUB, TB30, TECBASE, TM150,
TM15DI_DO, TM31, VECTOR3P, VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
Vector: OFF3 (NONE, OFF1, OFF2)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF1, OFF2)

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A CAN communications error has occurred.  
Fault value (r0949, interpret decimal):  
1: The error counter for the send telegrams has exceeded the BUS OFF value 255. The
bus disables the CAN controller.  
- Bus cable short circuit.  
- Incorrect baud rate.  
- Incorrect bit timing.  
2: The master no longer interrogated the CAN node status longer than for its "life
time". The "life time" is obtained from the "guard time" (p8604[0]) multiplied by
the "life time factor" (p8604[1]).  
- Bus cable interrupted.  
- Bus cable not connected.  
- Incorrect baud rate.  
- Incorrect bit timing.  
- Master fault.  
See also r8843.2 IF2 PZD status - fieldbus running.  
Note:  
The fault response can be set as required using p8641.  
See also: p8604 (CAN life guarding), p8641 (CAN Abort Connection Option Code), r8843 (IF2 PZD
state)

**Remedy:**
  
- Check the bus cable  
- Check the baud rate (p8622).  
- Check the bit timing (p8623).  
- Check the master.  
The CAN controller must be manually restarted with p8608 = 1 after the cause of the
fault has been resolved!  
See also: p8608 (CAN Clear Bus Off Error), p8622 (CAN bit rate), p8623 (CAN Bit Timing selection)

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

### F08701 CAN: NMT state change

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, CU_MV_DP, CU_MV_PN, ENC, HUB, TB30, TECBASE, TM150,
TM15DI_DO, TM31, VECTOR3P, VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
Vector: OFF3  
Chopper: NONE (OFF2)  
Infeed: OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A CANopen NMT state transition from "operational" to "pre-operational" or after "stopped".  
Fault value (r0949, interpret decimal):  
1: CANopen NMT state transition from "operational" to "pre-operational".  
2: CANopen NMT state transition from "operational" to "stopped".  
Note:  
In the NMT state "pre-operational", process data cannot be transferred and in the
NMT state "stopped", no process data and no service data can be transferred.

**Remedy:**
  
Not necessary.  
Acknowledge the fault and continue operation.

### F08702 (A) CAN: RPDO Timeout

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, CU_MV_DP, CU_MV_PN, ENC, HUB, TB30, TECBASE, TM150,
TM15DI_DO, TM31, VECTOR3P, VECTORGL, VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
4.4

**Message value:**
  
-

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
Vector: OFF3 (NONE, OFF1, OFF2)  
Chopper: NONE (OFF2)  
Infeed: OFF2 (NONE, OFF1)

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The monitoring time of the CANopen RPDO telegram has expired because the bus connection
was either interrupted or the CANopen Master was switched-off.  
See also r8843.0 IF2 PZD status - Setpoint failure or r8843.2 IF2 PZD status - fieldbus
running.  
See also: p8699 (CAN: RPDO monitoring time), r8843 (IF2 PZD state)

**Remedy:**
  
- Check the bus cable  
- Check the master.  
- If required, increase the monitoring time (p8699).

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

### F08703 (A) CAN: Maximum number of drive objects exceeded

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, CU_MV_DP, CU_MV_PN, ENC, HUB, TB30, TECBASE, TM150,
TM15DI_DO, TM31, VECTOR3P, VECTORGL, VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
4.4

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
Vector: OFF3 (NONE, OFF1, OFF2)  
Chopper: OFF2 (NONE)  
Infeed: OFF2 (NONE, OFF1)

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The maximum number of 8 drive objects with the "CAN" function module was exceeded.  
Note:  
In the CANopen standard, a maximum of 8 CANopen device modules (drive objects with
function module "CAN") are defined for each CANopen slave.

**Remedy:**
  
- New commissioning of maximum 8 drive objects with the "CAN" function module in the
topology.  
- For the drive objects, if required, deselect the "CAN" function module (r0108.29).

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

### A08751 (N) CAN: Telegram loss

**Drive object:**
  
All objects

**Valid as of version:**
  
4.6

**Message value:**
  
%1

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The CAN controller has lost a receive message.  
Alarm value (r2124, interpret decimal):  
Hardware channel in the CAN controller.  
0: Firmware version &lt; 5.2 (no reference to the original hardware channel).  
1: NMT command message  
2: SYNC message  
3: NMT error control message  
7 ... 31: RPDO message  
32: SDO message

**Remedy:**
  
- Increase the cycle times of the received messages.  
- CANopen reduce sampling time (p8848).  
See also: p8848 (IF2 PZD sampling time)

Reaction upon N:  
 NONE

Acknowl. upon N:  
NONE

### A08752 CAN: Error counter for error passive exceeded

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The error counter for the send or receive telegrams has exceeded the value 127.

**Remedy:**
  
- Check the bus cable  
- Set a higher baud rate (p8622).  
- Check the bit timing and if required optimize (p8623).  
See also: p8622 (CAN bit rate), p8623 (CAN Bit Timing selection)

### A08753 CAN: Message buffer overflow

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
A message buffer overflow.  
Alarm value (r2124, interpret decimal):  
1: Non-cyclic send buffer (SDO response buffer) overflow.  
2: Non-cyclic receive buffer (SDO receive buffer) overflow.  
3: Cyclic send buffer (PDO send buffer) overflow.

**Remedy:**
  
- Check the bus cable.  
- Set a higher baud rate (p8622).  
- Check the bit timing and if required optimize (p8623).  
For alarm value = 2:  
- Reduce the cycle times of the SDO receive messages.  
- SDO request from master only after SDO feedback for previous SDO request.  
See also: p8622 (CAN bit rate), p8623 (CAN Bit Timing selection)

### A08754 CAN: Incorrect communications mode

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
In the "operational" mode, an attempt was made to change parameters p8700 ... p8737.

**Remedy:**
  
Change to the "pre-operational" or "stopped" mode.

### A08755 CAN: Obj cannot be mapped

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The CANopen object is not provided for the Process Data Object (PDO) Mapping.

**Remedy:**
  
Use a CANopen object intended for the PDO mapping or enter 0.  
The following objects can be mapped in the Receive Process Data Object (RPDO) or Transmit
Process Data Object (TPDO):  
- RPDO: 6040 hex, 6060 hex, 60FF hex, 6071 hex; 5800 hex - 580F hex; 5820 hex - 5827
hex  
- TPDO: 6041 hex, 6061 hex, 6063 hex, 6069 hex, 606B hex, 606C hex, 6074 hex; 5810
hex - 581F hex; 5830 hex - 5837 hex  
Only sub-index 0 of the specified objects can be mapped.  
Note:  
As long as A08755 is present, the COB-ID cannot be set to valid.

### A08756 CAN: Number of mapped bytes exceeded

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The number of bytes of the mapped objects exceeds the telegram size for net data.
A max. of 8 bytes is permissible.

**Remedy:**
  
Map fewer objects or objects with a smaller data type.  
See also: p8710, p8711, p8712, p8713, p8714, p8715, p8716, p8717, p8730, p8731, p8732, p8733,
p8734, p8735, p8736, p8737

### A08757 CAN: Set COB-ID invalid

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
For online operation, the appropriate COB-ID must be set invalid before mapping.  
Example:  
Mapping for RPDO 1 should be changed (p8710[0]).  
--&gt; set p8700[0] = C00006E0 hex (invalid COB-ID)  
--&gt; set p8710[0] as required.  
--&gt; p8700[0] enter a valid COB-ID

**Remedy:**
  
Set the COB-ID to invalid.

### A08758 CAN: Maximum number of valid PDO exceeded

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
An attempt was made to exceed the maximum number of valid PDO.  
Alarm value (r2124, interpret decimal):  
1:  
An attempt was made to exceed the total number of valid RPDO of all CANopen supported
drive objects.  
As a result of the hardware, the limit is 25 valid RPDO.  
2:  
An attempt was made to exceed the total number of valid TPDO of all CANopen supported
drive objects.  
The limit is defined by the following ratio:  
CAN sampling time (p8848) / CAN minimum processing time (r8739)  
Note:  
RPDO: Receive Process Data Object  
TPDO: Transmit Process Data Object  
See also: r8739 (Minimum CAN processing time), r8742 (CAN PDO available number)

**Remedy:**
  
Comply with the limit for the maximum number of valid RPDO or TPDO.  
Apply one of the following options to delete the alarm:  
- Successfully write to the COB ID index of a PDO communication parameter (p870x[0],
p872x[0]).  
- Change CANopen NMT state.  
- Execute CANopen NMT command reset node.  
- Execute CANopen NMT command reset communication.  
- Carry out a warm restart (p0009 = 30, p0976 = 2).  
- Carry out a POWER ON (switch-off/switch-on).  
Note:  
The remaining available RPDO or TPDO are indicated in r8742.

### A08759 CAN: PDO COB-ID already available

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Parameter: %1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
An existing PDO COB-ID was allocated.  
Alarm value (r2124, interpret decimal):  
Parameter number.  
Note:  
The COB-ID is included in index zero (p870x[0], p872x[0]).

**Remedy:**
  
Select another PDO COB-ID.

### A08760 CAN: maximum size of the IF PZD exceeded

**Drive object:**
  
All objects

**Valid as of version:**
  
4.6

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The maximum size of the IF PZD was exceeded.  
Alarm value (r2124, interpret decimal):  
1: error for IF PZD receive.  
2: error for IF PZD send.  
Note:  
IF: interface

**Remedy:**
  
Map fewer process data in PDO.  
Apply one of the following options to delete the alarm:  
- POWER ON (switch-off/switch-on).  
- Carry out a warm restart (p0009 = 30, p0976 = 2).  
- Execute CANopen NMT command reset node.  
- Change CANopen NMT state.  
- Delete alarm buffer [0...7] (p2111 = 0).

### A09000 Web server user incorrectly configured

**Drive object:**
  
All objects

**Valid as of version:**
  
4.8

**Message value:**
  
%1

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
An error occurred when configuring the web server user.  
Fault value (r0949, interpret decimal):  
0: No admin password  
1: Invalid admin password  
2: Invalid SINAMICS password

**Remedy:**
  
Correct the user configuration, enter a correct password.

### A09001 Web server security: file required for web server missing

**Drive object:**
  
All objects

**Valid as of version:**
  
5.2

**Message value:**
  
-

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
A file required by the web server was not found on the memory card/device memory.

**Remedy:**
  
Update the firmware with a complete firmware file.

### F13000 License not adequate

**Drive object:**
  
All objects

**Valid as of version:**
  
5.1

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** GLOBAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
- For the converter, the options that require a license are being used but the licenses
are not sufficient.  
- An error occurred when checking the existing licenses.  
Fault value (r0949, interpret decimal):  
0:  
The existing license is not sufficient.  
1:  
An adequate license was not able to be determined as the memory card with the required
licensing data was withdrawn in operation.  
2:  
An adequate license was not able to be determined as there is no licensing data available
on the memory card.  
3:  
An adequate license was not able to be determined as there is a checksum error in
the license key.  
4:  
An internal error occurred when checking the license.

**Remedy:**
  
For fault value = 0:  
Additional licenses are required and these must be activated (p9920, p9921).  
For fault value = 1:  
With the system switched off, re-insert the memory card that matches the system.  
For fault value = 2:  
Enter and activate the license key (p9920, p9921).  
For fault value = 3:  
Compare the license key (p9920) entered with the license key on the Certificate of
License.  
Re-enter the license key and activate (p9920, p9921).  
For fault value = 4:  
- Carry out a POWER ON.  
- Upgrade firmware to later version.  
- Contact Technical Support.  
Note:  
An overview of the converter functions requiring a license can be displayed using
a commissioning tool in the online mode. Depending on the commissioning tool, you
can obtain the necessary licenses (serial number, license Key, Trial License Mode).

### A13001 Error in license checksum

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
When checking the checksum of the license key, an error was detected.

**Remedy:**
  
Compare the license key (p9920) entered with the license key on the Certificate of
License.  
Re-enter the license key and activate (p9920, p9921).

### F13009 Licensing Technology Extension not licensed

**Drive object:**
  
All objects

**Valid as of version:**
  
4.4

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
Vector: OFF1  
Chopper: OFF2  
Infeed: OFF1

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
At least one Technology Extension that requires a license does not have a license.  
Note:  
Refer to r4955 and p4955 for information about the installed Technology Extensions.

**Remedy:**
  
- Enter and activate the license key for Technology Extensions that require a license
(p9920, p9921).  
- If necessary, deactivate Technology Extensions that are not licensed (p4956).  
See also: p9920 (Licensing enter license key), p9921 (Licensing activate license key)

### F13010 Licensing function module not licensed

**Drive object:**
  
All objects

**Valid as of version:**
  
4.4

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
Vector: OFF1  
Chopper: OFF2  
Infeed: OFF1

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
At least one function module requiring a license is not licensed.  
Fault value (r0949, interpret hexadecimal):  
Bit x = 1: The corresponding function module does not have a license.  
Note:  
Assigning bit number to function module, see p0108 or r0108.

**Remedy:**
  
- Enter and activate the license key for function modules that require a license (p9920,
p9921).  
- If necessary, deactivate unlicensed function modules (p0108, r0108).  
See also: p9920 (Licensing enter license key), p9921 (Licensing activate license key)

### A13021 Licensing for output frequencies > 550 Hz missing

**Drive object:**
  
All objects

**Valid as of version:**
  
5.1

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
Configuring the converter results in an output frequency greater than 550 Hz. This
function requires a license. The "High Output Frequency" license is required.  
Note:  
- In this specific case, the output frequency is limited to 550 Hz.  
- The "Trial License" function is not effective for license "High Output Frequency".

**Remedy:**
  
- Enter and activate the license key for "High Output Frequency" and activate (p9920,
p9921).  
- If necessary operate the motor below the output frequency of 550 Hz.

### A13030 Trial License activated

**Drive object:**
  
All objects

**Valid as of version:**
  
5.1

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The "Trial License" function was activated. One of the available periods is expiring.  
See also: p9918 (Licensing active Trial License), r9919 (Licensing Trial License status)

**Remedy:**
  
Not necessary.  
The alarm is automatically withdrawn after the periods have expired.

### A13031 Trial License period expired

**Drive object:**
  
All objects

**Valid as of version:**
  
5.1

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
One of the available periods of the "Trial License" function has expired.  
See also: p9918 (Licensing active Trial License), r9919 (Licensing Trial License status)

**Remedy:**
  
- If required, start an additional period (p9918 = 1).  
- Deactivate functions requiring a license.  
- Appropriately license the drive unit.  
Note:  
A license that is not adequate will only become evident after the next time the system
runs up.

### A13032 Trial License last period activated

**Drive object:**
  
All objects

**Valid as of version:**
  
5.1

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The "Trial License" function was activated. The last of the available periods is expiring.  
See also: p9918 (Licensing active Trial License), r9919 (Licensing Trial License status)

**Remedy:**
  
Not necessary.  
The alarm is automatically withdrawn after the last period has expired.

### A13033 Trial License last period expired

**Drive object:**
  
All objects

**Valid as of version:**
  
5.1

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The last period of the "Trial License" function has expired. No additional periods
available.  
See also: p9918 (Licensing active Trial License), r9919 (Licensing Trial License status)

**Remedy:**
  
- Deactivate functions requiring a license.  
- Appropriately license the drive unit.  
Note:  
A license that is not adequate will only become evident after the next time the system
runs up.

### F13100 Know-how protection: Copy protection error

**Drive object:**
  
All objects

**Valid as of version:**
  
4.5

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** GLOBAL |

  

**Reaction:**
  
Vector: OFF1  
Chopper: OFF2  
Infeed: OFF1

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The know-how protection with copy protection for the memory card is active.  
An error has occurred when checking the memory card.  
Fault value (r0949, interpret decimal):  
0: A memory card is not inserted.  
2: An invalid memory card is inserted.  
3: The memory card is being used in another Control Unit.  
12: An invalid memory card is inserted (OEM input incorrect, p7769).  
13: The memory card is being used in another Control Unit (OEM input incorrect, p7759).  
See also: p7765 (KHP configuration)

**Remedy:**
  
For fault value = 0:  
- Insert the correct memory card and carry out POWER ON.  
For fault value = 2, 3, 12, 13:  
- Contact the responsible OEM.  
- Deactivate copy protection (p7765) and acknowledge the fault (p3981).  
- Deactivate know-how protection (p7766 ... p7768) and acknowledge the fault (p3981).  
Note:  
In general, the copy protection can only be changed when know-how protection is deactivated.  
KHP: Know-How Protection  
See also: p3981 (Acknowledge drive object faults), p7765 (KHP configuration)

### F13101 Know-how protection: Copy protection cannot be activated

**Drive object:**
  
All objects

**Valid as of version:**
  
4.5

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
An error occurred when attempting to activate the copy protection for the memory card.  
Fault value (r0949, interpret decimal):  
0: A memory card is not inserted.  
Note:  
KHP: Know-How Protection

**Remedy:**
  
- Insert the memory card and carry out POWER ON.  
- Try to activate copy protection again (p7765).  
See also: p7765 (KHP configuration)

### F13102 Know-how protection: Consistency error of the protected data

**Drive object:**
  
All objects

**Valid as of version:**
  
4.5

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** GLOBAL |

  

**Reaction:**
  
Vector: OFF1  
Chopper: OFF2  
Infeed: OFF1

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
An error was identified when checking the consistency of the protected files. As a
consequence, the project on the memory card cannot be run.  
Fault value (r0949, interpret hexadecimal):  
yyyyxxxx hex: yyyy = object number, xxxx = fault cause  
xxxx = 1:  
A file has a checksum error.  
xxxx = 2:  
The files are not consistent with one another.  
xxxx = 3:  
The project files, which were loaded into the file system via load (download from
the memory card), are inconsistent.  
Note:  
KHP: Know-How Protection

**Remedy:**
  
- Replace the project on the memory card or replace project files for download from
the memory card.  
- Restore the factory setting and download again.

### F30036 Power unit: Internal overtemperature

**Drive object:**
  
B_INFMV, CU_MV_DP, CU_MV_PN, ENC, HUB, TB30, TECBASE, TM150, TM15DI_DO, TM31, VECTORDM

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Power electronics faulted (5)

| Symbol | Meaning |
| --- | --- |
| **Component:** Power Module | **Propagation:** LOCAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The temperature inside the converter has exceeded the permissible limit value.  
- Insufficient cooling, fan failure.  
- Overload.  
- Ambient temperature too high.  
Fault value (r0949, interpret binary):  
Bit 0 = 1: Overtemperature in the control electronics area.  
Bit 1 = 1: Overtemperature in the power electronics area.  
Bit 2 = 1: Overtemperature in the processor area.  
Bit 3 = 1: Overtemperature in the processor area.  
Bit 4 = 1: Overtemperature when the internal fan is defective.  
Bit 5 = 1: Intake air overtemperature.

**Remedy:**
  
- Check the internal fan.  
- Check the fan elements.  
- Check whether the ambient temperature is in the permissible range.  
Notice:  
This fault can only be acknowledged once the permissible temperature limit minus 5
K has been fallen below.

### N30800 (F) Power unit: Group signal

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Power electronics faulted (5)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
NONE

**Cause:**
  
The power unit has detected at least one fault.

**Remedy:**
  
Evaluate the other messages that are presently available.

Reaction upon F:  
 OFF2

Acknowl. upon F:  
IMMEDIATELY

### F34851 VSM DRIVE-CLiQ (CU): Sign-of-life missing

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, TM150, TM15DI_DO, TM31, VECTOR3P, VECTORDM, VECTORGL,
VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
2.6

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** Voltage Sensing Module (VSM) | **Propagation:** LOCAL |

  

**Reaction:**
  
Vector: NONE (OFF1, OFF2)  
Chopper: NONE (OFF2)  
Infeed: OFF2 (NONE, OFF1)

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A DRIVE-CLiQ communications error has occurred from the Voltage Sensing Module involved
(VSM) to the Control Unit.  
The DRIVE-CLiQ component did not set the sign-of-life to the Control Unit.  
Fault cause:  
10 (= 0A hex):  
The sign-of-life bit in the receive telegram is not set.  
Note regarding the message value:  
The individual information is coded as follows in the message value (r0949/r2124):  
0000yyxx hex: yy = component number, xx = error cause

**Remedy:**
  
Upgrade the firmware of the component involved.

### F34860 VSM DRIVE-CLiQ (CU): Telegram error

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, TM150, TM15DI_DO, TM31, VECTOR3P, VECTORDM, VECTORGL,
VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
2.6

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** Voltage Sensing Module (VSM) | **Propagation:** LOCAL |

  

**Reaction:**
  
Vector: NONE (OFF1, OFF2)  
Chopper: NONE (OFF2)  
Infeed: OFF2 (NONE, OFF1)

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A DRIVE-CLiQ communications error has occurred from the Voltage Sensing Module involved
(VSM) to the Control Unit.  
Fault cause:  
1 (= 01 hex):  
Checksum error (CRC error).  
2 (= 02 hex):  
Telegram is shorter than specified in the length byte or in the receive list.  
3 (= 03 hex):  
Telegram is longer than specified in the length byte or in the receive list.  
4 (= 04 hex):  
The length of the receive telegram does not match the receive list.  
5 (= 05 hex):  
The type of the receive telegram does not match the receive list.  
6 (= 06 hex):  
The address of the power unit in the telegram and in the receive list do not match.  
9 (= 09 hex):  
The DRIVE-CLiQ communication from the DRIVE-CLiQ component involved to the Control
Unit signals that the supply voltage has failed.  
16 (= 10 hex):  
The receive telegram is too early.  
17 (= 11 hex):  
CRC error and the receive telegram is too early.  
18 (= 12 hex):  
The telegram is shorter than that specified in the length byte or in the receive list
and the receive telegram is too early.  
19 (= 13 hex):  
The telegram is longer than that specified in the length byte or in the receive list
and the receive telegram is too early.  
20 (= 14 hex):  
The length of the receive telegram does not match the receive list and the receive
telegram is too early.  
21 (= 15 hex):  
The type of the receive telegram does not match the receive list and the receive telegram
is too early.  
22 (= 16 hex):  
The address of the power unit in the telegram and in the receive list does not match
and the receive telegram is too early.  
25 (= 19 hex):  
The error bit in the receive telegram is set and the receive telegram is too early.  
Note regarding the message value:  
The individual information is coded as follows in the message value (r0949/r2124):  
0000yyxx hex: yy = component number, xx = error cause

**Remedy:**
  
- Carry out a POWER ON (switch-off/switch-on).  
- Check the electrical cabinet design and cable routing for EMC compliance.  
- Check the DRIVE-CLiQ wiring (interrupted cable, contacts, ...).

### F34875 VSM: power supply voltage failed

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, TM150, TM15DI_DO, TM31, VECTOR3P, VECTORDM, VECTORGL,
VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
4.5

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Supply voltage fault (undervoltage) (3)

| Symbol | Meaning |
| --- | --- |
| **Component:** Voltage Sensing Module (VSM) | **Propagation:** LOCAL |

  

**Reaction:**
  
Vector: OFF2  
Chopper: NONE (OFF2)  
Infeed: OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The DRIVE-CLiQ communication from the DRIVE-CLiQ component involved to the Control
Unit signals that the supply voltage has failed.  
Fault cause:  
9 (= 09 hex):  
The power supply voltage for the components has failed.  
Note regarding the message value:  
The individual information is coded as follows in the message value (r0949/r2124):  
0000yyxx hex: yy = component number, xx = error cause

**Remedy:**
  
- Carry out a POWER ON (switch-off/switch-on).  
- Check the power supply voltage wiring for the DRIVE-CLiQ component (interrupted
cable, contacts, ...).  
- Check the dimensioning of the power supply for the DRIVE-CLiQ component.

### F34885 VSM DRIVE-CLiQ (CU): Cyclic data transfer error

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, TM150, TM15DI_DO, TM31, VECTOR3P, VECTORDM, VECTORGL,
VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
2.6

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** Voltage Sensing Module (VSM) | **Propagation:** LOCAL |

  

**Reaction:**
  
Vector: NONE (OFF1, OFF2)  
Chopper: NONE (OFF2)  
Infeed: OFF2 (NONE, OFF1)

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A DRIVE-CLiQ communications error has occurred from the Voltage Sensing Module involved
(VSM) to the Control Unit.  
The nodes do not send and receive in synchronism.  
Fault cause:  
26 (= 1A hex):  
Sign-of-life bit in the receive telegram not set and the receive telegram is too early.  
33 (= 21 hex):  
The cyclic telegram has not been received.  
34 (= 22 hex):  
Timeout in the telegram receive list.  
64 (= 40 hex):  
Timeout in the telegram send list.  
98 (= 62 hex):  
Error at the transition to cyclic operation.  
Note regarding the message value:  
The individual information is coded as follows in the message value (r0949/r2124):  
0000yyxx hex: yy = component number, xx = error cause

**Remedy:**
  
- Check the power supply voltage of the component involved.  
- Carry out a POWER ON.  
- Replace the component involved.

### F34886 VSM DRIVE-CLiQ (CU): Error when sending DRIVE-CLiQ data

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, TM150, TM15DI_DO, TM31, VECTOR3P, VECTORDM, VECTORGL,
VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
2.6

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** Voltage Sensing Module (VSM) | **Propagation:** LOCAL |

  

**Reaction:**
  
Vector: NONE (OFF1, OFF2)  
Chopper: NONE (OFF2)  
Infeed: OFF2 (NONE, OFF1)

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A DRIVE-CLiQ communications error has occurred from the Voltage Sensing Module involved
(VSM) to the Control Unit.  
Data were not able to be sent.  
Fault cause:  
65 (= 41 hex):  
Telegram type does not match send list.  
Note regarding the message value:  
The individual information is coded as follows in the message value (r0949/r2124):  
0000yyxx hex: yy = component number, xx = error cause

**Remedy:**
  
Carry out a POWER ON.

### F34887 VSM DRIVE-CLiQ (CU): Component fault

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, TM150, TM15DI_DO, TM31, VECTOR3P, VECTORDM, VECTORGL,
VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
2.6

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** Voltage Sensing Module (VSM) | **Propagation:** LOCAL |

  

**Reaction:**
  
Vector: NONE (OFF1, OFF2)  
Chopper: NONE (OFF2)  
Infeed: OFF2 (NONE, OFF1)

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
Fault detected on the DRIVE-CLiQ component (Voltage Sensing Module) involved. Faulty
hardware cannot be excluded.  
Fault cause:  
32 (= 20 hex):  
Error in the telegram header.  
35 (= 23 hex):  
Receive error: The telegram buffer memory contains an error.  
66 (= 42 hex):  
Send error: The telegram buffer memory contains an error.  
67 (= 43 hex):  
Send error: The telegram buffer memory contains an error.  
96 (= 60 hex):  
Response received too late during runtime measurement.  
97 (= 61 hex):  
Time taken to exchange characteristic data too long.  
Note regarding the message value:  
The individual information is coded as follows in the message value (r0949/r2124):  
0000yyxx hex: yy = component number, xx = error cause

**Remedy:**
  
- Check the DRIVE-CLiQ wiring (interrupted cable, contacts, ...).  
- Check the electrical cabinet design and cable routing for EMC compliance.  
- If required, use another DRIVE-CLiQ socket (p9904).  
- Replace the component involved.

### F34895 VSM DRIVE-CLiQ (CU): Alternating cyclic data transfer error

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, TM150, TM15DI_DO, TM31, VECTOR3P, VECTORDM, VECTORGL,
VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
2.6

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** Voltage Sensing Module (VSM) | **Propagation:** LOCAL |

  

**Reaction:**
  
Vector: NONE (OFF1, OFF2)  
Chopper: NONE (OFF2)  
Infeed: OFF2 (NONE, OFF1)

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A DRIVE-CLiQ communications error has occurred from the Voltage Sensing Module involved
(VSM) to the Control Unit.  
Fault cause:  
11 (= 0B hex):  
Synchronization error during alternating cyclic data transfer.  
Note regarding the message value:  
The individual information is coded as follows in the message value (r0949/r2124):  
0000yyxx hex: yy = component number, xx = error cause

**Remedy:**
  
Carry out a POWER ON.

### F34896 VSM DRIVE-CLiQ (CU): Inconsistent component properties

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, TM150, TM15DI_DO, TM31, VECTOR3P, VECTORDM, VECTORGL,
VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
2.6

**Message value:**
  
Component number: %1

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** Voltage Sensing Module (VSM) | **Propagation:** LOCAL |

  

**Reaction:**
  
Vector: OFF2 (NONE, OFF1, OFF3)  
Chopper: NONE (OFF2)  
Infeed: OFF2 (NONE, OFF1)

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The properties of the DRIVE-CLiQ component (Voltage Sensing Module), specified by
the fault value, have changed in an incompatible fashion with respect to the properties
when booted. One cause can be, e.g. that a DRIVE-CLiQ cable or DRIVE-CLiQ component
has been replaced.  
Fault value (r0949, interpret decimal):  
Component number.

**Remedy:**
  
- Carry out a POWER ON.  
- When a component is replaced, the same component type and if possible the same firmware
version should be used.  
- When a cable is replaced, only cables whose length is the same as or as close as
possible to the length of the original cables should be used (ensure compliance with
the maximum cable length).

### A35200 (F, N) TM: Calibration data

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, TM150, TM15DI_DO, TM31, VECTOR3P, VECTORDM, VECTORGL,
VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** Terminal Module (TM) | **Propagation:** BICO |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
An error was detected in the calibration data of the Terminal Module.  
Alarm value (r2124, interpret decimal):  
ddcbaa dec: dd = component number, c = AI/AO, b = fault type, aa = number  
c = 0: analog input (AI)  
c = 1: analog output (AO)  
b = 0: No calibration data available.  
b = 1: Offset too high (&gt; 100 mV).

**Remedy:**
  
- Carry out a POWER ON (switch-off/switch-on) for all components.  
- Replace the component if necessary.

Reaction upon F:  
 NONE

Acknowl. upon F:  
IMMEDIATELY (POWER ON)

Reaction upon N:  
 NONE

Acknowl. upon N:  
NONE

### F35207 (N, A) TM: Temperature fault/alarm threshold channel 0 exceeded

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, TM150, TM15DI_DO, TM31, VECTOR3P, VECTORDM, VECTORGL,
VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
External measured value / signal state outside the permissible range (16)

| Symbol | Meaning |
| --- | --- |
| **Component:** Terminal Module (TM) | **Propagation:** BICO |

  

**Reaction:**
  
Vector: OFF2 (NONE, OFF1, OFF3)  
Chopper: OFF2 (NONE)  
Infeed: OFF2 (NONE, OFF1)

**Acknowledge:**
  
IMMEDIATELY (POWER ON)

**Cause:**
  
For the temperature evaluation via the Terminal Module (TM), at least one of the following
conditions to initiate this fault is fulfilled:  
- Alarm threshold has been exceeded longer than that set in the timer (p4102[0], p4103[0]).  
or  
- Fault threshold exceeded (p4102[1]).  
Note:  
For sensor type "PTC thermistor" and "Bimetallic NC contact" (p4100[0] = 1, 4), the
following applies:  
- If r4101[0] &gt; 1650 ohms, the temperature r4105[0] = 250 °C  
- If r4101[0] &lt;= 1650 ohms, the temperature r4105[0] = -50 °C  
The temperature actual value is displayed via connector output r4105[0] and can be
interconnected.  
Notice:  
This fault only causes the drive to shut down if there is at least one BICO interconnection
between the drive and the Terminal Module.  
Fault value (r0949, interpret decimal):  
Temperature actual value at the time of initiation [0.1 °C].

**Remedy:**
  
- Allow the temperature sensor to cool down to below p4102[1] - hysteresis (5 K, for
TM150, can be set using p4118[0]).  
- If required, set the fault response to NONE (p2100, p2101).  
See also: p4102

Reaction upon N:  
 NONE

Acknowl. upon N:  
NONE

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

### A35211 (F, N) TM: Temperature alarm threshold channel 0 exceeded

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, TM150, TM15DI_DO, TM31, VECTOR3P, VECTORDM, VECTORGL,
VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
External measured value / signal state outside the permissible range (16)

| Symbol | Meaning |
| --- | --- |
| **Component:** Terminal Module (TM) | **Propagation:** BICO |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The temperature measured using the temperature sensing of the Terminal Module (TM)
(r4105[0]) has exceeded the threshold value to initiate this alarm (p4102[0]).  
Note:  
For sensor type "PTC thermistor" and "Bimetallic NC contact" (p4100[0] = 1, 4), the
following applies:  
- If r4101[0] &gt; 1650 ohms, the temperature r4105[0] = 250 °C  
- If r4101[0] &lt;= 1650 ohms, the temperature r4105[0] = -50 °C  
Alarm value (r2124, interpret decimal):  
Temperature actual value at the time of initiation [0.1 °C].

**Remedy:**
  
Allow the temperature sensor to cool down to below p4102[0] - hysteresis (5 K, for
TM150, can be set using p4118[0]).  
See also: p4102

Reaction upon F:  
 NONE

Acknowl. upon F:  
IMMEDIATELY (POWER ON)

Reaction upon N:  
 NONE

Acknowl. upon N:  
NONE

### F35220 (N, A) TM: Frequency limit reached for signal output

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, TM15DI_DO, TM31, VECTOR3P, VECTORDM, VECTORGL,
VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Application/technological function faulted (17)

| Symbol | Meaning |
| --- | --- |
| **Component:** Terminal Module (TM) | **Propagation:** BICO |

  

**Reaction:**
  
Vector: OFF1 (NONE, OFF2, OFF3)  
Chopper: OFF2 (NONE)  
Infeed: OFF1 (NONE, OFF2)

**Acknowledge:**
  
IMMEDIATELY (POWER ON)

**Cause:**
  
The signals output from the Terminal Module 41 (TM41) for tracks A/B have reached
the limit frequency. The output signals are no longer in synchronism with the specified
setpoint.  
SIMOTION (p4400 = 0) operating mode:  
- If the TM41 has been configured as the technology project, this fault is also output
in response to short-circuited A/B signals in X520.  
SINAMICS (p4400 = 1) operating mode:  
- The fine resolution of TM41 in p0418 does not match that of the connector input
that was interconnected at p4420  
- The encoder position actual value r0479 interconnected at connector input p4420
has an excessively high actual speed  
- The output signals correspond to a speed, which is greater than the maximum speed
(r1082 of TM41).

**Remedy:**
  
SIMOTION (p4400 = 0) operating mode:  
- Enter a lower speed setpoint (p1155).  
- Reduce the encoder pulse number (p0408).  
- Check track A/B for short-circuits.  
SINAMICS (p4400 = 1) operating mode:  
- Enter a lower speed setpoint (p1155).  
- Reduce the encoder pulse number (p0408).  
Notice:  
The output signal is no longer monitored after changing the message type to "Alarm"
(A).

Reaction upon N:  
 NONE

Acknowl. upon N:  
NONE

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

### F35221 (N, A) TM: Setpoint - actual value deviation outside the tolerance range

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, TM15DI_DO, TM31, VECTOR3P, VECTORDM, VECTORGL,
VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Application/technological function faulted (17)

| Symbol | Meaning |
| --- | --- |
| **Component:** Terminal Module (TM) | **Propagation:** BICO |

  

**Reaction:**
  
Vector: OFF1 (NONE, OFF2, OFF3)  
Chopper: OFF2 (NONE)  
Infeed: OFF1 (NONE, OFF2)

**Acknowledge:**
  
IMMEDIATELY (POWER ON)

**Cause:**
  
The deviation between the setpoint and the output signals (track A/B) exceeds the
tolerance of +/-3 %. The deviation between the internal and external measured value
is too high (&gt; 1000 pulses).

**Remedy:**
  
- Reduce the basic clock cycle (p0110, p0111).  
- If required, replace the component (e.g. internal short-circuit).

Reaction upon N:  
 NONE

Acknowl. upon N:  
NONE

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

### A35222 (F, N) TM: Encoder pulse number not permissible

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, TM15DI_DO, TM31, VECTOR3P, VECTORDM, VECTORGL,
VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** BICO |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The encoder pulse number entered does not match the permissible pulse number from
a hardware perspective.  
Alarm value (r2124, interpret decimal):  
1: Encoder pulse number is too high.  
2: Encoder pulse number is too low.  
4: Encoder pulse number is less than the zero mark offset (p4426).

**Remedy:**
  
- Enter the encoder pulse number in the permissible range (p0408).  
- If necessary, replace TM41 SAC with TM41 DAC.  
Note:  
TM41 SAC: Article No. = 6SL3055-0AA00-3PA0  
TM41 DAC: Article No. = 6SL3055-0AA00-3PA1  
The following applies for TM41 SAC:  
- Minimum/maximum value for p0408: 1000/8192  
The following applies for TM41 DAC:  
- Minimum/maximum value for p0408: 1000/16384  
See also: p0408 (Rotary encoder pulse number)

Reaction upon F:  
Vector: OFF1 (NONE, OFF2, OFF3)  
Chopper: OFF2 (NONE)  
Infeed: OFF1 (NONE, OFF2)

Acknowl. upon F:  
IMMEDIATELY (POWER ON)

Reaction upon N:  
 NONE

Acknowl. upon N:  
NONE

### A35223 (F, N) TM: Zero mark offset not permissible

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, TM15DI_DO, TM31, VECTOR3P, VECTORDM, VECTORGL,
VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Application/technological function faulted (17)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** BICO |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The entered zero mark offset is not permissible.  
Alarm value (r2124, interpret decimal):  
1: Zero mark offset is too high.

**Remedy:**
  
Enter the zero mark offset in the permissible range (p4426).

Reaction upon F:  
Vector: OFF1 (NONE, OFF2, OFF3)  
Chopper: OFF2 (NONE)  
Infeed: OFF1 (NONE, OFF2)

Acknowl. upon F:  
IMMEDIATELY (POWER ON)

Reaction upon N:  
 NONE

Acknowl. upon N:  
NONE

### F35230 TM: Hardware fault

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, TM150, TM15DI_DO, TM31, VECTOR3P, VECTORDM, VECTORGL,
VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** Terminal Module (TM) | **Propagation:** GLOBAL |

  

**Reaction:**
  
Vector: NONE  
Chopper: NONE  
Infeed: OFF1 (NONE, OFF2)

**Acknowledge:**
  
POWER ON

**Cause:**
  
The Terminal Module (TM) used has signaled internal errors.  
Signals from this module may not be evaluated because they are very likely to be incorrect.

**Remedy:**
  
If required, replace the Terminal Module.

### F35233 DRIVE-CLiQ component function not supported

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, TM150, TM31, VECTOR3P, VECTORDM, VECTORGL, VECTORM2C,
VECTORMV, VECTORSL

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** Terminal Module (TM) | **Propagation:** BICO |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A function requested by the Control Unit is not supported by a DRIVE-CLiQ component.  
Fault value (r0949, interpret decimal):  
1: Terminal Module 31 does not support the function "Timer for temperature evaluation"
(X522.7/8, p4103 &gt; 0.000).  
4: The improved actual value resolution is not supported (p4401.4).  
5: The improved setpoint resolution is not supported (p4401.5).  
6: The residual value handling in the setpoint channel cannot be deactivated (p4401.6).  
7: Output frequencies greater than 750 kHz cannot be activated (p4401.7).

**Remedy:**
  
For fault value = 1:  
- Deactivate timer for temperature evaluation (X522.7/8) (p4103 = 0.000).  
- Use Terminal Module 31 and the relevant firmware version to enable the "Timer for
temperature evaluation" function (Article No. 6SL3055-0AA00-3AA1, firmware version
2.6 and higher).  
See also: p4103

### N35800 (F) TM: Group signal

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, TM150, TM15DI_DO, TM31, VECTOR3P, VECTORDM, VECTORGL,
VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** BICO |

  

**Reaction:**
  
Vector: OFF2 (NONE, OFF1, OFF3)  
Chopper: OFF2 (NONE)  
Infeed: OFF2 (NONE, OFF1)

**Acknowledge:**
  
NONE

**Cause:**
  
The Terminal Module has detected at least one fault.

**Remedy:**
  
Evaluates other actual messages.

Reaction upon F:  
Vector: OFF2 (NONE, OFF1, OFF3)  
Chopper: OFF2 (NONE)  
Infeed: OFF2 (NONE, OFF1)

Acknowl. upon F:  
IMMEDIATELY

### F35801 (N, A) TM DRIVE-CLiQ: Sign-of-life missing

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, TM150, TM15DI_DO, TM31, VECTOR3P, VECTORDM, VECTORGL,
VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
4.8

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** BICO |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A DRIVE-CLiQ communication error has occurred between the Control Unit and the Terminal
Module involved.  
Fault cause:  
10 (= 0A hex):  
The sign-of-life bit in the receive telegram is not set.  
Note regarding the message value:  
The individual information is coded as follows in the message value (r0949/r2124):  
0000yyxx hex: yy = component number, xx = error cause

**Remedy:**
  
- Check the DRIVE-CLiQ connection.  
- Replace the component involved.

Reaction upon N:  
 NONE

Acknowl. upon N:  
NONE

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

## SINAMICS Alarms TM31 (Terminal Module) 35802 - 50020

SINAMICS Alarms TM31 (Terminal Module) 35802 - 50020

### A35802 (F, N) TM: Time slice overflow

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, TM150, TM15DI_DO, TM31, VECTOR3P, VECTORDM, VECTORGL,
VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** Terminal Module (TM) | **Propagation:** BICO |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
A time slice overflow has occurred on the Terminal Module.

**Remedy:**
  
Replace the Terminal Module.

Reaction upon F:  
 NONE

Acknowl. upon F:  
IMMEDIATELY (POWER ON)

Reaction upon N:  
 NONE

Acknowl. upon N:  
NONE

### F35804 (N, A) TM: CRC

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, TM150, TM15DI_DO, TM31, VECTOR3P, VECTORDM, VECTORGL,
VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
4.5

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** Terminal Module (TM) | **Propagation:** BICO |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY (POWER ON)

**Cause:**
  
A checksum error has occurred when reading-out the program memory on the Terminal
Module.  
Fault value (r0949, interpret hexadecimal):  
Difference between the checksum at POWER ON and the actual checksum.

**Remedy:**
  
- Check whether the permissible ambient temperature for the component is maintained.  
- Replace the Terminal Module.

Reaction upon N:  
 NONE

Acknowl. upon N:  
NONE

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

### F35805 (N, A) TM: EEPROM checksum error

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, TM150, TM15DI_DO, TM31, VECTOR3P, VECTORDM, VECTORGL,
VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
4.8

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** Terminal Module (TM) | **Propagation:** BICO |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY (POWER ON)

**Cause:**
  
Internal parameter data is corrupted.  
Alarm value (r2124, interpret hexadecimal):  
01: EEPROM access error.  
02: Too many blocks in the EEPROM.

**Remedy:**
  
- Check whether the permissible ambient temperature for the component is maintained.  
- Replace the Terminal Module 31 (TM31).

Reaction upon N:  
 NONE

Acknowl. upon N:  
NONE

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

### F35820 TM DRIVE-CLiQ: Telegram error

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, TM150, TM15DI_DO, TM31, VECTOR3P, VECTORDM, VECTORGL,
VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
2.6

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** Terminal Module (TM) | **Propagation:** BICO |

  

**Reaction:**
  
Vector: OFF1 (OFF2)  
Chopper: OFF2 (NONE)  
Infeed: OFF1 (OFF2)

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A DRIVE-CLiQ communication error has occurred from the Control Unit to the Terminal
Module involved.  
Fault cause:  
1 (= 01 hex):  
Checksum error (CRC error).  
2 (= 02 hex):  
Telegram is shorter than specified in the length byte or in the receive list.  
3 (= 03 hex):  
Telegram is longer than specified in the length byte or in the receive list.  
4 (= 04 hex):  
The length of the receive telegram does not match the receive list.  
5 (= 05 hex):  
The type of the receive telegram does not match the receive list.  
6 (= 06 hex):  
The address of the component in the telegram and in the receive list do not match.  
7 (= 07 hex):  
A SYNC telegram is expected - but the received telegram is not a SYNC telegram.  
8 (= 08 hex):  
No SYNC telegram is expected - but the received telegram is one.  
9 (= 09 hex):  
The error bit in the receive telegram is set.  
16 (= 10 hex):  
The receive telegram is too early.  
Note regarding the message value:  
The individual information is coded as follows in the message value (r0949/r2124):  
0000yyxx hex: yy = component number, xx = error cause

**Remedy:**
  
- Carry out a POWER ON (switch-off/switch-on).  
- Check the electrical cabinet design and cable routing for EMC compliance.  
- Check the DRIVE-CLiQ wiring (interrupted cable, contacts, ...).

### F35835 TM DRIVE-CLiQ: Cyclic data transfer error

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, TM150, TM15DI_DO, TM31, VECTOR3P, VECTORDM, VECTORGL,
VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
2.6

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** Terminal Module (TM) | **Propagation:** BICO |

  

**Reaction:**
  
Vector: OFF1 (OFF2)  
Chopper: OFF2 (NONE)  
Infeed: OFF1 (OFF2)

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A DRIVE-CLiQ communication error has occurred from the Control Unit to the Terminal
Module involved. The nodes do not send and receive in synchronism.  
Fault cause:  
33 (= 21 hex):  
The cyclic telegram has not been received.  
34 (= 22 hex):  
Timeout in the telegram receive list.  
64 (= 40 hex):  
Timeout in the telegram send list.  
Note regarding the message value:  
The individual information is coded as follows in the message value (r0949/r2124):  
0000yyxx hex: yy = component number, xx = error cause

**Remedy:**
  
- Carry out a POWER ON.  
- Replace the component involved.

### F35836 TM DRIVE-CLiQ: Send error for DRIVE-CLiQ data

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, TM150, TM15DI_DO, TM31, VECTOR3P, VECTORDM, VECTORGL,
VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
2.6

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** Terminal Module (TM) | **Propagation:** BICO |

  

**Reaction:**
  
Vector: OFF1 (OFF2)  
Chopper: NONE  
Infeed: OFF1 (OFF2)

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A DRIVE-CLiQ communication error has occurred between the Control Unit and the Terminal
Module involved. Data were not able to be sent.  
Fault cause:  
65 (= 41 hex):  
Telegram type does not match send list.  
Note regarding the message value:  
The individual information is coded as follows in the message value (r0949/r2124):  
0000yyxx hex: yy = component number, xx = error cause

**Remedy:**
  
Carry out a POWER ON.

### F35837 PTM DRIVE-CLiQ: Component fault

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, TM150, TM15DI_DO, TM31, VECTOR3P, VECTORGL, VECTORM2C,
VECTORMV, VECTORSL

**Valid as of version:**
  
2.6

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** Terminal Module (TM) | **Propagation:** BICO |

  

**Reaction:**
  
Vector: OFF1 (OFF2)  
Chopper: NONE  
Infeed: OFF1 (OFF2)

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
Fault detected on the DRIVE-CLiQ component concerned. Faulty hardware cannot be excluded.  
Fault cause:  
32 (= 20 hex):  
Error in the telegram header.  
35 (= 23 hex):  
Receive error: The telegram buffer memory contains an error.  
66 (= 42 hex):  
Send error: The telegram buffer memory contains an error.  
67 (= 43 hex):  
Send error: The telegram buffer memory contains an error.  
Note regarding the message value:  
The individual information is coded as follows in the message value (r0949/r2124):  
0000yyxx hex: yy = component number, xx = error cause

**Remedy:**
  
- Check the DRIVE-CLiQ wiring (interrupted cable, contacts, ...).  
- Check the electrical cabinet design and cable routing for EMC compliance.  
- If required, use another DRIVE-CLiQ socket (p9904).  
- Replace the component involved.

### F35845 TM DRIVE-CLiQ: Cyclic data transfer error

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, TM150, TM15DI_DO, TM31, VECTOR3P, VECTORDM, VECTORGL,
VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
2.6

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** Terminal Module (TM) | **Propagation:** BICO |

  

**Reaction:**
  
Vector: OFF1 (OFF2)  
Chopper: OFF2 (NONE)  
Infeed: OFF1 (OFF2)

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A DRIVE-CLiQ communication error has occurred between the Control Unit and the Terminal
Module (TM) involved.  
Fault cause:  
11 (= 0B hex):  
Synchronization error during alternating cyclic data transfer.  
Note regarding the message value:  
The individual information is coded as follows in the message value (r0949/r2124):  
0000yyxx hex: yy = component number, xx = error cause

**Remedy:**
  
Carry out a POWER ON.

### F35850 TM: Internal software error

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, TM150, TM15DI_DO, TM31, VECTOR3P, VECTORDM, VECTORGL,
VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** Terminal Module (TM) | **Propagation:** BICO |

  

**Reaction:**
  
Vector: OFF1 (NONE, OFF2, OFF3)  
Chopper: OFF2 (NONE)  
Infeed: OFF1 (NONE, OFF2)

**Acknowledge:**
  
POWER ON

**Cause:**
  
An internal software error in the Terminal Module (TM) has occurred.  
Fault value (r0949, interpret decimal):  
1: Background time slice is blocked.  
2: Checksum over the code memory is not OK.

**Remedy:**
  
- Replace the Terminal Module (TM).  
- If required, upgrade the firmware in the Terminal Module.  
- Contact Technical Support.

### F35851 TM DRIVE-CLiQ (CU): Sign-of-life missing

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, TM150, TM15DI_DO, TM31, VECTOR3P, VECTORDM, VECTORGL,
VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
2.6

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** Terminal Module (TM) | **Propagation:** LOCAL |

  

**Reaction:**
  
Vector: OFF1 (OFF2)  
Chopper: OFF2 (NONE)  
Infeed: OFF1 (OFF2)

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A DRIVE-CLiQ communication error has occurred from the Terminal Module involved (TM)
to the Control Unit.  
The DRIVE-CLiQ component did not set the sign-of-life to the Control Unit.  
Fault cause:  
10 (= 0A hex):  
The sign-of-life bit in the receive telegram is not set.  
Note regarding the message value:  
The individual information is coded as follows in the message value (r0949/r2124):  
0000yyxx hex: yy = component number, xx = error cause

**Remedy:**
  
Upgrade the firmware of the component involved.

### F35860 TM DRIVE-CLiQ (CU): Telegram error

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, TM150, TM15DI_DO, TM31, VECTOR3P, VECTORDM, VECTORGL,
VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
2.6

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** Terminal Module (TM) | **Propagation:** LOCAL |

  

**Reaction:**
  
Vector: OFF1 (OFF2)  
Chopper: OFF2 (NONE)  
Infeed: OFF1 (OFF2)

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A DRIVE-CLiQ communication error has occurred from the Terminal Module involved (TM)
to the Control Unit.  
Fault cause:  
1 (= 01 hex):  
Checksum error (CRC error).  
2 (= 02 hex):  
Telegram is shorter than specified in the length byte or in the receive list.  
3 (= 03 hex):  
Telegram is longer than specified in the length byte or in the receive list.  
4 (= 04 hex):  
The length of the receive telegram does not match the receive list.  
5 (= 05 hex):  
The type of the receive telegram does not match the receive list.  
6 (= 06 hex):  
The address of the power unit in the telegram and in the receive list do not match.  
9 (= 09 hex):  
The DRIVE-CLiQ communication from the DRIVE-CLiQ component involved to the Control
Unit signals that the supply voltage has failed.  
16 (= 10 hex):  
The receive telegram is too early.  
17 (= 11 hex):  
CRC error and the receive telegram is too early.  
18 (= 12 hex):  
The telegram is shorter than that specified in the length byte or in the receive list
and the receive telegram is too early.  
19 (= 13 hex):  
The telegram is longer than that specified in the length byte or in the receive list
and the receive telegram is too early.  
20 (= 14 hex):  
The length of the receive telegram does not match the receive list and the receive
telegram is too early.  
21 (= 15 hex):  
The type of the receive telegram does not match the receive list and the receive telegram
is too early.  
22 (= 16 hex):  
The address of the power unit in the telegram and in the receive list does not match
and the receive telegram is too early.  
25 (= 19 hex):  
The error bit in the receive telegram is set and the receive telegram is too early.  
Note regarding the message value:  
The individual information is coded as follows in the message value (r0949/r2124):  
0000yyxx hex: yy = component number, xx = error cause

**Remedy:**
  
- Carry out a POWER ON (switch-off/switch-on).  
- Check the electrical cabinet design and cable routing for EMC compliance.  
- Check the DRIVE-CLiQ wiring (interrupted cable, contacts, ...).

### F35875 TM: power supply voltage failed

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, TM150, TM15DI_DO, TM31, VECTOR3P, VECTORDM, VECTORGL,
VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
4.5

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Supply voltage fault (undervoltage) (3)

| Symbol | Meaning |
| --- | --- |
| **Component:** Terminal Module (TM) | **Propagation:** LOCAL |

  

**Reaction:**
  
Vector: OFF1 (OFF2)  
Chopper: OFF2 (NONE)  
Infeed: OFF1 (OFF2)

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The DRIVE-CLiQ communication from the DRIVE-CLiQ component involved to the Control
Unit signals that the supply voltage has failed.  
Fault cause:  
9 (= 09 hex):  
The power supply voltage for the components has failed.  
Note regarding the message value:  
The individual information is coded as follows in the message value (r0949/r2124):  
0000yyxx hex: yy = component number, xx = error cause

**Remedy:**
  
- Carry out a POWER ON (switch-off/switch-on).  
- Check the power supply voltage wiring for the DRIVE-CLiQ component (interrupted
cable, contacts, ...).  
- Check the dimensioning of the power supply for the DRIVE-CLiQ component.

### F35885 TM DRIVE-CLiQ (CU): Cyclic data transfer error

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, TM150, TM15DI_DO, TM31, VECTOR3P, VECTORDM, VECTORGL,
VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
2.6

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** Terminal Module (TM) | **Propagation:** LOCAL |

  

**Reaction:**
  
Vector: OFF1 (OFF2)  
Chopper: OFF2 (NONE)  
Infeed: OFF1 (OFF2)

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A DRIVE-CLiQ communication error has occurred from the Terminal Module involved (TM)
to the Control Unit.  
The nodes do not send and receive in synchronism.  
Fault cause:  
26 (= 1A hex):  
Sign-of-life bit in the receive telegram not set and the receive telegram is too early.  
33 (= 21 hex):  
The cyclic telegram has not been received.  
34 (= 22 hex):  
Timeout in the telegram receive list.  
64 (= 40 hex):  
Timeout in the telegram send list.  
98 (= 62 hex):  
Error at the transition to cyclic operation.  
Note regarding the message value:  
The individual information is coded as follows in the message value (r0949/r2124):  
0000yyxx hex: yy = component number, xx = error cause

**Remedy:**
  
- Check the power supply voltage of the component involved.  
- Carry out a POWER ON.  
- Replace the component involved.

### F35886 TM DRIVE-CLiQ (CU): Error when sending DRIVE-CLiQ data

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, TM150, TM15DI_DO, TM31, VECTOR3P, VECTORDM, VECTORGL,
VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
2.6

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** Terminal Module (TM) | **Propagation:** LOCAL |

  

**Reaction:**
  
Vector: OFF1 (OFF2)  
Chopper: OFF2 (NONE)  
Infeed: OFF1 (OFF2)

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A DRIVE-CLiQ communication error has occurred from the Terminal Module involved (TM)
to the Control Unit.  
Data were not able to be sent.  
Fault cause:  
65 (= 41 hex):  
Telegram type does not match send list.  
Note regarding the message value:  
The individual information is coded as follows in the message value (r0949/r2124):  
0000yyxx hex: yy = component number, xx = error cause

**Remedy:**
  
Carry out a POWER ON.

### F35887 TM DRIVE-CLiQ (CU): Component fault

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, TM150, TM15DI_DO, TM31, VECTOR3P, VECTORDM, VECTORGL,
VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
2.6

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** Terminal Module (TM) | **Propagation:** LOCAL |

  

**Reaction:**
  
Vector: OFF1 (OFF2)  
Chopper: OFF2 (NONE)  
Infeed: OFF1 (OFF2)

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
Fault detected on the DRIVE-CLiQ component (Terminal Module) involved. Faulty hardware
cannot be excluded.  
Fault cause:  
32 (= 20 hex):  
Error in the telegram header.  
35 (= 23 hex):  
Receive error: The telegram buffer memory contains an error.  
66 (= 42 hex):  
Send error: The telegram buffer memory contains an error.  
67 (= 43 hex):  
Send error: The telegram buffer memory contains an error.  
96 (= 60 hex):  
Response received too late during runtime measurement.  
97 (= 61 hex):  
Time taken to exchange characteristic data too long.  
Note regarding the message value:  
The individual information is coded as follows in the message value (r0949/r2124):  
0000yyxx hex: yy = component number, xx = error cause

**Remedy:**
  
- Check the DRIVE-CLiQ wiring (interrupted cable, contacts, ...).  
- Check the electrical cabinet design and cable routing for EMC compliance.  
- If required, use another DRIVE-CLiQ socket (p9904).  
- Replace the component involved.

### F35895 TM DRIVE-CLiQ (CU): Alternating cyclic data transfer error

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, TM150, TM15DI_DO, TM31, VECTOR3P, VECTORDM, VECTORGL,
VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
2.6

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** Terminal Module (TM) | **Propagation:** LOCAL |

  

**Reaction:**
  
Vector: OFF1 (OFF2)  
Chopper: OFF2 (NONE)  
Infeed: OFF1 (OFF2)

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A DRIVE-CLiQ communication error has occurred from the Terminal Module involved (TM)
to the Control Unit.  
Fault cause:  
11 (= 0B hex):  
Synchronization error during alternating cyclic data transfer.  
Note regarding the message value:  
The individual information is coded as follows in the message value (r0949/r2124):  
0000yyxx hex: yy = component number, xx = error cause

**Remedy:**
  
Carry out a POWER ON.

### F35896 TM DRIVE-CLiQ (CU): Inconsistent component properties

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, TM150, TM15DI_DO, TM31, VECTOR3P, VECTORDM, VECTORGL,
VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
2.6

**Message value:**
  
Component number: %1

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** Terminal Module (TM) | **Propagation:** LOCAL |

  

**Reaction:**
  
Vector: OFF2 (NONE, OFF1, OFF3)  
Chopper: OFF2 (NONE)  
Infeed: OFF2 (NONE, OFF1)

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The properties of the DRIVE-CLiQ component (Terminal Module), specified by the fault
value, have changed in an incompatible fashion with respect to the properties when
booted. One cause can be, e.g. that a DRIVE-CLiQ cable or DRIVE-CLiQ component has
been replaced.  
Fault value (r0949, interpret decimal):  
Component number.

**Remedy:**
  
- Carry out a POWER ON.  
- When a component is replaced, the same component type and if possible the same firmware
version should be used.  
- When a cable is replaced, only cables whose length is the same as or as close as
possible to the length of the original cables should be used (ensure compliance with
the maximum cable length).

### N35898 (A) TM: POWER ON signal

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, TM150, TM15DI_DO, TM31, VECTOR3P, VECTORDM, VECTORGL,
VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** Terminal Module (TM) | **Propagation:** BICO |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The Terminal Module signals the start of the ramp-up.

**Remedy:**
  
Not necessary.

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

### F35899 (N, A) TM: Unknown fault

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, TM150, TM15DI_DO, TM31, VECTOR3P, VECTORDM, VECTORGL,
VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
2.6

**Message value:**
  
New message: %1

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** Terminal Module (TM) | **Propagation:** BICO |

  

**Reaction:**
  
Vector: NONE (OFF1, OFF2, OFF3)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF1, OFF2)

**Acknowledge:**
  
IMMEDIATELY (POWER ON)

**Cause:**
  
A fault has occurred on the Terminal Module that cannot be interpreted by the Control
Unit firmware.  
This can occur if the firmware on this component is more recent than the firmware
on the Control Unit.  
Fault value (r0949, interpret decimal):  
Fault number.  
Note:  
If required, the significance of this new fault can be read about in a more recent
description of the Control Unit.

**Remedy:**
  
- Replace the firmware on the Terminal Module by an older firmware version (r0158).  
- Upgrade the firmware on the Control Unit (r0018).

Reaction upon N:  
 NONE

Acknowl. upon N:  
NONE

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

### A35903 (F, N) TM: I2C bus error occurred

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, TM150, TM15DI_DO, TM31, VECTOR3P, VECTORDM, VECTORGL,
VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** Terminal Module (TM) | **Propagation:** BICO |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
An error has occurred while accessing the internal I2C bus of the Terminal Module.

**Remedy:**
  
Replace the Terminal Module.

Reaction upon F:  
 NONE

Acknowl. upon F:  
IMMEDIATELY (POWER ON)

Reaction upon N:  
 NONE

Acknowl. upon N:  
NONE

### A35904 (F, N) TM: EEPROM

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, TM150, TM15DI_DO, TM31, VECTOR3P, VECTORDM, VECTORGL,
VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** Terminal Module (TM) | **Propagation:** BICO |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
An error has occurred accessing the non-volatile memory on the Terminal Module.

**Remedy:**
  
Replace the Terminal Module.

Reaction upon F:  
 NONE

Acknowl. upon F:  
IMMEDIATELY (POWER ON)

Reaction upon N:  
 NONE

Acknowl. upon N:  
NONE

### A35905 (F, N) TM: Parameter access

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, TM150, TM15DI_DO, TM31, VECTOR3P, VECTORDM, VECTORGL,
VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** Terminal Module (TM) | **Propagation:** BICO |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The Control Unit attempted to write an illegal parameter value to the Terminal Module.

**Remedy:**
  
- Check whether the firmware version of the Terminal Module (r0158) matches the firmware
version of Control Unit (r0018).  
- If required, replace the Terminal Module.  
Note:  
The firmware versions that match each other are in the readme.txt file on the memory
card.

Reaction upon F:  
 NONE

Acknowl. upon F:  
IMMEDIATELY (POWER ON)

Reaction upon N:  
 NONE

Acknowl. upon N:  
NONE

### A35906 (F, N) TM: 24 V power supply missing

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, TM150, TM15DI_DO, TM31, VECTOR3P, VECTORDM, VECTORGL,
VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Supply voltage fault (undervoltage) (3)

| Symbol | Meaning |
| --- | --- |
| **Component:** Terminal Module (TM) | **Propagation:** BICO |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The 24 V power supply for the digital outputs is missing.  
Alarm value (r2124, interpret hexadecimal):  
01: TM17 24 V power supply for DI/DO 0 ... 7 missing.  
02: TM17 24 V power supply for DI/DO 8 ... 15 missing.  
04: TM15 24 V power supply for DI/DO 0 ... 7 (X520) missing.  
08: TM15 24 V power supply for DI/DO 8 ... 15 (X521) missing.  
10: TM15 24 V power supply for DI/DO 16 ... 23 (X522) missing.  
20: TM41 24 V power supply for DI/DO 0 ... 3 missing.

**Remedy:**
  
Check the terminals for the power supply voltage (L1+, L2+, L3+, M or +24 V_1 for
TM41).

Reaction upon F:  
 NONE

Acknowl. upon F:  
IMMEDIATELY (POWER ON)

Reaction upon N:  
 NONE

Acknowl. upon N:  
NONE

### A35907 (F, N) TM: Hardware initialization error

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, TM150, TM15DI_DO, TM31, VECTOR3P, VECTORDM, VECTORGL,
VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** Terminal Module (TM) | **Propagation:** BICO |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The Terminal Module was not successfully initialized.  
Alarm value (r2124, interpret hexadecimal):  
01: TM17 or TM41 - Incorrect configuration request.  
02: TM17 or TM41 - programming not successful.  
04: TM17 or TM41 - Invalid time stamp

**Remedy:**
  
Carry out a POWER ON.

Reaction upon F:  
 NONE

Acknowl. upon F:  
IMMEDIATELY (POWER ON)

Reaction upon N:  
 NONE

Acknowl. upon N:  
NONE

### A35910 (F, N) TM: Module overtemperature

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, TM150, TM15DI_DO, TM31, VECTOR3P, VECTORDM, VECTORGL,
VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Overtemperature of the electronic components (6)

| Symbol | Meaning |
| --- | --- |
| **Component:** Terminal Module (TM) | **Propagation:** BICO |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The temperature in the module has exceeded the highest permissible limit.

**Remedy:**
  
- Reduce the ambient temperature.  
- Replace the Terminal Module.

Reaction upon F:  
 NONE

Acknowl. upon F:  
IMMEDIATELY (POWER ON)

Reaction upon N:  
 NONE

Acknowl. upon N:  
NONE

### A35911 (F, N) TM: Clock synchronous operation sign-of-life missing

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, TM150, TM15DI_DO, TM31, VECTOR3P, VECTORDM, VECTORGL,
VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** BICO |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The maximum permissible number of errors in the master sign-of-life (clock synchronous
operation) has been exceeded in cyclic operation.  
When the alarm is output, the module outputs are reset up to the next synchronization.

**Remedy:**
  
- Check the physical bus configuration (terminating resistor, shielding, etc.).  
- Check the interconnection of the master sign-of-life (r4201 via p0915).  
- Check whether the master correctly sends the sign-of-life (e.g. set up a trace with
r4201.12 ... r4201.15 and trigger signal r4301.9).  
- Check the bus and master for utilization level (e.g. bus cycle time Tdp was set
too short).

Reaction upon F:  
 NONE

Acknowl. upon F:  
IMMEDIATELY (POWER ON)

Reaction upon N:  
 NONE

Acknowl. upon N:  
NONE

### A35920 (F, N) TM: Error temperature sensor channel 0

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, TM150, TM15DI_DO, TM31, VECTOR3P, VECTORDM, VECTORGL,
VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
External measured value / signal state outside the permissible range (16)

| Symbol | Meaning |
| --- | --- |
| **Component:** Terminal Module (TM) | **Propagation:** BICO |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
When evaluating the temperature sensor, an error occurred.  
Alarm value (r2124, interpret decimal):  
1: Wire breakage or sensor not connected.  
KTY84: R &gt; 1630 Ohm (TM150: R &gt; 2170 Ohm), PT100: R &gt; 194 Ohm, PT1000: R &gt; 1720 Ohm
(TM150: R &gt; 1944 Ohm)  
2: Measured resistance too low.  
PTC thermistor: R &lt; 20 Ohm, KTY84: R &lt; 50 Ohm (TM150: R &lt; 180 Ohm), PT100: R &lt; 60
Ohm, PT1000: R &lt; 603 Ohm

**Remedy:**
  
- Make sure that the sensor is connected correctly.  
- Replace the sensor.

Reaction upon F:  
Vector: NONE (OFF2)  
Chopper: NONE  
Infeed: NONE

Acknowl. upon F:  
IMMEDIATELY (POWER ON)

Reaction upon N:  
 NONE

Acknowl. upon N:  
NONE

### A35999 (F, N) TM: Unknown alarm

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, TM150, TM15DI_DO, TM31, VECTOR3P, VECTORDM, VECTORGL,
VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
2.6

**Message value:**
  
New message: %1

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** Terminal Module (TM) | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
An alarm has occurred on the Terminal Module that cannot be interpreted by the Control
Unit firmware.  
This can occur if the firmware on this component is more recent than the firmware
on the Control Unit.  
Alarm value (r2124, interpret decimal):  
Alarm number.  
Note:  
If required, the significance of this new alarm can be read about in a more recent
description of the Control Unit.

**Remedy:**
  
- Replace the firmware on the Terminal Module by an older firmware version (r0158).  
- Upgrade the firmware on the Control Unit (r0018).

Reaction upon F:  
Vector: NONE (OFF1, OFF2, OFF3)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF1, OFF2)

Acknowl. upon F:  
IMMEDIATELY (POWER ON)

Reaction upon N:  
 NONE

Acknowl. upon N:  
NONE

### F36851 Hub DRIVE-CLiQ (CU): Sign-of-life missing

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, HUB, TM150, TM15DI_DO, TM31, VECTOR3P, VECTORDM,
VECTORGL, VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
2.6

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** Terminal Board (TB) | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
DRIVE-CLiQ communication error from DRIVE-CLiQ Hub Module in question to Control Unit.  
The DRIVE-CLiQ component did not set the sign-of-life to the Control Unit.  
Fault cause:  
10 (= 0A hex):  
The sign-of-life bit in the receive telegram is not set.  
Note regarding the message value:  
The individual information is coded as follows in the message value (r0949/r2124):  
0000yyxx hex: yy = component number, xx = error cause

**Remedy:**
  
Upgrade the firmware of the component involved.

### F36860 Hub DRIVE-CLiQ (CU): Telegram error

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, HUB, TM150, TM15DI_DO, TM31, VECTOR3P, VECTORDM,
VECTORGL, VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
2.6

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** Terminal Board (TB) | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
DRIVE-CLiQ communication error from DRIVE-CLiQ Hub Module in question to Control Unit.  
Fault cause:  
1 (= 01 hex):  
Checksum error (CRC error).  
2 (= 02 hex):  
Telegram is shorter than specified in the length byte or in the receive list.  
3 (= 03 hex):  
Telegram is longer than specified in the length byte or in the receive list.  
4 (= 04 hex):  
The length of the receive telegram does not match the receive list.  
5 (= 05 hex):  
The type of the receive telegram does not match the receive list.  
6 (= 06 hex):  
The address of the power unit in the telegram and in the receive list do not match.  
9 (= 09 hex):  
The DRIVE-CLiQ communication from the DRIVE-CLiQ component involved to the Control
Unit signals that the supply voltage has failed.  
16 (= 10 hex):  
The receive telegram is too early.  
17 (= 11 hex):  
CRC error and the receive telegram is too early.  
18 (= 12 hex):  
The telegram is shorter than that specified in the length byte or in the receive list
and the receive telegram is too early.  
19 (= 13 hex):  
The telegram is longer than that specified in the length byte or in the receive list
and the receive telegram is too early.  
20 (= 14 hex):  
The length of the receive telegram does not match the receive list and the receive
telegram is too early.  
21 (= 15 hex):  
The type of the receive telegram does not match the receive list and the receive telegram
is too early.  
22 (= 16 hex):  
The address of the power unit in the telegram and in the receive list does not match
and the receive telegram is too early.  
25 (= 19 hex):  
The error bit in the receive telegram is set and the receive telegram is too early.  
Note regarding the message value:  
The individual information is coded as follows in the message value (r0949/r2124):  
0000yyxx hex: yy = component number, xx = error cause

**Remedy:**
  
- Carry out a POWER ON (switch-off/switch-on).  
- Check the electrical cabinet design and cable routing for EMC compliance.  
- Check the DRIVE-CLiQ wiring (interrupted cable, contacts, ...).

### F36875 HUB: power supply voltage failed

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, HUB, TM150, TM15DI_DO, TM31, VECTOR3P, VECTORDM,
VECTORGL, VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
4.5

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Supply voltage fault (undervoltage) (3)

| Symbol | Meaning |
| --- | --- |
| **Component:** Terminal Board (TB) | **Propagation:** LOCAL |

  

**Reaction:**
  
Vector: OFF1 (OFF2)  
Chopper: OFF2 (NONE)  
Infeed: OFF1 (OFF2)

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The DRIVE-CLiQ communication from the DRIVE-CLiQ component involved to the Control
Unit signals that the supply voltage has failed.  
Fault cause:  
9 (= 09 hex):  
The power supply voltage for the components has failed.  
Note regarding the message value:  
The individual information is coded as follows in the message value (r0949/r2124):  
0000yyxx hex: yy = component number, xx = error cause

**Remedy:**
  
- Carry out a POWER ON (switch-off/switch-on).  
- Check the power supply voltage wiring for the DRIVE-CLiQ component (interrupted
cable, contacts, ...).  
- Check the dimensioning of the power supply for the DRIVE-CLiQ component.

### F36885 Hub DRIVE-CLiQ (CU): Cyclic data transfer error

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, HUB, TM150, TM15DI_DO, TM31, VECTOR3P, VECTORDM,
VECTORGL, VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
2.6

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** Terminal Board (TB) | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
DRIVE-CLiQ communication error from DRIVE-CLiQ Hub Module in question to the Control
Unit.  
The nodes do not send and receive in synchronism.  
Fault cause:  
26 (= 1A hex):  
Sign-of-life bit in the receive telegram not set and the receive telegram is too early.  
33 (= 21 hex):  
The cyclic telegram has not been received.  
34 (= 22 hex):  
Timeout in the telegram receive list.  
64 (= 40 hex):  
Timeout in the telegram send list.  
98 (= 62 hex):  
Error at the transition to cyclic operation.  
Note regarding the message value:  
The individual information is coded as follows in the message value (r0949/r2124):  
0000yyxx hex: yy = component number, xx = error cause

**Remedy:**
  
- Check the supply voltage of the component involved.  
- Carry out a POWER ON.  
- Replace the component involved.

### F36886 Hub DRIVE-CLiQ (CU): Error when sending DRIVE-CLiQ data

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, HUB, TM150, TM15DI_DO, TM31, VECTOR3P, VECTORDM,
VECTORGL, VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
2.6

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** Terminal Board (TB) | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
DRIVE-CLiQ communication error from DRIVE-CLiQ Hub Module in question to Control Unit.  
Data were not able to be sent.  
Fault cause:  
65 (= 41 hex):  
Telegram type does not match send list.  
Note regarding the message value:  
The individual information is coded as follows in the message value (r0949/r2124):  
0000yyxx hex: yy = component number, xx = error cause

**Remedy:**
  
Carry out a POWER ON.

### F36887 Hub DRIVE-CLiQ (CU): Component fault

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, HUB, TM150, TM15DI_DO, TM31, VECTOR3P, VECTORDM,
VECTORGL, VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
2.6

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** Terminal Board (TB) | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
Fault detected on the DRIVE-CLiQ component (DRIVE-CLiQ Hub Module) involved. Faulty
hardware cannot be excluded.  
Fault cause:  
32 (= 20 hex):  
Error in the telegram header.  
35 (= 23 hex):  
Receive error: The telegram buffer memory contains an error.  
66 (= 42 hex):  
Send error: The telegram buffer memory contains an error.  
67 (= 43 hex):  
Send error: The telegram buffer memory contains an error.  
96 (= 60 hex):  
Response received too late during runtime measurement.  
97 (= 61 hex):  
Time taken to exchange characteristic data too long.  
Note regarding the message value:  
The individual information is coded as follows in the message value (r0949/r2124):  
0000yyxx hex: yy = component number, xx = error cause

**Remedy:**
  
- Check the DRIVE-CLiQ wiring (interrupted cable, contacts, ...).  
- Check the electrical cabinet design and cable routing for EMC compliance.  
- If required, use another DRIVE-CLiQ socket (p9904).  
- Replace the component involved.

### F36895 Hub DRIVE-CLiQ (CU): Alternating cyclic data transfer error

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, HUB, TM150, TM15DI_DO, TM31, VECTOR3P, VECTORDM,
VECTORGL, VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
2.6

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** Terminal Board (TB) | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
DRIVE-CLiQ communication error from DRIVE-CLiQ Hub Module in question to Control Unit.  
Fault cause:  
11 (= 0B hex):  
Synchronization error during alternating cyclic data transfer.  
Note regarding the message value:  
The individual information is coded as follows in the message value (r0949/r2124):  
0000yyxx hex: yy = component number, xx = error cause

**Remedy:**
  
Carry out a POWER ON.

### F36896 Hub DRIVE-CLiQ (CU): Inconsistent component properties

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, HUB, TM150, TM15DI_DO, TM31, VECTOR3P, VECTORDM,
VECTORGL, VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
2.6

**Message value:**
  
Component number: %1

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** Terminal Board (TB) | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The properties of the DRIVE-CLiQ component (DRIVE-CLiQ Hub Module), specified by the
fault value, have changed in an incompatible fashion with respect to the properties
when booted. One cause can be, e.g. that a DRIVE-CLiQ cable or DRIVE-CLiQ component
has been replaced.  
Fault value (r0949, interpret decimal):  
Component number.

**Remedy:**
  
- Carry out a POWER ON.  
- When a component is replaced, the same component type and if possible the same firmware
version should be used.  
- When a cable is replaced, only cables whose length is the same as or as close as
possible to the length of the original cables should be used (ensure compliance with
the maximum cable length).

### F40000 Fault at DRIVE-CLiQ socket X100

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A fault has occurred at the drive object at the DRIVE-CLiQ socket X100.  
Fault value (r0949, interpret decimal):  
First fault that has occurred for this drive object.

**Remedy:**
  
Evaluate the fault buffer of the specified object.

### F40001 Fault at DRIVE-CLiQ socket X101

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A fault has occurred at the drive object at the DRIVE-CLiQ socket X101.  
Fault value (r0949, interpret decimal):  
First fault that has occurred for this drive object.

**Remedy:**
  
Evaluate the fault buffer of the specified object.

### F40002 Fault at DRIVE-CLiQ socket X102

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A fault has occurred at the drive object at the DRIVE-CLiQ socket X102.  
Fault value (r0949, interpret decimal):  
First fault that has occurred for this drive object.

**Remedy:**
  
Evaluate the fault buffer of the specified object.

### F40003 Fault at DRIVE-CLiQ socket X103

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A fault has occurred at the drive object at the DRIVE-CLiQ socket X103.  
Fault value (r0949, interpret decimal):  
First fault that has occurred for this drive object.

**Remedy:**
  
Evaluate the fault buffer of the specified object.

### F40004 Fault at DRIVE-CLiQ socket X104

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A fault has occurred at the drive object at the DRIVE-CLiQ socket X104.  
Fault value (r0949, interpret decimal):  
First fault that has occurred for this drive object.

**Remedy:**
  
Evaluate the fault buffer of the specified object.

### F40005 Fault at DRIVE-CLiQ socket X105

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A fault has occurred at the drive object at the DRIVE-CLiQ socket X105.  
Fault value (r0949, interpret decimal):  
First fault that has occurred for this drive object.

**Remedy:**
  
Evaluate the fault buffer of the specified object.

### A40100 Alarm at DRIVE-CLiQ socket X100

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
An alarm has occurred at the drive object at the DRIVE-CLiQ socket X100.  
Alarm value (r2124, interpret decimal):  
First alarm that has occurred for this drive object.

**Remedy:**
  
Evaluate the alarm buffer of the specified object.

### A40101 Alarm at DRIVE-CLiQ socket X101

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
An alarm has occurred at the drive object at the DRIVE-CLiQ socket X101.  
Alarm value (r2124, interpret decimal):  
First alarm that has occurred for this drive object.

**Remedy:**
  
Evaluate the alarm buffer of the specified object.

### A40102 Alarm at DRIVE-CLiQ socket X102

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
An alarm has occurred at the drive object at the DRIVE-CLiQ socket X102.  
Alarm value (r2124, interpret decimal):  
First alarm that has occurred for this drive object.

**Remedy:**
  
Evaluate the alarm buffer of the specified object.

### A40103 Alarm at DRIVE-CLiQ socket X103

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
An alarm has occurred at the drive object at the DRIVE-CLiQ socket X103.  
Alarm value (r2124, interpret decimal):  
First alarm that has occurred for this drive object.

**Remedy:**
  
Evaluate the alarm buffer of the specified object.

### A40104 Alarm at DRIVE-CLiQ socket X104

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
An alarm has occurred at the drive object at the DRIVE-CLiQ socket X104.  
Alarm value (r2124, interpret decimal):  
First alarm that has occurred for this drive object.

**Remedy:**
  
Evaluate the alarm buffer of the specified object.

### A40105 Alarm at DRIVE-CLiQ socket X105

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
An alarm has occurred at the drive object at the DRIVE-CLiQ socket X105.  
Alarm value (r2124, interpret decimal):  
First alarm that has occurred for this drive object.

**Remedy:**
  
Evaluate the alarm buffer of the specified object.

### F40799 CX32: Configured transfer end time exceeded

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The configured transfer end time when transferring the cyclic actual values was exceeded.

**Remedy:**
  
- Carry out a POWER ON (switch-off/switch-on) for all components.  
- Contact Technical Support.

### F40801 CX32 DRIVE-CLiQ: Sign-of-life missing

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** LOCAL |

  

**Reaction:**
  
Vector: OFF2  
Chopper: NONE (OFF2)  
Infeed: OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A DRIVE-CLiQ communications error has occurred from the Control Unit to the controller
extension involved.  
Fault cause:  
10 (= 0A hex):  
The sign-of-life bit in the receive telegram is not set.  
Note regarding the message value:  
The individual information is coded as follows in the message value (r0949/r2124):  
0000yyxx hex: yy = component number, xx = error cause

**Remedy:**
  
- Carry out a POWER ON (switch-off/switch-on).  
- Replace the component involved.

### F40820 CX32 DRIVE-CLiQ: Telegram error

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** DRIVE-CLiQ Hub Module (Hub) | **Propagation:** LOCAL |

  

**Reaction:**
  
Vector: OFF2  
Chopper: NONE (OFF2)  
Infeed: OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A DRIVE-CLiQ communications error has occurred from the Control Unit to the controller
extension involved.  
Fault cause:  
1 (= 01 hex):  
Checksum error (CRC error).  
2 (= 02 hex):  
Telegram is shorter than specified in the length byte or in the receive list.  
3 (= 03 hex):  
Telegram is longer than specified in the length byte or in the receive list.  
4 (= 04 hex):  
The length of the receive telegram does not match the receive list.  
5 (= 05 hex):  
The type of the receive telegram does not match the receive list.  
6 (= 06 hex):  
The address of the component in the telegram and in the receive list do not match.  
7 (= 07 hex):  
A SYNC telegram is expected - but the received telegram is not a SYNC telegram.  
8 (= 08 hex):  
No SYNC telegram is expected - but the received telegram is one.  
9 (= 09 hex):  
The error bit in the receive telegram is set.  
16 (= 10 hex):  
The receive telegram is too early.  
Note regarding the message value:  
The individual information is coded as follows in the message value (r0949/r2124):  
0000yyxx hex: yy = component number, xx = error cause

**Remedy:**
  
- Carry out a POWER ON (switch-off/switch-on).  
- Check the electrical cabinet design and cable routing for EMC compliance.  
- Check the DRIVE-CLiQ wiring (interrupted cable, contacts, ...).

### F40825 CX32 DRIVE-CLiQ: Supply voltage failed

**Drive object:**
  
All objects

**Valid as of version:**
  
4.5

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Supply voltage fault (undervoltage) (3)

| Symbol | Meaning |
| --- | --- |
| **Component:** DRIVE-CLiQ Hub Module (Hub) | **Propagation:** LOCAL |

  

**Reaction:**
  
Vector: OFF1 (OFF2)  
Chopper: NONE (OFF2)  
Infeed: OFF1 (OFF2)

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The DRIVE-CLiQ communication from the DRIVE-CLiQ component involved to the Control
Unit signals that the supply voltage has failed.  
Fault cause:  
9 (= 09 hex):  
The power supply voltage for the components has failed.  
Note regarding the message value:  
The individual information is coded as follows in the message value (r0949/r2124):  
0000yyxx hex: yy = component number, xx = error cause

**Remedy:**
  
- Carry out a POWER ON (switch-off/switch-on).  
- Check the supply voltage wiring of the DRIVE-CLiQ component (interrupted cable,
contacts, ...).  
- Check the dimensioning of the DRIVE-CLiQ component power supply.

### F40835 CX32 DRIVE-CLiQ: Cyclic data transfer error

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** DRIVE-CLiQ Hub Module (Hub) | **Propagation:** LOCAL |

  

**Reaction:**
  
Vector: OFF2  
Chopper: NONE (OFF2)  
Infeed: OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A DRIVE-CLiQ communications error has occurred from the Control Unit to the controller
extension involved. The nodes do not send and receive in synchronism.  
Fault cause:  
33 (= 21 hex):  
The cyclic telegram has not been received.  
34 (= 22 hex):  
Timeout in the telegram receive list.  
64 (= 40 hex):  
Timeout in the telegram send list.  
Note regarding the message value:  
The individual information is coded as follows in the message value (r0949/r2124):  
0000yyxx hex: yy = component number, xx = error cause

**Remedy:**
  
- Carry out a POWER ON (switch-off/switch-on).  
- Replace the component involved.

### F40836 CX32 DRIVE-CLiQ: Send error for DRIVE-CLiQ data

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** DRIVE-CLiQ Hub Module (Hub) | **Propagation:** LOCAL |

  

**Reaction:**
  
Vector: OFF2  
Chopper: NONE (OFF2)  
Infeed: OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A DRIVE-CLiQ communications error has occurred from the Control Unit to the controller
extension involved. Data were not able to be sent.  
Fault cause:  
65 (= 41 hex):  
Telegram type does not match send list.  
Note regarding the message value:  
The individual information is coded as follows in the message value (r0949/r2124):  
0000yyxx hex: yy = component number, xx = error cause

**Remedy:**
  
Carry out a POWER ON (switch-off/switch-on).

### F40837 CX32 DRIVE-CLiQ: Component fault

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** DRIVE-CLiQ Hub Module (Hub) | **Propagation:** LOCAL |

  

**Reaction:**
  
Vector: OFF2  
Chopper: NONE (OFF2)  
Infeed: OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
Fault detected on the DRIVE-CLiQ component concerned. Faulty hardware cannot be excluded.  
Fault cause:  
32 (= 20 hex):  
Error in the telegram header.  
35 (= 23 hex):  
Receive error: The telegram buffer memory contains an error.  
66 (= 42 hex):  
Send error: The telegram buffer memory contains an error.  
67 (= 43 hex):  
Send error: The telegram buffer memory contains an error.  
Note regarding the message value:  
The individual information is coded as follows in the message value (r0949/r2124):  
0000yyxx hex: yy = component number, xx = error cause

**Remedy:**
  
- Check the DRIVE-CLiQ wiring (interrupted cable, contacts, ...).  
- Check the electrical cabinet design and cable routing for EMC compliance.  
- If required, use another DRIVE-CLiQ socket (p9904).  
- Replace the component involved.

### F40845 CX32 DRIVE-CLiQ: Cyclic data transfer error

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** DRIVE-CLiQ Hub Module (Hub) | **Propagation:** LOCAL |

  

**Reaction:**
  
Vector: OFF2  
Chopper: NONE (OFF2)  
Infeed: OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A DRIVE-CLiQ communications error has occurred from the Control Unit to the controller
extension involved.  
Fault cause:  
11 (= 0B hex):  
Synchronization error during alternating cyclic data transfer.  
Note regarding the message value:  
The individual information is coded as follows in the message value (r0949/r2124):  
0000yyxx hex: yy = component number, xx = error cause

**Remedy:**
  
Carry out a POWER ON (switch-off/switch-on).

### F40851 CX32 DRIVE-CLiQ (CU): Sign-of-life missing

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** DRIVE-CLiQ Hub Module (Hub) | **Propagation:** LOCAL |

  

**Reaction:**
  
Vector: OFF2  
Chopper: NONE (OFF2)  
Infeed: OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A DRIVE-CLiQ communications error has occurred from the controller extension involved
to the Control Unit.  
The DRIVE-CLiQ component did not set the sign-of-life to the Control Unit.  
Fault cause:  
10 (= 0A hex):  
The sign-of-life bit in the receive telegram is not set.  
Note regarding the message value:  
The individual information is coded as follows in the message value (r0949/r2124):  
0000yyxx hex: yy = component number, xx = error cause

**Remedy:**
  
Upgrade the firmware of the component involved.

### F40860 CX32 DRIVE-CLiQ (CU): Telegram error

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** DRIVE-CLiQ Hub Module (Hub) | **Propagation:** LOCAL |

  

**Reaction:**
  
Vector: OFF2  
Chopper: NONE (OFF2)  
Infeed: OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A DRIVE-CLiQ communications error has occurred from the controller extension involved
to the Control Unit.  
Fault cause:  
1 (= 01 hex):  
Checksum error (CRC error).  
2 (= 02 hex):  
Telegram is shorter than specified in the length byte or in the receive list.  
3 (= 03 hex):  
Telegram is longer than specified in the length byte or in the receive list.  
4 (= 04 hex):  
The length of the receive telegram does not match the receive list.  
5 (= 05 hex):  
The type of the receive telegram does not match the receive list.  
6 (= 06 hex):  
The address of the power unit in the telegram and in the receive list do not match.  
9 (= 09 hex):  
The error bit in the receive telegram is set.  
16 (= 10 hex):  
The receive telegram is too early.  
17 (= 11 hex):  
CRC error and the receive telegram is too early.  
18 (= 12 hex):  
The telegram is shorter than that specified in the length byte or in the receive list
and the receive telegram is too early.  
19 (= 13 hex):  
The telegram is longer than that specified in the length byte or in the receive list
and the receive telegram is too early.  
20 (= 14 hex):  
The length of the receive telegram does not match the receive list and the receive
telegram is too early.  
21 (= 15 hex):  
The type of the receive telegram does not match the receive list and the receive telegram
is too early.  
22 (= 16 hex):  
The address of the power unit in the telegram and in the receive list does not match
and the receive telegram is too early.  
25 (= 19 hex):  
The error bit in the receive telegram is set and the receive telegram is too early.  
Note regarding the message value:  
The individual information is coded as follows in the message value (r0949/r2124):  
0000yyxx hex: yy = component number, xx = error cause

**Remedy:**
  
- Carry out a POWER ON (switch-off/switch-on).  
- Check the electrical cabinet design and cable routing for EMC compliance.  
- Check the DRIVE-CLiQ wiring (interrupted cable, contacts, ...).

### F40875 CX32 DRIVE-CLiQ (CU): Supply voltage failed

**Drive object:**
  
All objects

**Valid as of version:**
  
4.5

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Supply voltage fault (undervoltage) (3)

| Symbol | Meaning |
| --- | --- |
| **Component:** DRIVE-CLiQ Hub Module (Hub) | **Propagation:** LOCAL |

  

**Reaction:**
  
Vector: OFF1 (OFF2)  
Chopper: NONE (OFF2)  
Infeed: OFF1 (OFF2)

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The DRIVE-CLiQ communication from the DRIVE-CLiQ component involved to the Control
Unit signals that the supply voltage has failed.  
Fault cause:  
9 (= 09 hex):  
The power supply voltage for the components has failed.  
Note regarding the message value:  
The individual information is coded as follows in the message value (r0949/r2124):  
0000yyxx hex: yy = component number, xx = error cause

**Remedy:**
  
- Carry out a POWER ON (switch-off/switch-on).  
- Check the supply voltage wiring of the DRIVE-CLiQ component (interrupted cable,
contacts, ...).  
- Check the dimensioning of the DRIVE-CLiQ component power supply.

### F40885 CX32 DRIVE-CLiQ (CU): Cyclic data transfer error

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** DRIVE-CLiQ Hub Module (Hub) | **Propagation:** LOCAL |

  

**Reaction:**
  
Vector: OFF2  
Chopper: NONE (OFF2)  
Infeed: OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A DRIVE-CLiQ communications error has occurred from the controller extension involved
to the Control Unit.  
The nodes do not send and receive in synchronism.  
Fault cause:  
26 (= 1A hex):  
Sign-of-life bit in the receive telegram not set and the receive telegram is too early.  
33 (= 21 hex):  
The cyclic telegram has not been received.  
34 (= 22 hex):  
Timeout in the telegram receive list.  
64 (= 40 hex):  
Timeout in the telegram send list.  
98 (= 62 hex):  
Error at the transition to cyclic operation.  
Note regarding the message value:  
The individual information is coded as follows in the message value (r0949/r2124):  
0000yyxx hex: yy = component number, xx = error cause

**Remedy:**
  
- Check the power supply voltage of the component involved.  
- Carry out a POWER ON (switch-off/switch-on).  
- Replace the component involved.

### F40886 CX32 DRIVE-CLiQ (CU): Error when sending DRIVE-CLiQ data

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** DRIVE-CLiQ Hub Module (Hub) | **Propagation:** LOCAL |

  

**Reaction:**
  
Vector: OFF2  
Chopper: NONE (OFF2)  
Infeed: OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A DRIVE-CLiQ communications error has occurred from the controller extension involved
to the Control Unit.  
Data were not able to be sent.  
Fault cause:  
65 (= 41 hex):  
Telegram type does not match send list.  
Note regarding the message value:  
The individual information is coded as follows in the message value (r0949/r2124):  
0000yyxx hex: yy = component number, xx = error cause

**Remedy:**
  
Carry out a POWER ON (switch-off/switch-on).

### F40887 CX32 DRIVE-CLiQ (CU): Component fault

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** DRIVE-CLiQ Hub Module (Hub) | **Propagation:** LOCAL |

  

**Reaction:**
  
Vector: OFF2  
Chopper: NONE (OFF2)  
Infeed: OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
Fault detected on the DRIVE-CLiQ component concerned. Faulty hardware cannot be excluded.  
Fault cause:  
32 (= 20 hex):  
Error in the telegram header.  
35 (= 23 hex):  
Receive error: The telegram buffer memory contains an error.  
66 (= 42 hex):  
Send error: The telegram buffer memory contains an error.  
67 (= 43 hex):  
Send error: The telegram buffer memory contains an error.  
96 (= 60 hex):  
Response received too late during runtime measurement.  
97 (= 61 hex):  
Time taken to exchange characteristic data too long.  
Note regarding the message value:  
The individual information is coded as follows in the message value (r0949/r2124):  
0000yyxx hex: yy = component number, xx = error cause

**Remedy:**
  
- Check the DRIVE-CLiQ wiring (interrupted cable, contacts, ...).  
- Check the electrical cabinet design and cable routing for EMC compliance.  
- If required, use another DRIVE-CLiQ socket (p9904).  
- Replace the component involved.

### F40895 CX32 DRIVE-CLiQ (CU): Cyclic data transfer error

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** DRIVE-CLiQ Hub Module (Hub) | **Propagation:** LOCAL |

  

**Reaction:**
  
Vector: OFF2  
Chopper: NONE (OFF2)  
Infeed: OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A DRIVE-CLiQ communications error has occurred from the controller extension involved
to the Control Unit.  
Fault cause:  
11 (= 0B hex):  
Synchronization error during alternating cyclic data transfer.  
Note regarding the message value:  
The individual information is coded as follows in the message value (r0949/r2124):  
0000yyxx hex: yy = component number, xx = error cause

**Remedy:**
  
Carry out a POWER ON (switch-off/switch-on).

### A49920 (F) Protective breaker, main circuit tripped

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, CU_MV_DP, CU_MV_PN, ENC, HUB, TB30, TECBASE, TM150,
TM15DI_DO, TM31, VECTOR3P, VECTORDM, VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
4.4

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
  
The protective breaker in the main circuit of the power supply has tripped.  
Note:  
This message is output via the signal source of binector input p6577[1] of the Control
Unit.  
See also: p6577

**Remedy:**
  
Check the main circuit.

Reaction upon F:  
Vector: OFF1 (NONE, OFF1_DELAYED, OFF2, OFF3)  
Chopper: OFF2 (NONE)  
Infeed: OFF1 (NONE, OFF1_DELAYED, OFF2)

Acknowl. upon F:  
IMMEDIATELY

### A49921 (F) Protective breaker redundant main circuit tripped

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, CU_MV_DP, CU_MV_PN, ENC, HUB, TB30, TECBASE, TM150,
TM15DI_DO, TM31, VECTOR3P, VECTORDM, VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
4.4

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
  
The protective breaker in the main circuit for the redundant feed to the power supply
has tripped.  
Note:  
This message is output via the signal source of binector input p6577[2] of the Control
Unit.  
See also: p6577

**Remedy:**
  
Check the redundant main circuit.

Reaction upon F:  
Vector: OFF1 (NONE, OFF1_DELAYED, OFF2, OFF3)  
Chopper: OFF2 (NONE)  
Infeed: OFF1 (NONE, OFF1_DELAYED, OFF2)

Acknowl. upon F:  
IMMEDIATELY

### A49922 (F) Protective breaker 24 V circuit has tripped

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, CU_MV_DP, CU_MV_PN, ENC, HUB, TB30, TECBASE, TM150,
TM15DI_DO, TM31, VECTOR3P, VECTORDM, VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
4.4

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
  
A protective breaker in the 24 V circuit has tripped.  
Note:  
This message is output via the signal source of binector input p6577[3] of the Control
Unit.  
See also: p6577

**Remedy:**
  
Check the 24 V circuit

Reaction upon F:  
Vector: OFF1 (NONE, OFF1_DELAYED, OFF2, OFF3)  
Chopper: NONE (OFF2)  
Infeed: OFF1 (NONE, OFF1_DELAYED, OFF2)

Acknowl. upon F:  
IMMEDIATELY

### A49923 (F) Protective breaker terminal strip 24 V circuit has tripped

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, CU_MV_DP, CU_MV_PN, ENC, HUB, TB30, TECBASE, TM150,
TM15DI_DO, TM31, VECTOR3P, VECTORDM, VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
4.4

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
  
A protective breaker for the terminal strip in the 24 V circuit has tripped.  
Note:  
This message is output via the signal source of binector input p6577[6] of the Control
Unit.  
See also: p6577

**Remedy:**
  
Check the terminal strip for the 24 V circuit.

Reaction upon F:  
Vector: OFF1 (NONE, OFF1_DELAYED, OFF2, OFF3)  
Chopper: OFF2 (NONE)  
Infeed: OFF1 (NONE, OFF1_DELAYED, OFF2)

Acknowl. upon F:  
IMMEDIATELY

### A49924 (F) Protective breaker power unit supply circuit tripped

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, CU_MV_DP, CU_MV_PN, ENC, HUB, TB30, TECBASE, TM150,
TM15DI_DO, TM31, VECTOR3P, VECTORDM, VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
4.4

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
  
A protective breaker in the circuit of the power unit supply has tripped.  
Note:  
This message is output via the signal source of binector input p6577[9] of the Control
Unit.  
See also: p6577

**Remedy:**
  
Check the power unit supply circuit.

Reaction upon F:  
Vector: OFF1 (NONE, OFF1_DELAYED, OFF2, OFF3)  
Chopper: OFF2 (NONE)  
Infeed: OFF1 (NONE, OFF1_DELAYED, OFF2)

Acknowl. upon F:  
IMMEDIATELY

### A49926 (F) Protective breaker synchronizing voltage tripped

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, CU_MV_DP, CU_MV_PN, ENC, HUB, TB30, TECBASE, TM150,
TM15DI_DO, TM31, VECTOR3P, VECTORDM, VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
4.4

**Message value:**
  
%1

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
  
A protective breaker for the synchronizing voltage has tripped.  
Note:  
This message is output via the signal source of binector input p6577[13] of the Control
Unit.  
See also: p6577

**Remedy:**
  
Check the synchronizing voltage.

Reaction upon F:  
Vector: OFF1 (NONE, OFF1_DELAYED, OFF2, OFF3)  
Chopper: OFF2 (NONE)  
Infeed: OFF1 (NONE, OFF1_DELAYED, OFF2)

Acknowl. upon F:  
IMMEDIATELY

### A49927 (F) Protective breaker auxiliary fan circuit has tripped

**Drive object:**
  
A_INFM2C, A_INFMV, B_INFMV, BMM2C, CU_MV_DP, CU_MV_PN, ENC, HUB, TB30, TECBASE, TM150,
TM15DI_DO, TM31, VECTOR3P, VECTORDM, VECTORM2C, VECTORMV, VECTORSL

**Valid as of version:**
  
4.4

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
  
The protective breaker in the fan circuit of the auxiliary fan has tripped.  
Note:  
This message is output via the signal source of binector input p6577[14] of the Control
Unit.  
See also: p6577

**Remedy:**
  
Check the auxiliary fan.

Reaction upon F:  
Vector: OFF1 (NONE, OFF1_DELAYED, OFF2, OFF3)  
Chopper: OFF2 (NONE)  
Infeed: OFF1 (NONE, OFF1_DELAYED, OFF2)

Acknowl. upon F:  
IMMEDIATELY

### A49933 (F) Protective breaker excitation 230 V AC circuit tripped

**Drive object:**
  
All objects

**Valid as of version:**
  
4.4

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
  
The protective breaker in the 230 V AC circuit of the excitation has tripped.  
Note:  
This message is output via the signal source of binector input p6577[17] of the Control
Unit.  
See also: p6577

**Remedy:**
  
Check the 230 V AC circuit of the excitation.

Reaction upon F:  
Vector: OFF1 (NONE, OFF1_DELAYED, OFF2, OFF3)  
Chopper: OFF2 (NONE)  
Infeed: OFF1 (NONE, OFF1_DELAYED, OFF2)

Acknowl. upon F:  
IMMEDIATELY

### A49934 (F) Protective breaker output cooling unit 230 V AC circuit tripped

**Drive object:**
  
All objects

**Valid as of version:**
  
4.4

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
  
The protective breaker in the 230 V AC circuit of the outgoing feeder of the cooling
unit has tripped.  
Note:  
This message is output via the signal source of binector input p6577[18] of the Control
Unit.  
See also: p6577

**Remedy:**
  
Check the 230 V AC circuit of the outgoing feeder of the cooling unit.

Reaction upon F:  
Vector: OFF1 (NONE, OFF1_DELAYED, OFF2, OFF3)  
Chopper: OFF2 (NONE)  
Infeed: OFF1 (NONE, OFF1_DELAYED, OFF2)

Acknowl. upon F:  
IMMEDIATELY

### A49935 (F) Protective breaker power unit door solenoids 24 V circuit has tripped

**Drive object:**
  
All objects

**Valid as of version:**
  
4.4

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
  
The protective breaker in the 24 V circuit of the door solenoids in the power unit
has tripped.  
Note:  
This message is output via the signal source of binector input p6577[19] of the Control
Unit.  
See also: p6577

**Remedy:**
  
Check the 24 V circuit of the door solenoids in the power unit.

Reaction upon F:  
Vector: OFF1 (NONE, OFF1_DELAYED, OFF2, OFF3)  
Chopper: OFF2 (NONE)  
Infeed: OFF1 (NONE, OFF1_DELAYED, OFF2)

Acknowl. upon F:  
IMMEDIATELY

### A49936 Protective breaker lighting supply/socket outlets 230V AC circuit has tripped

**Drive object:**
  
All objects

**Valid as of version:**
  
4.4

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
  
The protective breaker in the 230 V AC circuit for the lighting supply/socket outlets
has tripped.  
Note:  
This message is output via the signal source of binector input p6577[20] of the Control
Unit.  
See also: p6577

**Remedy:**
  
Check the 230V AC circuit for the lighting supply/socket outlets.

### A49937 (F) UPS not ready

**Drive object:**
  
All objects

**Valid as of version:**
  
4.4

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
  
The uninterruptible power supply (UPS) is not ready.  
Note:  
This message is output via the signal source of binector input p6577[25] of the Control
Unit.  
UPS: Uninterruptible Power Supply  
See also: p6577

**Remedy:**
  
Check the UPS.

Reaction upon F:  
Vector: OFF1 (NONE, OFF1_DELAYED, OFF2, OFF3)  
Chopper: OFF2 (NONE)  
Infeed: OFF1 (NONE, OFF1_DELAYED, OFF2)

Acknowl. upon F:  
IMMEDIATELY

### A49938 (F) UPS battery operation

**Drive object:**
  
All objects

**Valid as of version:**
  
4.4

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
  
The uninterruptible power supply (UPS) is in battery operation.  
Note:  
This message is output via the signal source of binector input p6577[26] of the Control
Unit.  
UPS: Uninterruptible Power Supply  
See also: p6577

**Remedy:**
  
Check the power supply of the control cabinet.

Reaction upon F:  
Vector: OFF1 (NONE, OFF1_DELAYED, OFF2, OFF3)  
Chopper: OFF2 (NONE)  
Infeed: OFF1 (NONE, OFF1_DELAYED, OFF2)

Acknowl. upon F:  
IMMEDIATELY

### A49939 (F) UPS battery discharged

**Drive object:**
  
All objects

**Valid as of version:**
  
4.4

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
  
The uninterruptible power supply (UPS) battery is discharged.  
Note:  
This message is output via the signal source of binector input p6577[27] of the Control
Unit.  
UPS: Uninterruptible Power Supply  
See also: p6577

**Remedy:**
  
Check the UPS battery.

Reaction upon F:  
Vector: OFF1 (NONE, OFF1_DELAYED, OFF2, OFF3)  
Chopper: OFF2 (NONE)  
Infeed: OFF1 (NONE, OFF1_DELAYED, OFF2)

Acknowl. upon F:  
IMMEDIATELY

### A49940 (F) Protective breaker tripped PU supply 400 V circuit

**Drive object:**
  
All objects

**Valid as of version:**
  
4.7

**Message value:**
  
-

**Message class:**
  
External measured value / signal state outside the permissible range (16)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** DRIVE |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The protective breaker for the 400 V AC supply of the power unit has tripped.  
Note:  
This message is output via the signal source of binector input p6577[28] of the Control
Unit.  
See also: p6577

**Remedy:**
  
Check the 400 V AC supply voltage for the power unit.

Reaction upon F:  
Vector: OFF1 (NONE, OFF1_DELAYED, OFF2, OFF3)  
Chopper: OFF2 (NONE)  
Infeed: OFF1 (NONE, OFF1_DELAYED, OFF2)

Acknowl. upon F:  
IMMEDIATELY

### A49941 (F) Protective breaker anti-condensation heating tripped

**Drive object:**
  
All objects

**Valid as of version:**
  
4.7

**Message value:**
  
-

**Message class:**
  
External measured value / signal state outside the permissible range (16)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** DRIVE |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The protective breaker for the anti-condensation heating was tripped.  
Note:  
This message is output via the signal source of binector input p6577[29] of the Control
Unit.  
See also: p6577

**Remedy:**
  
Check the anti-condensation heating circuit.

Reaction upon F:  
Vector: OFF1 (NONE, OFF1_DELAYED, OFF2, OFF3)  
Chopper: OFF2 (NONE)  
Infeed: OFF1 (NONE, OFF1_DELAYED, OFF2)

Acknowl. upon F:  
IMMEDIATELY

### A49942 (F) Protective breaker SITOP supply circuit tripped

**Drive object:**
  
All objects

**Valid as of version:**
  
4.7

**Message value:**
  
-

**Message class:**
  
External measured value / signal state outside the permissible range (16)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** DRIVE |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The protective breaker for the SITOP 24 V circuit has tripped.  
Note:  
This message is output via the signal source of binector input p6577[21] of the Control
Unit.  
See also: p6577

**Remedy:**
  
Check the SITOP power supply.

Reaction upon F:  
Vector: OFF1 (NONE, OFF1_DELAYED, OFF2, OFF3)  
Chopper: OFF2 (NONE)  
Infeed: OFF1 (NONE, OFF1_DELAYED, OFF2)

Acknowl. upon F:  
IMMEDIATELY

### F49955 Sign­of­life monitoring fault

**Drive object:**
  
All objects

**Valid as of version:**
  
4.8

**Message value:**
  
%1

**Message class:**
  
External measured value / signal state outside the permissible range (16)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
Vector: OFF2  
Chopper: NONE (OFF2)  
Infeed: OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The sign-of-life monitoring has detected a fault.  
Fault value (r0949, interpret decimal):  
Block number (instance):  
See also: p17983 (Sign-of-life monitoring mode), p17984 (Sign-of-life monitoring tolerance counter),
p17985 (Sign-of-life monitoring cycle), p17986 (Sign-of-life monitoring input), r17987
(Sign-of-life monitoring output)

**Remedy:**
  
- Observe bus propagation times – and when parameterizing, take into account the sign-of-life
monitoring.  
- Check the monitored connection for disturbances.

### A50001 (F) PN/COMM BOARD: Configuration error

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
CBE20:  
A PROFINET controller attempts to establish a connection using an incorrect configuring
telegram. The "Shared Device" function has been activated (p8829 = 2).  
Alarm value (r2124, interpret decimal):  
10: A CPU sends a PROFIsafe telegram.  
11: F CPU sends a PZD telegram.  
12: F CPU without an A CPU.  
13: F CPU with more PROFIsafe subslots than activated with p9601.3.  
14: F CPU with fewer PROFIsafe subslots than activated with p9601.3.  
15: PROFIsafe telegram of the F-CPU does not match the setting in p60022.

**Remedy:**
  
CBE20:  
Check the configuration of the PROFINET controllers as well as the p8829 and p9601.3
setting.

Reaction upon F:  
Vector: NONE (OFF1, OFF2, OFF3)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF1, OFF2)

Acknowl. upon F:  
IMMEDIATELY

### A50002 (F) COMM BOARD: Alarm 2

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
CBE20 SINAMICS Link:  
A specific telegram word (send) is being used twice.  
Alarm value (r2124, interpret decimal):  
Telegram word used twice  
See also: p8871 (SINAMICS Link PZD send word)

**Remedy:**
  
CBE20 SINAMICS Link:  
Correct the parameter assignment.  
See also: p8871 (SINAMICS Link PZD send word)

Reaction upon F:  
Vector: NONE (OFF1, OFF2, OFF3)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF1, OFF2)

Acknowl. upon F:  
IMMEDIATELY

### A50003 (F) COMM BOARD: Alarm 3

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Info. 1: %1, info. 2: %2

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
CBE20 SINAMICS Link:  
A specific telegram word (receive) is being used twice.  
Alarm value (r2124, interpret hexadecimal):  
yyyyxxxx hex: yyyy = info. 1, xxxx = info. 2  
Info. 1 (decimal) = Address of sender  
Info. 2 (decimal) = Receive telegram word  
See also: p8870 (SINAMICS Link PZD receive word), p8872 (SINAMICS Link PZD receive address)

**Remedy:**
  
CBE20 SINAMICS Link:  
Correct the parameter assignment.

Reaction upon F:  
Vector: NONE (OFF1, OFF2, OFF3)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF1, OFF2)

Acknowl. upon F:  
IMMEDIATELY

### A50004 (F) COMM BOARD: Alarm 4

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Info. 1: %1, info. 2: %2

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
CBE20 SINAMICS Link:  
- Telegram word (receive) and address of sender inconsistent. Both values have to
be either equal to zero or not equal to zero.  
- Address of the sender &gt; maximum project address.  
Alarm value (r2124, interpret hexadecimal):  
yyyyxxxx hex: yyyy = info. 1, xxxx = info. 2  
Info. 1 (decimal) = Drive object number from p8870, p8872  
Info. 2 (decimal) = Index from p8870, p8872  
See also: p8811, p8870, p8872

**Remedy:**
  
In the case of CBE20 SINAMICS Link:  
Correct the parameter assignment.

Reaction upon F:  
Vector: NONE (OFF1, OFF2, OFF3)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF1, OFF2)

Acknowl. upon F:  
IMMEDIATELY

### A50005 (F) COMM BOARD: Alarm 5

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
CBE20 SINAMICS Link:  
Sender not found on SINAMICS Link.  
Alarm value (r2124, interpret decimal):  
0: synchronization to the bus clock cycle unsuccessful.  
1 ... 64: address of the sender that was not found.  
See also: p8872 (SINAMICS Link PZD receive address)

**Remedy:**
  
CBE20 SINAMICS Link:  
Check the connection to the sender.  
Set parameters p8811, p8812[1] to identical values for all participants/nodes.  
Check parameter p8836 for all participants.  
See also: p8811 (SINAMICS Link project selection), p8812 (SINAMICS Link clock cycle settings),
p8836 (SINAMICS link node address)

Reaction upon F:  
Vector: NONE (OFF1, OFF2, OFF3)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF1, OFF2)

Acknowl. upon F:  
IMMEDIATELY

### A50006 (F) COMM BOARD: Alarm 6

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Info. 1: %1, info. 2: %2

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
CBE20 SINAMICS Link:  
The parameter assignment indicates that the sender and the receiver are one and the
same. This is not permitted.  
Alarm value (r2124, interpret hexadecimal):  
yyyyxxxx hex: yyyy = info. 1, xxxx = info. 2  
Info. 1 (decimal) = Drive object number from p8872  
Info. 2 (decimal) = Index from p8872  
See also: p8836 (SINAMICS link node address), p8872 (SINAMICS Link PZD receive address)

**Remedy:**
  
In the case of CBE20 SINAMICS Link:  
Correct the parameter assignment. All p8872[index] must be set to a value not equal
to p8836.

Reaction upon F:  
Vector: NONE (OFF1, OFF2, OFF3)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF1, OFF2)

Acknowl. upon F:  
IMMEDIATELY

### A50007 (F) COMM BOARD: Alarm 7

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Info. 1: %1, info. 2: %2

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
CBE20 SINAMICS Link:  
A send telegram word is greater than possible in the project.  
Alarm value (r2124, interpret hexadecimal):  
yyyyxxxx hex: yyyy = info. 1, xxxx = info. 2  
Info. 1 (decimal) = drive object number from p8871  
Info. 2 (decimal) = index from p8871  
See also: p8811 (SINAMICS Link project selection), p8871 (SINAMICS Link PZD send word)

**Remedy:**
  
In the case of CBE20 SINAMICS Link:  
Correct the parameter assignment.

Reaction upon F:  
Vector: NONE (OFF1, OFF2, OFF3)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF1, OFF2)

Acknowl. upon F:  
IMMEDIATELY

### A50008 (F) COMM BOARD: Alarm 8

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
Info. 1: %1, info. 2: %2

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
CBE20 SINAMICS Link:  
A receive telegram word is greater than possible in the project.  
Alarm value (r2124, interpret hexadecimal):  
yyyyxxxx hex: yyyy = info. 1, xxxx = info. 2  
Info. 1 (decimal) = drive object number from p8870  
Info. 2 (decimal) = index from p8870  
See also: p8811 (SINAMICS Link project selection), p8870 (SINAMICS Link PZD receive word)

**Remedy:**
  
In the case of CBE20 SINAMICS Link:  
Correct the parameter assignment.

Reaction upon F:  
Vector: NONE (OFF1, OFF2, OFF3)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF1, OFF2)

Acknowl. upon F:  
IMMEDIATELY

### A50009 (F) COMM BOARD: Alarm 9

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**

**Remedy:**

Reaction upon F:  
Vector: NONE (OFF1, OFF2, OFF3)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF1, OFF2)

Acknowl. upon F:  
IMMEDIATELY

### A50010 (F) PNCOMM BOARD: Consistency error affecting adjustable parameters

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
A consistency error was detected when activating the configuration (p8945) for the
Communication Board Ethernet 20 (CBE20).  
Alarm value (r2124, interpret decimal):  
0: General consistency error  
1: Error in the IP configuration (IP address, subnet mask or standard gateway).  
2: Error in the station names.  
3: DHCP was not able to be activated, as a cyclic PROFINET connection already exists.  
4: A cyclic PROFINET connection is not possible as DHCP is activated.  
Note:  
For all alarm values, the following applies: currently set configuration has not been
activated.  
DHCP: Dynamic Host Configuration Protocol  
See also: p8940 (CBExx name of station), p8941 (CBExx IP address), p8942 (CBExx default gateway),
p8943 (CBExx subnet mask), p8944 (CBExx DHCP mode)

**Remedy:**
  
- Check the required interface configuration (p8940 and following), correct if necessary,
and activate (p8945).  
or  
- Reinitialize the station using the "Edit Ethernet node" screen form (e.g. with STARTER
commissioning tool).  
See also: p8945 (CBExx activate configuration of interfaces)

Reaction upon F:  
Vector: NONE (OFF1, OFF2, OFF3)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF1, OFF2)

Acknowl. upon F:  
IMMEDIATELY

### A50011 (F) EtherNetIP/COMM BOARD: configuration error

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
CBE20 EtherNet/IP:  
An EtherNet/IP controller attempts to establish a connection using an incorrect configuring
telegram.  
The telegram length set in the controller does not match the parameterization in the
drive device.

**Remedy:**
  
Check the set telegram length.  
Note:  
PZD interface 1:  
For p0922 not equal to 999, then the length of the selected telegram applies.  
For p0922 = 999, the maximum interconnected PZD (r2067) applies.  
PZD interface 2:  
The maximum interconnected PZD (r8867) applies.  
See also: p0922, r2067, r8867

Reaction upon F:  
Vector: NONE (OFF1, OFF2, OFF3)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF1, OFF2)

Acknowl. upon F:  
IMMEDIATELY

### A50012 (F) COMM BOARD: Alarm 12

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**

**Remedy:**

Reaction upon F:  
Vector: NONE (OFF1, OFF2, OFF3)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF1, OFF2)

Acknowl. upon F:  
IMMEDIATELY

### A50013 (F) COMM BOARD: Alarm 13

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**

**Remedy:**

Reaction upon F:  
Vector: NONE (OFF1, OFF2, OFF3)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF1, OFF2)

Acknowl. upon F:  
IMMEDIATELY

### A50014 (F) COMM BOARD: Alarm 14

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**

**Remedy:**

Reaction upon F:  
Vector: NONE (OFF1, OFF2, OFF3)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF1, OFF2)

Acknowl. upon F:  
IMMEDIATELY

### A50015 (F) COMM BOARD: Alarm 15

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**

**Remedy:**

Reaction upon F:  
Vector: NONE (OFF1, OFF2, OFF3)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF1, OFF2)

Acknowl. upon F:  
IMMEDIATELY

### A50016 (F) COMM BOARD: Alarm 16

**Drive object:**
  
All objects

**Valid as of version:**
  
4.4

**Message value:**
  
%1

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**

**Remedy:**

Reaction upon F:  
Vector: NONE (OFF1, OFF2, OFF3)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF1, OFF2)

Acknowl. upon F:  
IMMEDIATELY

### A50017 (F) COMM BOARD: Alarm 17

**Drive object:**
  
All objects

**Valid as of version:**
  
4.4

**Message value:**
  
%1

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**

**Remedy:**

Reaction upon F:  
Vector: NONE (OFF1, OFF2, OFF3)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF1, OFF2)

Acknowl. upon F:  
IMMEDIATELY

### A50018 (F) COMM BOARD: Alarm 18

**Drive object:**
  
All objects

**Valid as of version:**
  
4.4

**Message value:**
  
%1

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**

**Remedy:**

Reaction upon F:  
Vector: NONE (OFF1, OFF2, OFF3)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF1, OFF2)

Acknowl. upon F:  
IMMEDIATELY

### A50019 (F) COMM BOARD: Alarm 19

**Drive object:**
  
All objects

**Valid as of version:**
  
4.4

**Message value:**
  
%1

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**

**Remedy:**

Reaction upon F:  
Vector: NONE (OFF1, OFF2, OFF3)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF1, OFF2)

Acknowl. upon F:  
IMMEDIATELY

### A50020 (F) PNCOMM BOARD: Second controller missing

**Drive object:**
  
All objects

**Valid as of version:**
  
4.4

**Message value:**
  
-

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
CBE20:  
The PROFINET function "Shared Device" has been activated (p8829 = 2). However, only
the connection to a PROFINET controller is present.

**Remedy:**
  
CBE20:  
Check the configuration of the PROFINET controllers as well as the p8829 setting.

Reaction upon F:  
Vector: NONE (OFF1, OFF2, OFF3)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF1, OFF2)

Acknowl. upon F:  
IMMEDIATELY

## SINAMICS Alarms TM31 (Terminal Module) 50201 - 51069

SINAMICS Alarms TM31 (Terminal Module) 50201 - 51069

### F50201 (A) COMM BOARD: Fault 1

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
Vector: OFF1 (OFF2, OFF3)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF1, OFF2)

**Acknowledge:**
  
IMMEDIATELY

**Cause:**

**Remedy:**

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

### F50202 (A) COMM BOARD: Fault 2

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
Vector: OFF1 (OFF2, OFF3)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF1, OFF2)

**Acknowledge:**
  
IMMEDIATELY

**Cause:**

**Remedy:**

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

### F50203 (A) COMM BOARD: Fault 3

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
Vector: OFF1 (OFF2, OFF3)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF1, OFF2)

**Acknowledge:**
  
IMMEDIATELY

**Cause:**

**Remedy:**

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

### F50204 (A) COMM BOARD: Fault 4

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
Vector: OFF1 (OFF2, OFF3)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF1, OFF2)

**Acknowledge:**
  
IMMEDIATELY

**Cause:**

**Remedy:**

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

### F50205 (A) COMM BOARD: Fault 5

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
Vector: OFF1 (OFF2, OFF3)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF1, OFF2)

**Acknowledge:**
  
IMMEDIATELY

**Cause:**

**Remedy:**

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

### F50206 (A) COMM BOARD: Fault 6

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
Vector: OFF1 (OFF2, OFF3)  
Chopper: NONE (OFF2)  
Infeed: OFF1 (OFF2)

**Acknowledge:**
  
IMMEDIATELY

**Cause:**

**Remedy:**

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

### F50207 (A) COMM BOARD: Fault 7

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
Vector: OFF1 (OFF2, OFF3)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF1, OFF2)

**Acknowledge:**
  
IMMEDIATELY

**Cause:**

**Remedy:**

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

### F50208 (A) COMM BOARD: Fault 8

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
Vector: OFF1 (OFF2, OFF3)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF1, OFF2)

**Acknowledge:**
  
IMMEDIATELY

**Cause:**

**Remedy:**

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

### F50209 (A) COMM BOARD: Fault 9

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
Vector: OFF1 (OFF2, OFF3)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF1, OFF2)

**Acknowledge:**
  
IMMEDIATELY

**Cause:**

**Remedy:**

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

### F50210 (A) COMM BOARD: Fault 10

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
Vector: OFF1 (OFF2, OFF3)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF1, OFF2)

**Acknowledge:**
  
IMMEDIATELY

**Cause:**

**Remedy:**

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

### F50211 (A) COMM BOARD: Fault 11

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
Vector: OFF1 (OFF2, OFF3)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF1, OFF2)

**Acknowledge:**
  
IMMEDIATELY

**Cause:**

**Remedy:**

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

### F50212 (A) COMM BOARD: Fault 12

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
Vector: OFF1 (OFF2, OFF3)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF1, OFF2)

**Acknowledge:**
  
IMMEDIATELY

**Cause:**

**Remedy:**

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

### F50213 (A) COMM BOARD: Fault 13

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
Vector: OFF1 (OFF2, OFF3)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF1, OFF2)

**Acknowledge:**
  
IMMEDIATELY

**Cause:**

**Remedy:**

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

### F50214 (A) COMM BOARD: Fault 14

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
Vector: OFF1 (OFF2, OFF3)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF1, OFF2)

**Acknowledge:**
  
IMMEDIATELY

**Cause:**

**Remedy:**

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

### F50215 (A) COMM BOARD: Fault 15

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
Vector: OFF1 (OFF2, OFF3)  
Chopper: NONE (OFF2)  
Infeed: NONE (OFF1, OFF2)

**Acknowledge:**
  
IMMEDIATELY

**Cause:**

**Remedy:**

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

### F50510 FBLOCKS: Logon of the runtime group rejected

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

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
  
IMMEDIATELY

**Cause:**
  
When the runtime groups of the free function blocks attempted to log on with the sampling
time management, the logon of at least one runtime group was rejected.  
Too many different hardware sampling times may have been assigned to the free function
blocks.  
See also: r20008 (Hardware sampling times available)

**Remedy:**
  
- check number of different hardware sampling times (r20008, r7903).  
- hardware sampling times are those sampling times that are formed as a multiple of
the basis hardware sampling times r20002 and are always &lt; r20003.  
- For internal purposes, the drive unit always requires at least two (or several,
depending on the parameterization of p0115 of the drive objects) free hardware sampling
times. Therefore, the current number of hardware sampling times that are still free
can be read out in r7903. If r7903=0, no additional sampling time that differs from
r20008[0...12] can be provided from the Control Unit. If, when selecting in this state,
a runtime group with a sampling time &lt; r20003 (p20000 &lt;= 255) is to be set in p20000,
only runtime groups whose sampling time is already provided in r20008[0...12] can
be selected.

### F50511 FBLOCKS: Memory no longer available for free function blocks

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

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
  
IMMEDIATELY

**Cause:**
  
When the free function blocks were activated, more memory was requested than was available
on the Control Unit.

**Remedy:**
  
Deactivate again the drive object on which the function module "free function blocks"
was last activated (p0108[0...15].18 = 0). Then carry out a POWER ON.  
Note:  
The assignment of drive object numbers to the index numbers of p0108[0...15] can be
read out in p0101[0...15]; the assignment to the drive object types can be read out
in p0107[0...15] on the drive object of the CU or CX (only with SM150).

### A50513 (F) FBLOCKS: Run sequence value already assigned

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

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
  
An attempt was made to assign a run sequence value already assigned to a function
block on this drive object to another additional function block on the same drive
object. A run sequence value can only be precisely assigned to one function block
on one drive object.

**Remedy:**
  
Set another value that is still available on this drive object for the run sequence.

Reaction upon F:  
 NONE

Acknowl. upon F:  
IMMEDIATELY

### A50514 FBLOCKS: Sampling time of fixed runtime group differs

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

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
  
The sampling time of a system function was set to a value (p0112, p0115) lower than
the smallest permissible sampling time that is allowed for the fixed runtime group
belonging to this system block (1 ms). The fixed runtime group involved is assigned
as a minimum to one block.

**Remedy:**
  
Using p0112 or p0115, increase the sampling time of the system function to the minimum
permissible sampling time for the runtime groups of 1 ms or change the sampling time
assignment of this runtime group in p20000[0...9].

### F50515 FBLOCKS: Data save unsuccessful after runtime measurement

**Drive object:**
  
All objects

**Valid as of version:**
  
4.5

**Message value:**
  
-

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The measurement data of the runtime measurement could not be saved to the non-volatile
memory.

**Remedy:**
  
Check whether there is still sufficient memory space in the non-volatile memory.

### F50516 FBLOCKS: Runtime group for runtime measurement not logged on

**Drive object:**
  
All objects

**Valid as of version:**
  
4.5

**Message value:**
  
-

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The runtime group to be measured is not logged on. A logged-on runtime group is required
for runtime measurement.

**Remedy:**
  
Log the runtime group on (p20020).  
See also: p20020 (Computing time measurement runtime group)

### A50517 FBLOCKS: Int. meas. active

**Drive object:**
  
All objects

**Valid as of version:**
  
4.5

**Message value:**
  
-

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
A Siemens internal measurement has been activated.

**Remedy:**
  
Carry out a POWER ON (switch-off/switch-on) for the Control Unit involved.

### F50518 FBLOCKS: Sampling time of free runtime group differs at download

**Drive object:**
  
All objects

**Valid as of version:**
  
4.5

**Message value:**
  
%1

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
In the STARTER/SCOUT project that was downloaded, the hardware sampling time of a
free runtime group (1 &lt;= p20000[i] &lt;= 256) was set to a value that was either too
low or too high.  
The sampling time must be between 1 ms and the value r20003 - r20002.  
If the sampling time of the selected free runtime group is &lt; 1 ms, the equivalent
value of 1 ms is used.  
If the value &gt;= r20003, then the sampling time is set to the next higher or the same
software sampling time &gt;= r21003.  
Fault value (r0949, interpret decimal):  
Number of the p20000 index of the runtime group where the sampling time is incorrectly
set.  
Number of the runtime group = fault value + 1  
Note:  
For SIMOTION D410, r20003 (unlike all the other Control Units) is automatically set
the same as the PROFIBUS sampling time.  
See also: r20008 (Hardware sampling times available)

**Remedy:**
  
- correctly set the sampling time of the runtime group.  
- if required, take all of the blocks from the runtime group.  
Note:  
Fault F50518 only detects an incorrectly parameterized runtime group. If, after correcting
p20000[i] in the project, this error occurs again at download, then the runtime group
involved should be identified using the fault value (r0949) and the sampling time
correctly set.

### F51000 DCC: Logon of the runtime group with sampling time management rejected

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

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
  
IMMEDIATELY

**Cause:**
  
For the sampling time management of the basic SINAMICS system, Drive Control Chart
(DCC) made an attempt to log on a sampling time that cannot be implemented. The logon
was rejected.  
STARTER:  
Fault value (r0949, decimal interpretation):  
Number of the p21000 index of the runtime group where the sampling time was incorrectly
set.  
Number of the runtime group = fault value  
StartDrive:  
Fault value (r0949, interpret decimal) indicates the position of the chart in the
chart sequence. Number of the fault value = position of the chart (numbering starts
with 1)

**Remedy:**
  
Attempt to assign this runtime group another fixed or free runtime group.  
The assignment is set in STARTER in the context menu of the DCC chart via sampling
times.  
Then compile the chart and download it again into the drive unit.

### F51001 DCC: No further hardware sampling times available

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The drive unit can no longer provide any additional hardware sampling times, whose
sampling time deviates from the sampling times.already logged on.  
STARTER:  
Fault value (r0949, decimal interpretation):  
Number of the p21000 index of the runtime group where the sampling time was incorrectly
set.  
Number of the runtime group = fault value  
StartDrive:  
Fault value (r0949, interpret decimal) indicates the position of the chart in the
chart sequence. Number of the fault value = position of the chart (numbering starts
with 1)

**Remedy:**
  
The fault can be immediately acknowledged, as the system runtime group 0 (corresponds
to "Do not calculate") was assigned in p21000[x]. In Startdrive it is p21100+5*(chart
ID-1). n= position of the chart in the chart sequence (first chart has position 1)  
Note:  
In window "Set runtime groups" in the context menu of the chart, p21000[0] (p21100
with Startdrive) is the topmost entry and p21000[9] is the lowest entry.  
The current assignment of hardware sampling times can be read-out in r21008.

### F51004 DCC: Sampling time of the free runtime group differs at download

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
In the STARTER/SCOUT project that was downloaded, the hardware sampling time of a
free runtime group (1 &lt;= p21000[i] or p21100+5*(n-1) with Startdrive &lt;= 256) was set
to a value that was either too low or too high. n= position of the chart in the chart
sequence (first chart has position 1). The sampling time must lie between 1 ms and
the value (r21003 - r21002).  
If the sampling time of the selected free runtime group is &lt; 1 ms, then the equivalent
value of 1 ms is used.  
If the value &gt;= r21003, then the sampling time is set to the next higher or the same
software sampling time &gt;= r21003. To prevent the fault, the determined software sampling
time can be set in the runtime group (1001 &lt;= p21000[i] &lt;= 1096 with STARTER or 1001
&lt;= p21100+5*(n-1) &lt;= 1096 with Startdrive).  
At least one block is assigned to the free runtime group involved.  
After correcting the selection in p21000[i] (p21100+5*(n-1) with Startdrive) in the
project, if this fault still occurs during download, please check which runtime group
is involved based on the fault value (r0949). Only one F51004 fault is signaled at
a time, even if several runtime groups have been incorrectly parameterized in p21000[]
(p21100+5*(n-1) with Startdrive).  
STARTER:  
Fault value (r0949, decimal interpretation):  
Number of the p21000 index of the runtime group where the sampling time was incorrectly
set.  
Number of the runtime group = fault value  
StartDrive:  
Fault value (r0949, interpret decimal) indicates the position of the chart in the
chart sequence. Number of the fault value = position of the chart (numbering starts
with 1)  
Note:  
With SIMOTION D410, r21003 (unlike all the other Control Units) is automatically set
the same as the PROFIBUS sampling time.

**Remedy:**
  
Correctly set the sampling time of the runtime group or remove all of the blocks from
the runtime group.

### F51005 DCC: Sampling time of the fixed runtime group differs online

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
Generally, the sampling times of the fixed runtime groups correspond to the sampling
times of the associated system function (e.g. the sampling time of the fixed runtime
group "BEFORE speed controller" generally corresponds to the sampling of the speed
controller p0115[1]).  
The sampling time of a system function online was set to a lower value (e.g. with
p0112, p0115, p0799, p4099) than the smallest permissible sampling time that is allowed
for the fixed runtime group belonging to this system function (1 ms). The sampling
time is set to 1 ms. At least one block is assigned to the fixed runtime group involved.  
STARTER:  
Fault value (r0949, decimal interpretation):  
Number of the p21000 index of the runtime group where the sampling time was incorrectly
set.  
Number of the runtime group = fault value  
StartDrive:  
Fault value (r0949, interpret decimal) indicates the position of the chart in the
chart sequence. Number of the fault value = position of the chart (numbering starts
with 1)

**Remedy:**
  
Using parameter p0112 or p0115, increase the sampling time of the system function
to the minimum permissible sampling time for the runtime groups of 1 ms or remove
all of the blocks from the runtime group.

### F51006 DCC: Sampling time of the fixed runtime group differs at download

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
Generally, the sampling times of the fixed runtime groups correspond to the sampling
times of the associated system function (e.g. the sampling time of the fixed runtime
group "BEFORE speed controller" generally corresponds to the sampling of the speed
controller p0115[1]).  
During a download, the sampling time of a system function was set to a lower value
(p0112, p0115) than the smallest permissible sampling time that is allowed for the
fixed runtime group belonging to this system function (1 ms). The sampling time is
set to the smallest possible value (r21002 on the drive object).  
STARTER:  
Fault value (r0949, decimal interpretation):  
Number of the p21000 index of the runtime group where the sampling time was incorrectly
set.  
Number of the runtime group = fault value  
StartDrive:  
Fault value (r0949, interpret decimal) indicates the position of the chart in the
chart sequence. Number of the fault value = position of the chart (numbering starts
with 1)

**Remedy:**
  
Using parameter p0112 or p0115, increase the sampling time of the system function
to the minimum permissible sampling time for the runtime groups of 1 ms or remove
all of the blocks from the runtime group.

### F51008 DCC: No NVRAM available

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The DCC project contains at least one block that requires remanent memory from the
basic SINAMICS system (e.g. SAV, SAV_BY, SAV_D, SAV_I). The request for remanent memory
was rejected by the basic SINAMICS system.  
Fault value (r0949, decimal interpretation):  
0: There is no more free remanent memory available on the drive unit.  
1: The EPROM data of the drive unit indicates that there is no remanent memory on
the module.

**Remedy:**
  
For fault value = 0:  
- Deactivate other applications on the drive unit that use remanent memory.  
- Do not use blocks that require remanent memory in your DCC charts.  
For fault value = 1:  
- For modules D425 or D435, use hardware version D or higher.  
Note:  
You can read out the hardware version using SCOUT in online mode under Target system
--&gt; Device diagnostics --&gt; tab "General" in the lower window, 3rd column in the line
of the CPU.

### F51009 DCC: Project data and block library are incompatible

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
-

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The block library and the saved or downloaded project data are incompatible.

**Remedy:**
  
Make sure that the block library and project data match.  
- Update the block library in SINAMICS by downloading the technology package.  
or  
- Update the project data in the DCC Editor by importing the correct block library.

### F51030 DCC: Data storage after runtime measurement unsuccessful

**Drive object:**
  
All objects

**Valid as of version:**
  
4.4

**Message value:**
  
-

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The propagation time measurement data could not be saved to the memory card.

**Remedy:**
  
Check whether there is still sufficient memory space on the memory card.

### F51031 DCC: Runtime group for computing time measurement not logged on

**Drive object:**
  
All objects

**Valid as of version:**
  
4.4

**Message value:**
  
-

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The runtime group to be measured is not logged on.  
Computing time measurement requires the relevant runtime group to be logged on.

**Remedy:**
  
Log on the runtime group to be measured (p21030).  
See also: p21030 (Runtime group, computing time measurement)

### A51032 DCC: Internal measurement active

**Drive object:**
  
All objects

**Valid as of version:**
  
4.4

**Message value:**
  
-

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
A Siemens internal measurement has been activated.

**Remedy:**
  
Carry out a POWER ON (switch off/on) for the Control Unit involved.

### F51033 Licensing DCC application not sufficient

**Drive object:**
  
All objects

**Valid as of version:**
  
4.6

**Message value:**
  
-

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
There is a license error in a DCB block.

**Remedy:**
  
-Obtain the necessary license.  
-Later licensing is not possible online via p9920, 9921.

### F51034 DCC: block runtimes are not measured

**Drive object:**
  
All objects

**Valid as of version:**
  
4.8

**Message value:**
  
-

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A block library created with DCB Studio contains blocks for which the runtime has
not been measured. Contact the person that created the library.

**Remedy:**

### F51035 DCC: DCC configuration error

**Drive object:**
  
All objects

**Valid as of version:**
  
4.8

**Message value:**
  
-

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
An error has occurred when powering up from a DCC configuration.

**Remedy:**
  
- Evaluate fault buffer (r0945).  
- Carry out a POWER ON for all components  
(switch off/switch on)  
- If required, check the data on the non-volatile memory (e.g. memory card).  
- Upgrade firmware to later version.  
- Contact the Hotline.

### F51036 (A) DCC: Error for online changes in the DCC chart

**Drive object:**
  
All objects

**Valid as of version:**
  
5.2

**Message value:**
  
%1

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
Infeed: OFF2 (NONE, OFF1, OFF1_DELAYED)  
Servo: OFF2 (ENCODER, IASC/DCBRK, NONE, OFF1, OFF1_DELAYED, OFF3, STOP2)  
Vector: OFF2 (ENCODER, IASC/DCBRK, NONE, OFF1, OFF1_DELAYED, OFF3, STOP2)  
Chopper: OFF2 (NONE)  
Hla: OFF2 (ENCODER, NONE, OFF1, OFF3, STOP2)

**Acknowledge:**
  
IMMEDIATELY (POWER ON)

**Cause:**
  
The changes in the DCC chart were not able to be undone.

**Remedy:**
  
- Restart the device and download the DCC configuration into the device.  
- Upgrade firmware to later version.  
- Contact the Hotline.

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

### F51037 (A) DCC: Alarm for online changes in the DCC chart

**Drive object:**
  
All objects

**Valid as of version:**
  
5.2

**Message value:**
  
%1

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
Infeed: NONE (OFF1, OFF1_DELAYED, OFF2)  
Servo: NONE (ENCODER, IASC/DCBRK, OFF1, OFF1_DELAYED, OFF2, OFF3, STOP2)  
Vector: NONE (ENCODER, IASC/DCBRK, OFF1, OFF1_DELAYED, OFF2, OFF3, STOP2)  
Chopper: NONE (OFF2)  
Hla: NONE (ENCODER, OFF1, OFF2, OFF3, STOP2)

**Acknowledge:**
  
IMMEDIATELY (POWER ON)

**Cause:**
  
The changes in the DCC chart were not able to be undone.

**Remedy:**
  
- Restart the device and download the DCC configuration into the device.  
- Upgrade firmware to later version.  
- Contact the Hotline.

Reaction upon A:  
 NONE

Acknowl. upon A:  
NONE

### A51038 DCC: Performance limits of online changes reached

**Drive object:**
  
All objects

**Valid as of version:**
  
5.2

**Message value:**
  
%1

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
Fault value (r2124, interpret decimal):  
0: Another fault has occurred.  
1: Too many online changes were requested. Saving such a project to the CF card slows
down the device restart, and it takes longer to execute online changes.

**Remedy:**
  
Load into the PC/PG and then load the DCC configuration into the device.

### F51050 DCC: Fault initiated by "Drive Control Chart"

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
Infeed: OFF2 (NONE, OFF1)  
Servo: OFF2 (ENCODER, IASC/DCBRK, NONE, OFF1, OFF3, STOP2)  
Vector: OFF2 (ENCODER, IASC/DCBRK, NONE, OFF1, OFF3, STOP2)  
Chopper: OFF2 (NONE)  
Hla: OFF2 (ENCODER, NONE, OFF1, OFF3, STOP2)

**Acknowledge:**
  
IMMEDIATELY (POWER ON)

**Cause:**
  
"Drive Control Chart" (DCC) had initiated this message via the block "Set Message"
(STM) or via a block (SINAMICS DCB Extension) generated using SINAMICS DCB Studio.  
Fault value (r0949, decimal interpretation):  
The configured message value is displayed in r0949.

**Remedy:**
  
This message was configured with "Drive Control Chart" (DCC).  
The cause and remedy depend on the project and should be described in the corresponding
project documentation.

### F51051 DCC: Fault initiated by "Drive Control Chart"

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
Infeed: OFF2 (NONE, OFF1)  
Servo: OFF2 (ENCODER, IASC/DCBRK, NONE, OFF1, OFF3, STOP2)  
Vector: OFF2 (ENCODER, IASC/DCBRK, NONE, OFF1, OFF3, STOP2)  
Chopper: OFF2 (NONE)  
Hla: OFF2 (ENCODER, NONE, OFF1, OFF3, STOP2)

**Acknowledge:**
  
IMMEDIATELY (POWER ON)

**Cause:**
  
"Drive Control Chart" (DCC) had initiated this message via the block "Set Message"
(STM) or via a block (SINAMICS DCB Extension) generated using SINAMICS DCB Studio.  
Fault value (r0949, decimal interpretation):  
The configured message value is displayed in r0949.

**Remedy:**
  
This message was configured with "Drive Control Chart" (DCC).  
The cause and remedy depend on the project and should be described in the corresponding
project documentation.

### F51052 DCC: Fault initiated by "Drive Control Chart"

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
Infeed: OFF2 (NONE, OFF1)  
Servo: OFF2 (ENCODER, IASC/DCBRK, NONE, OFF1, OFF3, STOP2)  
Vector: OFF2 (ENCODER, IASC/DCBRK, NONE, OFF1, OFF3, STOP2)  
Chopper: OFF2 (NONE)  
Hla: OFF2 (ENCODER, NONE, OFF1, OFF3, STOP2)

**Acknowledge:**
  
IMMEDIATELY (POWER ON)

**Cause:**
  
"Drive Control Chart" (DCC) had initiated this message via the block "Set Message"
(STM) or via a block (SINAMICS DCB Extension) generated using SINAMICS DCB Studio.  
Fault value (r0949, decimal interpretation):  
The configured message value is displayed in r0949.

**Remedy:**
  
This message was configured with "Drive Control Chart" (DCC).  
The cause and remedy depend on the project and should be described in the corresponding
project documentation.

### F51053 DCC: Fault initiated by "Drive Control Chart"

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
Infeed: OFF2 (NONE, OFF1)  
Servo: OFF2 (ENCODER, IASC/DCBRK, NONE, OFF1, OFF3, STOP2)  
Vector: OFF2 (ENCODER, IASC/DCBRK, NONE, OFF1, OFF3, STOP2)  
Chopper: OFF2 (NONE)  
Hla: OFF2 (ENCODER, NONE, OFF1, OFF3, STOP2)

**Acknowledge:**
  
IMMEDIATELY (POWER ON)

**Cause:**
  
"Drive Control Chart" (DCC) had initiated this message via the block "Set Message"
(STM) or via a block (SINAMICS DCB Extension) generated using SINAMICS DCB Studio.  
Fault value (r0949, decimal interpretation):  
The configured message value is displayed in r0949.

**Remedy:**
  
This message was configured with "Drive Control Chart" (DCC).  
The cause and remedy depend on the project and should be described in the corresponding
project documentation.

### F51054 DCC: Fault initiated by "Drive Control Chart"

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
Infeed: OFF2 (NONE, OFF1)  
Servo: OFF2 (ENCODER, IASC/DCBRK, NONE, OFF1, OFF3, STOP2)  
Vector: OFF2 (ENCODER, IASC/DCBRK, NONE, OFF1, OFF3, STOP2)  
Chopper: OFF2 (NONE)  
Hla: OFF2 (ENCODER, NONE, OFF1, OFF3, STOP2)

**Acknowledge:**
  
IMMEDIATELY (POWER ON)

**Cause:**
  
"Drive Control Chart" (DCC) had initiated this message via the block "Set Message"
(STM) or via a block (SINAMICS DCB Extension) generated using SINAMICS DCB Studio.  
Fault value (r0949, decimal interpretation):  
The configured message value is displayed in r0949.

**Remedy:**
  
This message was configured with "Drive Control Chart" (DCC).  
The cause and remedy depend on the project and should be described in the corresponding
project documentation.

### F51055 DCC: Fault initiated by "Drive Control Chart"

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
Infeed: OFF2 (NONE, OFF1)  
Servo: OFF2 (ENCODER, IASC/DCBRK, NONE, OFF1, OFF3, STOP2)  
Vector: OFF2 (ENCODER, IASC/DCBRK, NONE, OFF1, OFF3, STOP2)  
Chopper: OFF2 (NONE)  
Hla: OFF2 (ENCODER, NONE, OFF1, OFF3, STOP2)

**Acknowledge:**
  
IMMEDIATELY (POWER ON)

**Cause:**
  
"Drive Control Chart" (DCC) had initiated this message via the block "Set Message"
(STM) or via a block (SINAMICS DCB Extension) generated using SINAMICS DCB Studio.  
Fault value (r0949, decimal interpretation):  
The configured message value is displayed in r0949.

**Remedy:**
  
This message was configured with "Drive Control Chart" (DCC).  
The cause and remedy depend on the project and should be described in the corresponding
project documentation.

### F51056 DCC: Fault initiated by "Drive Control Chart"

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
Infeed: OFF2 (NONE, OFF1)  
Servo: OFF2 (ENCODER, IASC/DCBRK, NONE, OFF1, OFF3, STOP2)  
Vector: OFF2 (ENCODER, IASC/DCBRK, NONE, OFF1, OFF3, STOP2)  
Chopper: OFF2 (NONE)  
Hla: OFF2 (ENCODER, NONE, OFF1, OFF3, STOP2)

**Acknowledge:**
  
IMMEDIATELY (POWER ON)

**Cause:**
  
"Drive Control Chart" (DCC) had initiated this message via the block "Set Message"
(STM) or via a block (SINAMICS DCB Extension) generated using SINAMICS DCB Studio.  
Fault value (r0949, decimal interpretation):  
The configured message value is displayed in r0949.

**Remedy:**
  
This message was configured with "Drive Control Chart" (DCC).  
The cause and remedy depend on the project and should be described in the corresponding
project documentation.

### F51057 DCC: Fault initiated by "Drive Control Chart"

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
Infeed: OFF2 (NONE, OFF1)  
Servo: OFF2 (ENCODER, IASC/DCBRK, NONE, OFF1, OFF3, STOP2)  
Vector: OFF2 (ENCODER, IASC/DCBRK, NONE, OFF1, OFF3, STOP2)  
Chopper: OFF2 (NONE)  
Hla: OFF2 (ENCODER, NONE, OFF1, OFF3, STOP2)

**Acknowledge:**
  
IMMEDIATELY (POWER ON)

**Cause:**
  
"Drive Control Chart" (DCC) had initiated this message via the block "Set Message"
(STM) or via a block (SINAMICS DCB Extension) generated using SINAMICS DCB Studio.  
Fault value (r0949, decimal interpretation):  
The configured message value is displayed in r0949.

**Remedy:**
  
This message was configured with "Drive Control Chart" (DCC).  
The cause and remedy depend on the project and should be described in the corresponding
project documentation.

### F51058 DCC: Fault initiated by "Drive Control Chart"

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
Infeed: OFF2 (NONE, OFF1)  
Servo: OFF2 (ENCODER, IASC/DCBRK, NONE, OFF1, OFF3, STOP2)  
Vector: OFF2 (ENCODER, IASC/DCBRK, NONE, OFF1, OFF3, STOP2)  
Chopper: OFF2 (NONE)  
Hla: OFF2 (ENCODER, NONE, OFF1, OFF3, STOP2)

**Acknowledge:**
  
IMMEDIATELY (POWER ON)

**Cause:**
  
"Drive Control Chart" (DCC) had initiated this message via the block "Set Message"
(STM) or via a block (SINAMICS DCB Extension) generated using SINAMICS DCB Studio.  
Fault value (r0949, decimal interpretation):  
The configured message value is displayed in r0949.

**Remedy:**
  
This message was configured with "Drive Control Chart" (DCC).  
The cause and remedy depend on the project and should be described in the corresponding
project documentation.

### F51059 DCC: Fault initiated by "Drive Control Chart"

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

**Message class:**
  
General drive fault (19)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
Infeed: OFF2 (NONE, OFF1)  
Servo: OFF2 (ENCODER, IASC/DCBRK, NONE, OFF1, OFF3, STOP2)  
Vector: OFF2 (ENCODER, IASC/DCBRK, NONE, OFF1, OFF3, STOP2)  
Chopper: OFF2 (NONE)  
Hla: OFF2 (ENCODER, NONE, OFF1, OFF3, STOP2)

**Acknowledge:**
  
IMMEDIATELY (POWER ON)

**Cause:**
  
"Drive Control Chart" (DCC) had initiated this message via the block "Set Message"
(STM) or via a block (SINAMICS DCB Extension) generated using SINAMICS DCB Studio.  
Fault value (r0949, decimal interpretation):  
The configured message value is displayed in r0949.

**Remedy:**
  
This message was configured with "Drive Control Chart" (DCC).  
The cause and remedy depend on the project and should be described in the corresponding
project documentation.

### A51060 DCC: alarm initiated by "Drive Control Chart"

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

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
  
"Drive Control Chart" (DCC) had initiated this message via the block "Set Message"
(STM) or via a block (SINAMICS DCB Extension) generated using SINAMICS DCB Studio.  
Alarm value (r2124, interpret decimal):  
The configured message value is displayed in r2124.

**Remedy:**
  
This message was configured with "Drive Control Chart" (DCC).  
The cause and remedy depend on the project and should be described in the corresponding
project documentation.

### A51061 DCC: alarm initiated by "Drive Control Chart"

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

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
  
"Drive Control Chart" (DCC) had initiated this message via the block "Set Message"
(STM) or via a block (SINAMICS DCB Extension) generated using SINAMICS DCB Studio.  
Alarm value (r2124, interpret decimal):  
The configured message value is displayed in r2124.

**Remedy:**
  
This message was configured with "Drive Control Chart" (DCC).  
The cause and remedy depend on the project and should be described in the corresponding
project documentation.

### A51062 DCC: alarm initiated by "Drive Control Chart"

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

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
  
"Drive Control Chart" (DCC) had initiated this message via the block "Set Message"
(STM) or via a block (SINAMICS DCB Extension) generated using SINAMICS DCB Studio.  
Alarm value (r2124, interpret decimal):  
The configured message value is displayed in r2124.

**Remedy:**
  
This message was configured with "Drive Control Chart" (DCC).  
The cause and remedy depend on the project and should be described in the corresponding
project documentation.

### A51063 DCC: alarm initiated by "Drive Control Chart"

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

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
  
"Drive Control Chart" (DCC) had initiated this message via the block "Set Message"
(STM) or via a block (SINAMICS DCB Extension) generated using SINAMICS DCB Studio.  
Alarm value (r2124, interpret decimal):  
The configured message value is displayed in r2124.

**Remedy:**
  
This message was configured with "Drive Control Chart" (DCC).  
The cause and remedy depend on the project and should be described in the corresponding
project documentation.

### A51064 DCC: alarm initiated by "Drive Control Chart"

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

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
  
"Drive Control Chart" (DCC) had initiated this message via the block "Set Message"
(STM) or via a block (SINAMICS DCB Extension) generated using SINAMICS DCB Studio.  
Alarm value (r2124, interpret decimal):  
The configured message value is displayed in r2124.

**Remedy:**
  
This message was configured with "Drive Control Chart" (DCC).  
The cause and remedy depend on the project and should be described in the corresponding
project documentation.

### A51065 DCC: alarm initiated by "Drive Control Chart"

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

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
  
"Drive Control Chart" (DCC) had initiated this message via the block "Set Message"
(STM) or via a block (SINAMICS DCB Extension) generated using SINAMICS DCB Studio.  
Alarm value (r2124, interpret decimal):  
The configured message value is displayed in r2124.

**Remedy:**
  
This message was configured with "Drive Control Chart" (DCC).  
The cause and remedy depend on the project and should be described in the corresponding
project documentation.

### A51066 DCC: alarm initiated by "Drive Control Chart"

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

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
  
"Drive Control Chart" (DCC) had initiated this message via the block "Set Message"
(STM) or via a block (SINAMICS DCB Extension) generated using SINAMICS DCB Studio.  
Alarm value (r2124, interpret decimal):  
The configured message value is displayed in r2124.

**Remedy:**
  
This message was configured with "Drive Control Chart" (DCC).  
The cause and remedy depend on the project and should be described in the corresponding
project documentation.

### A51067 DCC: alarm initiated by "Drive Control Chart"

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

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
  
"Drive Control Chart" (DCC) had initiated this message via the block "Set Message"
(STM) or via a block (SINAMICS DCB Extension) generated using SINAMICS DCB Studio.  
Alarm value (r2124, interpret decimal):  
The configured message value is displayed in r2124.

**Remedy:**
  
This message was configured with "Drive Control Chart" (DCC).  
The cause and remedy depend on the project and should be described in the corresponding
project documentation.

### A51068 DCC: alarm initiated by "Drive Control Chart"

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

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
  
"Drive Control Chart" (DCC) had initiated this message via the block "Set Message"
(STM) or via a block (SINAMICS DCB Extension) generated using SINAMICS DCB Studio.  
Alarm value (r2124, interpret decimal):  
The configured message value is displayed in r2124.

**Remedy:**
  
This message was configured with "Drive Control Chart" (DCC).  
The cause and remedy depend on the project and should be described in the corresponding
project documentation.

### A51069 DCC: alarm initiated by "Drive Control Chart"

**Drive object:**
  
All objects

**Valid as of version:**
  
2.6

**Message value:**
  
%1

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
  
"Drive Control Chart" (DCC) had initiated this message via the block "Set Message"
(STM) or via a block (SINAMICS DCB Extension) generated using SINAMICS DCB Studio.  
Alarm value (r2124, interpret decimal):  
The configured message value is displayed in r2124.

**Remedy:**
  
This message was configured with "Drive Control Chart" (DCC).  
The cause and remedy depend on the project and should be described in the corresponding
project documentation.

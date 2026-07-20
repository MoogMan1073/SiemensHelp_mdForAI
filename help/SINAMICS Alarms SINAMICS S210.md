---
title: "SINAMICS Alarms SINAMICS S210"
package: sdral400enUS
topics: 296
source: Siemens TIA Portal Information System (offline help, en-US)
---


# SINAMICS Alarms SINAMICS S210

This section contains the alarm descriptions for the devices listed below. The alarm descriptions for the various devices can differ. If this is the case, then in the topic under "Drive object", the Control Unit is listed for which the description applies. In the table of contents, you will then see a separate entry for each alarm number. The following Control Units are taken into account in the online help:

- SINAMICS S210

## SINAMICS Alarms SINAMICS S210 01000 - 01716

SINAMICS Alarms SINAMICS S210 01000 - 01716

### F01000 Internal software error

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

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
  
- evaluate fault buffer (r0945).  
- carry out a POWER ON (switch-off/switch-on) for all components.  
- if required, check the data on the non-volatile memory (e.g. memory card).  
- upgrade firmware to later version.  
- contact Technical Support.  
- replace the Control Unit.

### F01001 FloatingPoint exception

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

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
  
An exception occurred for an operation with the FloatingPoint data type.  
The error can be caused by the basic system or a technology function.  
Fault value (r0949, interpret hexadecimal):  
Only for internal Siemens troubleshooting.

**Remedy:**
  
- carry out a POWER ON (switch-off/switch-on).  
- upgrade firmware to later version.  
- contact Technical Support.

### F01002 Internal software error

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

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
  
- carry out a POWER ON (switch-off/switch-on) for all components.  
- upgrade firmware to later version.  
- contact Technical Support.

### F01003 Acknowledgment delay when accessing the memory

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

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
  
- carry out a POWER ON (switch-off/switch-on) for all components.  
- contact Technical Support.

### N01004 Internal software error

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

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
  
- read out diagnostics parameter (r9999).  
- contact Technical Support.

### F01005 Firmware download for DRIVE-CLiQ component unsuccessful

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

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
  
- check the selected component number (p7828).  
- check the DRIVE-CLiQ wiring.  
- save suitable firmware file for download in the directory "/siemens/sinamics/code/sac/".  
- use a component with a suitable hardware version  
- after POWER ON has been carried out again for the DRIVE-CLiQ component, download
firmware again. Depending on p7826, the firmware will be automatically downloaded.

### A01006 Firmware update for DRIVE-CLiQ component required

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

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
- take the component number from the alarm value and enter into p7828.  
- start the firmware download with p7829 = 1.

### A01007 POWER ON for DRIVE-CLiQ component required

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

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

### A01009 CU: Control module overtemperature

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

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
  
- check the air intake for the Control Unit.  
- check the Control Unit fan.  
Note:  
The alarm is automatically withdrawn once the limit value has been fallen below.

### F01011 Download interrupted

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

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
  
- check the communication cable.  
- download the project again.  
- boot from previously saved files (switch-off/switch-on or p0976).  
- when loading into the file system (download from memory card), use the matching
version.

### F01012 Project conversion error

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
When converting the project of an older firmware version, an error occurred.  
Fault value (r0949, interpret decimal):  
Parameter number of the parameter causing the error.  
For fault value = 600, the following applies:  
The temperature evaluation is no longer assigned to the power unit but to the encoder
evaluation.  
Notice:  
Monitoring of the motor temperature is no longer ensured.

**Remedy:**
  
Check the parameter indicated in the fault value and correctly adjust it accordingly.  
For fault value = 600:  
Parameter p0600 must be set to the values 1, 2 or 3 in accordance with the assignment
of the internal encoder evaluation to the encoder interface.  
Value 1 means: The internal encoder evaluation is assigned to the encoder interface
1 via p0187.  
Value 2 means: The internal encoder evaluation is assigned to the encoder interface
2 via p0188.  
Value 3 means: The internal encoder evaluation is assigned to the encoder interface
3 via p0189.  
- if necessary, the internal encoder evaluation must be assigned to an encoder interface
via parameters p0187, p0188 or p0189 accordingly.  
- if necessary, upgrade the firmware to a later version.

### F01015 Internal software error

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

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
  
- carry out a POWER ON (switch-off/switch-on) for all components.  
- upgrade firmware to later version.  
- contact Technical Support.

### A01016 Firmware changed

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

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

### F01018 Booting has been interrupted several times

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
-

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
POWER ON

**Cause:**
  
Module booting was interrupted several times. As a consequence, the module boots with
the factory setting.  
Possible reasons for booting being interrupted:  
- power supply interrupted.  
- CPU crashed.  
- parameterization invalid.

**Remedy:**
  
- carry out a POWER ON (switch-off/switch-on). After switching on, the module reboots
from the valid parameterization (if available).  
- restore the valid parameterization.  
Examples:  
a) Carry out a first commissioning, save, carry out a POWER ON (switch-off/switch-on).  
b) Load another valid parameter backup (e.g. from the memory card), save, carry out
a POWER ON (switch-off/switch-on).  
Note:  
If the fault situation is repeated, then this fault is again output after several
interrupted boots.

### A01019 Writing to the removable data medium unsuccessful

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

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
  
S210

**Valid as of version:**
  
5.1

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

### F01023 Software timeout (internal)

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

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
  
- carry out a POWER ON (switch-off/switch-on) for all components.  
- upgrade firmware to later version.  
- contact Technical Support.

### F01030 Sign-of-life failure for master control

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
-

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 OFF3

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
For active PC master control, no sign-of-life was received within the monitoring time.  
The master control was returned to the active BICO interconnection.

**Remedy:**
  
Set the monitoring time higher at the PC or, if required, completely disable the monitoring
function.  
The monitoring time is set as follows using the commissioning tool:  
&lt;Drive&gt; -&gt; Commissioning -&gt; Control panel -&gt; Button "Fetch master control" -&gt; A window
is displayed to set the monitoring time in milliseconds.  
Notice:  
The monitoring time should be set as short as possible. A long monitoring time means
a late response when the communication fails!

### F01031 Sign-of-life failure for OFF in REMOTE

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
-

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 OFF3

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
With the "OFF in REMOTE" mode active, no sign-of-life was received within 3 seconds.

**Remedy:**
  
- check the data cable connection at the serial interface for the Control Unit (CU)
and operator panel.  
- check the data cable between the Control Unit and operator panel.

### F01033 Units changeover: Reference parameter value invalid

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

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
  
When changing over the units to the referred representation type, it is not permissible
for any of the required reference parameters to be equal to 0.0  
Fault value (r0949, parameter):  
Reference parameter whose value is 0.0.

**Remedy:**
  
Set the value of the reference parameter to a number different than 0.0.  
See also: r0304 (Rated motor voltage), r0305 (Rated motor current), p2000 (Reference speed),
p2003 (Reference torque)

### F01034 Units changeover: Calculation parameter values after reference value change unsuccessful

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

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
  
The change of a reference parameter meant that for an involved parameter the selected
value was not able to be re-calculated in the per unit representation. The change
was rejected and the original parameter value restored.  
Fault value (r0949, parameter):  
Parameter whose value was not able to be re-calculated.  
See also: r0304 (Rated motor voltage), r0305 (Rated motor current), p2000 (Reference speed),
p2003 (Reference torque)

**Remedy:**
  
- Select the value of the reference parameter such that the parameter involved can
be calculated in the per unit representation.  
- technology unit selection (p0595) before changing the reference parameter p0596,
set p0595 = 1.

### A01035 ACX: Parameter back-up file corrupted

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

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
  
When the Control Unit is booted, no complete data set was found from the parameter
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
See also: p0977 (Save all parameters)

**Remedy:**
  
- download the project again using the commissioning tool.  
- save all parameters (p0977 = 1 or "copy RAM to ROM").  
See also: p0977 (Save all parameters)

### F01036 ACX: Parameter back-up file missing

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

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

### F01039 ACX: Writing to the parameter back-up file was unsuccessful

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

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
  
Writing to at least one parameter back-up file PSxxxyyy.*** in the non-volatile memory
was unsuccessful.  
- in the directory /USER/SINAMICS/DATA/ at least one parameter back-up file PSxxxyyy.***
has the "read only" file attribute and cannot be overwritten.  
- there is not sufficient free memory space available.  
- the non-volatile memory is defective and cannot be written to.  
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
  
- check the file attribute of the files (PSxxxyyy.***, CAxxxyyy.***, CCxxxyyy.***)
and, if required, change from "read only" to "writeable".  
- check the free memory space in the non-volatile memory. Approx. 80 kbyte of free
memory space is required for every drive object in the system.  
- replace the memory card or Control Unit.

### F01040 Save parameter settings and carry out a POWER ON

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

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
reboot.

**Remedy:**
  
- save parameters (p0977).  
- carry out a POWER ON (switch-off/switch-on).  
Then:  
- upload the data to the converter (commissioning tool).

### F01041 Parameter save necessary

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

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
  
- save the parameters.  
- download the project again to the drive unit.  
- update the firmware  
- if required, replace the Control Unit and/or memory card.

### F01042 Parameter error during project download

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
Parameter: %1, index: %2, fault cause: %3

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
9: Descriptive data not available.  
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
  
- correct the parameterization in the commissioning tool and download the project
again.  
- enter the correct value in the specified parameter.  
- identify the parameter that restricts the limits of the specified parameter.

### F01043 Fatal error at project download

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
Fault cause: %1

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
20: The configuration is inconsistent.  
21: Error when accepting the download parameters.  
22: Software-internal download error.  
23: download not possible when know-how protection is activated.  
24: download not possible during a partial power up after inserting a component.  
25: The configuration is inconsistent. Know-how protection is either not activated
or only partially.  
Additional values:  
Only for internal Siemens troubleshooting.

**Remedy:**
  
- use the current version of the commissioning tool.  
- modify the offline project and carry out a new download (e.g. compare the number
of drive objects, motor, encoder, power unit in the offline project and at the drive).  
- change the drive state (is a drive rotating or is there a message/signal?).  
- Observe additional active messages/signals and remove their cause (e.g. correct
any incorrectly set parameters).  
- automatically calculate the control parameters (p0340). Then set p0010 = 0.  
- boot from previously saved files (switch-off/switch-on or p0976).  
- before a new download, restore the factory setting if the know-how protection was
not activated on all drive objects.

### F01044 CU: Descriptive data error

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

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
  
An error was detected when loading the descriptive data saved in the non-volatile
memory.

**Remedy:**
  
Replace the memory card or Control Unit.

### A01045 CU: Configuring data invalid

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

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
Alarm value (r2124, interpret hexadecimal):  
Only for internal Siemens troubleshooting.

**Remedy:**
  
- Restore the factory setting (p0976 = 1) and reload the project into the converter.  
Then save the parameterization using the "Copy RAM to ROM" or with p0977 = 1. This
overwrites the incorrect parameter files in the non-volatile memory – and this alarm
is withdrawn.

### A01049 CU: It is not possible to write to file

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

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
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
-

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
  
The memory card and the device type do not match (e.g. a memory card for SINAMICS
S is inserted in SINAMICS G).

**Remedy:**
  
- insert the matching memory card.  
- use the matching Control Unit or power unit.

### A01064 CU: Internal error (CRC)

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
-

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
  
A checksum error (CRC error) has occurred in the Control Unit program memory

**Remedy:**
  
- carry out a POWER ON (switch-off/switch-on) for all components.  
- upgrade firmware to later version.  
- contact Technical Support.

### A01069 Parameter backup and device incompatible

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

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
  
- insert a memory card with compatible parameter backup and carry out a POWER ON.  
- insert a memory card without parameter backup and carry out a POWER ON.  
- save the parameters (p0977 = 1).

### F01072 Memory card restored from the backup copy

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

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

### A01073 POWER ON required for backup copy on memory card

**Drive object:**
  
S210

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
  
The parameter assignment on the visible partition of the memory card has changed.  
In order that the backup copy on the memory card is updated on the non-visible partition,
it is necessary to carry out a POWER ON or hardware reset (p0972) of the Control Unit.  
Note:  
It is possible that a new POWER ON is requested via this alarm (e.g. after saving
with p0971 = 1).

**Remedy:**
  
- carry out a POWER ON (switch-off/switch-on) for the Control Unit.  
- carry out a hardware reset (RESET button, p0972).

### F01082 Parameter error when powering up from data backup

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
Parameter: %1, index: %2, fault cause: %3

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
9: Descriptive data not available.  
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
  
- correct the parameterization in the commissioning tool and download the project
again.  
- enter the correct value in the specified parameter.  
- identify the parameter that restricts the limits of the specified parameter.

### A01099 UTC synchronization tolerance violated

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

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

**Remedy:**
  
Select the synchronization intervals shorter so that the deviation between the time
of day master and drive system lies within the tolerance.  
Note:  
The deviation when synchronizing is shown in r3107.

### F01120 Terminal initialization has failed

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** BICO |

  

**Reaction:**
  
 OFF1

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
An internal software error occurred while the terminal functions were being initialized.  
Fault value (r0949, interpret hexadecimal):  
Only for internal Siemens troubleshooting.

**Remedy:**
  
- carry out a POWER ON (switch-off/switch-on) for all components.  
- upgrade firmware to later version.  
- contact Technical Support.  
- replace the Control Unit.

### F01122 Frequency at the measuring probe input too high

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
%1

**Message class:**
  
Application/technological function faulted (17)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** BICO |

  

**Reaction:**
  
 OFF1

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

### F01250 CU: CU-EEPROM incorrect read-only data

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

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
  
POWER ON

**Cause:**
  
Error when reading the read-only data of the EEPROM in the Control Unit.  
Fault value (r0949, interpret decimal):  
Only for internal Siemens troubleshooting.

**Remedy:**
  
- carry out a POWER ON (switch-off/switch-on).  
- replace the Control Unit.

### A01251 CU: CU-EEPROM incorrect read-write data

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

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
- carry out a POWER ON (switch-off/switch-on).  
- replace the Control Unit.  
For alarm value r2124 &gt;= 256, the following applies:  
- for the drive object with this alarm, clear the fault memory (p0952 = 0).  
- as an alternative, clear the fault memory of all drive objects (p2147 = 1).  
- replace the Control Unit.

### A01304 Firmware version of DRIVE-CLiQ component is not up-to-date

**Drive object:**
  
S210

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
  
The non-volatile memory has a more recent firmware version than the one in the connected
DRIVE-CLiQ component.  
Alarm value (r2124, interpret decimal):  
Component number of the DRIVE-CLiQ component involved.

**Remedy:**
  
Update the firmware (p7828, p7829 - or commissioning tool).

### A01306 Firmware of the DRIVE-CLiQ component being updated

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

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

### A01330 Topology: Commissioning not possible

**Drive object:**
  
S210

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
  
Unable to carry out commissioning. The actual topology does not fulfill the requirements.

**Remedy:**
  
- check the OCC cable between the converter and motor.  
- carry out a POWER ON (switch-off/switch-on).  
- Check that the connected hardware is supported.  
Note:  
OCC: One Cable Connection (one cable system)

### F01357 Topology: Two Control Units identified on the DRIVE-CLiQ line

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
component number: %1, connection number: %2

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
- remove the connection to the second Control Unit and restart.  
- for the S120M component DRIVE-CLiQ extension, interchange the hybrid cable (IN/OUT).  
When using OALINK:  
- remove the DRIVE-CLiQ connection and restart the systems.  
- install OALINK on both Control Units and activate.  
- Check the configuration of the DRIVE-CLiQ sockets in OALINK.

### A01489 Topology: motor with DRIVE-CLiQ not connected

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

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
- insert the components involved at the right connection (correct the actual topology).  
- adapt the project/parameterizing in the commissioning tool (correct the target topology).  
Check the hardware:  
- check the 24 V supply voltage.  
- check DRIVE-CLiQ cables for interruption and contact problems.  
- check that the component is working properly.  
Note:  
Under "Topology --&gt; Topology view" the commissioning tool where relevant offers improved
diagnostics capability (e.g. setpoint/actual value comparison).

### A01590 Drive: Motor maintenance interval expired

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

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

**Remedy:**
  
carry out service/maintenance and reset the service/maintenance interval (p0651).

### F01600 SI P1: STO initiated

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
%1

**Message class:**
  
Safety monitoring channel has identified an error (10)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The "Safety Integrated" function integrated in the drive has identified a fault in
monitoring channel 1, and has initiated STO.  
- forced checking procedure (test stop) of the safety switch-off signal path of monitoring
channel 1 unsuccessful.  
- subsequent response to fault F01611 (defect in a monitoring channel).  
Fault value (r0949, interpret decimal):  
0: Stop request from another monitoring channel.  
1005: STO active, although no STO is selected and no stop response with STO is active.  
1010: STO inactive, although STO is selected or a stop response with STO is active.  
9999: Subsequent response to fault F01611.

**Remedy:**
  
- select Safe Torque Off and deselect again.  
- replace drive.  
For fault value = 9999:  
- carry out diagnostics for fault F01611.  
Note:  
SI: Safety Integrated  
STO: Safe Torque Off

### F01611 SI P1: Defect in a monitoring channel

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
%1

**Message class:**
  
Safety monitoring channel has identified an error (10)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The "Safety Integrated" function integrated in the drive has identified a fault in
monitoring channel 1. As a result of this fault, after the parameterized transition
time has elapsed (p9658), fault F01600 is output.  
Fault value (r0949, interpret decimal):  
0: Stop request from another monitoring channel.  
1 ... 999:  
Number of the cross-compared data that resulted in this fault. This number is also
displayed in r9795.  
2: SI enable safety functions (p9601). Crosswise data comparison is only carried out
for the supported bits.  
3: SI SGE changeover discrepancy time (p9650).  
4: SI transition time from F01611 to STO (p9658).  
5: SI enable Safe Brake Control (p9602).  
6: SI Motion enable safety functions (p9501).  
7: SI delay time of STO for Safe Stop 1 (p9652).  
8: SI PROFIsafe address (p9610).  
9: SI debounce time for STO/SBC/SS1 (p9651).  
14: SI PROFIsafe telegram selection (p9611).  
15: SI PROFIsafe bus failure response (p9612).  
1000: Watchdog timer has expired.  
Within the time of approx. 5 x p9650, alternatively, the following was defined:  
- the signal at F-DI for STO/SS1 continually changes with time intervals less than
or equal to the discrepancy time (p9650).  
- via PROFIsafe, STO (also as subsequent response) was continually selected and deselected
with time intervals less than or equal to the discrepancy time (p9650).  
1001, 1002: Initialization error, change timer / check timer.  
1900: CRC error in the SAFETY sector.  
1901: CRC error in the ITCM sector.  
1902: Overloading in the ITCM sector has occurred in operation.  
1903: Internal parameterizing error for CRC calculation.  
2000: Status of the STO selection for both monitoring channels different.  
2001: Feedback signal of STO shutdown for both monitoring channels different. This
value can also subsequently occur as a result of other faults.  
2002: Status of the delay timer SS1 on both monitoring channels are different (status
of the timer in p9650).  
2003: Status of the STO terminal for both monitoring channels different.  
6000 ... 6999:  
Error in the PROFIsafe control.  
For these fault values, the failsafe control signals (Failsafe Values) are transferred
to the safety functions. For p9612 = 1, the transfer of Failsafe Values is delayed.  
6000: A fatal PROFIsafe communication error has occurred.  
6064 ... 6071: error when evaluating the F parameter. The values of the transferred
F parameters do not match the expected values in the PROFIsafe driver.  
6064: Destination address and PROFIsafe address are different (F_Dest_Add).  
6065: Destination address not valid (F_Dest_Add).  
6066: Source address not valid (F_Source_Add).  
6067: Watchdog time not valid (F_WD_Time).  
6068: Incorrect SIL level (F_SIL).  
6069: Incorrect F-CRC length (F_CRC_Length).  
6070: Incorrect F parameter version (F_Par_Version).  
6071: CRC error for the F parameters (CRC1). The transferred CRC value of the F parameters
does not match the value calculated in the PROFIsafe driver.  
6072: F parameterization is inconsistent.  
6165: A communications error was identified when receiving the PROFIsafe telegram.
The fault can also occur if an inconsistent or out-of-date PROFIsafe telegram has
been received after switching the drive off and on or after plugging in the PROFINET
cable.  
6166: A time monitoring error (timeout) was identified when receiving the PROFIsafe
telegram.

**Remedy:**
  
For fault value = 1 ... 5 and 7 ... 999:  
- check the data that caused the fault.  
- carry out a POWER ON (switch-off/switch-on) for all components.  
- upgrade the drive software.  
For fault value = 6:  
- carry out a POWER ON (switch-off/switch-on) for all components.  
- upgrade the drive software.  
For fault value = 1000:  
Check the wiring of the F-DI for STO/SS1 (contact problems).  
- PROFIsafe: Resolve contact problems/faults at the PROFINET controller.  
- check the discrepancy time, and if required, increase the value (p9650).  
For fault value = 1001, 1002:  
- carry out a POWER ON (switch-off/switch-on) for all components.  
- upgrade the drive software.  
For fault value = 1900, 1901, 1902:  
- carry out a POWER ON (switch-off/switch-on) for all components.  
- replace drive.  
- upgrade the drive software.  
For fault value = 2000, 2001, 2002, 2003:  
- check the discrepancy time, and if required, increase the value (p9650, p9652).  
- check the wiring of the safety-relevant inputs (SGE) (contact problems).  
- replace drive.  
- diagnose the other active faults and resolve the causes.  
Note:  
This fault can be acknowledged after removing the cause of the error and after correct
selection/deselection of STO.  
For fault value = 6000:  
- carry out a POWER ON (switch-off/switch-on) for all components.  
- check whether there is a DRIVE-CLiQ communication error between the two monitoring
channels and, if required, carry out a diagnostics routine for the faults identified.  
- upgrade firmware to later version.  
- contact Technical Support.  
- replace drive.  
For fault value = 6064:  
- check the setting of the value in the F parameter F_Dest_Add at the PROFIsafe slave.  
- check the setting of the PROFIsafe address (p9610). Using the commissioning tool,
copy the safety parameters and confirm the data change.  
For fault value = 6065:  
- check the setting of the value in the F parameter F_Dest_Add at the PROFIsafe slave.
It is not permissible for the destination address to be either 0 or FFFF!  
For fault value = 6066:  
- check the setting of the value in the F parameter F_Source_Add at the PROFIsafe
slave. It is not permissible for the source address to be either 0 or FFFF!  
For fault value = 6067:  
- check the setting of the value in the F parameter F_WD_Time at the PROFIsafe slave.
It is not permissible for the watch time to be 0!  
For fault value = 6068:  
- check the setting of the value in the F parameter F_SIL at the PROFIsafe slave.
The SIL level must correspond to SIL2!  
For fault value = 6069:  
- check the setting of the value in the F parameter F_CRC_Length at the PROFIsafe
slave. The setting of the CRC2 length is 2-byte CRC in the V1 mode and 3-byte CRC
in the V2 mode!  
For fault value = 6070:  
- check the setting of the value in the F parameter F_Par_Version at the PROFIsafe
slave. The value for the F parameter version is 0 in the V1 mode and 1 in the V2 mode!  
For fault value = 6071:  
- check the settings of the values of the F parameters and the F parameter CRC (CRC1)
calculated from these at the PROFIsafe slave and, if required, update.  
For fault value = 6072:  
- check the settings of the values for the F parameters and, if required, correct.  
The following combinations are permissible for F parameters F_CRC_Length and F_Par_Version:  
F_CRC_Length = 2-byte CRC and F_Par_Version = 0  
F_CRC_Length = 3-byte CRC and F_Par_Version = 1  
For fault value = 6165:  
- if the fault occurs after powering up or after inserting the PROFINET cable, acknowledge
the fault.  
- check the configuration and communication at the PROFIsafe slave.  
- check the setting of the value for F parameter F_WD_Time on the PROFIsafe slave
and increase if necessary.  
- check whether there is a DRIVE-CLiQ communication error between the two monitoring
channels and, if required, carry out a diagnostics routine for the faults identified.  
- check whether all F parameters of the drive match the F parameters of the F host.  
For fault value = 6166:  
- check the configuration and communication at the PROFIsafe slave.  
- check the setting of the value for F parameter F_WD_Time on the PROFIsafe slave
and increase if necessary.  
- evaluate diagnostic information in the F host.  
- check PROFIsafe connection.  
- check whether all F parameters of the drive match the F parameters of the F host.  
Note:  
F-DI: Failsafe Digital Input  
SGE: Safety-relevant input  
SI: Safety Integrated  
SS1: Safe Stop 1  
STO: Safe Torque Off

### N01620 SI P1: Safe Torque Off active

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
-

**Message class:**
  
Safety monitoring channel has identified an error (10)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The "Safe Torque Off" (STO) function of the basic functions has been selected in monitoring
channel 1 using the input terminal and is active.  
Note:  
- this message does not result in a safety stop response.  
- this message is not output when STO is selected using the Extended Functions.

**Remedy:**
  
Not necessary.  
Note:  
SI: Safety Integrated  
STO: Safe Torque Off

### N01621 SI P1: Safe Stop 1 active

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
-

**Message class:**
  
Safety monitoring channel has identified an error (10)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The "Safe Stop 1" function (SS1) was selected in monitoring channel 1 and is active.  
Note:  
This message does not result in a safety stop response.

**Remedy:**
  
Not necessary.  
Note:  
SI: Safety Integrated  
SS1: Safe Stop 1

### F01625 SI P1: sign-of-life error in the safety data

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
%1

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The "Safety Integrated" function integrated in the drive has identified an error in
the sign-of-life of the safety data in monitoring channel 1, and has initiated STO.  
- there is either a DRIVE-CLiQ communication error or communication has failed.  
- a time slice overflow of the safety software has occurred.  
Fault value (r0949, interpret decimal):  
Only for internal Siemens troubleshooting.

**Remedy:**
  
- select STO and then deselect again.  
- carry out a POWER ON (switch-off/switch-on).  
- check whether there is a DRIVE-CLiQ communication error between the two monitoring
channels and, if required, carry out a diagnostics routine for the faults identified.  
- deselect all drive functions that are not absolutely necessary.  
- check the electrical cabinet design and cable routing for EMC compliance  
Note:  
SI: Safety Integrated  
STO: Safe Torque Off

### F01630 SI P1: Brake control error

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
%1

**Message class:**
  
Safety monitoring channel has identified an error (10)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The "Safety Integrated" function integrated in the drive has identified a brake control
fault in monitoring channel 1, and has initiated STO.  
- OCC cable shield is not correctly connected.  
- defect in the brake control circuit of the drive.  
Fault value (r0949, interpret decimal):  
10, 11:  
Fault in "open brake" operation.  
- brake not closed or interrupted cable.  
- ground fault in brake cable.  
20:  
Fault in "brake open" state.  
- short-circuit in brake winding.  
30, 31:  
Fault in "close brake" operation.  
- brake not closed or interrupted cable.  
- short-circuit in brake winding.  
40:  
Fault in "brake closed" state.  
50:  
Fault in the brake control of the drive or a communication error (brake control diagnostics).

**Remedy:**
  
- select STO and then deselect again.  
- check the motor holding brake connection.  
- check the function of the motor holding brake.  
- carry out a diagnostics routine for the faults involved.  
- check for EMC-compliant control cabinet design and cable routing (e.g. shield OCC
cable with shield terminal and shield plate, check the connection of the brake conductors).  
- replace drive.  
Note:  
OCC: One Cable Connection (one cable system)  
SBC: Safe Brake Control  
SI: Safety Integrated  
STO: Safe Torque Off  
See also: p1215 (Motor holding brake configuration)

### A01631 SI P1: motor holding brake/SBC configuration not practical

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

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
  
A configuration of motor holding brake and SBC was detected that is not practical.  
The following configurations can result in this message:  
- "No motor holding brake available" (p1215 = 0) and "SBC" enabled (p9602 = 1).

**Remedy:**
  
Check the parameterization of the motor holding brake and SBC and correct.  
Note:  
SBC: Safe Brake Control  
See also: p1215 (Motor holding brake configuration), p9602 (SI enable safe brake control)

### A01637 SI: Safety password not assigned

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

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
  
Safety Integrated is parameterized and enabled. However, a valid safety password has
still not been entered.  
See also: r9767 (SI Safety password status)

**Remedy:**
  
- assign a valid safety password.  
- carry out data save.

### A01638 SI: Safety password entered

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

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
  
A valid safety password has been entered. It is possible to change safety parameters
in the safety commissioning mode.  
See also: r9767 (SI Safety password status)

**Remedy:**
  
Not necessary.  
This alarm is automatically withdrawn with "Delete password" (e.g. after exiting the
web server - or after a Power on). The password remains assigned.

### F01640 SI P1: component exchange identified and acknowledge/save necessary

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
Fault cause: %1

|  |  |  |  |
| --- | --- | --- | --- |
|  | Bit | Cause: | Remedy: |
| %1 | 0 | It has been identified that the Control Unit has been replaced |  |
| 1 | It has been identified that the Motor Module/Hydraulic Module has been replaced. |  |  |
| 2 | It has been identified that the Power Module has been replaced. |  |  |
| 3 | It has been identified that the Sensor Module channel 1 has been replaced. |  |  |
| 4 | It has been identified that the Sensor Module channel 2 has been replaced. |  |  |
| 5 | It has been identified that the sensor channel 1 has been replaced. |  |  |
| 6 | It has been identified that the sensor channel 2 has been replaced. |  |  |

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
  
"Safety Integrated" has identified that a component has been replaced.  
It is no longer possible to operate the particular drive without fault.  
When safety functions are active, after a component has been replaced it is necessary
to carry out a partial acceptance test.  
Fault value (r0949, interpret binary):  
Bit 0 = 1:  
It has been identified that the drive has been replaced.  
Bit 3 = 1:  
It has been identified that the Sensor Module has been replaced.  
Bit 5 = 1:  
It has been identified that the sensor has been replaced.

**Remedy:**
  
- acknowledge component replacement (p9702 = 29).  
- back up all parameters.  
- acknowledge fault.  
Note:  
In addition to the fault, diagnostics bits r9776.2 and r9776.3 are set.  
See also: r9776 (SI diagnostics)

### F01641 SI P1: component exchange identified and save necessary

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
Fault cause: %1

|  |  |  |  |
| --- | --- | --- | --- |
|  | Bit | Cause: | Remedy: |
| %1 | 0 | It has been identified that the Control Unit has been replaced |  |
| 1 | It has been identified that the Motor Module/Hydraulic Module has been replaced. |  |  |
| 2 | It has been identified that the Power Module has been replaced. |  |  |
| 3 | It has been identified that the Sensor Module channel 1 has been replaced. |  |  |
| 4 | It has been identified that the Sensor Module channel 2 has been replaced. |  |  |
| 5 | It has been identified that the sensor channel 1 has been replaced. |  |  |
| 6 | It has been identified that the sensor channel 2 has been replaced. |  |  |

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
  
"Safety Integrated" has identified that a component has been replaced.  
No additional fault response is initiated, therefore operation of the particular drive
is not restricted.  
When safety functions are active, after a component has been replaced it is necessary
to carry out a partial acceptance test.  
Fault value (r0949, interpret binary):  
Bit 0 = 1:  
It has been identified that the drive has been replaced.  
Bit 3 = 1:  
It has been identified that the Sensor Module has been replaced.  
Bit 5 = 1:  
It has been identified that the sensor has been replaced.

**Remedy:**
  
- save all parameters  
- acknowledge fault.  
See also: r9776 (SI diagnostics)

### F01649 SI P1: Internal software error

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

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
  
An internal error in the Safety Integrated software in monitoring channel 1 has occurred.  
Note:  
This fault results in an STO that cannot be acknowledged.  
Fault value (r0949, interpret hexadecimal):  
Only for internal Siemens troubleshooting.

**Remedy:**
  
- carry out a POWER ON (switch-off/switch-on).  
- re-commission the "Safety Integrated" function and carry out a POWER ON.  
- upgrade the drive firmware to a later version.  
- contact Technical Support.  
- replace drive.  
Note:  
SI: Safety Integrated  
STO: Safe Torque Off

### F01650 SI P1: Acceptance test required

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
%1

**Message class:**
  
Safety monitoring channel has identified an error (10)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** LOCAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The "Safety Integrated" function on monitoring channel 1 requires an acceptance test.  
Note:  
This fault results in an STO that can be acknowledged.  
Fault value (r0949, interpret decimal):  
130: Safety parameters for monitoring channel 2 not available.  
Note:  
This fault value is always output when Safety Integrated is commissioned for the first
time.  
1000: Reference and actual checksum in monitoring channel 1 are not identical (booting).  
- safety parameters set offline and loaded to the drive.  
- at least one checksum-checked piece of data is defective.  
2000: Reference and actual checksum in monitoring channel 1 are not identical (commissioning
mode).  
2001: Reference and actual checksum in monitoring channel 2 are not identical (commissioning
mode).  
2002: Enable of safety-related functions between the two monitoring channels differ.  
2003: Acceptance test is required as a safety parameter has been changed.  
2004: An acceptance test is required because a project with enabled safety-functions
has been downloaded.  
2005: The safety logbook has identified that the safety checksums have changed.  
2010: Safe brake control enable different between both monitoring channels.  
2020: Error when saving the safety parameters for the monitoring channel 2.  
3003: Acceptance test is required as a hardware-related safety parameter has been
changed.  
3005: The Safety logbook has identified that a hardware-related safety checksum has
changed.  
9999: Subsequent response of another safety-related fault that occurred when booting
that requires an acceptance test.

**Remedy:**
  
For fault value = 130:  
- carry out safety commissioning routine.  
For fault value = 1000:  
- again carry out safety commissioning routine.  
- replace the memory card or drive.  
For fault value = 2000:  
- confirm the data change using the commissioning tool.  
For fault value = 2001:  
- confirm the data change using the commissioning tool.  
For fault value = 2002:  
- using the commissioning tool, copy the safety parameters and confirm the data change.  
For fault value = 2003, 2004, 2005:  
- carry out an acceptance test and generate an acceptance report.  
Note:  
The fault with fault value 2005 can only be acknowledged when the "STO" function is
deselected.  
For fault value = 2010:  
- check that safe brake control is enabled.  
- using the commissioning tool, copy the safety parameters and confirm the data change.  
For fault value = 2020:  
- again carry out safety commissioning routine.  
- replace the memory card or drive.  
For fault value = 3003:  
- carry out the function checks for the modified hardware and generate an acceptance
report.  
For fault value = 3005:  
- carry out the function checks for the modified hardware and generate an acceptance
report.  
Note:  
The fault with fault value 3005 can only be acknowledged when the "STO" function is
deselected.  
For fault value = 9999:  
- carry out diagnostics for the other safety-related fault that is present.  
Note:  
SI: Safety Integrated  
STO: Safe Torque Off

### F01651 SI P1: Synchronization safety time slices unsuccessful

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The "Safety Integrated" function requires a synchronization of the safety time slices
between the two monitoring channels and between the drive and the higher-level control.
This synchronization routine was unsuccessful.  
Note:  
This fault results in an STO that cannot be acknowledged.

**Remedy:**
  
- carry out a POWER ON (switch-off/switch-on).  
- upgrade the drive software.  
- upgrade the software of the higher-level control.  
Note:  
SI: Safety Integrated  
STO: Safe Torque Off

### F01653 SI P1: PROFINET configuration error

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

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
  
There is a PROFINET configuration error for using Safety Integrated monitoring functions
with a higher-level control (F-PLC).  
Note:  
When the safety functions are enabled, this fault results in an STO that cannot be
acknowledged.  
Fault value (r0949, interpret decimal):  
200: A safety slot for receive data from the control has not been configured.  
210, 220: The configured safety slot for the receive data from the control has an
unknown format.  
230: The configured safety slot for the receive data from the F-PLC has the incorrect
length.  
231: The configured safety slot for the receive data from the F-PLC has the incorrect
length.  
250: A PROFIsafe slot is configured in the higher-level F control, however PROFIsafe
is not enabled in the drive.  
300: A safety slot for the send data to the control has not been configured.  
310, 320: The configured safety slot for the send data to the control has an unknown
format.  
330: The configured safety slot for the send data to the F-PLC has the incorrect length.  
331: The configured safety slot for the send data to the F-PLC has the incorrect length.  
400: The telegram number in the F-PLC does not match the parameterization in the drive.

**Remedy:**
  
The following generally applies:  
- check and, if necessary, correct the PROFINET configuration of the safety slot on
the master side.  
- upgrade the drive software.  
For fault value = 250:  
- remove the PROFIsafe configuring in the higher-level F control or enable PROFIsafe
in the drive.  
For fault value = 231, 331:  
- in the drive, parameterize the appropriate PROFIsafe telegram (p9611) to be set
on the F-PLC.  
- configure the PROFIsafe telegram matching the parameterization (p9611) in the F-PLC.  
Note:  
SI: Safety Integrated  
STO: Safe Torque Off

### A01654 SI P1: Deviating PROFIsafe configuration

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

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
  
The configuration of a PROFIsafe telegram in the higher-level control (F-PLC) does
not match the parameterization in the drive.  
Note:  
This message does not result in a safety stop response.  
Alarm value (r2124, interpret decimal):  
1:  
A PROFIsafe telegram is configured in the higher-level control, however PROFIsafe
is not enabled in the drive (p9601.3).  
2:  
PROFIsafe is parameterized in the drive; however, a PROFIsafe telegram has not been
configured in the higher-level control.

**Remedy:**
  
The following generally applies:  
- check and, if necessary, correct the PROFIsafe configuration in the higher-level
control.  
For alarm value = 1:  
- remove the PROFIsafe configuring in the higher-level F control or enable PROFIsafe
in the drive.  
For alarm value = 2:  
- configure the PROFIsafe telegram to match the parameterization in the higher-level
F-control.

### F01655 SI P1: Align monitoring functions

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
%1

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
  
An error has occurred when aligning the Safety Integrated monitoring functions of
both monitoring channels. No common set of supported SI monitoring functions was able
to be determined.  
- there is either a DRIVE-CLiQ communication error or communication has failed.  
- no POWER ON after upgrading the firmware.  
Note:  
This fault results in an STO that cannot be acknowledged.  
Fault value (r0949, interpret hexadecimal):  
Only for internal Siemens troubleshooting.

**Remedy:**
  
- carry out a POWER ON (switch-off/switch-on) for all components.  
- check the electrical cabinet design and cable routing for EMC compliance  
- upgrade the drive software.  
Note:  
SI: Safety Integrated  
STO: Safe Torque Off

### F01656 SI P1: Parameters monitoring channel 2 error

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
When accessing the Safety Integrated parameters for monitoring channel 2 in the non-volatile
memory, an error has occurred.  
Note:  
This fault results in an STO that can be acknowledged.  
Fault value (r0949, interpret decimal):  
129:  
- safety parameters for monitoring channel 2 corrupted.  
- drive with enabled safety functions was possibly copied offline using the commissioning
tool and the project downloaded.  
131: Internal software error on monitoring channel 2.  
132: Communication errors when uploading or downloading the safety parameters for
monitoring channel 2.  
255: Internal software error on monitoring channel 1.

**Remedy:**
  
- re-commission the safety functions.  
- upgrade the drive software.  
- replace the memory card or drive.  
For fault value = 129:  
- activate the safety commissioning mode (p0010 = 95).  
- adapt the PROFIsafe address (p9610).  
- using the commissioning tool, copy the safety parameters and confirm the data change.  
- exit the safety commissioning mode (p0010 = 0).  
- save all parameters (copy RAM to ROM).  
- carry out a POWER ON (switch-off/switch-on).  
For fault value = 132:  
- check the electrical cabinet design and cable routing for EMC compliance  
Note:  
SI: Safety Integrated  
STO: Safe Torque Off

### F01657 SI P1: PROFIsafe telegram number not valid

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

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
  
The PROFIsafe telegram number set in p9611 is not valid.  
When PROFIsafe is enabled (p9601.3 = 1), then a telegram number greater than zero
must be entered in p9611.  
Note:  
This fault does not result in a safety stop response.  
See also: p9611 (SI PROFIsafe telegram selection), r60022 (PROFIsafe telegram selection)

**Remedy:**
  
Check the telegram number setting (p9611).

### F01658 SI P1: PROFIsafe telegram numbers differ

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

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
  
IMMEDIATELY

**Cause:**
  
The PROFIsafe telegram number is set differently in p9611 and r60022.  
The telegram number must be identically set in both parameters.  
Note:  
This fault does not result in a safety stop response.  
See also: p9611 (SI PROFIsafe telegram selection), r60022 (PROFIsafe telegram selection)

**Remedy:**
  
Align the telegram number in both parameters so that they are the same (p9611, r60022).

### F01659 SI P1: Write request for parameter rejected

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
%1

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
  
The write request for one or several Safety Integrated parameters from monitoring
channel 1 was rejected.  
Note:  
This fault does not result in a safety stop response.  
Fault value (r0949, interpret decimal):  
1: The Safety Integrated password is not set.  
14: An attempt was made to enable the PROFIsafe communication - although the version
of the PROFIsafe driver used on both monitoring channels is different.  
20: An attempt was made to enable the motion monitoring functions integrated in the
drive and the STO function, both controlled via F-DI.  
25: An attempt was made to parameterize a PROFIsafe telegram although this cannot
be supported.  
27: An attempt was made to activate the Basic Functions by controlling via TM54F although
this is not supported.  
28: An attempt was made to enable the "STO via terminals at the Power Module" function
although this cannot be supported.  
9612: An attempt was made to set the stop response SS1 for PROFIsafe failure (p9612
= 1), although PROFIsafe is not enabled.

**Remedy:**
  
For fault value = 1:  
- set the Safety Integrated password.  
For fault value = 14, 27:  
- check whether there are faults in the safety function alignment between the two
monitoring channels (F01655, F30655) and if required, carry out diagnostics for the
faults involved.  
- upgrade the drive software.  
For fault value = 20:  
- correct the enable setting (p9601).  
For fault value = 25:  
- correct the telegram number setting (p9611).  
For fault value = 28:  
- correct the enable setting (p9601.7 = 0).  
For fault value = 9612:  
- establish communications with PROFIsafe (p9601).  
- parameterize STO as stop response for PROFIsafe failure (p9612 = 0).  
Note:  
F-DI: Failsafe Digital Input  
SBC: Safe Brake Control  
SI: Safety Integrated  
SS1: Safe Stop 1  
STO: Safe Torque Off  
See also: p9501 (SI Motion enable safety functions), p9601 (SI enable, functions integrated
in the drive), p9612 (SI PROFIsafe failure response)

### F01663 SI P1: copying SI parameters rejected

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** DRIVE |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The copy function for Safety Integrated parameters is initiated using the commissioning
tool.  
This is the reason that when booting, an attempt is made to copy Safety Integrated
parameters from monitoring channel 1 to monitoring channel 2. However, no safety-relevant
function has been selected in monitoring channel 1 (p9501 = 0, p9601 = 0). Copying
was rejected for safety reasons.  
As a consequence, inconsistent parameterization can occur in both monitoring channels,
which in turn results in additional error messages.  
Especially for inconsistent enabling of the safety functions on both monitoring channels,
fault F30625 is output.  
Note:  
This fault does not result in a safety stop response.  
SI: Safety Integrated

**Remedy:**
  
- check p9501 and p9601 and if required, correct.  
- perform copy function using the commissioning tool.  
- save all parameters or "Copy RAM to ROM".  
- carry out a POWER ON (switch-off/switch-on).

### F01670 SI Motion: Invalid parameterization of the encoder evaluation

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
%1

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
  
The parameterization of the encoder evaluation used for Safety Integrated is not permissible.  
Note:  
This fault results in an STO that cannot be acknowledged.  
Fault value (r0949, interpret decimal):  
1: No encoder was parameterized for Safety Integrated.  
2: An encoder was parameterized for Safety Integrated that does not have an A/B track
(sine/cosine).  
3: The encoder data set selected for Safety Integrated is still not valid.  
4: A communication error with the encoder has occurred.  
5: Number of relevant bits in the encoder coarse position invalid.  
6: DRIVE-CLiQ encoder configuration invalid.  
8: Parameterized Safety comparison algorithm not supported.

**Remedy:**
  
For fault value = 1, 2:  
- use and parameterize an encoder that Safety Integrated supports (encoder with track
A/B sine-wave, p0404.4 = 1).  
For fault value = 3:  
- check whether the drive or drive commissioning function is active and if required,
exit this (p0009 = p00010 = 0), save the parameters (p0971 = 1) and carry out a POWER
ON  
For fault value = 4:  
- check whether there are any active faults in the DRIVE-CLiQ communication between
the drive and the encoder evaluation - and when necessary, carry out diagnostics for
the faults involved.  
For fault value = 5:  
- p9525 = 0 (not permissible). Check the encoder parameterization.  
For fault value = 6:  
- check p9515.0 (for DRIVE-CLiQ encoders, the following applies: p9515.0 = 1). Check
the encoder parameterization.  
For fault value = 8:  
- use and parameterize an encoder that implements an algorithm supported by Safety
Integrated.  
Note:  
SI: Safety Integrated  
STO: Safe Torque Off

### F01671 SI Motion: Parameterization encoder error

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
%1

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
  
The parameterization of the encoder used by Safety Integrated is different to the
parameterization of the standard encoder.  
Note:  
This fault does not result in a safety stop response.  
Fault value (r0949, interpret decimal):  
Parameter number of the non-corresponding safety parameter.

**Remedy:**
  
Align the encoder parameterization between the safety encoder and the standard encoder.  
Note:  
SI: Safety Integrated

### F01672 SI P1: drive is incompatible regarding software/hardware

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** Power Module | **Propagation:** GLOBAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The software for monitoring channel 2 does not support safe motion monitoring, is
not compatible to the software for monitoring channel 1 - or there is a communications
error between the two monitoring channels.  
Note:  
This fault results in an STO that cannot be acknowledged.  
Fault value (r0949, interpret decimal):  
Only for internal Siemens troubleshooting.

**Remedy:**
  
- check whether faults F01655/F30655 are active - and when necessary, carry out diagnostics
for the faults involved.  
- upgrade the drive software.  
Note:  
SI: Safety Integrated  
STO: Safe Torque Off

### F01673 SI Motion: Sensor Module software/hardware incompatible

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
%1

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
  
The existing Sensor Module software and/or hardware does not support the safe motion
monitoring function with the higher-level control.  
Note:  
This fault does not result in a safety stop response.  
Fault value (r0949, interpret decimal):  
Only for internal Siemens troubleshooting.

**Remedy:**
  
- upgrade the Sensor Module software.  
- use a Sensor Module that supports the safe motion monitoring function.  
Note:  
SI: Safety Integrated

### F01674 SI Motion P1: Safety function not supported by PROFIsafe telegram

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
%1

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
  
The monitoring function enabled in p9501 and p9601 is not supported by the currently
set PROFIsafe telegram (p9611).  
Note:  
This fault results in an STO that cannot be acknowledged.  
Fault value (r0949, interpret bitwise):  
Bit 18 = 1:  
SS2E via PROFIsafe is not supported (p9501.18).  
Bit 24 = 1:  
Transfer SLS (SG) limit value via PROFIsafe not supported (p9501.24).  
Bit 25 = 1:  
Transfer safe position (SP) via PROFIsafe is not supported (p9501.25).  
Bit 26 = 1:  
Gearbox stage switchover via PROFIsafe is not supported (p9501.26).  
Bit 28 = 1:  
SCA via PROFIsafe is not supported (p9501.28).

**Remedy:**
  
- Deselect the monitoring function involved (p9501, p9601).  
- set the matching PROFIsafe telegram (p9611).  
Note:  
SCA: Safe Cam  
SI: Safety Integrated  
SLS: Safely-Limited Speed  
SP: Safe Position  
SS2E: Safe Stop 2 External (Safe Stop 2 with external stop)  
STO: Safe Torque Off

### F01675 SI Motion P1: settings in the PROFINET controller not permissible

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
%1

**Message class:**
  
Safety monitoring channel has identified an error (10)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** GLOBAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
For the "Safe synchronous position via PROFIsafe" function, an incorrect configuration
setting was identified.  
Note:  
This fault results in an STO that can be acknowledged as follows.  
- select STO and then deselect again.  
- internal event acknowledge (if the "Extended message acknowledgment" is active,
p9507.0 = 1).  
Fault value (r0949, interpret decimal):  
1:  
"Synchronous safe position via PROFIsafe" is enabled (p9501.29 = 1) and is not set
according to the rule Tdp = 2 x n x p9500 (n = 1, 2, 3, ...).  
2:  
"Synchronous safe position via PROFIsafe" is enabled (p9501.29 = 1) and isochronous
operation is not set.  
Note:  
SI: Safety Integrated  
STO: Safe Torque Off

**Remedy:**
  
For fault value = 1:  
- set bus cycle time Tdp and monitoring clock cycle p9500 according to the rule Tdp
= 2 x n x p9500 (n = 1, 2, 3, ...).  
For fault value = 2:  
- set "Isochronous mode" on the PROFINET controller.

### F01679 SI P1: Safety parameter settings and topology changed, warm restart/POWER ON required

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

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
  
Safety parameters have been changed; these will only take effect following a warm
restart or POWER ON (see alarm A01693).  
A partial power up (boot) with modified configuration was then performed.

**Remedy:**
  
- carry out a warm restart.  
- carry out a POWER ON (switch-off/switch-on).

### F01680 SI Motion P1: Checksum error safety monitoring functions

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
%1

**Message class:**
  
Safety monitoring channel has identified an error (10)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** GLOBAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The calculated actual checksum over the safety-relevant parameters does not match
the reference checksum saved at the last machine acceptance.  
Safety-relevant parameters have been changed or a fault is present.  
Note:  
This fault results in an STO that can be acknowledged.  
Fault value (r0949, interpret decimal):  
0: Checksum error for SI parameters for motion monitoring.  
1: Checksum error for SI parameters for actual values.  
2: Checksum error for SI parameters for component assignment.

**Remedy:**
  
- check the safety-relevant parameters and if required, correct.  
- execute the function "Copy RAM to ROM".  
- if necessary carry out a POWER ON (switch-off/switch-on).  
- carry out an acceptance test.  
Note:  
STO: Safe Torque Off

### F01681 SI Motion P1: Incorrect parameter value

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
Parameter: %1, supplementary information: %2

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
  
The parameter cannot be parameterized with this value.  
Note:  
This message does not result in a safety stop response.  
Fault value (r0949, interpret decimal):  
yyyyxxxx dec: yyyy = supplementary information, xxxx = parameter  
yyyy = 0:  
No additional information available.  
xxxx = 9501:  
Enabling function "SSM" (p9501.16) is not permissible in combination with the "Extended
functions without selection" function (p9601.5).  
xxxx = 9501 and yyyy = 10:  
Referencing via SCC (p9501.27 = 1) and epos (r0108.4 = 1) are simultaneously enabled.  
xxxx = 9506 and yyyy = 1:  
Parameter p9506 differs between the monitoring channels  
xxxx = 9522:  
The gear stage was set too high.  
xxxx = 9547:  
The hysteresis tolerance is not permissible.  
xxxx = 9578:  
SLA is enabled (p9501.20 = 1). Acceleration limit is too low (p9578). The acceleration
resolution is no longer sufficient (r9790).  
xxxx = 9601 and yyyy = 1:  
If motion monitoring functions integrated in the drive (p9601.2 = 1) and extended
functions without selection (p9601.5 = 1) are enabled, then PROFIsafe (p9601.3 = 1)
or onboard F-DI (p9601.4 = 1) is not possible.  
xxxx = 9601 and yyyy = 2:  
Extended functions without selection (p9601.5 =1) are enabled without enabling motion
monitoring functions integrated in the drive (p9601.2).  
xxxx = 9601 and yyyy = 3:  
Onboard F-DI are enabled without enabling motion monitoring functions integrated in
the drive (p9601.2).  
xxxx = 9601 and yyyy = 4:  
Onboard F-DI are enabled. Then, it is not permissible to simultaneously set PROFIsafe
and F-DI via PROFIsafe (p9501.30).  
xxxx = 9601 and yyyy = 5:  
Transfer of the SLS limit value via PROFIsafe (p9501.24) has been enabled, without
enabling PROFIsafe.  
xxxx = 9601 and yyyy = 6:  
Transfer of the safe position via PROFIsafe (p9501.25) has been enabled, without enabling
PROFIsafe.  
xxxx = 9601 and yyyy = 7:  
Safe switchover of the gearbox stages (p9501.26) has been enabled without enabling
PROFIsafe.  
xxxx = 9601 and yyyy = 11:  
SS2E (p9501.18 = 1) is enabled without PROFIsafe being enabled.  
xxxx = 9601 and yyyy = 12:  
SCA (p9501.28 = 1) is enabled without enabling PROFIsafe.  
xxxx = 9601 and yyyy = 13:  
Extended functions (p9601.2 = 1) have been enabled without enabling PROFIsafe (p9601.3).

**Remedy:**
  
Correct parameters:  
If xxxx = 9501:  
- deselect extended functions without selection (p9601.5).  
If xxxx = 9501 and yyyy = 10:  
Deselect referencing via SCC (p9501.27).  
For xxxx = 9501 and yyyy = 11:  
Deselect SS2E (p9501.18) - or enable PROFIsafe  
For xxxx = 9501 and yyyy = 12:  
Deselect SCA (p9501.28).  
For xxxx = 9507:  
Set synchronous motor.  
For xxxx = 9506:  
Using the commissioning tool, copy the safety parameters, confirm the data change,
backup the parameters and carry out a power on.  
For xxxx = 9522:  
Correct the corresponding parameter.  
For xxxx = 9547:  
With hysteresis/filtering enabled (p9501.16 = 1), the following applies:  
- set parameters p9546 and p9547 according to the following rule: p9547 &lt;= 0.75 x
p9546;  
- the following rule must also be adhered to when actual value synchronization (p9501.3
= 1) is enabled: p9547 &gt;= p9549;  
For xxxx = 9578:  
Increase the acceleration limit (p9578).  
- The minimum limit is 10x the acceleration resolution (r9790[1]).  
- observe the information in r9790.  
If xxxx = 9601:  
yyyy = 1:  
Only enable motion monitoring functions integrated in the drive (p9601.2 = 1) and
PROFIsafe (p9601.3 = 1).  
yyyy = 2:  
Deselect Extended Functions without selection (p9601.5 = 0)  
yyyy = 3:  
Deselect F-DI (p9601.4)  
yyyy = 4:  
Deselect onboard F-DI (p9601.4) and F-DI via PROFIsafe (p9501.30).  
yyyy = 5:  
To transfer the SLS limit values via PROFIsafe (p9501.24 = 1), also enable PROFIsafe
(p9601.3 =1) and motion monitoring functions integrated in the drive (p9601.2 = 1).  
yyyy = 6:  
Deselect the transfer of the safe position via PROFIsafe (p9501.25 = 0)  
yyyy = 7:  
Deselect the safe switchover of gearbox stages (p9501.26 = 1)  
yyyy = 13:  
Also enable PROFIsafe (p9601.3) for the extended functions (p9601.2)  
Note:  
SSM: Safe Speed Monitor (safety-relevant feedback signal from the speed monitoring)

### F01682 SI Motion P1: Monitoring function not supported

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
%1

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
  
The monitoring function enabled in p9501, p9506, p9507, p9601 is not supported in
this firmware version.  
Note:  
This fault results in an STO that cannot be acknowledged.  
Fault value (r0949, interpret decimal):  
20: Motion monitoring functions integrated in the drive are only supported in conjunction
with PROFIsafe (p9501 and p9601.1 ... 2).  
21: Enable a safe motion monitoring function (in p9501), not supported for enabled
basic functions via PROFIsafe (p9601.2 = 0, p9601.3 = 1).  
59: Safe actual value sensing with SIL3 encoder not supported.  
9612: An attempt was made to set the stop response SS1 for PROFIsafe failure (p9612
= 1), although PROFIsafe is not enabled.  
Additional fault values:  
Monitoring function not supported.  
See also: p9612 (SI PROFIsafe failure response)

**Remedy:**
  
- deselect the monitoring function involved (p9501, p9506, p9507, p9601).  
- restore the factory setting and repeat commissioning.  
- upgrade the firmware.  
For fault value = 59:  
- upgrade the firmware of the Motor Module to a later version.  
For fault value = 9612:  
- establish communications with PROFIsafe (p9601).  
- parameterize STO as stop response for PROFIsafe failure (p9612 = 0).  
Note:  
SI: Safety Integrated  
SS1: Safe Stop 1  
STO: Safe Torque Off  
See also: p9501 (SI Motion enable safety functions), p9601 (SI enable, functions integrated
in the drive), p9612 (SI PROFIsafe failure response)

### F01683 SI Motion P1: SOS/SLS enable missing

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

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
  
IMMEDIATELY

**Cause:**
  
The safety-relevant basic function "SOS/SLS" is not enabled in p9501 although other
safety-relevant monitoring functions are enabled.  
Note:  
This fault does not result in a safety stop response.

**Remedy:**
  
Enable the function "SOS/SLS" (p9501.0) and carry out a POWER ON.  
Note:  
SI: Safety Integrated  
SLS: Safely-Limited Speed  
SOS: Safe Operating Stop  
See also: p9501 (SI Motion enable safety functions)

### F01685 SI Motion P1: Safely-Limited Speed limit value too high

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
%1

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
  
The limit value for the function "Safely-Limited Speed" (SLS) is greater than the
speed that corresponds to an encoder limit frequency of 500 kHz.  
Note:  
This fault does not result in a safety stop response.  
Fault value (r0949, interpret decimal):  
Maximum permissible speed.

**Remedy:**
  
Correct the limit values for SLS and carry out a POWER ON.  
Note:  
SI: Safety Integrated  
SLS: Safely-Limited Speed  
See also: p9531 (SI Motion SLS limit values)

### F01689 SI Motion: Axis re-configured

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
Parameter: %1

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
  
The axis configuration was changed, and internally set to the correct value.  
Note:  
This fault does not result in a safety stop response.  
Fault value (r0949, interpret decimal):  
Number of the parameter that initiated the change.

**Remedy:**
  
The following should be carried out after the changeover:  
- exit the safety commissioning mode (p0010).  
- save all parameters  
- carry out a POWER ON.  
Once the drive has been powered up, message F01680 or F30680 indicates that the checksums
have changed in the drive. The following must, therefore, be carried out:  
- activate safety commissioning mode again.  
- complete safety commissioning of the drive.  
- exit the safety commissioning mode (p0010).  
- save all parameters  
- carry out a POWER ON.  
Note:  
For the commissioning tool, the units are only consistently displayed after a project
upload.

### F01690 SI Motion: Data save problem for the NVRAM

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

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
  
POWER ON

**Cause:**
  
There is not sufficient memory space in the NVRAM on the drive to save parameters
r9781 and r9782 (safety logbook).  
Note:  
This fault does not result in a safety stop response.  
Fault value (r0949, interpret decimal):  
1: There is no longer any free memory space in the NVRAM.

**Remedy:**
  
For fault value = 1:  
- deselect functions that are not required and that take up memory space in the NVRAM.  
- contact Technical Support.  
Note:  
NVRAM: Non-Volatile Random Access Memory (non-volatile read and write memory)

### A01691 SI Motion: Ti and To unsuitable for PN cycle

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

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
  
The configured times for PROFINET communication are not permitted and the PN cycle
is used as the actual value acquisition cycle for the safe movement monitoring functions:  
Isochronous PROFINET:  
The sum of Ti and To is too high for the selected PN cycle. The PN clock cycle should
be at least 1 current controller cycle greater than the sum of Ti and To.  
No isochronous PROFINET:  
The PN clock cycle must be at least 4x the current controller clock cycle.  
Notice:  
If this alarm is not observed, then message A01711 or A30711 – with the value 1020
... 1021 – can sporadically occur.

**Remedy:**
  
Configure Ti and To low so that they are suitable for the PN cycle or increase the
PN cycle time.

### A01693 SI P1: Safety parameter settings changed, warm restart/POWER ON required

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

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
  
Safety parameters have been changed; these will only take effect following a warm
restart or POWER ON.  
Alarm value (r2124, interpret decimal):  
Parameter number of the safety parameter which has changed, necessitating a warm restart
or POWER ON.

**Remedy:**
  
- carry out a warm restart.  
- carry out a POWER ON (switch-off/switch-on).  
Note:  
A POWER ON is required before carrying out the acceptance test.

### F01694 SI Motion P1: Firmware version monitoring channel 2 older than monitoring channel 1

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

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
  
IMMEDIATELY

**Cause:**
  
The firmware version of monitoring channel 2 is older than monitoring channel 1.  
Note:  
This message does not result in a safety stop response.  
This message can occur, if after an automatic firmware update, a POWER ON was not
carried out (Alarm A01007).

**Remedy:**
  
Carry out a POWER ON at the drive (switch-off/switch-on).  
See also: r9590 (SI Motion version, safe motion monitoring functions)

### A01695 SI Motion: Sensor Module was replaced

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

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
  
A Sensor Module, which is used for safe motion monitoring functions, was replaced.
The hardware replacement must be acknowledged. An acceptance test must be subsequently
performed.  
Note:  
This message does not result in a safety stop response.

**Remedy:**
  
- acknowledge component replacement (p9702 = 29).  
- back up all parameters.  
- carry out a POWER ON (switch-off/switch-on) for all components.  
- then carry out an acceptance test.

### A01696 SI Motion: Test stop for the motion monitoring functions selected when booting

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
-

**Message class:**
  
Safety monitoring channel has identified an error (10)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The forced checking procedure (test stop) for the safe motion monitoring functions
is already selected when booting, which is not permissible.  
This is the reason that the test is only carried out again after first selecting the
forced checking procedure.  
Note:  
This message does not result in a safety stop response.

**Remedy:**
  
Deselect the forced checking procedure (test stop) for the safe motion monitoring
functions and then select again.  
SI: Safety Integrated

### A01697 SI Motion: Test stop for motion monitoring functions required

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
-

**Message class:**
  
Safety monitoring channel has identified an error (10)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The time set in p9559 for the forced checking procedure (test stop) for the safe motion
monitoring functions has been exceeded. A new forced checking procedure is required.  
After the next time the forced checking procedure is selected, the message is withdrawn
and the monitoring time is reset.  
Note:  
- this message does not result in a safety stop response.  
- As the switch-off signal paths are not automatically checked during booting, an
alarm is always issued once booting is complete.  
- the test must be performed within a defined, maximum time interval (p9559, maximum
of 9000 hours) in order to comply with the requirements as laid down in the standards
for timely fault detection and the conditions to calculate the failure rates of safety
functions (PFH value). Operation beyond this maximum time period is permissible if
it can be ensured that the forced checking procedure is performed before persons enter
the hazardous area and who are depending on the safety functions correctly functioning.  
See also: p9559 (SI Motion forced checking procedure timer), r9765 (SI Motion forced checking
procedure remaining time)

**Remedy:**
  
Carry out the forced checking procedure (test stop) for the safe motion monitoring
functions.  
Note:  
SI: Safety Integrated

### A01698 SI P1: Commissioning mode active

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
-

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
  
The commissioning of the "Safety Integrated" function is selected.  
Note:  
- this message does not result in a safety stop response.  
- in the safety commissioning mode, the "STO" function is internally selected.  
See also: p0010 (Drive commissioning parameter filter 2)

**Remedy:**
  
Not necessary.  
This message is automatically withdrawn after the safety functions have been commissioned.  
Note:  
SI: Safety Integrated  
STO: Safe Torque Off

### A01699 SI P1: Test stop for STO required

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
-

**Message class:**
  
Safety monitoring channel has identified an error (10)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The time set in p9659 for the forced checking procedure (test stop) for the "STO"
function has been exceeded. A new forced checking procedure is required.  
After the next time the "STO" function is deselected, the message is withdrawn and
the monitoring time is reset.  
Note:  
- this message does not result in a safety stop response.  
- the test must be performed within a defined, maximum time interval (p9659) in order
to comply with the requirements as laid down in the standards for timely fault detection
and the conditions to calculate the failure rates of safety functions (PFH value).
Operation beyond this maximum time period is permissible if it can be ensured that
the forced checking procedure is performed before persons enter the hazardous area
and who are depending on the safety functions correctly functioning.  
See also: p9659 (SI forced checking procedure timer), r9660 (SI forced checking procedure remaining
time)

**Remedy:**
  
Select STO and then deselect again.  
Note:  
SI: Safety Integrated  
STO: Safe Torque Off

### F01700 SI Motion P1: STO initiated

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
-

**Message class:**
  
Safety monitoring channel has identified an error (10)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The drive is stopped using STO.  
Possible causes:  
- stop request from another monitoring channel.  
- STO not active after parameterized time (p9557) after test stop selection.  
- subsequent response, following messages: A01706, A01714, F01701, A01716

**Remedy:**
  
- remove the cause of the fault on the second monitoring channel.  
- carry out diagnostics for the active messages (A01706, A01714, F01701, A01716).  
- check the value in p9557 (where available), increase the value if necessary, and
carry out a POWER ON  
- check the switch-off signal path of monitoring channel 1 (check DRIVE-CLiQ communication
if it has been implemented)  
- replace drive.  
Note:  
SAM: Safe Acceleration Monitor (safe acceleration monitoring)  
SI: Safety Integrated  
STO: Safe Torque Off

### F01701 SI Motion P1: SS1 initiated

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
-

**Message class:**
  
Safety monitoring channel has identified an error (10)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The drive is stopped using SS1.  
As a result of this fault, after the time parameterized in p9556 has expired, or the
speed threshold parameterized in p9560 has been fallen below, message F01700 "STO
initiated" is output.  
Possible causes:  
- stop request from another monitoring channel.  
- subsequent response, following messages: A01714, A01711, A01707, A01716

**Remedy:**
  
- remove the cause of the fault on the second monitoring channel.  
- carry out diagnostics for the active messages (A01714, A01711, A01707, A01716).  
Note:  
This message can be acknowledged via PROFIsafe (safe acknowledgment).  
SI: Safety Integrated  
SS1: Safe Stop 1

### A01706 SI Motion P1: SAM/SBR limit exceeded

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
-

**Message class:**
  
Safety monitoring channel has identified an error (10)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
Motion monitoring functions with SAM (p9506 = 0):  
- after initiating SS1 or SS2, the speed exceeded the set tolerance.  
Motion monitoring functions with SBR (p9506 = 2):  
- after initiating SS1 or SLS switchover to the lower speed level, the speed exceeded
the set tolerance.  
The drive is stopped by message F01700.

**Remedy:**
  
Check the braking behavior and, if necessary, adapt the parameterization of the parameter
settings of the "SAM" or the "SBR" function.  
Note:  
This message can be acknowledged via PROFIsafe (safe acknowledgment).  
SAM: Safe Acceleration Monitor (safe acceleration monitoring)  
SBR: Safe Brake Ramp (safe ramp monitoring)  
SI: Safety Integrated  
SS1: Safe Stop 1  
SS2: Safe Stop 2  
SLS: Safely-Limited Speed  
See also: p9548 (SI Motion SAM actual speed tolerance), p9581 (SI Motion brake ramp reference
value), p9582 (SI Motion brake ramp delay time), p9583 (SI Motion brake ramp monitoring
time)

### A01707 SI Motion P1: Tolerance for safe operating stop exceeded

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
-

**Message class:**
  
Safety monitoring channel has identified an error (10)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The actual position has moved further away from the target position than the standstill
tolerance.  
The drive is stopped by message F01701.

**Remedy:**
  
- check whether safety faults are present and if required carry out the appropriate
diagnostic routines for the particular faults.  
- check whether the standstill tolerance matches the accuracy and control dynamic
performance of the axis.  
- carry out a POWER ON (switch-off/switch-on).  
Note:  
SI: Safety Integrated  
SOS: Safe Operating Stop  
See also: p9530 (SI Motion standstill tolerance)

### F01708 SI Motion P1: SS2 initiated

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
-

**Message class:**
  
Safety monitoring channel has identified an error (10)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 STOP2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The drive is stopped using SS2 (braking along the OFF3 down ramp).  
"Safe Operating Stop" (SOS) is activated after the parameterized time has expired.  
Possible causes:  
Subsequent response, following messages: A01714, A01716  
See also: p9552 (SI Motion transition time SS2 to SOS)

**Remedy:**
  
Carry out diagnostics for the active messages (A01714, A01716).  
Note:  
SI: Safety Integrated  
SOS: Safe Operating Stop  
SS2: Safe Stop 2

### A01709 SI Motion P1: SS2E initiated

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
-

**Message class:**
  
Safety monitoring channel has identified an error (10)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The drive is stopped using SS2E (braking along a path).  
"Safe Operating Stop" (SOS) is activated after the parameterized time has expired.  
Possible causes:  
Subsequent response, following messages: A01714, A01716  
See also: p9553 (SI Motion transition time SS2E to SOS)

**Remedy:**
  
- remove the cause of the fault at the control.  
- carry out diagnostics for the active messages (A01714, A01716).  
Note:  
SI: Safety Integrated  
SOS: Safe Operating Stop  
SS2E: Safe Stop 2 External (Safe Stop 2 with external stop)

### A01711 SI Motion P1: Defect in a monitoring channel

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
%1

**Message class:**
  
Safety monitoring channel has identified an error (10)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The drive has identified a difference between the input data or results of the monitoring
functions and initiated A01711. Safe operation is no longer possible.  
At least one monitoring function is active, so that after the parameterized timer
has expired, message F01701 is output.  
The message value that resulted in this message is shown in r9725.  
The following described message values involve the data cross-check between the two
monitoring channels (safety functions integrated in the drive).  
The message values may also occur in the following cases if the cause that is explicitly
mentioned does not apply:  
- For message values 3, 44 ... 57, 232 and 1-encoder system, differently set encoder
parameters.  
- incorrect synchronization.  
Message value (r2124, interpret decimal):  
0 to 999: Number of the cross-compared data that resulted in this fault.  
Message values that are not subsequently listed are only for internal Siemens troubleshooting.  
0: Stop request from another monitoring channel.  
1: Status image of monitoring functions SOS, SLS, SAM/SBR or SDI (result list 1) (r9710[0],
r9710[1]).  
2: Status image of monitoring function SSM (result list 2) (r9711[0], r9711[1]).  
3: The position actual value differential (r9713[0/1]) between the two monitoring
channels is greater than the tolerance in p9542.  
4: Error when synchronizing the data cross-check between the two channels.  
5: Enable safe functions (p9501).  
6: Limit value for SLS1 (p9531[0]).  
7: Limit value for SLS2 (p9531[1]).  
8: Limit value for SLS3 (p9531[2]).  
9: Limit value for SLS4 (p9531[3]).  
10: Standstill tolerance (p9530).  
31: Position tolerance (p9542).  
33: Time, speed switchover (p9551)  
35: Delay time STO (p9556).  
36: Test time, STO (p9557).  
37: Transition time SS2 to SOS (p9552).  
38: Transition time SS2E to SOS (p9553).  
42: Shutdown speed STO (p9560).  
43: Memory test stop response (STO).  
44 ... 57: General  
Possible cause 1 (during commissioning or parameter modification)  
The tolerance value for the monitoring function is not the same on the two monitoring
channels.  
Possible cause 2 (during active operation)  
The limit values are based on the actual value (r9713[0/1]). If the safe actual values
on the two monitoring channels do not match, the limit values, which have been set
at a defined interval, will also be different (i.e. corresponding to message value
3). This can be ascertained by checking the safe actual positions.  
Permissible deviation between the two monitoring channels: p9542.  
44: Position actual value (r9713[0/1]) + limit value SLS1 (p9531[0]) * safety monitoring
clock cycle.  
45: Position actual value (r9713[0/1]) + limit value SLS1 (p9531[0]) * safety monitoring
clock cycle.  
46: Position actual value (r9713[0/1]) + limit value SLS2 (p9531[1]) * safety monitoring
clock cycle.  
47: Position actual value (r9713[0/1]) + limit value SLS2 (p9531[1]) * safety monitoring
clock cycle.  
48: Position actual value (r9713[0/1]) + limit value SLS3 (p9531[2]) * safety monitoring
clock cycle.  
49: Position actual value (r9713[0/1]) - limit value SLS3 (p9531[2]) * safety monitoring
clock cycle.  
50: Position actual value (r9713[0/1]) + limit value SLS4 (p9531[3]) * safety monitoring
clock cycle.  
51: Position actual value (r9713[0/1]) - limit value SLS4 (p9531[3]) * safety monitoring
clock cycle.  
52: Standstill position + tolerance (p9530).  
53: Standstill position - tolerance (p9530).  
54: Position actual value (r9713[0/1]) + limit value of SSM (p9546) * safety monitoring
clock cycle + tolerance (p9542).  
55: Position actual value (r9713[0/1]) + limit value of SSM (p9546) * safety monitoring
clock cycle.  
56: Position actual value (r9713[0/1]) - limit value of SSM (p9546) * safety monitoring
clock cycle.  
57: Position actual value (r9713[0/1]) - limit value of SSM (p9546) * safety monitoring
clock cycle - tolerance (p9542).  
58: Actual stop request.  
75: Velocity limit of SSM (p9546).  
When function "SSM" is enabled (p9501.16 = 1), then this message value is output -
also for a different hysteresis tolerance (p9547).  
76: Stop response for SLS1 (p9563[0]).  
77: Stop response for SLS2 (p9563[1]).  
78: Stop response for SLS3 (p9563[2]).  
79: Stop response for SLS4 (p9563[3]).  
81: Velocity tolerance for SAM (p9548).  
82: SGEs for SLS correction factor.  
83: Acceptance test timer (p9558).  
84: Transition time A01711 (p9555).  
89: Encoder limit frequency.  
230: Filter time constant for SSM.  
231: Hysteresis tolerance for SSM.  
232: Smoothed velocity actual value.  
233: Limit value of SSM / safety monitoring clock cycle + hysteresis tolerance.  
234: Limit value of SSM / safety monitoring clock cycle.  
235: -Limit value of SSM / safety monitoring clock cycle.  
236: -Limit value of SSM / safety monitoring clock cycle - hysteresis tolerance.  
237: SGA SSM.  
238: Speed limit value for SAM (p9568 or p9546).  
239: Acceleration for SBR (p9581 and p9583).  
240: Inverse value of acceleration for SBR (p9581 and p9583).  
241: Deceleration time for SBR (p9582).  
242: Function specification (p9506).  
243: Function configuration (p9507).  
247: SDI tolerance (p9564).  
248: SDI positive upper limit (7FFFFFFF hex).  
249: Position actual value (r9713[0/1]) - SDI tolerance (p9564).  
250: Position actual value (r9713[0/1]) + SDI tolerance (p9564).  
251: SDI negative lower limit (80000001 hex).  
252: SDI stop response (p9566).  
253: SDI delay time (p9565).  
256: Status image of monitoring functions SOS, SLS, test stop, SBR, SDI (result list
1 ext) (r9710).  
259: PROFIsafe telegram (p9611) is different between the monitoring channels.  
261: Scaling factor for acceleration for SBR different.  
262: Scaling factor for the inverse value of the acceleration for SBR different.  
265: Status image of all change functions (results list 1) (r9710).  
270: Screen form for SGE image: all functions, which are not supported/enabled for
the actual parameterization (p9501, p9601 and p9506).  
273: speed limit value for flattening the ramp for SAM/SBR different.  
276: Limit value for SLA1 (p9578/p9378).  
277: Stop response for SLA1 (p9579/p9379).  
278: Upper limit value for SLA1.  
279: Lower limit value for SLA1.  
280: Upper limit value for SLA1 (fine resolution).  
281: Lower limit value for SLA1 (fine resolution).  
282: SLA filter time (p9576/p9376).  
283: Acceleration actual value (fine resolution).  
1000: Watchdog timer has expired. Too many signal changes have occurred at safety-relevant
inputs.  
1001: Initialization error of watchdog timer.  
1005: STO already active for test stop selection.  
1011: Acceptance test status between the monitoring channels differ.  
1012: Plausibility violation of the encoder actual value.  
1020: Cyc. communication failure between the monit. channels.  
1021: Cyclic communication failure between the monitoring channel and encoder evaluation.  
1022: Sign-of-life error for DRIVE-CLiQ encoders monitoring channel 1.  
1023: Error in the effectiveness test in the DRIVE-CLiQ encoder  
1032: Sign-of-life error for DRIVE-CLiQ encoders monitoring channel 2.  
1033: Error checking offset between POS1 and POS2 for DRIVE-CLiQ encoder monitoring
channel 1.  
1034: Error checking offset between POS1 and POS2 for DRIVE-CLiQ encoder monitoring
channel 2.  
1035: offset between POS1 and POS2 for DRIVE-CLiQ encoder on one of the monitoring
channels has changed since the last commissioning.  
1039: Overflow when calculating the position.  
5000 ... 5140:  
PROFIsafe message values.  
For these message values, the failsafe control signals (Failsafe Values) are transferred
to the safety functions.  
5000, 5014, 5023, 5024, 5030 ... 5032, 5042, 5043, 5052, 5053, 5068, 5072, 5073, 5082
... 5087, 5090, 5091, 5122 ... 5125, 5132 ... 5135, 5140:  
An internal software error has occurred (only for internal Siemens troubleshooting).  
5012: Error when initializing the PROFIsafe driver.  
5013: The result of the initialization is different for the two controllers.  
5022: Error when evaluating the F parameters. The values of the transferred F parameters
do not match the expected values in the PROFIsafe driver.  
5025: The result of the F parameterization is different for the two controllers.  
5026: CRC error for the F parameters. The transferred CRC value of the F parameters
does not match the value calculated in the PST.  
5065: A communications error was identified when receiving the PROFIsafe telegram.  
5066: A time monitoring error (timeout) was identified when receiving the PROFIsafe
telegram.  
6000 ... 6166:  
PROFIsafe message values (PROFIsafe driver for PROFIBUS DP V1/V2 and PROFINET).  
For these message values, the failsafe control signals (Failsafe Values) are transferred
to the safety functions. If "SS1 after failure of PROFIsafe communication" is parameterized
(p9612), then transfer of the Failsafe Values is delayed.  
The significance of the individual message values is described in safety fault F01611.  
7000: Difference of the safe position higher than the parameterized tolerance (p9542).  
7002: Cycle counter for transferring the safe position is different in both monitoring
channels.  
See also: p9555 (SI Motion transition time A01711 to SS1), r9725 (SI Motion diagnostics A01711)

**Remedy:**
  
For message value = 0:  
- no error was identified in this monitoring channel. Observe the error message of
the other monitoring channel (A30711).  
For message value = 3:  
Commissioning phase:  
- check encoder parameters, and if required, correct (p9516, p9517, p9518, p9520,
p9521, p9522, p9526).  
In operation:  
- check the mechanical design and the encoder signals.  
For message value = 232:  
- increase the hysteresis tolerance (p9547). Possibly set the filtering higher (p9545).  
For message value = 278, 279, 280, 281: - check whether the same acceleration limit
has been set for both channels. A different result depends on whether SLA is enabled
and not selected - or enabled and selected. In this case, another message value is
possible.  
For message value = 1 ... 999:  
- if the message value is listed under cause: Check the cross-checked parameters to
which the message value refers.  
- copy safety parameters and confirm the data change (commissioning tool).  
- carry out a POWER ON (switch off/switch on) or a warm restart (p0009 = 30, p0976
= 2, 3).  
- upgrade the drive software.  
- correction of the encoder evaluation. The actual values differ as a result of mechanical
faults (V belts, travel to a mechanical endstop, wear and window setting that is too
narrow, encoder fault, ...).  
For message value = 1001:  
- carry out a POWER ON (switch off/switch on) or a warm restart (p0009 = 30, p0976
= 2, 3).  
- upgrade the drive software.  
For message value = 1005:  
- check the conditions for deselecting STO.  
For message value = 1007:  
- check the PLC for the correct operating state (run state, basic program).  
For message value = 1011:  
- for diagnostics, refer to parameter (r9571).  
For message value = 1012:  
- upgrade the encoder evaluation firmware to a newer version.  
- check encoder parameters to ensure that they are the same (p9515, p9519, p9523,
p9524, p9525, p9529).  
- start the copy function for encoder parameters (commissioning tool).  
- the parameterized encoder does not correspond to the connected encoder - replace
the encoder.  
- check the electrical cabinet design and cable routing for EMC compliance  
- carry out a POWER ON (switch off/switch on) or a warm restart (p0009 = 30, p0976
= 2, 3).  
- replace the hardware.  
For message value = 1020, 1021:  
- check the communication link.  
- carry out a POWER ON (switch off/switch on) or a warm restart (p0009 = 30, p0976
= 2, 3).  
- replace the hardware.  
For message value = 1035, if the safety encoder was replaced:  
- acknowledge hardware replacement.  
- save all parameters  
- acknowledge fault.  
For message value = 1039:  
- check the conversion factors such as spindle pitch or gearbox ratios.  
For message value = 5000, 5014, 5023, 5024, 5030, 5031, 5032, 5042, 5043, 5052, 5053,
5068, 5072, 5073, 5082 ... 5087, 5090, 5091, 5122 ... 5125, 5132 ... 5135, 5140:  
- carry out a POWER ON (switch off/switch on) or a warm restart (p0009 = 30, p0976
= 2, 3).  
- upgrade firmware to later version.  
- contact Technical Support.  
- replace drive.  
For message value = 5012:  
- check the setting of the PROFIsafe address of the drive (p9610). It is not permissible
for the PROFIsafe address to be 0 or FFFF!  
- copy safety parameters and confirm the data change (commissioning tool).  
- carry out a POWER ON (switch off/switch on) or a warm restart (p0009 = 30, p0976
= 2, 3).  
For message value = 5013, 5025:  
- carry out a POWER ON (switch off/switch on) or a warm restart (p0009 = 30, p0976
= 2, 3).  
- check the setting of the PROFIsafe address of the drive (p9610).  
For message value = 5022:  
- check the setting of the values of the F parameters at the PROFIsafe slave (F_SIL,
F_CRC_Length, F_Par_Version, F_Source_Add, F_Dest_add, F_WD_Time).  
For message value = 5026:  
- check the settings of the values of the F parameters and the F parameter CRC (CRC1)
calculated from these at the PROFIsafe slave and update.  
For message value = 5065:  
- check the configuration and communication at the PROFIsafe slave (cons. No. / CRC).  
- check the setting of the value for F parameter F_WD_Time on the PROFIsafe slave
and increase if necessary.  
For message value = 5066:  
- check the setting of the value for F parameter F_WD_Time on the PROFIsafe slave
and increase if necessary.  
- evaluate diagnostic information in the F host.  
- check PROFIsafe connection.  
For message value = 6000 ... 6999:  
See the description of the message values for fault F01611.  
Note:  
SAM: Safe Acceleration Monitor (safe acceleration monitoring)  
SBR: Safe Brake Ramp (safe ramp monitoring)  
SDI: Safe Direction (safe motion direction)  
SI: Safety Integrated  
SLS: Safely-Limited Speed  
SOS: Safe Operating Stop  
SS1: Safe Stop 1  
SS2: Safe Stop 2  
SSM: Safe Speed Monitor (safety-relevant feedback signal from the speed monitoring)

### A01714 SI Motion P1: Safely-Limited Speed exceeded

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
%1

**Message class:**
  
Safety monitoring channel has identified an error (10)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The drive has moved faster than that specified by the velocity limit value (p9531).
The drive is stopped by the configured stop response (p9563).  
Message value (r2124, interpret decimal):  
100: SLS1 exceeded.  
200: SLS2 exceeded.  
300: SLS3 exceeded.  
400: SLS4 exceeded.  
1000: Encoder limit frequency exceeded.

**Remedy:**
  
- check the traversing/motion program in the control.  
- check limits for SLS and if required adapt accordingly (p9531).  
Note:  
SI: Safety Integrated  
SLS: Safely-Limited Speed  
See also: p9531 (SI Motion SLS limit values), p9563 (SI Motion SLS-specific stop response)

### A01716 SI Motion P1: Tolerance for safe motion direction exceeded

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
%1

**Message class:**
  
Safety monitoring channel has identified an error (10)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The tolerance for the "safe motion direction" function was exceeded. The drive is
stopped by the configured stop response (p9566).  
Message value (r2124, interpret decimal):  
0: Tolerance for function "safe motion direction positive" exceeded.  
1: Tolerance for function "safe motion direction negative" exceeded.

**Remedy:**
  
- check the traversing/motion program in the control.  
- check the tolerance for "SDI" function and if required, adapt (p9564).  
This message can be acknowledged as follows:  
Deselect/select SDI and perform safe acknowledgment via PROFIsafe.  
Note:  
SDI: Safe Direction (safe motion direction)  
SI: Safety Integrated  
See also: p9564 (SI Motion SDI tolerance), p9565 (SI Motion SDI delay time), p9566 (SI Motion
SDI stop response)

## SINAMICS Alarms SINAMICS S210 01730 - 30043

SINAMICS Alarms SINAMICS S210 01730 - 30043

### A01730 SI Motion P1: Reference block for dynamic Safely-Limited Speed invalid

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
%1

**Message class:**
  
Safety monitoring channel has identified an error (10)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The reference block transferred via PROFIsafe is negative.  
A reference block is used to generate a referred velocity limit value based on the
reference quantity "Velocity limit value SLS1" (p9531[0]).  
The drive is stopped by the configured stop response (p9563[0]).  
Message value (r2124, interpret decimal):  
requested, invalid reference block.

**Remedy:**
  
In the PROFIsafe telegram, input data S_SLS_LIMIT_IST must be corrected.  
Note:  
SI: Safety Integrated  
SLS: Safely-Limited Speed

### A01750 SI Motion P1: Hardware fault safety-relevant encoder

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** Encoder 1 | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The encoder that is used for the safety-relevant motion monitoring functions signals
a hardware fault.  
Message value (r2124, interpret decimal):  
Encoder status word 1, encoder status word 2 that resulted in the message.

**Remedy:**
  
- check the encoder connection.  
- replace encoder.

### A01751 SI Motion P1: Effectivity test fault safety-relevant encoder

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
%1

**Message class:**
  
Safety monitoring channel has identified an error (10)

| Symbol | Meaning |
| --- | --- |
| **Component:** Encoder 1 | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The DRIVE-CLiQ encoder for safe motion monitoring signals an error for the effectivity
tests.  
Message value (r2124, interpret decimal):  
Only for internal Siemens troubleshooting.

**Remedy:**
  
- check the encoder connection.  
- replace encoder.  
Note:  
This message can be acknowledged via PROFIsafe (safe acknowledgment).

### A01780 SBT When selected, the brake is closed

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
Following brakes are closed: %1 bin

**Message class:**
  
Safety monitoring channel has identified an error (10)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
When selecting the brake test or starting the brake test, the brake was not open.  
Alarm value (r2124, interpret binary):  
Bit 0 = 1:  
The internal brake is closed.  
Note:  
The alarm is also signaled if no brake is configured in p10202.  
SBT: Safe Brake Test  
See also: p10202 (SI Motion SBT brake)

**Remedy:**
  
Open the brake and reselect the brake test.

### A01781 SBT brake opening time exceeded

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
Fault cause: %1 bin

**Message class:**
  
Safety monitoring channel has identified an error (10)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The maximum time (11 s) to open the brake during the brake test was exceeded.  
Possible causes:  
- during the brake test the drive went into a fault condition, and therefore the brake
was closed by the drive.  
Alarm value (r2124, interpret binary):  
Bit 0 = 1:  
Internal brake was not able to be opened.  
Note:  
SBT: Safe Brake Test

**Remedy:**
  
- carry out a safe acknowledgment.  
- restart the brake test.

### A01782 SBT brake test incorrect control

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
Fault cause: %1 bin

**Message class:**
  
Safety monitoring channel has identified an error (10)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The brake test was canceled as a result of incorrect control.  
Alarm value (r2124, interpret binary):  
Alarm value 0:  
The brake test was canceled as a result of a fault (brake opening time or brake closing
time exceeded).  
Bit 0:  
The safe brake test was canceled by resetting the brake test selection.  
Bit 1:  
The safe brake test was canceled by resetting the brake test start.  
Bit 2:  
The brake is not configured in configured p10202.  
There is a brake test configuration error. In this case, alarm A01785 is also output.  
Note:  
SBT: Safe Brake Test  
See also: p10202 (SI Motion SBT brake)

**Remedy:**
  
- check parameterization of the brake test (p10202).  
- check as to whether alarm A01785 is present, and if so, evaluate.  
- carry out a safe acknowledgment.  
- if required, restart the brake test.

### A01783 SBT brake closing time exceeded

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
Fault cause: %1 bin

**Message class:**
  
Safety monitoring channel has identified an error (10)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The maximum time (11 s) to close the brake during the brake test was exceeded.  
Alarm value (r2124, interpret binary):  
Bit 0 = 1:  
The brake was not able to be closed.  
Note:  
SBT: Safe Brake Test

**Remedy:**
  
- when using an internal brake with external feedback signal, check whether the feedback
signal is correctly interconnected with the extended brake control.  
- carry out a safe acknowledgment.  
- restart the brake test.

### A01784 SBT brake test canceled with fault

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
Fault cause: %1

|  |  |  |  |
| --- | --- | --- | --- |
|  | Bit | Cause: | Remedy: |
| %1 | 0 | Operation when selecting the brake test not enabled (r0899.2=0). | Enable operation when selecting the brake test |
| 1 | External fault occurred (e.g. the brake test that has already started is canceled by the user) | Do not cancel the brake test |  |
| 2 | A brake is closed when selecting the brake test. | Keep the brake open when selecting the brake test |  |
| 3 | A brake is closed when the determining the load torque | Keep the brake open when determining the load torque |  |
| 4 | Stop response fault occurred - or pulse enable was withdrawn | Do not withdraw pulse enable |  |
| 5 | Axis setpoint speed too high when selecting the brake test | Check setpoint speed |  |
| 6 | Actual speed (r0063) of the axis too high when selecting the brake test | Check the actual speed |  |
| 7 | Incorrect speed controller mode (e.g. encoderless speed control or U/f operation). | Set the correct mode for SBT |  |
| 8 | Closed-loop control has not been enabled or function generator is active. | Enable closed-loop control or deactivate function generator |  |
| 9 | Closed-loop control does not to switchover to the brake test | Check closed-loop control |  |
| 10 | Torque limit reached (r1407.7, r1408.8). | Check torque limit |  |
| 17 | Brake test sequence error | see detailed fault cause (bits 0 to 10) |  |
| 18 | The internal brake is closed | Keep internal brake open |  |
| 19 | The external brake is closed | Keep external brake open |  |
| 20 | Not all of the brakes are open | Keep all brakes open |  |
| 21 | Axis position during the brake test invalid as a result of parking axis. | Check axis position |  |
| 22 | Internal software error |  |  |
| 23 | Permissible position range of the axis when the brake is closed was violated | Check position range |  |
| 24 | Internal brake was opened during the active brake test. | Keep the internal brake closed during the active brake test. |  |
| 25 | External brake was opened during the active brake test. | Keep the external brake closed during the active brake test. |  |
| 26 | During the active brake test, the test torque has exited its tolerance bandwidth | Check test torque |  |

**Message class:**
  
Safety monitoring channel has identified an error (10)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The safe brake test was canceled as a result of a fault.  
Alarm value (r2124, interpret binary):  
Bit 17 = 1: fault in the brake test sequence (cause, see bits 0 ... 10).  
Bit 20 = 1: the brake is not opened (p10202).  
Bit 21 = 1: axis position during the brake test not valid due to parking axis.  
Bit 22 = 1: internal software error.  
Bit 23 = 1: the permissible position range of the axis was violated with the brake
closed (p10212/p10222).  
Bit 24 = 1: the tested internal brake was opened while the brake test was active.  
Bit 26 = 1: during the active brake test, the test torque left its tolerance bandwidth
(20 %).  
Cause for alarm value bit 17:  
Bit 0 = 1: operation when selecting the brake test not enabled (r0899.2 = 0).  
Bit 1 = 1: external fault occurred (e.g. the brake test that has already started is
canceled by the user).  
Bit 2 = 1: when selecting the brake test a brake is closed.  
Bit 3 = 1: when determining the load torque a brake is closed.  
Bit 4 = 1: A fault has occurred with stop response (e.g. OFF1, OFF2 or OFF3) - or
the pulse enable was withdrawn (e.g. STO selected or operation no longer enabled).  
Bit 5 = 1: when selecting the brake test the axis speed setpoint is too high.  
Bit 6 = 1: the actual speed (r0063) of the axis is too high (e.g. brake does not hold
during the brake test).  
Bit 8 = 1: closed-loop control not enabled or function generator active.  
Bit 9 = 1: control does not switch over to the brake test (e.g. because PI speed control
has not been parameterized).  
Bit 10 = 1: torque limit reached (r1407.7, r1408.8).  
Note:  
SBT: Safe Brake Test

**Remedy:**
  
- remove the fault cause.  
- carry out a safe acknowledgment.  
- if required, restart the brake test.  
For bit 17 = 1 with bit 6 = 1 or bit 23 = 1:  
If the brake closing time of the motor holding brake (p1217) has been set too low,
then at the start of the brake test, the brake is closed too late. The brake closing
time should be adapted (p1217).

### A01785 SBT brake test configuration error

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
%1

**Message class:**
  
Safety monitoring channel has identified an error (10)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
Error when parameterizing the brake test.  
In this configuration, the brake test cannot be started or cannot be started without
error.  
Alarm value (r2124, interpret decimal):  
1:  
No motion monitoring functions have been enabled.  
4:  
No brake was configured (p10202).  
8:  
The brake test is configured for an internal brake, however the safety brake control
is not enabled (p9602).  
16:  
The safe brake test and safety without encoder are simultaneously enabled (p9506).
This is not permissible.  
Note:  
SBT: Safe Brake Test

**Remedy:**
  
Check parameterization of the brake test.

### A01788 SI: Automatic test stop waits for STO deselection via motion monitoring functions

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
-

**Message class:**
  
Safety monitoring channel has identified an error (10)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The automatic test stop (forced checking procedure) was not able to be carried out
after powering up.  
Possible causes:  
- the STO function is selected via safe motion monitoring functions.  
- a safety message is present, that resulted in a STO.  
Note:  
STO: Safe Torque Off

**Remedy:**
  
- deselect STO via safe motion monitoring functions.  
- remove the cause of the safety messages and acknowledge the messages.  
Note:  
The automatic test stop is performed after removing the cause.

### A01796 SI P1: Wait for communication

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

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
  
The drive waits for communication to be established to execute the safety-relevant
motion monitoring functions.  
Note:  
STO is active in this state.  
Alarm value (r2124, interpret decimal):  
3: Wait for communication to be established to PROFIsafe F-Host.

**Remedy:**
  
If the message is not automatically withdrawn after a longer period of time, then
carry out the following checks:  
- evaluate any other PROFIsafe communication messages/signals present.  
- check the operating state of the F-Host.  
- check the communication connection to the F Host.  
Note:  
STO: Safe Torque Off  
See also: p9601 (SI enable, functions integrated in the drive)

### A01798 SI Motion P1: Test stop for motion monitoring functions running

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
-

**Message class:**
  
Safety monitoring channel has identified an error (10)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The forced checking procedure (test stop) for the safe motion monitoring functions
is currently in progress.

**Remedy:**
  
Not necessary.  
The message is automatically withdrawn when the test stop has been completed.  
Note:  
SI: Safety Integrated

### A01799 SI Motion P1: Acceptance test mode active

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
-

**Message class:**
  
Safety monitoring channel has identified an error (10)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The acceptance test mode is active.  
This means that the setpoint speed limiting is deactivated (r9733).

**Remedy:**
  
Not necessary.  
The message is automatically withdrawn when exiting the acceptance test mode.  
Note:  
SI: Safety Integrated

### F01800 DRIVE-CLiQ: Hardware/configuration error

**Drive object:**
  
S210

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
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

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
- ensure that the DRIVE-CLiQ components have the same firmware versions.  
- avoid longer topologies for short current controller sampling times.  
For fault value = 10:  
- check the DRIVE-CLiQ cables at the Control Unit.  
- remove any short-circuit for motors with DRIVE-CLiQ.  
- carry out a POWER ON.  
For fault value = 11:  
- check the electrical cabinet design and cable routing for EMC compliance  
For fault value = 12:  
- replace the component involved.

### A01839 DRIVE-CLiQ diagnostics: cable fault to the component

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

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

**Remedy:**
  
- check the corresponding DRIVE-CLiQ cables.  
- check the electrical cabinet design and cable routing for EMC compliance

### A01900 PN: Configuration telegram error

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

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
PN: configured telegram cannot be set.  
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
- check the list of the drive objects with process data exchange (p0978).  
Note:  
With p0978[x] = 0, all of the following drive objects in the list are excluded from
the process data exchange.  
For alarm value = 2:  
- check the number of data words for output and input to a drive object.  
For alarm value = 211:  
- Ensure offline version &lt;= online version.  
For alarm value = 223, 500:  
- check the setting in p8839 and p8815.  
- check for inserted but not configured CBE20.  
- ensure that only one PZD interface is operated in clock synchronism or with PROFIsafe.  
For alarm value = 255:  
- check configured drive objects.  
For alarm value = 256:  
- check the configured telegram.  
For alarm value = 257:  
- check the number of data words for output and input to the complete device.  
For alarm value = 501:  
- check the set PROFIsafe address (p9610).  
For alarm value = 502:  
- check the set PROFIsafe telegram (p60022, p9611).

### A01902 PN: clock cycle synchronous operation parameterization not permissible

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

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
8: Bus reserve bus cycle time Tdp - data exchange time Tdx less than two current controller
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
- adapt the sampling time for the current controller or speed controller.  
For alarm value = 10:  
- reduce Tdx by using fewer bus participants or shorter telegrams.  
Note:  
PN: PROFINET

### F01910 Fieldbus: setpoint timeout

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
-

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 OFF3

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The reception of setpoints from the fieldbus interface (onboard, PROFIBUS/PROFINET/USS)
has been interrupted.  
- bus connection interrupted.  
- controller switched off.  
- controller set into the STOP state.

**Remedy:**
  
Restore the bus connection and set the controller to RUN.  
Note regarding PROFIBUS slave redundancy:  
For operation on a Y link, it must be ensured that "DP alarm mode = DPV1" is set in
the slave parameterization.

### F01911 PN: Clock synchronous operation, clock cycle failure

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
-

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 OFF1

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The global control telegram to synchronize the clock cycles has failed - in cyclic
operation - for several DP clock cycles or has violated the time grid specified in
the parameterizing telegram over several consecutive DP clock cycles (refer to the
bus cycle time, Tdp and Tpllw).

**Remedy:**
  
- check the physical bus configuration (cable, connector, terminating resistor, shielding,
etc.).  
- check whether communication was briefly or permanently interrupted.  
- check the utilization level of the bus and controller (e.g. bus cycle time Tdp was
set too short).  
Note:  
PN: PROFINET

### F01912 PN: Clock synchronous operation sign-of-life missing

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
-

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 OFF1

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The maximum permissible number of errors in the controller sign-of-life (clock synchronous
operation) has been exceeded in cyclic operation.

**Remedy:**
  
- physically check the bus (cables, connectors, terminating resistor, shielding, etc.).  
- correct the interconnection of the controller sign-of-life (p2045).  
- check whether the controller correctly sends the sign-of-life (e.g. create a trace
with STW2.12 ... STW2.15 and trigger signal ZSW1.3).  
- check the permissible telegram failure rate (p0925).  
- check the utilization level of the bus and controller (e.g. bus cycle time Tdp was
set too short).  
Note:  
PN: PROFINET

### A01932 PN: clock cycle synchronization missing for DSC

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

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
  
There is no clock synchronization or clock synchronous sign of life and DSC is selected.  
Note:  
DSC: Dynamic Servo Control  
See also: r0922 (PROFIdrive PZD telegram selection)

**Remedy:**
  
Set clock synchronization across the bus configuration and transfer clock synchronous
sign-of-life.

### A01940 PN: Clock cycle synchronism not reached

**Drive object:**
  
S210

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
  
The bus is in the data exchange state and clock synchronous operation has been selected
using the parameterizing telegram. It was not possible to synchronize to the clock
cycle specified by the master.  
- the master does not send a clock synchronous global control telegram although clock
synchronous operation was selected when configuring the bus.  
- the master is using an isochronous DP clock cycle that is different than was transferred
to the slave in the parameterizing telegram.  
- at least one drive object has a pulse enable (also not controlled from PROFINET).

**Remedy:**
  
- check the master application and bus configuration.  
- check the consistency between the clock cycle input when configuring the slave and
clock cycle setting at the master.  
- check that no drive object has a pulse enable. Only enable the pulses after synchronizing
the PROFINET drives.  
Note:  
PN: PROFINET

### A01941 PN: Clock cycle signal missing when the bus is being established

**Drive object:**
  
S210

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
  
The bus is in the data exchange state and clock synchronous operation has been selected
using the parameterizing telegram. The global control telegram for synchronization
is not being received.

**Remedy:**
  
Check the master application and bus configuration.  
Note:  
PN: PROFINET

### A01943 PN: Clock cycle signal error when the bus is being established

**Drive object:**
  
S210

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
  
The bus is in the data exchange state and clock synchronous operation has been selected
using the parameterizing telegram.  
The global control telegram for synchronization is being irregularly received.  
-.the master is sending an irregular global control telegram.  
- the master is using another clock synchronous DP clock cycle than was transferred
to the slave in the parameterizing telegram.

**Remedy:**
  
- check the master application and bus configuration.  
- check the consistency between the clock cycle input when configuring the slave and
clock cycle setting at the master.  
Note:  
PN: PROFINET

### A01944 PN: Sign-of-life synchronism not reached

**Drive object:**
  
S210

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
  
The bus is in the data exchange state and clock synchronous operation has been selected
using the parameterizing telegram.  
Synchronization with the master sign-of-life (STW2.12 ... STW2.15) could not be completed
because the sign-of-life is changing differently to how it was configured in the Tmapc
time grid.

**Remedy:**
  
- ensure that the master correctly increments the sign-of-life in the master application
clock cycle Tmapc.  
- correct the interconnection of the master sign-of-life (p2045).  
Note:  
PN: PROFINET

### F01950 PN: Clock synchronous operation, synchronization unsuccessful

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
-

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 OFF1

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
Synchronization of the internal clock cycle to the global control telegram has failed.
The internal clock cycle exhibits an unexpected shift.

**Remedy:**
  
Only for internal Siemens troubleshooting.  
Note:  
PN: PROFINET

### A01980 PN: cyclic connection interrupted

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

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
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
Info 1: %1, Info 2: %2

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

### A01989 PN: internal cyclic data transfer error

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

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

### A02007 Function generator: Drive not SERVO / VECTOR / DC_CTRL

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

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
- remove the cause of this alarm.  
- restart the function generator.

### F03001 NVRAM checksum incorrect

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

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

### A05000 Power unit: Overtemperature heat sink AC inverter

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
-

**Message class:**
  
Power electronics faulted (5)

| Symbol | Meaning |
| --- | --- |
| **Component:** Power Module | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The alarm threshold for overtemperature at the inverter heat sink has been reached.
The response is set using p0290.  
If the heat sink temperature exceeds the value set in p0292[0], then fault F30004
is output.

**Remedy:**
  
Check the following:  
- is the ambient temperature within the defined limit values?  
- have the load conditions and the load duty cycle been appropriately dimensioned?  
- has the cooling failed?

### A05001 Power unit: Overtemperature depletion layer chip

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
-

**Message class:**
  
Power electronics faulted (5)

| Symbol | Meaning |
| --- | --- |
| **Component:** Power Module | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
Alarm threshold for overtemperature of the power semiconductor in the AC converter
has been reached.  
Note:  
- the response is set using p0290.  
- if the temperature of the barrier layer increases by the value set in p0292[1],
then fault F30025 is initiated.

**Remedy:**
  
Check the following:  
- is the ambient temperature within the defined limit values?  
- have the load conditions and the load duty cycle been appropriately dimensioned?  
- has the cooling failed?  
- pulse frequency too high?  
See also: r0037 (Drive temperatures)

### A05003 Power unit: Internal overtemperature

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
-

**Message class:**
  
Power electronics faulted (5)

| Symbol | Meaning |
| --- | --- |
| **Component:** Power Module | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The alarm threshold for internal overtemperature has been reached.  
If the temperature inside the power unit increases by an additional 5 K, then fault
F30036 is triggered.

**Remedy:**
  
Check the following:  
- is the ambient temperature within the defined limit values?  
- has the fan failed? Check the direction of rotation.

### A05006 Power unit: Overtemperature thermal model

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
-

**Message class:**
  
Power electronics faulted (5)

| Symbol | Meaning |
| --- | --- |
| **Component:** Power Module | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The temperature difference between the chip and heat sink has exceeded the permissible
limit value (blocksize power units only).  
Depending on p0290, an appropriate overload response is initiated.  
See also: r0037 (Drive temperatures)

**Remedy:**
  
Not necessary.  
This alarm is automatically withdrawn once the limit value has been fallen below.  
Note:  
If the alarm is not automatically withdrawn and the temperature continues to rise,
this can result in fault F30024.

### F06310 Supply voltage (p0210) incorrectly parameterized

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
-

**Message class:**
  
Network fault (2)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
For AC/AC drive units, the measured DC voltage lies outside the tolerance range after
precharging has been completed.  
The following applies for the tolerance range: 1.16 * p0210 &lt; r0070 &lt; 1.6 * p0210  
Note:  
The fault can only be acknowledged when the drive is switched off.  
See also: p0210 (Drive unit line supply voltage)

**Remedy:**
  
- check the parameterized supply voltage and if required change (p0210).  
- check the line supply voltage.  
See also: p0210 (Drive unit line supply voltage)

### F07011 Drive: Motor overtemperature

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
%1

**Message class:**
  
Motor overload (8)

| Symbol | Meaning |
| --- | --- |
| **Component:** Motor | **Propagation:** GLOBAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The calculated motor temperature is too high.  
Possible causes:  
- motor overloaded.  
- motor ambient temperature too high.  
- sensor wire breakage  
Fault value (r0949, interpret decimal):  
200:  
Motor temperature model 1 (I2t): temperature too high.  
300:  
Motor temperature model 3: after the monitoring time has expired, the temperature
is still higher than the alarm threshold.  
301:  
Motor temperature model 3: temperature is too high, or the model has not been parameterized.  
302:  
Motor temperature model 3: Encoder temperature is not within the valid range.

**Remedy:**
  
- reduce the motor load.  
- check the ambient temperature and the motor ventilation.  
- check the wiring and temperature sensor connection.  
- check monitoring limits.

### A07012 Drive: Motor temperature model 1/3 overtemperature

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
%1

**Message class:**
  
Motor overload (8)

| Symbol | Meaning |
| --- | --- |
| **Component:** Motor | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The motor temperature model 1/3 identified that the alarm threshold was exceeded.  
Hysteresis:2K  
Alarm value (r2124, interpret decimal):  
200:  
Motor temperature model 1 (I2t): temperature too high.  
300:  
Motor temperature model 3: temperature too high.  
See also: r0034 (Motor utilization thermal), p0613 (Motor temperature model ambient temperature)

**Remedy:**
  
- check the motor load and if required, reduce.  
- check the motor ambient temperature.  
See also: r0034 (Motor utilization thermal)

### F07085 Drive: Open-loop/closed-loop control parameters changed

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

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
  
Open-loop/closed-loop control parameters have had to be changed.  
Possible causes:  
1. As a result of other parameters, they have exceeded the dynamic limits.  
2. They cannot be used due to the fact that the hardware detected not having certain
features.  
3. The value is estimated as the thermal time constant is missing.  
4. Motor temperature model 1 is activated as thermal motor protection is missing.  
See also: p1082 (Maximum speed)

**Remedy:**
  
Not necessary.  
It is not necessary to change the parameters as they have already been correctly limited.

### A07091 Drive: determined current controller dynamic response invalid

**Drive object:**
  
S210

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
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
When one button tuning is activated (p5300 = 1), the current controller is measured
after the pulses have been enabled. Evaluation has indicated that the current control
loop was not appropriately set.  
Possible causes:  
- incorrectly set current controller.  
- PRBS amplitude set too high (p5296).  
Alarm value (r2124, interpret hexadecimal):  
1: Dynamic response too low.  
2: Current controller unstable.  
Note:  
PRBS: Pseudo Random Binary Signal (binary noise)

**Remedy:**
  
- the measurement can be repeated with a smaller excitation amplitude (p5296).  
- if required, adapt the current controller proportional gain (p1715).

### A07092 Drive: moment of inertia estimator still not ready

**Drive object:**
  
S210

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
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The moment of inertia estimator has still not determined any valid values.  
The acceleration cannot be calculated.  
The moment of inertia estimator has stabilized, if the frictional values (p1563, p1564)
as well as the moment of inertia value (p1493) have been determined and the appropriate
status signal is set (r1407.26 = 1).  
The following parameters influence the response of the moment of the inertia estimator:  
p1560, p1561, p1562

**Remedy:**
  
Traverse the axis until the moment of inertia estimator has stabilized.  
This alarm is automatically withdrawn after the moment of inertia estimator has stabilized.

### F07093 Drive: Test signal error

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** GLOBAL |

  

**Reaction:**
  
 OFF3

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
An error was identified when executing the "Test signal" function.  
The function was not executed or was canceled.  
Fault value (r0949, interpret decimal):  
1: No distance limit has been defined (p5308 = 0).  
2: The moment of inertia estimator has not stabilized in the parameterized time (p5309)
(r1407.26).  
3: The parameterized distance (p5308) was exceeded.  
4: no motor encoder parameterized (closed-loop speed control without encoder).  
5: Offset (p5297) is too high for the parameterized distance (p5308).  
6: Pulse enable was withdrawn while traversing.  
7: speed setpoint not equal to zero.  
See also: p5308 (One Button Tuning distance limiting), p5309 (One Button Tuning duration)

**Remedy:**
  
For fault value = 1:  
- Define distance limiting (p5308).  
For fault value = 2:  
- increase the duration or distance limiting (p5309, p5308).  
For fault value = 3:  
- check distance limiting (p5308).  
For fault value = 4:  
- configure speed control with encoder.  
For fault value = 5:  
- increase distance limit p5308 or reduce offset p5297.  
- the fault can only be acknowledged after p5300 was set = 0.  
- for the factory setting, a test signal duration of approximately 1.3 s is obtained.
If an offset (p5297) of 60 rpm is set, for example, then this results in a distance
of approximately 1.3 revolutions. As a consequence, a value must be parameterized
in parameter p5308, which is longer than this distance + 10% controller reserve (e.g.
p5308=515°). Further, the distance depends on the speed controller sampling time (p0115[1])
and the controller configuration (p5271).  
For fault value = 6:  
- keep the drive switched on until the "Test signal" function has been completely
exited.  
For fault value = 7:  
- set the speed setpoint to zero. It is possible that the setpoint was entered from
the control panel.

### A07094 General parameter limit violation

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

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

### A07095 Drive: One Button Tuning activated

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

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
  
The One Button Tuning function is active.  
One Button Tuning is performed at the next switch-on command.  
See also: p5300 (One Button Tuning selection)

**Remedy:**
  
Not necessary.  
The alarm is automatically withdrawn after One Button Tuning has been exited (p5300
= 0).

### F07097 Drive: Test signal error distance limiting

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
Fault cause: %1, traversing distance: %2

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** GLOBAL |

  

**Reaction:**
  
 OFF3

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
An error was identified when executing the "Test signal" function or auto tuning was
selected (p5300 = 1).  
The function was not executed or was canceled.  
Fault value (r0949, interpret decimal):  
yyyyxxxx hex: yyyy = error cause, xxxx = traversing distance  
Fault cause = 4:  
- travel distance to the EPOS software limit switch is not sufficient.  
See also: p5308 (One Button Tuning distance limiting), p5309 (One Button Tuning duration)

**Remedy:**
  
- enter the traversing path in parameter p5308 - or deselect the function involved
in p5301.  
- for fault cause = 1, 2, shorter traversing paths may be possible.  
For fault cause = 1:  
- deselect bit 0 and bit 1 in parameter p5301.  
For fault cause = 2:  
- deselect bit 2 in parameter p5301.  
For fault cause = 3:  
- deselect bit 4 and bit 5 in parameter p5301.  
For fault cause = 4:  
- change the travel direction of One Button Tuning via p5308.  
- increase the clearance to the EPOS software limit switch by manually traversing.

### A07200 Drive: Master control ON command present

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

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
  
The ON/OFF1 command is present (no 0 signal).  
The command is either influenced via binector input p0840 (current CDS) or control
word bit 0 via the master control.

**Remedy:**
  
Switch the signal via binector input p0840 (current CDS) or control word bit 0 via
the master control to 0.

### F07220 Drive: Master control by PLC missing

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
-

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 OFF1

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The "master control by PLC" signal was missing in operation.  
- interconnection of the binector input for "master control by PLC" is incorrect (p0854).  
- the higher-level control has withdrawn the "master control by PLC" signal.  
- data transfer via the fieldbus (master/drive) was interrupted.

**Remedy:**
  
- check the interconnection of the binector input for "master control by PLC" (p0854).  
- check the "master control by PLC" signal and, if required, switch in.  
- check the data transfer via the fieldbus (master/drive).  
Note:  
If the drive should continue to operate after withdrawing "master control by PLC"
then fault response must be parameterized to NONE or the message type should be parameterized
as alarm.

### F07334 Function not possible

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
%1

**Message class:**
  
Application/technological function faulted (17)

| Symbol | Meaning |
| --- | --- |
| **Component:** Motor | **Propagation:** GLOBAL |

  

**Reaction:**
  
 OFF1

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
For this configuration, the selected function is not possible.  
Fault value (r0949, interpret decimal):  
0:  
Function "Travel to fixed end stop" (p1545) was selected, although encoderless operation
or U/f operation is active.

**Remedy:**
  
For fault value = 0:  
- Operate the closed-loop speed control with an encoder.  
- If necessary, deselect function "Travel to fixed stop".

### F07410 Drive: Current controller output limited

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
-

**Message class:**
  
Application/technological function faulted (17)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The condition "I_act = 0 and Uq_set_1 longer than 16 ms at its limit" is present and
can be caused by the following:  
- motor not connected or motor contactor open.  
- no DC link voltage present.  
- Motor Module defective.

**Remedy:**
  
- connect the motor or check the motor contactor.  
- check the DC link voltage (r0070).  
- check the Motor Module.

### F07412 Drive: Commutation angle incorrect (motor model)

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
%1

**Message class:**
  
Actual position/speed value incorrect or not available (11)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 ENCODER

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
An incorrect commutation angle was detected that can result in a positive coupling
in the speed controller.  
Possible causes:  
- the phase sequence of the output phases for the motor is incorrect (e.g. the phases
are interchanged).  
- the motor encoder is incorrectly adjusted with respect to the magnet position.  
- the motor encoder is damaged.  
- the angular commutation offset is incorrectly set (p0431).  
- data to calculate the motor model has been incorrectly set (p0356 (motor-stator
leakage inductance) and/or p0350 (motor-stator resistance) and/or p0352 (cable resistance)).  
- the changeover speed for the motor model is too low (p1752). The monitoring function
only becomes effective above the changeover speed.  
- pole position identification might have calculated an incorrect value when activated
(p1982 = 1).  
- the motor encoder speed signal is faulted.  
- the control loop is instable due to incorrect parameterization.  
Fault value (r0949, interpret decimal):  
SERVO:  
0: The comparison of the pole position angle from the encoder and motor model resulted
in an excessively high value (p1778[1] &gt; 80 ° electrical).  
1: -  
VECTOR:  
0: The comparison of the pole position angle from the encoder and motor model resulted
in an excessively high value (&gt; 45 ° electrical).  
1: The change in the speed signal from the motor encoder has changed by &gt; p0492 within
a current controller clock cycle.

**Remedy:**
  
- check the phase sequence for the motor, and if required, correct (wiring, p1820).  
- if the encoder mounting was changed - re-adjust the encoder.  
- replace the defective motor encoder.  
- correctly set the angular commutation offset (p0431). If required, determine using
p1990.  
- correctly set the motor stator resistance, cable resistance and motor-stator leakage
inductance (p0350, p0352, p0356).  
Calculate the cable resistance from the cross-section and length, check the inductance
and stator resistance using the motor data sheet, measure the stator resistance, e.g.
using a multimeter - and if required, again identify the values using the stationary
motor data identification (p1910).  
- increase the changeover speed for the motor model (p1752). The monitoring is completely
deactivated for p1752 &gt; p1082 (maximum speed).  
- with pole position identification activated (p1982 = 1) check the procedure for
pole position identification (p1980) and force a new pole position identification
procedure by means of deselection followed by selection (p1982 = 0 -&gt; 1).  
Note:  
For High Dynamic Motors (1FK7xxx-7xxx), for applications with a higher current, if
necessary, the monitoring should be disabled.

### F07414 Drive: Encoder serial number changed

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 ENCODER

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The serial number of the motor encoder of a synchronous motor has changed. The change
was only checked for encoders with serial number (e.g. EnDat encoders) and build-in
motors (e.g. p0300 = 401) or third-party motors (p0300 = 2).  
Cause 1:  
- the encoder was replaced.  
Cause 2:  
- a third-party, built-in or linear motor was re-commissioned.  
Cause 3:  
- the motor with integrated and adjusted encoder was replaced.  
Cause 4:  
- the firmware was updated to a version that checks the encoder serial number.  
Note:  
With closed-loop position control, the serial number is accepted when starting the
adjustment (p2507 = 2).  
When the encoder is adjusted (p2507 = 3), the serial number is checked for changes
and if required, the adjustment is reset (p2507 = 1).  
Proceed as follows to hide serial number monitoring:  
- set the following serial numbers for the corresponding Encoder Data Set: p0441=
FF, p0442 = 0, p0443 = 0, p0444 = 0, p0445 = 0.  
- parameterize F07414 as message type N (p2118, p2119).

**Remedy:**
  
For causes 1, 2:  
Carry out an automatic adjustment using the pole position identification routine.
Acknowledge fault. Initiate the pole position identification routine with p1990 =
1. Then check that the pole position identification routine is correctly executed.  
SERVO:  
If a pole position identification technique is selected in p1980, and if p0301 does
not contain a motor type with an encoder adjusted in the factory, then p1990 is automatically
activated.  
or  
Set the adjustment via p0431. In this case, the new serial number is automatically
accepted.  
or  
Mechanically adjust the encoder. Accept the new serial number with p0440 = 1.  
For causes 3, 4:  
Accept the new serial number with p0440 = 1.

### F07432 Drive: Motor without overvoltage protection

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
%1

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
  
In the case of a fault at maximum speed, the motor can generate an overvoltage that
can destroy the converter.

**Remedy:**
  
Limit the maximum speed (p1082) without any additional protection.  
Note:  
The maximum speed is calculated as follows:  
p1082 &lt;= 11.695 * DC link voltage overvoltage threshold/r0316  
DC link voltage overvoltage threshold:  
- line connection 1 AC: 410 V  
- line connection 3 AC: 820 V  
See also: r0316 (Motor torque constant), p1082 (Maximum speed)

### F07433 Drive: Closed-loop control with encoder is not possible as the encoder has not been unparked

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
%1

**Message class:**
  
Actual position/speed value incorrect or not available (11)

| Symbol | Meaning |
| --- | --- |
| **Component:** Sensor Module Encoder 1 | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The changeover to closed-loop control with encoder is not possible as the encoder
has not been unparked.

**Remedy:**
  
- check whether the encoder firmware supports the "parking" function (r0481.6 = 1).  
- upgrade the firmware.  
Note:  
For long-stator motors (p3870.0 = 1), the following applies:  
The encoder must have completed the unparking procedure (r3875.0 = 1) before a changeover
can be made to closed-loop control with encoder. The encoder is unparked using binector
input p3876 = 0/1 signal and remains until a 0 signal in this state.

### F07434 Drive: It is not possible to change the direction of rotation with the pulses enabled

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
-

**Message class:**
  
Application/technological function faulted (17)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A drive data set was selected - with the pulses enabled - which has a different parameterized
direction of rotation (p1821).  
It is only possible to change the motor direction of rotation using p1821 when the
pulses are inhibited.

**Remedy:**
  
- change over the drive data set with the pulses inhibited.  
- ensure that the changeover to a drive data set does not result in the motor direction
of rotation being changed (i.e. for these drive data sets, the same value must be
in p1821).  
See also: p1821 (Direction of rotation)

### A07565 Drive: Encoder error in PROFIdrive encoder interface 1

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
%1

**Message class:**
  
Actual position/speed value incorrect or not available (11)

| Symbol | Meaning |
| --- | --- |
| **Component:** Sensor Module Encoder 1 | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
An encoder error was signaled for encoder 1 via the PROFIdrive encoder interface (G1_ZSW.15).  
Alarm value (r2124, interpret decimal):  
Error code from G1_XIST2.

**Remedy:**
  
Acknowledge the encoder error using the encoder control word (G1_STW.15 = 1).

### F07575 Drive: Motor encoder not ready

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
-

**Message class:**
  
Actual position/speed value incorrect or not available (11)

| Symbol | Meaning |
| --- | --- |
| **Component:** Sensor Module Encoder 1 | **Propagation:** GLOBAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The motor encoder signals that it is not ready.  
- initialization of encoder 1 (motor encoder) was unsuccessful.  
- the function "parking encoder" is active (encoder control word G1_STW.14 = 1).  
- the encoder interface (Sensor Module) is deactivated (p0145).  
- the Sensor Module is defective.

**Remedy:**
  
Evaluate other queued faults via encoder 1.

### F07801 Drive: Motor overcurrent

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
-

**Message class:**
  
Motor overload (8)

| Symbol | Meaning |
| --- | --- |
| **Component:** Motor | **Propagation:** GLOBAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The permissible motor limit current was exceeded.  
- active current limit too low.  
- current controller not correctly set.  
- load is too high.  
- short-circuit in the motor cable or ground fault.  
- motor current does not match the drive current.

**Remedy:**
  
- reduce the load.  
- check the motor and motor cables for short-circuit and ground fault.  
- check the drive and motor combination.

### F07802 Drive: Infeed not ready

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
-

**Message class:**
  
Infeed faulted (13)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The drive does not signal a ready state after an internal switch-on command.  
- DC link voltage is not present.  
- defective drive.  
- supply voltage incorrectly set.

**Remedy:**
  
- check the enable signals for the drive.  
- replace the drive.  
- check the line supply voltage setting (p0210).

### A07805 Drive: Power unit overload I2t

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
-

**Message class:**
  
Power electronics faulted (5)

| Symbol | Meaning |
| --- | --- |
| **Component:** Power Module | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The alarm threshold for I2t overload (p0294) of the power unit has been exceeded.  
The response parameterized in p0290 becomes active.

**Remedy:**
  
- reduce the continuous load.  
- adapt the load duty cycle.  
- check the assignment of the rated currents of the motor and Motor Module.

### F07860 External braking resistor signals overtemperature

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
-

**Message class:**
  
External measured value / signal state outside the permissible range (16)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The temperature monitoring of the external braking resistor, connected via digital
input 4 (DI 4, X130/2.6), responded.  
Note:  
This signal is triggered for a 1/0 edge at digital input 4.

**Remedy:**
  
- Check the dimensioning of the external braking resistor for the application.  
- Check the external braking resistor and temperature monitoring.  
- Check the temperature monitoring connection (X130/2.6).

### F07900 Drive: Motor blocked/speed controller at its limit

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
-

**Message class:**
  
Application/technological function faulted (17)

| Symbol | Meaning |
| --- | --- |
| **Component:** Motor | **Propagation:** GLOBAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The motor operates longer than 0.2 seconds at the torque limit and below the speed
threshold in p2175.  
This signal can also be initiated if the speed actual value is oscillating and the
speed controller output repeatedly goes to its limit.  
See also: p2175 (Motor blocked speed threshold)

**Remedy:**
  
- check that the motor can freely move.  
- check the effective torque limit (r1538, r1539).  
- check the parameter of the "Motor blocked" signal and possibly correct (p2175).

### F07901 Drive: Motor overspeed

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
-

**Message class:**
  
Application/technological function faulted (17)

| Symbol | Meaning |
| --- | --- |
| **Component:** Motor | **Propagation:** GLOBAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The maximum permissible speed was either positively or negatively exceeded (p1082).

**Remedy:**
  
- check the speed controller.  
- check the maximum speed (p1082).

### F07930 Drive: Brake control error

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
%1

**Message class:**
  
Application/technological function faulted (17)

| Symbol | Meaning |
| --- | --- |
| **Component:** Motor | **Propagation:** GLOBAL |

  

**Reaction:**
  
 OFF1

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The "Safety Integrated" function integrated in the drive has identified a brake control
fault in monitoring channel 2, and has initiated STO.  
- OCC cable shield is not correctly connected.  
- defect in the brake control circuit of the drive.  
Fault value (r0949, interpret decimal):  
10, 11:  
Fault in "open holding brake" operation.  
- brake not closed or interrupted cable.  
- ground fault in brake cable.  
20:  
Fault in "brake open" state.  
- short-circuit in brake winding.  
30, 31:  
Fault in "close holding brake" operation.  
- brake not closed or interrupted cable.  
- short-circuit in brake winding.  
40:  
Fault in "brake closed" state.  
50:  
Fault in the brake control of the drive or a communication error (brake control diagnostics).

**Remedy:**
  
- select STO and then deselect again.  
- check the motor holding brake connection.  
- check the function of the motor holding brake.  
- carry out a diagnostics routine for the faults involved.  
- check for EMC-compliant control cabinet design and cable routing (e.g. shield OCC
cable with shield terminal and shield plate, check the connection of the brake conductors).  
- replace drive.  
Note:  
OCC: One Cable Connection (one cable system)  
SBC: Safe Brake Control  
SI: Safety Integrated  
STO: Safe Torque Off  
See also: p1215 (Motor holding brake configuration)

### F07935 Drive: Incorrect motor holding brake configuration

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

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
  
An incorrect motor holding brake configuration was detected.  
Fault value (r0949, interpret decimal):  
0:  
A motor holding brake was detected where the brake control has not been configured
(p1215 = 0).  
The brake control configuration was set to "motor holding brake the same as sequence
control" (p1215 = 1) (only when commissioning for the first time).  
1:  
A motor holding brake was detected where the brake control has not been configured
(p1215 = 0).  
The brake control configuration was left at "No motor holding brake available" (p1215
= 0).

**Remedy:**
  
For fault value = 0:  
- no remedy required.  
For fault value = 1:  
- if required change the motor holding brake configuration (p1215 = 1, 2).  
- if this fault value unexpectedly occurs, then the motor connections should be checked
in order to rule out that they have been interchanged.  
See also: p1215 (Motor holding brake configuration)

### F07955 Drive: Motor has been changed

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** Motor | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The code number of the actual motor with DRIVE-CLiQ does not match the saved number.  
If available:  
The code numbers of the bearings, gearbox and brake do not match the saved numbers.

**Remedy:**
  
Connect the original motor and switch on the converter again (POWER ON) - or restore
the factory settings.  
Note:  
The data for bearings, gearbox and brake are reloaded.

### F08501 PN/COMM BOARD: Setpoint timeout

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
-

**Message class:**
  
Communication error to the higher-level control system (9)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 OFF3

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The reception of setpoints from the COMM BOARD has been interrupted.  
- bus connection interrupted.  
- controller switched off.  
- controller set into the STOP state.  
- COMM BOARD defective.

**Remedy:**
  
- Restore the bus connection and set the controller to RUN.  
- if the error is repeated, check the update time set in the bus configuration (HW
Config).

### A08511 PN/COMM BOARD: Receive configuration data invalid

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

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
- check the list of the drive objects with process data exchange (p0978). With p0978[x]
= 0, all of the following drive objects in the list are excluded from the process
data exchange.  
For alarm value = 2:  
- check the number of data words for output and input to a drive object.  
For alarm value = 17:  
- CBE20 Shared Device: Unplug/plug A-CPU.  
For alarm value = 223, 500:  
- check the setting in p8839 and p8815.  
- ensure that only one PZD interface is operated in clock synchronism or with PROFIsafe.  
For alarm value = 257:  
- check the number of data words for output and input to the complete device.  
For alarm value = 501:  
- check the set PROFIsafe address (p9610).

### A08800 PROFIenergy energy-saving mode active

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

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
  
The PROFIenergy energy-saving mode is active  
Alarm value (r2124, interpret decimal):  
Mode ID of the active PROFIenergy energy-saving mode.  
See also: r5600 (Pe energy-saving mode ID)

**Remedy:**
  
The alarm is automatically withdrawn when the energy-saving mode is exited.  
Note:  
The energy-saving mode is exited after the following events:  
- the PROFIenergy command end_pause is received from the higher-level control.  
- the higher-level control has changed into the STOP operating state.  
- the PROFINET connection to the higher-level control has been disconnected.

### A09000 Web server user incorrectly configured

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

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

### F13000 License not adequate

**Drive object:**
  
S210

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
- an error occurred when checking the existing licenses.  
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
Additional licenses are required and must be activated.  
For fault value = 1:  
With the system powered down, re-insert the memory card that matches the system.  
For fault value = 2:  
Enter and activate the license key.  
For fault value = 3:  
Compare the license key entered with the license key on the Certificate of License.  
Re-enter the license key and activate.  
For fault value = 4:  
- carry out a POWER ON.  
- upgrade firmware to later version.  
- contact Technical Support.  
Note:  
An overview of the converter functions requiring a license can be displayed using
a commissioning tool in the online mode. Depending on the commissioning tool, you
can obtain the necessary licenses (serial number, license Key, Trial License Mode).

### A13001 Error in license checksum

**Drive object:**
  
S210

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
  
When checking the checksum of the license key, an error was detected.

**Remedy:**
  
Compare the license key entered with the license key on the Certificate of License.  
Re-enter the license key and activate.

### F13009 Licensing Technology Extension not licensed

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 OFF1

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
At least one Technology Extension that requires a license does not have a license.

**Remedy:**
  
- enter and activate the license key for Technology Extensions that require a license.  
- if necessary, deactivate non-licensed Technology Extensions.

### F13010 Licensing function module not licensed

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 OFF1

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
At least one function module requiring a license is not licensed.  
Fault value (r0949, interpret hexadecimal):  
Bit x = 1: The corresponding function module does not have a license.

**Remedy:**
  
- enter and activate the license key for function modules that require a license.  
- if necessary, deactivate non-licensed function modules.

### A13021 Licensing for output frequencies > 550 Hz missing

**Drive object:**
  
S210

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
- in this specific case, the output frequency is limited to 550 Hz.  
- the "Trial License" function is not effective for license "High Output Frequency".

**Remedy:**
  
- enter and activate the license key for "High Output Frequency".  
- if necessary operate the motor below the output frequency of 550 Hz.

### A13030 Trial License activated

**Drive object:**
  
S210

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

**Remedy:**
  
Not necessary.  
The alarm is automatically withdrawn after the periods have expired.

### A13031 Trial License period expired

**Drive object:**
  
S210

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

**Remedy:**
  
- if required, start an additional period.  
- deactivate functions requiring a license.  
- appropriately license the drive unit.  
Note:  
A license that is not adequate will only become evident after the next time the system
runs up.

### A13032 Trial License last period activated

**Drive object:**
  
S210

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

**Remedy:**
  
Not necessary.  
The alarm is automatically withdrawn after the last period has expired.

### A13033 Trial License last period expired

**Drive object:**
  
S210

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

**Remedy:**
  
- deactivate functions requiring a license.  
- appropriately license the drive unit.  
Note:  
A license that is not adequate will only become evident after the next time the system
runs up.

### F13100 Know-how protection: Copy protection error

**Drive object:**
  
S210

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
  
 OFF1

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

**Remedy:**
  
For fault value = 0:  
- insert the correct memory card and carry out POWER ON.  
For fault value = 2, 3, 12, 13:  
- contact the responsible OEM.  
- Deactivate copy protection (p7765) and acknowledge the fault (p3981).  
- Deactivate know-how protection (p7766 ... p7768) and acknowledge the fault (p3981).  
Note:  
In general, the copy protection can only be changed when know-how protection is deactivated.  
KHP: Know-How Protection

### F13101 Know-how protection: Copy protection cannot be activated

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

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
  
- insert the memory card and carry out POWER ON.  
- Try to activate copy protection again (p7765).

### F13102 Know-how protection: Consistency error of the protected data

**Drive object:**
  
S210

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
  
 OFF1

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

### F30001 Drive: overcurrent

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
Fault cause: %1 bin

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
  
The drive has detected an overcurrent condition.  
- closed-loop control is incorrectly parameterized.  
- motor has a short-circuit or fault to ground (frame).  
- the rated motor current is significantly higher than that of the drive.  
- infeed: High discharge and post-charging currents for line voltage dip.  
- infeed: High post-charging currents for overload when motoring and DC link voltage
dip.  
- infeed: Short-circuit currents at switch-on as there is no commutating reactor.  
- power cables are not correctly connected.  
- the power cables exceed the maximum permissible length.  
- defective drive.  
- line phase interrupted.  
Fault value (r0949, interpret bitwise binary):  
Bit 0: Phase U.  
Bit 1: Phase V.  
Bit 2: Phase W.  
Bit 3: Overcurrent in the DC link.  
Note:  
Fault value = 0 means that the phase with overcurrent is not recognized.

**Remedy:**
  
- check the motor data - if required, carry out commissioning.  
- check the assignment of the rated motor and drive currents.  
- infeed: Check the line supply quality.  
- infeed: Reduce the motor load.  
- infeed: Check the correct connection of the line filter and the line commutating
reactor.  
- check the power cable connections.  
- check the power cables for short-circuit or ground fault.  
- check the length of the power cables.  
- replace drive.  
- check the line supply phases.

### F30002 Drive: DC link overvoltage

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
%1

**Message class:**
  
DC link overvoltage (4)

| Symbol | Meaning |
| --- | --- |
| **Component:** Power Module | **Propagation:** LOCAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The drive has detected an overvoltage condition in the DC link.  
- motor regenerates too much energy.  
- device supply voltage too high.  
- line phase interrupted.  
Fault value (r0949, interpret decimal):  
DC link voltage at the time of trip [0.1 V].

**Remedy:**
  
- increase the ramp-down time  
- use a braking resistor.  
- use a drive with a higher power rating.  
- check the device supply voltage (p0210).  
- check the line supply phases.  
See also: p0210 (Drive unit line supply voltage)

### F30003 Drive: DC link undervoltage

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
-

**Message class:**
  
Infeed faulted (13)

| Symbol | Meaning |
| --- | --- |
| **Component:** Power Module | **Propagation:** LOCAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The power unit has detected an undervoltage condition in the DC link.  
- line supply failure  
- line supply voltage below the permissible value.  
- line supply infeed failed or interrupted.  
- line phase interrupted.

**Remedy:**
  
- check the line supply voltage  
- check the line supply infeed and observe the fault messages relating to it (if there
are any)  
- check the line supply phases.  
- check the line supply voltage setting (p0210).  
See also: p0210 (Drive unit line supply voltage)

### F30004 Power unit: Overtemperature heat sink AC inverter

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

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
  
The temperature of the power unit heat sink has exceeded the permissible limit value.  
- insufficient cooling, fan failure.  
- overload.  
- ambient temperature too high.  
- pulse frequency too high.  
Fault value (r0949, interpret decimal):  
Temperature [0.01 °C].

**Remedy:**
  
- check whether the fan is running.  
- check the fan elements.  
- check whether the ambient temperature is in the permissible range.  
- check the motor load.  
- reduce the pulse frequency if this is higher than the rated pulse frequency.  
Notice:  
This fault can only be acknowledged after the alarm threshold for alarm A05000 has
been undershot.

### F30005 Power unit: Overload I2t

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

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
  
The power unit was overloaded (r0036 = 100 %).  
- the permissible rated power unit current was exceeded for an inadmissibly long time.  
- the permissible load duty cycle was not maintained.  
Fault value (r0949, interpret decimal):  
I2t [100 % = 16384].

**Remedy:**
  
- reduce the continuous load.  
- adapt the load duty cycle.  
- check the motor and power unit rated currents.  
See also: r0307 (Rated motor power)

### F30011 Power unit: Line phase failure in main circuit

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
%1

**Message class:**
  
Network fault (2)

| Symbol | Meaning |
| --- | --- |
| **Component:** Power Module | **Propagation:** LOCAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
At the power unit, the DC link voltage ripple has exceeded the permissible limit value.  
Possible causes:  
- a line phase has failed.  
- the 3 line phases are inadmissibly asymmetrical.  
- the capacitance of the DC link capacitor forms a resonance frequency with the line
inductance and the reactor integrated in the power unit.  
- the fuse of a phase of a main circuit has ruptured.  
- a motor phase has failed.  
- for power units operated on a single phase, the permissible active power was exceeded.  
Fault value (r0949, interpret decimal):  
Only for internal Siemens troubleshooting.

**Remedy:**
  
- check the main circuit fuses.  
- check whether a single-phase load is distorting the line voltages.  
- Detune the resonant frequency with the line inductance by using an upstream line
reactor.  
- Dampen the resonant frequency with the line inductance by switching over the DC
link voltage compensation in the software (see p1810) – or increase the smoothing
(see p1806). However, this can have a negative impact on the torque ripple at the
motor output.  
- check the motor feeder cables.

### F30015 Drive: phase failure motor cable

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
-

**Message class:**
  
Application/technological function faulted (17)

| Symbol | Meaning |
| --- | --- |
| **Component:** Motor | **Propagation:** GLOBAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A phase failure in the motor feeder cable was detected.  
The signal can also be output in the following case:  
The motor is correctly connected, however the closed-speed control is instable and
therefore an oscillating torque is generated.

**Remedy:**
  
- check the motor feeder cables.  
- check the speed controller settings.

### A30016 Power unit: Load supply switched off

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
%1

**Message class:**
  
Network fault (2)

| Symbol | Meaning |
| --- | --- |
| **Component:** Power Module | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The DC link voltage is too low.  
Alarm value (r2124, interpret decimal):  
DC link voltage at the time of the trip [V].

**Remedy:**
  
- switch on load supply.  
- check the line supply if necessary.  
- If necessary, insert the jumper for the internal braking resistor.  
- For a 3 AC line connection, connect an internal or external braking resistor (X4).

### F30017 Power unit: Hardware current limit has responded too often

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
Fault cause: %1 bin

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
  
The hardware current limitation in the relevant phase (see A30031, A30032, A30033)
has responded too often. The number of times the limit has been exceeded depends on
the design and type of power unit.  
For infeed units, the following applies:  
- closed-loop control is incorrectly parameterized.  
- load on the infeed is too high.  
- line reactor missing or the incorrect type.  
- power unit defective.  
The following applies to Motor Modules:  
- closed-loop control is incorrectly parameterized.  
- fault in the motor or in the power cables.  
- the power cables exceed the maximum permissible length.  
- motor load too high  
- power unit defective.  
Fault value (r0949, interpret binary):  
Bit 3: phase U  
Bit 4: phase V  
Bit 5: phase W  
Additional bits:  
Only for internal Siemens troubleshooting.  
Note:  
Fault value = 0 means that the phase with current limiting is not recognized (e.g.
for blocksize device).

**Remedy:**
  
For infeed units, the following applies:  
- check the controller settings and reset and identify the controller if necessary
(p0340 = 2, p3410 = 5)  
- reduce the load and increase the DC link capacitance or use a higher-rating infeed
if necessary  
- check the connection and technical data of the commutating reactor.  
- check the power cables for short-circuit or ground fault.  
- replace power unit.  
The following applies to Motor Modules:  
- check the motor data and if required, recalculate the controller parameters (p0340
= 3). As an alternative, run a motor data identification (p1910 = 1, p1960 = 1).  
- check the motor circuit configuration (star-delta).  
- check the motor load.  
- check the power cable connections.  
- check the power cables for short-circuit or ground fault.  
- check the length of the power cables.  
- replace power unit.

### F30021 Drive: ground fault

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
%1

**Message class:**
  
Ground fault / inter-phase short-circuit detected (7)

| Symbol | Meaning |
| --- | --- |
| **Component:** Power Module | **Propagation:** LOCAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The drive has detected a ground fault.  
Possible causes:  
- ground fault in the power cables.  
- ground fault at the motor.  
- when the brake closes, this causes the hardware DC current monitoring to respond.  
- short-circuit at the braking resistor.  
Fault value (r0949, interpret decimal):  
0:  
- the hardware DC current monitoring has responded.  
- short-circuit at the braking resistor.  
&gt; 0:  
Absolute value summation current amplitude.

**Remedy:**
  
- check the power cable connections.  
- check the motor.  
- check the cables and contacts of the brake connection (a wire is possibly broken).  
- check the braking resistor.

### F30024 Power unit: Overtemperature thermal model

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

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
  
IMMEDIATELY

**Cause:**
  
The temperature difference between the heat sink and chip has exceeded the permissible
limit value.  
- the permissible load duty cycle was not maintained.  
- insufficient cooling, fan failure.  
- overload.  
- ambient temperature too high.  
- pulse frequency too high.  
See also: r0037 (Drive temperatures)

**Remedy:**
  
- adapt the load duty cycle.  
- check whether the fan is running.  
- check the fan elements.  
- check whether the ambient temperature is in the permissible range.  
- check the motor load.  
- reduce the pulse frequency if this is higher than the rated pulse frequency.

### F30025 Power unit: Chip overtemperature

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

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
  
The chip temperature of the semiconductor has exceeded the permissible limit value.  
- the permissible load duty cycle was not maintained.  
- insufficient cooling, fan failure.  
- overload.  
- ambient temperature too high.  
- pulse frequency too high.  
Fault value (r0949, interpret decimal):  
Temperature difference between the heat sink and chip [0.01 °C].

**Remedy:**
  
- adapt the load duty cycle.  
- check whether the fan is running.  
- check the fan elements.  
- check whether the ambient temperature is in the permissible range.  
- check the motor load.  
- reduce the pulse frequency if this is higher than the rated pulse frequency.  
Notice:  
This fault can only be acknowledged after the alarm threshold for alarm A05001 has
been undershot.  
See also: r0037 (Drive temperatures)

### F30027 Power unit: Precharging DC link time monitoring

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
Enable signals: %1, Status: %2

**Message class:**
  
Infeed faulted (13)

| Symbol | Meaning |
| --- | --- |
| **Component:** Power Module | **Propagation:** LOCAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The power unit DC link was not able to be precharged within the expected time.  
1) There is no line supply voltage connected.  
2) The line contactor/line side switch has not been closed.  
3) The line supply voltage is too low.  
4) Line supply voltage incorrectly set (p0210).  
5) The precharging resistors are overheated as there were too many precharging operations
per time unit.  
6) The precharging resistors are overheated as the DC link capacitance is too high.  
7) The precharging resistors are overheated because when there is no "ready for operation"
(r0863.0) of the infeed unit, power is taken from the DC link.  
8) The precharging resistors are overheated as the line contactor was closed during
the DC link fast discharge through the Braking Module.  
9) The DC link has either a ground fault or a short-circuit.  
Fault value (r0949, interpret binary):  
yyyyxxxx hex:  
yyyy = power unit state  
0: Fault status (wait for OFF and fault acknowledgment).  
1: Restart inhibit (wait for OFF).  
2: Overvoltage condition detected -&gt; change into the fault state.  
3: Undervoltage condition detected -&gt; change into the fault state.  
4: Wait for bridging contactor to open -&gt; change into the fault state.  
5: Wait for bridging contactor to open -&gt; change into restart inhibit.  
6: Wait for bypass contactor to open  
7: Commissioning.  
8: Ready for precharging.  
9: Precharging started, DC link voltage lower than the minimum switch-on voltage  
10: Precharging, DC link voltage end of precharging still not detected  
11: Wait for the end of the de-bounce time of the main contactor after precharging
has been completed.  
12: Precharging completed, ready for pulse enable.  
13: It was detected that the STO terminal was energized at the power unit  
xxxx = Missing internal enable signals, power unit (inverted bit-coded, FFFF hex -&gt;
all internal enable signals available)  
Bit 0: Power supply of the IGBT gating shut down.  
Bit 1: Ground fault detected.  
Bit 2: Peak current intervention.  
Bit 3: I2t exceeded.  
Bit 4. Thermal model overtemperature calculated.  
Bit 5: (heat sink, gating module, power unit) overtemperature measured.  
Bit 6: Reserved.  
Bit 7: Overvoltage detected.  
Bit 8: Power unit has completed precharging, ready for pulse enable.  
Bit 9: STO terminal missing.  
Bit 10: Overcurrent detected.  
Bit 11: Armature short-circuit active.  
Bit 12: DRIVE-CLiQ fault active.  
Bit 13: Vce fault detected, transistor de-saturated due to overcurrent/short-circuit.  
Bit 14: Undervoltage detected.  
See also: p0210 (Drive unit line supply voltage)

**Remedy:**
  
In general:  
- check the line supply voltage at the input terminals.  
- check the line supply voltage setting (p0210).  
For 5):  
- carefully observe the permissible precharging frequency (refer to the appropriate
Manual).  
For 6):  
- check the total capacitance of the DC link and reduce in accordance with the maximum
permissible DC link capacitance if necessary (refer to the appropriate Manual).  
For 7):  
- interconnect the ready-for-operation signal from the infeed unit (r0863.0) in the
enable logic of the drives connected to this DC link  
For 8):  
- check the connections of the external line contactor. The line contactor must be
open during DC link fast discharge.  
For 9):  
- check the DC link for ground faults or short circuits.  
For 11):  
- check the DC link voltage of the infeed (r0070) and Motor Modules (r0070).  
If the DC link voltage generated by the infeed (or external) is not displayed for
the Motor Modules (r0070), then a fuse has ruptured in the Motor Module.  
See also: p0210 (Drive unit line supply voltage)

### A30031 Power unit: Hardware current limiting in phase U

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
-

**Message class:**
  
Power electronics faulted (5)

| Symbol | Meaning |
| --- | --- |
| **Component:** Power Module | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
Hardware current limit for phase U responded. The pulsing in this phase is inhibited
for one pulse period.  
- closed-loop control is incorrectly parameterized.  
- fault in the motor or in the power cables.  
- the power cables exceed the maximum permissible length.  
- motor load too high  
- power unit defective.  
Note:  
Alarm A30031 is always output if, for a Power Module, the hardware current limiting
of phase U, V or W responds.

**Remedy:**
  
- check the motor data and if required, recalculate the control parameters (p0340
= 3). As an alternative, run a motor data identification (p1910 = 1, p1960 = 1).  
- check the motor circuit configuration (star/delta).  
- check the motor load.  
- check the power cable connections.  
- check the power cables for short-circuit or ground fault.  
- check the length of the power cables.

### A30034 Power unit: Internal overtemperature

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
%1

**Message class:**
  
Power electronics faulted (5)

| Symbol | Meaning |
| --- | --- |
| **Component:** Power Module | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The alarm threshold for internal overtemperature has been reached.  
If the temperature inside the power unit increases up to the fault threshold, then
fault F30036 is triggered.  
- ambient temperature might be too high.  
- insufficient cooling, fan failure.  
Alarm value (r2124, interpret binary):  
Bit 0 = 1: Overtemperature in the control electronics area.  
Bit 1 = 1: Overtemperature in the power electronics area.  
Bit 2 = 1: Overtemperature in the processor area.  
Bit 3 = 1: Overtemperature in the processor area.  
Bit 4 = 1: Overtemperature when the internal fan is defective.  
Bit 5 = 1: Intake air overtemperature.

**Remedy:**
  
- check the ambient temperature.  
- check the fan for the inside of the unit.

### F30036 Power unit: Internal overtemperature

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

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
- insufficient cooling, fan failure.  
- overload.  
- ambient temperature too high.  
Fault value (r0949, interpret binary):  
Bit 0 = 1: Overtemperature in the control electronics area.  
Bit 1 = 1: Overtemperature in the power electronics area.  
Bit 2 = 1: Overtemperature in the processor area.  
Bit 3 = 1: Overtemperature in the processor area.  
Bit 4 = 1: Overtemperature when the internal fan is defective.  
Bit 5 = 1: Intake air overtemperature.

**Remedy:**
  
- check the internal fan.  
- check the fan elements.  
- check whether the ambient temperature is in the permissible range.  
Notice:  
This fault can only be acknowledged once the permissible temperature limit minus 5
K has been fallen below.

### F30040 Drive: 24/48 V undervoltage

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
Channel: %1, voltage: %2 [0.1 V]

**Message class:**
  
Supply voltage fault (undervoltage) (3)

| Symbol | Meaning |
| --- | --- |
| **Component:** Power Module | **Propagation:** LOCAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The undervoltage threshold of the 24 V power supply for the drive was fallen below
for longer than 3 ms.  
Fault value (r0949, interpret hexadecimal):  
yyxxxx hex: yy = channel, xxxx = voltage [0.1 V]  
yy = 0: 24 V power supply  
yy = 1: 48 V power supply

**Remedy:**
  
- check the drive power supply.  
- carry out a POWER ON (switch-off/switch-on).

### A30041 Power unit: Undervolt 24/48 V alarm

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
Channel: %1, voltage: %2 [0.1 V]

**Message class:**
  
Supply voltage fault (undervoltage) (3)

| Symbol | Meaning |
| --- | --- |
| **Component:** Power Module | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
For the power unit power supply, the lower threshold has been violated.  
Alarm value (r2124, interpret hexadecimal):  
yyxxxx hex: yy = channel, xxxx = voltage [0.1 V]  
yy = 0: 24 V power supply  
yy = 1: 48 V power supply

**Remedy:**
  
- check the power supply of the power unit.  
- carry out a POWER ON (switch-off/switch-on) for the component.

### A30042 Power unit: Fan has reached the maximum operating hours

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
%1

**Message class:**
  
Power electronics faulted (5)

| Symbol | Meaning |
| --- | --- |
| **Component:** Power Module | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The maximum operating time of at least one fan will soon be reached, or has already
been exceeded.  
Alarm value (r2124, interpret binary):  
Bit 0 = 1:  
The operating hours counter of the heat sink fan will reach the maximum operating
time in 500 hours. After 500 hours has elapsed, bit 0 is cleared and bit 2 is set
in the alarm value.  
Bit 1 = 1:  
The wear counter of the heat sink fan has reached 99 %. The remaining service life
is 1%. After this 1% has elapsed, bit 1 is cleared and bit 2 is set in the alarm value.  
Bit 2 = 1:  
The operating hours counter of the heat sink fan has exceeded the maximum operating
time - and/or the wear counter has exceeded 100%.  
Bit 8 = 1:  
The operating hours counter of the fan inside the device will reach the maximum operating
time in 500 hours. After 500 hours has elapsed, bit 8 is cleared and bit 10 is set
in the alarm value.  
Bit 10 = 1:  
The operating hours counter of the fan inside the device has exceeded the maximum
operating time.

**Remedy:**
  
For the fan involved, carry out the following:  
- replace the fan.  
- reset the operating hours counter (p0251, p0254).  
See also: p0251 (Power unit heat sink fan operating hours counter)

### F30043 Power unit: Overvolt 24/48 V

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
Channel: %1, voltage: %2 [0.1 V]

**Message class:**
  
Supply voltage fault (overvoltage) (3)

| Symbol | Meaning |
| --- | --- |
| **Component:** Power Module | **Propagation:** LOCAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
POWER ON

**Cause:**
  
For the power unit power supply, the upper threshold has been violated.  
Fault value (r0949, interpret hexadecimal):  
yyxxxx hex: yy = channel, xxxx = voltage [0.1 V]  
yy = 0: 24 V power supply  
yy = 1: 48 V power supply

**Remedy:**
  
Check the power supply of the power unit.

## SINAMICS Alarms SINAMICS S210 30044 - 50518

SINAMICS Alarms SINAMICS S210 30044 - 50518

### A30044 Power unit: Overvolt 24/48 V alarm

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
Channel: %1, voltage: %2 [0.1 V]

**Message class:**
  
Supply voltage fault (overvoltage) (3)

| Symbol | Meaning |
| --- | --- |
| **Component:** Power Module | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
For the power unit power supply, the upper threshold has been violated.  
Alarm value (r2124, interpret hexadecimal):  
yyxxxx hex: yy = channel, xxxx = voltage [0.1 V]  
yy = 0: 24 V power supply  
yy = 1: 48 V power supply

**Remedy:**
  
Check the power supply of the power unit.

### F30050 Power unit: 24 V supply overvoltage

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
-

**Message class:**
  
Supply voltage fault (overvoltage) (3)

| Symbol | Meaning |
| --- | --- |
| **Component:** Power Module | **Propagation:** LOCAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
POWER ON

**Cause:**
  
The voltage monitor signals an overvoltage fault on the module.

**Remedy:**
  
- check the 24 V power supply.  
- replace the module if necessary.

### F30051 Power unit: Motor holding brake short circuit detected

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
%1

**Message class:**
  
External measured value / signal state outside the permissible range (16)

| Symbol | Meaning |
| --- | --- |
| **Component:** Power Module | **Propagation:** GLOBAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A short-circuit at the motor holding brake terminals has been detected.  
Fault value (r0949, interpret decimal):  
Only for internal Siemens troubleshooting.

**Remedy:**
  
- check the motor holding brake for a short-circuit.  
- check the connection and cable for the motor holding brake.

### F30052 EEPROM data error

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** Power Module | **Propagation:** LOCAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
POWER ON

**Cause:**
  
EEPROM data error of the power unit module.  
Fault value (r0949, interpret decimal):  
0, 2, 3, 4:  
The EEPROM data read in from the power unit module are incorrect.  
1:  
EEPROM data is not compatible to the firmware of the power unit application.  
Additional values:  
Only for internal Siemens troubleshooting.

**Remedy:**
  
For fault value = 0, 2, 3, 4:  
Replace the power unit module or update the EEPROM data.  
For fault value = 1:  
The following applies for CU31x and CUA31:  
Update the firmware \SIEMENS\SINAMICS\CODE\SAC\cu31xi.ufw (cua31.ufw)

### A30054 Power unit: Undervoltage when opening the brake

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
%1

**Message class:**
  
Supply voltage fault (undervoltage) (3)

| Symbol | Meaning |
| --- | --- |
| **Component:** Power Module | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
When the brake is being opened, it is detected that the power supply voltage is less
than 21.4 V  
Alarm value (r2124, interpret decimal):  
Supply voltage fault [0.1 V].  
Example:  
Alarm value = 195 --&gt; voltage = 19.5 V

**Remedy:**
  
Check the 24 V voltage for stability and value.

### F30055 Power unit: Braking chopper overcurrent

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
-

**Message class:**
  
Braking Module faulted (14)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
An overcurrent condition has occurred in the braking chopper.

**Remedy:**
  
- check whether the braking resistor has a short circuit.  
- for an external braking resistor, check whether the resistor may have been dimensioned
too small.  
Note:  
The braking chopper is only enabled again at pulse enable after the fault has been
acknowledged.

### F30068 Power unit: undertemperature inverter heat sink

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
%1

**Message class:**
  
Power electronics faulted (5)

| Symbol | Meaning |
| --- | --- |
| **Component:** Power Module | **Propagation:** DRIVE |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The actual inverter heat sink temperature is below the permissible minimum value.  
Possible causes:  
- the power unit is being operated at an ambient temperature that lies below the permissible
range.  
- the temperature sensor evaluation is defective.  
Fault value (r0949, interpret decimal):  
Inverter heat sink temperature [0.1 °C].

**Remedy:**
  
- ensure that higher ambient temperatures prevail.  
- replace the power unit.

### F30075 Configuration of the power unit unsuccessful

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
%1

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** LOCAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A communication error has occurred while configuring the power unit using the Control
Unit. The cause is not clear.  
Fault value (r0949, interpret decimal):  
0:  
The output filter initialization was unsuccessful.  
1:  
Activation/deactivation of the regenerative feedback functionality was unsuccessful.  
2:  
Activation/deactivation of the chopper function was unsuccessful.

**Remedy:**
  
- acknowledge the fault and continue operation.  
- if the fault reoccurs, carry out a POWER ON (switch-off/switch-on).  
- if required, replace the power unit.

### A30076 Power unit: thermal overload internal braking resistor alarm

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
%1

**Message class:**
  
Braking Module faulted (14)

| Symbol | Meaning |
| --- | --- |
| **Component:** Power Module | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The energy absorbed by the internal braking resistor has exceeded the alarm threshold
of 80 %. If the power unit is still operated in the generator mode, then this can
reach the shutdown threshold. To avoid overheating of the braking resistor, use of
the braking resistor is inhibited and alarm A30077 is output.  
Alarm value (r2124, interpret decimal):  
Energy absorbed by the braking resistor [Ws].

**Remedy:**
  
Reduce the power when generating.  
Note:  
For a DC link coupling, the generating power of all of the coupled power units must
be taken into consideration.

### A30077 Power unit: thermal overload internal braking resistor

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
%1

**Message class:**
  
Braking Module faulted (14)

| Symbol | Meaning |
| --- | --- |
| **Component:** Power Module | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The internal braking resistor is thermally overloaded. This is the reason that its
use was inhibited.  
Alarm value (r2124, interpret decimal):  
Energy absorbed by the braking resistor [Ws].

**Remedy:**
  
Reduce the power when generating.  
Note:  
- once the internal braking resistor has thermally recovered, it is enabled for further
use.  
- for a DC link coupling, the generating power of all the coupled power units must
be taken into consideration.

### F30078 Power unit: defective fan or line reactor has overheated

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
-

**Message class:**
  
Overtemperature of the electronic components (6)

| Symbol | Meaning |
| --- | --- |
| **Component:** Power Module | **Propagation:** LOCAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The temperature monitoring of the internal braking resistor or the line reactor has
responded. In addition to the OFF2 response, the use of the internal braking resistor
was inhibited.  
Note:  
- an overtemperature condition of the internal braking resistor can only be initiated
as a result of a defective fan.  
- an overtemperature condition of the line reactor can occur when a DC link coupling
is used – and if the power when motoring, which is fed into the DC link - is not evenly
distributed across the rectifiers of the power units.

**Remedy:**
  
- check the converter fan and replace if necessary.  
- reduce the motoring power.

### A30079 Power unit: referred to the supply voltage, the DC link voltage is too high

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
%1

**Message class:**
  
Infeed faulted (13)

| Symbol | Meaning |
| --- | --- |
| **Component:** Power Module | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The alarm is output if the following conditions are simultaneously satisfied:  
1. The device supply voltage (p0210) was reduced.  
2. A DC link voltage is present, which is too high when referred to the new supply
voltage.  
DC link precharging cannot be completed as this could place some converter components
at risk.  
Alarm value (r2124, interpret decimal):  
Voltage value to which the DC link voltage must, in the meantime, be reduced in order
to complete precharging [V].  
See also: p0210 (Drive unit line supply voltage)

**Remedy:**
  
As a minimum, reduce the DC link voltage to the voltage specified in the alarm value.  
Note:  
The alarm is automatically withdrawn if the DC link voltage drops below the voltage
specified in the alarm value.  
Fault F07802 is output if an attempt is made to enable the pulses even though an alarm
is active.

### A30502 Power unit: DC link overvoltage

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
%1

**Message class:**
  
DC link overvoltage (4)

| Symbol | Meaning |
| --- | --- |
| **Component:** Power Module | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The power unit has detected overvoltage in the DC link on a pulse inhibit.  
- device supply voltage too high.  
- line reactor incorrectly dimensioned.  
Alarm value (r0949, interpret decimal):  
DC link voltage [1 bit = 100 mV].  
See also: r0070 (Actual DC link voltage)

**Remedy:**
  
- check the device supply voltage (p0210).  
- check the dimensioning of the line reactor.  
See also: p0210 (Drive unit line supply voltage)

### F30600 SI P2: STO initiated

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
%1

**Message class:**
  
Safety monitoring channel has identified an error (10)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The "Safety Integrated" function integrated in the drive has identified a fault in
monitoring channel 2, and has initiated STO.  
- forced checking procedure (test stop) of the safety switch-off signal path of monitoring
channel 2 unsuccessful.  
- subsequent response to fault F30611 (defect in a monitoring channel).  
Fault value (r0949, interpret decimal):  
0: Stop request from another monitoring channel.  
1005: STO active, although no STO is selected and no stop response with STO is active.  
1010: STO inactive, although STO is selected or a stop response with STO is active.  
1011: internal error for STO deselected in monitoring channel 2.  
9999: Subsequent response to fault F30611.

**Remedy:**
  
- select Safe Torque Off and deselect again.  
- carry out a POWER ON (switch-off/switch-on) for all components.  
- replace drive.  
For fault value = 9999:  
- carry out diagnostics for fault F30611.  
Note:  
SI: Safety Integrated  
STO: Safe Torque Off

### F30611 SI P2: Defect in a monitoring channel

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
%1

**Message class:**
  
Safety monitoring channel has identified an error (10)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The "Safety Integrated" function integrated in the drive has identified a fault in
monitoring channel 2. As a result of this fault, after the parameterized transition
time has elapsed (p9658), fault F01600 is output.  
Fault value (r0949, interpret decimal):  
0: Stop request from another monitoring channel.  
1 ... 999:  
Number of the cross-compared data that resulted in this fault.  
2: SI enable safety functions (p9601). Crosswise data comparison is only carried out
for the supported bits.  
3: SI SGE changeover discrepancy time (p9650).  
4: SI transition time from F01611 to STO (p9658).  
5: SI enable Safe Brake Control (p9602).  
6: SI Motion enable safety functions (p9501).  
7: SI delay time of STO for Safe Stop 1 (p9652).  
8: SI PROFIsafe address (p9610).  
9: SI debounce time for STO/SBC/SS1 (p9651).  
14: SI PROFIsafe telegram selection (p9611).  
15: SI PROFIsafe bus failure response (p9612).  
1000: Watchdog timer has expired.  
Within the time of approx. 5 x p9650, alternatively, the following was defined:  
- the signal at F-DI for STO continually changes with time intervals less than or
equal to the discrepancy time (p9650).  
- via PROFIsafe, STO (also as subsequent response) was continually selected and deselected
with time intervals less than or equal to the discrepancy time (p9650).  
1001, 1002: Initialization error, change timer / check timer.  
1950: Module temperature outside the permissible temperature range.  
1951: Module temperature not plausible.  
2000: Status of the STO selection for both monitoring channels different.  
2001: Feedback signal of STO shutdown for both monitoring channels different. This
value can also subsequently occur as a result of other faults.  
2002: Status of the delay timer SS1 on both monitoring channels are different (status
of the timer in p9650).  
2003: Status of the STO terminal for both monitoring channels different.  
6000 ... 6999:  
Error in the PROFIsafe control.  
For these fault values, the failsafe control signals (Failsafe Values) are transferred
to the safety functions. For p9612 = 1, the transfer of Failsafe Values is delayed.  
The significance of the individual message values is defined in message F01611.

**Remedy:**
  
For fault value = 1 ... 5 and 7 ... 999:  
- check the data that caused the fault.  
- upgrade the drive software.  
- carry out a POWER ON (switch-off/switch-on).  
For fault value = 1000:  
- check the wiring of the safety-relevant inputs (SGE) in the first monitoring channel
(contact problems).  
- PROFIsafe: Resolve contact problems/faults at the PROFINET controller.  
- check the discrepancy time, and if required, increase the value (p9650).  
For fault value = 1001, 1002:  
- carry out a POWER ON (switch-off/switch-on).  
- upgrade the drive software.  
For fault value = 1950:  
- operate the module in the permissible range.  
- test module fan, replace drive.  
For fault value = 1951:  
- operate the module in the permissible range.  
- replace drive.  
For fault value = 2000, 2001, 2002, 2003:  
- check the discrepancy time, and if required, increase the value (p9650, p9652).  
- check the wiring of the F-DI for STO/SBC/SS1 (contact problems).  
- replace drive.  
- diagnose the other active faults and resolve the causes.  
Note:  
This fault can be acknowledged after removing the cause of the error and after correct
selection/deselection of STO.  
For fault value = 6000 ... 6999:  
Refer to the description of the message values for safety message F01611.  
Note:  
SGE: Safety-relevant input  
F-DI: Failsafe Digital Input  
SI: Safety Integrated  
SS1: Safe Stop 1  
STO: Safe Torque Off

### N30620 SI P2: Safe Torque Off active

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
-

**Message class:**
  
Safety monitoring channel has identified an error (10)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The "Safe Torque Off" (STO) function of the basic functions has been selected in monitoring
channel 2 using the input terminal and is active.  
Note:  
- this message does not result in a safety stop response.  
- this message is not output when STO is selected using the Extended Functions.

**Remedy:**
  
Not necessary.  
Note:  
SI: Safety Integrated  
STO: Safe Torque Off

### N30621 SI P2: Safe Stop 1 active

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
-

**Message class:**
  
Safety monitoring channel has identified an error (10)

| Symbol | Meaning |
| --- | --- |
| **Component:** Power Module | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The "Safe Stop 1" function (SS1) was selected in monitoring channel 2 and is active.  
Note:  
This message does not result in a safety stop response.

**Remedy:**
  
Not necessary.  
Note:  
SI: Safety Integrated  
SS1: Safe Stop 1

### F30625 SI P2: Sign-of-life error in safety data

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The "Safety Integrated" function integrated in the drive has identified an error in
the sign-of-life of the safety data in monitoring channel 2, and has initiated STO.  
- there is either a DRIVE-CLiQ communication error or communication has failed.  
- a time slice overflow of the safety software has occurred.  
- the enable of the safety functions in both monitoring channels is inconsistent.  
Fault value (r0949, interpret decimal):  
Only for internal Siemens troubleshooting.

**Remedy:**
  
- select STO and then deselect again.  
- carry out a POWER ON (switch-off/switch-on).  
- check whether there is a DRIVE-CLiQ communication error between the two monitoring
channels and, if required, carry out a diagnostics routine for the faults identified.  
- deselect all drive functions that are not absolutely necessary.  
- check the electrical cabinet design and cable routing for EMC compliance  
- check whether the safety functions are enabled (p9601), copy the safety parameters
using the commissioning tool, and confirm the data change.  
Note:  
P2: processor 2  
SI: Safety Integrated  
STO: Safe Torque Off

### F30630 SI P2: Brake control error

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
%1

**Message class:**
  
Safety monitoring channel has identified an error (10)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The "Safety Integrated" function integrated in the drive has identified a brake control
fault in monitoring channel 2, and has initiated STO.  
- OCC cable shield is not correctly connected.  
- defect in the brake control circuit of the drive.  
Fault value (r0949, interpret decimal):  
100, 101, 102:  
Fault in "open brake" operation.  
- brake not closed or interrupted cable.  
- ground fault in brake cable.  
300, 301, 302:  
Fault in "close brake" operation.  
- brake not closed or interrupted cable.  
200, 201, 202:  
Fault in the "Brake open" state.  
- short-circuit in brake winding.  
- defective hardware.  
400, 401, 402:  
Fault in "brake closed" state.  
60, 70:  
Fault in the brake control of the drive or a communication error between the monitoring
channels (brake control diagnostics).

**Remedy:**
  
- select STO and then deselect again.  
- check the motor holding brake connection.  
- check the function of the motor holding brake.  
- carry out a diagnostics routine for the faults involved.  
- check for EMC-compliant control cabinet design and cable routing (e.g. shield OCC
cable with shield terminal and shield plate, check the connection of the brake conductors).  
- replace drive.  
Note:  
OCC: One Cable Connection (one cable system)  
SBC: Safe Brake Control  
SI: Safety Integrated  
STO: Safe Torque Off

### F30649 SI P2: Internal software error

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** Power Module | **Propagation:** LOCAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
An internal error in the Safety Integrated software in monitoring channel 2 has occurred.  
Note:  
This fault results in an STO that cannot be acknowledged.  
Fault value (r0949, interpret hexadecimal):  
Only for internal Siemens troubleshooting.

**Remedy:**
  
- carry out a POWER ON (switch-off/switch-on).  
- re-commission the "Safety Integrated" function and carry out a POWER ON.  
- upgrade the drive firmware to a later version.  
- contact Technical Support.  
- replace drive.  
Note:  
SI: Safety Integrated  
STO: Safe Torque Off

### F30650 SI P2: Acceptance test required

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

| Symbol | Meaning |
| --- | --- |
| **Component:** Power Module | **Propagation:** LOCAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The "Safety Integrated" function on monitoring channel 2 requires an acceptance test.  
Note:  
This fault results in an STO that can be acknowledged.  
Fault value (r0949, interpret decimal):  
130: Safety parameters for monitoring channel 2 not available.  
Note:  
This fault value is always output when Safety Integrated is commissioned for the first
time.  
1000: Reference and actual checksum in monitoring channel 2 are not identical (booting).  
- safety parameters set offline and loaded to the drive.  
- at least one checksum-checked piece of data is defective.  
2000: Reference and actual checksum in monitoring channel 2 are not identical (commissioning
mode).  
2003: Acceptance test is required as a safety parameter has been changed.  
3003: Acceptance test is required as a hardware-related safety parameter has been
changed.  
9999: Subsequent response of another safety-related fault that occurred when booting
that requires an acceptance test.

**Remedy:**
  
For fault value = 130:  
- carry out safety commissioning routine.  
For fault value = 1000:  
- again carry out safety commissioning routine.  
- replace the memory card or drive.  
For fault value = 2000:  
- confirm the data change using the commissioning tool.  
For fault value = 2003:  
- carry out an acceptance test and generate an acceptance report.  
For fault value = 3003:  
- carry out the function checks for the modified hardware and generate an acceptance
report.  
For fault value = 9999:  
- carry out diagnostics for the other safety-related fault that is present.  
Note:  
SI: Safety Integrated  
STO: Safe Torque Off

### F30651 SI P2: synchronization with monitoring channel 1 unsuccessful

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The "Safety Integrated" function requires synchronization of the safety time slices
in both monitoring channels. This synchronization routine was unsuccessful.  
Note:  
This fault results in an STO that cannot be acknowledged.  
Fault value (r0949, interpret decimal):  
Only for internal Siemens troubleshooting.

**Remedy:**
  
- carry out a POWER ON (switch-off/switch-on).  
- upgrade the drive software.  
Note:  
SI: Safety Integrated  
STO: Safe Torque Off

### F30655 SI P2: Align monitoring functions

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
%1

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
  
An error has occurred when aligning the Safety Integrated monitoring functions of
both monitoring channels. No common set of supported SI monitoring functions was able
to be determined.  
- there is either a DRIVE-CLiQ communication error or communication has failed.  
Note:  
This fault results in an STO that cannot be acknowledged.  
Fault value (r0949, interpret hexadecimal):  
Only for internal Siemens troubleshooting.

**Remedy:**
  
- carry out a POWER ON (switch-off/switch-on) for all components.  
- upgrade the drive software.  
- check the electrical cabinet design and cable routing for EMC compliance  
Note:  
SI: Safety Integrated  
STO: Safe Torque Off

### F30656 SI P2: Parameter error monitoring channel 2

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** LOCAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
When accessing the Safety Integrated parameters for monitoring channel 2 in the non-volatile
memory, an error has occurred.  
Note:  
This fault results in an STO that can be acknowledged.  
Fault value (r0949, interpret decimal):  
129:  
- safety parameters for monitoring channel 2 corrupted.  
131: Internal software error of monitoring channel 1.  
255: Internal software error of monitoring channel 2.

**Remedy:**
  
- re-commission the safety functions.  
- upgrade the drive software.  
- replace the memory card or drive.  
For fault value = 129:  
- activate the Safety Integrated commissioning mode.  
- adapt the PROFIsafe address.  
- copy the safety parameters and confirm the data change.  
- exit the Safety Integrated commissioning mode.  
- save all parameters or "Copy RAM to ROM".  
- carry out a POWER ON (switch-off/switch-on).  
Note:  
SI: Safety Integrated  
STO: Safe Torque Off

### F30657 SI P2: PROFIsafe telegram number invalid

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

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
  
The PROFIsafe telegram number that has been set is not valid.  
When PROFIsafe is enabled (p9601.3 = 1), then telegram number 30 or 901 must be used.  
The copy function was not used.  
Note:  
This fault does not result in a safety stop response.  
See also: p9611 (SI PROFIsafe telegram selection), r60022 (PROFIsafe telegram selection)

**Remedy:**
  
Enter a valid PROFIsafe telegram number (p9611 = 30, 901).

### F30659 SI P2: Write request for parameter rejected

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
%1

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
  
The write request for one or several Safety Integrated parameters in monitoring channel
2 was rejected.  
Note:  
See also fault F01659.

**Remedy:**
  
Upgrade the firmware to later version.

### F30674 SI Motion P2: Safety function not supported by PROFIsafe telegram

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
%1

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
  
The monitoring function enabled in p9501 and p9601 is not supported by the currently
set PROFIsafe telegram (p9611).  
Note:  
This fault does not result in a safety stop response.  
Fault value (r0949, interpret bitwise binary):  
Bit 18 = 1:  
SS2E via PROFIsafe is not supported (p9501.18).  
Bit 24 = 1:  
Transfer SLS limit value via PROFIsafe not supported (p9501.24).

**Remedy:**
  
- Deselect the monitoring function involved (p9501, p9601).  
- set the matching PROFIsafe telegram (p9611).  
- using the commissioning tool, copy the safety parameters and confirm the data change.  
Note:  
SI: Safety Integrated  
SLS: Safely-Limited Speed  
SS2E: Safe Stop 2 External (Safe Stop 2 with external stop)

### F30680 SI Motion P2: Checksum error safety monitoring functions

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
%1

**Message class:**
  
Safety monitoring channel has identified an error (10)

| Symbol | Meaning |
| --- | --- |
| **Component:** Power Module | **Propagation:** GLOBAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The calculated actual checksum over the safety-relevant parameters does not match
the reference checksum saved at the last machine acceptance.  
Safety-relevant parameters have been changed or a fault is present.  
Note:  
This fault results in an STO that can be acknowledged.  
Fault value (r0949, interpret decimal):  
0: Checksum error for SI parameters for motion monitoring.  
1: Checksum error for SI parameters for component assignment.

**Remedy:**
  
- check the safety-relevant parameters and if required, correct.  
- execute the function "Copy RAM to ROM".  
- if necessary carry out a POWER ON (switch-off/switch-on).  
- carry out an acceptance test.  
Note:  
STO: Safe Torque Off

### F30681 SI Motion P1: Incorrect parameter value

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
Parameter: %1, supplementary information: %2

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
  
An internal parameter is not correctly set.  
This message does not result in a safety stop response.  
Fault value (r0949, interpret decimal):  
Only for internal Siemens diagnostics.

**Remedy:**
  
- resolve the cause of message F01681.  
- complete the Safety commissioning.

### F30682 SI Motion P2: Monitoring function not supported

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
%1

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
  
The monitoring function enabled in p9501, p9506, p9507, p9601 is not supported in
this firmware version.  
Note:  
This message does not result in a safety stop response.  
Fault value (r0949, interpret decimal):  
Monitoring function not supported.

**Remedy:**
  
- deselect the monitoring function involved (p9501, p9506, p9507, p9601).  
- restore the factory setting and repeat commissioning.  
- upgrade the firmware.  
Note:  
SI: Safety Integrated  
See also: p9501 (SI Motion enable safety functions), p9601 (SI enable, functions integrated
in the drive)

### F30683 SI Motion P2: SOS/SLS enable missing

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

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
  
IMMEDIATELY

**Cause:**
  
The safety-relevant basic function "SOS/SLS" is not enabled, although other safety-relevant
monitoring functions are enabled.  
Note:  
This message does not result in a safety stop response.

**Remedy:**
  
Using the commissioning tool, copy the safety parameters, confirm the data change
and carry out a power on.  
Note:  
SI: Safety Integrated  
SLS: Safely-Limited Speed  
SOS: Safe Operating Stop

### F30685 SI Motion P2: Safely-Limited Speed limit value too high

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
%1

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
  
The limit value for the function "Safely-Limited Speed" (SLS) is greater than the
speed that corresponds to an encoder limit frequency of 500 kHz.  
Note:  
This message does not result in a safety stop response.  
Fault value (r0949, interpret decimal):  
Maximum permissible speed.

**Remedy:**
  
Correct the limit values for SLS and carry out a POWER ON.  
Note:  
SI: Safety Integrated  
SLS: Safely-Limited Speed

### A30693 SI P2: Safety parameter settings changed, warm restart/POWER ON required

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

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
  
Safety parameters have been changed; these will only take effect following a warm
restart or POWER ON.  
Alarm value (r2124, interpret decimal):  
Only for internal Siemens diagnostics.

**Remedy:**
  
- carry out a warm restart.  
- carry out a POWER ON (switch-off/switch-on).  
Note:  
A POWER ON is required before carrying out the acceptance test.

### F30700 SI Motion P2: STO initiated

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
-

**Message class:**
  
Safety monitoring channel has identified an error (10)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The drive is stopped using STO.  
Possible causes:  
- stop request from another monitoring channel.  
- STO not active after parameterized time after test stop selection.  
- subsequent response, following messages: A30706, A30714, F30701, A30716

**Remedy:**
  
- remove the cause of the fault on the first monitoring channel.  
- check the switch-off signal path of the first of monitoring channel (check DRIVE-CLiQ
communication).  
- carry out diagnostics for the active messages (A30706, A30714, F30701, A30716).  
- replace drive.  
Note:  
SAM: Safe Acceleration Monitor (safe acceleration monitoring)  
SI: Safety Integrated  
STO: Safe Torque Off

### F30701 SI Motion P2: SS1 initiated

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
-

**Message class:**
  
Safety monitoring channel has identified an error (10)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The drive is stopped using SS1.  
As a result of this fault, after the time parameterized in p9556 has expired, or the
speed threshold parameterized in p9560 has been fallen below, message F30700 "SI Motion
P2: STO initiated" is output.  
Possible causes:  
- stop request from another monitoring channel.  
- subsequent response, following messages: A30714, A30711, A30707, A30716

**Remedy:**
  
- remove the cause of the fault on the first monitoring channel.  
- carry out diagnostics for the active messages (A30714, A30711, A30707, A30716).  
Note:  
SI: Safety Integrated  
SS1: Safe Stop 1

### A30706 SI Motion P2: SAM/SBR limit exceeded

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
-

**Message class:**
  
Safety monitoring channel has identified an error (10)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
Motion monitoring functions with encoder (SAM, p9506 = 0):  
- after initiating SS1 or SS2, the speed exceeded the set tolerance.  
Motion monitoring functions with encoder (SBR, p9506 = 2):  
- after initiating SS1 or SLS switchover to the lower speed level, the speed exceeded
the set tolerance.  
The drive is stopped by message F30700.

**Remedy:**
  
Check the braking behavior and, if necessary, adapt the parameterization of the parameter
settings of the "SAM" or the "SBR" function.  
Note:  
This message can be acknowledged via PROFIsafe (safe acknowledgment).  
SAM: Safe Acceleration Monitor (safe acceleration monitoring)  
SBR: Safe Brake Ramp (safe ramp monitoring)  
SI: Safety Integrated  
SS1: Safe Stop 1  
SS2: Safe Stop 2  
SLS: Safely-Limited Speed  
See also: p9548 (SI Motion SAM actual speed tolerance)

### A30707 SI Motion P2: Tolerance for safe operating stop exceeded

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
-

**Message class:**
  
Safety monitoring channel has identified an error (10)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The actual position has moved further away from the target position than the standstill
tolerance.  
The drive is stopped by message F30701.

**Remedy:**
  
- check whether safety faults are present and if required carry out the appropriate
diagnostic routines for the particular faults.  
- check whether the standstill tolerance matches the accuracy and control dynamic
performance of the axis.  
- carry out a POWER ON (switch-off/switch-on).  
Note:  
SI: Safety Integrated  
SOS: Safe Operating Stop  
See also: p9530 (SI Motion standstill tolerance)

### F30708 SI Motion P2: SS2 initiated

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
-

**Message class:**
  
Safety monitoring channel has identified an error (10)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 STOP2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The drive is stopped using SS2 (braking along the OFF3 down ramp).  
"Safe Operating Stop" (SOS) is activated after the parameterized time has expired.  
Possible causes:  
Subsequent response, following messages: A30714, A30716  
See also: p9552 (SI Motion transition time SS2 to SOS)

**Remedy:**
  
Carry out diagnostics for the active messages (A30714, A30716).  
Note:  
SI: Safety Integrated  
SOS: Safe Operating Stop  
SS2: Safe Stop 2

### A30709 SI Motion P2: SS2E initiated

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
-

**Message class:**
  
Safety monitoring channel has identified an error (10)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The drive is stopped using SS2E (braking along a path).  
"Safe Operating Stop" (SOS) is activated after the parameterized time has expired.  
Possible causes:  
Subsequent response, following messages: A30714, A30716  
See also: p9553 (SI Motion transition time SS2E to SOS)

**Remedy:**
  
- remove the cause of the fault at the control.  
- carry out diagnostics for the active messages (A30714, A30716).  
Note:  
SI: Safety Integrated  
SOS: Safe Operating Stop  
SS2E: Safe Stop 2 External (Safe Stop 2 with external stop)

### A30711 SI Motion P2: Defect in a monitoring channel

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
%1

**Message class:**
  
Safety monitoring channel has identified an error (10)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The drive has identified a difference between the input data or results of the monitoring
functions and initiated A30711. Safe operation is no longer possible.  
At least one monitoring function is active, so that after the parameterized timer
has expired, message F30701 is output.  
The following message values may also occur in the following cases if the cause that
is explicitly mentioned does not apply:  
- incorrect synchronization.  
Message value (r2124, interpret decimal):  
0 ... 999:  
Number of the cross-compared data that resulted in this message.  
The significance of the individual message values is described in message A01711.  
1000: Watchdog timer has expired. Too many signal changes have occurred at safety-relevant
inputs.  
1001: Initialization error of watchdog timer.  
1005: STO already active for test stop selection.  
1011: Acceptance test status between the monitoring channels differ.  
1012: Plausibility violation of the encoder actual value.  
1020: Cyc. communication failure between the monit. channels.  
1021: Cyclic communication failure between the monitoring channel and encoder evaluation.  
1023: Error in the effectiveness test in the DRIVE-CLiQ encoder  
1030: Encoder fault detected from another monitoring channel.  
1045: CRC of the standstill position incorrect.  
5000 ... 5140:  
PROFIsafe message values.  
For these message values, the failsafe control signals (Failsafe Values) are transferred
to the safety functions.  
The significance of the individual message values is described in message A01711.  
6000 ... 6166:  
PROFIsafe message values (PROFIsafe driver for PROFIBUS DP V1/V2 and PROFINET).  
For these message values, the failsafe control signals (Failsafe Values) are transferred
to the safety functions. If "SS1 after failure of PROFIsafe communication" is parameterized,
then transfer of the Failsafe Values is delayed.  
The significance of the individual message values is described in safety fault F01611.  
See also: p9555 (SI Motion transition time A01711 to SS1), r9725 (SI Motion diagnostics A01711)

**Remedy:**
  
For message value = 1005:  
- check the conditions for deselecting STO.  
For message value = 1012:  
- upgrade the encoder evaluation firmware to a newer version.  
- check encoder parameters to ensure that they are the same (p9515, p9519, p9523,
p9524, p9525, p9529).  
- start the copy function for encoder parameters (commissioning tool).  
- the parameterized encoder does not correspond to the connected encoder - replace
the encoder.  
- check the electrical cabinet design and cable routing for EMC compliance  
- carry out a POWER ON (switch off/switch on) or a warm restart (p0009 = 30, p0976
= 2, 3).  
- replace the hardware.  
For message value = 1024:  
- check the communication link.  
- carry out a POWER ON (switch off/switch on) or a warm restart (p0009 = 30, p0976
= 2, 3).  
- replace the hardware.  
For message value = 1030:  
- check the encoder connection.  
- if required, replace the encoder.  
Adapt the encoder parameterization for the second channel as follows:  
- activate the safety commissioning mode (p0010 = 95).  
- start the copy function for encoder parameters (commissioning tool).  
- exit the safety commissioning mode (p0010 = 0).  
- save the parameters in a non-volatile fashion (copy RAM to ROM).  
- carry out a POWER ON (switch off/switch on) or a warm restart (p0009 = 30, p0976
= 2, 3).  
The following always applies:  
- check the encoder connection.  
- if required, replace the encoder.  
For message value = 6000 ... 6999:  
- the significance of the individual message values are described in fault F01611.  
For other message values:  
- the significance of the individual message values is described in message A01711.  
Note:  
SI: Safety Integrated  
SS1: Safe Stop 1

### A30714 SI Motion P2: Safely-Limited Speed exceeded

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
%1

**Message class:**
  
Safety monitoring channel has identified an error (10)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The drive had moved faster than that specified by the velocity limit value. The drive
is stopped by the configured stop response.  
Message value (r2124, interpret decimal):  
100: SLS1 exceeded.  
200: SLS2 exceeded.  
300: SLS3 exceeded.  
400: SLS4 exceeded.  
1000: Encoder limit frequency exceeded.

**Remedy:**
  
- check the traversing/motion program in the control.  
- check the limits for the "SLS" function and if required adapt.  
Note:  
SI: Safety Integrated  
SLS: Safely-Limited Speed

### A30716 SI Motion P2: Tolerance for safe motion direction exceeded

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
%1

**Message class:**
  
Safety monitoring channel has identified an error (10)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The tolerance for the "safe motion direction" function was exceeded. The drive is
stopped by the configured stop response.  
Message value (r2124, interpret decimal):  
0: Tolerance for function "safe motion direction positive" exceeded.  
1: Tolerance for function "safe motion direction negative" exceeded.

**Remedy:**
  
- check the traversing/motion program in the control.  
- check the tolerance for the "SDI" function and adapt if necessary.  
This message can be acknowledged as follows:  
Deselect/select SDI and perform safe acknowledgment via PROFIsafe.  
Note:  
SDI: Safe Direction (safe motion direction)  
SI: Safety Integrated

### A30730 SI Motion P2: Reference block for dynamic Safely-Limited Speed invalid

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
%1

**Message class:**
  
Safety monitoring channel has identified an error (10)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The reference block transferred via PROFIsafe is negative.  
A reference block is used to generate a referred velocity limit value based on the
reference quantity "Velocity limit value SLS1" (p9531[0]).  
The drive is stopped by the configured stop response (p9563[0]).  
Message value (r2124, interpret decimal):  
requested, invalid reference block.

**Remedy:**
  
In the PROFIsafe telegram, input data S_SLS_LIMIT_IST must be corrected.  
This message can be acknowledged without a POWER ON as follows (safe acknowledgment):  
- PROFIsafe.  
Note:  
SI: Safety Integrated  
SLS: Safely-Limited Speed

### A30788 Automatic test stop: wait for STO deselection via SMM

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
-

**Message class:**
  
Safety monitoring channel has identified an error (10)

| Symbol | Meaning |
| --- | --- |
| **Component:** Motor | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The automatic test stop was not able to be carried out after powering up.  
Possible causes:  
- the STO function is selected via Safety Extended Functions.  
- a safety message is present, that resulted in a STO.  
Note:  
STO: Safe Torque Off

**Remedy:**
  
- Deselect STO via Safety Extended Functions.  
- remove the cause of the safety messages and acknowledge the messages.  
Note:  
The automatic test stop is performed after removing the cause.

### A30798 SI Motion P2: Test stop for motion monitoring functions running

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
-

**Message class:**
  
Safety monitoring channel has identified an error (10)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The forced checking procedure (test stop) for the safe motion monitoring functions
is currently in progress.

**Remedy:**
  
Not necessary.  
The message is automatically withdrawn when the test stop has been completed.  
Note:  
SI: Safety Integrated

### A30799 SI Motion P2: Acceptance test mode active

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
-

**Message class:**
  
Safety monitoring channel has identified an error (10)

| Symbol | Meaning |
| --- | --- |
| **Component:** None | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
The acceptance test mode is active.  
This means that the setpoint speed limiting is deactivated (r9733).

**Remedy:**
  
Not necessary.  
The message is automatically withdrawn when exiting the acceptance test mode.  
Note:  
SI: Safety Integrated

### N30800 Power unit: Group signal

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

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

### F30805 Power unit: EEPROM checksum error

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** Power Module | **Propagation:** LOCAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
Internal parameter data is corrupted.  
Fault value (r0949, interpret decimal):  
01: EEPROM access error.  
02: Too many blocks in the EEPROM.  
03: Safety EEPROM data error.  
...  
20: Safety EEPROM data error.

**Remedy:**
  
Replace the power unit involved.

### F30895 power module DRIVE-CLiQ: Alternating cyclic data transfer error

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** Power Module | **Propagation:** LOCAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A DRIVE-CLiQ communication error has occurred from the power unit to the Control Unit
involved.  
Fault cause:  
11 (= 0B hex):  
Synchronization error during alternating cyclic data transfer.  
Note regarding the message value:  
The individual information is coded as follows in the message value (r0949/r2124):  
0000yyxx hex: yy = component number, xx = error cause

**Remedy:**
  
Carry out a POWER ON (switch-off/switch-on).

### F30899 Power unit: Unknown fault

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
New message: %1

**Message class:**
  
Power electronics faulted (5)

| Symbol | Meaning |
| --- | --- |
| **Component:** Power Module | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A fault occurred on the power unit that cannot be interpreted by the Control Unit
firmware.  
This can occur if the firmware on this component is more recent than the firmware
on the Control Unit.  
Fault value (r0949, interpret decimal):  
Fault number.  
Note:  
If required, the significance of this new fault can be read about in a more recent
description of the Control Unit.

**Remedy:**
  
- replace the firmware on the power unit by an older firmware version (r0128).  
- upgrade the firmware on the Control Unit (r0018).

### F30950 Power unit: Internal software error

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** Power Module | **Propagation:** LOCAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
POWER ON

**Cause:**
  
An internal software error has occurred.  
Fault value (r0949, interpret decimal):  
Information about the fault source.  
Only for internal Siemens troubleshooting.

**Remedy:**
  
- if necessary, upgrade the firmware in the power unit to a later version.  
- contact Technical Support.

### A30999 Power unit: Unknown alarm

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
New message: %1

**Message class:**
  
Power electronics faulted (5)

| Symbol | Meaning |
| --- | --- |
| **Component:** Power Module | **Propagation:** LOCAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
An alarm occurred on the power unit that cannot be interpreted by the Control Unit
firmware.  
This can occur if the firmware on this component is more recent than the firmware
on the Control Unit.  
Alarm value (r2124, interpret decimal):  
Alarm number.  
Note:  
If required, the significance of this new alarm can be read about in a more recent
description of the Control Unit.

**Remedy:**
  
- replace the firmware on the power unit by an older firmware version (r0128).  
- upgrade the firmware on the Control Unit (r0018).

### F31120 Encoder 1: Encoder power supply fault

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
Fault cause: %1 bin

**Message class:**
  
Actual position/speed value incorrect or not available (11)

| Symbol | Meaning |
| --- | --- |
| **Component:** Encoder 1 | **Propagation:** LOCAL |

  

**Reaction:**
  
 ENCODER

**Acknowledge:**
  
PULSE INHIBIT

**Cause:**
  
An encoder power supply fault was detected.  
Fault value (r0949, interpret binary):  
Bit 0: Undervoltage condition on the sense line.  
Bit 1: Overcurrent condition for the encoder power supply.  
Bit 2: Overcurrent condition for encoder power supply on cable resolver excitation
negative.  
Bit 3: Overcurrent condition for encoder power supply on cable resolver excitation
positive.  
Bit 4: The 24 V power supply through the Power Module (PM) is overloaded.  
Bit 5: Overcurrent at the EnDat connection of the converter.  
Bit 6: Overvoltage at the EnDat connection of the converter.  
Bit 7: Hardware fault at the EnDat connection of the converter.  
Note:  
If the encoder cables 6FX2002-2EQ00-.... and 6FX2002-2CH00-.... are interchanged,
this can result in the encoder being destroyed because the pins of the operating voltage
are reversed.

**Remedy:**
  
For fault value, bit 0 = 1:  
- correct encoder cable connected?  
- check the plug connections of the encoder cable.  
- SMC30: Check the parameterization (p0404.22).  
For fault value, bit 1 = 1:  
- correct encoder cable connected?  
- replace the encoder or encoder cable.  
For fault value, bit 2 = 1:  
- correct encoder cable connected?  
- replace the encoder or encoder cable.  
For fault value, bit 3 = 1:  
- correct encoder cable connected?  
- replace the encoder or encoder cable.  
For fault value, bit 5 = 1:  
- Measuring unit correctly connected at the converter?  
- Replace the measuring unit or the cable to the measuring unit.  
For fault value, bit 6, 7 = 1:  
- Replace the defective EnDat 2.2 converter.

### F31135 Encoder 1: Fault when determining the position (single turn)

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
Fault cause: %1 bin

**Message class:**
  
Actual position/speed value incorrect or not available (11)

| Symbol | Meaning |
| --- | --- |
| **Component:** Encoder 1 | **Propagation:** GLOBAL |

  

**Reaction:**
  
 ENCODER

**Acknowledge:**
  
PULSE INHIBIT

**Cause:**
  
The encoder has identified a position determination fault (singleturn) and supplies
status information bit by bit in an internal status/fault word.  
Some of these bits cause this fault to be triggered. Other bits are status displays.
The status/fault word is displayed in the fault value.  
Note regarding the bit designation:  
The first designation is valid for DRIVE-CLiQ encoders, the second for EnDat 2.2 encoders.  
Fault value (r0949, interpret binary):  
Bit 0: F1 (safety status display).  
Bit 1: F2 (safety status display).  
Bit 2: Reserved (lighting).  
Bit 3: Reserved (signal amplitude).  
Bit 4: Reserved (position value).  
Bit 5: Reserved (overvoltage).  
Bit 6: Reserved (undervoltage)/hardware fault EnDat supply (--&gt; F3x110, x = 1, 2,
3).  
Bit 7: Reserved (overcurrent)/EnDat encoder withdrawn when not in the parked state
(--&gt; F3x110, x = 1, 2, 3).  
Bit 8: Reserved (battery)/overcurrent EnDat supply (--&gt; F3x110, x = 1, 2, 3).  
Bit 9: Reserved/overvoltage EnDat supply (--&gt; F3x110, x = 1, 2, 3).  
Bit 11: Reserved/internal communication error (--&gt; F3x110, x = 1, 2, 3).  
Bit 12: Reserved/internal communication error (--&gt; F3x110, x = 1, 2, 3).  
Bit 13: Reserved/internal communication error (--&gt; F3x110, x = 1, 2, 3).  
Bit 14: Reserved/internal communication error (--&gt; F3x110, x = 1, 2, 3).  
Bit 15: Internal communication error (--&gt; F3x110, x = 1, 2, 3).  
Bit 16: Lighting (--&gt; F3x135, x = 1, 2, 3).  
Bit 17: Signal amplitude (--&gt; F3x135, x = 1, 2, 3).  
Bit 18: Singleturn position 1 (--&gt; F3x135, x = 1, 2, 3).  
Bit 19: Overvoltage (--&gt; F3x135, x = 1, 2, 3).  
Bit 20: Undervoltage (--&gt; F3x135, x = 1, 2, 3).  
Bit 21: Overcurrent (--&gt; F3x135, x = 1, 2, 3).  
Bit 22: Temperature exceeded (--&gt; F3x405, x = 1, 2, 3).  
Bit 23: Singleturn position 2 (safety status display).  
Bit 24: Singleturn system (--&gt; F3x135, x = 1, 2, 3).  
Bit 25: Singleturn power down (--&gt; F3x135, x = 1, 2, 3)  
Bit 26: Multiturn position 1 (--&gt; F3x136, x = 1, 2, 3).  
Bit 27: Multiturn position 2 (--&gt; F3x136, x = 1, 2, 3).  
Bit 28: Multiturn system (--&gt; F3x136, x = 1, 2, 3).  
Bit 29: Multiturn power down (--&gt; F3x136, x = 1, 2, 3).  
Bit 30: Multiturn overflow/underflow (--&gt; F3x136, x = 1, 2, 3).  
Bit 31: Multiturn battery (reserved).

**Remedy:**
  
- determine the detailed cause of the fault using the fault value.  
- replace the encoder if necessary.  
Note:  
An EnDat 2.2 encoder may only be removed and inserted in the "Park" state.  
If an EnDat 2.2 encoder was removed when not in the "Park" state, then after inserting
the encoder, a POWER ON (switch-off/switch-on) is necessary to acknowledge the fault.

### F31136 Encoder 1: Fault when determining the position (multiturn)

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
Fault cause: %1 bin

**Message class:**
  
Actual position/speed value incorrect or not available (11)

| Symbol | Meaning |
| --- | --- |
| **Component:** Encoder 1 | **Propagation:** GLOBAL |

  

**Reaction:**
  
 ENCODER

**Acknowledge:**
  
PULSE INHIBIT

**Cause:**
  
The encoder has identified a position determination fault (multiturn) and supplies
status information bit by bit in an internal status/fault word.  
Some of these bits cause this fault to be triggered. Other bits are status displays.
The status/fault word is displayed in the fault value.  
Note regarding the bit designation:  
The first designation is valid for DRIVE-CLiQ encoders, the second for EnDat 2.2 encoders.  
Fault value (r0949, interpret binary):  
Bit 0: F1 (safety status display).  
Bit 1: F2 (safety status display).  
Bit 2: Reserved (lighting).  
Bit 3: Reserved (signal amplitude).  
Bit 4: Reserved (position value).  
Bit 5: Reserved (overvoltage).  
Bit 6: Reserved (undervoltage)/hardware fault EnDat supply (--&gt; F3x110, x = 1, 2,
3).  
Bit 7: Reserved (overcurrent)/EnDat encoder withdrawn when not in the parked state
(--&gt; F3x110, x = 1, 2, 3).  
Bit 8: Reserved (battery)/overcurrent EnDat supply (--&gt; F3x110, x = 1, 2, 3).  
Bit 9: Reserved/overvoltage EnDat supply (--&gt; F3x110, x = 1, 2, 3).  
Bit 11: Reserved/internal communication error (--&gt; F3x110, x = 1, 2, 3).  
Bit 12: Reserved/internal communication error (--&gt; F3x110, x = 1, 2, 3).  
Bit 13: Reserved/internal communication error (--&gt; F3x110, x = 1, 2, 3).  
Bit 14: Reserved/internal communication error (--&gt; F3x110, x = 1, 2, 3).  
Bit 15: Internal communication error (--&gt; F3x110, x = 1, 2, 3).  
Bit 16: Lighting (--&gt; F3x135, x = 1, 2, 3).  
Bit 17: Signal amplitude (--&gt; F3x135, x = 1, 2, 3).  
Bit 18: Singleturn position 1 (--&gt; F3x135, x = 1, 2, 3).  
Bit 19: Overvoltage (--&gt; F3x135, x = 1, 2, 3).  
Bit 20: Undervoltage (--&gt; F3x135, x = 1, 2, 3).  
Bit 21: Overcurrent (--&gt; F3x135, x = 1, 2, 3).  
Bit 22: Temperature exceeded (--&gt; F3x405, x = 1, 2, 3).  
Bit 23: Singleturn position 2 (safety status display).  
Bit 24: Singleturn system (--&gt; F3x135, x = 1, 2, 3).  
Bit 25: Singleturn power down (--&gt; F3x135, x = 1, 2, 3)  
Bit 26: Multiturn position 1 (--&gt; F3x136, x = 1, 2, 3).  
Bit 27: Multiturn position 2 (--&gt; F3x136, x = 1, 2, 3).  
Bit 28: Multiturn system (--&gt; F3x136, x = 1, 2, 3).  
Bit 29: Multiturn power down (--&gt; F3x136, x = 1, 2, 3).  
Bit 30: Multiturn overflow/underflow (--&gt; F3x136, x = 1, 2, 3).  
Bit 31: Multiturn battery (reserved).

**Remedy:**
  
- determine the detailed cause of the fault using the fault value.  
- replace the encoder if necessary.  
Note:  
An EnDat 2.2 encoder may only be removed and inserted in the "Park" state.  
If an EnDat 2.2 encoder was removed when not in the "Park" state, then after inserting
the encoder, a POWER ON (switch-off/switch-on) is necessary to acknowledge the fault.

### F31137 Encoder 1: Fault when determining the position (single turn)

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
Fault cause: %1 bin

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** Encoder 1 | **Propagation:** GLOBAL |

  

**Reaction:**
  
 ENCODER

**Acknowledge:**
  
PULSE INHIBIT

**Cause:**
  
A position determination fault has occurred in the DRIVE-CLiQ encoder.  
Fault value (r0949, interpret binary):  
yyxxxxxx hex: yy = encoder version, xxxxxx = bit coding of the fault cause  
----------  
For yy = 8 (0000 1000 bin), the following applies:  
Bit 1: Signal monitoring (sin/cos).  
Bit 8: F1 (safety status display) error position word 1.  
Bit 9: F2 (safety status display) error position word 2.  
Bit 16: LED monitoring.  
Bit 17: Fault when determining the position (multiturn).  
Bit 18: Single-step capability monitoring singleturn from the Safety channel.  
Bit 19: ECRC, configuration error in the safety channel.  
Bit 23: Temperature outside the limit values.  
----------  
For yy = 11 (0000 1011 bin), the following applies:  
Bit 0: Position word 1 difference between rotation counter and software counter (XC_ERR).  
Bit 1: Position word 1 track error of the incremental signals (LIS_ERR).  
Bit 2: Position word 1 error when aligning between incremental track signals and absolute
value (ST_ERR).  
Bit 3: Maximum permissible temperature exceeded (TEMP_ERR).  
Bit 4: Power supply overvoltage (MON_OVR_VOLT).  
Bit 5: Power supply overcurrent (MON_OVR_CUR).  
Bit 6: Power supply undervoltage (MON_UND_VOLT).  
Bit 7: Rotation error counter (MT_ERR).  
Bit 8: F1 (safety status display) error position word 1.  
Bit 9: F2 (safety status display) error position word 2.  
Bit 11: Position word 1 status bit: singleturn position OK (ADC_ready).  
Bit 12: Position word 1 status bit: rotation counter OK (MT_ready).  
Bit 13: Position word 1 memory error (MEM_ERR).  
Bit 14: Position word 1 absolute position error (MLS_ERR).  
Bit 15: position word 1 LED error, lighting unit error (LED_ERR).  
Bit 18: Position word 2 error when aligning between incremental track signals and
absolute value (ST_ERR).  
Bit 21: Position word 2 memory error (MEM_ERR).  
Bit 22: Position word 2 absolute position error (MLS_ERR).  
Bit 23: position word 2 LED error, lighting unit error (LED_ERR).  
----------  
For yy = 12 (0000 1100 bin), the following applies:  
Bit 8: encoder fault.  
Bit 10: error in the internal position data transport.  
----------  
For yy = 14 (0000 1110 bin), the following applies:  
Bit 0: Position word 1 temperature outside limit value.  
Bit 1: Position word 1 position determination error (multiturn).  
Bit 2: Position word 1 FPGA error.  
Bit 3: Position word 1 velocity error.  
Bit 4: Position word 1 communication error between FPGAs/error in the incremental
signal.  
Bit 5: Position word 1 timeout absolute value/error when determining the position
(singleturn).  
Bit 6: Position word 1 internal hardware fault (clock/power monitor IC/power).  
Bit 7: Position word 1 internal error (FPGA communication/FPGA parameterization/self-test/software).  
Bit 8: F1 (safety status display) error position word 1.  
Bit 9: F2 (safety status display) error position word 2.  
Bit 16: Position word 2 temperature outside limit value.  
Bit 17: Position word 2 position determination error (multiturn).  
Bit 18: Position word 2 FPGA error.  
Bit 19: Position word 2 velocity error.  
Bit 20: Position word 2 communication error between FPGAs.  
Bit 21: Position word 2 position determination error (singleturn).  
Bit 22: Position word 2 internal hardware fault (clock/power monitor IC/power).  
Bit 23: Position word 2 internal error (self-test/software).  
----------  
Note:  
For an encoder version that is not described here, please contact the encoder manufacturer
for more detailed information on the bit coding.

**Remedy:**
  
- determine the detailed cause of the fault using the fault value.  
- if required, replace the DRIVE-CLiQ encoder.

### F31138 Encoder 1: Fault when determining the position (multiturn)

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
Fault cause: %1 bin

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** Encoder 1 | **Propagation:** GLOBAL |

  

**Reaction:**
  
 ENCODER

**Acknowledge:**
  
PULSE INHIBIT

**Cause:**
  
A position determination fault has occurred in the DRIVE-CLiQ encoder.  
Fault value (r0949, interpret binary):  
yyxxxxxx hex: yy = encoder version, xxxxxx = bit coding of the fault cause  
----------  
For yy = 8 (0000 1000 bin), the following applies:  
Bit 1: Signal monitoring (sin/cos).  
Bit 8: F1 (safety status display) error position word 1.  
Bit 9: F2 (safety status display) error position word 2.  
Bit 16: LED monitoring.  
Bit 17: Fault when determining the position (multiturn).  
Bit 19: ECRC, configuration error in the safety channel.  
Bit 23: Temperature outside the limit values.  
----------  
For yy = 11 (0000 1011 bin), the following applies:  
Bit 0: Position word 1 difference between rotation counter and software counter (XC_ERR).  
Bit 1: Position word 1 track error of the incremental signals (LIS_ERR).  
Bit 2: Position word 1 error when aligning between incremental track signals and absolute
value (ST_ERR).  
Bit 3: Maximum permissible temperature exceeded (TEMP_ERR).  
Bit 4: Power supply overvoltage (MON_OVR_VOLT).  
Bit 5: Power supply overcurrent (MON_OVR_CUR).  
Bit 6: Power supply undervoltage (MON_UND_VOLT).  
Bit 7: Rotation error counter (MT_ERR).  
Bit 8: F1 (safety status display) error position word 1.  
Bit 9: F2 (safety status display) error position word 2.  
Bit 11: Position word 1 status bit: singleturn position OK (ADC_ready).  
Bit 12: Position word 1 status bit: rotation counter OK (MT_ready).  
Bit 13: Position word 1 memory error (MEM_ERR).  
Bit 14: Position word 1 absolute position error (MLS_ERR).  
Bit 15: position word 1 LED error, lighting unit error (LED_ERR).  
Bit 18: Position word 2 error when aligning between incremental track signals and
absolute value (ST_ERR).  
Bit 21: Position word 2 memory error (MEM_ERR).  
Bit 22: Position word 2 absolute position error (MLS_ERR).  
Bit 23: position word 2 LED error, lighting unit error (LED_ERR).  
----------  
For yy = 14 (0000 1110 bin), the following applies:  
Bit 0: Position word 1 temperature outside limit value.  
Bit 1: Position word 1 position determination error (multiturn).  
Bit 2: Position word 1 FPGA error.  
Bit 3: Position word 1 velocity error.  
Bit 4: Position word 1 communication error between FPGAs/error in the incremental
signal.  
Bit 5: Position word 1 timeout absolute value/error when determining the position
(singleturn).  
Bit 6: Position word 1 internal hardware fault (clock/power monitor IC/power).  
Bit 7: Position word 1 internal error (FPGA communication/FPGA parameterization/self-test/software).  
Bit 8: F1 (safety status display) error position word 1.  
Bit 9: F2 (safety status display) error position word 2.  
Bit 16: Position word 2 temperature outside limit value.  
Bit 17: Position word 2 position determination error (multiturn).  
Bit 18: Position word 2 FPGA error.  
Bit 19: Position word 2 velocity error.  
Bit 20: Position word 2 communication error between FPGAs.  
Bit 21: Position word 2 position determination error (singleturn).  
Bit 22: Position word 2 internal hardware fault (clock/power monitor IC/power).  
Bit 23: Position word 2 internal error (self-test/software).  
----------  
Note:  
For an encoder version that is not described here, please contact the encoder manufacturer
for more detailed information on the bit coding.

**Remedy:**
  
- determine the detailed cause of the fault using the fault value.  
- if required, replace the DRIVE-CLiQ encoder.

### F31405 Encoder 1: Temperature in the encoder evaluation exceeded

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
temperature: [0.1 degrees C] %1, temperature sensor number: %2

**Message class:**
  
Overtemperature of the electronic components (6)

| Symbol | Meaning |
| --- | --- |
| **Component:** Sensor Module Encoder 1 | **Propagation:** LOCAL |

  

**Reaction:**
  
 ENCODER

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
An inadmissibly high temperature was detected in the encoder electronics or the encoder
evaluation.  
Fault value (r0949, interpret hexadecimal):  
yyxxxx hex: yy = temperature sensor number, xxxx = measured module temperature in
0.1 °C.

**Remedy:**
  
Reduce the ambient temperature for the DRIVE-CLiQ connection of the motor.

### A31700 Encoder 1: Functional safety monitoring initiated

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
Fault cause: %1 bin

**Message class:**
  
Safety monitoring channel has identified an error (10)

| Symbol | Meaning |
| --- | --- |
| **Component:** Sensor Module Encoder 1 | **Propagation:** GLOBAL |

  

**Reaction:**
  
 NONE

**Acknowledge:**
  
NONE

**Cause:**
  
Functional safety was activated. Self-test of the DRIVE-CLiQ encoder has detected
a fault.  
Alarm value (r2124, interpret binary):  
Bit x = 1: Effectivity test x unsuccessful.

**Remedy:**
  
Replace encoder.

### F31801 Encoder 1 DRIVE-CLiQ: Sign-of-life missing

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** Control Unit (CU) | **Propagation:** LOCAL |

  

**Reaction:**
  
 ENCODER

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A DRIVE-CLiQ communication error has occurred from the Control Unit to the encoder
involved.  
Fault cause:  
10 (= 0A hex):  
The sign-of-life bit in the receive telegram is not set.  
Note regarding the message value:  
The individual information is coded as follows in the message value (r0949/r2124):  
0000yyxx hex: yy = component number, xx = error cause

**Remedy:**
  
- check the electrical cabinet design and cable routing for EMC compliance  
- replace the component involved.

### F31802 Encoder 1: Time slice overflow

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** Sensor Module Encoder 1 | **Propagation:** LOCAL |

  

**Reaction:**
  
 ENCODER

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A time slice overflow has occurred in encoder 1.  
Fault value (r0949, interpret hexadecimal):  
yx hex: y = function involved (Siemens-internal fault diagnostics), x = time slice
involved  
x = 9:  
Time slice overflow of the fast (current controller clock cycle) time slice.  
x = A:  
Time slice overflow of the average time slice.  
x = C:  
Time slice overflow of the slow time slice.  
yx = 3E7:  
Timeout when waiting for SYNO (e.g. unexpected return to non-cyclic operation).

**Remedy:**
  
Increase the current controller sampling time  
Note:  
For a current controller sampling time = 31.25 µs, use an SMx20 with Article No. 6SL3055-0AA00-5xA3.

### F31804 Encoder 1: Sensor Module checksum error

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** Sensor Module Encoder 1 | **Propagation:** LOCAL |

  

**Reaction:**
  
 ENCODER

**Acknowledge:**
  
POWER ON

**Cause:**
  
A checksum error has occurred when reading-out the program memory on the Sensor Module.  
Fault value (r0949, interpret hexadecimal):  
yyyyxxxx hex  
yyyy: Memory area involved.  
xxxx: Difference between the checksum at POWER ON and the actual checksum.

**Remedy:**
  
- carry out a POWER ON (switch-off/switch-on).  
- upgrade firmware to later version (&gt;= V2.6 HF3, &gt;= V4.3 SP2, &gt;= V4.4).  
- check whether the permissible ambient temperature for the component is maintained.  
- replace the Sensor Module.

### F31805 Encoder 1: EEPROM checksum error

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** Sensor Module Encoder 1 | **Propagation:** LOCAL |

  

**Reaction:**
  
 ENCODER

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
Data in the EEPROM corrupted .  
Fault value (r0949, interpret hexadecimal):  
01: EEPROM access error.  
02: Too many blocks in the EEPROM.

**Remedy:**
  
Replace the module.

### F31806 Encoder 1: Initialization error

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
%1

**Message class:**
  
Actual position/speed value incorrect or not available (11)

| Symbol | Meaning |
| --- | --- |
| **Component:** Sensor Module Encoder 1 | **Propagation:** LOCAL |

  

**Reaction:**
  
 ENCODER

**Acknowledge:**
  
PULSE INHIBIT

**Cause:**
  
The encoder was not successfully initialized.  
Fault value (r0949, interpret binary):  
Bit 0, 1: Encoder initialization with the motor rotating has failed (deviation involving
coarse and fine position in encoder pulses/4).  
Bit 2: Mid-voltage matching for track A unsuccessful.  
Bit 3: Mid-voltage matching for track B unsuccessful.  
Bit 4: Mid-voltage matching for acceleration input unsuccessful.  
Bit 5: Mid-voltage matching for track safety A unsuccessful.  
Bit 6: Mid-voltage matching for track safety B unsuccessful.  
Bit 7: Mid-voltage matching for track C unsuccessful.  
Bit 8: Mid-voltage matching for track D unsuccessful.  
Bit 9: Mid-voltage matching for track R unsuccessful.  
Bit 10: The difference in mid-voltages between A and B is too great (&gt; 0.5 V)  
Bit 11: The difference in mid-voltages between C and D is too great (&gt; 0.5 V)  
Bit 12: The difference in mid-voltages between safety A and safety B is too great
(&gt; 0.5 V)  
Bit 13: The difference in mid-voltages between A and safety B is too great (&gt; 0.5
V)  
Bit 14: The difference in mid-voltages between B and safety A is too great (&gt; 0.5
V)  
Bit 15: The standard deviation of the calculated mid-voltages is too great (&gt; 0.3
V)  
Bit 16: Internal fault - fault when reading a register (CAFE)  
Bit 17: Internal fault - fault when writing a register (CAFE)  
Bit 18: Internal fault: No mid-voltage matching available  
Bit 19: Internal error - ADC access error.  
Bit 20: Internal error - no zero crossover found.  
Bit 28: Error while initializing the EnDat 2.2 measuring unit.  
Bit 29: Error when reading out the data from the EnDat 2.2 measuring unit.  
Bit 30: EEPROM checksum of the EnDat 2.2 measuring unit incorrect.  
Bit 31: Data of the EnDat 2.2 measuring unit inconsistent.  
Note:  
Bit 0, 1: Up to 6SL3055-0AA00-5*A0  
Bits 2 ... 20: 6SL3055-0AA00-5*A1 and higher

**Remedy:**
  
Acknowledge fault.  
If the fault cannot be acknowledged:  
Bits 2 ... 9: Check encoder power supply.  
Bits 2 ... 14: Check the corresponding cable.  
Bit 15 with no other bits: Check track R, check settings in p0404.  
Bit 28: Check the cable between the EnDat 2.2 converter and the measuring unit.  
Bit 29 ... 31: Replace the defective measuring unit.

### F31813 Encoder 1: Hardware logic unit failed

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
Fault cause: %1 bin

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** Sensor Module Encoder 1 | **Propagation:** GLOBAL |

  

**Reaction:**
  
 ENCODER

**Acknowledge:**
  
PULSE INHIBIT

**Cause:**
  
The logic unit of the DRIVE-CLiQ encoder has failed.  
Fault value (r0949, interpret binary):  
Bit 0: ALU watchdog has responded.  
Bit 1: ALU has detected a sign-of-life error.

**Remedy:**
  
When the error reoccurs, replace the encoder.

### F31820 Encoder 1 DRIVE-CLiQ: Telegram error

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** Sensor Module Encoder 1 | **Propagation:** LOCAL |

  

**Reaction:**
  
 ENCODER

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A DRIVE-CLiQ communication error has occurred from the Control Unit to the encoder
concerned.  
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
  
- carry out a POWER ON (switch-off/switch-on).  
- check the electrical cabinet design and cable routing for EMC compliance  
- check the DRIVE-CLiQ wiring (interrupted cable, contacts, ...).

### F31835 Encoder 1 DRIVE-CLiQ: Cyclic data transfer error

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** Sensor Module Encoder 1 | **Propagation:** LOCAL |

  

**Reaction:**
  
 ENCODER

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A DRIVE-CLiQ communication error has occurred from the Control Unit to the encoder
concerned. The nodes do not send and receive in synchronism.  
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
  
- carry out a POWER ON.  
- replace the component involved.

### F31836 Encoder 1 DRIVE-CLiQ: Send error for DRIVE-CLiQ data

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** Sensor Module Encoder 1 | **Propagation:** LOCAL |

  

**Reaction:**
  
 ENCODER

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A DRIVE-CLiQ communication error has occurred from the Control Unit to the encoder
involved. Data were not able to be sent.  
Fault cause:  
65 (= 41 hex):  
Telegram type does not match send list.  
Note regarding the message value:  
The individual information is coded as follows in the message value (r0949/r2124):  
0000yyxx hex: yy = component number, xx = error cause

**Remedy:**
  
Carry out a POWER ON.

### F31837 Encoder 1 DRIVE-CLiQ: Component fault

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** Sensor Module Encoder 1 | **Propagation:** LOCAL |

  

**Reaction:**
  
 ENCODER

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
  
- check the DRIVE-CLiQ wiring (interrupted cable, contacts, ...).  
- check the electrical cabinet design and cable routing for EMC compliance  
- if required, use another DRIVE-CLiQ socket (p9904).  
- replace the component involved.

### F31845 Encoder 1 DRIVE-CLiQ: Cyclic data transfer error

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** Sensor Module Encoder 1 | **Propagation:** LOCAL |

  

**Reaction:**
  
 ENCODER

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A DRIVE-CLiQ communication error has occurred from the Control Unit to the encoder
involved.  
Fault cause:  
11 (= 0B hex):  
Synchronization error during alternating cyclic data transfer.  
Note regarding the message value:  
The individual information is coded as follows in the message value (r0949/r2124):  
0000yyxx hex: yy = component number, xx = error cause

**Remedy:**
  
Carry out a POWER ON (switch-off/switch-on).

### F31850 Encoder 1: Encoder evaluation internal software error

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** Sensor Module Encoder 1 | **Propagation:** LOCAL |

  

**Reaction:**
  
 ENCODER

**Acknowledge:**
  
POWER ON

**Cause:**
  
An internal software error has occurred in the Sensor Module of encoder 1.  
Fault value (r0949, interpret decimal):  
1: Background time slice is blocked.  
2: Checksum over the code memory is not OK.  
10000: OEM memory of the EnDat encoder contains data that cannot be interpreted.  
11000 ... 11499: Descriptive data from EEPROM incorrect.  
11500 ... 11899: Calibration data from EEPROM incorrect.  
11900 ... 11999: Configuration data from EEPROM incorrect.  
12000 ... 12008: communication with analog/digital converter faulted.  
16000: DRIVE-CLiQ encoder initialization application error.  
16001: DRIVE-CLiQ encoder initialization ALU error.  
16002: DRIVE-CLiQ encoder HISI / SISI initialization error.  
16003: DRIVE-CLiQ encoder safety initialization error.  
16004: DRIVE-CLiQ encoder internal system error.

**Remedy:**
  
- replace the Sensor Module.  
- if required, upgrade the firmware in the Sensor Module.  
- contact Technical Support.

### F31851 Encoder 1 DRIVE-CLiQ (CU): Sign-of-life missing

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** Sensor Module Encoder 1 | **Propagation:** LOCAL |

  

**Reaction:**
  
 ENCODER

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A DRIVE-CLiQ communication error has occurred from the Sensor Module (encoder 1) involved
to the Control Unit.  
The DRIVE-CLiQ component did not set the sign-of-life to the Control Unit.  
Fault cause:  
10 (= 0A hex):  
The sign-of-life bit in the receive telegram is not set.  
Note regarding the message value:  
The individual information is coded as follows in the message value (r0949/r2124):  
0000yyxx hex: yy = component number, xx = error cause

**Remedy:**
  
- Upgrade the firmware of the component involved.  
- carry out a POWER ON (switch-off/switch-on) for the component involved.

### F31860 Encoder 1 DRIVE-CLiQ (CU): Telegram error

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** Sensor Module Encoder 1 | **Propagation:** LOCAL |

  

**Reaction:**
  
 ENCODER

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A DRIVE-CLiQ communication error has occurred from the Sensor Module (encoder 1) involved
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
  
- carry out a POWER ON (switch-off/switch-on).  
- check the electrical cabinet design and cable routing for EMC compliance  
- check the DRIVE-CLiQ wiring (interrupted cable, contacts, ...).

### F31875 Encoder 1: power supply voltage failed

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Supply voltage fault (undervoltage) (3)

| Symbol | Meaning |
| --- | --- |
| **Component:** Sensor Module Encoder 1 | **Propagation:** LOCAL |

  

**Reaction:**
  
 ENCODER

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
  
- carry out a POWER ON (switch-off/switch-on).  
- check the power supply voltage wiring for the DRIVE-CLiQ component (interrupted
cable, contacts, ...).  
- check the dimensioning of the power supply for the DRIVE-CLiQ component.

### F31885 Encoder 1 DRIVE-CLiQ: Cyclic data transfer error

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** Sensor Module Encoder 1 | **Propagation:** LOCAL |

  

**Reaction:**
  
 ENCODER

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
There is a DRIVE-CLiQ communication error between the converter and motor.  
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
  
- check the OCC cable between the converter and motor.  
- check the power supply voltage of the component involved.  
- carry out a POWER ON (switch-off/switch-on).  
- replace the component involved.  
Note:  
OCC: One Cable Connection (one cable system)

### F31886 Encoder 1 DRIVE-CLiQ (CU): Error when sending DRIVE-CLiQ data

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** Sensor Module Encoder 1 | **Propagation:** LOCAL |

  

**Reaction:**
  
 ENCODER

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A DRIVE-CLiQ communication error has occurred from the Sensor Module (encoder 1) involved
to the Control Unit.  
Data were not able to be sent.  
Fault cause:  
65 (= 41 hex):  
Telegram type does not match send list.  
Note regarding the message value:  
The individual information is coded as follows in the message value (r0949/r2124):  
0000yyxx hex: yy = component number, xx = error cause

**Remedy:**
  
- carry out a POWER ON.  
- check whether the firmware version of the encoder (r0148) matches the firmware version
of Control Unit (r0018).

### F31887 Encoder 1 DRIVE-CLiQ (CU): Component fault

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** Sensor Module Encoder 1 | **Propagation:** LOCAL |

  

**Reaction:**
  
 ENCODER

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
Fault detected on the DRIVE-CLiQ component involved (Sensor Module for encoder 1).
Faulty hardware cannot be excluded.  
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
  
- check the DRIVE-CLiQ wiring (interrupted cable, contacts, ...).  
- check the electrical cabinet design and cable routing for EMC compliance  
- if required, use another DRIVE-CLiQ socket (p9904).  
- replace the component involved.

### F31895 Encoder 1 DRIVE-CLiQ (CU): Alternating cyclic data transfer error

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** Sensor Module Encoder 1 | **Propagation:** LOCAL |

  

**Reaction:**
  
 ENCODER

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
A DRIVE-CLiQ communication error has occurred from the Sensor Module (encoder 1) involved
to the Control Unit.  
Fault cause:  
11 (= 0B hex):  
Synchronization error during alternating cyclic data transfer.  
Note regarding the message value:  
The individual information is coded as follows in the message value (r0949/r2124):  
0000yyxx hex: yy = component number, xx = error cause

**Remedy:**
  
Carry out a POWER ON.

### F31896 Encoder 1 DRIVE-CLiQ (CU): Inconsistent component properties

**Drive object:**
  
S210

**Valid as of version:**
  
5.2

**Message value:**
  
Component number: %1

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause: | Remedy: |

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

| Symbol | Meaning |
| --- | --- |
| **Component:** Sensor Module Encoder 1 | **Propagation:** LOCAL |

  

**Reaction:**
  
 OFF2

**Acknowledge:**
  
IMMEDIATELY

**Cause:**
  
The properties of the DRIVE-CLiQ component (Sensor Module for encoder 1), specified
by the fault value, have changed in an incompatible fashion with respect to the properties
when booted. One cause can be, e.g. that a DRIVE-CLiQ cable or DRIVE-CLiQ component
has been replaced.  
Fault value (r0949, interpret decimal):  
Component number.

**Remedy:**
  
- carry out a POWER ON.  
- when a component is replaced, the same component type and if possible the same firmware
version should be used.  
- when a cable is replaced, only cables whose length is the same as or as close as
possible to the length of the original cables should be used (ensure compliance with
the maximum cable length).

### F31950 Encoder 1: Internal software error

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

| Symbol | Meaning |
| --- | --- |
| **Component:** Sensor Module Encoder 1 | **Propagation:** LOCAL |

  

**Reaction:**
  
 ENCODER

**Acknowledge:**
  
POWER ON

**Cause:**
  
An internal software error has occurred.  
Fault value (r0949, interpret decimal):  
The fault value contains information regarding the fault source.  
Only for internal Siemens troubleshooting.

**Remedy:**
  
- if necessary, upgrade the firmware in the Sensor Module to a later version.  
- contact Technical Support.

### F40000 Fault at DRIVE-CLiQ socket X100

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

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

### A40100 Alarm at DRIVE-CLiQ socket X100

**Drive object:**
  
S210

**Valid as of version:**
  
5.1

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

### A50517 FBLOCKS: Int meas active

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

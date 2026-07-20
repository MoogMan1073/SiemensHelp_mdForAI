---
title: "SINAMICS Alarms S200 Basic PN"
package: sdral423enUS
topics: 400
source: Siemens TIA Portal Information System (offline help, en-US)
---


# SINAMICS Alarms S200 Basic PN

This section contains the alarm descriptions for the devices listed below. The alarm descriptions for the various devices can differ. In the table of contents, you will then see a separate entry for each alarm number. The following device variants are taken into account in the online help:

- SINAMICS S200

## SINAMICS Alarms S200 Basic PN 01000 - 02030

SINAMICS Alarms S200 Basic PN 01000 - 02030

### F01000 Internal software error

**Valid as of version:**
  
06.02.015

**Message value:**
  
Module: %1, line: %2

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Control Unit (CU)

**Response:**
  
 OFF2

**Acknowledgment:**
  
POWER ON

**Cause**
  
An internal software error has occurred.  
Fault value (r0949, interpret hexadecimal):  
Only for internal Siemens troubleshooting.

**Remedy**
  
- Evaluate fault buffer (r0945).  
- Carry out a POWER ON (switch-off/switch-on) for all components.  
- If required, check the data on the non-volatile memory (e.g. memory card).  
- Upgrade firmware to later version.  
- Contact Technical Support.  
- Replace the converter.

### F01001 FloatingPoint exception

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Control Unit (CU)

**Response:**
  
 OFF2

**Acknowledgment:**
  
POWER ON

**Cause**
  
An exception occurred for an operation with the FloatingPoint data type.  
The error can be caused by the basic system or a technology function.  
Fault value (r0949, interpret hexadecimal):  
Only for internal Siemens troubleshooting.

**Remedy**
  
- Carry out a POWER ON (switch-off/switch-on) for all components.  
- Check configuration and signals of the blocks in FBLOCKS.  
- Check configuration and signals of DCC charts.  
- Check configuration and signals of TEC charts.  
- Upgrade firmware to later version.  
- Contact Technical Support.

### F01002 Internal software error

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Control Unit (CU)

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
An internal software error has occurred.  
Fault value (r0949, interpret hexadecimal):  
Only for internal Siemens troubleshooting.

**Remedy**
  
- Carry out a POWER ON (switch-off/switch-on) for all components.  
- Upgrade firmware to later version.  
- Contact Technical Support.

### F01003 Acknowledgment delay when accessing the memory

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Control Unit (CU)

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
A memory area was accessed that does not return a "READY".  
Fault value (r0949, interpret hexadecimal):  
Only for internal Siemens troubleshooting.

**Remedy**
  
- Carry out a POWER ON (switch-off/switch-on) for all components.  
- Contact Technical Support.

### N01004 Internal software error

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Control Unit (CU)

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
An internal software error has occurred.  
Fault value (r0949, hexadecimal):  
Only for internal Siemens troubleshooting.

**Remedy**
  
- Contact Technical Support.

### A01007 POWER ON for DRIVE-CLiQ component required

**Valid as of version:**
  
06.02.015

**Message value:**
  
Component number: %1

| Symbol | Meaning |
| --- | --- |
| For %1 | Component in target topology |

**Message class:**
  
General drive fault (19)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
A DRIVE-CLiQ component must be switched on again (POWER ON) (e.g. due to a firmware
update).  
Alarm value (r2124, interpret decimal):  
Component number of the DRIVE-CLiQ component.  
Note:  
For a component number = 1, a POWER ON of the Control Unit is required.

**Remedy**
  
- Switch off the power supply of the specified DRIVE-CLiQ component and switch it
on again.  
- For SINUMERIK, auto commissioning is prevented. In this case, a POWER ON is required
for all components and the auto commissioning must be restarted.

### A01009 Control Unit overtemperature

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Overtemperature of the electronic components (6)

**Component:**
  
Control Unit (CU)

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The temperature (r0037[0]) of the converter has exceeded the specified limit value.

**Remedy**
  
- Check the converter air intake.  
- Check the converter fan.  
Note:  
The alarm is automatically withdrawn once the limit value has been fallen below.

### F01011 Download interrupted

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The project download was interrupted.  
Fault value (r0949, interpret decimal):  
1: The user prematurely interrupted the project download.  
2: The communication cable was interrupted (e.g. cable breakage, cable withdrawn).  
3: The project download was prematurely exited by the commissioning tool.  
100: Different versions between the firmware version and project files which were
loaded by loading into the file system "Download from memory card".  
Note:  
The response to an interrupted download is the state "first commissioning".

**Remedy**
  
- Check the communication cable.  
- Download the project again.  
- Boot from previously saved files (switch-off/switch-on or p0976).  
- When loading into the file system (download from memory card), use the matching
version.

### F01014 Topology: Component property changed

**Valid as of version:**
  
06.02.015

**Message value:**
  
Component number: %1

**Message class:**
  
Hardware/software error (1)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The properties of the component have fundamentally changed.  
Fault value (r0949, interpret hexadecimal):  
Component number.

**Remedy**
  
- Carry out a restart, reload parameters.

### F01015 Internal software error

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Control Unit (CU)

**Response:**
  
 OFF2

**Acknowledgment:**
  
POWER ON

**Cause**
  
An internal software error has occurred.  
Fault value (r0949, interpret decimal):  
Only for internal Siemens troubleshooting.

**Remedy**
  
- Carry out a POWER ON (switch-off/switch-on) for all components.  
- Upgrade firmware to later version.  
- Contact Technical Support.

### A01016 Firmware changed

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Control Unit (CU)

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
At least one firmware file in the directory was illegally changed on the non-volatile
memory (memory card/device memory) with respect to the version when shipped from the
factory.  
Alarm value (r2124, interpret decimal):  
0: Checksum of one file is incorrect.  
1: File missing.  
2: File too many.  
3: Incorrect firmware version.  
4: Incorrect checksum of the backup file.

**Remedy**
  
Restore the delivery condition of the non-volatile memory for the firmware (memory
card/device memory).

### A01017 Component lists changed

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Control Unit (CU)

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The memory card has a defective file.  
Alarm value (r2124, interpret decimal):  
xyz dec: x = problem, y = file name  
x = 1: file checksum is incorrect.  
x = 2: error when parsing the file.  
y = 1: file MOTARM.ACX  
y = 2: file MOTARMLD.ACX  
y = 3: file MOTSRM.ACX  
y = 4: file MOTSLM.ACX  
y = 5: file MOTRESM.ACX  
y = 6: file BEARING.ACX  
y = 7: file CFG_BEAR.ACX  
y = 8: file BEARINGTYPE.ACX  
y = 9: file BRAKE.ACX  
y = 10: file CFG_BRAKE.ACX  
y = 11: file ENCODER.ACX  
y = 12: file CFG_ENCODER.ACX  
y = 13: file ENCODERGEAR.ACX  
y = 14: file CFG_ENC_GEAR.ACX  
y = 15: file LOADGEAR.ACX  
y = 16: file THERMMOTMOD3.ACX  
y = 17: file CFG_THERMMOTMOD3.ACX  
y = 30: file WHITELIST.ACX

**Remedy**
  
Correct the file involved.

### F01018 Runup has been interrupted several times

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Hardware/software error (1)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
POWER ON

**Cause**
  
Module booting was interrupted several times. As a consequence, the module boots with
the factory setting.  
Possible reasons for booting being interrupted:  
- Power supply interrupted.  
- CPU crashed.  
- Parameterization invalid.

**Remedy**
  
- Carry out a POWER ON (switch-off/switch-on). After switching on, the module reboots
from the valid parameterization (if available).  
- Restore the valid parameterization.  
Examples:  
a) Carry out a first commissioning, save, carry out a POWER ON (switch-off/switch-on).  
b) Load another valid parameter backup (e.g. from the memory card), save, carry out
a POWER ON (switch-off/switch-on).  
Note:  
If the fault situation is repeated, then this fault is again output after several
interrupted boots.

### A01019 Writing to the removable data medium unsuccessful

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Control Unit (CU)

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The write access to the removable data medium was unsuccessful.

**Remedy**
  
- Check the removable data medium and if required replace.  
- Repeat the data backup.

### A01020 Writing to RAM disk unsuccessful

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Control Unit (CU)

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
A write access to the internal RAM disk was unsuccessful.

**Remedy**
  
Adapt the file size for the system logbook to the internal RAM disk (p9930).

### F01023 Software timeout (internal)

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Control Unit (CU)

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
An internal software timeout has occurred.  
Fault value (r0949, interpret decimal):  
Only for internal Siemens troubleshooting.

**Remedy**
  
- Carry out a POWER ON (switch-off/switch-on) for all components.  
- Upgrade firmware to later version.  
- Contact Technical Support.

### F01030 Sign-of-life failure for master control

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Communication error to the higher-level control system (9)

**Component:**
  
None

**Response:**
  
 OFF3

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
For active PC master control of the PC, no sign-of-life was received within the monitoring
time.  
The master control was returned to the drive.

**Remedy**
  
Set the monitoring time higher at the PC or, if required, completely disable the monitoring
function.  
The monitoring time is set as follows using the commissioning tool:  
<Drive> -> Commissioning -> Control panel -> Button "Fetch master control" -> A window
is displayed to set the monitoring time in milliseconds.  
Notice:  
The monitoring time should be set as short as possible. A long monitoring time means
a late response when the communication fails!

### A01032 All parameters must be saved

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Control Unit (CU)

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
Data backup is incomplete  
The partially saved parameters are not loaded the next time the system runs up.  
For the system to successfully power up, all of the parameters must have been completely
backed up.  
Alarm value (r2124, interpret decimal):  
Only for internal Siemens troubleshooting.

**Remedy**
  
Save all parameters.  
See also: p0977 (Save all parameters)

### F01033 Units changeover: Reference parameter value invalid

**Valid as of version:**
  
06.02.015

**Message value:**
  
Parameter: %1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
When changing over the units to the referred representation type, it is not permissible
for any of the required reference parameters to be equal to 0.0  
Fault value (r0949, parameter):  
Reference parameter whose value is 0.0.

**Remedy**
  
Set the value of the reference parameter to a number different than 0.0.  
See also: p0304, p0305, p2000, p2002, p2003

### F01034 Units changeover: Calculation parameter values after reference value change unsuccessful

**Valid as of version:**
  
06.02.015

**Message value:**
  
Parameter: %1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The change of a reference parameter meant that for an involved parameter the selected
value was not able to be re-calculated in the per unit representation. The change
was rejected and the original parameter value restored.  
Fault value (r0949, parameter):  
Parameter whose value was not able to be re-calculated.  
See also: p0304, p0305, p2000, p2002, p2003

**Remedy**
  
- Select the value of the reference parameter such that the parameter involved can
be calculated in the per unit representation.

### A01035 ACX: Parameter backup file corrupted

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Control Unit (CU)

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
When the converter runs up, no complete data set was found from the parameter backup
files. The last time that the parameterization was saved, it was not completely carried
out.  
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

**Remedy**
  
- Download the project again using the commissioning tool.  
- Retentively save parameters (save all parameters p0977 = 1)  
See also: p0977 (Save all parameters)

### F01036 Parameter backup file missing

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Control Unit (CU)

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
When loading the device parameterization, a parameter backup file cannot be found.

**Remedy**
  
If the project data are backed up using the commissioning tool, then the project must
be downloaded again.  
Retentively save parameters (save all parameters, p0977 = 1), as a consequence, parameter
files are completely written back to the non-volatile memory.  
Note:  
If the project data have not been backed up, then a new first commissioning is required.

### F01038 Loading the parameter backup file unsuccessful

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Control Unit (CU)

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
An error has occurred when loading parameter backup files from the non-volatile memory.

**Remedy**
  
- If you have saved the project data using the commissioning tool, then download the
project again. Retentively save the data or set p0977 = 1. This means that the parameter
files are again completely written to the non-volatile memory.  
- Replace the memory card or the converter.

### F01039 Writing to the parameter back-up file unsuccessful

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Control Unit (CU)

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
Writing to at least one parameter backup file in the non-volatile memory was unsuccessful.  
- A parameter backup file has the "read only" file attribute and cannot be overwritten.  
- There is not sufficient free memory space available.  
- The non-volatile memory is defective and cannot be written to.

**Remedy**
  
- Check the free memory space in the non-volatile memory.  
- Replace the memory card or the converter.

### F01040 Save parameter settings and carry out a POWER ON

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 OFF2

**Acknowledgment:**
  
POWER ON

**Cause**
  
A parameter was changed, which means that it is necessary to save the parameters and
reboot.

**Remedy**
  
- Back up parameters.  
- Carry out a POWER ON (switch-off/switch-on) for all components.  
Then:  
- Upload the drive unit (commissioning tool).

### F01041 Parameter save necessary

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
Defective or missing files were detected on the memory card when booting.  
Fault value (r0949, interpret decimal):  
1: Source file cannot be opened.  
2: Source file cannot be read.  
3: Target directory cannot be set up.  
4. Target file cannot be set up/opened.  
5. Target file cannot be written to.  
Additional values:  
Only for internal Siemens troubleshooting.

**Remedy**
  
- Save the parameters.  
- Download the project again to the drive unit.  
- Update the firmware  
- If required, replace the converter and/or memory card.

### F01042 Parameter error during project download

**Valid as of version:**
  
06.02.015

**Message value:**
  
Parameter: %1, index: %2, fault cause: %3

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
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
109: Write access only in the commissioning status, encoder.  
110: Write access only in the commissioning status, motor.  
111: Write access only in the commissioning status, power unit.  
112: Write access only in the quick commissioning mode.  
113: Write access only in the ready mode.  
114: Write access only in the commissioning status, parameter reset.  
115: Write access only in the Safety Integrated commissioning status.  
116: Write access only in the commissioning status, technological application/units.  
117: Write access only in the commissioning status.  
118: Write access only in the commissioning status, download.  
119: Parameter may not be written in download.  
120: Write access only in the commissioning status, drive basis configuration.  
121: Write access only in the commissioning status, define drive type.  
122: Write access only in the commissioning status, data set basis configuration.  
123: Write access only in the commissioning status, device configuration.  
124: Write access only in the commissioning status, device download.  
125: Write access only in the commissioning status, device parameter reset.  
126: Write access only in the commissioning status, device ready.  
127: Write access only in the commissioning status, device.  
129: Parameter may not be written in download.  
131: Requested signal interconnection not possible as the signal source does not supply
float value.  
132: Free signal interconnection via PROFIdrive telegram setting inhibited.  
133: Access method not defined.  
200: Below the valid values.  
201: Above the valid values.  
202: Cannot be accessed from the Basic Operator Panel (BOP).  
203: Cannot be read from the Basic Operator Panel (BOP).  
204: Write access not permitted.

**Remedy**
  
- Correct the parameterization in the commissioning tool and download the project
again.  
- Enter the correct value in the specified parameter.  
- Identify the parameter that restricts the limits of the specified parameter.

### F01043 Fatal error at project download

**Valid as of version:**
  
06.02.015

**Message value:**
  
Fault cause: %1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
A fatal error was detected when downloading a project using the commissioning tool.  
Fault value (r0949, interpret decimal):  
1: Device status cannot be changed to device download (drive object ON?).  
2: Drive object number incorrect.  
3: A drive object that has already been deleted is deleted again.  
4: A drive object that has already been registered for generation is deleted.  
5: A drive object that does not exist is deleted.  
6: An undeleted drive object that already existed is generated.  
7: A drive object already registered for generation is generated again.  
8: Maximum number of drive objects that can be generated is exceeded.  
9: Error when generating the device drive object.  
10: Error when generating the target topology parameter.  
11: Error when generating a drive object (global component).  
12: Error when generating a drive object (drive component).  
13: Drive object type unknown.  
14: Drive status cannot be changed to "ready for operation" (r0947 and r0949).  
15: Drive status cannot be changed to drive download.  
16: Device status cannot be changed to "ready for operation".  
17: It is not possible to download the topology. The component wiring should be checked,
taking into account the various messages/signals.  
18: A new download is only possible if the factory settings are restored for the drive
unit.  
19: The slot for the option module has been configured several times (e.g. CAN and
COMM BOARD).  
20: The configuration is inconsistent.  
21: Error when accepting the download parameters.  
22: Software-internal download error.  
24: Download not possible during a partial run-up after inserting a component.  
Additional values:  
Only for internal Siemens troubleshooting.

**Remedy**
  
- Use the current version of the commissioning tool.  
- Modify the offline project and carry out a new download (e.g. compare the number
of drive objects, motors, encoders, power units in the offline project and at the
drive).  
- Change the drive state (is a drive rotating or is there a message/signal?).  
- Observe additional active messages/signals and remove their cause (e.g. correct
any incorrectly set parameters).  
- Automatically calculate the control parameters.  
- Boot from previously saved files (switch-off/switch-on or p0976).  
- Before a new download, restore the factory setting.

### F01044 Descriptive data error

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Control Unit (CU)

**Response:**
  
 OFF2

**Acknowledgment:**
  
POWER ON

**Cause**
  
An error was detected when loading the descriptive data saved in the non-volatile
memory.

**Remedy**
  
Replace the memory card or the converter.

### A01045 CU: Configuring data invalid

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Control Unit (CU)

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
An error was detected when evaluating the parameter files PSxxxyyy.ACX, PTxxxyyy.ACX,
CAxxxyyy.ACX, or CCxxxyyy.ACX saved in the non-volatile memory. Under certain circumstances,
several of the saved parameter values were not able to be accepted.  
Alarm value (r2124, interpret hexadecimal):  
Only for internal Siemens troubleshooting.

**Remedy**
  
- Restore the factory setting (p0976 = 1) and reload the project into the converter.  
Then retentively save the parameterization or set p0977 = 1. This overwrites the incorrect
parameter files in the non-volatile memory – and this alarm is withdrawn.

### A01049 CU: It is not possible to write to file

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Control Unit (CU)

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
It is not possible to write to a write-protected parameter backup file. The write
request was interrupted.  
Alarm value (r2124, interpret decimal):  
Number drive object

**Remedy**
  
Check whether the "write protected" attribute has been set for the files in the non-volatile
memory.  
When required, remove write protection and repeat the save operation (e.g. set p0977
= 1).

### F01050 Memory card and device incompatible

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
Control Unit (CU)

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The memory card and the device type do not match (e.g. a memory card for SINAMICS
S is inserted in SINAMICS G).

**Remedy**
  
- Insert the matching memory card.  
- Use the matching converter or power unit.

### F01054 CU: System limit exceeded

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
Control Unit (CU)

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
At least one system overload has been identified.  
Fault value (r0949, interpret decimal):  
1: Computing time load too high.  
5: Peak load too high.  
Note:  
As long as this fault is present, it is not possible to save the parameters (p0977).

**Remedy**
  
- Reduce the computing time load of the drive unit to below 100 %.  
- Deactivate functions.  
- Deactivate drive objects.  
- Remove drive objects from the target topology.  
- Note the DRIVE-CLiQ topology rules and if required, change the DRIVE-CLiQ topology.

### F01068 CU: Data memory memory overflow

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
Control Unit (CU)

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The utilization for a data memory area is too large.  
Fault value (r0949, interpret binary):  
Bit 0 = 1: High-speed data memory 1 overloaded  
Bit 1 = 1: High-speed data memory 2 overloaded  
Bit 2 = 1: High-speed data memory 3 overloaded  
Bit 3 = 1: High-speed data memory 4 overloaded

**Remedy**
  
- Deactivate function.  
- Deactivate drive object.  
- Remove drive object from the target topology.

### A01069 Parameter backup and device incompatible

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
Control Unit (CU)

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The parameter backup on the memory card and the drive unit do not match.  
The module boots with the factory settings.  
Example:  
Devices A and B. are not compatible and a memory card with the parameter backup for
device A is inserted in device B.

**Remedy**
  
- Insert a memory card with compatible parameter backup and carry out a POWER ON.  
- Insert a memory card without parameter backup and carry out a POWER ON.  
- Save the parameters (p0977 = 1).

### F01070 Project/firmware is being downloaded to the memory card

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
Control Unit (CU)

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
An upgrade (project/firmware download) was initiated on the memory card.  
While this fault is active, the corresponding update takes place with plausibility
and consistency checks. After this, depending on the command option, a new boot (reset)
for the converter is initiated.  
Caution:  
While upgrading and while this fault is active, it is not permissible to switch off
the converter.  
If the operation is interrupted, this can destroy the file system on the memory card.
The memory card will then no longer work properly and must be repaired.

**Remedy**
  
Not necessary.  
The fault is automatically withdrawn after the upgrade has been completed.

### F01072 Memory card restored from the backup copy

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
General drive fault (19)

**Component:**
  
Control Unit (CU)

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The converter was switched-off while writing to the memory card. This is why the visible
partition became defective.  
After switching on, the data from the non-visible partition (backup copy) were written
to the visible partition.

**Remedy**
  
Check that the firmware and parameterization is up-to-date.

### A01073 POWER ON required for backup copy on memory card

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
General drive fault (19)

**Component:**
  
Control Unit (CU)

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The parameter assignment on the visible partition of the memory card has changed.  
In order that the backup copy on the memory card is updated on the non-visible partition,
it is necessary to carry out a POWER ON or hardware reset (p0972) of the Control Unit.  
Note:  
It is possible that a new POWER ON is requested via this alarm (e.g. after saving
with p0971 = 1).

**Remedy**
  
- Carry out a POWER ON (switch-off/switch-on) for the Control Unit.  
- Carry out a hardware reset (RESET button, p0972).

### F01082 Parameter error when running up from data backup

**Valid as of version:**
  
06.02.015

**Message value:**
  
Parameter: %1, index: %2, fault cause: %3

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
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
109: Write access only in the commissioning status, encoder.  
110: Write access only in the commissioning status, motor.  
111: Write access only in the commissioning status, power unit.  
112: Write access only in the quick commissioning mode.  
113: Write access only in the ready mode.  
114: Write access only in the commissioning status, parameter reset.  
115: Write access only in the Safety Integrated commissioning status.  
116: Write access only in the commissioning status, technological application/units.  
117: Write access only in the commissioning status.  
118: Write access only in the commissioning status, download.  
119: Parameter may not be written in download.  
120: Write access only in the commissioning status, drive basis configuration.  
121: Write access only in the commissioning status, define drive type.  
122: Write access only in the commissioning status, data set basis configuration.  
123: Write access only in the commissioning status, device configuration.  
124: Write access only in the commissioning status, device download.  
125: Write access only in the commissioning status, device parameter reset.  
126: Write access only in the commissioning status, device ready.  
127: Write access only in the commissioning status, device.  
129: Parameter may not be written in download.  
131: Requested signal interconnection not possible as the signal source supplies non-float
value.  
132: Free signal interconnection via PROFIdrive telegram setting inhibited.  
133: Access method not defined.  
200: Below the valid values.  
201: Above the valid values.  
202: Cannot be accessed from the Basic Operator Panel (BOP).  
203: Cannot be read from the Basic Operator Panel (BOP).  
204: Write access not permitted.

**Remedy**
  
- Correct the parameterization in the commissioning tool and download the project
again.  
- Enter the correct value in the specified parameter.  
- Identify the parameter that restricts the limits of the specified parameter.

### A01100 CU: Memory card withdrawn

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
General drive fault (19)

**Component:**
  
Control Unit (CU)

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The memory card (non-volatile memory) was withdrawn during operation.  
Notice:  
It is not permissible for the memory card to be withdrawn or inserted under voltage.

**Remedy**
  
- Switch off the drive system.  
- Re-insert the memory card that was withdrawn - This card must match the drive system.  
- Switch on the drive system again.

### F01105 CU: Insufficient memory

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
Control Unit (CU)

**Response:**
  
 OFF1

**Acknowledgment:**
  
POWER ON

**Cause**
  
The functionality on this Control Unit is too extensive (e.g. too many drives, functions,
data sets, Technology Extensions, blocks, etc).  
Fault value (r0949, interpret decimal):  
Only for internal Siemens troubleshooting.

**Remedy**
  
- Change the configuration on this Control Unit, e.g.  
-- Use fewer axes  
-- Reduce the number of configurable functions  
-- Use fewer data sets  
-- Reduce Technology Extensions and blocks  
- Use an additional Control Unit.

### F01107 CU: Save to memory card unsuccessful

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Control Unit (CU)

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
A data save in the non-volatile memory was not able to be successfully carried out.  
- Non-volatile memory is defective.  
- Insufficient space in the non-volatile memory.  
Fault value (r0949, interpret decimal):  
Only for internal Siemens troubleshooting.

**Remedy**
  
- Try to save again.  
- Replace the memory card or Control Unit.

### F01110 CU: More than one SINAMICS G on one Control Unit

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
More than one SINAMICS G type power unit is being operated from the Control Unit.  
Fault value (r0949, interpret decimal):  
Number of the second drive with a SINAMICS G type power unit.

**Remedy**
  
Only one SINAMICS G drive type is permitted.

### F01111 CU: Mixed operation of drive units illegal

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
Illegal operation of various drive units on one Control Unit:  
- SINAMICS S together with SINAMICS G  
- SINAMICS S together with SINAMICS S Value or Combi  
Fault value (r0949, interpret decimal):  
Number of the first drive object with a different power unit type.

**Remedy**
  
Only power units of one particular drive type may be operated with one Control Unit.

### F01122 Frequency at the measuring probe input too high

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Application/technological function faulted (17)

**Component:**
  
None

**Response:**
  
 OFF1

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
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

**Remedy**
  
Reduce the frequency of the pulses at the measuring probe input.

### F01123 Power unit does not support digital inputs/outputs

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
Power Unit

**Response:**
  
 OFF1

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The power unit does not support the activated "Digital inputs/outputs" function.

**Remedy**
  
Deactivate function.

### F01150 CU: Number of instances of a drive object type exceeded

**Valid as of version:**
  
06.02.015

**Message value:**
  
Drive object type: %1, number permitted: %2, actual number: %3

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The maximum permissible number of instances of a drive object type was exceeded.  
Note regarding the message value:  
The individual information is coded as follows in the message value (r0949/r2124):  
ddccbbaa hex:  
aa = drive object type:  
- Drive object type (p0107), for which the maximum permissible number of instances
was exceeded.  
bb = number permitted:  
- Maximum permissible number of instances for this drive object type.  
cc = actual number:  
- Actual number of instances for this drive object type.  
dd = no significance

**Remedy**
  
- Switch off the unit.  
- Suitably restrict the number of instances of a drive object type by reducing the
number of inserted components.  
- Re-commission the unit.

### F01151 CU: Number of drive objects of a category exceeded

**Valid as of version:**
  
06.02.015

**Message value:**
  
Drive object category: %1, number permitted: %2, actual number: %3

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The maximum permissible number of drive objects of a category was exceeded.  
Note regarding the message value:  
The individual information is coded as follows in the message value (r0949/r2124):  
ddccbbaa hex:  
aa = drive object category:  
- Drive object category, for which the maximum permissible number of drive objects
was exceeded.  
bb = number permitted:  
- Maximum permissible number for this drive object category.  
cc = actual number:  
- Actual number for this drive object category.  
dd = no significance

**Remedy**
  
- Switch off the unit.  
- Suitably restrict the number of drive objects of the specified category by reducing
the number of inserted components.  
- Re-commission the unit.

### F01152 CU: Invalid constellation of drive object types

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
POWER ON

**Cause**
  
It is not possible to simultaneously operate drive object types SERVO, VECTOR and
HLA.  
A maximum of 2 of these drive object types can be operated on a Control Unit.

**Remedy**
  
- Switch off the unit.  
- Restrict the use of drive object types SERVO, VECTOR, HLA to a maximum of 2.  
- Re-commission the unit.

### F01200 CU: Time slice management internal software error

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Control Unit (CU)

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
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

**Remedy**
  
- Contact Technical Support.

### F01205 CU: Time slice overflow

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Control Unit (CU)

**Response:**
  
 OFF2

**Acknowledgment:**
  
POWER ON

**Cause**
  
Insufficient processing time is available for the existing topology.  
Fault value (r0949, interpret hexadecimal):  
Only for internal Siemens troubleshooting.

**Remedy**
  
- Reduce the number of drives.

### F01250 EEPROM incorrect read-only data

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Control Unit (CU)

**Response:**
  
 NONE

**Acknowledgment:**
  
POWER ON

**Cause**
  
Error when reading the read-only data of the EEPROM in the converter.  
Fault value (r0949, interpret decimal):  
Only for internal Siemens troubleshooting.

**Remedy**
  
- Carry out a POWER ON (switch-off/switch-on).  
- Replace the converter.

### A01251 CU: CU-EEPROM incorrect read-write data

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Control Unit (CU)

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
Error when reading the read-write data of the EEPROM in the converter.  
Alarm value (r2124, interpret decimal):  
Only for internal Siemens troubleshooting.

**Remedy**
  
For alarm value r2124 < 256, the following applies:  
- Carry out a POWER ON (switch-off/switch-on).  
- Replace the converter.  
For alarm value r2124 >= 256, the following applies:  
- For the converter with this alarm, clear the fault memory (p0952 = 0).  
- Replace the converter.

### F01255 CU: Option Board EEPROM read-only data error

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
POWER ON

**Cause**
  
Error when reading the read-only data of the EEPROM in the Option Board.  
Fault value (r0949, interpret decimal):  
Only for internal Siemens troubleshooting.

**Remedy**
  
- Carry out a POWER ON (switch-off/switch-on).  
- Replace the Control Unit.

### A01256 CU: Option Board EEPROM read-write data error

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
Error when reading the read-write data of the EEPROM in the Option Board.  
Alarm value (r2124, interpret decimal):  
Only for internal Siemens troubleshooting.

**Remedy**
  
- Carry out a POWER ON (switch-off/switch-on).  
- Replace the Control Unit.

### A01314 Topology: Component must not be present

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1, to %2, %3, connection: %4

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause | Remedy |
| For %1, %2 | 0 | Component unknown |  |
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

| Symbol | Meaning |
| --- | --- |
| For %3 | Component in target topology |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause | Remedy |
| For %4 | 0 | Port 0 |  |
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

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
For a component, "deactivate and not present" is set but this component is still in
the topology.  
Alarm value (r2124, interpret hexadecimal):  
ddccbbaa hex:  
aa = component number  
bb = component class of the component  
cc = connection number  
Note:  
Component class and connection number are described in F01375.

**Remedy**
  
- Remove the corresponding component.  
- Change the setting "deactivate and not present".  
Note:  
Under "Topology --> Topology view", the commissioning tool where relevant offers improved
diagnostics capability (e.g. setpoint/actual value comparison).

### A01317 Deactivated component again present

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
If a component of the target topology for an active drive object is inserted and the
associated parameter of the component is set to "deactivate" (p0125, p0145, p0155,
p0165).  
Note:  
This is the only message that is displayed for a deactivated component.

**Remedy**
  
The alarm is automatically withdrawn for the following actions:  
- Activate the components involved (p0125 = 1, p0145 = 1, p0155 = 1, p0165 = 1).  
- Again withdraw the component involved.

### A01319 Inserted component not initialized

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
Initialization is required for at least one inserted component.  
This is only possible if the pulse inhibit is active on all drive objects.

**Remedy**
  
Activate pulse inhibit for all drive objects.

### F01325 Topology: Component number not included in target topology

**Valid as of version:**
  
06.02.015

**Message value:**
  
Component number: %1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The component referenced in a data set (e.g. PDS, MDS or EDS) is not contained in
the target topology.  
Fault value (r0949, interpret decimal)

**Remedy**
  
Establish consistency between the topology and data set configuration.

### A01330 Topology: Quick commissioning not possible

**Valid as of version:**
  
06.02.015

**Message value:**
  
Fault cause: %1, supplementary information: %2, preliminary component number: %3

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
Unable to carry out a quick commissioning. The existing actual topology does not fulfill
the requirements.

**Remedy**
  
- Check the motor connection.  
- Carry out a POWER ON (switch-off/switch-on).

### F01356 Topology: There is a defective component

**Valid as of version:**
  
06.02.015

**Message value:**
  
Fault cause: %1, Component number: %2, Connection number: %3

**Message class:**
  
Hardware/software error (1)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The actual topology indicates at least one defective component.  
Note:  
Pulse enable is withdrawn and prevented.

**Remedy**
  
Replace the defective component and restart the system.

### F01380 Topology: Actual topology EEPROM defective

**Valid as of version:**
  
06.02.015

**Message value:**
  
Preliminary component number: %1

**Message class:**
  
Hardware/software error (1)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
POWER ON

**Cause**
  
When detecting the actual topology, a component with a defective EEPROM was detected.  
Fault value (r0949, interpret hexadecimal):  
bbbbaaaa hex:  
bbbb = reserved  
aaaa = preliminary component number of the defective components

**Remedy**
  
Output the fault value and remove the defected component.

### A01382 Topology: Sensor Module incorrectly inserted

**Valid as of version:**
  
06.02.015

**Message value:**
  
Component: %1, to %2, %3, connection: %4

| Symbol | Meaning |
| --- | --- |
| For %1 | Component in target topology |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause | Remedy |
| For %2 | 0 | Component unknown |  |
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

| Symbol | Meaning |
| --- | --- |
| For %3 | Component in actual topology |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause | Remedy |
| For %4 | 0 | Port 0 |  |
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

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The topology comparison has detected a Sensor Module in the actual topology that has
been incorrectly inserted with respect to the target topology.  
Alarm value (r2124, interpret hexadecimal):  
ddccbbaa hex:  
dd = connection number (%4)  
cc = component number (%3)  
bb = component class (%2)  
aa = component number of the incorrectly inserted component (%1)  
Note:  
The component is described in dd, cc and bb, where the component involved is incorrectly
inserted.  
Component class and connection number are described in F01375.  
The drive system is no longer booted. In this state, the drive control (closed-loop)
cannot be enabled.

**Remedy**
  
Adapting topologies:  
- Insert the components involved at the right connection (correct the actual topology).  
- Adapt the project/parameterizing in the commissioning tool (correct the target topology).  
- Automatically resolve the topology error.  
Note:  
Under "Topology --> Topology view" the commissioning tool where relevant offers improved
diagnostics capability (e.g. setpoint/actual value comparison).

### A01388 Topology: Encoder incorrectly inserted

**Valid as of version:**
  
06.02.015

**Message value:**
  
Component: %1, to %2, %3, connection: %4

| Symbol | Meaning |
| --- | --- |
| For %1 | Component in target topology |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause | Remedy |
| For %2 | 0 | Component unknown |  |
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

| Symbol | Meaning |
| --- | --- |
| For %3 | Component in actual topology |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause | Remedy |
| For %4 | 0 | Port 0 |  |
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

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The topology comparison has detected an EnDat encoder in the actual topology that
has been incorrectly inserted with respect to the target topology.  
Alarm value (r2124, interpret hexadecimal):  
ddccbbaa hex:  
dd = connection number (%4)  
cc = component number (%3)  
bb = component class (%2)  
aa = component number of the incorrectly inserted component (%1)  
Note:  
The component is described in dd, cc and bb, where the component involved is incorrectly
inserted.  
Component class and connection number are described in F01375.  
The drive system is no longer booted. In this state, the drive control (closed-loop)
cannot be enabled.

**Remedy**
  
Adapting topologies:  
- Insert the components involved at the right connection (correct the actual topology).  
- Adapt the project/parameterizing in the commissioning tool (correct the target topology).  
- Automatically resolve the topology error.  
Note:  
Under "Topology --> Topology view" the commissioning tool where relevant offers improved
diagnostics capability (e.g. setpoint/actual value comparison).

### A01416 Topology: Component additionally inserted

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1, to %2, %3, connection: %4

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause | Remedy |
| For %1, %2 | 0 | Component unknown |  |
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

| Symbol | Meaning |
| --- | --- |
| For %3 | Component in target topology |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause | Remedy |
| For %4 | 0 | Port 0 |  |
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

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The topology comparison has found a component in the actual topology which is not
specified in the target topology.  
Alarm value (r2124, interpret hexadecimal):  
ddccbbaa hex:  
dd = component class (%2)  
cc = connection number (%4)  
bb = component class of the additional component (%1)  
aa = component number (%3)  
Note:  
The component class of the additional component is contained in bb.  
The component is described in dd, cc and aa, where the additional component is inserted.  
Component class and connection number are described in F01375.

**Remedy**
  
Adapting topologies:  
- Remove the additional component (correct the actual topology).  
- Adapt the project/parameterizing in the commissioning tool (correct the target topology).  
Note:  
Under "Topology --> Topology view" the commissioning tool where relevant offers improved
diagnostics capability (e.g. setpoint/actual value comparison).

### A01420 Topology: Component different

**Valid as of version:**
  
06.02.015

**Message value:**
  
Component: %1, target: %2, actual: %3, difference: %4

| Symbol | Meaning |
| --- | --- |
| For %1 | Component in target topology |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause | Remedy |
| For %2, %3 | 0 | Component unknown |  |
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
|  | Value | Cause | Remedy |
| For %4 | 1 | Different component type |  |
| 2 | Different article number |  |  |
| 3 | Different manufacturer |  |  |
| 4 | Incorrect subcomponent connected |  |  |
| 5 | NX10 or NX15 used instead of CX32. |  |  |
| 6 | CX32 used instead of NX10 or NX15. |  |  |
| 7 | Different number of connections |  |  |

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The topology comparison has detected differences in the actual and target topologies
in the electronic nameplate component.  
Alarm value (r2124, interpret hexadecimal):  
ddccbbaa hex:  
aa = component number (%1),  
bb = component class of the target topology (%2),  
cc = component class of the actual topology (%3),  
dd = difference (%4)  
Note:  
The component class is described in F01375.  
The drive system is no longer booted. In this state, the drive control (closed-loop)
cannot be enabled.

**Remedy**
  
Adapting topologies:  
- Connect the expected component (correct the actual topology).  
- Adapt the project/parameterizing in the commissioning tool (correct the target topology).  
  
Note:  
Under "Topology --> Topology view" the commissioning tool where relevant offers improved
diagnostics capability (e.g. setpoint/actual value comparison).

### A01425 Topology: Serial number different

**Valid as of version:**
  
06.02.015

**Message value:**
  
Component: %1, %2, differences: %3

| Symbol | Meaning |
| --- | --- |
| For %1 | Component in target topology |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause | Remedy |
| For %2 | 0 | Component unknown |  |
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

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The topology comparison has detected differences in the actual and target topologies
in relation to one component. The serial number is different.  
Alarm value (r2124, interpret hexadecimal):  
ddccbbaa hex:  
dd = reserved  
cc = number of differences (%3)  
bb = component class (%2)  
aa = component number (%1)  
Note:  
The component class is described in F01375.  
The drive system is no longer booted. In this state, the drive control (closed-loop)
cannot be enabled.

**Remedy**
  
Adapting topologies:  
- Change over the actual topology to match the target topology.  
- Load the target topology that matches the actual topology (commissioning tool).  
Note:  
Under "Topology --> Topology view" the commissioning tool where relevant offers improved
diagnostics capability (e.g. setpoint/actual value comparison).

### F01451 Topology: Target topology is invalid

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
An error was detected in the target topology.  
The target topology is invalid.  
Fault value (r0949, interpret hexadecimal):  
ccccbbaa hex: cccc = index error, bb = component number, aa = fault cause  
aa = 1B hex = 27 dec: Error not specified.  
aa = 1C hex = 28 dec: Value illegal.  
aa = 1D hex = 29 dec: Incorrect ID.  
aa = 1E hex = 30 dec: Incorrect ID length.  
aa = 1F hex = 31 dec: Too few indices left.  
aa = 20 hex = 32 dec: component is not connected to the converter.

**Remedy**
  
Download the target topology again using the commissioning tool.

### A01481 Topology: Internal communications faulted

**Valid as of version:**
  
06.02.015

**Message value:**
  
Component: %1, to %2, %3, connection: %4

| Symbol | Meaning |
| --- | --- |
| For %1, %3 | Component in target topology |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause | Remedy |
| For %2 | 0 | Component unknown |  |
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
|  | Value | Cause | Remedy |
| For %4 | 0 | Port 0 |  |
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

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
Internal communications faulted.

**Remedy**
  
- Carry out a POWER ON (switch-off/switch-on).  
- Replace the device.

### A01486 Topology: Component not connected

**Valid as of version:**
  
06.02.015

**Message value:**
  
Component: %1, to %2, %3, connection: %4

| Symbol | Meaning |
| --- | --- |
| For %1, %3 | Component in target topology |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause | Remedy |
| For %2 | 0 | Component unknown |  |
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
|  | Value | Cause | Remedy |
| For %4 | 0 | Port 0 |  |
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

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The topology comparison has detected a component that is missing in the actual topology
with respect to the target topology.  
Alarm value (r2124, interpret hexadecimal):  
ddccbbaa hex:  
dd = connection number (%4)  
cc = component number (%3)  
bb = component class (%2)  
aa = component number of the component that has not been inserted (%1)  
Note:  
The component is described in dd, cc and bb, where the component has not been inserted.  
Component class and connection number are described in F01375.

**Remedy**
  
Adapting topologies:  
- Insert the components involved at the right connection (correct the actual topology).  
- Adapt the project/parameterizing in the commissioning tool (correct the target topology).  
Check the hardware:  
- Check the 24 V supply voltage.  
- Check cables for interruption and contact problems.  
- Check that the component is working properly.  
Note:  
Under "Topology --> Topology view" the commissioning tool where relevant offers improved
diagnostics capability (e.g. setpoint/actual value comparison).

### A01488 Topology: Encoder not connected

**Valid as of version:**
  
06.02.015

**Message value:**
  
Component: %1, to %2, %3, connection: %4

| Symbol | Meaning |
| --- | --- |
| For %1, %3 | Component in target topology |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause | Remedy |
| For %2 | 0 | Component unknown |  |
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
|  | Value | Cause | Remedy |
| For %4 | 0 | Port 0 |  |
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

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The topology comparison has detected an encoder that is missing in the actual topology
with respect to the target topology.  
Alarm value (r2124, interpret hexadecimal):  
ddccbbaa hex:  
dd = connection number (%4)  
cc = component number (%3)  
bb = component class (%2)  
aa = component number of the component that has not been inserted (%1)  
Note:  
The component is described in dd, cc and bb, where the component has not been inserted.  
Component class and connection number are described in F01375.

**Remedy**
  
Adapting topologies:  
- Insert the components involved at the right connection (correct the actual topology).  
- Adapt the project/parameterizing in the commissioning tool (correct the target topology).  
Check the hardware:  
- Check the 24 V supply voltage.  
- Check cables for interruption and contact problems.  
- Check that the component is working properly.  
Note:  
Under "Topology --> Topology view" the commissioning tool where relevant offers improved
diagnostics capability (e.g. setpoint/actual value comparison).

### A01489 Topology: Motor not connected

**Valid as of version:**
  
06.02.015

**Message value:**
  
Component: %1, to %2, %3, connection: %4

| Symbol | Meaning |
| --- | --- |
| For %1, %3 | Component in target topology |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause | Remedy |
| For %2 | 0 | Component unknown |  |
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
|  | Value | Cause | Remedy |
| For %4 | 0 | Port 0 |  |
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

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The topology comparison has detected a motor that is missing in the actual topology
with respect to the target topology.  
Alarm value (r2124, interpret hexadecimal):  
ddccbbaa hex:  
dd = connection number (%4)  
cc = component number (%3)  
bb = component class (%2)  
aa = component number of the component that has not been inserted (%1)  
Note:  
The component is described in dd, cc and bb, where the component has not been inserted.  
Component class and connection number are described in F01375.

**Remedy**
  
Adapting topologies:  
- Insert the components involved at the right connection (correct the actual topology).  
- Adapt the project/parameterizing in the commissioning tool (correct the target topology).  
Check the hardware:  
- Check the 24 V supply voltage.  
- Check cables for interruption and contact problems.  
- Check that the component is working properly.  
Note:  
Under "Topology --> Topology view" the commissioning tool where relevant offers improved
diagnostics capability (e.g. setpoint/actual value comparison).

### F01512 No scaling available

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 OFF2

**Acknowledgment:**
  
POWER ON

**Cause**
  
An attempt was made to determine a conversion factor for a scaling that does not exist.  
Fault value (r0949, interpret decimal):  
Unit (e.g. corresponding to SPEED) for which an attempt was made to determine a factor.

**Remedy**
  
Apply scaling or check the transfer value.

### A01514 Error when writing during a reconnect

**Valid as of version:**
  
06.02.015

**Message value:**
  
Parameter: %1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
During a reconnect operation (e.g. while booting or downloading - but can also occur
in normal operation) a parameter was not able to be written to.  
The parameter is then reset to the factory setting.  
  
Alarm value (r2124, interpret decimal):  
Parameter number

**Remedy**
  
Not necessary.

### A01550 Security: Drive data encryption invalid

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Control Unit (CU)

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The password for drive data encryption (DDE) does not match the password configured
in the converter or no password was configured.  
The DDE password protects sensitive data on the SD card.  
It is not possible to transfer the data backup from the SD card.

**Remedy**
  
To be able to restore the data backup on the SD card, the DDE password must correspond
to the password that was originally configured for the data backup in the original
converter:  
- With the SD card inserted, enter the correct DDE password in the Security Wizard
of the web server and restart the converter.  
- In Startdrive, with the SD card inserted, under Online & Diagnostics, enter the
correct DDE password in screen form "Specify password for encryption of the drive
data" and restart the converter.  
  
If the data backup on the SD card is not be used:  
- Remove the SD card from the converter and restart the converter.  
  
Notice: Not observing this and continuing to work at the converter can lead to the
data backup on the SD card being lost.

### A01590 Drive: Motor maintenance interval expired

**Valid as of version:**
  
06.02.015

**Message value:**
  
Fault cause: %1 bin

**Message class:**
  
General drive fault (19)

**Component:**
  
Motor

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The selected service/maintenance interval for this motor was reached.  
Alarm value (r2124, interpret decimal):  
Motor data set number.

**Remedy**
  
carry out service/maintenance and reset the service/maintenance interval (p0651).

### C01717 SI: SLA limit exceeded

**Valid as of version:**
  
06.03.014

**Message value:**
  
%1

**Message class:**
  
Safety monitoring channel has identified an error (10)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The acceleration limit for function SLA was exceeded. The drive is stopped as a result
of the configured stop response (p9579).  
Message value (r60049, interpret decimal):  
0: The monitoring of the coarsely resolved acceleration has violated the acceleration
limit.  
1: The monitoring of the finely resolved acceleration and possibly filtered acceleration
has violated the acceleration limit.

**Remedy**
  
- Check the traversing/motion program in the control.  
- Check the acceleration limit for the SLA function and if required, adapt (p9578).  
- Carry out a safe acknowledgment.  
For message value = 0:  
Analyze the causes using r9714[0] and r9714[3].  
For message value = 1:  
Analyze the causes using r9789[0], r9789[1] and r9789[2].  
Note:  
SI: Safety Integrated  
SLA: Safely-Limited Acceleration

### F01800 Internal communications faulted

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**

**Remedy**
  
Replace the component involved.

### A01900 PN: Configuration telegram error

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
A controller attempts to establish a connection using an incorrect configuring telegram.  
Alarm value (r2124, interpret decimal):  
2:  
Too many PZD data words for output or input. The number of possible PZD is specified
by the number of indices in r2050/r2053.  
3:  
Uneven number of bytes for input or output.  
4:  
Setting data for synchronization not accepted. For more information, see A01902.  
211:  
Unknown parameterizing block.  
Additional values:  
Only for internal Siemens troubleshooting.

**Remedy**
  
Check the bus configuration on the controller and device sides.

### A01902 PN: Isochronous operation parameterization not permissible

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
Parameterization for isochronous operation is not permissible.  
Alarm value (r2124, interpret decimal):  
0: Bus cycle time Tdp < 0.5 ms.  
1: Bus cycle time Tdp > 32 ms.  
2: Bus cycle time Tdp is not an integer multiple of the current controller sampling
time.  
3: Instant of the actual value sensing Ti > Bus cycle time Tdp or Ti = 0.  
4: Instant of the actual value sensing Ti is not an integer multiple of the current
controller sampling time.  
5: Instant of the setpoint acceptance To >= Bus cycle time Tdp or To = 0.  
6: Instant of the setpoint acceptance To is not an integer multiple of the current
controller sampling time.  
7: Controller application cycle time Tmapc is not an integer multiple of the speed
controller sampling time.  
8: Bus reserve bus cycle time Tdp - Data exchange time Tdx less than two current controller
sampling times.  
10: Instant of the setpoint acceptance To <= data exchange time Tdx + current controller
sampling time  
11: Controller application cycle time Tmapc > 14 x Tdp or Tmapc = 0.  
12: PLL tolerance window Tpll_w > Tpll_w_max.  
13: Bus cycle time Tdp is not a multiple of the speed controller clock cycle.

**Remedy**
  
- Adapt the bus parameterization Tdp, Ti, To.  
- Adapt the sampling time for the current controller or speed controller.  
For alarm value = 10:  
- Reduce Tdx by using fewer bus participants or shorter telegrams.  
Note:  
PB: PROFIBUS  
PN: PROFINET

### A01904 PN: Controller setting of the PZD telegram rejected

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Communication error to the higher-level control system (9)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
A controller attempts to set a PZD telegram. The setting is not applied.  
Alarm value (r2124, interpret decimal):  
3: Controllers have no function rights for making changes.  
4: Telegram cannot be set as a result of the drive configuration.  
See also: r0922 (PROFIdrive PZD telegram selection)

**Remedy**
  
Check and align the telegram settings in the drive project and in the controller.

### A01905 PN: Controller setting to activate the channel diagnostics rejected

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Communication error to the higher-level control system (9)

**Component:**
  
Control Unit (CU)

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
A controller attempted to change the activation of the channel diagnostics. The setting
is not applied as the controller does not have the function rights to make a change.  
Alarm value (r2124, interpret decimal):  
1: Channel diagnostics are activated. Controller attempts to deactivate them.  
2: Channel diagnostics are not activated. Controller attempts to activate them.

**Remedy**
  
Activate channel diagnostics in the bus configuration and check and align function
rights in the drive.

### F01910 Fieldbus: setpoint timeout

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Communication error to the higher-level control system (9)

**Component:**
  
None

**Response:**
  
 OFF3

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The reception of setpoints from the fieldbus interface (PROFINET) is interrupted.  
- Bus connection interrupted.  
- Controller switched off.  
- Controller set into the STOP state.

**Remedy**
  
Restore the bus connection and set the controller to RUN.

### F01911 PN: Isochronous operation, clock cycle failure

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Communication error to the higher-level control system (9)

**Component:**
  
None

**Response:**
  
 OFF1

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The telegram to synchronize the clock cycles has failed for several bus clock cycles
or in several bus clock cycles has consecutively violated the specified time grid
(see bus cycle time, Tdp and Tpllw).

**Remedy**
  
- Check the physical bus configuration (cable, connector, terminating resistor, shielding,
etc.).  
- Check whether communication was briefly or permanently interrupted.  
- Check the utilization level of the bus and controller (e.g. bus cycle time Tdp was
set too short).  
Note:  
PN: PROFINET

### F01912 PN: Isochronous operation sign-of-life missing

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Communication error to the higher-level control system (9)

**Component:**
  
None

**Response:**
  
 OFF1

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The maximum permissible number of errors in the controller sign-of-life (isochronous
operation) has been exceeded in cyclic operation.

**Remedy**
  
- Check the physical bus configuration (cables, connectors, etc.).  
- Check whether the controller correctly sends the sign-of-life (e.g. create a trace
with STW2.12 ... STW2.15 and trigger signal ZSW1.3).  
- Check the permissible telegram failure rate (p0925).  
- Check the utilization level of the bus and controller (e.g. bus cycle time Tdp was
set too short).  
Note:  
PN: PROFINET

### F01916 Internal communications error

**Valid as of version:**
  
06.03.014

**Message value:**
  
-

**Message class:**
  
Communication error to the higher-level control system (9)

**Component:**
  
None

**Response:**
  
 OFF1

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
An internal Ethernet communications error has occurred.

**Remedy**
  
- Carry out a POWER ON (switch-off/switch-on) for all components.  
- Upgrade firmware to later version.  
- Contact Technical Support.

### A01932 PN: Clock cycle synchronization missing for DSC

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
There is no clock synchronization or clock synchronous sign of life and DSC is selected.  
Note:  
DSC: Dynamic Servo Control  
See also: r0922 (PROFIdrive PZD telegram selection)

**Remedy**
  
Set clock synchronization across the bus configuration and transfer clock synchronous
sign-of-life.

### A01940 PB/PN: clock cycle synchronism not reached

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Communication error to the higher-level control system (9)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The bus is in the data exchange state and clock synchronous operation has been selected
using the parameterizing telegram. Synchronization with the clock cycle specified
by the controller was still not able to be performed.  
- The controller does not send an isochronous telegram, although isochronous operation
was selected when configuring the bus.  
- The controller uses another isochronous bus clock cycle than was transferred to
the device in the parameterizing telegram.

**Remedy**
  
- Check the controller application and bus configuration.  
- Check the consistency between the clock cycle input when configuring the device
and clock cycle setting at the controller.  
Note:  
PB: PROFIBUS  
PN: PROFINET

### A01941 PN: Clock cycle signal missing when the bus is being established

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Communication error to the higher-level control system (9)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The bus is in the data exchange state and clock synchronous operation has been selected
using the parameterizing telegram. The synchronization telegram is not received.

**Remedy**
  
Check the controller application and bus configuration.  
Note:  
PN: PROFINET

### A01943 PN: Clock cycle signal error when the bus is being established

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Communication error to the higher-level control system (9)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The bus is in the data exchange state and clock synchronous operation has been selected
using the parameterizing telegram.  
The synchronization telegram is irregularly received.  
- The controller sends an irregular synchronization telegram.  
- The controller uses another isochronous bus clock cycle than was transferred to
the device in the parameterizing telegram.

**Remedy**
  
- Check the controller application and bus configuration.  
- Check the consistency between the clock cycle input when configuring the device
and clock cycle setting at the controller.  
Note:  
PN: PROFINET

### A01944 PN: Sign-of-life synchronism not reached

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Communication error to the higher-level control system (9)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The bus is in the data exchange state and clock synchronous operation has been selected
using the parameterizing telegram.  
Synchronization with the controller sign-of-life (STW2.12 ... STW2.15) could not be
completed because the sign-of-life changes differently to how it was configured in
the Tmapc time grid.

**Remedy**
  
- Ensure that the controller correctly increments the sign-of-life in the controller
application clock cycle Tmapc.  
Note:  
PN: PROFINET

### F01950 PN: Isochronous operation, synchronization unsuccessful

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Communication error to the higher-level control system (9)

**Component:**
  
None

**Response:**
  
 OFF1

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
Synchronization of the internal clock cycle to the controller clock cycle has failed.
The internal clock cycle exhibits an unexpected shift.

**Remedy**
  
Only for internal Siemens troubleshooting.  
Note:  
PN: PROFINET

### A01980 PN: cyclic connection interrupted

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Communication error to the higher-level control system (9)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The cyclic connection to the PROFINET controller is interrupted.  
See also: r8936 (PN cyclic connection state)

**Remedy**
  
Establish the PROFINET connection and activate the PROFINET controller in the cyclic
mode.  
Check parameters "Name of Station" and "IP of Station".

### A01981 PN: Maximum number of controllers exceeded

**Valid as of version:**
  
06.02.015

**Message value:**
  
Info 1: %1, Info 2: %2

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
A controller attempts to establish a connection to the drive, and as a consequence
exceeds the permitted number of PROFINET connections.  
The alarm is automatically withdrawn after approx. 30 seconds.  
Alarm value (r2124, interpret hexadecimal):  
yyyyxxxx hex: yyyy = info. 1, xxxx = info. 2  
Info 1 = 0: number of RT connections exceeded  
Info 1 > 0: number of IRT connections exceeded  
Info 2: permitted number of connections

**Remedy**
  
Check the configuration of the PROFINET controllers.

### A01989 PN: internal cyclic data transfer error

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Communication error to the higher-level control system (9)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The cyclic actual values and/or setpoints were not transferred within the specified
times.  
Alarm value (r2124, interpret hexadecimal):  
Only for internal Siemens troubleshooting.

**Remedy**
  
Correctly set T_io_input or T_io_output.

### A02000 Function generator: Start not possible

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The function generator has already been started.

**Remedy**
  
Stop the function generator and restart again if necessary.  
Note:  
The alarm is reset as follows:  
- Remove the cause of this alarm.  
- Restart the function generator.

### A02006 Function generator: No drive specified for connection

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
No drive specified for connection was specified.

**Remedy**
  
At least one drive to be connected must be specified.  
Note:  
The alarm is reset as follows:  
- Remove the cause of this alarm.  
- Restart the function generator.

### A02010 Function generator: Speed setpoint from the drive is not zero

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The speed setpoint of a drive selected for connection is greater than the value for
the standstill detection set using p1226.

**Remedy**
  
For all of the drives specified for connection, set the speed setpoints to zero.  
Note:  
The alarm is reset as follows:  
- Remove the cause of this alarm.  
- Restart the function generator.

### A02020 Function generator: Parameter cannot be changed

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
This parameter setting cannot be changed when the function generator is active.

**Remedy**
  
- Stop the function generator before parameterizing.  
- Possibly start the function generator.  
Note:  
The alarm is reset as follows:  
- Remove the cause of this alarm.  
- Restart the function generator.

### A02026 Function generator: Pulse width too high

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The selected pulse width is too high.  
The pulse width must be less than the period duration.

**Remedy**
  
Reduce pulse width.  
Note:  
The alarm is reset as follows:  
- Remove the cause of this alarm.  
- Restart the function generator.

### A02030 Function generator: Physical address equals zero

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The specified physical address is zero.

**Remedy**
  
Set a physical address with a value other than zero.  
Note:  
The alarm is reset as follows:  
- Remove the cause of this alarm.  
- Restart the function generator.

## SINAMICS Alarms S200 Basic PN 02040 - 07482

SINAMICS Alarms S200 Basic PN 02040 - 07482

### A02040 Function generator: Illegal value for offset

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The value for the offset is higher than the value for the upper limit or lower than
the value for the lower limit.

**Remedy**
  
Adjust the offset value accordingly.  
Note:  
The alarm is reset as follows:  
- Remove the cause of this alarm.  
- Restart the function generator.

### A02041 Function generator: Illegal value for bandwidth

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The bandwidth referred to the time slice clock cycle of the function generator has
either been set too low or too high.  
Depending on the time slice clock cycle, the bandwidth is defined as follows:  
Bandwidth_max = 1 / (2 x time slice clock cycle)  
Bandwidth_min = Bandwidth_max / 100000  
Example:  
Assumption: Time slice clock cycle = 125 µs  
--> Bandwidth_max = 1 / (2 x 125 µs) = 4000 Hz  
--> Bandwidth_min = 4000 Hz / 100000 = 0.04 Hz

**Remedy**
  
Check the value for the bandwidth and adapt accordingly.  
Note:  
The alarm is reset as follows:  
- Remove the cause of this alarm.  
- Restart the function generator.

### A02047 Function generator: Time slice clock cycle invalid

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The time slice clock cycle selected does not match any of the existing time slices.

**Remedy**
  
Enter an existing time slice clock cycle. The fastest cycle time can be read out using
the commissioning tool.  
Note:  
The alarm is reset as follows:  
- Remove the cause of this alarm.  
- Restart the function generator.

### A02050 Trace: Start not possible

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The trace has already been started.

**Remedy**
  
Stop the trace and, if necessary, start again.

### A02051 Trace: recording not possible as a result of know-how protection

**Valid as of version:**
  
06.02.015

**Message value:**
  
initiating recorder: %1, parameter %2

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause | Remedy |
| For %1 | 1 | Recorder 0 |  |
| 2 | Recorder 1 |  |  |
| 3 | Recorders 0 and 1 |  |  |

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
TRACE recording is not possible as at least one signal or trigger signal being used
is under know-how protection.  
Alarm value (r2124, interpret hexadecimal):  
bbbbaaaa hex:  
aaaa = 1: recorder 0  
aaaa = 2: recorder 1  
aaaa = 3: recorders 0 and 1  
bbbb = parameter number (hexadecimal), that was not able to be written to.

**Remedy**
  
- Temporarily activate or deactivate know-how protection (p7766).  
- Include the signal in the OEM exception list (p7763, p7764).  
- Where relevant do not record the signal.

### A02055 Trace: Recording time too short

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The trace duration is too short.  
The minimum is twice the value of the trace clock cycle.

**Remedy**
  
Check the selected recording time and, if necessary, adjust.

### A02056 Trace: Recording cycle too short

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The selected recording clock cycle is shorter than the selected basic clock cycle
0.

**Remedy**
  
Increase the value for the trace cycle. The fastest cycle time can be read out using
the commissioning tool.

### A02057 Trace: Time slice clock cycle invalid

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The time slice clock cycle selected does not match any of the existing time slices.

**Remedy**
  
Enter an existing time slice clock cycle. The fastest cycle time can be read out using
the commissioning tool.

### A02059 Trace: Time slice clock cycle for 2 x 8 recording channels not valid

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The selected time slice clock cycle cannot be used for more than 4 recording channels.

**Remedy**
  
Enter the clock cycle of an existing time slice with a cycle time >= 4 ms or reduce
the number of recording channels to 4 per trace.  
The fastest cycle time can be read out using the commissioning tool.

### A02060 Trace: Signal to be traced missing

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
- A signal to be traced was not specified.  
- The specified signals are not valid.

**Remedy**
  
- Specify the signal to be traced.  
- Check whether the relevant signal can be traced.

### A02062 Trace: Invalid trigger signal

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
- A trigger signal was not specified.  
- The specified signal does not exist.  
- The specified signal is not a fixed-point signal.  
- The specified signal cannot be used as a trigger signal for the trace.

**Remedy**
  
Specify a valid trigger signal.

### A02063 Trace: Invalid data type

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The specified data type to select a signal using a physical address is invalid.

**Remedy**
  
Use a valid data type.

### A02070 Trace: Parameter cannot be changed

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The trace parameter settings cannot be changed when the trace is active.

**Remedy**
  
- Stop the trace before parameterization.  
- If required, start the trace.

### A02075 Trace: Pretrigger time too long

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The selected pretrigger time must be shorter than the trace time.

**Remedy**
  
Check the pretrigger time setting and change if necessary.

### F02080 Trace: Parameterization deleted due to unit changeover

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The trace parameterization in the drive unit was deleted due to a unit changeover
or a change in the reference parameters.

**Remedy**
  
Restart trace.

### A02085 Message function: Parameterization error

**Valid as of version:**
  
06.02.015

**Message value:**
  
Parameter: %1, index:%2

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
Power Unit

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
A parameterization error was identified when starting the variable message function.  
Alarm value (r2124, interpret decimal):  
yyxxxx dec: yy = index, xxxx = parameter

**Remedy**
  
Correct the parameter and restart.  
Note:  
The alarm is automatically withdrawn when stopping, or when successfully starting
the variable message function.

### A02096 MTrace 0: cannot be saved

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
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

**Remedy**
  
- Insert or remove the memory card.  
- Use a larger memory card.  
- Configure a longer trace time or use an endless trace.  
- Avoid saving parameters while a multiple trace is running.  
- Check whether other functions are presently accessing measurement result files.

### A02098 MTrace 1: cannot be saved

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
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

**Remedy**
  
- Insert or remove the memory card.  
- Use a larger memory card.  
- Configure a longer trace time or use an endless trace.  
- Avoid saving parameters while a multiple trace is running.  
- Check whether other functions are presently accessing measurement result files.

### A02099 Trace: Insufficient Control Unit memory

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The memory space still available on the Control Unit is no longer sufficient for the
trace function.

**Remedy**
  
Reduce the memory required, e.g. as follows:  
- Reduce the trace time.  
- Increase the trace clock cycle.  
- Reduce the number of signals to be traced.

### A02150 TEC: Technology Extension cannot be loaded

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The system was not able to load a Technology Extension.  
Alarm value (r2124, interpret hexadecimal):  
10 hex (16 dec):  
The interface version in the DCB user library is not compatible to the DCC standard
library that has been loaded.  
12 hex (18 dec):  
A technology package was not able to be downloaded to a Control Unit because the warm
restart necessary was not able to be performed.  
Only for internal Siemens troubleshooting.

**Remedy**
  
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

### F02151 TEC: internal software error

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

**Component:**
  
None

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
An internal software error has occurred within a Technology Extension.  
Fault value (r0949, interpret hexadecimal):  
Only for internal Siemens troubleshooting.

**Remedy**
  
- Carry out a POWER ON (switch-off/switch-on) for all components.  
- Upgrade firmware to later version.  
- Contact Technical Support.  
- Replace the Control Unit.  
Note:  
TEC: Technology Extension

### F02152 TEC: insufficient memory

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

**Component:**
  
None

**Response:**
  
 OFF1

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The functionality on this Control Unit is too extensive (e.g. too many drives, functions,
data sets, Technology Extensions, blocks, etc).  
Fault value (r0949, interpret decimal):  
Only for internal Siemens troubleshooting.

**Remedy**
  
- Change the configuration on this Control Unit, e.g.  
-- Use fewer axes  
-- Reduce the number of configurable functions  
-- Use fewer data sets  
-- Reduce Technology Extensions and blocks  
- Use an additional Control Unit.

### F02153 TEC: technology function does not exist

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Hardware/software error (1)

**Component:**
  
None

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
A technology function (e.g. Technology Extension, DCB library) does not exist on the
drive device.  
When configuring, a technology function is activated, which does not exist on the
drive device. This can occur when downloading a project or when powering up.

**Remedy**
  
- Load the required technology function to the drive device.  
- If required, deactivate the technology function not required in the configuration.  
Note:  
DCB: Drive Control Block  
TEC: Technology Extension

### F03001 NVRAM checksum incorrect

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Control Unit (CU)

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
A checksum error occurred when evaluating the non-volatile data (NVRAM) on the converter.  
The NVRAM data affected was deleted.

**Remedy**
  
Carry out a POWER ON (switch-off/switch-on) for all components.

### A03506 24 V power supply missing

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Supply voltage fault (undervoltage) (3)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The 24 V power supply for the digital outputs (X124) is missing.

**Remedy**
  
Check the terminals for the power supply voltage (X124, L1+, M).

### F03590 TM: Module not ready

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
Terminal Module (TM)

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The Terminal Module involved does not send a ready signal and no valid cyclic data.  
Fault value (r0949, interpret decimal):  
Drive object number of the Terminal Module involved.

**Remedy**
  
- Check the 24 V power supply.  
- Check the DRIVE-CLiQ wiring.

### F05055 Parallel connection: Power units with illegal code numbers

**Valid as of version:**
  
06.02.015

**Message value:**
  
Parameter: %1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The code numbers of the power units do not match.  
Fault value (r0949, interpret decimal):  
Parameter in which the first different power unit code number was detected.

**Remedy**
  
Use power units with the same code number.  
For parallel circuit configurations, only power units with identical power unit data
may be used.

### F05056 Parallel circuit: Power unit EEPROM versions differ

**Valid as of version:**
  
06.02.015

**Message value:**
  
Parameter: %1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The EEPROM versions of the power units do not match.  
Fault value (r0949, interpret decimal):  
Parameter in which the first different version number was detected.

**Remedy**
  
Use power units with the same EEPROM version.  
Note:  
For parallel circuit configurations, only power units with identical EEPROM versions
may be used.

### F05057 Parallel circuit: Power unit firmware versions differ

**Valid as of version:**
  
06.02.015

**Message value:**
  
Parameter: %1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The firmware versions of the power units connected in parallel do not match.  
Fault value (r0949, interpret decimal):  
Parameter in which the first different version number was detected.

**Remedy**
  
Use power units with the same firmware version.  
For parallel circuit configurations, only power units with identical firmware versions
may be used.

### F05058 Parallel circuit: VSM EEPROM versions differ

**Valid as of version:**
  
06.02.015

**Message value:**
  
Parameter: %1

**Message class:**
  
General drive fault (19)

**Component:**
  
Voltage Sensing Module (VSM)

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The EEPROM versions of the Voltage Sensing Modules (VSM) do not match.  
Fault value (r0949, interpret decimal):  
Parameter in which the first different version number was detected.

**Remedy**
  
For parallel circuit configurations, only Voltage Sensing Modules (VSM) with identical
EEPROM versions may be used.

### F05059 Parallel circuit: VSM firmware versions differ

**Valid as of version:**
  
06.02.015

**Message value:**
  
Parameter: %1

**Message class:**
  
General drive fault (19)

**Component:**
  
Voltage Sensing Module (VSM)

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The firmware versions of the Voltage Sensing Module (VSM) do not match.  
Fault value (r0949, interpret decimal):  
Parameter in which the first different version number was detected.

**Remedy**
  
For parallel circuit configurations, only Voltage Sensing Modules (VSM) with identical
firmware versions may be used.

### F05060 Parallel circuit: Power unit firmware version does not match

**Valid as of version:**
  
06.02.015

**Message value:**
  
Parameter: %1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
Firmware from version V02.30.01.00 is required when connecting the power units in
parallel.

**Remedy**
  
Update the firmware of the power units (at least V02.30.01.00).

### F05068 Parallel connection: AIM EEPROM versions different

**Valid as of version:**
  
06.03.014

**Message value:**
  
Parameter: %1

**Message class:**
  
General drive fault (19)

**Component:**
  
-

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The EEPROM versions of the Active Interface Module (AIM) do not match.  
Fault value (r0949, interpret decimal):  
Parameter in which the first different version number was detected.

**Remedy**
  
For parallel connections, only Active Interface Modules (AIM) with identical EEPROM
versions may be used.

### F05069 Parallel connection: AIM firmware versions different

**Valid as of version:**
  
06.03.014

**Message value:**
  
Parameter: %1

**Message class:**
  
General drive fault (19)

**Component:**
  
-

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The firmware versions of the Active Interface Module (AIM) do not match.  
Fault value (r0949, interpret decimal):  
Parameter in which the first different version number was detected.

**Remedy**
  
For parallel connections, only Active Interface Modules (AIM) with identical firmware
versions may be used.

### F06310 Supply voltage (p0210) incorrectly parameterized

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Network fault (2)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
For AC/AC drive units, the measured DC link voltage lies outside the tolerance range
after precharging has been completed.  
The following applies for the tolerance range: 1.16 * p0210 < r0070 < 1.6 * p0210  
Note:  
The fault can only be acknowledged when the drive is switched off.  
See also: p0210 (Device supply voltage)

**Remedy**
  
- Check the parameterized supply voltage and if required change (p0210).  
- Check the line voltage.  
See also: p0210 (Device supply voltage)

### F07011 Drive: Motor overtemperature

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Motor overload (8)

**Component:**
  
Motor

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The calculated motor temperature is too high.  
Possible causes:  
- Motor overloaded.  
- Motor ambient temperature too high.  
- Sensor wire breakage.  
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
400:  
Additional motor overload protection: the load is too high.

**Remedy**
  
- Reduce the motor load.  
- Check the ambient temperature and the motor ventilation.  
- Check the wiring and temperature sensor connection.  
- Check monitoring limits.  
- Check activation of the additional motor overload protection (5375).

### A07012 Drive: Motor temperature model overtemperature

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Motor overload (8)

**Component:**
  
Motor

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
Motor temperature model 1/3 or the additional motor overload protection identified
that the alarm threshold was exceeded.  
Hysteresis:2K  
Alarm value (r2124, interpret decimal):  
200:  
Motor temperature model 1 (I2t): temperature too high.  
300:  
Motor temperature model 3: temperature too high.  
400:  
Additional motor overload protection: the load is too high. If the load remains at
this level, the drive is shut down with fault F07011.  
See also: r0034, p0613

**Remedy**
  
- Check the motor load and if required, reduce.  
- Check the motor ambient temperature.  
- Check activation of the additional motor overload protection (p5375).  
See also: r0034 (Motor utilization thermal)

### F07082 Macro: Execution not possible

**Valid as of version:**
  
06.02.015

**Message value:**
  
Fault cause: %1, supplementary information: %2, preliminary parameter number: %3

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
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
37: Source parameter for a signal interconnection was not able to be determined.  
38: An index was set for a non-indexed (or CDS-dependent) parameter.  
39: No index was set for an indexed parameter.  
41: A bit operation is only permissible for parameters with the parameter format DISPLAY_BIN.  
42: A value not equal to 0 or 1 was set for a bit operation.  
43: Reading the parameter to be changed by the bit operation was unsuccessful.  
51: Factory setting for DEVICE may only be executed on the DEVICE.  
61: The setting of a value was unsuccessful.

**Remedy**
  
- Check the parameter involved.  
- Check the macro file and signal interconnection.

### F07083 Template: ACX file not found

**Valid as of version:**
  
06.02.015

**Message value:**
  
Parameter: %1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The template to be executed was not able to be found.  
Fault value (r0949, interpret decimal):  
Parameter number with which the execution was started.

**Remedy**
  
- Check whether the corresponding template number is available.

### F07084 Macro: Condition for WaitUntil not fulfilled

**Valid as of version:**
  
06.02.015

**Message value:**
  
Parameter: %1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The WaitUntil condition set in the macro was not fulfilled in a certain number of
attempts.  
Fault value (r0949, interpret decimal):  
Parameter number for which the condition was set.

**Remedy**
  
Check and correct the conditions for the WaitUntil loop.

### F07085 Drive: Open-loop/closed-loop control parameters changed

**Valid as of version:**
  
06.02.015

**Message value:**
  
Parameter: %1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
Open-loop/closed-loop control parameters have had to be changed.  
Possible causes:  
1. As a result of other parameters, they have exceeded the dynamic limits.  
2. They cannot be used due to the fact that the hardware detected not having certain
features.  
3. The value is estimated as the thermal time constant is missing.  
4. Motor temperature model 1 is activated as thermal motor protection is missing.  
See also: p1082 (Maximum speed)

**Remedy**
  
Not necessary.  
It is not necessary to change the parameters as they have already been correctly limited.

### F07086 Units changeover: Parameter limit violation due to reference value change

**Valid as of version:**
  
06.02.015

**Message value:**
  
Parameter: %1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
A reference parameter was changed in the system. This resulted in the fact that for
the parameters involved, the selected value was not able to be written in the per
unit notation.  
The values of the parameters were set to the corresponding violated minimum limit/maximum
limit or to the factory setting.  
Possible causes:  
- The steady-state minimum limit/maximum limit or that defined in the application
was violated.  
Fault value (r0949, parameter):  
Diagnostics parameter to display the parameters that were not able to be re-calculated.  
See also: p0304, p0305, p2000, p2002, p2003

**Remedy**
  
Check the adapted parameter value and if required correct.

### F07088 Units changeover: Parameter limit violation due to units changeover

**Valid as of version:**
  
06.02.015

**Message value:**
  
Parameter: %1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
A changeover of units was initiated. This resulted in a violation of a parameter limit  
Possible causes for the violation of a parameter limit:  
- When rounding off a parameter corresponding to its decimal places, the steady-state
minimum limit or maximum limit was violated.  
- Inaccuracies for the data type "FloatingPoint".  
In these cases, when the minimum limit is violated then the parameter value is rounded
up and when the maximum limited is violated the parameter value is rounded down.  
Fault value (r0949, interpret decimal).

**Remedy**
  
Check the adapted parameter values and if required correct.

### A07089 Unit switchover: Function activation is blocked because the units have been switched over

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
An attempt was made to activate a function. This is not permissible if the units have
already been changed over.

**Remedy**
  
Restore units that have been changed over to the factory setting.

### F07090 Drive: Upper torque limit less than the lower torque limit

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The upper torque limit is lower than the lower torque limit.

**Remedy**
  
When setting the torque limits via telegram 750, the positive torque limit must be
>= the negative torque.

### A07091 Drive: determined current controller dynamic response invalid

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
Control Unit (CU)

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
When One Button Tuning is activated (p5300 = 1), the current controller is measured
after the pulses have been enabled. Evaluation has indicated that the current control
loop was not appropriately set.  
Possible causes:  
- Incorrectly set current controller.  
- PRBS amplitude set too high (p5296).  
Alarm value (r2124, interpret hexadecimal):  
1: Dynamic response too low.  
2: Current controller unstable.  
Note:  
PRBS: Pseudo Random Binary Signal (binary noise)

**Remedy**
  
- The measurement can be repeated with a smaller excitation amplitude (p5296).

### A07092 Drive: moment of inertia estimator still not ready

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
Control Unit (CU)

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The moment of inertia estimator has still not determined any valid values.  
The acceleration cannot be calculated.  
The moment of inertia estimator has stabilized, if the frictional values as well as
the moment of inertia were determined and the corresponding status signal is set.

**Remedy**
  
Traverse the axis until the moment of inertia estimator has stabilized.  
This alarm is automatically withdrawn after the moment of inertia estimator has stabilized.

### F07093 Drive: Test signal error

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
Control Unit (CU)

**Response:**
  
 OFF3

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
An error was identified when executing the "Test signal" function.  
The function was not executed or was canceled.  
Fault value (r0949, interpret decimal):  
1: No distance limit has been defined (p5308 = 0).  
2: The moment of inertia estimator has not stabilized in the parameterized time (p5309).  
3: The parameterized distance (p5308) was exceeded.  
4: No motor encoder parameterized (closed-loop speed control without encoder).  
6: Pulse enable was withdrawn while traversing.  
7: speed setpoint not equal to zero.  
See also: p5308, p5309

**Remedy**
  
For fault value = 1:  
- Define distance limiting (p5308).  
For fault value = 2:  
- Increase the duration, distance limit or speed limit (p5309, p5308, p1082, p1083,
p1086).  
For fault value = 3:  
- Check distance limiting (p5308).  
For fault value = 4:  
- Configure speed control with encoder.  
For fault value = 6:  
- Keep the drive switched on until the "Test signal" function has been completely
exited.  
For fault value = 7:  
- Set the speed setpoint to zero. It is possible that the setpoint was specified from
the control panel.

### A07094 General parameter limit violation

**Valid as of version:**
  
06.02.015

**Message value:**
  
Parameter: %1

**Message class:**
  
Hardware/software error (1)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
As a result of the violation of a parameter limit, the parameter value was automatically
corrected.  
Minimum limit violated --> parameter is set to the minimum value.  
Maximum limit violated --> parameter is set to the maximum value.  
Alarm value (r2124, interpret decimal):  
Parameter number, whose value had to be adapted.

**Remedy**
  
Check the adapted parameter values and if required correct.

### A07095 Drive: One Button Tuning activated

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The One Button Tuning function is active.  
One Button Tuning is performed at the next switch-on command.  
See also: p5300 (Autotuning selection)

**Remedy**
  
Not necessary.  
The alarm is automatically withdrawn after One Button Tuning has been exited (p5300
= 0).

### F07097 Drive: Test signal error distance limiting

**Valid as of version:**
  
06.02.015

**Message value:**
  
Fault cause: %1, traversing distance: %2

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
Control Unit (CU)

**Response:**
  
 OFF3

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
An error was identified when executing function "Test signal" or One Button Tuning
selection (p5300 = 1).  
The function was not executed or was canceled.  
Fault value (r0949, interpret decimal):  
yyyyxxxx hex: yyyy = fault cause, xxxx = traversing distance.  
See also: p5308, p5309

**Remedy**
  
- Enter the traversing path in parameter p5308 - or deselect the function involved
in p5301.  
- For fault cause = 1, 2, shorter traversing paths may be possible.  
For fault cause = 1:  
- Deselect bit 0 and bit 1 in parameter p5301.  
For fault cause = 2:  
- Deselect bit 2 in parameter p5301.  
For fault cause = 3:  
- Deselect bit 4 and bit 5 in parameter p5301.

### A07200 Drive: Master control ON command present

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The ON/OFF1 command is present (no 0 signal).  
The command is either influenced via binary signal sink c0840 (actual CDS) or control
word bit 0 via the master control.

**Remedy**
  
Switch the signal to 0 via binary signal sink c0840 (actual CDS) or control word bit
0 via the master control.

### F07220 Drive: Master control by PLC missing

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Communication error to the higher-level control system (9)

**Component:**
  
None

**Response:**
  
 OFF1

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The "master control by PLC" signal was missing in operation.  
- The higher-level control has withdrawn the "master control by PLC" signal.  
- Data transfer via the fieldbus (controller/drive) was interrupted.

**Remedy**
  
- Check the "master control by PLC" signal and, if required, switch in.  
- Check data transfer via the fieldbus (controller/drive).  
Note:  
If the drive should continue to operate after withdrawing "master control by PLC",
then the fault response must be parameterized to NONE or the message type should be
parameterized as alarm.

### F07300 Drive: Line contactor feedback signal missing

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Auxiliary unit faulted (20)

**Component:**
  
None

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
- The line contactor was not able to be closed within the time in p0861.  
- The line contactor was not able to be opened within the time in p0861.  
- The line contactor dropped out during operation  
- The line contactor has closed although the drive converter is switched off.

**Remedy**
  
- Check the setting of p0860.  
- Check the feedback circuit from the line contactor.  
- Increase the monitoring time in p0861.

### A07350 Drive: Measuring probe parameterized to a digital output

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The measuring probe is connected to a bidirectional digital input/output and the terminal
is set as output.  
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

**Remedy**
  
- Deselect measuring probe (p0488, p0489).

### F07410 Drive: Current controller output limited

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Application/technological function faulted (17)

**Component:**
  
None

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The condition "I_act = 0 and Uq_set_1 longer than 16 ms at its limit" is present and
can be caused by the following:  
- Motor not connected or motor contactor open.  
- No DC link voltage present.  
- Power unit defective.

**Remedy**
  
- Connect the motor or check the motor contactor.  
- Check the DC link voltage (r0070).  
- Check the power unit.

### F07412 Drive: Commutation angle incorrect (motor model)

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Position/speed actual value incorrect or not available (11)

**Component:**
  
None

**Response:**
  
 ENCODER

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
An incorrect commutation angle was detected, which can result in a positive coupling
in the speed controller.  
Possible causes:  
- The phase sequence of the output phases for the motor is incorrect (e.g. the phases
are interchanged).  
- The motor encoder is incorrectly adjusted with respect to the magnet position.  
- The motor encoder is damaged.  
- The motor encoder speed signal is faulted.  
- The control loop is instable due to incorrect parameterization.

**Remedy**
  
- Check the phase sequence for the motor, and if required, correct.  
- If the encoder mounting was changed, re-adjust the encoder.  
- Replace the defective motor and/or motor encoder.

### F07419 Drive: Current setpoint filter adaptation error

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 OFF1

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
An error has occurred when configuring or when using the "Current setpoint filter
adaptation" function.  
Fault value (r0949, interpret binary):  
Bit 2: the assigned filter is a type or has a characteristic, which is unsuitable
for adaptation.  
Bit 3: the assigned filter has not been activated (p1656).  
Bits 0, 1, 4 ... 31: internal fault occurred.

**Remedy**
  
The remedy should be applied depending on the fault value.  
For bit 2:  
Set the filter type "General filter 2nd order" and set the characteristic of a bandstop
filter.  
For bit 3:  
Activate filter (p1656).  
For bits 0, 1, 4 ... 15:  
- Carry out a POWER ON (switch-off/switch-on) for all components.  
- Upgrade firmware to later version.

### F07420 Drive: Current setpoint filter natural frequency > Shannon frequency

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
One of the filter natural frequencies is greater than the Shannon frequency.  
The Shannon frequency is calculated according to the following formula: 0.5 / current
controller sampling time  
Fault value (r0949, interpret binary):  
Bit 0: Filter 1 (p1658, p1660)  
Bit 1: Filter 2 (p1663, p1665)  
Bit 2: Filter 3 (p1668, p1670)  
Bit 3: Filter 4 (p1673, p1675)

**Remedy**
  
- Reduce the numerator or denominator natural frequency of the current setpoint filter
involved.  
- Deactivate the filter involved (p1656).

### F07421 Drive: Speed filter natural frequency > Shannon frequency

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
One of the filter natural frequencies is greater than the Shannon frequency.  
The Shannon frequency is calculated according to the following formula: 0.5 / speed
controller sampling time.  
Fault value (r0949, interpret binary):  
Bit 0: Filter 1 (p1417, p1419)  
Bit 1: Filter 2 (p1423, p1425)

**Remedy**
  
- Reduce the numerator or denominator natural frequency of the speed setpoint filter
involved.  
- Deactivate the filter involved (p1414).

### F07422 Drive: Reference model natural frequency > Shannon frequency

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The natural filter frequency of the PT2 element for the reference model (p1433) is
greater than the Shannon frequency.  
The Shannon frequency is calculated according to the following formula: 0.5 / speed
controller sampling time.

**Remedy**
  
- Reduce the natural frequency of PT2 element for reference model (p1433).

### F07432 Drive: Motor without overvoltage protection

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
In the case of a fault at maximum speed, the motor can generate an overvoltage that
can destroy the converter.

**Remedy**
  
Limit the maximum speed (p1082) without any additional protection.  
Note:  
The maximum speed is calculated as follows:  
p1082 <= 11.695 * DC link voltage overvoltage threshold/r0316  
DC link voltage overvoltage threshold:  
- Line connection 1 AC: 410 V  
- Line connection 3 AC: 820 V  
See also: r0316, p1082

### F07434 Drive: It is not possible to change the direction of rotation with the pulses enabled

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Application/technological function faulted (17)

**Component:**
  
None

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
With the pulses enabled, a drive data set that has a different parameterized direction
of rotation was selected (p1821).  
It is only possible to change the motor direction of rotation using p1821 when the
pulses are inhibited.

**Remedy**
  
- Change over the drive data set with the pulses inhibited.  
- Ensure that the changeover to a drive data set does not result in the motor direction
of rotation being changed (i.e. for these drive data sets, the same value must be
in p1821).  
See also: p1821 (Direction of rotation)

### A07440 EPOS: Jerk time is limited

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The calculation of the jerk time Tr = max(p2572, p2573) / p2574 resulted in an excessively
high value so that the jerk time is internally limited to 1000 ms.  
Note:  
The alarm is also output if jerk limiting is not active.

**Remedy**
  
- Increase the jerk limiting (p2574).  
- Reduce maximum acceleration or maximum deceleration (p2572, p2573).  
See also: p2572 (EPOS maximum acceleration), p2573 (EPOS maximum deceleration), p2574 (EPOS
jerk limiting)

### A07441 LR: Save the position offset of the absolute encoder adjustment

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The status of the absolute encoder adjustment has changed.  
To permanently accept the determined position offset, it must be retentively saved
(p0977).  
Possible causes:  
- Motor or encoder were replaced (applies to EQN and DQI).  
- Position-relevant parameters were changed.  
- A non-adjusted encoder was adjusted (retentively save the project).  
Note:  
This message is not output when switching-on the axis after having first moved it
in the switched-off state, as long as the parameterizable monitoring window was not
exited.

**Remedy**
  
Readjust the encoder.  
See also: p2507 (LR absolute encoder adjustment status)

### F07442 LR: Multiturn does not match the modulo range

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 OFF1

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The ratio between the multiturn resolution and the modulo range (p2576) is not an
integer number.  
This results in the adjustment being set back, as the position actual value cannot
be reproduced after switch-off/switch-on.

**Remedy**
  
Make the ratio between the multiturn resolution and the modulo range an integer number.  
The ratio v is calculated as follows:  
v = (p0421 * p2506 * p2505) / (p2504 * p2576)  
See also: p2504 (LR motor/load motor revolutions), p2505 (LR motor/load load revolutions), p2506,
p2576 (EPOS modulo correction modulo range)

### F07443 LR: Home position not in the permissible range

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 OFF1

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The home position received when adjusting the encoder via numerical signal sink r2599
lies outside the half of the encoder range and cannot be set as actual axis position.  
Fault value (r0949, interpret decimal):  
Maximum permissible value for the home position

**Remedy**
  
Set the home position to a lower value than specified in the fault value.  
See also: c2598 (EPOS home position signal), p2599 (EPOS home position value)

### F07446 Load gearbox: Position tracking cannot be reset

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Application/technological function faulted (17)

**Component:**
  
None

**Response:**
  
 OFF1

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The position tracking cannot be reset.

**Remedy**
  
Reset the position tracking as follows:  
- Select encoder commissioning.  
- Reset position tracking, position (p2720.2 = 1).  
- Deselect encoder commissioning.  
Then acknowledge the fault and, if necessary, re-adjust the absolute encoder (p2507).

### F07450 LR: Standstill monitoring has responded

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Application/technological function faulted (17)

**Component:**
  
None

**Response:**
  
 OFF1

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
After the standstill monitoring time (p2543) expired, the drive left the standstill
window (p2542).  
- Standstill window set too small (p2542).  
- Standstill monitoring time set too low (p2543).  
- Position loop gain too low (p2538).  
- Position loop gain too high (instability/oscillation, p2538).  
- Mechanical overload.  
- Connecting cable, motor/drive converter incorrect (phase missing, interchanged).

**Remedy**
  
Check the causes and resolve.

### F07451 LR: Position monitoring has responded

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Application/technological function faulted (17)

**Component:**
  
None

**Response:**
  
 OFF1

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
When the position monitoring time (p2545) expired, the drive had still not reached
the positioning window (p2544).  
- Positioning window parameterized too small (p2544).  
- Position monitoring time parameterized too short (p2545).  
- Position loop gain too low (p2538).  
- Position loop gain too high (instability/oscillation, p2538).  
- Drive mechanically locked.

**Remedy**
  
Check the causes and resolve.

### F07452 LR: Following error too high

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Application/technological function faulted (17)

**Component:**
  
None

**Response:**
  
 OFF1

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The difference between the position setpoint position actual value (following error
dynamic model, r2563) is higher than the tolerance (p2546).  
- The drive torque or accelerating capacity exceeded.  
- Position measuring system fault.  
- Encoder cable interrupted.  
- Position control sense incorrect.  
- Mechanical system locked.  
- Excessively high traversing velocity or excessively high position reference value
(setpoint) differences.

**Remedy**
  
Check the causes and resolve.

### F07453 LR: Position actual value preprocessing error

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Application/technological function faulted (17)

**Component:**
  
None

**Response:**
  
 OFF1

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
A position measuring system fault has occurred (F31110, F31111).  
An error has occurred during the position actual value preprocessing.

**Remedy**
  
Resolve the cause of the position measuring position fault.  
Check the encoder for the position actual value preprocessing.  
See also: p2502 (LR encoder assignment)

### A07454 LR: Position actual value preprocessing does not have a valid encoder

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
One of the following problems has occurred with the position actual value preprocessing:  
- An encoder is not assigned for the position actual value preprocessing (p2502 =
0).  
- An encoder is assigned, but no encoder data set (p0187 = 99 or p0188 = 99 or p0189
= 99).  
- An encoder and an encoder data set have been assigned, however, the encoder data
set does not contain any encoder data (p0400 = 0) or invalid data (e.g. p0408 = 0).

**Remedy**
  
Check the drive data sets, encoder data sets and encoder assignment.  
See also: p0400 (Encoder type selection), p2502 (LR encoder assignment)

### A07455 EPOS: Maximum velocity limited

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The maximum velocity (p2571) is too high to correctly calculate the modulo correction.  
Within the sampling time for positioning, at the maximum velocity, a maximum of the
half modulo length must be moved through. p2571 was limited to this value.

**Remedy**
  
- Reduce the maximum velocity (p2571).

### A07456 EPOS: Setpoint velocity limited

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Application/technological function faulted (17)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The actual setpoint velocity is greater than the parameterized maximum velocity (p2571)
and is therefore limited.

**Remedy**
  
- Check the specified setpoint velocity.  
- Reduce the velocity override (c2646).  
- Increase the maximum velocity (p2571).

### A07457 EPOS: Combination of input signals illegal

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Application/technological function faulted (17)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
An illegal combination of input signals that are simultaneously set was identified.  
Alarm value (r2124, interpret decimal):  
0: Jog 1 and jog 2 (c2589, c2590).  
1: Jog 1 or jog 2 and direct setpoint input/MDI (c2589, c2590, c2647).  
2: Jog 1 or jog 2 and start homing (c2589, c2590, c2595).  
3: Jog 1 or jog 2 and activate traversing task (c2589, c2590, c2631).  
4: Direct setpoint input/MDI and starting homing (c2647, c2595).  
5: Direct setpoint input/MDI and activate traversing task (c2647, c2631).  
6: Start homing and activate traversing task (c2595, c2631).

**Remedy**
  
Check the appropriate input signals and correct.

### F07458 EPOS: Reference cam not found

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Application/technological function faulted (17)

**Component:**
  
None

**Response:**
  
 OFF1

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
After the active homing starts, the axis moved through the maximum permissible distance
to search for the reference cam without actually finding the reference cam.

**Remedy**
  
- Check signal "Reference cam" (c2612).  
- Check the maximum permissible distance to the reference cam (p2606).  
- If axis does not have any reference cam, then set p2607 to 0.  
See also: p2606 (EPOS active homing reference cam maximum distance), p2607 (EPOS active homing
reference cam available), c2612 (EPOS active homing reference cam)

### F07459 EPOS: No zero mark

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Application/technological function faulted (17)

**Component:**
  
None

**Response:**
  
 OFF1

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
After leaving the reference cam, the axis has traversed the maximum permissible distance
between the reference cam and zero mark without finding the zero mark.

**Remedy**
  
- Check the encoder regarding the zero mark.  
- Check the maximum permissible distance between the reference cam and zero mark (p2609).  
- use an external encoder zero mark (equivalent zero mark) (p0494).  
See also: p2609 (EPOS active homing max distance reference cam and zero mark)

### F07460 EPOS: End of reference cam not found

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Application/technological function faulted (17)

**Component:**
  
None

**Response:**
  
 OFF1

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
In the "active homing" mode, when approaching the zero mark, the axis reached the
end of the traversing range without detecting an edge at binary signal "Reference
cam" (c2612).  
Maximum traversing range: -2147483648 [LU] ... -2147483647 [LU]

**Remedy**
  
- Check signal "reference cam" (c2612).  
- Repeat active homing.  
See also: c2612 (EPOS active homing reference cam)

### A07461 EPOS: Home position not set

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Application/technological function faulted (17)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
When starting a traversing block/direct setpoint input, a home position is not set
(r2684.11 = 0).

**Remedy**
  
Carry out homing (active homing, passive homing, set home position).

### A07462 EPOS: Selected traversing block number does not exist

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
A traversing block selected via binector input c2625 ... c2629 was started via binary
signal c2631 = 0/1 edge "Activate traversing task".  
- The number of the started traversing block is not contained in p2616[0...n].  
- The started traversing block is suppressed.  
Alarm value (r2124, interpret decimal):  
Number of the selected traversing block that is also not available.

**Remedy**
  
- Correct the traversing program.  
- Select an available traversing block number.

### A07463 EPOS: External block change not requested in the traversing block

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Application/technological function faulted (17)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
For a traversing block with the block change enable CONTINUE_EXTERNAL_ALARM, the external
block change was not requested.  
Alarm value (r2124, interpret decimal):  
Number of the traversing block.

**Remedy**
  
Resolve the reason why the signal edge at the measuring probe is missing.

### F07464 EPOS: Traversing block is inconsistent

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 OFF1

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The traversing block does not contain valid information.  
Alarm value (r2124, interpret decimal):  
Number of the traversing block with invalid information.

**Remedy**
  
Check the traversing block and where relevant, take into consideration alarms that
are present.

### A07465 EPOS: Traversing block does not have a subsequent block

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
There is no subsequent block in the traversing block.  
Alarm value (r2124, interpret decimal):  
Number of the traversing block with the missing subsequent block.

**Remedy**
  
- Parameterize this traversing block with the block change enable END.  
- Parameterize additional traversing blocks with a higher block number and for the
last block, using the block change enable END.

### A07466 EPOS: Traversing block number assigned a multiple number of times

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The same traversing block number was assigned a multiple number of times.  
Alarm value (r2124, interpret decimal):  
Number of the traversing block that was assigned a multiple number of times.

**Remedy**
  
Correct the traversing blocks.

### A07467 EPOS: Traversing block has illegal task parameters

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The task parameter in the traversing block contains an illegal value.  
Alarm value (r2124, interpret decimal):  
Number of the traversing block with an illegal task parameter.

**Remedy**
  
Correct the task parameter in the traversing block.

### A07468 EPOS: Traversing block jump destination does not exist

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
In a traversing block, a jump was programmed to a non-existent block.  
Alarm value (r2124, interpret decimal):  
Number of the traversing block with a jump destination that does not exist.

**Remedy**
  
- Correct the traversing block.  
- Add the missing traversing block.

### A07469 EPOS: Traversing block target position < negative software limit switch

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
In the traversing block the specified absolute target position lies outside the range
limited by the negative software limit switch.  
Alarm value (r2124, interpret decimal):  
Number of the traversing block with illegal target position.

**Remedy**
  
- Correct the traversing block.  
- Change the negative software limit switch (c2578, p2580).

### A07470 EPOS: Traversing block target position > positive software limit switch

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
In the traversing block the specified absolute target position lies outside the range
limited by the positive software limit switch.  
Alarm value (r2124, interpret decimal):  
Number of the traversing block with illegal target position.

**Remedy**
  
- Correct the traversing block.  
- Change the positive software limit switch (c2579, p2581).

### A07471 EPOS: Traversing block target position outside the modulo range

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Application/technological function faulted (17)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
In the traversing block the target position lies outside the modulo range.  
Alarm value (r2124, interpret decimal):  
Number of the traversing block with illegal target position.

**Remedy**
  
- In the traversing block, correct the target position.  
- Change the modulo range (p2576).

### A07472 EPOS: Traversing block ABS_POS/ABS_NEG not possible

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Application/technological function faulted (17)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
In the traversing block the positioning mode ABS_POS or ABS_NEG were parameterized
with the modulo correction not activated.  
Alarm value (r2124, interpret decimal):  
Number of the traversing block with the illegal positioning mode.

**Remedy**
  
Correct the traversing block.

### A07473 EPOS: Beginning of traversing range reached

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Application/technological function faulted (17)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
When traversing, the axis has moved to the traversing range limit.

**Remedy**
  
Move away in the positive direction.

### A07474 EPOS: End of traversing range reached

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Application/technological function faulted (17)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
When traversing, the axis has moved to the traversing range limit.

**Remedy**
  
Move away in the negative direction.

### F07475 EPOS: Target position < start of traversing range

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 OFF1

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The target position for relative traversing lies outside the traversing range.

**Remedy**
  
Correct the target position.

### F07476 EPOS: Target position > end of the traversing range

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 OFF1

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The target position for relative traversing lies outside the traversing range.

**Remedy**
  
Correct the target position.

### A07477 EPOS: Target position < negative software limit switch

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
In the actual traversing operation, the target position is less than the negative
software limit switch.

**Remedy**
  
- Correct the target position.  
- Change the negative software limit switch (c2578, p2580).  
See also: c2578 (EPOS negative software limit switch), p2580 (EPOS negative software limit switch),
c2582 (EPOS software limit switch activation)

### A07478 EPOS: Target position > positive software limit switch

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
In the actual traversing operation, the target position is greater than the positive
software limit switch.

**Remedy**
  
- Correct the target position.  
- Change the positive software limit switch (c2579, p2581).  
See also: c2579 (EPOS positive software limit switch), p2581 (EPOS positive software limit switch),
c2582 (EPOS software limit switch activation)

### A07479 EPOS: Negative software limit switch reached

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Application/technological function faulted (17)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The axis is at the position of the negative software limit switch. An active traversing
block was interrupted.

**Remedy**
  
- Correct the target position.  
- Change the negative software limit switch (c2578, p2580).  
See also: c2578 (EPOS negative software limit switch), p2580 (EPOS negative software limit switch),
c2582 (EPOS software limit switch activation)

### A07480 EPOS: Positive software limit switch reached

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Application/technological function faulted (17)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The axis is at the position of the positive software limit switch. An active traversing
block was interrupted.

**Remedy**
  
- Correct the target position.  
- Change the positive software limit switch (c2579, p2581).  
See also: c2579 (EPOS positive software limit switch), p2581 (EPOS positive software limit switch),
c2582 (EPOS software limit switch activation)

### F07481 EPOS: Axis position < negative software limit switch

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Application/technological function faulted (17)

**Component:**
  
None

**Response:**
  
 OFF1

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The actual position of the axis is less than the position of the negative software
limit switch.

**Remedy**
  
- Correct the target position.  
- Change the negative software limit switch (c2578, p2580).  
See also: c2578 (EPOS negative software limit switch), p2580 (EPOS negative software limit switch),
c2582 (EPOS software limit switch activation)

### F07482 EPOS: Axis position > positive software limit switch

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Application/technological function faulted (17)

**Component:**
  
None

**Response:**
  
 OFF1

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The actual position of the axis is greater than the position of the positive software
limit switch.

**Remedy**
  
- Correct the target position.  
- Change the positive software limit switch (c2579, p2581).  
See also: c2579 (EPOS positive software limit switch), p2581 (EPOS positive software limit switch),
c2582 (EPOS software limit switch activation)

## SINAMICS Alarms S200 Basic PN 07483 - 30053

SINAMICS Alarms S200 Basic PN 07483 - 30053

### A07483 EPOS: Travel to fixed stop clamping torque not reached

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Application/technological function faulted (17)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The fixed stop in the traversing block was reached without the clamping torque/clamping
force having been achieved.

**Remedy**
  
- Check the torque limits (p1520, p1521).

### F07484 EPOS: Fixed stop outside the monitoring window

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Application/technological function faulted (17)

**Component:**
  
None

**Response:**
  
 OFF3

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
In the "fixed stop reached" state, the axis has moved outside the defined monitoring
window (p2635).

**Remedy**
  
- Check the monitoring window (p2635).  
- Check the mechanical system.

### F07485 EPOS: Fixed stop not reached

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Application/technological function faulted (17)

**Component:**
  
None

**Response:**
  
 OFF1

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
In a traversing block with the task FIXED STOP, the end position was reached without
detecting a fixed stop.

**Remedy**
  
- Check the traversing block and locate the target position further into the workpiece.  
- If required, reduce the maximum following error window to detect the fixed stop
(p2634).

### A07486 EPOS: Intermediate stop missing

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Application/technological function faulted (17)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
In operating mode "traversing blocks" or "direct setpoint input/MDI", at the start
of motion, c2640 is set to an intermediate stop, i.e. to a 0 signal.

**Remedy**
  
Set c2640 to "No intermediate stop" (1 signal) and restart motion.  
See also: c2640 (EPOS intermediate stop (0 signal))

### A07487 EPOS: Reject traversing task missing

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Application/technological function faulted (17)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
In the modes "Traversing blocks" or "Direct setpoint input/MDI" at the start of motion,
the binary signal sink "Do not reject traversing task/reject traversing task" (c2641)
does not have a 1 signal.

**Remedy**
  
Connect a 1 signal to the binary signal sink "Do not reject traversing task/reject
traversing task" (c2641) and restart motion.  
See also: c2641 (EPOS reject traversing task (0 signal))

### F07488 EPOS: Relative positioning not possible

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Application/technological function faulted (17)

**Component:**
  
None

**Response:**
  
 OFF1

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
In the mode "direct setpoint input/MDI", for continuous transfer (c2649 = 1) relative
positioning was selected (c2648 = 0 signal).

**Remedy**
  
Check the control.

### F07490 EPOS: Enable signal withdrawn while traversing

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Application/technological function faulted (17)

**Component:**
  
None

**Response:**
  
 OFF1

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
- For a standard assignment, another fault may have occurred as a result of withdrawing
the enable signals.  
- The drive is in the "switching on inhibited" state (for a standard assignment).

**Remedy**
  
- Set the enable signals or check the cause of the fault that first occurred and then
result (for a standard assignment).  
- Check the assignment to enable the basic positioning function.

### F07491 EPOS: Negative hardware limit switch reached

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Application/technological function faulted (17)

**Component:**
  
None

**Response:**
  
 OFF3

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
A 0 signal was detected at c2569, i.e. the negative hardware limit switch was reached.  
For a positive traversing direction, the negative hardware limit switch was reached
- i.e. the hardware limit switch wiring is incorrect.  
See also: c2569 (EPOS negative hardware limit switch)

**Remedy**
  
- Leave the negative hardware limit switch in the positive traversing direction and
return the axis to the valid traversing range.  
- Check the wiring of the hardware limit switch.

### F07492 EPOS: Positive hardware limit switch reached

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Application/technological function faulted (17)

**Component:**
  
None

**Response:**
  
 OFF3

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
A 0 signal was detected at c2570, i.e. the positive hardware limit switch was reached.  
For a negative traversing direction, the positive hardware limit switch was reached
- i.e. the hardware limit switch wiring is incorrect.  
See also: c2570 (EPOS positive hardware limit switch)

**Remedy**
  
- Leave the positive hardware limit switch in the negative traversing direction and
return the axis to the valid traversing range.  
- Check the wiring of the hardware limit switch.

### F07493 LR: Overflow of the value range for position actual value

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Application/technological function faulted (17)

**Component:**
  
None

**Response:**
  
 OFF1

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The value range (-2147483648 ... 2147483647) for the position actual value representation
was exceeded.  
When the overflow occurs, the "homed" or "adjustment absolute measuring system" status
is reset.  
Fault value (r0949, interpret decimal):  
1: The position actual value (r2521) has exceeded the value range.  
2: The encoder position actual value Gn_XIST2 has exceeded the value range.  
3: The maximum encoder value times the factor to convert the absolute position Gn_XIST2
from increments to length units (LU) has exceeded the value range for displaying the
position actual value.

**Remedy**
  
If required, reduce the traversing range or position resolution (p2506).  
Note for fault value = 3:  
If the value for the maximum possible absolute position (LU) is greater than 4294967296,
then it is not possible to make an adjustment due to an overflow.  
For rotary encoders, the maximum possible absolute position (LU) is calculated as
follows:  
p2506 * p2505 / p2504  
p2506 * p2505 * p0421 / p2504 for multiturn encoders

### F07494 LR: Drive Data Set changeover in operation

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Application/technological function faulted (17)

**Component:**
  
None

**Response:**
  
 OFF1

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
A Drive Data Set changeover (DDS) with a change of the mechanical relationships (p2503
... 2506), direction of rotation (p1821) or the encoder assignment (p2502) was requested
in operation.  
Note:  
DDS: Drive Data Set

**Remedy**
  
To changeover the drive data set, initially, exit the "operation" mode.

### A07495 LR: Homing function interrupted

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Application/technological function faulted (17)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
An activated homing function (homing mark search or measuring probe evaluation) was
canceled.  
Possible causes:  
- An encoder fault has occurred (Gn_ZSW.15 = 1).  
- Position actual value was set during an activated homing function.  
- Homing mark search and measuring probe evaluation simultaneously activated.  
- Activated homing function (homing mark search or measuring probe evaluation) was
de-activated.

**Remedy**
  
- Check the causes and resolve.  
- Reset the control and activate the required function.

### A07496 EPOS: Enable not possible

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Application/technological function faulted (17)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
It is not possible to enable the basic positioner because at least one condition is
missing.  
Alarm value (r2124, interpret decimal):  
1: EPOS enable missing.  
2: Position actual value, valid feedback signal missing.

**Remedy**
  
Check the corresponding missing condition.

### A07498 LR: Measuring probe evaluation not possible

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Application/technological function faulted (17)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
When evaluating the measuring probe, an error occurred.  
Alarm value (r2124, interpret decimal):  
6:  
The input terminal for the measuring probe is not set.  
4098:  
Error when initializing the measuring probe.  
4100:  
The measuring pulse frequency is too high.  
> 50000:  
The measuring clock cycle is not a multiple integer of the position controller clock
cycle.

**Remedy**
  
Deactivate measuring probe evaluation (c2509 = 0 signal).  
For alarm value = 6:  
Set the input terminal for the measuring probe (p0488, p0489 or p2517, p2518).  
For alarm value = 4098:  
Check the Control Unit hardware.  
For alarm value = 4100:  
Reduce the frequency of the measuring pulses at the measuring probe.  
For alarm value > 50000:  
Set the clock cycle ratio of the measuring clock cycle to the position controller
clock cycle to an integer multiple.  
To do this, the currently effective measuring clock cycle can be determined from the
alarm value as follows:  
Tmeas [125 µs] = alarm value - 50000  
With PROFIBUS, the measuring clock cycle corresponds to the bus clock cycle (r2064[1]).  
Without PROFIBUS, the measuring clock cycle is an internal cycle time that cannot
be influenced.

### F07499 EPOS: Reversing cam approached with the incorrect traversing direction

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Application/technological function faulted (17)

**Component:**
  
None

**Response:**
  
 OFF3

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The negative reversing cam was approached in the positive traversing direction, or
the positive reversing cam was approached in the negative traversing direction.  
See also: c2613 (EPOS active homing negative reversing cam), c2614 (EPOS active homing positive
reversing cam)

**Remedy**
  
- Check the wiring of the reversing cam (c2613, c2614).  
- Check the traversing direction to approach the reversing cam.

### F07503 EPOS: Hardware limit switch approached with the incorrect traversing direction

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Application/technological function faulted (17)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The negative hardware limit switch was approached in the positive traversing direction,
or the positive hardware limit switch was approached in the negative traversing direction.

**Remedy**
  
- Check the wiring of the hardware limit switch (c2569, c2570).  
- Check the traversing direction when approaching the hardware limit switch.

### A07507 EPOS: Home position cannot be set

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Application/technological function faulted (17)

**Component:**
  
Motor

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
After the home position correction, the position setpoint lies outside the traversing
range limits.

**Remedy**
  
- Optimize the position controller.  
- Due to a possible position controller deviation, home position p2599 should not
be directly placed at the traversing range limits.

### A07520 Drive: Motor cannot be changed over

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Application/technological function faulted (17)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
A motor data set switchover was requested via PROFINET that the converter does not
support.

**Remedy**
  
- Check the PROFINET telegram

### A07530 Drive: Drive Data Set DDS not present

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
A data set switchover was requested via PROFINET that the converter does not support.

**Remedy**
  
- Check the PROFINET telegram

### A07531 Drive: Command Data Set CDS not present

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The selected command data set is not available (r0836 > p0170). The command data set
was not changed over.

**Remedy**
  
- Select the existing command data set.  
- Set up additional command data sets.

### A07550 Drive: Not possible to reset encoder parameters

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
When restoring a factory setting, it was not possible to reset the encoder parameters.
The encoder parameters are directly read out of the encoder.  
Alarm value (r2124, interpret decimal):  
Component number of the encoder involved.

**Remedy**
  
- Repeat the operation.  
- Check the encoder connection.

### F07555 Drive encoder: Configuration position tracking

**Valid as of version:**
  
06.02.015

**Message value:**
  
Component number: %1, encoder data set: %2, drive data set: %3, fault cause: %4

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
Encoder 1

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
For position tracking, the configuration is not supported.  
Position tracking can only be activated for absolute encoders.  
For linear axes, it is not possible to simultaneously activate the position tracking
for load and measuring gears.  
Fault value (r0949, interpret hexadecimal):  
ddccbbaa hex  
aa = encoder data set  
bb = component number  
cc = drive data set  
dd = fault cause  
dd = 00 hex = 0 dec  
An absolute encoder is not being used.  
dd = 01 hex = 1 dec  
Position tracking cannot be activated because the memory of the internal NVRAM is
not sufficient or a Control Unit does not have an NVRAM.  
dd = 02 hex = 2 dec  
For a linear axis, the position tracking was activated for the load and measuring
gearbox.  
dd = 03 hex = 3 dec  
Position tracking cannot be activated because position tracking with another gear
ratio, axis type or tolerance window has already been detected for this encoder data
set.  
dd = 04 hex = 4 dec  
A linear encoder is being used.  
See also: p0404 (Encoder configuration effective)

**Remedy**
  
For fault value 0:  
- Use an absolute encoder.  
For fault value 1:  
- Use a Control Unit with sufficient NVRAM.  
For fault value = 2, 4:  
- If necessary, deselect the position tracking (p0411 for the measuring gearbox, p2720
for the load gearbox).  
For fault value 3:  
- Only activate position tracking of the load gearbox in the same encoder data set
if the gear ratio (p2504, p2505), axis type (p2720.1) and tolerance window (p2722)
are also the same. These parameters must be the same in all drive data sets, which
use the same motor encoder.

### F07556 Measuring gearbox: Position tracking, maximum actual value exceeded

**Valid as of version:**
  
06.02.015

**Message value:**
  
Component number: %1, encoder data set: %2

**Message class:**
  
Position/speed actual value incorrect or not available (11)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
When the position tracking of the measuring gearbox is configured, the drive/encoder
identifies a maximum possible absolute position actual value (r0483) that cannot be
represented within 32 bits.  
Maximum value: p0408 * p0412 * 2^p0419  
Fault value (r0949, interpret decimal):  
aaaayyxx hex: yy = component number, xx = encoder data set  
See also: p0408 (Rotary encoder pulse number)

**Remedy**
  
- Reduce the fine resolution (p0419).  
- Reduce the multiturn resolution (p0412).

### A07557 Motor encoder: Home position not in the permissible range

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Application/technological function faulted (17)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The home position received via p2599 when adjusting the encoder lies outside half
of the encoder range and cannot be set as actual axis position.  
The maximum permissible value is displayed in the supplementary information.

**Remedy**
  
Set the home position less than the value from the supplementary information.  
See also: c2598 (EPOS home position signal)

### F07562 Drive, encoder: Position tracking, incremental encoder not possible

**Valid as of version:**
  
06.02.015

**Message value:**
  
Fault cause: %1, component number: %2, encoder data set: %3

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The requested position tracking for incremental encoders is not supported.  
Fault value (r0949, interpret hexadecimal):  
ccccbbaa hex  
aa = encoder data set  
bb = component number  
cccc = fault cause  
cccc = 00 hex = 0 dec  
The encoder type does not support the "Position tracking incremental encoder" function.  
cccc = 01 hex = 1 dec  
Position tracking cannot be activated because the memory of the internal NVRAM is
not sufficient or a Control Unit does not have an NVRAM.  
cccc = 04 hex = 4 dec  
A linear encoder is used that does not support the "position tracking" function.  
See also: p0404 (Encoder configuration effective)

**Remedy**
  
- Check the encoder parameterization (p0400, p0404).  
- Use a Control Unit with sufficient NVRAM.  
- If required, deselect position tracking for the incremental encoder (p0411.3 = 0).

### A07565 Drive: Encoder error in PROFIdrive encoder interface 1

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Position/speed actual value incorrect or not available (11)

**Component:**
  
Sensor Module Encoder 1

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
An encoder error was signaled for encoder 1 via the PROFIdrive encoder interface (G1_ZSW.15).  
Alarm value (r2124, interpret decimal):  
Error code from G1_XIST2.

**Remedy**
  
Acknowledge the encoder error using the encoder control word (G1_STW.15 = 1).

### A07569 Enc identification active

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
During encoder identification (waiting) with p0400 = 10100, the encoder could still
not be identified.  
There is possibly an incorrect encoder or no encoder available, an incorrect encoder
cable inserted or no encoder cable inserted.

**Remedy**
  
- Check the encoder cable and if necessary connect it.  
- Enter the corresponding encoder type in p0400.

### F07575 Drive: Motor encoder not ready

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Position/speed actual value incorrect or not available (11)

**Component:**
  
Sensor Module Encoder 1

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The motor encoder signals that it is not ready.  
- Initialization of encoder 1 (motor encoder) was unsuccessful.  
- The function "parking encoder" is active (encoder control word G1_STW.14 = 1).  
- The Sensor Module is defective.

**Remedy**
  
Evaluate other active faults via the motor encoder.

### A07577 Motor encoder: Measuring probe evaluation not possible

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Application/technological function faulted (17)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
When evaluating the measuring probe, an error occurred.  
Alarm value (r2124, interpret decimal):  
6: The input terminal for the measuring probe is not set.  
4098: Error when initializing the probe.  
4100: The measuring pulse frequency is too high.  
4200: The bus cycle time is not a multiple integer of the position controller clock
cycle.

**Remedy**
  
Deactivate measuring probe evaluation (c2509 = 0 signal).  
For alarm value = 6:  
Set the input terminal for the measuring probe (p0488, p0489 or p2517, p2518).  
For alarm value = 4098:  
Check the Control Unit hardware.  
For alarm value = 4100:  
Reduce the frequency of the measuring pulses at the measuring probe.  
For alarm value = 4200:  
Set the clock cycle ratio between the bus cycle time and the position controller clock
cycle to an integer multiple.

### A07580 Drive: No Sensor Module with matching component number

**Valid as of version:**
  
06.02.015

**Message value:**
  
Encoder data set: %1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
A Sensor Module with the specified component number was not found.  
Alarm value (r2124, interpret decimal):  
Encoder data set involved.

**Remedy**
  
Correct the component number of the Sensor Module.

### A07581 Motor encoder: Position actual value preprocessing error

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Position/speed actual value incorrect or not available (11)

**Component:**
  
Encoder 1

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
An error has occurred during the position actual value preprocessing.

**Remedy**
  
Check the encoder for the position actual value preprocessing.  
See also: p2502 (LR encoder assignment)

### A07587 Motor encoder: Position actual value preprocessing has no valid encoder

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
Encoder 1

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The following problem has occurred during the position actual value preprocessing:  
- An encoder data set has been assigned, however, the encoder data set does not contain
any encoder data (p0400 = 0) or invalid data (e.g. p0408 = 0).

**Remedy**
  
Check the drive data sets, encoder data sets.  
See also: p0400 (Encoder type selection), p2502 (LR encoder assignment)

### A07593 Motor encoder: Value range for position actual value exceeded

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Application/technological function faulted (17)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The value range (-2147483648 ... 2147483647) for the position actual value representation
was exceeded.  
When the overflow occurs, the "homed" or "absolute encoder adjusted" status is reset.  
Alarm value (r2124, interpret decimal):  
1: The position actual value (r2521) has exceeded the value range.  
2: The encoder position actual value Gn_XIST2 has exceeded the value range.  
3: The maximum encoder value multiplied by the factor to convert the absolute position
Gn_XIST2 from increments to length units (LU) has exceeded the value range for displaying
the position actual value.

**Remedy**
  
If required, reduce the traversing range or position resolution.  
For alarm value = 3:  
Reducing the position resolution and conversion factor:  
- Reduce the length unit (LU) per load revolution for rotary encoders (p2506).

### A07596 Motor encoder: Homing function interrupted

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Application/technological function faulted (17)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
An activated homing function (homing mark search or measuring probe evaluation) was
canceled.  
- An encoder fault has occurred (Gn_ZSW.15 = 1).  
- Position actual value was set during an activated homing function.  
- Homing mark search and measuring probe evaluation simultaneously activated.  
- Activated homing function (homing mark search or measuring probe evaluation) was
de-activated.

**Remedy**
  
- Check the causes and resolve.  
- Reset the control and activate the required function.

### F07801 Drive: Motor overcurrent

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Motor overload (8)

**Component:**
  
Motor

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The permissible motor limit current was exceeded.  
- Active current limit too low.  
- Current controller not correctly set.  
- Load is too high.  
- Short-circuit in the motor cable or ground fault.  
- Motor current does not match the drive current.

**Remedy**
  
- Reduce the load.  
- Check the motor and motor cables for short-circuit and ground fault.  
- Check the drive and motor combination.

### F07802 Drive: Infeed not ready

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Infeed faulted (13)

**Component:**
  
None

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The drive does not signal a ready state after an internal switch-on command.  
- DC link voltage is not present.  
- Defective drive.  
- Supply voltage incorrectly set.

**Remedy**
  
- Check the enable signals for the drive.  
- Replace the drive.  
- Check the supply voltage setting (p0210).

### F07808 HF Damping Module: damping not ready

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Power electronics faulted (5)

**Component:**
  
None

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
When switching on or in the switched-on state, the HF Damping Module does not return
a ready signal.  
Fault value (r0949, interpret hexadecimal):  
1: Fault at switch-on identified.  
2: Fault during operation identified.

**Remedy**
  
- Check the DRIVE-CLiQ wiring to the HF Damping Module.  
- Check the 24 V supply voltage.  
- If required, replace the HF Damping Module.  
Note:  
HF Damping Module

### F07810 Drive: Power unit EEPROM without rated data

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Power Unit

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
No rated data are stored in the power unit EEPROM.

**Remedy**
  
Replace the power unit or inform Siemens Customer Service.

### F07815 Drive: Power unit has been changed

**Valid as of version:**
  
06.02.015

**Message value:**
  
Parameter: %1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
Power Unit

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The code number of the actual power unit does not match the saved number. This occurs
if a saved configuration (SD card, backup file) of a converter with another power
rating is used.  
Fault value only for internal Siemens diagnostics.  
See also: p0201 (Power unit code number)

**Remedy**
  
- Reset to the factory settings, which corresponds to recommissioning the converter.  
- Use an SD card or backup file with the configuration correct for the drive being
used and switch-off/switch-on the drive.  
- In case of doubt, before using an SD card, delete the existing configuration of
the USER folder.  
- For a series commissioning, only use the same converter types (order number, power
class).

### F07860 External fault 1

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
External measured value / signal state outside the permissible range (16)

**Component:**
  
None

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The condition for "External fault 1" is active.  
Note:  
"External fault 1" is initiated by a 1/0 edge via c2106.  
See also: c2106 (External fault 1)

**Remedy**
  
- Eliminate the causes of this fault.  
- Acknowledge fault.

### F07900 Drive: Motor blocked/speed controller at its limit

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Application/technological function faulted (17)

**Component:**
  
Motor

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The motor operates longer than 0.2 seconds at the torque limit and below the speed
threshold in p2175.  
This signal can also be initiated if the speed actual value is oscillating and the
speed controller output repeatedly goes to its limit.  
See also: p2175, p2177

**Remedy**
  
- Check that the motor can freely move.  
- Check the effective torque limit (r1538, r1539).  
- Check the parameter of the "Motor blocked" signal and possibly correct (p2175).

### F07901 Drive: Motor overspeed

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Application/technological function faulted (17)

**Component:**
  
Motor

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The maximum permissible speed was either positively or negatively exceeded (p1082).

**Remedy**
  
- Check the speed controller (p1460, p1462).  
- Check the moment of inertia (p1498).  
- Check the maximum speed (p1082).

### A07920 Drive: Torque/speed too low

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Application/technological function faulted (17)

**Component:**
  
Motor

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The torque deviates from the torque/speed envelope characteristic (too low).

**Remedy**
  
- Check the connection between the motor and load.  
- Adapt the parameterization corresponding to the load.

### A07921 Drive: Torque/speed too high

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Application/technological function faulted (17)

**Component:**
  
Motor

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The torque deviates from the torque/speed envelope characteristic (too high).

**Remedy**
  
- Check the connection between the motor and load.  
- Adapt the parameterization corresponding to the load.

### A07922 Drive: Torque/speed out of tolerance

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Application/technological function faulted (17)

**Component:**
  
Motor

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The torque deviates from the torque/speed envelope characteristic.

**Remedy**
  
- Check the connection between the motor and load.  
- Adapt the parameterization corresponding to the load.

### F07923 Drive: Torque/speed too low

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Application/technological function faulted (17)

**Component:**
  
Motor

**Response:**
  
 OFF1

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The torque deviates from the torque/speed envelope characteristic (too low).

**Remedy**
  
- Check the connection between the motor and load.  
- Adapt the parameterization corresponding to the load.

### F07924 Drive: Torque/speed too high

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Application/technological function faulted (17)

**Component:**
  
Motor

**Response:**
  
 OFF1

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The torque deviates from the torque/speed envelope characteristic (too high).

**Remedy**
  
- Check the connection between the motor and load.  
- Adapt the parameterization corresponding to the load.

### F07925 Drive: Torque/speed out of tolerance

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Application/technological function faulted (17)

**Component:**
  
Motor

**Response:**
  
 OFF1

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The torque deviates from the torque/speed envelope characteristic.

**Remedy**
  
- Check the connection between the motor and load.  
- Adapt the parameterization corresponding to the load.

### F07955 Drive: Motor has been changed

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
Motor

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The code number of the actual self-identifying motor does not match the saved number.  
If available:  
The code numbers of the bearings, gearbox and brake do not match the saved numbers.

**Remedy**
  
Connect the original motor and switch on the converter again (POWER ON) - or restore
the factory settings.  
Note:  
The data for bearings, gearbox and brake are reloaded.

### F07956 Drive: Motor code does not match the list (catalog) motor

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
Motor

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The motor code of the connected self-identifying motor does not match the possible
list motor types (see selection in p0300).  
It is possible that this firmware version does not support the connected motor.  
Fault value (r0949, interpret decimal):  
Motor code of the connected motor.  
Note:  
The first three digits of the motor code generally correspond to the list motor type.

**Remedy**
  
Use a self-identifying motor with the matching motor code.

### F08000 TB: +/-15 V power supply faulted

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Supply voltage fault (undervoltage) (3)

**Component:**
  
Controller Extension (CX)

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
Terminal Board 30 detects an incorrect internal power supply voltage.  
Fault value (r0949, interpret decimal):  
0: Error when testing the monitoring circuit.  
1: Fault in normal operation.

**Remedy**
  
- Replace Terminal Board 30.  
- Replace Control Unit.

### F08010 TB: Analog-digital converter

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Controller Extension (CX)

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The analog/digital converter on Terminal Board 30 has not supplied any converted data.

**Remedy**
  
- Check the power supply.  
- Replace Terminal Board 30.

### A08560 IE: Syntax error in configuration file

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
A syntax error has been detected in the configuration file for the Industrial Ethernet
interface (X127). The saved configuration file has not been loaded.  
Note:  
IE: Industrial Ethernet

**Remedy**
  
Reinitialize the station using the "Edit Ethernet node" screen form (e.g. with Startdrive
commissioning tool).

### A08561 IE: Consistency error affecting adjustable parameters

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
A consistency error was detected when activating the configuration for the Industrial
Ethernet interface (X127).  
Alarm value (r2124, interpret decimal):  
0: General consistency error  
1: Error in the IP configuration (IP address, subnet mask or standard gateway).  
2: Error in the station names.  
5: Standard gateway is also set at the PROFINET interface.  
6: The station name is also set at the PROFINET interface.  
7: The IP address is located in the same subnet as the IP address of the PROFINET
interface.  
Note:  
For alarm value = 0, 1, 2, 5, 7 the following applies: the configuration was not changed.  
For alarm value = 6 the following applies: The new configuration was however activated.  
IE: Industrial Ethernet

**Remedy**
  
Reinitialize the station using the "Edit Ethernet node" screen form (e.g. with Startdrive
commissioning tool).

### A08562 PROFINET: Syntax error in configuration file

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
A syntax error has been detected in the configuration file for the PROFINET interface
(X150). The saved configuration file has not been loaded.

**Remedy**
  
Reinitialize the station using the "Edit Ethernet node" screen form (e.g. with Startdrive
commissioning tool).

### A08563 PROFINET: Consistency error affecting adjustable parameters

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
A consistency error was detected when activating the configuration for the PROFINET
interface (X150).  
Alarm value (r2124, interpret decimal):  
0: General consistency error  
1: Error in the IP configuration (IP address, subnet mask or standard gateway).  
2: Error in the station names.  
3: DHCP was not able to be activated, as a cyclic PROFINET connection already exists.  
5: Standard gateway is also set at the Industrial Ethernet interface (X127).  
6: Standard station name is also set at the Industrial Ethernet interface (X127).  
7: IP address is located in the same subnet as the IP address of the Industrial Ethernet
interface (X127).  
Note:  
For alarm value = 0, 1, 2, 3, 4, 5, 7, the following applies: the configuration was
not changed.  
For alarm value = 6 the following applies: The new configuration was however activated.  
DHCP: Dynamic Host Configuration Protocol

**Remedy**
  
Reinitialize the station using the "Edit Ethernet node" screen form (e.g. with Startdrive
commissioning tool).

### A08566 IIOT: Syntax error in configuration file

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
A syntax error has been detected in the configuration file for the IIoT interface
(X128). The saved configuration file has not been loaded.  
Note:  
IIoT: Industrial Internet of Things

**Remedy**
  
Reinitialize the station using the "Edit Ethernet node" screen form (e.g. with Startdrive
commissioning tool).

### A08567 IIoT: Consistency error for adjustable parameters

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
A consistency error was detected when activating the configuration for the IIoT interface
(X128).  
Alarm value (r2124, interpret decimal):  
0: General consistency error  
1: Error in the IP configuration (IP address, subnet mask or standard gateway).  
2: Error in the station names.  
5: Standard gateway is also set at the PROFINET interface.  
6: The station name is also set at the PROFINET interface.  
7: The IP address is located in the same subnet as the IP address of the PROFINET
interface.  
Note:  
For alarm value = 0, 1, 2, 5, 7 the following applies: the configuration was not changed.  
For alarm value = 6 the following applies: The new configuration was however activated.  
IE: Industrial Ethernet

**Remedy**
  
Reinitialize the station using the "Edit Ethernet node" screen form (e.g. with Startdrive
commissioning tool).

### A08800 PROFIenergy energy-saving mode active

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Communication error to the higher-level control system (9)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The PROFIenergy energy-saving mode is active  
Alarm value (r2124, interpret decimal):  
Mode ID of the active PROFIenergy energy-saving mode.

**Remedy**
  
The alarm is automatically withdrawn when the energy-saving mode is exited.  
Note:  
The energy-saving mode is exited after the following events:  
- The PROFIenergy command end_pause is received from the higher-level control.  
- The higher-level control has changed into the STOP operating state.  
- The PROFINET connection to the higher-level control has been disconnected.

### F13000 License not adequate

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
Control Unit (CU)

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
- The converter uses options that require a license and the licenses are not sufficient.  
- An error has occurred when checking the licensing.  
Fault value (r0949, interpret decimal):  
0: Adequate licensing was not able to be determined as there is no licensing data
available on the memory card.  
1: Adequate licensing was not able to be determined as the memory card with the required
licensing data was withdrawn in operation or the memory card is defective.  
2: Adequate licensing was not able to be determined as there is no licensing data
available on the memory card.  
3: Adequate licensing was not able to be determined as the licensing data does not
match the serial number of the memory card being used.  
4, 5, 6, 7: Adequate licensing was not able to be determined as the licensing data
were manipulated and are therefore invalid.  
8, 9: An internal error occurred when checking the license.

**Remedy**
  
For fault value = 0:  
Transfer a license file with the required licenses to the converter.  
For fault value = 1:  
Reinsert the memory card into the converter. If you have to replace a defective memory
card, contact Technical Support.  
For fault value = 2:  
Transfer a license file with the required licenses to the converter.  
For fault value = 3:  
Compare the license file name (after "LK_" to ".ZIP") with the serial number of the
memory card.  
Transfer the appropriate license file to the converter.  
For fault value = 4, 5, 6, 7, 8, 9:  
- Carry out a POWER ON.  
- Upgrade firmware to later version.  
- Contact Technical Support.  
Note:  
An overview of the converter functions requiring a license can be displayed using
a commissioning tool in the online mode. Depending on the commissioning tool, you
can also obtain the necessary licensing (serial number, license file, Trial License
Mode).

### A13002 Licensing not sufficient in operation

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
Control Unit (CU)

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
- For the converter, the options that require a license are being used but the licenses
are not sufficient.  
- An error occurred when checking the existing licenses.  
Alarm value (r2124, interpret decimal):  
0: The existing license is not sufficient.  
1: An adequate license was not able to be determined as the memory card with the required
licensing data was withdrawn in operation or the memory card has developed a defect.  
2: An adequate license was not able to be determined as there is no licensing data
available on the memory card.  
3: An adequate license was not able to be determined as there is no licensing data
available on the memory card.  
4, 5, 6, 7: An adequate license was not able to be determined as the licensing data
were manipulated and are therefore invalid.  
8,9: An internal error occurred when checking the license.

**Remedy**
  
For alarm value = 0:  
Additional licenses are required and must be activated.  
For alarm value = 1:  
Reinsert or replace the memory card that matches the system.  
For alarm value = 2:  
Transfer the license file to the converter.  
For alarm value = 3:  
Compare the license file name (after "LK_" to ".ZIP") with the serial number of the
memory card.  
Transfer the appropriate license file to the converter.  
For alarm value = 4, 5, 6, 7, 8, 9:  
- Carry out a POWER ON.  
- Upgrade firmware to later version.  
- Contact Technical Support.  
Note:  
An overview of the converter functions requiring a license can be displayed using
a commissioning tool in the online mode. Depending on the commissioning tool, you
can also obtain the necessary licensing (serial number, license file, Trial License
Mode).

### A13030 Trial License activated

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
Control Unit (CU)

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The "Trial License" function was activated. One of the available periods is expiring.

**Remedy**
  
Not necessary.  
The alarm is automatically withdrawn after the periods have expired.

### A13031 Trial License period expired

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
Control Unit (CU)

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
One of the available periods of the "Trial License" function has expired.

**Remedy**
  
- If required, start an additional period.  
- Deactivate functions requiring a license.  
- Appropriately license the drive unit.  
Note:  
A license that is not adequate will only become evident after the next time the system
runs up.

### A13032 Trial License last period activated

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
Control Unit (CU)

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The "Trial License" function was activated. The last of the available periods is expiring.

**Remedy**
  
Not necessary.  
The alarm is automatically withdrawn after the last period has expired.

### A13033 Trial License last period expired

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
Control Unit (CU)

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The last period of the "Trial License" function has expired. No additional periods
available.

**Remedy**
  
- Deactivate functions requiring a license.  
- Appropriately license the drive unit.  
Note:  
A license that is not adequate will only become evident after the next time the system
runs up.

### F30001 Drive: overcurrent

**Valid as of version:**
  
06.02.015

**Message value:**
  
Fault cause: %1 bin

**Message class:**
  
Power electronics faulted (5)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The drive has detected an overcurrent condition.  
- Closed-loop control is incorrectly parameterized.  
- Motor has a short-circuit or fault to ground (frame).  
- The rated motor current is significantly higher than that of the drive.  
- Infeed: High discharge and post-charging currents for line voltage dip.  
- Infeed: High post-charging currents for overload when motoring and DC link voltage
dip.  
- Infeed: Short-circuit currents at switch-on as there is no line reactor.  
- Power cables are not correctly connected.  
- The power cables exceed the maximum permissible length.  
- Defective drive.  
- Line phase interrupted.  
Fault value (r0949, interpret bit-serial):  
Bit 0: Phase U.  
Bit 1: Phase V.  
Bit 2: Phase W.

**Remedy**
  
- Check the motor data - If required, carry out commissioning.  
- Check the assignment of the rated currents of the motor and converter.  
- Infeed: Check the line quality.  
- Infeed: Reduce the motor load.  
- Infeed: Check that the line filter and line reactor are correctly connected.  
- Check the power cable connections.  
- Check the power cables for short-circuit or ground fault.  
- Check the length of the power cables.  
- Replace drive.  
- Check the line phases.

### F30002 Drive: DC link overvoltage

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
DC link overvoltage (4)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The drive has detected an overvoltage condition in the DC link.  
- Motor regenerates too much energy.  
- Device supply voltage too high.  
- Line phase interrupted.  
Fault value only for internal Siemens diagnostics.

**Remedy**
  
- Increase the ramp-down time.  
- Use a braking resistor.  
- Use a drive with a higher power rating.  
- Check the device supply voltage (p0210).  
- Check the line phases.  
See also: p0210 (Device supply voltage)

### F30003 Power unit: DC link voltage undervoltage

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Infeed faulted (13)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The power unit has detected an undervoltage condition in the DC link.  
- Line supply failure.  
- Line voltage below the permissible value.  
- Line infeed failed or interrupted.  
- Line phase interrupted.  
Note:  
The monitoring threshold for undervoltage in the DC link is indicated in r0296.

**Remedy**
  
- Check the line voltage.  
- Check the line infeed and observe the fault messages relating to it (if there are
any).  
- Check the line phases.  
- Check the supply voltage setting (p0210).  
See also: p0210 (Device supply voltage)

### F30004 Power unit: Overtemperature heat sink inverter

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Power electronics faulted (5)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The temperature of the power unit heat sink has exceeded the permissible limit value.  
- Insufficient cooling, fan failure.  
- Overload.  
- Ambient temperature too high.  
- Pulse frequency too high.  
Fault value (r0949, interpret decimal):  
Temperature [0.01 °C].

**Remedy**
  
- Check whether the fan is running.  
- Check the fan elements.  
- Check whether the ambient temperature is in the permissible range.  
- Check the motor load.  
- Reduce the pulse frequency if this is higher than the rated pulse frequency.  
Notice:  
This fault can only be acknowledged after the alarm threshold for alarm A30250 has
been fallen below.

### F30005 Power unit: Overload I2t (AC)

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Power electronics faulted (5)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The fault threshold for the I2t overload on the AC side of the power unit has been
exceeded. The permissible load duty cycle or the continuous load was not maintained.  
Fault value (r0949, interpret decimal):  
I2t (AC) [100 % = 16384]  
See also: r0036 (Power unit overload)

**Remedy**
  
- Reduce the continuous load.  
- Adapt the load duty cycle.  
- Check the rated currents of the motor and power unit.  
See also: p0307 (Rated motor power)

### F30011 Power unit: Line phase failure in main circuit

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Network fault (2)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
At the power unit, the DC link voltage ripple has exceeded the permissible limit value.  
Possible causes:  
- A line phase has failed.  
- The 3 line phases are inadmissibly asymmetrical.  
- The capacitance of the DC link capacitor forms a resonance frequency with the line
inductance and the reactor integrated in the power unit.  
- The fuse of a phase of a main circuit has ruptured.  
- A motor phase has failed.  
- For power units operated on a single phase, the permissible active power was exceeded.  
Only for internal Siemens troubleshooting.

**Remedy**
  
- Check the main circuit fuses.  
- Check whether a single-phase load is distorting the line voltages.  
- Detune the resonant frequency with the line inductance by using an upstream line
reactor.  
- Dampen the resonant frequency with the line inductance by switching over the DC
link voltage compensation in the software or increase the smoothing. However, this
can have a negative impact on the torque ripple at the motor output.  
- Check the motor feeder cables.

### F30012 Power unit: Temperature sensor wire breakage

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Power electronics faulted (5)

**Component:**
  
Power Unit

**Response:**
  
 OFF1

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The connection to a temperature sensor in the power unit is interrupted.  
Fault value (r0949, interpret binary):  
Bit 1: Air intake  
Bit 2: Inverter 1  
Bit 3: Inverter 2  
Bit 4: Inverter 3  
Bit 5: Inverter 4  
Bit 6: Inverter 5  
Bit 7: Inverter 6  
Bit 8: Rectifier  
Bit 10: Moisture ext. moisture sensor  
Bit 11: Temperature ext. moisture sensor  
Bit 13: Balance resistor  
Bit 14: Capacitor air discharge  
Bit 15: Liquid intake

**Remedy**
  
Contact Technical Support.

### F30013 Power unit: Temperature sensor short-circuit

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Power electronics faulted (5)

**Component:**
  
Power Unit

**Response:**
  
 OFF1

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
A temperature sensor in the power unit is short-circuited.  
Fault value (r0949, interpret binary):  
Bit 1: Air intake  
Bit 2: Inverter 1  
Bit 3: Inverter 2  
Bit 4: Inverter 3  
Bit 5: Inverter 4  
Bit 6: Inverter 5  
Bit 7: Inverter 6  
Bit 8: Rectifier  
Bit 10: Moisture ext. moisture sensor  
Bit 11: Temperature ext. moisture sensor  
Bit 14: Capacitor air discharge  
Bit 15: Liquid intake

**Remedy**
  
Contact Technical Support.

### F30015 Power unit: Phase failure motor cable

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Application/technological function faulted (17)

**Component:**
  
Motor

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
A phase failure in the motor feeder cable was detected.  
The signal can also be output in the following case:  
- The motor is correctly connected, however the closed-speed control is instable and
therefore an oscillating torque is generated.  
Note:  
Chassis power units do not feature phase failure monitoring.

**Remedy**
  
- Check the motor feeder cables.  
- Check the speed controller settings.

### A30016 Power unit: Load supply switched off

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Network fault (2)

**Component:**
  
Power Unit

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The DC link voltage is too low.  
Alarm value (r2124, interpret decimal):  
DC link voltage at the time of the trip [V].

**Remedy**
  
- Switch on load supply.  
- Check the line supply if necessary.

### F30017 Power unit: Hardware current limit has responded too often

**Valid as of version:**
  
06.02.015

**Message value:**
  
Fault cause: %1 bin

**Message class:**
  
Power electronics faulted (5)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The hardware current limitation in the relevant phase (see A30031, A30032, A30033)
has responded too often. The number of times the limit has been exceeded depends on
the design and type of power unit.  
- Closed-loop control is incorrectly parameterized.  
- Fault in the motor or in the power cables.  
- The power cables exceed the maximum permissible length.  
- Motor load too high  
- Power unit defective.  
Fault value (r0949, interpret binary):  
Bit 0: Phase U  
Bit 1: Phase V  
Bit 2: Phase W  
Additional bits:  
Only for internal Siemens troubleshooting.  
Note:  
Fault value = 0 means that the phase with current limiting is not recognized (e.g.
for blocksize device).

**Remedy**
  
- Check the motor data.  
- Check the motor circuit configuration (star-delta).  
- Check the motor load.  
- Check the power cable connections.  
- Check the power cables for short-circuit or ground fault.  
- Check the length of the power cables.  
- Replace power unit.

### F30020 Power unit: Configuration not supported

**Valid as of version:**
  
06.02.015

**Message value:**
  
Fault cause: %1, additional information: %2

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
A configuration is requested that is not supported by the power unit.  
Fault value (r0949, interpret hexadecimal):  
yyyyxxxx hex: xxxx = fault cause, yyyy = additional information (internal Siemens)  
xxxx = 1: The requested DRIVE-CLiQ timing is not permissible.  
xxxx = 3: Initialization was not able to be successfully completed. It is possible
that the converter was switched-off before or while running up.  
xxxx = 4: The combination of power unit and converters is not supported.  
xxxx = 8: The version of the ASIC installed in the power unit is no longer supported.

**Remedy**
  
For fault cause = 1:  
Update the converter firmware or change the DRIVE-CLiQ topology.  
For fault cause = 3, 4:  
Use a converter with the appropriate power unit and carry out a POWER ON for the converter.  
For fault cause = 8:  
Replace the power unit by one which has a newer ASIC version.

### F30021 Drive: Ground fault

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Ground fault / inter-phase short-circuit detected (7)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The drive has detected a ground fault.  
Possible causes:  
- Ground fault in the power cables.  
- Ground fault at the motor.  
- When the brake closes, this causes the hardware DC current monitoring to respond.  
- Short-circuit at the braking resistor.  
Fault value (r0949, interpret decimal):  
0:  
- The hardware DC current monitoring has responded.  
- Short-circuit at the braking resistor.  
> 0:  
Absolute value summation current amplitude.

**Remedy**
  
- Check the power cable connections.  
- Check the motor.  
- Check the cables and contacts of the brake connection (a wire is possibly broken).  
- Check the braking resistor.

### F30022 Power unit: Monitoring U_ce

**Valid as of version:**
  
06.02.015

**Message value:**
  
Fault cause: %1 bin

**Message class:**
  
Ground fault / inter-phase short-circuit detected (7)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
POWER ON

**Cause**
  
In the power unit, the monitoring of the collector-emitter voltage (U_ce) of the semiconductor
has responded.  
Possible causes:  
- Fiber-optic cable interrupted.  
- The power supply for power semiconductor gating missing.  
- Short-circuit at the power unit output.  
- Defective semiconductor in the power unit.  
Fault value (r0949, interpret binary):  
Bit 0: Short-circuit in phase U  
Bit 1: Short-circuit in phase V  
Bit 2: Short-circuit in phase W  
Bit 3: Short-circuit in phase N  
See also: r0949 (Fault value)

**Remedy**
  
- Check the fiber-optic cable and if required, replace.  
- Check the power supply for the power semiconductor gating (24 V).  
- Check the power cable connections.  
- Select the defective semiconductor and replace.

### F30024 Power unit: Overtemperature thermal model

**Valid as of version:**
  
06.02.015

**Message value:**
  
Power semiconductor: %1, temperature: [0.01 degrees C] %2

**Message class:**
  
Power electronics faulted (5)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The temperature difference between the power semiconductor involved and the heat sink
has exceeded the permissible fault threshold.  
- The permissible load duty cycle was not maintained.  
- Insufficient cooling, fan failure.  
- Overload.  
- Ambient temperature too high.  
- Pulse frequency too high.  
  
Fault value (r0949, interpret hexadecimal):  
yyyyxxxx hex: yyyy= Power semiconductor, xxxx = Temperature in 0.01°C  
See also: r0037 (Power unit temperatures)

**Remedy**
  
- Adapt the load duty cycle.  
- Check whether the fan is running.  
- Check the fan elements.  
- Check whether the ambient temperature is in the permissible range.  
- Check the motor load.  
- Reduce the pulse frequency if this is higher than the rated pulse frequency.

### F30025 Power unit: Chip overtemperature

**Valid as of version:**
  
06.02.015

**Message value:**
  
Power semiconductor: %1, temperature: [0.01 degrees C] %2

**Message class:**
  
Power electronics faulted (5)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The chip temperature of the power semiconductor involved has exceeded the permissible
fault threshold.  
- The permissible load duty cycle was not maintained.  
- Insufficient cooling, fan failure.  
- Overload.  
- Ambient temperature too high.  
- Pulse frequency too high.  
  
Fault value (r0949, interpret hexadecimal):  
yyyyxxxx hex: yyyy= Power semiconductor, xxxx = Temperature in 0.01°C

**Remedy**
  
- Adapt the load duty cycle.  
- Check whether the fan is running.  
- Check the fan elements.  
- Check whether the ambient temperature is in the permissible range.  
- Check the motor load.  
- Reduce the pulse frequency if this is higher than the rated pulse frequency.  
Note:  
This fault can only be acknowledged after the alarm threshold for alarm A030252 has
been fallen below.  
See also: r0037 (Power unit temperatures)

### F30027 Power unit: Precharging DC link time monitoring

**Valid as of version:**
  
06.02.015

**Message value:**
  
Enable signals: %1, Status: %2

**Message class:**
  
Infeed faulted (13)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The power unit DC link was not able to be precharged within the expected time.  
1) There is no line voltage connected.  
2) The line contactor/line side switch has not been closed.  
3) The line voltage is too low.  
4) Line voltage incorrectly set (p0210).  
5) The precharging resistors are overheated as there were too many precharging operations
per time unit.  
6) The precharging resistors are overheated as the DC link capacitance is too high.  
7) The precharging resistors are overheated because when there is no "ready for operation"
(r0863.0) of the infeed unit, power is taken from the DC link.  
8) The precharging resistors are overheated as the line contactor was closed during
the DC link fast discharge through the Braking Module.  
9) The DC link has either a ground fault or a short-circuit.  
10) The precharging circuit is possibly defective (only for chassis units).  
11) Infeed defective and/or fuse ruptured  
  
Fault value (r0949, interpret binary):  
yyyyxxxx hex:  
  
yyyy = power unit state  
0: Fault status (wait for OFF and fault acknowledgment).  
1: Restart inhibit (wait for OFF).  
2: Overvoltage condition detected -> change into the fault state.  
3: Undervoltage condition detected -> change into the fault state.  
4: Wait for bridging contactor to open -> change into the fault state.  
5: Wait for bridging contactor to open -> change into restart inhibit.  
6: Wait for bypass contactor to open  
7: Commissioning.  
8: Ready for precharging.  
9: Precharging started, DC link voltage lower than the minimum switch-on voltage.  
10: Precharging, DC link voltage end of precharging still not detected.  
11: Wait for the end of the de-bounce time of the main contactor after precharging
has been completed.  
12: Precharging completed, ready for pulse enable.  
13: It was detected that the STO terminal was energized at the power unit.  
  
xxxx = Missing internal enable signals, power unit (inverted bit-coded, FFFF hex ->
all internal enable signals available)  
Bit 0: Power supply for the power semiconductor gating shut down.  
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
See also: p0210 (Device supply voltage)

**Remedy**
  
In general:  
- Check the line voltage at the input terminals.  
- Check the line voltage setting (p0210).  
For booksize drive units, the following applies:  
- Wait (approx. 8 minutes) until the precharging resistors have cooled down. For this
purpose, preferably disconnect the infeed unit from the line supply.  
For 5):  
- Carefully observe the permissible precharging frequency (refer to the product documentation).  
For 6):  
- Check the total capacitance of the DC link and reduce in accordance with the maximum
permissible DC link capacitance if necessary (refer to the product documentation).  
For 7):  
- Interconnect the ready-for-operation signal from the infeed unit (r0863.0) in the
enable logic of the drives connected to this DC link.  
For 8):  
- Check the connections of the external line contactor. The line contactor must be
open during DC link fast discharge.  
For 9):  
- Check the DC link for ground faults or short-circuits.  
For 11):  
- Check the DC link voltage of the infeed (r0070) and Motor Modules (r0070).  
If the DC link voltage generated by the infeed (or external) is not displayed for
the Motor Modules (r0070), then a fuse has ruptured in the Motor Module.  
See also: p0210 (Device supply voltage)

### A30030 Power unit: Internal overtemperature alarm

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Power electronics faulted (5)

**Component:**
  
Power Unit

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The temperature inside the drive converter has exceeded the permissible temperature
limit.  
- Insufficient cooling, fan failure.  
- Overload.  
- Ambient temperature too high.  
Alarm value (r2124, interpret decimal):  
Only for internal Siemens troubleshooting.

**Remedy**
  
- Possibly use an additional fan.  
- Check whether the ambient temperature is in the permissible range.  
Notice:  
This alarm is automatically withdrawn once the permissible temperature limit value
has been fallen below minus 5 K.

### A30031 Power unit: Hardware current limiting in phase U

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Power electronics faulted (5)

**Component:**
  
Power Unit

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
Hardware current limit for phase U responded. The pulsing in this phase is inhibited
for one pulse period.  
- Closed-loop control is incorrectly parameterized.  
- Fault in the motor or in the power cables.  
- The power cables exceed the maximum permissible length.  
- Motor load too high  
- Power unit defective.

**Remedy**
  
- Check the motor data.  
- Check the motor circuit configuration (star/delta).  
- Check the motor load.  
- Check the power cable connections.  
- Check the power cables for short-circuit or ground fault.  
- Check the length of the power cables.

### A30032 Power unit: Hardware current limiting in phase V

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Power electronics faulted (5)

**Component:**
  
Power Unit

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
Hardware current limit for phase V responded. The pulsing in this phase is inhibited
for one pulse period.  
- Closed-loop control is incorrectly parameterized.  
- Fault in the motor or in the power cables.  
- The power cables exceed the maximum permissible length.  
- Motor load too high  
- Power unit defective.

**Remedy**
  
- Check the motor data.  
- Check the motor circuit configuration (star/delta).  
- Check the motor load.  
- Check the power cable connections.  
- Check the power cables for short-circuit or ground fault.  
- Check the length of the power cables.

### A30033 Power unit: Hardware current limiting in phase W

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Power electronics faulted (5)

**Component:**
  
Power Unit

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
Hardware current limit for phase W responded. The pulsing in this phase is inhibited
for one pulse period.  
- Closed-loop control is incorrectly parameterized.  
- Fault in the motor or in the power cables.  
- The power cables exceed the maximum permissible length.  
- Motor load too high  
- Power unit defective.

**Remedy**
  
- Check the motor data.  
- Check the motor circuit configuration (star/delta).  
- Check the motor load.  
- Check the power cable connections.  
- Check the power cables for short-circuit or ground fault.  
- Check the length of the power cables.

### A30034 Power unit: Internal overtemperature

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Power electronics faulted (5)

**Component:**
  
Power Unit

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The alarm threshold for internal overtemperature has been reached.  
If the temperature inside the power unit increases up to the fault threshold, then
fault F30036 is triggered.  
- Ambient temperature might be too high.  
- Insufficient cooling, fan failure.  
Alarm value (r2124, interpret binary):  
Bit 0 = 1: Overtemperature in the control electronics area.  
Bit 1 = 1: Overtemperature in the power electronics area.  
Bit 2 = 1: Overtemperature in the processor area.  
Bit 3 = 1: Overtemperature in the processor area.  
Bit 4 = 1: Overtemperature when the internal fan is defective.  
Bit 5 = 1: Intake air overtemperature.

**Remedy**
  
- Check the ambient temperature.  
- Check the fan for the inside of the unit.

### F30036 Power unit: Internal overtemperature

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Power electronics faulted (5)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
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

**Remedy**
  
- Check the internal fan.  
- Check the fan elements.  
- Check whether the ambient temperature is in the permissible range.  
Notice:  
This fault can only be acknowledged once the permissible temperature limit minus 5
K has been fallen below.

### F30037 Power unit: Rectifier overtemperature

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Power electronics faulted (5)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The temperature in the rectifier of the power unit has exceeded the permissible temperature
limit.  
- Insufficient cooling, fan failure.  
- Overload.  
- Ambient temperature too high.  
- Line phase failure.  
Fault value (r0949, interpret decimal):  
Temperature [0.01 °C].

**Remedy**
  
- Check whether the fan is running.  
- Check the fan elements.  
- Check whether the ambient temperature is in the permissible range.  
- Check the motor load.  
- Check the line phases.  
Notice:  
This fault can only be acknowledged after the alarm threshold for alarm A05004 has
been undershot.

### F30040 Power unit: 24/48 V undervoltage

**Valid as of version:**
  
06.02.015

**Message value:**
  
Channel: %1, voltage: %2 [0.1 V]

**Message class:**
  
Supply voltage fault (undervoltage) (3)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The undervoltage threshold of the 24 V power supply for the power unit was fallen
below for longer than 3 ms.  
Note:  
- For booksize power units, the undervoltage threshold is 15 V.  
- For CU310-2, CUA31 and CUA32 the undervoltage threshold is 16 V.  
- for all other power units (e.g. S120M), the undervoltage threshold depends on the
power unit, and is not displayed.  
Fault value (r0949, interpret hexadecimal):  
yyxxxx hex: yy = channel, xxxx = voltage [0.1 V]  
yy = 0: 24 V power supply  
yy = 1: 48 V power supply

**Remedy**
  
- Check the power supply of the power unit.  
- Carry out a POWER ON (switch-off/switch-on) for the component.

### A30041 Power unit: Undervolt 24/48 V alarm

**Valid as of version:**
  
06.02.015

**Message value:**
  
Channel: %1, voltage: %2 [0.1 V]

**Message class:**
  
Supply voltage fault (undervoltage) (3)

**Component:**
  
Power Unit

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
For the power unit power supply, the lower threshold has been violated.  
Alarm value (r2124, interpret hexadecimal):  
yyxxxx hex: yy = channel, xxxx = voltage [0.1 V]  
yy = 0: 24 V power supply  
yy = 1: 48 V power supply

**Remedy**
  
- Check the power supply of the power unit.  
- Carry out a POWER ON (switch-off/switch-on) for the component.

### A30042 Power unit: Fan has reached the maximum operating hours

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Power electronics faulted (5)

**Component:**
  
Power Unit

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The maximum operating time of at least one fan will soon be reached, or has already
been exceeded.  
Alarm value (r2124, interpret binary):  
Bit 0 = 1:  
The wear counter of the heat sink fan has reached 99 %. The remaining service life
is 1 %. After this 1 % has elapsed, bit 0 is cleared and bit 2 is set in the alarm
value.  
Bit 2 = 1:  
The wear counter of the heat sink fan has exceeded 100 %.  
Bit 8 = 1:  
The wear counter of the 1st internal fan has reached 99 %. The remaining service life
is 1 %. After this 1 % has elapsed, bit 8 is cleared and bit 10 is set in the alarm
value.  
Bit 10 = 1:  
The wear counter of the 1st internal fan has exceeded 100 %.  
Bit 16 = 1:  
The wear counter of the 2nd internal fan has reached 99 %. The remaining service life
is 1 %. After this 1 % has elapsed, bit 16 is cleared and bit 18 is set in the alarm
value.  
Bit 18 = 1:  
The wear counter of the 2nd internal fan has exceeded 100 %.

**Remedy**
  
For the fan involved, carry out the following:  
1. Replace the fan.  
2. Reset the wear counter using the appropriate button in Startdrive or the web server.  
See also: r0277 (Power unit heat sink fan wear counter)

### F30043 Power unit: Overvolt 24/48 V

**Valid as of version:**
  
06.02.015

**Message value:**
  
Channel: %1, voltage: %2 [0.1 V]

**Message class:**
  
Supply voltage fault (overvoltage) (3)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
POWER ON

**Cause**
  
For the power unit power supply, the upper threshold has been violated.  
Fault value (r0949, interpret hexadecimal):  
yyxxxx hex: yy = channel, xxxx = voltage [0.1 V]  
yy = 0: 24 V power supply  
yy = 1: 48 V power supply

**Remedy**
  
Check the power supply of the power unit.

### A30044 Power unit: Overvolt 24/48 V alarm

**Valid as of version:**
  
06.02.015

**Message value:**
  
Channel: %1, voltage: %2 [0.1 V]

**Message class:**
  
Supply voltage fault (overvoltage) (3)

**Component:**
  
Power Unit

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
For the power unit power supply, the upper threshold has been violated.  
Alarm value (r2124, interpret hexadecimal):  
yyxxxx hex: yy = channel, xxxx = voltage [0.1 V]  
yy = 0: 24 V power supply  
yy = 1: 48 V power supply

**Remedy**
  
Check the power supply of the power unit.

### F30045 Power unit: Supply undervoltage

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Supply voltage fault (undervoltage) (3)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
Power supply fault in the power unit.  
- The voltage monitor signals an undervoltage fault on the module.  
The following applies for CU31x:  
- The voltage monitoring on the DAC board signals an undervoltage fault on the module.  
For S120M, the following applies:  
- This message is displayed for undervoltage or overvoltage.

**Remedy**
  
- Check the power supply of the power unit.  
- Carry out a POWER ON (switch-off/switch-on) for the component.  
- Replace the module if necessary.

### A30046 Power unit: Undervoltage alarm

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Power electronics faulted (5)

**Component:**
  
Power Unit

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
Before the last restart, a problem occurred at the power unit power supply.  
The voltage monitor in the internal FPGA of the PSA signals an undervoltage fault
on the module.  
Alarm value (r2124, interpret decimal):  
Register value of the voltage fault register.

**Remedy**
  
- Check the 24 V DC voltage supply to power unit.  
- Carry out a POWER ON (switch-off/switch-on) for the component.  
- Replace the module if necessary.

### A30048 Power unit: fan defective

**Valid as of version:**
  
06.02.015

**Message value:**
  
Fault cause: %1 bin

**Message class:**
  
External measured value / signal state outside the permissible range (16)

**Component:**
  
Power Unit

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The feedback signal of a fan signals a fault, or there is a communication error with
one or several fans.  
- Fan defective.  
- Fan blocked.  
- Feedback signal error.  
Alarm value (r2124, interpret binary):  
Bit 0 = 1: heat sink fan  
Bit 1 = 1: fan 1 inside the device  
Bit 2 = 1: fan 2 inside the device  
Bit 4 = 1: Internal communication error to one or several fans  
Bits 16 to 31 are only for internal Siemens diagnostics.

**Remedy**
  
- Check the fan involved.  
- If required, replace the fan.  
- For communication errors, update the software or replace the power unit.  
Note:  
If the alarm has been withdrawn, this does not necessarily mean that the cause of
the fault has been resolved. It is also possible that the software switched off the
fan, and therefore can no longer evaluate the feedback signal.

### F30050 Power unit: 24 V supply overvoltage

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Supply voltage fault (overvoltage) (3)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
POWER ON

**Cause**
  
The voltage monitor signals an overvoltage fault on the module.

**Remedy**
  
- Check the 24 V power supply.  
- Replace the module if necessary.

### F30051 Power unit: Motor holding brake short-circuit detected

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
External measured value / signal state outside the permissible range (16)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
A short-circuit at the motor holding brake terminals has been detected.  
Fault value (r0949, interpret decimal):  
Only for internal Siemens troubleshooting.

**Remedy**
  
- Check the motor holding brake for a short-circuit.  
- Check the connection and cable for the motor holding brake.

### F30052 EEPROM data error

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
POWER ON

**Cause**
  
The EEPROM data of the power unit module are incorrect.  
Fault value (r0949, interpret hexadecimal):  
Only for internal Siemens troubleshooting.

**Remedy**
  
Replace the power unit module or update the EEPROM data.

### F30053 FPGA data faulty

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Power Unit

**Response:**
  
 NONE

**Acknowledgment:**
  
POWER ON

**Cause**
  
The FPGA data of the power unit are faulty. This can be caused, for example, if a
firmware update is interrupted.

**Remedy**
  
Replace the power unit or update of the FPGA data by updating the firmware.  
Note:  
If this fault occurs after a firmware update, then update the firmware again.

## SINAMICS Alarms S200 Basic PN 30055 - 35950

SINAMICS Alarms S200 Basic PN 30055 - 35950

### F30055 Power unit: Braking chopper overcurrent

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Braking Module faulted (14)

**Component:**
  
None

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
An overcurrent condition has occurred in the braking chopper.

**Remedy**
  
- Check whether the braking resistor has a short-circuit.  
- For an external braking resistor, check whether the resistor may have been dimensioned
too small.  
Note:  
The braking chopper is only enabled again at pulse enable after the fault has been
acknowledged.

### A30057 Power unit: Line asymmetry

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Network fault (2)

**Component:**
  
Power Unit

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
Frequencies have been detected on the DC link voltage that would suggest line asymmetry
or failure of a line phase.  
It is also possible that a motor phase has failed.  
If these frequencies occur with the same or even higher amplitudes, then after a device-specific
time elapses, fault F30011 is output  
Alarm value, only for internal Siemens troubleshooting.

**Remedy**
  
- Check the line phase connection.  
- Check the motor feeder cable connections.  
If there is no phase failure of the line or motor, then line asymmetry is involved.  
- Reduce the power in order to avoid fault F30011.

### F30058 Power unit: heat sink fan defective

**Valid as of version:**
  
06.02.015

**Message value:**
  
Fault cause: %1 bin

**Message class:**
  
External measured value / signal state outside the permissible range (16)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The feedback signal of the heat sink fan signals a fault, or there is a communication
error with the fan.  
- Fan defective.  
- Fan blocked.  
- Feedback signal error.  
Fault value (r0949, interpret binary):  
Value in bits 0 to 15:  
0: Feedback signal of the fan signals a fault  
1: Internal communication error to the fan  
Bits 16 to 31 are only for internal Siemens diagnostics.

**Remedy**
  
- Check the heat sink fan and replace if necessary.  
- For communication errors, update the software or replace the power unit.  
Note:  
- If the fault can be acknowledged, this does not necessarily mean that the cause
of the fault has been resolved. It is also possible that the software switched off
the fan, and therefore can no longer evaluate the feedback signal.

### F30059 Power unit: Internal fan 1 defective

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Auxiliary unit faulted (20)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The feedback signal of internal fan 1 signals a fault, or there is a communication
error with the fan.  
Fault value (r0949, interpret decimal):  
0: Feedback signal of the fan signals a fault  
1: Internal communication error to the fan

**Remedy**
  
- Check internal fan 1 and replace if necessary.  
- For communication errors, update the software or replace the power unit.  
Note:  
If the fault can be acknowledged, this does not necessarily mean that the cause of
the fault has been resolved. It is also possible that the software switched off the
fan, and therefore can no longer evaluate the feedback signal.

### F30062 Bypass contactor opened under current

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Infeed faulted (13)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The bypass contactor of the precharging unit has been opened under current.  
Possible causes:  
- A defect at the bypass contactor

**Remedy**
  
It is urgently recommended that the components involved are replaced to prevent serious
damage to the entire converter line-up.

### F30068 Power unit: undertemperature inverter heat sink

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Power electronics faulted (5)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The actual inverter heat sink temperature is below the permissible minimum value.  
Possible causes:  
- The power unit is being operated at an ambient temperature that lies below the permissible
range.  
- The temperature sensor evaluation is defective.  
Fault value (r0949, interpret decimal):  
Inverter heat sink temperature [0.1 °C].

**Remedy**
  
- Ensure that higher ambient temperatures prevail.  
- Replace the power unit.

### A30076 Power unit: Thermal overload braking resistor alarm

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Braking Module faulted (14)

**Component:**
  
Power Unit

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The energy absorbed by the braking resistor has exceeded the alarm threshold of 80
%. If the power unit is still operated in the generator mode, then this can reach
the shutdown threshold. To avoid overheating of the braking resistor, use of the braking
resistor is inhibited and alarm A30077 is output.  
Alarm value (r2124, interpret decimal):  
Energy absorbed by the braking resistor [Ws].

**Remedy**
  
Reduce the power when generating.  
Note:  
For a DC link coupling, the generating power of all of the coupled power units must
be taken into consideration.

### A30077 Power unit: Thermal overload braking resistor

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Braking Module faulted (14)

**Component:**
  
Power Unit

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The braking resistor is thermally overloaded. This is the reason that its use was
inhibited.  
Alarm value (r2124, interpret decimal):  
Energy absorbed by the braking resistor [Ws].

**Remedy**
  
Reduce the power when generating.  
Note:  
- Once the braking resistor has thermally recovered, it is enabled for further use.  
- For a DC link coupling, the generating power of all the coupled power units must
be taken into consideration.

### F30078 Power unit: Line reactor overheated

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Overtemperature of the electronic components (6)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The temperature monitoring of the line reactor has responded. In addition to the OFF2
response, the use of the braking resistor was inhibited.  
Note:  
- An overtemperature condition of the line reactor can occur when a DC link coupling
is used – and if the power when motoring, which is fed into the DC link - Is not evenly
distributed across the rectifiers of the power units.

**Remedy**
  
- Check the converter fan and replace if necessary.  
- Reduce the motoring power.

### F30081 Power unit: Switching operations too frequent

**Valid as of version:**
  
06.02.015

**Message value:**
  
Fault cause: %1 bin

**Message class:**
  
Power electronics faulted (5)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The power unit has executed too many switching operations for current limitation.  
- Closed-loop control is incorrectly parameterized.  
- Motor has a short-circuit or fault to ground (frame).  
- U/f operation: Up ramp set too low.  
- U/f operation: Rated motor current is significantly higher than that of the power
section.  
- Infeed: High discharge and post-charging currents for line voltage dip.  
- Infeed: High post-charging currents for overload when motoring and DC link voltage
dip.  
- Infeed: Short-circuit currents at switch-on as there is no line reactor.  
- Power cables are not correctly connected.  
- Power cables exceed the maximum permissible length.  
- Power unit defective.  
Additional causes for a parallel switching device (r0108.15 = 1):  
- A power unit has tripped (switched off) due to a ground fault.  
- The closed-loop circulating current control is either too slow or has been set too
fast.  
Fault value (r0949, interpret bit-serial):  
Bit 0: Phase U.  
Bit 1: Phase V.  
Bit 2: Phase W.

**Remedy**
  
- Check the motor data - If required, carry out commissioning.  
- Check the motor circuit configuration (star-delta)  
- U/f operation: Increase up ramp.  
- U/f operation: Check the rated currents of the motor and power unit.  
- Infeed: Check the line quality.  
- Infeed: Reduce the motor load.  
- Infeed: Correct connection of the line reactor.  
- Check the power cable connections.  
- Check the power cables for short-circuit or ground fault.  
- Check the length of the power cables.  
- Replace power unit.  
For a parallel switching device (r0108.15 = 1) the following additionally applies:  
- Check the ground fault monitoring thresholds (p0287).  
- Check the setting of the closed-loop circulating current control (p7036, p7037).

### A30082 Power unit: cooling medium flow rate too low alarm threshold

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Power electronics faulted (5)

**Component:**
  
Power Unit

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The flow rate is too low, and has fallen below the specified alarm threshold. If the
flow rate is still too low after the specified time has expired, then fault F30083
is output.

**Remedy**
  
- Check the coolant flow rate.  
- Check the thermal conductivity of the coolant.  
- Check the coolant concentration.

### F30083 Power unit: cooling medium flow rate too low fault threshold

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Power electronics faulted (5)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The flow rate is too low, and has fallen below the specified fault threshold.

**Remedy**
  
- Check the coolant flow rate.  
- Check the thermal conductivity of the coolant.  
- Check the coolant concentration.

### A30086 Power unit: coolant temperature has exceeded the alarm threshold

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Power electronics faulted (5)

**Component:**
  
Power Unit

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The coolant temperature has exceeded the specified alarm threshold.  
If the coolant temperature increases up to the specified fault threshold, then fault
F30087 is output.  
Alarm value (r2124, interpret decimal):  
Coolant temperature.

**Remedy**
  
Check the cooling system and the ambient conditions.

### F30087 Power unit: coolant temperature has exceeded the fault threshold

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Power electronics faulted (5)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The coolant temperature has exceeded the specified fault threshold.  
Fault value (r0949, interpret decimal):  
Coolant temperature.

**Remedy**
  
Check the cooling system and the ambient conditions.

### F30105 PU: Actual value sensing fault

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Power electronics faulted (5)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
At least one incorrect actual value channel was detected on the Power Stack Adapter
(PSA).  
The incorrect actual value channels are displayed in the following diagnostic parameters.

**Remedy**
  
Evaluate the diagnostic parameters.  
If the actual value channel is incorrect, check the components and if required, replace.

### A30250 Power unit: Overtemperature heat sink inverter

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Power electronics faulted (5)

**Component:**
  
Power Unit

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The alarm threshold for overtemperature at the inverter heat sink has been reached.  
Fault F30004 is initiated if the temperature of the heat sink increases by 5 K.

**Remedy**
  
Check the following:  
- Is the ambient temperature within the defined limit values?  
- Have the load conditions and the load duty cycle been appropriately dimensioned?  
- Has the cooling failed?

### A30251 Power unit: Rectifier overtemperature

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Power electronics faulted (5)

**Component:**
  
Power Unit

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The alarm threshold for the overtemperature of the rectifier has been reached. The
response is set using p0290.  
If the temperature of the rectifier increases by an additional 5 K, then fault F30037
is triggered.

**Remedy**
  
Check the following:  
- Is the ambient temperature within the defined limit values?  
- Have the load conditions and the load duty cycle been appropriately dimensioned?  
- Has the fan failed? Check the direction of rotation.  
- Has a phase of the line supply failed?  
- Is an arm of the supply (incoming) rectifier defective?

### A30252 Power unit: Chip overtemperature alarm

**Valid as of version:**
  
06.02.015

**Message value:**
  
Power semiconductor: %1, temperature: [0.01 degrees C] %2

**Message class:**
  
Power electronics faulted (5)

**Component:**
  
Power Unit

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The chip temperature of the power semiconductor involved has exceeded the permissible
alarm threshold.  
Note:  
- If the chip temperature of the power semiconductor involved increases by 5K, then
fault F30025 is initiated.  
  
Alarm value (r2124, interpret hexadecimal):  
yyyyxxxx hex: yyyy= Power semiconductor, xxxx = Temperature in 0.01°C

**Remedy**
  
Check the following:  
- Is the ambient temperature within the defined limit values?  
- Have the load conditions and the load duty cycle been appropriately dimensioned?  
- Has the cooling failed?  
- Pulse frequency too high?

### A30253 Power unit: Overtemperature thermal model alarm

**Valid as of version:**
  
06.02.015

**Message value:**
  
Power semiconductor: %1, temperature: [0.01 degrees C] %2

**Message class:**
  
Power electronics faulted (5)

**Component:**
  
Power Unit

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The temperature difference between the power semiconductor involved and the heat sink
has exceeded the permissible alarm threshold.  
The maximum output current is reduced as overload response.  
  
Alarm value (r2124, interpret hexadecimal):  
yyyyxxxx hex: yyyy= Power semiconductor, xxxx = Temperature in 0.01°C

**Remedy**
  
Not necessary.  
The alarm is automatically withdrawn once the alarm threshold has been fallen below.  
Note:  
If the temperature continues to increase, this can result in fault F30024.

### A30256 Power unit: Overload I2t (AC)

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Power electronics faulted (5)

**Component:**
  
Power Unit

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The alarm threshold for the I2t overload on the AC side of the power unit has been
exceeded. Depending on the selected overload response, the output current and therefore
the output frequency can be reduced. If the current reduction is not sufficient to
thermally relieve the power unit, then when the fault threshold for overload is reached
the drive switches off the power unit and outputs fault F30005.  
See also: r0036 (Power unit overload)

**Remedy**
  
- Reduce the continuous load.  
- Adapt the load duty cycle.  
- Check the rated currents of the motor and power unit.  
See also: p0290 (Power unit overload response)

### A30257 Power unit: Overload I2t (DC)

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Power electronics faulted (5)

**Component:**
  
Power Unit

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The alarm threshold for the I2t overload on the DC side of the power unit has been
exceeded.  
Depending on the selected overload response, the output current and therefore the
output frequency can be reduced. If the current reduction is not sufficient to thermally
relieve the power unit, then when the fault threshold for overload is reached the
drive switches off the power unit and outputs fault F30258.  
See also: r0036 (Power unit overload)

**Remedy**
  
- Reduce the continuous load.  
- Adapt the load duty cycle.  
See also: p0290 (Power unit overload response)

### F30258 Power unit: Overload I2t (DC)

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Power electronics faulted (5)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The fault threshold for the I2t overload on the DC side of the power unit has been
exceeded.  
The permissible load duty cycle or the continuous load was not maintained.  
Fault value (r0949, interpret decimal):  
I2t (DC) [100 % = 16384]  
See also: r0036 (Power unit overload)

**Remedy**
  
- Reduce the continuous load.  
- Adapt the load duty cycle.  
See also: p0307 (Rated motor power)

### A30259 Braking resistor value too low

**Valid as of version:**
  
06.03.014

**Message value:**
  
%1

**Message class:**
  
Braking Module faulted (14)

**Component:**
  
Power Unit

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The braking resistor value used in p0216 is too low.  
This can result in an excessively high braking current.  
  
Alarm value (r2124, interpret decimal):  
Minimum limit value of the braking resistor [0.1 Ohm]  
See also: p0216 (Braking resistance value)

**Remedy**
  
- Use a braking resistor with the appropriate resistance value  
- Observe the product documentation

### F30260 Power unit: Fault in the driver supply for the power semiconductor

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
A fault has occurred in the driver supply of the power semiconductor.

**Remedy**
  
There is a hardware defect. The device must be replaced.

### F30262 Power unit: Braking chopper defective

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Power electronics faulted (5)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The braking chopper is defective.

**Remedy**
  
Replace the converter.

### F30263 Power unit: Braking chopper upper defective

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Power electronics faulted (5)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The upper braking chopper is defective.

**Remedy**
  
Replace the converter.

### F30264 Power unit: Braking chopper inhibited due to implausible DC link voltage

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Braking Module faulted (14)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The braking chopper was inhibited because the unloaded DC link voltage continuously
reaches or exceeds the chopper activation threshold. This prevents the braking chopper
from being permanently active and possibly damaged.  
  
Possible causes:  
The value of parameter p0210 does not match the line voltage.  
  
Fault value (r0949, interpret decimal): DC link voltage [V]

**Remedy**
  
Replace the converter.

### F30265 Power unit: Line voltage failure detected

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Power electronics faulted (5)

**Component:**
  
Power Unit

**Response:**
  
 OFF3

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
Line voltage failure was detected

**Remedy**
  
- Switch on the line voltage.  
- To increase the degree of ruggedness, the delay time in p3234 can be increased.  
- If necessary, line voltage failure detection can be deactivated using p2149.16.  
See also: p2149, p3234

### A30266 Power unit: Required modulator setting cannot be implemented

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Power Unit

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The required modulator setting was not able to be implemented. This can involve some
undesirable effects; for example, unexpectedly high switching losses can occur or
the current controller bandwidth can be reduced.  
  
Alarm value (r2124, interpret hexadecimal):  
Only for internal Siemens troubleshooting.

**Remedy**
  
- Carry out a POWER ON (switch-off/switch-on).

### A30267 Power unit: Active power overload

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Power electronics faulted (5)

**Component:**
  
Power Unit

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The alarm threshold for the active power overload of the power unit has been exceeded.
Depending on the selected overload response, the output current and therefore the
output frequency can be reduced. If the current reduction is not sufficient to thermally
relieve the power unit, then when the fault threshold for overload is reached the
drive switches off the power unit and outputs fault F30268.  
See also: r0036 (Power unit overload)

**Remedy**
  
- Reduce the continuous load.  
- Adapt the load duty cycle.  
See also: p0290 (Power unit overload response)

### F30268 Power unit: Active power overload

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Power electronics faulted (5)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The fault threshold for the active power overload of the power unit has been exceeded.  
The permissible load duty cycle or the continuous load was not maintained.  
Fault value (r0949, interpret decimal):  
Active power [100 % = 16384]  
See also: r0036 (Power unit overload)

**Remedy**
  
- Reduce the continuous load.  
- Adapt the load duty cycle.  
See also: p0307 (Rated motor power)

### F30314 Power unit: 24 V power supply overloaded by PM

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Supply voltage fault (undervoltage) (3)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The 24 V power supply through the Power Module (PM) is overloaded.  
An external 24 V power supply via X124 on the Control Unit is not connected.

**Remedy**
  
Connect an external 24 V power supply via X124 at the Control Unit.

### A30315 Power unit: 24 V power supply overloaded by PM

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Supply voltage fault (undervoltage) (3)

**Component:**
  
Power Unit

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The 24 V power supply through the Power Module (PM) is overloaded.  
An external 24 V power supply via X124 on the Control Unit is not connected.

**Remedy**
  
Connect an external 24 V power supply via X124 at the Control Unit.

### A30502 Power unit: DC link overvoltage

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
DC link overvoltage (4)

**Component:**
  
Power Unit

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The power unit has detected overvoltage in the DC link on a pulse inhibit.  
- Device supply voltage too high.  
- Line reactor incorrectly dimensioned.  
Alarm value (r2124, interpret decimal):  
DC link voltage [1 bit = 100 mV].  
See also: r0070 (Actual DC link voltage)

**Remedy**
  
- Check the device supply voltage (p0210).  
- Check the dimensioning of the line reactor.  
See also: p0210 (Device supply voltage)

### N30800 Power unit: Group signal

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Power electronics faulted (5)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
NONE

**Cause**
  
The power unit has detected at least one fault.

**Remedy**
  
Evaluate the other messages that are presently available.

### F30801 Power unit: Sign-of-life missing

**Valid as of version:**
  
06.02.015

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

**Component:**
  
Control Unit (CU)

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
Internal communications error.  
The computing time load might be too high.  
Message value (r0949/r2124):  
0000yyxx hex: yy = component number, xx = error cause  
xx = 0A hex (10 dec):  
The sign-of-life bit in the receive telegram is not set.

**Remedy**
  
- Deselect functions that are not required.

### F30802 Power unit: Time slice overflow

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
A time slice overflow has occurred.  
Fault value (r0949, interpret decimal):  
xx: time slice number

**Remedy**
  
- Carry out a POWER ON (switch-off/switch-on) for all components.  
- Upgrade firmware to later version.  
- Contact Technical Support.

### F30804 Power unit: Checksum error occurred

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
A checksum error (CRC error) has occurred for the power unit.

**Remedy**
  
- Carry out a POWER ON (switch-off/switch-on) for all components.  
- Upgrade firmware to later version.  
- Contact Technical Support.

### F30805 Power unit: EEPROM checksum error

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
Internal parameter data is corrupted.  
Fault value (r0949, interpret hexadecimal):  
01: EEPROM access error.  
02: Too many blocks in the EEPROM.

**Remedy**
  
Replace the module.

### F30809 Power unit: Switching information not valid

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
For 3P gating unit, the following applies:  
The last switching status word in the setpoint telegram is identified by the end ID.
Such an end ID was not found.

**Remedy**
  
- Carry out a POWER ON (switch-off/switch-on) for all components.  
- Upgrade firmware to later version.  
- Contact Technical Support.

### F30810 Power unit: Watchdog timer expired

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The watchdog timer has expired. This can only be caused by a fatal software error.

**Remedy**
  
- Carry out a POWER ON (switch-off/switch-on) for all components.  
- Upgrade firmware to later version.  
- Contact Technical Support.

### F30815 Power unit: Processor clock signal error

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
POWER ON

**Cause**
  
The processor clock signal monitoring has signaled an error. This can involve the
signal itself or its PLL.

**Remedy**
  
- Replace the hardware.  
- Contact Technical Support.

### F30820 Power unit: Telegram error

**Valid as of version:**
  
06.02.015

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
Internal communications error.  
Error cause:  
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

**Remedy**
  
- Carry out a POWER ON (switch-off/switch-on).  
- Check the electrical cabinet design and cable routing for EMC compliance.

### F30835 Power unit: Cyclic data transfer error

**Valid as of version:**
  
06.02.015

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
Internal communications error. The nodes do not send and receive in synchronism.  
Error cause:  
33 (= 21 hex):  
The cyclic telegram has not been received.  
34 (= 22 hex):  
Timeout in the telegram receive list.  
64 (= 40 hex):  
Timeout in the telegram send list.  
Note regarding the message value:  
The individual information is coded as follows in the message value (r0949/r2124):  
0000yyxx hex: yy = component number, xx = error cause

**Remedy**
  
- Carry out a POWER ON.  
- Replace the component involved.

### F30836 Power unit: Send error

**Valid as of version:**
  
06.02.015

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
Internal communications error. Data were not able to be sent.  
Error cause:  
65 (= 41 hex):  
Telegram type does not match send list.  
Note regarding the message value:  
The individual information is coded as follows in the message value (r0949/r2124):  
0000yyxx hex: yy = component number, xx = error cause

**Remedy**
  
Carry out a POWER ON.

### F30845 Power unit: Cyclic data transfer error

**Valid as of version:**
  
06.02.015

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
Internal communications error.  
Error cause:  
11 (= 0B hex):  
Synchronization error during alternating cyclic data transfer.  
Note regarding the message value:  
The individual information is coded as follows in the message value (r0949/r2124):  
0000yyxx hex: yy = component number, xx = error cause

**Remedy**
  
Carry out a POWER ON (switch-off/switch-on).

### F30850 Power unit: Internal software error

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Power Unit

**Response:**
  
 OFF1

**Acknowledgment:**
  
POWER ON

**Cause**
  
An internal software error has occurred in the power unit.  
Fault value (r0949, interpret decimal):  
Only for internal Siemens troubleshooting.

**Remedy**
  
- Replace power unit.  
- If required, upgrade the firmware in the power unit.  
- Contact Technical Support.

### F30851 Power unit (CU): Sign-of-life missing

**Valid as of version:**
  
06.02.015

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
Internal communications error.  
The component did not set the sign-of-life.  
Message value (r0949/r2124):  
0000yyxx hex: yy = component number, xx = error cause  
xx = 0A hex (10 dec):  
The sign-of-life bit in the receive telegram is not set.

**Remedy**
  
- Deselect functions that are not required.  
- Replace the component involved.

### A30853 Power unit: Sign-of-life error cyclic data

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
General drive fault (19)

**Component:**
  
Control Unit (CU)

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The cyclic setpoint telegrams of the power unit were not refreshed on time.

**Remedy**
  
- Check the power unit and if required replace.

### F30860 Power unit (CU): Telegram error

**Valid as of version:**
  
06.02.015

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
Internal communications error.  
Error cause:  
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
The internal communications from the component involved signals a failure of the supply
voltage.  
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

**Remedy**
  
- Carry out a POWER ON (switch-off/switch-on).  
- Check the electrical cabinet design and cable routing for EMC compliance.

### F30875 Power unit: power supply voltage failed

**Valid as of version:**
  
06.02.015

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Supply voltage fault (undervoltage) (3)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The component involved has signaled that the 24 V supply has failed.  
Error cause:  
9 (= 09 hex):  
The power supply voltage for the components has failed.  
Note regarding the message value:  
The individual information is coded as follows in the message value (r0949/r2124):  
0000yyxx hex: yy = component number, xx = error cause

**Remedy**
  
- Check the supply voltage wiring (interrupted cable, contacts, ...).  
- Check the dimensioning of the 24 V supply, check cable lengths.

### F30885 Power unit CU (CU): Cyclic data transfer error

**Valid as of version:**
  
06.02.015

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
Internal communications error.  
The nodes do not send and receive in synchronism.  
Error cause:  
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

**Remedy**
  
- Check the power supply voltage of the component involved.  
- Carry out a POWER ON.  
- Replace the component involved.

### F30886 Power unit (CU): Error when sending

**Valid as of version:**
  
06.02.015

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
Internal communications error.  
Data were not able to be sent.  
Error cause:  
65 (= 41 hex):  
Telegram type does not match send list.  
Note regarding the message value:  
The individual information is coded as follows in the message value (r0949/r2124):  
0000yyxx hex: yy = component number, xx = error cause

**Remedy**
  
Carry out a POWER ON.

### F30895 Power unit (CU): Alternating cyclic data transfer error

**Valid as of version:**
  
06.02.015

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
Communications error.  
Error cause:  
11 (= 0B hex):  
Synchronization error during alternating cyclic data transfer.  
Note regarding the message value:  
The individual information is coded as follows in the message value (r0949/r2124):  
0000yyxx hex: yy = component number, xx = error cause

**Remedy**
  
Carry out a POWER ON (switch-off/switch-on).

### F30896 Power unit (CU): Inconsistent component properties

**Valid as of version:**
  
06.02.015

**Message value:**
  
Component number: %1

| Symbol | Meaning |
| --- | --- |
| For %1 | Component in target topology |

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The properties of the component (power unit), specified by the fault value, have changed
in an incompatible fashion with respect to the properties when running up.  
Fault value (r0949, interpret decimal):  
Component number.

**Remedy**
  
- Carry out a POWER ON.

### F30899 Power unit: Unknown fault

**Valid as of version:**
  
06.02.015

**Message value:**
  
New message: %1

**Message class:**
  
Power electronics faulted (5)

**Component:**
  
Power Unit

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
A fault occurred on the power unit, which cannot be interpreted by the converter firmware.  
This can occur if the firmware on this component is more recent than the converter
firmware.  
Fault value (r0949, interpret decimal):  
Fault number.  
Note:  
If required, the significance of this new fault can be read about in a more recent
description of the converter.

**Remedy**
  
- Replace the firmware on the power unit by an older firmware version.  
- Upgrade the converter firmware.

### F30903 Power unit: I2C bus error occurred

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Power Unit

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
Communications error with an EEPROM or an analog/digital converter.  
Fault value (r0949, interpret hexadecimal):  
80000000 hex:  
- Internal software error.  
00000001 hex ... 0000FFFF hex:  
- Module fault.

**Remedy**
  
For fault value = 80000000 hex:  
- Upgrade firmware to later version.  
For fault value = 00000001 hex ... 0000FFFF hex:  
- Replace the module.

### F30907 Power unit: FPGA configuration unsuccessful

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
During initialization within the power unit, an internal software error has occurred.

**Remedy**
  
- If required, upgrade the firmware in the power unit.  
- Replace power unit.  
- Contact Technical Support.

### A30919 Power unit: Temperature monitoring failed

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Overtemperature of the electronic components (6)

**Component:**
  
Power Unit

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The temperature monitoring in the power unit has failed.  
Fault-free operation of the drive system is no longer guaranteed.  
Alarm value (r2124, interpret binary):  
Bit 0: Sensor 1 for the internal temperature can no longer be evaluated.  
Bit 1: Sensor 2 for the internal temperature can no longer be evaluated.

**Remedy**
  
Replace the power unit immediately.

### F30950 Power unit: Internal software error

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
POWER ON

**Cause**
  
An internal software error has occurred.  
Fault value (r0949, interpret decimal):  
Information about the fault source.  
Only for internal Siemens troubleshooting.

**Remedy**
  
- If necessary, upgrade the firmware in the power unit to a later version.  
- Contact Technical Support.

### A30999 Power unit: Unknown alarm

**Valid as of version:**
  
06.02.015

**Message value:**
  
New message: %1

**Message class:**
  
Power electronics faulted (5)

**Component:**
  
Power Unit

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
An alarm has occurred on the power unit, which cannot be interpreted by the converter
firmware.  
This can occur if the firmware on this component is more recent than the firmware
on the converter.  
Alarm value (r2124, interpret decimal):  
Alarm number.  
Note:  
If required, the significance of this new alarm can be read about in a more recent
description of the converter.

**Remedy**
  
- Replace the firmware on the power unit by an older firmware version.  
- Upgrade the converter firmware.

### F31110 Motor encoder: Serial communication faulted

**Valid as of version:**
  
06.02.015

**Message value:**
  
Fault cause: %1 bin

**Message class:**
  
Position/speed actual value incorrect or not available (11)

**Component:**
  
Encoder 1

**Response:**
  
 ENCODER

**Acknowledgment:**
  
PULSE INHIBIT

**Cause**
  
There is an error in the transfer of the serial communication protocol between the
encoder and internal or external evaluation module.  
Fault value (r0949, interpret binary):  
Bit 0: Alarm bit in the position protocol.  
Bit 2: Encoder does not respond (does not supply a start bit within 50 ms).  
Bit 3: CRC error: The checksum in the protocol from the encoder does not match the
data.  
Bit 6: Timeout when cyclically reading.  
Bit 7: Timeout for the register communication.  
Bit 14: Register communication error.

**Remedy**
  
For fault value, bit 0 = 1:  
- Encoder defect F31111 may provide further details.  
For fault value, bit 2 = 1:  
- Incorrect encoder type / replace the encoder or encoder cable.  
For fault value, bit 3 = 1:  
- EMC / connect the cable shield, replace the encoder or encoder cable.  
For fault value, bit 6 = 1:  
- Update the firmware  
For fault value, bit 7 = 1:  
- Incorrect encoder type / replace the encoder or encoder cable.  
For fault value, bit 14 = 1:  
- Incorrect encoder type / replace the encoder or encoder cable.

### F31111 Motor encoder: Encoder signals an internal error (detailed information)

**Valid as of version:**
  
06.02.015

**Message value:**
  
Fault cause: %1 bin, additional information: %2

**Message class:**
  
Position/speed actual value incorrect or not available (11)

**Component:**
  
Encoder 1

**Response:**
  
 ENCODER

**Acknowledgment:**
  
PULSE INHIBIT

**Cause**
  
The encoder error word provides detailed information (error bit).  
Fault value (r0949, interpret binary):  
yyyyxxxx hex: yyyy = supplementary information, xxxx = fault cause  
Bit 0: Error in the multiturn block.  
Bit 1: EEPROM error.  
Bit 2: Singleturn position incorrect.  
Bit 3: Multiturn position incorrect.  
Bit 4: MLS generation error.  
Bit 5: Reserved.  
Bit 6: Overtemperature.  
Bit 7: Internal fault.

**Remedy**
  
Encoder is defective. Replace the encoder or motor.

### F31112 Motor encoder: Encoder signals an internal error

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Position/speed actual value incorrect or not available (11)

**Component:**
  
Encoder 1

**Response:**
  
 ENCODER

**Acknowledgment:**
  
PULSE INHIBIT

**Cause**
  
The encoder signals an internal error via serial protocol.  
Fault value (r0949, interpret binary):  
Bit 0: Fault bit in the position protocol.

**Remedy**
  
For fault value, bit 0 = 1:  
In the case of an EnDat encoder, F31111 may provide further details.

### F31150 Motor encoder: Initialization error

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
Sensor Module Encoder 1

**Response:**
  
 ENCODER

**Acknowledgment:**
  
PULSE INHIBIT

**Cause**
  
Encoder functionality selected in p0404 cannot be executed.  
Fault value (r0949, interpret hexadecimal):  
Encoder malfunction.  
The bit assignment corresponds to that of p0404 (e.g. bit 5 set: Error track C/D).  
See also: p0404 (Encoder configuration effective)

**Remedy**
  
- Check that p0404 is correctly set.  
- Check the encoder type used (incremental/absolute) and for SMCxx, the encoder cable.  
- If relevant, note additional fault messages that describe the fault in detail.

### A31407 Motor encoder: Function limit reached

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Position/speed actual value incorrect or not available (11)

**Component:**
  
Encoder 1

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The encoder has reached one of its function limits. A service is recommended.  
Alarm value (r2124, interpret decimal):  
1: Incremental signals  
3: Absolute track  
4: Code connection

**Remedy**
  
Perform service. Replace the encoder if necessary.

### A31410 Motor encoder: Communication error (encoder and Sensor Module)

**Valid as of version:**
  
06.02.015

**Message value:**
  
Fault cause: %1 bin

**Message class:**
  
Position/speed actual value incorrect or not available (11)

**Component:**
  
Encoder 1

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
There is an error in the transfer of the serial communication protocol between the
encoder and internal or external evaluation module.  
Fault value (r0949, interpret binary):  
Bit 0: Alarm bit in the position protocol.  
Bit 2: Encoder does not respond (does not supply a start bit within 50 ms).  
Bit 3: CRC error: The checksum in the protocol from the encoder does not match the
data.  
Bit 6: Timeout when cyclically reading.  
Bit 7: Timeout for the register communication.  
Bit 14: Register communication error.

**Remedy**
  
- Check that the encoder cables are routed in compliance with EMC.  
- Check the plug connections.  
- Replace encoder.

### A31411 Motor encoder: Encoder signals an internal alarm (detailed information)

**Valid as of version:**
  
06.02.015

**Message value:**
  
Fault cause: %1 bin, additional information: %2

**Message class:**
  
Position/speed actual value incorrect or not available (11)

**Component:**
  
Encoder 1

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The encoder error word provides detailed information (alarm bit).  
Alarm value (r2124, interpret binary):  
yyyyxxxx hex: yyyy = supplementary information, xxxx = fault cause  
Bit 0: LED current incorrect.  
Bit 1: Signal amplitude outside the control range.  
Bit 2: Overtemperature.

**Remedy**
  
Replace encoder.

### A31412 Motor encoder: Encoder signals an internal alarm

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Position/speed actual value incorrect or not available (11)

**Component:**
  
Encoder 1

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The encoder signals an internal alarm via serial protocol.  
Alarm value (r2124, interpret binary):  
Bit 0: Fault bit in the position protocol.  
Bit 1: Alarm bit in the position protocol.

**Remedy**
  
- Carry out a POWER ON (switch-off/switch-on) for all components.  
- Check that the encoder cables are routed in compliance with EMC.  
- Check the plug connections.  
- Replace encoder.

### F31502 Motor encoder: Encoder with measuring gearbox without valid signals

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Position/speed actual value incorrect or not available (11)

**Component:**
  
Sensor Module Encoder 1

**Response:**
  
 OFF1

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The encoder with measuring gearbox no longer provides any valid signals.

**Remedy**
  
It must be ensured that all of the encoders, with mounted measuring gearbox, provide
valid actual values in operation.

### F31503 Motor encoder: Position tracking cannot be reset

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Position/speed actual value incorrect or not available (11)

**Component:**
  
None

**Response:**
  
 OFF1

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The position tracking for the measuring gearbox cannot be reset.

**Remedy**
  
The fault should be resolved as follows:  
- Select commissioning.  
- Reset the position tracking as follows (p0411.2 = 1).  
- Deselect commissioning.  
The fault should then be acknowledged and the absolute encoder adjusted.

### A31700 Motor encoder: Functional safety monitoring initiated

**Valid as of version:**
  
06.02.015

**Message value:**
  
Fault cause: %1 bin

**Message class:**
  
Safety monitoring channel has identified an error (10)

**Component:**
  
Sensor Module Encoder 1

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
Functional safety was activated. Self test of the DRIVE-CLiQ encoder has detected
a fault.  
Alarm value (r2124, interpret binary):  
Bit x = 1: Effectivity test x unsuccessful.

**Remedy**
  
Replace encoder.

### F31802 Motor encoder: Time slice overflow

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Sensor Module Encoder 1

**Response:**
  
 ENCODER

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
A time slice overflow for the motor encoder has occurred.  
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

**Remedy**
  
Increase the current controller sampling time  
Note:  
For a current controller sampling time = 31.25 µs, use an SMx20 with Article No. 6SL3055-0AA00-5xA3.

### F31804 Motor encoder: Sensor Module checksum error

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Sensor Module Encoder 1

**Response:**
  
 ENCODER

**Acknowledgment:**
  
POWER ON

**Cause**
  
A checksum error has occurred when reading-out the program memory on the Sensor Module.  
Fault value (r0949, interpret hexadecimal):  
yyyyxxxx hex  
yyyy: Memory area involved.  
xxxx: Difference between the checksum at POWER ON and the actual checksum.

**Remedy**
  
- Carry out a POWER ON (switch-off/switch-on).  
- Upgrade firmware to later version.  
- Check whether the permissible ambient temperature for the component is maintained.

### F31805 Motor encoder: EEPROM checksum error

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Sensor Module Encoder 1

**Response:**
  
 ENCODER

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
Data in the EEPROM corrupted .  
Fault value (r0949, interpret hexadecimal):  
01: EEPROM access error.  
02: Too many blocks in the EEPROM.

**Remedy**
  
Replace the module.

### F31813 Motor encoder: Hardware logic unit failed

**Valid as of version:**
  
06.02.015

**Message value:**
  
Fault cause: %1 bin

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Sensor Module Encoder 1

**Response:**
  
 ENCODER

**Acknowledgment:**
  
PULSE INHIBIT

**Cause**
  
The logic unit of the DRIVE-CLiQ encoder has failed.  
Fault value (r0949, interpret binary):  
Bit 0: ALU watchdog has responded.  
Bit 1: ALU has detected a sign-of-life error.

**Remedy**
  
When the error reoccurs, replace the encoder.

### F31850 Motor encoder: Encoder evaluation internal software error

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Sensor Module Encoder 1

**Response:**
  
 ENCODER

**Acknowledgment:**
  
POWER ON

**Cause**
  
An internal software error has occurred in the Sensor Module of the motor encoder.  
Fault value (r0949, interpret decimal):  
1: Background time slice is blocked.  
2: Checksum over the code memory is not correct.  
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

**Remedy**
  
- Replace the Sensor Module.  
- If required, upgrade the firmware.  
- Contact Technical Support.

### F31899 Motor encoder: Unknown fault

**Valid as of version:**
  
06.02.015

**Message value:**
  
New message: %1

**Message class:**
  
Position/speed actual value incorrect or not available (11)

**Component:**
  
Sensor Module Encoder 1

**Response:**
  
 ENCODER

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
A fault has occurred on the Sensor Module for the motor encoder, which cannot be interpreted
by the Control Unit firmware.  
This can occur if the firmware on this component is more recent than the firmware
on the Control Unit.  
Fault value (r0949, interpret decimal):  
Fault number.  
Note:  
If required, the significance of this new fault can be read about in a more recent
description of the Control Unit.

**Remedy**
  
- Replace the firmware on the Sensor Module by an older firmware version (r0148).  
- Upgrade the firmware on the Control Unit (r0018).

### A31902 Motor encoder: SPI-BUS error occurred

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Sensor Module Encoder 1

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
Error when operating the internal SPI bus.  
Alarm value (r2124, interpret hexadecimal):  
Only for internal Siemens troubleshooting.

**Remedy**
  
- Replace the Sensor Module.  
- If required, upgrade the firmware in the Sensor Module.  
- Contact Technical Support.

### A31903 Motor encoder: I2C-BUS error occurred

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Sensor Module Encoder 1

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
Error when operating the internal I2C bus.  
Alarm value (r2124, interpret hexadecimal):  
Only for internal Siemens troubleshooting.

**Remedy**
  
- Replace the Sensor Module.  
- If required, upgrade the firmware in the Sensor Module.  
- Contact Technical Support.

### F31905 Motor encoder: Encoder parameterization error

**Valid as of version:**
  
06.02.015

**Message value:**
  
Parameter: %1, supplementary information: %2

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
Sensor Module Encoder 1

**Response:**
  
 ENCODER

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
An error was identified in the encoder parameterization.  
It is possible that the parameterized encoder type does not match the connected encoder.  
Determine the parameter number using the fault value (r0949).  
  
Fault value (r0949, interpret decimal):  
yyyyxxxx dec: yyyy = supplementary information, xxxx = parameter  
yyyy = 0:  
No additional information available.  
yyyy = 10:  
The connected encoder is not supported.

**Remedy**
  
- Check whether the connected encoder type matches the encoder that has been parameterized.  
- Correct the parameter specified by the fault value (r0949).

### F31950 Motor encoder: Internal software error

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Sensor Module Encoder 1

**Response:**
  
 ENCODER

**Acknowledgment:**
  
POWER ON

**Cause**
  
An internal software error has occurred.  
Fault value (r0949, interpret decimal):  
The fault value contains information regarding the fault source.  
Only for internal Siemens troubleshooting.

**Remedy**
  
- If necessary, upgrade the firmware in the Sensor Module to a later version.  
- Contact Technical Support.

### A31999 Motor encoder: Unknown alarm

**Valid as of version:**
  
06.02.015

**Message value:**
  
New message: %1

**Message class:**
  
Position/speed actual value incorrect or not available (11)

**Component:**
  
Sensor Module Encoder 1

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
An alarm has occurred on the Sensor Module for encoder 1, which cannot be interpreted
by the converter firmware.  
This can occur if the firmware on this component is more recent than the converter
firmware.  
Alarm value (r2124, interpret decimal):  
Alarm number.  
Note:  
If required, the significance of this new alarm can be read about in a more recent
description of the converter.

**Remedy**
  
- Replace the firmware on the Sensor Module by an older firmware version.  
- Upgrade the converter firmware.

### F32805 Encoder 2: EEPROM checksum error

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Sensor Module Encoder 2

**Response:**
  
 OFF1

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
Data in the EEPROM corrupted .  
Fault value (r0949, interpret hexadecimal):  
01: EEPROM access error.  
02: Too many blocks in the EEPROM.

**Remedy**
  
Replace the module.

### F32899 Encoder 2: Unknown fault

**Valid as of version:**
  
06.02.015

**Message value:**
  
New message: %1

**Message class:**
  
Position/speed actual value incorrect or not available (11)

**Component:**
  
Sensor Module Encoder 2

**Response:**
  
 OFF1

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
A fault occurred on the Sensor Module for encoder 2, which cannot be interpreted by
the converter firmware.  
This can occur if the firmware on this component is more recent than the converter
firmware.  
Fault value (r0949, interpret decimal):  
Fault number.  
Note:  
If required, the significance of this new fault can be read about in a more recent
description of the converter.

**Remedy**
  
- Replace the firmware on the Sensor Module by an older firmware version.  
- Upgrade the converter firmware.

### F32950 Encoder 2: Internal software error

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Sensor Module Encoder 2

**Response:**
  
 OFF1

**Acknowledgment:**
  
POWER ON

**Cause**
  
An internal software error has occurred.  
Fault value (r0949, interpret decimal):  
Information about the fault source.  
Only for internal Siemens troubleshooting.

**Remedy**
  
- If necessary, upgrade the firmware in the Sensor Module to a later version.  
- Contact Technical Support.

### A32999 Encoder 2: Unknown alarm

**Valid as of version:**
  
06.02.015

**Message value:**
  
New message: %1

**Message class:**
  
Position/speed actual value incorrect or not available (11)

**Component:**
  
Sensor Module Encoder 2

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
An alarm has occurred on the Sensor Module for encoder 2, which cannot be interpreted
by the converter firmware.  
This can occur if the firmware on this component is more recent than the converter
firmware.  
Alarm value (r2124, interpret decimal):  
Alarm number.  
Note:  
If required, the significance of this new alarm can be read about in a more recent
description of the converter.

**Remedy**
  
- Replace the firmware on the Sensor Module by an older firmware version.  
- Upgrade the converter firmware.

### F33899 Encoder 3: Unknown fault

**Valid as of version:**
  
06.02.015

**Message value:**
  
New message: %1

**Message class:**
  
Position/speed actual value incorrect or not available (11)

**Component:**
  
Sensor Module Encoder 3

**Response:**
  
 OFF1

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
A fault occurred on the Sensor Module for encoder 3, which cannot be interpreted by
the converter firmware.  
This can occur if the firmware on this component is more recent than the converter
firmware.  
Fault value (r0949, interpret decimal):  
Fault number.  
Note:  
If required, the significance of this new fault can be read about in a more recent
description of the converter.

**Remedy**
  
- Replace the firmware on the Sensor Module by an older firmware version.  
- Upgrade the converter firmware.

### A33999 Encoder 3: Unknown alarm

**Valid as of version:**
  
06.02.015

**Message value:**
  
New message: %1

**Message class:**
  
Position/speed actual value incorrect or not available (11)

**Component:**
  
Sensor Module Encoder 3

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
An alarm has occurred on the Sensor Module for encoder 3, which cannot be interpreted
by the converter firmware.  
This can occur if the firmware on this component is more recent than the converter
firmware.  
Alarm value (r2124, interpret decimal):  
Alarm number.  
Note:  
If required, the significance of this new alarm can be read about in a more recent
description of the converter.

**Remedy**
  
- Replace the firmware on the Sensor Module by an older firmware version.  
- Upgrade the converter firmware.

### F34950 VSM: Internal software error

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Voltage Sensing Module (VSM)

**Response:**
  
 OFF2

**Acknowledgment:**
  
POWER ON

**Cause**
  
An internal software error in the Voltage Sensing Module (VSM) has occurred.  
Fault value (r0949, interpret decimal):  
Information about the fault source.  
Only for internal Siemens troubleshooting.

**Remedy**
  
- If necessary, upgrade the firmware in the Voltage Sensing Module to a later version.  
- Contact Technical Support.

### F35220 TM: Frequency limit reached for signal output

**Valid as of version:**
  
06.02.015

**Message value:**
  
-

**Message class:**
  
Application/technological function faulted (17)

**Component:**
  
Terminal Module (TM)

**Response:**
  
 OFF1

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The signals output from the Terminal Module 41 (TM41) for tracks A/B have reached
the limit frequency. The output signals are no longer in synchronism with the specified
setpoint.  
SIMOTION (p4400 = 0) operating mode:  
- If the TM41 has been configured as the technology project, this fault is also output
in response to short-circuited A/B signals in X520.  
SINAMICS (p4400 = 1) operating mode:  
- The fine resolution of TM41 in p0418 does not match that of the encoder that was
interconnected at connector input p4420.  
- The encoder position actual value r0479 interconnected at connector input p4420
has an excessively high actual speed.  
- The output signals correspond to a speed, which is greater than the maximum speed
(r1082 of TM41).

**Remedy**
  
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

### F35950 TM: Internal software error

**Valid as of version:**
  
06.02.015

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Terminal Module (TM)

**Response:**
  
 OFF2

**Acknowledgment:**
  
POWER ON

**Cause**
  
An internal software error has occurred.  
Fault value (r0949, interpret decimal):  
Information about the fault source.  
Only for internal Siemens troubleshooting.

**Remedy**
  
- If necessary, upgrade the firmware in the Terminal Module to a later version.  
- Contact Technical Support.

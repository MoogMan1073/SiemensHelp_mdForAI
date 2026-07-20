---
title: "SINAMICS Alarms S210"
package: sdral401enUS
topics: 318
source: Siemens TIA Portal Information System (offline help, en-US)
---


# SINAMICS Alarms S210

This section contains the alarm descriptions for the devices listed below. The alarm descriptions for the various devices can differ. In the table of contents, you will then see a separate entry for each alarm number. The following device variants are taken into account in the online help:

- SINAMICS S210 (from SINAMICS RT V6.1)

## SINAMICS Alarms S210 01000 - 01780

SINAMICS Alarms S210 01000 - 01780

### F01000 Internal software error

**Valid as of version:**
  
06.01.122

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
  
06.01.122

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
  
- Carry out a POWER ON (switch-off/switch-on).  
- Upgrade firmware to later version.  
- Contact Technical Support.

### F01002 Internal software error

**Valid as of version:**
  
06.01.122

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
  
06.01.122

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
  
06.01.122

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

### F01005 Firmware download for DRIVE-CLiQ component unsuccessful

**Valid as of version:**
  
06.01.122

**Message value:**
  
Component number: %1, fault cause: %2

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause | Remedy |
| For %2 | 11 | DRIVE-CLiQ component has detected a checksum error. | After POWER ON has been carried out again for the DRIVE-CLiQ component, download firmware again. |
| 15 | The selected DRIVE-CLiQ component did not accept the contents of the firmware file. | Use a suitable firmware version |  |
| 18 | Firmware version is too old and is not accepted by the component. | Use a suitable firmware version |  |
| 19 | Firmware version is not suitable for the hardware release of the component. | Use a suitable firmware version |  |
| 101 | After several communication attempts, no response from the DRIVE-CLiQ component. | Check the DRIVE-CLiQ wiring. |  |
| 139 | Initially, only one new boot loader was loaded. | After POWER ON has been carried out again for the DRIVE-CLiQ component, download firmware again. |  |
| 140 | Firmware file for the DRIVE-CLiQ component not available on the memory card. | Use a suitable firmware version |  |
| 141 | An inconsistent length of the firmware file was signaled. | Use a suitable firmware version |  |
| 142 | Component has not changed to the mode for firmware download. | After POWER ON has been carried out again for the DRIVE-CLiQ component, download firmware again. |  |
| 156 | Component with the specified component number is not available (p7828). | Check the selected component number. |  |

**Message class:**
  
Hardware/software error (1)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
It was not possible to download the firmware to a DRIVE-CLiQ component.  
Fault value (r0949, interpret hexadecimal):  
yyxxxx hex: yy = component number, xxxx = fault cause  
Example: xxxx = 000B hex = 11 dec:  
  
xxxx = 008D hex = 141 dec:  
An inconsistent length of the firmware file was signaled.  
The firmware download may have been caused by a loss of connection to the firmware
file.  
This can occur during a project download/reset, for example.  
  
xxxx = 008F hex = 143 dec:  
Component has not changed to the mode for firmware download. It was not possible to
delete the existing firmware.  
  
xxxx = 0090 hex = 144 dec:  
When checking the firmware that was downloaded (checksum), the component detected
a fault. It is possible that the file on the memory card is defective.  
  
xxxx = 0091 hex = 145 dec:  
Checking the loaded firmware (checksum) was not completed by the component in the
appropriate time.

**Remedy**
  
- Check the selected component number.  
- Check the DRIVE-CLiQ wiring.  
- Use a component with a suitable hardware version.  
- After warm restart has been carried out again for the DRIVE-CLiQ component, download
the firmware again.

### A01006 Firmware update for DRIVE-CLiQ component required

**Valid as of version:**
  
06.01.122

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
  
The firmware of a DRIVE-CLiQ component must be updated as there is no suitable firmware
or firmware version in the component for operation with the converter.  
Alarm value (r2124, interpret decimal):  
Component number of the DRIVE-CLiQ component.

**Remedy**
  
Repeat the firmware update by switching off the device and switching on again.

### A01007 POWER ON for DRIVE-CLiQ component required

**Valid as of version:**
  
06.01.122

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
  
06.01.122

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
  
06.01.122

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

### F01015 Internal software error

**Valid as of version:**
  
06.01.122

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
  
06.01.122

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

### F01018 Runup has been interrupted several times

**Valid as of version:**
  
06.01.122

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
  
06.01.122

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
  
06.01.122

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
  
06.01.122

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
  
06.01.122

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
  
06.03.014

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
  
06.01.122

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
See also: r0304 (Rated motor voltage), r0305 (Rated motor current), p2000 (Reference speed),
p2002 (Reference current), p2003 (Reference torque)

### F01034 Units changeover: Calculation parameter values after reference value change unsuccessful

**Valid as of version:**
  
06.01.122

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
See also: r0304 (Rated motor voltage), r0305 (Rated motor current), p2000 (Reference speed),
p2002 (Reference current), p2003 (Reference torque)

**Remedy**
  
- Select the value of the reference parameter such that the parameter involved can
be calculated in the per unit representation.

### A01035 ACX: Parameter backup file corrupted

**Valid as of version:**
  
06.01.122

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
  
06.01.122

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
  
06.03.014

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
  
06.01.122

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
  
06.01.122

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
  
- Save parameters (p0977).  
- Carry out a POWER ON (switch-off/switch-on).  
Then:  
- Upload the data to the converter (commissioning tool).

### F01041 Parameter save necessary

**Valid as of version:**
  
06.01.122

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
  
06.01.122

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
  
06.01.122

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
  
06.01.122

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
  
06.01.122

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
  
06.01.122

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
  
06.01.122

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

### A01069 Parameter backup and device incompatible

**Valid as of version:**
  
06.01.122

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
  
06.01.122

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
  
06.01.122

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
  
06.01.122

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
it is necessary to carry out a POWER ON or hardware reset (p0972) of the converter.  
Note:  
It is possible that a new POWER ON is requested via this alarm.

**Remedy**
  
- Carry out a POWER ON for the converter (switch off/switch on).  
- Carry out a hardware reset (RESET button, p0972).

### F01082 Parameter error when running up from data backup

**Valid as of version:**
  
06.01.122

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

### F01122 Frequency at the measuring probe input too high

**Valid as of version:**
  
06.01.122

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

### F01200 CU: Time slice management internal software error

**Valid as of version:**
  
06.03.014

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

### F01250 EEPROM incorrect read-only data

**Valid as of version:**
  
06.01.122

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
  
06.01.122

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

### A01304 Firmware version of DRIVE-CLiQ component is not up-to-date

**Valid as of version:**
  
06.01.122

**Message value:**
  
%1

**Message class:**
  
General drive fault (19)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The non-volatile memory has a more recent firmware version than the one in the connected
DRIVE-CLiQ component.  
Alarm value (r2124, interpret decimal):  
Component number of the DRIVE-CLiQ component involved.

**Remedy**
  
Repeat the firmware update by switching off the device and switching on again.

### A01306 Firmware of the DRIVE-CLiQ component being updated

**Valid as of version:**
  
06.01.122

**Message value:**
  
%1

**Message class:**
  
General drive fault (19)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
Firmware update is active for at least one DRIVE-CLiQ component.  
Alarm value (r2124, interpret decimal):  
Component number of the DRIVE-CLiQ component.

**Remedy**
  
Not necessary.  
This alarm is automatically withdrawn after the firmware update has been completed.

### A01330 Topology: Commissioning not possible

**Valid as of version:**
  
06.01.122

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
  
Unable to carry out commissioning. The actual topology does not fulfill the requirements.

**Remedy**
  
- Check the OCC cable between the converter and motor/encoder.  
- Carry out a POWER ON (switch-off/switch-on).  
- Check that the connected hardware is supported.  
Note:  
OCC: One Cable Connection (one cable system)

### F01357 Topology: Two converters identified on the DRIVE-CLiQ line

**Valid as of version:**
  
06.01.122

**Message value:**
  
component number: %1, connection number: %2

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
In the actual topology, 2 converters are connected with one another through DRIVE-CLiQ.  
As standard, this is not permitted.  
Fault value (r0949, interpret hexadecimal):  
yyxx hex:  
yy = connection number of the converter to which the second converter is connected  
xx = component number of the converter to which the second converter is connected  
Note:  
Pulse enable is withdrawn and prevented.

**Remedy**
  
- Remove the connection to the second converter and restart.

### A01482 Topology: Sensor Module not connected

**Valid as of version:**
  
06.03.014

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
  
The topology comparison has detected a Sensor Module that is missing in the actual
topology with respect to the target topology.  
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
- Check DRIVE-CLiQ cables for interruption and contact problems.  
- Check that the component is working properly.

### A01484 Topology: DRIVE-CLiQ Hub Module not connected

**Valid as of version:**
  
06.03.014

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
  
The topology comparison has detected a DRIVE-CLiQ Hub Module missing in the actual
topology with respect to the target topology.  
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
- Check DRIVE-CLiQ cables for interruption and contact problems.  
- Check that the component is working properly.

### A01489 Topology: motor with DRIVE-CLiQ not connected

**Valid as of version:**
  
06.01.122

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
  
The topology comparison has detected a motor with DRIVE-CLiQ missing in the actual
topology with respect to the target topology.  
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
- Check DRIVE-CLiQ cables for interruption and contact problems.  
- Check that the component is working properly.  
Note:  
Under "Topology --> Topology view" the commissioning tool where relevant offers improved
diagnostics capability (e.g. setpoint/actual value comparison).

### A01550 Security: Drive data encryption invalid

**Valid as of version:**
  
06.03.014

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
  
06.01.122

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

### C01600 SI: STO self test failed

**Valid as of version:**
  
06.01.122

**Message value:**
  
%1

**Message class:**
  
Safety monitoring channel has identified an error (10)

**Component:**
  
None

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The "Safety Integrated" function integrated in the drive has identified a fault in
the self test of the switch-off signal path, and has initiated an STO (Safe Torque
Off).  
Fault value (r60049, interpret decimal):  
1005: STO active, although STO not selected and there is no internal STO active.  
1010: STO inactive, although STO is selected or an internal STO is active.  
1015: The self test was unsuccessful in operation.  
1016: Error in the communication path to the I/O processor.

**Remedy**
  
- Select STO and then deselect again.  
- Carry out a POWER ON (switch-off/switch-on) for all components.  
- Upgrade software to a later version.  
- Contact Technical Support.

### C01603 SI: Module temperature - limit value exceeded

**Valid as of version:**
  
06.01.122

**Message value:**
  
-

**Message class:**
  
Safety monitoring channel has identified an error (10)

**Component:**
  
None

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
A safe monitoring function has detected that the module temperature has exceeded a
limit value. STO (Safe Torque Off) was initiated to maintain the safe state.

**Remedy**
  
- Check the ambient temperature.  
- Check the module fan.  
- Operate the module in the permissible range.

### F01604 SI: Safety EEPROM data error

**Valid as of version:**
  
06.01.122

**Message value:**
  
%1

**Message class:**
  
Safety monitoring channel has identified an error (10)

**Component:**
  
Control Unit (CU)

**Response:**
  
 OFF2

**Acknowledgment:**
  
POWER ON

**Cause**
  
Safety relevant EEPROM data are not correct.  
This message results in an STO (Safe Torque Off).  
  
Message value (r0949, interpret decimal): Only for internal Siemens fault diagnostics.

**Remedy**
  
Replace the module.

### A01605 SI: Checksum error has occurred

**Valid as of version:**
  
06.01.122

**Message value:**
  
%1

**Message class:**
  
Safety monitoring channel has identified an error (10)

**Component:**
  
Control Unit (CU)

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
A checksum error (CRC error) has occurred in the converter program memory.  
Alarm value (r2124, interpret decimal):  
Only for internal Siemens troubleshooting.

**Remedy**
  
- Carry out a POWER ON (switch-off/switch-on).  
- Upgrade firmware to later version.  
- Contact Technical Support.

### C01630 SI: Brake control error

**Valid as of version:**
  
06.01.122

**Message value:**
  
%1

**Message class:**
  
Safety monitoring channel has identified an error (10)

**Component:**
  
None

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The "Safety Integrated" function integrated in the drive has identified a brake control
fault, and has initiated an STO.  
Fault value (r0949, interpret decimal):  
1:  
Fault in the "Open brake" state.  
- Parameter p1278 incorrectly set.  
- Brake not connected or interrupted cable (check whether for p1278 = 1 and p9604
bit 1 = 0 (SBC deactivated) the brake opens).  
- Ground fault in brake cable.  
2:  
Fault in the "Close brake" state.  
- Brake not connected or interrupted cable (check whether for p1278 = 1 and p9604
bit 1 = 0 (SBC deactivated) the brake opens).  
- Short-circuit in brake winding.  
3:  
Hardware is defective or does not support the brake control.  
- Communication with the brake control has failed.  
- SBC is enabled on a module that does not support brake control.  
4:  
- Brake is not connected or interrupted cable.

**Remedy**
  
- Check the motor holding brake connection.  
- Check the function of the motor holding brake.  
- Check whether the brake control is supported.  
- Check whether there are disturbances in the communications from the self-identifying
brake, and if required carry out a diagnostics routine for the faults involved.  
- Check that the electrical cabinet design and cable routing are in compliance with
EMC regulations (e.g. shield of the motor cable and brake conductors are connected
with the shield connecting plate and the motor connectors are tightly screwed to the
housing).  
- Replace the hardware.  
  
Note:  
SBC: Safe Brake Control  
SI: Safety Integrated

### A01631 SI: Motor holding brake/SBC configuration not practical

**Valid as of version:**
  
06.01.122

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
  
A configuration of motor holding brake and SBC was detected that is not practical.  
The following configurations can result in this message:  
- "No motor holding brake available" (p1215 = 0) and "SBC" enabled (p9604 bit 1 =
1 and p9603>0).

**Remedy**
  
Check the parameterization of the motor holding brake and SBC and correct.  
Note:  
SBC: Safe Brake Control  
See also: p1215 (Motor holding brake configuration), p9603 (SI control), p9604 (SI enable)

### A01637 SI: Safety configuration not protected

**Valid as of version:**
  
06.01.122

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
  
Safety configuration is not protected using UMAC (User Management and Access Control).

**Remedy**
  
Activate UMAC and assign the rights for changing the "Edit Safety Integrated application"
safety configuration to a specific user that is saved with user name and password.

### A01641 SI: Component exchange identified and save necessary

**Valid as of version:**
  
06.01.122

**Message value:**
  
Fault cause: %1

|  |  |  |  |
| --- | --- | --- | --- |
|  | Bit | Cause | Remedy |
| For %1 | 0 | It was identified that the drive has been replaced |  |
| 4 | It was identified that the Sensor Module has been replaced |  |  |
| 5 | It was identified that the sensor has been replaced |  |  |

**Message class:**
  
General drive fault (19)

**Component:**
  
Control Unit (CU)

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
"Safety Integrated" has identified that a component has been replaced.  
No additional stop response is initiated, and therefore the operation of the specific
drive is not restricted.  
When safety functions are active, after a component has been replaced it is necessary
to carry out a partial acceptance test.  
Alarm value (r2124, interpret binary).

**Remedy**
  
- Save all parameters (p0977 = 1 or retentively save).  
- Acknowledge fault.  
See also: r9776 (SI diagnostics)

### F01646 SI: Change logbook

**Valid as of version:**
  
06.01.122

**Message value:**
  
%1

**Message class:**
  
Safety monitoring channel has identified an error (10)

**Component:**
  
Control Unit (CU)

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The saved functional safety checksum (r9780[0]) or hardware-related safety checksum
(r9780[1]) differs from the safety checksum calculated when running up or a previously
calculated safety checksum was not found.  
An acceptance test is required as changes have been made to a safety parameter or
the safety hardware.  
Fault value (r0949, interpret decimal):  
1: The safety logbook has identified that a functional safety checksum has changed.
An acceptance test is required.  
2: The safety logbook has identified that a hardware-related safety checksum has changed.
An acceptance test is required.

**Remedy**
  
For fault value = 1:  
- Carry out an acceptance test and generate an acceptance report.  
For fault value = 2:  
- Carry out the function checks for the modified hardware and generate an acceptance
report.  
Note:  
The procedure when carrying out an acceptance test as well as an example of the acceptance
report are provided in the following literature:  
SINAMICS Function Manual Safety Integrated

### C01647 SI: PROFIsafe PLC configuring not the same as the parameterization

**Valid as of version:**
  
06.01.122

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
  
The drive has identified a difference between the PROFIsafe configuring in the F-PLC
and the parameterization in SINAMICS.  
Note:  
This message results in an STO (Safe Torque Off).  
Message value (r60049, interpret decimal):  
1: The PROFIsafe telegram number in the F-PLC configuration is not identical with
the value in p9611.  
2: The PROFIsafe monitoring time F_WD_Time in the F-PLC configuration is not identical
with the value in p9614.

**Remedy**
  
- Change the configuring in the F-PLC and load to the drive.  
- Adapt the parameterization in the drive to the configuration in the F-PLC.

### C01648 SI: PROFIsafe communication error

**Valid as of version:**
  
06.01.122

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
  
The drive has identified a PROFIsafe communication error.  
Note:  
This message results in:  
- STO, if p9612 = 0,  
- SS1, if p9612 = 1.  
Message value (r60049, interpret decimal):  
6000 ... 6166:  
PROFIsafe message values (PROFIsafe driver for PROFINET).  
For these message values, the failsafe control signals (failsafe values) are transferred
to the safety functions. If "SS1 after failure of PROFIsafe communication" is parameterized
(p9612), then transfer of the Failsafe Values is delayed.  
6064 ... 6076:  
Error when evaluating F parameters. The values of the transferred F parameters do
not match the expected values.  
6064: Destination address and PROFIsafe address are different (F_Dest_Add != p9610).  
6065: Destination address not valid (F_Dest_Add == 0 or 0xFFFF).  
6066: Source address not valid (F_Source_Add == 0 or 0xFFFF) or source address and
PROFIsafe source address different (F_Source_Add != p9613).  
6067: Watchdog time not valid (F_WD_Time == 0).  
6068: Incorrect SIL level (F_SIL).  
6069: Incorrect F-CRC length (F_CRC_Length).  
6070: Incorrect F parameter version (F_Par_Version).  
6071: CRC error for the F parameters (CRC1). The transferred CRC value of the F parameters
does not match the value calculated in the PROFIsafe driver.  
6072: F parameterization is inconsistent.  
6076: Incorrect F_block_ID.  
6165: A communications error was identified when receiving the PROFIsafe telegram.
The error can also occur if an inconsistent or out-of-date PROFIsafe telegram was
received after switching the system off and on or after inserting the PROFINET cable.  
6166: A time monitoring error (timeout) was identified when receiving the PROFIsafe
telegram.  
>65535: A fatal PROFIsafe communication error has occurred (only for internal Siemens
error diagnostics).

**Remedy**
  
For message value = 6064:  
- Check the setting of the value in the F parameter F_Dest_Add at the PROFIsafe device.  
- Check the setting of the PROFIsafe address (p9610).  
For message value = 6065:  
- Check the setting of the value in the F parameter F_Dest_Add at the PROFIsafe device.
It is not permissible that the destination address is 0 or FFFF.  
For message value = 6066:  
- Check the setting of the value in F-parameter F_Source_Add at the PROFIsafe device.
It is not permissible for the source address to be either 0 or FFFF.  
- Check the setting of the PROFIsafe source address (p9613).  
For message value = 6067:  
- Check the setting of the value in the F parameter F_WD_Time at the PROFIsafe device.
It is not permissible for the watchdog time to be 0.  
For message value = 6068:  
- Check the setting of the value in F parameter F_SIL at the PROFIsafe device.  
For message value = 6069:  
- Check the setting of the value in the F parameter F_CRC_Length at the PROFIsafe
device.  
For message value = 6070:  
- Check the setting of the value in the F parameter F_Par_Version at the PROFIsafe
device. The value for the F parameter version is 0 in the V1 mode and 1 in the V2
mode.  
For message value = 6071:  
- Check the setting of the values of the F parameters and the F parameter CRC (CRC1)
calculated from these at the PROFIsafe device and update if necessary.  
For message value = 6072:  
- Check the settings of the values for the F parameters and, if required, correct.  
The following combinations are permissible for F parameters F_CRC_Length and F_Par_Version:  
F_CRC_Length = 3-byte CRC and F_Par_Version = 1  
F_CRC_Length = 4-byte CRC and F_Par_Version = 1  
For message value = 6076:  
- Check the settings of the values for the F parameters and, if required, correct.  
For message value = 6165:  
- Acknowledge the fault if it occurs after running up or after inserting the PROFINET
cable.  
- Check the configuration and communication at the PROFIsafe device.  
- Check the setting of the value for F parameter F_WD_Time at the PROFIsafe device
and increase if necessary.  
- Check whether all F parameters of the drive match the F parameters of the F host.  
For message value = 6166:  
- Check the configuration and communication at the PROFIsafe device.  
- Check the setting of the value for F parameter F_WD_Time at the PROFIsafe device
and increase if necessary.  
- Evaluate diagnostic information in the F host.  
- Check PROFIsafe connection.  
- Check whether all F parameters of the drive match the F parameters of the F host.  
For message value > 65535:  
- Carry out a POWER ON (switch-off/switch-on) for all components.  
- Check whether other faults are active - and when necessary, carry out diagnostics
for the faults involved.  
- Increase the monitoring cycle clock settings (p9500, p9511).  
- Upgrade firmware to later version.  
- Contact Technical Support.  
- Replace hardware relevant for the communication.

### C01649 SI: Internal software error

**Valid as of version:**
  
06.01.122

**Message value:**
  
Module: %1, line: %2

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Control Unit (CU)

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
An internal error has occurred in the Safety Integrated software.  
Note:  
This message results in an STO (Safe Torque Off) that cannot be acknowledged.  
Message value (r60049, interpret hexadecimal): Only for internal Siemens fault diagnostics.

**Remedy**
  
- Carry out a POWER ON (switch-off/switch-on) for all components.  
- Re-commission the "Safety Integrated" function and carry out a POWER ON.  
- Upgrade firmware to later version.  
- Contact Technical Support.  
- Replace hardware component.

### F01650 SI: Acceptance test required

**Valid as of version:**
  
06.01.122

**Message value:**
  
%1

**Message class:**
  
Safety monitoring channel has identified an error (10)

**Component:**
  
Control Unit (CU)

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The drive-integrated "Safety Integrated" function requires an acceptance test.  
Message value (r0949, interpret decimal):  
2003: Acceptance test is required as a safety parameter has been changed.

**Remedy**
  
For message value = 2003:  
- Carry out an acceptance test and generate an acceptance report.  
The procedure when carrying out an acceptance test as well as an example of the acceptance
report are provided in the product operating instructions.

### C01652 SI: Monitoring clock cycle not permissible

**Valid as of version:**
  
06.01.122

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
  
One of the Safety Integrated monitoring clock cycles is not permissible.  
- The monitoring clock cycle for safe motion monitoring functions is not permissible
(p9500).  
- The actual value sensing clock cycle for safe motion monitoring functions is not
permissible (p9511).  
- The sampling time for the current controller (p0112, p0115[0]) cannot be supported.  
Message value (r60049, interpret decimal):  
When motion monitoring is enabled (p9603 > 0), the following applies:  
100: No matching monitoring clock cycle (p9500) was able to be found.  
107: The actual value sensing clock cycle (p9511) is not an integer multiple of the
sampling time of the current controller (p0115[0]).  
108: The parameterized actual value sensing clock cycle (p9511) cannot be set on this
component.  
111: The monitoring clock cycle (p9500) is not an integer multiple of the sampling
time of the current controller (p0115[0]).

**Remedy**
  
When motion monitoring is enabled (p9603 > 0):  
- Upgrade firmware to later version.  
- Correct the monitoring clock cycle (p9500) and carry out POWER ON.  
For message value = 100:  
Set the monitoring clock cycle in p9500 as an integer multiple of the sampling time
of the current controller (p9500 / 2 = n *current controller clock cycle)  
For message value = 107, 108:  
Set the actual value sensing clock cycle in p9511 as an integer multiple of the current
controller sampling time (p9511 = n * current controller clock cycle), and at the
same time as an integer divisor of the monitoring clock cycle (p9511 = p9500 / m).  
For message value = 111:  
Set the monitoring clock cycle in p9500 as an integer multiple of the sampling time
of the current controller.

### C01653 SI: PROFINET configuration error

**Valid as of version:**
  
06.01.122

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
  
There is a PROFINET configuration error for using Safety Integrated monitoring functions
with a higher-level control (F-PLC).  
Note:  
When the safety functions are enabled, this fault results in an STO that cannot be
acknowledged.  
Fault value (r0949, interpret decimal):  
200: A safety slot for receive data from the control has not been configured.  
210, 220: The configured safety slot for the receive data from the control has an
unknown format.  
230, 231: The configured safety slot for the receive data from the F-PLC has the incorrect
length.  
250: A PROFIsafe slot is configured in the higher-level F control, however PROFIsafe
is not enabled in the drive.  
300: A safety slot for the send data to the control has not been configured.  
310, 320: The configured safety slot for the send data to the control has an unknown
format.  
330, 331: The configured safety slot for the send data to the F-PLC has the incorrect
length.  
400: The telegram number in the F-PLC does not match the parameterization in the drive.

**Remedy**
  
The following generally applies:  
- Check and, if necessary, correct the PROFINET configuration of the safety slot on
the controller side.  
- Upgrade the drive firmware to a later version.  
For fault value = 250:  
- Remove the PROFIsafe configuring in the higher-level F control or enable PROFIsafe
in the drive.  
For fault value = 231, 331:  
- In the drive, parameterize the appropriate PROFIsafe telegram (p9611) to be set
on the F-PLC.  
- Configure the PROFIsafe telegram matching the parameterization (p9611) in the F-PLC.

### A01654 SI: PROFIsafe configuration different

**Valid as of version:**
  
06.01.122

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
  
The configuration of a PROFIsafe telegram in the higher-level control (F-PLC) does
not match the parameterization in the drive.  
Note:  
This message does not result in a safety stop response.  
Alarm value (r2124, interpret decimal):  
1:  
A PROFIsafe telegram is configured in the higher-level control; however, PROFIsafe
is not enabled in the drive (p9603.1).  
2:  
PROFIsafe is parameterized in the drive; however, a PROFIsafe telegram has not been
configured in the higher-level control.

**Remedy**
  
The following generally applies:  
- Check and, if necessary, correct the PROFIsafe configuration in the higher-level
control.  
For alarm value = 1:  
- Remove the PROFIsafe configuring in the higher-level F control or enable PROFIsafe
in the drive.  
For alarm value = 2:  
- Configure the PROFIsafe telegram to match the parameterization in the higher-level
F-control.

### C01657 SI: PROFIsafe telegram number invalid

**Valid as of version:**
  
06.01.122

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
  
The PROFIsafe telegram number set in p9611 is not valid.  
When PROFIsafe is enabled (p9603.1 = 1), then a telegram number greater than zero
must be entered in p9611.  
Note:  
This fault does not result in a safety stop response.  
See also: p9611 (SI PROFIsafe telegram selection), r60022 (PROFIsafe telegram)

**Remedy**
  
Check the telegram number setting (p9611).

### C01658 SI: PROFIsafe telegram number not equal

**Valid as of version:**
  
06.01.122

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
  
The PROFIsafe telegram number is set differently in p9611 and r60022.  
The telegram number must be identically set in both parameters.  
Note:  
This fault does not result in a safety stop response.  
See also: p9611 (SI PROFIsafe telegram selection)

**Remedy**
  
Align the telegram number in both parameters so that they are the same (p9611, r60022).

### C01667 SI: Project data imported from V5.2 has an error

**Valid as of version:**
  
06.03.014

**Message value:**
  
%1

**Message class:**
  
Safety monitoring channel has identified an error (10)

**Component:**
  
Control Unit (CU)

**Response:**
  
 OFF2

**Acknowledgment:**
  
POWER ON

**Cause**
  
A project file is loaded that was created with FW Version V5.2. The download was not
able to be completely executed.  
Fault value (r0949, interpret binary):  
Bit 0 = 1:  
A project file is corrupt. There is a difference between the actual checksums and
reference CRC checksums.  
Bit 1 = 1:  
p9523 < p9525, p9523 must be set >= p9525 in order to correctly convert p9676 (SI
identifier encoder properties).  
Bit 2 = 1:  
p9523 < p9524, p9523 must be set >= p9524 in order to correctly convert p9630 (SI
safe maximum speed encoder (rotary)).  
Bit 3 = 1:  
p9523 < (p9524 + p9525), p9523 must be set >= (p9524 + p9525) in order to correctly
convert p9631 (SI safe position accuracy encoder (rotary))  
Bit 4 = 1:  
In the project, p9518 was set to 0, which means that p9630 and p9631 are not correctly
converted.

**Remedy**
  
For bit 0:  
Save the project file in firmware version V5.2 again and load into the current firmware.  
For bits 1 ... 4:  
Resolve the error in firmware version V5.2, save the project again and load into the
current firmware.

### C01668 SI: Checksum error safety monitoring functions

**Valid as of version:**
  
06.01.122

**Message value:**
  
%1

**Message class:**
  
Safety monitoring channel has identified an error (10)

**Component:**
  
Control Unit (CU)

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The actual checksum calculated by the drive and entered in r10098 via the safety-relevant
parameters does not match the reference checksum saved in p10099 at the last machine
acceptance.  
Safety-relevant parameters have been changed or a fault is present.  
Note:  
This message results in an STO (Safe Torque Off).  
Message value (r60049, only for internal Siemens diagnostics)

**Remedy**
  
- Carry out safety commissioning.  
- Carry out an acceptance test.

### C01670 SI: invalid Sensor Module configuration

**Valid as of version:**
  
06.01.122

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
  
The configuration of a Sensor Module used for Safety Integrated is not permissible.  
Note:  
This message results in an STO (Safe Torque Off).  
Message value (r60049, interpret decimal):  
1: The encoder data set selected for Safety Integrated is not valid or the encoder
is not assigned to an encoder data set.  
2: No encoder was parameterized for Safety Integrated or the encoder is not suitable
for safety-related applications.  
4: A communication error with the encoder has occurred.  
5: Number of relevant bits in the encoder coarse position invalid.  
6: DRIVE-CLiQ encoder configuration invalid.  
7: Non-safety relevant component of the encoder coarse position for the linear DRIVE-CLiQ
encoder not valid.  
8: Safety comparison algorithm not supported.  
9: Relationship between the grid division and measuring step for linear DRIVE-CLiQ
encoder is not binary.  
15: Pulses per revolution of a rotary encoder is not valid.  
16: Grid division of a linear encoder is not valid.  
17: Encoder is not compatible. The safe positioning accuracy of the encoder is not
equal to the setpoint parameterized in p9631 - or the safe maximum speed/velocity
of the encoder is not equal to the setpoint parameterized in p9630.  
18: Encoder has still not been configured for Safety Integrated. The safe positioning
accuracy of the encoder has still not been parameterized in p9631 - and the safe maximum
velocity of the encoder has still not been parameterized in p9630 (parameter values
are 0).  
19: The encoder parameterization or the module identifier of the encoder/encoder module
has changed or the encoder parameterization is corrupt.  
20: For a DQi encoder, the offset between POS1 and POS2 has changed since the last
run up.  
21: The timer for the effectivity test for a DQi encoder is not equal to 4 hours.  
22: In the current firmware version, the encoder type is not permitted for Safety
Integrated.

**Remedy**
  
For message value = 1:  
Carefully ensure that a safety-relevant encoder is connected and repeat the drive
commissioning.  
  
For message value = 2:  
Use an encoder that supports safety functions.  
  
For message value = 4:  
Check whether there is a DRIVE-CLiQ communication error to the Sensor Module involved
and, if required, carry out a diagnostics routine for the faults identified.  
  
For message value =8:  
Use an encoder that implements an algorithm supported by Safety Integrated.  
Supported encoder types are listed in the product documentation for Safety Integrated.  
  
For message value = 5, 6, 7, 9, 15, 16, 19, 20, 21:  
Replace the encoder if it is defective.  
  
For message value = 17, 18:  
Select and deselect the safety commissioning mode (during safety commissioning, the
quality of the connected encoder is transferred into the encoder quality parameter
p9630 and ff.).  
  
For message value = 22:  
Use an encoder type that is supported in the current firmware version.  
Supported encoder types are listed in the product documentation for Safety Integrated.

### C01671 SI: Parameterization actual value acquisition incorrect

**Valid as of version:**
  
06.01.122

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
  
The parameterization of the actual value sensing for Safety Integrated is incorrect.  
Note:  
This message results in an STO (Safe Torque Off).  
Message value (r60049, interpret decimal):  
yyyyxxxx dec: yyyy = supplementary information, xxxx = parameter  
yyyy = 0:  
No additional supplementary information  
xxxx = 9522:  
The gear stage was set too high.

**Remedy**
  
Check the parameterization of the actual value sensing for Safety Integrated and if
required correct.  
For message value 9522:  
- Set the gearbox stage lower.

### C01674 SI: Safety function not supported by PROFIsafe telegram

**Valid as of version:**
  
06.01.122

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
  
The monitoring function enabled in p9604 is not supported by the currently set PROFIsafe
telegram (p9611).  
Note:  
Message value (r60049, interpret bitwise binary):  
Bit 3 = 1:  
SS1E (Safe Stop 1 External) via PROFIsafe is not supported (p9604.3).  
Bit 5 = 1:  
SS2E (Safe Stop 2 External) via PROFIsafe is not supported (p9604.5).  
Bit 6 = 1:  
SS2ESR: (Safe Stop 2 Extended Stop and Retract) via PROFIsafe is not supported (p9604.6).  
Bit 9 = 1:  
Transfer of SLS (Safely-Limited Speed) limit value via PROFIsafe is not supported
(p9604.9).  
Bit 15 = 1:  
Gearbox stage switchover via PROFIsafe is not supported (p9604.15).  
Bit 19 = 1:  
SCA via PROFIsafe is not supported (p9604.19).  
Bit 20 = 1:  
Transfer of safe position (SP) via PROFIsafe is not supported (p9604.20).  
Bit 30 = 1:  
Transfer of F-DI via PROFIsafe is not supported (p9604.30).

**Remedy**
  
- Deselect the monitoring function involved (p9604).  
- Set the matching PROFIsafe telegram (p9611).

### C01676 SI: Parameterization of the failsafe inputs not permissible

**Valid as of version:**
  
06.01.122

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
  
When controlled via terminal (p9603.0 = 1).  
- Only the failsafe digital input F-DI 0 (r10071.0) may be selected  
- Only STO (c10022) / SS1 (c10023) / SS1E (c10060) may be interconnected  
  
Note:  
This message results in an STO (Safe Torque Off).  
Message value (r60049, interpret decimal):  
xxxx = parameter number

**Remedy**
  
Correct parameters:  
- Interconnect with a valid signal source.  
- Inhibit control via terminal (p9603.0 = 0).

### C01677 SI: Incorrect onboard F-I/O parameter value

**Valid as of version:**
  
06.01.122

**Message value:**
  
Parameter: %1, supplementary information: %2

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The parameter cannot be parameterized with this value.  
Note:  
This message does not result in a safety stop response.  
Message value (r60049, interpret decimal): yyyyxxxx dec:  
yyyy = supplementary information  
xxxx = parameter  
  
yyyy = 0:  
No additional information available.  
  
xxxx = 10000 and  
yyyy = F-DI number:  
A non-existent F-DI was enabled.  
  
xxxx = 10002:  
The F-DI discrepancy time (p10002) is less than or equal to the SI monitoring clock
cycle (p9500).  
  
xxxx = 10017 and  
yyyy = F-DI number:  
The input filter (p10017) is less than or equal to (p10018 + 2ms) when simultaneously
selecting "Self test using specified dark pulses" (p10041[y] = 1).  
  
xxxx = 10018 and  
yyyy = F-DI number:  
Setting "F-DI self test length dark pulses" (p10018) is zero when simultaneously selecting
"Self test using specified dark pulses" (p10041[y] = 1).  
  
xxxx = 10041 and  
yyyy = F-DI number:  
An invalid value was set in "F-DI self test mode selection" (p10041[y]).  
  
xxxx = 10071 and  
yyyy = F-DI number:  
An F-DI status r10071[y], which was not enabled in p10000, was set.

**Remedy**
  
Correct the parameter value.  
For xxxx = 10000 and yyyy = F-DI number:  
- Correct "SI F-DI enable" (p10000).  
For xxxx = 10002:  
- Set "SI F-DI switchover discrepancy time" (p10002) longer than "SI monitoring clock
cycle" (p9500).  
For xxxx = 10017 and yyyy = F-DI number:  
- Set "SI digital inputs input filter" (p10017) greater than (p10018 + 2 ms)  
- Change "SI F-DI self test mode selection" (p10041[y])  
For xxxx = 10018 and yyyy = F-DI number:  
- Set "SI F-DI self test length dark pulses" (p10018) greater than zero.  
- Change p10041[y] "SI F-DI self test mode selection".  
For xxxx = 10041 and yyyy = F-DI number:  
- Change "SI F-DI self test mode selection" (p10041[y])  
For xxxx = 10071 and yyyy = F-DI number:  
- Correct "SI F-DI enable" (p10000).

### C01680 SI: Checksum error safety monitoring functions

**Valid as of version:**
  
06.01.122

**Message value:**
  
%1

**Message class:**
  
Safety monitoring channel has identified an error (10)

**Component:**
  
Control Unit (CU)

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The actual checksum over the safety-relevant parameters, calculated by the drive,
does not match the reference checksum last saved for the last machine acceptance test.  
Safety-relevant parameters have been changed or a fault is present.  
Note:  
This message results in an STO (Safe Torque Off).  
Message value (r60049, only for internal Siemens diagnostics)

**Remedy**
  
- Check the safety-relevant parameters and if required, correct.  
- Retentively save parameters.  
- Perform a POWER ON if safety parameters requiring a POWER ON have been modified.  
- Carry out an acceptance test.

### C01681 SI: Incorrect parameter value

**Valid as of version:**
  
06.01.122

**Message value:**
  
Parameter: %1, supplementary information: %2

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
None

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The parameter cannot be parameterized with this value.  
Note:  
This message results in an STO (Safe Torque Off).  
Message value (r60049, interpret decimal):  
yyyyxxxx dec: yyyy = supplementary information, xxxx = parameter  
yyyy = 0:  
No additional information available.  
xxxx = 9547:  
Parameter rule not complied with.  
xxxx = 9560:  
For SS1 ramp-monitored (p9606 = 2) or SS1E ramp-monitored (p9607 = 2), the parameter
must be greater than zero.  
xxxx = 9578:  
The acceleration limit (p9578) or possibly the monitoring cycle (p9500) is set too
low.  
xxxx = 9603:  
The control type displayed under additional information is not permissible for p9603
on this device.  
xxxx = 10006 or 10022 to 10036:  
An inadmissible signal source for the control via F-DI was set.  
xxxx = 10050:  
An inadmissible signal source for the F-DI via PROFIsafe was set. yyyy contains the
incorrect index of c10050[].

**Remedy**
  
Correct parameters:  
For xxxx = 9547:  
Set parameters p9546 and p9547 according to the following rule: p9546 * 0.75 >= p9547  
For xxxx = 9560:  
Set a parameter value greater than zero.  
For xxxx = 9578:  
Increase parameter p9578 or if required, p9500.  
The following rule must be satisfied: p9578 * 10 > p9790[1] and p9578 * 3 > p9790[0].  
For xxxx = 9603:  
In p9603, set a control type that is permissible for this device.  
For xxxx = 10006 or 10022 to 10036:  
Interconnect with a valid signal source.  
For xxxx = 10050 and yyyy = 0, 1 or 2:  
Interconnect c10050[yyyy] with a valid signal source or fixed value.

### C01682 SI: Monitoring function not supported

**Valid as of version:**
  
06.01.122

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
  
At least one of the monitoring functions enabled in p9604 is not supported with this
firmware version on this device.  
Note:  
The message value (r60049, interpret binary) indicates the bits of the monitoring
functions, which form this firmware version on this device, are not supported. If
several, non-supported monitoring functions are simultaneously enabled, then these
are all displayed in the message value.  
This message results in an STO (Safe Torque Off).  
See also: p9604 (SI enable)

**Remedy**
  
Correct parameter p9604 so that monitoring functions only permitted for this firmware
version and for this device are enabled.  
See also: p9612 (SI stop response for failure or control fault)

### C01690 SI: Data backup problem for the NVRAM

**Valid as of version:**
  
06.01.122

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
  
When saving parameters r9780, r9781 and r9782 (Safety logbook) says, an error has
occurred in conjunction with the NVRAM.  
Note:  
This fault does not result in a safety stop response.  
Fault value (r60049, interpret decimal):  
1: There is no physical NVRAM in the drive.  
2: There is no longer any free memory space in the NVRAM.

**Remedy**
  
For fault value = 1:  
- Replace the hardware.  
For fault value = 2:  
- De-select functions that are not required and that take up memory space in the NVRAM.  
- Contact Technical Support.  
Note:  
NVRAM: Non-Volatile Random Access Memory (non-volatile read and write memory)

### A01698 SI: Commissioning mode active

**Valid as of version:**
  
06.01.122

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
  
The commissioning of the "Safety Integrated" function is selected.  
This message is withdrawn after the safety functions have been commissioned.  
Note:  
- This message does not result in a safety stop response.  
- In the safety commissioning mode, function STO (Safe Torque Off) is internally selected.

**Remedy**
  
Not necessary.

### C01700 SI: STO (Safe Torque Off) initiated

**Valid as of version:**
  
06.01.122

**Message value:**
  
-

**Message class:**
  
Safety monitoring channel has identified an error (10)

**Component:**
  
None

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The drive is stopped using STO (Safe Torque Off).  
Possible causes:  
Subsequent response, following messages: C01706, C01714, C01715, C01716.

**Remedy**
  
Carry out diagnostics for the active messages (C01706, C01714, C01715, C01716).

### C01701 SI: SS1 (Safe Stop 1) initiated

**Valid as of version:**
  
06.01.122

**Message value:**
  
-

**Message class:**
  
Safety monitoring channel has identified an error (10)

**Component:**
  
None

**Response:**
  
 OFF3

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The drive is stopped using SS1 (Safe Stop 1) (braked along the OFF3 down ramp).  
As a result of this fault, after the time parameterized in p9556 has expired, or the
speed threshold parameterized in p9560 has been fallen below, STO (Safe Torque Off)
is initiated.  
Possible causes:  
Subsequent response, following messages: C01707, C01711, C01714, C01715, C01716.

**Remedy**
  
Perform diagnostics for active messages (C01707, C01711, C01714, C01715, C01716).

### C01702 SI: SS1E (Safe Stop 1 External) initiated

**Valid as of version:**
  
06.03.014

**Message value:**
  
-

**Message class:**
  
Safety monitoring channel has identified an error (10)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The drive is stopped via SS1E (braked from an external control system).  
As a result of this fault, after the time parameterized in p9594 has expired, or the
speed threshold parameterized in p9560 has been fallen below, then STO is initiated.  
Possible causes:  
Subsequent response, following messages: C01714, C01716

**Remedy**
  
Carry out diagnostics for the active messages (C01714, C01716).

### C01706 SI: SAM/SBR limit exceeded

**Valid as of version:**
  
06.01.122

**Message value:**
  
%1

**Message class:**
  
Safety monitoring channel has identified an error (10)

**Component:**
  
None

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The safety functions with parameterized motion monitoring SAM (Safe Acceleration Monitor)
/ SBR (Safe Brake Ramp) have identified an error.  
After initiating SS1 (Safe Stop 1), SS1E (Safe Stop 1 External), SS2 (Safe Stop 2)
or SS2E (Safe Stop 2 External), the speed has exceeded the set tolerance.  
The drive is shut down by message C01700 (STO (Safe Torque Off) initiated).  
  
Message value (r60049, interpret decimal):  
0: SAM for SS1/SS2 has detected a fault.  
1: SBR for SS1/SS2 has detected a fault.  
2: SAM for SS1E/SS2E has detected a fault.  
3: SBR for SS1E/SS2E has detected a fault.

**Remedy**
  
Check the braking behavior and, if necessary, adapt the parameterization of the SAM
or SBR monitoring.  
Without a POWER ON, this message can be acknowledged using a safe acknowledgment mechanism
(e.g. via PROFIsafe).  
See also: p9548 (SI SAM velocity tolerance), p9581 (SI SBR reference velocity for SS1 and SS2),
p9582 (SI SAM/SBR delay time for SS1 and SS2), p9583 (SI SBR reference time for SS1
and SS2)

### C01707 SI: Tolerance for safe operating stop exceeded

**Valid as of version:**
  
06.03.014

**Message value:**
  
-

**Message class:**
  
Safety monitoring channel has identified an error (10)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The actual position has distanced itself further from the target position than the
standstill tolerance.  
The drive is shut down by message C01701 "SI: SS1 initiated".

**Remedy**
  
- Check whether safety faults are present and if required carry out the appropriate
diagnostic routines for the particular faults.  
- Check whether the standstill tolerance matches the accuracy and control dynamic
performance of the axis.  
- Carry out a POWER ON.  
This message can be acknowledged without any POWER ON via PROFIsafe (safe acknowledgment).  
Note:  
SI: Safety Integrated  
SOS: Safe Operating Stop  
SS1: Safe Stop 1  
See also: p9530 (SI SOS standstill tolerance)

### C01708 SI: SS2 (Safe Stop 2) initiated

**Valid as of version:**
  
06.03.014

**Message value:**
  
-

**Message class:**
  
Safety monitoring channel has identified an error (10)

**Component:**
  
None

**Response:**
  
 STOP2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The drive is stopped using SS2 (braking along the OFF3 down ramp).  
SOS is activated after the parameterized time has expired.  
Possible causes:  
- Stop request from the higher-level control system.  
- Subsequent response messages: C01714, C01715, C01716  
See also: p9552 (SI transition time SS2 to SOS)

**Remedy**
  
- Remove the cause of the fault at the control system.  
- Carry out diagnostics for the active messages (C01714, C01715, C01716)  
This message can be acknowledged without any POWER ON via PROFIsafe (safe acknowledgment).  
Note:  
SI: Safety Integrated  
SOS: Safe Operating Stop  
SS2: Safe Stop 2

### C01709 SI: SS2E (Safe Stop2 External) initiated

**Valid as of version:**
  
06.03.014

**Message value:**
  
-

**Message class:**
  
Safety monitoring channel has identified an error (10)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The drive is stopped using SS2E (braking along a path).  
SOS is activated after the parameterized time has expired.  
Possible causes:  
- Stop request from the higher-level control system.  
- Subsequent response messages: C01714, C01715, C01716  
See also: p9553 (SI transition time SS2E to SOS)

**Remedy**
  
- Remove the cause of the fault at the control system.  
- Carry out diagnostics for the active messages (C01714, C01715, C01716)  
This message can be acknowledged without any POWER ON via PROFIsafe (safe acknowledgment).  
Note:  
SI: Safety Integrated  
SOS: Safe Operating Stop  
SS2E: Safe Stop 2 External (Safe Stop 2 with external stop)

### C01711 SI: SCF (Safety Channel Failure) initiated

**Valid as of version:**
  
06.01.122

**Message value:**
  
-

**Message class:**
  
Safety monitoring channel has identified an error (10)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The drive has detected an error in a safe monitoring function and has initiated SCF
(Safety Channel Failure).  
Monitoring functions are no longer reliable. Safe operation not possible.  
Possible causes:  
Subsequent response, following messages: C01648, C01750, C01751, C01753, C01754, C01769.  
  
Note:  
This fault results in an SS1 (Safe Stop 1) or SS1E (Safe Stop 1 with external stop)
depending on p9561, and as a consequence, after the time parameterized in p9556 has
expired, or the speed threshold parameterized in p9560 has been fallen below, STO
(Safe Torque Off) is initiated.  
See also: p9555 (SI transition time SCF to SS1/SS1E), p9561 (SI SCF stop response)

**Remedy**
  
Carry out diagnostics for the active messages (C01648, C01750, C01751, C01753, C01754,
C01769).

### C01714 SI: Safely-Limited Speed exceeded

**Valid as of version:**
  
06.01.122

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
  
The drive has moved faster than that specified by the velocity limit value (p9531).
The drive is stopped by the configured stop response (p9563).  
Message value (r60049, interpret decimal):  
100: SLS1 exceeded.  
200: SLS2 exceeded.  
300: SLS3 exceeded.  
400: SLS4 exceeded.

**Remedy**
  
- Check the traversing/motion program in the control.  
- Check the limits for SLS (Safely-Limited Speed) and if required adapt accordingly
(p9531).  
Without a POWER ON, this message can be acknowledged using a safe acknowledgment mechanism
(e.g. via PROFIsafe).  
See also: p9531 (SI SLS limit values), p9563 (SI SLS stop response)

### C01716 SI: Tolerance for Safe Direction exceeded

**Valid as of version:**
  
06.01.122

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
  
The tolerance for function SDI (Safe Direction) was exceeded. The drive is stopped
by the configured stop response (p9566).  
Message value (r60049, interpret decimal):  
0: Tolerance for function "SDI positive" exceeded.  
1: The tolerance for function "SDI negative" exceeded.

**Remedy**
  
- Check the traversing/motion program in the control.  
- Check the tolerance for function SDI and if required, adapt (p9564).  
Without a POWER ON, this message can be acknowledged using a safe acknowledgment mechanism
(e.g. via PROFIsafe).  
Prerequisite:  
- Deselect function SDI function and if required select again.  
See also: p9564 (SI SDI tolerance), p9565 (SI SDI delay time), p9566 (SI SDI stop response)

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
See also: p9578 (SI SLA acceleration limit), p9579 (SI SLA stop response)

### C01730 SI: Reference block for dynamic Safely-Limited Speed invalid

**Valid as of version:**
  
06.01.122

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
  
The reference block transferred via PROFIsafe is negative.  
A reference block is used to generate a referred velocity limit value based on the
reference quantity in p9531[0].  
The drive is stopped by the configured stop response (p9563[0]).  
Message value (r60049, interpret decimal):  
Requested, invalid reference block.

**Remedy**
  
In the PROFIsafe telegram, input data S_SLS_LIMIT_IST must be corrected.  
Without a POWER ON, this message can be acknowledged using a safe acknowledgment mechanism
(e.g. via PROFIsafe).

### C01750 SI: Hardware fault safety-related encoder

**Valid as of version:**
  
06.01.122

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Encoder 1

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The encoder that is used for the safety-relevant motion monitoring functions signals
a hardware fault.  
Note:  
This message results in  
- STO (Safe Torque Off) if p9516 bit 4 = 0  
- SCF (Safety Channel Failure) if p9516 bit 4 = 1  
Message value (r60049, interpret decimal):  
Encoder status word 1, encoder status word 2 that resulted in the message.

**Remedy**
  
- Check the encoder connection.  
- Replace encoder.  
Without a POWER ON, this message can be acknowledged using a safe acknowledgment mechanism
(e.g. via PROFIsafe).

### C01751 SI: Effectivity test error safety-related encoder

**Valid as of version:**
  
06.01.122

**Message value:**
  
%1

**Message class:**
  
Safety monitoring channel has identified an error (10)

**Component:**
  
Encoder 1

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The DRIVE-CLiQ encoder for safe motion monitoring signals an error for the internal
encoder effectivity tests; the safety software cyclically monitors the sequence.  
Note:  
This message results in an SCF (Safety Channel Failure).  
Message value (r60049, interpret decimal):  
Only for internal Siemens troubleshooting.

**Remedy**
  
- Check the encoder connection.  
- Replace encoder.  
Without a POWER ON, this message can be acknowledged using a safe acknowledgment mechanism
(e.g. via PROFIsafe).

### C01753 SI: Fault safety-relevant encoder

**Valid as of version:**
  
06.01.122

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
  
The encoder that is used for the safety-relevant motion monitoring functions signals
a fault.  
This message results in SCF (Safety Channel Failure).  
Message value (r60049, interpret decimal):  
1012: Plausibility violation of the encoder actual value.  
1021: Cyclic communication failure between the monitoring channel and Sensor Module.  
1022: Sign-of-life error for DRIVE-CLiQ encoders.  
1024: Sign-of-life error for HTL/TTL encoders.  
1031: Data transfer error between the monitoring channel and the Sensor Module (CRC
error).  
1033: Fault when checking offset between POS1 and POS2

**Remedy**
  
- Check the encoder connection.  
- Replace encoder.  
Without a POWER ON, this message can be acknowledged using a safe acknowledgment mechanism
(e.g. via PROFIsafe).  
For message value = 1021, 1024:  
- Check the communication link.  
- Set the monitoring clock cycle higher (p9500, p9511).  
- Carry out a POWER ON (switch off/switch on) for all components.  
- Replace the hardware.  
For message value = 1033:  
if one of the safety encoders was replaced:  
- Acknowledge hardware replacement.  
- Save all parameters (p0977 = 1 or retentively save).  
- Acknowledge fault.

### C01754 SI: Fault safety-relevant actual value acquisition

**Valid as of version:**
  
06.01.122

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
  
The actual value sensing for safe motion monitoring signals an error.  
Message value (r60049, interpret decimal):  
1039: Converting the position on the load side exceeds data format.

**Remedy**
  
For message value = 1039: Check the parameterization of the gearbox (p9520, p9521,
p9522).

### C01755 SI: Encoder limit frequency exceeded

**Valid as of version:**
  
06.01.122

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
  
Message value (r60049, interpret decimal):  
1: Motion monitoring functions with encoder: the actual velocity exceeds the encoder
limit frequency of 500 kHz.  
Note:  
This fault results in an SS1 (Safe Stop 1).

**Remedy**
  
Without a POWER ON, this message can be acknowledged using a safe acknowledgment mechanism
(e.g. via PROFIsafe).

### A01767 SI: Configuration imported from V5.2 has an error

**Valid as of version:**
  
06.03.014

**Message value:**
  
%1

**Message class:**
  
Safety monitoring channel has identified an error (10)

**Component:**
  
Control Unit (CU)

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
A project file is loaded that was created with FW Version V5.2. Several values were
automatically adapted when being imported.  
Alarm value (r2124, interpret binary):  
Bit 0 = 1:  
SS1 was activated in the imported project as SI Basic Function and also as SI Extended
Function, whereby different times were configured (p9652 != p9556).  
p9556 is used as new value for p9556 (SS1) and p9594 (SS1E).  
Bit 1 = 1:  
SS1E was activated in the imported project as SI Basic Function and also as SI Extended
Function, whereby different times were configured (p9652 != p9556). p9556 is used
as new value for p9556 (SS1) and p9594 (SS1E).  
Bit 2 = 1:  
SS1 was activated in the imported project as SI Basic Function and also as SI Extended
Function, SS1 (t) and SS1 (a, r) cannot be simultaneously selected.  
Parameter SI SS1 function specification is set as follows:  
p9606 = 1 (SS1_a), if p9506 is equal to 0 in the imported project.  
p9606 = 2 (SS1_r), if p9506 is equal to 0 in the imported project.  
Bit 3 = 1:  
The imported value of p9546 is greater than the maximum value of p9568 and p9584,
which is why p9568 and p9584 are limited to a value of 1000.

**Remedy**
  
Checking and adapting the modified parameter values.

### C01769 SI: Error for data cross-check

**Valid as of version:**
  
06.01.122

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
  
When carrying out a data cross-check between the two monitoring channels, the drive
detected a difference between parameters or results and initiated an SCF (Safety Channel
Failure). One of the monitoring functions no longer functions reliably, i.e. safe
operation is no longer possible.  
Safety message C01711 is also displayed as SCF (Safety Channel Failure) has been initiated.  
If at least one monitoring function is active, then after the parameterized timer
has expired, message C01701 is output.  
Message value (r60049, interpret hexadecimal): Only for internal Siemens fault diagnostics.

**Remedy**
  
- Carry out a POWER ON (switch-off/switch-on) for all components.  
- Re-commission the "Safety Integrated" function and carry out a POWER ON.  
- Upgrade firmware to later version.  
- Contact Technical Support.  
- Replace the hardware.

### C01770 SI: Fault of the failsafe inputs

**Valid as of version:**
  
06.01.122

**Message value:**
  
Fault cause: %1, F-DI number: %2

|  |  |  |  |
| --- | --- | --- | --- |
|  | Value | Cause | Remedy |
| For %1 | 1 | Discrepancy error (state between two monitoring channels different for too long) | Check the F-DI wiring |
| 2 | Too many switching operations | Reduce the switching frequency |  |
| 3 | Test pulse error | Check the F-DI wiring |  |
| 4 | Internal software error |  |  |

**Message class:**
  
Safety monitoring channel has identified an error (10)

**Component:**
  
Control Unit (CU)

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The failsafe digital inputs (F-DI) have a fault condition.  
Message value (r60049, interpret hexadecimal):  
yyyyxxxx hex  
xxxx: number of the failsafe digital input (F-DI).  
yyyy: fault cause  
  
Note:  
If several faults occur consecutively, then this message is only signaled for the
first fault that occurs.

**Remedy**
  
- Check the wiring of the F-DI (contact problems).  
- If the wiring is correct, and for example there is no wire breakage, then a check
must be made as to whether the switching frequency at F-DI is too high and must therefore
be reduced (switching pulses must have a longer time between them). The time interval
between each signal edge at an F-DI must be at least equal to the discrepancy time
before the input is switched again.  
Note:  
This message can be acknowledged via F-DI or PROFIsafe (safe acknowledgment).  
Discrepancy errors of an F-DI can only be acknowledged if safe acknowledgment was
carried out after the cause of the error was resolved (acknowledgment via PROFIsafe,
extended message acknowledgment, self acknowledgment). As long as safety acknowledgment
was not carried out, the corresponding F-DI stays in the safe state internally.  
A self acknowledgment for an F-DI can be realized using a positive edge at the corresponding
F-DI.  
Sets the discrepancy time for fast switching operations at the F-DIs:  
For fast switching operations at the failsafe digital inputs (F-DI), it may be necessary
to adapt the discrepancy time to the switching frequency:  
- The period of a cyclic switching pulse must be less than half of the discrepancy
time (if necessary, round down).  
- The time between two fast switching pulses should be longer than the discrepancy
time (if necessary, round up).  
- The discrepancy time must be at least p9500 (it must always be rounded up or down
to be an integer multiple of the SI monitoring clock cycle p9500).  
If an input filter has been parameterized (p10017 > 0), then the shortest possible
discrepancy time is directly specified by the input filter.  
- The period of a cyclic switching pulse must be less than half of the discrepancy
time p10017 (if necessary, round down).  
- The time between two fast switching pulses should be longer than the discrepancy
time+p10017 (if necessary, round up).  
- The discrepancy time must be at least p9500 The input filter must always be set
less than the discrepancy time.  
Self test with specified dark pulses (p10041 > 0) for long cable lengths:  
- Increase the dark pulse length (p10018 or p10019).  
- Increase the input filter (p10017).  
Note:  
F-DI: Failsafe Digital Input

### C01780 SBT When selected, the brake is closed

**Valid as of version:**
  
06.03.014

**Message value:**
  
Following brakes are closed: %1 bin

**Message class:**
  
Safety monitoring channel has identified an error (10)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
When selecting the brake test or starting the brake test, not all of the brakes were
open.  
Message value (r60049, interpret binary):  
Bit 0 = 1:  
The internal brake is closed.  
Note:  
The message appears with message value 0, if no brakes are configured in p10202.  
SBT: Safe Brake Test  
See also: p10202 (SI SBT brake selection)

**Remedy**
  
Open the brake and reselect the brake test.

## SINAMICS Alarms S210 01781 - 30027

SINAMICS Alarms S210 01781 - 30027

### C01781 SBT brake opening time exceeded

**Valid as of version:**
  
06.03.014

**Message value:**
  
Fault cause: %1 bin

**Message class:**
  
Safety monitoring channel has identified an error (10)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The maximum time (11 s) to open the brake during the brake test was exceeded.  
Possible causes:  
- During the brake test the drive went into a fault condition, and therefore the brake
was closed by the drive.  
Message value (r60049, interpret binary):  
Bit 0 = 1:  
Internal brake was not able to be opened.  
Note:  
SBT: Safe Brake Test

**Remedy**
  
- Carry out a safe acknowledgment.  
- Restart the brake test.  
See also: c10235 (SI Safety Control Channel control word S_STW3B)

### C01782 SBT brake test control error

**Valid as of version:**
  
06.03.014

**Message value:**
  
Fault cause: %1 bin

**Message class:**
  
Safety monitoring channel has identified an error (10)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The brake test was canceled as a result of incorrect control.  
Message value (r60049, interpret binary):  
Message value 0:  
The brake test was canceled as a result of a fault (brake opening time or brake closing
time exceeded).  
Bit 0:  
The safe brake test was canceled by resetting the brake test selection.  
Bit 1:  
The safe brake test was canceled by resetting the brake test start.  
Bit 2:  
The brake is not configured in configured p10202.  
There is a brake test configuration error.  
Note:  
SBT: Safe Brake Test  
See also: p10202 (SI SBT brake selection)

**Remedy**
  
- Check parameterization of the brake test (p10202).  
- Carry out a safe acknowledgment.  
- If required, restart the brake test.

### C01783 SBT brake closing time exceeded

**Valid as of version:**
  
06.03.014

**Message value:**
  
Fault cause: %1 bin

**Message class:**
  
Safety monitoring channel has identified an error (10)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The maximum time (11 s) to close the brake during the brake test was exceeded.  
Message value (r60049, interpret binary):  
Bit 0 = 1:  
Internal brake was not able to be closed.  
Note:  
SBT: Safe Brake Test

**Remedy**
  
- When using an internal brake with external feedback signal, check whether the feedback
signal is correctly interconnected with the extended brake control.  
- Carry out a safe acknowledgment.  
- Restart the brake test.

### C01784 SBT brake test canceled with fault

**Valid as of version:**
  
06.03.014

**Message value:**
  
Fault cause: %1

|  |  |  |  |
| --- | --- | --- | --- |
|  | Bit | Cause | Remedy |
| For %1 | 0 | Operation when selecting the brake test not enabled (r0899.2=0). | Enable operation when selecting the brake test |
| 1 | External fault occurred (e.g. the brake test that has already started is canceled by the user) | Do not cancel the brake test |  |
| 2 | A brake is closed when selecting the brake test. | Keep the brake open when selecting the brake test |  |
| 3 | A brake is closed when the determining the load torque | Keep the brake open when determining the load torque |  |
| 4 | Stop response fault occurred - or pulse enable was withdrawn | Do not withdraw pulse enable |  |
| 5 | Axis setpoint speed too high when selecting the brake test | Check setpoint speed |  |
| 6 | Actual speed (r0063) of the axis too high when selecting the brake test | Check the actual speed |  |
| 7 | Incorrect speed controller mode (e.g. encoderless speed control or U/f operation). | Set the correct mode for SBT |  |
| 8 | Closed-loop control has not been enabled or function generator is active. | Enable closed-loop control or deactivate function generator |  |
| 9 | Closed-loop control does not switch over to the brake test | Check closed-loop control |  |
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

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The safe brake test was canceled as a result of a fault.  
Message value (r60049, interpret binary):  
Bit 17 = 1: fault in the brake test sequence (cause, see bits 0 ... 10).  
Bit 20 = 1: the brake is not opened (p10202).  
Bit 21 = 1: axis position during the brake test not valid due to parking axis.  
Bit 22 = 1: internal software error.  
Bit 23 = 1: the permissible position range of the axis was violated with the brake
closed (p10212/p10222).  
Bit 24 = 1: the tested internal brake was opened while the brake test was active.  
Bit 26 = 1: during the active brake test, the test torque left its tolerance bandwidth
(20 %).  
Cause for message value bit 17:  
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
Bit 7 = 1: Incorrect speed controller mode (e.g. encoderless speed control or U/f
operation).  
Bit 8 = 1: closed-loop control not enabled or function generator active.  
Bit 9 = 1: control does not switch over to the brake test (e.g. because PI speed control
has not been parameterized).  
Bit 10 = 1: torque limit reached (r1407.7).  
Note:  
SBT: Safe Brake Test

**Remedy**
  
- Remove the fault cause.  
- Carry out a safe acknowledgment.  
- If required, restart the brake test.  
For bit 17 = 1 with bit 6 = 1 or bit 23 = 1:  
If the brake closing time of the motor holding brake (p1217) has been set too low,
then at the start of the brake test, the brake is closed too late. The brake closing
time should be adapted (p1217).

### C01785 SBT brake test configuration error

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
  
Error when parameterizing the brake test.  
In this configuration, the brake test cannot be started or cannot be started without
error.  
Message value (r60049, interpret decimal):  
4:  
No brake was configured (p10202).  
Note:  
SBT: Safe Brake Test

**Remedy**
  
Check parameterization of the brake test.

### C01793 SI: Internal safety message buffer is full

**Valid as of version:**
  
06.01.122

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
  
Too many safety messages have occurred within a short time so that some have not been
able to be displayed.

**Remedy**
  
No remedy required

### A01796 SI: Wait for communication

**Valid as of version:**
  
06.01.122

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
  
The drive waits for communication to be established to execute the safety-relevant
motion monitoring functions.  
Note:  
STO is active in this state.  
Alarm value (r2124, interpret decimal):  
3: Wait for communication to be established to PROFIsafe F-Host.

**Remedy**
  
If the message is not automatically withdrawn after a longer period of time, then
carry out the following checks:  
- Evaluate any other active PROFIsafe communication messages/signals.  
- Check the operating state of the F-Host.  
- Check the communication connection to the F Host.  
Note:  
STO: Safe Torque Off

### C01799 SI: Acceptance test mode active

**Valid as of version:**
  
06.01.122

**Message value:**
  
-

**Message class:**
  
Safety monitoring channel has identified an error (10)

**Component:**
  
Control Unit (CU)

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The acceptance test mode is active.  
This means the following:  
- the setpoint velocity limiting is deactivated (r9733).

**Remedy**
  
Not necessary.  
The message is withdrawn when exiting the acceptance test mode.

### F01800 DRIVE-CLiQ: Hardware/configuration error

**Valid as of version:**
  
06.01.122

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
  
A DRIVE-CLiQ connection fault has occurred.  
Fault value (r0949, interpret decimal):  
100 ... 107:  
Communication via DRIVE-CLiQ socket X100 ... X107 has not been switched to cyclic
operation. The cause may be an incorrect structure or a configuration that results
in an impossible bus timing.  
10:  
Loss of the DRIVE-CLiQ connection. The cause may be, for example, that the DRIVE-CLiQ
cable was withdrawn from the converter or as a result of a short-circuit for motors
with DRIVE-CLiQ. This fault can only be acknowledged in cyclic communication.  
11:  
Repeated faults when detecting the connection. This fault can only be acknowledged
in cyclic communication.  
12:  
A connection was detected but the node ID exchange mechanism does not function. The
reason is probably that the component is defective. This fault can only be acknowledged
in cyclic communication.

**Remedy**
  
For fault value = 100 ... 107:  
- Ensure that the DRIVE-CLiQ components have the same firmware versions.  
- Avoid longer topologies for short current controller sampling times.  
For fault value = 10:  
- Check the DRIVE-CLiQ cables at the converter.  
- Remove any short-circuit for motors with DRIVE-CLiQ.  
- Carry out a POWER ON.  
For fault value = 11:  
- Check the electrical cabinet design and cable routing for EMC compliance.  
For fault value = 12:  
- Replace the component involved.

### A01839 DRIVE-CLiQ diagnostics: cable fault to the component

**Valid as of version:**
  
06.01.122

**Message value:**
  
Component number: %1

**Message class:**
  
General drive fault (19)

**Component:**
  
Control Unit (CU)

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The fault counter to monitor the DRIVE-CLiQ connections/cables has been incremented.  
Alarm value (r2124, interpret decimal):  
Component number.  
Note:  
The component number specifies the component whose feeder cable from the direction
of the converter is faulted.  
The alarm is automatically withdrawn after 5 seconds, assuming that no other data
transfer error has occurred.

**Remedy**
  
- Check the corresponding DRIVE-CLiQ cables.  
- Check the electrical cabinet design and cable routing for EMC compliance.

### A01900 PN: Configuration telegram error

**Valid as of version:**
  
06.01.122

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
253:  
PN Shared Device: Illegal mixed configuration of PROFIsafe and PZD.  
254:  
PN Shared Device: Illegal double assignment of a slot/subslot.  
257:  
PN Shared Device: Too many PZD data words for the output or input in the overall device.  
501:  
PROFIsafe parameter error (e.g. F_Source_Add, F_Dest_Add).  
502:  
PROFIsafe telegram does not match.  
Additional values:  
Only for internal Siemens troubleshooting.

**Remedy**
  
Check the bus configuration on the controller and device sides.

### A01902 PN: Isochronous operation parameterization not permissible

**Valid as of version:**
  
06.01.122

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
  
06.01.122

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
  
06.01.122

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
  
06.01.122

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
  
06.01.122

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
  
06.01.122

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
  
06.01.122

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

### A01940 PN: Clock cycle synchronism not reached

**Valid as of version:**
  
06.01.122

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
- The controller does not send an isochronous global control telegram, although isochronous
operation was selected when configuring the bus.  
- The controller uses another isochronous DP cycle than was transferred to the device
in the parameterizing telegram.  
- At least one drive object has a pulse enable (also not controlled from PROFINET).

**Remedy**
  
- Check the controller application and bus configuration.  
- Check the consistency between the clock cycle input when configuring the device
and clock cycle setting at the controller.  
- Check that no drive object has a pulse enable. Only enable the pulses after synchronizing
the PROFINET drives.  
Note:  
PN: PROFINET

### A01941 PN: Clock cycle signal missing when the bus is being established

**Valid as of version:**
  
06.01.122

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
  
06.01.122

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
  
06.01.122

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
  
06.01.122

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
  
06.01.122

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
  
06.01.122

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
  
06.01.122

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

### F03001 NVRAM checksum incorrect

**Valid as of version:**
  
06.01.122

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

### F03590 TM: Module not ready

**Valid as of version:**
  
06.03.014

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

### F06310 Supply voltage (p0210) incorrectly parameterized

**Valid as of version:**
  
06.01.122

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
  
06.01.122

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
  
06.01.122

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
See also: r0034 (Motor utilization thermal), p0613 (Motor temperature model ambient temperature)

**Remedy**
  
- Check the motor load and if required, reduce.  
- Check the motor ambient temperature.  
- Check activation of the additional motor overload protection (p5375).  
See also: r0034 (Motor utilization thermal)

### F07085 Drive: Open-loop/closed-loop control parameters changed

**Valid as of version:**
  
06.01.122

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

### F07090 Drive: Upper torque limit less than the lower torque limit

**Valid as of version:**
  
06.01.122

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
  
06.01.122

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
  
06.01.122

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
  
06.01.122

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
See also: p5308 (One Button Tuning distance limiting), p5309 (One Button Tuning duration)

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
  
06.01.122

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
  
06.01.122

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
See also: p5300 (One Button Tuning selection)

**Remedy**
  
Not necessary.  
The alarm is automatically withdrawn after One Button Tuning has been exited (p5300
= 0).

### F07097 Drive: Test signal error distance limiting

**Valid as of version:**
  
06.01.122

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
See also: p5308 (One Button Tuning distance limiting), p5309 (One Button Tuning duration)

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
  
06.01.122

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
  
06.01.122

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

### F07410 Drive: Current controller output limited

**Valid as of version:**
  
06.01.122

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
  
06.01.122

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

### F07420 Drive: Current setpoint filter natural frequency > Shannon frequency

**Valid as of version:**
  
06.03.014

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
  
06.03.014

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
  
06.03.014

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
  
06.01.122

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
See also: r0316 (Motor torque constant), p1082 (Maximum speed)

### F07434 Drive: It is not possible to change the direction of rotation with the pulses enabled

**Valid as of version:**
  
06.01.122

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

### A07441 LR: Save the position offset of the absolute encoder adjustment

**Valid as of version:**
  
06.01.122

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

### A07520 Drive: Motor cannot be changed over

**Valid as of version:**
  
06.03.014

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
  
06.03.014

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

### A07565 Drive: Encoder error in PROFIdrive encoder interface 1

**Valid as of version:**
  
06.01.122

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

### A07566 Drive: Encoder error in PROFIdrive encoder interface 2

**Valid as of version:**
  
06.03.014

**Message value:**
  
%1

**Message class:**
  
Position/speed actual value incorrect or not available (11)

**Component:**
  
Sensor Module Encoder 2

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
An encoder error was signaled for encoder 2 via the PROFIdrive encoder interface (G2_ZSW.15).  
Alarm value (r2124, interpret decimal):  
Error code from G2_XIST2.

**Remedy**
  
Acknowledge the encoder error using the encoder control word (G2_STW.15 = 1).

### A07569 Enc identification active

**Valid as of version:**
  
06.03.014

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
  
06.01.122

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

### A07581 Motor encoder: Position actual value preprocessing error

**Valid as of version:**
  
06.01.122

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

### A07582 Encoder 2: Position actual value preprocessing error

**Valid as of version:**
  
06.01.122

**Message value:**
  
-

**Message class:**
  
Position/speed actual value incorrect or not available (11)

**Component:**
  
Encoder 2

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
  
06.01.122

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
See also: p0187 (Motor encoder encoder data set number), p0188 (Encoder 2 encoder data set number),
p0400 (Encoder type selection), p2502 (LR encoder assignment)

### A07588 Encoder 2: Position actual value preprocessing does not have a valid encoder

**Valid as of version:**
  
06.01.122

**Message value:**
  
-

**Message class:**
  
Error in the parameterization / configuration / commissioning procedure (18)

**Component:**
  
Encoder 2

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
See also: p0187 (Motor encoder encoder data set number), p0188 (Encoder 2 encoder data set number),
p0400 (Encoder type selection), p2502 (LR encoder assignment)

### A07593 Motor encoder: Value range for position actual value exceeded

**Valid as of version:**
  
06.03.014

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

### A07594 Encoder 2: Value range for position actual value exceeded

**Valid as of version:**
  
06.03.014

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
2: The encoder position actual value Gn_XIST2 (r0483) or the absolute value after
the load gearbox (r2723) has exceeded the value range.  
3: The maximum encoder value times the factor to convert the absolute position (r0483
and/or r2723) from increments to length units (LU) has exceeded the value range for
displaying the position actual value.

**Remedy**
  
If required, reduce the traversing range or position resolution.  
For alarm value = 3:  
Reducing the position resolution and conversion factor:  
- Reduce the length unit (LU) per load revolution for rotary encoders (p2506).  
- Increase the fine resolution of absolute position actual values (p0419).

### A07596 Motor encoder: Homing function interrupted

**Valid as of version:**
  
06.03.014

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

### A07597 Encoder 2: Homing function interrupted

**Valid as of version:**
  
06.03.014

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
- Homing mark search and measuring probe evaluation simultaneously activated (c2508
and c2509 = 1 signal).  
- Activated homing function (homing mark search or measuring probe evaluation) was
deactivated (c2508 and c2509 = 0 signal).

**Remedy**
  
- Check the causes and resolve.  
- Reset the control (c2508 and c2509 = 0 signal) and activate the required function.

### F07801 Drive: Motor overcurrent

**Valid as of version:**
  
06.01.122

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
  
06.01.122

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

### F07815 Drive: Power unit has been changed

**Valid as of version:**
  
06.01.122

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

### F07860 External braking resistor signals an overtemperature

**Valid as of version:**
  
06.01.122

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
  
The temperature monitoring of the external braking resistor, connected via digital
input 4 (DI 4, X130/2.6), responded.  
Note:  
This signal is triggered for a 1/0 edge at digital input 4.

**Remedy**
  
- Check the dimensioning of the external braking resistor for the application.  
- Check the external braking resistor and temperature monitoring.  
- Check the temperature monitoring connection (X130/2.6).

### F07900 Drive: Motor blocked/speed controller at its limit

**Valid as of version:**
  
06.01.122

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
See also: p2175 (Motor blocked speed threshold)

**Remedy**
  
- Check that the motor can freely move.  
- Check the effective torque limit (r1538, r1539).  
- Check the parameter of the "Motor blocked" signal and possibly correct (p2175).

### F07901 Drive: Motor overspeed

**Valid as of version:**
  
06.01.122

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

### F07930 Drive: Brake control error

**Valid as of version:**
  
06.01.122

**Message value:**
  
%1

**Message class:**
  
Application/technological function faulted (17)

**Component:**
  
Motor

**Response:**
  
 OFF1

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The converter has detected a brake control fault.  
Fault value (r0949, interpret decimal):  
1, 2:  
- Motor cable shield is not correctly connected.  
- Defect in the brake control circuit of the converter.  
- Ground fault in brake cable.  
4:  
Brake is not connected or cable is interrupted.  
See also: p1278 (Brake control diagnostics evaluation)

**Remedy**
  
- Check the motor holding brake connection.  
- Check the function of the motor holding brake.  
- Check whether there is a DRIVE-CLiQ communication error, and if required, carry
out a diagnostics routine for the faults involved.  
- Check that the electrical cabinet design and cable routing are in compliance with
EMC regulations (e.g. shield of the motor cable and brake conductors are connected
with the shield connecting plate and the motor connectors are tightly screwed to the
housing).  
- Set p1278 to 1 if brake diagnostics is not required.  
- Replace the converter.  
See also: p1215 (Motor holding brake configuration), p1278 (Brake control diagnostics evaluation)

### F07933 Drive: Brake voltage incorrect

**Valid as of version:**
  
06.01.122

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
  
A brake voltage fault was detected.

**Remedy**
  
- Carry out a POWER ON (switch-off/switch-on) for all components.  
- Contact Technical Support.  
- Replace the converter.

### F07935 Drive: Incorrect motor holding brake configuration

**Valid as of version:**
  
06.01.122

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
  
An incorrect motor holding brake configuration was detected.  
Fault value (r0949, interpret decimal):  
0:  
A motor holding brake was detected where the brake control has not been configured
(p1215 = 0).  
1:  
A motor holding brake was detected where the brake control has not been configured
(p1215 = 0).  
The brake control configuration was left at "No motor holding brake available" (p1215
= 0).

**Remedy**
  
For fault value = 0:  
- No remedy required.  
For fault value = 1:  
- If required change the motor holding brake configuration (p1215 = 1, 2).  
- If this fault value unexpectedly occurs, then the motor connections should be checked
in order to rule out that they have been interchanged.  
See also: p1215 (Motor holding brake configuration)

### F07955 Drive: Motor has been changed

**Valid as of version:**
  
06.01.122

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
  
The code number of the actual motor with DRIVE-CLiQ does not match the saved number.  
If available:  
The code numbers of the bearings, gearbox and brake do not match the saved numbers.

**Remedy**
  
Connect the original motor and switch on the converter again (POWER ON) - or restore
the factory settings.  
Note:  
The data for bearings, gearbox and brake are reloaded.

### A08561 IE: Consistency error affecting adjustable parameters

**Valid as of version:**
  
06.01.122

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

### A08563 PROFINET: Consistency error affecting adjustable parameters

**Valid as of version:**
  
06.01.122

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
  
06.03.014

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
  
06.03.014

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
  
06.01.122

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
See also: r5600 (PROFIenergy energy-saving mode ID)

**Remedy**
  
The alarm is automatically withdrawn when the energy-saving mode is exited.  
Note:  
The energy-saving mode is exited after the following events:  
- The PROFIenergy command end_pause is received from the higher-level control.  
- The higher-level control has changed into the STOP operating state.  
- The PROFINET connection to the higher-level control has been disconnected.

### F13000 License not adequate

**Valid as of version:**
  
06.01.122

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
  
06.01.122

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
  
06.01.122

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
  
06.01.122

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
  
06.01.122

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
  
06.01.122

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
  
06.01.122

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
  
06.01.122

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

### F30003 Drive: DC link undervoltage

**Valid as of version:**
  
06.01.122

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

**Remedy**
  
- Check the line voltage.  
- Check the line infeed and observe the fault messages relating to it (if there are
any).  
- Check the line phases.  
- Check the supply voltage setting (p0210).  
See also: p0210 (Device supply voltage)

### F30004 Power unit: Overtemperature heat sink inverter

**Valid as of version:**
  
06.01.122

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
  
06.01.122

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
  
The power unit was overloaded.  
- The permissible rated power unit current was exceeded for an inadmissibly long time.  
- The permissible load duty cycle was not maintained.  
Fault value (r0949, interpret decimal):  
I2t [100 % = 16384].

**Remedy**
  
- Reduce the continuous load.  
- Adapt the load duty cycle.  
- Check the rated currents of the motor and power unit.  
See also: r0307 (Rated motor power)

### F30011 Power unit: Line phase failure in main circuit

**Valid as of version:**
  
06.01.122

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
  
06.03.014

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
  
06.03.014

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

### F30015 Drive: phase failure motor cable

**Valid as of version:**
  
06.01.122

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
The motor is correctly connected, however the closed-speed control is instable and
therefore an oscillating torque is generated.

**Remedy**
  
- Check the motor feeder cables.  
- Check the speed controller settings.

### A30016 Power unit: Load supply switched off

**Valid as of version:**
  
06.01.122

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
- If necessary, insert the jumper for the internal braking resistor.  
- For a 3 AC line connection, connect an internal or external braking resistor (X4).

### F30017 Power unit: Hardware current limit has responded too often

**Valid as of version:**
  
06.01.122

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
  
06.01.122

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
  
06.01.122

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

### F30024 Power unit: Overtemperature thermal model

**Valid as of version:**
  
06.01.122

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
See also: r0037 (Drive temperatures)

**Remedy**
  
- Adapt the load duty cycle.  
- Check whether the fan is running.  
- Check the fan elements.  
- Check whether the ambient temperature is in the permissible range.  
- Check the motor load.  
- Reduce the pulse frequency if this is higher than the rated pulse frequency.

### F30025 Power unit: Chip overtemperature

**Valid as of version:**
  
06.01.122

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
See also: r0037 (Drive temperatures)

### F30027 Power unit: Precharging DC link time monitoring

**Valid as of version:**
  
06.01.122

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
Possible causes:  
1) There is no line voltage connected.  
2) The line contactor/line side switch has not been closed.  
3) The line voltage is too low.  
4) Line voltage incorrectly set (p0210).  
5) The precharging resistors are overheated as there were too many precharging operations
per time unit.  
6) The precharging resistors are overheated as the DC link capacitance is too high.  
7) The precharging resistors have overheated as power was drawn from the DC link without
the infeed being ready for operation.  
8) The precharging resistors are overheated as the line contactor was closed during
the DC link fast discharge through the Braking Module.  
9) The DC link has either a ground fault or a short-circuit.  
10) Connector X4 is not correctly configured.  
  
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
See also: p0210 (Device supply voltage)

**Remedy**
  
In general:  
- Check the line voltage at the input terminals.  
- Check the line voltage setting (p0210).  
For 5):  
- Carefully observe the permissible precharging frequency (refer to the product documentation).  
For 6):  
- Check the total capacitance of the DC link and reduce in accordance with the maximum
permissible DC link capacitance if necessary (refer to the product documentation).  
For 7):  
- Interconnect the ready-for-operation signal from the infeed unit in the enable logic
of the drives connected to this DC link.  
For 8):  
- Check the connections of the external line contactor. The line contactor must be
open during DC link fast discharge.  
For 9):  
- Check the DC link for ground faults or short-circuits.  
For 10):  
- When using the internal braking resistor, terminals DCP and R2 of connector X4 must
be bridged.  
- When using an external braking resistor, this must be connected between DCP and
R1 of connector X4.  
See also: p0210 (Device supply voltage)

## SINAMICS Alarms S210 30031 - 36211

SINAMICS Alarms S210 30031 - 36211

### A30031 Power unit: Hardware current limiting in phase U

**Valid as of version:**
  
06.01.122

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
  
06.03.014

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
  
06.03.014

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
  
06.01.122

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
  
06.01.122

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

### F30040 Drive: 24/48 V undervoltage

**Valid as of version:**
  
06.01.122

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
  
The undervoltage threshold of the 24 V power supply for the drive was fallen below
for longer than 3 ms.  
Fault value (r0949, interpret hexadecimal):  
yyxxxx hex: yy = channel, xxxx = voltage [0.1 V]  
yy = 0: 24 V power supply  
yy = 1: 48 V power supply

**Remedy**
  
- Check the drive power supply.  
- Carry out a POWER ON (switch-off/switch-on).

### A30041 Power unit: Undervolt 24/48 V alarm

**Valid as of version:**
  
06.01.122

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
  
06.01.122

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
See also: p0251 (Power unit heat sink fan operating hours counter), r0277 (Power unit heat sink
fan wear counter)

### F30043 Power unit: Overvolt 24/48 V

**Valid as of version:**
  
06.01.122

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
  
06.01.122

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

### A30048 Power unit: fan defective

**Valid as of version:**
  
06.03.014

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
  
06.01.122

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
  
06.01.122

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
  
06.01.122

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

### F30055 Power unit: Braking chopper overcurrent

**Valid as of version:**
  
06.01.122

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
  
06.03.014

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

### F30062 Bypass contactor opened under current

**Valid as of version:**
  
06.01.122

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
  
06.01.122

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
  
06.01.122

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
  
06.01.122

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
  
06.01.122

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
  
06.03.014

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

### A30250 Power unit: Overtemperature heat sink inverter

**Valid as of version:**
  
06.01.122

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

### A30252 Power unit: Chip overtemperature alarm

**Valid as of version:**
  
06.01.122

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
  
06.01.122

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
  
06.01.122

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

**Remedy**
  
- Reduce the continuous load.  
- Adapt the load duty cycle.  
- Check the rated currents of the motor and power unit.

### A30257 Power unit: Overload I2t (DC)

**Valid as of version:**
  
06.03.014

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

**Remedy**
  
- Reduce the continuous load.  
- Adapt the load duty cycle.

### F30258 Power unit: Overload I2t (DC)

**Valid as of version:**
  
06.03.014

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

**Remedy**
  
- Reduce the continuous load.  
- Adapt the load duty cycle.  
See also: r0307 (Rated motor power)

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
  
06.01.122

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
  
06.01.122

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
  
06.01.122

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
  
06.03.014

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
  
06.01.122

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
- To increase the degree of ruggedness, the delay time can be increased.

### A30266 Power unit: Required modulator setting cannot be implemented

**Valid as of version:**
  
06.03.014

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
  
06.03.014

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

**Remedy**
  
- Reduce the continuous load.  
- Adapt the load duty cycle.

### F30268 Power unit: Active power overload

**Valid as of version:**
  
06.03.014

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

**Remedy**
  
- Reduce the continuous load.  
- Adapt the load duty cycle.  
See also: r0307 (Rated motor power)

### A30502 Power unit: DC link overvoltage

**Valid as of version:**
  
06.01.122

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

### C30603 SI: Module temperature - limit value exceeded

**Valid as of version:**
  
06.01.122

**Message value:**
  
-

**Message class:**
  
Safety monitoring channel has identified an error (10)

**Component:**
  
None

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
A safe monitoring function has detected that the module temperature has exceeded a
limit value. STO (Safe Torque Off) was initiated to maintain the safe state.

**Remedy**
  
- Check the ambient temperature.  
- Check the module fan.  
- Operate the module in the permissible range.

### F30604 SI: Safety EEPROM data error

**Valid as of version:**
  
06.01.122

**Message value:**
  
%1

**Message class:**
  
Safety monitoring channel has identified an error (10)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
POWER ON

**Cause**
  
Safety relevant EEPROM data are not correct.  
This message results in an STO (Safe Torque Off).  
  
Message value (r60049, interpret decimal): Only for internal Siemens fault diagnostics.

**Remedy**
  
Replace the module

### A30605 SI: Checksum error has occurred

**Valid as of version:**
  
06.01.122

**Message value:**
  
%1

**Message class:**
  
Safety monitoring channel has identified an error (10)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
A checksum error (CRC error) has occurred in the converter program memory.

**Remedy**
  
- Carry out a POWER ON (switch-off/switch-on).  
- Upgrade firmware to later version.  
- Contact Technical Support.

### C30649 SI: Internal software error

**Valid as of version:**
  
06.01.122

**Message value:**
  
Module: %1, line: %2

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Power Unit

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
An internal error has occurred in the Safety Integrated software.  
Note:  
This message results in an STO (Safe Torque Off) that cannot be acknowledged.  
Message value (r60049, interpret hexadecimal):  
Only for internal Siemens troubleshooting.

**Remedy**
  
- Carry out a POWER ON (switch-off/switch-on) for all components.  
- Re-commission the "Safety Integrated" function and carry out a POWER ON.  
- Upgrade firmware to later version.  
- Contact Technical Support.  
- Replace hardware component.

### C30667 SI: Project data imported from V5.2 has an error

**Valid as of version:**
  
06.03.014

**Message value:**
  
%1

**Message class:**
  
Safety monitoring channel has identified an error (10)

**Component:**
  
Control Unit (CU)

**Response:**
  
 OFF2

**Acknowledgment:**
  
POWER ON

**Cause**
  
A project file is loaded that was created with FW Version V5.2. The download was not
able to be completely executed.  
Fault value (r0949, interpret binary):  
Bit 0 = 1:  
A project file is corrupt. There is a difference between the actual checksums and
reference CRC checksums.  
Bit 1 = 1:  
p9523 < p9525, p9523 must be set >= p9525 in order to correctly convert p9676 (SI
identifier encoder properties).  
Bit 2 = 1:  
p9523 < p9524, p9523 must be set >= p9524 in order to correctly convert p9630 (SI
safe maximum speed encoder (rotary)).  
Bit 3 = 1:  
p9523 < (p9524 + p9525), p9523 must be set >= (p9524 + p9525) in order to correctly
convert p9631 (SI safe position accuracy encoder (rotary))  
Bit 4 = 1:  
In the project, p9518 was set to 0, which means that p9630 and p9631 are not correctly
converted.

**Remedy**
  
For bit 0:  
Save the project file in firmware version V5.2 again and load into the current firmware.  
For bits 1 ... 4:  
Resolve the error in firmware version V5.2, save the project again and load into the
current firmware.

### A30767 SI: Configuration imported from V5.2 has an error

**Valid as of version:**
  
06.03.014

**Message value:**
  
%1

**Message class:**
  
Safety monitoring channel has identified an error (10)

**Component:**
  
Control Unit (CU)

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
A project file is loaded that was created with FW Version V5.2. Several values were
automatically adapted when being imported.  
Alarm value (r2124, interpret binary):  
Bit 0 = 1:  
SS1 was activated in the imported project as SI Basic Function and also as SI Extended
Function, whereby different times were configured (p9652 != p9556).  
p9556 is used as new value for p9556 (SS1) and p9594 (SS1E).  
Bit 1 = 1:  
SS1E was activated in the imported project as SI Basic Function and also as SI Extended
Function, whereby different times were configured (p9652 != p9556). p9556 is used
as new value for p9556 (SS1) and p9594 (SS1E).  
Bit 2 = 1:  
SS1 was activated in the imported project as SI Basic Function and also as SI Extended
Function, SS1 (t) and SS1 (a, r) cannot be simultaneously selected.  
Parameter SI SS1 function specification is set as follows:  
p9606 = 1 (SS1_a), if p9506 is equal to 0 in the imported project.  
p9606 = 2 (SS1_r), if p9506 is equal to 0 in the imported project.  
Bit 3 = 1:  
The imported value of p9546 is greater than the maximum value of p9568 and p9584,
which is why p9568 and p9584 are limited to a value of 1000.

**Remedy**
  
Checking and adapting the modified parameter values.

### N30800 Power unit: Group signal

**Valid as of version:**
  
06.01.122

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

### F30805 Power unit: EEPROM checksum error

**Valid as of version:**
  
06.01.122

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

### F30810 Power unit: Watchdog timer expired

**Valid as of version:**
  
06.01.122

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
  
06.01.122

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

### F30850 Power unit: Internal software error

**Valid as of version:**
  
06.03.014

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

### A30853 Power unit: Sign-of-life error cyclic data

**Valid as of version:**
  
06.01.122

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

### F30860 Power unit DRIVE-CLiQ (CU): Telegram error

**Valid as of version:**
  
06.01.122

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
  
There is an internal communication error in the power unit.  
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
Failure of the supply voltage.  
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

### F30895 Power unit DRIVE-CLiQ: Alternating cyclic data transfer error

**Valid as of version:**
  
06.01.122

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
  
There is a DRIVE-CLiQ communication error from the power unit involved to the converter.  
Error cause:  
11 (= 0B hex):  
Synchronization error during alternating cyclic data transfer.  
Note regarding the message value:  
The individual information is coded as follows in the message value (r0949/r2124):  
0000yyxx hex:  
yy = component number,  
xx = fault cause

**Remedy**
  
Carry out a POWER ON (switch-off/switch-on).

### F30899 Power unit: Unknown fault

**Valid as of version:**
  
06.01.122

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

### F30950 Power unit: Internal software error

**Valid as of version:**
  
06.01.122

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
  
06.01.122

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

### F31120 Motor encoder: Encoder power supply fault

**Valid as of version:**
  
06.01.122

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
  
An encoder power supply fault was detected.  
Fault value (r0949, interpret binary):  
Bit 0: Undervoltage condition on the sense line.  
Bit 1: Overcurrent condition for the encoder power supply.  
Bit 2: Overcurrent condition for encoder power supply on cable resolver excitation
negative.  
Bit 3: Overcurrent condition for encoder power supply on cable resolver excitation
positive.  
Bit 4: The 24 V power supply via the inverter is overloaded.  
Bit 5: Overcurrent at the EnDat connection of the converter.  
Bit 6: Overvoltage at the EnDat connection of the converter.  
Bit 7: Hardware fault at the EnDat connection of the converter.  
Note:  
If the encoder cables 6FX2002-2EQ00-.... and 6FX2002-2CH00-.... are interchanged,
this can result in the encoder being destroyed because the pins of the operating voltage
are reversed.

**Remedy**
  
For fault value, bit 0 = 1:  
- Correct encoder cable connected?  
- Check the plug connections of the encoder cable.  
- SMC30: Check the parameterization (p0404.22).  
For fault value, bit 1 = 1:  
- Correct encoder cable connected?  
- Replace the encoder or encoder cable.  
For fault value, bit 2 = 1:  
- Correct encoder cable connected?  
- Replace the encoder or encoder cable.  
For fault value, bit 3 = 1:  
- Correct encoder cable connected?  
- Replace the encoder or encoder cable.  
For fault value, bit 5 = 1:  
- Measuring unit correctly connected at the converter?  
- Replace the measuring unit or the cable to the measuring unit.  
For fault value, bit 6, 7 = 1:  
- Replace the defective EnDat 2.2 converter.

### F31135 Motor encoder: Fault when determining the position (singleturn)

**Valid as of version:**
  
06.01.122

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
Bit 6: Reserved (undervoltage)/hardware fault EnDat supply (--> F3x110, x = 1, 2,
3).  
Bit 7: Reserved (overcurrent)/EnDat encoder withdrawn when not in the parked state
(--> F3x110, x = 1, 2, 3).  
Bit 8: Reserved (battery)/overcurrent EnDat supply (--> F3x110, x = 1, 2, 3).  
Bit 9: Reserved/overvoltage EnDat supply (--> F3x110, x = 1, 2, 3).  
Bit 11: Reserved/internal communication error (--> F3x110, x = 1, 2, 3).  
Bit 12: Reserved/internal communication error (--> F3x110, x = 1, 2, 3).  
Bit 13: Reserved/internal communication error (--> F3x110, x = 1, 2, 3).  
Bit 14: Reserved/internal communication error (--> F3x110, x = 1, 2, 3).  
Bit 15: Internal communication error (--> F3x110, x = 1, 2, 3).  
Bit 16: Lighting (--> F3x135, x = 1, 2, 3).  
Bit 17: Signal amplitude (--> F3x135, x = 1, 2, 3).  
Bit 18: Singleturn position 1 (--> F3x135, x = 1, 2, 3).  
Bit 19: Overvoltage (--> F3x135, x = 1, 2, 3).  
Bit 20: Undervoltage (--> F3x135, x = 1, 2, 3).  
Bit 21: Overcurrent (--> F3x135, x = 1, 2, 3).  
Bit 22: Temperature exceeded (--> F3x405, x = 1, 2, 3).  
Bit 23: Singleturn position 2 (safety status display).  
Bit 24: Singleturn system (--> F3x135, x = 1, 2, 3).  
Bit 25: Singleturn power down (--> F3x135, x = 1, 2, 3)  
Bit 26: Multiturn position 1 (--> F3x136, x = 1, 2, 3).  
Bit 27: Multiturn position 2 (--> F3x136, x = 1, 2, 3).  
Bit 28: Multiturn system (--> F3x136, x = 1, 2, 3).  
Bit 29: Multiturn power down (--> F3x136, x = 1, 2, 3).  
Bit 30: Multiturn overflow/underflow (--> F3x136, x = 1, 2, 3).  
Bit 31: Multiturn battery (reserved).

**Remedy**
  
- Determine the detailed cause of the fault using the fault value.  
- Replace the encoder if necessary.  
Note:  
An EnDat 2.2 encoder may only be removed and inserted in the "Park" state.  
If an EnDat 2.2 encoder was removed when not in the "Park" state, then after inserting
the encoder, a POWER ON (switch-off/switch-on) is necessary to acknowledge the fault.

### F31136 Motor encoder: Fault when determining the position (multiturn)

**Valid as of version:**
  
06.01.122

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
Bit 6: Reserved (undervoltage)/hardware fault EnDat supply (--> F3x110, x = 1, 2,
3).  
Bit 7: Reserved (overcurrent)/EnDat encoder withdrawn when not in the parked state
(--> F3x110, x = 1, 2, 3).  
Bit 8: Reserved (battery)/overcurrent EnDat supply (--> F3x110, x = 1, 2, 3).  
Bit 9: Reserved/overvoltage EnDat supply (--> F3x110, x = 1, 2, 3).  
Bit 11: Reserved/internal communication error (--> F3x110, x = 1, 2, 3).  
Bit 12: Reserved/internal communication error (--> F3x110, x = 1, 2, 3).  
Bit 13: Reserved/internal communication error (--> F3x110, x = 1, 2, 3).  
Bit 14: Reserved/internal communication error (--> F3x110, x = 1, 2, 3).  
Bit 15: Internal communication error (--> F3x110, x = 1, 2, 3).  
Bit 16: Lighting (--> F3x135, x = 1, 2, 3).  
Bit 17: Signal amplitude (--> F3x135, x = 1, 2, 3).  
Bit 18: Singleturn position 1 (--> F3x135, x = 1, 2, 3).  
Bit 19: Overvoltage (--> F3x135, x = 1, 2, 3).  
Bit 20: Undervoltage (--> F3x135, x = 1, 2, 3).  
Bit 21: Overcurrent (--> F3x135, x = 1, 2, 3).  
Bit 22: Temperature exceeded (--> F3x405, x = 1, 2, 3).  
Bit 23: Singleturn position 2 (safety status display).  
Bit 24: Singleturn system (--> F3x135, x = 1, 2, 3).  
Bit 25: Singleturn power down (--> F3x135, x = 1, 2, 3)  
Bit 26: Multiturn position 1 (--> F3x136, x = 1, 2, 3).  
Bit 27: Multiturn position 2 (--> F3x136, x = 1, 2, 3).  
Bit 28: Multiturn system (--> F3x136, x = 1, 2, 3).  
Bit 29: Multiturn power down (--> F3x136, x = 1, 2, 3).  
Bit 30: Multiturn overflow/underflow (--> F3x136, x = 1, 2, 3).  
Bit 31: Multiturn battery (reserved).

**Remedy**
  
- Determine the detailed cause of the fault using the fault value.  
- Replace the encoder if necessary.  
Note:  
An EnDat 2.2 encoder may only be removed and inserted in the "Park" state.  
If an EnDat 2.2 encoder was removed when not in the "Park" state, then after inserting
the encoder, a POWER ON (switch-off/switch-on) is necessary to acknowledge the fault.

### F31137 Motor encoder: Fault when determining the position (singleturn)

**Valid as of version:**
  
06.01.122

**Message value:**
  
Fault cause: %1 bin

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Encoder 1

**Response:**
  
 ENCODER

**Acknowledgment:**
  
PULSE INHIBIT

**Cause**
  
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
Bit 7: Position word 1 internal error (FPGA communication/FPGA parameterization/self
test/software).  
Bit 8: F1 (safety status display) error position word 1.  
Bit 9: F2 (safety status display) error position word 2.  
Bit 16: Position word 2 temperature outside limit value.  
Bit 17: Position word 2 position determination error (multiturn).  
Bit 18: Position word 2 FPGA error.  
Bit 19: Position word 2 velocity error.  
Bit 20: Position word 2 communication error between FPGAs.  
Bit 21: Position word 2 position determination error (singleturn).  
Bit 22: Position word 2 internal hardware fault (clock/power monitor IC/power).  
Bit 23: Position word 2 internal error (self test/software).  
----------  
Note:  
For an encoder version that is not described here, please contact the encoder manufacturer
for more detailed information on the bit coding.

**Remedy**
  
- Determine the detailed cause of the fault using the fault value.  
- If required, replace the DRIVE-CLiQ encoder.

### F31138 Motor encoder: Fault when determining the position (multiturn)

**Valid as of version:**
  
06.01.122

**Message value:**
  
Fault cause: %1 bin

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Encoder 1

**Response:**
  
 ENCODER

**Acknowledgment:**
  
PULSE INHIBIT

**Cause**
  
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
Bit 7: Position word 1 internal error (FPGA communication/FPGA parameterization/self
test/software).  
Bit 8: F1 (safety status display) error position word 1.  
Bit 9: F2 (safety status display) error position word 2.  
Bit 16: Position word 2 temperature outside limit value.  
Bit 17: Position word 2 position determination error (multiturn).  
Bit 18: Position word 2 FPGA error.  
Bit 19: Position word 2 velocity error.  
Bit 20: Position word 2 communication error between FPGAs.  
Bit 21: Position word 2 position determination error (singleturn).  
Bit 22: Position word 2 internal hardware fault (clock/power monitor IC/power).  
Bit 23: Position word 2 internal error (self test/software).  
----------  
Note:  
For an encoder version that is not described here, please contact the encoder manufacturer
for more detailed information on the bit coding.

**Remedy**
  
- Determine the detailed cause of the fault using the fault value.  
- If required, replace the DRIVE-CLiQ encoder.

### F31405 Motor encoder: Temperature in the encoder evaluation exceeded

**Valid as of version:**
  
06.01.122

**Message value:**
  
temperature: [0.1 degrees C] %1, temperature sensor number: %2

**Message class:**
  
Overtemperature of the electronic components (6)

**Component:**
  
Sensor Module Encoder 1

**Response:**
  
 ENCODER

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
An inadmissibly high temperature was detected in the encoder electronics or the encoder
evaluation.  
Fault value (r0949, interpret hexadecimal):  
yyxxxx hex: yy = temperature sensor number, xxxx = measured module temperature in
0.1 °C.

**Remedy**
  
When using a Sensor Module: Reduce the ambient temperature of the Sensor Module.  
Otherwise: Reduce the encoder ambient temperature.

### A31407 Motor encoder: Function limit reached

**Valid as of version:**
  
06.03.014

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

### F31503 Motor encoder: Position tracking cannot be reset

**Valid as of version:**
  
06.03.014

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
  
06.01.122

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

### F31801 Motor encoder DRIVE-CLiQ: Sign-of-life missing

**Valid as of version:**
  
06.01.122

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

**Component:**
  
Control Unit (CU)

**Response:**
  
 ENCODER

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
There is a DRIVE-CLiQ communication error between the converter and the encoder involved.  
  
Fault value (r0949, interpret hexadecimal):  
0000yyxx hex:  
yy = component number,  
xx = fault cause  
  
Error cause:  
10 (= 0A hex):  
The sign-of-life bit in the receive telegram is not set.

**Remedy**
  
- Check the electrical cabinet design and cable routing for EMC compliance.  
- Replace the component involved.

### F31802 Motor encoder: Time slice overflow

**Valid as of version:**
  
06.01.122

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
  
06.01.122

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
  
06.01.122

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
  
06.01.122

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

### F31820 Motor encoder DRIVE-CLiQ: Telegram error

**Valid as of version:**
  
06.01.122

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

**Component:**
  
Sensor Module Encoder 1

**Response:**
  
 ENCODER

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
There is a DRIVE-CLiQ communication error between the converter and the encoder involved.  
  
Fault value (r0949, interpret hexadecimal):  
0000yyxx hex:  
yy = component number,  
xx = fault cause  
  
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

**Remedy**
  
- Carry out a POWER ON (switch-off/switch-on).  
- Check the electrical cabinet design and cable routing for EMC compliance.  
- Check the DRIVE-CLiQ wiring (interrupted cable, contacts, ...).

### F31835 Motor encoder DRIVE-CLiQ: Cyclic data transfer error

**Valid as of version:**
  
06.01.122

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

**Component:**
  
Sensor Module Encoder 1

**Response:**
  
 ENCODER

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
There is a DRIVE-CLiQ communication error between the converter and the encoder involved.
The nodes do not send and receive in synchronism.  
  
Fault value (r0949, interpret hexadecimal):  
0000yyxx hex:  
yy = component number,  
xx = fault cause  
  
Error cause:  
33 (= 21 hex):  
The cyclic telegram has not been received.  
34 (= 22 hex):  
Timeout in the telegram receive list.  
64 (= 40 hex):  
Timeout in the telegram send list.

**Remedy**
  
- Carry out a POWER ON.  
- Replace the component involved.

### F31836 Motor encoder DRIVE-CLiQ: Send error for DRIVE-CLiQ data

**Valid as of version:**
  
06.01.122

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

**Component:**
  
Sensor Module Encoder 1

**Response:**
  
 ENCODER

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
There is a DRIVE-CLiQ communication error between the converter and the encoder involved.
Data were not able to be sent.  
  
Fault value (r0949, interpret hexadecimal):  
0000yyxx hex:  
yy = component number,  
xx = fault cause  
  
Error cause:  
65 (= 41 hex):  
Telegram type does not match send list.

**Remedy**
  
Carry out a POWER ON.

### F31837 Motor encoder DRIVE-CLiQ: Component fault

**Valid as of version:**
  
06.01.122

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

**Component:**
  
Sensor Module Encoder 1

**Response:**
  
 ENCODER

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
Fault detected on the DRIVE-CLiQ component involved. Faulty hardware cannot be excluded.  
  
Fault value (r0949, interpret hexadecimal):  
0000yyxx hex:  
yy = component number,  
xx = fault cause  
  
Error cause:  
32 (= 20 hex):  
Error in the telegram header.  
35 (= 23 hex):  
Receive error: The telegram buffer memory contains an error.  
66 (= 42 hex):  
Send error: The telegram buffer memory contains an error.  
67 (= 43 hex):  
Send error: The telegram buffer memory contains an error.

**Remedy**
  
- Check the DRIVE-CLiQ wiring (interrupted cable, contacts, ...).  
- Check the electrical cabinet design and cable routing for EMC compliance.  
- Replace the component involved.

### F31845 Motor encoder DRIVE-CLiQ: Cyclic data transfer error

**Valid as of version:**
  
06.01.122

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

**Component:**
  
Sensor Module Encoder 1

**Response:**
  
 ENCODER

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
There is a DRIVE-CLiQ communication error between the converter and the encoder involved.  
  
Fault value (r0949, interpret hexadecimal):  
0000yyxx hex:  
yy = component number,  
xx = fault cause  
  
Error cause:  
11 (= 0B hex):  
Synchronization error during alternating cyclic data transfer.

**Remedy**
  
Carry out a POWER ON (switch-off/switch-on).

### F31850 Motor encoder: Encoder evaluation internal software error

**Valid as of version:**
  
06.01.122

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

### F31851 Encoder 1 DRIVE-CLiQ: Sign-of-life missing

**Valid as of version:**
  
06.01.122

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

**Component:**
  
Sensor Module Encoder 1

**Response:**
  
 ENCODER

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
There is a DRIVE-CLiQ communication error from the Sensor Module involved (encoder
1) to the converter.  
The DRIVE-CLiQ component did not set the sign-of-life to the converter.  
  
Fault value (r0949, interpret hexadecimal):  
0000yyxx hex:  
yy = component number,  
xx = fault cause  
  
Error cause:  
10 (= 0A hex):  
The sign-of-life bit in the receive telegram is not set.

**Remedy**
  
- Upgrade the firmware of the component involved.  
- Carry out a POWER ON (switch-off/switch-on) for the component involved.

### F31860 Encoder 1 DRIVE-CLiQ: Telegram error

**Valid as of version:**
  
06.01.122

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

**Component:**
  
Sensor Module Encoder 1

**Response:**
  
 ENCODER

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
There is a DRIVE-CLiQ communication error from the Sensor Module involved (encoder
1) to the converter.  
  
Fault value (r0949, interpret hexadecimal):  
0000yyxx hex:  
yy = component number,  
xx = fault cause  
  
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
The DRIVE-CLiQ communication from the DRIVE-CLiQ component involved to the converter
signals that the supply voltage has failed.  
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

**Remedy**
  
- Carry out a POWER ON (switch-off/switch-on).  
- Check the electrical cabinet design and cable routing for EMC compliance.  
- Check the DRIVE-CLiQ wiring (interrupted cable, contacts, ...).

### F31875 Motor encoder: Supply voltage failed

**Valid as of version:**
  
06.01.122

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Supply voltage fault (undervoltage) (3)

**Component:**
  
Sensor Module Encoder 1

**Response:**
  
 ENCODER

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

### F31885 Encoder 1 DRIVE-CLiQ: Cyclic data transfer error

**Valid as of version:**
  
06.01.122

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

**Component:**
  
Sensor Module Encoder 1

**Response:**
  
 ENCODER

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
There is a DRIVE-CLiQ communication error between the converter and motor.  
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
  
- Check the OCC cable between the converter and motor.  
- Check the power supply voltage of the component involved.  
- Carry out a POWER ON (switch-off/switch-on).  
- Replace the component involved.  
Note:  
OCC: One Cable Connection (one cable system)

### F31886 Motor encoder DRIVE-CLiQ (CU): Error when sending DRIVE-CLiQ data

**Valid as of version:**
  
06.01.122

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

**Component:**
  
Sensor Module Encoder 1

**Response:**
  
 ENCODER

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
There is a DRIVE-CLiQ communication error from the Sensor Module involved (encoder
1) to the converter.  
Data were not able to be sent.  
  
Fault value (r0949, interpret hexadecimal):  
0000yyxx hex:  
yy = component number,  
xx = fault cause  
  
Error cause:  
65 (= 41 hex):  
Telegram type does not match send list.

**Remedy**
  
- Carry out a POWER ON.

### F31887 Motor encoder DRIVE-CLiQ (CU): Component fault

**Valid as of version:**
  
06.01.122

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

**Component:**
  
Sensor Module Encoder 1

**Response:**
  
 ENCODER

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
A fault has been detected on the DRIVE-CLiQ component involved (Sensor Module for
the motor encoder). Faulty hardware cannot be excluded.  
  
Fault value (r0949, interpret hexadecimal):  
0000yyxx hex:  
yy = component number,  
xx = fault cause  
  
Error cause:  
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

**Remedy**
  
- Check the DRIVE-CLiQ wiring (interrupted cable, contacts, ...).  
- Check the electrical cabinet design and cable routing for EMC compliance.  
- Replace the component involved.

### F31895 Encoder 1 DRIVE-CLiQ: Alternating cyclic data transfer error

**Valid as of version:**
  
06.01.122

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

**Component:**
  
Sensor Module Encoder 1

**Response:**
  
 ENCODER

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
There is a DRIVE-CLiQ communication error from the Sensor Module involved (encoder
1) to the converter.  
Error cause:  
11 (= 0B hex):  
Synchronization error during alternating cyclic data transfer.  
Note regarding the message value:  
The individual information is coded as follows in the message value (r0949/r2124):  
0000yyxx hex:  
yy = component number,  
xx = fault cause

**Remedy**
  
Carry out a POWER ON.

### F31896 Motor encoder DRIVE-CLiQ (CU): Inconsistent component properties

**Valid as of version:**
  
06.01.122

**Message value:**
  
Component number: %1

| Symbol | Meaning |
| --- | --- |
| For %1 | Component in target topology |

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

**Component:**
  
Sensor Module Encoder 1

**Response:**
  
 OFF2

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The properties of the DRIVE-CLiQ component (Sensor Module for the motor encoder),
specified by the fault value, have changed in an incompatible fashion with respect
to the properties when running up. One cause can be, e.g. that a DRIVE-CLiQ cable
or DRIVE-CLiQ component has been replaced.  
Fault value (r0949, interpret decimal):  
Component number.

**Remedy**
  
- Carry out a POWER ON.  
- When a component is replaced, the same component type and if possible the same firmware
version should be used.  
- When a cable is replaced, only cables whose length is the same as or as close as
possible to the length of the original cables should be used (ensure compliance with
the maximum cable length).

### F31950 Motor encoder: Internal software error

**Valid as of version:**
  
06.01.122

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
  
06.03.014

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

### F32120 Encoder 2: Encoder power supply fault

**Valid as of version:**
  
06.03.014

**Message value:**
  
Fault cause: %1 bin

**Message class:**
  
Position/speed actual value incorrect or not available (11)

**Component:**
  
Encoder 2

**Response:**
  
 OFF1

**Acknowledgment:**
  
PULSE INHIBIT

**Cause**
  
An encoder power supply fault was detected.  
Fault value (r0949, interpret binary):  
Bit 0: Undervoltage condition on the sense line.  
Bit 1: Overcurrent condition for the encoder power supply.  
Bit 2: Overcurrent condition for encoder power supply on cable resolver excitation
negative.  
Bit 3: Overcurrent condition for encoder power supply on cable resolver excitation
positive.  
Bit 4: The 24 V power supply via the inverter is overloaded.  
Bit 5: Overcurrent at the EnDat connection of the converter.  
Bit 6: Overvoltage at the EnDat connection of the converter.  
Bit 7: Hardware fault at the EnDat connection of the converter.  
Note:  
If the encoder cables 6FX2002-2EQ00-.... and 6FX2002-2CH00-.... are interchanged,
this can result in the encoder being destroyed because the pins of the operating voltage
are reversed.

**Remedy**
  
For fault value, bit 0 = 1:  
- Correct encoder cable connected?  
- Check the plug connections of the encoder cable.  
- SMC30: Check the parameterization (p0404.22).  
For fault value, bit 1 = 1:  
- Correct encoder cable connected?  
- Replace the encoder or encoder cable.  
For fault value, bit 2 = 1:  
- Correct encoder cable connected?  
- Replace the encoder or encoder cable.  
For fault value, bit 3 = 1:  
- Correct encoder cable connected?  
- Replace the encoder or encoder cable.  
For fault value, bit 5 = 1:  
- Measuring unit correctly connected at the converter?  
- Replace the measuring unit or the cable to the measuring unit.  
For fault value, bit 6, 7 = 1:  
- Replace the defective EnDat 2.2 converter.

### F32135 Encoder 2: Fault when determining the position (single turn)

**Valid as of version:**
  
06.03.014

**Message value:**
  
Fault cause: %1 bin

**Message class:**
  
Position/speed actual value incorrect or not available (11)

**Component:**
  
Encoder 2

**Response:**
  
 OFF1

**Acknowledgment:**
  
PULSE INHIBIT

**Cause**
  
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
Bit 6: Reserved (undervoltage)/hardware fault EnDat supply (--> F3x110, x = 1, 2,
3).  
Bit 7: Reserved (overcurrent)/EnDat encoder withdrawn when not in the parked state
(--> F3x110, x = 1, 2, 3).  
Bit 8: Reserved (battery)/overcurrent EnDat supply (--> F3x110, x = 1, 2, 3).  
Bit 9: Reserved/overvoltage EnDat supply (--> F3x110, x = 1, 2, 3).  
Bit 11: Reserved/internal communication error (--> F3x110, x = 1, 2, 3).  
Bit 12: Reserved/internal communication error (--> F3x110, x = 1, 2, 3).  
Bit 13: Reserved/internal communication error (--> F3x110, x = 1, 2, 3).  
Bit 14: Reserved/internal communication error (--> F3x110, x = 1, 2, 3).  
Bit 15: Internal communication error (--> F3x110, x = 1, 2, 3).  
Bit 16: Lighting (--> F3x135, x = 1, 2, 3).  
Bit 17: Signal amplitude (--> F3x135, x = 1, 2, 3).  
Bit 18: Singleturn position 1 (--> F3x135, x = 1, 2, 3).  
Bit 19: Overvoltage (--> F3x135, x = 1, 2, 3).  
Bit 20: Undervoltage (--> F3x135, x = 1, 2, 3).  
Bit 21: Overcurrent (--> F3x135, x = 1, 2, 3).  
Bit 22: Temperature exceeded (--> F3x405, x = 1, 2, 3).  
Bit 23: Singleturn position 2 (safety status display).  
Bit 24: Singleturn system (--> F3x135, x = 1, 2, 3).  
Bit 25: Singleturn power down (--> F3x135, x = 1, 2, 3)  
Bit 26: Multiturn position 1 (--> F3x136, x = 1, 2, 3).  
Bit 27: Multiturn position 2 (--> F3x136, x = 1, 2, 3).  
Bit 28: Multiturn system (--> F3x136, x = 1, 2, 3).  
Bit 29: Multiturn power down (--> F3x136, x = 1, 2, 3).  
Bit 30: Multiturn overflow/underflow (--> F3x136, x = 1, 2, 3).  
Bit 31: Multiturn battery (reserved).

**Remedy**
  
- Determine the detailed cause of the fault using the fault value.  
- Replace the encoder if necessary.  
Note:  
An EnDat 2.2 encoder may only be removed and inserted in the "Park" state.  
If an EnDat 2.2 encoder was removed when not in the "Park" state, then after inserting
the encoder, a POWER ON (switch-off/switch-on) is necessary to acknowledge the fault.

### F32136 Encoder 2: Fault when determining the position (multiturn)

**Valid as of version:**
  
06.03.014

**Message value:**
  
Fault cause: %1 bin

**Message class:**
  
Position/speed actual value incorrect or not available (11)

**Component:**
  
Encoder 2

**Response:**
  
 OFF1

**Acknowledgment:**
  
PULSE INHIBIT

**Cause**
  
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
Bit 6: Reserved (undervoltage)/hardware fault EnDat supply (--> F3x110, x = 1, 2,
3).  
Bit 7: Reserved (overcurrent)/EnDat encoder withdrawn when not in the parked state
(--> F3x110, x = 1, 2, 3).  
Bit 8: Reserved (battery)/overcurrent EnDat supply (--> F3x110, x = 1, 2, 3).  
Bit 9: Reserved/overvoltage EnDat supply (--> F3x110, x = 1, 2, 3).  
Bit 11: Reserved/internal communication error (--> F3x110, x = 1, 2, 3).  
Bit 12: Reserved/internal communication error (--> F3x110, x = 1, 2, 3).  
Bit 13: Reserved/internal communication error (--> F3x110, x = 1, 2, 3).  
Bit 14: Reserved/internal communication error (--> F3x110, x = 1, 2, 3).  
Bit 15: Internal communication error (--> F3x110, x = 1, 2, 3).  
Bit 16: Lighting (--> F3x135, x = 1, 2, 3).  
Bit 17: Signal amplitude (--> F3x135, x = 1, 2, 3).  
Bit 18: Singleturn position 1 (--> F3x135, x = 1, 2, 3).  
Bit 19: Overvoltage (--> F3x135, x = 1, 2, 3).  
Bit 20: Undervoltage (--> F3x135, x = 1, 2, 3).  
Bit 21: Overcurrent (--> F3x135, x = 1, 2, 3).  
Bit 22: Temperature exceeded (--> F3x405, x = 1, 2, 3).  
Bit 23: Singleturn position 2 (safety status display).  
Bit 24: Singleturn system (--> F3x135, x = 1, 2, 3).  
Bit 25: Singleturn power down (--> F3x135, x = 1, 2, 3)  
Bit 26: Multiturn position 1 (--> F3x136, x = 1, 2, 3).  
Bit 27: Multiturn position 2 (--> F3x136, x = 1, 2, 3).  
Bit 28: Multiturn system (--> F3x136, x = 1, 2, 3).  
Bit 29: Multiturn power down (--> F3x136, x = 1, 2, 3).  
Bit 30: Multiturn overflow/underflow (--> F3x136, x = 1, 2, 3).  
Bit 31: Multiturn battery (reserved).

**Remedy**
  
- Determine the detailed cause of the fault using the fault value.  
- Replace the encoder if necessary.  
Note:  
An EnDat 2.2 encoder may only be removed and inserted in the "Park" state.  
If an EnDat 2.2 encoder was removed when not in the "Park" state, then after inserting
the encoder, a POWER ON (switch-off/switch-on) is necessary to acknowledge the fault.

### F32137 Encoder 2: Fault when determining the position (single turn)

**Valid as of version:**
  
06.03.014

**Message value:**
  
Fault cause: %1 bin

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Encoder 2

**Response:**
  
 OFF1

**Acknowledgment:**
  
PULSE INHIBIT

**Cause**
  
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
Bit 7: Position word 1 internal error (FPGA communication/FPGA parameterization/self
test/software).  
Bit 8: F1 (safety status display) error position word 1.  
Bit 9: F2 (safety status display) error position word 2.  
Bit 16: Position word 2 temperature outside limit value.  
Bit 17: Position word 2 position determination error (multiturn).  
Bit 18: Position word 2 FPGA error.  
Bit 19: Position word 2 velocity error.  
Bit 20: Position word 2 communication error between FPGAs.  
Bit 21: Position word 2 position determination error (singleturn).  
Bit 22: Position word 2 internal hardware fault (clock/power monitor IC/power).  
Bit 23: Position word 2 internal error (self test/software).  
----------  
Note:  
For an encoder version that is not described here, please contact the encoder manufacturer
for more detailed information on the bit coding.

**Remedy**
  
- Determine the detailed cause of the fault using the fault value.  
- If required, replace the DRIVE-CLiQ encoder.

### F32138 Encoder 2: Fault when determining the position (multiturn)

**Valid as of version:**
  
06.03.014

**Message value:**
  
Fault cause: %1 bin

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Encoder 2

**Response:**
  
 OFF1

**Acknowledgment:**
  
PULSE INHIBIT

**Cause**
  
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
Bit 7: Position word 1 internal error (FPGA communication/FPGA parameterization/self
test/software).  
Bit 8: F1 (safety status display) error position word 1.  
Bit 9: F2 (safety status display) error position word 2.  
Bit 16: Position word 2 temperature outside limit value.  
Bit 17: Position word 2 position determination error (multiturn).  
Bit 18: Position word 2 FPGA error.  
Bit 19: Position word 2 velocity error.  
Bit 20: Position word 2 communication error between FPGAs.  
Bit 21: Position word 2 position determination error (singleturn).  
Bit 22: Position word 2 internal hardware fault (clock/power monitor IC/power).  
Bit 23: Position word 2 internal error (self test/software).  
----------  
Note:  
For an encoder version that is not described here, please contact the encoder manufacturer
for more detailed information on the bit coding.

**Remedy**
  
- Determine the detailed cause of the fault using the fault value.  
- If required, replace the DRIVE-CLiQ encoder.

### F32405 Encoder 2: Temperature in the encoder evaluation exceeded

**Valid as of version:**
  
06.03.014

**Message value:**
  
temperature: [0.1 degrees C] %1, temperature sensor number: %2

**Message class:**
  
Overtemperature of the electronic components (6)

**Component:**
  
Sensor Module Encoder 2

**Response:**
  
 OFF1

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
An inadmissibly high temperature was detected in the encoder electronics or the encoder
evaluation.  
Fault value (r0949, interpret hexadecimal):  
yyxxxx hex: yy = temperature sensor number, xxxx = measured module temperature in
0.1 °C.

**Remedy**
  
When using a Sensor Module: Reduce the ambient temperature of the Sensor Module.  
Otherwise: Reduce the encoder ambient temperature.

### F32802 Encoder 2: Time slice overflow

**Valid as of version:**
  
06.03.014

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
  
A time slice overflow has occurred in encoder 2.  
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

### F32804 Encoder 2: Sensor Module checksum error

**Valid as of version:**
  
06.03.014

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
  
A checksum error has occurred when reading-out the program memory on the Sensor Module.  
Fault value (r0949, interpret hexadecimal):  
yyyyxxxx hex  
yyyy: Memory area involved.  
xxxx: Difference between the checksum at POWER ON and the actual checksum.

**Remedy**
  
- Carry out a POWER ON (switch-off/switch-on).  
- Upgrade firmware to later version (>= V2.6 HF3, >= V4.3 SP2, >= V4.4).  
- Check whether the permissible ambient temperature for the component is maintained.  
- Replace the Sensor Module.

### F32813 Encoder 2: Hardware logic unit failed

**Valid as of version:**
  
06.03.014

**Message value:**
  
Fault cause: %1 bin

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Sensor Module Encoder 2

**Response:**
  
 OFF1

**Acknowledgment:**
  
PULSE INHIBIT

**Cause**
  
The logic unit of the DRIVE-CLiQ encoder has failed.  
Fault value (r0949, interpret binary):  
Bit 0: ALU watchdog has responded.  
Bit 1: ALU has detected a sign-of-life error.

**Remedy**
  
When the error reoccurs, replace the encoder.

### F32850 Encoder 2: Encoder evaluation internal software error

**Valid as of version:**
  
06.03.014

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
  
An internal software error has occurred in the Sensor Module of encoder 2.  
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

### F32899 Encoder 2: Unknown fault

**Valid as of version:**
  
06.03.014

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
  
A fault occurred on the Sensor Module for encoder 2 that cannot be interpreted by
the Control Unit firmware.  
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

### A32999 Encoder 2: Unknown alarm

**Valid as of version:**
  
06.03.014

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
  
06.03.014

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
  
06.03.014

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

### F36207 Hub: Overtemperature component

**Valid as of version:**
  
06.01.122

**Message value:**
  
%1

**Message class:**
  
Overtemperature of the electronic components (6)

**Component:**
  
Terminal Board (TB)

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The temperature on the DRIVE-CLiQ Hub Module has exceeded the fault threshold.  
Fault value (r0949, interpret decimal):  
Actual temperature in 0.1 °C resolution.

**Remedy**
  
- Check ambient temperature at component installation location.  
- Replace the component involved.

### A36211 Hub: Overtemperature alarm component

**Valid as of version:**
  
06.01.122

**Message value:**
  
%1

**Message class:**
  
Overtemperature of the electronic components (6)

**Component:**
  
Terminal Board (TB)

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The temperature on the DRIVE-CLiQ Hub Module has exceeded the alarm threshold.  
Alarm value (r2124, interpret decimal):  
Actual temperature in 0.1 °C resolution.

**Remedy**
  
- Check ambient temperature at component installation location.  
- Replace the component involved.

## SINAMICS Alarms S210 36214 - 36999

SINAMICS Alarms S210 36214 - 36999

### F36214 Hub: overvoltage fault 24 V supply

**Valid as of version:**
  
06.01.122

**Message value:**
  
%1

**Message class:**
  
Supply voltage fault (overvoltage) (3)

**Component:**
  
Terminal Board (TB)

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The 24 V power supply on the DRIVE-CLiQ Hub Module has exceeded the fault threshold.  
Fault value (r0949, interpret decimal):  
Actual operating voltage in 0.1 °C resolution

**Remedy**
  
- Check the power supply of the component.  
- Replace the component involved.

### F36216 Hub: undervoltage fault 24 V supply

**Valid as of version:**
  
06.01.122

**Message value:**
  
%1

**Message class:**
  
Supply voltage fault (undervoltage) (3)

**Component:**
  
Terminal Board (TB)

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The 24 V power supply on the DRIVE-CLiQ Hub Module has undershot the fault threshold.  
Fault value (r0949, interpret decimal):  
Actual operating voltage in 0.1 °C resolution

**Remedy**
  
- Check the power supply of the component.  
- Replace the component involved.

### A36217 Hub: undervoltage alarm 24 V supply

**Valid as of version:**
  
06.01.122

**Message value:**
  
%1

**Message class:**
  
Supply voltage fault (undervoltage) (3)

**Component:**
  
Terminal Board (TB)

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The 24 V power supply on the DRIVE-CLiQ Hub Module has undershot the alarm threshold.  
Alarm value (r2124, interpret decimal):  
Actual operating voltage in 0.1 °C resolution

**Remedy**
  
- Check the power supply of the component.  
- Replace the component involved.

### N36800 Hub: Group signal

**Valid as of version:**
  
06.01.122

**Message value:**
  
-

**Message class:**
  
General drive fault (19)

**Component:**
  
None

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
The DRIVE-CLiQ Hub Module has detected at least one fault.

**Remedy**
  
Evaluation of other active messages.

### A36802 Hub: Time slice overflow

**Valid as of version:**
  
06.01.122

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Terminal Board (TB)

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
A time slice overflow has occurred on the DRIVE-CLiQ Hub Module.  
Fault value (r0949, interpret decimal):  
xx: Time slice number xx

**Remedy**
  
- Reduce the current controller frequency.  
- Carry out a POWER ON (switch-off/switch-on) for all components.  
- Upgrade firmware to later version.  
- Contact Technical Support.

### F36804 Hub: Checksum error has occurred

**Valid as of version:**
  
06.01.122

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Terminal Board (TB)

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
A checksum error occurred when reading out the program memory on the DRIVE-CLiQ Hub
Module.  
Fault value (r0949, interpret hexadecimal):  
Difference between the checksum at POWER ON and the actual checksum.

**Remedy**
  
- Check whether the permissible ambient temperature for the component is maintained.  
- Replace the DRIVE-CLiQ Hub Module.

### F36805 Hub: EEPROM checksum incorrect

**Valid as of version:**
  
06.01.122

**Message value:**
  
%1

**Message class:**
  
Hardware/software error (1)

**Component:**
  
Terminal Board (TB)

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
The internal parameter data on the DRIVE-CLiQ Hub Module is incorrect.  
Alarm value (r2124, interpret hexadecimal):  
01: EEPROM access error.  
02: Too many blocks in the EEPROM.

**Remedy**
  
- Check whether the permissible ambient temperature for the component is maintained.  
- Replace the DRIVE-CLiQ Hub Module.

### F36837 Hub DRIVE-CLiQ: Component fault

**Valid as of version:**
  
06.01.122

**Message value:**
  
Component number: %1, fault cause: %2

**Message class:**
  
Internal (DRIVE-CLiQ) communication error (12)

**Component:**
  
Terminal Board (TB)

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
Fault detected on the DRIVE-CLiQ component involved. Faulty hardware cannot be excluded.  
Error cause:  
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

**Remedy**
  
- Check the DRIVE-CLiQ wiring (interrupted cable, contacts, ...).  
- Check the electrical cabinet design and cable routing for EMC compliance.  
- If required, use another DRIVE-CLiQ socket.  
- Replace the component involved.

### F36899 Hub: Unknown fault

**Valid as of version:**
  
06.01.122

**Message value:**
  
New message: %1

**Message class:**
  
General drive fault (19)

**Component:**
  
Terminal Board (TB)

**Response:**
  
 NONE

**Acknowledgment:**
  
IMMEDIATELY

**Cause**
  
A fault occurred on the DRIVE-CLiQ Hub Module, which cannot be interpreted by the
firmware.  
This can occur if the firmware on this component is more recent than the firmware
on the converter.  
Fault value (r0949, interpret decimal):  
Fault number.  
Note:  
If required, the significance of this new fault can be read about in a more recent
description of the converter.

**Remedy**
  
- Replace the firmware on the DRIVE-CLiQ Hub Module with older firmware.  
- Upgrade the converter firmware.

### A36999 Hub: Unknown alarm

**Valid as of version:**
  
06.01.122

**Message value:**
  
New message: %1

**Message class:**
  
General drive fault (19)

**Component:**
  
Terminal Board (TB)

**Response:**
  
 NONE

**Acknowledgment:**
  
NONE

**Cause**
  
An alarm has occurred on the DRIVE-CLiQ Hub Module, which cannot be interpreted by
the converter firmware.  
This can occur if the firmware on this component is more recent than the firmware
on the converter.  
Alarm value (r2124, interpret decimal):  
Alarm number.  
Note:  
If required, the significance of this new alarm can be read about in a more recent
description of the converter.

**Remedy**
  
- Replace the firmware on the DRIVE-CLiQ Hub Module with older firmware.  
- Upgrade the converter firmware.

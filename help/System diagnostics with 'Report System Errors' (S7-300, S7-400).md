---
title: "System diagnostics with 'Report System Errors' (S7-300, S7-400)"
package: SysDiagRSE34enUS
topics: 14
devices: [S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# System diagnostics with 'Report System Errors' (S7-300, S7-400)

This section contains information on the following topics:

- [Introduction to system diagnostics with 'Report System Errors' (S7-300, S7-400)](#introduction-to-system-diagnostics-with-report-system-errors-s7-300-s7-400)
- [Basics of system diagnostics (S7-300, S7-400)](#basics-of-system-diagnostics-s7-300-s7-400)
- [Modules with limited diagnostic possibilities (S7-300, S7-400)](#modules-with-limited-diagnostic-possibilities-s7-300-s7-400)
- [Diagnostics blocks for reporting system errors (S7-300, S7-400)](#diagnostics-blocks-for-reporting-system-errors-s7-300-s7-400)
- [Properties of the blocks (S7-300, S7-400)](#properties-of-the-blocks-s7-300-s7-400)
- [Supported error OBs (S7-300, S7-400)](#supported-error-obs-s7-300-s7-400)
- [Diagnostics status DB (S7-300, S7-400)](#diagnostics-status-db-s7-300-s7-400)
- [Displaying settings of system diagnostics (S7-300, S7-400)](#displaying-settings-of-system-diagnostics-s7-300-s7-400)
- [Settings (S7-300, S7-400)](#settings-s7-300-s7-400)

## Introduction to system diagnostics with 'Report System Errors' (S7-300, S7-400)

### Introduction

When a system error occurs, hardware components and devices of other manufacturers (slaves whose properties are set by the GSD files) can trigger organization block calls.

Example: If a wire breaks, a module with diagnostics capability can call OB 82.

The hardware components provide information on the system error that has occurred. The start event information, in other words, the local data of the assigned OB (including data record 0), provides general information on the location (for example, logical address of the module) and type (for example channel error or module fault) of the error.

The problem can also be specified in greater detail using additional diagnostics information (reading data record 1 with the "RDSYSST" instruction or reading the diagnostics frame from standard DP slaves with the "DPNRM_DG" instruction): For example, channel 0 or 1, broken wire or measuring range exceeded.

System diagnostics with "Report System Errors" (RSE) provides you with a convenient way of evaluating this diagnostics information for S7-300/400 PLCs, ET200S, ET200Pro and software PLCs and to display it in the form of messages. The required blocks and alarm texts are created in the properties of the particular PLC. You only need to download the generated blocks to the CPU and, if required, transfer the texts to connected HMI devices.

To display diagnostics events graphically, for example on an HMI device or via a Web server, you can generate one or more status DBs. These status DBs are updated by the system diagnostics blocks and then contain information on the current state of the system.

## Basics of system diagnostics (S7-300, S7-400)

Using system diagnostics with "Report System Errors", you can generate blocks that analyze errors in the system and generate alarms with a textual error description and the error location.

These alarms are defined per component with alarm capabilities (for example channel errors or rack errors) and are limited to 255 alarms component with alarm capability. You will receive a message if this limit is exceeded.

General settings that you make or change in system diagnostics are stored along with the project. The influence on the system diagnostics only takes effect after generating the blocks, compiling the hardware configuration and downloading the configuration to the components involved.

### Recommended procedure

Make the settings for reporting system errors and the structure of the alarms. Specify which diagnostics blocks will be created and configure the status DBs. Generate the blocks and download the configuration to apply the changes.

You will find detailed information in the sections below.

> **Note**
>
> If you use system diagnostics, the system response of the plant may change if an error occurs. For example, the CPU may not change to "STOP" mode as it would without system diagnostics.
>
> Make sure that all protective mechanisms of the plant are working properly.

## Modules with limited diagnostic possibilities (S7-300, S7-400)

### Introduction

The components of the S7-300 stations, S7-400 stations, PROFINET IO devices, DP slaves, and WinAC are supported by "Report System Errors", provided that they support functions such as diagnostic interrupts, pull/plug interrupts, and channel-specific diagnostics.

### Components not supported

The following components are not supported by "Report System Errors":

- M7 configurations
- PROFIBUS DP configurations using a DP master interface module (CP 342-5 DP) in S7-300 stations
- PROFINET IO devices using an external controller (CP 343-1 Advanced) in S7-300 stations

Please note that a hot restart can also result in missing interrupt alarms. This behavior is due to the fact that the alarm acknowledgment memory of the CPU is not cleared during a hot restart, but "Report System Errors" resets the internal data. Not all of the module or channel faults that occur before startup or during a failure will be reported.

A maximum of 8 channel faults are reported per module.

> **Note**
>
> **If you are using a CP 443-5 and it is in STOP mode, a master system failure is not reported at startup.**

### PROFIBUS DP

For all PROFIBUS DP slaves, station faults (failure/return) are indicated with a plain text alarm.

For all PROFIBUS DP slaves, the manufacturer-specific diagnostics are supported with the following limitations:

- Only V1 slaves are supported. These are slaves in whose GSD file the entry "DPV1_Slave=1" is set.
- The DP interrupt mode for this slave must be set to "DPV0".

### Diagnostics repeater

The alarms of the diagnostics repeater are output as plain text in DPV0 mode. The texts are read out from the GSD file.

### PROFINET IO

Below you will find the diagnostics of the various PROFINET IO devices that are supported by "Report System Errors".

Errors that occur during operation (CPU in RUN):

- Device faults (failure, return) are supported
- Module faults and submodule faults (Module/submodule removed, Wrong module/submodule, Compatible module/submodule) are supported
- Channel faults are supported and extended channel fault information is evaluated

### AS-Interface

For AS-Interface slaves, an alarm is sent if the actual configuration does not match the expected configuration.

### Shared devices

"Report System Errors" evaluates the information as to whether a (sub)module has been configured as a shared device. Because "Report System Errors" is always looking at a CPU, only the (sub)modules that have the full access setting for this CPU are taken into consideration for the diagnostics. The (sub)modules configured as "not assigned" are not evaluated.

## Diagnostics blocks for reporting system errors (S7-300, S7-400)

Once you have made the settings for reporting system errors, the required blocks (FB with assigned instance DB and one or more global DBs, an FC and, depending on the setting, also OBs that do not yet exist) and status DBs are created the next time you compile the hardware configuration.

The following blocks are created:

- Diagnostics FB (default: FB 49),
- Instance DB for the diagnostics FB (default: FB 49),
- Global DB (default: FB 50),
- Diagnostics FC (default: FC 49),
- Error OBs (are automatically created if the CPU supports this function),
- Cyclic OBs (if you have selected this option in the "OB configuration" group box),
- Optional status DBs

The created blocks (except OBs) are stored in the project tree under "Program blocks &gt; System blocks &gt; Report System Errors".

> **Note**
>
> The block numbers set for the created system diagnostics blocks must not overlap existing block numbers. Moreover, the numbers must not overlap the numbers of blocks located in libraries.
>
> If problems occur in the generation of blocks, check whether the preset numbers (FB 49, DB 49, FC 49, DB 50) have been changed. If this is the case, try to repeat the generation with the preset block numbers or use numbers which you are certain are not in use elsewhere.

---

**See also**

[Properties of the blocks (S7-300, S7-400)](#properties-of-the-blocks-s7-300-s7-400)

## Properties of the blocks (S7-300, S7-400)

### Diagnostics blocks

The created diagnostics blocks (FB with assigned instance DB and one or more global DBs and an FC) evaluate the local data of the error OB and read any additional diagnostics information from the hardware component that triggered the error.

They have the following properties:

- Created in RSE language (report system errors) (also applies to the blocks listed above)
- Know-how protected (also applies to the blocks listed above)
- Delay incoming interrupts during runtime

### Status DBs

The status DBs act as the interface for the diagnostics blocks and allow diagnostics events to be displayed graphically on an HMI device or a Web server.

---

**See also**

[Settings for system diagnostics blocks (S7-300, S7-400)](#settings-for-system-diagnostics-blocks-s7-300-s7-400)

## Supported error OBs (S7-300, S7-400)

The following error OBs are created automatically if they are supported by the configured CPU:

| OB | Diagnostics FB call | Description |
| --- | --- | --- |
| OB 70 (IO redundancy error) | possible | This OB exists only with H-CPUs. |
| OB 72 (CPU redundancy error) | possible | This OB exists only with H-CPUs. |
| OB 73 (communications redundancy error) | possible | This OB exists only with a few H-CPUs. |
| OB 81 (power supply error) | possible |  |
| OB 82 (diagnostics interrupt OB) | possible |  |
| OB 83 (pull/plug interrupt) | possible |  |
| OB 85 (program execution error) | not possible | If 'RSE' creates this OB when it is generating the diagnostics blocks, additional networks are inserted to implement the following program sequence:  - If errors occur when updating the process image (for example removing the module), the CPU is prevented from changing to STOP so that the diagnostic FB can be run in OB 83. If there is a setting for "CPU STOP" after an alarm from "RSE", this takes effect in OB 83. - With all other error events of OB 85, the CPU changes to STOP. |
| OB 86 (failure of an expansion rack, a DP master system or a distributed I/O device) | possible |  |

### If the OBs already exist...

Existing error OBs on not overwritten. If appropriate, the call for the diagnostics FB is appended in the existing OB.

### If the configuration includes distributed I/O devices...

To evaluate errors in the distributed I/O, the created FB automatically calls the "DPNRM_DG" instruction (read diagnostics data of the DP slaves). For this function to operate correctly, the created FB must be called either only in OB 1 or in a cyclic interrupt OB with a short call interval and in the startup OBs.

> **Note**
>
> Please note the following:
>
> - Due to the OB 85 created by the system diagnostics, the CPU does not change to STOP if the "error updating the process image" error event occurs.
> - OB 85 is also called by the CPU in the following error situations.
>
>   - "Error event for an OB that is not loaded"
>   - "Error calling or accessing a block that is not loaded"
>
>     When these errors occur, the OB 85 generated by the system diagnostics still changes the CPU to STOP, just like before the use of system diagnostics.

## Diagnostics status DB (S7-300, S7-400)

Within system diagnostics, you have the option of creating a status DB. This status DB is updated by the system diagnostics blocks and then contains information on the current system status.

### Interface for the diagnostics status DB

The created data block (default: DB 127) allows you to query the system state of a configured component and, if required, all its lower-level components.

This data block is required to support system diagnostics using the Web server or diagnostics viewer. As default, it is enabled.

> **Note**
>
> Please note that system diagnostics must be activated both on the Web server or diagnostics viewer and in the Inspector window of the PLC to be able to display diagnostics data of the status DBs.

After restarting a CPU with Web server, the module state is displayed following a delay. To shorten the waiting time, you can call the RSE diagnostics block in a cyclic interrupt OB.

### Structure of the diagnostics status DB

| Address |  | Name | Data type | Description |
| --- | --- | --- | --- | --- |
| +0 |  | Directory |  |  |
| 0 |  | D_Version | WORD | Version supported by system diagnostics |
| 2 |  | D_pGlobalState | WORD | Byte offset to the start of the "GlobalState" section |
| 4 |  | D_pQuery | WORD | Byte offset to the start of the "Query" section |
| 6 |  | D_pComponent | WORD | Byte offset to the start of the "Component" section |
| 8 |  | D_pError | WORD | Byte offset to the start of the "Error" section |
| 10 |  | D_pState | WORD | Byte offset to the start of the "State" section |
| 12 |  | D_pAlarm | WORD | Byte offset to the start of the "Alarm" section |
| 14 |  | D_pSubComponent | WORD | Byte offset to the start of the "Subcomponent" section |
| +16 | GlobalState |  |  |  |
| 0 |  | G_EventCount | WORD | ID of the last event (counter) |
| 2.0 |  | G_StartReporting | BOOL | Startup evaluation active |
| +20 |  | Query |  |  |
| 0 |  | Q_ClientID_User | DWORD | ID of the client; here, please use a value between 1 and 255. Make sure that different clients use different IDs. |
| 4 |  | Q_ClientID_Intern | DWORD | ID of the client (internal) |
| 8.0 |  | Q_WithSubComponent | BOOL | With/without status of the lower-level components (slower) |
| 8.1 |  | Q_SubComponentAlarm | BOOL | AS-i master returns AS-i slave interrupts |
| 8.2 |  | Q_Reserved2 | BOOL | Reserved |
| 8.3 |  | Q_Reserved3 | BOOL | Reserved |
| 8.4 |  | Q_Reserved4 | BOOL | Reserved |
| 8.5 |  | Q_Reserved5 | BOOL | Reserved |
| 8.6 |  | Q_Reserved6 | BOOL | Reserved |
| 8.7 |  | Q_Reserved7 | BOOL | Reserved |
| 9.0 |  | Q_Start | BOOL | Start query |
| 10 |  | Q_Error | BYTE | Internal error in query |
| 11 |  | Q_Reserved8 | BYTE | Reserved |
| +32 | Component |  |  |  |
| 0 |  | C_AddressMode | BYTE | Addressing mode of the module |
| 1 |  | C_Reserved1 | BYTE | Reserved |
| 2 |  | C_ComponentID | WORD | Hardware ID of the component (internal) |
| +36 |  | Error |  |  |
| 0 |  | E_ErrorNo | WORD | Index of the requested/actual error |
| 2.0 |  | E_LastError | BOOL | Is set when E_ErrorNo does not equal 0. Value TRUE if E_ErrorNo is the index of the last error otherwise FALSE |
| +40 |  | State |  |  |
| 0 |  | S_Hierarchy | BYTE | Reserved |
| 1 |  | S_Periphery | BYTE | Reserved |
| 2.0 |  | S_SupFault | BOOL | The component cannot be reached |
| 2.1 |  | S_NotAvailable | BOOL | The component does not exist |
| 2.2 |  | S_Faulty | BOOL | The component is faulty, the "Alarm" section is not empty |
| 2.3 |  | S_MoreErrors | BOOL | There are more errors than system diagnostics can store |
| 2.4 |  | S_Maintenance1 | BOOL | A maintenance request is pending |
| 2.5 |  | S_Maintenance2 | BOOL | A maintenance demand is pending |
| 2.6 |  | S_Deactivated | BOOL | The component was deactivated *) |
| 2.7 |  | S_Reserved2 | BOOL | Reserved |
| 3.0 |  | S_SubFault | BOOL | A subcomponent is faulty |
| 3.1 |  | S_SubMaintenance1 | BOOL | A maintenance request is pending for a subcomponent |
| 3.2 |  | S_SubMaintenance2 | BOOL | A maintenance demand is pending for a subcomponent |
| 3.3 |  | S_SubDeactivated | BOOL | A subcomponent is deactivated |
| 3.4 |  | S_Reserved4 | BOOL | Reserved |
| 3.5 |  | S_Reserved5 | BOOL | Reserved |
| 3.6 |  | S_Reserved6 | BOOL | Reserved |
| 3.7 |  | S_Reserved7 | BOOL | Reserved |
| 4 |  | S_TIAMS | DWORD | Maintenance state of the component |
| 8 |  | S_TIAMSChannelExist | DWORD | Maintenance state: Configured channels |
| 12 |  | S_TIAMSChannelOK | DWORD | Maintenance state: Faulty channels |
| 16 |  | S_ChannelCount | WORD | Number of channels; valid only when Q_WithSubComponent is set |
| 18.0 |  | S_ChannelVector | ARRAY [0 to 255]  BOOL | Number of channels affected; valid only when Q_WithSubComponent is set |
| +90 |  | Alarm |  |  |
| 0 |  | A_ComponentID | WORD | Hardware ID of the component (internal) |
| 2 |  | A_TextID1 | WORD | ID of the first error text |
| 4 |  | A_TextLexikonID1 | WORD | ID of the first error text lexicon |
| 6 |  | A_HelpTextLexikonID1 | WORD | ID of the first help text lexicon |
| 8 |  | A_MapTextID | WORD | ID of the first error text (HMI) |
| 10 |  | A_MapHelpTextID | WORD | ID of the first help text (HMI) |
| 12 |  | A_TextID2 | WORD | ID of the second error text |
| 14 |  | A_TextLexikonID2 | WORD | ID of the second error text lexicon |
| 16 |  | A_HelpTextLexikonID2 | WORD | ID of the second help text lexicon |
| 18 |  | A_MapTextID2 | WORD | ID of the second error text (HMI) |
| 20 |  | A_MapHelpTextID2 | WORD | ID of the second help text (HMI) |
| 22 |  | A_AlarmID | DWORD | Alarm number |
| 26 |  | A_ValueCount | WORD | Number of further bytes occupied (12) |
| 28 |  | A_AssociatedValue | ARRAY [1 to n]  WORD | Associated values of the alarm  n = A_ValueCount / 2 (= 6) |
| +130 | SubComponent |  |  |  |
| 0 |  | U_SubComponentCount | WORD | Number of subcomponents |
| 2 |  | U_SubComponentFault | ARRAY [1 to n]   BYTE | List of subcomponents  "n" depends on the configuration **) |
|  |  |  |  |  |

*) If the component was deactivated, the index of the requested/actual error is not changed and "E_LastError" is set to "true". The tag area of the alarm is also not filled in.

**) The list of subcomponents is valid only when Q_WithSubComponent is set. The ARRAY has a status byte for each configured component. For a master, the ARRAY contains the status of the configured stations sorted in ascending order according to the station ID. For a station, the ARRAY contains the status of the configured slots sorted in ascending order according to slot number. This field can contain a maximum of 4096 entries (for an IO system): only the actual maximum size is displayed.   
The status byte for each lower-level component is defined as follows:   
Bit 0 = SubFault: the component cannot be reached  
Bit 1 = Fault: the component is not available or is faulty  
Bit 2 = Maintenance1: the component has reported a need for maintenance  
Bit 3 = Maintenance2: the component has reported a need for maintenance  
Bit 4 = Deactivated: the component was deactivated  
Bit 5 = SubFault: a subcomponent is faulty  
Bit 6 = SubMaintenance1: a subcomponent has reported a need for maintenance  
Bit 7 = SubMaintenance2: a subcomponent has reported a need for maintenance

## Displaying settings of system diagnostics (S7-300, S7-400)

### Requirement

You are in the "Common data" folder in the project tree.

### Procedure

To display and edit the settings for system diagnostics, follow these steps:

1. Double-click the "System diagnostics settings" entry.
2. You can view and edit the settings in the system diagnostics.

## Settings (S7-300, S7-400)

This section contains information on the following topics:

- [General settings (S7-300, S7-400)](#general-settings-s7-300-s7-400)
- [Alarm settings (S7-300, S7-400)](#alarm-settings-s7-300-s7-400)
- [Settings for diagnostics support (S7-300, S7-400)](#settings-for-diagnostics-support-s7-300-s7-400)
- [Settings for system diagnostics blocks (S7-300, S7-400)](#settings-for-system-diagnostics-blocks-s7-300-s7-400)

### General settings (S7-300, S7-400)

#### Activate system diagnostics for this PLC

This option is deactivated by default.

> **Note**
>
> When this option is cleared, diagnostics data is also not read out in the Web server and diagnostics viewer, even if the option is selected there.
>
> If you clear this option on a PLC on which it was previously selected, all the diagnostics data is deleted the next time you compile the hardware configuration.

### Alarm settings (S7-300, S7-400)

For the alarm categories listed below, you can define whether an alarm is output and whether or not this alarm requires acknowledgment:

- Error
- Maintenance demanded
- Maintenance required
- Info

To do this, select the relevant options in the "Alarm" and "Acknowledgment" columns.

The set alarm class is displayed in the "Alarm class" column.

The set priority of the alarm class is displayed in the "Priority" column.

### Settings for diagnostics support (S7-300, S7-400)

With the help of diagnostics support, diagnostics data is made available in special status DBs by the diagnostics FB. This can then be displayed graphically, for example on an HMI device.

#### Status DB

Enable the status DB in order to read out the current system status of configured components using this data block.

The following status DB is preset by default:

| Block | Name | Number |
| --- | --- | --- |
| Diagnostics status DB | RSE_DIAGNOSTIC_STATUS_DB | 127 |
|  |  |  |

You can, however, assign a different name and/or number for this block, as long as it is not already being used.

If the "Enable Web server on this module" functionality is enabled in the properties of the CPU, the diagnostics status DB must be enabled. As default, DB 127 is generated if the CPU supports the Web server and if this is enabled in the properties of the CPU.

#### Extended diagnostics settings

This query is only possible if the PLC includes the "D_ACT_DP" instruction.

Enable the option "Query for status "activated/deactivated" after PLC startup" if you want the status of slaves to be queried.

Enable the "Send alarm if status changes from/to activated or deactivated" if you want an alarm to be output when there is a status change. To use this option, execute the "D_ACT_DP" instruction in mode 3/4 and select the diagnostics DB call in OB 86 in the "OB configuration" group.

---

**See also**

[D_ACT_DP: Enable/disable DP slaves (S7-300, S7-400)](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#d_act_dp-enabledisable-dp-slaves-s7-300-s7-400)

### Settings for system diagnostics blocks (S7-300, S7-400)

As default, the following values are set for the system diagnostics blocks:

| Block | Name | Number |
| --- | --- | --- |
| Diagnostics FB | RSE_FB | 49 |
| Diagnostics DB | RSE_DB | 49 |
| first global DB | RSE_GLOBAL_DB | 50 |
| Diagnostics FC | RSE_FC | 49 |

You can, however, assign different numbers and/or names for these blocks as long as they are not already being used.

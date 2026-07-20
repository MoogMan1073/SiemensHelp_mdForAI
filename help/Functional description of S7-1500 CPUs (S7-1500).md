---
title: "Functional description of S7-1500 CPUs (S7-1500)"
package: ProgCPU15enUS
topics: 110
devices: [S7-1500, S7-1500T]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Functional description of S7-1500 CPUs (S7-1500)

This section contains information on the following topics:

- [Operating modes (S7-1500)](#operating-modes-s7-1500)
- [Memory areas (S7-1500)](#memory-areas-s7-1500)
- [I/O data areas (S7-1500)](#io-data-areas-s7-1500)
- [Basics of program execution (S7-1500)](#basics-of-program-execution-s7-1500)
- [Setting the operating behavior (S7-1500)](#setting-the-operating-behavior-s7-1500)
- [Organization blocks (S7-1500)](#organization-blocks-s7-1500)
- [Useful information on CPU firmware versions and STEP 7 versions (S7-1500)](#useful-information-on-cpu-firmware-versions-and-step-7-versions-s7-1500)

## Operating modes (S7-1500)

This section contains information on the following topics:

- [Basics of the operating modes of S7-CPUs (S7-1500)](#basics-of-the-operating-modes-of-s7-cpus-s7-1500)
- [Operating mode transitions (S7-1500)](#operating-mode-transitions-s7-1500)
- ["STARTUP" operating mode (S7-1500)](#startup-operating-mode-s7-1500)
- ["RUN" operating mode (S7-1500)](#run-operating-mode-s7-1500)
- ["STOP" operating mode (S7-1500)](#stop-operating-mode-s7-1500)
- ["HOLD" operating mode (S7-1500)](#hold-operating-mode-s7-1500)
- [Basics of a memory reset (S7-1500)](#basics-of-a-memory-reset-s7-1500)

### Basics of the operating modes of S7-CPUs (S7-1500)

#### Introduction

Operating modes describe the states of the CPU. The following operating modes are possible:

- STARTUP
- RUN
- STOP
- HOLD

In these operating modes, the CPU can communicate via the PN/IE interface, for example.

#### Other operating modes

If the CPU is not ready for operation, it is in one of following two operating modes:

- Off-voltage, in other words, line power is switched off.
- Defective, which means that an internal error has occurred.

  If the "Defective" status is caused by a firmware error, this state is indicated by the status LEDs of the CPU (refer to the description of the CPU in the manuals). Proceed as follows to identify the cause:

  - Turn the power supply switch off and on again.
  - Read out the diagnostics buffer when the CPU starts up and send the data for analysis to Customer Support.

  If the CPU does not start up, replace it.

### Operating mode transitions (S7-1500)

#### Overview

The following figure shows the operating modes and the operating mode transitions of S7-1500 CPUs:

![Overview](images/102598929803_DV_resource.Stream@PNG-en-US.png)

The following table shows the conditions under which the operating modes will change:

| No. | Operating mode transition | Conditions |
| --- | --- | --- |
| ① | POWER ON → STARTUP | After switching on, the CPU goes to "STARTUP" mode if:  - "Warm restart" startup type is set, and - the hardware configuration and the program blocks are consistent.   Non-retentive memory is cleared and the contents of non-retentive DBs are reset to the initial values of the load memory. Retentive memory and retentive DB contents are retained. |
| ② | POWER ON → STOP | When startup type "No startup" is set, the CPU goes to "STOP" mode after the supply voltage is switched on.  Non-retentive memory is cleared and the contents of non-retentive DBs are reset to the initial values of the load memory. Retentive memory and retentive DB contents are retained. |
| ③ | STOP → STARTUP | The CPU switches to "STARTUP" mode if:  - CPU is set to "RUN" from the programming device, and - the hardware configuration and the program blocks are consistent. |
| ④ | STARTUP → STOP | The CPU returns to the "STOP" mode in the following situations:  - Error detected during startup. - The CPU is set to "STOP" from the programming device. - A STOP command is processed in the STARTUP OB. |
| ⑤ | STARTUP → RUN | If the STARTUP is successful, the CPU switches to "RUN". |
| ⑥ | RUN → STOP | The CPU returns to the "STOP" mode in the following situations:  - An error is detected that prevents continued processing. - The CPU is set to "STOP" from the programming device. - A STOP command is processed in the user program. |
| ⑦ | STARTUP → HOLD | Breakpoint in the start-up routine reached. |
| ⑧ | HOLD → STARTUP | Breakpoint in the start-up routine exited by setting to "RUN" from the programming device. |
| ⑨ | RUN → HOLD | Breakpoint reached. |
| ⑩ | HOLD → RUN | Breakpoint exited by setting to "RUN" from the programming device. |
| ⑪ | HOLD → STOP | Operation switch/display or setting the programming device to "STOP". |

---

**See also**

["RUN" operating mode (S7-1500)](#run-operating-mode-s7-1500)
  
["STOP" operating mode (S7-1500)](#stop-operating-mode-s7-1500)
  
["HOLD" operating mode (S7-1500)](#hold-operating-mode-s7-1500)
  
["STARTUP" operating mode (S7-1500)](#startup-operating-mode-s7-1500)

### "STARTUP" operating mode (S7-1500)

This section contains information on the following topics:

- [Basics of "STARTUP" operating mode (S7-1500)](#basics-of-startup-operating-mode-s7-1500)
- [Warm restart (S7-1500)](#warm-restart-s7-1500)
- [STARTUP activities (S7-1500)](#startup-activities-s7-1500)
- [Special features during startup (S7-1500)](#special-features-during-startup-s7-1500)

#### Basics of "STARTUP" operating mode (S7-1500)

##### Function

After turning on the CPU, it executes a startup program before starting to execute the cyclic user program.

By suitably programming startup OBs, you can specify certain initialization variables for your cyclic program in the startup program. There is no rule in terms of the number of startup OBs. That is, you can set up one or several startup OBs in your program or none at all.

##### Parameter settings for startup characteristics

You can specify whether the CPU remains in "STOP" mode or whether a warm restart is performed. Over and above this, you can set the response during startup ("RUN" or previous mode) in the "Startup" group of the CPU properties.

##### Special characteristics

- The CPU resets the process image input.
- All outputs are disabled or respond as configured for the given module: They provide a configured substitute value or retain the last value output and switch the controlled process to a safe operating state.
- Before processing the start-up routine, the CPU transfers the I/O inputs to the process image input.
- After processing the start-up routine, the CPU releases the I/O outputs.

  > **Note**
  >
  > To read the current state of inputs during STARTUP, you can access inputs via the process image or via direct I/O access.  
  > To initialize outputs during STARTUP, you can write values via the process image or via direct I/O access. The values are output to the outputs during the transition to RUN mode.
- The CPU always starts up in warm restart.

  - The non-retentive bit memories, timers and counters are initialized.
  - The non-retentive tags in data blocks are initialized.
- During startup, no cycle time monitoring is running yet.
- The CPU processes the startup OBs in the order of the startup OB numbers. The CPU processes all programmed startup OBs regardless of the selected startup mode (figure "Setting the startup behavior").
- If a corresponding event occurs, the CPU can start the following OBs during startup:

  - OB 82: Diagnostic interrupt
  - OB 83: Removal/insertion of modules
  - OB 86: Rack error
  - OB 121: Programming error (only for global error handling)
  - OB 122: I/O access error (for global error handling only)  
    You can find a description of how to use global and local error handling here: [Overview of mechanisms for error handling](Programming%20basics.md#overview-of-mechanisms-for-error-handling)

  The CPU does not start all the other OBs until the transition to RUN mode.

#### Warm restart (S7-1500)

##### Function

During a warm restart, all non-retentive bit memory is deleted and non-retentive DB contents are reset to the initial values from load memory. Retentive bit memory and retentive DB contents are retained.

Program execution begins at the call of the first startup OB.

##### Triggering a warm restart

You can trigger a "Warm restart" using a corresponding menu command on your programming device in the following situations:

- The CPU must be in "STOP" mode.
- After a memory reset
- After downloading a consistent program and a consistent hardware configuration in the "STOP" mode of the CPU.

"POWER ON" triggers a "warm restart" if you have set the following parameters for the startup response:

- Startup type "warm restart - RUN" (regardless of the CPU operating mode prior to POWER OFF).
- "Warm restart - mode prior to POWER OFF" (depending on the CPU operating mode prior to POWER OFF. The CPU must have been in RUN mode prior to this.)

#### STARTUP activities (S7-1500)

##### Overview

The following table shows which activities the CPU performs at STARTUP:

| Activities in execution sequence | At warm restart |
| --- | --- |
| Clear non-retentive bit memories | yes |
| Clear all bit memories | no |
| Clear the process image output | yes |
| Processing startup OBs | yes |
| Update the process image input | yes |
| Enable outputs after changing to "RUN" mode | yes |

##### Sequence

The following figure shows the activities of the CPU in "STOP", "STARTUP", and "RUN" operating modes.

You can use the following measures to specify the state of the I/O outputs in the first cycle of the user program:

- Use assignable output modules to be able to output substitute values or to retain the last value.
- Set default values for outputs in startup OBs.

During the startup, all interrupt events are entered in a queue so that they can be processed later during RUN mode. In RUN mode, hardware interrupts can be processed at any time.

![Sequence](images/166707801483_DV_resource.Stream@PNG-en-US.png)

#### Special features during startup (S7-1500)

##### Response when expected and actual configurations do not match

The expected configuration is represented by the engineering configuration loaded on the CPU. The actual configuration is the actual configuration of the automation system.

If the preset configuration and actual configuration deviate from one another, the CPU's characteristics are specified by the "Supported hardware compatibility" parameter.

##### Canceling a STARTUP

If errors occur during startup, the startup is canceled and the CPU remains in "STOP" mode.

Under the following conditions, a startup is not performed or canceled:

- If no SIMATIC memory card is inserted or an invalid SIMATIC memory card is inserted.
- If no hardware configuration has been downloaded.

### "RUN" operating mode (S7-1500)

#### Function

In "RUN" mode the cyclic, time-driven and interrupt-driven program sections execute. Addresses that are in the "Automatic Update" process image are automatically updated in each program cycle.

- The process image output is read out.
- The process image input table is read.
- The user program is executed.

Active data exchange between S7-1200 CPUs by means of Open User Communication is only possible in "RUN" mode.

#### Running the user program

Once the CPU has read the inputs, the cyclic program runs from the first to the last instruction.

If you have configured a minimum cycle time, the CPU does not end the cycle until this minimum cycle time is up even if the user program is completed sooner.

A maximum cycle time is set which you can adjust according to your requirements. This ensures that the cyclic program is completed within a specified time. The system responds with a time error if the cyclic program is not completed within this time.

Other events such as hardware and diagnostic interrupts can interrupt the cyclic program flow and prolong the cycle time.

---

**See also**

[Operating mode transitions (S7-1500)](#operating-mode-transitions-s7-1500)

### "STOP" operating mode (S7-1500)

#### Function

In "STOP" mode, the user program is not executed. All outputs are disabled or react according to the parameter settings: They provide a substitute value as set in the parameters or retain the last value output and bring the controlled process to a safe status.

The CPU checks the following points:

- Whether the default settings for the CPU are applicable or parameter sets are present
- Whether the general conditions for the programmed startup characteristics are correct

---

**See also**

[Operating mode transitions (S7-1500)](#operating-mode-transitions-s7-1500)

### "HOLD" operating mode (S7-1500)

#### Function

The "HOLD" operating mode is reached through a breakpoint in a block that you are testing in single step mode. The single step mode test function is available in the STL and SCL programming languages.

In "HOLD" operating mode, events are not initiated and the user program is not executed.

All outputs are disabled or react according to the parameter settings: Outputs supply a configured substitute value or keep the last value output and bring the controlled process to a safe operating state.

Timers and watchdogs are stopped. The timers for time-driven events are stopped.

In HOLD operating state, hardware interrupt OBs are not started by external interrupt triggers (e.g. hardware interrupt input).

The system time continues running.

At a POWER OFF > POWER ON transition while in HOLD mode, the CPU goes to STOP mode and remains in this state. In this case, the CPU does not perform an automatic startup.

When the user program reaches a breakpoint, the cycle monitoring time is stopped. When the breakpoint is exited again, the monitoring time restarts.

Errors that trigger a STOP of the CPU in RUN mode also do so in HOLD mode.

---

**See also**

[Operating mode transitions (S7-1500)](#operating-mode-transitions-s7-1500)

### Basics of a memory reset (S7-1500)

#### Function

A memory reset on the CPU is possible only in "STOP" mode.

When memory is reset, the CPU is changed to an "initial status". This means:

- An existing online connection between the PG/PC and the CPU is disconnected.
- The content of the work memory and the retentive and non-retentive data are deleted.
- The diagnostic buffer, time of day, and IP address are retained.
- The CPU is then initialized with the loaded project data (hardware configuration, code and data blocks, force jobs). These data are copied from the load memory to the work memory.

  Result:

  - If an IP address was set in the hardware configuration ("Set IP address in the project" option), this IP address is valid after the memory reset.
  - Data blocks no longer have current values but rather their configured start values.
  - Force jobs remain active

## Memory areas (S7-1500)

This section contains information on the following topics:

- [What you need to know about SIMATIC memory cards (S7-1500)](#what-you-need-to-know-about-simatic-memory-cards-s7-1500)
- [CPU memory areas (S7-1500)](#cpu-memory-areas-s7-1500)
- [Retentive memory areas (S7-1500)](#retentive-memory-areas-s7-1500)
- [Summary of retentive behavior (S7-1500)](#summary-of-retentive-behavior-s7-1500)
- [Memory behavior when loading software changes (S7-1500)](#memory-behavior-when-loading-software-changes-s7-1500)

### What you need to know about SIMATIC memory cards (S7-1500)

#### Function of the SIMATIC memory card

The SIMATIC memory card for an S7-1500 is an SD memory card, preformatted by Siemens for the CPU user program, that is compatible with the Windows operating system.

![Function of the SIMATIC memory card](images/86789090571_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Formatting the SIMATIC memory card**  You may only delete files and folders. If you format the SIMATIC memory card with Windows tools, for example with a commercially available card reader, you will render the memory card unusable as a storage medium for an S7 CPU. |  |

#### Setting the card type

You can use the SIMATIC memory card as a program card or as a firmware update card.

To set the card type, insert the SIMATIC memory card into the card reader of the programming device and select the "Card reader/USB memory" folder from the project tree. In the properties of the selected memory card, designate the card type:

- Program

  You use a program card as an external load memory for the CPU. It contains the entire user program for the CPU. The user program is transferred to the work memory and runs there. If the SIMATIC memory card with the user program is removed, the program is no longer available.

  Directory: SIMATIC.S7S
- Firmware card

  Firmware for the S7-1500 modules can be stored on a SIMATIC memory card. It is therefore possible to perform a firmware update with the help of a specifically prepared SIMATIC memory card.

  Directory: FWUPDATE.S7S

#### Folders and files on the SIMATIC memory card

The following folders and files can be found on the SIMATIC memory card:

| Folder | Description |
| --- | --- |
| FWUPDATE.S7S | Firmware update files for CPU and I/O modules |
| SIMATIC.S7S | User program, meaning all blocks (OBs, FCs, FBs, DBs) and system blocks, project data of the CPU |
| SINAMICS.S7S | If "SINAMICS Integrated" is configured: Project data of SINAMICS Integrated. The folder structure below the SINAMICS.S7S folder is based on the structure of a SINAMICS S120 memory card |
| SIMATIC.HMI | HMI-relevant data |
| SET_PWD.S7S | Folder for "SET PASSWORD" job file |
| MCRC | "Motion Control Runtime Component" folder for Motion Control UPD files |
| DEVICE_INFO.S7S | Folder for device information (DEVICE INFORMATION) |
| DataLogs | DataLog files |
| Recipes | Recipe files |
| UserFiles | User data |
| Backups | Files for backing up and restoring via the display |
| DUMP.S7S | Service data files |

The content of the "DataLogs", "Recipes" and "UserFiles" folders is also loaded when the device is loaded as a new station into the STEP 7 project (as of TIA Portal V15.1). The files are located in the project path under "AdditionalFiles/MemoryCards/<Name of the PLC>". You can find further information on DataLogs and recipe files in the chapter "[Recipes and Data Logging](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#recipes-and-data-logging-s7-1200-s7-1500)".

The following data structure exists on the SIMATIC memory card:

| File type | Description |
| --- | --- |
| S7_JOB.S7S | Job file |
| SIMATIC.HMI\Backup\*.psb | Panel backup files |
| SIMATICHMI_Backups_DMS.bin | Protected file (required to use panel backup files in STEP 7) |
| __LOG__ | Protected system file (required in order to use the card) |
| crdinfo.bin | Protected system file (required in order to use the card) |
| PWD.TXT | File in the SET_PWD.S7S folder for "SET PASSWORD" job |
| *.pdf, *.txt, *.csv, ... | Additional files with different formats that you can also store in folders of the SIMATIC memory card.  Only if you have saved these files in a folder by the name "UserFiles", are they stored when loading the device as a new station in the STEP 7 project. |

#### Transferring objects from the project to a SIMATIC memory card

When the SIMATIC memory card is inserted in the programming device or in an external card reader, you can transfer the following objects from the project tree to the SIMATIC memory card:

- Individual blocks (multiple selection possible)

  In this case a consistent transfer is available, as the dependencies of the blocks to each other is taken into account with block selection.
- PLC

  In this case, all objects relevant to processing, such as blocks and the hardware configuration, are transferred to the SIMATIC memory card, just as with downloading.

To perform the transfer, you can move the objects with drag-and-drop or use the command "Card reader/USB memory > Write to memory card" in the "Project" menu.

#### Saving user data on a SIMATIC memory card

You transfer user files, such as PDF files for project documentation, onto the SIMATIC memory card by manually creating a folder called "UserFiles" on the memory card and saving your files in this folder. Only files in this folder (*.pdf, *.txt, *.csv, etc) are also loaded into the STEP 7 project when loading the device as a new station. The "UserFiles" folder can be used for restoring in the case of a memory card or CPU failure.

After being loaded from the memory card, the "UserFiles" folder with the files contained in it is saved in the project tree in the "AdditionalFiles > MemoryCards > [Name of the CPU]" directory.

If the folder "[Name of the CPU]" already exists, as is the case in reloading from the memory card, the folder in the project tree is overwritten by the data from the memory card.

#### Transferring objects from the SIMATIC memory card to the project

You transfer objects by selecting the SIMATIC memory card symbol in the project tree and then dragging it to a CPU in the project. The contents of the SIMATIC memory card must correspond to the CPU type in the project tree. If blocks existed beforehand, these are deleted prior to the transfer.

#### Updating firmware with a SIMATIC memory card

You can get the latest firmware data on the Internet from the Service & Support pages:

http://support.automation.siemens.com

Save the firmware files on the hard disk and plug the SIMATIC Memory Card into the card reader of your programming device.

To store the file on the SIMATIC memory card, select the memory card in the "Card Reader/USB memory" folder in the project tree. Select the shortcut menu "Card Reader/USB memory > Create firmware update memory card".

Then follow the instructions for performing the firmware update in the Service & Support portal or in the S7-1500 system manual.

Updating the firmware provides the module, for example, CPU or I/O module, with a new firmware version. If you have used the module in the project, you must replace the already configured module with the new firmware version offline by means of module replacement and adapt and then load the program or configuration.

#### Diagnosing manipulation of SIMATIC memory cards

If a CPU has been out of operation for a time, it may not be possible to rule out manipulation of the SIMATIC memory card. The program may function differently to before the CPU was taken out of operation.

S7-1500 CPU as of firmware version 2.0 are capable of diagnosing the following manipulation, and enter these events during startup as a security event in the diagnostics buffer:

- The project on the SIMATIC memory card has changed (the SIMATIC memory card remains the same)
- The SIMATIC memory card was replaced by another memory card

#### Integrity protection of the SIMATIC Memory Card as of CPU FW version V3.1

With CPUs as of FW version V3.1, the integrity protection of the SIMATIC Memory Card depends on the password for protecting confidential configuration data that you assigned during the configuration of the CPU. This results in the following changes when using SIMATIC Memory Cards:

- To transfer a CPU to a card reader/USB memory device via drag and drop:  
  for CPUs as of FW version V3.1, you need to enter the password of the CPU you want to use with the SIMATIC Memory Card. If you enter an incorrect password, the CPU will not start up after power on and will report the contents of the SIMATIC Memory Card as faulty.
- To insert a CPU from a card reader/USB memory device:  
  In order to be able to verify the integrity of the included configuration in STEP 7, you must enter the password of the CPU from which the project was loaded. In this case, STEP 7 checks the data on the SIMATIC Memory Card and reports potential damage.   
  Entering the password is optional. If you want to skip the integrity check, you don't need to enter the password (restore project).

#### Service life of SIMATIC memory cards

The service life of SIMATIC memory cards is limited and depends on the following factors, among others:

- Capacity of the SIMATIC memory card
- Frequency of writing operations
- Amount of data written to the SIMATIC memory card.

Write or delete processes, particularly cyclic write/delete processes via the user program to the SIMATIC memory card, reduce its service life.

Cyclic execution of the instructions "CREATE_DB" (with "Create DB in load memory" attribute), "DataLogWrite", "RecipeExport", "RecipeImport" and setting the time zone "SET_TIMEZONE" reduce the service life of the memory card depending on the number or write processes and data.

In addition to the cyclic write/delete processes, writing or deleting very large amounts of data also has a negative impact on the service life of the SIMATIC memory card.

You can find a description of how to estimate the service life of SIMATIC memory cards for S7-1500 CPUs, ET 200SP CPUs and ET 200Pro CPUs in the following entry:

[SIMATIC S7-1500 structure and use of the CPU memory](https://support.industry.siemens.com/cs/ww/en/view/59193101)

For S7-1200 CPUs, you can find the information under the following entry:

[SIMATIC S7 S7-1200 Automation System](https://support.industry.siemens.com/cs/ww/en/view/109478121)

You have the option of configuring a service life percentage in the CPU properties so that the CPU generates a diagnostic interrupt and a diagnostic buffer entry (maintenance event) after expiration of the configured service life percentage. This will give you ample time to replace the SIMATIC memory card before it becomes unusable because the maximum number of write access operations has been reached.

Use the instruction "[GetSMCinfo](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#getsmcinfo-reading-out-information-about-the-simatic-memory-card-s7-1200-s7-1500)" to retrieve information about the inserted SIMATIC memory card. You select the information you wish to retrieve with the "Mode" parameter, for example:

- Mode = 2: Percentage of service life used so far (in %)
- Mode = 3: Configured percentage of service life after which the CPU enters a maintenance event in the diagnostic buffer and turns on the Maintenance LED.

#### Force jobs on the SIMATIC memory card

Note that a force job stored on the SIMATIC Memory Card is executed on every CPU into which this SIMATIC Memory Card is inserted. If you do not want this to happen, terminate the force job before you insert the SIMATIC memory card into a different CPU.

---

**See also**

[Assign password via SIMATIC Memory Card (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#assign-password-via-simatic-memory-card-s7-1200-s7-1500-s7-1500t)
  
[What you should know about group alarms for security events (S7-1500)](#what-you-should-know-about-group-alarms-for-security-events-s7-1500)
  
[Displaying properties of memory cards](Editing%20project%20data.md#displaying-properties-of-memory-cards)

### CPU memory areas (S7-1500)

#### Memory areas of the S7-1500 CPUs

The following figure shows the CPU memory areas and the load memory on the SIMATIC memory card. In addition to the load memory, the SIMATIC memory card may contain other data, such as recipes, Data Logs, HMI backups.

![Memory areas of the S7-1500 CPUs](images/41338793227_DV_resource.Stream@PNG-en-US.png)

#### Load memory

The load memory is a non-volatile memory for program code, data blocks and hardware configuration. When these objects are loaded to the CPU, they are first stored in the load memory. This memory is located on the SIMATIC memory card. A SIMATIC memory card must be inserted in order for the CPU to operate.

#### Work memory

The work memory is volatile memory that contains the code and data blocks. The work memory is integrated in the CPU and cannot be extended.

The work memory in the S7-1500 is divided into two areas:

- Code work memory for runtime-relevant parts of the program code.
- Data work memory for runtime-relevant parts of data blocks and technology objects. At the operating mode transitions POWER ON → startup and STOP → startup, tags from global data blocks, instance data blocks, and technology objects are initialized with their start values. Retentive tags retain their actual values that were saved in the retentive memory.

#### Retentive memory

Retentive memory is a non-volatile memory for storing a limited amount of data in the event of a power failure. The tags and operand areas that have been defined as retentive are saved in the retentive memory.

This data is retained after a power-off or power failure. All other tags are lost and are set to their start values during the operating mode transitions startup after POWER ON and startup after STOP.

The contents of the retentive memory are deleted by the following actions:

- Memory reset
- Reset to factory settings

Specific tags of technology objects are also stored in the retentive memory. These tags are not deleted during memory reset.

#### Other memory areas

The CPU has other memory areas in addition to those described for the user program and data.

These areas include the following runtime-relevant areas:

- Bit memory, timers, counters
- Temporary local data
- Process images

The relevant CPU-specific variables can be found in the CPU's technical specifications.

#### Information on memory areas

You can view information offline and online via the memory areas of your S7-1500 CPU.

**Offline**:

During the creation or modification of a program, you can determine whether or not it is too large for a specific CPU. You can find this information, for example, under "Program information" in the project tree. In the "Resources" tab, you will find information on the overall size of the memory areas and on the memory space already allocated. At this location, you can also find information on the inputs and outputs that are already assigned.

For the S7-1500, you can specify the total size of the load memory (program information; the Load memory - total box is a drop down list for selecting the load memory size).

**Online**:

Start "Online & Diagnostics" in the project navigation. The "Memory" function provides information on the fill level of all the CPU's memories.

Additional information on your CPU's resources can be found in the "Assignment list" and "Call structure" tabs of the program information as well as in the PLC tag table.

---

**See also**

[Overview of available program information](Displaying%20program%20information.md#overview-of-available-program-information)
  
[Showing fill levels of all types of memory on a CPU](Device%20and%20network%20diagnostics.md#showing-fill-levels-of-all-types-of-memory-on-a-cpu)

### Retentive memory areas (S7-1500)

#### Introduction

The S7-1500 CPUs have a retentive memory for storing retentive data in the event of a POWER OFF. The size of the retentive memory is documented in the CPU's technical specifications.

The utilization of the retentive memory of the configured CPU can be found offline in the project tree under "Program information > Resources" or online in the project tree under "Online & Diagnostics > Diagnostics > Memory".

If you define data as retentive, their content is retained after a power failure, during CPU startup, and when a modified program is loaded.

The following data and objects can be defined as retentive:

- Bit memory, timers, counters
- Tags of global data blocks
- Tags of instance data blocks of a function block

Certain tags of technology objects are always retentive, for example, calibration values of absolute encoders.

#### Bit memory, timers, counters

In the PLC tag table, you use the "Retain" button to define the number of retentive bit memories, timers and counters.

#### Tags of a global data block

Depending on the access settings, you can define either individual tags or all tags of a global data block as retentive in a global data block:

- Optimized block access enabled: retentivity can be set for each individual tag.
- Optimized block access disabled: The retain setting applies to all tags of the DB; either all or none of the tags are retentive.

#### Instance data block (function block) tags

You can define the tags of a function block's instance data block as retentive. Depending on the access to the instance data block, you can define the following for individual tags or for all tags of the block jointly:

- Optimized block access enabled: You can define individual tags as retentive in both the interface of the function block and in the assigned instance data block.
- Optimized block access disabled: You can define retentivity for all tags together in the instance data block.

#### Creating a data block in the user program

The instruction "Create_DB" is used to create a data block. Depending on the selection for the ATTRIB parameter, the generated data block either has the property "retentive" or "non-retentive". In this case, it is not possible to set the retentivity for individual tags.

#### Technology object tags

Certain tags of technology objects are also retentive, for example, calibration values of absolute encoders. STEP 7 manages the retentivity of the technology objects automatically. Hence, it is not necessary to configure retentivity for these. These tags are not affected by a memory reset and can only be deleted by resetting to factory settings.

#### Tip: Detect loss of retentivity in the startup OB and cyclic OBs

All tags (bit memories, timers, counters, DB content) of a user program lose their retentivity in the following case:

1. You plug the SIMATIC memory card with project (user program) into the card reader of your programming device.
2. You change the size of data blocks in the associated project or add data blocks with retentive tags to the associated project.
3. You transfer the changed project back to the SIMATIC memory card in the card reader.
4. You start the CPU with the changed project.

All tags (bit memories, timers, counters, DB content) of a user program lose their retentivity due to the offline changes. The tags are assigned their initial values after the STOP-RUN transition.

To react to a loss of retentivity in the user program, evaluate the following local tags of the start information:

- Startup OB: LostRetentive (true in case of loss of retentivity)
- Cyclic OBs Remanence (true if retentive data are available)

---

**See also**

[Using extended retentive data area with PS 60W 24/48/60VDC HF (S7-1500)](Configuring%20automation%20systems.md#using-extended-retentive-data-area-with-ps-60w-244860vdc-hf-s7-1500)

### Summary of retentive behavior (S7-1500)

#### Retentive characteristics of the memory objects

In addition to the retentive memory areas described, there are other objects with retentive characteristics, for example, the diagnostic buffer. These objects do not occupy retentive memory.

The following table shows the retentive characteristics of the memory objects:

- in the operating mode transitions STOP → Startup and POWER OFF → Startup
- in the memory-influencing functions Memory reset and Reset to factory settings

Retentive characteristics of memory objects ("x" = content is retained; "-" = content is initialized)

| Memory object | Operating mode transitions |  | Memory reset | Reset to factory settings |
| --- | --- | --- | --- | --- |
| STOP → STARTUP | POWER OFF → STARTUP |  |  |  |
| Actual values of the data blocks, instance data blocks | Can be set in the properties of the DB. |  | - | - |
| Bit memories, timers and counters - configured as retentive | x | x | - | - |
| Bit memories, timers and counters - configured as non-retentive | - | - | - | - |
| Certain retentive tags from technology objects (for example, adjustment values of absolute encoders) | x |  | x | - |
| Diagnostic buffer (retentive area) | x | x | x | - |
| Diagnostic buffer entries (non-retentive area) | x | - | - | - |
| Runtime meters | x | x | x | - |
| Time-of-day | x | x | x | - |

#### Diagnostics buffer

Part of the diagnostic buffer of S7-1500 CPUs is retentive. The most recent entries in the diagnostic buffer are retained after a power failure or memory reset. The retentive part of the diagnostic buffer can only be deleted by resetting to factory settings. The number of retentive diagnostic buffer entries depends on the CPU. The entries in the diagnostic buffer do not require retentive memory.

#### Runtime meters

The runtime meter of S7-1500 CPUs is retentive and not affected by a memory reset. After a reset to factory settings, it is set to zero.

#### Time-of-day

The time-of-day of S7-1500 CPUs is retentive and not affected by memory reset. After a reset to factory settings, the time-of-day is set to 01/01/2012 00:00:00.

### Memory behavior when loading software changes (S7-1500)

#### Introduction

In the STOP and RUN modes of the CPU, the S7-1500 CPU offers you the option of loading changes to the software without affecting the actual values of already loaded tags during the download operation.

In STEP 7, you load changes to the software under "Download to device > Software (changes only)".

#### Impact of software changes on PLC tags

You can load the following software changes, **without** affecting the actual values of tags that have already been loaded:

- Changing names
- Changing comments
- Adding new tags
- Deleting tags
- Changing retentivity settings for bit memories, times, and counters.

The actual values are affected by loading the following software changes:

- Changing data types
- Changing addresses

#### Impacts of software changes on data blocks with memory reserve

If you are using memory reserve for data blocks ("Optimized block access" attribute and "Download without reinitialization" button activated), you can load the following software changes **without** the actual values of already loaded tags being reinitialized.

- Changing start values
- Changing comments
- Adding new tags

To load the following software changes, you must deactivate the "Download without reinitialization" button. During the next load, all actual values of the data block will be reinitialized:

- Changing names
- Changing data types
- Changing retentivity settings
- Deleting tags
- Changes to the memory reserve settings

#### Impacts of software changes on data blocks without memory reserve

If you are not using memory reserve, you can load the following software changes, without affecting the actual values of tags that have already been loaded:

- Changing start values
- Changing comments

When loading the following software changes, all actual values of the data block will be reinitialized:

- Changing names
- Changing data types
- Changing retentivity settings
- Adding new tags
- Deleting tags

#### Memory reserve of data blocks

Each function block or data block with the activated attribute "Optimized block access" contains a memory reserve by default which you may use for subsequent interface changes. The memory reserve is initially not used. When you have compiled and loaded the block, and then observe that you want to reload interface changes, activate the memory reserve. All tags that you subsequently declare will be placed in the memory reserve. During the next load the new tags will be initialized to their start values; the previously loaded tags will not be reinitialized.

The setting for memory reserve can be found in the data block properties under "Download without reinitialization".

#### Memory requirements when loading software changes in RUN

For the consistent and atomic handling of the entire load procedure, the CPU requires adequate free memory space on the SIMATIC memory card. The files affected by loading the software changes on the CPU are only deleted after the new files have been created. This SIMATIC memory card therefore requires memory space corresponding approximately to the space required for all program objects on the memory card.

You will find information and tips on handling software changes in the manual "Structure and use of the CPU memory".

## I/O data areas (S7-1500)

This section contains information on the following topics:

- [Access to the I/O addresses (S7-1500)](#access-to-the-io-addresses-s7-1500)
- [Start address of a module (S7-1500)](#start-address-of-a-module-s7-1500)
- [Evaluating the value status (S7-1500)](#evaluating-the-value-status-s7-1500)
- [Example for evaluating the value status (S7-1500)](#example-for-evaluating-the-value-status-s7-1500)

### Access to the I/O addresses (S7-1500)

#### I/O addresses

If you insert a module in the device view, its user data is located in the process image of the S7-1500-CPU (default). The CPU handles the data exchange between the module and the process image area automatically during the update of the process images.

Append the suffix ":P" to the I/O address if you want the program to access the module directly instead of using the process image.

![I/O addresses](images/42112836235_DV_resource.Stream@PNG-en-US.png)

Direct I/O access does not improve performance for S7-1500 CPUs, however. Where possible, you should therefore use process images or process image partitions to address the I/O.

### Start address of a module (S7-1500)

#### Definition

The start address is the lowest byte address of a module. It acts as the initial address of the module user data area.

#### Configuring module start addresses

The addresses used in the user program and the module start addresses are coordinated when the modules are configured.

In the module properties ("I/O addresses" group), you can change the start addresses that were assigned automatically when the modules were inserted.

You can also set whether the addresses are located in the process image or in which process image partition they are located.

In addition to the process image partition, you can also select the organization block to which the process image partition is assigned. With the exception of the isochronous interrupt OB, the associated process image partition is updated when the assigned OB is called. Immediately before the beginning of the OB start, the process image partition of the inputs is updated. Immediately after the end of the OB, the process image partition of the outputs is transferred to the modules.

Select the "Automatic update" process image if the process image in which the addresses of the module are located is to be updated automatically at the cycle control point.

### Evaluating the value status (S7-1500)

#### Introduction

Value status (QI, quality information) refers to diagnostic information of I/O channels that is made available to the user program via the process image inputs (PII). The value status is transferred synchronously with the user data.

Each bit of the value status is assigned to a channel and provides information on the validity of the value (0 = value is incorrect).

For example, if there is a wire break at a digital input, the user data signal is logically "0". The module also sets the associated bit in the value status to 0 due to the wire break diagnostics, which means you have the option to determine that the value is invalid by querying the value status.

The assignment of the value status bytes in the process image inputs depends on the module used. Detailed information can be found in the manual for the relevant I/O module.

Summary: Possible cause for value status = 0:

- The supply voltage L+ is missing at the terminals or is not sufficient
- A channel has been deactivated
- Outputs are inactive (e.g. CPU in STOP)
- An output channel uses technology functions (HSC, PWM or PTO); see below

#### Enable value status

If you want to evaluate the value status of the channel, select the "Value status" check box in the properties of the I/O module. By activating the value status, additional addresses are assigned for the value status in the process image inputs (PIIs). For input modules, STEP 7 assigns the input addresses directly following the user data; for output modules, the next available input addresses are assigned.

#### Special features for modules with MSI/MSO

Requirement:

- GSD file for I/O modules with MSI/MSO
- IO device supports MSI/MSO (e.g., IM 155-5 PN ST firmware version V2.0.0 or higher)

The value status has the following meaning for modules with diagnostic capability for which you have configured a module-internal Shared Input (MSI) or module-internal Shared Output (MSO):

**MSI**:

For the 1st submodule (=basic submodule), the value status 0 indicates that the value is incorrect.

For the 2nd to 4th submodule (=MSI submodule), the value status 0 indicates that the value is incorrect or the basic submodule has not yet been assigned parameters (not ready).

**MSO**:

For the 1st submodule (=basic submodule), the value status 1 indicates that the output value specified by the user program is actually output at the module terminal.

Possible causes for value status = 0:

- Value is incorrect, for example, because the supply voltage is missing.
- IO controller of basic submodule is in STOP.

For the 2nd to 4th submodule (=MSO submodule), the value status 1 indicates that the output value specified by the user program is actually output at the module terminal.

Possible causes for value status = 0:

- Value is incorrect, for example, because the supply voltage is missing.
- IO controller of basic submodule is in STOP.
- The basic submodule parameters have not yet been assigned.

#### Behavior of the value status at the output channels for technology functions with compact CPUs, such as CPU 1511C-1 PN

The CPU 1511C-1 PN supports the value status (QI) for the channels of the analog and digital on-board I/O.

The value status is not supported by the output channels you are using for technology functions (HSC, PWM or PTO).

Therefore, the QI bits always output the value status 0 ("Bad") at the output channels for technology functions. It does not matter in this context whether the output value is incorrect or not.

---

**See also**

[Cyclic OBs (S7-1500)](#cyclic-obs-s7-1500)
  
[Module-internal shared input/shared output (MSI/MSO)](http://support.automation.siemens.com/WW/view/en/68052815)
  
[System diagnostics](http://support.automation.siemens.com/WW/view/en/68052815)
  
[Example for evaluating the value status (S7-1500)](#example-for-evaluating-the-value-status-s7-1500)

### Example for evaluating the value status (S7-1500)

The DI 32x24VDC HF module of the S7-1500 can be configured in STEP 7 (device view) for various applications. Depending on the configuration, additional/different addresses are assigned in the process image input.

This example shows various configurations with their respective assigned value status and describes the effect on the address assignment.

#### Configuration options of DI 32x24VDC HF

The following configurations are possible:

- 1 x 32-channel without value status
- 1 x 32-channel with value status
- 4 x 8-channel without value status
- 4 x 8-channel with value status
- 1 x 32-channel with value status for module-internal shared input (MSI) with up to 4 submodules

An additional bit for the value status is assigned to each channel in the configurations with value status. The value status bit indicates if the read in digital value is valid. (0 = value is incorrect).

#### Address space for configuration as 32-channel DI 32x24VDC HF with value status

The preset DI configuration is retained initially (32 channels, neither division into submodules nor module-internal shared input (MSI) configuration); however, the value status is to be enabled.

- Select the "Enable value status" check box in the "DI configuration" area in the module properties (Inspector window).

The following figure shows the assignment of the address space for the configuration as a 32-channel module with value status. You can freely assign the start address for the module. The addresses of the channels are derived from the start address.

**Example**: Start address 2 (input byte 2), end address 9 (input byte 9).

STEP 7 automatically reserves the addresses for the input values (4 bytes) and the subsequent addresses for the value status (also 4 bytes) so that the following address assignment results:

![Address space for configuration as 32-channel DI 32x24VDC HF with value status](images/61585900171_DV_resource.Stream@PNG-en-US.png)

#### Address space for configuration as 4 x 8-channel DI 32x24VDC HF with value status

The DI configuration is to be adapted so that the 32 channels of the DI 32x24VDC HF module of the S7-1500 are divided among four submodules with 8 channels each. The submodules can be assigned to different IO controllers when the module is used in a shared device. The value status is also to be enabled in this case.

- Select the submodule configuration "4 submodules with 8 digital inputs" in the "DI configuration" area in the module properties (Inspector window).
- Select the "Enable value status" check box.

The 4 submodules appear with their own name (e.g., DI 32x24VDC BA_1) in the area navigation of the Inspector window.

Contrary to the 1 x 32-channel module configuration, each of the four submodules has a freely assignable start address.

**Example**: The start addresses are assigned as follows:

- 1. Submodule: 10
- 2. Submodule: 20
- 3. Submodule 30
- 4. Submodule 40

STEP 7 automatically reserves a byte for the value status for each submodule. The byte for the value status has the address "Start address+1" so that the following address assignment results:

![Address space for configuration as 4 x 8-channel DI 32x24VDC HF with value status](images/61585904523_DV_resource.Stream@PNG-en-US.png)

#### Address space for configuration as 1 x 32-channel DI 32x24VDC HF with MSI and value status

The configuration shown here uses the "Module-internal shared input (MSI)" function. This function allows simultaneous reading of the input values by various IO controllers (CPUs) when the module is used in a shared device (ET 200MP).

The channels 0 to 31 of the module are copied in up to 4 submodules with configuration 1 x 32-channel module with module-internal shared input (MSI). Channels 0 to 31 are then available with identical input values in different submodules. These submodules can be assigned to up to four IO controllers when the module is used in a sShared device. Each IO controller has read access to the same channels ("listening in").

The number of usable submodules (= copies of the inputs) depends on the interface module used. Observe the information regarding this in the device manual of the particular interface module.

- Select the following options in the "DI configuration" area in the module properties (Inspector window):

  - For "Subdivision of module": None
  - For "Copies of module": One additional copy of the inputs

    This setting enables one additional IO controller to read the inputs of the module.

The value status is enabled automatically for MSI configurations (cannot be changed). The reason for this setting is that an IO controller of the shared device that is "listening in" can determine from the value status whether or not the module is ready for operation and providing valid values.

Below, the submodules that result from the above-described settings are named as follows:

- Basic submodule: That is the submodule assigned to the parameter-assigning IO controller. Only the parameter-assigning IO controller has access to module diagnostics and receives hardware interrupts.
- MSI submodule: That is the submodule assigned to an IO controller that is "listening in". The IO controller that is listening in does not have access to module diagnostics and only receives information on the validity of the input values by the value status.

**Value status (Quality Information, QI)**

The meaning of the value status depends on the submodule to which it pertains.

For the first submodule (=basic submodule), the value status 0 indicates that the value is incorrect.

For the 2nd to 4th submodule (=MSI submodule or copy of inputs), the value status 0 indicates that the value is incorrect or that the basic submodule parameters have not yet been assigned (not ready for operation).

**Example**: The DI 32x24VDC HF module is configured as described above (an additional copy of the inputs). A basic submodule and one MSI submodule result.

The basic submodule receives the start address 10, and the MSI submodule receives the start address 100 in this example. The address of the MSI submodule is not relevant for the IO controller because this submodule will be assigned to another IO controller later in the shared device configuration process and will disappear from the address space of the parameter-assigning IO controller as a result.

The following figure shows the assignment of the address space with submodules 1 and 2 and the value status. All submodules are initially assigned to the IO controller.

![Address space for configuration as 1 x 32-channel DI 32x24VDC HF with MSI and value status](images/61585908875_DV_resource.Stream@PNG-en-US.png)

#### Additional information

Additional information and a programming example for the evaluation of the value status are available [here](http://support.automation.siemens.com/WW/view/en/59192926).

---

**See also**

[Evaluating the value status (S7-1500)](#evaluating-the-value-status-s7-1500)

## Basics of program execution (S7-1500)

This section contains information on the following topics:

- [English designations of the OB types (S7-1500)](#english-designations-of-the-ob-types-s7-1500)
- [Events and OBs (S7-1500)](#events-and-obs-s7-1500)
- [CPU overload behavior (S7-1500)](#cpu-overload-behavior-s7-1500)
- [Example of a hardware interrupt event (S7-1500)](#example-of-a-hardware-interrupt-event-s7-1500)

### English designations of the OB types (S7-1500)

#### English designation of the OB types

When an OB is created in the "Add new block" dialog, the OB types can only be displayed in English for technical reasons – irrespective of the set user interface language. In order to facilitate handling, the following table lists the English terms and their corresponding designations in the set user interface language.

| English designation of the OB type in the "Add new block" dialog. | Designation in the information system |
| --- | --- |
| ProgramCycle | Cycle OB, OB for cyclic program processing, cyclic program |
| Startup | Startup OB |
| TimeDelayInterrupt | Time-delay interrupt OB |
| CyclicInterrupt | Cyclic interrupt OB |
| HardwareInterrupt | Hardware interrupt OB |
| TimeErrorInterrupt | Time error OB |
| DiagnosticErrorInterrupt | Diagnostic interrupt OB |
| PullOrPlugOfModules | Pull/plug interrupt OB |
| RackOrStationFailure | Rack failure OB |
| ProgrammingError | Programming error OB |
| IO_AccessError | I/O access error OB |
| TimeOfDay | Time-of-day interrupt OB |
| CPU_RedundancyError | CPU redundancy error OB |
| IO_RedundancyError | I/O redundancy error OB |
| MC_Interpolator | MC-Interpolator OB |
| MC_Servo | MC-Servo OB |
| MC_PreServo | MC-PreServo OB |
| MC_PostServo | MC-PostServo OB |
| MC_PreInterpolator | MC-PreInterpolator-OB |
| MC_LookAhead | MC-LookAhead-OB |
| MC_Transformation | MC-Transformation OB |
| SynchronousCycle | Isochronous mode interrupt OB |
| Status | Status interrupt OB |
| Update | Update interrupt OB |
| Profile | OB for vendor or profile-specific interrupt |

### Events and OBs (S7-1500)

#### OB start events

An OB start event causes the following reaction when it occurs:

- If the event comes from an event source to which you have assigned an OB, it triggers the execution of the assigned OB. This means that the event is positioned in a queue according to its priority.
- If the event comes from an event source to which you have not assigned an OB, the default system reaction is executed.

  > **Note**
  >
  > Some event sources, such as startup, pull/plug, exist even if you do not configure them.

The following table provides an overview of the OB start events, including the possible values for OB priority, possible OB numbers, default system reaction and number of OBs. The table is sorted based on the default OB priority. Priority class 1 is the lowest.

| Types of event sources | Possible priorities (default priority) | Possible  OB numbers | Default system reaction | Number of supported OBs |
| --- | --- | --- | --- | --- |
| Startup | 1 | 100, >= 123 | Ignore | 100 |
| Cyclic program | 1 | 1, >= 123 | Ignore | 100 |
| Time-of-day interrupt | 2 to 24 (2) | 10 to 17, >= 123 | Not applicable | 20 |
| Status interrupt | 2 to 24 (4) | 55 | Ignore | 1 |
| Update interrupt | 2 to 24 (4) | 56 | Ignore | 1 |
| Manufacturer- or profile-specific interrupt | 2 to 24 (4) | 57 | Ignore | 1 |
| Time-delay interrupt | 2 to 24 (3) | 20 to 23, >= 123 | Not applicable | 20 |
| Cyclic interrupt | 2 to 24 (8 to 17, depending on the cycle time) | 30 to 38, >= 123 | Not applicable | 20 |
| Hardware interrupt | 2 to 26 (16) | 40 to 47, >= 123 | Ignore | 50 |
| Isochronous mode interrupt | 16 to 26 (21) | 61 to 64, >= 123 | Ignore | 20 (one per isochronous interface) |
| I/O redundancy error (only with H and HF CPUs) | 2 to 26 (6) | 70 | Ignore | 1 |
| CPU redundancy error (for R/H-CPUs only) | 2 to 26 (26) | 72 | Ignore | 1 |
| MC-Interpolator | 16 to 25 (24) | 92 | Not applicable | 1 |
| MC-Servo | 17 to 26 (26) | 91 | Not applicable | 1 |
| MC-PreServo | Corresponds to MC-Servo | 67 | Not applicable | 1 |
| MC-PostServo | Corresponds to MC-Servo | 95 | Not applicable | 1 |
| MC PreInterpolator | Corresponds to MC Interpolator | 68 | Not applicable | 1 |
| MC-LookAhead | 15 to 16 (15) | 97 | Not applicable | 1 |
| MC-Transformation | 17 to 25 (25) | 98 | Not applicable | 1 |
| Time error | 22 | 80 | Ignore | 1 |
| Cycle monitoring time violated once <sup>1)</sup> | STOP |  |  |  |
| Diagnostic interrupt | 2 to 26 (5) | 82 | Ignore | 1 |
| Removal/insertion of modules | 2 to 26 (6) | 83 | Ignore | 1 |
| Rack error | 2 to 26 (6) | 86 | Ignore | 1 |
| Programming error (only for global error handling) | 2 to 26 (7) | 121 | STOP | 1 |
| I/O access error (only for global error handling) | 2 to 26 (7) | 122 | Ignore | 1 |
| <sup>1)</sup> How does the R/H system behave in the case of cycle timeouts? See "Redundant system S7-1500R/H System Manual". |  |  |  |  |

#### Assignment between event source and OBs

The type of OB determines where you make the assignment between OB and event source:

- With hardware interrupts and isochronous mode interrupts, the assignment is made during the configuration of the hardware or when the OB is created.
- STEP 7 automatically assigns OBs 91/92 to the MC Servo interrupt and MC-Interpolator interrupt, as soon as a technology object is added to "S7-1500 Motion Control".
- For all other types of OB, the assignment is made when the OB is created, possibly after you have configured the event source.

For hardware interrupts, you can change an assignment which has already been made during runtime with the instructions ATTACH and DETACH. In this case, only the actually effective assignment is changed, not the configured assignment. The configured assignment is effective after loading and for every startup.

Hardware interrupts to which no OB is assigned (because they were configured in this way or after the DETACH instruction is called) are ignored. The check as to whether an OB is assigned to an event does not take place when the associated event occurs, but only when the hardware interrupt actually has to be executed.

#### OB priority and runtime characteristics

S7-1500 CPUs support the priority classes 1 (lowest) to 26 (highest). An OB is assigned the priority of its start event.

The OBs are executed exclusively on a priority basis. This means that the OB with the highest priority is executed first when multiple OB requests occur at the same time. If an event with higher priority than the currently active OB occurs, this OB is interrupted. Events of the same priority are processed in order of occurrence.

---

**See also**

[Organization blocks (OB)](Programming%20basics.md#organization-blocks-ob)
  
[ATTACH: Attach an OB to an interrupt event (S7-1200, S7-1500)](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#attach-attach-an-ob-to-an-interrupt-event-s7-1200-s7-1500)
  
[DETACH: Detach an OB from an interrupt event (S7-1200, S7-1500)](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#detach-detach-an-ob-from-an-interrupt-event-s7-1200-s7-1500)
  
[Overview of mechanisms for error handling](Programming%20basics.md#overview-of-mechanisms-for-error-handling)

### CPU overload behavior (S7-1500)

#### Principle of CPU overload behavior

The sequence of the user program for S7-1500 CPUs is based on events of different priorities. An event triggers the execution of an OB. The OBs are executed exclusively on a priority basis. This means that the OB with the highest priority is executed first when multiple OB requests occur at the same time. If an event with higher priority than the currently active OB occurs, this OB is interrupted. Events of the same priority are processed in order of occurrence.

For the event scenarios considered in the following section, it is assumed that you have assigned an OB to each event source and that these OBs have the same priority. The second condition, in particular, is only for the sake of a simplified representation.

When an event occurs, the execution of the associated OB is triggered. This means that the event is positioned in a queue according to its priority. Depending on the OB priority and the current processor load, there is usually a time delay before the OB is executed. The same event can therefore occur once or several times before the OB belonging to the preceding event has been processed. Such a situation is handled by the CPU as follows: In the order of their occurrence, the operating system positions the events into the queue according to their priority.

To control temporary overload situations, you can limit the number of pending events that are linked from the same source. The next event is discarded as soon as the maximum number of pending start events of a specific cyclic interrupt OB, for example, is reached.

An overload occurs when events which originate from the same source occur faster than they can be processed.

More detailed information is provided in the following sections.

#### Discarding similar events or fetching them later

Below, the term "similar events" refers to events from a single source, such as start events for a specific cyclic interrupt OB.

The OB parameter "Events to be queued" is used to specify how many similar events the operating system places in the associated queue and therefore post-processes. If this parameter has the value 1, for example, exactly one event is stored temporarily.

> **Note**
>
> Post-processing of cyclic events is often not desirable, as this can lead to an overload with OBs of the same or lower priority. Therefore, it is generally advantageous to discard similar events and to react to the overload situation during the next scheduled OB processing. If the value of the "Events to be queued" parameter is low, this ensures that an overload situation is mitigated rather than aggravated.

If, for example, the maximum number of start events is reached in the queue for a cyclic interrupt OB, each additional start event is only counted and subsequently discarded. During the next scheduled execution of the OB, the number of discarded start events is made available (in optimized start information) in the "event_count" input parameter. You can then react appropriately to the overload situation. The CPU then sets the counter for lost events to zero.

If the CPU, for example, first discards a start event for a cyclic interrupt OB, its further behavior depends on the OB parameter "Report event overrun into diagnostic buffer": If the check box is selected, the CPU enters the event DW#16#0002:3507 once in the diagnostic buffer for the overload situation at this event source. Additional diagnostic buffer entries of the event DW# 16 #0002:3507 that refer to this event source are suppressed until all events from this source have been post-processed.

#### Threshold mechanism for time error OB request

The OB parameter "Enable time error" is used to specify whether the time error OB should be called when a specific overload level is reached for similar events.

If yes (check box selected), you use the OB parameter "Event threshold for time error" to specify the number of similar events in the queue at which the time error OB should be called. If this parameter has the value 1, for example, the event DW#16#0002:3502 is entered once in the diagnostic buffer and the time error OB is requested when the second event occurs. Additional diagnostic buffer entries of the event DW# 16 #0002:3502 that refer to this event source are suppressed until all events from this source have been post-processed.

In the event of an overload, you therefore have the option of programming a reaction well before the limit is reached for similar events and thus before the events are discarded.

The following value range applies to the "Event threshold for time error" parameter: 1 <= "Event threshold for time error" <= "Events to be queued"

### Example of a hardware interrupt event (S7-1500)

The functional principle of event-oriented program execution in the S7-1500 CPU is described based on the example of a module triggering a hardware interrupt.

Process events are events which are triggered by the I/O (e.g. a digital input) and initiate a call of the assigned OB in the S7-1500 CPU. OBs assigned to a process event are called hardware interrupt OBs.

#### Procedure

To configure a hardware interrupt, proceed as follows:

1. Configure an S7-1500 with CPU and a hardware interrupt-compatible module, e.g. DI 16x24VDC HF.
2. Select the hardware interrupt-compatible module and navigate in the area navigation to the area "Inputs > Channel 0".
3. Activate the option "Enable rising edge detection".
4. Assign a meaningful name to the event.
5. If necessary, change the priority of this event.

   In the PLC tags ("System constants" tab), a system constant of the data type Event_HwInt is created for the event.

   ![Procedure](images/46547763339_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/46547763339_DV_resource.Stream@PNG-en-US.png)
6. Click the "Hardware interrupt" drop down list to create a new hardware interrupt OB. If a hardware interrupt OB already exists, it can be selected.
7. Click the "Add object" button to create a new hardware interrupt OB.

   ![Procedure](images/46506373771_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/46506373771_DV_resource.Stream@PNG-en-US.png)
8. You can specify in the selection dialog whether the programming editor should start immediately with the opened hardware interrupt OB ("Add new and open" option).

   ![Procedure](images/46497822987_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/46497822987_DV_resource.Stream@PNG-en-US.png)

#### Hardware interrupt OB properties

The properties of the hardware interrupt OB contain the corresponding information about the start event for each interrupt-triggering event:

![Hardware interrupt OB properties](images/46551527691_DV_resource.Stream@PNG-en-US.png)

#### Hardware interrupt OB program

In the user program, you can use the start information of the hardware interrupt OB to identify and evaluate the hardware interrupt event.

![Hardware interrupt OB program](images/46495172235_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Assigning parameters to hardware interrupt OBs (S7-1500)](#assigning-parameters-to-hardware-interrupt-obs-s7-1500)
  
[Hardware interrupt OBs (S7-1500)](#hardware-interrupt-obs-s7-1500)
  
[What you need to know about HW identifiers (S7-1200, S7-1500, S7-1500T)](Configuring%20automation%20systems.md#what-you-need-to-know-about-hw-identifiers-s7-1200-s7-1500-s7-1500t)

## Setting the operating behavior (S7-1500)

This section contains information on the following topics:

- [CPU properties (S7-1500)](#cpu-properties-s7-1500)
- [Time-of-day functions (S7-1500)](#time-of-day-functions-s7-1500)
- [Enabling system memory (S7-1500)](#enabling-system-memory-s7-1500)
- [Using clock memory (S7-1500)](#using-clock-memory-s7-1500)
- [Protection & Security (S7-1500)](#protection-security-s7-1500)
- [Test, commissioning and routing (S7-1500)](#test-commissioning-and-routing-s7-1500)
- [Activating and deactivating SNMP (S7-1500)](#activating-and-deactivating-snmp-s7-1500)
- [Activating/deactivating SNMP through a program - standard CPU (S7-1500)](#activatingdeactivating-snmp-through-a-program---standard-cpu-s7-1500)
- [Activating/deactivating SNMP through a program - R/H-CPU (S7-1500)](#activatingdeactivating-snmp-through-a-program---rh-cpu-s7-1500)
- [Isochronous mode (central) (S7-1500)](#isochronous-mode-central-s7-1500)

### CPU properties (S7-1500)

This section contains information on the following topics:

- [Overview of the CPU properties (S7-1500)](#overview-of-the-cpu-properties-s7-1500)
- [CPU settings on the display (S7-1500)](#cpu-settings-on-the-display-s7-1500)
- [Cycle time and maximum cycle time (cycle monitoring time) (S7-1500)](#cycle-time-and-maximum-cycle-time-cycle-monitoring-time-s7-1500)
- [Cycle load due to communication (S7-1500)](#cycle-load-due-to-communication-s7-1500)
- [Multilingual (S7-1500)](#multilingual-s7-1500)
- [Central alarm management in the CPU (S7-1500)](#central-alarm-management-in-the-cpu-s7-1500)
- [CPUs with several PROFINET interfaces (S7-1500)](#cpus-with-several-profinet-interfaces-s7-1500)

#### Overview of the CPU properties (S7-1500)

##### Overview

The following table provides you with an overview of the CPU properties:

| Group | Properties | Description |
| --- | --- | --- |
| General | Project information | General information to describe the inserted CPU. Except for the slot number, you can change this information. |
| Catalog information | Read-only information from the hardware catalog for this CPU. |  |
| Identification & Maintenance | For saving application-specific information such as the name of the plant and the installation location. |  |
| Checksums | To check the identity or integrity of PLC programs.  Blocks in the block folder and text lists are automatically marked with unique checksums when they are compiled. You can easily establish whether the program currently running on the CPU is the same program that you loaded a long time ago or whether the program has been changed in the meantime. The "GetChecksum" instruction is available to read out the checksum while the program is running.  See: [Comparison of PLC programs based on checksums](Comparing%20PLC%20programs.md#comparison-of-plc-programs-based-on-checksums) |  |
| PROFINET interface | General | Name and comment for this PROFINET interface. The name is limited to 110 characters. |
| Ethernet addresses | Select whether the PROFINET interface is networked. If subnets have already been created in the project, they are available for selection in the drop-down list. If not, you can create a new subnet with the "Add new subnet" button.  Information on the IP address, subnet mask and IP router usage in the subnet is available in the IP protocol. If an IP router is used, the information about the IP address of the IP router is necessary.  See: [Assigning addresses and names to PROFINET devices](Configuring%20devices%20and%20networks.md#assigning-addresses-and-names-to-profinet-devices) |  |
| Time synchronization | Settings for time synchronization in the NTP time format.  The NTP (network time protocol) is a general mechanism for synchronizing system clocks in local and global area networks.   In NTP mode, the interface of the CPU sends time queries (in client mode) at regular intervals to NTP servers on the subnet (LAN) and the addresses must be set in the parameters here. Based on the replies from the server, the most reliable and most accurate time is calculated and synchronized. The advantage of this mode is that it allows the time to be synchronized across subnets. The accuracy depends on the quality of the NTP server being used. |  |
| Operating mode | Selection of operation of CPU as IO controller or IO device including the necessary settings.   As IO device (I-device), you must assign an IO controller and specify if the PROFINET interface is configured by the higher-level IO controller or if the local IO controller configures the PROFINET interface. The prioritized startup can also be enabled for the role IO device if the higher-level IO controller supports this function. If you have configured the CPU as IO device, the table for configuration of the transfer areas is displayed.   See: [Configuring the I-device](Special%20PROFINET%20configurations.md#configuring-the-i-device) |  |
| Advanced options | Name, comment and additional setting options of the Ethernet interface and the ports. This includes the following settings:  - Interface options such as the reaction of the user program in case of communication errors, if device replacement is possible without exchangeable medium or automatic commissioning, setting regarding IEEE-compliant LLDP mode (PROFINET V2.3), time lag between sending of Keep Alives for connections. - Media redundancy settings, such as the media redundancy role (client, manager (Auto) or devices not participating in the media redundancy ring), display of the ring ports and if diagnostic interrupts are generated in case of redundancy errors. A "Domain settings" interface is the link to the domain settings of the connected subnet (MRP domain and Sync domain). - Real-time settings such as send clock and synchronization properties with a "Domain settings" interface which is the link to the domain settings of the connected subnet (MRP domain and Sync domain). In the Sync domain you set the send clock for isochronous IO systems and specify the RT classes (RT and IRT) as well as the synchronization roles for IRT. - Ports: For ports you set the interconnection with neighboring devices (alternative: use the topology view), if necessary. Port interconnections are required for isochronous applications (IRT) as well as for automatic commissioning ("Device replacement without exchangeable medium" option is selected).  You also set the port options, for example, if the port is used (you can block unused ports). The port options include the connection settings (transmission rate/duplex) with the options for monitoring and autonegotiation. You also set the boundaries for the end of detecting accessible devices, for the end of topology detection and for the end of the sync domain.   See:    [Setting the send clock](Configuring%20devices%20and%20networks.md#setting-the-send-clock)    [Interconnecting ports](Configuring%20devices%20and%20networks.md#interconnecting-ports-1)    [Setting the port options](Configuring%20devices%20and%20networks.md#setting-the-port-options)    [What you should know about media redundancy](Special%20PROFINET%20configurations.md#what-you-should-know-about-media-redundancy)    [Introduction: Isochronous Realtime Ethernet](Special%20PROFINET%20configurations.md#introduction-isochronous-realtime-ethernet-s7-1500-s7-1500t)    [Enabling device replacement without exchangeable medium](Configuring%20devices%20and%20networks.md#enabling-device-replacement-without-exchangeable-medium) |  |
| Web server access | Allows access to the web server function. |  |
| PROFIBUS interface | General | Name and comment for this PROFIBUS interface. The name is limited to 110 characters. |
| PROFIBUS address | Selection of whether the PROFIBUS interface is networked. If subnets have already been created in the project, they are available for selection in the drop-down list. If not, you can create a new subnet with the "Add new subnet" button.  The PROFIBUS address is assigned and the highest address and the transmission speed are displayed. |  |
| Operating mode | Selection of CPU operating mode as DP master or DP slave. A DP master can be assigned to a DP slave and the I-slave communication parameters can be set here. |  |
| Time synchronization | The time can be synchronized. A default can be set for the time source and synchronization frequency. |  |
| SYNC/FREEZE | The DP master can send the SYNC and/or FREEZE control command to a group of DP slaves to synchronize these. For this purpose, the DP slaves are assigned to SYNC/FREEZE groups. |  |
| Startup | Startup after POWER ON | Setting the startup characteristics after a POWER OFF/POWER ON transition.  See: [Basics of "STARTUP" operating mode](#basics-of-startup-operating-mode-s7-1500) |
| Comparison preset to actual configuration | Specifies the startup characteristics for situations in which the actual configuration of the S7-1500 station does not correspond to the preset configuration:  - Startup of the CPU only if compatible - Startup of the CPU even if there are differences   With the "Startup CPU only if compatible" setting, a module in a configured slot must be compatible with the configured module.   Compatible means that the module that is present matches the number of inputs and outputs and must match with respect to its electrical and functional properties. A compatible module must be able to completely replace a configured module; it may be more capable, but not less capable.  Example for the "Startup CPU only if compatible" setting:  A CPU can be a compatible replacement for a CPU of the same type with a lower firmware version.  An input module with 32 digital inputs can be a compatible replacement for a signal module with 16 digital inputs. The CPU starts up when the configured module or a compatible module is plugged in. The CPU does not start up if an incompatible module is inserted.  Example of the "Startup CPU even if mismatch" setting:  Instead of a configured digital input module, an analog output module is plugged in or no module is present in this slot. Although the configured inputs cannot be accessed, the CPU starts up.   Note in this case that the user program cannot function correctly and take the appropriate measures.   **Note**: For S7-1500 modules and ET 200SP modules, you can configure the comparison between preset module and actual module individually for each slot. The default is "From CPU" (in other words, the CPU's setting applies to the slot). For I/O modules from other I/O series, generally the CPU's setting applies (cannot be changed). |  |
| Configuration time | Specifies a maximum time period (default: 60000 ms) in which the central and distributed I/O must be ready for operation. The CMs and CPs are supplied with voltage and communication parameters during the CPU startup. The configuration time limits the period during which I/O modules connected to the CM or CP must be ready for operation.  If the central and distributed I/O is not ready for operation within the configuration time, the startup characteristics of the CPU depends on the setting of the "Supported hardware compatibility" parameter. |  |
| Clock | - | Definition for synchronizing the clock via the backplane bus. The setting options depend on the CPU.  - As slave: The clock is synchronized by another clock. - As master: The clock synchronizes other clocks. - None: No synchronization takes place.   The time intervals for the synchronization can be selected.  See: [Time-of-day functions](#time-of-day-functions-s7-1500) |
| Cycle | Maximum cycle time (cycle monitoring time) and minimum cycle time | Specification of a maximum cycle time (cycle monitoring time) or a fixed minimum cycle time.  If the cycle time exceeds the maximum cycle time, the CPU calls organization block OB 80 "time error". If OB 80 is not available, the CPU changes to STOP mode.   If the maximum cycle time is exceeded twice in one cycle, the CPU changes to STOP mode even if OB 80 exists.  Causes of a violation:  - Communication processes - Accumulation of interrupt events - CPU program error.   If the cycle time is shorter than the minimum cycle time you have entered, the CPU waits until the minimum cycle time has been reached. The CPU processes the OB 90 (background OB) in this additional program processing time, if it is loaded.  See: [Cycle time and maximum cycle time (cycle monitoring time)](#cycle-time-and-maximum-cycle-time-cycle-monitoring-time-s7-1500) |
| Communication load | Cycle load due to communication | Controls the duration of communication processes that always also extend the cycle time, within certain limits. Examples of communication processes include: Transferring data to another CPU or loading blocks (initiated via the PC).  See: [Cycle load due to communication](#cycle-load-due-to-communication-s7-1500) |
| System and clock memory | System memory bits and clock memory bits | Setting of a byte for the system memory functions and setting of a byte for the clock memory functions (switches each bit on and off at a specified frequency).  You use system memory bits for the following queries:   - Is the current cycle the first since POWER OFF/POWER ON? - Have there been any diagnostics state changes since the previous cycle? For example, after an incoming or outgoing diagnostic message, the corresponding bit has the value 1 for the duration of a cycle. - Query for "1" (high) - Query for "0" (low)   Clock memory bits change their values periodically at specified intervals.  See: [Enabling system memory](#enabling-system-memory-s7-1500)  See: [Using clock memory](#using-clock-memory-s7-1500) |
| SIMATIC memory card | - | Enabling of diagnostics for SIMATIC memory card service life. |
| System diagnostics | General | System diagnostics is the recording, evaluation and reporting of errors within the automation system.  Examples of errors:  - CPU program error - Failure of modules - Wire break to sensors and actuators   Default alarm texts are available for determining the system diagnostics. If necessary, existing alarm texts can be changed and new ones added. The settings are saved with the project and are effective only after the compilation and loading of the hardware configuration to the relevant components. For S7-1500, the system diagnostics is automatically activated (cannot be deactivated). |
| PLC alarms | General  Central alarm management in the PLC | Activates the central alarm management in the CPU. An alarm is completely assembled in the CPU and then sent to the HMI device. Advantage: There is no need to download the alarm texts to the HMI devices.  See: [Central alarm management in the CPU](#central-alarm-management-in-the-cpu-s7-1500) |
| Web server | General | Activates and configures the web server function.  See: [Enable the web server](Configuring%20the%20Web%20server%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#enable-the-web-server-s7-300-s7-400-s7-1500) |
| Automatic update | Sends the requested web page with current CPU data periodically to the web browser. Enter the period duration under "Update interval". Automatic update can only be activated if the web server is enabled.  See: [Activate automatic update](Configuring%20the%20Web%20server%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#activate-automatic-update-s7-300-s7-400-s7-1500) |  |
| User management (only for CPUs with FW < V3.1) | Here you enter the user names with their access rights.  - Everyone: Pre-defined user whose access rights you assign using a drop-down list. The "Everyone" user is a user who does not log on with a password for web access. - User#: Editable name for a user for whom you assign access rights and a password. As soon as you click in a line below "Everyone", a preset name is displayed that you can change.   Each user can be assigned different access rights via a drop-down list.  There are access rights that are connected to each other. Example: When you activate the access right "Perform firmware update", the access rights "Change operating mode" and "... query diagnostics" are activated automatically. These two rights are required to perform a firmware update from the web server.  See: [User administration](Configuring%20the%20Web%20server%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#user-administration-s7-300-s7-400-s7-1500) |  |
| Security | Allows the use of a certificate for the identification of the server. |  |
| Watch tables | Allows you to create watch tables and defines access to those tables. |  |
| User-defined web pages | Allows access to freely-designed web pages of the CPU via a web browser.  See: [Creating and loading user pages](Configuring%20the%20Web%20server%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#creating-and-loading-user-pages-s7-300-s7-400-s7-1500) |  |
| Entry page | Allows you to select the entry page. |  |
| Overview of interfaces | Tabular representation of all modules with their Ethernet interfaces providing web server functionality for this device.  Here you can permit or deny access to the web server by means of the respective interface for each Ethernet interface of the device (CPU, CP, CM). |  |
| Display | General | The display remains dark in standby mode and is re-activated as soon as one of the display keys is pressed. You can also change standby mode in the display menu of the display.  In energy-saving mode, the display shows the information with reduced brightness. Energy-saving mode is switched off as soon as any display key is pressed. You can also change energy-saving mode in the display menu of the display.  Display language: the language is changed immediately after the hardware configuration is loaded with the set standard language. You can also change the language in the display menu of the display. |
| Automatic update | Input of the time interval at which the display is updated. |  |
| Password | Setting to enable or disable write-access via the CPU display. If you have enabled write-access, you can also enable display protection. The display is then protected by a configurable password. You can set the time until automatic logoff after input of the password on the display. |  |
| Watch tables | Configured watch tables are provided for selection. You can use the selected watch tables on the display during operation. |  |
| User-defined logo | You can select a user-defined logo and load it to the CPU with the hardware configuration. |  |
| Multilingual | - | If you want to use translations of project texts for the Web server/for the CPU display, you need to assign the project language to the languages for the Web server/for the CPU display (number depends on the CPU). With this, you specify the project languages that are displayed when the Web server is accessed or in the CPU display.   Example: You assign the project language "German (Luxembourg)", for example, to a German language of the Web server/the CPU display by selecting it from the drop-down list. Enable the project language under "Languages & resources > Project languages" in the project tree to make it available for selection in the drop-down list.  See: [Multilingual](#multilingual-s7-1500) |
| Time | Local time and daylight saving time | Selection of the time zone in which the CPU operates and setting for standard/daylight saving time.  See:    [Determining and setting the time of day on a CPU](Device%20and%20network%20diagnostics.md#determining-and-setting-the-time-of-day-on-a-cpu)    [Setting and reading the time of day](#setting-and-reading-the-time-of-day-s7-1500) |
| Protection & Security | Protection of the PLC configuration data | Configure here the protection of the confidential PLC configuration data.  See: [Protection of confidential configuration data](Configuring%20devices%20and%20networks.md#protection-of-confidential-configuration-data-s7-1200-s7-1500-s7-1500t) |
| Access control | Setting of the read/write protection and the password for access to the CPU. Starting from FW V3.1 (S7-1500) introduction of local user management.   See: [Useful information on the local user administration and access control](#useful-information-on-the-local-user-administration-and-access-control-s7-1500)  See: [What you should know about the access levels](#what-you-should-know-about-the-access-levels-s7-1500)  See: [Configuring access levels](#configuring-access-levels-s7-1500) |  |
| Connection mechanisms | Enable access via a PUT/GET communication or via secure PG/PC communication and HMI communication. For secure PG/PC communication and HMI communication you can select the communication certificates here.  See: [Restriction of communication services](#restriction-of-communication-services-s7-1500)  See: [Useful information for the protection of confidential PLC configuration data](Configuring%20devices%20and%20networks.md#useful-information-for-the-protection-of-confidential-plc-configuration-data-s7-1200-s7-1500-s7-1500t) |  |
| Certificate manager | Enabling of global security settings for the certificate manager and management of the certificates for the device. |  |
| Syslog | Enabling the transmission of Syslog messages to a Syslog server and managing the certificates for the device.  See: [Syslog](#syslog-s7-1500) |  |
| Security event | Enabling of group alarms for security events and specification of a monitoring time (interval).  See: [Summarizing security events](#what-you-should-know-about-group-alarms-for-security-events-s7-1500) |  |
| OPC UA | General | Shows the name of the OPC UA application. This is used for the OPC UA server on this CPU. |
| Server | Enabling and configuring of the OPC UA server. Besides the general settings for assignment of port numbers, send interval and sampling interval, you can configure the security settings here and perform the export of the PLC/DB tags available in the OPC UA address space to an XML file.  You have the following options for the security settings:  - Secure channel: Select between use of global security settings or use of the local CPU-specific certificate manager with limited functionality. Create or select the server certificate here, select the suitable security policy and manage the list of trusted clients. - User authentication (only for CPUs with FW < V3.1): Create or select new users and specify the authentication options. |  |
| Client | Enable the OPC UA client for this CPU. |  |
| System power supply | General | Specifies that the CPU is connected to the power grid. This CPU power therefore goes in to the power supply/consumption ratio as positive. |
| Power segment overview | In the power segment overview, the power provided by the CPU and the power supply modules is compared with the power required by the signal modules. If the supply/consumption ratio is negative, in other words the power requirements are greater than the power provided by the CPU and the power supply modules, this is indicated in the table. |  |
| Advanced configuration | DNS configuration | Configuration of the DNS server address.  A DNS server may be required if the CPU or a communication partner should be accessible via the host name (FQDN).  See: [DNS configuration](Communications%20modules%20and%20network%20components.md#dns-configuration) |
| IP forwarding | Enable IPv4 forwarding for all PROFINET interfaces of this CPU.  If IP forwarding is activated, the CPU can forward received IP data packets whose destination address does not correspond to its own IP address to another connected IP subnet via another PROFINET interface.  See: [IP forwarding](Configuring%20devices%20and%20networks.md#ip-forwarding) |  |
| Access to PLC via communications module | Assignment of a suitable communications module for activation of the virtual interface W1 (z. B. CP 1543-1 firmware V2.2 or higher). The virtual interface W1 provides access to IP-based applications of the CPU via the CP.  The firewall settings in the communications module do not change automatically when the access is activated. This means if the firewall is switched on, you need to enable the use of the virtual interface W1 in the firewall settings of the communications module.  See: [Virtual interface for IP-based applications](Configuring%20devices%20and%20networks.md#virtual-interface-for-ip-based-applications) |  |
| Configuration control | Enabling of the configuration control. Enables a configuration change in the user program within certain limits.  See: [Configuration control](Configuring%20automation%20systems.md#important-information-regarding-configuration-control-option-handling-s7-1500) |  |
| Isochronous mode | Here, you configure isochronous mode centrally for all plugged modules. You can switch the isochronous mode of individual modules on or off in the detailed overview.  Modules that do not support configurable isochronous mode are displayed in gray in the overview.  See: [Configuring isochronous mode for central I/O in S7-1500](#configuring-isochronous-mode-for-central-io-in-s7-1500-s7-1500) |  |
| Connection resources | - | Provides an overview of the assigned reserved and dynamic resources for the CPU connections. The resources currently used are also displayed in the online view.  See: [Connection resources and communication type](Configuring%20devices%20and%20networks.md#connection-resources-and-communication-type) |
| Address overview | - | Table of all addresses used by the CPU for integrated inputs/outputs and for the inserted modules. Addresses that are not used by any module are shown as gaps.   The view can be filtered by   - Input addresses - Output addresses - Address gaps |
| Runtime licenses | CPU applications that require an RT license, e.g. OPC UA, ProDiag, Energy Suite | Depending on the CPU application, select the number of licenses to be used here.  Purchasing these licenses is a requirement for their use.   Exception: If you use these CPU applications in the context of simulations with PLCSim Advanced, it is not necessary to purchase licenses. In this case, simply select the number of licenses you require.  Example of license selection: [Setting ProDiag licenses](Supervision%20of%20machinery%20and%20plants%20with%20ProDiag%20%28S7-1500%29.md#setting-prodiag-licenses-s7-1500) |

---

**See also**

[Set the regional web language (S7-300, S7-400, S7-1500)](Configuring%20the%20Web%20server%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#set-the-regional-web-language-s7-300-s7-400-s7-1500)
  
[What you need to know about HW identifiers (S7-1200, S7-1500, S7-1500T)](Configuring%20automation%20systems.md#what-you-need-to-know-about-hw-identifiers-s7-1200-s7-1500-s7-1500t)
  
[Setting prioritized startup](Special%20PROFINET%20configurations.md#setting-prioritized-startup)
  
[Assigning the device name and IP address](Configuring%20devices%20and%20networks.md#assigning-the-device-name-and-ip-address)
  
[CPU settings on the display (S7-1500)](#cpu-settings-on-the-display-s7-1500)
  
[Rules for CPUs with several PROFINET interfaces (S7-1500)](#rules-for-cpus-with-several-profinet-interfaces-s7-1500)
  
[IEEE-compliant LLDP (S7-1500)](#ieee-compliant-lldp-s7-1500)

#### CPU settings on the display (S7-1500)

The S7-1500 CPUs have a display with operator control buttons. The display can be used to read out status information about the configured modules, for diagnostic purposes, and also to adapt some CPU settings.

##### Example: Setting the IP address and the PROFINET device name on the display

If you want to assign the IP address parameters (IP address, subnet mask and router settings) on the display, you must select the following option in the relevant project for the PROFINET interface of the CPU:

- Set IP address on the device

The same applies accordingly to the PROFINET device name: If you want to assign the PROFINET device name on the display, then you must select the following option in the relevant project for the PROFINET interface of the CPU:

- Set PROFINET device name on the device

#### Cycle time and maximum cycle time (cycle monitoring time) (S7-1500)

##### Function

The cycle time is the time that the operating system requires to execute the cyclic program and all the program sections that interrupt this cycle. The program execution can be interrupted by:

- Time errors and 2xMaxCycleTime errors
- System activities, e.g., process image updating

The cycle time (Tcyc) is therefore not the same for every cycle.

The following schematic shows an example of different cycle times (TZ1 ≠ TZ2) for S7-1500 CPUs:

![Function](images/40846549771_DV_resource.Stream@PNG-en-US.png)

In the current cycle, the cyclic OB used here (e.g. OB 1) will be interrupted by a time error (e.g. OB 80). Following the cyclic OB, the next cycle OB 201 is processed.

##### Maximum cycle time (cycle monitoring time)

The operating system monitors the execution time of the cyclic program for a configurable upper limit known as the maximum cycle time. You can restart this time monitoring at any point in your program by calling the RE_TRIGR instruction.

If the cyclic program exceeds the maximum cycle time, the operating system attempts to start the time error OB (OB 80). If the OB is not present, the CPU switches to STOP mode.

In addition to monitoring the runtime for overshooting of the maximum cycle time, adherence to a minimum cycle time is guaranteed. To do this, the operating system delays the start of the new cycle until the minimum cycle time has been reached. During this waiting time, new events and operating system services are processed.

If the maximum cycle time is exceeded a second time, for example while the time error OB is being processed (2xMaxCycleTime error), the CPU changes to STOP mode.

#### Cycle load due to communication (S7-1500)

##### Function

The cycle time of the CPU can be extended due to communication processes. These communication processes include for example:

- Transferring data to another CPU
- Loading of blocks initiated by a programming device
- Certain motion control functions (commissioning of technology objects, restart of technology objects and interpolation of cam discs)

In addition to communication processes, test functions also extend the cycle time.

You can control the duration of the communication processes using the CPU parameter "Cycle load due to communication".

##### How the parameter works

You use the "Cycle load due to communication" parameter to enter the percentage of the overall CPU processing capacity that can be available for communication processes.

This processing capacity can be used for program execution when not required for communication.

> **Note**
>
> **Which effects can the specification of a minimum cycle time have?**
>
> When you have specified a minimum cycle time and the user program does not need it completely, the remaining time can be used once again for communication processes. The result may be that communication processes take up a larger percentage of the CPU processing capacity than you have specified in the CPU parameter "Cycle load due to communication".

The following applies to starting and processing OBs depending on their priority classes:

- The start of OBs of priority classes **lower than 15** can be delayed by the communication and interrupted in their processing.
- The start of OBs of priority class **15** can be delayed by the communication but not interrupted in their execution.
- The start of OBs of priority classes **higher than 15** cannot be delayed by the communication and cannot be interrupted in their execution.

By assigning the priority of an event or an OB, you can thereby influence the possible delay and interruptibility of the OB through communication. This also affects the blocks that are called by the OB. If program sections are made uninterruptible in this manner in order to minimize cycle times, the online functions of STEP 7 are delayed!

##### Effect on the actual cycle time

The "Cycle load due to communication" parameter can be used to extend the cycle time of the cyclic organization block (e.g., OB 1) by a factor calculated according to the following formula:

![Effect on the actual cycle time](images/40887772811_DV_resource.Stream@PNG-en-US.png)

The formula does not take into account the effect of asynchronous events such as hardware interrupts or cyclic interrupts on the cycle time.

If the cycle time is extended due to communication processes, more asynchronous events may occur within the cycle time of the cyclic organization block. This extends the cycle still further. The extension depends on how many events occur and how long it takes to process them.

##### Example 1 – no additional asynchronous events:

If the "Cycle load due to communication" parameter is set to 50%, this can cause the cycle time of the cyclic organization block to increase by up to a factor of 2.

##### Example 2 – additional asynchronous events:

For a pure cycle time of 500 ms, a communication load of 50% can result in an actual cycle time of up to 1000 ms, provided that the CPU always has enough communication jobs to process.

![Example 2 – additional asynchronous events:](images/127966734219_DV_resource.Stream@PNG-en-US.png)

If a cyclic interrupt (priority class less than 15) with a processing time of 20 ms runs every 100 ms with a pure cycle time of 500 ms, the cycle time without communication load has an extending effect on the cycle with a total of 5*20 ms = 100 ms, i.e. the actual cycle time is then initially 600 ms. By extending the cycle time over the processed cyclic interrupts, however, additional cyclic interrupts may be performed, the processing of which further extends the cycle time. The resulting cycle time is 640 ms for two additionally performed cyclic interrupts within the cycle.

![Example 2 – additional asynchronous events:](images/127969759627_DV_resource.Stream@PNG-en-US.png)

Because communication at 50 % communication load has an extending effect both on the cyclic program and on the cyclic interrupt and further cyclic interrupts are executed by this extension, the resulting cycle time is 1680 ms at 500 ms pure cycle time and by the cyclic interrupts added every 100 ms with 20 ms pure processing time each. This value is calculated as follows:

- OB1 processing time (500 ms) with 50 % communication load = 1000 ms
- Single OB30 cyclic interrupt (20 ms) with 50 % communication load = 40 ms

Since an OB30 cyclic interrupt (with 50 % communication load) of 40 ms is processed every 100 ms, a processing time of 60 ms remains for OB1 every 100 ms, 30 ms of which are used for communication, however, and therefore only 30 ms remain for pure OB1 processing in time slices of 100 ms:

- Available time for OB1 processing with communication portion in a 100 ms time slice = 60 ms
- Required number of time slices for OB1 processing = 1000 ms / 60 ms = 16.666

Processing OB1 with 50 % communication load, requires 16 complete time slices of 100 ms each (total time 1600 ms, of which 16 * 60 ms = 960 ms is for OB1 with communication). A remaining time of 40 ms is still required for OB1 processing with communication, but the newly started new time slice begins with another OB30 call (with communication share = 40 ms). In total, OB30 is called 17 times (17 * 40 ms = 680 ms), which results in a total cycle time of 1680 ms with the total OB1 processing time.

![Example 2 – additional asynchronous events:](images/127966729099_DV_resource.Stream@PNG-en-US.png)

The example illustrates that with a significant load of asynchronous events in the user program, the cycle time extension due to the communication load can also be much higher than specified in the formula above.

> **Note**
>
> Observe the following:
>
> - Check the effects of changing the value of the "Cycle load due to communication" parameter while the system is running.
> - You must always consider the communication load when setting the minimum cycle time; otherwise, time errors occur.

##### Recommendations

- Increase this value only if the CPU is used primarily for communication purposes and the user program is not time critical.
- In all other situations you should only reduce this value.
- If you do not want interrupt OBs to be interrupted by communication, you must set their priority to a value greater than 15.

#### Multilingual (S7-1500)

When you configure a CPU, texts of different categories result, e.g.

- Object names (names of blocks, modules, tags, ...)
- Comments (for blocks, networks, watch tables, ...)
- Alarm texts and diagnostics texts

Texts are made available by the system (e.g. diagnostics buffer texts) or are created during the configuration (e.g. alarms).

Depending on the specific element, texts are available in one language or they can be translated into other languages and can then be present in the project in multiple languages. You can maintain project texts in all languages available to you in the project tree (Languages & resources > Project texts).

The texts produced during the configuration can be loaded onto the CPU. Due to the limited resources (e.g. load memory) only a limited number of languages can be loaded.

The following description shows the uses of multilingual texts on the CPU, which texts are loaded and how you decide in which languages the texts are loaded onto the CPU.

You will also learn the influence the language assignment that you assign in the CPU properties (multilanguage) has and how this setting affects operation.

##### Uses of multilingual project texts

As the creator of the project, you create texts such as comments and alarms in your native language. For an original equipment manufacturer (OEM customer), you translate the texts into the language of the OEM customer, for example English, and into the language of the end customer. You can load a maximum of three languages onto the CPU.

The customers have the advantage that the relevant texts e.g. comments and alarms, exist in their native language even when the STEP 7 project is not available on the PG/PC. Loading the device as a new station also loads the languages, and the project can be analyzed and adapted on site.

A further advantage is that certain multilingual texts are available to an operator even without STEP 7.

Using the language selection of the Web server or the language selection of the CPU display, for example alarms, diagnostics buffer entries and status messages about the module status are visible in the set language.

Multilingual texts can also be displayed on HMI devices. You can display tag comments and step comments, for example, in the loaded languages in the Graph or Code viewer.

##### Requirements

- The project languages that are to be assigned must be activated.
- The corresponding texts (translations) must be available in the project.

  The project language selection can be found in the project tree under "Languages & Resources".

##### Setting the available languages for CPU display and Web server

The settings for multiple languages can be found in the CPU parameters: You set the following here:

- Which project languages are assigned to the languages of the CPU display/the Web server
- Which project languages are loaded onto the CPU

Follow these steps:

1. Navigate to the "Multiple languages" area ("Properties > General > Multiple languages") with selected CPU in the Inspector window.

   This area contains a table in which you assign languages: The project languages can be selected in the left-hand column. In the right-hand column, all the languages are listed that can be selected on the CPU display or for the Web server.
2. Assign a project language to the languages for the CPU display/Web server.

   With these assignments, existing project languages (as replacement languages) are displayed for languages that do not exist on the CPU.

   Note that these language settings only relate to the texts loaded from the configuration. Both the Web server and the CPU display have many more user interface languages so that you can have static texts displayed in the Web browser or on the CPU display in many more languages.

   ![Setting the available languages for CPU display and Web server](images/88468130827_DV_resource.Stream@PNG-en-US.png)

   > **Note**
   >
   > The number of loadable languages is limited for specific CPUs. If, for example, two languages are possible, assign the corresponding project language to your native language in the "Languages of the CPU display/Web server" column. In the remaining rows, you assign the same substitute language in the languages of the CPU display/Web server.

##### Example

Existing project languages in STEP 7 (PG): English, French, German, Italian.

Due to the assignment in the "Multilingual support" area of the CPU parameters, the following project languages are loaded during the next load procedure.

German, English.

The project language German is set automatically in display language German. The project language English is displayed with all other European display languages.

No language is assigned to the other display languages.

On the display, you can only select the language for the display; due to the language assignment from the configuration, the assigned project language is set automatically with the language for the display:

- If you select English as the language for the display, the project language English is set.
- If you select French as the language for the display, the project language English is also set.
- If you select Chinese as the language for the display, no project texts are displayed.

![Example](images/82762665099_DV_resource.Stream@PNG-de-DE.png)

##### Which project texts are loaded with the selected languages?

The following texts are loaded in the selected languages with the project data onto the CPU and used by the Web server/CPU display:

- Diagnostics buffer texts (cannot be changed)
- Status texts for the module status (cannot be changed)
- Alarm texts with corresponding text lists
- Tag comments and step comments for Graph and PLC Code Viewer
- Comments in watch tables

The following texts are also loaded in the selected languages with the project languages on the CPU but are not used by the Web server/CPU display:

- Comments in tag tables (for tags and constants)
- Comments in global data blocks
- Comments of elements in block interfaces of FBs, FCs, DBs and UDTs
- Network titles in blocks written in LAD, FBD or STL
- Block comments
- Network comments
- Comments of LAD and FBD elements

The following figure once again shows the relationship between multilingual project texts and the required memory space on a SIMATIC memory card.

![Which project texts are loaded with the selected languages?](images/82772121227_DV_resource.Stream@PNG-en-US.png)

##### Special considerations: Module comments

Module comments are only loaded in one language.

The following applies to loading module comments:

- Requirement: In the project settings (Options > Settings "Hardware configuration" area), the option "Download module comment" must be enabled (default).
- Module comments are loaded in the language set as the editing language. You change the editing languages in "Languages & Resources > Project languages".

##### Special considerations: Diagnostics buffer texts and status texts for the module status

The predefined texts for diagnostics buffer entries are not available in all languages that you can select as project languages in the languages & resources in STEP 7. With the assignment between the project language and language for the Web server/CPU display, the "closest" language is therefore loaded to the CPU.

Example: The texts mentioned above are in the German language, there is only one German language variant. If German (Luxemburg) or German (Austria) is selected as project language, the language German is always loaded.

##### Adding or removing languages - consequences for loading onto the CPU

If the number of project languages for the CPU display/Web server has changed, loading must be performed in STOP mode.

In this case, STEP 7 runs a complete load operation (hardware and software).

This applies regardless of the objects you have selected for loading: Loading a block, normally possible in RUN, also requires a CPU STOP whenever the number of languages for the CPU display/Web server has changed since the last load operation.

Even if you deselect an added project language again, a CPU STOP is required for the loading. You can only load the CPU in RUN when you undo the selection of an additional project language with the "Undo" command in the "Edit" menu and have not changed anything else that makes a STOP necessary.

In principle, the following applies:

Before each load operation, STEP 7 checks whether the number of languages for the CPU display/Web server has changed. If the number has changed (fewer or more languages selected since the last load operation), a CPU STOP is necessary.

##### Special features when loading the device as a new station (hardware and software)

If you have established an online connection to a device and you load this device (CPU with all assigned modules) into your project, the following rules apply:

- The project languages in the project are updated; in other words, when additional project languages exist on the device, they also exist in the project after loading (enabled in "Languages & Resources" in the project tree). The "Offline and online texts" are also compared after the loading; in other words, the version of the texts in the project corresponds to the version on the device.
- The project languages already existing in the project remain unaffected by the loading operation, no project language is deleted.
- After loading, the assignments "Project languages of the CPU/Web server" (multilingual) in the project correspond to the assignments loaded on the CPU. Loading to the device again loads the same languages that exist on the CPU.

##### Special features when loading from the device (software)

If you load the software from a CPU in your project, for example individual blocks or the entire program, the following rules apply:

- The project languages in the project are updated; in other words, when additional project languages exist on the device, they also exist in the project after loading (enabled in "Languages & Resources" in the project tree). The "Offline and online texts" of the loaded components are compared after the loading; in other words, the version of the texts in the project corresponds to the version on the device.
- The assignments "Project language - languages of the CPU display/Web server" (multilingual) in the project **are retained**; in other words, they do not change even if, for example, a new project language was used in the loaded block.   
  Note that in this case (new language only available in the CPU accessible online), you need to adapt the settings under "Multilingual support" in the properties of the CPU if the new language is to be loaded again to the CPU.
- There is a risk that existing translations in the project may be **deleted** when loading from the device in the following situation:

  - A language exists offline (e.g. in a block in the project)
  - This language does **not** exist online

    In this case, when you load from the device, you lose the language that exists online.
- Team engineering: You should only change the settings for multiple languages in the master project.

##### Special features with team engineering (joint commissioning)

In the case of joint commissioning, you have the option of recognizing missing translations with the synchronization dialog.

##### Recognizing missing languages during the online/offline comparison

In the online/offline comparison (comparison editor), you can recognize differences in the existing project languages for the following objects:

- Blocks
- Tag tables

Differences in the existing project languages for alarms and text lists are not taken into account by the comparison editor.

If know-how protected blocks are also included in the comparison: It is not necessary to enter passwords for these blocks for the comparison.

The following are used for the comparison:

- Online: The languages that actually exist on the CPU
- Offline: The languages selected in the "Assigned project languages" table in the "Multilingual support" area and therefore also taken into account when loading onto the CPU. These are not the languages in which, for example, the comments of the blocks actually exist.

The offline/offline comparison compares the activated project languages.

##### Preselection of the language for the OPC UA server

From TIA Portal V19 onwards, you can change the order of the rows in the table for the language assignments by simple drag-and-drop.

Uses of the sorting facility:

The OPC UA server uses the setting in the uppermost row of the table (default language or reference language) for transmitting text to the OPC UA client. If you need another language for your OPC UA configuration, then you must move the desired language into the uppermost row of the table.

To make alarm messages available in another language, for example, follow these steps:

1. Position the cursor in the first column (the column with the row numbering) right next to the number of the row that you wish to move to the uppermost position. Keep the mouse button pressed (for the drag movement).  
   An insertion marker appears above the mouse pointer.
2. Drag the mouse pointer to the desired position; here, the first row (drop).

![Preselection of the language for the OPC UA server](images/171175403787_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Overview of the CPU properties (S7-1500)](#overview-of-the-cpu-properties-s7-1500)
  
[Set the regional web language (S7-300, S7-400, S7-1500)](Configuring%20the%20Web%20server%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#set-the-regional-web-language-s7-300-s7-400-s7-1500)

#### Central alarm management in the CPU (S7-1500)

S7-1500 CPUs with firmware version V2.0 or higher support central alarm management.

The CPU parameter "Central alarm management in the PLC" is available under "PLC alarms > General".

Default: Central alarm management is enabled.

##### Effect of the CPU parameter "Central alarm management"

When central alarm management is enabled, the CPU transfers the entire alarm text, which can consist of multiple text list entries, to the HMI device. The CPU is responsible for compiling the entire alarm text. As soon as the triggering event for an alarm is pending, the CPU sends the entire alarm text with associated values, if any, to the HMI device through the existing HMI connection.

The enabled central alarm management makes it unnecessary to download the texts of the connected HMI devices.

If the central alarm management is **not** enabled, you must download the texts to the HMI device via the engineering system (WinCC) so that the alarm texts are displayed during operation. When the triggering event for an alarm is pending, the CPU sends only rudimentary information to the HMI device (e.g. alarm ID, alarm version and associated values). The HMI device is responsible for alarm management: The complete alarm text is compiled and prepared from the downloaded and transmitted data. This task does not require computing power of the CPU.

Any change to the message texts requires renewed downloading to the connected HM devices.

##### Notes and rules for central alarm management

- Required version of HMI Runtime: V14 or higher
- Required CPU: S7-1500 as of firmware version 2.0 (also S7-1500SP CPU, S7-1500Pro CPU and S7-1500 software controller).
- Alarms for which central alarm management is possible: Controller alarms (system diagnostics, process diagnostics, program alarms).
- "Automatic update" must be activated in the runtime settings of the HMI device ("Control alarms" section in the "Alarms" area).
- Modified texts that you load to the CPU have no effect on alarm texts that were already transferred to the HMI device. The updated alarm text will only be displayed with a new triggering event.
- The following applies to alarms that are displayed in the alarm view or alarm buffer of the HMI device:

  - You must download the languages in which the alarms are to be displayed on the HMI device to the CPU (max. 3 languages, see [Multilingual](#multilingual-s7-1500)).
  - The languages on the HMI device must be the languages that were loaded to the CPU. Otherwise the HMI device only indicates that alarm texts are missing during operation. For more than three languages, you must load the HMI device with the texts (central alarm management is not possible).
  - Message texts are only compiled at the time at which the message arrives. When the message departs, this compilation is not updated, even if individual parts of the message text (accompanying values) have changed in the meantime. If updated texts are required even for departing texts, then you have the following option if the HMI device is a Comfort Panel / device with WinCC RT Advanced/RT Professional:   
    Disable automatic updates in the runtime settings of the HMI device. In this case, the HMI device updates the texts for arriving and departing messages.   
    This option is not available for HMI devices with WinCC RT Unified.
- The following applies to alarms that are displayed in the alarm archive:

  - The alarm archive includes alarms in one language only. This language is set during configuration of the HMI device under "Archives > General > Archive language". The archive language also has to be one of the languages that was downloaded to the CPU.

> **Note**
>
> **Display of faults**
>
> If faults occur, a text is displayed as follows: #TextlistID, TextID (e.g. #123, 456)
>
> Example: You have forgotten an entry (Range) in the used text list. Then the first number is the text list ID (column is grayed out by default, but can be made visible). The second number shows the value for which the entry is missing. Text list ID = 123, value = 456.
>
> If Range is defined without text, this does not generate a fault.

---

**See also**

[Overview of the CPU properties (S7-1500)](#overview-of-the-cpu-properties-s7-1500)

#### CPUs with several PROFINET interfaces (S7-1500)

This section contains information on the following topics:

- [Rules for CPUs with several PROFINET interfaces (S7-1500)](#rules-for-cpus-with-several-profinet-interfaces-s7-1500)
- [Limitation of the data infeed into the network (S7-1500)](#limitation-of-the-data-infeed-into-the-network-s7-1500)
- [IEEE-compliant LLDP (S7-1500)](#ieee-compliant-lldp-s7-1500)

##### Rules for CPUs with several PROFINET interfaces (S7-1500)

The S7-1500 family of CPUs includes CPUs with two or three PROFINET interfaces, for example, CPU 1516-3 PN/DP.

One PROFINET interface can be used for PROFINET IO communication while the others are being used for communication with a higher-level network (backbone, router or Internet) or for communication with a different machine or automation cell, for example.

Please note that some settings can be changed only at interface X1 and are read-only at the other interfaces (for example, X2), see below.

###### CPUs as of firmware V2.0 with multiple PN IO interfaces

Central processing units as of CPU 1515 with firmware version V2.0 and higher have two PROFINET IO interfaces:

- you can operate two separate PROFINET IO systems as each of the PN IO interfaces supports the IO controller function.
- The PROFINET interface X1 supports real-time classes IRT and RT, and PROFINET interface X2 supports RT.
- Both PROFINET interfaces support the I-device function.
- The 2nd or the 3rd PROFINET interface has restrictions compared to the 1st PROFINET interface (X1):

  - Establishment of redundant ring structures not possible
  - IRT not possible (RT at the PROFINET interface X2 possible, but selection of the send clocks and the number of connectable IO devices restricted)

  Details about the performance capability of the individual interfaces are available in the respective manuals for the individual CPUs.

The following section shows how two CPUs operate their machine networks at the PROFINET interface X1. Operation of the machine networks also works with isochronous real time (IRT).

For coordination purposes, each PROFINET X2 interface is connected to a plant network that is separate from the local machine network: multiple "Sub_Machines" are connected to a "Main_Machine" with the I-device function.

![CPUs as of firmware V2.0 with multiple PN IO interfaces](images/86761407115_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Plant network |
| ② | The CPU is both the IO controller in the plant network (interface X2) and the IO controller in the machine network (interface X1). The machine network can be operated with IRT. |
| ③ | The CPU is both the I-device in the plant network (interface X2) and the IO controller in the machine network (interface X1). |
| ④ | Machine network |

###### Rules

The following applies to an S7-1500 CPU with several PROFINET interfaces:

- For CPUs with multiple PROFINET interfaces **with firmware version V2.0 or higher**, the second PROFINET interface (X2) also supports IO functionality with real-time class RT, in other words the roles of IO controller and IO device.

  In addition, the second and all further PROFINET interfaces (for example X2) supports HMI communication, communication with the configuration system, communication with a higher-level network (backbone, router, Internet) and communication with another machine or automation cell. In addition, the following is supported: Send topology via LLDP protocol, manage LLDP MIBs, reply to and manage SNMP requests as well as the "Accessible devices" function (DCP protocol).
- The following applies for CPUs with **firmware versions < V2.0**: The second or all other PROFINET interfaces (for example X2) do not support any IO functionality, meaning no IO controller/IO device role. HMI communication, communication with the configuration system, communication with a higher-level network (backbone, router, Internet) and communication with another machine or automation cell are supported. In addition, the following is supported: Send topology via LLDP protocol, manage LLDP MIBs, reply to and manage SNMP requests as well as the "Accessible devices" function (DCP protocol).
- The IP subnets of all interfaces must be different. This means that the subnet part of all interface IP addresses must be different.

  Advantages regarding communication across several PROFINET interfaces only apply when the interfaces are in different IP subnets.

  The subnet mask which you also configure during the IP addressing co-determines whether the IP subnets of the two interfaces are different or not.

  When the CPU addresses an Ethernet station, it decides over which interface the respective data packages are sent or received based on the rules described in RFC 4632.

  Example: Both IP addresses are in different subnets

  - Subnet mask of both interfaces: 255.255.255.0
  - IP address of the first interface: 192.168**.0**.10
  - IP address of the second interface: 192.168.**1**.10

  Negative example: Both IP addresses are in the same subnet

  - Subnet mask of both interfaces: 255.255.0.0
  - IP address of the first interface: 192.168.0.10
  - IP address of the second interface: 192.168.1.10
- The interfaces can be connected to the same physical network (a physical network with two logical subnets, which means with two IPv4 networks.)
- Only one router may be effective at any time. The IP address of the router must be located in the IP subnet of the PROFINET interface on which the router is configured.
- The name of the interface and the name of the device (CPU) are used in the automatic assignment of the device name. Example: plc_1.profinet interface_1
- Time-of-day synchronization: The activation of the synchronization and the settings for the NTP servers can only be made on the PROFINET interface X1. The settings are applied for the interface X2 and additional interfaces (read-only there).
- Keep-alive option: For the activation of the advanced option "Send keepalives for connections ... ", the same applies as for the time-of-day synchronization: Can be activated only at interface X1, read-only at interface X2 and additional interfaces.

###### Go online

If you want to use a PG/PC with STEP 7 to access a CPU with two or three PROFINET interfaces online, the following activities then run in the background:

- While establishing the online connection, STEP 7 checks whether one of the PROFINET interfaces connected to the S7 subnet is located in the same IP subnet as the IP address (= IP address of the online access of the PG/PC) and then uses this IP address/PROFINET interface to go online.
- If none of the PROFINET interfaces is located in the same IP subnet, STEP 7 goes online via the PROFINET interfaces for which a router is configured.
- If these requirements are not met, STEP 7 prompts the user to change the IP subnet address of the PG/PC interface so that the PG lies in the same IP subnet.

---

**See also**

[Multiple assignment of IO controllers](Special%20PROFINET%20configurations.md#multiple-assignment-of-io-controllers)
  
[IP forwarding](Configuring%20devices%20and%20networks.md#ip-forwarding)
  
[Virtual interface for IP-based applications](Configuring%20devices%20and%20networks.md#virtual-interface-for-ip-based-applications)

##### Limitation of the data infeed into the network (S7-1500)

###### Limiting the data infeed into the network on PROFINET interfaces

The "Limit data infeed into the network" function limits the network load of standard Ethernet communication which is fed into the network by the interface to a maximum value. This does not apply to cyclic real-time communication (RT/IRT).

With a line topology, critical network loads can occur quickly with standard Ethernet communication. Devices in a line topology should support the limitation of the data infeed into the network.

Devices that feed in a lot of "Standard Ethernet communication" to the network should not be positioned in a line topology but should be placed directly behind a switch.

In line with the interface, you can enable or disable the function "Limit data infeed into the network". If you use the X1 interface of an S7-1500 CPU as the IO controller or I-device, the "Limit data infeed into the network" function is always enabled. If you are not using the X1 interface of an S7-1500 CPU as IO controller or I-device, you can enable or disable the function. For other interfaces, you can always enable or disable the "Limit data infeed into the network" function.

###### Uses of the limitation of the data infeed to the network

- Fair division of the remaining bandwidth:  
  In PROFINET networks, cyclic and non-cyclic communication share the same network. This means that only a limited bandwidth remains for non-cyclic communication. The limitation of the data infeed ensures that the remaining bandwidth for non-cyclic communication is divided fairly between the devices in the network. The limitation of the data infeed does not solve any global overload problems in the network but it avoids an individual device occupying the entire bandwidth.
- Smoothing peaks in the data infeed:  
  The limitation of the data infeed smoothes peak loads of non-cyclic data (e.g. from Open User Communication, access by the Web server).
- Limitation of problems in data infeed:  
  Devices are not permitted to feed too much network load into a PROFINET network. If applications in a device generate too much data, this data is not forwarded into the PROFINET network. Negative effects (e.g. data loss, communication breakdown) remain limited to the device and its communications partner. Other nodes are not disturbed.

###### Setting limitation of the data infeed into the network for a CPU

To set the limitation of the data infeed into the network, follow these steps:

1. In the network view of STEP 7, select the interface of the CPU.
2. In the Inspector window, go to "Properties" > "General" > "Advanced options" > "Interface options".
3. Select or clear the "Limit data infeed into the network" check box.

![Setting limitation of the data infeed into the network for a CPU](images/90142566027_DV_resource.Stream@PNG-en-US.png)

##### IEEE-compliant LLDP (S7-1500)

LLDP stands for "Link Layer Discovery Protocol"; a manufacturer-independent protocol that is defined in the standard IEEE-802.1AB.

Ethernet devices use LLDP to send information about themselves to their neighboring devices in regular intervals. The neighboring devices save this information.

SNMP tools read this data and use it to create the network topology (SNMP stands for "Simple Network Management Protocol").

###### LLDP and IEC 61158

The fieldbus standard IEC 61158 V2.2, or "IEC V2.2" for short, implements LLDP for devices with PROFINET interface. SNMP tools use it to recognize the topology of Ethernet networks to which devices with PROFINET interface are connected.

Devices with several PROFINET interfaces require a new version of this standard, IEC V2.3. Siemens tools and third-party tools use it to detect all interfaces of a device with several PROFINET interfaces.

All networked PROFINET interfaces must be set to the same mode (either IEC V2.3 or IEC V2.2).

When you configure all devices in the PROFINET subnet in one project, STEP 7 automatically sets the correct mode and you do not have to worry about the settings. Below you will find out about the rules STEP 7 uses to automatically make the settings and the cases in which you have to set the mode manually.

###### How do you determine which mode is supported by a PROFINET interface?

You can see which mode is supported by a PROFINET interface in the properties of the PROFINET interface for a selected device or selected interface in the device view or network view. You can find the option "Use IEC V2.2 LLDP mode" in the area "PROFINET interface > Advanced options".

- If the option "Use IEC V2.2 LLDP mode" is selected and cannot be changed, the PROFINET interface only supports V2.2 mode.
- If the option "Use IEC V2.2 LLDP mode" is disabled and can be changed, the PROFINET interface supports V2.2 mode as well as V2.3 mode.

###### Automatic setting of the PROFINET interfaces

STEP 7 sets the mode of the PROFINET interfaces according to the following rules:

- If the devices support IEC V2.3 mode, STEP 7 sets all PROFINET interfaces on the subnet consistently to mode IEC V2.3.
- If only one device supports IEC V2.2 mode, STEP 7 sets all PROFINET interfaces on the subnet to IEC V2.2 mode.

###### Example 1: Automatic setting

In this example, an I-device was created in project 1 and then inserted in project 2 as GSD file (two projects).

Only one device (3) in project 1 supports mode V2.2. STEP 7 therefore set all PROFINET interfaces in this project to mode V2.2 and noted this setting in the GSD file.

The I-device project was then exported in a GSD file (2) and inserted into project 2. STEP 7 automatically set all PROFINET interfaces in project 2 also to mode V2.2 due to the entry in the GSD file.

In this example, the higher-level IO controller configures the lower-level IO system (1).

SNMP tools detect only one interface for each device in this example. Tools from Siemens detect all PROFINET interfaces.

![Example 1: Automatic setting](images/60311151755_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Higher-level IO controller configures the PROFINET interface of the I-device in the IO system A. |
| ② | PROFINET GSD file has entry that only IEC V2.2 mode is supported. |
| ③ | Devices with IEC V2.2 mode force IEC V2.2 mode for all PROFINET interfaces in project 1. |

###### Manual setting of the PROFINET interfaces

The manual setting of a PROFINET interface is required in the following cases:

- You configure a system in two or more projects. A device that only supports V2.2 mode is used in one of the projects (project 1). Only devices in V2.3 mode are used in another project (project 2). In this case, you must set one of the devices in project 2 manually to V2.2 mode.
- You are using two projects. The first project includes an I-device. The second project includes a higher-level IO system in which the I-device is integrated. This case is explained in greater detail below:

###### Setting the IEC mode manually

If the following conditions apply, you must manually set a PROFINET interface to IEC V2.2 mode:

- You configure an I-device and export the project as GSD file.
- You use the GSD file in another project
- You insert the I-device into a higher-level IO system.
- The project with the I-device only uses devices which support V2.3 mode. This mode is set automatically.
- The higher-level IO system includes a device which only supports the standard IEC V2.2.

You force a PROFINET interface of a device in the lower-level IO system into V2.2 mode by executing the following steps.

1. Open the I-device project in STEP 7.
2. Select any device.
3. Enable the option "Use IEC V2.2 LLDP mode" in the area "Interface options".

Then, generate the GSD file once again. Use the new GSD file in the higher-level IO system.

Download the new I-device configuration to the I-device CPU.

###### Example 2: Setting the IEC mode manually

**Project 1**: You have created an I-device in the project.

All PROFINET interfaces support V2.3 mode.

This means STEP 7 did not change the mode of the PROFINET interfaces and noted mode V2.3 in the GSD file (2).

**Project 2**: I-device from project 1 is inserted (GSD file).

One device only supports V2.2 mode.

This means STEP 7 sets all PROFINET interfaces in this project to V2.2 mode.

The PROFINET interfaces in project 1 and 2 have different settings.

This means you have to open the I-device project (project 1) in STEP 7 again and manually set a PROFINET interface to V2.2 mode.

You set a PROFINET interface of a device in the lower-level IO system to V2.2 mode by executing the following steps.

1. Open the I-device project in STEP 7.
2. Select any device.
3. Enable the option "Use IEC V2.2 LLDP mode" in the area "Interface options".

Then, generate a new GSD file. Insert the new GSD file in the higher-level IO system (project 2).

Download the project to the I-device CPU once again.

SNMP tools detect only one interface for each device in this example. Tools from Siemens detect all PROFINET interfaces.

If you do not change the setting of the PROFINET interface, each interface sends a diagnostics alarm during runtime (during operation).

![Example 2: Setting the IEC mode manually](images/60485886987_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | The PROFINET interfaces of the I-device have different settings (the PROFINET interface in IO system A is set to V2.2 mode; the PROFINET interface in the IO system B is set to V2.3 mode). |
| ② | GSD file has entry that the I-device only supports IEC V2.3 mode. |
| ③ | IO device 2 only supports V2.2 mode. This means STEP 7 sets all other PROFINET interfaces in project 2 to this mode (including the PROFINET interface of the I-device in IO system A). |

###### Example 3: Setting the IEC mode manually

This example is largely the same as example 2.

Only difference: The settings of the PROFINET interfaces are stored in the I-device (no parameter assignment by the higher-level IO controller as in example 2).

The PROFINET interfaces have different settings in IO system A (I-device set to V2.3, IO controller set to V2.2, IO device 2 only supports V2.2).

This means you must set a PROFINET interface in IO system B to V2.2 mode.

You set a PROFINET interface of a device in the lower-level IO system to V2.2 mode by executing the following steps.

1. Open the I-device project in STEP 7.
2. Select any device.
3. Enable the option "Use IEC V2.2 LLDP mode" in the area "Interface options".

Then generate a new GSD file and use the new GSD file.

Download the new I-device configuration to the I-device CPU.

![Example 3: Setting the IEC mode manually](images/60314461579_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | The PROFINET interfaces have different settings in IO system A (I-device set to V2.3, IO controller set to V2.2, IO device 2 only supports V2.2). |
| ② | The settings of the PROFINET interfaces are stored in the I-device (no parameter assignment by the higher-level IO controller). |
| ③ | GSD file has entry that IEC V2.3 mode is set. |
| ④ | All devices are automatically set to V2.3 mode: This means you must set a PROFINET interface in project 1 manually to V2.2 mode. |

### Time-of-day functions (S7-1500)

This section contains information on the following topics:

- [Basic principles of time of day functions (S7-1500)](#basic-principles-of-time-of-day-functions-s7-1500)
- [Setting and reading the time of day (S7-1500)](#setting-and-reading-the-time-of-day-s7-1500)
- [Time synchronization SIMATIC procedure (S7-1500)](#time-synchronization-simatic-procedure-s7-1500)
- [Time-of-day synchronization in NTP mode (S7-1500)](#time-of-day-synchronization-in-ntp-mode-s7-1500)

#### Basic principles of time of day functions (S7-1500)

All S7-1500 CPUs are equipped with an internal clock. The backup supports the display of the correct time for up to 10 hours if the power supply is interrupted.

##### Time-of-day format

The clock always shows the time-of-day with a resolution of 1 millisecond and the date including the day of the week. The time adjustment for daylight saving time is also taken into account.

---

**See also**

[Setting and reading the time of day (S7-1500)](#setting-and-reading-the-time-of-day-s7-1500)

#### Setting and reading the time of day (S7-1500)

##### Setting and reading the time with instructions

You can set, start and read the time and date on the CPU clock with the following instructions in the user program:

- Set the time: "WR_SYS_T"
- Read time "RD_SYS_T"
- Read local time "RD_LOC_T"
- Write local time "WR_LOC_T"

##### Manual setting

You can also read and set the time manually in the online and diagnostics view under "Functions > Set time".

---

**See also**

[WR_SYS_T: Set time-of-day (S7-1200, S7-1500)](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#wr_sys_t-set-time-of-day-s7-1200-s7-1500)
  
[RD_SYS_T: Read time-of-day (S7-1200, S7-1500)](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#rd_sys_t-read-time-of-day-s7-1200-s7-1500)
  
[RD_LOC_T: Read local time (S7-1200, S7-1500)](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#rd_loc_t-read-local-time-s7-1200-s7-1500)
  
[WR_LOC_T: Write local time (S7-1200, S7-1500)](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#wr_loc_t-write-local-time-s7-1200-s7-1500)
  
[SET_TIMEZONE: Set time zone (S7-1200, S7-1500)](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#set_timezone-set-time-zone-s7-1200-s7-1500)

#### Time synchronization SIMATIC procedure (S7-1500)

##### Reference

Assigning parameters for the interface properties in the "Properties > General > DP interface > Time synchronization" parameter group.

##### SIMATIC procedure

With the SIMATIC procedure, the time of day is set according to MMS time-of-day messages (MMS - Manufacturing Message Specification). The MMS time-of-day messages come from a SIMATIC time-of-day transmitter or a CPU that is configured as a time master.

With a CP, the time-of-day messages can either be received by the local CPU or via LAN. It is possible to set whether or not the CP forwards the received time-of-day.

Compared with an NTP method that may be available, the SIMATIC mode provides higher accuracy.

##### Clock parameters

The clock parameters allow you to make the following settings:

- Synchronization type

  If you have set the synchronization mode to "As master", you can then select the time interval for automatic synchronization.

  If more than one module with a clock is present within a network, you need to specify which CPU will act as the master and which as the slave for time synchronization purposes. There can only be one time master.
- Time interval

  The time interval defines the interval between time queries.

##### Instructions for synchronizing the time

To ensure that the time is consistent in all modules in the network, the time slaves are updated by the system program at regular configurable intervals. The instruction "SNC_RTCB" allows the date and time to be transferred from the time master to the time slave independently of the configured time interval.

#### Time-of-day synchronization in NTP mode (S7-1500)

##### Reference

Assigning parameters for the interface properties in the "Properties > General > PROFINET interface > Time synchronization" parameter group. The "Enable time synchronization via NTP server" option is selected.

##### NTP mode (NTP: Network Time Protocol)

In NTP mode, the device sends time queries at regular intervals (in client mode) to the NTP server in the subnet (LAN). Based on the replies from the server, the most reliable and most accurate time is calculated and the time on the station is synchronized.

The advantage of this mode is that it allows the time to be synchronized across subnets.

The IP addresses of up to four NTP servers need to be configured. The update interval defines the interval between the time queries (in seconds). The value of the interval ranges between 10 seconds and one day.

In NTP mode, it is generally UTC (Universal Time Coordinated) that is transferred; this corresponds to GMT (Greenwich Mean Time).

##### Time synchronization parameters in NTP mode

The clock parameters allow you to make the following settings:

- Enable time synchronization via NTP server

  Select this check box if you want the internal clock to be synchronized using the NTP synchronization mode.
- Server 1-4

  The IP addresses of up to four NTP servers need to be configured.
- Update interval

  The update interval defines the interval between time queries.

### Enabling system memory (S7-1500)

#### System memory

A system memory is a bit memory with defined values.

You decide which memory byte of the CPU will become the system memory byte when assigning the system memory parameters.

#### Benefits

You can use system memory in the user program, for example to run program segments in only the first program cycle after start-up. Two system memory bits are constant 1 or constant 0.

#### Bits of the system memory bytes

The following table shows the meaning of the system memory:

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Bit of the system memory bytes | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| Meaning | Reserved (=0) | Reserved (=0) | Reserved (=0) | Reserved (=0) | =0 | =1 | =1 with change to the diagnosis status | =1 during the startup and in first program cycle after startup, otherwise 0 |

> **Note**
>
> **System memory bit 1**
>
> After changing a diagnostic information, the diagnostic status change bit is 1 for the duration of a cycle. If, for example, the CPU receives the diagnosis "short circuit on channel 2" from one of the modules, the bit will be present for one cycle. If the diagnostic message returns to the channel after the short-circuit has been rectified, the bit will again be present for one cycle.

> **Note**
>
> The selected memory byte cannot be used for intermediate storage of data.

### Using clock memory (S7-1500)

#### Clock memory

A clock memory is a bit memory that changes its binary status periodically in the pulse-no-pulse ratio of 1:1.

You decide which memory byte of the CPU will become the clock memory byte when assigning the clock memory parameters.

#### Benefits

You can use clock memory, for example, to activate flashing indicator lamps or to initiate periodically recurring operations such as recording of actual values.

#### Available frequencies

Each bit of the clock bit memory byte is assigned a frequency. The following table shows the assignment:

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Bit of the clock memory byte | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| Period (s) | 2.0 | 1.6 | 1.0 | 0.8 | 0.5 | 0.4 | 0.2 | 0.1 |
| Frequency (Hz) | 0.5 | 0.625 | 1 | 1.25 | 2 | 2.5 | 5 | 10 |

> **Note**
>
> Clock memory runs asynchronously to the CPU cycle, i.e. the status of the clock memory can change several times during a long cycle.
>
> The selected memory byte cannot be used for intermediate storage of data.

### Protection & Security (S7-1500)

This section contains information on the following topics:

- [Using the Security settings wizard (S7-1500)](#using-the-security-settings-wizard-s7-1500)
- [Protection of confidential configuration data (S7-1500)](#protection-of-confidential-configuration-data-s7-1500)
- [Settings for users and roles (S7-1500)](#settings-for-users-and-roles-s7-1500)
- [Password transfer upon module replacement (S7-1500)](#password-transfer-upon-module-replacement-s7-1500)
- [Restriction of communication services (S7-1500)](#restriction-of-communication-services-s7-1500)
- [Connection mechanisms (S7-1500)](#connection-mechanisms-s7-1500)
- [Group alarms for security events (S7-1500)](#group-alarms-for-security-events-s7-1500)
- [Disabling online access to the CPU via the display (S7-1500)](#disabling-online-access-to-the-cpu-via-the-display-s7-1500)
- [Certificate manager (S7-1500)](#certificate-manager-s7-1500)
- [Syslog (S7-1500)](#syslog-s7-1500)

#### Using the Security settings wizard (S7-1500)

When you add a CPU to the project that supports secure PG/HMI communication in the TIA Portal from the hardware catalog, a wizard starts for the security settings of the CPU.

The wizard guides you step-by-step through the following CPU settings:

- Password to protect confidential PLC configuration data
- PG/PC and HMI communication mode
- Access level

Each of these settings is explained in detail in the wizard. At the end, all settings are once again summarized in an overview.

The wizard also starts, for example, when you replace a module in the network view of the TIA Portal and the new CPU, unlike the replaced CPU, supports secure PG/HMI communication.

All settings in the wizard are applied in the Inspector window (CPU properties).

You can start the wizard at any time using a Start button in the "Protection & Security" area of the CPU properties.

---

**See also**

[Protection of confidential configuration data (S7-1500)](#protection-of-confidential-configuration-data-s7-1500)
  
[What you should know about the access levels (S7-1500)](#what-you-should-know-about-the-access-levels-s7-1500)
  
[Connection mechanisms (S7-1500)](#connection-mechanisms-s7-1500)
  
[Configuring access levels (S7-1500)](#configuring-access-levels-s7-1500)
  
[Protection of confidential configuration data (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#protection-of-confidential-configuration-data-s7-1200-s7-1500-s7-1500t)

#### Protection of confidential configuration data (S7-1500)

As of STEP 7 V17, you have the option of assigning a password for protecting confidential configuration data of the respective CPU. This refers to data such as private keys that are required for the proper functioning of certificate-based protocols.

It is possible to do without the password if you have implemented measures to prevent unauthorized access to the TIA Portal project and the configuration of the CPU.

A description of the concept as well as detailed information on handling the password protection for confidential PLC configuration data (resetting, changing, information on spare parts) can be found in the requirements for secure communication (also in the function manual S7-1500 Communication).

##### Procedure

1. Open the CPU properties in the network view or in the device view.
2. Navigate to the area "Protection & Security > Protection of the PLC configuration data".

   **Result:** The "Protect confidential PLC configuration data" option is enabled first and the empty field for password entry is highlighted in red.
3. Configure the password (recommended) via the "Set" button or disable the "Protect confidential PLC configuration data" option.
4. Complete the configuration and create the user program.
5. Load the CPU.   
   When loading the hardware configuration, you will be asked once to re-enter the password.   
   **Background**: The configured password is used in the TIA Portal to generate the key information to protect confidential configuration data and thus to protect this data. For security reasons, however, neither the password nor the key information is saved in the project. In order for the key information to reach the CPU, it is re-generated when the hardware configuration is loaded, so that the password must be entered once at this point.

##### Tips and rules

- Manage your passwords in a password manager.
- Use TIA Portal's password policy verification settings to check newly entered passwords for compliance and prevent trivial passwords, for example:

  - In the project tree, navigate to the area "<Project name> > Security settings > Settings" area and select the "Password policies" area.
  - Specify, for example, the minimum number of characters the password must have or the minimum number of special characters.
- You do not have to assign different passwords for each CPU in a system or machine. If the requirements are met, you can also define the same password for a group of CPUs. This strategy also has advantages in the replacement parts scenario: If the group password is also assigned to the replacement CPU, the workload of replacing the CPU is reduced.

  Note here the risk that if the password of one of these CPUs is compromised, all CPUs with the same password are vulnerable.
- The definition of passwords also has an impact on the replacement parts scenario (see [Rules for the replacement parts scenario](Configuring%20devices%20and%20networks.md#rules-for-the-replacement-parts-scenario-s7-1200-s7-1500-s7-1500t)).
- With **S7-1500R/H CPUs**, the password for confidential PLC configuration data is only loaded onto one of the two CPUs during loading. In order that the sync-up process works and that the partner CPU also works properly, the password must also be transferred to the partner CPU, using the Online and Diagnostics editor:

  - In the Online and diagnostics view, you specify the area "Password to protect confidential PLC configuration data".
  - Enter the required password and click the "Set" button.

    If the correct password has been entered, the partner CPU can use the protected PLC configuration data and start the sync-up process.

---

**See also**

[Requirements for secure communication (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#requirements-for-secure-communication-s7-1200-s7-1500-s7-1500t)

#### Settings for users and roles (S7-1500)

This section contains information on the following topics:

- [Useful information on the local user administration and access control (S7-1500)](#useful-information-on-the-local-user-administration-and-access-control-s7-1500)
- [Advantages of the local user administration and access control (S7-1500)](#advantages-of-the-local-user-administration-and-access-control-s7-1500)
- [From the access level to the function right of users (S7-1500)](#from-the-access-level-to-the-function-right-of-users-s7-1500)
- [Information about compatibility (S7-1500)](#information-about-compatibility-s7-1500)
- [What you should know about the access levels (S7-1500)](#what-you-should-know-about-the-access-levels-s7-1500)
- [Configuring access levels (S7-1500)](#configuring-access-levels-s7-1500)

##### Useful information on the local user administration and access control (S7-1500)

As of TIA Portal version V19 and CPU firmware version V3.1 (V4.7 for S7-1200), S7-1500 and S7-1200 CPUs have improved management of users, roles and CPU function rights (User Management & Access Control, UMAC). Software controller from version V30.1 also have this function.

From the versions mentioned above onwards, you manage all project users along with their rights (for example, access rights) for all CPUs in the project in the editor for users and roles of the project in the TIA Portal:

- Navigate to the "Security Settings > Users and roles" area in the project navigation to manage users with their rights, for example, to control access rights.

The TIA Portal saves the assignment of the function rights of a CPU to user-defined roles and the assignment of these roles to users for each CPU. There are no system-defined roles with predefined function rights for CPUs.

After loading the configuration, the user management becomes effective in the respective CPUs. After loading, every CPU "knows" who may access which service and execute certain functions.

This new feature is also called "local user management and access control" below.

> **Note**
>
> **No global user support for CPU function rights**
>
> Another option for user management in the TIA Portal is the central user management UMC (User Management Component). With this component you manage global users on connected servers, e.g. also via the connection of an MS Active Directory. The authentication is then implemented via UMC. A global user management for CPU-specific function rights via UMC is currently not supported.

###### Users, roles and function rights - details of new features

Users and roles were already being managed in the predecessor version by TIA Portal under "Security settings > Users and roles". In addition to the existing user management for HMI devices, for example, you can also manage all CPU function rights via this editor as of TIA Portal Version V19.

The CPU function rights are valid during runtime. Therefore, these rights are located in the "Runtime rights" tab in the editor for users and roles. For each CPU in the project, there is a section with all CPU function rights to choose from - separated according to CPU services such as PG/HMI communication (engineering access, access levels), web server and OPC UA.

In addition to the user management for projects, there were additional user managements for web servers and OPC UA servers (static user management for CPUs up to FW version V3.0) in the properties of the CPU:

- User for the OPC UA server (authentication)
- User for the web server (authentication and access control)

These additional user managements are integrated in the local user management in the project navigation as of TIA Portal V19 and as of CPU FW version V3.1.

###### Introduction to the local user management and access control

For CPUs up to firmware versions V3.0 (S7-1500) or V4.6 (S7-1200), you managed the users under the respective CPU properties separated according to services such as "Web server" und "OPC UA". Web server users were parameterized in the "Web server" area, OPC UA users in the "OPC UA" area.

To restrict the PG/HMI access to the CPU at different levels, you configured passwords for the corresponding access levels. With this procedure, for example, HMI accesses could be permitted without restriction, but write accesses could be made dependent on the knowledge of a password. You have agreed passwords for the different access levels in the "Protection & Security" area of the CPU properties. The access protection therefore always related to groups that have the appropriate passwords - not to individual users.

With the introduction of the local user management and access control from TIA Portal version V19 onwards, you can use the "Security settings > Users and roles" area in TIA Portal in the project navigation for all users and their roles and function rights of a CPU. This also applies to the access protection for engineering/HMI access, which as of TIA Portal version V19 no longer works via access levels with password protection by default, but also via user management.

More information on the new access protection is available [here](#from-the-access-level-to-the-function-right-of-users-s7-1500).

As already introduced for engineering rights, for example, you use the role assignments for combining individual function rights. In a further step, you assign the roles to individual users. All the function rights which were assigned to a user via roles and which the user can exercise for the corresponding CPU are listed In the "Assigned rights" tab.

The following figure shows an example of the available and activated function rights of a CPU. At least one user must have full access to the CPU, otherwise the configuration cannot be compiled. To do this, first, a role with full access to the CPU must be created.

![Introduction to the local user management and access control](images/172103234187_DV_resource.Stream@PNG-en-US.png)

The following image displays the assignment of the role with full access to a user ("Admin").

![Introduction to the local user management and access control](images/172127982219_DV_resource.Stream@PNG-en-US.png)

###### Requirement

CPU parameterization: To be able to use users, roles and function rights for a CPU, the "Enable access control" option in the "Protection & Security > Access control" tab must be checked.

No project protection is required for local user management.

###### Default characteristics

The "Activate access control" option is preset for the access control. Users, with their assigned passwords as well as their roles and function rights, can be parameterized.

###### Downloading to device

You can load configuration changes with regard to the local user management and access control in the STOP and RUN mode of the CPU.

###### Runtime timeout

You can set a runtime timeout for both the role and the user in 'Security Settings > Users and Roles'.

For an S7-1500 CPU, these settings are taken into account by the various services as follows:

- By means of the Web API you can, for example, create a web page or application that takes the settings for the runtime timeout into account. Standard web pages do not take the settings for runtime timeout into account and use the default value.
- The other services (PG/HMI communication and OPC UA server) do not use the runtime timeout; the logged-in user is not logged out after the set time.

---

**See also**

[Basics of user management in the TIA Portal](Managing%20users%20and%20roles.md#basics-of-user-management-in-the-tia-portal)

##### Advantages of the local user administration and access control (S7-1500)

The following section discusses the advantages which the new local user management for S7-1200/S7-1500 CPUs provides, and what changes for you.

###### Quick activation/deactivation of the local user management

The options for user management are located in the "Protection & Security > Access control" tab:

- Access control deactivated: Every user has full access to all functions with the exception of the GDS Push function for the online transfer of certificates.

  | Symbol | Meaning |
  | --- | --- |
  |  | **Danger** |
  | **Disabled access control carries the risk of unauthorized access and thus the risk of personal injury and property damage.**   Only use this setting in a protected environment, for example during commissioning. |  |
- Access control enabled: The configured users with their assigned roles and concomitant linked function rights become effective after loading.

###### Access protection for PG/HMI accesses, now with user authentication

While it was possible to parameterize passwords for access levels for CPUs with firmware versions < V3.1 (S7-1500 CPUs) or < V4.7 (S7-1200 CPUs), with the current CPUs, you have the possibility to configure users with the corresponding function rights. This means that the authentication options for PG/HMI access correspond to the options offered by OPC UA or web server accesses.

###### All in one place

Irrespective of the service for which you configure users, roles and rights for a CPU: You have to manage the data at the same location.

All users, no matter if you manage their engineering rights for the project or their local runtime rights for each CPU in the project, can be found in the editor for users and roles in the project navigation.

###### Powerful password functions

- Support for compliance with complexity rules for password creation:   
  Right from the password creation stage, you can have the TIA Portal check compliance with complexity rules (such as the password length, uppercase/lowercase letters) (project navigation, "Security settings > Settings" area).  
  The complexity rules are also saved in the CPU upon loading the user management. When the password is changed online, the CPU determines and considers these rules. This prevents a user from overriding the complexity rules set by the configuration engineer and assigning a non-secure password.
- The period of validity of passwords is adjustable:   
  To ensure that a user does not have access to the CPU with a compromised password for an unlimited time, you can parameterize a period of validity. Before the period of validity expires, the remaining time is then displayed on login so that each user has the possibility to change their password in time.

###### Loading the user management during operation

From firmware version V3.1 onwards, you can load certain security-relevant configuration data both in the STOP operating state and in the RUN operating state. Therefore, loading the hardware configuration does not necessarily result in a STOP of the CPU.

You can make the following changes in the STOP operating state as well as in the RUN operating state (Download to device > Hardware configuration):

- Local user management extended/changed
- TIA Portal-configured certificates added/modified
- Syslog configuration changed

If you have made additional changes to the hardware configuration (for example, adding modules, re-parameterization, ...), then the CPU automatically prompts for the STOP state before loading.

Therefore, when you load just one user with modified roles/function rights to the CPU, for example, this process does not require any STOP state of the CPU.

The preview dialog for loading contains a security area so that you can determine when loading how the CPU should deal with user data that has changed in the meantime (not when loading for the first time). This allows changes to user data (e.g. password changes during runtime) to be retained.

###### Loading the device as a new station - with user data

If you load an already configured CPU into a new project, for example, because you do not have the original project, the user data is loaded into the project and is available for further processing of the CPU settings.

###### Changing of passwords during operation

You can use the web server API to write an application with which each user can change their password at runtime, provided that the original password was entered correctly and the new password corresponds to the set password guideline.

**Requirement**: You have enabled access control for the CPU.

Users can change their own password at any time, even if the password has expired. If the password has expired, the user must change the password. Login will not be possible with an expired password.

API methods used:

- Api.ChangePassword
- Api.GetPasswordPolicy

More information on the API methods is available in the function manual Web Server for S7-1500 CPUs.

> **Note**
>
> **Passwords changed at runtime take priority over loaded passwords**
>
> If you have changed your password during running operation and subsequently load your project, the password assigned during runtime takes precedence over the password set in the project (default setting).
>
> If you want to overwrite the passwords changed during runtime by loading the project, you have to select the option "Load all user management data (reset to project data)". In this case, **all** passwords changed during runtime will be lost.

##### From the access level to the function right of users (S7-1500)

The following section shows how to implement access protection with the new local user management for CPUs.

###### Access levels as function rights

Where, in the case of S7-1500 CPUs up to FW version V3.0 (S7-1200: V4.6), access could only be controlled via passwords, for CPUs from FW version V3.1 (S7-1200: V4.6), you can create the corresponding users and roles with the necessary function rights for the access control. The assignment between access level and the associated function right results from the already known access levels:

- Users who are to have full access must have a role with the function right "Full access", or "Full access incl. failsafe" for F-CPUs.

  A CPU configuration can only be compiled and loaded if at least one user has the function right "Full access" or "Full access incl. failsafe".
- Users who are to have read access must have a role with the function right "Read access".
- Users who are to have HMI access must have a role with the function right "HMI access".

If a user does not have any of these specified function rights, that user also has no access to the CPU.

The hierarchical organization of the access levels also remains the same for the corresponding function rights:

- A user with full access also has the function rights "Read access" and "HMI access".
- A user with read access also has the function right "HMI access".

###### Continuing to use access levels

Even though the new local user management replaces the usual access protection via corresponding function rights of individual users, there is still the possibility to continue to use this familiar access protection. This is required, for example, for HMI devices which only support access levels and which do not benefit yet from possibilities of the new user management.

If you require the configuration of an access level, for example, to ensure an HMI device access even without user or password access, you have to activate the "Use legacy access control via access levels" option in the CPU properties.

> **Note**
>
> **User for OPC UA and for the web server**
>
> Regardless of the access protection, you always have to configure the users for the web server and for the OPC UA server in the project tree ("Security settings > Users and roles" area).

###### Restrictions on continued use of the access levels

When using the "Legacy access control" option, you cannot select the access level directly in the table for setting the access levels. This selection can only be set for the new local user management in one way: Via the access protection function rights of the "Anonymous" user.

The local user "Anonymous" is created in a project by the system by default. With the help of this user, you determine the behavior of the CPUs in the project for someone who logs in without a user name and password. For security reasons, the anonymous user is deactivated and needs to be activated before use.

The area where you set the access levels leads you via a link to the editor for the required settings for the "Anonymous" user.

**Examples**:

- If the "Anonymous" user is deactivated or if the "Anonymous" user is activated and no function rights are assigned to that user, then nobody can log in without a user name and password (corresponds to the access level "No access (complete protection")).
- If the "Anonymous" user is activated and the "Full access" function right for a CPU is assigned to that user via a corresponding role, the result of this setting is "No protection". You can achieve the same effect with regard to access protection by setting "No access protection" in the "Protection & Security" area of the CPU properties.

###### Procedure

To activate the "Legacy access control" and set the required access level, follow these steps:

1. In the CPU properties, go to "Protection & Security > Access control".
2. Select the option "Activate access control" and, in addition, select the check box "Use legacy access control via access levels" check box.

   The access level selection cannot be used in this setting. You have to set the access level via the "Anonymous" user of the CPU.

   The "Anonymous" user is disabled in the default setting. This means that the resulting access level for users without a password is "No access (complete protection)" (default setting).
3. Go to "Security Settings > Users and roles" in the project navigation.
4. Activate the "Anonymous" user, if you want to set a different access level than "No access (complete protection)". You can assign a role with function rights that grants access to the CPU without password input, only to the activated "Anonymous" user.
5. You cannot assign function rights for a CPU directly to a user. You must first assign a role:  
   Therefore switch to the "Roles" tab and add a new role. Assign a meaningful name, e.g. "PLC1-Read-Access-Role". If you assign this role to a user, this user should have read access to PLC1 during operation.
6. Assign the required function right for the access to the CPU with the name "PLC1" to the role "PLC1-Read-Access-Role" - in this case "Read access".
7. Switch to the "User" tab and assign the "PLC1-Read-Access-Role" role to the activated "Anonymous" user.

   **Result**: The "Anonymous" user has read access for PLC1. This means that the access level tables of the CPU "PLC1" in the project are preset to "Read access" (cannot be changed) and users who are not logged in only have read access.

   For full access, or full access including fail-safe, you have to configure a password for the full access in the table for the access protection. Users who need full access to the CPU during runtime via an action, e.g. because a project is to be loaded onto the CPU, must legitimize themselves for this action with this password.

###### Tip

To make the user rights transparent, use meaningful names for the respective roles. You create users and roles for the entire project; you must select the function rights of a role individually for each CPU in the project. With a descriptive name you can, for example, immediately see which CPUs have read access and which CPUs are fully protected.

##### Information about compatibility (S7-1500)

In the following sections, you will find information on the behavior of the CPUs with the local user management, e.g. when replacing modules in STEP 7 and for further use of projects and programs without local user management.

###### Replacement part scenario

If you replace a CPU with a firmware version < V3.1 with a CPU with a firmware version V3.1 or higher, the program stored on the memory card runs like the original CPU. The behavior with regard to the configured access levels, the users for the OPC UA server and the web server corresponds to the behavior of the previous CPU.

In this case, the "Change password function" via the web server API is not accepted by the CPU because the CPU has been configured for firmware version < V3.1 and has no local user management.

###### Replace CPU (upgrade)

If you replace a CPU (FW < V3.1) with a current CPU (FW V3.1 or higher) in the TIA Portal, this has the following effects on the configured user data:

- The user data from the OPC UA server and web server is transferred to the "Users and roles" editor in the project navigation.

  | Symbol | Meaning |
  | --- | --- |
  |  | **Notice** |
  | **Passwords are lost when replacing the CPU**  Before replacing the CPU, make sure that the passwords are available. They must be entered again in the "Users and roles" editor. Otherwise, you have to assign new passwords and inform the users. |  |
- A corresponding role is created for each web server user in the "Users and roles" editor; the name of the role contains the CPU name, the "Web" string and the already configured web server user name. In this way, by assigning these roles in the "Users and roles" editor, you can easily restore the original rights for each CPU.
- The "OPC UA server access" role is created for each OPC UA server user.
- OPC UA guest access and the web server "Everybody" are migrated to the "Anonymous" user.
- Each OPC UA user and each web server user is listed in the "User" column in the editor for users and roles. If the names are the same (web server and OPC UA user), only one user is created.
- With a protected project, you can select which action the CPU performs:

  - Migrate user (requirement: You are logged in as a user with the right to manage users and roles and the right to edit the project/configuration)
  - Remove user
- The "Legacy access control via access levels" option is set for access protection.

###### Replace CPU (downgrade)

If you replace a CPU (as of FW V3.1) with a previous CPU (< FW V3.1) in the TIA Portal, this has the following effects on the configured user data:

- The local user management is no longer available.
- Users of the web server with their roles and function rights remain in the "Users and roles" editor. They are not transferred to the area of the CPU properties (Web server > User management) and are not in effect.
- Users of the OPC UA server with their roles and function rights remain in the "Users and roles" editor. No users are moved to the "OPC UA" area of the CPU parameters.

  With regard to the settings for user authentication, the default setting applies again (OPC UA > Server > Security > User authentication): Guest authentication is enabled.
- It is no longer possible for users to change passwords during runtime (via web server API).

##### What you should know about the access levels (S7-1500)

###### Access levels

The following section describes how to use the various access levels of the S7-1200/1500 CPUs. The description applies to S7-1200 CPUs up to firmware version V4.6 or to S7-1500 CPUs up to firmware version V3.0. In later firmware versions, use the local user administration in the editor for users and roles in the project navigation. The access levels are represented there by function rights of the same name, which you assign to individual users via roles.

The CPUs provide various access levels to limit the access to specific functions.

The individual access levels as well as their associated passwords are specified in the object properties of the CPU. You assign parameters for the access level in a table.

![Access levels](images/142980549771_DV_resource.Stream@PNG-en-US.png)

The green checkmarks in the columns to the right of the respective access level specify which operations are possible without knowing the password of this access level.

If you want to use the functions of fields that are not selected in the "Access" column, a password has to be entered:

**Example:**

You set the access level "Read access". You can see from the table that write access is not possible during operation without entering a password.

The table also shows that full access is necessary for the "Write" function.

To use a function requiring write access during operation, the password for full access must therefore be entered.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Configuring an access level does not replace know-how protection**  Configuring access levels offers a high degree of protection against unauthorized changes to the CPU by restricting download privileges to the CPU. However, blocks on the memory card are not write- or read-protected. Use know-how protection to protect the code of blocks on the memory card. |  |

###### Default characteristics

The default access level is "No access (complete protection)".

###### The access levels in detail

Below you can find an explanation of the existing access levels and which functions are possible at the respective access level.

- Full access including fail-safe (no protection) - only for F-CPUs:

  Users of STEP 7 and HMI applications have access to all standard and fail-safe functions. A password is not required.

  More information is available in the programming and operating manual SIMATIC Safety - Configuring and Programming.
- Full access (no protection):

  Users of STEP 7 have access to standard functions. HMI applications can access all functions (fail-safe and standard).
- Read access:

  With this access level, read-only access to the hardware configuration and the blocks is possible without entering a password, which means you can upload hardware configuration and blocks to the programming device. In addition, HMI access and access to diagnostics data, display of offline/online comparison results, changing the operating state (RUN/STOP), and setting time-of-day is possible.

  You cannot download blocks or a hardware configuration into the CPU. Moreover, no test functions and firmware updates are possible.

- HMI access:

  Only HMI access and access to diagnostics data possible.

  Example: With the HMI access access level, you can go online and view the diagnostics icons for the states of objects.

  Tags can be read and written via a HMI device.

  At this access level, you can neither load blocks and the hardware configuration into the CPU nor load blocks and the hardware configuration from the CPU into the programming device.

  In addition, the following is **not** possible: Test functions, changing the operating mode (RUN/STOP), firmware update and display of online/offline comparison results.
- No access (complete protection):

  Only identification data can be read, via "Accessible devices", for example.

  Neither read nor write access to the hardware configuration and the blocks is possible. HMI access is also not possible. The server function for PUT/GET communication is disabled in this access level (cannot be changed).

  Legitimation with a configured password provides you with access in accordance with the associated protection level.

###### Behavior of functions at different access levels

The table below describes which online functions are possible in the various protection levels.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Function** | **Full access** | **Read access** | **HMI access** | **No access** |
| Identification of the device, via "Accessible devices", for example | Yes | Yes | Yes | Yes |
| Assigning an emergency address (Emergency IP) | Yes | Yes | Yes | Yes |
|  |  |  |  |  |
| HMI diagnostics view | Yes | Yes | Yes | No |
| Monitoring tags (M, I, Q, DB content) via HMI device | Yes | Yes | Yes | No |
| Modifying tags (M, I, Q, DB content) via HMI device | Yes | Yes | Yes | No |
| Diagnostics display (for example, device information, connection display, alarm display, diagnostic buffer) | Yes | Yes | Yes | No |
| Reading cycle time statistics (Online & Diagnostics) | Yes | Yes | Yes | No |
| Reading information from the hardware configuration (Online & Diagnostics) | Yes | Yes | Yes | No |
| Reading time-of-day | Yes | Yes | Yes | No |
| Executing online functions within the hardware configuration (Online & Diagnostics) | Yes | Yes | Yes | No |
| Acknowledging alarms | Yes | Yes | Yes | No |
| Receiving alarms | Yes | Yes | Yes | No |
|  |  |  |  |  |
| Enabling/disabling alarms | Yes | Yes | No | No |
| Reading tags via test function (STEP 7, tag table or watch table) | Yes | Yes | No | No |
| Requesting operating state change online (RUN/STOP/warm restart) | Yes | Yes | No | No |
| Uploading data blocks, code blocks, hardware configuration to PG/PC | Yes | Yes | No | No |
| Set time-of-day | Yes | Yes | No | No |
| Display online/offline comparison results | Yes | Yes | No* | No |
|  |  |  |  |  |
| Deleting data blocks, code blocks, hardware configuration in the CPU | Yes | No | No | No |
| Downloading individual data blocks, code blocks, hardware configurations to the CPU | Yes | No | No | No |
| Loading PLC program to the device and resetting | Yes | No | No | No |
| Firmware update of CPUs or I/O modules | Yes | No | No | No |
| Modifying tags via test function (STEP 7, watch table) | Yes | No | No | No |
| Reading tags in the program status | Yes | No | No | No |
| Online editing of blocks | Yes | No | No | No |
| Modifying outputs in STOP mode | Yes | No | No | No |
| * As of STEP 7 V14, the "HMI access" access level is not sufficient for the display of online/offline comparison results, as they are for example displayed when going online with a project for blocks, PLC data types or PLC tags. You must have read access in order to have the online/offline comparison results displayed. Reason: The equivalence or non-equivalence of online/offline data is determined by STEP 7 through a comparison of the checksums for software and text lists. Reading these checksums requires the "read access" access level. |  |  |  |  |

###### Behavior of a password-protected module during operation

The CPU protection takes effect after the settings are downloaded to the CPU.

Before an online function is executed, the necessary permission is checked and, if necessary, the user is prompted to enter a password.

**Going online with a password-protected CPU**

Going online with a password-protected CPU requires read access as of STEP 7 V14. When going online, you must therefore enter the password for read access or, if no password was configured here, the password for full access.

If you only have a password for HMI access with a completely protected CPU, cancel the query for the read access password. You are then prompted to enter the password for HMI access. The authorization for HMI access is, however, not sufficient for the online/offline comparison - you require the read access right for this purpose.

**Examples:**

- A module was configured with read access and you want to execute the "Modify tags" test function. Since this requires write access to a test function, the configured password must be entered to execute the function (password for full access).
- A module was configured with HMI access and you want to go online with STEP 7 for this module. Since the data from which STEP 7 determines the equivalence between online and offline objects (checksum) requires read access, you are prompted to enter the password for read access when going online. If you abort the dialog for entering the password, an online connection to the module is nevertheless established. However, only question marks are displayed in the column for comparison icons in an online/offline comparison.

Access authorization to the protected data is in effect for the duration of the online connection. If the online connection is restored after an interruption, you do not have to enter the access data again. To manually cancel access authorization, click "Online > Delete access rights".

Each access level allows unrestricted access to certain functions without entering a password, for example, identification using the "Accessible devices" function.

Access to a password-protected S7-1500 CPU can be restricted locally on the display. The restriction is only in effect when the operating mode switch is set to RUN.

---

**See also**

[Disabling online access to the CPU via the display (S7-1500)](#disabling-online-access-to-the-cpu-via-the-display-s7-1500)
  
[Restriction of communication services (S7-1500)](#restriction-of-communication-services-s7-1500)
  
[Comparison of PLC programs based on checksums](Comparing%20PLC%20programs.md#comparison-of-plc-programs-based-on-checksums)
  
[Protection concept for project data](Editing%20project%20data.md#protection-concept-for-project-data)
  
[Configuring access levels (S7-1500)](#configuring-access-levels-s7-1500)
  
[Protecting blocks](Protecting%20blocks.md#protecting-blocks-1)
  
[Printing project data](Editing%20project%20data.md#printing-project-data)

##### Configuring access levels (S7-1500)

The following section describes how to configure an access level and enter passwords for an S7-1200/1500 CPU.

For a CPU, you can enter multiple passwords and thereby set up different access rights for various user groups.

The passwords are entered in a table in such a way that exactly one access level is assigned to each password.

How the password works is shown in the "Access level" column and in the explanatory text below the table.

###### Example

You select the "No access (complete protection)" access level for a standard CPU (in other words, not an F-CPU) and enter a separate password for each of the access levels that lie above it in the table.

For users who do not know any of the passwords, the CPU is completely protected. Not even HMI access is possible.

For users who know one of the set passwords, the effect depends on the table row in which the password occurs:

- The password in row 1 (Full access (no protection)) allows access as if the CPU were completely unprotected. Users who know this password have unrestricted access to the CPU.
- The password in row 2 (read access) allows access as if the CPU were write-protected. Despite knowing the password, users who know this password only have read access to the CPU.
- The password in row 3 (HMI access) allows access as if the CPU were read/write protected. For users who know this password, only HMI access is possible.

###### Procedure

To configure the access levels of a CPU, follow these steps:

1. Open the properties of the module in the inspector window.
2. Open the "Protection & Security > Access control" entry in the area navigation.

   A table with the possible access levels appears in the inspector window.

   ![Procedure](images/142980549771_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/142980549771_DV_resource.Stream@PNG-en-US.png)
3. Select the required access level in the first column of the table. The green checkmarks in the columns to the right of the respective protection level show you which operations are still available without entering the password.
4. If you have selected an access level other than "Full access":

   Specify a password for full access in the first row of the "Password" column.

   In the "Confirmation" column, enter the selected password again to protect against incorrect entries.

   Ensure that the password is sufficiently secure, in other words, that is does not follow a machine-recognizable pattern!

   You must enter a password in the first row "Full access (no protection)". This enables unrestricted access to the CPU for those who know the password, regardless of the selected protection level.
5. Assign additional passwords as needed to other access levels if the selected access level allows you to do so.
6. Download the hardware configuration so that the access level takes effect.

###### Result

The hardware configuration and the blocks are protected against unauthorized online access according to the set access level. If an operation cannot be executed without a password due to the set access level, a dialog for entering a password is displayed.

---

**See also**

[What you should know about the access levels (S7-1500)](#what-you-should-know-about-the-access-levels-s7-1500)
  
[Using the Security settings wizard (S7-1500)](#using-the-security-settings-wizard-s7-1500)

#### Password transfer upon module replacement (S7-1500)

If you assign a protection level that requires the input of a password, the CPU converts this input using a special algorithm and, put in simplified terms, saves a special checksum for that password.

STEP 7 never saves the password itself, nor is a password saved in the CPU in a form from which it could be reconstructed. If the password is lost, a new CPU configuration must therefore always be loaded; see the section below.

The algorithm for forming or encrypting the checksum from the password is constantly being developed to offer maximum protection from unauthorized access. This has no impact on the procedure for configuration, with the exception of module replacement. Depending on the firmware version of the CPUs affected (the CPU to be replaced and the replacement CPU), you are either offered an update to the latest algorithm or prompted to assign a new password because the replacement CPU cannot use the existing password configuration.

If the CPU to be replaced and the replacement CPU are identical in terms of the algorithm used, no action is required: the password configuration and the other parameter settings are transferred.

The same applies to the configured users of the CPU Web server: If you create users with specific rights, you must configure a password for each user. In this case too, you are informed if the algorithms are not compatible in the event of module replacement, and may then need to create new users and passwords.

##### Forgotten your password - loading new CPU configuration

If you forget the password protecting the CPU, you cannot go online with the CPU to load a new configuration (with a new password).

Proceed as follows to load a new configuration (with new password) in this case:

1. Plug the SIMATIC memory card into the card reader of your programming device.
2. In the project tree, drag and drop the CPU folder with the new configuration to the symbol for the SIMATIC memory card in the card reader.
3. In the load dialog, confirm that the configuration and program of the existing password-protected CPU configuration are to be overwritten.

##### Behavior of a password-protected CPU during module replacement

- You are replacing an S7-1500 CPU (**firmware < 2.0**) with an S7-1500 (**firmware ≥ 2.0**):

  You are informed that a more up-to-date algorithm is available for password encryption. You have the option of using the new algorithm by clicking on the button or - on the grounds of compatibility - retaining the previous algorithm.
- You are replacing an S7-1500 CPU (**firmware ≥ 2.0**) with an S7-1500 (**firmware < 2.0**):

  You are informed that the previous passwords will be lost and that new passwords must be configured.

##### Behavior of a CPU with configured Web server users during module replacement

To create users and their specific rights, you must configure a password for each user. Similar rules apply for module replacement as for a password-protected CPU:

- You are replacing an S7-1500 CPU (**firmware < V2.0**) with an S7-1500 (**firmware ≥ V2.0**):

  You are informed that a more up-to-date algorithm is available for password encryption. You have the option of using the new algorithm by clicking on the button or - on the grounds of compatibility - retaining the previous algorithm.
- You are replacing an S7-1500 CPU (**V1.7 ≤ firmware ≤ V1.8**) with an S7-1500 (**firmware ≤ 1.6**) or
- You are replacing an S7-1500 CPU (**firmware ≥ 2.0**) with an S7-1500 (**firmware < 2.0**):

  You are informed that all configured users are deleted and that the user "Everyone" is reset to default user rights.

  In this case, you must create the users again with rights and passwords.

#### Restriction of communication services (S7-1500)

##### Introduction

The CPU can be the server for a number of communication services. This means that other communication participants can access CPU data even if you have not configured and programmed connections for the CPU.

The local CPU as a server thus does not have the possibility to control communication to the clients.

The parameter "Connection mechanisms" in the "Protection" area of the CPU parameters is used to specify whether this type of communication is permitted or not for the local CPU during operation.

##### Permit access with PUT/GET communication from remote partners

By default, the "Permit access with PUT/GET communication from remote partners (...)" option is disabled. In this case, read and write access to CPU data is only possible for communication connections that require configuration or programming both for the local CPU and for the communication partner. Access through BSEND/BRCV instructions is possible, for example.

Connections for which the local CPU is only a server (meaning that no configuration/programming of the communication with the communication partner exists at the local CPU), are therefore not possible during operation of the CPU, for example,

- For PUT/GET, FETCH/WRITE or FTP access via communication modules
- For PUT/GET access from other S7 CPUs
- For HMI access that is realized via PUT/GET communication

If you want to allow access to CPU data from the client side, meaning that you do not want to restrict the communication services of the CPU, activate the "Permit access with PUT/GET communication from remote partners" option.

#### Connection mechanisms (S7-1500)

The settings for the connection mechanisms determine with which partners the CPU may connect. The default setting is that the CPU may only connect via Secure PG/HMI communication, which requires that the partner also supports Secure PG/HMI communication.

You can also select a certificate for secure PG/HMI communication or have the TIA Portal create a new certificate.

---

**See also**

[Additional settings for the secure PG/HMI communication (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#additional-settings-for-the-secure-pghmi-communication-s7-1200-s7-1500-s7-1500t)
  
[Using the Security settings wizard (S7-1500)](#using-the-security-settings-wizard-s7-1500)

#### Group alarms for security events (S7-1500)

This section contains information on the following topics:

- [What you should know about group alarms for security events (S7-1500)](#what-you-should-know-about-group-alarms-for-security-events-s7-1500)
- [Configuring a group alarm for security events (S7-1500)](#configuring-a-group-alarm-for-security-events-s7-1500)

##### What you should know about group alarms for security events (S7-1500)

###### Security events in the diagnostics buffer

The CPU stores information on important actions and events in the diagnostics buffer.

The following security events (event types) lead to an entry in the diagnostics buffer of the S7-1500:

- Going online with the correct or incorrect password.
- Manipulated communications data detected.
- Manipulated data detected on memory card.
- Manipulated firmware update file detected.
- Changed protection level (access protection) downloaded to the CPU.
- Password legitimization restricted or enabled (via an instruction or, if application, via the CPU display).
- Online access denied due to the possible number of simultaneous access attempts being exceeded.
- Timeout when an existing online connection is inactive.
- Logging in to the Web server with the correct or incorrect password.
- Creating a backup of the CPU.
- Restoring the CPU configuration.
- During startup:

  - Project on the SIMATIC memory card has changed (the SIMATIC memory card remains the same)
  - SIMATIC memory card was replaced

###### Group alarm for security events

To prevent the diagnostics buffer being "swamped" by large numbers of identical security events, as of STEP 7 V13 service pack 1, you can set parameters so that these events are entered in the diagnostics buffer as a group alarm. Per interval (monitoring time), the CPU then only generates one group alarm per event type.

**Example:**
 **Brute-Force**
 **attacks**

With Brute-Force attacks, attackers attempt to gain access to the CPU by systematically trying out a large number of the possible password combinations. As a result, the CPU receives a large number of login requests within seconds and the inrush of identical single entries in the diagnostics buffer leads to the loss of important diagnostics information. Group alarms help here.

**Principle of operation of group alarms**

The CPU enters the first three events of an event type in the diagnostics buffer. It then ignores all subsequent security events of this type.

At the end of the monitoring time (interval), the CPU generates a group alarm in which it enters the event type and the frequency of the event during the elapsed interval.

If these security events also occur in the intervals that follow, the CPU only generates one group alarm per interval.

An attack leaves the following pattern in the diagnostics buffer: Three individual alarms followed by a series of group alarms. This series can consist of two, three or more group alarms depending on the selected monitoring time and duration of the attack.

Since the alarms in the diagnostics buffer have a time stamp, the duration of the attack can be determined.

![Group alarm for security events](images/71228094091_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Security events of one type, for example login attempts with an invalid password. |
| ② | Interval (monitoring time): When a security event of a particular type occurs the first time (or reoccurs), the monitoring time is started (or restarted). |
| ③ | Single alarms: The first three security events of a type are entered in the diagnostics buffer immediately. As of the fourth security event of this type, the CPU only creates group alarms.  If a security event of this type occurs after a pause of at least one interval, the CPU enters a single alarm in the diagnostics buffer and restarts the monitoring time. |
| ④ | Group alarms: After three security events, the CPU only generates a group alarm as a summary of all other security events in this interval. If these security events also occur in the intervals that follow, the CPU only generates one group alarm per interval. |

---

**See also**

[Configuring a group alarm for security events (S7-1500)](#configuring-a-group-alarm-for-security-events-s7-1500)
  
[What you need to know about SIMATIC memory cards (S7-1500)](#what-you-need-to-know-about-simatic-memory-cards-s7-1500)

##### Configuring a group alarm for security events (S7-1500)

###### Requirements

- STEP 7 V13 Service Pack 1 or higher
- S7-1500 CPU with firmware version 1.7 or higher

###### Procedure

To configure group alarms for security events, follow these steps:

1. Click on the CPU symbol in the network view.

   The properties of the CPU are displayed in the Inspector window.
2. Go to the "Protection" > "Security event" area.
3. Click on "Security event".
4. Select the option "Summarize security events in case of high message volume" to enable group alarms for security events.
5. Set the duration of an interval (monitoring time); the default is 20 seconds.

---

**See also**

[What you should know about group alarms for security events (S7-1500)](#what-you-should-know-about-group-alarms-for-security-events-s7-1500)

#### Disabling online access to the CPU via the display (S7-1500)

You can block access to a password-protected CPU on the display of an S7-1500 CPU (local block).

The access block only functions if the operating mode switch is set to RUN.

The access block is effective irrespective of the password protection. This means that even if someone accesses the CPU via a connected programming device and has entered the correct password, access to the CPU remains disabled.

The access block can be set separately for each protection level on the display, so that, for example, read access is allowed locally, but write access is not allowed locally.

In addition, a password can be configured for the display in the properties of the CPU so that the local access protection is protected by a local password.

##### Procedure

Proceed as follows to set the local access protection for an S7-1500 CPU on the display:

1. Select the menu Settings > Protection on the display.
2. Confirm with "OK" and set for each protection level whether access in RUN mode is permitted:

   Allow: Access to the CPU is possible with password input.

   Block in RUN: If the operating mode switch is set to RUN, no user can log on to the CPU with the rights of this protection level, even when the relevant password is known. In STOP mode, access is possible with password input.

---

**See also**

[What you should know about the access levels (S7-1500)](#what-you-should-know-about-the-access-levels-s7-1500)

#### Certificate manager (S7-1500)

This section contains information on the following topics:

- [What you should know about the certificate manager (S7-1500)](#what-you-should-know-about-the-certificate-manager-s7-1500)
- [Local CPU-specific certificate manager (S7-1500)](#local-cpu-specific-certificate-manager-s7-1500)
- [Creating certificates (S7-1500)](#creating-certificates-s7-1500)
- [Assigning certificates (S7-1500)](#assigning-certificates-s7-1500)
- [Exporting certificates (S7-1500)](#exporting-certificates-s7-1500)
- [Deleting certificates (S7-1500)](#deleting-certificates-s7-1500)
- [Certificates for the Web server (S7-1500)](#certificates-for-the-web-server-s7-1500)
- [Certificates for OPC UA server (S7-1500)](#certificates-for-opc-ua-server-s7-1500)

##### What you should know about the certificate manager (S7-1500)

###### Introduction

Digital certificates play an important role in the secure data transfer between two devices. When digital certificates are used, the client must also check and trust the certificate of the server. Depending on the type of secure communication used, this also applies in the opposite direction: A client can only establish a secure connection to a server when the server accepts the digital certificate of the client, classifies it as trustworthy and trusts it.

CPUs of the S7-1500 as of firmware V2.0 support the use of certificates.

###### Device-specific and project-wide certificate manager

With the local CPU-specific certificate manager, certificates can be generated and managed for the respective device. These can then be used by the following objects:

- OPC UA server of the device
- Web server of the device
- Any additional system feature that requires certificates and is referenced by a certificate ID. In TIA Portal V14, Secure OUC and TMAIL are also the secure PG/HMI communication, as of TIA Portal V17).

  > **Note**
  >
  > Each certificate in the certificate manager receives an ID for unique referencing in specific SDTs. The certificate ID is assigned by the certificate manager when a certificate is created or imported. The certificate ID is unique within the project and cannot be changed.

Certificates of the local CPU-specific certificate manager refer solely to the device. If you want to use certificates project-wide, you have to activate the global security certificate manager in the device.

In the global security certificate manager you can utilize additional functions for the management of your certificates:

- Import of new certificates and certificate authorities.
- Export of the certificates and certificate authorities used in the project.
- Renewal of expired certificates and certificate authorities.
- Replacement of existing certificate authorities.
- Adding trusted certificates and certification authorities.
- Deleting manually imported certificates.

The global security settings are not visible until they have been activated in the project for at last one device. The "Use global security settings for certificate manager" check box is available to this purpose in the local CPU-specific certificate manager: It is located in the Inspector window in the general settings of a device with security functions under "Protection & Security > Certificate manager". Depending on this setting either only the local CPU-specific certificate manager with limited functionality is used or the global security certificate manager.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Loss of certificates and keys**  When you activate the global security certificate manager for the project, the contents of the local CPU-specific certificate manager are lost:  - The private keys cannot be restored. - Export your certificates if you want to keep using them in the global security certificate manager. - Update your configuration or your program, because the ID of the certificate can change. |  |

After activation of the global security certificate manager the local CPU-specific certificate manager acts like a temporary memory of the CPU-specific global certificates. When you create a new certificate in the local CPU-specific certificate manager, it is entered in the global security certificate manager. You can also select certificates in the global security certificate manager in the local CPU-specific certificate manager as a certificate for the CPU.

---

**See also**

[Certificates for the Web server (S7-1500)](#certificates-for-the-web-server-s7-1500)
  
[Certificates for OPC UA server (S7-1500)](#certificates-for-opc-ua-server-s7-1500)
  
[Local CPU-specific certificate manager (S7-1500)](#local-cpu-specific-certificate-manager-s7-1500)
  
[Useful information on Secure Communication (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#useful-information-on-secure-communication-s7-1200-s7-1500-s7-1500t)

##### Local CPU-specific certificate manager (S7-1500)

###### Introduction

With the local CPU-specific certificate manager, you can use certificates for different services, for example, for the OPC UA server and the Web server, without access to the global security certificate manager.

###### Functions of the local certificate manager

In comparison to the global certificate manager, the local CPU-specific certificate manager only has a limited functionality. Via the local certificate manager, you can only create, assign, export or delete self-signed certificates.

The settings for the local CPU-specific certificate manager are located in the Inspector window in the general settings of the device under "Protection & Security > Certificate manager".

- Option for activating the global certificate manager
- Table for device certificates: Display and management of the certificates that you use, for example, for secure OUC (TLS server / TLS client), the Web server and the OPC UA server of the device.
- Table for certificates of the partner devices: Display of the certificates that you have assigned as trusted users or clients.

###### Device certificates

Device certificates are valid for the device and its associated components. The certificates displayed here were, for example, also created for the Web server or for OPC UA and are displayed here. Similarly, certificates with the settings for the Web server or for OPC UA can be created here - but have to be used at the corresponding location.

When you create a new certificate, the following values are entered as the default in the corresponding dialog for the device:

- Purpose and key usage: For example, TLS client/ server The extensions "KeyUsage" and "ExtendedKeyUsage" for certificates of the X.509 V3 standard are suitably filled for the respective service.
- Certificate authority: Only self-signed certificates are possible for the local CPU-specific certificate management.
- Certificate parameters:

  - Certificate holder: For example, <Name of the CPU>/TLS. The set of characters is limited so that the specifications to ASN.1 can be observed.
  - Encryption process: For example, EC (Elliptic Curves), RSA. Note that the selected encryption process EC is not validated for the specific device at the time of input.
  - Encryption parameters: Depending on the encryption process.
  - Hash algorithm: Algorithm that is used for signing the certificate.
  - Validity period: The start and end of the validity period is entered in the two fields for the validity period in dependence on the system time.
  - Alternative name of the certificate holder (SAN): IP address or DNS names of the interfaces used.

You can overwrite the defaults with your own values.

###### Certificates of the partner devices

For the certificates of the partner devices you can select device certificates of the local certificate manager. Device certificates are used without their private key. You can also select the certificates of other CPUs or CPs for secure communication within the project. The certificates of other CPUs or CPs are loaded to the CPU without private keys. In as far as the chain of certificates via the global certificate manager is available, the chain of certificates belonging to a CPU or CP is still not interrupted and the corresponding certificate authority and intermediate certificates remain assigned to the CPU or the CP.

When you delete a certificate in the table of certificates of the partner devices, only the link of the certificate to the global certificate manager is deleted. The certificate is therefore no longer available to the device, but remains in the global certificate manager. If required, the certificate can therefore be used again in the device if it is selected as a new certificate from the global certificate manager. If the certificate is to be deleted for the entire project, you have to do so in the shortcut menu of the global certificate manager.

---

**See also**

[What you should know about the certificate manager (S7-1500)](#what-you-should-know-about-the-certificate-manager-s7-1500)
  
[Creating certificates (S7-1500)](#creating-certificates-s7-1500)
  
[Assigning certificates (S7-1500)](#assigning-certificates-s7-1500)
  
[Exporting certificates (S7-1500)](#exporting-certificates-s7-1500)
  
[Deleting certificates (S7-1500)](#deleting-certificates-s7-1500)
  
[Global security certificate manager (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#global-security-certificate-manager-s7-1200-s7-1500-s7-1500t)
  
[Device-dependent security features (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#device-dependent-security-features-s7-1200-s7-1500-s7-1500t)

##### Creating certificates (S7-1500)

###### Introduction

You can create a new certificate for a device. When you create a new certificate with deactivated global security certificate manager, the certificate only applies for this device. With exclusive use of the local CPU-specific certificate manager, only self-signed certificates can be created.

Furthermore, you can create new certificates directly with the CPU settings for the Web server or for OPC UA.

As of CPU firmware version V2.9 (S7-1500) or V4.5 (S7-1200), a PLC communication certificate is pre-selected and generated automatically.

###### Requirement

The device must offer security functions with certificate manager. This applies for S7-1500 CPUs as of firmware V2.0.

As of CPU firmware version V2.9 (S7-1500) or V4.5 (S7-1200) the settings for the password to protect confidential configuration data must be consistent.

###### Procedure

To create a new certificate, proceed as follows, for example:

1. In the Inspector window, go to "Protection & Security > Certificate manager" in the properties of the device.
2. Click "Add" in the table of certificates. A new row is entered in the table.
3. Click in the new row. The selection for new certificates is opened.
4. Click the "Add" button. The corresponding dialog window opens in which you can enter the data for the new certificate.
5. Select how the new certificate is to be signed:

   - Self-signed: If the certificate has to be a self-signed certificate.
   - Signed by a certificate authority (CA): Select a certificate authority from the drop-down list. Only possible with activated global security settings for the certificate manager.
6. Enter the parameters for the certificate.
7. When you click "OK", the new certificate is created and entered in the table.

> **Note**
>
> **Self-signed certificates**
>
> With a self-signed certificate you have already created an encryption for the transport path, but the recipient of a message does not yet have a confirmation whether the named sender is the real sender. A message that was signed by a certificate authority identifies the sender as "real" towards the recipient. However, you can create a self-signed certificate for the device when you still have to wait for a certificate signed by a certificate authority. Through the global security certificate manager in the project tree you can then either replace the temporarily used self-signed certificate or renew it by specifying the certificate authority after you have received the "official" certificate from the certificate authority (CA). You can naturally also retain a self-signed certificate in the project and forgo the usage of an "official" CA certificate.

###### Result

A new certificate is created for the device. "TLS" is entered automatically as the usage purpose in the procedure described above. Otherwise, the service from the context in which the certificate creation was started is entered, for example, "Web server", if you use the "Security" area in the CPU settings for the Web server.

###### Certificate ID

Each certificate in the certificate manager receives an ID. This ID is used for identification of the certificates in the following cases:

- OPC UA server certificate
- List of trusted OPC UA clients
- List of trusted OPC UA users
- Web server certificate
- Secure OUC instructions
- PLC communication certificate for Secure PG/HMI communication

The certificate ID is assigned by the certificate manager if a certificate is created or imported in the TIA Portal. The certificate IDs are required to uniquely assign the certificates to specific system data types, for example, to the SDT TCON_IP_v4_Sec. The certificate ID is unique within the project and cannot be changed.

---

**See also**

[Local CPU-specific certificate manager (S7-1500)](#local-cpu-specific-certificate-manager-s7-1500)
  
[Device-dependent security features (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#device-dependent-security-features-s7-1200-s7-1500-s7-1500t)

##### Assigning certificates (S7-1500)

###### Introduction

You can assign available certificates to the CPUs and CPs in the Inspector window.

###### Requirement

The device must offer security functions with certificate manager. This applies for S7-1500 CPUs as of firmware V2.0.

###### Procedure

To assign an available certificate to a device, follow these steps:

1. In the Inspector window, go to "Protection & Security > Certificate manager" in the properties of the device.
2. Click "Add" in the table of certificates. A new row is entered in the table.
3. Click in the new row. The selection for new certificates is opened.
4. Select an available certificate. If only the local CPU-specific certificate manager is active, you do not see the globally available certificates. You can only see and select globally available certificates when the global security certificate manager is activated.
5. Click the green check mark to enter the selection in the table of certificates.

###### Result

The selected certificate was assigned to the device.

---

**See also**

[Local CPU-specific certificate manager (S7-1500)](#local-cpu-specific-certificate-manager-s7-1500)

##### Exporting certificates (S7-1500)

###### Introduction

You can export available certificates via the certificate manager.

###### Requirement

The device must offer security functions with certificate manager. This applies for S7-1500 CPUs as of firmware V2.0.

###### Procedure

To export a certificate, follow these steps:

1. In the Inspector window, go to "Protection & Security > Certificate manager" in the properties of the device.
2. Right-click in the row with the certificate to be exported to open the shortcut menu.
3. Click "Export certificate".
4. Export the certificate into one of the selectable file formats: CER, DER.

Private keys cannot be exported since they are encrypted asymmetrically and cannot be restored.

###### Result

The selected certificate has been exported and can now be backed up or be used in other projects.

---

**See also**

[Local CPU-specific certificate manager (S7-1500)](#local-cpu-specific-certificate-manager-s7-1500)

##### Deleting certificates (S7-1500)

###### Introduction

You can delete available certificates via the certificate manager.

###### Requirement

The device must offer security functions with certificate manager. This applies for S7-1500 CPUs as of firmware V2.0.

###### Procedure

To delete a certificate, follow these steps:

1. In the Inspector window, go to "Protection & Security > Certificate manager" in the properties of the device.
2. Right-click in the row with the certificate to be deleted to open the shortcut menu.
3. Click "Delete certificate".

###### Result

The selected certificate was deleted in the device. With an activated global security certificate manager the certificate is retained for the project, but is no longer used for the device.

---

**See also**

[Local CPU-specific certificate manager (S7-1500)](#local-cpu-specific-certificate-manager-s7-1500)

##### Certificates for the Web server (S7-1500)

###### Introduction

You can create or assign a server certificate for the Web server in the inspection window under "Web server > Security".

###### Local Web server certificate

The following restrictions apply when you create Web server certificates locally without using the global security settings for the certificate manager:

- The certificate only applies to the configured CPU and is not available throughout the project.
- Only self-signed certificates are created. Self-signed certificates are not embedded in a "Public Key Infrastructure" (PKI) and cannot sign other certificates.
- Private keys of the certificate cannot be exported.

Import and renewal of certificates is only possible in the global security settings for the certificate manager.

###### Default settings for Web server certificates

When you create a new certificate, the following values are entered as the default in the corresponding dialog for a Web server:

- Purpose of usage: Web server. The entries under "Key usage" (Extensions "KeyUsage" and "ExtendedKeyUsage" for certificates of the X.509 V3) standard are filled suitably for the Web server.
- Certificate holder: <Name of the CPU>/Web server. The set of characters is limited so that the specifications to ASN.1 can be observed.
- Encryption process: EC.
- Encryption parameters: prime256v1.
- Validity period: The start and end of the validity period is entered in the two fields for the validity period in dependence on the system time.
- Alternative name of the certificate holder (SAN): IP address of the used interfaces of the CPU and CP.

You can overwrite the defaults with your own values.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **SAN with reserved IP address**  When the alternative name of the certificate holder contains one or more reserved IP addresses, the certificate does not fulfill the guideline "Baseline Requirements Certificate Policy for the Issuance and Management of Publicly-Trusted Certificates". This can result in incompatibility with your own Web browsers.  To meet the guideline you should replace the IP addresses of the alternative name of the certificate holder with domain names. This requires a DNS server in the network that dissolves the IP addresses of the devices. |  |

---

**See also**

[What you should know about the certificate manager (S7-1500)](#what-you-should-know-about-the-certificate-manager-s7-1500)
  
[Information about the web server (S7-300, S7-400, S7-1500)](Configuring%20the%20Web%20server%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#information-about-the-web-server-s7-300-s7-400-s7-1500)
  
[Access only through HTTPS (S7-300, S7-400, S7-1500)](Configuring%20the%20Web%20server%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#access-only-through-https-s7-300-s7-400-s7-1500)
  
[How communication with certificates works: HTTP over TLS (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#how-communication-with-certificates-works-http-over-tls-s7-1200-s7-1500-s7-1500t)

##### Certificates for OPC UA server (S7-1500)

###### Introduction

You can create or assign a server certificate for OPC UA in the Inspector window under "OPC UA > Server > Security".

###### Local server certificates for OPC UA

The following restrictions apply when you create server certificates locally for OPC UA without using the global security settings for the certificate manager:

- The certificate only applies to the configured CPU and is not available throughout the project.
- Only self-signed certificates are created. Self-signed certificates are not embedded in a "Public Key Infrastructure" (PKI) and cannot sign other certificates.
- Private keys of the certificate cannot be exported.

Import and renewal of certificates is only possible in the global security settings for the certificate manager.

###### Default settings for server certificates

When you create a new certificate, the following values are entered as the default in the corresponding dialog for a OPC UA:

- Purpose of usage: OPC UA server. The entries under "Key usage" ("KeyUsage" and "ExtendedKeyUsage" extensions for certificates of the X.509 V3) standard are filled suitably for the OPC UA server.
- Certificate holder: <Name of the CPU>/OPCUA. The set of characters is limited so that the specifications to ASN.1 can be observed.
- Encryption process: RSA.
- Encryption parameters: 2048.
- Validity period: The start and end of the validity period is entered in the two fields for the validity period in dependence on the system time.
- Alternative name of the certificate holder (SAN): IP address of the used interfaces and the URI of the OPC UA server.

You can overwrite the defaults with your own values.

---

**See also**

[What you should know about the certificate manager (S7-1500)](#what-you-should-know-about-the-certificate-manager-s7-1500)

#### Syslog (S7-1500)

This section contains information on the following topics:

- [Introduction (S7-1500)](#introduction-s7-1500)
- [Transfer the syslog messages to a syslog server (S7-1500)](#transfer-the-syslog-messages-to-a-syslog-server-s7-1500)

##### Introduction (S7-1500)

###### Using syslog messages

International standards and national regulations for the IT security of automation components require, for example, the ability to log safety-related events.  
Syslog (System Logging) is an IETF standard protocol (RFC 5424) for the transfer of recorded events and meets this requirement. A CPU records the following events, for example:

- Security events
- Firmware updates
- Changes to the user program
- Changes to the configuration
- Changes to the operating state

Each CPU as of FW version V3.1 saves syslog messages in a local cache. By querying this cache, you can view the syslog messages and identify potential security risks. If you want to access the local cache with the syslog messages, use the Web API of the web server (API method Syslog.Browse). You can find information on the procedure in the "[Web server](https://support.industry.siemens.com/cs/us/en/view/59193560)" Function Manual.

The recording of safety-related events cannot be deactivated. You have the option of transferring the events recorded by the CPU to a syslog server in the network.

###### Forwarding to a syslog server

From STEP 7 V19 and a CPU as of FW version V3.1, it is possible to transfer syslog messages to a server, e.g. SINEC INS. The syslog messages are transferred to the syslog server via the syslog protocol. The syslog server saves all syslog messages from its connected devices. Messages of system and network events are stored centrally in a storage location in the syslog server. At the syslog server interface, you can view the collected syslog messages and thereby determine the source of potential security risks or problems.

###### Processing in a Security Information and Event Management system (SIEM system)

In order to be able to accept the incoming syslog messages, a SIEM‑system must understand the syslog protocol according to RFC 5424. Otherwise, the SIEM system cannot accept or process the incoming messages.

The SIEM system breaks down the incoming syslog messages into individual elements. These elements are assigned to their own event within the SIEM system. Within this event, it is analyzed whether there are connections between the individual syslog messages. In this way, the SIEM system detects possible attack vectors and, if necessary, informs the user, e.g. in the event of multiple attacks at several points in the system.

![Processing in a Security Information and Event Management system (SIEM system)](images/171508715275_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | CPUs |
| ② | Syslog messages |
| ③ | Syslog server, e.g. SINEC INS |
| ④ | SIEM system |
| ⑤ | Notify user |

###### More information

More information on network management with SINEC INS is available in the ["SIMATIC NET: Network management SINEC INS V1.0 SP2"](https://support.industry.siemens.com/cs/us/en/view/109781023) manual.

You can find information on the structure of syslog messages in the S7-1500 System Manual.

The content of the messages is based on IEC 62443-3-3. An overview of the syslog messages can be found in the following [entry](https://support.industry.siemens.com/cs/ww/en/view/109823696).

##### Transfer the syslog messages to a syslog server (S7-1500)

###### Requirements

If you want to transfer the syslog messages of a CPU to a syslog server, the following requirements must be met:

- STEP 7 as of version V19
- CPU as of FW version V3.1
- A project has been created in STEP 7
- The device or network view of STEP 7 is open

###### Procedure

To configure the CPU to transfer syslog messages to a syslog server, following these steps:

1. Select the required CPU in the device or network view of STEP 7.
2. In the Inspector window, navigate to "Properties > Protection & Security > System Logging".
3. In the "Connection to syslog server" area, activate the option "Enable transfer of syslog messages to syslog servers". The selection options below become editable.
4. Select one of the following options from the "Transport protocol" drop-down list:

   - "Transport Layer Security (TLS - server and client authentication)": Encrypted data transfer, syslog server and client (CPU) must authenticate themselves.
   - "Transport Layer Security (TLS - server authentication only)": Encrypted data transfer, only the syslog server needs to authenticate itself.
   - "UDP": Unencrypted data transfer, syslog server and client (CPU) do not need to authenticate themselves.

   In the next sections you can read how to select the certificates for authentication (logon) depending on the settings specified.
5. In the "Addresses of the syslog servers" column, enter a valid server address.
6. In the "Port" column, enter one of the following port numbers depending on the transport protocol used:

   - Standard TCP port for TLS: 6514
   - Standard UDP port: 514

Result: You have configured the transfer of syslog messages to a syslog server.

###### Selecting the client certificate

STEP 7 provides the required client certificate for a CPU for the TLS transport protocol. If the certificate is managed within the CPU, you can either choose an existing certificate or create a new certificate. To do so, follow these steps:

1. Select the required CPU in the device or network view of STEP 7.
2. In the Inspector window, navigate to "Properties > Protection & Security > System Logging".  
   The certificate generated by STEP 7 is displayed next to "Client certificate".

###### Selecting the server authentication

After selecting the TLS transport protocol, the configured syslog server must authenticate itself. This ensures that the CPU only connects to a trusted server. If you want to waive server authentication, activate the automatic acceptance of server certificates during runtime. To configure these settings, follow these steps:

1. Select the required CPU in the device or network view of STEP 7.
2. In the Inspector window, navigate to "Properties > Protection & Security > System Logging".
3. In the "Trusted servers" area, specify whether the connected syslog server should be authenticated. In this case, it is necessary to complete the following information:

   - Add trusted server: Add a valid server certificate in the "Common name of subject" column.
   - Automatically accept certificates during runtime: Activate the "Automatically accept server certificates during runtime" option. Editing in the table is then not possible.

     > **Note**
     >
     > **No authentication with automatically accepted server certificates**
     >
     > If you enable the "Automatically accept server certificates during runtime" option, a server does not need to authenticate itself. This means that the CPU can also connect to unknown servers that could represent a security risk.
     >
     > Only select this option during commissioning or in a protected environment.

   Result: You have configured the server authentication.

### Test, commissioning and routing (S7-1500)

#### Test, commissioning, routing

Select the check box if, for example, you want to use PG functions needed for commissioning and testing regularly over this interface.

If you select the "Test, commissioning, routing" option, the interface becomes the active device on PROFIBUS (in other words, the interface is included in the token rotation of PROFIBUS). The following functions are then possible:

- Programming (for example loading)
- Testing (status/modify)
- S7 routing (I-slave as gateway)

This can extend the token rotation time. In time-critical applications and when S7 routing and client functionality are not required for communication, this option should therefore not be enabled.

If the "Test, commissioning, routing" check box is not selected, the interface functions only as a server for communication services.

Server functionality means that only the partner (for example PG, OP or automation system) can initiate communication. Note the following features when the "Test, commissioning, routing" option is not enabled:

- S7 routing is not possible
- Programming and testing are possible but slow (no extension of the bus token rotation time)

### Activating and deactivating SNMP (S7-1500)

The network management protocol SNMP (Simple Network Management Protocol) is a protocol that is used by various services and tools for performing monitoring and diagnostics of the network topology. SNMP uses the transport protocol UDP. The SNMP has two roles: the SNMP manager (client) and SNMP agent (server).

- The SNMP manager monitors the network nodes:
- The SNMP agents collect the various network-specific information in the individual network nodes and store it in a structured form in the MIB (Management Information Base). Various services and tools (as SNMP manager) can run detailed network diagnostics with the help of these data.

SNMP is also used in a PROFINET IO system for managing the network infrastructure and the IO controller and IO devices.

> **Note**
>
> If SNMP is deactivated for a device, various options for diagnostics of the network topology (for example, using the PRONETAtool) are no longer available to you.
>
> Example: For the topology comparison Online-Offline, the TIA Portal determines which ports are actually connected and uses SNMP for this function.

#### Default settings depending on the firmware version

S7-1200 and S7-1500 CPUs have an integrated SNMP agent. Depending on the firmware version, different defaults apply to SNMP (SNMP activated or deactivated).

With CPUs of the following firmware versions, the SNMP agent is **activated** by default and may be deactivated by data record in the user program:

- CPU S7-1200 V4.1 to V4.5
- CPU S7-1500 V1.8 to V2.9

Under certain conditions, it may be useful to deactivate SNMP. Examples:

- The security guidelines in your network do not allow the use of SNMP.
- You use your own SNMP solution, e.g. with your own communications instructions.

#### Current default settings

With CPUs of the following firmware versions, the SNMP agent is **deactivated** by default and may be activated by data record in the user program:

- CPU S7-1200 V4.6 and higher
- CPU S7-1500 V3.0 and higher

The default setting "disabled" is also in effect if no configuration has been loaded or if no memory card is plugged in (S7-1500).

> **Note**
>
> **Replacement part scenario**
>
> For compatibility reasons, an S7-1500 CPU as of firmware version V3.0 with a loaded predecessor project (CPU firmware < V3.0) behaves like the CPU in the predecessor project:
>
> SNMP is activated and "public" and "private" community strings are in effect.

#### Configuring SNMP (S7-1200)

As of CPU firmware version 4.6 and TIA Portal version V18, you have the possibility to change the following settings for SNMP in the CPU properties:

- Activate SNMP (default: deactivated)

You can find the settings in the "Advanced configuration > SNMP" area of the CPU properties.

#### Configuring SNMP (S7-1500)

As of CPU firmware version V3.0 and TIA Portal version V18, you have the possibility to change the following settings for SNMP in the CPU properties:

- Activate SNMP (default: deactivated)
- Read-only community string (default: "public")
- Read-write community string (default: "private")

You can find the settings in the "Advanced configuration > SNMP" area.

#### Meaning and properties of community strings

An SNMP community string, also referred to as a "community name", is like a user ID or a password, which allows access to information/statistics of a device such as a router.  
In this respect, to increase the security, you should change the default community strings in the CPU properties. An SNMP manager authenticates itself with the SNMP agent by transferring the community strings when there is a request.

The community strings are transferred as plain text.

- The default community string for SNMP read-only operations (GET) is "public".
- The default community string for SNMP read-write operations (SET) is "private".

Number of characters for the community string: 1-240.

You can use the following characters for the community string:

- a-z
- A-Z
- 0-9
- -
- .

#### Activate/deactivate SNMP in the user program

To activate or deactivate SNMP in the user program, follow these steps:

| 1. In STEP 7, create a data block that contains the structure of the B071<sub>H</sub> data record. The following table shows the structure of the data record B071<sub>H</sub>.       | Byte | Element | Code | Explanation |    | --- | --- | --- | --- |    | 0-1 | BlockID | F003<sub>H</sub> | Header The data record length is counted starting at byte 4 "Version". |    | 2-3 | BlockLength | 8 |  |    | 4 | Version | 0x01 |  |    | 5 | Subversion | 0x00 |  |    | 6-7 | Reserved | - | - |    | 8-11 | SNMP controller | 0, 1 | 0: Deactivate SNMP. 1: Activate SNMP. | 2. Transfer the data record 0xB071 in the program cycle OB (OB1) to the CPU with the "WRREC" instruction (write data record). Use an integrated PROFINET interface of the CPU as the hardware identifier. |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

#### Interplay of SNMP configuration and user program

- The SNMP setting "activated/deactivated" via the user program is non-retentive, i.e. the configured setting is effective again after POWER OFF/ON transition, after a new hardware configuration has been loaded, or after restoring the factory settings.
- When loading the configuration from the CPU ("Upload device as new station"), the configured SNMP setting (activated/deactivated) is taken into consideration. An SNMP setting previously set by data record in the user program is ignored.
- The community strings can only be changed in the configuration; the community strings cannot be set through a data record in the user program.   
  However, you can activate the configured community strings by data record.  
  **Example**:  
  You have set SNMP to deactivated in the configuration of an S7-1500 CPU. You change the default community strings in the CPU properties and then load the configuration into the CPU.   
  Then, you activate SNMP via data record transfer.  
  Result: The changed community strings take effect.
- With S7-1200 CPUs and S7-1500 CPUs up to firmware version 2.9, the preset community strings ("public" and "private") are always in effect when SNMP is activated.

### Activating/deactivating SNMP through a program - standard CPU (S7-1500)

#### Introduction

Because you wish to manage your network infrastructure, IO controller and peripheral devices with SNMP, you want to activate the SNMP for a CPU 1516-3 PN/DP. The example below shows the 0xB071 data record being transferred to a PROFINET interface for this purpose.

#### Requirement

- CPU 1516‑3 PN/DP from FW version V3.0 onwards
- STEP 7 version V14 or higher

#### Solution

Transfer the 0xB071 data record to the PROFINET interface of the IO controller. This activates the SNMP at this PROFINET interface.

The following example shows how you can create the data record in a global data block and transfer it in a program cycle OB (for example, OB1) to the PROFINET interface (Local~PROFINET_interface_1).

To activate SNMP for the addressed PROFINET interface of the 1516‑3 PN/DP, follow these steps:

1. Create a global data block.
2. Assign a name, for example, "ActivateSnmp".
3. Under "Static", create the structure of the 0xB071 data record (in the figure: "snmpRecord") and other variables for transferring the data record. The following figure shows the data block structure "ActivateSnmp".

   ![Solution](images/159074268171_DV_resource.Stream@PNG-de-DE.png)

   ![Solution](images/159074268171_DV_resource.Stream@PNG-de-DE.png)
4. Transfer the 0xB071 data record in an OB program cycle (for example, OB1), with the "WRREC" (write data record) instruction to the CPU 1516-3 PN/DP. You can find an example program in the next section

#### Programming example for the data record transfer in the OB1

In the following program code, the data record 0xB071 is transferred with a REPEAT-UNTIL loop.

//-----------------------------------------  
// Start writing SNMP settings  
//-----------------------------------------  
IF "ActivateSnmp".snmpWrite THEN  
 IF (NOT "ActivateSnmp".snmpWriteDone)  
 AND (NOT "ActivateSnmp".snmpWriteError) THEN  
 "instWrrec_1"(REQ := "ActivateSnmp".snmpWrite,  
 ID := "Local~PROFINET-Schnittstelle_1",  
 INDEX := 16#B071,  
 DONE => "ActivateSnmp".snmpWriteDone,  
 ERROR => "ActivateSnmp".snmpWriteError,  
 STATUS => "ActivateSnmp".snmpWriteStatus,  
 RECORD := "ActivateSnmp".snmpRecord);  
 END_IF;  
 IF "ActivateSnmp".snmpWriteError THEN  
 ; // add error handling  
 END_IF;  
 IF "ActivateSnmp".snmpWriteDone THEN  
 "ActivateSnmp".snmpWrite := FALSE;  
 END_IF;  
END_IF;

#### Deactivating SNMP again

You can use the program code used above, with small changes, to deactivate SNMP. In the user program, assign the value "0" to the "ActivateSnmp".snmpRecord.snmpControl tag:

"ActivateSnmp".snmpRecord.snmpControl := 0;

The next time the "WRREC" instruction is called, SNMP will be deactivated again.

### Activating/deactivating SNMP through a program - R/H-CPU (S7-1500)

In S7-1500R/H systems, activate/deactivate the SNMP in the user program as with standard CPUs.

However, the PROFINET interfaces (X1, X2, etc.) of the two CPUs have different hardware IDs. The PROFINET interface X1 of the left-hand CPU, for example, has a different hardware ID than the PROFINET interface X1 of the right-hand CPU.

The S7-1500R/H system does not automatically synchronize the SNMP status (activated/deactivated) for both CPUs. An SNMP status (activated/deactivated) set by the "WRREC" instruction only affects the CPU whose PROFINET interface addresses the "WRREC" instruction.

**Example:**

The S7‑1500R/H system is in the "RUN redundant" system state.

If a PROFINET interface of the left-hand CPU is addressed with the "WRREC" instruction, for example, the SNMP status of the left-hand CPU is changed. The SNMP status of the right-hand CPU remains unchanged.

If the left-hand CPU fails or is replaced, the unchanged SNMP status is valid again after the SYNCUP.

**Solution**:

Call the "WRREC" instruction 2 times. In the first call of "WRREC", address the hardware ID of a PROFINET interface of the left-hand CPU. Call the "WRREC" instruction again. This time, address the hardware ID of a PROFINET interface of the right-hand CPU.

Hardware IDs for PROFINET interface X1:

- The PROFINET interface X1 of the left-hand CPU has the hardware ID 65**1**64 (default name: Local1~PROFINET-interface_1).
- The PROFINET interface X1 of the right-hand CPU has the hardware ID 65**3**64 (default name: Local2~PROFINET-interface_1).

The addressing by means of the respective hardware IDs of the PROFINET interfaces X1 is also used in the following example for calling the "WRREC" instruction for both R/H CPUs.

> **Note**
>
> **Transfer of the data record to the backup CPU**
>
> Transfer the data record to the addressed PROFINET interface of the backup CPU only after the S7-1500R/H system has reached the "Run REDUNDANT" system state. Otherwise, the data record cannot be transferred to the addressed PROFINET interface of the backup CPU.
>
> When the S7-1500R/H system has reached the system state "Run REDUNDANT", the CPU redundancy error OB (OB72) is started. The "Fault_ID" tag of the OB72 contains the error code "B#16#03" or "B#16#06".

#### Example: WRREC calls for both R/H CPUs

To activate/deactivate SNMP for the addressed PROFINET interface of both the CPUs by transferring data records, proceed as follows:

1. Create a global data block.
2. Assign a name, for example, "ActivateSnmp".
3. Under "Static", create the structure of the 0xB071 data record (in the figure: "snmpRecord") and other tags for transferring the data record. The following figure shows the structure of the data block "ActivateSnmp".

   ![Example: WRREC calls for both R/H CPUs](images/161295128843_DV_resource.Stream@PNG-de-DE.png)
4. Add the organization block "CPU redundancy error" (OB72) to your user program. You can find an example program for the OB72 in the next section.
5. Open the program cycle OB (OB1).
6. In the OB1, execute two "WRREC" instructions for transferring the data record to the respective addressed PROFINET interface of both the CPUs. You can find an example program for the OB1 in the next section.

   Result: The 0xB071 data record was transferred to the PROFINET interface of both the CPUs addressed in each case.

#### Programming examples for the OB72 and OB1 organization blocks

Open the OB72. that has been added. With the following program code, determine whether the R/H system has assumed the "Run-REDUNDANT" state and set the starting command for the "WRREC" instructions:

//--------------------------------------------  
// Check redundancy state and set "snmpWrite"  
//--------------------------------------------  
IF #Fault_ID = B#16#03 OR #Fault_ID = B#16#06 THEN  
 "ActivateSnmp".snmpWrite := TRUE;  
END_IF;

Open the program cycle OB (OB1). With the following program code, you can run 2 "WRREC" instructions for transferring the data record to the respective addressed PROFINET interface of both the CPUs:

//-----------------------------------------  
// Start writing SNMP settings  
//-----------------------------------------  
IF "ActivateSnmp".snmpWrite THEN  
 IF (NOT "ActivateSnmp".plcLeft.snmpWrDone)  
 AND (NOT "ActivateSnmp".plcLeft.snmpWrError) THEN  
 // write SNMP settings for the left PLC  
 "instWrrec_1"(REQ := "ActivateSnmp".snmpWrite,  
 ID := "Local1~PROFINET_interface_1",  
 INDEX := 16#B071,  
 DONE => "ActivateSnmp".plcLeft.snmpWrDone,  
 ERROR => "ActivateSnmp".plcLeft.snmpWrError,  
 STATUS => "ActivateSnmp".plcLeft.snmpWrStatus,  
 RECORD := "ActivateSnmp".snmpRecord);  
 END_IF;  
 IF "ActivateSnmp".plcLeft.snmpWrError THEN  
 ; // add error handling for left plc  
 END_IF;  
 IF (NOT "ActivateSnmp".plcRight.snmpWrDone)  
 AND (NOT "ActivateSnmp".plcRight.snmpWrError) THEN  
 // write SNMP settings for the right PLC  
 "instWrrec_2"(REQ := "ActivateSnmp".snmpWrite,  
 ID := "Local2~PROFINET_interface_1",  
 INDEX := 16#B071,  
 DONE => "ActivateSnmp".plcRight.snmpWrDone,  
 ERROR => "ActivateSnmp".plcRight.snmpWrError,  
 STATUS =>  
 "ActivateSnmp".plcRight.snmpWrStatus,  
 RECORD := "ActivateSnmp".snmpRecord);  
 END_IF;  
 IF "ActivateSnmp".plcRight.snmpWrError THEN  
 ; // add error handling for right plc  
 END_IF;  
 IF "ActivateSnmp".plcLeft.snmpWrDone  
 AND "ActivateSnmp".plcRight.snmpWrDone THEN  
 "ActivateSnmp".snmpWrite := FALSE;  
 END_IF;  
END_IF;

#### Deactivating SNMP again

You can use the program code used above, with small changes, to deactivate SNMP. In the user program, assign the value "0" to the "ActivateSnmp".snmpRecord.snmpControl tag:

"ActivateSnmp".snmpRecord.snmpControl := 0;

The next time the "WRREC" instructions are called, SNMP will be deactivated again.

### Isochronous mode (central) (S7-1500)

This section contains information on the following topics:

- [Configuring isochronous mode for central I/O in S7-1500 (S7-1500)](#configuring-isochronous-mode-for-central-io-in-s7-1500-s7-1500)
- [Time sequence of synchronization in the central configuration (S7-1500)](#time-sequence-of-synchronization-in-the-central-configuration-s7-1500)

#### Configuring isochronous mode for central I/O in S7-1500 (S7-1500)

When you configure the isochronous mode of a module centrally in an S7-1500 station, such as an analog input module, disable it in the same way as when configuring a module that is configured in distributed manner:

- In the properties of the I/O modules, you need to enable isochronous mode, assign the addresses of the module to a process image partition, and assign this process image partition to the isochronous mode interrupt OB.
- In the properties of the isochronous mode interrupt OB, you can adapt the application cycle and delay time (recommendation: keep automatic setting).
- In the properties of the CPU, also enable isochronous mode and adjust the settings for send clock and T<sub>i</sub>/T<sub>o</sub> values.  
  A new feature is that you can select a synchronization type: Here you can set whether the CPU should use a local send clock or whether the send clock should be synchronized to the send clock of the PROFINET interface X1 for the centrally configured modules. In the latter case the send clock of the PROFINET interface is leading.

##### Requirements

- S7-1500 CPU firmware V2.6 or higher (without compact CPUs and without S7-1500R/H CPUs)
- STEP 7 (TIA Portal) V15.1 or higher
- Centrally configured isochronous modules
- No PROFINET IO and PROFIBUS DP systems on centrally configured communications processors (CPs) or communication modules (CMs)
- No communications processors (CPs) or communication modules (CMs) as I-devices or I-slaves in the central configuration

##### Basic procedure

**Configuring I/O and isochronous mode interrupt OB**

To create an isochronous connection between the I/O and user program, follow these steps:

1. Select the S7-1500 CPU in the network view of STEP 7.
2. If you have performed a firmware update of the S7-1500 CPU from an earlier version, update the module description:

   - Open the "properties" of the module.
   - In the "General > Catalog information" tab, click the "Update module description" button.
3. Change to the device view.
4. Insert an I/O module that can be operated isochronously (e.g. AI 8 x U/I HS).
5. Go to the "I/O addresses" area in the Inspector window of the selected I/O module.
6. Make the following settings in the I/O addresses area:

   - Select the "Isochronous mode" option.
   - Select a process image partition, e.g., process image partition 1.
   - Click on the "Organization block" drop-down list and click the "Add new object" button or select an already existing OB. A dialog box for selecting organization blocks opens.
   - Select the "Synchronous Cycle" OB. Confirm the selection with "OK".

     In the case of automatic number assignment, OB 61 will be generated and opened. The "Isochronous mode" area is selected in the Inspector window, and you can continue directly with the setting of the application cycle and delay time and start the programming of the OB in the instruction section.
7. If, due to the utilized modules, the isochronous system only operates with a certain send clock (e.g. 1 ms) but the process values must be sampled faster, use the oversampling function. For modules that support this function, scan the process values for channels, for example, of an analog input module, at shorter intervals.
8. If required, insert additional I/O modules in the device view. Adapt the configuration and the settings for isochronous mode.

**Configuring the CPU**

1. To check the settings for isochronous mode, select the CPU in the device view of STEP 7.
2. In the Inspector window of the marked CPU, navigate to the area "Advanced configuration > Isochronous mode".
3. In the "Isochronous mode for local modules" area, check to determine if:

   - Isochronous mode is selected
   - "Local send clock" is selected as synchronization type when the clock synchronization is only to gain access for the centrally configured module   
     or as synchronization type "Use send clock of PROFINET interface", if the SEND clock for the centrally configured module is to be synchronized to the send clock of the PROFINET interface X1.

   If necessary, you can adapt the send clock and times T<sub>i</sub>/T<sub>o</sub> for the isochronous read-in/output of data.
4. In the "Detail overview" area, you see all modules of the configuration you can operate isochronously. Select or deselect isochronous mode for the desired modules as appropriate.

> **Note**
>
> **Configuring isochronous mode after a firmware update**
>
> If, after upgrading a project and subsequently updating the firmware of the S7-1500 CPU to the current version, the centrally plugged modules cannot be configured in isochronous mode, update the module description of the individual modules. To do this, open the "Properties" of the modules and click the "Update module description" button in the "General > Catalog information" tab.
>
> You can find additional information in the section "[Changing or updating hardware components](Configuring%20devices%20and%20networks.md#changing-or-updating-hardware-components)".

---

**See also**

[Configuring isochronous mode (S7-1500)](Special%20PROFINET%20configurations.md#configuring-isochronous-mode-s7-1500)
  
[Overview of the CPU properties (S7-1500)](#overview-of-the-cpu-properties-s7-1500)

#### Time sequence of synchronization in the central configuration (S7-1500)

##### From reading-in of input data to outputting of output data

The basic time sequence of all components involved in synchronization is explained in the following:

① Measured value acquisition in the process

② Isochronous read-in of measured values (input data) from the central I/O

③ Transport of input data to the CPU

④ Further processing in the input data in the isochronous application of the CPU (OB 6x)

⑤ Transport of output data to the central I/O

⑥ Isochronous output of output data

![From reading-in of input data to outputting of output data](images/112406774155_DV_resource.Stream@PNG-en-US.png)

So that all input data is ready for transport to the CPU at the next start of the cycle, the start of the I/O read-in cycle is advanced by the amount of lead time T<sub>i</sub>. T<sub>i</sub> is the "flash" for the inputs. After that, all synchronized inputs are read in. T<sub>i</sub> is necessary in order to compensate for analog-to-digital conversion and the like. The lead time T<sub>i</sub>can be configured by STEP 7 or by you. Let the lead time T<sub>i</sub> be assigned automatically by STEP 7. With the default setting, STEP 7 ensures that a common, minimum T<sub>i</sub> is set.

The backplane bus transports the input data to the CPU. The application is started synchronized to the cycle. That is, the isochronous mode interrupt OB is called after a configurable delay time T<sub>V</sub>. The user program in the isochronous mode interrupt OB defines the process response and provides the output data in time for the start of the next data cycle. The length of the data cycle (send clock) is always configured by you.

Within time T<sub>o</sub>, the data is:

- Transported to the I/O module over the backplane bus
- Processed in the I/O module, e.g. converted to an analog value

After expiration of time T<sub>o</sub>, the data is output to the process.

Time T<sub>o </sub>can be configured by STEP 7 or by you. Let time T<sub>o</sub> be assigned automatically by STEP 7. STEP 7 automatically calculates a common, minimum T<sub>o</sub>.

## Organization blocks (S7-1500)

This section contains information on the following topics:

- [OB start information (S7-1500)](#ob-start-information-s7-1500)
- [Description of all types of organization blocks (S7-1500)](#description-of-all-types-of-organization-blocks-s7-1500)
- [Setting parameters of organization blocks (S7-1500)](#setting-parameters-of-organization-blocks-s7-1500)

### OB start information (S7-1500)

#### Structure of the OB start information

When you configure the properties of an OB for S7-1500 CPUs, you also specify the structure of the OB start information:

- As for S7-300 and S7-400 CPUs
- Optimized start information

#### OB start information as for S7-300 and S7-400 CPUs

The OB start information is part of the local data and has the same structure as for S7-300 and S7-400 CPUs.

#### Optimized start information

The optimized start information is a set of input tags.

It only provides the information that is necessary to identify the OB start event.

Semantically identical information is displayed for various OBs under the same tag name within the optimized start information.

### Description of all types of organization blocks (S7-1500)

This section contains information on the following topics:

- [Startup OBs (S7-1500)](#startup-obs-s7-1500)
- [Cyclic OBs (S7-1500)](#cyclic-obs-s7-1500)
- [Time-of-day interrupt OBs (S7-1500)](#time-of-day-interrupt-obs-s7-1500)
- [Status interrupt OB (S7-1500)](#status-interrupt-ob-s7-1500)
- [Update interrupt OB (S7-1500)](#update-interrupt-ob-s7-1500)
- [OB for manufacturer- or profile-specific interrupt (S7-1500)](#ob-for-manufacturer--or-profile-specific-interrupt-s7-1500)
- [Time-delay interrupt OBs (S7-1500)](#time-delay-interrupt-obs-s7-1500)
- [Cyclic interrupt OBs (S7-1500)](#cyclic-interrupt-obs-s7-1500)
- [Hardware interrupt OBs (S7-1500)](#hardware-interrupt-obs-s7-1500)
- [Isochronous mode interrupt OBs (S7-1500)](#isochronous-mode-interrupt-obs-s7-1500)
- [Time error OB (S7-1500)](#time-error-ob-s7-1500)
- [Diagnostic interrupt OB (S7-1500)](#diagnostic-interrupt-ob-s7-1500)
- [Pull/plug interrupt OB (S7-1500)](#pullplug-interrupt-ob-s7-1500)
- [Rack error OB (S7-1500)](#rack-error-ob-s7-1500)
- [Programming error OB (S7-1500)](#programming-error-ob-s7-1500)
- [I/O access error OB (S7-1500)](#io-access-error-ob-s7-1500)
- [ProDiag OB (S7-1500)](#prodiag-ob-s7-1500)
- [Motion Control OBs (S7-1500)](Motion%20Control%20OBs%20%28S7-1500%2C%20S7-1500T%29.md#motion-control-obs-s7-1500-s7-1500t)

#### Startup OBs (S7-1500)

##### Description

The operating system calls each startup OB once at the transition from "STOP" to "RUN" mode. If several startup OBs are available, they are called in the order of their OB numbers, starting with the OB that has the lowest OB number.

The entirety of all startup OBs is referred to as the startup routine.

You can define default settings for your cyclic program in the startup routine.

All values of the process image input have the value zero here. There is no time limit for executing the startup routine. Time-driven or interrupt-driven organization blocks cannot be used.

After the startup routine has been completed, the operating system reads in the process image input and starts the cyclic program.

##### Structure of the start information

A startup OB has the following start information:

- As for S7-300 and S7-400 CPUs

  See [Startup organization blocks (OB 100, OB 101 and OB 102)](Organization%20blocks%20%28S7-300%2C%20S7-400%29.md#startup-organization-blocks-ob-100-ob-101-and-ob-102-s7-300-s7-400)

  In contrast to the assignment of start information with S7-300 and S7-400-CPUs:

  - OB_NUMBR=B#16#FF, if the OB number > 254
- Optimized start information:

| Name | Data type | Meaning |
| --- | --- | --- |
| LostRetentive | BOOL | =TRUE, if the contents of retentive data areas have been lost |
| LostRTC | BOOL | =TRUE, if the time of the real-time clock has been lost |

---

**See also**

[Events and OBs (S7-1500)](#events-and-obs-s7-1500)
  
[OB start information (S7-1500)](#ob-start-information-s7-1500)
  
["STARTUP" operating mode (S7-1500)](#startup-operating-mode-s7-1500)

#### Cyclic OBs (S7-1500)

##### Description

The essential basis of the user program is the cyclic program. Its associated program parts are processed cyclically: When the processing has been completed, the operating system starts processing it again.

One or more cycle OBs belong to the cyclic program. These have priority 1. This is the lowest priority of all OBs. The cyclic program can be interrupted by events of any other event class.

When you have created several program cycle OBs, these are called one after the other in the order of their OB numbers. The program cycle OB with the lowest OB number is called first.

The following events start the cyclic program:

- End of startup processing
- End of the processing of the previous run of the cyclic program

After the cyclic program is complete, the operating system updates the process images as follows:

1. It writes the values from the process image output to the output modules.
2. It reads the inputs at the input modules and transfers these to the process image input.

##### Cycle time monitoring

Cycle time refers to the runtime of the cyclic program, including the runtime of all nested program parts of higher-priority OBs. If you have created several program cycle OBs, each program cycle OB contributes to the cycle time.

The operating system monitors whether the cycle time remains smaller than the configured maximum cycle time. If the cycle time exceeds the maximum cycle time, OB 80 is called (start event W#16#0002:3501). You can prevent this by restarting time monitoring at an appropriate point in program by calling the RE_TRIGR instruction. If the maximum cycle time is exceeded a second time within a cycle (without restarting time monitoring), the CPU switches to STOP mode (event W#16#0002:3500).

##### Minimum cycle time

Apart from monitoring the maximum cycle time, it is also possible to guarantee a minimum cycle time. To do this, the operating system delays the start of a new cycle until the minimum cycle time has been reached.

##### Structure of the start information

- As for S7-300 and S7-400 CPUs

  See [Cyclic program (OB 1)](Organization%20blocks%20%28S7-300%2C%20S7-400%29.md#cyclic-program-ob-1-s7-300-s7-400)

  In contrast to the assignment of start information with S7-300 and S7-400-CPUs:

  - SCAN_1=B#16#01 at the first call and B#16#03 at each further call
  - OB_NUMBR=B#16#FF, if the OB number > 254
- Optimized start information:

| Name | Data type | Meaning |
| --- | --- | --- |
| Initial_Call | BOOL | =TRUE in the first call of this OB at:  - Transition from STOP or HOLD to RUN - After reloading |
| Retentivity | BOOL | =TRUE, if retentive data is available |

---

**See also**

[Events and OBs (S7-1500)](#events-and-obs-s7-1500)
  
[Evaluating the value status (S7-1500)](#evaluating-the-value-status-s7-1500)
  
[OB start information (S7-1500)](#ob-start-information-s7-1500)

#### Time-of-day interrupt OBs (S7-1500)

##### Description

The S7-1500 CPUs provide time interrupt OBs, which can be started as follows:

- Once at a specific time (date with time)
- Periodically (the following time intervals are possible in this case: every minute, hourly, daily, weekly,  monthly, end of month, yearly)

##### Starting a time interrupt OB

The following requirements must be met in order for the CPU to start a time interrupt OB:

- You must have previously set and activated the associated time interrupt. (Setting a time interrupt means specifying its start time and its duration.)
- You must have loaded the time interrupt OB to your CPU.

To set and activate a time interrupt, you have the following three options:

- You set and activate the time interrupt with STEP 7.
- You set the time interrupt with STEP 7 and activate it by calling the ACT_TINT instruction from your program.
- You set the time interrupt by calling the SET_TINTL instruction and activate it by calling the ACT_TINT instruction from within your program.

##### Rules for time interrupts

- If you set a time interrupt in such a way that the corresponding OB is to be processed once, the start time must not be in the past (relative to the real-time clock of the CPU).
- If you set a time interrupt in such a way that the corresponding OB is to be processed periodically, but the start time is in the past, then the time interrupt OB is processed the next time it is due according to the current time.
- The date of periodic time interrupts must correspond to a real date. For example, the monthly repetition of a time interrupt OB with start date 1/31 is therefore not possible. In this case, an OB is only started in the months that have 31 days.
- A time interrupt activated during startup is not executed until the startup has been completed.
- A startup deletes all time interrupts that were set and activated by an instruction in the user program.
- In the event of a transition from HOLD to RUN, the operating system checks whether there are elapsed time interrupts. If so, it calls the time error OB. If you have selected the same start information for it as for S7-300 and S7-400 CPUs, it enters whether time interrupts have been missed for the OBs 10 to 17 (and only for these). After the processing of OB 80 has been completed, the first missed OB is executed subsequently.

##### Behavior of time interrupts when time is adjusted ahead or back

The characteristics of the time interrupts depend on the time difference by which the time is set ahead or back. This is explained in more detail in the following table.

| Changing the time | Effect on time interrupt |
| --- | --- |
| < 20 s | - When the time is set ahead: Every skipped time interrupt is executed subsequently. The start information tag "CaughtUp" is set. OB 80 is not called. - When the time is adjusted back: A time interrupt that was already executed in the reset time range or is currently active is not repeated. |
| > > = 20 s | - When the time is set ahead: If one or more time interrupts were skipped, OB 80 is called. For each priority, the start information provides information on whether at least one time interrupt was skipped. If you do not delete the time interrupt in OB 80, the first skipped time interrupt is executed subsequently and the start information tag "CaughtUp" is set. - When the time is adjusted back: The time interrupts in the range of the reset time are repeated. If the time correction is greater than the duration of a time interrupt, the operating system calculates the time of the first time interrupt to be repeated. In the case of a repeated time interrupt, the start information tag "SecondTime" is set. |
| Changing from standard to daylight saving time and vice versa | This change is only effective if you use local time.  - When there is a change from standard to daylight saving time, a skipped time interrupt is executed subsequently and the start information tag "CaughtUp" is set. OB 80 is not called. - When there is a change from daylight saving time to standard time: the time interrupts in the range of the reset time are repeated. In the case of a repeated time interrupt, the start information tag "SecondTime" is set. |
| Changing the time zone (results in change of the local time) | The start time of the active time interrupts is recalculated.  - When the local time is adjusted ahead, a skipped time interrupt is executed subsequently and the start information tag "CaughtUp" is set. OB 80 is not called. - When the local time is adjusted back, time interrupts that have already been executed may be repeated. In the case of repeated time interrupts, the start information tag "SecondTime" is set. |

##### Time monitoring

When working with time interrupts, the following events can occur due to time monitoring by the operating system:

- W#16#0002:3504  
  The time was adjusted ahead by the change from standard to daylight saving time. The start time of time interrupts was skipped during this process. OB 80 is called.
- W#16#0002:3505  
  The time was adjusted ahead. The start time of time interrupts was skipped during this process. OB 80 is called.
- W#16#0002:3507  
  Buffer overflow for OB start events. An entry is made in the diagnostic buffer.
- W#16#0002:3502  
  Number of pending OB start events violates a preset limit. OB 80 is called.

##### Structure of the start information

- As for S7-300 and S7-400 CPUs

  See [Time-of-day interrupt organization blocks (OB 10 to OB 17)](Organization%20blocks%20%28S7-300%2C%20S7-400%29.md#time-of-day-interrupt-organization-blocks-ob-10-to-ob-17-s7-300-s7-400)

  In contrast to the assignment of start information with S7-300 and S7-400-CPUs:

  - STRT_INF=B#16#1F, if the OB number > 122
  - OB_NUMBR=B#16#FF, if the OB number > 254
- Optimized start information:

| Name | Data type | Meaning |
| --- | --- | --- |
| CaughtUp | BOOL | =TRUE if an OB call was executed subsequently because time was adjusted ahead |
| SecondTime | BOOL | =TRUE if an OB was called a second time because time was adjusted back. Note: SecondTime is set only once in the cases where time is adjusted back. |

---

**See also**

[Parameter assignment for time-of-day interrupt OBs (S7-1500)](#parameter-assignment-for-time-of-day-interrupt-obs-s7-1500)
  
[Events and OBs (S7-1500)](#events-and-obs-s7-1500)
  
[OB start information (S7-1500)](#ob-start-information-s7-1500)

#### Status interrupt OB (S7-1500)

##### Description

When it receives a status interrupt, the operating system of the S7-1500 CPU calls the status interrupt OB. This may be the case if a module of a slave changes its operating state, for example, from "RUN" to "STOP". For more detailed information on events that trigger a status interrupt, refer to the documentation of the slave or device manufacturer.

##### Structure of the start information

- As for S7-300 and S7-400 CPUs

  See [Status interrupt OB (OB 55)](Organization%20blocks%20%28S7-300%2C%20S7-400%29.md#status-interrupt-ob-ob-55-s7-300-s7-400)
- Optimized start information:

| Name | Data type | Meaning |
| --- | --- | --- |
| LADDR | HW_IO | Hardware identifier of the component triggering the interrupt |
| Slot | UINT | Slot number of the component triggering the interrupt |
| Specifier | WORD | Interrupt specifier from the interrupt frame:  - PROFIBUS:   - Bit 0 to 1: Interrupt specifier   - Bit 2: Add_Ack   - Bit 3 to 7: Seq. no.   - Bit 8 to 15: Reserved  - Central and PNIO:   - Bits 0 to 10: Sequence number (value range 0 to 2047)   - Bits 11 to 15: 0 |

---

**See also**

[Events and OBs (S7-1500)](#events-and-obs-s7-1500)
  
[OB start information (S7-1500)](#ob-start-information-s7-1500)

#### Update interrupt OB (S7-1500)

##### Description

When it receives an update interrupt, the operating system of the S7-1500 CPU calls the update interrupt OB. This may be the case if you changed a parameter on a slot of a slave or device. For more detailed information on events that trigger an update interrupt, refer to the documentation of the slave or device manufacturer.

##### Structure of the start information

- As for S7-300 and S7-400 CPUs

  See [Update interrupt OB (OB 56)](Organization%20blocks%20%28S7-300%2C%20S7-400%29.md#update-interrupt-ob-ob-56-s7-300-s7-400)
- Optimized start information:

| Name | Data type | Meaning |
| --- | --- | --- |
| LADDR | HW_IO | Hardware identifier of the component triggering the interrupt |
| Slot | UINT | Slot number of the component triggering the interrupt |
| Specifier | WORD | Interrupt specifier from the interrupt frame:  - PROFIBUS:   - Bit 0 to 1: Interrupt specifier   - Bit 2: Add_Ack   - Bit 3 to 7: Seq. no.   - Bit 8 to 15: Reserved - Central and PNIO:   - Bits 0 to 10: Sequence number (value range 0 to 2047)   - Bits 11 to 15: 0 |

---

**See also**

[Events and OBs (S7-1500)](#events-and-obs-s7-1500)
  
[OB start information (S7-1500)](#ob-start-information-s7-1500)

#### OB for manufacturer- or profile-specific interrupt (S7-1500)

##### Description

When it receives a manufacturer- or profile-specific interrupt, the operating system of the S7-1500 CPU calls OB 57. For more detailed information on events that trigger this type of interrupt, refer to the documentation of the slave or device manufacturer.

##### Structure of the start information

- As for S7-300 and S7-400 CPUs

  See [OB for manufacturer-specific alarms (OB 57)](Organization%20blocks%20%28S7-300%2C%20S7-400%29.md#ob-for-manufacturer-specific-alarms-ob-57-s7-300-s7-400)

  In contrast to the assignment of start information with S7-300 and S7-400-CPUs:

  - STRT_INF=B#16#67
- Optimized start information:

| Name | Data type | Meaning |
| --- | --- | --- |
| LADDR | HW_IO | Hardware identifier of the component triggering the interrupt |
| Slot | UINT | Slot number of the component triggering the interrupt |
| Specifier | WORD | Interrupt specifier from the interrupt frame:  - PROFIBUS:   - Bit 0 to 1: Interrupt specifier   - Bit 2: Add_Ack   - Bit 3 to 7: Seq. no.   - Bit 8 to 15: Reserved - Central and PNIO:   - Bits 0 to 10: Sequence number (value range 0 to 2047)   - Bits 11 to 15: 0 |

---

**See also**

[Events and OBs (S7-1500)](#events-and-obs-s7-1500)
  
[OB start information (S7-1500)](#ob-start-information-s7-1500)

#### Time-delay interrupt OBs (S7-1500)

##### Description

A time-delay interrupt OB is started after a configurable time delay of the operating system. The time delay begins to elapse when the "SRT_DINT" instruction is called (this is the start of the associated time-delay interrupt).

Before a time-delay interrupt OB can be called by the operating system, the following conditions must be met:

- The time-delay interrupt must be started by calling the "SRT_DINT" instruction.
- The time-delay interrupt OB must not be deselected during configuration.

The time-delay interrupt OB must exist in the CPU.

##### Influencing time-delay interrupts with instructions

You can use the "CAN_DINT" instruction to cancel a time-delay interrupt which has already been started and whose associated time-delay interrupt OB has not yet been called by the operating system and use the "SRT_DINT" instruction to restart it (and thereby assign a different delay time to it). In addition, you can use the "QRY_DINT" instruction to query the current status of a time-delay interrupt.

You can disable and re-enable time-delay interrupts using the "DIS_AIRT" and "EN_AIRT" instructions.

> **Note**
>
> If you block this interrupt with "DIS_AIRT" after the execution of "SRT_DINT", processing is only continued after enabling with "EN_AIRT". This means that the delay time is extended accordingly.

##### Calling error OBs in connection with time-delay interrupt OBs

If the delay time of a time-delay interrupt expired before the processing of the associated time-delay interrupt OB was completed, the operating system generates a time error (calls OB 80).

##### Processing of time-delay interrupts depending on operating mode

"SRT_DINT" can be called and the delay time can elapse in both startup and in RUN mode. Time-delay interrupt OBs, however, are only processed in RUN mode. If a time-delay interrupt starts in a startup OB and the delay time has expired before the CPU reaches RUN mode, the call of the corresponding time-delay interrupt OB is delayed until the CPU is in RUN mode.

A warm or cold restart clears all start events for a time-delay interrupt OB.

##### Structure of the start information

- As for S7-300 and S7-400 CPUs

  See [Time-delay interrupt organization blocks (OB 20 to OB 23)](Organization%20blocks%20%28S7-300%2C%20S7-400%29.md#time-delay-interrupt-organization-blocks-ob-20-to-ob-23-s7-300-s7-400)

  In contrast to the assignment of start information with S7-300 and S7-400-CPUs:

  - STRT_INF=B#16#2F, if the OB number > 122
  - OB_NUMBR=B#16#FF, if the OB number > 254
- Optimized start information:

| Name | Data type | Meaning |
| --- | --- | --- |
| Sign | WORD | User ID: Input parameter SIGN from the call of the "SRT_DINT" instruction |

---

**See also**

[SRT_DINT: Start time-delay interrupt (S7-1200, S7-1500)](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#srt_dint-start-time-delay-interrupt-s7-1200-s7-1500)
  
[Events and OBs (S7-1500)](#events-and-obs-s7-1500)
  
[OB start information (S7-1500)](#ob-start-information-s7-1500)

#### Cyclic interrupt OBs (S7-1500)

##### Description

You can start program parts at equidistant time intervals with the help of a cyclic interrupt OB.

The start times of a cyclic interrupt OB result as follows from its time interval and its phase offset:

Start times = n * time interval + phase offset (n = 0, 1, 2 ... )

- The time interval is the period of time between two calls. It is an integer multiple of the basic clock cycle of 1 µs.
- The phase offset is the time interval by which the start times are offset compared to the multiple of the time interval.

  A phase offset may be advisable when you are using multiple cyclic interrupt OBs. When their time intervals have a common multiple, for example, you can use a phase offset to prevent simultaneous start times.

##### Example of the use of a phase offset

You are using two cyclic interrupt OBs in your program: one OB with a time interval of 20 ms and one with a time interval of 100 ms. Use a phase offset to ensure that these are not called simultaneously at integer multiples of 100 ms.

##### Call of error OBs in connection with cyclic interrupt OBs

The runtime of a cyclic interrupt OB must be significantly smaller than its time interval. Otherwise, it could still happen that the time interval of a cyclic interrupt has expired but the corresponding cyclic interrupt OB is still being processed. In this case, the operating system generates a time error (calls OB 80). The cyclic interrupt that caused the error is executed later or discarded. However, only one cyclic interrupt OB for each priority can be executed later.

##### Changing the time interval or the phase offset in RUN mode

You can also change the values for the time interval or the phase offset in RUN mode, for example, by loading in RUN mode or by calling the "SET_CINT" instruction.

Please note that the operating system of the CPU always calculates the start events of a cyclic interrupt OB relative to when the CPU is switched on (POWER ON). Depending on the point in time at which the parameter change takes place, the new time interval can therefore once have a different value than the newly specified value:

- Two successive start events of the cyclic interrupt OB can have a shorter interval than the old and a shorter interval than the new time interval (in extreme cases, a significantly shorter interval). This is shown in the following graphic when changing the time interval from T<sub>0</sub> to T<sub>1</sub> as Δt<sub>1</sub>.
- Two successive start events of the cyclic interrupt OB can be further apart than the old and the new time interval (the distance can be as large as the sum of the old and the new time interval). This is shown in the following graphic when changing the time interval from T<sub>1</sub> to T<sub>2</sub> as Δt<sub>2</sub>.

**Cyclic interrupt OB calls when the time interval changes in RUN mode**

![Changing the time interval or the phase offset in RUN mode](images/147251650571_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | POWER ON |
| ② | CPU changes to RUN |
| ③ | The time interval is set from T<sub>0</sub> to T<sub>1</sub> using "SET_CINT" |
| ④ | The time interval is set from T<sub>1</sub> to T<sub>2</sub> using "SET_CINT" |

##### Structure of the start information

- As for S7-300 and S7-400 CPUs

  See [Cyclic interrupt organization blocks (OB 30 to OB 38)](Organization%20blocks%20%28S7-300%2C%20S7-400%29.md#cyclic-interrupt-organization-blocks-ob-30-to-ob-38-s7-300-s7-400)

  In contrast to the assignment of start information with S7-300 and S7-400-CPUs:

  - STRT_INF=B#16#3F, if the OB number > 122 and the phase offset and cycle time are specified in ms
  - OB_NUMBR=B#16#FF, if the OB number > 254
- Optimized start information

| Name | Data type | Meaning |
| --- | --- | --- |
| Initial_Call | BOOL | =TRUE in the first call of this OB  - At the transition from STOP or HOLD to RUN - After reloading |
| Event_count | INT | Number of discarded start events since the last start of this OB |

---

**See also**

[Assigning parameters to cyclic interrupt OBs (S7-1500)](#assigning-parameters-to-cyclic-interrupt-obs-s7-1500)
  
[Events and OBs (S7-1500)](#events-and-obs-s7-1500)
  
[OB start information (S7-1500)](#ob-start-information-s7-1500)

#### Hardware interrupt OBs (S7-1500)

##### Description

You can use hardware interrupt OBs to react to those events of modules with hardware interrupt capability which trigger a hardware interrupt. You define which events these are by means of configuration.

> **Note**
>
> **Use of hardware interrupts**
>
> If possible, use hardware interrupts only to react to sporadically occurring events of modules with hardware interrupt capability.
>
> The usage of hardware interrupts to react to events recurring often or very often does not make sense and can result in timeouts on your CPU under unfavorable conditions.

You can assign only one hardware interrupt OB to each event that triggers a hardware interrupt. Multiple events, however, can be assigned to one hardware interrupt OB (in extreme cases, all events of a module triggering a hardware interrupt).

For S7-1500 modules, individual channels can trigger hardware interrupts (e.g., a binary input on a rising edge).

##### Functionality of a hardware interrupt OB

After a module or submodule has triggered a hardware interrupt, the operating system determines the associated event and the associated hardware interrupt OB. If the currently active OB has a lower priority than this hardware interrupt OB, the hardware interrupt OB is started. Otherwise, the hardware interrupt OB is positioned in the queue that corresponds to its priority. The hardware interrupt is acknowledged after the completion of the corresponding hardware interrupt OB.

If another process event occurs on the same module or submodule during the time between identification and acknowledgment of a hardware interrupt, the following applies:

- If the event occurs on the channel that triggered the current hardware interrupt, the relevant hardware interrupt is lost. Another hardware interrupt can only be triggered by this channel when the current hardware interrupt is acknowledged.
- If the event occurs on a different channel, a hardware interrupt is triggered.

There may be additional restrictions for distributed I/O: for example, that a module or submodule can trigger only one interrupt of an interrupt type until the current interrupt has been acknowledged.

Hardware interrupt OBs are called only in RUN mode of the CPU.

##### Structure of the start information

- As for S7-300 and S7-400 CPUs: The USI, IChannel and EventType tags (explanation can be found in the optimized start information) are copied to "OB40_POINT_ADDR".

  See [Hardware interrupt organization blocks (OB 40 to OB 47)](Organization%20blocks%20%28S7-300%2C%20S7-400%29.md#hardware-interrupt-organization-blocks-ob-40-to-ob-47-s7-300-s7-400)

  In contrast to the assignment of start information with S7-300 and S7-400-CPUs:

  - STRT_INF=B#16#41
  - OB_NUMBR=B#16#FF, if the OB number > 254
- Optimized start information:

| Name | Data type | Meaning |
| --- | --- | --- |
| LADDR | HW_IO | Hardware identifier of the module that triggers the hardware interrupt |
| USI | WORD | Identifier for future extensions (not user-relevant) |
| IChannel | USINT | Number of the channel that triggered the hardware interrupt |
| EventType | BYTE | Identifier for the event type to which the event that triggered the interrupt belongs (e.g., rising edge)  This identifier can be found in the description of the respective module. |
| PointAddr  (Version V14.0 or higher of the TIA Portal) | DWORD | - In the case of digital modules: Bit array containing the inputs on the module that have triggered the hardware interrupt.   Refer to the respective module description for information on which bit of Point_Addr is assigned to which module channel. - In the case of analog modules: Bit field with the information as to which channel has exceeded which threshold.    Refer to the module description for the precise structure. - In the case of CPs or IMs: Interrupt status of the module (not user-relevant) |

> **Note**
>
> **USI has the value 0xFFFF**
>
> If you have configured the affected module in HW Config with GSDML resources, USI has the value 0xFFFF. In this case, IChannel and EventType do not get valid values. To determine the event that triggered the interrupt, proceed as follows:
>
> You either use the structure of the start information as for S7-300 and S7-400 CPUs,
>
> or you use the optimized start information and call the RALRM instruction in the hardware interrupt OB.

##### Opening, compiling and loading of hardware interrupt OBs

Because the optimized start information of the hardware interrupt OB in version 14.0 or higher of the TIA Portal includes an additional tag, constellations may result in which opening, compiling and loading of the hardware interrupt OBs to the CPU is no longer possible. These constellations are listed below:

- You copy a hardware interrupt OB with a new interface to an S7-1500 CPU with firmware version < V2.0 or to an S7-1200-CPU in the engineering system. The OB can then no longer be opened, compiled and loaded.
- You replace an S7-1500 CPU with firmware version >= V2.0 that includes a hardware interrupt OB with new interface with an S7-1500 CPU with firmware version < V2.0 in the engineering system. The OB can then no longer be opened, compiled and loaded.

However, no problems arise during opening, compiling and loading in the following constellations:

- You copy a hardware interrupt OB with old interface to an S7-1500 CPU with firmware version >= V2.0 in the engineering system. The hardware interrupt OB retains the old interface.
- You replace an S7-1500 CPU with firmware version < V2.0 that includes a hardware interrupt OB with old interface with an S7-1500 CPU with firmware version >= V2.0 in the engineering system. The hardware interrupt OB retains the old interface.

---

**See also**

[Assigning parameters to hardware interrupt OBs (S7-1500)](#assigning-parameters-to-hardware-interrupt-obs-s7-1500)
  
[Events and OBs (S7-1500)](#events-and-obs-s7-1500)
  
[What you need to know about HW identifiers (S7-1200, S7-1500, S7-1500T)](Configuring%20automation%20systems.md#what-you-need-to-know-about-hw-identifiers-s7-1200-s7-1500-s7-1500t)
  
[OB start information (S7-1500)](#ob-start-information-s7-1500)
  
[Example of a hardware interrupt event (S7-1500)](#example-of-a-hardware-interrupt-event-s7-1500)

#### Isochronous mode interrupt OBs (S7-1500)

##### Description

Isochronous mode interrupt OBs are used to start subprograms isochronously to the DP cycle or PN send clock.

You update the associated process image partition of the inputs and the associated process image partition of the outputs by calling the instructions SYNC_PI and SYNC_PO in the isochronous mode interrupt OB.

| Symbol | Meaning |
| --- | --- |
|  | **Caution** |
| **Direct access**  In cases of direct access, avoid access to I/O areas to which process image partitions with isochronous mode interrupt OB connection are assigned. |  |

> **Note**
>
> **Effectiveness of the OB parameter "Report event overflow into diagnostic buffer"**
>
> When you select the check box "Report event overflow into diagnostic buffer" for the OB parameters, this does not become effective until you have loaded the OB properties to the CPU and the CPU has then performed a STOP-RUN transition.

##### Structure of the start information

- As for S7-300 and S7-400 CPUs

  See [Synchronous cycle interrupt OBs (OB 61 to OB 64)](Organization%20blocks%20%28S7-300%2C%20S7-400%29.md#synchronous-cycle-interrupt-obs-ob-61-to-ob-64-s7-300-s7-400)

  In contrast to the assignment of start information with S7-300 and S7-400-CPUs:

  - STRT_INF=B#16#6F, if the OB number > 122
  - OB_NUMBR=B#16#FF, if the OB number > 254
- Optimized start information:

| Name | Data type | Meaning |
| --- | --- | --- |
| Initial_Call | BOOL | =TRUE in the first call of this OB during transition from STOP to RUN |
| PIP_Input | BOOL | TRUE: The associated process image input is up-to-date  Note: For S7-1500 CPUs, this variable always has the value FALSE, since updating the corresponding process image partition of the inputs must be carried out by calling the SYNC_PI instruction. |
| PIP_Output | BOOL | TRUE: The associated process image output was transferred to the outputs in good time after the last cycle  Note: For S7-1500 CPUs, this variable always has the value FALSE, since updating the corresponding process image partition of the outputs must be carried out by calling the SYNC_PO instruction. |
| IO_System | USINT | Number of the distributed I/O system triggering the interrupt |
| Event_Count | INT | - = n: Number of lost cycles - = -1: An unknown number of cycles has been lost (e.g., because cycle has changed). |
| SyncCycleTime | LTIME | Calculated cycle time |

---

**See also**

[Assigning parameters to isochronous mode interrupt OBs (S7-1500)](#assigning-parameters-to-isochronous-mode-interrupt-obs-s7-1500)
  
[Events and OBs (S7-1500)](#events-and-obs-s7-1500)
  
[OB start information (S7-1500)](#ob-start-information-s7-1500)
  
[Overview of block properties](Creating%20and%20managing%20blocks.md#overview-of-block-properties)

#### Time error OB (S7-1500)

##### Description

The S7-1500 CPU operating system calls the time error OB if one of the following errors occurs:

- First violation of the cycle time within a cycle

  > **Note**
  >
  > If the cycle time is violated twice in the same cycle, the CPU goes to STOP mode. You can prevent this by calling the "RE_TRIGR" instruction at a suitable point.
- The number of requested but not completely processed OB requests has reached the configured warning limit. (For migrated programs, this warning limit set to 1.)

  If you have set the warning limit to 1, this means: If a start event, e.g., for a cyclic interrupt OB, occurs before the previous processing of the same OB has been completed, the operating system calls OB 80.  
  This applies to all events whose associated OB can cause a time error.
- Expired time interrupt on re-entry into RUN mode after the CPU was, for example, in HOLD
- Skipped time interrupt due to the time being adjusted more than 20 s ahead (also in the case of changeover from standard time to daylight saving time)

##### Structure of the start information

- As for S7-300 and S7-400 CPUs

  See [Time error OB (OB 80)](Organization%20blocks%20%28S7-300%2C%20S7-400%29.md#time-error-ob-ob-80-s7-300-s7-400)
- Optimized start information

| Name | Data type | Meaning |
| --- | --- | --- |
| Fault_ID | BYTE | Error code. Possible values:  - B#16#01: Cycle time exceeded - B#16#02: The requested OB is still being processed. - B#16#05: Expired time interrupt due to time jump - B#16#06: Expired time interrupt upon re-entry into RUN after HOLD - B#16#07: Overflow of the OB request buffer for the current priority class - B#16#08: Isochronous mode interrupt - time error - B#16#09: Interrupt loss due to high interrupt load - B#16#0B: Technology synchronization interrupt - time error - b#16#0C: (only for S7-1500 R/H CPUs) cycle time exceeded for the second time |
| Csg_OBnr | OB_ANY | Number of the OB that was being processed when the time error occurred |
| Csg_Prio | UINT | Priority of the OB that was being processed when the time error occurred |

> **Note**
>
> **Csg_OBnr=0 and Csg_Prio=0**
>
> If both the Csg_OBnr and Csg_Prio (or OB80_ERR_EV_CLASS and OB80_ERR_EV_NUM, if you have selected the S7-300 and S7-400 CPUs as structure of the start information) had the value zero, the CPU performed background activities as the time error occurred.

---

**See also**

[Events and OBs (S7-1500)](#events-and-obs-s7-1500)
  
[OB start information (S7-1500)](#ob-start-information-s7-1500)
  
[Programming of S7-1500R/H CPUs (S7-1500)](Principle%20of%20operation%20for%20S7-1500R-H%20CPUs%20%28S7-1500%29.md#programming-of-s7-1500rh-cpus-s7-1500)

#### Diagnostic interrupt OB (S7-1500)

##### Description

The operating system of the S7-1500 CPU calls the diagnostic interrupt OB in the following cases:

- A diagnostics-capable S7-1500 module detects a change in its diagnostic status and sends a diagnostic interrupt request to the CPU.
- A diagnostics-capable S7-300 or S7-400 module for which you have enabled the diagnostic interrupt detects a change in its diagnostic status and sends a diagnostic interrupt request to the CPU.
- An event occurs that was triggered by an error in the power supply or the battery backup.

  > **Note**
  >
  > With the S7-300 and S7-400 CPUs, such an event causes the power supply error OB to be called.
- The operating system has detected memory errors.

  > **Note**
  >
  > With the S7-300 and S7-400 CPUs, such an event causes the CPU hardware error OB to be called.

##### Structure of the start information

- As for S7-300 and S7-400 CPUs

  See [Diagnostic interrupt OB (OB 82)](Organization%20blocks%20%28S7-300%2C%20S7-400%29.md#diagnostic-interrupt-ob-ob-82-s7-300-s7-400)
- Optimized start information:

| Name | Data type | Meaning |
| --- | --- | --- |
| IO_state | WORD | Status of the hardware object:  - Bit 0: Good - Bit 1: Deactivated - Bit 2: Maintenance required - Bit 3: Maintenance demanded - Bit 4: Error - Bit 5: Not available - Bit 6: Qualified - Bit 7: Not available - Bits 8 to 14: Reserved (always "0") - Bit 15: Network / hardware fault   If bit 4 = 1 or bit 5 = 1:   - Bit 15 = 0: Network error   - Bit 15 = 1: Hardware error |
| LADDR | HW_ANY | Hardware identifier of the hardware object that triggered the diagnostic interrupt |
| Channel | UINT | Channel number |
| MultiError | BOOL | =TRUE, if there is more than one error |

---

**See also**

[Events and OBs (S7-1500)](#events-and-obs-s7-1500)
  
[OB start information (S7-1500)](#ob-start-information-s7-1500)

#### Pull/plug interrupt OB (S7-1500)

##### Description

The S7-1500 CPU operating system calls the pull/plug interrupt OB if a configured and non-disabled distributed I/O module or submodule is removed or inserted.

> **Note**
>
> The removing or inserting of a central module leads to STOP of the CPU, except for CPUs 1510SP-1 PN and 1512SP-1 PN and 1514SP-2 PN.

##### Structure of the start information

- As for S7-300 and S7-400 CPUs

  See [Insert/remove module interrupt organization block (OB 83)](Organization%20blocks%20%28S7-300%2C%20S7-400%29.md#insertremove-module-interrupt-organization-block-ob-83-s7-300-s7-400)
- Optimized start information:

| Name | Data type | Meaning |
| --- | --- | --- |
| LADDR | HW_IO | Hardware identifier of the affected module or submodule |
| Event_Class | BTYE | - B#16#38: (Sub)module plugged - B#16#39: (Sub)module pulled or not responding |
| Fault_ID | BYTE | Error code (possible values: B#16#51, B#16#54, B#16#55, B#16#56, B#16#57, B#16#58, B#16#61, B#16#63, B#16#64, B#16#65, B#16#66, B#16#71, B#16#72, B#16#73) |

The following table shows which event caused the start of the pull/plug interrupt OB.

| ev_class   B#16# ... | fault_id  B#16# ... | Meaning |
| --- | --- | --- |
| 39 | 51 | IO module removed |
| 39 | 54 | IO submodule removed |
| 38 | 54 | IO submodule inserted and matches configured submodule |
| 38 | 55 | IO submodule inserted, but does not match configured submodule |
| 38 | 56 | IO submodule inserted, but error in module parameter assignment |
| 38 | 57 | IO submodule or module inserted, but with fault or maintenance |
| 38 | 58 | IO submodule, access error corrected |
| 39 | 61 | Module removed or not responding |
| 38 | 61 | Module inserted |
| 39 | 71 | In the "RUN-Redundant" system state of an S7-1500R/H system, a configured central module was removed. Redundancy with its partner module was lost. |
| 38 | 72 | In the "RUN-Redundant" system state of an S7-1500R/H system, a configured central module was inserted. Redundancy with its partner module was restored. |
| 38 | 73 | In the "RUN-Redundant" system state of an S7-1500R/H system, a configured central module was inserted, but with a fault. Redundancy with its partner module was restored. |

---

**See also**

[Events and OBs (S7-1500)](#events-and-obs-s7-1500)
  
[OB start information (S7-1500)](#ob-start-information-s7-1500)

#### Rack error OB (S7-1500)

##### Description

The S7-1500 CPU operating system calls the OB 86 in the following cases:

- The failure of a DP master system or of a PROFINET IO system is detected (in the case of either an incoming or an outgoing event).
- The failure of a DP slave or of an IO device is detected (in the case of either an incoming or an outgoing event).
- Failure of some of the submodules of a PROFINET I-device is detected.

##### Structure of the start information

- As for S7-300 and S7-400 CPUs

  See [Rack failure organization block (OB 86)](Organization%20blocks%20%28S7-300%2C%20S7-400%29.md#rack-failure-organization-block-ob-86-s7-300-s7-400)
- Optimized start information:

| Name | Data type | Meaning |
| --- | --- | --- |
| LADDR | HW_Device | Hardware identifier of the defective hardware object |
| Event_Class | BYTE | - B#16#38: outgoing event - B#16#39: incoming event |
| Fault_ID | BYTE | Error code (possible values: B#16#C3, B#16#C4, B#16#C9, B#16#CA, B#16#CB, B#16#CC, B#16#CD, B#16#CE, B#16#CF, B#16#F8, B#16#F9) |

The following table shows which event caused the start of OB 86.

| ev_class  B#16# ... | fault_id  B#16# ... | Meaning |
| --- | --- | --- |
| 39 | C3 | Failure of a DP master system |
| 39/38 | C4 | Failure/return of a DP slave |
| 39 | CA | Failure of a PROFINET IO system |
| 39/38 | CB | Failure/return of a PROFINET IO device |
| 38 | CC | Return of a PROFINET IO device with fault or maintenance |
| 38 | CD | Return of a PROFINET IO device, deviation between preset/actual configuration |
| 38 | CE | Return of a PROFINET IO device, error in module configuration |
| 39/38 | F8 | Failure/return of some of the submodules of a PROFINET I-device |
| 38 | F9 | Return of some of the submodules of a PROFINET I-device with a device configuration difference |

---

**See also**

[Events and OBs (S7-1500)](#events-and-obs-s7-1500)
  
[OB start information (S7-1500)](#ob-start-information-s7-1500)

#### Programming error OB (S7-1500)

##### Requirement for calling the programming error OB

A necessary prerequisite for the S7-1500 CPU to call the programming error OB is: You do not use a local troubleshooting in the module causing the error, which means that you do not use the GET_ERROR instruction or the GET_ERR_ID instruction there.

##### Description

The S7-1500 CPU operating system calls the programming error OB if a programming error occurs during the processing of an instruction of the user program. The programming error OB is processed with the priority set for it.

> **Note**
>
> If you use the local troubleshooting in the module, i.e. the instruction GET_ERROR or GET_ERR_ID, the programming error OB is not called when a programming error occurs.

##### Structure of the start information

- As for S7-300 and S7-400 CPUs

  See [Programming error organization block (OB 121)](Organization%20blocks%20%28S7-300%2C%20S7-400%29.md#programming-error-organization-block-ob-121-s7-300-s7-400)
- Optimized start information:

| Name | Data type | Meaning |
| --- | --- | --- |
| BlockNr | UINT | Number of the block in which the programming error occurred |
| Reaction | USINT | - 0: Ignore errors - 1: Replace incorrect value - 2: Skip command - 3: Programmed error handling, triggered by an array access with invalid index, for example, or by an error during parameter supply of an FC or FB |
| Fault_ID | BYTE | Error code (possible values: B#16#00, B#16#03, B#16#04, B#16#05, B#16#20, B#16#21, B#16#22, B#16#23, B#16#24, B#16#25, B#16#26, B#16#27, B#16#28, B#16#29, B#16#2C, B#16#30, B#16#31, B#16#32, B#16#33, B#16#34, B#16#35, B#16#38, B#16#39, B#16#3A, B#16#3B, B#16#3C, B#16#3D, B#16#3E, B#16#3F, B#16#50, B#16#51, B#16#75, B#16#76, B#16#A1, B#16#A2) |
| BlockType | USINT | Type of block in which the error occurred:  - OB: 1 - FC: 2 - FB: 3 - SFC: 4 - SFB: 5 - DB: 6 |
| Area | USINT | Area in which the incorrect access occurred:  - Local data: B#16#40 to 4E, 86, 87, 8E, 8F, C0 to CE - Process image input: B#16#01 - Process image output: B#16#02 - Technology DB: B#16#04 - I: B#16#81 - Q: B#16#82 - M: B#16#83 - DB: B#16#84, 85, 8A, 8B |
| DBNr | Block_DB | DB no. if AREA = DB or DI |
| Csg_OBNr | OB_ANY | OB number (121) |
| Csg_Prio | USINT | OB priority |
| Width | USINT | Type of access during which the error occurred:  - Bit:   - B#16#00 for access to the standard memory area   - B#16#01 for access to the optimized memory area - Byte: B#16#01 - Word: B#16#02 - DWord: B#16#03 - LWord: B#16#04 |

The following table shows the meaning of the error codes:

| fault_ID  B#16# ... | Meaning |
| --- | --- |
| 00 | Maximum nesting depth of block calls exceeded |
| 03 | You have used a NULL pointer to address an operand. |
| 04 | Unknown instruction |
| 05 | Stop instruction |
| 20 | The addressed string has incorrect length information. |
| 21 | BCD conversion error |
| 22 | Area length error when reading |
| 23 | Area length error when writing |
| 24 | Area error when reading |
| 25 | Area error when writing |
| 26 | Error in timer no. |
| 27 | Error in counter no. |
| 28 | Read access to a byte, word or double word with a pointer whose bit address is not zero |
| 29 | Read access to a byte, word or double word with a pointer, whose bit address is not zero |
| 2C | You have used a NULL pointer to address an operand. |
| 30 | Write access to a write-protected global DB |
| 31 | Write access to a write-protected instance DB |
| 32 | DB number error when accessing a global DB |
| 33 | DB number error when accessing an instance DB |
| 34 | Number error during FC call |
| 35 | Number error during FB call |
| 38 | The type-safe data block is not loaded. |
| 39 | The data block is not defined as type-safe. |
| 3A | Access to a DB that is not loaded; the DB number is located in the permitted area |
| 3B | DB does not exist |
| 3C | Access to an FC that is not loaded; the FC number lies in the permissible area |
| 3D | Access to an SFC that is not loaded; the SFC number lies in the permissible area |
| 3E | Access to an FB that is not loaded; the FB number lies in the permissible area |
| 3F | Access to an SFB that is not available; the SFB number lies in the permissible area |
| 50 | The type-safe data block is not loaded. |
| 51 | The data block is not defined as type-safe. |
| 75 | The maximum nesting depth for block calls was exceeded. |
| 76 | The maximum of available local data was exceeded. |
| A1 | Write access to a write-protected tag |
| A2 | Access to a tag that contains an invalid numerical value |

---

**See also**

[Events and OBs (S7-1500)](#events-and-obs-s7-1500)
  
[OB start information (S7-1500)](#ob-start-information-s7-1500)
  
[Overview of mechanisms for error handling](Programming%20basics.md#overview-of-mechanisms-for-error-handling)

#### I/O access error OB (S7-1500)

##### Requirement for call of the I/O access error OB

A necessary prerequisite for the S7-1500 CPU to call the I/O access error OB is: You do not use a local troubleshooting in the module causing the error, which means that you do not use the GET_ERROR instruction or the GET_ERR_ID instruction there.

##### Description

The S7-1500-CPU operating system calls the I/O access error OB if an error occurs during direct access to the I/O data while an instruction of the user program is being executed. This, for example, is the case if a read error occurs during direct access to data of an input module. The I/O access error OB is processed with the priority assigned to it.

> **Note**
>
> If you use the local troubleshooting in the module, i.e. the instruction GET_ERROR or GET_ERR_ID, the I/O access error OB is not called when a programming error occurs.

##### Structure of the start information

- As for S7-300 and S7-400 CPUs

  See [I/O access error organization block (OB 122)](Organization%20blocks%20%28S7-300%2C%20S7-400%29.md#io-access-error-organization-block-ob-122-s7-300-s7-400)
- Optimized start information:

| Name | Data type | Meaning |
| --- | --- | --- |
| BlockNr | UINT | Number of the block in which the I/O access error occurred |
| Reaction | USINT | 0: Ignore error, 1: Replace incorrect value, 2: Skip command |
| Fault_ID | BYTE | Error code:  - B#16#42: I/O access error, reading - B#16#43: I/O access error, writing |
| BlockType | USINT | Type of block in which the error has occurred:  - OB: 1 - FC: 2 - FB: 3 - SFC: 4 - SFB: 5 - DB: 6 |
| Area | USINT | Identifier for the range in which the incorrect access occurred:  - B#16#01: Direct access to input - B#16#02: Direct access to output - B#16#81: Access to process image input - B#16#82: Access to process image output |
| DBNr | Block_DB | not user-relevant |
| Csg_OBNr | OB_ANY | OB number causing the I/O access error |
| Csg_Prio | USINT | OB priority that causes the I/O access error |
| Width | USINT | Type of access during which the error occurred:  - Bit: B#16#00 - Byte: B#16#01 - Word: B#16#02 - DWord: B#16#03 - LWord: B#16#04 |

---

**See also**

[Events and OBs (S7-1500)](#events-and-obs-s7-1500)
  
[OB start information (S7-1500)](#ob-start-information-s7-1500)
  
[Overview of mechanisms for error handling](Programming%20basics.md#overview-of-mechanisms-for-error-handling)

#### ProDiag OB (S7-1500)

##### Description

With ProDiag, you assign a ProDiag function block to each configured supervision. Supervisions for a ProDiag FB are, however, not enabled until the block is called. The call can be made either in the ProDiag organization block or at any other point in your program.

- If you explicitly call a ProDiag FB in your program, it is not called in the ProDiag OB.

  If you explicitly call all ProDiag FBs in your program, no ProDiag OB is created.
- If you do not want to manage calling one or more ProDiag FBs and do not call them at any point in your program, this is detected when your project is compiled. In this case, a ProDiag OB is automatically created and the ProDiag FBs are called in it.

  If you do not call any ProDiag FB of your project explicitly in your program, all ProDiag FBs are called in the ProDiag OB.

You can read out the information which ProDiag FBs are called in the ProDiag OB with the help of the cross-references.

---

**See also**

[Overview of calling the ProDiag function blocks (S7-1500)](Supervision%20of%20machinery%20and%20plants%20with%20ProDiag%20%28S7-1500%29.md#overview-of-calling-the-prodiag-function-blocks-s7-1500)

### Setting parameters of organization blocks (S7-1500)

This section contains information on the following topics:

- [Parameter assignment for time-of-day interrupt OBs (S7-1500)](#parameter-assignment-for-time-of-day-interrupt-obs-s7-1500)
- [Assigning parameters to cyclic interrupt OBs (S7-1500)](#assigning-parameters-to-cyclic-interrupt-obs-s7-1500)
- [Assigning parameters to hardware interrupt OBs (S7-1500)](#assigning-parameters-to-hardware-interrupt-obs-s7-1500)
- [Assigning parameters to isochronous mode interrupt OBs (S7-1500)](#assigning-parameters-to-isochronous-mode-interrupt-obs-s7-1500)

#### Parameter assignment for time-of-day interrupt OBs (S7-1500)

##### Procedure for setting the parameters

To set the parameters of a time-of-day interrupt OB, proceed as follows:

1. Open the "Properties" dialog belonging to the time-of-day interrupt OB in question.
2. Click the "Time-of-day interrupt" group in the area navigation.

##### Overview of the parameters that can be set

You can set the following parameters:

- Execution
- Start date and time-of-day
- Option buttons "Local time" and "System time"

##### "Execution" parameter

Use the drop-down list "Execution" to define the periods at which the time-of-day interrupt OB is to be executed. The time intervals relate to the settings for "Start date" and "Time-of-day".

The following values are possible for "Execution":

- Never
- Once
- Every minute
- Hourly
- Daily
- Weekly
- Monthly
- Yearly
- End of month

  > **Note**
  >
  > With the value "End of month", the value specified under "Start date" is irrelevant.

##### "Start date" and "Time-of-day" parameter

Here, you specify the time at which the time-of-day interrupt is to be executed for the first time.

Example: Start date = 01/05/2013, time =11:16

Depending on the value of the "Execution" parameter, the CPU generates additional time-of-day interrupts periodically. Depending on the setting, the start time relates either to the local time or to the coordinated universal timeUTC.

> **Note**
>
> If you set the "Execution" parameter to "Monthly", the start date cannot be set to the 29th, the 30th, or the 31st. If you want the time-of-day interrupt OB to start at the end of the month, you should set the parameter "Execution" to "End of month".

##### "Local time" or "System time"

Here, you decide which time the start time of the time-of-day interrupt OB relates to:

- "Local time": The start time relates to the time zone set for the CPU.
- "System time": The start time relates to the coordinated universal time UTC (Universal Time Coordinated).

---

**See also**

[Time-of-day interrupt OBs (S7-1500)](#time-of-day-interrupt-obs-s7-1500)

#### Assigning parameters to cyclic interrupt OBs (S7-1500)

##### Procedure for setting the parameters

To set the parameters of a cyclic interrupt OB, proceed as follows:

1. Open the "Properties" dialog belonging to the cyclic interrupt OB in question.
2. Click the "Cyclic interrupt" group in the area navigation.

##### Overview of the parameters that can be set in the "Cyclic interrupt" group

In the "Cyclic interrupt" group, you can set the following parameters:

- Cycle time
- Phase offset

##### "Cycle time" parameter

Use the parameter "Cycle time" to set the period of time between two calls of the cyclic interrupt OB. It is an integer multiple of 1 µs.

##### "Phase offset" parameter

Here, you set the time period by which the start times are shifted as compared to the multiple of the cycle time.

A phase offset may be advisable when you are using multiple cyclic interrupt OBs. If their cycle times have common multiples, you can use a phase offset to prevent simultaneous start times.

This will be explained below using an example:

You use two cyclic interrupt OBs: One with a cycle time of 50 ms and one with a cycle time of 100 ms. If neither of the two cyclic interrupt OBs has a phase offset, then they have the same start time every 100 ms (at these times the cycle times have common multiples). For the cyclic interrupt OB with a cycle time of 100 ms, select a phase offset of 20 ms, for example; there are no longer any common start times of the two OBs:

- OB with cycle time 50 ms starts at 50 ms, 100 ms, 150 ms, 200 ms, etc.
- OB with cycle time 100 ms starts at 120 ms, 220 ms, etc.

The start times of the OB with a cycle time of 100 ms are offset by 20 ms compared to multiples of 100 ms.

##### Priority of the cyclic interrupt OB

When you add a new cyclic interrupt OB to your project, you enter its cycle time. The priority of the cyclic interrupt OB is set in accordance with the following table.

| Cycle time | Default priority |
| --- | --- |
| 0.25 ms <= cycle time <= 2 ms | 17 |
| 2 ms < cycle time <= 5 ms | 16 |
| 5 ms < cycle time <= 10 ms | 14 |
| 10 ms < cycle time <= 100 ms | 13 |
| 100 ms < cycle time <= 200 ms | 12 |
| 200 ms < cycle time <= 500 ms | 11 |
| 500 ms < cycle time <= 1000 ms | 10 |
| 1000 ms < cycle time <= 2000 ms | 9 |
| Cycle time > 2000 ms | 8 |

You can change the default priority as follows:

1. Open the "Properties" dialog belonging to the cyclic interrupt OB in question.
2. Click the "Attributes" group in the area navigation.
3. In the "Priority" area, enter the desired value in the input field "Priority".

---

**See also**

[Cyclic interrupt OBs (S7-1500)](#cyclic-interrupt-obs-s7-1500)

#### Assigning parameters to hardware interrupt OBs (S7-1500)

##### Procedure for configuration of the start events of a hardware interrupt OB

Each start event for a hardware interrupt OB is configured in the properties of the corresponding module. To do this, follow these steps:

1. Open the "Properties" dialog related to the corresponding module.
2. In the area navigation, click the channel that is to trigger a hardware interrupt.
3. Select those check boxes whose associated events are to trigger a hardware interrupt. Enter associated limit values, if any.
4. Enter an event name, for example, "Rising edge 0".
5. Select an existing hardware interrupt OB from the drop-down list "Hardware interrupt" or create a new hardware interrupt OB.
6. If necessary, enter the priority of the hardware interrupt OB.

A system constant of the data type "Event_HwInt" is created automatically for the event identified by its unique event name. This is displayed in the standard tag table in the "System constants" tab.

##### Overview of the start events of a hardware interrupt OB

To display the currently configured start events of a hardware interrupt OB, proceed as follows:

1. Open the "Properties" dialog associated with the hardware interrupt OB in question.
2. Click the "Start events" group in the area navigation.

---

**See also**

[Hardware interrupt OBs (S7-1500)](#hardware-interrupt-obs-s7-1500)
  
[Example of a hardware interrupt event (S7-1500)](#example-of-a-hardware-interrupt-event-s7-1500)

#### Assigning parameters to isochronous mode interrupt OBs (S7-1500)

##### Procedure for setting the parameters

To set the parameters of an isochronous mode interrupt OB, proceed as follows:

1. Open the "Properties" dialog associated with the isochronous mode interrupt OB in question.
2. In the area navigation, click the "Isochronous mode" group .

##### Overview of the parameters that can be set

You can set the following parameters:

- Application cycle
- Automatic setting
- Delay time

##### "Application cycle" parameter

- For PROFINET: Integer multiple (possible values: 1, ... 14) of the send clock
- For PROFIBUS DP: DP cycle

##### Check box "Automatic setting"

- If the check box is cleared, you specify the delay time manually.
- If the check box is selected, the delay time is calculated automatically. The associated input box is then grayed out.

##### "Delay time" parameter

> **Note**
>
> You can only set the parameter "Delay time" if the check box "Automatic setting" is cleared.

The delay time is the time interval between the send clock or the global control frame and the start of the isochronous mode interrupt OB. In this period of time, the PROFINET IO controller or the DP master handles the cyclic data exchange with the IO devices or the DP slaves.

If the delay time is zero, the isochronous mode interrupt OB starts with the send cycle clock or the global control frame. In this case, it is extremely likely that access to the isochronous I/O via the extended instruction "SYNC_PI" at the start of the OB will fail as the I/O data is not yet available.

If the delay time is greater than the default value, then the OB runtime is "given away", since the clock-synchronized I/O could have been accessed earlier.

##### Overview of the displayed parameters

The following parameters are displayed:

- Distributed I/O
- Process image partition

##### "Distributed I/O"

Here, the PROFINET IO system or DP Master system containing the IO devices or DP slaves assigned to the isochronous mode interrupt OB are displayed.

The definition of a PROFINET IO system or DP master system takes place during the assignment of the process image partition to the isochronous mode interrupt OB.

##### "Process image partition"

Here, the process image partition assigned to the isochronous mode interrupt OB is displayed. This assignment has been made during hardware configuration.

---

**See also**

[Isochronous mode interrupt OBs (S7-1500)](#isochronous-mode-interrupt-obs-s7-1500)

## Useful information on CPU firmware versions and STEP 7 versions (S7-1500)

Below you will find information on the compatibility of the CPU firmware versions and their dependency on different STEP 7 versions.

It is possible to program a CPU with new firmware (e.g. firmware V1.7, which can be configured as of STEP 7 V13 SP1) with a non-current STEP 7 version (e.g. STEP 7 V12, which only recognizes the firmware V1.0). In this case, the functionality of the CPU with firmware version V1.7 is restricted to the functionality of firmware version V1.0.

The S7-1500 CPUs are downward compatible with their direct predecessors.

The S7-1500 CPUs are not compatible to comparable S7-1500T CPUs. Example: A CPU 1511 is compatible to a CPU 1511T.

Conversely, compatibility only exists if you do not use any extended Motion Control functions.

### Examples of downwards compatibility

- CPU 1516 V2.0 is compatible with all firmware versions of the CPU 1516.

  The CPU 1516 V2.0 is supplied with a new order number but is compatible without restrictions to the predecessor CPUs with the previous order number. You do not need to note anything.
- CPU 1516 V1.7 is compatible with the CPUs 1516 V1.6, V1.5, V1.1 and V1.0, but not compatible with all other S7-1500 CPUs, e.g. CPU 1518-4DPN/DP.
- CPU 1513 V1.5 is compatible with the CPUs 1513 V1.1 and V1.0, but not compatible with all other S7-1500 CPUs.
- CPU 1511 V1.0 is not compatible with all other S7-1500 CPUs.
- CPU 1518F V1.7 is compatible with CPU 1518F V1.6.

  > **Note**
  >
  > **Compatibility of F-CPUs**
  >
  > F-CPU versions are not compatible with non-F-CPUs. For example, CPU 1516F V1.6 is not compatible with CPU 1516 V1.5 and vice versa.

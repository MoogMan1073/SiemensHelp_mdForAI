---
title: "Functional description of S7-300/400 CPUs (S7-300, S7-400)"
package: ProgCPU34enUS
topics: 171
devices: [S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Functional description of S7-300/400 CPUs (S7-300, S7-400)

This section contains information on the following topics:

- [Operating modes (S7-300, S7-400)](#operating-modes-s7-300-s7-400)
- [Memory areas (S7-300, S7-400)](#memory-areas-s7-300-s7-400)
- [Access to the I/O data area (S7-300, S7-400)](#access-to-the-io-data-area-s7-300-s7-400)
- [Setting the operating behavior (S7-300, S7-400)](#setting-the-operating-behavior-s7-300-s7-400)
- [CPU information (S7-300, S7-400)](#cpu-information-s7-300-s7-400)
- [Addressing (S7-300, S7-400)](#addressing-s7-300-s7-400)
- [Organization blocks (S7-300, S7-400)](Organization%20blocks%20%28S7-300%2C%20S7-400%29.md#organization-blocks-s7-300-s7-400)
- [Events (S7-300, S7-400)](Events%20%28S7-300%2C%20S7-400%29.md#events-s7-300-s7-400)
- [Symbolic and numerical names of instructions (S7-300, S7-400)](#symbolic-and-numerical-names-of-instructions-s7-300-s7-400)

## Operating modes (S7-300, S7-400)

This section contains information on the following topics:

- [Principles of the operating modes of S7-CPUs (S7-300, S7-400)](#principles-of-the-operating-modes-of-s7-cpus-s7-300-s7-400)
- [Operating mode transitions (S7-300, S7-400)](#operating-mode-transitions-s7-300-s7-400)
- [Priority of the operating modes (S7-300, S7-400)](#priority-of-the-operating-modes-s7-300-s7-400)
- [STOP mode (S7-300, S7-400)](#stop-mode-s7-300-s7-400)
- ["STARTUP" operating mode (S7-300, S7-400)](#startup-operating-mode-s7-300-s7-400)
- [RUN mode (S7-300, S7-400)](#run-mode-s7-300-s7-400)
- [HOLD mode (S7-300, S7-400)](#hold-mode-s7-300-s7-400)
- [Basics of a memory reset (S7-300, S7-400)](#basics-of-a-memory-reset-s7-300-s7-400)

### Principles of the operating modes of S7-CPUs (S7-300, S7-400)

Operating modes describe the behavior of the CPU. You can query and evaluate the operating modes when programming the STARTUP, when testing the controller and when performing error diagnostics at any time.

S7 CPUs from the various different CPU families such as S7-300, S7-400, ET 200S, ET 200Pro or WinLC (PC-based controller) or embedded controller can have the following operating modes:

- STOP
- STARTUP
- RUN
- HOLD

The CPU can communicate via its interfaces (e.g. MPI interface) in these operating modes.

#### "STOP" operating mode

In "STOP" operating mode the CPU checks whether all configured modules and all modules used by the standard addressing are available. Provided the result is good, the CPU then sets the I/O to a pre-defined default condition. The user program is not executed when the CPU is in "STOP" operating mode.

See also: [STOP mode](#stop-mode-s7-300-s7-400)

#### "STARTUP" operating mode

A distinction is made in "STARTUP" operating mode between the "warm restart", "hot restart" and "cold restart" start-up modes.

See also: ["STARTUP" operating mode](#startup-operating-mode-s7-300-s7-400)

#### "RUN" operating mode

In "RUN" operating mode the CPU executes the user program, updates the inputs and outputs and processes interrupts and error messages.

See also: [RUN mode](#run-mode-s7-300-s7-400)

#### "HOLD" operating mode

In "HOLD" operating mode, execution of the user program is halted. The "HOLD" operating mode is used only when using the programming device for testing.

See also: [HOLD mode](#hold-mode-s7-300-s7-400)

#### Other operating modes

If the CPU is not ready for operation, it is in one of two operating modes:

- Deenergized, i.e. the supply voltage is switched off.
- Defective, i.e. a non-recoverable error has occurred.

  Check that the CPU is truly defective. To do this, set the CPU to "STOP" and switch the power switch off and on again. To analyze the error, read the diagnostics buffer when the CPU starts up. If the CPU does not start up, replace it.

### Operating mode transitions (S7-300, S7-400)

#### Overview

The following figure shows the operating modes and the operating mode transitions for the S7-300 CPUs:

![Overview](images/8642193291_DV_resource.Stream@PNG-en-US.png)

The following table shows the conditions under which the operating modes will change:

| No. | Operating mode transition | Conditions |
| --- | --- | --- |
| ① | STOP | After you turn on the power supply, the CPU is in "STOP" operating mode. It then determines the required type of startup and changes to the next operating mode. |
| ② | STOP → STARTUP | In the following cases the CPU switches to "STARTUP" operating mode:  - The CPU is set to "RUN" either by the operating mode selector or from the programming device. - After automatic triggering of a STARTUP operating mode by "POWER-ON". - The communications function "RESUME" or "START" is performed.   In the latter two cases the operating mode selector must be set to "RUN". |
| ③ | STARTUP → STOP | In the following cases the CPU switches back to STOP operating mode:  - An error is detected during the STARTUP. - The CPU is set to "STOP" either by the operating mode selector or from the programming device. - A STOP command is executed in the STARTUP OB. - The communications function "STOP" is performed. |
| ④ | STARTUP → RUN | If the STARTUP is successful, the CPU switches to "RUN". |
| ⑤ | RUN → STOP | In the following cases the CPU switches back to STOP operating mode:  - An error is detected in RUN operating mode and the associated OB is not loaded. - The CPU is set to "STOP" either by the operating mode selector or from the programming device. - A STOP command is executed in the user program. - The communications function "STOP" is performed. |

### Priority of the operating modes (S7-300, S7-400)

#### Function

If several operating mode changes are requested at the same time, the CPU switches to the operating mode with the highest priority. If, for example, the operating mode selector is set to "RUN" and an attempt is made via the programming device to switch the CPU to "STOP", the CPU will switch to "STOP", because this operating mode has the highest priority.

| Priority | Operating mode |
| --- | --- |
| Highest | [STOP](#stop-mode-s7-300-s7-400) |
|  | [HOLD](#hold-mode-s7-300-s7-400) |
|  | [STARTUP](#startup-operating-mode-s7-300-s7-400) |
| Lowest | [RUN](#run-mode-s7-300-s7-400) |

### STOP mode (S7-300, S7-400)

#### Function

In "STOP" operating mode the user program is not executed. All outputs are set to substitute values and the process being controlled is thereby brought to a safe operating mode. The CPU checks the following points:

- Hardware, for example whether are all modules are available.
- Whether the default settings for the CPU are applicable or parameter sets are present.
- Whether the general conditions for the programmed STARTUP behavior are correct.

In STOP mode you can receive global data. In addition passive one-way communications via the communications system function blocks for configured connections and via communications system functions for unconfigured connections can be performed.

---

**See also**

[Principles of the operating modes of S7-CPUs (S7-300, S7-400)](#principles-of-the-operating-modes-of-s7-cpus-s7-300-s7-400)

### "STARTUP" operating mode (S7-300, S7-400)

This section contains information on the following topics:

- [Principles of the STARTUP mode (S7-300, S7-400)](#principles-of-the-startup-mode-s7-300-s7-400)
- [Cold restart (S7-400)](#cold-restart-s7-400)
- [Warm restart (S7-300, S7-400)](#warm-restart-s7-300-s7-400)
- [Hot restart (S7-400)](#hot-restart-s7-400)
- [Retentive behavior after loss of power (S7-300, S7-400)](#retentive-behavior-after-loss-of-power-s7-300-s7-400)
- [Startup activities (S7-300, S7-400)](#startup-activities-s7-300-s7-400)
- [Cancellation of a startup (S7-300, S7-400)](#cancellation-of-a-startup-s7-300-s7-400)
- [Complete overview of the startup (S7-300, S7-400)](#complete-overview-of-the-startup-s7-300-s7-400)

#### Principles of the STARTUP mode (S7-300, S7-400)

##### Function

After the CPU has been switched on, it executes a STARTUP program before starting to execute the user program. By suitably programming the STARTUP OB, you can use the startup program to specify certain default settings for your cyclic program.

The following STARTUP operating modes are available:

- Warm restart
- Hot restart
- Cold restart

##### Special characteristics

Note the following points regarding the "STARTUP" operating mode:

- The program in the STARTUP OB will be executed. This means OB 100 for a "warm restart", OB 101 for a "hot restart", and OB 102 for a "cold restart".
- No time-based or interrupt-based program execution can be performed.
- The timers are updated.
- The runtime meter is running.
- The outputs on the modules are disabled.

---

**See also**

[Principles of the operating modes of S7-CPUs (S7-300, S7-400)](#principles-of-the-operating-modes-of-s7-cpus-s7-300-s7-400)

#### Cold restart (S7-400)

##### Cold restart

During a cold restart, all data (process image, bit memory, timers, counters and data blocks) are reset to the start values stored in the program (load memory), irrespective of whether they were configured as retentive or non-retentive.

Program execution is restarted at the beginning (startup OB or OB 1).

#### Warm restart (S7-300, S7-400)

##### Permitted warm restart

You can perform a warm restart in the following cases:

- After a memory reset.
- After loading the user program in CPU STOP operating mode.

You cannot run a warm restart if the system has requested a memory reset.

##### Manual restart (warm restart)

A manual restart ("warm restart") is triggered by:

- The operating mode selector.
- A menu command from the programming device or via a communications function, if the operating mode selector is set to RUN.

##### Automatic restart (warm restart)

An automatic restart ("warm restart") can by triggered by "POWER ON" in the following cases:

- When the "POWER OFF" occurred, the CPU was not in "STOP" operating mode.
- The operating mode selector is set to "RUN".
- The CPU was interrupted by a power failure during a warm restart. This is irrespective of the assigned STARTUP operating mode.

##### Automatic restart (warm restart) without battery backup

If your CPU is running without a backup battery, e.g. if maintenance-free operation is required, after switching on or on restoration of power after "POWER OFF" the CPU is automatically subjected to a memory reset and then a "warm restart". The user program must exist on flash EPROM (memory card) so that the user program can be copied to work memory again.

#### Hot restart (S7-400)

##### Hot restart

This start-up mode is only available with S7-400. The features of hot restart are as follows:

- When a hot restart is performed, all data and the process image retain their last valid value.
- Program execution is resumed at the breakpoint.
- The outputs do not change their status until the current cycle is completed.
- After a power supply interruption, the hot restart function is only available in backup mode.

S7-400 CPUs execute an initialization routine and then automatically a hot restart. During a hot restart, the user program is continued at the location at which the processing was interrupted. The part of the user program that was no longer processed before the power failure is referred to as remaining cycle. The remaining cycle can also contain time and interrupt controlled program parts.

As a rule a hot restart is only permissible if the user program was not modified in STOP state (for example, by reloading a modified block), or if a warm restart is not required for other reasons. It is necessary to distinguish between a manual and an automatic restart.

##### Manual hot restart

A manual hot restart is only possible if the appropriate parameters are set for the CPU and after the following STOP causes:

- The mode selector was changed from RUN to STOP
- By user programmed STOPs, STOPs after calling of OBs that are not loaded
- STOP state was caused by the programming device or by communication functions

A manual restart can be triggered via menu command from programming device or via communication functions (if the mode selector is on RUN or RUN-P). A requirement for this is that the restart is not disabled by operation (startup parameter).

- If the parameter set of the CPU's manual restart was configured

##### Automatic restart

An automatic restart was triggered by POWER ON if the CPU was not in STOP or HOLD at POWER OFF. A requirement for this is that the restart is not disabled by operation (startup parameter).

#### Retentive behavior after loss of power (S7-300, S7-400)

##### Retentive data areas after power failure

To avoid loss of data in the event of a power failure, you can specify the [retentivity](#) (Retentive data includes tags, data or blocks which are stored in the retentive memory area of a CPU and which are therefore retained even when the supply voltage is switched off.)  of bit memory, timers, counters and areas in data blocks. Providing that the STARTUP operating mode is "warm restart" (default), an "automatic restart with memory" will be performed when power is restored.

S7-300 and S7-400 CPUs react differently to power return after power failure.

S7-300 CPUs know only the "warm restart" restart mode To avoid loss of data in the event of a power failure, you can specify with STEP 7 the retentivity of bit memory, timers, counters and areas in data blocks. An "Automatic warm restart with memory" is executed when power returns.

Depending on the set parameters, S7-400 CPUs react to power return with either a warm restart (after buffered on unbuffered POWER ON) or with hot restart (only possible after buffered POWER ON).

##### Retentive behavior for CPUs with battery back-up

The following table shows the retentive behavior in the work memory of the S7-300 and S7-400 CPUs with buffering at "warm restart" and "cold restart":

| Data | Warm restart | Cold restart | Hot restart |
| --- | --- | --- | --- |
| Blocks in the load memory | X | X | X |
| DB in the work memory | X | 0 | X |
| Bit memory, timers, counters  configured as retentive | X | 0 | X |
| Bit memory, timers, counters,  configured as non-retentive | 0 | 0 | X |
| X: Data is retained 0: Data is reset or cleared (content of DBs) |  |  |  |

##### Retentive behavior for CPUs without battery back-up

No hot restart is permitted with S7-400 CPUs!

The following table shows the retentive behavior in the work memory of the S7-300 CPUs without battery backup at "warm restart" and "cold restart":

| Data | Warm restart |  | Cold restart |  |
| --- | --- | --- | --- | --- |
| S7-300 | S7-400 | S7-300 | S7-400 |  |
| Blocks in the load memory | VC | VC | VC | VC |
| DB in the work memory configured as retentive | VX | not possible | V | not possible |
| DB in the work memory configured as non-retentive | V | V | V | V |
| Bit memory, timers, counters  configured as retentive | X | 0 | 0 | 0 |
| Bit memory, timers, counters,  configured as non-retentive | 0 | 0 | 0 | 0 |
| X: Data is retained 0: Data is reset or cleared (content of DBs) V: Data is set to the default value from the EPROM VC: Code block in the EPROM is retained, any overloaded code blocks are lost VX: A data block is only retained if it is available in the load EPROM; retentive data is transferred the from NV-RAM (data blocks loaded or generated in RAM are lost) |  |  |  |  |

#### Startup activities (S7-300, S7-400)

##### Overview

The following table shows which activities the CPU performs at STARTUP:

| Activities in execution sequence | At warm restart | At cold restart | At hot restart |
| --- | --- | --- | --- |
| Clear the interrupt and block stack | X | X | 0 |
| Clear non-retentive bit memory, timers, counters | X | 0 | 0 |
| Clear all bit memory, timers, counters | 0 | X | 0 |
| Clear the process image output | X | X | Can be set |
| Reset the signal module outputs | X | X | Can be set |
| Discard the process interrupts | X | X | 0 |
| Discard the time-delay interrupts | X | X | 0 |
| Discard the diagnostics interrupts | X | X | X |
| Update the system status list (SSL) | X | X | X |
| Evaluate the module parameters and transfer them to modules or transfer default values | X | X | X |
| Execute the respective STARTUP OB | X | X | X |
| Execute the outstanding cycle (part of the user program that because of the "POWER OFF" was not executed | 0 | 0 | X |
| Update the process image input | X | X | X |
| Enable digital outputs (cancel the OD (Output Disabled) signal) after operating mode transition to RUN | X | X | X |
| X: Activity is performed 0: Activity is not performed |  |  |  |

---

**See also**

[Complete overview of the startup (S7-300, S7-400)](#complete-overview-of-the-startup-s7-300-s7-400)

#### Cancellation of a startup (S7-300, S7-400)

##### Reasons for cancellation

If errors occur during startup, the startup is canceled and the CPU switches to or remains in "STOP" operating mode. This has the following effects on the "warm restart" operating mode:

- A "warm restart" that is canceled must be repeated.
- Both a warm restart and a hot restart are possible in the event of a canceled hot restart.
- Under the following conditions a warm restart or hot restart will not be executed or will be canceled:

  - If the CPU operating mode selector is set to the "STOP" operating mode.
  - If a memory reset is requested.
  - If a memory card whose application code is not permissible is plugged in.
  - If more than one CPU is plugged in in single processor operation.
  - If the user program contains an organization block that the CPU does not recognize or has been disabled.
  - If, after the power is switched on, the CPU detects that not all modules that are listed in the configuration created with STEP 7 are actually plugged in (target-actual difference in configuration is not permitted).
  - If errors occur during the assignment of the module parameters.
- Under the following conditions, a hot restart will not be performed or will be canceled:

  - If the CPU memory was previously reset (after the memory reset, only a warm restart is permitted).
  - If the interruption limit is exceeded (the interruption time is the time that expires after leaving RUN mode until the startup OB incl. remaining cycle time was processed).
  - If the module configuration was changed (e.g. module exchange).
  - If the only warm restart configuration is permitted.
  - If blocks were loaded, deleted or changed in STOP mode.

#### Complete overview of the startup (S7-300, S7-400)

##### Sequence

The following figure shows the activities of the CPU in "STOP", "STARTUP", and "RUN" operating modes.

![Sequence](images/26365292811_DV_resource.Stream@PNG-en-US.png)

Legend for figure:

1. All peripheral outputs are switched by the peripheral modules (hardware side) to safe state (default value = "0"). This is regardless of whether it is used in the user program inside or outside the process image area.

   If signal modules with substitute value capability are used, the behavior of the outputs can be assigned, e.g. retain last value.
2. Necessary for the processing of the remaining cycle.
3. The interrupt OBs are also available during first calling of a current process image of the inputs.
4. You can use the following measures to specify the state of the local and distributed peripheral outputs in the first cycle of the user program:

   - Use configurable output modules to be able to output substitute values or to retain the last value.
   - On restart: Enable CPU startup parameter "Reset outputs on restart" in order to output a "0" (corresponds to default setting).
   - Pre-assign outputs in the startup OB (OB 100, OB 101, OB 102).
5. In S7-300 systems only the DB areas that are configured as retentive are retained.

### RUN mode (S7-300, S7-400)

#### Function

In "RUN" operating mode the cyclic, time-driven, and interrupt-driven program execution is performed:

- The process image input is read in.
- The user program is executed.
- The process image output is read out.

The active exchange of data between CPUs via global data communication (global data table), via communication instructions for configured connections and via communication instructions for non-configured connections is only possible in RUN mode.

---

**See also**

[Principles of the operating modes of S7-CPUs (S7-300, S7-400)](#principles-of-the-operating-modes-of-s7-cpus-s7-300-s7-400)

### HOLD mode (S7-300, S7-400)

#### Function

"HOLD" mode is a special case, since it is used only for tests in "STARTUP" or "RUN" operating mode.

"HOLD" mode:

- All timers are frozen. Timers and runtime meters are not processed, monitoring timers and the basic clock cycles of the time-driven levels are halted.
- The real-time clock still runs.
- Outputs are not enabled, they can however be enabled for test purposes.
- Inputs and outputs can be controlled.
- When power is restored after a power failure, CPUs with battery back-ups switch from "HOLD" to "STOP" operating mode and do not perform a "warm restart". On restoration of power, CPUs without battery back-ups automatically perform a "warm restart".
- They can receive global data. In addition passive one-way communication via the communications SFBs for configured connections and via communications SFCs for unconfigured connections can be performed.

---

**See also**

[Principles of the operating modes of S7-CPUs (S7-300, S7-400)](#principles-of-the-operating-modes-of-s7-cpus-s7-300-s7-400)

### Basics of a memory reset (S7-300, S7-400)

#### Function

A CPU memory reset can be performed in STOP mode. A memory reset can be performed manually using the mode selector (MRES) or from the programming device, e.g. before loading a user program.

A memory reset resets the CPU to the "initial condition". This means that:

- The entire user program in the work memory and in the RAM load memory and all operand areas are cleared.
- The system parameters together with the CPU and module parameters are reset to the default setting. The MPI parameters set before the memory reset remain unchanged.
- When a memory card (flash EPROM) or micro memory card is plugged in, the CPU will copy the user program from the memory card to the work memory. If the respective configuration data is also present on the memory card, the CPU and module parameters are also copied.
- The diagnostics buffer, the MPI parameters, the time of day, and the runtime meter are not reset.

## Memory areas (S7-300, S7-400)

This section contains information on the following topics:

- [What you should know about micro memory cards for S7-300 (S7-300)](#what-you-should-know-about-micro-memory-cards-for-s7-300-s7-300)
- [What you should know about memory cards for S7-400 (S7-400)](#what-you-should-know-about-memory-cards-for-s7-400-s7-400)
- [Organization of Memory Areas (S7-300, S7-400)](#organization-of-memory-areas-s7-300-s7-400)
- [Memory areas of the S7-300 (S7-300)](#memory-areas-of-the-s7-300-s7-300)
- [Memory areas of the S7-400 (S7-400)](#memory-areas-of-the-s7-400-s7-400)
- [Contents of work and system memory (S7-300, S7-400)](#contents-of-work-and-system-memory-s7-300-s7-400)

### What you should know about micro memory cards for S7-300 (S7-300)

#### How the memory card functions

The SIMATIC micro memory card is a memory module for a S7-300-CPU. You can configure the micro memory card as a load memory or as removable media.

STEP 7 V11 supports use as load memory.

To use it you have to insert the SIMATIC micro memory card in the CPU.

![How the memory card functions](images/21343062667_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Formatting the micro memory card**  If you format the micro memory card with Windows, for example with a commercially available card reader, you make the micro memory card unusable as a storage medium for an S7-CPU. |  |

#### What can be saved on a SIMATIC Micro Memory Card

You can save the user program (blocks and system data) on a micro memory card.

Alternatively, you can use the micro memory card for firmware updates or for backup of the CPU firmware.

#### Transferring objects from the project to a micro memory card

When the micro memory card is inserted in the programming device or an external prommer, you can transfer the following objects from project navigation to the micro memory card:

- Individual blocks (multiple selection possible)

  In this case a consistent transfer is available, as the dependencies of the blocks to each other is taken into account with block selection.
- PLC

  In this case, all objects relevant to processing are transferred, such as blocks and the hardware configuration on the micro memory card, just as with downloading.

To perform a transfer, you can move the objects by dragging and dropping, or use the command "Write to memory card" in the "Project" menu.

#### Transferring objects from the micro memory card to the project

You can transfer Individual blocks (multiple selection is possible) by dragging them to the project. A hardware configuration cannot be transferred from the memory card to the project.

#### Backing up firmware on the micro memory card

We recommend that your create a backup copy of the firmware for emergencies.

To do so, you must insert a blank micro memory card in the CPU and adhere to a specific sequence of steps. You will find them described in the CPU documentation.

[Documentation for S7-300](http://support.automation.siemens.com/WW/view/de/13008499/0/en)

#### Updating firmware with a micro memory card

You can get the latest firmware on the internet as *.UPD files from the Service &amp; Support pages:

[http://support.automation.siemens.com](http://support.automation.siemens.com)

Save the firmware files on the hard drive.

In order to store the files on the micro memory card, select the command "Create firmware update memory card" in the "Project" menu.

Then follow the instructions in the Service &amp; Support portal for performing a firmware update with your CPU.

---

**See also**

[Memory areas of the S7-300 CPUs (S7-300)](#memory-areas-of-the-s7-300-cpus-s7-300)

### What you should know about memory cards for S7-400 (S7-400)

#### How the memory card functions

You can insert a memory card in all S7-400 CPUs. They act as an expansion of the load memory. Depending on the type of memory card used, the user program remains saved on the memory card, even if the module has no voltage.

![How the memory card functions](images/21343446539_DV_resource.Stream@PNG-de-DE.png)

#### Types of memory cards

- RAM card: only for expanding the integrated load memory.
- FLASH card: for saving the user program, even if there is no voltage, without buffering or external to the CPU.

#### Transferring objects from the project to a memory card

When the memory card is inserted in the programming device or an external prommer, you can transfer the following objects from project navigation to the memory card:

- Individual blocks (multiple selection possible)

  In this case a consistent transfer is available, as the dependencies of the blocks to each other is taken into account with block selection.
- PLC

  In this case, all objects relevant to processing are transferred, such as blocks and the hardware configuration on the memory card, just as with downloading.

To perform a transfer, you can move the objects by dragging and dropping, or use the command "Write to memory card" in the "Project" menu, and if applicable, follow the instructions in the dialog.

#### Transferring objects from the memory card to the project

You can transfer Individual blocks (multiple selection is possible) by dragging them to the project. A hardware configuration cannot be transferred from the memory card to the project.

#### Downloading the user program to the memory card

The command "Download user program to memory card" in the menu "Online" saves the entire user program to the FLASH card. The FLASH card is in the CPU. Before the download, all existing data on the FLASH card is deleted.

- The CPU must be in STOP mode.
- You can only download to FLASH cards with these menu commands

#### Updating firmware with a memory card

You can get the latest firmware on the internet as *.UPD files from the Service &amp; Support pages:

[http://support.automation.siemens.com](http://support.automation.siemens.com)

Save the firmware files on the hard drive.

To store the file on the memory card, select the command "Create firmware update memory card" in the "Project" menu.

Then follow the instructions in the Service &amp; Support portal for performing a firmware update with your CPU.

---

**See also**

[Memory areas of the S7-400-CPUs (S7-400)](#memory-areas-of-the-s7-400-cpus-s7-400)

### Organization of Memory Areas (S7-300, S7-400)

#### Distribution

The memory of the S7 CPUs can be divided into three areas:

- Load memory (depending on the CPU and memory card type executed as RAM, EPROM or flash memory)
- Work memory (integrated RAM)
- System memory (integrated RAM)

### Memory areas of the S7-300 (S7-300)

This section contains information on the following topics:

- [Memory areas of the S7-300 CPUs (S7-300)](#memory-areas-of-the-s7-300-cpus-s7-300)
- [Retentivity of load memory, system memory, and main memory (S7-300)](#retentivity-of-load-memory-system-memory-and-main-memory-s7-300)

#### Memory areas of the S7-300 CPUs (S7-300)

##### The three memory areas of your CPU

![The three memory areas of your CPU](images/20600746123_DV_resource.Stream@PNG-en-US.png)

##### Load memory

The load memory is located on the SIMATIC Micro Memory Card. The size of the load memory corresponds exactly to the size of the SIMATIC Micro Memory Card. It is used to store code blocks, data blocks, and system data (configuration, connections, module parameters, etc.). Blocks that are identified as not relevant for execution are stored exclusively in the load memory. You can also store all the configuration data for your project on the SIMATIC Micro Memory Card.

> **Note**
>
> You must insert a SIMATIC Micro Memory Card into the CPU to enable loading of user programs and operation of the CPU.

##### System memory

The system memory is integrated in the CPU and cannot be expanded.

It contains

- The address areas for bit memories, timers, and counters
- The process images of the inputs and outputs
- Local data

##### Work memory

The work memory is integrated in the CPU and cannot be extended. It is used to execute the code and process user program data. Programs only run in the work memory and system memory.

---

**See also**

[What you should know about micro memory cards for S7-300 (S7-300)](#what-you-should-know-about-micro-memory-cards-for-s7-300-s7-300)

#### Retentivity of load memory, system memory, and main memory (S7-300)

Your CPU is equipped with a maintenance-free retentive memory, i.e. no back-up battery is required for its operation. Due to the retentivity, the content of the retentive memory is retained even during a POWER OFF and restart (warm restart).

##### Retentive data in the load memory

Your program in the load memory is always retentive: It is stored on the SIMATIC Micro Memory Card, where it is protected against power failures or memory resets

##### Retentive data in the system memory

For bit memory, timers and counters, you decide via configuration (CPU properties) which part should be retentive and which should be initialized to "0" at warm restart.

The diagnostic buffer, MPI address and transmission speed (baud rate), as well as the runtime meter, are generally stored in the retentive memory area on the CPU. Retentivity of the MPI address and transmission speed ensures that your CPU can continue to communicate, even after a power failure, memory reset or loss of communication parameters (e.g. due to removal of the SIMATIC Micro Memory Card or deletion of communication parameters).

##### Retentive data in the work memory

The contents of retentive DBs are always retentive at restart and POWER ON/OFF. Retentive data blocks can be uploaded to the work memory in accordance with the maximum limit allowed by the work memory.

Non-retentive DBs are initialized from the load memory with their initial values at restart or POWER ON/OFF. Non-retentive data blocks and code blocks can be loaded in accordance with the maximum work memory limit.

You can find the size of the CPU retentive work memory (for retentive data blocks) in the technical specifications of the respective CPU.

### Memory areas of the S7-400 (S7-400)

This section contains information on the following topics:

- [Memory areas of the S7-400-CPUs (S7-400)](#memory-areas-of-the-s7-400-cpus-s7-400)

#### Memory areas of the S7-400-CPUs (S7-400)

##### Organization of Memory Areas

The memory of the S7-400-CPU can be divided into the following areas:

![Organization of Memory Areas](images/63836024971_DV_resource.Stream@PNG-en-US.png)

##### Memory Types in S7-400 CPUs

- Load memory for the project data, e.g. blocks, configuration and parameter settings.
- Work memory for the runtime-relevant blocks (logic blocks and data blocks).
- System memory (RAM) contains the memory elements that each CPU makes available to the user program, such as bit memory, timers and counters. System memory also contains the interrupt stack
- System memory of the CPU also makes temporary memory available (local data stack, diagnostic buffer and communication resources) that is assigned to the program for the temporary data of a called block. These data is only valid as long as the block is active.

  By changing the default values for the process image, local data, diagnostic buffer and communications resources (CPU properties for which you can set parameters) you can influence the work memory available for the process-relevant blocks.

  > **Note**
  >
  > Please note the following if you expand the process image of a CPU. Reconfigure modules whose addresses have to be over the highest address of the process image so that the new addresses are still over the highest address of the expanded process image.

##### Important note for CPUs after the parameter settings for the allocation of RAM have been changed

If you change the work memory allocation by modifying parameters, this work memory is reorganized when you load system data into the CPU. The result of this is that data blocks that were created with SFC are deleted, and the remaining data blocks are assigned initial values from the load memory.

The usable size of the working memory for logic or data blocks is changed when loading the system data if you change the following parameters:

- Size of the process image (byte-oriented; in the "Cycle/Clock Memory" tab)
- Communication resources (S7-400 only; "Memory" tab)
- Size of the diagnostic buffer ("Diagnostics/Clock" tab)
- Number of local data for all priority classes ("Memory" tab)

##### Basis for Calculating the Required Working Memory

To ensure that you do not exceed the available amount of working memory on the CPU, you must take into consideration the following memory requirements when assigning parameters:

Memory requirements

| Parameters | Required working memory | In code/data memory |
| --- | --- | --- |
| Size of the process image (inputs) | 12 bytes per byte in the process image input  as of V6.0: 20 bytes per byte in the process image input | Code memory |
| Size of the process image (outputs) | 12 bytes per byte in the process image input  as of V6.0: 20 bytes per byte in the process image input | Code memory |
| Communication resources (communication jobs) | 72 bytes per communication job | Code memory |
| Size of the diagnostic buffer | 32 bytes per entry in the diagnostic buffer | Code memory |
| Quantity of local data | 1 byte per byte of local data | Data memory |

##### Flexible memory capacity

- Work memory:

  The capacity of the work memory is determined by selecting the appropriate CPU from the graded range of CPUs.
- Load memory:

  The integrated load memory is sufficient for small and medium-sized programs.

  The load memory can be increased for larger programs by inserting the RAM memory card.

  Flash memory cards are also available to ensure that programs are retained in the event of a power failure even without a backup battery. Flash memory cards (8 MB or more) are also suitable for sending and carrying out operating system updates.

##### Backup

- The backup battery provides backup power for the integrated and external part of the load memory, the data section of the working memory and the code section.

---

**See also**

[What you should know about memory cards for S7-400 (S7-400)](#what-you-should-know-about-memory-cards-for-s7-400-s7-400)

### Contents of work and system memory (S7-300, S7-400)

This section contains information on the following topics:

- [Address areas of the CPUs (S7-300, S7-400)](#address-areas-of-the-cpus-s7-300-s7-400)
- [process image input/output (S7-300, S7-400)](#process-image-inputoutput-s7-300-s7-400)
- [Local data stack (S7-300, S7-400)](#local-data-stack-s7-300-s7-400)
- [Interrupt stack (S7-300, S7-400)](#interrupt-stack-s7-300-s7-400)
- [Block stack (S7-300, S7-400)](#block-stack-s7-300-s7-400)
- [Diagnostics buffer (S7-300, S7-400)](#diagnostics-buffer-s7-300-s7-400)
- [Timers and counters (S7-300, S7-400)](#timers-and-counters-s7-300-s7-400)

#### Address areas of the CPUs (S7-300, S7-400)

##### Overview

Memory elements that each CPU makes available to the user program, such as the process image input and output, bit memory, timers and counters. The work or system memory of the S7-CPUs is divided into operand areas. Through use of appropriate operations in your user program, you address the data directly in the respective operand area.

The following table shows the operand areas:

| Operand area | Access via units of the following size: | S7 notation | Description |
| --- | --- | --- | --- |
| Process image input | Input (bit) | I | At the start of every cycle, the CPU reads the inputs from the input modules and saves the values to the process image input. |
| Input byte | IB |  |  |
| Input word | IW |  |  |
| Input double word | ID |  |  |
| Process image output | Output (bit) | Q | During its cycle, the program calculates the values for the outputs and places them in the process image output. At the end of the cycle, the CPU writes the calculated output values to the output modules. |
| Output byte | QB |  |  |
| Output word | QW |  |  |
| Output double word | QD |  |  |
| Bit memory | Bit memory (bit) | M | This area provides storage for intermediate results calculated in the program. |
| Memory byte | MB |  |  |
| Memory word | MW |  |  |
| Memory double word | MD |  |  |
| Timer | Timer (T) | T | This area provides storage for timers. |
| Counter | Counter (C) | C | This area provides storage for counters. |
| Data block | Data block, opened with "OPN DB": | DB | Data blocks store information for the program. They can either be defined so that all code blocks can access them (global DBs) or assigned to a specific FB or SFB (instance DB). |
| Data bit | DBX |  |  |
| Data byte | DBB |  |  |
| Data word | DBW |  |  |
| Data double word | DBD |  |  |
| Data block, opened with "OPN DI": | DI |  |  |
| Data bit | DIX |  |  |
| Data byte | DIB |  |  |
| Data word | DIW |  |  |
| Data double word | DID |  |  |
| Local data | Local data bit | L | This area contains the temporary local data of a block while the block is being processed. The L stack also provides memory for transferring block parameters and for saving intermediate results from LAD networks. |
| Local data byte | LB |  |  |
| Local data word | LW |  |  |
| Local data double word | LD |  |  |
| I/O area:  Inputs | Peripheral input byte | PIB | The peripheral input and output areas permit direct access to central and distributed input and output modules. |
| Peripheral input word | PIW |  |  |
| Peripheral input double word | PID |  |  |
| I/O area:  Outputs | Peripheral output byte | PQB |  |
| Peripheral output word | PQW |  |  |
| Peripheral output double word | PQD |  |  |

#### process image input/output (S7-300, S7-400)

This section contains information on the following topics:

- [Basic principles of process images (S7-300, S7-400)](#basic-principles-of-process-images-s7-300-s7-400)
- [Updating the process images (S7-300, S7-400)](#updating-the-process-images-s7-300-s7-400)

##### Basic principles of process images (S7-300, S7-400)

###### Function

When the user program addresses the input (I) and output (O) operand areas, it does not query or change the signal states on the digital signal modules. Instead, it accesses a memory area in the system memory of the CPU. This memory area is referred to as the process image.

###### Advantages of the process image

Compared with direct access to input and output modules, the main advantage of accessing the process image is that the CPU has a consistent image of the process signals for the duration of one program cycle. If a signal state on an input module changes during program execution, the signal state in the process image is retained until the process image is updated again in the next cycle. The process of repeatedly scanning an input signal within a user program ensures that consistent input information is always available.

Access to the process image also requires far less time than direct access to the signal modules since the process image is located in the internal memory of the CPU.

##### Updating the process images (S7-300, S7-400)

###### Sequence

The process image inputs/outputs (OB 1 process image) are updated in the following order:

1. The internal tasks of the operating system are performed.
2. The process image output (PIQ) table is written to the outputs of the module.
3. The status of the inputs is read into the process image input (PII) table.
4. The user program is executed with all the blocks that are called in it.

The operating system automatically controls the writing of the process image output to the outputs of the modules and the reading of the process image input.

###### I/O access error during process image updating

S7-300 CPUs respond to an error during the update of the process image as follows:

- No diagnostics buffer entry, no OB call. The respective input bytes are set to "0" and remain at "0" until the error is resolved.

S7-400 CPUs respond to an error during process image update as follows:

- Diagnostics buffer entry and start of OB 85 with every instance of I/O access each time the corresponding process image is updated. The defective input bytes are set to "0" each time the process image is accessed.

You can set the reaction to I/O access errors by selecting one of the following alternatives:

- The CPU creates a diagnostics buffer entry and starts OB 85 each time the I/O is accessed.
- The CPU creates a diagnostics buffer entry and starts OB 85 only for incoming and outgoing I/O access errors. Before OB 85 is called, the faulty input bytes are set to "0" and are no longer overwritten by the operating system until the outgoing I/O access error.
- The CPU exhibits the default behavior of the S7-300. OB 85 is not called, the corresponding input bytes are set to "0" and are no longer overwritten by the operating system until the error is resolved.

###### Frequency of OB 85 starts

In addition to the assigned reaction to I/O access errors, the address space of a module also influences how often OB 85 starts:

- For a module with an address space up to a double word, OB 85 starts once, for example, for a digital module with up to 32 inputs or outputs, or for an analog module with two channels.
- For modules with a larger address space, OB 85 starts as often as access has to be made to it with double word commands, for example, twice for an analog module with four channels.

#### Local data stack (S7-300, S7-400)

##### Function

When you create organization blocks, you can declare temporary tags (TEMP) that are only available when the block is executed and are then overwritten again. Each organization block also requires 20 bytes of local data for its start information.

The CPU has a limited amount of memory for the temporary tags of the local data of blocks currently being executed. The size of this local memory, called the local data stack or L stack, depends on the particular CPU. By default, the local data stack is divided equally among the priority classes. This means that each priority class has its own area in the local data stack. This ensures that high-priority classes and their OBs have space available for their local data.

Before the local data stack is accessed for the first time, the local data must be initialized.

The local data stack stores the following data:

- Temporary tags of the local data of blocks
- Start information of the organization blocks
- Information regarding the transfer of parameters
- Intermediate results of the logic in ladder logic programs

The following figure shows the assignment of local data to the priority classes:

![Function](images/5639994507_DV_resource.Stream@PNG-en-US.png)

In the local data stack, OB 1 is first interrupted by OB 20, which in turn is interrupted by OB 81.

| Symbol | Meaning |
| --- | --- |
|  | **Caution** |
| **All temporary tags (TEMP) of an OB and its associated blocks are stored in the local data stack. If you use a large number of nesting levels when executing your blocks, the local data stack can overflow.**  If you exceed the permissible local data stack size for a program, the S7-CPU changes to STOP operating mode.  You can get an overview of the required local data with the function "Show program information".   Don't forget the local data requirements of the synchronous error OBs. |  |

##### Assigning local data to priority classes

For S7-300: The maximum amount of local data per priority class and per block is limited for the S7-300 (see the technical data of the CPU).

For S7-400: The maximum amount of local data in total is limited (see the technical data of the CPU). You distribute the available local data freely to the various priority classes within the framework of the CPU parameter assignment. The maximum amount of local data must not be exceeded in the process.

#### Interrupt stack (S7-300, S7-400)

##### Function

If the program execution is interrupted by an organization block with higher priority, the operating system saves the following data in the interrupt stack (I stack):

- The current contents of the accumulators and address registers
- The number and size of the open data blocks

Once the new organization block has been executed, the operating system loads the information from the interrupt stack. The execution of the interrupted block then resumes at the place where it was interrupted.

#### Block stack (S7-300, S7-400)

##### Function

If processing of a block is interrupted by the call of another block or by a higher priority class, such as an interrupt or error handling, the operating system saves the following data in the block stack (B stack):

- Number, type (OB, FB, FC, SFB, SFC) and return address of the block that was interrupted.
- Numbers of the data blocks from the DB and DI registers that were open when the block was interrupted.

Using this data, the user program can be resumed after the interruption.

You can read the block stack in "STOP" mode on the programming device with the program editor open and using the test function "Call hierarchy". The block stack lists all the blocks that had not been completely executed when the CPU switched to STOP operating mode.

The following figure shows the order in which the blocks are called:

![Function](images/5640360971_DV_resource.Stream@PNG-en-US.png)

##### Data block register

Two data block registers are available. They contain the numbers of the data blocks that have been opened:

- The DB register contains the number of the opened global data block.
- The DI register contains the number of the opened instance data block.

#### Diagnostics buffer (S7-300, S7-400)

##### Function

The [diagnostics buffer](#) (The diagnostics buffer represents a backup memory in the CPU used to store a specific number of diagnostics events in the order of their occurrence.)  contains system- and user-defined diagnostics events, entered in the order in which they occur. The first entry contains the latest event. The number of entries in the diagnostics buffer depends on the respective module and its current operating mode.

Possible diagnostics events:

- Faults on a module
- Faults in the process wiring
- System errors in the CPU
- Operating mode transitions of the CPU
- Errors in the user program
- User-defined diagnostics events using system function SFC 52

The information that is entered in the diagnostics buffer when a system diagnostics event occurs is identical to the start information that is transferred to the respective organization block.

The entries in the diagnostics buffer cannot be deleted; the content of the diagnostics buffer is retained even after a memory reset.

##### Advantages of the diagnostics buffer

The diagnostics buffer offers the following advantages:

- If the CPU changes to "STOP" mode, you can evaluate the last events leading up to the STOP and thus determine the cause of the STOP.
- You can recognize the causes of errors more quickly and thus increase the availability of the system.
- You can evaluate and optimize the dynamic system response.

##### Organization of the diagnostics buffer

The diagnostics buffer is designed as a ring buffer. The maximum number of entries depends on the module; for example, the S7-300 CPU 314 can have 100 entries. When this maximum number of entries is reached, the next diagnostics buffer event causes the oldest entry to be deleted. All entries then move back on place. This means that the newest entry is always the first entry in the diagnostics buffer.

The number of entries displayed in the diagnostics buffer depends on the module and its current operating mode. With some CPUs, it is possible to assign the length of the diagnostics buffer.

##### Evaluation of the diagnostics buffer

The contents of the diagnostics buffer can be accessed as follows:

- Online via the diagnostics view
- In the user program via SFC 51 "RDSYSST".

By default, the CPU automatically sends the last diagnostics buffer entry to a monitoring device (programming device, OP, or TD) before it changes from "RUN" to "STOP" mode. This allows you to quickly find out why the operating mode changed and rectify the cause. You can change this default.

> **Note**
>
> To make the best use of the time stamp information on the diagnostics buffer entries, set the date and time of day on the module and check the settings occasionally.

#### Timers and counters (S7-300, S7-400)

##### Definition

Timers and counters are memory areas of the system memory. You specify the function of a timer or counter in the user program, for example the on-delay or the initial count value. The number of timers and counters available depends on the CPU.

> **Note**
>
> Note the following information on timers:
>
> - If you use more timers and counters in your user program than the CPU permits, a synchronous error is signaled and organization block "OB 121" is started.

## Access to the I/O data area (S7-300, S7-400)

This section contains information on the following topics:

- [I/O data area (S7-300, S7-400)](#io-data-area-s7-300-s7-400)
- [User data area (S7-300, S7-400)](#user-data-area-s7-300-s7-400)

### I/O data area (S7-300, S7-400)

This section contains information on the following topics:

- [Structure of the distributed I/O data area (S7-300, S7-400)](#structure-of-the-distributed-io-data-area-s7-300-s7-400)
- [User data (S7-300, S7-400)](#user-data-s7-300-s7-400)
- [Diagnostic and parameter data (S7-300, S7-400)](#diagnostic-and-parameter-data-s7-300-s7-400)
- [Accessing the data records of a module (S7-300, S7-400)](#accessing-the-data-records-of-a-module-s7-300-s7-400)
- [Module start address (S7-300, S7-400)](#module-start-address-s7-300-s7-400)

#### Structure of the distributed I/O data area (S7-300, S7-400)

##### I/O data area

The I/O data area can be divided into:

- User data
- Diagnostics and parameter data

Both areas have an input area with read-only access and an output area with write-only access.

#### User data (S7-300, S7-400)

##### Definition

User data can be:

- Digital and analog input and output signals from signal modules
- Control and status information from function modules
- Information for point-to-point and bus connections from communications modules

##### Access to user data

The user data in digital signal modules are addressed via the byte address of the input or output area.

For analog signal modules, the word address of the input or output area is used for addressing.

You can access user data via load and transfer commands or communications functions (operator control and monitoring) or via the process image transfer.

With load and transfer commands, it is possible to achieve a data consistency of 1, 2 and 4 bytes. Data from the process image are always consistent.

If you want to achieve data consistency of 3 or more than 4 bytes, you have to use the instruction "DPRD_DAT" (SFC 14) or "DPWR_DAT" (SFC 15).

To transfer 4 contiguous and unmodified bytes, use the instruction "Transfer double word". If you use four separate "transfer input byte" instructions, the consistency of the bytes cannot be maintained and unwanted results may occur.

---

**See also**

[DPRD_DAT: Read consistent data of a DP standard slave (S7-300, S7-400)](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#dprd_dat-read-consistent-data-of-a-dp-standard-slave-s7-300-s7-400)
  
[DPWR_DAT: Write consistent data of a DP standard slave (S7-300, S7-400)](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#dpwr_dat-write-consistent-data-of-a-dp-standard-slave-s7-300-s7-400)

#### Diagnostic and parameter data (S7-300, S7-400)

##### Data records of the diagnostics and parameter data

The diagnostics and parameter data for a module cannot be addressed individually. Rather, the data is always transferred in the form of complete data records. This means that consistent diagnostics and parameter data is always transferred.

Diagnostics and parameter data is addressed via the start address of the respective module and the data record number. Data records are divided into input and output data records. Input data records can only be read and output data records can only be written. You can access data records using system functions or communications functions.

The following table shows the assignment of data records to diagnostics and parameter data:

| Data | Description |
| --- | --- |
| Diagnostics data | For modules with diagnostics capability, you obtain the diagnostics data of the module by reading data records 0 and 1. |
| Parameter data | For modules with parameters, you transfer the parameters to the module by writing data records. |

#### Accessing the data records of a module (S7-300, S7-400)

##### Instructions for accessing data records

You can use the information in the data records to reassign parameters for modules with parameters and to read out diagnostics information for modules with diagnostics capability.

The following table shows which functions you can use to access data records:

| Instruction | Application |
| --- | --- |
| Assigning module parameters |  |
| WR_PARM | Transfers the modifiable parameters (data record 1) to the addressed signal module |
| WR_DPARM | Transfers the individual parameter data records from SDBs 100 to 129 to the addressed signal module |
| PARM_MOD | Transfers all parameters from SDBs 100 to 129 to the addressed signal module |
| WR_REC | Transfers any data record to the addressed signal module |
| Reading out diagnostics information |  |
| RD_REC | Reads out the diagnostics data |

> **Note**
>
> Data records must not be read or written by the I/O modules in the user program with instruction "WR_REC/RD_REC" or instructions "WRREC/RDREC" if a DPV1 slave is configured using a GSD file (GSD from rev. 3) and the DP interface of the DP master (S7-400 CPU) is set to "S7-compatible". In this case the DP master would address the wrong slot, i.e. the configured slot +3. To avoid this problem, change the DP master interface to "DPV1".

#### Module start address (S7-300, S7-400)

The module start address is the lowest byte address of a module. It represents the start address of the user data area in the module and is used in many cases to represent the entire module.

The module start address is entered in the start information of the appropriate organization block when, for example, process interrupts, diagnostics interrupts, insert/remove module interrupts, and power supply errors occur and thus identifies the interrupt-generating module.

##### Configuring module start addresses

The addresses used in the user program and the module start addresses are coordinated when the modules are configured.

You can change the start addresses automatically assigned when a module is inserted in the rack in the module properties ("Addresses" group).

---

**See also**

[Addressing modules](Configuring%20automation%20systems.md#addressing-modules)

### User data area (S7-300, S7-400)

This section contains information on the following topics:

- [Access to the I/O addresses (S7-300, S7-400)](#access-to-the-io-addresses-s7-300-s7-400)
- [Address areas (S7-300, S7-400)](#address-areas-s7-300-s7-400)

#### Access to the I/O addresses (S7-300, S7-400)

##### User data in the I/O operand area

The user data represent the I/O operand area. The following areas exist:

- Peripheral inputs PI
- Peripheral outputs PQ

If the user data lie in the process image, the CPU automatically undertakes the data exchange between module and process image area when updating the process images.

If the user data do not lie in the process image, you must access them from the user program by direct I/O access to the data (for example, L %IB500:P).

The addresses of analog input and analog output modules do not normally lie in the process image area. However, you can place the addresses of analog modules in this area.

---

**See also**

[Process images (input and output memory area) (S7-300, S7-400)](#process-images-input-and-output-memory-area-s7-300-s7-400)
  
[Direct access to the I/O (PI and PQ memory areas) (S7-300, S7-400)](#direct-access-to-the-io-pi-and-pq-memory-areas-s7-300-s7-400)

#### Address areas (S7-300, S7-400)

##### I/O address areas

There is a separate address area for inputs and outputs. This means that the address of an I/O area must not only include the byte or word information but also the "I" identifier for inputs and the "Q" identifier for outputs.

The following table lists the available I/O address areas:

| Operand area | Access via units of the following size: | S7 notation |
| --- | --- | --- |
| I/O area:   Inputs | Peripheral input byte   Peripheral input word   Peripheral input double word | PIB  PIW  PID |
| I/O area:   Outputs | Peripheral output byte  Peripheral output word  Peripheral output double word | PQB  PQW  PQD |

---

**See also**

[Direct access to the I/O (PI and PQ memory areas) (S7-300, S7-400)](#direct-access-to-the-io-pi-and-pq-memory-areas-s7-300-s7-400)

## Setting the operating behavior (S7-300, S7-400)

This section contains information on the following topics:

- [Introduction to tuning the operational performance (S7-300, S7-400)](#introduction-to-tuning-the-operational-performance-s7-300-s7-400)
- [Changing module parameters (S7-300, S7-400)](#changing-module-parameters-s7-300-s7-400)
- [General CPU parameters (S7-300, S7-400)](#general-cpu-parameters-s7-300-s7-400)
- [Startup (S7-300, S7-400)](#startup-s7-300-s7-400)
- [Cyclic behavior (S7-300, S7-400)](#cyclic-behavior-s7-300-s7-400)
- [Retentive behavior (S7-300, S7-400)](#retentive-behavior-s7-300-s7-400)
- [Possible settings for interrupts (S7-300, S7-400)](#possible-settings-for-interrupts-s7-300-s7-400)
- [Time-of-day functions (S7-300, S7-400)](#time-of-day-functions-s7-300-s7-400)
- [Use of clock bit memories (S7-300, S7-400)](#use-of-clock-bit-memories-s7-300-s7-400)
- [Web settings (S7-300, S7-400)](#web-settings-s7-300-s7-400)
- [Reservation of communications resources (S7-300, S7-400)](#reservation-of-communications-resources-s7-300-s7-400)
- [Test, commissioning and routing (S7-300, S7-400)](#test-commissioning-and-routing-s7-300-s7-400)
- [Activating and deactivating SNMP (S7-300, S7-400)](#activating-and-deactivating-snmp-s7-300-s7-400)
- [Settings for system diagnostics (S7-300, S7-400)](#settings-for-system-diagnostics-s7-300-s7-400)
- [Setting options for the level of protection (S7-300, S7-400)](#setting-options-for-the-level-of-protection-s7-300-s7-400)
- [Test mode and process mode (S7-300, S7-400)](#test-mode-and-process-mode-s7-300-s7-400)
- [Parameters of the compact CPU (S7-300, S7-400)](#parameters-of-the-compact-cpu-s7-300-s7-400)

### Introduction to tuning the operational performance (S7-300, S7-400)

#### Influencing the properties of automation systems

Properties of automation systems that are not preset can be influenced as follows:

- By setting the system parameters
- By using system functions (SFCs) in extended instructions

### Changing module parameters (S7-300, S7-400)

#### Default settings

In their as-delivered state, all modules with parameters have default settings suitable for standard applications. These default values allow the modules to be used immediately without making any additional settings.

You can, however, modify the behavior and the properties of the modules to suit the requirements and circumstances of your application. Modules for which you can set parameters include CPUs, FMs, CPs and some analog input and analog output modules and digital input and output modules.

#### Module parameters

Module parameters are grouped to improve clarity; for example, the following groups exist for CPUs:

- Startup
- Cycle
- PROFINET interface or other interface
- Diagnostics
- Retentive address area
- Clock memory
- Interrupts
- Protection
- Clock
- Connection resources

#### Settings and loading parameters

You can set the module parameters. When you save a device configuration with its parameters, system data is created and loaded to the CPU with the user program and then transferred to the modules during startup.

#### Assigning parameters with instructions

In addition to assigning parameters, you can also use advanced instructions in the program to modify module parameters.

The following table shows which instructions can change which module parameters:

| System function | Application |
| --- | --- |
| [WR_PARM](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#wr_parm-write-module-data-record-s7-300-s7-400) | Transfers the modifiable parameters (data record 1) to the addressed signal module. |
| [WR_DPARM](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#wr_dparm-transfer-data-record-s7-300-s7-400) | Transfers individual parameter data records from the corresponding SDBs to the addressed signal module. |
| [PARM_MOD](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#parm_mod-transfer-module-data-records-s7-300-s7-400) | Transfers all parameters from the corresponding SDBs to the addressed signal module. |
| [WR_REC](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#wr_rec-write-data-record-to-io-s7-300-s7-400) | Transfers any data record to the addressed signal module |

### General CPU parameters (S7-300, S7-400)

#### General properties of modules

The "General" parameter group specifies the type and location of the module as well as information relevant to the network, e.g. the device address, in the case of modules with interfaces.

#### Short designation, article no./ firmware, name, plant designation, location designation

The short designation, the information below it, and the article no./firmware are identical to the information in the hardware catalog.

The "Name" field contains the name of the module. You can change this as required. If you change the name, the changed name appears both in the device view and in the network view.

CPUs allow you to specify a specific plant designation. The higher-level item designation is used to identify parts of the plant uniquely according to their function. It is hierarchically structured in accordance with IEC 1346-1. You can also enter a location identifier of up to 32 characters. This is part of the item designation that identifies the exact location of, for example, a process tag or process tag group within a process (similar to a street on a city map).

The identifier entered in the "higher level item designation" or "location designation" field can be evaluated in the user program of the CPU. Use the option of entering a higher level item designation or location designation if you want to run the user program as a function of the higher level item designation of location designation.

#### Comment

Each module has a comments field. You can specify the purpose of the module in this field, for example.

### Startup (S7-300, S7-400)

This section contains information on the following topics:

- [Startup parameters (S7-300, S7-400)](#startup-parameters-s7-300-s7-400)
- [Startup parameters only for S7-400 CPUs (S7-300, S7-400)](#startup-parameters-only-for-s7-400-cpus-s7-300-s7-400)

#### Startup parameters (S7-300, S7-400)

##### Startup behavior of the CPU

The parameters that determine the startup behavior of the S7-CPU are described below.

##### Startup when expected and actual configurations do not match

The preset configuration is represented by the configuration loaded to the CPU (system data blocks). The actual configuration is the actual configuration of the automation system.

If the "Startup when expected and actual configurations do not match" check box is cleared, the CPU changes to "STOP" in the following situations:

- If one or more modules are not inserted in their configured slot.
- If a module type that differs from the configured module type is inserted, e.g. during commissioning.
- If the distributed I/O is missing.

If additional modules (central or distributed) beyond those configured are present, they are disregarded when comparing the preset and actual configurations.

If the "Startup when expected and actual configurations do not match" check box is selected, the CPU will startup even in the cases listed above.

The I/O structure (central and distributed modules, central rack and DP slaves) is not checked by the CPU. PROFIBUS-DP interface modules are an exception. Because of their close connection to the CPU, configured modules of this type must always be inserted in order for the CPU to startup.

The "Startup when expected and actual configurations do not match" option is selected by default for the CPU. This means that the CPU will startup even if the preset and actual configurations are different.

##### Monitoring time for the "ready message" from the modules

Maximum wait time for the "ready" message of all configured modules after POWER ON. If after expiration of this monitoring time any module has not sent a "ready" message to the CPU, the actual configuration is different from the preset one. The CPU reacts to this based on the setting of the "Startup when expected and actual configurations do not match" parameter.

Within this monitoring time, for example, the various power supplies for a multi-tier configuration or for devices connected to the CPU via the DP master interface can be switched on in any order.

##### Monitoring time for the transfer of parameters to the modules

Maximum wait time for parameters to be "distributed" to modules with parameters (monitoring time starts after "Ready message from modules"). For CPUs with a DP master interface, you also use this parameter to specify the power-up time monitoring for the DP slaves. In other words,within this time the DP slaves must power-up and be assigned parameters by the CPU (as DP master).

If this monitoring time expires before all of the module/DP slave parameters have been assigned, the actual configuration is different from the preset one. The CPU reacts to this based on the setting of the "Startup when expected and actual configurations do not match" parameter.

#### Startup parameters only for S7-400 CPUs (S7-300, S7-400)

This section contains information on the following topics:

- [Reset outputs at hot restart (S7-300, S7-400)](#reset-outputs-at-hot-restart-s7-300-s7-400)
- [Disable hot restart at startup by means of operator control (S7-300, S7-400)](#disable-hot-restart-at-startup-by-means-of-operator-control-s7-300-s7-400)

##### Reset outputs at hot restart (S7-300, S7-400)

###### Reset outputs at hot restart

S7-400 CPUs reset the outputs (and therefore also the process image of the outputs PIO) upon hot restart .

---

**See also**

[Hot restart (S7-400)](#hot-restart-s7-400)

##### Disable hot restart at startup by means of operator control (S7-300, S7-400)

###### Disable hot restart at startup by means of operator control (for example, programming device) or communication job (for example, from MPI stations)

You have the option of disabling "hot restart" startup mode for the S7-400 if it would otherwise be triggered by programming device operation or communication job. Hot restart can then only be executed locally.

- Select this check box if the startup mode triggered by operator control or communication job is to be limited to warm restart (=manual restart) or cold restart.
- All startup modes are possible if the check box is not selected.

###### Hot restart upon operator control or communication job (=manual hot restart) will be triggered under the following conditions:

- The "Disable hot restart ..." check box has not been selected and this parameter assignment has been transferred to the CPU
- There is nothing to prevent hot restart (battery ok, no user program change in STOP mode ...)
- Hot restart operating mode is selected in the programming device or another device triggers hot restart with a communication job.

---

**See also**

[Hot restart (S7-400)](#hot-restart-s7-400)

### Cyclic behavior (S7-300, S7-400)

This section contains information on the following topics:

- [Settings for the cycle behavior (S7-300, S7-400)](#settings-for-the-cycle-behavior-s7-300-s7-400)
- [Examples of cycle loading by communications (S7-300, S7-400)](#examples-of-cycle-loading-by-communications-s7-300-s7-400)
- [OB 85 call on a distributed I/O access error (DAE) (S7-300, S7-400)](#ob-85-call-on-a-distributed-io-access-error-dae-s7-300-s7-400)

#### Settings for the cycle behavior (S7-300, S7-400)

##### Update OB1 process image cyclically

If this option is selected, the OB1 process image is updated cyclically (default). For S7-400-CPUs the OB1 updating can be switched off with these parameters.

##### Scan cycle monitoring time

The scan cycle monitoring time is set in ms.

If the cycle time exceeds the scan cycle monitoring time, the CPU switches to "STOP" mode. You can prevent "STOP" by programming organization block OB 80.

Possible causes for exceeding the scan cycle monitoring time include:

- Communications processes
- Accumulation of interrupt events
- CPU program error

##### Control of cycle loading by communications processes

The "Cycle load due to communication" parameter allows you to restrict the time taken by communications processes, which inevitably also extend the cycle time. Examples of communications processes include:

- Transferring data to another CPU
- Loading blocks (initiated via a programming device)

Test functions performed with the programming device are hardly influenced by this parameter, they can however significantly extend the cycle time. The time available for test functions can be restricted in process operation.

**How the parameter works**

The operating system of the CPU constantly provides the configured percentage of the overall CPU processing capacity for communications (time sharing). If the allocated processing capacity is not required for communications, it is made available to other processes.

**Effect on the actual cycle time**

In the absence of additional asynchronous events, the OB 1 cycle time is extended by a factor calculated by the following formula:

![Control of cycle loading by communications processes](images/6865391243_DV_resource.Stream@PNG-en-US.png)

##### Setting the size of the process image

For CPUs with variable process image size, the size of the process image (in bytes) can be set. The process image area always starts at input or output byte 0.

For S7-300-CPUs with variable process image size, there are special characteristics that must be observed during programming when accessing the process image area. These special characteristics are described in the documentation for the CPU.

Example: The variable setting of the process image currently takes effect only when the process image is updated at the cycle control point. The PII is updated only up to the set PII size, and only the set PIQ area is output to the output modules. User program accesses to the area between the assigned process image size and maximum process image size do not trigger a synchronous access error.

---

**See also**

[Examples of cycle loading by communications (S7-300, S7-400)](#examples-of-cycle-loading-by-communications-s7-300-s7-400)

#### Examples of cycle loading by communications (S7-300, S7-400)

Below are two examples of how communications can affect the cycle loading.

##### Example of cycle load due to communications without additional asynchronous events

When you set the cycle load due to communication to 50%, the OB 1 cycle time can be doubled.

At the same time, the OB 1 cycle time is also influenced by asynchronous events (such as hardware interrupts or cyclic interrupts). From a statistical point of view, even more asynchronous events occur within the OB1 cycle because of the extension of the cycle time by the communication portion. This further extends the OB 1 cycle. This extension depends on how many events occur per OB 1 cycle and the duration of the event processing.

##### Example of cycle load due to communications with additional asynchronous events

For a pure OB 1 cycle time of 500 ms, a communications load of 50% can result in an actual cycle time of up to 1000 ms, assuming that the CPU has always enough communications jobs to process. If, parallel to this, a cyclic interrupt with 20 ms processing time is executed every 100 ms, this cyclic interrupt would extend the cycle by a total of 5*20 ms = 100 ms without communication load. That is, the actual cycle time would be 600 ms. Because a cyclic interrupt also interrupts communications, it affects the cycle time by adding 10 * 20 ms at 50% communication load. That is, in this case, the actual cycle time amounts to 1200 ms instead of 1000 ms.

> **Note**
>
> Check the effects of changing the value of the "Cycle load due to communication" parameter while the system is running.
>
> The communications load must always be taken into account when setting the minimum cycle time; otherwise, time errors will occur.

#### OB 85 call on a distributed I/O access error (DAE) (S7-300, S7-400)

##### Settings for the OB 85 call

You can change the default reaction of the CPU to I/O access errors that occur while the system updates the process image.

Recommendation: If you want to activate the OB 85 call for I/O access errors, select the "only for incoming and outgoing errors" option, so that the CPU cycle time is not extended by repeated OB 85 calls.

In their default settings, S7-300-CPUs do not call OB 85 nor do they make an entry in the diagnostics buffer in reaction to I/O access errors.

### Retentive behavior (S7-300, S7-400)

This section contains information on the following topics:

- [Retentive settings for bit memory, timers, and counters (S7-300, S7-400)](#retentive-settings-for-bit-memory-timers-and-counters-s7-300-s7-400)
- [Retention settings for data blocks (S7-300, S7-400)](#retention-settings-for-data-blocks-s7-300-s7-400)

#### Retentive settings for bit memory, timers, and counters (S7-300, S7-400)

You use the retentivity parameters to specify the memory areas that are to be retained after a power failure or after a change from "STOP" to "RUN".

##### Number of memories bytes starting at MB 0

Enter the number of retentive memory bytes starting at memory byte 0.

##### Example

If you enter "2", memory bytes MB 0 and MB 1 are retentive.

##### Number of S7 timers starting at T0

Enter the number of retentive S7 timers (T) starting at T 0.

Each S7 timer occupies 2 bytes.

##### Example

If you enter "2", S7 timers T 0 and T 1 are retentive.

##### Number of S7 counters starting at C0

Enter the number of retentive S7 counters (C) starting at C 0.

##### Example

If you enter "2", S7 counters C 0 and C 1 are retentive.

#### Retention settings for data blocks (S7-300, S7-400)

##### Function

In the retentivity properties, you can specify which memory areas of the CPU should be retained after a power failure and after a transition from "STOP" to "RUN", even without a battery backup in the backup memory of the CPU. Whether retentive areas can be configured and, if so, how many depends on the CPU.

If a backup battery is installed, data blocks are always retentive.

##### Retentive areas (relevant only for S7-300 without battery backup or micro memory card)

Retentive areas are data areas of data blocks.

If you data areas in the work memory of the CPU are to be retentive, enter the following:

- DB no.

  Numbers of the data blocks that are to be retentive.
- Byte address (start address with the length of the data bytes)

  Byte addresses of the data blocks that are to be retentive.
- Number of bytes

  Number of the retentive data bytes starting with the byte address. For example, if you enter "1", then data byte "0" is retentive.

### Possible settings for interrupts (S7-300, S7-400)

This section contains information on the following topics:

- [Settings for hardware interrupts (S7-300, S7-400)](#settings-for-hardware-interrupts-s7-300-s7-400)
- [Settings for time-delay interrupts (S7-300, S7-400)](#settings-for-time-delay-interrupts-s7-300-s7-400)
- [Settings for asynchronous error interrupts (S7-300, S7-400)](#settings-for-asynchronous-error-interrupts-s7-300-s7-400)
- [Settings for time-of-day interrupts (S7-300, S7-400)](#settings-for-time-of-day-interrupts-s7-300-s7-400)
- [Setting time interrupts (S7-300, S7-400)](#setting-time-interrupts-s7-300-s7-400)
- [Settings for the DPV1 interrupts (S7-300, S7-400)](#settings-for-the-dpv1-interrupts-s7-300-s7-400)
- [Setting the isochrone mode interrupts (S7-300, S7-400)](#setting-the-isochrone-mode-interrupts-s7-300-s7-400)

#### Settings for hardware interrupts (S7-300, S7-400)

##### Hardware interrupts

The higher the priority selected, the higher the priority will be for processing the associated hardware interrupt. Priority "0" deselects the interrupt OB. The default priority cannot be changed in S7-300 CPUs.

Process image partitions can be assigned to a hardware interrupt, provided the CPU supports process image partitions. At the start of the hardware interrupt OB, the assigned process image partition is updated so that the OB uses current process values. If the setting is "---", a process image is not assigned.

---

**See also**

[Hardware interrupt organization blocks (OB 40 to OB 47) (S7-300, S7-400)](Organization%20blocks%20%28S7-300%2C%20S7-400%29.md#hardware-interrupt-organization-blocks-ob-40-to-ob-47-s7-300-s7-400)

#### Settings for time-delay interrupts (S7-300, S7-400)

##### Time-delay interrupts

Time-delay interrupt OBs allows parts of the user program to be delayed in their execution.

The higher the priority selected, the higher the priority with which the associated time-delay interrupt will be executed. Priority "0" deselects the interrupt OB. The default priority cannot be changed in S7-300 CPUs.

Process image partitions can be assigned to a time-delay interrupt, provided the CPU supports process image partitions. At the start of the hardware interrupt OB, the assigned process image partition is updated so that the OB uses current process values. If the setting is "---", a process image is not assigned.

Time-delay interrupts are handled using the following instructions:

- SRT_DINT Start time-delay interrupt
- CAN_DINT Cancel time-delay interrupt
- QRY_DINT Query time-delay interrupt status

---

**See also**

[Time-delay interrupt organization blocks (OB 20 to OB 23) (S7-300, S7-400)](Organization%20blocks%20%28S7-300%2C%20S7-400%29.md#time-delay-interrupt-organization-blocks-ob-20-to-ob-23-s7-300-s7-400)

#### Settings for asynchronous error interrupts (S7-300, S7-400)

##### Asynchronous error interrupts

The default priority cannot be changed in S7-300 CPUs.

The priority of asynchronous error OBs can be changed so that the CPU can remains in "RUN" mode even under the following circumstances:

- Asynchronous errors accumulate, all triggering the same interrupt OB (e.g. diagnostics interrupt, call OB 82).
- In addition another asynchronous event occurs, triggering another interrupt OB (e.g. program execution error, call OB 85).
- Only one alarm should be issued (e.g. in the case of station failure, which station has failed). No process response is necessary. In this case. OB 86 can be assigned a low priority, so as not to increase the reaction time to other interrupts.

##### Example of why a priority change is necessary

Severing a string a signal cables could trigger a diagnostics interrupt (call OB 82) for every signal module that is affected ‑ which would immediately fill the start information buffer for OB 82.

So that an event that calls another asynchronous error OB (such as a program execution error, OB 85) does not cause the CPU to go the STOP mode, you should assign, for example, OB 85 a higher priority than OB 82.

---

**See also**

[Power supply error organization block (OB 81) (S7-300, S7-400)](Organization%20blocks%20%28S7-300%2C%20S7-400%29.md#power-supply-error-organization-block-ob-81-s7-300-s7-400)
  
[Diagnostic interrupt OB (OB 82) (S7-300, S7-400)](Organization%20blocks%20%28S7-300%2C%20S7-400%29.md#diagnostic-interrupt-ob-ob-82-s7-300-s7-400)
  
[Insert/remove module interrupt organization block (OB 83) (S7-300, S7-400)](Organization%20blocks%20%28S7-300%2C%20S7-400%29.md#insertremove-module-interrupt-organization-block-ob-83-s7-300-s7-400)
  
[CPU hardware fault organization block (OB 84) (S7-300, S7-400)](Organization%20blocks%20%28S7-300%2C%20S7-400%29.md#cpu-hardware-fault-organization-block-ob-84-s7-300-s7-400)
  
[Priority class error organization block (OB 85) (S7-300, S7-400)](Organization%20blocks%20%28S7-300%2C%20S7-400%29.md#priority-class-error-organization-block-ob-85-s7-300-s7-400)
  
[Rack failure organization block (OB 86) (S7-300, S7-400)](Organization%20blocks%20%28S7-300%2C%20S7-400%29.md#rack-failure-organization-block-ob-86-s7-300-s7-400)
  
[Communication error organization block (OB 87) (S7-300, S7-400)](Organization%20blocks%20%28S7-300%2C%20S7-400%29.md#communication-error-organization-block-ob-87-s7-300-s7-400)

#### Settings for time-of-day interrupts (S7-300, S7-400)

##### Priority

The priority of time-of-day interrupts determines the interrupt behavior of the interrupt OBs. For S7-300 the priority cannot at present be changed.

##### Active

Select the check box of the time-of-day interrupt OB if this OB should be started automatically when a restart occurs. You can alternatively activate the time-of-day interrupt in your user program using the OB_NR parameter in the ACT_TINT instruction.

##### Execution

Select how often the interrupts should be executed.

The intervals **every minute** to **every year** are available.

The intervals relate to the settings for start date and time of day.

> **Note**
>
> For **execution** = **end of month** the day of the start date is irrelevant (always the last day of the month).

##### Start time

Enter the date and time at which the interrupt is to be executed for the first time.

##### Example

| Start date | Time-of-day |
| --- | --- |
| 30.03.2006 | 10:15 |

Depending on the "Execution" parameter, the CPU will create further time-of-day interrupts at the specified intervals. The start time always relates to the base time of the CPU.

> **Note**
>
> If you selected "monthly" execution, the start date cannot be the 29th, 30th, or 31st, because then no time-of-day interrupt would occur in the month of February.
>
> Instead, select "End of month" execution! In this case the day of the start date is not relevant (always the last day of the month!).

##### Process image partition

A process image partition can be assigned to a time-of-day interrupt, provided the CPU supports process image partitions. At the start of the interrupt OB, the assigned process image partition is updated so that the OB uses current process values. If the setting is "---", a process image partition is not assigned.

##### Special case: the one-time start time configured is in the past

The following configuration exists:

- Execution: once
- Active: Yes
- Start date/Time-of-day: is in the past (in relation to the CPU real-time clock)

Behavior of the CPU: After a cold restart or warm restart, the corresponding time-of-day interrupt OB is **called once** by the operating system.

---

**See also**

Time-of-day interrupt organization blocks (OB 10 to OB 17)
  
[Time-of-day interrupt organization blocks (OB 10 to OB 17) (S7-300, S7-400)](Organization%20blocks%20%28S7-300%2C%20S7-400%29.md#time-of-day-interrupt-organization-blocks-ob-10-to-ob-17-s7-300-s7-400)

#### Setting time interrupts (S7-300, S7-400)

A cyclic interrupt is a periodic signal that leads to the automatic calling of a cyclic interrupt OB. The available settings are detailed below.

##### Priority

The priority determines the interrupt behavior of the interrupt OB. In the S7-300 CPUs it cannot be changed.

##### Execution

Enter the time intervals in the units shown (e.g. milliseconds) for execution of cyclic interrupt OBs.

The time cycle starts when the operating mode changes from "STOP" to "RUN".

##### Phase offset

If the phase offset is adjustable: Enter the time in milliseconds (ms) by which the actual execution time of the cyclic interrupt should be delayed.

> **Note**
>
> A phase offset is sensible if several cyclic interrupts are active. Without phase offset, cyclic interrupts would be called simultaneously and executed in succession depending on their priority.
>
> The phase offset allows the execution time of the cyclic interrupts to be distributed across the cycle.

##### Unit

Refers to the "Execution" and "Phase offset" parameters. This conversion is available only on special CPUs that support cyclic interrupt settings in microseconds.

##### Process image partition

A process image partition can be assigned to a cyclic interrupt, provided the CPU supports process image partitions. At the start of the cyclic interrupt OB, the assigned process image partition is updated so that the OB works with current process values. If the setting is "---", a process image is not assigned.

---

**See also**

[Cyclic interrupt organization blocks (OB 30 to OB 38) (S7-300, S7-400)](Organization%20blocks%20%28S7-300%2C%20S7-400%29.md#cyclic-interrupt-organization-blocks-ob-30-to-ob-38-s7-300-s7-400)

#### Settings for the DPV1 interrupts (S7-300, S7-400)

##### Interrupts for DPV1

Interrupts can be originated by a DPV1 slave to ensure that the master CPU handles the interrupt-triggering event. The interrupt data are evaluated in the CPU even in STOP mode (update of diagnostics buffer and module status). However an OB is not executed in "STOP" mode.

In addition to the normal SIMATIC interrupts (such as diagnostics interrupt for ET 200M), interrupts such as status interrupts, update interrupts, and manufacturer-specific interrupts are supported.

---

**See also**

[Status interrupt OB (OB 55) (S7-300, S7-400)](Organization%20blocks%20%28S7-300%2C%20S7-400%29.md#status-interrupt-ob-ob-55-s7-300-s7-400)
  
[Update interrupt OB (OB 56) (S7-300, S7-400)](Organization%20blocks%20%28S7-300%2C%20S7-400%29.md#update-interrupt-ob-ob-56-s7-300-s7-400)
  
[OB for manufacturer-specific alarms (OB 57) (S7-300, S7-400)](Organization%20blocks%20%28S7-300%2C%20S7-400%29.md#ob-for-manufacturer-specific-alarms-ob-57-s7-300-s7-400)

#### Setting the isochrone mode interrupts (S7-300, S7-400)

##### Properties of isochronous mode interrupts

Isochronous mode interrupt OBs are executed synchronously with the equidistant clock cycle.

##### DP master system no.

Select the DP master system whose DP slaves should be assigned to the interrupt OB. The inputs and outputs of these DP slaves can then be synchronized with the equidistant clock cycle and the user program in the interrupt OB.

##### Process image partition(s)

Enter here the numbers of the process image partitions that the interrupt OB should access. The assigned distributed I/O are updated synchronously with the equidistant clock cycle via the process image partitions.

The assigned process image partitions must be updated in the synchronous cycle interrupt OB using the instructions SYNC_PI" and "SYNC_PO". The instruction "SYNC_PI" updates the input process image partition and the instruction "SYNC_PO" the output process image partition.

If the distributed I/O addresses are assigned to different process image partitions, the numbers of the process image partitions used must be entered separated by commas (e.g. 1,2,3).

##### Delay time

The delay time is the time between the global control telegram and the start of OB 61 (or OB 62 to OB 64). During this time, the DP master performs the cyclic data exchange with the DP slaves.

If the delay time = 0 is, OB 6x starts with the global control telegram. It is in this case extremely likely that access to the isochronous I/O via "SYNC_PI" at the start of the OB will fail as the I/O data is not yet available.

If the delay time is larger than the default value, then the OB runtime is "given away", since the clock-synchronized I/O could have been accessed earlier.

---

**See also**

[Synchronous cycle interrupt OBs (OB 61 to OB 64) (S7-300, S7-400)](Organization%20blocks%20%28S7-300%2C%20S7-400%29.md#synchronous-cycle-interrupt-obs-ob-61-to-ob-64-s7-300-s7-400)
  
[Constant and isochronous modes](Configuring%20PROFIBUS%20DP.md#constant-and-isochronous-modes)

### Time-of-day functions (S7-300, S7-400)

This section contains information on the following topics:

- [Basic principles of time of day functions (S7-300, S7-400)](#basic-principles-of-time-of-day-functions-s7-300-s7-400)
- [Setting and reading the time of day (S7-300, S7-400)](#setting-and-reading-the-time-of-day-s7-300-s7-400)
- [Time synchronization SIMATIC procedure (S7-300, S7-400)](#time-synchronization-simatic-procedure-s7-300-s7-400)
- [Time-of-day synchronization in NTP mode (S7-300, S7-400)](#time-of-day-synchronization-in-ntp-mode-s7-300-s7-400)
- [Using an operating hours counter (S7-300, S7-400)](#using-an-operating-hours-counter-s7-300-s7-400)

#### Basic principles of time of day functions (S7-300, S7-400)

All S7-300/400 CPUs are equipped with either a real-time clock or a software clock. The clock can act in the automation system as both a time-of-day master and as a slave with external synchronization. This allows the use of time-of-day interrupts and run-time meters.

##### Time-of-day format

The clock always shows the time of day with a minimum resolution of 1 second and the date including the day of the week. Some CPUs also permit the display of milliseconds.

#### Setting and reading the time of day (S7-300, S7-400)

##### Setting the time of day

You can set and start the time of day and date of the CPU clock using the following instructions:

- "SET_CLK"
- "SET_CLKS" if this is available in the CPU

> **Note**
>
> To avoid time-of-day display differences in HMI systems, set the CPU to standard time or use central time-of-day synchronization.

##### Reading the time of day

You read the current date and time of day of the CPU with the instruction "READ_CLK" or via a menu command from the programming device.

#### Time synchronization SIMATIC procedure (S7-300, S7-400)

##### Reference

Parameter assignment of the interface properties in the following parameter groups:

- For the CPU: "Properties &gt; General &gt; Time"
- For the DP interface: "Properties &gt; General &gt; DP interface &gt; Time synchronization".

##### SIMATIC procedure

With the SIMATIC procedure, the time of day is set according to MMS time-of-day messages (MMS - Manufacturing Message Specification). The MMS time-of-day messages come from a SIMATIC time-of-day transmitter or a CPU that is configured as a time master.

With a CP, the time-of-day messages can either be received by the local CPU or via LAN. It is possible to set whether or not the CP forwards the received time-of-day.

Compared with an NTP method that may be available, the SIMATIC mode provides higher accuracy.

##### Clock parameters

The clock parameters allow you to make the following settings:

- Synchronization type

  You can set the synchronization properties for the CPU internally (PLC) and externally (MPI).

  If you have set the synchronization mode to "As master", you can then select the time interval for automatic synchronization.

  If more than one module with a clock is present within a network, you need to specify which CPU will act as the master and which as the slave for time synchronization purposes. There can only be one time master.
- Time interval

  The time interval defines the interval between time queries.
- Correction factor

  The correction factor is used for the CPU to correct any variation of the clock within a 24 hour period.

  You can enter positive or negative value in ms.  
  **Example:** If in 24 hours the clock has lost 4 seconds, you must enter a correction factor of "+4000 ms".

##### Instructions for synchronizing the time

To ensure that the time is consistent in all modules in the network, the time slaves are updated by the system program at regular configurable intervals. The instruction "SNC_RTCB" allows the date and time to be transferred from the time master to the time slave independently of the configured time interval.

#### Time-of-day synchronization in NTP mode (S7-300, S7-400)

##### Reference

Assigning parameters for the interface properties in the "Properties &gt; General &gt; PROFINET interface &gt; Time synchronization" parameter group. The "Enable time synchronization via NTP server" option is selected.

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

#### Using an operating hours counter  (S7-300, S7-400)

##### Definition

An run-time meter counts the operating hours of connected equipment or the total runtime of the CPU. A CPU can have up to 8 run-time meters. The numbering starts at 0.

In "STOP" mode, the run-time meter is stopped. Its count value is retained even after a memory reset. During a "warm restart", the run-time meter must be restarted by the user program.

##### Programming run-time meters

You can program the runtime meters using the following instructions:

- Use instruction "SET_RTM" to set the runtime meter to an initial value.
- Use instruction "CTRL_RTM" to start or stop the runtime meter.
- Use the instruction "READ_RTM" to read out the current number of operating hours and the status of the counter - either "stopped" or "counting".

### Use of clock bit memories (S7-300, S7-400)

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
| Period (s) | 2.0 | 1.6 | 1.0 | 0,8 | 0.5 | 0,4 | 0.2 | 0.1 |
| Frequency (Hz) | 0.5 | 0.625 | 1 | 1.25 | 2 | 2.5 | 5 | 10 |

> **Note**
>
> Clock memory runs asynchronously to the CPU cycle, i.e. the status of the clock memory can change several times during a long cycle.
>
> The selected memory byte cannot be used for intermediate storage of data.

### Web settings (S7-300, S7-400)

In this parameter group you can select:

- CPU Webserver start
- The languages in which texts are to be loaded (language-dependent texts are for example, diagnostics buffer entries and alarms).

#### Activating the Web server on this module

If the check box is selected, after the configuration data has been loaded, the Web server of the CPU is started and information can be read from the CPU via a Web browser.

Further settings relate to the update of web pages displayed. You can if required set the update time.

#### Only allow access via HTTPS

Enable this radio button for the encrypted transfer of web pages from the web server to the web browser.

> **Note**
>
> Access via HTTPS will only work if the time has been set in the CPU!

#### Selecting the languages

Select the national languages for language-dependent texts to be loaded to the CPU. The number of languages available is CPU-dependent.

#### Display and selection of CPU-specific languages

The display shows the languages which can be set for web access to the CPU. You can select a number of project languages for this "web server language" selection for a given CPU. Texts of diagnostics buffer entries and event texts are loaded into the CPU for the selected languages. For these languages, the information is also displayed on the Web browser in the corresponding language during operation.

If, during operation, you select a language in the web browser that has not yet been loaded, the diagnostics buffer entries and event texts will be shown in hexadecimal.

Note that each language requires memory space on the CPU.

#### User administration

You can define users for access to the CPU via the web browser and assign these users rights and passwords.

Rights can also be defined for the default user who does not log on to the web browser with a password ("everybody").

#### Monitoring tables

You can give users access via the web browser to the monitoring tables you define. Select the existing tables from the drop-down list and specify in the drop-down in the second column whether read-only or write access is to be possible.

#### Display classes of the messages

The selected message display classes are subsequently displayed on the CPU web pages.

You can reduce the memory occupied by the web SDBs by selecting only those display classes which are actually required.

The display class is set in the CPU properties "Message attributes" under "System diagnostics" in the inspector window.

#### User-defined web pages

The section "User-defined web pages" allows you to load your own web pages to the CPU and therefore make your own web applications available via the web browser.

---

**See also**

[Information about the web server (S7-300, S7-400, S7-1500)](Configuring%20the%20Web%20server%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#information-about-the-web-server-s7-300-s7-400-s7-1500)
  
[Creating and loading user pages (S7-300, S7-400, S7-1500)](Configuring%20the%20Web%20server%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#creating-and-loading-user-pages-s7-300-s7-400-s7-1500)

### Reservation of communications resources (S7-300, S7-400)

#### Assigning connection resources

Each communications connection requires a connection resource on the S7 CPU as a management element for the duration of the communications connection. As listed in the technical specifications, each S7 CPU has a certain number of connection resources available, which are assigned to the various communications services (programming device/OP communication, S7 communication or S7 basic communication).

#### Assignment of connection resources according to chronological order

When communications services log on, the connection resources are assigned according to the order in which they logged on.

#### Manual assignment of communications resources

In order to avoid allocation of the connection resources being dependent only on the chronological order in which various communication services are requested, connection resources can be reserved for the following services:

- Programming device communication and OP communication
- S7 basic communication

At least one connection resource is reserved by default for programming device communication and for OP communication. Smaller values are not possible.

Other communications services such as S7 communication with the extended instructions "[PUT](S7%20communication%20%28S7-300%2C%20S7-400%29.md#put-write-data-to-a-remote-cpu-s7-300-s7-400)" and "[GET](S7%20communication%20%28S7-300%2C%20S7-400%29.md#get-read-data-from-a-remote-cpu-s7-300-s7-400)" cannot occupy this connection resource, even if they establish their connection ahead of time. Instead, they are assigned other available connection resources, i.e. those that have not been specially reserved for a service.

#### Information on the maximum number and already occupied connection resources

The CPU properties display the following additional information regarding reservation of connection resources (read-only):

- Number of resources already occupied by S7 communication. These are resources such as for one-way S7 connections from another CPU to this CPU or for two-way S7 connections. These connections have already been configured in the network view.
- Maximum number of connection resources for this CPU.

### Test, commissioning and routing (S7-300, S7-400)

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

### Activating and deactivating SNMP (S7-300, S7-400)

The network management protocol SNMP (Simple Network Management Protocol) is a protocol that is used by various services and tools for performing monitoring and diagnostics of the network topology. SNMP uses the transport protocol UDP. The SNMP has two roles: the SNMP manager (client) and SNMP agent (server).

- The SNMP manager monitors the network nodes.
- The SNMP clients collect the various network-specific information in the individual network nodes and store it in a structured form in the MIB (Management Information Base). Various services and tools (as SNMP manager) can run detailed network diagnostics with the help of these data.

SNMP is also used in a PROFINET IO system for managing the network infrastructure and the IO controller and IO devices.

> **Note**
>
> If SNMP is deactivated for a device, various options for diagnostics of the network topology (for example, using the PRONETAtool) are no longer available to you.
>
> Example: For the topology comparison Online-Offline, the TIA Portal determines which ports are actually connected and uses SNMP for this function.

#### Requirement

- S7-300 CPUs with PROFINET interface
- Firmware version greater than or equal to V3.2.18
- Online and offline firmware versions of the CPU are identical.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **CPU does not start up under certain circumstances**  If you have configured an S7-300 CPU with a firmware version as of V3.2.18 and have loaded the configuration, and the real CPU firmware version is less than or equal to V3.2, the CPU will not start up. The error message in the diagnostic buffer indicates that there is a problem with the parameter assignment of the PROFINET interface.   Reason: The CPU cannot interpret the SNMP parameter data record that is generated by the TIA Portal. That is only possible as of firmware version V3.2.18.    **Solution**: Ensure that the firmware versions of the configured and the real existing CPU are identical. If required, replace the configured CPU with a CPU with firmware version 3.2 from the hardware catalog. |  |

#### Configuring SNMP

S7-300 CPUs fulfilling the above requirements make it possible for you to change the following settings for SNMP in the CPU properties:

- Activate SNMP (default: deactivated)

You can find the settings in the "SNMP" area of the CPU properties.

#### Configuring SNMP using a data record

You also have the option of reconfiguring SNMP with the 0xB071 data record.

Requirements and procedure are described in the [Product Information für S7-300](https://support.industry.siemens.com/cs/en/view/109764625).

### Settings for system diagnostics (S7-300, S7-400)

The diagnostics system is the recording, evaluation and reporting of errors within the automation system.

#### Examples of errors

- CPU program error
- Failures of modules
- Wire break for sensors and actuators

#### Report cause of STOP

Select the check box to display the reason why a CPU changed to "STOP" mode on the display device (programming device or OP).

The alarm is also entered in the diagnostics buffer.

#### Alarms triggered by acknowledgment of the ALARM extended instruction

This parameter is relevant to CPUs that are used for process control systems. When this function is enabled, the extended instructions "[ALARM](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#alarm-create-plc-alarms-with-acknowledgement-display-s7-400)", "[ALARM_8](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#alarm_8-create-plc-alarms-without-associated-values-for-eight-signals-s7-400)" and "[ALARM_8P](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#alarm_8p-create-plc-alarms-without-associated-values-for-eight-signals-s7-400)" (SFBs 33 to 35) only report a signal change again if the previous signal change (i.e., the previous incoming alarm) was acknowledged. This prevents the accumulation of alarms that cannot be processed.

### Setting options for the level of protection (S7-300, S7-400)

#### Protection level

This section explains how to use the individual protection levels of the S7 CPUs and what influence the type of S7 CPU has on the parameter assignment and use of the respective protection level.

#### Default behavior

There is no password assignment in the default protection level behavior. This level of protection means "No protection".

A password can only be given if you have selected the option "Removable with password". This option gives you write access to the CPU in RUN mode if the CPU has been write-protected with the "PROTECT" instruction in the user program.

> **Note**
>
> If the default protection level of your CPU is active and your CPU supports the instruction "[PROTECT](FBD%20%28S7-300%2C%20S7-400%29.md#protect-change-protection-level-s7-300-s7-400)", you can use this instruction to switch between the default protection level "No protection" and the protection level "Write protection".

#### Additional password-protected protection levels

A password is required for the following protection levels:

- Write protection: With this protection level, only read-only access is available without entering the correct password, regardless of the keyswitch setting. To enable this protection level a password is required.
- Write/read protection: With this protection level, neither read nor write access is available without entering the correct password, regardless of the keyswitch setting. A password must be assigned before this protection level can be selected.

Write and read access is possible if the password is known regardless of the level of protection set.

#### Behavior of a password-protected module during operation

The CPU protection takes effect after the settings are downloaded in the CPU.

Before an online function is executed, the necessary permission is checked and, if necessary, the user is prompted to enter a password.

Example: The module was assigned a protection level and you want to execute the "Modify tags" function. This requires write access; therefore, the assigned password must be entered to execute the function.

The functions protected by a password can only be executed by one programming device/PC at any one time. Another programming device/PC cannot log on with a password.

Access authorization to the protected data is in effect for the duration of the online connection, or until the access authorization is manually rescinded with "Online &gt; Delete access rights".

> **Note**
>
> You can not restrict functions for process control, monitoring, and communications. Thus, for example, the "Set time of day/date" function cannot be locked with a password.

### Test mode and process mode (S7-300, S7-400)

#### Introduction

For some CPU models you can set the mode for the program test.

In process operation, test functions such as program status or monitor/modify tags are restricted so that the set permissible cycle time extension is not exceeded. Testing using breakpoints and step-by-step program execution cannot be performed.

In test operation, all test functions via a programming device/PC – even if they increase the cycle time significantly – can be used.

#### Possible settings for operating behavior

You can set the following modes for testing with the program status in the inspector window under "Properties &gt; Mode":

- Test mode

  All test functions can be used without restrictions. The CPU cycle time can be extended considerably since, for example, the status of instructions in programmed loops is checked each time they are run through.
- Process mode

  The program status test function is restricted to ensure that the cycle time load is kept as low as possible:

  - For example, no call conditions are permitted.
  - The status display of a programmed loop is stopped at the return point.
  - The "HOLD" and step-by-step program execution test functions cannot be used.

> **Note**
>
> If the CPU is in test operation you must ensure that the CPU and the process can handle significant cycle time increases.

The "process operation" option allows you to prevent changes to the call environment being made in the program editor.

### Parameters of the compact CPU (S7-300, S7-400)

This section contains information on the following topics:

- [Counting function (S7-300, S7-400)](#counting-function-s7-300-s7-400)
- [Positioning function (S7-300, S7-400)](#positioning-function-s7-300-s7-400)
- [Point-to-point connection function (S7-300, S7-400)](#point-to-point-connection-function-s7-300-s7-400)

#### Counting function (S7-300, S7-400)

This section contains information on the following topics:

- [Properties of Counting (S7-300, S7-400)](#properties-of-counting-s7-300-s7-400)
- [Interrupt selection (S7-300, S7-400)](#interrupt-selection-s7-300-s7-400)
- [Channel-specific parameters (S7-300, S7-400)](#channel-specific-parameters-s7-300-s7-400)
- [Count (S7-300, S7-400)](#count-s7-300-s7-400)
- [Frequency measurement (S7-300, S7-400)](#frequency-measurement-s7-300-s7-400)
- [Pulse-width modulation (S7-300, S7-400)](#pulse-width-modulation-s7-300-s7-400)
- [Continuous Counting (S7-300, S7-400)](#continuous-counting-s7-300-s7-400)
- [Count once (S7-300, S7-400)](#count-once-s7-300-s7-400)
- [Count periodically (S7-300, S7-400)](#count-periodically-s7-300-s7-400)
- [Main counting direction (S7-300, S7-400)](#main-counting-direction-s7-300-s7-400)
- [Gate Function (S7-300, S7-400)](#gate-function-s7-300-s7-400)

##### Properties of Counting (S7-300, S7-400)

###### Description

If you select the CPU with integrated count and measurement function in the network view or the device view, you can configure the counting function for each of the channels listed in the inspector window under "Properties &gt; General &gt; Count".

If you decide to use channel 0 or channel 1 as the counting channel you can no longer use "Positioning" technology.

> **Note**
>
> The number of channels you can utilize as counting channels depends on the type of CPU you are using.

In the "Operating Mode" selection box, you can determine how you want the CPU to count for each channel. There are various options for this. Default is "not configured".

---

**See also**

[Documentation on technological functions of the CPU](http://support.automation.siemens.com/WW/view/de/12429336/0/en)

##### Interrupt selection (S7-300, S7-400)

You can select several interrupts for the "Counting" function.

###### Requirement

- The CPU is selected.
- Interrupt selection is located at "Properties &gt; General &gt; Counting &gt; Interrupt selection".

###### Interrupt selection (basic parameters)

In the "Select interrupt" drop-down list, select which interrupts the CPU should trigger. You have the following options:

- None
- Diagnostics
- Process
- Diagnostics and hardware

Default selection is "None".

Select the events you want to use for hardware interrupt triggering, dependent on the set operating mode.

###### Counting

Events that can trigger a hardware interrupt:

- HW gate opening (with opened SW gate)
- HW gate closing (with opened SW gate)
- On reaching (activating) the comparator
- On a counting pulse
- Overflow (when the high count limit is exceeded)
- Underflow (when the low count limit is fallen below)

###### Frequency measurement

Events that can trigger a hardware interrupt:

- HW gate opening (with opened SW gate)
- HW gate closing (with opened SW gate)
- End of measurement
- High limit violated
- Low limit violated

###### Pulse-width modulation

Events that can trigger a hardware interrupt:

- HW gate opening (with opened SW gate)

---

**See also**

[Count (S7-300, S7-400)](#count-s7-300-s7-400)
  
[Frequency measurement (S7-300, S7-400)](#frequency-measurement-s7-300-s7-400)
  
[Pulse-width modulation (S7-300, S7-400)](#pulse-width-modulation-s7-300-s7-400)

##### Channel-specific parameters (S7-300, S7-400)

###### General

All channel-specific parameters are set under "Properties &gt; General &gt; Counting &gt; Channel 0 (... Channel n)". There are six options available for this operating mode: "Not configured", "Count continuously", "Count once", "Count periodically", "Measure frequency" and "Pulse-width modulation".

"Not configured" is set as the default.

##### Count (S7-300, S7-400)

This section contains information on the following topics:

- [Operating parameters for counting (S7-300, S7-400)](#operating-parameters-for-counting-s7-300-s7-400)
- [Input 0 (count) (S7-300, S7-400)](#input-0-count-s7-300-s7-400)
- [Output (count) (S7-300, S7-400)](#output-count-s7-300-s7-400)
- [Max. frequency (S7-300, S7-400)](#max-frequency-s7-300-s7-400)
- [Hardware interrupt at (count) (S7-300, S7-400)](#hardware-interrupt-at-count-s7-300-s7-400)
- [Assigning input data (S7-300, S7-400)](#assigning-input-data-s7-300-s7-400)

###### Operating parameters for counting (S7-300, S7-400)

###### Main counting direction

In "Count once" and "Count periodically" modes, you can specify from the "Main count direction" drop-down list whether or not you want the counter to have a main count direction and, if so, whether the main count direction is up or down. Default selection is "None".

The "Main counting direction" drop-down list is not shown in the "Count continuously" operating mode.

###### Gate Function

In the "Gate function" drop-down list, you can select whether the count operation is to be canceled or interrupted when the gate is closed.

Here, if you select "Cancel count", the count is resumed with the load value after the gate is closed and opened again. Here, if you select "Stop count", the count is resumed with the last actual counter value after the gate is closed and opened again.

Default selection is "Cancel count".

###### Initial value / End value

In the Initial value / End value input field, enter a value for the respective counting limit, dependent on which main count direction you have selected in the respective drop-down list.

The main count direction and this entry are related as follows:

- If the main count direction is up, enter an end value here.
- If the main count direction is down, enter an initial value here.

This input field is not shown if you have not selected a main count direction.

The default setting always has the value "2147483647" (only visible if you have selected a main counting direction).

###### Compare Value

In the "Comparison value" input field, enter a value that is assigned to the digital output, to the comparator status bit STS_CMP and to a hardware interrupt. The count value is compared with the comparison value. Dependent on the result of this comparison, the output and the comparator status bit STS_CMP can be set and the hardware interrupt for "Reached comparison value" can be generated.

In the output group, customize how the output is actually set dependent on the counter value.

Default comparison value is "0".

###### Hysteresis

In the input field "Hysteresis" enter a hysteresis range of 0 to 255 (0 and 1 means: hysteresis is switched off).

An encoder might stop at a certain position and then "swing" up / down in this position. As a result, the counter value fluctuates around a certain value. Thus, the associated output would be switched on / off, dictated by the rhythm of those fluctuations if, for example, a comparison value lies within this fluctuation range. In order to prevent a switching action as a result of small fluctuations, the CPU offers a configurable hysteresis.

You can modify this hysteresis in a current operation via the user program.

The hysteresis influences the output and the comparator status bits STS_CMP, the overflow STS_OFLW, underflow STS_UFLW and the zero crossing STS_ZP.

Default is "0".

###### Time base

You can specify whether the period is to be measured in units of 125 ns or 1 μs at a maximum counting frequency of 1 kHz. If the maximum counting frequency is greater than 1 kHz, the period is not measured. You can measure the period of the counting signal up to a maximum counting frequency of 1 kHz.

At a maximum counting frequency of 1 kHz, the time between two consecutive counting edges is always measured.

With a time base of 1 μs, periods of up to 4294 s (71 min, 34 s) can be measured and with a time base of 125 ns, periods of up to 178 ms (2 min, 58 s) can be measured.

If the counting edges are further apart in time, the measured period is incorrect because a overflow has not been taken into account.

---

**See also**

[Count once (S7-300, S7-400)](#count-once-s7-300-s7-400)
  
[Continuous Counting (S7-300, S7-400)](#continuous-counting-s7-300-s7-400)
  
[Count periodically (S7-300, S7-400)](#count-periodically-s7-300-s7-400)
  
[Main counting direction (S7-300, S7-400)](#main-counting-direction-s7-300-s7-400)

###### Input 0 (count) (S7-300, S7-400)

###### Signal evaluation

In the "Signal evaluation" drop-down list, select which signals the connected encoder is to deliver. You can choose from the following options:

- Pulse and direction
- Rotary encoder single
- Rotary encoder double
- Rotary encoder quadruple

The default setting is "Pulse and direction".

###### HW gate

The "HW gate" check box allows you to select whether or not a hardware gate is to be used.

This check box is not selected by default.

###### Count Direction Inverted

The "Count direction inverted" check box allows you to select whether or not the count direction is to be inverted.

This check box is not selected by default.

---

**See also**

[Gate Function (S7-300, S7-400)](#gate-function-s7-300-s7-400)

###### Output (count) (S7-300, S7-400)

###### Output function course

The "Output function course" drop-down list offers you the following alternative options:

- No comparison

  The output will be switched in the same way as a normal output.

  The SFB input parameters CTRL_DO and SET_DO are not active.

  The status bit STS_DO and STS_CMP (status comparator in the IDB) remain reset.
- Set when count ≥ comparison value

  The output is set when the counter value reaches the compare value. It stays set as long as the counter value is greater than / equal to the compare value.
- Set when count ≤ comparison value

  The output is set when the counter value reaches the compare value. It stays set as long as the counter value is less than / equal to the compare value.
- Pulse when comparison value is reached

  You can specify a pulse period for the adaptation to the actuators you are using. The output is set for the specified pulse period when the counter value reaches the compare value. The output is only set when it reaches the compare value of the main counting direction, if you have configured a main counting direction.

Default is "No comparison".

###### Pulse Period

If you have selected the "Pulse when comparison value is reached" alternative in the "Output function course" drop-down list, you must enter the pulse period for the output signal in ms in the "Pulse period" input field. The maximum length is 510 ms. You can only enter even values.

The pulse period starts when the respective digital output is set. The pulse period inaccuracy is lower than 2 ms.

The output stays set until the compare conditions do not apply anymore if you have entered a 0-ms pulse period.

Default is "0 ms".

> **Note**
>
> The bit STS_CMP "Comparator Status" is set together with the output when the compare value is reached.

###### Max. frequency (S7-300, S7-400)

###### Counting signals / HW gate

In this drop-down list you can set the maximum counting frequency for the track A / pulse, track B / direction and hardware gate signals in fixed intervals. The maximum value depends on the CPU in use:

| CPU | Range of values | Default selection |
| --- | --- | --- |
| CPU 312C | 10, 5, 2, 1 kHz | 10 kHz |
| CPU 313C CPU 313C-2 DP CPU 313C-2 PtP | 30, 10, 5, 2, 1 kHz | 30 kHz |
| CPU 314C-2 DP CPU 314C-2 PN/DP CPU 314C-2 PtP | 60, 30, 10, 5, 2, 1 kHz | 60 kHz |

If your CPU does not support this function, the drop-down list in unavailable and grayed out.

###### Latch

In this drop-down list you can set the maximum counting frequency for the latch signal in fixed intervals. The maximum value depends on the CPU in use:

| CPU | Range of values | Default selection |
| --- | --- | --- |
| CPU 312C | 10, 5, 2, 1 kHz | 10 kHz |
| CPU 313C CPU 313C-2 DP CPU 313C-2 PtP | 30, 10, 5, 2, 1 kHz | 10 kHz |
| CPU 314C-2 DP CPU 314C-2 PN/DP CPU 314C-2 PtP | 60, 30, 10, 5, 2, 1 kHz | 10 kHz |

If your CPU does not support this function, the drop-down list in unavailable and grayed out.

###### Hardware interrupt at (count) (S7-300, S7-400)

###### Description

The corresponding event triggers a hardware interrupt when you select the respective button. The following events can trigger a hardware interrupt:

- HW gate opening (with opened SW gate)
- HW gate closing (with opened SW gate)
- On reaching (activating) the comparator
- On a counting pulse
- Overflow (when the high count limit is exceeded)
- Underflow (when the low count limit is fallen below)

You must enable this in the Basic Parameters tab to ensure that the CPU generates a hardware interrupt.

No option is selected by default.

Triggering a hardware interrupt on each counting edge results in high CPU utilization at higher counting frequencies. If the hardware interrupts in the "Counting" submodule occur faster than they can be processed in the hardware interrupt OB (OB 40), this produces the diagnostic "Hardware interrupt lost), provided the diagnostic interrupt is enabled.

###### Assigning input data (S7-300, S7-400)

###### Assigning input data

You can select whether the count value or the period can be read at a maximum counting frequency of 1 kHz in the input data (I data) of the "Counting" submodule. If the maximum counting frequency is greater than 1 kHz, only "Count value" is possible.

You can measure the period of the counting signal up to a maximum counting frequency of 1 kHz.

At a maximum counting frequency of 1 kHz, the time between two consecutive counting edges is always measured. If the maximum counting frequency is greater than 1 kHz, the period is not measured and the value is 0.

##### Frequency measurement (S7-300, S7-400)

This section contains information on the following topics:

- [Measure Frequency (S7-300, S7-400)](#measure-frequency-s7-300-s7-400)
- [Operating parameters for frequency measurement (S7-300, S7-400)](#operating-parameters-for-frequency-measurement-s7-300-s7-400)
- [Input 0 (frequency measurement) (S7-300, S7-400)](#input-0-frequency-measurement-s7-300-s7-400)
- [Output (frequency measurement) (S7-300, S7-400)](#output-frequency-measurement-s7-300-s7-400)
- [Hardware interrupt at (frequency measurement) (S7-300, S7-400)](#hardware-interrupt-at-frequency-measurement-s7-300-s7-400)

###### Measure Frequency (S7-300, S7-400)

###### Description

In this operating mode the CPU counts the pulses it receives with default time intervals (integration time) and calculates the frequency via the number of pulses and integration time.

The calculated frequency value is supplied in "mHz" units.

###### Operating parameters for frequency measurement (S7-300, S7-400)

###### Description

In this operating mode the CPU counts the pulses it receives within a configured integration time.

The measurement is carried out within this integration time. The measured value is updated when the integration time has expired.

If at least one rising edge does not occur during the integration time, a value of 0 or the averaged value is returned as the measured value, depending on the parameter assignment.

###### Integration time

In the "Integration time" input field, enter an integration time between 10 ms and 10000 ms.

Default is "100 ms".

###### Low limit and high limit

In the "Low limit" and "High limit" input fields, enter the values that the determined frequency is compared with, respectively, after the integration time has expired. The following are permissible ranges for limit value monitoring, dependent on the type of CPU:

- Low limit

  - CPU 312C: 0 to 9 999 999 mHz
  - CPU 313C: 0 to 29 999 999 mHz
  - CPU 314C: 0 to 59 999 999 mHz
- High limit

  - CPU 312C: 1 mHz to 10 000 000 mHz
  - CPU 313C: 1 mHz to 30 000 000 mHz
  - CPU 314C: 1 mHz to 60 000 000 mHz

    > **Note**
    >
    > At the time of input it is verified whether the high limit &gt; low limit.

Default for the low limits is 0 mHz respectively. CPU-dependent default high limits are:

- CPU 312C: 10 000 000 mHz
- CPU 313C: 30 000 000 mHz
- CPU 314C: 60 000 000 mHz

###### Max. counting frequency / HW gate

In this drop-down list you can set the maximum counting frequency for the track A / pulse, track B / direction and hardware gate signals in fixed intervals. The maximum value depends on the CPU in use:

| CPU | Range of values | Default selection |
| --- | --- | --- |
| CPU 312C | 10, 5, 2, 1 kHz | 10 kHz |
| CPU 313C CPU 313C-2 DP CPU 313C-2 PtP | 30, 10, 5, 2, 1 kHz | 30 kHz |
| CPU 314C-2 DP CPU 314C-2 PN/DP CPU 314C-2 PtP | 60, 30, 10, 5, 2, 1 kHz | 60 kHz |

###### Output measured value

You can select whether the measured value is to be output directly or as an averaged value. To do this, select the "Directly" or "Averaged" option in the "Output measured value" drop-down list.

The measured frequency is displayed at the end of an integration time within which at least one positive edge has occurred.

If at least one positive edge does not occur during the assigned integration time:

- for direct frequency value, "0" is returned at the end of the integration time.
- for averaged frequency value, the last value is exported to subsequent measurement intervals without positive edge (f ≥ 1 mHz). This operation represents an extension of the integration time. Here, the last measured value is divided by the number of measurement intervals without positive edge.

  Example: If the last measured value was 12 000 mHz, the value 4000 mHz is output after three measurement intervals.

  ![Output measured value](images/20722008971_DV_resource.Stream@PNG-de-DE.png)

  | Symbol | Meaning |
  | --- | --- |
  | ① | Time interval |
  | ② | Frequency averaged |
  | ③ | Frequency direct |
  | ④ | Pulses |

The "Direct" option is selected as the default in the drop-down list.

###### Input 0 (frequency measurement) (S7-300, S7-400)

###### Signal evaluation

In the "Count direction inverted" drop-down list, select which signals the connected encoder is to supply. You can choose from the following options:

- Pulse and direction
- Rotary encoder single

The default setting is "Pulse and direction".

###### HW gate

The "HW gate" check box allows you to select whether or not a hardware gate is to be used.

This check box is not selected by default.

###### Count Direction Inverted

The "Count direction inverted" check box allows you to select whether or not the count direction is to be inverted.

This check box is not selected by default.

---

**See also**

[Gate Function (S7-300, S7-400)](#gate-function-s7-300-s7-400)

###### Output (frequency measurement) (S7-300, S7-400)

###### Output function course

The "Output function course" drop-down list offers you the following alternative options:

- No comparison

  The output will be switched in the same way as a normal output.

  The SFB input parameters MAN_DO and SET_DO are not active.

  The status bit STS_DO remains reset.
- Set when outside the limits

  The output is set when the measured frequency is higher than the upper limit or lower than the lower limit.
- Set when lower limit is violated

  The output is set when the measured frequency drops below the lower limit.
- Set when upper limit is violated

  The output is set when the measured frequency exceeds the upper limit.

Default is "No comparison".

###### Hardware interrupt at (frequency measurement) (S7-300, S7-400)

###### Description

The corresponding event triggers a hardware interrupt when you select the respective check box. The following events can trigger a hardware interrupt:

- HW gate opening (with opened SW gate)
- HW gate closing (with opened SW gate)
- End of measurement
- High limit exceeded
- Low limit violated

You must enable this in the Basic Parameters tab to ensure that the CPU generates a hardware interrupt.

No option is selected by default.

##### Pulse-width modulation (S7-300, S7-400)

This section contains information on the following topics:

- [Pulse-Width Modulation (S7-300, S7-400)](#pulse-width-modulation-s7-300-s7-400-1)
- [Operating parameters for pulse width modulation (S7-300, S7-400)](#operating-parameters-for-pulse-width-modulation-s7-300-s7-400)
- [Input 0 (pulse-width modulation) (S7-300, S7-400)](#input-0-pulse-width-modulation-s7-300-s7-400)
- [Filter frequency (S7-300, S7-400)](#filter-frequency-s7-300-s7-400)
- [Hardware interrupt at (pulse-width modulation) (S7-300, S7-400)](#hardware-interrupt-at-pulse-width-modulation-s7-300-s7-400)

###### Pulse-Width Modulation (S7-300, S7-400)

###### Description

The output value you have specified is converted by the CPU into a pulse sequence of the respective pulse/pulse ratio (pulse-width modulation).

This pulse sequence is output on digital output DO (output sequence) after the parameterized on-delay has expired.

###### Operating parameters for pulse width modulation (S7-300, S7-400)

###### Output format

In the"Output format" drop-down list, select the value range of the output value by selecting the "ppm" or "S7 analog value" option.

If your output value lies between 0 and 1,000 check the "ppm" option.

If your output value is a SIMATIC S7 analog value (between 0 and 27,648), check the "S7 analog value" option.

The "ppm" button is selected by default.

###### Time base

In the "Time base" drop-down list, select the time base valid for the resolution, value range of the period, minimum pulse width and for the on-delay.

If you select the "1 ms" option, you can set times with a resolution of 1 ms.

Select "0.1 ms" option to configure times with a resolution of 0.1 ms.

The "0.1 ms" option is selected by default.

###### On delay

In the "On delay" input field, enter a value for the delay time between the start of an output sequence and the output of the pulse.

Enter a value as in the resolution configured above.

If you select the "1 ms" option in the "Time base" drop-down list, you can set times from 0 ms to 65535 ms with a resolution of 1 ms.

If you select the "0.1 ms" option in the "Time base" drop-down list, you can set times from 0 ms to 6553.5 ms with a resolution of 0.1 ms.

Default is "0".

This pulse sequence is output on digital output DO (output sequence) after the on-delay has expired.

![On delay](images/20722229643_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | On delay |
| ② | Pulse Period |
| ③ | Period |
| ④ | Output DO |

Default setting is "0".

###### Period

The pulse / pause period defines the length of the output sequence.

In the "Period" input field, enter a value as in the resolution configuration above.

If you select the "1 ms" option in the "Time base" drop-down list, you can set times from 1 ms to 65535 ms at a resolution of 1 ms.

If you select the "0.1 ms" option in the "Time base" drop-down list, you can set times from 0.4 ms to 6553.5 ms with a resolution of 0.1 ms.

Default setting is "20000".

###### Minimum pulse time

You can set a minimum pulse time for the attenuation of short output pulses/pauses. This suppresses all pulses or pauses shorter than the minimum pulse time.

In the "Minimum pulse time" input field, enter a value as in the resolution configuration above.

If you select the "1 ms" option in the "Time base" drop-down list, enter period values from 0 to /2.

If you select the "0.1 ms" option in the "Time base" drop-down list, enter period values from 2 to /2.

The minimum pulse width is internally set to 0.2 ms if you have selected 1 ms for the time base and a minimum pulse time of 0.

Default setting is "2".

###### Input 0 (pulse-width modulation) (S7-300, S7-400)

###### HW gate

The "HW gate" check box allows you to select whether or not a hardware gate is to be used.

This check box is not selected by default.

Start of pulse-width modulation with a hardware gate is only possible if you first open the software gate and then generate a positive edge on digital input "hardware gate".

Pulse width modulation can only be stopped with a negative edge at the software gate. The hardware gate status has no effect.

###### Filter frequency (S7-300, S7-400)

###### HW gate

This drop-down list is only available if the "HW gate" option is selected under "Input". Here you can set the maximum frequency of the hardware gate signal in fixed intervals. The maximum value depends on the CPU in use:

| CPU | Range of values | Default selection |
| --- | --- | --- |
| CPU 312C | 10, 5, 2, 1 kHz | 10 kHz |
| CPU 313C CPU 313C-2 DP CPU 313C-2 PtP | 30, 10, 5, 2, 1 kHz | 30 kHz |
| CPU 314C-2 DP CPU 314C-2 PN/DP CPU 314C-2 PtP | 60, 30, 10, 5, 2, 1 kHz | 60 kHz |

###### Hardware interrupt at (pulse-width modulation) (S7-300, S7-400)

###### Description

The corresponding event triggers a hardware interrupt when you select the respective check box. The following events can trigger a hardware interrupt:

- HW gate opening (with opened SW gate)

You must enable this in the Basic Parameters tab to ensure that the CPU generates a hardware interrupt.

No option is selected by default.

##### Continuous Counting (S7-300, S7-400)

###### Description

The "Count continuously" operating mode is defined as follows:

After the counter reaches its upper limit it jumps to the lowest counting limit at the next count pulse and resumes the count from there.

After the counter reaches its lower limit it jumps to the upper counting limit at the next count pulse and resumes the count from there.

Those counting limits are set fixed to the maximum counting range.

In this operating mode, counting is started and stopped via the gate function.

##### Count once (S7-300, S7-400)

###### Description

When the counter reaches the end value 1, in the up-counting main counting direction mode, the counter jumps to the counter range start at the next pulse and stops, even if there are additional count pulses coming in.

When the counter reaches the end value 1, in the down-counting main counting direction mode, the counter jumps to the counter range start at the next pulse and stops, even if there are additional count pulses coming in.

The counting limits are set to the maximum counting range if there is no master counting direction configuration.

In this operating mode, counting is started and stopped via the gate function.

When the gate opens, the counter can receive counting impulses and the count starts. When the gate is closed, the counter can no longer receive count pulses and the count stops.

##### Count periodically (S7-300, S7-400)

###### Description

If the main count direction of the counter is up and the counter has reached the end value - 1, the arrival of an additional count pulse causes the counter to jump to the load value from where it continues counting.

If the main count direction of the counter is down and the counter has reached the count value = 1, the arrival of an additional count pulse causes the counter to jump to the start value (load value) from where it continues counting.

The count limits are set to the maximum counting range if a main count direction is not configured.

In this operating mode, counting is started and stopped via the gate function.

When the gate opens, the counter can receive count pulses and the count starts. When the gate is closed, the counter can no longer receive count pulses and the count stops.

##### Main counting direction (S7-300, S7-400)

###### Description

In your parameters you can declare "up" or "down". This determines the counting limit for the start value or end value for the operating modes Single Counting and Periodic Counting.

For main counting direction "up", the counter starts at "0" or at the load value and counts up to the limit value you have declared in your parameters.

For the main count direction "down", the counter starts at the start value you have declared in your parameters and then counts down to "0".

Even though you may have declared "down" counts in your parameters for the main counting direction, you must still set a respective direction signal for reverse counting or you must declare "Invert direction of count" in your parameters.

##### Gate Function (S7-300, S7-400)

###### Software gate and Hardware gate

The CPU has two logical AND linked gates:

A **software gate** (SW gate), controlled via the user program.

The software gate can only be opened on a 0-1 edge transition of the input parameters SW_GATE on the SFB. A reset of this parameter closes the gate.

A **hardware gate** (HW gate), controlled via the digital input "Hardware gate". In the "Count" tab you can specify whether or not you want to use the hardware gate. This gate opens at a 0-1 transition and closes at a 1-0 transition on the digital input.

#### Positioning function (S7-300, S7-400)

This section contains information on the following topics:

- [Interrupt selection (S7-300, S7-400)](#interrupt-selection-s7-300-s7-400-1)
- [Operating mode (S7-300, S7-400)](#operating-mode-s7-300-s7-400)
- [Positioning with analog output (S7-300, S7-400)](#positioning-with-analog-output-s7-300-s7-400)
- [Positioning with digital outputs (S7-300, S7-400)](#positioning-with-digital-outputs-s7-300-s7-400)

##### Interrupt selection (S7-300, S7-400)

You can select interrupts for the "Positioning" function.

###### Requirement

- The CPU is selected.
- Interrupt selection is located at "Properties &gt; General &gt; Positioning &gt; Interrupt selection".

###### Interrupt selection

In the "Interrupt Selection" drop-down list, select whether or not the CPU should trigger diagnostic interrupts. You have the following options:

- None
- Diagnostics

Default selection is "None".

You must carry out supplementary configurations to ensure that the corresponding events are really going to trigger diagnostic interrupts.

Enable the required monitoring under "Properties &gt; Positioning &gt; Channel 0" with operating mode "Positioning with analog output" selected:

- Under "Drive"

  Actual value, target approach and target range can be monitored.
- Under "Axis"

  For a linear axis, you can specify here whether or not to monitor the working range. The traversing range is always monitored.
- Under "Encoder"

  For encoders with zero mark, it is verified whether the encoder always supplies the same number of pulses between two consecutive zero marks.

Select which events are to trigger a diagnostic interrupt under "Channel 0 - Diagnostics".

For a diagnostic interrupt, you must configure the parameters in the following settings:

- Interrupt selection under "Properties &gt; General &gt; Positioning &gt; Channel 0"
- The corresponding monitoring in the appropriate "Drive", "Axis" or "Encoder" section.
- The respective enable signal in the "Diagnostics" section.

##### Operating mode (S7-300, S7-400)

###### Operating mode

Use the "Operating mode" parameter to determine how you want to position. You have the following options:

- Analog outputs: Positioning with analog output
- Digital outputs: Positioning with digital outputs

Default selection is "not configured".

The operating mode is selected under "Properties &gt; General &gt; Positioning &gt; Channel 0".

> **Note**
>
> You cannot configure the "Positioning" circuit if you have configured channel 0 or 1 for the counting circuit.
>
> You can only assign an analog output to positioning if you have disabled output 0 in section AI5/AO2.
>
> I/O channels configured for positioning can no longer be addressed by the user program.

---

**See also**

[Documentation on technological functions of the CPU](http://support.automation.siemens.com/WW/view/de/12429336/0/en)

##### Positioning with analog output (S7-300, S7-400)

This section contains information on the following topics:

- [Drive (S7-300, S7-400)](#drive-s7-300-s7-400)
- [Axis (S7-300, S7-400)](#axis-s7-300-s7-400)
- [Encoder (S7-300, S7-400)](#encoder-s7-300-s7-400)
- [Diagnostics (S7-300, S7-400)](#diagnostics-s7-300-s7-400)

###### Drive (S7-300, S7-400)

This section contains information on the following topics:

- [Controlling the drive and control mode (S7-300, S7-400)](#controlling-the-drive-and-control-mode-s7-300-s7-400)
- [Max. frequency (S7-300, S7-400)](#max-frequency-s7-300-s7-400-1)
- [Target approach (analog) (S7-300, S7-400)](#target-approach-analog-s7-300-s7-400)
- [Enable power section (S7-300, S7-400)](#enable-power-section-s7-300-s7-400)
- [Monitoring (analog) (S7-300, S7-400)](#monitoring-analog-s7-300-s7-400)

###### Controlling the drive and control mode (S7-300, S7-400)

###### Controlling the drive and control mode

In "Properties &gt; Position &gt; Channel 0" in the "Channel 0 - Drive" section, specify the parameters for the drive and axis for positioning using an analog output.

###### Drive description

The drive is controlled via two fixed assigned analog outputs, with either a voltage of ±10 V (Pin 16) or a current of ±20 mA (Pin 17).

> **Note**
>
> You can only assign an analog output to positioning if you have disabled output 0 in section AI5/AO2 of the area navigation.

###### Description of control mode

In the drop-down list you have the option of 2 steer modes. The control mode describes how your connected power unit is controlled.

- Voltage ±10 V or current ±20 mA:

A positive voltage or current is generated when traveling in the plus direction (forward). A negative voltage or current is generated when traveling in the minus direction (back).

- Voltage 0 to 10 V or current from 0 to 20 mA and direction signal:

A positive voltage or current is generated when traveling in the plus direction (forwards) and the CONV_DIR digital output is switched off.

A positive voltage or current is generated when traveling in the minus direction (back) and the CONV_DIR digital output is switched on.

The default setting is "±10".

###### Max. frequency (S7-300, S7-400)

###### Position feedback

In this drop-down list you can set the maximum counting frequency for the position feedback signals (encoder signals A, B, N) in fixed levels.

If your CPU does not support this function, the drop-down list in unavailable and grayed out.

Default setting here is "60 kHz".

###### Accompanying signals

In this drop-down list you can set the maximum counting frequency for the length measurement and reference point switch signals in fixed levels.

If your CPU does not support this function, the drop-down list in unavailable and grayed out.

Default setting here is "10 kHz".

###### Target approach (analog) (S7-300, S7-400)

###### Target range

In the "Target range" input field, enter an even-numbered value between 0 and 2 x 10 pulses. An odd value is rounded off internally. The target range lies symmetrically around the target. Here, if you enter the value 0, the target must be reached with the accuracy of a pulse. The target range monitoring is switched off and the relevant check box in the "Monitoring" area is unavailable.

Default is "50" pulses.

###### Monitoring time

In the "Monitoring time" input field, enter a time between 0 and 100000 ms. The CPU rounds this value to a 4 ms execution cycle.

The CPU uses the monitoring time to monitor the actual value and the target approach.

If you enter the value 0, the actual value monitoring and target approach monitoring are switched off and the relevant check boxes in the "Monitoring" area are then unavailable.

Default selection is "2000 ms".

###### Maximum speed

In the "Maximum speed" input field, enter a value between 10 and 1 000 000 pulses/s. This corresponds to a level of 10 V or 20 mA at the analog output.

Default is "1000 pulses/s".

###### Creep speed / reference speed

In the "Creep-/referencing speed" input field, enter a value between 10 pulses/s and the assigned maximum speed.

The drive is decelerated to creep speed after it reaches the braking point.

In the reference point approach mode, the drive is decelerated to reference speed when it reaches the reference point switch.

Default is "100" pulses/s.

###### Enable power section (S7-300, S7-400)

###### Off delay

In the "Off delay" input field, enter a time in milliseconds. The CPU rounds this value to a 4 ms execution cycle. Output CONV_EN is reset after a delay of this amount of time when a run is canceled (power section enable is removed).

If you actuate a brake via the digital output, the delay time ensures that the axis, at the time the output is reset, is slow enough for the brake to handle the kinetic energy.

Default is "1000 ms".

###### Monitoring (analog) (S7-300, S7-400)

###### Description

Here you can switch process value, target approach and target range monitoring on and off.

###### Target range

Once you have selected the "Target range" button to monitor whether the drive remains in the approached target position or drifts off after it has reached this target position.

You cannot switch on target range monitoring if you have customized a 0 ms monitoring time for "Target approach".

An external error message is returned when the monitoring unit is triggered. You must acknowledge this external error with ERR_A. Monitoring is switched off. Monitoring is not switched on until a new run starts.

This monitoring function is disabled by default.

###### Target approach

Once you have selected the "Target approach" button, it is monitored whether the axis has approached the target range within the monitoring time after it has reached the switch-off point.

You cannot switch on process value monitoring if you have customized a 0 ms monitoring time for "Target approach".

This monitoring function is disabled by default.

###### Process value

Axis movement is monitored for the run start to the switch-off point if you have selected the "Process value" button. The run is interrupted if the axis does not move by at least one pulse into the specified direction within the monitoring time.

You cannot switch on process value monitoring if you have customized a 0 ms monitoring time for "Target approach".

The CPU does not recognize the failure of a digital input. Process value monitoring lets you detect missing encoder signals. This error can have the following causes:

- Digital input failure
- Wire break
- Defective encoder
- Faulty power section

This monitoring feature is switched on by default.

###### Axis (S7-300, S7-400)

This section contains information on the following topics:

- [Axis type (analog) (S7-300, S7-400)](#axis-type-analog-s7-300-s7-400)
- [Length measurement (analog) (S7-300, S7-400)](#length-measurement-analog-s7-300-s7-400)
- [Reference point (analog) (S7-300, S7-400)](#reference-point-analog-s7-300-s7-400)
- [Axis monitoring (analog) (S7-300, S7-400)](#axis-monitoring-analog-s7-300-s7-400)
- [Linear axis (S7-300, S7-400)](#linear-axis-s7-300-s7-400)
- [Rotary axis (S7-300, S7-400)](#rotary-axis-s7-300-s7-400)

###### Axis type (analog) (S7-300, S7-400)

###### Description

Specify the parameters for the axis under "Properties &gt; Positioning &gt; Channel 0" in the "Channel 0 - Axis " section.

###### Axis type

In "Axis type" select whether to control a linear axis or a rotary axis.

Default selection is "Linear axis".

###### Start and end of software limit switch

The working area of a linear axis is between the start of the software limit switch and the end of the software limit switch. The software limit switches belong to the working area. Enter values between -5 x 10<sup>8</sup> and +5 x 10<sup>8</sup> pulses in the relevant boxes. The start of the software limit switch must always be less than the end of the software limit switch.

The software limit switches are monitored, provided the axis is synchronized and working range monitoring is enabled.

Default is "-100000000 pulses" for the start of the software limit switch and "100000000 pulses" for the end of the software limit switch.

###### End of rotary axis

In the "End of rotary axis" box, enter a value between 1 and 10<sup>9</sup> pulses.

The "End of rotary axis" value is the theoretically largest value that the actual value can reach. Physically, it has the same position as the start of the rotary axis (0).

Default is "100000" pulses.

---

**See also**

[Linear axis (S7-300, S7-400)](#linear-axis-s7-300-s7-400)
  
[Rotary axis (S7-300, S7-400)](#rotary-axis-s7-300-s7-400)

###### Length measurement (analog) (S7-300, S7-400)

###### Description

The "Length measurement" function allows you to measure a distance during a run operation. The start and end of the length measurement are edge-triggered via the digital input "Length measurement". Select the type of edge in the "Detection" drop-down list.

You have the following options:

- Off
- Start/end on rising edge

  A rising edge on the digital input starts the length measurement, the next rising edge ends it.
- Start/end on falling edge

  A falling edge on the digital input starts the length measurement, the next falling edge ends it.
- Start on rising edge, end on falling edge

  A rising edge on the digital input starts the length measurement, the next falling edge ends it.
- Start with falling edge, end with rising edge

  A falling edge on the digital input starts the length measurement, the next rising edge ends it.

Default is "off".

###### Reference point (analog) (S7-300, S7-400)

###### Coordinate

After the CPU performs a STOP-RUN transition, the axis is set to the value of the reference point coordinate while the axis has not yet synchronized.

After a reference point run the value of the reference point coordinate is assigned to the reference point.

For a linear axis, the value of the reference point coordinate must lie within the working range (including the start / end of the software limit switches).

For a rotary axis, the value of the reference point coordinate must lie within the range from 0 to "End of rotary axis - 1".

Default is "0" pulses.

###### Reference Point Location for Reference Point Switch

In the "Reference point location for reference point switch" drop-down list, select whether the reference point lies in the plus direction (increasing actual values) or minus direction (decreasing actual values) relative to the reference point switch.

Default is "in plus direction".

###### Axis monitoring (analog) (S7-300, S7-400)

###### Working range

For a linear axis, you can specify here whether or not to monitor the working range. If you select the "Working range" button, a check is made to determine whether the actual position value is out of range of the software limit switches. Monitoring is only active on a synchronized axis.

The coordinates of the software limit switches as such belong to the working range.

If monitoring is triggered the run is aborted.

This monitoring function is enabled by default.

###### Traversing Range

You use traversing range monitoring to check whether the value is outside the permitted traversing range of - 5 x 10<sup>8</sup> to + 5 x 10<sup>8</sup>. The traversing range is always monitored. The monitoring cannot be disabled (always enabled in the "Monitoring" parameter).

If monitoring is triggered the run is aborted.

###### Linear axis (S7-300, S7-400)

###### Description

The **linear axis** is an axis whose physical traversing range is restricted.

The working area on the linear axis is limited by the software limit switches.

![Description](images/20690361355_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Physical start |
| ② | Physical end |

###### Rotary axis (S7-300, S7-400)

###### Description

The **rotary axis** is an axis the traversing range of which is not restricted by mechanical stops.

![Description](images/20690761227_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Largest display value = end of rotary axis - 1 |
| ② | Start of rotary axis (coordinate 0) = end of rotary axis |

A rotary movement of the rotary axis starts at the coordinate "Zero" and ends at the coordinate "End of rotary axis". Physically, the "zero" coordinate is identical with "End of rotary axis" (= 0). The actual position value is toggled at this point. The display of the actual position is always positive.

###### Encoder (S7-300, S7-400)

###### Increments per encoder revolution

In the "Increments per encoder revolution" input field, enter the number of increments your encoder should output per 360 degrees. You can find this value in the encoder description.

The CPU evaluates the increments 4 times, in other words, an increment corresponds to four pulses.

Default setting is "1000" increments.

###### Count direction

In "Count direction", adapt the direction of the position feedback to the axis motion direction.

In the "count direction" drop-down list, select the "Normal" option if rising count pulses correspond to increasing actual position values.

In the "count direction" drop-down list, select the "Inverted" option if rising count pulses correspond to decreasing actual position values.

You should consider all the directions of rotation of the transmission elements, such as clutches and gears.

The "Normal" option is selected by default.

###### Monitoring

In "Monitoring" you can determine whether the encoder is to be monitored for missing pulses. This is only possible for encoders where the value of "Increments per encoder revolution" is divisible by 10 or 16.

If you select the "Missing pulse" check box, a check is performed to determine whether the encoder always supplies the same number of pulses between two consecutive zero marks.

If you use an encoder without zero mark, you must disable the monitoring for missing pulses.

This monitoring function is disabled by default.

###### Diagnostics (S7-300, S7-400)

###### Description

In "Properties &gt; Position &gt; Channel 0" in section "Channel 0 - Diagnostics", select the events for which the diagnostics interrupt is to be generated. No check box is selected by default.

###### Missing pulse

If you select the "Missing pulse" check box, a diagnostic interrupt is generated as soon as the encoder does not supply the same number of pulses between two consecutive zero marks. You must enable the corresponding monitoring function in the "Channel 0 - Encoder" section.

###### Traversing range

If you select the "Traversing range" check box, a diagnostic interrupt is generated immediately when the axis exits the traversing range. The corresponding monitoring function is always enabled.

###### Working range

If you select the "Working range" check box, a diagnostic interrupt is generated if the actual position value is out of range of the software limit switches. You must enable the corresponding monitoring function in the "Channel 0 - Axis" section.

You cannot use this diagnostic interrupt for positioning on a rotary axis. The respective options box is grayed out.

###### Actual value

If you selected the "Actual value" check box, a diagnostic interrupt is generated if during a traversing motion, the axis does not move by at least one pulse in the specified direction within the monitoring time. The run is cancelled.

The actual value is monitored from the start of travel until the switch-off point is reached.

You must enable the corresponding monitoring function in the "Channel 0 - Drive" section.

The CPU does not recognize the failure of a digital input. Enabling the actual value monitoring allows you to detect missing encoder signals.

This check box is selected by default.

###### Target approach

If you select the "Target approach" check box, a diagnostic interrupt is generated if the axis does not reach the target range within the monitoring time after it has reached the switch-off point.

You must enable the corresponding monitoring function in the "Channel 0 - Drive" section.

###### Target range

If you selected the "Target range" check box, a diagnostic interrupt is generated if the drive does not stop on an approached target position after the target range is reached or if the drive drifts away from the approached target position.

You must enable the corresponding monitoring function in the "Channel 0 - Drive" section.

##### Positioning with digital outputs (S7-300, S7-400)

This section contains information on the following topics:

- [Drive (S7-300, S7-400)](#drive-s7-300-s7-400-1)
- [Axis (S7-300, S7-400)](#axis-s7-300-s7-400-1)
- [Encoder (S7-300, S7-400)](#encoder-s7-300-s7-400-1)
- [Diagnostics (S7-300, S7-400)](#diagnostics-s7-300-s7-400-1)

###### Drive (S7-300, S7-400)

This section contains information on the following topics:

- [Controlling the drive (S7-300, S7-400)](#controlling-the-drive-s7-300-s7-400)
- [Max. frequency (S7-300, S7-400)](#max-frequency-s7-300-s7-400-2)
- [Target approach (digital) (S7-300, S7-400)](#target-approach-digital-s7-300-s7-400)
- [Monitoring (digital) (S7-300, S7-400)](#monitoring-digital-s7-300-s7-400)

###### Controlling the drive (S7-300, S7-400)

In "Properties &gt; Position &gt; Channel 0" in the "Channel 0 - Drive" section, specify the parameters for the drive and axis for positioning with digital inputs.

###### Description

The drive is controlled via four permanently allocated 24 V digital outputs.

In the drop-down list you have the option of 4 steer modes. The control mode describes how the 4 digital outputs (DO+1.0 to DO+1.3) control the power section.

Below lists the individual output functions under the various control modes:

| Output | Control mode 1 | Control mode 2 | Control mode 3 | Control mode 4 |
| --- | --- | --- | --- | --- |
| DO + 1.0 | Rapid traverse | Rapid / creep traverse | Rapid traverse | Rapid traverse plus |
| DO + 1.1 | Creep traverse | Position reached | Creep traverse | Creep traverse plus |
| DO + 1.2 | Drive plus | Drive plus | Drive plus | Rapid traverse minus |
| DO + 1.3 | Drive minus | Drive minus | Drive minus | Creep traverse minus |

###### Max. frequency (S7-300, S7-400)

###### Position feedback

In this drop-down list you can set the maximum counting frequency for the position feedback signals (encoder signals A, B, N) in fixed levels.

If your CPU does not support this function, the drop-down list in unavailable and grayed out.

Default setting here is "60 kHz".

###### Accompanying signals

In this drop-down list you can set the maximum counting frequency for the length measurement and reference point switch signals in fixed levels.

If your CPU does not support this function, the drop-down list in unavailable and grayed out.

Default setting here is "10 kHz".

###### Target approach (digital) (S7-300, S7-400)

###### Target range

Enter an even-numbered value between 0 and 2 x 10 <sup>8</sup> pulses in the "Target range" input field. An odd value is rounded off internally. The target range lies symmetrically around the target. Here, if you enter the value 0, the target must be reached with the accuracy of a pulse. In this case, the target range monitoring is switched off and the relevant check box in the "Monitoring" area is unavailable.

Default is "50" pulses.

###### Monitoring time

Enter a time between 0 and 100000 ms in the "Monitoring time" input field. The CPU rounds this value to a 4 ms execution cycle.

The CPU uses the monitoring time to monitor the actual value and the target approach.

If you enter the value 0, the actual value monitoring and target approach monitoring are switched off and the relevant check boxes in the "Monitoring" area are then unavailable.

The default setting is "2000 ms".

###### Monitoring (digital) (S7-300, S7-400)

###### Description

Here you can switch actual value, target approach and target range monitoring on and off.

###### Target approach

If you select the "Target approach" check box, the axis is monitored to determine whether it reaches the target range within the monitoring time after the switch-off point is reached.

You cannot switch on actual value and target approach monitoring if you have set a 0 ms monitoring time for "Target approach". The respective fields are grayed out.

This monitoring function is disabled by default.

###### Target range

If you select "Target range" check box, the drive is monitored to determine whether it stops on an approached target position after the target range is reached or if the drive drifts away from the target range.

An external error is returned when the monitoring is triggered. You must acknowledge this external error with ERR_A. Monitoring is switched off. Monitoring is not switched on again until a new run starts.

This monitoring function is disabled by default.

###### Actual value

If you select the "Axis value" check box, the axis movement is monitored from the start of the run up until the switch-off point is reached. The run is canceled if the axis does not move by at least one pulse into the specified direction within the monitoring time.

You cannot switch on actual value and target approach monitoring if you have set a 0 ms monitoring time for "Target approach". The respective fields are grayed out.

The CPU does not recognize the failure of a digital input. Actual value monitoring lets you detect missing encoder signals. This error can have the following causes:

- Digital input failure
- Wire break
- Defective encoder
- Faulty power section

This monitoring function is enabled by default.

###### Axis (S7-300, S7-400)

This section contains information on the following topics:

- [Axis type (digital) (S7-300, S7-400)](#axis-type-digital-s7-300-s7-400)
- [Length measurement (digital) (S7-300, S7-400)](#length-measurement-digital-s7-300-s7-400)
- [Reference point (digital) (S7-300, S7-400)](#reference-point-digital-s7-300-s7-400)
- [Axis monitoring (digital) (S7-300, S7-400)](#axis-monitoring-digital-s7-300-s7-400)
- [Linear axis (S7-300, S7-400)](#linear-axis-s7-300-s7-400-1)
- [Rotary axis (S7-300, S7-400)](#rotary-axis-s7-300-s7-400-1)

###### Axis type (digital) (S7-300, S7-400)

###### Description

In "Axis type" select whether to control a linear axis or a rotary axis.

Default selection is "Linear axis".

###### Start and end of software limit switch

The working area of a linear axis is between the start of the software limit switch and the end of the software limit switch. The software limit switches belong to the working area. Enter values between -5 x 10<sup>8</sup> and +5 x 10<sup>8</sup> pulses in the relevant boxes. The start of the software limit switch must always be less than the end of the software limit switch.

The software limit switches are monitored, provided the axis is synchronized and working range monitoring is enabled.

Default is "-100000000 pulses" for the start of the software limit switch and "100000000 pulses" for the end of the software limit switch.

###### End of rotary axis

In the "End of rotary axis" box, enter a value between 1 and 10<sup>9</sup> pulses.

The "End of rotary axis" value is the theoretically largest value that the actual value can reach. Physically, it has the same position as the start of the rotary axis (0).

Default is "100000" pulses.

---

**See also**

[Linear axis (S7-300, S7-400)](#linear-axis-s7-300-s7-400-1)
  
[Rotary axis (S7-300, S7-400)](#rotary-axis-s7-300-s7-400-1)

###### Length measurement (digital) (S7-300, S7-400)

###### Description

The "Length measurement" function allows you to measure a distance during a run operation. The start and end of the length measurement are edge-triggered via the digital input "Length measurement". Select the type of edge in the "Detection" drop-down list.

You have the following options:

- Off
- Start/end on rising edge

  A rising edge on the digital input starts the length measurement, the next rising edge ends it.
- Start/end on falling edge

  A falling edge on the digital input starts the length measurement, the next falling edge ends it.
- Start on rising edge, end on falling edge

  A rising edge on the digital input starts the length measurement, the next falling edge ends it.
- Start with falling edge, end with rising edge

  A falling edge on the digital input starts the length measurement, the next rising edge ends it.

Default is "off".

###### Reference point (digital) (S7-300, S7-400)

###### Coordinate

After the CPU performs a STOP-RUN transition, the axis is set to the value of the reference point coordinate while the axis has not yet synchronized.

After a reference point run the value of the reference point coordinate is assigned to the reference point.

For a linear axis, the value of the reference point coordinate must lie within the working range (including the start / end of the software limit switches).

For a rotary axis, the value of the reference point coordinate must lie within the range from 0 to "End of rotary axis - 1".

Default is "0" pulses.

###### Reference Point Location for Reference Point Switch

In the "Reference point location for reference point switch" drop-down list, select whether the reference point lies in the plus direction (increasing actual values) or minus direction (decreasing actual values) relative to the reference point switch.

Default is "in plus direction".

###### Axis monitoring (digital) (S7-300, S7-400)

###### Working range

For a linear axis, you can specify here whether or not to monitor the working range. If you select the "Working range" button, a check is made to determine whether the actual position value is out of range of the software limit switches. Monitoring is only active on a synchronized axis.

The coordinates of the software limit switches as such belong to the working range.

If monitoring is triggered the run is aborted.

This monitoring function is enabled by default.

###### Traversing range

You use traversing range monitoring to check whether the value is outside the permitted traversing range of - 5 x 10<sup>8</sup> to + 5 x 10<sup>8</sup>. The traversing range is always monitored. The monitoring cannot be disabled (always enabled in the "Monitoring" parameter).

If monitoring is triggered the run is aborted.

###### Linear axis (S7-300, S7-400)

###### Description

The **linear axis** is an axis whose physical traversing range is restricted.

The working area on the linear axis is limited by the software limit switches.

![Description](images/20690361355_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Physical start |
| ② | Physical end |

###### Rotary axis (S7-300, S7-400)

###### Description

The **rotary axis** is an axis the traversing range of which is not restricted by mechanical stops.

![Description](images/20690761227_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Largest display value = end of rotary axis - 1 |
| ② | Start of rotary axis (coordinate 0) = end of rotary axis |

A rotary movement of the rotary axis starts at the coordinate "Zero" and ends at the coordinate "End of rotary axis". Physically, the "zero" coordinate is identical with "End of rotary axis" (= 0). The actual position value is toggled at this point. The display of the actual position is always positive.

###### Encoder (S7-300, S7-400)

###### Increments per encoder revolution

In the "Increments per encoder revolution" input field, enter the number of increments your encoder should output per 360 degrees. You can find this value in the encoder description.

The CPU evaluates the increments 4 times, in other words, an increment corresponds to four pulses.

Default setting is "1000" increments.

###### Count direction

In "Count direction", adapt the direction of the position feedback to the axis motion direction.

In the "count direction" drop-down list, select the "Normal" option if rising count pulses correspond to increasing actual position values.

In the "count direction" drop-down list, select the "Inverted" option if rising count pulses correspond to decreasing actual position values.

You should consider all the directions of rotation of the transmission elements, such as clutches and gears.

The "Normal" option is selected by default.

###### Monitoring

In "Monitoring" you can determine whether the encoder is to be monitored for missing pulses. This is only possible for encoders where the value of "Increments per encoder revolution" is divisible by 10 or 16.

If you select the "Missing pulse" check box, a check is performed to determine whether the encoder always supplies the same number of pulses between two consecutive zero marks.

If you use an encoder without zero mark, you must disable the monitoring for missing pulses.

This monitoring function is disabled by default.

###### Diagnostics (S7-300, S7-400)

###### Description

In "Properties &gt; Position &gt; Channel 0" in section "Channel 0 - Diagnostics", select the events for which the diagnostics interrupt is to be generated. No check box is selected by default.

###### Missing pulse

If you select the "Missing pulse" check box, a diagnostic interrupt is generated as soon as the encoder does not supply the same number of pulses between two consecutive zero marks. You must enable the corresponding monitoring function in the "Channel 0 - Encoder" section.

###### Traversing range

If you select the "Traversing range" check box, a diagnostic interrupt is generated immediately when the axis exits the traversing range. The corresponding monitoring function is always enabled.

###### Working range

If you select the "Working range" check box, a diagnostic interrupt is generated if the actual position value is out of range of the software limit switches. You must enable the corresponding monitoring function in the "Channel 0 - Axis" section.

You cannot use this diagnostic interrupt for positioning on a rotary axis. The respective options box is grayed out.

###### Actual value

If you selected the "Actual value" check box, a diagnostic interrupt is generated if during a traversing motion, the axis does not move by at least one pulse in the specified direction within the monitoring time. The run is cancelled.

The actual value is monitored from the start of travel until the switch-off point is reached.

You must enable the corresponding monitoring function in the "Channel 0 - Drive" section.

The CPU does not recognize the failure of a digital input. Enabling the actual value monitoring allows you to detect missing encoder signals.

This check box is selected by default.

###### Target approach

If you select the "Target approach" check box, a diagnostic interrupt is generated if the axis does not reach the target range within the monitoring time after it has reached the switch-off point.

You must enable the corresponding monitoring function in the "Channel 0 - Drive" section.

###### Target range

If you selected the "Target range" check box, a diagnostic interrupt is generated if the drive does not stop on an approached target position after the target range is reached or if the drive drifts away from the approached target position.

You must enable the corresponding monitoring function in the "Channel 0 - Drive" section.

#### Point-to-point connection function (S7-300, S7-400)

This section contains information on the following topics:

- [ASCII protocol (S7-300, S7-400)](#ascii-protocol-s7-300-s7-400)
- [3964(R) protocol (S7-300, S7-400)](#3964r-protocol-s7-300-s7-400)
- [RK512 protocol (S7-300, S7-400)](#rk512-protocol-s7-300-s7-400)

##### ASCII protocol (S7-300, S7-400)

This section contains information on the following topics:

- [PtP transmission (ASCII) (S7-300, S7-400)](#ptp-transmission-ascii-s7-300-s7-400)
- [PtP end delimiter (ASCII) (S7-300, S7-400)](#ptp-end-delimiter-ascii-s7-300-s7-400)
- [PtP - data reception (ASCII) (S7-300, S7-400)](#ptp---data-reception-ascii-s7-300-s7-400)
- [PtP - signal assignment (ASCII) (S7-300, S7-400)](#ptp---signal-assignment-ascii-s7-300-s7-400)

###### PtP transmission (ASCII) (S7-300, S7-400)

###### Description

The interrupts, characteristics of a CPU STOP, and protocol are set in "Properties &gt; General &gt; PtP &gt; Interrupt selection". Select "ASCII" as the protocol.

Depending on the type of protocol selected, the further subdivision changes in the area navigation.

For "ASCII" there are 4 parameter groups: transmission, end delimiter, data reception and signal assignment.

This section deals with PtP transmission and is divided into 3 sub-sections.

###### Transmission speed

Select the data transmission rate in bps (baud) from the "Transmission speed" drop-down list. You can select a value between 300 and 38400 baud. In full duplex mode, the maximum transmission speed is 19200 baud.

The default setting is "9600 baud".

###### Character frame

The data are transmitted via the serial interface in a character frame. Two data formats are available for each character frame.

- Data bits

  In the "Data bits" drop-down list, select the number of bits onto which a character is to be mapped.

  The default setting is "8 bits".
- Stop bits

  In the "Stop bits" drop-down list, select the number of bits appended to every transmitted character. The stop bit identifies the end of a character.

  The default setting is "1 bit".
- Parity

  In the "Parity" drop-down list, select whether the data transmission reliability is to be increased by using a parity bit. A parity of "None" means that no parity bit is transmitted. **The setting "None" is not possible in a 7-data-bit configuration.**

  A sequence of information bits can be extended to include another bit, the parity bit. The addition of its value ("0" or "1") brings the value of all the bits up to a defined state – either even or odd.

  Default selection is "Even".

###### Data flow control transmission

- Data flow control

  Here you can only specify parameters if you have selected "XON/XOFF" data flow control.

  Default selection is "None".
- XON character

  Enter a code in the "XON character" input field for the XON character. Enter a hex format code here.

  Default selection is "11".
- XOFF character

  Enter a code in the "XOFF character" input field for the XOFF character. Enter a hex format code here.

  Which values you can enter depends on whether you transmit your data with 7 or 8 data bits:

  - 7 data bits: 0 to 7FH
  - 8 data bits: 0 to FFH

    Default selection is "13".
- Wait for XON after XOFF

  In the "Wait for XON after XOFF" input field, specify a time the module has to wait after sending until it receives the XON character from the communication partner.

  You can enter a value in steps of 10 ms, from 20 ms to 65530 ms.

  Default selection is "20000 ms".

###### PtP end delimiter (ASCII) (S7-300, S7-400)

###### Description

The interrupts, characteristics of a CPU STOP, and protocol are set in "Properties &gt; General &gt; PtP &gt; Interrupt selection". Select "ASCII" as the protocol.

Depending on the type of protocol selected, the further subdivision changes in the area navigation.

For "ASCII" there are 4 PtP areas: transmission, end delimiter, data reception and signal assignment.

This section deals with PtP end delimiter and is divided into 2 sub-sections.

###### Detection of received frame

Select the required option from the "Detection of end of received frame" drop-down list. Three options are available: "After character delay time elapses", "Using end delimiter" and "After receiving a fixed number of characters".

- After character delay time elapses

  Select "After character delay time elapses" from the drop-down list to specify a configured time interval after which the end of a frame is recognized. The character delay time defines the permissible maximum interval between 2 consecutive received characters.

  This option is selected by default.
- Character delay time

  In the "Character delay time" input field you must enter this time interval in milliseconds between 1 and 65,535.

  The shortest character delay that you can select depends on the transmission speed.

| Transmission speed | Shortest character delay time |
| --- | --- |
| 300 bps | 130 ms |
| 600 bps | 65 ms |
| 1200 bps | 32 ms |
| 2400 bps | 16 ms |
| 4800 bps | 8 ms |
| 9600 bps | 4 ms |
| 19200 bps | 2 ms |
| 38400 bps | 1 ms |
| The default setting is "4 ms". |  |

- Using end delimiter

  Select "Using end delimiter" from the drop-down list to specify that the end of a message frame is recognized by its end characters.
- Monitoring time for missing end delimiter

  In the "Monitoring time for missing end delimiter" input field you can set the character delay time that can be used as monitoring time for missing end delimiter. This applies to the end delimiter for the following settings:

  - after receiving a fixed number of characters
  - after receiving the end delimiter(s)

    You can also modify the monitoring time here. The same marginal conditions as for the character delay time are applied.

    The calculation when sending and evaluating the block check character must be carried out in the user program itself.

    The default selection is "4 ms".
- End delimiter

  Select the "Using end delimiter" option of the "Detection of end of received frame" parameter to specify the use of one or two defined end delimiters for designating the end of a frame. You can work with one or two end delimiters. Optionally, one or two additional characters can be received after the end delimiter detection. You can use these characters, for example, to include a block check character (BCC) in your transmission.

  Select one of the following options in the corresponding drop-down list:

  - 1st character
  - 1st character with 1 BCC
  - 1st character with 2 BCC
  - 1st AND 2nd character
  - 1st AND 2nd character with 1 BCC
  - 1st AND 2nd character with 2 BCC

    If you have selected this option, the default setting is "1st character".
- Receiver end delimiter

  In the "Receiver 1st end delimiter" input field, and, if required, in the "Receiver 2nd end delimiter" input field, enter a code for the respective end delimiter.

  Which values you can enter depends on whether you transmit your data with 7 or 8 data bits:

  - 7 data bits: 0 to 7FH
  - 8 data bits: 0 to FFH

    The default setting is "3" for the first end delimiter and "0" for the second end delimiter.
- After receiving a fixed number of characters

  Select "After receiving a fixed number of characters" from the drop-down list to specify a fixed number of characters after which the end of a frame is recognized. The length of the received frames is always identical.

  This option is selected by default.
- Pause in transmission between frames (same length as monitoring time)

  If you have selected the "Pause in transmission between frames (same length as monitoring time)" option, a pause equal to the length of the monitoring time (for missing end delimiter) is observed so that the partner detects the receipt of the frame and can synchronize itself accordingly.

  This check box is not selected by default.
- Frame length

  In the "Frame length" input field, you can customize the number of bytes a frame should consist of. You can set a value between 1 and 1024 bytes.

  The default setting is "200 bytes".

###### Send with end delimiter

You can transmit with an end delimiter after you have specified an end delimiter as the end delimiter of a received frame.

Default selection is "Send up to and including end delimiter".

- Send up to and including end delimiter

  Select the "End criteria &gt; Send up to and including end delimiter" drop-down list to specify whether the end delimiter should be included in the data to be transmitted. Only data up to and including the end-of-message character is transmitted, even if a greater data length is specified in the SFB.
- Send up to length set in the block

  Select the "End criteria &gt; Send up to length set in the block" drop-down list to determine that data are transmitted up to the length declared in the SFB parameters. The last character must be the end delimiter.
- Send with automatically append the end delimiter

  Select the "End criteria &gt; Automatically append the end delimiter" drop-down list to determine that data are transmitted up to the length declared in the SFB parameters. The end delimiter(s) are automatically appended, that is, the end delimiters must not be contained in the data to be transmitted. Depending on the number of end identifiers, either one or two characters more than specified in the SFB (max. 1024 bytes) are transmitted to the partner.
- Sender end delimiter

  If you are using an end delimiter you can now specify its hex code. You can also select whether you want to use a second end delimiter and specify its hex code also. In the "Sender 1st end delimiter" input field, and, if required, in the "Sender 2nd end delimiter" input field, enter a code for the respective end delimiter.

  The default setting is "3" for the first end delimiter and "0" for the second end delimiter.

###### PtP - data reception (ASCII) (S7-300, S7-400)

###### Description

The interrupts, characteristics of a CPU STOP, and protocol are set in "Properties &gt; General &gt; PtP &gt; Interrupt selection". Select "ASCII" as the protocol.

Depending on the type of protocol selected, the further subdivision changes in the area navigation.

For "ASCII" there are 4 PtP areas: transmission, end delimiter, data reception and signal assignment.

This section deals with PtP data reception.

###### Reception buffering on the CPU

- Clear CPU receive buffer during startup

  Select the "Clear CPU receive buffer during startup" check box to clear the receive buffer of the technological function after power up and after the CPU transition from STOP to RUN.

  This check box is not selected by default.
- Prevent overwriting

  Select the "Prevent overwriting" check box to prevent overwriting data in the receive buffer when the buffer is full.

  This check box is selected by default.
- Use entire buffer

  Select the "Use entire buffer" check box to utilize the complete input buffer of 2048 bytes. When you use the complete buffer, the number of received frames is only dependent on the frame length.

  This check box is selected by default.
- Maximum number of buffered received frames

  In the "Maximum number of buffered received frames" input field, you can enter the number of received frames you want to have buffered in the receive buffer of the technological function. To do this, deactivate the "Use entire buffer" check box. You can select a value between 1 and 10.

  Default setting is "10".

  > **Note**
  >
  > If you specify "1" here and deactivate the "Prevent overwrite" parameter **and** cyclically read the received data from the user program, a current message frame will always be sent to the CPU.

###### PtP - signal assignment (ASCII) (S7-300, S7-400)

###### Description

The interrupts, characteristics of a CPU STOP, and protocol are set in "Properties &gt; General &gt; PtP &gt; Interrupt selection". Select "ASCII" as the protocol.

Depending on the type of protocol selected, the further subdivision changes in the area navigation.

For "ASCII" there are 4 PtP areas: transmission, end delimiter, data reception and signal assignment.

This section deals with PtP signal assignment and is divided into 2 sub-sections.

###### Operating mode

Select one of the three operating modes.

Default is "Full duplex (RS 422) four-wire point-to-point mode".

###### Full duplex (RS 422) four-wire mode point-to-point

Check the "Full duplex (RS422) four-wire PtP mode" option button to select the suitable operating mode for a PtP connection in four-wire mode. Here, you have the following options to preset the receive line:

- None
- Signal R(A) 5 volts, Signal R(B) 0 volts
- Signal R(A) 0 volts, Signal R(B) 5 volts

###### Full duplex (RS 422) four-wire multipoint master mode

If the CPU is the master, check the "Full duplex (RS422) four-wire multipoint master mode" option button to select a suitable operating mode for a four-wire connection that is capable of multipoint master operation. Here, you have the following options to preset the receive line:

- Signal R(A) 0 volts, Signal R(B) 5 volts

###### Half duplex (RS 485) two-wire mode

Check the "Half duplex (RS485) two-wire mode" option button to select a suitable operating mode for a PtP or multipoint connection in two-wire mode. The CPU can be master or slave. Here, you have the following options to preset the receive line:

- None
- Signal R(A) 0 volts, Signal R(B) 5 volts

###### Receive line initial state

- None

  Check the "None" option button to select a configuration that is significant for bus-compatible special drives only.
- Signal R(A) 5 volts, Signal R(B) 0 volts

  Select the "Signal R(A) 5 volts, Signal R(B) 0 volts" option button to select a configuration for break recognition. "Not available for full duplex (RS422) four-wire multipoint master and half duplex (RS485) two-wire operation)
- Signal R(A) 0 volts, Signal R(B) 5 volts
- Select the "Signal R(A) 0 volts, Signal R(B) 5 volts" option button to select a configuration that represents the idle state (no sending active). Break recognition is not possible with this configuration.
- Default is "Signal R(A) 5 volts, Signal R(B) 0 volts".

##### 3964(R) protocol (S7-300, S7-400)

This section contains information on the following topics:

- [PtP - transmission (3964(R)) (S7-300, S7-400)](#ptp---transmission-3964r-s7-300-s7-400)
- [PtP - data reception (3964(R)) (S7-300, S7-400)](#ptp---data-reception-3964r-s7-300-s7-400)
- [PtP - signal assignment (3964(R)) (S7-300, S7-400)](#ptp---signal-assignment-3964r-s7-300-s7-400)

###### PtP - transmission (3964(R)) (S7-300, S7-400)

###### Description

The interrupts, characteristics of a CPU STOP, and protocol are set in "Properties &gt; General &gt; PtP &gt; Interrupt selection". Select "3964(R)" as the protocol.

Depending on the type of protocol selected, the further subdivision changes in the area navigation.

For "3964(R)" there are 3 PtP areas: transmission, data reception and signal assignment.

This section deals with PtP transmission and is divided into 3 sub-sections.

###### Transmission speed

Select the data transmission rate in bps (baud) from the "Transmission speed" drop-down list. You can select a value between 300 and 38400 baud.

Default selection is "9600 baud".

###### Character frame

The data are transmitted via the serial interface in a character frame. Two data formats are available for each character frame.

- Data bits

  In the "Data bits" drop-down list, select the number of bits onto which a character is to be mapped.

  The default setting is "8 bits".
- Stop bits

  In the "Stop bits" drop-down list, select the number of bits appended to every transmitted character. The stop bit identifies the end of a character.

  The default setting is "1 bit".
- Parity

  In the "Parity" drop-down list, select whether the data transmission reliability is to be increased by using a parity bit. A parity of "None" means that no parity bit is transmitted. **The setting "None" is not possible in a 7-data-bit configuration.**

  A sequence of information bits can be extended to include another bit, the parity bit. The addition of its value ("0" or "1") brings the value of all the bits up to a defined state – either even or odd.

  Default selection is "Even".
- Priority

  In the "Priority" drop-down list, select whether the CPU should have high or low priority.

  A partner has high priority if its send request takes precedence over the send request of the other partner. A partner has low priority if its send request must wait until the send request of the other partner has been dealt with. For the 3964(R) procedure, both communication partners must be assigned different priorities, in other words, one partner is assigned high and the other low priority.

  Default selection is "High".

###### Frame parameters

- With block check

  Click the "With block check" check box to specify whether to transmit frames with or without block check.

  - Without block check

    The protocol parameters can be assigned by the user.

    If the CPU recognizes the string DLE ETX, it stops receiving and sends a DLE to the communication partner if the block was received without errors or an NAK if the block was received but with errors.
  - With block check

    The protocol parameters are set to default values.

    If the CPU recognizes the string DLE ETX BCC, it stops receiving. It compares the received block check character BCC with the internally generated longitudinal parity. If the BCC is correct and no other receive error has occurred, it returns the character string DLE (the character string NAK is returned to the communication partner if an error has occurred).

  The "With block check" check box is selected by default.
- Use defaults

  Select the "Use defaults" check box if you want to assign the default values to the protocol parameters.

  The module terminates receiving when it detects the character string DLE ETX and returns a DLE (or NAK) string to the communication partner to confirm that it has received an error-free (of faulty) block.

  You can specify the following parameters individually should you decide not to use defaults.

  The "Use defaults" check box is selected by default.
- Character delay time

  In the "Character delay time" input field, you specify the maximum permissible time interval between two received characters within a frame. You can enter a value in 10 ms increments between "20 ms" and "65530 ms".

  The shortest character delay that you can select depends on the transmission speed.

| Transmission speed | Shortest character delay time |
| --- | --- |
| 300 bps | 60 ms |
| 600 bps | 40 ms |
| 1200 bps | 30 ms |
| 2400 bps | 20 ms |
| 4800 bps | 20 ms |
| 9600 bps | 20 ms |
| 19200 bps | 20 ms |
| 38400 bps | 20 ms |
| The default setting is "220 ms". |  |

- Acknowledgment delay time

  In the "Acknowledgment delay time" input field, specify the maximum permissible time period until the acknowledgment of the partner when a connection is established (time between STX and DLE acknowledgment of the partner) or closed (time between DLE ETX and DLE acknowledgment of the partner). You can enter a value in 10 ms increments between "20 ms" and "65530 ms".

  The shortest acknowledgment delay time that you can select depends on the transmission speed.

| Transmission speed | Shortest acknowledgment delay time |
| --- | --- |
| 300 bps | 60 ms |
| 600 bps | 40 ms |
| 1200 bps | 30 ms |
| 2400 bps | 20 ms |
| 4800 bps | 20 ms |
| 9600 bps | 20 ms |
| 19200 bps | 20 ms |
| 38400 bps | 20 ms |
| Default is "2000 ms". |  |

- Connection retries

  In the "Connection retries" list, specify the maximum number of tries the module has to establish a connection. You can select a value between "1" and "255".

  Default selection is "6".
- Transmission retries

  In the "Transmission retries" list, specify the maximum number of tries the module is allowed to transmit a frame (including the first frame) in case of error. You can select a value between "1" and "255".

  Default selection is "6".

###### PtP - data reception (3964(R)) (S7-300, S7-400)

###### Description

The interrupts, characteristics of a CPU STOP, and protocol are set in "Properties &gt; General &gt; PtP &gt; Interrupt selection". Select "3964(R)" as the protocol.

Depending on the type of protocol selected, the further subdivision changes in the area navigation.

For "3964(R)" there are 3 PtP areas: transmission, data reception and signal assignment.

This topic deals with PtP data reception.

###### Reception buffer on CPU

- Clear CPU receive buffer during startup

  Select the "Clear CPU receive buffer during startup" check box to clear the receive buffer after power up and after the CPU transition from STOP to RUN.

  This check box is not selected by default.
- Prevent overwriting

  Select the "Prevent overwriting" check box to prevent overwriting data in the receive buffer when the buffer is full.

  This check box is selected by default.
- Use entire buffer

  Select the "Use entire buffer" check box if you want to use the entire 2048 bytes of the CPU receive buffer. When you use the complete buffer, the number of received frames is only dependent on the frame length.

  This check box is selected by default.
- Maximum number of buffered received frames

  In the "Maximum number of buffered received frames" input field, enter the number of received frames to be buffered in the CPU receive buffer. Enter a value between 1 and 10.

  Default setting is "10".

  > **Note**
  >
  > If you specify "1" here and deactivate the "Prevent overwrite" parameter **and** cyclically read the received data from the user program, a current message frame will always be sent to the CPU.

###### PtP - signal assignment (3964(R)) (S7-300, S7-400)

###### Description

The interrupts, characteristics of a CPU STOP, and protocol are set in "Properties &gt; General &gt; PtP &gt; Interrupt selection". Select "3964(R)" as the protocol.

Depending on the type of protocol selected, the further subdivision changes in the area navigation.

For "3964(R)" there are 3 PtP areas: transmission, data reception and signal assignment.

This section deals with PtP signal assignment.

###### Receive line initial state

With the 3964(R) protocol the X27 (RS 422/485) interface is operated in full duplex (RS 422) four-wire mode. This operating mode is suitable for four-wire PtP connections.

The following options are available as defaults for the receive line:

- None

  Select the "None" option to select a configuration that is only advisable for bus-compatible special drives.
- Signal R(A) 5 V, signal R(B) 0 V (break detection):

  With this option you select a setting that allows break detection.
- Signal R(A) 0 V, signal R(B) 5 V

  With this option you select a setting that corresponds to idle state (no sender active). No break detection is possible with this configuration.

"Signal R(A) 5 V, signal R(B) 0 V (break detection)" is selected as default.

##### RK512 protocol (S7-300, S7-400)

This section contains information on the following topics:

- [PtP - transmission (RK512) (S7-300, S7-400)](#ptp---transmission-rk512-s7-300-s7-400)
- [PtP - signal assignment (RK512) (S7-300, S7-400)](#ptp---signal-assignment-rk512-s7-300-s7-400)

###### PtP - transmission (RK512) (S7-300, S7-400)

###### Description

The interrupts, characteristics of a CPU STOP, and protocol are set in "Properties &gt; General &gt; PtP &gt; Interrupt selection". Select "RK512" as the protocol.

Depending on the type of protocol selected, the further subdivision changes in the area navigation.

For "RK512" there are 2 PtP areas: transmission and signal assignment.

This section deals with PtP transmission and is divided into 3 sub-sections.

###### Transmission speed

Select the data transmission rate in bps (baud) from the "Transmission speed" drop-down list. You can select a value between 300 and 38400 baud.

Default selection is "9600 baud".

###### Character frame

The data are transmitted via the serial interface in a character frame. Two data formats are available for each character frame.

- Data bits

  The "Data bits" drop-down list is grayed out as one character is always mapped onto 8 bits in RK512 transmission.
- Stop bits

  In the "Stop bits" drop-down list, select the number of bits appended to every transmitted character. The stop bit identifies the end of a character.

  The default setting is "1 bit".
- Parity

  In the "Parity" drop-down list, select whether the data transmission reliability is to be increased by using a parity bit. A parity of "None" means that no parity bit is transmitted. A sequence of information bits can be extended to include another bit, the parity bit. The addition of its value ("0" or "1") brings the value of all the bits up to a defined state – either even or odd.

  Default selection is "Even".
- Priority

  In the "Priority" drop-down list, select whether the CPU should have high or low priority.

  A partner has high priority if its send request takes precedence over the send request of the other partner. A partner has low priority if its send request must wait until the send request of the other partner has been dealt with. With RK512, both communication partners must be assigned different priorities, that is, one partner is assigned high and the other is assigned low priority.

  Default selection is "High".

###### Frame parameters

- With block check

  Click the "With block check" check box to specify whether to transmit frames with or without block check.

  - Without block check

    The protocol parameters can be assigned by the user.

    If the CPU recognizes the string DLE ETX, it stops receiving and sends a DLE to the communication partner if the block was received without errors or an NAK if the block was received but with errors.
  - With block check

    The protocol parameters are set to default values.

    If the CPU recognizes the string DLE ETX BCC, it stops receiving. It compares the received block check character BCC with the internally generated longitudinal parity. If the BCC is correct and no other receive error has occurred, it returns the character string DLE (the character string NAK is returned to the communication partner if an error has occurred).

  The "With block check" check box is selected by default.
- Use defaults

  Select the "Use defaults" check box if you want to assign default values to the protocol parameters.  
  If the CPU recognizes the string DLE ETX, it stops receiving and sends a DLE to the communication partner if the block was received without errors or an NAK if the block was received but with errors.

  You can specify the following parameters individually should you decide not to use defaults.

  The "Use defaults" check box is selected by default.
- Character delay time

  In the "Character delay time" input field, you specify the maximum permissible time interval between two received characters within a frame. You can enter a value in 10 ms increments between "20 ms" and "65530 ms".

  The shortest character delay that you can select depends on the transmission speed.

| Transmission speed | Shortest character delay time |
| --- | --- |
| 300 bps | 60 ms |
| 600 bps | 40 ms |
| 1200 bps | 30 ms |
| 2400 bps | 20 ms |
| 4800 bps | 20 ms |
| 9600 bps | 20 ms |
| 19200 bps | 20 ms |
| 38400 bps | 20 ms |
| The default setting is "220 ms". |  |

- Acknowledgment delay time

  In the "Acknowledgment delay time" input field, specify the maximum permissible time period until the acknowledgment of the partner when a connection is established (time between STX and DLE acknowledgment of the partner) or closed (time between DLE ETX and DLE acknowledgment of the partner). You can enter a value in 10 ms increments between "20 ms" and "65530 ms".

  The shortest acknowledgment delay time that you can select depends on the transmission speed.

| Transmission speed | Shortest acknowledgment delay time |
| --- | --- |
| 300 bps | 60 ms |
| 600 bps | 40 ms |
| 1200 bps | 30 ms |
| 2400 bps | 20 ms |
| 4800 bps | 20 ms |
| 9600 bps | 20 ms |
| 19200 bps | 20 ms |
| 38400 bps | 20 ms |
| Default selection is "2000 ms". |  |

- Connection retries

  In the "Connection retries" list, specify the maximum number of tries the module has to establish a connection. You can select a value between 1 and 255.

  Default selection is "6".
- Transmission retries

  In the "Transmission retries" list, specify the maximum number of attempts the module is allowed to transmit a frame. You can select a value between "1" and "255".

  Default selection is "6".

###### PtP - signal assignment (RK512) (S7-300, S7-400)

###### Description

The interrupts, characteristics of a CPU STOP, and protocol are set in "Properties &gt; General &gt; PtP &gt; Interrupt selection". Select "RK512" as the protocol.

Depending on the type of protocol selected, the further subdivision changes in the area navigation.

There are 2 PtP areas for "RK512": transmission and signal assignment.

This section deals with PtP transmission and is divided into 3 sub-sections.

###### Receive line initial state

The X27 (RS 422/485) interface is operated in full duplex (RS 422) four-wire operating mode. This operating mode is suitable for four-wire PtP connections.

The following options are available as defaults for the receive line:

- None

  Select the "None" option to select a configuration that is only advisable for bus-compatible special drives.
- Signal R(A) 5 V, signal R(B) 0 V (break detection):

  With this option you select a setting that allows break detection.
- Signal R(A) 0 V, signal R(B) 5 V

  With this option you select a setting that corresponds to idle state (no sender active). No break detection is possible with this configuration.
- "Signal R(A) 5 V, signal R(B) 0 V (break detection)" is selected as default.

## CPU information (S7-300, S7-400)

This section contains information on the following topics:

- [CPU registers (S7-300, S7-400)](#cpu-registers-s7-300-s7-400)
- [Accumulators (S7-300, S7-400)](#accumulators-s7-300-s7-400)

### CPU registers (S7-300, S7-400)

#### Overview

![Overview](images/63836337035_DV_resource.Stream@PNG-en-US.png)

### Accumulators (S7-300, S7-400)

#### Description

The 32-bit accumulators are general-purpose registers for processing bytes, words, and double words. For this purpose, the operands are loaded into the ACCUs and linked there. The result of the operation is always located in ACCU 1 from where it can be transferred to a memory location.

The stack mechanism for managing the accumulators works as follows:

- A load operation only affects ACCU 1 and stores the old content in ACCU 2.
- A transfer operation (copy operation) does not change the contents of the accumulators.
- The **TAK** operation swaps the contents of ACCU 1 and ACCU 2.
- The result of logic operations between ACCU 1 and ACCU 2 (math operations, comparison operations, AND, OR, etc.) is always stored in ACCU 1.

#### Definition of bytes and words in a 32-bit register (based on the example of ACCU 1)

![Definition of bytes and words in a 32-bit register (based on the example of ACCU 1)](images/63836376331_DV_resource.Stream@PNG-en-US.png)

## Addressing (S7-300, S7-400)

This section contains information on the following topics:

- [Process images (input and output memory area) (S7-300, S7-400)](#process-images-input-and-output-memory-area-s7-300-s7-400)
- [Direct access to the I/O (PI and PQ memory areas) (S7-300, S7-400)](#direct-access-to-the-io-pi-and-pq-memory-areas-s7-300-s7-400)
- [Full syntax for entering constants (S7-300, S7-400)](#full-syntax-for-entering-constants-s7-300-s7-400)
- [Summary of bit, byte, word, and double word identifiers (S7-300, S7-400)](#summary-of-bit-byte-word-and-double-word-identifiers-s7-300-s7-400)
- [Identifiers of elements and blocks (S7-300, S7-400)](#identifiers-of-elements-and-blocks-s7-300-s7-400)

### Process images (input and output memory area) (S7-300, S7-400)

#### Memory area of the process images

The OB-process image (OB1 PI) is cyclically updated by the operating system.

This process image is saved by the I/O hardware during each cycle of the instruction list. This means that the bits of the memory area I in the process image do not change during the access to the instructions. Even though the bits of the memory area Q in the process image can have different states during the program cycle, only the last signal state is sent to the output module.

See also: [User data](#user-data-s7-300-s7-400) and [Updating the process images](#updating-the-process-images-s7-300-s7-400)

#### Exceptions

The following cases do not use the process image to access the I/O:

- Direct I/O addressing of the inputs and outputs peripheral memory area (P area).
- Using functions that process the I/O data immediately.

#### Example of a normal I/O access via the process image

![Example of a normal I/O access via the process image](images/1848553611_DV_resource.Stream@PNG-en-US.png)

Update QW10 in the peripheral output with the value from MW0.

---

**See also**

[Access to the I/O addresses (S7-300, S7-400)](#access-to-the-io-addresses-s7-300-s7-400)

### Direct access to the I/O (PI and PQ memory areas) (S7-300, S7-400)

#### Direct access to the I/O

If your project needs to update the data of the I/O more quickly than the process image makes this available, you can access the signal modules directly in the peripheral inputs and outputs (PI, PQ). The current status of the input modules can be read from the PI memory area area. Output modules can be set by writing to the PQ memory area.

| Symbol | Meaning |
| --- | --- |
|  | **Caution** |
| Single bits (byte. bit) cannot be addressed in the I/O area area. To set single bits, you address bytes, words or double words in logic operations. When you write an updated bit (within a byte, word, or double word) to the PQ area, all bits at the address of this I/O area will be updated.  Refer to the **Process image** entry, for more information on the connection between the I/O memory area (PI, PQ memory area) and the process image (I and Q memory area). The entry also explains how the process image saves (stabilizes) what has been written from the signal modules or sent to them. |  |

#### Example of direct access to the I/O via the I/O memory area

![Example of direct access to the I/O via the I/O memory area](images/1848557707_DV_resource.Stream@PNG-en-US.png)

Update PQW10 in the peripheral output with the value from MW0.

---

**See also**

[Access to the I/O addresses (S7-300, S7-400)](#access-to-the-io-addresses-s7-300-s7-400)
  
[Address areas (S7-300, S7-400)](#address-areas-s7-300-s7-400)

### Full syntax for entering constants (S7-300, S7-400)

#### Overview

| Short form | Long form |
| --- | --- |
| B# | BYTE# |
| W# | WORD# |
| DW# | DWORD# |
| D# | DATE# |
| T# | TIME# |
| TOD# | TIME_OF_DAY# |
| S5T# | S5TIME# |
| DT# | DATE_AND_TIME# |
| P# | POINTER# |

### Summary of bit, byte, word, and double word identifiers (S7-300, S7-400)

#### Overview

| CPU memory area | Operand ID |  |  |  |
| --- | --- | --- | --- | --- |
|  | Bit | Byte | Word | Double word |
| Process image input | I | IB | IW | ID |
| Process image output | Q | QB | QW | QD |
| Bit memory | M | MB | MW | MD |
| Local data | L | LB | LW | LD |
| Direct I/O area inputs | - | PIB | PIW | PID |
| Direct I/O area outputs | - | PQB | PQW | PQD |
| Data block [OPN] DB [OPN] DI | DBX DIX | DBB DIB | DBW DIW | DBD DID |
| Timer (T) | T | - | T | - |
| Counter (C) | C | - | C | - |

> **Note**
>
> The two operands **IB0** and **IB1** (memory area I, format: byte, address bytes 0, 1) address the same two bytes as the operand **IW0** (memory area I, format: word, 2 bytes, incrementing of byte 0 to address bytes 0, 1).

### Identifiers of elements and blocks (S7-300, S7-400)

#### Overview

| Symbol | Meaning |
| --- | --- |
| T | Timer |
| DB | Global data block |
| DI | Instance data block |
| FC | Function |
| FB | Function block |
| OB | Organization block |
| C (or Z) | Counter (depending on the mnemonics) |
| SDB | System data block |
| SFC | System function |
| SFB | System function block |

## Symbolic and numerical names of instructions (S7-300, S7-400)

### Description

The instructions from the task card are comprised of functions (FC), function blocks (FB), system functions (SFC) and system function blocks (SFB) that are identified internally by numbers.

The following tables show the assignment of numerical and symbolic names.

### Function blocks (FBs)

| Numerical name | Symbolic name |
| --- | --- |
| FB 2 | S_RCV |
| FB 3 | S_SEND |
| FB 4 | S_VSTAT |
| FB 5 | S_VSET |
| FB 6 | S_XON |
| FB 7 | S_RTS |
| FB 8 | S_V24 |
| FB 8 <sup>(1)</sup> | USEND_S |
| FB 9 <sup>(1)</sup> | URCV_S |
| FB 14 <sup>(1)</sup> | GET_S |
| FB 15 <sup>(1)</sup> | PUT_S |
| FB 40 <sup>(1)</sup> | FTP_CMD |
| FB 46 | PG_DIAL |
| FB 47 | AS_DIAL |
| FB 48 | SMS_SEND |
| FB 49 | AS_MAIL |
| FB 52 <sup>(1)</sup> | PNIO_RW_REC |
| FB 53 | PE_DS3_Write_ET200S |
| FB 54 <sup>(1)</sup> | PNIO_ALARM |
| FB 55 | IP_CONFIG |
| FB 56 <sup>(1)</sup> | LOGICAL_TRIGGER |
| FB 60 | SET_SW |
| FB 61 | SET_SW_S |
| FB 62 | TIMESTMP |
| FB 80 | LEAD_LAG |
| FB 81 | DCAT |
| FB 81 | S_MODB |
| FB 82 | MCAT |
| FB 83 | IMC |
| FB 84 | SMC |
| FB 85 | DRUM |
| FB 86 | PACK |
| FB 210 | FW_TCP |
| FB 220 | FW_IOT |
| FB 450 <sup>(2)</sup> | RED_IN_MGP |
| FB 451 <sup>(2)</sup> | RED_OUT_MGP |
| FB 452 <sup>(2)</sup> | RED_DIAG_MGP |
| FB 453 <sup>(2)</sup> | RED_STATUS_MGP |
| FB 815 | PE_Start_End_Pause |
| FB 816 | PE_CMD |
| FB 817 <sup>(1)</sup> | PE_I_DEV |
| <sup>(1)</sup> for S7-300   <sup>(2)</sup> for S7-400   <sup>(3) </sup>not for WinAC   <sup>(4) </sup> for S7-400, not for WinAC   <sup>(5) </sup> for WinAC |  |

### Functions (FCs)

| Numerical name | Symbolic name |
| --- | --- |
| FC 0 <sup>(1)</sup> | PE_Error_RSP |
| FC 1 <sup>(1)</sup> | PE_Start_RSP |
| FC 1 <sup>(1)</sup> | DP_SEND |
| FC 2 | CONCAT |
| FC 2 <sup>(1)</sup> | PE_End_RSP |
| FC 2 <sup>(1)</sup> | DP_RECV |
| FC 3 <sup>(1)</sup> | PE_List_Modes_RSP |
| FC 3 <sup>(1)</sup> | DP_DIAG |
| FC 4 | DELETE |
| FC 4 <sup>(1)</sup> | PE_Get_Mode_RSP |
| FC 4 <sup>(1)</sup> | DP_CTRL |
| FC 5 <sup>(1)</sup> | PE_PEM_Status_RSP |
| FC 5 <sup>(1)</sup> | AG_SEND |
| FC 6 <sup>(1)</sup> | PE_Identify_RSP |
| FC 6 <sup>(1)</sup> | AG_RECV |
| FC 7 | Asi_3422 |
| FC 7 <sup>(1)</sup> | PE_Measurement_List_RSP |
| FC 7 <sup>(1)</sup> | AG_LOCK |
| FC 8 <sup>(1)</sup> | PE_Measurement_Value_RSP |
| FC 8 <sup>(1)</sup> | AG_UNLOCK |
| FC 10 <sup>(1)</sup> | AG_CNTRL |
| FC 11 | FIND |
| FC 11 <sup>(1)</sup> | PNIO_SEND |
| FC 12 <sup>(1)</sup> | PNIO_RECV |
| FC 17 | INSERT |
| FC 17 | S_USST |
| FC 18 | S_USSR |
| FC 19 | S_USSI |
| FC 20 | LEFT |
| FC 21 | LEN |
| FC 22 | LIMIT |
| FC 25 | MAX |
| FC 26 | MID |
| FC 27 | MIN |
| FC 31 | REPLACE |
| FC 32 | RIGHT |
| FC 36 | ENCO |
| FC 36 | SEL |
| FC 37 | DECO |
| FC 60 | LOC_TIME |
| FC 61 | BT_LT |
| FC 62 | LT_BT |
| FC 62 <sup>(1)</sup> | C_CNTRL |
| FC 63 | S_LTINT |
| FC 74 <sup>(3)</sup> | I_ABORT |
| FC 80 | TONR |
| FC 82 | RSET |
| FC 83 | SET |
| FC 84 | ATT |
| FC 85 | FIFO |
| FC 86 | TBL_FIND |
| FC 87 | LIFO |
| FC 88 | TBL |
| FC 89 | TBL_WRD |
| FC 90 | WSR |
| FC 91 | WRD_TBL |
| FC 92 | SHRB |
| FC 93 | SEG |
| FC 98 | BCDPL |
| FC 99 | BITSUM |
| FC 100 | RSETI |
| FC 101 | SETI |
| FC 102 | DEV |
| FC 103 | CDT |
| FC 104 | TBL_TBL |
| FC 105 | SCALE |
| FC 106 | UNSCALE |
| FC 450 <sup>(2)</sup> | RED_INIT_MGP |
| FC 451 <sup>(2)</sup> | RED_DEPA_MGP |
| <sup>(1)</sup> for S7-300   <sup>(2)</sup> for S7-400   <sup>(3) </sup>not for WinAC   <sup>(4) </sup> for S7-400, not for WinAC   <sup>(5) </sup> for WinAC |  |

### System function blocks (SFBs)

| Numerical name | Symbolic name |
| --- | --- |
| SFB 0 | CTU |
| SFB 1 | CTD |
| SFB 2 | CTUD |
| SFB 3 | TP |
| SFB 4 | TON |
| SFB 5 | TOF |
| SFB 16 <sup>(4)</sup> | PRINT |
| SFB 19 <sup>(2)</sup> | START |
| SFB 20 <sup>(2)</sup> | STOP |
| SFB 21 <sup>(4)</sup> | RESUME |
| SFB 22 <sup>(2)</sup> | STATUS |
| SFB 23 <sup>(2)</sup> | USTATUS |
| SFB 29 <sup>(1)</sup> | HS_COUNT_300C |
| SFB 30 <sup>(1)</sup> | FREQ_MES_300C |
| SFB 31 <sup>(2)</sup> | NOTIFY_8P |
| SFB 32 | DRUM_X |
| SFB 33 <sup>(2)</sup> | ALARM |
| SFB 34 <sup>(2)</sup> | ALARM_8 |
| SFB 35 <sup>(2)</sup> | ALARM_8P |
| SFB 36 <sup>(2)</sup> | NOTIFY_8P |
| SFB 37 <sup>(2)</sup> | AR_SEND |
| SFB 38 <sup>(1)</sup> | HSC_A_B_300C |
| SFB 39 <sup>(1)</sup> | POS_300C |
| SFB 44 <sup>(1)</sup> | ANALOG_300C |
| SFB 46 <sup>(1)</sup> | DIGITAL_300C |
| SFB 47 <sup>(1)</sup> | COUNT_300C |
| SFB 48 <sup>(1)</sup> | FREQUENC_300C |
| SFB 49 <sup>(1)</sup> | PULSE_300C |
| SFB 52 | RDREC |
| SFB 53 | WRREC |
| SFB 54 | RALRM |
| SFB 60 <sup>(1)</sup> | SEND_PTP_300C |
| SFB 61 <sup>(1)</sup> | RCV_PTP_300C |
| SFB 62 <sup>(1)</sup> | RES_RCVB_300C |
| SFB 63 <sup>(1)</sup> | SEND_RK_300C |
| SFB 64 <sup>(1)</sup> | FETCH_RK_300C |
| SFB 65 <sup>(1)</sup> | SERVE_RK_300C |
| SFB 73 | RCVREC |
| SFB 74 | PRVREC |
| SFB 75 | SALRM |
| SFB 81 | RD_DPAR |
| SFB 104 | IP_CONF |
| SFB 65001 <sup>(5)</sup> | CREA_COM |
| SFB 65002 <sup>(5)</sup> | EXEC_COM |
| SFB 65002 <sup>(5)</sup> | ASYN_COM |
| <sup>(1)</sup> for S7-300   <sup>(2)</sup> for S7-400   <sup>(3) </sup>not for WinAC   <sup>(4) </sup> for S7-400, not for WinAC   <sup>(5) </sup> for WinAC |  |

### System functions (SFCs)

| Numerical name | Symbolic name |
| --- | --- |
| SFC 2 | SET_RTM |
| SFC 3 | CTRL_RTM |
| SFC 4 | READ_RTM |
| SFC 5 | GADR_LGC |
| SFC 7 <sup>(3)</sup> | DP_PRAL |
| SFC 9 <sup>(2)</sup> | EN_MSG |
| SFC 10 <sup>(2)</sup> | DIS_MSG |
| SFC 11 | DPSYC_FR |
| SFC 12 | D_ACT_DP |
| SFC 13 | DPNRM_DG |
| SFC 14 | DPRD_DAT |
| SFC 17 | ALARM_SQ |
| SFC 18 | ALARM_S |
| SFC 19 | ALARM_SC |
| SFC 20 | BLKMOV |
| SFC 21 | FILL |
| SFC 22 | CREAT_DB |
| SFC 23 | DEL_DB |
| SFC 24 | TEST_DB |
| SFC 26 <sup>(2)</sup> | UPDAT_PI |
| SFC 27 <sup>(2)</sup> | UPDAT_PO |
| SFC 28 | SET_TINT |
| SFC 29 | CAN_TINT |
| SFC 30 | ACT_TINT |
| SFC 31 | QRY_TINT |
| SFC 32 | SRT_DINT |
| SFC 33 | CAN_DINT |
| SFC 34 | QRY_DINT |
| SFC 35 <sup>(4)</sup> | MP_ALM |
| SFC 36 | MSK_FLT |
| SFC 37 | DMSK_FLT |
| SFC 38 | READ_ERR |
| SFC 39 | DIS_IRT |
| SFC 40 | EN_IRT |
| SFC 41 | DIS_AIRT |
| SFC 42 | EN_AIRT |
| SFC 43 | RE_TRIGR |
| SFC 44 | REPL_VAL |
| SFC 46 | STP |
| SFC 47 | WAIT |
| SFC 48 <sup>(4)</sup> | SNC_RTCB |
| SFC 49 | LGC_GADR |
| SFC 50 | RD_LGADR |
| SFC 51 | RDSYSST |
| SFC 52 | WR_USMSG |
| SFC 54 <sup>(2)</sup> | RD_DPARM |
| SFC 55 | WR_PARM |
| SFC 56 | WR_DPARM |
| SFC 57 | PARM_MOD |
| SFC 58 | WR_REC |
| SFC 59 | RD_REC |
| SFC 60 <sup>(4)</sup> | GD_SND |
| SFC 61 <sup>(4)</sup> | GD_RCV |
| SFC 62 <sup>(2)</sup> | CONTROL |
| SFC 64 | TIME_TCK |
| SFC 64 | RD_SINFO |
| SFC 65 <sup>(3)</sup> | X_SEND |
| SFC 66 <sup>(3)</sup> | X_RCV |
| SFC 67 <sup>(3)</sup> | X_GET |
| SFC 68 <sup>(3)</sup> | X_PUT |
| SFC 69 <sup>(3)</sup> | X_ABORT |
| SFC 70 | GEO_LOG |
| SFC 71 | LOG_GEO |
| SFC 72 <sup>(3)</sup> | I_GET |
| SFC 73 <sup>(3)</sup> | I_PUT |
| SFC 75 | SET_ADDR |
| SFC 78 <sup>(2)</sup> | OB_RT |
| SFC 79 | SETP |
| SFC 80 | RESETP |
| SFC 81 | UBLKMOV |
| SFC 82 <sup>(1) (6)</sup> | CREA_DBL |
| SFC 83 <sup>(1) (6)</sup> | READ_DBL |
| SFC 84 <sup>(1) (6)</sup> | WRIT_DBL |
| SFC 85 <sup>(6)</sup> | CREA_DB |
| SFC 87 <sup>(2)</sup> | C_DIAG |
| SFC 90 <sup>(4)</sup> | H_CTRL |
| SFC 99 | WWW |
| SFC 100 <sup>(2)</sup> | SET_CLKS |
| SFC 101 | RTM |
| SFC 102 <sup>(1)</sup> | RD_DPARA |
| SFC 103 <sup>(3)</sup> | DP_TOPOL |
| SFC 104 <sup>(2)</sup> | CIR |
| SFC 105 | READ_SI |
| SFC 106 | DEL_SI |
| SFC 107 | ALARM_DQ |
| SFC 108 | ALARM_D |
| SFC 109 | PROTECT |
| SFC 112 | PN_IN |
| SFC 113 | PN_OUT |
| SFC 114 | PN_DP |
| SFC 126 | SYNC_PI |
| SFC 127 | SYNC_PO |
| SFC 154 | DPWR_DAT |
| <sup>(1)</sup> for S7-300   <sup>(2)</sup> for S7-400   <sup>(3) </sup>not for WinAC   <sup>(4) </sup> for S7-400, not for WinAC   <sup>(5) </sup> for WinAC |  |

---
title: "Functional description of S7-1200 CPUs (S7-1200)"
package: ProgCPU12002MenUS
topics: 111
devices: [S7-1200]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Functional description of S7-1200 CPUs (S7-1200)

This section contains information on the following topics:

- [Operating modes (S7-1200)](#operating-modes-s7-1200)
- [Memory areas (S7-1200)](#memory-areas-s7-1200)
- [I/O data area (S7-1200)](#io-data-area-s7-1200)
- [Basics of program execution (S7-1200)](#basics-of-program-execution-s7-1200)
- [Setting the operating behavior (S7-1200)](#setting-the-operating-behavior-s7-1200)
- [Symbolic and numerical names of instructions (S7-1200)](#symbolic-and-numerical-names-of-instructions-s7-1200)
- [Organization blocks (S7-1200)](#organization-blocks-s7-1200)
- [Useful information on CPU firmware versions and STEP 7 versions (S7-1200)](#useful-information-on-cpu-firmware-versions-and-step-7-versions-s7-1200)

## Operating modes (S7-1200)

This section contains information on the following topics:

- [Principles of the operating modes of S7-CPUs (S7-1200)](#principles-of-the-operating-modes-of-s7-cpus-s7-1200)
- [Operating mode transitions (S7-1200)](#operating-mode-transitions-s7-1200)
- ["STARTUP" operating mode (S7-1200)](#startup-operating-mode-s7-1200)
- [RUN mode (S7-1200)](#run-mode-s7-1200)
- [STOP mode (S7-1200)](#stop-mode-s7-1200)
- [Basics of a memory reset (S7-1200)](#basics-of-a-memory-reset-s7-1200)

### Principles of the operating modes of S7-CPUs (S7-1200)

#### Introduction

Operating modes describe the behavior of the CPU. The following operating modes are possible:

- STARTUP
- RUN
- STOP

In these operating modes, the CPU can communicate via the PN/IE interface, for example.

#### Other operating modes

If the CPU is not ready for operation, it is in one of following two operating modes:

- Deenergized, i.e. the supply voltage is switched off.
- Defective, which means an internal error has occurred.

  If the "Defective" status is caused by a firmware error, this state is indicated by the status LEDs of the CPU (refer to the description of the CPU). To find out the cause, follow these steps:

  - Turn the power supply switch off and on again.
  - Read out the diagnostics buffer when the CPU starts up and send the data for analysis to Customer Support.

  If the CPU does not start up, replace it.

---

**See also**

[STOP mode (S7-1200)](#stop-mode-s7-1200)
  
[RUN mode (S7-1200)](#run-mode-s7-1200)
  
["STARTUP" operating mode (S7-1200)](#startup-operating-mode-s7-1200)

### Operating mode transitions (S7-1200)

#### Overview

The following figure shows the operating modes and the operating mode transitions of S7-1200 CPUs:

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

### "STARTUP" operating mode (S7-1200)

This section contains information on the following topics:

- [Principles of the STARTUP mode (S7-1200)](#principles-of-the-startup-mode-s7-1200)
- [Warm restart (S7-1200)](#warm-restart-s7-1200)
- [Startup activities (S7-1200)](#startup-activities-s7-1200)
- [Special features during startup (S7-1200)](#special-features-during-startup-s7-1200)

#### Principles of the STARTUP mode (S7-1200)

##### Function

After turning on the CPU, it executes a startup program before starting to execute the cyclic user program.

By suitably programming startup OBs, you can specify certain initialization variables for your cyclic program in the startup program. There is no rule in terms of the number of startup OBs. That is, you can set up one or several startup OBs in your program, or none at all.

##### Parameter settings for startup characteristics

You can specify whether the CPU remains in STOP mode or whether a warm restart is run. Over and above this, you can set the response during startup (RUN or previous mode) in the "Startup" group of the CPU properties.

##### Special characteristics

Note the following points regarding the "STARTUP" mode:

- The startup OBs are executed. All startup OBs you have programmed are executed, regardless of the selected startup mode.
- No time-based program execution can be performed.
- Interrupt controlled program execution limited to:

  - OB 82 (diagnostics interrupt)
- The outputs on the modules are disabled.
- The process image is not updated; direct I/O access to inputs is possible.

---

**See also**

[Editing properties and parameters](Configuring%20devices%20and%20networks.md#editing-properties-and-parameters)
  
[Principles of the operating modes of S7-CPUs (S7-1200)](#principles-of-the-operating-modes-of-s7-cpus-s7-1200)
  
[Startup OBs (S7-1200)](#startup-obs-s7-1200)
  
[Warm restart (S7-1200)](#warm-restart-s7-1200)

#### Warm restart (S7-1200)

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

---

**See also**

[Retentive memory areas (S7-1200)](#retentive-memory-areas-s7-1200)

#### Startup activities (S7-1200)

##### Overview

The following table shows which activities the CPU performs at STARTUP:

| Activities in execution sequence | At warm restart |
| --- | --- |
| Clear non-retentive bit memories | Yes |
| Clear all bit memories | No |
| Clear the process image output | Yes |
| Processing startup OBs | Yes |
| Update the process image input | Yes |
| Enable outputs after changing to "RUN" mode | Yes |

##### Sequence

The following figure shows the activities of the CPU in "STOP", "STARTUP", and "RUN" modes.

You can use the following measures to specify the state of the I/O outputs in the first cycle of the user program:

- Use assignable output modules to be able to output substitute values or to retain the last value.
- Set default values for outputs in startup OBs.

During the startup, all interrupt events are entered in a queue so that they can be processed later during RUN mode. In RUN mode, hardware interrupts can be processed at any time.

![Sequence](images/166707801483_DV_resource.Stream@PNG-en-US.png)

#### Special features during startup (S7-1200)

##### Response when expected and actual configurations do not match

The expected configuration is represented by the engineering configuration loaded on the CPU. The actual configuration is the actual configuration of the automation system.

If the expected configuration and actual configuration differ, the CPU nevertheless initially changes to RUN.

##### Canceling a STARTUP

If errors occur during startup, the startup is canceled and the CPU remains in "STOP" mode.

Under the following conditions, a startup will not be performed or will be canceled:

- If an invalid SD card is inserted.
- If no hardware configuration has been downloaded.

---

**See also**

[Overview of the CPU properties (S7-1200)](#overview-of-the-cpu-properties-s7-1200)

### RUN mode (S7-1200)

#### Function

In "RUN" mode the cyclic, time-driven, and interrupt-driven program sections execute:

- The process image output is read out.
- The process image input table is read.
- The user program is executed.

Active data exchange between S7-1200 CPUs by means of Open User Communication is only possible in "RUN" mode.

#### Running the user program

Once the CPU has read the inputs, the cyclic program runs from the first to the last instruction.

If you have configured a minimum cycle time, the CPU will not end the cycle until this minimum cycle time is up even if the user program is completed sooner.

A maximum cycle time is set which you can adjust according to your requirements. This ensures that the cyclic program is completed within a specified time. The system will respond with a time error if the cyclic program is not completed within this time.

Other events such as hardware and diagnostic interrupts can interrupt the cyclic program flow and prolong the cycle time.

---

**See also**

[Principles of the operating modes of S7-CPUs (S7-1200)](#principles-of-the-operating-modes-of-s7-cpus-s7-1200)
  
[Events and OBs (S7-1200)](#events-and-obs-s7-1200)
  
[Using Open User Communication (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#using-open-user-communication-s7-1200-s7-1500-s7-1500t)

### STOP mode (S7-1200)

#### Function

In "STOP" mode, the user program is not executed. All outputs are disabled or react according to the parameter settings: They provide a substitute value as set in the parameters or retain the last value output and bring the controlled process to a safe status.

The CPU checks the following points:

- Hardware, for example whether are all modules are available
- Whether the default settings for the CPU are applicable or parameter sets are present
- Whether the general conditions for the programmed startup behavior are correct

---

**See also**

[Principles of the operating modes of S7-CPUs (S7-1200)](#principles-of-the-operating-modes-of-s7-cpus-s7-1200)

### Basics of a memory reset (S7-1200)

#### Function

A memory reset on the CPU is possible only in STOP mode.

When memory is reset, the CPU is changed to an "initial status". This means:

- An existing online connection between your programming device/PC and the CPU is terminated.
- The content of the work memory and the retentive and non-retentive data are deleted.
- The diagnostic buffer, the time, the IP address, the hardware configuration, and active force jobs are retained.
- The load memory (code and data blocks) is then copied to work memory. As a result, the data blocks no longer have current values but their configured initial values.

## Memory areas (S7-1200)

This section contains information on the following topics:

- [What you need to know about SIMATIC memory cards (S7-1200)](#what-you-need-to-know-about-simatic-memory-cards-s7-1200)
- [Load memory (S7-1200)](#load-memory-s7-1200)
- [Work memory (S7-1200)](#work-memory-s7-1200)
- [System memory (S7-1200)](#system-memory-s7-1200)

### What you need to know about SIMATIC memory cards (S7-1200)

#### Function of the SIMATIC memory card

The SIMATIC memory card for an S7-1200 is an SD memory card, preformatted by Siemens for the CPU user program, that is compatible with the Windows operating system.

![Function of the SIMATIC memory card](images/86790642571_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Formatting the SIMATIC memory card**  You may only delete files and folders. If you format the SIMATIC memory card with Windows tools, for example with a commercially available card reader, you will render the memory card unusable as a storage medium for an S7 CPU. |  |

#### Setting the card type

You can use the SIMATIC memory card as a transfer card, a program card or a firmware update card.

To set the card type, insert the SIMATIC memory card into the card reader of the programming device and select the "Card reader/USB memory" folder from the project tree. In the properties of the selected memory card, designate the card type:

- Program

  If the SIMATIC memory card is used as a program card, you can load the user program to the card. In this case, the internal load memory of the device is replaced by the SIMATIC memory card and the internal load memory is erased. The user program is then fully executable from the SIMATIC memory card. If the SIMATIC memory card with the user program is removed, there is then no program.
- Transfer

  If the SIMATIC memory card is used as a transfer card, you can transfer the user program from the card to the internal load memory of the CPU. You can then remove the SIMATIC memory card.
- Firmware card

  Firmware for the S7-1200 modules can be stored on a SIMATIC memory card. It is therefore possible to perform a firmware update with the help of a specifically prepared SIMATIC memory card. A backup copy of firmware for a module can also be stored on the SIMATIC memory card.

#### Transferring objects from the project to a SIMATIC memory card

When the SIMATIC memory card is inserted in the programming device or in an external card reader, you can transfer the following objects from the project tree to the SIMATIC memory card:

- Individual blocks (multiple selection possible)

  In this case a consistent transfer is available, as the dependencies of the blocks to each other is taken into account with block selection.
- PLC

  In this case, all objects relevant to processing, such as blocks and the hardware configuration, are transferred to the SIMATIC memory card, just as with downloading.

To perform the transfer, you can move the objects with drag-and-drop or use the command "Card reader/USB memory &gt; Write to memory card" in the "Project" menu.

#### Transferring objects from the SIMATIC memory card to the project

You can transfer Individual blocks (multiple selection is possible) by dragging them to the project. A hardware configuration cannot be transferred from the SIMATIC memory card to the project.

#### Updating firmware with a SIMATIC memory card

You can get the latest firmware data on the Internet from the Service &amp; Support pages:

[http://support.automation.siemens.com](http://support.automation.siemens.com/WW/view/en/34143537)

Save the firmware files on the hard disk and plug the SIMATIC Memory Card into the card reader of your programming device.

To store the file on the SIMATIC memory card, select the SIMATIC memory card in the "Card Reader/USB memory" folder in the project tree. Select the shortcut menu "Card Reader/USB memory &gt; Create firmware update memory card".

Then follow the instructions in the Service &amp; Support portal for performing a firmware update with your CPU.

Updating the firmware changes the CPU firmware status. If you have used the CPU in the project, you will have to update the CPU already configured to the CPU with the new firmware status by changing devices offline, and adapt and then load the program or configuration.

---

**See also**

[Replacing a hardware component](Configuring%20devices%20and%20networks.md#replacing-a-hardware-component)
  
[Useful information on CPU firmware versions and STEP 7 versions (S7-1200)](#useful-information-on-cpu-firmware-versions-and-step-7-versions-s7-1200)
  
[Displaying properties of memory cards](Editing%20project%20data.md#displaying-properties-of-memory-cards)
  
[GetSMCinfo: Reading out information about the SIMATIC memory card (S7-1200, S7-1500)](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#getsmcinfo-reading-out-information-about-the-simatic-memory-card-s7-1200-s7-1500)

### Load memory (S7-1200)

#### Function

Each CPU has an internal load memory. The size of this internal load memory depends on the CPU used.

This internal load memory can be replaced by using external memory cards. If there is no memory card inserted, the CPU uses the internal load memory; if a memory card is inserted, the CPU uses the memory card as load memory.

#### Copying from internal load memory to external load memory

With this option in the CPU properties, you can prevent someone from simply inserting a memory card and transferring the contents of the internal load memory (project data) to a memory card, thus gaining access to this data.

If you do not select the "Disable copying from internal load memory to external load memory" setting in the "Protection &amp; Security" area of the CPU properties, the CPU determines which type of memory card you are inserting:

- Empty memory card: An empty memory card has no job file (S7_JOB.S7S). If you insert an empty memory card, the CPU adds a program job file. It then copies the internal load memory to the external load memory (the program file on the memory card) and deletes the internal load memory.
- Empty program card: An empty program card contains a program job file, which is empty. In this case, the CPU copies the internal load memory to the external load memory (the program file on the memory card) and deletes the internal load memory.

If you have selected the setting "Disable copying from internal load memory to external load memory" in the protection properties of the device configuration of the CPU, the CPU reacts as follows:

- Empty memory card: An empty memory card has no job file (S7_JOB.S7S). If you insert an empty memory card, the CPU goes into STOP state. It creates no program job file and it does not copy the internal load memory to the external load memory (i.e. the program file on the memory card). It does not delete the internal load memory.
- Empty program card: An empty program card contains a program job file, which is empty. If you insert this memory card, then the CPU goes into STOP state. It does not copy the internal load memory to the external load memory (i.e. the program file on the memory card). It does not delete the internal load memory.

If you insert a program card, transfer card or a card with a firmware update into the CPU, the configuration setting "Disable copying from internal load memory to external load memory" does not affect how the CPU evaluates the memory card.

---

**See also**

[Using memory cards](Editing%20project%20data.md#using-memory-cards)

### Work memory (S7-1200)

#### Function

Work memory is a non-retentive memory area for storing elements of the user program that are relevant for program execution. The user program is executed exclusively in work memory and system memory.

### System memory (S7-1200)

This section contains information on the following topics:

- [System memory areas (S7-1200)](#system-memory-areas-s7-1200)
- [Retentive memory areas (S7-1200)](#retentive-memory-areas-s7-1200)
- [process image input/output (S7-1200)](#process-image-inputoutput-s7-1200)
- [Diagnostics buffer (S7-1200)](#diagnostics-buffer-s7-1200)

#### System memory areas (S7-1200)

##### Function

System memory contains the memory elements that each CPU makes available to the user program, such as the process image and bit memory.

By using appropriate operations in your user program, you address the data directly in the relevant operand area.

The following table shows the operand areas of the system memory:

| Operand area | Description | Access via units of the following size: | S7 notation |
| --- | --- | --- | --- |
| Process image output | The CPU writes the values from the process image output table to the output modules at the start of the cycle. | Output (bit) | Q |
| Output byte | QB |  |  |
| Output word | QW |  |  |
| Output double word | QD |  |  |
| Process image input | The CPU reads the inputs from the input modules and saves the values to the process image input table at the start of the cycle. | Input (bit) | I |
| Input byte | IB |  |  |
| Input word | IW |  |  |
| Input double word | ID |  |  |
| Bit memory | This area provides storage for intermediate results calculated in the program. | Bit memory (bit) | M |
| Memory byte | MB |  |  |
| Memory word | MW |  |  |
| Memory double word | MD |  |  |
| Data block | Data blocks store information for the program. They can either be defined so that all code blocks can access them (global DBs) or assigned to a specific FB or SFB (instance DB).  Requirement: The block attribute "Optimized block access" is not enabled. | Data bit | DBX |
| Data byte | DBB |  |  |
| Data word | DBW |  |  |
| Data double word | DBD |  |  |
| Local data | This area contains the temporary data of a block while the block is being processed.   Requirement: The block attribute "Optimized block access" is not enabled.  Recommendation: Access local data (temp) symbolically. | Local data bit | L |
| Local data byte | LB |  |  |
| Local data word | LW |  |  |
| Local data double word | LD |  |  |
| I/O input area | The I/O input and output areas permit direct access to central and distributed input and output modules. | I/O input bit | &lt;tag&gt;:P |
| I/O input byte |  |  |  |
| I/O input word |  |  |  |
| I/O input double word |  |  |  |
| I/O output area | I/O output bit |  |  |
| I/O output byte |  |  |  |
| I/O output word |  |  |  |
| I/O output double word |  |  |  |

---

**See also**

[Diagnostics buffer (S7-1200)](#diagnostics-buffer-s7-1200)
  
[Basic principles of process images (S7-1200)](#basic-principles-of-process-images-s7-1200)
  
[Basic principles for programming of data blocks](Programming%20data%20blocks.md#basic-principles-for-programming-of-data-blocks)
  
[Declaring local tags and constants in the block interface](Declaring%20the%20block%20interface.md#declaring-local-tags-and-constants-in-the-block-interface)
  
[Overview of the block interface](Declaring%20the%20block%20interface.md#overview-of-the-block-interface)
  
[Access to the I/O addresses (S7-1200)](#access-to-the-io-addresses-s7-1200)

#### Retentive memory areas (S7-1200)

##### Retentive memory areas

Data loss after power failure can be avoided by marking certain data as retentive. This data is stored in a retentive memory area. A retentive memory area is an area that retains its content following a warm restart, in other words, after cycling the power when the CPU changes from STOP to RUN.

The following data can be assigned retentivity:

- Bit memory: The precise width of the memory can be defined for bit memory in the PLC tag table or in the assignment list.
- Tags of a function block (FB): You can define individual tags as retentive in the interface of an FB if you have enabled optimized block access. Retentivity settings can be defined only in the assigned instance data block if optimized block access has not been activated for the FB.
- Tags of a global data block: You can define retentivity either for individual or for all tags of a global data block depending on the settings for access.

  - Block with optimized access: retentivity can be set for each individual tag.
  - Block with standard access: The retentivity setting applies to all tags of the DB; either all tags are retentive or no tag is retentive.

---

**See also**

[Warm restart (S7-1200)](#warm-restart-s7-1200)
  
[Basics of block access](Programming%20basics.md#basics-of-block-access)
  
[Setting the retentivity of PLC tags](Declaring%20PLC%20tags.md#setting-the-retentivity-of-plc-tags)

#### process image input/output (S7-1200)

This section contains information on the following topics:

- [Basic principles of process images (S7-1200)](#basic-principles-of-process-images-s7-1200)
- [Updating the process images (S7-1200)](#updating-the-process-images-s7-1200)

##### Basic principles of process images (S7-1200)

###### Function

When the user program addresses the input (I) and output (O) operand areas, it does not query or change the signal states on the digital signal modules. Instead, it accesses a memory area in the system memory of the CPU. This memory area is referred to as the process image.

###### Advantages of the process image

Compared with direct access to input and output modules, the main advantage of accessing the process image is that the CPU has a consistent image of the process signals for the duration of one program cycle. If a signal state on an input module changes during program execution, the signal state in the process image is retained until the process image is updated again in the next cycle. The process of repeatedly scanning an input signal within a user program ensures that consistent input information is always available.

Access to the process image also requires far less time than direct access to the signal modules since the process image is located in the internal memory of the CPU.

##### Updating the process images (S7-1200)

###### Sequence

The operating system updates the process images at cyclic intervals unless defined otherwise in your configuration. The process image input/output is updated in the following order:

1. The internal tasks of the operating system are performed.
2. The process image output (PIQ) table is written to the outputs of the module.
3. The status of inputs is read to the process image input (PII) table.
4. The user program is executed with all the blocks that are called in it.

The operating system automatically controls the writing of the process image output to the outputs of the modules and the reading of the process image input.

###### Special characteristics

You have the option of accessing inputs or outputs directly using direct I/O access.

- If an instruction accesses an output directly and the output address is located in the process image output, the process image of the relevant output is updated.
- If an instruction accesses an output directly and the output address is **not** located in the process image output, the process image of the relevant output is **not** updated.

###### Example of normal I/O access by way of the process image

![Example of normal I/O access by way of the process image](images/12627319435_DV_resource.Stream@PNG-en-US.png)

Update QW10 in the I/O output area with the value from MW0.

###### I/O access error during process image updating

If an error occurs during process image updating (I/O access error), the CPU reacts with the default system reaction "Ignore".

---

**See also**

[Start address of a module (S7-1200)](#start-address-of-a-module-s7-1200)
  
[Access to the I/O addresses (S7-1200)](#access-to-the-io-addresses-s7-1200)
  
[Startup activities (S7-1200)](#startup-activities-s7-1200)
  
[Overview of mechanisms for error handling](Programming%20basics.md#overview-of-mechanisms-for-error-handling)

#### Diagnostics buffer (S7-1200)

##### Function

The diagnostics buffer is part of the system memory of the CPU. It contains the errors detected by the CPU or modules with diagnostics capability. It includes the following events:

- Every mode change of the CPU (for example, POWER UP, change to STOP mode, change to RUN mode)
- Every diagnostics interrupt

The diagnostics buffer of the S7-1200-CPU has a capacity of 50 entries of which the last (most recent) 10 entries are retained following power cycling.

Those entries can only be cleared by restoring the CPU to factory defaults.

You can read the content of the diagnostics buffer with the help of the Online and Diagnostics view.

---

**See also**

[Basic information on the diagnostics buffer](Device%20and%20network%20diagnostics.md#basic-information-on-the-diagnostics-buffer)

## I/O data area (S7-1200)

This section contains information on the following topics:

- [Start address of a module (S7-1200)](#start-address-of-a-module-s7-1200)
- [Access to the I/O addresses (S7-1200)](#access-to-the-io-addresses-s7-1200)

### Start address of a module (S7-1200)

#### Definition

The start address is the lowest byte address of a module. It acts as the initial address of the module user data area.

#### Configuring module start addresses

The addresses used in the user program and the module start addresses are coordinated when the modules are configured.

In the module properties ("I/O addresses" group), you can change the start addresses that were assigned automatically after the modules were inserted.

You can also make a setting that decides whether or not the addresses are located in the process image.

### Access to the I/O addresses (S7-1200)

#### I/O addresses

If you insert a module in the device view, its user data is located in the process image of the S7-1200 CPU (default). The CPU handles the data exchange between the module and the process image area automatically during the update of the process images.

Append the suffix ":P" to the I/O address if you want the program to access the module directly instead of using the process image.

![I/O addresses](images/30690965003_DV_resource.Stream@PNG-en-US.png)

This could be necessary, for example, during execution of a time-sensitive program which also has to control the outputs within the same cycle.

## Basics of program execution (S7-1200)

This section contains information on the following topics:

- [English designation of the OB types (S7-1200)](#english-designation-of-the-ob-types-s7-1200)
- [Events and OBs (S7-1200)](#events-and-obs-s7-1200)
- [Event-based program execution (S7-1200)](#event-based-program-execution-s7-1200)
- [Example of a hardware interrupt event (S7-1200)](#example-of-a-hardware-interrupt-event-s7-1200)

### English designation of the OB types (S7-1200)

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
| TimeOfDay | Time-of-day interrupt OB |
| Status | Status interrupt OB |
| Update | Update interrupt OB |
| Profile | OB for vendor or profile-specific interrupt |
| MC_Interpolator | MC-Interpolator OB |
| MC_Servo | MC-Servo OB |
| MC_PreServo | MC-PreServo OB |
| MC_PostServo | MC-PostServo OB |

### Events and OBs (S7-1200)

#### Events and OBs

The operating system of S7-1200-CPUs is based on events. There are two types of events:

- Events which can start an OB
- Events which cannot start an OB

An event which can start an OB triggers the following reaction:

- It calls the OB you possibly assigned to this event. The event is entered in a queue according to its priority if it is currently not possible to call this OB.
- The default system reaction is triggered if you did not assign an OB to this event.

An event which cannot start an OB triggers the default system reaction for the associated event class.

The user program cycle is therefore based on events, the assignment of OBs to those events, and on the code which is either contained in the OB, or called in the OB.

The following table provides an overview of the events which can start an OB, including the associated event classes and OBs. The table is sorted based on the default OB priority. Priority class 1 is the lowest.

| Event class | OB no. | Number of OBs | Start event | OB priority (default) |
| --- | --- | --- | --- | --- |
| Cyclic program | 1, &gt;= 123 | &gt;= 1 | Starting or end of the last program cycle OB | 1 |
| Startup | 100, &gt;= 123 | &gt;=0 | STOP to RUN transition | 1 |
| Time-of-day interrupt | &gt;= 10 | Max. 2 | Start time has been reached | 2 |
| Time-delay interrupt | &gt;= 20 | Max. 4 | Delay time expired | - 3 - Firmware version V4.0 or higher: 3 for OB20, 4 for OB21, 5 for OB22, 6 for OB23, 3 for OB123 to 32767 |
| Cyclic interrupt | &gt;= 30 | Constant bus cycle time expired | - 8 - Firmware version V4.0 or higher: 8 for OB30, 9 for OB31, 10 for OB32, 11 for OB33, 12 for OB34, 13 for OB35, 14 for OB36, 16 for OB37, 17 for OB38, 7 for OB123 to 32767 |  |
| Hardware interrupt | &gt;= 40 | Max. 50 (more can be used with DETACH and ATTACH) | - Positive edge (max. 16) - Negative edge (max. 16) | 18 |
| - HSC: Count value = reference value (max. 6) - HSC: Count direction changed (max. 6) - HSC: External reset (max. 6) | 18 |  |  |  |
| Status interrupt | 55 | 0 or 1 | CPU has received status interrupt | 4 |
| Update interrupt | 56 | 0 or 1 | CPU has received update interrupt | 4 |
| Manufacturer- or profile-specific interrupt | 57 | 0 or 1 | CPU has received manufacturer-specific or profile-specific interrupt | 4 |
| Diagnostic error interrupt | 82 | 0 or 1 | Module has detected an error | 5 |
| Pull/plug interrupt | 83 | 0 or 1 | Removal/insertion of modules of distributed I/O | 6 |
| Rack error | 86 | 0 or 1 | Error in the I/O system of the distributed I/O | 6 |
| Time error | 80 | 0 or 1 | - Maximum cycle time exceeded - Called OB is still being executed - Time-of-day interrupt missed - Time-of-day interrupt missed during STOP - Queue overflow - Interrupt loss due to high interrupt load | 22 |
|  |  |  |  |  |

The following table describes events which do not trigger an OB start, including the corresponding reaction of the operating system. The table is sorted based on event priority.

| Event class | Event | Event priority | System reaction |
| --- | --- | --- | --- |
| Insert/remove central modules | Insert/remove a module | 21 | STOP |
| I/O access error during process image update | I/O access error during process image update | 22 | Ignore |
| Programming error | Programming error in a block for which you use system reactions provided by the operating system (note: the error handling routine in the block program is executed if you activated local error handling). | 23 | RUN |
| I/O access error | I/O access error in a block for which you use system reactions provided by the operating system (note: the error handling routine in the block program is executed if you activated local error handling). | 24 | RUN |
| Maximum cycle time exceeded twice | Maximum cycle time exceeded twice | 27 | STOP |
|  |  |  |  |

#### Assignment between OBs and events

With the exception of the cyclic program and startup program and event can only be assigned to one OB. However, in certain event classes such as hardware interrupts one and the same OB can be assigned to several events.

The assignment between OBs and events is defined in the hardware configuration. Defined assignments can be changed at runtime by means of ATTACH and DETACH instructions.

#### OB priority and runtime behavior

S7-1200-CPUs support the priority classes 1 (lowest) to 27 (highest). An OB is assigned the priority of its start event.

OBs are always executed on a priority basis: The OBs with the highest priority are executed first. Events of the same priority are processed in order of occurrence.

As of firmware version V4.0 of the S7-1200 CPUs you can specify in the device configuration, under properties of the CPU, if the OBs are interruptible or not. This parameter assignment has an effect on all OBs with exception of the cycle OBs which are always interruptible.

The following applies to S7-1200 CPUs with firmware version &lt; V4.0:

- Any OB with priority &gt;= 2 will interrupt cyclic program execution.
- An OB of priority 2 to 25 cannot be interrupted by any event of priority group 2 to 25. This rule also applies to events of a priority higher than that of the currently active OB. Such events are processed later.
- A time error (priority 26) will interrupt any other OB.

The following applies to S7-1200 CPUs as of firmware version V4.0:

If you do not configure the OBs as interruptible, an OB is always processed completely even if an event of a higher priority occurs during its runtime. Specifically, this means:

- Any OB with priority &gt;= 2 will interrupt cyclic program execution.
- An OB of priority 2 to 25 cannot be interrupted by any event. This rule also applies to events of a priority higher than that of the currently active OB, which also includes a time error. Such events are processed later.

If you do configure the OBs as interruptible and an event of a higher priority occurs during the runtime of an OB, the running OB is interrupted and the OB associated with the occurring event is processed. Once this OB has been completed, processing of the interrupted OB continues. Specifically, this means:

- Any OB with priority &gt;= 2 will interrupt cyclic program execution.
- An OB of priority 2 to 25 can be interrupted by any event whose priority is higher than that of the running OB. This is also true for time errors: A time error (priority 26) will interrupt any OB.

#### OB start information

Certain OBs have start information, while others do not. This is explained in greater detail in the description of the relevant OB.

---

**See also**

[Event-based program execution (S7-1200)](#event-based-program-execution-s7-1200)
  
[Organization blocks (OB)](Programming%20basics.md#organization-blocks-ob)
  
[ATTACH: Attach an OB to an interrupt event (S7-1200, S7-1500)](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#attach-attach-an-ob-to-an-interrupt-event-s7-1200-s7-1500)
  
[DETACH: Detach an OB from an interrupt event (S7-1200, S7-1500)](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#detach-detach-an-ob-from-an-interrupt-event-s7-1200-s7-1500)
  
[Overview of mechanisms for error handling](Programming%20basics.md#overview-of-mechanisms-for-error-handling)

### Event-based program execution (S7-1200)

#### OB priority and runtime behavior

S7-1200-CPUs support the priority classes 1 (lowest) to 27 (highest). An OB is assigned the priority of its start event.

Interrupt OBs can only be interrupted by time error interrupts. This rule also applies to events of a priority higher than that of the currently active OB. That is, only one interrupt OB can be active, with exception of the time error interrupt OB.

Any further event of generated while an interrupt OB is being executed is added to a queue in accordance with its priority. Start events within a queue are processed later based on the chronological order of their occurrence.

#### Program execution on the CPU

Cyclic OBs are interrupted by interrupt OBs.

Reactions to events which start an interrupt OB:

- For CPUs up to firmware version V3: Interrupt OBs can only be interrupted by time error interrupt OBs.
- For CPUs as of firmware version V4: Interrupt OBs can be interrupted by interrupt OBs of a higher priority.

The figure below shows the basic procedure in case interrupt OBs cannot be interrupted (behavior up to firmware version V3):

![Program execution on the CPU](images/14982868491_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① and ② | An event (e.g. a hardware interrupt) calls its associated OB.   A called OB is executed without interruption, including all of its nested blocks. Execution of the cyclic OB is resumed on completion of interrupt processing, provided the queue does not contain any events which trigger an OB start. |
| ③ | An interrupt OB can only be interrupted by a time error interrupt OB (OB 80). |
| ④ | An new alarm-triggering event occurs during interrupt processing.    **Reaction for CPUs up to and including firmware version V3:**    This new event is added to a queue. The queued events successively call their corresponding OBs only after execution of the current interrupt OBs was completed and according to the following rules:   - Events are processed in the order of their priority (starting at the highest priority). - Events of the same priority are processed in chronological order.    **Reaction for CPUs as of firmware version V4:**   You use a CPU parameter to set the interruptibility for CPUs as of firmware version V4. Default behavior: OBs are interruptible. In this case: If the new event has a higher priority than the currently running OB, the OB started by the new event interrupts the currently running OB.  If you disable the option, the interrupt OBs cannot be interrupted. |
| ⑤ | The cyclic OBs are processed one after the other. |

#### Notes on queues

- Every priority class (OBs of the same priority to be called) is assigned a separate queue. The size of those queues is set by default.
- Any new event leading to the overflow of a queue is discarded and therefore lost. A "time error interrupt event" is generated simultaneously. Information identifying the OB that caused the error is included in the start information of the time error interrupt OB (OB 80). A corresponding reaction such as an alarm trigger can be programmed in the time error interrupt OB.

---

**See also**

[Organization blocks (OB)](Programming%20basics.md#organization-blocks-ob)

### Example of a hardware interrupt event (S7-1200)

The function principle of event-oriented program execution in the S7-1200 CPU is described based on the example of a hardware interrupt-triggering module.

#### Process events and their priority

Process events are triggered by the I/O (e.g. at a digital input) and initiate a call of the assigned OB in the S7-1200 CPU. OBs assigned to a process event are called hardware interrupt OBs.

Examples of process events and their priority:

- Process events "rising edge" or "falling edge" at an interrupt-triggering module: The hardware interrupt OB started by such an event is always assigned priority 5.
- Process events from a high-speed counter

  - Count value corresponds to the reference value
  - Change count direction
  - External reset of the high-speed counter

    The hardware interrupt OB started by this event is always assigned priority 6.

The figure below shows the chronological sequence of hardware interrupt execution: In the case of two hardware interrupt events in immediate succession, the second hardware interrupt triggering event is held back in the queue until the first OBx has been processed. The next hardware interrupt triggering event can only start the associated OBx when the OBx has been processed. Additional hardware interrupt triggering events are lined up in the queue according to this principle.

![Process events and their priority](images/14962442123_DV_resource.Stream@PNG-en-US.png)

#### Hardware interrupt execution

| Symbol | Meaning |
| --- | --- |
| ① | A hardware interrupt-triggering event such as a rising edge at the input calls the OB to which it is assigned. |
| ② | If a new event occurs that triggers a hardware interrupt while the OB is executing, this event is entered in a queue. |
| ③ | The new event that triggers a hardware interrupt starts the hardware interrupt OB assigned to the event. |

#### Assigning the interrupt-triggering event

The interrupt-triggering event is assigned to an OB in the input properties of the device view.

- An interrupt-triggering event can only be assigned to a single OB.
- OBs, however, can be assigned to several interrupt-triggering events.   
  This means, for example, that you can assign both the rising and the falling edge to the same interrupt OB in order to trigger the same reaction to any change of the input signal.
- The started OB can interrupt a cycle OB at every instruction. Consistent data access is secured up to dword size.
- You can parameterize module-specific interrupt-triggering events such as a rising and the falling edge at the input.
- Assign the interrupt-triggering event and the OB to be started in the configuration of the interrupt-triggering module. However, within the started hardware interrupt OB you can override this assignment using the DETACH instruction, or assign the same event to a different OB using the ATTACH instruction. This functionality allows a flexible reaction to external process signals.

---

**See also**

[Hardware interrupt OBs (S7-1200)](#hardware-interrupt-obs-s7-1200)
  
[Assigning parameters to hardware interrupt OBs (S7-1200)](#assigning-parameters-to-hardware-interrupt-obs-s7-1200)
  
ATTACH
  
DETACH

## Setting the operating behavior (S7-1200)

This section contains information on the following topics:

- [Changing properties of the modules (S7-1200)](#changing-properties-of-the-modules-s7-1200)
- [CPU properties (S7-1200)](#cpu-properties-s7-1200)
- [Time-of-day functions (S7-1200)](#time-of-day-functions-s7-1200)
- [High-speed counters (S7-1200)](#high-speed-counters-s7-1200)
- [Point-to-point communication (S7-1200)](#point-to-point-communication-s7-1200)
- [Enabling system memory (S7-1200)](#enabling-system-memory-s7-1200)
- [Using clock memory (S7-1200)](#using-clock-memory-s7-1200)
- [Protection &amp; Security (S7-1200)](#protection-security-s7-1200)
- [Activating and deactivating SNMP (S7-1200)](#activating-and-deactivating-snmp-s7-1200)
- [Disabling SNMP: Full program example (S7-1200)](#disabling-snmp-full-program-example-s7-1200)

### Changing properties of the modules (S7-1200)

#### Default settings

When they leave the factory, all hardware components with parameters have default settings suitable for standard applications. These default values allow the hardware components to be used immediately without making any additional settings.

You can, however, modify the behavior and the properties of the hardware components to suit the requirements and circumstances of your application. Hardware components with settable parameters include, for example, communications modules and several analog and digital modules.

#### Setting and loading parameters

When you have selected a hardware component in the device or network view, you can set the properties in the Inspector window. When you save a device configuration with its parameters, data is generated that needs to be loaded on the CPU. This data is transferred to the relevant modules during startup.

#### Properties of the CPUs

The properties of the CPUs have special significance for system behavior. For example for a CPU you can set:

- Interfaces
- Inputs and outputs
- High-speed counters
- Pulse generators
- Startup behavior
- Time-of-day
- Protection level
- Bit memory for system and clock
- Cycle time
- Communications load

The entry possibilities specify what is adjustable and in which value ranges. Fields that cannot be edited are disabled or are not shown in the properties window.

#### Requirement

You have already arranged the hardware components for which you want to change properties on a rack.

#### Procedure

To change the properties and parameters of the hardware components, follow these steps:

1. In the device or network view, select the hardware component or interface that you want to edit.
2. Edit the settings for the selected object:

   - For example in the device view you can edit addresses and names.
   - In the Inspector window additional setting possibilities are available.

You do not need to confirm your entries, the changed values will be applied immediately.

---

**See also**

[Editing properties and parameters](Configuring%20devices%20and%20networks.md#editing-properties-and-parameters)
  
[Introduction to loading a configuration](Configuring%20devices%20and%20networks.md#introduction-to-loading-a-configuration)

### CPU properties (S7-1200)

This section contains information on the following topics:

- [Overview of the CPU properties (S7-1200)](#overview-of-the-cpu-properties-s7-1200)
- [Cycle time and maximum cycle time (S7-1200)](#cycle-time-and-maximum-cycle-time-s7-1200)
- [Cycle loading by communications (S7-1200)](#cycle-loading-by-communications-s7-1200)

#### Overview of the CPU properties (S7-1200)

##### Overview

The following table provides you with an overview of the CPU properties:

| Group | Properties | Description |
| --- | --- | --- |
| General | Project information | General information to describe the inserted CPU. Except for the slot number, you can change this information. |
| Catalog information | Read-only information from the hardware catalog for this CPU. |  |
| Identification &amp; Maintenance | For saving application-specific information such as the name of the plant and the installation location. |  |
| Checksums | To check the identity or integrity of PLC programs.  Blocks in the block folder and text lists are automatically marked with unique checksums when they are compiled. You can easily establish whether the program currently running on the CPU is the same program that you loaded a long time ago or whether the program has been changed in the meantime. The "GetChecksum" instruction is available to read out the checksum while the program is running.  See: [Comparison of PLC programs based on checksums](Comparing%20PLC%20programs.md#comparison-of-plc-programs-based-on-checksums) |  |
| PROFINET interface | General | Name and comment for this PROFINET interface. The name is limited to 110 characters. |
| Ethernet addresses | Select whether the PROFINET interface is networked. If subnets have already been created in the project, they are available for selection in the drop-down list. If not, you can create a new subnet with the "Add new subnet" button.  Information on the IP address, subnet mask and IP router usage in the subnet is available in the IP protocol. If an IP router is used, the information about the IP address of the IP router is necessary.  See: [Assigning addresses and names for PROFINET devices](Configuring%20devices%20and%20networks.md#assigning-addresses-and-names-to-profinet-devices) |  |
| Advanced options | Name, comment and additional setting options of the Ethernet interface port.  Media redundancy settings, such as the media redundancy role (client, manager (Auto) or devices not participating in the media redundancy ring), display of the ring ports and if diagnostic interrupts are generated in case of redundancy errors. A "Domain settings" button is the link to the domain settings of the connected subnet (MRP domain and Sync domain). |  |
| Time synchronization | Settings for time synchronization in the NTP time format.  The NTP (network time protocol) is a general mechanism for synchronizing system clocks in local and global area networks.   In NTP mode, the interface of the CPU sends time queries (in client mode) at regular intervals to NTP servers on the subnet (LAN) and the addresses must be set in the parameters here. Based on the replies from the server, the most reliable and most accurate time is calculated and synchronized. The advantage of this mode is that it allows the time to be synchronized across subnets. The accuracy depends on the quality of the NTP server being used. |  |
| DI#/DO# | General | Name of and comment on the integrated digital inputs of the CPU. |
| Digital inputs | Input delays can be set for digital inputs. The input delays can be set in groups (in each case for 4 inputs).   The detection of a positive and a negative edge can be enabled for each digital input. A name and a hardware interrupt can be assigned to this event.   Depending on the CPU, pulse catches can be activated at various inputs. When the pulse catch is activated, even pulse edges that are shorter than the cycle time of the program are detected. |  |
| Digital outputs | The reaction to a mode change from RUN to STOP can be set for all digital outputs:   The state can either be frozen (corresponds to retain last value) or you set a substitute value ("0" or "1") |  |
| I/O addresses | The address space of the input and output addresses is specified as is the process image. |  |
| AI# | General | Name of and comment on the integrated analog inputs of the CPU. |
| Analog inputs | During noise reduction, the specified integration time suppresses interference frequencies at the specified frequency (in Hz).   The channel address, measurement type, voltage range, smoothing and overflow diagnostics must be specified in the "Channel #" group. The measurement type and voltage range are set permanently to voltage, 0 to 10 V.  Smoothing analog values provides a stable analog signal for further processing. Smoothing analog values can be useful with slow measured value changes, for example, in temperature measurement. The measured values are smoothed with digital filtering. Smoothing is achieved by the module forming mean values from a specified number of converted (digitalized) analog values. The selected level (slight, medium, strong) decides the number of analog signals used to create the mean value.  If overflow diagnostics is enabled, a diagnostics event is generated if an overflow occurs. |  |
| I/O addresses | The address space of the input addresses is specified as is the process image. |  |
| High-speed counter (HSC) | High-speed counter (HSC)# | High-speed counters are typically used to drive counting mechanisms.  See: [Configuring high-speed counters](#configuring-high-speed-counters-s7-1200) |
| Pulse generators (PTO/PWM) | PTO#/PWM# | A pulse generator is activated and can be initialized with project information.  For the configuration of an activated pulse generator, specify the usage as PWM (Pulse Width Modulation) or as PTO (Pulse Train Output).  Specify the output source, time base, pulse width format, cycle time and initial pulse width for PWM. A pulse output is specified as the hardware output. The PWM output is controlled by the CTRL_PWM instruction, see [CTRL_PWM](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#ctrl_pwm-pulse-width-modulation-s7-1200).  Specify the output source for PTO. A pulse output and a direction output are specified as the hardware outputs. A PTO is operated together with a high-speed counter in the "axis of motion" count mode and controlled by the Motion Control technology object (see keyword "Motion Control S7-1200") .   The hardware ID is displayed in the I/O-diagnostics addresses and, if the PWM function is selected, the address space of the output addresses and the process image can be selected. |
| Startup | Startup after POWER ON | Setting the startup characteristics after cycling power.   See: [Principles of the STARTUP mode](#principles-of-the-startup-mode-s7-1200) |
| Comparison of preset configuration and actual configuration | Specifies the startup characteristics of the CPU for situations in which the actual configuration of the S7-1200 station does not correspond to the preset configuration:  - Startup of the CPU only if compatible - Startup of the CPU even if there are differences   With the "Startup CPU only if compatible" setting, a module in a configured slot must be compatible with the configured module.   Compatible means that the module that is present matches the number of inputs and outputs and must match with respect to its electrical and functional properties. A compatible module must be able to completely replace a configured module; it may be more capable, but not less capable.   Example for the "Startup CPU only if compatible" setting: A CPU can be a compatible replacement for a CPU of the same type with a lower firmware version. An input module with 32 digital inputs can be a compatible replacement for a signal module with 16 digital inputs. The CPU starts up when the configured module or a compatible module is plugged in. The CPU does not start up if an incompatible module is inserted.  Example of the "Startup CPU even if mismatch" setting: Instead of a configured digital input module, an analog output module is plugged in or no module is present in this slot. Although the configured inputs cannot be accessed, the CPU starts up.  Note in this case that the user program cannot function correctly and take the appropriate measures. |  |
| Configuration time for central and distributed I/O | Specifies a maximum period (standard: 60000 ms) in which the central I/O and distributed I/O must start up. (The CMs and CPs are supplied with voltage and communication parameters during the CPU startup. This configuration time provides a time period during which I/O modules connected to the CM or CP must start up.)  The CPU switches to RUN as soon as the central I/O and the distributed I/O has started and is ready for operation, regardless of the "Parameter assignment time for central and distributed I/O" parameter. If the central I/O and distributed I/O has not started up during this period, the CPU switches to RUN without the central I/O and distributed I/O. |  |
| Cycle | Maximum cycle time and minimum cycle time. | Specification of a maximum cycle time or a fixed minimum cycle time.  If the cycle time exceeds the maximum cycle time, the CPU goes to STOP mode.   See: [Cycle time and maximum cycle time](#cycle-time-and-maximum-cycle-time-s7-1200) |
| Communication load | Maximum allocation of the cycle for communication (as a percentage) | Controls the duration of communication processes that always also extend the cycle time, within certain limits. Examples of communication processes include: Transferring data to another CPU or loading blocks (initiated via the PC).  See: [Cycle loading by communications](#cycle-loading-by-communications-s7-1200) |
| System and clock memory | System memory bits and clock memory bits | You use system memory bits for the following scans:   - Is the current cycle the first since cycling power? - Have there been any diagnostics state changes compared with the previous cycle? - Scan for "1" (high) - Scan for "0" (low)   Clock memory bits change their values at specified periodic intervals.  See: [Enabling system memory](#enabling-system-memory-s7-1200)  See: [Using clock memory](#using-clock-memory-s7-1200) |
| Web server | - | Enables and configures the Web server function.  See: [Enabling the Web server](Configuring%20the%20Web%20server%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#enable-the-web-server-s7-300-s7-400-s7-1500) |
| Automatic update | Sends the requested web page with current CPU data periodically to the web browser. Enter the period duration under "Update interval". Automatic update can only be activated if the web server is enabled.  See: [Activate automatic update](Configuring%20the%20Web%20server%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#activate-automatic-update-s7-300-s7-400-s7-1500) |  |
| User Management | You enter the user names with their access rights here.  - Everyone: pre-defined user whose access rights you assign using a drop-down list. The "Everyone" user is a user who does not log on with a password for Web access. - User#: Editable name for a user for whom you assign access rights and a password. As soon as you click in a line below "Everyone", a preset name is displayed that you can change.   Each user can be assigned different access rights via a drop-down list.  There are access rights that are connected to each other. Example: When you activate the access right "Perform firmware update", the access rights "Change operating mode" and "... query diagnostics" are activated automatically. These two rights are required to perform a firmware update from the Web server.  See: [User list](Configuring%20the%20Web%20server%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#user-administration-s7-300-s7-400-s7-1500) |  |
| Watch tables | Allows you to create watch tables and defines access to those tables. |  |
| User-defined web pages | Allows access to freely-designed web pages of the CPU via a web browser.  See: [What you need to know about user pages](Configuring%20the%20Web%20server%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#what-you-need-to-know-about-user-pages-s7-300-s7-400-s7-1500) |  |
| Entry page | Allows you to select the entry page. |  |
| Overview of interfaces | Table of all modules with their Ethernet interfaces providing Web server functionality for this device.  Here, you can permit or deny access to the Web server over the interface for each Ethernet interface of the device (CPU, CP or CM). |  |
| User interface languages | - | If you want to use translations of project texts for the Web server, you need to assign the project language to the languages for the Web server (number depends on the CPU). This specifies the project languages that are displayed when the Web server is accessed.  Example: You assign the project language "German (Luxembourg)" to the Web server language "German" by selecting it from the drop-down list. Enable the project language under "Languages &amp; resources &gt; Project languages" in the project tree to make it available for selection in the drop-down list. |
| Time | Local time and daylight saving time | Setting of the time zone in which the CPU is operated and setting of the daylight-saving/standard time changeover. |
| Protection &amp; Security | Protection of the PLC configuration data | Configure here the protection of the confidential PLC configuration data.  See: [Protection of confidential configuration data](#protection-of-confidential-configuration-data-s7-1200) |
| Access level | Setting the read/write protection and the password for access to the CPU.  See: [Setting options for the protection level (FW V1 to V3)](#setting-options-for-the-protection-level-fw-v1-to-v3-s7-1200)  See: [Setting options for the protection (FW as of V4)](#setting-options-for-the-protection-fw-as-of-v4-s7-1200) |  |
| Connection mechanisms | Enabling access over PUT/GET communication. |  |
| Security event | Enabling group alarms for security events and specifying a monitoring time (interval). |  |
| External load memory | Disables copying from the internal to the external [load memory](#load-memory-s7-1200). |  |
| Configuration control | - | Enables configuration control. Allows a configuration change in the user program within certain limits.  See: [Configuration control](Configuring%20automation%20systems.md#important-information-regarding-configuration-control-option-handling-s7-1200) |
| Connection resources | - | Provides an overview of the assigned reserved and dynamic resources for the CPU connections. The resources currently used are also displayed in the online view.  See: [Use of connection resources](Configuring%20devices%20and%20networks.md#connection-resources-and-communication-type) |
| Address overview | - | Tabular representation of all addresses used by the CPU for integrated inputs/outputs as well as for the inserted modules. Addresses that are not used by any module are represented as gaps.   The view can be filtered according to   - Input addresses - Output addresses - Address gaps |

---

**See also**

[Specifying input and output addresses (S7-1200)](Configuring%20automation%20systems.md#specifying-input-and-output-addresses-s7-1200)
  
[Assigning parameters to hardware interrupt OBs (S7-1200)](#assigning-parameters-to-hardware-interrupt-obs-s7-1200)
  
[Access to the I/O addresses (S7-1200)](#access-to-the-io-addresses-s7-1200)
  
Configuration - General
  
[Addressing modules (S7-1200)](Configuring%20automation%20systems.md#addressing-modules-s7-1200)
  
[Special features during startup (S7-1200)](#special-features-during-startup-s7-1200)

#### Cycle time and maximum cycle time (S7-1200)

##### Function

The cycle time is the time that the operating system requires to execute the cyclic program and all the program sections that interrupt this cycle. The program execution can be interrupted by:

- Time errors and 2xMaxCycleTime errors
- System activities, e.g., process image updating

The cycle time (Tcyc) is therefore not the same for every cycle.

The following schematic shows an example of different cycle times (TZ1 ≠ TZ2) for S7-1200 CPUs:

![Function](images/25392479371_DV_resource.Stream@PNG-en-US.png)

In the current cycle, the cyclic OB used here (e.g. OB 1) will be interrupted by a time error (e.g. OB 80). Following the cyclic OB, the next cycle OB 201 is processed.

##### Maximum cycle time

The operating system monitors the execution time of the cyclic program for a configurable upper limit known as the maximum cycle time. You can restart this time monitoring at any point in your program by calling the RE_TRIGR instruction.

If the cyclic program exceeds the maximum cycle time, the operating system will attempt to start the time error OB (OB 80). If the OB is not available, the S7-1200 CPU reacts as follows:

- CPUs with firmware version V1.x to V3.x: The CPU remains in RUN mode.
- CPUs with firmware version as of V4.x: The CPU changes to STOP mode

In addition to monitoring the runtime for overshooting of the maximum cycle time, adherence to a minimum cycle time is guaranteed. To do this, the operating system delays the start of the new cycle until the minimum cycle time has been reached. During this waiting time, new events and operating system services are processed.

If the maximum cycle time is exceeded a second time, for example while the time error OB is being processed (2xMaxCycleTime error), the CPU changes to STOP mode.

#### Cycle loading by communications (S7-1200)

##### Function

The cycle time of the CPU can be extended due to communications processes. These communications processes include for example:

- Transferring data to another CPU
- Loading of blocks initiated by a programming device

You can control the duration of these communications processes to some extent using the CPU parameter "Cycle load due to communication".

In addition to communications processes, test functions also extend the cycle time. The "Cycle load due to communication" parameter can be used to influence the duration.

##### How the parameter works

You use the "Cycle load due to communication" parameter to enter the percentage of the overall CPU processing capacity that can be available for communications processes. This CPU processing capacity is now available at all times for communication. This processing capacity can be used for program execution when not required for communication.

##### Effect on the actual cycle time

The "Cycle load due to communication" parameter can be used to extend the cycle time of the cyclic organization block (e.g., OB 1) by a factor calculated according to the following formula:

![Effect on the actual cycle time](images/13257804683_DV_resource.Stream@PNG-en-US.png)

The formula does not take into account the effect of asynchronous events such as hardware interrupts or cyclic interrupts on the cycle time.

If the cycle time is extended due to communication processes, more asynchronous events may occur within the cycle time of the cyclic organization block. This extends the cycle still further. The extension depends on how many events occur and how long it takes to process them.

##### Example 1 – no additional asynchronous events:

If the "Cycle load due to communication" parameter is set to 50%, this can cause the cycle time of the cyclic organization block to increase by up to a factor of 2.

##### Example 2 – additional asynchronous events:

For a pure cycle time of 500 ms, a communication load of 50% can result in an actual cycle time of up to 1000 ms, provided that the CPU always has enough communications jobs to process. If, parallel to this, a cyclic interrupt with 20 ms processing time is executed every 100 ms, this cyclic interrupt would extend the cycle by a total of 5*20 ms = 100 ms without communication load. That is, the actual cycle time would be 600 ms. Because a cyclic interrupt also interrupts communications, it affects the cycle time by adding 10 * 20 ms at 50 % communication load. That is, in this case, the actual cycle time amounts to 1200 ms instead of 1000 ms.

> **Note**
>
> Observe the following:
>
> - Check the effects of changing the value of the "Cycle load due to communication" parameter while the system is running.
> - You must always consider the communication load when setting the minimum cycle time as time errors will otherwise occur.

##### Recommendations

- Increase this value only if the CPU is used primarily for communication purposes and the user program is not time critical.
- In all other situations you should only reduce this value.

### Time-of-day functions (S7-1200)

This section contains information on the following topics:

- [Basic principles of time of day functions (S7-1200)](#basic-principles-of-time-of-day-functions-s7-1200)
- [Setting and reading the time of day (S7-1200)](#setting-and-reading-the-time-of-day-s7-1200)
- [Assigning the clock parameters (S7-1200)](#assigning-the-clock-parameters-s7-1200)

#### Basic principles of time of day functions (S7-1200)

All S7-1200 CPUs are equipped with an internal clock. The backup supports the display of the correct time for up to 10 hours if the power supply is interrupted.

##### Time-of-day format

The clock always shows the time of day with a resolution of 1 millisecond and the date including the day of the week. The time adjustment for daylight-saving time is also taken into account.

#### Setting and reading the time of day (S7-1200)

##### Setting and reading the time with instructions

You can set, start and read the time-of-day and date on the CPU clock with the following instructions in the user program:

- Set the time-of-day: "WR_SYS_T"
- Read time of day "RD_SYS_T"
- Read local time "RD_LOC_T"
- Set time zone "SET_TIMEZONE"

##### Manual setting

You can also read and set the time-of-day manually in the online and diagnostics view under "Functions &gt; Set time-of-day".

---

**See also**

[WR_SYS_T: Set time-of-day (S7-1200, S7-1500)](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#wr_sys_t-set-time-of-day-s7-1200-s7-1500)
  
[RD_SYS_T: Read time-of-day (S7-1200, S7-1500)](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#rd_sys_t-read-time-of-day-s7-1200-s7-1500)
  
[RD_LOC_T: Read local time (S7-1200, S7-1500)](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#rd_loc_t-read-local-time-s7-1200-s7-1500)
  
[SET_TIMEZONE: Set time zone (S7-1200, S7-1500)](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#set_timezone-set-time-zone-s7-1200-s7-1500)

#### Assigning the clock parameters (S7-1200)

##### Clock parameters

The clock parameters allow you to make the following settings:

- Enable time synchronization via NTP server

  Select this check box if you want the internal clock to be synchronized using the NTP synchronization mode.
- Network time server

  The IP addresses of up to four NTP servers need to be configured.
- Update interval

  The update interval defines the interval between time queries.

---

**See also**

[NTP method - configuration](Communications%20modules%20and%20network%20components.md#ntp-method---configuration)

### High-speed counters (S7-1200)

This section contains information on the following topics:

- [General information on high-speed counters (S7-1200)](#general-information-on-high-speed-counters-s7-1200)
- [Interdependency of the counter mode and counter inputs (S7-1200)](#interdependency-of-the-counter-mode-and-counter-inputs-s7-1200)
- [Configuring high-speed counters (S7-1200)](#configuring-high-speed-counters-s7-1200)

#### General information on high-speed counters (S7-1200)

##### Introduction

High-speed counters are typically used to drive counting mechanisms in which a shaft turning at a constant speed is equipped with an incremental step encoder. The incremental step encoder ensures a certain number of count values per rotation and a reset pulse once per rotation. The clock memory bit(s) and the reset pulse of the incremental step encoder supply the inputs for the high-speed counter.

The various S7-1200 CPUs have differing numbers of high-speed counters available:

| S7-1200 CPU | Number of HSCs | HSC designation |
| --- | --- | --- |
| CPU 1211C | 3 (with digital signal board 4)* | HSC1…3 (and HSC5)* |
| CPU 1212C | 4 (with digital signal board 5)* | HSC1…4 (and HSC5)* |
| CPU 1214C  CPU 1215C  CPU 1217C | 6 | HSC1…6 |

* with DI2/DO2 signal board

##### How it works

The first of several default values is loaded on the high-speed counter. The required outputs are enabled for the time during which the current value of the counter is lower than the default value. The counter is set up so that an interrupt occurs if the current value of the counter is equal to the default value or when the counter is reset.

If the current value is equal to the default value and an interrupt event results, a new default value is loaded and the next signal state is set for the outputs. If an interrupt event occurs because the counter is reset, the first default value and the first signal states of the outputs are set and the cycle repeated.

Since the interrupts occur much less frequently than the high-speed counter counts, a precise control of the fast operations can be implemented with only a slight influence on the overall cycle of the automation system. Since you can assign specific interrupt programs to interrupts, each new default can be loaded in a separate interrupt program allowing simple control of the state.

> **Note**
>
> You can also process all interrupt events in a single interrupt program.

##### Count algorithms of the various counters

All counters work in the same way, however some high-speed counters do not support all count algorithms. There are four basic count algorithms:

- Single-phase counter with internal direction control
- Single-phase counter with external direction control
- 2-phase counter with 2 clock inputs
- A/B counter

Each high-speed counter can be used with or without a reset input. If the reset input is activated, this resets the current value. The current value remains reset until the reset input is deactivated.

---

**See also**

[Configuring high-speed counters (S7-1200)](#configuring-high-speed-counters-s7-1200)
  
[Interdependency of the counter mode and counter inputs (S7-1200)](#interdependency-of-the-counter-mode-and-counter-inputs-s7-1200)

#### Interdependency of the counter mode and counter inputs (S7-1200)

##### General information on counter mode and counter inputs

You can assign not only the counter modes and counter inputs to the high-speed counters but also functions such as clock pulse generator, direction control, and reset. The following rules apply:

- An input cannot be used for two different functions.
- If an input is not required by the current counter mode of the defined high-speed counter, it can be used other purposes.

If, for example, you set HSC1 to counter mode 1, in which inputs I0.0 and I0.3 are required, you can use I0.1 for edge interrupts or for HSC2.

If, for example, you set HSC1 and HSC5, inputs I0.0 (HSC1) and I1.0 (HSC5) are always used with the counting and frequency counter modes. As a result, these two inputs are not available for any other functions when counters are operated.

You have additional inputs available if you use a digital signal board.

##### Overview of the interdependency of counter mode and counter inputs

| Counter mode | Description | Inputs |  |  |
| --- | --- | --- | --- | --- |
|  | HSC1 | I0.0 (CPU)  I4.0 (signal board) | I0.1 (CPU)  I4.1 (signal board) | I0.3 (CPU)  I4.3 (signal board) |
| HSC2 | I0.2 (CPU)  I4.2 (signal board) | I0.3 (CPU)  I4.3 (signal board) | I0.1 (CPU)  I4.1 (signal board) |  |
| HSC3* | I0.4 (CPU) | I0.5 (CPU) | I0.7 (CPU) |  |
| HSC4 (CPU 1212/14/15/17C only) | I0.6 (CPU) | I0.7 (CPU) | I0.5 (CPU) |  |
| HSC5 (CPU 1214/15/17C only)** | I1.0 (CPU)  I4.0 (signal board) | I1.1 (CPU)  I4.1 (signal board) | I1.2 (CPU)  I4.3 (signal board) |  |
| HSC6 (CPU 1214/15/17C only)** | I1.3 (CPU) | I1.4 (CPU) | I1.5 (CPU) |  |
| Counting / frequency | Single-phase counter with internal direction control | Clock pulse generator | - | - |
| Counting | Resetting |  |  |  |
| Counting / frequency | Single-phase counter with external direction control | Clock pulse generator | Direction | - |
| Counting | Resetting |  |  |  |
| Counting / frequency | 2-phase counter with 2 clock inputs | Clock pulse generator forwards | Clock pulse generator backwards | - |
| Counting | Resetting |  |  |  |
| Counting / frequency | A/B counter | Clock pulse generator A | Clock pulse generator B | - |
| Counting | Resetting |  |  |  |
| Motion axis | Pulse generators PWM/PTO | HSC1 and HSC2 support the motion axis count mode for the PTO1 and PTO2 pulse generators:  - For PTO1, HSC1 evaluates the Q0.0 outputs for the number of pulses. - For PTO2, HSC2 evaluates the Q0.2 outputs for the number of pulses.   Q0.1 is used as the output for the motion direction. |  |  |

* HSC3 can only be used for CPU 1211 without a reset input

** HSC5 can be also be used for CPU 1211/12 if a DI2/DO2 signal board is used

---

**See also**

[General information on high-speed counters (S7-1200)](#general-information-on-high-speed-counters-s7-1200)
  
[Configuring high-speed counters (S7-1200)](#configuring-high-speed-counters-s7-1200)

#### Configuring high-speed counters (S7-1200)

##### Requirement

An S7-1200 CPU has been inserted in the hardware configuration.

##### Procedure

To configure a high-speed counter, follow these steps:

1. Select an S7-1200 CPU in the device or network view.
2. Click on the required high-speed counter under "Properties &gt; High-speed counter (HSC)" in the Inspector window:

   - CPU 1211C: HSC1 to HSC3 (also HSC5 with a DI2/DO2 signal board)
   - CPU 1212C: HSC1 to HSC4 (also HSC5 with a DI2/DO2 signal board)
   - CPU 1214C / 1215C / 1217C: HSC1 to HSC6
3. Enable the high-speed counter in the "General" parameter group using the relevant check box.

   In "Project information" you can enter a name and a comment for the counter.
4. Define the functionality of the counter in the "Function" parameter group:

   - Count mode: Select one of the following functions of the counter from the drop-down list:

     - Counting (decides the number of pulses)

     - Period (measurement of the period of pulses)

     - Frequency (measurement of the frequency of pulses)

     - Motion Control (use counter for motion control).
   - Operating phase: Select from the drop-down list how the counter will be operated:

     - Single phase (one clock input for counting, up and down can be set via the direction input)

     - Two-phase (one clock input for counting up, one clock input for counting down)

     - A/B counter (two clock inputs with phase-shifted pulses, single count value)

     -A/B counter fourfold (two clock inputs with phase-shifted pulses, quadruple count value)
   - Input source (only in firmware versions lower than 4.0): As the input source for the count pulses, select a CPU input or an input of a signal board.
   - Count direction is specified by: If the operating phase "Single phase" is set, you can choose whether the user program decides the count direction (instruction CTRL_HSC, parameters DIR and NEW_DIR) or a digital input.
   - Initial count direction: If the user program is set as the direction control for the count direction, you can select the count direction at the start of counting.
   - Frequency meter period: If frequency or period is set as the count mode, you can select the duration of the frequency measurement periods in the drop-down list.
5. Specify the initial values and reset condition of the counter in the "Reset to initial values" parameter group:

   - Initial counter value: Enter a start value for the counter.
   - Initial reference value: Enter a reference value.

     The current count is compared with this reference value: When the current counter value is equal to the reference value, an event is triggered (if enabled in "Event configuration").

   Here, you can also set whether the counter uses a reset input and the counter resets the current count at a high or low level at the reset input.
6. The following events can be enabled in the "Event configuration" parameter group:

   - Counter value equal to reference value
   - External reset
   - Direction change

   You can assign a hardware interrupt OB to each of these events under "Hardware interrupt". Alternatively, assign a hardware interrupt OB to every event in the user program ("ATTACH" instruction).

   Result: When an event is triggered, the CPU executes the assigned hardware interrupt OB (according to the configured priority).

   The names of the events and the hardware interrupts can be changed.
7. In the parameter group "Hardware inputs", hardware inputs are already entered. You can accept these. Alternatively, click the "..." button beside "Clock generator up", "Clock generator down" or "Reset input" and select an input.

   Note: With earlier firmware versions (lower than V4.0), the hardware inputs were preset and could not be changed.
8. In the "I/O addresses" area, the following parameters can be set:

   - Start address: The CPU writes the counter status to the address area with the set start address (data type DInt).
   - Organization block: Assignment of this address area to an organization block.
   - Process image: Assignment of the address area to a process image partition (PIP). The default setting is automatic update (PIP0).

**Note**

If you use a CPU 1211C or CPU 1212C with a DI2/DO2 signal board, you can also enable the high-speed counter HSC5.

**Note**

When you activate the pulse generators and operate them as PTO (to control stepper motors), high-speed counters are required.

With firmware versions as of V3.0, the CPU uses internal (additional) HSCs.

With firmware versions lower than V3.0, the CPU uses HSC1 for PTO1 and HSC2 for PTO2. The counters are then no longer available for other counting tasks.

##### Result

You have now adapted the parameters of the high-speed counter to the requirements of your project.

---

**See also**

[General information on high-speed counters (S7-1200)](#general-information-on-high-speed-counters-s7-1200)
  
[Interdependency of the counter mode and counter inputs (S7-1200)](#interdependency-of-the-counter-mode-and-counter-inputs-s7-1200)

### Point-to-point communication (S7-1200)

This section contains information on the following topics:

- [Overview of point-to-point communication (S7-1200)](#overview-of-point-to-point-communication-s7-1200)
- [Using RS-232 and RS-485 communications modules (S7-1200)](#using-rs-232-and-rs-485-communications-modules-s7-1200)
- [Configuring a communications port (S7-1200)](#configuring-a-communications-port-s7-1200)
- [Setting data flow control (S7-1200)](#setting-data-flow-control-s7-1200)
- [Configuration of message transfer (S7-1200)](#configuration-of-message-transfer-s7-1200)
- [User-programmed communication with RS-232 devices (S7-1200)](#user-programmed-communication-with-rs-232-devices-s7-1200)
- [Making the settings for sending (S7-1200)](#making-the-settings-for-sending-s7-1200)
- [Specifying the start of the message (S7-1200)](#specifying-the-start-of-the-message-s7-1200)
- [Specifying the end of the message (S7-1200)](#specifying-the-end-of-the-message-s7-1200)

#### Overview of point-to-point communication (S7-1200)

PtP communication is communication via a serial interface that uses standardized UART data transmission (Universal Asynchronous Receiver/Transmitter). The S7-1200 uses communications modules with an RS-232 or RS-485 interface to establish PtP communication.

##### Functions of point-to-point communication

Point-to-point communication (PtP) allows numerous applications:

- Direct transmission of information to an external device, for example a printer or a barcode reader
- Reception of information from external devices such as barcode readers, RFID readers, cameras and third-party optical systems as well as many other devices.
- Exchange of information with third-party devices, for example GPS devices, radio modems and many others

##### The Freeport protocol

The S7-1200 supports the Freeport protocol for character-based serial communication. Using Freeport communication, the data transmission protocol can be configured entirely by the user program.

Siemens provides libraries with Freeport communication functions that you can use in your user program:

- USS Drive protocol
- Modbus RTU Master protocol
- Modbus RTU Slave protocol

---

**See also**

[Configuring a communications port (S7-1200)](#configuring-a-communications-port-s7-1200)

#### Using RS-232 and RS-485 communications modules (S7-1200)

##### Communications modules with RS-232 and RS-485 interfaces

In an S7-1200 CPU, you can use two different communications modules:

- RS-232 communications module
- RS-485 communications module

The communications modules can be connected to the S7-1200 CPU via the I/O channel on the left. You can plug in up to three different modules.

##### Properties of the communications modules

The communications modules have the following features:

- Support of the Freeport protocol
- Configuration by the user program with the aid of expanded instructions and library functions

#### Configuring a communications port (S7-1200)

##### Configuring a communications port

After you have inserted a communications module with an RS-232 or RS-485 interface, you then set the interface parameters. You set the parameters for the interface either in the properties of the interface or you control the interface parameters from the user program using the PORT_CFG instruction. The following description relates to the graphic configuration.

> **Note**
>
> If you use the user program to change the port setting, the settings of the graphic configuration are overwritten.
>
> You should also keep in mind that the settings made by the user program are not retained if there is a power down.

##### Requirement

- A communications module is already plugged in.
- You are in the device view.

##### Procedure

To configure the communications port, proceed as follows:

1. Select the interface in the graphic representation in the device view.

   The properties of the interface are displayed in the Inspector window.
2. Select the "Port configuration" group in the area navigation of the Inspector window.

   The settings of the port are displayed.
3. From the "Transmission speed" drop-down list, select the speed for the data transmission. With user-programmed communication, remember the influence of the transmission speed on the changeover time.
4. From the "Parity" drop-down list, select the type of detection of bad information words.
5. Using the "Data bits" drop-down list, decide whether a character consists of eight or seven bits.
6. From the "Stop bit" drop-down list, select how many bits will identify the end of a transmitted word.
7. From the "Flow control" drop-down list, select the method for ensuring a trouble-free data stream between sender and receiver. This parameter can only be set for the RS-232 interface.

   - Enter a HEX value in the "XON character" box that will cause the transmission of the message to be continued when it is detected. This parameter can only be set for software-controlled data flow control.
   - Enter a HEX value in the "XOFF character" box that will cause the transmission of the message to be suspended for the set wait time. This parameter can only be set for software-controlled data flow control.
8. In the "Wait time" box, enter a wait time in ms that must be kept to after the end of the message before the next transmission can start.

> **Note**
>
> You can configure the interface in the network view as well. To do so, you must first select the communication module in the tabular network view and then select the interface in the Inspector window. Then you can continue as described above.

---

**See also**

[Setting data flow control (S7-1200)](#setting-data-flow-control-s7-1200)

#### Setting data flow control (S7-1200)

##### Data flow control

Data flow control is a method that ensures a balanced send and receive behavior. In the ideal situation, the intelligent control does not allow data to be lost. It ensures that a device does not send more information than the receiving partner can process.

There are two methods of data flow control:

- Hardware-controlled data flow control
- Software-controlled data flow control

With both methods, the DSR signals of the communications partners must be active at the beginning of transmission. If the DSR signals are inactive, the transmission is not started.

The RS-232 communications module can handle both methods. The RS-485 communications module does not support data flow control.

##### Hardware-controlled data flow control

Hardware-controlled data flow control uses the request to send (RTS) and clear to send (CTS) signals. With the RS-232 communications module, the RTS signal is transmitted via the output by pin 7. The CTS signal is received via pin 8.

If hardware-controlled data flow control is enabled, the RTS signal is then always set to activated when data is sent. At the same time, the CTS signal is monitored to check whether the receiving device can accept data. If the CTS signal is active, the module can transfer data until the CTS signal becomes inactive. If the CTS signal is inactive, the data transfer must be suspended for the set wait time. If the CTS signal is still inactive after the set wait time, the data transfer is aborted and an error is signaled back to the user program.

##### Data flow control using hardware handshaking

If data flow control is controlled by hardware handshaking, the sending device sets the RTS signal to active as default. A device such as a modem can then transfer data at any time. It does not wait for the CTS signal of the receiver. The sending device itself monitors it own transmission by sending only a limited number of frames (characters), for example to prevent overflow of the receive buffer. If there is nevertheless an overflow, the transferring device must hold back the message and signal an error back to the user program.

##### Software-controlled data flow control

Software-controlled data flow control uses certain characters within the messages and these control the transfer. These characters are ASCII characters selected for XON and XOFF.

XOFF indicates when a transmission must be suspended. XON indicates when a transmission can be continued.

If the sending device receives the XOFF character, it must suspend sending for the selected wait time. If the XON character is sent after the selected wait time, the transfer is continued. If no XON character is received after the wait time, an error is signaled back to the user program.

Software data flow control requires full duplex communication because the receiving partner needs to send the XON character during the ongoing transfer.

---

**See also**

[Configuring a communications port (S7-1200)](#configuring-a-communications-port-s7-1200)

#### Configuration of message transfer (S7-1200)

##### User-programmed communication

You can control the data traffic between a communications module and a device connected externally via the serial interface using your own mechanisms. If you want to do this, you will need to define a communications protocol yourself. In freely programmable communication, ASCII and binary protocols are supported for message transfer.

Within the communications protocol, you will need to specify the criteria by which the start and end of a transferred message can be recognized in the data stream.

User-programmed communication can only be activated in RUN mode. If there is a change to STOP mode, the user-programmed communication is stopped.

##### Specifying the communications protocol

You can specify the communications protocol as follows:

- With the user program

  - The behavior when sending data is controlled by the SEND_CFG instruction.
  - The behavior when receiving data is controlled by the RCV_CFG instruction.
- Using parameter settings set graphically in the Inspector window

  > **Note**
  >
  > If you change the communications protocol from the user program, the settings of the graphic configuration are overwritten.
  >
  > You should keep in mind that the settings made by the user program are not retained if there is a power down.

---

**See also**

[User-programmed communication with RS-232 devices (S7-1200)](#user-programmed-communication-with-rs-232-devices-s7-1200)
  
[Making the settings for sending (S7-1200)](#making-the-settings-for-sending-s7-1200)
  
[Specifying the start of the message (S7-1200)](#specifying-the-start-of-the-message-s7-1200)
  
[Specifying the end of the message (S7-1200)](#specifying-the-end-of-the-message-s7-1200)

#### User-programmed communication with RS-232 devices (S7-1200)

##### RS-232/PIP multi-master cable and user-programmed communication with RS-232 devices

Using the RS-232/PIP multi-master cable and user-programmed communication, you can connect a wide variety of RS-232-compliant devices to the communications modules of the S7-1200. The cable must, however, be set to the "PIP/user-programmed communication" mode.

##### Settings on the cable

The switches on the cable must be set as follows:

- Switch 5 must be set to 0
- Switch 6 sets either the local mode (DCE) or the remote mode (DTE):

  - Switch set to 0 for the local mode
  - Switch set to 1 for the remote mode

##### Changing over between send and receive mode

The RS-232/PIP multi-master cable is in send mode when data is sent from the RS-232 interface to the RS-485 interface. The cable is in receive mode when it is idle or when data is sent from the RS-485 interface to the RS-232 interface. The cable changes from receive to send mode immediately when it detects characters on the RS-232 send line.

##### Supported transmission speeds

The RS-232/PIP multi-master cable supports transmission rates between 1200 baud and 115.2 kbaud. The RS-232/PIP multi-master cable can be set to the required transmission rate using the DIP switch on the PC/PIP cable.

The following table shows the switch settings for the various transmission speeds:

| Transmission speed | Switchover time | Settings (1 = up) |
| --- | --- | --- |
| 115200 bps | 0.15 ms | 110 |
| 57600 bps | 0.3 ms | 111 |
| 38400 bps | 0.5 ms | 000 |
| 19200 bps | 1.0 ms | 001 |
| 9600 bps | 2.0 ms | 010 |
| 4800 bps | 4.0 ms | 011 |
| 2400 bps | 7.0 ms | 100 |
| 1200 bps | 14.0 ms | 101 |
|  |  |  |

The cable returns to receive mode when the RS-232 send line is idle for a certain time that is defined as the changeover time of the cable. The set transmission speed influences the changeover time as shown in the table.

##### Influence of the changeover time

When working with an RS-232/PIP multi-master cable in a system in which user-programmed communication is used, the program must take into account the changeover time for the following reasons:

- The communications module reacts to messages sent by the RS-232 device.

  Once the communications module has received a request from the RS-232 device, it must delay the reaction message for a period that is equal to or longer than the changeover time of the cable.
- The RS-232 device reacts to messages sent by the communications module.

  Once the communications module has received a reaction message from the RS-232 device, it must delay the next request message for a period that is equal to or longer than the changeover time of the cable.

In both situations, the RS-232-PIP multi-master cable has enough time to change from send to receive mode so that the data can be sent from the RS-485 interface to the RS-232 interface.

---

**See also**

[Configuration of message transfer (S7-1200)](#configuration-of-message-transfer-s7-1200)
  
[Making the settings for sending (S7-1200)](#making-the-settings-for-sending-s7-1200)
  
[Specifying the start of the message (S7-1200)](#specifying-the-start-of-the-message-s7-1200)
  
[Specifying the end of the message (S7-1200)](#specifying-the-end-of-the-message-s7-1200)

#### Making the settings for sending (S7-1200)

##### Sending messages

You can program pauses between individual messages.

The following table shows which pauses can be set:

| Parameter | Definition |
| --- | --- |
| RTS ON delay | You can set the time that must elapse after the send request RTS (request to send) before the actual data transfer starts. |
| RTS OFF delay | You can set the time that must elapse after the complete transfer before RTS signal is deactivated. |
| Send pause at the start of the message | You can specify that a pause is sent at the start of every message transfer when the RTS ON delay has elapsed.  The pause is specified in bit times. |
| Send Idle Line after a pause | You can make a setting so that following a selected pause at the start of the message, the "Idle Line" signal is output to signal that the line is not in use. To enable the parameter, "Send pause at message start" must be set.  The duration of the "Idle Line" signal is specified in bit times. |

---

**See also**

[Specifying the start of the message (S7-1200)](#specifying-the-start-of-the-message-s7-1200)
  
[Specifying the end of the message (S7-1200)](#specifying-the-end-of-the-message-s7-1200)
  
[User-programmed communication with RS-232 devices (S7-1200)](#user-programmed-communication-with-rs-232-devices-s7-1200)

#### Specifying the start of the message (S7-1200)

##### Recognizing the start of the message

To signal to the receiver when the transfer of a message is completed and when the next message transfer starts, criteria must be specified in the transmission protocol to identify the end and start of a message.

If a criterion is met that indicates the start of a message, the receiver starts searching the data stream for criteria that mean the end of the message.

There are two different methods for identifying the start of a message:

- Starting with any character:

  Any character can defined the start of a message. This is the default method.
- Starting with a specific condition:

  The start of a message is identified based on selected conditions.

##### Conditions for detecting the start of a message

The following table shows the various options for defining the start of a message:

| Parameter | Definition |
| --- | --- |
| Recognize start of message by line break | The receiver recognizes a line break when the received data stream is interrupted for longer than one character. If this is the case, the start of the message is identified by the line break. |
| Recognize start of message by idle line | The start of a message is recognized when the send transmission line is in the idle state for a certain time (specified in bit times) followed by an event such as reception of a character. |
| Recognize start of message with individual characters | The start of a message is recognized when a certain character occurs. You can enter the character as a HEX value. |
| Recognize start of message by a character string | The start of a message is detected when one of the specified character sequences arrives in the data stream. You can specify up to four character sequences each with up to five characters. |

The individual conditions can be logically linked in any way.

---

**See also**

[Making the settings for sending (S7-1200)](#making-the-settings-for-sending-s7-1200)
  
[User-programmed communication with RS-232 devices (S7-1200)](#user-programmed-communication-with-rs-232-devices-s7-1200)

#### Specifying the end of the message (S7-1200)

##### Recognizing the end of the message

To signal to the receiver when the transfer of a message is completed and when the next message transfer starts, criteria must be specified in the transmission protocol to identify the end and start of a message.

In total, there are six different methods of recognizing the end of a message and these can all be logically linked in any way. The following table shows the various possible setting options:

| Parameter | Definition |
| --- | --- |
| Recognize end of message by message timeout | The end of a message is recognized automatically when a selected maximum duration for a message is exceeded. Values from 0 to 65535 ms can be set. |
| Recognize end of message by reply timeout | The end of a message is recognized when there is no reply within a set time after transferring data. Values from 0 to 65535 ms can be set. |
| Recognize end of message by timeout between characters | The end of a message is detected when the time between two characters specified in bit times is exceeded. Values from 0 to 2500 bit times can be set.  The S7-1200 CPU only accepts a maximum time of eight seconds even if the value that is set results in a duration of more than eight seconds. |
| Recognize end of message by maximum length | The end of a message is recognized when the maximum length of a message is exceeded. Values from 1 to 1023 characters can be set. |
| Read message length from message | The message itself contains information about the length of the message. The end of a message is reached when the value taken from the message is reached. Which characters are used for the evaluation of the message length is specified with the following parameters:  - Offset of the length field in the message   The value decides the position of the character in the message that will be used to indicate the message length.  Values from 1 to 1022 characters can be set. - Size of the length field   This value specifies how many characters starting at the first evaluation position will be used to indicate the message length.  Values of 0, 1, 2 and 4 characters can be set. - The data following the length field  (does not belong to the message length)   The value specifies the number of bytes after the length field that must be ignored in the evaluation of the message length.  Values from 0 to 255 characters can be set. |
| Recognize message end with a character sequence | The end of a message is detected when the specified character sequence arrives in the data stream. You can define up to five characters in the character string that are to be checked. If the specified characters appear at the correct location in the message, the message end is recognized. To recognize the message end when character 1 and character 3 have a certain value, for example, you have to activate the check box for character 1 and character 3 and enter a character value. |
|  |  |

---

**See also**

[Making the settings for sending (S7-1200)](#making-the-settings-for-sending-s7-1200)
  
[User-programmed communication with RS-232 devices (S7-1200)](#user-programmed-communication-with-rs-232-devices-s7-1200)

### Enabling system memory (S7-1200)

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
> The selected memory byte cannot be used for intermediate storage of data.

### Using clock memory (S7-1200)

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

### Protection & Security (S7-1200)

This section contains information on the following topics:

- [Using the Security settings wizard (S7-1200)](#using-the-security-settings-wizard-s7-1200)
- [Protection of confidential configuration data (S7-1200)](#protection-of-confidential-configuration-data-s7-1200)
- [Setting options for the protection level (FW V1 to V3) (S7-1200)](#setting-options-for-the-protection-level-fw-v1-to-v3-s7-1200)
- [Setting options for the protection (FW as of V4) (S7-1200)](#setting-options-for-the-protection-fw-as-of-v4-s7-1200)
- [Restriction of communication services (S7-1200)](#restriction-of-communication-services-s7-1200)
- [Settings for users and roles (S7-1200)](#settings-for-users-and-roles-s7-1200)
- [Connection mechanisms (S7-1200)](#connection-mechanisms-s7-1200)
- [Group alarms for security events (S7-1200)](#group-alarms-for-security-events-s7-1200)
- [Certificate manager (S7-1200)](#certificate-manager-s7-1200)

#### Using the Security settings wizard (S7-1200)

When you add a CPU to the project that supports secure PG/HMI communication in the TIA Portal from the hardware catalog, a wizard starts for the security settings of the CPU.

The wizard guides you step-by-step through the following CPU settings:

- Password to protect confidential PLC configuration data
- PG/PC and HMI communication mode
- Access level

Each of these settings is explained in detail in the wizard. At the end, all settings are once again summarized in an overview.

The wizard also starts, for example, when you replace a module in the network view of the TIA Portal and the new CPU, unlike the replaced CPU, supports secure PG/HMI communication.

All settings in the wizard are applied in the Inspector window (CPU properties).

You can start the wizard at any time using a Start button in the "Protection &amp; Security" area of the CPU properties.

---

**See also**

[Protection of confidential configuration data (S7-1200)](#protection-of-confidential-configuration-data-s7-1200)
  
[Setting options for the protection (FW as of V4) (S7-1200)](#setting-options-for-the-protection-fw-as-of-v4-s7-1200)
  
[Connection mechanisms (S7-1200)](#connection-mechanisms-s7-1200)
  
[Protection of confidential configuration data (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#protection-of-confidential-configuration-data-s7-1200-s7-1500-s7-1500t)
  
[PG/HMI communication based on standardized security mechanisms (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#pghmi-communication-based-on-standardized-security-mechanisms-s7-1200-s7-1500-s7-1500t)

#### Protection of confidential configuration data (S7-1200)

As of STEP 7 V17, you have the option of assigning a password for protecting confidential configuration data of the respective CPU. This refers to data such as private keys that are required for the proper functioning of certificate-based protocols.

It is possible to do without the password if you have implemented measures to prevent unauthorized access to the TIA Portal project and the configuration of the CPU.

A description of the concept as well as detailed information on handling the password protection for confidential PLC configuration data (resetting, changing, information on spare parts) can be found in the requirements for secure communication.

##### Procedure

1. Open the CPU properties in the network view or in the device view.
2. Navigate to the area "Protection &amp; Security &gt; Protection of the PLC configuration data".

   **Result:** The "Protect confidential PLC configuration data" option is enabled first and the empty field for password entry is highlighted in red.
3. Configure the password (recommended) via the "Set" button or disable the "Protect confidential PLC configuration data" option.
4. Complete the configuration and create the user program.
5. Load the CPU.   
   When loading the hardware configuration, you will be asked once to re-enter the password.   
   **Background**: The configured password is used in the TIA Portal to generate the key information to protect confidential configuration data and thus to protect this data. For security reasons, however, neither the password nor the key information is saved in the project. In order for the key information to reach the CPU, it is re-generated when the hardware configuration is loaded, so that the password must be entered once at this point.

##### Tips and rules

- Manage your passwords in a password manager.
- Use TIA Portal's password policy verification settings to check newly entered passwords for compliance and prevent trivial passwords, for example:

  - In the project tree, navigate to the area "&lt;Project name&gt; &gt; Security settings &gt; Settings" area and select the "Password policies" area.
  - Specify, for example, the minimum number of characters the password must have or the minimum number of special characters.
- You do not have to assign different passwords for each CPU in a system or machine. If the requirements are met, you can also define the same password for a group of CPUs. This strategy also has advantages in the replacement parts scenario: If the group password is also assigned to the replacement CPU, the workload of replacing the CPU is reduced.
- The definition of passwords also has an impact on the replacement parts scenario.

---

**See also**

[Requirements for secure communication (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#requirements-for-secure-communication-s7-1200-s7-1500-s7-1500t)

#### Setting options for the protection level (FW V1 to V3) (S7-1200)

##### Protection level

The following section describes how to use the various protection levels of the S7-1200 CPUs V1 to V3.

##### Effects of the protection level setting

You can choose between the following protection levels:

- No protection: This corresponds to the default behavior. You cannot enter a password. Read and write access is always permitted.
- Write protection: Only read-only access is possible. You cannot change any data on the CPU and cannot load any blocks or a configuration. HMI access and communication between CPUs are excluded from the write protection. Assignment of a password is required to select this protection level.
- Write/read protection: No write or read access is possible in the "Accessible devices" area or in the project for devices that are switched online. Only the CPU type and the identification data can be displayed in the project tree under "Accessible devices". Display of online information or blocks under "Accessible devices", or in the project for devices interconnected online, is possible.

  HMI access and communication between CPUs are excluded from the write protection. Assignment of a password is required to select this protection level.

##### Behavior of a password-protected CPU during operation

The CPU protection takes effect after the settings are downloaded to the CPU.

Validity is checked before the online function is executed. If password protection is in place, you are prompted to enter a password.

Example: The module was assigned write protection and you want to execute the "Modify tags" function. This requires write access; therefore, the assigned password must be entered to execute the function.

The functions protected by a password can only be executed by one programming device/PC at any one time. Another programming device/PC cannot log on with a password.

Access authorization to the protected data is in effect for the duration of the online connection or until the access authorization is manually rescinded with "Online &gt; Delete access rights". Access authorization will also expire when the project is closed.

> **Note**
>
> You cannot restrict functions for process control, monitoring, and communications.
>
> However, some functions are protected due to their use as online data. RUN/STOP in the "Online tools" task card or "Set time of day" in the online and diagnostics view are therefore write-protected.

#### Setting options for the protection (FW as of V4) (S7-1200)

##### Protection level

The following section describes how to use the various access levels of the S7-1200 CPUs as of firmware version V4 to V4.6.

Starting from firmware version V4.7, you can protect the CPU via local user management. See [Settings for users and roles](#settings-for-users-and-roles-s7-1200).

S7-1200 CPUs provide various access levels to limit the access to specific functions.

The parameters for the access levels are assigned in a table. The green checkmarks in the columns to the right of the respective access level specify which operations are possible without knowing the password of this access level. If you want to use the functions of check boxes that are not selected, a password has to be entered.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Configuring an access level does not replace know-how protection**  Configuring access levels prevents unauthorized changes to the CPU by restricting download privileges. However, blocks on the memory card are not write- or read-protected. Use know-how protection to protect the code of blocks on the memory card. |  |

##### Default characteristics

The default access level is "No access (complete protection)".

##### The access levels in detail

With an S7-1200 CPU, you can configure the following access levels:

- Full access (no protection): The hardware configuration and the blocks can be read and changed by all users.
- Read access: With this access level, only read access to the hardware configuration and the blocks is possible without entering a password - meaning that you can load the hardware configuration and blocks into the programming device. In addition, HMI access and access to diagnostics data is possible.

  You cannot load blocks or a hardware configuration into the CPU without entering the password. Moreover, writing test functions and firmware updates are **not** possible without a password.
- HMI access: With this access level, only HMI access and access to diagnostics data is possible without entering the password.

  Without entering the password, you can neither load blocks and hardware configuration into the CPU, nor load blocks and hardware configuration from the CPU into the programming device. In addition, the following is **not** possible without a password: Writing test functions, changing the operating state (RUN/STOP) and firmware updates.
- No access (complete protection): When the CPU is completely protected, no read or write access to the hardware configuration and the blocks is possible. HMI access is also not possible. The server function for PUT/GET communication is disabled in this access level (cannot be changed).

  Authorization with the password again provides you full access to the CPU.

##### Behavior of a password-protected module during operation

The CPU protection takes effect after the settings are downloaded to the CPU.

Validity is checked before the online function is executed. If password protection is in place, you are prompted to enter a password.

Example: The module was configured with read access and you want to execute the "Modify tags" function. This requires write access; therefore, the assigned password must be entered to execute the function.

The functions protected by a password can only be executed by one programming device/PC at any one time. Another programming device/PC cannot log on.

Access authorization to the protected data is in effect for the duration of the online connection or until the access authorization is manually rescinded with "Online &gt; Delete access rights".

Each access level allows unrestricted access to certain functions without entering a password, for example, identification using the "Accessible devices" function.

#### Restriction of communication services (S7-1200)

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

#### Settings for users and roles (S7-1200)

This section contains information on the following topics:

- [Useful information on the local user administration and access control](#useful-information-on-the-local-user-administration-and-access-control)
- [Advantages of the local user administration and access control](#advantages-of-the-local-user-administration-and-access-control)
- [From the access level to the function right of users](#from-the-access-level-to-the-function-right-of-users)
- [Information about compatibility](#information-about-compatibility)
- [Configuring access levels](#configuring-access-levels)

##### Useful information on the local user administration and access control

As of TIA Portal version V19 and CPU firmware version V3.1 (V4.7 for S7-1200), S7-1500 and S7-1200 CPUs have improved management of users, roles and CPU function rights (User Management &amp; Access Control, UMAC). Software controller from version V30.1 also have this function.

From the versions mentioned above onwards, you manage all project users along with their rights (for example, access rights) for all CPUs in the project in the editor for users and roles of the project in the TIA Portal:

- Navigate to the "Security Settings &gt; Users and roles" area in the project navigation to manage users with their rights, for example, to control access rights.

The TIA Portal saves the assignment of the function rights of a CPU to user-defined roles and the assignment of these roles to users for each CPU. There are no system-defined roles with predefined function rights for CPUs.

After loading the configuration, the user management becomes effective in the respective CPUs. After loading, every CPU "knows" who may access which service and execute certain functions.

This new feature is also called "local user management and access control" below.

> **Note**
>
> **No global user support for CPU function rights**
>
> Another option for user management in the TIA Portal is the central user management UMC (User Management Component). With this component you manage global users on connected servers, e.g. also via the connection of an MS Active Directory. The authentication is then implemented via UMC. A global user management for CPU-specific function rights via UMC is currently not supported.

###### Users, roles and function rights - details of new features

Users and roles were already being managed in the predecessor version by TIA Portal under "Security settings &gt; Users and roles". In addition to the existing user management for HMI devices, for example, you can also manage all CPU function rights via this editor as of TIA Portal Version V19.

The CPU function rights are valid during runtime. Therefore, these rights are located in the "Runtime rights" tab in the editor for users and roles. For each CPU in the project, there is a section with all CPU function rights to choose from - separated according to CPU services such as PG/HMI communication (engineering access, access levels), web server and OPC UA.

In addition to the user management for projects, there were additional user managements for web servers and OPC UA servers (static user management for CPUs up to FW version V3.0) in the properties of the CPU:

- User for the OPC UA server (authentication)
- User for the web server (authentication and access control)

These additional user managements are integrated in the local user management in the project navigation as of TIA Portal V19 and as of CPU FW version V3.1.

###### Introduction to the local user management and access control

For CPUs up to firmware versions V3.0 (S7-1500) or V4.6 (S7-1200), you managed the users under the respective CPU properties separated according to services such as "Web server" und "OPC UA". Web server users were parameterized in the "Web server" area, OPC UA users in the "OPC UA" area.

To restrict the PG/HMI access to the CPU at different levels, you configured passwords for the corresponding access levels. With this procedure, for example, HMI accesses could be permitted without restriction, but write accesses could be made dependent on the knowledge of a password. You have agreed passwords for the different access levels in the "Protection &amp; Security" area of the CPU properties. The access protection therefore always related to groups that have the appropriate passwords - not to individual users.

With the introduction of the local user management and access control from TIA Portal version V19 onwards, you can use the "Security settings &gt; Users and roles" area in TIA Portal in the project navigation for all users and their roles and function rights of a CPU. This also applies to the access protection for engineering/HMI access, which as of TIA Portal version V19 no longer works via access levels with password protection by default, but also via user management.

More information on the new access protection is available [here](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#from-the-access-level-to-the-function-right-of-users-s7-1500).

As already introduced for engineering rights, for example, you use the role assignments for combining individual function rights. In a further step, you assign the roles to individual users. All the function rights which were assigned to a user via roles and which the user can exercise for the corresponding CPU are listed In the "Assigned rights" tab.

The following figure shows an example of the available and activated function rights of a CPU. At least one user must have full access to the CPU, otherwise the configuration cannot be compiled. To do this, first, a role with full access to the CPU must be created.

![Introduction to the local user management and access control](images/172103234187_DV_resource.Stream@PNG-en-US.png)

The following image displays the assignment of the role with full access to a user ("Admin").

![Introduction to the local user management and access control](images/172127982219_DV_resource.Stream@PNG-en-US.png)

###### Requirement

CPU parameterization: To be able to use users, roles and function rights for a CPU, the "Enable access control" option in the "Protection &amp; Security &gt; Access control" tab must be checked.

No project protection is required for local user management.

###### Default characteristics

The "Activate access control" option is preset for the access control. Users, with their assigned passwords as well as their roles and function rights, can be parameterized.

###### Downloading to device

You can load configuration changes with regard to the local user management and access control in the STOP and RUN mode of the CPU.

###### Runtime timeout

You can set a runtime timeout for both the role and the user in 'Security Settings &gt; Users and Roles'.

For an S7-1500 CPU, these settings are taken into account by the various services as follows:

- By means of the Web API you can, for example, create a web page or application that takes the settings for the runtime timeout into account. Standard web pages do not take the settings for runtime timeout into account and use the default value.
- The other services (PG/HMI communication and OPC UA server) do not use the runtime timeout; the logged-in user is not logged out after the set time.

---

**See also**

[Basics of user management in the TIA Portal](Managing%20users%20and%20roles.md#basics-of-user-management-in-the-tia-portal)

##### Advantages of the local user administration and access control

The following section discusses the advantages which the new local user management for S7-1200/S7-1500 CPUs provides, and what changes for you.

###### Quick activation/deactivation of the local user management

The options for user management are located in the "Protection &amp; Security &gt; Access control" tab:

- Access control deactivated: Every user has full access to all functions with the exception of the GDS Push function for the online transfer of certificates.

  | Symbol | Meaning |
  | --- | --- |
  |  | **Danger** |
  | **Disabled access control carries the risk of unauthorized access and thus the risk of personal injury and property damage.**   Only use this setting in a protected environment, for example during commissioning. |  |
- Access control enabled: The configured users with their assigned roles and concomitant linked function rights become effective after loading.

###### Access protection for PG/HMI accesses, now with user authentication

While it was possible to parameterize passwords for access levels for CPUs with firmware versions &lt; V3.1 (S7-1500 CPUs) or &lt; V4.7 (S7-1200 CPUs), with the current CPUs, you have the possibility to configure users with the corresponding function rights. This means that the authentication options for PG/HMI access correspond to the options offered by OPC UA or web server accesses.

###### All in one place

Irrespective of the service for which you configure users, roles and rights for a CPU: You have to manage the data at the same location.

All users, no matter if you manage their engineering rights for the project or their local runtime rights for each CPU in the project, can be found in the editor for users and roles in the project navigation.

###### Powerful password functions

- Support for compliance with complexity rules for password creation:   
  Right from the password creation stage, you can have the TIA Portal check compliance with complexity rules (such as the password length, uppercase/lowercase letters) (project navigation, "Security settings &gt; Settings" area).  
  The complexity rules are also saved in the CPU upon loading the user management. When the password is changed online, the CPU determines and considers these rules. This prevents a user from overriding the complexity rules set by the configuration engineer and assigning a non-secure password.
- The period of validity of passwords is adjustable:   
  To ensure that a user does not have access to the CPU with a compromised password for an unlimited time, you can parameterize a period of validity. Before the period of validity expires, the remaining time is then displayed on login so that each user has the possibility to change their password in time.

###### Loading the user management during operation

From firmware version V3.1 onwards, you can load certain security-relevant configuration data both in the STOP operating state and in the RUN operating state. Therefore, loading the hardware configuration does not necessarily result in a STOP of the CPU.

You can make the following changes in the STOP operating state as well as in the RUN operating state (Download to device &gt; Hardware configuration):

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

##### From the access level to the function right of users

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
> Regardless of the access protection, you always have to configure the users for the web server and for the OPC UA server in the project tree ("Security settings &gt; Users and roles" area).

###### Restrictions on continued use of the access levels

When using the "Legacy access control" option, you cannot select the access level directly in the table for setting the access levels. This selection can only be set for the new local user management in one way: Via the access protection function rights of the "Anonymous" user.

The local user "Anonymous" is created in a project by the system by default. With the help of this user, you determine the behavior of the CPUs in the project for someone who logs in without a user name and password. For security reasons, the anonymous user is deactivated and needs to be activated before use.

The area where you set the access levels leads you via a link to the editor for the required settings for the "Anonymous" user.

**Examples**:

- If the "Anonymous" user is deactivated or if the "Anonymous" user is activated and no function rights are assigned to that user, then nobody can log in without a user name and password (corresponds to the access level "No access (complete protection")).
- If the "Anonymous" user is activated and the "Full access" function right for a CPU is assigned to that user via a corresponding role, the result of this setting is "No protection". You can achieve the same effect with regard to access protection by setting "No access protection" in the "Protection &amp; Security" area of the CPU properties.

###### Procedure

To activate the "Legacy access control" and set the required access level, follow these steps:

1. In the CPU properties, go to "Protection &amp; Security &gt; Access control".
2. Select the option "Activate access control" and, in addition, select the check box "Use legacy access control via access levels" check box.

   The access level selection cannot be used in this setting. You have to set the access level via the "Anonymous" user of the CPU.

   The "Anonymous" user is disabled in the default setting. This means that the resulting access level for users without a password is "No access (complete protection)" (default setting).
3. Go to "Security Settings &gt; Users and roles" in the project navigation.
4. Activate the "Anonymous" user, if you want to set a different access level than "No access (complete protection)". You can assign a role with function rights that grants access to the CPU without password input, only to the activated "Anonymous" user.
5. You cannot assign function rights for a CPU directly to a user. You must first assign a role:  
   Therefore switch to the "Roles" tab and add a new role. Assign a meaningful name, e.g. "PLC1-Read-Access-Role". If you assign this role to a user, this user should have read access to PLC1 during operation.
6. Assign the required function right for the access to the CPU with the name "PLC1" to the role "PLC1-Read-Access-Role" - in this case "Read access".
7. Switch to the "User" tab and assign the "PLC1-Read-Access-Role" role to the activated "Anonymous" user.

   **Result**: The "Anonymous" user has read access for PLC1. This means that the access level tables of the CPU "PLC1" in the project are preset to "Read access" (cannot be changed) and users who are not logged in only have read access.

   For full access, or full access including fail-safe, you have to configure a password for the full access in the table for the access protection. Users who need full access to the CPU during runtime via an action, e.g. because a project is to be loaded onto the CPU, must legitimize themselves for this action with this password.

###### Tip

To make the user rights transparent, use meaningful names for the respective roles. You create users and roles for the entire project; you must select the function rights of a role individually for each CPU in the project. With a descriptive name you can, for example, immediately see which CPUs have read access and which CPUs are fully protected.

##### Information about compatibility

In the following sections, you will find information on the behavior of the CPUs with the local user management, e.g. when replacing modules in STEP 7 and for further use of projects and programs without local user management.

###### Replacement part scenario

If you replace a CPU with a firmware version &lt; V3.1 with a CPU with a firmware version V3.1 or higher, the program stored on the memory card runs like the original CPU. The behavior with regard to the configured access levels, the users for the OPC UA server and the web server corresponds to the behavior of the previous CPU.

In this case, the "Change password function" via the web server API is not accepted by the CPU because the CPU has been configured for firmware version &lt; V3.1 and has no local user management.

###### Replace CPU (upgrade)

If you replace a CPU (FW &lt; V3.1) with a current CPU (FW V3.1 or higher) in the TIA Portal, this has the following effects on the configured user data:

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

If you replace a CPU (as of FW V3.1) with a previous CPU (&lt; FW V3.1) in the TIA Portal, this has the following effects on the configured user data:

- The local user management is no longer available.
- Users of the web server with their roles and function rights remain in the "Users and roles" editor. They are not transferred to the area of the CPU properties (Web server &gt; User management) and are not in effect.
- Users of the OPC UA server with their roles and function rights remain in the "Users and roles" editor. No users are moved to the "OPC UA" area of the CPU parameters.

  With regard to the settings for user authentication, the default setting applies again (OPC UA &gt; Server &gt; Security &gt; User authentication): Guest authentication is enabled.
- It is no longer possible for users to change passwords during runtime (via web server API).

##### Configuring access levels

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
2. Open the "Protection &amp; Security &gt; Access control" entry in the area navigation.

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

[What you should know about the access levels (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#what-you-should-know-about-the-access-levels-s7-1500)
  
[Using the Security settings wizard (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#using-the-security-settings-wizard-s7-1500)

#### Connection mechanisms (S7-1200)

The settings for the connection mechanisms determine with which partners the CPU may connect. The default setting is that the CPU may only connect via Secure PG/HMI communication, which requires that the partner also supports Secure PG/HMI communication.

You can also select a certificate for secure PG/HMI communication or have the TIA Portal create a new certificate.

---

**See also**

[Additional settings for the secure PG/HMI communication (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#additional-settings-for-the-secure-pghmi-communication-s7-1200-s7-1500-s7-1500t)
  
[Using the Security settings wizard (S7-1200)](#using-the-security-settings-wizard-s7-1200)

#### Group alarms for security events (S7-1200)

This section contains information on the following topics:

- [What you should know about group alarms for security events](#what-you-should-know-about-group-alarms-for-security-events)
- [Configuring a group alarm for security events (S7-1200)](#configuring-a-group-alarm-for-security-events-s7-1200)

##### What you should know about group alarms for security events

###### Security events in the diagnostics buffer

The CPU stores information on important actions and events in the diagnostics buffer.

The following security events (event types) lead to an entry in the diagnostics buffer of the S7-1200:

- Going online with the correct or incorrect password.
- Manipulated communications data detected.
- Manipulated data detected on memory card.
- Manipulated firmware update file detected.
- Changed protection level (access protection) downloaded to the CPU.
- Password legitimization restricted or enabled (via an instruction).
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

##### Configuring a group alarm for security events (S7-1200)

###### Requirements

- STEP 7 V14
- S7-1200-CPU as of firmware V4.2

###### Procedure

To configure group alarms for security events, follow these steps:

1. Click on the CPU symbol in the network view.

   The properties of the CPU are displayed in the Inspector window.
2. Go to the "Protection" &gt; "Security event" area.
3. Click on "Security event".
4. Select the option "Summarize security events in case of high message volume" to enable group alarms for security events.
5. Set the duration of an interval (monitoring time); the default is 20 seconds.

---

**See also**

[What you should know about group alarms for security events](#what-you-should-know-about-group-alarms-for-security-events)

#### Certificate manager (S7-1200)

This section contains information on the following topics:

- [What you should know about the certificate manager (S7-1200)](#what-you-should-know-about-the-certificate-manager-s7-1200)
- [Local CPU-specific certificate manager (S7-1200)](#local-cpu-specific-certificate-manager-s7-1200)
- [Creating certificates (S7-1200)](#creating-certificates-s7-1200)
- [Assigning certificates (S7-1200)](#assigning-certificates-s7-1200)
- [Exporting certificates (S7-1200)](#exporting-certificates-s7-1200)
- [Deleting certificates (S7-1200)](#deleting-certificates-s7-1200)
- [Certificates for the Web server (S7-1200)](#certificates-for-the-web-server-s7-1200)
- [Certificates for OPC UA server (S7-1200)](#certificates-for-opc-ua-server-s7-1200)

##### What you should know about the certificate manager (S7-1200)

###### Introduction

Digital certificates play an important role in the secure data transfer between two devices. When digital certificates are used, the client must also check and trust the certificate of the server. Depending on the type of secure communication used, this also applies in the opposite direction: A client can only establish a secure connection to a server when the server accepts the digital certificate of the client, classifies it as trustworthy and trusts it.

S7-1200 CPUs as of firmware V4.3 support the use of certificates.

###### Device-specific and project-wide certificate manager

With the local CPU-specific certificate manager, certificates can be generated and managed for the respective device. These can then be used by the following objects:

- OPC UA server of the device
- Web server of the device
- Any additional system feature that requires certificates and is referenced by a certificate ID. As of TIA Portal V17, this is, for example, secure PG/HMI communication.

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

The global security settings are not visible until they have been activated in the project for at last one device. The "Use global security settings for certificate manager" check box is available to this purpose in the local CPU-specific certificate manager: It is located in the Inspector window in the general settings of a device with security functions under "Protection &amp; Security &gt; Certificate manager". Depending on this setting either only the local CPU-specific certificate manager with limited functionality is used or the global security certificate manager.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Loss of certificates and keys**  When you activate the global security certificate manager for the project, the contents of the local CPU-specific certificate manager are lost:  - The private keys cannot be restored. - Export your certificates if you want to keep using them in the global security certificate manager. - Update your configuration or your program, because the ID of the certificate can change. |  |

After activation of the global security certificate manager the local CPU-specific certificate manager acts like a temporary memory of the CPU-specific global certificates. When you create a new certificate in the local CPU-specific certificate manager, it is entered in the global security certificate manager. You can also select certificates in the global security certificate manager in the local CPU-specific certificate manager as a certificate for the CPU.

---

**See also**

[Certificates for the Web server (S7-1200)](#certificates-for-the-web-server-s7-1200)
  
[Certificates for OPC UA server (S7-1200)](#certificates-for-opc-ua-server-s7-1200)
  
[Local CPU-specific certificate manager (S7-1200)](#local-cpu-specific-certificate-manager-s7-1200)
  
[Useful information on Secure Communication (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#useful-information-on-secure-communication-s7-1200-s7-1500-s7-1500t)

##### Local CPU-specific certificate manager (S7-1200)

###### Introduction

With the local CPU-specific certificate manager you can use certificates for the OPC UA server and the Web server without access to the global security certificate manager.

###### Functions of the local certificate manager

In comparison to the global certificate manager, the local CPU-specific certificate manager only has a limited functionality. With the local certificate manager you can solely generate, assign, export or delete certificates.

The settings for the local CPU-specific certificate manager are located in the Inspector window in the general settings of the device under "Protection &amp; Security &gt; Certificate manager".

- Option for activating the global certificate manager
- Table for device certificates: Display and management of the certificates that you use, for example, for secure OUC (TLS server / TLS client), the Web server and the OPC UA server of the device.
- Table for certificates of the partner devices: Display of the certificates that you have assigned as trusted users or clients.

###### Device certificates

Device certificates are valid for the device and its associated components. The certificates displayed here were, for example, also created for the Web server or for OPC UA and are displayed here. Similarly, certificates with the settings for the Web server or for OPC UA can be created here - but have to be used at the corresponding location.

When you create a new certificate, the following values are entered as the default in the corresponding dialog for the device:

- Certificate holder: &lt;Name of the CPU&gt;/TLS. The set of characters is limited so that the specifications to ASN.1 can be observed.
- Type of signature: sha256RSA or sha1RSA, depending on the security policy in use.
- Validity period: The start and end of the validity period is entered in the two fields for the validity period in dependence on the system time.
- Usage: TLS. The extensions "KeyUsage" and "ExtendedKeyUsage" for certificates of the X.509 V3 standard are filled suitably for OPC UA.
- Alternative name of the certificate holder (SAN): IP address or DNS names of the interfaces used.

You can overwrite the defaults with your own values.

###### Certificates of the partner devices

For the certificates of the partner devices you can select device certificates of the local certificate manager. Device certificates are used without their private key. You can also select the certificates of other CPUs or CPs for secure communication within the project. The certificates of other CPUs or CPs are loaded to the CPU without private keys. In as far as the chain of certificates via the global certificate manager is available, the chain of certificates belonging to a CPU or CP is still not interrupted and the corresponding certificate authority and intermediate certificates remain assigned to the CPU or the CP.

When you delete a certificate in the table of certificates of the partner devices, only the link of the certificate to the global certificate manager is deleted. The certificate is therefore no longer available to the device, but remains in the global certificate manager. If required, the certificate can therefore be used again in the device if it is selected as a new certificate from the global certificate manager. If the certificate is to be deleted for the entire project, you have to do so in the shortcut menu of the global certificate manager.

---

**See also**

[What you should know about the certificate manager (S7-1200)](#what-you-should-know-about-the-certificate-manager-s7-1200)
  
[Creating certificates (S7-1200)](#creating-certificates-s7-1200)
  
[Assigning certificates (S7-1200)](#assigning-certificates-s7-1200)
  
[Exporting certificates (S7-1200)](#exporting-certificates-s7-1200)
  
[Deleting certificates (S7-1200)](#deleting-certificates-s7-1200)
  
[Global security certificate manager (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#global-security-certificate-manager-s7-1200-s7-1500-s7-1500t)

##### Creating certificates (S7-1200)

###### Introduction

You can create a new certificate for a device. When you create a new certificate with deactivated global security certificate manager, the certificate only applies for this device. With exclusive use of the local CPU-specific certificate manager, only self-signed certificates can be created.

You can furthermore create new certificates directly on the Web server or with OPC UA.

For S7-1200 CPUs as of firmware version V4.5 a PLC communication certificate is pre-selected and generated automatically.

###### Requirement

The device must offer security functions with certificate manager. This applies for S7-1200 CPUs as of firmware V4.3.

For S7-1200 CPUs as of firmware version V4.5 the settings for the password to protect confidential configuration data must be consistent.

###### Procedure

To create a new certificate, follow these steps:

1. In the Inspector window, go to "Protection &amp; Security &gt; Certificate manager" in the properties of the device.
2. Click "Add" in the table of certificates. A new row is entered in the table.
3. Click in the new row. The selection for new certificates is opened.
4. Click the "Add" button. The corresponding dialog window opens in which you can enter the data for the new certificate.
5. Select how the new certificate is to be signed:

   - Self-signed: If you want to assign the signature yourself.
   - Signed by a certificate authority (CA): Select a certificate authority from the drop-down list.
6. Enter the parameters for the certificate.

   - Certificate holder: The certificate holder is the device for which the certificate applies.
   - Valid from: The certificate is valid from the specified date.
   - Valid until: The certificate is no longer valid after the specified date has expired.
   - Usage: This value is entered in digital certificates of the X.509 V3 standard in the extensions "KeyUsage" and "ExtendedKeyUsage".
   - Alternative name of the certificate holder (SAN).
7. When you click "OK", the new certificate is created and entered in the table.

> **Note**
>
> **Self-signed certificates**
>
> With a self-signed certificate you have already created an encryption for the transport path, but the recipient of a message does not yet have a confirmation whether the named sender is the real sender. A message that was signed by a certificate authority identifies the sender as "real" towards the recipient. However, you can create a self-signed certificate for the device when you still have to wait for a certificate signed by a certificate authority. Through the global security certificate manager in the project tree you can then either replace the temporarily used self-signed certificate or renew it by specifying the certificate authority after you have received the "official" certificate from the certificate authority (CA). You can naturally also retain a self-signed certificate in the project and forgo the usage of an "official" CA certificate.

###### Result

A new certificate is created for the device. For an S7-1200 CPU, "TLS" is entered automatically as the usage. This is the case when a new self-signed certificate is issued or when a self-created certificate is issued by the root certificate authority of the TIA Portal via the activated global security certificate manager.

###### Certificate ID

Each certificate in the certificate manager receives an ID. This ID is used for identification of the certificates in the following cases:

- OPC UA server certificate
- List of trusted OPC UA clients
- List of trusted OPC UA users
- Web server certificate
- Secure OUC instructions
- PLC communication certificate for Secure PG/HMI communication

The certificate ID is assigned by the certificate manager when a certificate is created or imported. The certificate IDs are required to uniquely assign the certificates to specific system data types, for example, to the SDT TCON_IP_v4_Sec. The certificate ID is unique within the project and cannot be changed.

---

**See also**

[Local CPU-specific certificate manager (S7-1200)](#local-cpu-specific-certificate-manager-s7-1200)

##### Assigning certificates (S7-1200)

###### Introduction

You can assign available certificates to the CPUs and CPs in the Inspector window.

###### Requirement

The device must offer security functions with certificate manager. This applies for S7-1200 CPUs as of firmware V4.3.

###### Procedure

To assign an available certificate to a device, follow these steps:

1. In the Inspector window, go to "Protection &amp; Security &gt; Certificate manager" in the properties of the device.
2. Click "Add" in the table of certificates. A new row is entered in the table.
3. Click in the new row. The selection for new certificates is opened.
4. Select an available certificate. If only the local CPU-specific certificate manager is active, you do not see the globally available certificates. You can only see and select globally available certificates when the global security certificate manager is activated.
5. Click the green check mark to enter the selection in the table of certificates.

###### Result

The selected certificate was assigned to the device.

---

**See also**

[Local CPU-specific certificate manager (S7-1200)](#local-cpu-specific-certificate-manager-s7-1200)

##### Exporting certificates (S7-1200)

###### Introduction

You can export available certificates via the certificate manager.

###### Requirement

The device must offer security functions with certificate manager. This applies for S7-1200 CPUs as of firmware V4.3.

###### Procedure

To export a certificate, follow these steps:

1. In the Inspector window, go to "Protection &amp; Security &gt; Certificate manager" in the properties of the device.
2. Right-click in the row with the certificate to be exported to open the shortcut menu.
3. Click "Export certificate".
4. Export the certificate into one of the selectable file formats: CER, DER.

Private keys cannot be exported since they are encrypted asymmetrically and cannot be restored.

###### Result

The selected certificate has been exported and can now be backed up or be used in other projects.

---

**See also**

[Local CPU-specific certificate manager (S7-1200)](#local-cpu-specific-certificate-manager-s7-1200)

##### Deleting certificates (S7-1200)

###### Introduction

You can delete available certificates via the certificate manager.

###### Requirement

The device must offer security functions with certificate manager. This applies for S7-1200 CPUs as of firmware V4.3.

###### Procedure

To delete a certificate, follow these steps:

1. In the Inspector window, go to "Protection &amp; Security &gt; Certificate manager" in the properties of the device.
2. Right-click in the row with the certificate to be deleted to open the shortcut menu.
3. Click "Delete certificate".

###### Result

The selected certificate was deleted in the device. With an activated global security certificate manager the certificate is retained for the project, but is no longer used for the device.

---

**See also**

[Local CPU-specific certificate manager (S7-1200)](#local-cpu-specific-certificate-manager-s7-1200)

##### Certificates for the Web server (S7-1200)

###### Introduction

You can create or assign a server certificate for the Web server in the Inspector window under "Web server &gt; Server security".

###### Local Web server certificate

The following restrictions apply when you create Web server certificates locally without using the global security settings for the certificate manager:

- The certificate only applies to the configured CPU and is not available throughout the project.
- Only self-signed certificates are created. Self-signed certificates are not embedded in a "Public Key Infrastructure" (PKI) and cannot sign other certificates.
- Private keys of the certificate cannot be exported.
- Import and renewal of certificates is only possible in the global security settings for the certificate manager.

###### Default settings for Web server certificates

When you create a new certificate, the following values are entered as the default in the corresponding dialog for a Web server:

- Certificate holder: &lt;Name of the CPU&gt;/Web server. The set of characters is limited so that the specifications to ASN.1 can be observed.
- Type of signature: sha256RSA or sha1RSA, depending on the security policy in use.
- Validity period: The start and end of the validity period is entered in the two fields for the validity period in dependence on the system time.
- Usage: Web server. The extensions "KeyUsage" and "ExtendedKeyUsage" for certificates of the X.509 V3 standard are filled suitably for the Web server.
- Alternative name of the certificate holder (SAN): IP address of the used interfaces of the CPU and CP.

You can overwrite the defaults with your own values.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **SAN with reserved IP address**  When the alternative name of the certificate holder contains one or more reserved IP addresses, the certificate does not fulfill the guideline "Baseline Requirements Certificate Policy for the Issuance and Management of Publicly-Trusted Certificates". This can result in incompatibility with your own Web browsers.  To meet the guideline you should replace the IP addresses of the alternative name of the certificate holder with domain names. This requires a DNS server in the network that dissolves the IP addresses of the devices. |  |

---

**See also**

[What you should know about the certificate manager (S7-1200)](#what-you-should-know-about-the-certificate-manager-s7-1200)
  
[Information about the web server (S7-300, S7-400, S7-1500)](Configuring%20the%20Web%20server%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#information-about-the-web-server-s7-300-s7-400-s7-1500)
  
[Access only through HTTPS (S7-300, S7-400, S7-1500)](Configuring%20the%20Web%20server%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#access-only-through-https-s7-300-s7-400-s7-1500)
  
[How communication with certificates works: HTTP over TLS (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#how-communication-with-certificates-works-http-over-tls-s7-1200-s7-1500-s7-1500t)

##### Certificates for OPC UA server (S7-1200)

###### Introduction

You can create or assign a server certificate for OPC UA in the Inspector window under "OPC UA &gt; Server &gt; Security".

###### Local server certificates for OPC UA

The following restrictions apply when you create server certificates locally for OPC UA without using the global security settings for the certificate manager:

- The certificate only applies to the configured CPU and is not available throughout the project.
- Only self-signed certificates are created. Self-signed certificates are not embedded in a "Public Key Infrastructure" (PKI) and cannot sign other certificates.
- Private keys of the certificate cannot be exported.
- Import and renewal of certificates is only possible in the global security settings for the certificate manager.

###### Default settings for server certificates

When you create a new certificate, the following values are entered as the default in the corresponding dialog for a OPC UA:

- Certificate holder: &lt;Name of the CPU&gt;/OPCUA. The set of characters is limited so that the specifications to ASN.1 can be observed.
- Type of signature: sha256RSA or sha1RSA, depending on the security policy in use.
- Validity period: The start and end of the validity period is entered in the two fields for the validity period in dependence on the system time.
- Usage: OPC UA. The extensions "KeyUsage" and "ExtendedKeyUsage" for certificates of the X.509 V3 standard are filled suitably for OPC UA.
- Alternative name of the certificate holder (SAN): IP address of the used interfaces and the URI of the OPC UA server.

You can overwrite the defaults with your own values.

---

**See also**

[What you should know about the certificate manager (S7-1200)](#what-you-should-know-about-the-certificate-manager-s7-1200)

### Activating and deactivating SNMP (S7-1200)

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
> For compatibility reasons, an S7-1500 CPU as of firmware version V3.0 with a loaded predecessor project (CPU firmware &lt; V3.0) behaves like the CPU in the predecessor project:
>
> SNMP is activated and "public" and "private" community strings are in effect.

#### Configuring SNMP (S7-1200)

As of CPU firmware version 4.6 and TIA Portal version V18, you have the possibility to change the following settings for SNMP in the CPU properties:

- Activate SNMP (default: deactivated)

You can find the settings in the "Advanced configuration &gt; SNMP" area of the CPU properties.

#### Configuring SNMP (S7-1500)

As of CPU firmware version V3.0 and TIA Portal version V18, you have the possibility to change the following settings for SNMP in the CPU properties:

- Activate SNMP (default: deactivated)
- Read-only community string (default: "public")
- Read-write community string (default: "private")

You can find the settings in the "Advanced configuration &gt; SNMP" area.

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

### Disabling SNMP: Full program example (S7-1200)

#### Introduction

The example applies to S7-1500 and S7-1200.

Follow these steps to apply the program code to your project:

1. Copy the entire program code to the clipboard.
2. Open a text editor (e.g. "Editor").
3. Paste the content of the clipboard to the text editor with Ctrl+V. Save the document as scl file, for example, SNMP_DEACT.scl.
4. Open your project in STEP 7.
5. Import the scl file as an external source.
6. Generate the startup OB and the data blocks.
7. Right-click the scl file and select "Generate block from source" in the shortcut menu.

#### Example program with WRREC call in OB 100

DATA_BLOCK "Deactivate_SNMP"

{ S7_Optimized_Access := 'TRUE' }

VERSION : 0.1

NON_RETAIN

VAR

snmp_deactivate : Bool;

snmp_record : Struct

BlockID : UInt;

BlockLength : UInt;

"Version" : USInt;

Subversion : USInt;

Reserved : UInt;

SNMPControl : UDInt;

END_STRUCT;

snmp_done : Bool;

snmp_error : Bool;

snmp_Status : DWord;

END_VAR

BEGIN

snmp_deactivate := true;

snmp_record.BlockID := 16#f003;

snmp_record.BlockLength := 8;

snmp_record."Version" := 1;

END_DATA_BLOCK

ORGANIZATION_BLOCK "Startup"

TITLE = "Complete Restart"

{ S7_Optimized_Access := 'TRUE' }

VERSION : 0.1

BEGIN

REPEAT

"WRREC_DB_1"(REQ := "Deactivate_SNMP".snmp_deactivate,

ID := "Local~PROFINET-Schnittstelle_1",

INDEX := 16#b071,

DONE =&gt; "Deactivate_SNMP".snmp_done,

ERROR =&gt; "Deactivate_SNMP".snmp_error,

STATUS =&gt; "Deactivate_SNMP".snmp_Status,

RECORD := "Deactivate_SNMP".snmp_record);

UNTIL "Deactivate_SNMP".snmp_done OR "Deactivate_SNMP".snmp_error

END_REPEAT;

END_ORGANIZATION_BLOCK

DATA_BLOCK "WRREC_DB_1"

{OriginalPartName := 'WRREC';

VersionGUID := 'bc169451-58cd-44a3-855b-3f78cc0623c8';

S7_Optimized_Access := 'TRUE' }

AUTHOR : SIMATIC

FAMILY : DP

NAME : WRREC

VERSION : 1.0

NON_RETAIN

WRREC

BEGIN

END_DATA_BLOCK

## Symbolic and numerical names of instructions (S7-1200)

### Description

The instructions from the task card are comprised of functions (FC), function blocks (FB), system functions (SFC) and system function blocks (SFB) that are identified internally by numbers.

The following tables show the assignment of numerical and symbolic names.

### Function blocks (FBs)

| Numerical name | Symbolic name |
| --- | --- |
| FB 105 | TC_CONFIG |
| FB 110 | Port_Config |
| FB 111 | Send_Config |
| FB 112 | Receive_Config |
| FB 113 | Send_P2P |
| FB 114 | Receive_P2P |
| FB 115 | Receive_Reset |
| FB 116 | Signal_Get |
| FB 117 | Get_Features |
| FB 118 | Set_Features |
| FB 163 | TC_SEND |
| FB 164 | TC_RECV |
| FB 165 | TC_CON |
| FB 166 | TC_DISCON |
| FB 804 | SET_TIMEZONE |
| FB 1030 | TSEND_C |
| FB 1031 | TRCV_S |
| FB 1071 | USS_DRIVE |
| FB 1080 | MB_COMM_LOAD |
| FB 1081 | MB_MASTER |
| FB 1082 | MB_SLAVE |
| FB 1084 | MB_CLIENT |
| FB 1085 | MB_SERVER |
| FB 1100 | MB_Halt |
| FB 1101 | MC_Home |
| FB 1102 | MC_MoveAbsolute |
| FB 1103 | MC_MoveJog |
| FB 1104 | MC_MoveRelative |
| FB 1105 | MC_MoveVelocity |
| FB 1107 | MC_Power |
| FB 1108 | MC_Reset |
| FB 1110 | MC_MoveInterrupt |
| FB 1111 | MC_ChangeDynamik |
| FB 1112 | MC_CommandTable |
| FB 1113 | MC_MoveLinearAbs_2D |
| FB 1114 | MC_MoveLinearRel_2D |
| FB 1115 | MC_MoveCircular_2D |
| FB 1130 | PID_Compact |
| FB 1134 | PID_3Step |
| FB 1140 | HSC |
| FB 2040 | RecipeCreate |
| FB 2041 | RecipeOpen |
| FB 2042 | RecipeRead |
| FB 2043 | RecipeWrite |
| FB 2044 | RecipeAppend |
| FB 2045 | RecipeClose |

### Functions (FCs)

| Numerical name | Symbolic name |
| --- | --- |
| FC 2 <sup>(1)</sup> | CONCAT |
| FC 4 <sup>(1)</sup> | DELETE |
| FC 11 <sup>(1)</sup> | FIND |
| FC 17 <sup>(1)</sup> | INSERT |
| FC 20 <sup>(1)</sup> | LEFT |
| FC 21 <sup>(1)</sup> | LEN |
| FC 22 <sup>(1)</sup> | LIMIT |
| FC 25 <sup>(1)</sup> | MAX |
| FC 26 <sup>(1)</sup> | MID |
| FC 27 <sup>(1)</sup> | MIN |
| FC 31 <sup>(1)</sup> | REPLACE |
| FC 32 <sup>(1)</sup> | RIGHT |
| FC 36 <sup>(1)</sup> | ENCO |
| FC 36 <sup>(1)</sup> | SEL |
| FC 37 | DECO |
| FC 800 | LED |
| FC 801 | IM_DATA |
| FC 802 | DeviceStates |
| FC 803 | ModuleStates |
| FC 1070 | USS_PORT |
| FC 1072 | USS_RPM |
| FC 1073 | USS_WPM |
| <sup>(1)</sup> MC7+ instruction |  |

### System data types (SDTs)

| Numerical name | Symbolic name |
| --- | --- |
| SDT 99 | WWW_CDB |
| SDT 513 | CONDITIONS |
| SDT 581 | Send_Conditions |
| SDT 582 | Receive_Conditions |

### System function blocks (SFBs)

| Numerical name | Symbolic name |
| --- | --- |
| SFB 0 <sup>(1)</sup> | CTU |
| SFB 1 <sup>(1)</sup> | CTD |
| SFB 2 <sup>(1)</sup> | CTUD |
| SFB 3 <sup>(1)</sup> | TP |
| SFB 4 <sup>(1)</sup> | TON |
| SFB 5 <sup>(1)</sup> | TOF |
| SFB 27 | START_OB |
| SFB 52 | RDREC |
| SFB 53 | WRREC |
| SFB 54 | RALRM |
| SFB 105 | T_CONFIG |
| SFB 106 | TDIAG |
| SFB 107 | TRESET |
| SFB 110 | PORT_CFG |
| SFB 111 | SEND_CFG |
| SFB 112 | RCV_CFG |
| SFB 113 | SEND_PTP |
| SFB 114 | RCV_PTP |
| SFB 115 | SGN_GET |
| SFB 116 | SGN_SET |
| SFB 117 | RCV_RST |
| SFB 120 | CTRL_HSC |
| SFB 122 | CTRL_PWM |
| SFB 124 | CTRL_HSC_EXT |
| SFB 140 | DataLogCreate |
| SFB 141 | DataLogOpen |
| SFB 142 | DateLogWrite |
| SFB 143 | DataLogClear |
| SFB 144 | DataLogClose |
| SFB 145 | DataLogDelete |
| SFB 146 | DataLogNewFile |

### System functions (SFCs)

| Numerical name | Symbolic name |
| --- | --- |
| SFC 7 | DP_PRAL |
| SFC 11 | DPSYC_FR |
| SFC 13 | DPNRM_DG |
| SFC 14 | DPRD_DAT |
| SFC 16 | RD_OBINF |
| SFC 23 | DEL_DB |
| SFC 28 | SET_TINT |
| SFC 29 | CAN_TINT |
| SFC 30 | ACT_TINT |
| SFC 31 | QRY_TINT |
| SFC 32 | SRT_DINT |
| SFC 33 | CAN_DINT |
| SFC 34 | QRY_DINT |
| SFC 41 | DIS_AIRT |
| SFC 42 | EN_AIRT |
| SFC 43 | RE_TRIGR |
| SFC 45 | D_ACT_DP |
| SFC 46 | STP |
| SFC 82 | CREA_DBL |
| SFC 83 | READ_DBL |
| SFC 84 | WRIT_DBL |
| SFC 86 | CREATE_DB |
| SFC 89 | RST_EVOV |
| SFC 99 | WWW |
| SFC 101 | RTM |
| SFC 117 | GET_DIAG |
| SFC 124 | ATTR_DB |
| SFC 140 | IO2MOD |
| SFC 143 | RD_ADDR |
| SFC 154 | RD_LOC_T |
| SFC 154 | DPWR_DAT |
| SFC 161 | WR_LOC_T |
| SFC 180 | ID2LOG |
| SFC 181 | LOG2ID |
| SFC 182 | ID2GEO |
| SFC 190 | SET_CINT |
| SFC 191 | QRY_CINT |
| SFC 192 | ATTACH |
| SFC 193 | DETACH |
| MC7+ Anweisung | GET_ERROR |
| MC7+ Anweisung | GET_ERR_ID |

## Organization blocks (S7-1200)

This section contains information on the following topics:

- [Startup OBs (S7-1200)](#startup-obs-s7-1200)
- [Cyclic OBs (S7-1200)](#cyclic-obs-s7-1200)
- [Organization blocks for interrupt-driven program execution (S7-1200)](#organization-blocks-for-interrupt-driven-program-execution-s7-1200)
- [Block parameters of organization blocks (S7-1200)](#block-parameters-of-organization-blocks-s7-1200)

### Startup OBs (S7-1200)

#### Description

You can determine the boundary conditions for the startup characteristics of your CPU, for example, the initialization values for "RUN". To do this, write a startup program. The startup program consists of one or more startup OBs (OB numbers 100 or &gt;= 123).

The startup program is executed once during the transition from "STOP" mode to "RUN" mode. Current values from the process image of the inputs are not available for startup program, nor can these values be set.

After the complete execution of the startup OBs, the process image of the inputs is read in and the cyclic program is started.

There is no time limit for executing the startup routine. Therefore the scan cycle monitoring time is not active. Time-driven or interrupt-driven organization blocks cannot be used.

#### Start information

A startup OB has the following start information:

| Tag | Data type | Description |
| --- | --- | --- |
| LostRetentive | BOOL | = 1, if retentive data storage areas have been lost |
| LostRTC | BOOL | = 1, if realtime clock has been lost |

---

**See also**

["STARTUP" operating mode (S7-1200)](#startup-operating-mode-s7-1200)
  
[Organization blocks (OB)](Programming%20basics.md#organization-blocks-ob)
  

  
[Events and OBs (S7-1200)](#events-and-obs-s7-1200)

### Cyclic OBs (S7-1200)

#### Introduction

For the program execution to start, at least one program cycle OB must be present in the project. The operating system calls this program cycle OB once in each cycle and thereby starts the execution of the user program. You can use multiple OBs (OB numbers &gt;= 123). When multiple program cycle OBs are used, these are called in one after the other in the order of their OB numbers. The program cycle OB with the lowest OB number is called first.

The program cycle OBs have the priority class 1. This corresponds to the lowest priority of all OBs. The cyclic program can be interrupted by events of any other event class.

#### Programming cyclic program execution

You program cyclic program execution by writing your user program in the cycle OBs and the blocks that they call.

The first cyclic program execution begins as soon as the startup program has ended without errors. The cycle restarts after the end of each cyclic program execution.

#### Sequence of cyclic program execution

One cycle of the program execution encompasses the following steps:

1. The operating system starts the maximum cycle time.
2. The operating system writes the values from the process image output to the output modules.
3. The operating system reads out the state of the inputs of the input modules and updates the process image input.
4. The operating system processes the user program and executes the operations contained in the program.
5. At the end of a cycle, the operating system executes any tasks that are pending, for example, loading and deleting blocks or calling other cycle OBs.
6. Finally, the CPU returns to the start of the cycle and restarts the scan cycle monitoring time.

See also: [process image input/output](#process-image-inputoutput-s7-1200)

#### Options for interrupting

Cyclic program execution can be interrupted by the following events:

- Interrupt
- A STOP command, triggered by

  - Operation of the programming device
  - "STP" instruction
- Supply voltage failure
- Occurrence of a device fault or program error

#### Start information

- None
- Optimized start information:

| Name | Data type | Meaning |
| --- | --- | --- |
| first_scan | BOOL | = TRUE in the first call of this OB:  - Transition from STOP or HOLD to RUN - After reloading |
| retentivity | BOOL | = TRUE, if retentive data are available |

---

**See also**

[Organization blocks (OB)](Programming%20basics.md#organization-blocks-ob)
  

  
[Events and OBs (S7-1200)](#events-and-obs-s7-1200)

### Organization blocks for interrupt-driven program execution (S7-1200)

This section contains information on the following topics:

- [Time-of-day interrupt OBs (S7-1200)](#time-of-day-interrupt-obs-s7-1200)
- [Status interrupt OB (S7-1200)](#status-interrupt-ob-s7-1200)
- [Update interrupt OB (S7-1200)](#update-interrupt-ob-s7-1200)
- [OB for vendor- or profile-specific interrupts (S7-1200)](#ob-for-vendor--or-profile-specific-interrupts-s7-1200)
- [Time-delay interrupt OBs (S7-1200)](#time-delay-interrupt-obs-s7-1200)
- [Cyclic interrupt OBs (S7-1200)](#cyclic-interrupt-obs-s7-1200)
- [Hardware interrupt OBs (S7-1200)](#hardware-interrupt-obs-s7-1200)
- [Time error OB (S7-1200)](#time-error-ob-s7-1200)
- [Diagnostic interrupt OB (S7-1200)](#diagnostic-interrupt-ob-s7-1200)
- [Pull/plug interrupt OB (S7-1200)](#pullplug-interrupt-ob-s7-1200)
- [Rack error OB (S7-1200)](#rack-error-ob-s7-1200)
- [MC-servo OB (S7-1200)](#mc-servo-ob-s7-1200)
- [MC-PreServo OB (S7-1200)](#mc-preservo-ob-s7-1200)
- [MC-PostServo OB (S7-1200)](#mc-postservo-ob-s7-1200)
- [MC-interpolator OB (S7-1200)](#mc-interpolator-ob-s7-1200)

#### Time-of-day interrupt OBs (S7-1200)

##### Function

Organization blocks for time-of-day interrupt (OB number &gt;=123) can be processed as follows:

- One time to a preset time (date with time of day)
- Periodically with preset start time and the following intervals:

  - Every minute
  - Hourly
  - Daily
  - Weekly
  - Monthly
  - Yearly
  - End of month

Time-of-day interrupt-OBs are therefore used to run parts of the user program on a time-controlled basis.

##### Status for time-of-day interrupt

The following table contains the possible status of a time-of-day interrupt as well as it's meaning.

| Status | Meaning |
| --- | --- |
| Cancelled | The one-time processing has already taken place, or the start event of an not yet processed time-of-day interrupt has been deleted with the extended instruction CAN_TINT. |
| Set | You have scheduled the time or start time for processing. |
| Activated | You have scheduled whether processing takes place one time or periodically, and in the case of periodic processing, you have scheduled the interval. |

##### Rules for time-of-day interrupts

The following rules apply to the use of time-of-day interrupts:

- A time-of-day interrupt can only be processed if it is set and activated, and a corresponding organization block exists in the user program.
- The start times of periodic time-of-day interrupts must correspond to a real date. For example, it is not possible to repeat an organization block monthly which first occurs on January 31st. In this case, on OB will only be started in the months that have 31 days.
- A time-of-day interrupt activated during startup by extended instruction call ACT_TINTwill not be executed until the startup is complete.
- After each CPU startup, you must reactivate previously set time-of-day interrupts

##### Setting and activating a time-of-day interrupt OB

Before a time-of-day interrupt can be deleted and the corresponding time-of-day interrupt OB can be processed from the operating system, you must set and activate the interrupt. You have the following options:

| Set time-of-day interrupt | Activate time-of-day interrupt |
| --- | --- |
| Means of configuring | Means of configuring |
| Means of configuring | By extended instruction call ACT_TINT |
| By extended instruction call SET_TINTL | By extended instruction call ACT_TINT |
|  |  |

> **Note**
>
> If you configure a time-of-day interrupt in such a way that the corresponding OB is to be processed once, the start time must not be in the past (relative to the real-time clock of the CPU).
>
> If you configure a time-of-day interrupt in such a way that the corresponding OB is to be processed periodically, but the start time is in the past, then the time-of-day interrupt will be processed the next time it is due.

##### Time-of-day interrupt status query

In order to query the status of the time-of-day interrupt, call the extended instruction QRY_TINT.

##### Cancelling a time-of-day interrupt

You can cancel a time-of-day interrupt which has not yet been processed with the extended instruction CAN_TINT.

You can reset cancelled time-of-day interrupts with the extended instruction SET_TINTL and activate them with the extended instruction ACT_TINT.

##### Conditions that effect the time-of-day interrupt OBs

Since a time-of-day interrupt occurs only at specific intervals, certain conditions can affect the function of the associated OBs during execution of your program. The following table shows some of these conditions and describes how these affect the processing of a time-of-day interrupt OB.

| Condition | Result |
| --- | --- |
| The extended instruction CAN_TINT is called in the user program. | The operating system deletes the start event (date and time) of the time-of-day interrupt. You must reset and reactivate the time-of-day interrupt if you are going to call the corresponding time-of-day interrupt OB again. |
| By synchronizing or correcting the CPU system clock, the time of day will be set ahead. With this, the start time for a time-of-day interrupt OB will be bypassed. | The operating system calls the time error interrupt OB (OB 80) and records the start event, the number, and the priority of the first bypassed time-of-day interrupt OB in its start information. After completion of the OB 80, the operating system processes the bypassed time-of-day interrupt OB only once. |
| By synchronizing or correcting the CPU system clock, the time of day will be set back. The corrected clock time is before the start time of an already processed time-of-day interrupt OB. | The time-of-day interrupt OB is repeated. |
| A time-of-day interrupt OB is still being processed when the start event for its next execution occurs. | The operating system then calls time error interrupt OB 80. The requested OB is processed only after the processing and further execution of the current time-of-day interrupt OB has completed. |
|  |  |

##### Start information

A time-of-day interrupt OB has the following start information:

| Tag | Data type | Description |
| --- | --- | --- |
| CaughtUp | BOOL | =1, if the OB call is executed because clock time is turned ahead. |
| SecondTime | BOOL | =1 if the OB is called a second time because clock time is turned back (more exactly, if the planned time of the current OB processing is earlier than or the same time as the planned time for the previous OB processing).  Note: SecondTime is only set once. |

#### Status interrupt OB (S7-1200)

##### Description

When it receives a status interrupt, the operating system of the S7-1200 CPU calls the status interrupt OB from a DP master or IO controller. This may be the case if a module of a slave changes its operating mode, for example, from "RUN" to "STOP". For more detailed information on events that trigger a status interrupt, refer to the documentation of the slave or device manufacturer.

##### Structure of the start information

The status-interrupt OB has the following start information:

| Name | Data type | Meaning |
| --- | --- | --- |
| LADDR | HW_IO | Hardware address of the component triggering the interrupt |
| Slot | UINT | Slot number of the component triggering the interrupt |
| Specifier | WORD | Interrupt specifier from the interrupt frame |

---

**See also**

[Events and OBs (S7-1200)](#events-and-obs-s7-1200)

#### Update interrupt OB (S7-1200)

##### Description

When it receives a status interrupt, the operating system of the S7-1200 CPU calls the update interrupt OB from a DP master or IO controller. This may be the case if you changed a parameter on a slot of a slave or device. For more detailed information on events that trigger an update interrupt, refer to the documentation of the slave or device manufacturer.

##### Structure of the start information

The update interrupt OB has the following start information:

| Name | Data type | Meaning |
| --- | --- | --- |
| LADDR | HW_IO | Hardware address of the component triggering the interrupt |
| Slot | UINT | Slot number of the component triggering the interrupt |
| Specifier | WORD | Interrupt specifier from the interrupt frame |

---

**See also**

[Events and OBs (S7-1200)](#events-and-obs-s7-1200)

#### OB for vendor- or profile-specific interrupts (S7-1200)

##### Description

When it receives a manufacturer-specific or profile-specific interrupt from a DP master or IO controller, the operating system of the S7-1200 CPU calls OB 57. For more detailed information on events that trigger this type of interrupt, refer to the documentation of the slave or device manufacturer.

##### Structure of the start information

The OB for manufacturer-specific and profile-specific interrupts has the following start information:

| Name | Data type | Meaning |
| --- | --- | --- |
| LADDR | HW_IO | Hardware address of the component triggering the interrupt |
| Slot | UINT | Slot number of the component triggering the interrupt |
| Specifier | WORD | Interrupt specifier from the interrupt frame |

---

**See also**

[Events and OBs (S7-1200)](#events-and-obs-s7-1200)

#### Time-delay interrupt OBs (S7-1200)

##### Description

A time-delay interrupt OB is started after a configurable time delay of the operating system. The delay time starts after the SRT_DINT instruction is called.

You can use up to four time-delay interrupt OBs or cyclic interrupt OBs in your program. If, for example, you are already using two cyclic interrupt OBs, you can insert a maximum of two further time-delay interrupt OBs in your program.

You can use the CAN_DINT instruction to prevent the execution of a time-delay interrupt that has not yet started.

##### Function of time-delay interrupt OBs

The operating system starts the corresponding OB after the delay time, which you have transferred with an OB number and an identifier to the SRT_DINT instruction.

To use a time-delay interrupt OB, you must execute the following tasks:

- You must call the instruction SRT_DINT.
- You must download the time-delay interrupt OB to the CPU as part of your program.

The delay time is measured with a precision of 1 ms. A delay time can immediately start again after it expires.

Time delay interrupt OBs are executed only when the CPU is in the "RUN" mode. A warm restart clears all start events of time-delay interrupt OBs.

The operating system calls the time-delay interrupt OB if one of the following events occurs:

- If the operating system attempts to start an OB that is not loaded and you specified its number when calling the SRT_DINT instruction.
- If the next start event for a time-delay interrupt occurs before the time delay OB has completely executed.

You can disable and re-enable time-delay interrupts using the DIS_AIRT and EN_AIRT instructions.

> **Note**
>
> If you disable an interrupt with DIS_AIRT after executing SRT_DINT, this interrupt executes only after it has been enabled with EN_AIRT. The delay time is extended accordingly.

##### Start information

- None
- Optimized start information:

| Name | Data type | Meaning |
| --- | --- | --- |
| sign | WORD | User ID: Input parameter SIGN from the call of the "SRT_DINT" instruction |

> **Note**
>
> **"sign" tag**
>
> The "sign" tag exists only since firmware version V4.1 of the S7-1200 CPUs. See [Useful information on CPU firmware versions and STEP 7 versions](#useful-information-on-cpu-firmware-versions-and-step-7-versions-s7-1200)

---

**See also**

[SRT_DINT: Start time-delay interrupt (S7-1200, S7-1500)](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#srt_dint-start-time-delay-interrupt-s7-1200-s7-1500)
  
[CAN_DINT: Cancel time-delay interrupt (S7-1200, S7-1500)](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#can_dint-cancel-time-delay-interrupt-s7-1200-s7-1500)
  
[Organization blocks (OB)](Programming%20basics.md#organization-blocks-ob)
  
[Events and OBs (S7-1200)](#events-and-obs-s7-1200)

#### Cyclic interrupt OBs (S7-1200)

##### Description

Cyclic interrupt OBs serve to start program in periodic time intervals independently of the cyclic program execution. The start times of a cyclic interrupt OB are specified using the time base and the phase offset.

The time base defines the intervals at which the cyclic interrupt OB is started and is an integer multiple of the basic clock cycle of 1 ms. The phase offset is the time by which the start time is offset compared with the basic clock cycle. If several cyclic interrupt OBs are being used, you can use this offset to prevent a simultaneous start time if the time bases of the cyclic interrupt OBs have common multiples.

You can specify a time period between 1 ms and 60000 ms as the time base.

You can use up to four cyclic interrupt OBs or time-delay interrupt OBs in your program. If, for example, you are already using two time-delay interrupt OBs, you can insert a maximum of two further cyclic interrupt OBs in your program.

> **Note**
>
> The execution time of each cyclic interrupt OB must be noticeably smaller than its time base. If a cyclic interrupt OB has not been completely executed but execution is again pending because the cycle clock has expired, the time error OB is started. The cyclic interrupt that caused the error is executed later or discarded.

##### Example of the use of phase offset

You have inserted two cyclic interrupt OBs in your program:

- Cyclic interrupt OB1
- Cyclic interrupt OB2

For cyclic interrupt OB1, you have set a time base of 20 ms and for cyclic interrupt OB2 a time base of 100 ms. After expiration of the time base of 100 ms, the cyclic interrupt OB1 reaches the start time for the fifth time, cyclic interrupt OB2 for the first time. To nevertheless execute the cyclic interrupt OBs offset, enter a phase offset for one of the two cyclic interrupt OBs.

##### Start information

- None
- Optimized start information:

| Name | Data type | Meaning |
| --- | --- | --- |
| first_scan | BOOL | = TRUE in the first call of this OB  - At the transition from STOP or HOLD to RUN - After reloading |
| event_count | INT | Number of lost start events since the last start of this OB |

---

**See also**

[Organization blocks (OB)](Programming%20basics.md#organization-blocks-ob)
  
[Assigning parameters to cyclic interrupt OBs (S7-1200)](#assigning-parameters-to-cyclic-interrupt-obs-s7-1200)
  
[Events and OBs (S7-1200)](#events-and-obs-s7-1200)

#### Hardware interrupt OBs (S7-1200)

##### Description

You can use hardware interrupt OBs to react to specific events. You can assign an event that triggers an alarm to precisely one hardware interrupt OB. A hardware interrupt OB in contrast can be assigned to several events.

Hardware interrupts can be triggered by high-speed counters and input channels. For each high-speed counter and input channel that should trigger a hardware interrupt, the following properties need to be configured:

- The process event that should trigger the hardware interrupt (for example, the change of a count direction of a high-speed counter)
- The number of the hardware interrupt OB which is assigned to this process event

You can use up to 50 hardware interrupt OBs (OB numbers &gt;= 123) that are independent of each other in your program.

##### Functionality of a hardware interrupt OB

After triggering a hardware interrupt, the operating system identifies the channel of the input or the high-speed counter and determines the assigned hardware interrupt OB.

If no other interrupt OB is active, the determined hardware interrupt OB is called. If a different interrupt OB is already being executed, the hardware interrupt is placed in the queue of its priority class. The hardware interrupt is acknowledged after the completion of the assigned hardware interrupt OB.

If another event that triggers a hardware interrupt occurs on the same module during the time between identification and acknowledgement of a hardware interrupt, the following applies:

- If the event occurs on the channel that previously triggered the hardware interrupt, then no additional hardware interrupt is triggered. Another hardware interrupt can only be triggered if the current hardware interrupt is acknowledged.
- If the event occurs on a different channel, a hardware interrupt is triggered.

Hardware interrupt OBs are called only in the CPU's "RUN" mode.

##### Start information

- None
- Optimized start information:

| Name | Data type | Meaning |
| --- | --- | --- |
| Laddr | HW_IO | Hardware identifier of the module that triggers the hardware interrupt |
| USI | WORD | Identifier for future extensions (not user-relevant) |
| IChannel | USINT | Number of the channel that triggered the hardware interrupt |
| EventType | BYTE | Identifier for the event type associated with the event triggering the interrupt (e.g., positive edge)  This identifier can be found in the description of the respective module. |

---

**See also**

[Organization blocks (OB)](Programming%20basics.md#organization-blocks-ob)
  
[Assigning parameters to hardware interrupt OBs (S7-1200)](#assigning-parameters-to-hardware-interrupt-obs-s7-1200)
  
[Events and OBs (S7-1200)](#events-and-obs-s7-1200)

#### Time error OB (S7-1200)

##### Description

The operating system calls the time error OB (OB 80) if one of the following events occurs:

- The cyclic program exceeds the maximum cycle time.
- The OB called is currently still being executed (possible for time-delay interrupt OBs and cyclic interrupt OBs).
- A time-of-day interrupt was missed because the clock time was set forward by more than 20 seconds.
- A time-of-day interrupt was missed during a STOP.
- An overflow has occurred in an interrupt OB queue.
- An interrupt was lost due to the excessive interrupt load.

If you have programmed no time error OB, the S7-1200 CPU reacts as follows:

- CPUs with firmware version V1.x to V3.x: The CPU remains in RUN mode.
- CPUs with firmware version as of V4.x:

  - The CPUs goes to STOP mode when the maximum cycle time is exceeded.
  - With all other start events of the time error OB, the CPU remains in RUN mode.

Violation of the maximum cycle time twice does not lead to the calling of an OB, but to the STOP of the CPU. You can avoid the second violation by restarting the cycle monitoring of the CPU with the RE_TRIGR instruction.

You can use only one time error OB in your program.

##### Start information

The time error OB has the following start information:

| Tag | Data type | Description |
| --- | --- | --- |
| fault_id | BYTE | - 0x01: Maximum cycle time exceeded - 0x02: Called OB is still being executed - 0x05: Expired time-of-day interrupt due to time jump - 0x06: Expired time-of-day interrupt on return to RUN mode - 0x07: Queue overflow - 0x09: Interrupt loss due to high interrupt load |
| csg_OBnr | OB_ANY | Number of the OB being executed at the time of the error |
| csg_prio | UINT | Priority of the OB being executed at the time of the error |

---

**See also**

[Organization blocks (OB)](Programming%20basics.md#organization-blocks-ob)
  
[Events and OBs (S7-1200)](#events-and-obs-s7-1200)
  
[Cycle time and maximum cycle time (S7-1200)](#cycle-time-and-maximum-cycle-time-s7-1200)

#### Diagnostic interrupt OB (S7-1200)

##### Description

You can enable the diagnostic error interrupt for diagnostics-capable modules so that the module detects changes in the I/O status. As a result, the module triggers a diagnostic error interrupt in the following cases:

- A fault is present (incoming event)
- A fault is no longer present (outgoing event)

If no other interrupt OB is active, then the diagnostic interrupt OB (OB 82) is called. If another interrupt OB is already being executed, the diagnostic error interrupt is placed in the queue of its priority group.

You can use only one diagnostic interrupt OB in your program.

##### Start information

The diagnostic interrupt OB has the following start information:

| Tag | Data type | Description |
| --- | --- | --- |
| IO_state | WORD | Contains the I/O status of the diagnostics-capable module. |
| laddr | HW_ANY | HW-ID |
| Channel | UINT | Channel number |
| multi_error | BOOL | = 1, if there is more than one error |

##### IO_state tag

The following table shows the possible I/O states that the IO_state tag can contain:

| IO_state | Description |
| --- | --- |
| Bit 0 | Configuration correct:  = 1, if the configuration is correct  = 0, if the configuration is no longer correct |
| Bit 4 | Error:  = 1, if an error is present, e.g., a wire break  = 0, if the error is no longer present |
| Bit 5 | Configuration not correct:  = 1, if the configuration is not correct  = 0, if the configuration is correct again |
| Bit 7 | I/O cannot be accessed:  = 1, if an I/O access error has occurred In this case, laddr contains the hardware identifier of the I/O with the access error.   = 0, if the I/O can be accessed again |
| Bits 8 to 15 | Reserved (always 0) |

---

**See also**

[Organization blocks (OB)](Programming%20basics.md#organization-blocks-ob)
  
[Events and OBs (S7-1200)](#events-and-obs-s7-1200)

#### Pull/plug interrupt OB (S7-1200)

##### Description

The S7-1200 CPU operating system calls the pull/plug interrupt OB (OB 83) if a configured and non-disabled distributed I/O module or submodule (PROFIBUS, PROFINET, AS-i) is removed or inserted.

> **Note**
>
> The removal or insertion of a central module leads to the STOP of the CPU.

##### Start information

The pull/plug interrupt OB has the following start information:

| Name | Data type | Meaning |
| --- | --- | --- |
| LADDR | HW_IO | Hardware identifier of the affected module or submodule |
| Event_Class | BYTE | - B#16#38: (Sub)module plugged - B#16#39: (Sub)module pulled or not responding |
| Fault_ID | BYTE | Error code (possible values: B#16#51, B#16#54, B#16#55, B#16#56, B#16#57, B#16#58) |

The following table shows which event caused the start of the pull/plug interrupt OB.

| ev_class (B#16# ...) | fault_id (B#16# ...) | Meaning |
| --- | --- | --- |
| 39 | 51 | Module pulled |
| 39 | 54 | Submodule pulled |
| 38 | 54 | Submodule plugged, which conforms to the parameterized submodule |
| 38 | 55 | Submodule inserted, which does not conform to the submodule parameter assignment |
| 38 | 56 | Submodule inserted, but error in module parameter assignment |
| 38 | 57 | Submodule or module inserted, but with a fault or maintenance |
| 38 | 58 | Submodule access error remedied |

---

**See also**

[Events and OBs (S7-1200)](#events-and-obs-s7-1200)

#### Rack error OB (S7-1200)

##### Description

The S7-1200 CPU operating system calls the OB 86 in the following cases:

- The failure of a DP master system or of a PROFINET IO system is detected (in the case of either an incoming or an outgoing event).
- The failure of a DP slave or of an IO device is detected (in the case of either an incoming or an outgoing event).
- Failure of some of the submodules of a PROFINET I-device is detected.

##### Structure of the start information

The rack fault OB has the following start information:

| Name | Data type | Meaning |
| --- | --- | --- |
| LADDR | HW_IO | Hardware identifier of the defective hardware object |
| Event_Class | BYTE | - B#16#32: Activation of a DP slaves or an IO device - B#16#33: Deactivation of a DP slaves or an IO device - B#16#38: outgoing event - B#16#39: incoming event |
| Fault_ID | BYTE | Error code (possible values: B#16#C3, B#16#C4, B#16#C5, B#16#C6, B#16#C7, B#16#C8, B#16#C9, B#16#CA, B#16#CB, B#16#CC, B#16#CD, B#16#CE, B#16#CF, B#16#F8, B#16#F9) |

The following table shows which event caused the start of OB 86.

| Ev_class  B#16# ... | Fault_id  B#16# ... | Meaning |
| --- | --- | --- |
| 39 | C3 | Failure of a DP master system |
| 39/38 | C4 | Failure/return of a DP slave |
| 38 | C5 | Return of a DP slave; however, slave is faulty |
| 38 | C6 | Expansion unit return, but error in module parameter assignment |
| 38 | C7 | Return of a DP device, but there is error in module configuration |
| 38 | C8 | Return of a DP device, but discrepancy between preset/actual configuration |
| 32/33 | C9 | Activation/deactivation of a DP slave with the "D_ACT_DP" instruction |
| 39 | CA | Failure of a PROFINET IO system |
| 39/38 | CB | Failure/return of a PROFINET IO device |
| 38 | CC | Return of a PROFINET IO device with fault or maintenance |
| 38 | CD | Return of a PROFINET IO device, deviation between preset/actual configuration |
| 38 | CE | Return of a PROFINET IO device, error in module configuration |
| 32/33 | CF | Activation/deactivation of an IO device with the "D_ACT_DP" instruction |
| 39/38 | F8 | Failure/return of some of the submodules of a PROFINET I-device |
| 38 | F9 | Return of some of the submodules of a PROFINET I-device with a device configuration difference |

---

**See also**

[Events and OBs (S7-1200)](#events-and-obs-s7-1200)

#### MC-servo OB (S7-1200)

##### Description

When you create a technology object with drive connection using MC-Servo [OB91]/create an analog output, the organization block PROFIdrive is created automatically. The Motion Control functionality of the technology objects creates its own execution level, and is called according to the Motion Control application cycle.

The MC-Servo OB is write-protected. The content cannot be changed.

The position control algorithms of all technology objects configured for motion control on the CPU are calculated within the MC-Servo OB.

You can set the application cycle and the priority of the organization block in accordance with your requirements for control quality and system load.

##### Application cycle

You can set the application cycle in which the MC-Servo OB is called in the properties of the organization block.

The MC-Servo OB is called cyclically with the specified application cycle.

The selected application cycle must be long enough to allow all the technology objects to be processed in one cycle. If the processing time of the technology objects is longer than the application cycle, overflows will occur.

To avoid disruptions in the program execution on the CPU, set the application cycle depending on the number of axes used as follows:

Application cycle = number of axes x 2 ms

The following table shows the resulting application cycle as an example according to the number of axes:

| Number of axes | Application cycle |
| --- | --- |
| 1 | 2 ms |
| 2 | 4 ms |
| 4 | 8 ms |
| 8 | 16 ms |

The SINAMICS G120 drive updates the drive process image every 4 ms. To improve control, set the application cycle of the MC-Servo OB to 4 ms or to a multiple of 4 ms.

---

**See also**

[MC-PreServo OB (S7-1200)](#mc-preservo-ob-s7-1200)
  
[MC-PostServo OB (S7-1200)](#mc-postservo-ob-s7-1200)
  
[MC-interpolator OB (S7-1200)](#mc-interpolator-ob-s7-1200)
  
[Assigning the MC-Servo OB parameters (S7-1200)](#assigning-the-mc-servo-ob-parameters-s7-1200)

#### MC-PreServo OB (S7-1200)

##### Description

The organization block MC-PreServo [OB67] can be programmed and is called in the application cycle configured at the [MC-Servo OB](#mc-servo-ob-s7-1200). MC-PreServo [OB67] is called directly before MC-Servo [OB91].

Via the organization block, you can read out the configured application cycle (information in µs).

##### Structure of the start information

Optimized start information:

| Name | Data type | Meaning |
| --- | --- | --- |
| Initial_Call | BOOL | =TRUE in the first call of this OB during transition from STOP to RUN |
| PIP_Input | BOOL | TRUE: The associated process image input is up-to-date |
| PIP_Output | BOOL | TRUE: The associated process image output was transferred to the outputs in good time after the last cycle |
| IO_System | USINT | Number of the distributed I/O system triggering the interrupt |
| Event_Count | INT | - = n: Number of lost cycles - = -1: An unknown number of cycles has been lost (e.g., because cycle has changed). |
| Synchronous | BOOL | Reserved |
| CycleTime | UDINT | Display of the application cycle configured for the MC-Servo OB in μs |

#### MC-PostServo OB (S7-1200)

##### Description

The organization block MC-PostServo [OB95] can be programmed and is called in the application cycle configured for the [MC-Servo OB](#mc-servo-ob-s7-1200). MC-PostServo [OB95] is called directly after MC-Servo [OB91].

Via the organization block, you can read out the configured application cycle (information in µs).

##### Structure of the start information

Optimized start information:

| Name | Data type | Meaning |
| --- | --- | --- |
| Initial_Call | BOOL | =TRUE in the first call of this OB during transition from STOP to RUN |
| PIP_Input | BOOL | TRUE: The associated process image input is up-to-date |
| PIP_Output | BOOL | TRUE: The associated process image output was transferred to the outputs in good time after the last cycle |
| IO_System | USINT | Number of the distributed I/O system triggering the interrupt |
| Event_Count | INT | - = n: Number of lost cycles - = -1: An unknown number of cycles has been lost (e.g., because cycle has changed). |
| Synchronous | BOOL | Reserved |
| CycleTime | UDINT | Display of the application cycle configured for the MC-Servo OB in μs |

#### MC-interpolator OB (S7-1200)

##### Description

When you create a technology object with drive connection using MC‑Interpolator [OB91]/create an analog output, the organization block PROFIdrive is created automatically. The Motion Control functionality of the technology objects creates its own execution level, and is called according to the Motion Control application cycle of the [MC-Servo OB](#mc-servo-ob-s7-1200).

The MC-Interpolator OB is write-protected. The content cannot be changed.

The evaluation of the motion control instructions as well as the monitoring and the setpoint generation for all technology objects configured on the CPU (motion control) is performed within the MC-Interpolator OB.

The MC-Interpolator OB is called at the end of processing of the MC-Servo OB. The clock ratio between MC-Interpolator OB and MC-Servo OB is always 1:1.

##### Process response

You must select the application cycle of the MC-Servo OB long enough to allow all the technology objects for motion control to be processed in one application cycle. If the application cycle is not observed, overflows occur. Note the following response to overflows:

- The CPU tolerates a maximum of three consecutive overflows of the MC-Interpolator OB.
- The processing of an MC-Interpolator OB can be interrupted by the calling of the MC Servo OB, at most.

### Block parameters of organization blocks (S7-1200)

This section contains information on the following topics:

- [Basics of block parameters (S7-1200)](#basics-of-block-parameters-s7-1200)
- [Parameter assignment for time-of-day interrupt OBs (S7-1200)](#parameter-assignment-for-time-of-day-interrupt-obs-s7-1200)
- [Assigning parameters to cyclic interrupt OBs (S7-1200)](#assigning-parameters-to-cyclic-interrupt-obs-s7-1200)
- [Assigning parameters to hardware interrupt OBs (S7-1200)](#assigning-parameters-to-hardware-interrupt-obs-s7-1200)
- [Assigning the MC-Servo OB parameters (S7-1200)](#assigning-the-mc-servo-ob-parameters-s7-1200)

#### Basics of block parameters (S7-1200)

##### Introduction

Several organization blocks (OBs) have properties with which you can control their behavior or their assignment to specific events. You can influence these properties by assigning parameters.

##### Overview

You can assign parameters to the properties for the following organization blocks:

- Time-of-day interrupt OBs
- Cyclic interrupt OBs
- Hardware interrupt OBs
- MC-Servo OB

---

**See also**

[Assigning parameters to hardware interrupt OBs (S7-1200)](#assigning-parameters-to-hardware-interrupt-obs-s7-1200)
  
[Assigning parameters to cyclic interrupt OBs (S7-1200)](#assigning-parameters-to-cyclic-interrupt-obs-s7-1200)

#### Parameter assignment for time-of-day interrupt OBs (S7-1200)

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

Example: Start date = 07/05/2013, time =11:16

Depending on the value of the "Execution" parameter, the CPU generates additional time-of-day interrupts periodically. Depending on the setting, the start time relates either to the local time or to the coordinated universal timeUTC.

> **Note**
>
> If you set the "Execution" parameter to "Monthly", the start date cannot be set to the 29th, the 30th, or the 31st. If you want the time-of-day interrupt OB to start at the end of the month, you should set the parameter "Execution" to "End of month".

##### "Local time" or "System time"

Here, you decide which time the start time of the time-of-day interrupt OB relates to:

- "Local time": The start time relates to the time zone set for the CPU.
- "System time": The start time relates to the coordinated universal time UTC (Universal Time Coordinated).

#### Assigning parameters to cyclic interrupt OBs (S7-1200)

##### Introduction

You can use cyclic interrupt OBs to start programs at regular time intervals. To do so you must enter a scan time and a phase shift for each cyclic interrupt OB used.

You can use up to four cyclic interrupt OBs or time-delay OBs (OB numbers &gt;= 200) in your program. If, for example, you are already using two time-delay interrupt OBs, you can insert a maximum of two further cyclic interrupt OBs in your program.

> **Note**
>
> If you assign multiple cyclic OBs, make sure that you assign a different cycle time or phase offset to each cyclic interrupt OB to avoid them executing at the same time or having to queue. When you create a cyclic interrupt OB, the cycle time 100 and the phase offset 0 are entered as start value.

##### Procedure

To enter a scan time and a phase shift for a cyclic interrupt OB, proceed as follows:

1. Open the "Program blocks" folder in the project tree.
2. Right-click on an existing cyclic interrupt OB.
3. Select the "Properties" command in the shortcut menu.

   The "&lt;Name of the cyclic interrupt OB&gt;" dialog box opens.
4. Click the "Cyclic interrupt" group in the area navigation.

   The text boxes for the scan time and the phase shift are displayed.
5. Enter the scan time and the phase shift.
6. Confirm your entries with "OK".

---

**See also**

[Creating organization blocks](Creating%20and%20managing%20blocks.md#creating-organization-blocks)
  
[Basics of block parameters (S7-1200)](#basics-of-block-parameters-s7-1200)
  
[Cyclic interrupt OBs (S7-1200)](#cyclic-interrupt-obs-s7-1200)

#### Assigning parameters to hardware interrupt OBs (S7-1200)

##### Introduction

You must select the corresponding event and assign the following parameters for every input channel and high-speed counter that should trigger a hardware interrupt:

- Event name
- Number of the hardware interrupt OB that is assigned to this process event

The parameters of the hardware interrupt are assigned in the properties of the corresponding device. You can assign parameters for up to 50 hardware interrupt OBs.

You can create the hardware interrupt OB to be assigned parameters either before or during activation of an event.

##### Procedure

To configure a hardware interrupt event, follow these steps:

1. Double-click the "Devices &amp; Networks" command in the project tree.

   The hardware and network editor opens in the network view.
2. Change to the device view.
3. If the Inspector window closed in the device view, select the "Inspector window" check box in the "View" menu.

   The Inspector window opens.
4. Click the "Properties" tab.
5. In the device view, select the module for which you want to a assign a hardware interrupt.
6. Select the corresponding event that will trigger a hardware interrupt, e.g., a positive edge.

   ![Procedure](images/37656394635_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/37656394635_DV_resource.Stream@PNG-en-US.png)
7. Enter an event name.
8. Select an existing hardware interrupt OB from the "Hardware interrupt" drop-down list or create a new hardware interrupt OB. If you have not previously created any hardware interrupt OBs, you can click the "Add new block" button in the drop-down list.

   The start information of the corresponding hardware interrupt OB, including all specifications for the interrupt-triggering event, is updated.

   ![Procedure](images/37656398603_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/37656398603_DV_resource.Stream@PNG-en-US.png)
9. If you want to assign further hardware interrupts, repeat steps 5 to 8.

A system constant of data type Event_HwInt is created automatically for the event identified by the explicit event name. The system constants are displayed in the standard tag table.

---

**See also**

[Creating organization blocks](Creating%20and%20managing%20blocks.md#creating-organization-blocks)
  
[Basics of block parameters (S7-1200)](#basics-of-block-parameters-s7-1200)
  
[Hardware interrupt OBs (S7-1200)](#hardware-interrupt-obs-s7-1200)
  
[Events and OBs (S7-1200)](#events-and-obs-s7-1200)

#### Assigning the MC-Servo OB parameters (S7-1200)

##### Procedure for setting the parameters

To assign the parameters of an MC-Servo OB, follow these steps:

1. Open the "Properties" dialog associated with the MC-Servo OB in question.
2. Click on the "Cycle time " group in the area navigation.

##### Overview of the parameters that can be set

In the "Cycle time" group, select the application cycle with which the MC-Servo OB will be called cyclically in the execution system of the SIMATIC S7-1200

You set the cycle in which the MC-Servo OB is called in the "Application cycle" field.

---

**See also**

[Basics of block parameters (S7-1200)](#basics-of-block-parameters-s7-1200)
  
[MC-servo OB (S7-1200)](#mc-servo-ob-s7-1200)

## Useful information on CPU firmware versions and STEP 7 versions (S7-1200)

CPUs and engineering software for configuring the CPUs is constantly developed further to improve performance and security. New versions that have some special features with respect to the interaction of the components are created in this way. The sections below describe the special features of the S7-1200 CPUs with firmware version V4 as compared to firmware versions V1 to V3.

For a detailed comparison of the range of functions, read the S7-1200 System Manual (description of new instructions, new organization blocks and advanced configuration options).

### Required engineering software

S7-1200 CPUs V4 can be configured with STEP 7 as of V13.

### Compatibility between memory card content and firmware version of the CPU

Memory cards (transfer cards or program cards) with configuration and program for an S7-1200 CPU V1, V2 or V3 do not work with an S7-1200 CPU V4.   
Memory cards with configuration and program for an S7-1200 CPU V4 do not work with an S7-1200 CPU V1, V2 or V3.

You must change an S7-1200 CPU V1 to V3 configuration to an S7-1200 CPU V4 configuration (device replacement) and then download it to the CPU. A gradual device replacement is required for an S7-1200 CPU V1-V2 (see below).

When you insert the memory card into a CPU with an incompatible firmware version, the CPU does not start up. When you insert a memory card for a CPU V1, V2 or V3 into an S7-1200 CPU V4, this CPU outputs a version error.

### Going online and loading

When you have configured an S7-1200 CPU with firmware version V1, V2 or V3 with STEP 7, the CPU to which you want to go online or which you want to download must have one of these firmware versions. You cannot go online to an S7-1200 CPU V4 with a configured S7-1200 CPU V1, V2 or V3.

On the other hand, you cannot go online to an S7-1200 CPU V1, V2 or V3 with a configured S7-1200 CPU V4 or download this CPU.

### Replacing an existing CPU

You can replace a configured S7-1200-CPU V1, V2 or V3 with a new CPU with a firmware version greater than or equal to 4. In case of an existing S7-1200 CPU V1 or V2, you must start by replacing the device with an S7-1200 CPU V3: It is not possible to directly replace it with an S7-1200 CPU V4.

1. S7-1200 CPU V1 (V2) &gt; S7-1200 CPU V3
2. S7-1200 CPU V3 &gt; S7-1200 CPU V4

As long as you do not download the configuration, you can undo the device replacement ("Undo" command in the "Edit" menu). When you download the configuration for the new CPU firmware version ("V4 configuration") to the CPU, you can no longer return to version V3.

This means you should save the existing project, for example, with a V3 configuration as project archive so that you can access it later.

Special notes for device replacement (V3 &gt; V4):

- The interrupt behavior of interrupt OBs remains the same; they are not configured as interruptible. This is also the default behavior of S7-1200 CPUs V1-V3. The interrupt behavior of the interrupt OB can be configured for S7-1200 V4 CPUs. If you drag an S7-1200 CPU V4 directly from the hardware catalog into the network view, this option is activated (interrupt OBs are interruptible).
- The behavior for PUT/GET access of remote partners remains the same; access is permitted. This is also the default behavior of S7-1200 CPUs V1-V3. The access via PUT/GET communication by means of remote partners can be configured for S7-1200 V4 CPUs ("Protection" area of CPU parameters). If you drag an S7-1200 CPU V4 directly from the hardware catalog into the network view, access is not permitted and must be explicitly enabled.
- The wording for the protection levels changes but the effect of the settings remains the same. You can also select the access level "No access (complete protection)".
- The web server settings for activation of the web server and HTTP/HTTPS settings are applied. You also have the option to create users and assign them specific rights (Web server area &gt; User management of CPU parameters). Web server users only have access to standard websites when you do not configure users. An S7-1200 CPU V4 no longer supports the user "admin" and his/her password.
- For reasons of compatibility, the interfaces of used OBs are not changed by the device replacement. You can therefore continue to use used OBs. If you want to use OB properties that have been added or changed in the new firmware version of the S7-1200 CPU, you will need to recreate the corresponding OB.

### Communication with HMI devices

When you connect an HMI device to an S7-1200 CPU V4, make sure that you use the appropriate Runtime software version of the HMI device.

You may have to transfer the latest HMI Runtime version by means of the WinCC engineering software.

You must compile the HMI configuration once again and download it to the HMI device for the CPU-HMI communication to work.

---

**See also**

[What you need to know about SIMATIC memory cards (S7-1200)](#what-you-need-to-know-about-simatic-memory-cards-s7-1200)

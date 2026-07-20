---
title: "Commissioning projects with PLC synchronization"
package: ProgTeamGIB2MenUS
topics: 5
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Commissioning projects with PLC synchronization

This section contains information on the following topics:

- [Basics of PLC synchronization](#basics-of-plc-synchronization)
- [Requirements for PLC synchronization](#requirements-for-plc-synchronization)
- [Procedure for PLC synchronization](#procedure-for-plc-synchronization)
- [Rules for PLC synchronization](#rules-for-plc-synchronization)

## Basics of PLC synchronization

### Introduction

You have the option to perform PLC synchronization of projects as part of Team Engineering . Several editors can access one CPU at the same time with up to five Engineering Systems (ES) in this process.

A special advantage is that parts of a master project can be edited independently and offline at the same time during the commissioning phase. The changes of the other editors are displayed in the dialog "Software synchronization" during loading and synchronized automatically, if possible.

Depending on the firmware version of the CPU in use, certain online functions can also be executed at the same time from several Engineering Systems on the shared CPU, for example:

- Monitoring blocks on the CPU
- Modifying and forcing blocks on the CPU
- Trace functions

The following online functions cannot be executed at the same time:

- Loading: Only one ES can load to the CPU.

You can also find additional information on the topic of Team Engineering at [Service and support in Siemens Industry online support](http://support.automation.siemens.com/WW/view/en/82142829).

### Creating a master project

A ["master project" structured according to the specified rules](#rules-for-plc-synchronization), which already contains the complete configured hardware configuration with all required tags and blocks, is used as the basis for PLC synchronization during shared commissioning. This project is loaded in the jointly used CPU and then distributed as "master project" by means of project copies to up to five participating Engineering Systems.

![Creating a master project](images/59566735499_DV_resource.Stream@PNG-en-US.png)

### Working with project copies

Each Engineering System only processes the parts it was assigned within the specific project copy. This is especially important to avoid conflicts during loading and unintentional overwriting of blocks that were already modified by other Engineering Systems.

Each ES loads its parts to the shared CPU after editing. The TIA Portal helps you during download to the CPU. The changes made since the last download are displayed in the dialog "Software synchronization before loading to a device" (hereafter referred to as "synchronization dialog"), by means of an online-offline comparison. You are provided recommendations during download to the CPU about how you can synchronize the offline data you have edited with the existing online data.

If there are "competing changes", you may have to synchronize them manually.

Competing changes are:

- when different editors edit the same block in different project copies at the same time.
- when PLC tags (I, Q, M, T, C) are added, changed or deleted in the project copies.
- when blocks that have relations to the hardware configuration are edited in the project copies.
- when F blocks are edited in the project copies.

Each editor loads their changes only after all conflicts have been removed.

The procedure for editing and loading of project copies can be repeated as often as necessary by the individual engineering systems until PLC synchronization during shared commissioning is complete.

### Integrating project copies into the master project once again

The individual project copies must once again be integrated into the master project at the end of PLC synchronization. This way you also back up the data that only exist in the offline projects and have not been downloaded to the CPU. These include, for example, the project languages and text lists created in the project copies.

To do this, open the master project and one project copy as reference object. You determine the differences between the two projects by performing an offline/offline comparison using the comparison editor. Copy the edited objects from the respective project copy to the master project. Repeat this step for all project copies.

When the shared commissioning with PLC synchronization is completed, you therefore have an executable master project with all created project data.

The integration of the project data into the master project is required even if you determine during the commissioning phase that the shared central elements need to be expanded or corrected, for example, the PLC tag table needs to be expanded, or a new hardware component needs to be added.

### Notes on compatibility

The following compatibility rules apply to PLC synchronization performed during shared commissioning:

- If an Engineering System with TIA Portal V13 or later is online on the CPU and performs a download, a second ES cannot establish an online connection, regardless of the version.
- If an Engineering System with TIA Portal < V13 is online on the CPU, a second ES cannot establish an online connection, regardless of the version.

### Team Engineering

As part of Team Engineering , you have the option to perform shared commissioning of projects. Several editors can access one CPU in parallel and at the same time with multiple Engineering Systems (ES) in this process.

### PLC synchronization

In PLC synchronization, multiple engineering systems work together and in parallel on one CPU as part of team engineering.

### Master project

The master project is the basic project for PLC synchronization. It is a project structured according to the specified rules which already contains the fully configured hardware configuration with all required tags and blocks. This project is loaded into the jointly used CPU and then distributed as "master project" by means of project copies to the participating Engineering Systems. Each Engineering System only processes the parts it was assigned within the specific project copy. The project copies are then integrated into the master project once again.

### Project copy

Project copies are created from structured master projects when working with team engineering and distributed to the participating Engineering Systems for editing. Each engineering system only processes the parts it was assigned within the specific project copy as part of PLC synchronization. The individual project copies are once again integrated into the master project at the end of PLC synchronization.

---

**See also**

[Requirements for PLC synchronization](#requirements-for-plc-synchronization)
  
[Procedure for PLC synchronization](#procedure-for-plc-synchronization)

## Requirements for PLC synchronization

### Software and hardware requirements

For shared commissioning of projects, the minimum software and hardware requirements for the installation of TIA Portal V13 or later must be met.

The following requirements also apply:

Software:

- You have installed TIA Portal V13 or later and the "SIMATIC STEP 7 Professional" software package on the involved Engineering Systems.
- The same software version must be installed on all Engineering Systems.
- The master project must have been created with a project of V13 or later, which has been updated to the version of the TIA Portal used in the engineering system.
- After switching from a lower to a higher TIA Portal version, all involved engineering systems must use this version.
- After switching from a lower to a higher TIA Portal version, the master project must centrally adapted and new project copies must be transferred to the engineering systems involved.

Hardware:

- You have access to a fully configured CPU S7-1500 as of firmware version V1.5.
- The involved Engineering Systems can establish an online connection to this CPU.

### Requirements for shared, parallel working on the project

The following requirements are in effect for shared commissioning of projects:

- You have created a project with complete hardware configuration and fully programmed user program that can be commissioned.
- The project was downloaded to the CPU and defined as "master project".
- Multiple Engineering Systems have access to this CPU and can establish an online connection to this CPU.
- You are familiar with the defined rules and procedures for working together on one CPU.

### Note on compatibility mode

The functions for PLC synchronization are not available in compatibility mode.

---

**See also**

[Basics of PLC synchronization](#basics-of-plc-synchronization)
  
[Procedure for PLC synchronization](#procedure-for-plc-synchronization)
  
[Rules for PLC synchronization](#rules-for-plc-synchronization)

## Procedure for PLC synchronization

### Introduction

If you are performing shared commissioning of a project as part of team engineering, it is very important that all editors of the project observe a defined procedure.

Only when the specified procedure is observed are changes and corrections in the project automatically synchronized and applied, and changes of individual editors not unintentionally overwritten during loading or even lost in case of competing changes.

### Procedure for creating the master project

The master project is created in the following steps:

1. Create a master project that includes the entire project structure.
2. Fully configure the hardware for the master project.
3. Define a language as project language, which must also be used exclusively by all participating engineering systems.
4. Create all tags and blocks that are required in the master project.
5. Create your own folders and groups for the blocks to be edited by the individual engineering systems.
6. Create a fully programmed and executable user program.
7. Download the master project to the shared CPU.
8. Save the master project following every download.

You should also note the [Rules for PLC synchronization](#rules-for-plc-synchronization).

### Procedure for PLC synchronization

PLC synchronization is performed with the following steps:

1. Download the master project to the shared CPU.
2. Create copies of the master project and distribute them to the editors involved in the project on the associated engineering systems.
3. Inform all editors who is to edit the specific parts of the project copies and who may download to the CPU.
4. Have the project copies edited in the individual engineering systems.
5. After editing, the individual engineering systems download the changes one after the other to the CPU.
6. All changes are automatically detected during loading by means of an online-offline comparison. The displayed synchronization dialog offer you recommendations for synchronizing the modified data when possible. You may first have to download blocks that were edited by other editors to your ES before you can download your changes to the CPU. This may be needed to update the corrections of the other editors that have already been downloaded to the CPU in your project copy.

   The following synchronization options are available:

   - Download block: There are edited blocks on the CPU that must be updated in your project copy.
   - Download block: There are new blocks on the CPU that must be downloaded to your project copy.
   - Blocks with competing changes: System-supported synchronization is not possible in this case; the conflict must be resolved manually.
7. Manually resolve any conflicts that may occur due to competing changes or changes to central objects.
8. Download your project copy to the CPU when all conflicts have been removed.
9. Save your project copy following every download.
10. Repeat editing of project copies and download to the CPU as often as necessary until PLC synchronization is complete.
11. Integrate the completely edited project copies into the master project once again in order to also back up the project data that only exist offline.

You should also observe the [Rules for PLC synchronization](#rules-for-plc-synchronization).

### Procedure for manual synchronization of competing changes

Manual synchronization of competing changes is performed in the following steps:

1. Start the comparison editor to manually resolve a conflict displayed in the synchronization dialog during download to the CPU. Select the shared CPU in the project tree and select the "Compare > Offline/Online" command in the shortcut menu. You can define certain actions depending on the status of the objects. Note, however, that you can only perform actions in one direction during synchronizing.
2. First, select the action "Upload from device" for all blocks that were changed by other editors on the CPU and which you want to apply.
3. If necessary, perform a detailed comparison of the blocks to identify differences between your offline blocks and the online blocks loaded on the CPU.
4. Manually correct the competing changes to the blocks.
5. Then download the affected blocks to the CPU using the "Continue without synchronization" command.
6. Save your project or project copy following every download.

You should also note the [Rules for PLC synchronization](#rules-for-plc-synchronization).

> **Note**
>
> To prevent online changes occurring again while an engineering system is being manually synchronized, no downloading to the shared CPU should be performed by another participating engineering system during the manual synchronizing.

### Procedure for integrating project copies into the master project

You integrate project copies into the master project with the following steps:

1. Open the master project and the project copy to be integrated as a reference object.
2. Copy the program parts you have edited from the respective project copy to the master project and confirm overwriting the existing objects. You can also use the comparison editor to apply your program parts to the master project.
3. Save the master project and download it to the shared CPU with the "Continue without synchronization" command.
4. Save the master project following every download.

You should also note the [Rules for PLC synchronization](#rules-for-plc-synchronization).

### Procedure for modifying central objects within the master project

Modification of central objects that have an effect on all program parts is performed with the following steps:

1. Stop further processing of the project copies.
2. Integrate all existing project copies one after the other into the master project as described above.
3. Download the master project to the shared CPU with the "Continue without synchronization" command.
4. Make the required modification on the shared objects such as in the hardware configuration, for example, or in the PLC tag table. The procedure is the same for modification of other central objects such as technology objects, F blocks, OBs, etc.
5. Download the master project into the CPU once again when modification is complete.
6. Save the master project following every download.
7. Distribute the updated project copies to the respective engineering systems for further processing.

You should also note the [Rules for PLC synchronization](#rules-for-plc-synchronization).

---

**See also**

[Basics of PLC synchronization](#basics-of-plc-synchronization)
  
[Requirements for PLC synchronization](#requirements-for-plc-synchronization)
  
[Rules for PLC synchronization](#rules-for-plc-synchronization)

## Rules for PLC synchronization

### Introduction

If you are performing PLC synchronization of a project as part of team engineering, it is very important that all editors of the project observe predefined rules for successful cooperation.

### Rules for the master project

The following rules are to be observed:

- Create a master project that is suitable for shared editing.
- Divide the user program into program parts that are independent of each other.
- Use "Groups" to visually separate the program parts from each other.
- Use a main OB and a central FC for each program part which calls the functions of the part program.
- If possible, create a separate PLC tag table for each part.
- In the master project, specify a project language which cannot be changed in the project copies.
- If you want to exchange data between the program parts, use the FC and FB interface parameters (IN, OUT, INOUT) or global data blocks.
- Use global data blocks to save the data for the individual program parts, no bit memories.
- Do not assign different names for blocks with identical addresses.
- Do not assign identical names for blocks with different addresses.

### Example of the program structure in the master project

Here is an example of a team-capable, structured master project that is suitable for parallel editing during PLC synchronization.

The program parts to be edited by the individual Engineering Systems are:

- Program part 1: "Conveyer"
- Program part 2: "Drill"
- Program part 3: "FurtherProgramPart"

Each program part contains a "main FB", which calls the specific lower-lever functions for this program part.

Example: In the "Conveyer" program part, the "ConveyerMainFB" calls the "ConveyerStartupFC" function.

![Example of the program structure in the master project](images/60248928779_DV_resource.Stream@PNG-en-US.png)

In team engineering, this subdivision within the project structure allows the parallel editing of individual program parts and the automatic synchronization of changes during the shared commissioning phase.

### Rules for shared working on one CPU

Observe the following rules for shared working:

- Editor only edits the blocks they have been assigned in the project copy in the assigned groups.
- Only OBs, FBs, DBs, FCs and UDTs may be changed in the project copies, which means the following program elements must **not** be edited in the project copies:

  - Hardware configurations
  - PLC tag table
  - Technology objects
  - Text lists and project language
  - F blocks
- Global data blocks should be used in programming instead of bit memories.
- IEC timers and counters should be used during programming instead of SIMATIC timers and counters.
- The project language specified in the master project may not be changed in the project copies.

### Rules for editing shared, central objects

Observe the following rules for shared central objects:

- Changes to shared central objects always have to be made by means of the master project.

  These objects include:

  - Hardware configurations
  - PLC tag table
  - Technology objects
  - Text lists and project language
  - F blocks
- Before the shared central objects can be modified in the master project, the various working versions within the project copies must first be integrated into the master project once again.
- The modification can then be made within the master project, and the master project can then be downloaded to the shared CPU.
- Once modification is complete, new project copies can be created and distributed to the Engineering Systems for further processing.

### Rules for working with organization blocks

Observe the following rules for editing OBs:

- OBs can only be created in the master project. If you create new OBs in a project copy, they **cannot** be synchronized.
- OBs that already exist in the master project and that have already been downloaded to the CPU, can be modified in the respective project copies. These OBs are automatically synchronized during downloading.

### Rules for downloading to the CPU

Observe the following rules for downloading:

- Editors can download the project copies one after the other to the CPU; only one Engineering System can download at any given time.
- The online connection of the involved Engineering Systems can be maintained when downloading the blocks (hardware may only be downloaded in the master project).
- Perform the synchronization that is offered automatically in the synchronization dialog during download. This ensures that changes from other editors are not unintentionally overwritten.
- Correct the name conflicts that are shown in the synchronization dialog, which you rename in your offline block before downloading to the CPU. A name conflict is indicated if you want to download to the CPU a block that already exists with identical name on the CPU.
- So-called "competing changes" must be corrected manually. Competing changes come about when two editors work on the same block on two Engineering Systems at the same time. The first editor can still download his or her changes to the CPU without any problems. However, if the second editor wants to download the same block with the changes the editor has made, the synchronization dialog displays a conflict that cannot be removed automatically. The previous changes made to this block would be undone by overwriting during download. The editors have to decide in this case which change is to be applied and which one is to be discarded. Alternatively, you can manually merge the changes with the help of the detailed comparison of the blocks in the comparison editor.

  Such changes should always be avoided by implementing a good project structure and corresponding agreements between the editors.
- Changes to central objects are displayed in the synchronization dialog but cannot be synchronized automatically. Changes to central objects and to the hardware configuration always have to be made by means of the master project.
- Save your project or project copy following every download.

> **Note**
>
> **Creating and subsequent deleting of objects in the project copies**
>
> Please note that a software synchronization is also required before downloading when you create a new object in a project copy and then delete this again immediately afterwards.
>
> The creation of an object causes a change in the internal data management which cannot be undone by the subsequent deleting of the object. As a result it is necessary to perform a synchronization before the next loading if the newly created object was deleted immediately thereafter and no change in the existing object is visible within the project copy.

### Rules for online functions

The following rules are to be observed when using online functions:

**Loading:**

- Only one Engineering System can download data to the CPU at any given time.
- Other Engineering Systems can use additional online functions during the download, such as monitoring and controlling.

**Monitoring and controlling:**

- Up to ten Engineering Systems can monitor and control up to 16 different blocks simultaneously on the CPU (CPU 1517/1518). Further details can be found in the CPU's technical specifications.
- A specific code block can only be monitored and controlled by one Engineering System at a time.
- However, additional Engineering Systems can simultaneously monitor and control other code blocks.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Danger due to modifying an identical operand in parallel with different modify values in more than one watch table**  When working with more than one watch table, avoid modifying identical operands permanently multiple times with different modify values.  If an identical operand is modified permanently with different modify values at the same time in different watch tables, all watch tables will display the last modified value, because the modify value assigned last will be used in this case. |  |

**Force**

- Forcing can only be implemented on the CPU from one Engineering System at a time.
- The Engineering Systems that starts the forcing has taken over the force job exclusively. Although the other Engineering Systems receive the information that a force job is running, they cannot access this job to make changes. Use the command "Update forced operands" to update all operands and values currently being forced on the CPU in the open force table. All forced operands in the open force table are updated with the relevant values. A red "F" is displayed in the first column indicating which operands are being forced.
- As soon as the Engineering System to which the force job belongs ends the online connection, the force job can be applied by another ES that establishes an online connection to the CPU and has executed the "Update forced operands" command. This enables the "Force all" and "Stop forcing" buttons and you can select these functions.

**Trace functions:**

- Up to four Engineering Systems can perform trace functions simultaneously.
- The Engineering Systems that starts the tracing has taken over the trace job exclusively. Although the other Engineering Systems can see this job in the trace editor, they cannot access it.
- As soon as the Engineering System to which the trace job belongs closes the trace editor, the trace job can be taken over by another ES that re-opens the trace editor.

**Testing with breakpoints:**

The following rules apply as soon as a breakpoint is enabled by an engineering system of an S7-1500 CPU as of firmware version V2.5:

- Enabling of breakpoints by other engineering systems is blocked.
- Enabling of additional breakpoints on the executing engineering system is permitted even if the CPU is in "HOLD" mode after a breakpoint has been reached.
- "Download to device" cannot be executed by a different engineering system, and the program on the CPU can no longer be executed because the CPU is in "HOLD" mode when a breakpoint is reached. Program execution is not continued until the CPU is set from "HOLD" mode back to "RUN" mode by the executing engineering system. Other engineering systems cannot switch the mode directly to "RUN" after a breakpoint has been reached. The CPU must first be set to "STOP" mode and can only be switched to "RUN" afterwards.
- If a "Download to device" is already in progress, no breakpoints can be enabled during the download process.
- "Download to device" is also possible in "HOLD" mode when no breakpoints are enabled. During the download, the CPU is set to "STOP" mode.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Enabling breakpoints on an S7-1500 CPU as of firmware version V2.5**  As soon as you enable a breakpoint on an S7-1500 CPU as of V2.5, you are notified that the output values for the connected output modules are kept in their respective state and (unlike with SIMATIC S7-300/S7-400) are neither reset nor set to the configured substitute values. In addition, the SIMATIC S7-1500 can no longer respond to input values from input modules in this state.  This information is displayed only once during each online session. |  |

### Rules for working with software units

The following rules are to be observed when working with software units:

**Synchronization of software units:**

- The relations and properties associated with the software units (e.g. name, author etc.) cannot be automatically synchronized when working with "Synchronize PLC".
- This can result in relations and properties already changed by an editor being overwritten when loading to a device and then reloading from a device with an older version.

> **Note**
>
> **Changes to properties and relations of software units**
>
> Changes to properties and relations of software units can only be carried out in the master project.

---

**See also**

[Basics of PLC synchronization](#basics-of-plc-synchronization)
  
[Requirements for PLC synchronization](#requirements-for-plc-synchronization)
  
[Procedure for PLC synchronization](#procedure-for-plc-synchronization)

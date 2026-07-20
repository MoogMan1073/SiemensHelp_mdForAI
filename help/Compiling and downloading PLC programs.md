---
title: "Compiling and downloading PLC programs"
package: ProgPLCCompLoadenUS
topics: 19
devices: [S7-1200, S7-1500, S7-1500T]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Compiling and downloading PLC programs

This section contains information on the following topics:

- [Basics for compiling and downloading PLC programs](#basics-for-compiling-and-downloading-plc-programs)
- [Compiling blocks](#compiling-blocks)
- [Downloading blocks for S7-1200/1500 (S7-1200, S7-1500)](#downloading-blocks-for-s7-12001500-s7-1200-s7-1500)
- [Downloading blocks for S7-300/400 (S7-300, S7-400)](Downloading%20blocks%20for%20S7-300-400%20%28S7-300%2C%20S7-400%29.md#downloading-blocks-for-s7-300400-s7-300-s7-400)
- [Downloading PLC tags (S7-1200, S7-1500)](#downloading-plc-tags-s7-1200-s7-1500)

## Basics for compiling and downloading PLC programs

### Compiling and downloading PLC programs

In order for the PLC program you have created to become executable in the automation system, you must first compile the program data that you have created offline and then download it to a device. You can load the program data to devices and memory cards.

> **Note**
>
> When we refer to downloading "blocks" in the following descriptions, we always mean downloading the entire PLC program:
>
> - Including PLC data types and PLC tags
> - Including the software units with their lower-level blocks

### Compiling the PLC program

Blocks are always compiled completely to keep the program consistent.

You can find additional information on compiling the PLC program here: [Basic information on compiling blocks](#basic-information-on-compiling-blocks)

### Downloading the PLC program

When the program is downloaded for the first time, the program data is loaded completely. During later download operations, only changes are downloaded.

To ensure the consistency of the program, all dependent blocks are also compiled and downloaded when downloading changed blocks. For example, when you download structural changes to a global data block, all code blocks that access that data block are compiled and downloaded again.

### Downloading PLC tags

As of TIA Portal V15, the PLC tags are also adopted during a "Download to device" and stored as configured offline.

### Downloading groups and group structures for S7-1200 and S7-1500 CPUs

As of TIA Portal V17, existing groups and group structures are included in a "Download to device" and stored as configured offline.

The groups and group structures can be downloaded from the following system folders:

- Program blocks
- PLC data types
- PLC tags (only CPU S7-1500 firmware version >= V2.5 and higher)

This also applies to the system folders listed above below Software units.

You can select each of these objects in the project tree and download it to a CPU S7-1200 or S7-1500 with the included groups and group structures.

Download is possible via all download commands that are available for downloading software.

> **Note**
>
> **Downloading objects with groups and group structures**
>
> When downloading individual objects that contain groups and group structures, all changes in the group structure are included in the download.
>
> If the object to be downloaded is included in a software unit, all changes in the group structure within the software unit are included in the download.
>
> If the object to be downloaded is located outside a software unit, all changes in the group structure outside the software unit are included in the download.

> **Note**
>
> **Changes in groups and group structures that are not relevant for the download**
>
> Changes which only have an impact on the group structure are not relevant for the download because they have no effect on how the program is being processed.
>
> Changes that are not relevant for the download are, for example:
>
> - Moving a block to a different group
> - Creating and renaming groups
>
> A changed group structure is only downloaded to the controller with the next change that is relevant for the download, for example, a change to a block.

### Uploading groups and group structures for S7-1200 and S7-1500 CPUs

With "Upload from device", the groups and group structures are also transferred from the online project to the new project.

### Other particularities of loading

- During the download operation, all information that is required for the reconstruction of the program, including symbolic information such as the names and comments for code and data blocks, is also downloaded in the up to three configured project languages. If you change the project language, you must therefore re-load the program.
- The symbolic information is not loaded to the work memory, but rather to the load memory.
- After the data has been loaded from a device, the symbolic information is available again in your program, which increases the readability of your program code. Please note, however, that loading to and from a device is not a substitute for storing data in an offline project, as watch tables or multi-language capability of projects cannot be reproduced by loading to and from a device.
- After loading from a device, you can only display all data from know-how-protected blocks by entering the correct password.
- Test and commissioning functions may be affected by loading, e.g. if names or addresses of variables change. A message is therefore displayed in the "Load preview" dialog if test and commissioning functions are configured on the device. These can also be trace or force jobs that exist on the device but are not active.
- You can find additional information on downloading the PLC program here:

  [Introduction to downloading blocks](#introduction-to-downloading-blocks-s7-1200-s7-1500) (S7-1200/1500)

  [Introduction to loading of blocks](Downloading%20blocks%20for%20S7-300-400%20%28S7-300%2C%20S7-400%29.md#introduction-to-loading-of-blocks-s7-300-s7-400) (S7-300/400)

  [Introduction to downloading PLC tags](#introduction-to-downloading-plc-tags-s7-1200-s7-1500) (S7-1200/1500)

---

**See also**

[Basic information on compiling blocks](#basic-information-on-compiling-blocks)
  
[Introduction to loading of blocks (S7-300, S7-400)](Downloading%20blocks%20for%20S7-300-400%20%28S7-300%2C%20S7-400%29.md#introduction-to-loading-of-blocks-s7-300-s7-400)
  
[Introduction to downloading blocks (S7-1200, S7-1500)](#introduction-to-downloading-blocks-s7-1200-s7-1500)
  
[Introduction to downloading PLC tags (S7-1200, S7-1500)](#introduction-to-downloading-plc-tags-s7-1200-s7-1500)
  
[Compiling and downloading software units (S7-1500)](Using%20software%20units%20%28S7-1500%29.md#compiling-and-downloading-software-units-s7-1500)

## Compiling blocks

This section contains information on the following topics:

- [Basic information on compiling blocks](#basic-information-on-compiling-blocks)
- [Compiling blocks in the project tree](#compiling-blocks-in-the-project-tree)
- [Compiling blocks in the program editor](#compiling-blocks-in-the-program-editor)
- [Correcting compilation errors](#correcting-compilation-errors)

### Basic information on compiling blocks

#### Introduction

A user program must first be compiled before the CPU can execute it. You need to recompile your program each time you make a change.

The following procedures take place during compilation:

- The user program is checked for syntax errors.
- Unneeded instructions are removed from the user program.
- All the block calls within the compiled blocks are checked. In case of changes to the interface of called blocks, errors will be shown in the "Compilation" tab of the information window. You have to correct these errors first.
- The blocks must be numbered uniquely in the user program. If more than one block has the same number, the blocks with number conflicts are renumbered automatically during compilation. A block will not be renumbered in the following cases:

  - The block was selected either individually or as part of a multiselection for the compilation.
  - The number assignment is set to "manual" in the properties of the block.

  Number conflicts that cannot be resolved by automatic renumbering must be corrected manually. Note the messages in the Inspector window for this.

  > **Note**
  >
  > **Renumbering know-how-protected blocks**
  >
  > Automatic renumbering and manual renumbering without password of know-how-protected blocks is only possible for CPU of the series S7-1500 and S7-1200 (V4). The know-how protection must also be set with a TIA Portal version V13 SP1 or higher.
- Finally, the user program is compiled into a code that can be read by the CPU.

#### Compilation methods

You can start compilation in the following windows or editors:

- Compiling blocks in the project tree

  Serves to compile individual blocks or the simultaneous compilation of one or several blocks in the "Program blocks" folder.
- Compiling blocks in the program editor

  This is intended for compilation of a single open block.
- Compiling blocks in the call or dependency structure

  Used to compile individual blocks.

  See also: [Call structure](Displaying%20program%20information.md#displaying-the-call-structure), [Dependency structure](Displaying%20program%20information.md#displaying-the-dependency-structure)

#### Compilation options

If you are compiling blocks in project tree, you have further options:

- Software (only changes)

  All program changes of the selected blocks are compiled. If you have selected a block folder, all program changes to the bocks contained in the folder are compiled.
- Software (compile all blocks)

  All blocks are compiled. This is recommended for the first compilation and after major revisions.
- Software (reset memory reserve)

  All tags declared in the reserve area of the interface of selected blocks are moved to the standard area of the interface. Memory reserve is now available for further interface extensions.

  > **Note**
  >
  > This option is only available for CPUs of the S7-1500 and S7-1200 V4 and higher series.

#### Consistency check

Changing the interfaces of blocks called or PLC data types used can result in inconsistencies between calling blocks and called blocks or between the PLC data types and the global data blocks which use these PLC data types.

To avoid such inconsistencies in the user program, the system performs an automatic consistency check before each compilation process. The time stamps are compared and compilation is then either carried out or canceled depending on the results of the comparison.

- The calling block can only be compiled if the time stamps of the interfaces of the called blocks are older than those of the calling block.
- A global data block based on a PLC data type can only be compiled correctly if the time stamp of the global data block is newer than the time stamp of the PLC data type used.
- The instance data block can only be compiled correctly if the interface time stamps for the interface of the instance data block are identical to those of the assigned function block.

If the compilation process is cancelled, an alarm is displayed in the inspector window. Update the block calls in the relevant blocks and the PLC data types in the global data blocks and then restart compilation. The consistency check also finds know-how protected blocks which cannot be compiled. The corresponding messages will also be shown in the inspector window.

If you start loading immediately instead of first compiling, the blocks selected will be automatically compiled and the block call and global data blocks implicitly updated. Please note the following differences between the CPU families:

- S7-1200/1500: All blocks affected are loaded to ensure no inconsistencies can arise.
- S7-300/400: Only the block selected is loaded.

---

**See also**

[Compiling blocks in the project tree](#compiling-blocks-in-the-project-tree)
  
[Compiling blocks in the program editor](#compiling-blocks-in-the-program-editor)
  
[Correcting compilation errors](#correcting-compilation-errors)
  
[Block time stamps](Creating%20and%20managing%20blocks.md#block-time-stamps)
  
[Updating block calls in LAD](Creating%20LAD%20programs.md#updating-block-calls-in-lad)
  
[Updating block calls in FBD](Creating%20FBD%20programs.md#updating-block-calls-in-fbd)
  
[Updating block calls in STL (S7-300, S7-400, S7-1500)](Creating%20STL%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#updating-block-calls-in-stl-s7-300-s7-400-s7-1500)
  
[Compiling project data](Editing%20project%20data.md#compiling-project-data)

### Compiling blocks in the project tree

You can compile one block, multiple blocks or all of the blocks in the project tree.

For CPUs of the S7-1500 and S7-1200 V4 series, you can also reset the memory layout of blocks with memory reserve by running a compilation. For more information on memory reserve, refer to chapter "Loading blocks (S7-1200/1500) > Loading block changes without reinitialization".

#### Requirement

The project tree is open.

#### Compiling one or more blocks in the project tree

To compile multiple blocks in the project tree, follow these steps:

1. Open the "Program blocks" folder in project tree.
2. Select the blocks you want to compile.
3. Select the "Compile > Software (only changes)" command from the shortcut menu.

#### Compiling all blocks in the project tree

To compile all blocks in the "Program blocks" folder in project tree, follow these steps:

1. Select the "Program blocks" folder in the project tree.
2. You can select one of two different options for the compilation:

   - If you want to compile only the changes since the last compilation, select the "Compile > Software (only changes)" command in the shortcut menu.
   - If you want to compile all blocks completely, select the "Compile > Software (compile all blocks)" command in the shortcut menu.

#### Resetting memory layout (S7-1500/S7-1200 V4)

Proceed as follows to reset the memory layout of blocks:

1. Select the "Program blocks" folder, or specific blocks in this folder.
2. Select the "Compile > Software (Reset memory reserve)" command from the shortcut menu.

#### Result

The code for the blocks will be generated if the consistency check has been successful. Instance data blocks generated by the system which are no longer needed will be deleted.

The message under "Info > Compilation" in the inspector window reports whether the compilation was successful.

---

**See also**

[Basic information on compiling blocks](#basic-information-on-compiling-blocks)
  
[Compiling blocks in the program editor](#compiling-blocks-in-the-program-editor)
  
[Correcting compilation errors](#correcting-compilation-errors)
  
[Finding syntax errors in the program](Program%20editor.md#finding-syntax-errors-in-the-program)

### Compiling blocks in the program editor

> **Note**
>
> Note that the block is recompiled even if you have not made any changes and the time stamp of the block is modified.

#### Requirement

The block to be compiled is open.

#### Procedure

To compile a block in the program editor, follow these steps:

1. Right-click in the instruction window of the programming editor.
2. Select the "Compile" command in the shortcut menu.

#### Result

The code for the block is generated. Instance data blocks generated by the system which are no longer needed will be deleted.

The message under "Info > Compilation" in the inspector window reports whether the compilation was successful.

---

**See also**

[Basic information on compiling blocks](#basic-information-on-compiling-blocks)
  
[Compiling blocks in the project tree](#compiling-blocks-in-the-project-tree)
  
[Correcting compilation errors](#correcting-compilation-errors)

### Correcting compilation errors

In the Inspector window in "Info > Compile", you can see whether any compilation was successful or whether errors were detected in the program. If errors occur, you will need to correct them and then start the compilation again.

#### Procedure

To correct errors following compilation, follow these steps:

1. Open the error list in the Inspector window with "Info > Compile".
2. If there is one, click on the blue question mark next to the error text for information on remedying errors.
3. Double-click the error you want to correct.

   The corresponding error is highlighted.
4. Correct the error.
5. Restart compilation.

---

**See also**

[Basic information on compiling blocks](#basic-information-on-compiling-blocks)
  
[Compiling blocks in the program editor](#compiling-blocks-in-the-program-editor)
  
[Compiling blocks in the project tree](#compiling-blocks-in-the-project-tree)

## Downloading blocks for S7-1200/1500 (S7-1200, S7-1500)

This section contains information on the following topics:

- [Introduction to downloading blocks (S7-1200, S7-1500)](#introduction-to-downloading-blocks-s7-1200-s7-1500)
- [Downloading blocks in the "RUN" operating mode to the device (S7-1200, S7-1500)](#downloading-blocks-in-the-run-operating-mode-to-the-device-s7-1200-s7-1500)
- [Downloading blocks from program editor to device (S7-1200, S7-1500)](#downloading-blocks-from-program-editor-to-device-s7-1200-s7-1500)
- [Downloading blocks from the project tree to the device (S7-1200, S7-1500)](#downloading-blocks-from-the-project-tree-to-the-device-s7-1200-s7-1500)
- [Uploading blocks from device (S7-1200, S7-1500)](#uploading-blocks-from-device-s7-1200-s7-1500)
- [Downloading blocks to a memory card (S7-1200, S7-1500)](#downloading-blocks-to-a-memory-card-s7-1200-s7-1500)
- [Uploading blocks from a memory card (S7-1200, S7-1500)](#uploading-blocks-from-a-memory-card-s7-1200-s7-1500)
- [Switching off the sequencer prior to loading a GRAPH DB (S7-1500)](#switching-off-the-sequencer-prior-to-loading-a-graph-db-s7-1500)
- [Loading block extensions without reinitialization (S7-1200, S7-1500)](Loading%20block%20extensions%20without%20reinitialization%20%28S7-1200%2C%20S7-1500%29.md#loading-block-extensions-without-reinitialization-s7-1200-s7-1500)

### Introduction to downloading blocks (S7-1200, S7-1500)

#### Downloading blocks to device

So that the CPU can execute the user program, the program data must first be compiled and then downloaded to the device.

You can load the program data to devices and memory cards.

**There are different ways to download from and upload to the device:**

- By using the commands in the "Online" menu
- By using the shortcut menu
- By using the "Load" button in the toolbar

**Loading can be started in the project tree from the following selectable objects:**

- Devices
- "Program blocks" folder
- Individual blocks
- "PLC data types" folder
- "PLC tags" folder
- "Software units" folder
- Individual software units

**Depending on the selected object and the command selected, you can load the following components:**

- Downloading to device

  Both the hardware configuration and the software are downloaded to the destination if differences exist between the online and offline versions.
- Extended download to device

  Both the hardware configuration and software are downloaded to the destination if differences exist between the online and offline versions. With extended loading, you can also select a target device and the settings for a target device.
- Load PLC program to device and reset

  The PLC program including all blocks, PLC data types and PLC tags is downloaded to the target and all values are reset to their initial values. Be aware that this also applies to retentive values. The CPU goes to "STOP".
- Download user program to memory card

  The entire program is downloaded onto a plugged-in memory card.

**Depending on the selected object and the command selected, you can download the following components from the shortcut menu:**

- Hardware and software (only changes)

  Both the hardware configuration and software are downloaded to the destination if differences exist between the online and offline versions.
- Hardware configuration

  Only the hardware configuration is downloaded to the destination.
- Software (only changes)

  Only the objects that differ online and offline are downloaded to the destination.
- Software (all)

  The software is downloaded completely to the destination.

> **Note**
>
> **Downloading groups and group structures**
>
> As of V17 of the TIA Portal, existing groups and group structures are included in a "Download to device" and stored as configured offline.

> **Note**
>
> **No valid hardware configuration available**
>
> If no valid hardware configuration was found on the CPU while loading the software, the existing hardware is loaded as well during a "Download to device".
>
> Note that, in this case, hardware components are also loaded during the download, even though you executed the command for loading software.

> **Note**
>
> To avoid inconsistencies between calling and called blocks, all blocks affected are compiled and loaded after each global change, such as a change in the block interface.

> **Note**
>
> **S7-1500**
>
> The load memory of S7-1500 series CPUs is on the SIMATIC memory card. Therefore, a SIMATIC memory card absolutely must be inserted in order to operate the CPU.

#### Uploading blocks from device

You can load the blocks from a device into your project. This is necessary, for example, if you want to edit blocks that only exist in this device. You have the option of loading either all available blocks (organization blocks, function blocks, functions and data blocks) and global PLC tags or individual blocks to the project.

As of TIA Portal V17, groups and group structures existing online are also transferred to the new project during an upload.

#### Uploading blocks from or downloading blocks to a memory card

Memory cards are plug-in cards used with an S7-1200 series CPU, for example, to replace the load memory of a device. In the case of S7-1500 series CPUs, they contain the load memory. Only the SIMATIC memory card from Siemens can be used for devices of the S7-1200 and S7-1500 series.

To use a memory card as load memory, you must download the user program or individual blocks to a memory card. You can just as well upload blocks from a memory card back into the project.

> **Note**
>
> **S7-1200**
>
> Note the following when uploading to or downloading from a memory card:
>
> - If the CPU contains no previous program and you insert an empty memory card in the CPU the program will be loaded from the PG/PC to the memory card and not to the CPU.
> - If you insert an empty memory card prior to the startup of the CPU, the program that is on the CPU will be transferred automatically to the memory card. The program on the CPU will then be deleted.
> - If you insert a memory card with a program in the CPU prior to the startup of the CPU and the CPU already contains a program, the program on the memory card will be executed and not the program on the CPU. The program on the CPU will be deleted.

#### Loading GRAPH function blocks

If you load a GRAPH function block together with its instance data block, the processing of the sequencer starts over at the initial step. As a result, problems may occur when synchronizing the sequencer with the process. You can avoid these problems by switching off the sequencer before loading.

#### Downloading changes without reinitialization

It often proves necessary to edit or expand a PLC program that was already commissioned and that is running on the plant without error. Such operations should be performed without causing any major interruptions of current operations.

S7-1500 therefore offers the option of extending the interfaces of function or data blocks during runtime and loading the modified blocks without setting the CPU to STOP or affecting the value of tags that are already loaded. This is a simple means of implementing program changes. This load process (download without reinitialization) will not have a negative impact on the controlled process.

#### Effects of a load operation on the tag values of a data blocks

When data blocks are downloaded to a device in STOP mode, the next transition of the device to RUN affects the current tag values as follows:

- Tags not marked as being retentive retain their defined start values.
- Retentive tags of the S7-1200 only retain their values if the following conditions are met:

  - You loaded the data block by means of "Download to device > Software (changes only)".
  - You made no changes to the DB structure.

  Otherwise the retentive tags will also retain their defined start values.
- Retentive tags of the S7-1500 only retain their values if the following conditions are met:

  - You loaded the data block by means of "Download to device > Software (changes only)".
  - You made no changes to the structure of the data block or modified it within the memory reserve.

  Otherwise the retentive tags will also retain their defined start values.

#### Loading blocks with synchronization

In team engineering, it is possible for several users to work on one project with several engineering systems at the same time and access one S7-1500 CPU. To ensure consistency within the shared project, it is necessary to synchronize the changed data prior to loading so that nothing gets overwritten unintentionally.

If differences are determined between the online and offline data management within the shared project during loading that were caused by a different engineering system, automatic synchronization of the data to be loaded is offered during loading.

In this case, the "Synchronization" dialog displays the data to be synchronized with the current status (online-offline comparison) and the possible actions.

The following options are available for synchronization:

| Application case | Recommendation | Synchronization |
| --- | --- | --- |
| One or more blocks on the CPU (online) are more recent than in the engineering system (offline). | These blocks should be downloaded from the CPU to the engineering system before loading. | Automatic synchronization is possible:  The blocks in the engineering system are updated prior to loading. |
| One or more new blocks have been created and exist only in the CPU (online). | These blocks should be downloaded from the CPU to the engineering system before loading. | Automatic synchronization is possible:  The new blocks are added to the engineering system prior to the download. |
| One or more blocks on the CPU have been deleted. | The blocks should also be deleted prior to the download in the engineering system. | Automatic synchronization is not possible.  The blocks deleted on the CPU should be manually deleted in the offline project in the engineering system. |
| One or more blocks on the CPU and in the engineering system are different.  This is the case when a different user has changed blocks to which you have also made corrections and has already downloaded them to the CPU. | These blocks with competing changes must be adapted manually. You decide in this case which changes you are going to accept.  If the blocks on the CPU are to be retained, you should accept these blocks prior to download from the CPU to your engineering system.  If the blocks that you have changed are to be applied, you can continue with the download without synchronization. | Automatic synchronization is not possible:  The affected blocks on the CPU or in the engineering system must be adapted manually. One of the existing block versions (online or offline) will be overwritten in the process. |
| There are differences in the hardware configuration on the CPU (online) and in the engineering system (offline). | Differences in the hardware configuration must be adapted manually. You decide in this case which hardware configuration you are going to accept.  If the existing hardware configuration on the CPU is to be retained, you should apply these in your engineering system prior to loading.  If you want to apply the changed hardware configuration, you can continue with the download without synchronization. | Automatic synchronization is not possible:  The hardware configuration must be adapted manually.  One of the existing hardware configurations (online or offline) will be overwritten in the process. |

You can use the "Force download to device" command to download blocks without synchronization, if desired.

#### Loading I&M data in PROFINET IO devices to load your modules

When loaded in a device, you can load I&M data in PROFINET IO devices and their modules in addition to the above-mentioned components.

---

**See also**

[Downloading blocks in the "RUN" operating mode to the device (S7-1200, S7-1500)](#downloading-blocks-in-the-run-operating-mode-to-the-device-s7-1200-s7-1500)
  
[Downloading blocks from the project tree to the device (S7-1200, S7-1500)](#downloading-blocks-from-the-project-tree-to-the-device-s7-1200-s7-1500)
  
[Downloading blocks from program editor to device (S7-1200, S7-1500)](#downloading-blocks-from-program-editor-to-device-s7-1200-s7-1500)
  
[Uploading blocks from device (S7-1200, S7-1500)](#uploading-blocks-from-device-s7-1200-s7-1500)
  
[Downloading blocks to a memory card (S7-1200, S7-1500)](#downloading-blocks-to-a-memory-card-s7-1200-s7-1500)
  
[Uploading blocks from a memory card (S7-1200, S7-1500)](#uploading-blocks-from-a-memory-card-s7-1200-s7-1500)
  
[Loading I&M data to PROFINET IO devices and your modules](Device%20and%20network%20diagnostics.md#loading-im-data-to-profinet-io-devices-and-your-modules)

### Downloading blocks in the "RUN" operating mode to the device (S7-1200, S7-1500)

#### Basics on downloading blocks in the "RUN" operating mode

When you download modified objects, such as blocks, to the device, it is not always necessary to switch the device to the "STOP" operating mode. Prior to a download operation, the Engineering System checks whether the device must be stopped before downloading. The result of this check is displayed in the "Load preview" dialog.

If it is necessary to change to the "STOP" operating mode, you cannot continue the download process until you have stopped the CPU.

If the requirements are met, you can also download a modified program or program parts to a CPU in "RUN" operating mode.

The quantity structures may be exceeded for very complex programs which prevents a download in "RUN". In this case you must first create the prerequisites for a download in "RUN".

**Tips:**

- Use a memory card with sufficient capacity.
- Select a CPU with sufficient work memory.
- If necessary, reduce the number of objects to be loaded (blocks, constants, tags, data types).

  If you cannot download all objects at once, proceed in several steps and download a smaller number of objects in each step.

> **Note**
>
> Actual parameters are not overwritten by a download process in the "RUN" operating mode. Changes to the actual parameters are not made until the next operating state transition from "STOP" to "RUN".

#### Downloading changes in "RUN"

The table below shows which program and configuration changes can be downloaded in "RUN" operating mode, sorted by CPU family and taking into consideration the firmware versions of the CPUs.

Explanations on the table:

- "RUN": Change can be downloaded to the CPU not only in the STOP operating mode but also in the "RUN" operating mode.
- "RUN (< 57)": The CPU can integrate up to 56 new or modified objects/blocks in one program cycle. If you download more objects/blocks, they are integrated in several successive program cycles. If you want to download all objects/blocks consistently, you must set the CPU to "STOP" operating mode. This number depends on the setting for S7-300 CPUs with configuration option "Process mode/test mode".
- "RUN (Init)": Change can be downloaded in "RUN" operating mode; downloaded data blocks are re-initialized.
- "STOP": Change can only be downloaded in "STOP" operating mode.
- "STOP (Reset)": Change can only be downloaded in "STOP" operating mode; all data including retentive data is reset.

|  | S7-300 | S7-400 | S7-1200 V4.0 and higher | S7-1500 |
| --- | --- | --- | --- | --- |
| Action/type of change | Download possible in mode ... |  |  |  |
| Modified properties of HW components. This includes changes to comments in the HW configuration. | STOP | STOP | STOP | STOP |
| Added HW components | STOP | STOP | STOP | STOP |
|  |  |  |  |  |
| New/revised text lists (messages) | **RUN** | **RUN** | STOP | **RUN** **(V1.1 and higher)** |
| Revised comments (new, revised, deleted) with the exception of comments in the HW configuration | - | - | **RUN** | **RUN** |
| New/changed OPC/UA interface, new OPC/UA XML import | - | - | **RUN (as of V4.4)** | **RUN (as of V2.8)** |
|  |  |  |  |  |
| Number of blocks downloaded at the same time | **RUN (<17)** | **RUN (<57)** | **RUN (<21)** | **RUN (all)** |
| Download PLC program to the device and reset | STOP (Reset) | STOP (Reset) | STOP (Reset) | STOP (Reset) |
| New OB | **RUN** | **RUN** | STOP | **RUN** |
| Modified OB: Code changes | **RUN** | **RUN** | **RUN** | **RUN** |
| OB with modified properties   (e.g., cycle time change) | **RUN** | **RUN** | STOP | **RUN** |
| Deleted OB | **RUN** | **RUN** | STOP | **RUN** |
| New FB/FC/DB/User Data Type (UDT) | **RUN** | **RUN** | **RUN** | **RUN** |
| Deleted FB/FC/DB/User Data Type (UDT) | **RUN** | **RUN** | **RUN** | **RUN** |
| Revised FB/FC: Code change | **RUN** | **RUN** | **RUN** | **RUN** |
| Revised FB/FC: Interface change* | STOP | STOP | **RUN** | **RUN** |
| Modified DB: Modified property ("Only store in load memory" attribute changed) | STOP | STOP | **RUN (Init)** | **RUN (Init)** |
| Modified DB (memory reserve not enabled): Name/type of tags modified, tags added or deleted ** | **RUN (Init)** | **RUN (Init)** | **RUN (Init)** | **RUN (Init)** |
| Modified DB (memory reserve enabled): New tag added** | - | - | **RUN** | **RUN** |
|  |  |  |  |  |
| Modified User Data Type (UDT) | STOP | STOP | **RUN (Init)** | **RUN (Init)** |
| Add new PLC tags (timer, counter, bit memory) | **RUN** | **RUN** | **RUN** | **RUN** |
| Modified retentivity settings (timer, counter, bit memory, DB area) | STOP | STOP | STOP | STOP |
| Motion Control technology objects: Changes to MC Servo cycle clock, change from free-running to cyclical (and vice versa). Changes to the HW interface of the TO | - | - | - | STOP |
| * If the interface change results in structural changes at the instance DB, see "Modified DB...".  ** For the effect of download of data block changes to the data block content, see section "Downloading data blocks to the CPU" |  |  |  |  |

#### Download of changes in "RUN" with older CPU firmware versions

The table below shows which changes you can download in "RUN" operating mode, in particular, for which older CPU firmware versions.

|  | S7-1200  V1.0 - 2.1 | S7-1200  V2.2 - V3.0 |
| --- | --- | --- |
| Action/type of change | Download possible in mode ... |  |
| Modified properties of HW components.  This includes changes to comments in the HW configuration. | STOP | STOP |
| Added HW components | STOP | STOP |
|  |  |  |
| New/revised text lists (messages) | STOP | STOP |
| Revised comments (new, revised, deleted) with the exception of comments in the HW configuration | STOP | **RUN** |
|  |  |  |
| Number of blocks downloaded at the same time | STOP | **RUN (<11)** |
| Download PLC program to the device and reset | STOP (Reset) | STOP (Reset) |
| New OB | STOP | STOP |
| Modified OB: Code changes | STOP | **RUN** |
| OB with modified properties (e.g., cycle time change) | STOP | STOP |
| Deleted OB | STOP | STOP |
| New FB/FC/DB/User Data Type (UDT) | STOP | **RUN** |
| Deleted FB/FC/DB/User Data Type (UDT) | STOP | **RUN** |
| Revised FB/FC: Code change | STOP | **RUN** |
| Revised FB/FC: Interface change | STOP | STOP |
| Modified DB: Modified property ("Only store in load memory" attribute changed) | STOP | STOP |
| Modified DB (memory reserve not enabled): Name/type of tags modified, tags added or deleted | STOP | STOP |
|  |  |  |
| Modified User Data Type (UDT) | STOP | STOP |
| Add new PLC tags (timer, counter, bit memory) | STOP | STOP |
| Modified retentivity settings (timer, counter, bit memory, DB area) | STOP | STOP |

#### Downloading data blocks to the CPU

Depending on the conditions, the download of new or modified data blocks has an effect on the actual values in the data block:

| Symbol | Meaning |
| --- | --- |
| Download new data blocks | Actual values in the new data blocks are set to start values. |
| Download structurally modified data blocks (memory reserve not enabled) | Actual values of added tags in the structurally modified data blocks are set to start values. |
| Download structurally modified data blocks (memory reserve enabled) | The following actual values are retained:  - Actual values of tags outside the memory reserve - Actual values of tags that were not modified within the memory reserve   Actual values of added tags within the memory reserve are set to start values. |
| Download of simply modified data blocks (no structural modification) | Actual values are retained. |

#### Additional information

Additional information on download of block extensions without re-initialization and download of modified values for data blocks is available at "See also".

---

**See also**

[Downloading blocks from program editor to device (S7-1200, S7-1500)](#downloading-blocks-from-program-editor-to-device-s7-1200-s7-1500)
  
[Downloading blocks from the project tree to the device (S7-1200, S7-1500)](#downloading-blocks-from-the-project-tree-to-the-device-s7-1200-s7-1500)
  
[Downloading project data to a device](Editing%20project%20data.md#downloading-project-data-to-a-device)

### Downloading blocks from program editor to device (S7-1200, S7-1500)

#### Requirement

The block to be downloaded is open.

#### Procedure

To download a block from the program editor to the device, follow these steps:

1. Right-click in the instruction window of the programming editor.
2. Select the "Download to device" command in the shortcut menu.

   - If you have not already established an online connection, the "Extended download to device" dialog opens. In this case, set all parameters required for the connection and click "Load".
   - You can save your preferred connection parameters as default under "Options > Settings > Online & Diagnostics". When you first load with new connection parameters, a query is automatically displayed whether you want to store it as a default setting. Click "Yes", if you want to save the current connection parameters as default.
   - You have the option of showing all compatible devices by selecting the corresponding option and clicking the "Start search" command. You can also open the "Extended download to device" dialog explicitly via the "Online" menu.

     See also: [Establishing and terminating an online connection](Using%20online%20and%20diagnostics%20functions.md#establishing-or-changing-an-online-connection)
   - If you have already specified an online connection, then the project data is compiled if necessary and the "Load preview" dialog opens. This dialog displays alarms and proposes actions necessary for loading.
3. Check the alarms and, where necessary, enable the actions in the "Action" column.

   As soon as downloading becomes possible, the "Load" button is enabled.
4. Click "Load".

   If there is a need for synchronization, the system automatically displays the "Synchronization" dialog. This dialog displays messages and suggests actions that are needed for the synchronization. You have the option of performing these actions or forcing the download without synchronization by clicking "Force download to device". If you have performed the suggested actions, you will be asked whether you want to continue with the download. Click "Continue download" in order to download the block. The "Load results" dialog then opens and shows you the status and the actions after the download operation.
5. If you want to start the modules again directly after downloading, select the "Start module" check box.
6. To close the "Load results" dialog box, click "Finish".

**Note**

**Actions**

Performing the proposed actions during ongoing plant operation can cause serious damage to property or injury to persons if there are functional faults or program errors.

Make sure that no dangerous situations can arise before you start the actions.

**Note**

To avoid inconsistencies between calling and called blocks, download all affected blocks each time you make global changes, such as changes in the block interface. Select the "Consistent download" action.

#### Result

The code for the block will be downloaded to the device. If the changes affect additional blocks, these will be compiled and also downloaded to the device. Blocks that only exist online in the device are deleted. Existing CPU data blocks are retained, however. Inconsistencies between the blocks in the user program are avoided by loading all blocks affected and deleting the unneeded blocks in the device.

The messages under "Info > General" in the Inspector window show whether the downloading process was successful.

---

**See also**

[Downloading blocks from the project tree to the device (S7-1200, S7-1500)](#downloading-blocks-from-the-project-tree-to-the-device-s7-1200-s7-1500)
  
[Downloading project data to a device](Editing%20project%20data.md#downloading-project-data-to-a-device)
  
[Downloading blocks in the "RUN" operating mode to the device (S7-1200, S7-1500)](#downloading-blocks-in-the-run-operating-mode-to-the-device-s7-1200-s7-1500)

### Downloading blocks from the project tree to the device (S7-1200, S7-1500)

In the project tree you can download one block, multiple blocks or all blocks to a device.

#### Downloading one or more blocks from the project tree to the device

To download one block or multiple blocks to the device from the project tree, follow these steps:

1. Open the "Program blocks" folder in project tree.
2. Select the blocks you want to download.
3. Select the "Download to device > Software (only changes)" command from the shortcut menu.

   - If you have not already established an online connection, the "Extended download to device" dialog opens. In this case, set all parameters required for the connection and click "Load".
   - You can save your preferred connection parameters as default under "Options > Settings > Online & Diagnostics". You will be prompted as such when you download new connection parameters for the first time. Select "Yes", if you want to save the current connection parameters as default.
   - You have the option of showing all compatible devices by selecting the corresponding option and clicking the "Start search" command. You can also open the "Extended download to device" dialog explicitly via the "Online" menu.

     See also: [Establishing and terminating an online connection](Using%20online%20and%20diagnostics%20functions.md#establishing-or-changing-an-online-connection)
   - If you have already specified an online connection, then the project data is compiled if necessary and the "Load preview" dialog opens. This dialog displays alarms and proposes actions necessary for loading.
4. Check the alarms and, where necessary, enable the actions in the "Action" column.

   As soon as downloading becomes possible, the "Load" button is enabled.
5. Click "Load".

   If there is a need for synchronization, the system automatically displays the "Synchronization" dialog. This dialog displays messages and suggests actions that are needed for the synchronization. You have the option of performing these actions or forcing the download without synchronization by clicking "Force download to device". If you have performed the suggested actions, you will be asked whether you want to continue with the download. Click "Continue download" in order to download the block. The "Load results" dialog then opens and shows you the status and the actions after the download operation.
6. If you want to start the modules again directly after downloading, select the "Start all" check box.
7. To close the "Load results" dialog box, click "Finish".

**Note**

Performing the proposed actions during ongoing plant operation can cause serious damage to property or injury to persons if there are functional faults or program errors.

Make sure that no dangerous situations can arise before you start the actions.

#### Downloading blocks from the project tree to the device

To download all blocks in the "Program blocks" folder to the device from the project tree, follow these steps:

1. Select the "Program blocks" folder in the project tree.
2. Select the "Download to device" submenu in the shortcut menu.
3. If you only want to download the changes since the last download, select the "Software (only changes)" option. If all blocks are to be fully loaded and all values are to be reset to their start values, select "Download PLC program to the device and reset".

   - If you have not already established an online connection, the "Extended download to device" dialog opens. In this case, set all parameters required for the connection and click "Load". You have the option of showing all compatible devices by selecting the corresponding option and clicking the "Start search" command. You can also open the "Extended download to device" dialog explicitly via the "Online" menu.

     See also: [Establishing and terminating an online connection](Using%20online%20and%20diagnostics%20functions.md#establishing-or-changing-an-online-connection)
   - If you have already specified an online connection, then the project data is compiled if necessary and the "Load preview" dialog opens. This dialog displays alarms and proposes actions necessary for loading.
4. Check the alarms and, where necessary, enable the actions in the "Action" column.

   As soon as downloading becomes possible, the "Load" button is enabled.
5. Click "Load".

   If there is a need for synchronization, the system automatically displays the "Synchronization" dialog. This dialog displays messages and suggests actions that are needed for the synchronization. You have the option of performing these actions or forcing the download without synchronization by clicking "Force download to device". If you have performed the suggested actions, you will be asked whether you want to continue with the download. Click "Continue download" in order to download the block. The "Load results" dialog then opens and shows you the status and the actions after the download operation.
6. If you want to start the modules again directly after downloading, select the "Start module" check box.
7. To close the "Load results" dialog box, click "Finish".

**Note**

Performing the proposed actions during ongoing plant operation can cause serious damage to property or injury to persons if there are functional faults or program errors.

Make sure that no dangerous situations can arise before you start the actions.

#### Result

The code for the blocks is downloaded to the device. If the changes affect additional blocks, these will be compiled and also downloaded to the device. Blocks that only exist online in the device are deleted. Inconsistencies between the blocks in the user program are avoided by loading all blocks affected and deleting the unneeded blocks in the device.

The messages under "Info > General" in the Inspector window show whether the downloading process was successful.

---

**See also**

[Downloading blocks from program editor to device (S7-1200, S7-1500)](#downloading-blocks-from-program-editor-to-device-s7-1200-s7-1500)
  
[Downloading project data to a device](Editing%20project%20data.md#downloading-project-data-to-a-device)
  
[Downloading blocks in the "RUN" operating mode to the device (S7-1200, S7-1500)](#downloading-blocks-in-the-run-operating-mode-to-the-device-s7-1200-s7-1500)

### Uploading blocks from device (S7-1200, S7-1500)

You can load either all the blocks or only individual blocks from a device to your project.

> **Note**
>
> Please note the following:
>
> - Please note that when you load individual blocks, no tags or other required blocks to which you may refer are loaded together with the individual blocks. During the loading operation, references to tags and blocks are reassigned where possible based on the names. After the loading operation, check whether these assignments are correct.
> - When downloading from a device to your project or to a new station, groups and group structures existing online are also uploaded.
> - S7-1500: When GRAPH function blocks are loaded from a device to your project, the step-specific alarm texts for the interlock and supervision alarms are not loaded.
> - S7-1500: The start values that you have changed with the instruction "WRIT_DBL: Write to data block in the load memory" will be lost during execution of the action "Upload from device".

#### Requirement

The online and offline versions of the blocks to be loaded differ or the blocks only exist online.

#### Loading all blocks from a device

To load all blocks from a device, follow these steps:

1. Establish an online connection with the device from which you want to load the blocks.

   See also: [Establishing and terminating an online connection](Using%20online%20and%20diagnostics%20functions.md#establishing-or-changing-an-online-connection)
2. In the project tree, select the device folder from which you want to load blocks.
3. In the "Online" menu, select the "Upload from device" command.

   The "Upload preview" dialog box opens. This dialog displays alarms and proposes actions necessary for loading.
4. Check the alarms and, where necessary, enable the actions in the "Action" column.

   As soon as loading becomes possible, the "Upload from device" button is enabled.
5. Click the "Upload from device" button.

   The loading operation is performed.

#### Loading individual blocks from a device

To load individual blocks from a device, follow these steps:

1. Establish an online connection with the device from which you want to load the blocks.

   See also: [Establishing and terminating an online connection](Using%20online%20and%20diagnostics%20functions.md#establishing-or-changing-an-online-connection)
2. In the project tree, select the blocks that you want to load from the device.
3. In the "Online" menu, select the "Upload from device" command.

   The "Upload preview" dialog box opens. This dialog displays alarms and proposes actions necessary for loading.
4. Check the alarms and, where necessary, enable the actions in the "Action" column.

   As soon as loading becomes possible, the "Upload from device" button is enabled.
5. Click the "Upload from device" button.

   The loading operation is performed.

#### Result

The blocks will be loaded from the device to the project. You can edit them as normal, recompile them and load them to the device again.

### Downloading blocks to a memory card (S7-1200, S7-1500)

#### Requirement

- The memory card is marked as a program card.
- The "Program blocks" folder of the memory card is open.

#### Procedure

To download blocks to a memory card, follow these steps:

1. Open the "Program blocks" folder of the device in the project tree.
2. Select the blocks you want to download to the memory card.
3. Drag the blocks in project tree to the "Program blocks" folder of the memory card. You can also copy the blocks and add them to the memory card.

   If necessary, the blocks are compiled. The "Load preview" dialog then opens. This dialog displays alarms and proposes actions necessary for loading.
4. Check the alarms and, where necessary, enable the actions in the "Action" column.
5. As soon as downloading becomes possible, the "Load" button is enabled.
6. Click the "Load" button.

   If there is a need for synchronization, the system automatically displays the "Synchronization" dialog. This dialog displays messages and suggests actions that are needed for the synchronization. You have the option of performing these actions or forcing the download without synchronization by clicking "Force download to device". If you have performed the suggested actions, you will be asked whether you want to continue with the download. Click "Continue download" to download the block. The "Load results" dialog then opens and shows you the status and the actions after the download operation.
7. Click "Finish".

Or:

1. In the project tree, select the blocks that you want to upload.
2. Select the "Card reader/USB memory > Write to memory card" command in the "Project" menu.

   The "Select memory card" dialog opens.
3. Select a memory card which is compatible with the CPU.

   A button with a green check mark is activated at the bottom of the dialog.
4. Click the button with the green check mark.

   If necessary, the project data are compiled. The "Load preview" dialog then opens. This dialog displays alarms and proposes actions necessary for loading.
5. Check the alarms and, where necessary, enable the actions in the "Action" column.

   As soon as downloading becomes possible, the "Load" button is enabled.
6. Click the "Load" button.

   If there is a need for synchronization, the system automatically displays the "Synchronization" dialog. This dialog displays messages and suggests actions that are needed for the synchronization. You have the option of performing these actions or forcing the download without synchronization by clicking "Force download to device". If you have performed the suggested actions, you will be asked whether you want to continue with the download. Click "Continue download" to download the block. The "Load results" dialog then opens and shows you the status and the actions after the download operation.
7. Click "Finish".

#### Result

The blocks are downloaded to the memory card. If the changes affect additional blocks, these will also be downloaded to the memory card. Blocks that exist only on the memory card are deleted. Inconsistencies between the blocks in the user program are avoided by downloading all affected blocks and the deleting of the non-required blocks on the memory card.

The messages under "Info > General" in the Inspector window show whether the downloading process was successful.

---

**See also**

[Uploading blocks from a memory card (S7-1200, S7-1500)](#uploading-blocks-from-a-memory-card-s7-1200-s7-1500)
  
[Accessing memory cards](Editing%20project%20data.md#accessing-memory-cards)

### Uploading blocks from a memory card (S7-1200, S7-1500)

You can only upload all blocks from one memory card back into your project.

#### Requirement

The memory card is displayed.

See also: [Accessing memory cards](Editing%20project%20data.md#accessing-memory-cards)

#### Procedure

To upload blocks from a memory card to your project, follow these steps:

1. In the project tree, drag the folder of the memory card to the folder of the device in the project. You can also copy the memory card and insert it in the device.

   The "Upload preview" dialog box opens. This dialog displays alarms and proposes actions necessary for loading.
2. Check the alarms and, where necessary, enable the actions in the "Action" column.

   The "Upload from device" button will be enabled as soon as uploading becomes possible.
3. Click on the "Upload from device" button.

---

**See also**

[Downloading blocks to a memory card (S7-1200, S7-1500)](#downloading-blocks-to-a-memory-card-s7-1200-s7-1500)

### Switching off the sequencer prior to loading a GRAPH DB (S7-1500)

You can specify the switching off of the sequencer prior to loading an instance data block either globally or during the load operation.

#### Globally switching off the sequencer

To switch off the sequencer globally for each loading operation of an instance data block, follow these steps:

1. Select the "Settings" command in the "Options" menu.

   The "Settings" window is displayed in the work area.
2. Select the "PLC programming > GRAPH" group in the area navigation.
3. Select the "Turn off sequence before downloading DB" check box.

   For future loading operations, the sequencer is switched off prior to loading of the instance data block.

#### Switching off the sequencer during the loading operation

To switch off the sequencer during the loading operation, follow these steps:

1. Load the GRAPH function block to the device.

   During the loading operation, the "Load preview" dialog opens. This dialog displays alarms and suggests the required actions for loading. If the instance data block must be loaded together with the GRAPH function block, the "Load preview" dialog suggests the action "Turn off sequence before downloading the DB".
2. Select the "Turn off sequence before downloading DB" check box.

## Downloading PLC tags (S7-1200, S7-1500)

This section contains information on the following topics:

- [Introduction to downloading PLC tags (S7-1200, S7-1500)](#introduction-to-downloading-plc-tags-s7-1200-s7-1500)
- [Online/offline visibility of PLC tags (S7-1200, S7-1500)](#onlineoffline-visibility-of-plc-tags-s7-1200-s7-1500)

### Introduction to downloading PLC tags (S7-1200, S7-1500)

#### Introduction

PLC tags, as well as blocks, can be downloaded to a device and uploaded back to a project from a device. If you select a PLC tag table in the project navigation, the "Download to device > Software (only changes)" command becomes available.

You can use the command from the "Online" menu or from the shortcut menu or the "Load" button in the toolbar.

When you start the download to device from another object, for example from the block folder, the tag tables are always loaded consistently.

This functionality is supported by the following devices:

- CPU S7-1200
- CPU S7-1500

In the case of an S7-1500 as of firmware V2.5, the information to which PLC tag table the tags belong is downloaded to the CPU along with the PLC tags.

The command is not available for devices that do not support this functionality.

#### Rules for downloading to a device from PLC tag tables (S7-1500 as of V2.5 only)

Offline tag tables can be downloaded to the CPU in the specified structure.

The following rules apply:

- Downloading PLC tags is subject to the same requirements and procedures as downloading blocks.
- If inconsistencies are detected during loading of PLC tags, the synchronization dialog is displayed. To ensure consistency within a shared project, it is necessary to synchronize the changed data prior to loading so that nothing gets unintentionally overwritten. In this case, the data to be synchronized is displayed with the current status (offline/online comparison) and the actions that are possible. The comparison editor allows you to see which tags have changed in which tag table. The tags are always compared by name. In the event of a conflict, the user must decide which tags he would like to keep and load.

See also:

- [Comparing PLC tags](Comparing%20PLC%20programs.md#comparing-plc-tags-1)
- [Downloading blocks from the project tree to the device](#downloading-blocks-from-the-project-tree-to-the-device-s7-1200-s7-1500)
- [Downloading blocks to a memory card](#downloading-blocks-to-a-memory-card-s7-1200-s7-1500)

#### Rules for uploading from a device for PLC tag tables (S7-1500 as of V2.5 only)

Tag tables that are available online can be uploaded to the project in the specified structure.

The following rules apply:

- Uploading PLC tags is subject to the same requirements and procedures as uploading blocks.
- For PLC tags, the following special considerations apply to uploading from devices:

  - Tags that exist online and offline with the same name are overwritten offline.
  - Tags that are only available offline remain unchanged.
  - Tags that are only available online are created offline again.
  - Tags that exist online in another tag table are inserted in the uploaded tag table and are deleted from the other tag table.

See also:

- [Uploading blocks from device](#uploading-blocks-from-device-s7-1200-s7-1500)
- [Uploading blocks from a memory card](#uploading-blocks-from-a-memory-card-s7-1200-s7-1500)

#### Example for uploading from a device for PLC tag tables (S7-1500 as of V2.5 only)

The following example illustrates the system characteristics when uploading tag tables which differ online/offline:

- "Tag_A" tag is only available offline in tag table 1.
- "Tag_A" tag is only available online in tag table 2.

Result when uploading from tag table 1:

- "Tag_A" is only present offline in tag table 1 and therefore remains unchanged in tag table 1 after uploading.

Result when uploading from tag table 2:

- "Tag_A" is only available online in tag table 2 and is therefore added to tag table 2 after the upload; it is deleted in tag table 1.

---

**See also**

[Comparing PLC tags](Comparing%20PLC%20programs.md#comparing-plc-tags-1)
  
[Downloading blocks from the project tree to the device (S7-1200, S7-1500)](#downloading-blocks-from-the-project-tree-to-the-device-s7-1200-s7-1500)
  
[Uploading blocks from device (S7-1200, S7-1500)](#uploading-blocks-from-device-s7-1200-s7-1500)
  
[Uploading blocks from a memory card (S7-1200, S7-1500)](#uploading-blocks-from-a-memory-card-s7-1200-s7-1500)
  
[Downloading blocks to a memory card (S7-1200, S7-1500)](#downloading-blocks-to-a-memory-card-s7-1200-s7-1500)
  
[Online/offline visibility of PLC tags (S7-1200, S7-1500)](#onlineoffline-visibility-of-plc-tags-s7-1200-s7-1500)

### Online/offline visibility of PLC tags (S7-1200, S7-1500)

#### Introduction

PLC tag tables, as well as blocks, can be downloaded to a device and uploaded back to a project from a device.

Depending on whether tag tables are only available offline or online, they are displayed differently in the TIA Portal.

#### Visibility of PLC tag tables (S7-1500 as of V2.5 only)

PLC tag tables are displayed in the TIA Portal as follows:

| Display of PLC tag tables | Visibility | Possible actions |
| --- | --- | --- |
| Offline view in the   project tree | Offline data is permanently displayed, if available.   After uploading from the device, the online data is also visible offline. However, there may still be differences because only tags that are available offline are retained after the upload from device. | It is possible to open and edit in the editor.  It is possible to download and upload to and from the device as well as to and from memory cards. |
| Online view in the  project tree | Online data is displayed in online mode.   Online data is also displayed offline if there is no corresponding offline tag table. | The editor is opened in read-only mode, editing is not possible.  However, you can determine which tags are available. |
| For accessible devices | After downloading to device. | The editor is opened in read-only mode, editing is not possible.  However, you can determine which tags are available. |
| On local memory cards | After downloading to the memory card. | The editor is opened in read-only mode, editing is not possible.  However, you can determine which tags are available. |
| In the comparison editor | If there is one or more tag tables offline and/or online, comparative operations can be performed. | You can open the comparison editor and the comparison results for the selected tags are displayed by name. |

You can find additional information about how you can use the comparison editor for comparing PLC tags here: [Comparing PLC tags](Comparing%20PLC%20programs.md#comparing-plc-tags-1)

---

**See also**

[Comparing PLC tags](Comparing%20PLC%20programs.md#comparing-plc-tags-1)
  
[Introduction to downloading PLC tags (S7-1200, S7-1500)](#introduction-to-downloading-plc-tags-s7-1200-s7-1500)

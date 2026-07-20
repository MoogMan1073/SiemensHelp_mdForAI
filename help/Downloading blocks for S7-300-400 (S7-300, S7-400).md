---
title: "Downloading blocks for S7-300/400 (S7-300, S7-400)"
package: ProgLoad34enUS
topics: 9
devices: [S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Downloading blocks for S7-300/400 (S7-300, S7-400)

This section contains information on the following topics:

- [Introduction to loading of blocks (S7-300, S7-400)](#introduction-to-loading-of-blocks-s7-300-s7-400)
- [Downloading blocks in the "RUN" operating state to the device (S7-300, S7-400)](#downloading-blocks-in-the-run-operating-state-to-the-device-s7-300-s7-400)
- [Downloading blocks in the program editor to device (S7-300, S7-400)](#downloading-blocks-in-the-program-editor-to-device-s7-300-s7-400)
- [Downloading blocks from the project tree to the device (S7-300, S7-400)](#downloading-blocks-from-the-project-tree-to-the-device-s7-300-s7-400)
- [Uploading blocks from device (S7-300, S7-400)](#uploading-blocks-from-device-s7-300-s7-400)
- [Downloading blocks to a memory card (S7-300, S7-400)](#downloading-blocks-to-a-memory-card-s7-300-s7-400)
- [Uploading blocks from a memory card (S7-300, S7-400)](#uploading-blocks-from-a-memory-card-s7-300-s7-400)
- [Switching off the sequencer prior to loading a GRAPH DB (S7-300, S7-400)](#switching-off-the-sequencer-prior-to-loading-a-graph-db-s7-300-s7-400)

## Introduction to loading of blocks (S7-300, S7-400)

### Downloading blocks to device

So that the CPU can execute the user program, the program data must first be compiled and then downloaded to the device.

You can load the program data to devices and memory cards.

**There are different ways to download from and upload to the device:**

- By using the commands in the "Online" menu
- By using the shortcut menu
- By using the "Load" button in the toolbar

**Loading can be started in the project tree from the following objects:**

- From devices
- From the "Program blocks" folder
- From individual blocks
- From the "PLC data types" folder

**Depending on the selected object and the command selected, you can load the following components:**

- Downloading to device

  Both the hardware configuration and the software are downloaded to the destination if differences exist between the online and offline versions.
- Extended download to device

  Both the hardware configuration and software are downloaded to the destination if differences exist between the online and offline versions. With extended loading, you can also select a target device and the settings for a target device.
- Load PLC program to device and reset

  The PLC program including all blocks and PLC data types is downloaded to the target and all values are reset to their initial values. Be aware that this also applies to retentive values. The CPU goes to "STOP".
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
> **No valid hardware configuration available**
>
> If no valid hardware configuration was found on the CPU while loading the software, the existing hardware is loaded as well during a "Download to device".
>
> Note that, in this case, hardware components are also loaded during the download, even though you executed the command for loading software.

> **Note**
>
> **Downloading more than 16 blocks in RUN mode**
>
> If more blocks are to be downloaded in RUN than permitted by the CPU capacity for a download process, the blocks to be downloaded can be downloaded asynchronously over multiple cycles. When this error occurs, you can select this option in the "Load preview" dialog from the drop-down list.
>
> Keep in mind that a consistent state of the CPU is not reached again until the download over multiple cycles is complete.

> **Note**
>
> **Downloading know-how-protected blocks**
>
> If you download a know-how-protected block to a device, no restore information is installed along with it. This means that you cannot reopen a know-how-protected block if you upload it from the device.

> **Note**
>
> **Loading CPU S7-300/400**
>
> When loading from a device, please note that alarm information may be lost and that this could lead to errors during compilation.

### Loading PLC programs from device

You can download the program data loaded on a device back to your project.

This includes the existing blocks and PLC data types.

This is necessary, for example, if you want to edit blocks that only exist in this device. You can either upload all existing blocks (organization blocks, function blocks, functions, data blocks) and PLC data types or just individual blocks to the project.

> **Note**
>
> **Loading CPU S7-300/400**
>
> When downloading from a device, please note that alarm information may be lost and that this could lead to errors during compilation.

### Uploading blocks from or downloading blocks to a memory card

Memory cards are insertable cards used, for example, to expand the memory of a CPU and to protect data against power failures. You can use different types of memory cards depending on the CPU. For additional information on memory cards approved for your CPU, see "Additional information on configurations" in the section "Functional description of S7-300/400 CPUs".

### Loading GRAPH function blocks

If you load a GRAPH function block together with its instance data block, the processing of the sequencer starts over at the initial step. As a result, problems may occur when synchronizing the sequencer with the process. You can avoid these problems by switching off the sequencer before loading.

### Effects of a load operation on the tag values of a data blocks

When data blocks are downloaded to a device in STOP mode, the next transition of the device to RUN affects the current tag values as follows:

- Tags of non-retentive data blocks retain their defined start values.
- Tags of retentive data blocks only retain their values if the following conditions are met:

  - You loaded the data block by means of "Download to device > Software (changes only)".
  - You made no changes to the DB structure.

  Otherwise the tags of retentive data blocks also retain their defined start values.

### Loading I&M data in PROFINET IO devices to load your modules

When loaded in a device, you can load I&M data in PROFINET IO devices and their modules in addition to the above-mentioned components.

---

**See also**

[Loading I&M data to PROFINET IO devices and your modules](Device%20and%20network%20diagnostics.md#loading-im-data-to-profinet-io-devices-and-your-modules)

## Downloading blocks in the "RUN" operating state to the device (S7-300, S7-400)

### Basics about loading blocks in RUN mode

When you load modified blocks to a device, it is not always necessary to set the device to STOP mode. During the loading process, the engineering system checks whether the device has to be stopped before the loading. The result of the check is displayed in the "Load preview" dialog.

If it is necessary to change to STOP mode, you cannot continue the loading process until you have stopped the CPU.

If the requirements are met, you can also load a modified program or program parts in a CPU in RUN mode.

**Basically, there are the following restriction when loading in RUN mode:**

- Depending on the device used, the number and the type of blocks that you can load in RUN mode can be limited.
- You have the option to download the blocks to the device in RUN over multiple cycles. This is only possible when you use the "Download > Software (only changes)" command.
- It is not possible to load all the blocks using "Download PLC program to the device and reset".
- If you have changed the hardware configuration of the device that is to be used as the target of the loading process, loading in RUN mode is not possible.

> **Note**
>
> Actual parameters are not overwritten by a loading process in RUN mode. Modifications to the actual parameters only take place at the next change of operating mode from STOP to RUN.

### Loading changes in RUN mode

The following table shows which program or configuration changes can be loaded in RUN mode, sorted according to CPU series, and taking into account the firmware versions of the CPUs.

Explanations on the table:

- RUN: Change can be loaded in the CPU in STOP mode as well as in RUN mode.
- RUN (< 57): The CPU can integrate up to 56 new or modified objects/blocks in one program cycle. If you download more objects/blocks, they are integrated in several successive program cycles. If you want to load all objects/blocks consistently, you must set the CPU to STOP mode. This number depends on the setting for S7-300 CPUs with configuration option "Process mode/test mode".
- RUN (init): Change can loaded in RUN mode; loaded data blocks are re-initialized.
- STOP: Change can only be loaded in the STOP mode.
- STOP (reset): Change can only be loaded in STOP mode. All data including retentive data is reset.

|  | S7-300 | S7-400 | S7-1200 V4.0 and higher | S7-1500 |
| --- | --- | --- | --- | --- |
| Action/type of change | Download possible in operating state ... |  |  |  |
| Modified properties of HW components. This includes changes to comments in the HW configuration. | STOP | STOP | STOP | STOP |
| Added HW components | STOP | STOP | STOP | STOP |
|  |  |  |  |  |
| New/revised text lists (alarms) | **RUN** | **RUN** | STOP | **RUN** **(V1.1 and higher)** |
| Revised comments (new, revised, deleted) with the exception of comments in the HW configuration | - | - | **RUN** | **RUN** |
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
| Modified DB (memory reserve enabled): New tags added** | - | - | **RUN** | **RUN** |
|  |  |  |  |  |
| Modified User Data Type (UDT) | STOP | STOP | **RUN (Init)** | **RUN (Init)** |
| Add new PLC tags (timer, counter, bit memory) | **RUN** | **RUN** | **RUN** | **RUN** |
| Modified retentivity settings (timer, counter, bit memory, DB area) | STOP | STOP | STOP | STOP |
| Motion Control technology objects: Changes to MC Servo cycle clock, change from free-running to cyclical (and vice versa). Changes to the HW interface of the TO | - | - | - | STOP |
| * If the interface change results in structural changes at the instance DB, see "Modified DB...".  ** For information on the effect of downloading data block changes on the data block content, see section "Downloading data blocks to the CPU". |  |  |  |  |

### Loading changes in RUN with older CPU firmware versions

The table below shows the changes you can load in RUN mode and for older CPU firmware versions.

|  | S7-1200  V1.0 - 2.1 | S7-1200  V2.2 - V3.0 |
| --- | --- | --- |
| Action/type of change | Download possible in operating state ... |  |
| Modified properties of HW components.  This includes changes to comments in the HW configuration. | STOP | STOP |
| Added HW components | STOP | STOP |
|  |  |  |
| New/revised text lists (alarms) | STOP | STOP |
| Revised comments (new, revised, deleted) with the exception of comments in the HW configuration. | STOP | **RUN** |
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

### Downloading data blocks to the CPU

Depending on the conditions, the download of new or modified data blocks has an effect on the actual values in the data block:

| Symbol | Meaning |
| --- | --- |
| Download new data blocks | Actual values in the new data blocks are set to the initial values. |
| Download structurally modified data blocks (memory reserve not enabled) | Actual values of added tags in the structurally modified data blocks are set to initial values. |
| Download structurally modified data blocks (memory reserve enabled) | The following actual values are retained:  - Actual values of tags outside the memory reserve - Actual values of tags that were not modified within the memory reserve.   Actual values of added tags within the memory reserve are set to initial values. |
| Download of simply modified data blocks (no structural modification) | Actual values are retained. |

### Additional information

Additional information on download of block extensions without re-initialization and download of modified values for data blocks is available at "See also".

---

**See also**

[Downloading blocks in the program editor to device (S7-300, S7-400)](#downloading-blocks-in-the-program-editor-to-device-s7-300-s7-400)
  
[Downloading blocks from the project tree to the device (S7-300, S7-400)](#downloading-blocks-from-the-project-tree-to-the-device-s7-300-s7-400)
  
[Downloading project data to a device](Editing%20project%20data.md#downloading-project-data-to-a-device)

## Downloading blocks in the program editor to device (S7-300, S7-400)

### Requirement

The block to be downloaded is open.

### Procedure

To load a block from the program editor to the device, follow these steps:

1. Right-click in the Instruction window of the program editor.
2. Select the "Download to device" command in the shortcut menu.

   - If you have not already established an online connection, the "Extended download to device" dialog opens. In this case, set all parameters required for the connection and click "Load".
   - You can save your preferred connection parameters as default under "Options > Settings > Online & Diagnostics". When you first load with new connection parameters, a query is automatically displayed whether you want to store it as a default setting. Click "Yes", if you want to save the current connection parameters as default.
   - You have the option of showing all compatible devices by selecting the corresponding option and clicking the "Start search" command. You can also open the "Extended download to device" dialog with the "Online" menu.

     See also: [Establishing and terminating an online connection](Using%20online%20and%20diagnostics%20functions.md#establishing-or-changing-an-online-connection)
   - If the device is already online, the project data is compiled if necessary and the "Load preview" dialog opens. This dialog displays messages and recommends actions necessary for loading.
3. Check the alarms and, where necessary, enable the actions in the "Action" column.

   As soon loading becomes possible, the "Load" button is enabled.
4. Click "Load".

   If there is a need for synchronization, the system automatically displays the "Synchronization" dialog. This dialog displays alarms and suggests actions that are needed for the synchronization. You have the option of performing these actions or forcing the download without synchronization by clicking "Force download to device". If you have performed the suggested actions, you will be asked whether you want to continue with the download. Click "Continue download" in order to download the block. The "Load results" dialog then opens and shows you the status and the actions after the download operation.
5. If you want to start the modules again directly after downloading, select the "Start all" check box.
6. To close the "Load results" dialog box, click "Finish".

**Note**

Performing the proposed actions during ongoing plant operation can cause serious damage to property or injury to persons if there are functional faults or program errors.

Make sure that no dangerous situations can arise before you start the actions.

**Note**

To avoid inconsistencies between calling and called blocks, download all affected blocks each time you make global changes, such as changes in the block interface. Select the "Consistent download" action.

### Result

The code for the block is downloaded to the device. If you have selected "Consistent download", then all blocks that are subject to this change will be compiled and downloaded to the device.

The messages under "Info > General" in the Inspector window report indicate whether the loading process was successful.

---

**See also**

[Downloading blocks from the project tree to the device (S7-300, S7-400)](#downloading-blocks-from-the-project-tree-to-the-device-s7-300-s7-400)
  
[Downloading project data to a device](Editing%20project%20data.md#downloading-project-data-to-a-device)
  
[Downloading blocks in the "RUN" operating state to the device (S7-300, S7-400)](#downloading-blocks-in-the-run-operating-state-to-the-device-s7-300-s7-400)
  
[Default setting online connection data](Using%20online%20and%20diagnostics%20functions.md#default-setting-online-connection-data)

## Downloading blocks from the project tree to the device (S7-300, S7-400)

In the project tree you can download one block, multiple blocks or all blocks to a device.

### Loading one or more blocks from the project tree to the device

To load one or more blocks to the device from the project tree, follow these steps:

1. Open the "Program blocks" folder in project tree.
2. Select the blocks you want to download.
3. Select the "Download to device > Software (only changes)" command from the shortcut menu.

   - If you have not already established an online connection, the "Extended download to device" dialog opens. In this case, set all parameters required for the connection and click "Load". You can also open the "Extended download to device" dialog with the "Online" menu.

     See also: [Establishing and terminating an online connection](Using%20online%20and%20diagnostics%20functions.md#establishing-or-changing-an-online-connection)
   - If the device is already online, the project data is compiled if necessary and the "Load preview" dialog opens. This dialog displays messages and recommends actions necessary for loading.
4. Check the alarms and, where necessary, enable the actions in the "Action" column.

   As soon as loading becomes possible, the "Load" button is enabled.
5. Click "Load".

   The block is loaded and the "Load results" dialog opens. This dialog shows you the status and the actions after downloading.
6. To close the "Load results" dialog box, click "Finish".

**Note**

Performing the proposed actions during ongoing plant operation can cause serious damage to property or injury to persons if there are functional faults or program errors.

Make sure that no dangerous situations can arise before you start the actions.

**Note**

To avoid inconsistencies between calling and called blocks, download all affected blocks each time you make global changes, such as changes in the block interface. Select the "Consistent download" action.

### Loading blocks from the project tree to the device

To download all blocks in the "Program blocks" folder to the device from the project tree, follow these steps:

1. Select the "Program blocks" folder in the project tree.
2. Select the "Download to device" submenu in the shortcut menu.
3. If you only want to download the changes since the last download, select the "Software (only changes)" option. If all blocks are to be fully loaded and all values are to be reset to their start values, select "Download PLC program to the device and reset".

   - If you have not already established an online connection, the "Extended download to device" dialog opens. In this case, set all parameters required for the connection and click "Load". You can also open the "Extended download to device" dialog with the "Online" menu.

     See also: [Establishing and terminating an online connection](Using%20online%20and%20diagnostics%20functions.md#establishing-or-changing-an-online-connection)
   - If you have already specified an online connection, then the project data is compiled if necessary and the "Load preview" dialog opens. This dialog displays alarms and proposes actions necessary for loading.
4. Check the alarms and, where necessary, enable the actions in the "Action" column.

   As soon as loading becomes possible, the "Load" button is enabled.
5. Click "Load".

   The block is loaded and the "Load results" dialog opens. This dialog shows you the status and the actions after downloading.
6. To close the "Load results" dialog box, click "Finish".

**Note**

Performing the proposed actions during ongoing plant operation can cause serious damage to property or injury to persons if there are functional faults or program errors.

Make sure that no dangerous situations can arise before you start the actions.

**Note**

To avoid inconsistencies between calling and called blocks, download all affected blocks each time you make global changes, such as changes in the block interface. Select the "Consistent download" action.

### Result

The code for the blocks is downloaded to the device. If the changes affect additional blocks, these will be compiled and also downloaded to the device. Blocks that only exist online in the device are deleted. Inconsistencies between the blocks in the user program are avoided by loading all blocks affected and deleting the unneeded blocks in the device.

The messages under "Info > General" in the Inspector window report indicate whether the loading process was successful.

---

**See also**

[Downloading blocks in the program editor to device (S7-300, S7-400)](#downloading-blocks-in-the-program-editor-to-device-s7-300-s7-400)
  
[Downloading project data to a device](Editing%20project%20data.md#downloading-project-data-to-a-device)
  
[Downloading blocks in the "RUN" operating state to the device (S7-300, S7-400)](#downloading-blocks-in-the-run-operating-state-to-the-device-s7-300-s7-400)

## Uploading blocks from device (S7-300, S7-400)

You can upload either all the blocks or only individual blocks from a device to your project.

> **Note**
>
> Although SCL blocks and GRAPH function blocks can be loaded from an S7-300/400, they cannot be edited once loaded.

### Requirement

The online and offline versions of a blocks to be loaded differ or the blocks only exist online.

### Downloading all blocks from a device

To download all blocks from a device, follow these steps:

1. Establish an online connection with the device from which you want to upload the blocks.

   See also: [Establishing and terminating an online connection](Using%20online%20and%20diagnostics%20functions.md#establishing-or-changing-an-online-connection)
2. In the project tree, select the device folder from which you want to upload blocks.
3. In the "Online" menu, select the "Upload from device" command.

   The "Upload preview" dialog box opens. This dialog displays messages and recommends actions necessary for loading.
4. Check the alarms and, where necessary, enable the actions in the "Action" column.

   As soon as uploading becomes possible, the "Upload from device" button is enabled.
5. Click the "Upload from device" button.

   The load process is executed.

### Downloading individual blocks from a device

To upload individual blocks from a device, follow these steps:

1. Establish an online connection with the device from which you want to upload the blocks.

   See also: [Establishing and terminating an online connection](Using%20online%20and%20diagnostics%20functions.md#establishing-or-changing-an-online-connection)
2. In the project tree, select the blocks that you want to upload from the device.
3. In the "Online" menu, select the "Upload from device" command.

   The load process is executed.

### Result

The blocks will be uploaded from the device to the project. You can edit, recompile and load the blocks in the device again.

## Downloading blocks to a memory card (S7-300, S7-400)

### Requirement

The "Program blocks" folder of the memory card is open.

### Procedure

To download blocks to a memory card, follow these steps:

1. Open the "Program blocks" folder of the device in the project tree.
2. Select the blocks you want to download to the memory card.
3. Drag the blocks in project tree to the "Program blocks" folder of the memory card. You can also copy the blocks and add them to the memory card.

   If necessary, the blocks are compiled. The "Load preview" dialog then opens. This dialog displays messages and recommends actions necessary for loading.
4. Check the alarms and, where necessary, enable the actions in the "Action" column.

   As soon as loading becomes possible, the "Load" button is enabled.
5. Click the "Load" button.

   The load process is executed.

**Note**

Performing the proposed actions during ongoing plant operation can cause serious damage to property or injury to persons if there are functional faults or program errors.

Make sure that no dangerous situations can arise before you start the actions.

Or:

1. In the project tree, select the blocks that you want to upload.
2. Select the "Card Reader/USB memory > Write to memory card" command in the "Project" menu.

   The "Select memory card" dialog opens.
3. Select a memory card that is compatible with the CPU.

   A button with a green check mark is activated at the bottom of the dialog.
4. Click the button with the green check mark.

   If necessary, the project data is compiled. The "Load preview" dialog then opens. This dialog displays messages and recommends actions necessary for loading.
5. Check the alarms and, where necessary, enable the actions in the "Action" column.

   As soon as loading becomes possible, the "Load" button is enabled.
6. Click the "Load" button.

   The load process is executed.

### Result

The selected blocks will be downloaded to the memory card. The messages under "Info > General" in the Inspector window report indicate whether the loading process was successful.

---

**See also**

[Uploading blocks from a memory card (S7-300, S7-400)](#uploading-blocks-from-a-memory-card-s7-300-s7-400)
  
[Accessing memory cards](Editing%20project%20data.md#accessing-memory-cards)

## Uploading blocks from a memory card (S7-300, S7-400)

You can only upload all blocks from a memory card to your project. Note that no symbolic information is loaded when you upload from a memory card.

### Requirement

The memory card is displayed.

See also: [Accessing memory cards](Editing%20project%20data.md#accessing-memory-cards)

### Procedure

To upload blocks from a memory card to your project, follow these steps:

1. In the project tree, drag the memory card folder to the device folder in the project. You can also copy the memory card and insert it in the device.

   The "Upload preview" dialog box opens. This dialog displays messages and recommends actions necessary for loading.
2. Check the alarms and, where necessary, enable the actions in the "Action" column.

   As soon as uploading becomes possible, the "Upload from device" button is enabled.
3. Click the "Upload from device" button.

---

**See also**

[Downloading blocks to a memory card (S7-300, S7-400)](#downloading-blocks-to-a-memory-card-s7-300-s7-400)

## Switching off the sequencer prior to loading a GRAPH DB (S7-300, S7-400)

You can specify the switching off of the sequencer prior to loading an instance data block either globally or during the load operation.

### Globally switching off the sequencer

To switch off the sequencer globally for each loading operation of an instance data block, follow these steps:

1. Select the "Settings" command in the "Options" menu.

   The "Settings" window is displayed in the work area.
2. Select the "PLC programming > GRAPH" group in the area navigation.
3. Select the "Turn off sequence before downloading DB" check box.

   For future loading operations, the sequencer is switched off prior to loading of the instance data block.

### Switching off the sequencer during the loading operation

To switch off the sequencer during the loading operation, follow these steps:

1. Load the GRAPH function block to the device.

   During the loading operation, the "Load preview" dialog opens. This dialog displays alarms and suggests the required actions for loading. If the instance data block must be loaded together with the GRAPH function block, the "Load preview" dialog suggests the action "Turn off sequence before downloading the DB".
2. Select the "Turn off sequence before downloading DB" check box.

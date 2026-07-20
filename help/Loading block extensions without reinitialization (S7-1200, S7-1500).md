---
title: "Loading block extensions without reinitialization (S7-1200, S7-1500)"
package: ProgExtMem15enUS
topics: 7
devices: [S7-1200, S7-1500, S7-1500T]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Loading block extensions without reinitialization (S7-1200, S7-1500)

This section contains information on the following topics:

- [Basic information on loading block extensions without reinitialization (S7-1200, S7-1500)](#basic-information-on-loading-block-extensions-without-reinitialization-s7-1200-s7-1500)
- [Setting the reserved memory for block extensions (S7-1200, S7-1500)](#setting-the-reserved-memory-for-block-extensions-s7-1200-s7-1500)
- [Activating memory reserve (S7-1200, S7-1500)](#activating-memory-reserve-s7-1200-s7-1500)
- [Deactivating memory reserve (S7-1200, S7-1500)](#deactivating-memory-reserve-s7-1200-s7-1500)
- [Extending the block interface or data block (S7-1200, S7-1500)](#extending-the-block-interface-or-data-block-s7-1200-s7-1500)
- [Resetting the reserved memory (S7-1200, S7-1500)](#resetting-the-reserved-memory-s7-1200-s7-1500)

## Basic information on loading block extensions without reinitialization (S7-1200, S7-1500)

### Description

To enable the subsequent editing of PLC programs that have already been commissioned and are running without error on a system, CPUs of the S7-1200 V4 and higher and S7-1500 series support the option of extending the interfaces of function or data blocks during runtime.

You can download the modified blocks without setting the CPU to STOP and without affecting the values of already loaded tags.

This is a simple means of implementing program changes. This load process (download without reinitialization) will not have a negative impact on the controlled process.

### Principle of operation

In principle, every function or data block has a memory reserve by default, which can be used for subsequent interface changes. The memory reserve is not used initially. Activate the memory reserve if you have compiled and loaded the block and then decide that you want to load interface changes later. All tags that you subsequently declare will be saved to the memory reserve. A subsequent download has no impact on the values of tags that have already been loaded.

If you decide to revise your program at a later time while the plant is not in operation, you also have the option of resetting the memory layout of one or more blocks in one step. With this action, you move all tags from the reserve area to the regular area. The memory reserve is now cleared and made available for further interface extensions.

### Requirements

This "Download without reinitialization" function is available if the following requirements are met:

- The project is in the "TIA Portal V12" format or a higher version.
- You are working with a CPU of the S7-1200 V4 or higher or S7-1500 series.
- The blocks were created in LAD, FBD, STL, or SCL.
- The blocks were created by the user, i.e. they were not included in your delivery package.
- They are blocks with "optimized access".

The following blocks do not offer the option of downloading block extensions without reinitialization:

- GRAPH blocks
- ARRAY data blocks
- ProDiag blocks
- CEM blocks

> **Note**
>
> **Restriction regarding use of the memory reserve**
>
> It is not possible to assign the contents of a global data block to a structurally identical data block, e.g. using a move box, if one of the two DBs has a memory reserve.

### Basic steps

Perform the following steps if you want to extend the interface of a function or data block and then load the block without reinitialization. A detailed description of the individual steps can be found in the following chapters:

1. By default, all blocks have a memory reserve of 100 bytes in the non-retentive memory. If needed, you can adjust the amount of memory reserve or define additional memory reserve in the retentive memory.
2. Activate the memory reserve.
3. Extend the block interface.
4. Compile the block.
5. Download the block to the CPU as usual.

### Overview of settings for memory reserve

The overview of the project tree shows the settings for memory reserve for all program blocks at a glance:

To display the overview, follow these steps:

1. Select the "Program blocks" folder in the project tree.
2. Click "Maximizes/minimizes the Overview".

---

**See also**

[General information on loading](Editing%20project%20data.md#general-information-on-loading)
  
[Initializing setpoint values in the online program](Programming%20data%20blocks.md#initializing-setpoint-values-in-the-online-program)
  
[Setting the reserved memory for block extensions (S7-1200, S7-1500)](#setting-the-reserved-memory-for-block-extensions-s7-1200-s7-1500)
  
[Activating memory reserve (S7-1200, S7-1500)](#activating-memory-reserve-s7-1200-s7-1500)
  
[Deactivating memory reserve (S7-1200, S7-1500)](#deactivating-memory-reserve-s7-1200-s7-1500)
  
[Extending the block interface or data block (S7-1200, S7-1500)](#extending-the-block-interface-or-data-block-s7-1200-s7-1500)
  
[Resetting the reserved memory (S7-1200, S7-1500)](#resetting-the-reserved-memory-s7-1200-s7-1500)

## Setting the reserved memory for block extensions (S7-1200, S7-1500)

### Introduction

Essentially, each function or data block has a reserve of 100 bytes by default. This reserve is not located in the block's retentive memory area. By default, no reserve is available in the retentive memory area, since the retentive memory is restricted to the CPU.

You can change the default value of 100 bytes, which applies to all newly created blocks in the project. Furthermore, you can change the size of the reserved memory individually for specific blocks and define a reserve in the retentive memory area for specific blocks.

### Setting the amount of reserved memory for new blocks

To set the size of the reserved memory for all newly created blocks in the project, proceed as follows:

1. Select the "Settings" command in the "Options" menu.

   The "Settings" window is displayed in the work area.
2. Select the "PLC programming &gt; General" group in the area navigation.
3. In the "Reserved memory for download without reinitialization" group, enter in the "Memory reserve" input box the desired number of bytes to be allocated for a later extension of the block interface.

   Newly created function blocks and global data blocks now get a reserved memory in the specified size. Blocks that already exist are not affected by this change.

**Note**

The setting is only valid for blocks that support the "Download without reinitialization" function. Other blocks are not influenced by this setting.

### Setting the amount of reserved memory for an existing block

To set the amount of reserved memory for an existing block, proceed as follows:

1. Select the block in the project tree.
2. Select the "Properties" command in the shortcut menu.  
   The "Properties" dialog opens.
3. Select the "Download without reinitialization" group in the area navigation.
4. Enter the desired number of bytes in the "Memory reserve" input box.
5. To define a reserve in retentive memory, select the "Enable download without reinitialization for retentive tags" check box and enter the desired number of bytes in the "Retentive reserved memory" input box.

**Note**

Please note the following:

- If you have already activated reserved memory for the current block, you can no longer change the size of the reserved memory.
- In the memory, data elements are sorted according to specific rules that allow the fastest possible access while the program is running. This is why the available memory is sometimes reduced by more than the actual size of the data element when a new data element is added.

  For example, the available memory area may be reduced by four bytes when an element of the "WORD" type and an element of the "BYTE" type are added, since all data elements are aligned to a WORD limit.

---

**See also**

[Basic information on loading block extensions without reinitialization (S7-1200, S7-1500)](#basic-information-on-loading-block-extensions-without-reinitialization-s7-1200-s7-1500)

## Activating memory reserve (S7-1200, S7-1500)

### Introduction

Each function or data block is always assigned a default memory reserve. However, this memory reserve is not used initially. Activate the memory reserve if you have compiled and loaded the block and then decide that you want to load interface changes later. All tags that you subsequently declare will be saved to the memory reserve.

### Requirements

- The block is currently compiled.
- The block contains a memory reserve.

### Procedure

To activate the memory reserve for a function block or global data block, proceed as follows:

1. Open the block.
2. Select the "Keep actual values" button in the toolbar:

### Result

- As of now, all newly declared tags will be stored in the memory reserve and can therefore be downloaded without affecting the process that is running.
- It is no longer possible to delete existing tags. Their properties can no longer be changed, except for the properties "Default value", "Start value" and "Comment".
- Local constants which are used as ARRAY limits can no longer be changed, because changing the constant value could have an effect on the memory layout of the block.

---

**See also**

[Basic information on loading block extensions without reinitialization (S7-1200, S7-1500)](#basic-information-on-loading-block-extensions-without-reinitialization-s7-1200-s7-1500)

## Deactivating memory reserve (S7-1200, S7-1500)

### Introduction

In order to revise the memory layout of a block at a later time when the plant is not in operation, you can deactivate the reserved memory. With this action, you move all tags from the reserve area to the regular area. The reserved memory remains in existence and is now made available for further interface extensions. It then has the size which is defined in the block properties again.

> **Note**
>
> Please note that the block has to be compiled and loaded again after you have deactivated the reserved memory. It is not possible to perform a "Download without reinitialization" after deactivating the reserved memory.

### Requirement

The block's reserved memory is activated.

### Procedure

To activate the reserved memory for a function block or global data block, proceed as follows:

1. Open the block.
2. Select the "Keep actual values" button in the toolbar:

### Result

With this action, you move all tags that were previously located in the reserve area to the regular area. As a result, the block has to compiled and loaded again. The values of the tags in the CPU are reinitialized during loading.

---

**See also**

[Basic information on loading block extensions without reinitialization (S7-1200, S7-1500)](#basic-information-on-loading-block-extensions-without-reinitialization-s7-1200-s7-1500)

## Extending the block interface or data block (S7-1200, S7-1500)

### Introduction

You can add new tags after you have activated the reserved memory of a function block or global data block.

### Requirement

The reserved memory is activated.

### Procedure

To declare additional tags, follow these steps:

1. Select a declaration section, for example "Input", "Output", "InOut" or "Static".
2. In the selected section, declare as usual one or more tags and enter their properties in the columns. In the "Retain" column of an FB, you can select only between the "Retain" and "Non-retain" settings. The "Set in IDB" setting is not available in the reserved memory.
3. Compile the changed blocks, for example by selecting them in the project tree and selecting the command "Compile&gt; Software (only changes)" in the shortcut menu.

   During compiling, the newly declared tags are inserted into the reserved memory. If the reserved memory is too small, the compiling is terminated and an error message notifies you about this.
4. Load the changed blocks, for example by selecting them in the project tree and selecting the command "Load &gt; Software (only changes)" in the shortcut menu.

   When you load block extensions, only the newly added tags with defined start values are initialized. The existing online tags are not reinitialized.

**Note**

It is not possible to add new tags within a tag with structured data type. You cannot declare any new structure elements within an existing structure, for example.

However, you can create new structures within the reserved memory.

---

**See also**

[Basic information on loading block extensions without reinitialization (S7-1200, S7-1500)](#basic-information-on-loading-block-extensions-without-reinitialization-s7-1200-s7-1500)

## Resetting the reserved memory (S7-1200, S7-1500)

### Introduction

If you decide to revise your program at a later time while the plant is not in operation, you have the option of resetting the reserved memory of one or more blocks in one step. With this action, you move all tags from the reserved memory to the regular memory area. The reserved memory is now cleared and made available for further interface extensions.

### Requirement

- The block's reserved memory is activated.
- The reserved memory contains tags.

### Procedure

To reset the reserved memory of one or more blocks, follow these steps:

1. Select the "Program blocks" folder, or specific blocks in this folder.
2. Select the "Compile &gt; Software (Reset memory reserve)" command from the shortcut menu.

### Result

All tags in the selected blocks that were previously located in the reserved memory area are moved from this area to the regular area. The block is recompiled. The tags are reinitialized during the next loading. The block's configured reserved memory is retained and continues to be active.

| Symbol | Meaning |
| --- | --- |
|  | **Danger** |
| **Reinitialization at the next load**  When you reset the reserved memory, all the tags that were previously in the reserved memory are reinitialized the next time you load. This is true for both retentive and non-retentive tags.  Changing tag values during ongoing plant operation can cause serious material damage and personal injuries! It is therefore very important that you check the program thoroughly in a test environment after resetting the reserved memory before putting it in operation. |  |

---

**See also**

[Basic information on loading block extensions without reinitialization (S7-1200, S7-1500)](#basic-information-on-loading-block-extensions-without-reinitialization-s7-1200-s7-1500)

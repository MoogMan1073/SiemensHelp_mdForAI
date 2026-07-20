---
title: "Programming data blocks"
package: ProgPLCDatablockenUS
topics: 46
devices: [S7-1200, S7-1500, S7-1500T]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Programming data blocks

This section contains information on the following topics:

- [Basic principles for programming of data blocks](#basic-principles-for-programming-of-data-blocks)
- [Structure of the declaration table for data blocks](#structure-of-the-declaration-table-for-data-blocks)
- [Creating data blocks](#creating-data-blocks)
- [Updating data blocks](#updating-data-blocks)
- [Extending data blocks (S7-1200, S7-1500)](#extending-data-blocks-s7-1200-s7-1500)
- [Creating a data structure for global data blocks](#creating-a-data-structure-for-global-data-blocks)
- [Defining start values](#defining-start-values)
- [Setting retentivity](#setting-retentivity)
- [Editing the properties of tags in data blocks](#editing-the-properties-of-tags-in-data-blocks)
- [Editing the declaration table for data blocks](#editing-the-declaration-table-for-data-blocks)
- [Online and diagnostic functions for data blocks](#online-and-diagnostic-functions-for-data-blocks)

## Basic principles for programming of data blocks

A data block (DB) is used to save the values that are written during execution of the program.

In contrast to the code block, the data block contains only tag declarations. It contains no networks or instructions. The tag declarations define the structure of the data block.

### Types of data blocks

There are two types of data blocks:

- Global data blocks

  The global data block is not assigned to a code block. You can access the values of a global data block from any code block. A global data block contains only static tags.

  The structure of the global data block can be freely defined. In the declaration table for data blocks, you declare the data elements that are to contained in the global data block.
- Instance data blocks

  The instance data block is assigned directly to a function block (FB). The structure of an instance data block cannot be freely defined, but is instead determined by the interface declaration of the function block. The instance data block contains exactly those block parameters and tags that are declared there.

  However, you can define instance-specific values in the instance data block, for example, start values for the declared tags.

### ARRAY data blocks (S7-1500)

ARRAY data blocks are global data blocks that consist of an ARRAY. This ARRAY can be based on any data type. For example, an ARRAY of a PLC data type (UDT) is possible. The DB contains no other elements besides the ARRAY. Because of their flat structure, ARRAY data blocks facilitate access to the ARRAY elements and their transfer to called blocks.

You use ARRAY data blocks to address ARRAYs indirectly: You can determine during runtime which ARRAY DB is read or written and how large it is.

The "Move operations" section of the "Instructions" task card offers options for addressing of ARRAY DBs.

> **Note**
>
> **Retentivity of ARRAY data blocks**
>
> ARRAY data blocks and their components cannot be set retentively.

See also:

[Example of the use of ARRAY data blocks](Programming%20basics.md#example-of-the-use-of-array-data-blocks)

### PLC data types as a template for global data blocks

PLC data types can be used as templates for the creation of global data blocks with identical data structures. You create the structure as PLC data type only once and then generate the required data blocks by assigning the PLC data type.

### System data types as a template for global data blocks

System data types can also be used as templates for creating global data blocks with identical data structure. System data types already have a pre-defined structure. You insert the system data type in the program only once and then generate additional data blocks with an identical structure by assigning the system data type.

### Access modes

There are two different modes of accessing data values in data blocks:

- Data blocks with optimized access (only S7-1200)

  Data blocks with optimized access have no fixed defined structure. In the declaration, the data elements are assigned only a symbolic name and no fixed address within the block. You access the data values in these block via symbolic names.

  The "Optimized block access" attribute is always enabled for ARRAY data blocks.
- Data blocks with standard access (all CPU families)

  Data blocks with standard access have a fixed structure. In the declaration, the data elements are assigned both a symbolic name and a fixed address within the block. You can access the data values in this block via the symbolic names or addresses.

  Data blocks with standard access are tailored to WORD limits. This means that they always occupy one WORD (16 bits) or a multiple thereof. If necessary, tags are automatically added to the data block during compilation so that the block fills the space to the next WORD.

  ARRAY data blocks with standard access are not possible.

### Retentivity of data values

To prevent data loss in the event of power failure, you can store the data values in a retentive memory area.

---

**See also**

[Creating data blocks](Creating%20and%20managing%20blocks.md#creating-data-blocks)
  
[Global data blocks (DB)](Programming%20basics.md#global-data-blocks-db)
  
[Instance data blocks](Programming%20basics.md#instance-data-blocks)
  
[Blocks with optimized access](Programming%20basics.md#blocks-with-optimized-access)

## Structure of the declaration table for data blocks

### Structure of the declaration table for data blocks

The figure below shows the structure of the declaration table for data blocks. The display will vary depending on type of block and type of access.

![Structure of the declaration table for data blocks](images/83550810763_DV_resource.Stream@PNG-en-US.png)

### Display of instance-specific values

In instance data blocks, you can apply the already defined values from the interface of the assigned function block or define instance-specific start values. Values that are applied from the function block cannot be edited. You can replace the grayed-out values with instance-specific values. Values that were already changed instance specific are not grayed out.

### Meaning of the columns

The following table shows the meaning of the individual columns. You can show or hide the columns as required. The number of columns displayed varies depending on the CPU series.

| Column | Explanation |
| --- | --- |
| ![Meaning of the columns](images/45636405771_DV_resource.Stream@PNG-de-DE.png) | Symbol you can click to move or copy the tag. You can, for example, drag-and-drop the tag into a program and use it there as operand. |
| Name | Name of the tags. |
| Data type | Data type of the tags. |
| Offset | Relative address of the tags.   The column is only visible in data blocks with standard access.  Note:  Many instructions from the SIMATIC system libraries have the "optimized block access" property and therefore do not occupy any fixed memory addresses. No offset is displayed for these instructions, even if you use them as multi-instance in a block with standard access. |
| Default value | Default value of the tag in the interface of a higher-level code block or in a PLC data type.   The values contained in the "Default value" column can only be changed in the higher-level code block or PLC data type. The values are only displayed in the data block. |
| Start value | Value that the tag should assume at startup.  The default values defined in a code block are used as start values during the creation of the data block. You can then replace these adopted values with instance-specific start values.   Specification of an start value is optional. If you do not specify any value, the tag assumes the default value at startup. If a default is not defined either, the default value valid for the data type is used. For example, the value "FALSE" is specified as default value for BOOL. |
| Monitor value | Current data value in the CPU.   This column only appears if an online connection is available and you click "Monitor". |
| Snapshot | Shows values that were loaded from the device. |
| Retain | Marks the tag as retentive. The values of retentive tags are retained even after the power supply is switched off. |
| Visible in HMI engineering | Shows whether the tag is visible by default in the HMI selection list. |
| Accessible from HMI/OPC UA/Web API | Indicates whether HMI/OPC UA/Web API can access this variable during runtime.  Absolute access to non-optimized data, e.g. through ANY pointers are possible, even if the attribute from "Accessible from HMI/OPC UA/Web API" is deactivated. |
| Writable from HMI/OPC UA/Web API | Indicates whether or not the tag can be written from HMI/OPC UA/Web API during runtime.  Absolute access to non-optimized data, e.g. through ANY pointers are possible, even if the attribute from "Writable from HMI/OPC UA/Web API" is deactivated. |
| Setpoint | Setpoint are the values that will probably have to be fine tuned during commissioning. After commissioning, the values of these tags can be transferred to the offline program as start values and stored there. |
| Supervision | Indicates whether monitoring for process diagnostics was created for the tag. |
| Comment | Comment to document the tags. |

---

**See also**

[Editing the properties of tags in data blocks](#editing-the-properties-of-tags-in-data-blocks)
  
[Using setpoints during commissioning](#using-setpoints-during-commissioning)
  
[Creating data blocks](Creating%20and%20managing%20blocks.md#creating-data-blocks)
  
[Creating a data structure for global data blocks](#creating-a-data-structure-for-global-data-blocks)
  
[Basic information on start values](#basic-information-on-start-values)
  
[Defining start values](#defining-start-values)
  
[Setting retentivity](#setting-retentivity)

## Creating data blocks

### Requirement

The "Program blocks" folder in the project tree is open.

### Procedure

To create a data block, follow these steps:

1. Double-click the "Add new block" command.

   The "Add new block" dialog box opens.
2. Click the "Data block (DB)" button.
3. Select the type of the data block. You have the following options available to you:

   - To create a global data block, select the list entry "Global DB".
   - To create an ARRAY data block, select the "ARRAY DB" entry in the list.
   - To create an instance data block, select the function block to which you want to assign the instance data block from the list. The list contains only the function blocks that were previously created for the CPU.
   - To create a data block based on a PLC data type, select the PLC data type from the list. The list contains only the PLC data types that were previously created for the CPU.
   - To create a data block based on a system data type, select the system data type from the list. The list contains only those system data types that have already been inserted to program blocks in the CPU.
4. Enter a name for the data block. The name can contain up to 125 characters when no namespace has been defined for the data block.
5. Optional within software units: Enter a namespace for the new data block or use the namespace preset of the software unit.
6. Enter the properties of the new data block.
7. If you have selected an ARRAY DB as the data block type, enter the ARRAY data type and the high limit for the ARRAY.

   You can change the high limit for the ARRAY at any time in the property window of the created block. The ARRAY data type cannot be changed subsequently.
8. If you have selected a block that contains monitoring as the "Type", assign a ProDiag function block to the monitoring functions.
9. To enter additional properties of the new data block, click "Additional information".

   An area with further text boxes is displayed.
10. Enter all the properties you require.
11. Activate the "Add new and open" check box if the block does not open as soon as it is created.
12. Confirm your entry with "OK".

**Note**

**Namespaces in software units**

You can find information on namespaces, in particular on the naming conventions according to IEC 61131-3, here:

[Categorizing program elements in namespaces](Using%20software%20units%20%28S7-1500%29.md#categorizing-program-elements-in-namespaces-s7-1500)

### Result

The new data block is created. You can find the data block in the project tree in the "Program blocks" folder.

> **Note**
>
> **Retentivity of ARRAY data blocks**
>
> ARRAY data blocks and their components cannot be set retentively.

---

**See also**

[Global ARRAY data blocks (DB)](Programming%20basics.md#global-array-data-blocks-db)
  
[Basic principles for programming of data blocks](#basic-principles-for-programming-of-data-blocks)
  
[Global data blocks (DB)](Programming%20basics.md#global-data-blocks-db)
  
[Instance data blocks](Programming%20basics.md#instance-data-blocks)
  
[System data types](Data%20types.md#system-data-types-1)
  
[Using blocks from libraries](Creating%20and%20managing%20blocks.md#using-blocks-from-libraries)

## Updating data blocks

### Introduction

Changes in the interface of a function block or a PLC data type can lead to the corresponding data blocks becoming inconsistent. These inconsistencies are marked in red in the declaration table and at the call point of the block. To remedy these inconsistencies, the data blocks must be updated.

You have three options to update block calls:

- Explicit updating in the declaration table for data blocks.

  The data block is updated. Changes from the interface of the assigned function block and changes to the used PLC data types are applied.
- Explicit updating in the program editor.

  The block calls in the open block will be updated. The associated instance data block is also adjusted in the process.
- Implicit updating during compilation.

  All block calls in the program as well as the used PLC data types and the corresponding instance data blocks are updated.

### Explicit Updating in the Declaration Table for Data Blocks

To explicitly update an individual data block, follow these steps:

1. Open the data block.
2. Select "Update interface" in the shortcut menu.

### Explicit Updating in the Program Editor

To update all block calls or a specific call within a block, follow these steps:

1. Open the block in the program editor.
2. Right-click on the instruction with the block call.
3. Select the "Update" command in the shortcut menu.
4. The "Interface update" dialog opens. This dialog shows the differences between the block interface in use and the changed interface of the called block.
5. If you want to update the block call, click "OK". To cancel the update, click "Cancel".

### Implicit Updating during Compilation

To implicitly update all block calls and uses of PLC data types as well as the instance data blocks during the compiling, follow these steps:

1. Open the project tree.
2. Select the "Program blocks" folder.
3. Select the command "Compile > Software (rebuild all blocks)" in the shortcut menu.

---

**See also**

[Changing the properties of tags in instance data blocks](#changing-the-properties-of-tags-in-instance-data-blocks)

## Extending data blocks (S7-1200, S7-1500)

### Description

In order to enable the editing of PLC programs that have already been commissioned and that are running without error on a system, CPUs of the S7-1500 series and most CPUs of the S7-1200 V4 and higher series support the option of extending global data blocks during runtime.

You can download the modified blocks without setting the CPU to STOP and without affecting the values of already loaded tags.

This is a simple means of implementing program changes. This load process (download without reinitialization) will not have a negative impact on the controlled process.

### Principle of operation

Each data block is always assigned a default memory reserve. The memory reserve is not used initially. Activate the memory reserve if you decide on loading interface changes after having compiled and downloaded the block. All tags that you subsequently declare will be saved to the memory reserve. A subsequent download has no impact on the values of tags that have already been loaded.

If you decide to review your program at a later time while the plant is not in operation, you are also provided an option of reworking the memory layout of individual or several blocks in a single pass. With this action, you move all tags from the reserve area to the regular area. The memory reserve is now cleared and made available for further interface extensions.

### Requirements

This "Download without reinitialization" function is available if the following requirements are met:

- The project is in the "TIA Portal V12" format or a higher version.
- You are working with a CPU that supports "Download without reinitialization".
- The blocks were created in LAD, FBD, STL, or SCL.
- The blocks were created by the user, i.e. they are not included with the blocks delivered in your package.
- These blocks are assigned the optimized access attribute.

### Basic steps

Perform the following steps if you want to extend the data block and then load the block without re-initialization.

1. All blocks have a default memory reserve of 100 bytes. You can adapt this memory reserve to suit your requirements.
2. Activate the memory reserve.
3. Extend the block interface.
4. Compile the block.
5. Download the block to the CPU as usual.

### Reference

For more information on the various steps, refer to chapter "Loading blocks (S7-1200/1500) ".

## Creating a data structure for global data blocks

This section contains information on the following topics:

- [Declaring tags of elementary data type](#declaring-tags-of-elementary-data-type)
- [Declaring tags of the ARRAY data type](#declaring-tags-of-the-array-data-type)
- [Declaring tags of STRUCT data type](#declaring-tags-of-struct-data-type)
- [Declaring tags of the STRING data type](#declaring-tags-of-the-string-data-type)
- [Declaring tags based on a PLC data type](#declaring-tags-based-on-a-plc-data-type)

### Declaring tags of elementary data type

#### Requirement

A global data block is open.

> **Note**
>
> You cannot change the structure of instance data blocks and of data blocks based on a PLC data type directly, since the structures of these blocks are defined by the respective function block or the PLC data type.
>
> The type of the data block is entered in the block properties.

#### Procedure

To declare a tag of the elementary data type, follow these steps:

1. Enter a tag name in the "Name" column.
2. In the "Data type" column, click the button for the data type selection.

   A list of the permissible data types is opened.
3. Select the desired data type.
4. Optional: Change the properties of the tags that are displayed in the other columns.
5. Repeat steps 1 to 4 for all tags that are to be declared.

---

**See also**

[Displaying and editing block properties](Creating%20and%20managing%20blocks.md#displaying-and-editing-block-properties)
  
[Declaring tags of the ARRAY data type](#declaring-tags-of-the-array-data-type)
  
[Declaring tags of STRUCT data type](#declaring-tags-of-struct-data-type)
  
[Editing tables](Introduction%20to%20the%20TIA%20Portal.md#editing-tables)
  
[Editing the declaration table for data blocks](#editing-the-declaration-table-for-data-blocks)
  
[Defining start values](#defining-start-values)
  
[Setting retentivity](#setting-retentivity)
  
[Online and diagnostic functions for data blocks](#online-and-diagnostic-functions-for-data-blocks)

### Declaring tags of the ARRAY data type

#### Requirement

A global data block is open.

#### Procedure

To declare a tag of the ARRAY data type, follow these steps:

1. Enter a tag name in the "Name" column.
2. Enter the "Array" data type in the "Data type" column. You will be supported by Autocomplete in this step.

   The "Array" dialog opens.
3. In the "Data type" text box, specify the data type of the array elements.
4. In the "ARRAY limits" input field, specify the high and low limit for each dimension.

   Example of a one-dimensional ARRAY:

   `ARRAY [0..3] of Bool`

   Example of a three-dimensional ARRAY:

   `ARRAY[0..3, 0..15, 0..33] of Bool`

   Example of a one-dimensional ARRAY with local constants as ARRAY limits

   `ARRAY[#My_local_const1..#My_local_const2] of Bool`

   Example of a one-dimensional ARRAY with global constants as ARRAY limits

   `ARRAY["My_global_const1".."My_global_const1"] of Bool`
5. Confirm your entry.
6. Optional: Change the properties of the tags that are displayed in the other columns.

The tag is created but remains collapsed. To expand the ARRAY, click the triangle in front of the tag. Note that you cannot expand ARRAYs with more than 10,000 elements for reasons of clarity.

#### Entering start values of ARRAY elements

To set default start values for the individual elements of an ARRAY, follow these steps:

1. Click the triangle in front of the ARRAY data type tags.

   The ARRAY is expanded and the individual ARRAY elements are shown in separate lines.
2. Enter the required values in the "Start value" column.

#### Adding comments for ARRAYs

To add a comment for the entire ARRAY, enter the comment in the top line of the ARRAY declaration. The comment is used as a preset comment for all lower-level ARRAY elements.

To provide specific comments for the individual elements of an ARRAY, follow these steps:

1. Click the triangle in front of the ARRAY data type tags.

   The ARRAY is expanded and the individual ARRAY elements are shown in separate lines.
2. Enter the desired values in the "Comment" column.

#### Displaying ARRAYs in expanded mode

In "Expanded mode" all ARRAYs are displayed expanded by default.

To enable the expanded mode, follow these steps:

1. Click the "Expanded mode" button in the toolbar.

> **Note**
>
> **Restriction in "Expanded mode" display**
>
> Depending on the amount of RAM available on your computer, the following maximum limits apply to expanded mode:
>
> - RAM < 8 GB: A maximum of 10,000 rows are displayed.
> - RAM >= 8 GB: A maximum of 40,000 rows are displayed.

---

**See also**

[Defining start values](#defining-start-values)
  
[Setting retentivity](#setting-retentivity)
  
[Editing the declaration table for data blocks](#editing-the-declaration-table-for-data-blocks)
  
[ARRAY](Data%20types.md#array)
  
[Using autocompletion](Program%20editor.md#using-autocompletion)

### Declaring tags of STRUCT data type

#### Requirement

A global data block is open.

#### Procedure

To declare a tag of the STRUCT data type, follow these steps:

1. Enter a tag name in the "Name" column.
2. Enter "Struct" in the "Data type" column. You will be supported by autocompletion during input.

   An empty, indented row is inserted after the new tag.
3. Insert the first structural element in the first empty row.

   An additional empty row is inserted after the element.
4. Select a data type for the structure element.
5. Optional: Change the properties of the structural element that is displayed in the other columns of the block interface.
6. Repeat the step 4 to 7 for all additional structure elements.

   It is not necessary to end the structure explicitly. The structure ends with the last element that is entered.
7. To insert a new tag after the structure, leave a blank row after the end of the structure and then start the new tag in the second empty row.

#### Result

The tag of STRUCT data type is created.

#### Enter start values of structure elements

To set default start values for the individual elements of a structure, follow these steps:

1. Click the triangle in front of the STRUCT data type tags.

   The structure opens and the individual structure elements are shown in separate rows.

   Note that, for reasons of clarity, you cannot expand very large structures.
2. Enter the required values in the "Start value" column.

> **Note**
>
> **S7-1200/S7-1500: A maximum of 252 structures (STRUCT) in one data block**
>
> A maximum of 252 structures (STRUCT) are permitted in one block in CPUs of the S7-1200/S7-1500 series. If you need more structures, use PLC data types (UDT) instead of the "STRUCT" data type.

---

**See also**

[Basic information on STRUCT](Data%20types.md#basic-information-on-struct)
  
[Defining start values](#defining-start-values)
  
[Setting retentivity](#setting-retentivity)
  
[Editing the declaration table for data blocks](#editing-the-declaration-table-for-data-blocks)
  
[Using autocompletion](Program%20editor.md#using-autocompletion)

### Declaring tags of the STRING data type

#### Requirement

A global data block is open.

#### Procedure

To declare a tag of STRING data type, proceed as follows:

1. Select the appropriate declaration section in the interface.
2. Enter a tag name in the "Name" column.
3. Enter "STRING" in the "Data type" column. You will be supported by autocompletion during input.
4. Optional: Specify the maximum length of the string using square brackets after the keyword STRING. If you do not specify a maximum length, the string has a default length of 254 characters.

   Example of a STRING with the maximum length of 4:

   `STRING[4]`

   Example of a string whose maximum length is defined by a local constant:

   `STRING[#My_local_const1]`

   Example of a STRING whose maximum length is defined by a global constant:

   `STRING["My_global_const1"]`

#### Result

The tag of STRING data type is created.

### Declaring tags based on a PLC data type

#### Requirement

- A global data block is open.
- A PLC data type is declared in the current CPU.

#### Procedure

To declare a tag based on a PLC data type, follow these steps:

1. Enter a tag name in the "Name" column.
2. Enter the PLC data type in the "Data type" column. You will be supported by Autocomplete during input.
3. The tag is created.
4. Optional: Change the properties of the tags that are displayed in the other columns of the table.

   If you have already defined default values or comments for the tags within a PLC data type during declaration of the PLC data type, these are shown in gray. You can change these values in the block interface.

   The changed values are displayed in black and apply only to the specific point of use.

> **Note**
>
> If you change or delete PLC data types that are being used in the data block, the data block becomes inconsistent. To eliminate this inconsistency, you must recompile the program.

---

**See also**

[Overview of the block interface](Declaring%20the%20block%20interface.md#overview-of-the-block-interface)
  
[Editing the declaration table for data blocks](#editing-the-declaration-table-for-data-blocks)
  
[Using autocompletion](Program%20editor.md#using-autocompletion)

## Defining start values

This section contains information on the following topics:

- [Basic information on start values](#basic-information-on-start-values)
- [Defining start values](#defining-start-values-1)

### Basic information on start values

#### Definition of "Start value"

The start value of a tag is a value defined by you which the tag assumes after a CPU startup.

The retentive tags have a special status. Their values are retained during startup and are not reset to the start value.

An exception is a cold restart of the S7-400: During the cold restart, all data are reset to the initial values - regardless of whether they were configured as retentive or non-retentive.

#### Definition of "Default value"

The structure of the data blocks can be derived from higher-level elements.

- An instance data block is based, for example, on the interface of a higher-level code block.
- A global data block can be based on a predefined PLC data type.

In this case you can define a default value for each tag in the higher-level element. These default values are used as start values during the creation of the data block. You can then replace these values with instance-specific start values in the data block.

Specification of an start value is optional. If you do not specify any value, the tag assumes the default value at startup. If a default is not defined either, the default value valid for the data type is used. For example, the value "FALSE" is specified as standard for BOOL.

---

**See also**

[Defining start values](#defining-start-values-1)
  
[Structure of the declaration table for data blocks](#structure-of-the-declaration-table-for-data-blocks)
  
[Declaring local tags and constants in the block interface](Declaring%20the%20block%20interface.md#declaring-local-tags-and-constants-in-the-block-interface)
  
[Applying values from the online program as start values](#applying-values-from-the-online-program-as-start-values)

### Defining start values

#### Defining start values

To define the start values for the tags of a data block, follow these steps:

1. Open the data block.

   The "Default value" column shows the default values that were defined for the tags in the interface of a higher-level code block or in a PLC data type.
2. Click the "Expanded mode" button to show all elements of structured data types.
3. Enter the desired start values in the "Start value" column. The value must match the data type of the tag and should not exceed the range of the data type.

   The start values are defined. The tag takes the defined value at startup, provided it was not declared as retentive.

#### Resetting a tag to the default value

To reset a tag for which you have defined a start value to the default value, follow these steps:

1. Select a modified value in the table.
2. Delete the value.

   The default value is entered. The default value is displayed.

#### Resetting all tags to the default value

To reset to the default value all tags for which you have defined an start value, follow these steps:

1. Select the "Reset start values" icon in the toolbar.

   The default values are transferred to the "Start value" column. Write-protected start values are not overwritten.

---

**See also**

[Basic information on start values](#basic-information-on-start-values)
  
[Applying values from the online program as start values](#applying-values-from-the-online-program-as-start-values)
  
[Editing the declaration table for data blocks](#editing-the-declaration-table-for-data-blocks)

## Setting retentivity

This section contains information on the following topics:

- [Retentivity of tags in data blocks](#retentivity-of-tags-in-data-blocks)
- [Setting retentivity in an instance data block](#setting-retentivity-in-an-instance-data-block)
- [Setting retentivity in a global data block](#setting-retentivity-in-a-global-data-block)

### Retentivity of tags in data blocks

#### Retentive behavior

To prevent data loss in the event of power failure, you can mark the data as retentive. This data is stored in a retentive memory area. The options for setting the retentivity depend on the type of data block and the type of block access that is set.

---

**See also**

[Setting retentivity in an instance data block](#setting-retentivity-in-an-instance-data-block)
  
[Setting retentivity in a global data block](#setting-retentivity-in-a-global-data-block)

### Setting retentivity in an instance data block

#### Introduction

In an instance data block, the editability of the retentive behavior depends on the type of access of the higher-level function block:

- Function block with standard access

  You can define the instance data both as retentive or non-retentive. Individual retentivity settings are not possible for individual tags.
- Function block with optimized access

  In the instance data block, you can define the retentivity settings of the tags that are selected in the block interface with "Set in IDB". With these tags also, you cannot individually set the retentive behavior for each tag. The retentivity setting has an impact on all tags that are selected in the block interface with "Set in IDB".

#### Setting Retentivity for Standard Access

To centrally set the retentivity of all tags in the data block with standard access, follow these steps:

1. Open the instance data block.
2. Select the check box in the "Retain" column of a tag.

   All tags are defined as retentive.
3. To reset the retentivity setting for all tags, clear the check box in the "Retain" column of a tag.

   All tags will be defined as non-retentive.

#### Setting Retentivity for Optimized Access

To set the retentive behavior of the tags that are selected with "Set in IDB" in data blocks with optimized access, follow these steps:

1. Open the instance data block.
2. Select the check box in the "Retain" column of a tag.

   All tags selected with "Set in IDB" in the data block interface are defined as retentive.
3. To reset the retentivity setting for the tags, clear the check box in the "Retain" column of a tag.

   All tags selected with "Set in IDB" in the data block interface will be defined as non-retentive.

---

**See also**

[Basics of block access](Programming%20basics.md#basics-of-block-access)
  
[Retentivity of tags in data blocks](#retentivity-of-tags-in-data-blocks)
  
[Editing the declaration table for data blocks](#editing-the-declaration-table-for-data-blocks)

### Setting retentivity in a global data block

#### Introduction

In a global data block, the editability of the retentive behavior depends on the type of access:

- Global data block with standard access

  You can define the data both as retentive or non-retentive. Individual retentivity settings are not possible for individual tags.
- Global data block with optimized access

  You can individually define the retentivity settings of the tags. For tags with structured data types, retentivity settings are transferred for all tag elements.

> **Note**
>
> **Retentivity of ARRAY data blocks**
>
> ARRAY data blocks and their components cannot be set retentively.

#### Setting Retentivity for Standard Access

To centrally set the retentivity of all tags in the data block with standard access, follow these steps:

1. Open the global data block.
2. Select the check box in the "Retain" column of a tag.

   All tags are defined as retentive.
3. To reset the retentivity setting for all tags, clear the check box in the "Retain" column of a tag.

   All tags are defined as non-retentive.

#### Setting Retentivity for Optimized Access

To individually set the retentivity of all tags in data blocks with optimized access, follow these steps:

1. Open the global data block.
2. In the "Retain" column, select the check box for the tags for which you want to set a retentive behavior.

   The selected tag is defined as retentive.
3. To reset the retentivity setting for the tags, clear the check box in the "Retain" column of a tag.

   All selected tags are defined as non-retentive.

---

**See also**

[Basics of block access](Programming%20basics.md#basics-of-block-access)
  
[Retentivity of tags in data blocks](#retentivity-of-tags-in-data-blocks)
  
[Editing the declaration table for data blocks](#editing-the-declaration-table-for-data-blocks)

## Editing the properties of tags in data blocks

This section contains information on the following topics:

- [Properties of the tags in data blocks](#properties-of-the-tags-in-data-blocks)
- [Changing the properties of tags in instance data blocks](#changing-the-properties-of-tags-in-instance-data-blocks)
- [Changing the properties of tags in global data blocks](#changing-the-properties-of-tags-in-global-data-blocks)
- [Editing multilingual comments in the data block (S7-1500)](#editing-multilingual-comments-in-the-data-block-s7-1500)

### Properties of the tags in data blocks

#### Properties

The properties of a tag are displayed in the Inspector window when you select the tag in the declaration table or at a point of use in the program editor.

> **Note**
>
> **Properties of ARRAY elements**
>
> When you use ARRAY accesses with variable index in the form `#Program_Alarm_1[#myIndex]` in your program, the specific ARRAY element to be used during runtime is not yet known at the time of programming. For this reason, when you select this type of ARRAY access in the program editor, the properties of the first ARRAY element are always displayed.

The following table provides an overview of the properties of tags in data blocks:

| Group | Property | Description |
| --- | --- | --- |
| General | Name | Name of the tags. |
| Data type | Data type of the tags. |  |
| Default value | Default value of the tag in the interface of a higher-level code block or in a PLC data type.   The values contained in the "Default value" column can only be changed in the higher-level code block or PLC data type. The values are only displayed in the data block. |  |
| Start value | Value that the tag should assume at CPU startup.  The default values defined in a code block are used as start values during the creation of the data block. You can then replace these adopted values with instance-specific start values.   Specification of an start value is optional. If you do not specify any value, the tag assumes the default value at startup. If a default is not defined either, the default value valid for the data type is used. For example, the value "FALSE" is specified as default value for BOOL. |  |
| Comment | Comment on the tag. |  |
| Attributes | Retain | Marks the tag as retentive.   The values of retentive tags are retained even after the power supply is switched off.   This attribute is only available in the interface of the function block with optimized access. |
| Visible in HMI engineering | Shows whether the tag is visible by default in the HMI selection list. |  |
| Writable from HMI/OPC UA/Web API | Indicates whether or not the tag can be written from HMI/OPC UA/Web API during runtime. |  |
| Accessible from HMI/OPC UA/Web API | Indicates whether HMI/OPC UA/Web API can access this variable during runtime.  Note, however, that you cannot implement general access protection for the tag with the "Accessible from HMI/OPC UA/Web API" attribute. Read or write access from other applications is possible even if the attribute is not enabled. |  |
| Visibility in block calls in LAD/FBD | Show:  The parameter is always visible at block calls in LAD or FBD. |  |
| Hide:  The parameter is always hidden at block calls in LAD or FBD. The instruction box then has a small arrow on the lower edge. You can have the parameters displayed and interconnect them by clicking this arrow. |  |  |
| Hide if no parameter is assigned:  The parameter is always hidden at block calls in LAD or FBD as long as it has not yet been interconnected. If you assign an actual parameter, the parameter is displayed at the call box. |  |  |
| Predefined actual parameter | Defines a parameter that is to be used as actual parameter during the block call. |  |
| Show if parameter assigned on block call is not identical to the predefined actual parameter | The parameter is hidden at block calls in LAD or FBD as long as the predefined actual parameter has not yet been assigned. However, when a different parameter is assigned, the parameter becomes visible.     This option is only active if you have selected the "Hide" parameter and have defined a predefined actual parameter. |  |
| User-defined attributes | CFC_Visible | Visible  Indicates whether a parameter is visible in CFC. |
| CFC_Configurable | Configurable  Indicates whether a parameter is configurable in CFC. |  |
| CFC_ForTest | For test  Indicates whether a parameter is registered for the CFC test mode. |  |
| CFC_Interconnectable | Interconnectable  Indicates whether a parameter is interconnectable in CFC. |  |
| CFC_EnableTagReadback | Enable tag readback  Indicates whether a parameter is relevant for the "Read back chart" function in CFC. |  |
| CFC_EnumerationTexts | Enumeration texts  The attribute is only used internally. |  |
| CFC_EngineeringUnit | Engineering unit  Assigns a parameter to a unit in CFC. |  |
| CFC_LowLimit | Low limit  Defines the low limit for the parameter in CFC. |  |
| CFC_HighLimit | High limit  Defines the high limit for the parameter in CFC. |  |

---

**See also**

[Changing the properties of tags in instance data blocks](#changing-the-properties-of-tags-in-instance-data-blocks)
  
[Changing the properties of tags in global data blocks](#changing-the-properties-of-tags-in-global-data-blocks)
  
[Setting retentivity](#setting-retentivity)
  
[Defining start values](#defining-start-values)

### Changing the properties of tags in instance data blocks

#### Instance-specific tag properties

Two options are available for defining the tag properties:

- The tag properties are applied from the interface of the assigned function block.

  Properties that are applied from the function block are displayed grayed out out in the columns of the declaration table. The "Name" and "Data type" properties are always applied.
- You define instance-specific properties.

  You can change some properties instance specific. For example, the comment is a changeable value. Properties that were changed instance specific are not grayed out in the columns of the declaration table. The instance-specific changes are retained, even if the interface of the higher-level function block is changed and the instance data blocks are subsequently updated.

#### Editing properties of an element in the declaration table

To edit the properties of an element, follow these steps:

1. Open the instance data block.
2. Select the required element in the table.
3. Change the entries in the columns.

#### Editing properties of several elements in the declaration table

You can also simultaneously set or reset some properties for multiple selected elements.

To change one of these properties for several elements, follow these steps:

1. Open the data block.
2. Hold down the CTRL key.
3. In the required column, select each of the table cells whose value you want to change.
4. Select the "Set <property>" or "Reset <property>" command in the shortcut menu.

#### Editing properties in the properties window

To edit the properties of an individual tag, follow these steps:

1. Select a tag in the table.
2. Select the "Properties" command in the shortcut menu.

   The properties window opens. It shows the properties of the tag in the "General" and "Attributes" areas.
3. Select the required area in the area navigation.
4. Change the entries in the text boxes.

#### Reset individual properties to the default value.

To reset individual tag properties to the value that was defined as default in the function block, follow these steps:

1. Select an instance-specific, modified value in the table.
2. Delete the value.

   The instance-specific value will be deleted and the default value from the interface of the function block entered. The default value is displayed grayed out.

---

**See also**

[Updating data blocks](#updating-data-blocks)
  
[Properties of the tags in data blocks](#properties-of-the-tags-in-data-blocks)
  
[Editing the declaration table for data blocks](#editing-the-declaration-table-for-data-blocks)

### Changing the properties of tags in global data blocks

#### Introduction

Two options are available for defining the tag properties:

- The tag properties are applied from the PLC data type.

  Properties that are applied from the PLC data type are shown grayed out in the columns of the declaration table. The "Name" and "Data type" properties are always applied.
- You define specific properties.

  You can change some properties in the global data block. Changeable values are, for example, "Comment" or "Visible in HMI". Properties that were changed are not grayed out in the columns of the declaration table. The changes are retained, even if the PLC data type changes and the global data block is subsequently updated.

#### Editing properties of an element in the declaration table

To edit the properties of an element, follow these steps:

1. Open the global data block.
2. Select the required element in the table.
3. Change the entries in the columns.

#### Editing properties of several elements in the declaration table

You can also simultaneously set or reset some properties for multiple selected elements.

To change one of these properties for several elements, follow these steps:

1. Open the data block.
2. Hold down the CTRL key.
3. In the required column, select each of the table cells whose value you want to change.
4. Select the "Set <property>" or "Reset <property>" command in the shortcut menu.

#### Editing properties in the properties window

To edit the properties of an individual tag, follow these steps:

1. Select a tag in the table.
2. Select the "Properties" command in the shortcut menu.

   The properties window opens. It shows the properties of the tag in the "General" and "Attributes" areas.
3. Select the required area in the area navigation.
4. Change the entries in the text boxes.

#### Reset individual properties to the default value.

To reset individual tag properties to the value that was defined as default in the PLC data type, follow these steps:

1. Select a modified value in the table.
2. Delete the value.

   The default value from the PLC data type is entered. The default value is displayed grayed out.

---

**See also**

[Properties of the tags in data blocks](#properties-of-the-tags-in-data-blocks)
  
[Editing the declaration table for data blocks](#editing-the-declaration-table-for-data-blocks)

### Editing multilingual comments in the data block (S7-1500)

You can edit the comments from a data block in all project languages that you have activated in the project language settings. You can find additional information on activating project languages under [Select project languages](Editing%20project%20data.md#select-project-languages).

Note that the texts must not exceed a length of 32767 Unicode characters even after translation.

#### Requirement

- You have activated multiple project languages.
- The data block is open and it contains at least one comment.
- The block does not have know-how protection.

#### Procedure

To edit a comment in all project languages, follow these steps:

1. Click on the comment whose translation you want to edit.

   If you want to edit the translations of several comments at the same time, select all the desired comments.

   In instance data blocks, you can select only comments you have changed on an instance-specific basis. You can identify these comments by the fact that they are not grayed out. You can only select and edit grayed-out comments in the associated function block.
2. Open the "Properties" tab in the Inspector window.
3. Open the "Texts" tab.

   The "Texts" tab displays the selected comments in the active project languages and, if available, the translations of the comments.
4. You can edit the translations directly in the table in the "Texts" tab.
5. To edit the translations with an external editor, you can export the displayed texts to OOXML format using the "Export/Import project texts" buttons.

> **Note**
>
> **Editing all project texts in the global "Project texts" table**
>
> You can also edit the translations for the individual project languages in the global "Project texts" table. You can find the table in the project tree under "Languages & Resources > Project texts". It contains all translatable texts of the entire project.
>
> You can find additional information on translation of texts under [Project text basics](Editing%20project%20data.md#project-text-basics).​

## Editing the declaration table for data blocks

This section contains information on the following topics:

- [Inserting table rows](#inserting-table-rows)
- [Inserting table rows](#inserting-table-rows-1)
- [Deleting tags](#deleting-tags)
- [Automatically filling in successive cells](#automatically-filling-in-successive-cells)
- [Navigate to definitions](#navigate-to-definitions)
- [Show and hide table columns](#show-and-hide-table-columns)
- [Editing tags with external editors](#editing-tags-with-external-editors)

### Inserting table rows

#### Procedure

Proceed as follows to insert a row above the selected row:

1. Select the row in front of which you want to insert a new row.
2. Click the "Insert row" button on the toolbar of the table.

#### Result

A new row is inserted above the selected row.

---

**See also**

[Editing tables](Introduction%20to%20the%20TIA%20Portal.md#editing-tables)

### Inserting table rows

#### Procedure

Proceed as follows to insert a row below the selected row:

1. Select the row below which you want to insert a new row.
2. Click the "Add row" button on the table toolbar.

#### Result

A new empty row will be inserted below the selected row.

---

**See also**

[Editing tables](Introduction%20to%20the%20TIA%20Portal.md#editing-tables)

### Deleting tags

#### Requirements

A global data block is open.

#### Procedure

To delete a tag, follow these steps:

1. Select the row with the tag to be deleted. You can also select several rows by clicking on them one after the other while holding down the <Ctrl> key or by pressing and holding down <Shift> and clicking on the first and last row.
2. Select the "Delete" command in the shortcut menu.

> **Note**
>
> You cannot directly change the structure of instance data blocks and of global data blocks based on a PLC data type, since the structures of these blocks are defined in the higher-level object.
>
> The type of the data block is entered in the block properties.
>
> See also: [Displaying and editing block properties](Creating%20and%20managing%20blocks.md#displaying-and-editing-block-properties)

---

**See also**

[Editing tables](Introduction%20to%20the%20TIA%20Portal.md#editing-tables)

### Automatically filling in successive cells

You can load the contents of one or several table cells into the cells below, automatically filling in the successive cells.

If you automatically fill in cells in the "Name" column, a consecutive number will be appended to each name. For example, "Motor" will become "Motor_1".

You can define individual or more cells as well as entire rows as source area.

If less rows exist in the open table than you want to fill, then you will first have to insert additional empty rows.

#### Requirement

- The table is open.
- Sufficient declaration rows are available.

#### Procedure

To automatically fill in successive cells, follow these steps:

1. Select the cells to be loaded.
2. Click the "Fill" symbol in the bottom right corner of the cell.

   The mouse pointer is transformed into a crosshair.
3. Keep the mouse button pressed and drag the mouse pointer downwards over the cells that you want to fill in automatically.
4. Release the mouse button.

   The cells are filled in automatically.
5. If entries are already present in the cells that are to be automatically filled in, a dialog appears. In this dialog you can indicate whether you want to overwrite the existing entries or insert new rows for the new tags.

### Navigate to definitions

You can use PLC data types (UDT) in a data block or create an entire data block based on a PLC data type. To view the definition of the PLC data type, you can specifically navigate to the location of the definition.

#### Procedure

To navigate to the definition of a PLC data type, follow these steps:

1. Right-click a data block element that is based on a PLC data type.

   or

   Click the "Static" entry of a data block that is based on a PLC data type.
2. Select the shortcut menu command "Go to definition".

#### Result

The declaration table in which the PLC data type was defined opens and the declaration is displayed.

### Show and hide table columns

You can show or hide the columns in a table as needed.

#### Procedure

To show or hide table columns, follow these steps:

1. Click a column header.
2. Select the "Show/Hide" command in the shortcut menu.

   The selection of available columns is displayed.
3. To show a column, select the column's check box.
4. To hide a column, clear the column's check box.
5. To hide or show several columns, click "More" and activate or deactivate the check box of the corresponding columns in the "Show/Hide" dialog.

### Editing tags with external editors

To edit individual tags in external table editors, such as Excel, you can export or import these tags using copy and paste.

> **Note**
>
> **Restriction when displaying and copying ARRAY elements**
>
> Depending on the amount of work memory available on your computer, the following maximum limits apply when displaying and copying ARRAYs from the data block editor in an Excel table:
>
> - RAM < 8 GB: A maximum of 10,000 elements are displayed and copied.
> - RAM >= 8 GB: A maximum of 40,000 elements are displayed and copied.

#### Requirement

The data block and an external editor are opened.

#### Procedure

To export and re-import individual tags by drag-and-drop operation, follow these steps:

1. Click the "Expanded mode" button to show all elements of structured data types.
2. Select one or more tags.
3. Select "Copy" in the shortcut menu.
4. Switch to the external editor and paste the copied tags.
5. Edit the tags as required.
6. Copy the tags in the external editor.
7. Switch back to the declaration table.
8. Select "Paste" in the shortcut menu.

## Online and diagnostic functions for data blocks

This section contains information on the following topics:

- [Editing data blocks in online mode](#editing-data-blocks-in-online-mode)
- [Overview of the online and diagnostic functions in data blocks](#overview-of-the-online-and-diagnostic-functions-in-data-blocks)
- [Monitoring tags](#monitoring-tags)
- [Modifying tags](#modifying-tags)
- [Loading start values as actual values](#loading-start-values-as-actual-values)
- [Creating a snapshot of the actual values](#creating-a-snapshot-of-the-actual-values)
- [Loading snapshots as actual values](#loading-snapshots-as-actual-values)
- [Copying the snapshot to the start values](#copying-the-snapshot-to-the-start-values)
- [Using setpoints during commissioning](#using-setpoints-during-commissioning)

### Editing data blocks in online mode

#### Introduction

When you load a data block to the CPU, there are two versions of the block:

- An offline version in the project on your programming device
- An online version on the CPU

  Data blocks can either be located only in the load memory, only in the work memory or in both memory areas.

#### Start values and actual values of tags

The values of the tags in the offline and online version of a data block are different because the tags in the online block can be changed by the user program during runtime.

When you declare a data block, you assign a start value to the tags. The start value is the value of the tag when the data block is called for the first time. This means the tag is "initialized" with the start value.

The start values of the tag are declared in the offline version of the block. When the data block is loaded to the CPU, it is transferred to the load memory with the start values. From there, the data block is loaded to the work memory of the CPU. When the block is loaded for the first time, the tags in the work memory are initialized with the declared start values. They can now be changed with the user program. The values of the tags in the work memory are referred to as "actual values".

#### Loading changed data blocks

When you make changes to a data block after initial loading, you are editing the offline version of the block. Depending on the existing conditions, subsequent loading of the data block has different effects on the actual values.

- Loading changes in "RUN":

  - If you have not made any changes to the structure of the data block, the actual values of all tags are retained. The program is processed further "bumplessly" Any changes to the start values in the offline data block are written to the load memory. They are not transferred to the CPU until the next transition from "STOP" to "RUN".
  - If you have changed the structure of the data block, all tags are reinitialized with their start values. Initializing the tags may have unwanted effects on the process because the process and the program may not be synchronous any longer.   
    You can prevent this by using the memory reserve of the block. The memory reserve enables you to load data blocks in "RUN" without reinitialization. This means you can reload "bumplessly" even if you have changed the structure of the data block and have added new tags, for example.

    See also: [Basic information on loading block extensions without reinitialization](Loading%20block%20extensions%20without%20reinitialization%20%28S7-1200%2C%20S7-1500%29.md#basic-information-on-loading-block-extensions-without-reinitialization-s7-1200-s7-1500)
- Loading changes in "STOP":

  - The start values of non-retentive tags are placed in the load memory of the CPU. The program runs with the new start values at the next transition from "STOP" to "RUN".
  - Retentive tags are not reinitialized. Your actual values are retained after loading in "STOP".

    To also reinitialize the retentive tags when loading in "STOP", select the blocks you want to load in the project tree and select the command "Compile > Software (rebuild all blocks)" in the shortcut menu. In the "Online" menu, select the command "Download and reset PLC program". The online blocks are deleted and overwritten by the new blocks. This reinitializes all tags, including the retentive tags.

#### Editing actual values with online and diagnostic functions

To manipulate actual values directly in online mode without having to reload data blocks, you can use the online and diagnostic functions of the TIA Portal.

See also: [Overview of the online and diagnostic functions in data blocks](#overview-of-the-online-and-diagnostic-functions-in-data-blocks)

#### Loading data blocks from a device

You can also load data blocks from a device again. This makes sense, for example, if the original offline project is not available during servicing. Please note that the two CPU families handle the values of tags differently when loading blocks from a device:

- S7-1200/1500

  CPUs of the S7-1200 and S7-1500 series store the start values with which a data block is loaded to the CPU in the load memory. If you load a data block from an S7-1200/1500 CPU, these start values are applied from the load memory to the offline data block again. Even if you have made value changes in the load memory during runtime by means of the "WRIT_DBL" instruction, the values originally loaded to the device are applied to the offline data block.
- S7-300/400

  CPUs of the S7-300/400 series also store the start values with which a data block is loaded to the CPU in the load memory. However, they cannot read the values back from the load memory. If you load a data block from a device, the current monitored values are loaded from the CPU and entered in the "Start values" column in the offline data block.

---

**See also**

[Downloading blocks for S7-1200/1500 (S7-1200, S7-1500)](Compiling%20and%20downloading%20PLC%20programs.md#downloading-blocks-for-s7-12001500-s7-1200-s7-1500)

### Overview of the online and diagnostic functions in data blocks

#### Overview of functions

The data block editor offers different options for editing data blocks in online mode. These functions directly access the actual values of the tags in the online program. Actual values are the values which the tags have at the current time during program execution in the CPU work memory.

The following table provides an overview of the online and diagnostic functions. Detailed descriptions of the individual functions can be found in the following chapters.

| Button | Function | Description | S7-300/400 | S7-1200/1500 |
| --- | --- | --- | --- | --- |
| ![Overview of functions](images/85425601163_DV_resource.Stream@PNG-de-DE.png) | [Monitor tags online](#monitoring-tags) | Displays the actual values which the tags currently have in the CPU. | X | X |
| - | [Modify individual actual values](#modifying-tags) | Modifies individual tags immediately and once only to specific values in the declaration table. The CPU then uses these values as actual values in the online program. | X | X |
| ![Overview of functions](images/89437974539_DV_resource.Stream@PNG-de-DE.png) | [Create a snapshot of the actual values](#creating-a-snapshot-of-the-actual-values) | Saves the actual values present at the current time as snapshot in the offline project. The snapshot always captures the actual values of all tags of the data block. | X | X |
| ![Overview of functions](images/89437978251_DV_resource.Stream@PNG-de-DE.png) | [Reinitialize actual values with a snapshot](#loading-snapshots-as-actual-values) | Loads the snapshot to the CPU as actual values. The CPU then uses these values as actual values in the online program. | - | S7-1200 V4.1 and higher   S7-1500 V1.7 and higher |
| ![Overview of functions](images/85394826635_DV_resource.Stream@PNG-de-DE.png)       ![Overview of functions](images/85394754699_DV_resource.Stream@PNG-de-DE.png) | [Apply snapshot values as start values](#copying-the-snapshot-to-the-start-values) | Copies the snapshot to the start values in the offline program. The program runs with the new start values at the next transition from STOP to RUN.   You can copy all start values or only the start values of the tags identified as "setpoint". | X | X |
| ![Overview of functions](images/89437878027_DV_resource.Stream@PNG-de-DE.png) | [Reinitialize actual values with start values](#loading-start-values-as-actual-values) | Reinitializes the actual values of all tags. The start values are written directly to the CPU work memory. | - | S7-1200 V4.1 and higher   S7-1500 V1.7 and higher |
| ![Overview of functions](images/89437894539_DV_resource.Stream@PNG-de-DE.png) | [Initializing setpoints with start values](#initializing-setpoint-values-in-the-online-program) | Reinitialize the actual values of the tags identified as "setpoints". | X | X |

| Symbol | Meaning |
| --- | --- |
|  | **Danger** |
| **Danger when changing tag values**  Changing of the tag values during plant runtime can result in inconsistencies between the program and the actual process. This can cause serious damage to property and personal injury.  - Make sure that the plant is in a safe state before you overwrite the actual values. - Make sure that snapshots are taken at a time when the system was in a safe state. - Select individual tags as setpoints to selectively edit the actual values of these tags in the online program. - Make sure that the program does not read or write the affected data during transmission. - You may want to use the "Modify tag" function in the watch table or in the DB editor as an alternative. |  |

---

**See also**

[Applying values from the online program as start values](#applying-values-from-the-online-program-as-start-values)
  
[Editing data blocks in online mode](#editing-data-blocks-in-online-mode)
  
[Using setpoints during commissioning](#using-setpoints-during-commissioning)
  
[Defining start values](#defining-start-values)

### Monitoring tags

You can monitor the actual values of the tags in the CPU directly in the declaration table.

#### Requirement

- An online connection is available.
- The data block has been loaded to the CPU.
- The program execution is active (CPU in "RUN").
- The data block is open.

#### Procedure

To monitor the tags, follow these steps:

1. Start monitoring by clicking the "Monitor all" button.

   The additional "Monitor value" column is displayed in the table. This shows the current data values.

   See also: [Structure of the declaration table for data blocks](#structure-of-the-declaration-table-for-data-blocks)
2. End monitoring by clicking the "Monitor all" button again.

---

**See also**

[Overview of the online and diagnostic functions in data blocks](#overview-of-the-online-and-diagnostic-functions-in-data-blocks)

### Modifying tags

You can modify an individual tag in the data block to a specific value. The CPU then uses this value as the actual value in the online program.

| Symbol | Meaning |
| --- | --- |
|  | **Danger** |
| **Danger when changing tag values**  Changing the tag values while the plant is operating can cause serious damage to property or injury to persons if there are functional disturbances or program errors.  Make sure that no dangerous situations can arise before you modify the tags. |  |

#### Requirement

- An online connection to the CPU is available.
- The data block whose tags you wish to modify is identical offline and online.
- The data block is open.

#### Procedure

To modify an individual tag in the data block, follow these steps:

1. Start monitoring by clicking the "Monitor all" button.

   The additional "Monitor value" column is displayed in the table. This shows the current data values.
2. Double-click the tag to be modified.

   - In the case of Boolean tags, the "Toggle value" dialog opens. Confirm this dialog by clicking "OK".

     If you click the option "Do not show this message again" in this dialog, you can toggle the value in the further course of the online session by double-clicking.
   - In the case of non-Boolean tags, the "Modify value" dialog opens. Enter the desired value in the "Modify value" input field and confirm with "OK".

     If there is a snapshot, the value is already entered as default.

#### Result

The tag will have the specified value once when you execute the modify job. The job is executed immediately and is not tied to the next cycle control point.

---

**See also**

[Introduction to modifying tags](Testing%20with%20the%20watch%20table.md#introduction-to-modifying-tags)
  
[Overview of the online and diagnostic functions in data blocks](#overview-of-the-online-and-diagnostic-functions-in-data-blocks)

### Loading start values as actual values

You can load the start values from the offline program to the CPU as actual values. The start values are loaded directly to the CPU work memory. The tags in the online block are reinitialized, and the CPU uses the new values as actual values in the online program. No distinction is made between retentive and non-retentive values. You can copy all actual values or only the actual values of the tags identified as "setpoint".

You can quickly bring the controlled process into a defined state this way.

You cannot reinitialize the following types of data blocks:

- Data blocks that are part of a reference project
- Fail-safe data blocks
- Data blocks generated by the CPU
- Data blocks with the attribute "Only store in load memory"
- Data blocks that only exist online

You can execute this function in "RUN" mode as well as "STOP" mode.

| Symbol | Meaning |
| --- | --- |
|  | **Danger** |
| **Danger when changing tag values**  Changing of the tag values during plant runtime can result in inconsistencies between the program and the actual process. This can cause serious damage to property and personal injury.  If the volume of data to be transmitted is too large, the values may be transmitted in several cycles. If the program accesses tags before all values are completely transmitted, there is a risk that inconsistent value combinations may be created and processed.   Copying the values of elementary data types may also take several cycles. These values are potentially invalid until they have been completely transmitted. Dangerous states may occur if the program accesses these values before they have been completely transmitted.  To prevent dangerous states from occurring, please note the following:  - Make sure that the plant is in a safe state before you overwrite the actual values. - Select individual tags as setpoints to selectively edit the actual values of these tags in the online program. - Make sure that the program does not read or write the affected data during transmission. - You may want to use the "Modify tag" function in the watch table or in the DB editor as an alternative. |  |

#### Requirement

- You are using an S7-1200 V4.1 or higher or an S7-1500 V1.7 or higher.
- An online connection to the CPU is available.
- The data blocks whose actual values you want to reinitialize are identical offline and online.

#### Reinitializing actual values of an open block

To reinitialize all actual values or only the setpoints of a block with start values, follow these steps:

1. Open the data block.
2. Click the "Load start values as actual values > All values" button.

Or:

1. Open the data block.
2. Click the "Load start values as actual values > Only setpoints" button.

#### Reinitializing actual values of multiple blocks

To reinitialize all actual values of multiple blocks in one step, proceed as follows:

1. Select multiple blocks or the entire block folder in the project tree.
2. Select the "Load start values as actual values" command in the shortcut menu.

#### Result

The actual values in the online program are reinitialized with the start values.

The maximum number of tags that can be initialized is dependent on the CPU. If there are too many tags, an alarm informs you about this. In this case, you can insert the tags in a watch table and initialize them using the "Modify" function in the watch table.

---

**See also**

[Overview of the online and diagnostic functions in data blocks](#overview-of-the-online-and-diagnostic-functions-in-data-blocks)

### Creating a snapshot of the actual values

You can save the actual values​ of the tags of one or more data blocks as snapshot. Actual values are the values which the tags have at the current time during program execution in the CPU work memory.

A snapshot cannot be created for data blocks that are stored only in the load memory and are not integrated in the program.

You have the following options for creating a snapshot:

- Create a snapshot of an open data block
- Create a snapshot of several selected data blocks

A snapshot is also created automatically when you download a block or a program from the device.

| Symbol | Meaning |
| --- | --- |
|  | **Caution** |
| **Creating the snapshot**  The values in the snapshot may originate in several cycles. |  |

#### Requirement

- An online connection to the CPU is available.
- The data blocks for which you want to create a snapshot are identical offline and online.

#### Procedure

To create a snapshot of an open data block, follow these steps:

1. Open the data block.
2. Click "Snapshot".

To create a snapshot of several selected data blocks, follow these steps:

1. Select the blocks in the project tree.   
   You can select the blocks individually or select devices, groups or folders in the project tree which include the data blocks.
2. In the shortcut menu, select "Snapshot of the current values" or select the menu command "Online > Snapshot of the current values".

#### Result

- The latest monitored values will be applied in the "Snapshot" column.
- An alarm is shown in the Inspector window after the operation is complete.
- The time stamp of the snapshot is displayed above the declaration table.

> **Note**
>
> **Changes to the data block structure**
>
> If you change the structure of the data block after creation of a snapshot, individual values in the snapshot may become invalid. For example, if you change the data type of a tag, the value of this tag becomes invalid. No value is displayed for this tag in the "Snapshot" column.

---

**See also**

[Overview of the online and diagnostic functions in data blocks](#overview-of-the-online-and-diagnostic-functions-in-data-blocks)

### Loading snapshots as actual values

You can load the snapshots from the offline program to the CPU as actual values. The values from the snapshot are loaded directly to the CPU work memory. The tags in the online block are reinitialized, and the CPU uses the new values as actual values in the online program.

You can quickly bring the controlled process into a defined state this way.

You cannot reinitialize the following types of data blocks with snapshots:

- Data blocks that are part of a reference project
- Fail-safe data blocks
- Data blocks generated by the CPU
- Data blocks with the attribute "Only store in load memory"
- Data blocks that only exist online

| Symbol | Meaning |
| --- | --- |
|  | **Danger** |
| **Danger when changing tag values**  Changing of the tag values during plant runtime can result in inconsistencies between the program and the actual process. This can cause serious damage to property and personal injury.  - Make sure that the plant is in a safe state before you overwrite the actual values. - Make sure that the snapshot is taken at a time when the system was in a safe state. - Select individual tags as setpoints to selectively edit the actual values of these tags in the online program. - Make sure that the program does not read or write the affected data during transmission. - You may want to use the "Modify tag" function in the watch table or in the DB editor as an alternative. |  |

#### Dependencies on the CPU mode

You can execute this function in "RUN" mode as well as "STOP" mode. The table below shows the reactions of the CPU in the different modes:

| Action | System reaction | Consequences for the online program |
| --- | --- | --- |
| Overwrite actual values in "RUN" mode | The values of all DB tags are overwritten in the current program. No distinction is made between retentive and non-retentive values. | Changing the actual values can result in inconsistencies between the program and the actual process.   If the volume of data to be transmitted is too large, the values may be transmitted in several cycles. If the program accesses tags before all values are completely transmitted, there is a risk that inconsistent value combinations may be created and processed.   Copying the values of elementary data types may also take several cycles. These values are potentially invalid until they have been completely transmitted. Dangerous states may occur if the program accesses these values before they have been completely transmitted. |
| Overwrite actual values in "STOP" mode | Only the actual values of the retentive tags are overwritten by the snapshot. Non-retentive tags are initialized with their start values during the transition from "STOP" to "RUN". The values from the snapshot are not taken into consideration. | Because only the retentive data from the snapshot is transmitted, there is a risk that inconsistent value combinations may be created and processed. |

#### Requirement

- You are using an S7-1200 V4.1 or higher or an S7-1500 V1.7 or higher.
- An online connection to the CPU is available.
- The data blocks whose actual values you want to reinitialize are identical offline and online.
- A snapshot of the data blocks has been created.

#### Reinitializing actual values of an open block

To reinitialize all actual values of a block with snapshots, follow these steps:

1. Open the data block.
2. Click "Load snapshots as actual values".

#### Reinitializing actual values of multiple blocks

To reinitialize the actual values of multiple blocks in one step, follow these steps:

1. Select multiple blocks or the entire block folder in the project tree.
2. Select the "Load snapshots as actual values" command in the shortcut menu.

#### Result

The actual values in the online program are reinitialized with the values from the snapshot. Tags for which a valid snapshot does not exist are reinitialized with their start values.

---

**See also**

[Overview of the online and diagnostic functions in data blocks](#overview-of-the-online-and-diagnostic-functions-in-data-blocks)

### Copying the snapshot to the start values

You can copy the snapshot to the start values in the offline program. The program runs with the new start values at the next transition from "STOP" to "RUN".

You can copy all start values, the start values of the retentive tags or only the start values of the tags identified as "setpoint".

Note that the values from the snapshot are always copied. There is no check to determine whether all values originate from the same cycle.

Write-protected start values are not overwritten.

You have the following basic options for applying the values:

- Applying the values of an open data block

  You can apply all values or only the values of the tags marked as "setpoint" as start values in an open data block.
- Applying the values of multiple blocks in the project tree

  You can either apply all values, all setpoints or all retentive values as start values in the project tree.

| Symbol | Meaning |
| --- | --- |
|  | **Danger** |
| **Danger when changing start values**  The changed start values will be used for initialization of the tag values during the next loading process in the online program. Changing of the tag values during plant runtime can result in inconsistencies between the program and the actual process. This can cause serious damage to property and personal injury.  - Make sure that the plant is in a safe state before you overwrite the actual values. - Make sure that the snapshot is taken at a time when the system was in a safe state. - Select individual tags as setpoints to selectively edit the actual values of these tags in the online program. - Make sure that the program does not read or write the affected data during transmission. - You may want to use the "Modify tag" function in the watch table or in the DB editor as an alternative. |  |

#### Requirement

A snapshot has been created for the data block.

#### Procedure

To apply the snapshots as start values in a data block, follow these steps:

1. Open a data block.
2. In the toolbar, click "Copy snapshots to start values > All values".

Or:

1. Open a data block.
2. In the toolbar, click "Copy snapshots to start values > Only setpoints".

To apply the monitored values of multiple data blocks in the project tree, follow these steps:

1. Select the blocks in the project tree.
2. Then select one of the following commands in the shortcut menu:

   - "Copy snapshots to start values > All values"
   - "Copy snapshots to start values > Only setpoints"
   - "Copy snapshots to start values > Only retain values"

#### Result

The values from the "Snapshot" column are applied to the "Start value" column. The new start values are stored in the offline program.

> **Note**
>
> **Applying values of individual tags**
>
> You can also apply the values of individual tags from the "Snapshot" column to the "Start values" column. Use the "Copy" and "Paste" commands from the shortcut menu to copy the values and insert them in the "Start value" column. Note that only the values that are currently located in the visible area of the table are copied.

---

**See also**

[Overview of the online and diagnostic functions in data blocks](#overview-of-the-online-and-diagnostic-functions-in-data-blocks)

### Using setpoints during commissioning

This section contains information on the following topics:

- [Basic information on adjusting setpoints during commissioning](#basic-information-on-adjusting-setpoints-during-commissioning)
- [Marking data as values that can be set](#marking-data-as-values-that-can-be-set)
- [Initializing setpoint values in the online program](#initializing-setpoint-values-in-the-online-program)
- [Applying values from the online program as start values](#applying-values-from-the-online-program-as-start-values)

#### Basic information on adjusting setpoints during commissioning

##### Introduction

During commissioning of a plant, data values have to be frequently adjusted in order to optimally adapt the program to the general operating conditions on site. To this end, you can use the online and diagnostic functions of the declaration table for data blocks.

To use the functions, first define specific tags as "setpoints" in the program. Setpoints are the values that will probably have to be fine-tuned during commissioning.

The following table provides an overview of the functions for tuning values during commissioning. Detailed descriptions of the individual functions can be found in the following chapters.

In addition, there are also the general functions for monitoring and controlling the data block:

[Overview of the online and diagnostic functions in data blocks](#overview-of-the-online-and-diagnostic-functions-in-data-blocks)

| Button | Function | Description |
| --- | --- | --- |
| ![Introduction](images/89437894539_DV_resource.Stream@PNG-de-DE.png) | [Initialize setpoints in "RUN" mode](#initializing-setpoint-values-in-the-online-program) | This function enables you to change the values of individual tags online to quickly determine the optimum tag values. |
| ![Introduction](images/89437974539_DV_resource.Stream@PNG-de-DE.png)     ![Introduction](images/85394754699_DV_resource.Stream@PNG-de-DE.png) | [Apply values from the online program as start values to the offline program](#applying-values-from-the-online-program-as-start-values) | When you have determined the optimum tag values, you can apply these as start values in the offline program. This allows you to ensure that the program starts with the optimized values the next time it is loaded. |

---

**See also**

[Marking data as values that can be set](#marking-data-as-values-that-can-be-set)

#### Marking data as values that can be set

You can mark specific tags in the program as "Setpoints". Setpoints are the values that will probably have to be fine-tuned during commissioning.

##### Rules

You can mark tags as "setpoints" in the following block types:

- In function blocks (FB), but only in the "Static" section
- in global data blocks (DB)
- in PLC data types (UDT)

  In the case of PLC data types, however, the setting is only effective if the UDT is used in the "Static" section of a function block or data block.

It is not possible to define setpoints in the following block types:

- In data blocks based on a PLC data type and in instance data blocks. These inherit the setting from the higher-level FB or UDT.
- You cannot mark tags as "setpoints" in ARRAY data blocks.
- You also cannot mark tags as "setpoints" at the call point of a multi-instance. You have to make the setting in the interface of the function block that is called as multiple instance.
- You cannot change the "setpoint" marking in know-how-protected blocks. To do so, you must first remove the know-how protection.

##### Requirement

A function block, a global data block or a PLC data type (UDT) is open.

##### Procedure

To mark a tag as "setpoint", follow these steps:

1. Select a tag from the "Static" section.
2. Select the check box in the "Setpoint" column.

   - You cannot define the higher-level element of a structure or a PLC data type as "setpoint". You have to make the setting for the lower-level elements individually.
   - In the case of ARRAYs, you can only mark the higher-level element as "setpoint". The lower-level elements inherit the setting.
   - For ARRAYs of STRUCT, you can only mark the elements below the first structure as setpoints. The elements of other structures inherit the setting.

##### Result

The tags are marked as setpoints. During commissioning, these tags can be initialized online. You do not need to set the CPU to "STOP" mode; it can remain in "RUN". In addition, the current tag values can be transferred as start values to the offline program and saved there.

---

**See also**

[Overview of the online and diagnostic functions in data blocks](#overview-of-the-online-and-diagnostic-functions-in-data-blocks)
  
[Online and diagnostic functions for data blocks](#online-and-diagnostic-functions-for-data-blocks)
  
[Defining start values](#defining-start-values)

#### Initializing setpoint values in the online program

##### Basics on initializing setpoints

You can initialize all tags marked as "setpoints" with new values in the online program. At the same time, the start values will be loaded from the offline program to the online program. The CPU remains in "RUN" mode. All tags that are marked as setpoints are initialized once at the next cycle control point. This applies both to retentive and non-retentive tags. The program execution is then continued with the new tag values.

The maximum number of initializable tags is CPU-dependent: For S7-300/400 CPUs, you can initialize up to 35 setpoints. For S7-1200/1500 CPUs, the maximum amount is 200 setpoints. The maximum amount may be less, however, depending on the data types used.

If too many setpoints are selected, an alarm informs you of this. In this case, you can insert the tags in a watch table and initialize them using the "Modify" function in the watch table.

| Symbol | Meaning |
| --- | --- |
|  | **Danger** |
| **Danger when changing tag values**  Changing the tag values while the plant is operating can cause serious damage to property or injury to persons if there are functional disturbances or program errors.  Make sure that no dangerous situations can arise before you reinitialize the setpoints. |  |

##### Requirement

- An online connection to the CPU exists.
- The structure of the data block is identical offline and online.
- One or more tags are marked as "setpoints".

##### Procedure

To initialize all setpoints of the data block, follow these steps:

1. Open a global data block or an instance data block.
2. Enter the required values in the "Start value" column. The start values must correspond to the indicated data type.
3. Click the "Load start values as actual values > Only setpoints" button.

##### Result

The setpoints in the online program are initialized with the start values from the offline program at the next cycle control point.

---

**See also**

[Overview of the online and diagnostic functions in data blocks](#overview-of-the-online-and-diagnostic-functions-in-data-blocks)

#### Applying values from the online program as start values

In order to apply tag values from the online program to the offline program as start values, first create a snapshot of the tag values from the online program. You can then apply them to the offline program. Note that the values from the snapshot are always copied. There is no check to determine whether all values originate from the same cycle.

Write-protected start values are not overwritten.

You have the following basic options for applying the values:

- Applying the setpoints of an open data block
- Applying the setpoints of multiple blocks in the project tree

##### Requirement

- An online connection to the CPU is available.
- As least one data block has been loaded to the CPU.

##### Procedure

To apply all setpoints as start values in a data block, follow these steps:

1. Open the data block.
2. Start monitoring by clicking the "Monitor all" button.

   The "Monitor value" column is displayed in the table. This shows the current data values.
3. In the toolbar, click "Snapshot".

   The actual values are applied in the "Snapshot" column.
4. In the toolbar, click "Copy snapshots to start values > Only setpoints".

The values from the "Snapshot" column are applied to the "Start values" column.

To apply the monitored values of multiple data blocks in the project tree, follow these steps:

1. Select the blocks in the project tree.
2. Select the "Snapshot" command in the shortcut menu.

   The actual values of all selected blocks are applied in the "Snapshot" column.

   An alarm is shown in the Inspector window after the operation is complete.
3. Next, select the command "Copy snapshot values as start values > Only setpoints" in the shortcut menu.

The values from the "Snapshot" column are applied to the "Start value" column.

##### Result

The new start values are stored in the offline program.

> **Note**
>
> **Applying values of individual tags**
>
> You can also apply the values of individual tags that were not marked as setpoints beforehand from the "Snapshot" column to the "Start values" column. Use the "Copy" and "Paste" commands from the shortcut menu to copy the values and insert them in the "Start value" column. Note that only the values that are currently located in the visible area of the table are copied.

---

**See also**

[Basic information on start values](#basic-information-on-start-values)
  
[Defining start values](#defining-start-values-1)
  
[Overview of the online and diagnostic functions in data blocks](#overview-of-the-online-and-diagnostic-functions-in-data-blocks)
  
[Online and diagnostic functions for data blocks](#online-and-diagnostic-functions-for-data-blocks)

---
title: "Displaying program information"
package: ProgRef2MenUS
topics: 34
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Displaying program information

This section contains information on the following topics:

- [Overview of available program information](#overview-of-available-program-information)
- [Displaying an assignment list](#displaying-an-assignment-list)
- [Displaying the call structure](#displaying-the-call-structure)
- [Displaying the dependency structure](#displaying-the-dependency-structure)
- [Displaying CPU resources](#displaying-cpu-resources)

## Overview of available program information

### Program information

The program information of a user program contains the view specified in the following table.

| View | Application |
| --- | --- |
| [Assignment list](#introduction-to-the-assignment-list) | Provides an overview of the address bits for the I, Q, and M memory areas already allocated within the user program.  Also indicates if an address has been allocated by access from an S7 program or if the address has been assigned to a SIMATIC S7 module. |
| [Call structure](#introduction-to-the-call-structure) | Shows the call structure of the blocks within the user program and provides an overview of the blocks used and their relationships. |
| [Dependency structure](#introduction-to-the-dependency-structure) | Shows the list of blocks used in the user program. A block is shown at the first level and blocks that call or use this block are indented below it. In contrast to the call structure, instance blocks are listed separately. |
| [Resources](#introducing-resources) | Shows the hardware resources of the CPU for objects (OB, FC, FB, DB, user-defined data types and PLC tags), for CPU memory areas and for the existing I/O modules. |

### Displaying several views simultaneously

You can generate and display several views for one or more user programs to facilitate testing and changing your user program.

Displaying multiple views, for example, enables you to:

- Display all program information for a user program next to one another
- Compare different user programs

## Displaying an assignment list

This section contains information on the following topics:

- [Introduction to the assignment list](#introduction-to-the-assignment-list)
- [Layout of the assignment list](#layout-of-the-assignment-list)
- [Symbols in the assignment list](#symbols-in-the-assignment-list)
- [Displaying an assignment list](#displaying-an-assignment-list-1)
- [Setting the view options for the assignment list](#setting-the-view-options-for-the-assignment-list)
- [Filter options in the assignment list](#filter-options-in-the-assignment-list)
- [Defining filters for assignment list](#defining-filters-for-assignment-list)
- [Filtering an assignment list](#filtering-an-assignment-list)
- [Defining retentive memory areas for bit memories](#defining-retentive-memory-areas-for-bit-memories)
- [Enabling the display of retentive bit memories](#enabling-the-display-of-retentive-bit-memories)

### Introduction to the assignment list

#### Program information in the assignment list

The assignment list shows if an address has been allocated by access from an S7 program or if the address has been assigned to a SIMATIC S7 module. It is therefore an important basis for locating errors or changes in the user program.

In the assignment list, you have a CPU-specific overview of which bit is used in which byte of the memory areas listed below:

- Input (I)
- Output (O)
- Bit memory (M)
- Timer (T)
- Counter (C)
- I/O (P)

#### Display of the assignment list

The assignment list of inputs, outputs, and bit memory is displayed in several separate work windows.

#### Filters

You can filter the display within the assignment list. You can use predefined filters or create your own.

#### Displaying cross-reference information

You have the option of displaying cross-reference information for selected addresses in the assignment list.

You can display the cross-references for a selected address in the Inspector window using the "Cross-reference information" shortcut menu command. The command "Tools &gt; Cross-references" allows you to also open the cross-reference list for the selected object.

#### Displaying the PLC tag table

You can open the PLC tag table from the assignment list and edit the properties of the tags used.

To do this select an address of the assignment list and select the "Open editor" command in the shortcut menu.

#### Enabling the display of retentivity

You can enable and disable the display of the retentive state of bit memory by selecting the "Hide/show retain area" toolbar button.

---

**See also**

[Symbols in the assignment list](#symbols-in-the-assignment-list)
  
[Layout of the assignment list](#layout-of-the-assignment-list)

### Layout of the assignment list

#### Layout of the assignment list

Depending on the CPU, the [assignment list](#) (The assignment list shows if an address has been allocated by access from an S7 program or if the address has been assigned to a SIMATIC S7 module. The assignment list gives you an overview of which bit in a byte is used for the memory areas input (I), output (Q), and bit memory (M). )  is displayed in several work windows with the following operands.

For S7-300/400 and S7-1500 CPUs:

- Inputs
- Outputs
- Bit memories
- Timers
- Counters

For S7-1200 CPUs:

- Inputs
- Outputs
- Bit memories

#### Displaying inputs, outputs, bit memory, timers and counters

It shows all operands used and their assignment in the S7 program.

For all displayed operands, each line in the assignment list is dedicated to a byte of the memory area, in which the corresponding eight bits from 7 to 0 are labeled according to their access. Afterwards, a "bar" indicates whether access is made by a byte (B), word (W) or double word (D).

[You can find an explanation of the symbols in the assignment list here:](#symbols-in-the-assignment-list)

### Symbols in the assignment list

#### Meaning of the symbols in the assignment list

The following table shows the meaning of the symbols in the [assignment list](#) (The assignment list shows if an address has been allocated by access from an S7 program or if the address has been assigned to a SIMATIC S7 module. The assignment list gives you an overview of which bit in a byte is used for the memory areas input (I), output (Q), and bit memory (M). ) :

| Symbol | Meaning |
| --- | --- |
| ![Meaning of the symbols in the assignment list](images/6577838859_DV_resource.Stream@PNG-de-DE.png) | Indicates the address assignment in the selected state. |
| ![Meaning of the symbols in the assignment list](images/6578371979_DV_resource.Stream@PNG-de-DE.png) | Indicates the address assignment in the non-selected state. |
| ![Meaning of the symbols in the assignment list](images/6577744395_DV_resource.Stream@PNG-de-DE.png) | Indicates that a pointer start address and a tag address access the same address range and that they are selected. |
| ![Meaning of the symbols in the assignment list](images/6577829515_DV_resource.Stream@PNG-de-DE.png) | Indicates that a pointer start address and a tag address access the same address range and that they are not selected. |
| ![Meaning of the symbols in the assignment list](images/6583442059_DV_resource.Stream@PNG-de-DE.png) | Indicates the pointer assignment in the selected state. |
| ![Meaning of the symbols in the assignment list](images/6583527179_DV_resource.Stream@PNG-de-DE.png) | Indicates the pointer assignment in the non-selected state. |
| ![Meaning of the symbols in the assignment list](images/6583399819_DV_resource.Stream@PNG-de-DE.png) | Indicates that the byte is in use with byte access and the corresponding tag is selected. The shortcut menu allows you to display cross-reference information for the selected variables as well as the PLC tag table. |
| ![Meaning of the symbols in the assignment list](images/6583408139_DV_resource.Stream@PNG-de-DE.png) | Indicates that the byte is in use with byte access and the corresponding tag is not selected. |
| ![Meaning of the symbols in the assignment list](images/9104426123_DV_resource.Stream@PNG-de-DE.png) | Indicates that the byte is in use with word access and the corresponding tag is selected. The shortcut menu allows you to display cross-reference information for the selected variables as well as the PLC tag table. |
| ![Meaning of the symbols in the assignment list](images/9104653195_DV_resource.Stream@PNG-de-DE.png) | Indicates that the byte is in use with word access and the corresponding tag is not selected. |
| ![Meaning of the symbols in the assignment list](images/9104417675_DV_resource.Stream@PNG-de-DE.png) | Indicates that the byte is in use with double word access and the corresponding tag is selected. The shortcut menu allows you to display cross-reference information for the selected variables as well as the PLC tag table. |
| ![Meaning of the symbols in the assignment list](images/9105967243_DV_resource.Stream@PNG-de-DE.png) | Indicates that the byte is in use with double word access and the corresponding tag is not selected. |
| Background color: gray | Indicates that a byte is in use with byte, word or double word access and that the address is also in use by the hardware. The gray background color indicates overlapping memory access. |
| Background color: yellow | Indicates that the address is not in use by the hardware. |
| ![Meaning of the symbols in the assignment list](images/21541733131_DV_resource.Stream@PNG-de-DE.PNG) | Indicates that the memory area has been defined as system memory. |
| ![Meaning of the symbols in the assignment list](images/21541418379_DV_resource.Stream@PNG-de-DE.PNG) | Indicates that the memory area has been defined as clock memory. |

---

**See also**

[Layout of the assignment list](#layout-of-the-assignment-list)
  
[Introduction to the assignment list](#introduction-to-the-assignment-list)

### Displaying an assignment list

#### Requirement

A project has been created with programmed blocks.

#### Procedure

Proceed as follows to display the [assignment list](#) (The assignment list shows if an address has been allocated by access from an S7 program or if the address has been assigned to a SIMATIC S7 module. The assignment list gives you an overview of which bit in a byte is used for the memory areas input (I), output (Q), and bit memory (M). ) :

1. Select the "Program blocks" folder or one or more of the blocks it contains.
2. Select the "Assignment list" command in the "Tools" menu.

#### Result

The assignment list for the selected program is displayed.

#### View options in the assignment list

Refer to view respective view options that are set to display the desired information in the assignment list.

---

**See also**

[Setting the view options for the assignment list](#setting-the-view-options-for-the-assignment-list)
  
[Layout of the assignment list](#layout-of-the-assignment-list)

### Setting the view options for the assignment list

#### Introduction

The following view options are available for the [assignment list](#) (The assignment list shows if an address has been allocated by access from an S7 program or if the address has been assigned to a SIMATIC S7 module. The assignment list gives you an overview of which bit in a byte is used for the memory areas input (I), output (Q), and bit memory (M). ) :

- Used addresses:

  When this check box is activated, the addresses, I/Os and pointers used in the program are displayed.
- Free hardware addresses:

  When this check box is activated, only the free hardware addresses are displayed.

#### Requirement

- A project has been created with programmed blocks.
- The assignment list is open.

#### Procedure

Proceed as follows to set the view options for the assignment list:

1. Click on the arrow of the ![Procedure](images/9134808971_DV_resource.Stream@PNG-de-DE.png) symbol ("View options") in the task bar.

   The view options for the assignment list are opened. Check marks are set in front of the activated view options.
2. If you want to activate or deactivate a view option, click on the respective check box and set or remove the check mark.

#### Result

The view options are set and the desired information is displayed in the assignment list.

### Filter options in the assignment list

#### Filter settings

You can define your own filter settings for the [assignment list](#) (The assignment list shows if an address has been allocated by access from an S7 program or if the address has been assigned to a SIMATIC S7 module. The assignment list gives you an overview of which bit in a byte is used for the memory areas input (I), output (Q), and bit memory (M). ) . The following options are available for defining filters:

- Display all [addresses](#) (An address is the identification of an operand or of an operand area in the user program. Examples: Input I12.1, memory word MW25, data block DB3. )  of the address areas specified.
- Display of single, defined addresses from the selected address area, for example, "0" and "200".
- Display of complete areas from the selected address area, for example, "0 - 256".

The following table provides an overview of all available options:

| Selection in the | Selection | Symbol | Meaning |
| --- | --- | --- | --- |
| Address area | All CPU-dependent displayed addresses (I, O, M, T, C) can be activated as they are by default, or individual address areas can be activated. | Check box is activated | Only the activated address areas (I, O, M, T, C) are shown in the assignment list. |
| Filter area | Show assignment for all addresses | * | Displays the assignment of all addresses of the enabled address areas (I, Q, M). |
| Show assignment for selected addresses, for example, for the inputs "IB 0" and "IB 256" | 0;256  Separate individual addresses and areas by a semicolon. | Assignments of selected addresses for the activated address areas (I) are shown. |  |
| Show assignment for selected areas, for example, for the inputs "IB 0 to IB 100" and "IB 200 to IB 256". | 0-100;200-256  Contiguous areas should be connected by a hyphen. | Assignments of selected areas for the activated address areas (I) are shown. |  |

### Defining filters for assignment list

#### Requirement

- A project has been created with programmed blocks.
- The assignment list is open.

#### Defining filter

Proceed as follows to define a filter for the [assignment list](#) (The assignment list shows if an address has been allocated by access from an S7 program or if the address has been assigned to a SIMATIC S7 module. The assignment list gives you an overview of which bit in a byte is used for the memory areas input (I), output (Q), and bit memory (M). ) :

1. Click on the ![Defining filter](images/9137006859_DV_resource.Stream@PNG-de-DE.png) symbol ("Filter") in the task bar.

   The "Assignment List Filter" dialog opens.
2. Click on the ![Defining filter](images/13485299979_DV_resource.Stream@PNG-de-DE.png) symbol ("Create new filter") in the task bar.

   A new filter is created with the name "Filter_1". The check boxes for all addresses (inputs, outputs, memory bits, timers and counters) are activated by default for the filter.
3. If you want to change the name of the filter, click on the drop-down list in the task bar and enter a new filter name.
4. Deactivate the check boxes of addresses that are not to be affected by the filter.
5. Enter one of the following options in the filter area of the activated address:

   - Show all addresses used = "*"
   - Show single, defined addresses, for example, IB 0" and IB 25 = "0.25". Individual addresses and address areas are separated by commas or semicolons.
   - Show complete address areas, for example, IB 0 to IB 256 = "0-256". Complete address areas should be connected by a hyphen.
6. Confirm your entries with "OK".

   The newly defined filter is shown in the task bar of the assignment list under the specified name.

#### Delete filter

Proceed as follows to delete a filter:

1. Click on the ![Delete filter](images/9137006859_DV_resource.Stream@PNG-de-DE.png) symbol ("Filter") in the task bar.

   The filter dialog for the assignment list opens.
2. In the drop-down list of the task bar, select the filter you want to delete.
3. Click on the ![Delete filter](images/9137189643_DV_resource.Stream@PNG-de-DE.png) symbol ("Delete selected filter") in the task bar.

   The selected filter is deleted.

---

**See also**

[Filter options in the assignment list](#filter-options-in-the-assignment-list)
  
[Displaying an assignment list](#displaying-an-assignment-list-1)
  
[Introduction to the assignment list](#introduction-to-the-assignment-list)

### Filtering an assignment list

#### Requirement

- A project has been created with programmed blocks.
- The assignment list is open.

#### Procedure

1. Click on the arrow on the drop-down list.

   The available filter are displayed.
2. Select the desired filter.

#### Result

The assignment list is filtered according to the settings of the selected filter.

> **Note**
>
> The filter settings are saved when the project is closed.

### Defining retentive memory areas for bit memories

#### Introduction

In the assignment list you can define the width of the retentive memory area for bit memories. The content of tags which are addressed in retentive memory is retained after power off and at the STOP to RUN transition after power on.

The display of retentive bit memories can be enabled and disabled in the assignment list. If their display is enabled, retentive bit memories are identified by an icon in the "Address" column.

#### Requirement

The assignment list is open.

#### Procedure

Proceed as follows to define the width of the retentive memory area for bit memories:

1. Click "Retain" in the toolbar.

   The "Retain memory" dialog will open.
2. Starting at the count of 0, define the width of the retentive memory area by entering the last byte of this area in the input field. Watch out for any addresses of tags already assigned to the retentive area.
3. Load the block to the target system. Select the "Program blocks" folder in the Project tree and select the "Download to device" submenu in the shortcut menu.

#### Result

The width of the retentive memory area is defined. If enabled in the assignment list, an icon will indicate the retentive state of all tags in the "Address" column.

### Enabling the display of retentive bit memories

#### Introduction

In the assignment list you can enable and disable the display of retentive bit memories. The retentive bit memories are identified by means of an icon in the "Address" column if the display of retentivity is enabled.

#### Requirement

The assignment list is open.

#### Procedure

Proceed as follows to enable and disable the display of retentive bit memories:

1. Click "Display/hide retentivity" in the toolbar.

#### Result

The retentive tags are identified by means of an icon in the "Address" column of the bit memory area if the display of retentivity is enabled. The icons in the "Address" column are hidden if the display of retentivity is disabled.

## Displaying the call structure

This section contains information on the following topics:

- [Introduction to the call structure](#introduction-to-the-call-structure)
- [Symbols in the call structure](#symbols-in-the-call-structure)
- [Layout of the call structure](#layout-of-the-call-structure)
- [Displaying the call structure](#displaying-the-call-structure-1)
- [Setting the view options for the call structure](#setting-the-view-options-for-the-call-structure)
- [Introducing the consistency check in the call structure](#introducing-the-consistency-check-in-the-call-structure)
- [Checking block consistency in the call structure](#checking-block-consistency-in-the-call-structure)

### Introduction to the call structure

#### Call structure

The call structure describes the call hierarchy of the blocks within an S7 program.

It provides an overview of:

- The blocks used
- Jumps to the places of use of the blocks
- Dependencies between blocks
- Local data requirements of the blocks
- Status of the blocks

#### Information in the call structure

Displaying the call structure provides you with a list of the blocks used in the user program. The first level of the call structure is highlighted in color and shows the blocks that are not called by any other block in the program. Organization blocks are always shown on the first level of the call structure. Functions, function blocks and data blocks are only shown on the first level if they are not called by an organization block. When a block calls other blocks or functions, they are listed indented under the calling block. Instructions and blocks are shown in the call structure only if they are called by a block.

> **Note**
>
> Please note that no call structure is displayed for know-how-protected blocks.

#### View options

The following view options are available for the call structure:

- Show conflicts only:

  When this check box is activated, only conflicts within the call structure are displayed.
- Group multiple calls together:

  When this check box is activated, several block calls are grouped together. The number of block calls is displayed in the "Call frequency" column. The links to the various call locations are offered in a drop-down list in the "Details" column.

#### Displaying the block calls

You can display the block calls in a block by clicking on the arrow in front of the block title. To display the call information of all blocks, click on the "Expand list" icon in the toolbar.

You can hide the total overview by clicking the "Collapse list" icon.

#### Displaying cross-reference information

You can display the cross-reference information for a block in the Inspector window by right-clicking on the relevant block and selecting the "Cross-reference information" command from the shortcut menu.

To open the "Cross-references" view, click the "Cross-references" command in the shortcut menu.

#### Displaying blocks in the program editor

You can open the program editor from the call structure and edit blocks there.

To do this, select the required block in the call structure and select the "Open" command in the shortcut menu.

#### Displaying deleted blocks

The rows belonging to deleted blocks are identified by an icon.

> **Note**
>
> Please note that any existing local data can only be displayed or updated after a block is compiled.

---

**See also**

[Symbols in the call structure](#symbols-in-the-call-structure)

### Symbols in the call structure

#### Meaning of the symbols in the call structure

The following table shows the meaning of the symbols in the [call structure](#) (The call structure describes the call hierarchy of the blocks within an S7 program. It provides an overview of the blocks used, the jumps to the points of use of the blocks, the local data requirement of the blocks and the status of the blocks.) :

| Symbol | Meaning |
| --- | --- |
| ![Meaning of the symbols in the call structure](images/9094342283_DV_resource.Stream@PNG-de-DE.png) | Indicates an organization block (OB). |
| ![Meaning of the symbols in the call structure](images/9095971979_DV_resource.Stream@PNG-de-DE.png) | Indicates a function block (FB). |
| ![Meaning of the symbols in the call structure](images/9094350731_DV_resource.Stream@PNG-de-DE.png) | Indicates a function (FC). |
| ![Meaning of the symbols in the call structure](images/9095993227_DV_resource.Stream@PNG-de-DE.png) | Indicates a data block (DB). |
| ![Meaning of the symbols in the call structure](images/12276325643_DV_resource.Stream@PNG-de-DE.png) | Indicates that the block is declared as a multiple instance or as a parameter instance. |
| ![Meaning of the symbols in the call structure](images/8393519499_DV_resource.Stream@PNG-de-DE.png) | The object has an interface dependency to an object connected to the left. |
| ![Meaning of the symbols in the call structure](images/8394439819_DV_resource.Stream@PNG-de-DE.png) | Indicates that the block needs to be compiled again. |
| ![Meaning of the symbols in the call structure](images/8394448267_DV_resource.Stream@PNG-de-DE.png) | Indicates that the data block needs to be compiled again. |
| ![Meaning of the symbols in the call structure](images/8394333323_DV_resource.Stream@PNG-de-DE.png) | Indicates that the object is not available. |
| ![Meaning of the symbols in the call structure](images/8393612683_DV_resource.Stream@PNG-de-DE.png) | Indicates that the interface causes a time stamp conflict. |
| ![Meaning of the symbols in the call structure](images/8394571659_DV_resource.Stream@PNG-de-DE.png) | Indicates that the variable causes a time stamp conflict. |
| ![Meaning of the symbols in the call structure](images/6578754699_DV_resource.Stream@PNG-de-DE.png) | Indicates that the block is not called directly or indirectly from an OB. |
| ![Meaning of the symbols in the call structure](images/26161674891_DV_resource.Stream@PNG-de-DE.PNG) | Indicates that an object has know-how protection. |
| ![Meaning of the symbols in the call structure](images/8394797195_DV_resource.Stream@PNG-de-DE.png) | Indicates that a tag declaration in the interface has a recursive dependency:  - Scenario 1: FB1 calls FB2 and this then calls FB1. The instance data blocks of these FBs have a recursion in the interface. - Scenario 2: A multiple instance FB uses the instance DB of its parent FB as a global DB. |
| ![Meaning of the symbols in the call structure](images/8394652299_DV_resource.Stream@PNG-de-DE.png) | Indicates that the block is normally called recursively. |
| ![Meaning of the symbols in the call structure](images/102497147403_DV_resource.Stream@PNG-de-DE.png) | Indicates that a block is called recursively with a condition. |
| ![Meaning of the symbols in the call structure](images/102497156235_DV_resource.Stream@PNG-de-DE.png) | Indicates that a block is called recursively without a condition. |

### Layout of the call structure

#### Layout of the call structure

The view of the [call structure](#) (The call structure describes the call hierarchy of the blocks within an S7 program. It provides an overview of the blocks used, the jumps to the points of use of the blocks, the local data requirement of the blocks and the status of the blocks.)  consists of the following columns:

| Column | Content/meaning |
| --- | --- |
| Call structure | Shows an overview of the blocks called   If the viewing option "Group multiple calls together" is enabled, several block calls are grouped together and the "Number of calls" column is displayed. |
| Call type (!) | Shows the type of call, for example recursive block call. |
| Address | Shows the absolute address of the block. With a function block, the absolute address of the corresponding instance data block is also shown. |
| Call frequency | Indicates the number of multiple calls of blocks. |
| Details | Shows the network or interface of the calling block. All information are offered as a link in this column. With this link, you can jump to the location of the block call in the program editor. If the viewing option "Group multiple calls together" option is enabled, the calls are grouped together and are available as links in a drop-down list. |
| Local data (in path) | Indicates the local data requirement of the full path.  Blocks with optimized access have higher local data requirements because the information for the symbolic addressing is stored with them.  Please note that any existing local data can only be displayed or updated after compiling a block. |
| Local data (for blocks) | Show the local data requirements of the block.   Blocks with optimized access have higher local data requirements because the information for the symbolic addressing is stored with them.  Please note that any existing local data can only be displayed or updated after compiling a block. |

---

**See also**

[Symbols in the call structure](#symbols-in-the-call-structure)
  
[Introducing the consistency check in the call structure](#introducing-the-consistency-check-in-the-call-structure)

### Displaying the call structure

#### Requirement

A project has been created with [blocks](#) (A block structures the user program into independent sections. There are: organization blocks (OB), function blocks (FB), functions (FC) and data blocks (DB).) .

#### Procedure

Proceed as follows to display the [call structure](#) (The call structure describes the call hierarchy of the blocks within an S7 program. It provides an overview of the blocks used, the jumps to the points of use of the blocks, the local data requirement of the blocks and the status of the blocks.) :

1. Select the "Program blocks" folder or one or more of the blocks it contains.
2. Select the "Call structure" command in the "Tools" menu.

#### Result

The call structure for the selected program is displayed.

> **Note**
>
> Please note that any existing local data can only be displayed or updated after compiling a block.

---

**See also**

[Setting the view options for the call structure](#setting-the-view-options-for-the-call-structure)

### Setting the view options for the call structure

#### Introduction

The following view options are available for the [call structure](#) (The call structure describes the call hierarchy of the blocks within an S7 program. It provides an overview of the blocks used, the jumps to the points of use of the blocks, the local data requirement of the blocks and the status of the blocks.) :

- Show conflicts only:

  Only the blocks causing conflicts within the call structure are displayed if this check box is activated.

  The following blocks cause conflicts:

  - Blocks executing any calls with older or newer code time stamps.
  - Blocks calling a block with modified interface.
  - Blocks using a tag with modified address and/or data type.
  - Block called neither directly, nor indirectly by an OB.
  - Blocks calling a block which no longer exists.
- Group multiple calls together:

  When this viewing option is enabled, several block calls and data block accesses are grouped together. The number of block calls is displayed in the "Call frequency" column. The links to the various call locations are offered in a drop-down list in the "Details" column.

#### Requirement

- A project has been created with programmed blocks.
- The call structure is open.

#### Procedure

Proceed as follows to set the view options for the call structure:

1. Click on the arrow of the ![Procedure](images/9134808971_DV_resource.Stream@PNG-de-DE.png) symbol ("View options") in the task bar.

   The view options for the call structure opens. Check marks are set in front of the activated view options.
2. If you want to activate or deactivate a view option, click on the respective check box and set or remove the check mark.

#### Result

The view options are set and the required information is displayed in the call structure.

### Introducing the consistency check in the call structure

#### Consistency check

Changing the [time stamp](#) (The time stamp is an entry made in a block about the last change made.)  of a block during or after the program is generated can lead to time stamp conflicts, which in turn cause inconsistencies among the blocks that are calling and being called.

#### Using the consistency check

The "Consistency check" function is used to visualize inconsistencies when time stamp conflicts occur. Whe the consistency check is performed, the inconsistent blocks are shown in the [call structure](#) (The call structure describes the call hierarchy of the blocks within an S7 program. It provides an overview of the blocks used, the jumps to the points of use of the blocks, the local data requirement of the blocks and the status of the blocks.)  and marked with the correspoinding symbols.

- Most time stamp and interface conflicts can be rectified by recompiling the blocks.
- If compilation fails to clear up inconsistencies you can use the link in the "Details" column to go to the source of the problem in the program editor and manually eliminate any inconsistencies.
- The blocks marked in red must be recompiled.

---

**See also**

[Symbols in the call structure](#symbols-in-the-call-structure)

### Checking block consistency in the call structure

#### Requirement

- A project has been created with programmed blocks.
- The call structure is open.

#### Procedure

Proceed as follows to check the block consistency:

1. Click on the ![Procedure](images/9137263883_DV_resource.Stream@PNG-de-DE.png) symbol ("Consistency check") in the task bar.

   The block consistency is checked. Blocks found to be inconsistent are marked accordingly by a symbol.
2. If a block is inconsistent, click on the arrow in front of the block title in the call structure.

   The inconsistent blocks are displayed. The exact problem locations are listed as links in the "Details" column.
3. Click on the respective link in the "Details" column to jump to the location in the block requiring correction.
4. Check and correct the inconsistencies in the blocks.
5. Recompile the blocks by selecting the required blocks and clicking on the command "Compile" in the shortcut menu.
6. Download the corrected blocks to the target system by clicking the command "Download to device" in the shortcut menu.

#### Result

The block consistency is checked. The inconsistencies in the blocks are corrected. The corrected blocks are loaded to the target system.

---

**See also**

[Symbols in the call structure](#symbols-in-the-call-structure)

## Displaying the dependency structure

This section contains information on the following topics:

- [Introduction to the dependency structure](#introduction-to-the-dependency-structure)
- [Layout of the dependency structure](#layout-of-the-dependency-structure)
- [Symbols in the dependency structure](#symbols-in-the-dependency-structure)
- [Displaying the dependency structure](#displaying-the-dependency-structure-1)
- [Setting the view options for the dependency structure](#setting-the-view-options-for-the-dependency-structure)
- [Introducing the consistency check in the dependency structure](#introducing-the-consistency-check-in-the-dependency-structure)
- [Checking block consistency in the dependency structure](#checking-block-consistency-in-the-dependency-structure)

### Introduction to the dependency structure

#### Introduction

The dependency structure shows the dependencies each block in the program has to other blocks.

#### Information in the dependency structure

Displaying the dependency structure provides you with a list of the blocks used in the user program. A block is shown at the far left, and blocks that call or use this block are indented below it.

The dependency structure also shows the status of the individual blocks using symbols.

Objects that cause a time stamp conflict and could lead to an inconsistency in the program are marked with various symbols.

The dependency structure is an extension of the cross-reference list for objects.

#### View options

The following view options are available for the dependency structure:

- Show conflicts only:

  When this check box is activated, only the conflicts within the dependency structure are displayed.
- Group multiple calls together:

  When this check box is activated, several block calls are grouped together. The number of block calls is shown numerically in the "Dependency structure" column. The links to the various call locations are offered in a drop-down list in the "Details" column.

#### Displaying the dependencies

Clicking on the arrow in front of the block title displays the blocks that call or use this block. To display the dependencies of all blocks,

click the "Expand list" icon in the toolbar.

You can hide the total overview by clicking the "Collapse list" icon.

#### Displaying cross-reference information

You can display the cross-reference information for a block in the Inspector window by right-clicking on the relevant block and selecting the "Cross-reference information" command from the shortcut menu.

To open the "Cross-references" view, click the "Cross-references" command in the shortcut menu.

#### Displaying blocks in the program editor

You can open the program editor from the dependency structure and edit blocks there. To do this, select the required block in the dependency structure and select the "Open" command in the shortcut menu.

### Layout of the dependency structure

#### Layout of the dependency structure

The view of the [dependency structure](#) (The dependency structure is a display which shows the dependencies for each block in the program to other blocks. )  consists of the following columns:

| Column | Content/meaning |
| --- | --- |
| Dependency | It indicates the dependencies between each block and the other blocks in the program. |
| Call type (!) | Shows the type of call, for example recursive block call. |
| Address | Shows the absolute address of the block. |
| Call frequency | Indicates the number of multiple calls of blocks. |
| Details | Shows the network or interface of the called block. All information are offered as a link in this column. With this link, you can jump to the location of the block call in the program editor. If the viewing option "Group multiple calls together" option is enabled, the calls are grouped together and are available as links in a drop-down list. |

---

**See also**

[Symbols in the dependency structure](#symbols-in-the-dependency-structure)

### Symbols in the dependency structure

#### Meaning of the symbols in the dependency structure

The following table shows the meaning of the symbols in the [dependency structure](#) (The dependency structure is a display which shows the dependencies for each block in the program to other blocks. ) :

| Symbol | Meaning |
| --- | --- |
| ![Meaning of the symbols in the dependency structure](images/9094342283_DV_resource.Stream@PNG-de-DE.png) | Indicates an organization block (OB). |
| ![Meaning of the symbols in the dependency structure](images/9095971979_DV_resource.Stream@PNG-de-DE.png) | Indicates a function block (FB). |
| ![Meaning of the symbols in the dependency structure](images/9094350731_DV_resource.Stream@PNG-de-DE.png) | Indicates a function (FC). |
| ![Meaning of the symbols in the dependency structure](images/9095993227_DV_resource.Stream@PNG-de-DE.png) | Indicates a data block (DB). |
| ![Meaning of the symbols in the dependency structure](images/12276325643_DV_resource.Stream@PNG-de-DE.png) | Indicates that the block is declared as a multiple instance or as a parameter instance. |
| ![Meaning of the symbols in the dependency structure](images/8393519499_DV_resource.Stream@PNG-de-DE.png) | The object has an interface dependency to an object connected to the left. |
| ![Meaning of the symbols in the dependency structure](images/8394439819_DV_resource.Stream@PNG-de-DE.png) | Indicates that the block needs to be compiled again. |
| ![Meaning of the symbols in the dependency structure](images/8394448267_DV_resource.Stream@PNG-de-DE.png) | Indicates that the data block needs to be compiled again. |
| ![Meaning of the symbols in the dependency structure](images/8394571659_DV_resource.Stream@PNG-de-DE.png) | Indicates that there is an inconsistency with this object. |
| ![Meaning of the symbols in the dependency structure](images/26161674891_DV_resource.Stream@PNG-de-DE.PNG) | Indicates that an object has know-how protection. |
| ![Meaning of the symbols in the dependency structure](images/8394797195_DV_resource.Stream@PNG-de-DE.png) | Indicates that a tag declaration in the interface has a recursive dependency:  - Scenario 1: FB1 calls FB2 and this then calls FB1. The instance data blocks of these FBs have a recursion in the interface. - Scenario 2: A multiple instance FB uses the instance DB of its parent FB as a global DB. |
| ![Meaning of the symbols in the dependency structure](images/8394652299_DV_resource.Stream@PNG-de-DE.png) | Indicates that the block is normally called recursively. |
| ![Meaning of the symbols in the dependency structure](images/102497147403_DV_resource.Stream@PNG-de-DE.png) | Indicates that a block is called recursively with a condition. |
| ![Meaning of the symbols in the dependency structure](images/102497156235_DV_resource.Stream@PNG-de-DE.png) | Indicates that a block is called recursively without a condition. |

### Displaying the dependency structure

#### Requirement

A project has been created with programmed blocks.

#### Procedure

Proceed as follows to display the [dependency structure](#) (The dependency structure is a display which shows the dependencies for each block in the program to other blocks. ) :

1. Select the block folder or one or more of the blocks contained therein.
2. Select the "Dependency structure" command in the "Tools" menu.

#### Result

The dependency structure for the selected program is displayed.

---

**See also**

[Setting the view options for the dependency structure](#setting-the-view-options-for-the-dependency-structure)

### Setting the view options for the dependency structure

#### Introduction

The following view options are available for the [dependency structure](#) (The dependency structure is a display which shows the dependencies for each block in the program to other blocks. ) :

- Show conflicts only:

  When this check box is activated, only the conflicts within the dependency structure are displayed.

  The following blocks cause conflicts:

  - Blocks executing any calls with older or newer code time stamps.
  - Blocks called by a block with modified interface.
  - Blocks using a tag with modified address and/or data type.
  - Block called neither directly, nor indirectly by an OB.
- Group multiple calls together:

  When this check box is activated, several block calls are grouped together. The number of block calls is shown in the relevant column. The links to the various call locations are offered in a drop-down list in the "Details" column.

#### Requirement

- A project has been created with programmed blocks.
- The dependency structure is open.

#### Procedure

Proceed as follows to set the view options for the dependency structure:

1. Click on the arrow of the ![Procedure](images/9134808971_DV_resource.Stream@PNG-de-DE.png) symbol ("View options") in the task bar.

   The view options for the dependency structure are opened. Check marks are set in front of the activated view options.
2. If you want to activate or deactivate a view option, click on the respective check box and set or remove the check mark.

#### Result

The view options are set and the required information is displayed in the dependency structure.

### Introducing the consistency check in the dependency structure

#### Consistency check

Changing the [time stamp](#) (The time stamp is an entry made in a block about the last change made.)  of a block during or after program creation can lead to time stamp conflicts, which in turn cause inconsistencies among the blocks that are calling and being called.

#### Using the consistency check

The "Consistency check" function is used to visualize inconsistencies. When the consistency check is performed, the inconsistent blocks are shown in the [dependency structure](#) (The dependency structure is a display which shows the dependencies for each block in the program to other blocks. )  and marked with the corresponding symbols.

- Most time stamp and interface conflicts can be rectified by recompiling the blocks.
- If compilation fails to clear up inconsistencies, you can use the link in the "Details" column to go to the source of the problem in the program editor and manually eliminate any inconsistencies.
- The blocks marked in red must be recompiled.

---

**See also**

[Layout of the dependency structure](#layout-of-the-dependency-structure)
  
[Symbols in the dependency structure](#symbols-in-the-dependency-structure)

### Checking block consistency in the dependency structure

#### Requirement

- A project has been created with programmed blocks.
- The dependency structure is open.

#### Procedure

Proceed as follows to check the block consistency:

1. Click on the ![Procedure](images/9137263883_DV_resource.Stream@PNG-de-DE.png) symbol ("Consistency check") in the task bar.

   The block consistency is checked. Blocks found to be inconsistent are marked accordingly by a symbol.
2. If a block is inconsistent, click on the arrow in front of the block title in the dependency structure.

   The inconsistent blocks are displayed. The exact problem locations are listed as links in the "Details" column.
3. Check and correct the inconsistencies in the blocks.
4. Recompile the blocks by selecting the required blocks and clicking on the command "Compile" in the shortcut menu.
5. Download the corrected blocks to the target system by clicking the command "Download to device" in the shortcut menu.

#### Result

The block consistency is checked. The inconsistencies in the blocks are corrected. The corrected blocks are loaded to the target system.

---

**See also**

[Symbols in the dependency structure](#symbols-in-the-dependency-structure)

## Displaying CPU resources

This section contains information on the following topics:

- [Introducing resources](#introducing-resources)
- [Layout of the "Resources" tab](#layout-of-the-resources-tab)
- [Displaying resources](#displaying-resources)
- [Selecting the maximum load memory available](#selecting-the-maximum-load-memory-available)

### Introducing resources

#### Introduction

The "Resources" tab indicates the hardware resources of the configured CPU for:

- the used programming objects,
- the assignment of the different memory areas within the CPU and
- the assigned inputs and outputs of the existing input and output modules.

#### Information provided in the "Resources" tab

The resources tab provides an overview of the hardware resources. The display in this tab depends on the CPU which you are using. The following information is displayed:

- the programming objects used in the CPU (e.g. OB, FC, FB, DB, data types and PLC tags)
- the memory areas available on the CPU (load memory, work memory - divided into code work memory and data work memory depending on the CPU -, retentive memory), their maximum size and utilization by the programming objects stated above
- the I/O of modules which can be configured for the CPU (I/O modules, digital input modules, digital output modules, analog input modules, and analog output modules), including the I/O already in use.

#### Display of the maximum available load memory

The maximum size of available load memory can be selected from a drop-down list box in the "Total" row of the "Load memory" column.

> **Note**
>
> **Displaying the allocated load memory in the CPU**
>
> Note that the sum of the allocated load memory cannot be precisely determined if not all blocks are compiled.
>
> In this case, a preceding "&gt;" in front of the sum indicates that the amount of allocated space may be greater than that shown because uncompiled blocks are not taken into account in the total.

#### Display of the maximum available work memory

The maximum size of available work memory is displayed in the "Work memory" column or in the "Code work memory" and "Data work memory" columns in the "Total" row.

#### Display of the maximum available retentive memory

The maximum size of available retentive memory is displayed in the "Retain memory" column in the "Total" row.

> **Note**
>
> **Retentive memory data**
>
> All bit memories and data blocks specified as retentive will be integrated in the calculation of the retentive data.

#### Updating the display in the "Resources" tab

Click the "Update view" toolbar button to update the display of objects.

#### Benefits of the display in the "Resources" tab

The "Resources" tab of the program information dialog provides a detailed list of all objects and of the corresponding memory area used.

The tab also indicates shortage of resources and helps to avoid such states.

Blocks which are not compiled can be identified as their size is indicated by a question mark.

---

**See also**

[Layout of the "Resources" tab](#layout-of-the-resources-tab)
  
[Displaying resources](#displaying-resources)
  
[Selecting the maximum load memory available](#selecting-the-maximum-load-memory-available)

### Layout of the "Resources" tab

#### Layout of the "Resources" tab in the program information

The view of the "Resources" tab consists of the following columns:

| Column | Content/meaning |
| --- | --- |
| Objects | The "Details" area provides an overview of the programming objects available in the CPU, including their memory assignments. |
| Load memory | Displays the maximum load memory resources of the CPU as a percentage and as absolute value.  The values displayed under "Total" provide information on the maximum memory available in the load memory.  The values displayed under "Used" provide information on the memory actually used in the load memory.  If a value is displayed in red, the available memory capacity has been exceeded. |
| Work memory  or   code and data work memory | Displays the maximum work memory resources of the CPU as a percentage and as absolute value.  The work memory depends on the CPU and is divided into "Code work memory" and "Data work memory" for a CPU from the S7-400 or S7-1500 series, for example.  The values displayed under "Total" provide information on the maximum memory available in the work memory.  The values displayed under "Used" provide information on the memory space actually used in the work memory.  If a value is displayed in red, the available memory capacity has been exceeded. |
| Retentive memory | Displays the maximum resources for retentive memory in the CPU as a percentage and as absolute value.  The values displayed under "Total" provide information on the maximum memory available in the retentive memory.  The values displayed under "Used" provide information on the memory actually used in the retentive memory.   If a value is displayed in red, the available memory capacity has been exceeded. |
| I/O | Displays the I/Os which are available on the CPU, including their module-specific availability in the next columns.   The values displayed at "Configured" provide information about the maximum number of I/O available.  The values displayed under "Used" provide information on the actually used inputs and outputs. |
| DI / DQ / AI / AQ | Displays the number of configured and used inputs/outputs:  DI = Digital inputs  DQ = Digital outputs  AI = Analog inputs  AQ = Analog outputs  The values displayed at "Configured" provide information about the maximum number of I/O available.  The values displayed under "Used" provide information on the actually used inputs and outputs. |

---

**See also**

[Displaying resources](#displaying-resources)
  
[Selecting the maximum load memory available](#selecting-the-maximum-load-memory-available)
  
[Introducing resources](#introducing-resources)

### Displaying resources

#### Introduction

The memory use shows you which space is allocated to specific objects in the CPU.

> **Note**
>
> **Displaying the allocated load memory in the CPU**
>
> Note that the sum of the allocated load memory cannot be precisely determined if not all blocks are compiled.
>
> In this case, a preceding "&gt;" in front of the sum indicates that the amount of allocated space may be greater than that shown because uncompiled blocks are not taken into account in the total.

#### Requirement

A project with programmed blocks has been created.

#### Procedure

Proceed as follows to display the resources of the respective CPU memory areas:

1. Select the block folder below the relevant CPU, or one or several of the blocks contained therein.
2. Select the "Resources" command in the "Tools" menu.

#### Result

The memory resources of the assigned CPU are displayed.

### Selecting the maximum load memory available

#### Requirement

A project with programmed blocks has been created.

#### Procedure

Proceed as follows to display the available maximum of load memory resources:

1. Select the block folder below the relevant CPU, or one or several of the blocks contained therein.
2. Select the "Resources" command in the "Tools" menu.
3. In the dialog that is displayed, open the drop-down list in the "Total" field of the "Load memory" column by clicking the icon.
4. Select a corresponding value for the CPU used by clicking it in the drop-down list box.

#### Result

The "Total" field displays the selected maximum memory resources.

> **Note**
>
> **Display of maximum memory resources**
>
> If a value is displayed in red for the maximum memory resources, the available memory capacity has been exceeded.
>
> In this case, adapt the memory capacity as described above.

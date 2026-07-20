---
title: "Declaring PLC tags"
package: ProgPLCTagsenUS
topics: 58
devices: [S7-1200, S7-1500, S7-1500T, S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Declaring PLC tags

This section contains information on the following topics:

- [Overview of PLC tag tables](#overview-of-plc-tag-tables)
- [Structure of the PLC tag tables](#structure-of-the-plc-tag-tables)
- [Rules for PLC tags](#rules-for-plc-tags)
- [Creating and managing PLC tag tables](#creating-and-managing-plc-tag-tables)
- [Declaring PLC tags](#declaring-plc-tags-1)
- [Grouping PLC tags for inputs and outputs in structures](#grouping-plc-tags-for-inputs-and-outputs-in-structures)
- [Declaring global constants](#declaring-global-constants)
- [Editing properties](#editing-properties)
- [Monitoring of PLC tags](#monitoring-of-plc-tags)
- [Editing PLC tag tables](#editing-plc-tag-tables)

## Overview of PLC tag tables

### Introduction

PLC tag tables contain the definitions of the PLC tags and symbolic constants that are valid throughout the CPU. A PLC tag table is created automatically for each CPU used in the project. You can create additional tag tables and use these to sort and group tags and constants.

In the project tree there is a "PLC tags" folder for each CPU of the project. The following tables are included:

- "All tags" table
- Standard tag table
- Optional: Other user-defined tag tables

### All tags

The "All tags" table gives an overview of all PLC tags, user constants and system constants of the CPU. This table cannot be deleted or moved.

### Standard tag table

There is one standard tag table for each CPU of the project. It cannot be deleted, renamed or moved. The default tag table contains PLC tags, user constants and system constants. You can declare all PLC tags in the default tag table, or create additional user-defined tag tables as you want.

### User-defined tag tables

You can create multiple user-defined tag tables for each CPU to group tags according to your requirements. You can rename, gather into groups, or delete user-defined tag tables. User-defined tag tables can contain PLC tags and user constants.

---

**See also**

[Structure of the PLC tag tables](#structure-of-the-plc-tag-tables)
  
[Using tags within the program](Programming%20basics.md#using-tags-within-the-program)
  
[Basics of constants](Programming%20basics.md#basics-of-constants)

## Structure of the PLC tag tables

### Introduction

Each PLC tag table contains a tab for tags and a tab for user constants. The default tag table and the "All tags" table also have a "System constants" tab.

### Structure of the "PLC tags" tab

In the "Tags" tab you declare the global PLC tags that you require in the program. The following figure shows the tab structure. The number of columns shown can vary.

![Structure of the "PLC tags" tab](images/83551124363_DV_resource.Stream@PNG-en-US.png)

The following table shows the meaning of the individual columns. The number of columns shown can vary. You can show or hide the columns as required.

| Column | Explanation |
| --- | --- |
| ![Structure of the "PLC tags" tab](images/45636405771_DV_resource.Stream@PNG-de-DE.png) | Symbol you can click on to drag-and-drop a tag to a program for use as an operand. |
| Name | Unique name for the constants throughout the CPU. |
| Data type | Data type of the tags. |
| Address | Tag address. |
| Retain | Marks the tag as retentive.  The values of retentive tags are retained even after the power supply is switched off. |
| Visible in HMI engineering | Indicates whether the tag in the operand selection is visible for HMI as default. |
| Accessible from HMI/OPC UA/Web API | Indicates whether HMI/OPC UA/Web API can access this variable during runtime. |
| Writable from HMI/OPC UA/Web API | Indicates whether or not the tag can be written from HMI/OPC UA/Web API during runtime. |
| Supervision | Indicates whether monitoring for process diagnostics was created for the tag. |
| Monitor value | Current data value in the CPU.   This column only appears if an online connection is established and you select the "Monitor all" button. |
| Tag table | Shows which tag table includes the tag declaration.  This column is only available in the "All tags" table. |
| Comment | Comment to document the tags. |

### Structure of the "User constants" and "System constants" tabs

In the "User constants" you define symbolic constants that are valid throughout the CPU. The constants required by the system are shown in the "Systems constants" tab. System constants can be hardware identifiers, for example, which can be used for identification of modules.

The following figure shows the structure of both tabs. The number of columns shown can vary.

![Structure of the "User constants" and "System constants" tabs](images/25480892811_DV_resource.Stream@PNG-en-US.png)

The following table shows the meaning of the individual columns. You can show or hide the columns as required.

| Column | Explanation |
| --- | --- |
| ![Structure of the "User constants" and "System constants" tabs](images/13733607307_DV_resource.Stream@PNG-de-DE.png) | Symbol you can click to move a tag into a network via a drag-and-drop operation for use as an operand. |
| Name | Unique name for the constants throughout the CPU. |
| Data type | Data type of the constants |
| Value | Value of the constants |
| Tag table | Shows which tag table includes the constant declaration.  This column is only available in the "All tags" table. |
| Comment | Comments to document the tags. |

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Using tags within the program](Programming%20basics.md#using-tags-within-the-program)
  
[Basics of constants](Programming%20basics.md#basics-of-constants)
  
[Hardware data types](Data%20types.md#hardware-data-types)
  
[What you need to know about HW identifiers (S7-1200, S7-1500, S7-1500T)](Configuring%20automation%20systems.md#what-you-need-to-know-about-hw-identifiers-s7-1200-s7-1500-s7-1500t)
  
[Overview of PLC tag tables](#overview-of-plc-tag-tables)
  
[Show and hide table columns](#show-and-hide-table-columns)
  
[Editing tables](Introduction%20to%20the%20TIA%20Portal.md#editing-tables)

## Rules for PLC tags

This section contains information on the following topics:

- [Valid names of PLC tags](#valid-names-of-plc-tags)
- [Permissible addresses and data types of PLC tags](#permissible-addresses-and-data-types-of-plc-tags)

### Valid names of PLC tags

#### Permissible characters

The following rules apply to the use of names for PLC tags:

- Letters, numbers, special characters are permitted.
- The use of reserved keywords is not recommended.
- Quotation marks are not permitted as a component of the tag name.

#### Unique tag names

The names of the PLC tags must be unique throughout the CPU, even if the tags are located in different tag tables of a CPU. A name that is already used for a block, another PLC tag or a constant within the CPU, cannot be used for a new PLC tag. The uniqueness check does not differentiate between use of small and capital letters.

If you enter an already assigned name another time, a sequential number is automatically appended to the second name entered. For example, if you enter the name "Motor" a second time, the second entry is changed to "Motor(1)".

#### Unique table names

The names of the PLC tag tables must also be unique throughout the CPU. A unique name is automatically suggested when user-defined PLC tag tables are being created.

> **Note**
>
> **You can find more information on permissible characters in tag names in the Siemens Industry Online Support in the following entries:**
>
> When should identifiers and operands be used in "quotation marks" in STEP 7 (TIA Portal)?
>
> ![Unique table names](images/84907645963_DV_resource.Stream@PNG-de-DE.png)
> [https://support.industry.siemens.com/cs/ww/en/view/109477857](https://support.industry.siemens.com/cs/ww/en/view/109477857)

---

**See also**

[Using tags within the program](Programming%20basics.md#using-tags-within-the-program)
  
[Keywords and reserved identifiers](Programming%20basics.md#keywords-and-reserved-identifiers)
  
[Permissible addresses and data types of PLC tags](#permissible-addresses-and-data-types-of-plc-tags)
  
[Entering a PLC tag declaration](#entering-a-plc-tag-declaration)

### Permissible addresses and data types of PLC tags

The addresses of PLC tags are made up of the particulars of the operand area and the address within this area.

The addresses must be unique throughout the CPU. If you enter an address that is already assigned to another tag, the address will be highlighted at both places in yellow and an error message will be issued.

#### Operand areas

The following table shows the possible operand areas. The available data types depend on the CPU you use:

| Operand area |  | Explanation | Data type | Format | Address area: |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| International mnemonics | German mnemonics | S7-1200 | S7-300/400 | S7-1500 |  |  |  |
| I | E | Input bit | BOOL | I x.y  E x.y | 0.0..1023.7 | 0.0..65535.7 | 0.0..32767.7 |
| I | E | Input (64-bit) | LWORD, LINT, ULINT, LTIME, LTOD, LDT, LREAL, PLC data type (S7-1200/1500 only) | I x.0  E x.0 | - | - | 0.0..32760.0 |
| IB | EB | Input byte | BYTE, CHAR, SINT, USINT | IB x  EB y | 0..1023 | 0..65535 | 0..32767 |
| IW | EW | Input word | WORD, INT, UINT, DATE, WCHAR, S5TIME | IW x  EW y | 0..1022 | 0..65534 | 0..32766 |
| ID | ED | Input double word | DWORD, DINT, UDINT, REAL, TIME, TOD | ID x  ED y | 0..1020 | 0..65532 | 0..32764 |
| Q | A | Output bit | BOOL | Q x.y   A x.y | 0.0..1023.7 | 0.0..65535.7 | 0.0..32767.7 |
| Q | A | Output (64-bit) | LWORD, LINT, ULINT, LTIME, LTOD, LDT, LREAL, PLC data type (S7-1200/1500 only) | Q x.0   A x.0 | - | - | 0.0..32760.0 |
| QB | AB | Output byte | BYTE, CHAR, SINT, USINT | QB x   AB y | 0..1023 | 0..65535 | 0..32767 |
| QW | AW | Output word | WORD, INT, UINT, DATE, WCHAR, S5TIME | QW x   AW y | 0..1022 | 0..65534 | 0..32766 |
| QD | AD | Output double word | DWORD, DINT, UDINT, REAL, TIME, TOD | QD x   AD y | 0..1020 | 0..65532 | 0..32764 |
| M | M | Memory bit | BOOL | M x.y | 0.0..8191.7 | 0.0..65535.7 | 0.0..16383.7 |
| M | M | Bit memory (64-bit) | LREAL | M x.0 | 0.0..8184.0 | - | 0.0..16376.0 |
| M | M | Bit memory (64-bit) | LWORD, LINT, ULINT, LTIME, LTOD, LDT | M x.0 | - | - | 0.0..16376.0 |
| MB | MB | Memory byte | BYTE, CHAR, SINT, USINT | MB x | 0..8191 | 0..65535 | 0..16383 |
| MW | MW | Memory word | WORD, INT, UINT, DATE, WCHAR, S5TIME | MW x | 0..8190 | 0..65534 | 0..16382 |
| MD | MD | Memory double word | DWORD, DINT, UDINT, REAL, TIME, TOD | MD x | 0..8188 | 0..65532 | 0..16380 |
| T | T | Time function (for S7-300/400 only) | Timer | T n | - | 0..65535 | 0..2047 |
| C | Z | Counter function (for S7-300/400 only) | Counter | Z n  C n | - | 0..65535 | 0..2047 |

#### Addresses

The following table shows the possible addresses of tags:

| Data type | Address | Example |
| --- | --- | --- |
| BOOL | Tags with BOOL data type are addressed with a byte number and a bit number. The numbering of the bytes begins at 0 for each operand range. The numbering of the bits is from 0 to 7. | A 1.0 |
| BYTE, CHAR, SINT, USINT | Tags with BYTE, CHAR, SINT, and USINT data type are addressed with a byte number. | MB 1 |
| WORD, INT, UINT, DATE, WCHAR, S5TIME | Tags with WORD, INT, UINT, DATE, S5TIME data type consist of two bytes. They are addressed with the number of the lowest byte. | IW 1 |
| DWORD, DINT, UDINT, REAL, TIME, TOD | Tags with DWORD, DINT, UDINT, REAL, TIME, TOD data type consist of four bytes. They are addressed with the number of the lowest byte. | AD 1 |
| LWORD, LINT, ULINT, LTIME, LTOD, LDT, LREAL | Tags of data type LWORD, LINT, ULINT, LTIME, LTOD, LDT, and LREAL consist of eight bytes. They are addressed with it number 0 and the number of the lower byte. | I 1.0 |

#### Mnemonics used

The addresses that you enter in the PLC tag table are automatically adapted to the set mnemonics.

---

**See also**

[Setting the mnemonics](Program%20editor.md#setting-the-mnemonics)
  
[Using tags within the program](Programming%20basics.md#using-tags-within-the-program)
  
[Valid names of PLC tags](#valid-names-of-plc-tags)
  
[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Entering a PLC tag declaration](#entering-a-plc-tag-declaration)

## Creating and managing PLC tag tables

This section contains information on the following topics:

- [Creating PLC tag tables](#creating-plc-tag-tables)
- [Opening the PLC tag tables](#opening-the-plc-tag-tables)
- [Copying or moving PLC tag tables](#copying-or-moving-plc-tag-tables)
- [Grouping PLC tag tables](#grouping-plc-tag-tables)

### Creating PLC tag tables

You can created multiple user-defined PLC tag tables in a CPU. Each tag table must have have a unique name throughout the CPU.

#### Requirement

The project view is open.

#### Procedure

To created a new PLC tag table, follow these steps:

1. Open the "PLC tags" folder in the project navigation.
2. Double-click the "Add new tag table" command.

   The "Add new tag table" dialog opens.
3. Enter a name for the new tag table that is unique CPU-wide.
4. Optional: Select the option "released" if the new tag table is in a new Software Unit and access should be possible from other Software Units.
5. Confirm your entries with "OK".

#### Result

A new PLC tag table is created. You can now declare tags and constants in this table.

---

**See also**

[Overview of PLC tag tables](#overview-of-plc-tag-tables)
  
[Structure of the PLC tag tables](#structure-of-the-plc-tag-tables)
  
[Declaring PLC tags](#declaring-plc-tags-1)
  
[Declaring global constants](#declaring-global-constants)
  
[Exporting and importing PLC tags](#exporting-and-importing-plc-tags)

### Opening the PLC tag tables

#### Procedure

To open the PLC tag table in a CPU, proceed as follows:

1. Open the "PLC tags" folder under the CPU in the project tree.
2. Double-click the PLC tag table in the folder.
3. Select the desired tab in the upper corner.

#### Result

The PLC tag table associated with the CPU opens. You can declare the required tags and constants.

---

**See also**

[Overview of PLC tag tables](#overview-of-plc-tag-tables)
  
[Structure of the PLC tag tables](#structure-of-the-plc-tag-tables)
  
[Declaring PLC tags](#declaring-plc-tags-1)
  
[Declaring global constants](#declaring-global-constants)

### Copying or moving PLC tag tables

#### Copying PLC tag tables

To copy PLC tag tables, follow these steps:

1. Select the PLC tag table you want to copy.
2. Select the "Copy" command in the shortcut menu.
3. Position the cursor at the location where you want to insert the PLC tag table.

   You can insert the PLC tag table into the same software unit or into a different software unit or outside a software unit into the "PLC tags" folder of a CPU.
4. Select the "Paste" command in the shortcut menu.

   - If you paste the PLC tag table into the same CPU, the copy is pasted with the name extension "_&lt;consecutive number&gt;".
   - If you paste the PLC tag table into a different CPU where a PLC tag table of the same name already exists, the "Paste" dialog box opens. Select the desired option and confirm your selection with "OK".

Alternatively, you can also copy the PLC tag table via drag-and-drop while holding down the &lt;Ctrl&gt; key.

#### Moving PLC tag tables

To move tag tables, follow these steps:

1. Select the PLC tag table you want to move.
2. Drag the PLC tag table to the new position.

### Grouping PLC tag tables

You can gather the user-defined tag tables of the CPU into groups. You cannot, however, move the standard tag table and the "All tags" table into a group.

#### Requirement

Multiple user-defined tag tables are contained in the "PLC tags" folder of the CPU.

#### Procedure

To gather multiple PLC tag tables into a group, follow these steps:

1. Select the "PLC tags" folder under the CPU in the project tree.
2. Select the "Insert &gt; Group" menu command.

   A new group with the standard name "Group_x" is inserted.
3. Select the newly inserted group in the project tree.
4. Select the "Rename" command in the shortcut menu.
5. Assign the new group a unique name throughout the CPU.
6. Drag to the new group the tables you want to group together.

#### Result

The tag tables are gathered in the new group.

---

**See also**

[Overview of PLC tag tables](#overview-of-plc-tag-tables)
  
[Structure of the PLC tag tables](#structure-of-the-plc-tag-tables)
  
[Declaring PLC tags](#declaring-plc-tags-1)
  
[Declaring global constants](#declaring-global-constants)

## Declaring PLC tags

This section contains information on the following topics:

- [Entering a PLC tag declaration](#entering-a-plc-tag-declaration)
- [Setting the retentivity of PLC tags](#setting-the-retentivity-of-plc-tags)

### Entering a PLC tag declaration

This section contains information on the following topics:

- [Declaring tags in the PLC tag table](#declaring-tags-in-the-plc-tag-table)
- [Declaring PLC tags in the program editor](#declaring-plc-tags-in-the-program-editor)
- [Declare PLC tags using drag-and-drop](#declare-plc-tags-using-drag-and-drop)

#### Declaring tags in the PLC tag table

##### Requirement

The "Tags" tab of the PLC tag table is open.

##### Procedure

To define PLC tags, follow these steps:

1. Enter a tag name in the "Name" column.
2. Enter the required data type in the "Data type" column. You will be supported by autocompletion during input.

   An address corresponding to the data type is automatically appended.
3. Optional: Click on the arrow key in the "Address" column and enter an operand identifier, an operand type, an address and a bit number in the dialog which then opens.
4. Optional: Disable the options for HMI and OPC UA.
5. Optional: Enter a comment in the "Comments" column.
6. Repeat steps 1 - 5 for all the required tags.

   See also: [Rules for PLC tags](#rules-for-plc-tags)

##### Syntax check

A syntax check is performed automatically after each entry, and any errors found are displayed in red. You do not have to correct these errors immediately - you can continue editing and make any corrections later. As long as the tag declaration contains syntax errors and the tag is used in the program, you will not be able to compile the program.

---

**See also**

[Declare PLC tags using drag-and-drop](#declare-plc-tags-using-drag-and-drop)
  
[Exporting and importing PLC tags](#exporting-and-importing-plc-tags)
  
[Using autocompletion](Program%20editor.md#using-autocompletion)
  
[Declaring PLC tags in the program editor](#declaring-plc-tags-in-the-program-editor)
  
[Editing PLC tag tables](#editing-plc-tag-tables)
  
[Structure of the PLC tag tables](#structure-of-the-plc-tag-tables)
  
[Editing tables](Introduction%20to%20the%20TIA%20Portal.md#editing-tables)

#### Declaring PLC tags in the program editor

##### Requirement

- The program editor is open.

##### Procedure

To declare operands as global PLC tags, follow these steps:

1. Insert an instruction in your program.

   The "&lt;???&gt;", "&lt;??.?&gt;" or "..." strings represent operand placeholders.
2. Replace an operand placeholder with the name of the PLC tag to be created.
3. Select the tag name.

   If you want to declare multiple PLC tags, select the names of all the tags to be declared.
4. Select the "Define tag" command in the shortcut menu.

   The "Define tag" dialog box opens. This dialog displays a declaration table in which the name of the tag is already entered.
5. Click the arrow key in the "Section" column and select one of the following entries:

   - Global Memory
   - Global Input
   - Global Output
   - Global Timer
   - Global Counter
6. In the other columns, enter the address, data type, and comments.

   See also: [Rules for PLC tags](#rules-for-plc-tags)
7. If the CPU contains multiple PLC tag tables, you can use an entry in the "PLC tag table" column to indicate in which table the tag is to be inserted. If you make no entry in the column, the new tag will be inserted in the default tag table.
8. Click the "Define" button to complete your entry.

##### Result

The tag declaration is written to the PLC tag table and is valid for all blocks in the CPU.

---

**See also**

[Declare PLC tags using drag-and-drop](#declare-plc-tags-using-drag-and-drop)
  
[Declaring tags in the PLC tag table](#declaring-tags-in-the-plc-tag-table)
  
[Using autocompletion](Program%20editor.md#using-autocompletion)
  
[Editing tables](Introduction%20to%20the%20TIA%20Portal.md#editing-tables)

#### Declare PLC tags using drag-and-drop

##### Requirement

- The program editor is open.
- A PLC tag table is open.

##### Procedure

To declare operands as global PLC tags, follow these steps:

1. Insert an instruction in your program.

   The "&lt;???&gt;", "&lt;??.?&gt;" or "..." strings represent operand placeholders.
2. Replace an operand placeholder with the name of the PLC tag to be created.
3. Select the tag name.

   If you want to declare multiple PLC tags, select the names of all the tags to be declared.
4. Drag the tags to the PLC tag table.
5. In the other columns, enter the address, data type, and comments.

   See also: [Rules for PLC tags](#rules-for-plc-tags)

##### Result

The tag declaration is written to the PLC tag table and is valid for all blocks in the CPU.

---

**See also**

[Editing tables](Introduction%20to%20the%20TIA%20Portal.md#editing-tables)
  
[Declaring tags in the PLC tag table](#declaring-tags-in-the-plc-tag-table)
  
[Using autocompletion](Program%20editor.md#using-autocompletion)

### Setting the retentivity of PLC tags

This section contains information on the following topics:

- [Retentive behavior of PLC tags](#retentive-behavior-of-plc-tags)
- [Setting the retentive behavior of PLC tags (S7-1200, S7-1500)](#setting-the-retentive-behavior-of-plc-tags-s7-1200-s7-1500)
- [Setting the retentive behavior of PLC tags (S7-300, S7-400)](#setting-the-retentive-behavior-of-plc-tags-s7-300-s7-400)

#### Retentive behavior of PLC tags

##### Retentive PLC tags

Each CPU has a memory area whose content remains available even after the supply voltage has been switched off. This area is referred to as retentive memory area.

To avoid data loss during power failure, you can save specific PLC tags to this memory area. You make the retentivity setting of PLC tags in the PLC tag table (S7-1200/S7-1500) or in the CPU properties (S7-300/S7-400).

Depending on the CPU family, the retentive memory area can accommodate various type of PLC tags. The following table provides an overview of the options of the various CPUs:

| CPU type | Retentive bit memories | Retentive SIMATIC timers | Retentive SIMATIC counters |
| --- | --- | --- | --- |
| S7-300/400 series | ✓ | ✓ | ✓ |
| S7-1200 series | ✓ | - | - |
| S7-1500 series | ✓ | ✓ | ✓ |

---

**See also**

[Setting the retentive behavior of PLC tags (S7-1200, S7-1500)](#setting-the-retentive-behavior-of-plc-tags-s7-1200-s7-1500)
  
[Setting the retentive behavior of PLC tags (S7-300, S7-400)](#setting-the-retentive-behavior-of-plc-tags-s7-300-s7-400)

#### Setting the retentive behavior of PLC tags (S7-1200, S7-1500)

##### Introduction

You set the retentivity for PLC tags in the PLC tag table for the S7-1200/S7-1500 CPU series. You can recognize the retentivity setting of a tag by the check mark set in the "Retain" column of the PLC tag table.

##### Requirement

The "PLC tags" tab of the PLC tag table is open.

##### Procedure

To define the width of the retentive memory area for PLC tags of CPU S7-1200/S7-1500, follow these steps:

1. On the toolbar, click the "Retain" button.

   The "Retain memory" dialog will open.
2. Set the width of the retentive memory area.

   - Enter the number of retentive memory bytes.

     Example: If you enter "2", memory bytes MB 0 and MB 1 are retentive.
   - Enter the number of retentive timers. Each S7 timer occupies two bytes.

     Example: If you enter "2", S7 timers T 0 and T 1 are retentive.
   - Enter the number of retentive counters. Each S7 counter occupies two bytes.
   - Example: If you enter "2", S7 counters C 0 and C 1 are retentive.
3. Click the "OK" button.

##### Result

The width if the retentive memory area is defined. All tags with addresses in this memory area are then designated retentive. In the "Retain" column of the tag table a check mark is automatically set for all tags that are located within the retentive memory area.

---

**See also**

[Retentive behavior of PLC tags](#retentive-behavior-of-plc-tags)
  
[Editing tables](Introduction%20to%20the%20TIA%20Portal.md#editing-tables)

#### Setting the retentive behavior of PLC tags (S7-300, S7-400)

##### Introduction

You set the retentivity for PLC tags in the CPU settings for the S7-300/400 CPU series.

##### Procedure

To define the width of the retentive memory area for PLC tags of CPU S7-300/400, follow these steps:

1. Select the CPU in project tree.
2. Select the "Properties" menu command.
3. Select the section "Retentivity".

   - Enter the number of retentive memory bytes.

     Example: If you enter "2", memory bytes MB 0 and MB 1 are retentive.
   - Enter the number of retentive timers. Each S7 timer occupies two bytes.

     Example: If you enter "2", S7 timers T 0 and T 1 are retentive.
   - Enter the number of retentive counters. Each S7 counter occupies two bytes.

     Example: If you enter "2", S7 counters C 0 and C 1 are retentive.

##### Result

The width if the retentive memory area is defined. All tags within this memory area are then declared retentive.

---

**See also**

[Retentive behavior of PLC tags](#retentive-behavior-of-plc-tags)

## Grouping PLC tags for inputs and outputs in structures

This section contains information on the following topics:

- [Other useful information regarding structured PLC tags](#other-useful-information-regarding-structured-plc-tags)
- [Creating structured PLC tags](#creating-structured-plc-tags)

### Other useful information regarding structured PLC tags

#### Use of structured PLC tags (S7-1200 V4 and higher/S7-1500)

To make your program easier to view, you can group several input or output addresses in a higher-level PLC tag. The higher-level PLC tag represents a structure that contains several logically related inputs or outputs. When the block is called, you transfer the higher-level tag and thus need only an input or output parameter for all associated inputs or outputs.

#### Principle of operation

To create a structured PLC tag, you initially define a PLC data type (UDT). In it you declare the necessary data elements and specify their names and data types.

Then, you switch to the PLC tag table and specify the higher-level PLC tag there. As a data type for the tag, you select your PLC data types. The system now reserves a certain number of input or output addresses starting from the start address of the higher-level tag. The number of reserved addresses depends on the length of your PLC data type.

If you call a block that requires the reserved inputs or outputs for program execution, you transfer the higher-level tag as a block parameter.

You can address the individual PLC tags like structure elements in the program code.

A detailed description of the individual handling steps can be found in the following chapters.

#### Application example

You can use structured PLC tags in order to group the inputs or outputs of a function module. The following figure shows the schematic representation of a motor: A component was created in the "Datatype_Motor" PLC data type for each of the three inputs.

The memory areas of the declared tags must not overlap. In the example, you see that the "Speed" component has the data type "Integer" and therefore must start at a word address. For this reason, the first input word has been filled with the "Dummy" fill tag. This means that "Speed" is located on the second input word.

![Application example](images/52803705611_DV_resource.Stream@PNG-en-US.png)

The following figure shows the higher-level "Motor" PLC tag that is based on the "Data type_Motor" data type. With the declaration of "Motor", the addresses IW0 and IW1 are reserved on the input module.

![Application example](images/52826265355_DV_resource.Stream@PNG-en-US.png)

The following figure shows the transfer of the "Motor" PLC tag as an input parameter of the "Motor_Control" block.

![Application example](images/52826269067_DV_resource.Stream@PNG-de-DE.png)

You can address the individual components of the tag in the "Motor_Control" block.

| Addressing | Description |
| --- | --- |
| "Motor" | Addressing the higher-level PLC tag. |
| "Motor".On | Addressing a component of a structured PLC tag. |
| "Motor".On:P | Addressing an I/O input or output (PI or PQ). |

#### Rules for use of structured PLC tags

Note the following rules when creating and using structured PLC tags.

- Structured PLC tags can be used in the "Inputs" and "Outputs" operand areas.
- Structured tags are not permitted in the bit memory address area.
- For the declaration of the PLC tag table keep in mind that the memory areas of the structured PLC tags must not be overlapped by other tags. A structured PLC tag requires a memory area of at least 2 bytes or a multiple of 2 bytes (4 bytes, 6 bytes, 8 bytes, etc.).
- Structured PLC tags cannot be addressed from HMI.

Observe the following rules when creating the PLC data type that is to serve as the basis for a PLC tag:

- The memory areas of the individual elements must not overlap.

  See also: [Permissible addresses and data types of PLC tags](#permissible-addresses-and-data-types-of-plc-tags)
- Do not group inputs and outputs in one PLC data type but create different PLC data types for inputs and outputs.
- Do not group inputs or outputs from different modules in a PLC data type because it is not guaranteed that the process images of the modules are updated synchronously.
- In the lower-level PLC data types, all data types are permitted except for "STRING" and "WSTRING".

---

**See also**

[Creating structured PLC tags](#creating-structured-plc-tags)
  
[Inspector window: Displaying UDTs](Configuring%20devices%20and%20networks.md#inspector-window-displaying-udts)
  
[Addressing PLC tags](Programming%20basics.md#addressing-plc-tags)

### Creating structured PLC tags

#### Rules

Note the following rules when creating structured PLC tags:

- Use separate PLC data types for the "Inputs" and "Outputs" operand areas.
- Structured tags are not permitted in the bit memory address area.
- Do not group inputs or outputs from different modules in a PLC data type because it is not guaranteed that the process images of the modules are updated synchronously.

#### Procedure

To create a structured PLC tag, follow these steps:

1. Double-click the "Add new data type" command in the "PLC data types" folder in the project tree.

   A new declaration table for creating a PLC data type will be created and opened.
2. Declare all the necessary components in the PLC type. All data types except for "STRING" and "WSTRING" are permitted.
3. Select the PLC data type in the project tree and select the "Compile &gt; Software (only changes)" command from the shortcut menu.

   The PLC data type is compiled and can then be used in the PLC tag table.

   Even when you make changes to existing PLC data types, you must recompile the program. This updates all locations of use of the PLC data type.
4. Open a PLC tag table within the same CPU.
5. Declare a new tag or select an existing tag.
6. In the "Data type" column, select the PLC data type and assign it to the PLC tag.

   The PLC tag receives the structure of the PLC data type. A suitable address is assigned automatically. Structured PLC tags always start at word addresses.

   The highest structure element is displayed without its subelements in the table.

> **Note**
>
> **Assignment rules and default values**
>
> - For the declaration of the PLC data type, note that the memory areas of the individual tags must not overlap. For example, tags of data type "Integer" must start at a word limit. If necessary, insert "fill tags" to prevent overlaps.
>
>   See also: [Permissible addresses and data types of PLC tags](#permissible-addresses-and-data-types-of-plc-tags)
> - It is not possible to assign default values for the individual components. Values that you enter in the "Default value" column are not evaluated. Tags of data types "DT" and "DTL" may therefore contain invalid values.

---

**See also**

[Other useful information regarding structured PLC tags](#other-useful-information-regarding-structured-plc-tags)
  
[Inspector window: Displaying UDTs](Configuring%20devices%20and%20networks.md#inspector-window-displaying-udts)
  
[Basic principles for programming of data blocks](Programming%20data%20blocks.md#basic-principles-for-programming-of-data-blocks)
  
[Structure of the declaration table for PLC data types](Declaring%20PLC%20data%20types%20%28UDT%29.md#structure-of-the-declaration-table-for-plc-data-types)
  
[Addressing PLC tags](Programming%20basics.md#addressing-plc-tags)
  
[Declaring PLC tags](#declaring-plc-tags-1)

## Declaring global constants

This section contains information on the following topics:

- [Rules for global user constants](#rules-for-global-user-constants)
- [Rules for global system constants](#rules-for-global-system-constants)
- [Declaring global constants](#declaring-global-constants-1)

### Rules for global user constants

#### Permitted characters

Names of global constants may consist of the following characters:

- Letters, numbers, special characters are permitted.
- Quotation marks are not permitted.

#### Unique constant names

The names of global constants must be unique throughout the CPU, even if the constants are located in different tag tables of a CPU. A name that is already used for a block, a PLC tag or another constant within the CPU, cannot be used for new constant. The uniqueness check does not differentiate between use of small and capital letters.

If you enter an already assigned name another time, a sequential number is automatically appended to the second name entered. For example, if you enter the name "Motor" a second time, the second entry is changed to "Motor(1)".

#### Permitted data types

For constants, all data types supported by the CPU are permitted, with the exception of structured data types.

#### Permitted values

You can select any value from the value range of the specified data type as constant value. For information on the value ranges, refer to the "Data types" chapter.

See also: [Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)

---

**See also**

[Basics of constants](Programming%20basics.md#basics-of-constants)
  
[Declaring global constants](#declaring-global-constants-1)
  
[Constants](Programming%20basics.md#constants)

### Rules for global system constants

#### Definition

System constants are global constants, unique throughout the CPU, that are required and automatically created by the system. System constants can, for example, be used to address and identify hardware objects.

#### Rules

System constants are assigned automatically when components are inserted in the device or network view, and entered in the default tag table ("System constants" tab). A system constant is created for each module, but also for each submodule. An integrated counter, for example, therefore receives a system constant as well. System constants consist of a symbolic name and a numeric HW identifier and cannot be changed.

#### Names of system constants

The names of the system constants are structured hierarchically. They consist of a maximum of four hierarchical levels, each of which is separated by a tilde "~". Based on the name, you can therefore recognize the "path" to the relevant hardware module.

#### Example

A system constant with the name "`Local~PROFINET_interface_1~Port_1`" designates Port 1 of the PROFINET interface 1 of the local CPU.

---

**See also**

[What you need to know about HW identifiers (S7-1200, S7-1500, S7-1500T)](Configuring%20automation%20systems.md#what-you-need-to-know-about-hw-identifiers-s7-1200-s7-1500-s7-1500t)
  
[Instructions for address conversion (S7-1200, S7-1500)](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#instructions-for-address-conversion-s7-1200-s7-1500)
  
[Example for the use of hardware identifiers (S7-1200, S7-1500, S7-1500T)](Configuring%20automation%20systems.md#example-for-the-use-of-hardware-identifiers-s7-1200-s7-1500-s7-1500t)

### Declaring global constants

#### Introduction

You declare constants in the "User constants" tab of a PLC tag table. During declaration you have to to enter a symbolic name, a data type and a fixed value for each constant. You can select any value from the value range of the specified data type as constant value. For information on the value ranges, refer to the "Data types" chapter.

See also: [Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)

#### Procedure

To declare constants, follow these steps:

1. Open a PLC tag table.
2. Open the "User constants" tab.

   The constants table opens.
3. Enter a constant name in the "Name" column.
4. Enter the required data type in the "Data type" column. You will be supported by autocompletion during input.
5. Enter a constant value in the "Value" column; this constant value must be valid for the selected data type.
6. If you want, enter comments on the constants in the "Comments" column. The entry of a comment is optional.
7. If you want to declare additional constants, place the cursor in the next row and repeat steps 3 to 6.

#### Syntax check

A syntax check is performed automatically after each entry, and any errors found are displayed in red. You do not have to correct these errors immediately - you can continue editing and make any corrections later. As long as the tag declaration contains syntax errors and the constant is used in the program, you will not be able to compile the program.

---

**See also**

[Opening the PLC tag tables](#opening-the-plc-tag-tables)
  
[Inserting a table row in the PLC tag table](#inserting-a-table-row-in-the-plc-tag-table)
  
[Structure of the PLC tag tables](#structure-of-the-plc-tag-tables)
  
[Rules for global user constants](#rules-for-global-user-constants)
  
[Editing tables](Introduction%20to%20the%20TIA%20Portal.md#editing-tables)
  
[Using autocompletion](Program%20editor.md#using-autocompletion)
  
[Constants](Programming%20basics.md#constants)

## Editing properties

This section contains information on the following topics:

- [Editing the properties of PLC tags](#editing-the-properties-of-plc-tags)
- [Editing properties of global constants](#editing-properties-of-global-constants)
- [Editing the properties of PLC tag tables](#editing-the-properties-of-plc-tag-tables)
- [Editing multilingual comments in the PLC tag table (S7-1500)](#editing-multilingual-comments-in-the-plc-tag-table-s7-1500)

### Editing the properties of PLC tags

This section contains information on the following topics:

- [Properties of PLC tags](#properties-of-plc-tags)
- [Editing the properties of PLC tags](#editing-the-properties-of-plc-tags-1)

#### Properties of PLC tags

##### Overview

The following table provides an overview of the properties of PLC tags. The display of properties can vary depending on the CPU type.

| Group | Property | Description |
| --- | --- | --- |
| General | Name | A unique name within the CPU. |
| Data type | Data type of the tags. |  |
| Address | Tag address. |  |
| Retain | Shows the retain setting of the tag. |  |
| Comment | Comment on the tag. |  |
| History | Date created | Time when the tag was created (cannot be changed). |
| Last modified | Time when the tag was last changed (cannot be changed). |  |
| Application | Visible in HMI engineering | Shows whether the tag is visible by default in the HMI selection list. |
| Accessible from HMI/OPC UA/Web API | Indicates whether HMI/OPC UA/Web API can access this variable during runtime. |  |
| Writable from HMI/OPC UA/Web API | Indicates whether or not the tag can be written from HMI/OPC UA/Web API during runtime. |  |

---

**See also**

[Editing the properties of PLC tags](#editing-the-properties-of-plc-tags-1)

#### Editing the properties of PLC tags

##### Editing properties in a PLC tag table

To edit the properties of one or more tags, follow these steps:

1. In the project tree, double-click the PLC tag table that contains the tags.

   The PLC tag table opens.
2. Change the entries in the columns.

##### Editing addresses in the program editor

To edit the address of a tag in the program editor, follow these steps:

1. Select the tag name.
2. Select the "Rewire tag" command in the shortcut menu.

   The "Rewire tag" dialog will open. The dialog shows a declaration table.
3. Enter the new address in the "Address" column.
4. Click the "Change" button to confirm the input.

##### Editing names in the program editor

To edit the name of a tag in the program editor, follow these steps:

1. Select the tag name.
2. Select the "Rename tag" command in the shortcut menu.

   The "Rename tag" dialog opens. The dialog shows a declaration table.
3. Enter the new name in the "Name" column.
4. Click the "Change" button to confirm the input.

##### Effect in the program

In the case of a change of the tag's name, data type or address, each location of use of the tag is automatically updated in the program.

---

**See also**

[Properties of PLC tags](#properties-of-plc-tags)

### Editing properties of global constants

This section contains information on the following topics:

- [Properties of global constants](#properties-of-global-constants)
- [Editing properties of global constants](#editing-properties-of-global-constants-1)

#### Properties of global constants

##### Overview

The following table gives an overview of the properties of constants:

| Group | Property | Description |
| --- | --- | --- |
| General | Name | A unique name within the table |
| Data type | Data type of the constants |  |
| Value | Value that you defined for the constants.   This value must be compatible with the declared data type.   See also: [Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types) |  |
| Comment | Comment on the constants |  |
| History | Date created | Time when the constant was created (cannot be changed) |
| Last modified | Time when the constant was last changed (cannot be changed) |  |

#### Editing properties of global constants

##### Editing properties in a PLC tag table

To edit the properties of one or more constants, follow these steps:

1. In the project tree, double-click the PLC tag table that contains the constants.

   The PLC tag table opens.
2. Open the "User constants" tab.
3. Change the entries in the "Name", "Data type", "Value", or "Comments" column.

##### Effect in the program

In the case of a change of a constant's name, data type or value, each location of use of the constant is automatically updated in the program.

---

**See also**

[Editing tables](Introduction%20to%20the%20TIA%20Portal.md#editing-tables)

### Editing the properties of PLC tag tables

This section contains information on the following topics:

- [Properties of PLC tag tables](#properties-of-plc-tag-tables)
- [Editing the properties of PLC tag tables](#editing-the-properties-of-plc-tag-tables-1)

#### Properties of PLC tag tables

##### Overview

The following table provides an overview of the properties of PLC tag tables.

| Group | Property | Description |
| --- | --- | --- |
| General | Name | A unique name within the CPU. |
| Access | Only for PLC tag tables in software units:  Indicates whether the tags and constants of this PLC tag table can also be accessed from other software units. |  |

---

**See also**

[Editing the properties of PLC tag tables](#editing-the-properties-of-plc-tag-tables-1)

#### Editing the properties of PLC tag tables

##### Editing properties of a PLC tag table

To edit the properties of a PLC tag table, follow these steps:

1. Select the PLC tag table in the project tree.
2. Select the "Properties" command in the shortcut menu.

   The "Properties" dialog opens.
3. Change the properties of the PLC tag table.

---

**See also**

[Properties of PLC tag tables](#properties-of-plc-tag-tables)

### Editing multilingual comments in the PLC tag table (S7-1500)

You can edit the comments from a PLC tag table in all project languages that you have activated in the project language settings. You can find additional information on activating project languages under [Select project languages](Editing%20project%20data.md#select-project-languages).

Note that the texts must not exceed a length of 32767 Unicode characters even after translation.

#### Requirement

- You have activated multiple project languages.
- A PLC tag table is open and it contains at least one comment.
- The block does not have know-how protection.

#### Procedure

To edit a comment in all project languages, follow these steps:

1. Click on the comment whose translation you want to edit.

   If you want to edit the translations of several comments at the same time, select all the desired comments.

   Comments of a PLC data type (UDT) cannot be selected in the PLC tag table. You can only edit these comments in the PLC data type itself.
2. Open the "Properties" tab in the Inspector window.
3. Open the "Texts" tab.

   The "Texts" tab displays the selected comments in the active project languages and, if available, the translations of the comments.
4. You can edit the translations directly in the table in the "Texts" tab.
5. To edit the translations with an external editor, you can export the displayed texts to OOXML format using the "Export/Import project texts" buttons.

> **Note**
>
> **Editing all project texts in the global "Project texts" table**
>
> You can also edit the translations for the individual project languages in the global "Project texts" table. You can find the table in the project tree under "Languages &amp; Resources &gt; Project texts". It contains all translatable texts of the entire project.
>
> You can find additional information on translation of texts under [Project text basics](Editing%20project%20data.md#project-text-basics).​

## Monitoring of PLC tags

This section contains information on the following topics:

- [Monitoring of PLC tags](#monitoring-of-plc-tags-1)

### Monitoring of PLC tags

You can monitor the current data values of the tags on the CPU directly in the PLC tag table.

#### Requirement

An online connection to the CPU exists or is possible.

#### Procedure

To monitor the data values, proceed as follows:

1. Open a PLC tag table.
2. Start monitoring by clicking the "Monitor all" button.

   - If no online connection to the CPU exists, this is established.
   - Monitoring is started with the trigger setting "Permanent".
   - The additional "Monitor value" column is displayed in the table. This shows the current data values.
   - The symbol for the forcing of tags is displayed if a tag is currently being forced.
3. End the monitoring by clicking the "Monitor all" button again.

> **Note**
>
> **Editing PLC tags during the monitoring of tags**
>
> If the editing of tags is started and the PLC tag table is edited, for example by adding new tags, the monitoring is re-started after editing is complete.

> **Note**
>
> You also have the option of copying PLC tags to a monitor or force table so that you can monitor, control or force them in the table.

---

**See also**

[Structure of the PLC tag tables](#structure-of-the-plc-tag-tables)
  
[Introduction to testing with the watch table](Testing%20with%20the%20watch%20table.md#introduction-to-testing-with-the-watch-table)
  
[Introduction for testing with the force table](Testing%20with%20the%20force%20table.md#introduction-for-testing-with-the-force-table)
  
[Copying entries in the PLC tag table](#copying-entries-in-the-plc-tag-table)

## Editing PLC tag tables

This section contains information on the following topics:

- [Inserting a table row in the PLC tag table](#inserting-a-table-row-in-the-plc-tag-table)
- [Copying entries in the PLC tag table](#copying-entries-in-the-plc-tag-table)
- [Deleting entries in the PLC tag table](#deleting-entries-in-the-plc-tag-table)
- [Filtering entries in the PLC tag table](#filtering-entries-in-the-plc-tag-table)
- [Sorting rows in the PLC tag tables](#sorting-rows-in-the-plc-tag-tables)
- [Automatically filling in cells in the PLC tag table](#automatically-filling-in-cells-in-the-plc-tag-table)
- [Navigate to the device view](#navigate-to-the-device-view)
- [Navigate to definitions](#navigate-to-definitions)
- [Show and hide table columns](#show-and-hide-table-columns)
- [Exporting and importing PLC tags](#exporting-and-importing-plc-tags)

### Inserting a table row in the PLC tag table

#### Procedure

Proceed as follows to insert a row above the selected row:

1. Select the row in front of which you want to insert a new row.
2. Click the "Insert row" button on the toolbar of the table.

#### Result

A new row is inserted above the selected row.

---

**See also**

[Editing tables](Introduction%20to%20the%20TIA%20Portal.md#editing-tables)

### Copying entries in the PLC tag table

You can copy PLC tags within a table or to other tables.

#### Procedure

To copy a tag, follow these steps:

1. Select the tags you want to copy.

   You can also select several tags by clicking on them one after the other while holding down the &lt;Ctrl&gt; key or by pressing and holding down &lt;Shift&gt; and clicking on the first and last tag.
2. Select "Copy" in the shortcut menu.
3. Position the insertion pointer at the location where you want to insert the tags.
4. Select "Paste" in the shortcut menu.

Or

1. Select the tag.
2. Hold down the left mouse button.
3. At the same time, press &lt;Ctrl&gt;.
4. Drag the tag to the destination.

#### Result

- The tag is copied to the destination.
- If there is a name conflict, a number is automatically appended to the tag name. For example, "Tag" becomes "Tag(1)".
- All other properties of the tag remain unchanged.

---

**See also**

[Editing tables](Introduction%20to%20the%20TIA%20Portal.md#editing-tables)

### Deleting entries in the PLC tag table

#### Procedure

To delete a tag, follow these steps:

1. Select the row with the tag to be deleted. You can also select several rows by clicking on them one after the other while holding down the &lt;Ctrl&gt; key or by pressing and holding down &lt;Shift&gt; and clicking on the first and last row.
2. Select the "Delete" command in the shortcut menu.

---

**See also**

[Editing tables](Introduction%20to%20the%20TIA%20Portal.md#editing-tables)

### Filtering entries in the PLC tag table

#### Introduction

In the filter view, you define filter criteria for PLC tag tables to simplify targeted searching and replacing of PLC tags and global constants.

You have the following filter criteria:

- Name
- Data type
- Address
- Comment

The filter criteria can be combined.

The settings are text-based. You enter a character or a character string as the filter setting. The filter result includes all entries that contain the character or character string anywhere in the name, data type, address or comment. No distinction is made between upper and lower case in the filter setting.

The following figure shows the filter view of the PLC tag table. The entries are filtered by address and comment.

The filter result includes all PLC tags that meet the following filter settings:

- The address contains the character "Q":
- The comment contains the string "barrier".

![Introduction](images/171630450059_DV_resource.Stream@PNG-en-US.png)

#### Filtering the PLC tag table

To filter a PLC tag table, follow these steps:

1. Open the PLC tag table.
2. Click the symbol "Open filter view".

   The PLC tag table opens in the filter view. It contains a filter row below the column headers.
3. Enter the desired filter setting in the filter row or select a previous filter setting from the drop-down list.

   The filter settings are applied to the PLC tag table.

   You can now use the "Find and Replace" function to search for or replace text within the filtered entries.

#### Declaring new entries while the filter view is open.

To declare new entries while the filter view is open, follow these steps:

1. Switch to the standard view of the PLC tag table.
2. Declare the new entries.
3. Switch back to the filter view.
4. Click the "Update" symbol.

   The new entries are displayed in the filter view if they match the current filter settings.

> **Note**
>
> **Declaring new entries in the filter view**
>
> When declaring new entries in the filter view, no syntax check is performed. Incorrect inputs are therefore not marked in red. Check the syntax of your input in the standard view of the PLC tag table.

---

**See also**

[Find and replace](Introduction%20to%20the%20TIA%20Portal.md#find-and-replace)

### Sorting rows in the PLC tag tables

You can sort the rows in the tables alphanumerically by name, data type, or address.

#### Procedure

To sort the table rows, follow these steps:

1. Select the column by which you want to sort.
2. Click the column header.

   The column will be sorted in order of increasing values.

   An up arrow shows the sort sequence.
3. In order to change the sort sequence, click the arrow.

   The column will be sorted in order of decreasing values. A down arrow shows the sort sequence.
4. To restore the original sequence, click a third time on the column header.

---

**See also**

[Editing tables](Introduction%20to%20the%20TIA%20Portal.md#editing-tables)

### Automatically filling in cells in the PLC tag table

You can load the contents of one or several table cells into the cells below, automatically filling in the successive cells.

If you automatically fill in cells in the "Name" column, a consecutive number will be appended to each name. For example, "Motor" will become "Motor_1".

If you fill the cells in the column "Address" automatically, the addresses will be increased depending on the indicated data type.

#### Procedure

To automatically fill in successive cells, follow these steps:

1. Select the cells to be loaded.
2. Click the "Fill" symbol in the bottom right corner of the cell.

   The mouse pointer is transformed into a crosshair.
3. Keep the mouse button pressed and drag the mouse pointer downwards over the cells that you want to fill in automatically.
4. Release the mouse button.

   The cells are filled in automatically. If entries are already present in the cells that are to be automatically updated, a dialog appears in which you can indicate whether you want to overwrite the existing entries or whether you want to insert new rows for the new tags.

---

**See also**

[Editing tables](Introduction%20to%20the%20TIA%20Portal.md#editing-tables)

### Navigate to the device view

You can navigate from a PLC tag table to the device and network editor and display the configured input or output in the device view.

#### Requirements

- The tag is declared as input or output in a PLC tag table.
- An input or output group is configured in the hardware and network editor.

#### Procedure

To display a PLC tag in the device view, follow these steps:

1. Select the tag in the PLC tag table.
2. Select the shortcut menu command "Go to device view".

The device and network editor is opened and the input or output for which the tag was declared is displayed.

---

**See also**

Overview of hardware and network editor

### Navigate to definitions

You can use PLC data types (UDT) in a PLC tag table. To view the definition of the PLC data type, you can specifically navigate to the location of the definition.

#### Procedure

To navigate to the definition of a PLC data type, follow these steps:

1. Right-click a PLC tag that is based on a PLC data type.
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

---

**See also**

[Editing tables](Introduction%20to%20the%20TIA%20Portal.md#editing-tables)

### Exporting and importing PLC tags

This section contains information on the following topics:

- [Basics for exporting and importing PLC tags](#basics-for-exporting-and-importing-plc-tags)
- [Format of the export file (*.xlsx)](#format-of-the-export-file-xlsx)
- [Format of the export file (*.xml)](#format-of-the-export-file-xml)
- [Format of the export file (*.sdf)](#format-of-the-export-file-sdf)
- [Exporting PLC tags](#exporting-plc-tags)
- [Importing PLC tags](#importing-plc-tags)
- [Editing individual PLC tags with external editors](#editing-individual-plc-tags-with-external-editors)

#### Basics for exporting and importing PLC tags

##### Introduction

You can export PLC tag tables to edit them further with external applications. Similarly, you can import PLC tag tables edited externally to the TIA Portal.

The following formats are supported for import and export:

- XLSX (Excel)
- XML
- SDF

For the export you can specify which elements you want to export:

- Tags and/or constants
- All elements or just the elements that are actually being used in the program on the current CPU.

##### Overwriting existing PLC tags and constants during import

During import, PLC tags and constants are synchronized by name per default. This means existing elements are overwritten if they have the same name as the PLC tags or constants to be imported.

However, you can also synchronize the tags by addresses.

##### Link to existing objects

References to PLC tags or constants that already exist in the project are updated automatically during import. The update is executed based on the name of the PLC tags and constants.

##### Export of PLC data types (UDT)

It is not possible to export structured PLC tags based on a PLC data type for subsequent editing. The export file contains only the higher-level PLC tag. The individual elements of the PLC data type cannot be edited.

---

**See also**

[Exporting PLC tags](#exporting-plc-tags)
  
[Importing PLC tags](#importing-plc-tags)
  
[Format of the export file (*.xlsx)](#format-of-the-export-file-xlsx)
  
[Format of the export file (*.xml)](#format-of-the-export-file-xml)
  
[Format of the export file (*.sdf)](#format-of-the-export-file-sdf)

#### Format of the export file (*.xlsx)

##### Introduction

During the export of PLC tag tables, a standardized XSLX format will be generated that you can edit with external table editors.

This format is also expected during the import of tables.

The export file contains two sheets:

- The name of the first sheet is "PLCTags".
- The name of the second sheet is "TagTableProperties".

##### Format of the sheet "PLCTags"

This sheet can contain the displayed columns and any other columns that may be used internally.

When you create an *.xlsx file with an external editor, it must contain all or a subset of the displayed columns. It must not contain any other self-defined columns. The sorting order of columns can vary.

The column titles are predefined and are always expected to be in English.

The following table specifies the values expected for the individual columns. During import, missing values will be identified by a &lt;no value&gt; entry.

| Element | Description |
| --- | --- |
| Name | Name of the tags |
| Path | Group and name of the PLC tag table |
| Data Type | The notation of the data type corresponds to the notation used in the PLC tag table. |
| Logical Address | The address can be specified with German or international mnemonics. |
| Comment | Free-form comments |
| Hmi Visible | The value TRUE or FALSE is expected. |
| Hmi Accessible | The value TRUE or FALSE is expected. |
| Hmi Writeable | The value TRUE or FALSE is expected. |
| Typeobject ID | Value used internally that must not be changed manually. |
| Version ID | Value used internally that must not be changed manually. |

##### Format of the sheet "TagTableProperties"

This sheet contains the displayed columns. The column titles are predefined and are always expected to be in English.

The following table specifies the contents expected for the individual columns:

| Element | Explanation |
| --- | --- |
| Path | Group and name of the PLC tag table |
| BelongsToUnit | Software Unit in which the PLC tag has been created. |
| Accessibility | Publication status of the PLC tag table |

---

**See also**

[Basics for exporting and importing PLC tags](#basics-for-exporting-and-importing-plc-tags)
  
[Exporting PLC tags](#exporting-plc-tags)
  
[Importing PLC tags](#importing-plc-tags)

#### Format of the export file (*.xml)

##### Introduction

During the export of PLC tag tables, a standardized xml format will be generated. This format is also expected during the import of xml files.

##### Example of an xml export file

The following example shows a PLC tag table which was exported to the *.xml format:

![Example of an xml export file](images/108220252171_DV_resource.Stream@PNG-de-DE.png)

#### Format of the export file (*.sdf)

##### Introduction

During the export of PLC tag tables, a standardized sdf format will be generated. The individual columns are separated by commas.

This format is also expected during the import of sdf files.

##### Example of an sdf export file

The following example shows a PLC tag table which was exported to the *.sdf format:

![Example of an sdf export file](images/120419368843_DV_resource.Stream@PNG-de-DE.png)

The entries can be interpreted as follows:

![Example of an sdf export file](images/120406229771_DV_resource.Stream@PNG-de-DE.png)

#### Exporting PLC tags

You have the following options for exporting PLC tags and constants:

- Export the elements from a single PLC tag table.
- Export all PLC tags and constants of a CPU from the table "All tags".

##### Requirement

A single PLC tag table or the table "All tags" is open.

##### Procedure

To export PLC tags and constants, follow these steps:

1. In the PLC tag table, click the "Export" button.

   The "Export" dialog box opens.
2. Click the selection button under "Path of export file".

   The "Save as" dialog opens.
3. Enter the name of the export file and select the file in which it is to be stored.
4. Select *.xlsx, *.sdf or *.xml as the file type.
5. Click the "Save" button.
6. Now select the export options:

   - Select whether to export tags and/or constants.
   - Select whether you want to export all elements of the table or just the elements that are actually being used in the program on the current CPU.
7. Click the "OK" button.

##### Result

The export file will be generated. Errors and warnings generated during export are indicated in the "Info" tab of the Inspector window.

---

**See also**

[Basics for exporting and importing PLC tags](#basics-for-exporting-and-importing-plc-tags)
  
[Format of the export file (*.xlsx)](#format-of-the-export-file-xlsx)
  
[Importing PLC tags](#importing-plc-tags)

#### Importing PLC tags

##### Requirement

The PLC tag table from which the tags were exported is open. This can be either a single PLC tag table or the table "All tags".

##### Procedure

To import PLC tags, follow these steps:

1. Click the "Import" button.

   The "Import" dialog box opens.
2. Select the file you want to import.
3. Specify whether you want to import tags and/or constants.
4. Specify whether you want to synchronize the tags by names or addresses.

   When synchronizing by name, existing PLC tags are overwritten if they have the same name as the imported PLC tags. When synchronizing by address, tags with the same address are overwritten.
5. Click the "OK" button.

##### Result

The tags from the import file are imported into the open PLC tag table. Depending on the synchronization option selected in the import dialog, existing tags with the same name or the same address are overwritten.

References to PLC tags or constants that already exist in the project are updated automatically during import. The update is executed based on the name of the PLC tags and constants.

If the import file contains information on software units but the CPU does not support software units, then all PLC tags are imported into the open PLC tag table. The information on software units is ignored during the import.

Errors and warnings generated during import are indicated in the import log.

> **Note**
>
> **Missing version ID**
>
> When you see the message "Missing version ID in the properties of the XLSX file" during import, the internal export format of the file is invalid. In this case open the "Customize" tab in the extended document properties of the XLSX file. Set the value "TIA_Version" to "1.0".

---

**See also**

[Basics for exporting and importing PLC tags](#basics-for-exporting-and-importing-plc-tags)
  
[Format of the export file (*.xlsx)](#format-of-the-export-file-xlsx)
  
[Exporting PLC tags](#exporting-plc-tags)

#### Editing individual PLC tags with external editors

To edit individual PLC tags in external editors outside the TIA portal, you can export or import these tags using copy and paste. However, you cannot copy structured tags to an editor.

##### Requirement

A PLC tag table and an external editor are opened.

##### Procedure

To export and import individual PLC tags, follow these steps:

1. Select one or more PLC tags.
2. Select "Copy" in the shortcut menu.
3. Switch to the external editor and paste the copied tags.
4. Edit the tags as required.
5. Copy the tags in the external editor.
6. Switch back to the PLC tag table.
7. Select "Paste" in the shortcut menu.

> **Note**
>
> You also have the option of export or importing PLC tags as mass data.
>
> See also: [Exporting and importing PLC tags](#exporting-and-importing-plc-tags)

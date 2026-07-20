---
title: "Testing with the watch table"
package: ProgVAT2MenUS
topics: 30
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Testing with the watch table

This section contains information on the following topics:

- [Introduction to testing with the watch table](#introduction-to-testing-with-the-watch-table)
- [Layout of the watch table](#layout-of-the-watch-table)
- [Basic mode and expanded mode in the watch table](#basic-mode-and-expanded-mode-in-the-watch-table)
- [Icons in the watch table](#icons-in-the-watch-table)
- [Creating and editing watch tables](#creating-and-editing-watch-tables)
- [Entering tags in the watch table](#entering-tags-in-the-watch-table)
- [Monitoring tags in the watch table](#monitoring-tags-in-the-watch-table)
- [Modifying tags in the watch table](#modifying-tags-in-the-watch-table)

## Introduction to testing with the watch table

### Overview

The following functions are available in the watch table:

- **Monitoring tags**

  This allows the current values of the individual tags of a user program or a CPU to be displayed on the programming device or PC.
- **Modifying tags**

  You can use this function to assign fixed values to the individual tags of a user program or CPU. Modifying is also possible with [Test with program status](Testing%20the%20user%20program.md#introduction-to-testing-with-program-status) .
- **"Enable peripheral outputs" and "Modify now"**

  These two functions enable you to assign fixed values to individual peripheral outputs of a CPU in the STOP mode. You can also use them to check your wiring.

### Monitoring and modifying tags

The following tags can be monitored and modified:

- Inputs, outputs, and bit memories
- Contents of data blocks
- Content of UDTs
- I/O

### Team engineering in the watch table

As of TIA Portal V13 SP1, within the framework of team engineering with an S7-1500 CPU with firmware version >= 1.7, several Engineering Systems can access the CPU online simultaneously, for example to monitor and modify tags and download blocks. If you use this function, make sure that you keep to the requirements and rules that apply to team engineering as explained in the information system in "Using Team Engineering" in the section "Shared commissioning of projects".

### Possible applications

The advantage of the watch table is that a variety of test environments can be stored. This enables you to reproduce tests during commissioning or for service and maintenance purposes.

---

**See also**

[Layout of the watch table](#layout-of-the-watch-table)
  
[Basic mode and expanded mode in the watch table](#basic-mode-and-expanded-mode-in-the-watch-table)
  
[Icons in the watch table](#icons-in-the-watch-table)
  
[Creating and editing watch tables](#creating-and-editing-watch-tables)

## Layout of the watch table

### Introduction

A watch table contains the tags you defined for the entire CPU. A "Watch and force tables" folder is automatically generated for each CPU created in the project. You create a new watch table in this folder by selecting the "Add new Watch table" command.

### Layout of the watch table

The columns displayed in the watch table depend on the mode you are working in: basic mode or expanded mode.

The following additional columns are shown in expanded mode:

- Monitor with trigger
- Modify with trigger

The names of the columns can also be changed dynamically based on the action.

### Meaning of the columns

The following table shows the meaning of the individual columns in basic mode and expanded mode:

| Mode | Column | Meaning |
| --- | --- | --- |
| Basic mode | ![Meaning of the columns](images/21259497483_DV_resource.Stream@PNG-de-DE.PNG) | Identifier column |
| Name | Name of the inserted tag |  |
| Address | Address of the inserted tag |  |
| Display format | Selected display format |  |
| Monitor value | Values of the tags, depending on the selected display format. |  |
| Modify value | Value with which the tag is modified. |  |
| ![Meaning of the columns](images/21259319563_DV_resource.Stream@PNG-de-DE.PNG) | Select the tag to be modified by clicking the corresponding check box. |  |
| Comment | Option to enter a comment to document the tags in the watch table. |  |
| Tag comment | Display of the comment on the selected tag that was entered in other editors. This column cannot be edited. |  |
| The following additional columns are shown in expanded mode: | Monitor with trigger | Display of selected monitoring mode |
| Modify with trigger | Display of selected modify mode |  |

---

**See also**

[Icons in the watch table](#icons-in-the-watch-table)

## Basic mode and expanded mode in the watch table

### Difference between basic mode and expanded mode in the watch table

Depending on the mode specified, the watch table displays different columns and column headings that can be used to perform different actions.

You will find a detailed list of the columns in [Layout of the watch table](#layout-of-the-watch-table).

### Switching between basic mode and expanded mode

You have the following options of toggling between the basic and expanded mode:

- Click the icon "Show/hide advanced setting columns". Click this icon again to return to the basic mode.

  Or:
- In the "Online" menu, select the "Expanded mode" check box. Deactivate this check box to return to the basic mode.

### Functionality in expanded mode

The following functionality is only possible in expanded mode:

- Monitor with trigger
- Modify with trigger
- Enable peripheral outputs
- Monitor peripheral inputs
- Modify peripheral outputs

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Danger of a time-out while monitoring peripheral inputs and controlling peripheral outputs**  Note that the monitoring of peripheral inputs and the controlling of peripheral outputs in the watch table can result in a time-out.  The CPU assumes the "STOP" mode. |  |

---

**See also**

[Setting the monitoring and modify mode](#setting-the-monitoring-and-modify-mode)

## Icons in the watch table

### Meaning of the icons

The following table shows the meaning of the icons in the watch table:

| Icon | Meaning |
| --- | --- |
| ![Meaning of the icons](images/21263312907_DV_resource.Stream@PNG-de-DE.PNG) | Identifies a table inside the project tree as a watch table. |
| ![Meaning of the icons](images/21259497483_DV_resource.Stream@PNG-de-DE.PNG) | Shows information in the identifier column. |
| ![Meaning of the icons](images/57241034763_DV_resource.Stream@PNG-de-DE.png) | Inserts a row before the selected row. |
| ![Meaning of the icons](images/57243271051_DV_resource.Stream@PNG-de-DE.png) | Inserts a row after the selected row. |
| ![Meaning of the icons](images/95715440011_DV_resource.Stream@PNG-de-DE.png) | Inserts a comment line above the selected row. |
| ![Meaning of the icons](images/13511789195_DV_resource.Stream@PNG-de-DE.png) | Modifies the addresses of all selected tags immediately and once. This command is executed once and as quickly as possible without reference to a defined trigger point in the user program. |
| ![Meaning of the icons](images/13511528587_DV_resource.Stream@PNG-de-DE.png) | Modifies the addresses of all selected tags with reference to a defined trigger point in the user program. |
| ![Meaning of the icons](images/20309677835_DV_resource.Stream@PNG-de-DE.png) | Disables the command output disable of the peripheral outputs. You can then modify the peripheral outputs when the CPU is in STOP mode. |
| ![Meaning of the icons](images/21262260107_DV_resource.Stream@PNG-de-DE.PNG) | Displays all columns of expanded mode. If you click this icon again, the columns of expanded mode will be hidden. |
| ![Meaning of the icons](images/21262267659_DV_resource.Stream@PNG-de-DE.PNG) | Displays all modify columns. If you click this icon again, the modify columns will be hidden. |
| ![Meaning of the icons](images/13511990283_DV_resource.Stream@PNG-de-DE.png) | Starts monitoring of the visible tags in the active watch table. The default setting for the monitoring mode in basic mode is "permanent". In expanded mode, you can set defined trigger points for the monitoring of tags. |
| ![Meaning of the icons](images/13511997579_DV_resource.Stream@PNG-de-DE.png) | Starts monitoring of the visible tags in the active watch table. This command is executed immediately and the tags are monitored once. |
| ![Meaning of the icons](images/26034002059_DV_resource.Stream@PNG-de-DE.PNG) | Displays the check box for the selection of tags to be modified. |
| ![Meaning of the icons](images/8395330443_DV_resource.Stream@PNG-de-DE.png) | Indicates that the value of the selected tag has been modified to "1". |
| ![Meaning of the icons](images/8395351691_DV_resource.Stream@PNG-de-DE.png) | Indicates that the value of the selected tag has been modified to "0". |
| ![Meaning of the icons](images/8395279499_DV_resource.Stream@PNG-de-DE.png) | Indicates that the address is being used multiple times. |
| ![Meaning of the icons](images/8395918219_DV_resource.Stream@PNG-de-DE.png) | Indicates that the substitute value is being used. Substitute values are values that are output to the process in case of signal output module faults or are used instead of a process value in the user program in case of signal input module faults. The substitute values can be assigned by the user (e.g., retain old value). |
| ![Meaning of the icons](images/13518917387_DV_resource.Stream@PNG-de-DE.png) | Indicates that the address is blocked because it is already being modified. |
| ![Meaning of the icons](images/13515174027_DV_resource.Stream@PNG-de-DE.png) | Indicates that the address cannot be modified. |
| ![Meaning of the icons](images/13515181579_DV_resource.Stream@PNG-de-DE.png) | Indicates that the address cannot be monitored. |
| ![Meaning of the icons](images/8395965067_DV_resource.Stream@PNG-de-DE.png) | Indicates that an address is being forced. |
| ![Meaning of the icons](images/8395973515_DV_resource.Stream@PNG-de-DE.png) | Indicates that an address is being partly forced. |
| ![Meaning of the icons](images/26033994507_DV_resource.Stream@PNG-de-DE.PNG) | Indicates that an associated I/O address is being fully or partly forced. |
| ![Meaning of the icons](images/20510956427_DV_resource.Stream@PNG-de-DE.PNG) | Indicates that an address cannot be fully forced. Example: It is indeed possible to force the address QW0:P, but it is not possible to force the address QD0:P since this address area is eventually not available on the CPU. |
| ![Meaning of the icons](images/8395313547_DV_resource.Stream@PNG-de-DE.png) | Indicates that a syntax error occurred. |
| ![Meaning of the icons](images/13516393483_DV_resource.Stream@PNG-de-DE.png) | Indicates that the address is selected but at the moment e.g. has not yet been modified. |

---

**See also**

[Layout of the watch table](#layout-of-the-watch-table)

## Creating and editing watch tables

This section contains information on the following topics:

- [Creating a watch table](#creating-a-watch-table)
- [Opening a watch table](#opening-a-watch-table)
- [Copying and pasting a watch table](#copying-and-pasting-a-watch-table)
- [Saving a watch table](#saving-a-watch-table)

### Creating a watch table

#### Introduction

The [watch table](#) (The watch table allows you to monitor and modify tags in the user program. Within the watch table, it is also possible to assign fixed values to individual peripheral outputs of the CPU in STOP mode.)  allows you to monitor and modify tags in the user program. Once you have created a watch table, you can save it, duplicate it, and print it and use it again and again to monitor and modify tags.

#### Requirement

A project is open.

#### Procedure

To create a watch table, follow these steps:

1. Click "Project view" in the status bar.

   The project view is displayed.
2. In the project tree, double-click the CPU for which you want to create a watch table.
3. Double-click the "Watch and force tables" folder and then the "Add new watch table" command.

   A new watch table is added.
4. In the "Name" column or in the "Address" column, enter the name or the absolute address for the tags that you want to monitor or modify.
5. You can select a display format from the drop-down list in the "Display format" column if you want to change this default setting.
6. Now decide whether you want to monitor or modify the entered tags and, if applicable, enter the desired values for modifying.

### Opening a watch table

#### Requirement

A [watch table](#) (The watch table allows you to monitor and modify tags in the user program. Within the watch table, it is also possible to assign fixed values to individual peripheral outputs of the CPU in STOP mode.)  has been created.

#### Procedure

To open a watch table, follow these steps:

1. Open the "Watch and force tables" folder below the desired CPU.
2. Double-click on the required watch table in the folder.

#### Result

The selected watch table opens.

### Copying and pasting a watch table

#### Requirement

A [watch table](#) (The watch table allows you to monitor and modify tags in the user program. Within the watch table, it is also possible to assign fixed values to individual peripheral outputs of the CPU in STOP mode.)  has been created.

#### Procedure

To copy a watch table, follow these steps:

1. Right-click the watch table that you want to copy.
2. In the context menu, select "Copy".
3. In the project tree, open the folder structure for the CPU in which you want to paste the copied watch table.
4. Right-click on the "Watch and force tables" folder.
5. In the context menu, select "Paste".
6. Alternatively, you can select the entire contents of the watch table and Drag & Drop it onto another watch table.

#### Result

A copy of the selected watch table is placed in the "Watch and force tables" folder of the relevant CPU.

### Saving a watch table

#### Prerequisite

A [watch table](#) (The watch table allows you to monitor and modify tags in the user program. Within the watch table, it is also possible to assign fixed values to individual peripheral outputs of the CPU in STOP mode.)  has been created.

#### Procedure

To save a watch table, follow these steps:

1. In the project tree select the watch table you want to save.
2. If you wish to change the preset name of the table, select the "Rename" command in the context menu and enter a new name for the table.
3. In the "Project" menu, select "Save". Note that this save operation will save the entire project.

#### Result

The contents of the watch table and the project are saved.

> **Note**
>
> You can reuse saved watch tables to monitor and modify tags when retesting your program.

## Entering tags in the watch table

This section contains information on the following topics:

- [Basic information on entering tags in the watch table](#basic-information-on-entering-tags-in-the-watch-table)
- [Permitted operands for the watch table](#permitted-operands-for-the-watch-table)
- [Permissible modify values for the watch table](#permissible-modify-values-for-the-watch-table)
- [Overview of the display formats](#overview-of-the-display-formats)
- [Selecting the display format for tags](#selecting-the-display-format-for-tags)
- [Creating and editing comment lines](#creating-and-editing-comment-lines)

### Basic information on entering tags in the watch table

#### Recommended procedure

- Select the tags whose values you want to monitor or modify, and enter them in the watch table.
- When entering tags into the watch table, please note that these tags must be previously defined in the PLC tag table.
- When entering tags, work from the outside to the inside. This means that you start by entering the tags for the inputs in the watch table. Then, you enter the tags that are affected by the inputs or that affect the outputs. Finally, you enter the tags for the outputs.

#### Example of filling out a watch table

- Enter the absolute address to be monitored or modified in the "Address" column.
- Enter the symbolic name for the tag in the "Name" column.
- Select the display format you require from the drop-down list in the "Display format" column, if you do not want to use the default setting.
- Now decide whether you want to monitor or modify the entered tags. Enter the desired values for modifying as well as a comment in the corresponding columns of the watch table.

#### Create comment row

If required, you can create a comment row by entering the string "//" in the "Name" column.

#### Syntax check

When you enter the tags in the watch table, the syntax of each cell is checked when you exit the cell. Incorrect entries are marked in red.

> **Note**
>
> When you place the mouse pointer in a cell marked in red, brief information is displayed with additional notes on the error.

---

**See also**

[Permitted operands for the watch table](#permitted-operands-for-the-watch-table)
  
[Permissible modify values for the watch table](#permissible-modify-values-for-the-watch-table)

### Permitted operands for the watch table

#### Permissible operands for the watch table

The following table shows the operands that are permitted for the watch table:

| Permitted operand | Example of data type | Example (International mnemonics) |
| --- | --- | --- |
| Input/output/bit memory | BOOL | I1.0, Q1.7, M10.1  I0.0:P; Q0.0:P |
| Input/output/bit memory | BYTE | IB1/QB10/MB100  IB1:P; QB1:P |
| Input/output/bit memory | WORD | IW1; QW10; MW100  IW2:P; QW3:P |
| Input/output/bit memory | DWORD | ID4; QD10; MD100  ID2:P; QD1:P |
| Timers | TIMER | T1 |
| Counters | COUNTER | C1 |
| Data block | BOOL | DB1.DBX1.0 |
| Data block | BYTE | DB1.DBB1 |
| Data block | WORD | DB1.DBW1 |
| Data block | DWORD | DB1.DBD1 |

> **Note**
>
> **Please observe the following notes to work with the watch table.**
>
> - You cannot enter "DB0..." because it is used by the system!
> - Peripheral outputs can be modified but not monitored.
> - Peripheral inputs can be monitored but not modified.

> **Note**
>
> **No access to peripheral bits for S7-300/400 CPUs**
>
> The watch table does not allow S7-300/400 CPUs to access peripheral bits, e.g. %I0.0:P; %Q0.0:P.
>
> These bits cannot be watched or controlled.
>
> Please use the bits in the process image instead, e.g. %I0.0; %Q0.0.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Danger of a time-out while monitoring peripheral inputs and controlling peripheral outputs**  Note that the monitoring of peripheral inputs and the controlling of peripheral outputs in the watch table can result in a time-out.  The CPU assumes the "STOP" mode. |  |

### Permissible modify values for the watch table

#### Entry of modify values in the watch table

The following table shows the operands that are permitted for the entry of modify values in the watch table:

All tables
Bit operands
Byte operands
Word operands
Double word operands

Bit operands

| Possible bit operands | Example for permitted modify values |
| --- | --- |
| I1.0 | True |
| M1.7 | False |
| Q1.0 | 0 |
| Q1.1:P | 1 |
| DB1.DBX1.1 | 2#0 |
| M1.6 | 2#1 |

Byte operands

| Possible byte operands | Example for permitted modify values |
| --- | --- |
| IB1 | 2#0011_0011 |
| MB12 | B#16#1F |
| QB10 | 1F |
| QB11:P | 'a' |
| DB1.DBB1 | 10 |

Word operands

| Possible word operands | Example for permitted modify values |
| --- | --- |
| IW1 | 2#0011_0011_0011_0011 |
| MW12 | W#16#ABCD |
| MW14 | ABCD |
| QW10 | B#(12, 34) |
| QW12:P | 12345 |
| DB1.DBW1 | 'ab' |
| MW16 | S5T#9s_340ms |
| MW18 | C#123 |
| MW9 | D#2006-12-31 |

Double word operands

| Possible double word operands | Example for permitted modify values |
| --- | --- |
| ID1 | 2#0011_0011_0011_0011_0011_0011_0011_0011 |
| QD10 | Dw#16#abcdef10 |
| QD12:P | ABCDEF10 |
| DB1.DBD2 | b#(12,34,56,78) |
| MD8 | L#-12 |
| MD12 | L#12 |
| MD16 | 123456789 |
| MD20 | 123456789 |
| MD24 | T#12s_345ms |
| MD28 | Tod#1:2:34.567 |
| MD32 | P#e0.0 |

Timers

| Possible operands of the "Timer" type | Permitted control values | Explanation |
| --- | --- | --- |
| T1 | 0 ms | Time value in milliseconds (ms) |
| T12 | 20 ms | Time value in milliseconds (ms) |
| T14 | 12400 ms | Time value in milliseconds (ms) |
| T16 | S5t#12s300ms | Time value 12s 300 ms |

Counters

| Possible operands of the "Counter" type | Permitted control values |
| --- | --- |
| C1 | 0 |
| C14 | 20 |
| C16 | C#123 |

#### Notes on timers and counters

- Timers

  > **Note**
  >
  > Modifying a timer influences only the value, not the status. Timer T1 can be modified to the value "0", but the result of logic operation for A T1 is not changed.
  >
  > The time sequences "s5t" and "s5time" can be written in both lower-case and upper-case characters.
- Counters

  > **Note**
  >
  > Modifying a counter influences only the value, not the status. Counter C1 can be changed to the value "0", but the result of the logic operation for A C1 is not changed.

### Overview of the display formats

#### Display formats in the watch table

The display format you select specifies the representation of a tag value.

When entering the address a display format is automatically preset. If you want to change this, you can select a display format from the drop-down list in the "Display formats" column. The drop-down list only offers the display formats which are valid for this data type. The display format that appears first in the list is the pre-selected format.

#### Example

The following table shows the 32-bit data types permitted for all CPU families in the watch table and their possible display formats:

| Data type | Possible display formats |
| --- | --- |
| BOOL | Bool, Hex, BCD, Octal, Bin, Dec, Dec+/- |
| BYTE | Hex, BCD, Octal, Bin, Dec, Dec+/-, Character |
| WORD | Hex, BCD, Octal, Bin, Dec, Dec+/-, Dec_Sequence, Character, Unicode_Character, SIMATIC_Time, Date, Counter |
| DWORD | Hex, BCD, Octal, Bin, Dec, Dec+/-, Dec_Sequence, Character, Unicode_Character, Floating-point number, Time of day, Timer |
| SINT | Dec, Dec+/-, Hex, BCD, Octal, Bin, Character |
| INT | Dec, Dec+/-, Hex, BCD, Octal, Bin, Character, Unicode_Character, Dec_Sequence, SIMATIC_Time, Counter, Date |
| DINT | Dec, Dec+/-, Hex, BCD, Octal, Bin, Character, Unicode_Character, Dec_Sequence, Time of day, Timer |
| USINT | Dec, Dec+/-, Hex, BCD, Octal, Bin, Character |
| UINT | Dec, Dec+/-, Hex, BCD, Octal, Bin, Character, Unicode_Character, Dec_Sequence, SIMATIC_Time, Counter, Date |
| UDINT | Dec, Dec+/-, Hex, BCD, Octal, Bin, Character, Unicode_Character, Dec_Sequence, Time of day, Timer |
| REAL | Floating-point number, Hex, BCD, Octal, Bin, Character, Unicode_Character,Dec, Dec+/-, Dec_Sequence, Time of day, Timer |
| DATE | Date, Dec, Hex, Bin |
| TIME_OF_DAY | Time of day, Dec, Hex, Bin |
| TIME | Timer, Hex, Bin, Dec, Dec+/- |
| DATE_AND_TIME | Date and time, |
| TIMER | SIMATIC_Time, Hex, BCD, Bin |
| CHAR | Character, Hex, BCD, Octal, Bin, Dec, Dec+/- |
| WCHAR | Unicode_Character, Character, Hex, BCD, Octal, Bin, Dec, Dec+/- |
| STRING | Character string |
| WSTRING | Unicode_character string |
| POINTER | Pointer, Hex |
| COUNTER | Counter, Hex, BCD, Bin |
| S5TIME | SIMATIC_Time, Hex, BCD, Bin |

For the S7-1200 CPU family, all 32-bit data types are permitted (see table above), as well as the 64-bit data type LREAL with the following possible display formats:

| Data type | Possible display formats |
| --- | --- |
| LREAL | In a project created with TIA Portal < V12:   Floating-point number   Note: The display of LREAL is limited to 13 digits plus exponent. |
| LREAL | In a project created with TIA Portal >= V12:   Floating-point number, Hex, BCD, Octal, Bin, Character, Unicode_Character, Dec,  Dec+/-, Dec_Sequence, Time of day, Time, Date and time  Note: The display of LREAL is limited to 13 digits plus exponent. |

For the S7-1500 CPU family, in addition to 32-bit data types, the 64-bit data types listed in the table are also permitted with the following possible display formats:

| Data type | Possible display formats |
| --- | --- |
| LWORD | Hex, Octal, BCD, Bin, Character, Unicode_Character, Dec, Dec+/-, Dec_Sequence, Floating-point number, Time of day, Time, Date and time |
| LINT | Dec+/-, Dec, Hex, BCD, Octal, Bin, Character, Unicode_Character, Dec_Sequence, Time of day, Time, Date and time |
| ULINT | Dec, Dec+/-, Hex, BCD, Octal, Bin, Character, Unicode_Character, Dec_Sequence, Time of day, Time, Date and time |
| LREAL | Floating-point number, Hex, BCD, Octal, Bin, Character, Unicode_Character, Dec, Dec+/-, Dec_Sequence, Time of day, Time, Date and time |
| LTIME | Timer, Dec+/-, Dec, Hex, Bin |
| LTOD | Time of day, Dec, Hex, Bin |
| LDT | Date and time, Dec, Hex, Bin |

For more information, refer to the description of the valid [data types](Data%20types.md#overview-of-the-valid-data-types).

> **Note**
>
> **Rounding of floating-point numbers**
>
> In the watch table, floating-point numbers are stored as binary numbers in IEEE format. Because not every floating point number (real, longreal) that can be displayed on the user interface can be mapped to the IEEE format, there is a possibility that floating-point numbers will be rounded. If a rounded floating-point number in the watch table is copied and, in turn, inserted in another input field, the rounding may cause a slight difference.

> **Note**
>
> **Only symbolic addressing is possible**
>
> In the watch table, LongDataTypes such as LWORD or LREAL can only be addressed symbolically.

### Selecting the display format for tags

#### Procedure

To select the display format of the tags, follow these steps:

1. Enter the desired address in the watch table.
2. Click the desired cell in the "Display format" column, and open the drop-down list.

   The permissible display formats are shown in the drop-down list.
3. Select the desired display format from the drop-down list.

**Note**

If the selected display format cannot be applied, then the last selected display format will be displayed automatically.

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)

### Creating and editing comment lines

#### Basic principles of comment lines

In addition to the row related comments in the comment column, you can now also create complete comment lines to enhance the structure of the watch table.

The contents of the comment line are stored in the "Languages & Resources" folder in the "Project texts" tab and can be compiled in other project languages.

Alternatively, you have the following options to enter comment lines:

- Using the corresponding icon in the toolbar of the watch table.
- Using the menu command "Insert > Insert comment line".
- Using the shortcut menu command "Insert comment line".
- By entering the string "//" in the "Name" column of the watch table.

#### Inserting comment lines

To insert comment lines, follow these steps:

1. Open the watch table and enter the required addresses.
2. Insert a new comment line:

   - To do so, click the "Insert comment line" icon in the toolbar of the watch table.
   - Or click the menu command "Insert > Insert comment line".
   - Or click the shortcut menu command "Insert comment line".

     Result: A new comment line is inserted above the selected row in the watch table.
3. Enter the required comment in the comment line. The entered comment is shown in green.
4. To show all comments you entered, double-click "Project texts" in the project tree under "Languages & Resources".
5. If you are working in multi-lingual projects and want your comment to be translated into other languages, you can set the project languages required in addition to the editing language in the project tree under "Languages & Resources > Project languages".

#### Creating comment lines

To create comment lines, follow these steps:

1. Open the watch table and enter the required addresses.
2. Enter the character string "//" in a free row in the "Name" column. This turns the row into a comment line.

   No comment lines can be created in the other columns.
3. Enter the required comment in the comment line. The entered comment is shown in green.
4. To show all comments you entered, double-click "Project texts" in the project tree under "Languages & Resources".
5. If you are working in multi-lingual projects and want your comment to be translated into other languages, you can set the project languages required in addition to the editing language in the project tree under "Languages & Resources > Project languages".

#### Deleting comment lines

To delete comment lines, follow these steps:

1. Open a watch table containing comment lines.
2. Delete the entire comment with the introductory string "//", if you no longer required this.
3. Alternatively, delete only the introductory string "//". In this case the existing comment is retained and is displayed in the "Comment" column in the watch table.

   > **Note**
   >
   > **Deleting comment lines**
   >
   > When you delete comment lines the project languages and any existing translations for these comments are also deleted.

## Monitoring tags in the watch table

This section contains information on the following topics:

- [Introduction to monitoring tags in the watch table](#introduction-to-monitoring-tags-in-the-watch-table)
- [Setting the monitoring and modify mode](#setting-the-monitoring-and-modify-mode)
- ["Monitor all" command for tags](#monitor-all-command-for-tags)
- ["Monitor now" command for tags](#monitor-now-command-for-tags)

### Introduction to monitoring tags in the watch table

#### Introduction

The watch table allows you to monitor the tags of the configured input and output modules in the CPU, depending on the [monitoring and modify mode](#setting-the-monitoring-and-modify-mode) selected. To monitor tags, an online connection to the CPU must exist.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Danger of a time-out while monitoring peripheral inputs**  Note that the monitoring of peripheral inputs can result in a time-out.  The CPU assumes the "STOP" mode. |  |

#### Options for monitoring tags

The following options are available for monitoring tags:

- Monitor now  
  This command starts the monitoring of the visible tags in the active watch table immediately and once only.
- Monitor all  
  This command starts the monitoring of all visible tags in the active watch table, depending on the selected watch mode:

  - In basic mode, the monitoring mode is set to "permanent" by default.
  - In expanded mode, you can specify defined trigger points for the monitoring of tags.

    > **Note**
    >
    > If the monitoring mode is changed while in expanded mode and then a switch is made to basic mode, the monitoring mode set before will also be applied in basic mode.

#### CPU-specific limitations when monitoring tags

The following CPU-specific differences exist:

- CPU S7-300/400:  
  CPUs from this family can only monitor the first 30 characters of a string.
- CPU S7-1200/1500:  
  CPUs from this family can monitor a string up to the total size of 254 characters.

### Setting the monitoring and modify mode

#### Introduction

By selecting the monitoring and modify mode, you specify the trigger point and the duration of the tag monitoring in the [watch table](#) (The watch table allows you to monitor and modify tags in the user program. Within the watch table, it is also possible to assign fixed values to individual peripheral outputs of the CPU in STOP mode.)  and the [force table](#) (The force table allows you to monitor and force tags in the user program. Forcing is used to permanently assign fixed values to individual peripheral outputs of a CPU.) .

#### Possible monitoring and modify modes (duration of monitoring or modifying)

The following monitoring and modifying modes are available:

| Trigger | Execution | CPU status | Duration |
| --- | --- | --- | --- |
| Permanent | Permanent  During monitoring: The inputs are monitored at the end of the cycle and the outputs at the start of the cycle.  During modify: The inputs are modified at the start of the cycle and the outputs at the end of the cycle. | RUN | Will be executed until the user stops the action or the online connection to the CPU is interrupted. |
| Permanently, at start of scan cycle | Permanently, at start of scan cycle | RUN | Will be executed until the user stops the action or the online connection to the CPU is interrupted. |
| Permanently, at end of scan cycle | Permanently, at end of scan cycle | RUN | Will be executed until the user stops the action or the online connection to the CPU is interrupted. |
| Permanently, at transition to STOP | Permanently, at transition from RUN to STOP | RUN > STOP | Will be executed until the user stops the action or the online connection to the CPU is interrupted. |
| Once only, at start of scan cycle | Once only, at start of scan cycle | RUN | Ends automatically after being executed once. |
| Once only, at end of scan cycle | Once only, at end of scan cycle | RUN | Ends automatically after being executed once. |
| Once only, at transition to STOP | Once only, at transition from RUN to STOP | STOP > RUN | Ends automatically after being executed once. |

#### Special features when using "Permanent" mode

The "Permanent" mode is executed differently for the monitoring and modifying of tags.

- Monitoring: The inputs are monitored at the end of the cycle and the outputs at the start of the cycle.
- Modifying: The inputs are modified at the start of the cycle and the outputs at the end of the cycle.

#### Selecting the trigger point

The trigger points "Beginning of scan cycle", "End of scan cycle", and "Switch to stop" specify the time at which the tags are to be read from the CPU or updated in the CPU.

The following diagram shows the position of these trigger points:

![Selecting the trigger point](images/9165223563_DV_resource.Stream@PNG-en-US.png)

#### Position of the trigger points

From the position of the trigger points, it follows that:

- Modifying of inputs is only appropriate at the beginning of the scan cycle (corresponding to the beginning of the user program OB 1), because otherwise the process image input is updated again after modifying and is thus overwritten.
- Modifying of outputs is only appropriate at the end of the scan cycle (corresponding to the end of the user program OB 1), because otherwise the process image output can be overwritten by the user program.
- The modified value is displayed in the "Monitor value" column, provided that monitoring is active and the modified value is not overwritten by the user program.

#### Monitoring tags

When tags are being modified, the following applies to the trigger points:

- If you have specified the modify mode as "once only", you will receive an alarm if the selected tags cannot be modified.
- In "permanent" modify mode, you do not receive an alarm.

#### Note regarding the "Modify now" command

You can modify the values of selected tags immediately using the "Online > Modify >Modify now" command. This command is executed once only and as quickly as possible without reference to a defined position (trigger point) in the user program. This function is used mainly for modifying when the CPU is in STOP mode.

### "Monitor all" command for tags

#### Introduction

The "Monitor all" command allows you to start monitoring the visible tags in the active watch table. The default setting for the monitoring mode in basic mode of the watch table is "permanent". In expanded mode, you can specify defined trigger points for the monitoring of tags. In this case, the tags are monitored with reference to the specified trigger points.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Danger of a time-out while monitoring peripheral inputs**  Note that the monitoring of peripheral inputs can result in a time-out.  The CPU assumes the "STOP" mode. |  |

#### Requirements

- A watch table has been created.
- An online connection to the CPU exists.

#### Procedure

To execute the "Monitor all" command, follow these steps:

1. Enter the tags to be monitored and the corresponding addresses in the watch table.
2. Switch to expanded mode by clicking

   the icon "Show/hide advanced setting columns" in the toolbar.
3. If you want to change the default monitoring mode for a tag, click the appropriate cell in the "Monitor with trigger" column and select the desired monitoring mode from the drop-down list.
4. Click the "Monitor all" icon in the toolbar.

#### Result

The tags of the active watch table are monitored using the monitoring mode selected.

---

**See also**

[Icons in the watch table](#icons-in-the-watch-table)
  
[Basic mode and expanded mode in the watch table](#basic-mode-and-expanded-mode-in-the-watch-table)
  
[Entering tags in the watch table](#entering-tags-in-the-watch-table)

### "Monitor now" command for tags

#### Introduction

The "Monitor now" command starts the monitoring of tags immediately without reference to defined trigger points. The tag values are read out once only and displayed in the watch table.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Danger of a time-out while monitoring peripheral inputs**  Note that the monitoring of peripheral inputs can result in a time-out.  The CPU assumes the "STOP" mode. |  |

#### Requirements

- A watch table has been created.
- An online connection to the CPU exists.

#### Procedure

To execute the "Monitor now" command, follow these steps:

1. Enter the tags to be monitored and the corresponding addresses in the watch table.
2. Click the "Monitor now" icon in the toolbar.

#### Result

The tags of the active watch table are monitored immediately and once only.

---

**See also**

[Icons in the watch table](#icons-in-the-watch-table)
  
[Basic mode and expanded mode in the watch table](#basic-mode-and-expanded-mode-in-the-watch-table)
  
[Entering tags in the watch table](#entering-tags-in-the-watch-table)

## Modifying tags in the watch table

This section contains information on the following topics:

- [Introduction to modifying tags](#introduction-to-modifying-tags)
- [Modify tags to "0"](#modify-tags-to-0)
- [Modify tags to "1"](#modify-tags-to-1)
- ["Modify now" command for tags](#modify-now-command-for-tags)
- ["Modify selection now"](#modify-selection-now)
- ["Modify with trigger" command for tags](#modify-with-trigger-command-for-tags)
- [Enable peripheral outputs](#enable-peripheral-outputs)

### Introduction to modifying tags

#### Introduction

The watch table allows you to modify the tags of the configured input and output modules in the CPU, depending on the [monitoring and modify mode](#setting-the-monitoring-and-modify-mode) selected.

To monitor the tags, an online connection to the CPU must exist.

| Symbol | Meaning |
| --- | --- |
|  | **Danger** |
| **Danger when modifying:**  Serious personal injury and material damage can result from changes in the tags or addresses during plant operation in the event of malfunctions or program errors!  Make sure that dangerous conditions cannot occur before you execute the "Modify" function. |  |

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Danger of a time-out while controlling peripheral outputs**  Note that the controlling of peripheral outputs in the watch table can result in a time-out.  The CPU assumes the "STOP" mode. |  |

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Danger due to modifying an identical operand in parallel with different modify values in more than one watch table**  When working with more than one watch table, avoid modifying identical operands permanently multiple times with different modify values.  If an identical operand is modified permanently with different modify values at the same time in different watch tables, all watch tables will display the last modified value, because the modify value assigned last will be used in this case. |  |

#### Options for modifying tags

The following options are available for modifying tags:

- Modify to "0"

  This command modifies the selected address to the modify value "0".
- Modify to "1"

  This command modifies the selected address to the modify value "1".
- Modify now

  This command "immediately" modifies all activated addresses in the active watch table.
- Modify selection now

  This command "immediately" modifies all selected addresses in the active watch table.
- Modify with trigger

  This command modifies all selected addresses in the active watch table using the [monitoring and modify mode](#setting-the-monitoring-and-modify-mode) selected.

  The "Modify with trigger" function is only available in expanded mode. You will not receive an alarm indicating whether or not the selected addresses were actually modified with the specified value. You should use the "Modify once only and immediately" function if you require such a confirmation.
- Enable peripheral outputs

  This command disables the command output disable.

  This function can only be executed in expanded mode, when the CPU is in STOP and the option [Force](Testing%20with%20the%20force%20table.md#introduction-to-forcing-tags) of tags is not enabled. If desired, deactivate this function in the force table.

  > **Note**
  >
  > **When modifying, note the following:**
  >
  > Modifying of tags **cannot** be undone.

### Modify tags to "0"

#### Introduction

You can assign one-time values to tags independent of the monitoring and modify mode and modify them. The modify command is executed as fast as possible, similar to a "Trigger now" command, without reference to a defined position in the user program.

| Symbol | Meaning |
| --- | --- |
|  | **Danger** |
| **Danger when modifying:**  Serious personal injury and material damage can result from changes in the tags or addresses during plant operation in the event of malfunctions or program errors!  Make sure that dangerous conditions cannot occur before you execute the "Modify" function. |  |

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Danger of a time-out while controlling peripheral outputs**  Note that the controlling of peripheral outputs in the watch table can result in a time-out.  The CPU assumes the "STOP" mode. |  |

#### Requirements

- A watch table has been created.
- An online connection to the CPU exists.

#### Procedure

To modify tags to "0", follow these steps:

1. Enter the desired address in the watch table.
2. Select the "Online > Modify > Modify to 0" command in order to modify the selected address with the specified value.

#### Result

The selected address is modified to "0".

> **Note**
>
> **When modifying, note the following:**
>
> Modifying can **not** be undone!

### Modify tags to "1"

#### Introduction

You can assign one-time values to tags independent of the monitoring and modify mode and modify them. The modify command is executed as fast as possible, similar to a "Trigger now" command, without reference to a defined position in the user program.

| Symbol | Meaning |
| --- | --- |
|  | **Danger** |
| **Danger when modifying:**  Serious personal injury and material damage can result from changes in the tags or addresses during plant operation in the event of malfunctions or program errors!  Make sure that dangerous conditions cannot occur before you execute the "Modify" function. |  |

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Danger of a time-out while controlling peripheral outputs**  Note that the controlling of peripheral outputs in the watch table can result in a time-out.  The CPU assumes the "STOP" mode. |  |

#### Requirements

- A watch table has been created.
- An online connection to the CPU exists.

#### Procedure

To modify tags to "1", follow these steps:

1. Enter the desired address in the watch table.
2. Select the "Online > Modify > Modify to 1" command in order to modify the selected address with the specified value.

#### Result

The selected address is modified to "1".

> **Note**
>
> **When modifying, note the following:**
>
> Modifying can **not** be undone!

### "Modify now" command for tags

#### Introduction

You can assign one-time values to tags independent of the monitoring and modify mode and modify them immediately. The modify command is executed as fast as possible, similar to a "Trigger now" command, without reference to a defined position in the user program.

| Symbol | Meaning |
| --- | --- |
|  | **Danger** |
| **Danger when modifying:**  Serious personal injury and material damage can result from changes in the tags or addresses during plant operation in the event of malfunctions or program errors!  Make sure that dangerous conditions cannot occur before you execute the "Modify" function. |  |

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Danger of a time-out while controlling peripheral outputs**  Note that the controlling of peripheral outputs in the watch table can result in a time-out.  The CPU assumes the "STOP" mode. |  |

#### Requirements

- A watch table has been created.
- An online connection to the CPU exists.

#### Procedure

To modify tags immediately, follow these steps:

1. Enter the desired addresses and modify values in the watch table.
2. Select the addresses to be modified by selecting the check boxes for modifying in the column after the "Modify value".   
   A yellow triangle appears behind the selected check box, indicating that the address is now selected for modifying but has not yet been modified.
3. Select the "Online > Modify > Modify once and now" command in order to immediately modify the selected address once only with the specified value.

#### Result

The selected addresses are modified immediately and once only.

> **Note**
>
> **When modifying, note the following:**
>
> Modifying can **not** be undone!

### "Modify selection now"

#### Introduction

You can assign one-time values to a selection of tags independently of the monitoring and modifying mode and modify them immediately. The modify command is executed as fast as possible, similar to a "Trigger now" command, without reference to a defined position in the user program.

| Symbol | Meaning |
| --- | --- |
|  | **Danger** |
| **Danger when modifying:**  Serious personal injury and material damage can result from changes in the tags or addresses during plant operation in the event of malfunctions or program errors!  Make sure that dangerous conditions cannot occur before you execute the "Modify" function. |  |

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Danger of a time-out while controlling peripheral outputs**  Note that the controlling of peripheral outputs in the watch table can result in a time-out.  The CPU assumes the "STOP" mode. |  |

#### Requirements

- A watch table has been created.
- An online connection to the CPU exists.

#### Procedure

To modify tags immediately, follow these steps:

1. Enter the desired addresses and modify values in the watch table.
2. Select the addresses to be modified by selecting them with the mouse pointer. To select multiple addresses, use the <Shift> and <Ctrl> keys.
3. Select the "Online > Modify > Modify selection now" command to immediately modify the selected addresses once with the specified values.

#### Result

The selected addresses are modified immediately and once.

> **Note**
>
> **When modifying, note the following:**
>
> Modifying can **not** be undone!

### "Modify with trigger" command for tags

#### Introduction

You can assign values to addresses dependent on the defined monitoring and modify mode and modify them. The modify command is executed as specified in the monitoring and modify mode, with reference to the defined trigger position in the user program.

| Symbol | Meaning |
| --- | --- |
|  | **Danger** |
| **Danger when modifying:**  Serious personal injury and material damage can result from changes in the tags or addresses during plant operation in the event of malfunctions or program errors!  Make sure that dangerous conditions cannot occur before you execute the "Modify" function. |  |

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Danger of a time-out while controlling peripheral outputs**  Note that the controlling of peripheral outputs in the watch table can result in a time-out.  The CPU assumes the "STOP" mode. |  |

#### Requirements

- A watch table has been created.
- An online connection to the CPU exists.
- The watch table has to be in expanded mode.

#### Procedure

To modify tags "with trigger", follow these steps:

1. Enter the desired addresses and modify values in the watch table.
2. Select the addresses to be modified by selecting the check boxes for modifying in the column after the "Modify value".   
   A yellow triangle appears behind the selected check box, indicating that the address is now selected for modifying but has not yet been modified.
3. Switch to expanded mode using the icon "Show/hide advanced settings columns" in the toolbar or the "Online > Expanded mode" command.

   The "Monitor with trigger" and "Modify with trigger" columns are displayed.
4. In the "Modify with trigger" column, select the desired modify mode from the drop-down list box. The following options are available:

   - Permanent
   - Permanently, at start of scan cycle
   - Once only, at start of scan cycle
   - Permanently, at end of scan cycle
   - Once only, at end of scan cycle
   - Permanently, at transition to STOP
   - Once only, at transition to STOP
5. Start modifying using the "Online > Modify > Modify with trigger" command.
6. Confirm the prompt with "Yes" if you want to start modifying with trigger.

#### Result

The selected tags are modified using the selected monitoring and modify mode. The yellow triangle is no longer displayed.

> **Note**
>
> **When modifying, note the following:**
>
> Modifying can **not** be undone!

### Enable peripheral outputs

#### Introduction

The "Enable peripheral outputs" function deactivates the command output disable of the peripheral outputs. You can then modify the peripheral outputs when the CPU is in STOP mode.

This function is available in the watch table in "Expanded mode" only and only for CPUs of the S7-300/400 and S7-1200 family.

| Symbol | Meaning |
| --- | --- |
|  | **Danger** |
| **Danger when enabling the peripheral outputs:**  Attention, the enabling of the peripheral outputs can cause serious personal injury and material damage!  Make certain that dangerous conditions cannot occur before you execute the "Enable peripheral outputs" function. |  |

#### Prerequisites

- A watch table has been created.
- An online connection to the CPU exists.
- The CPU is in STOP mode before you can enable the peripheral outputs.
- The watch table has to be in expanded mode.
- The option [Force](Testing%20with%20the%20force%20table.md#introduction-to-forcing-tags) of tags must not be enabled.

> **Note**
>
> **"Enable peripheral outputs" function**
>
> - This function is possible only in STOP mode. The function is exited by an operating state change of the CPU and by the termination of the online connection.
> - While the function is enabled, forcing is not possible.

#### Procedure

To enable the peripheral outputs in STOP mode, follow these steps:

1. Enter the desired addresses and modify values in the watch table.
2. Select the addresses to be modified by selecting the check boxes for modifying in the column after the "Modify value".   
   A yellow triangle appears behind the selected check box, indicating that the address is now selected for modifying but has not yet been modified.
3. Switch to expanded mode using the icon "Show/hide advanced settings columns" in the toolbar or the "Online > Expanded mode" command.

   The "Monitor with trigger" and "Modify with trigger" columns are displayed.
4. Change the relevant CPU to STOP using the operator panel.
5. Right-click to open the shortcut menu and select "Enable peripheral outputs".
6. Confirm the prompt with "Yes" if you want to unlock the command output disable for the peripheral outputs.
7. Modify the peripheral outputs using the "Online > Modify > Modify now" command.

#### Result

The peripheral outputs are modified with the selected modify values. The yellow triangle is no longer displayed.

#### Enabling the peripheral outputs

The "Enable peripheral outputs" function remains active until:

- The "Enable peripheral outputs" command is deactivated again via the shortcut menu or via the "Online > Modify > Enable peripheral outputs" command.
- The CPU is no longer in STOP mode.
- The online connection is terminated.

  > **Note**
  >
  > **When modifying, note the following:**
  >
  > Modifying can **not** be undone!

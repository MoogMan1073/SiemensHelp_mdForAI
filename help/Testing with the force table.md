---
title: "Testing with the force table"
package: ProgForce2MenUS
topics: 32
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Testing with the force table

This section contains information on the following topics:

- [Introduction for testing with the force table](#introduction-for-testing-with-the-force-table)
- [Safety precautions when forcing tags](#safety-precautions-when-forcing-tags)
- [Layout of the force table](#layout-of-the-force-table)
- [Basic mode and expanded mode in the force table](#basic-mode-and-expanded-mode-in-the-force-table)
- [Icons in the force table](#icons-in-the-force-table)
- [Open and edit force table](#open-and-edit-force-table)
- [Entering tags in the force table](#entering-tags-in-the-force-table)
- [Monitoring tags in the force table](#monitoring-tags-in-the-force-table)
- [Forcing tags in the force table](#forcing-tags-in-the-force-table)
- [Stop forcing tags](#stop-forcing-tags)

## Introduction for testing with the force table

### Overview

You can use the force table to assign permanent values to individual tags

of the user program. This action is referred to as "forcing".

The following functions are available in the [force table](#) (The force table allows you to monitor and force tags in the user program. Forcing is used to permanently assign fixed values to individual peripheral outputs of a CPU.) :

- **Monitoring tags**

  This allows the current values of the individual tags of a user program or a CPU to be displayed on the programming device or PC. Tags can be monitored with or without a trigger condition.
- **Forcing tags**

  This function lets you assign a fixed value to individual I/O tags of the user program.

### Monitoring and forcing tags

The monitoring and forcing of tags is always dependent on the operand scope of the CPU used.

The following tags can be monitored:

- Inputs, outputs, and bit memories
- Contents of data blocks
- Peripheral inputs

The following tags can be forced:

- Peripheral inputs
- Peripheral outputs

### Example

Independent of the CPU used, only I/O can be forced, such as: "Tag_1":P or "QW0:P" or "IW0:P". Note that "Tag_1":P must not be the symbolic name of a bit memory.

### Possible applications

One advantage of the force table is that you can simulate different test environments and overwrite tags in the CPU with a permanent value. This enables you to intervene in the ongoing process for regulating purposes.

---

**See also**

[Layout of the force table](#layout-of-the-force-table)
  
[Basic mode and expanded mode in the force table](#basic-mode-and-expanded-mode-in-the-force-table)
  
[Icons in the force table](#icons-in-the-force-table)
  
[Open and edit force table](#open-and-edit-force-table)

## Safety precautions when forcing tags

### Safety precautions when forcing tags

Because the forcing function allows you to intervene permanently in the process, observance of the following notices is essential:

| Symbol | Meaning |
| --- | --- |
|  | **Danger** |
| **Prevent personal injury and material damage!**  Note that an incorrect action when executing the "Force" function can:  - Harm persons or pose a health hazard. - Cause damage to machinery or the entire plant. |  |

| Symbol | Meaning |
| --- | --- |
|  | **Caution** |
| **Prevent personal injury and material damage!**  - Before you start the "Force" function, you should ensure that no one else is currently executing this function on the same CPU. - Forcing can only be stopped by clicking the "Stop forcing" icon or using the "Online &gt; Force &gt; Stop forcing" command. Closing the active force table does **not** stop the forcing! - Forcing can **not** be undone! - Review the differences between " [modifying tags"](Testing%20with%20the%20watch%20table.md#introduction-to-modifying-tags) and "[forcing tags"](#introduction-to-forcing-tags). - If a CPU does not support the "Force" function, the relevant icons cannot be selected. - If the function "Enable peripheral outputs" is active on your CPU, then forcing is **not** possible on this CPU. If desired, deactivate this function in the watch table. |  |

## Layout of the force table

### Introduction

In the force table, enter the CPU-wide tags that you have defined and selected and which are to be forced in the allocated CPU. Only peripheral inputs and peripheral outputs can be forced.

For each CPU created in the project, a force table will automatically be created in the "Watch and force tables" folder. Only one force table can be allocated to a CPU. This force table displays all the addresses forced in the allocated CPU.

### Layout of the force table

The columns displayed in the force table depend on the mode you are working in: basic mode or expanded mode.

In expanded mode the "Monitor with trigger" column is also displayed.

### Meaning of the columns

The following table shows the meaning of the individual columns in basic mode and expanded mode:

| Mode | Column | Meaning |
| --- | --- | --- |
| Basic mode | ![Meaning of the columns](images/21259497483_DV_resource.Stream@PNG-de-DE.PNG) | Identification column |
| Name | Name of the inserted tag |  |
| Address | Address of the inserted tag |  |
| Display format | Selected display format |  |
| Monitor value | Values of the tags, dependent on the selected display format. |  |
| Force value | Value with which the tag is forced. |  |
| ![Meaning of the columns](images/20405036939_DV_resource.Stream@PNG-de-DE.png) ("Force") | Select the tag to be forced by activating the corresponding check box. |  |
| Comment | Option to enter a comment to document the tags in the force table. |  |
| Tag comment | Display of the comment on the selected tag that was entered in other editors.  This column cannot be edited. |  |
| The following additional column is shown in expanded mode: | Monitor with trigger | Display of selected monitoring mode |

---

**See also**

[Icons in the force table](#icons-in-the-force-table)
  
[Basic mode and expanded mode in the force table](#basic-mode-and-expanded-mode-in-the-force-table)

## Basic mode and expanded mode in the force table

### Difference between basic mode and expanded mode in the force table

In expanded mode the "Monitor with trigger" column is also displayed in the force table.

You will find a detailed list of the columns under [Layout of the force table](#layout-of-the-force-table).

### Switching between basic mode and expanded mode

You have the following options of toggling between the basic and expanded mode:

- Click the icon "Show/hide advanced setting columns". Click this icon again to return to the basic mode.

  Or:
- In the "Online" menu, select the "Expanded mode" check box. Deactivate this check box to return to the basic mode.

### Functionality in expanded mode

The following functionality is only possible in expanded mode:

- Monitor with trigger
- Monitor peripheral inputs

## Icons in the force table

### Meaning of the icons

The following table shows the meaning of the icons in the force table:

| Icon | Meaning |
| --- | --- |
| ![Meaning of the icons](images/20439401867_DV_resource.Stream@PNG-de-DE.PNG) | Identifies a table inside the project tree as a force table. |
| ![Meaning of the icons](images/21259497483_DV_resource.Stream@PNG-de-DE.PNG) | Identification column |
| ![Meaning of the icons](images/57241034763_DV_resource.Stream@PNG-de-DE.png) | Inserts a row before the selected row. |
| ![Meaning of the icons](images/57243271051_DV_resource.Stream@PNG-de-DE.png) | Inserts a row after the selected row. |
| ![Meaning of the icons](images/95715440011_DV_resource.Stream@PNG-de-DE.png) | Inserts a comment line above the selected row. |
| ![Meaning of the icons](images/21262260107_DV_resource.Stream@PNG-de-DE.PNG) | Displays all columns of expanded mode. If you click this icon again, the columns of the expanded mode will be hidden. |
| ![Meaning of the icons](images/69398885131_DV_resource.Stream@PNG-de-DE.png) | Updates all operands and values currently being forced on the CPU in the open force table. |
| ![Meaning of the icons](images/13510896267_DV_resource.Stream@PNG-de-DE.png) | Starts forcing for all addresses of the selected tags. If forcing is already running, the previous action is replaced without interruption. |
| ![Meaning of the icons](images/20453765131_DV_resource.Stream@PNG-de-DE.PNG) | Stops forcing of addresses in the force table. |
| ![Meaning of the icons](images/20455001099_DV_resource.Stream@PNG-de-DE.PNG) | Starts monitoring of the visible tags in the force table. The default setting for monitoring in basic mode is "permanent". In expanded mode an additional column is shown and you can set certain trigger points for monitoring tags. |
| ![Meaning of the icons](images/13511997579_DV_resource.Stream@PNG-de-DE.png) | Starts monitoring of the visible tags in the force table. This command is executed immediately and the tags are monitored once. |
| ![Meaning of the icons](images/20405036939_DV_resource.Stream@PNG-de-DE.png) | Displays the check box for the selection of tags to be forced. |
| ![Meaning of the icons](images/20510956427_DV_resource.Stream@PNG-de-DE.PNG) | Indicates that an address cannot be fully forced. Example: It is possible to force the address QW0:P, but it is not possible to force the address QD0:P because this address area is potentially not available on the CPU. |
| ![Meaning of the icons](images/20460189195_DV_resource.Stream@PNG-de-DE.PNG) | Indicates that an address cannot be monitored. |
| ![Meaning of the icons](images/8395965067_DV_resource.Stream@PNG-de-DE.png) | Indicates that an address is being forced. |
| ![Meaning of the icons](images/8395973515_DV_resource.Stream@PNG-de-DE.png) | Indicates that an address is being partly forced. |
| ![Meaning of the icons](images/21507942027_DV_resource.Stream@PNG-de-DE.PNG) | Indicates that the associated peripheral address is being forced. |
| ![Meaning of the icons](images/8395313547_DV_resource.Stream@PNG-de-DE.png) | Indicates that a syntax error occurred. |
| ![Meaning of the icons](images/13516393483_DV_resource.Stream@PNG-de-DE.png) | Indicates that the address is selected but has not been forced yet. |
| ![Meaning of the icons](images/8395330443_DV_resource.Stream@PNG-de-DE.png) | Indicates that the selected tag was monitored for the value "1". |
| ![Meaning of the icons](images/8395351691_DV_resource.Stream@PNG-de-DE.png) | Indicates that the selected tag was monitored for the value "0". |
| ![Meaning of the icons](images/8395279499_DV_resource.Stream@PNG-de-DE.png) | Indicates that the address is being used more than once. |
| ![Meaning of the icons](images/8395918219_DV_resource.Stream@PNG-de-DE.png) | Indicates that a substitute value is being used. Substitute values are values that are output to the process in case of signal output module faults or are used instead of a process value in the user program in case of signal input module faults. The substitute values can be assigned by the user (e.g., retain old value). |

---

**See also**

[Layout of the force table](#layout-of-the-force-table)

## Open and edit force table

This section contains information on the following topics:

- [Display force table](#display-force-table)
- [Open force table](#open-force-table)
- [Save force table](#save-force-table)

### Display force table

#### Introduction

You cannot create a new force table; one force table already exists for each CPU. It is permanently allocated to this CPU and cannot be copied or duplicated.

#### Requirements

A project with an allocated CPU has to be open.

#### Displaying a force table

The force table is always displayed below a CPU in the "Watch and force tables" folder.

### Open force table

#### Requirements

A project with an allocated CPU must be created.

#### Procedure

Proceed as follows to open a force table:

1. Open the "Watch and force tables" folder below the desired CPU.
2. Double-click the "Force table" in this folder.

#### Result

The selected force table opens.

### Save force table

#### Requirements

A project with an allocated CPU has been created.

#### Procedure

Proceed as follows to save a force table:

1. Enter the desired changes in the force table.
2. Select the "Save" command in the "Project" menu or click the "Save project" icon in the toolbar. Note that this save operation will save the entire project.

#### Result

The contents of the force table and the associated project are saved.

> **Note**
>
> You cannot rename a force table.

## Entering tags in the force table

This section contains information on the following topics:

- [Basic principles for entering tags in the force table](#basic-principles-for-entering-tags-in-the-force-table)
- [Permitted operands for the force table](#permitted-operands-for-the-force-table)
- [Permitted force values for the force table](#permitted-force-values-for-the-force-table)
- [Overview of the display formats](#overview-of-the-display-formats)
- [Selecting the display format for tags](#selecting-the-display-format-for-tags)
- [Creating and editing comment lines](#creating-and-editing-comment-lines)

### Basic principles for entering tags in the force table

#### Recommended procedure

Select the tags whose values you want to monitor or force, and enter them in the force table.

When entering tags in the force table, please note that these tags must be previously defined in the PLC tag table.

#### Example of filling out a force table

- You can enter the absolute address that is to be forced or monitored in the "Address" column or you can enter the symbolic name of the tag in the "Name" column.
- Select the display format you require from the drop-down list in the "Display format" column, if you do not want to use the default setting.
- Now you have to decide whether you want to monitor or force the entered tags. Enter the required force value and a comment in the appropriate columns of the force table.
- Note that only peripheral inputs and peripheral outputs can be forced and review the [Safety precautions when forcing tags](#safety-precautions-when-forcing-tags-1).

#### Create comment line

If required, you can create a comment row by entering the string "//" in the "Name" column.

#### Syntax check

When you enter tags in the force table, the syntax of each cell will be checked when you exit the cell. Incorrect entries are marked in red.

> **Note**
>
> When you place the mouse pointer in a cell marked in red, brief information is displayed with additional notes on the error.

### Permitted operands for the force table

#### Permitted operands for the force table

The following table shows the operands that are permitted for forcing in the force table:

| Permitted operand | Example of data type | Example (International mnemonics) |
| --- | --- | --- |
| Peripheral input/peripheral output | BOOL | I0.0:P; Q0.0:P |
| Peripheral input/peripheral output | BYTE | IB1:P; QB1:P |
| Peripheral input/peripheral output | WORD | IW2:P; QW3:P |
| Peripheral input/peripheral output | DWORD | ID2:P; QD1:P |

The following table shows the operands that are permitted for monitoring in the force table:

| Permitted operand | Example of data type | Example (International mnemonics) |
| --- | --- | --- |
| Input/output/bit memory | BOOL | I1.0, Q1.7, M10.1  I0.0:P |
| Input/output/bit memory | BYTE | IB1/QB10/MB100  IB1:P |
| Input/output/bit memory | WORD | IW1; QW10; MW100  IW2:P |
| Input/output/bit memory | DWORD | ID4; QD10; MD100  ID2:P |
| Timers | TIMER | T1 |
| Counters | COUNTER | C1 |
| Data block | BOOL | DB1.DBX1.0 |
| Data block | BYTE | DB1.DBB1 |
| Data block | WORD | DB1.DBW1 |
| Data block | DWORD | DB1.DBD1 |

> **Note**
>
> You cannot enter "DB0..." because it is used by the system!

> **Note**
>
> **No access to peripheral bits for S7-400 CPUs**
>
> The force table does not allow S7-400 CPUs to access peripheral bits, e.g. %I0.0:P; %Q0.0:P.
>
> These bits cannot be forced.

### Permitted force values for the force table

#### Entering force values in the force table

The following table shows the operands that are permitted for entering force values in the force table:

All tables
Bit operands
Byte operands
Word operands
Double word operands

Bit operands

| Possible bit operands | Example for permitted force values |
| --- | --- |
| I1.0:P | True |
| I1.1:P | False |
| Q1.0P | 0 |
| Q1.1:P | 1 |
| I2.0:P | 2#0 |
| I2.1:P | 2#1 |

Byte operands

| Possible byte operands | Example for permitted force values |
| --- | --- |
| IB1:P | 2#00110011 |
| IB2:P | B#16#1F |
| QB14:P | 1F |
| QB10:P | 'a' |
| IB3:P | 10 |

Word operands

| Possible word operands | Example for permitted force values |
| --- | --- |
| IW0:P | 2#0011001100110011 |
| IW2:P | W#16#ABCD |
| QW10:P | ABCD |
| QW12:P | B#(12, 34) |
| IW4:P | 'ab' |
| IW6:P | 12300 |
| IW8:P | S5T#9S_300ms |
| IW10:P | C#123 |
| IW12:P | D#2006-12-31 |

Double word operands

| Possible double word operands | Example for permitted force values |
| --- | --- |
| ID0:P | 2#00110011001100110011001100110011 |
| ID4:P | 1.2 |
| QD10:P | 1.234.e4 |
| QD14:P | Dw#16#abcdef10 |
| ID8:P | 16#ABCDEF10 |
| ID12:P | b#(12,34,56,78) |
| ID16:P | L#-12 |
| ID20:P | L#12 |
| ID24:P | 123456789 |
| ID28:P | 123456789 |
| ID32:P | T#12s300ms |
| ID36:P | Tod#14:20:40.645 |
| ID40:P | P#e0.0 |

### Overview of the display formats

#### Display formats in the force table

The display format you select specifies the representation of a tag value.

When entering the address a display format is automatically preset. If you want to change this, you can select a display format from the drop-down list in the "Display formats" column. The drop-down list only offers the display formats which are valid for this data type. The display format that appears first in the list is the pre-selected format.

#### Example

The following table shows the 32-bit data types permitted for all CPU families in the force table and their possible display formats:

| Data type | Possible display formats |
| --- | --- |
| BOOL | Bool, Hex, BCD, Octal, Bin, Dec, Dec+/- |
| BYTE | Hex, BCD, Octal, Bin, Dec, Dec+/-, Character |
| WORD | Hex, BCD, Octal, Bin, Dec, Dec+/-, Dec_Sequence, Character, SIMATIC_Time, Date, Unicode_Character, Counter |
| DWORD | Hex, BCD, Octal, Bin, Dec, Dec+/-, Dec_Sequence, Character, Floating-point number, Time of day, Timer, Unicode_Character |
| SINT | Dec, Dec+/-, Hex, BCD, Octal, Bin, Character |
| INT | Dec, Dec+/-, Hex, BCD, Octal, Bin, Character, Unicode_Character, Dec_Sequence, SIMATIC_Time, Counter, Date |
| DINT | Dec, Dec+/-, Hex, BCD, Octal, Bin, Character, Unicode_Character, Dec_Sequence, Time of day, Timer |
| USINT | Dec, Dec+/-, Hex, BCD, Octal, Bin, Character |
| UINT | Dec, Dec+/-, Hex, BCD, Octal, Bin, Character, Unicode_Character, Dec_Sequence, SIMATIC_Time, Counter, Date |
| UDINT | Dec, Dec+/-, Hex, BCD, Octal, Bin, Character, Unicode_Character, Dec_Sequence, Time of day, Timer |
| REAL | Floating-point number, Hex, BCD, Octal, Bin, Character, Unicode_Character, Dec,  Dec+/-, Dec_Sequence, Time of day, Timer |
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
| LREAL | In a project created with TIA Portal &lt; V12:   Floating-point number   Note: The display of LREAL is limited to 13 digits plus exponent. |
| LREAL | In a project created with TIA Portal &gt;= V12:   Floating-point number, Hex, BCD, Octal, Bin, Character, Unicode_Character, Dec, Dec+/-, Dec_Sequence, Time of day, Time, Date and time  Note: The display of LREAL is limited to 13 digits plus exponent. |

For the S7-1500 CPU family, in addition to 32-bit data types, the 64-bit data types listed in the table are also permitted with the following possible display formats:

| Data type | Possible display formats |
| --- | --- |
| LWORD | Hex, Octal, BCD, Bin, Character, Unicode_Character, Dec, Dec+/-, Dec_Sequence, Floating-point number, Time of day, Time, Date and time |
| LINT | Dec+/-, Dec, Hex, BCD, Octal, Bin, Character, Unicode_Character, Dec_Sequence, Time of day, Time, Date and time |
| ULINT | Dec, Dec+/-, Hex, BCD, Octal, Bin, Character, Unicode_Character, Dec_Sequence, Time of day, Time, Date and time |
| LREAL | Floating-point number, Hex, BCD, Octal, Bin, Character, Unicode_Character, Dec, Dec+/-, Dec_Sequence, Time of day, Time, Date and time |
| LTIME | Timer, Dec+/-, Dec, Hex, Bin |
| LTOD | Dec, Hex, Bin, Time of day |
| LDT | Dec, Hex, Date and time, Bin |

For more information, refer to the description of the valid [data types](Data%20types.md#overview-of-the-valid-data-types).

> **Note**
>
> **Rounding of floating-point numbers**
>
> In the force table, floating-point numbers are stored as binary numbers in IEEE format. Because not every floating point number (real, longreal) that can be displayed on the user interface can be mapped to the IEEE format, there is a possibility that floating-point numbers will be rounded. If a rounded floating-point number in the force table is copied and, in turn, inserted in another input field, the rounding may cause a slight difference.

> **Note**
>
> **Only symbolic addressing is possible**
>
> In the force table, LongDataTypes such as LWORD or LREAL can only be addressed symbolically.

### Selecting the display format for tags

#### Procedure

To select the display format of the tags, follow these steps:

1. Enter the desired address in the force table.
2. Click the desired cell in the "Display format" column, and open the drop-down list.

   The permitted display formats are shown in the drop-down list.
3. Select the desired display format from the drop-down list.

**Note**

If the selected display format cannot be applied, then the last selected display format will be displayed automatically.

### Creating and editing comment lines

#### Basic principles of comment lines

In addition to the row-related comments in the comment column, you can now also create complete comment lines to enhance the structure of the force table.

The contents of the comment line are stored in the "Languages &amp; Resources" folder in the "Project texts" tab and can be compiled in other project languages.

- Using the corresponding icon in the toolbar of the force table.
- Using the menu command "Insert &gt; Insert comment line".
- Using the shortcut menu command "Insert comment line".
- By entering the string "//" in the "Name" column of the force table.

#### Inserting comment lines

To insert comment lines, follow these steps:

1. Open the force table and enter the required addresses.
2. Insert a new comment line:

   - To do so, click the "Insert comment line" icon in the toolbar of the force table.
   - Or click the menu command "Insert &gt; Insert comment line".
   - Or click the shortcut menu command "Insert comment line".

     Result: A new comment line is inserted above the selected row in the force table.
3. Enter the required comment in the comment line. The entered comment is shown in green.
4. To show all comments you entered, double-click "Project texts" in the project tree under "Languages &amp; Resources".
5. If you are working in multi-lingual projects and want your comment to be translated into other languages, you can set the project languages required in addition to the editing language in the project tree under "Languages &amp; Resources &gt; Project languages".

#### Creating comment lines

To create comment lines, follow these steps:

1. Open the force table and enter the required addresses.
2. Enter the character string "//" in a free row in the "Name" column. This turns the row into a comment line.

   No comment lines can be created in the other columns.
3. Enter the required comment in the comment line. The entered comment is shown in green.
4. To show all comments you entered, double-click "Project texts" in the project tree under "Languages &amp; Resources".
5. If you are working in multi-lingual projects and want your comment to be translated into other languages, you can set the project languages required in addition to the editing language in the project tree under "Languages &amp; Resources &gt; Project languages".

#### Deleting comment lines

To delete comment lines, follow these steps:

1. Open a force table containing comment lines.
2. Delete the entire comment with the introductory string "//", if you no longer required this.
3. Alternatively, delete only the introductory string "//". In this case the existing comment is retained and is displayed in the "Comment" column in the force table.

   > **Note**
   >
   > **Deleting comment lines**
   >
   > When you delete comment lines the project languages and any existing translations for these comments are also deleted.

## Monitoring tags in the force table

This section contains information on the following topics:

- [Introduction to monitoring tags in the force table](#introduction-to-monitoring-tags-in-the-force-table)
- [Setting the monitoring mode in the force table](#setting-the-monitoring-mode-in-the-force-table)
- ["Monitor all" command for tags](#monitor-all-command-for-tags)
- ["Monitor now" command for tags](#monitor-now-command-for-tags)

### Introduction to monitoring tags in the force table

#### Introduction

Use the force table to monitor the tags of the configured input and output modules in the CPU, dependent on the [monitoring mode](#setting-the-monitoring-mode-in-the-force-table) you have selected. An online connection to the CPU must exist to monitor tags.

#### Options for monitoring tags

The following options are available for monitoring tags:

- Monitor all  
  This command starts the monitoring of all visible tags in the active force table, dependent on the selected monitoring mode:

  - In basic mode, the monitoring mode is set to "permanent" by default.
  - In expanded mode, you can specify defined trigger points for the monitoring of tags.

    > **Note**
    >
    > If the monitoring mode is changed while in expanded mode and then a switch is made to basic mode, the monitoring mode set before will also be applied in basic mode.
- Monitor now  
  This command starts the monitoring of the visible tags in the active force table immediately and once only.

#### CPU-specific limitations when monitoring tags

The following CPU-specific differences exist:

- CPU S7-300/400:  
  CPUs from this family can only monitor the first 30 characters of a string.
- CPU S7-1200:  
  CPUs from this family can monitor a string up to the total size of 254 characters.

### Setting the monitoring mode in the force table

#### Introduction

By selecting the monitoring mode, you specify the trigger point and the duration of tag monitoring in the [force table](#) (The force table allows you to monitor and force tags in the user program. Forcing is used to permanently assign fixed values to individual peripheral outputs of a CPU.) .

#### Possible monitoring mode (duration of monitoring)

The following selection options are available:

- Permanent
- Once only, at start of scan cycle
- Once only, at end of scan cycle
- Permanently, at start of scan cycle
- Permanently, at end of scan cycle
- Once only, at transition to STOP
- Permanently, at transition to STOP

#### Special features when using "Permanent" mode

The "Permanent" mode is executed as follows for the monitoring of tags: The inputs are monitored at the end of the cycle and the outputs at the start of the cycle.

#### Selecting the trigger point

The trigger points "Beginning of scan cycle", "End of scan cycle", and "Switch to stop" specify the time at which the tags are to be read from the CPU or updated in the CPU.

The following diagram shows the position of these trigger points:

![Selecting the trigger point](images/9165223563_DV_resource.Stream@PNG-en-US.png)

### "Monitor all" command for tags

#### Introduction

Use the "Monitor all" command to start monitoring the visible tags in the active force table. In basic mode of the force table, the default setting for the monitoring mode is "permanent". In expanded mode, you can specify defined trigger points for the monitoring of tags. In this case, the tags are monitored with reference to the specified trigger points.

#### Requirements

An online connection to the CPU exists.

#### Procedure

To execute the "Monitor all" command, follow these steps:

1. Enter the tags to be monitored and the corresponding addresses in the force table.
2. Switch to expanded mode by clicking

   the icon "Show/hide advanced setting columns" in the toolbar.
3. If you want to change the default monitoring mode for a tag, click the appropriate cell in the "Monitor with trigger" column and select the desired monitoring mode from the drop-down list.
4. Click the "Monitor all" icon in the toolbar.

#### Result

The tags of the active force table will be monitored using the set monitoring mode.

### "Monitor now" command for tags

#### Introduction

The "Monitor now" command starts the monitoring of tags immediately without reference to defined trigger points. The tag values are read out only once and displayed in the force table.

#### Requirements

An online connection to the CPU exists.

#### Procedure

To execute the "Monitor now" command, follow these steps:

1. Enter the tags to be monitored and the corresponding addresses in the force table.
2. Click the "Monitor now" icon in the toolbar.

#### Result

The tags of the active force table are monitored immediately and once only.

## Forcing tags in the force table

This section contains information on the following topics:

- [Introduction to forcing tags](#introduction-to-forcing-tags)
- [Safety precautions when forcing tags](#safety-precautions-when-forcing-tags-1)
- [Updating forced operands](#updating-forced-operands)
- [Force tags to "0"](#force-tags-to-0)
- [Force tags to "1"](#force-tags-to-1)
- ["Force all" command for tags](#force-all-command-for-tags)

### Introduction to forcing tags

#### Introduction

You can use the force table to assign permanent values to individual tags of the user program. This action is referred to as forcing. Only peripheral inputs and peripheral outputs can be forced.

To use the forcing function, you must have an online connection to the CPU and the utilized CPU must support this functionality.

If you open a force table in the "Watch and force tables" folder below a CPU on which a force job is already running, you will first be prompted to update the display of the forced operand. Forcing or stopping forcing in the open force table is only possible following this command.

#### Possible applications

By permanently assigning defined values to tags, you can specify defined default settings for your user program and, thus, test the programmed functions. Forcing is possible in [basic mode and in expanded mode](#basic-mode-and-expanded-mode-in-the-force-table).

#### Caution when forcing tags

Before forcing, make sure that you review the [safety precautions for this procedure](#safety-precautions-when-forcing-tags-1).

| Symbol | Meaning |
| --- | --- |
|  | **Danger** |
| **Prevent personal injury and material damage!**  Remember that an incorrect action when executing the "Force" function can:  - Harm persons or pose a health hazard. - Cause damage to machinery or the entire plant. |  |

#### Options for forcing tags

The following options are available for forcing tags:

- Force to "0"

  This command forces the selected address in the CPU to the force value "0".
- Force to "1"

  This command forces the selected address in the CPU to the force value "1".
- Force all

  This command starts the forcing of enabled addresses in the active force table or replaces an existing force job without interruption.
- Stop forcing

  This command stops the forcing of all addresses in the active force table.

#### Constraints when forcing tags

Note the following constraints when forcing:

- Forcing is always dependent on the operand scope of the CPU used.
- In principle, only peripheral inputs and peripheral outputs can be forced.
- If the function "Enable peripheral outputs" is active on your CPU, then forcing is not possible. If desired, deactivate this function in the watch table.

#### Unique aspects when forcing tags

Note that forcing of tags will overwrite values in the CPU and will continue even after the online connection to the CPU is terminated.

- **Stop forcing**

  Terminating the online connection is not sufficient to stop the forcing operation! To stop forcing, you must select the "Online &gt; Force &gt; Stop forcing" command. Only then will the tags that are visible in the active force table no longer be forced.
- **Stop forcing of individual tags**

  The "Online &gt; Force &gt; Stop forcing" command always applies to all tags displayed in the force table. To stop forcing individual tags, you must clear the check mark for forcing of these tags in the force table and restart forcing using the "Online &gt; Force &gt; Force all" command.

### Safety precautions when forcing tags

#### Safety precautions when forcing tags

Because the forcing function allows you to intervene permanently in the process, observance of the following notices is essential:

| Symbol | Meaning |
| --- | --- |
|  | **Danger** |
| **Prevent personal injury and material damage!**  Note that an incorrect action when executing the "Force" function can:  - Harm persons or pose a health hazard. - Cause damage to machinery or the entire plant. |  |

| Symbol | Meaning |
| --- | --- |
|  | **Caution** |
| **Prevent personal injury and material damage!**  - Before you start the "Force" function, you should ensure that no one else is currently executing this function on the same CPU. - Forcing can only be stopped by clicking the "Stop forcing" icon or using the "Online &gt; Force &gt; Stop forcing" command. Closing the active force table does **not** stop the forcing! - Forcing can **not** be undone! - Review the differences between " [modifying tags"](Testing%20with%20the%20watch%20table.md#introduction-to-modifying-tags) and "[forcing tags"](#introduction-to-forcing-tags). - If a CPU does not support the "Force" function, the relevant icons cannot be selected. - If the function "Enable peripheral outputs" is active on your CPU, then forcing is **not** possible on this CPU. If desired, deactivate this function in the watch table. |  |

### Updating forced operands

#### Introduction

If a force job is already running on a CPU, after opening the force table, you first need to make sure that the operands and values currently being forced on the CPU are displayed in the force table.

The command "Online" &gt; "Force" &gt; "Update forced operands" updates all operands and values currently being forced on the CPU in the open force table.

"Force" or "Stop forcing" in the open force table is only possible following this command.

#### Caution when forcing tags

Before forcing, make sure you are familiar with the [safety precautions when forcing tags](#safety-precautions-when-forcing-tags-1).

| Symbol | Meaning |
| --- | --- |
|  | **Danger** |
| **Prevent personal injury and material damage!**  Remember that an incorrect action when executing the "Force" function can:  - Harm persons or pose a health hazard. - Cause damage to machinery or the entire plant. |  |

#### Requirement

- An online connection to the CPU is possible.
- A force job is currently running on the CPU being used.

#### Procedure

To update the forced operands and values, follow these steps:

1. Open a force table.
2. Establish an online connection to the CPU.
3. Confirm the "Update forced operands" dialog that follows with "Yes".

#### Result

All forced operands in the open force table are updated with the relevant values. A red "F" is displayed in the first column indicating which operands are being forced.

This enables the "Force all" and "Stop forcing" buttons and you can select these functions.

> **Note**
>
> **When forcing, note the following:**
>
> - Forcing **cannot** be undone!
> - Terminating the online connection does **not** stop the forcing function!
> - To stop forcing, the forced address must be visible in the active force table.

### Force tags to "0"

#### Introduction

You can use the force function to assign permanent values to individual tags of a user program.

#### Caution when forcing tags

Before forcing, you must review the [safety precautions when forcing tags](#safety-precautions-when-forcing-tags-1).

| Symbol | Meaning |
| --- | --- |
|  | **Danger** |
| **Prevent personal injury and material damage!**  Note that an incorrect action when executing the "Force" function can:  - Pose a risk to the life or health of persons. - Cause damage to machinery or the entire plant. |  |

#### Requirements

- An online connection to the CPU exists.
- The utilized CPU supports the force function.
- The "Enable peripheral outputs" function is **not** enabled on the CPU on which the tags are to be forced. If desired, deactivate this function in the watch table.

#### Procedure

To force tags to "0", follow these steps:

1. Open the force table.
2. Enter the desired address in the force table.
3. Select the "Online &gt; Force&gt; Force to 0" command in order to force the selected address with the specified value.
4. Confirm the next dialog with "Yes".

#### Result

The selected address is forced to "0". The yellow triangle is no longer displayed. A red "F" is displayed in the first column, for example, indicating that the tag is being forced.

#### Stop forcing

To stop forcing, follow these steps:

1. Open the force table.
2. Select the "Online &gt; Force &gt; Stop forcing" command.
3. Confirm the next dialog with "Yes".

#### Result

Forcing of the selected values is stopped. The red "F" in the first column is no longer displayed. The yellow triangle reappears behind the check box again to indicate that the address is selected for forcing but is not being forced at the moment.

> **Note**
>
> **When forcing, note the following:**
>
> - Forcing **cannot** be undone!
> - Terminating the online connection does **not** stop the forcing!
> - To stop forcing, the forced address must be visible in the active force table.

### Force tags to "1"

#### Introduction

You can use the force function to assign permanent values to individual tags of a user program.

#### Caution when forcing tags

Before forcing, you must review the [safety precautions when forcing tags](#safety-precautions-when-forcing-tags-1).

| Symbol | Meaning |
| --- | --- |
|  | **Danger** |
| **Prevent personal injury and material damage!**  Note that an incorrect action when executing the "Force" function can:  - Endanger the life or health of personnel - Cause damage to machinery or the entire plant. |  |

#### Requirements

- An online connection to the CPU exists.
- The utilized CPU supports the force function.
- The "Enable peripheral outputs" function is **not** enabled on the CPU on which the tags are to be forced. If desired, deactivate this function in the watch table.

#### Procedure

To force tags to "1", follow these steps:

1. Open the force table.
2. Enter the desired address in the force table.
3. Select the "Online &gt; Force&gt; Force to 1" command in order to force the selected address with the specified value.
4. Confirm the next dialog with "Yes".

#### Result

The selected address is forced to "1". The yellow triangle is no longer displayed. A red "F" is displayed in the first column, for example, indicating that the tag is being forced.

#### Stop forcing

To stop forcing, follow these steps:

1. Open the force table.
2. Select the "Online &gt; Force &gt; Stop forcing" command.
3. Confirm the next dialog with "Yes".

#### Result

Forcing of the selected values is stopped. The red "F" in the first column is no longer displayed. The yellow triangle reappears behind the check box again to indicate that the address is selected for forcing but is not being forced at the moment.

> **Note**
>
> **When forcing, note the following:**
>
> - Forcing **cannot** be undone!
> - Terminating the online connection does **not** stop the forcing!
> - To stop forcing, the forced address must be visible in the active force table.

### "Force all" command for tags

#### Introduction

You can use the force function to assign permanent values to individual tags of a user program.

If forcing is already active, this forcing operation is replaced without interruption by the "Online &gt; Force &gt; Force all" command. Any forced addresses that are not selected will no longer be forced.

#### Caution when forcing tags

Before forcing, you must review the [safety precautions when forcing tags](#safety-precautions-when-forcing-tags-1).

| Symbol | Meaning |
| --- | --- |
|  | **Danger** |
| **Prevent personal injury and material damage!**  Note that an incorrect action when executing the "Force" function can:  - Pose a risk to the life or health of persons. - Cause damage to machinery or the entire plant. |  |

#### Requirements

- An online connection to the CPU exists.
- The utilized CPU supports the force function.
- The "Enable peripheral outputs" function is **not** enabled on the CPU on which the tags are to be forced. If desired, deactivate this function in the watch table.

#### Procedure

To force tags with the "Online &gt; Force &gt; Force all" command, follow these steps:

1. Open the force table.
2. Enter the desired addresses and force values in the force table.
3. Select the addresses to be forced by selecting the check boxes for forcing in the column after the "Force value".   
   A yellow triangle appears behind the selected check box, indicating that the address is selected for forcing but is not being forced at the moment.
4. Select the "Online &gt; Force&gt; Force all" command in order to force the selected addresses with the specified values.
5. Confirm the next dialog with "Yes".

#### Result

The selected addresses are forced to the specified values. The yellow triangle is no longer displayed. A red "F" is displayed in the first column, for example, indicating that the tag is being forced.

#### Stop forcing

To stop forcing, follow these steps:

1. Open the force table.
2. Select the "Online &gt; Force &gt; Stop forcing" command.
3. Confirm the next dialog with "Yes".

#### Result

Forcing of the selected addresses is stopped. The red "F" in the first column is no longer displayed. The yellow triangle reappears behind the check box again to indicate that the address is selected for forcing but is not being forced at the moment.

> **Note**
>
> **When forcing, note the following:**
>
> - Forcing **cannot** be undone!
> - Terminating the online connection does **not** stop the forcing!
> - To stop forcing, the forced address must be visible in the active force table.

## Stop forcing tags

This section contains information on the following topics:

- [Stop forcing all tags](#stop-forcing-all-tags)
- [Stop forcing individual tags](#stop-forcing-individual-tags)

### Stop forcing all tags

#### Introduction

Note the following before you stop forcing tags:

- Stopping forcing **cannot** be undone!
- Terminating the online connection does **not** stop the forcing!
- To stop forcing, the forced address must be visible in the active force table.

#### Caution when forcing tags

Before forcing, you must review the [safety precautions when forcing tags](#safety-precautions-when-forcing-tags-1).

| Symbol | Meaning |
| --- | --- |
|  | **Danger** |
| **Prevent personal injury and material damage!**  Note that an incorrect action when stopping the "Force" function can:  - Pose a risk to the life or health of persons. - Cause damage to machinery or the entire plant. |  |

#### Requirements

- Tags are forced in a force table.
- An online connection to the CPU exists.
- The utilized CPU supports the force function.
- The "Enable peripheral outputs" function is not enabled on the CPU on which the tags are to be forced. If desired, deactivate this function in the watch table.

#### Procedure

Proceed as follows to stop **forcing all tags** :

1. Open the force table.
2. Select the "Online &gt; Force &gt; Stop forcing" command in order to stop forcing the displayed addresses.
3. Confirm the "Stop forcing" dialog with "Yes".

#### Result

The forcing of all tags is stopped. The red "F" in the first column is no longer displayed. The yellow triangle reappears behind the check box again to indicate that the address is flagged for forcing but is not being forced at the moment.

### Stop forcing individual tags

#### Introduction

Note the following before you stop forcing tags:

- Stopping forcing **cannot** be undone!
- Terminating the online connection does **not** stop the forcing!
- To stop forcing, the forced address must be visible in the active force table.

#### Caution when forcing tags

Before forcing, you must review the [safety precautions when forcing tags](#safety-precautions-when-forcing-tags).

| Symbol | Meaning |
| --- | --- |
|  | **Danger** |
| **Prevent personal injury and material damage!**  Note that an incorrect action when stopping the "Force" function can:  - Pose a risk to the life or health of persons. - Cause damage to machinery or the entire plant. |  |

#### Requirements

- Tags are forced in a force table.
- An online connection to the CPU exists.
- The utilized CPU supports the force function.
- The "Enable peripheral outputs" function is not enabled on the CPU on which the tags are to be forced. If desired, deactivate this function in the watch table.

#### Procedure

Proceed as follows to stop **forcing individual tags** :

1. Open the force table.
2. Deactivate the check boxes for the addresses that are no longer to be forced.
3. Reselect the "Online &gt; Force" command.

#### Result

Forcing of the disabled addresses will be stopped. The red "F" in the first column is no longer displayed. The yellow triangle reappears behind the check box again to indicate that the address is flagged for forcing but is not being forced at the moment.

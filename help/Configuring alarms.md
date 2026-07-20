---
title: "Configuring alarms"
package: ProgAlarm34enUS
topics: 60
devices: [S7-1500, S7-1500T, S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Configuring alarms

This section contains information on the following topics:

- [Introduction to alarm configuration (S7-300, S7-400, S7-1500)](#introduction-to-alarm-configuration-s7-300-s7-400-s7-1500)
- [Assigning alarm numbers (S7-300, S7-400, S7-1500)](#assigning-alarm-numbers-s7-300-s7-400-s7-1500)
- [Components of an alarm (S7-300, S7-400, S7-1500)](#components-of-an-alarm-s7-300-s7-400-s7-1500)
- [Available alarm blocks (S7-300, S7-400, S7-1500)](#available-alarm-blocks-s7-300-s7-400-s7-1500)
- [Alarm type and alarms (S7-300, S7-400, S7-1500)](#alarm-type-and-alarms-s7-300-s7-400-s7-1500)
- [Formal parameters, alarm data types and alarm blocks (S7-300, S7-400, S7-1500)](#formal-parameters-alarm-data-types-and-alarm-blocks-s7-300-s7-400-s7-1500)
- [Layout of the alarm editor (S7-300, S7-400, S7-1500)](#layout-of-the-alarm-editor-s7-300-s7-400-s7-1500)
- [Working with the alarm editor (S7-300, S7-400, S7-1500)](#working-with-the-alarm-editor-s7-300-s7-400-s7-1500)
- [Creating and editing alarms (S7-300, S7-400)](#creating-and-editing-alarms-s7-300-s7-400)
- [Creating and editing alarms (S7-1500)](#creating-and-editing-alarms-s7-1500)
- [Texts and attributes (S7-300, S7-400, S7-1500)](#texts-and-attributes-s7-300-s7-400-s7-1500)
- [Text lists for alarms (S7-300, S7-400, S7-1500)](#text-lists-for-alarms-s7-300-s7-400-s7-1500)
- [Alarm classes (S7-300, S7-400, S7-1500)](#alarm-classes-s7-300-s7-400-s7-1500)
- [Exporting and importing alarm texts (S7-300, S7-400, S7-1500)](#exporting-and-importing-alarm-texts-s7-300-s7-400-s7-1500)

## Introduction to alarm configuration (S7-300, S7-400, S7-1500)

### Overview

Alarms allow you to detect errors in process control in the automation system quickly, to localize them precisely, and to eliminate them. This leads to a significant reduction in down times in the plant.

Before alarms can be output, they need to be configured.

You can create, edit and compile event-dependent alarms along with their alarm texts and alarm attributes and display them on display devices.

The table below lists the alarm types along with a brief description of their functions.

| Alarm type | Description |
| --- | --- |
| Program alarms | Program alarms are used to report program-synchronous events and are each assigned to a block. They are created in the program editor and edited in the alarm editor. |
| System diagnostic alarms | System diagnostic alarms are configuration-dependent module events and are activated or deactivated in the hardware configuration. They can only be viewed, not edited, in the alarm editor. |
| User diagnostic alarms | By means of user diagnostic alarms, you can write a user entry to the diagnostics buffer and send a corresponding alarm. They are assigned to a CPU. They are created in the alarm editor and can be edited there. |

## Assigning alarm numbers (S7-300, S7-400, S7-1500)

### Assigning numbers

The alarms are identified by a number that is unique within the CPU. This means that it is not necessary to recompile after copying complete programs. Copying a single block is an exception to this rule. Here, recompilation is necessary to include the changed alarm number (ID) in the program.

## Components of an alarm (S7-300, S7-400, S7-1500)

### Overview

How an alarm is displayed depends on the alarm method, the alarm block used and the display device.

The possible components of an alarm are listed in the following table:

| Component | Description |
| --- | --- |
| Time stamp | Generated when the alarm event occurs in the automation system. |
| Alarm state | The following are possible: Incoming, incoming with acknowledgment, outgoing, outgoing without acknowledgment, outgoing with acknowledgment. |
| Associated value | With some alarms, it is possible to add an associated value that can be evaluated by the alarm instruction being used. |
| Image | If there is a system crash, the resulting alarms can be displayed later on HMI devices. |
| Alarm number | A number (ID) assigned by the system that is unique within the CPU and identifies an alarm. |
| Alarm texts | Are configured by the user. |
| Group ID | A group of alarms can be acknowledged as a group if they are assigned the same value.   You can find information on configuring alarms in WinCC in the associated online help. |

## Available alarm blocks (S7-300, S7-400, S7-1500)

### S7-300/400: Overview of the alarm blocks

You can choose from the following alarm blocks:

- ALARM
- ALARM_8
- ALARM_8P
- NOTIFY
- ALARM_S
- ALARM_SQ
- AR_SEND (for sending archives; no configuration of alarm texts and alarm attributes possible)
- NOTIFY_8P
- ALARM_DQ
- ALARM_D
- ALARM_T

### S7-300/400: When do I use which alarm block?

The following table will help you to decide which alarm block to use for your application. The choice of alarm block depends on the following factors:

- The number of channels available in the block and therefore the number of signals to be monitored per block call.
- The possibility of acknowledging alarms.
- The possibility of including associated values.
- The display devices to be used.
- The configuration limits of the CPU.

| Alarm block | Channels | Acknowl- edgment | Associated values | Special features |
| --- | --- | --- | --- | --- |
| ALARM *) | 1 | Yes | up to 10 | Sends an alarm on rising or falling edge |
| ALARM_8 *) | 8 | Yes | - | Sends an alarm on rising or falling edge of one or more signals |
| ALARM_8P *) | 8 | Yes | up to 10 | as ALARM_8 |
| NOTIFY | 1 | no | up to 10 | as ALARM |
| NOTIFY_8P | 8 | no | up to 10 | as ALARM |
| AR_SEND | 1 | - | - | Used to send an archive; no configuration of alarm texts and alarm attributes possible |
| ALARM_SQ | 1 | Yes | 1 | With each block call and a signal change compared with the previous block call, an alarm is generated |
| ALARM_S | 1 | no | 1 | as ALARM_SQ |
| ALARM_DQ | 1 | Yes | 1 | as ALARM_SQ |
| ALARM_D | 1 | no | 1 | as ALARM_SQ |
| ALARM_T | - | - | - | Reserved for system test purposes |
| *) If acknowledgment-triggered alarming is activated, the alarm is not shown in the alarm view. |  |  |  |  |

### S7-1500: Overview of the alarm blocks

The following alarm block is available:

- Program_Alarm

The selection of the corresponding alarm class determines whether the block requires acknowledgment or not. The default setting is that the block does not require acknowledgment.

| Alarm block | Channels | Acknowl- edgment | Associated values | Special features |
| --- | --- | --- | --- | --- |
| Program_Alarm | 1 | possible | up to 10 | Sends an alarm with time stamp on rising or falling edge (see [Creating program alarms](#creating-program-alarms-s7-1500)). |

## Alarm type and alarms (S7-300, S7-400, S7-1500)

Using the program editors, you have the option of first creating an alarm type (which means an FB as template for instance DBs) and then alarms (which means instance DBs from the template of the alarm type).

### The block with alarm capability can be an FB or an instance DB

- With an FB you create an alarm type that serves as a template for alarms. All the input you make for the alarm type is automatically included for alarms derived from it. If you assign an instance DB to the FB, messages are generated automatically for the instance DB according to the template of the alarm type and alarm numbers are assigned.
- With an instance DB, you can modify the alarms generated based on the alarm type for the specific instance if they are not locked.

The visible difference is that alarm numbers are assigned to alarms whereas they are not assigned to an alarm type. The alarm types and corresponding instances are arranged one under the other in the alarm editor. By default, the table with the alarm instances is collapsed.

### Changing the data for an alarm type

If you change data for an alarm type, these changes are automatically included in the instances.   
Exceptions: You have already changed this data in the instance or have locked or unlocked data later in the alarm type.

> **Note**
>
> If you copy instances to a different program without copying the alarm type, then the instance will not be completely displayed. In this case, copy the alarm type to the new program as well.

### Resetting instance-specific data to the value of the alarm type

If attributes or texts were overwritten in an alarm instance, a type icon is displayed beside the attribute in the alarm editor. You can decide whether to use the value of the alarm type again for each attribute. In this case, no type icon is displayed.

---

**See also**

[Editing the alarm type (S7-300, S7-400)](#editing-the-alarm-type-s7-300-s7-400)
  
[Creating an instance DB and editing alarm instances (S7-300, S7-400)](#creating-an-instance-db-and-editing-alarm-instances-s7-300-s7-400)
  
[Basics for locking/unlocking texts and attributes (S7-300, S7-400, S7-1500)](#basics-for-lockingunlocking-texts-and-attributes-s7-300-s7-400-s7-1500)
  
[Locking new alarms and show/hide interlock symbols (S7-300, S7-400, S7-1500)](#locking-new-alarms-and-showhide-interlock-symbols-s7-300-s7-400-s7-1500)
  
[Creating alarm classes (S7-300, S7-400, S7-1500)](#creating-alarm-classes-s7-300-s7-400-s7-1500)
  
[Editing alarm classes (S7-300, S7-400, S7-1500)](#editing-alarm-classes-s7-300-s7-400-s7-1500)
  
[Working with the alarm editor (S7-300, S7-400, S7-1500)](#working-with-the-alarm-editor-s7-300-s7-400-s7-1500)

## Formal parameters, alarm data types and alarm blocks (S7-300, S7-400, S7-1500)

### Formal parameters as alarm number inputs (S7-300/400)

For each program alarm or group of program alarms, you require a formal parameter (name of the alarm) in your program that you specify as a STATIC parameter in the tag overview of your program. The formal parameter is used as an alarm number input and forms the basis for an alarm.

### Supplying the formal parameter with the suitable data type (S7-300/400)

The formal parameter must be assigned an alarm data type in keeping with the alarm block being used.

### Alarm data types and corresponding alarm blocks

The following table shows the alarm data types with their corresponding alarm blocks and their properties. The values of the data types have the same names as the alarm blocks (exception: see table) and have the prefix "C_".

| SIMATIC system | Data type | Alarm block | Properties |
| --- | --- | --- | --- |
| S7-400 | C_Alarm_8 | ALARM_8 | 8 channels, with acknowledgment, no associated values |
| S7-400 | C_Alarm_8p | ALARM_8P | 8 channels, with acknowledgment, up to 10 associated values per channel |
| S7-400 | C_Notify | NOTIFY | 1 channel, no acknowledgment, up to 10 associated values |
| S7-400 | C_Alarm | ALARM | 1 channel, with acknowledgment, up to 10 associated values |
| S7-300/400 | C_Alarm_s | ALARM_S | 1 channel, no acknowledgment, up to 1 associated value |
| S7-300/400 | C_Alarm_s | ALARM_SQ | 1 channel, with acknowledgment, up to 1 associated value |
| S7-400 | C_Ar_Send | AR_SEND | Used to send an archive |
| S7-400 | C_Notify_8p | NOTIFY_8P | 8 channels, no acknowledgment, up to 10 associated values |
| S7-300/400 | C_Alarm_s | ALARM_DQ | 1 channel, with acknowledgment, up to 1 associated value |
| S7-300/400 | C_Alarm_s | ALARM_D | 1 channel, no acknowledgment possible, up to 1 associated value |
| S7-1500 | Program_Alarm | Program_Alarm | 1 channel, acknowledgment possible by parameter assignment, up to 10 associated values |

## Layout of the alarm editor (S7-300, S7-400, S7-1500)

### Layout of the alarm editor

The following graphic shows an example of the components in the alarm editor:

![Layout of the alarm editor](images/88417163659_DV_resource.Stream@PNG-en-US.png)

|  |  |  |
| --- | --- | --- |
| 1 |  | Tabular display of the alarms in the work area, see: [Working with the alarm editor](#working-with-the-alarm-editor-s7-300-s7-400-s7-1500) |
| 2 | ![Layout of the alarm editor](images/41059615115_DV_resource.Stream@PNG-de-DE.png) | "Program alarms" tab: You can edit program alarms here. See [Basics of the work area](Introduction%20to%20the%20TIA%20Portal.md#basics-of-the-work-area) |
| 3 | ![Layout of the alarm editor](images/41057881227_DV_resource.Stream@PNG-de-DE.png) | "System alarms" tab: System alarms can only be viewed and cannot be edited. These alarms are configured in the device properties (shortcut menu command "Go to Device") as well as in the project navigation under "Common data &gt; System diagnostics settings". |
| 4 |  | The "Alarm instances" table contains the instances (instance DBs) derived from the alarm type (FB). As default, the table is collapsed. |
| 5 |  | [Inspector window](Introduction%20to%20the%20TIA%20Portal.md#inspector-window) |
|  | ![Layout of the alarm editor](images/41057891083_DV_resource.Stream@PNG-de-DE.png) | "User diagnostics alarms" tab: User diagnostics alarms can be created and edited here.   The tab is not available for S7-1500 CPUs. |
|  | ![Layout of the alarm editor](images/70582271243_DV_resource.Stream@PNG-de-DE.PNG) | Save window settings: The current window settings will be restored when the PLC alarms are opened again. |

You can enter or modify the necessary parameters, texts and attributes in the table or in the Inspector window. You can sort the table columns in ascending or descending order.

### Display of the CPU name in system alarms

As of V15.1, the name of the CPU (or for H or R CPUs, the name of the station) is displayed in the "Additional text 1" column of the system alarms. To do this, you need to compile the hardware of the device in question. If the CPU name is not displayed via the "Compile &gt; Hardware (only changes)" option, use the option "Compile &gt; Hardware (rebuild all)".

Make sure that loading to the device is actually performed since the message that the hardware is up-to-date is not enough!

## Working with the alarm editor (S7-300, S7-400, S7-1500)

Below are some basic procedures for working with the alarm editor.

### Show/hide alarm instances

The table with the alarm instances is collapsed when you open the alarm editor for the first time. You can change the split between the two tables with the mouse. To do this, click between the two areas and change the spacing by moving the divider to the left or right while keeping the mouse button pressed. The Speedy Splitter (the two small arrow keys) allows you to use a single click to minimize the table view, maximize the table view or restore the last selected split.

### Sorting tables in ascending or descending order

To sort a table by a column in ascending or descending order, follow the steps below:

1. Click the table header of a column if you want to sort the column in ascending order.
2. Click again on the same column of the table header to sort the column in descending order.
3. Click a third time on the table header of the same column to cancel the sorting.

### Copying/pasting cells

You can select one or more cells and insert them at a different position. The data is checked and, if it is valid, the shortcut menu command "Copy" is enabled. The data is checked again at the point of insertion and, if it is valid, the shortcut menu command "Paste" is enabled. If the data is invalid, the shortcut menu commands are grayed out.

## Creating and editing alarms (S7-300, S7-400)

This section contains information on the following topics:

- [Creating program alarms (S7-300, S7-400)](#creating-program-alarms-s7-300-s7-400)
- [Editing program alarms in the alarm editor (S7-300, S7-400)](#editing-program-alarms-in-the-alarm-editor-s7-300-s7-400)
- [Editing program alarms in the program editor (S7-300, S7-400)](#editing-program-alarms-in-the-program-editor-s7-300-s7-400)
- [Deleting program alarms (S7-300, S7-400)](#deleting-program-alarms-s7-300-s7-400)
- [Editing the alarm type (S7-300, S7-400)](#editing-the-alarm-type-s7-300-s7-400)
- [Creating an instance DB and editing alarm instances (S7-300, S7-400)](#creating-an-instance-db-and-editing-alarm-instances-s7-300-s7-400)
- [Creating user diagnostic alarms (S7-300, S7-400)](#creating-user-diagnostic-alarms-s7-300-s7-400)
- [Editing user diagnostic alarms (S7-300, S7-400)](#editing-user-diagnostic-alarms-s7-300-s7-400)
- [Deleting user diagnostic alarms (S7-300, S7-400)](#deleting-user-diagnostic-alarms-s7-300-s7-400)
- [Insert associated values in alarms (S7-300, S7-400)](#insert-associated-values-in-alarms-s7-300-s7-400)
- [Structure of associated values (S7-300, S7-400)](#structure-of-associated-values-s7-300-s7-400)
- [Examples of associated values (S7-300, S7-400)](#examples-of-associated-values-s7-300-s7-400)
- [Deleting associated values (S7-300, S7-400)](#deleting-associated-values-s7-300-s7-400)

### Creating program alarms (S7-300, S7-400)

#### Requirement

You have created a function block.

#### Procedure

To create a program alarm, follow these steps:

1. In the "Program blocks" folder in the project navigation, select the function block (FB) for which you want to create a program alarm and double-click the block to open it.
2. Click "Extended instructions" &gt; "Alarms" in the "Instructions" task card and drag the required alarm block (e.g., "Alarm_S") into the instruction window or network (depending on the block language).  
   Result: The instruction part of the FB displays the inputs of the called alarm block, in this case the ALARM_S block.
3. Fill in the block interface. For each alarm block that will be called in the FB, you will need to declare tags in the calling FB. For this purpose, enter the following tags, for example:

   - For the "STATIC" parameter, a name for the alarm block input, for example, "Alarm01" and the data type (C_Alarm_s).
   - Assign the name that you entered for the alarm block input to the "EV_ID" tag, in this case "Alarm01" and ID_16#eeee.
4. Repeat steps 2 through 3 for all alarm block calls in this FB.

**Note**

If, instead of an alarm block in the CPU, you call an FB with multiple instances in which alarms are also configured, you also need to configure the alarms of the FB with multiple instances in the calling block.

### Editing program alarms in the alarm editor (S7-300, S7-400)

#### Requirement

You have created a program alarm.

#### Procedure

To edit program alarms, follow these steps:

1. Double-click "PLC supervisions &amp; alarms" in the project navigation. Select the "Alarms" tab. The alarm editor opens.
2. Enter the required texts and attributes in the appropriate columns.

---

**See also**

[Basics for locking/unlocking texts and attributes (S7-300, S7-400, S7-1500)](#basics-for-lockingunlocking-texts-and-attributes-s7-300-s7-400-s7-1500)
  
[Locking new alarms and show/hide interlock symbols (S7-300, S7-400, S7-1500)](#locking-new-alarms-and-showhide-interlock-symbols-s7-300-s7-400-s7-1500)

### Editing program alarms in the program editor (S7-300, S7-400)

#### Requirement

You have created a program alarm.

#### Procedure

To edit program alarms, follow these steps:

1. Select the appropriate line in the block interface.
2. Switch to the "Alarm" tab in the Inspector window.
3. Enter the required texts and attributes in the appropriate fields.

### Deleting program alarms (S7-300, S7-400)

#### Procedure

To delete a program alarm, follow these steps:

1. Open the block containing the alarm you want to delete.
2. Delete the alarm block inserted during creation in the instruction window or network (depending on the block language).
3. Select the corresponding row in the block interface and select "Delete" in the shortcut menu.

#### Result

The alarm is deleted.

### Editing the alarm type (S7-300, S7-400)

#### Procedure

To edit an alarm type, follow these steps:

1. Select the required alarm block.
2. Enter the texts you require or select the required attributes.   
   If you have selected a multichannel alarm block (for example, "ALARM_8"), you can assign a separate text and certain separate attributes to each subalarm.
3. If you do not want the texts or attributes of the instance to be changed, lock them in the alarm type.

**Note**

You must be working in the alarm editor to edit subalarms.

---

**See also**

[Alarm type and alarms (S7-300, S7-400, S7-1500)](#alarm-type-and-alarms-s7-300-s7-400-s7-1500)
  
[Basics for locking/unlocking texts and attributes (S7-300, S7-400, S7-1500)](#basics-for-lockingunlocking-texts-and-attributes-s7-300-s7-400-s7-1500)
  
[Locking new alarms and show/hide interlock symbols (S7-300, S7-400, S7-1500)](#locking-new-alarms-and-showhide-interlock-symbols-s7-300-s7-400-s7-1500)

### Creating an instance DB and editing alarm instances (S7-300, S7-400)

#### Requirement

You have already created an FB and created at least one alarm in it.

#### Procedure

To assign instance data blocks (DBs) to an alarm type and to edit the alarms for these DBs for specific instances, follow the steps below:

1. Double-click on "Add new block" in the project navigation, click on the "Data block (DB)" button that appears in the dialog and select the function block (alarm type) to which you want to assign the instance DB from the "Type" drop-down list.
2. Double-click "PLC supervisions &amp; alarms" in the project navigation. Select the "Alarms" tab to open the alarm configuration.
3. Enter the desired changes for the respective alarm instance.

#### Result

This completes the alarm configuration for the created instance DB.

---

**See also**

[Alarm type and alarms (S7-300, S7-400, S7-1500)](#alarm-type-and-alarms-s7-300-s7-400-s7-1500)
  
[Basics for locking/unlocking texts and attributes (S7-300, S7-400, S7-1500)](#basics-for-lockingunlocking-texts-and-attributes-s7-300-s7-400-s7-1500)
  
[Locking new alarms and show/hide interlock symbols (S7-300, S7-400, S7-1500)](#locking-new-alarms-and-showhide-interlock-symbols-s7-300-s7-400-s7-1500)

### Creating user diagnostic alarms (S7-300, S7-400)

User diagnostics alarms are assigned to a CPU. They are created and edited in the alarm editor.

#### Requirement

You have created a function block.

#### Procedure

To create a user diagnostics alarm, follow these steps:

1. In the "Program blocks" folder in the project navigation, select the function block (FB) for which you want to create a user diagnostics alarm and double-click the block to open it.
2. Insert a configuration of the outgoing and incoming user diagnostics alarm in the instruction window of the FB by calling the "WR_USMSG" alarm block twice (each in connection with a negative and a positive edge).
3. Double-click "PLC supervisions &amp; alarms" in the project navigation. Select the "Alarms" tab to open the alarm editor.
4. Select the "User diagnostics alarms" tab in the alarm editor.
5. Click in the table and select "Insert new alarm" in the shortcut menu.

#### Result

You have created a user diagnostics alarm.

### Editing user diagnostic alarms (S7-300, S7-400)

#### Requirement

You have created a user diagnostic alarm.

The alarm editor is open.

#### Procedure

To edit a user diagnostic alarm, follow these steps:

1. Enter the required texts and attributes in the appropriate columns.

### Deleting user diagnostic alarms (S7-300, S7-400)

You can delete a selected alarm. The texts you configured for this alarm are deleted and the alarm number is released for use.

#### Procedure

To delete a user diagnostics alarm, follow these steps:

1. Delete the alarm blocks inserted during creation in the instruction window of the FB.
2. In the alarm editor, select the corresponding row in the table and select "Delete" in the shortcut menu.

#### Result

The alarm is deleted. It is no longer displayed in the table.

### Insert associated values in alarms (S7-300, S7-400)

To add current information to alarms, e.g. from the process, you can insert associated values at any location within an alarm text.

#### Procedure

To insert an associated value into an alarm, follow these steps:

#### Alarm SFB for the S7-400 (e.g. Alarm, Alarm_8P)

There are 10 associated values whose length is limited to 12 bytes each. They cannot be addressed internally.

1. Configure a block as follows:   
   @&lt;No. of the associated value&gt;&lt;element type&gt;%&lt;format&gt;@.
2. Insert this block at the locations in the alarm text at which the associated value is to be shown.

#### Alarm SFC for the S7-300/400 (e.g. Alarm_S)

There is one associated value whose length is limited to 12 bytes. It can be addressed internally with the index and the element type.

1. Configure a block as follows:   
   @&lt;Index&gt;&lt;element type&gt;%&lt;format&gt;@.

   Index: Index in the associated value. The index is interpreted as an array index (starting with 1).

   The byte offset is calculated with the following formula:

   Offset = ((Index - 1) * data width (element type))

   Use only element types Y, W, X, or R. The element type is used here only to determine the data width. The display type is determined by the format specification.
2. Insert this block at the locations in the alarm text at which the associated value is to be shown.

---

**See also**

[Structure of associated values (S7-300, S7-400)](#structure-of-associated-values-s7-300-s7-400)
  
[Examples of associated values (S7-300, S7-400)](#examples-of-associated-values-s7-300-s7-400)

### Structure of associated values (S7-300, S7-400)

Associated values are comprised of the following:

#### Element type

This uniquely configures the data type of the associated value:

| Element type | Data type |
| --- | --- |
| Y | BYTE |
| W | WORD |
| X | DWORD |
| I | Integer |
| D | DINT |
| B | BOOL |
| C | CHAR |
| R | REAL |
| O | LREAL |

The element type only uniquely identifies the data type transferred by the AS. It is not used as Casting Operator.

#### Format

Determine the output format for the associated value on the display device. The format is preceded by the "%" sign. The following fixed formats apply to alarm texts:

| Format | Description |
| --- | --- |
| %[i]X | Hexadecimal number with i digits |
| %[i]u | Decimal number without sign with i digits |
| %[i]d | Decimal number with sign with i digits |
| %[i]b | Binary number with i digits |
| %[i][.y]f | Floating-point number with sign with y digits after the decimal point and total number of digits i |
| %[i]s | String (ANSI string) with i digits  Characters are printed up to the first 0 Byte (00Hex). |
| %t#&lt;Name of text list&gt; | Access to text list |

If the number of digits [i] is too small, the value is nevertheless output in full.

If the number of digits [i] is too large, an appropriate number of fill characters is output before the value.

If the number of digits [i] is too large and if a sign is output (for decimal/floating-point numbers), the number of fill characters is reduced by one. The same applies to periods or commas within floating-point numbers.

Example: Value = 1234.567 Format=%8.3f Output=1234.567; that is, no fill character is output even though there are only 7 digits.

> **Note**
>
> Please note that you can optionally enter "[i]" (without the square brackets).

---

**See also**

[Insert associated values in alarms (S7-300, S7-400)](#insert-associated-values-in-alarms-s7-300-s7-400)
  
[Examples of associated values (S7-300, S7-400)](#examples-of-associated-values-s7-300-s7-400)

### Examples of associated values (S7-300, S7-400)

#### Examples of associated values:

@1I%6d@: The value from associated value 1 is shown as a decimal number with a max. 6 digits.

@2R%6f@: The value "5.4", for instance from associated value 2, is shown as a fixed number of points "5.4" (three leading spaces).

@2R%2f@: The value "5.4", for instance from associated value 2, is shown as a fixed number of points "5.4" (if number of digits is too small then these are not cut off).

@1W%t#Textbib1@: Associated value 1 of the WORD data type is the index by which the text to be inserted is referenced in the Textbib1 text library.

Examples of formats and output values:

Value=255 Format=%5X Output="16#000FF"

Value=123 Format=%5u Output=" 123"

Value=-200 Format=%4d Output="-200"

Value=19 Format=%8b Output="2#00010011"

Value = 1234,567 Format=%8.3f Output="1234.567"; that is, no empty character is output even though there are only 7 digits.

> **Note**
>
> If you want to transfer more than one associated value to an ALARM_S block then you can transfer an array with a max. length of 12 bytes. These could be, e.g. maximum 12 Byte or Char, maximum 6 Word or Int or maximum 3 DWord, Real or Dint.

---

**See also**

[Insert associated values in alarms (S7-300, S7-400)](#insert-associated-values-in-alarms-s7-300-s7-400)
  
[Structure of associated values (S7-300, S7-400)](#structure-of-associated-values-s7-300-s7-400)

### Deleting associated values (S7-300, S7-400)

You can delete associated values by deleting the placeholder that represents an associated value in the alarm text.

#### Procedure:

Follow the steps below to delete associated values:

1. Find the placeholder in the alarm text that corresponds to the associated value you want to delete.  
   The placeholder starts with the "@" character followed by the index and element type by which you can recognize the associated value, then a format specification, and it ends with the "@" character.
2. Delete the placeholder you have found from the alarm text.

## Creating and editing alarms (S7-1500)

This section contains information on the following topics:

- [Creating program alarms (S7-1500)](#creating-program-alarms-s7-1500)
- [Editing program alarms in the alarm editor (S7-1500)](#editing-program-alarms-in-the-alarm-editor-s7-1500)
- [Editing program alarms in the program editor (S7-1500)](#editing-program-alarms-in-the-program-editor-s7-1500)
- [Deleting program alarms (S7-1500)](#deleting-program-alarms-s7-1500)
- [Editing the alarm type (S7-1500)](#editing-the-alarm-type-s7-1500)
- [Creating an instance DB and editing alarm instances (S7-1500)](#creating-an-instance-db-and-editing-alarm-instances-s7-1500)
- [Insert associated values in alarms (S7-1500)](#insert-associated-values-in-alarms-s7-1500)
- [Settings when entering associated values (S7-1500)](#settings-when-entering-associated-values-s7-1500)
- [Special features of associated values (S7-1500)](#special-features-of-associated-values-s7-1500)
- [Examples of associated values (S7-1500)](#examples-of-associated-values-s7-1500)
- [Deleting associated values (S7-1500)](#deleting-associated-values-s7-1500)

### Creating program alarms (S7-1500)

#### Requirement

You have created a function block.

#### Procedure

To create a program alarm, follow these steps:

1. In the "Program blocks" folder in the project tree, select the function block (FB) for which you want to create a program alarm and double-click the block to open it.
2. In the instruction window or network of the FB (depending on the block language), insert the call for the selected alarm block ("Program_Alarm"). It is available in the "Instructions" task card under "Extended instructions" &gt; "Alarms". The block interface is automatically provided with the necessary information in the "Static" area.
3. If necessary, change the alarm name in the dialog that opens.

   Result: The instruction part of the FB displays the input tags of the called alarm block, in this case the Program_Alarm block.
4. Repeat steps 2 through 3 for all alarm block calls in this FB.

Please note that you must specify the alarm class when you create alarms for S7-1500 CPUs. Indicates whether the alarm requires acknowledgment. Alarms that do not require acknowledgment can also be used only for information purposes.

As a result, there are three types of alarm:

- The alarm has to be acknowledged and has the status "incoming" or "outgoing".
- The alarm does not have to be acknowledged and has the status "incoming" or "outgoing".
- The alarm is used only for information purposes and has no status. The check mark must be set in the "Information only" column. In the alarm log, this alarm type has only the status "incoming" (rising edge), an outgoing (falling) edge is not shown.   
  The alarm type is displayed in HMI under "Control alarms".

> **Note**
>
> The default setting is "without acknowledgment".

---

**See also**

[Creating alarm classes (S7-300, S7-400, S7-1500)](#creating-alarm-classes-s7-300-s7-400-s7-1500)

### Editing program alarms in the alarm editor (S7-1500)

#### Requirement

You have created a program alarm.

#### Procedure

To edit program alarms, follow these steps:

1. Double-click "PLC supervisions &amp; alarms" in the project navigation. Select the "Alarms" tab. The alarm editor opens.
2. Enter the required texts and attributes in the appropriate columns.

---

**See also**

[Basics for locking/unlocking texts and attributes (S7-300, S7-400, S7-1500)](#basics-for-lockingunlocking-texts-and-attributes-s7-300-s7-400-s7-1500)
  
[Locking new alarms and show/hide interlock symbols (S7-300, S7-400, S7-1500)](#locking-new-alarms-and-showhide-interlock-symbols-s7-300-s7-400-s7-1500)

### Editing program alarms in the program editor (S7-1500)

#### Requirement

You have created a program alarm.

#### Procedure

To edit program alarms, follow these steps:

1. Select the appropriate line in the block interface.
2. Switch to the "Alarm" tab in the Inspector window.
3. Enter the required texts and attributes in the appropriate fields.

#### "Program_Alarm" alarm block

If you use the "Program_Alarm" alarm block, the additional "Configuration" tab is displayed in the Inspector window. You can enter additional associated values, which for example do not occur in texts, at the empty input channels SD_1 to SD_10.

For this, click the selection box next to the parameter and select the desired value.

---

**See also**

[Basics for locking/unlocking texts and attributes (S7-300, S7-400, S7-1500)](#basics-for-lockingunlocking-texts-and-attributes-s7-300-s7-400-s7-1500)
  
[Locking new alarms and show/hide interlock symbols (S7-300, S7-400, S7-1500)](#locking-new-alarms-and-showhide-interlock-symbols-s7-300-s7-400-s7-1500)

### Deleting program alarms (S7-1500)

#### Procedure

To delete a program alarm, follow these steps:

1. Open the block containing the alarm you want to delete.
2. Select the corresponding row in the block interface and select "Delete" in the shortcut menu.
3. Delete the alarm block from the instruction window or network (depending on the block language).

#### Result

The alarm is deleted.

### Editing the alarm type (S7-1500)

#### Procedure

To edit an alarm type, follow these steps:

1. Select the required alarm block.
2. Enter the texts you require or select the required attributes.

---

**See also**

[Alarm type and alarms (S7-300, S7-400, S7-1500)](#alarm-type-and-alarms-s7-300-s7-400-s7-1500)
  
[Basics for locking/unlocking texts and attributes (S7-300, S7-400, S7-1500)](#basics-for-lockingunlocking-texts-and-attributes-s7-300-s7-400-s7-1500)
  
[Locking new alarms and show/hide interlock symbols (S7-300, S7-400, S7-1500)](#locking-new-alarms-and-showhide-interlock-symbols-s7-300-s7-400-s7-1500)

### Creating an instance DB and editing alarm instances (S7-1500)

#### Requirement

You have already created an FB and created at least one alarm in it.

#### Procedure

To assign instance data blocks (DBs) to an alarm type and to edit the alarms for these DBs for specific instances, follow the steps below:

1. Double-click on "Add new block" in the project navigation, click on the "Data block (DB)" button that appears in the dialog and select the function block (alarm type) to which you want to assign the instance DB from the "Type" drop-down list.
2. Double-click "PLC supervisions &amp; alarms" in the project navigation. Select the "Alarms" tab to open the alarm configuration.
3. Enter the desired changes for the respective alarm instance.

#### Result

This completes the alarm configuration for the created instance DB.

---

**See also**

[Alarm type and alarms (S7-300, S7-400, S7-1500)](#alarm-type-and-alarms-s7-300-s7-400-s7-1500)
  
[Basics for locking/unlocking texts and attributes (S7-300, S7-400, S7-1500)](#basics-for-lockingunlocking-texts-and-attributes-s7-300-s7-400-s7-1500)
  
[Locking new alarms and show/hide interlock symbols (S7-300, S7-400, S7-1500)](#locking-new-alarms-and-showhide-interlock-symbols-s7-300-s7-400-s7-1500)

### Insert associated values in alarms (S7-1500)

To add current information to alarms, for example from the process, you can insert associated values at various positions within an alarm text.

#### Procedure using the shortcut menu

To insert an associated value into an alarm, follow these steps:

1. Open the shortcut menu at the desired position, and use the corresponding menu command to select whether you want to insert a keyword, a tag, or an entry from a text list.
2. Enter the desired parameters in the dialog that appears, and confirm your entries.

> **Note**
>
> You can configure associated values both in the alarm editor and the block editor. If you work in the alarm editor, you should have opened the block for which you are configuring the alarm in the block editor. Otherwise, only already configured tags, but no newly added or created tags, can be interconnected or shown in the "Tag" selection box.
>
> If you enter associated values in the alarm editor, you must be in edit mode (click the required box twice) to display the required shortcut menu.

#### Result

The associated value is integrated into the alarm.

If there is a syntax error, the text is displayed with a red background and must be corrected. Not every combination of tag and formatting is possible.

When tags and text list entries are entered, the "Address" and alarm parameter fields are automatically filled out. They are not displayed until the dialog is opened again. With open block editor, the associated value is added automatically at input channel SD1 to SD10.

> **Note**
>
> If you have set different project languages, the associated values are copied to all project languages. Any changes you make are automatically applied to all project languages. When translating the texts, make sure that the same order is adhered to in all the languages.
>
> Copying embedded data between different Program_Alarm blocks results in errors, unless the two blocks have an identical arrangement of SD tags of the same data type and format.

#### Procedure without the shortcut menu

You can insert associated values at any location within an alarm text or infotext. To do this, follow these steps:

1. Insert your "Program_Alarm" block in your PLC program.
2. Assign the tag whose value you want to display in the "Program_Alarm" alarm text or in the associated infotext to the SD input of the "Program_Alarm" block.
3. Double-click "PLC supervisions &amp; alarms" in the project tree. Select the "Alarms" &gt; "Program alarms" tab.
4. Select your new "Program_Alarm" and insert the reference to the required associated value in the format "@SD_number%format_information@" at the required location in the alarm text or infotext.

> **Note**
>
> If you have set different project languages, the associated values are not copied to all project languages. You must insert the associated values in the adapted classical notation for each language. There is no stipulation that the associated values must be in the same order in each language.

---

**See also**

[Settings when entering associated values (S7-1500)](#settings-when-entering-associated-values-s7-1500)
  
[Special features of associated values (S7-1500)](#special-features-of-associated-values-s7-1500)
  
[Structure of the associated values](Supervision%20of%20machinery%20and%20plants%20with%20ProDiag%20%28S7-1500%29.md#structure-of-the-associated-values)
  
[Examples of associated values (S7-1500)](#examples-of-associated-values-s7-1500)

### Settings when entering associated values (S7-1500)

You can insert associated values in alarms both in the alarm editor and the block editor. If you work in the alarm editor, you should have opened the block for which you are configuring the alarm in the block editor. As a result of this, the "Tag" selection box will display the available parameters, which you can then apply. If the block editor is closed, you will see only the previously used parameters.

#### Entering keyword

The possible keywords that you can define in the text are available for selection in the drop-down list.

#### Entering a text list entry as an associated value

You select the desired text list in the drop-down list. In the "Tag" selection box select the tag which includes the index for the text list during run time.

#### Entering a text list tag as an associated value

In the "Text list" selection box, select the tag that contains the index of the text list in the automation system. In the "Tag" selection box, select the tag that contains the index of the text list entry in the automation system.

#### Entering a tag as an associated value

You select the desired tag in the "Tag" selection box. The address and the alarm parameter are added automatically by the program. In the "Format" section, you must now define the display type suitable for the specified tag, the minimum length, and, if applicable, the number of decimal places.

> **Note**
>
> Projects created with an older version of the TIA Portal can still contain the manual notation with embedded associated values. This corresponds to the syntax @&lt;Number of the associated value&gt;%&lt;Format specification&gt;@. For information on the "Format specification" parameter, refer to [Structure of associated values](#structure-of-associated-values-s7-300-s7-400).
>
> We recommend that you use only the above described dialog boxes to enter associated values in new projects.
>
> When you use ARRAY accesses with tag index in the form #Program_Alarm_1[#myIndex] in your program, the specific ARRAY element to be used during runtime is not yet known at the time of programming. For this reason, when you select this type of ARRAY access in the program editor, the properties of the first ARRAY element are always displayed in the inspector window.

---

**See also**

[Keywords for alarm texts (S7-300, S7-400, S7-1500)](#keywords-for-alarm-texts-s7-300-s7-400-s7-1500)
  
[Insert associated values in alarms (S7-1500)](#insert-associated-values-in-alarms-s7-1500)

### Special features of associated values (S7-1500)

#### Upgrading older projects

Projects created with an older version of the TIA Portal can contain embedded associated values with different structures in the different project languages. The associated values may have a different order or may be missing in a different language. When a project of this type is upgraded, the order of the associated values is harmonized. It is based on the reference language set in the original project. In this case, it is recommended to have the translated texts checked and corrected.

#### Importing a translated text list &lt; V14

It may occur that you have exported, translated and re-imported a text list for alarms in an older version. If you try to import an old file in a current project (e.g. due to identical names), this is rejected due to data incompatibility.

### Examples of associated values (S7-1500)

#### Examples of associated values that can be entered in the shortcut menu:

**Keyword:**

&lt;Keyword: CpuName&gt;

The name of the CPU is entered as an associated value.

**Tag:**

&lt;Tag: #Temperature&gt;

The value of the "#Temperature" tag is displayed at this point in the alarm text.

**Text list entry:**

&lt;Text list: USER_1: "tag_1"&gt;

The content of the "tag_1" tag is used as index for the "USER_1" text list. The entry from the text list is displayed at this point in the alarm text.

**Text list tag:**

&lt;Text list: "tag_2"(SD_1):Tag: "tag_1"(SD_2)&gt;

"Tag_2" is for the index for the text list to be used, "Tag_1" is used as index for the entry.

> **Note**
>
> Note that text list variables are only output correctly on HMI devices if the "Central alarm management in the PLC" setting is activated! If not, errors are output when compiling the project.

#### Examples of associated values that can be entered without the shortcut menu:

@1%6d@: The value from associated value 1 (SD_1) is shown as a decimal number with maximum 6 digits.

@2%6f@: The value "5.4", for instance from associated value 2 (SD_2), is shown as a fixed number of points "5.4" (three leading spaces).

@2%2f@: The value "5.4", for instance from associated value 2 (SD_2), is shown as a fixed number of points "5.4" (if number of digits is too small then these are not cut off).

@10%t#Textbib1@: The associated value 10 (SD_10) is shown with the text to be inserted from the "Textbib1" text library.

**Examples of formats and output values:**

Value=255 Format=%5X Output="16#000FF"

Value=123 Format=%5u Output=" 123"

Value=-200 Format=%4d Output="-200"

Value=19 Format=%8b Output="2#00010011"

Value = 1234.567 Format=%8.3f Output="1234.567"; that is, no empty character is output even though there are only 7 digits.

---

**See also**

[Insert associated values in alarms (S7-1500)](#insert-associated-values-in-alarms-s7-1500)

### Deleting associated values (S7-1500)

#### Procedure:

Follow the steps below to delete associated values:

1. Open the "Configuration" tab in the program editor.
2. Select the required associated value and delete it.
3. Also delete the associated value from the alarm texts in the alarm editor.

Or

1. Select the required input channel in the program editor.
2. Delete the associated value.
3. Also delete the associated value from the alarm texts in the alarm editor.

## Texts and attributes (S7-300, S7-400, S7-1500)

This section contains information on the following topics:

- [Keywords for alarm texts (S7-300, S7-400, S7-1500)](#keywords-for-alarm-texts-s7-300-s7-400-s7-1500)
- [Entering texts (S7-300, S7-400, S7-1500)](#entering-texts-s7-300-s7-400-s7-1500)
- [Basics for locking/unlocking texts and attributes (S7-300, S7-400, S7-1500)](#basics-for-lockingunlocking-texts-and-attributes-s7-300-s7-400-s7-1500)
- [Locking new alarms and show/hide interlock symbols (S7-300, S7-400, S7-1500)](#locking-new-alarms-and-showhide-interlock-symbols-s7-300-s7-400-s7-1500)
- [Locking texts (S7-300, S7-400, S7-1500)](#locking-texts-s7-300-s7-400-s7-1500)
- [Locking attributes (S7-300, S7-400, S7-1500)](#locking-attributes-s7-300-s7-400-s7-1500)

### Keywords for alarm texts (S7-300, S7-400, S7-1500)

#### Overview of keywords for alarm texts

You can select or enter the following keywords in event texts, info texts, or additional texts. These are then replaced with their real values by the engineering system. Only manual notation is possible with S7-300/S7-400. With S7-1500 you can use manual notation as well as the selection method using the shortcut menu.

#### PLC name

Name of the configured PLC.

Example S7-1500: &lt;Keyword: CpuName&gt; = "PLC_1"

Example S7-300/S7-400/S7-1500: $$CpuName$$ = "PLC_1"

> **Note**
>
> If you are working with an R/H system, the keyword is replaced with the name of the R/H station.

#### Name of the instance DB

Location of the alarm instance, usually a data block.

Example S7-1500: &lt;Keyword: Instance&gt; = "Block_3_DB"

Example S7-300/S7-400/S7-1500: $$Instance$$ = "Block_3_DB"

#### FB nesting for alarm

If you are using nested blocks in the project, the tag path of the alarm-defining block is shown that leads from the function block from which the data block is generated through all multiple instances.

Example S7-1500: &lt;Keyword: Path&gt; = "myFB2\myFB1"

Example S7-300/S7-400/S7-1500: $$Path$$ = "myFB2\myFB1"

> **Note**
>
> For blocks that are not nested, the "Path" keyword is replaced with an empty string.

#### Name of the alarm

Name of the alarm.

Example S7-1500: &lt;Keyword: Name&gt; = "myAlarm"

Example S7-300/S7-400/S7-1500: $$Name$$ = "myAlarm"

> **Note**
>
> Keywords cannot be entered in text lists.

### Entering texts (S7-300, S7-400, S7-1500)

You can enter the texts for the alarm instances manually or you can use the default values which you input in the texts at the alarm type.. Click in the relevant row and type in the text. If you want to protect the text from being overwritten, click the option in the column. The texts can include line breaks.

> **Note**
>
> **Using the character @ in a text box**
>
> Please use the @ character only for declaring the associated values, for example @4%6d@. Also, if you use the @ character in the free text of a text field, you might not be able to resolve the associated values contained in the free text of the alarm under certain circumstances.

#### Text template from the alarm type

All the texts in the alarm type are available as a template for creating alarm texts. If the alarm type already contains a general text, all instances of this alarm type include the same attributes and texts. You can adapt it at the alarm instance, if necessary.

#### Event text

Event texts can be shown on all display devices.

#### Info text

The info text is a text that can be specified for certain display devices.

#### Additional texts

Additional texts are texts that can be displayed by certain display devices.

### Basics for locking/unlocking texts and attributes (S7-300, S7-400, S7-1500)

You can lock texts and attributes at the alarm type to prevent them from being altered at the alarm instances. As of version V13 SP1, the interlock symbols are not displayed by default and set automatically for newly generated alarms.

#### Locking the data for an alarm type

Use the alarm types as templates to facilitate creation of alarms.

- When you enter data (attributes and texts) for the alarm type, you can specify whether or not they are locked. If you lock data, the icon of a closed chain link is shown beside the input box. If the attribute is not locked, the chain link is open.
- If you lock data in the alarm type, you can no longer change this in the alarms of the specific instance. The data is simply displayed.
- If, however, you want to make changes, you will need to go back to the alarm type, cancel the lock and make any changes there.

> **Note**
>
> If you have edited alarm instances in the alarm editor in which the texts/attributes are not locked in the alarm type, a type icon is displayed in front of the relevant column. When you click on this icon, modified texts/attributes are reset to the values of the alarm type.

---

**See also**

[Locking new alarms and show/hide interlock symbols (S7-300, S7-400, S7-1500)](#locking-new-alarms-and-showhide-interlock-symbols-s7-300-s7-400-s7-1500)

### Locking new alarms and show/hide interlock symbols (S7-300, S7-400, S7-1500)

#### Show/hide interlock symbols

#### Procedure

To show or hide the interlock symbols, follow these steps:

1. Select the "Settings" command in the "Options" menu.  
   The "Settings" window is displayed in the work area.
2. Select the "PLC alarms" group in the area navigation, click the "Show interlock symbols" check box and set or remove the check mark. Setting the check mark causes the interlock symbols to be displayed; removing the check mark hides the symbols.

#### Result

The change is applied and does not have to explicitly saved.

> **Note**
>
> As default, the option is disabled.

#### Set/remove interlock for new program alarms

#### Procedure

To set or remove the interlock for new program alarms, follow these steps:

1. Select the "Settings" command in the "Options" menu.  
   The "Settings" window is displayed in the work area.
2. Select the "PLC alarms" group in the area navigation, click the "Show/hide interlock symbols on creation of a new program alarm" check box and set or remove the check mark.

> **Note**
>
> The option is activated by default.

### Locking texts (S7-300, S7-400, S7-1500)

#### "Locked" option in the alarm type

You can only lock texts at alarm types. The icon displayed beside the input field indicates whether or not they are locked. The locked texts in all alarm instances derived from the alarm type are write-protected.

#### Requirement

The interlocking symbols are activated.

> **Note**
>
> The order of the procedure described below is random.

#### Locking texts

Follow the steps below to lock texts:

- Start by editing the alarm types.
- Click on the icon beside the input box you want to lock.

  Result: The icon changes to a closed chain link.

#### Unlocking texts

To unlock texts, follow the steps below:

- Start by editing the alarm types.
- Click on the icon beside the input box you want to unlock.

  Result: The icon changes to an open chain link.

---

**See also**

[Basics for locking/unlocking texts and attributes (S7-300, S7-400, S7-1500)](#basics-for-lockingunlocking-texts-and-attributes-s7-300-s7-400-s7-1500)
  
[Locking new alarms and show/hide interlock symbols (S7-300, S7-400, S7-1500)](#locking-new-alarms-and-showhide-interlock-symbols-s7-300-s7-400-s7-1500)
  
[Entering texts (S7-300, S7-400, S7-1500)](#entering-texts-s7-300-s7-400-s7-1500)

### Locking attributes (S7-300, S7-400, S7-1500)

#### Locking attributes in the alarm type

You can only lock attributes at alarm types. The icon displayed beside the input field indicates whether or not they are locked. The locked attributes in all alarm instances derived from the alarm type are write-protected.

#### Requirement

The interlocking symbols are activated.

> **Note**
>
> The order of the procedure described below is random.

#### Locking attributes

Follow the steps below to lock attributes:

- Start by editing the alarm types.
- Click on the icon to the left of the input box you want to lock in the table.

  Result: The icon changes to a closed chain link.

#### Unlocking attributes

Follow the steps below to unlock attributes:

- Start by editing the alarm types.
- Click on the icon to the left of the input box you want to unlock in the table.

  Result: The icon changes to an open chain link.

---

**See also**

[Basics for locking/unlocking texts and attributes (S7-300, S7-400, S7-1500)](#basics-for-lockingunlocking-texts-and-attributes-s7-300-s7-400-s7-1500)
  
[Locking new alarms and show/hide interlock symbols (S7-300, S7-400, S7-1500)](#locking-new-alarms-and-showhide-interlock-symbols-s7-300-s7-400-s7-1500)

## Text lists for alarms (S7-300, S7-400, S7-1500)

This section contains information on the following topics:

- [Basics of alarm text lists (S7-300, S7-400, S7-1500)](#basics-of-alarm-text-lists-s7-300-s7-400-s7-1500)
- [Editing text lists for alarms (S7-300, S7-400, S7-1500)](#editing-text-lists-for-alarms-s7-300-s7-400-s7-1500)
- [Integrating texts from text lists in alarms (S7-300, S7-400, S7-1500)](#integrating-texts-from-text-lists-in-alarms-s7-300-s7-400-s7-1500)
- [Example of integrating texts from text lists in alarms (S7-300, S7-400, S7-1500)](#example-of-integrating-texts-from-text-lists-in-alarms-s7-300-s7-400-s7-1500)

### Basics of alarm text lists (S7-300, S7-400, S7-1500)

You can adapt existing text lists (user-defined and system-defined text lists) to your requirements and edit texts and attributes. You can then export the texts into the project language(s) you want to use and then import them.

> **Note**
>
> Note that the "Export" button is only enabled if at least one PLC message text list is selected.

If a signaling block which references a text list is copied into another program, you must either also copy the associated text lists, create another text list with the same name and contents, or change the associated value in the alarm text.

> **Note**
>
> Note that the names of text lists for messages are not permitted to contain any of the following special characters:
>
> \ / : * ? " &lt; &gt; | @
>
> If you reference a text list that contains one of these characters, a system error is detected. The text is displayed with a red background and must be corrected.

Detailed information on text lists is contained in the "Working with text lists" chapter.

---

**See also**

[Text lists](Editing%20project%20data.md#text-lists)
  
[Creating user-defined text lists](Editing%20project%20data.md#creating-user-defined-text-lists)
  
[Editing user-defined text lists](Editing%20project%20data.md#editing-user-defined-text-lists)
  
[Editing system-defined text lists](Editing%20project%20data.md#editing-system-defined-text-lists)
  
[Basics for exporting and importing alarm texts (S7-300, S7-400, S7-1500)](#basics-for-exporting-and-importing-alarm-texts-s7-300-s7-400-s7-1500)

### Editing text lists for alarms (S7-300, S7-400, S7-1500)

#### Requirement

- You have created a user-defined text list.

#### Procedure

Follow the steps below to edit user-defined text lists:

1. Double-click on the "PLC alarm text lists" below the device in the project navigation.

   The text list editor opens.
2. Select the text list you want to edit from the table.
3. Change the desired values.  
   You can change the previously created texts or insert new texts in an existing text list.

> **Note**
>
> Please note that text lists for messages are not permitted to contain any of the following special characters:
>
> \ / : * ? " &lt; &gt; | @
>
> If you reference a text list that contains one of these characters, a system error is detected. The text is displayed with a red background and must be corrected.

---

**See also**

[Editing system-defined text lists](Editing%20project%20data.md#editing-system-defined-text-lists)

### Integrating texts from text lists in alarms (S7-300, S7-400, S7-1500)

You can integrate texts from various text lists in an alarm. The texts can be positioned anywhere you want which means that they can be used in alarms in foreign languages.

#### Procedure S7-300/400

To integrate texts from text lists in alarms, follow the steps below:

1. Double-click "PLC supervisions &amp; alarms" in the project navigation. Select the "Alarms" tab. The alarm editor opens.
2. Put an associated value in the format @[Index][Data type]%t#[Text list]@ at the point in the alarm at which you want the text from the text list to appear. The data type must be WORD (W).

**Note**

S7-300/400: [Index] = e.g. 1, where 1 is the first associated value of the alarm.

#### Procedure S7-1500

To integrate texts from text lists in alarms, follow the steps below:

1. Double-click "PLC supervisions &amp; alarms" in the project navigation. Select the "Alarms" tab. The alarm editor opens.
2. Go to the point in the alarm at which you want the text from the text list to appear, and select "Insert a dynamic parameter (text list)" or "Insert a dynamic parameter (text list tag)" from the shortcut menu to insert a text list or a reference to a text list.
3. In the "Text list" selection box, first select the tag that will contain the index of the text list in the automation system. Then, in the "Tag" selection field, select the tag that will contain the index of the text list entry in the automation system.

**Note**

If you work in the alarm editor, you should have opened the block for which you are configuring the alarm in the block editor.

If you enter associated values in the alarm editor, you must be in edit mode (click the required box twice) to display the required shortcut menu.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| Note that selecting the text list tag can also be applied to the S7-300/400, but these PLCs will not resolve the tag. For S7-1500, the tag is only resolved for CPUs with a firmware version 2.9 or higher if the "Central alarm management in the PLC" setting is enabled. |  |

---

**See also**

[Structure of associated values (S7-300, S7-400)](#structure-of-associated-values-s7-300-s7-400)
  
[Example of integrating texts from text lists in alarms (S7-300, S7-400, S7-1500)](#example-of-integrating-texts-from-text-lists-in-alarms-s7-300-s7-400-s7-1500)

### Example of integrating texts from text lists in alarms (S7-300, S7-400, S7-1500)

S7-300/400: Configured alarm text: Pressure is @2W%t#USER_1@.

S7-1500: Configured alarm text: Pressure has &lt;Text list: USER_1: "tag_1"&gt;.

Text list with the name "USER_1":

| Index | German | English |
| --- | --- | --- |
| 1734 | zu hoch | too high |
| 1735 | zu niedrig | too low |

Assumption: The associated value of "tag_1" is supplied with the value 1734.

Result: The following alarm text is displayed in run time on the HMI on the operator panel (if the project language is set to "English"): Pressure is too high.

Assumption: The associated value of "tag_1" is supplied with the value 1735.

Result: The following alarm text is displayed in run time on the HMI on the operator panel (if the project language is set to "English"): Pressure is too low.

---

**See also**

[Integrating texts from text lists in alarms (S7-300, S7-400, S7-1500)](#integrating-texts-from-text-lists-in-alarms-s7-300-s7-400-s7-1500)

## Alarm classes (S7-300, S7-400, S7-1500)

This section contains information on the following topics:

- [Creating alarm classes (S7-300, S7-400, S7-1500)](#creating-alarm-classes-s7-300-s7-400-s7-1500)
- [Editing alarm classes (S7-300, S7-400, S7-1500)](#editing-alarm-classes-s7-300-s7-400-s7-1500)
- [Deleting alarm classes (S7-300, S7-400, S7-1500)](#deleting-alarm-classes-s7-300-s7-400-s7-1500)
- [Priority of the alarm class (S7-300, S7-400, S7-1500)](#priority-of-the-alarm-class-s7-300-s7-400-s7-1500)
- [Exporting and importing alarm classes (S7-300, S7-400, S7-1500)](#exporting-and-importing-alarm-classes-s7-300-s7-400-s7-1500)

### Creating alarm classes (S7-300, S7-400, S7-1500)

You can configure alarm classes to suit your purposes. You can create and edit them in the alarm class editor. An alarm can then by assigned to an alarm class in the alarm editor.

The system has already created two alarm classes, "Acknowledgment" (for alarms with acknowledgment), and "No acknowledgment" (for alarms without acknowledgment). Only the display name can be modified here.

A total of 16 alarm classes can be created to which you can assign the corresponding priority. The "With acknowledgment" property of the alarm classes indicates that it is mandatory to acknowledge the assigned alarms. The ID of the alarm class must be unique in the project, but can be changed (allowed range 33 to 48).

#### Requirement

You have opened the "Common data" folder in project navigation.

#### Procedure

To configure an alarm class, follow these steps:

1. Double click on the "Alarm classes" entry in project navigation.

   The alarm class editor opens.
2. Select "Insert new alarm class" in the shortcut menu.  
   Result: A new alarm class with an automatically assigned name is created.
3. If necessary, enter a different name for the new alarm class in the "Name" column.

   The language of the name you assign here is neutral.
4. If necessary, enter a display name in the "Display name" column. This name is translatable.
5. Specify whether or not alarms of this alarm class require acknowledgment in the "With acknowledgment" column.
6. If necessary, set a priority. This is only possible with user-defined alarm classes.   
   The priority is taken over for the alarm type.

> **Note**
>
> Please note that you must specify the alarm class when you create alarms for S7-1500 CPUs. Indicates whether the alarm requires acknowledgment.
>
> S7-1500: Program alarms for which the option "Information only" is selected should be set as briefly as possible. This avoids multiple archiving (alarm log) on download after changes to program alarm text.

### Editing alarm classes (S7-300, S7-400, S7-1500)

You can change the settings (name, ID, display name, priority or acknowledgment) of an alarm class at any time, even if alarms have already been assigned to this alarm class. The changes are applied automatically to the alarms (if the settings at the alarm were not overwritten).

#### Copying alarm classes

To copy alarm classes, follow these steps:

1. Select the row with the alarm class you want to copy.
2. Select "Copy" in the shortcut menu.
3. Select "Paste" in the shortcut menu.

#### Result

The copied alarm class is appended to the end of the table under a new name.

The name of the new alarm class is made up as follows:

&lt;old name&gt;_&lt;no.&gt;

no.: This is the lowest free natural number.

> **Note**
>
> - Please note that you must specify the alarm class when you create alarms for S7-1500 CPUs. Indicates whether the alarm requires acknowledgment.
> - You can only change the display name for alarm classes generated by the system.

### Deleting alarm classes (S7-300, S7-400, S7-1500)

Because you can only create up to 16 alarm classes, it is necessary to delete alarm classes that are no longer required.

#### Procedure

To delete an alarm class, follow these steps:

1. Double click on the "Alarm classes" entry in project navigation.

   The alarm class editor opens.
2. Select the required alarm class and click the "Delete" icon in the toolbar.

#### Result

The alarm class is deleted.

> **Note**
>
> Alarm classes generated by the system cannot be deleted.

### Priority of the alarm class (S7-300, S7-400, S7-1500)

You can define a priority (0 to 16) for every alarm type for program alarms and user diagnostics alarms. The priority of an alarm class is usually specified or changed in the alarm class editor, but it can be changed later in the alarm editor for individual alarms. The block assigned to the alarm may not be write-protected. When you create new alarms, the priority is set by default to "0".

#### Changing the priority for alarm types and alarms

If you change data for an alarm type later, these changes are automatically included in the instances. Exception: You have already changed this data in the instance.

The following table lists the possible actions and their effects:

| Initial status | Action | Result |
| --- | --- | --- |
| No alarm type exists. | The alarm type is created. | The priority of the alarm class in the alarm class editor and the priority at the alarm type in the alarm editor in the "Priority" column are identical. |
| The alarm type exists, the priority is not changed. | The alarm class of the alarm type is changed. | The priority of the alarm class in the alarm class editor and the priority at the alarm type in the alarm editor in the "Priority" column are identical. |
| The alarm type exists, the priority is not changed. | The priority of the alarm class is changed in the alarm class editor. | The priority of the alarm class in the alarm class editor and the priority at the alarm type in the alarm editor in the "Priority" column are identical. |
| The alarm type exists, the priority is not changed. | The alarm class is deleted in the alarm class editor. | The priority of the alarm type is set to "0" and is marked as "invalid". |
| The alarm type exists, the priority is not changed. | The priority is changed for the alarm type. | The priority of the alarm class in the alarm class editor and the priority at the alarm type in the alarm editor in the "Priority" column are different. |
| The alarm type exists, the priority for the alarm type was changed. | The alarm class of the instance is changed. | The priority of the alarm class in the alarm class editor and the priority at the instance in the alarm editor in the "Priority" column are different. |
| The alarm (instance) exists, the priority for the alarm type was changed. | The priority of the alarm class is changed. | The priority of the alarm class in the alarm class editor and the priority at the instance in the alarm editor in the "Priority" column are different. |
| The alarm (instance) exists, the priority for the alarm type was changed. | The alarm class is deleted in the alarm class editor. | The priority for the alarm type is displayed, the alarm class is marked as "invalid". |
| The alarm (instance) exists, the priority for the alarm type was changed. | The priority for the alarm type is changed to the same value as the priority of the alarm class. | The priority of the alarm class and the priority in the "Priority" column in the alarm editor are identical but not coupled (*). |
| The alarm (instance) exists, the priority for the alarm type was changed. | The priority for the alarm type is reset to the priority of the alarm class. | The priority of the alarm class and the priority in the "Priority" column in the alarm editor are identical. |

If you change the priority at the alarm later, the value is marked with an asterisk (*).

You can reset the changed values again at any time to the priority of the alarm class. To do this, select the "Reset to type alarm value" from the drop-down list.

### Exporting and importing alarm classes (S7-300, S7-400, S7-1500)

This section contains information on the following topics:

- [Basics for exporting and importing alarm classes (S7-300, S7-400, S7-1500)](#basics-for-exporting-and-importing-alarm-classes-s7-300-s7-400-s7-1500)
- [Exporting alarm classes (S7-300, S7-400, S7-1500)](#exporting-alarm-classes-s7-300-s7-400-s7-1500)
- [Importing alarm classes (S7-300, S7-400, S7-1500)](#importing-alarm-classes-s7-300-s7-400-s7-1500)

#### Basics for exporting and importing alarm classes (S7-300, S7-400, S7-1500)

##### Description

You can export the alarm classes of a project and import them into another project. The advantage of importing alarm classes is that they do not have to be created separately for each project.

The alarm classes are saved in a data file (*.dat).

#### Exporting alarm classes (S7-300, S7-400, S7-1500)

##### Requirement

A project is open.

##### Procedure

To export alarm classes, follow these steps:

1. In the project tree, click on the "Shared data" folder and double-click "Alarm classes".
2. In the alarm classes editor, click the "Export of alarm class settings" icon in the toolbar. The "Save as" dialog opens.
3. Select the path to which you want to save the export file.
4. Click the "Save" button.

##### Result

A .dat file is created at the selected memory location.

#### Importing alarm classes (S7-300, S7-400, S7-1500)

##### Requirement

The project into which you want to import the alarm classes is open.

##### Procedure

To import alarm classes, follow these steps:

1. In the project tree, click on the "Shared data" folder and double-click "Alarm classes".
2. In the alarm classes editor, click the "Import of alarm class settings" icon in the toolbar. The "Open" dialog opens.
3. Select the path where the file to be imported is stored.
4. Select the required .dat file.
5. Click the "Open" button.

> **Note**
>
> The "Import" icon is grayed out when the open project is read-only (e.g. reference object).
>
> If an error occurs during the import, an alarm is displayed and the process is aborted.

##### Result

The alarm classes are displayed.

## Exporting and importing alarm texts (S7-300, S7-400, S7-1500)

This section contains information on the following topics:

- [Basics for exporting and importing alarm texts (S7-300, S7-400, S7-1500)](#basics-for-exporting-and-importing-alarm-texts-s7-300-s7-400-s7-1500)
- [Exporting alarm texts (S7-300, S7-400, S7-1500)](#exporting-alarm-texts-s7-300-s7-400-s7-1500)
- [Importing alarm texts (S7-300, S7-400, S7-1500)](#importing-alarm-texts-s7-300-s7-400-s7-1500)

### Basics for exporting and importing alarm texts (S7-300, S7-400, S7-1500)

#### Introduction

You can export program alarm texts of the alarm type to a standardized XLSX format for editing with external table editors (for example, translation). Similarly, you can import these alarm texts edited with external table editors to the TIA Portal.

#### Format of the export file

The names of the column titles are fixed and should not be modified. The sorting order of columns can vary within the spreadsheet. The number of columns depends on the selection made during export. Each alarm is assigned a separate row in the file.

The following table specifies the contents expected for the individual columns:

| Column | Explanation |  | Translation-related |
| --- | --- | --- | --- |
| Location | Name of the block to which the alarm is assigned. |  | No |
| Alarm name | Name of the alarm |  | No |
| "Alarm text" - English (United States) / [en-US] / Event text | Event text of the alarm | The field designation contains a language ID. Alarm texts must be assigned a language ID for import.  An expression with a reference ID will be added to the text for S7-1500 if the alarm text has an associated value. Example: text &lt;field ref="0" /&gt;. The associated value is assigned to an alarm text with the ID. | Yes |
| "Info text" - English (United States) / [en-US] / Info text | Info text of the alarm | Yes |  |
| "Additional text" - English (United States) / [en-US] / Additional text | Additional text of the alarm | Yes |  |
| FieldInfo (for S7-1500 only) | Specifies whether the alarm text contains associated values. The settings are separated by a semicolon ";".   Example for associated values with S7-1500:  Tag: &lt;ref id = 0; type = AlarmTag; Tag = Tag1; DisplayType = Decimal; Length = 5;&gt;  Text list: &lt;ref id = 1; type = CommonTextList; TextList = Textlist1; Tag = tag 2; Length = 5;&gt; |  | No |

#### Example for S7-300/400

The figure below shows an excerpt of an export file for S7-300/400 as an example.

![Example for S7-300/400](images/72353773579_DV_resource.Stream@PNG-de-DE.PNG)

> **Note**
>
> Note that the keywords (enclosed by $$ or @) are also not to be translated in the example above.

#### Example for S7-1500

The figure below shows an excerpt of an export file for S7-1500 as an example.

![Example for S7-1500](images/89024045323_DV_resource.Stream@PNG-de-DE.png)

#### Translating the alarm texts in an external table editor

The texts are translated in the respective column with the language ID specified for the language to be translated. When translating the texts, make sure that the same order of the associated values is adhered to in all the languages; otherwise, the texts can no longer be imported!

---

**See also**

[Exporting alarm texts (S7-300, S7-400, S7-1500)](#exporting-alarm-texts-s7-300-s7-400-s7-1500)
  
[Importing alarm texts (S7-300, S7-400, S7-1500)](#importing-alarm-texts-s7-300-s7-400-s7-1500)
  
[Special features of associated values (S7-1500)](#special-features-of-associated-values-s7-1500)

### Exporting alarm texts (S7-300, S7-400, S7-1500)

#### Requirement

The alarm editor is open.

#### Procedure

To export alarm texts, follow these steps:

1. Click the "Export" button in the "Program alarms" tab in the toolbar. The "Export alarm texts" dialog box opens.
2. Select the path to which you want to save the export file.
3. Select the required languages.
4. If necessary, specify if event texts, info texts and/or additional texts are to be exported as well.
5. Click "OK".

> **Note**
>
> - All project languages selected in TIA Portal are displayed in the export dialog. You can add additional project languages in the project language editor so that they are displayed in this selection. All available project languages are selected by default; you can deselect languages for which the current translation process is of no importance.
> - Only export data to an area that is protected with corresponding access mechanisms.

---

**See also**

[Basics for exporting and importing alarm texts (S7-300, S7-400, S7-1500)](#basics-for-exporting-and-importing-alarm-texts-s7-300-s7-400-s7-1500)

### Importing alarm texts (S7-300, S7-400, S7-1500)

#### Requirement

The alarm editor is open.

#### Procedure

To import alarm texts, follow these steps:

1. Click the "Import" button in the "Program alarms" tab in the toolbar. The "Import alarm texts" dialog box opens.
2. Select the path in which you want to save the file to be imported and click "Import".
3. In the next dialog, select the required language(s).
4. Click "OK".

> **Note**
>
> - You do not have to use the same settings for import as you do for export.
> - Only import files from trusted sources.

---

**See also**

[Basics for exporting and importing alarm texts (S7-300, S7-400, S7-1500)](#basics-for-exporting-and-importing-alarm-texts-s7-300-s7-400-s7-1500)
